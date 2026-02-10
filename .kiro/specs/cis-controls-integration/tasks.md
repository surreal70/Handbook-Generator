# Implementation Plan: CIS Controls v8 Hardening Templates Integration

## Overview

This implementation plan breaks down the CIS Controls integration into discrete, incremental tasks. The approach focuses on template migration first, followed by minimal code changes, comprehensive testing, and documentation updates. Each task builds on previous work to ensure a smooth integration process.

## Tasks

- [x] 1. Prepare CIS Controls template structure
  - Create directory structure for German and English templates
  - Migrate existing templates from input directory
  - Verify template numbering and naming conventions
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [x] 2. Create metadata templates
  - [x] 2.1 Create German metadata template
    - Write `templates/de/cis-controls/0000_metadata_de_cis-controls.md`
    - Include all required metadata fields (title, version, author, date)
    - Add placeholder support for dynamic metadata values
    - _Requirements: 2.1, 2.4, 2.5_
  
  - [x] 2.2 Create English metadata template
    - Write `templates/en/cis-controls/0000_metadata_en_cis-controls.md`
    - Mirror German template structure with English translations
    - Ensure identical placeholder references
    - _Requirements: 2.2, 2.4, 2.5_
  
  - [x] 2.3 Write property test for metadata template positioning
    - **Property 6: Metadata Template First Position**
    - **Validates: Requirements 2.3**
  
  - [x] 2.4 Write property test for metadata required fields
    - **Property 7: Metadata Required Fields Presence**
    - **Validates: Requirements 2.4**

- [x] 3. Translate CIS Controls templates to English
  - [x] 3.1 Translate foundation templates (0010-0050)
    - Translate 5 foundation templates to English
    - Preserve all placeholders and technical terms
    - Maintain identical numbering and structure
    - _Requirements: 7.1, 7.3, 7.4_
  
  - [x] 3.2 Translate operating system templates (0100-0150)
    - Translate 6 OS templates to English
    - Preserve technical configuration details
    - Maintain placeholder references
    - _Requirements: 7.1, 7.3, 7.4_
  
  - [x] 3.3 Translate application templates (0200-0330)
    - Translate 14 application templates to English
    - Preserve technical specifications
    - Maintain placeholder references
    - _Requirements: 7.1, 7.3, 7.4_
  
  - [x] 3.4 Translate appendix templates (0400-0410)
    - Translate 2 appendix templates to English
    - Preserve table structures and formatting
    - Maintain placeholder references
    - _Requirements: 7.1, 7.3, 7.4_
  
  - [x] 3.5 Write property test for bilingual structure consistency
    - **Property 16: Bilingual Structure Consistency**
    - **Validates: Requirements 7.3**
  
  - [x] 3.6 Write property test for placeholder preservation
    - **Property 17: Placeholder Preservation Across Languages**
    - **Validates: Requirements 7.4**

- [x] 4. Update CLI to support CIS Controls
  - [x] 4.1 Add cis-controls to template choices
    - Modify `src/cli.py` argument parser
    - Add 'cis-controls' to choices list for --template flag
    - Update help text with CIS Controls description
    - _Requirements: 3.1, 3.2_
  
  - [x] 4.2 Write unit tests for CLI cis-controls acceptance
    - Test `--template cis-controls` flag acceptance
    - Test `-t cis-controls` short flag acceptance
    - Test that cis-controls appears in help text
    - _Requirements: 3.1, 3.2_
  
  - [x] 4.3 Write property test for CLI flag compatibility
    - **Property 10: CLI Flag Compatibility**
    - **Validates: Requirements 3.4**
  
  - [x] 4.4 Write property test for error message informativeness
    - **Property 11: Error Message Informativeness**
    - **Validates: Requirements 3.5**

- [x] 5. Checkpoint - Verify template discovery
  - Run handbook generator with `--template cis-controls --test`
  - Verify templates are discovered for both languages
  - Verify no errors in template parsing
  - Ask user if any issues arise

- [x] 6. Test template manager integration
  - [x] 6.1 Write property test for template discovery completeness
    - **Property 1: Template Discovery Completeness**
    - **Validates: Requirements 1.1, 1.2, 4.1**
  
  - [x] 6.2 Write property test for template sorting consistency
    - **Property 2: Template Sorting Consistency**
    - **Validates: Requirements 4.2, 4.3**
  
  - [x] 6.3 Write property test for filename convention validation
    - **Property 3: Filename Convention Validation**
    - **Validates: Requirements 1.3, 11.1, 11.2, 11.3, 11.4, 11.5**
  
  - [x] 6.4 Write property test for available options completeness
    - **Property 9: Available Options Completeness**
    - **Validates: Requirements 3.3, 4.4**
  
  - [x] 6.5 Write property test for template existence validation
    - **Property 12: Template Existence Validation**
    - **Validates: Requirements 4.5**
  
  - [x] 6.6 Write unit tests for CIS Controls template discovery
    - Test discovery in German directory
    - Test discovery in English directory
    - Test discovery when directory is empty
    - Test discovery when directory doesn't exist
    - _Requirements: 1.1, 1.2_

- [x] 7. Test output generation for CIS Controls
  - [x] 7.1 Write property test for multi-format output generation
    - **Property 13: Multi-Format Output Generation**
    - **Validates: Requirements 5.1, 5.2, 5.3, 5.4, 5.5**
  
  - [x] 7.2 Write unit tests for Markdown generation
    - Test combined Markdown file generation
    - Test separate Markdown files generation
    - Test TOC.md generation
    - _Requirements: 5.3, 5.4_
  
  - [x] 7.3 Write unit tests for PDF generation
    - Test PDF generation without TOC
    - Test PDF generation with TOC
    - Test PDF with page breaks
    - _Requirements: 5.2, 5.5_
  
  - [x] 7.4 Write unit tests for HTML generation
    - Test HTML mini-website generation
    - Test navigation structure
    - Test styles.css inclusion
    - _Requirements: 5.1_

