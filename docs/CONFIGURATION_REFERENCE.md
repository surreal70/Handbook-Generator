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


---

## Service and Process Documentation Configuration

**Since Version 0.0.17**, the Handbook Generator supports structured documentation of IT services and business processes.

### Directory Structure

```
project-root/
├── services/
│   ├── de/
│   │   ├── meta-global-service.yaml      # Global service configuration
│   │   ├── generic-service-template/
│   │   │   ├── meta-service.yaml         # Service-specific configuration
│   │   │   └── service-template.md       # Service template
│   │   └── email-service/                # Example service
│   │       ├── meta-service.yaml
│   │       └── email-service.md
│   └── en/
│       └── (similar structure)
└── processes/
    ├── de/
    │   ├── meta-global-process.yaml      # Global process configuration
    │   ├── generic-process-template/
    │   │   ├── meta-process.yaml         # Process-specific configuration
    │   │   ├── diagrams/                 # BPMN diagrams
    │   │   └── process-template.md       # Process template
    │   └── incident-management/          # Example process
    │       ├── meta-process.yaml
    │       ├── diagrams/
    │       └── incident-management.md
    └── en/
        └── (similar structure)
```

### meta-global-service.yaml

Global configuration for all services. Provides default values that can be overridden by service-specific configurations.

#### Structure

```yaml
# Default SLA values
sla:
  availability_target: "99.5%"
  response_time_p1: "15 minutes"
  response_time_p2: "4 hours"
  response_time_p3: "24 hours"
  response_time_p4: "5 business days"
  
# Support hours
support:
  business_hours: "Mo-Fr 08:00-18:00 CET"
  extended_hours: "Mo-Fr 06:00-22:00 CET"
  maintenance_window: "Sa 02:00-06:00 CET"
  
# Escalation paths
escalation:
  level_1: "{{ group_Helpdesk }}"
  level_2: "{{ role_IT_Manager }}"
  level_3: "{{ role_CIO }}"
  level_4: "{{ role_CEO }}"
  
# Compliance frameworks
compliance:
  cobit_version: "COBIT 2019"
  itil_version: "ITIL 4"
  iso_27001: true
  
# Service categories
categories:
  - infrastructure
  - application
  - business
  - security
  - support
```

#### Fields

##### sla (optional)

Default SLA values for all services.

- **availability_target:** Target availability percentage (e.g., "99.5%", "99.9%")
- **response_time_p1:** Response time for P1 (Critical) incidents
- **response_time_p2:** Response time for P2 (High) incidents
- **response_time_p3:** Response time for P3 (Medium) incidents
- **response_time_p4:** Response time for P4 (Low) incidents

##### support (optional)

Default support hours and maintenance windows.

- **business_hours:** Standard business hours (e.g., "Mo-Fr 08:00-18:00 CET")
- **extended_hours:** Extended support hours (e.g., "Mo-Fr 06:00-22:00 CET")
- **maintenance_window:** Standard maintenance window (e.g., "Sa 02:00-06:00 CET")

##### escalation (optional)

Default escalation paths. Can reference roles from meta-organisation-roles.yaml.

- **level_1:** First escalation level (e.g., "{{ group_Helpdesk }}")
- **level_2:** Second escalation level (e.g., "{{ role_IT_Manager }}")
- **level_3:** Third escalation level (e.g., "{{ role_CIO }}")
- **level_4:** Fourth escalation level (e.g., "{{ role_CEO }}")

##### compliance (optional)

Compliance framework versions and flags.

- **cobit_version:** COBIT version (e.g., "COBIT 2019")
- **itil_version:** ITIL version (e.g., "ITIL 4")
- **iso_27001:** ISO 27001 compliance flag (true/false)

##### categories (optional)

List of valid service categories.

- infrastructure
- application
- business
- security
- support

### meta-service.yaml

Service-specific configuration. Overrides global defaults from meta-global-service.yaml.

#### Structure

