# Placeholder Reference

## Overview

Placeholders are template variables that get replaced with actual values during handbook generation. The Handbook Generator uses a unified, language-agnostic placeholder format that works identically in both German (de) and English (en) templates.

## Placeholder Format

All placeholders follow this format:

```
{{ meta-source.field }}
```

Where:
- `meta-source` is one of: `meta-global`, `meta-organisation`, `meta-organisation-roles`, `meta-handbook`
- `field` is the specific field name from the corresponding metadata file

### Examples

```markdown
{{ meta-global.version }}
{{ meta-organisation.name }}
{{ meta-organisation-roles.role_CEO }}
{{ meta-handbook.author }}
```

## Important Rules

1. **English Identifiers Only:** All placeholders use English identifiers, even in German templates
2. **Case Sensitive:** Field names are case-sensitive (e.g., `role_CEO` not `role_ceo`)
3. **Dot Notation:** Use dots to separate source and field (e.g., `meta-organisation.name`)
4. **Whitespace:** Spaces inside `{{ }}` are optional but recommended for readability
5. **Language-Agnostic:** Same placeholders work in both German and English templates

---

## meta-global Placeholders

Global metadata from `meta-global.yaml` - Handbook Generator version and source information.

### {{ meta-global.source }}

- **Description:** Identifier for the handbook generation system
- **Default Value:** "HandBook Generator"
- **Example Value:** "HandBook Generator"
- **Usage:** Appears in generated handbooks to identify the tool used
- **Common Locations:** Document footers, metadata sections

**Example:**
```markdown
This handbook was generated using {{ meta-global.source }}.
```

### {{ meta-global.version }}

- **Description:** Version number of the Handbook Generator
- **Default Value:** "1.0.0"
- **Example Value:** "1.0.0", "2.1.3"
- **Usage:** Identifies the generator version used to create the handbook
- **Common Locations:** Document footers, version information sections

**Example:**
```markdown
Generator Version: {{ meta-global.version }}
```

---

## meta-organisation Placeholders

Organization metadata from `meta-organisation.yaml` - Organization-specific information.

### {{ meta-organisation.name }}

- **Description:** Legal or common name of the organization
- **Default Value:** "[TODO]"
- **Example Value:** "AdminsEnd Ltd.", "Acme Corporation"
- **Usage:** Document headers, footers, throughout handbook content
- **Common Locations:** Document headers, contact information, title pages

**Example:**
```markdown
**Organisation:** {{ meta-organisation.name }}

This handbook is the property of {{ meta-organisation.name }}.
```

### {{ meta-organisation.address }}

- **Description:** Full postal address of the organization
- **Default Value:** "[TODO]"
- **Example Value:** "Endless Lane 42, DE-35813 LandsEnd"
- **Usage:** Contact information sections, document footers
- **Common Locations:** Contact pages, document footers

**Example:**
```markdown
**Address:** {{ meta-organisation.address }}
```

### {{ meta-organisation.web }}

- **Description:** Primary website URL for the organization
- **Default Value:** "[TODO]"
- **Example Value:** "https://www.adminsend.de"
- **Usage:** Contact information, document footers, external references
- **Common Locations:** Contact pages, document footers

**Example:**
```markdown
**Website:** {{ meta-organisation.web }}

For more information, visit {{ meta-organisation.web }}.
```

### {{ meta-organisation.phone }}

- **Description:** Primary contact phone number
- **Default Value:** "[TODO]"
- **Example Value:** "+49 2323 555 4242"
- **Usage:** Contact information sections
- **Common Locations:** Contact pages, emergency contact sections

**Example:**
```markdown
**Phone:** {{ meta-organisation.phone }}
```

### {{ meta-organisation.revision }}

- **Description:** Manual revision counter for organization metadata changes
- **Default Value:** 0
- **Example Value:** 0, 1, 2, 3
- **Usage:** Tracking significant changes to organization information
- **Common Locations:** Metadata sections, change tracking

**Example:**
```markdown
Organisation Metadata Revision: {{ meta-organisation.revision }}
```

---

