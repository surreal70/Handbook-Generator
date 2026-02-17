# Implementation Plan: Configuration Separation and Metadata Unification

## Overview

This implementation plan breaks down the configuration separation and metadata unification feature into discrete, incremental coding tasks. The approach follows a bottom-up strategy: build core data models and loaders first, then update processors and managers, then update templates, and finally update tests.

## Tasks

- [x] 1. Create core data models for unified metadata
  - Create `src/unified_metadata.py` with data classes for GlobalMetadata, OrganisationMetadata, RolesMetadata, HandbookMetadata, and UnifiedMetadata
  - Implement `get_field()` method for nested field access using dot notation
  - Implement `__post_init__` for HandbookMetadata to default maintainer to author
  - _Requirements: 1.1, 3.1, 4.1, 5.1, 6.1, 6.2_

- [x] 1.1 Write property test for unified metadata field access
  - **Property 7: Unified Placeholder Replacement**
  - **Validates: Requirements 3.3, 4.3, 5.3, 6.4, 7.2**

- [x] 2. Create metadata loader component
  - [x] 2.1 Create `src/metadata_loader.py` with MetadataLoader class
    - Implement `__init__` to accept data source configuration
    - Implement `_load_yaml()` helper for safe YAML loading
    - Implement `_apply_defaults()` helper for default value application
    - _Requirements: 1.1, 1.3_
  
  - [x] 2.2 Implement global metadata loading
    - Implement `_load_global_metadata()` to load meta-global.yaml
    - Apply defaults: source="HandBook Generator", version="1.0.0"
    - Handle missing file gracefully with defaults
    - _Requirements: 3.1, 3.2_
  
  - [x] 2.3 Implement organisation metadata loading
    - Implement `_load_organisation_metadata()` to load meta-organisation.yaml
    - Apply defaults: all fields default to "[TODO]", revision=0
    - Handle missing file gracefully with defaults
    - _Requirements: 4.1, 4.2_
  
  - [x] 2.4 Implement roles metadata loading
    - Implement `_load_roles_metadata()` to load meta-organisation-roles.yaml
    - Apply defaults: all role fields default to "[TODO]"
    - Validate English role identifiers (role_CEO not rolle_CEO)
    - Handle missing file gracefully with defaults
    - _Requirements: 5.1, 5.2, 5.4_
  
  - [x] 2.5 Implement handbook metadata loading
    - Implement `load_handbook_metadata()` to load meta-handbook.yaml from handbook directory
    - Apply defaults: all fields default to "[TODO]", revision=0, maintainer=author
    - Handle missing file with defaults and warning
    - _Requirements: 6.1, 6.2, 6.5_
  
  - [x] 2.6 Implement unified metadata assembly
    - Implement `load_all_metadata()` to load and merge all global metadata
    - Return UnifiedMetadata object with all metadata sources
    - _Requirements: 1.1_

- [x] 2.7 Write property test for default values
  - **Property 3: Default Values for Missing Configuration**
  - **Validates: Requirements 1.3, 3.2, 4.2, 5.2, 6.5**

- [x] 2.8 Write property test for English role identifiers
  - **Property 14: English Role Identifiers**
  - **Validates: Requirements 5.4**

- [x] 3. Add configuration validation
  - [x] 3.1 Implement YAML syntax validation in MetadataLoader
    - Catch yaml.YAMLError and report file name and line number
    - Provide clear error message with corrective action
    - _Requirements: 9.1, 9.2_
  
  - [x] 3.2 Implement required field validation
    - Validate required fields are present in each metadata file
    - Report missing fields with file name and field name
    - Suggest corrective action
    - _Requirements: 1.4, 9.1, 9.2_
  
  - [x] 3.3 Implement field type validation
    - Validate field types match expected types (string, int, etc.)
    - Report type mismatches with expected vs actual type
    - _Requirements: 1.4, 9.1, 9.2_
  
  - [x] 3.4 Implement circular reference detection
    - Detect circular file references in configuration
    - Report error and halt processing
    - _Requirements: 9.3_

- [x] 3.5 Write property test for configuration validation
  - **Property 4: Configuration Validation**
  - **Validates: Requirements 1.4, 9.1, 9.2**

- [x] 3.6 Write property test for circular reference detection
  - **Property 15: Circular Reference Detection**
  - **Validates: Requirements 9.3**

