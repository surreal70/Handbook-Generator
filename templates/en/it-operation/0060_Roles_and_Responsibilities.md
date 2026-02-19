# Roles and Responsibilities

**Document-ID:** [FRAMEWORK]-0060
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

## Organizational Structure

### Company Information

- **Organization:** {{ meta-organisation.name }}
- **Address:** {{ meta-organisation.address }}, {{ meta-organisation.postal_code }} {{ meta-organisation.city }}
- **Country:** {{ meta-organisation.country }}
- **Website:** {{ meta-organisation.website }}
- **Phone:** {{ meta-organisation.phone }}
- **Email:** {{ meta-organisation.email }}

### Organizational Overview

[TODO: Insert organizational chart or description of organizational structure here]

## Executive Level

### Chief Executive Officer (CEO)

- **Name:** {{ meta-organisation-roles.role_CEO }}
- **Email:** {{ meta-organisation-roles.role_CEO_email }}
- **Phone:** {{ meta-organisation-roles.role_CEO_phone }}

**Responsibilities:**
- Overall responsibility for the company
- Strategic direction and corporate objectives
- Approval of critical IT investments
- Escalation point for business-critical IT incidents

### Chief Information Officer (CIO)

- **Name:** {{ meta-organisation-roles.role_CIO }}
- **Email:** {{ meta-organisation-roles.role_CIO_email }}
- **Phone:** {{ meta-organisation-roles.role_CIO_phone }}

**Responsibilities:**
- Overall responsibility for IT strategy and operations
- IT budget and resource planning
- IT governance and compliance
- Approval of major changes
- Responsibility for IT service quality and SLA compliance

### Chief Information Security Officer (CISO)

- **Name:** {{ meta-organisation-roles.role_CISO }}
- **Email:** {{ meta-organisation-roles.role_CISO_email }}
- **Phone:** {{ meta-organisation-roles.role_CISO_phone }}

**Responsibilities:**
- IT security strategy and policies
- Information Security Management System (ISMS)
- Security incident response
- Compliance with security standards (ISO 27001, BSI Grundschutz)
- Risk management and vulnerability management
- Security awareness and training

### Chief Financial Officer (CFO)

- **Name:** {{ meta-organisation-roles.role_CFO }}
- **Email:** {{ meta-organisation-roles.role_CFO_email }}
- **Phone:** {{ meta-organisation-roles.role_CFO_phone }}

**Responsibilities:**
- Financial approval of IT projects
- IT budget monitoring
- Cost-benefit analysis for IT investments
- Financial compliance and audits

### Chief Operating Officer (COO)

- **Name:** {{ meta-organisation-roles.role_COO }}
- **Email:** {{ meta-organisation-roles.role_COO_email }}
- **Phone:** {{ meta-organisation-roles.role_COO_phone }}

**Responsibilities:**
- Operational business processes
- Business continuity management
- Coordination between IT and business units
- Service level requirements from business perspective

## IT Operations Level

### IT Operations Manager

- **Name:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
- **Email:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Phone:** {{ meta-organisation-roles.role_IT_Operations_Manager_phone }}

**Responsibilities:**
- Daily IT operations and service delivery
- Monitoring and incident management
- Change management coordination
- Capacity and performance management
- IT operations team leadership
- Escalation management for operational incidents
- Ensuring SLA compliance

**Deputy:** [TODO: Name and contact of deputy]

### Service Desk Lead

