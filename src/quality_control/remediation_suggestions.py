"""
Remediation suggestion system for quality control issues.

This module provides automated suggestions for fixing common quality control
issues such as missing mapping files, missing version history, and missing
translations.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import logging
from typing import List, Dict, Optional
from pathlib import Path

from .data_structures import (
    FrameworkInfo,
    TemplateFile,
    Framework,
    ValidationResult,
    VersionHistoryValidationResult
)


class RemediationSuggestions:
    """
    Generates remediation suggestions for quality control issues.
    
    Provides actionable suggestions with code snippets and commands for
    fixing common issues identified by quality control validators.
    """
    
    def __init__(self):
        """Initialize the remediation suggestions generator."""
        self.logger = logging.getLogger(__name__)
    
    def suggest_missing_mapping_file(self, framework: FrameworkInfo) -> Dict[str, str]:
        """
        Generate suggestion for creating a missing framework mapping file.
        
        Args:
            framework: FrameworkInfo object for framework missing mapping file
            
        Returns:
            Dictionary with suggestion details:
            {
                'issue': str,
                'suggestion': str,
                'command': str,
                'template': str
            }
        """
        file_path = framework.path / "9999_Framework_Mapping.md"
        
        template = f"""# Framework Mapping: {framework.name.upper()}

## Overview

This document maps the requirements and controls of {framework.name.upper()} to the 
corresponding handbook templates.

## Mapping Table

| Control ID | Control Name | Template File | Notes |
|------------|--------------|---------------|-------|
| [ID] | [Name] | [Template] | [Notes] |

## Coverage Summary

- Total Controls: [NUMBER]
- Mapped Controls: [NUMBER]
- Coverage: [PERCENTAGE]%

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | {Path.cwd()} | [Author] | Initial mapping document |
"""
        
        command = f"# Create the mapping file\ncat > {file_path} << 'EOF'\n{template}EOF"
        
        return {
            'issue': f"Missing mapping file: {framework.language}/{framework.name}/9999_Framework_Mapping.md",
            'suggestion': f"Create the standardized mapping file at: {file_path}",
            'command': command,
            'template': template,
            'file_path': str(file_path)
        }
    
    def suggest_incorrect_mapping_filename(self, framework: FrameworkInfo) -> Dict[str, str]:
        """
        Generate suggestion for renaming an incorrectly named mapping file.
        
        Args:
            framework: FrameworkInfo object with incorrect mapping file name
            
        Returns:
            Dictionary with suggestion details
        """
        old_path = framework.path / framework.mapping_file_name
        new_path = framework.path / "9999_Framework_Mapping.md"
        
        command = f"# Rename the mapping file\nmv {old_path} {new_path}"
        
        return {
            'issue': f"Incorrect mapping file name: {framework.language}/{framework.name}/{framework.mapping_file_name}",
            'suggestion': f"Rename to: 9999_Framework_Mapping.md",
            'command': command,
            'old_path': str(old_path),
            'new_path': str(new_path)
        }
    
    def suggest_missing_version_history(self, template: TemplateFile) -> Dict[str, str]:
        """
        Generate suggestion for adding version history to a template.
        
        Args:
            template: TemplateFile object missing version history
            
        Returns:
            Dictionary with suggestion details
        """
        # Determine language for section header
        if template.language == 'de':
            section_header = "## Versionshistorie"
        else:
            section_header = "## Version History"
        
        version_history_template = f"""
{section_header}

| Version | Datum / Date | Autor / Author | Änderungen / Changes |
|---------|--------------|----------------|----------------------|
| 1.0.0   | YYYY-MM-DD   | [Author]       | Initiale Version / Initial version |
"""
        
        suggestion = f"""Add the following version history section to the end of the template file:

{version_history_template}

Steps:
1. Open the file: {template.path}
2. Scroll to the end of the file
3. Add the version history section above
4. Update the date and author information
5. Save the file
"""
        
        command = f"""# Append version history to template
