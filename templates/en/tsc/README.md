# TSC (SOC 2) Compliance Handbook Templates (English)

## Overview

These templates form the foundation for a complete TSC (Trust Services Criteria) compliance handbook for **SOC 2 audits**.

The TSC handbook for [TODO] includes structured documents covering all five Trust Services categories: Security (Common Criteria), Availability, Processing Integrity, Confidentiality, and Privacy.

## Template Structure

### Foundation (0010-0050)

| Document ID | Title | Description |
|-|-|-|
| TSC-0010 | System Description | Description of the service system and its boundaries |
| TSC-0020 | System Boundaries | Definition of system boundaries and interfaces |
| TSC-0030 | System Components | Infrastructure, software, people, processes, data |
| TSC-0040 | Roles and Responsibilities | TSC-specific roles and RACI matrices |
| TSC-0050 | Control Environment | Control environment and governance structure |

### Common Criteria - Security (Required for all SOC 2, 0100-0150)

| Document ID | Title | Description |
|-|-|-|
| TSC-0100 | CC1: Control Environment | Organizational structure, integrity, ethics |
| TSC-0110 | CC2: Communication | Communication of objectives and responsibilities |
| TSC-0120 | CC3: Risk Assessment | Risk assessment process |
| TSC-0130 | CC4: Monitoring | Monitoring of control effectiveness |
| TSC-0140 | CC5: Control Activities | Logical and physical access control |
| TSC-0150 | CC6-CC9: Security Controls | Change management, operations, risk mitigation |

### Availability Criteria (Optional, 0200-0230)

| Document ID | Title | Description |
|-|-|-|
| TSC-0200 | A1.1: Availability Commitments | Availability commitments and SLAs |
| TSC-0210 | A1.2: System Monitoring | System availability monitoring |
| TSC-0220 | A1.3: Incident Management | Incident response for availability issues |
| TSC-0230 | A1.4: Recovery Procedures | Backup and disaster recovery |

### Processing Integrity Criteria (Optional, 0240-0270)

| Document ID | Title | Description |
|-|-|-|
| TSC-0240 | PI1.1: Processing Commitments | Processing integrity commitments |
| TSC-0250 | PI1.2: Input Validation | Input data validation |
| TSC-0260 | PI1.3: Processing Controls | Controls during processing |
| TSC-0270 | PI1.4: Output Controls | Output data controls |

### Confidentiality Criteria (Optional, 0280-0310)

| Document ID | Title | Description |
|-|-|-|
| TSC-0280 | C1.1: Confidentiality Commitments | Confidentiality commitments |
| TSC-0290 | C1.2: Access Controls | Access control for confidential data |
| TSC-0300 | C1.3: Encryption | Encryption of confidential data |
| TSC-0310 | C1.4: Data Disposal | Secure disposal of confidential data |

### Privacy Criteria (Optional, 0320-0350)

| Document ID | Title | Description |
|-|-|-|
| TSC-0320 | P1: Notice and Communication | Privacy notices |
| TSC-0330 | P2-P3: Choice and Consent | Consent and choices |
| TSC-0340 | P4-P5: Collection and Use | Data collection and use |
| TSC-0350 | P6-P8: Access, Disclosure, Quality | Access, disclosure, data quality |

### Appendices (0400-0450)

| Document ID | Title | Description |
|-|-|-|
| TSC-0400 | Control Matrix | Complete TSC control matrix |
| TSC-0410 | Evidence Documentation | Evidence documentation for audits |
| TSC-0420 | Test Results | Control test results |
| TSC-0430 | Vendor Management | Subservice organization management |
| TSC-0440 | Glossary | TSC-specific terms and abbreviations |

## Placeholder Usage

### Meta Placeholders (Organization Data)

Templates use placeholders from the `metadata.yaml` file:

```markdown
**Organization:** [TODO]
**Service Auditor:** [TODO] ([TODO])
**CISO:** [TODO] ([TODO])
**System Name:** {{ meta.tsc.system_name }}
**Report Period:** {{ meta.tsc.report_period }}
```

### [TODO] Markers

All templates contain `[TODO]` markers for organization-specific customization:

```markdown
**System Description:** [TODO: Description of service system]
**Availability SLA:** [TODO: 99.9% uptime]
**Encryption Standard:** [TODO: AES-256]
```

## TSC Criteria Mapping

