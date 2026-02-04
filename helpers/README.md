# Helper Scripts

This directory contains utility scripts for working with the Handbook Generator.

## PDF Generation Scripts

### generate_handbook_pdfs.py
Generates PDF versions of example handbooks from Markdown files using WeasyPrint.

**Usage:**
```bash
python helpers/generate_handbook_pdfs.py
```

**Requirements:**
- WeasyPrint and system dependencies (see docs/PDF_GENERATION_GUIDE.md)

### generate_pdfs.py
Alternative PDF generation using pure Python libraries (markdown + reportlab).

**Usage:**
```bash
python helpers/generate_pdfs.py
```

### generate_pdfs_pandoc.sh
Shell script for PDF generation using Pandoc and LaTeX.

**Usage:**
```bash
bash helpers/generate_pdfs_pandoc.sh
```

**Requirements:**
- Pandoc
- LaTeX distribution (texlive)

### generate_pdfs_simple.sh
Simplified shell script for PDF generation with basic options.

**Usage:**
```bash
bash helpers/generate_pdfs_simple.sh
```

## Template Utilities

### insert_framework_sections.py
Utility for inserting framework-specific sections into templates.

**Usage:**
```bash
python helpers/insert_framework_sections.py
```

## Notes

- These scripts are optional utilities and not required for core functionality
- The main CLI (`python -m src.cli`) handles handbook generation
- PDF generation scripts are alternatives to the built-in PDF generation
- See `docs/` directory for detailed documentation on PDF generation
