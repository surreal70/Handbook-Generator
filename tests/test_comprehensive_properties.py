"""
Comprehensive property-based tests for template system extension.

This module contains property tests for universal correctness properties
that should hold across all template types and configurations.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import os
import re
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest

from src.template_manager import TemplateManager
from src.placeholder_processor import PlaceholderProcessor
from src.html_comment_processor import HTMLCommentProcessor


class TestTemplateTypeDiscovery:
    """
    Property 3: Template Type Discovery
    
    For any valid template directory structure, the system SHALL discover all template types
    (it-operation, bcm, isms, bsi-grundschutz) and correctly identify available languages
    for each type.
    
    Validates: Requirements 21.1, 21.2, 21.3, 21.4
    """
    
    @pytest.fixture
    def template_manager(self):
        """Get template manager instance."""
        return TemplateManager(Path("templates"))
    
    def test_all_template_types_discoverable(self, template_manager):
        """
        Test that all implemented template types are discoverable.
        
        Feature: template-system-extension
        Property 3: Template Type Discovery
        """
        discovered = template_manager.discover_templates()
        
        # Should discover at least one language
        assert len(discovered) > 0, "Should discover at least one language"
        
        # Expected template types that should exist
        expected_types = ['it-operation', 'bcm', 'isms', 'bsi-grundschutz']
        
        # Check each language for template types
        for language, categories in discovered.items():
            # Should have at least one template type
            assert len(categories) > 0, f"Language {language} should have at least one template type"
            
            # Check which expected types are present
            found_types = [t for t in expected_types if t in categories]
            
            # Should have at least one of the expected types
            assert len(found_types) > 0, \
                f"Language {language} should have at least one of: {expected_types}"
    
    def test_bilingual_support_for_template_types(self, template_manager):
        """
        Test that core template types are available in both German and English.
        
        Feature: template-system-extension
        Property 3: Template Type Discovery
        """
        discovered = template_manager.discover_templates()
        
        # Should have both German and English
        assert 'de' in discovered, "Should discover German templates"
        assert 'en' in discovered, "Should discover English templates"
        
        # Get template types for each language
        de_types = set(discovered['de'].keys())
        en_types = set(discovered['en'].keys())
        
        # Core template types that should exist in both languages
        core_types = {'it-operation', 'bcm', 'isms', 'bsi-grundschutz'}
        
        # Check that core types exist in both languages
        de_core = de_types & core_types
        en_core = en_types & core_types
        
        # Both languages should have the same core template types
        assert de_core == en_core, \
            f"German and English should have same core template types. DE: {de_core}, EN: {en_core}"
        
        # Should have at least 3 core types
        assert len(de_core) >= 3, \
            f"Should have at least 3 core template types, found {len(de_core)}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['it-operation', 'bcm', 'isms', 'bsi-grundschutz'])
    )
    def test_property_template_type_discovery(self, template_manager, language, template_type):
        """
        Property test: For any valid language and template type combination,
        the system should discover templates if they exist.
        
        Feature: template-system-extension
        Property 3: Template Type Discovery
        
        Validates: Requirements 21.1, 21.2, 21.3, 21.4
        """
        discovered = template_manager.discover_templates()
        
        # If language exists in discovered templates
        if language in discovered:
            # If template type exists for this language
            if template_type in discovered[language]:
                # Should have at least one template file
                template_files = discovered[language][template_type]
                assert len(template_files) > 0, \
                    f"Template type {template_type} for {language} should have at least one file"
                
                # All files should be .md files
                for template_file in template_files:
                    assert template_file.suffix == '.md', \
                        f"Template file {template_file} should be a .md file"
                    
                    # File should exist
                    assert template_file.exists(), \
                        f"Template file {template_file} should exist"
    
    def test_template_directory_structure(self, template_manager):
        """
        Test that template directory structure follows expected pattern.
        
        Feature: template-system-extension
        Property 3: Template Type Discovery
        """
        template_root = Path("templates")
        
        # Template root should exist
        assert template_root.exists(), "Template root directory should exist"
        
        # Should have language directories
        language_dirs = [d for d in template_root.iterdir() if d.is_dir()]
        assert len(language_dirs) > 0, "Should have at least one language directory"
        
        # Each language directory should have template type subdirectories
        for lang_dir in language_dirs:
            if lang_dir.name in ['de', 'en']:  # Only check known languages
                type_dirs = [d for d in lang_dir.iterdir() if d.is_dir()]
                assert len(type_dirs) > 0, \
                    f"Language directory {lang_dir.name} should have template type subdirectories"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_type=st.sampled_from(['it-operation', 'bcm', 'isms', 'bsi-grundschutz'])
    )
    def test_property_template_type_consistency(self, template_manager, template_type):
        """
        Property test: For any template type, if it exists in one language,
        it should exist in all supported languages.
        
        Feature: template-system-extension
        Property 3: Template Type Discovery
        
        Validates: Requirements 21.1, 21.2, 21.3
        """
        discovered = template_manager.discover_templates()
        
        # Get languages that have this template type
        languages_with_type = [
            lang for lang, categories in discovered.items()
            if template_type in categories
        ]
        
        # If template type exists in any language
        if languages_with_type:
            # Should exist in both de and en
            if 'de' in discovered and 'en' in discovered:
                if template_type in discovered['de']:
                    assert template_type in discovered['en'], \
                        f"Template type {template_type} exists in German but not in English"
                if template_type in discovered['en']:
                    assert template_type in discovered['de'], \
                        f"Template type {template_type} exists in English but not in German"




class TestPlaceholderProcessingIndependence:
    """
    Property 5: Placeholder Processing Independence
    
    For any template type (it-operation, bcm, isms, bsi-grundschutz), placeholder processing
    SHALL work identically, replacing {{ meta.* }} and {{ netbox.* }} placeholders with the
    same data sources.
    
    Validates: Requirements 20.1, 24.1, 24.2
    """
    
    @pytest.fixture
    def placeholder_processor(self):
        """Get placeholder processor with mock data sources."""
        # Create mock data sources
        class MockDataSource:
            def __init__(self, data):
                self.data = data
            
            def get_field(self, field):
                parts = field.split('.')
                value = self.data
                for part in parts:
                    if isinstance(value, dict) and part in value:
                        value = value[part]
                    else:
                        return None
                return value
        
        meta_data = {
            'organization': {'name': 'Test Organization'},
            'cio': {'name': 'John Doe', 'email': 'john@example.com'},
            'document': {'owner': 'Jane Smith', 'version': '1.0'}
        }
        
        netbox_data = {
            'site': {'name': 'Main Site'},
            'device': {'name': 'Server01'},
            'vlan': {'management': {'vid': '100'}}
        }
        
        data_sources = {
            'meta': MockDataSource(meta_data),
            'netbox': MockDataSource(netbox_data)
        }
        
        return PlaceholderProcessor(data_sources=data_sources)
    
    def test_meta_placeholders_work_across_template_types(self, placeholder_processor):
        """
        Test that meta placeholders work identically across all template types.
        
        Feature: template-system-extension
        Property 5: Placeholder Processing Independence
        """
        # Test content with meta placeholders
        content = """
        Organization: {{ meta.organization.name }}
        CIO: {{ meta.cio.name }}
        Owner: {{ meta.document.owner }}
        """
        
        result = placeholder_processor.process_template(content)
        
        # Should have 3 successful replacements
        assert len(result.replacements) == 3, \
            f"Should have 3 replacements, found {len(result.replacements)}"
        
        # All replacements should be from 'meta' source
        for replacement in result.replacements:
            assert replacement.source == 'meta', \
                f"Replacement should be from 'meta' source, found '{replacement.source}'"
        
        # Verify actual replacements
        assert 'Test Organization' in result.content
        assert 'John Doe' in result.content
        assert 'Jane Smith' in result.content
    
    def test_netbox_placeholders_work_across_template_types(self, placeholder_processor):
        """
        Test that netbox placeholders work identically across all template types.
        
        Feature: template-system-extension
        Property 5: Placeholder Processing Independence
        """
        # Test content with netbox placeholders
        content = """
        Site: {{ netbox.site.name }}
        Device: {{ netbox.device.name }}
        VLAN: {{ netbox.vlan.management.vid }}
        """
        
        result = placeholder_processor.process_template(content)
        
        # Should have 3 successful replacements
        assert len(result.replacements) == 3, \
            f"Should have 3 replacements, found {len(result.replacements)}"
        
        # All replacements should be from 'netbox' source
        for replacement in result.replacements:
            assert replacement.source == 'netbox', \
                f"Replacement should be from 'netbox' source, found '{replacement.source}'"
        
        # Verify actual replacements
        assert 'Main Site' in result.content
        assert 'Server01' in result.content
        assert '100' in result.content
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        placeholder_source=st.sampled_from(['meta', 'netbox']),
        field_depth=st.integers(min_value=1, max_value=3)
    )
    def test_property_placeholder_processing_independence(
        self, placeholder_processor, placeholder_source, field_depth
    ):
        """
        Property test: For any placeholder source (meta or netbox) and field depth,
        placeholder processing should work identically regardless of template type.
        
        Feature: template-system-extension
        Property 5: Placeholder Processing Independence
        
        Validates: Requirements 20.1, 24.1, 24.2
        """
        # Build a field path based on depth
        if placeholder_source == 'meta':
            field_paths = {
                1: 'organization',
                2: 'organization.name',
                3: 'cio.email'
            }
        else:  # netbox
            field_paths = {
                1: 'site',
                2: 'site.name',
                3: 'vlan.management.vid'
            }
        
        field_path = field_paths.get(field_depth, field_paths[1])
        
        # Create test content with placeholder
        content = f"Value: {{{{ {placeholder_source}.{field_path} }}}}"
        
        # Process the template
        result = placeholder_processor.process_template(content)
        
        # Should have at least one replacement or one warning
        total_results = len(result.replacements) + len(result.warnings)
        assert total_results > 0, \
            "Should have at least one replacement or warning"
        
        # If replacement was successful, verify source
        if result.replacements:
            assert result.replacements[0].source == placeholder_source, \
                f"Replacement source should be '{placeholder_source}'"
    
    def test_mixed_placeholders_work_together(self, placeholder_processor):
        """
        Test that meta and netbox placeholders can coexist in the same template.
        
        Feature: template-system-extension
        Property 5: Placeholder Processing Independence
        """
        content = """
        Organization: {{ meta.organization.name }}
        Site: {{ netbox.site.name }}
        CIO: {{ meta.cio.name }}
        Device: {{ netbox.device.name }}
        """
        
        result = placeholder_processor.process_template(content)
        
        # Should have 4 successful replacements
        assert len(result.replacements) == 4, \
            f"Should have 4 replacements, found {len(result.replacements)}"
        
        # Should have both meta and netbox sources
        sources_used = result.get_sources_used()
        assert 'meta' in sources_used, "Should have meta replacements"
        assert 'netbox' in sources_used, "Should have netbox replacements"
        
        # Should have 2 replacements from each source
        assert result.get_replacement_count_by_source('meta') == 2
        assert result.get_replacement_count_by_source('netbox') == 2
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        num_meta=st.integers(min_value=0, max_value=5),
        num_netbox=st.integers(min_value=0, max_value=5)
    )
    def test_property_mixed_placeholder_independence(
        self, placeholder_processor, num_meta, num_netbox
    ):
        """
        Property test: For any combination of meta and netbox placeholders,
        processing should work independently for each source.
        
        Feature: template-system-extension
        Property 5: Placeholder Processing Independence
        
        Validates: Requirements 20.1, 24.1, 24.2
        """
        # Build content with specified number of placeholders
        lines = []
        
        for i in range(num_meta):
            lines.append(f"Meta{i}: {{{{ meta.organization.name }}}}")
        
        for i in range(num_netbox):
            lines.append(f"NetBox{i}: {{{{ netbox.site.name }}}}")
        
        content = '\n'.join(lines)
        
        # Process the template
        result = placeholder_processor.process_template(content)
        
        # Should have expected number of replacements
        expected_total = num_meta + num_netbox
        assert len(result.replacements) == expected_total, \
            f"Should have {expected_total} replacements, found {len(result.replacements)}"
        
        # Verify source counts
        if num_meta > 0:
            assert result.get_replacement_count_by_source('meta') == num_meta
        if num_netbox > 0:
            assert result.get_replacement_count_by_source('netbox') == num_netbox
    
    def test_placeholder_syntax_consistency(self, placeholder_processor):
        """
        Test that placeholder syntax is consistent across all sources.
        
        Feature: template-system-extension
        Property 5: Placeholder Processing Independence
        """
        # Test various valid placeholder syntaxes
        test_cases = [
            "{{ meta.organization.name }}",  # Standard spacing
            "{{meta.organization.name}}",    # No spacing
            "{{  meta.organization.name  }}", # Extra spacing
        ]
        
        for test_content in test_cases:
            result = placeholder_processor.process_template(test_content)
            
            # Should have exactly one replacement
            assert len(result.replacements) == 1, \
                f"Should have 1 replacement for '{test_content}', found {len(result.replacements)}"
            
            # Should replace with correct value
            assert 'Test Organization' in result.content, \
                f"Should replace placeholder in '{test_content}'"




class TestTemplateNumberingSequence:
    """
    Property 6: Template Numbering Sequence
    
    For any set of templates in a template type directory, when sorted by filename,
    the numeric prefixes SHALL form a valid sequence with no duplicates.
    
    Validates: Requirements 23.2, 23.3, 23.4, 23.5
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_template_numbering_no_duplicates(self, template_base_path):
        """
        Test that template numbering has no duplicates within each template type.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        """
        for language in ['de', 'en']:
            for template_type in ['it-operation', 'bcm', 'isms', 'bsi-grundschutz']:
                template_dir = template_base_path / language / template_type
                
                if not template_dir.exists():
                    continue
                
                # Get all template files (excluding metadata)
                templates = [
                    f for f in os.listdir(template_dir)
                    if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
                ]
                
                # Extract numbers
                numbers = [int(f[:4]) for f in templates]
                
                # Check for duplicates
                assert len(numbers) == len(set(numbers)), \
                    f"Template numbering should have no duplicates in {language}/{template_type}. " \
                    f"Found: {sorted(numbers)}"
    
    def test_template_numbering_ascending_order(self, template_base_path):
        """
        Test that template numbers are in ascending order.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        """
        for language in ['de', 'en']:
            for template_type in ['it-operation', 'bcm', 'isms', 'bsi-grundschutz']:
                template_dir = template_base_path / language / template_type
                
                if not template_dir.exists():
                    continue
                
                # Get all template files (excluding metadata)
                templates = sorted([
                    f for f in os.listdir(template_dir)
                    if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
                ])
                
                # Extract numbers
                numbers = [int(f[:4]) for f in templates]
                
                # Check ascending order
                assert numbers == sorted(numbers), \
                    f"Template numbers should be in ascending order in {language}/{template_type}. " \
                    f"Found: {numbers}"
    
    def test_template_numbering_four_digits(self, template_base_path):
        """
        Test that all template numbers use 4-digit format.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        """
        for language in ['de', 'en']:
            for template_type in ['it-operation', 'bcm', 'isms', 'bsi-grundschutz']:
                template_dir = template_base_path / language / template_type
                
                if not template_dir.exists():
                    continue
                
                # Get all template files
                templates = [
                    f for f in os.listdir(template_dir)
                    if f.endswith('.md') and f.startswith('0')
                ]
                
                for template in templates:
                    # First 4 characters should be digits
                    assert template[:4].isdigit(), \
                        f"Template {template} should start with 4-digit number in {language}/{template_type}"
                    
                    # Should have underscore after number
                    assert template[4] == '_', \
                        f"Template {template} should have underscore after number in {language}/{template_type}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['it-operation', 'bcm', 'isms', 'bsi-grundschutz'])
    )
    def test_property_template_numbering_sequence(self, template_base_path, language, template_type):
        """
        Property test: For any template type and language, template numbering should
        form a valid sequence with no duplicates and in ascending order.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        
        Validates: Requirements 23.2, 23.3, 23.4, 23.5
        """
        template_dir = template_base_path / language / template_type
        
        if not template_dir.exists():
            return  # Skip if template type doesn't exist
        
        # Get all template files (excluding metadata)
        templates = sorted([
            f for f in os.listdir(template_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ])
        
        if not templates:
            return  # Skip if no templates
        
        # Extract numbers
        numbers = [int(f[:4]) for f in templates]
        
        # Property 1: No duplicates
        assert len(numbers) == len(set(numbers)), \
            f"Template numbering should have no duplicates"
        
        # Property 2: Ascending order
        assert numbers == sorted(numbers), \
            f"Template numbers should be in ascending order"
        
        # Property 3: All numbers are 4 digits (10-9999)
        for num in numbers:
            assert 10 <= num <= 9999, \
                f"Template number {num} should be between 0010 and 9999"
    
    def test_bcm_template_numbering_range(self, template_base_path):
        """
        Test that BCM templates use numbering range 0010-0290.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        """
        for language in ['de', 'en']:
            bcm_dir = template_base_path / language / "bcm"
            
            if not bcm_dir.exists():
                continue
            
            # Get all BCM template files (excluding metadata)
            templates = [
                f for f in os.listdir(bcm_dir)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            ]
            
            # Extract numbers
            numbers = [int(f[:4]) for f in templates]
            
            # All numbers should be in range 10-290
            for num in numbers:
                assert 10 <= num <= 290, \
                    f"BCM template number {num} should be between 0010 and 0290 for {language}"
    
    def test_isms_template_numbering_range(self, template_base_path):
        """
        Test that ISMS templates use numbering range 0010-0740.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        """
        for language in ['de', 'en']:
            isms_dir = template_base_path / language / "isms"
            
            if not isms_dir.exists():
                continue
            
            # Get all ISMS template files (excluding metadata)
            templates = [
                f for f in os.listdir(isms_dir)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            ]
            
            # Extract numbers
            numbers = [int(f[:4]) for f in templates]
            
            # All numbers should be in range 10-740
            for num in numbers:
                assert 10 <= num <= 740, \
                    f"ISMS template number {num} should be between 0010 and 0740 for {language}"
    
    def test_bsi_template_numbering_range(self, template_base_path):
        """
        Test that BSI Grundschutz templates use numbering range 0010-0740.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        """
        for language in ['de', 'en']:
            bsi_dir = template_base_path / language / "bsi-grundschutz"
            
            if not bsi_dir.exists():
                continue
            
            # Get all BSI template files (excluding metadata)
            templates = [
                f for f in os.listdir(bsi_dir)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            ]
            
            # Extract numbers
            numbers = [int(f[:4]) for f in templates]
            
            # All numbers should be in range 10-740
            for num in numbers:
                assert 10 <= num <= 740, \
                    f"BSI template number {num} should be between 0010 and 0740 for {language}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz'])
    )
    def test_property_template_type_numbering_ranges(self, template_base_path, template_type):
        """
        Property test: For any template type, all template numbers should fall within
        the defined range for that type.
        
        Feature: template-system-extension
        Property 6: Template Numbering Sequence
        
        Validates: Requirements 23.2, 23.3, 23.4, 23.5
        """
        # Define expected ranges for each template type
        ranges = {
            'bcm': (10, 290),
            'isms': (10, 740),
            'bsi-grundschutz': (10, 740)
        }
        
        min_num, max_num = ranges[template_type]
        
        for language in ['de', 'en']:
            template_dir = template_base_path / language / template_type
            
            if not template_dir.exists():
                continue
            
            # Get all template files (excluding metadata)
            templates = [
                f for f in os.listdir(template_dir)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            ]
            
            # Extract numbers
            numbers = [int(f[:4]) for f in templates]
            
            # All numbers should be within range
            for num in numbers:
                assert min_num <= num <= max_num, \
                    f"Template number {num} in {template_type} should be between " \
                    f"{min_num:04d} and {max_num:04d} for {language}"




