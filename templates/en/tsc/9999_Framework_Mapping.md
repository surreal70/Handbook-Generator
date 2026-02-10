# TSC Framework Mapping

## Overview

This document maps the TSC templates to the Trust Services Criteria (TSC) for SOC 2 audits.

## Trust Services Categories

### Common Criteria (CC) - Security (Required for all SOC 2)

| TSC Criterion | Template | Description |
|---------------|----------|-------------|
| **CC1: Control Environment** | TSC-0100 | Organizational structure, integrity, ethical values |
| CC1.1 | TSC-0100 | Integrity and ethical values |
| CC1.2 | TSC-0100 | Board independence |
| CC1.3 | TSC-0100 | Management oversight |
| CC1.4 | TSC-0100 | Commitment to competence |
| CC1.5 | TSC-0100 | Accountability |
| **CC2: Communication and Information** | TSC-0110 | Communication of objectives and responsibilities |
| CC2.1 | TSC-0110 | Internal communication |
| CC2.2 | TSC-0110 | External communication |
| CC2.3 | TSC-0110 | Information quality |
| **CC3: Risk Assessment** | TSC-0120 | Risk assessment process |
| CC3.1 | TSC-0120 | Risk identification |
| CC3.2 | TSC-0120 | Risk analysis |
| CC3.3 | TSC-0120 | Risk response |
| **CC4: Monitoring Activities** | TSC-0130 | Monitoring of control effectiveness |
| CC4.1 | TSC-0130 | Ongoing monitoring |
| CC4.2 | TSC-0130 | Separate evaluations |
| CC4.3 | TSC-0130 | Evaluation and communication |
| **CC5: Control Activities** | TSC-0140 | Logical and physical access control |
| CC5.1 | TSC-0140 | Selection and development of control activities |
| CC5.2 | TSC-0140 | Technology controls |
| CC5.3 | TSC-0140 | Policies and procedures |
| **CC6: Logical and Physical Access Controls** | TSC-0150 | Access control |
| CC6.1 | TSC-0150 | Logical access |
| CC6.2 | TSC-0150 | Physical access |
| CC6.3 | TSC-0150 | Access removal |
| CC6.6 | TSC-0150 | Logical access - Identification and authentication |
| CC6.7 | TSC-0150 | Logical access - Privileged access |
| CC6.8 | TSC-0150 | Physical access - Data centers |
| **CC7: System Operations** | TSC-0150 | System operations |
| CC7.1 | TSC-0150 | Detection and monitoring |
| CC7.2 | TSC-0150 | System capacity |
| CC7.3 | TSC-0150 | System monitoring tools |
| CC7.4 | TSC-0150 | Incident response |
| CC7.5 | TSC-0150 | Incident mitigation |
| **CC8: Change Management** | TSC-0150 | Change management |
| CC8.1 | TSC-0150 | Change authorization |
| CC8.2 | TSC-0150 | Change testing |
| CC8.3 | TSC-0150 | Change deployment |
| **CC9: Risk Mitigation** | TSC-0150 | Risk mitigation |
| CC9.1 | TSC-0150 | Risk assessment |
| CC9.2 | TSC-0150 | Vendor management |

### Availability (A) - Optional

| TSC Criterion | Template | Description |
|---------------|----------|-------------|
| **A1: Availability** | TSC-0200 | System availability |
| A1.1 | TSC-0200 | Availability commitments and SLAs |
| A1.2 | TSC-0200 | System monitoring and alerting |
| A1.3 | TSC-0200 | Incident management for availability |
| A1.4 | TSC-0200 | Recovery procedures and disaster recovery |

### Processing Integrity (PI) - Optional

| TSC Criterion | Template | Description |
|---------------|----------|-------------|
| **PI1: Processing Integrity** | TSC-0240 | Processing integrity |
| PI1.1 | TSC-0240 | Processing commitments |
| PI1.2 | TSC-0240 | Input validation |
| PI1.3 | TSC-0240 | Processing controls |
| PI1.4 | TSC-0240 | Output controls |
| PI1.5 | TSC-0240 | Error handling and correction |

### Confidentiality (C) - Optional

| TSC Criterion | Template | Description |
|---------------|----------|-------------|
| **C1: Confidentiality** | TSC-0280 | Confidentiality |
| C1.1 | TSC-0280 | Confidentiality commitments |
| C1.2 | TSC-0280 | Access controls for confidential data |
| C1.3 | TSC-0280 | Encryption of confidential data |
| C1.4 | TSC-0280 | Secure disposal of confidential data |

