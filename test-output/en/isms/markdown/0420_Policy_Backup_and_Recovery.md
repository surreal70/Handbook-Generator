# Policy: Backup and Recovery



**Document ID:** 0420  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.13 (incl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the principles for backup and recovery at **AdminSend GmbH**. It ensures that critical data and systems can be restored in case of data loss, corruption, or disasters.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Systems:** All IT systems, databases, applications, file systems, VMs, cloud resources
- **Data:** All business-critical and personal data
- **Backup Types:** Full, incremental, differential, snapshot, cloud backup
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Backup Strategy Based on RPO/RTO
Backup strategies are defined based on Recovery Point Objective (RPO) and Recovery Time Objective (RTO):
- **Critical Systems:** RPO < 1 hour, RTO < 4 hours
- **Important Systems:** RPO < 24 hours, RTO < 24 hours
- **Standard Systems:** RPO < 7 days, RTO < 72 hours

### 3.2 3-2-1 Backup Rule
Backups follow the 3-2-1 rule:
- **3** copies of data (original + 2 backups)
- **2** different storage media/technologies
- **1** copy offsite/offline (air-gapped or geographically separated)

### 3.3 Encrypted Backups
All backups are stored encrypted (at rest) and transmitted encrypted (in transit). Encryption keys are securely managed and stored separately from backups.

### 3.4 Regular Backup Tests
Backups are regularly tested to ensure recoverability:
- **Critical Systems:** Monthly restore tests
- **Important Systems:** Quarterly restore tests
- **Standard Systems:** Annual restore tests

### 3.5 Immutable Backups
Critical backups are stored as immutable to provide protection against ransomware and accidental deletion.

### 3.6 Backup Monitoring and Alerting
Backup jobs are continuously monitored. Failed backups trigger immediate alerts and are prioritized for remediation.

### 3.7 Retention and Preservation
Backups are retained according to legal, regulatory, and business requirements:
- **Daily Backups:** 30 days
- **Weekly Backups:** 12 weeks
- **Monthly Backups:** 12 months
- **Annual Backups:** 7 years (or per compliance requirements)

### 3.8 Disaster Recovery Integration
Backup strategies are integrated into disaster recovery and business continuity plans.

## 4. Roles and Responsibilities

### RACI Matrix: Backup and Recovery

| Activity | CISO | Backup Administrator | IT Operations | System Owner | BCM Manager |
|----------|------|----------------------|---------------|--------------|-------------|
| Policy creation | R/A | C | C | C | C |
| Backup configuration | C | R/A | C | C | I |
| Backup execution | I | R/A | C | I | I |
| Backup monitoring | C | R/A | C | I | I |
| Restore tests | C | R | R | R/A | C |
| Disaster recovery | A | C | R | C | R |
| Compliance review | R/A | C | I | I | C |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** Thomas Weber (CISO)
- **Backup Administrator:** {{ meta.it.backup_admin }}
- **BCM Manager:** {{ meta.bcm.manager }}
- **Implementation Responsible:** IT Operations, System Owners
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0430_Guideline_Backup_Restore_and_Regular_Tests.md** - Detailed implementation guideline
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy
- `0260_Policy_Cryptography_and_Key_Management.md` - Cryptography Policy
- `0580_Policy_Retention_and_Deletion.md` - Retention Policy

### Related Standards/Baselines
- RPO/RTO matrix
- Backup schedule
- Retention requirements
- Restore test procedures

### Related Processes
- Backup process
- Restore process
- Backup test process
- Disaster recovery process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Backup success rate (target: 99.9%)
- Number of failed backups
- Average backup duration
- Restore success rate (target: 100%)
- Average restore duration (RTO compliance)
- Backup test completion rate (target: 100%)

### Evidence and Proof
- Backup logs and job status
- Restore test protocols
- Backup monitoring reports
- Disaster recovery test reports
- Compliance evidence (retention)
- Backup compliance audit reports

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Missing backups:** Immediate remediation, investigation
- **Untested backups:** Completion, retraining
- **Unencrypted backups:** Immediate encryption, investigation
- **Repeated violations:** Employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and System Owner
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0430_Guideline_Backup_Restore_and_Regular_Tests.md` - Detailed Guideline
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.8.13** - Information backup
- **ISO/IEC 27002:2022** - Information security controls
- **ISO 22301** - Business Continuity Management
- **GDPR (EU 2016/679)** - General Data Protection Regulation (backup of personal data)

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
