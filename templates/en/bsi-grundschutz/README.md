# BSI IT-Grundschutz Handbook Templates (English)

## Overview

These templates form the foundation for a complete IT security handbook according to **BSI IT-Grundschutz** (BSI Standards 200-1, 200-2, 200-3) and the **BSI IT-Grundschutz Compendium**.

The IT security handbook of [TODO] comprises approximately 40 structured documents covering all essential aspects of an Information Security Management System (ISMS) according to BSI IT-Grundschutz.

## Template Structure

### ISMS Foundation (Basics, 0010-0110)

| Document ID | Title | Description | BSI Standard |
|-|-|-|--|
| BSI-0010 | Information Security Policy | Top management policy for information security | BSI 200-1 |
| BSI-0020 | ISMS Organization, Roles, RACI | Organizational structure and responsibilities | BSI 200-1 |
| BSI-0030 | Document Control and Document Register | Versioning, approval, and maintenance of ISMS documentation | BSI 200-1 |
| BSI-0040 | Scope and Information Domain | Definition of ISMS scope | BSI 200-2 |
| BSI-0050 | Structure Analysis | Capture of all relevant objects | BSI 200-2 |
| BSI-0060 | Protection Requirements Assessment | Assessment of confidentiality, integrity, availability | BSI 200-2 |
| BSI-0070 | Modeling and Module Assignment | Assignment of BSI modules | BSI 200-2 |
| BSI-0080 | Basic Security Check (Gap Analysis) | Target-actual comparison of measures | BSI 200-2 |
| BSI-0090 | Risk Analysis according to BSI 200-3 | Risk analysis for additional protection requirements | BSI 200-3 |
| BSI-0100 | Security Concept and Measure Plan | Consolidated security concept | BSI 200-2 |
| BSI-0110 | Implementation Control, Reporting, KPIs | Control and monitoring of implementation | BSI 200-1 |

### Security Policies and Guidelines (Policies, 0200-0530)

Security policies are organized in policy-guideline pairs:
- **Policies (even numbers, 0200-0520):** Abstract, strategic principles
- **Guidelines (odd numbers, 0210-0530):** Concrete implementation instructions

| Policy ID | Policy Title | Guideline ID | Guideline Title | BSI Modules |
|-----|--|--|-----|-|
| BSI-0200 | Policy: Access Control and Permissions | BSI-0210 | Guideline: IAM Joiner Mover Leaver and Recertification | ORP.4, OPS.1.1.2 |
| BSI-0220 | Policy: Authentication and MFA | BSI-0230 | Guideline: Password, MFA and Session Rules | ORP.4, OPS.1.1.5 |
| BSI-0240 | Policy: Asset and Inventory Management | BSI-0250 | Guideline: Asset Lifecycle, Tagging and Disposal | OPS.1.1.1, OPS.1.2.7 |
| BSI-0260 | Policy: Configuration and Hardening | BSI-0270 | Guideline: Security Baselines and Deviation Management | SYS.1.1, SYS.2.1 |
| BSI-0280 | Policy: Patch and Vulnerability Management | BSI-0290 | Guideline: Scans, Patching and Exploitation Response | OPS.1.1.3 |
| BSI-0300 | Policy: Logging, Monitoring and Detection | BSI-0310 | Guideline: Log Standards, SIEM, Use Cases and Retention | OPS.1.1.5, DER.1 |
| BSI-0320 | Policy: Incident Management | BSI-0330 | Guideline: Incident Response, Escalation and Forensics | DER.2.1 |
| BSI-0340 | Policy: Cryptography and Key Management | BSI-0350 | Guideline: Encryption, Key Rotation and Certificates | CON.1 |
| BSI-0360 | Policy: Secure Software Development | BSI-0370 | Guideline: Secure SDLC, Code Reviews, SAST, DAST, Secrets | CON.8 |
| BSI-0380 | Policy: Change and Release Management | BSI-0390 | Guideline: Change, Approvals and Security Checks | OPS.1.1.3 |
| BSI-0400 | Policy: Supplier and Outsourcing Management | BSI-0410 | Guideline: Third-Party Risk Assessment and Contract Clauses | OPS.2.1, OPS.2.2 |
| BSI-0420 | Policy: Data Protection and Data Handling | BSI-0430 | Guideline: Data Classification, Labeling and Transfer | CON.2, CON.3 |
| BSI-0440 | Policy: Backup and Recovery | BSI-0450 | Guideline: Backup, Restore and Regular Tests | CON.3 |
| BSI-0460 | Policy: Network and Communication Security | BSI-0470 | Guideline: Segmentation, Firewalling, VPN and Admin Access | NET.1.1, NET.1.2 |
| BSI-0480 | Policy: Endpoint and Mobile Security | BSI-0490 | Guideline: MDM, EDR, Device Compliance and Remote Work | SYS.2.1, SYS.3.2.2 |
| BSI-0500 | Policy: Physical Security | BSI-0510 | Guideline: Access, Visitors and Equipment Protection | INF.1, INF.2 |
| BSI-0520 | Policy: Exception Process and Risk Acceptance | BSI-0530 | Guideline: Exceptions, Risk Waiver and Review | - |

