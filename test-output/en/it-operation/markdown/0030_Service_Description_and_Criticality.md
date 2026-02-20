# Service Description and Criticality

**Document-ID:** [FRAMEWORK]-0030
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

## Service Description

### Basic Information

- **Service Name:** [TODO: Unique Service Name]
- **Service ID:** [TODO: Unique Service Identification]
- **Service Owner:** [TODO]
- **Technical Contact:** [TODO: Name and Contact]
- **Organization:** AdminSend GmbH

### Brief Description

[TODO: Describe the service in 2-3 sentences. What does the service do? What main functions does it provide?]

### Business Purpose

**Business Value:**
[TODO: What business value does this service deliver? Which business processes does it support?]

**Strategic Importance:**
[TODO: How important is this service for the company strategy?]

### Customers and User Groups

| User Group | Number of Users | Usage Type | Criticality |
|---|---:|---|---|
| [TODO: Group 1] | [TODO] | [TODO: Primary/Secondary] | [TODO: High/Medium/Low] |
| [TODO: Group 2] | [TODO] | [TODO: Primary/Secondary] | [TODO: High/Medium/Low] |
| [TODO: Group 3] | [TODO] | [TODO: Primary/Secondary] | [TODO: High/Medium/Low] |

**Primary User Groups:**
- [TODO: Description of main users]

**Secondary User Groups:**
- [TODO: Description of secondary users]

### Dependencies on Other Services

#### Upstream Dependencies (Services this service depends on)

| Service | Dependency Type | Criticality | Impact on Failure |
|---|---|---|---|
| [TODO: Service 1] | [TODO: Hard/Soft] | [TODO: High/Medium/Low] | [TODO: Description] |
| [TODO: Service 2] | [TODO: Hard/Soft] | [TODO: High/Medium/Low] | [TODO: Description] |

#### Downstream Dependencies (Services that depend on this service)

| Service | Dependency Type | Criticality | Impact on Failure |
|---|---|---|---|
| [TODO: Service 1] | [TODO: Hard/Soft] | [TODO: High/Medium/Low] | [TODO: Description] |
| [TODO: Service 2] | [TODO: Hard/Soft] | [TODO: High/Medium/Low] | [TODO: Description] |

> **Note:**
> - **Hard Dependency:** Service does not function without dependency
> - **Soft Dependency:** Service functions with limitations without dependency

## Criticality and Protection Requirements

### Criticality Assessment

Criticality is assessed according to the dimensions of availability, integrity, confidentiality, and traceability.

| Dimension | Classification | Justification | Measures |
|---|---|---|---|
| **Availability** | ☐ low ☐ medium ☐ high | [TODO: Justification] | [TODO: Protection measures] |
| **Integrity** | ☐ low ☐ medium ☐ high | [TODO: Justification] | [TODO: Protection measures] |
| **Confidentiality** | ☐ low ☐ medium ☐ high | [TODO: Justification] | [TODO: Protection measures] |
| **Traceability** | ☐ low ☐ medium ☐ high | [TODO: Justification] | [TODO: Protection measures] |

### Criticality Levels

#### Low
- **Availability:** Outage tolerable for several days
- **Integrity:** Data loss acceptable, simple recovery
- **Confidentiality:** Public or non-critical information
- **Traceability:** No audit requirements

#### Medium
- **Availability:** Outage tolerable for hours to 1 day
- **Integrity:** Data loss problematic, recovery required
- **Confidentiality:** Internal information, restricted access
- **Traceability:** Basic logging required

#### High
- **Availability:** Outage only tolerable for minutes
- **Integrity:** Data loss unacceptable, immediate recovery
- **Confidentiality:** Confidential data, strict access control
- **Traceability:** Complete audit trail required

### Overall Criticality

**Criticality Classification:** [TODO: Low/Medium/High/Critical]

**Justification:**
[TODO: Summary justification of overall criticality based on individual dimensions]

## Service Hours and Operating Windows

### Service Hours

- **Availability:** [TODO: e.g., 24/7, Mon-Fri 08:00-18:00 CET, Business Hours]
- **Support Hours:** [TODO: When is support available?]
- **Time Zone:** [TODO: e.g., CET/CEST, UTC]

### Operating Model

- **Operating Model:** [TODO: 24/7, Business Hours, Follow-the-Sun]
- **On-Call Availability:** [TODO: Yes/No, Times]
- **Escalation Levels:** [TODO: Level 1/2/3 Support]

### Maintenance Windows

| Maintenance Type | Time Window | Frequency | Duration | Announcement |
|---|---|---|---|---|
| **Planned Maintenance** | [TODO: e.g., Sun 02:00-06:00] | [TODO: Weekly/Monthly] | [TODO: Hours] | [TODO: Days in advance] |
| **Emergency Maintenance** | [TODO: As needed] | [TODO: Ad-hoc] | [TODO: Variable] | [TODO: Immediate] |
| **Patch Window** | [TODO: e.g., 2nd Tuesday/month] | [TODO: Monthly] | [TODO: Hours] | [TODO: Days in advance] |

### Planned Downtimes

