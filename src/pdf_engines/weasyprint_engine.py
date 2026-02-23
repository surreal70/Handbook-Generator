"""WeasyPrint PDF engine implementation.

This module implements the PDFEngine interface using WeasyPrint, a Python
library for rendering HTML/CSS to PDF. WeasyPrint requires system libraries
(libpango) but offers advanced CSS styling and layout capabilities.

Key Features:
- Advanced CSS styling support (CSS 2.1 and some CSS 3)
- Professional typography and layout
- Complex page layouts with CSS Grid and Flexbox
- Automatic table of contents generation
- System dependencies required (libpango, cairo)

Example:
    >>> from pdf_engines import WeasyPrintEngine
    >>> engine = WeasyPrintEngine()
    >>> if engine.is_available():
    ...     engine.generate_pdf("# Title\\n\\nContent", "output.pdf")
    ... else:
    ...     print(engine.get_installation_instructions())
"""

import sys
import tempfile
from typing import Optional
import markdown

from . import PDFEngine, PDFGenerationError, PDFEngineNotAvailableError


class WeasyPrintEngine(PDFEngine):
    """PDF engine using WeasyPrint (requires system dependencies).
    
    This engine converts markdown content to PDF using WeasyPrint, which
    provides advanced CSS styling and layout capabilities. WeasyPrint requires
    system libraries (libpango, cairo) to be installed.
    
    The engine performs the following steps:
    1. Convert markdown to HTML using the markdown library
    2. Wrap HTML in a complete HTML5 document structure
    3. Apply CSS styling for professional appearance
    4. Use WeasyPrint to render HTML/CSS to PDF
    
    Advantages over ReportLab:
    - Advanced CSS support (Grid, Flexbox, etc.)
    - Better typography and layout control
    - Professional-quality output
    
    Disadvantages:
    - Requires system libraries (libpango, cairo)
    - Less portable than ReportLab
    - Slower for simple documents
    
    Attributes:
        None (stateless engine)
    
    Example:
        >>> engine = WeasyPrintEngine()
        >>> if engine.is_available():
        ...     markdown_text = "# Hello\\n\\nThis is **bold** text."
        ...     engine.generate_pdf(markdown_text, "output.pdf")
    """
    
    def generate_pdf(
        self,
        markdown_content: str,
        output_path: str,
        include_toc: bool = False,
        metadata: Optional[dict] = None
    ) -> None:
        """
        Generate PDF using WeasyPrint.
        
        Args:
            markdown_content: The markdown text to convert
            output_path: Path where the PDF should be saved
            include_toc: Whether to include a table of contents
            metadata: Optional metadata (title, author, etc.)
        
        Raises:
            PDFGenerationError: If PDF generation fails
        """
        try:
            from weasyprint import HTML, CSS
        except ImportError as e:
            error_msg = (
                f"WeasyPrint PDF Engine Error: WeasyPrint is not installed.\n\n"
                f"{self.get_installation_instructions()}\n\n"
                f"Alternative: For a pure Python solution without system dependencies,\n"
                f"consider using ReportLab instead:\n"
                f"  pip install reportlab markdown\n"
                f"  Use with: --pdf-engine reportlab\n\n"
                f"Original error: {e}"
            )
            raise PDFEngineNotAvailableError(
                error_msg,
                engine_name="WeasyPrint"
            ) from e
        
        try:
            # Convert markdown to HTML with extensions
            # Extensions are conditionally added based on features needed
            extensions = ['extra', 'codehilite']
            if include_toc:
                extensions.append('toc')  # Add TOC extension only when needed
            
            html_content = markdown.markdown(
                markdown_content,
                extensions=extensions
            )
            
            # Wrap in full HTML document
            # WeasyPrint requires a complete HTML5 document structure
            full_html = self._wrap_html(html_content, metadata, include_toc)
            
            # Get CSS styling
            # CSS defines the visual appearance of the PDF
            css_content = self._get_default_css()
            
            # Generate PDF using WeasyPrint
            # HTML string is converted to PDF with CSS styling applied
            HTML(string=full_html).write_pdf(
                output_path,
                stylesheets=[CSS(string=css_content)]
            )
            
        except Exception as e:
            error_type = type(e).__name__
            
            # Provide specific guidance based on error type
            # This helps users quickly identify and resolve common issues
            if "OSError" in error_type or "cairo" in str(e).lower() or "pango" in str(e).lower():
                # System dependency errors (most common with WeasyPrint)
                troubleshooting = (
                    "This error typically indicates missing system dependencies.\n"
                    "WeasyPrint requires libpango and related libraries.\n\n"
                    f"{self.get_installation_instructions()}\n\n"
                    "After installing system dependencies, you may need to restart your terminal."
                )
            elif "Permission" in str(e) or "denied" in str(e).lower():
                # File system permission errors
                troubleshooting = (
                    "Permission Error: Cannot write to the output location.\n\n"
                    "Troubleshooting:\n"
                    "  1. Check if you have write permissions for the output directory\n"
                    "  2. Verify the output path is not read-only\n"
                    "  3. Try a different output location\n"
                    "  4. On Unix systems, check file permissions with: ls -la"
                )
            elif "No space" in str(e) or "Disk" in str(e):
                # Disk space errors
                troubleshooting = (
                    "Disk Space Error: Insufficient disk space.\n\n"
                    "Troubleshooting:\n"
                    "  1. Check available disk space\n"
                    "  2. Clean up temporary files\n"
                    "  3. Try a different output location with more space"
                )
            else:
                # Generic error with general troubleshooting steps
                troubleshooting = (
                    "General PDF Generation Error.\n\n"
                    "Troubleshooting:\n"
                    "  1. Verify your markdown content is valid\n"
                    "  2. Check the output path is writable\n"
                    "  3. Ensure WeasyPrint is properly installed\n"
                    "  4. Try using ReportLab engine instead: --pdf-engine reportlab"
                )
            
            error_msg = (
                f"WeasyPrint PDF Generation Error: Failed to generate PDF.\n\n"
                f"Output path: {output_path}\n\n"
                f"{troubleshooting}\n\n"
                f"Technical details:\n"
                f"  Error type: {error_type}\n"
                f"  Error message: {str(e)}\n"
            )
            raise PDFGenerationError(error_msg) from e
    
    def is_available(self) -> bool:
        """Check if WeasyPrint is installed and functional.
        
        This method performs a comprehensive availability check:
        1. Attempts to import the weasyprint module
        2. Creates a test PDF to verify system dependencies
        3. Returns True only if both checks pass
        
        The test PDF generation verifies that system libraries (libpango, cairo)
        are properly installed and accessible. This is more thorough than just
        checking for the Python package.
        
        Returns:
            True if WeasyPrint can be used, False otherwise
        
        Note:
            This method creates a temporary PDF file to verify functionality.
            The file is automatically deleted after the check.
        
        Example:
            >>> engine = WeasyPrintEngine()
            >>> if engine.is_available():
            ...     print("WeasyPrint is ready to use")
            ... else:
            ...     print("WeasyPrint is not available")
            ...     print(engine.get_installation_instructions())
        """
        try:
            from weasyprint import HTML
            # Try to create a simple document to verify system deps
            # This ensures libpango and cairo are properly installed
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=True) as tmp:
                HTML(string="<p>test</p>").write_pdf(tmp.name)
            return True
        except (ImportError, OSError, Exception):
            # ImportError: weasyprint not installed
            # OSError: system dependencies missing (libpango, cairo)
            # Other exceptions: configuration or permission issues
            return False
    
    def get_installation_instructions(self) -> str:
        """Get WeasyPrint installation instructions.
        
        This method returns platform-specific installation instructions for
        WeasyPrint and its system dependencies. The instructions vary based
        on the detected operating system.
        
        Platform Detection:
        - Linux: Provides instructions for Ubuntu/Debian and Fedora/RHEL
        - macOS: Provides Homebrew installation instructions
        - Windows: Provides GTK3 runtime download link
        - Other: Provides link to official documentation
        
        Returns:
            Multi-line string with platform-specific installation instructions
        
        Example:
            >>> engine = WeasyPrintEngine()
            >>> print(engine.get_installation_instructions())
            WeasyPrint is not installed or missing system dependencies.
            
            Install WeasyPrint with:
              pip install weasyprint
            ...
        """
        platform = sys.platform
        
        instructions = [
            "WeasyPrint is not installed or missing system dependencies.",
            "",
            "Install WeasyPrint with:",
            "  pip install weasyprint",
            "",
            "System dependencies required:",
        ]
        
        # Platform-specific system dependency instructions
        if platform.startswith('linux'):
            instructions.extend([
                "  Ubuntu/Debian: sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0",
                "  Fedora/RHEL: sudo dnf install pango",
            ])
        elif platform == 'darwin':
            instructions.append("  macOS: brew install pango")
        elif platform == 'win32':
            instructions.extend([
                "  Windows: Download GTK3 runtime from:",
                "  https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases",
            ])
        else:
            instructions.append(f"  {platform}: See https://doc.courtbouillon.org/weasyprint/stable/first_steps.html")
        
        # Add general documentation link for all platforms
        instructions.extend([
            "",
            "For more information, see:",
            "  https://doc.courtbouillon.org/weasyprint/stable/first_steps.html"
        ])
        
        return "\n".join(instructions)
    
    def _get_default_css(self) -> str:
        """
        Get default CSS styling for PDF.
        
        This method returns a comprehensive CSS stylesheet that defines the
        visual appearance of the PDF document. The CSS includes:
        - Page layout and margins
        - Typography (fonts, sizes, line heights)
        - Heading styles with borders
        - Code block formatting with monospace fonts
        - List and table styling
        - Table of contents styling
        
        Returns:
            CSS string with default styling for professional PDF output
        
        Note:
            WeasyPrint supports most CSS 2.1 and some CSS 3 features.
            The @page rule is used to define page size and margins.
        """
        return """
            @page {
                size: A4;
                margin: 2cm;
            }
            
            body {
                font-family: 'DejaVu Sans', 'Arial', sans-serif;
                font-size: 11pt;
                line-height: 1.5;
                color: #333;
            }
            
            h1, h2, h3, h4, h5, h6 {
                color: #222;
                margin-top: 1em;
                margin-bottom: 0.5em;
                font-weight: bold;
            }
            
            h1 {
                font-size: 24pt;
                border-bottom: 2px solid #333;
                padding-bottom: 0.3em;
            }
            
            h2 {
                font-size: 20pt;
                border-bottom: 1px solid #666;
                padding-bottom: 0.2em;
            }
            
            h3 {
                font-size: 16pt;
            }
            
            h4 {
                font-size: 14pt;
            }
            
            p {
                margin: 0.5em 0;
            }
            
            code {
                font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
                background-color: #f5f5f5;
                padding: 2px 4px;
                border-radius: 3px;
                font-size: 10pt;
            }
            
            pre {
                background-color: #f5f5f5;
                padding: 1em;
                border-radius: 5px;
                overflow-x: auto;
                margin: 1em 0;
            }
            
            pre code {
                background-color: transparent;
                padding: 0;
            }
            
            ul, ol {
                margin: 0.5em 0;
                padding-left: 2em;
            }
            
            li {
                margin: 0.3em 0;
            }
            
            blockquote {
                border-left: 4px solid #ddd;
                padding-left: 1em;
                margin: 1em 0;
                color: #666;
            }
            
            table {
                border-collapse: collapse;
                width: 100%;
                margin: 1em 0;
            }
            
            th, td {
                border: 1px solid #ddd;
                padding: 0.5em;
                text-align: left;
            }
            
            th {
                background-color: #f5f5f5;
                font-weight: bold;
            }
            
            a {
                color: #0066cc;
                text-decoration: none;
            }
            
            a:hover {
                text-decoration: underline;
            }
            
            /* Table of Contents styling */
            .toc {
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                padding: 1em;
                margin: 1em 0 2em 0;
            }
            
            .toc ul {
                list-style-type: none;
                padding-left: 1em;
            }
            
            .toc a {
                color: #333;
            }
        """
    
    def _wrap_html(
        self,
        html_content: str,
        metadata: Optional[dict] = None,
        include_toc: bool = False
    ) -> str:
        """
        Wrap HTML content in a complete HTML document.
        
        This method takes HTML body content and wraps it in a complete HTML5
        document structure with proper DOCTYPE, head, and body tags. It also
        adds metadata and enhances the TOC styling if present.
        
        Args:
            html_content: The HTML body content (from markdown conversion)
            metadata: Optional metadata for the document (title, author, etc.)
            include_toc: Whether TOC is included (for styling enhancement)
        
        Returns:
            Complete HTML document string ready for PDF conversion
        
        Note:
            The TOC div is enhanced with a heading if detected in the content.
            This provides better visual separation in the final PDF.
        """
        title = ""
        if metadata and 'title' in metadata:
            title = metadata['title']
        
        # Wrap TOC in a styled div if present
        # The markdown extension generates <div class="toc">...</div>
        # We enhance it with a heading for better visual separation
        if include_toc and '[TOC]' in html_content:
            html_content = html_content.replace(
                '<div class="toc">',
                '<div class="toc"><h2>Table of Contents</h2>'
            )
        
        # Build complete HTML5 document structure
        # WeasyPrint requires proper DOCTYPE and meta tags for correct rendering
        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
</head>
<body>
{html_content}
</body>
</html>"""

