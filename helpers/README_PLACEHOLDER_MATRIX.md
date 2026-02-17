# Placeholder Coverage Matrix Generator

## Overview

The `generate_placeholder_matrix.py` script analyzes all handbook templates and configuration files to create a comprehensive placeholder coverage matrix. This helps identify:

- Which placeholders are used in each handbook
- Which placeholders are defined but unused
- Which placeholders are used but not defined in config files

## Usage

```bash
python helpers/generate_placeholder_matrix.py
```

## Output Files

The script generates three output files:

### 1. `placeholder_matrix.html` (Recommended)
An interactive HTML report with:
- Color-coded matrix table
- Statistics dashboard
- Legend and documentation
- List of undefined placeholders
- Sticky headers for easy navigation
- Responsive design

**Features:**
- 🟢 Green (#) - Placeholder is used and defined
- 🔵 Blue (O) - Placeholder is defined but not used
- 🔴 Red (X) - Placeholder is used but NOT defined

Open in your browser: `file://path/to/placeholder_matrix.html`

### 2. `placeholder_matrix.csv`
A CSV file for spreadsheet analysis with:
- Rows: Handbooks (de/en for each framework)
- Columns: All unique placeholders
- Values: #, O, X, or empty

Import into Excel, Google Sheets, or other tools for custom analysis.

### 3. Console Output
Terminal output with:
- Color-coded matrix sections
- Full placeholder list with status
- Summary statistics
- List of undefined placeholders

## How It Works

### 1. Placeholder Detection

The script scans all markdown files in `templates/` for two placeholder patterns:

- `{{placeholder}}` - Curly brace syntax
- `[PLACEHOLDER]` - Square bracket syntax (uppercase only)

Common non-placeholder patterns are filtered out (e.g., `[TODO]`, `[FRAMEWORK]`).

### 2. Configuration Analysis

Loads placeholder definitions from:
- `meta-global.yaml` - Global configuration
- `meta-organisation.yaml` - Organization details
- `meta-organisation-roles.yaml` - Role assignments
- `templates/*/meta-handbook.yaml` - Handbook-specific metadata

### 3. Coverage Analysis

For each handbook and placeholder combination:
- **Used & Defined (#)**: Placeholder appears in template AND is defined in config
- **Defined but Unused (O)**: Placeholder is in config but not used in template
- **Used but Undefined (X)**: Placeholder appears in template but NOT in config

## Interpreting Results

### Green Cells (#) - Good
These placeholders are properly configured and used. No action needed.

### Blue Cells (O) - Informational
These placeholders are defined but not used in this specific handbook. This is normal as not all handbooks use all placeholders.

### Red Cells (X) - Action Required
These placeholders are used in templates but not defined in any config file. You should:

1. Add the placeholder to the appropriate config file:
   - Global placeholders → `meta-global.yaml`
   - Organization info → `meta-organisation.yaml`
   - Role assignments → `meta-organisation-roles.yaml`
   - Handbook-specific → `templates/*/meta-handbook.yaml`

2. Or update the template to use a different placeholder that is defined

## Example Output

```
Summary Statistics:
================================================================================
Total Placeholders: 380
Total Handbooks: 46
Used & Defined: 0
Defined but Unused: 15,916
Used but Undefined: 54

Undefined Placeholders:
  - CC1, CC2, CC3 (Common Criteria specific)
  - DATE, DATUM (date placeholders)
  - LEVEL, NAME (generic placeholders)
  - VERSION (version placeholder)
```

## Common Issues

### No Placeholders Detected
- Check that templates use `{{placeholder}}` or `[PLACEHOLDER]` syntax
- Verify markdown files exist in `templates/de/` and `templates/en/`

### Many Undefined Placeholders
- Review the list of undefined placeholders
- Add missing placeholders to appropriate config files
- Consider if templates are using correct placeholder names

### Large Number of Unused Placeholders
- This is normal - not all handbooks use all placeholders
- Focus on the "Used but Undefined" count instead

## Maintenance

Run this script regularly to:
- Verify new placeholders are properly defined
- Identify unused placeholders that could be removed
- Ensure consistency across all handbooks
- Document placeholder coverage for audits

## Technical Details

**Language:** Python 3.8+
**Dependencies:** 
- `pyyaml` - For parsing YAML config files
- Standard library only (pathlib, re, collections)

**Performance:**
- Scans ~46 handbooks in seconds
- Generates reports in under 5 seconds
- HTML file size: ~1MB (includes all data)

## Related Files

- `meta-global.yaml` - Global configuration
- `meta-organisation.yaml` - Organization metadata
- `meta-organisation-roles.yaml` - Role definitions
- `templates/*/meta-handbook.yaml` - Handbook-specific config
- `docs/PLACEHOLDER_REFERENCE.md` - Placeholder documentation
