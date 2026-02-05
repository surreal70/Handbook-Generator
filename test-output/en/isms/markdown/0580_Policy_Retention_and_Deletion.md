# Policy: Retention and Deletion



**Document ID:** 0580  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.33, A.5.34, A.8.10 (incl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the requirements for retention and deletion of information and data at **AdminSend GmbH**. It ensures compliance with legal retention obligations and adherence to data protection principles (data minimization, storage limitation).

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Data:** All information and data (structured and unstructured)
- **Systems:** All IT systems, databases, backup systems, archives
- **Media:** Digital and physical media
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Retention Periods
Retention periods are defined for all information. Retention periods are based on legal, regulatory, and business requirements.

### 3.2 Retention Schedule
A retention schedule is created and maintained. The retention schedule defines for each information category:
- Retention period
- Legal basis
- Deletion procedure
- Responsible role

### 3.3 Data Minimization and Storage Limitation
Data is retained only as long as necessary (GDPR Art. 5(1)(e)). After expiration of the retention period, data is deleted or anonymized.

### 3.4 Secure Deletion
Data is securely and irrevocably deleted. Deletion procedures ensure that data cannot be recovered.

### 3.5 Deletion Concept
A deletion concept defines:
- Deletion procedures for different media
- Deletion periods and triggers
- Responsibilities
- Evidence documentation

### 3.6 Backup Retention
Backups are subject to the same retention periods as production data. Backups are deleted after expiration of the retention period.

### 3.7 Legal Hold
For legal proceedings or investigations, data may be exempted from deletion (Legal Hold). Legal Hold is documented and monitored.

### 3.8 Physical Media
Physical media (hard drives, USB drives, paper) are securely disposed of:
- Digital media: Secure deletion or physical destruction
- Paper: Shredding or certified disposal

## 4. Roles and Responsibilities

### RACI Matrix: Retention and Deletion

| Activity | CISO | DPO | IT Operations | Business Owner | Records Manager |
|----------|------|-----|---------------|----------------|-----------------|
| Policy Creation | R/A | C | C | C | C |
| Retention Schedule | C | C | C | R | R/A |
| Deletion Concept | R/A | C | R | C | C |
| Deletion Execution | I | I | R/A | C | C |
| Legal Hold | C | C | I | C | R/A |
| Backup Deletion | C | I | R/A | I | C |
| Physical Disposal | C | I | R/A | I | C |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** Thomas Weber (CISO)
- **Records Manager:** {{ meta.records.manager }}
- **Data Protection Officer:** {{ meta.dpo.name }}
- **Implementation Responsible:** IT Operations, Business Owner
- **Control/Audit Function:** ISMS, Internal Audit, Legal

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Associated Guidelines
- **0590_Guideline_Records_Retention_and_Secure_Deletion.md** - Detailed implementation guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0560_Policy_Data_Protection_Interfaces.md` - Privacy Policy
- `0420_Policy_Backup_and_Recovery.md` - Backup Policy

### Associated Standards/Baselines
- Retention schedule
- Deletion concept
- Secure deletion procedures (NIST SP 800-88, BSI TL-03423)
- Legal Hold process

### Associated Processes
- Retention management process
- Deletion process (automated and manual)
- Legal Hold process
- Physical disposal process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Retention schedule coverage (Target: 100% of information categories)
- Number of deletions performed (planned vs. performed)
- Average time to deletion after expiration (Target: < 30 days)
- Number of legal holds and duration
- Backup deletion compliance (Target: 100%)
- Number of securely disposed physical media

### Evidence and Proof
- Retention schedule
- Deletion logs and evidence
- Legal Hold documentation
- Backup deletion logs
- Disposal certificates
- Audit logs for deletions

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Non-deleted Data:** Completion, compliance investigation
- **Missing Retention Schedule:** Creation, risk assessment
- **Insecure Deletion:** Incident response, risk assessment
- **Repeated Violations:** Employment consequences, fines

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and DPO
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0590_Guideline_Records_Retention_and_Secure_Deletion.md` - Detailed Guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.33** - Protection of records
- **ISO/IEC 27001:2022 Annex A.5.34** - Privacy and protection of PII
- **ISO/IEC 27001:2022 Annex A.8.10** - Information deletion
- **GDPR Art. 5(1)(e)** - Storage limitation
- **GDPR Art. 17** - Right to erasure
- **NIST SP 800-88** - Guidelines for Media Sanitization
- **BSI TL-03423** - Guide to Deletion and Destruction

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