### Common Criteria (CC) - Required for all SOC 2

| TSC Criterion | TSC Document | Description |
|---|--|-|
| CC1: Control Environment | TSC-0100 | Organizational structure and integrity |
| CC2: Communication | TSC-0110 | Communication of objectives |
| CC3: Risk Assessment | TSC-0120 | Risk assessment |
| CC4: Monitoring | TSC-0130 | Control monitoring |
| CC5: Control Activities | TSC-0140 | Access control |
| CC6: Logical Access | TSC-0150 | Logical access control |
| CC7: System Operations | TSC-0150 | System operations |
| CC8: Change Management | TSC-0150 | Change management |
| CC9: Risk Mitigation | TSC-0150 | Risk mitigation |

### Optional Categories

| Category | TSC Documents | Description |
|----|---|-|
| Availability (A) | TSC-0200 - TSC-0230 | System availability |
| Processing Integrity (PI) | TSC-0240 - TSC-0270 | Processing integrity |
| Confidentiality (C) | TSC-0280 - TSC-0310 | Confidentiality |
| Privacy (P) | TSC-0320 - TSC-0350 | Privacy |

## SOC 2 Report Types

### Type I Report

- **Point in Time:** As of a specific date
- **Scope:** Design of controls
- **Opinion:** Controls are suitably designed

### Type II Report

- **Period of Time:** Over a period (e.g., 6-12 months)
- **Scope:** Design and operating effectiveness of controls
- **Opinion:** Controls are suitably designed AND operating effectively

## Trust Services Categories

### Security (Common Criteria) - REQUIRED

Protection of the system against unauthorized access (logical and physical):
- Access control
- Authentication
- Network security
- Physical security
- Change management

### Availability - OPTIONAL

System is available for operation and use as committed:
- System availability
- Incident management
- Backup and recovery
- Capacity planning

### Processing Integrity - OPTIONAL

System processing is complete, valid, accurate, timely, and authorized:
- Input validation
- Processing controls
- Output controls
- Error handling

### Confidentiality - OPTIONAL

Confidential information is protected as committed:
- Data encryption
- Access restrictions
- Secure transmission
- Secure disposal

### Privacy - OPTIONAL

Personal information is collected, used, retained, disclosed, and disposed of in conformity with privacy notices:
- Privacy notices
- Consent
- Data minimization
- Data subject rights

## Best Practices for SOC 2 Compliance

### 1. Scope Definition

- **System Boundaries:** Clear definition of system boundaries
- **Service Commitments:** Documented commitments to customers
- **Subservice Organizations:** Identification of all subservice providers
- **Complementary User Entity Controls (CUEC):** Controls at the customer

### 2. Control Design

- **Risk-Based Approach:** Controls based on risk assessment
- **Control Objectives:** Define clear control objectives
- **Control Activities:** Document specific control activities
- **Evidence Collection:** Collect evidence for each control

### 3. Control Testing

- **Test Procedures:** Documented test procedures
- **Sample Selection:** Appropriate sample selection
- **Test Frequency:** Regular testing during report period
- **Exception Handling:** Handling of control deviations

### 4. Documentation

- **System Description:** Detailed system description
- **Control Matrix:** Complete control matrix
- **Policies and Procedures:** All relevant policies
- **Evidence Repository:** Central evidence repository

## Handbook Generation

### CLI Usage

```bash
# Generate German TSC handbook
python -m src.cli --language de --template tsc --test

# Generate English TSC handbook
python -m src.cli --language en --template tsc --test

# Generate PDF with table of contents
python -m src.cli --language en --template tsc --output pdf --test --pdf-toc

# Generate all formats
python -m src.cli --language en --template tsc --output all --test --separate-files --pdf-toc
```

## Maintenance and Updates

### Update Intervals

- **Annually:** Complete review before SOC 2 audit
- **Quarterly:** Review of control effectiveness
- **Ad-hoc:** For system changes or new risks

### Versioning

- **MAJOR:** New TSC version or significant system changes
- **MINOR:** Additions and updates
- **PATCH:** Corrections and editorial changes

## Support and Feedback

For questions or issues:

- **Documentation:** See main README.md
- **AICPA:** https://www.aicpa.org/soc4so
- **Issues:** GitHub Issues for bug reports

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-07  
**Maintainer:** TSC-Template-Team
