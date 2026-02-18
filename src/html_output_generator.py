"""
HTML Output Generator for Handbook Generator

Generates HTML mini-website from processed templates with navigation and styling.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List
import re


@dataclass
class Template:
    """
    Represents a template with its metadata.
    
    Attributes:
        number: Template number (e.g., '0010')
        name: Template name (e.g., 'Zweck_und_Geltungsbereich')
        title: Human-readable title
        content: Processed markdown content
        filename: Original filename
    """
    number: str
    name: str
    title: str
    content: str
    filename: str


class HTMLOutputGenerator:
    """
    Generates HTML mini-website from processed templates.
    
    Creates separate HTML files for each template with:
    - Table of contents index page
    - Navigation between pages (previous/next/TOC)
    - Consistent styling across all pages
    """
    
    def __init__(self, output_dir: Path, test_mode: bool = False):
        """
        Initialize HTML output generator.
        
        Args:
            output_dir: Base directory for output files (e.g., "test-output")
            test_mode: Whether test mode is enabled (required for output generation)
        """
        self.output_dir = Path(output_dir)
        self.test_mode = test_mode
    
    def ensure_output_structure(self, language: str, handbook_type: str = None) -> Path:
        """
        Ensure HTML output directory structure exists.
        
        Creates directory structure:
        output_dir/language/handbook_type/html/ (if handbook_type provided)
        output_dir/language/html/ (if handbook_type not provided - backward compatible)
        
        Args:
            language: Language code (e.g., 'de', 'en')
            handbook_type: Optional handbook type (e.g., 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            
        Returns:
            Path to the HTML output directory
            
        Raises:
            RuntimeError: If test mode is not enabled
        """
        if not self.test_mode:
            raise RuntimeError(
                "Output generation requires --test flag. "
                "Use --test to enable test mode output."
            )
        
        if handbook_type:
            html_dir = self.output_dir / language / handbook_type / 'html'
        else:
            html_dir = self.output_dir / language / 'html'
        
        html_dir.mkdir(parents=True, exist_ok=True)
        return html_dir
    
    def parse_template_metadata(self, filename: str, content: str) -> Template:
        """
        Parse template metadata from filename and content.
        
        Args:
            filename: Template filename (e.g., '0010_Zweck_und_Geltungsbereich.md')
            content: Template content
            
        Returns:
            Template object with parsed metadata
        """
        # Extract number and name from filename
        match = re.match(r'(\d{4})_(.+)\.md$', filename)
        if match:
            number = match.group(1)
            name = match.group(2)
        else:
            # Fallback for non-standard filenames
            number = '0000'
            name = filename.replace('.md', '')
        
        # Extract title from first heading in content
        title = name.replace('_', ' ')
        lines = content.split('\n')
        for line in lines:
            if line.strip().startswith('#'):
                # Remove markdown heading markers
                title = re.sub(r'^#+\s*', '', line.strip())
                break
        
        return Template(
            number=number,
            name=name,
            title=title,
            content=content,
            filename=filename
        )
    
    def markdown_to_html(self, markdown_content: str) -> str:
        """
        Convert markdown content to HTML.
        
        Args:
            markdown_content: Markdown content to convert
            
        Returns:
            HTML content
        """
        try:
            import markdown
            html_content = markdown.markdown(
                markdown_content,
                extensions=['extra', 'codehilite', 'toc', 'tables']
            )
            return html_content
        except ImportError:
            # Fallback: basic markdown conversion
            html_content = markdown_content
            # Convert headers
            html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
            html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
            html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
            # Convert paragraphs
            html_content = html_content.replace('\n\n', '</p><p>')
            html_content = f'<p>{html_content}</p>'
            return html_content
    
    def generate_toc_page(self, templates: List[Template], language: str, template_type: str) -> str:
        """
        Generate table of contents HTML page.
        
        Args:
            templates: List of templates
            language: Language code
            template_type: Template type
            
        Returns:
            HTML content for TOC page
        """
        # Determine page title based on language
        if language == 'de':
            page_title = f"{template_type.upper()} Handbuch - Inhaltsverzeichnis"
            toc_heading = "Inhaltsverzeichnis"
        else:
            page_title = f"{template_type.upper()} Handbook - Table of Contents"
            toc_heading = "Table of Contents"
        
        # Build TOC list
        toc_items = []
        for template in templates:
            html_filename = f"{template.number}_{template.name}.html"
            toc_items.append(
                f'<li><a href="{html_filename}">{template.number} - {template.title}</a></li>'
            )
        
        toc_list = '\n'.join(toc_items)
        
        html_content = f"""<!DOCTYPE html>
<html lang="{language}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>{toc_heading}</h1>
        </header>
        
        <main>
            <nav class="toc">
                <ul>
{toc_list}
                </ul>
            </nav>
        </main>
        
        <footer>
            <p>Generated by Handbook Generator</p>
        </footer>
    </div>
</body>
</html>"""
        
        return html_content
    
    def generate_template_page(
        self,
        template: Template,
        prev_link: Optional[str],
        next_link: Optional[str],
        language: str
    ) -> str:
        """
        Generate HTML page for single template.
        
        Args:
            template: Template to render
            prev_link: Link to previous page (None if first page)
            next_link: Link to next page (None if last page)
            language: Language code
            
        Returns:
            HTML content for template page
        """
        # Convert markdown to HTML
        content_html = self.markdown_to_html(template.content)
        
        # Build navigation
        nav_items = []
        
        if prev_link:
            prev_text = "← Zurück" if language == 'de' else "← Previous"
            nav_items.append(f'<a href="{prev_link}" class="nav-prev">{prev_text}</a>')
        else:
            nav_items.append('<span class="nav-prev disabled">—</span>')
        
        toc_text = "Inhaltsverzeichnis" if language == 'de' else "Table of Contents"
        nav_items.append(f'<a href="index.html" class="nav-toc">{toc_text}</a>')
        
        if next_link:
            next_text = "Weiter →" if language == 'de' else "Next →"
            nav_items.append(f'<a href="{next_link}" class="nav-next">{next_text}</a>')
        else:
            nav_items.append('<span class="nav-next disabled">—</span>')
        
        navigation = '\n'.join(nav_items)
        
        html_content = f"""<!DOCTYPE html>
<html lang="{language}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{template.number} - {template.title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <div class="template-number">{template.number}</div>
            <h1>{template.title}</h1>
        </header>
        
        <nav class="page-nav">
{navigation}
        </nav>
        
        <main>
{content_html}
        </main>
        
        <nav class="page-nav">
{navigation}
        </nav>
        
        <footer>
            <p>Generated by Handbook Generator</p>
        </footer>
    </div>
</body>
</html>"""
        
        return html_content
    
    def apply_styling(self) -> str:
        """
        Generate CSS stylesheet content.
        
        Returns:
            CSS content as string
        """
        css_content = """/* Handbook Generator - HTML Output Styles */

/* Reset and base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f5f5f5;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background-color: #fff;
    min-height: 100vh;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Header styles */
header {
    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
    color: #fff;
    padding: 2rem;
    border-bottom: 4px solid #3498db;
}

header h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.template-number {
    font-size: 0.9rem;
    opacity: 0.8;
    margin-bottom: 0.5rem;
}

/* Navigation styles */
.page-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #ecf0f1;
    border-bottom: 1px solid #bdc3c7;
}

