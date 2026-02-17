# Configuration Reference

## Overview

The Handbook Generator uses a modular configuration system with separate files for different concerns:

- **config.yaml** - Data source references and system settings
- **meta-global.yaml** - Handbook Generator version information
- **meta-organisation.yaml** - Organization-specific information
- **meta-organisation-roles.yaml** - Personnel roles and responsibilities
- **meta-handbook.yaml** - Individual handbook metadata (per handbook)

All configuration files use YAML format and support inline comments for documentation.

## File Locations

```
project-root/
├── config.yaml                           # Main configuration
├── meta-global.yaml                      # Global metadata
├── meta-organisation.yaml                # Organization metadata
├── meta-organisation-roles.yaml          # Roles metadata
└── templates/
    ├── de/
    │   ├── bcm/
    │   │   ├── meta-handbook.yaml        # BCM handbook metadata
    │   │   └── ...
    │   └── isms/
    │       ├── meta-handbook.yaml        # ISMS handbook metadata
    │       └── ...
    └── en/
        └── (similar structure)
```

## Path Resolution

- All paths in `config.yaml` are resolved **relative to the config.yaml location**
- Handbook-specific `meta-handbook.yaml` files are located in each handbook's root directory
- Absolute paths are not supported for security reasons

## Version Control Recommendations

| File | Commit to Git? | Reason |
|------|----------------|--------|
| config.yaml | ❌ No | May contain API tokens and credentials |
| config.example.yaml | ✅ Yes | Template for other users |
| meta-global.yaml | ✅ Yes | No sensitive data |
| meta-organisation.yaml | ✅ Yes | No sensitive data (consider privacy) |
| meta-organisation-roles.yaml | ⚠️ Maybe | Consider privacy implications of personal names |
| meta-handbook.yaml | ✅ Yes | No sensitive data |

**Recommendation:** Add `config.yaml` to `.gitignore` and provide `config.example.yaml` for team members.

---

## config.yaml

Main configuration file containing data source references and system settings.

### Structure

```yaml
data_sources:
  meta-global: "meta-global.yaml"
  meta-organisation: "meta-organisation.yaml"
  meta-organisation-roles: "meta-organisation-roles.yaml"
  # Optional external sources
  netbox:
    url: "https://netbox.example.com"
    api_token: "xyz"
  verinice:
    url: "https://verinice.example.com"
    api_token: "xyz"

defaults:
  language: "de"
  output_format: "both"
```

### Fields

#### data_sources (required)

Container for all data source configurations.

##### data_sources.meta-global (required)

- **Type:** String (file path)
- **Default:** "meta-global.yaml"
- **Description:** Path to global metadata file (relative to config.yaml)
- **Example:** "meta-global.yaml", "config/meta-global.yaml"

##### data_sources.meta-organisation (required)

- **Type:** String (file path)
- **Default:** "meta-organisation.yaml"
- **Description:** Path to organization metadata file (relative to config.yaml)
- **Example:** "meta-organisation.yaml", "config/meta-organisation.yaml"

##### data_sources.meta-organisation-roles (required)

- **Type:** String (file path)
- **Default:** "meta-organisation-roles.yaml"
- **Description:** Path to roles metadata file (relative to config.yaml)
- **Example:** "meta-organisation-roles.yaml", "config/meta-organisation-roles.yaml"

##### data_sources.netbox (optional)

NetBox integration for network documentation and DCIM data.

- **Type:** Object
- **Default:** Not configured
- **Fields:**
  - `url` (string, required): NetBox instance URL
  - `api_token` (string, required): API authentication token
  - `verify_ssl` (boolean, optional): Verify SSL certificates (default: true)

**Example:**
```yaml
netbox:
  url: "https://netbox.example.com"
  api_token: "abc123def456"
  verify_ssl: true
```

##### data_sources.verinice (optional)

Verinice integration for GRC and compliance management data.

- **Type:** Object
- **Default:** Not configured
- **Fields:**
  - `url` (string, required): Verinice instance URL
  - `api_token` (string, required): API authentication token
  - `verify_ssl` (boolean, optional): Verify SSL certificates (default: true)

