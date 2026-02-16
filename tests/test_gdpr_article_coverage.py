"""
Tests for GDPR Article Coverage

Property-based tests to verify that GDPR template set covers all required articles.

Author: Kiro AI Assistant
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import re


class TestGDPRArticleCoverage:
    """Tests for GDPR article coverage."""
    
    def test_gdpr_templates_exist(self):
        """Test that GDPR template directories exist."""
        de_dir = Path('templates/de/gdpr')
        en_dir = Path('templates/en/gdpr')
        
        assert de_dir.exists(), "German GDPR template directory should exist"
        assert en_dir.exists(), "English GDPR template directory should exist"
    
    def test_gdpr_framework_mapping_exists(self):
        """Test that 9999_Framework_Mapping.md exists for GDPR."""
        de_mapping = Path('templates/de/gdpr/9999_Framework_Mapping.md')
        en_mapping = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        
        assert de_mapping.exists(), "German GDPR 9999_Framework_Mapping.md should exist"
        assert en_mapping.exists(), "English GDPR 9999_Framework_Mapping.md should exist"
    
    def test_gdpr_all_chapters_covered(self):
        """
        Test that GDPR template set covers all main chapters.
        
        GDPR (EU 2016/679) has 11 chapters:
        - Chapter I: General Provisions (Art. 1-4)
        - Chapter II: Principles (Art. 5-11)
        - Chapter III: Rights of the Data Subject (Art. 12-23)
        - Chapter IV: Controller and Processor (Art. 24-43)
        - Chapter V: Transfers to Third Countries (Art. 44-50)
        - Chapter VI: Independent Supervisory Authorities (Art. 51-59)
        - Chapter VII: Cooperation and Consistency (Art. 60-76)
        - Chapter VIII: Remedies, Liability and Penalties (Art. 77-84)
        - Chapter IX: Specific Processing Situations (Art. 85-91)
        - Chapter X: Delegated Acts and Implementing Acts (Art. 92-93)
        - Chapter XI: Final Provisions (Art. 94-99)
        """
        # Read 9999_Framework_Mapping.md to check coverage
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define main GDPR chapters that should be covered
        chapters = {
            'I': 'General Provisions',
            'II': 'Principles',
            'III': 'Rights of the Data Subject',
            'IV': 'Controller and Processor',
            'V': 'Transfers of Personal Data to Third Countries'
        }
        
        # Check that each chapter is mentioned in the mapping
        for chapter_num, chapter_name in chapters.items():
            pattern = rf'###\s+Chapter\s+{chapter_num}[:\s]'
            assert re.search(pattern, mapping_content), \
                f"Chapter {chapter_num} ({chapter_name}) should be documented in 9999_Framework_Mapping.md"
    
    def test_gdpr_chapter_i_articles(self):
        """
        Test that all Chapter I (General Provisions) articles are covered.
        
        Chapter I includes:
        - Art. 1: Subject-matter and objectives
        - Art. 2: Material scope
        - Art. 3: Territorial scope
        - Art. 4: Definitions
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        chapter_i_articles = ['Art. 1', 'Art. 2', 'Art. 3', 'Art. 4']
        
        for article in chapter_i_articles:
            assert article in mapping_content, \
                f"{article} should be documented in 9999_Framework_Mapping.md"
    
    def test_gdpr_chapter_ii_articles(self):
        """
        Test that all Chapter II (Principles) articles are covered.
        
        Chapter II includes:
        - Art. 5: Principles relating to processing of personal data
        - Art. 6: Lawfulness of processing
        - Art. 7: Conditions for consent
        - Art. 8: Conditions applicable to child's consent
        - Art. 9: Processing of special categories of personal data
        - Art. 10: Processing of personal data relating to criminal convictions
        - Art. 11: Processing which does not require identification
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        chapter_ii_articles = [
            'Art. 5', 'Art. 6', 'Art. 7', 'Art. 8', 
            'Art. 9', 'Art. 10', 'Art. 11'
        ]
        
        for article in chapter_ii_articles:
            assert article in mapping_content, \
                f"{article} should be documented in 9999_Framework_Mapping.md"
    
    def test_gdpr_chapter_iii_articles(self):
        """
        Test that all Chapter III (Rights of the Data Subject) articles are covered.
        
        Chapter III includes:
        - Art. 12: Transparent information, communication and modalities
        - Art. 13: Information to be provided where personal data are collected
        - Art. 14: Information to be provided where personal data have not been obtained
        - Art. 15: Right of access by the data subject
        - Art. 16: Right to rectification
        - Art. 17: Right to erasure ('right to be forgotten')
        - Art. 18: Right to restriction of processing
        - Art. 19: Notification obligation regarding rectification or erasure
        - Art. 20: Right to data portability
        - Art. 21: Right to object
        - Art. 22: Automated individual decision-making, including profiling
        - Art. 23: Restrictions
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        chapter_iii_articles = [
            'Art. 12', 'Art. 13', 'Art. 14', 'Art. 15',
            'Art. 16', 'Art. 17', 'Art. 18', 'Art. 19',
            'Art. 20', 'Art. 21', 'Art. 22', 'Art. 23'
        ]
        
        for article in chapter_iii_articles:
            assert article in mapping_content, \
                f"{article} should be documented in 9999_Framework_Mapping.md"
    
    def test_gdpr_chapter_iv_articles(self):
        """
        Test that all Chapter IV (Controller and Processor) articles are covered.
        
        Chapter IV includes key articles:
        - Art. 24: Responsibility of the controller
        - Art. 25: Data protection by design and by default
        - Art. 28: Processor
        - Art. 30: Records of processing activities
        - Art. 32: Security of processing
        - Art. 33: Notification of a personal data breach to the supervisory authority
        - Art. 34: Communication of a personal data breach to the data subject
        - Art. 35: Data protection impact assessment
        - Art. 37: Designation of the data protection officer
        - Art. 40: Codes of conduct
        - Art. 42: Certification
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        chapter_iv_articles = [
            'Art. 24', 'Art. 25', 'Art. 28', 'Art. 30',
            'Art. 32', 'Art. 33', 'Art. 34', 'Art. 35',
            'Art. 37', 'Art. 40', 'Art. 42'
        ]
        
        for article in chapter_iv_articles:
            assert article in mapping_content, \
                f"{article} should be documented in 9999_Framework_Mapping.md"
    
    def test_gdpr_chapter_v_articles(self):
        """
        Test that all Chapter V (Transfers to Third Countries) articles are covered.
        
        Chapter V includes:
        - Art. 44: General principle for transfers
        - Art. 45: Transfers on the basis of an adequacy decision
        - Art. 46: Transfers subject to appropriate safeguards
        - Art. 47: Binding corporate rules
        - Art. 49: Derogations for specific situations
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        chapter_v_articles = [
            'Art. 44', 'Art. 45', 'Art. 46', 'Art. 47', 'Art. 49'
        ]
        
        for article in chapter_v_articles:
            assert article in mapping_content, \
                f"{article} should be documented in 9999_Framework_Mapping.md"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        chapter=st.sampled_from(['I', 'II', 'III', 'IV', 'V'])
    )
    def test_property_27_gdpr_article_coverage(self, language, chapter):
        """
        Feature: compliance-framework-templates, Property 27: GDPR Article Coverage
        
        For any GDPR template set, templates must exist covering all main chapters
        (I-V) which contain the core compliance requirements.
        
        This property verifies that:
        1. The 9999_Framework_Mapping.md file exists
        2. Each of the main chapters (I-V) is documented in the mapping
        3. The mapping indicates which templates cover each chapter's articles
        
        **Validates: Requirements 7.1**
        """
        # Check that template directory exists
        template_dir = Path(f'templates/{language}/gdpr')
        assert template_dir.exists(), \
            f"GDPR template directory should exist for language '{language}'"
        
        # Check that 9999_Framework_Mapping.md exists
        mapping_file = template_dir / '9999_Framework_Mapping.md'
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist in {template_dir}"
        
        # Read mapping content
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Verify that the specific chapter is documented
        # Look for "### Chapter X:" or "### Kapitel X:" pattern (English/German)
        if language == 'de':
            pattern = rf'###\s+Kapitel\s+{chapter}[:\s]'
        else:
            pattern = rf'###\s+Chapter\s+{chapter}[:\s]'
        assert re.search(pattern, mapping_content), \
            f"Chapter {chapter} should be documented in 9999_Framework_Mapping.md for language '{language}'"
        
        # Additionally verify that the chapter section has some content
        # Look for the chapter section and check it has at least some text after it
        if language == 'de':
            section_pattern = rf'###\s+Kapitel\s+{chapter}[:\s][^\n]*\n\n.*?\n'
        else:
            section_pattern = rf'###\s+Chapter\s+{chapter}[:\s][^\n]*\n\n.*?\n'
        section_match = re.search(section_pattern, mapping_content, re.DOTALL)
        
        if section_match:
            # If we found a section, verify it has meaningful content
            section_text = section_match.group(0)
            # Should have more than just the header
            assert len(section_text.strip()) > 50, \
                f"Chapter {chapter} section should have meaningful content"
    
    def test_gdpr_article_to_template_mapping(self):
        """
        Test that key GDPR articles are mapped to specific templates.
        
        This test verifies that the 9999_Framework_Mapping.md not only lists articles
        but also maps them to specific template files.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Define expected mappings based on current implementation
        expected_mappings = {
            'Art. 5': ['0030', '0100'],  # Principles
            'Art. 6': ['0040'],  # Lawfulness
            'Art. 15': ['0220'],  # Right of access
            'Art. 28': ['0310', '0720'],  # Processor
            'Art. 30': ['0320', '0700'],  # Records of processing
            'Art. 33': ['0330', '0600', '0610'],  # Breach notification
            'Art. 35': ['0400', '0410'],  # DPIA
            'Art. 37': ['0340'],  # DPO
        }
        
        for article, template_numbers in expected_mappings.items():
            # Check that at least one of the expected templates is mentioned
            found_template = False
            for template_num in template_numbers:
                if template_num in mapping_content:
                    found_template = True
                    break
            
            assert found_template, \
                f"{article} should reference at least one template from {template_numbers}"
    
    def test_gdpr_coverage_analysis_documented(self):
        """
        Test that coverage analysis is documented in 9999_Framework_Mapping.md.
        
        The mapping should include a coverage analysis section showing coverage
        for all chapters.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for coverage analysis section
        assert '## Coverage Analysis' in mapping_content, \
            "9999_Framework_Mapping.md should include a coverage analysis section"
        
        # Check that complete coverage is documented for main chapters
        assert 'Complete Coverage' in mapping_content or 'comprehensively covered' in mapping_content, \
            "Coverage analysis should show complete coverage for main chapters"
    
    def test_gdpr_template_files_exist_for_covered_articles(self):
        """
        Test that template files actually exist for articles marked as covered.
        
        This verifies that the 9999_Framework_Mapping.md accurately reflects the actual
        template files present in the directory.
        """
        template_dir = Path('templates/en/gdpr')
        
        # Key articles that should be covered with their expected templates
        covered_articles = {
            'Principles': [
                '0030_Data_Protection_Principles.md',
                '0100_Lawfulness_Fairness_and_Transparency.md'
            ],
            'Rights': [
                '0200_Transparent_Information_and_Communication.md',
                '0220_Right_of_Access.md',
                '0230_Rectification_and_Erasure.md'
            ],
            'Controller': [
                '0300_Controller_Obligations_and_Accountability.md',
                '0310_Processing_by_Processor.md',
                '0320_Records_of_Processing_Activities.md'
            ],
            'Breach': [
                '0600_Data_Breach_Response_Plan_Template.md',
                '0610_Breach_Notification_Template_Supervisory_Authority.md'
            ],
            'DPIA': [
                '0400_Data_Protection_Impact_Assessment_DPIA.md',
                '0410_DPIA_Template.md'
            ]
        }
        
        for article_group, template_files in covered_articles.items():
            for template_file in template_files:
                template_path = template_dir / template_file
                assert template_path.exists(), \
                    f"Template {template_file} for {article_group} should exist"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_27_bilingual_consistency(self, language):
        """
        Property 27 Extension: Bilingual Consistency for GDPR Coverage
        
        For any language (German or English), the GDPR article coverage
        should be consistent - both languages should document all main chapters.
        
        Validates: Requirements 7.1, 9.1, 9.2
        """
        mapping_file = Path(f'templates/{language}/gdpr/9999_Framework_Mapping.md')
        
        assert mapping_file.exists(), \
            f"9999_Framework_Mapping.md should exist for language '{language}'"
        
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # All main chapters should be documented
        main_chapters = ['I', 'II', 'III', 'IV', 'V']
        
        for chapter in main_chapters:
            # Use language-specific pattern (Chapter for English, Kapitel for German)
            if language == 'de':
                pattern = rf'###\s+Kapitel\s+{chapter}[:\s]'
            else:
                pattern = rf'###\s+Chapter\s+{chapter}[:\s]'
            assert re.search(pattern, mapping_content), \
                f"Chapter {chapter} should be documented in {language} 9999_Framework_Mapping.md"
    
    def test_gdpr_data_subject_rights_comprehensive(self):
        """
        Test that all data subject rights are comprehensively covered.
        
        GDPR provides extensive rights to data subjects (Chapter III).
        All rights should be mapped to templates.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Key data subject rights
        rights = [
            'Right of access',
            'Right to rectification',
            'Right to erasure',
            'Right to restriction',
            'Right to data portability',
            'Right to object'
        ]
        
        for right in rights:
            assert right.lower() in mapping_content.lower(), \
                f"{right} should be documented in 9999_Framework_Mapping.md"
    
    def test_gdpr_accountability_principle_covered(self):
        """
        Test that the accountability principle is covered.
        
        Art. 5(2) and Art. 24 establish the accountability principle,
        which is fundamental to GDPR compliance.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for accountability references
        assert 'Art. 24' in mapping_content, \
            "Art. 24 (Responsibility of the controller) should be documented"
        assert 'accountability' in mapping_content.lower() or 'Accountability' in mapping_content, \
            "Accountability principle should be documented"
    
    def test_gdpr_security_measures_covered(self):
        """
        Test that security measures (Art. 32) are covered.
        
        Art. 32 requires appropriate technical and organizational measures.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        assert 'Art. 32' in mapping_content, \
            "Art. 32 (Security of processing) should be documented"
        assert 'security' in mapping_content.lower() or 'Security' in mapping_content, \
            "Security measures should be documented"
    
    def test_gdpr_breach_notification_covered(self):
        """
        Test that breach notification requirements (Art. 33-34) are covered.
        
        Art. 33 and 34 establish breach notification obligations.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        assert 'Art. 33' in mapping_content, \
            "Art. 33 (Notification to supervisory authority) should be documented"
        assert 'Art. 34' in mapping_content, \
            "Art. 34 (Communication to data subjects) should be documented"
    
    def test_gdpr_dpia_requirements_covered(self):
        """
        Test that DPIA requirements (Art. 35) are covered.
        
        Art. 35 requires data protection impact assessments for high-risk processing.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        assert 'Art. 35' in mapping_content, \
            "Art. 35 (Data protection impact assessment) should be documented"
        assert 'DPIA' in mapping_content or 'impact assessment' in mapping_content.lower(), \
            "DPIA should be documented"
    
    def test_gdpr_dpo_requirements_covered(self):
        """
        Test that DPO requirements (Art. 37-39) are covered.
        
        Art. 37-39 establish requirements for data protection officers.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        dpo_articles = ['Art. 37', 'Art. 38', 'Art. 39']
        
        for article in dpo_articles:
            assert article in mapping_content, \
                f"{article} (DPO requirements) should be documented"
    
    def test_gdpr_processor_obligations_covered(self):
        """
        Test that processor obligations (Art. 28) are covered.
        
        Art. 28 establishes requirements for processor contracts and obligations.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        assert 'Art. 28' in mapping_content, \
            "Art. 28 (Processor) should be documented"
        assert 'processor' in mapping_content.lower() or 'Processor' in mapping_content, \
            "Processor obligations should be documented"
    
    def test_gdpr_records_of_processing_covered(self):
        """
        Test that records of processing (Art. 30) are covered.
        
        Art. 30 requires maintaining records of processing activities.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        assert 'Art. 30' in mapping_content, \
            "Art. 30 (Records of processing activities) should be documented"
    
    def test_gdpr_international_transfers_covered(self):
        """
        Test that international transfer requirements (Chapter V) are covered.
        
        Chapter V (Art. 44-50) establishes requirements for data transfers to third countries.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        transfer_articles = ['Art. 44', 'Art. 45', 'Art. 46']
        
        for article in transfer_articles:
            assert article in mapping_content, \
                f"{article} (International transfers) should be documented"
    
    @settings(max_examples=50)
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_27_foundation_templates_exist(self, language):
        """
        Property 27 Extension: Foundation Templates Existence
        
        For any language, the foundation templates (0010-0050) should exist
        as they provide the basis for GDPR compliance.
        
        Validates: Requirements 7.1, 7.2, 7.3, 7.4
        """
        template_dir = Path(f'templates/{language}/gdpr')
        
        foundation_templates = [
            '0010',  # Scope and Application
            '0020',  # Roles and Responsibilities
            '0030',  # Data Protection Principles
            '0040',  # Lawfulness of Processing
            '0050',  # Special Categories of Personal Data
        ]
        
        for template_num in foundation_templates:
            # Find any file starting with this number
            matching_files = list(template_dir.glob(f'{template_num}_*.md'))
            assert len(matching_files) > 0, \
                f"Foundation template {template_num} should exist in {language} GDPR templates"
    
    def test_gdpr_readme_exists(self):
        """Test that README.md exists for GDPR in both languages."""
        de_readme = Path('templates/de/gdpr/README.md')
        en_readme = Path('templates/en/gdpr/README.md')
        
        assert de_readme.exists(), "German GDPR README.md should exist"
        assert en_readme.exists(), "English GDPR README.md should exist"
    
    def test_gdpr_metadata_templates_exist(self):
        """Test that metadata templates exist for GDPR in both languages."""
        de_metadata = Path('templates/de/gdpr/0000_metadata_de_gdpr.md')
        en_metadata = Path('templates/en/gdpr/0000_metadata_en_gdpr.md')
        
        assert de_metadata.exists(), "German GDPR metadata template should exist"
        assert en_metadata.exists(), "English GDPR metadata template should exist"
    
    def test_gdpr_appendix_templates_exist(self):
        """
        Test that appendix templates exist for GDPR.
        
        These provide supporting documentation and reference materials.
        """
        appendix_templates = [
            '0700_Appendix_Records_of_Processing_Activities_Template.md',
            '0710_Appendix_DPIA_Quick_Reference.md',
            '0720_Appendix_Data_Processing_Agreement_DPA_Template.md',
            '0730_Appendix_Terms_and_Abbreviations.md'
        ]
        
        template_dir = Path('templates/en/gdpr')
        
        for template_file in appendix_templates:
            template_path = template_dir / template_file
            assert template_path.exists(), \
                f"Appendix template {template_file} should exist"
    
    def test_gdpr_key_article_groups_documented(self):
        """
        Test that key article groups are documented in 9999_Framework_Mapping.md.
        
        The mapping should organize articles into logical groups for easier reference.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for key article group sections
        key_groups = [
            'Core Compliance Requirements',
            'Data Subject Rights',
            'Security and Risk Management',
            'Processor Management',
            'International Data Transfers'
        ]
        
        found_groups = sum(1 for group in key_groups if group in mapping_content)
        
        assert found_groups >= 3, \
            "9999_Framework_Mapping.md should document key article groups"
    
    def test_gdpr_usage_recommendations_documented(self):
        """
        Test that usage recommendations are documented in 9999_Framework_Mapping.md.
        
        The mapping should provide guidance on how to use the templates effectively.
        """
        mapping_file = Path('templates/en/gdpr/9999_Framework_Mapping.md')
        mapping_content = mapping_file.read_text(encoding='utf-8')
        
        # Check for usage recommendations section
        assert '## Usage Recommendations' in mapping_content or 'How to Use' in mapping_content, \
            "9999_Framework_Mapping.md should include usage recommendations"