- **Name:** {{ meta-organisation-roles.role_Service_Desk_Lead }}
- **Email:** {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **Phone:** {{ meta-organisation-roles.role_Service_Desk_Lead_phone }}

**Responsibilities:**
- First-level support and incident management
- Ticket management and prioritization
- User communication
- Service catalog maintenance
- Service desk team leadership
- Service desk metrics and reporting

**Deputy:** [TODO: Name and contact of deputy]

## Additional IT Roles

### System Administrator

- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Server and system administration
- Patch and update management
- Backup and restore
- System monitoring
- System configuration documentation

### Network Administrator

- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Network infrastructure management
- Firewall and security configuration
- Network monitoring
- VPN and remote access management
- Network documentation

### Database Administrator (DBA)

- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Database administration and optimization
- Database backup and recovery
- Performance tuning
- Database security
- Database monitoring

### Application Manager

- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Application support and maintenance
- Release management for applications
- Application monitoring
- Coordination with development teams
- Application documentation

### Security Administrator

- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Security monitoring and incident response
- Vulnerability scanning and management
- Security patch management
- Access management and permissions
- Security audits and compliance checks

## RACI Matrix for IT Operations Activities

The RACI matrix defines responsibilities for IT operations activities:
- **R** = Responsible (execution responsibility)
- **A** = Accountable (overall responsibility, decision authority)
- **C** = Consulted (must be consulted)
- **I** = Informed (must be informed)

### Service Management

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Service Strategy** | A | R | C | C | C | C | I | I | I | I | I | I |
| **Service Design** | I | A | C | I | C | R | C | C | C | C | C | C |
| **Service Transition** | I | A | C | I | C | R | C | R | R | R | R | C |
| **Service Operation** | I | A | C | I | I | R | R | R | R | R | R | R |
| **Continual Improvement** | I | A | C | I | C | R | C | C | C | C | C | C |

### Incident Management

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Incident Recording** | I | I | I | I | I | C | R | C | C | C | C | C |
| **Incident Classification** | I | I | C | I | I | C | R | C | C | C | C | C |
| **Incident Diagnosis** | I | I | C | I | I | C | R | R | R | R | R | R |
| **Incident Resolution** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Incident Closure** | I | I | I | I | I | A | R | C | C | C | C | C |
| **Major Incident** | I | A | C | I | C | R | R | R | R | R | R | R |

### Problem Management

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Problem Identification** | I | I | C | I | I | A | R | R | R | R | R | R |
| **Problem Analysis** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Root Cause Analysis** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Workaround Development** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Known Error Documentation** | I | I | I | I | I | A | R | C | C | C | C | C |
| **Problem Resolution** | I | A | C | I | I | R | C | R | R | R | R | R |

### Change Management

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Change Request** | I | I | C | I | I | C | C | R | R | R | R | R |
| **Change Assessment** | I | C | C | I | C | A | I | R | R | R | R | R |
| **Change Approval (Standard)** | I | I | I | I | I | A | I | I | I | I | I | I |
| **Change Approval (Normal)** | I | A | C | I | C | R | I | I | I | I | I | I |
| **Change Approval (Emergency)** | I | A | C | I | C | R | I | I | I | I | I | I |
| **Change Implementation** | I | I | C | I | I | A | I | R | R | R | R | R |
| **Change Review** | I | A | C | I | I | R | C | C | C | C | C | C |

### Security Management

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Security Strategy** | A | C | R | C | C | C | I | I | I | I | I | I |
| **Security Policies** | A | C | R | I | C | C | I | C | C | C | C | C |
| **Security Monitoring** | I | I | A | I | I | C | I | C | C | C | C | R |
| **Security Incident** | I | A | R | I | C | C | C | C | C | C | C | R |
| **Vulnerability Management** | I | I | A | I | I | C | I | C | C | C | C | R |
| **Access Management** | I | I | A | I | I | C | C | R | R | R | R | R |
| **Security Audits** | I | A | R | C | C | C | I | C | C | C | C | R |

### Backup and Recovery

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Backup Strategy** | I | A | C | I | C | R | I | C | C | C | C | C |
| **Backup Execution** | I | I | I | I | I | A | I | R | C | R | C | I |
| **Backup Monitoring** | I | I | I | I | I | A | I | R | C | R | C | I |
| **Backup Testing** | I | I | C | I | I | A | I | R | C | R | C | C |
| **Restore Execution** | I | I | C | I | I | A | C | R | C | R | C | C |
| **Disaster Recovery** | I | A | C | I | C | R | C | R | R | R | R | C |

### Monitoring and Performance

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Monitoring Strategy** | I | A | C | I | C | R | I | C | C | C | C | C |
| **Monitoring Configuration** | I | I | C | I | I | A | I | R | R | R | R | R |
| **24/7 Monitoring** | I | I | C | I | I | A | R | R | R | R | R | R |
| **Alert Management** | I | I | C | I | I | A | R | R | R | R | R | R |
| **Performance Tuning** | I | I | I | I | I | A | I | R | R | R | R | I |
| **Capacity Planning** | I | A | I | C | C | R | I | C | C | C | C | I |

### Compliance and Audits

| Activity | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Compliance Strategy** | A | R | C | C | C | C | I | I | I | I | I | I |
| **Compliance Controls** | I | A | R | C | C | C | I | C | C | C | C | C |
| **Audit Preparation** | I | A | R | C | C | R | C | C | C | C | C | C |
| **Audit Execution** | C | A | R | C | C | R | C | C | C | C | C | C |
| **Audit Follow-up** | I | A | R | I | C | R | I | C | C | C | C | C |

## Contact Lists and Availability

### Executive Level - Contacts

| Role | Name | Email | Phone | Mobile | Availability |
|---|---|---|---|---|---|
| **CEO** | {{ meta-organisation-roles.role_CEO }} | {{ meta-organisation-roles.role_CEO_email }} | {{ meta-organisation-roles.role_CEO_phone }} | [TODO] | Mon-Fri 09:00-17:00 |
| **CIO** | {{ meta-organisation-roles.role_CIO }} | {{ meta-organisation-roles.role_CIO_email }} | {{ meta-organisation-roles.role_CIO_phone }} | [TODO] | Mon-Fri 08:00-18:00 |
| **CISO** | {{ meta-organisation-roles.role_CISO }} | {{ meta-organisation-roles.role_CISO_email }} | {{ meta-organisation-roles.role_CISO_phone }} | [TODO] | Mon-Fri 08:00-18:00 |
| **CFO** | {{ meta-organisation-roles.role_CFO }} | {{ meta-organisation-roles.role_CFO_email }} | {{ meta-organisation-roles.role_CFO_phone }} | [TODO] | Mon-Fri 09:00-17:00 |
| **COO** | {{ meta-organisation-roles.role_COO }} | {{ meta-organisation-roles.role_COO_email }} | {{ meta-organisation-roles.role_COO_phone }} | [TODO] | Mon-Fri 08:00-18:00 |

### IT Operations - Contacts

| Role | Name | Email | Phone | Mobile | Availability |
|---|---|---|---|---|---|
| **IT Ops Manager** | {{ meta-organisation-roles.role_IT_Operations_Manager }} | {{ meta-organisation-roles.role_IT_Operations_Manager_email }} | {{ meta-organisation-roles.role_IT_Operations_Manager_phone }} | [TODO] | Mon-Fri 07:00-19:00 |
| **Service Desk Lead** | {{ meta-organisation-roles.role_Service_Desk_Lead }} | {{ meta-organisation-roles.role_Service_Desk_Lead_email }} | {{ meta-organisation-roles.role_Service_Desk_Lead_phone }} | [TODO] | Mon-Fri 08:00-17:00 |
| **System Admin** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Network Admin** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **DBA** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **App Manager** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Security Admin** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### Service Desk - Contacts

**Central Service Desk Number:** [TODO: Phone number]  
**Service Desk Email:** [TODO: Email address]  
**Service Portal:** [TODO: URL]

**Service Hours:**
- **Regular:** Mon-Fri 08:00-17:00
- **Extended:** [TODO: If applicable]
- **24/7:** [TODO: If applicable]

## On-Call and Standby Duty

### On-Call Model

**Operating Model:** [TODO: 24/7, Business Hours, Follow-the-Sun]

**On-Call Hours:**
- **Weekdays:** [TODO: e.g., 17:00-08:00]
- **Weekend:** [TODO: e.g., Fri 17:00 - Mon 08:00]
- **Holidays:** [TODO: 24 hours]

### On-Call Rotation

| Week | Primary | Secondary | Escalation |
|---|---|---|---|
| **Week [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **Week [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **Week [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **Week [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |

**Rotation Schedule:** [TODO: Link to current on-call schedule]

### On-Call Contacts

**Primary On-Call:**
- **Phone:** [TODO: On-call number]
- **Email:** [TODO: On-call email]
- **Availability:** [TODO: Response time]

**Secondary On-Call:**
- **Phone:** [TODO: Backup number]
- **Email:** [TODO: Backup email]
- **Availability:** [TODO: Response time]

**Escalation:**
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_phone }})
- **CIO:** {{ meta-organisation-roles.role_CIO }} ({{ meta-organisation-roles.role_CIO_phone }})

### On-Call Process

**1. Alerting:**
- Monitoring system sends alert
- Automatic notification to on-call person
- Channels: SMS, phone, email, push notification

**2. Response:**
- **Response Time:** [TODO: e.g., 15 minutes]
- **Acknowledgment:** On-call person confirms receipt
- **Initial Analysis:** Within [TODO: e.g., 30 minutes]

**3. Escalation:**
- **Level 1:** Primary on-call (0-15 min)
- **Level 2:** Secondary on-call (15-30 min)
- **Level 3:** IT Operations Manager (30-60 min)
- **Level 4:** CIO (> 60 min or critical incident)

**4. Documentation:**
- Document all activities in ticket system
- Timestamps for all actions
- Post-incident review for major incidents

### On-Call Guidelines

**Availability:**
- On-call person must be reachable
- Response time: [TODO: e.g., 15 minutes]
- Access to laptop and VPN required
- Sobriety during on-call duty

**Compensation:**
- On-call allowance: [TODO: Amount]
- Call-out fee: [TODO: Hourly rate]
- Time off in lieu: [TODO: Policy]

**Handover:**
- Handover call at end of on-call duty
- Documentation of open incidents
- Briefing of next on-call person

## Escalation Paths

### Standard Escalation

```
Level 1: Service Desk
    ↓ (15 min)
Level 2: Specialist (Sys/Net/DB/App Admin)
    ↓ (30 min)
Level 3: IT Operations Manager
    ↓ (60 min)
Level 4: CIO
    ↓ (critical)
Level 5: CEO
```

### Security Incident Escalation

```
Security Alert
    ↓ (immediate)
Security Administrator
    ↓ (15 min)
CISO
    ↓ (30 min for major incident)
CIO + CEO
    ↓ (for data breach)
Data Protection Officer + Authorities
```

### Business-Critical Incident Escalation

```
Major Incident
    ↓ (immediate)
IT Operations Manager + On-Call
    ↓ (15 min)
CIO + CISO
    ↓ (30 min)
COO + CEO
    ↓ (if needed)
External Service Providers + Vendors
```

### Escalation Criteria

**Automatic Escalation When:**
- No response within defined time
- Incident cannot be resolved
- Multiple critical systems affected
- Data protection or security incident
- Business-critical services down

**Escalation Times:**
- **P1 (Critical):** 15 min → 30 min → 60 min
- **P2 (High):** 30 min → 60 min → 2 hrs
- **P3 (Medium):** 2 hrs → 4 hrs → 8 hrs
- **P4 (Low):** 8 hrs → 1 day → 2 days

## Deputy Arrangements

### Executive Level - Deputies

| Role | Primary | Deputy 1 | Deputy 2 |
|---|---|---|---|
| **CEO** | {{ meta-organisation-roles.role_CEO }} | [TODO: Name] | [TODO: Name] |
| **CIO** | {{ meta-organisation-roles.role_CIO }} | {{ meta-organisation-roles.role_IT_Operations_Manager }} | [TODO: Name] |
| **CISO** | {{ meta-organisation-roles.role_CISO }} | [TODO: Name] | {{ meta-organisation-roles.role_CIO }} |
| **CFO** | {{ meta-organisation-roles.role_CFO }} | [TODO: Name] | [TODO: Name] |
| **COO** | {{ meta-organisation-roles.role_COO }} | [TODO: Name] | [TODO: Name] |

### IT Operations - Deputies

| Role | Primary | Deputy 1 | Deputy 2 |
|---|---|---|---|
| **IT Ops Manager** | {{ meta-organisation-roles.role_IT_Operations_Manager }} | [TODO: Name] | {{ meta-organisation-roles.role_CIO }} |
| **Service Desk Lead** | {{ meta-organisation-roles.role_Service_Desk_Lead }} | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **System Admin** | [TODO: Name] | [TODO: Name] | [TODO: Name] |
| **Network Admin** | [TODO: Name] | [TODO: Name] | [TODO: Name] |
| **DBA** | [TODO: Name] | [TODO: Name] | [TODO: Name] |

### Deputy Process

**For Planned Absence:**
1. Inform deputy at least [TODO: e.g., 1 week] in advance
2. Create handover documentation
3. Hand over open issues and incidents
4. Update contact information
5. Set out-of-office message with deputy contact

**For Unplanned Absence:**
1. Inform supervisor
2. Automatic deputy arrangement takes effect
3. Deputy assumes all ongoing tasks
4. Subsequent handover upon return

## Training and Qualifications

### Required Qualifications

| Role | Required Certifications | Recommended Training |
|---|---|---|
| **IT Ops Manager** | ITIL Foundation, ITIL Managing Professional | COBIT, ISO 20000 |
| **Service Desk Lead** | ITIL Foundation | ITIL Specialist, HDI Support Center Manager |
| **System Admin** | [TODO: e.g., MCSA, RHCSA] | [TODO: Vendor certifications] |
| **Network Admin** | [TODO: e.g., CCNA, CCNP] | [TODO: Network security] |
| **DBA** | [TODO: e.g., Oracle DBA, MCDBA] | [TODO: Performance tuning] |
| **Security Admin** | [TODO: e.g., CISSP, CEH] | [TODO: Security frameworks] |

### Training Plan

**Annual Mandatory Training:**
- IT security and data protection (all staff)
- ITIL refresher (IT operations team)
- Incident management processes (service desk)
- Change management processes (all IT staff)

**Individual Development:**
- Budget: [TODO: Amount per employee/year]
- Approval: IT Operations Manager / CIO
- Documentation: Training certificates in personnel file

## Change History

| Version | Date | Author | Changes | Approved by |
|---|---|---|---|---|
| 1.0.0 | [TODO] | {{ meta-handbook.owner }} | Initial version | {{ meta-handbook.approver }} |

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Classification:** {{ meta-handbook.classification }}  
**Organization:** {{ meta-organisation.name }}

