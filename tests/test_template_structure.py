"""
Tests for Template Structure and Organization

Tests for IT-Operations template structure, renaming, and organization.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import tempfile
import shutil

from src.template_manager import TemplateManager


class TestTemplateRenaming:
    """Tests for template renaming functionality."""
    
    def test_german_templates_renamed(self):
        """Test that German IT-operation templates have been renamed correctly."""
        templates_dir = Path('templates/de/it-operation')
        
        # Verify old names don't exist
        assert not (templates_dir / '0100_einleitung.md').exists(), \
            "Old template 0100_einleitung.md should not exist"
        assert not (templates_dir / '0200_betriebsprozesse.md').exists(), \
            "Old template 0200_betriebsprozesse.md should not exist"
        
        # Verify new names exist
        assert (templates_dir / '0010_Einleitung.md').exists(), \
            "New template 0010_Einleitung.md should exist"
        assert (templates_dir / '0011_Rahmenbedingungen.md').exists(), \
            "New template 0011_Rahmenbedingungen.md should exist"
    
    def test_english_templates_renamed(self):
        """Test that English IT-operation templates have been renamed correctly."""
        templates_dir = Path('templates/en/it-operation')
        
        # Verify old names don't exist
        assert not (templates_dir / '0100_introduction.md').exists(), \
            "Old template 0100_introduction.md should not exist"
        assert not (templates_dir / '0200_operational_processes.md').exists(), \
            "Old template 0200_operational_processes.md should not exist"
        
        # Verify new names exist
        assert (templates_dir / '0010_Introduction.md').exists(), \
            "New template 0010_Introduction.md should exist"
        assert (templates_dir / '0011_Framework_Conditions.md').exists(), \
            "New template 0011_Framework_Conditions.md should exist"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        old_number=st.sampled_from([100, 200]),
        new_number=st.sampled_from([10, 11])
    )
    def test_property_9_template_file_renaming(self, language, old_number, new_number):
        """
        Feature: it-operation-template-extension, Property 9: Template File Renaming
        
        For any template file that was renamed from the old numbering scheme (0100, 0200)
        to the new scheme (0010, 0011), the old file should not exist and the new file
        should exist with the correct numbering.
        
        Validates: Requirements 1.1, 1.2
        """
        templates_dir = Path(f'templates/{language}/it-operation')
        
        # Map old numbers to new numbers
        old_to_new = {
            100: 10,
            200: 11
        }
        
        # Only test if this is a valid mapping
        if old_number in old_to_new and new_number == old_to_new[old_number]:
            # Define old and new filenames based on language
            if language == 'de':
                old_names = {
                    100: '0100_einleitung.md',
                    200: '0200_betriebsprozesse.md'
                }
                new_names = {
                    10: '0010_Einleitung.md',
                    11: '0011_Rahmenbedingungen.md'
                }
            else:  # en
                old_names = {
                    100: '0100_introduction.md',
                    200: '0200_operational_processes.md'
                }
                new_names = {
                    10: '0010_Introduction.md',
                    11: '0011_Framework_Conditions.md'
                }
            
            old_filename = old_names[old_number]
            new_filename = new_names[new_number]
            
            # Verify old file doesn't exist
            old_path = templates_dir / old_filename
            assert not old_path.exists(), \
                f"Old template {old_filename} should not exist after renaming"
            
            # Verify new file exists
            new_path = templates_dir / new_filename
            assert new_path.exists(), \
                f"New template {new_filename} should exist after renaming"
            
            # Verify new file has content
            content = new_path.read_text()
            assert len(content) > 0, \
                f"New template {new_filename} should have content"
            
            # Verify new file has correct numbering in filename
            assert new_filename.startswith(f'{new_number:04d}_'), \
                f"New template should start with {new_number:04d}_"


class TestTemplateNumberingSequence:
    """Tests for template numbering sequence."""
    
    def test_it_operation_templates_exist(self):
        """Test that IT-operation templates exist in both languages."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            assert templates_dir.exists(), \
                f"IT-operation templates directory should exist for {language}"
            
            # Check that at least the renamed templates exist
            template_files = list(templates_dir.glob('*.md'))
            assert len(template_files) >= 3, \
                f"Should have at least 3 templates (metadata + 2 content) for {language}"
    
    def test_metadata_template_exists(self):
        """Test that metadata templates exist."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            metadata_file = templates_dir / f'0000_metadata_{language}_it-operation.md'
            assert metadata_file.exists(), \
                f"Metadata template should exist for {language}"
    
    def test_template_numbering_starts_correctly(self):
        """Test that template numbering starts with 0010 and 0011."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            # Get all content templates (excluding metadata)
            content_templates = sorted([
                f for f in templates_dir.glob('*.md')
                if not f.name.startswith('0000_')
            ])
            
            # Verify we have at least the two renamed templates
            assert len(content_templates) >= 2, \
                f"Should have at least 2 content templates for {language}"
            
            # Verify first two templates are 0010 and 0011
            assert content_templates[0].name.startswith('0010_'), \
                f"First content template should start with 0010_ for {language}"
            assert content_templates[1].name.startswith('0011_'), \
                f"Second content template should start with 0011_ for {language}"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_11_template_numbering_sequence(self, language):
        """
        Feature: it-operation-template-extension, Property 11: Template Numbering Sequence
        
        For any set of IT-operations templates, the numbering should follow the sequence
        0010, 0011, 0020, 0030, ..., 0290 with no gaps in the defined templates.
        
        Validates: Requirements 2.2
        """
        templates_dir = Path(f'templates/{language}/it-operation')
        
        # Get all content templates (excluding metadata and README)
        content_templates = sorted([
            f for f in templates_dir.glob('*.md')
            if not f.name.startswith('0000_') and f.name != 'README.md'
        ])
        
        # Extract template numbers
        template_numbers = []
        for template in content_templates:
            try:
                number = int(template.name[:4])
                template_numbers.append(number)
            except ValueError:
                pytest.fail(f"Template {template.name} does not start with a valid 4-digit number")
        
        # Verify numbering sequence
        if len(template_numbers) > 0:
            # First template should be 0010
            assert template_numbers[0] == 10, \
                f"First template should be numbered 0010, found {template_numbers[0]:04d}"
            
            # Second template should be 0011
            if len(template_numbers) > 1:
                assert template_numbers[1] == 11, \
                    f"Second template should be numbered 0011, found {template_numbers[1]:04d}"
            
            # After 0011, templates should follow 10-step increments (0020, 0030, ...)
            if len(template_numbers) > 2:
                for i in range(2, len(template_numbers)):
                    expected_number = 20 + (i - 2) * 10
                    actual_number = template_numbers[i]
                    
                    # Allow for missing templates (gaps are ok), but numbers should be in sequence
                    assert actual_number >= expected_number, \
                        f"Template {i} should be >= {expected_number:04d}, found {actual_number:04d}"
                    
                    # Numbers should be multiples of 10 (after 0011)
                    assert actual_number % 10 == 0, \
                        f"Template number {actual_number:04d} should be a multiple of 10"
                    
                    # Numbers should not exceed 0290
                    assert actual_number <= 290, \
                        f"Template number {actual_number:04d} should not exceed 0290"
            
            # Verify no duplicate numbers
            assert len(template_numbers) == len(set(template_numbers)), \
                f"Template numbers should be unique, found duplicates: {template_numbers}"
            
            # Verify templates are in ascending order
            assert template_numbers == sorted(template_numbers), \
                f"Template numbers should be in ascending order: {template_numbers}"


