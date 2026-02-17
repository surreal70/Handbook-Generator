# Security Requirements

**Document-ID:** 0400
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific Target of Evaluation (TOE).

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
This template defines the Security Requirements for the TOE according to ISO/IEC 15408-2 (SFRs) 
and ISO/IEC 15408-3 (SARs). Security Requirements must be derived from and traceable to the 
Security Objectives defined in section 0300.

Key considerations:
- SFRs define WHAT security functionality the TOE must provide
- SARs define HOW the TOE will be evaluated for correctness
- All requirements must be unambiguous, testable, and verifiable
- Operations on SFRs (assignment, selection, refinement, iteration) must be clearly marked
- Dependencies between SFRs must be identified and satisfied
- The chosen EAL determines the minimum set of SARs required
-->

## 1. Introduction

This chapter specifies the security requirements for the TOE according to ISO/IEC 15408 (Common Criteria). The security requirements are divided into:

- **Security Functional Requirements (SFRs)**: Functional security requirements that the TOE must fulfill
- **Security Assurance Requirements (SARs)**: Assurance requirements for the evaluation of the TOE

All security requirements are derived from the security objectives defined in Chapter 0300 and address the threats, organizational security policies, and assumptions identified in Chapter 0200.

## 2. Security Functional Requirements (SFRs)

### 2.1 Overview of SFRs

The following Security Functional Requirements from ISO/IEC 15408-2 have been selected for the TOE:

<!-- TODO: List all selected SFRs with class, family, and component -->

| SFR-ID | Class | Family | Component | Description |
|--------|-------|--------|-----------|-------------|
| [TODO] | [TODO: e.g., FAU] | [TODO: e.g., FAU_GEN] | [TODO: e.g., FAU_GEN.1] | [TODO: Brief description] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 2.2 Security Audit (FAU)

<!-- TODO: Add relevant FAU requirements if applicable -->

#### FAU_GEN.1 Audit data generation

**Hierarchical to:** None  
**Dependencies:** FPT_STM.1 Reliable time stamps

**FAU_GEN.1.1** The TSF shall be able to generate an audit record of the following auditable events:
- [assignment: list of auditable events]
- [TODO: Specify concrete events]

**FAU_GEN.1.2** The TSF shall record within each audit record at least the following information:
- Date and time of the event
- Type of event
- Subject identity
- Outcome (success or failure) of the event
- [assignment: other audit relevant information]

### 2.3 Cryptographic Support (FCS)

<!-- TODO: Add relevant FCS requirements if applicable -->

#### FCS_COP.1 Cryptographic operation

**Hierarchical to:** None  
**Dependencies:** 
- FDP_ITC.1 Import of user data without security attributes or FDP_ITC.2 Import of user data with security attributes or FCS_CKM.1 Cryptographic key generation

**FCS_COP.1.1** The TSF shall perform [assignment: cryptographic operation] in accordance with a specified cryptographic algorithm [assignment: cryptographic algorithm] and cryptographic key sizes [assignment: key sizes] that meet the following: [selection: standards, rules, guidelines].

[TODO: Specify concrete cryptographic operations, algorithms, and key sizes]

### 2.4 User Data Protection (FDP)

<!-- TODO: Add relevant FDP requirements -->

#### FDP_ACC.1 Subset access control

**Hierarchical to:** None  
**Dependencies:** FDP_ACF.1 Security attribute based access control

**FDP_ACC.1.1** The TSF shall enforce the [assignment: access control policy] on [assignment: subjects, objects, and operations].

[TODO: Define access control policy, subjects, objects, and operations]

### 2.5 Identification and Authentication (FIA)

<!-- TODO: Add relevant FIA requirements -->

#### FIA_UID.1 Timing of identification

**Hierarchical to:** None  
**Dependencies:** None

**FIA_UID.1.1** The TSF shall allow [selection: no other actions, [assignment: list of TSF-mediated actions]] on behalf of the user to be performed before the user is identified.

[TODO: Specify exceptions if any]

### 2.6 Security Management (FMT)

<!-- TODO: Add relevant FMT requirements -->

#### FMT_SMF.1 Specification of Management Functions

**Hierarchical to:** None  
**Dependencies:** None

**FMT_SMF.1.1** The TSF shall be capable of performing the following management functions:
- [assignment: list of security management functions]

[TODO: List all security management functions]

### 2.7 Protection of the TSF (FPT)

<!-- TODO: Add relevant FPT requirements -->

#### FPT_STM.1 Reliable time stamps

**Hierarchical to:** None  
**Dependencies:** None

