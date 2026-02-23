# Implementation Plan: PDF Generation Without Dependencies

## Overview

This implementation plan breaks down the PDF generation feature into discrete coding tasks. The approach follows a layered architecture: first establishing the abstraction layer (interfaces and factory), then implementing each engine, and finally integrating with the CLI. Testing tasks are included as sub-tasks to validate functionality incrementally.

## Tasks

- [x] 1. Set up project structure and core abstractions
  - Create `src/pdf_engines/` directory for PDF engine modules
  - Define `PDFEngine` abstract base class with interface methods
  - Define custom exception classes (`PDFEngineNotAvailableError`, `PDFGenerationError`, `MarkdownConversionError`)
  - Set up testing framework with pytest and hypothesis
  - _Requirements: 1.1, 2.1, 4.1_

- [ ] 2. Implement ReportLab PDF engine
  - [x] 2.1 Create `ReportLabEngine` class implementing `PDFEngine` interface
    - Implement `generate_pdf()` method with markdown to PDF conversion
    - Implement `is_available()` method to check ReportLab installation
    - Implement `get_installation_instructions()` method
    - Add HTML to ReportLab flowables converter (`_html_to_reportlab()`)
    - _Requirements: 1.1, 1.2, 1.3, 1.5_
  
  - [x] 2.2 Write property test for markdown element preservation
    - **Property 2: Markdown Element Preservation**
    - **Validates: Requirements 1.2, 1.5, 6.2, 6.4, 6.5**
  
  - [x] 2.3 Implement TOC support for ReportLab
    - Add `TableOfContents` flowable integration
    - Parse markdown headings and create TOC entries
    - Add page number tracking and linking
    - _Requirements: 1.4, 6.3_
  
  - [x] 2.4 Write property test for TOC generation
    - **Property 4: Table of Contents Generation**
    - **Validates: Requirements 1.4, 5.2, 6.3**
  
  - [x] 2.5 Write unit tests for ReportLab engine
    - Test empty markdown content (edge case)
    - Test special characters and Unicode
    - Test code block rendering with monospace font
    - _Requirements: 1.2, 1.5, 6.4_

- [x] 3. Implement WeasyPrint PDF engine
  - [x] 3.1 Create `WeasyPrintEngine` class implementing `PDFEngine` interface
    - Implement `generate_pdf()` method using WeasyPrint
    - Implement `is_available()` method with system dependency check
    - Implement `get_installation_instructions()` with platform-specific guidance
    - Add default CSS styling (`_get_default_css()`)
    - _Requirements: 2.1, 2.3, 2.4_
  
  - [x] 3.2 Write property test for WeasyPrint CSS styling
    - **Property 10: WeasyPrint CSS Styling Support**
    - **Validates: Requirements 2.4**
  
  - [x] 3.3 Write unit tests for WeasyPrint engine
    - Test error handling when system dependencies missing
    - Test CSS application to PDF output
    - Test TOC generation with WeasyPrint
    - _Requirements: 2.2, 2.3, 4.3_

- [x] 4. Checkpoint - Ensure engine implementations work independently
  - Ensure all tests pass, ask the user if questions arise.

- [x] 5. Implement PDF engine factory and auto-detection
  - [x] 5.1 Create `EngineType` enum with REPORTLAB, WEASYPRINT, AUTO values
    - Define enum class with string values
    - _Requirements: 3.1, 3.2, 3.3_
  
  - [x] 5.2 Create `PDFEngineFactory` class with engine creation logic
    - Implement `create_engine()` method with engine type routing
    - Implement `_auto_detect_engine()` with preference order (ReportLab > WeasyPrint)
    - Implement `_create_reportlab_engine()` with availability check
    - Implement `_create_weasyprint_engine()` with availability check
    - _Requirements: 3.3, 3.4, 3.5, 3.6_
  
  - [x] 5.3 Write property test for engine selection routing
    - **Property 1: Engine Selection Routing**
    - **Validates: Requirements 1.1, 2.1, 3.1, 3.2, 3.3**
  
  - [x] 5.4 Write property test for auto-detection preference
    - **Property 3: Auto-Detection Preference Order**
    - **Validates: Requirements 3.5**
  
  - [x] 5.5 Write unit tests for factory error handling
    - Test error when no engines available
    - Test error when specific engine unavailable
    - Test installation instructions in error messages
    - _Requirements: 3.6, 4.1, 4.2_

