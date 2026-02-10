"""
Tests for Placeholder Processor

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from hypothesis import given, settings, strategies as st

from src.placeholder_processor import (
    Placeholder,
    Replacement,
    ProcessingResult,
    PlaceholderProcessor
)


# Mock data source adapter for testing
class MockDataSourceAdapter:
    """Mock adapter for testing placeholder replacement."""
    
    def __init__(self, data: dict):
        """
        Initialize with mock data.
        
        Args:
            data: Dictionary mapping field paths to values
        """
        self.data = data
    
    def get_field(self, field_path: str):
        """Get field value from mock data."""
        return self.data.get(field_path)


# Hypothesis strategies for generating test data
@st.composite
def valid_placeholder_string(draw):
    """Generate a valid placeholder string."""
    source = draw(st.text(
        alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd'), whitelist_characters='_'),
        min_size=1,
        max_size=15
    ).filter(lambda x: x and x[0].isalpha()))
    
    # Generate field path (can have dots for nested fields)
    num_parts = draw(st.integers(min_value=1, max_value=3))
    field_parts = []
    for _ in range(num_parts):
        part = draw(st.text(
            alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd'), whitelist_characters='_'),
            min_size=1,
            max_size=15
        ).filter(lambda x: x and x[0].isalpha()))
        field_parts.append(part)
    
    field = '.'.join(field_parts)
    
    # Add optional whitespace
    ws_before = draw(st.text(alphabet=' \t', max_size=3))
    ws_after = draw(st.text(alphabet=' \t', max_size=3))
    
    return f'{{{{{ws_before}{source}.{field}{ws_after}}}}}'


@st.composite
def template_with_placeholders(draw):
    """Generate template content with placeholders."""
    num_lines = draw(st.integers(min_value=1, max_value=20))
    lines = []
    placeholder_info = []
    
    for line_num in range(1, num_lines + 1):
        has_placeholder = draw(st.booleans())
        
        if has_placeholder:
            placeholder = draw(valid_placeholder_string())
            # Placeholder on its own line (valid)
            lines.append(placeholder)
            placeholder_info.append((line_num, placeholder))
        else:
            # Regular content line
            content = draw(st.text(
                alphabet=st.characters(blacklist_characters='{}\n'),
                max_size=50
            ))
            lines.append(content)
    
    return {
        'content': '\n'.join(lines),
        'placeholders': placeholder_info
    }


class TestPlaceholderDataModel:
    """Unit tests for Placeholder data model."""
    
    def test_placeholder_creation(self):
        """Test creating a Placeholder instance."""
        placeholder = Placeholder(
            raw='{{ netbox.device_name }}',
            source='netbox',
            field='device_name',
            line_number=5
        )
        
        assert placeholder.raw == '{{ netbox.device_name }}'
        assert placeholder.source == 'netbox'
        assert placeholder.field == 'device_name'
        assert placeholder.line_number == 5
    
    def test_placeholder_parse(self):
        """Test parsing placeholder from regex match."""
        import re
        pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        
        text = '{{ netbox.device_name }}'
        match = pattern.search(text)
        
        placeholder = Placeholder.parse(match, 10)
        
        assert placeholder.raw == '{{ netbox.device_name }}'
        assert placeholder.source == 'netbox'
        assert placeholder.field == 'device_name'
        assert placeholder.line_number == 10
    
    def test_placeholder_parse_nested_field(self):
        """Test parsing placeholder with nested field path."""
        import re
        pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        
        text = '{{ netbox.site.location.name }}'
        match = pattern.search(text)
        
        placeholder = Placeholder.parse(match, 15)
        
        assert placeholder.source == 'netbox'
        assert placeholder.field == 'site.location.name'


class TestReplacementDataModel:
    """Unit tests for Replacement data model."""
    
    def test_replacement_creation(self):
        """Test creating a Replacement instance."""
        replacement = Replacement(
            placeholder='{{ netbox.device_name }}',
            value='server-01',
            source='netbox',
            line_number=5
        )
        
        assert replacement.placeholder == '{{ netbox.device_name }}'
        assert replacement.value == 'server-01'
        assert replacement.source == 'netbox'
        assert replacement.line_number == 5


class TestProcessingResultDataModel:
    """Unit tests for ProcessingResult data model."""
    
    def test_processing_result_creation(self):
        """Test creating a ProcessingResult instance."""
        result = ProcessingResult(
            content='Processed content',
            replacements=[],
            warnings=[],
            errors=[]
        )
        
        assert result.content == 'Processed content'
        assert result.replacements == []
        assert result.warnings == []
        assert result.errors == []
    
    def test_processing_result_with_data(self):
        """Test ProcessingResult with replacements and warnings."""
        replacement = Replacement(
            placeholder='{{ netbox.device_name }}',
            value='server-01',
            source='netbox',
            line_number=5
        )
        
        result = ProcessingResult(
            content='Device: server-01',
            replacements=[replacement],
            warnings=['Warning message'],
            errors=[]
        )
        
        assert len(result.replacements) == 1
        assert len(result.warnings) == 1
        assert result.replacements[0].value == 'server-01'


class TestPlaceholderDetection:
    """Tests for placeholder detection functionality."""
    
    @settings(max_examples=100)
    @given(template_data=template_with_placeholders())
    def test_property_3_placeholder_detection_and_parsing(self, template_data):
        """
        Feature: handbook-generator, Property 3: Placeholder Detection and Parsing
        
        For any template content containing placeholders in the format "{{ source.field }}",
        the system should correctly identify all placeholders and extract both the source
        and field components.
        
        Validates: Requirements 3.1, 3.4
        """
        processor = PlaceholderProcessor()
        content = template_data['content']
        expected_placeholders = template_data['placeholders']
        
        # Find placeholders
        found_placeholders = processor.find_placeholders(content)
        
        # Verify correct number of placeholders found
        assert len(found_placeholders) == len(expected_placeholders), \
            f"Expected {len(expected_placeholders)} placeholders, found {len(found_placeholders)}"
        
        # Verify each placeholder is correctly parsed
        for placeholder in found_placeholders:
            # Verify placeholder has source and field
            assert placeholder.source, "Placeholder source should not be empty"
            assert placeholder.field, "Placeholder field should not be empty"
            
            # Verify source and field are alphanumeric (with underscores and dots for field)
            assert placeholder.source.replace('_', '').isalnum(), \
                f"Source should be alphanumeric: {placeholder.source}"
            
            # Field can have dots for nested paths
            field_parts = placeholder.field.split('.')
            for part in field_parts:
                assert part.replace('_', '').isalnum(), \
                    f"Field part should be alphanumeric: {part}"
            
            # Verify line number is valid
            assert placeholder.line_number > 0, "Line number should be positive"
            assert placeholder.line_number <= len(content.split('\n')), \
                "Line number should not exceed content line count"
    
    def test_find_placeholders_basic(self):
        """Test basic placeholder detection."""
        processor = PlaceholderProcessor()
        content = """# Header
{{ netbox.device_name }}
Some text
{{ netbox.site_name }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 2
        assert placeholders[0].source == 'netbox'
        assert placeholders[0].field == 'device_name'
        assert placeholders[0].line_number == 2
        assert placeholders[1].source == 'netbox'
        assert placeholders[1].field == 'site_name'
        assert placeholders[1].line_number == 4
    
    def test_find_placeholders_nested_field(self):
        """Test detection of placeholders with nested field paths."""
        processor = PlaceholderProcessor()
        content = '{{ netbox.site.location.name }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'netbox'
        assert placeholders[0].field == 'site.location.name'
    
    def test_find_placeholders_with_whitespace(self):
        """Test detection of placeholders with whitespace."""
        processor = PlaceholderProcessor()
        content = '{{  netbox.device_name  }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'netbox'
        assert placeholders[0].field == 'device_name'
    
    def test_find_placeholders_none(self):
        """Test detection with no placeholders."""
        processor = PlaceholderProcessor()
        content = """# Header
Just regular text
No placeholders here
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 0


class TestPlaceholderValidation:
    """Tests for placeholder validation functionality."""
    
    @settings(max_examples=100)
    @given(
        placeholder_text=valid_placeholder_string(),
        has_extra_content=st.booleans(),
        extra_content=st.text(
            alphabet=st.characters(
                blacklist_characters='\n\r\t ',
                min_codepoint=33  # Exclude all whitespace and control characters
            ),
            min_size=1,
            max_size=20
        )
    )
    def test_property_4_placeholder_line_validation(self, placeholder_text, has_extra_content, extra_content):
        """
        Feature: handbook-generator, Property 4: Placeholder Line Validation
        
        For any placeholder in a template, if the placeholder is not the only statement
        on its line, the system should generate a warning with the filename and line number.
        
        Validates: Requirements 3.2, 3.3
        """
        processor = PlaceholderProcessor()
        
        # Create line with or without extra content
        if has_extra_content:
            line = f'{extra_content} {placeholder_text}'
        else:
            line = placeholder_text
        
        # Find placeholder in line
        placeholders = processor.find_placeholders(line)
        
        if len(placeholders) > 0:
            placeholder = placeholders[0]
            
            # Validate placeholder line
            warning = processor.validate_placeholder_line(line, placeholder)
            
            if has_extra_content:
                # Should generate warning
                assert warning is not None, \
                    "Should generate warning when placeholder is not alone on line"
                assert str(placeholder.line_number) in warning, \
                    "Warning should include line number"
            else:
                # Should not generate warning
                assert warning is None, \
                    "Should not generate warning when placeholder is alone on line"
    
    def test_validate_placeholder_line_valid(self):
        """Test validation with placeholder alone on line."""
        processor = PlaceholderProcessor()
        line = '{{ netbox.device_name }}'
        
        placeholders = processor.find_placeholders(line)
        placeholder = placeholders[0]
        
        warning = processor.validate_placeholder_line(line, placeholder)
        
        assert warning is None
    
    def test_validate_placeholder_line_invalid(self):
        """Test validation with extra content on line."""
        processor = PlaceholderProcessor()
        line = 'Device: {{ netbox.device_name }}'
        
        placeholders = processor.find_placeholders(line)
        placeholder = placeholders[0]
        
        warning = processor.validate_placeholder_line(line, placeholder)
        
        assert warning is not None
        assert 'only content' in warning.lower() or 'not_alone_in_line' in warning.lower()
    
    def test_validate_placeholder_line_with_whitespace(self):
        """Test validation with only whitespace around placeholder."""
        processor = PlaceholderProcessor()
        line = '   {{ netbox.device_name }}   '
        
        placeholders = processor.find_placeholders(line)
        placeholder = placeholders[0]
        
        warning = processor.validate_placeholder_line(line, placeholder)
        
        assert warning is None


class TestTemplatePassThrough:
    """Tests for template pass-through functionality."""
    
    @settings(max_examples=100)
    @given(
        content=st.text(
            alphabet=st.characters(blacklist_characters='{}'),
            min_size=0,
            max_size=500
        )
    )
    def test_property_5_template_pass_through(self, content):
        """
        Feature: handbook-generator, Property 5: Template Pass-Through
        
        For any template content without placeholders, the system should output
        the content unchanged.
        
        Validates: Requirements 3.5
        """
        processor = PlaceholderProcessor()
        
        # Process template
        result = processor.process_template(content)
        
        # Verify content is unchanged
        assert result.content == content, \
            "Content without placeholders should remain unchanged"
        
        # Verify no replacements were made
        assert len(result.replacements) == 0, \
            "No replacements should be made for content without placeholders"
        
        # Verify no warnings or errors
        assert len(result.warnings) == 0, \
            "No warnings should be generated for content without placeholders"
        assert len(result.errors) == 0, \
            "No errors should be generated for content without placeholders"
    
    def test_process_template_no_placeholders(self):
        """Test processing template without placeholders."""
        processor = PlaceholderProcessor()
        content = """# Header
This is regular content
No placeholders here
"""
        
        result = processor.process_template(content)
        
        assert result.content == content
        assert len(result.replacements) == 0
        assert len(result.warnings) == 0



class TestPlaceholderReplacement:
    """Tests for placeholder replacement functionality."""
    
    @settings(max_examples=100)
    @given(
        num_placeholders=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_8_placeholder_replacement(self, num_placeholders, data):
        """
        Feature: handbook-generator, Property 8: Placeholder Replacement
        
        For any placeholder with successfully retrieved data, the system should replace
        the placeholder with the actual value in the output.
        
        Validates: Requirements 4.5
        """
        # Generate placeholders and corresponding data
        placeholders_data = {}
        template_lines = []
        
        for i in range(num_placeholders):
            source = data.draw(st.sampled_from(['netbox', 'database', 'api']))
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd'), whitelist_characters='_'),
                min_size=1,
                max_size=15
            ).filter(lambda x: x and x[0].isalpha()))
            value = data.draw(st.text(min_size=1, max_size=50))
            
            placeholder_text = f'{{{{ {source}.{field} }}}}'
            template_lines.append(placeholder_text)
            
            # Store data for this source
            if source not in placeholders_data:
                placeholders_data[source] = {}
            placeholders_data[source][field] = value
        
        template_content = '\n'.join(template_lines)
        
        # Create mock adapters
        mock_adapters = {}
        for source, fields in placeholders_data.items():
            mock_adapters[source] = MockDataSourceAdapter(fields)
        
        # Process template
        processor = PlaceholderProcessor(data_sources=mock_adapters)
        result = processor.process_template(template_content)
        
        # Verify all placeholders were replaced
        assert len(result.replacements) == num_placeholders, \
            f"Expected {num_placeholders} replacements, got {len(result.replacements)}"
        
        # Verify each replacement has correct value
        for replacement in result.replacements:
            # Extract source and field from placeholder
            import re
            match = re.search(r'\{\{\s*(\w+)\.(\w+)\s*\}\}', replacement.placeholder)
            if match:
                source = match.group(1)
                field = match.group(2)
                expected_value = placeholders_data[source][field]
                
                assert replacement.value == expected_value, \
                    f"Replacement value mismatch: expected '{expected_value}', got '{replacement.value}'"
        
        # Verify placeholders are no longer in content
        for line in result.content.split('\n'):
            assert '{{' not in line, \
                f"Placeholder not replaced in line: {line}"
    
    def test_replace_placeholder_success(self):
        """Test successful placeholder replacement."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        placeholder = Placeholder(
            raw='{{ netbox.device_name }}',
            source='netbox',
            field='device_name',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value == 'server-01'
        assert warning is None
    
    def test_process_template_with_replacement(self):
        """Test processing template with successful replacements."""
        mock_adapter = MockDataSourceAdapter({
            'device_name': 'server-01',
            'site_name': 'datacenter-1'
        })
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """# Device Information
{{ netbox.device_name }}
Location: {{ netbox.site_name }}
"""
        
        result = processor.process_template(content)
        
        assert len(result.replacements) == 2
        assert 'server-01' in result.content
        assert 'datacenter-1' in result.content
        assert '{{' not in result.content


class TestMissingFieldHandling:
    """Tests for missing field handling."""
    
    @settings(max_examples=100)
    @given(
        num_valid_fields=st.integers(min_value=0, max_value=5),
        num_missing_fields=st.integers(min_value=1, max_value=5),
        data=st.data()
    )
    def test_property_7_missing_field_handling(self, num_valid_fields, num_missing_fields, data):
        """
        Feature: handbook-generator, Property 7: Missing Field Handling
        
        For any placeholder referencing a non-existent field, the system should generate
        a warning and leave the placeholder unchanged in the output.
        
        Validates: Requirements 4.4
        """
        # Generate valid and missing fields
        valid_fields = {}
        template_lines = []
        expected_warnings = 0
        
        source = 'netbox'
        
        # Add valid fields
        for i in range(num_valid_fields):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=15
            ).filter(lambda x: x and x[0].isalpha()))
            value = data.draw(st.text(min_size=1, max_size=50))
            
            placeholder_text = f'{{{{ {source}.{field} }}}}'
            template_lines.append(placeholder_text)
            valid_fields[field] = value
        
        # Add missing fields
        for i in range(num_missing_fields):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=15
            ).filter(lambda x: x and x[0].isalpha() and x not in valid_fields))
            
            placeholder_text = f'{{{{ {source}.{field} }}}}'
            template_lines.append(placeholder_text)
            expected_warnings += 1
        
        template_content = '\n'.join(template_lines)
        
        # Create mock adapter with only valid fields
        mock_adapter = MockDataSourceAdapter(valid_fields)
        processor = PlaceholderProcessor(data_sources={source: mock_adapter})
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify warnings were generated for missing fields
        assert len(result.warnings) >= expected_warnings, \
            f"Expected at least {expected_warnings} warnings, got {len(result.warnings)}"
        
        # Verify missing field placeholders remain in content
        missing_field_count = 0
        for line in result.content.split('\n'):
            if '{{' in line:
                missing_field_count += 1
        
        assert missing_field_count == num_missing_fields, \
            f"Expected {num_missing_fields} unchanged placeholders, found {missing_field_count}"
        
        # Verify valid fields were replaced
        assert len(result.replacements) == num_valid_fields, \
            f"Expected {num_valid_fields} replacements, got {len(result.replacements)}"
    
    def test_replace_placeholder_missing_field(self):
        """Test replacement with missing field."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        placeholder = Placeholder(
            raw='{{ netbox.missing_field }}',
            source='netbox',
            field='missing_field',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value is None
        assert warning is not None
        assert 'field_not_found' in warning.lower() or 'not found' in warning.lower()
    
    def test_replace_placeholder_unknown_source(self):
        """Test replacement with unknown data source."""
        processor = PlaceholderProcessor(data_sources={})
        
        placeholder = Placeholder(
            raw='{{ unknown.field }}',
            source='unknown',
            field='field',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value is None
        assert warning is not None
        assert 'unknown_data_source' in warning.lower() or 'unknown data source' in warning.lower()
    
    def test_process_template_with_missing_field(self):
        """Test processing template with missing field."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """# Device Information
{{ netbox.device_name }}
{{ netbox.missing_field }}
"""
        
        result = processor.process_template(content)
        
        assert len(result.replacements) == 1
        assert len(result.warnings) >= 1
        assert 'server-01' in result.content
        assert '{{ netbox.missing_field }}' in result.content



class TestAdapterRouting:
    """Tests for data source adapter routing."""
    
    @settings(max_examples=100)
    @given(
        num_sources=st.integers(min_value=1, max_value=5),
        num_placeholders=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_21_data_source_adapter_routing(self, num_sources, num_placeholders, data):
        """
        Feature: handbook-generator, Property 21: Data Source Adapter Routing
        
        For any placeholder with a specified source (e.g., "netbox"), the system should
        route the data request to the corresponding adapter; for unknown sources, it should
        generate a warning listing available sources.
        
        Validates: Requirements 11.2, 11.3
        """
        # Generate available data sources
        available_sources = []
        mock_adapters = {}
        
        for i in range(num_sources):
            source_name = data.draw(st.sampled_from([
                'netbox', 'database', 'api', 'ldap', 'config'
            ]))
            if source_name not in available_sources:
                available_sources.append(source_name)
                # Create mock adapter with some data
                mock_adapters[source_name] = MockDataSourceAdapter({
                    'test_field': f'value_from_{source_name}'
                })
        
        # Generate placeholders with both known and unknown sources
        template_lines = []
        expected_known_sources = 0
        expected_unknown_sources = 0
        
        for i in range(num_placeholders):
            use_known_source = data.draw(st.booleans())
            
            if use_known_source and available_sources:
                # Use a known source
                source = data.draw(st.sampled_from(available_sources))
                field = 'test_field'
                expected_known_sources += 1
            else:
                # Use an unknown source
                source = data.draw(st.sampled_from([
                    'unknown1', 'unknown2', 'unknown3', 'missing'
                ]))
                field = 'test_field'
                if source not in available_sources:
                    expected_unknown_sources += 1
            
            placeholder_text = f'{{{{ {source}.{field} }}}}'
            template_lines.append(placeholder_text)
        
        template_content = '\n'.join(template_lines)
        
        # Create processor with mock adapters
        processor = PlaceholderProcessor(data_sources=mock_adapters)
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify routing behavior
        # Known sources should result in replacements (or warnings if field not found)
        # Unknown sources should result in warnings about unknown source
        
        # Count warnings about unknown sources
        unknown_source_warnings = sum(
            1 for w in result.warnings 
            if 'unknown data source' in w.lower()
        )
        
        # Verify warnings were generated for unknown sources
        assert unknown_source_warnings == expected_unknown_sources, \
            f"Expected {expected_unknown_sources} unknown source warnings, got {unknown_source_warnings}"
        
        # Verify warnings list available sources
        for warning in result.warnings:
            if 'unknown data source' in warning.lower():
                assert 'available sources' in warning.lower(), \
                    "Warning should list available sources"
                # Check that at least one available source is mentioned
                sources_mentioned = any(source in warning for source in available_sources)
                assert sources_mentioned or len(available_sources) == 0, \
                    "Warning should mention available sources"
    
    def test_adapter_routing_known_source(self):
        """Test routing to known data source."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        placeholder = Placeholder(
            raw='{{ netbox.device_name }}',
            source='netbox',
            field='device_name',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value == 'server-01'
        assert warning is None
    
    def test_adapter_routing_unknown_source(self):
        """Test routing to unknown data source."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        placeholder = Placeholder(
            raw='{{ unknown.field }}',
            source='unknown',
            field='field',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value is None
        assert warning is not None
        assert 'unknown_data_source' in warning.lower() or 'unknown data source' in warning.lower()
        assert 'available sources' in warning.lower()
        assert 'netbox' in warning
    
    def test_adapter_routing_multiple_sources(self):
        """Test routing with multiple data sources."""
        mock_netbox = MockDataSourceAdapter({'device_name': 'server-01'})
        mock_database = MockDataSourceAdapter({'user_count': '42'})
        
        processor = PlaceholderProcessor(data_sources={
            'netbox': mock_netbox,
            'database': mock_database
        })
        
        content = """# Information
{{ netbox.device_name }}
{{ database.user_count }}
{{ unknown.field }}
"""
        
        result = processor.process_template(content)
        
        # Should have 2 successful replacements
        assert len(result.replacements) == 2
        
        # Should have 1 warning for unknown source
        assert len(result.warnings) >= 1
        
        # Verify content
        assert 'server-01' in result.content
        assert '42' in result.content
        assert '{{ unknown.field }}' in result.content
    
    def test_adapter_routing_no_sources(self):
        """Test routing when no data sources are configured."""
        processor = PlaceholderProcessor(data_sources={})
        
        placeholder = Placeholder(
            raw='{{ netbox.device_name }}',
            source='netbox',
            field='device_name',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value is None
        assert warning is not None
        assert 'unknown_data_source' in warning.lower() or 'unknown data source' in warning.lower()
        assert 'none' in warning.lower()



class TestMetadataPlaceholders:
    """Tests for metadata placeholder handling."""
    
    @settings(max_examples=100)
    @given(
        has_version_in_metadata=st.booleans(),
        custom_version=st.text(
            alphabet=st.characters(whitelist_categories=('Nd',), whitelist_characters='.-'),
            min_size=1,
            max_size=20
        ).filter(lambda x: x and x[0].isdigit()),
        has_author_in_metadata=st.booleans(),
        custom_author=st.text(min_size=1, max_size=100)
    )
    def test_property_14_version_number_fallback(
        self, 
        has_version_in_metadata, 
        custom_version,
        has_author_in_metadata,
        custom_author
    ):
        """
        Feature: handbook-generator, Property 14: Version Number Fallback
        
        For any metadata template processing, if a version number is specified in the
        configuration, use it; otherwise, use "1.0.0" as the default.
        
        Validates: Requirements 7.4
        """
        # Create metadata dictionary
        metadata = {}
        if has_version_in_metadata:
            metadata['version'] = custom_version
        if has_author_in_metadata:
            metadata['author'] = custom_author
        
        # Create processor with metadata
        processor = PlaceholderProcessor(metadata=metadata)
        
        # Create template with metadata placeholders
        template_content = """# Handbook Metadata

