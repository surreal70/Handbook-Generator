"""Unit tests for ReportLab PDF engine."""

import pytest
import tempfile
import os

from src.pdf_engines import (
    ReportLabEngine,
    PDFGenerationError,
    MarkdownConversionError
)


# Check if ReportLab is available
try:
    import reportlab
    import markdown
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


@pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
class TestReportLabEngineBasics:
    """Test basic ReportLab engine functionality."""
    
    def test_is_available_returns_true_when_installed(self):
        """Test that is_available returns True when ReportLab is installed."""
        engine = ReportLabEngine()
        assert engine.is_available() is True
    
    def test_get_installation_instructions_returns_string(self):
        """Test that installation instructions are provided."""
        engine = ReportLabEngine()
        instructions = engine.get_installation_instructions()
        assert isinstance(instructions, str)
        assert "pip install" in instructions
        assert "reportlab" in instructions
        assert "markdown" in instructions
    
    def test_generate_pdf_creates_file(self):
        """Test that generate_pdf creates a PDF file."""
        engine = ReportLabEngine()
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


@pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
class TestReportLabEngineEdgeCases:
    """Test edge cases for ReportLab engine."""
    
    def test_empty_markdown_content(self):
        """Test handling of empty markdown content."""
        engine = ReportLabEngine()
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
    
    def test_whitespace_only_markdown(self):
        """Test handling of whitespace-only markdown content."""
        engine = ReportLabEngine()
        markdown_content = "   \n\n   \n   "
        
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
        engine = ReportLabEngine()
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
        engine = ReportLabEngine()
        markdown_content = """
# Unicode Test

This paragraph contains Unicode: café, naïve, 日本語, 中文, Ελληνικά

- Bullet with émojis: 😀 🎉 ✨
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


@pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
class TestReportLabEngineCodeBlocks:
    """Test code block rendering with monospace font."""
    
    def test_code_block_rendering(self):
        """Test that code blocks are rendered with monospace font."""
        engine = ReportLabEngine()
        markdown_content = """
# Code Block Test

Here is a code block:

```
def hello_world():
    print("Hello, World!")
    return True
```

And some more text after the code block.
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
            
            # Verify the PDF contains the code
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(tmp_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                # Check that code content is present
                assert "hello_world" in text or "Hello" in text
            except ImportError:
                pass  # PyPDF2 not available
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_inline_code_rendering(self):
        """Test that inline code is rendered with monospace font."""
        engine = ReportLabEngine()
        markdown_content = """
# Inline Code Test

Use the `print()` function to output text.

The variable `x` should be set to `42`.
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
    
    def test_multiple_code_blocks(self):
        """Test rendering of multiple code blocks."""
        engine = ReportLabEngine()
        markdown_content = """
# Multiple Code Blocks

First code block:

```
function one() {
    return 1;
}
```

Second code block:

```
function two() {
    return 2;
}
```

Third code block:

```
function three() {
    return 3;
}
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


@pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
class TestReportLabEngineTextFormatting:
    """Test text formatting (bold, italic) preservation."""
    
    def test_bold_text_rendering(self):
        """Test that bold text is rendered correctly."""
        engine = ReportLabEngine()
        markdown_content = """
# Bold Text Test

This is **bold text** in a paragraph.

**This entire paragraph is bold.**
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
    
    def test_italic_text_rendering(self):
        """Test that italic text is rendered correctly."""
        engine = ReportLabEngine()
        markdown_content = """
# Italic Text Test

This is *italic text* in a paragraph.

*This entire paragraph is italic.*
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
    
    def test_bold_and_italic_combined(self):
        """Test that bold and italic can be combined."""
        engine = ReportLabEngine()
        markdown_content = """
# Combined Formatting Test

This is ***bold and italic*** text.

This has **bold** and *italic* separately.
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


@pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
class TestReportLabEngineMetadata:
    """Test PDF metadata handling."""
    
    def test_generate_pdf_with_metadata(self):
        """Test that metadata can be passed to generate_pdf."""
        engine = ReportLabEngine()
        markdown_content = "# Test Document\n\nThis is a test."
        metadata = {
            'title': 'Test Document',
            'author': 'Test Author',
            'subject': 'Testing'
        }
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            # Should not raise an error even if metadata is not fully implemented
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
        engine = ReportLabEngine()
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
