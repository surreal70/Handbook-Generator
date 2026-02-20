# Structure Analysis (Template)

**Document-ID:** [FRAMEWORK]-0050
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

---



## 1. Objective and Purpose

The structure analysis systematically captures the structure of the information domain of **AdminSend GmbH**. It forms the basis for:
- Protection needs assessment (Document 0060)
- Modeling and module assignment (Document 0070)
- Basic security check (Document 0080)
- Risk analysis (Document 0090)

**Responsible:** [TODO] (ISO)

## 2. Approach and Methodology

### 2.1 Data Sources

The following data sources are used for the structure analysis:

| Data Source | Type | Responsible | Currency |
|---|---|---|---|
| CMDB/Asset Inventory | System | [TODO] | [TODO] |
| Network Documentation | Document | [TODO] | [TODO] |
| Architecture Diagrams | Document | [TODO] | [TODO] |
| Service Provider Contracts | Document | [TODO] | [TODO] |
| Stakeholder Interviews | Primary Source | [TODO] | [TODO] |

### 2.2 Granularity

The structure analysis is performed at the following granularity levels:

- **Business Processes:** Process level (not activity level)
- **Applications:** Application system level (not module level)
- **IT Systems:** Logical systems (servers, databases, storage)
- **Networks:** Network segments and zones
- **Rooms:** Locations and critical rooms (data center, server room)

### 2.3 Execution

**Timeline:**
- **Start:** [TODO]
- **Data Collection:** [TODO: e.g. 2 weeks]
- **Validation:** [TODO: e.g. 1 week]
- **Completion:** [TODO]

**Participants:**
- ISO: [TODO]
- IT Management: [TODO]
- Information Domain Managers: [TODO]
- Departments: [TODO]

## 3. Structure Register

### 3.1 Business Processes and Services



| ID | Process/Service | Owner | Description | Criticality | Dependencies | Applications |
|---|---|---|---|---|---|---|
| P-001 | [TODO: Process 1] | [TODO] | [TODO] | High/Medium/Low | [TODO] | [TODO: A-001, A-002] |
| P-002 | [TODO: Process 2] | [TODO] | [TODO] | High/Medium/Low | [TODO] | [TODO] |
| P-003 | [TODO: Process 3] | [TODO] | [TODO] | High/Medium/Low | [TODO] | [TODO] |

**Total Number of Processes:** [TODO]

### 3.2 Applications



| ID | Application | Owner | Purpose | User Group | Interfaces | Hosting | Criticality |
|---|---|---|---|---|---|---|---|
| A-001 | [TODO: App 1] | [TODO] | [TODO] | [TODO] | [TODO] | On-Prem/Cloud/SaaS | High/Medium/Low |
| A-002 | [TODO: App 2] | [TODO] | [TODO] | [TODO] | [TODO] | On-Prem/Cloud/SaaS | High/Medium/Low |
| A-003 | [TODO: App 3] | [TODO] | [TODO] | [TODO] | [TODO] | On-Prem/Cloud/SaaS | High/Medium/Low |

**Total Number of Applications:** [TODO]

**Hosting Distribution:**
- On-Premise: [TODO]
- Cloud (IaaS/PaaS): [TODO]
- SaaS: [TODO]

### 3.3 IT Systems and Components



| ID | System/Component | Type | Owner | Location/Region | Operation | IP Address | Notes |
|---|---|---|---|---|---|---|---|
| S-001 | [[ netbox.device.server_001 ]] | Server | [TODO] | [TODO] | Internal | [[ netbox.ip.server_001 ]] | [TODO] |
| S-002 | [TODO: System 2] | Database | [TODO] | [TODO] | Internal/External | [TODO] | [TODO] |
| S-003 | [TODO: System 3] | Storage | [TODO] | [TODO] | Internal/External | [TODO] | [TODO] |
| S-004 | [TODO: System 4] | Firewall | [TODO] | [TODO] | Internal | [TODO] | [TODO] |

**Total Number of IT Systems:** [TODO]

**System Types:**
- Servers: [TODO]
- Databases: [TODO]
- Storage: [TODO]
- Network Components: [TODO]
- Security Components: [TODO]
- Clients: [TODO]

### 3.4 Networks and Communication



| ID | Network/Zone | Purpose | Segmentation | Internet Access | VLAN ID | Operator | Security Zone |
|---|---|---|---|---|---|---|---|
| N-001 | Management Network | Administration | Yes | No | [[ netbox.vlan.management ]] | [TODO] | High Security |
| N-002 | Production Network | Business Applications | Yes | Yes (filtered) | [TODO] | [TODO] | Secure |
| N-003 | DMZ | External Services | Yes | Yes | [TODO] | [TODO] | Medium |
| N-004 | Guest WLAN | Guests | Yes | Yes (isolated) | [TODO] | [TODO] | Low |

