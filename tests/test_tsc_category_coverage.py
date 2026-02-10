"""
Tests for TSC Category Coverage

Property-based tests to verify that TSC template set covers all Trust Services Categories.

Author: Kiro AI Assistant
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import re


class TestTSCCategoryCoverage:
    """Tests for TSC category coverage."""
    
    def test_tsc_templates_exist(self):
        """Test that TSC template directories exist."""
        de_dir = Path('templates/de/tsc')
        en_dir = Path('templates/en/tsc')
        
        assert de_dir.exists(), "German TSC template directory should exist"
        assert en_dir.exists(), "English TSC template directory should exist"
    
    def test_tsc_framework_mapping_exists(self):
        """Test that FRAMEWORK_MAPPING.md exists for TSC."""
        de_mapping = Path('templates/de/tsc/FRAMEWORK_MAPPING.md')
        en_mapping = Path('templates/en/tsc/FRAMEWORK_MAPPING.md')
        
        assert de_mapping.exists(), "German TSC FRAMEWORK_MAPPING.md should exist"
        assert en_mapping.exists(), "English TSC FRAMEWORK_MAPPING.md should exist"
    
    def test_tsc_all_categories_covered(self):
        """
        Test that TSC template set covers all Trust Services Categories.
        
        TSC has 5 categories:
        - Common Criteria (CC) - Security (Required for all SOC 2)
        - Availability (A) - Optional
        - Processing Integrity (PI) - Optional
        - Confidentiality (C) - Optional
        - Privacy (P) - Optional
        """
        # Read FRAMEWORK_MAPPING.md to check coverage
        mapping_file = Path('templates/de/tsc/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define all TSC categories
        categories = {
            'CC': 'Common Criteria',
            'A': 'Availability',
            'PI': 'Processing Integrity',
            'C': 'Confidentiality',
            'P': 'Privacy'
        }
        
        # Check that each category is mentioned in the mapping
        for category_id, category_name in categories.items():
            # Look for "### Category Name (ID)" pattern
            pattern = rf'###\s+{re.escape(category_name)}\s+\({category_id}\)'
            assert re.search(pattern, mapping_content), \
                f"TSC category {category_id} ({category_name}) should be documented in FRAMEWORK_MAPPING.md"
    
    def test_tsc_common_criteria_coverage(self):
        """
        Test that all 9 Common Criteria (CC1-CC9) are covered.
        
        Common Criteria are required for all SOC 2 reports:
        CC1 - Control Environment
        CC2 - Communication and Information
        CC3 - Risk Assessment
        CC4 - Monitoring Activities
        CC5 - Control Activities
        CC6 - Logical and Physical Access Controls
        CC7 - System Operations
        CC8 - Change Management
        CC9 - Risk Mitigation
        """
        mapping_file = Path('templates/de/tsc/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        common_criteria = {
            'CC1': 'Control Environment',
            'CC2': 'Communication',
            'CC3': 'Risk Assessment',
            'CC4': 'Monitoring',
            'CC5': 'Control Activities',
            'CC6': 'Logical and Physical Access',
            'CC7': 'System Operations',
            'CC8': 'Change Management',
            'CC9': 'Risk Mitigation'
        }
        
        for cc_id, cc_name in common_criteria.items():
            # Look for "**CCN: Name**" pattern
            pattern = rf'\*\*{cc_id}:.*?\*\*'
            assert re.search(pattern, mapping_content), \
                f"Common Criterion {cc_id} ({cc_name}) should be documented in FRAMEWORK_MAPPING.md"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        category=st.sampled_from(['CC', 'A', 'PI', 'C', 'P'])
    )
    def test_property_24_tsc_category_coverage(self, language, category):
        """
        Feature: compliance-framework-templates, Property 24: TSC Category Coverage
        
        For any TSC template set, templates must exist covering all 5 Trust Services Categories.
        
        This property verifies that:
        1. The FRAMEWORK_MAPPING.md file exists
        2. Each of the 5 TSC categories is documented in the mapping
        3. The mapping indicates which templates cover each category
        
        Validates: Requirements 4.1
        """
        # Check that template directory exists
        template_dir = Path(f'templates/{language}/tsc')
        assert template_dir.exists(), \
            f"TSC template directory should exist for language '{language}'"
        
        # Check that FRAMEWORK_MAPPING.md exists
        mapping_file = template_dir / 'FRAMEWORK_MAPPING.md'
        assert mapping_file.exists(), \
            f"FRAMEWORK_MAPPING.md should exist in {template_dir}"
        
        # Read mapping content
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define category names for verification
        category_names = {
            'CC': 'Common Criteria',
            'A': 'Availability',
            'PI': 'Processing Integrity',
            'C': 'Confidentiality',
            'P': 'Privacy'
        }
        
        category_name = category_names[category]
        
        # Verify that the specific category is documented
        # Look for "### Category Name (ID)" pattern
        pattern = rf'###\s+{re.escape(category_name)}\s+\({category}\)'
        assert re.search(pattern, mapping_content), \
            f"TSC category {category} ({category_name}) should be documented in FRAMEWORK_MAPPING.md for language '{language}'"
        
        # Additionally verify that the category section has some content
        # (not just a header with no details)
        section_pattern = rf'###\s+{re.escape(category_name)}\s+\({category}\).*?\n\n.*?\n'
        section_match = re.search(section_pattern, mapping_content, re.DOTALL)
        
        if section_match:
            # If we found a section, verify it has meaningful content
            section_text = section_match.group(0)
            # Should have more than just the header
            assert len(section_text.strip()) > 50, \
                f"TSC category {category} section should have meaningful content"
    
    def test_tsc_category_to_template_mapping(self):
        """
        Test that each TSC category is mapped to specific templates.
        
        This test verifies that the FRAMEWORK_MAPPING.md not only lists categories
        but also maps them to specific template files.
        """
        mapping_file = Path('templates/de/tsc/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define expected mappings based on current implementation
        expected_mappings = {
            'CC': ['0100', '0110', '0120', '0130', '0140', '0150'],  # Common Criteria
            'A': ['0200'],  # Availability
            'PI': ['0240'],  # Processing Integrity
            'C': ['0280'],  # Confidentiality
            'P': ['0320']  # Privacy
        }
        
        for category_id, template_numbers in expected_mappings.items():
            # Find the category section
            category_section_pattern = rf'###\s+.*?\({category_id}\).*?(?=###\s+|##\s+Coverage|$)'
            category_section = re.search(category_section_pattern, mapping_content, re.DOTALL)
            
            assert category_section, f"TSC category {category_id} section should exist in mapping"
            
            section_text = category_section.group(0)
            
            # Check that at least one of the expected templates is mentioned
            found_template = False
            for template_num in template_numbers:
                if f'TSC-{template_num}' in section_text or template_num in section_text:
                    found_template = True
                    break
            
            assert found_template, \
                f"TSC category {category_id} should reference at least one template from {template_numbers}"
    
    def test_tsc_coverage_analysis_documented(self):
        """
        Test that coverage analysis is documented in FRAMEWORK_MAPPING.md.
        
        The mapping should include a coverage analysis section showing 100% coverage
        for all categories.
        """
        mapping_file = Path('templates/de/tsc/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for coverage analysis section
        assert '## Coverage Analysis' in mapping_content or '## Abdeckungsanalyse' in mapping_content, \
            "FRAMEWORK_MAPPING.md should include a coverage analysis section"
        
        # Check that 100% coverage is documented
        assert '100% Coverage' in mapping_content or '100% Abdeckung' in mapping_content, \
            "Coverage analysis should show 100% coverage"
    
    def test_tsc_template_files_exist_for_categories(self):
        """
        Test that template files actually exist for all TSC categories.
        
        This verifies that the FRAMEWORK_MAPPING.md accurately reflects the actual
        template files present in the directory.
        """
        template_dir = Path('templates/de/tsc')
        
        # Categories with their expected templates
        category_templates = {
            'CC': [
                '0100_CC1_Control_Environment.md',
                '0110_CC2_Communication.md',
                '0120_CC3_Risk_Assessment.md',
                '0130_CC4_Monitoring.md',
                '0140_CC5_Control_Activities.md',
                '0150_CC6_CC9_Security_Controls.md'
            ],
            'A': ['0200_A1_Availability.md'],
            'PI': ['0240_PI1_Processing_Integrity.md'],
            'C': ['0280_C1_Confidentiality.md'],
            'P': ['0320_P1_Privacy.md']
        }
        
        for category_id, template_files in category_templates.items():
            for template_file in template_files:
                template_path = template_dir / template_file
                assert template_path.exists(), \
                    f"Template {template_file} for TSC category {category_id} should exist"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_24_bilingual_consistency(self, language):
        """
        Property 24 Extension: Bilingual Consistency for TSC Coverage
        
        For any language (German or English), the TSC category coverage
        should be consistent - both languages should document all 5 categories.
        
        Validates: Requirements 4.1, 9.1, 9.2
        """
        mapping_file = Path(f'templates/{language}/tsc/FRAMEWORK_MAPPING.md')
        
        assert mapping_file.exists(), \
            f"FRAMEWORK_MAPPING.md should exist for language '{language}'"
        
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All 5 TSC categories should be documented
        categories = ['CC', 'A', 'PI', 'C', 'P']
        
        for category_id in categories:
            # Look for category documentation
            pattern = rf'###\s+.*?\({category_id}\)'
            assert re.search(pattern, mapping_content), \
                f"TSC category {category_id} should be documented in {language} FRAMEWORK_MAPPING.md"
    
    def test_tsc_foundation_templates_exist(self):
        """
        Test that foundation templates (0010-0050) exist for TSC.
        
        These are critical templates that should be present for system description.
        """
        foundation_templates = [
            '0010_Systembeschreibung.md',
            '0020_System_Boundaries.md',
            '0030_System_Komponenten.md',
            '0040_Rollen_und_Verantwortlichkeiten.md',
            '0050_Control_Environment.md'
        ]
        
        template_dir = Path('templates/de/tsc')
        
        for template_file in foundation_templates:
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Foundation template {template_file} should exist"
    
    def test_tsc_appendix_templates_exist(self):
        """
        Test that appendix templates (0400-0450) exist for TSC.
        
        These provide supporting documentation and reference materials.
        """
        appendix_templates = [
            '0400_Control_Matrix.md',
            '0440_Glossar.md'
        ]
        
        template_dir = Path('templates/de/tsc')
        
        for template_file in appendix_templates:
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Appendix template {template_file} should exist"
    
    def test_tsc_readme_exists(self):
        """Test that README.md exists for TSC in both languages."""
        de_readme = Path('templates/de/tsc/README.md')
        en_readme = Path('templates/en/tsc/README.md')
        
        assert de_readme.exists(), "German TSC README.md should exist"
        assert en_readme.exists(), "English TSC README.md should exist"
    
    def test_tsc_metadata_templates_exist(self):
        """Test that metadata templates exist for TSC in both languages."""
        de_metadata = Path('templates/de/tsc/0000_metadata_de_tsc.md')
        en_metadata = Path('templates/en/tsc/0000_metadata_en_tsc.md')
        
        assert de_metadata.exists(), "German TSC metadata template should exist"
        assert en_metadata.exists(), "English TSC metadata template should exist"
    
    def test_tsc_common_criteria_all_nine_covered(self):
        """
        Test that all 9 Common Criteria (CC1-CC9) have template coverage.
        
        This is critical as Common Criteria are required for all SOC 2 reports.
        """
        template_dir = Path('templates/de/tsc')
        
        # All 9 Common Criteria should be covered
        cc_templates = {
            'CC1': '0100_CC1_Control_Environment.md',
            'CC2': '0110_CC2_Communication.md',
            'CC3': '0120_CC3_Risk_Assessment.md',
            'CC4': '0130_CC4_Monitoring.md',
            'CC5': '0140_CC5_Control_Activities.md',
            'CC6-CC9': '0150_CC6_CC9_Security_Controls.md'
        }
        
        for cc_id, template_file in cc_templates.items():
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Template for Common Criterion {cc_id} should exist: {template_file}"
    
    def test_tsc_optional_categories_all_covered(self):
        """
        Test that all 4 optional TSC categories have template coverage.
        
        While optional, organizations may need any combination of these categories.
        """
        template_dir = Path('templates/de/tsc')
        
        # All 4 optional categories should be covered
        optional_templates = {
            'Availability': '0200_A1_Availability.md',
            'Processing Integrity': '0240_PI1_Processing_Integrity.md',
            'Confidentiality': '0280_C1_Confidentiality.md',
            'Privacy': '0320_P1_Privacy.md'
        }
        
        for category_name, template_file in optional_templates.items():
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Template for optional category '{category_name}' should exist: {template_file}"
    
    def test_tsc_soc2_report_types_documented(self):
        """
        Test that SOC 2 report types (Type I and Type II) are documented.
        
        The README should explain the difference between Type I and Type II reports.
        """
        readme_file = Path('templates/de/tsc/README.md')
        readme_content = readme_file.read_text(encoding='utf-8')
        
        # Check for Type I and Type II documentation
        assert 'Type I' in readme_content or 'Type 1' in readme_content, \
            "README should document Type I reports"
        assert 'Type II' in readme_content or 'Type 2' in readme_content, \
            "README should document Type II reports"
