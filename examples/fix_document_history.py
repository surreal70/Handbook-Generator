#!/usr/bin/env python3
"""
Fix Document History in Template Files

This script fixes document history sections in all template files by:
1. Removing duplicate entries
2. Placing history before <!-- End of template --> marker
3. Using the old format: **Document History:**

Usage:
    python examples/fix_document_history.py
    python examples/fix_document_history.py --framework bcm
    python examples/fix_document_history.py --dry-run

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
        description='Fix document history sections in template files'
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
        if args.framework and file_framework != args.framework:
            continue
        
        files_to_process.append((filepath, file_language, file_framework))
    
    print(f"Processing {len(files_to_process)} template files...")
    print()
    
    # Process files
    fixed_count = 0
    error_count = 0
    
    for filepath, language, framework in files_to_process:
        if args.dry_run:
            print(f"WOULD FIX: {filepath}")
            fixed_count += 1
        else:
            # Fix document history (this will remove duplicates and reposition)
            success = standardizer.add_document_history(filepath, language)
            
            if success:
                print(f"FIXED: {filepath}")
                fixed_count += 1
            else:
                print(f"ERROR: {filepath}")
                error_count += 1
    
    # Print summary
    print()
    print("=" * 60)
    print("Summary:")
    print(f"  Files processed: {len(files_to_process)}")
    print(f"  Files fixed: {fixed_count}")
    print(f"  Errors: {error_count}")
    
    if args.dry_run:
        print()
        print("DRY RUN - No changes were made")
    
    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
