# Security Objectives Summary

**Document-ID:** COMMON-CRITERIA-0330
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

This document provides a compact summary of all security objectives for the TOE **{{ meta-handbook.toe_name }}** and its operational environment. The security objectives describe the intended security properties required to counter identified threats, comply with organizational security policies, and fulfill assumptions.

### 1.1 Purpose

This summary serves as:
- **Quick reference** for all security objectives
- **Executive summary** for management decisions
- **Communication tool** for stakeholders
- **Audit documentation** for evaluators

### 1.2 Document Structure

- Section 2: Overview of TOE security objectives
- Section 3: Overview of environment objectives
- Section 4: Categorization by security domains
- Section 5: Coverage statistics
- Section 6: Graphical representations

## 2. TOE Security Objectives (Overview)

The following security objectives are fulfilled by the TOE itself:

| ID | Objective | Brief Description | Category | Priority |
|----|-----------|-------------------|----------|----------|
| **O.ACCESS_CONTROL** | Access Control | Controls access to protected resources based on user identity and permissions | Access Control | High |
| **O.IDENTIFICATION_AUTHENTICATION** | Identification & Authentication | Identifies and authenticates all users before granting access to protected functions | Access Control | High |
| **O.AUDIT_GENERATION** | Audit Recording | Records security-relevant events | Audit & Accountability | High |
| **O.AUDIT_PROTECTION** | Audit Protection | Protects audit records from unauthorized modification and deletion | Audit & Accountability | High |
| **O.DATA_CONFIDENTIALITY** | Data Confidentiality | Protects sensitive user data from unauthorized disclosure | Data Protection | High |
| **O.CRYPTOGRAPHIC_OPERATIONS** | Cryptographic Operations | Performs cryptographic operations for encryption and integrity protection | Data Protection | Medium |
| **O.DATA_INTEGRITY** | Data Integrity | Protects data integrity against unauthorized modification | Integrity | High |
| **O.SECURITY_MANAGEMENT** | Security Management | Enables authorized administrators to manage security functions | Management | Medium |
| **O.SECURE_STATE** | Secure State | Starts in secure state and transitions to secure state upon errors | Self-Protection | High |
| **O.TSF_PROTECTION** | TSF Protection | Protects own security functions from tampering and bypass | Self-Protection | High |
| **[TODO]** | | | | |

**Total TOE Security Objectives:** 10 **[TODO: Update count]**

### 2.1 Categorization of TOE Security Objectives

**Access Control (2 objectives):**
- O.ACCESS_CONTROL
- O.IDENTIFICATION_AUTHENTICATION

**Audit & Accountability (2 objectives):**
- O.AUDIT_GENERATION
- O.AUDIT_PROTECTION

**Data Protection (2 objectives):**
- O.DATA_CONFIDENTIALITY
- O.CRYPTOGRAPHIC_OPERATIONS

**Integrity (1 objective):**
- O.DATA_INTEGRITY

**Management (1 objective):**
- O.SECURITY_MANAGEMENT

**Self-Protection (2 objectives):**
- O.SECURE_STATE
- O.TSF_PROTECTION

**[TODO: Add additional categories]**

## 3. Environment Objectives (Overview)

The following security objectives must be fulfilled by the operational environment:

| ID | Objective | Brief Description | Category | Responsible |
|----|-----------|-------------------|----------|-------------|
| **OE.PHYSICAL_PROTECTION** | Physical Protection | Protects TOE from physical access by unauthorized persons | Physical Security | Operator |
| **OE.TRUSTED_ADMIN** | Trustworthy Administrators | Ensures that administrators are trustworthy, trained, and competent | Personnel | Organization |
| **OE.USER_TRAINING** | User Training | Ensures that users are trained in secure use of the TOE | Personnel | Organization |
| **OE.NETWORK_PROTECTION** | Network Protection | Protects TOE from network attacks through firewalls and other mechanisms | Network | IT Department |
| **OE.EXTERNAL_SYSTEMS** | Secure External Systems | Ensures that external systems are trustworthy and secure | Integration | IT Department |
| **OE.TIME_STAMPS** | Reliable Timestamps | Provides reliable timestamps for audit records | Infrastructure | IT Department |
| **[TODO]** | | | | |

**Total Environment Objectives:** 6 **[TODO: Update count]**

### 3.1 Categorization of Environment Objectives

**Physical Security (1 objective):**
- OE.PHYSICAL_PROTECTION

**Personnel (2 objectives):**
- OE.TRUSTED_ADMIN
- OE.USER_TRAINING

**Network (1 objective):**
- OE.NETWORK_PROTECTION

**Integration (1 objective):**
- OE.EXTERNAL_SYSTEMS

**Infrastructure (1 objective):**
- OE.TIME_STAMPS

