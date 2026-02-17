# Requirements Rationale

**Document-ID:** 0420
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
This template provides the rationale for the security requirements selected in document 0400.
The rationale must demonstrate that:
1. All SFRs are necessary and sufficient to meet the security objectives for the TOE
2. All SFR dependencies are satisfied
3. The selected SARs are appropriate for the evaluation assurance level
4. The security requirements are internally consistent

Key considerations:
- Each SFR must be traced back to at least one security objective
- Each security objective must be addressed by at least one SFR
- The rationale must be clear, logical, and auditable
- Any augmentation of the EAL package must be justified
-->

## 1. Introduction

This document justifies the selection of security requirements (Security Functional Requirements and Security Assurance Requirements) for the TOE. The rationale demonstrates that:

1. All SFRs are necessary and sufficient to meet the security objectives for the TOE
2. All SFR dependencies are satisfied
3. The selected SARs correspond to the Evaluation Assurance Level
4. The security requirements are internally consistent and non-contradictory

## 2. Derivation of SFRs from Security Objectives

### 2.1 Mapping: Security Objectives → SFRs

The following table shows the mapping between security objectives for the TOE (from document 0300) and Security Functional Requirements (from document 0400):

<!-- TODO: Create complete mapping table -->

| Security Objective | Assigned SFRs | Rationale |
|-------------------|---------------|-----------|
| [TODO: O.AUDIT] | FAU_GEN.1, FAU_SAR.1, FPT_STM.1 | [TODO: Rationale for assignment] |
| [TODO: O.CRYPTO] | FCS_COP.1, FCS_CKM.1 | [TODO: Rationale for assignment] |
| [TODO: O.ACCESS] | FDP_ACC.1, FDP_ACF.1, FIA_UID.1, FIA_UAU.1 | [TODO: Rationale for assignment] |
| [TODO] | [TODO] | [TODO] |

### 2.2 Detailed Rationale per Security Objective

#### 2.2.1 [TODO: Security Objective 1]

**Security Objective:** [TODO: Description from document 0300]

**Assigned SFRs:**
- [TODO: SFR-ID]: [TODO: Rationale for how this SFR fulfills the objective]
- [TODO: SFR-ID]: [TODO: Rationale]

**Completeness:** [TODO: Explanation why these SFRs are sufficient]

#### 2.2.2 [TODO: Security Objective 2]

**Security Objective:** [TODO: Description from document 0300]

**Assigned SFRs:**
- [TODO: SFR-ID]: [TODO: Rationale]

**Completeness:** [TODO: Explanation]

<!-- TODO: Repeat for all security objectives -->

### 2.3 Completeness Analysis

**Coverage of Security Objectives:**
- Number of security objectives for TOE: [TODO: X]
- Number of objectives addressed by SFRs: [TODO: X]
- Coverage rate: [TODO: 100%]

**Objectives Not Addressed by SFRs:**
[TODO: If any, list and justify why no SFRs are required]

## 3. Necessity of SFRs

### 3.1 Rationale per SFR

Each selected SFR must be necessary to fulfill at least one security objective.

#### 3.1.1 [TODO: SFR-ID 1]

**SFR:** [TODO: Name and description]

**Addressed Security Objectives:**
- [TODO: Objective-ID]: [TODO: How the SFR contributes to the objective]

**Necessity:** [TODO: Why this SFR is indispensable]

**Alternatives:** [TODO: Why alternative SFRs were not selected]

#### 3.1.2 [TODO: SFR-ID 2]

**SFR:** [TODO: Name and description]

**Addressed Security Objectives:**
- [TODO: Objective-ID]: [TODO: Rationale]

**Necessity:** [TODO: Rationale]

<!-- TODO: Repeat for all SFRs -->

### 3.2 Superfluous SFRs

[TODO: Confirm that no superfluous SFRs are included]

All selected SFRs are necessary and contribute to fulfilling at least one security objective. No superfluous SFRs have been identified.

## 4. SFR Dependencies

### 4.1 Overview of Dependencies

The following table shows all SFR dependencies and their satisfaction:

<!-- TODO: Create complete dependency table (see also document 0430) -->

| SFR | Dependency | Satisfied by | Status |
|-----|------------|--------------|--------|
| FAU_GEN.1 | FPT_STM.1 | FPT_STM.1 | ✓ Satisfied |
| FCS_COP.1 | FCS_CKM.1 or FDP_ITC.1/2 | FCS_CKM.1 | ✓ Satisfied |
| FDP_ACC.1 | FDP_ACF.1 | FDP_ACF.1 | ✓ Satisfied |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 4.2 Satisfaction of All Dependencies

