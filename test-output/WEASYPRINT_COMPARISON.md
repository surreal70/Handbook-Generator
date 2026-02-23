# WeasyPrint vs ReportLab Comparison

## Current System Status

WeasyPrint is **not available** on this system because it requires system-level dependencies that are not installed.

### Error Message
```
OSError: cannot load library 'libpango-1.0-0': libpango-1.0-0: cannot open shared object file: No such file or directory
```

This is exactly why we implemented ReportLab as the default PDF engine!

## Engine Comparison

### ReportLab (Default) ✅
**Status**: Available and working

**Advantages**:
- ✅ Pure Python - no system dependencies required
- ✅ Works on all platforms (Linux, macOS, Windows)
- ✅ Easy installation: `pip install reportlab markdown`
- ✅ Portable - works in virtual environments
- ✅ Fast PDF generation
- ✅ Supports TOC with page numbers
- ✅ Proper page breaks for chapters
- ✅ Good quality output

**Limitations**:
- Limited CSS support (uses ReportLab styles instead)
- Less advanced layout features compared to WeasyPrint

**Usage**:
```bash
./handbook-generator --language en --template bcm --output pdf --pdf-engine reportlab --pdf-toc --test
```

### WeasyPrint (Advanced) ❌
**Status**: Not available (missing system dependencies)

**Advantages**:
- Advanced CSS support
- Complex page layouts
- Better typography options
- HTML/CSS rendering engine

**Disadvantages**:
- ❌ Requires system libraries (libpango, libcairo)
- ❌ Installation is platform-specific and complex
- ❌ Not portable across systems
- ❌ Requires root/admin access to install system packages
- ❌ May break when system libraries are updated

**System Dependencies Required**:

**Ubuntu/Debian**:
```bash
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0
pip install weasyprint
```

**Fedora/RHEL**:
```bash
sudo dnf install pango
pip install weasyprint
```

**macOS**:
```bash
brew install pango
pip install weasyprint
```

**Windows**:
See: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

**Usage** (after installation):
```bash
./handbook-generator --language en --template bcm --output pdf --pdf-engine weasyprint --pdf-toc --test
```

## Auto-Detection Feature

The system automatically detects which PDF engine is available:

### Preference Order
1. **ReportLab** (preferred for portability)
2. **WeasyPrint** (fallback if ReportLab not available)
3. **Error** (if neither is available)

### Auto-Detection Usage
```bash
# Let the system choose the best available engine
./handbook-generator --language en --template bcm --output pdf --test

# Explicitly use auto-detection
./handbook-generator --language en --template bcm --output pdf --pdf-engine auto --test
```

## Error Handling

When WeasyPrint is requested but not available, the system provides:

1. ✅ Clear error message explaining the issue
2. ✅ Platform-specific installation instructions
3. ✅ Link to official documentation
4. ✅ Suggestion to use ReportLab as alternative
5. ✅ Graceful exit without crashing

### Example Error Output
```
WeasyPrint is not installed or missing system dependencies.

Install WeasyPrint with:
  pip install weasyprint

System dependencies required:
  Ubuntu/Debian: sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0
  Fedora/RHEL: sudo dnf install pango

For more information, see:
  https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

Alternative: For a pure Python solution without system dependencies,
consider using ReportLab instead:
  pip install reportlab markdown
  Use with: --pdf-engine reportlab
```

## Recommendation

**For most users**: Use ReportLab (the default)
- No system dependencies
- Easy to install and maintain
- Works everywhere
- Produces high-quality PDFs
- Supports all essential features (TOC, page breaks, formatting)

**For advanced users**: Use WeasyPrint only if you:
- Have root/admin access to install system packages
- Need advanced CSS features
- Need complex page layouts
- Are willing to deal with platform-specific installation issues

## Testing Auto-Detection

You can test the auto-detection feature:

```bash
# This will use ReportLab (the only available engine)
./handbook-generator --language en --template bcm --output pdf --test

# This will show an error with installation instructions
./handbook-generator --language en --template bcm --output pdf --pdf-engine weasyprint --test

# This will use ReportLab (auto-detected)
./handbook-generator --language en --template bcm --output pdf --pdf-engine auto --test
```

## Generated Examples

All example PDFs in this repository were generated with **ReportLab** because:
1. It's available on this system
2. It produces excellent quality PDFs
3. It requires no system dependencies
4. It's the recommended default engine

### Available Examples (ReportLab)
- `test-output/en/bcm/pdf/bcm_handbook.pdf` (137 pages with TOC)
- `test-output/en/gdpr/pdf/gdpr_handbook.pdf` (263 pages with TOC)
- `test-output/en/isms/pdf/isms_handbook.pdf` (316 pages)

All PDFs feature:
- ✅ Professional formatting
- ✅ Page breaks for chapters
- ✅ Table of contents with page numbers
- ✅ Clickable links
- ✅ Proper spacing and typography

## Conclusion

The dual-engine approach provides:
- **Portability**: ReportLab works everywhere without system dependencies
- **Flexibility**: WeasyPrint available for users who need advanced features
- **Reliability**: Auto-detection ensures PDFs can always be generated
- **User-Friendly**: Clear error messages guide users to solutions

This design achieves the goal of eliminating mandatory system dependencies while still supporting advanced features for users who want them.
