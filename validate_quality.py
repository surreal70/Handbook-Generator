#!/usr/bin/env python3
"""
Quality Assurance and Validation Script

This script performs comprehensive validation of all framework templates:
1. Verify Document-IDs match filenames
2. Ensure all templates have proper metadata sections
3. Verify all templates have version history
4. Check bilingual consistency (DE/EN content alignment)
5. Validate framework mappings reference only existing templates
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
import json


@dataclass
class ValidationIssue:
    """Represents a validation issue found during checks"""
    severity: str  # 'error', 'warning', 'info'
    category: str
    file_path: str
    message: str


@dataclass
class ValidationReport:
    """Complete validation report"""
    total_files_checked: int
    issues: List[ValidationIssue]
    frameworks_checked: Set[str]
    
    def has_errors(self) -> bool:
        return any(issue.severity == 'error' for issue in self.issues)
    
    def error_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity == 'error')
    
    def warning_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity == 'warning')


class QualityValidator:
    """Comprehensive quality validation for framework templates"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.templates_path = self.base_path / "templates"
        self.issues: List[ValidationIssue] = []
        self.frameworks_checked: Set[str] = set()
        self.total_files_checked = 0
        
    def validate_all(self) -> ValidationReport:
        """Run all validation checks"""
        print("Starting comprehensive quality validation...")
        print("=" * 80)
        
        # Check 1: Document-ID vs filename matching
        print("\n1. Validating Document-IDs match filenames...")
        self.validate_document_ids()
        
        # Check 2: Metadata sections
        print("\n2. Validating metadata sections...")
        self.validate_metadata_sections()
        
        # Check 3: Version history
        print("\n3. Validating version history...")
        self.validate_version_history()
        
        # Check 4: Bilingual consistency
        print("\n4. Validating bilingual consistency...")
        self.validate_bilingual_consistency()
        
        # Check 5: Framework mapping references
        print("\n5. Validating framework mapping references...")
        self.validate_framework_mappings()
        
        return ValidationReport(
            total_files_checked=self.total_files_checked,
            issues=self.issues,
            frameworks_checked=self.frameworks_checked
        )
    
    def validate_document_ids(self):
        """Verify Document-IDs match filenames"""
        for lang in ['de', 'en']:
            lang_path = self.templates_path / lang
            if not lang_path.exists():
                continue
                
            for framework_dir in lang_path.iterdir():
                if not framework_dir.is_dir():
                    continue
                    
                self.frameworks_checked.add(framework_dir.name)
                
                for template_file in framework_dir.glob("*.md"):
                    self.total_files_checked += 1
                    
                    # Skip metadata and README files
                    if template_file.name in ['metadata.yaml', 'README.md']:
                        continue
                    
                    # Extract expected Document-ID from filename
                    filename_id = template_file.stem  # e.g., "0100_template_name"
                    
                    # Read file and find Document-ID
                    try:
                        content = template_file.read_text(encoding='utf-8')
                        
                        # Look for Document-ID pattern
                        doc_id_match = re.search(r'Document-ID:\s*([^\s\n]+)', content)
                        
                        if not doc_id_match:
                            self.issues.append(ValidationIssue(
                                severity='error',
                                category='document_id',
                                file_path=str(template_file.relative_to(self.base_path)),
                                message='Missing Document-ID in metadata'
                            ))
                            continue
                        
                        doc_id = doc_id_match.group(1)
                        
                        # Check if Document-ID matches filename
                        if doc_id != filename_id:
                            self.issues.append(ValidationIssue(
                                severity='error',
                                category='document_id',
                                file_path=str(template_file.relative_to(self.base_path)),
                                message=f'Document-ID mismatch: file={filename_id}, metadata={doc_id}'
                            ))
                    
                    except Exception as e:
                        self.issues.append(ValidationIssue(
                            severity='error',
                            category='document_id',
                            file_path=str(template_file.relative_to(self.base_path)),
                            message=f'Error reading file: {str(e)}'
                        ))
    
    def validate_metadata_sections(self):
        """Ensure all templates have proper metadata sections"""
        required_metadata_fields = [
            'Document-ID',
            'Title',
            'Version',
            'Last Updated',
            'Author',
            'Classification'
        ]
        
        for lang in ['de', 'en']:
            lang_path = self.templates_path / lang
            if not lang_path.exists():
                continue
                
            for framework_dir in lang_path.iterdir():
                if not framework_dir.is_dir():
                    continue
                
                for template_file in framework_dir.glob("*.md"):
                    # Skip metadata and README files
                    if template_file.name in ['metadata.yaml', 'README.md']:
                        continue
                    
                    try:
                        content = template_file.read_text(encoding='utf-8')
                        
                        # Check for metadata section
                        if '---' not in content[:500]:  # Metadata should be at the top
                            self.issues.append(ValidationIssue(
                                severity='warning',
                                category='metadata',
                                file_path=str(template_file.relative_to(self.base_path)),
                                message='No metadata section found (missing --- delimiters)'
                            ))
                            continue
                        
                        # Check for required fields
                        missing_fields = []
                        for field in required_metadata_fields:
                            if f'{field}:' not in content[:1000]:
                                missing_fields.append(field)
                        
                        if missing_fields:
                            self.issues.append(ValidationIssue(
                                severity='warning',
                                category='metadata',
                                file_path=str(template_file.relative_to(self.base_path)),
                                message=f'Missing metadata fields: {", ".join(missing_fields)}'
                            ))
                    
                    except Exception as e:
                        self.issues.append(ValidationIssue(
                            severity='error',
                            category='metadata',
                            file_path=str(template_file.relative_to(self.base_path)),
                            message=f'Error reading file: {str(e)}'
                        ))
    
    def validate_version_history(self):
        """Verify all templates have version history"""
        for lang in ['de', 'en']:
            lang_path = self.templates_path / lang
            if not lang_path.exists():
                continue
                
            for framework_dir in lang_path.iterdir():
                if not framework_dir.is_dir():
                    continue
                
                for template_file in framework_dir.glob("*.md"):
                    # Skip metadata and README files
                    if template_file.name in ['metadata.yaml', 'README.md']:
                        continue
                    
                    try:
                        content = template_file.read_text(encoding='utf-8')
                        
                        # Check for version history section (German or English)
                        has_version_history = (
                            '## Version History' in content or
                            '## Versionshistorie' in content or
                            '## Document History' in content or
                            '## Dokumentenhistorie' in content
                        )
                        
                        if not has_version_history:
                            self.issues.append(ValidationIssue(
                                severity='error',
                                category='version_history',
                                file_path=str(template_file.relative_to(self.base_path)),
                                message='Missing version history section'
                            ))
                    
                    except Exception as e:
                        self.issues.append(ValidationIssue(
                            severity='error',
                            category='version_history',
                            file_path=str(template_file.relative_to(self.base_path)),
                            message=f'Error reading file: {str(e)}'
                        ))
    
    def validate_bilingual_consistency(self):
        """Check bilingual consistency (DE/EN content alignment)"""
        de_path = self.templates_path / 'de'
        en_path = self.templates_path / 'en'
        
        if not de_path.exists() or not en_path.exists():
            self.issues.append(ValidationIssue(
                severity='error',
                category='bilingual',
                file_path='templates/',
                message='Missing de/ or en/ directory'
            ))
            return
        
        # Get all frameworks
        de_frameworks = {d.name for d in de_path.iterdir() if d.is_dir()}
        en_frameworks = {d.name for d in en_path.iterdir() if d.is_dir()}
        
        # Check for missing framework translations
        missing_en = de_frameworks - en_frameworks
        missing_de = en_frameworks - de_frameworks
        
        for framework in missing_en:
            self.issues.append(ValidationIssue(
                severity='error',
                category='bilingual',
                file_path=f'templates/en/{framework}',
                message=f'Framework exists in DE but missing in EN'
            ))
        
        for framework in missing_de:
            self.issues.append(ValidationIssue(
                severity='error',
                category='bilingual',
                file_path=f'templates/de/{framework}',
                message=f'Framework exists in EN but missing in DE'
            ))
        
        # Check template counts for each framework
        common_frameworks = de_frameworks & en_frameworks
        
        for framework in common_frameworks:
            de_templates = set((de_path / framework).glob("*.md"))
            en_templates = set((en_path / framework).glob("*.md"))
            
            de_names = {t.name for t in de_templates}
            en_names = {t.name for t in en_templates}
            
            # Check for missing translations
            missing_en_templates = de_names - en_names
            missing_de_templates = en_names - de_names
            
            for template_name in missing_en_templates:
                self.issues.append(ValidationIssue(
                    severity='warning',
                    category='bilingual',
                    file_path=f'templates/en/{framework}/{template_name}',
                    message=f'Template exists in DE but missing in EN'
                ))
            
            for template_name in missing_de_templates:
                self.issues.append(ValidationIssue(
                    severity='warning',
                    category='bilingual',
                    file_path=f'templates/de/{framework}/{template_name}',
                    message=f'Template exists in EN but missing in DE'
                ))
    
    def validate_framework_mappings(self):
        """Validate framework mappings reference only existing templates"""
        for lang in ['de', 'en']:
            lang_path = self.templates_path / lang
            if not lang_path.exists():
                continue
                
            for framework_dir in lang_path.iterdir():
                if not framework_dir.is_dir():
                    continue
                
                # Look for framework mapping file
                mapping_file = framework_dir / '9999_Framework_Mapping.md'
                
                if not mapping_file.exists():
                    self.issues.append(ValidationIssue(
                        severity='error',
                        category='framework_mapping',
                        file_path=str(framework_dir.relative_to(self.base_path)),
                        message='Missing 9999_Framework_Mapping.md file'
                    ))
                    continue
                
                try:
                    content = mapping_file.read_text(encoding='utf-8')
                    
                    # Get all actual template files in this framework
                    actual_templates = {
                        f.stem for f in framework_dir.glob("*.md")
                        if f.name not in ['metadata.yaml', 'README.md', '9999_Framework_Mapping.md']
                    }
                    
                    # Find all template references in mapping file
                    # Look for patterns like: 0100_template_name.md or [0100_template_name]
                    referenced_templates = set()
                    
                    # Pattern 1: Direct file references (0100_template.md)
                    for match in re.finditer(r'(\d{4}_[a-z_]+)\.md', content):
                        referenced_templates.add(match.group(1))
                    
                    # Pattern 2: Markdown links [text](0100_template.md)
                    for match in re.finditer(r'\]\((\d{4}_[a-z_]+)\.md\)', content):
                        referenced_templates.add(match.group(1))
                    
                    # Pattern 3: Just the ID in brackets or lists
                    for match in re.finditer(r'(?:^|\s)(\d{4}_[a-z_]+)(?:\s|$|:)', content, re.MULTILINE):
                        referenced_templates.add(match.group(1))
                    
                    # Check for references to non-existent templates
                    missing_templates = referenced_templates - actual_templates
                    
                    for template_id in missing_templates:
                        self.issues.append(ValidationIssue(
                            severity='error',
                            category='framework_mapping',
                            file_path=str(mapping_file.relative_to(self.base_path)),
                            message=f'References non-existent template: {template_id}.md'
                        ))
                    
                    # Check for templates not mentioned in mapping (info only)
                    unreferenced_templates = actual_templates - referenced_templates
                    
                    if unreferenced_templates:
                        self.issues.append(ValidationIssue(
                            severity='info',
                            category='framework_mapping',
                            file_path=str(mapping_file.relative_to(self.base_path)),
                            message=f'Templates not referenced in mapping: {", ".join(sorted(unreferenced_templates))}'
                        ))
                
                except Exception as e:
                    self.issues.append(ValidationIssue(
                        severity='error',
                        category='framework_mapping',
                        file_path=str(mapping_file.relative_to(self.base_path)),
                        message=f'Error reading mapping file: {str(e)}'
                    ))


