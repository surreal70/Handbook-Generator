# Organizational Security Policies (OSPs)

**Document-ID:** 0220
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents organizational security policies (OSPs) according to ISO/IEC 15408-1:2022.
OSPs are security rules, practices, or policies imposed by the organization
that the TOE must enforce or support.

Customization required:
- Identify all relevant organizational security policies
- Document each policy with purpose and requirements
- Map policies to external standards and regulations
- Define compliance requirements
- Describe enforcement mechanisms

Reference: ISO/IEC 15408-1:2022, Section 8.3.2 (Organizational Security Policies)
-->

## 1. OSP Overview

### 1.1 Purpose
Organizational Security Policies (OSPs) define security rules and practices that:
- Are mandated by the organization
- Must be enforced or supported by the TOE
- Apply independently of specific threats
- Fulfill compliance requirements

### 1.2 OSP Categories
**Policy Categories:**
- **Access Control Policies**: Access control policies
- **Audit Policies**: Audit and logging policies
- **Cryptographic Policies**: Cryptography policies
- **Data Protection Policies**: Data protection policies
- **Authentication Policies**: Authentication policies
- **Configuration Policies**: Configuration policies
- **Operational Policies**: Operational policies

### 1.3 Policy Scope
**In Scope:**
[TODO: Which policies are enforced by the TOE?]

**Out of Scope:**
[TODO: Which policies are not enforced by the TOE?]

## 2. Access Control Policies

### P.ACCESS_CONTROL
**Policy ID:** P.ACCESS_CONTROL  
**Category:** Access Control  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: The TOE must implement access control mechanisms that ensure only authorized users can access protected resources]

**Purpose:**
[TODO: Protection against unauthorized access to sensitive data and functions]

**Requirements:**
- [TODO: Implementation of Role-Based Access Control (RBAC)]
- [TODO: Enforcement of Least-Privilege principle]
- [TODO: Regular review of access rights]
- [TODO: Documentation of all access decisions]

**Scope:**
[TODO: All users and administrators of the TOE]

**Enforcement:**
- **TOE Responsibility:** [TODO: Implement access control mechanisms]
- **Environment Responsibility:** [TODO: Define and assign user roles]

**Compliance Requirements:**
- ISO 27001: A.9.1, A.9.2, A.9.4
- NIST 800-53: AC-2, AC-3, AC-6
- [TODO: Additional standards]

**Verification:**
[TODO: How is compliance with this policy verified?]

### P.NEED_TO_KNOW
**Policy ID:** P.NEED_TO_KNOW  
**Category:** Access Control  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Access to information may only be granted when there is a legitimate need]

[TODO: Add more Access Control Policies]

## 3. Audit Policies

### P.AUDIT_LOGGING
**Policy ID:** P.AUDIT_LOGGING  
**Category:** Audit  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: The TOE must log all security-relevant events and protect audit logs from unauthorized modification]

**Purpose:**
[TODO: Traceability of actions and support for forensic analysis]

**Requirements:**
- [TODO: Logging of all authentication attempts]
- [TODO: Logging of all accesses to sensitive data]
- [TODO: Logging of all administrative actions]
- [TODO: Protection of audit logs from tampering]
- [TODO: Regular review of audit logs]
- [TODO: Retention of logs for [TODO: period]]

**Scope:**
[TODO: All users and system components]

**Enforcement:**
- **TOE Responsibility:** [TODO: Implement audit mechanisms]
- **Environment Responsibility:** [TODO: Provide and monitor log storage]

**Compliance Requirements:**
- ISO 27001: A.12.4
- NIST 800-53: AU-2, AU-3, AU-9
- [TODO: Additional standards]

**Verification:**
[TODO: How is compliance with this policy verified?]

### P.AUDIT_REVIEW
**Policy ID:** P.AUDIT_REVIEW  
**Category:** Audit  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Audit logs must be regularly reviewed to detect security incidents]

[TODO: Add more Audit Policies]

## 4. Cryptographic Policies

### P.CRYPTOGRAPHY
**Policy ID:** P.CRYPTOGRAPHY  
**Category:** Cryptographic  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: The TOE must use cryptographic mechanisms to ensure confidentiality and integrity]

**Purpose:**
[TODO: Protection of sensitive data through encryption]

**Requirements:**
- [TODO: Use of approved cryptographic algorithms]
- [TODO: Minimum key lengths: AES-256, RSA-2048, etc.]
- [TODO: Secure key management and storage]
- [TODO: Regular key rotation]
- [TODO: Use of TLS 1.2 or higher for communication]
- [TODO: Use of FIPS 140-2 validated crypto modules]

**Scope:**
[TODO: All encrypted data and communication channels]

