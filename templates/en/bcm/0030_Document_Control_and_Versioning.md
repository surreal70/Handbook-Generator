# Document Control and Versioning

**Document-ID:** [FRAMEWORK]-0030
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
This template defines document control procedures for the BCMS.
It aligns with ISO 22301:2019 Clause 7.5 (Documented information).

Customization required:
- Define document repository and access controls
- Establish version control scheme
- Define review and approval workflows
- Ensure offline availability for emergency access
-->

## 1. Document Landscape

### 1.1 BCM Document Structure

The BCM documentation of {{ meta-organisation.name }} includes the following document types:

**Strategic Documents:**
- BCM policy and guidelines
- BCM strategy and objectives
- Scope and boundaries

**Operational Documents:**
- Business Impact Analysis (BIA)
- Risk analysis and scenarios
- Business Continuity Plans (BCP)
- IT Disaster Recovery Plans (DRP)
- Crisis management plans

**Supporting Documents:**
- Contact lists and escalation matrices
- Runbooks and checklists
- Test protocols and exercise reports
- Training materials

### 1.2 Document Repository

**Primary Repository:**
[TODO: Define the primary document management system]

**Example:**
- **System:** SharePoint / Confluence / Document Management System
- **Path:** `BCM/Documentation/`
- **Access:** Role-based (RBAC) according to authorization concept
- **Backup:** Daily backup, 30-day retention

**Offline Availability / Emergency Access:**

Critical BCM documents must be available even when IT systems fail:

[TODO: Define offline access options]

**Example:**
- **Emergency USB drives:** Encrypted USB drives with current BCM plans held by crisis team members
- **Paper printouts:** Sealed emergency binders at defined locations (safe, alternate site)
- **Cloud backup:** Access via mobile devices even when main site fails
- **Update:** Quarterly or upon significant changes

### 1.3 Document Register

| Document ID | Document Name | Version | Owner | Classification | Location |
|-------------|---------------|---------|-------|----------------|----------|
| BCM-0010 | Purpose and Scope | {{ meta-handbook.revision }} | {{ meta-handbook.owner }} | {{ meta-handbook.classification }} | [TODO: Path] |
| BCM-0020 | BCM Policy | {{ meta-handbook.revision }} | {{ meta-handbook.owner }} | {{ meta-handbook.classification }} | [TODO: Path] |
| BCM-0030 | Document Control | {{ meta-handbook.revision }} | {{ meta-handbook.owner }} | {{ meta-handbook.classification }} | [TODO: Path] |
| ... | ... | ... | ... | ... | ... |

[TODO: Complete the document register]

## 2. Versioning

### 2.1 Versioning Scheme

{{ meta-organisation.name }} uses the following versioning scheme for BCM documents:

**Format:** `MAJOR.MINOR.PATCH`

**Example:** Version 2.3.1

- **MAJOR (2):** Significant content changes, new structure, new requirements
- **MINOR (3):** Additions, updates without fundamental changes
- **PATCH (1):** Corrections, formatting, editorial changes

### 2.2 Version Increment

**Increment MAJOR version for:**
- Fundamental restructuring of the document
- Significant changes to BCM strategy or processes
- New regulatory requirements
- Changes to scope

**Increment MINOR version for:**
- Addition of new sections or processes
- Update of contact data or roles
- Adaptation to organizational changes
- Results from exercises or tests

**Increment PATCH version for:**
- Spelling corrections
- Formatting changes
- Update of references
- Editorial adjustments

### 2.3 Version Status

| Status | Description | Usage |
|--------|-------------|-------|
| **Draft** | Document in creation | Visible only to authors |
| **In Review** | Document under review | Visible to reviewers |
| **Approved** | Document approved and active | Visible to all authorized users |
| **Archived** | Document obsolete, historical | For archival purposes only |

## 3. Approval and Review Process

### 3.1 Roles in Document Process

**Author (Creator):**
- **Responsible:** Subject matter expert or BCM manager
- **Tasks:** Creation and maintenance of document content

**Reviewer:**
- **Responsible:** Subject matter experts, affected stakeholders
- **Tasks:** Content review, feedback, approval recommendation

**Approver:**
- **Responsible:** {{ meta-handbook.approver }} or delegated manager
- **Tasks:** Formal approval, assumption of responsibility

### 3.2 Approval Process

1. **Creation:** Author creates document in "Draft" status
2. **Review:** Document is submitted to reviewers for review (Status: "In Review")
3. **Revision:** Author incorporates feedback
4. **Approval:** Approver releases document (Status: "Approved")
5. **Publication:** Document is made available to target audience
6. **Archiving:** Old version is archived

### 3.3 Review Intervals

| Document Type | Review Interval | Responsible |
|---------------|-----------------|-------------|
| BCM Policy | Annually | {{ meta-organisation-roles.role_CEO }} |
| BIA Results | Annually | BCM Manager |
| BCM Plans (BCP/DRP) | Semi-annually | Subject matter experts |
| Contact Lists | Quarterly | BCM Manager |
| Runbooks | After each exercise | IT Operations |

**Event-driven Reviews:**
- After severe incidents
- Upon organizational changes
- Upon changes to regulatory requirements
- After audits or certifications

## 4. Distribution and Access Rights

### 4.1 Target Audiences

**Crisis Team:**
- Access to all BCM documents
- Offline copies of critical plans
- Notification of changes

**IT Operations:**
- Access to IT DR plans and runbooks
- Technical documentation
- Contact lists

**Departments:**
- Access to relevant BCP plans
- Process-specific runbooks
- Training materials

**External Service Providers:**
- Access to relevant excerpts (NDA required)
- No access to confidential contact data
- Only approved versions

### 4.2 Access Control (RBAC)

[TODO: Define role-based access rights]

**Example:**

| Role | Read | Write | Approve | Delete |
|------|------|-------|---------|--------|
| BCM Manager | ✓ | ✓ | ✓ | ✓ |
| Crisis Team | ✓ | - | - | - |
| Department | ✓ (own plans) | ✓ (own plans) | - | - |
| IT Operations | ✓ (IT plans) | ✓ (IT plans) | - | - |
| External | ✓ (approved) | - | - | - |

### 4.3 Protection Requirements and Classification

| Classification | Description | Example Documents |
|----------------|-------------|-------------------|
| **Public** | No protection required | BCM Policy (external) |
| **Internal** | For employees only | BCM handbook, training materials |
| **Confidential** | Restricted group | BIA results, contact lists |
| **Strictly Confidential** | Crisis team only | Emergency access, passwords |

## 5. Change Log (Changelog)

### 5.2 Change Requests

Change requests for BCM documents can be submitted through:

- **Email to:** [TODO: BCM Manager email]
- **Ticketing system:** [TODO: System and category]
- **Form:** [TODO: Link to change request form]

Each change request is reviewed and prioritized. Processing follows defined SLAs.

<!-- End of template -->
