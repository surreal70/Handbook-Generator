# Scope and Information Domain (Boundaries)

**Document-ID:** BSI-GRUNDSCHUTZ-0040
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



## 1. Purpose and Objectives

This document defines the scope of the Information Security Management System (ISMS) of **AdminSend GmbH** and delineates the information domain. The clear definition of scope is the foundation for all further IT-Grundschutz activities (structure analysis, protection needs assessment, modeling).

## 2. Scope Definition

### 2.1 Organizational Units and Locations

**Organization:** AdminSend GmbH

**Locations in Scope:**

| Location | Address | Type | Employees | In Scope |
|---|---|---|---|---|
| [TODO] | [TODO] | Main location | [TODO] | ✓ |
| [TODO: Additional locations] | [TODO] | [TODO] | [TODO] | ✓/✗ |

**Organizational Units in Scope:**
- Executive Management
- IT Department
- [TODO: Additional departments]

### 2.2 Business Processes and Services

**Critical Business Processes in Scope:**

| Process | Description | Criticality | Owner | In Scope |
|---|---|---|---|---|
| [TODO: Process 1] | [TODO] | High/Medium/Low | [TODO] | ✓ |
| [TODO: Process 2] | [TODO] | High/Medium/Low | [TODO] | ✓ |

**IT Services in Scope:**

| Service | Description | Users | Service Owner | In Scope |
|---|---|---|---|---|
| [TODO: Service 1] | [TODO] | [TODO] | [TODO] | ✓ |
| [TODO: Service 2] | [TODO] | [TODO] | [TODO] | ✓ |

### 2.3 IT Infrastructure

**IT Systems in Scope:**

#### 2.3.1 On-Premise IT

| Category | Systems | Quantity | In Scope |
|---|---|---|---|
| Servers | [[ netbox.device.servers ]] | [TODO] | ✓ |
| Network | [[ netbox.device.network ]] | [TODO] | ✓ |
| Storage | [[ netbox.device.storage ]] | [TODO] | ✓ |
| Clients | Workstations, Laptops | [TODO] | ✓ |
| Mobile Devices | Smartphones, Tablets | [TODO] | ✓ |

#### 2.3.2 Cloud Services

| Cloud Service | Provider | Type (IaaS/PaaS/SaaS) | In Scope |
|---|---|---|---|
| [TODO: Cloud Service 1] | [TODO] | [TODO] | ✓ |
| [TODO: Cloud Service 2] | [TODO] | [TODO] | ✓ |

#### 2.3.3 OT/IoT (if applicable)

| OT/IoT System | Description | Location | In Scope |
|---|---|---|---|
| [TODO: OT System 1] | [TODO] | [TODO] | ✓/✗ |

### 2.4 Applications and Data

**Business Applications in Scope:**

| Application | Type | Criticality | Data Classification | In Scope |
|---|---|---|---|---|
| [TODO: Application 1] | [TODO] | High/Medium/Low | Confidential/Internal | ✓ |
| [TODO: Application 2] | [TODO] | High/Medium/Low | Confidential/Internal | ✓ |

**Data Types in Scope:**
- Personal data (GDPR-relevant)
- Trade secrets
- Customer data
- Financial data
- [TODO: Additional data types]

## 3. Information Domain Boundaries

### 3.1 In Scope

**The following elements are in scope of the ISMS:**

1. **Infrastructure:**
   - All servers and network components at location [TODO]
   - [TODO: Additional infrastructure]

2. **Applications:**
   - All business-critical applications
   - [TODO: Specific applications]

3. **Data:**
   - All personal data
   - All business data classified as "Confidential" or higher
   - [TODO: Additional data]

4. **People:**
   - All employees of AdminSend GmbH
   - External service providers with access to scope systems
   - [TODO: Additional groups]

5. **Processes:**
   - All IT operations processes
   - All business-critical processes
   - [TODO: Additional processes]

### 3.2 Out of Scope

**The following elements are NOT in scope of the ISMS:**

