#!/usr/bin/env python3
"""
Consolidated framework validation script.

This script validates compliance framework templates for naming conventions,
structure, placeholders, and bilingual consistency.

Supported frameworks:
- bcm (Business Continuity Management)
- bsi-grundschutz (BSI IT-Grundschutz)
- cis-controls (CIS Controls)
- common-criteria (Common Criteria)
- gdpr (General Data Protection Regulation)
- hipaa (Health Insurance Portability and Accountability Act)
- idw-ps-951 (IDW PS 951 IT Auditing Standard)
- isms (Information Security Management System)
- iso-9001 (ISO 9001 Quality Management)
- it-operation (IT Operations)
- nist-800-53 (NIST SP 800-53)
- nist-csf (NIST Cybersecurity Framework 2.0)
- pci-dss (Payment Card Industry Data Security Standard)
- service-directory (Service Directory)
- togaf (The Open Group Architecture Framework)
- tsc (Trust Services Criteria)

Usage:
    python helpers/validate_frameworks.py
    python helpers/validate_frameworks.py --framework idw-ps-951
    python helpers/validate_frameworks.py --language de
    python helpers/validate_frameworks.py --output report.txt
    python helpers/validate_frameworks.py --verbose

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2025, 2026
"""

import argparse
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.template_validator import TemplateValidator


# All available frameworks
ALL_FRAMEWORKS = [
    'bcm',
    'bsi-grundschutz',
    'cis-controls',
    'common-criteria',
    'gdpr',
    'hipaa',
    'idw-ps-951',
    'isms',
    'iso-9001',
    'it-operation',
    'nist-800-53',
    'nist-csf',
    'pci-dss',
    'service-directory',
    'togaf',
    'tsc'
]


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Validate compliance framework templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --framework idw-ps-951
  %(prog)s --framework idw-ps-951 --language de
  %(prog)s --output report.txt
  %(prog)s --framework nist-csf --verbose
        """
    )
    
    # Framework selection
    parser.add_argument(
        '--framework',
        type=str,
        help='Specific framework to validate (if omitted, validates all frameworks)'
    )
    
    # Language selection
    parser.add_argument(
        '--language',
        type=str,
        choices=['de', 'en', 'both'],
        default='both',
        help='Language to validate (default: both)'
    )
    
    # Output options
    parser.add_argument(
        '--output',
        type=str,
        help='Output file for validation report (optional)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed validation results'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Only show summary (suppress per-framework output)'
    )
    
    args = parser.parse_args()
    
    # Determine which frameworks to validate
    if args.framework:
        frameworks = [args.framework]
    else:
        frameworks = ALL_FRAMEWORKS
    
    # Determine which languages to validate
    if args.language == 'both':
        languages = ['de', 'en']
    else:
        languages = [args.language]
    
    # Initialize validator
    templates_dir = Path(__file__).parent.parent / 'templates'
    validator = TemplateValidator()
    
    # Print header
    if not args.quiet:
        print("=" * 80)
        print("FRAMEWORK VALIDATION REPORT")
        print("=" * 80)
        print(f"Frameworks: {', '.join(frameworks)}")
        print(f"Languages: {', '.join(languages)}")
        print("=" * 80)
        print()
    
    # Validate frameworks
    results = {}
    all_valid = True
    
    for framework in frameworks:
        results[framework] = {}
        
        for language in languages:
            key = f"{language}/{framework}"
            
            if not args.quiet:
                print(f"Validating {key}...")
            
            result = validator.validate_framework(language, framework, templates_dir)
            results[framework][language] = result
            
            if not result.is_valid:
                all_valid = False
            
            if not args.quiet:
                if result.is_valid:
                    print(f"  ✓ VALID")
                else:
                    print(f"  ✗ INVALID")
                
                if args.verbose or not result.is_valid:
                    if result.errors:
                        print(f"  Errors: {len(result.errors)}")
                        max_errors = None if args.verbose else 5
                        for i, error in enumerate(result.errors[:max_errors]):
                            print(f"    - {error}")
                        if not args.verbose and len(result.errors) > 5:
                            print(f"    ... and {len(result.errors) - 5} more errors")
                    
                    if result.warnings:
                        print(f"  Warnings: {len(result.warnings)}")
                        max_warnings = None if args.verbose else 5
                        for i, warning in enumerate(result.warnings[:max_warnings]):
                            print(f"    - {warning}")
                        if not args.verbose and len(result.warnings) > 5:
                            print(f"    ... and {len(result.warnings) - 5} more warnings")
                
                print()
    
    # Print summary
    print("=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print()
    
    for framework in frameworks:
        de_result = results[framework].get('de')
        en_result = results[framework].get('en')
        
        status_parts = []
        if de_result:
            de_status = "✓" if de_result.is_valid else "✗"
            status_parts.append(f"DE: {de_status}")
        if en_result:
            en_status = "✓" if en_result.is_valid else "✗"
            status_parts.append(f"EN: {en_status}")
        
        status_str = "  ".join(status_parts)
        print(f"{framework:25s} {status_str}")
    
    print()
    print("=" * 80)
    
    if all_valid:
        print("✓ ALL FRAMEWORKS VALID")
        exit_code = 0
    else:
        print("✗ SOME FRAMEWORKS HAVE ERRORS")
        exit_code = 1
    
    # Generate detailed report if requested
    if args.output:
        output_path = Path(args.output)
        all_results = {
            f"{lang}/{fw}": results[fw][lang]
            for fw in frameworks
            for lang in languages
            if lang in results[fw]
        }
        report = validator.generate_validation_report(all_results, output_path)
        print(f"\nDetailed validation report written to: {output_path}")
    
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