```yaml
service:
  id: "SVC-001"
  name: "Email Service"
  category: "infrastructure"
  criticality: "High"
  status: "Production"
  classification: "Internal"
  revision: 1
  modifydate: "2025-02-19"
  
  # Role references from meta-organisation-roles.yaml
  owner: "role_IT_Manager"
  manager: "role_IT_Manager"
  approver: "role_CIO"
  
  # Service-specific SLA (overrides global)
  sla:
    availability_target: "99.9%"
    response_time_p1: "10 minutes"
    
  # Technology stack
  technology:
    platform: "Microsoft Exchange Online"
    backup: "Veeam Backup for Office 365"
    monitoring: "Zabbix"
    
  # COBIT mapping
  cobit:
    processes:
      - "DSS01 - Manage Operations"
      - "DSS02 - Manage Service Requests"
      
  # ITIL lifecycle
  itil:
    lifecycle_phase: "Service Operation"
    processes:
      - "Incident Management"
      - "Problem Management"
```

#### Fields

##### service.id (required)

Unique service identifier.

- **Format:** "SVC-<CATEGORY>-<NUMBER>" (e.g., "SVC-INFRA-001")
- **Example:** "SVC-001", "SVC-EMAIL-001", "SVC-INFRA-001"

##### service.name (required)

Service name.

- **Example:** "Email Service", "ERP System", "Firewall Service"

##### service.category (required)

Service category. Must be one of the categories defined in meta-global-service.yaml.

- **Values:** infrastructure, application, business, security, support

##### service.criticality (required)

Service criticality level.

- **Values:** Critical, High, Medium, Low

##### service.status (required)

Current service status.

- **Values:** Production, Development, Testing, Retired

##### service.classification (required)

Data classification level.

- **Values:** Public, Internal, Confidential, Restricted

##### service.revision (required)

Document revision number.

- **Type:** Integer
- **Example:** 1, 2, 3

##### service.modifydate (required)

Last modification date.

- **Format:** "YYYY-MM-DD"
- **Example:** "2025-02-19"

##### service.owner (required)

Service owner role reference.

- **Format:** Role reference from meta-organisation-roles.yaml
- **Example:** "role_IT_Manager", "role_CIO"

##### service.manager (required)

Service manager role reference.

- **Format:** Role reference from meta-organisation-roles.yaml
- **Example:** "role_IT_Manager", "role_Service_Manager"

##### service.approver (required)

Service approver role reference.

- **Format:** Role reference from meta-organisation-roles.yaml
- **Example:** "role_CIO", "role_CEO"

##### service.sla (optional)

Service-specific SLA values. Overrides global defaults.

- **availability_target:** Target availability (e.g., "99.9%")
- **response_time_p1:** P1 response time (e.g., "10 minutes")
- **response_time_p2:** P2 response time (e.g., "2 hours")
- **response_time_p3:** P3 response time (e.g., "8 hours")
- **response_time_p4:** P4 response time (e.g., "2 business days")

##### service.technology (optional)

Technology stack information.

- **platform:** Primary platform (e.g., "Microsoft Exchange Online")
- **backup:** Backup solution (e.g., "Veeam Backup for Office 365")
- **monitoring:** Monitoring tool (e.g., "Zabbix")
- Additional fields as needed

##### service.cobit (optional)

COBIT framework mapping.

- **processes:** List of COBIT processes (e.g., ["DSS01 - Manage Operations"])
- **controls:** List of COBIT controls (e.g., ["DSS01.01 - Perform operational procedures"])

##### service.itil (optional)

ITIL framework mapping.

- **lifecycle_phase:** ITIL lifecycle phase (e.g., "Service Operation")
- **processes:** List of ITIL processes (e.g., ["Incident Management", "Problem Management"])

### meta-global-process.yaml

Global configuration for all processes. Provides default values that can be overridden by process-specific configurations.

#### Structure

