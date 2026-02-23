# Version 0.0.22 Release Notes

**Release Date:** 2026-02-23  
**Status:** ⚠️ Experimental PDF Generation - Limited Production Use

## Overview

Version 0.0.22 marks PDF generation as highly experimental and partially broken. While the core handbook generation functionality remains stable and production-ready, direct PDF generation has known issues and is not recommended for production use.

## ⚠️ Critical Changes

### PDF Generation Status

**PDF generation is now marked as HIGHLY EXPERIMENTAL and PARTIALLY BROKEN:**

- **ReportLab Engine:** Functional but with significant limitations
  - ❌ TOC formatting incomplete
  - ❌ Page breaks partially faulty
  - ⚠️ Not production-ready

- **WeasyPrint Engine:** Often non-functional
  - ❌ Requires system libraries (libpango)
  - ❌ Library loading issues common
  - ❌ Frequently fails despite installed dependencies

### Recommended Workflow

**For production use, we strongly recommend:**

1. Generate Markdown output:
   ```bash
   ./handbook-generator -l de -t bcm -o markdown --test
   ```

2. Convert externally with Pandoc:
   ```bash
   pandoc output/de/bcm/markdown/bcm_handbook.md -o bcm.pdf --pdf-engine=xelatex --toc
   ```

This approach provides:
- ✅ Reliable PDF generation
- ✅ Professional formatting
- ✅ Complete TOC with page numbers
- ✅ Consistent page breaks
- ✅ Production-ready output

## What's New

### Documentation Updates

- ✅ Updated version to 0.0.22 in `src/__init__.py`
- ✅ Updated README.md version badge to 0.0.22
- ✅ Added experimental warnings to README.md about PDF generation
- ✅ Updated PDF Engine section with detailed warnings and status indicators
- ✅ Changed recommendation from direct PDF to Markdown→Pandoc workflow
- ✅ Created comprehensive release notes

### Status Indicators

All documentation now clearly indicates:
- ⚠️ PDF generation is experimental
- ❌ Known issues with both engines
- ✅ Markdown generation is stable
- ✅ External conversion is recommended

## Known Issues

### ReportLab Engine

1. **TOC Formatting:**
   - Line breaks not properly rendered
   - Page numbers may be incorrect
   - Formatting inconsistent

2. **Page Breaks:**
   - Not all chapters start on new pages
   - Inconsistent behavior across handbooks
   - Manual adjustment may be needed

### WeasyPrint Engine

1. **Library Loading:**
   - libpango libraries often fail to load
   - OSError: "cannot load library 'libpango-1.0-0'"
   - Occurs even with all dependencies installed

2. **System Dependencies:**
   - Complex dependency chain
   - Platform-specific issues
   - Difficult to troubleshoot

## Migration Guide

### If You're Using Direct PDF Generation

**Before (0.0.21 and earlier):**
```bash
./handbook-generator -l de -t bcm -o pdf --test
```

**After (0.0.22 - Recommended):**
```bash
# Step 1: Generate Markdown
./handbook-generator -l de -t bcm -o markdown --test

# Step 2: Convert with Pandoc
pandoc output/de/bcm/markdown/bcm_handbook.md -o bcm.pdf --pdf-engine=xelatex --toc
```

### If You Must Use Direct PDF Generation

If you absolutely need direct PDF generation (not recommended):

```bash
# Use ReportLab (less broken than WeasyPrint)
./handbook-generator -l de -t bcm -o pdf --pdf-engine reportlab --test

# Expect issues with:
# - TOC formatting
# - Page breaks
# - Overall quality
```

## What Still Works

### Stable Features (Production-Ready)

- ✅ Markdown handbook generation (all 44 handbooks)
- ✅ HTML output generation
- ✅ Placeholder replacement
- ✅ Template processing
- ✅ Metadata handling
- ✅ Service and process documentation
- ✅ Bilingual support (DE/EN)
- ✅ All 22 compliance frameworks

### Test Coverage

- ✅ 7,635 total tests
- ✅ 72% code coverage
- ✅ All core functionality tested
- ✅ Property-based testing for correctness

## Breaking Changes

None. This is a documentation and status update only. All existing functionality continues to work as before.

## Upgrade Instructions

1. Pull latest changes:
   ```bash
   git pull origin main
   ```

2. No code changes required - version update only

3. Update your workflows to use Markdown→Pandoc for PDF generation

## Future Plans

### Short Term (0.0.23)

- Investigate TOC formatting fixes for ReportLab
- Document WeasyPrint troubleshooting steps
- Improve error messages for PDF generation failures

### Long Term (0.1.0)

- Consider removing direct PDF generation entirely
- Focus on Markdown output quality
- Provide better Pandoc integration examples
- Potentially add Pandoc wrapper scripts

## Support

If you encounter issues:

1. **For PDF generation:** Use Markdown→Pandoc workflow
2. **For other issues:** Check existing documentation
3. **For bugs:** Create GitHub issue with details

## Acknowledgments

Thanks to all users who reported PDF generation issues. Your feedback helped us make the honest assessment that direct PDF generation is not production-ready.

## Version Comparison

| Feature | 0.0.21 | 0.0.22 |
|---------|--------|--------|
| Markdown Generation | ✅ Stable | ✅ Stable |
| HTML Generation | ✅ Stable | ✅ Stable |
| PDF - ReportLab | ⚠️ Experimental | ⚠️ Experimental (marked) |
| PDF - WeasyPrint | ⚠️ Experimental | ❌ Often broken (marked) |
| Recommended PDF | Direct generation | Markdown→Pandoc |
| Documentation | Unclear status | Clear warnings |

## Conclusion

Version 0.0.22 is an honest assessment of the current state of PDF generation. While we initially hoped to provide production-ready direct PDF generation, testing has shown that the external Pandoc approach is more reliable and produces better results.

The core handbook generation functionality remains stable and production-ready. Only the direct PDF generation feature is affected by this status change.

---

**Previous Version:** [0.0.21](VERSION_0.0.21_RELEASE_NOTES.md)  
**Version History:** [VERSION.md](VERSION.md)
