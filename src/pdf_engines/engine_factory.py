"""PDF engine factory for creating and managing PDF engines.

This module provides the factory pattern implementation for creating PDF engines.
It handles engine selection, auto-detection, and provides a unified interface
for engine instantiation.

The factory supports:
- Explicit engine selection (ReportLab or WeasyPrint)
- Automatic engine detection with preference order
- Graceful error handling with installation instructions

Example:
    >>> from pdf_engines import PDFEngineFactory, EngineType
    >>> 
    >>> # Auto-detect available engine
    >>> engine = PDFEngineFactory.create_engine(EngineType.AUTO)
    >>> 
    >>> # Explicitly request ReportLab
    >>> engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
    >>> 
    >>> # Generate PDF
    >>> engine.generate_pdf("# Hello", "output.pdf")
"""

from enum import Enum
from typing import Optional

from . import PDFEngine, PDFEngineNotAvailableError
from .reportlab_engine import ReportLabEngine
from .weasyprint_engine import WeasyPrintEngine


class EngineType(Enum):
    """Available PDF engine types.
    
    This enumeration defines the supported PDF engines and the auto-detection mode.
    
    Attributes:
        REPORTLAB: Pure Python engine (no system dependencies)
        WEASYPRINT: Advanced engine (requires system libraries)
        AUTO: Automatic detection (prefers ReportLab for portability)
    
    Example:
        >>> engine_type = EngineType.REPORTLAB
        >>> engine = PDFEngineFactory.create_engine(engine_type)
    """
    REPORTLAB = "reportlab"
    WEASYPRINT = "weasyprint"
    AUTO = "auto"


