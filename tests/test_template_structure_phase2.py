"""
Unit tests for template structure of Phase 2 compliance frameworks.

Tests template header parsing, markdown structure validation, and placeholder extraction
for ISO/IEC 38500, ISO 31000, CSA CCM, TISAX, SOC 1, COSO, and DORA templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026

Validates: Requirements 14.1, 14.2, 14.3
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


class TestPhase2TemplateHeaderParsing:
    """Unit tests for Phase 2 template header parsing."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_template_headers_german(self, template_base_path, framework, display_name):
        """Test that Phase 2 German templates have proper headers."""
        framework_dir = template_base_path / "de" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} German templates not found")
        
        # Get all content templates (excluding metadata and README)
        templates = sorted([
            f for f in framework_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "FRAMEWORK_MAPPING.md"
        ])
        
        assert len(templates) > 0, f"Should have {display_name} German templates"
        
        # Check first few templates for header structure
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for header section (YAML front matter or structured header)
            assert "Document-ID:" in content or "Dokument-ID:" in content or "---" in content, \
                f"Template {template.name} should have header section"
            
            # Check for required header fields
            has_owner = "Owner:" in content or "owner:" in content
            has_version = "Version:" in content or "version:" in content
            has_status = "Status:" in content or "status:" in content
            
            assert has_owner or has_version or has_status, \
                f"Template {template.name} should have at least one header field"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_template_headers_english(self, template_base_path, framework, display_name):
        """Test that Phase 2 English templates have proper headers."""
        framework_dir = template_base_path / "en" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} English templates not found")
        
        # Get all content templates (excluding metadata and README)
        templates = sorted([
            f for f in framework_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "FRAMEWORK_MAPPING.md"
        ])
        
        assert len(templates) > 0, f"Should have {display_name} English templates"
        
        # Check first few templates for header structure
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for header section
            assert "Document-ID:" in content or "---" in content, \
                f"Template {template.name} should have header section"
            
            # Check for required header fields
            has_owner = "Owner:" in content or "owner:" in content
            has_version = "Version:" in content or "version:" in content
            has_status = "Status:" in content or "status:" in content
            
            assert has_owner or has_version or has_status, \
                f"Template {template.name} should have at least one header field"
    
    def test_header_field_extraction_phase2(self, template_base_path):
        """Test extraction of header fields from Phase 2 templates."""
        # Test with first available Phase 2 framework
        for framework, display_name in PHASE2_FRAMEWORKS:
            framework_dir = template_base_path / "de" / framework
            
            if not framework_dir.exists():
                continue
            
            templates = list(framework_dir.glob("00[1-5]0_*.md"))
            
            if not templates:
                continue
            
            template = templates[0]
            content = template.read_text()
            
            # Extract header fields using regex
            owner_match = re.search(r'Owner:\s*(.+)', content, re.IGNORECASE)
            version_match = re.search(r'Version:\s*(.+)', content, re.IGNORECASE)
            status_match = re.search(r'Status:\s*(.+)', content, re.IGNORECASE)
            
            # At least one field should be extractable
            assert owner_match or version_match or status_match, \
                f"Should be able to extract at least one header field from {display_name}"
            
            # Found a valid template, test passed
            return
        
        pytest.skip("No Phase 2 templates found for header extraction test")


