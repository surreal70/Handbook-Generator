# Helper Scripts

This directory contains utility scripts for working with the Handbook Generator.

## Batch Generation Scripts

### generate_all_handbooks.sh
**NEW** - Batch generation script for all handbooks in HTML format.

Automatically generates all 4 handbook types (BCM, ISMS, BSI Grundschutz, IT-Operation) in both German and English languages.

**Usage:**
```bash
bash helpers/generate_all_handbooks.sh
```

**Output:**
- 8 complete HTML handbooks (4 types × 2 languages)
- 388 HTML files total
- Organized in test-output/{language}/{type}/html/ directories

**Features:**
- Progress tracking
- Error handling
- Automatic directory creation
- Summary report

### generate_pdfs_pandoc.sh
**NEW** - Batch PDF generation using Pandoc + XeLaTeX.

Generates PDF versions of all handbooks with professional formatting, table of contents, and section numbering.

**Usage:**
```bash
bash helpers/generate_pdfs_pandoc.sh
```

**Output:**
- 8 PDF files (4 types × 2 languages)
- Total size: ~3.4 MB
- Organized in test-output/{language}/{type}/pdf/ directories

**Features:**
- Automatic markdown generation
- Combines separate markdown files
- Adds table of contents
- Section numbering
- Professional formatting
- Unicode support

**Requirements:**
- Pandoc
- XeLaTeX (texlive-xetex package)

**Installation:**
```bash
sudo apt-get install pandoc texlive-xetex
```

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

## Legacy PDF Generation Scripts

The following scripts are alternative PDF generation methods. For production use, we recommend **generate_pdfs_pandoc.sh** which provides the best results.

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
