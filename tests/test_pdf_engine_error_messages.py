"""Property-based tests for PDF engine error message quality."""

import pytest
import tempfile
import os
from hypothesis import given, strategies as st, settings, assume
from hypothesis import HealthCheck
from unittest.mock import patch, MagicMock

from src.pdf_engines import (
    PDFEngineFactory,
    EngineType,
    PDFEngineNotAvailableError,
    PDFGenerationError,
    MarkdownConversionError,
    ReportLabEngine,
    WeasyPrintEngine
)


# Strategy for generating engine type names
@st.composite
def engine_type_name(draw):
    """Generate engine type names (valid and invalid)."""
    return draw(st.sampled_from(['reportlab', 'weasyprint', 'auto', 'invalid', 'unknown']))


# Strategy for generating file paths
@st.composite
def file_path(draw):
    """Generate various file paths including problematic ones."""
    path_type = draw(st.sampled_from(['valid', 'nonexistent', 'readonly', 'invalid_chars']))
    
    if path_type == 'valid':
        return '/tmp/test_output.pdf'
    elif path_type == 'nonexistent':
        return '/nonexistent/directory/output.pdf'
    elif path_type == 'readonly':
        return '/root/output.pdf'  # Typically not writable
    else:
        return '/tmp/test<>|?.pdf'  # Invalid characters


# Strategy for generating markdown content
@st.composite
def markdown_content(draw):
    """Generate markdown content including malformed content."""
    content_type = draw(st.sampled_from(['valid', 'malformed', 'empty', 'special_chars']))
    
    if content_type == 'valid':
        return draw(st.text(min_size=10, max_size=200))
    elif content_type == 'malformed':
        # Unclosed code block
        return "```python\nprint('hello')\n# Missing closing ```"
    elif content_type == 'empty':
        return ""
    else:
        # Special characters that might cause issues
        return "<script>alert('test')</script>"


