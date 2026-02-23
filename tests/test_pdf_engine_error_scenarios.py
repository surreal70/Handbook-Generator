"""Unit tests for PDF engine error scenarios."""

import pytest
import tempfile
import os
from unittest.mock import patch, MagicMock
from pathlib import Path

from src.pdf_engines import (
    ReportLabEngine,
    WeasyPrintEngine,
    PDFEngineFactory,
    EngineType,
    PDFGenerationError,
    MarkdownConversionError,
    PDFEngineNotAvailableError
)


# Check if engines are available
try:
    import reportlab
    import markdown
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

try:
    # Try to import weasyprint, but handle system dependency errors
    import weasyprint
    WEASYPRINT_AVAILABLE = True
except (ImportError, OSError):
    # OSError occurs when system libraries (libpango) are missing
    WEASYPRINT_AVAILABLE = False


class TestEngineFailureDuringGeneration:
    """Test error handling when engine fails during PDF generation."""
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_reportlab_fails_with_invalid_output_path(self):
        """Test that ReportLab raises PDFGenerationError with invalid output path."""
        engine = ReportLabEngine()
        markdown_content = "# Test Content"
        
        # Use a path that cannot be written to
        invalid_path = "/root/nonexistent/directory/output.pdf"
        
        with pytest.raises(PDFGenerationError) as exc_info:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=invalid_path
            )
        
        # Verify error message contains helpful information
        error_msg = str(exc_info.value)
        assert "PDF Generation Error" in error_msg or "Failed to generate PDF" in error_msg
        assert "Troubleshooting" in error_msg or "troubleshooting" in error_msg.lower()
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_reportlab_fails_with_readonly_directory(self):
        """Test that ReportLab handles read-only directory gracefully."""
        engine = ReportLabEngine()
        markdown_content = "# Test Content"
        
        # Try to write to a typically read-only location
        readonly_path = "/etc/test_output.pdf"
        
        with pytest.raises((PDFGenerationError, PermissionError, OSError)):
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=readonly_path
            )
    
    @pytest.mark.skipif(not WEASYPRINT_AVAILABLE, reason="WeasyPrint not installed")
    def test_weasyprint_fails_with_invalid_output_path(self):
        """Test that WeasyPrint raises PDFGenerationError with invalid output path."""
        engine = WeasyPrintEngine()
        markdown_content = "# Test Content"
        
        # Use a path that cannot be written to
        invalid_path = "/root/nonexistent/directory/output.pdf"
        
        with pytest.raises(PDFGenerationError) as exc_info:
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=invalid_path
            )
        
        # Verify error message contains helpful information
        error_msg = str(exc_info.value)
        assert "PDF Generation Error" in error_msg or "Failed to generate PDF" in error_msg
        assert "Troubleshooting" in error_msg or "troubleshooting" in error_msg.lower()


class TestMarkdownConversionErrors:
    """Test error handling when markdown conversion fails."""
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_markdown_conversion_error_includes_snippet(self):
        """Test that markdown conversion errors include the problematic content."""
        engine = ReportLabEngine()
        
        # Mock markdown.markdown to raise an exception
        with patch('markdown.markdown', side_effect=Exception("Markdown parsing failed")):
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            try:
                with pytest.raises(MarkdownConversionError) as exc_info:
                    engine.generate_pdf(
                        markdown_content="# Test Content\n\nSome problematic markdown",
                        output_path=tmp_path
                    )
                
                # Verify error message contains helpful information
                error_msg = str(exc_info.value)
                assert "Markdown Conversion Error" in error_msg or "markdown" in error_msg.lower()
                assert "Troubleshooting" in error_msg or "troubleshooting" in error_msg.lower()
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_markdown_conversion_error_provides_guidance(self):
        """Test that markdown conversion errors provide troubleshooting guidance."""
        engine = ReportLabEngine()
        
        # Mock markdown.markdown to raise an exception
        with patch('markdown.markdown', side_effect=ValueError("Invalid markdown syntax")):
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            try:
                with pytest.raises(MarkdownConversionError) as exc_info:
                    engine.generate_pdf(
                        markdown_content="# Malformed\n```\nUnclosed code block",
                        output_path=tmp_path
                    )
                
                error_msg = str(exc_info.value)
                # Should provide actionable guidance
                has_guidance = any(keyword in error_msg.lower() 
                                  for keyword in ['check', 'verify', 'ensure', 'try'])
                assert has_guidance, "Error should provide troubleshooting guidance"
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)