**Example:**
```yaml
verinice:
  url: "https://verinice.example.com"
  api_token: "xyz789abc123"
  verify_ssl: true
```

#### defaults (optional)

Default settings for handbook generation.

##### defaults.language (optional)

- **Type:** String
- **Default:** "de"
- **Valid Values:** "de" (German), "en" (English)
- **Description:** Default language for handbook generation
- **Example:** "de", "en"

##### defaults.output_format (optional)

- **Type:** String
- **Default:** "both"
- **Valid Values:** "markdown", "pdf", "both"
- **Description:** Default output format for generated handbooks
- **Example:** "markdown", "pdf", "both"

### Example

See `config.example.yaml` for a complete example with all options and inline documentation.

---

## meta-global.yaml

Global metadata containing Handbook Generator version and source information.

### Structure

```yaml
source: "HandBook Generator"
version: "1.0.0"
```

### Fields

#### source (required)

- **Type:** String
- **Default:** "HandBook Generator"
- **Description:** Identifier for the handbook generation system
- **Usage:** Appears in generated handbooks to identify the tool used
- **Example:** "HandBook Generator", "Custom Handbook System"

#### version (required)

- **Type:** String
- **Default:** "1.0.0"
- **Format:** Semantic versioning (MAJOR.MINOR.PATCH)
- **Description:** Version number of the Handbook Generator
- **Usage:** Should match the installed version of the generator
- **Example:** "1.0.0", "2.1.3", "0.9.0-beta"

### Default Values

If `meta-global.yaml` is missing, the system uses these defaults:
- source: "HandBook Generator"
- version: "1.0.0"

### Example

See `meta-global.example.yaml` for a complete example with optional fields and inline documentation.

---

## meta-organisation.yaml

Organization-specific information used across all handbooks.

### Structure

```yaml
name: "AdminsEnd Ltd."
address: "Endless Lane 42, DE-35813 LandsEnd"
web: "https://www.adminsend.de"
phone: "+49 2323 555 4242"
revision: 0
```

### Fields

#### name (required)

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Legal or common name of the organization
- **Usage:** Document headers, footers, throughout handbook content
- **Example:** "Acme Corporation", "TechStart GmbH", "Global Services Ltd."

#### address (required)

- **Type:** String
- **Default:** "[TODO]"
- **Format:** Free text (recommend: "Street Number, Postal Code City, Country")
- **Description:** Full postal address of the organization
- **Usage:** Document headers, contact information sections
- **Example:** "123 Main Street, 12345 New York, USA"

#### web (required)

