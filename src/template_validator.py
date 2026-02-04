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
    """Validates templates for quality and compliance across multiple template types."""
    
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
    
    # BCM Framework keywords
    ISO22301_KEYWORDS = [
        'ISO 22301', 'ISO/IEC 22301', 'ISO-22301', 'ISO22301',
        'Business Continuity Management', 'BCM',
        'Clause 4.', 'Clause 5.', 'Clause 6.', 'Clause 7.', 'Clause 8.', 'Clause 9.', 'Clause 10.',
        'ISO 22301:2019', 'ISO 22301:2012',
        'BCM standard', 'BCM framework'
    ]
    
    BSI_BCM_KEYWORDS = [
        'BSI Standard 100-4', 'BSI 100-4', 'BSI-Standard 100-4',
        'BSI BCM', 'BSI Business Continuity',
        'Notfallmanagement', 'Emergency Management',
        'BSI-Standard', 'BSI Grundschutz BCM'
    ]
    
    # ISMS Framework keywords
    ISO27001_KEYWORDS = [
        'ISO 27001', 'ISO/IEC 27001', 'ISO-27001', 'ISO27001',
        'ISO 27001:2022', 'ISO 27001:2013',
        'Amendment 1:2024', 'Amendment 1',
        'Information Security Management System', 'ISMS',
        'Clause 4.', 'Clause 5.', 'Clause 6.', 'Clause 7.', 'Clause 8.', 'Clause 9.', 'Clause 10.',
        'Annex A', 'Control A.', 'ISO 27001 control'
    ]
    
    # BSI Grundschutz Framework keywords
    BSI_GRUNDSCHUTZ_KEYWORDS = [
        'BSI Standard 200-1', 'BSI 200-1', 'BSI-Standard 200-1',
        'BSI Standard 200-2', 'BSI 200-2', 'BSI-Standard 200-2',
        'BSI Standard 200-3', 'BSI 200-3', 'BSI-Standard 200-3',
        'BSI IT-Grundschutz', 'BSI Grundschutz', 'IT-Grundschutz',
        'Baustein', 'BSI Baustein',
        'Grundschutz-Kompendium', 'IT-Grundschutz-Kompendium'
    ]
    
    # Template type to framework mapping
    TEMPLATE_TYPE_FRAMEWORKS = {
        'it-operation': ['ITIL', 'ISO20000', 'COBIT'],
        'bcm': ['ISO22301', 'BSI_BCM'],
        'isms': ['ISO27001'],
        'bsi-grundschutz': ['BSI_GRUNDSCHUTZ']
    }
    
    def __init__(self):
        """Initialize template validator."""
        pass
    
    def validate_template(self, template_path: Path, template_type: str = 'it-operation') -> ValidationResult:
        """
        Validate a single template file.
        
        Args:
            template_path: Path to template file
            template_type: Type of template (it-operation, bcm, isms, bsi-grundschutz)
            
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
        raci_warnings = self.validate_raci_matrix(content)
        for warning in raci_warnings:
            result.add_warning(f"{template_path.name}: {warning}")
        
        # Validate placeholder syntax
        placeholder_warnings = self.validate_placeholder_syntax(content)
        for warning in placeholder_warnings:
            result.add_warning(f"{template_path.name}: {warning}")
        
        # Validate framework references
        framework_warnings = self.validate_framework_references(content, template_type)
        for warning in framework_warnings:
            result.add_warning(f"{template_path.name}: {warning}")
        
        return result
    
    def validate_raci_matrix(self, content: str) -> list[str]:
        """
        Validate RACI matrix completeness.
        
        Checks that each activity row has:
        - Exactly one 'A' (Accountable)
        - At least one 'R' (Responsible)
        
        Args:
            content: Template content to validate
            
        Returns:
            List of warning messages
        """
        warnings = []
        
        # Find all tables that might be RACI matrices
        raci_pattern = re.compile(
            r'\|[^\n]*\|[^\n]*\n\|[-:\s|]+\n((?:\|[^\n]*\n)+)',
            re.MULTILINE
        )
        
        tables = raci_pattern.findall(content)
        
        if not tables:
            return warnings
        
        # Check each table for RACI matrix characteristics
        for table_idx, table_content in enumerate(tables):
            rows = table_content.strip().split('\n')
            
            # Check if this looks like a RACI matrix
            is_raci_matrix = False
            for row in rows:
                cells = [cell.strip() for cell in row.split('|')[1:-1]]
                for cell in cells:
                    if cell.upper() in {'R', 'A', 'C', 'I'}:
                        is_raci_matrix = True
                        break
                if is_raci_matrix:
                    break
            
            if not is_raci_matrix:
                continue
            
            # Validate RACI matrix completeness
            for row_idx, row in enumerate(rows):
                cells = [cell.strip() for cell in row.split('|')[1:-1]]
                
                if len(cells) < 2:
                    continue
                
                # First cell is activity name, rest are RACI assignments
                activity = cells[0]
                raci_values = [cell.upper() for cell in cells[1:]]
                
                # Count A and R values
                a_count = raci_values.count('A')
                r_count = raci_values.count('R')
                
                # Check for exactly one A
                if a_count == 0:
                    warnings.append(
                        f"RACI matrix row '{activity}' has no Accountable (A) assignment"
                    )
                elif a_count > 1:
                    warnings.append(
                        f"RACI matrix row '{activity}' has multiple Accountable (A) assignments ({a_count})"
                    )
                
                # Check for at least one R
                if r_count == 0:
                    warnings.append(
                        f"RACI matrix row '{activity}' has no Responsible (R) assignment"
                    )
        
        return warnings
    
    def validate_framework_references(self, content: str, template_type: str) -> list[str]:
        """
        Validate presence of framework references based on template type.
        
        Args:
            content: Template content to validate
            template_type: Type of template (it-operation, bcm, isms, bsi-grundschutz)
            
        Returns:
            List of warning messages
        """
        warnings = []
        
        # Get expected frameworks for this template type
        expected_frameworks = self.TEMPLATE_TYPE_FRAMEWORKS.get(template_type, [])
        
        if not expected_frameworks:
            return warnings
        
        # Check for framework references
        has_framework = False
        
        for framework in expected_frameworks:
            if framework == 'ITIL':
                if any(keyword in content for keyword in self.ITIL_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'ISO20000':
                if any(keyword in content for keyword in self.ISO20000_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'COBIT':
                if any(keyword in content for keyword in self.COBIT_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'ISO22301':
                if any(keyword in content for keyword in self.ISO22301_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'BSI_BCM':
                if any(keyword in content for keyword in self.BSI_BCM_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'ISO27001':
                if any(keyword in content for keyword in self.ISO27001_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'BSI_GRUNDSCHUTZ':
                if any(keyword in content for keyword in self.BSI_GRUNDSCHUTZ_KEYWORDS):
                    has_framework = True
                    break
        
        if not has_framework:
            framework_names = ', '.join(expected_frameworks)
            warnings.append(
                f"Template does not reference expected frameworks ({framework_names}). "
                f"Consider adding framework references for compliance documentation."
            )
        
        return warnings
    
    def validate_placeholder_syntax(self, content: str) -> list[str]:
        """
        Validate placeholder syntax correctness.
        
        Checks that all placeholders follow the format: {{ source.field }}
        where source is alphanumeric and field can contain dots for nested paths.
        
        Args:
            content: Template content to validate
            
        Returns:
            List of warning messages
        """
        warnings = []
        
        # Find all potential placeholders
        placeholder_pattern = re.compile(r'\{\{[^}]*\}\}')
        placeholders = placeholder_pattern.findall(content)
        
        # Valid placeholder format: {{ source.field }}
        valid_pattern = re.compile(r'^\{\{\s*[a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+\s*\}\}$')
        
        for placeholder in placeholders:
            if not valid_pattern.match(placeholder):
                warnings.append(
                    f"Invalid placeholder syntax: '{placeholder}'. "
                    f"Expected format: {{{{ source.field }}}}"
                )
        
        return warnings
    
    def validate_numbering(self, templates: list) -> list[str]:
        """
        Validate template numbering sequence.
        
        Checks that template numbering:
        - Uses 4-digit prefixes
        - Has no duplicates
        - Forms a valid sequence
        
        Args:
            templates: List of Template objects or file paths
            
        Returns:
            List of warning messages
        """
        warnings = []
        
        # Extract numbering from templates
        numbers = []
        filenames = []
        
        for template in templates:
            # Handle both Template objects and Path objects
            if hasattr(template, 'path'):
                filename = template.path.name
            elif hasattr(template, 'name'):
                filename = template.name
            else:
                filename = str(template)
            
            filenames.append(filename)
            
            # Extract 4-digit prefix
            match = re.match(r'^(\d{4})_', filename)
            if match:
                numbers.append(int(match.group(1)))
            else:
                warnings.append(
                    f"Template '{filename}' does not have 4-digit prefix (e.g., 0010_)"
                )
        
        # Check for duplicates
        if len(numbers) != len(set(numbers)):
            duplicates = [n for n in numbers if numbers.count(n) > 1]
            warnings.append(
                f"Duplicate template numbers found: {set(duplicates)}"
            )
        
        # Check for gaps (optional - only warn if significant gaps)
        if numbers:
            sorted_numbers = sorted(numbers)
            for i in range(len(sorted_numbers) - 1):
                gap = sorted_numbers[i + 1] - sorted_numbers[i]
                if gap > 20:  # Warn only for significant gaps
                    warnings.append(
                        f"Large gap in template numbering: {sorted_numbers[i]} to {sorted_numbers[i + 1]}"
                    )
        
        return warnings
    
    def validate_template_directory(
        self,
        templates_dir: Path,
        template_type: str = 'it-operation'
    ) -> Dict[str, ValidationResult]:
        """
        Validate all templates in a directory.
        
        Args:
            templates_dir: Path to templates directory
            template_type: Type of template (it-operation, bcm, isms, bsi-grundschutz)
            
        Returns:
            Dictionary mapping template filenames to ValidationResults
        """
        results = {}
        
        if not templates_dir.exists():
            return results
        
        for template_file in templates_dir.glob('*.md'):
            result = self.validate_template(template_file, template_type)
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
        description='Validate templates for quality and compliance'
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
    parser.add_argument(
        '--template-type',
        type=str,
        choices=['it-operation', 'bcm', 'isms', 'bsi-grundschutz'],
        default='it-operation',
        help='Template type (default: it-operation)'
    )
    
    args = parser.parse_args()
    
    templates_dir = Path(args.template_dir)
    
    if not templates_dir.exists():
        print(f"Error: Template directory not found: {templates_dir}")
        return 1
    
    validator = TemplateValidator()
    results = validator.validate_template_directory(templates_dir, args.template_type)
    validator.print_validation_summary(results)
    
    # Return non-zero exit code if there are errors
    has_errors = any(not r.is_valid for r in results.values())
    return 1 if has_errors else 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
