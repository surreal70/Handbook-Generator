"""Unit tests for PDF engine abstractions and exception classes."""

import pytest
from src.pdf_engines import (
    PDFEngine,
    PDFGenerationError,
    PDFEngineNotAvailableError,
    MarkdownConversionError,
)


class TestExceptionClasses:
    """Test custom exception classes."""
    
    def test_pdf_generation_error_basic(self):
        """Test basic PDFGenerationError exception."""
        error = PDFGenerationError("Test error message")
        assert str(error) == "Test error message"
        assert isinstance(error, Exception)
    
    def test_pdf_engine_not_available_error_with_engine_name(self):
        """Test PDFEngineNotAvailableError with engine name."""
        error = PDFEngineNotAvailableError(
            "Engine not found",
            engine_name="reportlab"
        )
        assert str(error) == "Engine not found"
        assert error.engine_name == "reportlab"
        assert isinstance(error, PDFGenerationError)
    
    def test_pdf_engine_not_available_error_without_engine_name(self):
        """Test PDFEngineNotAvailableError without engine name."""
        error = PDFEngineNotAvailableError("No engines available")
        assert str(error) == "No engines available"
        assert error.engine_name is None
    
    def test_markdown_conversion_error_with_snippet(self):
        """Test MarkdownConversionError with markdown snippet."""
        snippet = "# Invalid markdown\n[broken link"
        error = MarkdownConversionError(
            "Failed to parse markdown",
            markdown_snippet=snippet
        )
        assert str(error) == "Failed to parse markdown"
        assert error.markdown_snippet == snippet
        assert isinstance(error, PDFGenerationError)
    
    def test_markdown_conversion_error_without_snippet(self):
        """Test MarkdownConversionError without snippet."""
        error = MarkdownConversionError("Conversion failed")
        assert str(error) == "Conversion failed"
        assert error.markdown_snippet is None


class TestPDFEngineInterface:
    """Test PDFEngine abstract base class."""
    
    def test_cannot_instantiate_abstract_class(self):
        """Test that PDFEngine cannot be instantiated directly."""
        with pytest.raises(TypeError) as exc_info:
            PDFEngine()
        
        assert "Can't instantiate abstract class" in str(exc_info.value)
    
    def test_concrete_implementation_requires_all_methods(self):
        """Test that concrete implementations must implement all abstract methods."""
        
        # Missing all methods
        class IncompletePDFEngine(PDFEngine):
            pass
        
        with pytest.raises(TypeError) as exc_info:
            IncompletePDFEngine()
        
        error_msg = str(exc_info.value)
        assert "Can't instantiate abstract class" in error_msg
    
    def test_concrete_implementation_with_all_methods(self):
        """Test that concrete implementation with all methods can be instantiated."""
        
        class CompletePDFEngine(PDFEngine):
            def generate_pdf(self, markdown_content, output_path, 
                           include_toc=False, metadata=None):
                pass
            
            def is_available(self):
                return True
            
            def get_installation_instructions(self):
                return "Install instructions"
        
        # Should not raise an error
        engine = CompletePDFEngine()
        assert isinstance(engine, PDFEngine)
        assert engine.is_available() is True
        assert engine.get_installation_instructions() == "Install instructions"


class TestPDFEngineMethodSignatures:
    """Test that PDFEngine method signatures are correct."""
    
    def test_generate_pdf_signature(self):
        """Test generate_pdf method signature."""
        
        class TestEngine(PDFEngine):
            def generate_pdf(self, markdown_content, output_path,
                           include_toc=False, metadata=None):
                self.last_call = {
                    'markdown_content': markdown_content,
                    'output_path': output_path,
                    'include_toc': include_toc,
                    'metadata': metadata,
                }
            
            def is_available(self):
                return True
            
            def get_installation_instructions(self):
                return "Test"
        
        engine = TestEngine()
        engine.generate_pdf(
            markdown_content="# Test",
            output_path="/tmp/test.pdf",
            include_toc=True,
            metadata={'title': 'Test Doc'}
        )
        
        assert engine.last_call['markdown_content'] == "# Test"
        assert engine.last_call['output_path'] == "/tmp/test.pdf"
        assert engine.last_call['include_toc'] is True
        assert engine.last_call['metadata'] == {'title': 'Test Doc'}
    
    def test_is_available_returns_bool(self):
        """Test is_available returns boolean."""
        
        class TestEngine(PDFEngine):
            def generate_pdf(self, markdown_content, output_path,
                           include_toc=False, metadata=None):
                pass
            
            def is_available(self):
                return True
            
            def get_installation_instructions(self):
                return "Test"
        
        engine = TestEngine()
        result = engine.is_available()
        assert isinstance(result, bool)
        assert result is True
    
    def test_get_installation_instructions_returns_string(self):
        """Test get_installation_instructions returns string."""
        
        class TestEngine(PDFEngine):
            def generate_pdf(self, markdown_content, output_path,
                           include_toc=False, metadata=None):
                pass
            
            def is_available(self):
                return True
            
            def get_installation_instructions(self):
                return "Install with: pip install test-engine"
        
        engine = TestEngine()
        result = engine.get_installation_instructions()
        assert isinstance(result, str)
        assert "pip install" in result
