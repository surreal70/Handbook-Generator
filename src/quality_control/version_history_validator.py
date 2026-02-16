"""
Version History Validator for Quality Control System.

This module validates that all template files contain version history metadata
and reports any templates with missing or invalid version history sections.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import re
from pathlib import Path
from typing import List
import logging

from .base_validator import BaseValidator
from .data_structures import TemplateFile, VersionHistoryValidationResult


class VersionHistoryValidator(BaseValidator):
    """
    Validator for template version history metadata.
    
    Ensures all template files contain version history sections with proper
    formatting and at least one version entry.
    """
    
    # Regex patterns for version history section headers (German and English)
    VERSION_HISTORY_PATTERNS = [
        re.compile(r'^##\s+Version\s+History\s*$', re.IGNORECASE | re.MULTILINE),
        re.compile(r'^##\s+Versionshistorie\s*$', re.IGNORECASE | re.MULTILINE),
    ]
    
    # Files to exclude from scanning
    EXCLUDED_FILES = [
        'metadata.yaml',
        'metadata.yml',
        'README.md',
        'README.en.md',
        'README.de.md',
        '9999_Framework_Mapping.md',
    ]
    
    def __init__(self, base_path: str = "."):
        """
        Initialize the Version History Validator.
        
        Args:
            base_path: Base path of the project (default: current directory)
        """
        super().__init__()
        self.base_path = Path(base_path)
        self.logger = logging.getLogger(__name__)
    
    def scan_templates(self, framework_path: str = None) -> List[TemplateFile]:
        """
        Find all template Markdown files in framework directories.
        
        Args:
            framework_path: Optional specific framework path to scan
            
        Returns:
            List of TemplateFile objects for all discovered templates
        """
        templates = []
        
        if framework_path:
            search_paths = [Path(framework_path)]
        else:
            # Scan both German and English template directories
            search_paths = []
            for language in ['de', 'en']:
                templates_dir = self.base_path / 'templates' / language
                if templates_dir.exists() and templates_dir.is_dir():
                    search_paths.append(templates_dir)
        
        for search_path in search_paths:
            # Determine language from path
            if '/de/' in str(search_path) or str(search_path).endswith('/de'):
                language = 'de'
            elif '/en/' in str(search_path) or str(search_path).endswith('/en'):
                language = 'en'
            else:
                language = 'unknown'
            
            try:
                # Recursively find all .md files
                for md_file in search_path.rglob('*.md'):
                    # Skip excluded files
                    if md_file.name in self.EXCLUDED_FILES:
                        continue
                    
                    # Determine framework name from path
                    try:
                        # Get the framework directory (parent of the template file)
                        relative_path = md_file.relative_to(search_path)
                        framework = relative_path.parts[0] if relative_path.parts else 'unknown'
                    except ValueError:
                        framework = 'unknown'
                    
                    # Parse the file for version history
                    has_version_history, format_valid, version_count = self._parse_version_history(md_file)
                    
                    template_file = TemplateFile(
                        path=md_file,
                        framework=framework,
                        language=language,
                        has_version_history=has_version_history,
                        version_history_format_valid=format_valid,
                        version_entries=version_count
                    )
                    templates.append(template_file)
            
            except PermissionError as e:
                self.logger.error(f"Permission denied accessing {search_path}: {e}")
            except Exception as e:
                self.logger.error(f"Error scanning {search_path}: {e}")
        
        return templates
    
    def _parse_version_history(self, file_path: Path) -> tuple:
        """
        Parse a Markdown file for version history section.
        
        Args:
            file_path: Path to the Markdown file
            
        Returns:
            Tuple of (has_version_history, format_valid, version_count)
        """
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            self.logger.warning(f"Could not read file {file_path}: {e}")
            return (False, False, 0)
        
        # Check for version history section header
        has_section = False
        section_match = None
        
        for pattern in self.VERSION_HISTORY_PATTERNS:
            match = pattern.search(content)
            if match:
                has_section = True
                section_match = match
                break
        
        if not has_section:
            return (False, False, 0)
        
        # Extract content after the version history header
        section_start = section_match.end()
        
        # Find the next section header (## ) or end of file
        next_section_pattern = re.compile(r'^##\s+', re.MULTILINE)
        next_section_match = next_section_pattern.search(content, section_start)
        
        if next_section_match:
            section_content = content[section_start:next_section_match.start()]
        else:
            section_content = content[section_start:]
        
        # Count version entries (lines that look like version entries)
        # Common patterns: "- Version X.Y", "* Version X.Y", "### Version X.Y", etc.
        version_entry_pattern = re.compile(
            r'(?:^[-*]\s+|^###\s+)?[Vv]ersion\s+\d+',
            re.MULTILINE
        )
        version_entries = version_entry_pattern.findall(section_content)
        version_count = len(version_entries)
        
        # Format is valid if there's at least one version entry
        format_valid = version_count > 0
        
        return (True, format_valid, version_count)
    
    def validate_version_history(self, templates: List[TemplateFile]) -> VersionHistoryValidationResult:
        """
        Validate that all templates have valid version history.
        
        Args:
            templates: List of TemplateFile objects to validate
            
        Returns:
            VersionHistoryValidationResult with validation status and details
        """
        valid_templates = []
        missing_version_history = []
        invalid_format = []
        
        for template in templates:
            if not template.has_version_history:
                missing_version_history.append(template)
            elif not template.version_history_format_valid:
                invalid_format.append(template)
            else:
                valid_templates.append(template)
        
        total = len(templates)
        valid_count = len(valid_templates)
        success = (valid_count == total)
        
        return VersionHistoryValidationResult(
            total_templates=total,
            valid_templates=valid_count,
            missing_version_history=missing_version_history,
            invalid_format=invalid_format,
            success=success
        )
    
    def validate(self) -> VersionHistoryValidationResult:
        """
        Execute the complete validation process.
        
        Returns:
            VersionHistoryValidationResult with validation status and details
        """
        try:
            templates = self.scan_templates()
            result = self.validate_version_history(templates)
            return result
        except Exception as e:
            self.logger.error(f"Validation failed: {e}")
            return VersionHistoryValidationResult(
                total_templates=0,
                valid_templates=0,
                missing_version_history=[],
                invalid_format=[],
                success=False,
                error=str(e)
            )
    
    def generate_report(self, result: VersionHistoryValidationResult) -> str:
        """
        Generate a human-readable report from validation results.
        
        Args:
            result: VersionHistoryValidationResult object
            
        Returns:
            Formatted report as a string
        """
        lines = []
        lines.append("=" * 80)
        lines.append("Version History Validation Report")
        lines.append("=" * 80)
        lines.append("")
        
        if result.error:
            lines.append(f"ERROR: {result.error}")
            lines.append("")
            return "\n".join(lines)
        
        # Summary statistics
        lines.append("Summary:")
        lines.append(f"  Total Templates: {result.total_templates}")
        lines.append(f"  Valid Templates: {result.valid_templates}")
        lines.append(f"  Missing Version History: {len(result.missing_version_history)}")
        lines.append(f"  Invalid Format: {len(result.invalid_format)}")
        
        if result.total_templates > 0:
            compliance_rate = (result.valid_templates / result.total_templates) * 100
            lines.append(f"  Compliance Rate: {compliance_rate:.1f}%")
        
        lines.append(f"  Status: {'PASS' if result.success else 'FAIL'}")
        lines.append("")
        
        # List templates with missing version history
        if result.missing_version_history:
            lines.append("Templates Missing Version History:")
            for template in result.missing_version_history[:20]:  # Limit to first 20
                lines.append(f"  - {template.framework}/{template.path.name} ({template.language})")
            
            if len(result.missing_version_history) > 20:
                remaining = len(result.missing_version_history) - 20
                lines.append(f"  ... and {remaining} more")
            lines.append("")
            
            # Remediation suggestion
            lines.append("Remediation: Add a '## Version History' or '## Versionshistorie' section")
            lines.append("with at least one version entry to each template.")
            lines.append("")
        
        # List templates with invalid format
        if result.invalid_format:
            lines.append("Templates with Invalid Version History Format:")
            for template in result.invalid_format[:20]:  # Limit to first 20
                lines.append(f"  - {template.framework}/{template.path.name} ({template.language})")
                lines.append(f"    Version entries found: {template.version_entries}")
            
            if len(result.invalid_format) > 20:
                remaining = len(result.invalid_format) - 20
                lines.append(f"  ... and {remaining} more")
            lines.append("")
            
            # Remediation suggestion
            lines.append("Remediation: Ensure version history sections contain at least one")
            lines.append("version entry (e.g., '- Version 1.0' or '### Version 1.0').")
            lines.append("")
        
        # Success message
        if result.success:
            lines.append("All templates have valid version history!")
        else:
            lines.append("Action Required: Fix the issues listed above.")
        
        lines.append("=" * 80)
        
        return "\n".join(lines)
