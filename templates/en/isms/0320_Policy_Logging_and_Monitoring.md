# Policy: Logging and Monitoring

**Document-ID:** [FRAMEWORK]-0320
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
This policy establishes the principles for logging, monitoring, and security event management.
It ensures that security-relevant events are logged, monitored, and analyzed to detect
and respond to security incidents. Customize based on your organization's SIEM/SOC
capabilities and compliance requirements.

ISO 27001:2022 Annex A Reference: A.8.15, A.8.16
-->

**Document ID:** 0320  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.15, A.8.16 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This policy defines the principles for logging, monitoring, and security event management at **{{ meta-organisation.name }}**. It ensures that security-relevant events are captured, monitored, and analyzed to detect, investigate, and respond to security incidents.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Systems:** All IT systems, applications, network components, security systems
- **Log Sources:** Servers, workstations, network devices, firewalls, IDS/IPS, applications, databases
- **Monitoring Areas:** Security, performance, availability, compliance
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Comprehensive Logging
All security-relevant events are logged:
- Authentication attempts (successful and failed)
- Access to sensitive data and systems
- Privileged activities (admin access, configuration changes)
- Security incidents and anomalies
- System and application errors

### 3.2 Centralized Log Management
Logs are centrally collected, stored, and analyzed in a SIEM (Security Information and Event Management) system. This enables correlated analysis and efficient incident response.

### 3.3 Log Integrity and Protection
Logs are protected against unauthorized modification and deletion:
- Write-protected log storage
- Integrity checks (hashing, digital signatures)
- Access control to log systems
- Encrypted transmission

### 3.4 Retention and Preservation
Logs are retained according to legal, regulatory, and business requirements:
- Security logs: Minimum 12 months online, 7 years archive
- Audit logs: Per compliance requirements
- Performance logs: Per operational requirements

### 3.5 Proactive Monitoring and Alerting
Security-relevant events are proactively monitored and alerts are generated for anomalies:
- Real-time monitoring of critical systems
- Automated alerting rules
- Escalation processes for critical alerts
- 24/7 SOC (Security Operations Center) for critical systems

### 3.6 SIEM Use Cases and Detection Rules
SIEM systems are configured with use cases and detection rules to identify known attack patterns and anomalies:
- Brute-force attacks
- Privilege escalation
- Data exfiltration
- Malware activities
- Insider threats

### 3.7 Log Analysis and Forensics
Logs are regularly analyzed and used for forensic investigations during security incidents:
- Regular log reviews
- Threat hunting
- Incident investigation
- Root cause analysis

### 3.8 Data Protection Compliance
Logging and monitoring comply with data protection regulations (GDPR):
- Minimization of personal data in logs
- Purpose limitation of log data
- Access control to personal log data
- Deletion after retention period expiration

## 4. Roles and Responsibilities

### RACI Matrix: Logging and Monitoring

| Activity | CISO | SOC/Security Operations | IT Operations | System Owner | DPO |
|----------|------|-------------------------|---------------|--------------|-----|
| Policy Creation | R/A | C | C | C | C |
| SIEM Operations | A | R | C | I | I |
| Log Configuration | C | C | R | R | I |
| Monitoring and Alerting | A | R | C | I | I |
| Incident Investigation | A | R | C | C | C |
| Log Retention | C | C | R | I | C |
| Compliance Review | R/A | C | C | I | C |

**Legend:** R = Responsible (Execution), A = Accountable (Accountable), C = Consulted (Consulted), I = Informed (Informed)

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **SOC Manager:** {{ meta.security.soc_manager }}
- **SIEM Administrator:** {{ meta.it.siem_admin }}
- **Implementation Responsible:** SOC, IT operations, system owners
- **Control/Audit Function:** ISMS, internal audit, DPO

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0330_Richtlinie_Logging_SIEM_und_Audit_Trails.md** - Detailed implementation guideline
- `0400_Policy_Incident_Management.md` - Incident management policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Data protection policy
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Vulnerability management policy

### Related Standards/Baselines
- Log standards and formats
- SIEM use cases and detection rules
- Retention requirements
- Alerting thresholds

### Related Processes
- Log onboarding process
- Alert triage and escalation
- Incident investigation
- Log review process

## 6. Compliance, Monitoring, and Enforcement

### Metrics and KPIs
- Number of log sources in SIEM (target: 100% of critical systems)
- Log completeness and availability (target: 99.9%)
- Average time to alert triage (MTTD - Mean Time To Detect)
- Number of false positives per day
- SIEM use case coverage
- Compliance rate with retention requirements

### Evidence and Proof
- SIEM configuration and use cases
- Log retention evidence
- Alert statistics and triage reports
- Incident investigation reports
- Audit reports on logging and monitoring
- Data protection impact assessments

### Consequences for Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Deactivation of logging:** Immediate remediation, investigation
- **Unauthorized log manipulation:** Incident response, employment law consequences
- **Non-compliance with retention:** Remediation, retraining
- **Repeated violations:** Employment law consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO
- **Documentation:** All exceptions are documented in the risk register
- **Time Limit:** Exceptions are generally time-limited
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS policy
- `0330_Richtlinie_Logging_SIEM_und_Audit_Trails.md` - Detailed guideline
- `0400_Policy_Incident_Management.md` - Incident management policy
- `0080_ISMS_Risikoregister_Template.md` - Risk register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.8.15** - Logging
- **ISO/IEC 27001:2022 Annex A.8.16** - Monitoring activities
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-92** - Guide to Computer Security Log Management
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- **BSI IT-Grundschutz** - Module OPS.1.1.5 Logging

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

