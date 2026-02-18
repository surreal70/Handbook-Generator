# BCM Handbook Templates (English)

## Overview

These templates form the foundation for a complete Business Continuity Management (BCM) handbook according to **ISO 22301:2019** and **BSI Standard 100-4**.

The BCM handbook of [TODO] comprises 30 structured documents covering all essential aspects of Business Continuity Management.

## Template Structure

### Foundation (0010-0090)

| Document ID | Title | Description |
|-|-|-|
| BCM-0010 | Purpose and Scope | Definition of purpose, scope, and objectives of the BCMS |
| BCM-0020 | BCM Policy | Management commitment and BCM policy |
| BCM-0030 | Document Control | Versioning, approval, and maintenance of BCM documentation |
| BCM-0040 | Emergency Organization | Roles, responsibilities, and RACI matrices |
| BCM-0050 | Contacts and Escalation | Contact lists and escalation paths |
| BCM-0060 | Service and Process Catalog | Criticality assessment of services and processes |
| BCM-0070 | BIA Methodology | Business Impact Analysis methodology |
| BCM-0080 | BIA Results and RTO/RPO | BIA results with RTO/RPO values |
| BCM-0090 | Risk Analysis and Scenarios | Risk assessment and disaster scenarios |

### Strategy & Plans (0100-0180)

| Document ID | Title | Description |
|-|-|-|
| BCM-0100 | Strategy and Continuity Options | BCM strategy and recovery options |
| BCM-0110 | Activation Criteria | Criteria for BCM activation |
| BCM-0120 | Crisis Management Plan | Crisis management processes |
| BCM-0130 | Communication Plan | Internal and external crisis communication |
| BCM-0140 | BCP Template | Business Continuity Plan template |
| BCM-0150 | DRP Template | IT Disaster Recovery Plan template |
| BCM-0160 | Backup and Restore | Backup strategy and recovery |
| BCM-0170 | Alternative Sites | Alternative sites and emergency workplaces |
| BCM-0180 | Supplier Continuity | BCM for critical suppliers |

### Operations & Compliance (0190-0290)

| Document ID | Title | Description |
|-|-|-|
| BCM-0190 | Resource Planning | Minimum staffing and resource requirements |
| BCM-0200 | Emergency Access (Break-Glass) | Emergency access and privileged access |
| BCM-0210 | Cyber Incident Playbook | Ransomware and cyber incidents |
| BCM-0220 | Exercise and Test Program | BCM exercises and tests |
| BCM-0230 | Test Protocols | Documentation of tests and exercises |
| BCM-0240 | Post-Incident Review | Post-incident review and lessons learned |
| BCM-0250 | Maintenance and KPIs | Maintenance and performance measurement |
| BCM-0260 | Training and Awareness | Training and awareness programs |
| BCM-0270 | Compliance and Audits | Evidence and audits |
| BCM-0280 | Appendix: Templates | Checklists and templates |
| BCM-0290 | Glossary | Terms and abbreviations |

## Placeholder Usage

### Meta Placeholders (Organization Data)

Templates use placeholders from the `metadata.yaml` file:

```markdown
**Organization:** [TODO]
**CEO:** [TODO] ([TODO])
**CIO:** [TODO] ([TODO])
**CISO:** [TODO] ([TODO])
**Document Owner:** [TODO]
```

### NetBox Placeholders (Infrastructure Data)

For IT-specific information, NetBox placeholders can be used:

```markdown
**Site:** {{ netbox.site.name }}
**Data Center:** {{ netbox.site.datacenter.name }}
**Core Switch:** {{ netbox.device.core_switch.name }}
```

### [TODO] Markers

All templates contain `[TODO]` markers for organization-specific customizations:

```markdown
**Critical Supplier:** [TODO: Supplier name]
**RTO:** [TODO: 4 hours]
**Emergency Budget:** [TODO: $50,000]
```

## ISO 22301:2019 Compliance Mapping