**Total Number of Network Segments:** [TODO]

**Security Zones:**
- High Security (Management, critical systems): [TODO]
- Secure (Production systems): [TODO]
- Medium (DMZ, external interfaces): [TODO]
- Low (Guest network): [TODO]

### 3.5 Rooms and Locations



| ID | Location/Room | Type | Protection Measures | Access | Operator | Criticality |
|---|---|---|---|---|---|---|
| R-001 | [TODO] | Main Location | [TODO] | Access Control | AdminSend GmbH | High |
| R-002 | Data Center | Server Room | Climate Control, Fire Protection, Access Control | Authorized | AdminSend GmbH | High |
| R-003 | [TODO: Room 3] | [TODO] | [TODO] | [TODO] | [TODO] | Medium/Low |

**Total Number of Locations:** [TODO]  
**Total Number of Critical Rooms:** [TODO]

### 3.6 External Service Providers and Cloud Providers



| ID | Service Provider | Service | Criticality | Contract | Certifications | Location | Notes |
|---|---|---|---|---|---|---|---|
| D-001 | [TODO: Provider 1] | [TODO: Service] | High/Medium/Low | [TODO: Contract No.] | [TODO: ISO 27001, etc.] | [TODO] | [TODO] |
| D-002 | [TODO: Provider 2] | [TODO: Service] | High/Medium/Low | [TODO] | [TODO] | [TODO] | [TODO] |

**Total Number of Service Providers:** [TODO]

### 3.7 Personnel and Roles



| Role | Name | Area of Responsibility | Contact | Deputy |
|---|---|---|---|---|
| Executive Management | [TODO] | Overall Responsibility | {{ meta-organisation-roles.role_CEO_email }} | [TODO] |
| ISO | [TODO] | ISMS Coordination | {{ meta-organisation-roles.role_CISO_email }} | [TODO] |
| IT Management | [TODO] | IT Operations | {{ meta-organisation-roles.role_CIO_email }} | [TODO] |
| [TODO: Additional Roles] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Dependencies and Interfaces

### 4.1 Internal Dependencies

| From (Source) | To (Target) | Type | Criticality | Notes |
|---|---|---|---|---|
| [TODO: System A] | [TODO: System B] | Data Flow | High/Medium/Low | [TODO] |
| [TODO: Application X] | [TODO: Database Y] | Data Access | High/Medium/Low | [TODO] |

### 4.2 External Interfaces

| Interface | Partner/Provider | Direction | Data Types | Protocol | Security Measures |
|---|---|---|---|---|---|
| [TODO: Interface 1] | [TODO] | Inbound/Outbound/Bidirectional | [TODO] | [TODO] | [TODO: VPN, TLS, etc.] |
| [TODO: Interface 2] | [TODO] | Inbound/Outbound/Bidirectional | [TODO] | [TODO] | [TODO] |

## 5. Diagrams and Visualizations



### 5.1 Network Diagram

![Network Diagram](diagrams/netzwerk.png)

[TODO: Create a network diagram with all segments and zones]

### 5.2 Application Architecture

![Application Architecture](diagrams/anwendungsarchitektur.png)

[TODO: Create a diagram of the application landscape]

### 5.3 Data Flow Diagram

![Data Flow Diagram](diagrams/datenfluss.png)

[TODO: Create a data flow diagram for critical processes]

## 6. Validation and Quality Assurance

### 6.1 Validation Process

The structure analysis is validated by:
1. **Review by IT Management:** [TODO]
2. **Review by Information Domain Managers:** [TODO]
3. **Comparison with CMDB/Inventory:** [TODO: Date]
4. **Approval by ISO:** [TODO]

### 6.2 Completeness Check

| Category | Number Captured | Completeness | Notes |
|---|---|---|---|
| Business Processes | [TODO] | [TODO: %] | [TODO] |
| Applications | [TODO] | [TODO: %] | [TODO] |
| IT Systems | [TODO] | [TODO: %] | [TODO] |
| Networks | [TODO] | [TODO: %] | [TODO] |
| Rooms | [TODO] | [TODO: %] | [TODO] |
| Service Providers | [TODO] | [TODO: %] | [TODO] |

## 7. Update and Maintenance

The structure analysis is updated when:
- New IT systems or applications
- Changes in network architecture
- New service providers or cloud services
- Organizational changes
- At least annually as part of ISMS review

**Responsible:** [TODO] (ISO)  
**Next Review:** [TODO]

## 8. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| ISO | [TODO] | [TODO] | Draft |
| IT Management | [TODO] | [TODO] | Draft |

**References:**
- BSI Standard 200-2: IT-Grundschutz Methodology (Chapter 5: Structure Analysis)
- BSI IT-Grundschutz Compendium

