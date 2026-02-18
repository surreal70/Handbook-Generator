# ISMS Handbook Templates (English)

## Overview

These templates form the foundation for a complete Information Security Management System (ISMS) handbook according to **ISO/IEC 27001:2022** (including **Amendment 1:2024**).

The ISMS handbook of [TODO] comprises approximately 50 structured documents covering all essential aspects of information security management. The templates follow a **three-tier architecture** that clearly separates strategic, abstract, and operational documentation.

## Three-Tier Architecture

The ISMS handbook is structured in three hierarchical tiers:

### Tier 1: Basis ISMS (Foundation)
Strategic documents that define the framework and foundations of the ISMS.

### Tier 2: Abstract Policies
High-level security policies that establish principles and requirements.

### Tier 3: Detailed Guidelines
Detailed implementation guidelines with concrete procedures and technical controls.

This structure enables:
- **Clear separation** between strategic and operational documentation
- **Flexibility** in adapting operational details without changing strategic requirements
- **Scalability** for different organization sizes
- **Compliance** with ISO 27001:2022 requirements

## Template Structure

### Tier 1: Basis ISMS (0010-0160)

| Document ID | Title | Description |
|-|-|-|
| ISMS-0010 | Information Security Policy | Top-Level ISMS Policy, Management Commitment |
| ISMS-0020 | Scope | ISMS Scope Definition, Boundaries |
| ISMS-0030 | Context and Interested Parties | Context of Organization, Stakeholders |
| ISMS-0040 | Governance, Roles and Responsibilities | ISMS Governance Structure, RACI Matrices |
| ISMS-0050 | Document Control | Document Control, Version Management |
| ISMS-0060 | Risk Management Methodology | Risk Management Methodology |
| ISMS-0070 | Risk Acceptance Criteria | Risk Acceptance Criteria |
| ISMS-0080 | Risk Register (Template) | Risk Register Template |
| ISMS-0090 | Risk Treatment Plan (RTP) | Risk Treatment Plan Template |
| ISMS-0100 | Statement of Applicability (SoA) | SoA Template with Annex A Controls |
| ISMS-0110 | Security Objectives and Metrics | Security Objectives, KPIs |
| ISMS-0120 | Training, Awareness and Competence | Training and Awareness Program |
| ISMS-0130 | Internal Audit Program | Internal Audit Program |
| ISMS-0140 | Management Review (Template) | Management Review Template |
| ISMS-0150 | Non-Conformities and Corrective Actions | Non-conformities, Corrective Actions |
| ISMS-0160 | Continuous Improvement | Continuous Improvement Process |

### Tier 2: Abstract Policies (0200-0680, even numbers)

High-level security policies for 25 topic areas:

| Document ID | Title | Annex A Mapping |
|-|-|-----|
| ISMS-0200 | Policy: Acceptable Use of IT | A.5.10 |
| ISMS-0220 | Policy: Access Control and Identity Management | A.5.15, A.5.16, A.5.18 |
| ISMS-0240 | Policy: Authentication and Passwords | A.5.17, A.8.5 |
| ISMS-0260 | Policy: Cryptography and Key Management | A.8.24 |
| ISMS-0280 | Policy: Data Classification and Information Handling | A.5.9, A.5.10, A.5.12 |
| ISMS-0300 | Policy: Asset Management | A.5.9, A.5.11 |
| ISMS-0320 | Policy: Logging and Monitoring | A.8.15, A.8.16 |
| ISMS-0340 | Policy: Vulnerability and Patch Management | A.8.8 |
| ISMS-0360 | Policy: Change and Release Management | A.8.32 |
| ISMS-0380 | Policy: Secure Development | A.8.25, A.8.26, A.8.27, A.8.28 |
| ISMS-0400 | Policy: Incident Management | A.5.24, A.5.25, A.5.26, A.6.8 |
| ISMS-0420 | Policy: Backup and Recovery | A.8.13 |
| ISMS-0440 | Policy: Business Continuity / ICT Readiness | A.5.29, A.5.30 |
| ISMS-0460 | Policy: Supplier and Cloud Security | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 |
| ISMS-0480 | Policy: Physical Security | A.7.1, A.7.2, A.7.3, A.7.4 |
| ISMS-0500 | Policy: Mobile Device and Remote Work | A.6.7, A.7.9, A.8.1 |
| ISMS-0520 | Policy: HR Security | A.6.1, A.6.2, A.6.4, A.6.5, A.6.6 |
| ISMS-0540 | Policy: Configuration and Hardening | A.8.9, A.8.18, A.8.19 |
| ISMS-0560 | Policy: Data Protection Interfaces | A.5.34, A.5.36 |
| ISMS-0580 | Policy: Retention and Deletion | A.5.10, A.7.14, A.8.10, A.8.11 |
| ISMS-0600 | Policy: Network Security | A.8.20, A.8.21, A.8.22, A.8.23 |
| ISMS-0620 | Policy: Endpoint Security | A.8.1, A.8.7 |
| ISMS-0640 | Policy: Exceptions and Risk Waivers | A.5.1 (Exception Process) |
| ISMS-0660 | Policy: Information Transfer and Communication | A.5.13, A.5.14 |
| ISMS-0680 | Policy: Security in Projects | A.5.8 |

