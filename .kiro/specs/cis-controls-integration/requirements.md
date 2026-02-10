# Requirements Document: CIS Controls v8 Hardening Templates Integration

## Introduction

This document specifies the requirements for integrating CIS Controls v8 Hardening Templates as a fifth handbook type in the existing handbook generator system. The handbook generator is a Python tool that generates professional handbooks from Markdown templates with placeholder replacement from external data sources. It currently supports BCM, ISMS, BSI Grundschutz, and IT-Operation handbook types with 186 templates across German and English languages.

The CIS Controls v8 Hardening Templates provide a structured approach to documenting and implementing system hardening baselines based on CIS Controls v8 framework. The templates cover foundation concepts, operating system hardening, application hardening, and appendices with 27 template files.

## Glossary

- **Handbook_Generator**: The Python-based system that generates professional handbooks from Markdown templates
- **Template**: A Markdown file with placeholders that gets processed to generate handbook content
- **Handbook_Type**: A category of handbook (BCM, ISMS, BSI Grundschutz, IT-Operation, CIS-Controls)
- **Template_Manager**: The Python class responsible for discovering and managing templates
- **Placeholder**: A token in format `{{ source.field }}` that gets replaced with actual data
- **Metadata_Template**: A special template file named `0000_metadata_[lang]_[type].md` containing handbook metadata
- **Content_Template**: A regular template file with 4-digit numbering (e.g., `0010_filename.md`)
- **CIS_Controls**: Center for Internet Security Controls v8 framework for cybersecurity
- **Hardening_Baseline**: A documented set of security configuration requirements for a platform
- **Output_Format**: The format of generated handbook (HTML, PDF, Markdown)
- **CLI**: Command-Line Interface for the handbook generator
- **Bilingual_Support**: Support for both German and English languages

## Requirements

### Requirement 1: Template File Migration

**User Story:** As a system administrator, I want the CIS Controls templates moved to the proper template structure, so that they can be discovered and processed by the handbook generator.

#### Acceptance Criteria

1. WHEN the system initializes, THE Template_Manager SHALL discover CIS Controls templates in `templates/de/cis-controls/` directory
2. WHEN the system initializes, THE Template_Manager SHALL discover CIS Controls templates in `templates/en/cis-controls/` directory
3. THE System SHALL maintain the 4-digit numbering convention for all CIS Controls templates (0010-0410)
4. THE System SHALL preserve all template content during migration from `input/CIS-Controls-Hardening-Templates/`
5. WHEN templates are migrated, THE System SHALL maintain the original file structure and organization

### Requirement 2: Metadata Template Creation

**User Story:** As a documentation manager, I want metadata templates for CIS Controls handbooks, so that generated handbooks include proper title pages and metadata.

#### Acceptance Criteria

1. THE System SHALL include a metadata template at `templates/de/cis-controls/0000_metadata_de_cis-controls.md`
2. THE System SHALL include a metadata template at `templates/en/cis-controls/0000_metadata_en_cis-controls.md`
3. WHEN a CIS Controls handbook is generated, THE System SHALL render the metadata template as the first page
4. THE Metadata_Template SHALL include handbook title, version, author, and creation date
5. THE Metadata_Template SHALL support placeholder replacement for dynamic metadata values

### Requirement 3: CLI Integration

**User Story:** As a user, I want to generate CIS Controls handbooks via command-line, so that I can integrate handbook generation into automated workflows.

#### Acceptance Criteria

1. WHEN a user runs `./handbook-generator --template cis-controls`, THE CLI SHALL accept the command without errors
2. WHEN a user runs `./handbook-generator -t cis-controls`, THE CLI SHALL accept the short form flag
3. WHEN a user requests available templates, THE System SHALL list "cis-controls" as an available option
4. WHEN a user generates a CIS Controls handbook, THE CLI SHALL support all existing flags (--language, --output, --test, --separate-files, --pdf-toc, --verbose)
5. WHEN invalid parameters are provided, THE CLI SHALL display helpful error messages including "cis-controls" in available options

### Requirement 4: Template Discovery Integration

**User Story:** As a developer, I want the Template_Manager to automatically discover CIS Controls templates, so that no code changes are needed when templates are added or modified.

#### Acceptance Criteria

1. WHEN `discover_templates()` is called, THE Template_Manager SHALL include CIS Controls templates in the returned dictionary
2. WHEN `get_templates('de', 'cis-controls')` is called, THE Template_Manager SHALL return all German CIS Controls templates sorted by sort_order
3. WHEN `get_templates('en', 'cis-controls')` is called, THE Template_Manager SHALL return all English CIS Controls templates sorted by sort_order
4. WHEN `get_available_options()` is called, THE Template_Manager SHALL include 'cis-controls' in the available types for both languages
5. WHEN `validate_template_exists('de', 'cis-controls')` is called, THE Template_Manager SHALL return None (no error) if templates exist

### Requirement 5: Output Format Support

**User Story:** As a security officer, I want to generate CIS Controls handbooks in multiple formats, so that I can share documentation in the most appropriate format for each audience.

#### Acceptance Criteria

