# Contacts, Escalation, and Vendors

## Overview

This document contains contact lists, escalation paths, vendors and suppliers, as well as support contacts for the IT service. The goal is to ensure quick access to relevant contact information in all situations.

**Document Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Organization:** {{ meta.organization.name }}

---

## Internal Contacts

### Management

#### Chief Executive Officer (CEO)
- **Name:** {{ meta.ceo.name }}
- **Title:** {{ meta.ceo.title }}
- **Email:** {{ meta.ceo.email }}
- **Phone:** {{ meta.ceo.phone }}
- **Department:** {{ meta.ceo.department }}
- **Availability:** Mon-Fri 09:00-18:00
- **Escalation:** Only for critical business impact situations

#### Chief Information Officer (CIO)
- **Name:** {{ meta.cio.name }}
- **Title:** {{ meta.cio.title }}
- **Email:** {{ meta.cio.email }}
- **Phone:** {{ meta.cio.phone }}
- **Department:** {{ meta.cio.department }}
- **Availability:** Mon-Fri 08:00-18:00
- **Escalation:** IT strategic decisions, critical incidents

#### Chief Information Security Officer (CISO)
- **Name:** {{ meta.ciso.name }}
- **Title:** {{ meta.ciso.title }}
- **Email:** {{ meta.ciso.email }}
- **Phone:** {{ meta.ciso.phone }}
- **Department:** {{ meta.ciso.department }}
- **Availability:** Mon-Fri 08:00-18:00, 24/7 for security incidents
- **Escalation:** Security incidents, compliance questions

---

### IT Operations

#### IT Operations Manager
- **Name:** {{ meta.it_operations_manager.name }}
- **Title:** {{ meta.it_operations_manager.title }}
- **Email:** {{ meta.it_operations_manager.email }}
- **Phone:** {{ meta.it_operations_manager.phone }}
- **Department:** {{ meta.it_operations_manager.department }}
- **Availability:** Mon-Fri 08:00-18:00, On-call for P1 incidents
- **Responsibility:** Overall responsibility for IT operations

#### Service Desk Lead
- **Name:** {{ meta.service_desk_lead.name }}
- **Title:** {{ meta.service_desk_lead.title }}
- **Email:** {{ meta.service_desk_lead.email }}
- **Phone:** {{ meta.service_desk_lead.phone }}
- **Department:** {{ meta.service_desk_lead.department }}
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** First-level support, ticket management

---

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

---

## Escalation Paths

### Incident Escalation

#### Level 1: Service Desk
- **Contact:** {{ meta.service_desk_lead.email }}
- **Phone:** {{ meta.service_desk_lead.phone }}
- **Availability:** Mon-Fri 08:00-18:00
- **Responsibility:** First-level support, ticket creation

**Escalation to Level 2:**
- P1: Immediately
- P2: After 1 hour without solution
- P3: After 4 hours without solution
- P4: After 8 hours without solution

---

#### Level 2: Operations Team
- **Contact:** [TODO: ops-team@example.com]
- **Phone:** [TODO: Phone Number]
- **Availability:** Mon-Fri 08:00-18:00, On-call 24/7
- **Responsibility:** Second-level support, technical analysis

**Escalation to Level 3:**
- P1: After 2 hours without solution
- P2: After 4 hours without solution
- P3: After 8 hours without solution

---

#### Level 3: IT Operations Manager
- **Contact:** {{ meta.it_operations_manager.email }}
- **Phone:** {{ meta.it_operations_manager.phone }}
- **Availability:** Mon-Fri 08:00-18:00, On-call for P1
- **Responsibility:** Coordination, resource allocation

**Escalation to Level 4:**
- P1: After 4 hours without solution
- P2: After 8 hours without solution
- When external support required

---

#### Level 4: CIO
- **Contact:** {{ meta.cio.email }}
- **Phone:** {{ meta.cio.phone }}
- **Availability:** Mon-Fri 08:00-18:00, reachable for critical incidents
- **Responsibility:** Strategic decisions, management communication

**Escalation to Level 5:**
- Critical business impact
- Media relevance
- Regulatory implications

---

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

---

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

---

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

---

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

---

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

---

## Contact Update

### Update Process

1. **Report Changes:**
   - Email to {{ meta.it_operations_manager.email }}
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
- **Responsible:** {{ meta.it_operations_manager.name }}

---

## Quick Reference

### Most Important Contacts

| Situation | Contact | Phone |
|---|---|---|
| IT Support | {{ meta.service_desk_lead.name }} | {{ meta.service_desk_lead.phone }} |
| Critical Incident | IT Operations Manager | {{ meta.it_operations_manager.phone }} |
| Security Incident | {{ meta.ciso.name }} | {{ meta.ciso.phone }} |
| Management Escalation | {{ meta.cio.name }} | {{ meta.cio.phone }} |
| Emergency (Fire/Medical) | Emergency | 112 |
| Police | Emergency | 110 |

---

**Last Update:** {{ meta.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta.it_operations_manager.email }}