class TestOutputStructureConsistency:
    """
    Property 9: Output Structure Consistency
    
    For any template type and language combination, generated output SHALL be stored in
    `Handbook/{language}/{template-type}/` with filenames following the pattern
    `{template-type}_handbook_{language}.{ext}`.
    
    Validates: Requirements 25.1, 25.2, 25.3
    """
    
    def test_output_directory_structure_pattern(self):
        """
        Test that output directory follows expected pattern.
        
        Feature: template-system-extension
        Property 9: Output Structure Consistency
        """
        # Expected pattern: Handbook/{language}/{template-type}/
        handbook_dir = Path("Handbook")
        
        if not handbook_dir.exists():
            pytest.skip("Handbook directory does not exist yet")
        
        # Check for language directories
        for lang_dir in handbook_dir.iterdir():
            if lang_dir.is_dir() and lang_dir.name in ['de', 'en']:
                # Should have template type subdirectories
                assert any(lang_dir.iterdir()), \
                    f"Language directory {lang_dir.name} should have template type subdirectories"
    
    def test_output_filename_pattern(self):
        """
        Test that output filenames follow expected pattern for new template types.
        
        Feature: template-system-extension
        Property 9: Output Structure Consistency
        """
        handbook_dir = Path("Handbook")
        
        if not handbook_dir.exists():
            pytest.skip("Handbook directory does not exist yet")
        
        # Pattern: {template-type}_handbook.{ext} (language is in directory structure)
        filename_pattern = re.compile(r'^([a-z-]+)_handbook\.(md|pdf)$')
        
        # New template types that should follow the pattern
        new_template_types = ['bcm', 'isms', 'bsi-grundschutz']
        
        # Check all files in handbook directories
        for lang_dir in handbook_dir.iterdir():
            if not lang_dir.is_dir():
                continue
            
            for type_dir in lang_dir.iterdir():
                if not type_dir.is_dir():
                    continue
                
                # Only check new template types
                if type_dir.name not in new_template_types:
                    continue
                
                for file in type_dir.iterdir():
                    if file.is_file() and file.suffix in ['.md', '.pdf']:
                        assert filename_pattern.match(file.name), \
                            f"Output filename {file.name} should follow pattern " \
                            f"{{template-type}}_handbook_{{language}}.{{ext}}"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['it-operation', 'bcm', 'isms', 'bsi-grundschutz']),
        extension=st.sampled_from(['md', 'pdf'])
    )
    def test_property_output_structure_consistency(self, language, template_type, extension):
        """
        Property test: For any template type, language, and output format combination,
        the output path should follow the consistent pattern.
        
        Feature: template-system-extension
        Property 9: Output Structure Consistency
        
        Validates: Requirements 25.1, 25.2, 25.3
        """
        # Expected directory structure
        expected_dir = Path("Handbook") / language / template_type
        
        # Expected filename
        expected_filename = f"{template_type}_handbook_{language}.{extension}"
        expected_path = expected_dir / expected_filename
        
        # Verify pattern components
        assert expected_dir.parts[0] == "Handbook", \
            "Output should be in Handbook directory"
        
        assert expected_dir.parts[1] == language, \
            f"Language directory should be {language}"
        
        assert expected_dir.parts[2] == template_type, \
            f"Template type directory should be {template_type}"
        
        assert expected_filename.startswith(template_type), \
            f"Filename should start with template type {template_type}"
        
        assert f"_handbook_{language}" in expected_filename, \
            f"Filename should contain _handbook_{language}"
        
        assert expected_filename.endswith(f".{extension}"), \
            f"Filename should end with .{extension}"
    
    def test_output_directory_creation_pattern(self):
        """
        Test that output directories can be created following the pattern.
        
        Feature: template-system-extension
        Property 9: Output Structure Consistency
        """
        import tempfile
        import shutil
        
        # Create temporary directory for testing
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            
            # Test creating output structure
            for language in ['de', 'en']:
                for template_type in ['bcm', 'isms']:
                    output_dir = tmpdir_path / "Handbook" / language / template_type
                    output_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Verify directory was created
                    assert output_dir.exists(), \
                        f"Output directory should be created: {output_dir}"
                    
                    # Verify it's a directory
                    assert output_dir.is_dir(), \
                        f"Output path should be a directory: {output_dir}"
    
    @settings(max_examples=100)
    @given(
        template_type=st.sampled_from(['it-operation', 'bcm', 'isms', 'bsi-grundschutz'])
    )
    def test_property_bilingual_output_structure(self, template_type):
        """
        Property test: For any template type, output structure should be consistent
        across both German and English.
        
        Feature: template-system-extension
        Property 9: Output Structure Consistency
        
        Validates: Requirements 25.1, 25.2, 25.3
        """
        # Both languages should have same structure
        de_dir = Path("Handbook") / "de" / template_type
        en_dir = Path("Handbook") / "en" / template_type
        
        # Directory structure should be parallel
        assert de_dir.parts[0] == en_dir.parts[0] == "Handbook", \
            "Both should be in Handbook directory"
        
        assert de_dir.parts[2] == en_dir.parts[2] == template_type, \
            "Both should have same template type directory"
        
        # Filenames should follow same pattern with different language
        de_filename = f"{template_type}_handbook_de.md"
        en_filename = f"{template_type}_handbook_en.md"
        
        # Extract template type from both filenames
        de_prefix = de_filename.split('_handbook_')[0]
        en_prefix = en_filename.split('_handbook_')[0]
        
        assert de_prefix == en_prefix == template_type, \
            "Both filenames should have same template type prefix"




