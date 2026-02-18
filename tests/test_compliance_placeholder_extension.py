"""
Tests for Compliance Framework Templates Placeholder Extension

Tests placeholder recognition and preservation for new compliance frameworks.

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


class TestPlaceholderRecognitionForNewFrameworks:
    """Unit tests for placeholder recognition in new compliance frameworks (Subtask 12.1)."""
    
    def test_recognize_netbox_placeholder(self):
        """Test that {{ netbox.field }} syntax is recognized."""
        processor = PlaceholderProcessor()
        content = '{{ netbox.device_name }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'netbox'
        assert placeholders[0].field == 'device_name'
    
    def test_recognize_meta_placeholder(self):
        """Test that {{ meta.field }} syntax is recognized."""
        processor = PlaceholderProcessor()
        content = '{{ meta.organization.name }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'meta'
        assert placeholders[0].field == 'organization.name'
    
    def test_recognize_metadata_author_placeholder(self):
        """Test that {{ meta.author }} syntax is recognized."""
        processor = PlaceholderProcessor()
        content = '{{ meta.author }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'meta'
        assert placeholders[0].field == 'author'
    
    def test_recognize_metadata_version_placeholder(self):
        """Test that {{ meta.version }} syntax is recognized."""
        processor = PlaceholderProcessor()
        content = '{{ meta.version }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'meta'
        assert placeholders[0].field == 'version'
    
    def test_recognize_metadata_date_placeholder(self):
        """Test that {{ meta.date }} syntax is recognized."""
        processor = PlaceholderProcessor()
        content = '{{ meta.date }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'meta'
        assert placeholders[0].field == 'date'
    
    def test_recognize_multiple_source_types(self):
        """Test recognition of multiple placeholder source types in one template."""
        processor = PlaceholderProcessor()
        content = """# Compliance Framework Template
{{ netbox.device_name }}
{{ meta.organization.name }}
{{ meta.author }}
{{ meta.version }}
{{ meta.date }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 5
        
        # Verify sources
        sources = [p.source for p in placeholders]
        assert sources.count('netbox') == 1
        assert sources.count('meta') == 4
    
    def test_recognize_nested_field_paths(self):
        """Test recognition of nested field paths."""
        processor = PlaceholderProcessor()
        content = """
{{ netbox.site.location.name }}
{{ meta.organization.address.city }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 2
        assert placeholders[0].field == 'site.location.name'
        assert placeholders[1].field == 'organization.address.city'


class TestPlaceholderPreservationOnMissingData:
    """Unit tests for placeholder preservation when data is unavailable (Subtask 12.2)."""
    
    def test_preserve_placeholder_when_source_unavailable(self):
        """Test that placeholder is preserved when data source is unavailable."""
        # Create processor without any data sources
        processor = PlaceholderProcessor(data_sources={})
        
        content = '{{ netbox.device_name }}'
        result = processor.process_template(content)
        
        # Placeholder should remain unchanged
        assert '{{ netbox.device_name }}' in result.content
        
        # Should generate warning
        assert len(result.warnings) >= 1
        assert any('unknown' in w.lower() or 'not found' in w.lower() for w in result.warnings)
    
    def test_preserve_placeholder_when_field_not_found(self):
        """Test that placeholder is preserved when field is not found in data source."""
        # Create processor with data source but missing field
        mock_adapter = MockDataSourceAdapter({'other_field': 'value'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = '{{ netbox.missing_field }}'
        result = processor.process_template(content)
        
        # Placeholder should remain unchanged
        assert '{{ netbox.missing_field }}' in result.content
        
        # Should generate warning
        assert len(result.warnings) >= 1
        assert any('field_not_found' in w.lower() or 'not found' in w.lower() for w in result.warnings)
    
    def test_log_missing_data_for_debugging(self):
        """Test that missing data is logged in warnings for debugging."""
        processor = PlaceholderProcessor(data_sources={})
        
        content = """
{{ netbox.device_name }}
{{ meta.organization.name }}
"""
        
        result = processor.process_template(content)
        
        # Should have warnings for both missing sources
        assert len(result.warnings) >= 2
        
        # Warnings should contain useful debugging information
        warning_text = ' '.join(result.warnings).lower()
        assert 'netbox' in warning_text
        assert 'meta' in warning_text
    
    def test_preserve_original_placeholder_text_exactly(self):
        """Test that original placeholder text is preserved exactly, including whitespace."""
        processor = PlaceholderProcessor(data_sources={})
        
        # Test with various whitespace patterns
        content = """
{{  netbox.device_name  }}
{{ meta.organization.name}}
{{meta.ceo.name }}
"""
        
        result = processor.process_template(content)
        
        # All placeholders should remain exactly as they were
        assert '{{  netbox.device_name  }}' in result.content
        assert '{{ meta.organization.name}}' in result.content
        assert '{{meta.ceo.name }}' in result.content
    
    def test_mixed_available_and_unavailable_data(self):
        """Test that available data is replaced while unavailable data is preserved."""
        # Create processor with partial data
        mock_adapter = MockDataSourceAdapter({'device_name': 'server-01'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """
{{ netbox.device_name }}
{{ netbox.missing_field }}
{{ meta.organization.name }}
"""
        
        result = processor.process_template(content)
        
        # Available data should be replaced
        assert 'server-01' in result.content
        assert '{{ netbox.device_name }}' not in result.content
        
        # Unavailable data should be preserved
        assert '{{ netbox.missing_field }}' in result.content
        assert '{{ meta.organization.name }}' in result.content
        
        # Should have warnings for missing data
        assert len(result.warnings) >= 2


class TestPlaceholderProcessingUnitTests:
    """Additional unit tests for placeholder processing (Subtask 12.3)."""
    
    def test_placeholder_recognition_with_hyphens_in_source(self):
        """Test recognition of source names with hyphens (e.g., meta-netbox)."""
        processor = PlaceholderProcessor()
        content = '{{ meta-netbox.contacts.ciso.name }}'
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 1
        assert placeholders[0].source == 'meta-netbox'
        assert placeholders[0].field == 'contacts.ciso.name'
    
    def test_data_substitution_with_netbox_source(self):
        """Test data substitution from netbox source."""
        mock_adapter = MockDataSourceAdapter({
            'device_name': 'server-01',
            'site_name': 'datacenter-1',
            'ip_address': '192.168.1.100'
        })
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = """
{{ netbox.device_name }}
{{ netbox.site_name }}
{{ netbox.ip_address }}
"""
        
        result = processor.process_template(content)
        
        # All values should be substituted
        assert 'server-01' in result.content
        assert 'datacenter-1' in result.content
        assert '192.168.1.100' in result.content
        
        # No placeholders should remain
        assert '{{ netbox.' not in result.content
        
        # Should have 3 successful replacements
        assert len(result.replacements) == 3
    
    def test_data_substitution_with_meta_source(self):
        """Test data substitution from meta source."""
        mock_adapter = MockDataSourceAdapter({
            'organization.name': 'AdminSend GmbH',
            'ceo.name': 'Max Mustermann',
            'cio.email': 'cio@example.com'
        })
        processor = PlaceholderProcessor(data_sources={'meta': mock_adapter})
        
        content = """
{{ meta.organization.name }}
{{ meta.ceo.name }}
{{ meta.cio.email }}
"""
        
        result = processor.process_template(content)
        
        # All values should be substituted
        assert 'AdminSend GmbH' in result.content
        assert 'Max Mustermann' in result.content
        assert 'cio@example.com' in result.content
        
        # No placeholders should remain
        assert '{{ meta.' not in result.content
        
        # Should have 3 successful replacements
        assert len(result.replacements) == 3
    
    def test_fallback_behavior_for_missing_source(self):
        """Test fallback behavior when data source is not configured."""
        processor = PlaceholderProcessor(data_sources={'netbox': MockDataSourceAdapter({})})
        
        content = '{{ unknown_source.field }}'
        result = processor.process_template(content)
        
        # Placeholder should be preserved
        assert '{{ unknown_source.field }}' in result.content
        
        # Should generate warning with available sources
        assert len(result.warnings) >= 1
        warning_text = ' '.join(result.warnings).lower()
        assert 'unknown' in warning_text or 'not found' in warning_text
        assert 'available' in warning_text
    
    def test_fallback_behavior_for_missing_field(self):
        """Test fallback behavior when field is not found in source."""
        mock_adapter = MockDataSourceAdapter({'existing_field': 'value'})
        processor = PlaceholderProcessor(data_sources={'netbox': mock_adapter})
        
        content = '{{ netbox.nonexistent_field }}'
        result = processor.process_template(content)
        
        # Placeholder should be preserved
        assert '{{ netbox.nonexistent_field }}' in result.content
        
        # Should generate warning
        assert len(result.warnings) >= 1
        assert any('field_not_found' in w.lower() or 'not found' in w.lower() for w in result.warnings)
    
    def test_empty_template_handling(self):
        """Test handling of empty templates."""
        processor = PlaceholderProcessor()
        
        content = ''
        result = processor.process_template(content)
        
        assert result.content == ''
        assert len(result.replacements) == 0
        assert len(result.warnings) == 0
    
    def test_template_with_no_placeholders(self):
        """Test handling of templates without placeholders."""
        processor = PlaceholderProcessor()
        
        content = """# Compliance Framework
This is a template without any placeholders.
Just regular markdown content.
"""
        
        result = processor.process_template(content)
        
        # Content should remain unchanged
        assert result.content == content
        assert len(result.replacements) == 0
        assert len(result.warnings) == 0




class TestProperty15PlaceholderRecognition:
    """Property-based tests for Property 15: Placeholder Recognition (Subtask 12.4)."""
    
    @settings(max_examples=100)
    @given(
        num_placeholders=st.integers(min_value=1, max_value=20),
        data=st.data()
    )
    def test_property_15_placeholder_recognition(self, num_placeholders, data):
        """
        Property 15: Placeholder Recognition
        
        For any template containing valid {{ source.field }} syntax, the Placeholder_System
        must recognize and extract all placeholders.
        
        **Validates: Requirements 11.1, 11.2, 11.3**
        """
        processor = PlaceholderProcessor()
        
        # Generate template with various placeholder types
        template_lines = []
        expected_placeholders = []
        
        for i in range(num_placeholders):
            # Choose source type
            source = data.draw(st.sampled_from(['netbox', 'meta', 'meta-netbox', 'metadata']))
            
            # Generate field path (can be nested)
            if source == 'metadata':
                # Metadata has specific fields
                field = data.draw(st.sampled_from(['author', 'version', 'date']))
            else:
                # Generate nested field path
                num_parts = data.draw(st.integers(min_value=1, max_value=3))
                field_parts = []
                for _ in range(num_parts):
                    part = data.draw(st.text(
                        alphabet=st.characters(whitelist_categories=('Ll', 'Lu'), whitelist_characters='_'),
                        min_size=1,
                        max_size=10
                    ).filter(lambda x: x and x[0].isalpha()))
                    field_parts.append(part)
                field = '.'.join(field_parts)
            
            # Add optional whitespace
            ws_before = data.draw(st.text(alphabet=' \t', max_size=3))
            ws_after = data.draw(st.text(alphabet=' \t', max_size=3))
            
            placeholder = f'{{{{{ws_before}{source}.{field}{ws_after}}}}}'
            template_lines.append(placeholder)
            expected_placeholders.append((source, field))
        
        template_content = '\n'.join(template_lines)
        
        # Find placeholders
        found_placeholders = processor.find_placeholders(template_content)
        
        # Verify correct number of placeholders found
        assert len(found_placeholders) == num_placeholders, \
            f"Expected {num_placeholders} placeholders, found {len(found_placeholders)}"
        
        # Verify each placeholder is correctly parsed
        for i, placeholder in enumerate(found_placeholders):
            expected_source, expected_field = expected_placeholders[i]
            
            # Verify source is correctly extracted
            assert placeholder.source == expected_source, \
                f"Expected source '{expected_source}', got '{placeholder.source}'"
            
            # Verify field is correctly extracted
            assert placeholder.field == expected_field, \
                f"Expected field '{expected_field}', got '{placeholder.field}'"
            
            # Verify line number is valid
            assert placeholder.line_number > 0, \
                "Line number should be positive"
            assert placeholder.line_number <= len(template_lines), \
                "Line number should not exceed template line count"
            
            # Verify raw placeholder is captured
            assert placeholder.raw, \
                "Raw placeholder text should not be empty"
            assert '{{' in placeholder.raw and '}}' in placeholder.raw, \
                "Raw placeholder should contain {{ and }}"
    
    @settings(max_examples=100)
    @given(
        num_netbox=st.integers(min_value=0, max_value=10),
        num_meta=st.integers(min_value=0, max_value=10),
        num_metadata=st.integers(min_value=0, max_value=5),
        data=st.data()
    )
    def test_property_15_source_type_recognition(self, num_netbox, num_meta, num_metadata, data):
        """
        Property 15: Source Type Recognition
        
        For any template with multiple source types (netbox, meta, metadata), the system
        must correctly identify and categorize each placeholder by its source.
        
        **Validates: Requirements 11.2, 11.3**
        """
        # Skip if no placeholders
        if num_netbox + num_meta + num_metadata == 0:
            return
        
        processor = PlaceholderProcessor()
        template_lines = []
        
        # Add netbox placeholders
        for i in range(num_netbox):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=10
            ).filter(lambda x: x and x[0].isalpha()))
            template_lines.append(f'{{{{ netbox.{field} }}}}')
        
        # Add meta placeholders
        for i in range(num_meta):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=10
            ).filter(lambda x: x and x[0].isalpha()))
            template_lines.append(f'{{{{ meta.{field} }}}}')
        
        # Add metadata placeholders
        for i in range(num_metadata):
            field = data.draw(st.sampled_from(['author', 'version', 'date']))
            template_lines.append(f'{{{{ metadata.{field} }}}}')
        
        template_content = '\n'.join(template_lines)
        
        # Find placeholders
        found_placeholders = processor.find_placeholders(template_content)
        
        # Count by source
        netbox_count = sum(1 for p in found_placeholders if p.source == 'netbox')
        meta_count = sum(1 for p in found_placeholders if p.source == 'meta')
        metadata_count = sum(1 for p in found_placeholders if p.source == 'metadata')
        
        # Verify counts match expected
        assert netbox_count == num_netbox, \
            f"Expected {num_netbox} netbox placeholders, found {netbox_count}"
        assert meta_count == num_meta, \
            f"Expected {num_meta} meta placeholders, found {meta_count}"
        assert metadata_count == num_metadata, \
            f"Expected {num_metadata} metadata placeholders, found {metadata_count}"


class TestProperty16PlaceholderPreservation:
    """Property-based tests for Property 16: Placeholder Preservation on Missing Data (Subtask 12.5)."""
    
    @settings(max_examples=100)
    @given(
        num_available=st.integers(min_value=0, max_value=10),
        num_missing=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_16_placeholder_preservation_on_missing_data(self, num_available, num_missing, data):
        """
        Property 16: Placeholder Preservation on Missing Data
        
        For any placeholder where the data source is unavailable, the original placeholder
        text must be preserved in the output (not replaced with empty string or error message).
        
        **Validates: Requirements 11.4**
        """
        # Generate available and missing fields
        available_fields = {}
        missing_placeholders = []
        template_lines = []
        
        source = 'netbox'
        
        # Add available fields
        for i in range(num_available):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=10
            ).filter(lambda x: x and x[0].isalpha()))
            value = data.draw(st.text(min_size=1, max_size=50))
            
            available_fields[field] = value
            template_lines.append(f'{{{{ {source}.{field} }}}}')
        
        # Add missing fields
        for i in range(num_missing):
            field = data.draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                min_size=1,
                max_size=10
            ).filter(lambda x: x and x[0].isalpha() and x not in available_fields))
            
            placeholder_text = f'{{{{ {source}.{field} }}}}'
            missing_placeholders.append(placeholder_text)
            template_lines.append(placeholder_text)
        
        template_content = '\n'.join(template_lines)
        
        # Create processor with only available fields
        mock_adapter = MockDataSourceAdapter(available_fields)
        processor = PlaceholderProcessor(data_sources={source: mock_adapter})
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify available fields were replaced
        assert len(result.replacements) == num_available, \
            f"Expected {num_available} replacements, got {len(result.replacements)}"
        
        for field, value in available_fields.items():
            assert value in result.content, \
                f"Available field value '{value}' should be in content"
        
        # Verify missing placeholders are preserved exactly
        for placeholder in missing_placeholders:
            assert placeholder in result.content, \
                f"Missing placeholder '{placeholder}' should be preserved in content"
        
        # Verify warnings were generated for missing fields
        assert len(result.warnings) >= num_missing, \
            f"Expected at least {num_missing} warnings for missing fields"
        
        # Verify no empty strings or error messages replaced placeholders
        for placeholder in missing_placeholders:
            # The placeholder should still be in the content
            assert placeholder in result.content, \
                f"Placeholder '{placeholder}' should not be replaced with empty string or error"
    
    @settings(max_examples=100)
    @given(
        num_sources=st.integers(min_value=1, max_value=5),
        data=st.data()
    )
    def test_property_16_preservation_across_multiple_sources(self, num_sources, data):
        """
        Property 16: Preservation Across Multiple Sources
        
        For any template with placeholders from multiple sources, missing data from any
        source must be preserved while available data is replaced.
        
        **Validates: Requirements 11.4, 11.6**
        """
        # Generate sources with partial data
        sources = ['netbox', 'meta', 'database', 'api', 'ldap'][:num_sources]
        
        adapters = {}
        template_lines = []
        expected_preserved = []
        expected_replaced = []
        
        for source in sources:
            # Each source has some available and some missing fields
            has_available = data.draw(st.booleans())
            has_missing = data.draw(st.booleans())
            
            used_fields = set()
            
            if has_available:
                # Add available field
                field = data.draw(st.text(
                    alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                    min_size=1,
                    max_size=10
                ).filter(lambda x: x and x[0].isalpha() and x not in used_fields))
                used_fields.add(field)
                value = data.draw(st.text(min_size=1, max_size=50))
                
                adapters[source] = MockDataSourceAdapter({field: value})
                template_lines.append(f'{{{{ {source}.{field} }}}}')
                expected_replaced.append(value)
            
            if has_missing:
                # Add missing field (different from available field)
                field = data.draw(st.text(
                    alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
                    min_size=1,
                    max_size=10
                ).filter(lambda x: x and x[0].isalpha() and x not in used_fields))
                
                placeholder = f'{{{{ {source}.{field} }}}}'
                template_lines.append(placeholder)
                expected_preserved.append(placeholder)
                
                # Ensure adapter exists but doesn't have this field
                if source not in adapters:
                    adapters[source] = MockDataSourceAdapter({})
        
        # Skip if no template content
        if not template_lines:
            return
        
        template_content = '\n'.join(template_lines)
        
        # Create processor
        processor = PlaceholderProcessor(data_sources=adapters)
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify replaced values are in content
        for value in expected_replaced:
            assert value in result.content, \
                f"Replaced value '{value}' should be in content"
        
        # Verify preserved placeholders are in content
        for placeholder in expected_preserved:
            assert placeholder in result.content, \
                f"Preserved placeholder '{placeholder}' should be in content"
    
    @settings(max_examples=100)
    @given(
        source=st.sampled_from(['netbox', 'meta', 'database', 'api']),
        field=st.text(
            alphabet=st.characters(whitelist_categories=('Ll',), whitelist_characters='_'),
            min_size=1,
            max_size=15
        ).filter(lambda x: x and x[0].isalpha() and 
                 'error' not in x.lower() and 
                 'fail' not in x.lower() and
                 'warning' not in x.lower()),
        ws_before=st.text(alphabet=' \t', max_size=3),
        ws_after=st.text(alphabet=' \t', max_size=3)
    )
    def test_property_16_exact_preservation_of_placeholder_text(self, source, field, ws_before, ws_after):
        """
        Property 16: Exact Preservation of Placeholder Text
        
        For any placeholder with missing data, the exact original text (including whitespace
        and formatting) must be preserved in the output.
        
        **Validates: Requirements 11.4**
        
        Note: Field names containing 'error', 'fail', or 'warning' are filtered out to avoid
        false positives when checking for error messages in output.
        """
        # Create processor without data sources
        processor = PlaceholderProcessor(data_sources={})
        
        # Create placeholder with specific whitespace
        placeholder_text = f'{{{{{ws_before}{source}.{field}{ws_after}}}}}'
        
        # Create template with the placeholder
        template_content = f"# Header\n{placeholder_text}\n# Footer"
        
        # Process template
        result = processor.process_template(template_content)
        
        # Verify placeholder is preserved exactly
        assert placeholder_text in result.content, \
            f"Placeholder text '{placeholder_text}' should be preserved exactly in content"
        
        # Verify it wasn't replaced with empty string
        assert result.content != "# Header\n\n# Footer", \
            "Placeholder should not be replaced with empty string"
        
        # Verify it wasn't replaced with error message
        # Check for error message patterns, not just the word "ERROR"
        assert "ERROR:" not in result.content.upper(), \
            "Placeholder should not be replaced with error message"
        assert "[ERROR]" not in result.content.upper(), \
            "Placeholder should not be replaced with error marker"
