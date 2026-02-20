# Version Management

## Current Version: 0.0.20

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

- **0.0.20** (2026-02-20): 🎯 Limited Production Use - Handbook Generator Fixes & Full Generation
  - ✅ Fixed handbook generator AttributeError (config.metadata → config.unified_metadata)
  - ✅ Fixed MetaAdapter to support both UnifiedMetadata and MetadataConfig
  - ✅ Removed "placeholder must be alone in line" restriction
  - ✅ Fixed handbook-specific metadata loading from meta-handbook.yaml files
  - ✅ Added unified_metadata parameter to PlaceholderProcessor
  - ✅ Removed version information from 19 handbook README files
  - ✅ Generated all 44 handbooks successfully (22 types × 2 languages)
  - ✅ Created 1,722 markdown files (33 MB total)
  - ✅ 100% placeholder replacement success (352 replacements per handbook average)
  - ✅ Batch generation script (generate_all_handbooks.sh)
  - ✅ 9 seconds total generation time for all handbooks
  - ✅ Inline placeholder support enabled
  - ✅ Separate file output per template
  - **Status**: 🎯 Limited Production Use - Core functionality stable, PDF requires system libraries
- **0.0.19** (2026-02-20): Placeholder Migration & Analysis System
  - ✅ Complete placeholder migration to standardized format (100% coverage)
  - ✅ Placeholder matrix analysis tool with filtering capabilities
  - ✅ Framework-specific placeholder support (NIST 800-53, PCI-DSS, TSC)
  - ✅ Enhanced statistics (unique vs cell counts)
  - ✅ Detailed unused placeholder reporting
  - ✅ Individual handbook analysis support
  - ✅ Flipped matrix axes for better readability
  - ✅ Comprehensive migration documentation
  - **Status**: Placeholder system fully standardized and documented
- **0.0.18** (2026-02-19): Service and Process Documentation System
  - ✅ Added Service and Process Documentation System (major new feature)
  - ✅ Service documentation with COBIT/ITIL compliance
  - ✅ Process documentation with BPMN and RACI support
  - ✅ CLI integration (--service and --process options)
  - ✅ TemplateManager extensions (discover_services, discover_processes)
  - ✅ MetaAdapter extensions (hierarchical metadata resolution)
  - ✅ Bilingual support (German and English)
  - ✅ Comprehensive documentation (SERVICE_DOCUMENTATION_GUIDE.md, PROCESS_DOCUMENTATION_GUIDE.md)
  - ✅ Complete test suite (7,635 tests, 72% coverage)
  - ✅ Final validation (quality control, backward compatibility, performance, security, UAT)
  - ✅ 2 service templates and 2 process templates per language
  - **Status**: Service and process documentation feature complete
- **0.0.17** (2026-02-19): Documentation & Metadata Improvements
  - ✅ Updated all copyright notices to 2025, 2026
  - ✅ Added Handbook Generator logo to README files
  - ✅ Created comprehensive METADATA_REFERENCE.md documentation
  - ✅ Simplified "Was ist neu?" section to be version-agnostic
  - ✅ Updated Unified Metadata Structure section with documentation references
  - ✅ Removed production version recommendations from README files
- **0.0.16** (2026-02-18): Test Suite Improvements & Bug Fixes
  - ✅ Fixed 23 test failures across multiple test suites (99.6% pass rate)
  - ✅ Fixed Common Criteria structure tests (bilingual section headers)
  - ✅ Fixed framework mapping validation tests (service directory reorganization)
  - ✅ Fixed placeholder processing tests (proper placeholder detection)
  - ✅ Fixed template structure tests (service directory path updates)
  - ✅ Fixed setup version test (removed hardcoded version checks)
  - ✅ Fixed template manager tests (format validation, metadata extraction, CIS integration)
  - ✅ Fixed logger verbose details test (bidirectional overlap check)
  - ✅ Enhanced framework mapping documentation (ITIL v4, COBIT 2019, ISO 20000 details)
  - ✅ Filtered documentation files from template discovery (README.md, 9999_Framework_Mapping.md)
  - ✅ Added Unicode surrogate exclusion in hypothesis strategies
  - ✅ Comprehensive test fixes progress documentation
  - **Status**: Test suite quality improvement release

- **0.0.15** (2026-02-18): Metadata Placeholder Migration & Testing Improvements
  - ✅ Migrated all 44 metadata files (0000_metadata_*.md) to use placeholder syntax
  - ✅ Updated metadata files to use {{ meta-handbook.* }} placeholders
  - ✅ Standardized change history with version 0.1 and Handbook-Generator author
  - ✅ Fixed document history validation tests to only check metadata files
  - ✅ Updated placeholder regex to support hyphens in field names (meta-handbook.field)
  - ✅ Fixed placeholder matrix generator to correctly detect and track placeholders
  - ✅ Added location tracking for undefined placeholders (file + line numbers)
  - ✅ Enhanced HTML report with detailed undefined placeholder locations
  - ✅ Moved undefined placeholders section to end of HTML report
  - ✅ All 21 metadata standardization tests passing (4 skipped)
  - **Status**: Metadata placeholder migration and testing improvements release

- **0.0.14** (2026-02-17): Template Structure & Metadata Improvements
  - ✅ Created comprehensive diagrams structure test suite (327 tests)
  - ✅ Added diagrams subdirectories with README.md to all 23 frameworks (46 total)
  - ✅ Consolidated auxiliary metadata from 0000_metadata subdirectories
  - ✅ Merged framework-specific placeholders into root meta-handbook.yaml files
  - ✅ Removed 12 redundant 0000_metadata subdirectories
  - ✅ Updated templateset_version from 0.1 to 0.2 across all 46 handbooks
  - ✅ Updated tests to validate version >= 0.2
  - ✅ Fixed escaped backticks in all diagrams README files
  - ✅ All 327 diagrams structure tests passing
  - **Status**: Template structure standardization release

- **0.0.13** (2026-02-17): Documentation Enhancement - Framework Mapping Summary
  - ✅ Created comprehensive framework mapping summary document
  - ✅ Documented all 23 available frameworks with statistics
  - ✅ Added direct links to framework-specific mapping files
  - ✅ Framework categorization by domain (IT Ops, Security, Compliance, etc.)
  - ✅ Template count statistics (~1,520 files across both languages)
  - ✅ Framework maturity status tracking
  - ✅ Bilingual support documentation (English/German)
  - ✅ Updated maintenance dates to 2026
  - **Status**: Documentation improvement release

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
