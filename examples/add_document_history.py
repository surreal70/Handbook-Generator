#!/usr/bin/env python3
"""
Add Document History to Template Files

This script adds standardized document history sections to all template
markdown files across specified frameworks.

Usage:
    python examples/add_document_history.py --frameworks bcm isms bsi-grundschutz it-operation
    python examples/add_document_history.py --all
    python examples/add_document_history.py --framework bcm --language de

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import DocumentHistoryStandardizer


def main():
    parser = argparse.ArgumentParser(
        description='Add document history sections to template files'
    )
    parser.add_argument(
        '--frameworks',
        nargs='+',
        help='Framework names to process (e.g., bcm isms gdpr)'
    )
    parser.add_argument(
        '--framework',
        help='Single framework to process'
    )
    parser.add_argument(
        '--language',
        choices=['de', 'en'],
        help='Language to process (de or en)'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all frameworks'
    )
    parser.add_argument(
        '--templates-dir',
        default='templates',
        help='Path to templates directory (default: templates)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    
    args = parser.parse_args()
    
    # Initialize standardizer
    standardizer = DocumentHistoryStandardizer(args.templates_dir)
    
    # Determine which frameworks to process
    if args.all:
        frameworks = None  # Process all
    elif args.framework:
        frameworks = [args.framework]
    elif args.frameworks:
        frameworks = args.frameworks
    else:
        print("Error: Must specify --all, --framework, or --frameworks")
        return 1
    
    # Determine which languages to process
    languages = [args.language] if args.language else ['de', 'en']
    
    # Scan all template files
    all_files = standardizer.scan_template_files()
    
    # Filter by framework and language
    files_to_process = []
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
        if frameworks and file_framework not in frameworks:
            continue
        
        files_to_process.append((filepath, file_language, file_framework))
    
    print(f"Found {len(files_to_process)} template files to process")
    print()
    
    # Process files
    added_count = 0
    skipped_count = 0
    error_count = 0
    
    for filepath, language, framework in files_to_process:
        # Check if already has document history
        if standardizer.has_document_history(filepath):
            print(f"SKIP: {filepath} (already has document history)")
            skipped_count += 1
            continue
        
        if args.dry_run:
            print(f"WOULD ADD: {filepath}")
            added_count += 1
        else:
            # Add document history
            success = standardizer.add_document_history(filepath, language)
            
            if success:
                print(f"ADDED: {filepath}")
                added_count += 1
            else:
                print(f"ERROR: {filepath}")
                error_count += 1
    
    # Print summary
    print()
    print("=" * 60)
    print("Summary:")
    print(f"  Files processed: {len(files_to_process)}")
    print(f"  Document history added: {added_count}")
    print(f"  Already had history (skipped): {skipped_count}")
    print(f"  Errors: {error_count}")
    
    if args.dry_run:
        print()
        print("DRY RUN - No changes were made")
    
    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