### Management Processes (Management Processes, 0600-0630)

| Document ID | Title | Description | BSI Standard |
|-|-|-|--|
| BSI-0600 | Training and Awareness Program | Awareness and training | BSI 200-1, ORP.3 |
| BSI-0610 | Internal Audit Program | ISMS audits and controls | BSI 200-1 |
| BSI-0620 | Management Review | Assessment by top management | BSI 200-1 |
| BSI-0630 | Non-conformities and Corrective Actions | Treatment of deviations | BSI 200-1 |

### Appendices (Appendices, 0700-0740)

| Document ID | Title | Description |
|-|-|-|
| BSI-0700 | Appendix: Evidence Register | Register of all evidence and proofs |
| BSI-0710 | Appendix: Asset Inventory | Complete asset inventory |
| BSI-0720 | Appendix: Data Flows and Interfaces | Documentation of all data flows |
| BSI-0730 | Appendix: Diagrams, Network Plan and Zones | Network diagrams and zoning |
| BSI-0740 | Appendix: Terms and Abbreviations | Glossary |

## Placeholder Usage

### Meta Placeholders (Organization Data)

The templates use placeholders from the `metadata.yaml` file:

```markdown
**Organization:** [TODO]
**CEO:** {{ meta-organisation-roles.role_CEO }} ({{ meta-organisation-roles.role_CEO_email }})
**CIO:** {{ meta-organisation-roles.role_CIO }} ({{ meta-organisation-roles.role_CIO_email }})
**CISO/ISB:** {{ meta-organisation-roles.role_CISO }} ({{ meta-organisation-roles.role_CISO_email }})
**Document Owner:** [TODO]
**Locations:** [TODO]
```

### NetBox Placeholders (Infrastructure Data)

For IT-specific information, NetBox placeholders can be used:

```markdown
**Site:** [[ netbox.site.name ]]
**Data Center:** [[ netbox.site.datacenter.name ]]
**Core Switch:** [[ netbox.device.core_switch.name ]]
**Management VLAN:** [[ netbox.vlan.management ]]
**Server:** [[ netbox.device.server_001 ]]
**IP Address:** [[ netbox.ip.server_001 ]]
```

### [TODO] Markers

All templates contain `[TODO]` markers for organization-specific customizations:

```markdown
**Critical System:** [TODO: System name]
**Protection Requirement:** [TODO: High/Medium/Low]
**Responsible:** [TODO: Name]
**BSI Module:** [TODO: e.g., SYS.1.1]
```

## BSI Standards Compliance Mapping

### BSI Standard 200-1: ISMS Requirements

| BSI 200-1 Chapter | BSI Document | Description |
|-|--|-|
| 4 Establishing an ISMS | BSI-0010, BSI-0020 | Policy and organization |
| 5 ISMS Process | BSI-0040 to BSI-0110 | Structure analysis to implementation control |
| 6 Documentation | BSI-0030 | Document control |
| 7 Roles in ISMS | BSI-0020 | RACI matrices |
| 8 Resources | BSI-0020 | Resource planning |
| 9 Training and Awareness | BSI-0600 | Awareness program |
| 10 Maintenance and Improvement | BSI-0610, BSI-0620, BSI-0630 | Audits, reviews, corrective actions |

### BSI Standard 200-2: IT-Grundschutz Methodology