## meta-organisation-roles Placeholders

Personnel roles from `meta-organisation-roles.yaml` - Roles and responsibilities.

### Executive Roles

#### {{ meta-organisation-roles.role_CEO }}

- **Description:** Chief Executive Officer - Overall organizational leadership
- **Default Value:** "[TODO]"
- **Example Value:** "Jane Smith"
- **Usage:** Strategic documents, governance handbooks, approval workflows
- **Common Locations:** Approval sections, responsibility matrices, governance documents

**Example:**
```markdown
**CEO:** {{ meta-organisation-roles.role_CEO }}

Approved by: {{ meta-organisation-roles.role_CEO }}
```

#### {{ meta-organisation-roles.role_CFO }}

- **Description:** Chief Financial Officer - Financial management and oversight
- **Default Value:** "[TODO]"
- **Example Value:** "John Doe"
- **Usage:** Financial policies, budget approvals, audit documents
- **Common Locations:** Financial sections, approval workflows

**Example:**
```markdown
**CFO:** {{ meta-organisation-roles.role_CFO }}
```

#### {{ meta-organisation-roles.role_CTO }}

- **Description:** Chief Technology Officer - Technology strategy and innovation
- **Default Value:** "[TODO]"
- **Example Value:** "Alice Johnson"
- **Usage:** Technology roadmaps, architecture decisions, R&D documents
- **Common Locations:** Technology strategy sections, architecture documents

**Example:**
```markdown
**CTO:** {{ meta-organisation-roles.role_CTO }}
```

#### {{ meta-organisation-roles.role_CIO }}

- **Description:** Chief Information Officer - IT operations and information management
- **Default Value:** "[TODO]"
- **Example Value:** "Bob Williams"
- **Usage:** IT policies, system documentation, technology governance
- **Common Locations:** IT policy sections, governance documents

**Example:**
```markdown
**CIO:** {{ meta-organisation-roles.role_CIO }}
```

#### {{ meta-organisation-roles.role_CISO }}

- **Description:** Chief Information Security Officer - Information security leadership
- **Default Value:** "[TODO]"
- **Example Value:** "Carol Martinez"
- **Usage:** Security policies, ISMS documentation, incident response plans
- **Common Locations:** Security sections, ISMS documents, incident response

**Example:**
```markdown
**CISO:** {{ meta-organisation-roles.role_CISO }}

Security incidents should be reported to {{ meta-organisation-roles.role_CISO }}.
```

### Management Roles

#### {{ meta-organisation-roles.role_HR_Manager }}

- **Description:** Human Resources Manager - Personnel management and HR policies
- **Default Value:** "[TODO]"
- **Example Value:** "David Brown"
- **Usage:** HR policies, employee handbooks, training documentation
- **Common Locations:** HR sections, personnel policies

**Example:**
```markdown
**HR Manager:** {{ meta-organisation-roles.role_HR_Manager }}
```

#### {{ meta-organisation-roles.role_Risk_Manager }}

- **Description:** Risk Manager - Enterprise risk management and mitigation
- **Default Value:** "[TODO]"
- **Example Value:** "Emma Davis"
- **Usage:** Risk assessments, BCM documentation, compliance reports
- **Common Locations:** Risk management sections, BCM documents

**Example:**
```markdown
**Risk Manager:** {{ meta-organisation-roles.role_Risk_Manager }}
```

#### {{ meta-organisation-roles.role_GDPR_Manager }}

- **Description:** Data Protection Officer / GDPR Manager - Privacy and data protection
- **Default Value:** "[TODO]"
- **Example Value:** "Frank Wilson"
- **Usage:** GDPR documentation, privacy policies, data processing records
- **Common Locations:** GDPR sections, privacy policies

**Example:**
```markdown
**Data Protection Officer:** {{ meta-organisation-roles.role_GDPR_Manager }}

For privacy concerns, contact {{ meta-organisation-roles.role_GDPR_Manager }}.
```

#### {{ meta-organisation-roles.role_IT_Manager }}