- [x] 4. Update ConfigManager to use new metadata structure
  - [x] 4.1 Modify ConfigManager.load_config()
    - Remove old metadata.yaml loading code
    - Integrate MetadataLoader for new metadata files
    - Load config.yaml and extract data source references
    - Pass data source config to MetadataLoader
    - _Requirements: 1.1, 2.1_
  
  - [x] 4.2 Update Config dataclass
    - Replace old metadata field with UnifiedMetadata
    - Remove deprecated fields
    - _Requirements: 1.1_
  
  - [x] 4.3 Implement relative path resolution
    - Resolve meta-* file paths relative to config.yaml location
    - Validate paths to prevent directory traversal
    - _Requirements: 2.3_

- [x] 4.4 Write property test for relative path resolution
  - **Property 6: Relative Path Resolution**
  - **Validates: Requirements 2.3**

- [x] 4.5 Create new global configuration files
  - [x] 4.5.1 Create meta-global.yaml
    - Create file in project root with source and version fields
    - Use values from current metadata.yaml if available
    - _Requirements: 3.1, 3.2_
  
  - [x] 4.5.2 Create meta-organisation.yaml
    - Create file in project root with organization fields
    - Migrate data from current metadata.yaml organization section
    - _Requirements: 4.1, 4.2_
  
  - [x] 4.5.3 Create meta-organisation-roles.yaml
    - Create file in project root with role fields
    - Migrate data from current metadata.yaml roles section
    - Ensure all role identifiers use English names
    - _Requirements: 5.1, 5.2, 5.4_
  
  - [x] 4.5.4 Update config.yaml
    - Add data_sources section with references to new meta-* files
    - Keep existing netbox configuration if present
    - _Requirements: 2.1, 2.3_
  
  - [x] 4.5.5 Remove old configuration files
    - Remove metadata.yaml (replaced by meta-* files)
    - Remove metadata.example.yaml (will be replaced by individual examples)
    - Keep backup copies with .old extension for reference
    - _Requirements: Backward incompatibility_

- [x] 4.6 Update test scripts for new configuration structure
  - [x] 4.6.1 Audit test files for old metadata references
    - Search all test files for references to config.metadata
    - Identify tests that need updating to use config.unified_metadata
    - Document which tests are affected
    - _Requirements: All_
  
  - [x] 4.6.2 Update test_config_manager.py
    - Update tests referencing config.metadata to use config.unified_metadata
    - Update tests expecting metadata.yaml to expect meta-* files
    - Remove or update tests for old metadata structure
    - Ensure all property tests still pass
    - _Requirements: 1.1, 2.1_
  
  - [x] 4.6.3 Update other affected test files
    - Update any other test files that reference old metadata structure
    - Ensure integration tests use new configuration format
    - Update test fixtures and mock data
    - _Requirements: All_
  
  - [x] 4.6.4 Verify all tests pass
    - Run full test suite
    - Fix any remaining test failures
    - Ensure no references to old metadata structure remain
    - _Requirements: All_

- [x] 5. Update PlaceholderProcessor for new placeholder format
  - [x] 5.1 Update PLACEHOLDER_PATTERN regex
    - Change pattern to match {{ meta-source.field }} format
    - Support meta-global, meta-organisation, meta-organisation-roles, meta-handbook
    - _Requirements: 7.1, 7.2_
  
  - [x] 5.2 Modify replace_placeholder() method
    - Remove old metadata source handling
    - Route all meta-* placeholders to UnifiedMetadata.get_field()
    - Build full field path (e.g., "meta-organisation.name")
    - Handle unknown sources with clear error messages
    - _Requirements: 3.3, 4.3, 5.3, 6.4, 7.2_
  
  - [x] 5.3 Update __init__ to accept UnifiedMetadata
    - Replace old data_sources parameter with unified_metadata
    - Remove legacy metadata handling
    - _Requirements: 1.1_

- [x] 5.4 Write property test for placeholder format validation
  - **Property 9: English Placeholder Format**
  - **Validates: Requirements 7.1, 7.2**

- [x] 6. Update TemplateManager for handbook-specific metadata
  - [x] 6.1 Modify process_handbook() method
    - Load handbook-specific metadata using MetadataLoader
    - Merge handbook metadata into UnifiedMetadata context
    - Pass updated context to PlaceholderProcessor
    - _Requirements: 1.2_
  
  - [x] 6.2 Add handbook path detection
    - Detect handbook directory from template path
    - Look for meta-handbook.yaml in handbook directory
    - _Requirements: 1.2_

- [x] 6.3 Write property test for handbook metadata loading
  - **Property 2: Handbook Metadata Loading**
  - **Validates: Requirements 1.2**

