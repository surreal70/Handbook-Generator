# Common Criteria Framework Mapping

**Document-ID:** [FRAMEWORK]-9999
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

## Overview

This document maps the Common Criteria Security Target templates to the ISO/IEC 15408 standard components and Evaluation Assurance Levels (EAL). It provides traceability between template files and specific Common Criteria requirements, ensuring comprehensive coverage of the Security Target structure.

## ISO/IEC 15408 Standard Structure

The Common Criteria standard consists of three parts:

- **ISO/IEC 15408-1**: Introduction and general model
- **ISO/IEC 15408-2**: Security functional components (SFRs)
- **ISO/IEC 15408-3**: Security assurance components (SARs)

## Template Mapping to ISO/IEC 15408-1 (Security Target Structure)

### Part 1: ST Introduction (ISO/IEC 15408-1, Section 8.1)

| Template | ISO/IEC 15408-1 Reference | Description |
|----------|---------------------------|-------------|
| 0010_ST_Introduction.md | Section 8.1.1 | ST identification, ST overview, ST conventions |
| 0020_TOE_Overview.md | Section 8.1.2 | TOE overview and general description |
| 0030_TOE_Description_Summary.md | Section 8.1.2 | Summary of TOE description |
| 0040_Conformance_Claims.md | Section 8.1.3 | CC conformance claim, PP conformance claim, Package conformance claim |
| 0050_Document_Conventions.md | Section 8.1.4 | Notation, terminology, and conventions |

### Part 2: TOE Description (ISO/IEC 15408-1, Section 8.2)

| Template | ISO/IEC 15408-1 Reference | Description |
|----------|---------------------------|-------------|
| 0100_TOE_Physical_Scope.md | Section 8.2.1 | Physical scope of the TOE (hardware, software, firmware, guidance) |
| 0110_TOE_Logical_Scope.md | Section 8.2.2 | Logical scope of the TOE (security features and functions) |
| 0120_TOE_Interfaces.md | Section 8.2.3 | TOE interfaces (user, administrator, external systems) |
| 0130_TOE_Architecture.md | Section 8.2.4 | TOE architecture and subsystems |
| 0140_TOE_Lifecycle.md | Section 8.2.5 | TOE lifecycle (development, deployment, operation, maintenance) |

### Part 3: Security Problem Definition (ISO/IEC 15408-1, Section 8.3)

| Template | ISO/IEC 15408-1 Reference | Description |
|----------|---------------------------|-------------|
| 0200_Security_Problem_Definition.md | Section 8.3 | Overview of security problem definition |
| 0210_Threats.md | Section 8.3.1 | Threats to the TOE and assets |
| 0220_Organizational_Security_Policies.md | Section 8.3.2 | Organizational security policies (OSPs) |
| 0230_Assumptions.md | Section 8.3.3 | Assumptions about the operational environment |
| 0240_Threat_Agents_and_Assets.md | Section 8.3.1 | Threat agents (attackers) and assets to be protected |

### Part 4: Security Objectives (ISO/IEC 15408-1, Section 8.4)

| Template | ISO/IEC 15408-1 Reference | Description |
|----------|---------------------------|-------------|
| 0300_Security_Objectives.md | Section 8.4 | Overview of security objectives |
| 0310_Security_Objectives_Rationale.md | Section 8.4.1, 8.4.2 | Security objectives for the TOE and operational environment |
| 0320_Security_Objectives_Coverage_Matrix.md | Section 8.4.3 | Security objectives rationale and coverage matrix |
| 0330_Security_Objectives_Summary.md | Section 8.4 | Summary of security objectives |

### Part 5: Security Requirements (ISO/IEC 15408-1, Section 8.5)

| Template | ISO/IEC 15408-1 Reference | Description |
|----------|---------------------------|-------------|
| 0400_Security_Requirements.md | Section 8.5 | Overview of security requirements |
| 0410_Evaluation_Assurance_Level.md | Section 8.5.2 | Security Assurance Requirements (SARs) and EAL selection |
| 0420_Requirements_Rationale.md | Section 8.5.3 | Security requirements rationale |
| 0430_SFR_Dependencies.md | Section 8.5.3 | SFR dependencies and satisfaction |
| 0440_Coverage_Matrix.md | Section 8.5.3 | Requirements coverage matrix (SFRs/objectives) |

