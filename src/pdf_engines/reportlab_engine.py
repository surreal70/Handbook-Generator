"""ReportLab PDF engine implementation (pure Python, no system dependencies).

This module implements the PDFEngine interface using ReportLab, a pure Python
PDF generation library. ReportLab requires no system dependencies, making it
the most portable option for PDF generation.

Key Features:
- Pure Python implementation (no system libraries required)
- Supports markdown to PDF conversion
- Table of contents generation with clickable links
- Code block rendering with monospace fonts
- Text formatting (bold, italic, headings)

Example:
    >>> from pdf_engines import ReportLabEngine
    >>> engine = ReportLabEngine()
    >>> if engine.is_available():
    ...     engine.generate_pdf("# Title\\n\\nContent", "output.pdf", include_toc=True)
"""

from typing import Optional, List
from html.parser import HTMLParser
import io

from . import PDFEngine, PDFGenerationError, MarkdownConversionError


class ReportLabEngine(PDFEngine):
    """PDF engine using ReportLab (pure Python, no system dependencies).
    
    This engine converts markdown content to PDF using ReportLab, a pure Python
    library that requires no system dependencies. It's the recommended engine
    for maximum portability across platforms.
    
    The engine performs the following steps:
    1. Convert markdown to HTML using the markdown library
    2. Parse HTML and convert to ReportLab flowable elements
    3. Build PDF document with proper styling and formatting
    4. Optionally generate table of contents with clickable links
    
    Attributes:
        None (stateless engine)
    
    Example:
        >>> engine = ReportLabEngine()
        >>> markdown_text = "# Hello\\n\\nThis is **bold** text."
        >>> engine.generate_pdf(markdown_text, "output.pdf")
    """
    
    def generate_pdf(
        self,
        markdown_content: str,
        output_path: str,
        include_toc: bool = False,
        metadata: Optional[dict] = None
    ) -> None:
        """
        Generate PDF using ReportLab.
        
        Args:
            markdown_content: The markdown text to convert
            output_path: Path where the PDF should be saved
            include_toc: Whether to include a table of contents
            metadata: Optional metadata (title, author, etc.)
        
        Raises:
            PDFGenerationError: If PDF generation fails
            MarkdownConversionError: If markdown conversion fails
        """
        try:
            import markdown
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
            from reportlab.platypus.tableofcontents import TableOfContents
            from reportlab.lib.enums import TA_LEFT
        except ImportError as e:
            missing_package = str(e).split("'")[1] if "'" in str(e) else "unknown"
            error_msg = (
                f"ReportLab PDF Engine Error: Required dependency '{missing_package}' is not available.\n\n"
                f"Installation Instructions:\n"
                f"{self.get_installation_instructions()}\n\n"
                f"Troubleshooting:\n"
                f"  1. Ensure you have activated your virtual environment\n"
                f"  2. Verify installation with: pip list | grep -E '(reportlab|markdown)'\n"
                f"  3. Try reinstalling: pip install --upgrade reportlab markdown\n\n"
                f"Original error: {e}"
            )
            raise PDFGenerationError(error_msg)
        
        try:
            # Convert markdown to HTML using the markdown library
            # Extensions used:
            # - 'extra': Adds tables, footnotes, and other features
            # - 'codehilite': Syntax highlighting for code blocks
            # - 'toc': Table of contents generation
            html_content = markdown.markdown(
                markdown_content,
                extensions=['extra', 'codehilite', 'toc']
            )
        except Exception as e:
            snippet = markdown_content[:200] if len(markdown_content) > 200 else markdown_content
            error_msg = (
                f"Markdown Conversion Error: Failed to convert markdown to HTML.\n\n"
                f"Problematic content (first 200 chars):\n"
                f"{snippet}\n\n"
                f"Troubleshooting:\n"
                f"  1. Check for malformed markdown syntax (unclosed code blocks, invalid headers)\n"
                f"  2. Verify special characters are properly escaped\n"
                f"  3. Ensure markdown extensions are compatible with your content\n"
                f"  4. Try validating your markdown with an online validator\n\n"
                f"Original error: {e}"
            )
            raise MarkdownConversionError(error_msg, snippet)
        
        try:
            # Create PDF document with A4 page size and standard margins
            # Margins: 72 points = 1 inch (standard for professional documents)
            doc = SimpleDocTemplate(
                output_path,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=18
            )
            
            # Build story (content elements)
            # The "story" is ReportLab's term for the list of flowable elements
            # that will be rendered in the PDF
            story = []
            styles = getSampleStyleSheet()
            
            # Add custom code style if it doesn't exist
            # This ensures code blocks are rendered with monospace font
            if 'Code' not in styles:
                code_style = ParagraphStyle(
                    'Code',
                    parent=styles['Normal'],
                    fontName='Courier',  # Monospace font for code
                    fontSize=9,
                    leftIndent=20,
                    rightIndent=20,
                    spaceBefore=6,
                    spaceAfter=6,
                    backColor='#f5f5f5'  # Light gray background
                )
                styles.add(code_style)
            
            # Create TOC object if needed (must be created before parsing content)
            toc = None
            if include_toc:
                # Create table of contents with custom styling
                toc = TableOfContents()
                # Define styles for different heading levels in TOC
                # Level 0 = h1, Level 1 = h2, Level 2 = h3
                # Each level has proper spacing to ensure line breaks between entries
                toc.levelStyles = [
                    ParagraphStyle(
                        name='TOCHeading1',
                        parent=styles['Normal'],
                        fontSize=14,
                        leftIndent=20,
                        spaceBefore=12,  # Space before each h1 entry
                        spaceAfter=6,    # Space after each h1 entry
                        leading=18       # Line height for proper spacing
                    ),
                    ParagraphStyle(
                        name='TOCHeading2',
                        parent=styles['Normal'],
                        fontSize=12,
                        leftIndent=40,  # Indent to show hierarchy
                        spaceBefore=6,  # Space before each h2 entry
                        spaceAfter=3,   # Space after each h2 entry
                        leading=16      # Line height for proper spacing
                    ),
                    ParagraphStyle(
                        name='TOCHeading3',
                        parent=styles['Normal'],
                        fontSize=10,
                        leftIndent=60,  # Further indent for h3
                        spaceBefore=3,  # Space before each h3 entry
                        spaceAfter=3,   # Space after each h3 entry
                        leading=14      # Line height for proper spacing
                    ),
                ]
                story.append(toc)
                story.append(PageBreak())  # TOC on separate page
            
            # Parse HTML and convert to ReportLab elements
            # Pass the toc object so parser can create proper bookmarks
            elements = self._html_to_reportlab(html_content, styles, toc)
            
            # If TOC is enabled, wrap elements to notify TOC during rendering
            if include_toc and toc:
                elements = self._wrap_elements_for_toc(elements, toc)
            
            story.extend(elements)
            
            # Build PDF - this triggers the actual PDF generation
            # Use multiBuild when TOC is enabled to support page number collection
            if include_toc and toc:
                # multiBuild is required for TOC with page numbers
                # First pass: collect TOC entries and page numbers
                # Second pass: render TOC with collected information
                doc.multiBuild(story)
            else:
                doc.build(story)
            
        except Exception as e:
            error_msg = (
                f"PDF Generation Error: Failed to generate PDF with ReportLab.\n\n"
                f"Output path: {output_path}\n\n"
                f"Troubleshooting:\n"
                f"  1. Verify the output directory exists and is writable\n"
                f"  2. Check available disk space\n"
                f"  3. Ensure the output path doesn't contain invalid characters\n"
                f"  4. Try a different output location\n"
                f"  5. Check if the file is open in another application\n\n"
                f"Technical details:\n"
                f"  Error type: {type(e).__name__}\n"
                f"  Error message: {str(e)}\n"
            )
            raise PDFGenerationError(error_msg)
    
    def is_available(self) -> bool:
        """
        Check if ReportLab is installed.
        
        Returns:
            True if ReportLab and markdown are available, False otherwise
        """
        try:
            import reportlab
            import markdown
            return True
        except ImportError:
            return False
    
    def get_installation_instructions(self) -> str:
        """
        Get ReportLab installation instructions.
        
        Returns:
            String with installation instructions
        """
        return (
            "ReportLab is not installed. Install it with:\n"
            "  pip install reportlab markdown"
        )
    
    def _wrap_elements_for_toc(self, elements: List, toc) -> List:
        """Wrap elements to notify TOC during rendering.
        
        This method processes the list of flowable elements and creates
        TOC notification flowables for headings.
        
        Args:
            elements: List of ReportLab flowable elements
            toc: TableOfContents object to notify
        
        Returns:
            List of elements with TOC notifications inserted
        """
        from reportlab.platypus import Paragraph
        
        wrapped_elements = []
        for element in elements:
            # Check if this element has a TOC entry
            if isinstance(element, Paragraph) and hasattr(element, '_tocEntry'):
                level, text, key = element._tocEntry
                # Create a TOC notification flowable
                toc_notifier = TOCNotifier(toc, level, text, key)
                wrapped_elements.append(toc_notifier)
            wrapped_elements.append(element)
        
        return wrapped_elements
    
    def _html_to_reportlab(self, html: str, styles, toc=None) -> List:
        """Convert HTML to ReportLab flowable elements.
        
        This method parses HTML content (generated from markdown) and converts it
        into ReportLab flowable elements (Paragraph, Spacer, Preformatted, etc.)
        that can be rendered in a PDF document.
        
        The conversion process:
        1. Create an HTMLToReportLabParser instance
        2. Feed HTML content to the parser
        3. Parser generates ReportLab flowables during parsing
        4. Return list of flowables ready for PDF rendering
        
        Args:
            html: HTML content to convert (typically from markdown.markdown())
            styles: ReportLab StyleSheet containing paragraph styles
            toc: Optional TableOfContents object to notify of heading entries
        
        Returns:
            List of ReportLab flowable elements ready for PDF rendering
        
        Note:
            The HTML parser handles common markdown elements:
            - Headings (h1-h4) with optional TOC bookmarks
            - Paragraphs with text formatting (bold, italic)
            - Code blocks (pre/code) with monospace font
            - Lists (ul/ol) with bullet points
        
        Example:
            >>> html = "<h1>Title</h1><p>Content</p>"
            >>> elements = engine._html_to_reportlab(html, styles)
            >>> # elements is now a list of Paragraph and Spacer objects
        """
        from reportlab.platypus import Paragraph, Spacer, Preformatted
        from reportlab.lib.units import inch
        
        parser = HTMLToReportLabParser(styles, toc)
        parser.feed(html)
        return parser.get_elements()


