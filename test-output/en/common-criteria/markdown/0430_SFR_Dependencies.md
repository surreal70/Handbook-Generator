# SFR Dependencies

**Document-ID:** 0430
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

This document documents all dependencies between the Security Functional Requirements (SFRs) of the TOE and demonstrates their satisfaction. According to ISO/IEC 15408-2, SFRs may have dependencies on other SFRs that must be satisfied for the requirement to function correctly.

## 2. Overview of SFR Dependencies

### 2.1 Summary

**Statistics:**
- Number of selected SFRs: [TODO: X]
- Number of SFRs with dependencies: [TODO: X]
- Total number of dependencies: [TODO: X]
- Number of satisfied dependencies: [TODO: X]
- Number of unsatisfied dependencies: [TODO: 0]

**Status:** [TODO: ✓ All dependencies satisfied / ⚠ Dependencies not satisfied]

### 2.2 Complete Dependency Table



| SFR-ID | SFR-Name | Dependency | Satisfied by | Status | Notes |
|--------|----------|------------|--------------|--------|-------|
| FAU_GEN.1 | Audit data generation | FPT_STM.1 | FPT_STM.1 | ✓ | Time stamps for audit records |
| FAU_SAR.1 | Audit review | FAU_GEN.1 | FAU_GEN.1 | ✓ | Audit data must be generated |
| FCS_CKM.1 | Cryptographic key generation | [FCS_CKM.2 or FCS_COP.1] | FCS_COP.1 | ✓ | Keys for cryptographic operations |
| FCS_COP.1 | Cryptographic operation | [FDP_ITC.1 or FDP_ITC.2 or FCS_CKM.1] | FCS_CKM.1 | ✓ | Key generation |
| FDP_ACC.1 | Subset access control | FDP_ACF.1 | FDP_ACF.1 | ✓ | Access control functions |
| FDP_ACF.1 | Security attribute based access control | FDP_ACC.1, FMT_MSA.3 | FDP_ACC.1, FMT_MSA.3 | ✓ | Access control policy and attribute management |
| FIA_UAU.1 | Timing of authentication | FIA_UID.1 | FIA_UID.1 | ✓ | Identification before authentication |
| FIA_UID.1 | Timing of identification | None | N/A | ✓ | No dependencies |
| FMT_MSA.1 | Management of security attributes | [FDP_ACC.1 or FDP_IFC.1], FMT_SMR.1, FMT_SMF.1 | FDP_ACC.1, FMT_SMR.1, FMT_SMF.1 | ✓ | Access control and role management |
| FMT_MSA.3 | Static attribute initialisation | FMT_MSA.1, FMT_SMR.1 | FMT_MSA.1, FMT_SMR.1 | ✓ | Attribute management and roles |
| FMT_SMF.1 | Specification of Management Functions | None | N/A | ✓ | No dependencies |
| FMT_SMR.1 | Security roles | FIA_UID.1 | FIA_UID.1 | ✓ | Identification for role assignment |
| FPT_STM.1 | Reliable time stamps | None | N/A | ✓ | No dependencies |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 3. Detailed Dependency Analysis

### 3.1 Security Audit (FAU)

#### FAU_GEN.1 Audit data generation

**Dependencies:**
- FPT_STM.1 Reliable time stamps

**Satisfaction:**
FPT_STM.1 is included in the Security Target and provides reliable time stamps for audit records.

**Rationale:**
Audit records must be timestamped with precise time information to ensure chronological traceability of security events.

#### FAU_SAR.1 Audit review

**Dependencies:**
- FAU_GEN.1 Audit data generation

**Satisfaction:**
FAU_GEN.1 is included in the Security Target and generates the audit data that is reviewed by FAU_SAR.1.

**Rationale:**
Audit data must exist before it can be reviewed.

### 3.2 Cryptographic Support (FCS)

#### FCS_CKM.1 Cryptographic key generation

**Dependencies:**
- [FCS_CKM.2 Cryptographic key distribution] or [FCS_COP.1 Cryptographic operation]

**Satisfaction:**
FCS_COP.1 is included in the Security Target. Generated keys are used for cryptographic operations.

**Rationale:**
Keys must be generated for a purpose. In this case, they are used for cryptographic operations (FCS_COP.1).

#### FCS_COP.1 Cryptographic operation

**Dependencies:**
- [FDP_ITC.1 Import of user data without security attributes] or [FDP_ITC.2 Import of user data with security attributes] or [FCS_CKM.1 Cryptographic key generation]

**Satisfaction:**
FCS_CKM.1 is included in the Security Target and generates the keys required for cryptographic operations.

**Rationale:**
Cryptographic operations require keys that must either be imported or generated.

### 3.3 User Data Protection (FDP)

#### FDP_ACC.1 Subset access control

**Dependencies:**
- FDP_ACF.1 Security attribute based access control

**Satisfaction:**
FDP_ACF.1 is included in the Security Target and defines the access control functions.

**Rationale:**
An access control policy (FDP_ACC.1) requires access control functions (FDP_ACF.1) for enforcement.

#### FDP_ACF.1 Security attribute based access control

**Dependencies:**
- FDP_ACC.1 Subset access control
- FMT_MSA.3 Static attribute initialisation

**Satisfaction:**
Both dependencies are included in the Security Target.

**Rationale:**
- FDP_ACC.1: Access control functions require an access control policy
- FMT_MSA.3: Security attributes must be initialized before they can be used for access decisions

### 3.4 Identification and Authentication (FIA)

