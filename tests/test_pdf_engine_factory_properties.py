"""Property-based tests for PDF engine factory."""

import pytest
from hypothesis import given, strategies as st, settings, assume
import tempfile
import os

from src.pdf_engines import (
    EngineType,
    PDFEngineFactory,
    PDFEngineNotAvailableError,
    ReportLabEngine,
    WeasyPrintEngine
)


# Feature: pdf-generation-without-dependencies, Property 1: Engine Selection Routing
@given(
    engine_choice=st.sampled_from([
        EngineType.REPORTLAB,
        EngineType.WEASYPRINT,
        EngineType.AUTO
    ])
)
@settings(max_examples=100)
def test_engine_selection_routing(engine_choice):
    """
    Property 1: Engine Selection Routing
    
    For any valid engine type specification (reportlab, weasyprint, auto),
    when the user provides the engine type, the system should route to and
    use the corresponding PDF engine.
    
    Validates: Requirements 1.1, 2.1, 3.1, 3.2, 3.3
    """
    # Skip if the requested engine is not available
    if engine_choice == EngineType.REPORTLAB:
        test_engine = ReportLabEngine()
        if not test_engine.is_available():
            assume(False)  # Skip this test case
    elif engine_choice == EngineType.WEASYPRINT:
        test_engine = WeasyPrintEngine()
        if not test_engine.is_available():
            assume(False)  # Skip this test case
    elif engine_choice == EngineType.AUTO:
        # For AUTO, at least one engine must be available
        reportlab_available = ReportLabEngine().is_available()
        weasyprint_available = WeasyPrintEngine().is_available()
        if not (reportlab_available or weasyprint_available):
            assume(False)  # Skip if no engines available
    
    # Create engine using factory
    try:
        engine = PDFEngineFactory.create_engine(engine_choice)
        
        # Verify the correct engine type was created
        if engine_choice == EngineType.REPORTLAB:
            assert isinstance(engine, ReportLabEngine), \
                f"Expected ReportLabEngine but got {type(engine).__name__}"
        elif engine_choice == EngineType.WEASYPRINT:
            assert isinstance(engine, WeasyPrintEngine), \
                f"Expected WeasyPrintEngine but got {type(engine).__name__}"
        elif engine_choice == EngineType.AUTO:
            # AUTO should return either ReportLab or WeasyPrint
            assert isinstance(engine, (ReportLabEngine, WeasyPrintEngine)), \
                f"Expected ReportLabEngine or WeasyPrintEngine but got {type(engine).__name__}"
            
            # Verify preference order: ReportLab should be preferred over WeasyPrint
            if ReportLabEngine().is_available():
                assert isinstance(engine, ReportLabEngine), \
                    "AUTO mode should prefer ReportLab when available"
        
        # Verify the engine is actually available
        assert engine.is_available(), \
            f"Factory returned an unavailable engine: {type(engine).__name__}"
        
    except PDFEngineNotAvailableError:
        # This should only happen if the engine is truly unavailable
        pytest.fail(f"Factory raised PDFEngineNotAvailableError for available engine: {engine_choice}")


# Feature: pdf-generation-without-dependencies, Property 3: Auto-Detection Preference Order
def test_auto_detection_preference_order():
    """
    Property 3: Auto-Detection Preference Order
    
    For any system state where both ReportLab and WeasyPrint are available,
    when auto-detection runs, the system should select ReportLab over WeasyPrint.
    
    Validates: Requirements 3.5
    """
    reportlab_available = ReportLabEngine().is_available()
    weasyprint_available = WeasyPrintEngine().is_available()
    
    # Only run this test if both engines are available
    if not (reportlab_available and weasyprint_available):
        pytest.skip("Both engines must be available to test preference order")
    
    # Create engine using AUTO mode
    engine = PDFEngineFactory.create_engine(EngineType.AUTO)
    
    # Verify ReportLab is selected
    assert isinstance(engine, ReportLabEngine), \
        "AUTO mode should prefer ReportLab when both engines are available"
    
    # Verify it's not WeasyPrint
    assert not isinstance(engine, WeasyPrintEngine), \
        "AUTO mode should not select WeasyPrint when ReportLab is available"