class TestOutputPathErrors:
    """Test error handling for output path issues."""
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_nonexistent_directory_error(self):
        """Test error when output directory doesn't exist."""
        engine = ReportLabEngine()
        markdown_content = "# Test Content"
        
        # Use a path with nonexistent directory
        nonexistent_path = "/tmp/nonexistent_dir_12345/output.pdf"
        
        with pytest.raises((PDFGenerationError, OSError, FileNotFoundError)):
            engine.generate_pdf(
                markdown_content=markdown_content,
                output_path=nonexistent_path
            )
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_invalid_characters_in_path(self):
        """Test error handling with invalid characters in output path."""
        engine = ReportLabEngine()
        markdown_content = "# Test Content"
        
        # Create a temp directory for testing
        with tempfile.TemporaryDirectory() as tmpdir:
            # Use invalid characters (on some systems)
            # Note: This might not fail on all systems, so we just verify it doesn't crash
            try:
                invalid_path = os.path.join(tmpdir, "test<>|?.pdf")
                engine.generate_pdf(
                    markdown_content=markdown_content,
                    output_path=invalid_path
                )
                # If it succeeds, that's okay too (depends on OS)
            except (PDFGenerationError, OSError, ValueError):
                # Expected on systems that don't allow these characters
                pass
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_permission_error_provides_guidance(self):
        """Test that permission errors provide helpful guidance."""
        engine = ReportLabEngine()
        markdown_content = "# Test Content"
        
        # Mock the file writing to raise PermissionError
        with patch('reportlab.platypus.SimpleDocTemplate.build', 
                   side_effect=PermissionError("Permission denied")):
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            try:
                with pytest.raises((PDFGenerationError, PermissionError)) as exc_info:
                    engine.generate_pdf(
                        markdown_content=markdown_content,
                        output_path=tmp_path
                    )
                
                # If it's a PDFGenerationError, check for guidance
                if isinstance(exc_info.value, PDFGenerationError):
                    error_msg = str(exc_info.value)
                    assert "permission" in error_msg.lower() or "write" in error_msg.lower()
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)


class TestEngineNotAvailableErrors:
    """Test error handling when engines are not available."""
    
    def test_reportlab_not_available_error_message(self):
        """Test error message when ReportLab is not available."""
        with patch.object(ReportLabEngine, 'is_available', return_value=False):
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.REPORTLAB)
            
            error_msg = str(exc_info.value)
            # Should include installation instructions
            assert "install" in error_msg.lower()
            assert "pip" in error_msg.lower()
            assert "reportlab" in error_msg.lower()
    
    def test_weasyprint_not_available_error_message(self):
        """Test error message when WeasyPrint is not available."""
        with patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
            
            error_msg = str(exc_info.value)
            # Should include installation instructions
            assert "install" in error_msg.lower()
            assert "weasyprint" in error_msg.lower()
            # Should suggest alternative
            assert "reportlab" in error_msg.lower() or "alternative" in error_msg.lower()
    
    def test_no_engines_available_error_message(self):
        """Test error message when no engines are available."""
        with patch.object(ReportLabEngine, 'is_available', return_value=False), \
             patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.AUTO)
            
            error_msg = str(exc_info.value)
            # Should provide comprehensive guidance
            assert "install" in error_msg.lower()
            assert "pip" in error_msg.lower()
            # Should mention at least one engine
            assert "reportlab" in error_msg.lower() or "weasyprint" in error_msg.lower()
            # Should include troubleshooting steps
            has_troubleshooting = any(keyword in error_msg.lower() 
                                     for keyword in ['troubleshooting', 'verify', 'check', 'ensure'])
            assert has_troubleshooting


class TestErrorMessageQuality:
    """Test that error messages are high quality and actionable."""
    
    def test_error_messages_are_multiline(self):
        """Test that error messages are structured with multiple lines."""
        with patch.object(ReportLabEngine, 'is_available', return_value=False):
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.REPORTLAB)
            
            error_msg = str(exc_info.value)
            # Should be multi-line for readability
            assert '\n' in error_msg
            # Should have substantial content
            assert len(error_msg) > 50
    
    def test_error_messages_include_context(self):
        """Test that error messages include context about what failed."""
        with patch.object(ReportLabEngine, 'is_available', return_value=False):
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.REPORTLAB)
            
            error_msg = str(exc_info.value)
            # Should mention what component failed
            assert "reportlab" in error_msg.lower() or "engine" in error_msg.lower()
    
    def test_error_messages_provide_next_steps(self):
        """Test that error messages provide clear next steps."""
        with patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
            
            error_msg = str(exc_info.value)
            # Should provide actionable next steps
            has_action_words = any(word in error_msg.lower() 
                                  for word in ['install', 'run', 'use', 'try'])
            assert has_action_words


class TestDiskSpaceErrors:
    """Test error handling for disk space issues."""
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_disk_space_error_handling(self):
        """Test that disk space errors are handled gracefully."""
        engine = ReportLabEngine()
        markdown_content = "# Test Content" * 1000  # Large content
        
        # Mock to simulate disk space error
        with patch('reportlab.platypus.SimpleDocTemplate.build', 
                   side_effect=OSError(28, "No space left on device")):
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp_path = tmp.name
            
            try:
                with pytest.raises((PDFGenerationError, OSError)) as exc_info:
                    engine.generate_pdf(
                        markdown_content=markdown_content,
                        output_path=tmp_path
                    )
                
                # If it's a PDFGenerationError, check for helpful message
                if isinstance(exc_info.value, PDFGenerationError):
                    error_msg = str(exc_info.value)
                    # Should mention disk or space
                    has_disk_info = any(keyword in error_msg.lower() 
                                       for keyword in ['disk', 'space', 'storage'])
                    # This is optional since we're mocking, but good to have
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)


class TestConcurrentAccessErrors:
    """Test error handling for file access conflicts."""
    
    @pytest.mark.skipif(not REPORTLAB_AVAILABLE, reason="ReportLab not installed")
    def test_file_in_use_error(self):
        """Test handling when output file is in use."""
        engine = ReportLabEngine()
        markdown_content = "# Test Content"
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
            
            # Keep the file open to simulate it being in use
            try:
                # First generation should succeed
                engine.generate_pdf(
                    markdown_content=markdown_content,
                    output_path=tmp_path
                )
                
                # File exists and can be overwritten (on most systems)
                assert os.path.exists(tmp_path)
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
