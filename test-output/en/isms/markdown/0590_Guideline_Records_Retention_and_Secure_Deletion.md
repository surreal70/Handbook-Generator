# Guideline: Records Retention and Secure Deletion

**Document-ID:** [FRAMEWORK]-0590
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

## 1. Purpose and Scope

This guideline specifies the `0580_Policy_Retention_and_Deletion.md` and defines:
- Retention periods for different data types
- Secure deletion procedures
- Records management processes

**Scope:** All data and documents at **AdminSend GmbH**

## 2. Retention Periods

### 2.1 Business Documents

| Document Type | Retention Period | Legal Basis |
|---------------|------------------|-------------|
| Annual financial statements | 10 years | HGB §257 |
| Accounting records | 10 years | HGB §257 |
| Invoices | 10 years | HGB §257, AO §147 |
| Contracts | 10 years after end | HGB §257 |
| Business correspondence | 6 years | HGB §257 |
| Quotes | 6 years | HGB §257 |

### 2.2 Personnel Documents

| Document Type | Retention Period | Legal Basis |
|---------------|------------------|-------------|
| Personnel files | 10 years after departure | GDPR Art. 17 |
| Payroll records | 10 years | AO §147 |
| Employment references | 3 years | BGB §195 |
| Application documents (rejected) | 6 months | AGG §15 |
| Time tracking data | 2 years | ArbZG §16 |

### 2.3 IT Data

| Data Type | Retention Period | Justification |
|-----------|------------------|---------------|
| Emails (business) | {{ meta-handbook.retention_email_years }} years | Business correspondence |
| Logs (security) | {{ meta-handbook.retention_log_years }} years | Forensics, compliance |
| Logs (system) | 1 year | Troubleshooting |
| Backups | Per backup policy | Recovery |
| Audit trails | {{ meta-handbook.retention_audit_years }} years | Compliance |

### 2.4 Customer Data

| Data Type | Retention Period | Legal Basis |
|-----------|------------------|-------------|
| Customer master data | Until contract end + 3 years | Statute of limitations |
| Order data | 10 years | HGB §257 |
| Payment data | 10 years | AO §147 |
| Communication | 6 years | HGB §257 |

## 3. Retention Management

### 3.1 Retention Policies

**Automation:**
- Retention labels in Microsoft 365
- Lifecycle policies in cloud storage
- Automatic deletion after expiration

**Manual Processes:**
- For physical documents
- For legacy systems

### 3.2 Legal Hold

**For Legal Proceedings:**
- Suspension of deletion
- Preservation order
- Documentation of legal hold
- Lifting after proceedings end

### 3.3 Retention Register

**Documentation:**
- Data type, retention period, legal basis
- Storage location, responsible person
- Deletion date
- Regular reviews (annually)

## 4. Secure Deletion

### 4.1 Digital Data

**Methods per DIN 66399:**

| Media | Method | Standard |
|-------|--------|----------|
| HDD | Software deletion (3-pass) or degaussing | DIN 66399 H-3/H-4 |
| SSD | Secure Erase (ATA) or cryptographic deletion | DIN 66399 H-3 |
| Cloud data | Logical deletion + confirmation | Provider-dependent |
| Backups | Cryptographic deletion (destroy keys) | DIN 66399 H-4 |

**Tools:**
- DBAN, Blancco (software deletion)
- Degausser (magnetic deletion)
- Shredder (physical destruction)

### 4.2 Physical Documents

**Methods per DIN 66399:**

| Protection Level | Particle Size | Application |
|------------------|---------------|-------------|
| P-3 | ≤ 320 mm² | Internal documents |
| P-4 | ≤ 160 mm² | Confidential documents |
| P-5 | ≤ 30 mm² | Highly confidential documents |

**Process:**
- Shredders in offices (P-3)
- Certified disposal partners (P-4, P-5)
- Disposal certificate

### 4.3 Deletion Log

**Documentation:**
- Date of deletion
- Deleted data/documents
- Deletion method
- Person performing deletion
- Confirmation of deletion

**Retention:** {{ meta-handbook.retention_deletion_log_years }} years

## 5. Email Archiving

### 5.1 Archiving Obligation

**Business Emails:**
- Automatic archiving
- Immutability (WORM)
- Retention: {{ meta-handbook.retention_email_years }} years

**Private Emails:**
- No archiving
- Marking by user (Subject: [PRIVATE])

### 5.2 Archiving System

**System:** {{ meta-handbook.email_archive_system }}

**Functions:**
- Automatic archiving
- Full-text search
- eDiscovery
- Legal hold

### 5.3 Archive Access

**Permissions:**
- Users: Own emails
- Supervisors: With legitimate interest (with approval)
- Legal/Compliance: For audits and investigations
- IT admins: Only for technical administration

## 6. Data Minimization

### 6.1 Privacy by Design

**Principles:**
- Collect only necessary data
- Choose shortest retention period
- Implement automatic deletion

### 6.2 Regular Reviews

**Quarterly:**
- Identify unused data
- Review deletion
- Adjust retention policies

## 7. Cloud Data Deletion

### 7.1 SaaS Applications

**Process:**
1. Logical deletion in application
2. Wait for retention period (provider-dependent)
3. Request confirmation of final deletion
4. Documentation

### 7.2 IaaS/PaaS

**Process:**
1. Delete data
2. Delete volumes/disks
3. Delete snapshots
4. Destroy cryptographic keys
5. Confirmation of deletion

## 8. Compliance and Audit

### 8.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Automatic deletion (after expiration) | 100% |
| Deletion log completeness | 100% |
| Retention policy compliance | > 95% |
| Disposal certificates | 100% |

### 8.2 Audit Evidence

- Retention register
- Deletion logs
- Disposal certificates
- Email archiving reports

## 9. References

### Internal Documents
- `0580_Policy_Retention_and_Deletion.md`
- `0570_Guideline_Data_Protection_Requirements_and_Data_Processing.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.33** - Protection of records
- **DIN 66399** - Destruction of data carriers
- **HGB §257** - Retention of documents
- **AO §147** - Regulations for retention of documents

**Approved by:** [TODO], CISO  
**Next Review:** [TODO]