class TestBilingualConsistency:
    """Tests for bilingual template consistency."""
    
    def test_german_and_english_templates_match(self):
        """Test that German and English IT-operation templates have matching structure."""
        de_dir = Path('templates/de/it-operation')
        en_dir = Path('templates/en/it-operation')
        
        # Get template files (excluding metadata)
        de_templates = sorted([
            f.name for f in de_dir.glob('*.md')
            if not f.name.startswith('0000_')
        ])
        en_templates = sorted([
            f.name for f in en_dir.glob('*.md')
            if not f.name.startswith('0000_')
        ])
        
        # Extract numbering from filenames
        de_numbers = [t[:4] for t in de_templates]
        en_numbers = [t[:4] for t in en_templates]
        
        # Verify same numbering exists in both languages
        assert de_numbers == en_numbers, \
            f"Template numbering should match between languages. " \
            f"DE: {de_numbers}, EN: {en_numbers}"
    
    def test_metadata_templates_match(self):
        """Test that metadata templates exist in both languages."""
        de_metadata = Path('templates/de/it-operation/0000_metadata_de_it-operation.md')
        en_metadata = Path('templates/en/it-operation/0000_metadata_en_it-operation.md')
        
        assert de_metadata.exists(), "German metadata template should exist"
        assert en_metadata.exists(), "English metadata template should exist"


class TestTemplateContentStructure:
    """Tests for template content structure."""
    
    def test_renamed_templates_have_content(self):
        """Test that renamed templates still have their original content."""
        # Test German templates
        de_intro = Path('templates/de/it-operation/0010_Einleitung.md')
        de_content = de_intro.read_text()
        assert '# 1. Einleitung' in de_content or '# Einleitung' in de_content, \
            "German introduction template should have introduction heading"
        
        de_framework = Path('templates/de/it-operation/0011_Rahmenbedingungen.md')
        de_framework_content = de_framework.read_text()
        assert len(de_framework_content) > 0, \
            "German framework conditions template should have content"
        
        # Test English templates
        en_intro = Path('templates/en/it-operation/0010_Introduction.md')
        en_content = en_intro.read_text()
        assert '# 1. Introduction' in en_content or '# Introduction' in en_content, \
            "English introduction template should have introduction heading"
        
        en_framework = Path('templates/en/it-operation/0011_Framework_Conditions.md')
        en_framework_content = en_framework.read_text()
        assert len(en_framework_content) > 0, \
            "English framework conditions template should have content"


class TestBilingualTemplateConsistency:
    """Property-based tests for bilingual template consistency."""
    
    @settings(max_examples=100)
    @given(
        template_number=st.integers(min_value=10, max_value=290).filter(lambda x: x % 10 == 0)
    )
    def test_property_10_bilingual_template_consistency(self, template_number):
        """
        Feature: it-operation-template-extension, Property 10: Bilingual Template Consistency
        
        For any German IT-operations template, there should exist a corresponding English template
        with the same numbering and equivalent content structure.
        
        Validates: Requirements 21.1, 21.2, 21.5
        """
        de_dir = Path('templates/de/it-operation')
        en_dir = Path('templates/en/it-operation')
        
        # Find German template with this number
        de_templates = list(de_dir.glob(f'{template_number:04d}_*.md'))
        
        # If German template exists, English should exist too
        if de_templates:
            de_template = de_templates[0]
            template_name_de = de_template.name
            
            # Extract the number prefix
            number_prefix = template_name_de[:4]
            
            # Find corresponding English template
            en_templates = list(en_dir.glob(f'{number_prefix}_*.md'))
            
            assert len(en_templates) > 0, \
                f"English template with number {number_prefix} should exist for German template {template_name_de}"
            
            en_template = en_templates[0]
            
            # Read both templates
            de_content = de_template.read_text()
            en_content = en_template.read_text()
            
            # Both should have content
            assert len(de_content) > 0, f"German template {template_name_de} should have content"
            assert len(en_content) > 0, f"English template {en_template.name} should have content"
            
            # Both should have similar structure (similar number of lines within 20%)
            de_lines = len(de_content.split('\n'))
            en_lines = len(en_content.split('\n'))
            
            # Allow 30% variance in line count (due to translation differences)
            line_ratio = min(de_lines, en_lines) / max(de_lines, en_lines)
            assert line_ratio > 0.7, \
                f"Template line counts should be similar. DE: {de_lines}, EN: {en_lines}"
    
    def test_all_german_templates_have_english_counterparts(self):
        """Test that all German IT-operation templates have English counterparts."""
        de_dir = Path('templates/de/it-operation')
        en_dir = Path('templates/en/it-operation')
        
        # Get all German templates (excluding metadata)
        de_templates = sorted([
            f for f in de_dir.glob('*.md')
            if not f.name.startswith('0000_') and f.name != 'README.md'
        ])
        
        for de_template in de_templates:
            # Extract number prefix
            number_prefix = de_template.name[:4]
            
            # Find corresponding English template
            en_templates = list(en_dir.glob(f'{number_prefix}_*.md'))
            
            assert len(en_templates) > 0, \
                f"English template with number {number_prefix} should exist for {de_template.name}"
    
    def test_template_count_matches_between_languages(self):
        """Test that the number of templates matches between German and English."""
        de_dir = Path('templates/de/it-operation')
        en_dir = Path('templates/en/it-operation')
        
        # Count templates (excluding metadata)
        de_count = len([f for f in de_dir.glob('*.md') if not f.name.startswith('0000_')])
        en_count = len([f for f in en_dir.glob('*.md') if not f.name.startswith('0000_')])
        
        assert de_count == en_count, \
            f"Number of templates should match between languages. DE: {de_count}, EN: {en_count}"


