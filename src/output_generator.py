"""
Output Generator for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import re


@dataclass
class OutputResult:
    """
    Result of output generation.
    
    Attributes:
        markdown_path: Path to generated markdown file (if generated)
        pdf_path: Path to generated PDF file (if generated)
        warnings: List of warning messages
        errors: List of error messages
    """
    markdown_path: Optional[Path] = None
    pdf_path: Optional[Path] = None
    warnings: list[str] = None
    errors: list[str] = None
    
    def __post_init__(self):
        if self.warnings is None:
            self.warnings = []
        if self.errors is None:
            self.errors = []


class OutputGenerator:
    """
    Generates output files (Markdown and PDF) from processed templates.
    """
    
    def __init__(self, output_dir: Path, test_mode: bool = False):
        """
        Initialize with output directory and test mode.
        
        Args:
            output_dir: Base directory for output files (e.g., "test-output")
            test_mode: Whether test mode is enabled (required for output generation)
        """
        self.output_dir = Path(output_dir)
        self.test_mode = test_mode
    
    def assemble_markdown(self, processed_contents: list[str]) -> str:
        """
        Assemble multiple processed template contents into a single markdown document.
        
        Args:
            processed_contents: List of processed template contents in order
            
        Returns:
            Assembled markdown content as a single string
        """
        if not processed_contents:
            return ""
        
        # Join templates with double newline separator for clear section breaks
        assembled = "\n\n".join(processed_contents)
        
        return assembled
    
    def validate_markdown(self, content: str) -> list[str]:
        """
        Validate markdown content for common issues.
        
        Args:
            content: Markdown content to validate
            
        Returns:
            List of validation warnings (empty if valid)
        """
        warnings = []
        
        if not content or not content.strip():
            warnings.append("Markdown content is empty")
            return warnings
        
        # Check for basic markdown validity
        lines = content.split('\n')
        
        # Check for unclosed code blocks
        code_block_count = 0
        for line in lines:
            if line.strip().startswith('```'):
                code_block_count += 1
        
        if code_block_count % 2 != 0:
            warnings.append("Unclosed code block detected in markdown")
        
        # Check for malformed headers (multiple # without space)
        for i, line in enumerate(lines, start=1):
            if re.match(r'^#{1,6}[^#\s]', line):
                warnings.append(f"Line {i}: Malformed header - missing space after #")
        
        return warnings
    
    def ensure_output_structure(self, language: str, output_type: str, handbook_type: str = None) -> Path:
        """
        Ensure output directory structure exists and return the target directory.
        
        Creates directory structure:
        output_dir/language/handbook_type/output_type/ (if handbook_type provided)
        output_dir/language/output_type/ (if handbook_type not provided - backward compatible)
        
        Args:
            language: Language code (e.g., 'de', 'en')
            output_type: Output type ('markdown', 'pdf', or 'html')
            handbook_type: Optional handbook type (e.g., 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            
        Returns:
            Path to the target output directory
            
        Raises:
            RuntimeError: If test mode is not enabled
        """
        if not self.test_mode:
            raise RuntimeError(
                "Output generation requires --test flag. "
                "Use --test to enable test mode output."
            )
        
        if handbook_type:
            target_dir = self.output_dir / language / handbook_type / output_type
        else:
            target_dir = self.output_dir / language / output_type
        
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir
    
    def generate_markdown(
        self,
        processed_contents: list[str],
        language: str,
        template_type: str,
        filename: Optional[str] = None
    ) -> OutputResult:
        """
        Generate markdown output file from processed templates.
        
        Args:
            processed_contents: List of processed template contents
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'backup', 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            filename: Optional custom filename (default: {template_type}_handbook.md)
            
        Returns:
            OutputResult with path to generated file and any warnings/errors
        """
        result = OutputResult()
        
        # Assemble markdown content
        markdown_content = self.assemble_markdown(processed_contents)
        
        # Validate markdown
        validation_warnings = self.validate_markdown(markdown_content)
        result.warnings.extend(validation_warnings)
        
        # Ensure output directory exists (uses 'markdown' as output_type, includes handbook_type)
        try:
            output_dir = self.ensure_output_structure(language, 'markdown', template_type)
        except RuntimeError as e:
            result.errors.append(str(e))
            return result
        except Exception as e:
            result.errors.append(f"Failed to create output directory: {str(e)}")
            return result
        
        # Determine output filename
        if filename is None:
            filename = f"{template_type}_handbook.md"
        
        output_path = output_dir / filename
        
        # Check if file exists and warn
        if output_path.exists():
            result.warnings.append(
                f"Output file already exists and will be overwritten: {output_path}"
            )
        
        # Write markdown file
        try:
            output_path.write_text(markdown_content, encoding='utf-8')
            result.markdown_path = output_path
        except Exception as e:
            result.errors.append(f"Failed to write markdown file: {str(e)}")
        
        return result
    
    def generate_separate_markdown_files(
        self,
        templates_data: list[tuple[str, str]],
        language: str,
        template_type: str
    ) -> OutputResult:
        """
        Generate separate markdown files for each template.
        
        Args:
            templates_data: List of (template_name, content) tuples
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'backup', 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            
        Returns:
            OutputResult with paths to generated files and any warnings/errors
        """
        result = OutputResult()
        
        # Ensure output directory exists (uses 'markdown' as output_type, includes handbook_type)
        try:
            output_dir = self.ensure_output_structure(language, 'markdown', template_type)
        except RuntimeError as e:
            result.errors.append(str(e))
            return result
        except Exception as e:
            result.errors.append(f"Failed to create output directory: {str(e)}")
            return result
        
        # Generate separate file for each template
        generated_files = []
        for template_name, content in templates_data:
            # Extract template number and name from filename
            # Expected format: 0010_Template_Name.md
            filename_base = Path(template_name).stem  # Remove .md extension
            
            # Create output filename using the same pattern
            output_filename = f"{filename_base}.md"
            output_path = output_dir / output_filename
            
            # Check if file exists and warn
            if output_path.exists():
                result.warnings.append(
                    f"Output file already exists and will be overwritten: {output_path}"
                )
            
            # Write markdown file
            try:
                output_path.write_text(content, encoding='utf-8')
                generated_files.append(output_path)
            except Exception as e:
                result.errors.append(
                    f"Failed to write markdown file {output_filename}: {str(e)}"
                )
        
        # Store first file path in markdown_path for compatibility
        if generated_files:
            result.markdown_path = generated_files[0]
            result.warnings.insert(
                0,
                f"Generated {len(generated_files)} separate markdown files in {output_dir}"
            )
        
        return result
    
    def generate_markdown_toc(
        self,
        templates_info: list[tuple[str, str, str]],
        language: str,
        template_type: str
    ) -> OutputResult:
        """
        Generate table of contents markdown file for separate markdown files.
        
        Args:
            templates_info: List of (template_number, template_title, filename) tuples
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'backup', 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            
        Returns:
            OutputResult with path to generated TOC file and any warnings/errors
        """
        result = OutputResult()
        
        # Ensure output directory exists (uses 'markdown' as output_type, includes handbook_type)
        try:
            output_dir = self.ensure_output_structure(language, 'markdown', template_type)
        except RuntimeError as e:
            result.errors.append(str(e))
            return result
        except Exception as e:
            result.errors.append(f"Failed to create output directory: {str(e)}")
            return result
        
        # Build TOC content
        toc_lines = [
            f"# Table of Contents - {template_type.upper()} Handbook",
            "",
            f"Language: {language}",
            "",
            "## Templates",
            ""
        ]
        
        for template_number, template_title, filename in templates_info:
            # Create markdown link: - [0010 - Title](0010_Title.md)
            link_text = f"{template_number} - {template_title}"
            toc_lines.append(f"- [{link_text}]({filename})")
        
        toc_content = "\n".join(toc_lines)
        
        # Write TOC file
        toc_path = output_dir / "TOC.md"
        
        # Check if file exists and warn
        if toc_path.exists():
            result.warnings.append(
                f"TOC file already exists and will be overwritten: {toc_path}"
            )
        
        try:
            toc_path.write_text(toc_content, encoding='utf-8')
            result.markdown_path = toc_path
        except Exception as e:
            result.errors.append(f"Failed to write TOC file: {str(e)}")
        
        return result
    
    def generate_pdf(
        self,
        markdown_content: str,
        language: str,
        template_type: str,
        filename: Optional[str] = None
    ) -> OutputResult:
        """
        Generate PDF output file from markdown content.
        
        Args:
            markdown_content: Markdown content to convert to PDF
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'backup', 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            filename: Optional custom filename (default: {template_type}_handbook.pdf)
            
        Returns:
            OutputResult with path to generated file and any warnings/errors
        """
        result = OutputResult()
        
        # Ensure output directory exists (uses 'pdf' as output_type, includes handbook_type)
        try:
            output_dir = self.ensure_output_structure(language, 'pdf', template_type)
        except RuntimeError as e:
            result.errors.append(str(e))
            return result
        except Exception as e:
            result.errors.append(f"Failed to create output directory: {str(e)}")
            return result
        
        # Determine output filename
        if filename is None:
            filename = f"{template_type}_handbook.pdf"
        
        output_path = output_dir / filename
        
        # Check if file exists and warn
        if output_path.exists():
            result.warnings.append(
                f"Output file already exists and will be overwritten: {output_path}"
            )
        
        # Try to import PDF generation library
        try:
            import markdown
            from weasyprint import HTML, CSS
            from weasyprint.text.fonts import FontConfiguration
        except ImportError as e:
            result.errors.append(
                f"PDF generation dependencies not available: {str(e)}. "
                f"Install with: pip install markdown weasyprint"
            )
            return result
        
        # Convert markdown to HTML
        try:
            html_content = markdown.markdown(
                markdown_content,
                extensions=['extra', 'codehilite', 'toc']
            )
            
            # Wrap in basic HTML structure with styling
            full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{
            font-family: 'DejaVu Sans', Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 24px;
            margin-bottom: 16px;
        }}
        h1 {{
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 10px;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'DejaVu Sans Mono', monospace;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 16px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        @page {{
            margin: 2.5cm;
            @bottom-right {{
                content: counter(page);
            }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""
        except Exception as e:
            result.errors.append(f"Failed to convert markdown to HTML: {str(e)}")
            return result
        
        # Generate PDF from HTML
        try:
            font_config = FontConfiguration()
            HTML(string=full_html).write_pdf(
                output_path,
                font_config=font_config
            )
            result.pdf_path = output_path
        except Exception as e:
            result.errors.append(
                f"Failed to generate PDF: {str(e)}. "
                f"Ensure weasyprint dependencies are installed correctly."
            )
        
        return result
    
    def generate_pdf_with_toc(
        self,
        templates_data: list[tuple[str, str, str]],
        language: str,
        template_type: str,
        filename: Optional[str] = None
    ) -> OutputResult:
        """
        Generate PDF output file with table of contents from template data.
        
        Args:
            templates_data: List of (template_number, template_title, content) tuples
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'backup', 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            filename: Optional custom filename (default: {template_type}_handbook.pdf)
            
        Returns:
            OutputResult with path to generated file and any warnings/errors
        """
        result = OutputResult()
        
        # Ensure output directory exists (uses 'pdf' as output_type, includes handbook_type)
        try:
            output_dir = self.ensure_output_structure(language, 'pdf', template_type)
        except RuntimeError as e:
            result.errors.append(str(e))
            return result
        except Exception as e:
            result.errors.append(f"Failed to create output directory: {str(e)}")
            return result
        
        # Determine output filename
        if filename is None:
            filename = f"{template_type}_handbook.pdf"
        
        output_path = output_dir / filename
        
        # Check if file exists and warn
        if output_path.exists():
            result.warnings.append(
                f"Output file already exists and will be overwritten: {output_path}"
            )
        
        # Try to import PDF generation library
        try:
            import markdown
            from weasyprint import HTML
            from weasyprint.text.fonts import FontConfiguration
        except ImportError as e:
            result.errors.append(
                f"PDF generation dependencies not available: {str(e)}. "
                f"Install with: pip install markdown weasyprint"
            )
            return result
        
        # Generate TOC HTML
        toc_html = self._generate_toc_html(templates_data, template_type)
        
        # Convert each template's markdown content to HTML and add page breaks
        templates_html = []
        for template_number, template_title, content in templates_data:
            try:
                # Convert markdown to HTML
                html_content = markdown.markdown(
                    content,
                    extensions=['extra', 'codehilite', 'toc']
                )
                
                # Add anchor ID for linking from TOC
                section_html = f'<div id="section-{template_number}">\n{html_content}\n</div>'
                templates_html.append(section_html)
            except Exception as e:
                result.errors.append(
                    f"Failed to convert template {template_number} to HTML: {str(e)}"
                )
                return result
        
        # Add page breaks between templates
        templates_with_breaks = self._add_page_breaks(templates_html)
        
        # Combine TOC and templates
        full_body_html = toc_html + "\n" + templates_with_breaks
        
        # Wrap in complete HTML structure with styling
        full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{
            font-family: 'DejaVu Sans', Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 24px;
            margin-bottom: 16px;
        }}
        h1 {{
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 10px;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'DejaVu Sans Mono', monospace;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 16px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        .toc {{
            margin-bottom: 40px;
        }}
        .toc h1 {{
            font-size: 2em;
            margin-bottom: 20px;
        }}
        .toc ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        .toc li {{
            margin: 8px 0;
            padding: 8px;
            border-bottom: 1px solid #eee;
        }}
        .toc a {{
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
        }}
        .toc a:hover {{
            color: #3498db;
        }}
        .page-break {{
            page-break-after: always;
        }}
        @page {{
            margin: 2.5cm;
            @bottom-right {{
                content: counter(page);
            }}
        }}
    </style>
</head>
<body>
{full_body_html}
</body>
</html>
"""
        
        # Generate PDF from HTML
        try:
            font_config = FontConfiguration()
            HTML(string=full_html).write_pdf(
                output_path,
                font_config=font_config
            )
            result.pdf_path = output_path
        except Exception as e:
            result.errors.append(
                f"Failed to generate PDF with TOC: {str(e)}. "
                f"Ensure weasyprint dependencies are installed correctly."
            )
        
        return result
    
    def _add_page_breaks(self, templates_html: list[str]) -> str:
        """
        Add page breaks between template sections.
        
        Args:
            templates_html: List of HTML content for each template
            
        Returns:
            Combined HTML with page breaks inserted
        """
        if not templates_html:
            return ""
        
        # Join templates with page break divs
        sections_with_breaks = []
        for i, template_html in enumerate(templates_html):
            sections_with_breaks.append(template_html)
            # Add page break after each template except the last one
            if i < len(templates_html) - 1:
                sections_with_breaks.append('<div class="page-break"></div>')
        
        return "\n".join(sections_with_breaks)
    
    def _generate_toc_html(
        self,
        templates_data: list[tuple[str, str, str]],
        template_type: str
    ) -> str:
        """
        Generate HTML for table of contents.
        
        Args:
            templates_data: List of (template_number, template_title, content) tuples
            template_type: Template category (e.g., 'backup', 'bcm')
            
        Returns:
            HTML string for table of contents
        """
        toc_lines = [
            '<div class="toc">',
            '<h1>Table of Contents</h1>',
            '<ul>'
        ]
        
        for template_number, template_title, _ in templates_data:
            # Create anchor link to template section
            link = f'<li><a href="#section-{template_number}">{template_number} - {template_title}</a></li>'
            toc_lines.append(link)
        
        toc_lines.append('</ul>')
        toc_lines.append('</div>')
        toc_lines.append('<div class="page-break"></div>')  # Page break after TOC
        
        return "\n".join(toc_lines)
