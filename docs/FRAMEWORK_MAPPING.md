# IT Framework Mapping Documentation

## Overview

This document provides detailed mappings between the IT-Operations templates and established IT frameworks: ITIL v4, ISO 20000-1:2018, and COBIT 2019. These mappings ensure that the templates align with industry best practices and compliance requirements.

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

## Compliance Checklist

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

## Framework Version History

| Framework | Version | Release Date | Template Alignment Date |
|---|---|---|---|
| ITIL | v4 (2019) | February 2019 | January 2024 |
| ISO 20000-1 | 2018 | September 2018 | January 2024 |
| COBIT | 2019 | November 2018 | January 2024 |

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

## Maintenance and Updates

This framework mapping document is maintained by the IT Operations Team and is reviewed:
- Annually for framework updates
- When new framework versions are released
- When templates are significantly updated
- Upon request from stakeholders

**Last Review Date:** 2024-01-31  
**Next Review Date:** 2025-01-31  
**Document Owner:** IT Operations Manager  
**Approved by:** CIO

---

For questions or suggestions regarding framework mappings, please contact the IT Operations Team.
