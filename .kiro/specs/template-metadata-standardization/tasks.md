# Implementation Tasks: Template Metadata Standardization

## Overview

This implementation plan breaks down the template metadata standardization into discrete, manageable tasks. The plan covers metadata structure unification, version tracking implementation, service directory reorganization, validation, testing, and documentation.

## Tasks

- [x] 1. Create Metadata Standardizer Tool
  - [x] 1.1 Implement MetadataStandardizer class
    - Create `src/metadata_standardizer.py`
    - Implement `__init__` with templates directory configuration
    - Implement `scan_frameworks()` to discover all frameworks
    - Implement `detect_missing_metadata()` to find missing files
    - _Requirements: 1.1, 4.1, 4.2_
  
  - [x] 1.2 Implement metadata file creation
    - Implement `create_metadata_file(framework, language)`
    - Use unified metadata template structure
    - Initialize template_version to "1.0"
    - Initialize revision to "0"
    - Include framework-specific content (title, purpose, references)
    - _Requirements: 1.2, 1.3, 2.2, 3.2, 4.4, 4.5, 4.6_
  
  - [x] 1.3 Implement metadata enhancement
    - Implement `enhance_existing_metadata(filepath)`
    - Add missing required fields to existing files
    - Add template_version and revision fields
    - Preserve existing content and structure
    - _Requirements: 1.4, 2.1, 3.1_
  
  - [x] 1.4 Implement metadata validation
    - Implement `validate_metadata_structure(filepath)`
    - Check for all 13 required fields
    - Validate template_version format (MAJOR.MINOR)
    - Validate revision is non-negative integer
    - Return ValidationResult with errors and warnings
    - _Requirements: 6.1, 6.2, 6.3, 6.6_
  
  - [x] 1.5 Implement reporting
    - Implement `generate_report()`
    - Count frameworks processed, files created, files enhanced
    - Report validation errors and warnings
    - Generate summary statistics
    - _Requirements: 4.8, 6.7_

- [x] 2. Create Metadata Validation Script
  - [x] 2.1 Implement CLI validation tool
    - Create `helpers/validate_metadata.py`
    - Implement argument parser (--all, --framework, --language, --report)
    - Implement validation for single framework
    - Implement validation for all frameworks
    - _Requirements: 6.8_
  
  - [x] 2.2 Implement validation checks
    - Implement required fields check
    - Implement template_version format check
    - Implement revision number check
    - Implement placeholder syntax check
    - _Requirements: 6.1, 6.2, 6.3, 6.5_
  
  - [x] 2.3 Implement bilingual consistency check
    - Compare DE and EN metadata files
    - Verify matching field structure
    - Check placeholder consistency
    - Report inconsistencies with details
    - _Requirements: 1.7, 6.4_
  
  - [x] 2.4 Implement validation reporting
    - Generate detailed error reports
    - Include framework name, file path, error description
    - Calculate success rate (X of Y frameworks valid)
    - Support JSON output format for --report option
    - _Requirements: 6.6, 6.7_

- [x] 3. Implement Service Directory Reorganization
  - [x] 3.1 Create reorganization script
    - Create `helpers/reorganize_service_directory.py`
    - Implement directory creation for service-directory/
    - Implement safe file moving with verification
    - Implement rollback on errors
    - _Requirements: 5.1, 5.2, 5.3, 5.4_
  
  - [x] 3.2 Move service templates
    - Move templates/de/email-service/ to templates/de/service-directory/email-service/
    - Move templates/de/service-templates/ to templates/de/service-directory/service-templates/
    - Move templates/en/service-templates/ to templates/en/service-directory/service-templates/
    - Verify all files moved successfully
    - _Requirements: 5.2, 5.3, 5.4, 5.5_
  
  - [x] 3.3 Update code references
    - Search for hardcoded paths in Python code
    - Update paths to use service-directory/
    - Update template loading logic if needed
    - _Requirements: 5.7_
  
  - [x] 3.4 Clean up old directories
    - Remove old templates/de/email-service/ directory
    - Remove old templates/de/service-templates/ directory
    - Remove old templates/en/service-templates/ directory
    - Verify no broken links remain
    - _Requirements: 5.6_