class TestBackwardCompatibility:
    """
    Property 10: Backward Compatibility
    
    For any existing it-operation template, processing with the extended system SHALL
    produce identical output to the original system (when HTML comments are not present).
    
    Validates: Requirements 20.1, 20.2, 20.3, 20.4, 20.5
    """
    
    @pytest.fixture
    def template_manager(self):
        """Get template manager instance."""
        return TemplateManager(Path("templates"))
    
    @pytest.fixture
    def placeholder_processor(self):
        """Get placeholder processor with mock data sources."""
        class MockDataSource:
            def __init__(self, data):
                self.data = data
            
            def get_field(self, field):
                parts = field.split('.')
                value = self.data
                for part in parts:
                    if isinstance(value, dict) and part in value:
                        value = value[part]
                    else:
                        return None
                return value
        
        meta_data = {
            'organization': {'name': 'Test Org'},
            'document': {'owner': 'Test Owner'}
        }
        
        data_sources = {'meta': MockDataSource(meta_data)}
        return PlaceholderProcessor(data_sources=data_sources)
    
    def test_it_operation_templates_still_work(self, template_manager):
        """
        Test that existing it-operation templates can still be discovered and loaded.
        
        Feature: template-system-extension
        Property 10: Backward Compatibility
        """
        # Should be able to get it-operation templates
        for language in ['de', 'en']:
            templates = template_manager.get_templates(language, 'it-operation')
            
            # Should have templates
            assert len(templates) > 0, \
                f"Should have it-operation templates for {language}"
            
            # Should be able to read content
            for template in templates[:3]:  # Test first 3
                content = template.read_content()
                assert len(content) > 0, \
                    f"Template {template.path.name} should have content"
    
    def test_existing_placeholder_syntax_still_works(self, placeholder_processor):
        """
        Test that existing placeholder syntax continues to work.
        
        Feature: template-system-extension
        Property 10: Backward Compatibility
        """
        # Test existing meta placeholder syntax
        content = "Organization: {{ meta.organization.name }}"
        
        result = placeholder_processor.process_template(content)
        
        # Should have successful replacement
        assert len(result.replacements) == 1, \
            "Existing placeholder syntax should still work"
        
        assert 'Test Org' in result.content, \
            "Placeholder should be replaced with correct value"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_backward_compatibility(self, template_manager, language):
        """
        Property test: For any language, existing it-operation templates should
        continue to work with the extended system.
        
        Feature: template-system-extension
        Property 10: Backward Compatibility
        
        Validates: Requirements 20.1, 20.2, 20.3, 20.4, 20.5
        """
        # Should be able to discover it-operation templates
        discovered = template_manager.discover_templates()
        
        assert language in discovered, \
            f"Should discover {language} templates"
        
        assert 'it-operation' in discovered[language], \
            f"Should discover it-operation templates for {language}"
        
        # Should be able to get templates
        templates = template_manager.get_templates(language, 'it-operation')
        
        assert len(templates) > 0, \
            f"Should have it-operation templates for {language}"
        
        # Should be able to read template content
        for template in templates[:5]:  # Test first 5
            content = template.read_content()
            assert isinstance(content, str), \
                "Template content should be string"
            assert len(content) > 0, \
                "Template should have content"
    
    def test_template_manager_api_unchanged(self, template_manager):
        """
        Test that TemplateManager API remains unchanged for backward compatibility.
        
        Feature: template-system-extension
        Property 10: Backward Compatibility
        """
        # Test that existing methods still exist and work
        assert hasattr(template_manager, 'discover_templates'), \
            "TemplateManager should have discover_templates method"
        
        assert hasattr(template_manager, 'get_templates'), \
            "TemplateManager should have get_templates method"
        
        assert hasattr(template_manager, 'validate_template_exists'), \
            "TemplateManager should have validate_template_exists method"
        
        # Test that methods work
        discovered = template_manager.discover_templates()
        assert isinstance(discovered, dict), \
            "discover_templates should return dict"
        
        templates = template_manager.get_templates('de', 'it-operation')
        assert isinstance(templates, list), \
            "get_templates should return list"
    
    def test_placeholder_processor_api_unchanged(self, placeholder_processor):
        """
        Test that PlaceholderProcessor API remains unchanged for backward compatibility.
        
        Feature: template-system-extension
        Property 10: Backward Compatibility
        """
        # Test that existing methods still exist and work
        assert hasattr(placeholder_processor, 'find_placeholders'), \
            "PlaceholderProcessor should have find_placeholders method"
        
        assert hasattr(placeholder_processor, 'process_template'), \
            "PlaceholderProcessor should have process_template method"
        
        # Test that methods work
        content = "Test: {{ meta.organization.name }}"
        
        placeholders = placeholder_processor.find_placeholders(content)
        assert isinstance(placeholders, list), \
            "find_placeholders should return list"
        
        result = placeholder_processor.process_template(content)
        assert hasattr(result, 'content'), \
            "ProcessingResult should have content attribute"
        assert hasattr(result, 'replacements'), \
            "ProcessingResult should have replacements attribute"




