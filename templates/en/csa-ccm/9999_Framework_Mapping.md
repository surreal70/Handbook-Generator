# CSA CCM Framework Mapping

**Document-ID:** [FRAMEWORK]-9999
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

## Overview

This document maps the handbook templates to specific CSA Cloud Controls Matrix (CCM) v4.0 controls.

## Mapping Structure

### Governance and Risk Management (0010-0099)

#### 0010_ccm_framework_overview.md
**Covered Control Domains**: All 16 domains (overview)
- Provides overview of the entire CCM framework
- Describes the 16 control domains
- Defines implementation approach

#### 0020_governance_enterprise_risk_management.md
**Control Domain**: GRC (Governance, Risk & Compliance)
- **GRC-01**: Baseline Requirements
- **GRC-02**: Governance Oversight
- **GRC-03**: Risk Management Program
- **GRC-04**: Policy
- **GRC-05**: Policy Enforcement
- **GRC-06**: Policy Impact on Risk Assessments
- **GRC-07**: Policy Reviews

#### 0030_risk_management_program.md
**Control Domain**: GRC (Governance, Risk & Compliance)
- **GRC-03**: Risk Management Program
- **GRC-06**: Policy Impact on Risk Assessments

### Application and Interface Security (0100-0199)

#### 0100_application_security_overview.md
**Control Domain**: AIS (Application & Interface Security)
- **AIS-01**: Application Security
- **AIS-02**: Application Security - Secure Design & Development
- **AIS-03**: Application Security - Application Security Testing
- **AIS-04**: Application Security - Application Security Monitoring

### Data Security and Privacy (0200-0299)

#### 0200_data_security_privacy_overview.md
**Control Domain**: DSP (Data Security & Privacy)
- **DSP-01**: Data Inventory / Flows
- **DSP-02**: Data Security / Integrity
- **DSP-03**: Data Classification
- **DSP-04**: Data Retention / Deletion
- **DSP-05**: Data Encryption at Rest
- **DSP-06**: Data Encryption in Transit
- **DSP-07**: Data Loss Prevention (DLP)
- **DSP-08**: Privacy

**Control Domain**: EKM (Encryption & Key Management)
- **EKM-01**: Encryption & Key Management
- **EKM-02**: Encryption & Key Management - Entitlement
- **EKM-03**: Encryption & Key Management - Key Generation
- **EKM-04**: Encryption & Key Management - Sensitive Data Protection

### Identity and Access Management (0300-0399)

IAM controls are implemented in individual templates (0310-0380).

### Infrastructure and Virtualization Security (0400-0499)

#### 0400_infrastructure_virtualization_security.md
**Control Domain**: IVS (Infrastructure & Virtualization Security)
- **IVS-01**: Infrastructure & Virtualization Security
- **IVS-02**: Network Security
- **IVS-03**: Network Security - Network Security Management
- **IVS-04**: Network Security - Perimeter Security
- **IVS-05**: Network Security - Wireless Security
- **IVS-06**: OS Hardening and Base Controls
- **IVS-07**: Production / Non-Production Environments
- **IVS-08**: Segmentation
- **IVS-09**: Virtualization Security

**Control Domain**: DCS (Datacenter Security)
- **DCS-01**: Datacenter Security
- **DCS-02**: Controlled Access Points
- **DCS-03**: Equipment Identification
- **DCS-04**: Off-Site Authorization
- **DCS-05**: Off-Site Equipment
- **DCS-06**: Physical Security - Perimeter
- **DCS-07**: Secure Area Authorization
- **DCS-08**: Unauthorized Persons Entry

### Security Operations (0500-0599)

Security Operations controls are implemented in individual templates (0540-0590).
- **SEF-01**: Security Incident Management
- **SEF-02**: Incident Management - Incident Response Plan
- **SEF-03**: Incident Management - Incident Response Metrics
- **SEF-04**: Incident Management - Incident Response Testing

**Control Domain**: TVM (Threat & Vulnerability Management)
- **TVM-01**: Threat & Vulnerability Management
- **TVM-02**: Vulnerability / Patch Management
- **TVM-03**: Mobile Code

**Control Domain**: BCR (Business Continuity Management & Operational Resilience)
- **BCR-01**: Business Continuity Management & Operational Resilience
- **BCR-02**: Business Continuity Planning
- **BCR-03**: Business Continuity Testing
- **BCR-04**: Environmental Risks
- **BCR-05**: Equipment Location
- **BCR-06**: Equipment Maintenance
- **BCR-07**: Equipment Power Failures
- **BCR-08**: Impact Analysis
- **BCR-09**: Policy
- **BCR-10**: Retention Policy