#### FIA_UID.1 Timing of identification

**Dependencies:**
None

**Satisfaction:**
N/A

#### FIA_UAU.1 Timing of authentication

**Dependencies:**
- FIA_UID.1 Timing of identification

**Satisfaction:**
FIA_UID.1 is included in the Security Target.

**Rationale:**
Users must be identified before they can be authenticated.

### 3.5 Security Management (FMT)

#### FMT_MSA.1 Management of security attributes

**Dependencies:**
- [FDP_ACC.1 Subset access control] or [FDP_IFC.1 Subset information flow control]
- FMT_SMR.1 Security roles
- FMT_SMF.1 Specification of Management Functions

**Satisfaction:**
All dependencies are included in the Security Target.

**Rationale:**
- FDP_ACC.1: Security attributes are used for access control
- FMT_SMR.1: Management of attributes requires role definitions
- FMT_SMF.1: Management functions must be specified

#### FMT_MSA.3 Static attribute initialisation

**Dependencies:**
- FMT_MSA.1 Management of security attributes
- FMT_SMR.1 Security roles

**Satisfaction:**
Both dependencies are included in the Security Target.

**Rationale:**
Attribute initialization requires attribute management and role definitions.

#### FMT_SMF.1 Specification of Management Functions

**Dependencies:**
None

**Satisfaction:**
N/A

#### FMT_SMR.1 Security roles

**Dependencies:**
- FIA_UID.1 Timing of identification

**Satisfaction:**
FIA_UID.1 is included in the Security Target.

**Rationale:**
Roles can only be assigned to identified users.

### 3.6 Protection of the TSF (FPT)

#### FPT_STM.1 Reliable time stamps

**Dependencies:**
None

**Satisfaction:**
N/A

### 3.7 [TODO: Additional SFR Classes]

[TODO: Add dependency analyses for all other used SFRs]

## 4. Dependency Graph

### 4.1 Visualization

[TODO: Create a dependency graph that visualizes the relationships between SFRs]

```
Example Graph (as text):

FIA_UID.1 ──┬──> FIA_UAU.1
            └──> FMT_SMR.1 ──┬──> FMT_MSA.1 ──> FDP_ACF.1 ──┐
                             └──> FMT_MSA.3 ──────────────┘
                                                           │
FPT_STM.1 ──> FAU_GEN.1 ──> FAU_SAR.1                     │
                                                           ▼
FCS_CKM.1 ◄──> FCS_COP.1                          FDP_ACC.1 ◄──┘
```

### 4.2 Critical Paths

[TODO: Identify critical dependency paths]

**Critical Path 1: Access Control**
```
FIA_UID.1 → FMT_SMR.1 → FMT_MSA.1 → FDP_ACF.1 ↔ FDP_ACC.1
```

**Critical Path 2: Audit**
```
FPT_STM.1 → FAU_GEN.1 → FAU_SAR.1
```

## 5. Unsatisfied Dependencies

### 5.1 Overview

[TODO: If dependencies are not satisfied, document them here]

**Status:** [TODO: No unsatisfied dependencies / X unsatisfied dependencies]

### 5.2 Rationale for Unsatisfied Dependencies

[TODO: For each unsatisfied dependency, provide a detailed rationale]

**Example (if applicable):**
```
SFR: FCS_CKM.1
Dependency: FCS_CKM.2 or FCS_COP.1
Status: Partially satisfied (only FCS_COP.1)

Rationale: FCS_CKM.2 (Key distribution) is not required because the TOE does not 
perform key distribution to external entities. All keys are generated and used 
internally (FCS_COP.1).
```

## 6. Hierarchical Relationships

### 6.1 Use of Hierarchical Components

[TODO: Document if hierarchically higher SFR components are used]

According to ISO/IEC 15408-2, a hierarchically higher component automatically satisfies the dependencies of lower components.

**Example:**
```
If FDP_ACC.2 (Complete access control) is used, it automatically satisfies 
the dependency on FDP_ACC.1 (Subset access control).
```

## 7. Iterations

### 7.1 Iterated SFRs

[TODO: If SFRs are used multiple times (iteration), document the dependencies for each iteration]

| Iterated SFR | Iteration | Dependencies | Satisfaction |
|--------------|-----------|--------------|--------------|
| [TODO: e.g., FDP_ACC.1/1] | 1 | FDP_ACF.1/1 | ✓ |
| [TODO: e.g., FDP_ACC.1/2] | 2 | FDP_ACF.1/2 | ✓ |

## 8. Validation

### 8.1 Validation Checklist

- [ ] All SFRs are listed in the dependency table
- [ ] All dependencies are correctly identified according to ISO/IEC 15408-2
- [ ] All dependencies are satisfied or justified
- [ ] Hierarchical relationships are correctly considered
- [ ] Iterations are fully documented
- [ ] Dependency graph is consistent with the table

### 8.2 Peer Review

**Reviewer:** [TODO: Name]  
**Date:** [TODO: Date]  
**Status:** [TODO: Approved / Changes requested]  
**Comments:** [TODO: Comments]

## 9. References

- Document 0400: Security Requirements
- Document 0420: Requirements Rationale
- ISO/IEC 15408-2:2022 - Security functional requirements (Annex B: Dependencies)
- [TODO: Other relevant documents]

**Next Steps:**
1. Complete all [TODO] placeholders
2. Create complete dependency table
3. Verify all dependencies against ISO/IEC 15408-2
4. Create dependency graph
5. Conduct peer review
6. Update when SFRs change

