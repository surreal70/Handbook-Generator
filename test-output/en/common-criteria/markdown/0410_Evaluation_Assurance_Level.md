# Evaluation Assurance Level (EAL)

**Document-ID:** 0410
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

---

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific Target of Evaluation (TOE).



## 1. Introduction

This document describes the selection and justification of the Evaluation Assurance Level (EAL) for the TOE. The EAL defines the depth and rigor of the security evaluation according to ISO/IEC 15408-3.

## 2. EAL Overview

Common Criteria defines seven predefined Evaluation Assurance Levels:

| EAL | Designation | Description | Typical Application |
|-----|-------------|-------------|-------------------|
| EAL1 | Functionally tested | Basic functional testing | Commercial off-the-shelf products |
| EAL2 | Structurally tested | Structural testing with developer documentation | Commercial products with security functions |
| EAL3 | Methodically tested and checked | Methodical testing and checking | Security products with moderate requirements |
| EAL4 | Methodically designed, tested, and reviewed | Methodical design, testing, and review | Security products for commercial environments |
| EAL5 | Semiformally designed and tested | Semiformal design and testing | High-security products |
| EAL6 | Semiformally verified design and tested | Semiformal verification and testing | High-security environments with high risk |
| EAL7 | Formally verified design and tested | Formal verification and testing | Extremely high security requirements |

## 3. Selected EAL

**Selected Evaluation Assurance Level:** [TODO: e.g., EAL4]

### 3.1 Justification for EAL Selection

[TODO: Justify the EAL selection based on:]
- Threat landscape and risk assessment
- Protection needs of assets to be protected
- Operational environment of the TOE
- Cost-benefit ratio
- Market requirements and regulatory mandates
- Development resources and timeline

**Example:**
```
EAL4 was selected as it provides a balanced ratio between security assurance and 
development effort. The TOE will be deployed in commercial environments with moderate to 
high security requirements. EAL4 requires methodical design, testing, and review, which 
corresponds to the security requirements of the target environment without requiring the 
formal verification requirements of higher EALs.
```

### 3.2 Alternatives and Trade-offs

[TODO: Discuss alternative EALs and why they were not selected]

**Lower EALs (e.g., EAL3):**
- [TODO: Why not sufficient?]

**Higher EALs (e.g., EAL5+):**
- [TODO: Why not required or not practical?]

## 4. Security Assurance Requirements (SARs) for Selected EAL

### 4.1 Mandatory SARs for EAL [TODO: X]

The following Security Assurance Requirements are mandatory for EAL [TODO: X]:

#### 4.1.1 Security Target Evaluation (ASE)

- **ASE_CCL.1** Conformance claims
- **ASE_ECD.1** Extended components definition
- **ASE_INT.1** ST introduction
- **ASE_OBJ.2** Security objectives
- **ASE_REQ.2** Derived security requirements
- **ASE_SPD.1** Security problem definition
- **ASE_TSS.1** TOE summary specification

#### 4.1.2 Development (ADV)

[TODO: Add ADV components for selected EAL]

**For EAL4:**
- **ADV_ARC.1** Security architecture description
- **ADV_FSP.4** Complete functional specification
- **ADV_IMP.1** Implementation representation of the TSF
- **ADV_TDS.3** Basic modular design

#### 4.1.3 Guidance Documents (AGD)

- **AGD_OPE.1** Operational user guidance
- **AGD_PRE.1** Preparative procedures

#### 4.1.4 Life-cycle Support (ALC)

[TODO: Add ALC components for selected EAL]

**For EAL4:**
- **ALC_CMC.4** Production support, acceptance procedures and automation
- **ALC_CMS.4** Problem tracking CM coverage
- **ALC_DEL.1** Delivery procedures
- **ALC_DVS.1** Identification of security measures
- **ALC_LCD.1** Developer defined life-cycle model
- **ALC_TAT.1** Well-defined development tools

#### 4.1.5 Tests (ATE)

[TODO: Add ATE components for selected EAL]

**For EAL4:**
- **ATE_COV.2** Analysis of coverage
- **ATE_DPT.1** Testing: high-level design
- **ATE_FUN.1** Functional testing
- **ATE_IND.2** Independent testing - sample

#### 4.1.6 Vulnerability Assessment (AVA)

[TODO: Add AVA components for selected EAL]

**For EAL4:**
- **AVA_VAN.3** Focused vulnerability analysis

### 4.2 Augmentation (Additional SARs)

[TODO: If additional SARs beyond the selected EAL are used, list and justify them here]

**Example:**
```
In addition to the EAL4 requirements, the following SARs are added:
- ALC_FLR.2 Flaw reporting procedures (from EAL5)
  Justification: Enhanced vulnerability management for production environments
```

## 5. Development and Evaluation Effort

### 5.1 Development Effort

[TODO: Estimate the additional development effort for the selected EAL]

**Documentation Effort:**
- [TODO: Required documents and estimated effort]

**Process Requirements:**
- [TODO: Required development processes and tools]

**Testing Effort:**
- [TODO: Required tests and test coverage]

### 5.2 Evaluation Effort

[TODO: Estimate duration and costs of evaluation]

**Estimated Evaluation Duration:** [TODO: e.g., 6-12 months]  
**Estimated Evaluation Costs:** [TODO: Cost range]  
**Evaluation Laboratory:** [TODO: Planned or selected laboratory]

## 6. Compliance and Certification

### 6.1 Certification Scheme

[TODO: Specify the certification scheme]

**Examples:**
- Common Criteria Recognition Arrangement (CCRA)
- National scheme (e.g., BSI Germany, ANSSI France)
- [TODO: Specific scheme]

### 6.2 Mutual Recognition

[TODO: Describe Mutual Recognition Agreements if relevant]

The selected EAL and certification scheme enables recognition in the following countries:
- [TODO: List of countries with Mutual Recognition]

## 7. Timeline and Milestones

[TODO: Create a rough timeline for the evaluation]

| Milestone | Planned Date | Status |
|-----------|--------------|--------|
| ST Completion | [TODO] | [TODO] |
| Evaluation Start | [TODO] | [TODO] |
| ADV Phase Completed | [TODO] | [TODO] |
| ATE Phase Completed | [TODO] | [TODO] |
| AVA Phase Completed | [TODO] | [TODO] |
| Certification | [TODO] | [TODO] |

## 8. Risks and Mitigation

[TODO: Identify risks for the evaluation]

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [TODO: e.g., Delays in documentation] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

## 9. References

- ISO/IEC 15408-3:2022 - Security assurance requirements
- Common Criteria for Information Technology Security Evaluation - Evaluation Assurance Levels
- [TODO: National certification guidelines]
- [TODO: Other relevant documents]

**Next Steps:**
1. Complete all [TODO] placeholders
2. Validate EAL selection with stakeholders
3. Confirm availability of resources for evaluation
4. Contact potential evaluation laboratories
5. Create detailed project plan for evaluation