- [x] 7. Checkpoint - Ensure core functionality works
  - Ensure all tests pass, ask the user if questions arise.

- [x] 8. Create example configuration files
  - [x] 8.1 Create config.example.yaml
    - Include complete structure with data source references
    - Add inline comments explaining each field
    - Include realistic example values
    - Add references to documentation
    - _Requirements: 10.1, 10.2_
  
  - [x] 8.2 Create meta-global.example.yaml
    - Include source and version fields
    - Add inline comments
    - _Requirements: 10.1, 10.2_
  
  - [x] 8.3 Create meta-organisation.example.yaml
    - Include all organisation fields
    - Add inline comments
    - Include realistic example values
    - _Requirements: 10.1, 10.2_
  
  - [x] 8.4 Create meta-organisation-roles.example.yaml
    - Include all required roles
    - Add inline comments
    - Include realistic example values
    - _Requirements: 10.1, 10.2_
  
  - [x] 8.5 Create meta-handbook.example.yaml
    - Include all handbook fields
    - Add inline comments
    - Include realistic example values
    - Note that maintainer defaults to author
    - _Requirements: 10.1, 10.2_

- [x] 8.6 Write property test for example file completeness
  - **Property 17: Example File Completeness**
  - **Validates: Requirements 10.2**

- [x] 9. Update template files with new placeholder format
  - [x] 9.1 Update German BCM templates
    - Replace old placeholders with new format ({{ meta-organisation.name }})
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.2 Update German ISMS templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.3 Update German BSI Grundschutz templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.4 Update German CIS Controls templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.5 Update German Common Criteria templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.6 Update German COSO templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.7 Update German CSA CCM templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.8 Update German DORA templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.9 Update German GDPR templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.10 Update German HIPAA templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.11 Update German IDW PS 951 templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.12 Update German ISO 31000 templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.13 Update German ISO 38500 templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.14 Update German ISO 9001 templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.15 Update German IT Operation templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.16 Update German NIST 800-53 templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.17 Update German NIST CSF templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.18 Update German PCI DSS templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.19 Update German Service Directory templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.20 Update German SOC1 templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.21 Update German TISAX templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.22 Update German TOGAF templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.23 Update German TSC templates
    - Replace old placeholders with new format
    - Add standardized German document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.3_
  
  - [x] 9.24 Update English BCM templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.25 Update English ISMS templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.26 Update English BSI Grundschutz templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.27 Update English CIS Controls templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.28 Update English Common Criteria templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.29 Update English COSO templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.30 Update English CSA CCM templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.31 Update English DORA templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.32 Update English GDPR templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.33 Update English HIPAA templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.34 Update English IDW PS 951 templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.35 Update English ISO 31000 templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.36 Update English ISO 38500 templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.37 Update English ISO 9001 templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.38 Update English IT Operation templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.39 Update English NIST 800-53 templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.40 Update English NIST CSF templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.41 Update English PCI DSS templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.42 Update English Service Directory templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.43 Update English SOC1 templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.44 Update English TISAX templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.45 Update English TOGAF templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_
  
  - [x] 9.46 Update English TSC templates
    - Replace old placeholders with new format
    - Add standardized English document header
    - Remove trailing version information
    - _Requirements: 7.1, 7.5, 8.1, 8.2, 8.3_

- [x] 9.47 Write property test for template header validation
  - **Property 11: Standardized Document Headers**
  - **Validates: Requirements 8.1**

- [x] 9.48 Write property test for localized header labels
  - **Property 12: Localized Header Labels**
  - **Validates: Requirements 8.2**

- [x] 9.49 Write property test for no trailing version info
  - **Property 13: No Trailing Version Information**
  - **Validates: Requirements 8.3**

- [x] 9.50 Write property test for bilingual placeholder consistency
  - **Property 10: Bilingual Placeholder Consistency**
  - **Validates: Requirements 7.3**

