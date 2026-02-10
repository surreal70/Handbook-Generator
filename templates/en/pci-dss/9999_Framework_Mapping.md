# PCI-DSS Framework Mapping

## Overview

This document maps PCI-DSS v4.0 requirements to the corresponding template files in this template set. It serves as a reference for compliance audits and to identify coverage gaps.

**PCI-DSS Version:** 4.0  
**Template Set Version:** 1.0  
**Last Updated:** 2026-02-06  
**Responsible:** Compliance Team  

## PCI-DSS Requirement Structure

PCI-DSS v4.0 is organized into 12 main requirements grouped into 6 objective areas:

### Objective 1: Build and Maintain a Secure Network and Systems
- Requirement 1: Install and Maintain Network Security Controls
- Requirement 2: Apply Secure Configurations to All System Components

### Objective 2: Protect Account Data
- Requirement 3: Protect Stored Account Data
- Requirement 4: Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks

### Objective 3: Maintain a Vulnerability Management Program
- Requirement 5: Protect All Systems and Networks from Malicious Software
- Requirement 6: Develop and Maintain Secure Systems and Software

### Objective 4: Implement Strong Access Control Measures
- Requirement 7: Restrict Access to System Components and Cardholder Data by Business Need to Know
- Requirement 8: Identify Users and Authenticate Access to System Components
- Requirement 9: Restrict Physical Access to Cardholder Data

### Objective 5: Regularly Monitor and Test Networks
- Requirement 10: Log and Monitor All Access to System Components and Cardholder Data
- Requirement 11: Test Security of Systems and Networks Regularly

### Objective 6: Maintain an Information Security Policy
- Requirement 12: Support Information Security with Organizational Policies and Programs

## Template Mapping by PCI-DSS Requirements

### Foundation Templates (0010-0050)

These templates form the foundation for the entire PCI-DSS compliance program:

| Template | Filename | PCI-DSS Requirements |
|----------|----------|---------------------|
| 0010 | Scope_and_CDE_Definition.md | All (Scope Definition) |
| 0020 | Network_Segmentation.md | Req 1, Req 2 |
| 0030 | Roles_and_Responsibilities.md | Req 12 |
| 0040 | Data_Flow_Diagrams.md | Req 1, Req 3, Req 4 |
| 0050 | Compliance_Program.md | Req 12 |


### Requirement 1: Install and Maintain Network Security Controls

**Objective:** Install and maintain network security controls to protect cardholder data.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 1.1 | Processes and mechanisms for network security controls | 0100 | Firewall_Configuration.md |
| 1.2 | Configure network security controls | 0100 | Firewall_Configuration.md |
| 1.3 | Restrict network access to and from the CDE | 0100, 0020 | Firewall_Configuration.md, Network_Segmentation.md |
| 1.4 | Restrict network connections between trusted and untrusted networks | 0100, 0020 | Firewall_Configuration.md, Network_Segmentation.md |
| 1.5 | Mitigate risks to the CDE from use of services, protocols, and ports | 0100 | Firewall_Configuration.md |

**Coverage:** Complete  
**Notes:** Templates cover firewall configuration, network segmentation, and access control.

### Requirement 2: Apply Secure Configurations to All System Components

**Objective:** Apply secure configurations to all system components.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 2.1 | Processes and mechanisms for secure configurations | - | **GAP** |
| 2.2 | Apply secure configurations to all system components | - | **GAP** |
| 2.3 | Secure wireless environments | - | **GAP** |

**Coverage:** Partial (via 0100 Firewall Configuration)  
**Notes:** **IDENTIFIED GAP** - Dedicated templates for system hardening and secure configurations are missing.

### Requirement 3: Protect Stored Account Data

**Objective:** Protect stored account data.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 3.1 | Processes and mechanisms for protecting stored account data | - | **GAP** |
| 3.2 | Minimize storage of account data after authorization | - | **GAP** |
| 3.3 | Do not store Sensitive Authentication Data (SAD) after authorization | - | **GAP** |
| 3.4 | Restrict access to displays of full PAN | 0400 | Access_Control.md |
| 3.5 | Render PAN unreadable wherever stored | - | **GAP** |
| 3.6 | Secure cryptographic keys used to protect stored account data | - | **GAP** |
| 3.7 | Manage cryptography for protection of stored account data | - | **GAP** |