| Element | Justification | Risk Assessment | Interfaces to Scope |
|---|---|---|---|
| [TODO: Out-of-Scope Element 1] | [TODO: Justification] | [TODO: Risk] | [TODO: Interfaces] |
| [TODO: Out-of-Scope Element 2] | [TODO: Justification] | [TODO: Risk] | [TODO: Interfaces] |

**Important:** Even out-of-scope elements must be assessed for their risks to the scope, especially when interfaces exist.

### 3.3 Justification of Boundaries

[TODO: Explain the reasons for the chosen scope boundaries]

Examples of justifications:
- Focus on critical business processes
- Resource constraints (phased expansion planned)
- External responsibility (e.g. outsourced processes)
- Low criticality

## 4. Interfaces and Dependencies

### 4.1 External Service Providers

| Service Provider | Service | Criticality | Contractual Arrangements | Security Requirements |
|---|---|---|---|---|
| [TODO: Provider 1] | [TODO] | High/Medium/Low | [TODO: Contract available] | [TODO: SLA, Certifications] |
| [TODO: Provider 2] | [TODO] | High/Medium/Low | [TODO: Contract available] | [TODO: SLA, Certifications] |

### 4.2 Critical Interfaces

**Interfaces between Scope and Out-of-Scope:**

| Interface | From (Scope) | To (Out-of-Scope) | Data Flow | Security Measures |
|---|---|---|---|---|
| [TODO: Interface 1] | [TODO] | [TODO] | [TODO] | [TODO: Encryption, Firewall, etc.] |
| [TODO: Interface 2] | [TODO] | [TODO] | [TODO] | [TODO] |

**Interfaces to External Partners:**

| Partner | Purpose | Data Types | Security Measures |
|---|---|---|---|
| [TODO: Partner 1] | [TODO] | [TODO] | [TODO] |
| [TODO: Partner 2] | [TODO] | [TODO] | [TODO] |

### 4.3 Dependencies

**Critical Dependencies of the Scope:**

| Dependency | Type | Impact of Failure | Mitigation Measures |
|---|---|---|---|
| Internet Connection | External Infrastructure | [TODO] | [TODO: Redundancy, Backup line] |
| Power Supply | External Infrastructure | [TODO] | [TODO: UPS, Emergency power] |
| [TODO: Additional dependencies] | [TODO] | [TODO] | [TODO] |

## 5. Information Domain Diagram



![Information Domain Diagram](diagrams/informationsverbund.png)

**Diagram Legend:**
- **Green Line:** Scope boundary (in ISMS)
- **Red Line:** Out-of-scope boundary
- **Blue Arrows:** Data flows
- **Yellow Symbols:** Critical interfaces

[TODO: Create an information domain diagram]

## 6. Scope Changes

### 6.1 Change Process

Scope changes require:
1. **Request:** Formal change request to ISO
2. **Assessment:** Assessment of impacts (risks, resources, compliance)
3. **Approval:** Approval by executive management
4. **Implementation:** Update of all affected documents
5. **Communication:** Information to all stakeholders

**Responsible:** [TODO] (ISO)

### 6.2 Scope Review

The scope is regularly reviewed:
- **Frequency:** Annually or upon significant changes
- **Triggers:** New business processes, IT systems, locations, regulatory requirements
- **Responsible:** ISO

**Next Review:** [TODO]

## 7. Documentation and Evidence

The following documents and evidence are maintained for the scope:
- This scope document
- Information domain diagram
- Asset inventory (see Appendix 0710)
- Data flow diagrams (see Appendix 0720)
- Contracts with external service providers
- Scope change logs

## 8. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| Executive Management | [TODO] | [TODO] | Draft |
| ISO | [TODO] | [TODO] | Draft |

**References:**
- BSI Standard 200-1: Management Systems for Information Security (ISMS)
- BSI Standard 200-2: IT-Grundschutz Methodology (Chapter 4: Scope Definition)
- BSI IT-Grundschutz Compendium

