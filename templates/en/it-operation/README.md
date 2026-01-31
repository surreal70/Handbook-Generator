# IT-Operations Handbook Templates

## Overview

This template collection provides a comprehensive structure for IT operations handbooks based on best practices from ITIL v4, ISO 20000, and COBIT 2019. The templates cover all essential aspects of IT operations and enable the creation of professional, standards-compliant operational documentation.

## Template Structure

The templates are numbered in a logical sequence (0010-0290) and cover the following topic areas:

### Fundamentals (0010-0060)

| Template | Description | Framework Reference |
|---|---|---|
| **0010_Introduction.md** | Purpose, scope, and target audience of the handbook | - |
| **0011_Framework_Conditions.md** | Organizational and technical framework conditions | - |
| **0020_Document_Control_and_Versioning.md** | Version control, change history, approval processes | ISO 20000: 6.1 |
| **0030_Service_Description_and_Criticality.md** | Service definition, criticality assessment, SLA/SLO | ISO 20000: 8.2, 8.3 |
| **0040_System_Overview_and_Architecture.md** | Technical architecture, components, dependencies | COBIT: BAI03 |
| **0050_Infrastructure_and_Platform.md** | Hardware, virtualization, cloud resources, network | - |
| **0060_Roles_and_Responsibilities.md** | RACI matrix, contacts, escalation paths | COBIT: APO07 |

### Operational Processes (0070-0110)

| Template | Description | Framework Reference |
|---|---|---|
| **0070_Operating_Concept_and_Processes.md** | Operating models, ITIL processes, interfaces | ITIL: Service Design, COBIT: APO01 |
| **0080_Operations_Handover_and_GoLive_Checklist.md** | Go-live checklist, handover documentation | - |
| **0090_Configuration_Management_and_CMDB.md** | CI management, CMDB structure, change processes | ITIL: Service Configuration Management, COBIT: BAI10 |
| **0100_Access_and_Permission_Management.md** | Access control, RBAC, permission concept | ITIL: Service Desk |
| **0110_Monitoring_Alerting_and_Observability.md** | Monitoring concepts, alerting rules, dashboards | ITIL: Monitoring and Event Management |

### Service Management (0120-0160)

| Template | Description | Framework Reference |
|---|---|---|
| **0120_Incident_Management_Runbook.md** | Incident handling, escalation, standard runbooks | ITIL: Incident Management, COBIT: DSS02 |
| **0130_Problem_Management_and_Postmortems.md** | Root cause analysis, known error database | ITIL: Problem Management, COBIT: DSS03 |
| **0140_Change_and_Release_Management.md** | Change categories, CAB processes, deployment | ITIL: Change Enablement, Release Management, COBIT: BAI06 |
| **0150_Backup_and_Restore.md** | Backup strategies, RPO/RTO, restore procedures | ITIL: Service Continuity Management |
| **0160_Disaster_Recovery_and_Business_Continuity.md** | DR scenarios, failover/failback, BC plans | ITIL: Service Continuity Management, ISO 20000: 8.5, COBIT: APO12, DSS04 |

### Security & Compliance (0170-0190, 0280)

| Template | Description | Framework Reference |
|---|---|---|
| **0170_Security_Operations_and_Hardening.md** | Hardening guidelines, security monitoring, compliance | ISO 20000: 8.8, COBIT: APO13, DSS05 |
| **0180_Patch_and_Update_Management.md** | Patch categories, maintenance windows, vulnerability scanning | - |
| **0190_Log_Management_and_Audit.md** | Log collection, retention policies, SIEM integration | - |
| **0280_Compliance_and_Audits.md** | Standards (ISO 27001, GDPR, SOX), audit processes | COBIT: DSS06 |

### Operations & Support (0200-0270, 0290)

| Template | Description | Framework Reference |
|---|---|---|
| **0200_Capacity_and_Performance_Management.md** | Capacity planning, performance monitoring, scaling | ITIL: Capacity and Performance Management, ISO 20000: 8.7, COBIT: APO09 |
| **0210_Availability_and_Service_Level.md** | Availability requirements, SLA definitions, reporting | ITIL: Availability Management, ISO 20000: 8.3, 8.4 |
| **0220_Data_Management_and_Privacy.md** | Data classification, GDPR requirements, data governance | - |
| **0230_Maintenance_and_Operations_Routines.md** | Regular maintenance tasks, housekeeping procedures | COBIT: DSS01 |
| **0240_Runbooks_Standard_Operations.md** | Standard runbooks, step-by-step instructions | - |
| **0250_Tooling_and_Access_Methods.md** | Tools used, access methods, authentication | - |
| **0260_Known_Issues_and_FAQ.md** | Known issues, workarounds, troubleshooting tips | - |
| **0270_Contacts_Escalation_and_Vendors.md** | Contact lists, escalation paths, support contacts | - |
| **0290_Appendix_Checklists_and_Templates.md** | Checklist collection, templates, forms | - |