**Enforcement:**
- **TOE Responsibility:** [TODO: Implement cryptographic functions]
- **Environment Responsibility:** [TODO: Manage cryptographic keys]

**Compliance Requirements:**
- ISO 27001: A.10.1
- NIST 800-53: SC-12, SC-13
- FIPS 140-2
- [TODO: Additional standards]

**Verification:**
[TODO: How is compliance with this policy verified?]

### P.KEY_MANAGEMENT
**Policy ID:** P.KEY_MANAGEMENT  
**Category:** Cryptographic  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Cryptographic keys must be securely generated, stored, and managed]

[TODO: Add more Cryptographic Policies]

## 5. Data Protection Policies

### P.DATA_CLASSIFICATION
**Policy ID:** P.DATA_CLASSIFICATION  
**Category:** Data Protection  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: All data must be classified and protected according to its classification]

**Purpose:**
[TODO: Appropriate protection of data based on its sensitivity]

**Requirements:**
- [TODO: Classification scheme: Public, Internal, Confidential, Restricted]
- [TODO: Labeling of all data with classification]
- [TODO: Protection measures according to classification]
- [TODO: Regular review of classification]

**Scope:**
[TODO: All data processed in the TOE]

**Enforcement:**
- **TOE Responsibility:** [TODO: Classification-based access control]
- **Environment Responsibility:** [TODO: Perform data classification]

**Compliance Requirements:**
- ISO 27001: A.8.2
- GDPR: Article 32
- [TODO: Additional standards]

**Verification:**
[TODO: How is compliance with this policy verified?]

### P.DATA_RETENTION
**Policy ID:** P.DATA_RETENTION  
**Category:** Data Protection  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Data must be stored and deleted according to retention policies]

[TODO: Add more Data Protection Policies]

## 6. Authentication Policies

### P.STRONG_AUTHENTICATION
**Policy ID:** P.STRONG_AUTHENTICATION  
**Category:** Authentication  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: The TOE must implement strong authentication mechanisms]

**Purpose:**
[TODO: Ensuring user identity]

**Requirements:**
- [TODO: Multi-Factor Authentication (MFA) for privileged accounts]
- [TODO: Password policies: minimum length, complexity, expiration]
- [TODO: Account lockout after failed login attempts]
- [TODO: Secure storage of authentication data (hashing)]
- [TODO: Session timeout after inactivity]

**Scope:**
[TODO: All users of the TOE]

**Enforcement:**
- **TOE Responsibility:** [TODO: Implement authentication mechanisms]
- **Environment Responsibility:** [TODO: Train and monitor users]

**Compliance Requirements:**
- ISO 27001: A.9.4
- NIST 800-53: IA-2, IA-5
- [TODO: Additional standards]

**Verification:**
[TODO: How is compliance with this policy verified?]

### P.PASSWORD_POLICY
**Policy ID:** P.PASSWORD_POLICY  
**Category:** Authentication  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Passwords must meet certain complexity and security requirements]

[TODO: Add more Authentication Policies]

## 7. Configuration Policies

### P.SECURE_CONFIGURATION
**Policy ID:** P.SECURE_CONFIGURATION  
**Category:** Configuration  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: The TOE must be operated in a secure configuration]

**Purpose:**
[TODO: Minimizing attack surface through secure configuration]

**Requirements:**
- [TODO: Disabling of unnecessary services and functions]
- [TODO: Use of secure default settings]
- [TODO: Regular review of configuration]
- [TODO: Documentation of all configuration changes]
- [TODO: Change management process for configuration changes]

**Scope:**
[TODO: All TOE components]

**Enforcement:**
- **TOE Responsibility:** [TODO: Provide secure default configuration]
- **Environment Responsibility:** [TODO: Monitor and manage configuration]

**Compliance Requirements:**
- ISO 27001: A.12.6
- NIST 800-53: CM-6, CM-7
- CIS Controls
- [TODO: Additional standards]

**Verification:**
[TODO: How is compliance with this policy verified?]

### P.CONFIGURATION_MANAGEMENT
**Policy ID:** P.CONFIGURATION_MANAGEMENT  
**Category:** Configuration  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Configuration changes must be controlled and documented]

[TODO: Add more Configuration Policies]

## 8. Operational Policies

### P.SECURITY_UPDATES
**Policy ID:** P.SECURITY_UPDATES  
**Category:** Operational  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Security updates must be installed promptly]

**Purpose:**
[TODO: Protection against known vulnerabilities]

**Requirements:**
- [TODO: Regular checking for available updates]
- [TODO: Assessment and prioritization of updates]
- [TODO: Timely installation of critical security updates]
- [TODO: Testing of updates before production installation]
- [TODO: Documentation of all installed updates]

**Scope:**
[TODO: All TOE components]

