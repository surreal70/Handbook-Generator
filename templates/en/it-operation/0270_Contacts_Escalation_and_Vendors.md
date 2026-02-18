# Contacts, Escalation, and Vendors

**Document-ID:** [FRAMEWORK]-0270
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Overview

This document contains contact lists, escalation paths, vendors and suppliers, as well as support contacts for the IT service. The goal is to ensure quick access to relevant contact information in all situations.

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organization:** {{ meta-organisation.name }}

## Internal Contacts

### Management

#### Chief Executive Officer (CEO)
- **Name:** {{ meta-organisation-roles.role_ceo.name }}
- **Title:** {{ meta-organisation-roles.role_ceo.title }}
- **Email:** {{ meta-organisation-roles.role_ceo.email }}
- **Phone:** {{ meta-organisation-roles.role_ceo.phone }}
- **Department:** {{ meta-organisation-roles.role_ceo.department }}
- **Availability:** Mon-Fri 09:00-18:00
- **Escalation:** Only for critical business impact situations

#### Chief Information Officer (CIO)
- **Name:** {{ meta-organisation-roles.role_cio.name }}
- **Title:** {{ meta-organisation-roles.role_cio.title }}
- **Email:** {{ meta-organisation-roles.role_cio.email }}
- **Phone:** {{ meta-organisation-roles.role_cio.phone }}
- **Department:** {{ meta-organisation-roles.role_cio.department }}
- **Availability:** Mon-Fri 08:00-18:00
- **Escalation:** IT strategic decisions, critical incidents

#### Chief Information Security Officer (CISO)
- **Name:** {{ meta-organisation-roles.role_ciso.name }}
- **Title:** {{ meta-organisation-roles.role_ciso.title }}
- **Email:** {{ meta-organisation-roles.role_ciso.email }}
- **Phone:** {{ meta-organisation-roles.role_ciso.phone }}
- **Department:** {{ meta-organisation-roles.role_ciso.department }}
- **Availability:** Mon-Fri 08:00-18:00, 24/7 for security incidents
- **Escalation:** Security incidents, compliance questions

#### Chief Financial Officer (CFO)
- **Name:** {{ meta-organisation-roles.role_cfo.name }}
- **Title:** {{ meta-organisation-roles.role_cfo.title }}
- **Email:** {{ meta-organisation-roles.role_cfo.email }}
- **Phone:** {{ meta-organisation-roles.role_cfo.phone }}
- **Department:** {{ meta-organisation-roles.role_cfo.department }}
- **Availability:** Mon-Fri 09:00-17:00
- **Escalation:** Budget questions, financial approvals

#### Chief Operating Officer (COO)
- **Name:** {{ meta-organisation-roles.role_coo.name }}
- **Title:** {{ meta-organisation-roles.role_coo.title }}
- **Email:** {{ meta-organisation-roles.role_coo.email }}
- **Phone:** {{ meta-organisation-roles.role_coo.phone }}
- **Department:** {{ meta-organisation-roles.role_coo.department }}
- **Availability:** Mon-Fri 08:00-18:00
- **Escalation:** Operational impacts, process questions

### IT Operations

#### IT Operations Manager
- **Name:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Title:** {{ meta-organisation-roles.role_it_operations_manager.title }}
- **Email:** {{ meta-organisation-roles.role_it_operations_manager.email }}
- **Phone:** {{ meta-organisation-roles.role_it_operations_manager.phone }}
- **Department:** {{ meta-organisation-roles.role_it_operations_manager.department }}
- **Availability:** Mon-Fri 08:00-18:00, On-call for P1 incidents
- **Responsibility:** Overall responsibility for IT operations

#### Service Desk Lead
- **Name:** {{ meta-organisation-roles.role_service_desk_lead.name }}
- **Title:** {{ meta-organisation-roles.role_service_desk_lead.title }}
- **Email:** {{ meta-organisation-roles.role_service_desk_lead.email }}
- **Phone:** {{ meta-organisation-roles.role_service_desk_lead.phone }}
- **Department:** {{ meta-organisation-roles.role_service_desk_lead.department }}
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** First-level support, ticket management

