"""Integration tests for end-to-end PDF generation workflows."""

import pytest
import tempfile
import os

from src.pdf_engines import (
    EngineType,
    PDFEngineFactory,
    ReportLabEngine,
    WeasyPrintEngine,
    PDFEngineNotAvailableError
)


# Check engine availability
REPORTLAB_AVAILABLE = ReportLabEngine().is_available()
WEASYPRINT_AVAILABLE = WeasyPrintEngine().is_available()


class TestEndToEndWorkflows:
    """
    Integration tests for complete PDF generation workflows.
    
    Validates: Requirements 5.1, 5.2, 5.4
    
    These tests verify complete workflows from markdown input to PDF output,
    including engine selection, TOC generation, and auto-detection.
    """
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_complete_workflow_markdown_to_reportlab_pdf(self):
        """
        Test complete workflow: markdown → ReportLab → PDF
        
        Validates: Requirements 5.1, 5.4
        """
        # Prepare markdown content
        markdown_content = """
# Introduction

This is a test document for the ReportLab PDF engine.

## Section 1

This section contains some basic text to verify that the PDF generation
works correctly from end to end.

### Subsection 1.1

Here we have a subsection with some additional content.

## Section 2

This section includes a code block:

```python
def hello_world():
    print("Hello, World!")
```

And some **bold text** and *italic text*.

## Conclusion

This concludes our test document.
"""
        
        # Create engine using factory
        engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
        
        # Generate PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path), "PDF file was not created"
            assert os.path.getsize(tmp_path) > 0, "PDF file is empty"
            
            # Verify it's a valid PDF
            with open(tmp_path, 'rb') as f:
                header = f.read(5)
                assert header == b'%PDF-', "File is not a valid PDF"
            
            # Verify PDF has content (multiple pages expected)
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(tmp_path)
                assert len(reader.pages) >= 1, "PDF should have at least one page"
                
                # Extract text and verify some content is present
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                assert "Introduction" in text, "PDF should contain heading text"
                assert "Section 1" in text, "PDF should contain section text"
            except ImportError:
                pass  # PyPDF2 not available, skip content verification
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
    def test_complete_workflow_markdown_to_weasyprint_pdf(self):
        """
        Test complete workflow: markdown → WeasyPrint → PDF
        
        Validates: Requirements 5.1, 5.4
        """
        # Prepare markdown content
        markdown_content = """
# Introduction

This is a test document for the WeasyPrint PDF engine.

## Section 1

This section contains some basic text to verify that the PDF generation
works correctly from end to end.

### Subsection 1.1

Here we have a subsection with some additional content.

## Section 2

This section includes a code block:

```python
def hello_world():
    print("Hello, World!")
```

And some **bold text** and *italic text*.

## Conclusion

This concludes our test document.
"""
        
        # Create engine using factory
        engine = PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
        
        # Generate PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path), "PDF file was not created"
            assert os.path.getsize(tmp_path) > 0, "PDF file is empty"
            
            # Verify it's a valid PDF
            with open(tmp_path, 'rb') as f:
                header = f.read(5)
                assert header == b'%PDF-', "File is not a valid PDF"
            
            # Verify PDF has content
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(tmp_path)
                assert len(reader.pages) >= 1, "PDF should have at least one page"
                
                # Extract text and verify some content is present
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                assert "Introduction" in text, "PDF should contain heading text"
                assert "Section 1" in text, "PDF should contain section text"
            except ImportError:
                pass  # PyPDF2 not available, skip content verification
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_complete_workflow_with_toc_enabled(self):
        """
        Test complete workflow with TOC enabled
        
        Validates: Requirements 5.2
        """
        # Prepare markdown content with multiple sections
        markdown_content = """
# Chapter 1: Introduction

This is the introduction chapter.

## Section 1.1

First section content.

## Section 1.2

Second section content.

# Chapter 2: Main Content

This is the main content chapter.

## Section 2.1

Main content section.

### Subsection 2.1.1

Detailed subsection.

# Chapter 3: Conclusion

This is the conclusion chapter.
"""
        
        # Create engine using factory
        engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
        
        # Generate PDF with TOC enabled
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=True
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path), "PDF file was not created"
            assert os.path.getsize(tmp_path) > 0, "PDF file is empty"
            
            # Verify it's a valid PDF
            with open(tmp_path, 'rb') as f:
                header = f.read(5)
                assert header == b'%PDF-', "File is not a valid PDF"
            
            # Verify PDF has multiple pages (TOC + content)
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(tmp_path)
                # With TOC enabled, we should have at least 2 pages
                assert len(reader.pages) >= 2, \
                    f"Expected at least 2 pages with TOC, got {len(reader.pages)}"
                
                # Extract text from all pages
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                # Verify content is present
                assert "Chapter 1" in text, "PDF should contain chapter headings"
                assert "Introduction" in text, "PDF should contain content"
            except ImportError:
                pass  # PyPDF2 not available, skip verification
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @pytest.mark.skipif(
        not (REPORTLAB_AVAILABLE and WEASYPRINT_AVAILABLE),
        reason="Both engines must be available"
    )
    def test_auto_detection_with_both_engines_available(self):
        """
        Test auto-detection with both engines available
        
        Validates: Requirements 5.4
        
        When both engines are available, auto-detection should prefer ReportLab.
        """
        # Prepare markdown content
        markdown_content = """
# Test Document

This is a test document for auto-detection.

## Content

Some content here.
"""
        
        # Create engine using AUTO mode
        engine = PDFEngineFactory.create_engine(EngineType.AUTO)
        
        # Verify ReportLab was selected (preference order)
        assert isinstance(engine, ReportLabEngine), \
            "AUTO mode should prefer ReportLab when both engines are available"
        
        # Generate PDF to verify it works
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
    
    @pytest.mark.skipif(
        not (REPORTLAB_AVAILABLE or WEASYPRINT_AVAILABLE),
        reason="At least one engine must be available"
    )
    def test_auto_detection_with_single_engine_available(self):
        """
        Test auto-detection with only one engine available
        
        Validates: Requirements 5.4
        
        When only one engine is available, auto-detection should use it.
        """
        # Prepare markdown content
        markdown_content = """
# Test Document

This is a test document for auto-detection.

## Content

Some content here.
"""
        
        # Create engine using AUTO mode
        engine = PDFEngineFactory.create_engine(EngineType.AUTO)
        
        # Verify an engine was selected
        assert isinstance(engine, (ReportLabEngine, WeasyPrintEngine)), \
            "AUTO mode should select an available engine"
        
        # Generate PDF to verify it works
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
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_workflow_with_complex_markdown(self):
        """
        Test workflow with complex markdown containing various elements
        
        Validates: Requirements 5.1
        """
        # Prepare complex markdown content
        markdown_content = """
# Complex Document Test

## Lists

### Unordered List

- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3

### Ordered List

1. First item
2. Second item
3. Third item

## Code Blocks

Here's a Python code block:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Calculate first 10 Fibonacci numbers
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

## Text Formatting

This paragraph contains **bold text**, *italic text*, and ***bold italic text***.

## Blockquotes

> This is a blockquote.
> It can span multiple lines.

## Horizontal Rule

---

## Tables

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |

## Conclusion

This document tests various markdown elements.
"""
        
        # Create engine
        engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
        
        # Generate PDF
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
            
            # Verify it's a valid PDF
            with open(tmp_path, 'rb') as f:
                header = f.read(5)
                assert header == b'%PDF-'
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_workflow_with_empty_markdown(self):
        """
        Test workflow with edge case: empty markdown
        
        Validates: Requirements 5.1
        """
        # Empty markdown content
        markdown_content = ""
        
        # Create engine
        engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
        
        # Generate PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created (even if empty)
            assert os.path.exists(tmp_path)
            # Empty content should still produce a valid PDF file
            assert os.path.getsize(tmp_path) > 0
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_workflow_with_unicode_content(self):
        """
        Test workflow with Unicode characters
        
        Validates: Requirements 5.1
        """
        # Markdown with Unicode characters
        markdown_content = """
# Unicode Test Document

## Various Languages

### German
Äpfel, Öl, Übung, ß

### French
Café, naïve, Noël

### Spanish
¿Cómo estás? ¡Hola!

### Greek
Ελληνικά

### Emoji
😀 🎉 ✨ 🚀

## Mathematical Symbols
∑ ∫ ∞ ≈ ≠ ± × ÷

## Currency
€ £ ¥ ₹ ₽

## Conclusion
Unicode support is important for international documents.
"""
        
        # Create engine
        engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
        
        # Generate PDF
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
            
            # Verify it's a valid PDF
            with open(tmp_path, 'rb') as f:
                header = f.read(5)
                assert header == b'%PDF-'
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_workflow_error_when_no_engines_available(self):
        """
        Test that appropriate error is raised when no engines are available
        
        Validates: Requirements 5.4
        """
        # This test verifies error handling, not actual unavailability
        # We can't easily simulate no engines being available in the test
        # environment, but we can verify the error handling exists
        
        # If at least one engine is available, skip this test
        if REPORTLAB_AVAILABLE or WEASYPRINT_AVAILABLE:
            pytest.skip("At least one engine is available")
        
        # Try to create engine with AUTO mode when none available
        with pytest.raises(PDFEngineNotAvailableError) as exc_info:
            PDFEngineFactory.create_engine(EngineType.AUTO)
        
        # Verify error message contains installation instructions
        error_message = str(exc_info.value)
        assert "install" in error_message.lower(), \
            "Error message should contain installation instructions"