- [x] 6. Integrate with CLI
  - [x] 6.1 Add `--pdf-engine` argument to CLI parser
    - Add argument with choices: reportlab, weasyprint, auto
    - Set default value to 'auto'
    - Update help text
    - _Requirements: 3.1, 3.2, 3.3, 3.4_
  
  - [x] 6.2 Update `generate_pdf_output()` function in output_generator.py
    - Accept `engine_type` parameter
    - Create engine using `PDFEngineFactory`
    - Call engine's `generate_pdf()` method
    - Add error handling with user-friendly messages
    - Log which engine was used
    - _Requirements: 5.4, 4.4_
  
  - [x] 6.3 Write property test for backward compatibility
    - **Property 9: Backward Compatibility with Output Flag**
    - **Validates: Requirements 5.1, 5.4**
  
  - [x] 6.4 Write unit tests for CLI integration
    - Test CLI argument parsing for --pdf-engine
    - Test default behavior (auto-detection)
    - Test error messages displayed to user
    - _Requirements: 3.4, 4.2_

- [x] 7. Implement error handling and messaging
  - [x] 7.1 Add comprehensive error messages for all failure modes
    - Engine not available errors with installation instructions
    - PDF generation errors with troubleshooting guidance
    - Markdown conversion errors with problematic content
    - _Requirements: 4.1, 4.2, 4.3, 4.4_
  
  - [x] 7.2 Write property test for error message quality
    - **Property 5: Error Messages Include Installation Instructions**
    - **Validates: Requirements 2.2, 4.1, 4.3**
  
  - [x] 7.3 Write unit tests for error scenarios
    - Test error when engine fails during generation
    - Test error when markdown is malformed
    - Test error when output path is not writable
    - _Requirements: 4.4_

- [-] 8. Update documentation and dependencies
  - [x] 8.1 Update requirements.txt with clear dependency sections
    - Mark reportlab as recommended (pure Python)
    - Mark weasyprint as optional (requires system libs)
    - Add testing dependencies (pytest, hypothesis, PyPDF2)
    - _Requirements: 7.1, 7.2, 7.3_
  
  - [x] 8.2 Update README.md with PDF engine documentation
    - Document --pdf-engine flag usage
    - Explain engine differences and trade-offs
    - Provide installation instructions for both engines
    - Add examples for each engine
    - _Requirements: 7.4_
  
  - [x] 8.3 Add inline code documentation
    - Add docstrings to all public methods
    - Add type hints to all function signatures
    - Add comments explaining complex logic (HTML parsing, TOC generation)
    - _Requirements: 7.4_

- [x] 9. Quality assurance and validation
  - [x] 9.1 Write property test for PDF quality standards
    - **Property 7: PDF Quality Standards**
    - **Validates: Requirements 6.1**
  
  - [x] 9.2 Write property test for engine availability check
    - **Property 8: Engine Availability Check**
    - **Validates: Requirements 1.3, 7.1, 7.2**
  
  - [x] 9.3 Write integration tests for end-to-end workflows
    - Test complete workflow: markdown → ReportLab → PDF
    - Test complete workflow: markdown → WeasyPrint → PDF
    - Test complete workflow with TOC enabled
    - Test auto-detection with both engines available
    - _Requirements: 5.1, 5.2, 5.4_
  
  - [x] 9.4 Run all property tests with 100+ iterations
    - Verify all property tests pass with randomized inputs
    - Check test coverage meets 90% minimum
    - _Requirements: All_

- [x] 10. Final checkpoint - Ensure all tests pass and documentation is complete
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- All tasks are required for comprehensive implementation
- Each task references specific requirements for traceability
- Property tests validate universal correctness properties defined in design
- Unit tests validate specific examples and edge cases
- The implementation follows a bottom-up approach: abstractions → engines → factory → CLI
- ReportLab is prioritized as the default engine for portability
- WeasyPrint remains available for users who need advanced features
