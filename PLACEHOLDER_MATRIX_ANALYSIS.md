# Placeholder Matrix Analysis

## Overview
The placeholder matrix has been successfully generated and now correctly identifies placeholder usage across all 46 handbooks (23 DE + 23 EN).

## Key Findings

### Statistics
- **Total Placeholders**: 800 unique placeholders tracked
- **Total Handbooks**: 46 (23 German + 23 English)
- **Used & Defined**: 1,279 instances (✓ Good!)
- **Defined but Unused**: 14,729 instances (Available for future use)
- **Used but Undefined**: 983 instances (Need attention)

### Placeholder Categories

#### 1. Well-Defined Placeholders (✓)
The majority of placeholders are now correctly recognized:
- `meta-handbook.*` - Handbook-specific metadata (author, owner, classification, etc.)
- `meta-organisation.*` - Organization information (name, address, etc.)
- `meta-organisation-roles.*` - Role assignments (CEO, CISO, IT_Manager, etc.)
- `meta-global.*` - Global configuration values

#### 2. Undefined Placeholders (Need Action)

**Common Criteria Specific (35 placeholders)**
Used in Common Criteria templates but not defined in config:
- CC1, CC2, CC3, CCPORTAL, CEM (Common Criteria references)
- PP1, PP2 (Protection Profile references)
- FIPS140, ISO27001, ISO27002 (Standard references)
- CUSTOM_OBJECTIVE_1, CUSTOM_OBJECTIVE_2, CUSTOM_ENV_OBJECTIVE, etc.

**Recommendation**: Create a `meta-common-criteria.yaml` config file for these framework-specific placeholders.

**Generic Template Placeholders (34 placeholders)**
Used as examples or TODOs in templates:
- DATE, DATUM, TIME, ZEIT (Date/time examples)
- VERSION, NUMBER, NUMMER, NNN, YYYY (Version examples)
- NAME, ID, LEVEL, STUFE (Generic identifiers)
- NOTES, NOTIZEN (Note placeholders)
- CONFIDENTIAL, VERTRAULICH, PRIVATE, PRIVAT (Classification examples)

**Recommendation**: These are intentional template placeholders that users should replace. Consider documenting them as "user-replaceable" placeholders.

**Missing Handbook Fields (7 placeholders)**
Should be added to handbook configs:
- meta-handbook.iso20000_certifier
- meta-handbook.iso20000_status
- meta-handbook.iso27001_certification
- meta-handbook.iso27001_certifier
- meta-handbook.iso27001_status
- meta-handbook.iso27001_valid_until
- meta-handbook.last_updated

**Recommendation**: Add these fields to the `meta-handbook.yaml` template.

**Role Template Examples (10 placeholders)**
Pattern examples in templates:
- meta-organisation-roles.role_ROLE.* (English example)
- meta-organisation-roles.role_ROLLE.* (German example)

**Recommendation**: These are documentation examples showing the role placeholder pattern. No action needed.

## Script Improvements Made

### 1. Fixed Regex Pattern
**Before**: `\{\{([a-zA-Z0-9_\.]+)\}\}`
**After**: `\{\{\s*([a-zA-Z0-9_\.\-]+)\s*\}\}`

**Changes**:
- Added support for hyphens (`\-`) in placeholder names
- Added support for optional whitespace (`\s*`) around placeholders
- Now correctly matches `{{ meta-handbook.author }}` format

### 2. Fixed Namespace Prefixing
**Before**: Loaded `author` from `meta-handbook.yaml`
**After**: Loads `meta-handbook.author` to match template usage

**Changes**:
- Config placeholders now prefixed with their namespace (meta-global, meta-organisation, meta-organisation-roles)
- Handbook placeholders now prefixed with `meta-handbook.`
- Matches actual template usage: `{{ meta-handbook.author }}`

## Output Files

1. **placeholder_matrix.html** - Interactive HTML report with color-coded matrix
2. **placeholder_matrix.csv** - CSV export for spreadsheet analysis
3. **Console output** - Detailed text report with statistics

## Next Steps

1. **Add Missing Fields**: Update `meta-handbook.yaml` template with ISO 20000/27001 fields
2. **Document Common Criteria**: Create framework-specific config for Common Criteria placeholders
3. **Document User Placeholders**: Create guide explaining which placeholders users should replace (DATE, VERSION, etc.)
4. **Regular Monitoring**: Run matrix generation periodically to track placeholder coverage

## Usage

Generate the matrix anytime with:
```bash
python helpers/generate_placeholder_matrix.py
```

View the interactive report:
```bash
open placeholder_matrix.html  # macOS
xdg-open placeholder_matrix.html  # Linux
start placeholder_matrix.html  # Windows
```