#### Operations Team
- **Email:** [TODO: ops-team@example.com]
- **Phone:** [TODO: +49 89 12345678-250]
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** Daily operations, monitoring, incident response

### Specialized Teams

#### Network Team
- **Team Lead:** [TODO: Name]
- **Email:** [TODO: network-team@example.com]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** Network infrastructure, firewall, VPN

#### Security Team
- **Team Lead:** {{ meta-organisation-roles.role_ciso.name }}
- **Email:** [TODO: security-team@example.com]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 08:00-18:00, 24/7 for security incidents
- **Responsibility:** IT security, compliance, incident response

#### Database Team
- **Team Lead:** [TODO: Name]
- **Email:** [TODO: dba-team@example.com]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** Database administration, performance tuning

#### Application Team
- **Team Lead:** [TODO: Name]
- **Email:** [TODO: app-team@example.com]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** Application support, deployment

## On-Call and Standby

### On-Call Rotation

#### Primary On-Call
- **Current:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Mobile Number]
- **Availability:** 24/7
- **Rotation:** Weekly (Monday 08:00)

#### Secondary On-Call (Backup)
- **Current:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Mobile Number]
- **Availability:** 24/7
- **Rotation:** Weekly (Monday 08:00)

### On-Call Calendar
- **URL:** [TODO: Calendar URL]
- **Access:** All IT staff
- **Update:** Automatic through rotation tool

### On-Call Guidelines
- **Response Time P1:** 15 minutes
- **Response Time P2:** 1 hour
- **Availability:** Phone and email
- **Escalation:** After 30 minutes without response

## Escalation Paths

### Incident Escalation

#### Level 1: Service Desk
- **Contact:** {{ meta-organisation-roles.role_service_desk_lead.email }}
- **Phone:** {{ meta-organisation-roles.role_service_desk_lead.phone }}
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** First-level support, ticket creation

**Escalation to Level 2:**
- P1: Immediately
- P2: After 1 hour without solution
- P3: After 4 hours without solution
- P4: After 8 hours without solution

#### Level 2: Operations Team
- **Contact:** [TODO: ops-team@example.com]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 08:00-18:00, On-call 24/7
- **Responsibility:** Second-level support, technical analysis

**Escalation to Level 3:**
- P1: After 2 hours without solution
- P2: After 4 hours without solution
- P3: After 8 hours without solution

#### Level 3: IT Operations Manager
- **Contact:** {{ meta-organisation-roles.role_it_operations_manager.email }}
- **Phone:** {{ meta-organisation-roles.role_it_operations_manager.phone }}
- **Availability:** Mon-Fri 08:00-18:00, On-call for P1
- **Responsibility:** Coordination, resource allocation

**Escalation to Level 4:**
- P1: After 4 hours without solution
- P2: After 8 hours without solution
- When external support required

#### Level 4: CIO
- **Contact:** {{ meta-organisation-roles.role_cio.email }}
- **Phone:** {{ meta-organisation-roles.role_cio.phone }}
- **Availability:** Mon-Fri 08:00-18:00, reachable for critical incidents
- **Responsibility:** Strategic decisions, management communication

**Escalation to Level 5:**
- Critical business impact
- Media relevance
- Regulatory implications

#### Level 5: CEO
- **Contact:** {{ meta-organisation-roles.role_ceo.email }}
- **Phone:** {{ meta-organisation-roles.role_ceo.phone }}
- **Availability:** By appointment
- **Responsibility:** Company-wide decisions

### Security Incident Escalation

#### Level 1: Security Team
- **Contact:** [TODO: security-team@example.com]
- **Phone:** [TODO: Phone Number]
- **Availability:** 24/7
- **Responsibility:** Incident response, forensics