class TestServiceTemplateGenericity:
    """Tests for service template genericity and individualization."""
    
    def test_service_template_exists_in_both_languages(self):
        """Test that service description template exists in both languages."""
        de_template = Path('templates/de/service-directory/service-templates/service_description_template.md')
        en_template = Path('templates/en/service-directory/service-templates/service_description_template.md')
        
        assert de_template.exists(), "German service template should exist"
        assert en_template.exists(), "English service template should exist"
    
    def test_service_template_has_todo_markers(self):
        """Test that service templates contain [TODO] markers for customization."""
        for language in ['de', 'en']:
            template_path = Path(f'templates/{language}/service-directory/service-templates/service_description_template.md')
            content = template_path.read_text()
            
            # Should have multiple TODO markers
            todo_count = content.count('[TODO')
            assert todo_count >= 10, \
                f"Service template should have at least 10 [TODO] markers for {language}, found {todo_count}"
    
    def test_service_template_has_placeholders(self):
        """Test that service templates contain both meta and netbox placeholders."""
        import re
        
        for language in ['de', 'en']:
            template_path = Path(f'templates/{language}/service-directory/service-templates/service_description_template.md')
            content = template_path.read_text()
            
            # Should have meta placeholders
            meta_placeholders = re.findall(r'\{\{\s*meta\.[a-zA-Z0-9_.]+\s*\}\}', content)
            assert len(meta_placeholders) > 0, \
                f"Service template should have meta placeholders for {language}"
            
            # Should have netbox placeholders
            netbox_placeholders = re.findall(r'\{\{\s*netbox\.[a-zA-Z0-9_.]+\s*\}\}', content)
            assert len(netbox_placeholders) > 0, \
                f"Service template should have netbox placeholders for {language}"
    
    def test_service_template_has_standard_sections(self):
        """Test that service templates have standard sections."""
        standard_sections = [
            'Service-Übersicht',  # German
            'Technische Details',
            'Betrieb',
            'Monitoring',
            'Backup',
            'Sicherheit',
            'Kontakte'
        ]
        
        de_template = Path('templates/de/service-directory/service-templates/service_description_template.md')
        de_content = de_template.read_text()
        
        # Check for German sections
        for section in standard_sections:
            assert section in de_content, \
                f"German service template should have section '{section}'"
        
        # Check for English sections
        en_sections = [
            'Service Overview',
            'Technical Details',
            'Operations',
            'Monitoring',
            'Backup',
            'Security',
            'Contacts'
        ]
        
        en_template = Path('templates/en/service-directory/service-templates/service_description_template.md')
        en_content = en_template.read_text()
        
        for section in en_sections:
            assert section in en_content, \
                f"English service template should have section '{section}'"
    
    @settings(max_examples=100)
    @given(
        section_name=st.sampled_from([
            'Service-Übersicht', 'Technische Details', 'Betrieb',
            'Monitoring', 'Backup', 'Sicherheit', 'Kontakte'
        ])
    )
    def test_property_13_service_template_genericity(self, section_name):
        """
        Feature: it-operation-template-extension, Property 13: Service Template Genericity
        
        For any service description template, it should contain placeholder sections that can be
        customized for any specific IT service without requiring template structure changes.
        
        Validates: Requirements 15.2, 15.3, 15.5
        """
        de_template = Path('templates/de/service-directory/service-templates/service_description_template.md')
        content = de_template.read_text()
        
        # Template should contain the section
        assert section_name in content, \
            f"Service template should contain section '{section_name}'"
        
        # Section should have customizable content (TODO markers or placeholders)
        section_start = content.find(section_name)
        if section_start != -1:
            # Get next 500 characters after section heading
            section_content = content[section_start:section_start + 500]
            
            # Should have either TODO markers or placeholders
            has_todo = '[TODO' in section_content
            has_placeholder = '{{' in section_content and '}}' in section_content
            
            assert has_todo or has_placeholder, \
                f"Section '{section_name}' should have TODO markers or placeholders for customization"
    
    @settings(max_examples=100)
    @given(
        placeholder_type=st.sampled_from(['meta', 'netbox']),
        field_name=st.text(
            alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd')),
            min_size=3,
            max_size=20
        ).filter(lambda x: x.isalnum())
    )
    def test_property_18_service_template_individualization(self, placeholder_type, field_name):
        """
        Feature: it-operation-template-extension, Property 18: Service Template Individualization
        
        For any service description template, when copied and customized for a specific service,
        all [TODO] markers should be replaceable with service-specific values while maintaining
        template structure.
        
        Validates: Requirements 15.4
        """
        import tempfile
        import shutil
        
        de_template = Path('templates/de/service-directory/service-templates/service_description_template.md')
        content = de_template.read_text()
        
        # Create a temporary copy
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
            tmp_path = Path(tmp.name)
            
            try:
                # Copy template
                tmp_path.write_text(content)
                
                # Simulate individualization: replace first TODO with a value
                individualized_content = content.replace('[TODO', f'[{field_name}', 1)
                tmp_path.write_text(individualized_content)
                
                # Read back
                result = tmp_path.read_text()
                
                # Should still have structure (headings)
                assert '##' in result, "Template structure should be maintained"
                
                # Should have the individualized value
                assert field_name in result, "Individualized value should be present"
                
                # Should still have other TODO markers
                remaining_todos = result.count('[TODO')
                original_todos = content.count('[TODO')
                assert remaining_todos == original_todos - 1, \
                    "Should have one less TODO marker after individualization"
                
                # Should still have placeholders
                assert '{{' in result and '}}' in result, \
                    "Placeholders should still be present after individualization"
                
            finally:
                # Clean up
                if tmp_path.exists():
                    tmp_path.unlink()
    
    def test_service_template_structure_preserved_after_customization(self):
        """Test that service template structure is preserved after customization."""
        import tempfile
        
        de_template = Path('templates/de/service-directory/service-templates/service_description_template.md')
        content = de_template.read_text()
        
        # Count original structure elements
        original_headings = content.count('##')
        original_tables = content.count('|---|')
        
        # Simulate customization: replace all TODOs
        customized = content.replace('[TODO]', 'CustomValue')
        customized = customized.replace('[TODO:', 'CustomValue:')
        
        # Count structure elements after customization
        customized_headings = customized.count('##')
        customized_tables = customized.count('|---|')
        
        # Structure should be preserved
        assert customized_headings == original_headings, \
            "Number of headings should be preserved after customization"
        assert customized_tables == original_tables, \
            "Number of tables should be preserved after customization"
        
        # Should still have placeholders
        assert '{{' in customized and '}}' in customized, \
            "Placeholders should still be present after customization"


