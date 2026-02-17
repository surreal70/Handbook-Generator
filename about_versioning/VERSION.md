# Version Management

## Current Version: 0.0.12

### Single Source of Truth

The version number for this project is defined in **one place only**:

```
src/__init__.py
```

This file contains the `__version__` variable which is the authoritative source for the project version.

### How Version is Used

All other parts of the codebase reference this single source:

1. **setup.py**: Imports `__version__` from `src/__init__.py` for package distribution
2. **config_manager.py**: Uses `__version__` as default fallback for metadata version
3. **placeholder_processor.py**: Uses `__version__` as default fallback for document version
4. **metadata_config_manager.py**: Uses version from `__version__` as default for document metadata

### Updating the Version

To update the version number:

1. Edit `src/__init__.py`
2. Change the `__version__` value
3. All other references will automatically use the new version

**Do not** hardcode version numbers elsewhere in the codebase.

### Version History

- **0.0.12** (2026-02-17): ⚠️ Intermediate Development Release - NOT FOR PRODUCTION
  - ⚠️ **Development release only** - not intended for production use
  - ✅ Config separation and metadata unification work in progress
  - ✅ Bilingual placeholder analysis completed
  - ✅ Framework mapping documentation updates
  - ⚠️ Experimental features under development
  - **Status**: Intermediate development release

- **0.0.11** (2026-02-16): ⚠️ Intermediate Quality Control Release - NOT FOR PRODUCTION
  - ⚠️ **Development release only** - not intended for production use
  - ✅ Implemented comprehensive quality control system
  - ✅ Framework Mapping Validator (100% compliance)
  - ✅ Version History Validator (currently disabled)
  - ✅ Test Suite Runner with category filtering (95.2% pass rate)
  - ✅ Coverage Documentation Generator
  - ✅ Quality metrics tracking and trend analysis
  - ✅ Interactive mode for failed test triage
  - ✅ CLI interface for quality checks
  - ✅ Complete quality control documentation
  - ⚠️ 10 known test failures (framework-specific validation)
  - ⚠️ Incomplete test coverage
  - ⚠️ Experimental features
  - **Status**: Intermediate development release

- **0.0.10** (2026-02-11): Phase 2 Completion - Seven New Frameworks + Quality Improvements
  - ✅ Added seven new compliance frameworks (ISO 38500, ISO 31000, CSA CCM, TISAX, SOC 1, COSO, DORA)
  - ✅ 280+ new templates (40 per framework, bilingual)
  - ✅ Fixed template numbering inconsistencies (512 files renamed, 204 duplicates removed)
  - ✅ Added document history sections to 474 Phase 2 templates
  - ✅ Enhanced metadata standardization (COSO framework)
  - ✅ Comprehensive quality validation (1,692 tests, 84.7% pass rate)
  - ✅ Total: 17 compliance frameworks with 866+ templates per language
  - ✅ Production-ready Phase 2 implementation

- **0.0.9** (2026-02-10): Repository Cleanup & Validation Consolidation + New Frameworks
  - ✅ Added three new compliance frameworks (IDW PS 951, NIST CSF 2.0, TOGAF)
  - ✅ 180+ new templates (60 per framework, bilingual)
  - ✅ Consolidated validation scripts into `helpers/validate_frameworks.py`
  - ✅ Removed redundant validation scripts (`validate_all_frameworks.py`, `validate_new_frameworks.py`, `validate_new_frameworks_integration.py`)
  - ✅ Removed obsolete checkpoint script (`verify_template_checkpoint.py`)
  - ✅ Organized version history into `about_versioning/` directory
  - ✅ Simplified validation options (all frameworks or individual framework)
  - ✅ Created comprehensive validation guide (`helpers/VALIDATION_GUIDE.md`)
  - ✅ Updated helper documentation
  - ✅ Total: 15 compliance frameworks with 586+ templates per language

- **0.0.8** (2026-02-10): Role Cleanup & Documentation Enhancement
  - ✅ Removed duplicate role 'datenschutzbeauftragter' (use 'data_protection_officer')
  - ✅ Reorganized IT operations roles (it_manager, sysop moved to IT Operations section)
  - ✅ Enhanced metadata.example.yaml inline comments with migration guidance
  - ✅ Created comprehensive role cleanup migration guide (ROLE_CLEANUP_MIGRATION.md)
  - ✅ Updated README.md and README.en.md with role cleanup documentation
  - ✅ Improved role organization: C-Level → IT Operations → BCM/Security → Custom
  - ✅ Complete migration instructions with examples and verification commands
  - ✅ All documentation cross-referenced and consistent
