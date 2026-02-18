#!/usr/bin/env python3
"""
Metadata Validation Script for Handbook Generator

Command-line tool for validating metadata across all compliance framework templates.
Validates required fields, template version format, revision numbers, bilingual
consistency, and placeholder syntax.

Usage:
    python helpers/validate_metadata.py --all
    python helpers/validate_metadata.py --framework gdpr
    python helpers/validate_metadata.py --language de
    python helpers/validate_metadata.py --report output.json

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataStandardizer, ValidationResult


@dataclass
class ValidationError:
    """
    Detailed validation error information.
    
    Attributes:
        framework: Framework name
        language: Language code
        filepath: Path to metadata file
        error_type: Type of error (missing_field, invalid_format, etc.)
        description: Human-readable error description
    """
    framework: str
    language: str
    filepath: str
    error_type: str
    description: str


@dataclass
class ValidationReport:
    """
    Complete validation report.
    
    Attributes:
        total_frameworks: Total number of frameworks checked
        total_files: Total number of metadata files checked
        valid_files: Number of files that passed validation
        invalid_files: Number of files that failed validation
        errors: List of validation errors
        warnings: List of validation warnings
        success_rate: Percentage of valid files
    """
    total_frameworks: int
    total_files: int
    valid_files: int
    invalid_files: int
    errors: List[ValidationError]
    warnings: List[str]
    success_rate: float


class MetadataValidator:
    """
    Validates metadata files across all frameworks.
    
    Provides comprehensive validation including:
    - Required fields check
    - Template version format validation
    - Revision number validation
    - Placeholder syntax validation
    - Bilingual consistency check
    """
    
    # Pattern for valid placeholders: {{ source.field }}
    PLACEHOLDER_PATTERN = r'\{\{\s*\w+\.\w+\s*\}\}'
    
    def __init__(self, templates_dir: str = 'templates'):
        """
        Initialize validator with templates directory.
        
        Args:
            templates_dir: Path to templates directory
        """
        self.standardizer = MetadataStandardizer(templates_dir)
        self.templates_dir = Path(templates_dir)
    
    def validate_all(self) -> ValidationReport:
        """
        Validate all frameworks.
        
        Returns:
            ValidationReport with complete validation results
        """
        frameworks = self.standardizer._discover_frameworks()
        return self._validate_frameworks(frameworks)
    
    def validate_framework(self, framework: str) -> ValidationReport:
        """
        Validate single framework.
        
        Args:
            framework: Framework name
        
        Returns:
            ValidationReport for the framework
        """
        return self._validate_frameworks({framework})
    
    def validate_language(self, language: str) -> ValidationReport:
        """
        Validate all frameworks for specific language.
        
        Args:
            language: Language code ('de' or 'en')
        
        Returns:
            ValidationReport for the language
        """
        frameworks = self.standardizer._discover_frameworks()
        return self._validate_frameworks(frameworks, language_filter=language)
    
    def validate_placeholder_syntax(self, content: str) -> List[str]:
        """
        Validate placeholder syntax in metadata content.
        
        Checks that all placeholders follow the format {{ source.field }}.
        
        Args:
            content: Metadata file content
        
        Returns:
            List of malformed placeholders found
        """
        import re
        
        malformed = []
        
        # Find all potential placeholders (anything between {{ and }})
        potential_placeholders = re.findall(r'\{\{[^}]*\}\}', content)
        
        for placeholder in potential_placeholders:
            # Check if it matches the valid pattern
            if not re.match(self.PLACEHOLDER_PATTERN, placeholder):
                malformed.append(placeholder)
        
        return malformed
    
    def check_bilingual_consistency(
        self,
        framework: str
    ) -> List[str]:
        """
        Check consistency between DE and EN metadata files.
        
        Verifies:
        - Both files exist
        - Matching field structure
        - Placeholder consistency
        
        Args:
            framework: Framework name
        
        Returns:
            List of inconsistency descriptions
        """
        import re
        
        inconsistencies = []
        
        de_path = self.standardizer._get_metadata_path(framework, 'de')
        en_path = self.standardizer._get_metadata_path(framework, 'en')
        
        # Check if both files exist
        if not de_path.exists():
            inconsistencies.append('German metadata file missing')
            return inconsistencies
        
        if not en_path.exists():
            inconsistencies.append('English metadata file missing')
            return inconsistencies
        
        # Read both files
        try:
            de_content = de_path.read_text(encoding='utf-8')
            en_content = en_path.read_text(encoding='utf-8')
        except Exception as e:
            inconsistencies.append(f'Could not read files: {e}')
            return inconsistencies
        
        # Extract fields from both files
        de_fields = self._extract_fields(de_content)
        en_fields = self._extract_fields(en_content)
        
        # Compare field sets
        de_field_names = set(de_fields.keys())
        en_field_names = set(en_fields.keys())
        
        # Check for missing fields
        missing_in_en = de_field_names - en_field_names
        missing_in_de = en_field_names - de_field_names
        
        if missing_in_en:
            inconsistencies.append(
                f'Fields in DE but not in EN: {", ".join(sorted(missing_in_en))}'
            )
        
        if missing_in_de:
            inconsistencies.append(
                f'Fields in EN but not in DE: {", ".join(sorted(missing_in_de))}'
            )
        
        # Extract placeholders from both files
        de_placeholders = set(re.findall(r'\{\{\s*\w+\.\w+\s*\}\}', de_content))
        en_placeholders = set(re.findall(r'\{\{\s*\w+\.\w+\s*\}\}', en_content))
        
        # Compare placeholders
        if de_placeholders != en_placeholders:
            missing_in_en_ph = de_placeholders - en_placeholders
            missing_in_de_ph = en_placeholders - de_placeholders
            
            if missing_in_en_ph:
                inconsistencies.append(
                    f'Placeholders in DE but not in EN: {", ".join(sorted(missing_in_en_ph))}'
                )
            
            if missing_in_de_ph:
                inconsistencies.append(
                    f'Placeholders in EN but not in DE: {", ".join(sorted(missing_in_de_ph))}'
                )
        
        # Check section structure
        de_sections = self._extract_sections(de_content)
        en_sections = self._extract_sections(en_content)
        
        if len(de_sections) != len(en_sections):
            inconsistencies.append(
                f'Different number of sections: DE has {len(de_sections)}, EN has {len(en_sections)}'
            )
        
        return inconsistencies
    
    def _extract_fields(self, content: str) -> Dict[str, str]:
        """
        Extract field names and values from metadata content.
        
        Args:
            content: Metadata file content
        
        Returns:
            Dictionary mapping field names to values
        """
        import re
        
        fields = {}
        
        # Pattern for markdown bold fields: **Label:** value
        pattern = r'\*\*([^*]+):\*\*\s*(.+?)(?:\n|$)'
        matches = re.findall(pattern, content)
        
        for label, value in matches:
            # Normalize field name (remove language-specific variations)
            normalized = self._normalize_field_name(label.strip())
            fields[normalized] = value.strip()
        
        return fields
    
    def _normalize_field_name(self, label: str) -> str:
        """
        Normalize field label to language-independent name.
        
        Args:
            label: Field label (German or English)
        
        Returns:
            Normalized field name
        """
        # Map of labels to normalized names
        label_map = {
            'Dokument-ID': 'document_id',
            'Document-ID': 'document_id',
            'Document ID': 'document_id',
            'Owner': 'owner',
            'Version': 'version',
            'Status': 'status',
            'Klassifizierung': 'classification',
            'Classification': 'classification',
            'Letzte Aktualisierung': 'date',
            'Last Updated': 'date',
            'Template-Version': 'template_version',
            'Template Version': 'template_version',
            'Revision': 'revision',
            'Handbuch-Titel': 'handbook_title',
            'Handbook Title': 'handbook_title',
            'Organisation': 'organization',
            'Organization': 'organization',
            'Autor': 'author',
            'Author': 'author',
            'Geltungsbereich': 'scope',
            'Scope': 'scope',
            'Gültig ab': 'valid_from',
            'Valid from': 'valid_from',
            'Nächste Überprüfung': 'next_review',
            'Next Review': 'next_review',
        }
        
        return label_map.get(label, label.lower().replace(' ', '_'))
    
    def _extract_sections(self, content: str) -> List[str]:
        """
        Extract section headers from metadata content.
        
        Args:
            content: Metadata file content
        
        Returns:
            List of section headers
        """
        import re
        
        # Pattern for markdown headers: ## Header
        pattern = r'^##\s+(.+)$'
        sections = re.findall(pattern, content, re.MULTILINE)
        
        return sections
    
    def _validate_frameworks(
        self,
        frameworks: Set[str],
        language_filter: Optional[str] = None
    ) -> ValidationReport:
        """
        Validate specified frameworks.
        
        Args:
            frameworks: Set of framework names to validate
            language_filter: Optional language filter ('de' or 'en')
        
        Returns:
            ValidationReport with validation results
        """
        errors = []
        warnings = []
        total_files = 0
        valid_files = 0
        invalid_files = 0
        
        languages = [language_filter] if language_filter else ['de', 'en']
        
        for framework in sorted(frameworks):
            # Check bilingual consistency (only if validating both languages)
            if not language_filter:
                inconsistencies = self.check_bilingual_consistency(framework)
                if inconsistencies:
                    for inconsistency in inconsistencies:
                        errors.append(ValidationError(
                            framework=framework,
                            language='de/en',
                            filepath=f'templates/{{de,en}}/{framework}/0000_metadata_*',
                            error_type='bilingual_inconsistency',
                            description=inconsistency
                        ))
            
            for language in languages:
                metadata_path = self.standardizer._get_metadata_path(framework, language)
                
                if not metadata_path.exists():
                    errors.append(ValidationError(
                        framework=framework,
                        language=language,
                        filepath=str(metadata_path),
                        error_type='missing_file',
                        description=f'Metadata file does not exist'
                    ))
                    total_files += 1
                    invalid_files += 1
                    continue
                
                total_files += 1
                
                # Read file content for additional checks
                try:
                    content = metadata_path.read_text(encoding='utf-8')
                except Exception as e:
                    errors.append(ValidationError(
                        framework=framework,
                        language=language,
                        filepath=str(metadata_path),
                        error_type='read_error',
                        description=f'Could not read file: {e}'
                    ))
                    invalid_files += 1
                    continue
                
                # Validate metadata structure
                validation = self.standardizer.validate_metadata_structure(str(metadata_path))
                
                # Validate placeholder syntax
                malformed_placeholders = self.validate_placeholder_syntax(content)
                
                # Determine if file is valid
                is_valid = validation.is_valid and len(malformed_placeholders) == 0
                
                if is_valid:
                    valid_files += 1
                else:
                    invalid_files += 1
                    
                    # Add errors for missing fields
                    for field in validation.missing_fields:
                        errors.append(ValidationError(
                            framework=framework,
                            language=language,
                            filepath=str(metadata_path),
                            error_type='missing_field',
                            description=f'Missing required field: {field}'
                        ))
                    
                    # Add errors for invalid fields
                    for field_desc in validation.invalid_fields:
                        errors.append(ValidationError(
                            framework=framework,
                            language=language,
                            filepath=str(metadata_path),
                            error_type='invalid_field',
                            description=f'Invalid field: {field_desc}'
                        ))
                    
                    # Add errors for malformed placeholders
                    for placeholder in malformed_placeholders:
                        errors.append(ValidationError(
                            framework=framework,
                            language=language,
                            filepath=str(metadata_path),
                            error_type='invalid_placeholder',
                            description=f'Malformed placeholder: {placeholder}'
                        ))
                
                # Add warnings
                for warning in validation.warnings:
                    warnings.append(f'{framework} ({language}): {warning}')
        
        # Calculate success rate
        success_rate = (valid_files / total_files * 100) if total_files > 0 else 0.0
        
        return ValidationReport(
            total_frameworks=len(frameworks),
            total_files=total_files,
            valid_files=valid_files,
            invalid_files=invalid_files,
            errors=errors,
            warnings=warnings,
            success_rate=success_rate
        )


def main():
    """Main entry point for validation script."""
    parser = argparse.ArgumentParser(
        description='Validate metadata files across compliance framework templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --all                    Validate all frameworks
  %(prog)s --framework gdpr         Validate GDPR framework only
  %(prog)s --language de            Validate all German metadata files
  %(prog)s --all --report out.json  Validate all and save JSON report
        """
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Validate all frameworks'
    )
    
    parser.add_argument(
        '--framework',
        type=str,
        help='Validate specific framework (e.g., gdpr, iso-9001)'
    )
    
    parser.add_argument(
        '--language',
        type=str,
        choices=['de', 'en'],
        help='Validate specific language only'
    )
    
    parser.add_argument(
        '--report',
        type=str,
        help='Output JSON report to file'
    )
    
    parser.add_argument(
        '--templates-dir',
        type=str,
        default='templates',
        help='Path to templates directory (default: templates)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not (args.all or args.framework or args.language):
        parser.error('Must specify --all, --framework, or --language')
    
    if args.framework and args.all:
        parser.error('Cannot specify both --framework and --all')
    
    # Create validator
    validator = MetadataValidator(args.templates_dir)
    
    # Run validation
    if args.all:
        print('Validating all frameworks...')
        report = validator.validate_all()
    elif args.framework:
        print(f'Validating framework: {args.framework}')
        report = validator.validate_framework(args.framework)
    elif args.language:
        print(f'Validating language: {args.language}')
        report = validator.validate_language(args.language)
    
    # Print results
    print_report(report)
    
    # Save JSON report if requested
    if args.report:
        save_json_report(report, args.report)
        print(f'\nJSON report saved to: {args.report}')
    
    # Exit with error code if validation failed
    sys.exit(0 if report.invalid_files == 0 else 1)


def print_report(report: ValidationReport):
    """
    Print validation report to console.
    
    Args:
        report: ValidationReport to print
    """
    print('\n' + '=' * 70)
    print('METADATA VALIDATION REPORT')
    print('=' * 70)
    print(f'\nFrameworks checked: {report.total_frameworks}')
    print(f'Total files checked: {report.total_files}')
    print(f'Valid files: {report.valid_files}')
    print(f'Invalid files: {report.invalid_files}')
    print(f'Success rate: {report.success_rate:.1f}%')
    
    if report.errors:
        print(f'\n{len(report.errors)} ERRORS FOUND:')
        print('-' * 70)
        
        # Group errors by framework
        errors_by_framework = {}
        for error in report.errors:
            key = f'{error.framework} ({error.language})'
            if key not in errors_by_framework:
                errors_by_framework[key] = []
            errors_by_framework[key].append(error)
        
        for framework_key in sorted(errors_by_framework.keys()):
            print(f'\n{framework_key}:')
            for error in errors_by_framework[framework_key]:
                print(f'  [{error.error_type}] {error.description}')
                print(f'    File: {error.filepath}')
    
    if report.warnings:
        print(f'\n{len(report.warnings)} WARNINGS:')
        print('-' * 70)
        for warning in report.warnings:
            print(f'  {warning}')
    
    if report.invalid_files == 0:
        print('\n✓ All metadata files are valid!')
    else:
        print(f'\n✗ {report.invalid_files} file(s) failed validation')
    
    print('=' * 70)


def save_json_report(report: ValidationReport, filepath: str):
    """
    Save validation report as JSON.
    
    Args:
        report: ValidationReport to save
        filepath: Output file path
    """
    # Convert report to dict
    report_dict = {
        'total_frameworks': report.total_frameworks,
        'total_files': report.total_files,
        'valid_files': report.valid_files,
        'invalid_files': report.invalid_files,
        'success_rate': report.success_rate,
        'errors': [asdict(error) for error in report.errors],
        'warnings': report.warnings
    }
    
    # Write JSON file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(report_dict, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
