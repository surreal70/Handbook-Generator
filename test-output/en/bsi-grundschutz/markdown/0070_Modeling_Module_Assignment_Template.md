# Modeling: Module Assignment (Template)

**Document-ID:** BSI-GRUNDSCHUTZ-0070
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

The modeling assigns appropriate IT-Grundschutz modules to the objects of the information domain of **AdminSend GmbH**. It forms the basis for:
- Basic security check (Document 0080)
- Identification of requirements to be implemented
- Systematic security measure planning

**Responsible:** [TODO] (ISB)

**Important:** This document only references modules. The complete module texts are located in the BSI IT-Grundschutz Compendium and are not copied.

## 2. IT-Grundschutz Modules: Overview

### 2.1 Module Structure

The BSI IT-Grundschutz Compendium organizes modules into the following layers:

| Layer | Abbreviation | Description | Examples |
|---|---|---|---|
| **ISMS** | ISMS | Security Management | ISMS.1 Security Management |
| **Organization and Personnel** | ORP | Organizational Processes | ORP.1 Organization, ORP.3 Awareness and Training |
| **Conception and Approaches** | CON | Concepts and Methods | CON.1 Crypto Concept, CON.3 Data Backup Concept |
| **Operations** | OPS | IT Operations Processes | OPS.1.1.2 Proper IT Administration |
| **Detection and Response** | DER | Incident Management | DER.1 Detection of Security-Relevant Events |
| **Systems** | SYS | IT Systems | SYS.1.1 General Server, SYS.2.1 General Client |
| **Applications** | APP | Application Software | APP.1.1 Office Products, APP.3.1 Web Applications |
| **IT Systems** | NET | Networks and Communication | NET.1.1 Network Architecture and Design, NET.3.1 Routers and Switches |
| **Industrial IT** | IND | OT/ICS Systems | IND.1 Operational and Control Technology |

### 2.2 Assignment Logic

**Principles:**
1. **Completeness:** All relevant objects receive module assignments
2. **Appropriateness:** Modules match the object type and protection need
3. **No Redundancy:** Each module is assigned only once per object
4. **Granularity:** Assignment at a meaningful abstraction level

**Approach:**
1. Adopt objects from structure analysis (Document 0050)
2. Identify suitable modules from IT-Grundschutz Compendium
3. Document assignment
4. Validation by IT management and ISB

## 3. Module Assignment

### 3.1 ISMS and Organization (ISMS, ORP)



| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| ORG-001 | AdminSend GmbH | Organization | ISMS.1 Security Management | Overall organization | [TODO] |
| ORG-001 | AdminSend GmbH | Organization | ORP.1 Organization | Organizational structure | [TODO] |
| ORG-001 | AdminSend GmbH | Organization | ORP.2 Personnel | Personnel management | [TODO: HR] |
| ORG-001 | AdminSend GmbH | Organization | ORP.3 Awareness and Training | Awareness program | [TODO] |
| ORG-001 | AdminSend GmbH | Organization | ORP.4 Identity and Access Management | IAM processes | [TODO] |
| ORG-001 | AdminSend GmbH | Organization | ORP.5 Compliance Management (Requirements Management) | Compliance | [TODO] |

### 3.2 Conception and Approaches (CON)

| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| CON-001 | Crypto Concept | Concept | CON.1 Crypto Concept | Encryption strategy | [TODO] |
| CON-002 | Data Backup Concept | Concept | CON.3 Data Backup Concept | Backup strategy | [TODO] |
| CON-003 | Deletion Concept | Concept | CON.6 Deletion and Destruction | Data deletion | [TODO] |
| CON-004 | Patch and Change Management | Concept | CON.7 Information Security on Business Trips | [TODO: if applicable] | [TODO] |
| CON-005 | Software Development | Concept | CON.8 Software Development | [TODO: if applicable] | [TODO] |

### 3.3 Operations (OPS)

| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| OPS-001 | IT Operations | Operations Process | OPS.1.1.2 Proper IT Administration | IT administration | [TODO] |
| OPS-002 | Patch Management | Operations Process | OPS.1.1.3 Patch and Change Management | Patch process | [TODO] |
| OPS-003 | Protection Against Malware | Operations Process | OPS.1.1.4 Protection Against Malware | Malware protection | [TODO] |
| OPS-004 | Data Backup | Operations Process | OPS.1.1.5 Logging | Logging | [TODO] |
| OPS-005 | Software Tests | Operations Process | OPS.1.1.6 Software Tests and Releases | [TODO: if applicable] | [TODO] |
| OPS-006 | Outsourcing | Operations Process | OPS.2.1 Outsourcing for Customers | [TODO: if applicable] | [TODO] |
| OPS-007 | Cloud Usage | Operations Process | OPS.2.2 Cloud Usage | Cloud services | [TODO] |

### 3.4 Detection and Response (DER)

| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| DER-001 | Detection | Process | DER.1 Detection of Security-Relevant Events | SIEM, Monitoring | [TODO] |
| DER-002 | Incident Management | Process | DER.2.1 Handling of Security Incidents | Incident response | [TODO] |
| DER-003 | Forensics | Process | DER.2.2 Preparation for IT Forensics | [TODO: if applicable] | [TODO] |
| DER-004 | Audits | Process | DER.3.1 Audits and Reviews | Internal audit | [TODO] |

### 3.5 Applications (APP)



| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| A-001 | [TODO: Application 1] | Application | APP.1.1 Office Products | [TODO: if office application] | [TODO] |
| A-002 | [TODO: Application 2] | Application | APP.3.1 Web Applications | [TODO: if web application] | [TODO] |
| A-003 | [TODO: Application 3] | Application | APP.3.2 Web Server | [TODO: if web server] | [TODO] |
| A-004 | [TODO: Application 4] | Application | APP.3.3 File Server | [TODO: if file server] | [TODO] |
| A-005 | [TODO: Application 5] | Application | APP.3.6 DNS Server | [TODO: if DNS] | [TODO] |
| A-006 | [TODO: Application 6] | Application | APP.4.3 Relational Database Systems | [TODO: if database] | [TODO] |
| A-007 | [TODO: Application 7] | Application | APP.5.1 General Groupware | [TODO: if groupware] | [TODO] |
| A-008 | [TODO: Application 8] | Application | APP.5.2 Microsoft Exchange and Outlook | [TODO: if Exchange] | [TODO] |

### 3.6 IT Systems (SYS)



| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| S-001 | [[ netbox.device.server_001 ]] | Server | SYS.1.1 General Server | General server | [TODO] |
| S-002 | [TODO: Linux Server] | Server | SYS.1.3 Server under Linux and Unix | Linux server | [TODO] |
| S-003 | [TODO: Windows Server] | Server | SYS.1.2.3 Windows Server | Windows server | [TODO] |
| S-004 | [TODO: Virtualization] | Virtualization | SYS.1.5 Virtualization | VMware/Hyper-V | [TODO] |
| S-005 | [TODO: Container] | Container | SYS.1.6 Containerization | Docker/Kubernetes | [TODO] |
| S-006 | [TODO: Storage] | Storage | SYS.1.8 Storage Solutions | SAN/NAS | [TODO] |
| S-007 | [TODO: Client] | Client | SYS.2.1 General Client | Workstations | [TODO] |
| S-008 | [TODO: Windows Client] | Client | SYS.2.2.3 Clients under Windows | Windows clients | [TODO] |
| S-009 | [TODO: macOS Client] | Client | SYS.2.4 Clients under macOS | macOS clients | [TODO] |
| S-010 | [TODO: Mobile Device] | Mobile | SYS.3.2.1 General Smartphones and Tablets | Mobile devices | [TODO] |
| S-011 | [TODO: IoT] | IoT | SYS.4.4 General IoT Device | [TODO: if IoT] | [TODO] |

### 3.7 Networks and Communication (NET)



| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| N-001 | Network Architecture | Network | NET.1.1 Network Architecture and Design | Overall network | [TODO] |
| N-002 | Network Management | Network | NET.1.2 Network Management | Network monitoring | [TODO] |
| N-003 | [TODO: Routers/Switches] | Network Component | NET.3.1 Routers and Switches | Network devices | [TODO] |
| N-004 | [TODO: Firewall] | Security Component | NET.3.2 Firewall | Perimeter protection | [TODO] |
| N-005 | [TODO: VPN] | Security Component | NET.3.3 VPN | Remote access | [TODO] |
| N-006 | [TODO: WLAN] | Network | NET.2.1 WLAN Operations | Wireless network | [TODO] |
| N-007 | [TODO: Email] | Communication | NET.4.1 TLS Encryption | [TODO: if applicable] | [TODO] |

