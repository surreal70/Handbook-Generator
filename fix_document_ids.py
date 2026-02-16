#!/usr/bin/env python3
"""
Script to add Document-ID metadata to templates that are missing it.

This script:
1. Scans all template files
2. Checks if Document-ID exists in metadata
3. Adds Document-ID matching the filename if missing
"""

import re
from pathlib import Path
from typing import Optional


def extract_document_id_from_content(content: str) -> Optional[str]:
    """Extract existing Document-ID from content"""
    match = re.search(r'Document-ID:\s*([^\s\n]+)', content)
    return match.group(1) if match else None


def add_document_id_to_template(file_path: Path, dry_run: bool = True) -> bool:
    """Add Document-ID to template if missing"""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Skip if already has Document-ID
        if extract_document_id_from_content(content):
            return False
        
        # Get expected Document-ID from filename
        expected_id = file_path.stem
        
        # Check if file has metadata section with ---
        if content.startswith('---'):
            # Find the end of metadata section
            end_match = re.search(r'\n---\n', content[3:])
            if end_match:
                # Insert Document-ID at the beginning of metadata
                insert_pos = 4  # After first ---\n
                new_content = (
                    content[:insert_pos] +
                    f'Document-ID: {expected_id}\n' +
                    content[insert_pos:]
                )
                
                if not dry_run:
                    file_path.write_text(new_content, encoding='utf-8')
                
                print(f"✓ Added Document-ID to {file_path.relative_to(Path('.'))}")
                return True
        
        # If no metadata section, check if there's any metadata-like content
        # Look for patterns like "Title:", "Version:", etc. in first 500 chars
        metadata_pattern = r'^(Title|Version|Last Updated|Author|Classification):'
        if re.search(metadata_pattern, content[:500], re.MULTILINE):
            # Add Document-ID at the very beginning
            new_content = f'Document-ID: {expected_id}\n' + content
            
            if not dry_run:
                file_path.write_text(new_content, encoding='utf-8')
            
            print(f"✓ Added Document-ID to {file_path.relative_to(Path('.'))}")
            return True
        
        # If no metadata at all, add a basic metadata section
        new_content = f'''---
Document-ID: {expected_id}
---

{content}'''
        
        if not dry_run:
            file_path.write_text(new_content, encoding='utf-8')
        
        print(f"✓ Added Document-ID with metadata section to {file_path.relative_to(Path('.'))}")
        return True
    
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Add Document-ID to templates')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('--framework', help='Only process specific framework')
    args = parser.parse_args()
    
    templates_path = Path('templates')
    
    if not templates_path.exists():
        print("Error: templates/ directory not found")
        return 1
    
    total_processed = 0
    total_updated = 0
    
    for lang in ['de', 'en']:
        lang_path = templates_path / lang
        if not lang_path.exists():
            continue
        
        for framework_dir in lang_path.iterdir():
            if not framework_dir.is_dir():
                continue
            
            # Skip if specific framework requested and this isn't it
            if args.framework and framework_dir.name != args.framework:
                continue
            
            print(f"\nProcessing {lang}/{framework_dir.name}...")
            
            for template_file in framework_dir.glob("*.md"):
                # Skip metadata and README files
                if template_file.name in ['metadata.yaml', 'README.md']:
                    continue
                
                total_processed += 1
                
                if add_document_id_to_template(template_file, dry_run=args.dry_run):
                    total_updated += 1
    
    print(f"\n{'=' * 80}")
    print(f"Summary:")
    print(f"  Total templates processed: {total_processed}")
    print(f"  Templates updated: {total_updated}")
    
    if args.dry_run:
        print(f"\nDRY RUN - No changes were made")
        print(f"Run without --dry-run to apply changes")
    
    return 0


if __name__ == '__main__':
    exit(main())
