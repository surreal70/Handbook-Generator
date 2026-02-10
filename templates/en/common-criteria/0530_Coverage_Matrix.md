# Coverage Matrix

**Document-ID:** 0530  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Update:** {{ meta.date }}  

---

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific TOE (Target of Evaluation).

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
The Coverage Matrix is a central overview showing how all security requirements
are covered by security functions, tests, and assurance measures.

IMPORTANT NOTES:
- The matrix must be complete - no gaps!
- Use clear markings (●, ○, ◐) for different coverage levels
- Ensure that each requirement has at least one coverage
- The matrix serves as an audit trail for the evaluation
-->

## 1. Introduction

### 1.1 Purpose

This document contains the complete Coverage Matrix for **[TODO: TOE Name]**. The matrix shows the mapping between:

- Security Objectives ↔ Threats, OSPs, Assumptions
- Security Functional Requirements (SFRs) ↔ Security Objectives
- TOE Security Functions (TSFs) ↔ SFRs
- Tests ↔ TSFs and SFRs
- Assurance Measures ↔ Security Assurance Requirements (SARs)

### 1.2 Legend

**Coverage Levels:**
- ● = Complete coverage
- ◐ = Partial coverage
- ○ = Supporting coverage
- (empty) = No coverage

## 2. Security Objectives Coverage

### 2.1 Security Objectives for TOE ↔ Threats

This matrix shows how the Security Objectives for TOE address the identified Threats:

| Threat-ID | Threat-Name | O.TOE-1 | O.TOE-2 | O.TOE-3 | O.TOE-4 | O.TOE-5 |
|-----------|-------------|---------|---------|---------|---------|---------|
| T.[TODO] | [TODO] | ● | | | | |
| T.[TODO] | [TODO] | ● | ● | | | |
| T.[TODO] | [TODO] | | ● | | | |
| T.[TODO] | [TODO] | | | ● | | |
| T.[TODO] | [TODO] | | | ● | ◐ | |

<!-- 
GUIDANCE:
- List all Threats from Chapter 2 (Security Problem Definition)
- List all Security Objectives for TOE from Chapter 3
- Mark which Objective addresses which Threat
- Ensure that each Threat is covered by at least one Objective
-->

**Completeness Check:**
- Number of Threats: [TODO]
- Number of covered Threats: [TODO]
- Uncovered Threats: [TODO: List or "None"]

### 2.2 Security Objectives for TOE ↔ Organizational Security Policies

This matrix shows how the Security Objectives for TOE fulfill the OSPs:

| OSP-ID | OSP-Name | O.TOE-1 | O.TOE-2 | O.TOE-3 | O.TOE-4 | O.TOE-5 |
|--------|----------|---------|---------|---------|---------|---------|
| P.[TODO] | [TODO] | ● | | | | |
| P.[TODO] | [TODO] | | ● | | | |
| P.[TODO] | [TODO] | | | ● | | |

**Completeness Check:**
- Number of OSPs: [TODO]
- Number of covered OSPs: [TODO]
- Uncovered OSPs: [TODO: List or "None"]

### 2.3 Security Objectives for Environment ↔ Threats

This matrix shows how the Security Objectives for Environment address the Threats:

| Threat-ID | Threat-Name | O.ENV-1 | O.ENV-2 | O.ENV-3 | O.ENV-4 |
|-----------|-------------|---------|---------|---------|---------|
| T.[TODO] | [TODO] | ● | | | |
| T.[TODO] | [TODO] | | ● | | |
| T.[TODO] | [TODO] | | | ● | |

### 2.4 Security Objectives for Environment ↔ Assumptions

This matrix shows how the Security Objectives for Environment fulfill the Assumptions:

| Assumption-ID | Assumption-Name | O.ENV-1 | O.ENV-2 | O.ENV-3 | O.ENV-4 |
|---------------|-----------------|---------|---------|---------|---------|
| A.[TODO] | [TODO] | ● | | | |
| A.[TODO] | [TODO] | | ● | | |
| A.[TODO] | [TODO] | | | ● | |