Version: {{ metadata.version }}
Author: {{ metadata.author }}
Date: {{ metadata.date }}
"""
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify version replacement
        if has_version_in_metadata:
            # Should use custom version
            assert custom_version in result.content, \
                f"Custom version '{custom_version}' should be in content"
        else:
            # Should use default version "0.0.6" from src/__init__.py
            assert '0.0.6' in result.content, \
                "Default version '0.0.6' should be used when not specified"
        
        # Verify author replacement
        if has_author_in_metadata:
            # Should use custom author
            assert custom_author in result.content, \
                f"Custom author '{custom_author}' should be in content"
        else:
            # Should use default author
            default_author = 'Andreas Huemmer [andreas.huemmer@adminsend.de]'
            assert default_author in result.content, \
                f"Default author should be used when not specified"
        
        # Verify date replacement (should always work)
        # Date format: YYYY-MM-DD
        import re
        date_pattern = r'\d{4}-\d{2}-\d{2}'
        assert re.search(date_pattern, result.content), \
            "Date in ISO format should be present in content"
        
        # Verify all metadata placeholders were replaced
        assert '{{ metadata.version }}' not in result.content, \
            "Version placeholder should be replaced"
        assert '{{ metadata.author }}' not in result.content, \
            "Author placeholder should be replaced"
        assert '{{ metadata.date }}' not in result.content, \
            "Date placeholder should be replaced"
        
        # Verify correct number of replacements
        assert len(result.replacements) == 3, \
            f"Expected 3 metadata replacements, got {len(result.replacements)}"
    
    def test_metadata_version_with_config(self):
        """Test metadata version replacement with configured version."""
        metadata = {'version': '2.5.1'}
        processor = PlaceholderProcessor(metadata=metadata)
        
        content = 'Version: {{ metadata.version }}'
        result = processor.process_template(content)
        
        assert '2.5.1' in result.content
        assert '{{ metadata.version }}' not in result.content
    
    def test_metadata_version_without_config(self):
        """Test metadata version replacement with default fallback."""
        processor = PlaceholderProcessor(metadata={})
        
        content = 'Version: {{ metadata.version }}'
        result = processor.process_template(content)
        
        assert '0.0.6' in result.content  # Default version from src/__init__.py
        assert '{{ metadata.version }}' not in result.content
    
    def test_metadata_author_with_config(self):
        """Test metadata author replacement with configured author."""
        metadata = {'author': 'John Doe [john@example.com]'}
        processor = PlaceholderProcessor(metadata=metadata)
        
        content = 'Author: {{ metadata.author }}'
        result = processor.process_template(content)
        
        assert 'John Doe [john@example.com]' in result.content
        assert '{{ metadata.author }}' not in result.content
    
    def test_metadata_author_without_config(self):
        """Test metadata author replacement with default fallback."""
        processor = PlaceholderProcessor(metadata={})
        
        content = 'Author: {{ metadata.author }}'
        result = processor.process_template(content)
        
        assert 'Andreas Huemmer [andreas.huemmer@adminsend.de]' in result.content
        assert '{{ metadata.author }}' not in result.content
    
    def test_metadata_date_always_current(self):
        """Test metadata date replacement always uses current date."""
        processor = PlaceholderProcessor(metadata={})
        
        content = 'Date: {{ metadata.date }}'
        result = processor.process_template(content)
        
        # Verify date format YYYY-MM-DD
        import re
        from datetime import datetime
        
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', result.content)
        assert date_match, "Date should be in ISO format"
        
        # Verify it's today's date
        date_str = date_match.group(1)
        today = datetime.now().strftime('%Y-%m-%d')
        assert date_str == today, f"Date should be today ({today}), got {date_str}"
    
    def test_metadata_unknown_field(self):
        """Test metadata placeholder with unknown field."""
        processor = PlaceholderProcessor(metadata={})
        
        content = '{{ metadata.unknown_field }}'
        result = processor.process_template(content)
        
        # Should generate warning
        assert len(result.warnings) >= 1
        assert 'unknown metadata field' in result.warnings[0].lower()
        
        # Placeholder should remain unchanged
        assert '{{ metadata.unknown_field }}' in result.content
    
    def test_metadata_mixed_with_data_sources(self):
        """Test metadata placeholders mixed with data source placeholders."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        metadata = {'version': '3.0.0', 'author': 'Test Author'}
        
        processor = PlaceholderProcessor(
            data_sources={'netbox': mock_adapter},
            metadata=metadata
        )
        
        content = """# Handbook
Version: {{ metadata.version }}
Author: {{ metadata.author }}
Device: {{ netbox.device_name }}
"""
        
        result = processor.process_template(content)
        
        # Verify all replacements
        assert '3.0.0' in result.content
        assert 'Test Author' in result.content
        assert 'server-01' in result.content
        
        # Verify no placeholders remain
        assert '{{' not in result.content
        
        # Verify correct number of replacements
        assert len(result.replacements) == 3



