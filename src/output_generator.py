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
    
    def __init__(self, output_dir: Path):
        """
        Initialize with output directory.
        
        Args:
            output_dir: Base directory for output files (e.g., "Handbook")
        """
        self.output_dir = Path(output_dir)
    
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
    
    def ensure_output_structure(self, language: str, template_type: str) -> Path:
        """
        Ensure output directory structure exists and return the target directory.
        
        Creates directory structure mirroring template organization:
        output_dir/language/template_type/
        
        Args:
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'backup', 'bcm')
            
        Returns:
            Path to the target output directory
        """
        target_dir = self.output_dir / language / template_type
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
            template_type: Template category (e.g., 'backup', 'bcm')
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
        
        # Ensure output directory exists
        try:
            output_dir = self.ensure_output_structure(language, template_type)
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
            template_type: Template category (e.g., 'backup', 'bcm')
            filename: Optional custom filename (default: {template_type}_handbook.pdf)
            
        Returns:
            OutputResult with path to generated file and any warnings/errors
        """
        result = OutputResult()
        
        # Ensure output directory exists
        try:
            output_dir = self.ensure_output_structure(language, template_type)
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
