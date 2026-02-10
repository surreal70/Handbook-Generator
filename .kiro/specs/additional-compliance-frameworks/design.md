# Design Document: Additional Compliance Frameworks

## Overview

This design document specifies the implementation approach for adding three new compliance framework template sets to the handbook generator system: IDW PS 951 (German IT auditing standard), NIST Cybersecurity Framework (CSF) 2.0, and TOGAF (The Open Group Architecture Framework).

The implementation will follow the established template architecture pattern used by the existing 13 frameworks, ensuring seamless integration with the Template_Manager, Placeholder_System, Validation_System, and Output_Generator components. Each framework will provide bilingual templates (German and English) with structured markdown content, placeholder support, and comprehensive framework mapping documentation.

## Architecture

### System Context

The handbook generator system follows a modular architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                    Handbook Generator CLI                    │
└───────────────────────────┬─────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐   ┌──────────────┐   ┌──────────────┐
│   Template    │   │ Placeholder  │   │  Validation  │
│   Manager     │   │   System     │   │   System     │
└───────┬───────┘   └──────┬───────┘   └──────┬───────┘
        │                  │                   │
        └──────────────────┼───────────────────┘
                           │
                           ▼
                   ┌──────────────┐
                   │   Output     │
                   │  Generator   │
                   └──────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
    HTML Output       PDF Output       Markdown Output
```

### Template Directory Structure

Each new framework will follow this directory structure:

```
templates/
├── de/
│   ├── idw-ps-951/
│   │   ├── 0000_metadata_de_idw-ps-951.md
│   │   ├── 0010_audit_planning.md
│   │   ├── 0020_risk_assessment.md
│   │   ├── ...
│   │   ├── diagrams/
│   │   ├── FRAMEWORK_MAPPING.md
│   │   └── README.md
│   ├── nist-csf/
│   │   ├── 0000_metadata_de_nist-csf.md
│   │   ├── 0010_govern_overview.md
│   │   ├── 0020_organizational_context.md
│   │   ├── ...
│   │   ├── diagrams/
│   │   ├── FRAMEWORK_MAPPING.md
│   │   └── README.md
│   └── togaf/
│       ├── 0000_metadata_de_togaf.md
│       ├── 0010_preliminary_phase.md
│       ├── 0020_architecture_vision.md
│       ├── ...
│       ├── diagrams/
│       ├── FRAMEWORK_MAPPING.md
│       └── README.md
└── en/
    ├── idw-ps-951/
    ├── nist-csf/
    └── togaf/
```

## Components and Interfaces

### Template Structure

Each template file follows this standard structure:

```markdown
---
Document-ID: {framework}-{number}
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Template Title

## Purpose

[Description of what this template documents]

## Scope

[What is covered and what is not covered]

## Section 1

[Content with placeholders like {{ source.organization_name }}]

### Subsection 1.1

[Detailed content]

## Section 2

[More content]

<!-- Author notes: Additional guidance for template users -->
```

### Metadata Template Structure

Each framework requires metadata templates:

```markdown
---
title: "{Framework Name} Handbook"
author: "{{ source.author }}"
version: "1.0"
date: "{{ source.date }}"
organization: "{{ source.organization_name }}"
classification: "Internal"
---

# Metadata