**Completeness Check:**
- Number of Assumptions: [TODO]
- Number of covered Assumptions: [TODO]
- Uncovered Assumptions: [TODO: List or "None"]

## 3. Security Functional Requirements Coverage

### 3.1 SFRs ↔ Security Objectives for TOE

This matrix shows how the SFRs fulfill the Security Objectives for TOE:

| SFR-ID | SFR-Name | O.TOE-1 | O.TOE-2 | O.TOE-3 | O.TOE-4 | O.TOE-5 |
|--------|----------|---------|---------|---------|---------|---------|
| FAU_GEN.1 | Audit data generation | ● | | | | |
| FAU_SAR.1 | Audit review | ● | | | | |
| FCS_CKM.1 | Cryptographic key generation | | ● | | | |
| FCS_COP.1 | Cryptographic operation | | ● | | | |
| FDP_ACC.1 | Subset access control | | | ● | | |
| FDP_ACF.1 | Security attribute based access control | | | ● | | |
| FIA_UID.1 | Timing of identification | | | | ● | |
| FIA_UAU.1 | Timing of authentication | | | | ● | |
| FIA_AFL.1 | Authentication failure handling | | | | ● | |
| FMT_SMF.1 | Specification of management functions | | | | | ● |
| FMT_SMR.1 | Security roles | | | | | ● |
| FPT_STM.1 | Reliable time stamps | ● | | | | |
| FTA_SSL.1 | TSF-initiated session locking | | | | ● | |
| FTP_TRP.1 | Trusted path | | | | ● | |

<!-- 
GUIDANCE:
- List all SFRs from Chapter 4 (Security Requirements)
- Mark which SFR fulfills which Security Objective
- Ensure that each SFR is assigned to at least one Objective
- Ensure that each Objective is fulfilled by at least one SFR
-->

**Completeness Check:**
- Number of SFRs: [TODO]
- Number of Security Objectives for TOE: [TODO]
- Uncovered SFRs: [TODO: List or "None"]
- Uncovered Objectives: [TODO: List or "None"]

## 4. TOE Security Functions Coverage

### 4.1 TSFs ↔ SFRs

This matrix shows how the TSFs implement the SFRs:

| SFR-ID | SFR-Name | TSF-1 | TSF-2 | TSF-3 | TSF-4 | TSF-5 | TSF-6 |
|--------|----------|-------|-------|-------|-------|-------|-------|
| FAU_GEN.1 | Audit data generation | | | ● | | | |
| FAU_SAR.1 | Audit review | | | ● | | | |
| FCS_CKM.1 | Cryptographic key generation | | | | ● | | |
| FCS_COP.1 | Cryptographic operation | | | | ● | | |
| FDP_ACC.1 | Subset access control | | ● | | | | |
| FDP_ACF.1 | Security attribute based access control | | ● | | | | |
| FIA_UID.1 | Timing of identification | ● | | | | | |
| FIA_UAU.1 | Timing of authentication | ● | | | | | |
| FIA_AFL.1 | Authentication failure handling | ● | | | | | |
| FMT_SMF.1 | Specification of management functions | | | | | ● | |
| FMT_SMR.1 | Security roles | | | | | ● | |
| FPT_STM.1 | Reliable time stamps | | | | | | ● |
| FTA_SSL.1 | TSF-initiated session locking | ● | | | | | |
| FTP_TRP.1 | Trusted path | | | | | | ● |

<!-- 
GUIDANCE:
- List all TSFs from Chapter 5 (TOE Summary Specification)
- Mark which TSF implements which SFR
- Ensure that each SFR is covered by at least one TSF
- An SFR can be implemented by multiple TSFs
-->

**TSF Descriptions:**

| TSF-ID | TSF-Name | Description |
|--------|----------|-------------|
| TSF-1 | [TODO] | [TODO: Brief description] |
| TSF-2 | [TODO] | [TODO: Brief description] |
| TSF-3 | [TODO] | [TODO: Brief description] |
| TSF-4 | [TODO] | [TODO: Brief description] |
| TSF-5 | [TODO] | [TODO: Brief description] |
| TSF-6 | [TODO] | [TODO: Brief description] |

