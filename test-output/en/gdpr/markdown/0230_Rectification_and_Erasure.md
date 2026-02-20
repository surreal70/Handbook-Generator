# Rectification and Erasure

**Document-ID:** GDPR-0230
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



## Purpose

This document describes the implementation of the right to rectification and erasure in AdminSend GmbH. Data subjects have the right to rectification of inaccurate data and erasure of data no longer necessary.

## Right to Rectification (Art. 16)

### Scope of Rectification Right

**Data subjects have the right to:**
- Immediate rectification of inaccurate data
- Completion of incomplete data
- Supplementary statement

### Rectification Process

**Standard Process:**

1. **Receipt of Request (Day 0)**
   - Registration
   - Acknowledgment
   - Assignment

2. **Review (Day 1-10)**
   - Identification of data subject
   - Review of inaccuracy
   - Comparison with evidence

3. **Implementation (Day 11-25)**
   - Rectification in all systems
   - Notification of recipients (Art. 19)
   - Documentation

4. **Response (Day 26-30)**
   - Information about rectification performed
   - List of notified recipients

### Rectification Matrix

| System | Responsible | Rectification Procedure | Documentation |
|--------|-------------|------------------------|---------------|
| [TODO: CRM] | IT | Manual change | Change log |
| [TODO: ERP] | IT | Workflow-driven | Audit trail |
| [TODO: Database] | IT | SQL update | Change protocol |
| [TODO: Backup] | IT | Marking | Backup log |

## Right to Erasure (Art. 17)

### Grounds for Erasure

**Erasure is required when:**

| Ground | Description | Example |
|--------|-------------|---------|
| No Longer Necessary | Purpose fulfilled | Applicant data after rejection |
| Withdrawal of Consent | Consent withdrawn | Newsletter unsubscribe |
| Objection | Objection lodged (Art. 21) | Marketing objection |
| Unlawful Processing | Without legal basis | Data without consent |
| Legal Obligation | Legal erasure obligation | Data protection violation |
| Children | Information society services | Social media under 16 |

### Exceptions to Right of Erasure

**Erasure not required for:**

| Exception | Description |
|-----------|-------------|
| Freedom of Expression | Exercise of right to freedom of expression |
| Legal Obligation | Compliance with legal obligations |
| Public Interest | Tasks in the public interest |
| Healthcare | Healthcare, occupational medicine |
| Archiving Purposes | Archiving in the public interest |
| Legal Claims | Establishment, exercise or defense |

### Erasure Process

**Standard Process:**

1. **Receipt of Request (Day 0)**
   - Registration
   - Acknowledgment
   - Assignment

2. **Review (Day 1-10)**
   - Identification of data subject
   - Review of erasure grounds
   - Review of exceptions
   - Review of legal retention periods

3. **Decision (Day 11-15)**
   - Erasure or reasoned refusal
   - If refusal: Review of restriction (Art. 18)

4. **Implementation (Day 16-25)**
   - Erasure in all systems
   - Notification of recipients (Art. 19)
   - Documentation

5. **Response (Day 26-30)**
   - Information about erasure or refusal
   - If refusal: Justification and remedies

### Erasure Procedures

**Technical Erasure:**

| System | Erasure Method | Responsible | Documentation |
|--------|----------------|-------------|---------------|
| [TODO: Production Systems] | Immediate erasure | IT | Erasure log |
| [TODO: Backups] | Marking/overwriting | IT | Backup log |
| [TODO: Archives] | Physical destruction | IT | Destruction log |
| [TODO: Cloud] | API-driven erasure | IT | API log |

## Notification Obligation (Art. 19)

### Notification of Recipients

**Recipients must be informed of rectification or erasure:**

**Process:**
1. Identification of all recipients
2. Notification of rectification/erasure
3. Documentation of notifications
4. Information to data subject about recipients (on request)

**Exceptions:**
- Impossible
- Disproportionate effort

### Recipient Matrix

| Recipient Type | Notification Obligation | Method | Documentation |
|----------------|------------------------|--------|---------------|
| [TODO: Processors] | Yes | Email | Notification log |
| [TODO: Third Party Recipients] | Yes | Email/written | Notification log |
| [TODO: Public Authorities] | Yes | Written | Notification log |

## Documentation

### Rectification and Erasure Register

| Date | Data Subject | Type | Reason | Performed | Recipients Notified | Processor |
|------|--------------|------|--------|-----------|-------------------|-----------|
| [TODO] | [TODO] | Rectification | Inaccurate | Yes | Yes | [TODO] |
| [TODO] | [TODO] | Erasure | No longer necessary | Yes | Yes | [TODO] |
| [TODO] | [TODO] | Erasure | Refused (retention period) | No | N/A | [TODO] |

### Evidence Requirements

**Documentation for Accountability:**
- All rectification and erasure requests
- Performed rectifications and erasures
- Refusals and their justification
- Notifications to recipients
- Exceptions and their justification

## Deadlines

**Processing Deadline:**
- Without delay, at most 1 month
- Extension by 2 months possible for complexity
- Justification of extension required

## Links to Other Documents

- **Transparency (Art. 12):** Modalities of processing
- **Accuracy (Art. 5(1)(d)):** Principle of accuracy
- **Storage Limitation (Art. 5(1)(e)):** Principle of erasure
- **Notification Obligation (Art. 19):** Notification of recipients
- **Restriction (Art. 18):** Alternative to erasure

## Common Violations and Their Prevention

| Violation | Example | Prevention |
|-----------|---------|------------|
| Incomplete Rectification | Only in one system | Check all systems |
| Delayed Erasure | Erasure after 3 months | Deadline control |
| Missing Notification | Recipients not informed | Notification process |
| Unjustified Refusal | Refusal without review | Careful review |

**Next Steps:**
1. Establish processes for rectification and erasure requests
2. Implement erasure procedures for all systems
3. Define notification process for recipients
4. Train employees on rectification and erasure rights
5. Document all requests in register

