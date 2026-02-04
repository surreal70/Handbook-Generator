# IT Framework Mapping Documentation

## Overview

This document provides detailed mappings between the handbook templates and established IT frameworks. The handbook generator supports four template types, each aligned with specific industry standards and best practices:

1. **IT-Operations**: ITIL v4, ISO 20000-1:2018, COBIT 2019
2. **BCM (Business Continuity Management)**: ISO 22301:2019, BSI BCM Standards
3. **ISMS (Information Security Management System)**: ISO/IEC 27001:2022 (including Amendment 1:2024), Annex A Controls
4. **BSI Grundschutz**: BSI Standards 200-1, 200-2, 200-3, BSI IT-Grundschutz Compendium

These mappings ensure that the templates align with industry best practices and compliance requirements.

## Table of Contents

1. [IT-Operations Framework Mapping](#it-operations-framework-mapping)
   - ITIL v4 Process Mapping
   - ISO 20000-1:2018 Compliance Mapping
   - COBIT 2019 Alignment
2. [BCM Framework Mapping](#bcm-framework-mapping)
   - ISO 22301:2019 Compliance Mapping
   - BSI BCM Standards Alignment
3. [ISMS Framework Mapping](#isms-framework-mapping)
   - ISO 27001:2022 Compliance Mapping
   - Annex A Controls Mapping
   - Amendment 1:2024 Updates
4. [BSI Grundschutz Framework Mapping](#bsi-grundschutz-framework-mapping)
   - BSI Standard 200-1 (ISMS)
   - BSI Standard 200-2 (Methodology)
   - BSI Standard 200-3 (Risk Analysis)
   - BSI Baustein References
5. [Cross-Framework Mapping](#cross-framework-mapping)
6. [Compliance Checklists](#compliance-checklists)
7. [Framework Version History](#framework-version-history)
8. [References](#references)

---

# IT-Operations Framework Mapping

## ITIL v4 Process Mapping

### Service Value System (SVS) Components

The IT-Operations templates support the ITIL v4 Service Value System through comprehensive coverage of service management practices.

#### General Management Practices

| Template | ITIL Practice | Description | Key Activities |
|---|---|---|---|
| **0070_Betriebskonzept** | Strategy Management | Defines operating models and strategic approach | - Define service strategy<br>- Establish operating models<br>- Align IT with business |
| **0060_Rollen** | Organizational Change Management | Defines roles and responsibilities | - Define organizational structure<br>- Establish RACI matrices<br>- Manage stakeholders |
| **0200_Kapazitaets** | Portfolio Management | Capacity and resource planning | - Plan capacity<br>- Optimize resources<br>- Forecast demand |
| **0280_Compliance** | Risk Management | Compliance and audit management | - Identify risks<br>- Implement controls<br>- Monitor compliance |

#### Service Management Practices

| Template | ITIL Practice | Description | Key Activities |
|---|---|---|---|
| **0110_Monitoring** | Monitoring and Event Management | Systematic observation of services and CIs | - Define monitoring strategy<br>- Configure event detection<br>- Implement alerting rules<br>- Create dashboards |
| **0120_Incident** | Incident Management | Restore normal service operation quickly | - Detect and log incidents<br>- Categorize and prioritize<br>- Investigate and diagnose<br>- Resolve and close |
| **0130_Problem** | Problem Management | Reduce likelihood and impact of incidents | - Identify problems<br>- Perform root cause analysis<br>- Implement workarounds<br>- Maintain known error database |
| **0140_Change** | Change Enablement | Ensure changes are assessed and authorized | - Request and assess changes<br>- Authorize changes (CAB)<br>- Implement and review<br>- Manage change schedule |
| **0140_Change** | Release Management | Make new and changed services available | - Plan releases<br>- Build and test<br>- Deploy and review<br>- Manage release schedule |
| **0090_Konfiguration** | Service Configuration Management | Maintain information about CIs | - Identify CIs<br>- Control CI lifecycle<br>- Maintain CMDB<br>- Verify configuration data |
| **0100_Access** | Service Desk | Single point of contact for users | - Handle service requests<br>- Manage incidents<br>- Provide information<br>- Coordinate support |
| **0210_Verfuegbarkeit** | Availability Management | Ensure services meet availability requirements | - Define availability requirements<br>- Monitor availability<br>- Analyze failures<br>- Improve availability |
| **0200_Kapazitaets** | Capacity and Performance Management | Ensure adequate capacity and performance | - Plan capacity<br>- Monitor performance<br>- Analyze trends<br>- Optimize resources |
| **0150_Backup** | Service Continuity Management | Ensure service continuity during disruptions | - Define backup strategies<br>- Implement backup procedures<br>- Test restore procedures<br>- Maintain backup schedules |
| **0160_Disaster_Recovery** | Service Continuity Management | Recover services after major disruptions | - Identify disaster scenarios<br>- Define recovery strategies<br>- Implement DR procedures<br>- Test DR plans |
| **0030_Service** | Service Level Management | Set clear targets for service performance | - Define SLAs and SLOs<br>- Monitor service levels<br>- Report performance<br>- Review and improve |
| **0030_Service** | Service Catalogue Management | Provide information about services | - Define service catalogue<br>- Maintain service information<br>- Publish service details<br>- Update regularly |

#### Technical Management Practices

| Template | ITIL Practice | Description | Key Activities |
|---|---|---|---|
| **0050_Infrastruktur** | Infrastructure and Platform Management | Oversee infrastructure and platforms | - Manage physical infrastructure<br>- Manage virtualization<br>- Manage cloud resources<br>- Maintain network infrastructure |
| **0140_Change** | Deployment Management | Move new or changed components to live | - Plan deployments<br>- Prepare deployment packages<br>- Execute deployments<br>- Verify deployments |
| **0170_Sicherheit** | Information Security Management | Protect information and assets | - Define security policies<br>- Implement security controls<br>- Monitor security events<br>- Manage vulnerabilities |

### ITIL Process Integration Points

```
┌─────────────────────────────────────────────────────────────┐
│                    Service Strategy                          │
│  (0070_Betriebskonzept, 0030_Service)                       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                    Service Design                            │
│  (0040_System, 0050_Infrastruktur, 0210_Verfuegbarkeit)    │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Service Transition                          │
│  (0140_Change, 0090_Konfiguration, 0080_Betriebsuebergabe) │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Service Operation                           │
│  (0120_Incident, 0110_Monitoring, 0100_Access)             │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Continual Service Improvement                   │
│  (0130_Problem, 0200_Kapazitaets, 0240_Postmortems)        │
└─────────────────────────────────────────────────────────────┘
```

## ISO 20000-1:2018 Compliance Mapping

### Service Management System (SMS) Requirements

| ISO Clause | Requirement | Template(s) | Implementation Notes |
|---|---|---|---|
| **4.1** | Understanding the organization and its context | 0010_Einleitung<br>0011_Rahmenbedingungen | Document organizational context, stakeholders, and constraints |
| **4.2** | Understanding needs and expectations | 0030_Service | Identify interested parties and their requirements |
| **4.3** | Determining scope of SMS | 0010_Einleitung | Define scope and boundaries of service management |
| **4.4** | Service management system | 0070_Betriebskonzept | Establish, implement, maintain, and improve SMS |
| **5.1** | Leadership and commitment | 0060_Rollen | Top management demonstrates leadership |
| **5.2** | Policy | 0070_Betriebskonzept | Establish service management policy |
| **5.3** | Organizational roles | 0060_Rollen | Assign responsibilities and authorities |
| **6.1** | Actions to address risks | 0160_Disaster_Recovery<br>0280_Compliance | Risk assessment and treatment |
| **6.2** | Service management objectives | 0030_Service<br>0210_Verfuegbarkeit | Define measurable objectives |
| **6.3** | Planning of changes | 0140_Change | Plan changes to SMS |
| **7.1** | Resources | 0050_Infrastruktur<br>0200_Kapazitaets | Determine and provide resources |
| **7.2** | Competence | 0060_Rollen | Ensure personnel competence |
| **7.3** | Awareness | 0060_Rollen | Ensure awareness of SMS |
| **7.4** | Communication | 0270_Kontakte | Internal and external communication |
| **7.5** | Documented information | 0020_Dokumentenlenkung | Control documented information |

### Service Management Processes

| ISO Clause | Process | Template(s) | Key Requirements |
|---|---|---|---|
| **8.1** | Operational planning and control | 0070_Betriebskonzept<br>0230_Wartung | Plan, implement, and control processes |
| **8.2** | Service portfolio | 0030_Service | Define and maintain service catalogue |
| **8.3** | Service level management | 0210_Verfuegbarkeit<br>0030_Service | Define, document, and monitor SLAs |
| **8.4** | Service reporting | 0110_Monitoring<br>0210_Verfuegbarkeit | Generate service reports |
| **8.5** | Service continuity and availability | 0150_Backup<br>0160_Disaster_Recovery<br>0210_Verfuegbarkeit | Ensure service continuity |
| **8.6** | Budgeting and accounting | 0200_Kapazitaets | Financial management for services |
| **8.7** | Capacity management | 0200_Kapazitaets | Ensure adequate capacity |
| **8.8** | Information security management | 0170_Sicherheit<br>0220_Datenmanagement | Manage information security |
| **9.1** | Monitoring, measurement, analysis | 0110_Monitoring | Monitor and measure SMS performance |
| **9.2** | Internal audit | 0280_Compliance | Conduct internal audits |
| **9.3** | Management review | 0280_Compliance | Review SMS effectiveness |
| **10.1** | Nonconformity and corrective action | 0130_Problem | Handle nonconformities |
| **10.2** | Continual improvement | 0130_Problem<br>0240_Runbooks | Improve SMS continuously |

### Relationship Management Processes

| ISO Clause | Process | Template(s) | Key Requirements |
|---|---|---|---|
| **8.2.2** | Business relationship management | 0030_Service | Establish and maintain business relationships |
| **8.2.3** | Supplier management | 0270_Kontakte | Manage suppliers and contracts |

### Resolution Processes

| ISO Clause | Process | Template(s) | Key Requirements |
|---|---|---|---|
| **8.3.1** | Incident management | 0120_Incident | Restore service quickly |
| **8.3.2** | Service request management | 0100_Access<br>0120_Incident | Fulfill service requests |
| **8.3.3** | Problem management | 0130_Problem | Identify and manage problems |

### Control Processes

| ISO Clause | Process | Template(s) | Key Requirements |
|---|---|---|---|
| **8.4.1** | Change management | 0140_Change | Control changes |
| **8.4.2** | Asset management | 0050_Infrastruktur<br>0090_Konfiguration | Manage assets throughout lifecycle |
| **8.4.3** | Configuration management | 0090_Konfiguration | Maintain configuration information |

## COBIT 2019 Alignment

### Governance and Management Objectives

#### Align, Plan and Organize (APO)

| COBIT Objective | Template(s) | Governance/Management | Key Focus Areas |
|---|---|---|---|
| **APO01** Managed IT Management Framework | 0070_Betriebskonzept | Management | - Define IT management framework<br>- Establish organizational structures<br>- Optimize IT processes |
| **APO02** Managed Strategy | 0010_Einleitung<br>0030_Service | Governance | - Define strategic plan<br>- Communicate strategy<br>- Manage strategic initiatives |
| **APO07** Managed Human Resources | 0060_Rollen | Management | - Maintain adequate staffing<br>- Define roles and responsibilities<br>- Manage competencies |
| **APO09** Managed Service Agreements | 0210_Verfuegbarkeit<br>0030_Service | Management | - Identify services and requirements<br>- Define and prepare service agreements<br>- Monitor and report service levels |
| **APO12** Managed Risk | 0160_Disaster_Recovery<br>0280_Compliance | Governance | - Collect data<br>- Analyze risk<br>- Maintain risk profile<br>- Articulate risk |
| **APO13** Managed Security | 0170_Sicherheit<br>0220_Datenmanagement | Governance | - Establish information security management<br>- Define security baseline<br>- Manage security measures |

#### Build, Acquire and Implement (BAI)

| COBIT Objective | Template(s) | Governance/Management | Key Focus Areas |
|---|---|---|---|
| **BAI03** Managed Solutions Identification and Build | 0040_System<br>0050_Infrastruktur | Management | - Design high-level solutions<br>- Acquire or develop solution components<br>- Build solutions |
| **BAI06** Managed IT Changes | 0140_Change | Management | - Evaluate, prioritize and authorize change requests<br>- Manage emergency changes<br>- Track and report change status |
| **BAI10** Managed Configuration | 0090_Konfiguration | Management | - Establish and maintain configuration model<br>- Establish and maintain configuration repository<br>- Maintain and control configuration items |

#### Deliver, Service and Support (DSS)

| COBIT Objective | Template(s) | Governance/Management | Key Focus Areas |
|---|---|---|---|
| **DSS01** Managed Operations | 0230_Wartung<br>0240_Runbooks | Management | - Execute operational procedures<br>- Manage IT infrastructure<br>- Manage facilities |
| **DSS02** Managed Service Requests and Incidents | 0120_Incident<br>0100_Access | Management | - Define incident classification<br>- Record, classify and prioritize requests<br>- Investigate, diagnose and allocate<br>- Resolve and recover |
| **DSS03** Managed Problems | 0130_Problem<br>0260_Bekannte_Probleme | Management | - Identify and classify problems<br>- Investigate and diagnose problems<br>- Raise known errors<br>- Resolve and close problems |
| **DSS04** Managed Continuity | 0150_Backup<br>0160_Disaster_Recovery | Management | - Define business continuity policy<br>- Maintain continuity strategy<br>- Develop and implement continuity plans<br>- Test continuity plans |
| **DSS05** Managed Security Services | 0170_Sicherheit<br>0180_Patch<br>0190_Log | Management | - Protect against malware<br>- Manage network and connectivity security<br>- Manage endpoint security<br>- Manage sensitive data |
| **DSS06** Managed Business Process Controls | 0280_Compliance<br>0220_Datenmanagement | Management | - Align IT activities with business requirements<br>- Manage IT processing<br>- Optimize business process controls |

#### Monitor, Evaluate and Assess (MEA)

| COBIT Objective | Template(s) | Governance/Management | Key Focus Areas |
|---|---|---|---|
| **MEA01** Managed Performance and Conformance Monitoring | 0110_Monitoring<br>0200_Kapazitaets | Governance | - Establish monitoring approach<br>- Set performance and conformance targets<br>- Collect and process data<br>- Report performance |
| **MEA02** Managed System of Internal Control | 0280_Compliance | Governance | - Monitor internal controls<br>- Review business process controls<br>- Perform control self-assessments |
| **MEA03** Managed Compliance With External Requirements | 0280_Compliance | Governance | - Identify external compliance requirements<br>- Optimize response to external requirements<br>- Confirm external compliance |

### COBIT Design Factors

The templates consider the following COBIT design factors:

1. **Enterprise Strategy** - Addressed in 0010_Einleitung, 0030_Service
2. **Enterprise Goals** - Addressed in 0030_Service, 0210_Verfuegbarkeit
3. **Risk Profile** - Addressed in 0160_Disaster_Recovery, 0280_Compliance
4. **IT-Related Issues** - Addressed throughout all templates
5. **Threat Landscape** - Addressed in 0170_Sicherheit, 0180_Patch
6. **Compliance Requirements** - Addressed in 0280_Compliance
7. **Role of IT** - Addressed in 0070_Betriebskonzept
8. **Sourcing Model** - Addressed in 0270_Kontakte
9. **IT Implementation Methods** - Addressed in 0140_Change
10. **Technology Adoption Strategy** - Addressed in 0050_Infrastruktur
11. **Enterprise Size** - Adaptable through template customization


---

# BCM Framework Mapping

## ISO 22301:2019 Compliance Mapping

### Business Continuity Management System (BCMS) Requirements

| ISO Clause | Requirement | Template(s) | Implementation Notes |
|---|---|---|---|
| **4.1** | Understanding the organization | 0010_Zweck_und_Geltungsbereich | Document organizational context for BCM |
| **4.2** | Understanding stakeholder needs | 0010_Zweck_und_Geltungsbereich | Identify interested parties and BCM requirements |
| **4.3** | Determining scope of BCMS | 0010_Zweck_und_Geltungsbereich | Define BCM scope and boundaries |
| **4.4** | Business continuity management system | 0020_BCM_Leitlinie_Policy | Establish, implement, maintain BCMS |
| **5.1** | Leadership and commitment | 0020_BCM_Leitlinie_Policy<br>0040_Notfallorganisation | Top management demonstrates BCM leadership |
| **5.2** | Policy | 0020_BCM_Leitlinie_Policy | Establish BCM policy |
| **5.3** | Organizational roles | 0040_Notfallorganisation<br>0060_Service_und_Prozesskatalog | Assign BCM responsibilities |
| **6.1** | Actions to address risks | 0090_Risikoanalyse | Risk assessment for business continuity |
| **6.2** | BC objectives | 0080_BIA_Ergebnisse | Define measurable BC objectives |
| **7.1** | Resources | 0190_Ressourcenplanung | Determine and provide BC resources |
| **7.2** | Competence | 0260_Schulungen | Ensure BCM competence |
| **7.3** | Awareness | 0260_Schulungen | Ensure BCM awareness |
| **7.4** | Communication | 0050_Kontakte<br>0130_Kommunikationsplan | Internal and external BC communication |
| **7.5** | Documented information | 0030_Dokumentenlenkung | Control BCM documented information |
| **8.1** | Operational planning | 0100_Strategie<br>0110_Aktivierungskriterien | Plan and control BCM processes |
| **8.2** | Business impact analysis | 0070_BIA_Methodik<br>0080_BIA_Ergebnisse | Conduct BIA, determine RTO/RPO |
| **8.3** | Business continuity strategy | 0100_Strategie | Determine BC strategies |
| **8.4** | BC procedures | 0120_Krisenmanagementplan<br>0140_BCP<br>0150_DRP | Establish and implement BC procedures |
| **8.5** | Exercising and testing | 0220_Uebungs_und_Testprogramm<br>0230_Testprotokoll | Test BC arrangements |
| **9.1** | Monitoring and measurement | 0250_Pflege_Review_und_KPIs | Monitor BCMS performance |
| **9.2** | Internal audit | 0270_Compliance_Audit | Conduct BCM audits |
| **9.3** | Management review | 0250_Pflege_Review_und_KPIs | Review BCMS effectiveness |
| **10.1** | Nonconformity and corrective action | 0240_Nachbereitung_Postmortem | Handle BC nonconformities |
| **10.2** | Continual improvement | 0250_Pflege_Review_und_KPIs | Improve BCMS continuously |

### BCM Key Processes

| Process Area | Templates | ISO 22301 Clauses | Key Activities |
|---|---|---|---|
| **Policy and Program Management** | 0020_BCM_Leitlinie<br>0040_Notfallorganisation<br>0050_Kontakte | 5.2, 5.3 | - Establish BCM policy<br>- Define BCM organization<br>- Assign roles and responsibilities |
| **Business Impact Analysis** | 0060_Service_und_Prozesskatalog<br>0070_BIA_Methodik<br>0080_BIA_Ergebnisse | 8.2 | - Identify critical processes<br>- Determine RTO/RPO<br>- Assess impact of disruptions |
| **Risk Assessment** | 0090_Risikoanalyse | 6.1, 8.2.3 | - Identify threats and vulnerabilities<br>- Assess likelihood and impact<br>- Determine risk treatment |
| **Business Continuity Strategies** | 0100_Strategie<br>0170_Alternativstandort<br>0180_Lieferanten | 8.3 | - Define continuity options<br>- Select appropriate strategies<br>- Plan alternative sites |
| **BC Plans and Procedures** | 0120_Krisenmanagementplan<br>0140_BCP<br>0150_DRP<br>0160_Backup | 8.4 | - Develop crisis management plans<br>- Create business continuity plans<br>- Establish IT disaster recovery<br>- Define backup procedures |
| **Testing and Exercising** | 0220_Uebungs_und_Testprogramm<br>0230_Testprotokoll<br>0240_Nachbereitung | 8.5 | - Plan BC exercises<br>- Conduct tests and drills<br>- Document results<br>- Implement improvements |
| **Awareness and Training** | 0260_Schulungen | 7.2, 7.3 | - Develop training programs<br>- Conduct awareness campaigns<br>- Ensure competence |
| **Maintenance and Review** | 0250_Pflege_Review_und_KPIs<br>0270_Compliance_Audit | 9.1, 9.2, 9.3 | - Monitor KPIs<br>- Conduct audits<br>- Perform management reviews<br>- Update plans |

## BSI BCM Standards Alignment

### BSI Standard 100-4 (Business Continuity Management)

| BSI 100-4 Section | Template(s) | Key Requirements |
|---|---|---|
| **3.1** BCM Policy | 0020_BCM_Leitlinie_Policy | Management commitment, BCM objectives |
| **3.2** BCM Organization | 0040_Notfallorganisation | BCM roles, crisis management team |
| **3.3** BCM Concept | 0070_BIA_Methodik<br>0100_Strategie | BIA methodology, continuity strategies |
| **3.4** Business Impact Analysis | 0060_Service_und_Prozesskatalog<br>0080_BIA_Ergebnisse | Critical process identification, impact assessment |
| **3.5** Continuity Strategy | 0100_Strategie<br>0170_Alternativstandort | Recovery strategies, alternative sites |
| **3.6** Emergency Management** | 0110_Aktivierungskriterien<br>0120_Krisenmanagementplan | Activation criteria, crisis management |
| **3.7** BC Plans | 0140_BCP<br>0150_DRP | Business continuity plans, IT recovery plans |
| **3.8** Tests and Exercises | 0220_Uebungs_und_Testprogramm<br>0230_Testprotokoll | Test planning, execution, evaluation |
| **3.9** Awareness and Training | 0260_Schulungen | Training programs, awareness campaigns |
| **3.10** Maintenance | 0250_Pflege_Review_und_KPIs | Plan updates, continuous improvement |

### BCM Template Structure

```
BCM Templates (30 files, 0010-0290):
├── Foundation (0010-0050): Scope, Policy, Organization, Contacts
├── Analysis (0060-0090): Service Catalog, BIA, Risk Analysis
├── Strategy & Planning (0100-0180): Strategies, Plans, Resources
├── Operations (0190-0210): Resources, Emergency Access, Cyber Incidents
├── Testing & Improvement (0220-0260): Exercises, Reviews, Training
└── Compliance & Appendices (0270-0290): Audits, Templates, Glossary
```

---

# ISMS Framework Mapping

## ISO 27001:2022 Compliance Mapping

### Information Security Management System (ISMS) Requirements

| ISO Clause | Requirement | Template(s) | Implementation Notes |
|---|---|---|---|
| **4.1** | Understanding the organization | 0030_ISMS_Kontext | Document organizational context for ISMS |
| **4.2** | Understanding stakeholder needs | 0030_ISMS_Kontext | Identify interested parties and security requirements |
| **4.3** | Determining scope of ISMS | 0020_ISMS_Geltungsbereich | Define ISMS scope and boundaries |
| **4.4** | Information security management system | 0010_ISMS_Informationssicherheitsleitlinie | Establish, implement, maintain ISMS |
| **5.1** | Leadership and commitment | 0010_ISMS_Informationssicherheitsleitlinie<br>0040_ISMS_Governance | Top management demonstrates security leadership |
| **5.2** | Policy | 0010_ISMS_Informationssicherheitsleitlinie | Establish information security policy |
| **5.3** | Organizational roles | 0040_ISMS_Governance | Assign ISMS responsibilities and authorities |
| **6.1.1** | General (Risk assessment) | 0060_ISMS_Risikomanagement<br>0080_ISMS_Risikoregister | Establish risk assessment process |
| **6.1.2** | Information security risk assessment | 0080_ISMS_Risikoregister | Identify and analyze risks |
| **6.1.3** | Information security risk treatment | 0090_ISMS_Risikobehandlungsplan | Select and implement risk treatment options |
| **6.1.4** | Statement of Applicability | 0100_ISMS_SoA | Document Annex A control applicability |
| **6.2** | Information security objectives | 0110_ISMS_Sicherheitsziele | Define measurable security objectives |
| **7.1** | Resources | 0040_ISMS_Governance | Determine and provide ISMS resources |
| **7.2** | Competence | 0120_ISMS_Schulung | Ensure personnel competence |
| **7.3** | Awareness | 0120_ISMS_Schulung | Ensure security awareness |
| **7.4** | Communication | 0040_ISMS_Governance | Internal and external ISMS communication |
| **7.5** | Documented information | 0050_ISMS_Dokumentenlenkung | Control ISMS documented information |
| **8.1** | Operational planning and control | 0100_ISMS_SoA<br>Policies 0200-0680 | Plan, implement, control security processes |
| **9.1** | Monitoring, measurement, analysis | 0110_ISMS_Sicherheitsziele | Monitor ISMS performance |
| **9.2** | Internal audit | 0130_ISMS_Internes_Auditprogramm | Conduct ISMS audits |
| **9.3** | Management review | 0140_ISMS_Management_Review | Review ISMS effectiveness |
| **10.1** | Nonconformity and corrective action | 0150_ISMS_Nichtkonformitaeten | Handle security nonconformities |
| **10.2** | Continual improvement | 0160_ISMS_Kontinuierliche_Verbesserung | Improve ISMS continuously |

## Annex A Controls Mapping (ISO 27001:2022)

### Organizational Controls (5.x)

| Control | Title | Template(s) | Implementation Guidance |
|---|---|---|---|
| **5.1** | Policies for information security | 0010_ISMS_Informationssicherheitsleitlinie<br>Policies 0200-0680 | Information security policy framework |
| **5.2** | Information security roles and responsibilities | 0040_ISMS_Governance | RACI matrices, role definitions |
| **5.3** | Segregation of duties | 0040_ISMS_Governance | Separation of conflicting responsibilities |
| **5.7** | Threat intelligence | 0340_Policy_Vulnerability<br>0350_Richtlinie_Scans | Threat monitoring and intelligence |
| **5.8** | Information security in project management | 0680_Policy_Security_in_Projects<br>0690_Richtlinie_Projektlebenszyklus | Security requirements in projects |
| **5.10** | Acceptable use of information | 0200_Policy_Akzeptable_Nutzung<br>0210_Richtlinie_Akzeptable_Nutzung | Acceptable use policy |
| **5.14** | Information transfer | 0660_Policy_Informationsuebertragung<br>0670_Richtlinie_Email_Sharing | Secure information transfer |
| **5.15** | Access control | 0220_Policy_Zugriffssteuerung<br>0230_Richtlinie_IAM | Access control policy |
| **5.16** | Identity management | 0220_Policy_Zugriffssteuerung<br>0230_Richtlinie_IAM | Identity lifecycle management |
| **5.17** | Authentication information | 0240_Policy_Authentisierung<br>0250_Richtlinie_MFA | Authentication and password management |
| **5.18** | Access rights | 0220_Policy_Zugriffssteuerung<br>0230_Richtlinie_IAM | Access rights management |
| **5.19** | Information security in supplier relationships | 0460_Policy_Lieferanten<br>0470_Richtlinie_Third_Party | Supplier security management |
| **5.20** | Addressing information security in supplier agreements | 0460_Policy_Lieferanten<br>0470_Richtlinie_Third_Party | Security clauses in contracts |
| **5.23** | Information security for cloud services | 0460_Policy_Lieferanten<br>0470_Richtlinie_Cloud_Controls | Cloud security controls |
| **5.24** | Information security incident management | 0400_Policy_Incident<br>0410_Richtlinie_Incident_Response | Incident management process |
| **5.25** | Assessment of information security events | 0400_Policy_Incident<br>0410_Richtlinie_Incident_Response | Event assessment and classification |
| **5.26** | Response to information security incidents | 0400_Policy_Incident<br>0410_Richtlinie_Incident_Response | Incident response procedures |
| **5.27** | Learning from information security incidents | 0400_Policy_Incident<br>0410_Richtlinie_Incident_Response | Post-incident analysis |
| **5.28** | Collection of evidence | 0400_Policy_Incident<br>0410_Richtlinie_Forensik | Forensic evidence handling |
| **5.29** | Information security during disruption | 0440_Policy_Business_Continuity<br>0450_Richtlinie_ICT_DR | ICT continuity planning |
| **5.30** | ICT readiness for business continuity | 0440_Policy_Business_Continuity<br>0450_Richtlinie_ICT_DR | ICT disaster recovery |
| **5.31** | Legal, statutory, regulatory requirements | 0560_Policy_Datenschutz<br>0570_Richtlinie_Datenschutz | Compliance with legal requirements |
| **5.32** | Intellectual property rights | 0560_Policy_Datenschutz<br>0570_Richtlinie_Datenverarbeitung | Protection of intellectual property |
| **5.33** | Protection of records | 0580_Policy_Aufbewahrung<br>0590_Richtlinie_Records_Retention | Records management |
| **5.34** | Privacy and protection of PII | 0560_Policy_Datenschutz<br>0570_Richtlinie_Datenschutz | GDPR compliance, PII protection |
| **5.35** | Independent review of information security | 0130_ISMS_Internes_Auditprogramm | Independent ISMS audits |
| **5.36** | Compliance with policies | 0130_ISMS_Internes_Auditprogramm | Policy compliance monitoring |
| **5.37** | Documented operating procedures | Guidelines 0210-0690 | Detailed operational procedures |

### People Controls (6.x)

| Control | Title | Template(s) | Implementation Guidance |
|---|---|---|---|
| **6.1** | Screening | 0520_Policy_HR_Security<br>0530_Richtlinie_HR_Onboarding | Background checks, screening procedures |
| **6.2** | Terms and conditions of employment | 0520_Policy_HR_Security<br>0530_Richtlinie_HR_Onboarding | Security responsibilities in contracts |
| **6.3** | Information security awareness | 0120_ISMS_Schulung | Awareness training programs |
| **6.4** | Disciplinary process | 0520_Policy_HR_Security<br>0530_Richtlinie_HR_Offboarding | Security violation handling |
| **6.5** | Responsibilities after termination | 0520_Policy_HR_Security<br>0530_Richtlinie_HR_Offboarding | Offboarding security procedures |
| **6.6** | Confidentiality agreements | 0520_Policy_HR_Security<br>0530_Richtlinie_HR_Onboarding | NDAs and confidentiality |
| **6.7** | Remote working | 0500_Policy_Mobile_Device<br>0510_Richtlinie_Remote_Access | Remote work security |
| **6.8** | Information security event reporting | 0400_Policy_Incident<br>0410_Richtlinie_Incident_Response | Incident reporting procedures |

### Physical Controls (7.x)

| Control | Title | Template(s) | Implementation Guidance |
|---|---|---|---|
| **7.1** | Physical security perimeters | 0480_Policy_Physische_Sicherheit<br>0490_Richtlinie_Zutritt | Physical access controls |
| **7.2** | Physical entry | 0480_Policy_Physische_Sicherheit<br>0490_Richtlinie_Zutritt | Entry controls and visitor management |
| **7.3** | Securing offices, rooms and facilities | 0480_Policy_Physische_Sicherheit<br>0490_Richtlinie_Equipment | Office and facility security |
| **7.4** | Physical security monitoring | 0480_Policy_Physische_Sicherheit<br>0490_Richtlinie_Zutritt | Surveillance and monitoring |
| **7.7** | Clear desk and clear screen | 0480_Policy_Physische_Sicherheit<br>0490_Richtlinie_Equipment | Clean desk policy |
| **7.8** | Equipment siting and protection | 0480_Policy_Physische_Sicherheit<br>0490_Richtlinie_Equipment | Equipment protection |
| **7.10** | Storage media | 0280_Policy_Datenklassifizierung<br>0290_Richtlinie_Handling | Media handling and storage |
| **7.11** | Supporting utilities | 0480_Policy_Physische_Sicherheit | Power, cooling, infrastructure |
| **7.12** | Cabling security | 0480_Policy_Physische_Sicherheit | Network cabling protection |
| **7.13** | Equipment maintenance | 0480_Policy_Physische_Sicherheit<br>0490_Richtlinie_Equipment | Maintenance procedures |
| **7.14** | Secure disposal of equipment | 0300_Policy_Asset<br>0310_Richtlinie_Entsorgung | Secure equipment disposal |

### Technological Controls (8.x)

| Control | Title | Template(s) | Implementation Guidance |
|---|---|---|---|
| **8.1** | User endpoint devices | 0620_Policy_Endpoint<br>0630_Richtlinie_EDR | Endpoint security controls |
| **8.2** | Privileged access rights | 0220_Policy_Zugriffssteuerung<br>0230_Richtlinie_IAM | Privileged account management |
| **8.3** | Information access restriction | 0220_Policy_Zugriffssteuerung<br>0230_Richtlinie_IAM | Access control implementation |
| **8.4** | Access to source code | 0380_Policy_Secure_Development<br>0390_Richtlinie_Secure_SDLC | Source code access control |
| **8.5** | Secure authentication | 0240_Policy_Authentisierung<br>0250_Richtlinie_MFA | MFA and authentication |
| **8.6** | Capacity management | 0200_Kapazitaets (IT-Ops) | Capacity planning and monitoring |
| **8.7** | Protection against malware | 0620_Policy_Endpoint<br>0630_Richtlinie_AV | Antivirus and anti-malware |
| **8.8** | Management of technical vulnerabilities | 0340_Policy_Vulnerability<br>0350_Richtlinie_Scans_Patching | Vulnerability management |
| **8.9** | Configuration management | 0540_Policy_Konfiguration<br>0550_Richtlinie_Sicherheitsbaselines | Configuration and hardening |
| **8.10** | Information deletion | 0580_Policy_Aufbewahrung<br>0590_Richtlinie_Sichere_Loeschung | Secure data deletion |
| **8.11** | Data masking | 0280_Policy_Datenklassifizierung<br>0290_Richtlinie_Handling | Data masking and anonymization |
| **8.12** | Data leakage prevention | 0280_Policy_Datenklassifizierung<br>0290_Richtlinie_Weitergabe | DLP controls |
| **8.13** | Information backup | 0420_Policy_Backup<br>0430_Richtlinie_Backup_Restore | Backup procedures |
| **8.14** | Redundancy of information processing | 0440_Policy_Business_Continuity<br>0450_Richtlinie_ICT_DR | Redundancy and high availability |
| **8.15** | Logging | 0320_Policy_Logging<br>0330_Richtlinie_SIEM | Logging and audit trails |
| **8.16** | Monitoring activities | 0320_Policy_Logging<br>0330_Richtlinie_SIEM | Security monitoring |
| **8.17** | Clock synchronization | 0320_Policy_Logging<br>0330_Richtlinie_Log_Standards | Time synchronization (NTP) |
| **8.18** | Use of privileged utility programs | 0220_Policy_Zugriffssteuerung<br>0230_Richtlinie_IAM | Privileged utility control |
| **8.19** | Installation of software | 0360_Policy_Change<br>0370_Richtlinie_Change_Management | Software installation controls |
| **8.20** | Networks security | 0600_Policy_Netzwerksicherheit<br>0610_Richtlinie_Segmentierung | Network security controls |
| **8.21** | Security of network services | 0600_Policy_Netzwerksicherheit<br>0610_Richtlinie_Firewalling | Network service security |
| **8.22** | Segregation of networks | 0600_Policy_Netzwerksicherheit<br>0610_Richtlinie_Segmentierung | Network segmentation |
| **8.23** | Web filtering | 0600_Policy_Netzwerksicherheit<br>0610_Richtlinie_Network_Access | Web filtering controls |
| **8.24** | Use of cryptography | 0260_Policy_Kryptografie<br>0270_Richtlinie_Key_Management | Cryptographic controls |
| **8.25** | Secure development life cycle | 0380_Policy_Secure_Development<br>0390_Richtlinie_Secure_SDLC | Secure SDLC implementation |
| **8.26** | Application security requirements | 0380_Policy_Secure_Development<br>0390_Richtlinie_Code_Reviews | Application security standards |
| **8.27** | Secure system architecture | 0380_Policy_Secure_Development<br>0390_Richtlinie_Secure_SDLC | Secure architecture design |
| **8.28** | Secure coding | 0380_Policy_Secure_Development<br>0390_Richtlinie_SAST_DAST | Secure coding practices |
| **8.29** | Security testing | 0380_Policy_Secure_Development<br>0390_Richtlinie_SAST_DAST | Security testing (SAST/DAST) |
| **8.30** | Outsourced development | 0460_Policy_Lieferanten<br>0470_Richtlinie_Third_Party | Third-party development security |
| **8.31** | Separation of environments | 0380_Policy_Secure_Development<br>0390_Richtlinie_Secure_SDLC | Dev/Test/Prod separation |
| **8.32** | Change management | 0360_Policy_Change<br>0370_Richtlinie_Change_Management | Change control process |
| **8.33** | Test information | 0380_Policy_Secure_Development<br>0390_Richtlinie_Secure_SDLC | Test data management |
| **8.34** | Protection of information systems during audit | 0130_ISMS_Internes_Auditprogramm | Audit controls |

## Amendment 1:2024 Updates

ISO 27001:2022 Amendment 1:2024 introduced minor clarifications and corrections. The ISMS templates incorporate these updates:

- **Clarification of control objectives**: Enhanced descriptions in policy templates
- **Updated terminology**: Consistent use of "information security event" vs "incident"
- **Risk assessment guidance**: Improved risk assessment methodology in 0060_ISMS_Risikomanagement
- **Cloud security emphasis**: Enhanced cloud controls in 0460_Policy_Lieferanten

### ISMS Three-Tier Structure

```
ISMS Templates (~50 files, 0010-0740):
├── Basis ISMS (0010-0160): Foundation, Scope, Context, Governance, Risk Management
├── Abstract Policies (0200-0680, even): High-level security policies (25 policies)
├── Detailed Guidelines (0210-0690, odd): Implementation guidance (24 guidelines)
└── Appendices (0710-0740): Annex A Mapping, Assets, Data Flows, Glossary
```

---

# BSI Grundschutz Framework Mapping

## BSI Standard 200-1: ISMS

### ISMS Requirements per BSI 200-1

| BSI 200-1 Section | Requirement | Template(s) | Implementation Notes |
|---|---|---|---|
| **4.1** | Information security policy | 0010_Informationssicherheitsleitlinie | Management commitment, security objectives |
| **4.2** | Information security organization | 0020_ISMS_Organisation | ISMS roles, responsibilities, RACI |
| **4.3** | Personnel for information security | 0020_ISMS_Organisation<br>0600_Schulung | ISB, CISO, security team |
| **4.4** | Scope and boundaries | 0040_Geltungsbereich | Information domain definition |
| **4.5** | Information security concept | 0100_Sicherheitskonzept | Comprehensive security concept |
| **5.1** | Management responsibility | 0010_Informationssicherheitsleitlinie | Top management commitment |
| **5.2** | Resources | 0020_ISMS_Organisation | Adequate resources for ISMS |
| **5.3** | Competence and awareness | 0600_Schulung | Training and awareness programs |
| **6.1** | Structure analysis | 0050_Strukturanalyse | Asset identification, dependencies |
| **6.2** | Protection needs assessment | 0060_Schutzbedarfsfeststellung | Confidentiality, integrity, availability |
| **6.3** | Modeling | 0070_Modellierung | BSI Baustein assignment |
| **6.4** | IT-Grundschutz-Check | 0080_Basis_Sicherheitscheck | Gap analysis, implementation status |
| **6.5** | Risk analysis | 0090_Risikoanalyse | Risk analysis per BSI 200-3 |
| **6.6** | Consolidation | 0100_Sicherheitskonzept | Consolidated security concept |
| **7.1** | Implementation planning | 0100_Sicherheitskonzept<br>0110_Umsetzungssteuerung | Measure planning and prioritization |
| **7.2** | Implementation | Policies 0200-0530 | Security measure implementation |
| **7.3** | Monitoring | 0110_Umsetzungssteuerung | Implementation monitoring, KPIs |
| **8.1** | Audits | 0610_Internes_Auditprogramm | Internal ISMS audits |
| **8.2** | Management review | 0620_Managementbewertung | Management review process |
| **8.3** | Continuous improvement | 0630_Nichtkonformitaeten | Corrective actions, improvements |

## BSI Standard 200-2: IT-Grundschutz Methodology

### IT-Grundschutz Process Steps

| Process Step | BSI 200-2 Phase | Template(s) | Key Activities |
|---|---|---|---|
| **1. Initiation** | Initialization | 0010_Informationssicherheitsleitlinie<br>0020_ISMS_Organisation | - Define security policy<br>- Establish ISMS organization<br>- Obtain management commitment |
| **2. Scope Definition** | Scope | 0040_Geltungsbereich | - Define information domain<br>- Identify boundaries<br>- Document scope |
| **3. Structure Analysis** | Modeling | 0050_Strukturanalyse | - Identify assets<br>- Document dependencies<br>- Create network diagrams |
| **4. Protection Needs** | Modeling | 0060_Schutzbedarfsfeststellung | - Assess confidentiality needs<br>- Assess integrity needs<br>- Assess availability needs |
| **5. Modeling** | Modeling | 0070_Modellierung | - Select BSI Bausteine<br>- Assign to target objects<br>- Document modeling |
| **6. IT-Grundschutz-Check** | Basis-Security-Check | 0080_Basis_Sicherheitscheck | - Compare with requirements<br>- Identify gaps<br>- Document implementation status |
| **7. Risk Analysis** | Supplementary Security Analysis | 0090_Risikoanalyse | - Identify additional risks<br>- Assess threats<br>- Determine treatment |
| **8. Security Concept** | Consolidation | 0100_Sicherheitskonzept | - Consolidate measures<br>- Create implementation plan<br>- Prioritize actions |
| **9. Implementation** | Implementation | Policies 0200-0530 | - Implement measures<br>- Document implementation<br>- Verify effectiveness |
| **10. Monitoring** | Continuous Improvement | 0110_Umsetzungssteuerung<br>0610_Internes_Auditprogramm | - Monitor KPIs<br>- Conduct audits<br>- Review and improve |

## BSI Standard 200-3: Risk Analysis

### Risk Analysis per BSI 200-3

| Risk Analysis Step | Template | Key Activities |
|---|---|---|
| **1. Preparation** | 0090_Risikoanalyse | Define risk analysis scope, identify assets requiring additional analysis |
| **2. Threat Identification** | 0090_Risikoanalyse | Identify relevant threats from BSI threat catalog |
| **3. Vulnerability Assessment** | 0090_Risikoanalyse | Assess vulnerabilities that could be exploited |
| **4. Risk Determination** | 0090_Risikoanalyse | Calculate risk levels (likelihood × impact) |
| **5. Risk Treatment** | 0090_Risikoanalyse<br>0100_Sicherheitskonzept | Select treatment options: avoid, reduce, transfer, accept |
| **6. Risk Acceptance** | 0520_Policy_Ausnahmenprozess<br>0530_Richtlinie_Risk_Waiver | Document risk acceptance decisions |
| **7. Documentation** | 0090_Risikoanalyse | Document complete risk analysis process and results |

## BSI Baustein References

### BSI IT-Grundschutz Compendium Bausteine

The BSI Grundschutz templates reference relevant BSI Bausteine throughout. Key Baustein mappings:

| Baustein Category | Bausteine | Template(s) | Coverage |
|---|---|---|---|
| **ISMS** | ISMS.1 | 0010_Informationssicherheitsleitlinie<br>0020_ISMS_Organisation | Security management |
| **Organization** | ORP.1-ORP.5 | 0020_ISMS_Organisation<br>0600_Schulung | Organization, personnel, awareness |
| **Concepts** | CON.1-CON.10 | 0260_Policy_Konfiguration<br>0340_Policy_Kryptografie<br>0420_Policy_Datenschutz | Crypto, data protection, archiving |
| **Operations** | OPS.1.1-OPS.1.2 | 0440_Policy_Backup<br>0180_Patch | Backup, patch management |
| **Detection** | DER.1-DER.4 | 0320_Policy_Incident<br>0300_Policy_Logging | Incident management, logging |
| **Applications** | APP.1-APP.7 | 0360_Policy_Secure_Development | Application security |
| **IT Systems** | SYS.1-SYS.4 | 0480_Policy_Endpoint<br>0600_Policy_Netzwerksicherheit | Servers, clients, networks |
| **Industrial IT** | IND.1-IND.3 | (Customizable) | OT/ICS security |
| **Networks** | NET.1-NET.4 | 0600_Policy_Netzwerksicherheit<br>0460_Policy_Netzwerk | Network infrastructure |
| **Infrastructure** | INF.1-INF.12 | 0500_Policy_Physische_Sicherheit | Physical security, facilities |

### BSI Grundschutz Template Structure

```
BSI Grundschutz Templates (~40 files, 0010-0740):
├── ISMS Foundation (0010-0100): Policy, Organization, Scope, Structure Analysis, Protection Needs
├── Security Concept (0100-0110): Gap Analysis, Risk Analysis, Measures, Implementation Control
├── Policies & Guidelines (0200-0530): 17 Policy-Guideline pairs for security areas
├── Management Processes (0600-0630): Training, Audits, Management Review, Non-conformities
└── Appendices (0700-0740): Evidence Register, Asset Inventory, Data Flows, Diagrams, Glossary
```

---

# CIS Controls v8 Structure (Preparation)

## Overview

The CIS Controls v8 framework provides a prioritized set of actions to protect organizations from known cyber attack vectors. While CIS Controls templates are not yet implemented, this section documents the planned structure for future implementation.

### CIS Controls v8 Categories

The 18 CIS Controls categories that would be covered:

1. **Inventory and Control of Enterprise Assets**
2. **Inventory and Control of Software Assets**
3. **Data Protection**
4. **Secure Configuration of Enterprise Assets and Software**
5. **Account Management**
6. **Access Control Management**
7. **Continuous Vulnerability Management**
8. **Audit Log Management**
9. **Email and Web Browser Protections**
10. **Malware Defenses**
11. **Data Recovery**
12. **Network Infrastructure Management**
13. **Network Monitoring and Defense**
14. **Security Awareness and Skills Training**
15. **Service Provider Management**
16. **Application Software Security**
17. **Incident Response Management**
18. **Penetration Testing**

### Implementation Groups (IG)

CIS Controls are organized into three Implementation Groups based on organization size and resources:

- **IG1**: Essential cyber hygiene (small organizations, limited resources)
- **IG2**: Enterprises with moderate cybersecurity resources
- **IG3**: Advanced organizations with significant security resources

### Planned Template Structure

```
Planned CIS Controls Templates (~20-25 files):
├── Foundation (0010-0030): Policy, Organization, Scope
├── Asset Management (0040-0060): Hardware and Software Inventory
├── Data Protection (0070-0090): Data Classification, Protection, Recovery
├── Configuration & Vulnerability (0100-0130): Hardening, Patching, Vulnerability Management
├── Access Control (0140-0170): Identity, Authentication, Access Management
├── Monitoring & Defense (0180-0210): Logging, Monitoring, Incident Response
├── Application Security (0220-0240): Secure Development, Testing
└── Governance (0250-0270): Training, Audits, Third-Party Management
```

### Mapping to Existing Templates

Many CIS Controls align with existing ISMS and BSI Grundschutz templates:

| CIS Control | Existing Template Alignment |
|---|---|
| CIS 1 (Asset Inventory) | ISMS 0300_Policy_Asset, BSI 0050_Strukturanalyse |
| CIS 3 (Data Protection) | ISMS 0280_Policy_Datenklassifizierung, BSI 0420_Policy_Datenschutz |
| CIS 5 (Account Management) | ISMS 0220_Policy_Zugriffssteuerung, BSI 0200_Policy_Zugriffssteuerung |
| CIS 7 (Vulnerability Management) | ISMS 0340_Policy_Vulnerability, BSI 0280_Policy_Patch |
| CIS 8 (Audit Logs) | ISMS 0320_Policy_Logging, BSI 0300_Policy_Logging |
| CIS 11 (Data Recovery) | ISMS 0420_Policy_Backup, BSI 0440_Policy_Backup |
| CIS 17 (Incident Response) | ISMS 0400_Policy_Incident, BSI 0320_Policy_Incident |

**Note:** CIS Controls templates are planned for future implementation. This section provides the design framework for when implementation begins.

## Cross-Framework Mapping

### Incident Management Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ITIL v4** | Incident Management Practice | 0120_Incident | Detect, log, categorize, prioritize, investigate, resolve |
| **ISO 20000** | Clause 8.3.1 | 0120_Incident | Restore service operation as quickly as possible |
| **COBIT 2019** | DSS02 | 0120_Incident | Record, classify, prioritize, investigate, diagnose, resolve |

### Change Management Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ITIL v4** | Change Enablement Practice | 0140_Change | Request, assess, authorize, implement, review |
| **ISO 20000** | Clause 8.4.1 | 0140_Change | Plan, assess, authorize, implement, review changes |
| **COBIT 2019** | BAI06 | 0140_Change | Evaluate, prioritize, authorize, manage emergency changes |

### Configuration Management Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ITIL v4** | Service Configuration Management | 0090_Konfiguration | Identify, control, record, report, verify CIs |
| **ISO 20000** | Clause 8.4.3 | 0090_Konfiguration | Plan, identify, control, maintain configuration information |
| **COBIT 2019** | BAI10 | 0090_Konfiguration | Establish model, maintain repository, control items |

### Availability Management Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ITIL v4** | Availability Management Practice | 0210_Verfuegbarkeit | Define requirements, monitor, analyze, improve |
| **ISO 20000** | Clause 8.5 | 0210_Verfuegbarkeit | Ensure services meet availability requirements |
| **COBIT 2019** | APO09 | 0210_Verfuegbarkeit | Define service agreements, monitor service levels |

### Business Continuity Management Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ISO 22301** | Clause 8.4 | BCM 0120_Krisenmanagementplan<br>BCM 0140_BCP<br>BCM 0150_DRP | Develop and implement BC procedures |
| **BSI 100-4** | Section 3.7 | BCM 0140_BCP<br>BCM 0150_DRP | Business continuity and IT recovery plans |
| **ISO 20000** | Clause 8.5 | IT-Ops 0160_Disaster_Recovery | Service continuity management |
| **COBIT 2019** | DSS04 | IT-Ops 0150_Backup<br>IT-Ops 0160_Disaster_Recovery | Managed continuity |

### Information Security Management Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ISO 27001** | Clause 8.1 | ISMS Policies 0200-0680<br>ISMS Guidelines 0210-0690 | Operational security controls |
| **BSI 200-1** | Section 7.2 | BSI Policies 0200-0530 | Security measure implementation |
| **ISO 20000** | Clause 8.8 | IT-Ops 0170_Sicherheit | Information security management |
| **COBIT 2019** | APO13, DSS05 | IT-Ops 0170_Sicherheit<br>IT-Ops 0180_Patch | Managed security |

### Risk Management Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ISO 22301** | Clause 6.1 | BCM 0090_Risikoanalyse | BC risk assessment |
| **ISO 27001** | Clause 6.1 | ISMS 0080_ISMS_Risikoregister<br>ISMS 0090_ISMS_Risikobehandlungsplan | Information security risk management |
| **BSI 200-3** | Complete Standard | BSI 0090_Risikoanalyse | Risk analysis per BSI methodology |
| **COBIT 2019** | APO12 | IT-Ops 0160_Disaster_Recovery | Managed risk |

### Audit and Compliance Process

| Framework | Reference | Template | Key Activities |
|---|---|---|---|
| **ISO 22301** | Clause 9.2 | BCM 0270_Compliance_Audit | BCM internal audits |
| **ISO 27001** | Clause 9.2 | ISMS 0130_ISMS_Internes_Auditprogramm | ISMS internal audits |
| **BSI 200-1** | Section 8.1 | BSI 0610_Internes_Auditprogramm | ISMS audits per BSI |
| **ISO 20000** | Clause 9.2 | IT-Ops 0280_Compliance | SMS internal audits |
| **COBIT 2019** | MEA02, MEA03 | IT-Ops 0280_Compliance | Internal control and compliance |

## Compliance Checklists

### ITIL v4 Compliance

- [ ] Service Strategy defined (0070_Betriebskonzept)
- [ ] Service Design documented (0040_System, 0050_Infrastruktur)
- [ ] Service Transition processes established (0140_Change, 0090_Konfiguration)
- [ ] Service Operation procedures defined (0120_Incident, 0110_Monitoring)
- [ ] Continual Service Improvement implemented (0130_Problem)
- [ ] All 34 ITIL practices considered and documented where applicable

### ISO 20000-1:2018 Compliance

- [ ] SMS scope defined (0010_Einleitung)
- [ ] Service management policy established (0070_Betriebskonzept)
- [ ] Roles and responsibilities assigned (0060_Rollen)
- [ ] Risk management implemented (0160_Disaster_Recovery, 0280_Compliance)
- [ ] All mandatory processes documented (Clauses 8.1-8.8)
- [ ] Monitoring and measurement established (0110_Monitoring)
- [ ] Internal audit process defined (0280_Compliance)
- [ ] Management review process defined (0280_Compliance)
- [ ] Continual improvement process established (0130_Problem)

### COBIT 2019 Compliance

- [ ] Governance objectives addressed (APO02, APO12, APO13, MEA01, MEA02, MEA03)
- [ ] Management objectives addressed (APO01, APO07, APO09, BAI03, BAI06, BAI10, DSS01-DSS06)
- [ ] Design factors considered in template customization
- [ ] Performance management established (0110_Monitoring, 0200_Kapazitaets)
- [ ] Risk management implemented (0160_Disaster_Recovery, 0280_Compliance)
- [ ] Compliance management established (0280_Compliance)

### ISO 22301:2019 Compliance (BCM)

- [ ] BCMS scope defined (0010_Zweck_und_Geltungsbereich)
- [ ] BCM policy established (0020_BCM_Leitlinie_Policy)
- [ ] BCM organization defined (0040_Notfallorganisation)
- [ ] Business Impact Analysis conducted (0070_BIA_Methodik, 0080_BIA_Ergebnisse)
- [ ] Risk assessment completed (0090_Risikoanalyse)
- [ ] BC strategies defined (0100_Strategie)
- [ ] BC plans developed (0120_Krisenmanagementplan, 0140_BCP, 0150_DRP)
- [ ] Testing program established (0220_Uebungs_und_Testprogramm)
- [ ] Training and awareness implemented (0260_Schulungen)
- [ ] Monitoring and review process defined (0250_Pflege_Review_und_KPIs)
- [ ] Internal audit process defined (0270_Compliance_Audit)
- [ ] Continual improvement implemented (0240_Nachbereitung_Postmortem)

### BSI BCM Standards Compliance

- [ ] BCM policy and organization (BSI 100-4 Sections 3.1, 3.2)
- [ ] BCM concept and BIA (BSI 100-4 Sections 3.3, 3.4)
- [ ] Continuity strategies (BSI 100-4 Section 3.5)
- [ ] Emergency and crisis management (BSI 100-4 Section 3.6)
- [ ] BC plans (BSI 100-4 Section 3.7)
- [ ] Tests and exercises (BSI 100-4 Section 3.8)
- [ ] Awareness and training (BSI 100-4 Section 3.9)
- [ ] Maintenance and improvement (BSI 100-4 Section 3.10)

### ISO 27001:2022 Compliance (ISMS)

- [ ] ISMS scope defined (0020_ISMS_Geltungsbereich)
- [ ] Information security policy established (0010_ISMS_Informationssicherheitsleitlinie)
- [ ] Organizational context documented (0030_ISMS_Kontext)
- [ ] ISMS governance established (0040_ISMS_Governance)
- [ ] Risk management process implemented (0060-0090_ISMS_Risikomanagement)
- [ ] Statement of Applicability completed (0100_ISMS_SoA)
- [ ] Security objectives defined (0110_ISMS_Sicherheitsziele)
- [ ] All applicable Annex A controls implemented (Policies 0200-0680, Guidelines 0210-0690)
- [ ] Training and awareness program (0120_ISMS_Schulung)
- [ ] Internal audit program (0130_ISMS_Internes_Auditprogramm)
- [ ] Management review process (0140_ISMS_Management_Review)
- [ ] Nonconformity management (0150_ISMS_Nichtkonformitaeten)
- [ ] Continual improvement (0160_ISMS_Kontinuierliche_Verbesserung)

### Amendment 1:2024 Compliance

- [ ] Updated control objectives reviewed
- [ ] Terminology updates applied
- [ ] Risk assessment guidance incorporated
- [ ] Cloud security controls enhanced

### BSI Standards 200-1/200-2/200-3 Compliance (BSI Grundschutz)

- [ ] Information security policy (BSI 200-1 Section 4.1)
- [ ] ISMS organization (BSI 200-1 Section 4.2)
- [ ] Scope and boundaries (BSI 200-1 Section 4.4)
- [ ] Structure analysis (BSI 200-1 Section 6.1, BSI 200-2)
- [ ] Protection needs assessment (BSI 200-1 Section 6.2, BSI 200-2)
- [ ] Modeling with BSI Bausteine (BSI 200-1 Section 6.3, BSI 200-2)
- [ ] IT-Grundschutz-Check (BSI 200-1 Section 6.4, BSI 200-2)
- [ ] Risk analysis per BSI 200-3 (BSI 200-1 Section 6.5, BSI 200-3)
- [ ] Security concept (BSI 200-1 Section 6.6)
- [ ] Implementation planning (BSI 200-1 Section 7.1)
- [ ] Security measures implemented (BSI 200-1 Section 7.2)
- [ ] Implementation monitoring (BSI 200-1 Section 7.3)
- [ ] Internal audits (BSI 200-1 Section 8.1)
- [ ] Management review (BSI 200-1 Section 8.2)
- [ ] Continuous improvement (BSI 200-1 Section 8.3)

### CIS Controls v8 Compliance (Planned)

- [ ] Asset inventory (CIS 1, 2)
- [ ] Data protection (CIS 3)
- [ ] Secure configuration (CIS 4)
- [ ] Account and access management (CIS 5, 6)
- [ ] Vulnerability management (CIS 7)
- [ ] Audit logs (CIS 8)
- [ ] Email and web protections (CIS 9)
- [ ] Malware defenses (CIS 10)
- [ ] Data recovery (CIS 11)
- [ ] Network management and monitoring (CIS 12, 13)
- [ ] Security awareness (CIS 14)
- [ ] Service provider management (CIS 15)
- [ ] Application security (CIS 16)
- [ ] Incident response (CIS 17)
- [ ] Penetration testing (CIS 18)

## Framework Version History

| Framework | Version | Release Date | Template Alignment Date |
|---|---|---|---|
| **IT-Operations** | | | |
| ITIL | v4 (2019) | February 2019 | January 2024 |
| ISO 20000-1 | 2018 | September 2018 | January 2024 |
| COBIT | 2019 | November 2018 | January 2024 |
| **BCM** | | | |
| ISO 22301 | 2019 | October 2019 | February 2025 |
| BSI 100-4 | 2009 (archived, replaced by BSI 200-4) | 2009 | February 2025 |
| **ISMS** | | | |
| ISO 27001 | 2022 | October 2022 | February 2025 |
| ISO 27001 Amendment 1 | 2024 | February 2024 | February 2025 |
| **BSI Grundschutz** | | | |
| BSI Standard 200-1 | 2023 (Edition 2023) | 2023 | February 2025 |
| BSI Standard 200-2 | 2023 (Edition 2023) | 2023 | February 2025 |
| BSI Standard 200-3 | 2023 (Edition 2023) | 2023 | February 2025 |
| BSI IT-Grundschutz Compendium | 2024 (Edition 2024) | 2024 | February 2025 |
| **CIS Controls** | | | |
| CIS Controls | v8.1 | May 2023 | Planned (Design only) |

## References

### ITIL v4
- AXELOS. (2019). *ITIL Foundation: ITIL 4 Edition*. TSO (The Stationery Office).
- AXELOS. (2019). *ITIL 4: Create, Deliver and Support*. TSO (The Stationery Office).
- AXELOS. (2019). *ITIL 4: Drive Stakeholder Value*. TSO (The Stationery Office).
- AXELOS. (2019). *ITIL 4: High-velocity IT*. TSO (The Stationery Office).
- AXELOS. (2020). *ITIL 4: Direct, Plan and Improve*. TSO (The Stationery Office).

### ISO 20000-1:2018
- ISO/IEC. (2018). *ISO/IEC 20000-1:2018 Information technology — Service management — Part 1: Service management system requirements*. International Organization for Standardization.
- ISO/IEC. (2019). *ISO/IEC 20000-2:2019 Information technology — Service management — Part 2: Guidance on the application of service management systems*. International Organization for Standardization.

### COBIT 2019
- ISACA. (2018). *COBIT 2019 Framework: Introduction and Methodology*. ISACA.
- ISACA. (2018). *COBIT 2019 Framework: Governance and Management Objectives*. ISACA.
- ISACA. (2019). *COBIT 2019 Framework: Design Guide*. ISACA.

### ISO 22301:2019 (BCM)
- ISO. (2019). *ISO 22301:2019 Security and resilience — Business continuity management systems — Requirements*. International Organization for Standardization.
- ISO. (2021). *ISO/TS 22317:2021 Security and resilience — Business continuity management systems — Guidelines for business impact analysis*. International Organization for Standardization.
- ISO. (2021). *ISO/TS 22318:2021 Security and resilience — Business continuity management systems — Guidelines for supply chain continuity*. International Organization for Standardization.

### BSI BCM Standards
- BSI. (2009). *BSI-Standard 100-4: Business Continuity Management*. Bundesamt für Sicherheit in der Informationstechnik. (Note: Archived, replaced by BSI Standard 200-4)
- BSI. (2021). *BSI-Standard 200-4: Business Continuity Management*. Bundesamt für Sicherheit in der Informationstechnik.

### ISO 27001:2022 (ISMS)
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. International Organization for Standardization.
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. International Organization for Standardization.
- ISO/IEC. (2024). *ISO/IEC 27001:2022/Amd 1:2024 Amendment 1*. International Organization for Standardization.

### BSI IT-Grundschutz
- BSI. (2023). *BSI-Standard 200-1: Information Security Management Systems (ISMS)*. Bundesamt für Sicherheit in der Informationstechnik.
- BSI. (2023). *BSI-Standard 200-2: IT-Grundschutz Methodology*. Bundesamt für Sicherheit in der Informationstechnik.
- BSI. (2023). *BSI-Standard 200-3: Risk Analysis based on IT-Grundschutz*. Bundesamt für Sicherheit in der Informationstechnik.
- BSI. (2024). *IT-Grundschutz Compendium: Edition 2024*. Bundesamt für Sicherheit in der Informationstechnik.

### CIS Controls v8
- Center for Internet Security. (2023). *CIS Controls v8.1*. Center for Internet Security, Inc.
- Center for Internet Security. (2023). *CIS Controls v8.1 Implementation Guide*. Center for Internet Security, Inc.

## Maintenance and Updates

This framework mapping document is maintained by the IT Operations Team and is reviewed:
- Annually for framework updates
- When new framework versions are released
- When templates are significantly updated
- Upon request from stakeholders

**Last Review Date:** 2025-02-03  
**Next Review Date:** 2026-02-03  
**Document Owner:** IT Operations Manager  
**Approved by:** CIO

---

For questions or suggestions regarding framework mappings, please contact the IT Operations Team.
