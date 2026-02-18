#!/usr/bin/env python3
"""
Add Template Version field to template headers.

This script adds a **Template Version:** field to all template files,
excluding metadata files (0000_*) and README files.
"""

import re
from pathlib import Path
from typing import List, Tuple


def should_process_file(filepath: Path) -> bool:
    """
    Determine if a file should be processed.
    
    Args:
        filepath: Path to the file
        
    Returns:
        True if file should be processed, False otherwise
    """
    filename = filepath.name
    
    # Skip metadata files
    if filename.startswith('0000_'):
        return False
    
    # Skip README files
    if filename.upper().startswith('README'):
        return False
    
    # Only process .md files
    if not filename.endswith('.md'):
        return False
    
    return True


def has_template_version_field(content: str) -> bool:
    """
    Check if content already has a Template Version field.
    
    Args:
        content: File content
        
    Returns:
        True if Template Version field exists
    """
    return bool(re.search(r'\*\*Template Version:\*\*', content, re.IGNORECASE))


def add_template_version_field(content: str) -> Tuple[str, bool]:
    """
    Add Template Version field to template header and set Revision to [TODO].
    
    The field is added after the header metadata section, typically after
    **Letzte Aktualisierung:** or **Last Update:** field.
    
    Both Template Version and Revision are set to [TODO] for template files.
    
    Args:
        content: Original file content
        
    Returns:
        Tuple of (modified content, was_modified)
    """
    modified = False
    modified_content = content
    
    # Step 1: Change Revision field to [TODO] if it uses placeholder
    revision_patterns = [
        # German: Revision with placeholder
        (r'\*\*Revision:\*\* \{\{ meta-handbook\.revision \}\}',
         r'**Revision:** [TODO]'),
        
        # English: Revision with placeholder
        (r'\*\*Revision:\*\* \{\{ meta-handbook\.revision \}\}',
         r'**Revision:** [TODO]'),
    ]
    
    for pattern, replacement in revision_patterns:
        if re.search(pattern, modified_content):
            modified_content = re.sub(pattern, replacement, modified_content)
            modified = True
            break
    
    # Step 2: Check if already has Template Version field
    if has_template_version_field(modified_content):
        return modified_content, modified
    
    # Step 3: Add Template Version field after the last metadata field
    # Look for common last fields in both German and English
    patterns = [
        # German: Letzte Aktualisierung
        (r'(\*\*Letzte Aktualisierung:\*\* \{\{ meta-handbook\.modifydate \}\})\n',
         r'\1\n**Template Version:** [TODO]\n'),
        
        # English: Last Update
        (r'(\*\*Last Update:\*\* \{\{ meta-handbook\.modifydate \}\})\n',
         r'\1\n**Template Version:** [TODO]\n'),
        
        # Fallback: After Classification field (German)
        (r'(\*\*Klassifizierung:\*\* \{\{ meta-handbook\.classification \}\})\n',
         r'\1\n**Template Version:** [TODO]\n'),
        
        # Fallback: After Classification field (English)
        (r'(\*\*Classification:\*\* \{\{ meta-handbook\.classification \}\})\n',
         r'\1\n**Template Version:** [TODO]\n'),
    ]
    
    # Try each pattern
    for pattern, replacement in patterns:
        if re.search(pattern, modified_content):
            modified_content = re.sub(pattern, replacement, modified_content, count=1)
            modified = True
            break
    
    return modified_content, modified


def process_template_file(filepath: Path, dry_run: bool = False) -> Tuple[bool, str]:
    """
    Process a single template file.
    
    Args:
        filepath: Path to template file
        dry_run: If True, don't write changes
        
    Returns:
        Tuple of (was_modified, message)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified_content, was_modified = add_template_version_field(content)
        
        if was_modified:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                return True, f"✓ Updated (Template Version + Revision set to [TODO])"
            else:
                return True, f"✓ Would update (Template Version + Revision to [TODO]) (dry run)"
        else:
            return False, "○ Already has Template Version field or no suitable location found"
            
    except Exception as e:
        return False, f"✗ Error: {e}"


def process_templates(templates_dir: Path = Path('templates'), 
                     dry_run: bool = False) -> None:
    """
    Process all template files in the templates directory.
    
    Args:
        templates_dir: Path to templates directory
        dry_run: If True, don't write changes
    """
    if not templates_dir.exists():
        print(f"Error: Templates directory not found: {templates_dir}")
        return
    
    # Statistics
    total_files = 0
    modified_files = 0
    skipped_files = 0
    error_files = 0
    
    # Process all .md files recursively
    for filepath in sorted(templates_dir.rglob('*.md')):
        if not should_process_file(filepath):
            skipped_files += 1
            continue
        
        total_files += 1
        relative_path = filepath.relative_to(templates_dir)
        
        was_modified, message = process_template_file(filepath, dry_run)
        
        if was_modified:
            modified_files += 1
            print(f"{relative_path}: {message}")
        elif "Error" in message:
            error_files += 1
            print(f"{relative_path}: {message}")
    
    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total template files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Files skipped (metadata/README): {skipped_files}")
    print(f"Errors: {error_files}")
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No files were actually modified")
        print("Run without --dry-run to apply changes")


def main():
    """Main execution function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Add Template Version field to template headers'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--templates-dir',
        type=Path,
        default=Path('templates'),
        help='Path to templates directory (default: templates)'
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("Add Template Version Field to Templates")
    print("=" * 80)
    print(f"Templates directory: {args.templates_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print("=" * 80)
    print()
    
    process_templates(args.templates_dir, args.dry_run)


if __name__ == '__main__':
    main()
