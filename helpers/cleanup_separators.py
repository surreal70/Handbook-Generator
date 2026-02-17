#!/usr/bin/env python3
"""
Script to clean up multiple consecutive separators in template files.
"""

import re
from pathlib import Path


def clean_separators(content: str) -> str:
    """Clean up multiple consecutive separators."""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a separator
        if line.strip() == '---':
            # Add this separator
            result.append(line)
            i += 1
            
            # Skip any blank lines and additional separators
            while i < len(lines) and (lines[i].strip() == '' or lines[i].strip() == '---'):
                if lines[i].strip() == '---':
                    # Skip duplicate separator
                    pass
                else:
                    # Keep blank line after separator
                    if len(result) == 0 or result[-1].strip() != '':
                        result.append(lines[i])
                i += 1
        else:
            result.append(line)
            i += 1
    
    # Clean up excessive blank lines (more than 2 consecutive)
    final = []
    blank_count = 0
    for line in result:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                final.append(line)
        else:
            blank_count = 0
            final.append(line)
    
    return '\n'.join(final)


def process_file(file_path: Path):
    """Process a single file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        cleaned = clean_separators(content)
        
        if cleaned != content:
            file_path.write_text(cleaned, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"  Error processing {file_path.name}: {e}")
        return False


def main():
    """Main entry point."""
    templates_dir = Path('templates')
    
    cleaned_count = 0
    
    # Process all markdown files
    for md_file in templates_dir.rglob('*.md'):
        if md_file.name.startswith('0000_metadata') or md_file.name == 'README.md':
            continue
        
        if process_file(md_file):
            cleaned_count += 1
    
    print(f"Cleaned {cleaned_count} files")


if __name__ == '__main__':
    main()
