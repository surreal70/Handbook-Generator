#!/usr/bin/env python3
"""
Reorganize IT Operations Roles

This script moves it_manager and sysop from "Add Custom Roles Here" section
to "IT Operations Roles" section in metadata.example.yaml.

Usage:
    python examples/reorganize_it_roles.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataRoleCleanup


def main():
    """Reorganize IT operations roles."""
    print("=" * 70)
    print("Reorganize IT Operations Roles")
    print("=" * 70)
    print()
    
    # Initialize role cleanup
    cleanup = MetadataRoleCleanup('metadata.example.yaml')
    
    # Check current structure
    print("Step 1: Validating current role structure...")
    validation = cleanup.validate_role_structure()
    
    if validation.warnings:
        print("Current issues found:")
        for warning in validation.warnings:
            print(f"  ⚠ {warning}")
    else:
        print("✓ No structural issues found")
    print()
    
    # Reorganize roles
    print("Step 2: Reorganizing IT operations roles...")
    print("  Moving it_manager to IT Operations Roles section")
    print("  Moving sysop to IT Operations Roles section")
    
    success = cleanup.reorganize_it_operations_roles()
    
    if success:
        print("✓ Successfully reorganized IT operations roles")
    else:
        print("✗ Failed to reorganize IT operations roles")
        return
    print()
    
    # Verify reorganization
    print("Step 3: Verifying reorganization...")
    try:
        import yaml
        with open('metadata.example.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        roles = data.get('roles', {})
        role_names = list(roles.keys())
        
        # Check if roles exist
        if 'it_manager' not in role_names:
            print("✗ ERROR: it_manager role not found!")
            return
        
        if 'sysop' not in role_names:
            print("✗ ERROR: sysop role not found!")
            return
        
        # Check ordering
        if 'service_desk_lead' in role_names:
            service_desk_idx = role_names.index('service_desk_lead')
            it_manager_idx = role_names.index('it_manager')
            sysop_idx = role_names.index('sysop')
            
            if it_manager_idx > service_desk_idx and sysop_idx > service_desk_idx:
                print("✓ it_manager and sysop are in IT Operations Roles section")
                print(f"  Role order: service_desk_lead (#{service_desk_idx}) → it_manager (#{it_manager_idx}) → sysop (#{sysop_idx})")
            else:
                print("✗ ERROR: Roles not in correct order!")
                print(f"  service_desk_lead: #{service_desk_idx}")
                print(f"  it_manager: #{it_manager_idx}")
                print(f"  sysop: #{sysop_idx}")
                return
        else:
            print("⚠ WARNING: service_desk_lead not found, cannot verify ordering")
    except Exception as e:
        print(f"✗ ERROR: Could not verify reorganization: {e}")
        return
    print()
    
    # Validate final structure
    print("Step 4: Validating final structure...")
    validation = cleanup.validate_role_structure()
    
    if validation.is_valid:
        print("✓ Role structure is valid")
    else:
        print("✗ Role structure has errors:")
        for error in validation.invalid_fields:
            print(f"  ✗ {error}")
    
    if validation.warnings:
        print("Remaining warnings:")
        for warning in validation.warnings:
            print(f"  ⚠ {warning}")
    else:
        print("✓ No structural warnings")
    print()
    
    print("=" * 70)
    print("✓ IT operations roles reorganization completed successfully")
    print("=" * 70)
    print()
    print("Role organization:")
    print("  1. C-Level Executives (ceo, cio, ciso, cfo, coo)")
    print("  2. IT Operations Roles (it_operations_manager, service_desk_lead, it_manager, sysop)")
    print("  3. BCM and Security Roles (bcm_manager, information_security_officer, data_protection_officer, ...)")
    print("  4. Add Custom Roles Here (for user-defined roles)")


if __name__ == '__main__':
    main()
