# Document Control and Versioning

**Document-ID:** [FRAMEWORK]-0020
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

## Document Metadata

| Field | Value |
|---|---|
| Document Title | IT Operations Handbook – {{ meta-organisation.name }} |
| Document ID | [TODO: Unique Document ID] |
| System/Service | [TODO: System/Service Name] |
| Owner | {{ meta-handbook.owner }} |
| Responsible Editor | [Author] |
| Approval Authority | {{ meta-handbook.approver }} |
| Classification | {{ meta-handbook.classification }} |
| Storage Location | [TODO: Central Repository/Storage Location] |
| Organization | {{ meta-organisation.name }} |
| Location | {{ meta-organisation.city }}, {{ meta-organisation.country }} |

## Version History

| Version | Date | Author | Changes | Approval |
|---|---|---|---|---|
| {{ meta-handbook.revision }} | [TODO: Date] | [Author] | Initial Version | {{ meta-handbook.approver }} |
| | | | | |
| | | | | |

> **Note:** Use Semantic Versioning (SemVer) for versioning:
> - **Major.Minor.Patch** (e.g., 1.0.0)
> - **Major:** Fundamental changes, breaking changes
> - **Minor:** New features, backward compatible
> - **Patch:** Bugfixes, minor corrections

## Versioning Guidelines

### Semantic Versioning (SemVer)

**Format:** MAJOR.MINOR.PATCH

- **MAJOR:** Incompatible changes, fundamental revisions
  - Example: Change of system architecture, new operating models
- **MINOR:** New functionality, backward compatible
  - Example: New processes, additional sections
- **PATCH:** Bugfixes, corrections, clarifications
  - Example: Typos, formatting, minor additions

### Versioning Rules

1. **Initial Version:** 1.0.0 after initial release
2. **Drafts:** 0.x.x before initial release
3. **Document Changes:** Record every change in version history
4. **Date:** ISO 8601 format (YYYY-MM-DD)
5. **Author:** Full name and email

## Review and Approval Process

### 1. Change Request

**Responsible:** Document Owner or Department

**Content:**
- Description of change
- Justification and business value
- Impact analysis
- Affected sections

**Approval:** {{ meta-handbook.owner }}

### 2. Technical Review

**Reviewers:**
- **Operations:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})
- **Architecture:** [TODO: Architecture Lead]
- **Security:** {{ meta-organisation-roles.role_ciso.name }} ({{ meta-organisation-roles.role_ciso.email }})
- **Compliance:** [TODO: Compliance Lead]

**Review Criteria:**
- Technical correctness
- Completeness
- Consistency with other documents
- Compliance with standards and best practices

### 3. Approval

**Approval Authority:** {{ meta-handbook.approver }}

**Approval Criteria:**
- All reviews completed
- No open comments
- Quality criteria met
- Documentation standards adhered to

**Approval Process:**
1. Incorporate review comments
2. Create final version
3. Approval by {{ meta-handbook.approver }}
4. Increment version
5. Publication in repository

### 4. Publication

**Responsible:** {{ meta-handbook.owner }}

**Steps:**
1. Store document in central repository
2. Inform stakeholders
3. Archive old version
4. Publish change notice

## Approval Processes

### Standard Changes (Patch)

- **Approval:** Document Owner
- **Review:** Optional
- **Examples:** Typos, formatting, minor additions

### Normal Changes (Minor)

- **Approval:** {{ meta-handbook.approver }}
- **Review:** Department (Operations/Security)
- **Examples:** New sections, process changes

### Major Changes (Major)

- **Approval:** {{ meta-organisation-roles.role_cio.name }} ({{ meta-organisation-roles.role_cio.email }})
- **Review:** All departments + management
- **CAB Meeting:** Required
- **Examples:** Fundamental revisions, architecture changes

## Documentation Standards

### Language and Format

- **Language:** {{ meta-handbook.language }}
- **Format:** Markdown (.md)
- **Character Set:** UTF-8
- **Line Breaks:** Unix (LF)

### Required Fields

Every document MUST contain the following information:

- **Title:** Unique document title
- **Version:** According to SemVer
- **Date:** Last change (ISO 8601)
- **Author:** Responsible editor
- **Owner:** Document owner
- **Approval:** Approval authority
- **Classification:** Confidentiality level

### Structure Requirements

1. **Headings:** Hierarchical (# H1, ## H2, ### H3)
2. **Tables:** Markdown syntax with alignment
3. **Lists:** Numbered or bullet points
4. **Code:** Fenced code blocks with syntax highlighting
5. **Links:** Relative links preferred

### Linking

- **Internal Links:** Relative paths within repository
- **External Links:** Absolute URLs with description
- **References:** Unique identifiers for cross-references

### Metadata Placeholders

Use the following placeholders for organization-wide information:

- **Organization:** `{{ meta-organisation.name }}`
- **Roles:** `{{ meta-organisation-roles.role_ceo.name }}`, `{{ meta-organisation-roles.role_cio.name }}`, `{{ meta-organisation-roles.role_ciso.name }}`
- **Document:** `{{ meta-handbook.owner }}`, `{{ meta-handbook.approver }}`
- **Author:** `{{ meta-handbook.author }}`

## Document Classification

| Classification | Description | Access | Examples |
|---|---|---|---|
| **Public** | No restrictions | All | General information |
| **Internal** | Employees only | Employees | Operations handbooks, processes |
| **Confidential** | Restricted access | Authorized persons | Security concepts, passwords |
| **Strictly Confidential** | Highest confidentiality | Management + Authorized | Trade secrets, compliance |

**Current Classification:** {{ meta-handbook.classification }}

## Archiving and Retention

### Retention Periods

- **Current Version:** Unlimited in repository
- **Previous Versions:** Minimum 3 years
- **Drafts:** 1 year after release
- **Archived Documents:** According to retention policy

### Archiving Process

1. **Version Change:** Move old version to archive
2. **Metadata:** Document archiving date and reason
3. **Access:** Read access for authorized persons
4. **Deletion:** After retention period expires

## Responsibilities

| Role | Responsibility | Person |
|---|---|---|
| **Document Owner** | Overall responsibility, currency | {{ meta-handbook.owner }} |
| **Editor** | Content maintenance, changes | [Author] |
| **Approval Authority** | Approval of changes | {{ meta-handbook.approver }} |
| **CIO** | Strategic alignment | {{ meta-organisation-roles.role_cio.name }} |
| **CISO** | Security review | {{ meta-organisation-roles.role_ciso.name }} |

## Contacts

**For questions about document control:**
- **Document Owner:** {{ meta-handbook.owner }}
- **IT Operations Manager:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})
- **CIO:** {{ meta-organisation-roles.role_cio.name }} ({{ meta-organisation-roles.role_cio.email }})

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organization:** {{ meta-organisation.name }}