### 3.8 Industrial IT (IND) - Optional



| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| IND-001 | [TODO: OT System] | OT/ICS | IND.1 Operational and Control Technology | [TODO: if OT in scope] | [TODO] |
| IND-002 | [TODO: ICS Component] | OT/ICS | IND.2.1 General ICS Component | [TODO: if ICS in scope] | [TODO] |

### 3.9 Rooms and Infrastructure (INF)

| Object ID | Object | Object Class | Assigned Modules | Justification | Owner |
|---|---|---|---|---|---|
| R-001 | Data Center | Room | INF.2 Data Center and Server Room | Critical server room | [TODO: Facility] |
| R-002 | [TODO] | Building | INF.1 General Building | Main location | [TODO: Facility] |
| R-003 | [TODO: Office Room] | Room | INF.8 Home Office | [TODO: if home office] | [TODO] |

## 4. Summary and Statistics

### 4.1 Assignment Statistics

| Module Layer | Number of Assigned Modules | Number of Affected Objects |
|---|---|---|
| ISMS | [TODO] | [TODO] |
| ORP (Organization and Personnel) | [TODO] | [TODO] |
| CON (Conception) | [TODO] | [TODO] |
| OPS (Operations) | [TODO] | [TODO] |
| DER (Detection and Response) | [TODO] | [TODO] |
| APP (Applications) | [TODO] | [TODO] |
| SYS (Systems) | [TODO] | [TODO] |
| NET (Networks) | [TODO] | [TODO] |
| IND (Industrial IT) | [TODO] | [TODO] |
| INF (Infrastructure) | [TODO] | [TODO] |
| **Total** | **[TODO]** | **[TODO]** |

### 4.2 Completeness Check

| Object Type | Number of Objects | Number with Module Assignment | Completeness |
|---|---|---|---|
| Processes | [TODO] | [TODO] | [TODO: %] |
| Applications | [TODO] | [TODO] | [TODO: %] |
| IT Systems | [TODO] | [TODO] | [TODO: %] |
| Networks | [TODO] | [TODO] | [TODO: %] |
| Rooms | [TODO] | [TODO] | [TODO: %] |

### 4.3 Open Items

| ID | Object | Issue | Responsible | Deadline |
|---|---|---|---|---|
| [TODO] | [TODO] | [TODO: No suitable module found] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO: Unclear assignment] | [TODO] | [TODO] |

## 5. Validation and Quality Assurance

### 5.1 Validation Process

The module assignment is validated by:
1. **Review by IT Management:** [TODO] - Technical correctness
2. **Review by Information Domain Responsible:** Completeness
3. **Comparison with IT-Grundschutz Compendium:** Currency of modules
4. **Approval by ISB:** [TODO]

### 5.2 Quality Criteria

| Criterion | Status | Comments |
|---|---|---|
| All objects have module assignments | [TODO: ✓/✗] | [TODO] |
| Modules are current (IT-Grundschutz Compendium Edition [TODO]) | [TODO: ✓/✗] | [TODO] |
| Assignments are comprehensibly justified | [TODO: ✓/✗] | [TODO] |
| No redundancies | [TODO: ✓/✗] | [TODO] |
| Owners are named | [TODO: ✓/✗] | [TODO] |

## 6. Next Steps

After completing the modeling, the following steps follow:
1. **Basic Security Check (Document 0080):** Target-actual comparison for all assigned modules
2. **Risk Analysis (Document 0090):** For objects with increased protection needs or non-modelable risks
3. **Measure Planning (Document 0100):** Implementation planning of identified requirements

## 7. Update and Maintenance

The module assignment is updated when:
- New IT systems or applications are introduced
- Changes in IT architecture occur
- New edition of IT-Grundschutz Compendium is released
- At least annually as part of the ISMS review

**Responsible:** [TODO] (ISB)  
**Next Review:** [TODO]

## 8. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| ISB | [TODO] | [TODO] | Draft |
| IT Management | [TODO] | [TODO] | Draft |

**References:**
- BSI Standard 200-2: IT-Grundschutz Methodology (Chapter 7: Modeling)
- BSI IT-Grundschutz Compendium (current edition)
- BSI IT-Grundschutz Compendium: https://www.bsi.bund.de/grundschutz-kompendium

