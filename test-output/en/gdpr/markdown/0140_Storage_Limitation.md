# Storage Limitation

**Document-ID:** 0140  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft  
**Classification:** Internal  
**Last Update:** {{ meta.date }}  

---



## Purpose

This document describes the implementation of the principle of storage limitation in {{ meta.organization }}. Personal data may only be stored for as long as necessary for the processing purpose.

## Principle according to Art. 5(1)(e) GDPR

**Legal Requirement:**  
Personal data must be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed.

### Core Principle

**Storage Period = Purpose Fulfillment + Legal Retention Periods**

After expiration of storage period, data must be:
- Deleted, or
- Anonymized, or
- Archived (with access restrictions)

## Deletion Concept

### Definition of Deletion Periods

**Criteria for Deletion Periods:**
1. Purpose of processing
2. Legal retention periods
3. Contractual obligations
4. Legitimate interests
5. Limitation periods

### Deletion Period Matrix

| Processing Purpose | Data Type | Deletion Period | Legal Basis | Exceptions |
|-------------------|-----------|-----------------|-------------|------------|
| [TODO: Customer Order] | Order data | After contract fulfillment + 2 years | Warranty | Tax law: 10 years |
| [TODO: Newsletter] | Email, name | Until withdrawal | Consent | None |
| [TODO: Application] | Applicant data | 6 months after rejection | Legitimate interest | Longer with consent |
| [TODO: Accounting] | Invoice data | 10 years | Tax code, Commercial code | None |
| [TODO: Employee Data] | Personnel data | 10 years after departure | Social security | None |

## Legal Retention Periods

### Tax Law (Example: Germany)

| Document Type | Retention Period | Legal Basis |
|--------------|------------------|-------------|
| Books, records, annual statements | 10 years | § 147 AO |
| Commercial letters, accounting documents | 10 years | § 147 AO |
| Other documents | 6 years | § 147 AO |

### Commercial Law (Example: Germany)

| Document Type | Retention Period | Legal Basis |
|--------------|------------------|-------------|
| Commercial books, inventories, balance sheets | 10 years | § 257 HGB |
| Commercial letters | 6 years | § 257 HGB |
| Accounting documents | 10 years | § 257 HGB |

### Other Legal Periods

- [TODO: Social security law]
- [TODO: Labor law]
- [TODO: Product liability]
- [TODO: Industry-specific regulations]

## Deletion Processes

### Routine Deletion

**Automated Deletion Processes:**

| System/Database | Deletion Rhythm | Method | Responsible |
|----------------|-----------------|--------|-------------|
| [TODO: CRM System] | Monthly | Automated | IT |
| [TODO: Web Server Logs] | Daily | Automated | IT |
| [TODO: Backup Systems] | On deletion | Manual | IT |
| [TODO: Archive] | Annually | Manual | Department |

### Deletion Procedure

**Steps for Deletion:**

1. **Identification of Deletable Data**
   - Automatic check of deletion periods
   - Consideration of exceptions
   - Creation of deletion list

2. **Review Before Deletion**
   - No ongoing proceedings
   - No legal retention obligations
   - No contractual obligations

3. **Implementation of Deletion**
   - Deletion in all systems
   - Deletion in backups (or marking)
   - Secure deletion (irrecoverable)

4. **Documentation**
   - Logging of deletion
   - Evidence of deletion
   - Retention of deletion log

### Secure Deletion

**Technical Deletion Methods:**
- Overwriting of data carriers
- Cryptographic deletion (key destruction)
- Physical destruction of data carriers
- Secure deletion in cloud systems

## Exceptions to Deletion Obligation

### Archiving in Public Interest (Art. 89 GDPR)

**Permissible Archiving for:**
- Archiving purposes in the public interest
- Scientific or historical research purposes
- Statistical purposes

**Prerequisites:**
- Appropriate safeguards (pseudonymization, access restrictions)
- Data minimization
- Technical and organizational measures

### Retention for Legal Claims

**Retention Permissible for:**
- Ongoing court proceedings
- Threatening legal disputes
- Limitation periods not yet expired

**Measures:**
- Restriction of processing (Art. 18)
- Access restrictions
- Documentation of retention reasons

## Right to Erasure (Art. 17 GDPR)

### Implementation of Erasure Right

**Data subjects have right to erasure when:**
- Data no longer necessary
- Consent withdrawn
- Objection lodged (Art. 21)
- Data unlawfully processed
- Legal obligation to erase

**Exceptions to Erasure Right:**
- Exercise of right to freedom of expression
- Compliance with legal obligations
- Establishment of legal claims
- Archiving purposes in public interest

### Erasure Request Process

1. **Receipt of Request**
   - Identification of data subject
   - Documentation of request
   - Confirmation of receipt

2. **Review of Erasure Obligation**
   - Is data still necessary?
   - Are there retention obligations?
   - Do exceptions apply?

3. **Implementation or Rejection**
   - If erasure obligation: Perform deletion
   - If exception: Reasoned rejection
   - Notification of recipients (Art. 19)

4. **Response**
   - Information about erasure or rejection
   - Deadline: Without delay, at most 1 month

## Controls and Monitoring

### Regular Reviews

| Control | Frequency | Responsible | Documentation |
|---------|-----------|-------------|---------------|
| Deletion Period Review | Monthly | IT | Deletion log |
| Deletion Concept Review | Annually | DPO | Review report |
| Backup Deletion | Quarterly | IT | Backup log |
| Erasure Requests | On receipt | DPO | Request register |

### Deletion Logging

**Documentation of Each Deletion:**
- Date and time
- Deleted data types
- Number of deleted records
- Deletion reason (period, request, etc.)
- Executing person
- Affected systems

## Documentation

### Evidence Requirements

**Document for Accountability:**
- Deletion concept with periods
- Deletion processes and procedures
- Performed deletions (logs)
- Processed erasure requests
- Exceptions and their justification

### Records of Processing Activities (Art. 30)

**Documentation of Storage Period:**
- Deletion periods for each processing activity
- Justification of periods
- Legal retention obligations
- Deletion procedures

## Links to Other Documents

- **Data Protection Principles (Art. 5):** Storage limitation as core principle
- **Right to Erasure (Art. 17):** Implementation of data subject right
- **Restriction (Art. 18):** Alternative to deletion
- **Notification Obligation (Art. 19):** Notification of recipients
- **Records (Art. 30):** Documentation of deletion periods

## Common Violations and Their Prevention

| Violation | Example | Prevention |
|-----------|---------|------------|
| Unlimited storage | "Keep just in case" | Define deletion periods |
| Missing deletion processes | No automated deletion | Implement deletion routines |
| Ignoring erasure requests | Delayed processing | Establish process |
| Incomplete deletion | Only deleted in one system | Check all systems |

---

**Next Steps:**
1. Define deletion periods for all processing activities
2. Implement automated deletion processes
3. Establish procedures for erasure requests
4. Document deletion concept and logs
5. Train employees on deletion obligations