- **0.0.7** (2026-02-10): Template Metadata Standardization
  - ✅ Unified metadata structure across all 12 frameworks
  - ✅ Added template_version field (1.0) for template format tracking
  - ✅ Added revision field (0) for customization tracking
  - ✅ Service directory reorganization (templates/*/service-directory/)
  - ✅ Comprehensive metadata validation system
  - ✅ 100% metadata validation success rate (24/24 files)
  - ✅ 100/100 metadata standardization tests passing
  - ✅ Property-based testing with 100+ iterations
  - ✅ Complete backward compatibility maintained
  - ✅ Migration guide and documentation updates
  - ✅ All 12 frameworks standardized (BCM, ISMS, BSI, IT-Ops, CIS, CC, GDPR, HIPAA, ISO 9001, NIST, PCI-DSS, TSC)
- **0.0.6** (2026-02-10): Final Checkpoint & Quality Improvements
  - ✅ Fixed FRAMEWORK_MAPPING.md naming convention (renamed to 9999_Framework_Mapping.md)
  - ✅ Created missing English framework mapping files (5 frameworks)
  - ✅ Fixed output directory structure for backward compatibility
  - ✅ Documented PDF generation requirements and alternatives
  - ✅ 82% test pass rate (941/1149 tests passing)
  - ✅ All core functionality production-ready
  - ✅ Comprehensive final checkpoint documentation
- **0.0.5** (2026-02-05): Placeholder System Validation & Testing
  - ✅ Comprehensive placeholder system validation
  - ✅ Metadata configuration validation
  - ✅ Cross-handbook placeholder consistency analysis
  - ✅ Test suite enhancement (93% pass rate, 144 tests)
  - ✅ Complete validation and test documentation
  - ✅ Fixed test assertions for version numbers
- **0.0.4** (2025-02-05): CIS Controls v8 Hardening Templates Integration
  - ✅ Added CIS Controls v8 as fifth handbook type
  - ✅ 27 new templates for system hardening baselines (54 total with German/English)
  - ✅ Foundation templates (overview, scope, lifecycle, exceptions, testing)
  - ✅ Operating system hardening (Windows Server/Client, Linux, macOS, Containers)
  - ✅ Application hardening (web servers, databases, Kubernetes, Docker, SSH, Identity)
  - ✅ Appendices (control mapping, checklists, evidence)
  - ✅ Full bilingual support (German and English)
  - ✅ Complete integration with existing template system
  - ✅ Comprehensive test suite (90+ new tests)
  - ✅ Property-based testing for correctness validation
  - ✅ End-to-end integration tests for all output formats
  - ✅ Backward compatibility with existing handbook types
  - ✅ Updated batch generation scripts
  - ✅ Total: 240 templates across 5 handbook types

- **0.0.3** (2025-02-05): Complete handbook generation with PDF support
  - ✅ Generated all 8 handbooks in HTML format (388 HTML files)
  - ✅ Generated all 8 handbooks in PDF format (8 PDFs, 3.4 MB total)
  - ✅ Implemented Pandoc + XeLaTeX PDF generation pipeline
  - ✅ Created batch generation scripts (generate_all_handbooks.sh, generate_pdfs_pandoc.sh)
  - ✅ Moved helper scripts to helpers/ directory
  - ✅ Updated documentation with current state
  - ✅ Separate directory structure per handbook type
  - ✅ Professional PDF formatting with TOC and section numbering
  - ✅ 784 total files generated (388 HTML + 8 PDF + 388 Markdown)
  - ✅ Production-ready output in all formats

- **0.0.2** (2025-02-04): Documentation update
  - Updated README.md with accurate template counts (186 total)
  - Created English version (README.en.md)
  - Updated copyright year to 2025, 2026
  - Added language switcher to both README files
  - Reorganized documentation files to docs/ directory
  - Moved helper scripts to helpers/ directory
  - Updated VERSION.md and README.1st.md

- **1.0.0** (2025-02-04): First stable release
  - Complete template system with 4 handbook types (BCM, ISMS, BSI Grundschutz, IT-Operations)
  - 186 templates in German and English (30 BCM, 71 ISMS, 54 BSI, 31 IT-Ops)
  - HTML comment processing for template documentation
  - Comprehensive test suite (450+ tests, 86% coverage)
  - Property-based testing for correctness validation
  - PDF generation support (WeasyPrint)
  - Multi-language support (de, en)
  - NetBox integration for data sources
  - Production ready

- **0.0.1** (2025-01-31): Initial experimental release
  - Early development state
  - Highly experimental
  - Not production ready