### Part 6: TOE Summary Specification (ISO/IEC 15408-1, Section 8.6)

| Template | ISO/IEC 15408-1 Reference | Description |
|----------|---------------------------|-------------|
| 0500_TOE_Summary_Specification.md | Section 8.6 | Overview of TOE summary specification |
| 0510_Assurance_Measures.md | Section 8.6.2 | Assurance measures |
| 0520_Functions_Rationale.md | Section 8.6.3 | TOE security functions rationale |
| 0530_Coverage_Matrix.md | Section 8.6.3 | Functions coverage matrix (TSFs/SFRs) |
| 0540_Strength_of_Function.md | Section 8.6.1 | Strength of function claims |

### Part 7: Appendices and Supporting Documentation

| Template | ISO/IEC 15408-1 Reference | Description |
|----------|---------------------------|-------------|
| 0600_PP_Conformance.md | Section 8.1.3 | Protection Profile conformance demonstration |
| 0610_Rationale_for_Objectives.md | Section 8.4.3 | Detailed rationale for security objectives |
| 0620_Rationale_for_Requirements.md | Section 8.5.3 | Detailed rationale for security requirements |
| 0630_Glossary.md | Section 8.1.4 | Glossary of terms and acronyms |
| 0640_References.md | N/A | References to standards, specifications, and documentation |
| 0650_Evidence_and_Documentation.md | N/A | Supporting evidence and evaluation documentation |

## Security Functional Requirements (ISO/IEC 15408-2)

The Security Functional Requirements (SFRs) are defined in ISO/IEC 15408-2 and organized into 11 functional classes. Templates 0400-0440 should reference appropriate SFRs from these classes:

### SFR Classes

| Class | Name | Description | Template Reference |
|-------|------|-------------|-------------------|
| FAU | Security audit | Audit data generation, analysis, review, storage | 0400, 0430, 0440 |
| FCO | Communication | Non-repudiation of origin and receipt | 0400, 0430, 0440 |
| FCS | Cryptographic support | Cryptographic key management and operations | 0400, 0430, 0440 |
| FDP | User data protection | Access control, data authentication, residual information protection | 0400, 0430, 0440 |
| FIA | Identification and authentication | User authentication, authentication failures | 0400, 0430, 0440 |
| FMT | Security management | Management of security attributes, functions, and data | 0400, 0430, 0440 |
| FPR | Privacy | Anonymity, pseudonymity, unlinkability, unobservability | 0400, 0430, 0440 |
| FPT | Protection of the TSF | TSF physical protection, self-test, trusted recovery | 0400, 0430, 0440 |
| FRU | Resource utilization | Fault tolerance, priority of service, resource allocation | 0400, 0430, 0440 |
| FTA | TOE access | Session locking, TOE access history, access banners | 0400, 0430, 0440 |
| FTP | Trusted path/channels | Trusted path, trusted channels | 0400, 0430, 0440 |

## Security Assurance Requirements (ISO/IEC 15408-3)

The Security Assurance Requirements (SARs) are defined in ISO/IEC 15408-3 and organized into 10 assurance classes. Templates 0410 and 0510 should reference appropriate SARs based on the selected EAL:

### SAR Classes

| Class | Name | Description | Template Reference |
|-------|------|-------------|-------------------|
| ADV | Development | Security architecture, functional specification, implementation representation | 0410, 0510 |
| AGD | Guidance documents | Operational user guidance, preparative procedures | 0410, 0510 |
| ALC | Life-cycle support | CM capabilities, delivery, development security, flaw remediation | 0410, 0510 |
| ATE | Tests | Coverage, depth, functional tests, independent testing | 0410, 0510 |
| AVA | Vulnerability assessment | Vulnerability analysis, covert channel analysis, misuse analysis | 0410, 0510 |
| ACO | Composition | Composition rationale (for composed evaluations) | 0410, 0510 |
| ASE | Security Target evaluation | ST introduction, conformance claims, security problem definition | 0410, 0510 |

## Evaluation Assurance Levels (EAL)

The templates support all seven Evaluation Assurance Levels. Template 0410 should specify the selected EAL and corresponding SARs:

### EAL1: Functionally Tested

