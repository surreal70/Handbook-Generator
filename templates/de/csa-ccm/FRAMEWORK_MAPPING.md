# CSA CCM Framework-Mapping

## Überblick

Dieses Dokument ordnet die Handbuch-Vorlagen den spezifischen CSA Cloud Controls Matrix (CCM) v4.0 Kontrollen zu.

## Mapping-Struktur

### Governance und Risk Management (0010-0099)

#### 0010_ccm_framework_overview.md
**Abgedeckte Kontrolldomänen**: Alle 16 Domänen (Übersicht)
- Bietet Überblick über das gesamte CCM-Framework
- Beschreibt die 16 Kontrolldomänen
- Definiert Implementierungsansatz

#### 0020_governance_enterprise_risk_management.md
**Kontrolldomäne**: GRC (Governance, Risk & Compliance)
- **GRC-01**: Baseline Requirements
- **GRC-02**: Governance Oversight
- **GRC-03**: Risk Management Program
- **GRC-04**: Policy
- **GRC-05**: Policy Enforcement
- **GRC-06**: Policy Impact on Risk Assessments
- **GRC-07**: Policy Reviews

#### 0030_risk_management_program.md
**Kontrolldomäne**: GRC (Governance, Risk & Compliance)
- **GRC-03**: Risk Management Program
- **GRC-06**: Policy Impact on Risk Assessments

### Anwendungs- und Schnittstellensicherheit (0100-0199)

#### 0100_application_security_overview.md
**Kontrolldomäne**: AIS (Application & Interface Security)
- **AIS-01**: Application Security
- **AIS-02**: Application Security - Secure Design & Development
- **AIS-03**: Application Security - Application Security Testing
- **AIS-04**: Application Security - Application Security Monitoring

### Datensicherheit und Datenschutz (0200-0299)

#### 0200_data_security_privacy_overview.md
**Kontrolldomäne**: DSP (Data Security & Privacy)
- **DSP-01**: Data Inventory / Flows
- **DSP-02**: Data Security / Integrity
- **DSP-03**: Data Classification
- **DSP-04**: Data Retention / Deletion
- **DSP-05**: Data Encryption at Rest
- **DSP-06**: Data Encryption in Transit
- **DSP-07**: Data Loss Prevention (DLP)
- **DSP-08**: Privacy

**Kontrolldomäne**: EKM (Encryption & Key Management)
- **EKM-01**: Encryption & Key Management
- **EKM-02**: Encryption & Key Management - Entitlement
- **EKM-03**: Encryption & Key Management - Key Generation
- **EKM-04**: Encryption & Key Management - Sensitive Data Protection

### Identitäts- und Zugriffsmanagement (0300-0399)

#### 0300_identity_access_management_overview.md
**Kontrolldomäne**: IAM (Identity & Access Management)
- **IAM-01**: Identity & Access Management
- **IAM-02**: Credential Lifecycle / Provision Management
- **IAM-03**: Authentication & Authorization
- **IAM-04**: Privileged User & Access Management
- **IAM-05**: User Access Reviews
- **IAM-06**: User Access Revocation
- **IAM-07**: User Access Policy
- **IAM-08**: User ID Credentials

### Infrastruktur- und Virtualisierungssicherheit (0400-0499)

#### 0400_infrastructure_virtualization_security.md
**Kontrolldomäne**: IVS (Infrastructure & Virtualization Security)
- **IVS-01**: Infrastructure & Virtualization Security
- **IVS-02**: Network Security
- **IVS-03**: Network Security - Network Security Management
- **IVS-04**: Network Security - Perimeter Security
- **IVS-05**: Network Security - Wireless Security
- **IVS-06**: OS Hardening and Base Controls
- **IVS-07**: Production / Non-Production Environments
- **IVS-08**: Segmentation
- **IVS-09**: Virtualization Security

