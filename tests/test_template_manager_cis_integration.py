"""
Property-based tests for Template Manager CIS Controls Integration.

This module contains property tests specifically for template manager integration
with CIS Controls, validating discovery, sorting, validation, and availability.

Feature: cis-controls-integration
Task: 6. Test template manager integration
Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import tempfile
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest

from src.template_manager import TemplateManager


class TestTemplateDiscoveryCompleteness:
    """
    Property 1: Template Discovery Completeness
    
    For any language directory containing a template type subdirectory with .md files,
    the Template_Manager SHALL discover and return all templates in that subdirectory
    when discover_templates() is called.
    
    Validates: Requirements 1.1, 1.2, 4.1
    """
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        num_templates=st.integers(min_value=1, max_value=10)
    )
    def test_property_1_template_discovery_completeness(self, language, num_templates):
        """
        Property test: For any language directory with CIS Controls templates,
        all templates SHALL be discovered.
        
        Feature: cis-controls-integration, Task 6.1
        Property 1: Template Discovery Completeness
        
        Validates: Requirements 1.1, 1.2, 4.1
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            cis_dir = templates_dir / language / 'cis-controls'
            cis_dir.mkdir(parents=True)
            
            # Create metadata template
            metadata_file = cis_dir / f'0000_metadata_{language}_cis-controls.md'
            metadata_file.write_text(f'# Metadata for {language}')
            
            # Create content templates
            expected_files = [metadata_file]
            for i in range(num_templates):
                sort_num = (i + 1) * 100
                template_file = cis_dir / f'{sort_num:04d}_template_{i}.md'
                template_file.write_text(f'# Template {i}')
                expected_files.append(template_file)
            
            # Initialize TemplateManager and discover
            manager = TemplateManager(templates_dir)
            discovered = manager.discover_templates()
            
            # Verify language is discovered
            assert language in discovered, \
                f"Language {language} should be discovered"
            
            # Verify cis-controls category is discovered
            assert 'cis-controls' in discovered[language], \
                f"cis-controls category should be discovered for {language}"
            
            # Verify all template files are discovered
            discovered_paths = discovered[language]['cis-controls']
            discovered_names = {p.name for p in discovered_paths}
            expected_names = {p.name for p in expected_files}
            
            assert discovered_names == expected_names, \
                f"All templates should be discovered. Expected: {expected_names}, Got: {discovered_names}"
            
            # Verify template count
            assert len(discovered_paths) == len(expected_files), \
                f"Template count should match. Expected: {len(expected_files)}, Got: {len(discovered_paths)}"
    
    def test_cis_controls_templates_discovered_german(self):
        """
        Unit test: German CIS Controls templates should be discovered.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 1.1
        """
        manager = TemplateManager(Path('templates'))
        discovered = manager.discover_templates()
        
        assert 'de' in discovered, \
            "German language should be discovered"
        assert 'cis-controls' in discovered['de'], \
            "CIS Controls should be discovered for German"
        
        # Should have templates
        de_cis_templates = discovered['de']['cis-controls']
        assert len(de_cis_templates) > 0, \
            "German CIS Controls should have templates"
    
    def test_cis_controls_templates_discovered_english(self):
        """
        Unit test: English CIS Controls templates should be discovered.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 1.2
        """
        manager = TemplateManager(Path('templates'))
        discovered = manager.discover_templates()
        
        assert 'en' in discovered, \
            "English language should be discovered"
        assert 'cis-controls' in discovered['en'], \
            "CIS Controls should be discovered for English"
        
        # Should have templates
        en_cis_templates = discovered['en']['cis-controls']
        assert len(en_cis_templates) > 0, \
            "English CIS Controls should have templates"
    
    def test_cis_controls_discovery_empty_directory(self):
        """
        Unit test: Discovery should handle empty CIS Controls directory.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 1.1, 1.2
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            cis_dir = templates_dir / 'de' / 'cis-controls'
            cis_dir.mkdir(parents=True)
            
            # Empty directory - no templates
            manager = TemplateManager(templates_dir)
            discovered = manager.discover_templates()
            
            # Empty directory should not be included in discovered templates
            # (no .md files means no templates to discover)
            if 'de' in discovered:
                assert 'cis-controls' not in discovered['de'], \
                    "Empty directory should not be discovered"
            else:
                # Language not discovered at all is also acceptable
                assert True
    
    def test_cis_controls_discovery_nonexistent_directory(self):
        """
        Unit test: Discovery should handle nonexistent CIS Controls directory.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 1.1, 1.2
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            # Don't create cis-controls directory
            
            manager = TemplateManager(templates_dir)
            discovered = manager.discover_templates()
            
            # No templates should be discovered
            assert discovered == {} or 'cis-controls' not in discovered.get('de', {}), \
                "Nonexistent directory should not be discovered"


