#!/usr/bin/env python3
"""
Generate PDF versions of example handbooks from Markdown files.

This script converts the generated Markdown handbooks to PDF format using
markdown and pdfkit libraries (which uses wkhtmltopdf).
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def check_dependencies() -> bool:
    """Check if required dependencies are installed."""
    try:
        import markdown
        import pdfkit
        
        # Check if wkhtmltopdf is installed
        try:
            subprocess.run(['wkhtmltopdf', '--version'], 
                         capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.error("wkhtmltopdf is not installed")
            logger.error("Please install wkhtmltopdf:")
            logger.error("  Ubuntu/Debian: sudo apt-get install wkhtmltopdf")
            logger.error("  macOS: brew install wkhtmltopdf")
            logger.error("  Or download from: https://wkhtmltopdf.org/downloads.html")
            return False
        
        return True
    except ImportError as e:
        logger.error(f"Missing required dependency: {e}")
        logger.error("Please install required packages:")
        logger.error("  pip install markdown pdfkit")
        return False


def find_handbooks(base_dir: str = "Handbook") -> List[Tuple[Path, Path]]:
    """
    Find all handbook markdown files.
    
    Returns:
        List of tuples (input_path, output_path)
    """
    handbooks = []
    base_path = Path(base_dir)
    
    if not base_path.exists():
        logger.error(f"Handbook directory not found: {base_dir}")
        return handbooks
    
    # Find all *_handbook.md files
    for md_file in base_path.rglob("*_handbook.md"):
        # Create output path with same structure but in PDF_Output directory
        relative_path = md_file.relative_to(base_path)
        output_path = Path("PDF_Output") / relative_path.parent / f"{md_file.stem}.pdf"
        handbooks.append((md_file, output_path))
    
    return handbooks


def convert_markdown_to_pdf(input_path: Path, output_path: Path) -> bool:
    """
    Convert a Markdown file to PDF.
    
    Args:
        input_path: Path to input Markdown file
        output_path: Path to output PDF file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        import markdown
        import pdfkit
        
        logger.info(f"Converting: {input_path}")
        
        # Read Markdown content
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert Markdown to HTML
        md = markdown.Markdown(extensions=[
            'extra',
            'codehilite',
            'toc',
            'tables',
            'fenced_code'
        ])
        html_content = md.convert(md_content)
        
        # Create HTML document with styling
        html_doc = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                @page {{
                    size: A4;
                    margin: 2cm;
                }}
                body {{
                    font-family: Arial, sans-serif;
                    font-size: 10pt;
                    line-height: 1.6;
                    color: #333;
                }}
                h1 {{
                    color: #2c3e50;
                    font-size: 24pt;
                    margin-top: 20pt;
                    margin-bottom: 12pt;
                    page-break-after: avoid;
                }}
                h2 {{
                    color: #34495e;
                    font-size: 18pt;
                    margin-top: 16pt;
                    margin-bottom: 10pt;
                    page-break-after: avoid;
                }}
                h3 {{
                    color: #555;
                    font-size: 14pt;
                    margin-top: 12pt;
                    margin-bottom: 8pt;
                    page-break-after: avoid;
                }}
                h4 {{
                    color: #666;
                    font-size: 12pt;
                    margin-top: 10pt;
                    margin-bottom: 6pt;
                }}
                p {{
                    margin-bottom: 8pt;
                    text-align: justify;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 4px;
                    border-radius: 3px;
                    font-family: monospace;
                    font-size: 9pt;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10pt;
                    border-radius: 5px;
                    border-left: 3px solid #3498db;
                    overflow-x: auto;
                    page-break-inside: avoid;
                }}
                pre code {{
                    background-color: transparent;
                    padding: 0;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 10pt 0;
                    page-break-inside: avoid;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8pt;
                    text-align: left;
                }}
                th {{
                    background-color: #3498db;
                    color: white;
                    font-weight: bold;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
                ul, ol {{
                    margin-bottom: 8pt;
                    padding-left: 20pt;
                }}
                li {{
                    margin-bottom: 4pt;
                }}
                blockquote {{
                    border-left: 4px solid #3498db;
                    padding-left: 12pt;
                    margin-left: 0;
                    color: #555;
                    font-style: italic;
                }}
                .toc {{
                    background-color: #f8f9fa;
                    padding: 15pt;
                    border-radius: 5px;
                    margin-bottom: 20pt;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Create output directory
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # PDF options
        options = {
            'page-size': 'A4',
            'margin-top': '2cm',
            'margin-right': '2cm',
            'margin-bottom': '2cm',
            'margin-left': '2cm',
            'encoding': 'UTF-8',
            'enable-local-file-access': None,
            'footer-center': '[page] / [topage]',
            'footer-font-size': '9',
        }
        
        # Convert HTML to PDF
        pdfkit.from_string(html_doc, str(output_path), options=options)
        
        logger.info(f"  → Created: {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"  ✗ Failed to convert {input_path}: {e}")
        return False


def main():
    """Main execution function."""
    logger.info("=== Handbook PDF Generator ===")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Find all handbooks
    handbooks = find_handbooks()
    
    if not handbooks:
        logger.warning("No handbook files found in Handbook/ directory")
        sys.exit(0)
    
    logger.info(f"Found {len(handbooks)} handbook(s) to convert")
    
    # Convert each handbook
    success_count = 0
    failed_count = 0
    
    for input_path, output_path in handbooks:
        if convert_markdown_to_pdf(input_path, output_path):
            success_count += 1
        else:
            failed_count += 1
    
    # Summary
    logger.info("\n=== Conversion Summary ===")
    logger.info(f"Successfully converted: {success_count}")
    logger.info(f"Failed: {failed_count}")
    logger.info(f"Output directory: PDF_Output/")
    
    if failed_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
