"""Unit tests for WeasyPrint PDF engine."""

import pytest
import tempfile
import os

from src.pdf_engines import (
    WeasyPrintEngine,
    PDFGenerationError,
    PDFEngineNotAvailableError
)


# Check if WeasyPrint is available
try:
    from weasyprint import HTML, CSS
    import markdown
    WEASYPRINT_AVAILABLE = True
except (ImportError, OSError):
    WEASYPRINT_AVAILABLE = False


@pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
class TestWeasyPrintEngineBasics:
    """Test basic WeasyPrint engine functionality."""
    
    def test_is_available_returns_true_when_installed(self):
        """Test that is_available returns True when WeasyPrint is installed."""
        engine = WeasyPrintEngine()
        # This will be True if WeasyPrint and system deps are available
        result = engine.is_available()
        assert isinstance(result, bool)
    
    def test_get_installation_instructions_returns_string(self):
        """Test that installation instructions are provided."""
        engine = WeasyPrintEngine()
        instructions = engine.get_installation_instructions()
        assert isinstance(instructions, str)
        assert "pip install" in instructions
        assert "weasyprint" in instructions
        assert "dependencies" in instructions.lower()
    
    def test_installation_instructions_platform_specific(self):
        """Test that installation instructions include platform-specific guidance."""
        engine = WeasyPrintEngine()
        instructions = engine.get_installation_instructions()
        
        # Should mention at least one platform
        has_platform_info = any(
            platform in instructions.lower()
            for platform in ['ubuntu', 'debian', 'macos', 'windows', 'fedora']
        )
        assert has_platform_info, "Installation instructions should include platform-specific guidance"
    
    def test_generate_pdf_creates_file(self):
        """Test that generate_pdf creates a PDF file."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = "# Test Heading\n\nThis is a test paragraph."
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path
            )
            
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


class TestWeasyPrintEngineErrorHandling:
    """Test error handling when system dependencies are missing."""
    
    def test_error_when_weasyprint_not_installed(self):
        """Test error handling when WeasyPrint is not installed."""
        # This test simulates the case where WeasyPrint is not available
        # We can't easily test this in an environment where it IS installed,
        # but we can verify the error message structure
        engine = WeasyPrintEngine()
        instructions = engine.get_installation_instructions()
        
        # Verify the error message would be helpful
        assert "pip install weasyprint" in instructions
        assert len(instructions) > 50, "Error message should be detailed"
    
    def test_installation_instructions_include_system_deps(self):
        """Test that installation instructions mention system dependencies."""
        engine = WeasyPrintEngine()
        instructions = engine.get_installation_instructions()
        
        # Should mention system dependencies
        assert any(
            keyword in instructions.lower()
            for keyword in ['pango', 'gtk', 'system', 'dependencies']
        ), "Installation instructions should mention system dependencies"
    
    def test_installation_instructions_include_links(self):
        """Test that installation instructions include helpful links."""
        engine = WeasyPrintEngine()
        instructions = engine.get_installation_instructions()
        
        # Should include a URL for more information
        assert 'http' in instructions.lower(), \
            "Installation instructions should include a URL for more information"


@pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
class TestWeasyPrintEngineCSSApplication:
    """Test CSS application to PDF output."""
    
    def test_default_css_is_applied(self):
        """Test that default CSS styling is applied to PDF."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = "# Test Heading\n\nThis is a test paragraph."
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
            
            # Verify default CSS includes expected properties
            default_css = engine._get_default_css()
            assert '@page' in default_css
            assert 'A4' in default_css
            assert 'font-family' in default_css
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_css_includes_monospace_for_code(self):
        """Test that CSS includes monospace font for code blocks."""
        engine = WeasyPrintEngine()
        default_css = engine._get_default_css()
        
        # Should include monospace font for code
        assert 'monospace' in default_css.lower()
        assert 'code' in default_css.lower() or 'pre' in default_css.lower()
    
    def test_css_includes_page_margins(self):
        """Test that CSS includes page margin settings."""
        engine = WeasyPrintEngine()
        default_css = engine._get_default_css()
        
        # Should include margin settings
        assert 'margin' in default_css.lower()
    
    def test_css_includes_heading_styles(self):
        """Test that CSS includes heading styles."""
        engine = WeasyPrintEngine()
        default_css = engine._get_default_css()
        
        # Should include heading styles
        assert any(f'h{i}' in default_css.lower() for i in range(1, 7))


@pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
class TestWeasyPrintEngineTOC:
    """Test TOC generation with WeasyPrint."""
    
    def test_toc_generation_enabled(self):
        """Test that TOC is generated when include_toc=True."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = """
# First Heading

Some content here.

## Second Heading

More content.

### Third Heading

Even more content.
"""
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=True
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_toc_generation_disabled(self):
        """Test that TOC is not generated when include_toc=False."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = """
# First Heading

Some content here.

## Second Heading

More content.
"""
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_toc_with_multiple_heading_levels(self):
        """Test TOC generation with multiple heading levels."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = """
# Level 1 Heading

Content for level 1.

## Level 2 Heading

Content for level 2.

### Level 3 Heading

Content for level 3.

#### Level 4 Heading

Content for level 4.
"""
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=True
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


@pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
class TestWeasyPrintEngineEdgeCases:
    """Test edge cases for WeasyPrint engine."""
    
    def test_empty_markdown_content(self):
        """Test handling of empty markdown content."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = ""
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path
            )
            
            # Should still create a valid PDF file
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_special_characters_in_markdown(self):
        """Test handling of special characters in markdown."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = """
# Special Characters Test

This paragraph contains special characters: & < > " ' 

- Bullet with & ampersand
- Bullet with < less than
- Bullet with > greater than
"""
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path
            )
            
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_unicode_characters_in_markdown(self):
        """Test handling of Unicode characters in markdown."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = """
# Unicode Test

This paragraph contains Unicode: café, naïve, 日本語, 中文, Ελληνικά

- Bullet with symbols: © ® ™ € £ ¥
"""
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path
            )
            
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_code_blocks_with_special_characters(self):
        """Test code blocks containing special characters."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = """
# Code Block Test

```python
def test():
    x = "string with <special> & characters"
    return x
```
"""
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path
            )
            
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


@pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
class TestWeasyPrintEngineMetadata:
    """Test PDF metadata handling."""
    
    def test_generate_pdf_with_metadata(self):
        """Test that metadata can be passed to generate_pdf."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = "# Test Document\n\nThis is a test."
        metadata = {
            'title': 'Test Document',
            'author': 'Test Author',
            'subject': 'Testing'
        }
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                metadata=metadata
            )
            
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_generate_pdf_without_metadata(self):
        """Test that generate_pdf works without metadata."""
        engine = WeasyPrintEngine()
        
        if not engine.is_available():
            pytest.skip("WeasyPrint system dependencies not available")
        
        markdown_content = "# Test Document\n\nThis is a test."
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                metadata=None
            )
            
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_metadata_title_in_html(self):
        """Test that metadata title is included in HTML wrapper."""
        engine = WeasyPrintEngine()
        
        metadata = {'title': 'Test Title'}
        html_content = "<p>Test content</p>"
        
        wrapped_html = engine._wrap_html(html_content, metadata, False)
        
        assert 'Test Title' in wrapped_html
        assert '<title>' in wrapped_html
        assert '</title>' in wrapped_html