- **Description:** IT Manager - Day-to-day IT operations management
- **Default Value:** "[TODO]"
- **Example Value:** "Grace Taylor"
- **Usage:** IT procedures, service management, operational documentation
- **Common Locations:** IT operations sections, service management

**Example:**
```markdown
**IT Manager:** {{ meta-organisation-roles.role_IT_Manager }}
```

#### {{ meta-organisation-roles.role_Compliance_Manager }}

- **Description:** Compliance Manager - Regulatory compliance and audit coordination
- **Default Value:** "[TODO]"
- **Example Value:** "Henry Anderson"
- **Usage:** Compliance frameworks, audit reports, regulatory documentation
- **Common Locations:** Compliance sections, audit documents

**Example:**
```markdown
**Compliance Manager:** {{ meta-organisation-roles.role_Compliance_Manager }}
```

#### {{ meta-organisation-roles.role_Internal_Auditor }}

- **Description:** Internal Auditor - Internal audit and quality assurance
- **Default Value:** "[TODO]"
- **Example Value:** "Isabel Thomas"
- **Usage:** Audit plans, quality management, internal reviews
- **Common Locations:** Audit sections, quality management documents

**Example:**
```markdown
**Internal Auditor:** {{ meta-organisation-roles.role_Internal_Auditor }}
```

### Groups and Teams

#### {{ meta-organisation-roles.group_IT_Services }}

- **Description:** IT Services Group - General IT services team
- **Default Value:** "[TODO]"
- **Example Value:** "IT Services Team"
- **Usage:** Service documentation, responsibility matrices, escalation paths
- **Common Locations:** Service descriptions, contact information

**Example:**
```markdown
**IT Services:** {{ meta-organisation-roles.group_IT_Services }}

Contact {{ meta-organisation-roles.group_IT_Services }} for support.
```

#### {{ meta-organisation-roles.group_DEVOPS }}

- **Description:** DevOps Group - Development and operations team
- **Default Value:** "[TODO]"
- **Example Value:** "DevOps Team"
- **Usage:** CI/CD documentation, deployment procedures, automation guides
- **Common Locations:** DevOps sections, deployment procedures

**Example:**
```markdown
**DevOps Team:** {{ meta-organisation-roles.group_DEVOPS }}
```

#### {{ meta-organisation-roles.group_Helpdesk }}

- **Description:** Helpdesk Group - User support and helpdesk team
- **Default Value:** "[TODO]"
- **Example Value:** "Helpdesk Team"
- **Usage:** Support procedures, ticket handling, user guides
- **Common Locations:** Support sections, contact information

**Example:**
```markdown
**Helpdesk:** {{ meta-organisation-roles.group_Helpdesk }}

For technical support, contact {{ meta-organisation-roles.group_Helpdesk }}.
```

---

## meta-handbook Placeholders

Handbook-specific metadata from `meta-handbook.yaml` - Individual handbook information.

### Authorship and Responsibility

#### {{ meta-handbook.author }}

- **Description:** Primary author of the handbook
- **Default Value:** "[TODO]"
- **Example Value:** "Jane Smith", "IT Department"
- **Usage:** Document headers, approval workflows, contact information
- **Common Locations:** Document headers, authorship sections

**Example:**
```markdown
**Author:** {{ meta-handbook.author }}
```

#### {{ meta-handbook.maintainer }}

- **Description:** Person responsible for keeping the handbook up-to-date
- **Default Value:** Defaults to `author` value if not specified
- **Example Value:** "John Doe", "Documentation Team"
- **Usage:** Maintenance schedules, update notifications, contact information
- **Common Locations:** Maintenance sections, contact information

**Example:**
```markdown
**Maintainer:** {{ meta-handbook.maintainer }}

For updates, contact {{ meta-handbook.maintainer }}.
```

#### {{ meta-handbook.owner }}

- **Description:** Person or role with ultimate responsibility for the handbook
- **Default Value:** "[TODO]"
- **Example Value:** "Chief Information Security Officer"
- **Usage:** Governance documentation, approval chains, accountability matrices
- **Common Locations:** Document headers, governance sections

**Example:**
```markdown
**Owner:** {{ meta-handbook.owner }}
```