- [x] 9.51 Create and process individual handbook configuration files
  - [x] 9.51.1 Identify all handbook directories
    - Scan templates/de and templates/en for handbook directories
    - Create list of all unique handbooks across both languages
    - _Requirements: 1.2, 6.1_
  
  - [x] 9.51.2 Create meta-handbook.yaml for each handbook
    - Create meta-handbook.yaml in each handbook directory (templates/de/[handbook]/0000_metadata/ and templates/en/[handbook]/0000_metadata/)
    - Populate with handbook-specific metadata fields (title, author, revision, etc.)
    - Apply defaults: all fields default to "[TODO]", revision=0, maintainer=author
    - _Requirements: 6.1, 6.2, 6.5_
  
  - [x] 9.51.3 Process existing 0000_metadata files
    - Read existing 0000_metadata.md files in each handbook
    - Extract handbook-specific metadata values
    - Migrate extracted values to new meta-handbook.yaml files
    - Replace existing 0000_metadata content with standardized format (German example):
      ```markdown
      # [Handbook Title] - Metadaten
      **Dokument-ID:** 0000
      **Owner:** {{ meta-handbook.owner }}
      **Revision:** {{ meta-handbook.revision }}
      **Status:** {{ meta-handbook.status }}
      **Klassifizierung:** {{ meta-handbook.classification }}
      **Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
      **Template-Version:** {{ meta-handbook.templateset_version }}
      ---
      ## Handbuch-Informationen
      **Handbuch-Titel:** {{ meta-handbook.longname }}
      **Handbuch-Short:** {{ meta-handbook.shortname }}
      **Organisation:** {{ meta-organisation.name }}
      **Autor:** {{ meta-handbook.author }}
      **Geltungsbereich:** {{ meta-handbook.scope }}
      **Gültig ab:** {{ meta-handbook.valid_from }}
      **Nächste Überprüfung:** {{ meta-handbook.next_review }}
      ```
    - For English handbooks, use English labels (Document-ID, Owner, Revision, Status, Classification, Last Update, Template-Version, Handbook Information, Handbook Title, Handbook Short, Organisation, Author, Scope, Valid from, Next Review)
    - Ensure shortname matches the handbook directory name
    - _Requirements: 1.2, 6.1, 7.1, 7.2_
  
  - [x] 9.51.4 Validate handbook-specific placeholders
    - Scan all template files in each handbook for placeholders
    - Identify handbook-specific placeholders ({{ meta-handbook.* }})
    - Cross-reference with meta-handbook.yaml fields
    - Report any placeholders not covered by configuration
    - _Requirements: 6.4, 7.2, 9.1_
  
  - [x] 9.51.5 Identify missing placeholders in templates
    - Review meta-handbook.yaml fields across all handbooks
    - Check if corresponding placeholders exist in templates
    - Report fields that have no placeholder usage
    - Suggest removal of unused fields or addition of missing placeholders
    - _Requirements: 7.2, 9.1_
  
  - [x] 9.51.6 Verify bilingual consistency for handbook metadata
    - Compare meta-handbook.yaml between German and English versions of same handbook
    - Ensure field structure is consistent (same fields present)
    - Verify placeholder usage is consistent across languages
    - Report any inconsistencies
    - _Requirements: 7.3, 8.2_

- [x] 10. Add TODO value warning system
  - [x] 10.1 Implement TODO detection in PlaceholderProcessor
    - Check if replacement value is "[TODO]"
    - Emit warning but continue processing
    - _Requirements: 9.4_
  
  - [x] 10.2 Add warning collection to ProcessingResult
    - Track TODO warnings separately from other warnings
    - Include field path in warning message
    - _Requirements: 9.4_

- [x] 10.3 Write property test for TODO value warnings
  - **Property 16: TODO Value Warnings**
  - **Validates: Requirements 9.4**

- [x] 11. Update all existing tests
  - [x] 11.1 Update test_config_manager.py
    - Update tests to use new configuration structure
    - Add tests for new metadata loading
    - Update mock data to use new format
    - _Requirements: All_
  
  - [x] 11.2 Update test_placeholder_processor.py
    - Update tests to use new placeholder format
    - Add tests for new metadata sources
    - Update mock data to use UnifiedMetadata
    - _Requirements: 7.1, 7.2_
  
  - [x] 11.3 Update test_template_manager.py
    - Update tests to use new metadata structure
    - Add tests for handbook-specific metadata loading
    - _Requirements: 1.2_
  
  - [x] 11.4 Update integration tests
    - Update end-to-end tests to use new configuration
    - Verify all placeholders are replaced correctly
    - Test multi-handbook processing
    - _Requirements: All_

