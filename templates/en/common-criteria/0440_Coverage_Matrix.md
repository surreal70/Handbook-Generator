# Coverage Matrix

**Document-ID:** 0440
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

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific Target of Evaluation (TOE).

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
This template provides comprehensive coverage matrices that demonstrate traceability
between all elements of the Security Target: Threats, OSPs, Assumptions, Security
Objectives, and Security Requirements.

Key considerations:
- Complete traceability must be demonstrated in both directions
- Every threat must be addressed by at least one security objective
- Every security objective must be addressed by at least one SFR
- Gaps in coverage must be identified and justified
- The matrices support audit and certification processes
-->

## 1. Introduction

This document provides comprehensive coverage matrices that demonstrate traceability between all elements of the Security Target:

- Threats
- Organizational Security Policies (OSPs)
- Assumptions
- Security Objectives
- Security Requirements

The matrices ensure complete coverage and consistency of the Security Target.

## 2. Threats → Security Objectives

### 2.1 Threat Coverage Matrix

This matrix shows how each identified threat is addressed by security objectives.

<!-- TODO: Create complete matrix -->

| Threat | Description | Addressing Security Objectives | Coverage |
|--------|-------------|-------------------------------|----------|
| T.UNAUTH_ACCESS | Unauthorized access to TOE functions | O.ACCESS, O.IDENTIFY, O.AUTHENTICATE | ✓ Complete |
| T.DATA_DISCLOSURE | Unauthorized disclosure of data | O.CRYPTO, O.ACCESS | ✓ Complete |
| T.DATA_MANIPULATION | Unauthorized manipulation of data | O.INTEGRITY, O.ACCESS, O.AUDIT | ✓ Complete |
| T.MASQUERADE | Identity spoofing | O.AUTHENTICATE, O.IDENTIFY | ✓ Complete |
| T.AUDIT_COMPROMISE | Compromise of audit data | O.AUDIT, O.PROTECT_TSF | ✓ Complete |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 2.2 Completeness Analysis

**Statistics:**
- Number of identified threats: [TODO: X]
- Number of fully addressed threats: [TODO: X]
- Number of partially addressed threats: [TODO: 0]
- Number of unaddressed threats: [TODO: 0]

**Status:** [TODO: ✓ All threats addressed / ⚠ Gaps present]

### 2.3 Unaddressed Threats

[TODO: If threats are not fully addressed, justify this]

**Example (if applicable):**
```
Threat: T.PHYSICAL_ATTACK
Status: Not addressed by TOE
Rationale: Physical attacks are addressed by environmental assumptions 
(A.PHYSICAL_PROTECTION) and organizational measures, not by TOE functionality.
```

## 3. OSPs → Security Objectives

### 3.1 OSP Coverage Matrix

This matrix shows how organizational security policies are implemented through security objectives.

<!-- TODO: Create complete matrix -->

| OSP | Description | Addressing Security Objectives | Coverage |
|-----|-------------|-------------------------------|----------|
| P.ACCOUNTABILITY | User actions must be traceable | O.AUDIT, O.IDENTIFY | ✓ Complete |
| P.AUTHORIZED_USERS | Only authorized users may access TOE | O.ACCESS, O.AUTHENTICATE | ✓ Complete |
| P.CRYPTOGRAPHY | Sensitive data must be encrypted | O.CRYPTO | ✓ Complete |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 3.2 Completeness Analysis

**Statistics:**
- Number of defined OSPs: [TODO: X]
- Number of fully implemented OSPs: [TODO: X]
- Number of partially implemented OSPs: [TODO: 0]
- Number of unimplemented OSPs: [TODO: 0]

**Status:** [TODO: ✓ All OSPs implemented / ⚠ Gaps present]

## 4. Assumptions → Security Objectives for the Environment

### 4.1 Assumption Coverage Matrix

This matrix shows how assumptions are addressed by security objectives for the environment.

<!-- TODO: Create complete matrix -->

| Assumption | Description | Addressing Environmental Objectives | Coverage |
|------------|-------------|-------------------------------------|----------|
| A.PHYSICAL_PROTECTION | TOE is physically protected | OE.PHYSICAL | ✓ Complete |
| A.TRUSTED_ADMIN | Administrators are trustworthy | OE.ADMIN_TRAINING, OE.ADMIN_VETTING | ✓ Complete |
| A.NETWORK_PROTECTION | Network is protected against external attacks | OE.NETWORK_SECURITY | ✓ Complete |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 4.2 Completeness Analysis

**Statistics:**
- Number of defined assumptions: [TODO: X]
- Number of fully addressed assumptions: [TODO: X]
- Number of partially addressed assumptions: [TODO: 0]
- Number of unaddressed assumptions: [TODO: 0]

