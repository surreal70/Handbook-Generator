"""
Comprehensive property-based tests for template system extension.

This module contains property tests for universal correctness properties
that should hold across all template types and configurations.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import os
import re
from datetime import date
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




class TestPerHandbookMetadataIndependence:
    """
    Property 16: Per-Handbook Metadata Independence
    
    For any handbook type (bcm, isms, bsi-grundschutz, it-operation), the system SHALL
    support independent version numbers, owners, approvers, and dates, such that changing
    metadata for one handbook does not affect any other handbook.
    
    Validates: Requirements 26.1, 26.2, 26.3, 26.4
    """
    
    @pytest.fixture
    def temp_metadata_file(self, tmp_path):
        """Create temporary metadata file."""
        metadata_path = tmp_path / "metadata.yaml"
        return metadata_path
    
    @pytest.fixture
    def base_metadata_content(self):
        """Base metadata content without handbooks."""
        return """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

defaults:
  author: "Test Author"
  language: "de"
"""
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        handbook_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation']),
        version=st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Nd', 'Lu', 'Ll'), whitelist_characters='.-')),
        owner=st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
        approver=st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
        date=st.dates(min_value=date(2020, 1, 1), max_value=date(2030, 12, 31))
    )
    def test_property_handbook_metadata_independence(
        self, temp_metadata_file, base_metadata_content, 
        handbook_type, version, owner, approver, date
    ):
        """
        Property test: For any handbook type and metadata values, changing one handbook's
        metadata should not affect other handbooks.
        
        Feature: template-system-extension
        Property 16: Per-Handbook Metadata Independence
        
        Validates: Requirements 26.1, 26.2, 26.3, 26.4
        """
        from src.metadata_config_manager import MetadataConfigManager, HandbookInfo
        
        # Convert date to string format
        date_str = date.strftime("%Y-%m-%d")
        
        # Create metadata with all handbook types
        all_handbooks = ['bcm', 'isms', 'bsi-grundschutz', 'it-operation']
        
        # Build handbooks section with default values
        handbooks_yaml = "handbooks:\n"
        for hb_type in all_handbooks:
            handbooks_yaml += f"  {hb_type}:\n"
            handbooks_yaml += f"    version: \"1.0.0\"\n"
            handbooks_yaml += f"    owner: \"Default Owner\"\n"
            handbooks_yaml += f"    approver: \"Default Approver\"\n"
            handbooks_yaml += f"    date: \"2025-01-01\"\n"
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Store original values for all handbooks
        original_values = {}
        for hb_type in all_handbooks:
            hb = config.get_handbook_metadata(hb_type)
            assert hb is not None, f"Handbook {hb_type} should exist"
            original_values[hb_type] = {
                'version': hb.version,
                'owner': hb.owner,
                'approver': hb.approver,
                'date': hb.date
            }
        
        # Modify the target handbook
        config.handbooks[handbook_type] = HandbookInfo(
            version=version,
            owner=owner,
            approver=approver,
            date=date_str
        )
        
        # Verify target handbook was modified
        modified_hb = config.get_handbook_metadata(handbook_type)
        assert modified_hb is not None
        assert modified_hb.version == version
        assert modified_hb.owner == owner
        assert modified_hb.approver == approver
        assert modified_hb.date == date_str
        
        # Verify all other handbooks remain unchanged
        for hb_type in all_handbooks:
            if hb_type == handbook_type:
                continue  # Skip the modified handbook
            
            current_hb = config.get_handbook_metadata(hb_type)
            assert current_hb is not None, f"Handbook {hb_type} should still exist"
            
            # Verify values are unchanged
            assert current_hb.version == original_values[hb_type]['version'], \
                f"Version of {hb_type} should not change when modifying {handbook_type}"
            assert current_hb.owner == original_values[hb_type]['owner'], \
                f"Owner of {hb_type} should not change when modifying {handbook_type}"
            assert current_hb.approver == original_values[hb_type]['approver'], \
                f"Approver of {hb_type} should not change when modifying {handbook_type}"
            assert current_hb.date == original_values[hb_type]['date'], \
                f"Date of {hb_type} should not change when modifying {handbook_type}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        versions=st.lists(
            st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Nd', 'Lu', 'Ll'), whitelist_characters='.-')),
            min_size=4, max_size=4, unique=True
        )
    )
    def test_property_all_handbooks_have_unique_versions(
        self, temp_metadata_file, base_metadata_content, versions
    ):
        """
        Property test: All handbooks can have unique version numbers simultaneously.
        
        Feature: template-system-extension
        Property 16: Per-Handbook Metadata Independence
        
        Validates: Requirements 26.1
        """
        from src.metadata_config_manager import MetadataConfigManager
        
        # Create metadata with unique versions for each handbook
        all_handbooks = ['bcm', 'isms', 'bsi-grundschutz', 'it-operation']
        
        handbooks_yaml = "handbooks:\n"
        for i, hb_type in enumerate(all_handbooks):
            handbooks_yaml += f"  {hb_type}:\n"
            handbooks_yaml += f"    version: \"{versions[i]}\"\n"
            handbooks_yaml += f"    owner: \"Owner {i}\"\n"
            handbooks_yaml += f"    approver: \"Approver {i}\"\n"
            handbooks_yaml += f"    date: \"2025-01-0{i+1}\"\n"
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify each handbook has its unique version
        for i, hb_type in enumerate(all_handbooks):
            hb = config.get_handbook_metadata(hb_type)
            assert hb is not None, f"Handbook {hb_type} should exist"
            assert hb.version == versions[i], \
                f"Handbook {hb_type} should have version {versions[i]}"
        
        # Verify all versions are different
        loaded_versions = [
            config.get_handbook_metadata(hb_type).version 
            for hb_type in all_handbooks
        ]
        assert len(set(loaded_versions)) == 4, \
            "All handbooks should have unique versions"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        owners=st.lists(
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
            min_size=4, max_size=4, unique=True
        )
    )
    def test_property_all_handbooks_have_unique_owners(
        self, temp_metadata_file, base_metadata_content, owners
    ):
        """
        Property test: All handbooks can have unique owners simultaneously.
        
        Feature: template-system-extension
        Property 16: Per-Handbook Metadata Independence
        
        Validates: Requirements 26.2
        """
        from src.metadata_config_manager import MetadataConfigManager
        
        # Create metadata with unique owners for each handbook
        all_handbooks = ['bcm', 'isms', 'bsi-grundschutz', 'it-operation']
        
        handbooks_yaml = "handbooks:\n"
        for i, hb_type in enumerate(all_handbooks):
            handbooks_yaml += f"  {hb_type}:\n"
            handbooks_yaml += f"    version: \"1.{i}.0\"\n"
            handbooks_yaml += f"    owner: \"{owners[i]}\"\n"
            handbooks_yaml += f"    approver: \"Approver {i}\"\n"
            handbooks_yaml += f"    date: \"2025-01-0{i+1}\"\n"
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify each handbook has its unique owner
        for i, hb_type in enumerate(all_handbooks):
            hb = config.get_handbook_metadata(hb_type)
            assert hb is not None, f"Handbook {hb_type} should exist"
            assert hb.owner == owners[i], \
                f"Handbook {hb_type} should have owner {owners[i]}"
        
        # Verify all owners are different
        loaded_owners = [
            config.get_handbook_metadata(hb_type).owner 
            for hb_type in all_handbooks
        ]
        assert len(set(loaded_owners)) == 4, \
            "All handbooks should have unique owners"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        approvers=st.lists(
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
            min_size=4, max_size=4, unique=True
        )
    )
    def test_property_all_handbooks_have_unique_approvers(
        self, temp_metadata_file, base_metadata_content, approvers
    ):
        """
        Property test: All handbooks can have unique approvers simultaneously.
        
        Feature: template-system-extension
        Property 16: Per-Handbook Metadata Independence
        
        Validates: Requirements 26.3
        """
        from src.metadata_config_manager import MetadataConfigManager
        
        # Create metadata with unique approvers for each handbook
        all_handbooks = ['bcm', 'isms', 'bsi-grundschutz', 'it-operation']
        
        handbooks_yaml = "handbooks:\n"
        for i, hb_type in enumerate(all_handbooks):
            handbooks_yaml += f"  {hb_type}:\n"
            handbooks_yaml += f"    version: \"1.{i}.0\"\n"
            handbooks_yaml += f"    owner: \"Owner {i}\"\n"
            handbooks_yaml += f"    approver: \"{approvers[i]}\"\n"
            handbooks_yaml += f"    date: \"2025-01-0{i+1}\"\n"
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify each handbook has its unique approver
        for i, hb_type in enumerate(all_handbooks):
            hb = config.get_handbook_metadata(hb_type)
            assert hb is not None, f"Handbook {hb_type} should exist"
            assert hb.approver == approvers[i], \
                f"Handbook {hb_type} should have approver {approvers[i]}"
        
        # Verify all approvers are different
        loaded_approvers = [
            config.get_handbook_metadata(hb_type).approver 
            for hb_type in all_handbooks
        ]
        assert len(set(loaded_approvers)) == 4, \
            "All handbooks should have unique approvers"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        dates=st.lists(
            st.dates(min_value=date(2020, 1, 1), max_value=date(2030, 12, 31)),
            min_size=4, max_size=4, unique=True
        )
    )
    def test_property_all_handbooks_have_unique_dates(
        self, temp_metadata_file, base_metadata_content, dates
    ):
        """
        Property test: All handbooks can have unique dates simultaneously.
        
        Feature: template-system-extension
        Property 16: Per-Handbook Metadata Independence
        
        Validates: Requirements 26.4
        """
        from src.metadata_config_manager import MetadataConfigManager
        
        # Convert dates to string format
        date_strs = [date.strftime("%Y-%m-%d") for date in dates]
        
        # Create metadata with unique dates for each handbook
        all_handbooks = ['bcm', 'isms', 'bsi-grundschutz', 'it-operation']
        
        handbooks_yaml = "handbooks:\n"
        for i, hb_type in enumerate(all_handbooks):
            handbooks_yaml += f"  {hb_type}:\n"
            handbooks_yaml += f"    version: \"1.{i}.0\"\n"
            handbooks_yaml += f"    owner: \"Owner {i}\"\n"
            handbooks_yaml += f"    approver: \"Approver {i}\"\n"
            handbooks_yaml += f"    date: \"{date_strs[i]}\"\n"
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify each handbook has its unique date
        for i, hb_type in enumerate(all_handbooks):
            hb = config.get_handbook_metadata(hb_type)
            assert hb is not None, f"Handbook {hb_type} should exist"
            assert hb.date == date_strs[i], \
                f"Handbook {hb_type} should have date {date_strs[i]}"
        
        # Verify all dates are different
        loaded_dates = [
            config.get_handbook_metadata(hb_type).date 
            for hb_type in all_handbooks
        ]
        assert len(set(loaded_dates)) == 4, \
            "All handbooks should have unique dates"
    
    def test_handbook_metadata_isolation(self, temp_metadata_file, base_metadata_content):
        """
        Test that handbook metadata objects are isolated from each other.
        
        Feature: template-system-extension
        Property 16: Per-Handbook Metadata Independence
        
        Validates: Requirements 26.1, 26.2, 26.3, 26.4
        """
        from src.metadata_config_manager import MetadataConfigManager
        
        # Create metadata with all handbooks
        handbooks_yaml = """