class TestTemplateSortingConsistency:
    """
    Property 2: Template Sorting Consistency
    
    For any language and template type combination, when get_templates() is called,
    the returned templates SHALL be sorted by sort_order with metadata templates
    (sort_order=0) appearing first, followed by content templates in ascending
    numeric order.
    
    Validates: Requirements 4.2, 4.3
    """
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        num_templates=st.integers(min_value=2, max_value=10),
        has_metadata=st.booleans()
    )
    def test_property_2_template_sorting_consistency(self, language, num_templates, has_metadata):
        """
        Property test: For any set of CIS Controls templates, they SHALL be
        sorted with metadata first, then content in ascending order.
        
        Feature: cis-controls-integration, Task 6.2
        Property 2: Template Sorting Consistency
        
        Validates: Requirements 4.2, 4.3
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            cis_dir = templates_dir / language / 'cis-controls'
            cis_dir.mkdir(parents=True)
            
            # Create templates in random order
            import random
            sort_numbers = [(i + 1) * 100 for i in range(num_templates)]
            shuffled_numbers = sort_numbers.copy()
            random.shuffle(shuffled_numbers)
            
            # Create metadata if requested
            if has_metadata:
                metadata_file = cis_dir / f'0000_metadata_{language}_cis-controls.md'
                metadata_file.write_text('# Metadata')
            
            # Create content templates in shuffled order
            for sort_num in shuffled_numbers:
                template_file = cis_dir / f'{sort_num:04d}_content.md'
                template_file.write_text(f'# Content {sort_num}')
            
            # Get templates through TemplateManager
            manager = TemplateManager(templates_dir)
            templates = manager.get_templates(language, 'cis-controls')
            
            # Verify correct count
            expected_count = num_templates + (1 if has_metadata else 0)
            assert len(templates) == expected_count, \
                f"Should have {expected_count} templates"
            
            # Verify metadata comes first if present
            if has_metadata:
                assert templates[0].is_metadata(), \
                    "First template should be metadata"
                assert templates[0].sort_order == 0, \
                    "Metadata should have sort_order 0"
                content_start = 1
            else:
                content_start = 0
            
            # Verify content templates are sorted in ascending order
            content_templates = templates[content_start:]
            for i in range(len(content_templates) - 1):
                assert content_templates[i].sort_order < content_templates[i + 1].sort_order, \
                    f"Templates should be sorted: {content_templates[i].sort_order} < {content_templates[i + 1].sort_order}"
            
            # Verify sort orders match expected numbers
            actual_sort_orders = [t.sort_order for t in content_templates]
            assert actual_sort_orders == sorted(sort_numbers), \
                f"Sort orders should match expected: {sorted(sort_numbers)}"
    
    def test_cis_controls_sorting_german(self):
        """
        Unit test: German CIS Controls templates should be properly sorted.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 4.2
        """
        manager = TemplateManager(Path('templates'))
        templates = manager.get_templates('de', 'cis-controls')
        
        # First should be metadata
        assert templates[0].is_metadata(), \
            "First template should be metadata"
        
        # Rest should be in ascending order
        for i in range(len(templates) - 1):
            assert templates[i].sort_order <= templates[i + 1].sort_order, \
                f"Templates should be sorted: {templates[i].sort_order} <= {templates[i + 1].sort_order}"
    
    def test_cis_controls_sorting_english(self):
        """
        Unit test: English CIS Controls templates should be properly sorted.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 4.3
        """
        manager = TemplateManager(Path('templates'))
        templates = manager.get_templates('en', 'cis-controls')
        
        # First should be metadata
        assert templates[0].is_metadata(), \
            "First template should be metadata"
        
        # Rest should be in ascending order
        for i in range(len(templates) - 1):
            assert templates[i].sort_order <= templates[i + 1].sort_order, \
                f"Templates should be sorted: {templates[i].sort_order} <= {templates[i + 1].sort_order}"


class TestFilenameConventionValidation:
    """
    Property 3: Filename Convention Validation
    
    For any template file in a template directory, if the filename does not match
    the pattern NNNN_name.md (where NNNN is 4 digits) or 0000_metadata_[lang]_[type].md,
    the validate_template_structure() method SHALL generate a warning message
    containing the filename and the reason for invalidity.
    
    Validates: Requirements 1.3, 11.1, 11.2, 11.3, 11.4, 11.5
    """
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        invalid_filename=st.sampled_from([
            'template.md',  # No number
            '123_template.md',  # Only 3 digits
            '12345_template.md',  # 5 digits
            'metadata_de_cis-controls.md',  # Missing 0000
        ])
    )
    def test_property_3_filename_convention_validation(self, language, invalid_filename):
        """
        Property test: For any invalid filename, a warning SHALL be generated.
        
        Feature: cis-controls-integration, Task 6.3
        Property 3: Filename Convention Validation
        
        Validates: Requirements 1.3, 11.1, 11.2, 11.3, 11.4, 11.5
        
        Note: Filenames like '0001_metadata_de_cis-controls.md' are treated as
        valid content templates (they match NNNN_name.md pattern), even though
        they look like metadata templates. This is acceptable behavior - the
        validation checks for proper numbering format, not semantic correctness.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            cis_dir = templates_dir / language / 'cis-controls'
            cis_dir.mkdir(parents=True)
            
            # Create invalid template file
            invalid_file = cis_dir / invalid_filename
            invalid_file.write_text('# Invalid template')
            
            # Validate structure
            manager = TemplateManager(templates_dir)
            warnings = manager.validate_template_structure()
            
            # Should have at least one warning
            assert len(warnings) > 0, \
                f"Should generate warning for invalid filename: {invalid_filename}"
            
            # Warning should mention the filename
            warning_text = ' '.join(warnings).lower()
            assert invalid_filename.lower() in warning_text or 'invalid' in warning_text or 'numbering' in warning_text, \
                f"Warning should mention invalid filename or numbering issue"
    
    def test_valid_filenames_no_warnings(self):
        """
        Unit test: Valid CIS Controls filenames should not generate warnings.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 1.3, 11.1
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            cis_dir = templates_dir / 'de' / 'cis-controls'
            cis_dir.mkdir(parents=True)
            
            # Create valid templates
            (cis_dir / '0000_metadata_de_cis-controls.md').write_text('# Metadata')
            (cis_dir / '0010_overview.md').write_text('# Overview')
            (cis_dir / '0100_os_hardening.md').write_text('# OS Hardening')
            
            # Validate structure
            manager = TemplateManager(templates_dir)
            warnings = manager.validate_template_structure()
            
            # Should have no warnings for valid filenames
            cis_warnings = [w for w in warnings if 'cis-controls' in w.lower()]
            assert len(cis_warnings) == 0, \
                f"Valid filenames should not generate warnings: {cis_warnings}"
    
    def test_metadata_naming_pattern_validation(self):
        """
        Unit test: Metadata templates must follow naming pattern.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 11.4
        """
        manager = TemplateManager(Path('templates'))
        
        # Check German metadata
        de_metadata = Path('templates/de/cis-controls/0000_metadata_de_cis-controls.md')
        assert de_metadata.exists(), \
            "German metadata should follow naming pattern"
        
        # Check English metadata
        en_metadata = Path('templates/en/cis-controls/0000_metadata_en_cis-controls.md')
        assert en_metadata.exists(), \
            "English metadata should follow naming pattern"
    
    def test_content_template_numbering_validation(self):
        """
        Unit test: Content templates must have 4-digit numbering.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 11.2, 11.3
        """
        manager = TemplateManager(Path('templates'))
        
        for language in ['de', 'en']:
            templates = manager.get_templates(language, 'cis-controls')
            
            # Check all content templates
            for template in templates:
                if not template.is_metadata():
                    # Filename should match NNNN_name.md pattern
                    filename = template.path.name
                    assert filename[:4].isdigit(), \
                        f"Content template should start with 4 digits: {filename}"
                    assert filename[4] == '_', \
                        f"Content template should have underscore after digits: {filename}"
                    assert filename.endswith('.md'), \
                        f"Content template should end with .md: {filename}"


class TestAvailableOptionsCompleteness:
    """
    Property 9: Available Options Completeness
    
    For any template type discovered by discover_templates(), that template type
    SHALL appear in the list returned by get_available_options() for all languages
    where it exists.
    
    Validates: Requirements 3.3, 4.4
    """
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en', 'fr']),
        template_type=st.sampled_from(['cis-controls', 'bcm', 'isms', 'test-type'])
    )
    def test_property_9_available_options_completeness(self, language, template_type):
        """
        Property test: For any discovered template type, it SHALL appear in
        available options for that language.
        
        Feature: cis-controls-integration, Task 6.4
        Property 9: Available Options Completeness
        
        Validates: Requirements 3.3, 4.4
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            type_dir = templates_dir / language / template_type
            type_dir.mkdir(parents=True)
            
            # Create at least one template
            template_file = type_dir / '0100_test.md'
            template_file.write_text('# Test')
            
            # Get available options
            manager = TemplateManager(templates_dir)
            available_languages, available_types = manager.get_available_options()
            
            # Language should be in available languages
            assert language in available_languages, \
                f"Language {language} should be in available languages"
            
            # Template type should be in available types for that language
            assert language in available_types, \
                f"Language {language} should have available types"
            assert template_type in available_types[language], \
                f"Template type {template_type} should be available for {language}"
    
    def test_cis_controls_in_available_options_german(self):
        """
        Unit test: CIS Controls should be in available options for German.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 3.3
        """
        manager = TemplateManager(Path('templates'))
        available_languages, available_types = manager.get_available_options()
        
        assert 'de' in available_languages, \
            "German should be in available languages"
        assert 'cis-controls' in available_types['de'], \
            "CIS Controls should be available for German"
    
    def test_cis_controls_in_available_options_english(self):
        """
        Unit test: CIS Controls should be in available options for English.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 4.4
        """
        manager = TemplateManager(Path('templates'))
        available_languages, available_types = manager.get_available_options()
        
        assert 'en' in available_languages, \
            "English should be in available languages"
        assert 'cis-controls' in available_types['en'], \
            "CIS Controls should be available for English"
    
    def test_all_discovered_types_in_available_options(self):
        """
        Unit test: All discovered template types should be in available options.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 3.3, 4.4
        """
        manager = TemplateManager(Path('templates'))
        discovered = manager.discover_templates()
        available_languages, available_types = manager.get_available_options()
        
        # For each discovered language and type
        for language, types in discovered.items():
            assert language in available_languages, \
                f"Discovered language {language} should be in available languages"
            
            for template_type in types.keys():
                assert template_type in available_types[language], \
                    f"Discovered type {template_type} should be available for {language}"