| SAR Component | Description | Template Reference |
|---------------|-------------|-------------------|
| ADV_FSP.1 | Basic functional specification | 0410, 0510 |
| AGD_OPE.1 | Operational user guidance | 0410, 0510 |
| AGD_PRE.1 | Preparative procedures | 0410, 0510 |
| ALC_CMC.1 | Labelling of the TOE | 0410, 0510 |
| ALC_CMS.1 | TOE CM coverage | 0410, 0510 |
| ATE_IND.1 | Independent testing - conformance | 0410, 0510 |
| AVA_VAN.1 | Vulnerability survey | 0410, 0510 |

### EAL2: Structurally Tested

EAL2 includes all EAL1 components plus:

| SAR Component | Description | Template Reference |
|---------------|-------------|-------------------|
| ADV_ARC.1 | Security architecture description | 0410, 0510 |
| ADV_FSP.2 | Security-enforcing functional specification | 0410, 0510 |
| AGD_OPE.1 | Operational user guidance | 0410, 0510 |
| AGD_PRE.1 | Preparative procedures | 0410, 0510 |
| ALC_CMC.2 | Use of a CM system | 0410, 0510 |
| ALC_CMS.2 | Parts of the TOE CM coverage | 0410, 0510 |
| ALC_DEL.1 | Delivery procedures | 0410, 0510 |
| ATE_COV.1 | Evidence of coverage | 0410, 0510 |
| ATE_FUN.1 | Functional testing | 0410, 0510 |
| ATE_IND.2 | Independent testing - sample | 0410, 0510 |
| AVA_VAN.2 | Vulnerability analysis | 0410, 0510 |

### EAL3: Methodically Tested and Checked

EAL3 includes all EAL2 components plus:

| SAR Component | Description | Template Reference |
|---------------|-------------|-------------------|
| ADV_FSP.3 | Functional specification with complete summary | 0410, 0510 |
| ADV_TDS.1 | Basic design | 0410, 0510 |
| ALC_CMC.3 | Authorization controls | 0410, 0510 |
| ALC_CMS.3 | Implementation representation CM coverage | 0410, 0510 |
| ALC_DEL.1 | Delivery procedures | 0410, 0510 |
| ALC_DVS.1 | Identification of security measures | 0410, 0510 |
| ALC_LCD.1 | Developer defined life-cycle model | 0410, 0510 |
| ATE_DPT.1 | Testing: basic design | 0410, 0510 |
| ATE_FUN.1 | Functional testing | 0410, 0510 |
| ATE_IND.2 | Independent testing - sample | 0410, 0510 |
| AVA_VAN.2 | Vulnerability analysis | 0410, 0510 |

### EAL4: Methodically Designed, Tested, and Reviewed

EAL4 includes all EAL3 components plus:

| SAR Component | Description | Template Reference |
|---------------|-------------|-------------------|
| ADV_ARC.1 | Security architecture description | 0410, 0510 |
| ADV_FSP.4 | Complete functional specification | 0410, 0510 |
| ADV_IMP.1 | Implementation representation of the TSF | 0410, 0510 |
| ADV_TDS.2 | Architectural design | 0410, 0510 |
| ALC_CMC.4 | Production support, acceptance procedures and automation | 0410, 0510 |
| ALC_CMS.4 | Problem tracking CM coverage | 0410, 0510 |
| ALC_TAT.1 | Well-defined development tools | 0410, 0510 |
| ATE_COV.2 | Analysis of coverage | 0410, 0510 |
| ATE_DPT.1 | Testing: basic design | 0410, 0510 |
| ATE_FUN.1 | Functional testing | 0410, 0510 |
| ATE_IND.2 | Independent testing - sample | 0410, 0510 |
| AVA_VAN.3 | Focused vulnerability analysis | 0410, 0510 |

### EAL5: Semiformally Designed and Tested

EAL5 includes all EAL4 components plus:

| SAR Component | Description | Template Reference |
|---------------|-------------|-------------------|
| ADV_ARC.1 | Security architecture description | 0410, 0510 |
| ADV_FSP.5 | Complete semi-formal functional specification | 0410, 0510 |
| ADV_IMP.1 | Implementation representation of the TSF | 0410, 0510 |
| ADV_INT.2 | Well-structured internals | 0410, 0510 |
| ADV_TDS.3 | Basic modular design | 0410, 0510 |
| ALC_DVS.1 | Identification of security measures | 0410, 0510 |
| ATE_COV.2 | Analysis of coverage | 0410, 0510 |
| ATE_DPT.2 | Testing: security enforcing modules | 0410, 0510 |
| ATE_FUN.1 | Functional testing | 0410, 0510 |
| ATE_IND.2 | Independent testing - sample | 0410, 0510 |
| AVA_VAN.4 | Methodical vulnerability analysis | 0410, 0510 |

### EAL6: Semiformally Verified Design and Tested

EAL6 includes all EAL5 components plus:

| SAR Component | Description | Template Reference |
|---------------|-------------|-------------------|
| ADV_ARC.1 | Security architecture description | 0410, 0510 |
| ADV_FSP.5 | Complete semi-formal functional specification | 0410, 0510 |
| ADV_IMP.2 | Complete mapping of the implementation representation of the TSF | 0410, 0510 |
| ADV_INT.3 | Minimally complex internals | 0410, 0510 |
| ADV_SPM.1 | Formal TOE security policy model | 0410, 0510 |
| ADV_TDS.4 | Semiformal modular design | 0410, 0510 |
| ALC_DVS.2 | Sufficiency of security measures | 0410, 0510 |
| ATE_COV.3 | Rigorous analysis of coverage | 0410, 0510 |
| ATE_DPT.3 | Testing: modular design | 0410, 0510 |
| ATE_FUN.2 | Ordered functional testing | 0410, 0510 |
| ATE_IND.2 | Independent testing - sample | 0410, 0510 |
| AVA_VAN.5 | Advanced methodical vulnerability analysis | 0410, 0510 |

### EAL7: Formally Verified Design and Tested

EAL7 includes all EAL6 components plus:

| SAR Component | Description | Template Reference |
|---------------|-------------|-------------------|
| ADV_ARC.1 | Security architecture description | 0410, 0510 |
| ADV_FSP.6 | Complete semi-formal functional specification with additional error information | 0410, 0510 |
| ADV_IMP.2 | Complete mapping of the implementation representation of the TSF | 0410, 0510 |
| ADV_INT.3 | Minimally complex internals | 0410, 0510 |
| ADV_SPM.1 | Formal TOE security policy model | 0410, 0510 |
| ADV_TDS.5 | Complete semiformal modular design | 0410, 0510 |
| ALC_DVS.2 | Sufficiency of security measures | 0410, 0510 |
| ATE_COV.3 | Rigorous analysis of coverage | 0410, 0510 |
| ATE_DPT.4 | Testing: implementation representation | 0410, 0510 |
| ATE_FUN.2 | Ordered functional testing | 0410, 0510 |
| ATE_IND.3 | Independent testing - complete | 0410, 0510 |
| AVA_VAN.5 | Advanced methodical vulnerability analysis | 0410, 0510 |

## Protection Profile Conformance

When claiming conformance to a Protection Profile (PP), the following templates are relevant:

| Template | PP Conformance Aspect | Description |
|----------|----------------------|-------------|
| 0040_Conformance_Claims.md | PP identification | Identify the PP(s) to which the ST claims conformance |
| 0600_PP_Conformance.md | PP conformance demonstration | Demonstrate how the ST satisfies PP requirements |
| 0610_Rationale_for_Objectives.md | Objectives consistency | Show consistency between ST and PP objectives |
| 0620_Rationale_for_Requirements.md | Requirements consistency | Show consistency between ST and PP requirements |

### PP Conformance Types

- **Strict Conformance**: ST contains all PP requirements without additions
- **Demonstrable Conformance**: ST contains all PP requirements plus additional requirements
- **Package Augmentation**: ST augments a PP with additional assurance requirements

## Coverage Analysis

### Security Problem Coverage

| Security Problem Element | Addressed By | Template Reference |
|-------------------------|--------------|-------------------|
| Threats | Security Objectives for TOE | 0210, 0300, 0310, 0320 |
| Organizational Security Policies | Security Objectives for TOE | 0220, 0300, 0310, 0320 |
| Assumptions | Security Objectives for Environment | 0230, 0300, 0310, 0320 |

### Security Objectives Coverage

