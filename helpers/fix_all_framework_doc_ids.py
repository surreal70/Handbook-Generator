#!/usr/bin/env python3
"""
Fix All Framework Document IDs

This script replaces [FRAMEWORK] with the appropriate uppercase handbook name
in all template files across all handbooks.

Usage:
    python helpers/fix_all_framework_doc_ids.py [--dry-run]
"""

import argparse
import re
from pathlib import Path
from typing import Dict


# Mapping of handbook directory names to their uppercase identifiers
HANDBOOK_MAPPING = {
    'bcm': 'BCM',
    'bsi-grundschutz': 'BSI-GRUNDSCHUTZ',
    'cis-controls': 'CIS-CONTROLS',
    'common-criteria': 'COMMON-CRITERIA',
    'coso': 'COSO',
    'csa-ccm': 'CSA-CCM',
    'dora': 'DORA',
    'gdpr': 'GDPR',
    'hipaa': 'HIPAA',
    'idw-ps-951': 'IDW-PS-951',
    'isms': 'ISMS',
    'iso-31000': 'ISO-31000',
    'iso-38500': 'ISO-38500',
    'iso-9001': 'ISO-9001',
    'it-operation': 'IT-OPERATION',
    'nist-800-53': 'NIST-800-53',
    'nist-csf': 'NIST-CSF',
    'pci-dss': 'PCI-DSS',
    'soc1': 'SOC1',
    'tisax': 'TISAX',
    'togaf': 'TOGAF',
    'tsc': 'TSC'
}


def fix_doc_id(file_path: Path, handbook_id: str, dry_run: bool = False) -> bool:
    """
    Fix document ID in a single file.
    
    Args:
        file_path: Path to the template file
        handbook_id: Uppercase handbook identifier (e.g., 'BCM', 'ISMS')
        dry_run: If True, only show what would be changed
    
    Returns:
        True if changes were made, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains [FRAMEWORK]
        if '[FRAMEWORK]' not in content:
            return False
        
        # Replace [FRAMEWORK] with handbook ID in document ID lines
        original_content = content
        content = re.sub(
            r'(\*\*(?:Dokument-ID|Document-ID):\*\*\s*)\[FRAMEWORK\]',
            rf'\1{handbook_id}',
            content
        )
        
        if content == original_content:
            return False
        
        if dry_run:
            print(f"Would update: {file_path}")
            # Show the changes
            for line_num, (old_line, new_line) in enumerate(zip(original_content.split('\n'), content.split('\n')), 1):
                if old_line != new_line:
                    print(f"  Line {line_num}:")
                    print(f"    - {old_line}")
                    print(f"    + {new_line}")
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {file_path}")
        
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Fix all handbook document IDs by replacing [FRAMEWORK] with uppercase handbook names'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without making actual changes'
    )
    
    args = parser.parse_args()
    
    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    templates_dir = project_root / 'templates'
    
    if not templates_dir.exists():
        print(f"Error: Templates directory not found: {templates_dir}")
        return 1
    
    total_files = 0
    updated_files = 0
    handbooks_processed = {}
    
    # Process each language
    for lang_dir in sorted(templates_dir.iterdir()):
        if not lang_dir.is_dir():
            continue
        
        language = lang_dir.name
        
        # Process each handbook
        for handbook_dir in sorted(lang_dir.iterdir()):
            if not handbook_dir.is_dir():
                continue
            
            handbook = handbook_dir.name
            
            # Get the uppercase identifier for this handbook
            handbook_id = HANDBOOK_MAPPING.get(handbook)
            if not handbook_id:
                print(f"Warning: No mapping found for handbook '{handbook}', skipping...")
                continue
            
            # Track statistics per handbook
            if handbook not in handbooks_processed:
                handbooks_processed[handbook] = {'total': 0, 'updated': 0}
            
            # Process all markdown files in this handbook
            for md_file in sorted(handbook_dir.glob('*.md')):
                total_files += 1
                handbooks_processed[handbook]['total'] += 1
                
                if fix_doc_id(md_file, handbook_id, dry_run=args.dry_run):
                    updated_files += 1
                    handbooks_processed[handbook]['updated'] += 1
    
    # Print summary
    print("\n" + "=" * 80)
    print("Summary by Handbook:")
    print("=" * 80)
    
    for handbook in sorted(handbooks_processed.keys()):
        stats = handbooks_processed[handbook]
        if stats['updated'] > 0:
            handbook_id = HANDBOOK_MAPPING.get(handbook, handbook.upper())
            print(f"  {handbook:20} ({handbook_id:20}): {stats['updated']:3} / {stats['total']:3} files {'would be ' if args.dry_run else ''}updated")
    
    print("\n" + "=" * 80)
    print(f"Overall Summary:")
    print(f"  Total files processed: {total_files}")
    print(f"  Files {'that would be ' if args.dry_run else ''}updated: {updated_files}")
    print(f"  Files unchanged: {total_files - updated_files}")
    print(f"  Handbooks affected: {len([h for h, s in handbooks_processed.items() if s['updated'] > 0])}")
    
    if args.dry_run:
        print("\nThis was a dry run. Use without --dry-run to apply changes.")
    else:
        print("\nAll changes have been applied.")
    
    return 0


if __name__ == '__main__':
    exit(main())
