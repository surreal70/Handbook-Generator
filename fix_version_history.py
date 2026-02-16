#!/usr/bin/env python3
"""
Script to add version history sections to templates that are missing them.

This script:
1. Scans all template files
2. Checks if version history section exists
3. Adds standard version history section if missing
"""

import re
from pathlib import Path
from datetime import datetime


def has_version_history(content: str) -> bool:
    """Check if content has version history section"""
    patterns = [
        r'## Version History',
        r'## Versionshistorie',
        r'## Document History',
        r'## Dokumentenhistorie'
    ]
    
    return any(re.search(pattern, content) for pattern in patterns)


def add_version_history_to_template(file_path: Path, dry_run: bool = True) -> bool:
    """Add version history section to template if missing"""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Skip if already has version history
        if has_version_history(content):
            return False
        
        # Determine language from path
        is_german = '/de/' in str(file_path)
        
        # Create version history section
        if is_german:
            version_section = '''

## Versionshistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 2026-02-16 | Quality Control System | Initiale Version |
'''
        else:
            version_section = '''

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-02-16 | Quality Control System | Initial version |
'''
        
        # Add version history at the end of the document
        new_content = content.rstrip() + version_section
        
        if not dry_run:
            file_path.write_text(new_content, encoding='utf-8')
        
        print(f"✓ Added version history to {file_path.relative_to(Path('.'))}")
        return True
    
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Add version history to templates')
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
                
                if add_version_history_to_template(template_file, dry_run=args.dry_run):
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
