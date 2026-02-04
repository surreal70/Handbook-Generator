# PDF Generation Guide

This guide explains how to generate PDF versions of your handbooks using the Handbook Generator system.

## Available Methods

Three PDF generation scripts are provided, each with different dependencies:

### 1. Python-Based Generator (Recommended) ✅

**Script:** `generate_pdfs.py`

**Advantages:**
- Pure Python solution (no system dependencies)
- Automatic dependency installation
- Works on all platforms (Linux, macOS, Windows)
- Handles Unicode characters correctly
- Professional formatting with ReportLab

**Requirements:**
- Python 3.8+
- pip (Python package manager)

**Dependencies (auto-installed):**
- markdown
- reportlab

**Usage:**
```bash
python generate_pdfs.py
```

The script will automatically offer to install missing dependencies.

### 2. Pandoc with LaTeX

**Script:** `generate_pdfs_pandoc.sh`

**Advantages:**
- High-quality typesetting
- Advanced PDF features
- Professional document layout

**Requirements:**
- pandoc
- XeLaTeX (texlive-xetex)

**Installation:**
```bash
# Ubuntu/Debian
sudo apt-get install pandoc texlive-xetex texlive-fonts-recommended

# macOS
brew install pandoc
brew install --cask mactex
```

**Usage:**
```bash
./generate_pdfs_pandoc.sh
```

### 3. Pandoc with wkhtmltopdf

**Script:** `generate_pdfs_simple.sh`

**Advantages:**
- HTML-based rendering
- Good for web-style layouts
- Handles CSS styling

**Requirements:**
- pandoc
- wkhtmltopdf

**Installation:**
```bash
# Ubuntu/Debian
sudo apt-get install pandoc wkhtmltopdf

# macOS
brew install pandoc wkhtmltopdf
```

**Usage:**
```bash
./generate_pdfs_simple.sh
```

## Quick Start

For most users, the Python-based generator is the easiest option:

```bash
# 1. Ensure you're in the project directory
cd /path/to/Handbook-Generator

# 2. Activate virtual environment (if using one)
source venv/bin/activate

# 3. Run the generator
python generate_pdfs.py

# 4. Check the output
ls -lh PDF_Output/
```

## Output Structure

PDFs are generated in the `PDF_Output/` directory with the same structure as the source:

```
PDF_Output/
├── README.md
├── de/
│   ├── bsi-grundschutz/
│   │   └── bsi-grundschutz_handbook.pdf
│   ├── bcm/
│   │   └── bcm_handbook.pdf
│   ├── isms/
│   │   └── isms_handbook.pdf
│   ├── it-operation/
│   │   └── it-operation_handbook.pdf
│   ├── email-service/
│   │   └── email_service_handbook.pdf
│   └── backup/
│       └── backup_handbook.pdf
└── en/
    ├── bsi-grundschutz/
    │   └── bsi-grundschutz_handbook.pdf
    ├── bcm/
    │   └── bcm_handbook.pdf
    ├── isms/
    │   └── isms_handbook.pdf
    └── it-operation/
        └── it-operation_handbook.pdf
```

## PDF Styling

All generated PDFs include:

- **Page Format:** A4 (210mm × 297mm)
- **Margins:** 2cm on all sides
- **Font Size:** 10pt body text
- **Headings:** Color-coded hierarchy
  - H1: #2c3e50 (dark blue-gray), 24pt
  - H2: #34495e (blue-gray), 18pt
  - H3: #555555 (gray), 14pt
  - H4: #666666 (light gray), 12pt
- **Tables:** Blue headers with alternating row colors
- **Code Blocks:** Gray background with blue left border
- **Footer:** Page numbers (page/total)

## Customization

### Modifying PDF Styles

Edit `generate_pdfs.py` to customize:

```python
# Change page size
pagesize=A4  # Options: A4, LETTER, LEGAL

# Adjust margins
rightMargin=2*cm  # Change to 1.5*cm for narrower margins

# Modify colors
textColor=colors.HexColor('#2c3e50')  # Change heading colors
```

### Adding Custom Metadata

PDFs can include custom metadata by modifying the `SimpleDocTemplate` parameters:

```python
doc = SimpleDocTemplate(
    str(output_path),
    pagesize=A4,
    title="Your Custom Title",
    author="Your Organization",
    subject="Handbook Documentation"
)
```

## Troubleshooting

### Issue: "Missing required packages"

**Solution:** Let the script install them automatically, or install manually:
```bash
pip install markdown reportlab
```

### Issue: "No handbook files found"

**Solution:** Ensure handbooks exist in the `Handbook/` directory:
```bash
ls -la Handbook/de/*/
```

Generate handbooks first if needed:
```bash
python -m src.cli --language de --template isms
```

### Issue: Unicode characters not displaying

**Solution:** Use the Python-based generator (`generate_pdfs.py`) which handles Unicode correctly, or use Pandoc with XeLaTeX instead of pdfLaTeX.

### Issue: Images not appearing in PDF

**Solution:** Ensure diagram files exist in the template directories:
```bash
# Check for diagram files
find templates/ -name "*.png" -o -name "*.jpg"

# Copy diagrams if needed
cp -r templates/de/isms/diagrams/ Handbook/de/isms/
```

### Issue: PDF generation is slow

**Solution:** This is normal for large handbooks (500+ KB). The ISMS handbook takes ~2 seconds to convert. For faster generation, consider:
- Using Pandoc with LaTeX (faster for large documents)
- Generating only specific handbooks by modifying the script

## Performance

Typical generation times on modern hardware:

| Handbook | Size | Time |
|----------|------|------|
| Email Service | 8.5 KB | <0.1s |
| Backup | 2.3 KB | <0.1s |
| BCM | 120 KB | ~0.3s |
| BSI Grundschutz | 280 KB | ~0.7s |
| IT Operations | 350 KB | ~1.1s |
| ISMS | 580 KB | ~1.5s |

**Total for all 10 handbooks:** ~7 seconds

## Integration with CI/CD

To automatically generate PDFs in your CI/CD pipeline:

```yaml
# Example GitHub Actions workflow
- name: Generate Handbook PDFs
  run: |
    python -m pip install markdown reportlab
    python generate_pdfs.py
    
- name: Upload PDFs
  uses: actions/upload-artifact@v3
  with:
    name: handbook-pdfs
    path: PDF_Output/
```

## Best Practices

1. **Version Control:** Don't commit PDFs to git (they're binary and large)
   - Add `PDF_Output/` to `.gitignore`
   - Generate PDFs on-demand or in CI/CD

2. **Regeneration:** Regenerate PDFs whenever handbooks are updated
   ```bash
   # After updating metadata or templates
   python -m src.cli --language de --template isms
   python generate_pdfs.py
   ```

3. **Quality Check:** Always review generated PDFs before distribution
   - Check page breaks
   - Verify table formatting
   - Ensure images are included
   - Validate Unicode characters

4. **Distribution:** Use PDFs for:
   - Audit documentation
   - Stakeholder reviews
   - Training materials
   - Compliance evidence
   - Offline reference

## Support

For issues or questions:
1. Check this guide first
2. Review the `PDF_Output/README.md` for output details
3. Check the main `README.md` for project documentation
4. Review error messages carefully (they usually indicate the issue)

---

**Last Updated:** 2026-02-04  
**Version:** 2.0.0  
**Project:** Handbook Generator