**Coverage:** Minimal  
**Notes:** **IDENTIFIED GAP** - Templates for data encryption, key management, and data storage are missing.

### Requirement 4: Protect Cardholder Data with Strong Cryptography During Transmission

**Objective:** Protect cardholder data with strong cryptography during transmission.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 4.1 | Processes and mechanisms for protecting CHD during transmission | - | **GAP** |
| 4.2 | Protect PAN with strong cryptography during transmission over open, public networks | - | **GAP** |

**Coverage:** None  
**Notes:** **IDENTIFIED GAP** - Templates for encryption in transit are missing.

### Requirement 5: Protect All Systems and Networks from Malicious Software

**Objective:** Protect all systems and networks from malicious software.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 5.1 | Processes and mechanisms for protecting from malware | - | **GAP** |
| 5.2 | Implement malware protection on all systems | - | **GAP** |
| 5.3 | Keep anti-malware mechanisms and processes active | - | **GAP** |
| 5.4 | Implement anti-phishing mechanisms | - | **GAP** |

**Coverage:** None  
**Notes:** **IDENTIFIED GAP** - Templates for malware protection and anti-phishing are missing.

### Requirement 6: Develop and Maintain Secure Systems and Software

**Objective:** Develop and maintain secure systems and software.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 6.1 | Processes and mechanisms for secure systems and software | - | **GAP** |
| 6.2 | Protect bona fide software and applications from threats | - | **GAP** |
| 6.3 | Identify and address security vulnerabilities | - | **GAP** |
| 6.4 | Protect public-facing web applications from attacks | - | **GAP** |
| 6.5 | Securely manage changes to all system components | - | **GAP** |

**Coverage:** None  
**Notes:** **IDENTIFIED GAP** - Templates for secure development, vulnerability management, and change management are missing.


### Requirement 7: Restrict Access to System Components and Cardholder Data

**Objective:** Restrict access to system components and cardholder data by business need-to-know.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 7.1 | Processes and mechanisms for restricting access | 0400 | Access_Control.md |
| 7.2 | Establish access to system components and data by need-to-know | 0400 | Access_Control.md |
| 7.3 | Establish access to system components and data via applications and systems | 0400 | Access_Control.md |

**Coverage:** Complete  
**Notes:** Template 0400 covers RBAC, least privilege, need-to-know, and access management.

### Requirement 8: Identify Users and Authenticate Access to System Components

**Objective:** Identify users and authenticate access to system components.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 8.1 | Processes and mechanisms for user identification and authentication | 0410 | User_Authentication.md |
| 8.2 | Identify users before access to system components | 0410 | User_Authentication.md |
| 8.3 | Establish strong authentication for users | 0410 | User_Authentication.md |
| 8.4 | Implement multi-factor authentication (MFA) | 0410 | User_Authentication.md |
| 8.5 | Protect MFA systems from misuse | 0410 | User_Authentication.md |
| 8.6 | Manage use of application and system accounts | 0410 | User_Authentication.md |

**Coverage:** Complete  
**Notes:** Template 0410 covers authentication, MFA, password policies, and account management.

### Requirement 9: Restrict Physical Access to Cardholder Data

**Objective:** Restrict physical access to cardholder data.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 9.1 | Processes and mechanisms for restricting physical access | 0420 | Physical_Security.md |
| 9.2 | Restrict physical access to CDE | 0420 | Physical_Security.md |
| 9.3 | Control physical access for personnel and visitors | 0420 | Physical_Security.md |
| 9.4 | Secure media with cardholder data | 0420 | Physical_Security.md |
| 9.5 | Protect point-of-interaction (POI) devices from tampering | 0420 | Physical_Security.md |

**Coverage:** Complete  
**Notes:** Template 0420 covers physical access controls, visitor management, and media security.

### Requirement 10: Log and Monitor All Access to System Components and Cardholder Data

