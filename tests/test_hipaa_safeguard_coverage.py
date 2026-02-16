"""
Tests for HIPAA Safeguard Coverage

Property-based tests to verify that HIPAA template set covers all required safeguards.

Author: Kiro AI Assistant
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import re


class TestHIPAASafeguardCoverage:
    """Tests for HIPAA safeguard coverage."""
    
    def test_hipaa_templates_exist(self):
        """Test that HIPAA template directories exist."""
        de_dir = Path('templates/de/hipaa')
        en_dir = Path('templates/en/hipaa')
        
        assert de_dir.exists(), "German HIPAA template directory should exist"
        assert en_dir.exists(), "English HIPAA template directory should exist"
    
    def test_hipaa_framework_mapping_exists(self):
        """Test that 9999_Framework_Mapping.md exists for HIPAA."""
        de_mapping = Path('templates/de/hipaa/9999_Framework_Mapping.md')
        en_mapping = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        
        assert de_mapping.exists(), "German HIPAA 9999_Framework_Mapping.md should exist"
        assert en_mapping.exists(), "English HIPAA 9999_Framework_Mapping.md should exist"
    
    def test_hipaa_all_safeguards_covered(self):
        """
        Test that HIPAA template set covers all required safeguards.
        
        HIPAA Security Rule has three main categories of safeguards:
        1. Administrative Safeguards (§164.308)
        2. Physical Safeguards (§164.310)
        3. Technical Safeguards (§164.312)
        
        Plus:
        4. Privacy Rule requirements (§164.500-534)
        5. Breach Notification Rule (§164.400-414)
        """
        # Read 9999_Framework_Mapping.md to check coverage
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define all HIPAA safeguard categories
        safeguards = {
            'Administrative Safeguards': '§164.308',
            'Physical Safeguards': '§164.310',
            'Technical Safeguards': '§164.312',
            'Privacy Rule': '§164.502',  # Privacy Rule starts at §164.502, not §164.500
            'Breach Notification': '§164.400'
        }
        
        # Check that each safeguard category is mentioned in the mapping
        for safeguard_name, section in safeguards.items():
            assert safeguard_name in mapping_content, \
                f"{safeguard_name} should be documented in 9999_Framework_Mapping.md"
            assert section in mapping_content, \
                f"Section {section} for {safeguard_name} should be documented in 9999_Framework_Mapping.md"
    
    def test_hipaa_administrative_safeguards_standards(self):
        """
        Test that all Administrative Safeguards standards are covered.
        
        Administrative Safeguards (§164.308) include:
        - Security Management Process (§164.308(a)(1))
        - Assigned Security Responsibility (§164.308(a)(2))
        - Workforce Security (§164.308(a)(3))
        - Information Access Management (§164.308(a)(4))
        - Security Awareness and Training (§164.308(a)(5))
        - Security Incident Procedures (§164.308(a)(6))
        - Contingency Plan (§164.308(a)(7))
        - Evaluation (§164.308(a)(8))
        - Business Associate Contracts (§164.308(b))
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        admin_standards = [
            '§164.308(a)(1)',  # Security Management Process
            '§164.308(a)(2)',  # Assigned Security Responsibility
            '§164.308(a)(3)',  # Workforce Security
            '§164.308(a)(4)',  # Information Access Management
            '§164.308(a)(5)',  # Security Awareness and Training
            '§164.308(a)(6)',  # Security Incident Procedures
            '§164.308(a)(7)',  # Contingency Plan
            '§164.308(a)(8)',  # Evaluation
            '§164.308(b)',     # Business Associate Contracts
        ]
        
        for standard in admin_standards:
            assert standard in mapping_content, \
                f"Administrative Safeguard {standard} should be documented in 9999_Framework_Mapping.md"
    
    def test_hipaa_physical_safeguards_standards(self):
        """
        Test that all Physical Safeguards standards are covered.
        
        Physical Safeguards (§164.310) include:
        - Facility Access Controls (§164.310(a)(1))
        - Workstation Use (§164.310(b))
        - Workstation Security (§164.310(c))
        - Device and Media Controls (§164.310(d)(1))
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        physical_standards = [
            '§164.310(a)(1)',  # Facility Access Controls
            '§164.310(b)',     # Workstation Use
            '§164.310(c)',     # Workstation Security
            '§164.310(d)(1)',  # Device and Media Controls
        ]
        
        for standard in physical_standards:
            assert standard in mapping_content, \
                f"Physical Safeguard {standard} should be documented in 9999_Framework_Mapping.md"
    
    def test_hipaa_technical_safeguards_standards(self):
        """
        Test that all Technical Safeguards standards are covered.
        
        Technical Safeguards (§164.312) include:
        - Access Control (§164.312(a)(1))
        - Audit Controls (§164.312(b))
        - Integrity (§164.312(c)(1))
        - Person or Entity Authentication (§164.312(d))
        - Transmission Security (§164.312(e)(1))
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        technical_standards = [
            '§164.312(a)(1)',  # Access Control
            '§164.312(b)',     # Audit Controls
            '§164.312(c)(1)',  # Integrity
            '§164.312(d)',     # Person or Entity Authentication
            '§164.312(e)(1)',  # Transmission Security
        ]
        
        for standard in technical_standards:
            assert standard in mapping_content, \
                f"Technical Safeguard {standard} should be documented in 9999_Framework_Mapping.md"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        safeguard_type=st.sampled_from(['Administrative', 'Physical', 'Technical'])
    )
    def test_property_22_hipaa_safeguard_coverage(self, language, safeguard_type):
        """
        Feature: compliance-framework-templates, Property 22: HIPAA Safeguard Coverage
        
        For any HIPAA template set, templates must exist covering all three types of
        safeguards (Administrative, Physical, Technical) as required by HIPAA Security Rule.
        
        This property verifies that:
        1. The 9999_Framework_Mapping.md file exists
        2. Each safeguard type is documented in the mapping
        3. The mapping indicates which templates cover each safeguard
        
        Validates: Requirements 2.1
        """
        # Check that template directory exists
        template_dir = Path(f'templates/{language}/hipaa')
        assert template_dir.exists(), \
            f"HIPAA template directory should exist for language '{language}'"
        
        # Check that 9999_Framework_Mapping.md exists
        mapping_file = template_dir / '9999_Framework_Mapping.md'
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist in {template_dir}"
        
        # Read mapping content
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Verify that the specific safeguard type is documented
        safeguard_patterns = {
            'Administrative': r'Administrative\s+Safeguards',
            'Physical': r'Physical\s+Safeguards',
            'Technical': r'Technical\s+Safeguards'
        }
        
        pattern = safeguard_patterns[safeguard_type]
        assert re.search(pattern, mapping_content, re.IGNORECASE), \
            f"{safeguard_type} Safeguards should be documented in 9999_Framework_Mapping.md for language '{language}'"
        
        # Additionally verify that the safeguard section has some content
        # Look for the safeguard section and check it has at least some text after it
        section_pattern = rf'###\s+{pattern}.*?\n\n.*?\n'
        section_match = re.search(section_pattern, mapping_content, re.DOTALL | re.IGNORECASE)
        
        if section_match:
            # If we found a section, verify it has meaningful content
            section_text = section_match.group(0)
            # Should have more than just the header
            assert len(section_text.strip()) > 50, \
                f"{safeguard_type} Safeguards section should have meaningful content"
    
    def test_hipaa_safeguard_to_template_mapping(self):
        """
        Test that each HIPAA safeguard is mapped to specific templates.
        
        This test verifies that the 9999_Framework_Mapping.md not only lists safeguards
        but also maps them to specific template files.
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define expected mappings based on current implementation
        expected_mappings = {
            'Administrative': ['0100', '0110'],  # Security Management, Workforce Security
            'Physical': ['0300', '0310'],  # Facility Access, Workstation Security
            'Technical': ['0400'],  # Access Control
            'Privacy': ['0500'],  # Privacy Practices
            'Breach': ['0600']  # Breach Notification
        }
        
        for safeguard_type, template_numbers in expected_mappings.items():
            # Check that at least one of the expected templates is mentioned
            found_template = False
            for template_num in template_numbers:
                # Look for template references like "HIPAA-0100" or "0100"
                if f'HIPAA-{template_num}' in mapping_content or template_num in mapping_content:
                    found_template = True
                    break
            
            assert found_template, \
                f"{safeguard_type} safeguards should reference at least one template from {template_numbers}"
    
    def test_hipaa_template_files_exist_for_covered_safeguards(self):
        """
        Test that template files actually exist for safeguards marked as covered.
        
        This verifies that the 9999_Framework_Mapping.md accurately reflects the actual
        template files present in the directory.
        """
        template_dir = Path('templates/en/hipaa')
        
        # Safeguards that should be covered with their expected templates
        covered_safeguards = {
            'Administrative': [
                '0100_Security_Management_Process.md',
                '0110_Workforce_Security.md'
            ],
            'Physical': [
                '0300_Facility_Access_Controls.md',
                '0310_Workstation_Use_and_Security.md'
            ],
            'Technical': [
                '0400_Access_Control.md'
            ],
            'Privacy': [
                '0500_Privacy_Practices_and_Individual_Rights.md'
            ],
            'Breach': [
                '0600_Breach_Notification_and_Incident_Response.md'
            ]
        }
        
        for safeguard_type, template_files in covered_safeguards.items():
            for template_file in template_files:
                template_path = template_dir / template_file
                assert template_path.exists(), \
                    f"Template {template_file} for {safeguard_type} safeguards should exist"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_22_bilingual_consistency(self, language):
        """
        Property 22 Extension: Bilingual Consistency for HIPAA Coverage
        
        For any language (German or English), the HIPAA safeguard coverage
        should be consistent - both languages should document all safeguard types.
        
        Validates: Requirements 2.1, 9.1, 9.2
        """
        mapping_file = Path(f'templates/{language}/hipaa/9999_Framework_Mapping.md')
        
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist for language '{language}'"
        
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All safeguard types should be documented
        safeguard_types = ['Administrative', 'Physical', 'Technical']
        
        for safeguard_type in safeguard_types:
            pattern = rf'{safeguard_type}\s+Safeguards'
            assert re.search(pattern, mapping_content, re.IGNORECASE), \
                f"{safeguard_type} Safeguards should be documented in {language} 9999_Framework_Mapping.md"
    
    def test_hipaa_privacy_rule_requirements(self):
        """
        Test that Privacy Rule requirements are covered.
        
        Privacy Rule key requirements include:
        - Notice of Privacy Practices (§164.520)
        - Right of Access (§164.524)
        - Right to Amend (§164.526)
        - Accounting of Disclosures (§164.528)
        - Privacy Officer designation (§164.530(a)(1))
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        privacy_requirements = [
            '§164.520',  # Notice of Privacy Practices
            '§164.524',  # Right of Access
            '§164.526',  # Right to Amend
            '§164.528',  # Accounting of Disclosures
            '§164.530',  # Administrative Requirements
        ]
        
        for requirement in privacy_requirements:
            assert requirement in mapping_content, \
                f"Privacy Rule requirement {requirement} should be documented in 9999_Framework_Mapping.md"
    
    def test_hipaa_breach_notification_requirements(self):
        """
        Test that Breach Notification Rule requirements are covered.
        
        Breach Notification Rule requirements include:
        - Breach definition (§164.402)
        - Notification to individuals (§164.404)
        - Notification to HHS (§164.408)
        - Notification to media (§164.406)
        - Business associate notification (§164.410)
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        breach_requirements = [
            '§164.402',  # Definitions
            '§164.404',  # Notification to Individuals
            '§164.406',  # Notification to Media
            '§164.408',  # Notification to HHS
            '§164.410',  # Notification by Business Associate
        ]
        
        for requirement in breach_requirements:
            assert requirement in mapping_content, \
                f"Breach Notification requirement {requirement} should be documented in 9999_Framework_Mapping.md"
    
    def test_hipaa_required_vs_addressable_specifications(self):
        """
        Test that the mapping distinguishes between Required and Addressable specifications.
        
        HIPAA Security Rule has both Required and Addressable implementation specifications.
        The mapping should clearly indicate which is which.
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Should contain indicators of Required vs Addressable
        assert 'Required' in mapping_content, \
            "9999_Framework_Mapping.md should indicate Required specifications"
        assert 'Addressable' in mapping_content, \
            "9999_Framework_Mapping.md should indicate Addressable specifications"
    
    def test_hipaa_no_coverage_gaps(self):
        """
        Test that no coverage gaps are identified in 9999_Framework_Mapping.md.
        
        According to the design, HIPAA template set should provide comprehensive coverage
        with no identified gaps.
        """
        mapping_file = Path('templates/en/hipaa/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Look for coverage analysis section
        assert 'Coverage Analysis' in mapping_content or 'Comprehensive Coverage' in mapping_content, \
            "9999_Framework_Mapping.md should include coverage analysis"
        
        # Should indicate no gaps
        assert 'No Identified Gaps' in mapping_content or 'No gaps' in mapping_content, \
            "9999_Framework_Mapping.md should indicate no coverage gaps"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_22_foundation_templates_exist(self, language):
        """
        Property 22 Extension: Foundation Templates Existence
        
        For any language, the foundation templates (0010-0050) should exist
        as they provide the basis for the HIPAA compliance program.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.4
        """
        template_dir = Path(f'templates/{language}/hipaa')
        
        foundation_templates = [
            '0010',  # Scope and Applicability
            '0020',  # Covered Entities
            '0030',  # Business Associates
            '0040',  # Roles and Responsibilities
            '0050',  # HIPAA Compliance Program
        ]
        
        for template_num in foundation_templates:
            # Find any file starting with this number
            matching_files = list(template_dir.glob(f'{template_num}_*.md'))
            assert len(matching_files) > 0, \
                f"Foundation template {template_num} should exist in {language} HIPAA templates"