- [x] 4. Standardize Metadata for All Frameworks
  - [x] 4.1 Scan and analyze existing metadata
    - Run metadata standardizer scan
    - Generate report of current state
    - Identify frameworks with missing metadata
    - Identify frameworks with incomplete metadata
    - _Requirements: 4.1, 4.7_
  
  - [x] 4.2 Create missing metadata files
    - Create metadata for frameworks missing files
    - Generate both DE and EN variants
    - Use unified structure with all required fields
    - Initialize template_version="1.0" and revision="0"
    - _Requirements: 4.3, 4.4, 4.5_
  
  - [x] 4.3 Enhance existing metadata files - Part 1 (BCM, ISMS, BSI Grundschutz, IT-Operation)
    - Add missing fields to BCM metadata (de/en)
    - Add missing fields to ISMS metadata (de/en)
    - Add missing fields to BSI Grundschutz metadata (de/en)
    - Add missing fields to IT-Operation metadata (de/en)
    - Add template_version and revision to all
    - _Requirements: 1.1, 1.2, 1.3, 2.1, 3.1_
  
  - [x] 4.4 Enhance existing metadata files - Part 2 (CIS Controls, Common Criteria, GDPR, HIPAA)
    - Add missing fields to CIS Controls metadata (de/en)
    - Verify Common Criteria metadata is complete (de/en)
    - Verify GDPR metadata is complete (de/en)
    - Add missing fields to HIPAA metadata (de/en)
    - Add template_version and revision to all
    - _Requirements: 1.1, 1.2, 1.3, 2.1, 3.1_
  
  - [x] 4.5 Enhance existing metadata files - Part 3 (ISO 9001, NIST 800-53, PCI-DSS, TSC)
    - Add missing fields to ISO 9001 metadata (de/en)
    - Add missing fields to NIST 800-53 metadata (de/en)
    - Add missing fields to PCI-DSS metadata (de/en)
    - Add missing fields to TSC metadata (de/en)
    - Add template_version and revision to all
    - _Requirements: 1.1, 1.2, 1.3, 2.1, 3.1_
  
  - [x] 4.6 Verify metadata standardization
    - Run validation on all 12 frameworks
    - Verify all required fields present
    - Verify template_version and revision fields
    - Fix any validation errors
    - _Requirements: 6.1, 6.2, 6.3, 6.7_

- [x] 5. Implement Document History Standardization
  - [x] 5.1 Create DocumentHistoryStandardizer class
    - Create implementation in `src/metadata_standardizer.py` or separate module
    - Implement `scan_template_files()` to find all template markdown files
    - Implement `has_document_history(filepath)` to detect existing sections
    - Implement `generate_history_section(language)` for DE/EN templates
    - _Requirements: 9.1, 9.2, 9.3, 9.4_
  
  - [x] 5.2 Implement document history addition
    - Implement `add_document_history(filepath, language)`
    - Insert section at end of file with proper formatting
    - Skip metadata files (0000_metadata_*.md)
    - Preserve existing file content
    - Add blank line before section for readability
    - _Requirements: 9.1, 9.4_
  
  - [x] 5.3 Implement document history validation
    - Implement `validate_document_history_format(filepath)`
    - Check for presence of "Dokumenthistorie" or "Document History"
    - Verify table format with correct column headers
    - Verify initial row with version 0.1
    - Return validation warnings (not errors) for backward compatibility
    - _Requirements: 9.5, 9.6, 9.8_
  
  - [x] 5.4 Add document history to all template files - Part 1 (BCM, ISMS, BSI Grundschutz, IT-Operation)
    - Scan and add history to BCM templates (de/en)
    - Scan and add history to ISMS templates (de/en)
    - Scan and add history to BSI Grundschutz templates (de/en)
    - Scan and add history to IT-Operation templates (de/en)
    - Verify bilingual consistency
    - _Requirements: 9.1, 9.4, 9.7_
  
  - [x] 5.5 Add document history to all template files - Part 2 (CIS Controls, Common Criteria, GDPR, HIPAA)
    - Scan and add history to CIS Controls templates (de/en)
    - Scan and add history to Common Criteria templates (de/en)
    - Scan and add history to GDPR templates (de/en)
    - Scan and add history to HIPAA templates (de/en)
    - Verify bilingual consistency
    - _Requirements: 9.1, 9.4, 9.7_
  
  - [x] 5.6 Add document history to all template files - Part 3 (ISO 9001, NIST 800-53, PCI-DSS, TSC)
    - Scan and add history to ISO 9001 templates (de/en)
    - Scan and add history to NIST 800-53 templates (de/en)
    - Scan and add history to PCI-DSS templates (de/en)
    - Scan and add history to TSC templates (de/en)
    - Verify bilingual consistency
    - _Requirements: 9.1, 9.4, 9.7_
  
  - [x] 5.7 Verify document history standardization
    - Run validation on all template files
    - Verify all templates have document history sections
    - Verify correct format for DE and EN variants
    - Fix any formatting issues
    - _Requirements: 9.5, 9.6, 9.7_