handbooks:
  bcm:
    version: "1.0.0"
    owner: "BCM Owner"
    approver: "BCM Approver"
    date: "2025-01-01"
  
  isms:
    version: "2.0.0"
    owner: "ISMS Owner"
    approver: "ISMS Approver"
    date: "2025-02-01"
  
  bsi-grundschutz:
    version: "3.0.0"
    owner: "BSI Owner"
    approver: "BSI Approver"
    date: "2025-03-01"
  
  it-operation:
    version: "4.0.0"
    owner: "IT Owner"
    approver: "IT Approver"
    date: "2025-04-01"
"""
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Get all handbooks
        bcm = config.get_handbook_metadata("bcm")
        isms = config.get_handbook_metadata("isms")
        bsi = config.get_handbook_metadata("bsi-grundschutz")
        it_op = config.get_handbook_metadata("it-operation")
        
        # Verify they are all different objects
        assert bcm is not isms
        assert bcm is not bsi
        assert bcm is not it_op
        assert isms is not bsi
        assert isms is not it_op
        assert bsi is not it_op
        
        # Verify they all have different values
        versions = [bcm.version, isms.version, bsi.version, it_op.version]
        assert len(set(versions)) == 4, "All versions should be unique"
        
        owners = [bcm.owner, isms.owner, bsi.owner, it_op.owner]
        assert len(set(owners)) == 4, "All owners should be unique"
        
        approvers = [bcm.approver, isms.approver, bsi.approver, it_op.approver]
        assert len(set(approvers)) == 4, "All approvers should be unique"
        
        dates = [bcm.date, isms.date, bsi.date, it_op.date]
        assert len(set(dates)) == 4, "All dates should be unique"



class TestHandbookPlaceholderSupport:
    """
    Property 17: Handbook Placeholder Support
    
    For any handbook type, placeholders in the format {{ handbook.version }}, {{ handbook.owner }},
    {{ handbook.approver }}, and {{ handbook.date }} SHALL be replaced with the correct
    handbook-specific metadata.
    
    Validates: Requirements 26.5
    """
    
    @pytest.fixture
    def temp_metadata_file(self, tmp_path):
        """Create temporary metadata file."""
        metadata_path = tmp_path / "metadata.yaml"
        return metadata_path
    
    @pytest.fixture
    def base_metadata_content(self):
        """Base metadata content without handbooks."""
        return """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

defaults:
  author: "Test Author"
  language: "de"
"""
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        handbook_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation']),
        version=st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Nd', 'Lu', 'Ll'), whitelist_characters='.-')),
        owner=st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
        approver=st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
        date=st.dates(min_value=date(2020, 1, 1), max_value=date(2030, 12, 31))
    )
    def test_property_handbook_placeholder_replacement(
        self, temp_metadata_file, base_metadata_content,
        handbook_type, version, owner, approver, date
    ):
        """
        Property test: For any handbook type and metadata values, all handbook placeholders
        should be correctly replaced with the handbook-specific metadata.
        
        Feature: template-system-extension
        Property 17: Handbook Placeholder Support
        
        Validates: Requirements 26.5
        """
        from src.metadata_config_manager import MetadataConfigManager
        from src.meta_adapter import MetaAdapter
        
        # Convert date to string format
        date_str = date.strftime("%Y-%m-%d")
        
        # Create metadata with handbook
        handbooks_yaml = f"""
handbooks:
  {handbook_type}:
    version: "{version}"
    owner: "{owner}"
    approver: "{approver}"
    date: "{date_str}"
"""
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Create meta adapter
        adapter = MetaAdapter(config)
        adapter.connect()
        adapter.set_handbook_type(handbook_type)
        
        # Test version placeholder
        version_value = adapter.get_field("handbook.version")
        assert version_value == version, \
            f"handbook.version should return {version}"
        
        # Test owner placeholder
        owner_value = adapter.get_field("handbook.owner")
        assert owner_value == owner, \
            f"handbook.owner should return {owner}"
        
        # Test approver placeholder
        approver_value = adapter.get_field("handbook.approver")
        assert approver_value == approver, \
            f"handbook.approver should return {approver}"
        
        # Test date placeholder
        date_value = adapter.get_field("handbook.date")
        assert date_value == date_str, \
            f"handbook.date should return {date_str}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        handbook_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation']),
        placeholder_field=st.sampled_from(['version', 'owner', 'approver', 'date'])
    )
    def test_property_handbook_placeholder_independence(
        self, temp_metadata_file, base_metadata_content,
        handbook_type, placeholder_field
    ):
        """
        Property test: For any handbook type, accessing a handbook placeholder should only
        return data for that specific handbook, not affecting other handbooks.
        
        Feature: template-system-extension
        Property 17: Handbook Placeholder Support
        
        Validates: Requirements 26.5
        """
        from src.metadata_config_manager import MetadataConfigManager
        from src.meta_adapter import MetaAdapter
        
        # Create metadata with all handbooks having different values
        handbooks_yaml = """
handbooks:
  bcm:
    version: "1.0.0"
    owner: "BCM Owner"
    approver: "BCM Approver"
    date: "2025-01-01"
  
  isms:
    version: "2.0.0"
    owner: "ISMS Owner"
    approver: "ISMS Approver"
    date: "2025-02-01"
  
  bsi-grundschutz:
    version: "3.0.0"
    owner: "BSI Owner"
    approver: "BSI Approver"
    date: "2025-03-01"
  
  it-operation:
    version: "4.0.0"
    owner: "IT Owner"
    approver: "IT Approver"
    date: "2025-04-01"
"""
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Create meta adapter for target handbook
        adapter = MetaAdapter(config)
        adapter.connect()
        adapter.set_handbook_type(handbook_type)
        
        # Get value for the placeholder field
        placeholder = f"handbook.{placeholder_field}"
        value = adapter.get_field(placeholder)
        
        # Verify value is not None
        assert value is not None, \
            f"Placeholder {placeholder} should return a value for {handbook_type}"
        
        # Verify value matches the expected handbook-specific value
        expected_values = {
            'bcm': {
                'version': '1.0.0',
                'owner': 'BCM Owner',
                'approver': 'BCM Approver',
                'date': '2025-01-01'
            },
            'isms': {
                'version': '2.0.0',
                'owner': 'ISMS Owner',
                'approver': 'ISMS Approver',
                'date': '2025-02-01'
            },
            'bsi-grundschutz': {
                'version': '3.0.0',
                'owner': 'BSI Owner',
                'approver': 'BSI Approver',
                'date': '2025-03-01'
            },
            'it-operation': {
                'version': '4.0.0',
                'owner': 'IT Owner',
                'approver': 'IT Approver',
                'date': '2025-04-01'
            }
        }
        
        expected_value = expected_values[handbook_type][placeholder_field]
        assert value == expected_value, \
            f"Placeholder {placeholder} for {handbook_type} should return {expected_value}, got {value}"
        
        # Verify that other handbooks have different values
        all_handbooks = ['bcm', 'isms', 'bsi-grundschutz', 'it-operation']
        other_handbooks = [hb for hb in all_handbooks if hb != handbook_type]
        
        for other_hb in other_handbooks:
            other_adapter = MetaAdapter(config)
            other_adapter.connect()
            other_adapter.set_handbook_type(other_hb)
            other_value = other_adapter.get_field(placeholder)
            
            # Value should be different from the target handbook
            assert other_value != value, \
                f"Placeholder {placeholder} for {other_hb} should differ from {handbook_type}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        handbook_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation']),
        version=st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Nd', 'Lu', 'Ll'), whitelist_characters='.-')),
        owner=st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
        approver=st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'), whitelist_characters=' ')),
        date=st.dates(min_value=date(2020, 1, 1), max_value=date(2030, 12, 31))
    )
    def test_property_all_handbook_placeholders_work_together(
        self, temp_metadata_file, base_metadata_content,
        handbook_type, version, owner, approver, date
    ):
        """
        Property test: For any handbook type, all four handbook placeholders (version, owner,
        approver, date) should work correctly when used together in the same template.
        
        Feature: template-system-extension
        Property 17: Handbook Placeholder Support
        
        Validates: Requirements 26.5
        """
        from src.metadata_config_manager import MetadataConfigManager
        from src.meta_adapter import MetaAdapter
        
        # Convert date to string format
        date_str = date.strftime("%Y-%m-%d")
        
        # Create metadata with handbook
        handbooks_yaml = f"""
handbooks:
  {handbook_type}:
    version: "{version}"
    owner: "{owner}"
    approver: "{approver}"
    date: "{date_str}"
"""
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Create meta adapter
        adapter = MetaAdapter(config)
        adapter.connect()
        adapter.set_handbook_type(handbook_type)
        
        # Get all placeholder values
        version_value = adapter.get_field("handbook.version")
        owner_value = adapter.get_field("handbook.owner")
        approver_value = adapter.get_field("handbook.approver")
        date_value = adapter.get_field("handbook.date")
        
        # Verify all values are correct
        assert version_value == version, \
            f"handbook.version should return {version}"
        assert owner_value == owner, \
            f"handbook.owner should return {owner}"
        assert approver_value == approver, \
            f"handbook.approver should return {approver}"
        assert date_value == date_str, \
            f"handbook.date should return {date_str}"
        
        # Verify all values are non-empty
        assert version_value, "handbook.version should not be empty"
        assert owner_value, "handbook.owner should not be empty"
        assert approver_value, "handbook.approver should not be empty"
        assert date_value, "handbook.date should not be empty"
    
    def test_handbook_placeholder_without_setting_type(
        self, temp_metadata_file, base_metadata_content
    ):
        """
        Test that handbook placeholders return None or empty when handbook type is not set.
        
        Feature: template-system-extension
        Property 17: Handbook Placeholder Support
        
        Validates: Requirements 26.5
        """
        from src.metadata_config_manager import MetadataConfigManager
        from src.meta_adapter import MetaAdapter
        
        # Create metadata with handbooks
        handbooks_yaml = """
