# TOE Summary Specification

**Document-ID:** 0500
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

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific TOE (Target of Evaluation).

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
The TOE Summary Specification describes how the TOE fulfills the Security Functional Requirements (SFRs)
and which Assurance Measures are implemented.

This section is central to the Common Criteria Evaluation as it bridges the gap between abstract
requirements and concrete implementation.

IMPORTANT NOTES:
- Describe security functions at an appropriate level of abstraction
- Avoid overly detailed implementation details (these belong in the Evaluation Evidence)
- Ensure that each SFR is covered by at least one security function
- Document the mapping between security functions and SFRs
- Describe the Strength of Function (SOF) of security functions
-->

## 1. Introduction

### 1.1 Purpose

This document describes the TOE Summary Specification (TSS) for **[TODO: TOE Name]**. The TSS shows how the TOE fulfills the Security Functional Requirements (SFRs) and Security Assurance Requirements (SARs) defined in Chapter 4 (Security Requirements).

<!-- 
GUIDANCE:
- Explain the purpose of the TSS in the context of the Security Target
- Reference the relevant chapters of the Security Target
- Describe the structure of this chapter
-->

### 1.2 Structure of the TSS

The TOE Summary Specification is structured as follows:

- **Chapter 2**: Overview of TOE Security Functions (TSFs)
- **Chapter 3**: Detailed description of security functions
- **Chapter 4**: Mapping of security functions to SFRs (Coverage Matrix)
- **Chapter 5**: Assurance Measures
- **Chapter 6**: Strength of Function (SOF)

## 2. Overview of TOE Security Functions

### 2.1 Security Functions - Overview

The TOE implements the following security functions (TSFs):

| TSF-ID | Security Function | Description | Associated SFRs |
|--------|-------------------|-------------|-----------------|
| TSF-1 | [TODO: Name] | [TODO: Brief description] | [TODO: SFR-IDs] |
| TSF-2 | [TODO: Name] | [TODO: Brief description] | [TODO: SFR-IDs] |
| TSF-3 | [TODO: Name] | [TODO: Brief description] | [TODO: SFR-IDs] |

<!-- 
GUIDANCE:
- List all security functions of the TOE
- Assign unique TSF-IDs (TSF-1, TSF-2, etc.)
- Provide a concise description of each function
- Reference the associated SFRs
- Typical TSFs: Identification & Authentication, Access Control, Audit, Cryptography, etc.
-->

### 2.2 Architecture of Security Functions

```
[TODO: Insert diagram - Architecture of TSFs]

Example:
┌─────────────────────────────────────────────────┐
│           TOE Security Functions                │
├─────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐            │
│  │ TSF-1: I&A   │  │ TSF-2: Access│            │
│  │              │  │ Control      │            │
│  └──────────────┘  └──────────────┘            │
│  ┌──────────────┐  ┌──────────────┐            │
│  │ TSF-3: Audit │  │ TSF-4: Crypto│            │
│  │              │  │              │            │
│  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────┘
```

<!-- 
GUIDANCE:
- Create an architecture diagram of the security functions
- Show the relationships between the TSFs
- Illustrate the layers and dependencies
- Save the diagram in diagrams/toe_tsf_architecture.png
-->

**Description:**

[TODO: Describe the architecture of the security functions. Explain how the various TSFs work together and what dependencies exist.]

## 3. Detailed Description of Security Functions

<!-- 
GUIDANCE:
For each security function (TSF):
1. Describe the functionality at an appropriate level of abstraction
2. Explain how the function fulfills the associated SFRs
3. Describe the interfaces to other TSFs
4. Document relevant parameters and configurations
5. Avoid overly detailed implementation details

IMPORTANT: This section is the core of the TSS!
-->

### 3.1 TSF-1: [TODO: Name of Security Function]

**TSF-ID:** TSF-1  
**Associated SFRs:** [TODO: e.g., FIA_UID.1, FIA_UAU.1]

#### 3.1.1 Function Description

[TODO: Describe the security function in detail. Explain:
- What the function does
- How it works (at an appropriate level of abstraction)
- What inputs it processes
- What outputs it produces
- What security properties it ensures]

**Example:**
The Identification and Authentication function (TSF-1) ensures that all users are identified and authenticated before accessing TOE functions. The function uses a username for identification and a password for authentication. Passwords are stored hashed with SHA-256 and salted.

#### 3.1.2 Fulfillment of SFRs

[TODO: For each associated SFR, explain how this security function fulfills the requirement.]

**SFR [TODO: ID]:**
- [TODO: Description of how the SFR is fulfilled]

**SFR [TODO: ID]:**
- [TODO: Description of how the SFR is fulfilled]

#### 3.1.3 Interfaces

[TODO: Describe the interfaces of this TSF to other TSFs or external components.]

- **Interface to TSF-X:** [TODO: Description]
- **External Interfaces:** [TODO: Description]

### 3.2 TSF-2: [TODO: Name of Security Function]

**TSF-ID:** TSF-2  
**Associated SFRs:** [TODO: SFR-IDs]

#### 3.2.1 Function Description

[TODO: Description analogous to 3.1.1]

#### 3.2.2 Fulfillment of SFRs

[TODO: Description analogous to 3.1.2]

#### 3.2.3 Interfaces

[TODO: Description analogous to 3.1.3]