**Escalation to Level 2:**
- Critical security incident
- Data loss or theft
- Compliance violation

#### Level 2: CISO
- **Contact:** {{ meta-organisation-roles.role_ciso.email }}
- **Phone:** {{ meta-organisation-roles.role_ciso.phone }}
- **Availability:** 24/7 for security incidents
- **Responsibility:** Security strategy, compliance

**Escalation to Level 3:**
- Severe data loss
- Public disclosure required
- Regulatory reporting obligation

#### Level 3: CIO / CEO
- **Contact:** {{ meta-organisation-roles.role_cio.email }} / {{ meta-organisation-roles.role_ceo.email }}
- **Availability:** By appointment
- **Responsibility:** Company-wide communication, legal action

## External Vendors and Suppliers

### Hardware Vendor

#### [TODO: Hardware Vendor Name]
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Support Hotline:** [TODO: Support Number]
- **Contract Number:** [TODO: Contract Number]
- **Contract End:** [TODO: Date]
- **Support Level:** [TODO: 24/7, Business Hours]
- **Response Time:** [TODO: 4h, 8h, Next Business Day]
- **Services:**
  - Hardware delivery
  - Warranty and repair
  - Spare parts service

### Software Vendor

#### [TODO: Software Vendor Name]
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Support Portal:** [TODO: URL]
- **Contract Number:** [TODO: Contract Number]
- **License Count:** [TODO: Number]
- **Contract End:** [TODO: Date]
- **Support Level:** [TODO: Standard, Premium, Enterprise]
- **Services:**
  - Software updates
  - Bug fixes
  - Technical support
  - Training

### Cloud Provider

#### [TODO: Cloud Provider Name]
- **Account Manager:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Support Hotline:** [TODO: Support Number]
- **Account ID:** [TODO: Account ID]
- **Support Plan:** [TODO: Basic, Business, Enterprise]
- **Services:**
  - Cloud infrastructure
  - 24/7 support
  - SLA: [TODO: Availability]
  - Technical support

**Support Channels:**
- **Phone:** [TODO: Number]
- **Chat:** [TODO: URL]
- **Ticket:** [TODO: Portal URL]
- **Emergency:** [TODO: Emergency Number]

### Network Provider

#### Internet Provider
- **Provider:** [TODO: Provider Name]
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Fault Hotline:** [TODO: Fault Number]
- **Contract Number:** [TODO: Contract Number]
- **Bandwidth:** [TODO: Bandwidth]
- **SLA:** [TODO: Availability]
- **Services:**
  - Internet connectivity
  - 24/7 support
  - Fault resolution

### Managed Service Provider

#### [TODO: MSP Name]
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Support Hotline:** [TODO: Support Number]
- **Contract Number:** [TODO: Contract Number]
- **Contract End:** [TODO: Date]
- **Support Level:** [TODO: 24/7, Business Hours]
- **Services:**
  - [TODO: Managed Services]
  - [TODO: Monitoring]
  - [TODO: Support]

### Backup Service Provider

#### [TODO: Backup Provider Name]
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Support Hotline:** [TODO: Support Number]
- **Contract Number:** [TODO: Contract Number]
- **Storage Capacity:** [TODO: Capacity]
- **Retention:** [TODO: Retention Period]
- **Services:**
  - Backup storage
  - Disaster recovery
  - 24/7 support

### Security Service Provider

#### [TODO: Security Provider Name]
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **SOC Hotline:** [TODO: SOC Number]
- **Contract Number:** [TODO: Contract Number]
- **Services:**
  - Security monitoring
  - Incident response
  - Threat intelligence
  - Penetration testing

## Emergency Contacts

### Critical Situations

#### Fire / Medical Emergency
- **Emergency:** 112
- **Building Security:** [TODO: Phone Number]
- **First Aid:** [TODO: First Responder Contact]

#### Police
- **Emergency:** 110
- **Local Police:** [TODO: Phone Number]

