"""
Property-Based Tests for Placeholder System with New Compliance Frameworks

Tests universal properties for placeholder recognition, processing, and logging
for IDW PS 951, NIST CSF 2.0, and TOGAF templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from hypothesis import given, settings, strategies as st
import re

from src.placeholder_processor import PlaceholderProcessor


class MockDataSourceAdapter:
    """Mock adapter for testing placeholder replacement."""
    
    def __init__(self, data: dict):
        """Initialize with mock data."""
        self.data = data
    
    def get_field(self, field_path: str):
        """Get field value from mock data."""
        return self.data.get(field_path)


# Hypothesis strategies for generating test data
@st.composite
def valid_source_name(draw):
    """Generate a valid source name (alphanumeric with hyphens)."""
    # Common sources used in new frameworks
    common_sources = ['meta', 'source', 'netbox', 'metadata']
    use_common = draw(st.booleans())
    
    if use_common:
        return draw(st.sampled_from(common_sources))
    else:
        # Generate custom source name
        name = draw(st.text(
            alphabet=st.characters(
                whitelist_categories=('Ll', 'Lu', 'Nd'),
                whitelist_characters='-_'
            ),
            min_size=1,
            max_size=20
        ).filter(lambda x: x and x[0].isalpha()))
        return name


@st.composite
def valid_field_name(draw):
    """Generate a valid field name (alphanumeric with dots for nesting)."""
    # Generate 1-3 parts separated by dots
    num_parts = draw(st.integers(min_value=1, max_value=3))
    parts = []
    
    for _ in range(num_parts):
        part = draw(st.text(
            alphabet=st.characters(
                whitelist_categories=('Ll', 'Lu', 'Nd'),
                whitelist_characters='_'
            ),
            min_size=1,
            max_size=15
        ).filter(lambda x: x and x[0].isalpha()))
        parts.append(part)
    
    return '.'.join(parts)


@st.composite
def valid_placeholder(draw):
    """Generate a valid placeholder string."""
    source = draw(valid_source_name())
    field = draw(valid_field_name())
    
    # Add optional whitespace
    ws_before = draw(st.text(alphabet=' \t', max_size=3))
    ws_after = draw(st.text(alphabet=' \t', max_size=3))
    
    return f'{{{{{ws_before}{source}.{field}{ws_after}}}}}'


@st.composite
def invalid_placeholder(draw):
    """Generate an invalid placeholder string."""
    # Various invalid formats
    invalid_formats = [
        '{{ source }}',  # Missing field
        '{{ .field }}',  # Missing source
        '{{ source.field',  # Missing closing braces
        'source.field }}',  # Missing opening braces
        '{ source.field }',  # Single braces
        '{{ source field }}',  # Missing dot
        '{{ source..field }}',  # Double dot
        '{{ source. }}',  # Empty field
        '{{ .field }}',  # Empty source
    ]
    
    return draw(st.sampled_from(invalid_formats))


class TestProperty6PlaceholderSyntaxValidation:
    """
    Property 6: Placeholder Syntax Validation
    
    For any placeholder in a template, it must follow the syntax {{ source.field }}
    where source is one of (source, meta, netbox) and field is a valid identifier.
    
    Validates: Requirements 4.5, 7.1, 7.5, 9.5
    """
    
    @settings(max_examples=100)
    @given(placeholder=valid_placeholder())
    def test_property_6_valid_placeholder_syntax(self, placeholder):
        """
        Feature: additional-compliance-frameworks, Property 6: Placeholder Syntax Validation
        
        For any valid placeholder following {{ source.field }} syntax, the system
        should correctly parse and recognize it.
        
        Validates: Requirements 4.5, 7.1, 7.5, 9.5
        """
        processor = PlaceholderProcessor()
        
        # Find placeholders in content
        placeholders = processor.find_placeholders(placeholder)
        
        # Should find exactly one placeholder
        assert len(placeholders) == 1, \
            f"Should find exactly one placeholder in '{placeholder}'"
        
        found = placeholders[0]
        
        # Verify source is not empty
        assert found.source, \
            f"Source should not be empty in '{placeholder}'"
        
        # Verify field is not empty
        assert found.field, \
            f"Field should not be empty in '{placeholder}'"
        
        # Verify source contains only valid characters (alphanumeric, hyphens, underscores)
        assert re.match(r'^[\w-]+$', found.source), \
            f"Source should contain only alphanumeric characters, hyphens, and underscores: '{found.source}'"
        
        # Verify field contains only valid characters (alphanumeric, dots, underscores)
        assert re.match(r'^[\w.]+$', found.field), \
            f"Field should contain only alphanumeric characters, dots, and underscores: '{found.field}'"
        
        # Verify field parts (separated by dots) are valid identifiers
        field_parts = found.field.split('.')
        for part in field_parts:
            assert part, f"Field part should not be empty in '{found.field}'"
            assert re.match(r'^\w+$', part), \
                f"Field part should be alphanumeric: '{part}'"
    
    @settings(max_examples=100)
    @given(invalid=invalid_placeholder())
    def test_property_6_invalid_placeholder_syntax(self, invalid):
        """
        Feature: additional-compliance-frameworks, Property 6: Placeholder Syntax Validation
        
        For any invalid placeholder not following {{ source.field }} syntax, the system
        should not recognize it as a placeholder.
        
        Validates: Requirements 4.5, 7.1, 7.5, 9.5
        """
        processor = PlaceholderProcessor()
        
        # Find placeholders in content
        placeholders = processor.find_placeholders(invalid)
        
        # Should not find any valid placeholders
        assert len(placeholders) == 0, \
            f"Should not find valid placeholders in invalid syntax: '{invalid}'"


class TestProperty11PlaceholderRecognitionAndProcessing:
    """
    Property 11: Placeholder Recognition and Processing
    
    For any template containing valid placeholder syntax, the Placeholder_System must
    recognize and process all placeholders, substituting available data or preserving
    the placeholder if data is unavailable.
    
    Validates: Requirements 7.1, 7.2, 7.3, 7.4
    """
    
    @settings(max_examples=100)
    @given(
        num_placeholders=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_11_placeholder_recognition_and_processing(
        self,
        num_placeholders,
        data
    ):
        """
        Feature: additional-compliance-frameworks, Property 11: Placeholder Recognition and Processing
        
        For any template containing placeholders, the system should recognize all
        placeholders and process them correctly, substituting available data or
        preserving placeholders when data is unavailable.
        
        Validates: Requirements 7.1, 7.2, 7.3, 7.4
        """
        # Generate placeholders and data
        template_lines = []
        available_data = {}
        expected_substitutions = 0
        expected_preserved = 0
        
        # Use common sources for new frameworks
        sources = ['meta', 'source']
        
        # Track used field names to avoid duplicates
        used_fields = set()
        
        for i in range(num_placeholders):
            source = data.draw(st.sampled_from(sources))
            
            # Generate unique field name
            field = data.draw(valid_field_name())
            field_key = f"{source}.{field}"
            
            # Skip if we've already used this field
            if field_key in used_fields:
                continue
            
            used_fields.add(field_key)
            
            # Randomly decide if data is available
            has_data = data.draw(st.booleans())
            
            if has_data:
                value = data.draw(st.text(min_size=1, max_size=50))
                if source not in available_data:
                    available_data[source] = {}
                available_data[source][field] = value
                expected_substitutions += 1
            else:
                expected_preserved += 1
            
            # Add placeholder on its own line
            template_lines.append(f'{{{{ {source}.{field} }}}}')
        
        # If we didn't generate enough unique placeholders, adjust expectations
        actual_placeholders = len(template_lines)
        if actual_placeholders < num_placeholders:
            # Some were skipped due to duplicates, recalculate expectations
            expected_substitutions = sum(
                1 for line in template_lines
                if any(
                    f'{{{{ {src}.{fld} }}}}' == line
                    for src, fields in available_data.items()
                    for fld in fields.keys()
                )
            )
            expected_preserved = actual_placeholders - expected_substitutions
        
        template_content = '\n'.join(template_lines)
        
        # Skip test if no placeholders were generated
        if not template_lines:
            return
        
        # Create mock adapters
        mock_adapters = {}
        for source, fields in available_data.items():
            mock_adapters[source] = MockDataSourceAdapter(fields)
        
        # Process template
        processor = PlaceholderProcessor(data_sources=mock_adapters)
        result = processor.process_template(template_content)
        
        # Verify all placeholders were recognized
        total_placeholders = processor.find_placeholders(template_content)
        assert len(total_placeholders) == actual_placeholders, \
            f"Should recognize all {actual_placeholders} placeholders"
        
        # Verify substitutions
        assert len(result.replacements) == expected_substitutions, \
            f"Expected {expected_substitutions} substitutions, got {len(result.replacements)}"
        
        # Verify preserved placeholders
        # Count actual placeholder patterns, not just '{{' which could be in substituted values
        preserved_placeholders = processor.find_placeholders(result.content)
        preserved_count = len(preserved_placeholders)
        assert preserved_count == expected_preserved, \
            f"Expected {expected_preserved} preserved placeholders, got {preserved_count}"
        
        # Verify warnings for missing data
        if expected_preserved > 0:
            assert len(result.warnings) >= expected_preserved, \
                f"Should generate warnings for {expected_preserved} missing fields"
        
        # Verify all available data was substituted
        for source, fields in available_data.items():
            for field, value in fields.items():
                assert value in result.content, \
                    f"Value '{value}' should be in content"
    
    @settings(max_examples=100)
    @given(
        num_meta_placeholders=st.integers(min_value=1, max_value=5),
        num_source_placeholders=st.integers(min_value=1, max_value=5),
        data=st.data()
    )
    def test_property_11_multi_source_processing(
        self,
        num_meta_placeholders,
        num_source_placeholders,
        data
    ):
        """
        Feature: additional-compliance-frameworks, Property 11: Placeholder Recognition and Processing
        
        For any template containing placeholders from multiple sources (meta, source),
        the system should correctly route each to the appropriate adapter and process
        them independently.
        
        Validates: Requirements 7.1, 7.2, 7.3, 7.4
        """
        # Generate meta placeholders and data
        meta_data = {}
        template_lines = []
        
        for i in range(num_meta_placeholders):
            field = data.draw(valid_field_name())
            value = data.draw(st.text(min_size=1, max_size=50))
            meta_data[field] = value
            template_lines.append(f'{{{{ meta.{field} }}}}')
        
        # Generate source placeholders and data
        source_data = {}
        
        for i in range(num_source_placeholders):
            field = data.draw(valid_field_name())
            value = data.draw(st.text(min_size=1, max_size=50))
            source_data[field] = value
            template_lines.append(f'{{{{ source.{field} }}}}')
        
        template_content = '\n'.join(template_lines)
        
        # Create mock adapters
        mock_meta = MockDataSourceAdapter(meta_data)
        mock_source = MockDataSourceAdapter(source_data)
        
        processor = PlaceholderProcessor(data_sources={
            'meta': mock_meta,
            'source': mock_source
        })
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify all placeholders were processed
        total_expected = num_meta_placeholders + num_source_placeholders
        assert len(result.replacements) == total_expected, \
            f"Expected {total_expected} replacements, got {len(result.replacements)}"
        
        # Verify replacements by source
        meta_replacements = [r for r in result.replacements if r.source == 'meta']
        source_replacements = [r for r in result.replacements if r.source == 'source']
        
        assert len(meta_replacements) == num_meta_placeholders, \
            f"Expected {num_meta_placeholders} meta replacements"
        assert len(source_replacements) == num_source_placeholders, \
            f"Expected {num_source_placeholders} source replacements"
        
        # Verify all values are in content
        for value in meta_data.values():
            assert value in result.content, \
                f"Meta value '{value}' should be in content"
        
        for value in source_data.values():
            assert value in result.content, \
                f"Source value '{value}' should be in content"
        
        # Verify no placeholders remain
        # Check for actual placeholder patterns, not just '{{' which could be in substituted values
        remaining_placeholders = processor.find_placeholders(result.content)
        assert len(remaining_placeholders) == 0, \
            f"No placeholders should remain in content, found {len(remaining_placeholders)}"


class TestProperty12PlaceholderSubstitutionLogging:
    """
    Property 12: Placeholder Substitution Logging
    
    For any placeholder substitution operation, the Placeholder_System must log the
    operation including the placeholder name, source, and substituted value.
    
    Validates: Requirements 7.6
    """
    
    @settings(max_examples=100)
    @given(
        num_substitutions=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_12_substitution_logging(self, num_substitutions, data):
        """
        Feature: additional-compliance-frameworks, Property 12: Placeholder Substitution Logging
        
        For any placeholder substitution, the system should log the operation with
        complete details including placeholder text, source, field, value, and line number.
        
        Validates: Requirements 7.6
        """
        # Generate placeholders and data
        template_lines = []
        expected_data = {}
        sources = ['meta', 'source']
        
        for i in range(num_substitutions):
            source = data.draw(st.sampled_from(sources))
            field = data.draw(valid_field_name())
            value = data.draw(st.text(min_size=1, max_size=50))
            
            if source not in expected_data:
                expected_data[source] = {}
            expected_data[source][field] = value
            
            template_lines.append(f'{{{{ {source}.{field} }}}}')
        
        template_content = '\n'.join(template_lines)
        
        # Create mock adapters
        mock_adapters = {}
        for source, fields in expected_data.items():
            mock_adapters[source] = MockDataSourceAdapter(fields)
        
        # Process template
        processor = PlaceholderProcessor(data_sources=mock_adapters)
        result = processor.process_template(template_content)
        
        # Verify all substitutions are logged
        assert len(result.replacements) == num_substitutions, \
            f"Expected {num_substitutions} logged replacements"
        
        # Verify each replacement has complete information
        for replacement in result.replacements:
            # Verify placeholder text is logged
            assert replacement.placeholder, \
                "Replacement should have placeholder text"
            assert '{{' in replacement.placeholder and '}}' in replacement.placeholder, \
                f"Placeholder should contain braces: '{replacement.placeholder}'"
            
            # Verify source is logged
            assert replacement.source, \
                "Replacement should have source"
            assert replacement.source in sources, \
                f"Source should be one of {sources}: '{replacement.source}'"
            
            # Verify value is logged
            assert replacement.value, \
                "Replacement should have value"
            
            # Verify line number is logged
            assert replacement.line_number > 0, \
                "Replacement should have positive line number"
            
            # Verify value matches expected data
            # Extract field from placeholder
            match = re.search(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}', replacement.placeholder)
            if match:
                source = match.group(1)
                field = match.group(2)
                expected_value = expected_data[source][field]
                assert replacement.value == expected_value, \
                    f"Logged value should match expected: '{replacement.value}' != '{expected_value}'"
    
    @settings(max_examples=100)
    @given(
        num_successful=st.integers(min_value=1, max_value=5),
        num_failed=st.integers(min_value=1, max_value=5),
        data=st.data()
    )
    def test_property_12_logging_with_failures(
        self,
        num_successful,
        num_failed,
        data
    ):
        """
        Feature: additional-compliance-frameworks, Property 12: Placeholder Substitution Logging
        
        For any template with both successful and failed substitutions, the system
        should log successful substitutions in replacements and failed substitutions
        in warnings.
        
        Validates: Requirements 7.6
        """
        # Generate successful placeholders
        template_lines = []
        available_data = {}
        source = 'meta'
        
        for i in range(num_successful):
            field = data.draw(valid_field_name())
            value = data.draw(st.text(min_size=1, max_size=50))
            available_data[field] = value
            template_lines.append(f'{{{{ {source}.{field} }}}}')
        
        # Generate failed placeholders (missing data)
        for i in range(num_failed):
            field = data.draw(valid_field_name().filter(lambda x: x not in available_data))
            template_lines.append(f'{{{{ {source}.{field} }}}}')
        
        template_content = '\n'.join(template_lines)
        
        # Create mock adapter with only successful data
        mock_adapter = MockDataSourceAdapter(available_data)
        processor = PlaceholderProcessor(data_sources={source: mock_adapter})
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify successful substitutions are logged
        assert len(result.replacements) == num_successful, \
            f"Expected {num_successful} successful replacements"
        
        # Verify failed substitutions generate warnings
        assert len(result.warnings) >= num_failed, \
            f"Expected at least {num_failed} warnings for failed substitutions"
        
        # Verify successful values are in content
        for value in available_data.values():
            assert value in result.content, \
                f"Successful value '{value}' should be in content"
        
        # Verify failed placeholders are preserved
        preserved_placeholders = processor.find_placeholders(result.content)
        preserved_count = len(preserved_placeholders)
        assert preserved_count == num_failed, \
            f"Expected {num_failed} preserved placeholders"
    
    @settings(max_examples=100)
    @given(
        num_placeholders=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_12_statistics_tracking(self, num_placeholders, data):
        """
        Feature: additional-compliance-frameworks, Property 12: Placeholder Substitution Logging
        
        For any template processing, the system should track statistics by source
        including replacement counts and sources used.
        
        Validates: Requirements 7.6
        """
        # Generate placeholders from multiple sources
        template_lines = []
        expected_counts = {'meta': 0, 'source': 0}
        available_data = {'meta': {}, 'source': {}}
        
        for i in range(num_placeholders):
            source = data.draw(st.sampled_from(['meta', 'source']))
            field = data.draw(valid_field_name())
            value = data.draw(st.text(min_size=1, max_size=50))
            
            available_data[source][field] = value
            expected_counts[source] += 1
            template_lines.append(f'{{{{ {source}.{field} }}}}')
        
        template_content = '\n'.join(template_lines)
        
        # Create mock adapters
        mock_meta = MockDataSourceAdapter(available_data['meta'])
        mock_source = MockDataSourceAdapter(available_data['source'])
        
        processor = PlaceholderProcessor(data_sources={
            'meta': mock_meta,
            'source': mock_source
        })
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify statistics summary
        stats = result.get_statistics_summary()
        
        # Verify counts by source
        for source, expected_count in expected_counts.items():
            if expected_count > 0:
                assert source in stats, \
                    f"Source '{source}' should be in statistics"
                assert stats[source] == expected_count, \
                    f"Expected {expected_count} replacements for '{source}', got {stats[source]}"
        
        # Verify sources used
        sources_used = result.get_sources_used()
        
        for source, count in expected_counts.items():
            if count > 0:
                assert source in sources_used, \
                    f"Source '{source}' should be in sources used"