class TestMetaPlaceholderDetection:
    """Tests for meta placeholder detection and processing."""
    
    def test_detect_meta_placeholder(self):
        """Test detection of meta placeholders."""
        processor = PlaceholderProcessor()
        content = '{{ meta.organization.name }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'meta'
        assert placeholders[0].field == 'organization.name'
    
    def test_detect_multiple_meta_placeholders(self):
        """Test detection of multiple meta placeholders."""
        processor = PlaceholderProcessor()
        content = """# Organization
{{ meta.organization.name }}
{{ meta.ceo.name }}
{{ meta.cio.email }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 3
        assert all(p.source == 'meta' for p in placeholders)
        assert placeholders[0].field == 'organization.name'
        assert placeholders[1].field == 'ceo.name'
        assert placeholders[2].field == 'cio.email'
    
    def test_distinguish_meta_from_netbox(self):
        """Test that meta and netbox placeholders are distinguished."""
        processor = PlaceholderProcessor()
        content = """# Mixed Sources
{{ netbox.device_name }}
{{ meta.organization.name }}
{{ netbox.site_name }}
{{ meta.ceo.email }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 4
        
        # Check sources are correctly identified
        sources = [p.source for p in placeholders]
        assert sources.count('netbox') == 2
        assert sources.count('meta') == 2
        
        # Check fields are correctly parsed
        netbox_placeholders = [p for p in placeholders if p.source == 'netbox']
        meta_placeholders = [p for p in placeholders if p.source == 'meta']
        
        assert netbox_placeholders[0].field == 'device_name'
        assert netbox_placeholders[1].field == 'site_name'
        assert meta_placeholders[0].field == 'organization.name'
        assert meta_placeholders[1].field == 'ceo.email'


class TestDualSourceRouting:
    """Tests for dual-source routing (netbox + meta)."""
    
    def test_route_to_meta_adapter(self):
        """Test routing meta placeholder to meta adapter."""
        # Create mock meta adapter
        mock_meta = MockDataSourceAdapter({
            'organization.name': 'AdminSend GmbH',
            'ceo.name': 'Max Mustermann'
        })
        
        processor = PlaceholderProcessor(data_sources={'meta': mock_meta})
        
        placeholder = Placeholder(
            raw='{{ meta.organization.name }}',
            source='meta',
            field='organization.name',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value == 'AdminSend GmbH'
        assert warning is None
    
    def test_route_to_netbox_adapter(self):
        """Test routing netbox placeholder to netbox adapter."""
        # Create mock netbox adapter
        mock_netbox = MockDataSourceAdapter({
            'device_name': 'server-01'
        })
        
        processor = PlaceholderProcessor(data_sources={'netbox': mock_netbox})
        
        placeholder = Placeholder(
            raw='{{ netbox.device_name }}',
            source='netbox',
            field='device_name',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        assert value == 'server-01'
        assert warning is None
    
    def test_dual_source_processing(self):
        """Test processing template with both netbox and meta placeholders."""
        # Create mock adapters
        mock_netbox = MockDataSourceAdapter({
            'device_name': 'server-01',
            'site_name': 'datacenter-1'
        })
        mock_meta = MockDataSourceAdapter({
            'organization.name': 'AdminSend GmbH',
            'ceo.name': 'Max Mustermann',
            'cio.email': 'cio@example.com'
        })
        
        processor = PlaceholderProcessor(data_sources={
            'netbox': mock_netbox,
            'meta': mock_meta
        })
        
        # Use placeholders on their own lines to avoid validation warnings
        content = """# IT Operations Handbook
{{ meta.organization.name }}
{{ meta.ceo.name }}
{{ meta.cio.email }}
{{ netbox.device_name }}
{{ netbox.site_name }}
"""
        
        result = processor.process_template(content)
        
        # Verify all replacements
        assert len(result.replacements) == 5
        
        # Verify content
        assert 'AdminSend GmbH' in result.content
        assert 'Max Mustermann' in result.content
        assert 'cio@example.com' in result.content
        assert 'server-01' in result.content
        assert 'datacenter-1' in result.content
        
        # Verify no placeholders remain
        assert '{{' not in result.content
        
        # Verify no warnings (placeholders are on their own lines)
        assert len(result.warnings) == 0
    
    def test_mixed_placeholders_with_missing_fields(self):
        """Test mixed placeholders with some missing fields."""
        # Create mock adapters with partial data
        mock_netbox = MockDataSourceAdapter({
            'device_name': 'server-01'
            # site_name is missing
        })
        mock_meta = MockDataSourceAdapter({
            'organization.name': 'AdminSend GmbH'
            # ceo.name is missing
        })
        
        processor = PlaceholderProcessor(data_sources={
            'netbox': mock_netbox,
            'meta': mock_meta
        })
        
        content = """# Handbook
Organization: {{ meta.organization.name }}
CEO: {{ meta.ceo.name }}
Device: {{ netbox.device_name }}
Site: {{ netbox.site_name }}
"""
        
        result = processor.process_template(content)
        
        # Should have 2 successful replacements
        assert len(result.replacements) == 2
        
        # Should have 2 warnings for missing fields
        assert len(result.warnings) >= 2
        
        # Verify successful replacements
        assert 'AdminSend GmbH' in result.content
        assert 'server-01' in result.content
        
        # Verify missing placeholders remain
        assert '{{ meta.ceo.name }}' in result.content
        assert '{{ netbox.site_name }}' in result.content
    
    def test_error_handling_consistency(self):
        """Test that error handling is consistent across sources."""
        # Create processor with only netbox adapter
        mock_netbox = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_netbox})
        
        # Try to use meta placeholder without meta adapter
        placeholder = Placeholder(
            raw='{{ meta.organization.name }}',
            source='meta',
            field='organization.name',
            line_number=1
        )
        
        value, warning = processor.replace_placeholder(placeholder)
        
        # Should return None and warning
        assert value is None
        assert warning is not None
        # Check for error type in warning (case-insensitive)
        warning_lower = warning.lower()
        assert 'unknown_data_source' in warning_lower or 'unknown data source' in warning_lower
        assert 'meta' in warning
        assert 'available sources' in warning_lower
        assert 'netbox' in warning


class TestStatisticsBySource:
    """Tests for statistics tracking by source."""
    
    def test_get_replacement_count_by_source(self):
        """Test getting replacement count for specific source."""
        result = ProcessingResult(content='test')
        result.replacements = [
            Replacement('{{ netbox.device }}', 'server-01', 'netbox', 1),
            Replacement('{{ netbox.site }}', 'dc-1', 'netbox', 2),
            Replacement('{{ meta.org }}', 'AdminSend', 'meta', 3),
        ]
        
        assert result.get_replacement_count_by_source('netbox') == 2
        assert result.get_replacement_count_by_source('meta') == 1
        assert result.get_replacement_count_by_source('unknown') == 0
    
    def test_get_sources_used(self):
        """Test getting set of sources used."""
        result = ProcessingResult(content='test')
        result.replacements = [
            Replacement('{{ netbox.device }}', 'server-01', 'netbox', 1),
            Replacement('{{ meta.org }}', 'AdminSend', 'meta', 2),
            Replacement('{{ metadata.date }}', '2025-01-30', 'metadata', 3),
        ]
        
        sources = result.get_sources_used()
        
        assert len(sources) == 3
        assert 'netbox' in sources
        assert 'meta' in sources
        assert 'metadata' in sources
    
    def test_get_statistics_summary(self):
        """Test getting statistics summary."""
        result = ProcessingResult(content='test')
        result.replacements = [
            Replacement('{{ netbox.device }}', 'server-01', 'netbox', 1),
            Replacement('{{ netbox.site }}', 'dc-1', 'netbox', 2),
            Replacement('{{ meta.org }}', 'AdminSend', 'meta', 3),
            Replacement('{{ meta.ceo }}', 'Max', 'meta', 4),
            Replacement('{{ meta.cio }}', 'Anna', 'meta', 5),
            Replacement('{{ metadata.date }}', '2025-01-30', 'metadata', 6),
        ]
        
        stats = result.get_statistics_summary()
        
        assert stats['netbox'] == 2
        assert stats['meta'] == 3
        assert stats['metadata'] == 1
    
    def test_statistics_with_dual_source_processing(self):
        """Test statistics tracking during dual-source processing."""
        # Create mock adapters
        mock_netbox = MockDataSourceAdapter({
            'device_name': 'server-01',
            'site_name': 'datacenter-1'
        })
        mock_meta = MockDataSourceAdapter({
            'organization.name': 'AdminSend GmbH',
            'ceo.name': 'Max Mustermann',
            'cio.email': 'cio@example.com'
        })
        
        processor = PlaceholderProcessor(
            data_sources={'netbox': mock_netbox, 'meta': mock_meta},
            metadata={'version': '1.0.0'}
        )
        
        content = """# Handbook
Version: {{ metadata.version }}
Organization: {{ meta.organization.name }}
CEO: {{ meta.ceo.name }}
Device: {{ netbox.device_name }}
Site: {{ netbox.site_name }}
"""
        
        result = processor.process_template(content)
        
        # Verify statistics
        stats = result.get_statistics_summary()
        
        assert stats['metadata'] == 1
        assert stats['meta'] == 2
        assert stats['netbox'] == 2
        
        # Verify total replacements
        assert len(result.replacements) == 5
        
        # Verify sources used
        sources = result.get_sources_used()
        assert len(sources) == 3
        assert 'netbox' in sources
        assert 'meta' in sources
        assert 'metadata' in sources



class TestMetaPlaceholderDetectionProperty:
    """Property-based tests for meta placeholder detection."""
    
    @settings(max_examples=100)
    @given(
        num_meta_placeholders=st.integers(min_value=1, max_value=10),
        num_netbox_placeholders=st.integers(min_value=0, max_value=10),
        data=st.data()
    )
    def test_property_1_meta_placeholder_detection(
        self, 
        num_meta_placeholders, 
        num_netbox_placeholders,
        data
    ):
        """
        Feature: it-operation-template-extension, Property 1: Meta Placeholder Detection
        
        For any template content containing meta placeholders in the format "{{ meta.field }}",
        the system should correctly identify all meta placeholders and distinguish them from
        netbox placeholders.
        
        Validates: Requirements 16.1, 16.2
        """
        processor = PlaceholderProcessor()
        
        # Generate template with meta and netbox placeholders
        template_lines = []
        expected_meta_count = 0
        expected_netbox_count = 0
        
        # Add meta placeholders
        for i in range(num_meta_placeholders):
            field_parts = []
            num_parts = data.draw(st.integers(min_value=1, max_value=3))
            for _ in range(num_parts):
                part = data.draw(st.text(
                    alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                    min_size=1,
                    max_size=10
                ).filter(lambda x: x and x[0].isalpha()))
                field_parts.append(part)
            
            field = '.'.join(field_parts)
            placeholder = f'{{{{ meta.{field} }}}}'
            template_lines.append(placeholder)
            expected_meta_count += 1
        
        # Add netbox placeholders
        for i in range(num_netbox_placeholders):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=10
            ).filter(lambda x: x and x[0].isalpha()))
            
            placeholder = f'{{{{ netbox.{field} }}}}'
            template_lines.append(placeholder)
            expected_netbox_count += 1
        
        template_content = '\n'.join(template_lines)
        
        # Find placeholders
        placeholders = processor.find_placeholders(template_content)
        
        # Verify correct number of placeholders found
        assert len(placeholders) == expected_meta_count + expected_netbox_count, \
            f"Expected {expected_meta_count + expected_netbox_count} placeholders, found {len(placeholders)}"
        
        # Count meta and netbox placeholders
        meta_placeholders = [p for p in placeholders if p.source == 'meta']
        netbox_placeholders = [p for p in placeholders if p.source == 'netbox']
        
        # Verify correct counts by source
        assert len(meta_placeholders) == expected_meta_count, \
            f"Expected {expected_meta_count} meta placeholders, found {len(meta_placeholders)}"
        assert len(netbox_placeholders) == expected_netbox_count, \
            f"Expected {expected_netbox_count} netbox placeholders, found {len(netbox_placeholders)}"
        
        # Verify all meta placeholders have source='meta'
        for placeholder in meta_placeholders:
            assert placeholder.source == 'meta', \
                f"Meta placeholder should have source='meta', got '{placeholder.source}'"
            assert placeholder.field, \
                "Meta placeholder should have non-empty field"
        
        # Verify all netbox placeholders have source='netbox'
        for placeholder in netbox_placeholders:
            assert placeholder.source == 'netbox', \
                f"NetBox placeholder should have source='netbox', got '{placeholder.source}'"
            assert placeholder.field, \
                "NetBox placeholder should have non-empty field"