### Privacy (P) - Optional

| TSC Criterion | Template | Description |
|---------------|----------|-------------|
| **P1: Notice and Communication** | TSC-0320 | Privacy notices |
| P1.1 | TSC-0320 | Privacy notice |
| P1.2 | TSC-0320 | Privacy policy communication |
| **P2: Choice and Consent** | TSC-0320 | Consent |
| P2.1 | TSC-0320 | Consent for collection |
| **P3: Collection** | TSC-0320 | Data collection |
| P3.1 | TSC-0320 | Collection limitation |
| P3.2 | TSC-0320 | Data minimization |
| **P4: Use, Retention, and Disposal** | TSC-0320 | Use and retention |
| P4.1 | TSC-0320 | Purpose limitation |
| P4.2 | TSC-0320 | Data retention |
| P4.3 | TSC-0320 | Secure disposal |
| **P5: Access** | TSC-0320 | Access |
| P5.1 | TSC-0320 | Data subject access requests |
| P5.2 | TSC-0320 | Data correction |
| **P6: Disclosure to Third Parties** | TSC-0320 | Disclosure |
| P6.1 | TSC-0320 | Third-party disclosures |
| P6.2 | TSC-0320 | Data processing agreements |
| **P7: Quality** | TSC-0320 | Data quality |
| P7.1 | TSC-0320 | Data accuracy |
| **P8: Monitoring and Enforcement** | TSC-0320 | Monitoring |
| P8.1 | TSC-0320 | Privacy compliance monitoring |

## Foundation Templates

| Template | Description | TSC Relevance |
|----------|-------------|---------------|
| TSC-0010 | System Description | System Description (Required for all SOC 2) |
| TSC-0020 | System Boundaries | System Boundaries (Required for all SOC 2) |
| TSC-0030 | System Components | Infrastructure, Software, People, Processes, Data |
| TSC-0040 | Roles and Responsibilities | Organizational Structure (CC1) |
| TSC-0050 | Control Environment | Control Environment (CC1) |

## Appendices

| Template | Description | TSC Relevance |
|----------|-------------|---------------|
| TSC-0400 | Control Matrix | Complete mapping of all controls |
| TSC-0410 | Evidence Documentation | Audit evidence repository |
| TSC-0420 | Test Results | Control testing results |
| TSC-0430 | Vendor Management | Subservice organization management |
| TSC-0440 | Glossary | TSC terminology |

## Coverage Analysis

### Common Criteria (CC) - 100% Coverage

All 9 Common Criteria (CC1-CC9) are fully covered:
- ✅ CC1: Control Environment (TSC-0100)
- ✅ CC2: Communication (TSC-0110)
- ✅ CC3: Risk Assessment (TSC-0120)
- ✅ CC4: Monitoring (TSC-0130)
- ✅ CC5: Control Activities (TSC-0140)
- ✅ CC6: Logical and Physical Access (TSC-0150)
- ✅ CC7: System Operations (TSC-0150)
- ✅ CC8: Change Management (TSC-0150)
- ✅ CC9: Risk Mitigation (TSC-0150)

### Optional Categories - 100% Coverage

All optional categories are fully covered:
- ✅ Availability (A1) - TSC-0200
- ✅ Processing Integrity (PI1) - TSC-0240
- ✅ Confidentiality (C1) - TSC-0280
- ✅ Privacy (P1-P8) - TSC-0320

## Gaps and Recommendations

### No Gaps Identified

All TSC criteria are covered by templates.

### Recommendations

1. **Customization:** Customize templates to your specific system environment
2. **Evidence Collection:** Collect evidence for each control
3. **Control Testing:** Perform regular control testing
4. **Documentation:** Keep documentation up to date
5. **Audit Preparation:** Prepare early for SOC 2 audit

## SOC 2 Report Types

### Type I Report

- **Scope:** Design of controls
- **Point in Time:** As of a specific date
- **Templates:** All templates relevant

### Type II Report

- **Scope:** Design and operating effectiveness of controls
- **Period of Time:** Over a period (6-12 months)
- **Templates:** All templates relevant + evidence of control effectiveness

## Usage

1. **Scope Definition:** Define which TSC categories are relevant for your SOC 2 audit
2. **Template Selection:** Select the appropriate templates
3. **Customization:** Customize templates to your organization
4. **Evidence Collection:** Collect evidence for each control
5. **Audit Preparation:** Prepare documentation for audit

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-07  
**Maintainer:** TSC-Template-Team

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
