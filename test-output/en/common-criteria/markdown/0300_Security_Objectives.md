# Security Objectives

**Document-ID:** COMMON-CRITERIA-0300
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

This document defines the security objectives for the TOE **{{ meta-handbook.toe_name }}** and its operational environment. The security objectives are derived from the security problem definition and describe the intended security properties required to counter identified threats, comply with organizational security policies, and fulfill assumptions.

### 1.1 Purpose

The security objectives serve as a bridge between:
- The security problem definition (threats, OSPs, assumptions)
- The security requirements (SFRs and SARs)

They describe **what** should be achieved, not **how** it will be implemented.

### 1.2 Structure

The security objectives are divided into two categories:
- **Security objectives for the TOE (O.xxx)**: Objectives achieved by the TOE itself
- **Security objectives for the environment (OE.xxx)**: Objectives that must be fulfilled by the operational environment

## 2. Security Objectives for the TOE



### 2.1 Access Control and Authentication

#### O.ACCESS_CONTROL
**Description:** The TOE must control access to protected resources based on user identity and permissions.

**Rationale:** This objective addresses the threats T.UNAUTHORIZED_ACCESS and T.PRIVILEGE_ESCALATION as well as the organizational security policy P.ACCESS_CONTROL.

**[TODO: Adapt the description to your specific TOE]**

#### O.IDENTIFICATION_AUTHENTICATION
**Description:** The TOE must uniquely identify and authenticate all users before granting access to protected functions.

**Rationale:** This objective addresses the threat T.MASQUERADE and supports O.ACCESS_CONTROL.

**[TODO: Add additional authentication objectives if required]**

### 2.2 Audit and Accountability

#### O.AUDIT_GENERATION
**Description:** The TOE must record security-relevant events, including user actions, security violations, and system events.

**Rationale:** This objective addresses the threat T.AUDIT_COMPROMISE and the organizational security policy P.ACCOUNTABILITY.

**[TODO: Define specific audit requirements]**

#### O.AUDIT_PROTECTION
**Description:** The TOE must protect audit records from unauthorized modification and deletion.

**Rationale:** This objective addresses the threat T.AUDIT_COMPROMISE and ensures the integrity of audit data.

**[TODO: Describe protection mechanisms for audit data]**

### 2.3 Data Protection and Confidentiality

#### O.DATA_CONFIDENTIALITY
**Description:** The TOE must protect sensitive user data from unauthorized disclosure.

**Rationale:** This objective addresses the threats T.DATA_DISCLOSURE and T.EAVESDROPPING as well as the organizational security policy P.CONFIDENTIALITY.

**[TODO: Define which data must be protected]**

#### O.CRYPTOGRAPHIC_OPERATIONS
**Description:** The TOE must perform cryptographic operations for encryption and integrity protection of data.

**Rationale:** This objective supports O.DATA_CONFIDENTIALITY and O.DATA_INTEGRITY by providing cryptographic mechanisms.

**[TODO: Specify required cryptographic functions]**

### 2.4 Data Integrity

#### O.DATA_INTEGRITY
**Description:** The TOE must protect the integrity of user data and system data against unauthorized modification.

**Rationale:** This objective addresses the threats T.DATA_MODIFICATION and T.DATA_CORRUPTION as well as the organizational security policy P.INTEGRITY.

**[TODO: Describe integrity protection mechanisms]**

### 2.5 Security Management

#### O.SECURITY_MANAGEMENT
**Description:** The TOE must enable authorized administrators to manage security functions and policies.

**Rationale:** This objective addresses the organizational security policy P.MANAGEMENT and enables configuration and maintenance of the TOE.

**[TODO: Define management functions]**

#### O.SECURE_STATE
**Description:** The TOE must start in a secure state and transition to a secure state upon errors.

**Rationale:** This objective addresses the threat T.MALFUNCTION and ensures that the TOE remains secure even during errors.

**[TODO: Describe secure states and error handling]**

### 2.6 Self-Protection

#### O.TSF_PROTECTION
**Description:** The TOE must protect its own security functions (TSF) from tampering and bypass.

**Rationale:** This objective addresses the threats T.TSF_COMPROMISE and T.TSF_BYPASS and ensures the integrity of security functions.

**[TODO: Describe TSF protection mechanisms]**

### 2.7 Additional TOE Security Objectives

**[TODO: Add additional specific security objectives for your TOE]**

#### O.[CUSTOM_OBJECTIVE_1]
**Description:** [TODO: Description]

**Rationale:** [TODO: Justification and reference to threats/OSPs]

#### O.[CUSTOM_OBJECTIVE_2]
**Description:** [TODO: Description]

**Rationale:** [TODO: Justification and reference to threats/OSPs]

