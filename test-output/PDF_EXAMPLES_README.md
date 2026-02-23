# PDF Generation Examples

This directory contains example PDF handbooks generated using the new PDF generation feature with ReportLab engine.

## Generated Examples

### Example 1: ISMS Handbook (without TOC)
- **File**: `en/isms/pdf/isms_handbook.pdf`
- **Template**: Information Security Management System (ISMS)
- **Language**: English
- **Pages**: 316
- **Size**: 574 KB
- **PDF Engine**: ReportLab (pure Python, no system dependencies)
- **TOC**: Not included
- **Page Breaks**: Each chapter (h1) starts on a new page
- **Command Used**:
  ```bash
  ./handbook-generator --language en --template isms --output pdf --pdf-engine reportlab --test --output-dir test-output/example1
  ```

### Example 2: BCM Handbook (with TOC)
- **File**: `en/bcm/pdf/bcm_handbook.pdf`
- **Template**: Business Continuity Management (BCM)
- **Language**: English
- **Pages**: 113
- **Size**: 127 KB
- **PDF Engine**: ReportLab (pure Python, no system dependencies)
- **TOC**: Included with clickable links and proper line breaks
- **Page Breaks**: Each chapter (h1) starts on a new page
- **Command Used**:
  ```bash
  ./handbook-generator --language en --template bcm --output pdf --pdf-engine reportlab --pdf-toc --test --output-dir test-output/example2
  ```

### Example 3: GDPR Handbook (with TOC)
- **File**: `en/gdpr/pdf/gdpr_handbook.pdf`
- **Template**: GDPR Compliance
- **Language**: English
- **Pages**: 208
- **Size**: 284 KB
- **PDF Engine**: ReportLab (pure Python, no system dependencies)
- **TOC**: Included with clickable links and proper line breaks
- **Page Breaks**: Each chapter (h1) starts on a new page
- **Command Used**:
  ```bash
  ./handbook-generator --language en --template gdpr --output pdf --pdf-engine reportlab --pdf-toc --test --output-dir test-output/gdpr-example
  ```

## Recent Improvements

### Page Breaks for Chapters
Each h1 heading (chapter) now automatically starts on a new page, making the document structure clearer and more professional. This ensures:
- ✅ Clear visual separation between major sections
- ✅ Professional document layout
- ✅ Easier navigation and printing
- ✅ Better readability for long documents

### Table of Contents Formatting
The TOC now has proper line breaks and spacing between entries:
- ✅ Each TOC entry appears on its own line
- ✅ Proper spacing before and after entries (spaceBefore/spaceAfter)
- ✅ Correct line height (leading) for readability
- ✅ Hierarchical indentation for h1, h2, h3 levels
- ✅ Clickable links to jump to sections

## Features Demonstrated

### ReportLab Engine
All examples use the ReportLab PDF engine, which:
- ✅ Requires no system dependencies (pure Python)
- ✅ Works on all platforms (Linux, macOS, Windows)
- ✅ Generates high-quality PDFs with proper formatting
- ✅ Supports markdown elements (headings, lists, code blocks, emphasis)
- ✅ Includes table of contents with clickable links (when enabled)
- ✅ Maintains proper page layout and styling
- ✅ Automatically adds page breaks before chapters
- ✅ Proper TOC formatting with line breaks

### PDF Quality Standards
All PDFs meet the quality standards defined in the requirements:
- ✅ Readable fonts (minimum 9pt)
- ✅ Proper line spacing (minimum 1.2)
- ✅ Adequate margins (minimum 1.5cm)
- ✅ Preserved document structure
- ✅ Proper text formatting (bold, italic)
- ✅ Monospace font for code blocks
- ✅ Page breaks for chapters
- ✅ Well-formatted table of contents

## Viewing the PDFs

You can open these PDFs with any standard PDF viewer:
- Linux: `evince`, `okular`, `xpdf`
- macOS: Preview, Adobe Acrobat
- Windows: Adobe Acrobat, Edge, Chrome

## Comparing with WeasyPrint

If you have WeasyPrint installed with system dependencies, you can generate the same handbooks using:

```bash
# ISMS with WeasyPrint
./handbook-generator --language en --template isms --output pdf --pdf-engine weasyprint --test

# BCM with WeasyPrint and TOC
./handbook-generator --language en --template bcm --output pdf --pdf-engine weasyprint --pdf-toc --test
```

## Auto-Detection

The system automatically detects available PDF engines. If you don't specify `--pdf-engine`, it will:
1. Try ReportLab first (recommended for portability)
2. Fall back to WeasyPrint if ReportLab is not available
3. Show an error with installation instructions if neither is available

Example with auto-detection:
```bash
./handbook-generator --language en --template isms --output pdf --test
```

## Technical Details

### PDF Version
Both PDFs use PDF version 1.4, which is widely compatible with all PDF readers.

### Generation Time
- ISMS Handbook (316 pages): ~3-4 seconds
- BCM Handbook (62 pages): ~0.9 seconds

### Processing Statistics

**ISMS Handbook:**
- Documents processed: 70
- Placeholders replaced: 1,000+
- Total words: ~50,000
- Output size: 574 KB

**BCM Handbook:**
- Documents processed: 30
- Placeholders replaced: 326
- Total words: 13,928
- Output size: 102 KB

## Next Steps

To generate your own handbooks:

1. Choose a template from the available options:
   - `isms` - Information Security Management System
   - `bcm` - Business Continuity Management
   - `bsi-grundschutz` - BSI IT-Grundschutz
   - `gdpr` - GDPR Compliance
   - `iso-9001` - ISO 9001 Quality Management
   - And many more...

2. Run the handbook generator:
   ```bash
   ./handbook-generator --language en --template <template-name> --output pdf --pdf-engine reportlab --test
   ```

3. Find your PDF in the output directory:
   ```
   output/en/<template-name>/pdf/<template-name>_handbook.pdf
   ```

## Support

For issues or questions about PDF generation:
- Check the main README.md for detailed documentation
- Review the PDF generation guide in docs/PDF_GENERATION_GUIDE.md
- See installation instructions in requirements.txt