**Summary:**
- Number of SFRs with dependencies: [TODO: X]
- Number of satisfied dependencies: [TODO: X]
- Number of unsatisfied dependencies: [TODO: 0]

[TODO: If dependencies are not satisfied, justify this in detail]

### 4.3 Detailed Rationale for Critical Dependencies

[TODO: For complex or critical dependencies, provide detailed explanations]

**Example:**
```
FCS_COP.1 requires FCS_CKM.1 (Cryptographic key generation) because cryptographic 
operations can only be performed securely with correctly generated keys. This dependency 
is satisfied by the implementation of FCS_CKM.1, which specifies the generation of keys 
according to [Standard].
```

## 5. Internal Consistency of SFRs

### 5.1 Consistency Check

[TODO: Demonstrate that the SFRs are internally consistent]

**Checked Aspects:**
- No contradictory requirements
- Compatible operations (Assignments, Selections)
- Consistent terminology
- No overlaps or redundancies

**Result:** [TODO: Confirmation of consistency]

### 5.2 Identified Conflicts and Resolution

[TODO: If conflicts were identified, describe their resolution]

**Example:**
```
Conflict: FDP_ACC.1 and FMT_MSA.1 could have different interpretations of 
"security attributes".

Resolution: The security attributes were clearly defined in section X.Y and 
both SFRs use this consistent definition.
```

## 6. Rationale for SARs

### 6.1 EAL Selection

**Selected EAL:** [TODO: e.g., EAL4]

**Rationale:** [TODO: Reference to document 0410 and summary]

The selection of EAL [TODO: X] is appropriate because:
- [TODO: Rationale 1]
- [TODO: Rationale 2]
- [TODO: Rationale 3]

### 6.2 Augmentation

[TODO: If additional SARs beyond the EAL package are used]

**Additional SARs:**
- [TODO: SAR-ID]: [TODO: Rationale for addition]

**No Augmentation:**
[TODO: If no augmentation, confirm this]

The standard SARs for EAL [TODO: X] are sufficient for the evaluation of the TOE. No additional SARs are required.

## 7. Addressing Security Objectives for the Environment

### 7.1 Non-TOE Security Requirements

[TODO: Explain how security objectives for the environment are addressed]

The security objectives for the environment (from document 0300) are not addressed by SFRs, but by:
- Organizational measures
- Physical security measures
- Environmental assumptions

**Example:**
```
O.ENV_PHYSICAL (Physical protection) is addressed by organizational measures such as 
access controls and monitoring, not by TOE functionality.
```

## 8. Traceability

### 8.1 Traceability Matrix

Complete traceability between threats, security objectives, and SFRs is shown in the following matrix:

<!-- TODO: Create complete Traceability Matrix -->

| Threat | Security Objective | SFR | Rationale |
|--------|-------------------|-----|-----------|
| T.UNAUTH_ACCESS | O.ACCESS | FIA_UID.1, FIA_UAU.1, FDP_ACC.1 | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 8.2 Coverage Matrix

A detailed Coverage Matrix can be found in document 0440.

## 9. Summary

### 9.1 Completeness

The selected security requirements are complete:
- ✓ All security objectives for the TOE are addressed by SFRs
- ✓ All SFR dependencies are satisfied
- ✓ The SARs correspond to the selected EAL

### 9.2 Consistency

The security requirements are consistent:
- ✓ No contradictory requirements
- ✓ Internal consistency of SFRs
- ✓ Consistent terminology

### 9.3 Appropriateness

The security requirements are appropriate:
- ✓ Necessary to fulfill security objectives
- ✓ Sufficient to address threats
- ✓ Practically implementable in the TOE

## 10. References

- Document 0200: Security Problem Definition
- Document 0300: Security Objectives
- Document 0400: Security Requirements
- Document 0410: Evaluation Assurance Level
- Document 0430: SFR Dependencies
- Document 0440: Coverage Matrix
- ISO/IEC 15408-2:2022 - Security functional requirements
- ISO/IEC 15408-3:2022 - Security assurance requirements

**Next Steps:**
1. Complete all [TODO] placeholders
2. Create complete mapping tables
3. Verify all dependencies
4. Conduct peer review of rationale
5. Update when objectives or requirements change

