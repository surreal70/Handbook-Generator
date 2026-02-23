"""Property-based tests for WeasyPrint PDF engine."""

import pytest
import tempfile
import os
from hypothesis import given, strategies as st, settings, assume
from hypothesis import HealthCheck

from src.pdf_engines import WeasyPrintEngine


# Check if WeasyPrint is available
try:
    from weasyprint import HTML, CSS
    import markdown
    WEASYPRINT_AVAILABLE = True
except (ImportError, OSError):
    WEASYPRINT_AVAILABLE = False


# Strategy for generating valid CSS properties
@st.composite
def css_font_size(draw):
    """Generate valid CSS font-size values."""
    size = draw(st.integers(min_value=8, max_value=24))
    unit = draw(st.sampled_from(['pt', 'px']))
    return f"{size}{unit}"


@st.composite
def css_color(draw):
    """Generate valid CSS color values."""
    r = draw(st.integers(min_value=0, max_value=255))
    g = draw(st.integers(min_value=0, max_value=255))
    b = draw(st.integers(min_value=0, max_value=255))
    return f"rgb({r}, {g}, {b})"


@st.composite
def css_margin(draw):
    """Generate valid CSS margin values."""
    size = draw(st.floats(min_value=0.5, max_value=5.0))
    return f"{size:.1f}cm"


@st.composite
def custom_css_stylesheet(draw):
    """Generate a custom CSS stylesheet with various properties."""
    font_size = draw(css_font_size())
    color = draw(css_color())
    margin = draw(css_margin())
    line_height = draw(st.floats(min_value=1.0, max_value=2.0))
    
    css = f"""
        @page {{
            size: A4;
            margin: {margin};
        }}
        
        body {{
            font-size: {font_size};
            color: {color};
            line-height: {line_height:.1f};
        }}
        
        h1 {{
            color: {color};
            font-size: {font_size};
        }}
    """
    return css


# Strategy for generating simple markdown content
@st.composite
def simple_markdown(draw):
    """Generate simple markdown content for CSS testing."""
    heading = draw(st.text(
        alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'),
            whitelist_characters=' '
        ),
        min_size=5,
        max_size=50
    ))
    heading = ' '.join(heading.split())
    assume(len(heading) >= 5)
    
    paragraph = draw(st.text(
        alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'),
            whitelist_characters=' .,!?'
        ),
        min_size=20,
        max_size=200
    ))
    paragraph = ' '.join(paragraph.split())
    assume(len(paragraph) >= 20)
    
    return f"# {heading}\n\n{paragraph}"


@pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
class TestWeasyPrintCSSSupport:
    """
    Property 10: WeasyPrint CSS Styling Support
    
    Feature: pdf-generation-without-dependencies
    Validates: Requirements 2.4
    
    For any CSS stylesheet provided to WeasyPrint engine, the generated PDF
    should apply the CSS rules to the document layout and styling.
    """
    
    @given(markdown_content=simple_markdown())
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_default_css_applied(self, markdown_content):
        """Test that default CSS is applied to PDF output."""
        engine = WeasyPrintEngine()
        
        # Skip if engine not available
        if not engine.is_available():
            pytest.skip("WeasyPrint not available")
        
        # Generate PDF with default CSS
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
    
    @given(
        markdown_content=simple_markdown(),
        font_size=css_font_size()
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_custom_font_size_applied(self, markdown_content, font_size):
        """Test that custom font sizes are applied correctly."""
        engine = WeasyPrintEngine()
        
        # Skip if engine not available
        if not engine.is_available():
            pytest.skip("WeasyPrint not available")
        
        # Create custom CSS with specific font size
        custom_css = f"""
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-size: {font_size};
            }}
        """
        
        # Temporarily override the _get_default_css method
        original_method = engine._get_default_css
        engine._get_default_css = lambda: custom_css
        
        try:
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        
        finally:
            engine._get_default_css = original_method
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(
        markdown_content=simple_markdown(),
        color=css_color()
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_custom_color_applied(self, markdown_content, color):
        """Test that custom colors are applied correctly."""
        engine = WeasyPrintEngine()
        
        # Skip if engine not available
        if not engine.is_available():
            pytest.skip("WeasyPrint not available")
        
        # Create custom CSS with specific color
        custom_css = f"""
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                color: {color};
            }}
        """
        
        # Temporarily override the _get_default_css method
        original_method = engine._get_default_css
        engine._get_default_css = lambda: custom_css
        
        try:
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        
        finally:
            engine._get_default_css = original_method
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(
        markdown_content=simple_markdown(),
        margin=css_margin()
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_custom_page_margins_applied(self, markdown_content, margin):
        """Test that custom page margins are applied correctly."""
        engine = WeasyPrintEngine()
        
        # Skip if engine not available
        if not engine.is_available():
            pytest.skip("WeasyPrint not available")
        
        # Create custom CSS with specific margins
        custom_css = f"""
            @page {{
                size: A4;
                margin: {margin};
            }}
            body {{
                font-size: 11pt;
            }}
        """
        
        # Temporarily override the _get_default_css method
        original_method = engine._get_default_css
        engine._get_default_css = lambda: custom_css
        
        try:
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        
        finally:
            engine._get_default_css = original_method
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(
        markdown_content=simple_markdown(),
        css_stylesheet=custom_css_stylesheet()
    )
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_complex_css_stylesheet_applied(self, markdown_content, css_stylesheet):
        """Test that complex CSS stylesheets with multiple properties are applied."""
        engine = WeasyPrintEngine()
        
        # Skip if engine not available
        if not engine.is_available():
            pytest.skip("WeasyPrint not available")
        
        # Temporarily override the _get_default_css method
        original_method = engine._get_default_css
        engine._get_default_css = lambda: css_stylesheet
        
        try:
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        
        finally:
            engine._get_default_css = original_method
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    @given(markdown_content=simple_markdown())
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_code_block_monospace_styling(self, markdown_content):
        """Test that code blocks receive monospace font styling via CSS."""
        engine = WeasyPrintEngine()
        
        # Skip if engine not available
        if not engine.is_available():
            pytest.skip("WeasyPrint not available")
        
        # Add a code block to the markdown
        markdown_with_code = markdown_content + "\n\n```python\ndef hello():\n    print('world')\n```"
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            engine.generate_pdf(
                markdown_content=markdown_with_code,
                output_path=tmp_path,
                include_toc=False
            )
            
            # Verify PDF was created
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
            
            # Verify the default CSS includes monospace font for code
            default_css = engine._get_default_css()
            assert 'monospace' in default_css.lower(), \
                "Default CSS should include monospace font for code blocks"
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