- **Type:** String (URL)
- **Default:** "[TODO]"
- **Format:** Full URL including protocol (https://)
- **Description:** Primary website URL for the organization
- **Usage:** Contact information, document footers
- **Example:** "https://www.example.com"

#### phone (required)

- **Type:** String
- **Default:** "[TODO]"
- **Format:** International format recommended (e.g., +49 123 456789)
- **Description:** Primary contact phone number
- **Usage:** Contact information sections
- **Example:** "+1 555 123 4567", "+44 20 1234 5678"

#### revision (required)

- **Type:** Integer
- **Default:** 0
- **Description:** Manual revision counter for organization metadata changes
- **Usage:** Tracking significant changes to organization information
- **Note:** NOT automatically incremented - must be updated manually
- **Example:** 0, 1, 2, 3

### Default Values

If `meta-organisation.yaml` is missing, the system uses these defaults:
- name: "[TODO]"
- address: "[TODO]"
- web: "[TODO]"
- phone: "[TODO]"
- revision: 0

### Example

See `meta-organisation.example.yaml` for a complete example with optional fields and inline documentation.

---

## meta-organisation-roles.yaml

Personnel roles and contact information for the organization.

### Structure

```yaml
# Executive roles
role_CEO: "Jane Smith"
role_CFO: "John Doe"
role_CTO: "Alice Johnson"
role_CIO: "Bob Williams"
role_CISO: "Carol Martinez"

# Management roles
role_HR_Manager: "David Brown"
role_Risk_Manager: "Emma Davis"
role_GDPR_Manager: "Frank Wilson"
role_IT_Manager: "Grace Taylor"
role_Compliance_Manager: "Henry Anderson"
role_Internal_Auditor: "Isabel Thomas"

# Groups and teams
group_IT_Services: "IT Services Team"
group_DEVOPS: "DevOps Team"
group_Helpdesk: "Helpdesk Team"
```

### Naming Convention

**IMPORTANT:** All role identifiers MUST use English names for language-agnostic templates.

- Individual roles: `role_[Position]`
- Groups/Teams: `group_[Name]`
- Always use English identifiers (e.g., `role_CEO`, NOT `rolle_CEO`)

### Fields

#### Executive Roles

##### role_CEO

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Chief Executive Officer - Overall organizational leadership
- **Usage:** Strategic documents, governance handbooks, approval workflows
- **Example:** "Jane Smith", "J. Smith", "CEO Office"

##### role_CFO

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Chief Financial Officer - Financial management and oversight
- **Usage:** Financial policies, budget approvals, audit documents
- **Example:** "John Doe"

##### role_CTO

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Chief Technology Officer - Technology strategy and innovation
- **Usage:** Technology roadmaps, architecture decisions, R&D documents
- **Example:** "Alice Johnson"

##### role_CIO

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Chief Information Officer - IT operations and information management
- **Usage:** IT policies, system documentation, technology governance
- **Example:** "Bob Williams"

##### role_CISO

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Chief Information Security Officer - Information security leadership
- **Usage:** Security policies, ISMS documentation, incident response plans
- **Example:** "Carol Martinez"

#### Management Roles

##### role_HR_Manager

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Human Resources Manager - Personnel management and HR policies
- **Usage:** HR policies, employee handbooks, training documentation
- **Example:** "David Brown"

##### role_Risk_Manager

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Risk Manager - Enterprise risk management and mitigation
- **Usage:** Risk assessments, BCM documentation, compliance reports
- **Example:** "Emma Davis"

##### role_GDPR_Manager

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Data Protection Officer / GDPR Manager - Privacy and data protection
- **Usage:** GDPR documentation, privacy policies, data processing records
- **Example:** "Frank Wilson"

##### role_IT_Manager

- **Type:** String
- **Default:** "[TODO]"
- **Description:** IT Manager - Day-to-day IT operations management
- **Usage:** IT procedures, service management, operational documentation
- **Example:** "Grace Taylor"

##### role_Compliance_Manager

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Compliance Manager - Regulatory compliance and audit coordination
- **Usage:** Compliance frameworks, audit reports, regulatory documentation
- **Example:** "Henry Anderson"

##### role_Internal_Auditor

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Internal Auditor - Internal audit and quality assurance
- **Usage:** Audit plans, quality management, internal reviews
- **Example:** "Isabel Thomas"

#### Groups and Teams

##### group_IT_Services

- **Type:** String
- **Default:** "[TODO]"
- **Description:** IT Services Group - General IT services team
- **Usage:** Service documentation, responsibility matrices, escalation paths
- **Example:** "IT Services Team", "IT Department"

##### group_DEVOPS

- **Type:** String
- **Default:** "[TODO]"
- **Description:** DevOps Group - Development and operations team
- **Usage:** CI/CD documentation, deployment procedures, automation guides
- **Example:** "DevOps Team", "Platform Engineering"

##### group_Helpdesk

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Helpdesk Group - User support and helpdesk team
- **Usage:** Support procedures, ticket handling, user guides
- **Example:** "Helpdesk Team", "Service Desk"

### Default Values

If `meta-organisation-roles.yaml` is missing, the system uses "[TODO]" as the default for all roles.

### Privacy Considerations

- Consider using role titles instead of personal names for public documents
- Review data protection requirements before committing personal information
- Update this file when personnel changes occur

### Example

See `meta-organisation-roles.example.yaml` for a complete example with additional optional roles and inline documentation.

---

## meta-handbook.yaml

Handbook-specific metadata for individual handbooks. This file is placed in each handbook's root directory.

### Location

Place this file in the handbook directory:
- German handbooks: `templates/de/[handbook]/meta-handbook.yaml`
- English handbooks: `templates/en/[handbook]/meta-handbook.yaml`

Example:
- `templates/de/bcm/meta-handbook.yaml`
- `templates/en/isms/meta-handbook.yaml`

### Structure

```yaml
# Authorship and responsibility
author: "Jane Smith"
maintainer: "John Doe"  # Optional, defaults to author
owner: "Chief Information Security Officer"
approver: "Chief Information Officer"

# Classification and status
classification: "Internal"
status: "Draft"
type: "Handbook"

# Version and identification
templateset_version: "0.1"
revision: 0
shortname: "BCM"
longname: "Business Continuity Management Handbook"

# Dates and validity
creationdate: "2024-01-15"
modifydate: "2024-03-20"
valid_from: "2024-04-01"
next_review: "2025-04-01"

# Scope
scope: "This handbook applies to all employees and contractors..."
```

### Fields

#### Authorship and Responsibility

##### author (required)

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Primary author of the handbook
- **Usage:** Document headers, approval workflows, contact information
- **Example:** "Jane Smith", "IT Department", "Security Team"

##### maintainer (optional)

- **Type:** String
- **Default:** Defaults to `author` value if not specified
- **Description:** Person responsible for keeping the handbook up-to-date
- **Usage:** Maintenance schedules, update notifications, contact information
- **Example:** "John Doe", "Documentation Team"
- **Note:** Only specify if different from author

##### owner (required)

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Person or role with ultimate responsibility for the handbook
- **Usage:** Governance documentation, approval chains, accountability matrices
- **Example:** "Chief Information Security Officer", "IT Manager", "Risk Manager"

##### approver (required)

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Person or role who approves handbook changes and releases
- **Usage:** Approval workflows, change management, version control
- **Example:** "Chief Information Officer", "Management Board", "Quality Manager"

#### Classification and Status

##### classification (required)

- **Type:** String
- **Default:** "[TODO]"
- **Valid Values:** "Public", "Internal", "Confidential", "Restricted" (or custom values)
- **Description:** Security classification of the handbook content
- **Usage:** Document headers, access control, distribution lists
- **Example:** "Internal", "Confidential"

##### status (required)

- **Type:** String
- **Default:** "[TODO]"
- **Valid Values:** "Draft", "In Review", "Approved", "Published", "Archived" (or custom values)
- **Description:** Current lifecycle status of the handbook
- **Usage:** Document headers, workflow management, publication control
- **Example:** "Draft", "Published"

##### type (required)

- **Type:** String
- **Default:** "[TODO]"
- **Valid Values:** "Policy", "Procedure", "Guideline", "Standard", "Handbook" (or custom values)
- **Description:** Category or type of handbook
- **Usage:** Document organization, template selection, reporting
- **Example:** "Handbook", "Policy"

#### Version and Identification

##### templateset_version (required)

- **Type:** String
- **Default:** "0.1"
- **Format:** Semantic versioning (MAJOR.MINOR.PATCH)
- **Description:** Version of the template set used to generate this handbook
- **Usage:** Template compatibility, migration tracking, version control
- **Example:** "0.1", "1.0.0", "2.1.3"

##### revision (required)

- **Type:** Integer
- **Default:** 0
- **Description:** Manual revision counter for tracking handbook changes
- **Usage:** Document headers, change tracking, version history
- **Note:** NOT automatically incremented - must be updated manually
- **Example:** 0, 1, 2, 3

##### shortname (required)

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Brief identifier for the handbook (acronym or short code)
- **Usage:** File names, cross-references, navigation menus
- **Example:** "BCM", "ISMS", "IT-SEC", "GDPR"

##### longname (required)

- **Type:** String
- **Default:** "[TODO]"
- **Description:** Full descriptive name of the handbook
- **Usage:** Document titles, cover pages, table of contents
- **Example:** "Business Continuity Management Handbook", "Information Security Management System Documentation"

#### Dates and Validity

##### creationdate (required)

- **Type:** String (date)
- **Default:** "[TODO]"
- **Format:** ISO 8601 date (YYYY-MM-DD) recommended
- **Description:** Date when the handbook was first created
- **Usage:** Document history, audit trails, compliance reporting
- **Example:** "2024-01-15"

##### modifydate (required)

- **Type:** String (date)
- **Default:** "[TODO]"
- **Format:** ISO 8601 date (YYYY-MM-DD) recommended
- **Description:** Date when the handbook was last updated
- **Usage:** Document headers, change tracking, freshness indicators
- **Note:** Update this date whenever you make changes to the handbook
- **Example:** "2024-03-20"

##### valid_from (required)

- **Type:** String (date)
- **Default:** "[TODO]"
- **Format:** ISO 8601 date (YYYY-MM-DD) recommended
- **Description:** Date when the handbook becomes effective
- **Usage:** Compliance tracking, policy enforcement, transition planning
- **Example:** "2024-04-01"

##### next_review (required)

- **Type:** String (date)
- **Default:** "[TODO]"
- **Format:** ISO 8601 date (YYYY-MM-DD) recommended
- **Description:** Scheduled date for the next handbook review
- **Usage:** Review schedules, compliance tracking, maintenance planning
- **Note:** Set this to ensure regular handbook reviews (typically annually)
- **Example:** "2025-04-01"

#### Scope and Applicability

##### scope (required)

- **Type:** String (multi-line text)
- **Default:** "[TODO]"
- **Description:** Description of what the handbook covers and to whom it applies
- **Usage:** Document introduction, applicability statements, scope definitions
- **Example:** "This handbook applies to all employees and contractors involved in business continuity management activities."

### Default Values

If `meta-handbook.yaml` is missing for a handbook, the system uses these defaults:
- author: "[TODO]"
- classification: "[TODO]"
- status: "[TODO]"
- type: "[TODO]"
- templateset_version: "0.1"
- revision: 0
- shortname: "[TODO]"
- longname: "[TODO]"
- maintainer: (defaults to author value)
- owner: "[TODO]"
- approver: "[TODO]"
- creationdate: "[TODO]"
- modifydate: "[TODO]"
- valid_from: "[TODO]"
- next_review: "[TODO]"
- scope: "[TODO]"

### Special Behavior

**Maintainer Default:** If the `maintainer` field is not specified, it automatically defaults to the `author` value. Only specify `maintainer` if it differs from the author.

### Example

See `meta-handbook.example.yaml` for a complete example with optional fields and inline documentation.

---

## Default Values Summary

When configuration files are missing or fields are not specified, the system uses these default values:

| File | Field | Default Value | Notes |
|------|-------|---------------|-------|
| meta-global.yaml | source | "HandBook Generator" | Standard product name |
| meta-global.yaml | version | "1.0.0" | Semantic versioning start |
| meta-organisation.yaml | name | "[TODO]" | Explicit placeholder |
| meta-organisation.yaml | address | "[TODO]" | Explicit placeholder |
| meta-organisation.yaml | web | "[TODO]" | Explicit placeholder |
| meta-organisation.yaml | phone | "[TODO]" | Explicit placeholder |
| meta-organisation.yaml | revision | 0 | Start at zero |
| meta-organisation-roles.yaml | (all roles) | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | author | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | classification | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | status | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | type | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | templateset_version | "0.1" | Initial version |
| meta-handbook.yaml | revision | 0 | Start at zero |
| meta-handbook.yaml | shortname | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | longname | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | maintainer | (author value) | Defaults to author |
| meta-handbook.yaml | owner | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | approver | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | creationdate | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | modifydate | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | valid_from | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | next_review | "[TODO]" | Explicit placeholder |
| meta-handbook.yaml | scope | "[TODO]" | Explicit placeholder |

**Note:** The system will emit warnings for "[TODO]" values but will continue processing. Replace "[TODO]" values before publishing handbooks.

---

## Validation

The system validates configuration files during loading:

### YAML Syntax Validation

- Checks for valid YAML syntax
- Reports file name and line number for syntax errors
- Provides clear error messages with corrective actions

### Required Field Validation

- Verifies all required fields are present
- Reports missing fields with file name and field name
- Suggests corrective actions

### Field Type Validation

- Validates field types match expected types (string, integer, etc.)
- Reports type mismatches with expected vs actual type
- Provides examples of correct values

### Circular Reference Detection

- Detects circular file references in configuration
- Reports error and halts processing
- Prevents infinite loops

### TODO Value Warnings

- Detects "[TODO]" placeholder values
- Emits warnings but continues processing
- Helps identify incomplete configuration

---

## Error Handling

All configuration errors follow this format:

```
[ERROR|WARNING] [Component] [File:Line]: Message
  Context: Additional context information
  Suggestion: Corrective action
```

### Example Errors

**Missing Required Field:**
```
ERROR ConfigLoader meta-organisation.yaml:5: Missing required field 'name'
  Context: Field 'name' is required for organization metadata
  Suggestion: Add 'name: "Your Organization Name"' to meta-organisation.yaml
```

**Invalid YAML Syntax:**
```
ERROR ConfigLoader meta-global.yaml:3: Invalid YAML syntax
  Context: Expected ':' after key 'version'
  Suggestion: Check YAML syntax at line 3, ensure proper key: value format
```

**TODO Value Warning:**
```
WARNING PlaceholderProcessor template.md:15: TODO value found for 'meta-organisation.name'
  Context: Placeholder {{ meta-organisation.name }} resolved to "[TODO]"
  Suggestion: Update 'name' field in meta-organisation.yaml with actual value
```

---

## Best Practices

### 1. Use Example Files as Templates

Copy the `.example.yaml` files and customize them:

```bash
cp config.example.yaml config.yaml
cp meta-global.example.yaml meta-global.yaml
cp meta-organisation.example.yaml meta-organisation.yaml
cp meta-organisation-roles.example.yaml meta-organisation-roles.yaml
```

### 2. Keep Sensitive Data Secure

- Add `config.yaml` to `.gitignore` (contains API tokens)
- Commit example files but not actual configuration
- Use environment variables for sensitive values in CI/CD

### 3. Use Consistent Date Formats

- Use ISO 8601 format (YYYY-MM-DD) for all dates
- Ensures proper sorting and international compatibility
- Example: "2024-03-20"

### 4. Maintain Revision Numbers

- Manually increment revision numbers for significant changes
- Document changes in a change log
- Use semantic versioning for major updates

### 5. Regular Reviews

- Set `next_review` dates for all handbooks
- Review and update metadata annually
- Keep personnel roles current

### 6. Replace TODO Values

- Search for "[TODO]" in all configuration files
- Replace with actual values before publishing
- Use validation warnings to identify incomplete configuration

### 7. Document Custom Fields

- Add inline comments for custom fields
- Document valid values and usage
- Keep documentation up-to-date

---

## Troubleshooting

### Configuration Not Loading

**Problem:** Configuration files are not being loaded

**Solutions:**
1. Check file paths are relative to config.yaml location
2. Verify YAML syntax is correct (use a YAML validator)
3. Ensure file permissions allow reading
4. Check for circular references

### Placeholders Not Replaced

**Problem:** Placeholders appear as {{ ... }} in output

**Solutions:**
1. Verify placeholder format: `{{ meta-source.field }}`
2. Check field exists in corresponding metadata file
3. Ensure metadata file is loaded (check config.yaml references)
4. Look for typos in placeholder names

### TODO Warnings

**Problem:** System warns about [TODO] values

**Solutions:**
1. Search for "[TODO]" in all configuration files
2. Replace with actual values
3. If intentional, warnings can be ignored (system continues processing)

### Missing Handbook Metadata

**Problem:** Handbook-specific metadata not found

**Solutions:**
1. Create `meta-handbook.yaml` in handbook root directory
2. Copy from `meta-handbook.example.yaml` and customize
3. Verify file is named exactly `meta-handbook.yaml`
4. Check file is in correct location (handbook root, not subdirectory)

---

## Migration from Old Format

If you're migrating from the old `metadata.yaml` format, see the [Migration Guide](MIGRATION_GUIDE.md) for step-by-step instructions.

---

## See Also

- [Placeholder Reference](PLACEHOLDER_REFERENCE.md) - Complete list of all placeholders
- [Template Header Specification](TEMPLATE_HEADER_SPECIFICATION.md) - Document header format
- [Migration Guide](MIGRATION_GUIDE.md) - Migrating from old configuration format

---

## Support

For questions or issues with configuration:

1. Check this reference documentation
2. Review example files (*.example.yaml)
3. Check validation error messages for specific guidance
4. Consult the troubleshooting section above