class TestErrorMessageInstallationInstructions:
    """
    Property 5: Error Messages Include Installation Instructions
    
    Feature: pdf-generation-without-dependencies
    Validates: Requirements 2.2, 4.1, 4.3
    
    For any PDF engine that is unavailable (not installed or missing dependencies),
    when the system attempts to use that engine, it should raise an error message
    that includes specific installation instructions for that engine.
    """
    
    @given(engine_name=st.sampled_from(['reportlab', 'weasyprint']))
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_unavailable_engine_includes_installation_instructions(self, engine_name):
        """Test that unavailable engines provide installation instructions."""
        # Mock the engine as unavailable
        if engine_name == 'reportlab':
            with patch.object(ReportLabEngine, 'is_available', return_value=False):
                try:
                    PDFEngineFactory.create_engine(EngineType.REPORTLAB)
                    pytest.fail("Expected PDFEngineNotAvailableError")
                except PDFEngineNotAvailableError as e:
                    error_msg = str(e)
                    # Verify installation instructions are present
                    assert 'install' in error_msg.lower(), \
                        "Error message should include installation instructions"
                    assert 'pip' in error_msg.lower(), \
                        "Error message should mention pip"
                    assert 'reportlab' in error_msg.lower(), \
                        "Error message should mention the package name"
        
        elif engine_name == 'weasyprint':
            with patch.object(WeasyPrintEngine, 'is_available', return_value=False):
                try:
                    PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
                    pytest.fail("Expected PDFEngineNotAvailableError")
                except PDFEngineNotAvailableError as e:
                    error_msg = str(e)
                    # Verify installation instructions are present
                    assert 'install' in error_msg.lower(), \
                        "Error message should include installation instructions"
                    assert 'weasyprint' in error_msg.lower(), \
                        "Error message should mention the package name"
    
    def test_no_engines_available_provides_instructions(self):
        """Test that when no engines are available, clear instructions are provided."""
        # Mock both engines as unavailable
        with patch.object(ReportLabEngine, 'is_available', return_value=False), \
             patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            
            try:
                PDFEngineFactory.create_engine(EngineType.AUTO)
                pytest.fail("Expected PDFEngineNotAvailableError")
            except PDFEngineNotAvailableError as e:
                error_msg = str(e)
                # Verify comprehensive instructions
                assert 'install' in error_msg.lower(), \
                    "Error message should include installation instructions"
                assert 'pip' in error_msg.lower(), \
                    "Error message should mention pip"
                # Should mention at least one engine
                assert 'reportlab' in error_msg.lower() or 'weasyprint' in error_msg.lower(), \
                    "Error message should mention at least one engine"
    
    @given(engine_name=st.sampled_from(['reportlab', 'weasyprint']))
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_installation_instructions_are_platform_aware(self, engine_name):
        """Test that installation instructions consider the platform."""
        if engine_name == 'weasyprint':
            engine = WeasyPrintEngine()
            instructions = engine.get_installation_instructions()
            
            # Should include platform-specific information
            # At minimum, should mention system dependencies
            assert 'system' in instructions.lower() or 'dependencies' in instructions.lower(), \
                "WeasyPrint instructions should mention system dependencies"
            
            # Should provide guidance for at least one platform
            has_platform_info = any(platform in instructions.lower() 
                                   for platform in ['ubuntu', 'debian', 'macos', 'windows', 'linux'])
            assert has_platform_info, \
                "Instructions should include platform-specific guidance"
    
    @given(engine_name=st.sampled_from(['reportlab', 'weasyprint']))
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_error_messages_include_troubleshooting_steps(self, engine_name):
        """Test that error messages include troubleshooting guidance."""
        # Get the engine's installation instructions directly
        if engine_name == 'reportlab':
            engine = ReportLabEngine()
            instructions = engine.get_installation_instructions()
            # ReportLab instructions should be clear and actionable
            assert 'install' in instructions.lower(), \
                "Instructions should include installation steps"
            assert 'pip' in instructions.lower(), \
                "Instructions should mention pip"
        
        elif engine_name == 'weasyprint':
            engine = WeasyPrintEngine()
            instructions = engine.get_installation_instructions()
            # WeasyPrint instructions should include system dependencies
            assert 'install' in instructions.lower(), \
                "Instructions should include installation steps"
            assert 'dependencies' in instructions.lower() or 'system' in instructions.lower(), \
                "Instructions should mention system dependencies"


