"""
Property-based tests for DORA Metrics templates.

This module contains property tests for DORA template structure,
bilingual consistency, and template numbering range coverage.

Feature: additional-compliance-frameworks
Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import os
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest


class TestDORATemplateNumberingRangeCoverage:
    """
    Property 3: Template Numbering Range Coverage
    
    For DORA framework template set, the templates must span from 0010 to at least 0400.
    
    Validates: Requirements 21.2, 21.6
    Feature: additional-compliance-frameworks
    Property 3: Template Numbering Range Coverage
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_dora_minimum_template_range_german(self, template_base_path):
        """
        Test that DORA German templates span from 0010 to at least 0400.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 21.2**
        """
        dora_dir = template_base_path / "de" / "dora"
        
        assert dora_dir.exists(), "DORA German template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(dora_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0400
        assert numbers[-1] >= 400, \
            f"Last template number should be at least 0400, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (DORA Framework Overview)
        overview_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(overview_templates) > 0, "Should have DORA Framework Overview templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Deployment Frequency)
        deployment_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(deployment_templates) > 0, "Should have Deployment Frequency templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Lead Time for Changes)
        lead_time_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(lead_time_templates) > 0, "Should have Lead Time for Changes templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Mean Time to Restore)
        mttr_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(mttr_templates) > 0, "Should have Mean Time to Restore templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Change Failure Rate and Technical Practices)
        cfr_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(cfr_templates) > 0, "Should have Change Failure Rate and Technical Practices templates (0400-0499)"
    
    def test_dora_minimum_template_range_english(self, template_base_path):
        """
        Test that DORA English templates span from 0010 to at least 0400.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 21.2**
        """
        dora_dir = template_base_path / "en" / "dora"
        
        assert dora_dir.exists(), "DORA English template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(dora_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0400
        assert numbers[-1] >= 400, \
            f"Last template number should be at least 0400, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (DORA Framework Overview)
        overview_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(overview_templates) > 0, "Should have DORA Framework Overview templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Deployment Frequency)
        deployment_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(deployment_templates) > 0, "Should have Deployment Frequency templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Lead Time for Changes)
        lead_time_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(lead_time_templates) > 0, "Should have Lead Time for Changes templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Mean Time to Restore)
        mttr_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(mttr_templates) > 0, "Should have Mean Time to Restore templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Change Failure Rate and Technical Practices)
        cfr_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(cfr_templates) > 0, "Should have Change Failure Rate and Technical Practices templates (0400-0499)"


class TestDORABilingualTemplateConsistency:
    """
    Property 7: Bilingual Template Consistency
    
    For any template in one language (German or English), there must exist a corresponding
    template in the other language with identical filename, section structure, and placeholder locations.
    
    Validates: Requirements 21.2, 21.6
    Feature: additional-compliance-frameworks
    Property 7: Bilingual Template Consistency
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_dora_bilingual_filename_consistency(self, template_base_path):
        """
        Test that DORA German and English templates have matching filenames.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 21.6**
        """
        de_dir = template_base_path / "de" / "dora"
        en_dir = template_base_path / "en" / "dora"
        
        assert de_dir.exists(), "DORA German template directory should exist"
        assert en_dir.exists(), "DORA English template directory should exist"
        
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
    
    def test_dora_metadata_template_consistency(self, template_base_path):
        """
        Test that DORA metadata templates exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 21.6**
        """
        de_metadata = template_base_path / "de" / "dora" / "0000_metadata_de_dora.md"
        en_metadata = template_base_path / "en" / "dora" / "0000_metadata_en_dora.md"
        
        assert de_metadata.exists(), "German metadata template should exist"
        assert en_metadata.exists(), "English metadata template should exist"
    
    def test_dora_documentation_files_exist(self, template_base_path):
        """
        Test that DORA documentation files exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 21.6**
        """
        de_readme = template_base_path / "de" / "dora" / "README.md"
        en_readme = template_base_path / "en" / "dora" / "README.md"
        de_mapping = template_base_path / "de" / "dora" / "FRAMEWORK_MAPPING.md"
        en_mapping = template_base_path / "en" / "dora" / "FRAMEWORK_MAPPING.md"
        
        assert de_readme.exists(), "German README should exist"
        assert en_readme.exists(), "English README should exist"
        assert de_mapping.exists(), "German FRAMEWORK_MAPPING should exist"
        assert en_mapping.exists(), "English FRAMEWORK_MAPPING should exist"
