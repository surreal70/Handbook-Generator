# Assumptions

**Document-ID:** 0230
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents assumptions about the operational environment according to ISO/IEC 15408-1:2022.
Assumptions describe expectations about the physical, personnel, and technical environment
in which the TOE is operated.

Customization required:
- Identify all assumptions about the operational environment
- Document each assumption with rationale and impact
- Define responsibilities for fulfilling assumptions
- Describe verification methods
- Assess criticality of each assumption

Reference: ISO/IEC 15408-1:2022, Section 8.3.3 (Assumptions)
-->

## 1. Assumptions Overview

### 1.1 Purpose
Assumptions define expectations about the TOE's operational environment:
- **Physical Environment**: Assumptions about physical security and infrastructure
- **Personnel**: Assumptions about users, administrators, and their behavior
- **Connectivity**: Assumptions about network and communication infrastructure
- **Technical Environment**: Assumptions about IT infrastructure and platforms

### 1.2 Assumption Categories
**Assumption Categories:**
- **Physical Assumptions**: Physical security assumptions
- **Personnel Assumptions**: Personnel assumptions
- **Connectivity Assumptions**: Connectivity assumptions
- **Platform Assumptions**: Platform assumptions
- **Operational Assumptions**: Operational assumptions

### 1.3 Assumption Scope
**In Scope:**
[TODO: Which aspects of the environment are covered by assumptions?]

**Out of Scope:**
[TODO: Which aspects are not covered by assumptions?]

## 2. Physical Assumptions

### A.PHYSICAL_SECURITY
**Assumption ID:** A.PHYSICAL_SECURITY  
**Category:** Physical  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: The TOE is operated in a physically secure environment protected from unauthorized physical access]

**Rationale:**
[TODO: Physical security is required to prevent hardware tampering and direct system access]

**Requirements:**
- [TODO: Access control to server rooms]
- [TODO: Video surveillance of critical areas]
- [TODO: Alarm system for unauthorized access]
- [TODO: Secure storage of backup media]
- [TODO: Visitor log and escort requirement]

**Impact if Not Met:**
[TODO: Describe security risks if this assumption is not met]
- Risk: [TODO: e.g., Hardware tampering, theft]
- Affected Assets: [TODO: A.001, A.002]
- Affected Threats: [TODO: T.001, T.003]

**Responsibility:**
- **Primary:** [TODO: Facility Management]
- **Secondary:** [TODO: Security Team]

**Verification:**
[TODO: How is it verified that this assumption is met?]
- Method: [TODO: e.g., Physical inspection, audit]
- Frequency: [TODO: e.g., Annually, Quarterly]
- Documentation: [TODO: e.g., Audit report, checklist]

### A.ENVIRONMENTAL_PROTECTION
**Assumption ID:** A.ENVIRONMENTAL_PROTECTION  
**Category:** Physical  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: The TOE is operated in an environment protected from environmental hazards]

**Rationale:**
[TODO: Protection from fire, water, temperature, humidity is required for availability]

**Requirements:**
- [TODO: Air conditioning and temperature control]
- [TODO: Fire detection and suppression system]
- [TODO: Water protection and leak detection]
- [TODO: Uninterruptible Power Supply (UPS)]
- [TODO: Emergency power supply]

[TODO: Add more Physical Assumptions]

## 3. Personnel Assumptions

### A.TRUSTED_ADMIN
**Assumption ID:** A.TRUSTED_ADMIN  
**Category:** Personnel  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: Administrators are trustworthy, competent, and do not act maliciously]

**Rationale:**
[TODO: Administrators have privileged access and can bypass security mechanisms]

**Requirements:**
- [TODO: Background checks before hiring]
- [TODO: Signing of confidentiality agreements]
- [TODO: Regular security training]
- [TODO: Four-eyes principle for critical operations]
- [TODO: Monitoring of administrative activities]
- [TODO: Regular review of administrator rights]

**Impact if Not Met:**
[TODO: Describe security risks]
- Risk: [TODO: e.g., Insider threat, sabotage, data theft]
- Affected Assets: [TODO: All assets]
- Affected Threats: [TODO: T.002, T.004, T.006]

**Responsibility:**
- **Primary:** [TODO: HR Department]
- **Secondary:** [TODO: Security Team, IT Management]

**Verification:**
[TODO: How is it verified that this assumption is met?]
- Method: [TODO: e.g., Background checks, audit log review]
- Frequency: [TODO: e.g., At hiring, annually]
- Documentation: [TODO: e.g., HR file, training records]

### A.USER_TRAINING
**Assumption ID:** A.USER_TRAINING  
**Category:** Personnel  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: Users are trained and follow security policies]

**Rationale:**
[TODO: Users must understand and correctly use security mechanisms]

