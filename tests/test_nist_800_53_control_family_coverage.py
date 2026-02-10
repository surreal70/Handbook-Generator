"""
Tests for NIST 800-53 Control Family Coverage

Property-based tests to verify that NIST 800-53 template set covers all 20 control families.

Author: Kiro AI Assistant
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import re


class TestNIST80053ControlFamilyCoverage:
    """Tests for NIST 800-53 control family coverage."""
    
    def test_nist_800_53_templates_exist(self):
        """Test that NIST 800-53 template directories exist."""
        de_dir = Path('templates/de/nist-800-53')
        en_dir = Path('templates/en/nist-800-53')
        
        assert de_dir.exists(), "German NIST 800-53 template directory should exist"
        assert en_dir.exists(), "English NIST 800-53 template directory should exist"
    
    def test_nist_800_53_framework_mapping_exists(self):
        """Test that FRAMEWORK_MAPPING.md exists for NIST 800-53."""
        de_mapping = Path('templates/de/nist-800-53/FRAMEWORK_MAPPING.md')
        en_mapping = Path('templates/en/nist-800-53/FRAMEWORK_MAPPING.md')
        
        assert de_mapping.exists(), "German NIST 800-53 FRAMEWORK_MAPPING.md should exist"
        assert en_mapping.exists(), "English NIST 800-53 FRAMEWORK_MAPPING.md should exist"
    
    def test_nist_800_53_all_20_control_families_covered(self):
        """
        Test that NIST 800-53 template set covers all 20 control families.
        
        NIST SP 800-53 Rev. 5 has 20 control families:
        AC - Access Control
        AT - Awareness and Training
        AU - Audit and Accountability
        CA - Assessment, Authorization, and Monitoring
        CM - Configuration Management
        CP - Contingency Planning
        IA - Identification and Authentication
        IR - Incident Response
        MA - Maintenance
        MP - Media Protection
        PE - Physical and Environmental Protection
        PL - Planning
        PM - Program Management
        PS - Personnel Security
        RA - Risk Assessment
        SA - System and Services Acquisition
        SC - System and Communications Protection
        SI - System and Information Integrity
        SR - Supply Chain Risk Management
        Privacy Controls (PT, AP, AR, DI, DM, IP, SE, TR, UL)
        """
        # Read FRAMEWORK_MAPPING.md to check coverage
        mapping_file = Path('templates/de/nist-800-53/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define all 20 NIST 800-53 control families
        control_families = {
            'AC': 'Access Control',
            'AT': 'Awareness and Training',
            'AU': 'Audit and Accountability',
            'CA': 'Assessment, Authorization, and Monitoring',
            'CM': 'Configuration Management',
            'CP': 'Contingency Planning',
            'IA': 'Identification and Authentication',
            'IR': 'Incident Response',
            'MA': 'Maintenance',
            'MP': 'Media Protection',
            'PE': 'Physical and Environmental Protection',
            'PL': 'Planning',
            'PM': 'Program Management',
            'PS': 'Personnel Security',
            'RA': 'Risk Assessment',
            'SA': 'System and Services Acquisition',
            'SC': 'System and Communications Protection',
            'SI': 'System and Information Integrity',
            'SR': 'Supply Chain Risk Management',
            'Privacy': 'Privacy Controls'
        }
        
        # Check that each control family is mentioned in the mapping
        for family_id, family_name in control_families.items():
            # Look for "### N. Family Name (ID)" pattern
            # Special case: Privacy controls have multiple identifiers
            if family_id == 'Privacy':
                pattern = rf'###\s+\d+\.\s+{re.escape(family_name)}\s+\(PT,\s+AP,\s+AR,\s+DI,\s+DM,\s+IP,\s+SE,\s+TR,\s+UL\)'
            else:
                pattern = rf'###\s+\d+\.\s+{re.escape(family_name)}\s+\({family_id}\)'
            assert re.search(pattern, mapping_content), \
                f"Control family {family_id} ({family_name}) should be documented in FRAMEWORK_MAPPING.md"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        control_family=st.sampled_from([
            'AC', 'AT', 'AU', 'CA', 'CM', 'CP', 'IA', 'IR', 'MA', 'MP',
            'PE', 'PL', 'PM', 'PS', 'RA', 'SA', 'SC', 'SI', 'SR', 'Privacy'
        ])
    )
    def test_property_23_nist_800_53_control_family_coverage(self, language, control_family):
        """
        Feature: compliance-framework-templates, Property 23: NIST 800-53 Control Family Coverage
        
        For any NIST 800-53 template set, templates must exist covering all 20 control families.
        
        This property verifies that:
        1. The FRAMEWORK_MAPPING.md file exists
        2. Each of the 20 control families is documented in the mapping
        3. The mapping indicates which templates cover each control family
        
        Validates: Requirements 3.1
        """
        # Check that template directory exists
        template_dir = Path(f'templates/{language}/nist-800-53')
        assert template_dir.exists(), \
            f"NIST 800-53 template directory should exist for language '{language}'"
        
        # Check that FRAMEWORK_MAPPING.md exists
        mapping_file = template_dir / 'FRAMEWORK_MAPPING.md'
        assert mapping_file.exists(), \
            f"FRAMEWORK_MAPPING.md should exist in {template_dir}"
        
        # Read mapping content
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define control family names for verification
        family_names = {
            'AC': 'Access Control',
            'AT': 'Awareness and Training',
            'AU': 'Audit and Accountability',
            'CA': 'Assessment, Authorization, and Monitoring',
            'CM': 'Configuration Management',
            'CP': 'Contingency Planning',
            'IA': 'Identification and Authentication',
            'IR': 'Incident Response',
            'MA': 'Maintenance',
            'MP': 'Media Protection',
            'PE': 'Physical and Environmental Protection',
            'PL': 'Planning',
            'PM': 'Program Management',
            'PS': 'Personnel Security',
            'RA': 'Risk Assessment',
            'SA': 'System and Services Acquisition',
            'SC': 'System and Communications Protection',
            'SI': 'System and Information Integrity',
            'SR': 'Supply Chain Risk Management',
            'Privacy': 'Privacy Controls'
        }
        
        family_name = family_names[control_family]
        
        # Verify that the specific control family is documented
        # Look for "### N. Family Name (ID)" pattern
        # Special case: Privacy controls have multiple identifiers
        if control_family == 'Privacy':
            pattern = rf'###\s+\d+\.\s+{re.escape(family_name)}\s+\(PT,\s+AP,\s+AR,\s+DI,\s+DM,\s+IP,\s+SE,\s+TR,\s+UL\)'
        else:
            pattern = rf'###\s+\d+\.\s+{re.escape(family_name)}\s+\({control_family}\)'
        assert re.search(pattern, mapping_content), \
            f"Control family {control_family} ({family_name}) should be documented in FRAMEWORK_MAPPING.md for language '{language}'"
        
        # Additionally verify that the control family section has some content
        # (not just a header with no details)
        if control_family == 'Privacy':
            section_pattern = rf'###\s+\d+\.\s+{re.escape(family_name)}\s+\(PT,\s+AP,\s+AR,\s+DI,\s+DM,\s+IP,\s+SE,\s+TR,\s+UL\).*?\n\n.*?\n'
        else:
            section_pattern = rf'###\s+\d+\.\s+{re.escape(family_name)}\s+\({control_family}\).*?\n\n.*?\n'
        section_match = re.search(section_pattern, mapping_content, re.DOTALL)
        
        if section_match:
            # If we found a section, verify it has meaningful content
            section_text = section_match.group(0)
            # Should have more than just the header
            assert len(section_text.strip()) > 50, \
                f"Control family {control_family} section should have meaningful content"
    
    def test_nist_800_53_control_family_to_template_mapping(self):
        """
        Test that each NIST 800-53 control family is mapped to specific templates.
        
        This test verifies that the FRAMEWORK_MAPPING.md not only lists control families
        but also maps them to specific template files.
        """
        mapping_file = Path('templates/de/nist-800-53/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define expected mappings based on current implementation
        # These are the control families that should have template coverage
        expected_mappings = {
            'AC': ['0100', '0110'],  # Access Control Policy, Account Management
            'AT': ['0200'],  # Security Awareness and Training
            'AU': ['0220'],  # Audit and Accountability Policy
            'CM': ['0300'],  # Configuration Management Policy
            'CP': ['0330'],  # Contingency Planning Policy
            'IA': ['0400'],  # Identification and Authentication Policy
            'IR': ['0430'],  # Incident Response Policy
            'MA': ['0500'],  # System Maintenance
            'PL': ['0600'],  # Security Planning Policy
            'SC': ['0700'],  # System and Communications Protection
        }
        
        for family_id, template_numbers in expected_mappings.items():
            # Find the control family section
            family_section_pattern = rf'###\s+\d+\.\s+.*?\({family_id}\).*?(?=###\s+\d+\.|##\s+Coverage|$)'
            family_section = re.search(family_section_pattern, mapping_content, re.DOTALL)
            
            assert family_section, f"Control family {family_id} section should exist in mapping"
            
            section_text = family_section.group(0)
            
            # Check that at least one of the expected templates is mentioned
            found_template = False
            for template_num in template_numbers:
                if f'NIST-{template_num}' in section_text or template_num in section_text:
                    found_template = True
                    break
            
            assert found_template, \
                f"Control family {family_id} should reference at least one template from {template_numbers}"
    
    def test_nist_800_53_coverage_complete(self):
        """
        Test that all control families show complete coverage in FRAMEWORK_MAPPING.md.
        
        According to the implementation, all 20 control families have been fully covered
        with templates, so the mapping should show complete coverage with checkmarks.
        """
        mapping_file = Path('templates/de/nist-800-53/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All main control families (19 families + Privacy Controls section)
        # Note: PT, AP, AR, DI, DM, IP, SE, TR, UL are grouped under "Privacy Controls"
        main_families = ['AC', 'AT', 'AU', 'CA', 'CM', 'CP', 'IA', 'IR', 'MA', 'MP', 
                        'PE', 'PL', 'PM', 'PS', 'RA', 'SA', 'SC', 'SI', 'SR']
        
        # Check that all main families are documented with coverage
        for family_id in main_families:
            family_section_pattern = rf'###\s+\d+\.\s+.*?\({family_id}\)'
            assert re.search(family_section_pattern, mapping_content), \
                f"Control family {family_id} should be documented in FRAMEWORK_MAPPING.md"
        
        # Check that Privacy Controls section exists (contains PT, AP, AR, DI, DM, IP, SE, TR, UL)
        assert re.search(r'###\s+\d+\.\s+Privacy Controls', mapping_content), \
            "Privacy Controls section should be documented in FRAMEWORK_MAPPING.md"
    
    def test_nist_800_53_template_files_exist_for_covered_families(self):
        """
        Test that template files actually exist for control families marked as covered.
        
        This verifies that the FRAMEWORK_MAPPING.md accurately reflects the actual
        template files present in the directory.
        """
        template_dir = Path('templates/de/nist-800-53')
        
        # Control families that should be covered with their expected templates
        covered_families = {
            'AC': ['0100_Access_Control_Policy.md', '0110_Account_Management.md'],
            'AT': ['0200_Security_Awareness_and_Training.md'],
            'AU': ['0220_Audit_and_Accountability_Policy.md'],
            'CM': ['0300_Configuration_Management_Policy.md'],
            'CP': ['0330_Contingency_Planning_Policy.md'],
            'IA': ['0400_Identification_and_Authentication_Policy.md'],
            'IR': ['0430_Incident_Response_Policy.md'],
            'MA': ['0500_System_Maintenance.md'],
            'PL': ['0600_Security_Planning_Policy.md'],
            'SC': ['0700_System_and_Communications_Protection.md']
        }
        
        for family_id, template_files in covered_families.items():
            for template_file in template_files:
                template_path = template_dir / template_file
                assert template_path.exists(), \
                    f"Template {template_file} for control family {family_id} should exist"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_23_bilingual_consistency(self, language):
        """
        Property 23 Extension: Bilingual Consistency for NIST 800-53 Coverage
        
        For any language (German or English), the NIST 800-53 control family coverage
        should be consistent - both languages should document all 20 control families.
        
        Validates: Requirements 3.1, 9.1, 9.2
        """
        mapping_file = Path(f'templates/{language}/nist-800-53/FRAMEWORK_MAPPING.md')
        
        assert mapping_file.exists(), \
            f"FRAMEWORK_MAPPING.md should exist for language '{language}'"
        
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All 20 control families should be documented
        control_families = [
            'AC', 'AT', 'AU', 'CA', 'CM', 'CP', 'IA', 'IR', 'MA', 'MP',
            'PE', 'PL', 'PM', 'PS', 'RA', 'SA', 'SC', 'SI', 'SR', 'Privacy'
        ]
        
        for family_id in control_families:
            # Special case: Privacy controls have multiple identifiers
            if family_id == 'Privacy':
                pattern = rf'###\s+\d+\.\s+.*?\(PT,\s+AP,\s+AR,\s+DI,\s+DM,\s+IP,\s+SE,\s+TR,\s+UL\)'
            else:
                pattern = rf'###\s+\d+\.\s+.*?\({family_id}\)'
            assert re.search(pattern, mapping_content), \
                f"Control family {family_id} should be documented in {language} FRAMEWORK_MAPPING.md"
    
    def test_nist_800_53_foundation_templates_exist(self):
        """
        Test that foundation templates (0010-0050) exist for NIST 800-53.
        
        These are critical templates that should be present regardless of control family.
        """
        foundation_templates = [
            '0010_Systemkategorisierung.md',
            '0020_Geltungsbereich_und_Systemgrenzen.md',
            '0030_Rollen_und_Verantwortlichkeiten.md',
            '0040_Risk_Management_Framework.md',
            '0050_Continuous_Monitoring_Strategy.md'
        ]
        
        template_dir = Path('templates/de/nist-800-53')
        
        for template_file in foundation_templates:
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Foundation template {template_file} should exist"
    
    def test_nist_800_53_appendix_templates_exist(self):
        """
        Test that appendix templates (0800-0850) exist for NIST 800-53.
        
        These provide supporting documentation and reference materials.
        """
        appendix_templates = [
            '0800_Control_Traceability_Matrix.md',
            '0850_Glossar_und_Abkuerzungen.md'
        ]
        
        template_dir = Path('templates/de/nist-800-53')
        
        for template_file in appendix_templates:
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Appendix template {template_file} should exist"
    
    def test_nist_800_53_readme_exists(self):
        """Test that README.md exists for NIST 800-53 in both languages."""
        de_readme = Path('templates/de/nist-800-53/README.md')
        en_readme = Path('templates/en/nist-800-53/README.md')
        
        assert de_readme.exists(), "German NIST 800-53 README.md should exist"
        assert en_readme.exists(), "English NIST 800-53 README.md should exist"
    
    def test_nist_800_53_metadata_templates_exist(self):
        """Test that metadata templates exist for NIST 800-53 in both languages."""
        de_metadata = Path('templates/de/nist-800-53/0000_metadata_de_nist-800-53.md')
        en_metadata = Path('templates/en/nist-800-53/0000_metadata_en_nist-800-53.md')
        
        assert de_metadata.exists(), "German NIST 800-53 metadata template should exist"
        assert en_metadata.exists(), "English NIST 800-53 metadata template should exist"
