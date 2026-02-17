#!/usr/bin/env python3
"""
Script to clean up duplicate headers in template files.
"""

import re
from pathlib import Path


def clean_duplicate_headers(content: str) -> str:
    """Remove duplicate headers, keeping only the first one."""
    lines = content.split('\n')
    
    # Find the title
    title_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title_idx = i
            break
    
    if title_idx < 0:
        return content
    
    # Find all header blocks (lines starting with **)
    header_blocks = []
    i = title_idx + 1
    while i < len(lines):
        if lines[i].strip().startswith('**'):
            # Found start of a header block
            block_start = i
            block_end = i
            while block_end < len(lines) and (lines[block_end].strip().startswith('**') or lines[block_end].strip() == ''):
                block_end += 1
            header_blocks.append((block_start, block_end))
            i = block_end
        elif lines[i].strip() == '---':
            i += 1
        elif lines[i].strip().startswith('<!--') or lines[i].strip().startswith('##'):
            # Reached content, stop looking
            break
        else:
            i += 1
    
    # If we found multiple header blocks, keep only the first
    if len(header_blocks) > 1:
        # Remove all but the first header block
        for block_start, block_end in reversed(header_blocks[1:]):
            del lines[block_start:block_end]
    
    # Clean up multiple consecutive separators
    result = []
    prev_was_sep = False
    for line in lines:
        if line.strip() == '---':
            if not prev_was_sep:
                result.append(line)
                prev_was_sep = True
        else:
            result.append(line)
            prev_was_sep = False
    
    # Clean up multiple blank lines
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
        cleaned = clean_duplicate_headers(content)
        
        if cleaned != content:
            file_path.write_text(cleaned, encoding='utf-8')
            print(f"  Cleaned {file_path.name}")
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
    
    print(f"\nCleaned {cleaned_count} files")


if __name__ == '__main__':
    main()
