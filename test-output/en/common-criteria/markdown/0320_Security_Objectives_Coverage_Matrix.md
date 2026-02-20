# Security Objectives Coverage Matrix

**Document-ID:** 0320
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

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific TOE (Target of Evaluation).



## 1. Introduction

This document presents the Coverage Matrix for the security objectives of the TOE **{{ meta-handbook.toe_name }}**. The matrix visualizes the relationships between:

- Security objectives and threats
- Security objectives and organizational security policies (OSPs)
- Environment objectives and assumptions

### 1.1 Purpose

The Coverage Matrix serves as:
- **Completeness proof**: All elements of the security problem definition are covered
- **Traceability tool**: Quick identification of relationships
- **Audit documentation**: Evidence for evaluators and auditors
- **Change management**: Identification of impacts during changes

### 1.2 Legend

| Symbol | Meaning |
|--------|---------|
| X | Primary mapping - The objective directly addresses the threat/OSP/assumption |
| • | Supporting mapping - The objective indirectly supports |
| - | No mapping |

## 2. Threats vs. Security Objectives

The following matrix shows which security objectives address which threats:

| Threat | O.ACCESS_CONTROL | O.IDENTIFICATION_AUTHENTICATION | O.AUDIT_GENERATION | O.AUDIT_PROTECTION | O.DATA_CONFIDENTIALITY | O.CRYPTOGRAPHIC_OPERATIONS | O.DATA_INTEGRITY | O.SECURITY_MANAGEMENT | O.SECURE_STATE | O.TSF_PROTECTION | OE.PHYSICAL_PROTECTION | **[TODO]** |
|--------|------------------|--------------------------------|-------------------|-------------------|------------------------|---------------------------|------------------|----------------------|---------------|-----------------|----------------------|------------|
| **T.UNAUTHORIZED_ACCESS** | X | • | - | - | - | - | - | - | - | - | - | |
| **T.PRIVILEGE_ESCALATION** | X | • | - | - | - | - | - | - | - | - | - | |
| **T.MASQUERADE** | • | X | - | - | - | - | - | - | - | - | - | |
| **T.AUDIT_COMPROMISE** | - | - | X | X | - | - | - | - | - | - | - | |
| **T.DATA_DISCLOSURE** | • | - | - | - | X | X | - | - | - | - | - | |
| **T.EAVESDROPPING** | - | - | - | - | X | X | - | - | - | - | - | |
| **T.DATA_MODIFICATION** | • | - | - | - | - | X | X | - | - | - | - | |
| **T.DATA_CORRUPTION** | - | - | - | - | - | - | X | - | - | - | - | |
| **T.MALFUNCTION** | - | - | - | - | - | - | - | - | X | - | - | |
| **T.TSF_COMPROMISE** | - | - | - | - | - | - | - | - | - | X | - | |
| **T.TSF_BYPASS** | - | - | - | - | - | - | - | - | - | X | - | |
| **T.PHYSICAL_ATTACK** | - | - | - | - | - | - | - | - | - | - | X | |
| **[TODO: Additional threats]** | | | | | | | | | | | | |

**Analysis:**
- All threats are covered by at least one security objective ✓
- Multiple coverage shows Defense-in-Depth approach
- **[TODO: Add specific analyses for your TOE]**

## 3. Organizational Security Policies vs. Security Objectives

The following matrix shows which security objectives implement which OSPs:

| OSP | O.ACCESS_CONTROL | O.IDENTIFICATION_AUTHENTICATION | O.AUDIT_GENERATION | O.AUDIT_PROTECTION | O.DATA_CONFIDENTIALITY | O.CRYPTOGRAPHIC_OPERATIONS | O.DATA_INTEGRITY | O.SECURITY_MANAGEMENT | O.SECURE_STATE | O.TSF_PROTECTION | **[TODO]** |
|-----|------------------|--------------------------------|-------------------|-------------------|------------------------|---------------------------|------------------|----------------------|---------------|-----------------|------------|
| **P.ACCESS_CONTROL** | X | • | - | - | - | - | - | - | - | - | |
| **P.ACCOUNTABILITY** | - | - | X | X | - | - | - | - | - | - | |
| **P.CONFIDENTIALITY** | • | - | - | - | X | • | - | - | - | - | |
| **P.INTEGRITY** | • | - | - | - | - | • | X | - | - | - | |
| **P.MANAGEMENT** | - | - | - | - | - | - | - | X | - | - | |
| **[TODO: Additional OSPs]** | | | | | | | | | | | |