**Requirements:**
- [TODO: Security training before system access]
- [TODO: Regular refresher training]
- [TODO: Phishing awareness training]
- [TODO: Training on password policies]
- [TODO: Training on data classification]
- [TODO: Incident reporting training]

[TODO: Add more Personnel Assumptions]

## 4. Connectivity Assumptions

### A.NETWORK_SECURITY
**Assumption ID:** A.NETWORK_SECURITY  
**Category:** Connectivity  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: The network in which the TOE operates is protected by firewalls and other security mechanisms]

**Rationale:**
[TODO: Network security is required to defend against external attacks]

**Requirements:**
- [TODO: Firewall between TOE and Internet]
- [TODO: Network segmentation]
- [TODO: Intrusion Detection/Prevention System (IDS/IPS)]
- [TODO: Regular network scans]
- [TODO: VPN for remote access]
- [TODO: DDoS protection]

**Impact if Not Met:**
[TODO: Describe security risks]
- Risk: [TODO: e.g., Network attacks, data exfiltration]
- Affected Assets: [TODO: A.003, A.004]
- Affected Threats: [TODO: T.005, T.007]

**Responsibility:**
- **Primary:** [TODO: Network Team]
- **Secondary:** [TODO: Security Team]

**Verification:**
[TODO: How is it verified that this assumption is met?]
- Method: [TODO: e.g., Network audit, penetration test]
- Frequency: [TODO: e.g., Quarterly]
- Documentation: [TODO: e.g., Network diagram, firewall rules]

### A.SECURE_COMMUNICATION
**Assumption ID:** A.SECURE_COMMUNICATION  
**Category:** Connectivity  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: Communication channels between TOE and external systems are encrypted]

**Rationale:**
[TODO: Encryption protects against eavesdropping and man-in-the-middle attacks]

**Requirements:**
- [TODO: TLS 1.2 or higher for all connections]
- [TODO: Certificate validation]
- [TODO: Secure cipher suites]
- [TODO: Regular certificate renewal]

[TODO: Add more Connectivity Assumptions]

## 5. Platform Assumptions

### A.TRUSTED_PLATFORM
**Assumption ID:** A.TRUSTED_PLATFORM  
**Category:** Platform  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: The platform on which the TOE runs is trustworthy and securely configured]

**Rationale:**
[TODO: TOE security depends on the security of the underlying platform]

**Requirements:**
- [TODO: Current and patched operating system]
- [TODO: Hardening according to best practices (e.g., CIS Benchmarks)]
- [TODO: Disabling of unnecessary services]
- [TODO: Host-based firewall]
- [TODO: Antivirus/Endpoint Protection]
- [TODO: Regular vulnerability scans]

**Impact if Not Met:**
[TODO: Describe security risks]
- Risk: [TODO: e.g., Platform compromise, privilege escalation]
- Affected Assets: [TODO: All assets]
- Affected Threats: [TODO: T.008, T.009]

**Responsibility:**
- **Primary:** [TODO: System Administration]
- **Secondary:** [TODO: Security Team]

**Verification:**
[TODO: How is it verified that this assumption is met?]
- Method: [TODO: e.g., Configuration audit, vulnerability scan]
- Frequency: [TODO: e.g., Monthly]
- Documentation: [TODO: e.g., Scan reports, configuration documentation]

### A.PLATFORM_AVAILABILITY
**Assumption ID:** A.PLATFORM_AVAILABILITY  
**Category:** Platform  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: The platform provides sufficient resources and availability for TOE operation]

**Rationale:**
[TODO: TOE requires sufficient resources for proper operation]

**Requirements:**
- [TODO: Sufficient CPU capacity]
- [TODO: Sufficient memory]
- [TODO: Sufficient storage space]
- [TODO: High availability architecture (if required)]
- [TODO: Regular capacity planning]

[TODO: Add more Platform Assumptions]

## 6. Operational Assumptions

### A.SECURITY_MONITORING
**Assumption ID:** A.SECURITY_MONITORING  
**Category:** Operational  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: Security events are continuously monitored and analyzed]

**Rationale:**
[TODO: Early detection of security incidents is critical]

**Requirements:**
- [TODO: 24/7 Security Operations Center (SOC)]
- [TODO: SIEM system for log aggregation and analysis]
- [TODO: Automatic alerting for critical events]
- [TODO: Defined incident response processes]
- [TODO: Regular review of security events]

**Impact if Not Met:**
[TODO: Describe security risks]
- Risk: [TODO: e.g., Delayed detection of attacks]
- Affected Assets: [TODO: All assets]
- Affected Threats: [TODO: All threats]

**Responsibility:**
- **Primary:** [TODO: Security Operations Team]
- **Secondary:** [TODO: IT Operations]