- [x] 6. Implement Metadata Role Cleanup
  - [x] 6.1 Create MetadataRoleCleanup class
    - Create implementation in `src/metadata_standardizer.py` or separate module
    - Implement `detect_duplicate_roles()` to find semantic duplicates
    - Implement `remove_duplicate_role(role_name)` to remove from YAML
    - Implement `reorganize_it_operations_roles()` to restructure sections
    - Implement `validate_role_structure()` to check organization
    - _Requirements: 10.1, 10.4, 10.5, 10.8_
  
  - [x] 6.2 Remove duplicate datenschutzbeauftragter role
    - Identify datenschutzbeauftragter in metadata.example.yaml
    - Remove datenschutzbeauftragter role definition
    - Verify data_protection_officer role exists
    - Update YAML file preserving formatting and comments
    - _Requirements: 10.1, 10.2_
  
  - [x] 6.3 Reorganize IT operations roles
    - Move it_manager from "Add Custom Roles Here" to "IT Operations Roles"
    - Move sysop from "Add Custom Roles Here" to "IT Operations Roles"
    - Ensure proper section ordering: C-Level → IT Operations → BCM/Security
    - Update section comments to reflect new structure
    - _Requirements: 10.4, 10.5_
  
  - [x] 6.4 Update template references to removed roles
    - Implement `update_template_references(old_role, new_role)`
    - Scan all template files for {{ meta.datenschutzbeauftragter.* }} references
    - Replace with {{ meta.data_protection_officer.* }}
    - Report number of files updated
    - _Requirements: 10.3, 10.7_
  
  - [x] 6.5 Verify role cleanup
    - Run validation to check for duplicate roles
    - Verify datenschutzbeauftragter is removed
    - Verify it_manager and sysop in IT Operations section
    - Verify no broken template references
    - Test handbook generation with cleaned roles
    - _Requirements: 10.8_
  
  - [x] 6.6 Document role cleanup changes
    - Add migration notes explaining datenschutzbeauftragter removal
    - Document new role organization structure
    - Provide examples of updated role references
    - Update metadata.example.yaml comments
    - _Requirements: 10.6_

- [x] 7. Implement Testing
  - [x] 7.1 Create unit tests for metadata standardizer
    - Test framework scanning
    - Test missing metadata detection
    - Test metadata file creation
    - Test metadata enhancement
    - Test validation logic
    - _Requirements: All requirements_
  
  - [x] 7.2 Create unit tests for validation script
    - Test required fields check
    - Test template_version format validation
    - Test revision number validation
    - Test placeholder syntax validation
    - Test bilingual consistency check
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_
  
  - [x] 7.3 Create unit tests for service directory reorganization
    - Test directory creation
    - Test file moving
    - Test rollback on errors
    - Test cleanup of old directories
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.6_
  
  - [x] 7.4 Create unit tests for document history standardization
    - Test document history detection
    - Test document history generation (DE/EN)
    - Test document history addition to files
    - Test document history format validation
    - Test skipping metadata files
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6_
  
  - [x] 7.5 Create unit tests for role cleanup
    - Test duplicate role detection
    - Test role removal from YAML
    - Test role reorganization
    - Test template reference updates
    - Test role structure validation
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.8_
  
  - [x] 7.6 Write property test for metadata completeness
    - **Property 1: Metadata Field Completeness**
    - Test all frameworks have all 13 required fields
    - Test both DE and EN variants
    - **Validates: Requirements 1.1, 1.6**
  
  - [x] 7.7 Write property test for template version format
    - **Property 2: Template Version Format**
    - Test template_version follows MAJOR.MINOR format
    - Test semantic versioning compliance
    - **Validates: Requirements 2.1, 2.4, 2.5, 2.6**
  
  - [x] 7.8 Write property test for revision number validity
    - **Property 3: Revision Number Validity**
    - Test revision is non-negative integer
    - Test revision format
    - **Validates: Requirements 3.1, 3.3, 3.4, 3.5**
  
  - [x] 7.9 Write property test for bilingual consistency
    - **Property 4: Bilingual Consistency**
    - Test DE and EN metadata have identical structure
    - Test placeholder consistency across languages
    - **Validates: Requirements 1.7, 6.4**
  
  - [x] 7.10 Write property test for placeholder syntax
    - **Property 5: Placeholder Syntax Validity**
    - Test all placeholders follow {{ source.field }} format
    - Test no malformed placeholders exist
    - **Validates: Requirements 1.5, 6.5**
  
  - [x] 7.11 Write property test for service directory structure
    - **Property 6: Service Directory Structure**
    - Test service-directory exists with correct structure
    - Test old directories removed
    - **Validates: Requirements 5.1, 5.2, 5.3, 5.5, 5.6**
  
  - [x] 7.12 Write property test for document history presence
    - **Property 7: Document History Presence**
    - Test all template files have document history sections
    - Test correct format for DE and EN variants
    - Test bilingual consistency of history sections
    - **Validates: Requirements 9.1, 9.5, 9.6, 9.7**
  
  - [x] 7.13 Write property test for no duplicate roles
    - **Property 8: No Duplicate Roles**
    - Test metadata.example.yaml has no duplicate roles
    - Test datenschutzbeauftragter is removed
    - Test IT operations roles properly organized
    - **Validates: Requirements 10.1, 10.2, 10.4, 10.5, 10.8**