class TestDualSourceProcessingProperty:
    """Property-based tests for dual-source placeholder processing."""
    
    @settings(max_examples=100)
    @given(
        num_meta_fields=st.integers(min_value=1, max_value=5),
        num_netbox_fields=st.integers(min_value=1, max_value=5),
        data=st.data()
    )
    def test_property_4_dual_source_placeholder_processing(
        self,
        num_meta_fields,
        num_netbox_fields,
        data
    ):
        """
        Feature: it-operation-template-extension, Property 4: Dual Source Placeholder Processing
        
        For any template containing both netbox and meta placeholders, the system should
        correctly process both types and route each to the appropriate adapter.
        
        Validates: Requirements 16.5, 19.2
        """
        # Generate field data for both sources
        meta_fields = {}
        netbox_fields = {}
        template_lines = []
        
        # Generate meta fields and placeholders
        for i in range(num_meta_fields):
            # Generate field path (can be nested)
            field_parts = []
            num_parts = data.draw(st.integers(min_value=1, max_value=3))
            for _ in range(num_parts):
                part = data.draw(st.text(
                    alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                    min_size=1,
                    max_size=10
                ).filter(lambda x: x and x[0].isalpha()))
                field_parts.append(part)
            
            field = '.'.join(field_parts)
            value = data.draw(st.text(min_size=1, max_size=50))
            
            meta_fields[field] = value
            template_lines.append(f'{{{{ meta.{field} }}}}')
        
        # Generate netbox fields and placeholders
        for i in range(num_netbox_fields):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=10
            ).filter(lambda x: x and x[0].isalpha()))
            value = data.draw(st.text(min_size=1, max_size=50))
            
            netbox_fields[field] = value
            template_lines.append(f'{{{{ netbox.{field} }}}}')
        
        template_content = '\n'.join(template_lines)
        
        # Create mock adapters
        mock_meta = MockDataSourceAdapter(meta_fields)
        mock_netbox = MockDataSourceAdapter(netbox_fields)
        
        processor = PlaceholderProcessor(data_sources={
            'meta': mock_meta,
            'netbox': mock_netbox
        })
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify all placeholders were replaced
        expected_total = num_meta_fields + num_netbox_fields
        assert len(result.replacements) == expected_total, \
            f"Expected {expected_total} replacements, got {len(result.replacements)}"
        
        # Verify replacements by source
        meta_replacements = [r for r in result.replacements if r.source == 'meta']
        netbox_replacements = [r for r in result.replacements if r.source == 'netbox']
        
        assert len(meta_replacements) == num_meta_fields, \
            f"Expected {num_meta_fields} meta replacements, got {len(meta_replacements)}"
        assert len(netbox_replacements) == num_netbox_fields, \
            f"Expected {num_netbox_fields} netbox replacements, got {len(netbox_replacements)}"
        
        # Verify all meta values are in content
        for field, value in meta_fields.items():
            assert value in result.content, \
                f"Meta field value '{value}' should be in content"
        
        # Verify all netbox values are in content
        for field, value in netbox_fields.items():
            assert value in result.content, \
                f"NetBox field value '{value}' should be in content"
        
        # Verify no placeholders remain
        assert '{{' not in result.content, \
            "No placeholders should remain in content"
        
        # Verify no warnings (all fields exist in adapters)
        assert len(result.warnings) == 0, \
            f"No warnings expected, got {len(result.warnings)}: {result.warnings}"
        
        # Verify statistics
        stats = result.get_statistics_summary()
        assert stats.get('meta', 0) == num_meta_fields, \
            f"Statistics should show {num_meta_fields} meta replacements"
        assert stats.get('netbox', 0) == num_netbox_fields, \
            f"Statistics should show {num_netbox_fields} netbox replacements"
        
        # Verify sources used
        sources = result.get_sources_used()
        assert 'meta' in sources, "Meta source should be in sources used"
        assert 'netbox' in sources, "NetBox source should be in sources used"