**Kontrolldomäne**: DCS (Datacenter Security)
- **DCS-01**: Datacenter Security
- **DCS-02**: Controlled Access Points
- **DCS-03**: Equipment Identification
- **DCS-04**: Off-Site Authorization
- **DCS-05**: Off-Site Equipment
- **DCS-06**: Physical Security - Perimeter
- **DCS-07**: Secure Area Authorization
- **DCS-08**: Unauthorized Persons Entry

### Security Operations (0500-0599)

#### 0500_security_operations_overview.md
**Kontrolldomäne**: SEF (Security Incident Management)
- **SEF-01**: Security Incident Management
- **SEF-02**: Incident Management - Incident Response Plan
- **SEF-03**: Incident Management - Incident Response Metrics
- **SEF-04**: Incident Management - Incident Response Testing

**Kontrolldomäne**: TVM (Threat & Vulnerability Management)
- **TVM-01**: Threat & Vulnerability Management
- **TVM-02**: Vulnerability / Patch Management
- **TVM-03**: Mobile Code

**Kontrolldomäne**: BCR (Business Continuity Management & Operational Resilience)
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

### Compliance und Audit (0600-0699)

#### 0600_compliance_audit_overview.md
**Kontrolldomäne**: AAC (Audit Assurance & Compliance)
- **AAC-01**: Audit Assurance & Compliance
- **AAC-02**: Audit Planning
- **AAC-03**: Independent Audits
- **AAC-04**: Audit Logging / Intrusion Detection
- **AAC-05**: Audit Tools Access

**Kontrolldomäne**: SCM (Supply Chain Management)
- **SCM-01**: Supply Chain Management
- **SCM-02**: Supply Chain Agreements
- **SCM-03**: Supply Chain Metrics
- **SCM-04**: Third Party Assessment

### Personalwesen und Änderungsmanagement (0700-0799)

#### 0700_human_resources_change_management.md
**Kontrolldomäne**: HRS (Human Resources)
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

**Kontrolldomäne**: CCC (Change Control & Configuration Management)
- **CCC-01**: Change Control & Configuration Management
- **CCC-02**: Change Control - Change Detection
- **CCC-03**: Change Control - Change Management
- **CCC-04**: Change Control - Configuration Management
- **CCC-05**: Change Control - New Development / Acquisition
- **CCC-06**: Change Control - Outsourced Development
- **CCC-07**: Change Control - Production Changes
- **CCC-08**: Change Control - Quality Testing
- **CCC-09**: Change Control - Unauthorized Software Installations

**Kontrolldomäne**: MOS (Mobile Security)
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

**Kontrolldomäne**: IPY (Interoperability & Portability)
- **IPY-01**: Interoperability & Portability
- **IPY-02**: Interoperability & Portability - APIs
- **IPY-03**: Interoperability & Portability - Data Request
- **IPY-04**: Interoperability & Portability - Policy & Legal
- **IPY-05**: Interoperability & Portability - Standardized Network Protocols

## Abdeckungsübersicht

| Kontrolldomäne | Anzahl Kontrollen | Abgedeckte Vorlagen |
|----------------|-------------------|---------------------|
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

**Gesamt**: 112 CCM-Kontrollen abgedeckt

## Hinweise zur Verwendung

1. **Vollständige Abdeckung**: Die Vorlagen bieten eine Grundstruktur für alle 16 CCM-Kontrolldomänen.

2. **Anpassung erforderlich**: Jede Organisation muss die Vorlagen an ihre spezifischen Cloud-Umgebungen und -Services anpassen.

3. **Evidenz-Sammlung**: Für jede Kontrolle sollten entsprechende Nachweise und Evidenzen dokumentiert werden.

4. **Kontinuierliche Verbesserung**: Die Implementierung der Kontrollen sollte regelmäßig überprüft und verbessert werden.

5. **Cross-Framework-Mapping**: Nutzen Sie die CCM-Zuordnungen zu anderen Standards (ISO 27001, NIST, etc.) für effiziente Compliance.

## Referenzen

- CSA Cloud Controls Matrix v4.0
- CSA Security Guidance for Critical Areas of Focus in Cloud Computing
- CSA STAR Certification and Attestation
