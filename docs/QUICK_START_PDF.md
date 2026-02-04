# Quick Start: PDF Generation

## Generate PDFs in 3 Steps

### Step 1: Activate Environment
```bash
source venv/bin/activate
```

### Step 2: Generate PDFs
```bash
python generate_pdfs.py
```

### Step 3: View Results
```bash
ls -lh PDF_Output/de/*/
ls -lh PDF_Output/en/*/
```

## What You Get

✅ **10 Professional PDF Handbooks**
- 6 German handbooks (de/)
- 4 English handbooks (en/)
- Total size: ~2.6 MB

## Handbook Types

| Type | Framework | German | English |
|------|-----------|--------|---------|
| ISMS | ISO 27001:2022 | ✅ 582 KB | ✅ 520 KB |
| BCM | ISO 22301 | ✅ 123 KB | ✅ 117 KB |
| BSI | BSI 200-x | ✅ 284 KB | ✅ 274 KB |
| IT-Ops | ITIL/ITSM | ✅ 370 KB | ✅ 291 KB |
| Email | Service | ✅ 8.5 KB | - |
| Backup | Procedures | ✅ 2.3 KB | - |

## Output Location

```
PDF_Output/
├── de/          # German PDFs
└── en/          # English PDFs
```

## Features

- A4 format with 2cm margins
- Professional color-coded headings
- Formatted tables and code blocks
- Page numbering
- UTF-8 Unicode support

## Regenerate Anytime

```bash
# After updating handbooks
python generate_pdfs.py
```

## View a PDF

```bash
# Linux
xdg-open PDF_Output/de/isms/isms_handbook.pdf

# macOS
open PDF_Output/de/isms/isms_handbook.pdf

# Windows
start PDF_Output/de/isms/isms_handbook.pdf
```

## Need Help?

See [PDF_GENERATION_GUIDE.md](PDF_GENERATION_GUIDE.md) for detailed documentation.

---

**Generated:** 2026-02-04  
**Time:** ~7 seconds  
**Success Rate:** 100%
