#!/usr/bin/env python3
"""
Remove Duplicate datenschutzbeauftragter Role

This script removes the duplicate datenschutzbeauftragter role from
metadata.example.yaml, as it duplicates the data_protection_officer role.

Usage:
    python examples/remove_duplicate_role.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataRoleCleanup


def main():
    """Remove duplicate datenschutzbeauftragter role."""
    print("=" * 70)
    print("Remove Duplicate datenschutzbeauftragter Role")
    print("=" * 70)
    print()
    
    # Initialize role cleanup
    cleanup = MetadataRoleCleanup('metadata.example.yaml')
    
    # Detect duplicates
    print("Step 1: Detecting duplicate roles...")
    duplicates = cleanup.detect_duplicate_roles()
    
    if not duplicates:
        print("✓ No duplicate roles found")
        return
    
    print(f"Found {len(duplicates)} duplicate role(s):")
    for dup in duplicates:
        print(f"  - {dup.role_name} (duplicate of {dup.canonical_role})")
        print(f"    Reason: {dup.reason}")
    print()
    
    # Verify data_protection_officer exists
    print("Step 2: Verifying data_protection_officer role exists...")
    try:
        import yaml
        with open('metadata.example.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if 'data_protection_officer' in data.get('roles', {}):
            print("✓ data_protection_officer role exists")
        else:
            print("✗ ERROR: data_protection_officer role not found!")
            print("  Cannot remove datenschutzbeauftragter without canonical role")
            return
    except Exception as e:
        print(f"✗ ERROR: Could not verify roles: {e}")
        return
    print()
    
    # Remove duplicate role
    print("Step 3: Removing datenschutzbeauftragter role...")
    success = cleanup.remove_duplicate_role('datenschutzbeauftragter')
    
    if success:
        print("✓ Successfully removed datenschutzbeauftragter role")
    else:
        print("✗ Failed to remove datenschutzbeauftragter role")
        return
    print()
    
    # Verify removal
    print("Step 4: Verifying removal...")
    try:
        with open('metadata.example.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        roles = data.get('roles', {})
        
        if 'datenschutzbeauftragter' not in roles:
            print("✓ datenschutzbeauftragter role successfully removed")
        else:
            print("✗ ERROR: datenschutzbeauftragter role still present!")
            return
        
        if 'data_protection_officer' in roles:
            print("✓ data_protection_officer role still present")
        else:
            print("✗ ERROR: data_protection_officer role was removed!")
            return
    except Exception as e:
        print(f"✗ ERROR: Could not verify removal: {e}")
        return
    print()
    
    print("=" * 70)
    print("✓ Duplicate role removal completed successfully")
    print("=" * 70)
    print()
    print("Next steps:")
    print("  1. Update template references using examples/update_role_references.py")
    print("  2. Reorganize IT operations roles using examples/reorganize_it_roles.py")


if __name__ == '__main__':
    main()