class TestHTMLCommentMultilineHandling:
    """
    Property 11: HTML Comment Multiline Handling
    
    For any HTML comment spanning multiple lines, the entire comment including all
    intermediate lines SHALL be removed, leaving no comment markers or partial comment content.
    
    Validates: Requirements 16.3, 17.2
    """
    
    @pytest.fixture
    def html_comment_processor(self):
        """Get HTML comment processor instance."""
        return HTMLCommentProcessor()
    
    def test_multiline_comment_removal(self, html_comment_processor):
        """
        Test that multiline HTML comments are completely removed.
        
        Feature: template-system-extension
        Property 11: HTML Comment Multiline Handling
        """
        content = """
        Line before comment
        <!-- This is a
        multiline
        comment -->
        Line after comment
        """
        
        result = html_comment_processor.remove_comments(content)
        
        # Should not contain comment markers
        assert '<!--' not in result, "Should not contain opening comment marker"
        assert '-->' not in result, "Should not contain closing comment marker"
        
        # Should not contain comment content
        assert 'This is a' not in result, "Should not contain comment content"
        assert 'multiline' not in result, "Should not contain comment content"
        
        # Should preserve surrounding content
        assert 'Line before comment' in result
        assert 'Line after comment' in result
    
    def test_multiple_multiline_comments(self, html_comment_processor):
        """
        Test that multiple multiline comments are all removed.
        
        Feature: template-system-extension
        Property 11: HTML Comment Multiline Handling
        """
        content = """
        <!-- First
        multiline
        comment -->
        Content between
        <!-- Second
        multiline
        comment -->
        """
        
        result = html_comment_processor.remove_comments(content)
        
        # Should not contain any comment markers
        assert result.count('<!--') == 0, "Should not contain any opening markers"
        assert result.count('-->') == 0, "Should not contain any closing markers"
        
        # Should preserve content between comments
        assert 'Content between' in result
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        num_lines=st.integers(min_value=2, max_value=10),
        content_before=st.text(min_size=1, max_size=50).filter(lambda x: '<!--' not in x and '-->' not in x),
        content_after=st.text(min_size=1, max_size=50).filter(lambda x: '<!--' not in x and '-->' not in x)
    )
    def test_property_multiline_comment_removal(
        self, html_comment_processor, num_lines, content_before, content_after
    ):
        """
        Property test: For any multiline comment with any number of lines,
        the entire comment should be removed completely.
        
        Feature: template-system-extension
        Property 11: HTML Comment Multiline Handling
        
        Validates: Requirements 16.3, 17.2
        """
        # Build multiline comment
        comment_lines = [f"Comment line {i}" for i in range(num_lines)]
        comment = "<!-- " + "\n".join(comment_lines) + " -->"
        
        # Build content with comment
        content = f"{content_before}\n{comment}\n{content_after}"
        
        # Remove comments
        result = html_comment_processor.remove_comments(content)
        
        # Should not contain comment markers
        assert '<!--' not in result, "Should not contain opening comment marker"
        assert '-->' not in result, "Should not contain closing comment marker"
        
        # Should not contain any comment line content
        for i in range(num_lines):
            assert f"Comment line {i}" not in result, \
                f"Should not contain comment line {i}"
        
        # Should preserve surrounding content
        if content_before.strip():
            assert content_before in result, "Should preserve content before comment"
        if content_after.strip():
            assert content_after in result, "Should preserve content after comment"
    
    def test_comment_with_markdown_inside(self, html_comment_processor):
        """
        Test that comments containing markdown are completely removed.
        
        Feature: template-system-extension
        Property 11: HTML Comment Multiline Handling
        """
        content = """
        # Header
        <!--
        ## This is a commented header
        - List item 1
        - List item 2
        -->
        ## Real Header
        """
        
        result = html_comment_processor.remove_comments(content)
        
        # Should not contain commented markdown
        assert 'This is a commented header' not in result
        assert 'List item 1' not in result
        
        # Should preserve real markdown
        assert '# Header' in result
        assert '## Real Header' in result
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        comment_content=st.text(min_size=10, max_size=200)
    )
    def test_property_comment_content_removal(self, html_comment_processor, comment_content):
        """
        Property test: For any comment content, after removal, the content
        should not appear in the result.
        
        Feature: template-system-extension
        Property 11: HTML Comment Multiline Handling
        
        Validates: Requirements 16.3, 17.2
        """
        # Build content with comment
        content = f"Before\n<!-- {comment_content} -->\nAfter"
        
        # Remove comments
        result = html_comment_processor.remove_comments(content)
        
        # Should not contain comment markers
        assert '<!--' not in result
        assert '-->' not in result
        
        # Should preserve surrounding content
        assert 'Before' in result
        assert 'After' in result




