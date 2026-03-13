#!/usr/bin/env python3
"""
Template List Generator

Generates a comprehensive list of all templates per handbook including:
- Template name and ID
- Template version
- Revision
- Source (raw templates or rendered output)

Usage:
    python helpers/generate_template_list.py [--source raw|rendered|both] [--output OUTPUT_FILE]
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import subprocess
import json


class TemplateInfo:
    """Represents information about a single template."""
    
    def __init__(self, filename: str, title: str, doc_id: str, 
                 template_version: str, revision: str, source: str):
        self.filename = filename
        self.title = title
        self.doc_id = doc_id
        self.template_version = template_version
        self.revision = revision
        self.source = source
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON export."""
        return {
            'filename': self.filename,
            'title': self.title,
            'document_id': self.doc_id,
            'template_version': self.template_version,
            'revision': self.revision,
            'source': self.source
        }


class TemplateListGenerator:
    """Generates lists of templates per handbook."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.templates_dir = project_root / 'templates'
        self.test_output_dir = project_root / 'test-output'
        
    def extract_template_info(self, file_path: Path, source: str) -> Optional[TemplateInfo]:
        """Extract template information from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title (first # heading)
            title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else 'N/A'
            
            # Extract Document ID
            doc_id_match = re.search(r'\*\*(?:Dokument-ID|Document-ID):\*\*\s*(.+?)$', 
                                    content, re.MULTILINE | re.IGNORECASE)
            doc_id = doc_id_match.group(1).strip() if doc_id_match else 'N/A'
            
            # Extract Template Version
            version_match = re.search(r'\*\*(?:Template Version|Template-Version):\*\*\s*(.+?)$',
                                     content, re.MULTILINE | re.IGNORECASE)
            template_version = version_match.group(1).strip() if version_match else 'N/A'
            
            # Extract Revision
            revision_match = re.search(r'\*\*Revision:\*\*\s*(.+?)$',
                                      content, re.MULTILINE | re.IGNORECASE)
            revision = revision_match.group(1).strip() if revision_match else 'N/A'
            
            return TemplateInfo(
                filename=file_path.name,
                title=title,
                doc_id=doc_id,
                template_version=template_version,
                revision=revision,
                source=source
            )
        except Exception as e:
            print(f"Warning: Could not parse {file_path}: {e}", file=sys.stderr)
            return None
    
    def get_raw_templates(self, language: str, handbook: str) -> List[TemplateInfo]:
        """Get template information from raw template directory."""
        templates = []
        template_path = self.templates_dir / language / handbook
        
        if not template_path.exists():
            return templates
        
        for md_file in sorted(template_path.glob('*.md')):
            # Skip README and TOC files
            if md_file.name.upper() in ('README.MD', 'TOC.MD'):
                continue
            
            info = self.extract_template_info(md_file, 'raw')
            if info:
                templates.append(info)
        
        return templates
    
    def get_rendered_templates(self, language: str, handbook: str) -> List[TemplateInfo]:
        """Get template information from rendered output directory."""
        templates = []
        # Try both possible output structures
        output_paths = [
            self.test_output_dir / language / handbook / 'markdown',
            self.test_output_dir / f'{language}_{handbook}'
        ]
        
        output_path = None
        for path in output_paths:
            if path.exists():
                output_path = path
                break
        
        if not output_path:
            print(f"Warning: Rendered output not found for {language}/{handbook}", 
                  file=sys.stderr)
            return templates
        
        for md_file in sorted(output_path.glob('*.md')):
            # Skip README and TOC files
            if md_file.name.upper() in ('README.MD', 'TOC.MD'):
                continue
            
            info = self.extract_template_info(md_file, 'rendered')
            if info:
                templates.append(info)
        
        return templates
    
    def render_handbook(self, language: str, handbook: str) -> bool:
        """Render a handbook using the handbook-generator CLI."""
        print(f"Rendering {language}/{handbook}...")
        
        try:
            # Use the CLI to generate the handbook
            cmd = [
                sys.executable, '-m', 'src.cli',
                '--language', language,
                '--handbook', handbook,
                '--output-format', 'markdown-single'
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print(f"Successfully rendered {language}/{handbook}")
                return True
            else:
                print(f"Error rendering {language}/{handbook}: {result.stderr}", 
                      file=sys.stderr)
                return False
                
        except Exception as e:
            print(f"Failed to render {language}/{handbook}: {e}", file=sys.stderr)
            return False
    
    def discover_handbooks(self) -> List[Tuple[str, str]]:
        """Discover all available handbooks (language, handbook pairs)."""
        handbooks = []
        
        for lang_dir in self.templates_dir.iterdir():
            if not lang_dir.is_dir():
                continue
            
            language = lang_dir.name
            
            for handbook_dir in lang_dir.iterdir():
                if not handbook_dir.is_dir():
                    continue
                
                handbook = handbook_dir.name
                handbooks.append((language, handbook))
        
        return sorted(handbooks)
    
    def generate_report(self, source: str = 'both', 
                       language_filter: str = 'all',
                       handbook_filter: str = 'all',
                       output_file: Optional[str] = None) -> str:
        """Generate a comprehensive template list report."""
        handbooks = self.discover_handbooks()
        
        # Apply filters
        if language_filter != 'all':
            handbooks = [(lang, hb) for lang, hb in handbooks if lang == language_filter]
        
        if handbook_filter and handbook_filter != 'all':
            handbooks = [(lang, hb) for lang, hb in handbooks if hb == handbook_filter]
        
        report_lines = []
        report_lines.append("=" * 150)
        report_lines.append("TEMPLATE LIST REPORT")
        report_lines.append("=" * 150)
        report_lines.append(f"Source: {source}")
        if language_filter != 'all':
            report_lines.append(f"Language: {language_filter}")
        if handbook_filter and handbook_filter != 'all':
            report_lines.append(f"Handbook: {handbook_filter}")
        report_lines.append(f"Total Handbooks: {len(handbooks)}")
        report_lines.append("=" * 150)
        report_lines.append("")
        
        all_data = {}
        
        for language, handbook in handbooks:
            handbook_key = f"{language}/{handbook}"
            report_lines.append(f"\n{'=' * 150}")
            report_lines.append(f"HANDBOOK: {handbook_key}")
            report_lines.append(f"{'=' * 150}\n")
            
            templates = []
            
            if source in ('raw', 'both'):
                raw_templates = self.get_raw_templates(language, handbook)
                templates.extend(raw_templates)
            
            if source in ('rendered', 'both'):
                # Check if rendered output exists
                output_paths = [
                    self.test_output_dir / language / handbook / 'markdown',
                    self.test_output_dir / f'{language}_{handbook}'
                ]
                
                output_exists = any(path.exists() for path in output_paths)
                
                if not output_exists:
                    print(f"\nRendered output not found for {handbook_key}. Rendering now...")
                    if self.render_handbook(language, handbook):
                        rendered_templates = self.get_rendered_templates(language, handbook)
                    else:
                        rendered_templates = []
                        report_lines.append(f"\n⚠️  Failed to render {handbook_key}\n")
                else:
                    rendered_templates = self.get_rendered_templates(language, handbook)
                
                templates.extend(rendered_templates)
            
            # For 'both' mode, combine raw and rendered in one table
            if source == 'both':
                self._add_combined_template_table(report_lines, templates)
            else:
                self._add_template_table(report_lines, templates)
            
            # Store data for JSON export
            all_data[handbook_key] = [t.to_dict() for t in templates]
            
            report_lines.append(f"\nTotal Templates: {len(templates)}\n")
        
        report = '\n'.join(report_lines)
        
        # Write to file if specified
        if output_file:
            output_path = Path(output_file)
            
            # Write text report
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\nReport written to: {output_path}")
            
            # Also write JSON version
            json_path = output_path.with_suffix('.json')
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(all_data, f, indent=2, ensure_ascii=False)
            print(f"JSON data written to: {json_path}")
        
        return report
    
    def _add_template_table(self, report_lines: List[str], 
                           templates: List[TemplateInfo]) -> None:
        """Add a formatted table of templates to the report."""
        if not templates:
            report_lines.append("No templates found.\n")
            return
        
        # Table header with adjusted widths (filename reduced by 20%)
        report_lines.append(f"{'Filename':<60} {'Doc ID':<23} {'Version':<30} {'Revision':<23}")
        report_lines.append(f"{'-' * 60} {'-' * 23} {'-' * 30} {'-' * 23}")
        
        # Table rows
        for template in templates:
            filename = template.filename[:58] + '..' if len(template.filename) > 60 else template.filename
            doc_id = template.doc_id[:21] + '..' if len(template.doc_id) > 23 else template.doc_id
            version = template.template_version[:28] + '..' if len(template.template_version) > 30 else template.template_version
            revision = template.revision[:21] + '..' if len(template.revision) > 23 else template.revision
            
            report_lines.append(f"{filename:<60} {doc_id:<23} {version:<30} {revision:<23}")
        
        report_lines.append("")
    
    def _add_combined_template_table(self, report_lines: List[str], 
                                    templates: List[TemplateInfo]) -> None:
        """Add a combined table showing both raw and rendered templates side by side."""
        if not templates:
            report_lines.append("No templates found.\n")
            return
        
        # Separate raw and rendered templates
        raw_templates = {t.filename: t for t in templates if t.source == 'raw'}
        rendered_templates = {t.filename: t for t in templates if t.source == 'rendered'}
        
        # Get all unique filenames
        all_filenames = sorted(set(raw_templates.keys()) | set(rendered_templates.keys()))
        
        # Table header with adjusted widths (filename reduced by 20%)
        report_lines.append(f"{'Filename':<60} {'Doc ID':<23} {'Raw Ver':<30} {'Raw Rev':<23} {'Rnd Ver':<30} {'Rnd Rev':<23}")
        report_lines.append(f"{'-' * 60} {'-' * 23} {'-' * 30} {'-' * 23} {'-' * 30} {'-' * 23}")
        
        # Table rows
        for filename in all_filenames:
            raw = raw_templates.get(filename)
            rendered = rendered_templates.get(filename)
            
            # Filename (truncate if needed)
            fn = filename[:58] + '..' if len(filename) > 60 else filename
            
            # Doc ID (use raw if available, otherwise rendered)
            doc_id = (raw.doc_id if raw else rendered.doc_id) if (raw or rendered) else 'N/A'
            doc_id = doc_id[:21] + '..' if len(doc_id) > 23 else doc_id
            
            # Raw version and revision
            raw_ver = raw.template_version[:28] + '..' if raw and len(raw.template_version) > 30 else (raw.template_version if raw else '-')
            raw_rev = raw.revision[:21] + '..' if raw and len(raw.revision) > 23 else (raw.revision if raw else '-')
            
            # Rendered version and revision
            rnd_ver = rendered.template_version[:28] + '..' if rendered and len(rendered.template_version) > 30 else (rendered.template_version if rendered else '-')
            rnd_rev = rendered.revision[:21] + '..' if rendered and len(rendered.revision) > 23 else (rendered.revision if rendered else '-')
            
            report_lines.append(f"{fn:<60} {doc_id:<23} {raw_ver:<30} {raw_rev:<23} {rnd_ver:<30} {rnd_rev:<23}")
        
        report_lines.append("")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate a list of all templates per handbook',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List both raw and rendered templates (default)
  python helpers/generate_template_list.py
  
  # List only raw templates
  python helpers/generate_template_list.py --source raw
  
  # List only rendered templates (will render if needed)
  python helpers/generate_template_list.py --source rendered
  
  # Filter by language
  python helpers/generate_template_list.py --language de
  python helpers/generate_template_list.py --language en
  
  # Filter by handbook
  python helpers/generate_template_list.py --handbook it-operation
  python helpers/generate_template_list.py --handbook bcm --language de
  
  # Save report to file
  python helpers/generate_template_list.py --output template_report.txt
  python helpers/generate_template_list.py --handbook isms --language en --output isms_en.txt
        """
    )
    
    parser.add_argument(
        '--source',
        choices=['raw', 'rendered', 'both'],
        default='both',
        help='Source of templates to list (default: both)'
    )
    
    parser.add_argument(
        '--language',
        '-l',
        choices=['de', 'en', 'all'],
        default='all',
        help='Language to filter (default: all)'
    )
    
    parser.add_argument(
        '--handbook',
        '-b',
        help='Specific handbook to report on (e.g., it-operation, bcm, isms). Use "all" for all handbooks (default: all)'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        help='Output file path (optional, prints to stdout if not specified)'
    )
    
    args = parser.parse_args()
    
    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Generate report
    generator = TemplateListGenerator(project_root)
    
    # Handle handbook filter
    handbook_filter = args.handbook if args.handbook else 'all'
    
    report = generator.generate_report(
        source=args.source,
        language_filter=args.language,
        handbook_filter=handbook_filter,
        output_file=args.output
    )
    
    # Print to stdout if no output file specified
    if not args.output:
        print(report)


if __name__ == '__main__':
    main()