class PDFEngineFactory:
    """Factory for creating and managing PDF engines.
    
    This factory class provides static methods for creating PDF engine instances.
    It implements the Factory design pattern to abstract engine creation and
    provide a consistent interface for engine instantiation.
    
    The factory handles:
    - Engine type routing (ReportLab, WeasyPrint, Auto)
    - Availability checking before instantiation
    - Error handling with helpful installation instructions
    - Auto-detection with preference order (ReportLab > WeasyPrint)
    
    All methods are static, so no instance creation is needed.
    
    Example:
        >>> # Auto-detect and create engine
        >>> engine = PDFEngineFactory.create_engine(EngineType.AUTO)
        >>> 
        >>> # Create specific engine
        >>> engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
        >>> 
        >>> # Use the engine
        >>> engine.generate_pdf("# Title", "output.pdf")
    """
    
    @staticmethod
    def create_engine(engine_type: EngineType = EngineType.AUTO) -> PDFEngine:
        """Create a PDF engine based on the specified type.
        
        This is the main entry point for creating PDF engines. It routes to
        the appropriate creation method based on the engine type.
        
        Engine Selection Logic:
        - AUTO: Calls _auto_detect_engine() to find first available engine
        - REPORTLAB: Calls _create_reportlab_engine() to create ReportLab instance
        - WEASYPRINT: Calls _create_weasyprint_engine() to create WeasyPrint instance
        
        Args:
            engine_type: The type of engine to create (default: AUTO)
        
        Returns:
            An instance of a PDFEngine (ReportLabEngine or WeasyPrintEngine)
        
        Raises:
            PDFEngineNotAvailableError: If the requested engine is not available
            ValueError: If an unknown engine type is specified
        
        Example:
            >>> # Auto-detect
            >>> engine = PDFEngineFactory.create_engine()
            >>> 
            >>> # Explicit selection
            >>> engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
            >>> 
            >>> # From string (CLI usage)
            >>> engine_type = EngineType("reportlab")
            >>> engine = PDFEngineFactory.create_engine(engine_type)
        """
        if engine_type == EngineType.AUTO:
            return PDFEngineFactory._auto_detect_engine()
        elif engine_type == EngineType.REPORTLAB:
            return PDFEngineFactory._create_reportlab_engine()
        elif engine_type == EngineType.WEASYPRINT:
            return PDFEngineFactory._create_weasyprint_engine()
        else:
            raise ValueError(f"Unknown engine type: {engine_type}")
    
    @staticmethod
    def _auto_detect_engine() -> PDFEngine:
        """Auto-detect and return the first available engine.
        
        This method implements the auto-detection logic with a preference order
        that prioritizes portability and ease of installation.
        
        Detection Order (by design):
        1. ReportLab: Pure Python, no system dependencies (preferred)
        2. WeasyPrint: Requires system libraries (fallback)
        
        The preference for ReportLab ensures maximum portability across platforms
        and simplifies deployment in containerized environments.
        
        Returns:
            An available PDFEngine instance (ReportLabEngine or WeasyPrintEngine)
        
        Raises:
            PDFEngineNotAvailableError: If no engines are available
        
        Example:
            >>> try:
            ...     engine = PDFEngineFactory._auto_detect_engine()
            ...     print(f"Using {type(engine).__name__}")
            ... except PDFEngineNotAvailableError as e:
            ...     print(f"No engines available: {e}")
        """
        # Try ReportLab first (pure Python, better portability)
        reportlab_engine = ReportLabEngine()
        if reportlab_engine.is_available():
            return reportlab_engine
        
        # Try WeasyPrint as fallback (requires system libraries)
        weasyprint_engine = WeasyPrintEngine()
        if weasyprint_engine.is_available():
            return weasyprint_engine
        
        # No engines available - provide comprehensive installation guidance
        error_msg = (
            "No PDF Engines Available: Neither ReportLab nor WeasyPrint could be found.\n\n"
            "Recommended Solution (Pure Python):\n"
            "  Install ReportLab for a dependency-free solution:\n"
            "  pip install reportlab markdown\n\n"
            "Alternative Solution (Advanced Features):\n"
            "  Install WeasyPrint (requires system libraries):\n"
            "  pip install weasyprint\n"
            "  System dependencies: libpango (see platform-specific instructions)\n\n"
            "Troubleshooting:\n"
            "  1. Verify you're in the correct virtual environment\n"
            "  2. Check installed packages: pip list\n"
            "  3. Try installing with verbose output: pip install -v reportlab\n"
            "  4. Ensure pip is up to date: pip install --upgrade pip\n"
        )
        raise PDFEngineNotAvailableError(error_msg)
    
    @staticmethod
    def _create_reportlab_engine() -> PDFEngine:
        """Create ReportLab engine or raise error if unavailable.
        
        This method creates a ReportLabEngine instance after verifying that
        ReportLab is available. If ReportLab is not installed, it raises
        an error with installation instructions.
        
        Returns:
            ReportLabEngine instance
        
        Raises:
            PDFEngineNotAvailableError: If ReportLab is not available
        
        Example:
            >>> try:
            ...     engine = PDFEngineFactory._create_reportlab_engine()
            ... except PDFEngineNotAvailableError as e:
            ...     print(f"ReportLab not available: {e}")
        """
        engine = ReportLabEngine()
        if not engine.is_available():
            raise PDFEngineNotAvailableError(
                engine.get_installation_instructions(),
                engine_name="ReportLab"
            )
        return engine
    
    @staticmethod
    def _create_weasyprint_engine() -> PDFEngine:
        """Create WeasyPrint engine or raise error if unavailable.
        
        This method creates a WeasyPrintEngine instance after verifying that
        WeasyPrint and its system dependencies are available. If WeasyPrint
        is not installed or system libraries are missing, it raises an error
        with installation instructions and suggests ReportLab as an alternative.
        
        Returns:
            WeasyPrintEngine instance
        
        Raises:
            PDFEngineNotAvailableError: If WeasyPrint is not available
        
        Example:
            >>> try:
            ...     engine = PDFEngineFactory._create_weasyprint_engine()
            ... except PDFEngineNotAvailableError as e:
            ...     print(f"WeasyPrint not available: {e}")
            ...     # Error message includes ReportLab alternative
        """
        engine = WeasyPrintEngine()
        if not engine.is_available():
            error_msg = (
                f"{engine.get_installation_instructions()}\n\n"
                f"Alternative: For a pure Python solution without system dependencies,\n"
                f"consider using ReportLab instead:\n"
                f"  pip install reportlab markdown\n"
                f"  Use with: --pdf-engine reportlab"
            )
            raise PDFEngineNotAvailableError(
                error_msg,
                engine_name="WeasyPrint"
            )
        return engine


__all__ = ['EngineType', 'PDFEngineFactory']
