# Document Control and Document Register

**Document ID:** 0030  
**Document Type:** Process/Foundation  
**Reference Framework:** BSI IT-Grundschutz (BSI Standards 200-1/200-2/200-3)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Classification:** {{ meta.document.classification }}  
**Last Updated:** {{ meta.document.last_updated }}  
**Next Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines document control procedures for the ISMS according to BSI IT-Grundschutz.
Customize all [TODO] placeholders based on your organization's document management practices.
Reference: BSI Standard 200-1 (Documentation Requirements)
-->

## 1. Purpose and Scope

This document describes document control for the Information Security Management System (ISMS) of **{{ meta.organization.name }}**. It defines processes for creation, review, approval, distribution, modification, and archiving of ISMS documents.

### 1.1 Scope

This document control applies to all ISMS-relevant documents:
- Policies
- Guidelines and process descriptions
- Security concepts and risk analyses
- Work instructions and checklists
- Protocols and evidence

## 2. Storage and Access

### 2.1 Official Storage Location

**Primary Storage Location:** [TODO: e.g. SharePoint, Confluence, DMS]

**Responsible:** {{ meta.document.owner }}

All ISMS documents are stored centrally in:
- **Path:** [TODO: e.g. /ISMS/Documentation/]
- **Backup:** [TODO: Backup strategy]
- **Versioning:** Automatic versioning enabled

### 2.2 Access Control (RBAC)

Access to ISMS documents is role-based:

| Role | Read | Write | Approve | Delete |
|---|---|---|---|---|
| Executive Management | ✓ | ✗ | ✓ | ✗ |
| ISO | ✓ | ✓ | ✓ | ✓ |
| ISMS Team | ✓ | ✓ | ✗ | ✗ |
| Information Domain Managers | ✓ | ✓ (own documents) | ✗ | ✗ |
| All Employees | ✓ (public documents) | ✗ | ✗ | ✗ |

### 2.3 Classification and Protection Need

| Classification | Description | Access | Examples |
|---|---|---|---|
| **Public** | No confidentiality | All Employees | Awareness material |
| **Internal** | Internal use only | All Employees | Policies, guidelines |
| **Confidential** | Restricted access | ISMS Team, Authorized | Risk analyses, security concepts |
| **Strictly Confidential** | Highest confidentiality | Executive Management, ISO | Incident reports, audit findings |

### 2.4 Emergency Access

In emergencies (e.g. ISO unavailable), the following persons have access to all ISMS documents:
- **Executive Management:** {{ meta.ceo.name }}
- **IT Management:** {{ meta.cio.name }}
- **Deputy ISO:** [TODO]

## 3. Document Lifecycle

### 3.1 Creation

**Process:**
1. **Initiation:** Need is identified (ISO, ISMS Team, Department)
2. **Creation:** Author creates document based on template
3. **Quality Assurance:** Peer review by ISMS Team
4. **Approval:** Approval by responsible role (see approval matrix)

**Responsible:** Document author, ISO (coordination)

### 3.2 Review and Approval

#### 3.2.1 Approval Matrix

| Document Type | Creator | Reviewer | Approver |
|---|---|---|---|
| Policies | ISO | ISMS Team | Executive Management |
| Guidelines | ISO, Department | ISMS Team | ISO |
| Security Concepts | Information Domain Managers | ISO | ISO |
| Work Instructions | Department | ISO | IT Management |
| Risk Analyses | ISO | ISMS Team | Executive Management |

#### 3.2.2 Review Intervals

| Document Type | Review Interval | Responsible |
|---|---|---|
| Policies | Annually | ISO |
| Guidelines | Annually | ISO |
| Security Concepts | Annually or upon changes | Information Domain Managers |
| Work Instructions | Annually | Department |
| Risk Analyses | Annually or upon significant changes | ISO |

**Additional Review Triggers:**
- Significant changes in IT infrastructure
- New legal requirements
- Security incidents
- Audit findings
- Organizational changes

### 3.3 Versioning

**Versioning Scheme:**
- **Major Version (X.0):** Significant content changes, new approval required
- **Minor Version (X.Y):** Minor adjustments, editorial changes

**Example:**
- Version 1.0: Initial approval
- Version 1.1: Minor adjustments
- Version 2.0: Major revision

### 3.4 Distribution and Communication

**Distribution Process:**
1. Document approval
2. Publication in central storage location
3. Notification of affected stakeholders (email, intranet)
4. Training/awareness (if required)
5. Acknowledgment of receipt (for critical documents)

**Responsible:** ISO

### 3.5 Change Management

**Process for Changes:**
1. **Change Request:** Initiator submits change request to ISO
2. **Assessment:** ISO assesses change need and impacts
3. **Approval:** Approval by responsible role
4. **Implementation:** Author updates document
5. **Review:** Review by ISMS Team
6. **Approval:** Approval according to approval matrix
7. **Distribution:** Communication of changes

### 3.6 Archiving and Deletion

**Archiving:**
- Old versions are archived for [TODO: e.g. 5 years]
- Archived documents are write-protected
- Access only for ISO and Audit

**Deletion:**
- Documents are deleted after retention period expires
- Deletion according to data protection and compliance requirements
- Deletion log is maintained

**Responsible:** ISO

## 4. Document Register

<!-- 
TEMPLATE AUTHOR NOTE:
Maintain this register with all ISMS documents. Update regularly.
-->

| Document | ID | Owner | Status | Version | Last Updated | Next Review |
|---|---|---|---|---|---|---|
| Information Security Policy | 0010 | {{ meta.ciso.name }} | {{ meta.document.status }} | {{ meta.document.version }} | {{ meta.document.last_updated }} | {{ meta.document.next_review }} |
| ISMS Organization, Roles and RACI | 0020 | {{ meta.ciso.name }} | {{ meta.document.status }} | {{ meta.document.version }} | {{ meta.document.last_updated }} | {{ meta.document.next_review }} |
| Document Control | 0030 | {{ meta.ciso.name }} | {{ meta.document.status }} | {{ meta.document.version }} | {{ meta.document.last_updated }} | {{ meta.document.next_review }} |
| [TODO: Add additional documents] | | | | | | |

## 5. Change Log

| Version | Date | Change | Author | Approver | Status |
|---|---|---|---|---|---|
| 0.1 | {{ meta.document.last_updated }} | First draft | {{ meta.document.owner }} | - | Draft |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Quality Assurance

### 6.1 Document Quality

All ISMS documents must meet the following quality criteria:
- **Completeness:** All required content present
- **Correctness:** Content accurate and current
- **Comprehensibility:** Clearly and understandably formulated
- **Consistency:** Consistent with other ISMS documents
- **Traceability:** Changes documented traceably

### 6.2 Document Templates

Templates exist for all document types with:
- Standardized header (metadata)
- Structure specifications
- Placeholders for variable content
- Notes for authors

**Template Storage Location:** [TODO: e.g. /ISMS/Templates/]

## 7. Training and Awareness

All document authors and ISMS Team members are trained in:
- Document control process
- Use of templates
- Versioning and change management
- Classification and protection needs

**Responsible:** ISO

## 8. Monitoring and Improvement

The document control process is regularly monitored:
- **Metrics:** Number of documents, review compliance, change rate
- **Review:** Annual review of the process
- **Improvement:** Continuous optimization based on feedback

**Next Review:** {{ meta.document.next_review }}

---

**References:**
- BSI Standard 200-1: Management Systems for Information Security (ISMS)
- BSI Standard 200-2: IT-Grundschutz Methodology

<!-- End of template -->
