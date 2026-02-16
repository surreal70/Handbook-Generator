"""
Tests for ISO 9001 Clause Coverage

Property-based tests to verify that ISO 9001 template set covers all required clauses.

Author: Kiro AI Assistant
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import re


class TestISO9001ClauseCoverage:
    """Tests for ISO 9001 clause coverage."""
    
    def test_iso_9001_templates_exist(self):
        """Test that ISO 9001 template directories exist."""
        de_dir = Path('templates/de/iso-9001')
        en_dir = Path('templates/en/iso-9001')
        
        assert de_dir.exists(), "German ISO 9001 template directory should exist"
        assert en_dir.exists(), "English ISO 9001 template directory should exist"
    
    def test_iso_9001_framework_mapping_exists(self):
        """Test that 9999_Framework_Mapping.md exists for ISO 9001."""
        de_mapping = Path('templates/de/iso-9001/9999_Framework_Mapping.md')
        en_mapping = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        
        assert de_mapping.exists(), "German ISO 9001 9999_Framework_Mapping.md should exist"
        assert en_mapping.exists(), "English ISO 9001 9999_Framework_Mapping.md should exist"
    
    def test_iso_9001_all_clauses_covered(self):
        """
        Test that ISO 9001 template set covers all required clauses.
        
        ISO 9001:2015 has 10 clauses, with clauses 4-10 containing the main requirements:
        - Clause 4: Context of the Organization
        - Clause 5: Leadership
        - Clause 6: Planning
        - Clause 7: Support
        - Clause 8: Operation
        - Clause 9: Performance Evaluation
        - Clause 10: Improvement
        """
        # Read 9999_Framework_Mapping.md to check coverage
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define all ISO 9001 clauses (4-10)
        clauses = {
            4: 'Context of the Organization',
            5: 'Leadership',
            6: 'Planning',
            7: 'Support',
            8: 'Operation',
            9: 'Performance Evaluation',
            10: 'Improvement'
        }
        
        # Check that each clause is mentioned in the mapping
        for clause_num, clause_name in clauses.items():
            # Look for "### Clause N:" or "Clause N:" pattern
            pattern = rf'###\s+Clause\s+{clause_num}[:\s]'
            assert re.search(pattern, mapping_content), \
                f"Clause {clause_num} ({clause_name}) should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_clause_4_components(self):
        """
        Test that all Clause 4 (Context of the Organization) components are covered.
        
        Clause 4 includes:
        - 4.1 Understanding the organization and its context
        - 4.2 Understanding the needs and expectations of interested parties
        - 4.3 Determining the scope of the QMS
        - 4.4 Quality management system and its processes
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        clause_4_components = [
            '4.1',  # Understanding the organization and its context
            '4.2',  # Understanding the needs and expectations of interested parties
            '4.3',  # Determining the scope of the QMS
            '4.4',  # Quality management system and its processes
        ]
        
        for component in clause_4_components:
            assert component in mapping_content, \
                f"Clause 4 component {component} should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_clause_5_components(self):
        """
        Test that all Clause 5 (Leadership) components are covered.
        
        Clause 5 includes:
        - 5.1 Leadership and commitment
        - 5.2 Policy
        - 5.3 Organizational roles, responsibilities and authorities
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        clause_5_components = [
            '5.1',  # Leadership and commitment
            '5.2',  # Policy
            '5.3',  # Organizational roles, responsibilities and authorities
        ]
        
        for component in clause_5_components:
            assert component in mapping_content, \
                f"Clause 5 component {component} should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_clause_6_components(self):
        """
        Test that all Clause 6 (Planning) components are covered.
        
        Clause 6 includes:
        - 6.1 Actions to address risks and opportunities
        - 6.2 Quality objectives and planning to achieve them
        - 6.3 Planning of changes
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        clause_6_components = [
            '6.1',  # Actions to address risks and opportunities
            '6.2',  # Quality objectives and planning to achieve them
            '6.3',  # Planning of changes
        ]
        
        for component in clause_6_components:
            assert component in mapping_content, \
                f"Clause 6 component {component} should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_clause_7_components(self):
        """
        Test that all Clause 7 (Support) components are covered.
        
        Clause 7 includes:
        - 7.1 Resources
        - 7.2 Competence
        - 7.3 Awareness
        - 7.4 Communication
        - 7.5 Documented information
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        clause_7_components = [
            '7.1',  # Resources
            '7.2',  # Competence
            '7.3',  # Awareness
            '7.4',  # Communication
            '7.5',  # Documented information
        ]
        
        for component in clause_7_components:
            assert component in mapping_content, \
                f"Clause 7 component {component} should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_clause_8_components(self):
        """
        Test that all Clause 8 (Operation) components are covered.
        
        Clause 8 includes:
        - 8.1 Operational planning and control
        - 8.2 Requirements for products and services
        - 8.3 Design and development of products and services
        - 8.4 Control of externally provided processes, products and services
        - 8.5 Production and service provision
        - 8.6 Release of products and services
        - 8.7 Control of nonconforming outputs
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        clause_8_components = [
            '8.1',  # Operational planning and control
            '8.2',  # Requirements for products and services
            '8.3',  # Design and development of products and services
            '8.4',  # Control of externally provided processes, products and services
            '8.5',  # Production and service provision
            '8.6',  # Release of products and services
            '8.7',  # Control of nonconforming outputs
        ]
        
        for component in clause_8_components:
            assert component in mapping_content, \
                f"Clause 8 component {component} should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_clause_9_components(self):
        """
        Test that all Clause 9 (Performance Evaluation) components are covered.
        
        Clause 9 includes:
        - 9.1 Monitoring, measurement, analysis and evaluation
        - 9.2 Internal audit
        - 9.3 Management review
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        clause_9_components = [
            '9.1',  # Monitoring, measurement, analysis and evaluation
            '9.2',  # Internal audit
            '9.3',  # Management review
        ]
        
        for component in clause_9_components:
            assert component in mapping_content, \
                f"Clause 9 component {component} should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_clause_10_components(self):
        """
        Test that all Clause 10 (Improvement) components are covered.
        
        Clause 10 includes:
        - 10.1 General
        - 10.2 Nonconformity and corrective action
        - 10.3 Continual improvement
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        clause_10_components = [
            '10.1',  # General
            '10.2',  # Nonconformity and corrective action
            '10.3',  # Continual improvement
        ]
        
        for component in clause_10_components:
            assert component in mapping_content, \
                f"Clause 10 component {component} should be documented in 9999_Framework_Mapping.md"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        clause_number=st.integers(min_value=4, max_value=10)
    )
    def test_property_26_iso_9001_clause_coverage(self, language, clause_number):
        """
        Feature: compliance-framework-templates, Property 26: ISO 9001 Clause Coverage
        
        For any ISO 9001 template set, templates must exist covering clauses 4-10
        (Context, Leadership, Planning, Support, Operation, Performance Evaluation, Improvement).
        
        This property verifies that:
        1. The 9999_Framework_Mapping.md file exists
        2. Each of the 7 main clauses (4-10) is documented in the mapping
        3. The mapping indicates which templates cover each clause
        
        Validates: Requirements 6.1
        """
        # Check that template directory exists
        template_dir = Path(f'templates/{language}/iso-9001')
        assert template_dir.exists(), \
            f"ISO 9001 template directory should exist for language '{language}'"
        
        # Check that 9999_Framework_Mapping.md exists
        mapping_file = template_dir / '9999_Framework_Mapping.md'
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist in {template_dir}"
        
        # Read mapping content
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Verify that the specific clause is documented
        # Look for "### Clause N:" or "### Kapitel N:" pattern (English/German)
        if language == 'de':
            pattern = rf'###\s+Kapitel\s+{clause_number}[:\s]'
        else:
            pattern = rf'###\s+Clause\s+{clause_number}[:\s]'
        
        assert re.search(pattern, mapping_content), \
            f"Clause {clause_number} should be documented in 9999_Framework_Mapping.md for language '{language}'"
        
        # Additionally verify that the clause section has some content
        # (not just a header with no details)
        # Look for the clause section and check it has at least some text after it
        if language == 'de':
            section_pattern = rf'###\s+Kapitel\s+{clause_number}[:\s][^\n]*\n\n.*?\n'
        else:
            section_pattern = rf'###\s+Clause\s+{clause_number}[:\s][^\n]*\n\n.*?\n'
        section_match = re.search(section_pattern, mapping_content, re.DOTALL)
        
        if section_match:
            # If we found a section, verify it has meaningful content
            section_text = section_match.group(0)
            # Should have more than just the header
            assert len(section_text.strip()) > 50, \
                f"Clause {clause_number} section should have meaningful content"
    
    def test_iso_9001_clause_to_template_mapping(self):
        """
        Test that each ISO 9001 clause is mapped to specific templates.
        
        This test verifies that the 9999_Framework_Mapping.md not only lists clauses
        but also maps them to specific template files.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define expected mappings based on current implementation
        expected_mappings = {
            4: ['0010', '0020', '0030', '0040', '0050'],  # Context
            5: ['0100', '0110', '0120'],  # Leadership
            6: ['0200', '0210', '0220'],  # Planning
            7: ['0300', '0310', '0320', '0330'],  # Support
            8: ['0400', '0410', '0420', '0430', '0440'],  # Operation
            9: ['0550', '0560', '0570'],  # Performance Evaluation
            10: ['0650', '0660']  # Improvement
        }
        
        for clause_num, template_numbers in expected_mappings.items():
            # Find the clause section
            clause_section_pattern = rf'###\s+Clause\s+{clause_num}[:\s].*?(?=###\s+Clause\s+\d+|##\s+Coverage|$)'
            clause_section = re.search(clause_section_pattern, mapping_content, re.DOTALL)
            
            assert clause_section, f"Clause {clause_num} section should exist in mapping"
            
            section_text = clause_section.group(0)
            
            # Check that at least one of the expected templates is mentioned
            found_template = False
            for template_num in template_numbers:
                if template_num in section_text:
                    found_template = True
                    break
            
            assert found_template, \
                f"Clause {clause_num} should reference at least one template from {template_numbers}"
    
    def test_iso_9001_coverage_analysis_documented(self):
        """
        Test that coverage analysis is documented in 9999_Framework_Mapping.md.
        
        The mapping should include a coverage analysis section showing complete coverage
        for all clauses.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for coverage analysis section
        assert '## Coverage Analysis' in mapping_content or '## Abdeckungsanalyse' in mapping_content, \
            "9999_Framework_Mapping.md should include a coverage analysis section"
        
        # Check that complete coverage is documented
        assert 'Complete Coverage' in mapping_content or 'Fully covered' in mapping_content or 'Vollständig' in mapping_content, \
            "Coverage analysis should show complete coverage"
    
    def test_iso_9001_template_files_exist_for_covered_clauses(self):
        """
        Test that template files actually exist for clauses marked as covered.
        
        This verifies that the 9999_Framework_Mapping.md accurately reflects the actual
        template files present in the directory.
        """
        template_dir = Path('templates/en/iso-9001')
        
        # Clauses that should be covered with their expected templates
        covered_clauses = {
            4: [
                '0010_Context_of_Organization.md',
                '0020_Interested_Parties.md',
                '0030_QMS_Scope.md',
                '0040_QMS_and_Processes.md',
                '0050_Process_Map.md'
            ],
            5: [
                '0100_Quality_Policy.md',
                '0110_Leadership_and_Commitment.md',
                '0120_Roles_Responsibilities_Authorities.md'
            ],
            6: [
                '0200_Risk_and_Opportunity_Assessment.md',
                '0210_Quality_Objectives.md',
                '0220_Planning_of_Changes.md'
            ],
            7: [
                '0300_Resources.md',
                '0310_Competence_Training_Awareness.md',
                '0320_Communication.md',
                '0330_Documented_Information.md'
            ],
            8: [
                '0400_Operational_Planning_and_Control.md',
                '0410_Requirements_for_Products_and_Services.md',
                '0420_Design_and_Development.md',
                '0430_Control_of_Externally_Provided_Processes_Products_Services.md',
                '0440_Production_and_Service_Provision.md'
            ],
            9: [
                '0550_Monitoring_Measurement_Analysis_Evaluation.md',
                '0560_Internal_Audit.md',
                '0570_Management_Review.md'
            ],
            10: [
                '0650_Improvement.md',
                '0660_Nonconformity_and_Corrective_Action.md'
            ]
        }
        
        for clause_num, template_files in covered_clauses.items():
            for template_file in template_files:
                template_path = template_dir / template_file
                assert template_path.exists(), \
                    f"Template {template_file} for Clause {clause_num} should exist"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_26_bilingual_consistency(self, language):
        """
        Property 26 Extension: Bilingual Consistency for ISO 9001 Coverage
        
        For any language (German or English), the ISO 9001 clause coverage
        should be consistent - both languages should document all clauses 4-10.
        
        Validates: Requirements 6.1, 9.1, 9.2
        """
        mapping_file = Path(f'templates/{language}/iso-9001/9999_Framework_Mapping.md')
        
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist for language '{language}'"
        
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All clauses 4-10 should be documented
        for clause_num in range(4, 11):
            # Use language-specific pattern (Clause for English, Kapitel for German)
            if language == 'de':
                pattern = rf'###\s+Kapitel\s+{clause_num}[:\s]'
            else:
                pattern = rf'###\s+Clause\s+{clause_num}[:\s]'
            
            assert re.search(pattern, mapping_content), \
                f"Clause {clause_num} should be documented in {language} 9999_Framework_Mapping.md"
    
    def test_iso_9001_no_coverage_gaps(self):
        """
        Test that no coverage gaps are identified in 9999_Framework_Mapping.md.
        
        According to the design, ISO 9001 template set should provide comprehensive
        coverage with no identified gaps.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Look for coverage gaps section
        assert 'Coverage Gaps' in mapping_content or 'Lücken' in mapping_content, \
            "9999_Framework_Mapping.md should include coverage gaps section"
        
        # Should indicate no gaps
        assert 'No gaps identified' in mapping_content or 'Keine Lücken' in mapping_content, \
            "9999_Framework_Mapping.md should indicate no coverage gaps"
    
    def test_iso_9001_foundation_templates_exist(self):
        """
        Test that foundation templates (0010-0050) exist for ISO 9001.
        
        These are critical templates that should be present for Clause 4 (Context).
        """
        foundation_templates = [
            '0010_Context_of_Organization.md',
            '0020_Interested_Parties.md',
            '0030_QMS_Scope.md',
            '0040_QMS_and_Processes.md',
            '0050_Process_Map.md'
        ]
        
        template_dir = Path('templates/en/iso-9001')
        
        for template_file in foundation_templates:
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Foundation template {template_file} should exist"
    
    def test_iso_9001_appendix_templates_exist(self):
        """
        Test that appendix templates (0750-0770) exist for ISO 9001.
        
        These provide supporting documentation and reference materials.
        """
        appendix_templates = [
            '0750_Appendix_Process_Map.md',
            '0760_Appendix_Forms_and_Templates.md',
            '0770_Appendix_Terms_and_Abbreviations.md'
        ]
        
        template_dir = Path('templates/en/iso-9001')
        
        for template_file in appendix_templates:
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Appendix template {template_file} should exist"
    
    def test_iso_9001_readme_exists(self):
        """Test that README.md exists for ISO 9001 in both languages."""
        de_readme = Path('templates/de/iso-9001/README.md')
        en_readme = Path('templates/en/iso-9001/README.md')
        
        assert de_readme.exists(), "German ISO 9001 README.md should exist"
        assert en_readme.exists(), "English ISO 9001 README.md should exist"
    
    def test_iso_9001_metadata_templates_exist(self):
        """Test that metadata templates exist for ISO 9001 in both languages."""
        de_metadata = Path('templates/de/iso-9001/0000_metadata_de_iso-9001.md')
        en_metadata = Path('templates/en/iso-9001/0000_metadata_en_iso-9001.md')
        
        assert de_metadata.exists(), "German ISO 9001 metadata template should exist"
        assert en_metadata.exists(), "English ISO 9001 metadata template should exist"
    
    def test_iso_9001_hls_structure_documented(self):
        """
        Test that High-Level Structure (HLS) is documented.
        
        ISO 9001:2015 follows the HLS common to all ISO management system standards.
        The mapping should reference this structure.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for HLS references
        assert 'High-Level Structure' in mapping_content or 'HLS' in mapping_content, \
            "High-Level Structure should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_pdca_cycle_support(self):
        """
        Test that PDCA (Plan-Do-Check-Act) cycle is supported.
        
        ISO 9001 is based on the PDCA cycle. The template structure should support this.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for PDCA references or the cycle components
        # Plan: Clauses 4-6
        # Do: Clauses 7-8
        # Check: Clause 9
        # Act: Clause 10
        
        # At minimum, all these clauses should be present
        for clause_num in range(4, 11):
            pattern = rf'Clause\s+{clause_num}'
            assert re.search(pattern, mapping_content), \
                f"Clause {clause_num} (part of PDCA cycle) should be documented"
    
    def test_iso_9001_process_approach_documented(self):
        """
        Test that process approach is documented.
        
        ISO 9001 requires a process approach to quality management.
        The templates should support process documentation.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for process-related references
        process_indicators = [
            'process',
            'Process Map',
            'processes'
        ]
        
        found_indicators = sum(1 for indicator in process_indicators 
                              if indicator in mapping_content)
        
        assert found_indicators >= 2, \
            "Process approach should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_risk_based_thinking_support(self):
        """
        Test that risk-based thinking is supported.
        
        ISO 9001:2015 emphasizes risk-based thinking throughout the QMS.
        The templates should support risk assessment and management.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for risk-related references
        risk_indicators = [
            'risk',
            'Risk',
            'opportunity',
            'Opportunity'
        ]
        
        found_indicators = sum(1 for indicator in risk_indicators 
                              if indicator in mapping_content)
        
        assert found_indicators >= 2, \
            "Risk-based thinking should be documented in 9999_Framework_Mapping.md"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_26_foundation_templates_exist(self, language):
        """
        Property 26 Extension: Foundation Templates Existence
        
        For any language, the foundation templates (0010-0050) should exist
        as they provide the basis for Clause 4 (Context of the Organization).
        
        Validates: Requirements 6.1, 6.2, 6.3, 6.4
        """
        template_dir = Path(f'templates/{language}/iso-9001')
        
        foundation_templates = [
            '0010',  # Context of Organization
            '0020',  # Interested Parties
            '0030',  # QMS Scope
            '0040',  # QMS and Processes
            '0050',  # Process Map
        ]
        
        for template_num in foundation_templates:
            # Find any file starting with this number
            matching_files = list(template_dir.glob(f'{template_num}_*.md'))
            assert len(matching_files) > 0, \
                f"Foundation template {template_num} should exist in {language} ISO 9001 templates"
    
    def test_iso_9001_customer_focus_documented(self):
        """
        Test that customer focus is documented.
        
        Customer focus is a key principle of ISO 9001. The templates should
        support customer requirements and satisfaction measurement.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for customer-related references
        customer_indicators = [
            'customer',
            'Customer',
            'satisfaction'
        ]
        
        found_indicators = sum(1 for indicator in customer_indicators 
                              if indicator in mapping_content)
        
        assert found_indicators >= 2, \
            "Customer focus should be documented in 9999_Framework_Mapping.md"
    
    def test_iso_9001_continual_improvement_documented(self):
        """
        Test that continual improvement is documented.
        
        Continual improvement is a fundamental principle of ISO 9001.
        Clause 10 specifically addresses improvement.
        """
        mapping_file = Path('templates/en/iso-9001/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for improvement-related references
        improvement_indicators = [
            'Continual improvement',
            'continual improvement',
            'Improvement',
            'Clause 10'
        ]
        
        found_indicators = sum(1 for indicator in improvement_indicators 
                              if indicator in mapping_content)
        
        assert found_indicators >= 2, \
            "Continual improvement should be documented in 9999_Framework_Mapping.md"