class HTMLToReportLabParser(HTMLParser):
    """
    Parser to convert HTML to ReportLab flowables.
    
    This parser extends Python's HTMLParser to convert HTML elements into
    ReportLab flowable objects. It maintains state during parsing to handle
    nested elements and formatting.
    
    Attributes:
        styles: ReportLab StyleSheet for paragraph formatting
        toc: Optional TableOfContents object to notify of heading entries
        elements: List of generated ReportLab flowable elements
        current_text: Buffer for accumulating text within an element
        current_style: Current paragraph style being applied
        in_code_block: Flag indicating if parser is inside a <pre> block
        code_content: Buffer for accumulating code block content
        heading_counter: Counter for generating unique heading bookmarks
    
    Example:
        >>> parser = HTMLToReportLabParser(styles, toc=toc_object)
        >>> parser.feed("<h1>Title</h1><p>Content</p>")
        >>> elements = parser.get_elements()
    """
    
    def __init__(self, styles, toc=None):
        super().__init__()
        self.styles = styles
        self.toc = toc
        self.elements = []
        self.current_text = []
        self.current_style = None
        self.in_code_block = False
        self.code_content = []
        self.heading_counter = 0
        
    def handle_starttag(self, tag: str, attrs: list) -> None:
        """Handle opening HTML tags.
        
        This method is called by HTMLParser when an opening tag is encountered.
        It sets the appropriate ReportLab style and handles special formatting
        for different HTML elements.
        
        Tag Handling Strategy:
        - Block elements (h1-h4, p): Set current_style for paragraph creation
        - Inline elements (strong, em, code): Add formatting markup to text buffer
        - Code blocks (pre): Set flag to preserve whitespace
        - Lists (ul, ol, li): Add bullet points and list formatting
        
        Args:
            tag: HTML tag name (e.g., 'h1', 'p', 'code')
            attrs: List of (name, value) tuples for tag attributes
        """
        from reportlab.platypus import Spacer
        from reportlab.lib.units import inch
        
        # Map HTML heading tags to ReportLab styles
        # Each heading increments the counter for TOC bookmark generation
        if tag == 'h1':
            self.current_style = 'Heading1'
            self.heading_counter += 1
        elif tag == 'h2':
            self.current_style = 'Heading2'
            self.heading_counter += 1
        elif tag == 'h3':
            self.current_style = 'Heading3'
            self.heading_counter += 1
        elif tag == 'h4':
            self.current_style = 'Heading4'
            self.heading_counter += 1
        elif tag == 'p':
            self.current_style = 'BodyText'
        
        # Handle inline code with monospace font
        # Uses ReportLab's XML-like markup for font changes
        elif tag == 'code':
            if not self.in_code_block:
                self.current_text.append('<font name="Courier">')
        
        # Handle code blocks (pre-formatted text)
        # Set flag to accumulate content in separate buffer
        elif tag == 'pre':
            self.in_code_block = True
            self.code_content = []
        
        # Handle text formatting with ReportLab markup
        elif tag == 'strong' or tag == 'b':
            self.current_text.append('<b>')
        elif tag == 'em' or tag == 'i':
            self.current_text.append('<i>')
        
        # Handle lists (basic support)
        elif tag == 'ul':
            pass  # Unordered list container
        elif tag == 'ol':
            pass  # Ordered list container
        elif tag == 'li':
            # Add bullet point for list items
            # TODO: Support numbered lists (ol) with proper numbering
            self.current_text.append('• ')
    
    def handle_endtag(self, tag: str) -> None:
        """Handle closing HTML tags.
        
        This method is called by HTMLParser when a closing tag is encountered.
        It creates ReportLab flowable elements from accumulated text and adds
        them to the elements list.
        
        Processing Strategy:
        - Block elements: Create Paragraph from accumulated text, add to elements
        - Code blocks: Create Preformatted element, preserving whitespace
        - Inline elements: Close formatting markup in text buffer
        
        Args:
            tag: HTML tag name (e.g., 'h1', 'p', 'code')
        """
        from reportlab.platypus import Paragraph, Spacer, Preformatted
        from reportlab.lib.units import inch
        
        # Handle block-level elements (headings and paragraphs)
        if tag in ['h1', 'h2', 'h3', 'h4', 'p']:
            if self.current_text:
                text = ''.join(self.current_text).strip()
                if text:
                    style = self.styles[self.current_style]
                    
                    # Add page break before h1 headings (new chapter)
                    # This ensures each major section starts on a new page
                    if tag == 'h1' and len(self.elements) > 0:
                        from reportlab.platypus import PageBreak
                        self.elements.append(PageBreak())
                    
                    # Create paragraph with TOC bookmark if needed
                    if self.toc and tag in ['h1', 'h2', 'h3']:
                        level = int(tag[1]) - 1  # h1=0, h2=1, h3=2
                        # Create a unique bookmark key for this heading
                        bookmark_key = f'heading_{self.heading_counter}'
                        
                        # Create paragraph with bookmark
                        # The bookmark format: <a name="key"/>text
                        para_text = f'<a name="{bookmark_key}"/>{text}'
                        para = Paragraph(para_text, style)
                        
                        # Register this heading with the TOC
                        # The TOC will be notified during the build process
                        # Store the TOC entry information on the paragraph
                        para._tocEntry = (level, text, bookmark_key)
                    else:
                        para = Paragraph(text, style)
                    
                    self.elements.append(para)
                    # Add spacing after each paragraph (0.2 inches)
                    self.elements.append(Spacer(1, 0.2 * inch))
                
                # Reset text buffer and style for next element
                self.current_text = []
                self.current_style = None
        
        # Handle inline code
        elif tag == 'code':
            if not self.in_code_block:
                self.current_text.append('</font>')
        
        # Handle code blocks
        # Use Preformatted to preserve whitespace and indentation
        elif tag == 'pre':
            if self.code_content:
                code_text = ''.join(self.code_content)
                # Use Preformatted for code blocks (preserves whitespace)
                code_para = Preformatted(
                    code_text,
                    self.styles['Code']
                )
                self.elements.append(code_para)
                self.elements.append(Spacer(1, 0.2 * inch))
            self.in_code_block = False
            self.code_content = []
        
        # Handle text formatting
        elif tag == 'strong' or tag == 'b':
            self.current_text.append('</b>')
        elif tag == 'em' or tag == 'i':
            self.current_text.append('</i>')
    
    def handle_data(self, data: str) -> None:
        """Handle text data within HTML elements.
        
        This method is called by HTMLParser for text content between tags.
        Text is accumulated in buffers (current_text or code_content) depending
        on the current parsing context.
        
        Buffer Strategy:
        - Inside code blocks: Accumulate in code_content to preserve formatting
        - Regular text: Accumulate in current_text for paragraph creation
        
        Args:
            data: Text content from HTML
        """
        if self.in_code_block:
            # Accumulate code block content separately to preserve formatting
            # This ensures whitespace and indentation are maintained
            self.code_content.append(data)
        else:
            # Accumulate regular text content
            self.current_text.append(data)
    
    def get_elements(self) -> List:
        """Get the list of ReportLab flowable elements.
        
        This method returns all flowable elements that were generated during
        HTML parsing. The elements are ready to be added to a ReportLab
        document's story for PDF generation.
        
        Returns:
            List of ReportLab flowable elements (Paragraph, Spacer, Preformatted, etc.)
            ready to be added to a PDF document story.
        
        Example:
            >>> parser = HTMLToReportLabParser(styles)
            >>> parser.feed("<h1>Title</h1>")
            >>> elements = parser.get_elements()
            >>> doc.build(elements)  # Add to PDF document
        """
        return self.elements


class TOCNotifier:
    """A zero-height flowable that notifies the TOC of an entry.
    
    This flowable is inserted before headings to register them with
    the Table of Contents, allowing page numbers to be captured.
    """
    
    def __init__(self, toc, level, text, key):
        self.toc = toc
        self.level = level
        self.text = text
        self.key = key
        self.width = 0
        self.height = 0
        self._fixedWidth = 0
        self._fixedHeight = 0
    
    def wrap(self, availWidth, availHeight):
        """Return zero size - this flowable takes no space."""
        return (0, 0)
    
    def drawOn(self, canvas, x, y, _sW=0):
        """Notify the TOC when this flowable is rendered."""
        # Get the current page number from the canvas
        page_num = canvas.getPageNumber()
        
        # Notify the TOC with the entry information
        self.toc.addEntry(self.level, self.text, page_num, self.key)
    
    def isIndexing(self):
        """Return False - this is not an indexing flowable."""
        return False
    
    def getKeepWithNext(self):
        """Return False - no keep with next behavior."""
        return False
    
    def getSpaceAfter(self):
        """Return 0 - no space after."""
        return 0
    
    def getSpaceBefore(self):
        """Return 0 - no space before."""
        return 0


__all__ = ['ReportLabEngine']