#### {{ meta-handbook.approver }}

- **Description:** Person or role who approves handbook changes and releases
- **Default Value:** "[TODO]"
- **Example Value:** "Chief Information Officer"
- **Usage:** Approval workflows, change management, version control
- **Common Locations:** Document headers, approval sections

**Example:**
```markdown
**Approved by:** {{ meta-handbook.approver }}
```

### Classification and Status

#### {{ meta-handbook.classification }}

- **Description:** Security classification of the handbook content
- **Default Value:** "[TODO]"
- **Example Value:** "Internal", "Confidential"
- **Usage:** Document headers, access control, distribution lists
- **Common Locations:** Document headers, classification sections

**Example:**
```markdown
**Classification:** {{ meta-handbook.classification }}
```

#### {{ meta-handbook.status }}

- **Description:** Current lifecycle status of the handbook
- **Default Value:** "[TODO]"
- **Example Value:** "Draft", "Published"
- **Usage:** Document headers, workflow management, publication control
- **Common Locations:** Document headers, status sections

**Example:**
```markdown
**Status:** {{ meta-handbook.status }}
```

#### {{ meta-handbook.type }}

- **Description:** Category or type of handbook
- **Default Value:** "[TODO]"
- **Example Value:** "Handbook", "Policy"
- **Usage:** Document organization, template selection, reporting
- **Common Locations:** Document headers, classification sections

**Example:**
```markdown
**Type:** {{ meta-handbook.type }}
```

### Version and Identification

#### {{ meta-handbook.templateset_version }}

- **Description:** Version of the template set used to generate this handbook
- **Default Value:** "0.1"
- **Example Value:** "0.1", "1.0.0"
- **Usage:** Template compatibility, migration tracking, version control
- **Common Locations:** Metadata sections, version information

**Example:**
```markdown
**Template Version:** {{ meta-handbook.templateset_version }}
```

#### {{ meta-handbook.revision }}

- **Description:** Manual revision counter for tracking handbook changes
- **Default Value:** 0
- **Example Value:** 0, 1, 2, 3
- **Usage:** Document headers, change tracking, version history
- **Common Locations:** Document headers, version sections

**Example:**
```markdown
**Revision:** {{ meta-handbook.revision }}
```

#### {{ meta-handbook.shortname }}

- **Description:** Brief identifier for the handbook (acronym or short code)
- **Default Value:** "[TODO]"
- **Example Value:** "BCM", "ISMS"
- **Usage:** File names, cross-references, navigation menus
- **Common Locations:** Headers, navigation, cross-references

**Example:**
```markdown
**Handbook:** {{ meta-handbook.shortname }}

See also: {{ meta-handbook.shortname }} Section 5
```

#### {{ meta-handbook.longname }}

- **Description:** Full descriptive name of the handbook
- **Default Value:** "[TODO]"
- **Example Value:** "Business Continuity Management Handbook"
- **Usage:** Document titles, cover pages, table of contents
- **Common Locations:** Title pages, headers, table of contents

**Example:**
```markdown
# {{ meta-handbook.longname }}

Welcome to the {{ meta-handbook.longname }}.
```

### Dates and Validity

#### {{ meta-handbook.creationdate }}

- **Description:** Date when the handbook was first created
- **Default Value:** "[TODO]"
- **Example Value:** "2024-01-15"
- **Usage:** Document history, audit trails, compliance reporting
- **Common Locations:** Metadata sections, document history

**Example:**
```markdown
**Created:** {{ meta-handbook.creationdate }}
```

#### {{ meta-handbook.modifydate }}

- **Description:** Date when the handbook was last updated
- **Default Value:** "[TODO]"
- **Example Value:** "2024-03-20"
- **Usage:** Document headers, change tracking, freshness indicators
- **Common Locations:** Document headers, update information

**Example:**
```markdown
**Last Update:** {{ meta-handbook.modifydate }}
```

#### {{ meta-handbook.valid_from }}