- [x] 8. Test placeholder processing
  - [x] 8.1 Write property test for placeholder replacement correctness
    - **Property 14: Placeholder Replacement Correctness**
    - **Validates: Requirements 6.1, 6.4**
  
  - [x] 8.2 Write property test for placeholder error handling
    - **Property 15: Placeholder Error Handling**
    - **Validates: Requirements 6.2, 6.3, 6.5**
  
  - [x] 8.3 Write property test for placeholder processing in metadata
    - **Property 8: Placeholder Processing in Metadata**
    - **Validates: Requirements 2.5**
  
  - [x] 8.4 Write unit tests for placeholder replacement in CIS Controls templates
    - Test valid placeholder replacement
    - Test invalid data source handling
    - Test invalid field handling
    - Test error logging
    - _Requirements: 6.1, 6.2, 6.3, 6.5_

- [x] 9. Test backward compatibility
  - [x] 9.1 Write property test for backward compatibility preservation
    - **Property 19: Backward Compatibility Preservation**
    - **Validates: Requirements 10.1, 10.2, 10.3, 10.4**
  
  - [x] 9.2 Write unit tests for existing handbook types
    - Test BCM handbook generation produces identical output
    - Test ISMS handbook generation produces identical output
    - Test BSI Grundschutz handbook generation produces identical output
    - Test IT-Operation handbook generation produces identical output
    - _Requirements: 10.1, 10.2, 10.3, 10.4_

- [x] 10. Checkpoint - Run full test suite
  - Run `pytest --cov=src --cov-report=html`
  - Verify all tests pass
  - Verify code coverage remains at or above 86%
  - Ask user if any test failures occur

- [x] 11. Test language selection functionality
  - [x] 11.1 Write property test for language selection functionality
    - **Property 18: Language Selection Functionality**
    - **Validates: Requirements 7.5**
  
  - [x] 11.2 Write unit tests for language selection
    - Test German CIS Controls handbook generation
    - Test English CIS Controls handbook generation
    - Test language flag controls template selection
    - _Requirements: 7.2, 7.5_

- [x] 12. Update batch generation scripts
  - [x] 12.1 Update generate_all_handbooks.sh
    - Add CIS Controls to handbook types list
    - Add generation commands for German and English
    - Update progress reporting
    - _Requirements: 12.1, 12.2_
  
  - [x] 12.2 Update generate_pdfs_pandoc.sh
    - Add CIS Controls PDF generation
    - Add for both German and English
    - Update file count reporting
    - _Requirements: 12.1, 12.2_
  
  - [x] 12.3 Write property test for output structure consistency
    - **Property 20: Output Structure Consistency**
    - **Validates: Requirements 12.4**
  
  - [x] 12.4 Write property test for batch generation error resilience
    - **Property 21: Batch Generation Error Resilience**
    - **Validates: Requirements 12.5**
  
  - [x] 12.5 Write integration test for batch generation
    - Test batch script includes CIS Controls
    - Test both languages are generated
    - Test file count reporting
    - _Requirements: 12.1, 12.2, 12.3_

- [x] 13. Update documentation
  - [x] 13.1 Update README.md features section
    - Add CIS Controls to handbook types list
    - Update template count (186 → 240 templates)
    - Add CIS Controls description
    - _Requirements: 8.1_
  
  - [x] 13.2 Update README.md handbook types table
    - Add CIS Controls row with template count (27)
    - Add description: "CIS Controls v8 Hardening"
    - Add standards reference: "CIS Controls v8"
    - _Requirements: 8.2_
  
  - [x] 13.3 Add CIS Controls example commands
    - Add example for generating German CIS Controls handbook
    - Add example for generating English CIS Controls handbook
    - Add example for all formats
    - _Requirements: 8.3_
  
  - [x] 13.4 Document CIS Controls template structure
    - Add section describing the 4 template categories
    - Document template numbering (0010-0410)
    - Explain foundation, OS, application, and appendix sections
    - _Requirements: 8.4, 8.5_
  
  - [x] 13.5 Update template directory structure diagram
    - Add cis-controls to directory tree
    - Show both German and English directories
    - Update template counts
    - _Requirements: 8.4_

- [x] 14. Integration testing
  - [x] 14.1 Write end-to-end integration test
    - Test full workflow from CLI to output files
    - Test German CIS Controls handbook generation
    - Test English CIS Controls handbook generation
    - Test all output formats
    - _Requirements: 3.1, 5.1, 5.2, 5.3_
  
  - [x] 14.2 Write integration test for separate files mode
    - Test separate Markdown files generation
    - Test TOC.md creation
    - Test file naming conventions
    - _Requirements: 5.4_
  
  - [x] 14.3 Write integration test for PDF with TOC mode
    - Test PDF with table of contents
    - Test page breaks between sections
    - Test clickable links
    - _Requirements: 5.5_

- [ ] 15. Final checkpoint - Complete system verification
  - Generate all CIS Controls handbooks (German and English, all formats)
  - Verify output files exist and are valid
  - Run complete test suite and verify 86%+ coverage
  - Verify all existing handbook types still work correctly
  - Ask user to review generated handbooks

## Notes

- All tasks are required for comprehensive implementation
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties (minimum 100 iterations each)
- Unit tests validate specific examples and edge cases
- Integration tests verify end-to-end workflows
- The implementation requires minimal code changes (only CLI update)
- Most work involves template migration and comprehensive testing
- Target: Maintain 86%+ code coverage across the entire codebase