- [x] 12. Create migration documentation
  - [x] 12.2 Create docs/CONFIGURATION_REFERENCE.md
    - Complete reference for all configuration files
    - Field descriptions and valid values
    - Default values table
    - Examples for each file
    - _Requirements: 10.3_
  
  - [x] 12.3 Create docs/PLACEHOLDER_REFERENCE.md
    - Complete list of all placeholders
    - Organized by metadata source
    - Usage examples
    - Mapping from old to new format
    - _Requirements: 10.3_
  
  - [x] 12.4 Create docs/TEMPLATE_HEADER_SPECIFICATION.md
    - Document header format specification
    - Required fields
    - Language-specific variations
    - Examples for German and English
    - _Requirements: 10.3_

- [x] 12.5 Write property test for documentation completeness
  - **Property 18: Documentation Completeness**
  - **Validates: Requirements 10.3**

- [x] 13. Add old format detection and error reporting
  - [x] 13.1 Implement old format detection in ConfigManager
    - Detect if old metadata.yaml exists
    - Detect if old placeholder format is used in templates
    - _Requirements: Backward incompatibility_
  
  - [x] 13.2 Implement clear error messages
    - Provide error message directing to migration guide
    - List required new configuration files
    - Reference example files
    - _Requirements: Backward incompatibility_

- [x] 14. Final checkpoint - Comprehensive testing
  - Run full test suite including property-based tests (without limiting output with tail/head)
  - Verify all templates process correctly with new configuration
  - Test with missing configuration files (verify defaults work)
  - Test with invalid configuration (verify validation works)
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- All tasks are required for comprehensive implementation
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties with minimum 100 iterations
- Unit tests validate specific examples and edge cases
- All code changes maintain backward incompatibility (no support for old format)
- Focus on clear error messages and helpful defaults throughout implementation


## Post-Implementation Test Failure Analysis

After completing the configuration refactoring, 185 test failures were identified. These tasks will systematically analyze each category of failures and determine the appropriate resolution strategy.

- [x] 15. Analyze bilingual placeholder consistency failures (45 tests)
  - Analyze test failures in `test_bilingual_placeholder_consistency.py` and `test_bilingual_consistency_phase2.py`
  - Identify specific templates with placeholder mismatches between DE/EN versions
  - Common issue: EN templates have `{{ meta.author }}` but DE templates don't
  - Document affected templates and placeholder differences
  - Ask user: Should we (A) fix templates to match, (B) update tests to allow differences, or (C) investigate why differences exist?
  - _Related Requirements: 7.3, 8.2_

- [x] 16. Analyze trailing version information failures (37 tests)
  - Analyze test failures in `test_no_trailing_version_info.py`
  - Identify templates that have "Document History" sections at the end instead of only in headers
  - Document affected templates (e.g., ISO 31000, ISO 38500, NIST CSF, BCM, IT Operation templates)
  - Ask user: Should we (A) remove trailing version info from templates, (B) update tests to allow it, or (C) define a new versioning scheme first?
  - _Related Requirements: 8.3_
 
- [x] 17. Analyze compliance framework output failures (28 tests)
  - Analyze test failures in `test_compliance_framework_output.py`
  - Identify specific framework validation issues
  - ignore pdf related errors
  - Document which frameworks are affected and what validations are failing
  - Ask user: Should we (A) fix framework-specific issues, (B) update test expectations, or (C) investigate if these are real bugs?
  - _Related Requirements: Various framework-specific requirements_

- [x] 18. Analyze template structure failures (13 tests)
  - Analyze test failures in `test_template_structure.py`
  - Issues include: template numbering (9999 templates), documentation files missing, template counts
  - Document specific structural issues found
  - Ask user: Should we (A) fix template structure issues, (B) update test expectations, or (C) defer to separate template cleanup task?
  - _Related Requirements: Template organization requirements_

- [x] 19. Analyze metadata standardization failures (9 tests)
  - Analyze test failures in `test_metadata_standardization_properties.py`
  - Issues include: missing fields, invalid version formats, placeholder syntax, document history presence
  - Document specific metadata issues found
  - Ask user: Should we (A) fix metadata files, (B) update tests for new structure, or (C) investigate if these are configuration bugs?
  - _Related Requirements: 1.1, 3.1, 4.1, 5.1, 6.1, 8.3_

- [x] 20. Analyze CIS controls integration failures (9 tests)
  - Analyze test failures in `test_cis_controls_integration.py`
  - Issues include: metadata required fields, placeholder replacement, error handling
  - Document specific CIS-related issues
  - Ask user: Should we (A) fix CIS templates/metadata, (B) update tests for new configuration, or (C) investigate placeholder processing bugs?
  - _Related Requirements: 7.1, 7.2, CIS-specific requirements_