| ISO 22301 Clause | BCM Document | Description |
||--|-|
| 4.1 Understanding the organization | BCM-0010 | Context of the organization |
| 4.3 Determining the scope | BCM-0010 | Scope definition |
| 5.2 Policy | BCM-0020 | BCM policy |
| 5.3 Organizational roles | BCM-0040 | Roles and responsibilities |
| 7.5 Documented information | BCM-0030 | Document control |
| 8.2.2 Business impact analysis | BCM-0070, BCM-0080 | BIA methodology and results |
| 8.2.3 Risk assessment | BCM-0090 | Risk analysis |
| 8.3 Business continuity strategies | BCM-0100 | BCM strategy |
| 8.4 Business continuity procedures | BCM-0140, BCM-0150 | BCP and DRP |
| 8.5 Exercise and testing | BCM-0220, BCM-0230 | Exercises and tests |
| 9.1 Monitoring and measurement | BCM-0250 | KPIs and monitoring |
| 9.2 Internal audit | BCM-0270 | Internal audits |
| 9.3 Management review | BCM-0250 | Management review |
| 10.1 Nonconformity and corrective action | BCM-0240 | Corrective actions |

## BSI Standard 100-4 Mapping

| BSI 100-4 Chapter | BCM Document | Description |
|-|--|-|
| 3.1 Initiation | BCM-0020 | BCM policy and initiation |
| 3.2 Conception | BCM-0070, BCM-0080, BCM-0090 | BIA and risk analysis |
| 3.3 Implementation | BCM-0100, BCM-0140, BCM-0150 | Strategy and plans |
| 3.4 Tests and exercises | BCM-0220, BCM-0230 | Exercise program |
| 3.5 Maintenance | BCM-0250 | Maintenance and improvement |

## HTML Comments for Template Authors

Templates contain HTML comments with notes for template authors:

```markdown
<!-- 
TEMPLATE AUTHOR NOTE:
This section requires customization based on your organization's specific BCM strategy.
Consider the following:
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)
- Critical business processes
-->
```

These comments are automatically removed when generating the handbook.

## Best Practices for Customization

### 1. Order of Processing

Recommended order for customizing templates:

1. **Foundation** (0010-0090): Establish fundamentals
2. **Conduct BIA** (0070, 0080): Determine criticality
3. **Develop strategy** (0100): Define BCM strategy
4. **Create plans** (0140, 0150): Develop BCP and DRP
5. **Plan exercises** (0220): Set up test program

### 2. RACI Matrices

All RACI matrices should be completely filled out:

- **R** (Responsible): Execution responsibility
- **A** (Accountable): Overall responsibility, decision authority
- **C** (Consulted): Consulted, subject matter expertise
- **I** (Informed): Informed

**Rule:** Each activity must have exactly one "A".

### 3. RTO/RPO Values

RTO/RPO values should be realistic and achievable:

- **RTO:** Should be 50-70% of MTPD (safety buffer)
- **RPO:** Depends on backup frequency and data change rate
- **Validation:** Confirm through tests and exercises

### 4. Contact Lists

Contact lists require special attention:

- **Data Privacy:** Store and process in compliance with GDPR
- **Currency:** Quarterly review
- **Offline Availability:** Encrypted USB drives or paper printouts

### 5. Dependency Documentation

Document all critical dependencies:

- **People:** Key personnel and minimum staffing
- **Facilities:** Sites and premises
- **Technology:** IT systems and infrastructure
- **Information:** Data and knowledge
- **Suppliers:** Vendors and service providers

## Handbook Generation

### CLI Usage

```bash
# Generate German BCM handbook
python src/cli.py --language de --template bcm --output Handbook/de/bcm/

# Generate English BCM handbook
python src/cli.py --language en --template bcm --output Handbook/en/bcm/
```

### Output Formats

- **Markdown:** Individual .md files for each chapter
- **PDF:** Complete handbook as PDF (requires Pandoc)

## Maintenance and Updates

### Update Intervals

- **Annually:** Complete review of all documents
- **Quarterly:** Contact lists and escalation paths
- **Ad-hoc:** After organizational changes or incidents

### Versioning

Use semantic versioning:

- **MAJOR:** Fundamental changes to structure or strategy
- **MINOR:** Additions and updates
- **PATCH:** Corrections and editorial changes

## Support and Feedback

For questions or issues:

- **Documentation:** See main README.md
- **Issues:** GitHub Issues for bug reports
- **Contributions:** Pull requests welcome

---

**Version:** 1.0.0  
**Last Updated:** 2026-01-31  
**Maintainer:** BCM Template Team