**Enforcement:**
- **TOE Responsibility:** [TODO: Provide update mechanism]
- **Environment Responsibility:** [TODO: Install and manage updates]

**Compliance Requirements:**
- ISO 27001: A.12.6.1
- NIST 800-53: SI-2
- [TODO: Additional standards]

**Verification:**
[TODO: How is compliance with this policy verified?]

### P.BACKUP_RECOVERY
**Policy ID:** P.BACKUP_RECOVERY  
**Category:** Operational  
**Mandatory:** [TODO: Yes/No]  
**Priority:** [TODO: High/Medium/Low]

**Description:**
[TODO: Regular backups must be created and tested]

[TODO: Add more Operational Policies]

## 9. Policy Compliance Matrix

### 9.1 Standards Mapping
**Mapping to External Standards:**

| OSP ID | ISO 27001 | NIST 800-53 | PCI-DSS | GDPR | HIPAA | SOC 2 |
|--------|-----------|-------------|---------|------|-------|-------|
| [TODO: P.001] | [TODO: A.9.1] | [TODO: AC-2] | [TODO: 7.1] | [TODO: Art. 32] | [TODO: §164.312] | [TODO: CC6.1] |
| [TODO: P.002] | [TODO: A.12.4] | [TODO: AU-2] | [TODO: 10.1] | [TODO: Art. 30] | [TODO: §164.312] | [TODO: CC7.2] |

### 9.2 Regulatory Compliance
**Regulatory Requirements:**

| Regulation | Applicable OSPs | Compliance Status |
|------------|----------------|-------------------|
| [TODO: GDPR] | [TODO: P.001, P.003, P.005] | [TODO: Compliant/Partial/Non-Compliant] |
| [TODO: HIPAA] | [TODO: P.002, P.004] | [TODO: Compliant/Partial/Non-Compliant] |
| [TODO: PCI-DSS] | [TODO: P.001, P.002, P.006] | [TODO: Compliant/Partial/Non-Compliant] |

### 9.3 Industry Standards
**Industry Standards:**

| Standard | Applicable OSPs | Compliance Status |
|----------|----------------|-------------------|
| [TODO: ISO 27001] | [TODO: All OSPs] | [TODO: Compliant/Partial/Non-Compliant] |
| [TODO: NIST 800-53] | [TODO: P.001-P.010] | [TODO: Compliant/Partial/Non-Compliant] |
| [TODO: CIS Controls] | [TODO: P.003, P.007] | [TODO: Compliant/Partial/Non-Compliant] |

## 10. Policy Summary

### 10.1 Policy Statistics
**Policy Statistics:**
- Total number of OSPs: [TODO: Number]
- Mandatory policies: [TODO: Number]
- Optional policies: [TODO: Number]
- Access Control Policies: [TODO: Number]
- Audit Policies: [TODO: Number]
- Cryptographic Policies: [TODO: Number]
- Data Protection Policies: [TODO: Number]
- Authentication Policies: [TODO: Number]
- Configuration Policies: [TODO: Number]
- Operational Policies: [TODO: Number]

### 10.2 Enforcement Responsibility
**Enforcement Responsibility:**

| Responsibility | Number of OSPs | OSP IDs |
|----------------|----------------|---------|
| **TOE Only** | [TODO: Number] | [TODO: P.001, P.003] |
| **Environment Only** | [TODO: Number] | [TODO: P.005] |
| **Shared (TOE + Environment)** | [TODO: Number] | [TODO: P.002, P.004] |

### 10.3 Priority Distribution
**Priority Distribution:**
- High Priority: [TODO: Number] ([TODO: %])
- Medium Priority: [TODO: Number] ([TODO: %])
- Low Priority: [TODO: Number] ([TODO: %])

## 11. Traceability

### 11.1 OSP-to-Threat Mapping
**Mapping OSPs to Threats:**

| OSP ID | Addresses Threats | Rationale |
|--------|------------------|-----------|
| [TODO: P.001] | [TODO: T.001, T.003] | [TODO: Rationale] |
| [TODO: P.002] | [TODO: T.002, T.005] | [TODO: Rationale] |

### 11.2 OSP-to-Asset Mapping
**Mapping OSPs to Assets:**

| OSP ID | Protects Assets | Protection Type |
|--------|----------------|-----------------|
| [TODO: P.001] | [TODO: A.001, A.002] | [TODO: Confidentiality/Integrity/Availability] |
| [TODO: P.002] | [TODO: A.003] | [TODO: Integrity] |

**Next Steps:**
1. Complete all [TODO] placeholders with organization-specific policies
2. Document all relevant OSPs
3. Map OSPs to external standards
4. Define enforcement mechanisms
5. Create compliance matrix
6. Verify consistency with Threats (Template 0210) and Security Objectives (Template 0300)

