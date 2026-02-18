"""
Unit tests for bilingual consistency of Phase 2 compliance frameworks.

Tests filename matching, section structure matching, and placeholder location matching
for ISO/IEC 38500, ISO 31000, CSA CCM, TISAX, SOC 1, COSO, and DORA templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2025, 2026

Validates: Requirements 14.6
"""

import pytest
import re
from pathlib import Path


# Phase 2 frameworks
PHASE2_FRAMEWORKS = [
    ('iso-38500', 'ISO/IEC 38500'),
    ('iso-31000', 'ISO 31000'),
    ('csa-ccm', 'CSA CCM'),
    ('tisax', 'TISAX'),
    ('soc1', 'SOC 1'),
    ('coso', 'COSO'),
    ('dora', 'DORA')
]


class TestPhase2FilenameMatching:
    """Unit tests for Phase 2 filename matching across languages."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_filename_matching(self, template_base_path, framework, display_name):
        """Test that German and English templates have matching filenames."""
        de_dir = template_base_path / "de" / framework
        en_dir = template_base_path / "en" / framework
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip(f"{display_name} templates not found in both languages")
        
        # Get all template files (excluding language-specific metadata)
        de_templates = {
            f.name for f in de_dir.glob("*.md")
            if not f.name.startswith("0000_metadata_de_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
        }
        
        en_templates = {
            f.name for f in en_dir.glob("*.md")
            if not f.name.startswith("0000_metadata_en_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
        }
        
        # Check for missing templates
        missing_in_english = de_templates - en_templates
        missing_in_german = en_templates - de_templates
        
        assert len(missing_in_english) == 0, \
            f"{display_name}: German templates missing in English: {missing_in_english}"
        assert len(missing_in_german) == 0, \
            f"{display_name}: English templates missing in German: {missing_in_german}"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_metadata_files_exist(self, template_base_path, framework, display_name):
        """Test that metadata files exist in both languages."""
        de_metadata = template_base_path / "de" / framework / f"0000_metadata_de_{framework}.md"
        en_metadata = template_base_path / "en" / framework / f"0000_metadata_en_{framework}.md"
        
        if not (template_base_path / "de" / framework).exists():
            pytest.skip(f"{display_name} German templates not found")
        
        if not (template_base_path / "en" / framework).exists():
            pytest.skip(f"{display_name} English templates not found")
        
        assert de_metadata.exists(), f"{display_name}: German metadata template should exist"
        assert en_metadata.exists(), f"{display_name}: English metadata template should exist"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_documentation_files_exist(self, template_base_path, framework, display_name):
        """Test that documentation files exist in both languages."""
        de_readme = template_base_path / "de" / framework / "README.md"
        en_readme = template_base_path / "en" / framework / "README.md"
        de_mapping = template_base_path / "de" / framework / "9999_Framework_Mapping.md"
        en_mapping = template_base_path / "en" / framework / "9999_Framework_Mapping.md"
        
        if not (template_base_path / "de" / framework).exists():
            pytest.skip(f"{display_name} German templates not found")
        
        if not (template_base_path / "en" / framework).exists():
            pytest.skip(f"{display_name} English templates not found")
        
        assert de_readme.exists(), f"{display_name}: German README should exist"
        assert en_readme.exists(), f"{display_name}: English README should exist"
        assert de_mapping.exists(), f"{display_name}: German 9999_Framework_Mapping should exist"
        assert en_mapping.exists(), f"{display_name}: English 9999_Framework_Mapping should exist"


class TestPhase2SectionStructureMatching:
    """Unit tests for Phase 2 section structure matching across languages."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def extract_section_headers(self, content):
        """Extract section headers from template content."""
        # Extract all markdown headers
        headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        return [(len(marks), text.strip()) for marks, text in headers]
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_section_structure_matching(self, template_base_path, framework, display_name):
        """Test that German and English templates have matching section structure."""
        de_dir = template_base_path / "de" / framework
        en_dir = template_base_path / "en" / framework
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip(f"{display_name} templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {
            f.name: f for f in de_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
        }
        
        en_templates = {
            f.name: f for f in en_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
        }
        
        # Check first few matching templates
        matching_names = sorted(set(de_templates.keys()) & set(en_templates.keys()))[:5]
        
        for template_name in matching_names:
            de_content = de_templates[template_name].read_text()
            en_content = en_templates[template_name].read_text()
            
            de_headers = self.extract_section_headers(de_content)
            en_headers = self.extract_section_headers(en_content)
            
            # Check that header counts match
            assert len(de_headers) == len(en_headers), \
                f"{display_name} {template_name}: Header count mismatch (DE: {len(de_headers)}, EN: {len(en_headers)})"
            
            # Check that header levels match
            de_levels = [level for level, _ in de_headers]
            en_levels = [level for level, _ in en_headers]
            
            assert de_levels == en_levels, \
                f"{display_name} {template_name}: Header level structure mismatch"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_header_hierarchy_consistency(self, template_base_path, framework, display_name):
        """Test that header hierarchy is consistent across languages."""
        de_dir = template_base_path / "de" / framework
        en_dir = template_base_path / "en" / framework
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip(f"{display_name} templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {
            f.name: f for f in de_dir.glob("00[1-5]0_*.md")
        }
        
        en_templates = {
            f.name: f for f in en_dir.glob("00[1-5]0_*.md")
        }
        
        matching_names = sorted(set(de_templates.keys()) & set(en_templates.keys()))
        
        if not matching_names:
            pytest.skip(f"No matching {display_name} templates found")
        
        # Check first matching template
        template_name = matching_names[0]
        de_content = de_templates[template_name].read_text()
        en_content = en_templates[template_name].read_text()
        
        de_headers = self.extract_section_headers(de_content)
        en_headers = self.extract_section_headers(en_content)
        
        # Verify both have headers
        assert len(de_headers) > 0, f"{display_name}: German template should have headers"
        assert len(en_headers) > 0, f"{display_name}: English template should have headers"
        
        # Verify header structure matches
        assert len(de_headers) == len(en_headers), \
            f"{display_name}: Header count should match between languages"


