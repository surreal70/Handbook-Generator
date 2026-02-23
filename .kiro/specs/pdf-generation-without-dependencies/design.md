# Design Document: PDF Generation Without Dependencies

## Overview

This design implements a flexible PDF generation system that supports multiple PDF engines (ReportLab and WeasyPrint) with automatic detection and graceful fallback. The solution eliminates mandatory system dependencies by making ReportLab the default engine while keeping WeasyPrint as an optional advanced engine.

The architecture introduces an abstraction layer for PDF engines, allowing the system to dynamically select and use different PDF generation backends based on availability and user preference. This approach maintains backward compatibility while significantly improving portability.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLI Interface                         │
│              (handbook-generator)                        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Output Generator                            │
│         (output_generator.py)                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           PDF Engine Factory                             │
│         (pdf_engine_factory.py)                         │
│  - Engine detection                                      │
│  - Engine selection                                      │
│  - Error handling                                        │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
┌──────────────────┐    ┌──────────────────┐
│  ReportLab       │    │  WeasyPrint      │
│  Engine          │    │  Engine          │
│  (Pure Python)   │    │  (Advanced)      │
└──────────────────┘    └──────────────────┘
```

### Design Principles

1. **Abstraction**: Common interface for all PDF engines
2. **Portability**: Default to pure Python solutions
3. **Flexibility**: Allow users to choose their preferred engine
4. **Graceful Degradation**: Clear error messages when engines unavailable
5. **Backward Compatibility**: Existing CLI commands continue to work

## Components and Interfaces

### 1. PDF Engine Interface (Abstract Base Class)

```python
from abc import ABC, abstractmethod
from typing import Optional

