#!/usr/bin/env python3
"""
Update Template References to Removed Roles

This script scans all template files for references to the removed
datenschutzbeauftragter role and replaces them with data_protection_officer.

Usage:
    python examples/update_role_references.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataRoleCleanup


def main():
    """Update template references to removed roles."""
    print("=" * 70)
    print("Update Template References to Removed Roles")
    print("=" * 70)
    print()
    
    # Initialize role cleanup
    cleanup = MetadataRoleCleanup('metadata.example.yaml')
    
    # Update references
    print("Step 1: Scanning templates for datenschutzbeauftragter references...")
    print("  Pattern: {{ meta.datenschutzbeauftragter.* }}")
    print("  Replacement: {{ meta.data_protection_officer.* }}")
    print()
    
    files_updated = cleanup.update_template_references(
        old_role='datenschutzbeauftragter',
        new_role='data_protection_officer',
        templates_dir='templates'
    )
    
    print()
    print(f"Step 2: Summary")
    print(f"  Files updated: {files_updated}")
    print()
    
    if files_updated > 0:
        print("=" * 70)
        print(f"✓ Successfully updated {files_updated} template file(s)")
        print("=" * 70)
    else:
        print("=" * 70)
        print("✓ No template files needed updating")
        print("=" * 70)
        print()
        print("This is expected if:")
        print("  - No templates reference datenschutzbeauftragter")
        print("  - All templates already use data_protection_officer")


if __name__ == '__main__':
    main()