class TestHTMLCommentIntegration:
    """Integration tests for HTML comment processing with placeholder replacement."""
    
    def test_comments_removed_before_placeholder_processing(self):
        """Test that HTML comments are removed before placeholders are processed."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """# Device Information
<!-- This is a comment about the device -->
{{ netbox.device_name }}
<!-- End of device section -->"""
        
        result = processor.process_template(content)
        
        # Verify comments are removed
        assert "<!--" not in result.content
        assert "-->" not in result.content
        assert "This is a comment" not in result.content
        
        # Verify placeholder was replaced
        assert "server-01" in result.content
        assert "{{ netbox.device_name }}" not in result.content
        
        # Verify statistics
        assert result.comments_removed == 2
        assert len(result.replacements) == 1
    
    def test_comment_with_placeholder_inside(self):
        """Test that placeholders inside comments are not processed."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """# Device Information
<!-- TODO: Replace {{ netbox.device_name }} with actual value -->
{{ netbox.device_name }}"""
        
        result = processor.process_template(content)
        
        # Verify comment is removed (including placeholder inside it)
        assert "<!--" not in result.content
        assert "-->" not in result.content
        assert "TODO" not in result.content
        
        # Verify only the placeholder outside the comment was replaced
        assert result.content.count("server-01") == 1
        assert "{{ netbox.device_name }}" not in result.content
        
        # Verify statistics
        assert result.comments_removed == 1
        assert len(result.replacements) == 1
    
    def test_mixed_comments_and_placeholders(self):
        """Test template with both comments and placeholders mixed."""
        mock_netbox = MockDataSourceAdapter({
            'device_name': 'server-01',
            'site_name': 'datacenter-1'
        })
        mock_meta = MockDataSourceAdapter({
            'organization.name': 'AdminSend GmbH'
        })
        
        processor = PlaceholderProcessor(data_sources={
            'netbox': mock_netbox,
            'meta': mock_meta
        })
        
        content = """# IT Operations Handbook