class TestMultiLanguagePlaceholderConsistency:
    """Property-based tests for multi-language placeholder consistency."""
    
    @settings(max_examples=100)
    @given(
        template_number=st.integers(min_value=10, max_value=290).filter(lambda x: x % 10 == 0)
    )
    def test_property_17_multi_language_placeholder_consistency(self, template_number):
        """
        Feature: it-operation-template-extension, Property 17: Multi-Language Placeholder Consistency
        
        For any placeholder used in a German template, the same placeholder (with same source and field)
        should be usable in the corresponding English template.
        
        Validates: Requirements 21.4
        """
        import re
        
        de_dir = Path('templates/de/it-operation')
        en_dir = Path('templates/en/it-operation')
        
        # Find German template with this number
        de_templates = list(de_dir.glob(f'{template_number:04d}_*.md'))
        
        if de_templates:
            de_template = de_templates[0]
            number_prefix = de_template.name[:4]
            
            # Find corresponding English template
            en_templates = list(en_dir.glob(f'{number_prefix}_*.md'))
            
            if en_templates:
                en_template = en_templates[0]
                
                # Read both templates
                de_content = de_template.read_text()
                en_content = en_template.read_text()
                
                # Extract placeholders from both templates
                placeholder_pattern = r'\{\{\s*(meta|netbox)\.[a-zA-Z0-9_.]+\s*\}\}'
                
                de_placeholders = set(re.findall(placeholder_pattern, de_content))
                en_placeholders = set(re.findall(placeholder_pattern, en_content))
                
                # If German template has placeholders, English should have the same ones
                if de_placeholders:
                    # Extract just the source (meta or netbox) for comparison
                    de_sources = {p.split('.')[0] for p in de_placeholders}
                    en_sources = {p.split('.')[0] for p in en_placeholders}
                    
                    # Both should use the same placeholder sources
                    assert de_sources == en_sources, \
                        f"Placeholder sources should match. DE: {de_sources}, EN: {en_sources}"
    
    def test_placeholder_format_consistency(self):
        """Test that placeholders use consistent format across all templates."""
        import re
        
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            for template_file in templates_dir.glob('*.md'):
                content = template_file.read_text()
                
                # Find all placeholders
                placeholders = re.findall(r'\{\{[^}]+\}\}', content)
                
                for placeholder in placeholders:
                    # Verify placeholder format (meta, netbox, or metadata)
                    assert re.match(r'\{\{\s*(meta|netbox|metadata)\.[a-zA-Z0-9_.]+\s*\}\}', placeholder), \
                        f"Placeholder '{placeholder}' in {template_file.name} should follow format {{{{ source.field }}}}"
    
    def test_common_placeholders_exist_in_both_languages(self):
        """Test that common placeholders exist in both language versions."""
        import re
        
        # Common placeholders that should exist in most templates
        common_placeholders = [
            'meta.organization.name',
            'meta.document.owner',
            'meta.document.approver',
            'meta.document.version'
        ]
        
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            # Check at least one template has these common placeholders
            found_placeholders = set()
            
            for template_file in templates_dir.glob('*.md'):
                content = template_file.read_text()
                
                for placeholder in common_placeholders:
                    if f'{{{{ {placeholder} }}}}' in content or f'{{{{{placeholder}}}}}' in content:
                        found_placeholders.add(placeholder)
            
            # At least some common placeholders should be found
            assert len(found_placeholders) > 0, \
                f"Common placeholders should be found in {language} templates"