class TestPlaceholderSyntaxValidation:
    """
    Property 12: Placeholder Syntax Validation
    
    For any template content, all placeholders SHALL match the pattern `{{ source.field }}`
    where source is alphanumeric and field can contain dots for nested paths.
    
    Validates: Requirements 22.1, 24.3
    """
    
    @pytest.fixture
    def placeholder_processor(self):
        """Get placeholder processor instance."""
        return PlaceholderProcessor()
    
    def test_valid_placeholder_syntax_detected(self, placeholder_processor):
        """
        Test that valid placeholder syntax is correctly detected.
        
        Feature: template-system-extension
        Property 12: Placeholder Syntax Validation
        """
        valid_placeholders = [
            "{{ meta.organization.name }}",
            "{{ netbox.device.name }}",
            "{{ meta.cio.email }}",
            "{{meta.field}}",  # No spaces
            "{{  meta.field  }}",  # Extra spaces
        ]
        
        for placeholder in valid_placeholders:
            content = f"Test: {placeholder}"
            found = placeholder_processor.find_placeholders(content)
            
            assert len(found) == 1, \
                f"Should detect valid placeholder: {placeholder}"
    
    def test_invalid_placeholder_syntax_not_detected(self, placeholder_processor):
        """
        Test that invalid placeholder syntax is not detected as placeholders.
        
        Feature: template-system-extension
        Property 12: Placeholder Syntax Validation
        """
        invalid_placeholders = [
            "{ meta.field }",  # Single braces
            "{{ meta }}",  # No field
            "{{ .field }}",  # No source
            "{{ meta field }}",  # Space instead of dot
            "{{ meta-field }}",  # Hyphen instead of dot (no dot separator)
        ]
        
        for placeholder in invalid_placeholders:
            content = f"Test: {placeholder}"
            found = placeholder_processor.find_placeholders(content)
            
            assert len(found) == 0, \
                f"Should not detect invalid placeholder: {placeholder}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        source=st.text(
            alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd')),
            min_size=3,
            max_size=20
        ).filter(lambda x: x.isalnum()),
        field=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.',
            min_size=3,
            max_size=30
        ).filter(lambda x: x.replace('.', '').isalnum() and not x.startswith('.') and not x.endswith('.') and '..' not in x)
    )
    def test_property_placeholder_syntax_validation(
        self, placeholder_processor, source, field
    ):
        """
        Property test: For any valid source and field combination, the placeholder
        should be correctly detected and parsed.
        
        Feature: template-system-extension
        Property 12: Placeholder Syntax Validation
        
        Validates: Requirements 22.1, 24.3
        """
        # Build valid placeholder
        placeholder = f"{{{{ {source}.{field} }}}}"
        content = f"Test: {placeholder}"
        
        # Find placeholders
        found = placeholder_processor.find_placeholders(content)
        
        # Should find exactly one placeholder
        assert len(found) == 1, \
            f"Should find exactly one placeholder in: {placeholder}"
        
        # Verify parsed components
        assert found[0].source == source, \
            f"Source should be '{source}', found '{found[0].source}'"
        
        assert found[0].field == field, \
            f"Field should be '{field}', found '{found[0].field}'"
    
    def test_nested_field_paths_supported(self, placeholder_processor):
        """
        Test that nested field paths with dots are supported.
        
        Feature: template-system-extension
        Property 12: Placeholder Syntax Validation
        """
        nested_placeholders = [
            ("{{ meta.organization.name }}", "meta", "organization.name"),
            ("{{ netbox.device.interface.name }}", "netbox", "device.interface.name"),
            ("{{ meta.a.b.c.d }}", "meta", "a.b.c.d"),
        ]
        
        for placeholder, expected_source, expected_field in nested_placeholders:
            content = f"Test: {placeholder}"
            found = placeholder_processor.find_placeholders(content)
            
            assert len(found) == 1, \
                f"Should find placeholder: {placeholder}"
            
            assert found[0].source == expected_source, \
                f"Source should be '{expected_source}'"
            
            assert found[0].field == expected_field, \
                f"Field should be '{expected_field}'"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        num_placeholders=st.integers(min_value=1, max_value=10)
    )
    def test_property_multiple_placeholders_detection(
        self, placeholder_processor, num_placeholders
    ):
        """
        Property test: For any number of placeholders in content, all should be detected.
        
        Feature: template-system-extension
        Property 12: Placeholder Syntax Validation
        
        Validates: Requirements 22.1, 24.3
        """
        # Build content with multiple placeholders
        lines = []
        for i in range(num_placeholders):
            lines.append(f"Field{i}: {{{{ meta.field{i} }}}}")
        
        content = '\n'.join(lines)
        
        # Find placeholders
        found = placeholder_processor.find_placeholders(content)
        
        # Should find all placeholders
        assert len(found) == num_placeholders, \
            f"Should find {num_placeholders} placeholders, found {len(found)}"
        
        # Verify each placeholder
        for i, placeholder in enumerate(found):
            assert placeholder.source == 'meta', \
                f"Placeholder {i} should have source 'meta'"
            assert placeholder.field == f'field{i}', \
                f"Placeholder {i} should have field 'field{i}'"




