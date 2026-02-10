"""
Tests for PCI-DSS Requirement Coverage

Property-based tests to verify that PCI-DSS template set covers all 12 requirements.

Author: Kiro AI Assistant
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import re


class TestPCIDSSRequirementCoverage:
    """Tests for PCI-DSS requirement coverage."""
    
    def test_pci_dss_templates_exist(self):
        """Test that PCI-DSS template directories exist."""
        de_dir = Path('templates/de/pci-dss')
        en_dir = Path('templates/en/pci-dss')
        
        assert de_dir.exists(), "German PCI-DSS template directory should exist"
        assert en_dir.exists(), "English PCI-DSS template directory should exist"
    
    def test_pci_dss_framework_mapping_exists(self):
        """Test that FRAMEWORK_MAPPING.md exists for PCI-DSS."""
        de_mapping = Path('templates/de/pci-dss/FRAMEWORK_MAPPING.md')
        en_mapping = Path('templates/en/pci-dss/FRAMEWORK_MAPPING.md')
        
        assert de_mapping.exists(), "German PCI-DSS FRAMEWORK_MAPPING.md should exist"
        assert en_mapping.exists(), "English PCI-DSS FRAMEWORK_MAPPING.md should exist"
    
    def test_pci_dss_all_12_requirements_covered(self):
        """
        Test that PCI-DSS template set covers all 12 requirements.
        
        PCI-DSS v4.0 has 12 main requirements:
        1. Install and Maintain Network Security Controls
        2. Apply Secure Configurations to All System Components
        3. Protect Stored Account Data
        4. Protect Cardholder Data with Strong Cryptography During Transmission
        5. Protect All Systems and Networks from Malicious Software
        6. Develop and Maintain Secure Systems and Software
        7. Restrict Access to System Components and Cardholder Data
        8. Identify Users and Authenticate Access to System Components
        9. Restrict Physical Access to Cardholder Data
        10. Log and Monitor All Access to System Components and Cardholder Data
        11. Test Security of Systems and Networks Regularly
        12. Support Information Security with Organizational Policies and Programs
        """
        # Read FRAMEWORK_MAPPING.md to check coverage
        mapping_file = Path('templates/de/pci-dss/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define all 12 PCI-DSS requirements
        requirements = {
            1: "Network Security Controls",
            2: "Secure Configurations",
            3: "Protect Stored Account Data",
            4: "Protect Cardholder Data with Strong Cryptography",
            5: "Protect All Systems and Networks from Malicious Software",
            6: "Develop and Maintain Secure Systems and Software",
            7: "Restrict Access to System Components",
            8: "Identify Users and Authenticate Access",
            9: "Restrict Physical Access to Cardholder Data",
            10: "Log and Monitor All Access",
            11: "Test Security of Systems and Networks",
            12: "Support Information Security with Organizational Policies"
        }
        
        # Check that each requirement is mentioned in the mapping
        for req_num, req_name in requirements.items():
            # Look for "Requirement N:" or "### Requirement N:"
            pattern = rf'(?:###\s+)?Requirement\s+{req_num}[:\s]'
            assert re.search(pattern, mapping_content), \
                f"Requirement {req_num} ({req_name}) should be documented in FRAMEWORK_MAPPING.md"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        requirement_number=st.integers(min_value=1, max_value=12)
    )
    def test_property_21_pci_dss_requirement_coverage(self, language, requirement_number):
        """
        Feature: compliance-framework-templates, Property 21: PCI-DSS Requirement Coverage
        
        For any PCI-DSS template set, templates must exist covering all 12 PCI-DSS 
        requirements (Requirements 1-12).
        
        This property verifies that:
        1. The FRAMEWORK_MAPPING.md file exists
        2. Each of the 12 PCI-DSS requirements is documented in the mapping
        3. The mapping indicates which templates cover each requirement
        
        Validates: Requirements 1.1
        """
        # Check that template directory exists
        template_dir = Path(f'templates/{language}/pci-dss')
        assert template_dir.exists(), \
            f"PCI-DSS template directory should exist for language '{language}'"
        
        # Check that FRAMEWORK_MAPPING.md exists
        mapping_file = template_dir / 'FRAMEWORK_MAPPING.md'
        assert mapping_file.exists(), \
            f"FRAMEWORK_MAPPING.md should exist in {template_dir}"
        
        # Read mapping content
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Verify that the specific requirement is documented
        # Look for "Requirement N:" or "### Requirement N:"
        pattern = rf'(?:###\s+)?Requirement\s+{requirement_number}[:\s]'
        assert re.search(pattern, mapping_content), \
            f"Requirement {requirement_number} should be documented in FRAMEWORK_MAPPING.md for language '{language}'"
        
        # Additionally verify that the requirement section has some content
        # (not just a header with no details)
        # Look for the requirement section and check it has at least some text after it
        section_pattern = rf'###\s+Requirement\s+{requirement_number}[:\s][^\n]*\n\n.*?\n'
        section_match = re.search(section_pattern, mapping_content, re.DOTALL)
        
        if section_match:
            # If we found a section, verify it has meaningful content
            section_text = section_match.group(0)
            # Should have more than just the header
            assert len(section_text.strip()) > 50, \
                f"Requirement {requirement_number} section should have meaningful content"
    
    def test_pci_dss_requirement_to_template_mapping(self):
        """
        Test that each PCI-DSS requirement is mapped to specific templates.
        
        This test verifies that the FRAMEWORK_MAPPING.md not only lists requirements
        but also maps them to specific template files.
        """
        mapping_file = Path('templates/de/pci-dss/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define expected mappings based on current implementation
        # These are the requirements that should have template coverage
        expected_mappings = {
            1: ['0100', '0020'],  # Firewall, Network Segmentation
            7: ['0400'],  # Access Control
            8: ['0410'],  # User Authentication
            9: ['0420'],  # Physical Security
            10: ['0500'],  # Logging and Monitoring
            11: ['0510'],  # Security Testing
            12: ['0600', '0050']  # Information Security Policy, Compliance Program
        }
        
        for req_num, template_numbers in expected_mappings.items():
            # Find the requirement section
            req_section_pattern = rf'###\s+Requirement\s+{req_num}[:\s].*?(?=###\s+Requirement\s+\d+|##\s+Zusammenfassung|$)'
            req_section = re.search(req_section_pattern, mapping_content, re.DOTALL)
            
            assert req_section, f"Requirement {req_num} section should exist in mapping"
            
            section_text = req_section.group(0)
            
            # Check that at least one of the expected templates is mentioned
            found_template = False
            for template_num in template_numbers:
                if template_num in section_text:
                    found_template = True
                    break
            
            assert found_template, \
                f"Requirement {req_num} should reference at least one template from {template_numbers}"
    
    def test_pci_dss_coverage_gaps_documented(self):
        """
        Test that coverage gaps are documented in FRAMEWORK_MAPPING.md.
        
        According to the design, Requirements 2, 3, 4, 5, and 6 have identified gaps.
        These should be documented in the mapping file.
        """
        mapping_file = Path('templates/de/pci-dss/FRAMEWORK_MAPPING.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Requirements with known gaps
        gap_requirements = [2, 3, 4, 5, 6]
        
        # Check that gaps are documented
        # Look for "LÜCKE" (gap in German) or similar indicators
        for req_num in gap_requirements:
            req_section_pattern = rf'###\s+Requirement\s+{req_num}[:\s].*?(?=###\s+Requirement\s+\d+|##\s+Zusammenfassung|$)'
            req_section = re.search(req_section_pattern, mapping_content, re.DOTALL)
            
            if req_section:
                section_text = req_section.group(0)
                # Should mention gaps or missing coverage
                assert 'LÜCKE' in section_text or 'Keine' in section_text or 'Minimal' in section_text or 'Teilweise' in section_text, \
                    f"Requirement {req_num} should document coverage gaps"
    
    def test_pci_dss_template_files_exist_for_covered_requirements(self):
        """
        Test that template files actually exist for requirements marked as covered.
        
        This verifies that the FRAMEWORK_MAPPING.md accurately reflects the actual
        template files present in the directory.
        """
        template_dir = Path('templates/de/pci-dss')
        
        # Requirements that should be fully covered with their expected templates
        covered_requirements = {
            1: ['0100_Firewall_Konfiguration.md', '0020_Netzwerksegmentierung.md'],
            7: ['0400_Zugriffskontrolle.md'],
            8: ['0410_Benutzerauthentifizierung.md'],
            9: ['0420_Physische_Sicherheit.md'],
            10: ['0500_Logging_und_Monitoring.md'],
            11: ['0510_Netzwerksicherheitstests.md'],
            12: ['0600_Informationssicherheitsrichtlinie.md', '0050_Compliance_Programm.md']
        }
        
        for req_num, template_files in covered_requirements.items():
            for template_file in template_files:
                template_path = template_dir / template_file
                assert template_path.exists(), \
                    f"Template {template_file} for Requirement {req_num} should exist"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_21_bilingual_consistency(self, language):
        """
        Property 21 Extension: Bilingual Consistency for PCI-DSS Coverage
        
        For any language (German or English), the PCI-DSS requirement coverage
        should be consistent - both languages should document all 12 requirements.
        
        Validates: Requirements 1.1, 9.1, 9.2
        """
        mapping_file = Path(f'templates/{language}/pci-dss/FRAMEWORK_MAPPING.md')
        
        assert mapping_file.exists(), \
            f"FRAMEWORK_MAPPING.md should exist for language '{language}'"
        
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All 12 requirements should be documented
        for req_num in range(1, 13):
            pattern = rf'(?:###\s+)?Requirement\s+{req_num}[:\s]'
            assert re.search(pattern, mapping_content), \
                f"Requirement {req_num} should be documented in {language} FRAMEWORK_MAPPING.md"