**Analysis:**
- All OSPs are implemented by at least one security objective ✓
- Clear mapping between policies and technical objectives
- **[TODO: Add specific analyses for your TOE]**

## 4. Assumptions vs. Environment Objectives

The following matrix shows which environment objectives fulfill which assumptions:

| Assumption | OE.PHYSICAL_PROTECTION | OE.TRUSTED_ADMIN | OE.USER_TRAINING | OE.NETWORK_PROTECTION | OE.EXTERNAL_SYSTEMS | OE.TIME_STAMPS | **[TODO]** |
|------------|----------------------|------------------|------------------|----------------------|---------------------|---------------|------------|
| **A.PHYSICAL_SECURITY** | X | - | - | - | - | - | |
| **A.TRUSTED_ADMIN** | - | X | - | - | - | - | |
| **A.USER_TRAINING** | - | - | X | - | - | - | |
| **A.NETWORK_SECURITY** | - | - | - | X | - | - | |
| **A.EXTERNAL_SYSTEMS** | - | - | - | - | X | - | |
| **A.TIME_SOURCE** | - | - | - | - | - | X | |
| **[TODO: Additional assumptions]** | | | | | | | |

**Analysis:**
- All assumptions are fulfilled by at least one environment objective ✓
- Clear separation between TOE and environment responsibilities
- **[TODO: Add specific analyses for your TOE]**

## 5. Reverse Traceability: Security Objectives to Security Problems

The following matrix shows the reverse perspective - which threats/OSPs/assumptions justify each security objective:

### 5.1 TOE Security Objectives

| Security Objective | Addressed Threats | Implemented OSPs | Justification |
|-------------------|-------------------|------------------|---------------|
| **O.ACCESS_CONTROL** | T.UNAUTHORIZED_ACCESS, T.PRIVILEGE_ESCALATION | P.ACCESS_CONTROL | Controls access to resources |
| **O.IDENTIFICATION_AUTHENTICATION** | T.MASQUERADE | - | Prevents identity impersonation |
| **O.AUDIT_GENERATION** | T.AUDIT_COMPROMISE | P.ACCOUNTABILITY | Records security-relevant events |
| **O.AUDIT_PROTECTION** | T.AUDIT_COMPROMISE | - | Protects audit data from tampering |
| **O.DATA_CONFIDENTIALITY** | T.DATA_DISCLOSURE, T.EAVESDROPPING | P.CONFIDENTIALITY | Protects sensitive data from disclosure |
| **O.CRYPTOGRAPHIC_OPERATIONS** | T.DATA_DISCLOSURE, T.DATA_MODIFICATION | - | Provides cryptographic mechanisms |
| **O.DATA_INTEGRITY** | T.DATA_MODIFICATION, T.DATA_CORRUPTION | P.INTEGRITY | Protects data integrity |
| **O.SECURITY_MANAGEMENT** | - | P.MANAGEMENT | Enables management of security functions |
| **O.SECURE_STATE** | T.MALFUNCTION | - | Ensures secure state during errors |
| **O.TSF_PROTECTION** | T.TSF_COMPROMISE, T.TSF_BYPASS | - | Protects security functions themselves |
| **[TODO: Additional objectives]** | | | |

**Result:** All TOE security objectives are justified by threats or OSPs ✓

### 5.2 Environment Objectives

| Environment Objective | Fulfilled Assumptions | Addressed Threats | Justification |
|----------------------|----------------------|-------------------|---------------|
| **OE.PHYSICAL_PROTECTION** | A.PHYSICAL_SECURITY | T.PHYSICAL_ATTACK | Protects TOE from physical access |
| **OE.TRUSTED_ADMIN** | A.TRUSTED_ADMIN | - | Ensures trustworthy administrators |
| **OE.USER_TRAINING** | A.USER_TRAINING | - | Trains users in secure usage |
| **OE.NETWORK_PROTECTION** | A.NETWORK_SECURITY | - | Protects TOE from network attacks |
| **OE.EXTERNAL_SYSTEMS** | A.EXTERNAL_SYSTEMS | - | Ensures security of external systems |
| **OE.TIME_STAMPS** | A.TIME_SOURCE | - | Provides reliable timestamps |
| **[TODO: Additional objectives]** | | | |

