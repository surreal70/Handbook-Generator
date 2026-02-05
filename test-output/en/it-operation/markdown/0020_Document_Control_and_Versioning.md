# Document Control and Versioning

## Document Metadata

| Field | Value |
|---|---|
| Document Title | IT Operations Handbook – AdminSend GmbH |
| Document ID | [TODO: Unique Document ID] |
| System/Service | [TODO: System/Service Name] |
| Owner | IT Operations Manager |
| Responsible Editor | Andreas Huemmer [andreas.huemmer@adminsend.de] |
| Approval Authority | CIO |
| Classification | internal |
| Storage Location | [TODO: Central Repository/Storage Location] |
| Organization | AdminSend GmbH |
| Location | München, Deutschland |

## Version History

| Version | Date | Author | Changes | Approval |
|---|---|---|---|---|
| 1.0.0 | [TODO: Date] | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial Version | CIO |
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

**Approval:** IT Operations Manager

### 2. Technical Review

**Reviewers:**
- **Operations:** Andreas Huemmer (andreas.huemmer@adminsend.de)
- **Architecture:** [TODO: Architecture Lead]
- **Security:** Thomas Weber (thomas.weber@adminsend.de)
- **Compliance:** [TODO: Compliance Lead]

**Review Criteria:**
- Technical correctness
- Completeness
- Consistency with other documents
- Compliance with standards and best practices

### 3. Approval

**Approval Authority:** CIO

**Approval Criteria:**
- All reviews completed
- No open comments
- Quality criteria met
- Documentation standards adhered to

**Approval Process:**
1. Incorporate review comments
2. Create final version
3. Approval by CIO
4. Increment version
5. Publication in repository

### 4. Publication

**Responsible:** IT Operations Manager

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

- **Approval:** CIO
- **Review:** Department (Operations/Security)
- **Examples:** New sections, process changes

### Major Changes (Major)

- **Approval:** Anna Schmidt (anna.schmidt@adminsend.de)
- **Review:** All departments + management
- **CAB Meeting:** Required
- **Examples:** Fundamental revisions, architecture changes

## Documentation Standards

### Language and Format

- **Language:** de
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

- **Organization:** `AdminSend GmbH`
- **Roles:** `Max Mustermann`, `Anna Schmidt`, `Thomas Weber`
- **Document:** `IT Operations Manager`, `CIO`
- **Author:** `Andreas Huemmer [andreas.huemmer@adminsend.de]`

## Document Classification

| Classification | Description | Access | Examples |
|---|---|---|---|
| **Public** | No restrictions | All | General information |
| **Internal** | Employees only | Employees | Operations handbooks, processes |
| **Confidential** | Restricted access | Authorized persons | Security concepts, passwords |
| **Strictly Confidential** | Highest confidentiality | Management + Authorized | Trade secrets, compliance |

**Current Classification:** internal

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
| **Document Owner** | Overall responsibility, currency | IT Operations Manager |
| **Editor** | Content maintenance, changes | Andreas Huemmer [andreas.huemmer@adminsend.de] |
| **Approval Authority** | Approval of changes | CIO |
| **CIO** | Strategic alignment | Anna Schmidt |
| **CISO** | Security review | Thomas Weber |

## Contacts

**For questions about document control:**
- **Document Owner:** IT Operations Manager
- **IT Operations Manager:** Andreas Huemmer (andreas.huemmer@adminsend.de)
- **CIO:** Anna Schmidt (anna.schmidt@adminsend.de)

---

**Document Owner:** IT Operations Manager  
**Approved by:** CIO  
**Version:** 1.0.0  
**Organization:** AdminSend GmbH
