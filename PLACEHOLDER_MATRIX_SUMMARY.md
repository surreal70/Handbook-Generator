# Placeholder Coverage Matrix - Summary

## Quick Start

Generate the placeholder coverage matrix:

```bash
python helpers/generate_placeholder_matrix.py
```

Then open `placeholder_matrix.html` in your browser to view the interactive report.

## What This Tool Does

The Placeholder Coverage Matrix analyzes all handbook templates and configuration files to show:

1. **Which placeholders are used** in each handbook template
2. **Which placeholders are defined** in configuration files
3. **Coverage gaps** where placeholders are used but not defined

## Output Files

| File | Format | Best For |
|------|--------|----------|
| `placeholder_matrix.html` | Interactive HTML | Visual analysis, presentations, documentation |
| `placeholder_matrix.csv` | CSV spreadsheet | Data analysis, Excel/Sheets, filtering |
| Console output | Terminal text | Quick checks, CI/CD pipelines |

## Understanding the Matrix

### Color Coding

- 🟢 **Green (#)** - ✅ Placeholder is used in handbook AND defined in config
- 🔵 **Blue (O)** - ℹ️ Placeholder is defined but not used in this handbook
- 🔴 **Red (X)** - ⚠️ Placeholder is used but NOT defined in config

### Current Status

Based on the latest analysis:

- **Total Placeholders:** 380 unique placeholders
- **Total Handbooks:** 46 (23 German + 23 English)
- **Used & Defined:** 0 instances (all defined placeholders are currently unused)
- **Defined but Unused:** 15,916 instances (normal - not all handbooks use all placeholders)
- **Used but Undefined:** 54 instances (⚠️ requires attention)

## Action Items

### High Priority: Undefined Placeholders

The following placeholders are used in templates but not defined in config files:

#### Common Criteria Specific (de/common-criteria, en/common-criteria)
- `CC1`, `CC2`, `CC3` - Common Criteria components
- `CCPORTAL` - Common Criteria portal URL
- `CEM` - Common Evaluation Methodology
- `CUSTOM_ENV_OBJECTIVE`, `CUSTOM_ENV_OBJECTIVE_1`, `CUSTOM_ENV_OBJECTIVE_2`
- `CUSTOM_OBJECTIVE_1`, `CUSTOM_OBJECTIVE_2`
- `FIPS140` - FIPS 140 certification
- `ISO27001`, `ISO27002` - ISO standards
- `PP1`, `PP2` - Protection Profiles
- `PRIVAT`, `PRIVATE`, `VERTRAULICH`, `CONFIDENTIAL` - Classification levels
- `STUFE`, `LEVEL` - Security levels

#### TISAX Specific (en/tisax)
- `LEVEL` - Assessment level
- `NAME` - Entity name

#### Generic Placeholders (multiple handbooks)
- `DATE`, `DATUM` - Date fields
- `TIME`, `ZEIT` - Time fields
- `VERSION` - Version numbers
- `ID` - Identifiers
- `NAME` - Names
- `NUMBER`, `NUMMER` - Numbers
- `NOTES`, `NOTIZEN` - Notes fields
- `NNN` - Numeric placeholder
- `YYYY` - Year placeholder

### Recommended Actions

1. **Add to meta-handbook.yaml** (handbook-specific):
   ```yaml
   # For Common Criteria handbook
   cc1: "[TODO]"
   cc2: "[TODO]"
   cc3: "[TODO]"
   ccportal: "[TODO]"
   # ... etc
   ```

2. **Add to meta-global.yaml** (global placeholders):
   ```yaml
   # Generic date/time placeholders
   date: "[TODO]"
   time: "[TODO]"
   version: "[TODO]"
   ```

3. **Update templates** to use existing placeholders instead of undefined ones

## Configuration Files

Placeholders can be defined in:

| File | Scope | Use For |
|------|-------|---------|
| `meta-global.yaml` | All handbooks | Company info, dates, versions |
| `meta-organisation.yaml` | All handbooks | Organization details, addresses |
| `meta-organisation-roles.yaml` | All handbooks | Role assignments, contacts |
| `templates/*/meta-handbook.yaml` | Specific handbook | Framework-specific values |

## Regular Maintenance

Run this analysis:

- ✅ Before generating handbooks
- ✅ After adding new templates
- ✅ After modifying config files
- ✅ During code reviews
- ✅ As part of CI/CD pipeline

## HTML Report Features

The interactive HTML report includes:

- 📊 **Statistics Dashboard** - Overview of placeholder usage
- 📋 **Interactive Table** - Sortable, scrollable matrix
- 🎨 **Color Coding** - Visual status indicators
- 📝 **Legend** - Clear explanation of symbols
- ⚠️ **Undefined List** - Quick reference for missing placeholders
- 🖨️ **Print-Friendly** - Optimized for printing/PDF export
- 📱 **Responsive** - Works on desktop and mobile

## Example Use Cases

### 1. Before Handbook Generation
```bash
# Check for undefined placeholders
python helpers/generate_placeholder_matrix.py
# Review placeholder_matrix.html
# Fix any red (X) entries
# Generate handbooks
```

### 2. Adding New Handbook
```bash
# Create new handbook template
# Run matrix analysis
python helpers/generate_placeholder_matrix.py
# Check which placeholders are needed
# Add to appropriate config file
```

### 3. Auditing Configuration
```bash
# Generate matrix
python helpers/generate_placeholder_matrix.py
# Review blue (O) entries
# Remove unused placeholders from config
# Clean up configuration files
```

## Troubleshooting

### Issue: No placeholders detected
**Solution:** Check that templates use `{{placeholder}}` or `[PLACEHOLDER]` syntax

### Issue: Too many undefined placeholders
**Solution:** Review templates for typos, add missing placeholders to config files

### Issue: HTML file won't open
**Solution:** Check file permissions, try different browser, verify file size

## Documentation

For more details, see:
- `helpers/README_PLACEHOLDER_MATRIX.md` - Detailed documentation
- `docs/PLACEHOLDER_REFERENCE.md` - Placeholder reference guide
- `docs/CONFIGURATION_REFERENCE.md` - Configuration file guide

## Support

For issues or questions:
1. Check the undefined placeholders list in the HTML report
2. Review the configuration reference documentation
3. Examine existing handbook templates for examples
4. Run the script with verbose output for debugging
