# PDF Generation Alternatives

## Current Solution: WeasyPrint
- **Pros**: Excellent CSS support, high-quality output
- **Cons**: Requires system libraries (libpango, libcairo, etc.)

## Pure Python Alternatives

### 1. ReportLab (Recommended)
- **Pure Python**: Yes, no system dependencies
- **Pros**: 
  - Mature, stable library
  - No system dependencies
  - Good performance
  - Commercial support available
- **Cons**: 
  - Lower-level API (more code needed)
  - Limited HTML/CSS support (would need custom conversion)
- **Installation**: `pip install reportlab`

### 2. xhtml2pdf (pisa)
- **Pure Python**: Yes
- **Pros**:
  - HTML to PDF conversion
  - No system dependencies
  - Simple API
- **Cons**:
  - Limited CSS support
  - Not actively maintained
  - Lower quality output
- **Installation**: `pip install xhtml2pdf`

### 3. borb
- **Pure Python**: Yes
- **Pros**:
  - Modern, actively maintained
  - Pure Python
  - Good documentation
- **Cons**:
  - Newer library (less battle-tested)
  - More complex API
- **Installation**: `pip install borb`

### 4. fpdf2
- **Pure Python**: Yes
- **Pros**:
  - Simple API
  - No dependencies
  - Good for basic PDFs
- **Cons**:
  - Very limited HTML support
  - Basic styling only
- **Installation**: `pip install fpdf2`

## Recommendation

For this project, I recommend **keeping WeasyPrint** but documenting the system requirements clearly. Here's why:

1. **Quality**: WeasyPrint produces the best quality PDFs with proper CSS support
2. **Existing Code**: Already integrated and working
3. **Documentation**: The system dependency is well-documented and easy to install
4. **Alternative**: Users can skip PDF generation if they don't want to install system libraries

## Installation Documentation

Add to README.md:

```markdown
### PDF Generation (Optional)

PDF generation requires system libraries. If you don't need PDF output, you can skip this step.

#### Ubuntu/Debian:
```bash
sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

#### macOS:
```bash
brew install pango gdk-pixbuf libffi
```

#### Windows:
Download GTK3 runtime from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

#### Skip PDF Generation:
If you don't want to install system libraries, you can still use all other features (HTML and Markdown output).
```

## Implementation Plan

1. Keep WeasyPrint as the default PDF generator
2. Add clear documentation about system requirements
3. Make PDF generation gracefully fail with helpful error message
4. Consider adding a `--skip-pdf` flag for users who don't want PDF output