| BSI 200-2 Chapter | BSI Document | Description |
|-|--|-|
| 4 Defining the Scope | BSI-0040 | Information domain |
| 5 Structure Analysis | BSI-0050 | Capture of all objects |
| 6 Protection Requirements Assessment | BSI-0060 | CIA assessment |
| 7 Modeling | BSI-0070 | Module assignment |
| 8 IT-Grundschutz Check | BSI-0080 | Gap analysis |
| 9 Risk Analysis | BSI-0090 | Additional protection requirements |
| 10 Consolidation | BSI-0100 | Security concept |
| 11 Implementation | BSI-0110 | Measure implementation |

### BSI Standard 200-3: Risk Analysis

| BSI 200-3 Chapter | BSI Document | Description |
|-|--|-|
| 4 Preparation | BSI-0090 | Risk analysis preparation |
| 5 Threat Analysis | BSI-0090 | Identification of threats |
| 6 Risk Assessment | BSI-0090 | Assessment of risks |
| 7 Risk Treatment | BSI-0100 | Measure planning |

## BSI IT-Grundschutz Compendium Module Mapping

### Process Modules (ORP, OPS, DER)

| Module | Title | BSI Documents |
|--|-|---|
| ORP.1 | Organization | BSI-0020 |
| ORP.2 | Personnel | BSI-0600 |
| ORP.3 | Awareness and Training | BSI-0600 |
| ORP.4 | Identity and Access Management | BSI-0200, BSI-0210, BSI-0220, BSI-0230 |
| ORP.5 | Compliance Management | BSI-0630 |
| OPS.1.1.1 | Proper IT Administration | BSI-0240, BSI-0250 |
| OPS.1.1.2 | Proper IT Administration | BSI-0200, BSI-0210 |
| OPS.1.1.3 | Patch and Change Management | BSI-0280, BSI-0290, BSI-0380, BSI-0390 |
| OPS.1.1.5 | Logging | BSI-0300, BSI-0310 |
| OPS.1.2.7 | Sale/Disposal of IT | BSI-0240, BSI-0250 |
| OPS.2.1 | Outsourcing for Customers | BSI-0400, BSI-0410 |
| OPS.2.2 | Cloud Usage | BSI-0400, BSI-0410 |
| DER.1 | Detection of Security-Relevant Events | BSI-0300, BSI-0310 |
| DER.2.1 | Treatment of Security Incidents | BSI-0320, BSI-0330 |

### System Modules (SYS, NET, INF)

| Module | Title | BSI Documents |
|--|-|---|
| SYS.1.1 | General Server | BSI-0260, BSI-0270 |
| SYS.2.1 | General Client | BSI-0260, BSI-0270, BSI-0480, BSI-0490 |
| SYS.3.2.2 | Mobile Device Management | BSI-0480, BSI-0490 |
| NET.1.1 | Network Architecture and Design | BSI-0460, BSI-0470 |
| NET.1.2 | Network Management | BSI-0460, BSI-0470 |
| INF.1 | General Building | BSI-0500, BSI-0510 |
| INF.2 | Data Center and Server Room | BSI-0500, BSI-0510 |

### Concept Modules (CON)

| Module | Title | BSI Documents |
|--|-|---|
| CON.1 | Crypto Concept | BSI-0340, BSI-0350 |
| CON.2 | Data Protection | BSI-0420, BSI-0430 |
| CON.3 | Data Backup Concept | BSI-0440, BSI-0450 |
| CON.8 | Software Development | BSI-0360, BSI-0370 |

## HTML Comments for Template Authors

The templates contain HTML comments with notes for template authors:

```markdown
<!-- 
TEMPLATE AUTHOR NOTE:
This template guides the structure analysis according to BSI IT-Grundschutz Standard 200-2.
The structure analysis captures all relevant elements of the information domain.
Reference: BSI Standard 200-2 (Chapter 5: Structure Analysis)
-->
```

These comments are automatically removed when generating the handbook.

## Best Practices for Customization

### 1. Order of Processing

Recommended order for customizing templates according to BSI IT-Grundschutz methodology:

1. **ISMS Foundation** (0010-0040): Define policy, organization, scope
2. **Structure Analysis** (0050): Capture all objects
3. **Protection Requirements Assessment** (0060): Perform CIA assessment
4. **Modeling** (0070): Assign BSI modules
5. **Basic Security Check** (0080): Perform gap analysis
6. **Risk Analysis** (0090): Determine additional protection requirements
7. **Security Concept** (0100): Consolidate measures
8. **Policies and Guidelines** (0200-0530): Develop detailed policies
9. **Management Processes** (0600-0630): Plan audits, reviews, training