class PDFEngine(ABC):
    """Abstract base class for PDF generation engines."""
    
    @abstractmethod
    def generate_pdf(
        self,
        markdown_content: str,
        output_path: str,
        include_toc: bool = False,
        metadata: Optional[dict] = None
    ) -> None:
        """
        Generate a PDF from markdown content.
        
        Args:
            markdown_content: The markdown text to convert
            output_path: Path where the PDF should be saved
            include_toc: Whether to include a table of contents
            metadata: Optional metadata (title, author, etc.)
        
        Raises:
            PDFGenerationError: If PDF generation fails
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """
        Check if this engine is available (dependencies installed).
        
        Returns:
            True if the engine can be used, False otherwise
        """
        pass
    
    @abstractmethod
    def get_installation_instructions(self) -> str:
        """
        Get instructions for installing this engine.
        
        Returns:
            String with installation instructions
        """
        pass
```

### 2. ReportLab Engine Implementation

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus import TableOfContents
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import markdown

class ReportLabEngine(PDFEngine):
    """PDF engine using ReportLab (pure Python, no system dependencies)."""
    
    def generate_pdf(
        self,
        markdown_content: str,
        output_path: str,
        include_toc: bool = False,
        metadata: Optional[dict] = None
    ) -> None:
        """Generate PDF using ReportLab."""
        # Convert markdown to HTML
        html_content = markdown.markdown(
            markdown_content,
            extensions=['extra', 'codehilite', 'toc']
        )
        
        # Create PDF document
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Build story (content elements)
        story = []
        styles = getSampleStyleSheet()
        
        if include_toc:
            toc = TableOfContents()
            story.append(toc)
            story.append(PageBreak())
        
        # Parse HTML and convert to ReportLab elements
        elements = self._html_to_reportlab(html_content, styles)
        story.extend(elements)
        
        # Build PDF
        doc.build(story)
    
    def is_available(self) -> bool:
        """Check if ReportLab is installed."""
        try:
            import reportlab
            return True
        except ImportError:
            return False
    
    def get_installation_instructions(self) -> str:
        """Get ReportLab installation instructions."""
        return (
            "ReportLab is not installed. Install it with:\n"
            "  pip install reportlab markdown"
        )
    
    def _html_to_reportlab(self, html: str, styles) -> list:
        """Convert HTML to ReportLab flowable elements."""
        # Implementation details for parsing HTML and creating
        # ReportLab Paragraph, Spacer, and other elements
        pass
```

### 3. WeasyPrint Engine Implementation

```python
from weasyprint import HTML, CSS
import markdown

class WeasyPrintEngine(PDFEngine):
    """PDF engine using WeasyPrint (requires system dependencies)."""
    
    def generate_pdf(
        self,
        markdown_content: str,
        output_path: str,
        include_toc: bool = False,
        metadata: Optional[dict] = None
    ) -> None:
        """Generate PDF using WeasyPrint."""
        # Convert markdown to HTML
        html_content = markdown.markdown(
            markdown_content,
            extensions=['extra', 'codehilite', 'toc']
        )
        
        # Add CSS styling
        css_content = self._get_default_css()
        
        # Generate PDF
        HTML(string=html_content).write_pdf(
            output_path,
            stylesheets=[CSS(string=css_content)]
        )
    
    def is_available(self) -> bool:
        """Check if WeasyPrint is installed and functional."""
        try:
            import weasyprint
            # Try to create a simple document to verify system deps
            HTML(string="<p>test</p>").write_pdf()
            return True
        except (ImportError, OSError):
            return False
    
    def get_installation_instructions(self) -> str:
        """Get WeasyPrint installation instructions."""
        return (
            "WeasyPrint is not installed or missing system dependencies.\n"
            "Install it with:\n"
            "  pip install weasyprint\n"
            "\n"
            "System dependencies required:\n"
            "  Ubuntu/Debian: sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0\n"
            "  macOS: brew install pango\n"
            "  Windows: See https://doc.courtbouillon.org/weasyprint/stable/first_steps.html"
        )
    
    def _get_default_css(self) -> str:
        """Get default CSS styling for PDF."""
        return """
            @page {
                size: A4;
                margin: 2cm;
            }
            body {
                font-family: sans-serif;
                font-size: 11pt;
                line-height: 1.5;
            }
            h1, h2, h3 {
                color: #333;
            }
            code {
                font-family: monospace;
                background-color: #f5f5f5;
                padding: 2px 4px;
            }
        """
```

### 4. PDF Engine Factory

```python
from enum import Enum
from typing import Optional

class EngineType(Enum):
    """Available PDF engine types."""
    REPORTLAB = "reportlab"
    WEASYPRINT = "weasyprint"
    AUTO = "auto"

class PDFEngineFactory:
    """Factory for creating and managing PDF engines."""
    
    @staticmethod
    def create_engine(engine_type: EngineType = EngineType.AUTO) -> PDFEngine:
        """
        Create a PDF engine based on the specified type.
        
        Args:
            engine_type: The type of engine to create (or AUTO for detection)
        
        Returns:
            An instance of a PDFEngine
        
        Raises:
            PDFEngineNotAvailableError: If the requested engine is not available
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
        """
        Auto-detect and return the first available engine.
        Preference order: ReportLab > WeasyPrint
        """
        # Try ReportLab first (pure Python, better portability)
        reportlab_engine = ReportLabEngine()
        if reportlab_engine.is_available():
            return reportlab_engine
        
        # Try WeasyPrint as fallback
        weasyprint_engine = WeasyPrintEngine()
        if weasyprint_engine.is_available():
            return weasyprint_engine
        
        # No engines available
        raise PDFEngineNotAvailableError(
            "No PDF engines available. Install ReportLab with:\n"
            "  pip install reportlab markdown"
        )
    
    @staticmethod
    def _create_reportlab_engine() -> PDFEngine:
        """Create ReportLab engine or raise error if unavailable."""
        engine = ReportLabEngine()
        if not engine.is_available():
            raise PDFEngineNotAvailableError(
                engine.get_installation_instructions()
            )
        return engine
    
    @staticmethod
    def _create_weasyprint_engine() -> PDFEngine:
        """Create WeasyPrint engine or raise error if unavailable."""
        engine = WeasyPrintEngine()
        if not engine.is_available():
            raise PDFEngineNotAvailableError(
                engine.get_installation_instructions()
            )
        return engine

class PDFEngineNotAvailableError(Exception):
    """Raised when a requested PDF engine is not available."""
    pass
```

### 5. CLI Integration

```python
import argparse

def setup_cli_arguments(parser: argparse.ArgumentParser) -> None:
    """Add PDF engine selection argument to CLI."""
    parser.add_argument(
        '--pdf-engine',
        type=str,
        choices=['reportlab', 'weasyprint', 'auto'],
        default='auto',
        help='PDF generation engine to use (default: auto-detect)'
    )
    
    parser.add_argument(
        '--pdf-toc',
        action='store_true',
        help='Include table of contents in PDF output'
    )

