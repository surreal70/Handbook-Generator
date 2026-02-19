# Placeholder Matrix Script - Quick Reference

## Basic Usage

```bash
# Analyze all handbooks
python helpers/generate_placeholder_matrix.py

# Get help
python helpers/generate_placeholder_matrix.py --help
```

## Filtering Options

### By Handbook
```bash
# Analyze specific handbook (both languages)
python helpers/generate_placeholder_matrix.py --handbook isms
python helpers/generate_placeholder_matrix.py -b it-operation
```

### By Language
```bash
# Analyze all handbooks in one language
python helpers/generate_placeholder_matrix.py --language de
python helpers/generate_placeholder_matrix.py -l en
```

### Combined Filters
```bash
# Analyze specific handbook in specific language
python helpers/generate_placeholder_matrix.py -b isms -l de
python helpers/generate_placeholder_matrix.py --handbook nist-csf --language en
```

### Custom Output
```bash
# Specify output filename prefix
python helpers/generate_placeholder_matrix.py -b isms -o my_analysis
# Creates: my_analysis_isms.csv and my_analysis_isms.html
```

## Available Handbooks

```
bcm                 bsi-grundschutz     cis-controls
common-criteria     coso                csa-ccm
dora                gdpr                hipaa
idw-ps-951          isms                iso-31000
iso-38500           iso-9001            it-operation
nist-800-53         nist-csf            pci-dss
soc1                tisax               togaf
tsc
```

## Output Files

### Default (No Filters)
- `placeholder_matrix.csv`
- `placeholder_matrix.html`

### With Handbook Filter
- `placeholder_matrix_{handbook}.csv`
- `placeholder_matrix_{handbook}.html`

### With Language Filter
- `placeholder_matrix_{language}.csv`
- `placeholder_matrix_{language}.html`

### With Both Filters
- `placeholder_matrix_{handbook}_{language}.csv`
- `placeholder_matrix_{handbook}_{language}.html`

## Common Use Cases

### 1. Check Specific Handbook
```bash
python helpers/generate_placeholder_matrix.py -b isms
```

### 2. Review German Handbooks Only
```bash
python helpers/generate_placeholder_matrix.py -l de
```

### 3. Audit Single Handbook Version
```bash
python helpers/generate_placeholder_matrix.py -b it-operation -l en
```

### 4. Generate Custom Report
```bash
python helpers/generate_placeholder_matrix.py -b nist-csf -o nist_audit_2026
```

### 5. Quick Placeholder Check
```bash
# Before committing changes
python helpers/generate_placeholder_matrix.py -b my-handbook
```

## Understanding the Output

### Unique Placeholder Status
- **Used & Defined**: Placeholders that are both used in templates and defined in config
- **Defined but Unused**: Placeholders defined in config but not used (candidates for cleanup)
- **Used but Undefined**: Placeholders used in templates but missing from config (errors!)

### Matrix Cell Counts
- Represents placeholder × handbook combinations
- Useful for understanding overall coverage
- Example: 40 unused placeholders × 44 handbooks = 1,760 cells

## Tips

1. **Start Specific**: Use filters when developing or debugging specific handbooks
2. **Check Before Commit**: Run filtered analysis on changed handbooks
3. **Compare Languages**: Generate separate reports for de/en to check consistency
4. **Custom Names**: Use `-o` for dated or versioned reports
5. **Review HTML**: The HTML report is interactive and easier to navigate than CSV

## Troubleshooting

### "No handbooks found"
- Check handbook name spelling (case-sensitive)
- Use `--help` to see available options
- Verify templates directory structure

### Wrong output location
- Script creates files in current directory
- Use absolute path with `-o` if needed

### Performance
- Single handbook: ~0.3-0.5 seconds
- All handbooks: ~3 seconds
- Use filters for faster iteration

---

For detailed documentation, see `placeholder_matrix_filtering_feature.md`