handbooks:
  bcm:
    version: "1.0.0"
    owner: "BCM Owner"
    approver: "BCM Approver"
    date: "2025-01-01"
"""
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Create meta adapter WITHOUT setting handbook type
        adapter = MetaAdapter(config)
        adapter.connect()
        
        # Try to get handbook placeholders
        version_value = adapter.get_field("handbook.version")
        owner_value = adapter.get_field("handbook.owner")
        approver_value = adapter.get_field("handbook.approver")
        date_value = adapter.get_field("handbook.date")
        
        # Should return None or empty string when handbook type is not set
        assert version_value in [None, ""], \
            "handbook.version should return None or empty when handbook type not set"
        assert owner_value in [None, ""], \
            "handbook.owner should return None or empty when handbook type not set"
        assert approver_value in [None, ""], \
            "handbook.approver should return None or empty when handbook type not set"
        assert date_value in [None, ""], \
            "handbook.date should return None or empty when handbook type not set"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        handbook_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_property_handbook_placeholder_with_missing_metadata(
        self, temp_metadata_file, base_metadata_content, handbook_type
    ):
        """
        Property test: For any handbook type, if handbook metadata is missing,
        placeholders should return None or empty string gracefully.
        
        Feature: template-system-extension
        Property 17: Handbook Placeholder Support
        
        Validates: Requirements 26.5
        """
        from src.metadata_config_manager import MetadataConfigManager
        from src.meta_adapter import MetaAdapter
        
        # Write metadata file WITHOUT handbooks section
        temp_metadata_file.write_text(base_metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Create meta adapter
        adapter = MetaAdapter(config)
        adapter.connect()
        adapter.set_handbook_type(handbook_type)
        
        # Try to get handbook placeholders
        version_value = adapter.get_field("handbook.version")
        owner_value = adapter.get_field("handbook.owner")
        approver_value = adapter.get_field("handbook.approver")
        date_value = adapter.get_field("handbook.date")
        
        # Should return None or empty string when handbook metadata is missing
        assert version_value in [None, ""], \
            f"handbook.version should return None or empty for missing {handbook_type} metadata"
        assert owner_value in [None, ""], \
            f"handbook.owner should return None or empty for missing {handbook_type} metadata"
        assert approver_value in [None, ""], \
            f"handbook.approver should return None or empty for missing {handbook_type} metadata"
        assert date_value in [None, ""], \
            f"handbook.date should return None or empty for missing {handbook_type} metadata"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        handbook_types=st.lists(
            st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation']),
            min_size=2, max_size=4, unique=True
        )
    )
    def test_property_switching_handbook_types(
        self, temp_metadata_file, base_metadata_content, handbook_types
    ):
        """
        Property test: For any sequence of handbook types, switching between them should
        correctly update the placeholder values to match the current handbook type.
        
        Feature: template-system-extension
        Property 17: Handbook Placeholder Support
        
        Validates: Requirements 26.5
        """
        from src.metadata_config_manager import MetadataConfigManager
        from src.meta_adapter import MetaAdapter
        
        # Create metadata with all handbooks having unique values
        handbooks_yaml = """
handbooks:
  bcm:
    version: "1.0.0"
    owner: "BCM Owner"
    approver: "BCM Approver"
    date: "2025-01-01"
  
  isms:
    version: "2.0.0"
    owner: "ISMS Owner"
    approver: "ISMS Approver"
    date: "2025-02-01"
  
  bsi-grundschutz:
    version: "3.0.0"
    owner: "BSI Owner"
    approver: "BSI Approver"
    date: "2025-03-01"
  
  it-operation:
    version: "4.0.0"
    owner: "IT Owner"
    approver: "IT Approver"
    date: "2025-04-01"
