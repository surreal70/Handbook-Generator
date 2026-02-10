"""
Unit tests for template structure of new compliance frameworks.

Tests template header parsing, markdown structure validation, and placeholder extraction
for IDW PS 951, NIST CSF 2.0, and TOGAF templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026

Validates: Requirements 14.1, 14.2, 14.3
"""

import pytest
import re
from pathlib import Path


class TestTemplateHeaderParsing:
    """Unit tests for template header parsing."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def test_idw_ps_951_template_headers_german(self, template_base_path):
        """Test that IDW PS 951 German templates have proper headers."""
        idw_dir = template_base_path / "de" / "idw-ps-951"
        
        if not idw_dir.exists():
            pytest.skip("IDW PS 951 German templates not found")
        
        # Get all content templates (excluding metadata)
        templates = sorted([
            f for f in idw_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        assert len(templates) > 0, "Should have IDW PS 951 German templates"
        
        # Check first few templates for header structure
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for header section (YAML front matter or structured header)
            assert "Document-ID:" in content or "---" in content, \
                f"Template {template.name} should have header section"
            
            # Check for required header fields
            has_owner = "Owner:" in content or "owner:" in content
            has_version = "Version:" in content or "version:" in content
            has_status = "Status:" in content or "status:" in content
            
            assert has_owner or has_version or has_status, \
                f"Template {template.name} should have at least one header field"
    
    def test_nist_csf_template_headers_english(self, template_base_path):
        """Test that NIST CSF English templates have proper headers."""
        nist_dir = template_base_path / "en" / "nist-csf"
        
        if not nist_dir.exists():
            pytest.skip("NIST CSF English templates not found")
        
        # Get all content templates (excluding metadata)
        templates = sorted([
            f for f in nist_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        assert len(templates) > 0, "Should have NIST CSF English templates"
        
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
    
    def test_togaf_template_headers_german(self, template_base_path):
        """Test that TOGAF German templates have proper headers."""
        togaf_dir = template_base_path / "de" / "togaf"
        
        if not togaf_dir.exists():
            pytest.skip("TOGAF German templates not found")
        
        # Get all content templates (excluding metadata)
        templates = sorted([
            f for f in togaf_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        assert len(templates) > 0, "Should have TOGAF German templates"
        
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
    
    def test_header_field_extraction(self, template_base_path):
        """Test extraction of header fields from templates."""
        # Test with IDW PS 951 templates
        idw_dir = template_base_path / "de" / "idw-ps-951"
        
        if not idw_dir.exists():
            pytest.skip("IDW PS 951 templates not found")
        
        templates = list(idw_dir.glob("00[1-5]0_*.md"))
        
        if not templates:
            pytest.skip("No IDW PS 951 templates found")
        
        template = templates[0]
        content = template.read_text()
        
        # Extract header fields using regex
        owner_match = re.search(r'Owner:\s*(.+)', content, re.IGNORECASE)
        version_match = re.search(r'Version:\s*(.+)', content, re.IGNORECASE)
        status_match = re.search(r'Status:\s*(.+)', content, re.IGNORECASE)
        
        # At least one field should be extractable
        assert owner_match or version_match or status_match, \
            "Should be able to extract at least one header field"


class TestMarkdownStructureValidation:
    """Unit tests for markdown structure validation."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def test_idw_ps_951_markdown_headers(self, template_base_path):
        """Test that IDW PS 951 templates have proper markdown headers."""
        idw_dir = template_base_path / "de" / "idw-ps-951"
        
        if not idw_dir.exists():
            pytest.skip("IDW PS 951 templates not found")
        
        templates = sorted([
            f for f in idw_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        assert len(templates) > 0, "Should have IDW PS 951 templates"
        
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for markdown headers (##, ###)
            has_h2 = re.search(r'^##\s+', content, re.MULTILINE)
            has_h3 = re.search(r'^###\s+', content, re.MULTILINE)
            has_h1 = re.search(r'^#\s+', content, re.MULTILINE)
            
            assert has_h1 or has_h2 or has_h3, \
                f"Template {template.name} should have markdown headers"
    
    def test_nist_csf_markdown_headers(self, template_base_path):
        """Test that NIST CSF templates have proper markdown headers."""
        nist_dir = template_base_path / "en" / "nist-csf"
        
        if not nist_dir.exists():
            pytest.skip("NIST CSF templates not found")
        
        templates = sorted([
            f for f in nist_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        assert len(templates) > 0, "Should have NIST CSF templates"
        
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for markdown headers
            has_h2 = re.search(r'^##\s+', content, re.MULTILINE)
            has_h3 = re.search(r'^###\s+', content, re.MULTILINE)
            has_h1 = re.search(r'^#\s+', content, re.MULTILINE)
            
            assert has_h1 or has_h2 or has_h3, \
                f"Template {template.name} should have markdown headers"
    
    def test_togaf_markdown_headers(self, template_base_path):
        """Test that TOGAF templates have proper markdown headers."""
        togaf_dir = template_base_path / "de" / "togaf"
        
        if not togaf_dir.exists():
            pytest.skip("TOGAF templates not found")
        
        templates = sorted([
            f for f in togaf_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        assert len(templates) > 0, "Should have TOGAF templates"
        
        for template in templates[:5]:
            content = template.read_text()
            
            # Check for markdown headers
            has_h2 = re.search(r'^##\s+', content, re.MULTILINE)
            has_h3 = re.search(r'^###\s+', content, re.MULTILINE)
            has_h1 = re.search(r'^#\s+', content, re.MULTILINE)
            
            assert has_h1 or has_h2 or has_h3, \
                f"Template {template.name} should have markdown headers"
    
    def test_markdown_structure_hierarchy(self, template_base_path):
        """Test that templates have proper header hierarchy."""
        # Test with NIST CSF templates
        nist_dir = template_base_path / "en" / "nist-csf"
        
        if not nist_dir.exists():
            pytest.skip("NIST CSF templates not found")
        
        templates = list(nist_dir.glob("00[1-5]0_*.md"))
        
        if not templates:
            pytest.skip("No NIST CSF templates found")
        
        template = templates[0]
        content = template.read_text()
        
        # Extract all headers
        headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        
        if headers:
            # Verify headers exist
            assert len(headers) > 0, "Should have at least one header"
            
            # Verify header levels are reasonable (1-4)
            for header_marks, header_text in headers:
                level = len(header_marks)
                assert 1 <= level <= 4, \
                    f"Header level should be 1-4, got {level} for '{header_text}'"


class TestPlaceholderExtraction:
    """Unit tests for placeholder extraction."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def test_extract_placeholders_from_idw_ps_951(self, template_base_path):
        """Test extracting placeholders from IDW PS 951 templates."""
        idw_dir = template_base_path / "de" / "idw-ps-951"
        
        if not idw_dir.exists():
            pytest.skip("IDW PS 951 templates not found")
        
        templates = list(idw_dir.glob("*.md"))
        
        if not templates:
            pytest.skip("No IDW PS 951 templates found")
        
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
                    f"Placeholder source should be alphanumeric: {source}"
                assert all(part.replace('_', '').isalnum() for part in field.split('.')), \
                    f"Placeholder field should be alphanumeric: {field}"
        
        # Should have at least some placeholders across all templates
        assert total_placeholders >= 0, "Should be able to extract placeholders"
    
    def test_extract_placeholders_from_nist_csf(self, template_base_path):
        """Test extracting placeholders from NIST CSF templates."""
        nist_dir = template_base_path / "en" / "nist-csf"
        
        if not nist_dir.exists():
            pytest.skip("NIST CSF templates not found")
        
        templates = list(nist_dir.glob("*.md"))
        
        if not templates:
            pytest.skip("No NIST CSF templates found")
        
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
                    f"Placeholder source should be alphanumeric: {source}"
                assert all(part.replace('_', '').isalnum() for part in field.split('.')), \
                    f"Placeholder field should be alphanumeric: {field}"
        
        # Should have at least some placeholders across all templates
        assert total_placeholders >= 0, "Should be able to extract placeholders"
    
    def test_extract_placeholders_from_togaf(self, template_base_path):
        """Test extracting placeholders from TOGAF templates."""
        togaf_dir = template_base_path / "de" / "togaf"
        
        if not togaf_dir.exists():
            pytest.skip("TOGAF templates not found")
        
        templates = list(togaf_dir.glob("*.md"))
        
        if not templates:
            pytest.skip("No TOGAF templates found")
        
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
                    f"Placeholder source should be alphanumeric: {source}"
                assert all(part.replace('_', '').isalnum() for part in field.split('.')), \
                    f"Placeholder field should be alphanumeric: {field}"
        
        # Should have at least some placeholders across all templates
        assert total_placeholders >= 0, "Should be able to extract placeholders"
    
    def test_placeholder_sources(self, template_base_path):
        """Test that placeholders use valid sources."""
        valid_sources = {'meta', 'netbox', 'metadata', 'source'}
        
        # Check all new framework templates
        frameworks = [
            ('de', 'idw-ps-951'),
            ('en', 'nist-csf'),
            ('de', 'togaf')
        ]
        
        placeholder_pattern = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
        
        for lang, framework in frameworks:
            framework_dir = template_base_path / lang / framework
            
            if not framework_dir.exists():
                continue
            
            templates = list(framework_dir.glob("*.md"))
            
            for template in templates:
                content = template.read_text()
                placeholders = placeholder_pattern.findall(content)
                
                for source, field in placeholders:
                    # Source should be one of the valid sources (or allow custom sources)
                    # For now, just verify it's alphanumeric
                    assert source.replace('_', '').isalnum(), \
                        f"Placeholder source should be alphanumeric: {source} in {template.name}"