**Status:** [TODO: ✓ All assumptions addressed / ⚠ Gaps present]

## 5. Security Objectives for TOE → SFRs

### 5.1 Security Objectives to SFRs Matrix

This matrix shows how security objectives for the TOE are fulfilled by Security Functional Requirements.

<!-- TODO: Create complete matrix -->

| Security Objective | Description | Fulfilling SFRs | Coverage |
|-------------------|-------------|-----------------|----------|
| O.ACCESS | Access control to TOE resources | FDP_ACC.1, FDP_ACF.1, FMT_MSA.1, FMT_MSA.3 | ✓ Complete |
| O.IDENTIFY | Identification of users | FIA_UID.1 | ✓ Complete |
| O.AUTHENTICATE | Authentication of users | FIA_UAU.1, FIA_AFL.1 | ✓ Complete |
| O.AUDIT | Audit recording of security-relevant events | FAU_GEN.1, FAU_SAR.1, FPT_STM.1 | ✓ Complete |
| O.CRYPTO | Cryptographic protection of sensitive data | FCS_CKM.1, FCS_COP.1 | ✓ Complete |
| O.INTEGRITY | Protection of data integrity | FDP_SDI.1, FPT_TST.1 | ✓ Complete |
| O.PROTECT_TSF | Protection of TSF functionality | FPT_STM.1, FPT_TST.1 | ✓ Complete |
| O.MANAGE | Secure management of TOE | FMT_SMF.1, FMT_SMR.1, FMT_MOF.1 | ✓ Complete |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 5.2 Completeness Analysis

**Statistics:**
- Number of security objectives for TOE: [TODO: X]
- Number of fully fulfilled objectives: [TODO: X]
- Number of partially fulfilled objectives: [TODO: 0]
- Number of unfulfilled objectives: [TODO: 0]

**Status:** [TODO: ✓ All objectives fulfilled / ⚠ Gaps present]

### 5.3 Unfulfilled Security Objectives

[TODO: If security objectives are not fully fulfilled by SFRs, justify this]

## 6. Reverse Traceability: SFRs → Security Objectives

### 6.1 SFRs to Security Objectives Matrix

This matrix shows reverse traceability: Each SFR must fulfill at least one security objective.

<!-- TODO: Create complete matrix -->

| SFR | Fulfilled Security Objectives | Necessity |
|-----|------------------------------|-----------|
| FAU_GEN.1 | O.AUDIT | ✓ Necessary |
| FAU_SAR.1 | O.AUDIT | ✓ Necessary |
| FCS_CKM.1 | O.CRYPTO | ✓ Necessary |
| FCS_COP.1 | O.CRYPTO | ✓ Necessary |
| FDP_ACC.1 | O.ACCESS | ✓ Necessary |
| FDP_ACF.1 | O.ACCESS | ✓ Necessary |
| FDP_SDI.1 | O.INTEGRITY | ✓ Necessary |
| FIA_AFL.1 | O.AUTHENTICATE | ✓ Necessary |
| FIA_UAU.1 | O.AUTHENTICATE | ✓ Necessary |
| FIA_UID.1 | O.IDENTIFY | ✓ Necessary |
| FMT_MOF.1 | O.MANAGE | ✓ Necessary |
| FMT_MSA.1 | O.ACCESS, O.MANAGE | ✓ Necessary |
| FMT_MSA.3 | O.ACCESS | ✓ Necessary |
| FMT_SMF.1 | O.MANAGE | ✓ Necessary |
| FMT_SMR.1 | O.MANAGE | ✓ Necessary |
| FPT_STM.1 | O.AUDIT, O.PROTECT_TSF | ✓ Necessary |
| FPT_TST.1 | O.INTEGRITY, O.PROTECT_TSF | ✓ Necessary |
| [TODO] | [TODO] | [TODO] |

### 6.2 Superfluous SFRs

[TODO: Identify SFRs that do not fulfill any security objective (should be none)]

**Status:** [TODO: ✓ No superfluous SFRs / ⚠ Superfluous SFRs identified]

## 7. Complete Traceability Matrix

### 7.1 End-to-End Traceability

This matrix shows complete traceability from threats to SFRs.

<!-- TODO: Create complete end-to-end matrix -->

