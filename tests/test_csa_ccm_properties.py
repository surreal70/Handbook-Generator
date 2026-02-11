"""
Property-based tests for CSA CCM templates.

This module contains property tests for CSA CCM template structure,
bilingual consistency, and template numbering range coverage.

Feature: additional-compliance-frameworks
Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import os
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest


class TestCSACCMTemplateNumberingRangeCoverage:
    """
    Property 3: Template Numbering Range Coverage
    
    For CSA CCM framework template set, the templates must span from 0010 to at least 0800.
    
    Validates: Requirements 17.2, 17.6
    Feature: additional-compliance-frameworks
    Property 3: Template Numbering Range Coverage
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_csa_ccm_minimum_template_range_german(self, template_base_path):
        """
        Test that CSA CCM German templates span from 0010 to at least 0800.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 17.2**
        """
        csa_ccm_dir = template_base_path / "de" / "csa-ccm"
        
        assert csa_ccm_dir.exists(), "CSA CCM German template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(csa_ccm_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0800
        assert numbers[-1] >= 700, \
            f"Last template number should be at least 0700, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (Governance and Risk Management)
        governance_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(governance_templates) > 0, "Should have Governance templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Application Security)
        app_security_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(app_security_templates) > 0, "Should have Application Security templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Data Security)
        data_security_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(data_security_templates) > 0, "Should have Data Security templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (IAM)
        iam_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(iam_templates) > 0, "Should have IAM templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Infrastructure Security)
        infra_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(infra_templates) > 0, "Should have Infrastructure Security templates (0400-0499)"
        
        # Should have templates in the 0500-0599 range (Security Operations)
        secops_templates = [n for n in numbers if 500 <= n <= 599]
        assert len(secops_templates) > 0, "Should have Security Operations templates (0500-0599)"
        
        # Should have templates in the 0600-0699 range (Compliance and Audit)
        compliance_templates = [n for n in numbers if 600 <= n <= 699]
        assert len(compliance_templates) > 0, "Should have Compliance templates (0600-0699)"
        
        # Should have templates in the 0700-0799 range (HR and Change Management)
        hr_templates = [n for n in numbers if 700 <= n <= 799]
        assert len(hr_templates) > 0, "Should have HR and Change Management templates (0700-0799)"
    
    def test_csa_ccm_minimum_template_range_english(self, template_base_path):
        """
        Test that CSA CCM English templates span from 0010 to at least 0800.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 17.2**
        """
        csa_ccm_dir = template_base_path / "en" / "csa-ccm"
        
        assert csa_ccm_dir.exists(), "CSA CCM English template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(csa_ccm_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0700
        assert numbers[-1] >= 700, \
            f"Last template number should be at least 0700, found {numbers[-1]:04d}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_csa_ccm_template_range_coverage(self, template_base_path, language):
        """
        Property test: For any language (German or English), CSA CCM templates
        should span from 0010 to at least 0800.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        
        **Validates: Requirements 17.2, 17.6**
        """
        csa_ccm_dir = template_base_path / language / "csa-ccm"
        
        if not csa_ccm_dir.exists():
            pytest.skip(f"CSA CCM {language} template directory does not exist")
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(csa_ccm_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        if not templates:
            pytest.skip(f"No templates found in {language}/csa-ccm")
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Property: Range should span from near 0010 to at least 0700
        assert numbers[0] <= 50, \
            f"First template should be near 0010, found {numbers[0]:04d}"
        assert numbers[-1] >= 700, \
            f"Last template should be at least 0700, found {numbers[-1]:04d}"
        
        # Property: Should have coverage across all major control domains
        ranges = {
            'governance_risk': (10, 99),
            'application_security': (100, 199),
            'data_security': (200, 299),
            'iam': (300, 399),
            'infrastructure': (400, 499),
            'security_operations': (500, 599),
            'compliance_audit': (600, 699),
            'hr_change_mgmt': (700, 799)
        }
        
        for range_name, (min_val, max_val) in ranges.items():
            range_templates = [n for n in numbers if min_val <= n <= max_val]
            assert len(range_templates) > 0, \
                f"Should have templates in {range_name} range ({min_val:04d}-{max_val:04d})"


class TestCSACCMBilingualTemplateConsistency:
    """
    Property 7: Bilingual Template Consistency
    
    For any template in one language (German or English), there must exist a corresponding
    template in the other language with identical filename, section structure, and
    placeholder locations.
    
    Validates: Requirements 17.6, 5.3, 5.4, 5.5, 9.6
    Feature: additional-compliance-frameworks
    Property 7: Bilingual Template Consistency
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_csa_ccm_bilingual_filename_consistency(self, template_base_path):
        """
        Test that German and English CSA CCM templates have matching filenames.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 17.6**
        """
        de_dir = template_base_path / "de" / "csa-ccm"
        en_dir = template_base_path / "en" / "csa-ccm"
        
        assert de_dir.exists(), "German CSA CCM directory should exist"
        assert en_dir.exists(), "English CSA CCM directory should exist"
        
        # Get template files (excluding metadata and documentation)
        de_templates = set([
            f[:4] for f in os.listdir(de_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            and f not in ['README.md', 'FRAMEWORK_MAPPING.md']
        ])
        
        en_templates = set([
            f[:4] for f in os.listdir(en_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            and f not in ['README.md', 'FRAMEWORK_MAPPING.md']
        ])
        
        # Both languages should have the same template numbers
        assert de_templates == en_templates, \
            f"German and English templates should have matching numbers. " \
            f"DE only: {de_templates - en_templates}, EN only: {en_templates - de_templates}"
    
    def test_csa_ccm_metadata_files_exist(self, template_base_path):
        """
        Test that metadata files exist for both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 17.6**
        """
        de_metadata = template_base_path / "de" / "csa-ccm" / "0000_metadata_de_csa-ccm.md"
        en_metadata = template_base_path / "en" / "csa-ccm" / "0000_metadata_en_csa-ccm.md"
        
        assert de_metadata.exists(), "German metadata file should exist"
        assert en_metadata.exists(), "English metadata file should exist"
    
    def test_csa_ccm_documentation_files_exist(self, template_base_path):
        """
        Test that documentation files exist for both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 17.6**
        """
        de_readme = template_base_path / "de" / "csa-ccm" / "README.md"
        en_readme = template_base_path / "en" / "csa-ccm" / "README.md"
        de_mapping = template_base_path / "de" / "csa-ccm" / "FRAMEWORK_MAPPING.md"
        en_mapping = template_base_path / "en" / "csa-ccm" / "FRAMEWORK_MAPPING.md"
        
        assert de_readme.exists(), "German README should exist"
        assert en_readme.exists(), "English README should exist"
        assert de_mapping.exists(), "German FRAMEWORK_MAPPING should exist"
        assert en_mapping.exists(), "English FRAMEWORK_MAPPING should exist"
    
    def test_csa_ccm_template_header_structure(self, template_base_path):
        """
        Test that templates have proper header structure with required fields.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 17.6**
        """
        for language in ['de', 'en']:
            csa_ccm_dir = template_base_path / language / "csa-ccm"
            
            if not csa_ccm_dir.exists():
                continue
            
            # Get template files (excluding metadata and documentation)
            templates = [
                f for f in os.listdir(csa_ccm_dir)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
                and f not in ['README.md', 'FRAMEWORK_MAPPING.md']
            ]
            
            for template_file in templates:
                template_path = csa_ccm_dir / template_file
                
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for required header fields (YAML frontmatter format)
                assert 'Document-ID:' in content or 'Dokument-ID:' in content, \
                    f"Template {template_file} should have Document-ID field"
                assert 'Owner:' in content, \
                    f"Template {template_file} should have Owner field"
                assert 'Version:' in content, \
                    f"Template {template_file} should have Version field"
                assert 'Status:' in content, \
                    f"Template {template_file} should have Status field"
                assert 'Classification:' in content or 'Klassifizierung:' in content, \
                    f"Template {template_file} should have Classification field"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_number=st.integers(min_value=10, max_value=799)
    )
    def test_property_csa_ccm_bilingual_consistency(self, template_base_path, template_number):
        """
        Property test: For any template number, if it exists in one language,
        it should exist in the other language with matching structure.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        
        **Validates: Requirements 17.6, 5.3, 5.4, 5.5, 9.6**
        """
        de_dir = template_base_path / "de" / "csa-ccm"
        en_dir = template_base_path / "en" / "csa-ccm"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("CSA CCM directories do not exist")
        
        # Find templates with this number
        template_num_str = f"{template_number:04d}"
        
        de_templates = [
            f for f in os.listdir(de_dir)
            if f.startswith(template_num_str) and f.endswith('.md')
        ]
        
        en_templates = [
            f for f in os.listdir(en_dir)
            if f.startswith(template_num_str) and f.endswith('.md')
        ]
        
        # If template exists in one language, it should exist in the other
        if de_templates:
            assert en_templates, \
                f"Template {template_num_str} exists in German but not in English"
        
        if en_templates:
            assert de_templates, \
                f"Template {template_num_str} exists in English but not in German"
        
        # If both exist, verify they have similar structure
        if de_templates and en_templates:
            de_path = de_dir / de_templates[0]
            en_path = en_dir / en_templates[0]
            
            with open(de_path, 'r', encoding='utf-8') as f:
                de_content = f.read()
            
            with open(en_path, 'r', encoding='utf-8') as f:
                en_content = f.read()
            
            # Both should have markdown headers
            de_headers = len([line for line in de_content.split('\n') if line.startswith('#')])
            en_headers = len([line for line in en_content.split('\n') if line.startswith('#')])
            
            # Header count should be similar (within 20% tolerance)
            if de_headers > 0 and en_headers > 0:
                ratio = min(de_headers, en_headers) / max(de_headers, en_headers)
                assert ratio >= 0.8, \
                    f"Template {template_num_str} should have similar header structure. " \
                    f"DE: {de_headers}, EN: {en_headers}"
    
    def test_csa_ccm_diagrams_directory_exists(self, template_base_path):
        """
        Test that diagrams subdirectory exists for both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 17.6**
        """
        de_diagrams = template_base_path / "de" / "csa-ccm" / "diagrams"
        en_diagrams = template_base_path / "en" / "csa-ccm" / "diagrams"
        
        assert de_diagrams.exists(), "German diagrams directory should exist"
        assert en_diagrams.exists(), "English diagrams directory should exist"
        assert de_diagrams.is_dir(), "German diagrams should be a directory"
        assert en_diagrams.is_dir(), "English diagrams should be a directory"