**Objective:** Log and monitor all access to system components and cardholder data.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 10.1 | Processes and mechanisms for logging and monitoring | 0500 | Logging_and_Monitoring.md |
| 10.2 | Implement audit logs to reconstruct user activities | 0500 | Logging_and_Monitoring.md |
| 10.3 | Protect audit logs from destruction and unauthorized changes | 0500 | Logging_and_Monitoring.md |
| 10.4 | Review audit logs to identify anomalies or suspicious activity | 0500 | Logging_and_Monitoring.md |
| 10.5 | Retain audit log history | 0500 | Logging_and_Monitoring.md |
| 10.6 | Detect and respond to security vulnerabilities and anomalies through security monitoring | 0500 | Logging_and_Monitoring.md |
| 10.7 | Detect and respond to failures of security systems in a timely manner | 0500 | Logging_and_Monitoring.md |

**Coverage:** Complete  
**Notes:** Template 0500 covers logging requirements, SIEM, log retention, monitoring, and alerting.

### Requirement 11: Test Security of Systems and Networks Regularly

**Objective:** Test security of systems and networks regularly.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 11.1 | Processes and mechanisms for regular security testing | 0510 | Network_Security_Testing.md |
| 11.2 | Identify and monitor wireless access points | 0510 | Network_Security_Testing.md |
| 11.3 | Identify and address external and internal vulnerabilities | 0510 | Network_Security_Testing.md |
| 11.4 | Perform external and internal penetration testing | 0510 | Network_Security_Testing.md |
| 11.5 | Detect and respond to network intrusions and manipulations | 0510 | Network_Security_Testing.md |
| 11.6 | Detect and respond to unauthorized changes to payment pages | 0510 | Network_Security_Testing.md |

**Coverage:** Complete  
**Notes:** Template 0510 covers vulnerability scanning, penetration testing, IDS/IPS, and change detection.

### Requirement 12: Support Information Security with Organizational Policies and Programs

**Objective:** Support information security with organizational policies and programs.

| Sub-Requirement | Description | Template | Filename |
|-----------------|-------------|----------|----------|
| 12.1 | Processes and mechanisms for information security policies | 0600 | Information_Security_Policy.md |
| 12.2 | Implement acceptable use policies | 0600 | Information_Security_Policy.md |
| 12.3 | Assess and manage risks to information assets | 0600 | Information_Security_Policy.md |
| 12.4 | Ensure PCI-DSS compliance through risk assessment of service providers | 0600 | Information_Security_Policy.md |
| 12.5 | Manage PCI-DSS requirements in business-as-usual (BAU) processes | 0050, 0600 | Compliance_Program.md, Information_Security_Policy.md |
| 12.6 | Maintain security awareness | 0600 | Information_Security_Policy.md |
| 12.7 | Screen personnel prior to hire and regularly | 0600 | Information_Security_Policy.md |
| 12.8 | Manage risk from service providers and other third parties | 0600 | Information_Security_Policy.md |
| 12.9 | Service providers acknowledge PCI-DSS requirements at least annually | 0600 | Information_Security_Policy.md |
| 12.10 | Document and communicate suspected and confirmed security incidents | 0600 | Information_Security_Policy.md |

**Coverage:** Complete  
**Notes:** Templates 0050 and 0600 cover policies, risk management, awareness, and incident response.

## Coverage Summary

### Fully Covered Requirements

| Requirement | Title | Primary Template(s) |
|-------------|-------|---------------------|
| 1 | Network Security Controls | 0100, 0020 |
| 7 | Access Control | 0400 |
| 8 | User Authentication | 0410 |
| 9 | Physical Security | 0420 |
| 10 | Logging and Monitoring | 0500 |
| 11 | Security Testing | 0510 |
| 12 | Information Security Policy | 0600, 0050 |

**Coverage Rate:** 7 out of 12 requirements (58%)


### Identified Coverage Gaps

The following PCI-DSS requirements are **not fully** covered by templates:

| Requirement | Title | Missing Templates | Priority |
|-------------|-------|-------------------|----------|
| 2 | Secure Configurations | System Hardening, Secure Configurations, Wireless Security | **HIGH** |
| 3 | Protect Stored Account Data | Data Encryption, Key Management, Data Storage, Data Retention | **CRITICAL** |
| 4 | Protect Data in Transit | Encryption in Transit, TLS Configuration | **CRITICAL** |
| 5 | Malware Protection | Anti-Malware, Anti-Phishing | **HIGH** |
| 6 | Secure Development | Secure SDLC, Vulnerability Management, Change Management, Patch Management | **HIGH** |

### Recommended Additional Templates

To achieve complete PCI-DSS compliance, the following templates should be created:

#### Requirement 2: Secure Configurations
- **0110_System_Hardening.md** - Secure system configurations and hardening standards
- **0120_Wireless_Security.md** - Wireless network security
- **0130_Default_Accounts_and_Passwords.md** - Management of default accounts and passwords

#### Requirement 3: Protect Stored Account Data
- **0200_Data_Storage_and_Retention.md** - Data storage and retention policies
- **0210_Data_Encryption.md** - Encryption of stored data
- **0220_Key_Management.md** - Cryptographic key management
- **0230_PAN_Masking.md** - PAN masking and display controls

#### Requirement 4: Protect Data in Transit
- **0240_Encryption_in_Transit.md** - Encryption during data transmission
- **0250_TLS_Configuration.md** - TLS/SSL configuration and management

#### Requirement 5: Malware Protection
- **0300_Anti_Malware.md** - Anti-malware protection and management
- **0310_Anti_Phishing.md** - Anti-phishing measures

#### Requirement 6: Secure Development
- **0320_Secure_SDLC.md** - Secure Software Development Lifecycle
- **0330_Vulnerability_Management.md** - Vulnerability management
- **0340_Patch_Management.md** - Patch management process
- **0350_Change_Management.md** - Change management
- **0360_Web_Application_Security.md** - Web application security (WAF, code reviews)

### Appendix Templates (0700-0750)

The following appendix templates are available:

| Template | Filename | Purpose |
|----------|----------|---------|
| 0700 | Appendix_Evidence_Register.md | Documentation of compliance evidence |
| 0710 | Appendix_Glossary.md | Terms and definitions |

**Recommended Additional Appendix Templates:**
- **0720_Appendix_Checklists.md** - Compliance checklists for all 12 requirements
- **0730_Appendix_Audit_Logs.md** - Examples of audit log formats
- **0740_Appendix_Forms.md** - Standard forms (access requests, change requests, etc.)
- **0750_Appendix_Contacts.md** - Emergency contacts and escalation paths

## Usage Guidelines

### For Compliance Audits

1. **Requirement Mapping:** Use this document to identify which templates are relevant for each PCI-DSS requirement.

2. **Gap Analysis:** Review the identified gaps and prioritize creation of missing templates.

3. **Evidence Collection:** Use template 0700 (Evidence Register) to document all compliance evidence.

4. **Audit Preparation:** Ensure all relevant templates are completed and current.

### For Template Customization

1. **Organization-Specific Customization:** Replace all `[TODO]` placeholders with organization-specific information.

2. **Placeholder Substitution:** Use the placeholder system (`{{ meta.* }}`) for automatic data insertion.

3. **Additional Sections:** Add additional sections as needed that are relevant to your organization.

4. **Version Control:** Document all changes in the document history at the end of each template.

### For Continuous Compliance

1. **Regular Reviews:** Review templates quarterly for currency.

2. **Change Management:** Update templates when processes or technologies change.

3. **PCI-DSS Updates:** Adapt templates when new PCI-DSS versions are released.

4. **Lessons Learned:** Integrate insights from audits and incidents into templates.

## References

- **PCI-DSS v4.0:** [PCI Security Standards Council](https://www.pcisecuritystandards.org/)
- **PCI-DSS v4.0 Summary of Changes:** Documents changes from v3.2.1 to v4.0
- **PCI-DSS v4.0 ROC Template:** Report on Compliance Template
- **PCI-DSS v4.0 SAQ:** Self-Assessment Questionnaires

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-06 | Compliance Team | Initial creation of framework mapping |

---

**Note:** This mapping document should be updated whenever templates change or when new PCI-DSS versions are released.

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