## Placeholder Usage

The templates support two types of placeholders for dynamic content:

### Meta Placeholders (Organization-wide Metadata)

Meta placeholders are populated from the `metadata.yaml` configuration file:

```markdown
**Organization:** {{ meta.organization.name }}
**Location:** {{ meta.organization.city }}, {{ meta.organization.country }}
**Website:** {{ meta.organization.website }}

**CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
**CISO:** {{ meta.ciso.name }} ({{ meta.ciso.email }})
**IT Operations Manager:** {{ meta.it_operations_manager.name }}
```

**Available Meta Fields:**

**Organization:**
- `{{ meta.organization.name }}` - Organization name
- `{{ meta.organization.address }}` - Address
- `{{ meta.organization.city }}` - City
- `{{ meta.organization.postal_code }}` - Postal code
- `{{ meta.organization.country }}` - Country
- `{{ meta.organization.website }}` - Website
- `{{ meta.organization.phone }}` - Phone
- `{{ meta.organization.email }}` - Email

**Roles (ceo, cio, ciso, cfo, coo, it_operations_manager, service_desk_lead):**
- `{{ meta.ROLE.name }}` - Person's name
- `{{ meta.ROLE.title }}` - Title/position
- `{{ meta.ROLE.email }}` - Email address
- `{{ meta.ROLE.phone }}` - Phone number
- `{{ meta.ROLE.department }}` - Department (optional)

**Document:**
- `{{ meta.document.owner }}` - Document owner
- `{{ meta.document.approver }}` - Approver
- `{{ meta.document.version }}` - Version
- `{{ meta.document.classification }}` - Classification

### NetBox Placeholders (Infrastructure Data)

NetBox placeholders are populated from the NetBox CMDB:

```markdown
**Site:** {{ netbox.site.name }}
**Address:** {{ netbox.site.physical_address }}
**Data Center:** {{ netbox.site.facility }}

**Core Switch:** {{ netbox.device.core_switch.name }}
**Management VLAN:** {{ netbox.vlan.management.vid }}
**Hypervisor Cluster:** {{ netbox.cluster.name }}
```

## Best Practices for Template Customization

### 1. Template Individualization

**Copy templates for specific services:**
```bash
# Example: Individual template for a specific service
cp templates/en/service-templates/service_description_template.md \
   my-service/service_description_my_app.md
```

**Replace [TODO] markers:**
- All templates contain `[TODO]` markers for customizable sections
- Replace these with service-specific information
- Maintain the structure and headings

### 2. Completing RACI Matrices

**Complete RACI matrices are essential:**
```markdown
| Activity | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Operations & Monitoring | A | C | R | I |
| Incident Management | A | C | R | R |
| Change Management | A | C | R | I |
```

**RACI Legend:**
- **R** (Responsible) - Performs the activity
- **A** (Accountable) - Has overall responsibility
- **C** (Consulted) - Is consulted
- **I** (Informed) - Is informed

**Best Practices:**
- Each activity must have exactly one "A"
- At least one "R" per activity
- Avoid too many "C" (decision delays)

### 3. Including Framework References

**Reference relevant standards:**
```markdown
## Compliance Requirements

This process meets the following standards:
- **ITIL v4:** Incident Management Practice
- **ISO 20000-1:2018:** Clause 8.6 (Incident Management)
- **COBIT 2019:** DSS02 (Managed Service Requests and Incidents)
```

### 4. Using Placeholders Consistently

**Use placeholders for recurring information:**
```markdown
<!-- Good: Placeholder for organization name -->
**Organization:** {{ meta.organization.name }}

<!-- Bad: Hardcoded value -->
**Organization:** AdminSend GmbH
```

**Advantages:**
- Central management in metadata.yaml
- Consistency across all handbooks
- Easy updates when changes occur

### 5. Versioning and Change History

**Maintain change history:**
```markdown
## Change History

| Version | Date | Author | Changes | Approved by |
|---|---|---|---|---|
| 1.0.0 | 2024-01-15 | {{ meta.author }} | Initial version | {{ meta.document.approver }} |
| 1.1.0 | 2024-02-20 | {{ meta.author }} | Extended monitoring section | {{ meta.document.approver }} |
```

### 6. Service Level Definitions