def print_report(report: ValidationReport):
    """Print validation report"""
    print("\n" + "=" * 80)
    print("VALIDATION REPORT")
    print("=" * 80)
    
    print(f"\nTotal files checked: {report.total_files_checked}")
    print(f"Frameworks checked: {len(report.frameworks_checked)}")
    print(f"  {', '.join(sorted(report.frameworks_checked))}")
    
    print(f"\nIssues found:")
    print(f"  Errors: {report.error_count()}")
    print(f"  Warnings: {report.warning_count()}")
    print(f"  Info: {sum(1 for i in report.issues if i.severity == 'info')}")
    
    if report.issues:
        print("\n" + "-" * 80)
        print("DETAILED ISSUES")
        print("-" * 80)
        
        # Group by category
        by_category: Dict[str, List[ValidationIssue]] = {}
        for issue in report.issues:
            if issue.category not in by_category:
                by_category[issue.category] = []
            by_category[issue.category].append(issue)
        
        for category, issues in sorted(by_category.items()):
            print(f"\n{category.upper()} ({len(issues)} issues):")
            
            # Group by severity
            errors = [i for i in issues if i.severity == 'error']
            warnings = [i for i in issues if i.severity == 'warning']
            infos = [i for i in issues if i.severity == 'info']
            
            if errors:
                print(f"\n  ERRORS ({len(errors)}):")
                for issue in errors[:10]:  # Limit to first 10
                    print(f"    - {issue.file_path}")
                    print(f"      {issue.message}")
                if len(errors) > 10:
                    print(f"    ... and {len(errors) - 10} more errors")
            
            if warnings:
                print(f"\n  WARNINGS ({len(warnings)}):")
                for issue in warnings[:5]:  # Limit to first 5
                    print(f"    - {issue.file_path}")
                    print(f"      {issue.message}")
                if len(warnings) > 5:
                    print(f"    ... and {len(warnings) - 5} more warnings")
            
            if infos:
                print(f"\n  INFO ({len(infos)}):")
                for issue in infos[:3]:  # Limit to first 3
                    print(f"    - {issue.file_path}")
                    print(f"      {issue.message}")
                if len(infos) > 3:
                    print(f"    ... and {len(infos) - 3} more info messages")
    
    print("\n" + "=" * 80)
    
    if report.has_errors():
        print("VALIDATION FAILED - Errors found")
        return 1
    else:
        print("VALIDATION PASSED - No errors found")
        return 0


def save_report_json(report: ValidationReport, output_file: str = "validation_report.json"):
    """Save validation report as JSON"""
    data = {
        'total_files_checked': report.total_files_checked,
        'frameworks_checked': sorted(list(report.frameworks_checked)),
        'error_count': report.error_count(),
        'warning_count': report.warning_count(),
        'issues': [
            {
                'severity': issue.severity,
                'category': issue.category,
                'file_path': issue.file_path,
                'message': issue.message
            }
            for issue in report.issues
        ]
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\nDetailed report saved to: {output_file}")


if __name__ == '__main__':
    validator = QualityValidator()
    report = validator.validate_all()
    
    exit_code = print_report(report)
    save_report_json(report)
    
    exit(exit_code)