**Completeness Check:**
- Number of SFRs: [TODO]
- Number of covered SFRs: [TODO]
- Uncovered SFRs: [TODO: List or "None"]

## 5. Test Coverage

### 5.1 Tests ↔ TSFs

This matrix shows how the tests verify the TSFs:

| TSF-ID | TSF-Name | Test-1 | Test-2 | Test-3 | Test-4 | Test-5 | Test-6 |
|--------|----------|--------|--------|--------|--------|--------|--------|
| TSF-1 | [TODO] | ● | ● | | | | |
| TSF-2 | [TODO] | | | ● | | | |
| TSF-3 | [TODO] | | | | ● | ● | |
| TSF-4 | [TODO] | | | | | | ● |
| TSF-5 | [TODO] | | ● | | | | |
| TSF-6 | [TODO] | ● | | | | | |

<!-- 
GUIDANCE:
- List all tests from the Test Plan
- Mark which test verifies which TSF
- Ensure that each TSF is covered by at least one test
- Multiple tests per TSF are recommended
-->

**Test Descriptions:**

| Test-ID | Test-Name | Description | Test Type |
|---------|-----------|-------------|-----------|
| Test-1 | [TODO] | [TODO] | Unit / Integration / System |
| Test-2 | [TODO] | [TODO] | Unit / Integration / System |
| Test-3 | [TODO] | [TODO] | Unit / Integration / System |
| Test-4 | [TODO] | [TODO] | Unit / Integration / System |
| Test-5 | [TODO] | [TODO] | Unit / Integration / System |
| Test-6 | [TODO] | [TODO] | Unit / Integration / System |

**Completeness Check:**
- Number of TSFs: [TODO]
- Number of tested TSFs: [TODO]
- Untested TSFs: [TODO: List or "None"]

### 5.2 Tests ↔ SFRs (indirect via TSFs)

This matrix shows the indirect coverage of SFRs by tests:

| SFR-ID | SFR-Name | Test-1 | Test-2 | Test-3 | Test-4 | Test-5 | Test-6 |
|--------|----------|--------|--------|--------|--------|--------|--------|
| FAU_GEN.1 | Audit data generation | | | | ● | ● | |
| FAU_SAR.1 | Audit review | | | | ● | ● | |
| FCS_CKM.1 | Cryptographic key generation | | | | | | ● |
| FCS_COP.1 | Cryptographic operation | | | | | | ● |
| FDP_ACC.1 | Subset access control | | | ● | | | |
| FDP_ACF.1 | Security attribute based access control | | | ● | | | |
| FIA_UID.1 | Timing of identification | ● | ● | | | | |
| FIA_UAU.1 | Timing of authentication | ● | ● | | | | |
| FIA_AFL.1 | Authentication failure handling | ● | ● | | | | |
| FMT_SMF.1 | Specification of management functions | | ● | | | | |
| FMT_SMR.1 | Security roles | | ● | | | | |
| FPT_STM.1 | Reliable time stamps | ● | | | | | |
| FTA_SSL.1 | TSF-initiated session locking | ● | ● | | | | |
| FTP_TRP.1 | Trusted path | ● | | | | | |

**Completeness Check:**
- Number of SFRs: [TODO]
- Number of tested SFRs: [TODO]
- Untested SFRs: [TODO: List or "None"]

## 6. Assurance Measures Coverage

### 6.1 Assurance Measures ↔ SARs

This matrix shows how the Assurance Measures fulfill the SARs:

| SAR-ID | SAR-Name | AM-1 | AM-2 | AM-3 | AM-4 | AM-5 | AM-6 |
|--------|----------|------|------|------|------|------|------|
| ACM_CAP.4 | Generation support and acceptance procedures | ● | | | | | |
| ACM_SCP.2 | Problem tracking CM coverage | ● | | | | | |
| ADO_DEL.2 | Detection of modification | | ● | | | | |
| ADO_IGS.1 | Installation, generation, and start-up procedures | | ● | | | | |
| ADV_FSP.2 | Security-enforcing functional specification | | | ● | | | |
| ADV_IMP.1 | Implementation representation of the TSF | | | ● | | | |
| ADV_TDS.2 | Architectural design | | | ● | | | |
| AGD_ADM.1 | Administrator guidance | | | | ● | | |
| AGD_USR.1 | User guidance | | | | ● | | |
| ALC_DVS.1 | Identification of security measures | | | | | ● | |
| ALC_LCD.1 | Developer defined life-cycle model | | | | | ● | |
| ALC_TAT.1 | Well-defined development tools | | | | | ● | |
| ATE_COV.2 | Analysis of coverage | | | | | | ● |
| ATE_DPT.1 | Testing: high-level design | | | | | | ● |
| ATE_FUN.1 | Functional testing | | | | | | ● |
| ATE_IND.2 | Independent testing - sample | | | | | | ● |
| AVA_MSU.2 | Validation of analysis | | | | | | ● |
| AVA_SOF.1 | Strength of TOE security function evaluation | | | | | | ● |
| AVA_VLA.2 | Independent vulnerability analysis | | | | | | ● |

<!-- 
GUIDANCE:
- List all SARs for the chosen EAL
- List all Assurance Measures from Chapter 5
- Mark which Assurance Measure fulfills which SAR
- Ensure that each SAR is covered by at least one Assurance Measure
-->

**Assurance Measure Descriptions:**

| AM-ID | AM-Name | Description |
|-------|---------|-------------|
| AM-1 | Configuration Management | [TODO] |
| AM-2 | Delivery and Operation | [TODO] |
| AM-3 | Development Documentation | [TODO] |
| AM-4 | Guidance Documents | [TODO] |
| AM-5 | Life Cycle Support | [TODO] |
| AM-6 | Testing and Vulnerability Assessment | [TODO] |

**Completeness Check:**
- Number of SARs: [TODO]
- Number of covered SARs: [TODO]
- Uncovered SARs: [TODO: List or "None"]

## 7. Overall Summary

### 7.1 End-to-End Traceability

This overview shows the complete traceability from Threats to Tests:

```
Threats/OSPs/Assumptions
    ↓
Security Objectives (TOE & Environment)
    ↓
Security Functional Requirements (SFRs)
    ↓
TOE Security Functions (TSFs)
    ↓
Tests
```

**Completeness Check:**
- ✓ All Threats are covered by Security Objectives
- ✓ All Security Objectives are fulfilled by SFRs
- ✓ All SFRs are implemented by TSFs
- ✓ All TSFs are verified by Tests
- ✓ All SARs are fulfilled by Assurance Measures

### 7.2 Statistics

| Category | Count | Covered | Coverage Rate |
|----------|-------|---------|---------------|
| Threats | [TODO] | [TODO] | [TODO]% |
| OSPs | [TODO] | [TODO] | [TODO]% |
| Assumptions | [TODO] | [TODO] | [TODO]% |
| Security Objectives (TOE) | [TODO] | [TODO] | [TODO]% |
| Security Objectives (ENV) | [TODO] | [TODO] | [TODO]% |
| SFRs | [TODO] | [TODO] | [TODO]% |
| TSFs | [TODO] | [TODO] | [TODO]% |
| Tests | [TODO] | [TODO] | [TODO]% |
| SARs | [TODO] | [TODO] | [TODO]% |
| Assurance Measures | [TODO] | [TODO] | [TODO]% |

### 7.3 Identified Gaps

[TODO: List all identified gaps in coverage. If no gaps exist, write "No gaps identified".]

| Category | Element | Gap | Action |
|----------|---------|-----|--------|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 8. Summary

The Coverage Matrix demonstrates:

- ✓ Complete traceability from Threats to Tests
- ✓ All security requirements are covered
- ✓ All security functions are tested
- ✓ All Assurance Requirements are fulfilled
- ✓ No critical gaps in coverage

**Status:** [TODO: Complete / With Gaps / In Progress]

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [TODO] | [TODO] | Initial version |
| 1.0 | [TODO] | [TODO] | [TODO] |