**[TODO: Add additional categories]**

## 4. Security Objectives by Security Domains

### 4.1 Access Control and Authentication

**TOE Objectives:**
- O.ACCESS_CONTROL: Access control to resources
- O.IDENTIFICATION_AUTHENTICATION: User identification and authentication

**Environment Objectives:**
- OE.TRUSTED_ADMIN: Trustworthy administrators

**Summary:** The TOE implements technical access control and authentication mechanisms, while the environment provides trustworthy administrators.

### 4.2 Audit and Accountability

**TOE Objectives:**
- O.AUDIT_GENERATION: Recording of security-relevant events
- O.AUDIT_PROTECTION: Protection of audit records

**Environment Objectives:**
- OE.TIME_STAMPS: Reliable timestamps

**Summary:** The TOE records events and protects audit data, while the environment provides reliable timestamps.

### 4.3 Data Protection and Confidentiality

**TOE Objectives:**
- O.DATA_CONFIDENTIALITY: Protection of sensitive data from disclosure
- O.CRYPTOGRAPHIC_OPERATIONS: Cryptographic operations

**Environment Objectives:**
- OE.NETWORK_PROTECTION: Network protection

**Summary:** The TOE protects data through access control and encryption, while the environment provides network protection.

### 4.4 Data Integrity

**TOE Objectives:**
- O.DATA_INTEGRITY: Protection of data integrity
- O.CRYPTOGRAPHIC_OPERATIONS: Cryptographic integrity protection

**Environment Objectives:**
- No direct environment objectives

**Summary:** The TOE is primarily responsible for integrity protection.

### 4.5 Security Management

**TOE Objectives:**
- O.SECURITY_MANAGEMENT: Management of security functions

**Environment Objectives:**
- OE.TRUSTED_ADMIN: Trustworthy administrators
- OE.USER_TRAINING: User training

**Summary:** The TOE provides management functions, while the environment provides trained personnel.

### 4.6 Self-Protection and Availability

**TOE Objectives:**
- O.SECURE_STATE: Secure state at startup and errors
- O.TSF_PROTECTION: Protection of security functions

**Environment Objectives:**
- OE.PHYSICAL_PROTECTION: Physical protection
- OE.EXTERNAL_SYSTEMS: Secure external systems

**Summary:** The TOE protects itself, while the environment provides physical protection and secure integration.

**[TODO: Add additional security domains]**

## 5. Coverage Statistics

### 5.1 Threat Coverage

| Category | Count | Covered by TOE Objectives | Covered by Environment Objectives |
|----------|-------|---------------------------|----------------------------------|
| Access Control | 3 | 3 | 0 |
| Data Disclosure | 2 | 2 | 0 |
| Data Manipulation | 2 | 2 | 0 |
| Audit Compromise | 1 | 1 | 0 |
| System Failure | 1 | 1 | 0 |
| TSF Compromise | 2 | 2 | 0 |
| Physical Attacks | 1 | 0 | 1 |
| **Total** | **12** | **11** | **1** |

**[TODO: Update statistics based on your threats]**

### 5.2 OSP Coverage

| OSP | Implementing TOE Objectives | Status |
|-----|----------------------------|--------|
| P.ACCESS_CONTROL | O.ACCESS_CONTROL | ✓ Implemented |
| P.ACCOUNTABILITY | O.AUDIT_GENERATION, O.AUDIT_PROTECTION | ✓ Implemented |
| P.CONFIDENTIALITY | O.DATA_CONFIDENTIALITY | ✓ Implemented |
| P.INTEGRITY | O.DATA_INTEGRITY | ✓ Implemented |
| P.MANAGEMENT | O.SECURITY_MANAGEMENT | ✓ Implemented |
| **[TODO]** | | |

**Total OSPs:** 5 **[TODO: Update count]**  
**Implemented OSPs:** 5 (100%)

### 5.3 Assumption Coverage

| Assumption | Fulfilling Environment Objective | Status |
|------------|--------------------------------|--------|
| A.PHYSICAL_SECURITY | OE.PHYSICAL_PROTECTION | ✓ Fulfilled |
| A.TRUSTED_ADMIN | OE.TRUSTED_ADMIN | ✓ Fulfilled |
| A.USER_TRAINING | OE.USER_TRAINING | ✓ Fulfilled |
| A.NETWORK_SECURITY | OE.NETWORK_PROTECTION | ✓ Fulfilled |
| A.EXTERNAL_SYSTEMS | OE.EXTERNAL_SYSTEMS | ✓ Fulfilled |
| A.TIME_SOURCE | OE.TIME_STAMPS | ✓ Fulfilled |
| **[TODO]** | | |

**Total Assumptions:** 6 **[TODO: Update count]**  
**Fulfilled Assumptions:** 6 (100%)

