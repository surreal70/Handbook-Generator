#!/usr/bin/env python3
"""
Reorganize IT Operations Roles (Version 2)

This script moves it_manager and sysop from "Add Custom Roles Here" section
to "IT Operations Roles" section in metadata.example.yaml using a more reliable
line-by-line approach.

Usage:
    python examples/reorganize_it_roles_v2.py
"""

import sys
from pathlib import Path


def main():
    """Reorganize IT operations roles."""
    print("=" * 70)
    print("Reorganize IT Operations Roles (v2)")
    print("=" * 70)
    print()
    
    metadata_file = 'metadata.example.yaml'
    
    # Read the file
    print("Step 1: Reading metadata.example.yaml...")
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"✗ ERROR: Could not read file: {e}")
        return
    print(f"✓ Read {len(lines)} lines")
    print()
    
    # Find and extract role definitions
    print("Step 2: Extracting it_manager and sysop definitions...")
    
    roles_to_move = {}  # role_name -> (start_line, end_line, lines)
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check for it_manager or sysop
        if stripped == 'it_manager:' or stripped == 'sysop:':
            role_name = stripped[:-1]  # Remove the colon
            start_line = i
            role_lines = [line]
            base_indent = len(line) - len(line.lstrip())
            
            # Collect all lines for this role
            i += 1
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                
                # Empty line or comment - include it
                if not next_stripped or next_stripped.startswith('#'):
                    role_lines.append(next_line)
                    i += 1
                    continue
                
                # Check indentation
                next_indent = len(next_line) - len(next_line.lstrip())
                
                # If we're back to base indentation or less, we've left the role
                if next_indent <= base_indent:
                    break
                
                role_lines.append(next_line)
                i += 1
            
            end_line = i - 1
            roles_to_move[role_name] = (start_line, end_line, role_lines)
            print(f"  Found {role_name} at lines {start_line+1}-{end_line+1}")
            continue
        
        i += 1
    
    if len(roles_to_move) != 2:
        print(f"✗ ERROR: Expected to find 2 roles, found {len(roles_to_move)}")
        return
    print()
    
    # Find service_desk_lead insertion point
    print("Step 3: Finding insertion point after service_desk_lead...")
    
    insertion_point = None
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if stripped == 'service_desk_lead:':
            base_indent = len(line) - len(line.lstrip())
            
            # Find the end of service_desk_lead
            i += 1
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                
                if not next_stripped or next_stripped.startswith('#'):
                    i += 1
                    continue
                
                next_indent = len(next_line) - len(next_line.lstrip())
                
                if next_indent <= base_indent:
                    insertion_point = i
                    break
                
                i += 1
            
            if insertion_point:
                print(f"  Insertion point: line {insertion_point+1}")
                break
        
        i += 1
    
    if not insertion_point:
        print("✗ ERROR: Could not find service_desk_lead")
        return
    print()
    
    # Build new file
    print("Step 4: Building new file with reorganized roles...")
    
    new_lines = []
    skip_ranges = []
    
    # Mark ranges to skip (the original role locations)
    for role_name, (start, end, _) in roles_to_move.items():
        skip_ranges.append((start, end))
    
    # Sort skip ranges
    skip_ranges.sort()
    
    # Build new file
    i = 0
    while i < len(lines):
        # Check if we should skip this line
        should_skip = False
        for start, end in skip_ranges:
            if start <= i <= end:
                should_skip = True
                break
        
        if should_skip:
            i += 1
            continue
        
        # Check if this is the insertion point
        if i == insertion_point:
            # Insert the roles
            new_lines.append('\n')
            new_lines.extend(roles_to_move['it_manager'][2])
            new_lines.append('\n')
            new_lines.extend(roles_to_move['sysop'][2])
        
        new_lines.append(lines[i])
        i += 1
    
    print(f"  New file has {len(new_lines)} lines")
    print()
    
    # Write the new file
    print("Step 5: Writing reorganized file...")
    try:
        with open(metadata_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print("✓ File written successfully")
    except Exception as e:
        print(f"✗ ERROR: Could not write file: {e}")
        return
    print()
    
    # Verify
    print("Step 6: Verifying reorganization...")
    try:
        import yaml
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        roles = data.get('roles', {})
        role_names = list(roles.keys())
        
        if 'it_manager' not in role_names or 'sysop' not in role_names:
            print("✗ ERROR: Roles missing after reorganization!")
            return
        
        service_desk_idx = role_names.index('service_desk_lead')
        it_manager_idx = role_names.index('it_manager')
        sysop_idx = role_names.index('sysop')
        
        if it_manager_idx > service_desk_idx and sysop_idx > service_desk_idx:
            print("✓ Roles successfully reorganized")
            print(f"  Role order: service_desk_lead (#{service_desk_idx}) → it_manager (#{it_manager_idx}) → sysop (#{sysop_idx})")
        else:
            print("✗ ERROR: Roles not in correct order!")
            return
    except Exception as e:
        print(f"✗ ERROR: Could not verify: {e}")
        return
    print()
    
    print("=" * 70)
    print("✓ IT operations roles reorganization completed successfully")
    print("=" * 70)


if __name__ == '__main__':
    main()
