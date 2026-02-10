# Metadata Validation Guide

## Overview

This guide explains how to validate template metadata files to ensure they meet the unified metadata structure requirements. The validation process checks for completeness, format compliance, and bilingual consistency across all frameworks.

## Table of Contents

- [Quick Start](#quick-start)
- [Validation Script Usage](#validation-script-usage)
- [Validation Checks](#validation-checks)
- [Understanding Validation Output](#understanding-validation-output)
- [Common Validation Errors](#common-validation-errors)
- [Fixing Validation Errors](#fixing-validation-errors)
- [Automated Validation](#automated-validation)
- [Best Practices](#best-practices)

## Quick Start

### Basic Validation

```bash
# Validate all frameworks
python helpers/validate_metadata.py --all

# Validate specific framework
python helpers/validate_metadata.py --framework gdpr

# Validate specific language
python helpers/validate_metadata.py --language de

# Generate JSON report
python helpers/validate_metadata.py --all --report validation_report.json
```

### Expected Output

```
Validating metadata for all frameworks...

✓ BCM (de): Valid
✓ BCM (en): Valid
✓ ISMS (de): Valid
✓ ISMS (en): Valid
✓ BSI Grundschutz (de): Valid
✓ BSI Grundschutz (en): Valid
✓ IT-Operation (de): Valid
✓ IT-Operation (en): Valid
✓ CIS Controls (de): Valid
✓ CIS Controls (en): Valid
✓ Common Criteria (de): Valid
✓ Common Criteria (en): Valid
✓ GDPR (de): Valid
✓ GDPR (en): Valid
✓ HIPAA (de): Valid
✓ HIPAA (en): Valid
✓ ISO 9001 (de): Valid
✓ ISO 9001 (en): Valid
✓ NIST 800-53 (de): Valid
✓ NIST 800-53 (en): Valid
✓ PCI-DSS (de): Valid
✓ PCI-DSS (en): Valid
✓ TSC (de): Valid
✓ TSC (en): Valid

Summary: 24/24 metadata files valid (100%)
```

## Validation Script Usage

### Command-Line Options

```bash
python helpers/validate_metadata.py [OPTIONS]
```

**Options:**

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--all` | `-a` | Validate all frameworks | `--all` |
| `--framework` | `-f` | Validate specific framework | `--framework gdpr` |
| `--language` | `-l` | Validate specific language | `--language de` |
| `--report` | `-r` | Generate JSON report | `--report report.json` |
| `--verbose` | `-v` | Show detailed output | `--verbose` |
| `--check-bilingual` | `-b` | Check DE/EN consistency | `--check-bilingual` |
| `--help` | `-h` | Show help message | `--help` |

### Usage Examples

#### Validate All Frameworks

```bash
python helpers/validate_metadata.py --all
```

Validates all 12 frameworks in both German and English (24 metadata files total).

#### Validate Specific Framework

```bash
# Validate GDPR framework (both languages)
python helpers/validate_metadata.py --framework gdpr

# Validate only German GDPR metadata
python helpers/validate_metadata.py --framework gdpr --language de
```

#### Validate All German Metadata

```bash
python helpers/validate_metadata.py --language de
```

Validates all German metadata files across all frameworks.

#### Generate Detailed Report

```bash
python helpers/validate_metadata.py --all --report validation_report.json --verbose
```

Creates a JSON report with detailed validation results.

#### Check Bilingual Consistency

```bash
python helpers/validate_metadata.py --framework iso-9001 --check-bilingual
```

Compares German and English metadata for structural consistency.

## Validation Checks

### 1. Required Fields Check

**Purpose:** Verify all 13 required fields are present

**Required Fields:**
1. `document_id`
2. `owner`
3. `version`
4. `status`
5. `classification`
6. `date`
7. `template_version`
8. `revision`
9. `organization`
10. `author`
11. `scope`
12. `valid_from`
13. `next_review`

**Check Logic:**
```python
def check_required_fields(metadata_content):
    required_fields = [
        'document_id', 'owner', 'version', 'status', 
        'classification', 'date', 'template_version', 
        'revision', 'organization', 'author', 'scope', 
        'valid_from', 'next_review'
    ]
    
    missing_fields = []
    for field in required_fields:
        if not field_exists_in_metadata(metadata_content, field):
            missing_fields.append(field)
    
    return missing_fields
```

**Example Output:**
```
✗ Missing fields: template_version, revision, scope
```

### 2. Template Version Format Check

**Purpose:** Verify template_version follows MAJOR.MINOR format

**Valid Formats:**
- ✅ `1.0`
- ✅ `1.1`
- ✅ `2.0`
- ✅ `10.5`
- ❌ `1` (missing minor version)
- ❌ `1.0.0` (too many components)
- ❌ `v1.0` (invalid prefix)
- ❌ `1.0-beta` (invalid suffix)

**Check Logic:**
```python
import re

def validate_template_version(version_string):
    pattern = r'^\d+\.\d+$'
    return re.match(pattern, version_string) is not None
```

**Example Output:**
```
✓ Template version: 1.0 (valid)
✗ Template version: 1.0.0 (invalid format, expected MAJOR.MINOR)
```

### 3. Revision Number Check

**Purpose:** Verify revision is a valid non-negative integer

**Valid Values:**
- ✅ `0`
- ✅ `1`
- ✅ `42`
- ✅ `1000`
- ❌ `-1` (negative)
- ❌ `1.5` (not an integer)
- ❌ `v1` (not a number)
- ❌ `"0"` (string, not integer)

**Check Logic:**
```python
def validate_revision(revision_value):
    try:
        rev = int(revision_value)
        return rev >= 0
    except (ValueError, TypeError):
        return False
```

**Example Output:**
```
✓ Revision: 0 (valid)
✗ Revision: -1 (invalid, must be non-negative)
```

### 4. Bilingual Consistency Check

**Purpose:** Verify German and English metadata have identical structure

**Checks:**
- Same number of fields
- Same field names
- Same placeholder names
- Same section organization

**Check Logic:**
```python
def check_bilingual_consistency(de_metadata, en_metadata):
    de_fields = extract_fields(de_metadata)
    en_fields = extract_fields(en_metadata)
    
    # Check field count
    if len(de_fields) != len(en_fields):
        return False, "Field count mismatch"
    
    # Check field names
    if set(de_fields.keys()) != set(en_fields.keys()):
        return False, "Field names don't match"
    
    # Check placeholders
    de_placeholders = extract_placeholders(de_metadata)
    en_placeholders = extract_placeholders(en_metadata)
    if de_placeholders != en_placeholders:
        return False, "Placeholder mismatch"
    
    return True, "Consistent"
```

**Example Output:**
```
✓ Bilingual consistency: DE and EN structures match
✗ Bilingual consistency: Field count mismatch (DE: 13, EN: 12)
```

### 5. Placeholder Syntax Check

**Purpose:** Verify all placeholders follow `{{ source.field }}` format

**Valid Formats:**
- ✅ `{{ meta.owner }}`
- ✅ `{{ netbox.device_name }}`
- ✅ `{{ custom.field }}`
- ❌ `{ meta.owner }` (single braces)
- ❌ `{{ meta.owner}` (missing closing space)
- ❌ `{{meta.owner }}` (missing opening space)
- ❌ `{{ meta owner }}` (missing dot)

**Check Logic:**
```python
import re

def validate_placeholder_syntax(placeholder):
    pattern = r'\{\{\s*\w+\.\w+\s*\}\}'
    return re.match(pattern, placeholder) is not None

def check_all_placeholders(metadata_content):
    placeholders = extract_placeholders(metadata_content)
    invalid = []
    
    for placeholder in placeholders:
        if not validate_placeholder_syntax(placeholder):
            invalid.append(placeholder)
    
    return invalid
```

**Example Output:**
```
✓ Placeholders: 11 found, all valid
✗ Invalid placeholders: { meta.owner }, {{meta.owner}}
```

## Understanding Validation Output

### Success Output

```
Validating GDPR metadata...

✓ templates/de/gdpr/0000_metadata_de_gdpr.md
  - All 13 required fields present
  - Template version: 1.0 (valid)
  - Revision: 0 (valid)
  - Placeholders: 11 found, all valid

✓ templates/en/gdpr/0000_metadata_en_gdpr.md
  - All 13 required fields present
  - Template version: 1.0 (valid)
  - Revision: 0 (valid)
  - Placeholders: 11 found, all valid

✓ Bilingual consistency check passed

Result: GDPR metadata is valid
```

### Error Output

```
Validating HIPAA metadata...

✗ templates/de/hipaa/0000_metadata_de_hipaa.md
  - Missing fields: template_version, revision, scope, valid_from, next_review
  - Warnings: 5 missing fields

✗ templates/en/hipaa/0000_metadata_en_hipaa.md
  - Missing fields: template_version, revision, scope, valid_from, next_review
  - Warnings: 5 missing fields

✗ Bilingual consistency check: Both files have same issues

Result: HIPAA metadata has issues
Suggestion: Run 'python -m src.metadata_standardizer --framework hipaa --enhance-all'
```

### Warning Output

```
Validating CIS Controls metadata...

⚠ templates/de/cis-controls/0000_metadata_de_cis-controls.md
  - All required fields present
  - Template version: 1.0 (valid)
  - Revision: 0 (valid)
  - Warning: Placeholder {{ custom.field }} uses non-standard source

✓ templates/en/cis-controls/0000_metadata_en_cis-controls.md
  - All 13 required fields present
  - Template version: 1.0 (valid)
  - Revision: 0 (valid)

Result: CIS Controls metadata is valid with warnings
```

### JSON Report Format

```json
{
  "validation_date": "2026-02-10T14:30:00Z",
  "total_frameworks": 12,
  "total_files": 24,
  "valid_files": 22,
  "invalid_files": 2,
  "success_rate": 91.67,
  "frameworks": {
    "gdpr": {
      "de": {
        "valid": true,
        "file": "templates/de/gdpr/0000_metadata_de_gdpr.md",
        "fields_present": 13,
        "fields_missing": [],
        "template_version": "1.0",
        "revision": 0,
        "placeholders": 11,
        "errors": [],
        "warnings": []
      },
      "en": {
        "valid": true,
        "file": "templates/en/gdpr/0000_metadata_en_gdpr.md",
        "fields_present": 13,
        "fields_missing": [],
        "template_version": "1.0",
        "revision": 0,
        "placeholders": 11,
        "errors": [],
        "warnings": []
      },
      "bilingual_consistent": true
    },
    "hipaa": {
      "de": {
        "valid": false,
        "file": "templates/de/hipaa/0000_metadata_de_hipaa.md",
        "fields_present": 8,
        "fields_missing": ["template_version", "revision", "scope", "valid_from", "next_review"],
        "errors": ["Missing required fields"],
        "warnings": []
      },
      "en": {
        "valid": false,
        "file": "templates/en/hipaa/0000_metadata_en_hipaa.md",
        "fields_present": 8,
        "fields_missing": ["template_version", "revision", "scope", "valid_from", "next_review"],
        "errors": ["Missing required fields"],
        "warnings": []
      },
      "bilingual_consistent": true
    }
  }
}
```

## Common Validation Errors

### Error 1: Missing Required Fields

**Error Message:**
```
✗ Missing fields: template_version, revision, scope
```

**Cause:** Metadata file doesn't contain all 13 required fields

**Fix:**
```bash
# Run metadata standardizer to add missing fields
python -m src.metadata_standardizer --framework <framework> --language <lang>
```

**Manual Fix:**
Add missing fields to metadata file:
```markdown
**Template-Version:** 1.0  
**Revision:** 0  
**Geltungsbereich:** {{ meta.scope }}  
```

### Error 2: Invalid Template Version Format

**Error Message:**
```
✗ Template version: 1.0.0 (invalid format, expected MAJOR.MINOR)
```

**Cause:** Template version doesn't follow MAJOR.MINOR format

**Fix:**
Edit metadata file and change:
```markdown
<!-- Wrong -->
**Template-Version:** 1.0.0

<!-- Correct -->
**Template-Version:** 1.0
```

### Error 3: Invalid Revision Number

**Error Message:**
```
✗ Revision: -1 (invalid, must be non-negative integer)
```

**Cause:** Revision is negative or not an integer

**Fix:**
Edit metadata file and change:
```markdown
<!-- Wrong -->
**Revision:** -1

<!-- Correct -->
**Revision:** 0
```

### Error 4: Bilingual Inconsistency

**Error Message:**
```
✗ Bilingual consistency: Field count mismatch (DE: 13, EN: 12)
```

**Cause:** German and English metadata have different structures

**Fix:**
1. Compare both files:
   ```bash
   diff templates/de/gdpr/0000_metadata_de_gdpr.md \
        templates/en/gdpr/0000_metadata_en_gdpr.md
   ```

2. Add missing field to English version:
   ```markdown
   **Next Review:** {{ meta.next_review }}
   ```

### Error 5: Invalid Placeholder Syntax

**Error Message:**
```
✗ Invalid placeholders: { meta.owner }, {{meta.owner}}
```

**Cause:** Placeholders don't follow `{{ source.field }}` format

**Fix:**
Edit metadata file and correct placeholders:
```markdown
<!-- Wrong -->
{ meta.owner }
{{meta.owner}}
{{ meta owner }}

<!-- Correct -->
{{ meta.owner }}
```

### Error 6: File Not Found

**Error Message:**
```
✗ File not found: templates/de/gdpr/0000_metadata_de_gdpr.md
```

**Cause:** Metadata file doesn't exist

**Fix:**
```bash
# Create missing metadata file
python -m src.metadata_standardizer --framework gdpr --language de --create
```

## Fixing Validation Errors

### Automated Fix (Recommended)

Use the metadata standardizer to automatically fix most issues:

```bash
# Fix all frameworks
python -m src.metadata_standardizer --enhance-all

# Fix specific framework
python -m src.metadata_standardizer --framework gdpr --enhance-all

# Fix specific language
python -m src.metadata_standardizer --framework gdpr --language de
```

### Manual Fix

1. **Identify the error:**
   ```bash
   python helpers/validate_metadata.py --framework gdpr --verbose
   ```

2. **Open the metadata file:**
   ```bash
   vim templates/de/gdpr/0000_metadata_de_gdpr.md
   ```

3. **Add missing fields or fix format issues**

4. **Validate again:**
   ```bash
   python helpers/validate_metadata.py --framework gdpr
   ```

### Step-by-Step Fix Example

**Problem:** HIPAA metadata missing 5 fields

**Step 1: Check current state**
```bash
$ python helpers/validate_metadata.py --framework hipaa

✗ Missing fields: template_version, revision, scope, valid_from, next_review
```

**Step 2: Run standardizer**
```bash
$ python -m src.metadata_standardizer --framework hipaa --enhance-all

Enhancing HIPAA metadata...
✓ Added template_version: 1.0
✓ Added revision: 0
✓ Added scope placeholder
✓ Added valid_from placeholder
✓ Added next_review placeholder
✓ Backup created: templates/de/hipaa/0000_metadata_de_hipaa.md.backup
```

**Step 3: Validate fix**
```bash
$ python helpers/validate_metadata.py --framework hipaa

✓ HIPAA (de): Valid
✓ HIPAA (en): Valid
✓ Bilingual consistency check passed
```

## Automated Validation

### CI/CD Integration

Add validation to your CI/CD pipeline:

**GitHub Actions Example:**
```yaml
name: Validate Metadata

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Validate metadata
        run: python helpers/validate_metadata.py --all
```

**GitLab CI Example:**
```yaml
validate_metadata:
  stage: test
  script:
    - pip install -r requirements.txt
    - python helpers/validate_metadata.py --all
  only:
    - merge_requests
    - main
```

### Pre-commit Hook

Add validation as a pre-commit hook:

```bash
# .git/hooks/pre-commit
#!/bin/bash

echo "Validating metadata..."
python helpers/validate_metadata.py --all

if [ $? -ne 0 ]; then
    echo "Metadata validation failed. Commit aborted."
    exit 1
fi

echo "Metadata validation passed."
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

### Scheduled Validation

Run validation on a schedule:

```bash
# Add to crontab
0 2 * * * cd /path/to/handbook-generator && python helpers/validate_metadata.py --all --report /var/log/metadata_validation.json
```

## Best Practices

### 1. Validate Before Committing

Always validate metadata before committing changes:

```bash
# Before git commit
python helpers/validate_metadata.py --all
```

### 2. Use Verbose Mode for Debugging

When troubleshooting, use verbose mode:

```bash
python helpers/validate_metadata.py --framework gdpr --verbose
```

### 3. Generate Reports for Documentation

Create validation reports for documentation:

```bash
python helpers/validate_metadata.py --all --report validation_$(date +%Y%m%d).json
```

### 4. Validate After Standardization

Always validate after running the standardizer:

```bash
python -m src.metadata_standardizer --enhance-all
python helpers/validate_metadata.py --all
```

### 5. Check Bilingual Consistency Regularly

Ensure DE/EN consistency:

```bash
python helpers/validate_metadata.py --all --check-bilingual
```

### 6. Keep Validation Logs

Maintain validation logs for audit purposes:

```bash
python helpers/validate_metadata.py --all > validation_$(date +%Y%m%d).log
```

### 7. Validate Individual Frameworks During Development

When working on a specific framework:

```bash
# Validate frequently during development
python helpers/validate_metadata.py --framework gdpr
```

### 8. Use JSON Reports for Automation

Generate JSON reports for automated processing:

```bash
python helpers/validate_metadata.py --all --report report.json

# Process with jq
cat report.json | jq '.success_rate'
```

## Summary

The metadata validation process ensures:
- ✅ All required fields are present
- ✅ Template versions follow correct format
- ✅ Revision numbers are valid
- ✅ Bilingual consistency is maintained
- ✅ Placeholders use correct syntax
- ✅ Metadata structure is standardized

Regular validation helps maintain high-quality, consistent metadata across all compliance frameworks.