cat >> {template.path} << 'EOF'
{version_history_template}
EOF"""
        
        return {
            'issue': f"Missing version history: {template.framework}/{template.path.name}",
            'suggestion': suggestion,
            'command': command,
            'template': version_history_template,
            'file_path': str(template.path)
        }
    
    def suggest_missing_translation(self, framework: Framework, missing_language: str) -> Dict[str, str]:
        """
        Generate suggestion for creating missing translations.
        
        Args:
            framework: Framework object with translation discrepancy
            missing_language: Language code that is missing ('de' or 'en')
            
        Returns:
            Dictionary with suggestion details
        """
        if missing_language == 'de':
            source_path = framework.path_en
            target_path = framework.path_de
            source_lang = "English"
            target_lang = "German"
        else:
            source_path = framework.path_de
            target_path = framework.path_en
            source_lang = "German"
            target_lang = "English"
        
        suggestion = f"""Translation discrepancy detected for framework: {framework.name}

Source ({source_lang}): {framework.template_count_de if missing_language == 'en' else framework.template_count_en} templates
Target ({target_lang}): {framework.template_count_en if missing_language == 'en' else framework.template_count_de} templates

Steps to resolve:
1. Identify which templates are missing in {target_lang}
2. Translate the missing templates from {source_lang} to {target_lang}
3. Ensure template filenames match between languages
4. Verify all metadata is translated appropriately

Command to compare directories:
  diff -r {source_path} {target_path}

Command to list files in each directory:
  ls -1 {source_path}
  ls -1 {target_path}
