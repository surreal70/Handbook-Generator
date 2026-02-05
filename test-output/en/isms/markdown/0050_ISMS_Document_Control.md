# Document Control / Documented Information



**Document ID:** 0050  
**Document Type:** ISMS Foundation Document  
**Standard Reference:** ISO/IEC 27001:2022 Clause 7.5  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose and Scope

This document defines the requirements for controlling documented information within the ISMS of **AdminSend GmbH**. It ensures that:
- Documents are available and suitable for use
- Documents are adequately protected
- Documents are controlled in their creation, review, approval, and update

## 2. Storage and Access

### 2.1 Official Storage Location

**Primary Storage:**
- **System:** [TODO: SharePoint, Confluence, DMS]
- **Path:** [TODO: /ISMS/Documentation/]
- **URL:** [TODO: https://docs.organization.com/isms/]

**Backup and Archiving:**
- **Backup System:** {{ netbox.backup.system }}
- **Backup Frequency:** Daily
- **Archiving Duration:** 10 years after decommissioning

### 2.2 Access Control

**Access Permissions:**

| Document Type | CISO | ISMS Manager | IT Operations | Business Units | All Employees |
|---------------|------|--------------|---------------|----------------|---------------|
| ISMS Policy | R/W | R/W | R | R | R |
| Policies (Abstract) | R/W | R/W | R | R | R |
| Guidelines (Detailed) | R/W | R/W | R/W | R | R |
| Risk Register | R/W | R/W | R | - | - |
| Audit Reports | R/W | R/W | - | - | - |
| Incident Reports | R/W | R/W | R/W | - | - |

**Legend:** R = Read, W = Write, - = No Access

**Access Management:**
- Access rights are managed via IAM system
- See `0220_Policy_Access_Control_and_Identity_Management.md`
- Recertification: Quarterly

### 2.3 Offline/Emergency Access

**Emergency Access:**
- Critical documents (emergency plans, contact lists) are additionally stored offline
- Storage Location: [TODO: Physical safe, encrypted USB stick]
- Responsible: Thomas Weber

**Break-Glass Access:**
- See `0200_Emergency_Access_BreakGlass.md` (BCM Handbook)
- Emergency access to ISMS documentation in case of primary system failure



## 3. Document Lifecycle

### 3.1 Creation

**Process:**
1. **Initiation:** Need is identified (e.g., new policy, new requirement)
2. **Assign Author:** CISO or ISMS Manager assigns author
3. **Use Template:** Author uses appropriate template
4. **Create Draft:** Author creates draft with status "Draft"
5. **Capture Metadata:** Document ID, owner, version, classification

**Responsible:** Document author (assigned by CISO)

### 3.2 Review

**Review Process:**
1. **Peer Review:** Technical review by colleagues
2. **Stakeholder Review:** Consultation with affected stakeholders
3. **CISO Review:** Final review by CISO
4. **Change Status:** From "Draft" to "In Review"

**Review Criteria:**
- Technical correctness
- Completeness
- Consistency with other ISMS documents
- Compliance with ISO 27001:2022
- Understandability and implementability

**Responsible:** CISO or ISMS Manager

### 3.3 Approval

**Approval Process:**
1. **Approval Request:** After successful review
2. **Approval:** By CISO (policies) or management (ISMS policy)
3. **Change Status:** From "In Review" to "Approved"
4. **Version Number:** Assign final version number (e.g., 1.0)

**Approval Authorities:**

| Document Type | Approved By |
|---------------|-------------|
| ISMS Policy | Management |
| Policies (Abstract) | CISO |
| Guidelines (Detailed) | CISO or ISMS Manager |
| Process Documents | CISO or ISMS Manager |
| Templates | ISMS Manager |

**Responsible:** See table above

### 3.4 Publication and Communication

**Publication:**
1. **Upload:** Document is published in official storage location
2. **Update Document Register:** Entry in document register
3. **Archive Old Version:** Previous version is archived

**Communication:**
- **New Documents:** Email notification to all affected stakeholders
- **Significant Changes:** Email notification + awareness campaign
- **Minor Changes:** Entry in change log, no separate notification

**Communication Channels:**
- Email to all employees
- Intranet news
- Security awareness training
- Team meetings

**Responsible:** ISMS Manager

### 3.5 Change Management

**Change Process:**
1. **Change Request:** Need for change is identified
2. **Impact Assessment:** Assess impact of change
3. **Implement Change:** Document is updated
4. **Review and Approval:** As with new creation
5. **Increment Version Number:** Major (1.0 → 2.0) or Minor (1.0 → 1.1)

**Versioning Scheme:**
- **Major Version (X.0):** Significant changes, new requirements
- **Minor Version (X.Y):** Minor changes, corrections, clarifications

**Change Log:**
Each document contains a change log with:
- Version number
- Date
- Author
- Description of change
- Approver

**Responsible:** Document author, CISO

### 3.6 Regular Review

**Review Intervals:**

| Document Type | Review Interval |
|---------------|-----------------|
| ISMS Policy | Annually |
| Policies (Abstract) | Annually |
| Guidelines (Detailed) | Annually or as needed |
| Risk Register | Quarterly |
| SoA | Annually or upon scope change |
| Process Documents | Every 2 years |

**Review Triggers (event-driven):**
- New legal requirements
- Significant organizational changes
- Security incidents with lessons learned
- Audit findings
- Technology changes

**Review Process:**
1. **Review Reminder:** ISMS Manager reminds owner
2. **Conduct Review:** Owner checks currency and relevance
3. **Decision:** No change / Change required
4. **Documentation:** Update review date in document

**Responsible:** Document owner (see document register)

### 3.7 Archiving and Deletion

**Archiving:**
- **Old Versions:** Are archived once new version is approved
- **Archiving Duration:** 10 years
- **Archiving Location:** [TODO: Archive system]

**Deletion:**
- **Decommissioning:** Documents are deleted after archiving period expires
- **Deletion Process:** Secure deletion according to `0580_Policy_Retention_and_Deletion.md`
- **Approval:** Deletion must be approved by CISO

**Responsible:** ISMS Manager

## 4. Versioning

### 4.1 Versioning Scheme

**Format:** X.Y

- **X (Major Version):** Significant changes
  - New requirements
  - Structural changes
  - Change in scope

- **Y (Minor Version):** Minor changes
  - Corrections
  - Clarifications
  - Update of contact information

**Examples:**
- 0.1 → Draft
- 1.0 → First approved version
- 1.1 → Minor correction
- 2.0 → Major revision

### 4.2 Change Log

Each document contains a change log at the end:

```markdown
## Change History

| Version | Date | Author | Description | Approved By |
|---------|------|--------|-------------|-------------|
| 1.0 | 2026-01-15 | Thomas Weber | Initial version | Management |
| 1.1 | 2026-03-20 | ISMS Manager | Contact information updated | CISO |
| 2.0 | 2026-12-01 | Thomas Weber | New requirements from NIS2 | Management |
```

## 5. Document Register

The document register is the central overview of all ISMS documents.

### 5.1 Document Register Structure

| Document ID | Document Title | Owner | Status | Version | Last Change | Next Review |
|-------------|----------------|-------|--------|---------|-------------|-------------|
| 0010 | ISMS Policy | Thomas Weber | Approved | 1.0 | {{ meta.document.date }} | {{ meta.document.next_review }} |
| 0020 | ISMS Scope | Thomas Weber | Approved | 1.0 | {{ meta.document.date }} | {{ meta.document.next_review }} |
| 0030 | Context and Stakeholders | Thomas Weber | Approved | 1.0 | {{ meta.document.date }} | {{ meta.document.next_review }} |
| 0040 | ISMS Governance | Thomas Weber | Approved | 1.0 | {{ meta.document.date }} | {{ meta.document.next_review }} |
| 0050 | Document Control | Thomas Weber | Approved | 1.0 | {{ meta.document.date }} | {{ meta.document.next_review }} |
| ... | ... | ... | ... | ... | ... | ... |

[TODO: Create and maintain complete document register]

### 5.2 Maintenance of Document Register

**Responsible:** ISMS Manager

**Updates:**
- With every document change
- With status changes
- With owner changes

**Access:**
- Document register is readable by all employees
- Storage location: [TODO: Link to document register]

## 6. Document Classification

All ISMS documents are classified according to `0280_Policy_Data_Classification_and_Information_Handling.md`:

| Classification | Description | Examples |
|----------------|-------------|----------|
| **Public** | No confidentiality | Public policies |
| **Internal** | For employees only | Most ISMS documents |
| **Confidential** | Restricted access | Risk register, audit reports |
| **Strictly Confidential** | Very restricted access | Incident reports with sensitive data |

**Marking:**
- Classification is indicated in document header
- Classification determines access rights and handling

## 7. External Documents

**External Documents** (e.g., supplier policies, certificates) are also controlled:

**Process:**
1. **Identification:** Identify relevant external documents
2. **Assessment:** Check relevance and trustworthiness
3. **Storage:** Store in separate area
4. **Marking:** Mark as "External Document"
5. **Review:** Regularly check for currency

**Responsible:** ISMS Manager

## 8. Retention Periods

| Document Type | Retention Period | Legal Basis |
|---------------|------------------|-------------|
| ISMS Policy | 10 years after decommissioning | ISO 27001 |
| Policies and Guidelines | 10 years after decommissioning | ISO 27001 |
| Risk Register | 10 years | ISO 27001 |
| Audit Reports | 10 years | ISO 27001, Commercial Law |
| Incident Reports | 10 years | GDPR, NIS2 |
| Training Records | 10 years | Evidence requirement |
| Contracts | According to contract law | Commercial Law |

See `0580_Policy_Retention_and_Deletion.md` for details.

## 9. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0040_ISMS_Governance_Roles_and_Responsibilities.md` - Governance
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification
- `0360_Policy_Change_and_Release_Management.md` - Change Management
- `0580_Policy_Retention_and_Deletion.md` - Retention and Deletion

### External Standards
- **ISO/IEC 27001:2022** - Clause 7.5: Documented information
- **ISO/IEC 27002:2022** - Control 5.1: Policies for information security

---

**Approved by:**  
Thomas Weber, CISO  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }}
