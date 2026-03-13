# Template List Generator

## Overview

The `generate_template_list.py` script generates comprehensive reports of all templates across all handbooks in the Handbook-Generator project. It extracts metadata including template names, document IDs, template versions, and revisions from both raw template files and rendered output.

## Features

- **Multiple Source Options**: Report on raw templates, rendered output, or both
- **Automatic Rendering**: Automatically renders handbooks if rendered output is requested but not available
- **Dual Output Formats**: Generates both human-readable text reports and machine-readable JSON data
- **Comprehensive Metadata**: Extracts document ID, template version, revision, and title from each template
- **Multi-Language Support**: Handles all language/handbook combinations in the project

## Usage

### Basic Usage

```bash
# List all raw templates (default)
python helpers/generate_template_list.py

# List raw templates explicitly
python helpers/generate_template_list.py --source raw

# List rendered templates (will render if needed)
python helpers/generate_template_list.py --source rendered

# List both raw and rendered templates
python helpers/generate_template_list.py --source both
```

### Save to File

```bash
# Save report to file (also creates JSON version)
python helpers/generate_template_list.py --source raw --output reports/template_list.txt

# This creates two files:
# - reports/template_list.txt (human-readable report)
# - reports/template_list.json (machine-readable data)
```

### Command-Line Options

- `--source {raw|rendered|both}`: Source of templates to list (default: raw)
  - `raw`: List templates from the `templates/` directory
  - `rendered`: List templates from the `test-output/` directory (renders if needed)
  - `both`: List both raw and rendered templates side-by-side
  
- `--output FILE`, `-o FILE`: Output file path (optional)
  - If specified, writes report to file and creates a JSON version
  - If omitted, prints report to stdout

## Output Format

### Text Report

The text report includes:

```
================================================================================
TEMPLATE LIST REPORT
================================================================================
Source: raw
Total Handbooks: 44
================================================================================

================================================================================
HANDBOOK: de/it-operation
================================================================================

Filename                                           Doc ID               Version      Revision    
-------------------------------------------------- -------------------- ------------ ------------
0000_metadata_de_it-operation.md                   0000                 {{ meta-..   {{ meta-..
0010_Einleitung.md                                 [FRAMEWORK]-0010     [TODO]       [TODO]      
0020_IT_Organisation.md                            [FRAMEWORK]-0020     1.0          [TODO]      
...

Total Templates: 45
```

### JSON Output

The JSON output provides structured data for programmatic access:

```json
{
  "de/it-operation": [
    {
      "filename": "0010_Einleitung.md",
      "title": "1. Einleitung",
      "document_id": "[FRAMEWORK]-0010",
      "template_version": "[TODO]",
      "revision": "[TODO]",
      "source": "raw"
    },
    ...
  ]
}
```

## Use Cases

### Quality Assurance

Check which templates are missing version information:

```bash
python helpers/generate_template_list.py --source raw --output qa/template_audit.txt
# Review the report for templates with [TODO] in version or revision fields
```

### Documentation

Generate a complete inventory of all templates:

```bash
python helpers/generate_template_list.py --source both --output docs/template_inventory.txt
```

### Automation

Use the JSON output for automated processing:

```python
import json

with open('template_list.json') as f:
    data = json.load(f)

# Find all templates missing version info
for handbook, templates in data.items():
    for template in templates:
        if template['template_version'] == '[TODO]':
            print(f"{handbook}/{template['filename']} needs version")
```

### Comparison

Compare raw vs rendered templates to verify rendering:

```bash
python helpers/generate_template_list.py --source both --output comparison/raw_vs_rendered.txt
```

## Metadata Extraction

The script extracts the following metadata from each template:

1. **Title**: First `#` heading in the document
2. **Document ID**: Value from `**Dokument-ID:**` or `**Document-ID:**` field
3. **Template Version**: Value from `**Template Version:**` or `**Template-Version:**` field
4. **Revision**: Value from `**Revision:**` field

## Requirements

- Python 3.8+
- Access to the Handbook-Generator project structure
- For rendered output: Ability to run the handbook-generator CLI

## Integration with Handbook-Generator

The script integrates with the main handbook-generator system:

- Uses the same project structure (`templates/`, `test-output/`)
- Can invoke the CLI to render handbooks on-demand
- Respects the same metadata conventions used throughout the project

## Troubleshooting

### "Rendered output not found"

If you see this warning, the script will automatically attempt to render the handbook. If rendering fails, check:

- The handbook-generator CLI is working: `python -m src.cli --help`
- Required metadata files exist (e.g., `meta-global.yaml`)
- Template files are valid markdown

### "Could not parse file"

This warning indicates a template file couldn't be parsed. Common causes:

- File encoding issues (should be UTF-8)
- Malformed markdown headers
- Missing required metadata fields

### Performance

For large projects with many handbooks:

- Use `--source raw` for faster execution (no rendering needed)
- Use `--source rendered` only when you need to verify rendered output
- Consider running in parallel for different handbook sets if needed

## Examples

### Example 1: Quick Inventory

```bash
# Get a quick count of all templates
python helpers/generate_template_list.py --source raw | grep "Total Templates"
```

### Example 2: Find Missing Versions

```bash
# Generate report and search for TODO markers
python helpers/generate_template_list.py --source raw --output audit.txt
grep "\[TODO\]" audit.txt
```

### Example 3: Verify Rendering

```bash
# Compare raw vs rendered to ensure all templates rendered correctly
python helpers/generate_template_list.py --source both --output verify.txt
```

### Example 4: JSON Processing

```bash
# Generate JSON and process with jq
python helpers/generate_template_list.py --source raw --output list.txt
cat list.json | jq '.["de/it-operation"] | length'
```

## See Also

- [Handbook-Generator Documentation](../README.md)
- [Template Structure Guide](../docs/TEMPLATE_HEADER_SPECIFICATION.md)
- [Metadata Reference](../docs/METADATA_REFERENCE.md)