**Result:** All environment objectives are justified by assumptions ✓

## 6. Completeness Analysis

### 6.1 Threat Coverage

**Total number of threats:** 12 **[TODO: Update count]**  
**Covered threats:** 12 **[TODO: Update count]**  
**Uncovered threats:** 0 **[TODO: Update count]**

**Status:** ✓ Fully covered

**[TODO: List uncovered threats if any]**

### 6.2 OSP Coverage

**Total number of OSPs:** 5 **[TODO: Update count]**  
**Implemented OSPs:** 5 **[TODO: Update count]**  
**Unimplemented OSPs:** 0 **[TODO: Update count]**

**Status:** ✓ Fully implemented

**[TODO: List unimplemented OSPs if any]**

### 6.3 Assumption Coverage

**Total number of assumptions:** 6 **[TODO: Update count]**  
**Fulfilled assumptions:** 6 **[TODO: Update count]**  
**Unfulfilled assumptions:** 0 **[TODO: Update count]**

**Status:** ✓ Fully fulfilled

**[TODO: List unfulfilled assumptions if any]**

### 6.4 Objective Justification

**Total number of security objectives:** 16 **[TODO: Update count]**  
**Justified objectives:** 16 **[TODO: Update count]**  
**Unjustified objectives:** 0 **[TODO: Update count]**

**Status:** ✓ All objectives justified

**[TODO: List unjustified objectives if any]**

## 7. Gap Analysis

### 7.1 Identified Gaps

**[TODO: Document identified gaps in coverage]**

Example:
- **Gap 1:** Threat T.XXX is not covered by security objectives
  - **Impact:** [Description]
  - **Recommended Action:** Add security objective O.XXX
  
- **Gap 2:** Security objective O.YYY is not justified by threats/OSPs
  - **Impact:** [Description]
  - **Recommended Action:** Remove objective or identify justifying threat

**Current Status:** No gaps identified ✓

### 7.2 Redundancies and Overlaps

**[TODO: Document redundancies between security objectives]**

Example:
- **Overlap 1:** O.XXX and O.YYY both address T.ZZZ
  - **Analysis:** [Is this intentional? Defense-in-Depth?]
  - **Recommendation:** [Consolidate or maintain]

**Current Status:** Overlaps are intentional (Defense-in-Depth) ✓

## 8. Change Management

### 8.1 Impact Analysis for Changes

When changes are made to the security problem definition or security objectives, the Coverage Matrix must be updated:

**When adding a new threat:**
1. Add row in Matrix 2
2. Identify addressing security objectives
3. If no objectives exist: Create new security objective
4. Update completeness analysis

**When adding a new security objective:**
1. Add column in Matrix 2 and 3
2. Identify addressed threats/OSPs
3. If no threats/OSPs: Review necessity of objective
4. Update reverse traceability

**When removing a threat:**
1. Remove row from Matrix 2
2. Check if assigned security objectives are still justified
3. Update completeness analysis

**When removing a security objective:**
1. Remove column from matrices
2. Check if all threats/OSPs are still covered
3. If not: Identify alternative objective or create new objective

### 8.2 Change History

| Date | Change | Impact | Editor |
|------|--------|--------|--------|
| [Date] | Initial version | - | [TODO] |
| **[TODO]** | | | |

## 9. Summary

The Coverage Matrix demonstrates:

1. **Completeness:** ✓
   - All threats are covered by security objectives
   - All OSPs are implemented by security objectives
   - All assumptions are fulfilled by environment objectives

2. **Traceability:** ✓
   - All security objectives are justified by threats/OSPs
   - All environment objectives are justified by assumptions

3. **Consistency:** ✓
   - No gaps in coverage
   - No unjustified objectives

The security objectives form a complete and consistent foundation for deriving the security requirements (SFRs and SARs).

## 10. Next Steps

After the Coverage Matrix:
1. Derive security requirements (SFRs) from TOE security objectives (see Template 0400-0450)
2. Define security requirements for the environment based on environment objectives
3. Create rationale for security requirements

## 11. References

- ISO/IEC 15408-1: Security Target Evaluation
- ISO/IEC 15408-2: Security Functional Components
- Template 0200-0240: Security Problem Definition
- Template 0300: Security Objectives
- Template 0310: Security Objectives Rationale
- Template 0400-0450: Security Requirements