## 3. Security Objectives for the Environment



### 3.1 Physical Security

#### OE.PHYSICAL_PROTECTION
**Description:** The operational environment must protect the TOE from physical access by unauthorized persons.

**Rationale:** This objective fulfills the assumption A.PHYSICAL_SECURITY and addresses the threat T.PHYSICAL_ATTACK.

**[TODO: Define required physical protection measures]**

### 3.2 Personnel and Trust

#### OE.TRUSTED_ADMIN
**Description:** The operational environment must ensure that administrators are trustworthy, trained, and competent.

**Rationale:** This objective fulfills the assumption A.TRUSTED_ADMIN and reduces the risk of insider threats.

**[TODO: Describe requirements for administrators]**

#### OE.USER_TRAINING
**Description:** The operational environment must ensure that users are trained in the secure use of the TOE.

**Rationale:** This objective fulfills the assumption A.USER_TRAINING and reduces the risk of user errors.

**[TODO: Define training requirements]**

### 3.3 Network and Connectivity

#### OE.NETWORK_PROTECTION
**Description:** The operational environment must protect the TOE from network attacks through firewalls, intrusion detection, and other protection mechanisms.

**Rationale:** This objective fulfills the assumption A.NETWORK_SECURITY and addresses threats from the network.

**[TODO: Specify required network protection measures]**

### 3.4 External Systems and Services

#### OE.EXTERNAL_SYSTEMS
**Description:** The operational environment must ensure that external systems with which the TOE interacts are trustworthy and secure.

**Rationale:** This objective fulfills the assumption A.EXTERNAL_SYSTEMS and reduces risks from third-party components.

**[TODO: Define requirements for external systems]**

### 3.5 Time Services

#### OE.TIME_STAMPS
**Description:** The operational environment must provide reliable timestamps for audit records and security events.

**Rationale:** This objective fulfills the assumption A.TIME_SOURCE and supports O.AUDIT_GENERATION.

**[TODO: Describe requirements for time sources]**

### 3.6 Additional Environment Objectives

**[TODO: Add additional specific security objectives for the environment]**

#### OE.[CUSTOM_ENV_OBJECTIVE_1]
**Description:** [TODO: Description]

**Rationale:** [TODO: Justification and reference to assumptions]

#### OE.[CUSTOM_ENV_OBJECTIVE_2]
**Description:** [TODO: Description]

**Rationale:** [TODO: Justification and reference to assumptions]

## 4. Summary of Security Objectives

### 4.1 TOE Security Objectives (Overview)

| Objective ID | Brief Description | Category |
|--------------|-------------------|----------|
| O.ACCESS_CONTROL | Access control to resources | Access Control |
| O.IDENTIFICATION_AUTHENTICATION | User identification and authentication | Access Control |
| O.AUDIT_GENERATION | Recording of security-relevant events | Audit |
| O.AUDIT_PROTECTION | Protection of audit records | Audit |
| O.DATA_CONFIDENTIALITY | Protection of sensitive data from disclosure | Data Protection |
| O.CRYPTOGRAPHIC_OPERATIONS | Cryptographic operations | Data Protection |
| O.DATA_INTEGRITY | Protection of data integrity | Integrity |
| O.SECURITY_MANAGEMENT | Management of security functions | Management |
| O.SECURE_STATE | Secure state at startup and errors | Self-Protection |
| O.TSF_PROTECTION | Protection of security functions | Self-Protection |
| **[TODO: Additional objectives]** | | |

### 4.2 Environment Objectives (Overview)

| Objective ID | Brief Description | Category |
|--------------|-------------------|----------|
| OE.PHYSICAL_PROTECTION | Physical protection of the TOE | Physical Security |
| OE.TRUSTED_ADMIN | Trustworthy administrators | Personnel |
| OE.USER_TRAINING | User training | Personnel |
| OE.NETWORK_PROTECTION | Network protection | Network |
| OE.EXTERNAL_SYSTEMS | Secure external systems | Integration |
| OE.TIME_STAMPS | Reliable timestamps | Infrastructure |
| **[TODO: Additional objectives]** | | |

## 5. Next Steps

After defining the security objectives:
1. Create the rationale (justification) for the security objectives (see Template 0310)
2. Create the Coverage Matrix (see Template 0320)
3. Derive the security requirements (SFRs and SARs) from the objectives

## 6. References

- ISO/IEC 15408-1: Security Target Evaluation
- ISO/IEC 15408-2: Security Functional Components
- ISO/IEC 15408-3: Security Assurance Components
- Template 0200-0240: Security Problem Definition
- Template 0310: Security Objectives Rationale
- Template 0320: Security Objectives Coverage Matrix

