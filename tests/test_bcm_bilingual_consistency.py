"""
Property-based tests for BCM template bilingual consistency.

Feature: template-system-extension
Property 4: Bilingual Template Consistency

For any template type, the German and English versions SHALL have identical numbering,
identical placeholder usage, and identical structural organization.

Validates: Requirements 3.3, 3.4, 3.5
"""

import os
import re
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest


class TestBCMBilingualConsistency:
    """Test bilingual consistency of BCM templates."""
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_bcm_template_count_consistency(self, template_base_path):
        """
        Test that German and English BCM templates have the same count.
        
        Property 4: Bilingual Template Consistency
        Validates: Requirements 3.3
        """
        de_bcm_path = template_base_path / "de" / "bcm"
        en_bcm_path = template_base_path / "en" / "bcm"
        
        # Get all BCM template files (excluding README and metadata)
        de_templates = sorted([
            f for f in os.listdir(de_bcm_path)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ])
        
        en_templates = sorted([
            f for f in os.listdir(en_bcm_path)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ])
        
        # Extract numbering from filenames
        de_numbers = [f[:4] for f in de_templates]
        en_numbers = [f[:4] for f in en_templates]
        
        # Should have same count
        assert len(de_numbers) == len(en_numbers), \
            f"Template count mismatch: DE has {len(de_numbers)}, EN has {len(en_numbers)}"
        
        # Should have same numbering sequence
        assert de_numbers == en_numbers, \
            f"Numbering mismatch: DE={de_numbers}, EN={en_numbers}"
    
    def test_bcm_template_numbering_consistency(self, template_base_path):
        """
        Test that German and English BCM templates have identical numbering.
        
        Property 4: Bilingual Template Consistency
        Validates: Requirements 3.3
        """
        de_bcm_path = template_base_path / "de" / "bcm"
        en_bcm_path = template_base_path / "en" / "bcm"
        
        # Get all BCM template files
        de_templates = [
            f for f in os.listdir(de_bcm_path)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        # Check each German template has corresponding English template
        for de_template in de_templates:
            template_num = de_template[:4]
            
            # Find corresponding English template
            en_templates = [
                f for f in os.listdir(en_bcm_path)
                if f.startswith(template_num) and f.endswith('.md')
            ]
            
            assert len(en_templates) > 0, \
                f"No English template found for German template {de_template}"
    
    def test_bcm_template_placeholder_consistency(self, template_base_path):
        """
        Test that German and English BCM templates use identical placeholders.
        
        Property 4: Bilingual Template Consistency
        Validates: Requirements 3.4
        """
        de_bcm_path = template_base_path / "de" / "bcm"
        en_bcm_path = template_base_path / "en" / "bcm"
        
        # Pattern to match placeholders: {{ meta.* }} or {{ netbox.* }}
        placeholder_pattern = re.compile(r'\{\{\s*(?:meta|netbox)\.[a-zA-Z0-9_.]+\s*\}\}')
        
        # Get sample templates to check
        sample_templates = ['0010', '0020', '0030', '0040', '0050']
        
        for template_num in sample_templates:
            # Find German template
            de_files = [
                f for f in os.listdir(de_bcm_path)
                if f.startswith(template_num) and f.endswith('.md')
            ]
            
            # Find English template
            en_files = [
                f for f in os.listdir(en_bcm_path)
                if f.startswith(template_num) and f.endswith('.md')
            ]
            
            if not de_files or not en_files:
                continue
            
            # Read templates
            with open(de_bcm_path / de_files[0], 'r', encoding='utf-8') as f:
                de_content = f.read()
            
            with open(en_bcm_path / en_files[0], 'r', encoding='utf-8') as f:
                en_content = f.read()
            
            # Extract placeholders
            de_placeholders = set(placeholder_pattern.findall(de_content))
            en_placeholders = set(placeholder_pattern.findall(en_content))
            
            # Placeholders should be identical
            assert de_placeholders == en_placeholders, \
                f"Placeholder mismatch in {template_num}: DE={de_placeholders}, EN={en_placeholders}"
    
    def test_bcm_template_structure_consistency(self, template_base_path):
        """
        Test that German and English BCM templates have identical structure.
        
        Property 4: Bilingual Template Consistency
        Validates: Requirements 3.5
        """
        de_bcm_path = template_base_path / "de" / "bcm"
        en_bcm_path = template_base_path / "en" / "bcm"
        
        # Pattern to match markdown headers
        header_pattern = re.compile(r'^#{1,6}\s+(.+)$', re.MULTILINE)
        
        # Get sample templates to check
        sample_templates = ['0010', '0020', '0030']
        
        for template_num in sample_templates:
            # Find German template
            de_files = [
                f for f in os.listdir(de_bcm_path)
                if f.startswith(template_num) and f.endswith('.md')
            ]
            
            # Find English template
            en_files = [
                f for f in os.listdir(en_bcm_path)
                if f.startswith(template_num) and f.endswith('.md')
            ]
            
            if not de_files or not en_files:
                continue
            
            # Read templates
            with open(de_bcm_path / de_files[0], 'r', encoding='utf-8') as f:
                de_content = f.read()
            
            with open(en_bcm_path / en_files[0], 'r', encoding='utf-8') as f:
                en_content = f.read()
            
            # Extract header structure (count of headers at each level)
            de_headers = header_pattern.findall(de_content)
            en_headers = header_pattern.findall(en_content)
            
            # Should have same number of headers
            assert len(de_headers) == len(en_headers), \
                f"Header count mismatch in {template_num}: DE has {len(de_headers)}, EN has {len(en_headers)}"
    
    def test_bcm_readme_exists_both_languages(self, template_base_path):
        """
        Test that README.md exists in both German and English BCM directories.
        
        Property 4: Bilingual Template Consistency
        Validates: Requirements 3.3
        """
        de_readme = template_base_path / "de" / "bcm" / "README.md"
        en_readme = template_base_path / "en" / "bcm" / "README.md"
        
        assert de_readme.exists(), "German BCM README.md not found"
        assert en_readme.exists(), "English BCM README.md not found"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(template_number=st.integers(min_value=10, max_value=290).filter(lambda x: x % 10 == 0))
    def test_property_bilingual_template_numbering(self, template_base_path, template_number):
        """
        Property test: For any valid template number, if a German template exists,
        an English template with the same number should exist.
        
        Feature: template-system-extension
        Property 4: Bilingual Template Consistency
        
        Validates: Requirements 3.3, 3.4, 3.5
        """
        template_num = f"{template_number:04d}"
        
        de_bcm_path = template_base_path / "de" / "bcm"
        en_bcm_path = template_base_path / "en" / "bcm"
        
        # Find German template
        de_templates = [
            f for f in os.listdir(de_bcm_path)
            if f.startswith(template_num) and f.endswith('.md')
        ]
        
        # If German template exists, English should exist too
        if de_templates:
            en_templates = [
                f for f in os.listdir(en_bcm_path)
                if f.startswith(template_num) and f.endswith('.md')
            ]
            
            assert len(en_templates) > 0, \
                f"German template {template_num} exists but no corresponding English template found"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