#### Building Management
- **Facility Management:** [TODO: Phone Number]
- **Availability:** 24/7
- **Responsibility:** Building security, access

#### Legal Department
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 09:00-17:00, emergency hotline
- **Responsibility:** Legal advice, contracts

#### PR / Communications
- **Contact Person:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 09:00-18:00, emergency hotline
- **Responsibility:** External communication, media

## Communication Channels

### Internal Communication

#### Email
- **Primary:** Official communication
- **Distribution Lists:**
  - IT Team: [TODO: it-team@example.com]
  - Management: [TODO: management@example.com]
  - All Hands: [TODO: all@example.com]

#### Chat / Collaboration
- **Platform:** [TODO: Chat Platform]
- **Channels:**
  - #it-operations: Daily operations
  - #incidents: Incident communication
  - #changes: Change communication
  - #general: General communication

#### Phone Conference
- **System:** [TODO: Conferencing System]
- **Bridge Number:** [TODO: Phone Number]
- **PIN:** [TODO: PIN]

#### Video Conference
- **System:** [TODO: Video System]
- **URL:** [TODO: Meeting URL]

### External Communication

#### Customer Communication
- **Email:** [TODO: support@example.com]
- **Phone:** [TODO: Support Number]
- **Portal:** [TODO: Portal URL]

#### Status Page
- **URL:** [TODO: status.example.com]
- **Purpose:** Public status updates
- **Update:** During incidents and maintenance

#### Social Media
- **Twitter:** [TODO: @company]
- **LinkedIn:** [TODO: Company Page]
- **Purpose:** Public announcements

## Contact Update

### Update Process

1. **Report Changes:**
   - Email to {{ meta-organisation-roles.role_it_operations_manager.email }}
   - Provide new contact details
   - Specify effective date

2. **Validation:**
   - IT Operations Manager reviews change
   - Obtain approval (if required)

3. **Update:**
   - Update document
   - Update CMDB
   - Inform affected teams

4. **Verification:**
   - Test new contact details
   - Obtain confirmation

### Review Cycle
- **Frequency:** Quarterly
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Process:**
  - Review all contacts
  - Check for accuracy
  - Document changes
  - Inform teams

## Processes and Responsibilities

### RACI Matrix

| Activity | CIO | Ops Manager | Ops Team | Service Desk |
|---|---|---|---|---|
| Contact Management | C | A | R | C |
| Escalation Level 1-2 | I | C | R | R |
| Escalation Level 3-4 | A | R | C | I |
| Vendor Management | A | R | C | I |
| Emergency Communication | A | R | C | I |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance and Standards

### Relevant Standards
- **ITIL v4:** Service Desk Practice, Incident Management
- **ISO 20000:** Clause 8.2 - Service Desk
- **COBIT 2019:** DSS02 - Managed Service Requests and Incidents

### Audit Requirements
- Current contact lists
- Escalation path documentation
- Vendor contracts
- Communication protocols

## Appendix

### Glossary

| Term | Definition |
|---|---|
| On-Call | Standby duty outside regular working hours |
| Escalation | Forwarding to higher support level |
| SLA | Service Level Agreement - agreement on service performance |
| MSP | Managed Service Provider - external service provider |

### References
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

## Quick Reference

### Most Important Contacts

| Situation | Contact | Phone |
|---|---|---|
| IT Support | {{ meta-organisation-roles.role_service_desk_lead.name }} | {{ meta-organisation-roles.role_service_desk_lead.phone }} |
| Critical Incident | IT Operations Manager | {{ meta-organisation-roles.role_it_operations_manager.phone }} |
| Security Incident | {{ meta-organisation-roles.role_ciso.name }} | {{ meta-organisation-roles.role_ciso.phone }} |
| Management Escalation | {{ meta-organisation-roles.role_cio.name }} | {{ meta-organisation-roles.role_cio.phone }} |
| Emergency (Fire/Medical) | Emergency | 112 |
| Police | Emergency | 110 |

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_it_operations_manager.email }}

