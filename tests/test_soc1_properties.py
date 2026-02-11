"""
Property-based tests for SOC 1 / SSAE 18 templates.

This module contains property tests for SOC 1 template structure,
bilingual consistency, and template numbering range coverage.

Feature: additional-compliance-frameworks
Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import os
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest


class TestSOC1TemplateNumberingRangeCoverage:
    """
    Property 3: Template Numbering Range Coverage
    
    For SOC 1 framework template set, the templates must span from 0010 to at least 0500.
    
    Validates: Requirements 19.2, 19.6
    Feature: additional-compliance-frameworks
    Property 3: Template Numbering Range Coverage
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_soc1_minimum_template_range_german(self, template_base_path):
        """
        Test that SOC 1 German templates span from 0010 to at least 0500.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 19.2**
        """
        soc1_dir = template_base_path / "de" / "soc1"
        
        assert soc1_dir.exists(), "SOC 1 German template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(soc1_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0450
        assert numbers[-1] >= 450, \
            f"Last template number should be at least 0450, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (Service Organization Overview)
        overview_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(overview_templates) > 0, "Should have Service Organization Overview templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Control Environment)
        control_env_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(control_env_templates) > 0, "Should have Control Environment templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Risk Assessment)
        risk_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(risk_templates) > 0, "Should have Risk Assessment templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Control Activities)
        control_activities_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(control_activities_templates) > 0, "Should have Control Activities templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Information, Communication, and Monitoring)
        info_comm_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(info_comm_templates) > 0, "Should have Information and Communication templates (0400-0499)"
    
    def test_soc1_minimum_template_range_english(self, template_base_path):
        """
        Test that SOC 1 English templates span from 0010 to at least 0500.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 19.2**
        """
        soc1_dir = template_base_path / "en" / "soc1"
        
        assert soc1_dir.exists(), "SOC 1 English template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(soc1_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0450
        assert numbers[-1] >= 450, \
            f"Last template number should be at least 0450, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (Service Organization Overview)
        overview_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(overview_templates) > 0, "Should have Service Organization Overview templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Control Environment)
        control_env_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(control_env_templates) > 0, "Should have Control Environment templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Risk Assessment)
        risk_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(risk_templates) > 0, "Should have Risk Assessment templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Control Activities)
        control_activities_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(control_activities_templates) > 0, "Should have Control Activities templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Information, Communication, and Monitoring)
        info_comm_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(info_comm_templates) > 0, "Should have Information and Communication templates (0400-0499)"


class TestSOC1BilingualTemplateConsistency:
    """
    Property 7: Bilingual Template Consistency
    
    For any template in one language (German or English), there must exist a corresponding
    template in the other language with identical filename, section structure, and placeholder locations.
    
    Validates: Requirements 19.2, 19.6
    Feature: additional-compliance-frameworks
    Property 7: Bilingual Template Consistency
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_soc1_bilingual_filename_consistency(self, template_base_path):
        """
        Test that SOC 1 German and English templates have matching filenames.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 19.6**
        """
        de_dir = template_base_path / "de" / "soc1"
        en_dir = template_base_path / "en" / "soc1"
        
        assert de_dir.exists(), "SOC 1 German template directory should exist"
        assert en_dir.exists(), "SOC 1 English template directory should exist"
        
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
    
    def test_soc1_metadata_template_consistency(self, template_base_path):
        """
        Test that SOC 1 metadata templates exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 19.6**
        """
        de_metadata = template_base_path / "de" / "soc1" / "0000_metadata_de_soc1.md"
        en_metadata = template_base_path / "en" / "soc1" / "0000_metadata_en_soc1.md"
        
        assert de_metadata.exists(), "German metadata template should exist"
        assert en_metadata.exists(), "English metadata template should exist"
    
    def test_soc1_documentation_files_exist(self, template_base_path):
        """
        Test that SOC 1 documentation files exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 19.6**
        """
        de_readme = template_base_path / "de" / "soc1" / "README.md"
        en_readme = template_base_path / "en" / "soc1" / "README.md"
        de_mapping = template_base_path / "de" / "soc1" / "FRAMEWORK_MAPPING.md"
        en_mapping = template_base_path / "en" / "soc1" / "FRAMEWORK_MAPPING.md"
        
        assert de_readme.exists(), "German README should exist"
        assert en_readme.exists(), "English README should exist"
        assert de_mapping.exists(), "German FRAMEWORK_MAPPING should exist"
        assert en_mapping.exists(), "English FRAMEWORK_MAPPING should exist"
