#!/usr/bin/env python3
"""
Generate PDF versions of example handbooks from Markdown files.

This script uses markdown and reportlab (pure Python) to convert handbooks to PDF.
No external system dependencies required beyond Python packages.
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple
import logging
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def check_and_install_dependencies() -> bool:
    """Check if required dependencies are installed, offer to install if missing."""
    missing = []
    
    try:
        import markdown
    except ImportError:
        missing.append('markdown')
    
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate
    except ImportError:
        missing.append('reportlab')
    
    if missing:
        logger.warning(f"Missing required packages: {', '.join(missing)}")
        response = input("Would you like to install them now? (y/n): ").strip().lower()
        
        if response == 'y':
            import subprocess
            try:
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install'] + missing
                )
                logger.info("Packages installed successfully")
                return True
            except subprocess.CalledProcessError:
                logger.error("Failed to install packages")
                return False
        else:
            logger.error("Please install required packages manually:")
            logger.error(f"  pip install {' '.join(missing)}")
            return False
    
    return True


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
        # Create output path
        relative_path = md_file.relative_to(base_path)
        output_path = Path("PDF_Output") / relative_path.parent / f"{md_file.stem}.pdf"
        handbooks.append((md_file, output_path))
    
    return handbooks


def convert_markdown_to_pdf(input_path: Path, output_path: Path) -> bool:
    """
    Convert a Markdown file to PDF using reportlab.
    
    Args:
        input_path: Path to input Markdown file
        output_path: Path to output PDF file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        import markdown
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import cm
        from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer, PageBreak,
            Table, TableStyle, Preformatted
        )
        from reportlab.lib import colors
        from html.parser import HTMLParser
        
        logger.info(f"Converting: {input_path}")
        
        # Read Markdown content
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert Markdown to HTML
        md = markdown.Markdown(extensions=[
            'extra',
            'tables',
            'fenced_code'
        ])
        html_content = md.convert(md_content)
        
        # Create output directory
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create PDF document
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm
        )
        
        # Container for PDF elements
        story = []
        
        # Define styles
        styles = getSampleStyleSheet()
        
        # Custom styles
        styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=12,
            spaceBefore=20
        ))
        
        styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=styles['Heading2'],
            fontSize=18,
            textColor=colors.HexColor('#34495e'),
            spaceAfter=10,
            spaceBefore=16
        ))
        
        styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=styles['Heading3'],
            fontSize=14,
            textColor=colors.HexColor('#555555'),
            spaceAfter=8,
            spaceBefore=12
        ))
        
        styles.add(ParagraphStyle(
            name='CustomBody',
            parent=styles['BodyText'],
            fontSize=10,
            alignment=TA_JUSTIFY,
            spaceAfter=8
        ))
        
        # Simple HTML to PDF converter
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.story = []
                self.current_text = []
                self.current_tag = None
                self.in_pre = False
                self.table_data = []
                self.current_row = []
                
            def handle_starttag(self, tag, attrs):
                self.current_tag = tag
                if tag == 'pre':
                    self.in_pre = True
                elif tag == 'tr':
                    self.current_row = []
                    
            def handle_endtag(self, tag):
                text = ''.join(self.current_text).strip()
                
                if tag == 'h1' and text:
                    self.story.append(Paragraph(text, styles['CustomTitle']))
                    self.story.append(Spacer(1, 0.2*cm))
                elif tag == 'h2' and text:
                    self.story.append(Paragraph(text, styles['CustomHeading2']))
                    self.story.append(Spacer(1, 0.15*cm))
                elif tag == 'h3' and text:
                    self.story.append(Paragraph(text, styles['CustomHeading3']))
                    self.story.append(Spacer(1, 0.1*cm))
                elif tag == 'p' and text:
                    self.story.append(Paragraph(text, styles['CustomBody']))
                    self.story.append(Spacer(1, 0.1*cm))
                elif tag == 'pre' and text:
                    # Handle code blocks
                    self.story.append(Preformatted(text, styles['Code']))
                    self.story.append(Spacer(1, 0.2*cm))
                    self.in_pre = False
                elif tag == 'td' or tag == 'th':
                    self.current_row.append(text)
                elif tag == 'tr' and self.current_row:
                    self.table_data.append(self.current_row)
                    self.current_row = []
                elif tag == 'table' and self.table_data:
                    # Create table
                    t = Table(self.table_data)
                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)
                    ]))
                    self.story.append(t)
                    self.story.append(Spacer(1, 0.3*cm))
                    self.table_data = []
                elif tag == 'hr':
                    self.story.append(Spacer(1, 0.5*cm))
                
                self.current_text = []
                self.current_tag = None
                
            def handle_data(self, data):
                if data.strip():
                    self.current_text.append(data)
        
        # Parse HTML and build story
        parser = SimpleHTMLParser()
        parser.feed(html_content)
        story = parser.story
        
        if not story:
            # Fallback: just add the content as paragraphs
            for line in md_content.split('\n'):
                if line.strip():
                    story.append(Paragraph(line, styles['CustomBody']))
                    story.append(Spacer(1, 0.1*cm))
        
        # Build PDF
        doc.build(story)
        
        logger.info(f"  → Created: {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"  ✗ Failed to convert {input_path}: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main execution function."""
    logger.info("=== Handbook PDF Generator ===")
    
    # Check and install dependencies
    if not check_and_install_dependencies():
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
