# Common Criteria Security Target Templates (ISO/IEC 15408)

This directory contains templates for creating a Security Target (ST) according to ISO/IEC 15408 (Common Criteria for Information Technology Security Evaluation).

## Overview

The Common Criteria (CC) is an international standard for evaluating the security of IT products and systems. A Security Target documents the security properties of a Target of Evaluation (TOE) and serves as the basis for certification.

## Template Structure

The templates are organized according to the structure of ISO/IEC 15408-1:2022:

### Foundation (0010-0050)
- **0010**: ST Introduction - Introduction and ST identification
- **0020**: TOE Overview - Overview of the evaluation object
- **0030**: TOE Description Summary - Summary of TOE description
- **0040**: Conformance Claims - Conformance claims (PP, Package, CC Version)
- **0050**: Document Conventions - Documentation conventions and terminology

### TOE Description (0100-0150)
- **0100**: TOE Physical Scope - Physical scope (hardware, software, firmware)
- **0110**: TOE Logical Scope - Logical scope (security functions)
- **0120**: TOE Interfaces - TOE interfaces
- **0130**: TOE Architecture - Architecture and components
- **0140**: TOE Lifecycle - Lifecycle (development, operation, maintenance)

### Security Problem Definition (0200-0250)
- **0200**: Threats - Threats to the TOE
- **0210**: Organizational Security Policies - Organizational security policies
- **0220**: Assumptions - Assumptions about the operational environment
- **0230**: Threat Agents - Attackers and their capabilities
- **0240**: Assets - Assets to be protected

### Security Objectives (0300-0350)
- **0300**: Security Objectives for TOE - Security objectives for the TOE
- **0310**: Security Objectives for Environment - Security objectives for the environment
- **0320**: Security Objectives Rationale - Rationale for security objectives
- **0330**: Objectives Coverage Matrix - Coverage matrix objectives/threats

### Security Requirements (0400-0450)
- **0400**: Security Functional Requirements (SFR) - Functional security requirements
- **0410**: Security Assurance Requirements (SAR) - Assurance requirements
- **0420**: Evaluation Assurance Level (EAL) - Evaluation assurance level
- **0430**: Security Requirements Rationale - Rationale for requirements
- **0440**: SFR Dependencies - Dependencies between SFRs
- **0450**: Requirements Coverage Matrix - Coverage matrix requirements/objectives

### TOE Summary Specification (0500-0550)
- **0500**: Security Functions - Security functions of the TOE
- **0510**: Assurance Measures - Assurance measures
- **0520**: Security Functions Rationale - Rationale for security functions
- **0530**: Functions Coverage Matrix - Coverage matrix functions/SFRs
- **0540**: Strength of Function Claims - Strength of function claims

### Appendices (0600-0650)
- **0600**: Protection Profile Conformance - PP conformance
- **0610**: Rationale for Security Objectives - Detailed rationale
- **0620**: Rationale for Security Requirements - Detailed rationale
- **0630**: Glossary and Acronyms - Glossary and acronyms
- **0640**: References - References and standards
- **0650**: Evidence and Documentation - Evidence and documentation

## Numbering Scheme

- Templates use 4-digit numbers with 10-step increments (0010, 0020, 0030, ...)
- This allows for future insertions between existing templates
- Number ranges group related topics

## Usage

1. **Preparation**: Determine the Evaluation Assurance Level (EAL1-EAL7)
2. **TOE Definition**: Clearly define the scope of the TOE
3. **PP Selection**: Select an appropriate Protection Profile (optional)
4. **Customization**: Adapt the templates to your specific product
5. **Placeholders**: Replace all `[TODO]` markers
6. **Consistency**: Ensure consistency across all sections
7. **Rationale**: Document all rationales completely

## Placeholders

Templates support two types of placeholders:

- **Manual Placeholders**: `[TODO: Description]` - must be replaced manually
- **Automatic Placeholders**: `[TODO]` - populated from data sources

Examples of automatic placeholders:
- `{{ meta-organisation.name }}` - Organization name
- `{{ meta-handbook.author }}` - Author
- `{{ meta-handbook.revision }}` - Version number
- `{{ meta-handbook.modifydate }}` - Date

## Common Criteria Versions

These templates are based on:
- ISO/IEC 15408-1:2022 (Part 1: Introduction and general model)
- ISO/IEC 15408-2:2022 (Part 2: Security functional components)
- ISO/IEC 15408-3:2022 (Part 3: Security assurance components)

## Evaluation Assurance Levels (EAL)

- **EAL1**: Functionally tested
- **EAL2**: Structurally tested
- **EAL3**: Methodically tested and checked
- **EAL4**: Methodically designed, tested, and reviewed
- **EAL5**: Semiformally designed and tested
- **EAL6**: Semiformally verified design and tested
- **EAL7**: Formally verified design and tested

## Important Notes

- The ST must be complete and consistent
- All SFRs must be derived from ISO/IEC 15408-2
- All SARs must be derived from ISO/IEC 15408-3
- The rationale must demonstrate all relationships
- Dependencies between SFRs must be satisfied
- The ST must be evaluated by an accredited laboratory

## Framework Mapping

See `FRAMEWORK_MAPPING.md` for a detailed mapping of templates to ISO/IEC 15408 components.

## Additional Resources

- Common Criteria Portal: https://www.commoncriteriaportal.org/
- ISO/IEC 15408 Standard
- Protection Profiles Repository
- Certified Products List
- Evaluation Schemes (e.g., BSI, ANSSI, NIAP)

## Support

For questions about using these templates or Common Criteria evaluation, contact:
- Your internal security team
- Accredited evaluation laboratories
- National certification bodies (e.g., BSI in Germany)