**Define measurable SLAs:**
```markdown
| Metric | Target | Measurement Method | Responsible |
|---|---:|---|---|
| Availability | 99.9% | Uptime monitoring | {{ meta.it_operations_manager.name }} |
| Response time | < 200ms | APM tool | {{ meta.it_operations_manager.name }} |
| MTTR | < 4h | Incident tracking | {{ meta.service_desk_lead.name }} |
```

## Generating Handbooks

### Generate Complete IT-Operations Handbook

```bash
# German handbook
python -m src.cli --language de --template it-operation --output-format both

# English handbook
python -m src.cli --language en --template it-operation --output-format both
```

### Create Service-Specific Handbook

```bash
# 1. Copy and customize service template
cp templates/en/service-templates/service_description_template.md \
   my-service/service_description.md

# 2. Replace [TODO] markers
# 3. Generate handbook
python -m src.cli --language en --template my-service --output-format both
```

### Output Formats

- `--output-format markdown` - Markdown files only
- `--output-format pdf` - PDF files only
- `--output-format both` - Markdown and PDF

## Configuration

### Creating metadata.yaml

```bash
# Copy the example configuration
cp metadata.example.yaml metadata.yaml

# Edit the file with your organization data
nano metadata.yaml
```

### Minimal metadata.yaml

```yaml
organization:
  name: "Your Organization"
  address: "Your Address"
  city: "Your City"
  postal_code: "12345"
  country: "Germany"
  website: "https://www.your-domain.com"
  phone: "+49 123 456789"
  email: "info@your-domain.com"

roles:
  cio:
    name: "CIO Name"
    title: "Chief Information Officer"
    email: "cio@your-domain.com"
    phone: "+49 123 456789-100"

document:
  owner: "IT Operations Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"
```

## Framework Compliance

### ITIL v4 Process Coverage

The templates cover the following ITIL v4 Service Management Practices:

- **Service Design** - Operating concept and processes
- **Monitoring and Event Management** - Monitoring and alerting
- **Incident Management** - Incident handling
- **Problem Management** - Root cause analysis
- **Change Enablement** - Change control
- **Release Management** - Release planning
- **Service Configuration Management** - CMDB and CI management
- **Service Continuity Management** - Backup, DR, BC
- **Availability Management** - Availability management
- **Capacity and Performance Management** - Capacity planning

### ISO 20000-1:2018 Compliance

The templates support the following ISO 20000 requirements:

- **6.1** Service Planning - Operating concept
- **8.2** Service Catalogue - Service description
- **8.3** Service Level Management - SLA definitions
- **8.4** Service Reporting - Monitoring and reporting
- **8.5** Service Continuity - Disaster recovery
- **8.7** Capacity Management - Capacity management
- **8.8** Information Security - Security operations

### COBIT 2019 Alignment

The templates support the following COBIT Objectives:

- **APO01** Managed IT Management Framework
- **APO07** Managed Human Resources
- **APO09** Managed Service Agreements
- **APO12** Managed Risk
- **APO13** Managed Security
- **BAI03** Managed Solutions Identification
- **BAI06** Managed IT Changes
- **BAI10** Managed Configuration
- **DSS01** Managed Operations
- **DSS02** Managed Service Requests
- **DSS03** Managed Problems
- **DSS04** Managed Continuity
- **DSS05** Managed Security Services
- **DSS06** Managed Business Process Controls

## Frequently Asked Questions (FAQ)

### Do I need to use all templates?

No. Select the templates that are relevant for your service. The numbering provides a logical sequence, but not all templates are required for every service.

### Can I add my own templates?

Yes. Follow the numbering convention (e.g., 0095 for a template between 0090 and 0100) and use the same structure with placeholders.

### How do I update organization information?

Edit the `metadata.yaml` file. All handbooks you generate afterwards will automatically use the updated information.

### Do the templates work without NetBox?

Yes. NetBox placeholders are optional. If NetBox is not configured, the placeholders remain unchanged and can be filled in manually.

### How do I create multilingual handbooks?

Generate handbooks with `--language de` for German and `--language en` for English. The templates are available in both languages.

## Support and Development

### Feedback and Improvement Suggestions

If you have suggestions for improving the templates:
1. Document the improvement suggestion
2. Create an example
3. Contact the template maintainer team

### Template Updates

The templates are regularly updated to:
- Consider new framework versions (ITIL, ISO 20000, COBIT)
- Integrate best practices
- Incorporate user feedback

## License and Usage

These templates are intended for internal use within your organization. You are free to customize and extend the templates.

---

**Version:** 1.0.0  
**Last Updated:** 2024-01-31  
**Maintainer:** IT Operations Team