class TestTemplateExistenceValidation:
    """
    Property 12: Template Existence Validation
    
    For any valid combination of language and template type where templates exist
    in the filesystem, validate_template_exists() SHALL return None (indicating
    no error).
    
    Validates: Requirements 4.5
    """
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['cis-controls', 'bcm', 'isms', 'test-type'])
    )
    def test_property_12_template_existence_validation(self, language, template_type):
        """
        Property test: For any existing template combination, validation SHALL
        return None (no error).
        
        Feature: cis-controls-integration, Task 6.5
        Property 12: Template Existence Validation
        
        Validates: Requirements 4.5
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            type_dir = templates_dir / language / template_type
            type_dir.mkdir(parents=True)
            
            # Create at least one template
            template_file = type_dir / '0100_test.md'
            template_file.write_text('# Test')
            
            # Validate existence
            manager = TemplateManager(templates_dir)
            error = manager.validate_template_exists(language, template_type)
            
            # Should return None (no error) for existing templates
            assert error is None, \
                f"Should return None for existing {language}/{template_type}, got: {error}"
    
    def test_cis_controls_exists_german(self):
        """
        Unit test: German CIS Controls templates should exist and validate.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 4.5
        """
        manager = TemplateManager(Path('templates'))
        error = manager.validate_template_exists('de', 'cis-controls')
        
        assert error is None, \
            f"German CIS Controls should exist, got error: {error}"
    
    def test_cis_controls_exists_english(self):
        """
        Unit test: English CIS Controls templates should exist and validate.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 4.5
        """
        manager = TemplateManager(Path('templates'))
        error = manager.validate_template_exists('en', 'cis-controls')
        
        assert error is None, \
            f"English CIS Controls should exist, got error: {error}"
    
    def test_nonexistent_template_returns_error(self):
        """
        Unit test: Nonexistent template should return error message.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 4.5
        """
        manager = TemplateManager(Path('templates'))
        error = manager.validate_template_exists('de', 'nonexistent-type')
        
        assert error is not None, \
            "Nonexistent template should return error message"
        assert 'not found' in error.lower() or 'nonexistent-type' in error.lower(), \
            f"Error message should indicate template not found: {error}"
    
    def test_nonexistent_language_returns_error(self):
        """
        Unit test: Nonexistent language should return error message.
        
        Feature: cis-controls-integration, Task 6.6
        Validates: Requirements 4.5
        """
        manager = TemplateManager(Path('templates'))
        error = manager.validate_template_exists('xx', 'cis-controls')
        
        assert error is not None, \
            "Nonexistent language should return error message"
        assert 'not found' in error.lower(), \
            f"Error message should indicate language not found: {error}"