This file contains metadata for the {Framework Name} handbook.
```

### Framework-Specific Template Organization

#### IDW PS 951 Template Organization

Number ranges for IDW PS 951 templates:

- **0010-0099**: Audit Planning and Preparation
  - 0010: Audit planning overview
  - 0020: Audit scope definition
  - 0030: Risk assessment methodology
  - 0040: Audit team and resources
  - 0050: Audit timeline and milestones

- **0100-0199**: IT Strategy and Organization
  - 0100: IT strategy evaluation
  - 0110: IT governance structure
  - 0120: IT organization and roles
  - 0130: IT steering committee
  - 0140: IT service management

- **0200-0299**: IT Processes
  - 0200: Process overview
  - 0210: Change management
  - 0220: Incident management
  - 0230: Problem management
  - 0240: Release management
  - 0250: Configuration management

- **0300-0399**: IT Systems and Applications
  - 0300: Application landscape
  - 0310: System architecture
  - 0320: Application controls
  - 0330: Interface management
  - 0340: Data integrity controls

- **0400-0499**: IT Infrastructure and Operations
  - 0400: Infrastructure overview
  - 0410: Server and storage systems
  - 0420: Network infrastructure
  - 0430: Database systems
  - 0440: Backup and recovery
  - 0450: IT operations procedures

- **0500-0599**: IT Security and Data Protection
  - 0500: Security strategy
  - 0510: Access control
  - 0520: Encryption and key management
  - 0530: Security monitoring
  - 0540: Data protection compliance
  - 0550: Privacy controls

#### NIST CSF 2.0 Template Organization

Number ranges for NIST CSF 2.0 templates:

- **0010-0099**: Govern Function
  - 0010: Governance overview
  - 0020: Organizational context
  - 0030: Risk management strategy
  - 0040: Roles and responsibilities
  - 0050: Policy framework
  - 0060: Oversight and accountability
  - 0070: Supply chain risk management

- **0100-0199**: Identify Function
  - 0100: Asset management
  - 0110: Business environment
  - 0120: Governance
  - 0130: Risk assessment
  - 0140: Risk management strategy
  - 0150: Supply chain risk management

- **0200-0299**: Protect Function
  - 0200: Identity management and access control
  - 0210: Awareness and training
  - 0220: Data security
  - 0230: Information protection processes
  - 0240: Maintenance
  - 0250: Protective technology

- **0300-0399**: Detect Function
  - 0300: Anomalies and events
  - 0310: Security continuous monitoring
  - 0320: Detection processes

- **0400-0499**: Respond Function
  - 0400: Response planning
  - 0410: Communications
  - 0420: Analysis
  - 0430: Mitigation
  - 0440: Improvements

- **0500-0599**: Recover Function
  - 0500: Recovery planning
  - 0510: Improvements
  - 0520: Communications

- **0600-0699**: Implementation and Assessment
  - 0600: Implementation tiers
  - 0610: Current profile
  - 0620: Target profile
  - 0630: Gap analysis
  - 0640: Action plan

#### TOGAF Template Organization

Number ranges for TOGAF templates:

- **0010-0099**: Preliminary Phase and Foundation
  - 0010: Architecture framework setup
  - 0020: Architecture principles
  - 0030: Architecture governance framework
  - 0040: Architecture repository structure
  - 0050: Stakeholder management approach
  - 0060: Architecture tools and techniques

- **0100-0199**: Phase A - Architecture Vision
  - 0100: Architecture vision overview
  - 0110: Business goals and drivers
  - 0120: Stakeholder concerns
  - 0130: Architecture scope
  - 0140: Architecture constraints
  - 0150: Architecture vision statement

- **0200-0299**: Phase B - Business Architecture
  - 0200: Business architecture overview
  - 0210: Business capability model
  - 0220: Value streams
  - 0230: Organization structure
  - 0240: Business processes
  - 0250: Business functions

- **0300-0399**: Phase C - Information Systems Architecture
  - 0300: Data architecture
  - 0310: Data entities and relationships
  - 0320: Data lifecycle management
  - 0330: Application architecture
  - 0340: Application portfolio
  - 0350: Application interfaces

- **0400-0499**: Phase D - Technology Architecture
  - 0400: Technology architecture overview
  - 0410: Technology platforms
  - 0420: Infrastructure architecture
  - 0430: Network architecture
  - 0440: Security architecture
  - 0450: Technology standards

- **0500-0599**: Phase E - Opportunities and Solutions
  - 0500: Implementation approach
  - 0510: Architecture building blocks
  - 0520: Solution building blocks
  - 0530: Gap analysis
  - 0540: Transition architectures

- **0600-0699**: Phase F-H - Migration and Governance
  - 0600: Migration planning
  - 0610: Implementation and migration plan
  - 0620: Architecture roadmap
  - 0630: Implementation governance
  - 0640: Architecture change management
  - 0650: Architecture compliance

- **0700-0799**: Requirements Management
  - 0700: Requirements management process
  - 0710: Requirements repository
  - 0720: Requirements traceability
  - 0730: Requirements prioritization

## Data Models

### Template Metadata Model

```python
class TemplateMetadata:
    """Metadata for a template file"""
    document_id: str          # e.g., "idw-ps-951-0010"
    owner: str                # Template owner/author
    version: str              # Version number
    status: str               # Draft, Review, Approved, Published
    classification: str       # Internal, Confidential, Public
    last_update: str          # ISO date format
    framework: str            # idw-ps-951, nist-csf, togaf
    language: str             # de, en
    template_number: int      # Numeric prefix (10, 20, 30, etc.)
