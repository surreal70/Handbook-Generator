"""
Coverage Documentation Generator for the Quality Control System.

This module generates comprehensive documentation of all supported frameworks,
including template counts, bilingual consistency checks, and metadata extraction.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import os
from pathlib import Path
from typing import List, Optional
import logging

from .base_validator import BaseValidator
from .data_structures import Framework, TemplateCounts, ConsistencyReport


class CoverageDocumentationGenerator(BaseValidator):
    """
    Generates comprehensive documentation of framework coverage.
    
    This class scans framework directories, counts templates, extracts metadata,
    checks bilingual consistency, and generates Markdown documentation.
    """
    
    def __init__(self, base_path: str = "."):
        """
        Initialize the coverage documentation generator.
        
        Args:
            base_path: Base path to the project root (default: current directory)
        """
        super().__init__()
        self.base_path = Path(base_path)
        self.templates_path = self.base_path / "templates"
        
    def discover_frameworks(self) -> List[Framework]:
        """
        Discover all frameworks by scanning template directories.
        
        Scans both templates/de/ and templates/en/ directories to identify
        all available frameworks and extract their information.
        
        Returns:
            List of Framework objects with discovered information.
        """
        self.logger.info("Discovering frameworks in template directories")
        
        frameworks_dict = {}
        
        # Scan German templates
        de_path = self.templates_path / "de"
        if de_path.exists() and de_path.is_dir():
            for framework_dir in de_path.iterdir():
                if framework_dir.is_dir():
                    name = framework_dir.name
                    if name not in frameworks_dict:
                        frameworks_dict[name] = {
                            'name': name,
                            'path_de': framework_dir,
                            'path_en': None,
                            'template_count_de': 0,
                            'template_count_en': 0,
                            'standard': '',
                            'description': ''
                        }
                    else:
                        frameworks_dict[name]['path_de'] = framework_dir
        
        # Scan English templates
        en_path = self.templates_path / "en"
        if en_path.exists() and en_path.is_dir():
            for framework_dir in en_path.iterdir():
                if framework_dir.is_dir():
                    name = framework_dir.name
                    if name not in frameworks_dict:
                        frameworks_dict[name] = {
                            'name': name,
                            'path_de': None,
                            'path_en': framework_dir,
                            'template_count_de': 0,
                            'template_count_en': 0,
                            'standard': '',
                            'description': ''
                        }
                    else:
                        frameworks_dict[name]['path_en'] = framework_dir
        
        # Convert to Framework objects
        frameworks = []
        for name, data in frameworks_dict.items():
            # Count templates
            if data['path_de']:
                data['template_count_de'] = self._count_templates(data['path_de'])
            if data['path_en']:
                data['template_count_en'] = self._count_templates(data['path_en'])
            
            # Extract metadata
            metadata = self._extract_metadata(data['path_de'] or data['path_en'])
            data['standard'] = metadata.get('standard', '')
            data['description'] = metadata.get('description', '')
            
            # Check bilingual consistency
            bilingual_consistent = data['template_count_de'] == data['template_count_en']
            
            framework = Framework(
                name=name,
                standard=data['standard'],
                description=data['description'],
                template_count_de=data['template_count_de'],
                template_count_en=data['template_count_en'],
                path_de=data['path_de'] or Path(),
                path_en=data['path_en'] or Path(),
                bilingual_consistent=bilingual_consistent
            )
            frameworks.append(framework)
        
        self.logger.info(f"Discovered {len(frameworks)} frameworks")
        return frameworks
    
    def _count_templates(self, framework_path: Path) -> int:
        """
        Count template files in a framework directory.
        
        Counts .md files excluding metadata files, mapping files, and README files.
        This provides an accurate count of content templates for DE and EN separately.
        
        Args:
            framework_path: Path to the framework directory
            
        Returns:
            Number of template files (excluding metadata and mapping files)
        """
        count = 0
        if not framework_path.exists():
            return count
        
        for file in framework_path.iterdir():
            if file.is_file() and file.suffix == '.md':
                # Exclude metadata and mapping files
                filename_lower = file.name.lower()
                if not filename_lower.startswith('metadata') and \
                   not file.name.endswith('Framework_Mapping.md') and \
                   filename_lower != 'readme.md':
                    count += 1
        
        return count
    
    def count_templates_detailed(self, framework_path: Path) -> TemplateCounts:
        """
        Count templates with detailed categorization.
        
        Args:
            framework_path: Path to the framework directory
            
        Returns:
            TemplateCounts object with detailed counts
        """
        counts = TemplateCounts(
            total=0,
            content_templates=0,
            metadata_templates=0,
            mapping_files=0
        )
        
        if not framework_path.exists():
            return counts
        
        for file in framework_path.iterdir():
            if file.is_file() and file.suffix == '.md':
                counts.total += 1
                
                filename_lower = file.name.lower()
                if filename_lower.startswith('metadata'):
                    counts.metadata_templates += 1
                elif file.name.endswith('Framework_Mapping.md'):
                    counts.mapping_files += 1
                elif filename_lower != 'readme.md':
                    counts.content_templates += 1
        
        return counts
    
    def _extract_metadata(self, framework_path: Optional[Path]) -> dict:
        """
        Extract metadata from framework README.md file.
        
        Args:
            framework_path: Path to the framework directory
            
        Returns:
            Dictionary with 'standard' and 'description' keys
        """
        metadata = {'standard': '', 'description': ''}
        
        if not framework_path or not framework_path.exists():
            return metadata
        
        readme_path = framework_path / "README.md"
        if not readme_path.exists():
            return metadata
        
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract standard (look for common patterns)
            lines = content.split('\n')
            for line in lines:
                line_lower = line.lower()
                if 'standard' in line_lower or 'iso' in line_lower or \
                   'nist' in line_lower or 'gdpr' in line_lower:
                    # Extract the standard identifier
                    metadata['standard'] = line.strip('# ').strip()
                    break
            
            # Extract description (first paragraph after title)
            in_description = False
            description_lines = []
            for line in lines:
                if line.startswith('#'):
                    in_description = True
                    continue
                if in_description and line.strip():
                    description_lines.append(line.strip())
                    if len(description_lines) >= 2:
                        break
            
            metadata['description'] = ' '.join(description_lines)
            
        except Exception as e:
            self.logger.warning(f"Failed to extract metadata from {readme_path}: {e}")
        
        return metadata
    
    def validate(self) -> List[Framework]:
        """
        Execute framework discovery and return the list of frameworks.
        
        Returns:
            List of discovered Framework objects.
        """
        return self.discover_frameworks()
    
    def check_bilingual_consistency(self, frameworks: List[Framework]) -> ConsistencyReport:
        """
        Check bilingual consistency across frameworks.
        
        Compares template counts between German and English versions of each
        framework and identifies discrepancies and missing translations.
        
        Args:
            frameworks: List of Framework objects to check
            
        Returns:
            ConsistencyReport with consistent and inconsistent frameworks
        """
        consistent = []
        inconsistent = []
        missing_translations = []
        
        for framework in frameworks:
            if framework.bilingual_consistent:
                consistent.append(framework)
            else:
                inconsistent.append(framework)
                
                # Identify which language is missing templates
                if framework.template_count_de > framework.template_count_en:
                    missing_translations.append((framework, 'en'))
                elif framework.template_count_en > framework.template_count_de:
                    missing_translations.append((framework, 'de'))
        
        return ConsistencyReport(
            consistent_frameworks=consistent,
            inconsistent_frameworks=inconsistent,
            missing_translations=missing_translations
        )
    
    def generate_report(self, frameworks: List[Framework]) -> str:
        """
        Generate a human-readable report from framework list.
        
        Args:
            frameworks: List of Framework objects
            
        Returns:
            Formatted report as a string.
        """
        report = []
        report.append("=" * 80)
        report.append("Framework Coverage Report")
        report.append("=" * 80)
        report.append("")
        report.append(f"Total Frameworks: {len(frameworks)}")
        report.append("")
        
        for framework in frameworks:
            report.append(f"Framework: {framework.name}")
            report.append(f"  Standard: {framework.standard or 'N/A'}")
            report.append(f"  Templates (DE): {framework.template_count_de}")
            report.append(f"  Templates (EN): {framework.template_count_en}")
            report.append(f"  Bilingual Consistent: {'Yes' if framework.bilingual_consistent else 'No'}")
            report.append("")
        
        return "\n".join(report)
    
    def generate_markdown_documentation(self, frameworks: List[Framework]) -> str:
        """
        Generate comprehensive Markdown documentation for all frameworks.
        
        Creates a Markdown table with framework information including name,
        standard, template counts, and description. Includes a summary section
        with totals.
        
        Args:
            frameworks: List of Framework objects
            
        Returns:
            Formatted Markdown documentation as a string.
        """
        lines = []
        
        # Title
        lines.append("# Framework Coverage Documentation")
        lines.append("")
        lines.append("This document provides a comprehensive overview of all supported compliance frameworks in the Handbook Generator.")
        lines.append("")
        
        # Summary section
        total_templates_de = sum(f.template_count_de for f in frameworks)
        total_templates_en = sum(f.template_count_en for f in frameworks)
        consistent_count = sum(1 for f in frameworks if f.bilingual_consistent)
        
        lines.append("## Summary")
        lines.append("")
        lines.append(f"- **Total Frameworks**: {len(frameworks)}")
        lines.append(f"- **Total Templates (DE)**: {total_templates_de}")
        lines.append(f"- **Total Templates (EN)**: {total_templates_en}")
        lines.append(f"- **Bilingual Consistent**: {consistent_count}/{len(frameworks)}")
        lines.append("")
        
        # Framework table
        lines.append("## Frameworks")
        lines.append("")
        lines.append("| Framework | Standard | Templates (DE) | Templates (EN) | Consistent | Description |")
        lines.append("|-----------|----------|----------------|----------------|------------|-------------|")
        
        for framework in sorted(frameworks, key=lambda f: f.name):
            name = framework.name
            standard = framework.standard or "N/A"
            count_de = framework.template_count_de
            count_en = framework.template_count_en
            consistent = "✓" if framework.bilingual_consistent else "✗"
            description = framework.description[:100] + "..." if len(framework.description) > 100 else framework.description
            description = description.replace("|", "\\|")  # Escape pipe characters
            
            lines.append(f"| {name} | {standard} | {count_de} | {count_en} | {consistent} | {description} |")
        
        lines.append("")
        
        # Inconsistent frameworks section
        inconsistent = [f for f in frameworks if not f.bilingual_consistent]
        if inconsistent:
            lines.append("## Bilingual Inconsistencies")
            lines.append("")
            lines.append("The following frameworks have different template counts between German and English:")
            lines.append("")
            
            for framework in sorted(inconsistent, key=lambda f: f.name):
                diff = abs(framework.template_count_de - framework.template_count_en)
                missing_lang = "EN" if framework.template_count_de > framework.template_count_en else "DE"
                lines.append(f"- **{framework.name}**: {diff} template(s) missing in {missing_lang}")
            
            lines.append("")
        
        return "\n".join(lines)
    
    def save_documentation(self, content: str, output_path: str = "docs/FRAMEWORK_COVERAGE.md") -> None:
        """
        Save documentation to a file.
        
        Creates the output directory if it doesn't exist and writes the
        documentation content to the specified file.
        
        Args:
            content: Documentation content to save
            output_path: Path where to save the documentation (default: docs/FRAMEWORK_COVERAGE.md)
            
        Raises:
            IOError: If file write fails
        """
        output_file = Path(output_path)
        
        # Create directory if it doesn't exist
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.logger.info(f"Documentation saved to {output_file}")
        except Exception as e:
            self.logger.error(f"Failed to save documentation to {output_file}: {e}")
            raise IOError(f"Failed to save documentation: {e}")
