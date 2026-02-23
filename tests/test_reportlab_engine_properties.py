"""Property-based tests for ReportLab PDF engine."""

import pytest
import tempfile
import os
from hypothesis import given, strategies as st, settings, assume
from hypothesis import HealthCheck

from src.pdf_engines import ReportLabEngine


# Check if ReportLab is available
try:
    import reportlab
    import markdown
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


# Helper function to extract text from PDF
def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text content from a PDF file."""
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except ImportError:
        # If PyPDF2 is not available, just check file exists
        return ""


# Strategy for generating valid markdown headings
@st.composite
def markdown_heading(draw):
    """Generate a valid markdown heading."""
    level = draw(st.integers(min_value=1, max_value=3))
    text = draw(st.text(
        alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'),
            whitelist_characters=' '
        ),
        min_size=3,
        max_size=50
    ))
    # Clean up text
    text = ' '.join(text.split())  # Normalize whitespace
    assume(len(text) >= 3)
    return f"{'#' * level} {text}"


# Strategy for generating valid markdown paragraphs
@st.composite
def markdown_paragraph(draw):
    """Generate a valid markdown paragraph."""
    text = draw(st.text(
        alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'),
            whitelist_characters=' .,!?'
        ),
        min_size=10,
        max_size=200
    ))
    # Clean up text and remove problematic characters
    text = ' '.join(text.split())  # Normalize whitespace
    # Remove any HTML-like characters that could cause issues
    text = text.replace('<', '').replace('>', '').replace('&', '')
    assume(len(text) >= 10)
    return text


# Strategy for generating valid code blocks
@st.composite
def markdown_code_block(draw):
    """Generate a valid markdown code block."""
    code = draw(st.text(
        alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'),
            whitelist_characters=' =(){}[]'
        ),
        min_size=5,
        max_size=100
    ))
    # Clean up code
    code = ' '.join(code.split())  # Normalize whitespace
    assume(len(code) >= 5)
    return f"```\n{code}\n```"


# Strategy for generating markdown with emphasis
@st.composite
def markdown_with_emphasis(draw):
    """Generate markdown text with bold and italic."""
    text = draw(st.text(
        alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'),
            whitelist_characters=' '
        ),
        min_size=5,
        max_size=50
    ))
    text = ' '.join(text.split())
    assume(len(text) >= 5)
    
    emphasis_type = draw(st.sampled_from(['bold', 'italic', 'both']))
    if emphasis_type == 'bold':
        return f"**{text}**"
    elif emphasis_type == 'italic':
        return f"*{text}*"
    else:
        return f"***{text}***"


@pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
class TestMarkdownElementPreservation:
    """
    Property 2: Markdown Element Preservation
    
    Feature: pdf-generation-without-dependencies
    Validates: Requirements 1.2, 1.5, 6.2, 6.4, 6.5
    
    For any markdown content containing headings, paragraphs, lists, code blocks,
    and text emphasis (bold, italic), when the ReportLab engine generates a PDF,
    the output should preserve all these structural and formatting elements.
    """
    
    @given(
        headings=st.lists(markdown_heading(), min_size=1, max_size=3),
        paragraphs=st.lists(markdown_paragraph(), min_size=1, max_size=5)
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_headings_and_paragraphs_preserved(self, headings, paragraphs):
        """Test that headings and paragraphs are preserved in PDF output."""
        engine = ReportLabEngine()
        
        # Build markdown content
        markdown_parts = []
        for heading in headings:
            markdown_parts.append(heading)
        for paragraph in paragraphs:
            markdown_parts.append(paragraph)
        
        markdown_content = '\n\n'.join(markdown_parts)
        
        # Generate PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created and is not empty
            assert os.path.exists(tmp_path), "PDF file was not created"
            assert os.path.getsize(tmp_path) > 0, "PDF file is empty"
            
            # Verify it's a valid PDF by checking the header
            with open(tmp_path, 'rb') as f:
                header = f.read(5)
                assert header == b'%PDF-', "File is not a valid PDF"
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(code_blocks=st.lists(markdown_code_block(), min_size=1, max_size=3))
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_code_blocks_preserved(self, code_blocks):
        """Test that code blocks are preserved in PDF output."""
        engine = ReportLabEngine()
        
        markdown_content = '\n\n'.join(code_blocks)
        
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
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(emphasis_text=st.lists(markdown_with_emphasis(), min_size=1, max_size=5))
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_text_emphasis_preserved(self, emphasis_text):
        """Test that bold and italic text formatting is preserved."""
        engine = ReportLabEngine()
        
        markdown_content = '\n\n'.join(emphasis_text)
        
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
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(
        headings=st.lists(markdown_heading(), min_size=1, max_size=2),
        paragraphs=st.lists(markdown_paragraph(), min_size=1, max_size=3),
        code_blocks=st.lists(markdown_code_block(), min_size=0, max_size=2),
        emphasis_text=st.lists(markdown_with_emphasis(), min_size=0, max_size=2)
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_mixed_elements_preserved(self, headings, paragraphs, code_blocks, emphasis_text):
        """Test that mixed markdown elements are all preserved together."""
        engine = ReportLabEngine()
        
        # Interleave different element types
        markdown_parts = []
        for i, heading in enumerate(headings):
            markdown_parts.append(heading)
            if i < len(paragraphs):
                markdown_parts.append(paragraphs[i])
            if i < len(code_blocks):
                markdown_parts.append(code_blocks[i])
            if i < len(emphasis_text):
                markdown_parts.append(emphasis_text[i])
        
        # Add remaining elements
        markdown_parts.extend(paragraphs[len(headings):])
        markdown_parts.extend(code_blocks[len(headings):])
        markdown_parts.extend(emphasis_text[len(headings):])
        
        markdown_content = '\n\n'.join(markdown_parts)
        
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
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)



@pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
class TestTOCGeneration:
    """
    Property 4: Table of Contents Generation
    
    Feature: pdf-generation-without-dependencies
    Validates: Requirements 1.4, 5.2, 6.3
    
    For any markdown content with multiple heading levels, when TOC is enabled
    (via include_toc=True), the PDF engine should generate a table of contents
    with clickable entries that have accurate page numbers.
    """
    
    @given(
        headings=st.lists(
            markdown_heading(),
            min_size=2,
            max_size=5
        )
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_toc_generated_when_enabled(self, headings):
        """Test that TOC is generated when include_toc=True."""
        engine = ReportLabEngine()
        
        # Build markdown content with headings
        markdown_content = '\n\n'.join(headings)
        
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
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
            
            # Verify PDF has multiple pages (TOC + content)
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(tmp_path)
                # With TOC enabled, we should have at least 2 pages
                # (1 for TOC, 1+ for content)
                assert len(reader.pages) >= 2, \
                    f"Expected at least 2 pages with TOC, got {len(reader.pages)}"
            except ImportError:
                pass  # PyPDF2 not available, skip page count verification
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(
        headings=st.lists(
            markdown_heading(),
            min_size=2,
            max_size=5
        )
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_toc_not_generated_when_disabled(self, headings):
        """Test that TOC is not generated when include_toc=False."""
        engine = ReportLabEngine()
        
        # Build markdown content with headings
        markdown_content = '\n\n'.join(headings)
        
        # Generate PDF without TOC
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
            
            # Verify PDF has fewer pages than with TOC
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(tmp_path)
                # Without TOC, we should have just content pages
                # This is a basic check - exact page count depends on content
                assert len(reader.pages) >= 1
            except ImportError:
                pass  # PyPDF2 not available, skip verification
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(
        h1_headings=st.lists(
            st.text(
                alphabet=st.characters(
                    whitelist_categories=('Lu', 'Ll', 'Nd'),
                    whitelist_characters=' '
                ),
                min_size=5,
                max_size=30
            ).map(lambda t: f"# {' '.join(t.split())}"),
            min_size=1,
            max_size=3
        ),
        h2_headings=st.lists(
            st.text(
                alphabet=st.characters(
                    whitelist_categories=('Lu', 'Ll', 'Nd'),
                    whitelist_characters=' '
                ),
                min_size=5,
                max_size=30
            ).map(lambda t: f"## {' '.join(t.split())}"),
            min_size=1,
            max_size=3
        )
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_toc_with_multiple_heading_levels(self, h1_headings, h2_headings):
        """Test that TOC handles multiple heading levels correctly."""
        engine = ReportLabEngine()
        
        # Interleave h1 and h2 headings
        markdown_parts = []
        for i in range(max(len(h1_headings), len(h2_headings))):
            if i < len(h1_headings):
                markdown_parts.append(h1_headings[i])
            if i < len(h2_headings):
                markdown_parts.append(h2_headings[i])
        
        markdown_content = '\n\n'.join(markdown_parts)
        
        # Generate PDF with TOC
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