### Compliance and Audit (0600-0699)

#### 0600_compliance_audit_overview.md
**Control Domain**: AAC (Audit Assurance & Compliance)
- **AAC-01**: Audit Assurance & Compliance
- **AAC-02**: Audit Planning
- **AAC-03**: Independent Audits
- **AAC-04**: Audit Logging / Intrusion Detection
- **AAC-05**: Audit Tools Access

**Control Domain**: SCM (Supply Chain Management)
- **SCM-01**: Supply Chain Management
- **SCM-02**: Supply Chain Agreements
- **SCM-03**: Supply Chain Metrics
- **SCM-04**: Third Party Assessment

### Human Resources and Change Management (0700-0799)

#### 0700_human_resources_change_management.md
**Control Domain**: HRS (Human Resources)
- **HRS-01**: Human Resources Security
- **HRS-02**: Human Resources - Asset Returns
- **HRS-03**: Human Resources - Background Screening
- **HRS-04**: Human Resources - Employment Agreements
- **HRS-05**: Human Resources - Employment Termination
- **HRS-06**: Human Resources - Mobile Device Management
- **HRS-07**: Human Resources - Non-Disclosure Agreements
- **HRS-08**: Human Resources - Roles / Responsibilities
- **HRS-09**: Human Resources - Training / Awareness
- **HRS-10**: Human Resources - User Responsibility
- **HRS-11**: Human Resources - Workspace

**Control Domain**: CCC (Change Control & Configuration Management)
- **CCC-01**: Change Control & Configuration Management
- **CCC-02**: Change Control - Change Detection
- **CCC-03**: Change Control - Change Management
- **CCC-04**: Change Control - Configuration Management
- **CCC-05**: Change Control - New Development / Acquisition
- **CCC-06**: Change Control - Outsourced Development
- **CCC-07**: Change Control - Production Changes
- **CCC-08**: Change Control - Quality Testing
- **CCC-09**: Change Control - Unauthorized Software Installations

**Control Domain**: MOS (Mobile Security)
- **MOS-01**: Mobile Security
- **MOS-02**: Mobile Security - Anti-Malware
- **MOS-03**: Mobile Security - Application Stores
- **MOS-04**: Mobile Security - Approved Applications
- **MOS-05**: Mobile Security - Approved Software
- **MOS-06**: Mobile Security - Device Eligibility
- **MOS-07**: Mobile Security - Device Inventory
- **MOS-08**: Mobile Security - Device Management
- **MOS-09**: Mobile Security - Jailbreaking and Rooting
- **MOS-10**: Mobile Security - OS Versions
- **MOS-11**: Mobile Security - Remote Wipe
- **MOS-12**: Mobile Security - Security Patches
- **MOS-13**: Mobile Security - User Awareness

**Control Domain**: IPY (Interoperability & Portability)
- **IPY-01**: Interoperability & Portability
- **IPY-02**: Interoperability & Portability - APIs
- **IPY-03**: Interoperability & Portability - Data Request
- **IPY-04**: Interoperability & Portability - Policy & Legal
- **IPY-05**: Interoperability & Portability - Standardized Network Protocols

## Coverage Overview

| Control Domain | Number of Controls | Covered Templates |
|----------------|-------------------|-------------------|
| AIS | 4 | 0100 |
| AAC | 5 | 0600 |
| BCR | 10 | 0500 |
| CCC | 9 | 0700 |
| DSP | 8 | 0200 |
| DCS | 8 | 0400 |
| EKM | 4 | 0200 |
| GRC | 7 | 0020, 0030 |
| HRS | 11 | 0700 |
| IAM | 8 | 0300 |
| IVS | 9 | 0400 |
| IPY | 5 | 0700 |
| MOS | 13 | 0700 |
| SEF | 4 | 0500 |
| SCM | 4 | 0600 |
| TVM | 3 | 0500 |

**Total**: 112 CCM controls covered

## Usage Notes

1. **Complete Coverage**: The templates provide a basic structure for all 16 CCM control domains.

2. **Customization Required**: Each organization must adapt the templates to their specific cloud environments and services.

3. **Evidence Collection**: For each control, appropriate evidence and artifacts should be documented.

4. **Continuous Improvement**: The implementation of controls should be regularly reviewed and improved.

5. **Cross-Framework Mapping**: Use the CCM mappings to other standards (ISO 27001, NIST, etc.) for efficient compliance.

## References

- CSA Cloud Controls Matrix v4.0
- CSA Security Guidance for Critical Areas of Focus in Cloud Computing
- CSA STAR Certification and Attestation