### Tier 3: Detailed Guidelines (0210-0690, odd numbers)

Detailed implementation guidelines for each policy:

| Document ID | Title | Associated Policy |
|-|-|-|
| ISMS-0210 | Guideline: Acceptable Use of IT | 0200 |
| ISMS-0230 | Guideline: IAM, Joiner-Mover-Leaver, Access Requests | 0220 |
| ISMS-0250 | Guideline: MFA, Password Rules, Session Management | 0240 |
| ISMS-0270 | Guideline: Key Management and Encryption | 0260 |
| ISMS-0290 | Guideline: Data Classification, Labeling, Handling | 0280 |
| ISMS-0310 | Guideline: Asset Inventory, Tagging, Disposal | 0300 |
| ISMS-0330 | Guideline: Logging, SIEM, Audit Trails | 0320 |
| ISMS-0350 | Guideline: Vulnerability Scans, Patching, Exploitation Response | 0340 |
| ISMS-0370 | Guideline: Change Management with Security Approvals | 0360 |
| ISMS-0390 | Guideline: Secure SDLC, Coding Review, Secrets | 0380 |
| ISMS-0410 | Guideline: Incident Response and Major Incident Process | 0400 |
| ISMS-0430 | Guideline: Backup, Restore, Regular Tests | 0420 |
| ISMS-0450 | Guideline: ICT DR, Interfaces to BCM | 0440 |
| ISMS-0470 | Guideline: Third-Party Risk Assessment, Cloud Controls | 0460 |
| ISMS-0490 | Guideline: Access, Visitors, Equipment Protection | 0480 |
| ISMS-0510 | Guideline: MDM, BringYourOwnDevice, Remote Access | 0500 |
| ISMS-0530 | Guideline: HR Onboarding, Role Change, Offboarding | 0520 |
| ISMS-0550 | Guideline: Security Baselines, Hardening, Config Changes | 0540 |
| ISMS-0570 | Guideline: Data Protection Requirements, Data Processing | 0560 |
| ISMS-0590 | Guideline: Records Retention, Secure Deletion | 0580 |
| ISMS-0610 | Guideline: Segmentation, Firewalling, Network Access Control | 0600 |
| ISMS-0630 | Guideline: EDR, AV, Host Firewall, Device Compliance | 0620 |
| ISMS-0650 | Guideline: Exception Process | 0640 |
| ISMS-0670 | Guideline: Email, Sharing, Collaboration Tools | 0660 |
| ISMS-0690 | Guideline: Security Requirements in Project Lifecycle | 0680 |

### Appendices (0710-0740)

