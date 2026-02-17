# Release Notes - Version 0.0.14

**Release Date:** 2026-02-17  
**Release Type:** Template Structure & Metadata Improvements

## Overview

Version 0.0.14 focuses on standardizing template structure, consolidating metadata, and improving test coverage for handbook diagrams support.

## Key Changes

### 1. Diagrams Structure Standardization

- ✅ **Created comprehensive test suite** (`tests/test_diagrams_structure.py`)
  - 327 tests covering all aspects of diagrams structure
  - Validates directory existence, README files, content quality
  - Checks bilingual symmetry between EN and DE versions
  - All tests passing

- ✅ **Added diagrams subdirectories to all frameworks**
  - Created 46 diagrams directories (23 frameworks × 2 languages)
  - Each directory includes comprehensive README.md with:
    - Purpose and usage guidelines
    - Supported formats (PlantUML, Mermaid, Draw.io, SVG/PNG)
    - Markdown reference syntax
    - Naming conventions for different diagram types

- ✅ **Fixed content issues**
  - Corrected escaped backticks in all 46 README files
  - Ensured proper markdown code block formatting

### 2. Metadata Consolidation

- ✅ **Merged auxiliary placeholders**
  - Found and processed 12 `0000_metadata` subdirectories
  - Extracted auxiliary placeholder sections (1-107 placeholders per framework)
  - Merged into root meta-handbook.yaml files
  - Affected frameworks:
    - common-criteria (3 placeholders)
    - gdpr (1 placeholder)
    - iso-31000 (18 placeholders)
    - iso-38500 (103-107 placeholders)
    - it-operation (65-81 placeholders)
    - nist-csf (63 placeholders)

- ✅ **Removed redundant directories**
  - Deleted all 12 `0000_metadata` subdirectories
  - Cleaner repository structure
  - Single source of truth for metadata

### 3. Version Updates

- ✅ **Updated templateset_version**
  - Changed from "0.1" to "0.2" in all 46 meta-handbook.yaml files
  - Reflects template structure improvements

- ✅ **Updated test validations**
  - Modified `tests/test_metadata_loader_properties.py` to check version >= 0.2
  - Updated `tests/test_template_manager.py` test data to use version 0.2
  - All affected tests passing

## Files Changed

### Core Files
- `src/__init__.py` - Version bump to 0.0.14
- `README.md` - Version badge and notice updated
- `about_versioning/VERSION.md` - Version history updated

### New Files
- `tests/test_diagrams_structure.py` - Comprehensive diagrams test suite
- `templates/*/diagrams/README.md` - 46 new README files

### Modified Files
- `templates/*/*/meta-handbook.yaml` - 46 files updated with:
  - Merged auxiliary placeholders
  - Updated templateset_version to 0.2
- `tests/test_metadata_loader_properties.py` - Version validation updated
- `tests/test_template_manager.py` - Test data updated

### Removed
- `templates/*/0000_metadata/` - 12 subdirectories removed

## Statistics

- **Diagrams directories created:** 46 (23 frameworks × 2 languages)
- **README files created:** 46
- **Metadata files updated:** 46
- **Subdirectories removed:** 12
- **Tests added:** 327
- **Test pass rate:** 100% (327/327)

## Testing

All tests passing:
```bash
pytest tests/test_diagrams_structure.py -v
# 327 passed in 1.24s

pytest tests/test_metadata_loader_properties.py -k "defaults" -v
# 4 passed, 17 deselected
```

## Migration Notes

No migration required. All changes are backward compatible:
- Diagrams directories are optional and don't affect existing functionality
- Auxiliary placeholders merged into existing metadata structure
- Version 0.2 is compatible with version 0.1 templates

## Next Steps

Potential areas for future development:
- Add example diagrams to framework directories
- Create diagram generation utilities
- Enhance metadata validation for auxiliary placeholders
- Document framework-specific placeholder usage

## Contributors

- Andreas Huemmer

---

**Full Changelog:** [VERSION.md](VERSION.md)