"""
        
        command = f"# Compare template files between languages\ndiff -r {source_path} {target_path}"
        
        return {
            'issue': f"Translation discrepancy: {framework.name} ({source_lang} → {target_lang})",
            'suggestion': suggestion,
            'command': command,
            'source_path': str(source_path),
            'target_path': str(target_path),
            'missing_language': missing_language
        }
    
    def generate_batch_remediation_script(
        self,
        mapping_issues: List[FrameworkInfo],
        version_issues: List[TemplateFile],
        translation_issues: List[tuple]
    ) -> str:
        """
        Generate a batch script for remediating multiple issues.
        
        Args:
            mapping_issues: List of frameworks with mapping file issues
            version_issues: List of templates with version history issues
            translation_issues: List of (framework, language) tuples with translation issues
            
        Returns:
            Shell script as a string
        """
        script_lines = [
            "#!/bin/bash",
            "#",
            "# Batch Remediation Script",
            "# Generated by Quality Control System",
            "#",
            "# This script addresses multiple quality control issues.",
            "# Review each section before executing.",
            "#",
            "",
            "set -e  # Exit on error",
            "",
        ]
        
        # Section 1: Create missing mapping files
        if mapping_issues:
            script_lines.extend([
                "echo '=== Creating Missing Mapping Files ==='",
                ""
            ])
            
            for framework in mapping_issues:
                if not framework.has_mapping_file:
                    suggestion = self.suggest_missing_mapping_file(framework)
                    script_lines.extend([
                        f"# {framework.language}/{framework.name}",
                        f"echo 'Creating mapping file for {framework.name}...'",
                        suggestion['command'],
                        ""
                    ])
                elif framework.mapping_file_name != "9999_Framework_Mapping.md":
                    suggestion = self.suggest_incorrect_mapping_filename(framework)
                    script_lines.extend([
                        f"# {framework.language}/{framework.name}",
                        f"echo 'Renaming mapping file for {framework.name}...'",
                        suggestion['command'],
                        ""
                    ])
        
        # Section 2: Add version history to templates
        if version_issues:
            script_lines.extend([
                "echo '=== Adding Version History to Templates ==='",
                ""
            ])
            
            # Limit to first 10 to avoid overly long scripts
            for template in version_issues[:10]:
                suggestion = self.suggest_missing_version_history(template)
                script_lines.extend([
                    f"# {template.framework}/{template.path.name}",
                    f"echo 'Adding version history to {template.path.name}...'",
                    suggestion['command'],
                    ""
                ])
            
            if len(version_issues) > 10:
                script_lines.extend([
                    f"# ... and {len(version_issues) - 10} more templates",
                    f"# Run quality control again to get suggestions for remaining templates",
                    ""
                ])
        
        # Section 3: Translation issues (informational only)
        if translation_issues:
            script_lines.extend([
                "echo '=== Translation Issues (Manual Review Required) ==='",
                ""
            ])
            
            for framework, language in translation_issues:
                script_lines.extend([
                    f"echo 'Translation discrepancy: {framework.name} (missing {language})'",
                    f"# Manual translation required - see detailed suggestions",
                    ""
                ])
        
        script_lines.extend([
            "echo '=== Batch Remediation Complete ==='",
            "echo 'Run quality control again to verify fixes'",
            ""
        ])
        
        return "\n".join(script_lines)
    
    def generate_remediation_report(
        self,
        mapping_validation: ValidationResult,
        version_validation: VersionHistoryValidationResult,
        frameworks: List[Framework]
    ) -> str:
        """
        Generate a comprehensive remediation report with all suggestions.
        
        Args:
            mapping_validation: Framework mapping validation result
            version_validation: Version history validation result
            frameworks: List of discovered frameworks
            
        Returns:
            Formatted remediation report as a string
        """
        lines = []
        
        lines.append("=" * 80)
        lines.append("REMEDIATION SUGGESTIONS")
        lines.append("=" * 80)
        lines.append("")
        
        # Section 1: Framework Mapping Issues
        if not mapping_validation.success:
            lines.append("-" * 80)
            lines.append("1. FRAMEWORK MAPPING FILE ISSUES")
            lines.append("-" * 80)
            lines.append("")
            
            # Missing files
            if mapping_validation.missing_files:
                lines.append(f"Missing Mapping Files: {len(mapping_validation.missing_files)}")
                lines.append("")
                
                for framework in mapping_validation.missing_files[:3]:
                    suggestion = self.suggest_missing_mapping_file(framework)
                    lines.append(f"Issue: {suggestion['issue']}")
                    lines.append(f"Suggestion: {suggestion['suggestion']}")
                    lines.append("")
                    lines.append("Command:")
                    lines.append(f"  touch {suggestion['file_path']}")
                    lines.append("  # Then add the template content")
                    lines.append("")
                
                if len(mapping_validation.missing_files) > 3:
                    lines.append(f"... and {len(mapping_validation.missing_files) - 3} more")
                    lines.append("")
            
            # Incorrect names
            if mapping_validation.invalid_frameworks:
                lines.append(f"Incorrectly Named Mapping Files: {len(mapping_validation.invalid_frameworks)}")
                lines.append("")
                
                for framework in mapping_validation.invalid_frameworks[:3]:
                    suggestion = self.suggest_incorrect_mapping_filename(framework)
                    lines.append(f"Issue: {suggestion['issue']}")
                    lines.append(f"Suggestion: {suggestion['suggestion']}")
                    lines.append("")
                    lines.append("Command:")
                    lines.append(f"  {suggestion['command']}")
                    lines.append("")
                
                if len(mapping_validation.invalid_frameworks) > 3:
                    lines.append(f"... and {len(mapping_validation.invalid_frameworks) - 3} more")
                    lines.append("")
        
        # Section 2: Version History Issues
        if not version_validation.success:
            lines.append("-" * 80)
            lines.append("2. VERSION HISTORY ISSUES")
            lines.append("-" * 80)
            lines.append("")
            
            if version_validation.missing_version_history:
                lines.append(f"Templates Missing Version History: {len(version_validation.missing_version_history)}")
                lines.append("")
                
                for template in version_validation.missing_version_history[:3]:
                    suggestion = self.suggest_missing_version_history(template)
                    lines.append(f"Issue: {suggestion['issue']}")
                    lines.append(f"File: {suggestion['file_path']}")
                    lines.append("")
                    lines.append("Add this section to the end of the file:")
                    lines.append(suggestion['template'])
                    lines.append("")
                
                if len(version_validation.missing_version_history) > 3:
                    lines.append(f"... and {len(version_validation.missing_version_history) - 3} more")
                    lines.append("")
        
        # Section 3: Translation Issues
        inconsistent_frameworks = [f for f in frameworks if not f.bilingual_consistent]
        if inconsistent_frameworks:
            lines.append("-" * 80)
            lines.append("3. TRANSLATION CONSISTENCY ISSUES")
            lines.append("-" * 80)
            lines.append("")
            lines.append(f"Frameworks with Translation Discrepancies: {len(inconsistent_frameworks)}")
            lines.append("")
            
            for framework in inconsistent_frameworks[:3]:
                # Determine which language is missing templates
                if framework.template_count_de > framework.template_count_en:
                    missing_lang = 'en'
                else:
                    missing_lang = 'de'
                
                suggestion = self.suggest_missing_translation(framework, missing_lang)
                lines.append(f"Framework: {framework.name}")
                lines.append(f"  DE templates: {framework.template_count_de}")
                lines.append(f"  EN templates: {framework.template_count_en}")
                lines.append(f"  Difference: {abs(framework.template_count_de - framework.template_count_en)}")
                lines.append("")
                lines.append("Command to compare:")
                lines.append(f"  {suggestion['command']}")
                lines.append("")
            
            if len(inconsistent_frameworks) > 3:
                lines.append(f"... and {len(inconsistent_frameworks) - 3} more")
                lines.append("")
        
        # Section 4: Batch Remediation
        lines.append("-" * 80)
        lines.append("4. BATCH REMEDIATION")
        lines.append("-" * 80)
        lines.append("")
        
        if not mapping_validation.success or not version_validation.success:
            lines.append("A batch remediation script can be generated to fix multiple issues at once.")
            lines.append("")
            lines.append("To generate the script:")
            lines.append("  python quality_control.py --generate-remediation-script")
            lines.append("")
            lines.append("Review the script before executing to ensure it matches your needs.")
        else:
            lines.append("✓ No batch remediation needed - all checks passed!")
        
        lines.append("")
        lines.append("=" * 80)
        
        return "\n".join(lines)
    
    def save_remediation_script(
        self,
        mapping_validation: ValidationResult,
        version_validation: VersionHistoryValidationResult,
        frameworks: List[Framework],
        output_path: str
    ) -> None:
        """
        Save a batch remediation script to a file.
        
        Args:
            mapping_validation: Framework mapping validation result
            version_validation: Version history validation result
            frameworks: List of discovered frameworks
            output_path: Path where to save the script
        """
        # Collect issues
        mapping_issues = (
            mapping_validation.missing_files +
            mapping_validation.invalid_frameworks
        )
        
        version_issues = version_validation.missing_version_history
        
        translation_issues = [
            (f, 'en' if f.template_count_de > f.template_count_en else 'de')
            for f in frameworks if not f.bilingual_consistent
        ]
        
        # Generate script
        script = self.generate_batch_remediation_script(
            mapping_issues,
            version_issues,
            translation_issues
        )
        
        # Save to file
        try:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(script)
            
            # Make script executable on Unix systems
            try:
                import stat
                output_file.chmod(output_file.stat().st_mode | stat.S_IEXEC)
            except Exception:
                pass  # Ignore on Windows
            
            self.logger.info(f"Remediation script saved to: {output_path}")
            print(f"\n✓ Remediation script saved to: {output_path}")
            print("  Review the script before executing.")
            print(f"  Execute with: bash {output_path}")
        
        except Exception as e:
            self.logger.error(f"Failed to save remediation script: {e}")
            print(f"\n✗ Failed to save remediation script: {e}")