```

### Framework Configuration Model

```python
class FrameworkConfig:
    """Configuration for a compliance framework"""
    framework_id: str         # idw-ps-951, nist-csf, togaf
    display_name: str         # "IDW PS 951", "NIST CSF 2.0", "TOGAF"
    languages: List[str]      # ["de", "en"]
    template_count: int       # Expected number of templates
    has_diagrams: bool        # Whether framework includes diagrams
    mapping_file: str         # Path to FRAMEWORK_MAPPING.md
    readme_file: str          # Path to README.md
```

### Placeholder Model

```python
class Placeholder:
    """Represents a placeholder in a template"""
    placeholder_text: str     # Full placeholder: {{ source.field }}
    source: str               # source, meta, netbox
    field: str                # field name
    default_value: str        # Optional default value
    is_required: bool         # Whether placeholder must be filled
```

### Template Validation Result Model

```python
class ValidationResult:
    """Result of template validation"""
    is_valid: bool
    template_path: str
    errors: List[str]         # List of validation errors
    warnings: List[str]       # List of validation warnings
    placeholder_count: int    # Number of placeholders found
    missing_metadata: List[str]  # Missing metadata fields
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*


### Property 1: Template Naming Convention Compliance
*For any* template file in a framework template set, the filename must match the pattern NNNN_descriptive_name.md where NNNN is a 4-digit number.
**Validates: Requirements 4.1, 9.1**

### Property 2: Template Numbering Increments
*For any* sequence of consecutive templates in a framework, the numeric prefixes must increment by 10 (e.g., 0010, 0020, 0030).
**Validates: Requirements 4.2**

### Property 3: Template Numbering Range Coverage
*For any* framework template set, the templates must span from 0010 to at least the minimum required number (IDW PS 951: 0500, NIST CSF 2.0: 0600, TOGAF: 0700).
**Validates: Requirements 1.2, 2.2, 3.2**

### Property 4: Template Header Structure
*For any* template file, it must include a header section containing Document-ID, Owner, Version, Status, Classification, and Last Update fields.
**Validates: Requirements 4.3**