### 2. RACI Matrices

All RACI matrices should be completely filled out:

- **R** (Responsible): Execution responsibility
- **A** (Accountable): Overall responsibility, decision authority
- **C** (Consulted): Consulted, subject matter expertise
- **I** (Informed): Informed

**Rule:** Each activity must have exactly one "A".

### 3. Protection Requirements Assessment

Protection requirements assessment is performed for the basic values:

- **Confidentiality:** Protection against unauthorized disclosure
- **Integrity:** Protection against unauthorized modification
- **Availability:** Ensuring availability

**Categories:**
- **Normal:** Damage impact is limited and manageable
- **High:** Damage impact can be considerable
- **Very High:** Damage impact can reach existentially threatening, catastrophic proportions

### 4. BSI Module Assignment

During modeling (Document 0070), BSI modules are assigned:

- **Process Modules:** ORP, OPS, DER
- **System Modules:** SYS, NET, INF, IND
- **Application Modules:** APP
- **Concept Modules:** CON

**Tip:** Use the current BSI IT-Grundschutz Compendium as reference.

### 5. Gap Analysis (Basic Security Check)

The basic security check (Document 0080) compares target and actual:

- **Dispensable:** Requirement not applicable
- **Yes:** Requirement fully implemented
- **Partially:** Requirement partially implemented
- **No:** Requirement not implemented

**Goal:** Identification of implementation gaps for the measure plan.

### 6. Risk Analysis according to BSI 200-3

Risk analysis (Document 0090) is performed for:

- Objects with additional protection requirements (very high)
- Objects not covered by IT-Grundschutz
- Objects with specific threats

**Methodology:** BSI Standard 200-3 (threat analysis, risk assessment, risk treatment)

### 7. Documentation of Evidence

All evidence should be documented in the evidence register (Document 0700):

- **Type:** Document, screenshot, log, configuration, certificate
- **Storage Location:** Path or URL
- **Responsible:** Owner of the evidence
- **Currency:** Date of last update

## Handbook Generation

### CLI Usage

```bash
# Generate German BSI Grundschutz handbook
python src/cli.py --language de --template bsi-grundschutz --output Handbook/de/bsi-grundschutz/

# Generate English BSI Grundschutz handbook
python src/cli.py --language en --template bsi-grundschutz --output Handbook/en/bsi-grundschutz/
```

### Output Formats

- **Markdown:** Individual .md files for each chapter
- **PDF:** Complete handbook as PDF (requires Pandoc)

## Maintenance and Updates

### Update Intervals

- **Annually:** Complete review of all documents (management review)
- **Quarterly:** Structure analysis, asset inventory, contact lists
- **Ad-hoc:** For organizational changes, new systems, security incidents

### Versioning

Use semantic versioning:

- **MAJOR:** Fundamental changes to ISMS structure or scope
- **MINOR:** Additions and updates (new modules, policies)
- **PATCH:** Corrections and editorial changes

### BSI IT-Grundschutz Compendium Updates

The BSI IT-Grundschutz Compendium is regularly updated:

- **Annually:** New edition of the compendium
- **Ongoing:** Updates to individual modules

**Recommendation:** Review annually whether new or updated modules are relevant.

## ISO 27001 Certification based on IT-Grundschutz

The BSI IT-Grundschutz templates support ISO 27001 certification based on IT-Grundschutz:

- **ISO 27001 Certification:** International recognition
- **IT-Grundschutz Certification:** BSI certification (only for German organizations)

**Mapping:** The templates contain references to ISO 27001:2022 clauses where relevant.

## Support and Feedback

For questions or issues:

- **Documentation:** See main README.md
- **BSI Resources:** https://www.bsi.bund.de/grundschutz
- **Issues:** GitHub Issues for bug reports
- **Contributions:** Pull requests welcome

## Further Resources

- **BSI IT-Grundschutz Compendium:** https://www.bsi.bund.de/kompendium
- **BSI Standards 200-1, 200-2, 200-3:** https://www.bsi.bund.de/standards
- **BSI Grundschutz Tools:** GSTOOL, verinice
- **ISO 27001:2022:** International standard for ISMS

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-03  
**Maintainer:** BSI-Grundschutz-Template-Team
