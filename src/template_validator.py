"""
Template Validator

Validates IT-Operations templates for quality and compliance.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of template validation."""
    is_valid: bool
    warnings: List[str]
    errors: List[str]
    
    def add_warning(self, message: str) -> None:
        """Add a warning message."""
        self.warnings.append(message)
        
    def add_error(self, message: str) -> None:
        """Add an error message."""
        self.errors.append(message)
        self.is_valid = False


class TemplateValidator:
    """Validates IT-Operations templates for quality and compliance."""
    
    # Valid RACI values
    VALID_RACI_VALUES = {'R', 'A', 'C', 'I', 'N/A', 'n/a', '-', ''}
    
    # IT Framework keywords - must be explicit framework references
    ITIL_KEYWORDS = [
        'ITIL v4', 'ITIL V4', 'ITIL 4', 'ITIL Foundation',
        'ITIL Practice', 'ITIL Service', 'ITIL Framework',
        'follows ITIL', 'based on ITIL', 'according to ITIL',
        'ITIL best practice', 'ITIL standard'
    ]
    
    ISO20000_KEYWORDS = [
        'ISO 20000', 'ISO/IEC 20000', 'ISO-20000', 'ISO20000',
        'Service Management System', 'SMS',
        'Clause 8.', 'ISO 20000-1', 'ISO 20000-2',
        'ISO standard', 'ISO certification'
    ]
    
    COBIT_KEYWORDS = [
        'COBIT 2019', 'COBIT 5', 'COBIT Framework',
        'APO01', 'APO02', 'APO07', 'APO09', 'APO12', 'APO13',
        'BAI03', 'BAI06', 'BAI10',
        'DSS01', 'DSS02', 'DSS03', 'DSS04', 'DSS05', 'DSS06',
        'MEA01', 'MEA02', 'MEA03',
        'COBIT objective', 'COBIT domain'
    ]
    
    def __init__(self):
        """Initialize template validator."""
        pass
    
    def validate_template(self, template_path: Path) -> ValidationResult:
        """
        Validate a single template file.
        
        Args:
            template_path: Path to template file
            
        Returns:
            ValidationResult with validation status and messages
        """
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        
        if not template_path.exists():
            result.add_error(f"Template file not found: {template_path}")
            return result
        
        try:
            content = template_path.read_text(encoding='utf-8')
        except Exception as e:
            result.add_error(f"Failed to read template: {e}")
            return result
        
        # Validate RACI matrices
        self._validate_raci_matrices(content, template_path.name, result)
        
        # Validate placeholder syntax
        self._validate_placeholder_syntax(content, template_path.name, result)
        
        # Validate framework references
        self._validate_framework_references(content, template_path.name, result)
        
        return result
    
    def _validate_raci_matrices(
        self,
        content: str,
        filename: str,
        result: ValidationResult
    ) -> None:
        """
        Validate RACI matrices in template content.
        
        Args:
            content: Template content
            filename: Template filename
            result: ValidationResult to update
        """
        # Find all tables that might be RACI matrices
        # Look for tables with RACI-like headers
        raci_pattern = re.compile(
            r'\|[^\n]*\|[^\n]*\n\|[-:\s|]+\n((?:\|[^\n]*\n)+)',
            re.MULTILINE
        )
        
        tables = raci_pattern.findall(content)
        
        if not tables:
            # No tables found - this is OK, not all templates need RACI matrices
            return
        
        # Check if any table looks like a RACI matrix
        # (has columns with role names and rows with activities)
        for table_content in tables:
            rows = table_content.strip().split('\n')
            
            # Check if this looks like a RACI matrix
            # (has cells with R, A, C, I values)
            is_raci_matrix = False
            for row in rows:
                cells = [cell.strip() for cell in row.split('|')[1:-1]]
                for cell in cells:
                    if cell.upper() in {'R', 'A', 'C', 'I'}:
                        is_raci_matrix = True
                        break
                if is_raci_matrix:
                    break
            
            if is_raci_matrix:
                # Validate this RACI matrix
                self._validate_raci_matrix_completeness(
                    table_content,
                    filename,
                    result
                )
    
    def _validate_raci_matrix_completeness(
        self,
        table_content: str,
        filename: str,
        result: ValidationResult
    ) -> None:
        """
        Validate that a RACI matrix is complete.
        
        Args:
            table_content: RACI matrix table content
            filename: Template filename
            result: ValidationResult to update
        """
        rows = table_content.strip().split('\n')
        
        incomplete_cells = []
        
        for row_idx, row in enumerate(rows):
            cells = [cell.strip() for cell in row.split('|')[1:-1]]
            
            # Skip first cell (activity name)
            for cell_idx, cell in enumerate(cells[1:], start=1):
                # Check if cell is empty
                if not cell:
                    incomplete_cells.append((row_idx + 1, cell_idx + 1))
                    continue
                
                # Check if it's a valid RACI value (case-insensitive)
                cell_upper = cell.upper()
                if cell_upper not in {'R', 'A', 'C', 'I', 'N/A', '-'}:
                    incomplete_cells.append((row_idx + 1, cell_idx + 1))
        
        if incomplete_cells:
            result.add_warning(
                f"RACI matrix in {filename} has incomplete or invalid cells at positions: "
                f"{incomplete_cells}. All cells should contain R, A, C, I, or N/A."
            )
    
    def _validate_placeholder_syntax(
        self,
        content: str,
        filename: str,
        result: ValidationResult
    ) -> None:
        """
        Validate placeholder syntax in template content.
        
        Args:
            content: Template content
            filename: Template filename
            result: ValidationResult to update
        """
        # Find all potential placeholders
        placeholder_pattern = re.compile(r'\{\{[^}]*\}\}')
        placeholders = placeholder_pattern.findall(content)
        
        for placeholder in placeholders:
            # Valid placeholder format: {{ source.field }}
            # where source is 'meta' or 'netbox'
            valid_pattern = re.compile(r'^\{\{\s*(meta|netbox)\.[a-zA-Z0-9_.]+\s*\}\}$')
            
            if not valid_pattern.match(placeholder):
                result.add_warning(
                    f"Invalid placeholder syntax in {filename}: '{placeholder}'. "
                    f"Expected format: {{{{ meta.field }}}} or {{{{ netbox.field }}}}"
                )
    
    def _validate_framework_references(
        self,
        content: str,
        filename: str,
        result: ValidationResult
    ) -> None:
        """
        Validate that template references relevant IT frameworks.
        
        Args:
            content: Template content
            filename: Template filename
            result: ValidationResult to update
        """
        # Check if template references any IT frameworks
        has_itil = any(keyword in content for keyword in self.ITIL_KEYWORDS)
        has_iso20000 = any(keyword in content for keyword in self.ISO20000_KEYWORDS)
        has_cobit = any(keyword in content for keyword in self.COBIT_KEYWORDS)
        
        has_any_framework = has_itil or has_iso20000 or has_cobit
        
        # Only warn for content templates (not metadata templates)
        if not filename.startswith('0000_') and not has_any_framework:
            # Check if this is a template that should have framework references
            # (operational templates like incident, change, monitoring, etc.)
            operational_keywords = [
                'incident', 'problem', 'change', 'monitoring', 'backup',
                'disaster', 'security', 'compliance', 'capacity', 'availability'
            ]
            
            is_operational_template = any(
                keyword in filename.lower() for keyword in operational_keywords
            )
            
            if is_operational_template:
                result.add_warning(
                    f"Template {filename} does not reference any IT frameworks "
                    f"(ITIL, ISO 20000, COBIT). Consider adding framework references "
                    f"for compliance and best practice alignment."
                )
    
    def validate_template_directory(
        self,
        templates_dir: Path
    ) -> Dict[str, ValidationResult]:
        """
        Validate all templates in a directory.
        
        Args:
            templates_dir: Path to templates directory
            
        Returns:
            Dictionary mapping template filenames to ValidationResults
        """
        results = {}
        
        if not templates_dir.exists():
            return results
        
        for template_file in templates_dir.glob('*.md'):
            result = self.validate_template(template_file)
            results[template_file.name] = result
        
        return results
    
    def print_validation_summary(
        self,
        results: Dict[str, ValidationResult]
    ) -> None:
        """
        Print validation summary.
        
        Args:
            results: Dictionary of validation results
        """
        total_templates = len(results)
        valid_templates = sum(1 for r in results.values() if r.is_valid)
        total_warnings = sum(len(r.warnings) for r in results.values())
        total_errors = sum(len(r.errors) for r in results.values())
        
        print(f"\n=== Template Validation Summary ===")
        print(f"Total templates: {total_templates}")
        print(f"Valid templates: {valid_templates}")
        print(f"Templates with warnings: {total_templates - valid_templates}")
        print(f"Total warnings: {total_warnings}")
        print(f"Total errors: {total_errors}")
        
        if total_errors > 0:
            print(f"\n=== Errors ===")
            for filename, result in results.items():
                if result.errors:
                    print(f"\n{filename}:")
                    for error in result.errors:
                        print(f"  ERROR: {error}")
        
        if total_warnings > 0:
            print(f"\n=== Warnings ===")
            for filename, result in results.items():
                if result.warnings:
                    print(f"\n{filename}:")
                    for warning in result.warnings:
                        print(f"  WARNING: {warning}")


def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validate IT-Operations templates'
    )
    parser.add_argument(
        'template_dir',
        type=str,
        help='Path to templates directory'
    )
    parser.add_argument(
        '--language',
        type=str,
        choices=['de', 'en'],
        default='de',
        help='Template language (default: de)'
    )
    
    args = parser.parse_args()
    
    templates_dir = Path(args.template_dir)
    
    if not templates_dir.exists():
        print(f"Error: Template directory not found: {templates_dir}")
        return 1
    
    validator = TemplateValidator()
    results = validator.validate_template_directory(templates_dir)
    validator.print_validation_summary(results)
    
    # Return non-zero exit code if there are errors
    has_errors = any(not r.is_valid for r in results.values())
    return 1 if has_errors else 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
