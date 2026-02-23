"""Unit tests for PDF engine factory error handling."""

import pytest
from unittest.mock import patch, MagicMock

from src.pdf_engines import (
    EngineType,
    PDFEngineFactory,
    PDFEngineNotAvailableError,
    ReportLabEngine,
    WeasyPrintEngine
)


class TestFactoryErrorHandling:
    """Test error handling in PDF engine factory."""
    
    def test_error_when_no_engines_available(self):
        """
        Test that factory raises error with installation instructions
        when no engines are available.
        
        Validates: Requirements 3.6, 4.1, 4.2
        """
        # Mock both engines as unavailable
        with patch.object(ReportLabEngine, 'is_available', return_value=False), \
             patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.AUTO)
            
            # Verify error message contains installation instructions
            error_message = str(exc_info.value)
            assert "no pdf engines available" in error_message.lower()
            assert "pip install" in error_message
            assert "reportlab" in error_message.lower()
    
    def test_error_when_reportlab_unavailable(self):
        """
        Test that factory raises error when ReportLab is specifically
        requested but not available.
        
        Validates: Requirements 3.6, 4.1, 4.2
        """
        # Mock ReportLab as unavailable
        with patch.object(ReportLabEngine, 'is_available', return_value=False):
            
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.REPORTLAB)
            
            # Verify error message contains ReportLab installation instructions
            error_message = str(exc_info.value)
            assert "ReportLab" in error_message or "reportlab" in error_message
            assert "pip install" in error_message
            
            # Verify engine_name is set
            assert exc_info.value.engine_name == "ReportLab"
    
    def test_error_when_weasyprint_unavailable(self):
        """
        Test that factory raises error when WeasyPrint is specifically
        requested but not available.
        
        Validates: Requirements 3.6, 4.1, 4.2
        """
        # Mock WeasyPrint as unavailable
        with patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            
            with pytest.raises(PDFEngineNotAvailableError) as exc_info:
                PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
            
            # Verify error message contains WeasyPrint installation instructions
            error_message = str(exc_info.value)
            assert "WeasyPrint" in error_message or "weasyprint" in error_message
            assert "pip install" in error_message
            
            # Verify engine_name is set
            assert exc_info.value.engine_name == "WeasyPrint"
    
    def test_installation_instructions_in_error_messages(self):
        """
        Test that error messages include specific installation instructions
        for each engine type.
        
        Validates: Requirements 4.1, 4.2
        """
        # Test ReportLab installation instructions
        with patch.object(ReportLabEngine, 'is_available', return_value=False):
            try:
                PDFEngineFactory.create_engine(EngineType.REPORTLAB)
                pytest.fail("Should have raised PDFEngineNotAvailableError")
            except PDFEngineNotAvailableError as e:
                error_message = str(e)
                # Should contain pip install command
                assert "pip install" in error_message
                assert "reportlab" in error_message.lower()
                assert "markdown" in error_message.lower()
        
        # Test WeasyPrint installation instructions
        with patch.object(WeasyPrintEngine, 'is_available', return_value=False):
            try:
                PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
                pytest.fail("Should have raised PDFEngineNotAvailableError")
            except PDFEngineNotAvailableError as e:
                error_message = str(e)
                # Should contain pip install command
                assert "pip install" in error_message
                assert "weasyprint" in error_message.lower()
                # Should mention system dependencies
                assert "dependencies" in error_message.lower() or "pango" in error_message.lower()
    
    def test_invalid_engine_type_raises_value_error(self):
        """
        Test that factory raises ValueError for invalid engine types.
        """
        # Create a mock invalid enum value
        class InvalidEngineType:
            pass
        
        invalid_type = InvalidEngineType()
        
        with pytest.raises(ValueError) as exc_info:
            PDFEngineFactory.create_engine(invalid_type)
        
        assert "Unknown engine type" in str(exc_info.value)
    
    def test_auto_detection_fallback_to_weasyprint(self):
        """
        Test that auto-detection falls back to WeasyPrint when
        ReportLab is unavailable but WeasyPrint is available.
        
        Validates: Requirements 3.5, 3.6
        """
        # Mock ReportLab as unavailable, WeasyPrint as available
        with patch.object(ReportLabEngine, 'is_available', return_value=False), \
             patch.object(WeasyPrintEngine, 'is_available', return_value=True):
            
            engine = PDFEngineFactory.create_engine(EngineType.AUTO)
            
            # Should return WeasyPrint engine
            assert isinstance(engine, WeasyPrintEngine)
            assert not isinstance(engine, ReportLabEngine)
    
    def test_reportlab_engine_availability_check(self):
        """
        Test that ReportLab engine is only created when available.
        
        Validates: Requirements 3.6
        """
        # When ReportLab is available
        if ReportLabEngine().is_available():
            engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
            assert isinstance(engine, ReportLabEngine)
            assert engine.is_available()
        else:
            # When ReportLab is not available
            with pytest.raises(PDFEngineNotAvailableError):
                PDFEngineFactory.create_engine(EngineType.REPORTLAB)
    
    def test_weasyprint_engine_availability_check(self):
        """
        Test that WeasyPrint engine is only created when available.
        
        Validates: Requirements 3.6
        """
        # When WeasyPrint is available
        if WeasyPrintEngine().is_available():
            engine = PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
            assert isinstance(engine, WeasyPrintEngine)
            assert engine.is_available()
        else:
            # When WeasyPrint is not available
            with pytest.raises(PDFEngineNotAvailableError):
                PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