.page-nav a {
    color: #2c3e50;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.page-nav a:hover {
    background-color: #3498db;
    color: #fff;
}

.page-nav .nav-toc {
    font-weight: bold;
}

.page-nav .disabled {
    color: #95a5a6;
    cursor: not-allowed;
}

/* Main content styles */
main {
    padding: 2rem;
}

main h1 {
    color: #2c3e50;
    font-size: 1.8rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
}

main h2 {
    color: #34495e;
    font-size: 1.5rem;
    margin-top: 1.5rem;
    margin-bottom: 0.8rem;
}

main h3 {
    color: #34495e;
    font-size: 1.2rem;
    margin-top: 1.2rem;
    margin-bottom: 0.6rem;
}

main p {
    margin-bottom: 1rem;
}

main ul, main ol {
    margin-left: 2rem;
    margin-bottom: 1rem;
}

main li {
    margin-bottom: 0.5rem;
}

/* Code styles */
code {
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.9em;
}

pre {
    background-color: #f4f4f4;
    padding: 1rem;
    border-radius: 5px;
    overflow-x: auto;
    margin-bottom: 1rem;
}

pre code {
    background-color: transparent;
    padding: 0;
}

/* Table styles */
table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.75rem;
    text-align: left;
}

th {
    background-color: #34495e;
    color: #fff;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

/* TOC styles */
.toc ul {
    list-style: none;
    margin-left: 0;
}

.toc li {
    margin-bottom: 0.8rem;
}

.toc a {
    color: #2c3e50;
    text-decoration: none;
    font-size: 1.1rem;
    display: block;
    padding: 0.5rem;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.toc a:hover {
    background-color: #ecf0f1;
}

/* Footer styles */
footer {
    background-color: #2c3e50;
    color: #fff;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
}

footer p {
    margin: 0;
    font-size: 0.9rem;
    opacity: 0.8;
}

/* Responsive design */
@media (max-width: 768px) {
    .container {
        box-shadow: none;
    }
    
    header, main, .page-nav {
        padding: 1rem;
    }
    
    header h1 {
        font-size: 1.5rem;
    }
    
    .page-nav {
        flex-direction: column;
        gap: 0.5rem;
    }
}
"""
        return css_content
    
    def generate_html_site(
        self,
        processed_contents: List[str],
        filenames: List[str],
        language: str,
        template_type: str
    ) -> dict:
        """
        Generate complete HTML mini-website.
        
        Args:
            processed_contents: List of processed template contents
            filenames: List of template filenames
            language: Language code (e.g., 'de', 'en')
            template_type: Template type (e.g., 'bcm', 'isms', 'bsi-grundschutz', 'it-operation')
            
        Returns:
            Dictionary with:
                - 'html_dir': Path to HTML output directory
                - 'files': List of generated file paths
                - 'warnings': List of warnings
                - 'errors': List of errors
        """
        result = {
            'html_dir': None,
            'files': [],
            'warnings': [],
            'errors': []
        }
        
        # Ensure output directory exists (includes handbook_type)
        try:
            html_dir = self.ensure_output_structure(language, template_type)
            result['html_dir'] = html_dir
        except RuntimeError as e:
            result['errors'].append(str(e))
            return result
        except Exception as e:
            result['errors'].append(f"Failed to create HTML output directory: {str(e)}")
            return result
        
        # Parse template metadata
        templates = []
        for filename, content in zip(filenames, processed_contents):
            try:
                template = self.parse_template_metadata(filename, content)
                templates.append(template)
            except Exception as e:
                result['warnings'].append(
                    f"Failed to parse template metadata for {filename}: {str(e)}"
                )
        
        if not templates:
            result['errors'].append("No templates to process")
            return result
        
        # Generate CSS stylesheet
        try:
            css_content = self.apply_styling()
            css_path = html_dir / 'styles.css'
            css_path.write_text(css_content, encoding='utf-8')
            result['files'].append(css_path)
        except Exception as e:
            result['errors'].append(f"Failed to generate CSS stylesheet: {str(e)}")
            return result
        
        # Generate TOC page
        try:
            toc_html = self.generate_toc_page(templates, language, template_type)
            toc_path = html_dir / 'index.html'
            toc_path.write_text(toc_html, encoding='utf-8')
            result['files'].append(toc_path)
        except Exception as e:
            result['errors'].append(f"Failed to generate TOC page: {str(e)}")
            return result
        
        # Generate template pages
        for i, template in enumerate(templates):
            try:
                # Determine previous and next links
                prev_link = None
                next_link = None
                
                if i > 0:
                    prev_template = templates[i - 1]
                    prev_link = f"{prev_template.number}_{prev_template.name}.html"
                
                if i < len(templates) - 1:
                    next_template = templates[i + 1]
                    next_link = f"{next_template.number}_{next_template.name}.html"
                
                # Generate page HTML
                page_html = self.generate_template_page(
                    template,
                    prev_link,
                    next_link,
                    language
                )
                
                # Write to file
                page_filename = f"{template.number}_{template.name}.html"
                page_path = html_dir / page_filename
                page_path.write_text(page_html, encoding='utf-8')
                result['files'].append(page_path)
                
            except Exception as e:
                result['errors'].append(
                    f"Failed to generate page for template {template.filename}: {str(e)}"
                )
        
        return result