def generate_pdf_output(
    content: str,
    output_path: str,
    engine_type: str = 'auto',
    include_toc: bool = False
) -> None:
    """
    Generate PDF output using the specified engine.
    
    Args:
        content: Markdown content to convert
        output_path: Path for the output PDF file
        engine_type: Engine to use ('reportlab', 'weasyprint', or 'auto')
        include_toc: Whether to include table of contents
    """
    try:
        # Create engine
        engine_enum = EngineType(engine_type)
        engine = PDFEngineFactory.create_engine(engine_enum)
        
        # Generate PDF
        engine.generate_pdf(
            markdown_content=content,
            output_path=output_path,
            include_toc=include_toc
        )
        
        print(f"PDF generated successfully: {output_path}")
        print(f"Engine used: {type(engine).__name__}")
        
    except PDFEngineNotAvailableError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"PDF generation failed: {e}", file=sys.stderr)
        sys.exit(1)
```

## Data Models

### Engine Configuration

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class PDFMetadata:
    """Metadata for PDF documents."""
    title: Optional[str] = None
    author: Optional[str] = None
    subject: Optional[str] = None
    keywords: Optional[list[str]] = None

@dataclass
class PDFGenerationConfig:
    """Configuration for PDF generation."""
    engine_type: EngineType
    include_toc: bool
    metadata: Optional[PDFMetadata] = None
    page_size: str = "A4"
    margin_size: float = 2.0  # in cm
```

### Markdown Processing

The system uses the Python `markdown` library with the following extensions:
- `extra`: Additional markdown features (tables, footnotes, etc.)
- `codehilite`: Syntax highlighting for code blocks
- `toc`: Table of contents generation

## Correctness Properties


A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.

### Property 1: Engine Selection Routing

*For any* valid engine type specification (reportlab, weasyprint, auto), when the user provides the `--pdf-engine` flag with that value, the system should route to and use the corresponding PDF engine.

**Validates: Requirements 1.1, 2.1, 3.1, 3.2, 3.3**

### Property 2: Markdown Element Preservation

*For any* markdown content containing headings, paragraphs, lists, code blocks, and text emphasis (bold, italic), when either PDF engine generates a PDF, the output should preserve all these structural and formatting elements.

**Validates: Requirements 1.2, 1.5, 6.2, 6.4, 6.5**

### Property 3: Auto-Detection Preference Order

*For any* system state where both ReportLab and WeasyPrint are available, when auto-detection runs, the system should select ReportLab over WeasyPrint.

**Validates: Requirements 3.5**

### Property 4: Table of Contents Generation

*For any* markdown content with multiple heading levels, when TOC is enabled (via `--pdf-toc` flag), the PDF engine should generate a table of contents with clickable entries that have accurate page numbers, regardless of which engine is used.

**Validates: Requirements 1.4, 5.2, 6.3**

### Property 5: Error Messages Include Installation Instructions

*For any* PDF engine that is unavailable (not installed or missing dependencies), when the system attempts to use that engine, it should raise an error message that includes specific installation instructions for that engine.

**Validates: Requirements 2.2, 4.1, 4.3**

### Property 6: Code Block Monospace Rendering

*For any* markdown content containing code blocks, when a PDF engine generates the PDF, all code blocks should be rendered using a monospace font family.

**Validates: Requirements 6.4**

### Property 7: PDF Quality Standards

*For any* generated PDF using ReportLab, the output should have readable fonts (minimum 9pt), proper line spacing (minimum 1.2), and adequate margins (minimum 1.5cm).

**Validates: Requirements 6.1**

### Property 8: Engine Availability Check

*For any* PDF engine implementation, the `is_available()` method should return True if and only if all required dependencies are installed and functional.

**Validates: Requirements 1.3, 7.1, 7.2**

### Property 9: Backward Compatibility with Output Flag

*For any* existing CLI command using `-o pdf` without the `--pdf-engine` flag, the system should successfully generate a PDF using the auto-detected engine.

**Validates: Requirements 5.1, 5.4**

### Property 10: WeasyPrint CSS Styling Support

*For any* CSS stylesheet provided to WeasyPrint engine, the generated PDF should apply the CSS rules to the document layout and styling.

**Validates: Requirements 2.4**

## Error Handling

### Error Types

1. **PDFEngineNotAvailableError**: Raised when a requested engine is not installed or functional
   - Contains installation instructions
   - Includes specific error details (missing packages, system dependencies)

2. **PDFGenerationError**: Raised when PDF generation fails during processing
   - Contains the original error message
   - Includes troubleshooting guidance
   - Logs full stack trace for debugging

3. **MarkdownConversionError**: Raised when markdown parsing fails
   - Contains the problematic markdown section
   - Suggests corrections

### Error Handling Strategy