- [x] 8. Update Documentation
  - [x] 8.1 Update main README.md
    - Document unified metadata structure
    - Explain template_version field and purpose
    - Explain revision field and future use
    - Document service-directory reorganization
    - _Requirements: 8.1, 8.2, 8.3, 8.4_
  
  - [x] 8.2 Create migration guide
    - Document migration steps for existing users
    - Provide examples of running standardizer
    - Explain backward compatibility guarantees
    - Include troubleshooting section
    - _Requirements: 7.6, 8.7_
  
  - [x] 8.3 Create metadata examples
    - Provide complete metadata file examples
    - Show before/after for enhanced metadata
    - Document all required fields with descriptions
    - Include framework-specific examples
    - _Requirements: 8.5_
  
  - [x] 8.4 Document validation process
    - Explain how to run validation script
    - Document validation checks performed
    - Provide examples of validation output
    - Explain how to fix common validation errors
    - _Requirements: 8.6_
  
  - [x] 8.5 Update framework-specific documentation
    - Update README.md in each framework directory
    - Document metadata structure for each framework
    - Update examples to use new metadata fields
    - Document service-directory structure
    - _Requirements: 8.8_
  
  - [x] 8.6 Document document history standardization
    - Explain document history section purpose
    - Document standard format for DE and EN
    - Provide examples of document history sections
    - Explain how to manually add history to custom templates
    - _Requirements: 9.1, 9.2, 9.3, 9.4_
  
  - [x] 8.7 Document role cleanup changes
    - Document removal of datenschutzbeauftragter
    - Explain new role organization structure
    - Provide migration guide for role references
    - Update metadata.example.yaml inline comments
    - _Requirements: 10.2, 10.4, 10.5, 10.6_

- [x] 9. Verify Backward Compatibility
  - [x] 9.1 Test with existing metadata files
    - Test handbook generation with old metadata format
    - Verify no errors with missing template_version/revision
    - Test with minimal metadata (like old CIS Controls)
    - Verify placeholders preserved when data missing
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5_
  
  - [x] 9.2 Test validation warnings vs errors
    - Verify validation warns (not errors) on missing new fields
    - Test that old metadata files don't break validation
    - Verify helpful warning messages
    - _Requirements: 7.7_
  
  - [x] 9.3 Test service template paths
    - Test handbook generation with old service template paths
    - Verify new paths work correctly
    - Test both old and new paths (if temporary support added)
    - _Requirements: 7.1_

- [x] 10. Final Integration and Validation
  - [x] 10.1 Run complete standardization
    - Run metadata standardizer on all frameworks
    - Verify all metadata files created/enhanced
    - Run validation on all frameworks
    - Fix any remaining issues
    - _Requirements: All requirements_
  
  - [x] 10.2 Run complete test suite
    - Run all unit tests
    - Run all property-based tests (minimum 100 iterations)
    - Verify all tests pass
    - Check code coverage
    - _Requirements: All requirements_
  
  - [x] 10.3 Test handbook generation
    - Generate handbooks for all 12 frameworks
    - Test both DE and EN variants
    - Verify HTML, PDF, and Markdown outputs
    - Verify service templates work with new paths
    - _Requirements: 7.1, 7.5_
  
  - [x] 10.4 Generate final report
    - Document all frameworks standardized
    - Report validation results
    - Document any issues or warnings
    - Provide summary statistics
    - _Requirements: 4.8, 6.7_

## Notes

- All tasks reference specific requirements for traceability
- Tasks 4.3, 4.4, 4.5 can be parallelized (different framework groups)
- Tasks 5.4, 5.5, 5.6 can be parallelized (document history for different framework groups)
- Property-based tests should run with minimum 100 iterations
- Backward compatibility must be maintained throughout
- All metadata files must support bilingual (German/English) versions
- Template version initially set to "1.0" for all frameworks
- Revision initially set to "0" for all frameworks
- Document history sections use version "0.1" for initial template creation
- Role cleanup must update all template references to avoid broken placeholders

## Success Criteria

Implementation is complete when:
1. All 12 frameworks have complete metadata with unified structure
2. All metadata files include template_version="1.0" and revision="0"
3. All template files have standardized document history sections
4. Duplicate role "datenschutzbeauftragter" removed from metadata.example.yaml
5. IT operations roles (it_manager, sysop) properly organized
6. Service templates reorganized into service-directory/
7. All validation checks pass (0 errors)
8. All tests pass (unit and property-based, including 8 properties)
9. Documentation updated with migration guide and new features
10. Existing handbook generation continues to work
11. Final report generated with statistics
