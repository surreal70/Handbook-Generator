# Framework Validation Guide

This guide explains how to use the consolidated framework validation script.

## Quick Start

```bash
# Validate all frameworks
python helpers/validate_frameworks.py

# Validate specific framework
python helpers/validate_frameworks.py --framework idw-ps-951

# Validate with quiet mode (summary only)
python helpers/validate_frameworks.py --quiet
```

## Supported Frameworks

The validation script supports all 16 frameworks in the system:
- bcm (Business Continuity Management)
- bsi-grundschutz (BSI IT-Grundschutz)
- cis-controls (CIS Controls)
- common-criteria (Common Criteria)
- gdpr (General Data Protection Regulation)
- hipaa (Health Insurance Portability and Accountability Act)
- idw-ps-951 (IDW PS 951 IT Auditing Standard)
- isms (Information Security Management System)
- iso-9001 (ISO 9001 Quality Management)
- it-operation (IT Operations)
- nist-800-53 (NIST SP 800-53)
- nist-csf (NIST Cybersecurity Framework 2.0)
- pci-dss (Payment Card Industry Data Security Standard)
- service-directory (Service Directory)
- togaf (The Open Group Architecture Framework)
- tsc (Trust Services Criteria)

## Command Options

### Framework Selection

```bash
# Validate all frameworks (default)
python helpers/validate_frameworks.py

# Validate specific framework
python helpers/validate_frameworks.py --framework idw-ps-951
python helpers/validate_frameworks.py --framework nist-csf
python helpers/validate_frameworks.py --framework pci-dss
```

### Language Selection

```bash
# Validate both languages (default)
python helpers/validate_frameworks.py --framework idw-ps-951

# Validate German only
python helpers/validate_frameworks.py --framework idw-ps-951 --language de

# Validate English only
python helpers/validate_frameworks.py --framework idw-ps-951 --language en
```

### Output Options

```bash
# Normal output (default)
python helpers/validate_frameworks.py

# Quiet mode (summary only)
python helpers/validate_frameworks.py --quiet

# Verbose mode (detailed errors/warnings)
python helpers/validate_frameworks.py --framework idw-ps-951 --verbose

# Save report to file
python helpers/validate_frameworks.py --output report.txt
```

## Common Use Cases

### Pre-commit Validation
Validate all frameworks before committing:
```bash
python helpers/validate_frameworks.py --quiet
```

### New Framework Development
Validate a specific framework during development:
```bash
python helpers/validate_frameworks.py --framework my-new-framework --verbose
```

### CI/CD Integration
Validate all frameworks in CI pipeline:
```bash
python helpers/validate_frameworks.py --quiet
```

### Debugging Issues
Get detailed validation output for troubleshooting:
```bash
python helpers/validate_frameworks.py --framework pci-dss --verbose
```

### Generate Validation Report
Create a detailed report for documentation:
```bash
python helpers/validate_frameworks.py --output validation_report.txt
```

## Validation Checks

The script validates:

1. **Template Structure**
   - Required files exist
   - Proper directory organization
   - Naming conventions

2. **Placeholder Consistency**
   - All placeholders are properly formatted
   - Required placeholders are present
   - No undefined placeholders

3. **Bilingual Consistency**
   - German and English versions match
   - Same structure in both languages
   - Consistent placeholder usage

4. **Framework-Specific Rules**
   - Framework-specific requirements
   - Proper section organization
   - Metadata completeness

## Exit Codes

- `0` - All validations passed
- `1` - One or more validations failed

## Migration from Old Scripts

The consolidated script replaces these deprecated scripts:
- `validate_all_frameworks.py` → Use without `--framework` option
- `validate_new_frameworks.py` → Use with specific `--framework` option
- `validate_new_frameworks_integration.py` → Use with specific `--framework` option

### Migration Examples

```bash
# Old: python validate_all_frameworks.py
# New:
python helpers/validate_frameworks.py

# Old: python validate_new_frameworks.py --framework idw-ps-951
# New:
python helpers/validate_frameworks.py --framework idw-ps-951

# Old: python validate_new_frameworks.py --framework idw-ps-951 --language de
# New:
python helpers/validate_frameworks.py --framework idw-ps-951 --language de
```

## Troubleshooting

### Script Not Found
Make sure you're running from the project root:
```bash
cd /path/to/Handbook-Generator
python helpers/validate_frameworks.py
```

### Import Errors
Ensure the virtual environment is activated:
```bash
source venv/bin/activate
python helpers/validate_frameworks.py
```

### Permission Denied
Make the script executable:
```bash
chmod +x helpers/validate_frameworks.py
```

## See Also

- [helpers/README.md](README.md) - Overview of all helper scripts
- [docs/FRAMEWORK_MAPPING.md](../docs/FRAMEWORK_MAPPING.md) - Framework documentation
- [src/template_validator.py](../src/template_validator.py) - Validation implementation
