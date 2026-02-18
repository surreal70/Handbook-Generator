"""
Template Validator

Validates IT-Operations templates for quality and compliance.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2025, 2026
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
    
    # IDW PS 951 Framework keywords
    IDW_PS_951_KEYWORDS = [
        'IDW PS 951', 'IDW-PS-951', 'IDW PS951',
        'Prüfungsstandard 951', 'IT-Prüfung', 'IT-Audit',
        'Prüfungsplanung', 'Risikobeurteilung', 'Kontrollprüfung',
        'Prüfungsfeststellungen', 'IT-Strategie', 'IT-Governance',
        'IT-Organisation', 'IT-Prozesse', 'IT-Systeme'
    ]
    
    # NIST CSF Framework keywords
    NIST_CSF_KEYWORDS = [
        'NIST CSF', 'NIST Cybersecurity Framework', 'CSF 2.0',
        'NIST Framework', 'Govern function', 'Identify function',
        'Protect function', 'Detect function', 'Respond function',
        'Recover function', 'CSF Profile', 'Implementation Tier'
    ]
    
    # TOGAF Framework keywords
    TOGAF_KEYWORDS = [
        'TOGAF', 'The Open Group Architecture Framework',
        'Architecture Development Method', 'ADM',
        'Preliminary Phase', 'Architecture Vision', 'Business Architecture',
        'Information Systems Architecture', 'Technology Architecture',
        'Opportunities and Solutions', 'Migration Planning',
        'Implementation Governance', 'Architecture Change Management',
        'Requirements Management', 'Architecture Building Block', 'ABB', 'SBB'
    ]
    
    # Template type to framework mapping
    TEMPLATE_TYPE_FRAMEWORKS = {
        'it-operation': ['ITIL', 'ISO20000', 'COBIT'],
        'bcm': ['ISO22301', 'BSI_BCM'],
        'isms': ['ISO27001'],
        'bsi-grundschutz': ['BSI_GRUNDSCHUTZ'],
        'idw-ps-951': ['IDW_PS_951'],
        'nist-csf': ['NIST_CSF'],
        'togaf': ['TOGAF']
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
            elif framework == 'IDW_PS_951':
                if any(keyword in content for keyword in self.IDW_PS_951_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'NIST_CSF':
                if any(keyword in content for keyword in self.NIST_CSF_KEYWORDS):
                    has_framework = True
                    break
            elif framework == 'TOGAF':
                if any(keyword in content for keyword in self.TOGAF_KEYWORDS):
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

    def validate_new_frameworks(self, templates_base_dir: Path = None) -> Dict[str, ValidationResult]:
        """
        Validate all new framework templates (IDW PS 951, NIST CSF, TOGAF).
        
        Args:
            templates_base_dir: Base directory for templates (defaults to ./templates)
            
        Returns:
            Dictionary mapping framework names to ValidationResults
        """
        if templates_base_dir is None:
            templates_base_dir = Path("templates")
        
        results = {}
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        languages = ['de', 'en']
        
        for framework in new_frameworks:
            for language in languages:
                key = f"{language}/{framework}"
                results[key] = self.validate_framework(language, framework, templates_base_dir)
        
        return results
    
    def generate_validation_report(self, results: Dict[str, ValidationResult], output_path: Path = None) -> str:
        """
        Generate a comprehensive validation report.
        
        Args:
            results: Dictionary of validation results
            output_path: Optional path to write report to file
            
        Returns:
            Report as string
        """
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("TEMPLATE VALIDATION REPORT")
        report_lines.append("=" * 80)
        report_lines.append("")
        
        # Summary statistics
        total_frameworks = len(results)
        valid_frameworks = sum(1 for r in results.values() if r.is_valid)
        total_errors = sum(len(r.errors) for r in results.values())
        total_warnings = sum(len(r.warnings) for r in results.values())
        
        report_lines.append("SUMMARY")
        report_lines.append("-" * 80)
        report_lines.append(f"Total frameworks validated: {total_frameworks}")
        report_lines.append(f"Valid frameworks: {valid_frameworks}")
        report_lines.append(f"Frameworks with issues: {total_frameworks - valid_frameworks}")
        report_lines.append(f"Total errors: {total_errors}")
        report_lines.append(f"Total warnings: {total_warnings}")
        report_lines.append("")
        
        # Detailed results per framework
        for framework_key, result in sorted(results.items()):
            report_lines.append("=" * 80)
            report_lines.append(f"FRAMEWORK: {framework_key}")
            report_lines.append("=" * 80)
            report_lines.append(f"Status: {'VALID' if result.is_valid else 'INVALID'}")
            report_lines.append(f"Errors: {len(result.errors)}")
            report_lines.append(f"Warnings: {len(result.warnings)}")
            report_lines.append("")
            
            if result.errors:
                report_lines.append("ERRORS:")
                report_lines.append("-" * 80)
                for error in result.errors:
                    report_lines.append(f"  ✗ {error}")
                report_lines.append("")
            
            if result.warnings:
                report_lines.append("WARNINGS:")
                report_lines.append("-" * 80)
                for warning in result.warnings:
                    report_lines.append(f"  ⚠ {warning}")
                report_lines.append("")
        
        report = "\n".join(report_lines)
        
        # Write to file if path provided
        if output_path:
            output_path.write_text(report, encoding='utf-8')
        
        return report

    def validate_framework(self, language: str, framework: str, templates_base_dir: Path = None) -> ValidationResult:
        """
        Validate all templates in a framework.

        Checks:
        - File naming convention (NNNN_name.md)
        - Unique template numbers
        - Metadata template exists
        - README.md exists
        - Placeholder syntax
        - Bilingual consistency (if both languages present)

        Args:
            language: Language code (de, en)
            framework: Framework name (pci-dss, hipaa, nist-800-53, etc.)
            templates_base_dir: Base directory for templates (defaults to ./templates)

        Returns:
            ValidationResult with errors and warnings
        """
        result = ValidationResult(is_valid=True, warnings=[], errors=[])

        if templates_base_dir is None:
            templates_base_dir = Path("templates")

        template_dir = templates_base_dir / language / framework

        # Check directory exists
        if not template_dir.exists():
            result.add_error(f"Template directory not found: {template_dir}")
            return result

        # Check README exists
        readme_path = template_dir / "README.md"
        if not readme_path.exists():
            result.add_warning(f"README.md not found in {template_dir}")

        # Check FRAMEWORK_MAPPING exists
        mapping_path = template_dir / "9999_Framework_Mapping.md"
        if not mapping_path.exists():
            result.add_warning(f"9999_Framework_Mapping.md not found in {template_dir}")

        # Check metadata template exists
        metadata_pattern = f"0000_metadata_{language}_{framework}.md"
        metadata_path = template_dir / metadata_pattern
        if not metadata_path.exists():
            result.add_error(f"Metadata template not found: {metadata_pattern}")

        # Validate each template file
        template_numbers = set()
        for file_path in template_dir.glob("*.md"):
            # Skip special files
            if file_path.name in ["README.md", "9999_Framework_Mapping.md"]:
                continue

            # Validate filename format (NNNN_name.md)
            if not re.match(r'^\d{4}_[\w\-äöüÄÖÜß]+\.md$', file_path.name):
                result.add_error(f"Invalid filename format: {file_path.name} (expected NNNN_name.md)")
                continue

            # Check for duplicate numbers
            number = int(file_path.name[:4])
            if number in template_numbers:
                result.add_error(f"Duplicate template number: {number:04d}")
            template_numbers.add(number)

            # Validate template content
            self._validate_template_content(file_path, result)

        # Check bilingual consistency if this is German
        if language == 'de':
            self._check_bilingual_consistency(framework, templates_base_dir, result)

        return result

    def _validate_template_content(self, file_path: Path, result: ValidationResult) -> None:
        """
        Validate individual template content.

        Args:
            file_path: Path to template file
            result: ValidationResult to add warnings/errors to
        """
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            result.add_error(f"{file_path.name}: Failed to read file: {e}")
            return

        # Check for required header fields (for non-metadata templates)
        if not file_path.name.startswith('0000_metadata'):
            required_fields = ['Dokument-ID', 'Owner', 'Version', 'Status']
            for field in required_fields:
                if f"**{field}:**" not in content and f"**{field}**:" not in content:
                    result.add_warning(f"{file_path.name}: Missing header field '{field}'")

        # Validate placeholder syntax
        placeholders = re.findall(r'\{\{[^}]+\}\}', content)
        for placeholder in placeholders:
            # Valid format: {{ source.field }} or {{ source.nested.field }}
            if not re.match(r'^\{\{\s*[a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+\s*\}\}$', placeholder):
                result.add_error(f"{file_path.name}: Invalid placeholder syntax: {placeholder}")

    def _check_bilingual_consistency(self, framework: str, templates_base_dir: Path, result: ValidationResult) -> None:
        """
        Check that German and English templates match in structure.

        Args:
            framework: Framework name
            templates_base_dir: Base directory for templates
            result: ValidationResult to add warnings/errors to
        """
        de_dir = templates_base_dir / 'de' / framework
        en_dir = templates_base_dir / 'en' / framework

        if not en_dir.exists():
            result.add_warning(f"English templates not found for framework '{framework}'")
            return

        de_files = {f.name for f in de_dir.glob("*.md") if f.name not in ["README.md", "9999_Framework_Mapping.md"]}
        en_files = {f.name for f in en_dir.glob("*.md") if f.name not in ["README.md", "9999_Framework_Mapping.md"]}

        # Extract template numbers for comparison
        de_numbers = {int(f[:4]) for f in de_files if re.match(r'^\d{4}_', f)}
        en_numbers = {int(f[:4]) for f in en_files if re.match(r'^\d{4}_', f)}

        # Check for missing translations by number
        missing_en = de_numbers - en_numbers
        missing_de = en_numbers - de_numbers

        if missing_en:
            result.add_warning(f"Missing English translations for template numbers: {sorted(missing_en)}")
        if missing_de:
            result.add_warning(f"Missing German translations for template numbers: {sorted(missing_de)}")

        # Check matching markdown structure for common templates
        common_numbers = de_numbers & en_numbers
        for number in common_numbers:
            de_file = next((f for f in de_dir.glob(f"{number:04d}_*.md")), None)
            en_file = next((f for f in en_dir.glob(f"{number:04d}_*.md")), None)

            if de_file and en_file:
                self._check_matching_structure(de_file, en_file, result)

    def _check_matching_structure(self, de_file: Path, en_file: Path, result: ValidationResult) -> None:
        """
        Check that two template files have matching markdown structure.

        Args:
            de_file: German template file
            en_file: English template file
            result: ValidationResult to add warnings/errors to
        """
        try:
            de_content = de_file.read_text(encoding='utf-8')
            en_content = en_file.read_text(encoding='utf-8')
        except Exception as e:
            result.add_warning(f"Failed to read files for structure comparison: {e}")
            return

        # Extract markdown headers
        de_headers = re.findall(r'^#{1,6}\s+.+$', de_content, re.MULTILINE)
        en_headers = re.findall(r'^#{1,6}\s+.+$', en_content, re.MULTILINE)

        # Check header count matches
        if len(de_headers) != len(en_headers):
            result.add_warning(
                f"Structure mismatch between {de_file.name} and {en_file.name}: "
                f"Different number of headers ({len(de_headers)} vs {len(en_headers)})"
            )

        # Extract placeholders
        de_placeholders = re.findall(r'\{\{[^}]+\}\}', de_content)
        en_placeholders = re.findall(r'\{\{[^}]+\}\}', en_content)

        # Check placeholder positions match (same placeholders in same order)
        if de_placeholders != en_placeholders:
            result.add_warning(
                f"Placeholder mismatch between {de_file.name} and {en_file.name}: "
                f"Placeholders differ or are in different positions"
            )

    
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