- **Description:** Date when the handbook becomes effective
- **Default Value:** "[TODO]"
- **Example Value:** "2024-04-01"
- **Usage:** Compliance tracking, policy enforcement, transition planning
- **Common Locations:** Validity sections, compliance information

**Example:**
```markdown
**Valid from:** {{ meta-handbook.valid_from }}
```

#### {{ meta-handbook.next_review }}

- **Description:** Scheduled date for the next handbook review
- **Default Value:** "[TODO]"
- **Example Value:** "2025-04-01"
- **Usage:** Review schedules, compliance tracking, maintenance planning
- **Common Locations:** Review schedules, maintenance sections

**Example:**
```markdown
**Next Review:** {{ meta-handbook.next_review }}
```

### Scope and Applicability

#### {{ meta-handbook.scope }}

- **Description:** Description of what the handbook covers and to whom it applies
- **Default Value:** "[TODO]"
- **Example Value:** "This handbook applies to all employees..."
- **Usage:** Document introduction, applicability statements, scope definitions
- **Common Locations:** Introduction sections, scope statements

**Example:**
```markdown
## Scope

{{ meta-handbook.scope }}
```

---

## Migration from Old Format

If you're migrating from the old placeholder format, use this mapping:

### Old Format → New Format

| Old Placeholder | New Placeholder | Notes |
|----------------|-----------------|-------|
| `{{ meta.organisation.name }}` | `{{ meta-organisation.name }}` | Hyphen instead of dot in source |
| `{{ meta.document.owner }}` | `{{ meta-handbook.owner }}` | Changed from `document` to `handbook` |
| `{{ meta.document.version }}` | `{{ meta-handbook.revision }}` | Changed from `version` to `revision` |
| `{{ meta.document.author }}` | `{{ meta-handbook.author }}` | Changed from `document` to `handbook` |
| `{{ meta.ceo.name }}` | `{{ meta-organisation-roles.role_CEO }}` | Moved to roles, English identifier |
| `{{ meta.cio.name }}` | `{{ meta-organisation-roles.role_CIO }}` | Moved to roles, English identifier |
| `{{ meta.ciso.name }}` | `{{ meta-organisation-roles.role_CISO }}` | Moved to roles, English identifier |
| `{{ metadata.version }}` | `{{ meta-global.version }}` | Changed to `meta-global` source |
| `{{ metadata.source }}` | `{{ meta-global.source }}` | Changed to `meta-global` source |
| `{{ metadata.author }}` | `{{ meta-handbook.author }}` | Changed to `meta-handbook` source |
| `{{ organisation.address }}` | `{{ meta-organisation.address }}` | Added `meta-` prefix |
| `{{ organisation.phone }}` | `{{ meta-organisation.phone }}` | Added `meta-` prefix |
| `{{ organisation.web }}` | `{{ meta-organisation.web }}` | Added `meta-` prefix |

### German Placeholders → English Placeholders

| Old German Placeholder | New English Placeholder | Notes |
|------------------------|-------------------------|-------|
| `{{ rolle_CEO }}` | `{{ meta-organisation-roles.role_CEO }}` | English identifier, added source |
| `{{ rolle_CIO }}` | `{{ meta-organisation-roles.role_CIO }}` | English identifier, added source |
| `{{ rolle_CISO }}` | `{{ meta-organisation-roles.role_CISO }}` | English identifier, added source |
| `{{ gruppe_IT }}` | `{{ meta-organisation-roles.group_IT_Services }}` | English identifier, added source |

---

## Common Patterns

### Standard Document Header

Most templates include a standard document header with these placeholders:

```markdown
**Document-ID:** [FRAMEWORK]-0010
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
```

### Contact Information Section

```markdown
## Contact Information

**Organisation:** {{ meta-organisation.name }}
**Address:** {{ meta-organisation.address }}
**Phone:** {{ meta-organisation.phone }}
**Website:** {{ meta-organisation.web }}

**IT Manager:** {{ meta-organisation-roles.role_IT_Manager }}
**CISO:** {{ meta-organisation-roles.role_CISO }}
**Helpdesk:** {{ meta-organisation-roles.group_Helpdesk }}
```