class TestPhase2PlaceholderLocationMatching:
    """Unit tests for Phase 2 placeholder location matching across languages."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def extract_placeholders(self, content):
        """Extract placeholders from template content."""
        placeholder_pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        return placeholder_pattern.findall(content)
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_placeholder_location_matching(self, template_base_path, framework, display_name):
        """Test that German and English templates have matching placeholder locations."""
        de_dir = template_base_path / "de" / framework
        en_dir = template_base_path / "en" / framework
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip(f"{display_name} templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {
            f.name: f for f in de_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
        }
        
        en_templates = {
            f.name: f for f in en_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
        }
        
        # Check first few matching templates
        matching_names = sorted(set(de_templates.keys()) & set(en_templates.keys()))[:5]
        
        for template_name in matching_names:
            de_content = de_templates[template_name].read_text()
            en_content = en_templates[template_name].read_text()
            
            de_placeholders = self.extract_placeholders(de_content)
            en_placeholders = self.extract_placeholders(en_content)
            
            # Convert to sets of placeholder identifiers (source.field)
            de_placeholder_set = {f"{source}.{field}" for source, field in de_placeholders}
            en_placeholder_set = {f"{source}.{field}" for source, field in en_placeholders}
            
            # Check that placeholder sets match
            assert de_placeholder_set == en_placeholder_set, \
                f"{display_name} {template_name}: Placeholder mismatch\n" \
                f"DE only: {de_placeholder_set - en_placeholder_set}\n" \
                f"EN only: {en_placeholder_set - de_placeholder_set}"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_placeholder_count_consistency(self, template_base_path, framework, display_name):
        """Test that placeholder counts are consistent across languages."""
        de_dir = template_base_path / "de" / framework
        en_dir = template_base_path / "en" / framework
        
        if not de_dir.exists() or not en_dir.exists():
            pytest.skip(f"{display_name} templates not found in both languages")
        
        # Get matching template pairs
        de_templates = {
            f.name: f for f in de_dir.glob("00[1-5]0_*.md")
        }
        
        en_templates = {
            f.name: f for f in en_dir.glob("00[1-5]0_*.md")
        }
        
        matching_names = sorted(set(de_templates.keys()) & set(en_templates.keys()))
        
        if not matching_names:
            pytest.skip(f"No matching {display_name} templates found")
        
        # Check first matching template
        template_name = matching_names[0]
        de_content = de_templates[template_name].read_text()
        en_content = en_templates[template_name].read_text()
        
        de_placeholders = self.extract_placeholders(de_content)
        en_placeholders = self.extract_placeholders(en_content)
        
        # Verify placeholder counts match
        assert len(de_placeholders) == len(en_placeholders), \
            f"{display_name} {template_name}: Placeholder count mismatch " \
            f"(DE: {len(de_placeholders)}, EN: {len(en_placeholders)})"


class TestPhase2ComprehensiveBilingualConsistency:
    """Comprehensive bilingual consistency tests for Phase 2."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def test_all_phase2_frameworks_have_bilingual_support(self, template_base_path):
        """Test that all Phase 2 frameworks have both German and English versions."""
        for framework, display_name in PHASE2_FRAMEWORKS:
            de_dir = template_base_path / "de" / framework
            en_dir = template_base_path / "en" / framework
            
            assert de_dir.exists(), f"{display_name}: German template directory should exist"
            assert en_dir.exists(), f"{display_name}: English template directory should exist"
            
            # Check that both have templates
            de_templates = list(de_dir.glob("*.md"))
            en_templates = list(en_dir.glob("*.md"))
            
            assert len(de_templates) > 0, f"{display_name}: Should have German templates"
            assert len(en_templates) > 0, f"{display_name}: Should have English templates"
    
    def test_phase2_diagrams_directories_exist(self, template_base_path):
        """Test that diagrams directories exist for all Phase 2 frameworks."""
        for framework, display_name in PHASE2_FRAMEWORKS:
            de_diagrams = template_base_path / "de" / framework / "diagrams"
            en_diagrams = template_base_path / "en" / framework / "diagrams"
            
            if not (template_base_path / "de" / framework).exists():
                continue
            
            if not (template_base_path / "en" / framework).exists():
                continue
            
            assert de_diagrams.exists(), f"{display_name}: German diagrams directory should exist"
            assert en_diagrams.exists(), f"{display_name}: English diagrams directory should exist"
    
    def test_phase2_template_count_balance(self, template_base_path):
        """Test that German and English template counts are balanced."""
        for framework, display_name in PHASE2_FRAMEWORKS:
            de_dir = template_base_path / "de" / framework
            en_dir = template_base_path / "en" / framework
            
            if not de_dir.exists() or not en_dir.exists():
                continue
            
            # Count content templates (excluding metadata, README, 9999_Framework_Mapping)
            de_count = len([
                f for f in de_dir.glob("*.md")
                if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
            ])
            
            en_count = len([
                f for f in en_dir.glob("*.md")
                if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "9999_Framework_Mapping.md"
            ])
            
            assert de_count == en_count, \
                f"{display_name}: Template count mismatch (DE: {de_count}, EN: {en_count})"
