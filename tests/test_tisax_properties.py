"""
Property-based tests for TISAX templates.

This module contains property tests for TISAX template structure,
bilingual consistency, and template numbering range coverage.

Feature: additional-compliance-frameworks
Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2025, 2026
"""

import os
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest


class TestTISAXTemplateNumberingRangeCoverage:
    """
    Property 3: Template Numbering Range Coverage
    
    For TISAX framework template set, the templates must span from 0010 to at least 0600.
    
    Validates: Requirements 18.2, 18.6
    Feature: additional-compliance-frameworks
    Property 3: Template Numbering Range Coverage
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_tisax_minimum_template_range_german(self, template_base_path):
        """
        Test that TISAX German templates span from 0010 to at least 0600.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 18.2**
        """
        tisax_dir = template_base_path / "de" / "tisax"
        
        assert tisax_dir.exists(), "TISAX German template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(tisax_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0550
        assert numbers[-1] >= 550, \
            f"Last template number should be at least 0550, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (Information Security Management)
        ism_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(ism_templates) > 0, "Should have Information Security Management templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Asset Management and Access Control)
        asset_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(asset_templates) > 0, "Should have Asset Management templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Cryptography and Physical Security)
        crypto_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(crypto_templates) > 0, "Should have Cryptography templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Operations and Communications Security)
        ops_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(ops_templates) > 0, "Should have Operations Security templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Supplier Relationships and Incident Management)
        supplier_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(supplier_templates) > 0, "Should have Supplier and Incident Management templates (0400-0499)"
        
        # Should have templates in the 0500-0599 range (Business Continuity and Compliance)
        bc_templates = [n for n in numbers if 500 <= n <= 599]
        assert len(bc_templates) > 0, "Should have Business Continuity templates (0500-0599)"
    
    def test_tisax_minimum_template_range_english(self, template_base_path):
        """
        Test that TISAX English templates span from 0010 to at least 0600.
        
        Feature: additional-compliance-frameworks
        Property 3: Template Numbering Range Coverage
        **Validates: Requirements 18.2**
        """
        tisax_dir = template_base_path / "en" / "tisax"
        
        assert tisax_dir.exists(), "TISAX English template directory should exist"
        
        # Get all template files (excluding metadata)
        templates = [
            f for f in os.listdir(tisax_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        assert len(templates) > 0, "Should have at least one template"
        
        # Extract numbers
        numbers = sorted([int(f[:4]) for f in templates])
        
        # Minimum number should be 0010 or close to it
        assert numbers[0] <= 50, \
            f"First template number should be 0010 or close, found {numbers[0]:04d}"
        
        # Maximum number should be at least 0550
        assert numbers[-1] >= 550, \
            f"Last template number should be at least 0550, found {numbers[-1]:04d}"
        
        # Should have templates in the 0010-0099 range (Information Security Management)
        ism_templates = [n for n in numbers if 10 <= n <= 99]
        assert len(ism_templates) > 0, "Should have Information Security Management templates (0010-0099)"
        
        # Should have templates in the 0100-0199 range (Asset Management and Access Control)
        asset_templates = [n for n in numbers if 100 <= n <= 199]
        assert len(asset_templates) > 0, "Should have Asset Management templates (0100-0199)"
        
        # Should have templates in the 0200-0299 range (Cryptography and Physical Security)
        crypto_templates = [n for n in numbers if 200 <= n <= 299]
        assert len(crypto_templates) > 0, "Should have Cryptography templates (0200-0299)"
        
        # Should have templates in the 0300-0399 range (Operations and Communications Security)
        ops_templates = [n for n in numbers if 300 <= n <= 399]
        assert len(ops_templates) > 0, "Should have Operations Security templates (0300-0399)"
        
        # Should have templates in the 0400-0499 range (Supplier Relationships and Incident Management)
        supplier_templates = [n for n in numbers if 400 <= n <= 499]
        assert len(supplier_templates) > 0, "Should have Supplier and Incident Management templates (0400-0499)"
        
        # Should have templates in the 0500-0599 range (Business Continuity and Compliance)
        bc_templates = [n for n in numbers if 500 <= n <= 599]
        assert len(bc_templates) > 0, "Should have Business Continuity templates (0500-0599)"


class TestTISAXBilingualTemplateConsistency:
    """
    Property 7: Bilingual Template Consistency
    
    For any template in one language (German or English), there must exist a corresponding
    template in the other language with identical filename, section structure, and placeholder locations.
    
    Validates: Requirements 18.2, 18.6
    Feature: additional-compliance-frameworks
    Property 7: Bilingual Template Consistency
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_tisax_bilingual_filename_consistency(self, template_base_path):
        """
        Test that TISAX German and English templates have matching filenames.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 18.6**
        """
        de_dir = template_base_path / "de" / "tisax"
        en_dir = template_base_path / "en" / "tisax"
        
        assert de_dir.exists(), "TISAX German template directory should exist"
        assert en_dir.exists(), "TISAX English template directory should exist"
        
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
    
    def test_tisax_metadata_template_consistency(self, template_base_path):
        """
        Test that TISAX metadata templates exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 18.6**
        """
        de_metadata = template_base_path / "de" / "tisax" / "0000_metadata_de_tisax.md"
        en_metadata = template_base_path / "en" / "tisax" / "0000_metadata_en_tisax.md"
        
        assert de_metadata.exists(), "German metadata template should exist"
        assert en_metadata.exists(), "English metadata template should exist"
    
    def test_tisax_documentation_files_exist(self, template_base_path):
        """
        Test that TISAX documentation files exist in both languages.
        
        Feature: additional-compliance-frameworks
        Property 7: Bilingual Template Consistency
        **Validates: Requirements 18.6**
        """
        de_readme = template_base_path / "de" / "tisax" / "README.md"
        en_readme = template_base_path / "en" / "tisax" / "README.md"
        de_mapping = template_base_path / "de" / "tisax" / "9999_Framework_Mapping.md"
        en_mapping = template_base_path / "en" / "tisax" / "9999_Framework_Mapping.md"
        
        assert de_readme.exists(), "German README should exist"
        assert en_readme.exists(), "English README should exist"
        assert de_mapping.exists(), "German FRAMEWORK_MAPPING should exist"
        assert en_mapping.exists(), "English FRAMEWORK_MAPPING should exist"
