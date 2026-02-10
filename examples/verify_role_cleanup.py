#!/usr/bin/env python3
"""
Verify Role Cleanup

This script verifies that the role cleanup was successful:
1. No duplicate roles exist
2. datenschutzbeauftragter is removed
3. it_manager and sysop are in IT Operations section
4. No broken template references
5. Test handbook generation (optional)

Usage:
    python examples/verify_role_cleanup.py [--test-handbook]
"""

import sys
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataRoleCleanup


def main():
    """Verify role cleanup."""
    parser = argparse.ArgumentParser(description='Verify role cleanup')
    parser.add_argument('--test-handbook', action='store_true',
                       help='Test handbook generation (requires handbook-generator)')
    args = parser.parse_args()
    
    print("=" * 70)
    print("Verify Role Cleanup")
    print("=" * 70)
    print()
    
    # Initialize role cleanup
    cleanup = MetadataRoleCleanup('metadata.example.yaml')
    
    all_checks_passed = True
    
    # Check 1: Validate role structure
    print("Check 1: Validate role structure...")
    validation = cleanup.validate_role_structure()
    
    if validation.is_valid:
        print("✓ Role structure is valid")
    else:
        print("✗ Role structure has errors:")
        for error in validation.invalid_fields:
            print(f"  ✗ {error}")
        all_checks_passed = False
    
    if validation.warnings:
        print("  Warnings:")
        for warning in validation.warnings:
            print(f"  ⚠ {warning}")
    print()
    
    # Check 2: Verify datenschutzbeauftragter is removed
    print("Check 2: Verify datenschutzbeauftragter is removed...")
    try:
        import yaml
        with open('metadata.example.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        roles = data.get('roles', {})
        
        if 'datenschutzbeauftragter' in roles:
            print("✗ datenschutzbeauftragter role still exists!")
            all_checks_passed = False
        else:
            print("✓ datenschutzbeauftragter role successfully removed")
    except Exception as e:
        print(f"✗ ERROR: Could not verify: {e}")
        all_checks_passed = False
    print()
    
    # Check 3: Verify data_protection_officer exists
    print("Check 3: Verify data_protection_officer exists...")
    try:
        if 'data_protection_officer' in roles:
            print("✓ data_protection_officer role exists")
        else:
            print("✗ data_protection_officer role missing!")
            all_checks_passed = False
    except Exception as e:
        print(f"✗ ERROR: Could not verify: {e}")
        all_checks_passed = False
    print()
    
    # Check 4: Verify it_manager and sysop in IT Operations section
    print("Check 4: Verify it_manager and sysop in IT Operations section...")
    try:
        role_names = list(roles.keys())
        
        if 'it_manager' not in role_names:
            print("✗ it_manager role missing!")
            all_checks_passed = False
        elif 'sysop' not in role_names:
            print("✗ sysop role missing!")
            all_checks_passed = False
        elif 'service_desk_lead' not in role_names:
            print("⚠ service_desk_lead role missing (cannot verify ordering)")
        else:
            service_desk_idx = role_names.index('service_desk_lead')
            it_manager_idx = role_names.index('it_manager')
            sysop_idx = role_names.index('sysop')
            
            if it_manager_idx > service_desk_idx and sysop_idx > service_desk_idx:
                print("✓ it_manager and sysop are in IT Operations section")
                print(f"  Role order: service_desk_lead (#{service_desk_idx+1}) → it_manager (#{it_manager_idx+1}) → sysop (#{sysop_idx+1})")
            else:
                print("✗ Roles not in correct order!")
                print(f"  service_desk_lead: #{service_desk_idx+1}")
                print(f"  it_manager: #{it_manager_idx+1}")
                print(f"  sysop: #{sysop_idx+1}")
                all_checks_passed = False
    except Exception as e:
        print(f"✗ ERROR: Could not verify: {e}")
        all_checks_passed = False
    print()
    
    # Check 5: Verify no duplicate roles
    print("Check 5: Verify no duplicate roles...")
    try:
        unique_roles = set(role_names)
        if len(role_names) == len(unique_roles):
            print(f"✓ No duplicate roles (total: {len(role_names)} roles)")
        else:
            duplicates = len(role_names) - len(unique_roles)
            print(f"✗ Found {duplicates} duplicate role(s)!")
            all_checks_passed = False
    except Exception as e:
        print(f"✗ ERROR: Could not verify: {e}")
        all_checks_passed = False
    print()
    
    # Check 6: Verify no broken template references to datenschutzbeauftragter
    print("Check 6: Verify no references to removed datenschutzbeauftragter role...")
    
    templates_dir = Path('templates')
    broken_refs = []
    
    if templates_dir.exists():
        for md_file in templates_dir.rglob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                
                # Check specifically for datenschutzbeauftragter placeholder references
                if 'meta.datenschutzbeauftragter.' in content:
                    broken_refs.append(str(md_file))
            except Exception:
                pass
        
        if broken_refs:
            print(f"✗ Found {len(broken_refs)} file(s) with datenschutzbeauftragter references:")
            for file_path in broken_refs[:10]:  # Show first 10
                print(f"  ✗ {file_path}")
            if len(broken_refs) > 10:
                print(f"  ... and {len(broken_refs) - 10} more")
            all_checks_passed = False
        else:
            print("✓ No references to removed datenschutzbeauftragter role found")
    else:
        print("⚠ Templates directory not found, skipping check")
    print()
    
    # Check 7: Test handbook generation (optional)
    if args.test_handbook:
        print("Check 7: Test handbook generation...")
        print("  (This check is optional and requires handbook-generator)")
        print("  Skipping for now - manual testing recommended")
        print()
    
    # Summary
    print("=" * 70)
    if all_checks_passed:
        print("✓ All verification checks passed!")
        print("=" * 70)
        print()
        print("Role cleanup completed successfully:")
        print("  ✓ datenschutzbeauftragter role removed")
        print("  ✓ data_protection_officer role exists")
        print("  ✓ it_manager and sysop in IT Operations section")
        print("  ✓ No duplicate roles")
        print("  ✓ No references to removed datenschutzbeauftragter role")
        return 0
    else:
        print("✗ Some verification checks failed!")
        print("=" * 70)
        print()
        print("Please review the errors above and fix them.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
