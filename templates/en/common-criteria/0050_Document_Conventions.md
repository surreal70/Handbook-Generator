# Document Conventions

**Document-ID:** 0050
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines documentation conventions, terminology, notation, and formatting
standards used throughout the Security Target according to ISO/IEC 15408.

Customization required:
- Add TOE-specific terminology and definitions
- Define TOE-specific abbreviations and acronyms
- Document diagram conventions if applicable
- List informative references specific to the TOE
- Ensure consistency of terminology throughout the ST

Reference: ISO/IEC 15408-1:2022 (General conventions)
ISO/IEC 15408-2:2022 (SFR notation)
ISO/IEC 15408-3:2022 (SAR notation)
-->

## 1. Terminology and Notation

### 1.1 Common Criteria Terminology
This Security Target uses terminology from ISO/IEC 15408:2022:

| Term | Definition |
|------|------------|
| **TOE** | Target of Evaluation - the IT product or system being evaluated |
| **TSF** | TOE Security Functionality - combined functionality of all hardware, software, and firmware of the TOE that must be relied upon for the correct enforcement of the SFRs |
| **TSP** | TOE Security Policy - set of rules that regulate how assets are managed, protected, and distributed within the TOE |
| **SFR** | Security Functional Requirement - requirement for security enforcement by the TOE |
| **SAR** | Security Assurance Requirement - requirement to assure the security of the TOE |
| **PP** | Protection Profile - implementation-independent statement of security needs for a TOE type |
| **ST** | Security Target - implementation-dependent statement of security needs for a specific identified TOE |
| **EAL** | Evaluation Assurance Level - package of assurance requirements |

### 1.2 TOE-Specific Terminology
[TODO: Define TOE-specific terms]

| Term | Definition |
|------|------------|
| [TODO: Term 1] | [TODO: Definition] |
| [TODO: Term 2] | [TODO: Definition] |
| [TODO: Term 3] | [TODO: Definition] |

## 2. Notation Conventions

### 2.1 SFR Notation
Security Functional Requirements are identified using the notation from ISO/IEC 15408-2:2022:

**Format:** `CLASS.FAMILY.COMPONENT.ELEMENT`

**Example:** `FIA_UAU.1.1`
- **FIA** = Class (Identification and Authentication)
- **UAU** = Family (User Authentication)
- **1** = Component number
- **1** = Element number

### 2.2 SAR Notation
Security Assurance Requirements are identified using the notation from ISO/IEC 15408-3:2022:

**Format:** `CLASS.FAMILY.COMPONENT`

**Example:** `ADV_FSP.1`
- **ADV** = Class (Development)
- **FSP** = Family (Functional Specification)
- **1** = Component number

### 2.3 Operations on Requirements
The following operations can be performed on SFRs and SARs:

| Operation | Symbol | Description |
|-----------|--------|-------------|
| **Assignment** | [assignment:] | Specify a parameter |
| **Selection** | [selection:] | Choose from a list of options |
| **Refinement** | **bold** | Add detail or restrict |
| **Iteration** | /iteration | Apply requirement multiple times |

**Example:**
- Original: "The TSF shall authenticate [assignment: list of users]"
- Completed: "The TSF shall authenticate [assignment: administrators, operators]"

## 3. Document Structure

### 3.1 Section Organization
This ST is organized according to ISO/IEC 15408-1:2022:

1. **ST Introduction** - Identification and overview
2. **TOE Description** - Physical and logical description
3. **Security Problem Definition** - Threats, OSPs, assumptions
4. **Security Objectives** - Objectives for TOE and environment
5. **Security Requirements** - SFRs and SARs
6. **TOE Summary Specification** - Security functions
7. **Appendices** - Supporting information

### 3.2 Cross-References
Cross-references within this ST use the following format:
- Section references: "See Section X.Y"
- Table references: "See Table X"
- Figure references: "See Figure X"

## 4. Formatting Conventions

### 4.1 Text Formatting
| Format | Usage |
|--------|-------|
| **Bold** | Emphasis, refinements |
| *Italic* | Definitions, first use of terms |
| `Monospace` | Code, commands, identifiers |
| [TODO] | Placeholder requiring completion |

### 4.2 Lists and Tables
- **Bulleted lists**: Used for unordered items
- **Numbered lists**: Used for sequential steps or ordered items
- **Tables**: Used for structured data and mappings

### 4.3 Diagrams
[TODO: Describe diagram conventions if applicable]
- Architecture diagrams: [TODO]
- Data flow diagrams: [TODO]
- Sequence diagrams: [TODO]

## 5. Abbreviations and Acronyms

### 5.1 Common Criteria Abbreviations
| Abbreviation | Full Term |
|--------------|-----------|
| CC | Common Criteria |
| CEM | Common Evaluation Methodology |
| EAL | Evaluation Assurance Level |
| IT | Information Technology |
| OSP | Organizational Security Policy |
| PP | Protection Profile |
| SAR | Security Assurance Requirement |
| SFR | Security Functional Requirement |
| ST | Security Target |
| TOE | Target of Evaluation |
| TSF | TOE Security Functionality |
| TSP | TOE Security Policy |

### 5.2 TOE-Specific Abbreviations
[TODO: List TOE-specific abbreviations]

| Abbreviation | Full Term |
|--------------|-----------|
| [TODO: Abbr 1] | [TODO: Full term] |
| [TODO: Abbr 2] | [TODO: Full term] |
| [TODO: Abbr 3] | [TODO: Full term] |

## 6. References

### 6.1 Normative References
The following documents are referenced normatively in this ST:

1. ISO/IEC 15408-1:2022, Information technology — Security techniques — Evaluation criteria for IT security — Part 1: Introduction and general model
2. ISO/IEC 15408-2:2022, Information technology — Security techniques — Evaluation criteria for IT security — Part 2: Security functional components
3. ISO/IEC 15408-3:2022, Information technology — Security techniques — Evaluation criteria for IT security — Part 3: Security assurance components
4. Common Methodology for Information Technology Security Evaluation (CEM)

### 6.2 Informative References
[TODO: List informative references]

1. [TODO: Reference 1]
2. [TODO: Reference 2]
3. [TODO: Reference 3]

## 7. Document Conventions Summary

### 7.1 Key Conventions
- All SFRs are from ISO/IEC 15408-2:2022 unless marked as extended
- All SARs are from ISO/IEC 15408-3:2022 unless marked as augmented
- Operations on requirements are clearly marked
- All [TODO] placeholders must be completed before finalization

### 7.2 Consistency Rules
- Terminology must be consistent throughout the ST
- All cross-references must be valid
- All tables and figures must be numbered sequentially
- All requirements must be uniquely identified

**Next Steps:**
1. Complete all [TODO] placeholders
2. Verify consistency of terminology usage
3. Ensure all abbreviations are defined
4. Check that all references are complete