- [x] 21. Analyze quality control test failures (8 tests)
  - Analyze test failures in `test_quality_control_integration.py` and `test_quality_control_orchestrator.py`
  - Main issue: Tests expect version_history_compliance=100% but get 0% (validation is intentionally disabled)
  - Document quality control expectations vs reality
  - Ask user: Should we (A) update tests to accept disabled validation, (B) re-enable version history validation, or (C) remove these tests until versioning scheme is defined?
  - _Related Requirements: Quality control requirements_

- [x] 22. Analyze miscellaneous test failures (36 tests)
  - Analyze remaining test failures across various test files
  - Categories include: Common Criteria structure, framework mapping validation, ISO properties, template manager issues, etc.
  - Document each unique failure type
  - Ask user for each category: Should we (A) fix the issue, (B) update the test, or (C) investigate further?
  - _Related Requirements: Various_

- [ ] 23. Create consolidated test failure resolution plan
  - Based on user decisions from tasks 15-22, create a prioritized action plan
  - Group similar fixes together for efficiency
  - Estimate effort for each resolution
  - Create sub-tasks for implementation if needed
  - _Related Requirements: All_

- [ ] 24. Execute test failure resolutions
  - Implement fixes based on the consolidated resolution plan
  - Run tests after each category of fixes
  - Document any new issues discovered during fixes
  - Ensure test pass rate improves incrementally
  - _Related Requirements: All_

- [ ] 25. Final verification after test failure resolution
  - Run complete test suite
  - Verify all critical tests pass
  - Document any remaining acceptable failures (if any)
  - Update documentation with any lessons learned
  - _Related Requirements: All_


## IT Operation Translation Tasks

These tasks were identified during Task 18 analysis. The English translations of IT Operation templates are incomplete (26-62% complete). See `IT_OPERATION_TRANSLATION_TASKS.md` for detailed information.

### Priority 1: Critical Templates (Most Incomplete)

- [x] T1. Translate 0280_Compliance_and_Audits.md
  - Current: 300 lines (26% complete), Target: 1167 lines
  - Missing: 867 lines
  - Estimated effort: 2.5 hours
  - Priority: CRITICAL

- [x] T2. Translate 0240_Runbooks_Standard_Operations.md
  - Current: 380 lines (42% complete), Target: 904 lines
  - Missing: 524 lines
  - Estimated effort: 1.5 hours
  - Priority: CRITICAL

- [x] T3. Translate 0250_Tooling_and_Access_Methods.md
  - Current: 206 lines (34% complete), Target: 602 lines
  - Missing: 396 lines
  - Estimated effort: 1.2 hours
  - Priority: CRITICAL

### Priority 2: High-Impact Templates

- [x] T4. Translate 0260_Known_Issues_and_FAQ.md
  - Current: 289 lines (46% complete), Target: 632 lines
  - Missing: 343 lines
  - Estimated effort: 1.0 hour
  - Priority: HIGH

- [x] T5. Translate 0190_Log_Management_and_Audit.md
  - Current: 526 lines (61% complete), Target: 862 lines
  - Missing: 336 lines
  - Estimated effort: 1.0 hour
  - Priority: HIGH

- [x] T6. Translate 0210_Availability_and_Service_Level.md
  - Current: 191 lines (40% complete), Target: 472 lines
  - Missing: 281 lines
  - Estimated effort: 0.8 hours
  - Priority: HIGH

### Priority 3: Standard Templates

- [x] T7. Translate 0270_Contacts_Escalation_and_Vendors.md
  - Current: 278 lines (53% complete), Target: 527 lines
  - Missing: 249 lines
  - Estimated effort: 0.7 hours
  - Priority: MEDIUM

- [x] T8. Translate 0230_Maintenance_and_Operations_Routines.md
  - Current: 388 lines (62% complete), Target: 628 lines
  - Missing: 240 lines
  - Estimated effort: 0.7 hours
  - Priority: MEDIUM

- [x] T9. Translate 0200_Capacity_and_Performance_Management.md
  - Current: 204 lines (48% complete), Target: 423 lines
  - Missing: 219 lines
  - Estimated effort: 0.6 hours
  - Priority: MEDIUM

- [x] T10. Translate 0220_Data_Management_and_Privacy.md
  - Current: 281 lines (59% complete), Target: 474 lines
  - Missing: 193 lines
  - Estimated effort: 0.5 hours
  - Priority: MEDIUM

**Total Translation Work**: 3,648 lines across 10 templates, estimated 8-12 hours

**Note**: Template 0290 was already completed during Task 18 (92% complete, within acceptable range).