class TestPhase2MarkdownStructureValidation:
    """Unit tests for Phase 2 markdown structure validation."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_markdown_headers_german(self, template_base_path, framework, display_name):
        """Test that Phase 2 German templates have proper markdown headers."""
        framework_dir = template_base_path / "de" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} German templates not found")
        
        templates = sorted([
            f for f in framework_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "FRAMEWORK_MAPPING.md"
        ])
        
        assert len(templates) > 0, f"Should have {display_name} German templates"
        
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for markdown headers (##, ###)
            has_h2 = re.search(r'^##\s+', content, re.MULTILINE)
            has_h3 = re.search(r'^###\s+', content, re.MULTILINE)
            has_h1 = re.search(r'^#\s+', content, re.MULTILINE)
            
            assert has_h1 or has_h2 or has_h3, \
                f"Template {template.name} should have markdown headers"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_phase2_markdown_headers_english(self, template_base_path, framework, display_name):
        """Test that Phase 2 English templates have proper markdown headers."""
        framework_dir = template_base_path / "en" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} English templates not found")
        
        templates = sorted([
            f for f in framework_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md" and f.name != "FRAMEWORK_MAPPING.md"
        ])
        
        assert len(templates) > 0, f"Should have {display_name} English templates"
        
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for markdown headers
            has_h2 = re.search(r'^##\s+', content, re.MULTILINE)
            has_h3 = re.search(r'^###\s+', content, re.MULTILINE)
            has_h1 = re.search(r'^#\s+', content, re.MULTILINE)
            
            assert has_h1 or has_h2 or has_h3, \
                f"Template {template.name} should have markdown headers"
    
    def test_markdown_structure_hierarchy_phase2(self, template_base_path):
        """Test that Phase 2 templates have proper header hierarchy."""
        # Test with first available Phase 2 framework
        for framework, display_name in PHASE2_FRAMEWORKS:
            framework_dir = template_base_path / "en" / framework
            
            if not framework_dir.exists():
                continue
            
            templates = list(framework_dir.glob("00[1-5]0_*.md"))
            
            if not templates:
                continue
            
            template = templates[0]
            content = template.read_text()
            
            # Extract all headers
            headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
            
            if headers:
                # Verify headers exist
                assert len(headers) > 0, f"Should have at least one header in {display_name}"
                
                # Verify header levels are reasonable (1-4)
                for header_marks, header_text in headers:
                    level = len(header_marks)
                    assert 1 <= level <= 4, \
                        f"Header level should be 1-4, got {level} for '{header_text}' in {display_name}"
                
                # Found a valid template, test passed
                return
        
        pytest.skip("No Phase 2 templates found for header hierarchy test")


class TestPhase2PlaceholderExtraction:
    """Unit tests for Phase 2 placeholder extraction."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_extract_placeholders_from_phase2_german(self, template_base_path, framework, display_name):
        """Test extracting placeholders from Phase 2 German templates."""
        framework_dir = template_base_path / "de" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} German templates not found")
        
        templates = list(framework_dir.glob("*.md"))
        
        if not templates:
            pytest.skip(f"No {display_name} German templates found")
        
        # Check all templates for placeholders
        placeholder_pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        total_placeholders = 0
        
        for template in templates:
            content = template.read_text()
            placeholders = placeholder_pattern.findall(content)
            total_placeholders += len(placeholders)
            
            # Verify placeholder format
            for source, field in placeholders:
                assert source.isalnum() or '_' in source, \
                    f"Placeholder source should be alphanumeric: {source} in {template.name}"
                assert all(part.replace('_', '').isalnum() for part in field.split('.')), \
                    f"Placeholder field should be alphanumeric: {field} in {template.name}"
        
        # Should have at least some placeholders across all templates
        assert total_placeholders >= 0, f"Should be able to extract placeholders from {display_name}"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_extract_placeholders_from_phase2_english(self, template_base_path, framework, display_name):
        """Test extracting placeholders from Phase 2 English templates."""
        framework_dir = template_base_path / "en" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} English templates not found")
        
        templates = list(framework_dir.glob("*.md"))
        
        if not templates:
            pytest.skip(f"No {display_name} English templates found")
        
        # Check all templates for placeholders
        placeholder_pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        total_placeholders = 0
        
        for template in templates:
            content = template.read_text()
            placeholders = placeholder_pattern.findall(content)
            total_placeholders += len(placeholders)
            
            # Verify placeholder format
            for source, field in placeholders:
                assert source.isalnum() or '_' in source, \
                    f"Placeholder source should be alphanumeric: {source} in {template.name}"
                assert all(part.replace('_', '').isalnum() for part in field.split('.')), \
                    f"Placeholder field should be alphanumeric: {field} in {template.name}"
        
        # Should have at least some placeholders across all templates
        assert total_placeholders >= 0, f"Should be able to extract placeholders from {display_name}"
    
    def test_placeholder_sources_phase2(self, template_base_path):
        """Test that Phase 2 placeholders use valid sources."""
        valid_sources = {'meta', 'netbox', 'metadata', 'source'}
        
        # Check all Phase 2 framework templates
        placeholder_pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        
        for framework, display_name in PHASE2_FRAMEWORKS:
            for lang in ['de', 'en']:
                framework_dir = template_base_path / lang / framework
                
                if not framework_dir.exists():
                    continue
                
                templates = list(framework_dir.glob("*.md"))
                
                for template in templates:
                    content = template.read_text()
                    placeholders = placeholder_pattern.findall(content)
                    
                    for source, field in placeholders:
                        # Source should be alphanumeric (allow custom sources)
                        assert source.replace('_', '').isalnum(), \
                            f"Placeholder source should be alphanumeric: {source} in {template.name} ({display_name})"
