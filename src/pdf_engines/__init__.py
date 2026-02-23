"""PDF engine abstraction layer for flexible PDF generation.

This module provides the core abstractions for PDF generation engines,
including the base PDFEngine interface and custom exception classes.
It enables flexible PDF generation with multiple backend engines
(ReportLab, WeasyPrint) through a common interface.

Example:
    >>> from pdf_engines import PDFEngineFactory, EngineType
    >>> engine = PDFEngineFactory.create_engine(EngineType.REPORTLAB)
    >>> engine.generate_pdf("# Hello", "output.pdf")
"""

from abc import ABC, abstractmethod
from typing import Optional


class PDFGenerationError(Exception):
    """Base exception for PDF generation errors.
    
    This is the parent exception for all PDF-related errors in the system.
    Catching this exception will catch all PDF generation failures.
    
    Attributes:
        message: Human-readable error description
    """
    pass


class PDFEngineNotAvailableError(PDFGenerationError):
    """Raised when a requested PDF engine is not available.
    
    This exception is raised when:
    - The requested engine's dependencies are not installed
    - System libraries required by the engine are missing
    - The engine fails its availability check
    
    Attributes:
        message: Human-readable error description with installation instructions
        engine_name: Name of the unavailable engine (e.g., "ReportLab", "WeasyPrint")
    
    Example:
        >>> try:
        ...     engine = PDFEngineFactory.create_engine(EngineType.WEASYPRINT)
        ... except PDFEngineNotAvailableError as e:
        ...     print(f"Engine {e.engine_name} not available: {e}")
    """
    
    def __init__(self, message: str, engine_name: Optional[str] = None) -> None:
        """Initialize the exception.
        
        Args:
            message: Error message with installation instructions
            engine_name: Optional name of the unavailable engine
        """
        super().__init__(message)
        self.engine_name = engine_name


class MarkdownConversionError(PDFGenerationError):
    """Raised when markdown conversion fails.
    
    This exception is raised when the markdown-to-HTML conversion fails,
    typically due to malformed markdown syntax or unsupported markdown features.
    
    Attributes:
        message: Human-readable error description
        markdown_snippet: Optional snippet of problematic markdown content
    
    Example:
        >>> try:
        ...     html = markdown.markdown(bad_markdown)
        ... except Exception as e:
        ...     raise MarkdownConversionError(str(e), bad_markdown[:200])
    """
    
    def __init__(self, message: str, markdown_snippet: Optional[str] = None) -> None:
        """Initialize the exception.
        
        Args:
            message: Error message describing the conversion failure
            markdown_snippet: Optional snippet of the problematic markdown
        """
        super().__init__(message)
        self.markdown_snippet = markdown_snippet


class PDFEngine(ABC):
    """Abstract base class for PDF generation engines.
    
    This abstract class defines the interface that all PDF engines must implement.
    It provides a consistent API for PDF generation regardless of the underlying
    engine (ReportLab, WeasyPrint, etc.).
    
    Implementing classes must provide:
    - generate_pdf(): Convert markdown to PDF
    - is_available(): Check if engine dependencies are installed
    - get_installation_instructions(): Provide installation guidance
    
    Example:
        >>> class MyEngine(PDFEngine):
        ...     def generate_pdf(self, markdown_content, output_path, **kwargs):
        ...         # Implementation here
        ...         pass
        ...     def is_available(self):
        ...         return True
        ...     def get_installation_instructions(self):
        ...         return "pip install my-engine"
    """
    
    @abstractmethod
    def generate_pdf(
        self,
        markdown_content: str,
        output_path: str,
        include_toc: bool = False,
        metadata: Optional[dict] = None
    ) -> None:
        """Generate a PDF from markdown content.
        
        This method converts markdown text to a formatted PDF document.
        The implementation should handle markdown parsing, styling, and
        PDF generation using the engine's specific capabilities.
        
        Args:
            markdown_content: The markdown text to convert to PDF
            output_path: Filesystem path where the PDF should be saved
            include_toc: Whether to include a table of contents in the PDF
            metadata: Optional dictionary with document metadata:
                - title: Document title
                - author: Document author
                - subject: Document subject
                - keywords: List of keywords
        
        Raises:
            PDFGenerationError: If PDF generation fails for any reason
            MarkdownConversionError: If markdown parsing fails
            PDFEngineNotAvailableError: If engine dependencies are missing
        
        Example:
            >>> engine = ReportLabEngine()
            >>> engine.generate_pdf(
            ...     "# Hello World\\n\\nThis is a test.",
            ...     "output.pdf",
            ...     include_toc=True,
            ...     metadata={"title": "Test Document"}
            ... )
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if this engine is available (dependencies installed).
        
        This method verifies that all required dependencies for the engine
        are installed and functional. It should perform a lightweight check
        without generating actual PDFs if possible.
        
        Returns:
            True if the engine can be used, False otherwise
        
        Example:
            >>> engine = ReportLabEngine()
            >>> if engine.is_available():
            ...     engine.generate_pdf(content, path)
            ... else:
            ...     print(engine.get_installation_instructions())
        """
        pass
    
    @abstractmethod
    def get_installation_instructions(self) -> str:
        """Get instructions for installing this engine.
        
        This method returns human-readable instructions for installing
        the engine's dependencies. Instructions should be platform-specific
        when necessary and include both Python packages and system libraries.
        
        Returns:
            Multi-line string with installation instructions
        
        Example:
            >>> engine = WeasyPrintEngine()
            >>> if not engine.is_available():
            ...     print(engine.get_installation_instructions())
            WeasyPrint is not installed. Install it with:
              pip install weasyprint
            ...
        """
        pass


from .reportlab_engine import ReportLabEngine
from .weasyprint_engine import WeasyPrintEngine
from .engine_factory import EngineType, PDFEngineFactory


__all__ = [
    'PDFEngine',
    'PDFGenerationError',
    'PDFEngineNotAvailableError',
    'MarkdownConversionError',
    'ReportLabEngine',
    'WeasyPrintEngine',
    'EngineType',
    'PDFEngineFactory',
]