**Communication Process:**
1. **Announcement:** At least [TODO: X days] in advance
2. **Channel:** [TODO: Email, Portal, Ticket System]
3. **Recipients:** [TODO: All users, Key stakeholders]
4. **Content:** Time window, reason, impacts, contact person

**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_email }})

## Service Level Agreements (SLA)

### SLA Overview

| Metric | Target Value | Measurement Method | Measurement Source | Reporting |
|---|---:|---|---|---|
| **Availability** | [TODO: e.g., 99.9%] | [TODO: Uptime monitoring] | [TODO: Monitoring tool] | [TODO: Monthly] |
| **MTTR** | [TODO: e.g., 4h] | [TODO: Ticket analysis] | [TODO: ITSM tool] | [TODO: Monthly] |
| **MTBF** | [TODO: e.g., 720h] | [TODO: Incident analysis] | [TODO: ITSM tool] | [TODO: Quarterly] |
| **Response Time** | [TODO: e.g., < 200ms] | [TODO: APM] | [TODO: APM tool] | [TODO: Daily] |
| **Throughput** | [TODO: e.g., 1000 TPS] | [TODO: Performance monitoring] | [TODO: Monitoring tool] | [TODO: Daily] |

### Service Level Objectives (SLO)

#### Availability

- **Target:** [TODO: e.g., 99.9% uptime per month]
- **Calculation:** (Total time - Downtime) / Total time × 100%
- **Exceptions:** Planned maintenance windows
- **Measurement:** Continuous uptime monitoring

#### Performance

- **Response Time (P95):** [TODO: e.g., < 200ms]
- **Response Time (P99):** [TODO: e.g., < 500ms]
- **Throughput:** [TODO: e.g., min. 1000 requests/second]
- **Error Rate:** [TODO: e.g., < 0.1%]

#### Recovery

- **RTO (Recovery Time Objective):** [TODO: e.g., 4 hours]
- **RPO (Recovery Point Objective):** [TODO: e.g., 1 hour]
- **MTTR (Mean Time To Repair):** [TODO: e.g., 4 hours]
- **MTBF (Mean Time Between Failures):** [TODO: e.g., 720 hours]

### SLA Reporting

**Reporting Frequency:** [TODO: Monthly/Quarterly]

**Recipients:**
- Service Owner: [TODO]
- IT Operations Manager: {{ meta-organisation-roles.role_IT_Operations_Manager }}
- CIO: [TODO]
- [TODO: Additional stakeholders]

**Content:**
- Availability statistics
- Performance metrics
- Incident overview
- SLA compliance
- Improvement measures

### SLA Violations

**Escalation Process for SLA Violation:**

1. **Automatic Notification:** Monitoring system
2. **Analysis:** IT Operations team
3. **Escalation Level 1:** IT Operations Manager
4. **Escalation Level 2:** CIO
5. **Root Cause Analysis:** Within [TODO: X days]
6. **Action Plan:** Within [TODO: X days]

## Capacity Planning

### Current Capacity

| Resource | Current | Maximum | Utilization | Threshold |
|---|---:|---:|---:|---:|
| [TODO: CPU] | [TODO] | [TODO] | [TODO]% | [TODO]% |
| [TODO: RAM] | [TODO] | [TODO] | [TODO]% | [TODO]% |
| [TODO: Storage] | [TODO] | [TODO] | [TODO]% | [TODO]% |
| [TODO: Network] | [TODO] | [TODO] | [TODO]% | [TODO]% |

### Growth Forecast

- **User Growth:** [TODO: e.g., +10% per year]
- **Data Growth:** [TODO: e.g., +20% per year]
- **Transaction Growth:** [TODO: e.g., +15% per year]

### Scaling Strategies

- **Vertical Scaling:** [TODO: Description]
- **Horizontal Scaling:** [TODO: Description]
- **Auto-Scaling:** [TODO: Yes/No, Configuration]

## Responsibilities

| Role | Responsibility | Person | Contact |
|---|---|---|---|
| **Service Owner** | Overall responsibility | [TODO] | [TODO: Email] |
| **Technical Lead** | Technical implementation | [TODO: Name] | [TODO: Email] |
| **Operations Manager** | Daily operations | {{ meta-organisation-roles.role_IT_Operations_Manager }} | {{ meta-organisation-roles.role_IT_Operations_Manager_email }} |
| **Service Desk Lead** | First-level support | {{ meta-organisation-roles.role_Service_Desk_Lead }} | {{ meta-organisation-roles.role_Service_Desk_Lead_email }} |

## Contacts and Escalation

**For questions about the service:**
- **Service Owner:** [TODO]
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_email }})
- **Service Desk:** {{ meta-organisation-roles.role_Service_Desk_Lead }} ({{ meta-organisation-roles.role_Service_Desk_Lead_email }})

**Escalation Path:**
1. **Level 1:** Service Desk - {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
2. **Level 2:** IT Operations - {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
3. **Level 3:** CIO - {{ meta-organisation-roles.role_CIO_email }}

**Service Owner:** [TODO]  
**Approved by:** [TODO]  
**Version:** 0  
**Organization:** AdminSend GmbH