### 3.3 TSF-3: [TODO: Name of Security Function]

[TODO: Describe additional security functions following the same schema]

## 4. Mapping of Security Functions to SFRs

### 4.1 Coverage Matrix

The following table shows the mapping between security functions (TSFs) and Security Functional Requirements (SFRs):

| SFR-ID | SFR-Name | TSF-1 | TSF-2 | TSF-3 | TSF-4 | TSF-5 |
|--------|----------|-------|-------|-------|-------|-------|
| [TODO] | [TODO]   | X     |       |       |       |       |
| [TODO] | [TODO]   | X     | X     |       |       |       |
| [TODO] | [TODO]   |       | X     |       |       |       |
| [TODO] | [TODO]   |       |       | X     |       |       |

<!-- 
GUIDANCE:
- List all SFRs from Chapter 4
- Mark with "X" which TSF fulfills which SFR
- Ensure that each SFR is assigned to at least one TSF
- An SFR can be fulfilled by multiple TSFs
- Reference the separate document 0530_Functions_Rationale.md for the rationale
-->

### 4.2 Completeness Check

**Coverage of SFRs:**
- Number of SFRs: [TODO: Number]
- Number of covered SFRs: [TODO: Number]
- Coverage rate: [TODO: Percentage]

**Uncovered SFRs:**
[TODO: List all SFRs that are not covered by TSFs. If all are covered, write "None".]

<!-- 
GUIDANCE:
- Check if all SFRs are covered by at least one TSF
- Document any gaps
- Justify why certain SFRs may not be covered by TSFs
-->

## 5. Assurance Measures

### 5.1 Overview

The following Assurance Measures are implemented to fulfill the Security Assurance Requirements (SARs):

| SAR-ID | SAR-Name | Assurance Measure | Description |
|--------|----------|-------------------|-------------|
| [TODO] | [TODO]   | [TODO]            | [TODO]      |
| [TODO] | [TODO]   | [TODO]            | [TODO]      |

<!-- 
GUIDANCE:
- List all SARs from Chapter 4
- Describe the corresponding Assurance Measure for each SAR
- Typical Assurance Measures: Documentation, Tests, Reviews, Analyses, etc.
- Reference the separate document 0510_Assurance_Measures.md for details
-->

### 5.2 Mapping to Evaluation Assurance Level

The TOE is evaluated at **[TODO: EAL level, e.g., EAL4]**. The following Assurance Measures support this EAL:

[TODO: List the Assurance Measures required for the chosen EAL.]

**Example for EAL4:**
- Configuration Management (ACM_CAP.4, ACM_SCP.2)
- Delivery and Operation (ADO_DEL.2, ADO_IGS.1)
- Development (ADV_FSP.2, ADV_IMP.1, ADV_TDS.2)
- Guidance Documents (AGD_ADM.1, AGD_USR.1)
- Life Cycle Support (ALC_DVS.1, ALC_LCD.1, ALC_TAT.1)
- Tests (ATE_COV.2, ATE_DPT.1, ATE_FUN.1, ATE_IND.2)
- Vulnerability Assessment (AVA_MSU.2, AVA_SOF.1, AVA_VLA.2)

## 6. Strength of Function (SOF)

### 6.1 SOF-Claim

The TOE claims the following Strength of Function:

**SOF-Claim:** [TODO: SOF-basic / SOF-medium / SOF-high]

<!-- 
GUIDANCE:
- SOF-basic: Protection against attackers with limited resources
- SOF-medium: Protection against attackers with moderate resources
- SOF-high: Protection against attackers with high resources
- Choose the SOF level based on the threat analysis
-->

### 6.2 SOF-Analysis

The following table shows the strength of individual probabilistic or permutation-based security mechanisms:

| TSF-ID | Mechanism | SOF-Level | Rationale |
|--------|-----------|-----------|-----------|
| [TODO] | [TODO]    | [TODO]    | [TODO]    |
| [TODO] | [TODO]    | [TODO]    | [TODO]    |

<!-- 
GUIDANCE:
- Identify all probabilistic or permutation-based mechanisms
- Typical examples: Password authentication, random number generators, cryptographic keys
- Analyze the strength of each mechanism
- Justify the SOF level (e.g., key length, entropy, attack resistance)
- Reference the separate document 0540_Strength_of_Function.md for details
-->

### 6.3 Fulfillment of SOF-Claim

[TODO: Explain how the analyzed mechanisms fulfill the SOF-Claim. Show that all relevant mechanisms achieve at least the claimed SOF level.]

**Summary:**
- Number of analyzed mechanisms: [TODO]
- Lowest SOF level: [TODO]
- Fulfillment of SOF-Claim: [TODO: Yes/No]

## 7. Summary

### 7.1 Completeness of TSS

The TOE Summary Specification is complete and covers all aspects:

- ✓ All SFRs are covered by TSFs
- ✓ All SARs are covered by Assurance Measures
- ✓ SOF-Claim is analyzed and justified
- ✓ All security functions are described in detail

### 7.2 Reference to Additional Documents

For detailed information see:

- **0510_Assurance_Measures.md**: Detailed description of assurance measures
- **0520_Functions_Rationale.md**: Rationale for mapping TSFs to SFRs
- **0530_Coverage_Matrix.md**: Complete Coverage Matrix
- **0540_Strength_of_Function.md**: Detailed SOF analysis