| Document ID | Title | Description |
|-|-|-|
| ISMS-0710 | Appendix: Annex A Mapping | Complete mapping of all 93 Annex A Controls |
| ISMS-0720 | Appendix: Asset and System Inventory | Asset Inventory Template |
| ISMS-0730 | Appendix: Data Flows and Interfaces | Data Flow Diagrams |
| ISMS-0740 | Appendix: Terms and Abbreviations | Glossary |

## Placeholder Usage

### Meta Placeholders (Organization Data)

The templates use placeholders from the `metadata.yaml` file:

```markdown
**Organization:** [TODO]
**CEO:** {{ meta.management.ceo }}
**CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
**CISO:** {{ meta.ciso.name }} ({{ meta.ciso.email }})
**Document Owner:** [TODO]
**Date:** {{ meta-handbook.modifydate }}
**Next Review:** [TODO]
```

### NetBox Placeholders (Infrastructure Data)

For IT-specific information, NetBox placeholders can be used:

```markdown
**Site:** {{ netbox.site.name }}
**Data Center:** {{ netbox.site.datacenter.name }}
**Core Switch:** {{ netbox.device.core_switch.name }}
**Management VLAN:** {{ netbox.vlan.management.vid }}
```

### [TODO] Markers

All templates contain `[TODO]` markers for organization-specific customizations:

```markdown
**Critical System:** [TODO: System name]
**RTO:** [TODO: 4 hours]
**Security Tool:** {{ meta.security.edr_solution }} [TODO: e.g., CrowdStrike, SentinelOne]
```

## ISO 27001:2022 Compliance Mapping

### Main Clauses

| ISO 27001 Clause | ISMS Document | Description |
||---|-|
| 4.1 Understanding the organization | ISMS-0030 | Context of Organization |
| 4.2 Understanding needs of interested parties | ISMS-0030 | Interested Parties |
| 4.3 Determining the scope | ISMS-0020 | ISMS Scope |
| 4.4 Information security management system | ISMS-0010, ISMS-0040 | ISMS Establishment |
| 5.1 Leadership and commitment | ISMS-0010 | Management Commitment |
| 5.2 Policy | ISMS-0010 | Information Security Policy |
| 5.3 Organizational roles | ISMS-0040 | Roles and Responsibilities |
| 6.1.1 General (Risk assessment) | ISMS-0060, ISMS-0080 | Risk Management |
| 6.1.2 Information security risk assessment | ISMS-0060, ISMS-0080 | Risk Assessment |
| 6.1.3 Information security risk treatment | ISMS-0090 | Risk Treatment Plan |
| 6.1.3 d) Statement of Applicability | ISMS-0100 | SoA |
| 6.2 Information security objectives | ISMS-0110 | Security Objectives |
| 7.2 Competence | ISMS-0120 | Training and Awareness |
| 7.5 Documented information | ISMS-0050 | Document Control |
| 8.1 Operational planning and control | ISMS-0090, ISMS-0100 | Operational Controls |
| 9.1 Monitoring, measurement, analysis | ISMS-0110 | Performance Evaluation |
| 9.2 Internal audit | ISMS-0130 | Internal Audit |
| 9.3 Management review | ISMS-0140 | Management Review |
| 10.1 Nonconformity and corrective action | ISMS-0150 | Corrective Actions |
| 10.2 Continual improvement | ISMS-0160 | Continuous Improvement |

### Annex A Controls (93 Controls)

**Complete Mapping:** See `0710_Appendix_AnnexA_Mapping_Template.md`

**Categories:**
- **Organisational Controls (5.x):** 37 Controls → Policies 0200-0680
- **People Controls (6.x):** 8 Controls → Policy 0520, Guideline 0530
- **Physical Controls (7.x):** 14 Controls → Policy 0480, Guideline 0490
- **Technological Controls (8.x):** 34 Controls → Policies 0220-0640

**Amendment 1:2024:**
- Incorporates changes from Amendment 1:2024
- Updated control descriptions
- New attributes (Control Type, Information Security Properties, Cybersecurity Concepts, Operational Capabilities, Security Domains)

## HTML Comments for Template Authors