```yaml
# Standard escalation
escalation:
  level_1: "{{ role_IT_Manager }}"
  level_2: "{{ role_Risk_Manager }}"
  level_3: "{{ role_CIO }}"
  level_4: "{{ role_CEO }}"
  
# Compliance frameworks
compliance:
  iso_27001: true
  bsi_grundschutz: true
  gdpr: true
  
# Standard KPIs
kpis:
  process_efficiency: "Cycle time reduction"
  quality: "Error rate"
  compliance: "Audit findings"
  
# Process categories
categories:
  - core
  - support
  - management
  
# Standard control points
controls:
  - "Management approval"
  - "Four-eyes principle"
  - "Audit trail"
```

#### Fields

##### escalation (optional)

Default escalation paths for processes.

- **level_1:** First escalation level
- **level_2:** Second escalation level
- **level_3:** Third escalation level
- **level_4:** Fourth escalation level

##### compliance (optional)

Compliance framework flags.

- **iso_27001:** ISO 27001 compliance (true/false)
- **bsi_grundschutz:** BSI IT-Grundschutz compliance (true/false)
- **gdpr:** GDPR compliance (true/false)

##### kpis (optional)

Standard KPI definitions.

- **process_efficiency:** Efficiency metric description
- **quality:** Quality metric description
- **compliance:** Compliance metric description

##### categories (optional)

List of valid process categories.

- core
- support
- management

##### controls (optional)

List of standard control points.

- "Management approval"
- "Four-eyes principle"
- "Audit trail"

### meta-process.yaml

Process-specific configuration. Overrides global defaults from meta-global-process.yaml.

#### Structure

```yaml
process:
  id: "PROC-001"
  name: "Incident Management"
  category: "core"
  criticality: "Critical"
  status: "Active"
  classification: "Internal"
  revision: 2
  modifydate: "2025-02-19"
  
  # Role references from meta-organisation-roles.yaml
  owner: "role_IT_Manager"
  manager: "role_IT_Manager"
  approver: "role_CIO"
  
  # Process-specific SLA
  sla:
    p1_resolution: "4 hours"
    p2_resolution: "24 hours"
    p3_resolution: "5 business days"
    
  # Systems used
  systems:
    - "ServiceNow"
    - "Zabbix"
    - "Slack"
    
  # RACI roles
  raci:
    incident_detection:
      responsible: "role_System_Administrator"
      accountable: "role_IT_Manager"
      consulted: "role_CISO"
      informed: "role_CIO"
      
  # Compliance requirements
  compliance:
    frameworks:
      - "ISO 27001:2022 - Clause 5.24"
      - "BSI IT-Grundschutz - DER.2.1"
    sod_rules:
      - "Incident handler cannot approve own escalations"
      
  # KPIs
  kpis:
    mttr: "Mean Time To Resolve"
    mtbf: "Mean Time Between Failures"
```

#### Fields

##### process.id (required)

Unique process identifier.

- **Format:** "PROC-<CATEGORY>-<NUMBER>" (e.g., "PROC-INC-001")
- **Example:** "PROC-001", "PROC-INC-001", "PROC-CHG-001"

##### process.name (required)

Process name.

- **Example:** "Incident Management", "Change Management", "Backup and Recovery"

##### process.category (required)

Process category. Must be one of the categories defined in meta-global-process.yaml.

- **Values:** core, support, management

##### process.criticality (required)

Process criticality level.

- **Values:** Critical, High, Medium, Low

##### process.status (required)

Current process status.

- **Values:** Active, Draft, Retired

##### process.classification (required)

Data classification level.

- **Values:** Public, Internal, Confidential, Restricted

##### process.revision (required)

Document revision number.

- **Type:** Integer
- **Example:** 1, 2, 3

##### process.modifydate (required)

Last modification date.

- **Format:** "YYYY-MM-DD"
- **Example:** "2025-02-19"

##### process.owner (required)

Process owner role reference.

- **Format:** Role reference from meta-organisation-roles.yaml
- **Example:** "role_IT_Manager", "role_Risk_Manager"

##### process.manager (required)

Process manager role reference.

- **Format:** Role reference from meta-organisation-roles.yaml
- **Example:** "role_IT_Manager", "role_Process_Manager"