**FPT_STM.1.1** The TSF shall be able to provide reliable time stamps for its own use.

### 2.8 TOE Access (FTA)

<!-- TODO: Add relevant FTA requirements if applicable -->

### 2.9 Trusted Path/Channels (FTP)

<!-- TODO: Add relevant FTP requirements if applicable -->

### 2.10 Additional SFR Classes

<!-- TODO: Add other relevant SFR classes (FCO, FRU, etc.) -->

## 3. Security Assurance Requirements (SARs)

### 3.1 Overview of SARs

The Security Assurance Requirements define the assurance requirements for the evaluation of the TOE. The SARs are determined by the selection of the Evaluation Assurance Level (EAL).

**Selected EAL:** [TODO: e.g., EAL4]

### 3.2 Assurance Class: Security Target Evaluation (ASE)

The following ASE components are required for all EALs:

- **ASE_CCL.1** Conformance claims
- **ASE_ECD.1** Extended components definition
- **ASE_INT.1** ST introduction
- **ASE_OBJ.2** Security objectives
- **ASE_REQ.2** Derived security requirements
- **ASE_SPD.1** Security problem definition
- **ASE_TSS.1** TOE summary specification

[TODO: Adapt to selected EAL]

### 3.3 Assurance Class: Development (ADV)

<!-- TODO: Add ADV components according to selected EAL -->

For EAL [TODO: X], the following ADV components are required:

- **ADV_ARC.1** Security architecture description
- **ADV_FSP.4** Complete functional specification
- **ADV_IMP.1** Implementation representation of the TSF
- **ADV_TDS.3** Basic modular design

[TODO: Adapt to selected EAL]

### 3.4 Assurance Class: Guidance Documents (AGD)

<!-- TODO: Add AGD components -->

- **AGD_OPE.1** Operational user guidance
- **AGD_PRE.1** Preparative procedures

### 3.5 Assurance Class: Life-cycle Support (ALC)

<!-- TODO: Add ALC components according to selected EAL -->

For EAL [TODO: X], the following ALC components are required:

- **ALC_CMC.4** Production support, acceptance procedures and automation
- **ALC_CMS.4** Problem tracking CM coverage
- **ALC_DEL.1** Delivery procedures
- **ALC_DVS.1** Identification of security measures
- **ALC_LCD.1** Developer defined life-cycle model
- **ALC_TAT.1** Well-defined development tools

[TODO: Adapt to selected EAL]

### 3.6 Assurance Class: Tests (ATE)

<!-- TODO: Add ATE components according to selected EAL -->

- **ATE_COV.2** Analysis of coverage
- **ATE_DPT.1** Testing: high-level design
- **ATE_FUN.1** Functional testing
- **ATE_IND.2** Independent testing - sample

[TODO: Adapt to selected EAL]

### 3.7 Assurance Class: Vulnerability Assessment (AVA)

<!-- TODO: Add AVA components according to selected EAL -->

- **AVA_VAN.3** Focused vulnerability analysis

[TODO: Adapt to selected EAL]

## 4. Security Requirements Rationale

The rationale for the selection of security requirements is detailed in document 0420.

Summary:
- All SFRs are derived from the security objectives for the TOE
- All SFR dependencies are satisfied (see document 0430)
- The selected SARs correspond to Evaluation Assurance Level [TODO: X]
- The security requirements are complete, consistent, and internally non-contradictory

## 5. Operations on SFRs

According to ISO/IEC 15408-2, the following operations can be performed on SFRs:

- **Assignment**: Specification of parameters (marked with [assignment: ...])
- **Selection**: Selection from predefined options (marked with [selection: ...])
- **Refinement**: Refinement of the requirement (displayed in italics)
- **Iteration**: Multiple use of a component (indicated by suffix, e.g., FDP_ACC.1/1, FDP_ACC.1/2)

All operations performed are documented in the SFR specifications above.

## 6. References

- ISO/IEC 15408-2:2022 - Security functional requirements
- ISO/IEC 15408-3:2022 - Security assurance requirements
- [TODO: Other relevant standards and specifications]

## 7. Appendices

### 7.1 SFR Overview Table

A complete overview of all SFRs with dependencies can be found in document 0430.

### 7.2 SAR Overview Table

A complete overview of all SARs according to the selected EAL can be found in document 0410.

**Next Steps:**
1. Complete all [TODO] placeholders
2. Specify all assignments and selections in the SFRs
3. Verify completeness of SFR dependencies (see document 0430)
4. Ensure all SFRs are derived from security objectives
5. Document the rationale in document 0420