The templates contain HTML comments with notes for template authors:

```markdown
<!-- 
TEMPLATE AUTHOR NOTE:
This section requires customization based on your organization's specific
security requirements. Consider the following:
- Risk appetite and tolerance levels
- Compliance requirements (GDPR, NIS2, etc.)
- Industry-specific standards
-->
```

These comments are automatically removed when generating the handbook.

## Best Practices for Customization

### 1. Customization Sequence

Recommended sequence for customizing the templates:

**Phase 1: Foundation (Week 1-2)**
1. **ISMS-0010:** Customize Information Security Policy
2. **ISMS-0020:** Define ISMS Scope
3. **ISMS-0030:** Identify context and stakeholders
4. **ISMS-0040:** Establish governance structure and roles

**Phase 2: Risk Management (Week 3-4)**
5. **ISMS-0060:** Adapt risk management methodology
6. **ISMS-0070:** Define risk acceptance criteria
7. **ISMS-0080:** Conduct risk analysis, create risk register
8. **ISMS-0090:** Create risk treatment plan

**Phase 3: Controls Selection (Week 5-6)**
9. **ISMS-0100:** Create Statement of Applicability
10. **Policies (0200-0680):** Select and customize relevant policies
11. **Guidelines (0210-0690):** Develop detailed guidelines

**Phase 4: Operations (Week 7-8)**
12. **ISMS-0110:** Define security objectives and KPIs
13. **ISMS-0120:** Establish training program
14. **ISMS-0130:** Plan audit program
15. **ISMS-0140:** Establish management review

### 2. RACI Matrices

All RACI matrices should be completely filled out:

- **R** (Responsible): Execution responsibility
- **A** (Accountable): Overall responsibility, decision authority (exactly one person per activity)
- **C** (Consulted): Consulted, subject matter expertise
- **I** (Informed): Informed

**Rule:** Each activity must have exactly one "A".

### 3. Annex A Controls

**Selection Criteria:**
- **Risk-based:** Controls to treat identified risks
- **Compliance:** Legal and regulatory requirements (GDPR, NIS2, etc.)
- **Best Practices:** Industry-standard security measures
- **Stakeholder Requirements:** Customers, partners, regulators

**Document Exclusions:**
- Justification for non-applicable controls
- Alternative measures (if available)
- Approval by CISO

### 4. Utilize Three-Tier Structure

**Tier 1 (Basis ISMS):**
- Strategic documents, rarely changed
- Management approval required
- Annual review

**Tier 2 (Abstract Policies):**
- High-level principles, stable
- CISO approval required
- Annual review

**Tier 3 (Detailed Guidelines):**
- Operational details, changed more frequently
- IT Operations/Department approval
- Quarterly review or as needed

**Advantage:** Operational changes don't require adjustments to strategic documents.

### 5. Evidence Documentation

For each implemented control, evidence should be documented:

- **Policies and Guidelines:** Approved documents
- **Technical Controls:** Configuration evidence, screenshots
- **Processes:** Process descriptions, workflows
- **Training:** Attendance records, certificates
- **Audits:** Audit reports, findings, corrective actions
- **Monitoring:** Logs, reports, dashboards

**Evidence Register:** See `0700_Appendix_Evidence_Register.md` (BSI Grundschutz)

### 6. Integration with Other Management Systems

**BCM (Business Continuity Management):**
- Policy 0440: Business Continuity / ICT Readiness
- Guideline 0450: ICT DR, Interfaces to BCM
- Link to BCM Handbook (see BCM Templates)

**Data Protection (GDPR):**
- Policy 0560: Data Protection Interfaces
- Guideline 0570: Data Protection Requirements, Data Processing
- Link to Data Protection Management System

**IT Service Management (ITIL):**
- Policy 0360: Change and Release Management
- Policy 0400: Incident Management
- Integration with ITSM tools (ServiceNow, Jira Service Management)

## Handbook Generation

### CLI Usage