class TestTemplateREADMEPresence:
    """
    Property 13: Template README Presence
    
    For any template type directory (bcm, isms, bsi-grundschutz), a README.md file SHALL
    be present explaining template structure, placeholder usage, and framework compliance.
    
    Validates: Requirements 4.1, 4.2, 9.1, 9.2, 14.1, 14.2
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_bcm_readme_exists_both_languages(self, template_base_path):
        """
        Test that BCM README.md exists in both German and English.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        """
        de_readme = template_base_path / "de" / "bcm" / "README.md"
        en_readme = template_base_path / "en" / "bcm" / "README.md"
        
        assert de_readme.exists(), "German BCM README.md should exist"
        assert en_readme.exists(), "English BCM README.md should exist"
        
        # Should have substantial content
        de_content = de_readme.read_text()
        en_content = en_readme.read_text()
        
        assert len(de_content) > 1000, \
            "German BCM README should have substantial content (>1000 chars)"
        assert len(en_content) > 1000, \
            "English BCM README should have substantial content (>1000 chars)"
    
    def test_isms_readme_exists_both_languages(self, template_base_path):
        """
        Test that ISMS README.md exists in both German and English.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        """
        de_readme = template_base_path / "de" / "isms" / "README.md"
        en_readme = template_base_path / "en" / "isms" / "README.md"
        
        assert de_readme.exists(), "German ISMS README.md should exist"
        assert en_readme.exists(), "English ISMS README.md should exist"
        
        # Should have substantial content
        de_content = de_readme.read_text()
        en_content = en_readme.read_text()
        
        assert len(de_content) > 1000, \
            "German ISMS README should have substantial content (>1000 chars)"
        assert len(en_content) > 1000, \
            "English ISMS README should have substantial content (>1000 chars)"
    
    def test_bsi_readme_exists_both_languages(self, template_base_path):
        """
        Test that BSI Grundschutz README.md exists in both German and English.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        """
        de_readme = template_base_path / "de" / "bsi-grundschutz" / "README.md"
        en_readme = template_base_path / "en" / "bsi-grundschutz" / "README.md"
        
        assert de_readme.exists(), "German BSI Grundschutz README.md should exist"
        assert en_readme.exists(), "English BSI Grundschutz README.md should exist"
        
        # Should have substantial content
        de_content = de_readme.read_text()
        en_content = en_readme.read_text()
        
        assert len(de_content) > 1000, \
            "German BSI Grundschutz README should have substantial content (>1000 chars)"
        assert len(en_content) > 1000, \
            "English BSI Grundschutz README should have substantial content (>1000 chars)"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz'])
    )
    def test_property_readme_presence(self, template_base_path, language, template_type):
        """
        Property test: For any template type and language, a README.md should exist.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        
        Validates: Requirements 4.1, 4.2, 9.1, 9.2, 14.1, 14.2
        """
        readme_path = template_base_path / language / template_type / "README.md"
        
        # README should exist
        assert readme_path.exists(), \
            f"README.md should exist for {language}/{template_type}"
        
        # README should be a file
        assert readme_path.is_file(), \
            f"README.md should be a file for {language}/{template_type}"
        
        # README should have content
        content = readme_path.read_text()
        assert len(content) > 0, \
            f"README.md should have content for {language}/{template_type}"
    
    def test_readme_documents_template_structure(self, template_base_path):
        """
        Test that READMEs document template structure.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        """
        for language in ['de', 'en']:
            for template_type in ['bcm', 'isms', 'bsi-grundschutz']:
                readme_path = template_base_path / language / template_type / "README.md"
                
                if not readme_path.exists():
                    continue
                
                content = readme_path.read_text()
                
                # Should mention template numbering
                has_numbering = any(num in content for num in ['0010', '0020', '0030'])
                assert has_numbering, \
                    f"README for {language}/{template_type} should document template numbering"
    
    def test_readme_documents_placeholder_usage(self, template_base_path):
        """
        Test that READMEs document placeholder usage.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        """
        for language in ['de', 'en']:
            for template_type in ['bcm', 'isms', 'bsi-grundschutz']:
                readme_path = template_base_path / language / template_type / "README.md"
                
                if not readme_path.exists():
                    continue
                
                content = readme_path.read_text()
                
                # Should mention placeholders
                has_placeholders = 'placeholder' in content.lower() or '{{' in content
                assert has_placeholders, \
                    f"README for {language}/{template_type} should document placeholder usage"
    
    def test_readme_documents_framework_compliance(self, template_base_path):
        """
        Test that READMEs document framework compliance.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        """
        framework_mappings = {
            'bcm': ['ISO 22301', 'BSI BCM'],
            'isms': ['ISO 27001', 'Annex A'],
            'bsi-grundschutz': ['BSI', '200-1', '200-2', '200-3']
        }
        
        for language in ['de', 'en']:
            for template_type, frameworks in framework_mappings.items():
                readme_path = template_base_path / language / template_type / "README.md"
                
                if not readme_path.exists():
                    continue
                
                content = readme_path.read_text()
                
                # Should mention at least one framework
                has_framework = any(framework in content for framework in frameworks)
                assert has_framework, \
                    f"README for {language}/{template_type} should document framework compliance. " \
                    f"Expected one of: {frameworks}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz'])
    )
    def test_property_bilingual_readme_consistency(self, template_base_path, template_type):
        """
        Property test: For any template type, German and English READMEs should
        have similar structure and content length.
        
        Feature: template-system-extension
        Property 13: Template README Presence
        
        Validates: Requirements 4.1, 4.2, 9.1, 9.2, 14.1, 14.2
        """
        de_readme = template_base_path / "de" / template_type / "README.md"
        en_readme = template_base_path / "en" / template_type / "README.md"
        
        # Both should exist
        assert de_readme.exists(), f"German README should exist for {template_type}"
        assert en_readme.exists(), f"English README should exist for {template_type}"
        
        # Read content
        de_content = de_readme.read_text()
        en_content = en_readme.read_text()
        
        # Both should have substantial content
        assert len(de_content) > 500, \
            f"German README for {template_type} should have substantial content"
        assert len(en_content) > 500, \
            f"English README for {template_type} should have substantial content"
        
        # Content length should be similar (within 50% variance)
        de_len = len(de_content)
        en_len = len(en_content)
        ratio = min(de_len, en_len) / max(de_len, en_len)
        
        assert ratio > 0.5, \
            f"README content length should be similar for {template_type}. " \
            f"DE: {de_len}, EN: {en_len}"