<!-- Organization information -->
{{ meta.organization.name }}
<!-- Device details -->
{{ netbox.device_name }}
<!-- Site information -->
{{ netbox.site_name }}
<!-- End of document -->"""
        
        result = processor.process_template(content)
        
        # Verify all comments are removed
        assert "<!--" not in result.content
        assert "-->" not in result.content
        
        # Verify all placeholders are replaced
        assert "AdminSend GmbH" in result.content
        assert "server-01" in result.content
        assert "datacenter-1" in result.content
        
        # Verify statistics
        assert result.comments_removed == 4
        assert len(result.replacements) == 3
    
    def test_multiline_comment_with_placeholders(self):
        """Test multiline comment with placeholders in surrounding content."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """# Device Information
{{ netbox.device_name }}
<!--
This is a multiline comment
that spans several lines
and should be completely removed
-->
{{ netbox.device_name }}"""
        
        result = processor.process_template(content)
        
        # Verify comment is removed
        assert "<!--" not in result.content
        assert "-->" not in result.content
        assert "multiline comment" not in result.content
        
        # Verify both placeholders are replaced
        assert result.content.count("server-01") == 2
        
        # Verify statistics
        assert result.comments_removed == 1
        assert len(result.replacements) == 2
    
    def test_empty_template_with_comments(self):
        """Test template that becomes empty after comment removal."""
        processor = PlaceholderProcessor()
        
        content = "<!-- Only a comment -->"
        
        result = processor.process_template(content)
        
        # Verify comment is removed
        assert "<!--" not in result.content
        assert "-->" not in result.content
        
        # Verify statistics
        assert result.comments_removed == 1
        assert len(result.replacements) == 0
    
    def test_template_without_comments(self):
        """Test that templates without comments still work correctly."""
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """# Device Information
{{ netbox.device_name }}"""
        
        result = processor.process_template(content)
        
        # Verify placeholder is replaced
        assert "server-01" in result.content
        
        # Verify statistics
        assert result.comments_removed == 0
        assert len(result.replacements) == 1
    
    def test_comment_removal_statistics(self):
        """Test that comment removal statistics are accurate."""
        processor = PlaceholderProcessor()
        
        content = """<!-- Comment 1 -->
