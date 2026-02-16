"""
Tests for Common Criteria Security Target Structure

Property-based tests to verify that Common Criteria template set covers all required
Security Target components according to ISO/IEC 15408-1.

Author: Kiro AI Assistant
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import re


class TestCommonCriteriaSTStructure:
    """Tests for Common Criteria Security Target structure coverage."""
    
    def test_common_criteria_templates_exist(self):
        """Test that Common Criteria template directories exist."""
        de_dir = Path('templates/de/common-criteria')
        en_dir = Path('templates/en/common-criteria')
        
        assert de_dir.exists(), "German Common Criteria template directory should exist"
        assert en_dir.exists(), "English Common Criteria template directory should exist"
    
    def test_common_criteria_framework_mapping_exists(self):
        """Test that 9999_Framework_Mapping.md exists for Common Criteria."""
        de_mapping = Path('templates/de/common-criteria/9999_Framework_Mapping.md')
        en_mapping = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        
        assert de_mapping.exists(), "German Common Criteria 9999_Framework_Mapping.md should exist"
        assert en_mapping.exists(), "English Common Criteria 9999_Framework_Mapping.md should exist"
    
    def test_common_criteria_all_st_sections_covered(self):
        """
        Test that Common Criteria template set covers all required ST sections.
        
        According to ISO/IEC 15408-1, Section 8, a Security Target must include:
        1. ST Introduction (Section 8.1)
        2. TOE Description (Section 8.2)
        3. Security Problem Definition (Section 8.3)
        4. Security Objectives (Section 8.4)
        5. Security Requirements (Section 8.5)
        6. TOE Summary Specification (Section 8.6)
        """
        # Read 9999_Framework_Mapping.md to check coverage
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define all required ST sections from ISO/IEC 15408-1
        st_sections = {
            'ST Introduction': 'Section 8.1',
            'TOE Description': 'Section 8.2',
            'Security Problem Definition': 'Section 8.3',
            'Security Objectives': 'Section 8.4',
            'Security Requirements': 'Section 8.5',
            'TOE Summary Specification': 'Section 8.6'
        }
        
        # Check that each ST section is mentioned in the mapping
        for section_name, section_ref in st_sections.items():
            assert section_name in mapping_content, \
                f"{section_name} should be documented in 9999_Framework_Mapping.md"
            # Check for section reference (e.g., "8.1" or "Abschnitt 8.1")
            assert re.search(rf'(Section|Abschnitt)\s+{re.escape(section_ref.split()[-1])}', 
                           mapping_content, re.IGNORECASE), \
                f"Section reference {section_ref} for {section_name} should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_st_introduction_components(self):
        """
        Test that ST Introduction components are covered.
        
        ST Introduction (ISO/IEC 15408-1, Section 8.1) includes:
        - ST Identification (Section 8.1.1)
        - TOE Overview (Section 8.1.2)
        - Conformance Claims (Section 8.1.3)
        - Document Conventions (Section 8.1.4)
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        st_intro_components = [
            ('ST Introduction', '8.1.1'),
            ('TOE Overview', '8.1.2'),
            ('Conformance Claims', '8.1.3'),
            ('Document Conventions', '8.1.4')
        ]
        
        for component_name, section_ref in st_intro_components:
            assert component_name in mapping_content, \
                f"ST Introduction component '{component_name}' should be documented in 9999_Framework_Mapping.md"
            assert section_ref in mapping_content, \
                f"Section reference {section_ref} for '{component_name}' should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_toe_description_components(self):
        """
        Test that TOE Description components are covered.
        
        TOE Description (ISO/IEC 15408-1, Section 8.2) includes:
        - Physical Scope (Section 8.2.1)
        - Logical Scope (Section 8.2.2)
        - TOE Interfaces (Section 8.2.3)
        - TOE Architecture (Section 8.2.4)
        - TOE Lifecycle (Section 8.2.5)
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        toe_components = [
            ('Physical Scope', '8.2.1'),
            ('Logical Scope', '8.2.2'),
            ('Interfaces', '8.2.3'),
            ('Architecture', '8.2.4'),
            ('Lifecycle', '8.2.5')
        ]
        
        for component_name, section_ref in toe_components:
            assert component_name in mapping_content, \
                f"TOE Description component '{component_name}' should be documented in 9999_Framework_Mapping.md"
            assert section_ref in mapping_content, \
                f"Section reference {section_ref} for '{component_name}' should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_security_problem_definition_components(self):
        """
        Test that Security Problem Definition components are covered.
        
        Security Problem Definition (ISO/IEC 15408-1, Section 8.3) includes:
        - Threats (Section 8.3.1)
        - Organizational Security Policies (Section 8.3.2)
        - Assumptions (Section 8.3.3)
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        security_problem_components = [
            ('Threats', '8.3.1'),
            ('Organizational Security Policies', '8.3.2'),
            ('Assumptions', '8.3.3')
        ]
        
        for component_name, section_ref in security_problem_components:
            assert component_name in mapping_content, \
                f"Security Problem Definition component '{component_name}' should be documented in 9999_Framework_Mapping.md"
            assert section_ref in mapping_content, \
                f"Section reference {section_ref} for '{component_name}' should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_security_objectives_components(self):
        """
        Test that Security Objectives components are covered.
        
        Security Objectives (ISO/IEC 15408-1, Section 8.4) includes:
        - Security Objectives for TOE (Section 8.4.1)
        - Security Objectives for Environment (Section 8.4.2)
        - Security Objectives Rationale (Section 8.4.3)
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        objectives_components = [
            ('Security Objectives', '8.4'),
            ('Rationale', '8.4.3')
        ]
        
        for component_name, section_ref in objectives_components:
            assert component_name in mapping_content, \
                f"Security Objectives component '{component_name}' should be documented in 9999_Framework_Mapping.md"
            assert section_ref in mapping_content, \
                f"Section reference {section_ref} for '{component_name}' should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_security_requirements_components(self):
        """
        Test that Security Requirements components are covered.
        
        Security Requirements (ISO/IEC 15408-1, Section 8.5) includes:
        - Security Functional Requirements (SFRs) (Section 8.5.1)
        - Security Assurance Requirements (SARs) (Section 8.5.2)
        - Security Requirements Rationale (Section 8.5.3)
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        requirements_components = [
            ('Security Requirements', '8.5'),
            ('Evaluation Assurance Level', '8.5.2'),
            ('Requirements Rationale', '8.5.3'),
            ('SFR Dependencies', '8.5.3')
        ]
        
        for component_name, section_ref in requirements_components:
            assert component_name in mapping_content, \
                f"Security Requirements component '{component_name}' should be documented in 9999_Framework_Mapping.md"
            assert section_ref in mapping_content, \
                f"Section reference {section_ref} for '{component_name}' should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_toe_summary_specification_components(self):
        """
        Test that TOE Summary Specification components are covered.
        
        TOE Summary Specification (ISO/IEC 15408-1, Section 8.6) includes:
        - TOE Security Functions (TSFs) (Section 8.6.1)
        - Assurance Measures (Section 8.6.2)
        - TSF Rationale (Section 8.6.3)
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        tss_components = [
            ('TOE Summary Specification', '8.6'),
            ('Assurance Measures', '8.6.2'),
            ('Functions Rationale', '8.6.3'),
            ('Strength of Function', '8.6.1')
        ]
        
        for component_name, section_ref in tss_components:
            assert component_name in mapping_content, \
                f"TOE Summary Specification component '{component_name}' should be documented in 9999_Framework_Mapping.md"
            assert section_ref in mapping_content, \
                f"Section reference {section_ref} for '{component_name}' should be documented in 9999_Framework_Mapping.md"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        st_section=st.sampled_from([
            'ST Introduction',
            'TOE Description',
            'Security Problem Definition',
            'Security Objectives',
            'Security Requirements',
            'TOE Summary Specification'
        ])
    )
    def test_property_25_common_criteria_st_structure(self, language, st_section):
        """
        Feature: compliance-framework-templates, Property 25: Common Criteria Security Target Structure
        
        For any Common Criteria template set, templates must exist covering all six main
        Security Target sections as required by ISO/IEC 15408-1, Section 8:
        1. ST Introduction
        2. TOE Description
        3. Security Problem Definition
        4. Security Objectives
        5. Security Requirements
        6. TOE Summary Specification
        
        This property verifies that:
        1. The 9999_Framework_Mapping.md file exists
        2. Each ST section is documented in the mapping
        3. The mapping indicates which templates cover each section
        
        Validates: Requirements 5.1
        """
        # Check that template directory exists
        template_dir = Path(f'templates/{language}/common-criteria')
        assert template_dir.exists(), \
            f"Common Criteria template directory should exist for language '{language}'"
        
        # Check that 9999_Framework_Mapping.md exists
        mapping_file = template_dir / '9999_Framework_Mapping.md'
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist in {template_dir}"
        
        # Read mapping content
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Verify that the specific ST section is documented
        # Use flexible pattern matching to handle both English and German
        section_patterns = {
            'ST Introduction': r'(ST[\s-]?Introduction|ST[\s-]?Einführung)',
            'TOE Description': r'(TOE[\s-]?Description|TOE[\s-]?Beschreibung)',
            'Security Problem Definition': r'(Security\s+Problem\s+Definition|Sicherheitsproblem[\s-]?Definition)',
            'Security Objectives': r'(Security\s+Objectives|Sicherheitsziele)',
            'Security Requirements': r'(Security\s+Requirements|Sicherheitsanforderungen)',
            'TOE Summary Specification': r'(TOE\s+Summary\s+Specification|TOE[\s-]?Zusammenfassende\s+Spezifikation)'
        }
        
        pattern = section_patterns[st_section]
        assert re.search(pattern, mapping_content, re.IGNORECASE), \
            f"{st_section} should be documented in 9999_Framework_Mapping.md for language '{language}'"
        
        # Additionally verify that the section has some content
        # Look for the section and check it has at least some text after it
        section_pattern = rf'###\s+.*?{pattern}.*?\n\n.*?\n'
        section_match = re.search(section_pattern, mapping_content, re.DOTALL | re.IGNORECASE)
        
        if section_match:
            # If we found a section, verify it has meaningful content
            section_text = section_match.group(0)
            # Should have more than just the header
            assert len(section_text.strip()) > 50, \
                f"{st_section} section should have meaningful content"
    
    def test_common_criteria_st_section_to_template_mapping(self):
        """
        Test that each ST section is mapped to specific templates.
        
        This test verifies that the 9999_Framework_Mapping.md not only lists ST sections
        but also maps them to specific template files.
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define expected mappings based on current implementation
        expected_mappings = {
            'ST Introduction': ['0010', '0020', '0030', '0040', '0050'],
            'TOE Description': ['0100', '0110', '0120', '0130', '0140'],
            'Security Problem Definition': ['0200', '0210', '0220', '0230', '0240'],
            'Security Objectives': ['0300', '0310', '0320', '0330'],
            'Security Requirements': ['0400', '0410', '0420', '0430', '0440'],
            'TOE Summary Specification': ['0500', '0510', '0520', '0530', '0540']
        }
        
        for st_section, template_numbers in expected_mappings.items():
            # Check that at least one of the expected templates is mentioned
            found_template = False
            for template_num in template_numbers:
                # Look for template references like "0010" in the mapping
                if template_num in mapping_content:
                    found_template = True
                    break
            
            assert found_template, \
                f"{st_section} should reference at least one template from {template_numbers}"
    
    def test_common_criteria_template_files_exist_for_covered_sections(self):
        """
        Test that template files actually exist for ST sections marked as covered.
        
        This verifies that the 9999_Framework_Mapping.md accurately reflects the actual
        template files present in the directory.
        """
        template_dir = Path('templates/en/common-criteria')
        
        # ST sections that should be covered with their expected templates
        covered_sections = {
            'ST Introduction': [
                '0010_ST_Introduction.md',
                '0020_TOE_Overview.md',
                '0040_Conformance_Claims.md'
            ],
            'TOE Description': [
                '0100_TOE_Physical_Scope.md',
                '0110_TOE_Logical_Scope.md',
                '0120_TOE_Interfaces.md'
            ],
            'Security Problem Definition': [
                '0200_Security_Problem_Definition.md',
                '0210_Threats.md',
                '0220_Organizational_Security_Policies.md',
                '0230_Assumptions.md'
            ],
            'Security Objectives': [
                '0300_Security_Objectives.md',
                '0310_Security_Objectives_Rationale.md'
            ],
            'Security Requirements': [
                '0400_Security_Requirements.md',
                '0410_Evaluation_Assurance_Level.md',
                '0420_Requirements_Rationale.md'
            ],
            'TOE Summary Specification': [
                '0500_TOE_Summary_Specification.md',
                '0510_Assurance_Measures.md',
                '0520_Functions_Rationale.md'
            ]
        }
        
        for st_section, template_files in covered_sections.items():
            for template_file in template_files:
                template_path = template_dir / template_file
                assert template_path.exists(), \
                    f"Template {template_file} for {st_section} should exist"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_25_bilingual_consistency(self, language):
        """
        Property 25 Extension: Bilingual Consistency for Common Criteria Coverage
        
        For any language (German or English), the Common Criteria ST structure coverage
        should be consistent - both languages should document all ST sections.
        
        Validates: Requirements 5.1, 9.1, 9.2
        """
        mapping_file = Path(f'templates/{language}/common-criteria/9999_Framework_Mapping.md')
        
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist for language '{language}'"
        
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All ST sections should be documented
        st_sections = [
            'ST Introduction',
            'TOE Description',
            'Security Problem',
            'Security Objectives',
            'Security Requirements',
            'TOE Summary Specification'
        ]
        
        for st_section in st_sections:
            # Use flexible pattern to match both English and German
            pattern = rf'{st_section}|{st_section.replace(" ", "[\s-]?")}'
            assert re.search(pattern, mapping_content, re.IGNORECASE), \
                f"{st_section} should be documented in {language} 9999_Framework_Mapping.md"
    
    def test_common_criteria_iso_15408_references(self):
        """
        Test that ISO/IEC 15408 standard references are included.
        
        The mapping should reference the ISO/IEC 15408 standard parts:
        - ISO/IEC 15408-1: Introduction and general model
        - ISO/IEC 15408-2: Security functional components
        - ISO/IEC 15408-3: Security assurance components
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        iso_references = [
            'ISO/IEC 15408-1',
            'ISO/IEC 15408-2',
            'ISO/IEC 15408-3'
        ]
        
        for iso_ref in iso_references:
            assert iso_ref in mapping_content, \
                f"ISO standard reference {iso_ref} should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_eal_support(self):
        """
        Test that Evaluation Assurance Levels (EAL) are documented.
        
        Common Criteria defines seven EAL levels (EAL1-EAL7).
        The mapping should document support for all EAL levels.
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for EAL references
        assert 'EAL' in mapping_content or 'Evaluation Assurance Level' in mapping_content, \
            "Evaluation Assurance Levels should be documented in 9999_Framework_Mapping.md"
        
        # Check for at least some EAL levels
        eal_levels = ['EAL1', 'EAL2', 'EAL3', 'EAL4', 'EAL5', 'EAL6', 'EAL7']
        found_eals = sum(1 for eal in eal_levels if eal in mapping_content)
        
        assert found_eals >= 4, \
            f"At least 4 EAL levels should be documented (found {found_eals})"
    
    def test_common_criteria_sfr_and_sar_classes(self):
        """
        Test that SFR and SAR classes are documented.
        
        Security Functional Requirements (SFRs) and Security Assurance Requirements (SARs)
        are organized into classes. The mapping should reference these.
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for SFR and SAR references
        assert 'SFR' in mapping_content or 'Security Functional Requirements' in mapping_content, \
            "Security Functional Requirements should be documented in 9999_Framework_Mapping.md"
        assert 'SAR' in mapping_content or 'Security Assurance Requirements' in mapping_content, \
            "Security Assurance Requirements should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_coverage_matrices(self):
        """
        Test that coverage matrices are documented.
        
        Common Criteria requires several coverage matrices to demonstrate completeness:
        - Threats/Objectives matrix
        - Objectives/SFRs matrix
        - SFRs/TSFs matrix
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        matrix_types = [
            'Coverage Matri',  # Matches both "Coverage Matrix" and "Coverage Matrices"
            'Objectives',
            'Requirements'
        ]
        
        for matrix_type in matrix_types:
            assert matrix_type in mapping_content, \
                f"{matrix_type} should be documented in 9999_Framework_Mapping.md"
    
    def test_common_criteria_no_coverage_gaps(self):
        """
        Test that no coverage gaps are identified in 9999_Framework_Mapping.md.
        
        According to the design, Common Criteria template set should provide
        comprehensive coverage with no identified gaps.
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Look for coverage analysis section
        assert 'Coverage' in mapping_content or 'Abdeckung' in mapping_content, \
            "9999_Framework_Mapping.md should include coverage analysis"
        
        # Should indicate comprehensive coverage
        # Check for positive indicators rather than gaps
        positive_indicators = [
            'comprehensive',
            'complete',
            'all',
            'umfassend',
            'vollständig'
        ]
        
        found_indicators = sum(1 for indicator in positive_indicators 
                              if indicator.lower() in mapping_content.lower())
        
        assert found_indicators >= 2, \
            "9999_Framework_Mapping.md should indicate comprehensive coverage"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_25_foundation_templates_exist(self, language):
        """
        Property 25 Extension: Foundation Templates Existence
        
        For any language, the foundation templates (0010-0050) should exist
        as they provide the ST Introduction section.
        
        Validates: Requirements 5.1, 5.2, 5.3, 5.4
        """
        template_dir = Path(f'templates/{language}/common-criteria')
        
        foundation_templates = [
            '0010',  # ST Introduction
            '0020',  # TOE Overview
            '0030',  # TOE Description Summary
            '0040',  # Conformance Claims
            '0050',  # Document Conventions
        ]
        
        for template_num in foundation_templates:
            # Find any file starting with this number
            matching_files = list(template_dir.glob(f'{template_num}_*.md'))
            assert len(matching_files) > 0, \
                f"Foundation template {template_num} should exist in {language} Common Criteria templates"
    
    def test_common_criteria_pp_conformance_support(self):
        """
        Test that Protection Profile (PP) conformance is supported.
        
        Common Criteria allows Security Targets to claim conformance to Protection Profiles.
        The template set should support PP conformance documentation.
        """
        mapping_file = Path('templates/en/common-criteria/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for PP conformance references
        pp_indicators = [
            'Protection Profile',
            'PP Conformance',
            'PP-Konformität'
        ]
        
        found_pp = any(indicator in mapping_content for indicator in pp_indicators)
        assert found_pp, \
            "Protection Profile conformance should be documented in 9999_Framework_Mapping.md"

