"""
Property-based and unit tests for CLI PDF engine integration.

This module tests the integration of PDF engine selection with the CLI,
including backward compatibility and engine routing.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from hypothesis import given, strategies as st, settings, assume

from src.cli import parse_arguments
from src.output_generator import OutputGenerator, OutputResult
from src.pdf_engines import EngineType, PDFEngineFactory, PDFEngineNotAvailableError


class TestCLIPDFEngineArgumentParsing:
    """Unit tests for CLI PDF engine argument parsing."""
    
    def test_pdf_engine_argument_default(self):
        """Test that --pdf-engine defaults to 'auto'."""
        with patch('sys.argv', ['handbook-generator', '--test']):
            args = parse_arguments()
            assert args.pdf_engine == 'auto'
    
    def test_pdf_engine_argument_reportlab(self):
        """Test --pdf-engine with 'reportlab' value."""
        with patch('sys.argv', ['handbook-generator', '--test', '--pdf-engine', 'reportlab']):
            args = parse_arguments()
            assert args.pdf_engine == 'reportlab'
    
    def test_pdf_engine_argument_weasyprint(self):
        """Test --pdf-engine with 'weasyprint' value."""
        with patch('sys.argv', ['handbook-generator', '--test', '--pdf-engine', 'weasyprint']):
            args = parse_arguments()
            assert args.pdf_engine == 'weasyprint'
    
    def test_pdf_engine_argument_auto(self):
        """Test --pdf-engine with explicit 'auto' value."""
        with patch('sys.argv', ['handbook-generator', '--test', '--pdf-engine', 'auto']):
            args = parse_arguments()
            assert args.pdf_engine == 'auto'
    
    def test_pdf_engine_invalid_value(self):
        """Test that invalid --pdf-engine value raises error."""
        with patch('sys.argv', ['handbook-generator', '--test', '--pdf-engine', 'invalid']):
            with pytest.raises(SystemExit):
                parse_arguments()


class TestOutputGeneratorPDFEngineIntegration:
    """Unit tests for OutputGenerator PDF engine integration."""
    
    def test_generate_pdf_accepts_engine_type_parameter(self):
        """Test that generate_pdf accepts engine_type parameter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Mock the PDF engine factory at the import location
            with patch('src.pdf_engines.PDFEngineFactory') as mock_factory:
                mock_engine = Mock()
                mock_engine.generate_pdf = Mock()
                mock_factory.create_engine.return_value = mock_engine
                
                # Call with engine_type parameter
                result = generator.generate_pdf(
                    markdown_content="# Test",
                    language="en",
                    template_type="test",
                    engine_type="reportlab"
                )
                
                # Verify engine was created with correct type
                mock_factory.create_engine.assert_called_once()
                call_args = mock_factory.create_engine.call_args
                assert call_args[0][0].value == "reportlab"
    
    def test_generate_pdf_with_toc_accepts_engine_type_parameter(self):
        """Test that generate_pdf_with_toc accepts engine_type parameter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Mock the PDF engine factory at the import location
            with patch('src.pdf_engines.PDFEngineFactory') as mock_factory:
                mock_engine = Mock()
                mock_engine.generate_pdf = Mock()
                mock_factory.create_engine.return_value = mock_engine
                
                # Call with engine_type parameter
                templates_data = [("0001", "Test Template", "# Content")]
                result = generator.generate_pdf_with_toc(
                    templates_data=templates_data,
                    language="en",
                    template_type="test",
                    engine_type="weasyprint"
                )
                
                # Verify engine was created with correct type
                mock_factory.create_engine.assert_called_once()
                call_args = mock_factory.create_engine.call_args
                assert call_args[0][0].value == "weasyprint"
    
    def test_generate_pdf_logs_engine_used(self):
        """Test that generate_pdf logs which engine was used."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Mock the PDF engine factory at the import location
            with patch('src.pdf_engines.PDFEngineFactory') as mock_factory:
                mock_engine = Mock()
                mock_engine.__class__.__name__ = "ReportLabEngine"
                mock_engine.generate_pdf = Mock()
                mock_factory.create_engine.return_value = mock_engine
                
                # Call generate_pdf
                result = generator.generate_pdf(
                    markdown_content="# Test",
                    language="en",
                    template_type="test",
                    engine_type="auto"
                )
                
                # Verify warning contains engine name
                assert any("ReportLabEngine" in warning for warning in result.warnings)
    
    def test_generate_pdf_handles_engine_not_available_error(self):
        """Test that generate_pdf handles PDFEngineNotAvailableError gracefully."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Mock the PDF engine factory to raise error at the import location
            with patch('src.pdf_engines.PDFEngineFactory') as mock_factory:
                mock_factory.create_engine.side_effect = PDFEngineNotAvailableError(
                    "Engine not available",
                    engine_name="reportlab"
                )
                
                # Call generate_pdf
                result = generator.generate_pdf(
                    markdown_content="# Test",
                    language="en",
                    template_type="test",
                    engine_type="reportlab"
                )
                
                # Verify error was captured
                assert len(result.errors) > 0
                assert "Engine not available" in result.errors[0]
                assert result.pdf_path is None


# Feature: pdf-generation-without-dependencies, Property 9: Backward Compatibility with Output Flag
class TestBackwardCompatibilityProperty:
    """
    Property-based tests for backward compatibility.
    
    **Validates: Requirements 5.1, 5.4**
    
    Property 9: Backward Compatibility with Output Flag
    For any existing CLI command using `-o pdf` without the `--pdf-engine` flag,
    the system should successfully generate a PDF using the auto-detected engine.
    """
    
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz']),
        markdown_content=st.text(min_size=10, max_size=500)
    )
    @settings(max_examples=100)
    def test_backward_compatibility_without_pdf_engine_flag(
        self,
        language,
        template_type,
        markdown_content
    ):
        """
        Property: CLI commands without --pdf-engine flag should work with auto-detection.
        
        **Validates: Requirements 5.1, 5.4**
        """
        # Ensure markdown content is valid
        assume(len(markdown_content.strip()) > 0)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Mock the PDF engine factory at the import location
            with patch('src.pdf_engines.PDFEngineFactory') as mock_factory:
                mock_engine = Mock()
                mock_engine.__class__.__name__ = "ReportLabEngine"
                mock_engine.generate_pdf = Mock()
                mock_factory.create_engine.return_value = mock_engine
                
                # Call generate_pdf WITHOUT specifying engine_type (uses default 'auto')
                result = generator.generate_pdf(
                    markdown_content=markdown_content,
                    language=language,
                    template_type=template_type
                    # Note: engine_type parameter not provided, should default to 'auto'
                )
                
                # Verify auto-detection was used
                mock_factory.create_engine.assert_called_once()
                call_args = mock_factory.create_engine.call_args
                engine_type_arg = call_args[0][0]
                
                # Should use EngineType.AUTO when not specified
                assert engine_type_arg.value == 'auto', \
                    "Should default to auto-detection when engine_type not specified"
                
                # Verify PDF generation was attempted
                mock_engine.generate_pdf.assert_called_once()
                
                # Verify no errors occurred
                assert len(result.errors) == 0, \
                    f"Backward compatibility failed with errors: {result.errors}"
    
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms']),
        num_templates=st.integers(min_value=1, max_value=5)
    )
    @settings(max_examples=50)
    def test_backward_compatibility_with_toc_without_engine_flag(
        self,
        language,
        template_type,
        num_templates
    ):
        """
        Property: CLI commands with --pdf-toc but without --pdf-engine should work.
        
        **Validates: Requirements 5.1, 5.2, 5.4**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Generate template data
            templates_data = [
                (f"{i:04d}", f"Template {i}", f"# Content {i}\n\nTest content")
                for i in range(1, num_templates + 1)
            ]
            
            # Mock the PDF engine factory at the import location
            with patch('src.pdf_engines.PDFEngineFactory') as mock_factory:
                mock_engine = Mock()
                mock_engine.__class__.__name__ = "ReportLabEngine"
                mock_engine.generate_pdf = Mock()
                mock_factory.create_engine.return_value = mock_engine
                
                # Call generate_pdf_with_toc WITHOUT specifying engine_type
                result = generator.generate_pdf_with_toc(
                    templates_data=templates_data,
                    language=language,
                    template_type=template_type
                    # Note: engine_type parameter not provided, should default to 'auto'
                )
                
                # Verify auto-detection was used
                mock_factory.create_engine.assert_called_once()
                call_args = mock_factory.create_engine.call_args
                engine_type_arg = call_args[0][0]
                
                # Should use EngineType.AUTO when not specified
                assert engine_type_arg.value == 'auto', \
                    "Should default to auto-detection when engine_type not specified"
                
                # Verify PDF generation was attempted with TOC enabled
                mock_engine.generate_pdf.assert_called_once()
                gen_call_args = mock_engine.generate_pdf.call_args
                assert gen_call_args.kwargs['include_toc'] is True, \
                    "TOC should be enabled when using generate_pdf_with_toc"
                
                # Verify no errors occurred
                assert len(result.errors) == 0, \
                    f"Backward compatibility with TOC failed with errors: {result.errors}"
    
    @given(
        engine_type=st.sampled_from(['reportlab', 'weasyprint', 'auto'])
    )
    @settings(max_examples=30)
    def test_engine_type_routing_property(self, engine_type):
        """
        Property: Engine type should be correctly routed to factory.
        
        **Validates: Requirements 3.1, 3.2, 3.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Mock the PDF engine factory at the import location
            with patch('src.pdf_engines.PDFEngineFactory') as mock_factory:
                mock_engine = Mock()
                mock_engine.__class__.__name__ = "TestEngine"
                mock_engine.generate_pdf = Mock()
                mock_factory.create_engine.return_value = mock_engine
                
                # Call generate_pdf with specific engine_type
                result = generator.generate_pdf(
                    markdown_content="# Test",
                    language="en",
                    template_type="test",
                    engine_type=engine_type
                )
                
                # Verify correct engine type was passed to factory
                mock_factory.create_engine.assert_called_once()
                call_args = mock_factory.create_engine.call_args
                engine_type_arg = call_args[0][0]
                
                assert engine_type_arg.value == engine_type, \
                    f"Engine type {engine_type} should be correctly routed to factory"