| Security Objective Element | Addressed By | Template Reference |
|---------------------------|--------------|-------------------|
| Security Objectives for TOE | Security Functional Requirements (SFRs) | 0300, 0400, 0420, 0440 |
| Security Objectives for Environment | Non-TOE security measures | 0300, 0310, 0320 |

### Security Requirements Coverage

| Security Requirement Element | Addressed By | Template Reference |
|----------------------------|--------------|-------------------|
| Security Functional Requirements (SFRs) | TOE Security Functions (TSFs) | 0400, 0500, 0520, 0530 |
| Security Assurance Requirements (SARs) | Assurance Measures | 0410, 0510 |

## Rationale Requirements

The Common Criteria requires comprehensive rationale documentation to demonstrate:

1. **Security Objectives Rationale** (Template 0310, 0610)
   - Each threat is countered by at least one security objective
   - Each OSP is covered by at least one security objective
   - Each assumption is covered by at least one security objective for the environment

2. **Security Requirements Rationale** (Template 0420, 0620)
   - Each security objective for the TOE is addressed by at least one SFR
   - Each SFR contributes to at least one security objective
   - All SFR dependencies are satisfied

3. **TOE Summary Specification Rationale** (Template 0520)
   - Each SFR is implemented by at least one TSF
   - Each TSF implements at least one SFR

## Coverage Matrices

The templates include several coverage matrices to demonstrate completeness:

| Matrix | Template | Purpose |
|--------|----------|---------|
| Threats/Objectives Matrix | 0320 | Maps threats to security objectives |
| OSPs/Objectives Matrix | 0320 | Maps OSPs to security objectives |
| Assumptions/Objectives Matrix | 0320 | Maps assumptions to security objectives for environment |
| Objectives/SFRs Matrix | 0440 | Maps security objectives to SFRs |
| SFRs/TSFs Matrix | 0530 | Maps SFRs to TOE security functions |
| SFR Dependencies Matrix | 0430 | Shows satisfaction of SFR dependencies |

## Template Completeness Checklist

To ensure complete coverage of ISO/IEC 15408 requirements, verify that:

- [ ] All mandatory ST sections are present (templates 0010-0650)
- [ ] TOE description is complete and unambiguous (templates 0100-0140)
- [ ] All threats, OSPs, and assumptions are identified (templates 0210-0240)
- [ ] Security objectives address all security problem elements (templates 0300-0330)
- [ ] All SFRs are from ISO/IEC 15408-2 (template 0400)
- [ ] All SARs match the selected EAL (template 0410)
- [ ] All SFR dependencies are satisfied (template 0430)
- [ ] All rationales are complete and traceable (templates 0310, 0420, 0520, 0610, 0620)
- [ ] All coverage matrices are complete (templates 0320, 0440, 0530)
- [ ] PP conformance is demonstrated (if applicable) (templates 0040, 0600)

## Gap Analysis

### Current Coverage

The template set provides comprehensive coverage of:
- ✅ All mandatory ST sections per ISO/IEC 15408-1, Section 8
- ✅ Support for all EAL levels (EAL1-EAL7)
- ✅ All SFR classes from ISO/IEC 15408-2
- ✅ All SAR classes from ISO/IEC 15408-3
- ✅ Protection Profile conformance demonstration
- ✅ Complete rationale documentation
- ✅ Coverage matrices for traceability

### Optional Enhancements

The following optional elements could be added in future versions:
- Extended packages (e.g., CCEVS, ANSSI-specific requirements)
- Composed evaluation templates (ACO class)
- Formal methods templates for EAL6/EAL7
- Specific PP templates for common domains (e.g., operating systems, smart cards, network devices)

## References

- ISO/IEC 15408-1:2022 - Information security, cybersecurity and privacy protection — Evaluation criteria for IT security — Part 1: Introduction and general model
- ISO/IEC 15408-2:2022 - Part 2: Security functional components
- ISO/IEC 15408-3:2022 - Part 3: Security assurance components
- Common Criteria Portal: https://www.commoncriteriaportal.org/
- Common Methodology for Information Technology Security Evaluation (CEM)

## Contact

For questions about this framework mapping or Common Criteria evaluation:
- Common Criteria Portal: https://www.commoncriteriaportal.org/
- National certification schemes (e.g., BSI, ANSSI, NIAP)
- Accredited evaluation laboratories

