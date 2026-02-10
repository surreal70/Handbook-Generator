# Role Cleanup Migration Guide

## Overview

This document explains the role cleanup changes made to `metadata.example.yaml` as part of the template metadata standardization effort. These changes improve the organization and eliminate duplicate role definitions.

## Changes Made

### 1. Removed Duplicate Role: `datenschutzbeauftragter`

**What changed:**
- The `datenschutzbeauftragter` role has been removed from `metadata.example.yaml`
- This role was a duplicate of the existing `data_protection_officer` role

**Why:**
- Both roles served the same purpose (Data Protection Officer)
- `datenschutzbeauftragter` was the German name, while `data_protection_officer` is the canonical English name
- Having both roles created confusion and potential inconsistencies

**Migration:**
- If you were using `datenschutzbeauftragter` in your `metadata.yaml`, rename it to `data_protection_officer`
- Update any custom templates that reference `{{ meta.datenschutzbeauftragter.* }}` to use `{{ meta.data_protection_officer.* }}`
- The built-in templates do not use placeholder references to this role, so no template updates are needed

### 2. Reorganized IT Operations Roles

**What changed:**
- `it_manager` and `sysop` roles have been moved from the "Add Custom Roles Here" section to the "IT Operations Roles" section
- These roles now appear immediately after `service_desk_lead` in the role list

**Why:**
- These roles are core IT operations roles, not custom roles
- Grouping them with other IT operations roles improves organization and clarity
- Makes it easier to find and manage IT-related roles

**New Role Organization:**

```yaml
roles:
  # C-Level Executives
  ceo:
  cio:
  ciso:
  cfo:
  coo:
  
  # IT Operations Roles
  it_operations_manager:
  service_desk_lead:
  it_manager:          # ← Moved here
  sysop:               # ← Moved here
  
  # BCM and Security Roles
  bcm_manager:
  information_security_officer:
  data_protection_officer:
  risikomanager:
  interner_auditor:
  personalleitung:
  
  # Add Custom Roles Here
  # (Your custom roles go here)
```

**Migration:**
- No action required - the roles still exist with the same names and structure
- If you have custom code that depends on role ordering, verify it still works correctly

## Updated Role Structure

### Section 1: C-Level Executives
Core executive leadership roles:
- `ceo` - Chief Executive Officer
- `cio` - Chief Information Officer
- `ciso` - Chief Information Security Officer
- `cfo` - Chief Financial Officer
- `coo` - Chief Operating Officer

### Section 2: IT Operations Roles
IT operations and management roles:
- `it_operations_manager` - IT Operations Manager
- `service_desk_lead` - Service Desk Lead
- `it_manager` - IT Manager
- `sysop` - System Administrator

### Section 3: BCM and Security Roles
Business continuity, security, and compliance roles:
- `bcm_manager` - Business Continuity Manager
- `information_security_officer` - Information Security Officer
- `data_protection_officer` - Data Protection Officer (canonical role)
- `risikomanager` - Risk Manager
- `interner_auditor` - Internal Auditor
- `personalleitung` - HR Manager

### Section 4: Add Custom Roles Here
This section is reserved for your organization-specific custom roles.

## Migration Steps

### For Existing Users

1. **Backup your current metadata.yaml:**
   ```bash
   cp metadata.yaml metadata.yaml.backup
   ```

2. **Check if you're using datenschutzbeauftragter:**
   ```bash
   grep -i "datenschutzbeauftragter:" metadata.yaml
   ```

3. **If found, rename to data_protection_officer:**
   - Open `metadata.yaml` in your editor
   - Find the `datenschutzbeauftragter:` section
   - Rename it to `data_protection_officer:`
   - Keep all the nested fields (name, title, email, etc.) unchanged

4. **Check custom templates for references:**
   ```bash
   grep -r "meta.datenschutzbeauftragter" templates/
   ```

5. **If found, update references:**
   - Replace `{{ meta.datenschutzbeauftragter.name }}` with `{{ meta.data_protection_officer.name }}`
   - Replace `{{ meta.datenschutzbeauftragter.email }}` with `{{ meta.data_protection_officer.email }}`
   - And so on for other fields

6. **Verify your metadata.yaml:**
   ```bash
   python examples/verify_role_cleanup.py
   ```

7. **Test handbook generation:**
   ```bash
   ./handbook-generator --template <your-template> --language de --output test-output/
   ```

### For New Users

No migration needed! Just copy `metadata.example.yaml` to `metadata.yaml` and fill in your organization's information.

## Examples

### Example 1: Renaming datenschutzbeauftragter

**Before:**
```yaml
roles:
  datenschutzbeauftragter:
    name: "Dr. Sarah Klein"
    title: "Datenschutzbeauftragter"
    email: "sarah.klein@example.com"
    phone: "+49 30 12345678-320"
    department: "Legal & Compliance"
```

**After:**
```yaml
roles:
  data_protection_officer:
    name: "Dr. Sarah Klein"
    title: "Data Protection Officer"
    email: "sarah.klein@example.com"
    phone: "+49 30 12345678-320"
    department: "Legal & Compliance"
```

### Example 2: Updating Template References

**Before:**
```markdown
**Data Protection Officer:** {{ meta.datenschutzbeauftragter.name }}  
**Email:** {{ meta.datenschutzbeauftragter.email }}  
**Phone:** {{ meta.datenschutzbeauftragter.phone }}
```

**After:**
```markdown
**Data Protection Officer:** {{ meta.data_protection_officer.name }}  
**Email:** {{ meta.data_protection_officer.email }}  
**Phone:** {{ meta.data_protection_officer.phone }}
```

## Verification

After migration, verify your changes:

1. **Check for duplicate roles:**
   ```bash
   python -c "import yaml; data = yaml.safe_load(open('metadata.yaml')); roles = list(data['roles'].keys()); print(f'Unique roles: {len(set(roles))} / Total: {len(roles)}')"
   ```

2. **Verify datenschutzbeauftragter is removed:**
   ```bash
   grep -i "datenschutzbeauftragter:" metadata.yaml
   ```
   (Should return no results)

3. **Verify data_protection_officer exists:**
   ```bash
   grep -i "data_protection_officer:" metadata.yaml
   ```
   (Should return one result)

4. **Run full verification:**
   ```bash
   python examples/verify_role_cleanup.py
   ```

## Troubleshooting

### Issue: "Duplicate role 'datenschutzbeauftragter' found"

**Solution:** You still have the old role in your metadata.yaml. Remove it and use `data_protection_officer` instead.

### Issue: "Template references broken"

**Solution:** Search for `meta.datenschutzbeauftragter` in your custom templates and replace with `meta.data_protection_officer`.

### Issue: "Handbook generation fails"

**Solution:** 
1. Verify your metadata.yaml is valid YAML (no syntax errors)
2. Check that all required roles are defined
3. Run the verification script to identify issues

## Support

If you encounter issues during migration:

1. Check this migration guide for solutions
2. Review the verification script output for specific errors
3. Consult the main README.md for general handbook generator usage
4. Check the metadata.example.yaml file for the correct structure

## Summary

The role cleanup improves metadata organization by:
- ✓ Removing duplicate `datenschutzbeauftragter` role
- ✓ Using canonical `data_protection_officer` role name
- ✓ Organizing IT operations roles in a dedicated section
- ✓ Maintaining backward compatibility (roles still work, just better organized)

These changes make the metadata structure clearer and easier to maintain while ensuring consistency across all handbooks.