**Verification:**
[TODO: How is it verified that this assumption is met?]
- Method: [TODO: e.g., SOC audit, incident response test]
- Frequency: [TODO: e.g., Quarterly]
- Documentation: [TODO: e.g., SOC reports, incident logs]

### A.BACKUP_RECOVERY
**Assumption ID:** A.BACKUP_RECOVERY  
**Category:** Operational  
**Criticality:** [TODO: High/Medium/Low]  
**Mandatory:** [TODO: Yes/No]

**Description:**
[TODO: Regular backups are created and recovery processes are tested]

**Rationale:**
[TODO: Backups are required for disaster recovery and business continuity]

**Requirements:**
- [TODO: Daily incremental backups]
- [TODO: Weekly full backups]
- [TODO: Offsite storage of backups]
- [TODO: Encryption of backup data]
- [TODO: Regular recovery tests]
- [TODO: Documented recovery procedures]

[TODO: Add more Operational Assumptions]

## 7. Assumption Summary

### 7.1 Assumption Statistics
**Assumption Statistics:**
- Total number of assumptions: [TODO: Number]
- Physical Assumptions: [TODO: Number]
- Personnel Assumptions: [TODO: Number]
- Connectivity Assumptions: [TODO: Number]
- Platform Assumptions: [TODO: Number]
- Operational Assumptions: [TODO: Number]

### 7.2 Criticality Distribution
**Criticality Distribution:**
- High Criticality: [TODO: Number] ([TODO: %])
- Medium Criticality: [TODO: Number] ([TODO: %])
- Low Criticality: [TODO: Number] ([TODO: %])

### 7.3 Mandatory vs. Optional
**Mandatory vs. Optional Assumptions:**
- Mandatory: [TODO: Number] ([TODO: %])
- Optional: [TODO: Number] ([TODO: %])

## 8. Assumption Validation

### 8.1 Validation Methods
**Validation Methods:**

| Assumption ID | Validation Method | Frequency | Responsible Party |
|---------------|------------------|-----------|-------------------|
| [TODO: A.001] | [TODO: Method] | [TODO: Frequency] | [TODO: Responsible] |
| [TODO: A.002] | [TODO: Method] | [TODO: Frequency] | [TODO: Responsible] |

### 8.2 Validation Schedule
**Validation Schedule:**
- [TODO: Monthly]: [TODO: A.001, A.003]
- [TODO: Quarterly]: [TODO: A.002, A.004, A.005]
- [TODO: Annually]: [TODO: A.006, A.007]

### 8.3 Validation Documentation
**Validation Documentation:**
[TODO: Describe how validation results are documented]

## 9. Responsibility Matrix

### 9.1 Primary Responsibilities
**Primary Responsibilities:**

| Organization Unit | Assumptions | Count |
|-------------------|-------------|-------|
| [TODO: Facility Management] | [TODO: A.001, A.002] | [TODO: 2] |
| [TODO: HR Department] | [TODO: A.003, A.004] | [TODO: 2] |
| [TODO: Network Team] | [TODO: A.005, A.006] | [TODO: 2] |
| [TODO: System Administration] | [TODO: A.007, A.008] | [TODO: 2] |
| [TODO: Security Operations] | [TODO: A.009, A.010] | [TODO: 2] |

### 9.2 Shared Responsibilities
**Shared Responsibilities:**
[TODO: Describe assumptions with shared responsibilities]

## 10. Traceability

### 10.1 Assumption-to-Threat Mapping
**Mapping Assumptions to Threats:**

| Assumption ID | Mitigates Threats | Rationale |
|---------------|------------------|-----------|
| [TODO: A.001] | [TODO: T.001, T.003] | [TODO: Rationale] |
| [TODO: A.002] | [TODO: T.002, T.005] | [TODO: Rationale] |

### 10.2 Assumption-to-Asset Mapping
**Mapping Assumptions to Assets:**

| Assumption ID | Protects Assets | Protection Type |
|---------------|----------------|-----------------|
| [TODO: A.001] | [TODO: A.001, A.002] | [TODO: Physical Protection] |
| [TODO: A.002] | [TODO: A.003] | [TODO: Availability] |

### 10.3 Assumption-to-OSP Mapping
**Mapping Assumptions to OSPs:**

| Assumption ID | Supports OSPs | Relationship |
|---------------|--------------|--------------|
| [TODO: A.001] | [TODO: P.001, P.003] | [TODO: Enables enforcement] |
| [TODO: A.002] | [TODO: P.002] | [TODO: Prerequisite] |

**Next Steps:**
1. Complete all [TODO] placeholders with environment-specific assumptions
2. Document all relevant assumptions
3. Define validation methods
4. Assign responsibilities
5. Create validation schedule
6. Verify consistency with Threats (Template 0210), OSPs (Template 0220), and Security Objectives (Template 0300)