### 5.4 Completeness Assessment

| Criterion | Status | Percentage |
|-----------|--------|------------|
| All threats covered | ✓ Yes | 100% |
| All OSPs implemented | ✓ Yes | 100% |
| All assumptions fulfilled | ✓ Yes | 100% |
| All objectives justified | ✓ Yes | 100% |

**Overall Assessment:** ✓ Complete and consistent

## 6. Graphical Representations

### 6.1 Distribution of TOE Security Objectives by Category

```
Access Control:           ██████████ (20%)
Audit & Accountability:   ██████████ (20%)
Data Protection:          ██████████ (20%)
Integrity:                █████ (10%)
Management:               █████ (10%)
Self-Protection:          ██████████ (20%)
```

**[TODO: Create diagram with actual values]**

### 6.2 Distribution of Environment Objectives by Responsibility

```
Operator (Physical):      ████████████████ (17%)
Organization (Personnel): ████████████████████████████████ (33%)
IT Department (Technical):██████████████████████████████████████████████████ (50%)
```

**[TODO: Create diagram with actual values]**

### 6.3 Relationship Diagram (simplified)

```
Threats (12)  ──────▶  TOE Objectives (10)  ──────▶  SFRs
                                                       (next step)
OSPs (5)      ──────▶  TOE Objectives (10)  ──────▶

Assumptions (6) ─────▶  Environment Objectives (6) ─▶  Environment
                                                       Requirements
```

**[TODO: Create detailed diagram]**

## 7. Priorities and Dependencies

### 7.1 High-Priority Security Objectives

The following security objectives have highest priority and must be implemented first:

1. **O.TSF_PROTECTION** - Fundamental for all other objectives
2. **O.ACCESS_CONTROL** - Basis for access control
3. **O.IDENTIFICATION_AUTHENTICATION** - Prerequisite for access control
4. **O.DATA_CONFIDENTIALITY** - Protection of sensitive data
5. **O.DATA_INTEGRITY** - Protection of data integrity
6. **O.AUDIT_GENERATION** - Accountability
7. **O.SECURE_STATE** - Secure operation

**[TODO: Adapt priorities to your TOE]**

### 7.2 Dependencies Between Security Objectives

| Objective | Depends On | Justification |
|-----------|-----------|---------------|
| O.ACCESS_CONTROL | O.IDENTIFICATION_AUTHENTICATION | Access control requires authentication |
| O.AUDIT_GENERATION | OE.TIME_STAMPS | Audit records need timestamps |
| O.DATA_CONFIDENTIALITY | O.ACCESS_CONTROL | Confidentiality requires access control |
| O.DATA_INTEGRITY | O.ACCESS_CONTROL | Integrity requires access control |
| O.SECURITY_MANAGEMENT | OE.TRUSTED_ADMIN | Management requires trustworthy admins |
| **[TODO]** | | |

## 8. Summary and Assessment

### 8.1 Strengths of Security Objectives

1. **Complete Coverage:** All threats, OSPs, and assumptions are addressed
2. **Clear Separation:** TOE and environment responsibilities are clearly defined
3. **Defense-in-Depth:** Multiple protection layers through overlapping objectives
4. **Traceability:** All objectives are justified by security problems
5. **Balance:** Good balance between different security domains

**[TODO: Add specific strengths for your TOE]**

### 8.2 Potential Challenges

1. **Complexity:** Many security objectives require careful implementation
2. **Dependencies:** Some objectives depend on each other
3. **Environment Requirements:** Success depends on correct environment configuration

**[TODO: Identify specific challenges for your TOE]**

### 8.3 Recommendations

1. Prioritize implementation of high-priority objectives
2. Consider dependencies in implementation planning
3. Ensure environment requirements are achievable
4. Document implementation decisions for evaluators

**[TODO: Add specific recommendations]**

## 9. Next Steps

After the summary of security objectives:

1. **Derive Security Requirements** (Template 0400-0450)
   - Derive Security Functional Requirements (SFRs) from TOE objectives
   - Define Security Assurance Requirements (SARs)
   - Select Evaluation Assurance Level (EAL)

2. **Create Rationale for Requirements**
   - Show how SFRs fulfill security objectives
   - Document SFR dependencies

3. **Develop TOE Summary Specification**
   - Describe how the TOE implements the SFRs

## 10. References

- ISO/IEC 15408-1: Security Target Evaluation
- ISO/IEC 15408-2: Security Functional Components
- ISO/IEC 15408-3: Security Assurance Components
- Template 0200-0240: Security Problem Definition
- Template 0300: Security Objectives
- Template 0310: Security Objectives Rationale
- Template 0320: Security Objectives Coverage Matrix
- Template 0400-0450: Security Requirements