### Approval Section

```markdown
## Approvals

This handbook has been reviewed and approved by:

**Owner:** {{ meta-handbook.owner }}
**Approver:** {{ meta-handbook.approver }}
**Date:** {{ meta-handbook.modifydate }}
```

### Handbook Metadata Section

```markdown
## Handbook Information

**Title:** {{ meta-handbook.longname }}
**Short Name:** {{ meta-handbook.shortname }}
**Author:** {{ meta-handbook.author }}
**Maintainer:** {{ meta-handbook.maintainer }}
**Revision:** {{ meta-handbook.revision }}
**Status:** {{ meta-handbook.status }}
**Valid from:** {{ meta-handbook.valid_from }}
**Next Review:** {{ meta-handbook.next_review }}

### Scope

{{ meta-handbook.scope }}
```

---

## Troubleshooting

### Placeholder Not Replaced

**Problem:** Placeholder appears as `{{ ... }}` in output

**Solutions:**
1. Check placeholder format: `{{ meta-source.field }}`
2. Verify field exists in corresponding metadata file
3. Check for typos in placeholder name (case-sensitive)
4. Ensure metadata file is loaded (check config.yaml)

### TODO Value in Output

**Problem:** Output contains "[TODO]" instead of actual value

**Solutions:**
1. Update the corresponding metadata file with actual value
2. Check which metadata file contains the field:
   - `meta-global.yaml` for `meta-global.*`
   - `meta-organisation.yaml` for `meta-organisation.*`
   - `meta-organisation-roles.yaml` for `meta-organisation-roles.*`
   - `meta-handbook.yaml` for `meta-handbook.*`
3. Replace "[TODO]" with actual value

### Wrong Value Displayed

**Problem:** Placeholder shows unexpected value

**Solutions:**
1. Check the correct metadata file is being loaded
2. Verify handbook-specific metadata is in correct location
3. Check for multiple metadata files (handbook-specific overrides global)
4. Verify field name matches exactly (case-sensitive)

---

## Best Practices

### 1. Use Consistent Placeholders

Use the same placeholders across all templates for consistency:
- Always use `{{ meta-organisation.name }}` for organization name
- Always use `{{ meta-handbook.owner }}` for handbook owner
- Don't create custom variations

### 2. Document Custom Placeholders

If you add custom fields to metadata files:
- Document them in inline comments
- Add them to this reference guide
- Ensure they follow the naming convention

### 3. Test Placeholder Replacement

Before publishing:
- Generate a test handbook
- Search for `{{ ` in output (should find none)
- Search for `[TODO]` in output (replace with actual values)

### 4. Use Meaningful Default Values

When creating new handbooks:
- Replace "[TODO]" values immediately
- Use descriptive values, not just names
- Include contact information where relevant

### 5. Keep Placeholders Language-Agnostic

- Always use English identifiers in placeholders
- Don't translate placeholder names
- Translate only the values in metadata files

## Recommendations

### Placeholder Naming

- Use clear, descriptive field names
- Follow existing naming conventions
- Avoid abbreviations unless widely understood
- Use underscores for multi-word fields (e.g., `role_HR_Manager`)

### Metadata Organization

- Group related fields in the same metadata file
- Keep handbook-specific data in `meta-handbook.yaml`
- Keep organization-wide data in `meta-organisation.yaml`
- Don't duplicate data across multiple files

### Documentation

- Document the purpose of each placeholder
- Provide examples of expected values
- Note any special formatting requirements
- Keep documentation up-to-date when adding fields

---

## See Also

- [Configuration Reference](CONFIGURATION_REFERENCE.md) - Complete configuration file documentation
- [Template Header Specification](TEMPLATE_HEADER_SPECIFICATION.md) - Document header format
- [Migration Guide](MIGRATION_GUIDE.md) - Migrating from old placeholder format

---

## Support

For questions or issues with placeholders:

1. Check this reference documentation
2. Verify placeholder format: `{{ meta-source.field }}`
3. Check corresponding metadata file for field definition
4. Review error messages for specific guidance
5. Consult the troubleshooting section above