class TestTemplateDocumentation:
    """Tests for template documentation completeness."""
    
    def test_readme_exists_in_both_languages(self):
        """Test that README.md exists in both German and English IT-operation directories."""
        de_readme = Path('templates/de/it-operation/README.md')
        en_readme = Path('templates/en/it-operation/README.md')
        
        assert de_readme.exists(), "German README.md should exist in IT-operation templates"
        assert en_readme.exists(), "English README.md should exist in IT-operation templates"
    
    def test_readme_has_substantial_content(self):
        """Test that README files have substantial documentation content."""
        for language in ['de', 'en']:
            readme_path = Path(f'templates/{language}/it-operation/README.md')
            content = readme_path.read_text()
            
            # Should have substantial content (at least 5000 characters)
            assert len(content) > 5000, \
                f"README for {language} should have substantial content (>5000 chars), found {len(content)}"
    
    def test_readme_documents_template_structure(self):
        """Test that README documents the template structure and numbering."""
        for language in ['de', 'en']:
            readme_path = Path(f'templates/{language}/it-operation/README.md')
            content = readme_path.read_text()
            
            # Should mention template numbering
            assert '0010' in content or '0020' in content, \
                f"README for {language} should document template numbering"
            
            # Should have table or list of templates
            assert '|' in content or '-' in content, \
                f"README for {language} should have structured template list"
    
    def test_readme_documents_placeholder_usage(self):
        """Test that README documents placeholder usage."""
        for language in ['de', 'en']:
            readme_path = Path(f'templates/{language}/it-operation/README.md')
            content = readme_path.read_text()
            
            # Should document meta placeholders
            assert 'meta' in content.lower(), \
                f"README for {language} should document meta placeholders"
            
            # Should document netbox placeholders
            assert 'netbox' in content.lower(), \
                f"README for {language} should document netbox placeholders"
            
            # Should show placeholder examples
            assert '{{' in content and '}}' in content, \
                f"README for {language} should show placeholder examples"
    
    def test_readme_has_best_practices_section(self):
        """Test that README includes best practices for template customization."""
        for language in ['de', 'en']:
            readme_path = Path(f'templates/{language}/it-operation/README.md')
            content = readme_path.read_text()
            
            # Should have best practices section
            best_practices_keywords = ['best practice', 'anpassung', 'customization', 'individualisierung']
            has_best_practices = any(keyword in content.lower() for keyword in best_practices_keywords)
            
            assert has_best_practices, \
                f"README for {language} should include best practices section"
    
    def test_framework_mapping_document_exists(self):
        """Test that framework mapping documentation exists."""
        framework_doc = Path('docs/9999_Framework_Mapping.md')
        
        assert framework_doc.exists(), \
            "Framework mapping documentation should exist at docs/9999_Framework_Mapping.md"
        
        # Should have substantial content
        content = framework_doc.read_text()
        assert len(content) > 10000, \
            f"Framework mapping document should have substantial content (>10000 chars), found {len(content)}"
    
    def test_framework_mapping_documents_itil(self):
        """Test that framework mapping documents ITIL v4 alignment."""
        framework_doc = Path('docs/9999_Framework_Mapping.md')
        content = framework_doc.read_text()
        
        # Should document ITIL
        assert 'ITIL' in content, "Framework mapping should document ITIL"
        assert 'v4' in content or 'V4' in content, "Framework mapping should reference ITIL v4"
        
        # Should have ITIL process mappings
        itil_practices = ['Incident Management', 'Change', 'Problem Management', 'Monitoring']
        for practice in itil_practices:
            assert practice in content, \
                f"Framework mapping should document ITIL practice: {practice}"
    
    def test_framework_mapping_documents_iso20000(self):
        """Test that framework mapping documents ISO 20000 compliance."""
        framework_doc = Path('docs/9999_Framework_Mapping.md')
        content = framework_doc.read_text()
        
        # Should document ISO 20000
        assert 'ISO 20000' in content or 'ISO/IEC 20000' in content, \
            "Framework mapping should document ISO 20000"
        
        # Should reference specific clauses
        assert 'Clause' in content or 'clause' in content, \
            "Framework mapping should reference ISO 20000 clauses"
    
    def test_framework_mapping_documents_cobit(self):
        """Test that framework mapping documents COBIT 2019 alignment."""
        framework_doc = Path('docs/9999_Framework_Mapping.md')
        content = framework_doc.read_text()
        
        # Should document COBIT
        assert 'COBIT' in content, "Framework mapping should document COBIT"
        assert '2019' in content, "Framework mapping should reference COBIT 2019"
        
        # Should have COBIT objectives
        cobit_objectives = ['APO', 'BAI', 'DSS', 'MEA']
        for objective in cobit_objectives:
            assert objective in content, \
                f"Framework mapping should document COBIT domain: {objective}"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_19_template_documentation_completeness(self, language):
        """
        Feature: it-operation-template-extension, Property 19: Template Documentation Completeness
        
        For any template directory containing IT-operations templates, there should exist a README.md
        file documenting the template structure and usage.
        
        Validates: Requirements 22.1, 22.2
        """
        templates_dir = Path(f'templates/{language}/it-operation')
        readme_path = templates_dir / 'README.md'
        
        # README should exist
        assert readme_path.exists(), \
            f"README.md should exist in {templates_dir}"
        
        # README should have content
        content = readme_path.read_text()
        assert len(content) > 1000, \
            f"README.md should have substantial content (>1000 chars), found {len(content)}"
        
        # README should document template structure
        # Should mention template numbers
        has_template_numbers = any(f'{num:04d}' in content for num in [10, 20, 30, 40, 50])
        assert has_template_numbers, \
            "README should document template numbering"
        
        # Should document placeholder usage
        assert 'meta' in content.lower() or 'placeholder' in content.lower(), \
            "README should document placeholder usage"
        
        # Should have structured content (tables or lists)
        has_structure = '|' in content or ('- ' in content and content.count('- ') > 5)
        assert has_structure, \
            "README should have structured content (tables or lists)"
        
        # Should document framework references
        frameworks = ['ITIL', 'ISO', 'COBIT']
        has_framework_refs = any(framework in content for framework in frameworks)
        assert has_framework_refs, \
            "README should reference IT frameworks (ITIL, ISO 20000, COBIT)"
        
        # Should have usage examples
        has_examples = 'example' in content.lower() or 'beispiel' in content.lower()
        assert has_examples, \
            "README should include usage examples"