##### process.approver (required)

Process approver role reference.

- **Format:** Role reference from meta-organisation-roles.yaml
- **Example:** "role_CIO", "role_CEO"

##### process.sla (optional)

Process-specific SLA values.

- **p1_resolution:** P1 resolution time (e.g., "4 hours")
- **p2_resolution:** P2 resolution time (e.g., "24 hours")
- **p3_resolution:** P3 resolution time (e.g., "5 business days")
- **p4_resolution:** P4 resolution time (e.g., "10 business days")

##### process.systems (optional)

List of systems used in the process.

- **Example:** ["ServiceNow", "Zabbix", "Slack"]

##### process.raci (optional)

RACI matrix definitions for process steps.

Each process step can have:
- **responsible:** Role reference (who executes)
- **accountable:** Role reference (who is accountable)
- **consulted:** Role reference (who is consulted)
- **informed:** Role reference (who is informed)

**Example:**
```yaml
raci:
  incident_detection:
    responsible: "role_System_Administrator"
    accountable: "role_IT_Manager"
    consulted: "role_CISO"
    informed: "role_CIO"
```

##### process.compliance (optional)

Compliance requirements.

- **frameworks:** List of compliance frameworks (e.g., ["ISO 27001:2022 - Clause 5.24"])
- **sod_rules:** List of Segregation of Duties rules (e.g., ["Incident handler cannot approve own escalations"])

##### process.kpis (optional)

Process-specific KPIs.

- **Example:** {"mttr": "Mean Time To Resolve", "mtbf": "Mean Time Between Failures"}

### Placeholder Resolution Hierarchy

Placeholders are resolved in the following priority order (highest to lowest):

#### For Services

1. `meta-service.yaml` (service-specific)
2. `meta-global-service.yaml` (global for all services)
3. `meta-organisation-roles.yaml` (roles)
4. `meta-organisation.yaml` (organization)
5. `meta-global.yaml` (generator)

#### For Processes

1. `meta-process.yaml` (process-specific)
2. `meta-global-process.yaml` (global for all processes)
3. `meta-organisation-roles.yaml` (roles)
4. `meta-organisation.yaml` (organization)
5. `meta-global.yaml` (generator)

### CLI Usage

#### Generate Service Documentation

```bash
# German service
./handbook-generator --language de --service generic-service-template --test

# English service
./handbook-generator --language en --service email-service --test

# With all output formats
./handbook-generator -l de --service email-service -o all --test --separate-files --pdf-toc
```

#### Generate Process Documentation

```bash
# German process
./handbook-generator --language de --process generic-process-template --test

# English process
./handbook-generator --language en --process incident-management --test

# With all output formats
./handbook-generator -l de --process incident-management -o all --test --separate-files --pdf-toc
```

### Best Practices

1. **Use Global Defaults:** Define common values in meta-global-service.yaml and meta-global-process.yaml
2. **Override Selectively:** Only override values in meta-service.yaml and meta-process.yaml when needed
3. **Role References:** Always use role references (e.g., "role_IT_Manager") instead of direct names
4. **Consistent IDs:** Use consistent ID formats (SVC-<CATEGORY>-<NUMBER>, PROC-<CATEGORY>-<NUMBER>)
5. **Bilingual Consistency:** Keep German and English versions synchronized
6. **Version Control:** Track all metadata files in version control
7. **Documentation:** Document custom fields and their purpose

### Related Documentation

- **[SERVICE_DOCUMENTATION_GUIDE.md](SERVICE_DOCUMENTATION_GUIDE.md)** - Service documentation guide
- **[PROCESS_DOCUMENTATION_GUIDE.md](PROCESS_DOCUMENTATION_GUIDE.md)** - Process documentation guide
- **[PLACEHOLDER_STRUCTURE.md](PLACEHOLDER_STRUCTURE.md)** - Placeholder hierarchy and resolution
- **[METADATA_REFERENCE.md](METADATA_REFERENCE.md)** - Metadata field reference

---
