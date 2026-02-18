#!/usr/bin/env python3
"""
Validate Document History Standardization

This script validates that all template files have standardized document
history sections with correct format.

Usage:
    python examples/validate_document_history.py
    python examples/validate_document_history.py --framework bcm
    python examples/validate_document_history.py --language de

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import DocumentHistoryStandardizer


def main():
    parser = argparse.ArgumentParser(
        description='Validate document history sections in template files'
    )
    parser.add_argument(
        '--framework',
        help='Single framework to validate'
    )
    parser.add_argument(
        '--language',
        choices=['de', 'en'],
        help='Language to validate (de or en)'
    )
    parser.add_argument(
        '--templates-dir',
        default='templates',
        help='Path to templates directory (default: templates)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed validation results'
    )
    
    args = parser.parse_args()
    
    # Initialize standardizer
    standardizer = DocumentHistoryStandardizer(args.templates_dir)
    
    # Determine which languages to process
    languages = [args.language] if args.language else ['de', 'en']
    
    # Scan all template files
    all_files = standardizer.scan_template_files()
    
    # Filter by framework and language
    files_to_validate = []
    for filepath in all_files:
        path = Path(filepath)
        
        # Extract framework and language from path
        # Path format: templates/{language}/{framework}/...
        parts = path.parts
        if len(parts) < 3:
            continue
        
        file_language = parts[1]  # de or en
        file_framework = parts[2]  # framework name
        
        # Filter by language
        if file_language not in languages:
            continue
        
        # Filter by framework
        if args.framework and file_framework != args.framework:
            continue
        
        files_to_validate.append((filepath, file_language, file_framework))
    
    print(f"Validating {len(files_to_validate)} template files...")
    print()
    
    # Validate files
    valid_count = 0
    missing_count = 0
    warning_count = 0
    warnings_by_type = {}
    
    for filepath, language, framework in files_to_validate:
        validation = standardizer.validate_document_history_format(filepath)
        
        if validation.warnings:
            warning_count += 1
            
            if args.verbose:
                print(f"WARNINGS: {filepath}")
                for warning in validation.warnings:
                    print(f"  - {warning}")
                    # Track warning types
                    warnings_by_type[warning] = warnings_by_type.get(warning, 0) + 1
            
            # Check if missing document history
            if any('Missing document history' in w for w in validation.warnings):
                missing_count += 1
        else:
            valid_count += 1
            if args.verbose:
                print(f"OK: {filepath}")
    
    # Print summary
    print()
    print("=" * 60)
    print("Validation Summary:")
    print(f"  Total files validated: {len(files_to_validate)}")
    print(f"  Valid (no warnings): {valid_count}")
    print(f"  Files with warnings: {warning_count}")
    print(f"  Missing document history: {missing_count}")
    
    if warnings_by_type:
        print()
        print("Warning Types:")
        for warning_type, count in sorted(warnings_by_type.items(), key=lambda x: -x[1]):
            print(f"  {count:4d} - {warning_type}")
    
    # Calculate success rate
    success_rate = (valid_count / len(files_to_validate) * 100) if files_to_validate else 0
    print()
    print(f"Success Rate: {success_rate:.1f}%")
    
    # Return exit code
    if missing_count > 0:
        print()
        print("ERROR: Some files are missing document history sections")
        return 1
    elif warning_count > 0:
        print()
        print("WARNING: Some files have formatting warnings (backward compatibility)")
        return 0  # Warnings are acceptable for backward compatibility
    else:
        print()
        print("SUCCESS: All files have valid document history sections")
        return 0


if __name__ == '__main__':
    sys.exit(main())