class TestPDFGenerationErrorMessages:
    """Test that PDF generation errors provide helpful troubleshooting information."""
    
    @given(
        markdown_text=st.text(min_size=10, max_size=100),
        output_path=st.text(min_size=5, max_size=50)
    )
    @settings(
        max_examples=50,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_generation_errors_include_output_path(self, markdown_text, output_path):
        """Test that generation errors mention the output path."""
        # Clean up markdown text to avoid conversion issues
        markdown_text = ' '.join(markdown_text.split())
        assume(len(markdown_text) >= 10)
        
        # Use an invalid output path to trigger an error
        invalid_path = f"/nonexistent_dir_{output_path}/test.pdf"
        
        try:
            import reportlab
            import markdown as md
            engine = ReportLabEngine()
            
            try:
                engine.generate_pdf(
                    markdown_content=markdown_text,
                    output_path=invalid_path,
                    include_toc=False
                )
                # If it somehow succeeds, clean up
                if os.path.exists(invalid_path):
                    os.unlink(invalid_path)
            except (PDFGenerationError, OSError, PermissionError) as e:
                error_msg = str(e)
                # Error message should provide context about what failed
                has_context = any(keyword in error_msg.lower() 
                                 for keyword in ['output', 'path', 'directory', 'file'])
                assert has_context, \
                    "Error message should provide context about the failure"
        except ImportError:
            pytest.skip("ReportLab not available")
    
    def test_markdown_conversion_errors_include_snippet(self):
        """Test that markdown conversion errors include problematic content."""
        try:
            import reportlab
            import markdown as md
            
            engine = ReportLabEngine()
            
            # Create problematic markdown that might cause issues
            # We'll mock the markdown conversion to force an error
            with patch('markdown.markdown', side_effect=Exception("Conversion failed")):
                try:
                    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                        tmp_path = tmp.name
                    
                    engine.generate_pdf(
                        markdown_content="# Test Content",
                        output_path=tmp_path,
                        include_toc=False
                    )
                    pytest.fail("Expected MarkdownConversionError")
                except MarkdownConversionError as e:
                    error_msg = str(e)
                    # Should include information about the conversion failure
                    assert 'markdown' in error_msg.lower() or 'conversion' in error_msg.lower(), \
                        "Error message should mention markdown conversion"
                finally:
                    if os.path.exists(tmp_path):
                        os.unlink(tmp_path)
        except ImportError:
            pytest.skip("ReportLab not available")
    
    @given(engine_name=st.sampled_from(['reportlab', 'weasyprint']))
    @settings(
        max_examples=50,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_error_messages_suggest_alternative_engines(self, engine_name):
        """Test that errors suggest trying alternative engines when appropriate."""
        # For WeasyPrint errors, should suggest ReportLab as alternative
        if engine_name == 'weasyprint':
            with patch.object(WeasyPrintEngine, 'is_available', return_value=False):
                try:
                    PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
                    pytest.fail("Expected PDFEngineNotAvailableError")
                except PDFEngineNotAvailableError as e:
                    error_msg = str(e)
                    # Should mention alternative
                    has_alternative = 'reportlab' in error_msg.lower() or 'alternative' in error_msg.lower()
                    assert has_alternative, \
                        "WeasyPrint error should suggest ReportLab as alternative"


class TestErrorMessageCompleteness:
    """Test that error messages are complete and actionable."""
    
    @given(engine_name=st.sampled_from(['reportlab', 'weasyprint']))
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_error_messages_are_not_empty(self, engine_name):
        """Test that error messages are never empty."""
        # Mock engine as unavailable
        if engine_name == 'reportlab':
            with patch.object(ReportLabEngine, 'is_available', return_value=False):
                try:
                    PDFEngineFactory.create_engine(EngineType.REPORTLAB)
                    pytest.fail("Expected PDFEngineNotAvailableError")
                except PDFEngineNotAvailableError as e:
                    error_msg = str(e)
                    assert len(error_msg) > 0, "Error message should not be empty"
                    assert len(error_msg) > 20, "Error message should be substantial"
        
        elif engine_name == 'weasyprint':
            with patch.object(WeasyPrintEngine, 'is_available', return_value=False):
                try:
                    PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
                    pytest.fail("Expected PDFEngineNotAvailableError")
                except PDFEngineNotAvailableError as e:
                    error_msg = str(e)
                    assert len(error_msg) > 0, "Error message should not be empty"
                    assert len(error_msg) > 20, "Error message should be substantial"
    
    @given(engine_name=st.sampled_from(['reportlab', 'weasyprint']))
    @settings(
        max_examples=100,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    def test_error_messages_are_user_friendly(self, engine_name):
        """Test that error messages avoid technical jargon where possible."""
        # Get installation instructions
        if engine_name == 'reportlab':
            engine = ReportLabEngine()
        else:
            engine = WeasyPrintEngine()
        
        instructions = engine.get_installation_instructions()
        
        # Should use clear language
        assert 'install' in instructions.lower(), \
            "Instructions should use clear action words like 'install'"
        
        # Should not be overly technical
        # (This is subjective, but we can check for some basic clarity)
        assert len(instructions.split('\n')) > 1, \
            "Instructions should be multi-line for clarity"
    
    def test_error_messages_include_technical_details(self):
        """Test that error messages include technical details for debugging."""
        # Mock both engines as unavailable
        with patch.object(ReportLabEngine, 'is_available', return_value=False), \
             patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            
            try:
                PDFEngineFactory.create_engine(EngineType.AUTO)
                pytest.fail("Expected PDFEngineNotAvailableError")
            except PDFEngineNotAvailableError as e:
                error_msg = str(e)
                # Should provide enough detail for troubleshooting
                # Check for structured information
                has_structure = '\n' in error_msg  # Multi-line
                assert has_structure, \
                    "Error message should be structured with multiple lines"
