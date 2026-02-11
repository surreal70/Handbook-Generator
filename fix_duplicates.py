#!/usr/bin/env python3
"""
Fix duplicate template numbers by removing duplicates and keeping the first occurrence.
"""

import os
from pathlib import Path
from collections import defaultdict

def fix_duplicates_in_framework(framework_id, lang='de'):
    """Fix duplicate template numbers in a framework."""
    template_dir = Path(f'templates/{lang}/{framework_id}')
    if not template_dir.exists():
        return 0
    
    # Group files by their number
    number_to_files = defaultdict(list)
    
    for filename in os.listdir(template_dir):
        if filename.endswith('.md') and filename[0].isdigit() and not filename.startswith('0000'):
            number = int(filename.split('_')[0])
            number_to_files[number].append(filename)
    
    # Find and remove duplicates
    removed_count = 0
    for number, files in number_to_files.items():
        if len(files) > 1:
            print(f"  Found {len(files)} files with number {number:04d}:")
            # Keep the first one, remove others
            for i, filename in enumerate(files):
                if i == 0:
                    print(f"    KEEP: {filename}")
                else:
                    filepath = template_dir / filename
                    print(f"    REMOVE: {filename}")
                    filepath.unlink()
                    removed_count += 1
    
    return removed_count

def main():
    """Main execution."""
    print("=" * 80)
    print("FIXING DUPLICATE TEMPLATE NUMBERS")
    print("=" * 80)
    
    frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
    total_removed = 0
    
    for framework in frameworks:
        print(f"\n{framework}:")
        for lang in ['de', 'en']:
            print(f"  {lang}:")
            removed = fix_duplicates_in_framework(framework, lang)
            if removed == 0:
                print(f"    No duplicates found")
            total_removed += removed
    
    print("\n" + "=" * 80)
    print(f"COMPLETE: Removed {total_removed} duplicate files")
    print("=" * 80)

if __name__ == '__main__':
    main()