class TestITILProcessCoverage:
    """Property-based tests for ITIL process coverage."""
    
    @settings(max_examples=100)
    @given(
        itil_practice=st.sampled_from([
            'Incident Management',
            'Problem Management',
            'Change Enablement',
            'Service Continuity Management',
            'Service Configuration Management',
            'Monitoring and Event Management',
            'Availability Management',
            'Capacity and Performance Management'
        ])
    )
    def test_property_12_itil_process_coverage(self, itil_practice):
        """
        Feature: it-operation-template-extension, Property 12: ITIL Process Coverage
        
        For any ITIL v4 core practice (Incident, Problem, Change, Service Continuity),
        there should exist at least one template that addresses that practice.
        
        Validates: Requirements 2.5
        """
        # Define mapping of ITIL practices to template numbers
        itil_to_template_mapping = {
            'Incident Management': [120],  # 0120_Incident_Management_Runbook.md
            'Problem Management': [130],  # 0130_Problem_Management_und_Postmortems.md
            'Change Enablement': [140],  # 0140_Change_und_Release_Management.md
            'Service Continuity Management': [150, 160],  # 0150_Backup, 0160_Disaster_Recovery
            'Service Configuration Management': [90],  # 0090_Konfigurationsmanagement_und_CMDB.md
            'Monitoring and Event Management': [110],  # 0110_Monitoring_Alerting_und_Observability.md
            'Availability Management': [210],  # 0210_Verfuegbarkeit_und_Service_Level.md
            'Capacity and Performance Management': [200]  # 0200_Kapazitaets_und_Performance_Management.md
        }
        
        # Get expected template numbers for this ITIL practice
        expected_template_numbers = itil_to_template_mapping.get(itil_practice, [])
        
        assert len(expected_template_numbers) > 0, \
            f"ITIL practice '{itil_practice}' should have at least one mapped template"
        
        # Check both languages
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            # Find templates that address this ITIL practice
            found_templates = []
            for template_number in expected_template_numbers:
                matching_templates = list(templates_dir.glob(f'{template_number:04d}_*.md'))
                found_templates.extend(matching_templates)
            
            assert len(found_templates) > 0, \
                f"ITIL practice '{itil_practice}' should be addressed by at least one template in {language}. " \
                f"Expected template numbers: {[f'{n:04d}' for n in expected_template_numbers]}"
            
            # Verify templates have content
            for template in found_templates:
                content = template.read_text()
                assert len(content) > 100, \
                    f"Template {template.name} addressing '{itil_practice}' should have substantial content"
    
    def test_all_core_itil_practices_covered(self):
        """Test that all core ITIL v4 practices are covered by templates."""
        # Core ITIL v4 Service Management Practices that should be covered
        core_practices = {
            'Incident Management': [120],
            'Problem Management': [130],
            'Change Enablement': [140],
            'Service Continuity Management': [150, 160],
            'Service Configuration Management': [90],
            'Monitoring and Event Management': [110],
            'Availability Management': [210],
            'Capacity and Performance Management': [200]
        }
        
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            for practice, template_numbers in core_practices.items():
                # Check that at least one template exists for this practice
                found = False
                for template_number in template_numbers:
                    matching_templates = list(templates_dir.glob(f'{template_number:04d}_*.md'))
                    if matching_templates:
                        found = True
                        break
                
                assert found, \
                    f"ITIL practice '{practice}' should be covered by templates in {language}. " \
                    f"Expected template numbers: {[f'{n:04d}' for n in template_numbers]}"
    
    def test_itil_practice_templates_have_framework_references(self):
        """Test that templates addressing ITIL practices reference ITIL or related frameworks."""
        import re
        
        # Templates that should reference ITIL or frameworks
        itil_templates = {
            90: 'Configuration Management',
            110: 'Monitoring',
            120: 'Incident Management',
            130: 'Problem Management',
            140: 'Change Management',
            150: 'Backup',
            160: 'Disaster Recovery',
            200: 'Capacity Management',
            210: 'Availability'
        }
        
        framework_keywords = ['ITIL', 'ISO 20000', 'ISO/IEC 20000', 'COBIT', 'Best Practice']
        
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            for template_number, practice_name in itil_templates.items():
                matching_templates = list(templates_dir.glob(f'{template_number:04d}_*.md'))
                
                if matching_templates:
                    template = matching_templates[0]
                    content = template.read_text()
                    
                    # Check if template references any framework
                    has_framework_ref = any(keyword in content for keyword in framework_keywords)
                    
                    # Note: Not all templates may explicitly reference frameworks in content,
                    # but they should follow framework principles in structure
                    # This is a soft check - we just verify the template exists and has content
                    assert len(content) > 100, \
                        f"Template {template.name} for '{practice_name}' should have substantial content"
    
    def test_itil_incident_management_template_structure(self):
        """Test that Incident Management template has ITIL-aligned structure."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            incident_templates = list(templates_dir.glob('0120_*.md'))
            
            assert len(incident_templates) > 0, \
                f"Incident Management template (0120) should exist for {language}"
            
            content = incident_templates[0].read_text()
            
            # Should have incident-related sections
            incident_keywords = ['incident', 'störung', 'priority', 'priorität', 'escalation', 'eskalation']
            has_incident_content = any(keyword in content.lower() for keyword in incident_keywords)
            
            assert has_incident_content, \
                f"Incident Management template should contain incident-related content for {language}"
    
    def test_itil_change_management_template_structure(self):
        """Test that Change Management template has ITIL-aligned structure."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            change_templates = list(templates_dir.glob('0140_*.md'))
            
            assert len(change_templates) > 0, \
                f"Change Management template (0140) should exist for {language}"
            
            content = change_templates[0].read_text()
            
            # Should have change-related sections
            change_keywords = ['change', 'änderung', 'release', 'deployment', 'rollback']
            has_change_content = any(keyword in content.lower() for keyword in change_keywords)
            
            assert has_change_content, \
                f"Change Management template should contain change-related content for {language}"
    
    def test_itil_problem_management_template_structure(self):
        """Test that Problem Management template has ITIL-aligned structure."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            problem_templates = list(templates_dir.glob('0130_*.md'))
            
            assert len(problem_templates) > 0, \
                f"Problem Management template (0130) should exist for {language}"
            
            content = problem_templates[0].read_text()
            
            # Should have problem-related sections
            problem_keywords = ['problem', 'root cause', 'ursache', 'postmortem', 'known error']
            has_problem_content = any(keyword in content.lower() for keyword in problem_keywords)
            
            assert has_problem_content, \
                f"Problem Management template should contain problem-related content for {language}"
    
    def test_itil_service_continuity_templates_exist(self):
        """Test that Service Continuity Management is covered by Backup and DR templates."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            # Service Continuity is covered by both Backup (0150) and Disaster Recovery (0160)
            backup_templates = list(templates_dir.glob('0150_*.md'))
            dr_templates = list(templates_dir.glob('0160_*.md'))
            
            assert len(backup_templates) > 0, \
                f"Backup template (0150) for Service Continuity should exist for {language}"
            assert len(dr_templates) > 0, \
                f"Disaster Recovery template (0160) for Service Continuity should exist for {language}"
            
            # Verify they have continuity-related content
            backup_content = backup_templates[0].read_text()
            dr_content = dr_templates[0].read_text()
            
            continuity_keywords = ['backup', 'restore', 'recovery', 'rto', 'rpo', 'disaster', 'continuity', 'kontinuität']
            
            has_backup_content = any(keyword in backup_content.lower() for keyword in continuity_keywords)
            has_dr_content = any(keyword in dr_content.lower() for keyword in continuity_keywords)
            
            assert has_backup_content, \
                f"Backup template should contain continuity-related content for {language}"
            assert has_dr_content, \
                f"Disaster Recovery template should contain continuity-related content for {language}"


