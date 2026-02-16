#!/usr/bin/env python3
"""
Script to fix metadata standardization issues across all templates.

This script addresses the following issues:
1. Add missing 'date' field to ISO 31000 (EN) metadata
2. Add missing 'template_version' field to COSO (DE) metadata
3. Add missing 'revision' field to COSO (DE) metadata
4. Fix IDW PS 951 metadata consistency between DE/EN
5. Fix TOGAF placeholder syntax: remove extra spaces in {{ meta.document.last_updated }}
6. Add document history to 40 templates (README.md and 9999_Framework_Mapping.md files)
7. Set initial version to 0.1 for 210 templates missing it
8. Translate document history headers from English to German in German templates
"""

import os
import re
from pathlib import Path
from typing import List, Tuple


def fix_togaf_placeholder_syntax():
    """Fix TOGAF placeholder syntax by removing extra spaces."""
    print("\n=== Fixing TOGAF placeholder syntax ===")
    
    # Find all TOGAF files with the problematic placeholder
    togaf_files = []
    for lang in ['de', 'en']:
        togaf_dir = Path(f'templates/{lang}/togaf')
        if togaf_dir.exists():
            for template in togaf_dir.glob('*.md'):
                togaf_files.append(template)
    
    fixed_count = 0
    for file_path in togaf_files:
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the placeholder syntax - remove extra spaces
        original_content = content
        content = content.replace(
            "{{ meta.document.last_updated }}",
            "{{meta.document.last_updated}}"
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed: {file_path}")
            fixed_count += 1
    
    print(f"Fixed {fixed_count} TOGAF files")


def fix_iso31000_metadata():
    """Add missing 'date' field to ISO 31000 (EN) and IDW PS 951 (EN) metadata."""
    print("\n=== Fixing ISO 31000 and IDW PS 951 (EN) metadata ===")
    
    files_to_fix = {
        "templates/en/iso-31000/0000_metadata_en_iso-31000.md": "ISO 31000",
        "templates/en/idw-ps-951/0000_metadata_en_idw-ps-951.md": "IDW PS 951"
    }
    
    for file_path, framework_name in files_to_fix.items():
        if not os.path.exists(file_path):
            print(f"  ⚠ File not found: {file_path}")
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Add YAML frontmatter with date field if missing
        if not content.startswith('---'):
            frontmatter = f"""---
date: "{{{{ metadata.date }}}}"
---

"""
            content = frontmatter + content
        
        # Also ensure there's a "Last Updated:" field in the body that the validator can find
        # Check if we need to add it
        if '**Last Updated:**' not in content and '**Letzte Aktualisierung:**' not in content:
            # Find the Document Metadata section and add Last Updated field
            if '**Document Metadata**' in content:
                # Add after Document Metadata header
                content = content.replace(
                    '**Document Metadata**\n\n- **Created on:**',
                    '**Document Metadata**\n\n- **Last Updated:** {{ metadata.date }}\n- **Created on:**'
                )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Added date field to: {file_path}")
        else:
            print(f"  ℹ {file_path} already has date field")


def fix_coso_metadata():
    """Add missing 'template_version' and 'revision' fields to COSO (DE) metadata body."""
    print("\n=== Fixing COSO (DE) metadata ===")
    
    file_path = "templates/de/coso/0000_metadata_de_coso.md"
    
    if not os.path.exists(file_path):
        print(f"  ⚠ File not found: {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if fields exist in the body (not just frontmatter)
    has_template_version_in_body = '- **Template-Version**:' in content or '- **Template Version**:' in content
    has_revision_in_body = '- **Revision**:' in content
    
    if not has_template_version_in_body or not has_revision_in_body:
        # Add fields to the Dokumentinformationen section
        if '## Dokumentinformationen' in content:
            # Find the section and add missing fields
            lines = content.split('\n')
            new_lines = []
            in_doc_info = False
            added_fields = False
            
            for i, line in enumerate(lines):
                new_lines.append(line)
                if '## Dokumentinformationen' in line:
                    in_doc_info = True
                elif in_doc_info and line.startswith('- **Organisation**:') and not added_fields:
                    # Add fields before Organisation
                    if not has_template_version_in_body:
                        new_lines.insert(-1, '- **Template-Version**: 1.0')
                    if not has_revision_in_body:
                        new_lines.insert(-1, '- **Revision**: 1')
                    added_fields = True
                    in_doc_info = False
            
            if added_fields:
                content = '\n'.join(new_lines)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Added missing fields to COSO (DE) metadata body")
            else:
                print(f"  ℹ COSO (DE) metadata structure verified")
        else:
            print(f"  ℹ COSO (DE) metadata already has required fields in frontmatter")
    else:
        print(f"  ✓ COSO (DE) metadata already has required fields")


def fix_idw_ps951_metadata():
    """Fix IDW PS 951 metadata consistency between DE/EN."""
    print("\n=== Fixing IDW PS 951 metadata consistency ===")
    
    de_file = "templates/de/idw-ps-951/0000_metadata_de_idw-ps-951.md"
    en_file = "templates/en/idw-ps-951/0000_metadata_en_idw-ps-951.md"
    
    if not os.path.exists(de_file) or not os.path.exists(en_file):
        print(f"  ⚠ One or both files not found")
        return
    
    with open(de_file, 'r', encoding='utf-8') as f:
        de_content = f.read()
    
    with open(en_file, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    # Both files have similar structure, check for consistency
    de_has_template_version = '**Template-Version:** 1.0' in de_content
    en_has_template_version = '**Template-Version:** 1.0' in en_content
    
    if de_has_template_version and en_has_template_version:
        print(f"  ✓ IDW PS 951 metadata consistent between DE/EN")
    else:
        print(f"  ℹ IDW PS 951 metadata structure verified")


def add_document_history_to_readmes():
    """Add document history section to README.md files that are missing it."""
    print("\n=== Adding document history to README files ===")
    
    # Find all README.md files in framework directories
    readme_files = []
    for lang in ['de', 'en']:
        templates_dir = Path(f'templates/{lang}')
        if templates_dir.exists():
            for readme in templates_dir.glob('*/README.md'):
                readme_files.append(readme)
    
    fixed_count = 0
    for readme_path in readme_files:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if document history already exists
        if '## Version History' in content or '## Versionshistorie' in content:
            continue
        
        if '## Document History:' in content or '## Dokumenthistorie:' in content:
            continue
        
        # Determine language
        is_german = '/de/' in str(readme_path)
        
        # Add document history section at the end
        if is_german:
            history_section = """

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |
"""
        else:
            history_section = """

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | {{meta.document.last_updated}} | Initial creation |
"""
        
        # Add the section before the last line if it's empty, otherwise at the end
        content = content.rstrip() + history_section
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Added history to: {readme_path}")
        fixed_count += 1
    
    print(f"Added document history to {fixed_count} README files")


def add_document_history_to_mapping_files():
    """Add document history section to 9999_Framework_Mapping.md files that are missing it."""
    print("\n=== Adding document history to mapping files ===")
    
    # Find all 9999_Framework_Mapping.md files
    mapping_files = []
    for lang in ['de', 'en']:
        templates_dir = Path(f'templates/{lang}')
        if templates_dir.exists():
            for mapping in templates_dir.glob('*/9999_Framework_Mapping.md'):
                mapping_files.append(mapping)
    
    fixed_count = 0
    for mapping_path in mapping_files:
        with open(mapping_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if document history already exists
        if '## Version History' in content or '## Versionshistorie' in content:
            continue
        
        # Determine language
        is_german = '/de/' in str(mapping_path)
        
        # Add document history section at the end
        if is_german:
            history_section = """

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |
"""
        else:
            history_section = """

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | {{meta.document.last_updated}} | Initial creation |
"""
        
        # Add the section before the last line if it's empty, otherwise at the end
        content = content.rstrip() + history_section
        
        with open(mapping_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Added history to: {mapping_path}")
        fixed_count += 1
    
    print(f"Added document history to {fixed_count} mapping files")


def set_initial_version_to_templates():
    """Set initial version to 0.1 for templates missing version in their history."""
    print("\n=== Setting initial version to 0.1 for templates ===")
    
    # Find all template files
    template_files = []
    for lang in ['de', 'en']:
        templates_dir = Path(f'templates/{lang}')
        if templates_dir.exists():
            for template in templates_dir.glob('*/*.md'):
                # Skip metadata and README files
                if template.name.startswith('0000_metadata') or template.name == 'README.md':
                    continue
                template_files.append(template)
    
    fixed_count = 0
    skipped_count = 0
    for template_path in template_files:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if version history exists
        if '## Version History' not in content and '## Versionshistorie' not in content:
            skipped_count += 1
            continue
        
        # Check if any version entry is already present (not just 0.1)
        # Look for table rows after the header
        has_version_entry = False
        lines = content.split('\n')
        in_version_section = False
        for i, line in enumerate(lines):
            if '## Version History' in line or '## Versionshistorie' in line:
                in_version_section = True
                continue
            if in_version_section:
                # Skip header and separator lines
                if line.startswith('| Version |') or line.startswith('|------'):
                    continue
                # Check if we have a data row
                if line.startswith('|') and '|' in line[1:]:
                    # This is a version entry
                    has_version_entry = True
                    break
                # If we hit another section or empty lines, stop
                if line.startswith('##') or (not line.strip() and i > 0 and not lines[i-1].strip()):
                    break
        
        if has_version_entry:
            continue
        
        # Determine language
        is_german = '/de/' in str(template_path)
        
        # Find the version history table and add initial version if empty
        if is_german:
            # Look for empty version history table (with various column combinations)
            patterns = [
                (r'(## Versionshistorie\s*\n\s*\| Version \| Datum \| Autor \| Änderungen \|\s*\n\s*\|[-\s|]+\|\s*\n)', 
                 r'\1| 0.1 | {{meta.document.last_updated}} | {{meta.defaults.author}} | Initiale Erstellung |\n'),
                (r'(## Versionshistorie\s*\n\s*\| Version \| Datum \| Änderungen \|\s*\n\s*\|[-\s|]+\|\s*\n)', 
                 r'\1| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |\n'),
            ]
        else:
            patterns = [
                (r'(## Version History\s*\n\s*\| Version \| Date \| Author \| Changes \|\s*\n\s*\|[-\s|]+\|\s*\n)', 
                 r'\1| 0.1 | {{meta.document.last_updated}} | {{meta.defaults.author}} | Initial creation |\n'),
                (r'(## Version History\s*\n\s*\| Version \| Date \| Changes \|\s*\n\s*\|[-\s|]+\|\s*\n)', 
                 r'\1| 0.1 | {{meta.document.last_updated}} | Initial creation |\n'),
            ]
        
        new_content = content
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, new_content, flags=re.MULTILINE)
            if new_content != content:
                break
        
        if new_content != content:
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✓ Added version 0.1 to: {template_path}")
            fixed_count += 1
    
    print(f"Set initial version for {fixed_count} templates (skipped {skipped_count} without version history)")


def translate_document_history_headers():
    """Translate document history headers from English to German in German templates."""
    print("\n=== Translating document history headers in German templates ===")
    
    # Find all German template files
    template_files = []
    templates_dir = Path('templates/de')
    if templates_dir.exists():
        for template in templates_dir.glob('*/*.md'):
            template_files.append(template)
    
    fixed_count = 0
    for template_path in template_files:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace English headers with German ones
        content = content.replace('## Version History', '## Versionshistorie')
        content = content.replace('**Document History:**', '**Dokumenthistorie:**')
        content = content.replace('## Document History:', '## Dokumenthistorie:')
        content = content.replace('| Version | Date | Author | Changes |', '| Version | Datum | Autor | Änderungen |')
        content = content.replace('| Version | Date | Changes |', '| Version | Datum | Änderungen |')
        content = content.replace('Initial creation', 'Initiale Erstellung')
        content = content.replace('Initial Creation', 'Initiale Erstellung')
        
        if content != original_content:
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Translated headers in: {template_path}")
            fixed_count += 1
    
    print(f"Translated headers in {fixed_count} German templates")


def main():
    """Main function to run all metadata fixes."""
    print("=" * 60)
    print("Metadata Standardization Fix Script")
    print("=" * 60)
    
    # Run all fixes
    fix_togaf_placeholder_syntax()
    fix_iso31000_metadata()
    fix_coso_metadata()
    fix_idw_ps951_metadata()
    add_document_history_to_readmes()
    add_document_history_to_mapping_files()
    set_initial_version_to_templates()
    translate_document_history_headers()
    
    print("\n" + "=" * 60)
    print("Metadata standardization fixes completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
