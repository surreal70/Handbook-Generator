# Version 0.0.4 Release Notes

**Release Date:** February 5, 2026

## Overview

Version 0.0.4 introduces **CIS Controls v8 Hardening Templates** as the fifth handbook type, expanding the Handbook Generator's capabilities to include comprehensive system hardening documentation based on the CIS Controls v8 framework.

## Major Features

### 🆕 CIS Controls v8 Integration

Added complete support for CIS Controls v8 Hardening Templates:

- **27 new templates** covering system hardening baselines
- **54 total templates** with full German and English support
- **4 template categories**:
  - Foundation (5 templates): Overview, scope, lifecycle, exceptions, testing
  - Operating Systems (6 templates): Windows Server/Client, Linux, macOS, Containers
  - Applications (14 templates): Web servers, databases, Kubernetes, Docker, SSH, Identity
  - Appendices (2 templates): Control mapping, checklists, evidence

### 📚 Template Organization

**Foundation Templates (0010-0050):**
- CIS Controls Overview and Approach
- Scope, Asset Groups and Tiering
- Hardening Lifecycle
- Exceptions and Risk Acceptance
- Testing and Validation

**Operating System Templates (0100-0150):**
- Windows Server Hardening Baseline
- Windows Client Hardening Baseline
- Linux Hardening Baseline
- macOS Hardening Baseline
- Container Base Images Hardening

**Application Templates (0200-0330):**
- Web Server Hardening (Nginx, Apache, IIS, Tomcat)
- Database Hardening (PostgreSQL, MySQL, MS SQL Server)
- Container Platform Hardening (Kubernetes, Docker)
- Service Hardening (SSH, Identity/AD)

**Appendix Templates (0400-0410):**
- Control Mapping Template
- Checklists and Evidence

## Technical Improvements

### ✅ Comprehensive Testing

- **90+ new tests** added to the test suite
- **Property-based tests** for correctness validation
- **Integration tests** for end-to-end workflows
- **765 total tests** passing (up from 450)
- **84% code coverage** maintained

### 🔄 Backward Compatibility

- All existing handbook types (BCM, ISMS, BSI Grundschutz, IT-Operation) work unchanged
- No breaking changes to existing APIs or workflows
- Existing templates and configurations remain fully compatible

### 🌍 Bilingual Support

- Complete German and English translations
- Identical structure and numbering across languages
- Consistent placeholder references
- Language-specific content and terminology

## Updated Statistics

### Template Count
- **Total Templates:** 240 (up from 186)
- **CIS Controls:** 27 templates (54 with DE/EN)
- **BCM:** 30 templates
- **ISMS:** 71 templates
- **BSI Grundschutz:** 54 templates
- **IT-Operation:** 31 templates

### Test Coverage
- **Total Tests:** 765 (up from 450)
- **Code Coverage:** 84%
- **Property Tests:** 100+ iterations each
- **Integration Tests:** Full workflow validation

## Usage Examples

### Generate CIS Controls Handbook

```bash
# German CIS Controls handbook
./handbook-generator --language de --template cis-controls --test

# English CIS Controls handbook
./handbook-generator --language en --template cis-controls --test

# All formats with separate files and PDF TOC
./handbook-generator --language de --template cis-controls --output all --test --separate-files --pdf-toc
```

### Batch Generation

The batch generation scripts have been updated to include CIS Controls:

```bash
# Generate all handbooks including CIS Controls
bash helpers/generate_all_handbooks.sh

# Generate all PDFs including CIS Controls
bash helpers/generate_pdfs_pandoc.sh
```

## Documentation Updates

- Updated README.md with CIS Controls information
- Updated README.en.md with English documentation
- Added CIS Controls to handbook types table
- Updated usage examples with CIS Controls commands
- Updated version badges and statistics

## Breaking Changes

None. This release is fully backward compatible.

## Known Issues

- PDF generation requires system libraries (Pandoc, XeLaTeX)
- Some tests skip if PDF libraries are not available (expected behavior)

## Migration Guide

No migration required. Simply update to version 0.0.4 and start using CIS Controls templates:

1. Pull the latest version
2. Run `./handbook-generator --language de --template cis-controls --test`
3. All existing handbooks continue to work as before

## Contributors

- Andreas Huemmer [andreas.huemmer@adminsend.de]

## Next Steps

Future enhancements may include:
- Additional hardening templates for cloud platforms
- Integration with security scanning tools
- Automated compliance reporting
- Custom template creation tools

---

**Full Changelog:** [VERSION.md](VERSION.md)