### Property 5: Markdown Structure Compliance
*For any* template file, it must contain structured sections using markdown headers (##, ###).
**Validates: Requirements 4.4**

### Property 6: Placeholder Syntax Validation
*For any* placeholder in a template, it must follow the syntax {{ source.field }} where source is one of (source, meta, netbox) and field is a valid identifier.
**Validates: Requirements 4.5, 7.1, 7.5, 9.5**

### Property 7: Bilingual Template Consistency
*For any* template in one language (German or English), there must exist a corresponding template in the other language with identical filename, section structure, and placeholder locations.
**Validates: Requirements 1.6, 5.3, 5.4, 5.5, 9.6**

### Property 8: Template Discovery
*For any* new framework directory added to templates/de/ or templates/en/, the Template_Manager must automatically discover and load it.
**Validates: Requirements 6.1**

### Property 9: Template Sorting by Numeric Prefix
*For any* set of loaded templates from a framework, the Template_Manager must sort them in ascending order by their numeric prefix.
**Validates: Requirements 6.3**

### Property 10: Metadata Extraction
*For any* metadata template file (0000_metadata_*.md), the Template_Manager must successfully extract all metadata fields (title, author, version, date, organization, classification).
**Validates: Requirements 6.4**

### Property 11: Placeholder Recognition and Processing
*For any* template containing valid placeholder syntax, the Placeholder_System must recognize and process all placeholders, substituting available data or preserving the placeholder if data is unavailable.
**Validates: Requirements 7.1, 7.2, 7.3, 7.4**

### Property 12: Placeholder Substitution Logging
*For any* placeholder substitution operation, the Placeholder_System must log the operation including the placeholder name, source, and substituted value.
**Validates: Requirements 7.6**

### Property 13: Multi-Format Output Generation
*For any* new framework template set, the Output_Generator must successfully generate output in all three formats (HTML with navigation, PDF with table of contents, and Markdown in both combined and separate file modes).
**Validates: Requirements 6.6, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6**

### Property 14: Output Directory Structure
*For any* generated handbook output, files must be placed in the directory structure test-output/{language}/{framework}/ where language is (de, en) and framework is the framework identifier.
**Validates: Requirements 8.7**

### Property 15: Template Number Uniqueness
*For any* framework template set, all template numeric prefixes must be unique within that framework.
**Validates: Requirements 9.2**

### Property 16: Framework Requirement Mapping Completeness
*For any* framework requirement or control listed in FRAMEWORK_MAPPING.md, it must be mapped to at least one specific template file.
**Validates: Requirements 10.3**

### Property 17: Code Coverage Threshold
*For any* test suite execution covering new template functionality, the code coverage must be at least 80%.
**Validates: Requirements 14.7**

## Error Handling

### Template Loading Errors

**Error Condition**: Template file not found or inaccessible
- **Detection**: File system operations during template loading
- **Handling**: Log error with file path, skip template, continue loading other templates
- **User Feedback**: Warning message listing missing templates

**Error Condition**: Invalid template filename format
- **Detection**: Filename validation during template discovery
- **Handling**: Log validation error, skip template, continue loading
- **User Feedback**: Validation report listing invalid filenames

**Error Condition**: Malformed template metadata
- **Detection**: Metadata parsing during template processing
- **Handling**: Use default metadata values, log warning, continue processing
- **User Feedback**: Warning message with template path and missing fields

### Placeholder Processing Errors

**Error Condition**: Invalid placeholder syntax
- **Detection**: Placeholder parsing using regex pattern matching
- **Handling**: Preserve original text, log warning, continue processing
- **User Feedback**: Validation report listing invalid placeholders

**Error Condition**: Placeholder data source unavailable
- **Detection**: Data source connection or query failure
- **Handling**: Preserve placeholder in output, log warning, continue processing
- **User Feedback**: Warning message listing unresolved placeholders

**Error Condition**: Circular placeholder references
- **Detection**: Placeholder resolution tracking during substitution
- **Handling**: Break circular reference, log error, use placeholder text
- **User Feedback**: Error message identifying circular reference chain

### Validation Errors

**Error Condition**: Bilingual template structure mismatch
- **Detection**: Section header comparison between language versions
- **Handling**: Log validation error, generate detailed diff report
- **User Feedback**: Validation report showing structural differences

**Error Condition**: Missing required files (metadata, README, FRAMEWORK_MAPPING)
- **Detection**: File existence checks during validation
- **Handling**: Log validation error, list missing files
- **User Feedback**: Validation report listing missing required files

**Error Condition**: Template number gaps or duplicates
- **Detection**: Numeric prefix analysis during validation
- **Handling**: Log validation error, list problematic numbers
- **User Feedback**: Validation report showing numbering issues

### Output Generation Errors

**Error Condition**: HTML generation failure
- **Detection**: HTML rendering exceptions
- **Handling**: Log error with stack trace, attempt fallback to Markdown output
- **User Feedback**: Error message with generation details

**Error Condition**: PDF generation failure
- **Detection**: PDF conversion exceptions
- **Handling**: Log error, provide HTML output as alternative
- **User Feedback**: Error message suggesting HTML alternative

**Error Condition**: Output directory creation failure
- **Detection**: File system permission errors
- **Handling**: Log error, attempt to use temporary directory
- **User Feedback**: Error message with permission details

### Framework-Specific Errors

**Error Condition**: IDW PS 951 templates missing German terminology
- **Detection**: Terminology validation in German templates
- **Handling**: Log warning, continue processing
- **User Feedback**: Warning message listing missing terminology

**Error Condition**: NIST CSF 2.0 templates missing Govern function
- **Detection**: Function coverage validation
- **Handling**: Log validation error, mark as incomplete
- **User Feedback**: Validation report showing missing function

**Error Condition**: TOGAF templates missing ADM phase coverage
- **Detection**: Phase coverage validation
- **Handling**: Log validation error, mark as incomplete
- **User Feedback**: Validation report showing missing phases

## Testing Strategy

### Dual Testing Approach

This feature requires both unit testing and property-based testing to ensure comprehensive coverage:

- **Unit tests**: Verify specific examples, edge cases, and error conditions
- **Property tests**: Verify universal properties across all inputs
- Both approaches are complementary and necessary for comprehensive validation

### Unit Testing

Unit tests will focus on:

1. **Specific Template Examples**
   - Loading specific IDW PS 951, NIST CSF 2.0, and TOGAF templates
   - Verifying specific template content and structure
   - Testing specific placeholder substitutions

2. **Edge Cases**
   - Empty template files
   - Templates with no placeholders
   - Templates with maximum number of placeholders
   - Templates with special characters in filenames
   - Bilingual templates with different content lengths

3. **Error Conditions**
   - Missing template files
   - Invalid filename formats
   - Malformed metadata
   - Invalid placeholder syntax
   - Missing required files (README, FRAMEWORK_MAPPING)

4. **Integration Points**
   - Template_Manager integration with new frameworks
   - Placeholder_System integration with new templates
   - Output_Generator integration with new frameworks
   - Validation_System integration with new templates

### Property-Based Testing

Property-based testing will use **pytest with Hypothesis** (Python's property-based testing library) to verify universal properties across randomized inputs.

**Configuration**:
- Minimum 100 iterations per property test
- Each test tagged with: **Feature: additional-compliance-frameworks, Property {number}: {property_text}**

**Property Test Coverage**:

1. **Property 1: Template Naming Convention Compliance**
   - Generate random template filenames
   - Verify all match NNNN_descriptive_name.md pattern
   - Tag: **Feature: additional-compliance-frameworks, Property 1: Template Naming Convention Compliance**

2. **Property 2: Template Numbering Increments**
   - Generate random sequences of template numbers
   - Verify consecutive numbers differ by 10
   - Tag: **Feature: additional-compliance-frameworks, Property 2: Template Numbering Increments**

3. **Property 3: Template Numbering Range Coverage**
   - Generate random template sets for each framework
   - Verify numbering ranges meet minimum requirements
   - Tag: **Feature: additional-compliance-frameworks, Property 3: Template Numbering Range Coverage**

4. **Property 4: Template Header Structure**
   - Generate random template files
   - Verify all contain required header fields
   - Tag: **Feature: additional-compliance-frameworks, Property 4: Template Header Structure**

5. **Property 5: Markdown Structure Compliance**
   - Generate random template content
   - Verify all contain markdown headers
   - Tag: **Feature: additional-compliance-frameworks, Property 5: Markdown Structure Compliance**

6. **Property 6: Placeholder Syntax Validation**
   - Generate random placeholder strings
   - Verify all valid placeholders match {{ source.field }} pattern
   - Tag: **Feature: additional-compliance-frameworks, Property 6: Placeholder Syntax Validation**

7. **Property 7: Bilingual Template Consistency**
   - Generate random bilingual template pairs
   - Verify filename, structure, and placeholder consistency
   - Tag: **Feature: additional-compliance-frameworks, Property 7: Bilingual Template Consistency**

8. **Property 8: Template Discovery**
   - Generate random framework directories
   - Verify Template_Manager discovers all
   - Tag: **Feature: additional-compliance-frameworks, Property 8: Template Discovery**

9. **Property 9: Template Sorting by Numeric Prefix**
   - Generate random unsorted template lists
   - Verify Template_Manager sorts correctly
   - Tag: **Feature: additional-compliance-frameworks, Property 9: Template Sorting by Numeric Prefix**

10. **Property 10: Metadata Extraction**
    - Generate random metadata templates
    - Verify Template_Manager extracts all fields
    - Tag: **Feature: additional-compliance-frameworks, Property 10: Metadata Extraction**

11. **Property 11: Placeholder Recognition and Processing**
    - Generate random templates with placeholders
    - Verify Placeholder_System processes all correctly
    - Tag: **Feature: additional-compliance-frameworks, Property 11: Placeholder Recognition and Processing**

12. **Property 12: Placeholder Substitution Logging**
    - Generate random placeholder substitutions
    - Verify all operations are logged
    - Tag: **Feature: additional-compliance-frameworks, Property 12: Placeholder Substitution Logging**

13. **Property 13: Multi-Format Output Generation**
    - Generate random framework template sets
    - Verify Output_Generator produces all formats
    - Tag: **Feature: additional-compliance-frameworks, Property 13: Multi-Format Output Generation**

14. **Property 14: Output Directory Structure**
    - Generate random handbook outputs
    - Verify correct directory structure
    - Tag: **Feature: additional-compliance-frameworks, Property 14: Output Directory Structure**

15. **Property 15: Template Number Uniqueness**
    - Generate random template sets
    - Verify no duplicate numbers within frameworks
    - Tag: **Feature: additional-compliance-frameworks, Property 15: Template Number Uniqueness**

16. **Property 16: Framework Requirement Mapping Completeness**
    - Generate random framework mappings
    - Verify all requirements mapped to templates
    - Tag: **Feature: additional-compliance-frameworks, Property 16: Framework Requirement Mapping Completeness**

17. **Property 17: Code Coverage Threshold**
    - Run test suite with coverage measurement
    - Verify coverage meets 80% threshold
    - Tag: **Feature: additional-compliance-frameworks, Property 17: Code Coverage Threshold**

### Test Organization

```
tests/
├── unit/
│   ├── test_idw_ps_951_templates.py
│   ├── test_nist_csf_templates.py
│   ├── test_togaf_templates.py
│   ├── test_template_structure.py
│   ├── test_bilingual_support.py
│   ├── test_template_manager_integration.py
│   ├── test_placeholder_system.py
│   ├── test_output_generator.py
│   └── test_validation_system.py
├── property/
│   ├── test_template_properties.py
│   ├── test_bilingual_properties.py
│   ├── test_manager_properties.py
│   ├── test_placeholder_properties.py
│   ├── test_output_properties.py
│   └── test_validation_properties.py
└── integration/
    ├── test_end_to_end_idw_ps_951.py
    ├── test_end_to_end_nist_csf.py
    └── test_end_to_end_togaf.py
```

### Test Data

Test data will include:

1. **Sample Templates**: Minimal valid templates for each framework
2. **Sample Metadata**: Valid metadata files for each framework and language
3. **Sample Placeholders**: Various placeholder patterns and data sources
4. **Sample Framework Mappings**: Complete mapping documents for each framework
5. **Invalid Test Cases**: Malformed templates, invalid filenames, broken placeholders

### Continuous Integration

- All tests must pass before merging
- Code coverage must meet 80% threshold
- Property tests run with 100 iterations minimum
- Integration tests run against all three frameworks
- Validation tests run against all bilingual template pairs