1. WHEN output format is HTML, THE System SHALL generate a CIS Controls handbook as an HTML mini-website with navigation
2. WHEN output format is PDF, THE System SHALL generate a CIS Controls handbook as a PDF document with table of contents
3. WHEN output format is Markdown, THE System SHALL generate a CIS Controls handbook as combined or separate Markdown files
4. WHEN `--separate-files` flag is used, THE System SHALL generate individual Markdown files for each template with a TOC.md index
5. WHEN `--pdf-toc` flag is used, THE System SHALL generate PDF with clickable table of contents and page breaks between sections

### Requirement 6: Placeholder Processing

**User Story:** As a template author, I want placeholders in CIS Controls templates to be replaced with actual data, so that handbooks contain organization-specific information.

#### Acceptance Criteria

1. WHEN a CIS Controls template contains `{{ source.field }}` placeholders, THE Placeholder_Processor SHALL replace them with actual values
2. WHEN a placeholder references a non-existent data source, THE System SHALL handle the error gracefully with a clear error message
3. WHEN a placeholder references a non-existent field, THE System SHALL handle the error gracefully with a clear error message
4. THE System SHALL support all existing placeholder sources (netbox, metadata) for CIS Controls templates
5. WHEN placeholder replacement fails, THE System SHALL log the error with template name and placeholder details

### Requirement 7: English Translation

**User Story:** As an international organization, I want CIS Controls handbooks available in English, so that non-German-speaking teams can use the documentation.

#### Acceptance Criteria

1. THE System SHALL include English translations for all 27 CIS Controls templates
2. WHEN generating an English CIS Controls handbook, THE System SHALL use templates from `templates/en/cis-controls/`
3. THE English_Templates SHALL maintain identical structure and numbering as German templates
4. THE English_Templates SHALL preserve all technical content and placeholder references
5. WHEN both languages are available, THE System SHALL allow users to choose between German and English via `--language` flag

### Requirement 8: Documentation Updates

**User Story:** As a new user, I want updated documentation that includes CIS Controls, so that I understand how to generate CIS Controls handbooks.

#### Acceptance Criteria

1. THE README.md SHALL list CIS Controls as a fifth handbook type in the features section
2. THE README.md SHALL include CIS Controls in the handbook types table with template count and description
3. THE README.md SHALL include example commands for generating CIS Controls handbooks
4. THE README.md SHALL document the CIS Controls template structure and organization
5. WHEN users read the documentation, THE System SHALL provide clear guidance on using CIS Controls templates

### Requirement 9: Testing Integration

**User Story:** As a developer, I want comprehensive tests for CIS Controls integration, so that I can ensure the feature works correctly and prevent regressions.

#### Acceptance Criteria

1. THE Test_Suite SHALL include unit tests for CIS Controls template discovery
2. THE Test_Suite SHALL include unit tests for CIS Controls template parsing
3. THE Test_Suite SHALL include integration tests for CIS Controls handbook generation in all formats
4. WHEN all tests are run, THE System SHALL maintain at least 86% code coverage
5. WHEN CIS Controls tests fail, THE System SHALL provide clear error messages indicating the failure reason

### Requirement 10: Backward Compatibility

**User Story:** As an existing user, I want the CIS Controls integration to not break existing functionality, so that I can continue generating BCM, ISMS, BSI Grundschutz, and IT-Operation handbooks without issues.

#### Acceptance Criteria

1. WHEN generating BCM handbooks, THE System SHALL produce identical output as before CIS Controls integration
2. WHEN generating ISMS handbooks, THE System SHALL produce identical output as before CIS Controls integration
3. WHEN generating BSI Grundschutz handbooks, THE System SHALL produce identical output as before CIS Controls integration
4. WHEN generating IT-Operation handbooks, THE System SHALL produce identical output as before CIS Controls integration
5. WHEN existing tests are run, THE System SHALL pass all tests that passed before CIS Controls integration

### Requirement 11: Template Structure Validation

**User Story:** As a quality assurance engineer, I want the system to validate CIS Controls template structure, so that template errors are caught early.

#### Acceptance Criteria

1. WHEN `validate_template_structure()` is called, THE Template_Manager SHALL check CIS Controls templates for proper numbering
2. WHEN a CIS Controls template lacks proper 4-digit numbering, THE System SHALL generate a warning message
3. WHEN a CIS Controls template has invalid filename format, THE System SHALL provide a descriptive warning with the filename and reason
4. THE System SHALL validate that metadata templates follow the naming pattern `0000_metadata_[lang]_cis-controls.md`
5. WHEN validation warnings are generated, THE System SHALL include the template path and suggested corrections

### Requirement 12: Batch Generation Support

**User Story:** As a documentation manager, I want to generate all handbooks including CIS Controls in batch mode, so that I can automate documentation generation.

#### Acceptance Criteria

1. WHEN the batch generation script runs, THE System SHALL include CIS Controls handbooks in the generation queue
2. WHEN generating all handbooks, THE System SHALL create CIS Controls handbooks for both German and English
3. WHEN batch generation completes, THE System SHALL report the number of CIS Controls files generated
4. THE System SHALL generate CIS Controls handbooks in the same output structure as other handbook types
5. WHEN batch generation fails for CIS Controls, THE System SHALL log the error and continue with other handbook types