```python
class PDFGenerationError(Exception):
    """Base exception for PDF generation errors."""
    pass

class PDFEngineNotAvailableError(PDFGenerationError):
    """Raised when a PDF engine is not available."""
    
    def __init__(self, message: str, engine_name: str):
        super().__init__(message)
        self.engine_name = engine_name

class MarkdownConversionError(PDFGenerationError):
    """Raised when markdown conversion fails."""
    
    def __init__(self, message: str, markdown_snippet: str):
        super().__init__(message)
        self.markdown_snippet = markdown_snippet
```

### Error Recovery

1. **Auto-detection fallback**: If preferred engine fails, try next available engine
2. **Graceful degradation**: If TOC generation fails, generate PDF without TOC and warn user
3. **Detailed logging**: Log all errors with context for troubleshooting

## Testing Strategy

### Dual Testing Approach

This feature requires both unit tests and property-based tests for comprehensive coverage:

- **Unit tests**: Verify specific examples, edge cases, and error conditions
- **Property tests**: Verify universal properties across all inputs

### Property-Based Testing

We will use **Hypothesis** (Python's property-based testing library) to implement the correctness properties defined above. Each property test will:

- Run a minimum of 100 iterations with randomized inputs
- Be tagged with a comment referencing the design property
- Tag format: `# Feature: pdf-generation-without-dependencies, Property N: [property text]`

Example property test structure:

```python
from hypothesis import given, strategies as st
import hypothesis

# Feature: pdf-generation-without-dependencies, Property 2: Markdown Element Preservation
@given(
    headings=st.lists(st.text(min_size=1, max_size=100), min_size=1, max_size=5),
    paragraphs=st.lists(st.text(min_size=10, max_size=500), min_size=1, max_size=10),
    code_blocks=st.lists(st.text(min_size=5, max_size=200), min_size=0, max_size=3)
)
@hypothesis.settings(max_examples=100)
def test_markdown_element_preservation(headings, paragraphs, code_blocks):
    """Property: All markdown elements should be preserved in PDF output."""
    # Generate markdown with various elements
    markdown_content = generate_markdown(headings, paragraphs, code_blocks)
    
    # Generate PDF with both engines
    for engine_type in [EngineType.REPORTLAB, EngineType.WEASYPRINT]:
        if not is_engine_available(engine_type):
            continue
            
        pdf_path = generate_test_pdf(markdown_content, engine_type)
        pdf_text = extract_text_from_pdf(pdf_path)
        
        # Verify all elements are present
        for heading in headings:
            assert heading in pdf_text
        for paragraph in paragraphs:
            assert paragraph in pdf_text
```

### Unit Testing Focus Areas

Unit tests should focus on:

1. **Specific examples**: Test known markdown documents with expected outputs
2. **Edge cases**:
   - Empty markdown content
   - Very large documents (>1000 pages)
   - Special characters and Unicode
   - Malformed markdown
3. **Error conditions**:
   - Engine not installed
   - Invalid engine type specified
   - File system errors (no write permission)
4. **Integration points**:
   - CLI argument parsing
   - Engine factory creation
   - File output operations

### Test Coverage Goals

- Minimum 90% code coverage
- All error paths tested
- All public API methods tested
- Both engines tested (when available)

### Testing Dependencies

```
pytest>=7.0.0
hypothesis>=6.0.0
pytest-cov>=4.0.0
PyPDF2>=3.0.0  # For PDF content verification
```

## Implementation Notes

### ReportLab HTML Parsing

ReportLab doesn't have built-in HTML parsing, so we need to implement a converter from HTML (generated by markdown library) to ReportLab flowables. Key considerations:

1. Use `html.parser` from Python standard library
2. Map HTML tags to ReportLab styles:
   - `<h1>` → Heading1 style
   - `<p>` → BodyText style
   - `<code>` → Code style with monospace font
   - `<ul>`, `<ol>` → ListFlowable
3. Handle nested elements recursively

### TOC Implementation Differences

- **ReportLab**: Uses `TableOfContents` flowable with `addEntry()` calls
- **WeasyPrint**: Uses CSS `content: target-counter()` for page numbers

Both approaches should produce functionally equivalent TOCs.

### Performance Considerations

- ReportLab is generally faster for simple documents
- WeasyPrint is slower but handles complex layouts better
- For large documents (>100 pages), consider streaming/chunking

### Dependency Installation

Update `requirements.txt` to clearly separate required and optional dependencies:

```
# Core dependencies (required)
markdown>=3.5.0

# PDF engines (at least one required)
reportlab>=4.0.0  # Recommended: pure Python, no system deps

# Optional PDF engines
# weasyprint>=60.0  # Uncomment for advanced PDF features (requires system libs)
```