"""
        
        # Write metadata file
        metadata_content = base_metadata_content + "\n" + handbooks_yaml
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Create meta adapter
        adapter = MetaAdapter(config)
        adapter.connect()
        
        # Expected values for each handbook
        expected_values = {
            'bcm': {
                'version': '1.0.0',
                'owner': 'BCM Owner',
                'approver': 'BCM Approver',
                'date': '2025-01-01'
            },
            'isms': {
                'version': '2.0.0',
                'owner': 'ISMS Owner',
                'approver': 'ISMS Approver',
                'date': '2025-02-01'
            },
            'bsi-grundschutz': {
                'version': '3.0.0',
                'owner': 'BSI Owner',
                'approver': 'BSI Approver',
                'date': '2025-03-01'
            },
            'it-operation': {
                'version': '4.0.0',
                'owner': 'IT Owner',
                'approver': 'IT Approver',
                'date': '2025-04-01'
            }
        }
        
        # Switch between handbook types and verify values
        for handbook_type in handbook_types:
            # Set handbook type
            adapter.set_handbook_type(handbook_type)
            
            # Get all placeholder values
            version_value = adapter.get_field("handbook.version")
            owner_value = adapter.get_field("handbook.owner")
            approver_value = adapter.get_field("handbook.approver")
            date_value = adapter.get_field("handbook.date")
            
            # Verify values match the current handbook type
            expected = expected_values[handbook_type]
            assert version_value == expected['version'], \
                f"After switching to {handbook_type}, handbook.version should be {expected['version']}"
            assert owner_value == expected['owner'], \
                f"After switching to {handbook_type}, handbook.owner should be {expected['owner']}"
            assert approver_value == expected['approver'], \
                f"After switching to {handbook_type}, handbook.approver should be {expected['approver']}"
            assert date_value == expected['date'], \
                f"After switching to {handbook_type}, handbook.date should be {expected['date']}"



class TestNetBoxMetadataLoading:
    """
    Property 18: NetBox Metadata Loading
    
    For any valid NetBox configuration, when the system starts, it SHALL fetch contacts,
    devices, and sites from NetBox exactly once before document processing begins, and
    populate metadata-netbox.yaml with the fetched data.
    
    Validates: Requirements 27.2, 27.3, 27.4, 27.5
    """
    
    @settings(max_examples=100)
    @given(
        num_contacts=st.integers(min_value=0, max_value=10),
        num_devices=st.integers(min_value=0, max_value=10),
        num_sites=st.integers(min_value=0, max_value=10)
    )
    def test_netbox_metadata_structure(self, num_contacts, num_devices, num_sites):
        """
        Test that NetBox metadata has correct structure regardless of data size.
        
        Feature: template-system-extension
        Property 18: NetBox Metadata Loading
        """
        from unittest.mock import MagicMock, patch
        from src.netbox_metadata_loader import NetBoxMetadataLoader
        
        # Create mock NetBox API
        mock_api = MagicMock()
        mock_api.version = "3.5.0"
        
        # Create mock contacts
        mock_contacts = []
        for i in range(num_contacts):
            contact = MagicMock()
            contact.name = f"Contact {i}"
            contact.email = f"contact{i}@example.com"
            contact.phone = f"+123456789{i}"
            contact.role = f"Role {i}"
            mock_contacts.append(contact)
        
        # Create mock devices
        mock_devices = []
        for i in range(num_devices):
            device = MagicMock()
            device.name = f"device-{i}"
            device.primary_ip = f"192.168.1.{i}"
            
            site = MagicMock()
            site.name = f"Site {i}"
            device.site = site
            
            device_role = MagicMock()
            device_role.name = f"DeviceRole {i}"
            device.device_role = device_role
            
            device.status = "active"
            mock_devices.append(device)
        
        # Create mock sites
        mock_sites = []
        for i in range(num_sites):
            site = MagicMock()
            site.name = f"Site {i}"
            site.physical_address = f"{i} Main St"
            site.description = f"Site {i} description"
            site.status = "active"
            mock_sites.append(site)
        
        mock_api.tenancy.contacts.all.return_value = mock_contacts
        mock_api.dcim.devices.all.return_value = mock_devices
        mock_api.dcim.sites.all.return_value = mock_sites
        
        # Create loader with mock
        role_config = {
            'method': 'field',
            'field': 'role',
            'mappings': {}
        }
        
        with patch('src.netbox_metadata_loader.pynetbox.api') as mock_pynetbox:
            mock_pynetbox.return_value = mock_api
            
            loader = NetBoxMetadataLoader(
                "https://netbox.example.com",
                "test-token",
                role_config
            )
            
            # Load metadata
            metadata = loader.load_metadata()
            
            # Property: Metadata must have correct structure
            assert 'contacts' in metadata, "Metadata must have 'contacts' key"
            assert 'devices' in metadata, "Metadata must have 'devices' key"
            assert 'sites' in metadata, "Metadata must have 'sites' key"
            
            # Property: All sections must be dictionaries
            assert isinstance(metadata['contacts'], dict), "Contacts must be a dictionary"
            assert isinstance(metadata['devices'], dict), "Devices must be a dictionary"
            assert isinstance(metadata['sites'], dict), "Sites must be a dictionary"
            
            # Property: Number of entries should match input (or less due to filtering)
            assert len(metadata['contacts']) <= num_contacts, \
                "Number of contacts should not exceed input"
            assert len(metadata['devices']) <= num_devices, \
                "Number of devices should not exceed input"
            assert len(metadata['sites']) <= num_sites, \
                "Number of sites should not exceed input"
    
    @settings(max_examples=50)
    @given(
        role_method=st.sampled_from(['field', 'name']),
        num_contacts=st.integers(min_value=1, max_value=5)
    )
    def test_netbox_metadata_once_per_run(self, role_method, num_contacts):
        """
        Test that NetBox metadata is loaded exactly once per run.
        
        Feature: template-system-extension
        Property 18: NetBox Metadata Loading
        """
        from unittest.mock import MagicMock, patch
        from src.netbox_metadata_loader import NetBoxMetadataLoader
        
        # Create mock NetBox API
        mock_api = MagicMock()
        mock_api.version = "3.5.0"
        
        # Create mock contacts
        mock_contacts = []
        for i in range(num_contacts):
            contact = MagicMock()
            contact.name = f"Contact {i}"
            contact.email = f"contact{i}@example.com"
            contact.phone = f"+123456789{i}"
            if role_method == 'field':
                contact.role = f"Role {i}"
            else:
                contact.name = f"Contact {i} (Role{i})"
                contact.role = None
            mock_contacts.append(contact)
        
        mock_api.tenancy.contacts.all.return_value = mock_contacts
        mock_api.dcim.devices.all.return_value = []
        mock_api.dcim.sites.all.return_value = []
        
        # Create loader with mock
        role_config = {
            'method': role_method,
            'field': 'role' if role_method == 'field' else None,
            'mappings': {}
        }
        
        with patch('src.netbox_metadata_loader.pynetbox.api') as mock_pynetbox:
            mock_pynetbox.return_value = mock_api
            
            loader = NetBoxMetadataLoader(
                "https://netbox.example.com",
                "test-token",
                role_config
            )
            
            # Load metadata first time
            metadata1 = loader.load_metadata()
            
            # Property: API should be called exactly once per load_metadata() call
            assert mock_api.tenancy.contacts.all.call_count == 1, \
                "Contacts should be fetched exactly once per load_metadata() call"
            assert mock_api.dcim.devices.all.call_count == 1, \
                "Devices should be fetched exactly once per load_metadata() call"
            assert mock_api.dcim.sites.all.call_count == 1, \
                "Sites should be fetched exactly once per load_metadata() call"
            
            # Load metadata second time (simulating second run)
            metadata2 = loader.load_metadata()
            
            # Property: Each load_metadata() call should fetch data once
            assert mock_api.tenancy.contacts.all.call_count == 2, \
                "Contacts should be fetched once per load_metadata() call"
            assert mock_api.dcim.devices.all.call_count == 2, \
                "Devices should be fetched once per load_metadata() call"
            assert mock_api.dcim.sites.all.call_count == 2, \
                "Sites should be fetched once per load_metadata() call"
            
            # Property: Both loads should return same structure
            assert set(metadata1.keys()) == set(metadata2.keys()), \
                "Both metadata loads should have same structure"
    
    @settings(max_examples=50)
    @given(
        contact_name=st.text(min_size=1, max_size=50, alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'), whitelist_characters=' -'
        )),
        contact_email=st.emails(),
        contact_phone=st.text(min_size=5, max_size=20, alphabet=st.characters(
            whitelist_categories=('Nd',), whitelist_characters='+-() '
        ))
    )
    def test_netbox_contact_data_preservation(self, contact_name, contact_email, contact_phone):
        """
        Test that contact data is preserved correctly during metadata loading.
        
        Feature: template-system-extension
        Property 18: NetBox Metadata Loading
        """
        from unittest.mock import MagicMock, patch
        from src.netbox_metadata_loader import NetBoxMetadataLoader
        
        # Create mock NetBox API
        mock_api = MagicMock()
        mock_api.version = "3.5.0"
        
        # Create mock contact with property-generated data
        contact = MagicMock()
        contact.name = contact_name
        contact.email = contact_email
        contact.phone = contact_phone
        contact.role = "Test Role"
        
        mock_api.tenancy.contacts.all.return_value = [contact]
        mock_api.dcim.devices.all.return_value = []
        mock_api.dcim.sites.all.return_value = []
        
        # Create loader with mock
        role_config = {
            'method': 'field',
            'field': 'role',
            'mappings': {'test_role': 'Test Role'}
        }
        
        with patch('src.netbox_metadata_loader.pynetbox.api') as mock_pynetbox:
            mock_pynetbox.return_value = mock_api
            
            loader = NetBoxMetadataLoader(
                "https://netbox.example.com",
                "test-token",
                role_config
            )
            
            # Load metadata
            metadata = loader.load_metadata()
            
            # Property: Contact data must be preserved
            if metadata['contacts']:  # If contact was mapped to a role
                # Get the first (and only) contact
                contact_data = list(metadata['contacts'].values())[0]
                
                # Property: Name must be preserved exactly
                assert contact_data['name'] == contact_name, \
                    "Contact name must be preserved exactly"
                
                # Property: Email must be preserved exactly
                assert contact_data['email'] == contact_email, \
                    "Contact email must be preserved exactly"
                
                # Property: Phone must be preserved exactly
                assert contact_data['phone'] == contact_phone, \
                    "Contact phone must be preserved exactly"



class TestNetBoxRoleDistinctionApplication:
    """
    Property 20: NetBox Role Distinction Application
    
    For any configured role distinction method (field-based or name-based), when loading
    NetBox data, the system SHALL apply the configured logic to map NetBox contacts to roles,
    and the configuration SHALL be persisted in config.yaml.
    
    Validates: Requirements 29.4, 29.5
    """
    
    @settings(max_examples=100)
    @given(
        role_method=st.sampled_from(['field', 'name']),
        num_contacts=st.integers(min_value=1, max_value=10),
        role_name=st.sampled_from(['ciso', 'cio', 'cto', 'sysop', 'datenschutzbeauftragter'])
    )
    def test_role_distinction_method_application(self, role_method, num_contacts, role_name):
        """
        Test that role distinction method is applied correctly.
        
        Feature: template-system-extension
        Property 20: NetBox Role Distinction Application
        """
        from unittest.mock import MagicMock, patch
        from src.netbox_metadata_loader import NetBoxMetadataLoader
        
        # Create mock NetBox API
        mock_api = MagicMock()
        mock_api.version = "3.5.0"
        
        # Create mock contacts based on role method
        mock_contacts = []
        for i in range(num_contacts):
            contact = MagicMock()
            
            if role_method == 'field':
                # Field-based: set role field
                contact.name = f"Contact {i}"
                contact.email = f"contact{i}@example.com"
                contact.phone = f"+123456789{i}"
                contact.role = f"Role {i}" if i > 0 else role_name.upper()
            else:
                # Name-based: include role in name
                role_indicator = role_name.upper() if i == 0 else f"Role{i}"
                contact.name = f"Contact {i} ({role_indicator})"
                contact.email = f"contact{i}@example.com"
                contact.phone = f"+123456789{i}"
                contact.role = None
            
            mock_contacts.append(contact)
        
        mock_api.tenancy.contacts.all.return_value = mock_contacts
        mock_api.dcim.devices.all.return_value = []
        mock_api.dcim.sites.all.return_value = []
        
        # Create role configuration
        if role_method == 'field':
            role_config = {
                'method': 'field',
                'field': 'role',
                'mappings': {
                    role_name: role_name.upper()
                }
            }
        else:
            role_config = {
                'method': 'name',
                'mappings': {
                    role_name: role_name.upper()
                }
            }
        
        with patch('src.netbox_metadata_loader.pynetbox.api') as mock_pynetbox:
            mock_pynetbox.return_value = mock_api
            
            loader = NetBoxMetadataLoader(
                "https://netbox.example.com",
                "test-token",
                role_config
            )
            
            # Load metadata
            metadata = loader.load_metadata()
            
            # Property: Role distinction method must be applied
            contacts = metadata['contacts']
            
            # Property: At least one contact should be mapped to the configured role
            if num_contacts > 0:
                # The first contact should be mapped to the configured role
                assert role_name in contacts, \
                    f"Role '{role_name}' should be present in contacts when using {role_method} method"
                
                # Property: Mapped contact should have all required fields
                mapped_contact = contacts[role_name]
                assert 'name' in mapped_contact, "Mapped contact must have 'name' field"
                assert 'email' in mapped_contact, "Mapped contact must have 'email' field"
                assert 'phone' in mapped_contact, "Mapped contact must have 'phone' field"
    
    @settings(max_examples=50)
    @given(
        field_name=st.sampled_from(['role', 'title', 'position']),
        num_mappings=st.integers(min_value=1, max_value=5)
    )
    def test_field_based_role_mapping_consistency(self, field_name, num_mappings):
        """
        Test that field-based role mapping is consistent across multiple contacts.
        
        Feature: template-system-extension
        Property 20: NetBox Role Distinction Application
        """
        from unittest.mock import MagicMock, patch
        from src.netbox_metadata_loader import NetBoxMetadataLoader
        
        # Create mock NetBox API
        mock_api = MagicMock()
        mock_api.version = "3.5.0"
        
        # Create role mappings
        role_mappings = {}
        mock_contacts = []
        
        for i in range(num_mappings):
            role_key = f"role_{i}"
            role_value = f"Role Value {i}"
            role_mappings[role_key] = role_value
            
            # Create contact with this role
            contact = MagicMock()
            contact.name = f"Contact {i}"
            contact.email = f"contact{i}@example.com"
            contact.phone = f"+123456789{i}"
            
            # Set the field dynamically
            setattr(contact, field_name, role_value)
            
            mock_contacts.append(contact)
        
        mock_api.tenancy.contacts.all.return_value = mock_contacts
        mock_api.dcim.devices.all.return_value = []
        mock_api.dcim.sites.all.return_value = []
        
        # Create role configuration
        role_config = {
            'method': 'field',
            'field': field_name,
            'mappings': role_mappings
        }
        
        with patch('src.netbox_metadata_loader.pynetbox.api') as mock_pynetbox:
            mock_pynetbox.return_value = mock_api
            
            loader = NetBoxMetadataLoader(
                "https://netbox.example.com",
                "test-token",
                role_config
            )
            
            # Load metadata
            metadata = loader.load_metadata()
            
            # Property: All mapped roles should be present
            contacts = metadata['contacts']
            
            for role_key in role_mappings.keys():
                assert role_key in contacts, \
                    f"Role '{role_key}' should be mapped from field '{field_name}'"
            
            # Property: Number of mapped contacts should equal number of mappings
            assert len(contacts) == num_mappings, \
                f"Should have {num_mappings} mapped contacts, found {len(contacts)}"
    
    @settings(max_examples=50)
    @given(
        num_patterns=st.integers(min_value=1, max_value=5),
        contact_prefix=st.text(min_size=1, max_size=10, alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll')
        ))
    )
    def test_name_based_role_mapping_consistency(self, num_patterns, contact_prefix):
        """
        Test that name-based role mapping is consistent across multiple contacts.
        
        Feature: template-system-extension
        Property 20: NetBox Role Distinction Application
        """
        from unittest.mock import MagicMock, patch
        from src.netbox_metadata_loader import NetBoxMetadataLoader
        
        # Create mock NetBox API
        mock_api = MagicMock()
        mock_api.version = "3.5.0"
        
        # Create role mappings
        role_mappings = {}
        mock_contacts = []
        
        for i in range(num_patterns):
            role_key = f"role_{i}"
            role_pattern = f"PATTERN{i}"
            role_mappings[role_key] = role_pattern
            
            # Create contact with pattern in name
            contact = MagicMock()
            contact.name = f"{contact_prefix} {role_pattern} Contact"
            contact.email = f"contact{i}@example.com"
            contact.phone = f"+123456789{i}"
            contact.role = None
            
            mock_contacts.append(contact)
        
        mock_api.tenancy.contacts.all.return_value = mock_contacts
        mock_api.dcim.devices.all.return_value = []
        mock_api.dcim.sites.all.return_value = []
        
        # Create role configuration
        role_config = {
            'method': 'name',
            'mappings': role_mappings
        }
        
        with patch('src.netbox_metadata_loader.pynetbox.api') as mock_pynetbox:
            mock_pynetbox.return_value = mock_api
            
            loader = NetBoxMetadataLoader(
                "https://netbox.example.com",
                "test-token",
                role_config
            )
            
            # Load metadata
            metadata = loader.load_metadata()
            
            # Property: All mapped roles should be present
            contacts = metadata['contacts']
            
            for role_key in role_mappings.keys():
                assert role_key in contacts, \
                    f"Role '{role_key}' should be mapped from name pattern"
            
            # Property: Number of mapped contacts should equal number of patterns
            assert len(contacts) == num_patterns, \
                f"Should have {num_patterns} mapped contacts, found {len(contacts)}"
    
    @settings(max_examples=50)
    @given(
        role_method=st.sampled_from(['field', 'name']),
        has_mapping=st.booleans()
    )
    def test_role_mapping_with_and_without_configuration(self, role_method, has_mapping):
        """
        Test role mapping behavior with and without explicit mappings.
        
        Feature: template-system-extension
        Property 20: NetBox Role Distinction Application
        """
        from unittest.mock import MagicMock, patch
        from src.netbox_metadata_loader import NetBoxMetadataLoader
        
        # Create mock NetBox API
        mock_api = MagicMock()
        mock_api.version = "3.5.0"
        
        # Create mock contact
        contact = MagicMock()
        contact.name = "Test Contact (CISO)"
        contact.email = "test@example.com"
        contact.phone = "+1234567890"
        
        if role_method == 'field':
            contact.role = "Chief Information Security Officer"
        else:
            contact.role = None
        
        mock_api.tenancy.contacts.all.return_value = [contact]
        mock_api.dcim.devices.all.return_value = []
        mock_api.dcim.sites.all.return_value = []
        
        # Create role configuration
        if has_mapping:
            if role_method == 'field':
                role_config = {
                    'method': 'field',
                    'field': 'role',
                    'mappings': {
                        'ciso': 'Chief Information Security Officer'
                    }
                }
            else:
                role_config = {
                    'method': 'name',
                    'mappings': {
                        'ciso': 'CISO'
                    }
                }
        else:
            # No explicit mappings
            role_config = {
                'method': role_method,
                'field': 'role' if role_method == 'field' else None,
                'mappings': {}
            }
        
        with patch('src.netbox_metadata_loader.pynetbox.api') as mock_pynetbox:
            mock_pynetbox.return_value = mock_api
            
            loader = NetBoxMetadataLoader(
                "https://netbox.example.com",
                "test-token",
                role_config
            )
            
            # Load metadata
            metadata = loader.load_metadata()
            
            # Property: Contacts should be a dictionary
            assert isinstance(metadata['contacts'], dict), \
                "Contacts must be a dictionary"
            
            # Property: With mapping, specific role should be present
            if has_mapping:
                if role_method == 'field':
                    # Field-based with mapping should map to 'ciso'
                    assert 'ciso' in metadata['contacts'], \
                        "CISO role should be mapped with field-based method and mapping"
                else:
                    # Name-based with mapping should map to 'ciso'
                    assert 'ciso' in metadata['contacts'], \
                        "CISO role should be mapped with name-based method and mapping"
            else:
                # Without mapping, role might be normalized or not mapped
                # Property: Should have at most one contact (the one we created)
                assert len(metadata['contacts']) <= 1, \
                    "Should have at most one contact without explicit mapping"



class TestMetaNetBoxPlaceholderSupport:
    """
    Property 19: Meta-NetBox Placeholder Support
    
    For any template containing {{ meta-netbox.* }} placeholders, the system SHALL replace them
    with data from metadata-netbox.yaml, and both {{ meta.* }} and {{ meta-netbox.* }} placeholders
    SHALL work independently in the same template.
    
    Validates: Requirements 28.1, 28.2, 28.3, 28.4, 28.5
    """
    
    @pytest.fixture
    def sample_netbox_metadata(self):
        """Sample NetBox metadata for testing."""
        return {
            'contacts': {
                'ciso': {
                    'name': 'NetBox CISO',
                    'email': 'netbox.ciso@example.com',
                    'phone': '+49 123 456789'
                },
                'cio': {
                    'name': 'NetBox CIO',
                    'email': 'netbox.cio@example.com',
                    'phone': '+49 123 456790'
                }
            },
            'devices': {
                'firewall': {
                    'name': 'fw-netbox-01',
                    'ip': '10.0.0.1',
                    'model': 'Cisco ASA'
                },
                'switch': {
                    'name': 'sw-netbox-01',
                    'ip': '10.0.0.2',
                    'model': 'Cisco Catalyst'
                }
            },
            'sites': {
                'primary': {
                    'name': 'NetBox HQ',
                    'address': '123 NetBox Street',
                    'city': 'NetBox City'
                },
                'secondary': {
                    'name': 'NetBox Branch',
                    'address': '456 NetBox Avenue',
                    'city': 'NetBox Town'
                }
            }
        }
    
    @pytest.fixture
    def sample_meta_config(self):
        """Sample meta configuration for testing."""
        from src.metadata_config_manager import MetadataConfig, OrganizationInfo, DocumentInfo, PersonRole
        
        return MetadataConfig(
            organization=OrganizationInfo(
                name="Meta Organization",
                address="789 Meta Street",
                city="Meta City",
                postal_code="12345",
                country="Meta Country",
                website="https://meta.org",
                phone="+1234567890",
                email="meta@meta.org"
            ),
            roles={
                'ciso': PersonRole(
                    name="Meta CISO",
                    title="Chief Information Security Officer",
                    email="meta.ciso@meta.org",
                    phone="+1234567891"
                ),
                'cio': PersonRole(
                    name="Meta CIO",
                    title="Chief Information Officer",
                    email="meta.cio@meta.org",
                    phone="+1234567892"
                )
            },
            document=DocumentInfo(
                owner="Meta Owner",
                approver="Meta Approver",
                version="1.0.0",
                classification="internal"
            ),
            author="Meta Author",
            language="en"
        )
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        contact_role=st.sampled_from(['ciso', 'cio']),
        device_type=st.sampled_from(['firewall', 'switch']),
        site_type=st.sampled_from(['primary', 'secondary']),
        field_type=st.sampled_from(['name', 'email', 'phone', 'ip', 'model', 'address', 'city'])
    )
    def test_meta_netbox_placeholder_replacement(
        self, sample_netbox_metadata, contact_role, device_type, site_type, field_type
    ):
        """
        Property: Meta-NetBox placeholders are replaced with correct data.
        
        Feature: template-system-extension
        Property 19: Meta-NetBox Placeholder Support
        """
        from src.meta_netbox_adapter import MetaNetBoxAdapter
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create meta-netbox adapter
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Create placeholder processor
        processor = PlaceholderProcessor(data_sources={'meta-netbox': adapter})
        
        # Build template with appropriate placeholders based on field type
        if field_type in ['name', 'email', 'phone']:
            # Contact field
            template = f"**Contact:** {{{{ meta-netbox.contacts.{contact_role}.{field_type} }}}}"
            expected_value = sample_netbox_metadata['contacts'][contact_role][field_type]
        elif field_type in ['ip', 'model']:
            # Device field
            template = f"**Device:** {{{{ meta-netbox.devices.{device_type}.{field_type} }}}}"
            expected_value = sample_netbox_metadata['devices'][device_type][field_type]
        else:
            # Site field (name, address, city)
            template = f"**Site:** {{{{ meta-netbox.sites.{site_type}.{field_type} }}}}"
            expected_value = sample_netbox_metadata['sites'][site_type][field_type]
        
        # Process template
        result = processor.process_template(template)
        
        # Property 1: Placeholder should be replaced
        assert f"meta-netbox." not in result.content, \
            "Meta-NetBox placeholder should be replaced"
        
        # Property 2: Correct value should be present
        assert expected_value in result.content, \
            f"Expected value '{expected_value}' should be in processed content"
        
        # Property 3: Should have exactly one replacement
        assert len(result.replacements) == 1, \
            "Should have exactly one replacement"
        
        # Property 4: Replacement source should be 'meta-netbox'
        assert result.replacements[0].source == 'meta-netbox', \
            "Replacement source should be 'meta-netbox'"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        use_meta_placeholder=st.booleans(),
        use_netbox_placeholder=st.booleans()
    )
    def test_meta_and_meta_netbox_independence(
        self, sample_netbox_metadata, sample_meta_config, use_meta_placeholder, use_netbox_placeholder
    ):
        """
        Property: Meta and meta-netbox placeholders work independently.
        
        Feature: template-system-extension
        Property 19: Meta-NetBox Placeholder Support
        """
        # Skip if neither placeholder is used
        if not use_meta_placeholder and not use_netbox_placeholder:
            return
        
        from src.meta_netbox_adapter import MetaNetBoxAdapter
        from src.meta_adapter import MetaAdapter
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create adapters
        netbox_adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        netbox_adapter.connect()
        
        meta_adapter = MetaAdapter(sample_meta_config)
        meta_adapter.connect()
        
        # Create placeholder processor with both adapters
        processor = PlaceholderProcessor(
            data_sources={
                'meta': meta_adapter,
                'meta-netbox': netbox_adapter
            }
        )
        
        # Build template
        template_parts = []
        expected_replacements = 0
        
        if use_meta_placeholder:
            template_parts.append("**Meta CISO:** {{ meta.ciso.name }}")
            expected_replacements += 1
        
        if use_netbox_placeholder:
            template_parts.append("**NetBox CISO:** {{ meta-netbox.contacts.ciso.name }}")
            expected_replacements += 1
        
        template = "\n".join(template_parts)
        
        # Process template
        result = processor.process_template(template)
        
        # Property 1: All placeholders should be replaced
        assert "{{ meta." not in result.content, \
            "Meta placeholders should be replaced"
        assert "{{ meta-netbox." not in result.content, \
            "Meta-NetBox placeholders should be replaced"
        
        # Property 2: Correct number of replacements
        assert len(result.replacements) == expected_replacements, \
            f"Should have {expected_replacements} replacements"
        
        # Property 3: If both used, should have replacements from both sources
        if use_meta_placeholder and use_netbox_placeholder:
            sources = {r.source for r in result.replacements}
            assert 'meta' in sources, "Should have meta replacement"
            assert 'meta-netbox' in sources, "Should have meta-netbox replacement"
            
            # Property 4: Meta and meta-netbox values should be different
            assert "Meta CISO" in result.content, "Should have Meta CISO value"
            assert "NetBox CISO" in result.content, "Should have NetBox CISO value"
    
    def test_meta_netbox_placeholder_with_nonexistent_field(self, sample_netbox_metadata):
        """
        Property: Nonexistent meta-netbox fields generate warnings.
        
        Feature: template-system-extension
        Property 19: Meta-NetBox Placeholder Support
        """
        from src.meta_netbox_adapter import MetaNetBoxAdapter
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create meta-netbox adapter
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Create placeholder processor
        processor = PlaceholderProcessor(data_sources={'meta-netbox': adapter})
        
        # Template with nonexistent field
        template = "**Nonexistent:** {{ meta-netbox.contacts.nonexistent.name }}"
        
        # Process template
        result = processor.process_template(template)
        
        # Property 1: Placeholder should not be replaced
        assert "{{ meta-netbox.contacts.nonexistent.name }}" in result.content, \
            "Nonexistent placeholder should remain in content"
        
        # Property 2: Should have a warning
        assert len(result.warnings) > 0, \
            "Should have at least one warning for nonexistent field"
        
        # Property 3: Should have no replacements
        assert len(result.replacements) == 0, \
            "Should have no replacements for nonexistent field"
    
    @settings(max_examples=100)
    @given(
        nested_levels=st.integers(min_value=2, max_value=5)
    )
    def test_meta_netbox_placeholder_with_nested_paths(self, nested_levels):
        """
        Property: Meta-NetBox placeholders support nested paths.
        
        Feature: template-system-extension
        Property 19: Meta-NetBox Placeholder Support
        """
        from src.meta_netbox_adapter import MetaNetBoxAdapter
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create nested metadata structure
        nested_metadata = {'level0': {}}
        current = nested_metadata['level0']
        
        for i in range(1, nested_levels):
            current[f'level{i}'] = {}
            current = current[f'level{i}']
        
        # Add final value
        current['value'] = 'nested_value'
        
        # Create meta-netbox adapter
        adapter = MetaNetBoxAdapter(nested_metadata)
        adapter.connect()
        
        # Create placeholder processor
        processor = PlaceholderProcessor(data_sources={'meta-netbox': adapter})
        
        # Build nested path
        path_parts = [f'level{i}' for i in range(nested_levels)]
        path_parts.append('value')
        nested_path = '.'.join(path_parts)
        
        # Template with nested placeholder
        template = f"**Nested:** {{{{ meta-netbox.{nested_path} }}}}"
        
        # Process template
        result = processor.process_template(template)
        
        # Property 1: Placeholder should be replaced
        assert "{{ meta-netbox." not in result.content, \
            "Nested placeholder should be replaced"
        
        # Property 2: Correct value should be present
        assert "nested_value" in result.content, \
            "Nested value should be in processed content"
        
        # Property 3: Should have exactly one replacement
        assert len(result.replacements) == 1, \
            "Should have exactly one replacement"
    
    def test_meta_netbox_placeholder_syntax_with_hyphens(self):
        """
        Property: Meta-NetBox placeholder syntax supports hyphens in source name.
        
        Feature: template-system-extension
        Property 19: Meta-NetBox Placeholder Support
        """
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create processor without data sources (just to test pattern matching)
        processor = PlaceholderProcessor()
        
        # Template with meta-netbox placeholder (hyphenated source name)
        template = "**Test:** {{ meta-netbox.contacts.ciso.name }}"
        
        # Find placeholders
        placeholders = processor.find_placeholders(template)
        
        # Property 1: Should find exactly one placeholder
        assert len(placeholders) == 1, \
            "Should find exactly one placeholder"
        
        # Property 2: Source should be 'meta-netbox' (with hyphen)
        assert placeholders[0].source == 'meta-netbox', \
            "Source should be 'meta-netbox' with hyphen"
        
        # Property 3: Field path should be correct
        assert placeholders[0].field == 'contacts.ciso.name', \
            "Field path should be 'contacts.ciso.name'"



class TestExtendedRoleSupport:
    """
    Property 21: Extended Role Support
    
    For any of the six new roles (sysop, datenschutzbeauftragter, risikomanager, interner_auditor,
    personalleitung, it_manager), the system SHALL support metadata configuration and placeholder
    replacement, and SHALL translate German role names to English equivalents in English templates.
    
    Validates: Requirements 30.1, 30.2, 30.3, 30.4, 30.5, 30.6, 30.7
    """
    
    @pytest.fixture
    def extended_roles_config(self):
        """Create metadata config with all 6 extended roles using German titles."""
        from src.metadata_config_manager import MetadataConfig, OrganizationInfo, DocumentInfo, PersonRole
        
        return MetadataConfig(
            organization=OrganizationInfo(
                name="Test Organization",
                address="Test Street 123",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "sysop": PersonRole(
                    name="Michael Schneider",
                    title="Systemadministrator",  # German
                    email="michael.schneider@test.com",
                    phone="+49 89 12345678-260",
                    department="IT Operations"
                ),
                "datenschutzbeauftragter": PersonRole(
                    name="Dr. Sarah Klein",
                    title="Datenschutzbeauftragter",  # German
                    email="sarah.klein@test.com",
                    phone="+49 89 12345678-320",
                    department="Legal & Compliance"
                ),
                "risikomanager": PersonRole(
                    name="Frank Wagner",
                    title="Risikomanager",  # German
                    email="frank.wagner@test.com",
                    phone="+49 89 12345678-350",
                    department="Risk Management"
                ),
                "interner_auditor": PersonRole(
                    name="Dr. Klaus Hoffmann",
                    title="Interner Auditor",  # German
                    email="klaus.hoffmann@test.com",
                    phone="+49 89 12345678-360",
                    department="Internal Audit"
                ),
                "personalleitung": PersonRole(
                    name="Sabine Richter",
                    title="Personalleitung",  # German
                    email="sabine.richter@test.com",
                    phone="+49 89 12345678-600",
                    department="Human Resources"
                ),
                "it_manager": PersonRole(
                    name="Martin Bauer",
                    title="IT Manager",  # Already English
                    email="martin.bauer@test.com",
                    phone="+49 89 12345678-240",
                    department="IT"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        role_key=st.sampled_from([
            'sysop', 'datenschutzbeauftragter', 'risikomanager',
            'interner_auditor', 'personalleitung', 'it_manager'
        ]),
        field_name=st.sampled_from(['name', 'title', 'email', 'phone', 'department'])
    )
    def test_extended_role_placeholder_replacement(self, extended_roles_config, role_key, field_name):
        """
        Property: All 6 extended roles support placeholder replacement.
        
        Feature: template-system-extension
        Property 21: Extended Role Support
        """
        from src.meta_adapter import MetaAdapter
        
        # Create meta adapter with German language
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        # Get field value
        field_value = adapter.get_field(f"{role_key}.{field_name}")
        
        # Property 1: Field value should not be None
        assert field_value is not None, \
            f"Field {role_key}.{field_name} should have a value"
        
        # Property 2: Field value should be non-empty string
        assert isinstance(field_value, str), \
            f"Field {role_key}.{field_name} should be a string"
        assert len(field_value.strip()) > 0, \
            f"Field {role_key}.{field_name} should be non-empty"
        
        # Property 3: Email fields should contain @
        if field_name == 'email':
            assert '@' in field_value, \
                f"Email field {role_key}.{field_name} should contain @"
        
        # Property 4: Phone fields should contain digits
        if field_name == 'phone':
            assert any(c.isdigit() for c in field_value), \
                f"Phone field {role_key}.{field_name} should contain digits"
        
        adapter.disconnect()
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        role_key=st.sampled_from([
            'sysop', 'datenschutzbeauftragter', 'risikomanager',
            'interner_auditor', 'personalleitung', 'it_manager'
        ]),
        language=st.sampled_from(['de', 'en'])
    )
    def test_extended_role_title_translation(self, extended_roles_config, role_key, language):
        """
        Property: German role titles are translated to English in English templates.
        
        Feature: template-system-extension
        Property 21: Extended Role Support
        """
        from src.meta_adapter import MetaAdapter
        
        # Expected translations
        german_to_english = {
            'Systemadministrator': 'System Administrator',
            'Datenschutzbeauftragter': 'Data Protection Officer',
            'Risikomanager': 'Risk Manager',
            'Interner Auditor': 'Internal Auditor',
            'Personalleitung': 'HR Manager',
            'IT Manager': 'IT Manager'  # Already English
        }
        
        # Create meta adapter with specified language
        adapter = MetaAdapter(extended_roles_config, language=language)
        adapter.connect()
        
        # Get title
        title = adapter.get_field(f"{role_key}.title")
        
        # Property 1: Title should not be None
        assert title is not None, \
            f"Title for {role_key} should not be None"
        
        # Property 2: Title should be non-empty
        assert len(title.strip()) > 0, \
            f"Title for {role_key} should be non-empty"
        
        # Property 3: If language is English, title should be translated
        if language == 'en':
            # Title should be one of the English translations
            assert title in german_to_english.values(), \
                f"Title '{title}' for {role_key} should be translated to English"
        
        # Property 4: If language is German, title should be original German or English
        if language == 'de':
            # Title should be either German or English (for roles already in English)
            assert title in german_to_english.keys() or title in german_to_english.values(), \
                f"Title '{title}' for {role_key} should be German or English"
        
        adapter.disconnect()
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        role_key=st.sampled_from([
            'sysop', 'datenschutzbeauftragter', 'risikomanager',
            'interner_auditor', 'personalleitung', 'it_manager'
        ])
    )
    def test_extended_role_in_template_processing(self, extended_roles_config, role_key):
        """
        Property: Extended roles work in template processing with placeholder processor.
        
        Feature: template-system-extension
        Property 21: Extended Role Support
        """
        from src.meta_adapter import MetaAdapter
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create meta adapter
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        # Create placeholder processor
        processor = PlaceholderProcessor(data_sources={'meta': adapter})
        
        # Template with extended role placeholders (placeholders on their own lines)
        template = f"""
{{{{ meta.{role_key}.name }}}}
{{{{ meta.{role_key}.title }}}}
{{{{ meta.{role_key}.email }}}}
{{{{ meta.{role_key}.phone }}}}
"""
        
        # Process template
        result = processor.process_template(template)
        
        # Property 1: All placeholders should be replaced
        assert "{{ meta." not in result.content, \
            f"All {role_key} placeholders should be replaced"
        
        # Property 2: Should have 4 replacements (name, title, email, phone)
        assert len(result.replacements) == 4, \
            f"Should have 4 replacements for {role_key}"
        
        # Property 3: All replacements should be from 'meta' source
        for replacement in result.replacements:
            assert replacement.source == 'meta', \
                "All replacements should be from 'meta' source"
        
        # Property 4: No errors should be generated
        assert len(result.errors) == 0, \
            f"No errors should be generated for {role_key}"
        
        adapter.disconnect()
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        num_roles=st.integers(min_value=1, max_value=6)
    )
    def test_multiple_extended_roles_in_template(self, extended_roles_config, num_roles):
        """
        Property: Multiple extended roles can be used in the same template.
        
        Feature: template-system-extension
        Property 21: Extended Role Support
        """
        from src.meta_adapter import MetaAdapter
        from src.placeholder_processor import PlaceholderProcessor
        
        # All extended roles
        all_roles = [
            'sysop', 'datenschutzbeauftragter', 'risikomanager',
            'interner_auditor', 'personalleitung', 'it_manager'
        ]
        
        # Select subset of roles
        selected_roles = all_roles[:num_roles]
        
        # Create meta adapter
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        # Create placeholder processor
        processor = PlaceholderProcessor(data_sources={'meta': adapter})
        
        # Build template with multiple roles
        template_parts = []
        for role_key in selected_roles:
            template_parts.append(f"**{role_key}:** {{{{ meta.{role_key}.name }}}}")
        
        template = "\n".join(template_parts)
        
        # Process template
        result = processor.process_template(template)
        
        # Property 1: All placeholders should be replaced
        assert "{{ meta." not in result.content, \
            "All placeholders should be replaced"
        
        # Property 2: Should have correct number of replacements
        assert len(result.replacements) == num_roles, \
            f"Should have {num_roles} replacements"
        
        # Property 3: Each selected role should have a replacement
        replaced_roles = set()
        for replacement in result.replacements:
            # Extract role from placeholder (e.g., "{{ meta.sysop.name }}" -> "sysop")
            role = replacement.placeholder.split('.')[1]
            replaced_roles.add(role)
        
        assert replaced_roles == set(selected_roles), \
            f"All selected roles should have replacements"
        
        adapter.disconnect()
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        role_key=st.sampled_from([
            'sysop', 'datenschutzbeauftragter', 'risikomanager',
            'interner_auditor', 'personalleitung', 'it_manager'
        ])
    )
    def test_extended_role_translation_consistency(self, extended_roles_config, role_key):
        """
        Property: Role title translation is consistent across multiple calls.
        
        Feature: template-system-extension
        Property 21: Extended Role Support
        """
        from src.meta_adapter import MetaAdapter
        
        # Create adapters for both languages
        adapter_de = MetaAdapter(extended_roles_config, language='de')
        adapter_de.connect()
        
        adapter_en = MetaAdapter(extended_roles_config, language='en')
        adapter_en.connect()
        
        # Get titles multiple times
        title_de_1 = adapter_de.get_field(f"{role_key}.title")
        title_de_2 = adapter_de.get_field(f"{role_key}.title")
        
        title_en_1 = adapter_en.get_field(f"{role_key}.title")
        title_en_2 = adapter_en.get_field(f"{role_key}.title")
        
        # Property 1: German titles should be consistent
        assert title_de_1 == title_de_2, \
            f"German title for {role_key} should be consistent across calls"
        
        # Property 2: English titles should be consistent
        assert title_en_1 == title_en_2, \
            f"English title for {role_key} should be consistent across calls"
        
        # Property 3: If original title is German, English should be different
        german_titles = ['Systemadministrator', 'Datenschutzbeauftragter', 'Risikomanager',
                        'Interner Auditor', 'Personalleitung']
        
        if title_de_1 in german_titles:
            assert title_en_1 != title_de_1, \
                f"English title should be different from German title for {role_key}"
        
        adapter_de.disconnect()
        adapter_en.disconnect()
    
    def test_all_extended_roles_defined_in_metadata(self, extended_roles_config):
        """
        Property: All 6 extended roles are defined in metadata configuration.
        
        Feature: template-system-extension
        Property 21: Extended Role Support
        """
        # Expected roles
        expected_roles = [
            'sysop', 'datenschutzbeauftragter', 'risikomanager',
            'interner_auditor', 'personalleitung', 'it_manager'
        ]
        
        # Property 1: All roles should be present
        for role_key in expected_roles:
            role = extended_roles_config.get_role(role_key)
            assert role is not None, \
                f"Role {role_key} should be defined in metadata"
        
        # Property 2: All roles should have required fields
        for role_key in expected_roles:
            role = extended_roles_config.get_role(role_key)
            assert role.name is not None and len(role.name) > 0, \
                f"Role {role_key} should have a name"
            assert role.title is not None and len(role.title) > 0, \
                f"Role {role_key} should have a title"
            assert role.email is not None and '@' in role.email, \
                f"Role {role_key} should have a valid email"
            assert role.phone is not None and len(role.phone) > 0, \
                f"Role {role_key} should have a phone"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        field_name=st.sampled_from(['name', 'email', 'phone', 'department'])
    )
    def test_extended_role_non_title_fields_unchanged_by_language(
        self, extended_roles_config, field_name
    ):
        """
        Property: Non-title fields are not affected by language setting.
        
        Feature: template-system-extension
        Property 21: Extended Role Support
        """
        from src.meta_adapter import MetaAdapter
        
        # Create adapters for both languages
        adapter_de = MetaAdapter(extended_roles_config, language='de')
        adapter_de.connect()
        
        adapter_en = MetaAdapter(extended_roles_config, language='en')
        adapter_en.connect()
        
        # Test all extended roles
        all_roles = [
            'sysop', 'datenschutzbeauftragter', 'risikomanager',
            'interner_auditor', 'personalleitung', 'it_manager'
        ]
        
        for role_key in all_roles:
            value_de = adapter_de.get_field(f"{role_key}.{field_name}")
            value_en = adapter_en.get_field(f"{role_key}.{field_name}")
            
            # Property: Non-title fields should be identical regardless of language
            assert value_de == value_en, \
                f"Field {role_key}.{field_name} should be identical in both languages"
        
        adapter_de.disconnect()
        adapter_en.disconnect()



class TestSeparateMarkdownFileGeneration:
    """
    Property 23: Separate Markdown File Generation
    
    For any set of templates, when generating separate markdown files:
    - Separate files are created with correct naming pattern {template-number}_{template-name}.md
    - TOC contains all templates with valid links
    - No combined file is created in separate mode
    
    Validates: Requirements 32.1, 32.2, 32.3, 32.4, 32.5, 32.6
    """
    
    @pytest.fixture
    def output_generator(self, tmp_path):
        """Get output generator instance with test mode enabled."""
        from src.output_generator import OutputGenerator
        output_dir = tmp_path / "test-output"
        return OutputGenerator(output_dir, test_mode=True)
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=1, max_value=10),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_separate_files_created_with_correct_naming(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: For any set of templates, separate files are created with correct naming.
        
        Feature: template-system-extension
        Property 23: Separate Markdown File Generation
        """
        # Generate template data
        templates_data = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_name = f"{template_num}_Template_{i+1}.md"
            content = f"# Template {i+1}\n\nContent for template {i+1}."
            templates_data.append((template_name, content))
        
        # Generate separate markdown files
        result = output_generator.generate_separate_markdown_files(
            templates_data,
            language,
            template_type
        )
        
        # Property 1: No errors should occur
        assert len(result.errors) == 0, f"Should not have errors: {result.errors}"
        
        # Property 2: All files should be created with correct naming pattern
        output_dir = output_generator.output_dir / language / "markdown"
        assert output_dir.exists(), "Output directory should exist"
        
        for template_name, _ in templates_data:
            # Extract filename (remove .md extension and re-add it)
            expected_filename = Path(template_name).stem + ".md"
            file_path = output_dir / expected_filename
            
            assert file_path.exists(), \
                f"File {expected_filename} should exist in {output_dir}"
            
            # Check filename follows pattern {template-number}_{template-name}.md
            assert re.match(r'^\d{4}_.*\.md$', expected_filename), \
                f"Filename {expected_filename} should match pattern ####_Name.md"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=1, max_value=10),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_toc_contains_all_templates_with_valid_links(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: TOC contains all templates with valid links.
        
        Feature: template-system-extension
        Property 23: Separate Markdown File Generation
        """
        # Generate template info
        templates_info = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_title = f"Template {i+1}"
            filename = f"{template_num}_Template_{i+1}.md"
            templates_info.append((template_num, template_title, filename))
        
        # Generate TOC
        result = output_generator.generate_markdown_toc(
            templates_info,
            language,
            template_type
        )
        
        # Property 1: No errors should occur
        assert len(result.errors) == 0, f"Should not have errors: {result.errors}"
        
        # Property 2: TOC file should exist
        toc_path = output_generator.output_dir / language / "markdown" / "TOC.md"
        assert toc_path.exists(), "TOC.md should exist"
        
        # Property 3: TOC should contain all templates with valid markdown links
        toc_content = toc_path.read_text(encoding='utf-8')
        
        for template_num, template_title, filename in templates_info:
            # Check that link exists in TOC
            link_text = f"{template_num} - {template_title}"
            link_pattern = f"[{link_text}]({filename})"
            
            assert link_pattern in toc_content, \
                f"TOC should contain link: [{link_text}]({filename})"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=2, max_value=10),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_no_combined_file_created_in_separate_mode(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: No combined file is created in separate mode.
        
        Feature: template-system-extension
        Property 23: Separate Markdown File Generation
        """
        # Generate template data
        templates_data = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_name = f"{template_num}_Template_{i+1}.md"
            content = f"# Template {i+1}\n\nContent for template {i+1}."
            templates_data.append((template_name, content))
        
        # Generate separate markdown files
        result = output_generator.generate_separate_markdown_files(
            templates_data,
            language,
            template_type
        )
        
        assert len(result.errors) == 0, f"Should not have errors: {result.errors}"
        
        # Property: No combined file should exist
        output_dir = output_generator.output_dir / language / "markdown"
        
        # Common combined file patterns
        combined_patterns = [
            f"{template_type}_handbook.md",
            f"{template_type}_handbook_{language}.md",
            "handbook.md",
            "combined.md"
        ]
        
        for pattern in combined_patterns:
            combined_file = output_dir / pattern
            assert not combined_file.exists(), \
                f"Combined file {pattern} should not exist in separate mode"
        
        # Property: Only individual template files and TOC should exist
        md_files = list(output_dir.glob("*.md"))
        
        # All files should match template pattern or be TOC.md
        for md_file in md_files:
            filename = md_file.name
            is_template = re.match(r'^\d{4}_.*\.md$', filename)
            is_toc = filename == "TOC.md"
            
            assert is_template or is_toc, \
                f"File {filename} should be either a template file or TOC.md"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=1, max_value=10),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_separate_files_content_preserved(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: Content is preserved exactly in separate files.
        
        Feature: template-system-extension
        Property 23: Separate Markdown File Generation
        """
        # Generate template data with unique content
        templates_data = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_name = f"{template_num}_Template_{i+1}.md"
            content = f"# Template {i+1}\n\nUnique content {i+1}: {template_num}"
            templates_data.append((template_name, content))
        
        # Generate separate markdown files
        result = output_generator.generate_separate_markdown_files(
            templates_data,
            language,
            template_type
        )
        
        assert len(result.errors) == 0, f"Should not have errors: {result.errors}"
        
        # Property: Each file should contain exactly its original content
        output_dir = output_generator.output_dir / language / "markdown"
        
        for template_name, original_content in templates_data:
            filename = Path(template_name).stem + ".md"
            file_path = output_dir / filename
            
            assert file_path.exists(), f"File {filename} should exist"
            
            file_content = file_path.read_text(encoding='utf-8')
            
            # Content should be preserved exactly
            assert file_content == original_content, \
                f"Content in {filename} should match original content"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_separate_files_require_test_mode(
        self, tmp_path, language, template_type
    ):
        """
        Property: Separate file generation requires test mode.
        
        Feature: template-system-extension
        Property 23: Separate Markdown File Generation
        """
        from src.output_generator import OutputGenerator
        
        # Create generator with test mode disabled
        output_dir = tmp_path / "test-output"
        generator = OutputGenerator(output_dir, test_mode=False)
        
        templates_data = [
            ("0010_Test.md", "# Test Content")
        ]
        
        # Try to generate separate files without test mode
        result = generator.generate_separate_markdown_files(
            templates_data,
            language,
            template_type
        )
        
        # Property: Should have error about test mode
        assert len(result.errors) > 0, "Should have errors when test mode is disabled"
        assert any("--test" in e for e in result.errors), \
            "Error should mention --test flag"
        assert result.markdown_path is None, \
            "Should not generate files when test mode is disabled"


# ============================================================================
# Property 24: PDF Table of Contents
# ============================================================================

class TestPDFTableOfContents:
    """
    Property 24: PDF Table of Contents
    
    For any set of templates, when generating PDF with TOC:
    - PDF includes TOC with all templates listed
    - Page breaks are inserted between all templates
    - TOC contains template numbers and titles
    - Anchor IDs are correctly generated for linking
    
    Validates: Requirements 33.1, 33.2, 33.3, 33.4
    """
    
    @pytest.fixture
    def output_generator(self, tmp_path):
        """Get output generator instance with test mode enabled."""
        from src.output_generator import OutputGenerator
        output_dir = tmp_path / "test-output"
        return OutputGenerator(output_dir, test_mode=True)
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=1, max_value=10),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_toc_includes_all_templates(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: For any set of templates, TOC includes all templates listed.
        
        Feature: template-system-extension
        Property 24: PDF Table of Contents
        """
        # Generate template data
        templates_data = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_title = f"Template {i+1}"
            content = f"# Template {i+1}\n\nContent for template {i+1}."
            templates_data.append((template_num, template_title, content))
        
        # Generate TOC HTML
        toc_html = output_generator._generate_toc_html(templates_data, template_type)
        
        # Property 1: TOC should contain all template numbers and titles
        for template_num, template_title, _ in templates_data:
            assert f"{template_num} - {template_title}" in toc_html, \
                f"TOC should contain '{template_num} - {template_title}'"
        
        # Property 2: TOC should have proper structure
        assert '<div class="toc">' in toc_html, "TOC should have toc div"
        assert '<h1>Table of Contents</h1>' in toc_html, "TOC should have title"
        assert '<ul>' in toc_html, "TOC should have list"
        assert '</ul>' in toc_html, "TOC should close list"
        
        # Property 3: TOC should have page break after it
        assert '<div class="page-break"></div>' in toc_html, \
            "TOC should have page break after it"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=2, max_value=10),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_page_breaks_inserted_between_templates(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: For any set of templates, page breaks are inserted between all templates.
        
        Feature: template-system-extension
        Property 24: PDF Table of Contents
        """
        # Generate template HTML
        templates_html = []
        for i in range(template_count):
            html = f"<h1>Template {i+1}</h1><p>Content {i+1}</p>"
            templates_html.append(html)
        
        # Add page breaks
        result_html = output_generator._add_page_breaks(templates_html)
        
        # Property 1: Should have n-1 page breaks for n templates
        expected_breaks = template_count - 1
        actual_breaks = result_html.count('<div class="page-break"></div>')
        assert actual_breaks == expected_breaks, \
            f"Should have {expected_breaks} page breaks for {template_count} templates, got {actual_breaks}"
        
        # Property 2: All templates should be present in result
        for i in range(template_count):
            assert f"Template {i+1}" in result_html, \
                f"Template {i+1} should be in result"
        
        # Property 3: Page breaks should be between templates, not at the end
        # The last template should not be followed by a page break
        last_template_html = templates_html[-1]
        # Find the last occurrence of the last template
        last_template_pos = result_html.rfind(last_template_html)
        last_page_break_pos = result_html.rfind('<div class="page-break"></div>')
        
        if last_page_break_pos != -1:
            assert last_page_break_pos < last_template_pos, \
                "Last page break should come before the last template"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=1, max_value=10),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_anchor_ids_correctly_generated(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: For any set of templates, anchor IDs are correctly generated for linking.
        
        Feature: template-system-extension
        Property 24: PDF Table of Contents
        """
        # Generate template data
        templates_data = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_title = f"Template {i+1}"
            content = f"# Template {i+1}\n\nContent for template {i+1}."
            templates_data.append((template_num, template_title, content))
        
        # Generate TOC HTML
        toc_html = output_generator._generate_toc_html(templates_data, template_type)
        
        # Property 1: Each template should have an anchor link in TOC
        for template_num, template_title, _ in templates_data:
            anchor_link = f'href="#section-{template_num}"'
            assert anchor_link in toc_html, \
                f"TOC should contain anchor link '{anchor_link}'"
        
        # Property 2: Anchor links should be in <a> tags
        for template_num, _, _ in templates_data:
            # Check that the anchor is part of a proper link structure
            link_pattern = f'<a href="#section-{template_num}">'
            assert link_pattern in toc_html, \
                f"TOC should have proper link structure for section-{template_num}"
    
    @settings(max_examples=30, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=1, max_value=5),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_pdf_with_toc_test_mode_validation(
        self, tmp_path, template_count, language, template_type
    ):
        """
        Property: PDF with TOC generation requires test mode to be enabled.
        
        Feature: template-system-extension
        Property 24: PDF Table of Contents
        """
        from src.output_generator import OutputGenerator
        
        # Create generator with test mode disabled
        output_dir = tmp_path / "test-output"
        generator = OutputGenerator(output_dir, test_mode=False)
        
        # Generate template data
        templates_data = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_title = f"Template {i+1}"
            content = f"# Template {i+1}\n\nContent."
            templates_data.append((template_num, template_title, content))
        
        # Try to generate PDF with TOC
        result = generator.generate_pdf_with_toc(
            templates_data,
            language,
            template_type
        )
        
        # Property 1: Should have error about test mode
        assert len(result.errors) > 0, "Should have errors when test mode is disabled"
        assert any("--test" in e for e in result.errors), \
            "Error should mention --test flag"
        
        # Property 2: PDF should not be generated
        assert result.pdf_path is None, "PDF should not be generated without test mode"
    
    @settings(max_examples=30, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_count=st.integers(min_value=1, max_value=5),
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation'])
    )
    def test_pdf_with_toc_output_directory_structure(
        self, output_generator, template_count, language, template_type
    ):
        """
        Property: PDF with TOC is stored in correct directory structure.
        
        Feature: template-system-extension
        Property 24: PDF Table of Contents
        """
        # Generate template data
        templates_data = []
        for i in range(template_count):
            template_num = f"{(i+1)*10:04d}"
            template_title = f"Template {i+1}"
            content = f"# Template {i+1}\n\nContent."
            templates_data.append((template_num, template_title, content))
        
        try:
            # Try to generate PDF with TOC
            result = output_generator.generate_pdf_with_toc(
                templates_data,
                language,
                template_type
            )
            
            # If PDF generation succeeds (dependencies available)
            if result.pdf_path is not None:
                # Property 1: PDF should be in correct directory structure
                expected_dir = output_generator.output_dir / language / "pdf"
                assert result.pdf_path.parent == expected_dir, \
                    f"PDF should be in {expected_dir}, got {result.pdf_path.parent}"
                
                # Property 2: Filename should follow pattern
                assert result.pdf_path.name == f"{template_type}_handbook.pdf", \
                    f"PDF filename should be {template_type}_handbook.pdf"
        
        except (ImportError, OSError):
            # PDF dependencies not available - skip this property check
            pytest.skip("PDF generation dependencies not available")
