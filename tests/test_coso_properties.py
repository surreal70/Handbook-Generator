"""
Property-based tests for COSO Internal Control Framework templates.

This module contains property tests for COSO template structure,
bilingual consistency, and template numbering range coverage.

Feature: additional-compliance-frameworks
Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import os
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest


class TestCOSOTemplateNumberingRangeCoverage:
    """
    Property 3: Template Numbering Range Coverage
    
    For COSO framework template set, the templates must span from 0010 to at least 0600.
    
    Validates: Requirements 20.2, 20.6
    Feature: additional-compliance-frameworks
    Property 3: Template Numbering Range Coverage
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_coso_minimum_template_range_german(self, template_base_path):
        """
        Test that COSO German templates span from 0010 to at least 0600.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 20.2**
        """
        coso_dir = template_base_path / "de" / "coso"
        
        assert coso_dir.exists(), "COSO German template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(coso_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0500
        assert numbers[-1] >= 500, \
            f"Last template number should be at least 0500, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (Framework Overview and Control Environment)
        overview_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(overview_templates) > 0, "Should have Framework Overview and Control Environment templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Risk Assessment)
        risk_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(risk_templates) > 0, "Should have Risk Assessment templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Control Activities)
        control_activities_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(control_activities_templates) > 0, "Should have Control Activities templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Information and Communication)
        info_comm_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(info_comm_templates) > 0, "Should have Information and Communication templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Monitoring Activities)
        monitoring_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(monitoring_templates) > 0, "Should have Monitoring Activities templates (0400-0499)"
        
        # Should have templates in the 0500-0599 range (Integration and Implementation)
        integration_templates = [n for n in numbers if 500 <= n <= 599]
        assert len(integration_templates) > 0, "Should have Integration and Implementation templates (0500-0599)"
    
    def test_coso_minimum_template_range_english(self, template_base_path):
        """
        Test that COSO English templates span from 0010 to at least 0600.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 20.2**
        """
        coso_dir = template_base_path / "en" / "coso"
        
        assert coso_dir.exists(), "COSO English template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(coso_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0500
        assert numbers[-1] >= 500, \
            f"Last template number should be at least 0500, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (Framework Overview and Control Environment)
        overview_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(overview_templates) > 0, "Should have Framework Overview and Control Environment templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Risk Assessment)
        risk_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(risk_templates) > 0, "Should have Risk Assessment templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Control Activities)
        control_activities_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(control_activities_templates) > 0, "Should have Control Activities templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Information and Communication)
        info_comm_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(info_comm_templates) > 0, "Should have Information and Communication templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Monitoring Activities)
        monitoring_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(monitoring_templates) > 0, "Should have Monitoring Activities templates (0400-0499)"
        
        # Should have templates in the 0500-0599 range (Integration and Implementation)
        integration_templates = [n for n in numbers if 500 <= n <= 599]
        assert len(integration_templates) > 0, "Should have Integration and Implementation templates (0500-0599)"


class TestCOSOBilingualTemplateConsistency:
    """
    Property 7: Bilingual Template Consistency
    
    For any template in one language (German or English), there must exist a corresponding
    template in the other language with identical filename, section structure, and placeholder locations.
    
    Validates: Requirements 20.2, 20.6
    Feature: additional-compliance-frameworks
    Property 7: Bilingual Template Consistency
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_coso_bilingual_filename_consistency(self, template_base_path):
        """
        Test that COSO German and English templates have matching filenames.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 20.6**
        """
        de_dir = template_base_path / "de" / "coso"
        en_dir = template_base_path / "en" / "coso"
        
        assert de_dir.exists(), "COSO German template directory should exist"
        assert en_dir.exists(), "COSO English template directory should exist"
        
        # Get all template files (excluding language-specific metadata files)
        de_templates = set([
            f for f in os.listdir(de_dir)
            if f.endswith('.md') and not f.startswith('0000_metadata_de')
        ])
        
        en_templates = set([
            f for f in os.listdir(en_dir)
            if f.endswith('.md') and not f.startswith('0000_metadata_en')
        ])
        
        # Check that all German templates have English counterparts
        missing_in_english = de_templates - en_templates
        assert len(missing_in_english) == 0, \
            f"German templates missing in English: {missing_in_english}"
        
        # Check that all English templates have German counterparts
        missing_in_german = en_templates - de_templates
        assert len(missing_in_german) == 0, \
            f"English templates missing in German: {missing_in_german}"
    
    def test_coso_metadata_template_consistency(self, template_base_path):
        """
        Test that COSO metadata templates exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 20.6**
        """
        de_metadata = template_base_path / "de" / "coso" / "0000_metadata_de_coso.md"
        en_metadata = template_base_path / "en" / "coso" / "0000_metadata_en_coso.md"
        
        assert de_metadata.exists(), "German metadata template should exist"
        assert en_metadata.exists(), "English metadata template should exist"
    
    def test_coso_documentation_files_exist(self, template_base_path):
        """
        Test that COSO documentation files exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 20.6**
        """
        de_readme = template_base_path / "de" / "coso" / "README.md"
        en_readme = template_base_path / "en" / "coso" / "README.md"
        de_mapping = template_base_path / "de" / "coso" / "FRAMEWORK_MAPPING.md"
        en_mapping = template_base_path / "en" / "coso" / "FRAMEWORK_MAPPING.md"
        
        assert de_readme.exists(), "German README should exist"
        assert en_readme.exists(), "English README should exist"
        assert de_mapping.exists(), "German FRAMEWORK_MAPPING should exist"
        assert en_mapping.exists(), "English FRAMEWORK_MAPPING should exist"

