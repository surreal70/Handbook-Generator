#!/usr/bin/env python3
"""
Example: Analyze Template Versions

This script demonstrates how to use the template list JSON output
to analyze template version information across all handbooks.

Usage:
    # First generate the template list
    python helpers/generate_template_list.py --source raw --output template_list.txt
    
    # Then run this analysis
    python examples/analyze_template_versions.py template_list.json
"""

import json
import sys
from collections import defaultdict
from pathlib import Path


def analyze_versions(json_file: Path):
    """Analyze template version information from JSON output."""
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("=" * 80)
    print("TEMPLATE VERSION ANALYSIS")
    print("=" * 80)
    print()
    
    # Statistics
    total_handbooks = len(data)
    total_templates = sum(len(templates) for templates in data.values())
    
    # Count templates by version status
    version_stats = defaultdict(int)
    revision_stats = defaultdict(int)
    missing_both = []
    
    for handbook, templates in data.items():
        for template in templates:
            version = template['template_version']
            revision = template['revision']
            
            # Categorize version
            if version == '[TODO]':
                version_stats['TODO'] += 1
            elif version == 'N/A':
                version_stats['N/A'] += 1
            elif '{{' in version:
                version_stats['Placeholder'] += 1
            else:
                version_stats['Set'] += 1
            
            # Categorize revision
            if revision == '[TODO]':
                revision_stats['TODO'] += 1
            elif revision == 'N/A':
                revision_stats['N/A'] += 1
            elif '{{' in revision:
                revision_stats['Placeholder'] += 1
            else:
                revision_stats['Set'] += 1
            
            # Track templates missing both
            if version == '[TODO]' and revision == '[TODO]':
                missing_both.append({
                    'handbook': handbook,
                    'filename': template['filename'],
                    'title': template['title']
                })
    
    # Print summary
    print(f"Total Handbooks: {total_handbooks}")
    print(f"Total Templates: {total_templates}")
    print()
    
    print("VERSION STATUS:")
    for status, count in sorted(version_stats.items()):
        percentage = (count / total_templates) * 100
        print(f"  {status:12} {count:5} ({percentage:5.1f}%)")
    print()
    
    print("REVISION STATUS:")
    for status, count in sorted(revision_stats.items()):
        percentage = (count / total_templates) * 100
        print(f"  {status:12} {count:5} ({percentage:5.1f}%)")
    print()
    
    # Templates needing attention
    if missing_both:
        print(f"TEMPLATES MISSING BOTH VERSION AND REVISION: {len(missing_both)}")
        print()
        
        # Group by handbook
        by_handbook = defaultdict(list)
        for item in missing_both:
            by_handbook[item['handbook']].append(item)
        
        for handbook in sorted(by_handbook.keys()):
            templates = by_handbook[handbook]
            print(f"  {handbook} ({len(templates)} templates):")
            for template in templates[:5]:  # Show first 5
                print(f"    - {template['filename']}")
            if len(templates) > 5:
                print(f"    ... and {len(templates) - 5} more")
            print()
    
    # Find handbooks with best coverage
    print("HANDBOOKS WITH COMPLETE VERSION INFO:")
    complete_handbooks = []
    for handbook, templates in data.items():
        missing = sum(1 for t in templates 
                     if t['template_version'] == '[TODO]' or t['revision'] == '[TODO]')
        if missing == 0:
            complete_handbooks.append(handbook)
    
    if complete_handbooks:
        for handbook in sorted(complete_handbooks):
            print(f"  ✓ {handbook}")
    else:
        print("  None found - all handbooks need version updates")
    print()
    
    # Recommendations
    print("RECOMMENDATIONS:")
    todo_count = version_stats['TODO'] + revision_stats['TODO']
    if todo_count > 0:
        print(f"  • Update {version_stats['TODO']} templates with [TODO] version")
        print(f"  • Update {revision_stats['TODO']} templates with [TODO] revision")
        print(f"  • Consider using a consistent versioning scheme (e.g., 1.0, 1.1, etc.)")
    else:
        print("  ✓ All templates have version information!")
    print()


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python examples/analyze_template_versions.py <template_list.json>")
        print()
        print("First generate the template list:")
        print("  python helpers/generate_template_list.py --source raw --output template_list.txt")
        sys.exit(1)
    
    json_file = Path(sys.argv[1])
    
    if not json_file.exists():
        print(f"Error: File not found: {json_file}")
        sys.exit(1)
    
    analyze_versions(json_file)


if __name__ == '__main__':
    main()
