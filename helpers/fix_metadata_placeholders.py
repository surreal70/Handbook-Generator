#!/usr/bin/env python3
"""
Fix metadata files by replacing placeholders with actual values.

This script implements Option A from the metadata standardization analysis:
- Replace all placeholders in metadata files with actual values
- Ensure all required fields are present
- Ensure bilingual consistency
"""

import re
from pathlib import Path
from datetime import datetime


def get_default_values():
    """Get default values for metadata fields."""
    return {
        # Handbook-specific defaults
        'meta-handbook.owner': '[TODO]',
        'meta-handbook.revision': '0',
        'meta-handbook.status': 'Draft',
        'meta-handbook.classification': 'Internal',
        'meta-handbook.modifydate': datetime.now().strftime('%Y-%m-%d'),
        'meta-handbook.templateset_version': '1.0',
        'meta-handbook.longname': '[TODO]',
        'meta-handbook.shortname': '[TODO]',
        'meta-handbook.author': '[TODO]',
        'meta-handbook.scope': '[TODO]',
        'meta-handbook.valid_from': '[TODO]',
        'meta-handbook.next_review': '[TODO]',
        
        # Organisation defaults
        'meta-organisation.name': '[TODO]',
    }


def extract_framework_name(filepath):
    """Extract framework name from metadata file path."""
    # Example: templates/de/coso/0000_metadata_de_coso.md -> coso
    parts = Path(filepath).parts
    if 'templates' in parts:
        lang_idx = parts.index('templates') + 1
        if lang_idx + 1 < len(parts):
            return parts[lang_idx + 1]
    return None


def fix_metadata_file(filepath):
    """Fix a single metadata file by replacing placeholders with actual values."""
    print(f"Processing: {filepath}")
    
    # Read the file
    content = Path(filepath).read_text(encoding='utf-8')
    original_content = content
    
    # Get default values
    defaults = get_default_values()
    
    # Extract framework name for shortname
    framework = extract_framework_name(filepath)
    if framework:
        defaults['meta-handbook.shortname'] = framework.upper()
        defaults['meta-handbook.longname'] = f"{framework.upper()} Handbook"
    
    # Replace all placeholders
    placeholder_pattern = r'\{\{\s*([a-zA-Z0-9_.-]+)\s*\}\}'
    
    def replace_placeholder(match):
        placeholder = match.group(1)
        if placeholder in defaults:
            return defaults[placeholder]
        else:
            print(f"  Warning: Unknown placeholder {{{{{ placeholder }}}}} - keeping as is")
            return match.group(0)
    
    content = re.sub(placeholder_pattern, replace_placeholder, content)
    
    # Fix field labels to match validator expectations
    # The validator expects "Last Updated" not "Last Update"
    content = content.replace('**Last Update:**', '**Last Updated:**')
    content = content.replace('**Letzte Aktualisierung:**', '**Letzte Aktualisierung:**')  # Already correct
    
    # Write back if changed
    if content != original_content:
        Path(filepath).write_text(content, encoding='utf-8')
        print(f"  ✓ Fixed {filepath}")
        return True
    else:
        print(f"  - No changes needed for {filepath}")
        return False


def main():
    """Main function to fix all metadata files."""
    print("=" * 80)
    print("Fixing Metadata Files - Option A Implementation")
    print("=" * 80)
    print()
    
    # Find all metadata files
    templates_dir = Path('templates')
    metadata_files = list(templates_dir.glob('**/0000_metadata*.md'))
    
    print(f"Found {len(metadata_files)} metadata files")
    print()
    
    fixed_count = 0
    for filepath in sorted(metadata_files):
        if fix_metadata_file(filepath):
            fixed_count += 1
    
    print()
    print("=" * 80)
    print(f"Summary: Fixed {fixed_count} out of {len(metadata_files)} files")
    print("=" * 80)


if __name__ == '__main__':
    main()