| Threat/OSP/Assumption | Security Objective | SFR | Rationale |
|-----------------------|-------------------|-----|-----------|
| T.UNAUTH_ACCESS | O.ACCESS | FDP_ACC.1, FDP_ACF.1 | Access control prevents unauthorized access |
| T.UNAUTH_ACCESS | O.IDENTIFY | FIA_UID.1 | Identification required before access |
| T.UNAUTH_ACCESS | O.AUTHENTICATE | FIA_UAU.1 | Authentication verifies identity |
| T.DATA_DISCLOSURE | O.CRYPTO | FCS_COP.1 | Encryption protects against disclosure |
| T.DATA_DISCLOSURE | O.ACCESS | FDP_ACC.1 | Access control limits data access |
| T.DATA_MANIPULATION | O.INTEGRITY | FDP_SDI.1 | Integrity checking detects manipulation |
| T.DATA_MANIPULATION | O.ACCESS | FDP_ACC.1 | Access control prevents unauthorized changes |
| T.DATA_MANIPULATION | O.AUDIT | FAU_GEN.1 | Audit recording documents changes |
| [TODO] | [TODO] | [TODO] | [TODO] |

## 8. Coverage Gaps Analysis

### 8.1 Identified Gaps

[TODO: Identify and document gaps in coverage]

**Gap Types:**
- Threats without security objectives
- Security objectives without SFRs
- SFRs without security objectives
- OSPs without implementation

**Status:** [TODO: ✓ No gaps / ⚠ X gaps identified]

### 8.2 Rationale for Gaps

[TODO: For each identified gap, provide a rationale]

**Example (if applicable):**
```
Gap: Threat T.PHYSICAL_ATTACK has no TOE security objective
Rationale: Physical threats are addressed by environmental assumptions and objectives,
not by TOE functionality. See A.PHYSICAL_PROTECTION and OE.PHYSICAL.
```

## 9. Visualization

### 9.1 Traceability Diagram

[TODO: Create a diagram that visualizes traceability]

```
Example (as text):

Threats              Security Objectives      SFRs
─────────────        ─────────────────        ────────────
T.UNAUTH_ACCESS ───┬─> O.ACCESS ──────────┬─> FDP_ACC.1
                   │                      └─> FDP_ACF.1
                   ├─> O.IDENTIFY ─────────> FIA_UID.1
                   └─> O.AUTHENTICATE ────> FIA_UAU.1

T.DATA_DISCLOSURE ─┬─> O.CRYPTO ──────────┬─> FCS_CKM.1
                   │                      └─> FCS_COP.1
                   └─> O.ACCESS ──────────> FDP_ACC.1

T.DATA_MANIPULATION┬─> O.INTEGRITY ───────> FDP_SDI.1
                   ├─> O.ACCESS ──────────> FDP_ACC.1
                   └─> O.AUDIT ───────────┬─> FAU_GEN.1
                                          └─> FPT_STM.1
```

## 10. Validation and Maintenance

### 10.1 Validation Checklist

- [ ] All threats are addressed by security objectives
- [ ] All OSPs are implemented by security objectives
- [ ] All assumptions are addressed by environmental objectives
- [ ] All security objectives for TOE are fulfilled by SFRs
- [ ] All SFRs fulfill at least one security objective
- [ ] No gaps in coverage (or justified)
- [ ] Traceability is bidirectionally complete

### 10.2 Maintenance Notes

**When Changes Occur:**
- New threat → Add security objective → Add SFR
- New SFR → Assign to security objective → Assign to threat/OSP
- Removed threat → Check if security objective still needed
- Removed SFR → Check if security objective still fulfilled

**Update Frequency:**
- With every change to threats, objectives, or requirements
- Before each review milestone
- Before submission for evaluation

## 11. Summary

### 11.1 Coverage Summary

**Completeness:**
- ✓ All threats addressed: [TODO: X/X]
- ✓ All OSPs implemented: [TODO: X/X]
- ✓ All assumptions addressed: [TODO: X/X]
- ✓ All security objectives fulfilled: [TODO: X/X]
- ✓ All SFRs necessary: [TODO: X/X]

**Overall Status:** [TODO: ✓ Complete / ⚠ Gaps present]

### 11.2 Audit Readiness

[TODO: Confirm readiness for audit]

The coverage matrices demonstrate complete and consistent traceability between all elements of the Security Target. The TOE is ready for evaluation.

## 12. References

- Document 0200: Security Problem Definition
- Document 0300: Security Objectives
- Document 0400: Security Requirements
- Document 0420: Requirements Rationale
- Document 0430: SFR Dependencies
- ISO/IEC 15408-1:2022 - Introduction and general model
- ISO/IEC 15408-2:2022 - Security functional requirements
- ISO/IEC 15408-3:2022 - Security assurance requirements

**Next Steps:**
1. Complete all [TODO] placeholders
2. Create complete coverage matrices
3. Identify and justify gaps
4. Create traceability diagram
5. Conduct peer review
6. Keep matrices updated when changes occur