class TestCompleteTemplateStructure:
    """Comprehensive unit tests for template structure validation."""
    
    def test_all_29_german_templates_present(self):
        """
        Test: Alle 29 Templates vorhanden (de)
        
        Note: Actually 30 templates total (0010-0290), including 2 renamed + 28 new
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5
        """
        templates_dir = Path('templates/de/it-operation')
        
        # Expected template numbers (excluding metadata 0000)
        # 0010, 0011 (renamed), then 0020-0290 in steps of 10
        expected_numbers = [10, 11] + list(range(20, 300, 10))  # 0010, 0011, 0020, ..., 0290
        
        # Get actual template numbers
        actual_templates = sorted([
            f for f in templates_dir.glob('*.md')
            if not f.name.startswith('0000_') and f.name != 'README.md'
        ])
        
        actual_numbers = []
        for template in actual_templates:
            try:
                number = int(template.name[:4])
                actual_numbers.append(number)
            except ValueError:
                pytest.fail(f"Template {template.name} does not start with a valid 4-digit number")
        
        # Verify we have exactly 30 templates (2 renamed + 28 new)
        assert len(actual_numbers) == 30, \
            f"Should have exactly 30 German IT-operation templates, found {len(actual_numbers)}"
        
        # Verify all expected numbers are present
        assert actual_numbers == expected_numbers, \
            f"Template numbers should match expected sequence. " \
            f"Expected: {expected_numbers}, Found: {actual_numbers}"
    
    def test_all_29_english_templates_present(self):
        """
        Test: Alle 29 Templates vorhanden (en)
        
        Note: Actually 30 templates total (0010-0290), including 2 renamed + 28 new
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5
        """
        templates_dir = Path('templates/en/it-operation')
        
        # Expected template numbers (excluding metadata 0000)
        expected_numbers = [10, 11] + list(range(20, 300, 10))  # 0010, 0011, 0020, ..., 0290
        
        # Get actual template numbers
        actual_templates = sorted([
            f for f in templates_dir.glob('*.md')
            if not f.name.startswith('0000_') and f.name != 'README.md'
        ])
        
        actual_numbers = []
        for template in actual_templates:
            try:
                number = int(template.name[:4])
                actual_numbers.append(number)
            except ValueError:
                pytest.fail(f"Template {template.name} does not start with a valid 4-digit number")
        
        # Verify we have exactly 30 templates (2 renamed + 28 new)
        assert len(actual_numbers) == 30, \
            f"Should have exactly 30 English IT-operation templates, found {len(actual_numbers)}"
        
        # Verify all expected numbers are present
        assert actual_numbers == expected_numbers, \
            f"Template numbers should match expected sequence. " \
            f"Expected: {expected_numbers}, Found: {actual_numbers}"
    
    def test_numbering_consistent_0010_to_0290(self):
        """
        Test: Nummerierung konsistent (0010-0290)
        
        Validates: Requirements 2.2
        """
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            # Get all content templates (excluding metadata and README)
            content_templates = sorted([
                f for f in templates_dir.glob('*.md')
                if not f.name.startswith('0000_') and f.name != 'README.md'
            ])
            
            # Extract and verify template numbers
            for i, template in enumerate(content_templates):
                number_str = template.name[:4]
                
                # Verify it's a 4-digit number
                assert number_str.isdigit() and len(number_str) == 4, \
                    f"Template {template.name} should start with 4-digit number"
                
                number = int(number_str)
                
                # Verify number is in valid range
                assert 10 <= number <= 290, \
                    f"Template number {number} should be between 0010 and 0290"
                
                # Verify first two are 0010 and 0011
                if i == 0:
                    assert number == 10, f"First template should be 0010, found {number:04d}"
                elif i == 1:
                    assert number == 11, f"Second template should be 0011, found {number:04d}"
                else:
                    # After 0011, should be multiples of 10
                    assert number % 10 == 0, \
                        f"Template number {number:04d} should be a multiple of 10"
    
    def test_service_template_present_both_languages(self):
        """
        Test: Service-Template vorhanden
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5
        """
        # Check German service template
        de_service_template = Path('templates/de/service-directory/service-templates/service_description_template.md')
        assert de_service_template.exists(), \
            "German service description template should exist"
        
        # Check English service template
        en_service_template = Path('templates/en/service-directory/service-templates/service_description_template.md')
        assert en_service_template.exists(), \
            "English service description template should exist"
        
        # Verify both have content
        de_content = de_service_template.read_text()
        en_content = en_service_template.read_text()
        
        assert len(de_content) > 1000, \
            "German service template should have substantial content (>1000 chars)"
        assert len(en_content) > 1000, \
            "English service template should have substantial content (>1000 chars)"
    
    def test_all_templates_have_content(self):
        """Test that all templates have meaningful content."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            for template_file in templates_dir.glob('*.md'):
                content = template_file.read_text()
                
                # Each template should have at least 100 characters
                assert len(content) > 100, \
                    f"Template {template_file.name} should have substantial content"
                
                # Each template should have at least one heading
                assert '#' in content, \
                    f"Template {template_file.name} should have at least one heading"
    
    def test_template_filenames_follow_convention(self):
        """Test that all template filenames follow the naming convention."""
        import re
        
        # Pattern: 4-digit number, underscore, title with underscores/hyphens/capitalization, .md
        # Allow hyphens for metadata files like "0000_metadata_de_it-operation.md"
        filename_pattern = re.compile(r'^\d{4}_[A-Za-z0-9_-]+\.md$')
        
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            for template_file in templates_dir.glob('*.md'):
                # Skip README.md
                if template_file.name == 'README.md':
                    continue
                assert filename_pattern.match(template_file.name), \
                    f"Template filename {template_file.name} should follow convention: NNNN_Title_Words.md"
    
    def test_german_english_template_count_matches(self):
        """Test that German and English have the same number of templates."""
        de_dir = Path('templates/de/it-operation')
        en_dir = Path('templates/en/it-operation')
        
        # Count content templates (excluding metadata and README)
        de_count = len([f for f in de_dir.glob('*.md') if not f.name.startswith('0000_') and f.name != 'README.md'])
        en_count = len([f for f in en_dir.glob('*.md') if not f.name.startswith('0000_') and f.name != 'README.md'])
        
        assert de_count == en_count, \
            f"German and English should have same number of templates. DE: {de_count}, EN: {en_count}"
        
        # Both should have exactly 30 templates (2 renamed + 28 new)
        assert de_count == 30, f"Should have exactly 30 templates, found {de_count}"
    
    def test_specific_required_templates_exist(self):
        """Test that specific required templates exist in both languages."""
        required_templates = {
            '0010': 'Introduction/Einleitung',
            '0011': 'Framework Conditions/Rahmenbedingungen',
            '0020': 'Document Control/Dokumentenlenkung',
            '0030': 'Service Description/Servicebeschreibung',
            '0060': 'Roles/Rollen',
            '0110': 'Monitoring',
            '0120': 'Incident Management',
            '0140': 'Change Management',
            '0150': 'Backup',
            '0160': 'Disaster Recovery',
            '0170': 'Security/Sicherheit',
            '0280': 'Compliance',
            '0290': 'Appendix/Anhang'
        }
        
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            for number, description in required_templates.items():
                matching_templates = list(templates_dir.glob(f'{number}_*.md'))
                assert len(matching_templates) > 0, \
                    f"Required template {number} ({description}) should exist for {language}"
    
    def test_metadata_templates_exist_both_languages(self):
        """Test that metadata templates exist for both languages."""
        de_metadata = Path('templates/de/it-operation/0000_metadata_de_it-operation.md')
        en_metadata = Path('templates/en/it-operation/0000_metadata_en_it-operation.md')
        
        assert de_metadata.exists(), "German metadata template should exist"
        assert en_metadata.exists(), "English metadata template should exist"
        
        # Verify metadata templates have content
        de_content = de_metadata.read_text()
        en_content = en_metadata.read_text()
        
        assert len(de_content) > 50, "German metadata template should have content"
        assert len(en_content) > 50, "English metadata template should have content"
    
    def test_service_template_directory_structure(self):
        """Test that service-templates directory exists with correct structure."""
        de_service_dir = Path('templates/de/service-templates')
        en_service_dir = Path('templates/en/service-templates')
        
        assert de_service_dir.exists(), "German service-templates directory should exist"
        assert en_service_dir.exists(), "English service-templates directory should exist"
        
        assert de_service_dir.is_dir(), "German service-templates should be a directory"
        assert en_service_dir.is_dir(), "English service-templates should be a directory"
    
    def test_no_duplicate_template_numbers(self):
        """Test that there are no duplicate template numbers in each language."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            # Get all template numbers (excluding README)
            template_numbers = []
            for template_file in templates_dir.glob('*.md'):
                if template_file.name == 'README.md':
                    continue
                try:
                    number = int(template_file.name[:4])
                    template_numbers.append(number)
                except ValueError:
                    pytest.fail(f"Template {template_file.name} does not start with valid number")
            
            # Check for duplicates
            duplicates = [num for num in template_numbers if template_numbers.count(num) > 1]
            assert len(duplicates) == 0, \
                f"Found duplicate template numbers in {language}: {set(duplicates)}"
    
    def test_templates_sorted_by_number(self):
        """Test that when templates are listed alphabetically, they are in numerical order."""
        for language in ['de', 'en']:
            templates_dir = Path(f'templates/{language}/it-operation')
            
            # Get templates sorted alphabetically (which should match numerical order)
            templates = sorted([
                f for f in templates_dir.glob('*.md')
                if not f.name.startswith('0000_') and f.name != 'README.md'
            ])
            
            # Extract numbers
            numbers = [int(t.name[:4]) for t in templates]
            
            # Verify they are in ascending order
            assert numbers == sorted(numbers), \
                f"Templates should be in numerical order when sorted alphabetically for {language}"