```bash
# Generate German ISMS handbook
python src/cli.py --language de --template isms --output Handbook/de/isms/

# Generate English ISMS handbook
python src/cli.py --language en --template isms --output Handbook/en/isms/
```

### Output Formats

- **Markdown:** Individual .md files for each chapter
- **PDF:** Complete handbook as PDF (requires Pandoc)

### Configuration

**metadata.yaml:**
```yaml
organization:
  name: "Example Corp"
  
management:
  ceo: "John Doe"
  
cio:
  name: "Dr. Jane Smith"
  email: "jane.smith@example.com"
  
ciso:
  name: "Thomas Miller"
  email: "thomas.miller@example.com"
  
document:
  owner: "ISMS Team"
  date: "2026-02-01"
  next_review: "2027-02-01"
  approval_date: "2026-02-01"
  
security:
  edr_solution: "CrowdStrike Falcon"
  siem_solution: "Microsoft Sentinel"
  web_filter: "Cisco Umbrella"
  # ... additional security tools
```

## Maintenance and Updates

### Update Intervals

**Annually:**
- Complete review of all Basis ISMS documents (0010-0160)
- Review of all Abstract Policies (0200-0680)
- Update of Statement of Applicability (0100)
- Management Review (0140)

**Quarterly:**
- Review of Detailed Guidelines (0210-0690) as needed
- Update of Risk Register (0080)
- Tracking of Risk Treatment Plan (0090)
- KPI Review (0110)

**Ad-hoc:**
- Organizational changes (scope, structure)
- New risks or threats
- Audit findings or incidents
- Changes in compliance requirements

### Versioning

Use semantic versioning:

- **MAJOR:** Fundamental changes to ISMS structure or strategy
- **MINOR:** Additions and updates to policies/guidelines
- **PATCH:** Corrections and editorial changes

### Change Management

Changes to ISMS documents should be managed through the change process:
- **Change Request:** Request with justification
- **Impact Assessment:** Impact on ISMS and compliance
- **Approval:** Approval by CISO (policies) or department (guidelines)
- **Communication:** Information to affected stakeholders
- **Training:** Training for significant changes

## Certification and Audits

### ISO 27001:2022 Certification

**Preparation:**
1. **Gap Analysis:** Compare current state with ISO 27001 requirements
2. **Documentation:** Create complete ISMS documentation
3. **Implementation:** Implement controls according to SoA
4. **Internal Audit:** Conduct internal audit (ISMS-0130)
5. **Management Review:** Conduct management review (ISMS-0140)

**Certification Audit:**
- **Stage 1:** Document review, readiness assessment
- **Stage 2:** On-site audit, interviews, evidence review
- **Certificate:** Valid for 3 years
- **Surveillance Audits:** Annual surveillance audits

**Recertification:**
- Complete recertification audit after 3 years

### Internal Audits

**Audit Program:** See ISMS-0130

**Audit Frequency:**
- All ISMS areas at least annually
- Critical areas semi-annually
- Ad-hoc audits as needed

**Audit Evidence:**
- Audit plans and reports
- Findings and corrective actions
- Follow-up audits

## Support and Feedback

For questions or issues:

- **Documentation:** See main README.md
- **Issues:** GitHub Issues for bug reports
- **Contributions:** Pull requests welcome

## References

### External Standards

- **ISO/IEC 27001:2022** - Information security management systems - Requirements
- **ISO/IEC 27001:2022/Amd 1:2024** - Amendment 1 (Annex A updates)
- **ISO/IEC 27002:2022** - Information security controls (detailed guidance)
- **ISO/IEC 27005:2022** - Information security risk management
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- **NIS2 Directive (EU 2022/2555)** - Network and Information Security Directive
- **BSI IT-Grundschutz** - German Federal Office for Information Security

### Related Template Sets

- **BCM Templates:** Business Continuity Management (ISO 22301)
- **BSI Grundschutz Templates:** BSI IT-Grundschutz Standards 200-1, 200-2, 200-3
- **IT-Operation Templates:** IT Operations Handbook

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-02  
**Maintainer:** ISMS Template Team
