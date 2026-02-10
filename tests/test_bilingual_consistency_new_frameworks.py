"""
Unit tests for bilingual consistency of new compliance frameworks.

Tests filename matching, section structure matching, and placeholder location matching
across German and English versions of IDW PS 951, NIST CSF 2.0, and TOGAF templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026

Validates: Requirements 14.6
"""

import pytest
import re
from pathlib import Path


class TestFilenameMatching:
    """Unit tests for filename matching across languages."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def test_idw_ps_951_filename_matching(self, template_base_path):
        """Test that IDW PS 951 German and English templates have matching filenames."""
        de_dir = template_base_path / "de" / "idw-ps-951"
        en_dir = template_base_path / "en" / "idw-ps-951"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("IDW PS 951 templates not found in both languages")
        
        # Get template numbers (excluding metadata and README)
        de_templates = sorted([
            f.name[:4] for f in de_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        en_templates = sorted([
            f.name[:4] for f in en_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        # Convert to sets for comparison
        de_numbers = set(de_templates)
        en_numbers = set(en_templates)
        
        # Check for matching numbers
        assert de_numbers == en_numbers, \
            f"Template numbers should match. " \
            f"DE only: {de_numbers - en_numbers}, EN only: {en_numbers - de_numbers}"
    
    def test_nist_csf_filename_matching(self, template_base_path):
        """Test that NIST CSF German and English templates have matching filenames."""
        de_dir = template_base_path / "de" / "nist-csf"
        en_dir = template_base_path / "en" / "nist-csf"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("NIST CSF templates not found in both languages")
        
        # Get template numbers
        de_templates = sorted([
            f.name[:4] for f in de_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        en_templates = sorted([
            f.name[:4] for f in en_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        # Convert to sets for comparison
        de_numbers = set(de_templates)
        en_numbers = set(en_templates)
        
        # Check for matching numbers
        assert de_numbers == en_numbers, \
            f"Template numbers should match. " \
            f"DE only: {de_numbers - en_numbers}, EN only: {en_numbers - de_numbers}"
    
    def test_togaf_filename_matching(self, template_base_path):
        """Test that TOGAF German and English templates have matching filenames."""
        de_dir = template_base_path / "de" / "togaf"
        en_dir = template_base_path / "en" / "togaf"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("TOGAF templates not found in both languages")
        
        # Get template numbers
        de_templates = sorted([
            f.name[:4] for f in de_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        en_templates = sorted([
            f.name[:4] for f in en_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        # Convert to sets for comparison
        de_numbers = set(de_templates)
        en_numbers = set(en_templates)
        
        # Check for matching numbers
        assert de_numbers == en_numbers, \
            f"Template numbers should match. " \
            f"DE only: {de_numbers - en_numbers}, EN only: {en_numbers - de_numbers}"
    
    def test_metadata_files_exist_both_languages(self, template_base_path):
        """Test that metadata files exist in both languages for all frameworks."""
        frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in frameworks:
            de_metadata = template_base_path / "de" / framework / f"0000_metadata_de_{framework}.md"
            en_metadata = template_base_path / "en" / framework / f"0000_metadata_en_{framework}.md"
            
            if de_metadata.parent.exists():
                assert de_metadata.exists(), \
                    f"German metadata should exist for {framework}"
            
            if en_metadata.parent.exists():
                assert en_metadata.exists(), \
                    f"English metadata should exist for {framework}"


class TestSectionStructureMatching:
    """Unit tests for section structure matching across languages."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def extract_section_headers(self, content):
        """Extract section headers from markdown content."""
        # Find all markdown headers (##, ###, etc.)
        headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        # Return list of (level, text) tuples
        return [(len(marks), text.strip()) for marks, text in headers]
    
    def test_idw_ps_951_section_structure(self, template_base_path):
        """Test that IDW PS 951 templates have matching section structure."""
        de_dir = template_base_path / "de" / "idw-ps-951"
        en_dir = template_base_path / "en" / "idw-ps-951"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("IDW PS 951 templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {f.name[:4]: f for f in de_dir.glob("00[1-5]0_*.md")}
        en_templates = {f.name[:4]: f for f in en_dir.glob("00[1-5]0_*.md")}
        
        # Find common template numbers
        common_numbers = set(de_templates.keys()) & set(en_templates.keys())
        
        if not common_numbers:
            pytest.skip("No matching templates found")
        
        # Check first few matching templates
        for number in sorted(common_numbers)[:3]:
            de_content = de_templates[number].read_text()
            en_content = en_templates[number].read_text()
            
            de_headers = self.extract_section_headers(de_content)
            en_headers = self.extract_section_headers(en_content)
            
            # Check that header levels match
            de_levels = [level for level, _ in de_headers]
            en_levels = [level for level, _ in en_headers]
            
            assert de_levels == en_levels, \
                f"Template {number}: Header levels should match. " \
                f"DE: {de_levels}, EN: {en_levels}"
    
    def test_nist_csf_section_structure(self, template_base_path):
        """Test that NIST CSF templates have matching section structure."""
        de_dir = template_base_path / "de" / "nist-csf"
        en_dir = template_base_path / "en" / "nist-csf"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("NIST CSF templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {f.name[:4]: f for f in de_dir.glob("00[1-6]0_*.md")}
        en_templates = {f.name[:4]: f for f in en_dir.glob("00[1-6]0_*.md")}
        
        # Find common template numbers
        common_numbers = set(de_templates.keys()) & set(en_templates.keys())
        
        if not common_numbers:
            pytest.skip("No matching templates found")
        
        # Check first few matching templates
        for number in sorted(common_numbers)[:3]:
            de_content = de_templates[number].read_text()
            en_content = en_templates[number].read_text()
            
            de_headers = self.extract_section_headers(de_content)
            en_headers = self.extract_section_headers(en_content)
            
            # Check that header levels match
            de_levels = [level for level, _ in de_headers]
            en_levels = [level for level, _ in en_headers]
            
            assert de_levels == en_levels, \
                f"Template {number}: Header levels should match. " \
                f"DE: {de_levels}, EN: {en_levels}"
    
    def test_togaf_section_structure(self, template_base_path):
        """Test that TOGAF templates have matching section structure."""
        de_dir = template_base_path / "de" / "togaf"
        en_dir = template_base_path / "en" / "togaf"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("TOGAF templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {f.name[:4]: f for f in de_dir.glob("00[1-7]0_*.md")}
        en_templates = {f.name[:4]: f for f in en_dir.glob("00[1-7]0_*.md")}
        
        # Find common template numbers
        common_numbers = set(de_templates.keys()) & set(en_templates.keys())
        
        if not common_numbers:
            pytest.skip("No matching templates found")
        
        # Check first few matching templates
        for number in sorted(common_numbers)[:3]:
            de_content = de_templates[number].read_text()
            en_content = en_templates[number].read_text()
            
            de_headers = self.extract_section_headers(de_content)
            en_headers = self.extract_section_headers(en_content)
            
            # Check that header levels match
            de_levels = [level for level, _ in de_headers]
            en_levels = [level for level, _ in en_headers]
            
            assert de_levels == en_levels, \
                f"Template {number}: Header levels should match. " \
                f"DE: {de_levels}, EN: {en_levels}"
    
    def test_section_count_similarity(self, template_base_path):
        """Test that bilingual templates have similar section counts."""
        frameworks = [
            ('idw-ps-951', '00[1-5]0_*.md'),
            ('nist-csf', '00[1-6]0_*.md'),
            ('togaf', '00[1-7]0_*.md')
        ]
        
        for framework, pattern in frameworks:
            de_dir = template_base_path / "de" / framework
            en_dir = template_base_path / "en" / framework
            
            if not de_dir.exists() or not en_dir.exists():
                continue
            
            # Get matching template pairs
            de_templates = {f.name[:4]: f for f in de_dir.glob(pattern)}
            en_templates = {f.name[:4]: f for f in en_dir.glob(pattern)}
            
            common_numbers = set(de_templates.keys()) & set(en_templates.keys())
            
            for number in sorted(common_numbers)[:3]:
                de_content = de_templates[number].read_text()
                en_content = en_templates[number].read_text()
                
                de_headers = self.extract_section_headers(de_content)
                en_headers = self.extract_section_headers(en_content)
                
                # Section counts should be similar (within 20%)
                if len(de_headers) > 0 and len(en_headers) > 0:
                    ratio = min(len(de_headers), len(en_headers)) / max(len(de_headers), len(en_headers))
                    assert ratio > 0.8, \
                        f"{framework} template {number}: Section counts should be similar. " \
                        f"DE: {len(de_headers)}, EN: {len(en_headers)}"


class TestPlaceholderLocationMatching:
    """Unit tests for placeholder location matching across languages."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def extract_placeholders(self, content):
        """Extract placeholders from content."""
        pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        return pattern.findall(content)
    
    def test_idw_ps_951_placeholder_locations(self, template_base_path):
        """Test that IDW PS 951 templates have placeholders in matching locations."""
        de_dir = template_base_path / "de" / "idw-ps-951"
        en_dir = template_base_path / "en" / "idw-ps-951"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("IDW PS 951 templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {f.name[:4]: f for f in de_dir.glob("*.md")}
        en_templates = {f.name[:4]: f for f in en_dir.glob("*.md")}
        
        common_numbers = set(de_templates.keys()) & set(en_templates.keys())
        
        if not common_numbers:
            pytest.skip("No matching templates found")
        
        # Check templates for placeholder consistency
        for number in sorted(common_numbers)[:5]:
            de_content = de_templates[number].read_text()
            en_content = en_templates[number].read_text()
            
            de_placeholders = self.extract_placeholders(de_content)
            en_placeholders = self.extract_placeholders(en_content)
            
            # Extract just the source.field combinations
            de_refs = {f"{source}.{field}" for source, field in de_placeholders}
            en_refs = {f"{source}.{field}" for source, field in en_placeholders}
            
            # Placeholders should be the same (or very similar)
            # Allow for some differences due to language-specific content
            if de_refs or en_refs:
                common_refs = de_refs & en_refs
                # At least 70% of placeholders should be common
                if de_refs:
                    de_ratio = len(common_refs) / len(de_refs)
                    assert de_ratio > 0.7 or len(de_refs) <= 2, \
                        f"Template {number}: Most placeholders should match. " \
                        f"DE: {de_refs}, EN: {en_refs}"
    
    def test_nist_csf_placeholder_locations(self, template_base_path):
        """Test that NIST CSF templates have placeholders in matching locations."""
        de_dir = template_base_path / "de" / "nist-csf"
        en_dir = template_base_path / "en" / "nist-csf"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("NIST CSF templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {f.name[:4]: f for f in de_dir.glob("*.md")}
        en_templates = {f.name[:4]: f for f in en_dir.glob("*.md")}
        
        common_numbers = set(de_templates.keys()) & set(en_templates.keys())
        
        if not common_numbers:
            pytest.skip("No matching templates found")
        
        # Check templates for placeholder consistency
        for number in sorted(common_numbers)[:5]:
            de_content = de_templates[number].read_text()
            en_content = en_templates[number].read_text()
            
            de_placeholders = self.extract_placeholders(de_content)
            en_placeholders = self.extract_placeholders(en_content)
            
            # Extract just the source.field combinations
            de_refs = {f"{source}.{field}" for source, field in de_placeholders}
            en_refs = {f"{source}.{field}" for source, field in en_placeholders}
            
            # Placeholders should be the same (or very similar)
            if de_refs or en_refs:
                common_refs = de_refs & en_refs
                # At least 70% of placeholders should be common
                if de_refs:
                    de_ratio = len(common_refs) / len(de_refs)
                    assert de_ratio > 0.7 or len(de_refs) <= 2, \
                        f"Template {number}: Most placeholders should match. " \
                        f"DE: {de_refs}, EN: {en_refs}"
    
    def test_togaf_placeholder_locations(self, template_base_path):
        """Test that TOGAF templates have placeholders in matching locations."""
        de_dir = template_base_path / "de" / "togaf"
        en_dir = template_base_path / "en" / "togaf"
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip("TOGAF templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {f.name[:4]: f for f in de_dir.glob("*.md")}
        en_templates = {f.name[:4]: f for f in en_dir.glob("*.md")}
        
        common_numbers = set(de_templates.keys()) & set(en_templates.keys())
        
        if not common_numbers:
            pytest.skip("No matching templates found")
        
        # Check templates for placeholder consistency
        for number in sorted(common_numbers)[:5]:
            de_content = de_templates[number].read_text()
            en_content = en_templates[number].read_text()
            
            de_placeholders = self.extract_placeholders(de_content)
            en_placeholders = self.extract_placeholders(en_content)
            
            # Extract just the source.field combinations
            de_refs = {f"{source}.{field}" for source, field in de_placeholders}
            en_refs = {f"{source}.{field}" for source, field in en_placeholders}
            
            # Placeholders should be the same (or very similar)
            if de_refs or en_refs:
                common_refs = de_refs & en_refs
                # At least 70% of placeholders should be common
                if de_refs:
                    de_ratio = len(common_refs) / len(de_refs)
                    assert de_ratio > 0.7 or len(de_refs) <= 2, \
                        f"Template {number}: Most placeholders should match. " \
                        f"DE: {de_refs}, EN: {en_refs}"
    
    def test_metadata_placeholders_match(self, template_base_path):
        """Test that metadata templates have matching placeholders."""
        frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in frameworks:
            de_metadata = template_base_path / "de" / framework / f"0000_metadata_de_{framework}.md"
            en_metadata = template_base_path / "en" / framework / f"0000_metadata_en_{framework}.md"
            
            if not de_metadata.exists() or not en_metadata.exists():
                continue
            
            de_content = de_metadata.read_text()
            en_content = en_metadata.read_text()
            
            de_placeholders = self.extract_placeholders(de_content)
            en_placeholders = self.extract_placeholders(en_content)
            
            # Extract source.field combinations
            de_refs = {f"{source}.{field}" for source, field in de_placeholders}
            en_refs = {f"{source}.{field}" for source, field in en_placeholders}
            
            # Metadata placeholders should match exactly
            assert de_refs == en_refs, \
                f"{framework} metadata: Placeholders should match exactly. " \
                f"DE: {de_refs}, EN: {en_refs}"