Text
<!-- Comment 2 -->
More text
<!-- Comment 3 -->"""
        
        result = processor.process_template(content)
        
        # Verify all comments are removed
        assert "<!--" not in result.content
        
        # Verify statistics
        assert result.comments_removed == 3
    
    def test_unclosed_comment_warning(self):
        """Test that unclosed comments generate warnings."""
        processor = PlaceholderProcessor()
        
        content = """# Header
<!-- Unclosed comment
Some text"""
        
        result = processor.process_template(content)
        
        # Verify warning is generated
        assert len(result.warnings) >= 1
        assert any("unclosed" in w.lower() for w in result.warnings)



class TestHTMLCommentMarkdownPreservationProperty:
    """Property-based tests for markdown preservation during HTML comment removal."""
    
    @settings(max_examples=100)
    @given(
        markdown_elements=st.lists(
            st.sampled_from([
                '# Header 1',
                '## Header 2',
                '### Header 3',
                '**Bold text**',
                '*Italic text*',
                '- List item',
                '1. Numbered item',
                '`code`',
                '[Link](url)',
                '> Quote',
            ]),
            min_size=1,
            max_size=10
        ),
        has_comment=st.booleans(),
        comment_text=st.text(
            alphabet=st.characters(blacklist_characters='<>-'),
            max_size=50
        )
    )
    def test_property_2_html_comment_removal_preserves_markdown(
        self,
        markdown_elements,
        has_comment,
        comment_text
    ):
        """
        Feature: template-system-extension
        Property 2: HTML Comment Removal Preserves Markdown
        
        For any template content with HTML comments, removing comments SHALL preserve
        all non-comment markdown content exactly, including formatting, headers, lists,
        and code blocks.
        
        Validates: Requirements 17.3, 17.4, 17.5
        """
        processor = PlaceholderProcessor()
        
        # Build content with markdown elements
        content_parts = []
        for element in markdown_elements:
            content_parts.append(element)
            
            # Optionally add a comment after this element
            if has_comment:
                content_parts.append(f"<!-- {comment_text} -->")
        
        content = '\n'.join(content_parts)
        
        # Process template (which removes comments)
        result = processor.process_template(content)
        
        # Verify all markdown elements are preserved
        for element in markdown_elements:
            assert element in result.content, \
                f"Markdown element '{element}' should be preserved in content"
        
        # Verify no comment markers remain
        assert "<!--" not in result.content, \
            "Opening comment markers should be removed"
        assert "-->" not in result.content, \
            "Closing comment markers should be removed"
        
        # Verify markdown structure is intact (no broken formatting)
        # Check that markdown syntax characters are still present
        if any('#' in elem for elem in markdown_elements):
            assert '#' in result.content, "Header markers should be preserved"
        if any('**' in elem for elem in markdown_elements):
            assert '**' in result.content, "Bold markers should be preserved"
        if any('*' in elem and '**' not in elem for elem in markdown_elements):
            assert '*' in result.content, "Italic markers should be preserved"
        if any('`' in elem for elem in markdown_elements):
            assert '`' in result.content, "Code markers should be preserved"
        if any('[' in elem and ']' in elem for elem in markdown_elements):
            assert '[' in result.content and ']' in result.content, \
                "Link markers should be preserved"
