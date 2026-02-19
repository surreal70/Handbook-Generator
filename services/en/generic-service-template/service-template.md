# Service: {{ meta-service.name }}

<!-- 
INSTRUCTIONS: Document Header
- All fields with {{ }} are automatically populated from meta-service.yaml
- Adjust the values in meta-service.yaml to match your specific service
- Document ID should be unique (e.g., SVC-001, SVC-EMAIL, etc.)
-->

**Document ID:** {{ meta-service.id }}  
**Organization:** {{ meta-organisation.name }}  
**Service Owner:** {{ meta-service.owner }}  
**Service Manager:** {{ meta-service.manager }}  
**Revision:** {{ meta-service.revision }}  
**Author:** {{ meta-service.source }}  
**Status:** {{ meta-service.status }}  
**Last Updated:** {{ meta-service.modifydate }}  
**Template Version:** {{ meta-service.version }}

---

## 1. Service Overview

<!-- 
INSTRUCTIONS: Service Overview
- Describe the main functionality of your service here
- Specify the target audience (e.g., "all employees", "development team", "sales")
- List the main components
- Example: "This service provides email communication and supports all employees"
-->

### 1.1 Description

This service provides [description of main functionality] and supports [target audience/business processes].

The service includes:
- [Main component 1]
- [Main component 2]
- [Main component 3]

### 1.2 Service Category

<!-- 
INSTRUCTIONS: Service Category
- Category is loaded from meta-service.yaml
- Possible values: infrastructure, application, business, security, support
- Criticality: Critical, High, Medium, Low
-->

**Category:** {{ meta-service.category }}  
**Criticality:** {{ meta-service.criticality }}

### 1.3 Service Objectives

<!-- 
INSTRUCTIONS: Service Objectives
- Adapt the objectives to your specific service
- Focus on measurable objectives
- Examples: "99.9% availability", "< 1 second response time"
-->

The main objectives of this service are:

- **Availability:** Ensuring high availability for business-critical processes
- **Performance:** Guaranteeing optimal response times and throughput
- **Security:** Protecting data and systems according to compliance requirements
- **Reliability:** Minimizing outages and disruptions

### 1.4 Benefits to the Organization

<!-- 
INSTRUCTIONS: Benefits
- Describe the specific business value
- Examples: "Enables mobile work", "Reduces manual processes by 50%"
-->

- Supporting business processes through [specific benefit]
- Improving productivity through [specific benefit]
- Reducing risks through [specific benefit]

---

## 2. COBIT Mapping

<!-- 
INSTRUCTIONS: COBIT Mapping
- COBIT processes are loaded from meta-service.yaml
- Select relevant COBIT 2019 processes
- Typical processes: DSS01 (Manage Operations), DSS02 (Manage Service Requests), DSS05 (Manage Security Services)
- Documentation: https://www.isaca.org/resources/cobit
-->

**COBIT Version:** {{ meta-global-service.compliance.cobit_version }}

### 2.1 Relevant Processes

This service supports the following COBIT processes:

{{ meta-service.cobit.processes }}

### 2.2 Controls

The following controls are addressed by this service:

{{ meta-service.cobit.controls }}

### 2.3 Governance Requirements

<!-- 
INSTRUCTIONS: Governance
- Describe specific governance requirements for this service
- Examples: "Monthly reporting to IT steering committee"
-->

- **Monitoring:** Regular review of service performance
- **Compliance:** Adherence to internal and external requirements
- **Risk Management:** Identification and treatment of service risks

---

## 3. ITIL Mapping

<!-- 
INSTRUCTIONS: ITIL Mapping
- ITIL processes are loaded from meta-service.yaml
- Select relevant ITIL 4 processes
- Lifecycle phases: Service Strategy, Service Design, Service Transition, Service Operation, Continual Service Improvement
- Documentation: https://www.axelos.com/certifications/itil-service-management
-->

**ITIL Version:** {{ meta-global-service.compliance.itil_version }}

### 3.1 Lifecycle Phase

**Current Phase:** {{ meta-service.itil.lifecycle_phase }}

### 3.2 ITIL Processes

This service is integrated into the following ITIL processes:

{{ meta-service.itil.processes }}

### 3.3 Service Lifecycle Activities

<!-- 
INSTRUCTIONS: Lifecycle Activities
- Describe specific activities in each phase
- Example Service Strategy: "Annual review of service strategy in Q4"
-->

#### Service Strategy
- Definition of service strategy and positioning
- Identification of business requirements

#### Service Design
- Architecture and design of the service
- Definition of SLAs and OLAs

#### Service Transition
- Planning and execution of changes
- Knowledge management and documentation

#### Service Operation
- Daily operations and support
- Incident and problem management

#### Continual Service Improvement
- Regular service reviews
- Implementation of improvement measures

---

## 4. Service Components

<!-- 
INSTRUCTIONS: Service Components
- Technology stack is loaded from meta-service.yaml
- Describe the technical architecture
- Add architecture diagrams (e.g., as PNG/SVG)
-->

### 4.1 Technology Stack

- **Platform:** {{ meta-service.technology.platform }}
- **Backup:** {{ meta-service.technology.backup }}
- **Monitoring:** {{ meta-service.technology.monitoring }}

### 4.2 Architecture Overview

<!-- 
INSTRUCTIONS: Architecture
- Insert an architecture diagram here
- Describe the main components and their interaction
- Example: "Load Balancer -> Web Server -> Application Server -> Database"
-->

[Description of service architecture]

```
[Architecture diagram or description]
```

### 4.3 Interfaces and Dependencies

<!-- 
INSTRUCTIONS: Interfaces
- List all interfaces to other services
- Internal interfaces: Other IT services in your organization
- External interfaces: Cloud services, partner systems
- Dependencies: Services this service depends on
-->

#### Internal Interfaces
- [Interface 1]: Description
- [Interface 2]: Description

#### External Interfaces
- [External interface 1]: Description
- [External interface 2]: Description

#### Dependencies
- [Dependent service 1]: Type of dependency
- [Dependent service 2]: Type of dependency

---

## 5. Service Level Agreements (SLAs)

<!-- 
INSTRUCTIONS: SLAs
- SLA values are loaded from meta-service.yaml
- Adjust the values to match your service requirements
- Availability: Typical 99.5% (Standard), 99.9% (High), 99.99% (Critical)
- Response Times: P1 (Critical), P2 (High), P3 (Medium), P4 (Low)
-->

### 5.1 Availability

**Availability Target:** {{ meta-service.sla.availability_target }}

**Measurement Period:** Monthly  
**Exceptions:** Planned maintenance windows

### 5.2 Response Times

The following response times apply to service requests:

| Priority | Description | Response Time | Resolution Time |
|----------|-------------|---------------|-----------------|
| P1 - Critical | Complete service outage | {{ meta-service.sla.response_time_p1 }} | 4 hours |
| P2 - High | Partial outage, workaround available | {{ meta-service.sla.response_time_p2 }} | 8 hours |
| P3 - Medium | Limited functionality | {{ meta-service.sla.response_time_p3 }} | 2 business days |
| P4 - Low | Requests and information | {{ meta-service.sla.response_time_p4 }} | 5 business days |

### 5.3 Performance Targets

<!-- 
INSTRUCTIONS: Performance Targets
- Define measurable performance targets
- Examples: "< 2 seconds response time for 95% of requests"
- Adapt to your service
-->

- **Response Time:** < 2 seconds for 95% of requests
- **Throughput:** [Specific throughput requirements]
- **Capacity:** [Capacity requirements]

### 5.4 SLA Reporting

<!-- 
INSTRUCTIONS: SLA Reporting
- Define reporting frequency and recipients
- Example: "Monthly SLA report to service owner and stakeholders"
-->

- Monthly SLA reports to service owner
- Quarterly service reviews with stakeholders
- Escalation for SLA violations

---

## 6. Operational Level Agreements (OLAs)

<!-- 
INSTRUCTIONS: OLAs
- OLAs are internal agreements between IT teams
- Define responsibilities and response times
- Example: "Network team restores connectivity within 2 hours"
-->

### 6.1 Internal Support Agreements

| Support Team | Responsibility | Response Time |
|--------------|----------------|---------------|
| [Team 1] | [Responsibility] | [Time] |
| [Team 2] | [Responsibility] | [Time] |

### 6.2 Maintenance Windows

**Standard Maintenance Window:** {{ support.maintenance_window }}

During maintenance windows, the following activities may be performed:
- System updates and patches
- Configuration changes
- Backup verification

---

## 7. Roles and Responsibilities

<!-- 
INSTRUCTIONS: Roles
- Roles are loaded from meta-service.yaml and meta-organisation-roles.yaml
- Service Owner: Strategic responsibility, budget
- Service Manager: Operational management, day-to-day operations
- Adapt the RACI matrix to your organization
-->

### 7.1 Service Organization

| Role | Name | Contact | Responsibility |
|------|------|---------|----------------|
| Service Owner | {{ meta-service.owner }} | {{ meta-service.owner_email }} | Strategic responsibility, budget, service strategy |
| Service Manager | {{ meta-service.manager }} | {{ meta-service.manager_email }} | Operational management, SLA compliance, team leadership |

### 7.2 RACI Matrix

<!-- 
INSTRUCTIONS: RACI Matrix
- R = Responsible (Execution): Who performs the activity?
- A = Accountable (Responsible): Who has overall responsibility?
- C = Consulted (Consulted): Who is asked for advice?
- I = Informed (Informed): Who is informed?
- Adapt the activities and roles to your service
- Add more roles (e.g., {{ role_CISO }}, {{ role_System_Administrator }})
- Role names are loaded from meta-service.yaml and meta-organisation-roles.yaml
-->

| Activity | {{ meta-service.owner }} | {{ meta-service.manager }} | {{ role_System_Administrator }} | {{ role_Service_Desk_Lead }} |
|----------|---------------|-----------------|--------------|----------|
| Service Strategy | A | C | I | I |
| SLA Definition | A | R | C | I |
| Daily Operations | I | A | R | - |
| Incident Handling | I | A | R | I |
| Change Approval | C | C | R | - |

**Legend:**
- R = Responsible (Execution)
- A = Accountable (Responsible)
- C = Consulted (Consulted)
- I = Informed (Informed)

---

## 8. Support Model

<!-- 
INSTRUCTIONS: Support Model
- Support hours are loaded from service-config.yaml
- Define available support channels
- Escalation path is loaded from service-config.yaml
-->

### 8.1 Support Hours

- **Business Hours:** {{ support.business_hours }}
- **Extended Hours:** {{ support.extended_hours }}
- **Maintenance Window:** {{ support.maintenance_window }}

### 8.2 Support Channels

<!-- 
INSTRUCTIONS: Support Channels
- List all available support channels
- Examples: Phone, email, ticketing system, chat, self-service portal
-->

| Channel | Availability | Usage |
|---------|--------------|-------|
| Phone | Business Hours | Critical incidents (P1, P2) |
| Email | 24/7 | All priorities |
| Self-Service Portal | 24/7 | Requests, documentation |
| Chat | Business Hours | Quick inquiries |

### 8.3 Escalation Path

| Level | Role | Contact | Escalation Criteria |
|-------|------|---------|---------------------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} | First point of contact |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} | After 30 min without resolution (P1) |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} | After 1 hour without resolution (P1) |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} | Business-critical escalation |

### 8.4 Incident Classification

<!-- 
INSTRUCTIONS: Incident Classification
- Adapt the classification to your service
- Define clear criteria for each priority
- Examples for P1: "Complete outage", "Data loss", "Security incident"
-->

**P1 - Critical:**
- Complete service outage
- Data loss
- Security incident

**P2 - High:**
- Partial outage with workaround
- Performance issues
- Multiple users affected

**P3 - Medium:**
- Individual users affected
- Limited functionality
- Non-critical errors

**P4 - Low:**
- Information requests
- Feature requests
- Documentation questions

---

## 9. Operating Hours and Availability

<!-- 
INSTRUCTIONS: Operating Hours
- Define service hours and support hours
- Planned maintenance: Frequency, window, announcement period
-->

### 9.1 Service Hours

**Production Operation:** 24/7  
**Support:** {{ support.business_hours }}

### 9.2 Planned Maintenance

- **Frequency:** Monthly
- **Window:** {{ support.maintenance_window }}
- **Announcement:** At least 5 business days in advance
- **Duration:** Maximum 4 hours

### 9.3 Emergency Maintenance

For critical security updates or emergencies, unscheduled maintenance may be performed with shortened announcement period.

---

## 10. Monitoring and Reporting

<!-- 
INSTRUCTIONS: Monitoring
- Monitoring tool is loaded from meta-service.yaml
- Define monitored metrics
- Alerting rules: When is who notified how?
-->

### 10.1 Monitoring Strategy

**Monitoring Tool:** {{ meta-service.technology.monitoring }}

#### Monitored Metrics
- **Availability:** Uptime monitoring of all components
- **Performance:** Response times, throughput, resource utilization
- **Capacity:** CPU, RAM, disk, network
- **Errors:** Error rates, failed transactions

#### Alerting
- **P1 Alerts:** Immediate notification via SMS and email
- **P2 Alerts:** Email notification within 15 minutes
- **P3 Alerts:** Email notification within 1 hour

### 10.2 Reporting

<!-- 
INSTRUCTIONS: Reporting
- Define reporting frequency and content
- Operational reports: For IT teams (daily/weekly)
- Management reports: For executives (monthly/quarterly)
-->

#### Operational Reports
- **Daily:** Incident overview, performance metrics
- **Weekly:** Trend analysis, capacity planning

#### Management Reports
- **Monthly:** SLA compliance, service performance, costs
- **Quarterly:** Service review, improvement measures

### 10.3 Dashboards

- **Operations Dashboard:** Real-time overview for support teams
- **Management Dashboard:** KPIs and trends for service owner
- **User Dashboard:** Service status and announcements

---

## 11. Backup and Disaster Recovery

<!-- 
INSTRUCTIONS: Backup and DR
- Backup solution is loaded from meta-service.yaml
- RTO (Recovery Time Objective): How quickly must the service be restored?
- RPO (Recovery Point Objective): How much data loss is acceptable?
- Typical values: RTO 4h, RPO 24h (Standard), RTO 1h, RPO 1h (Critical)
-->

### 11.1 Backup Strategy

**Backup Solution:** {{ meta-service.technology.backup }}

- **Frequency:** Daily (incremental), Weekly (full)
- **Retention:** 30 days online, 1 year archived
- **Location:** Primary: On-site, Secondary: Off-site

### 11.2 Recovery Objectives

- **RTO (Recovery Time Objective):** {{ meta-service.recovery.rto }}
- **RPO (Recovery Point Objective):** {{ meta-service.recovery.rpo }}

### 11.3 Disaster Recovery Plan

<!-- 
INSTRUCTIONS: DR Plan
- Describe the steps for recovery
- Define responsibilities
- Test the DR plan regularly
-->

1. **Incident Detection:** Monitoring alerts, user reports
2. **Assessment:** Scope of damage and impact
3. **Activation:** Activate DR plan, inform teams
4. **Recovery:** Restore systems, recover data
5. **Validation:** Check functionality, perform tests
6. **Communication:** Inform stakeholders

---

## 12. Security and Compliance

<!-- 
INSTRUCTIONS: Security
- Describe implemented security measures
- List relevant compliance standards
- Data protection: Consider GDPR requirements
-->

### 12.1 Security Measures

- **Access Control:** Role-based permissions (RBAC)
- **Authentication:** Multi-factor authentication (MFA)
- **Encryption:** TLS 1.3 for data in transit, AES-256 for data at rest
- **Logging:** Comprehensive audit logs for all access

### 12.2 Compliance Requirements

**Relevant Standards:**
- ISO 27001: Information Security Management
- {{ meta-global-service.compliance.cobit_version }}: IT Governance
- {{ meta-global-service.compliance.itil_version }}: Service Management

### 12.3 Data Protection

- **GDPR Compliance:** Privacy by design and by default
- **Data Classification:** [Classification level]
- **Retention Periods:** According to legal requirements

---

## 13. Change Management

<!-- 
INSTRUCTIONS: Change Management
- Describe the change process for this service
- Change categories: Standard (approved), Normal (CAB), Emergency (immediate)
-->

### 13.1 Change Process

All changes to the service follow the established change management process:

1. **Request for Change (RFC):** Submission via service portal
2. **Assessment:** Impact and risk analysis
3. **Approval:** Change Advisory Board (CAB)
4. **Planning:** Detailed implementation planning
5. **Implementation:** Execution during maintenance window
6. **Review:** Post-implementation review

### 13.2 Change Categories

| Category | Approval | Lead Time |
|----------|----------|-----------|
| Standard | Service Manager | 2 business days |
| Normal | CAB | 5 business days |
| Emergency | Emergency CAB | Immediate |

---

## 14. Continual Service Improvement

<!-- 
INSTRUCTIONS: Continual Service Improvement
- Define service review process
- KPIs are partially loaded from meta-service.yaml
- Improvement measures: Prioritize and track
-->

### 14.1 Service Review Process

- **Frequency:** Quarterly
- **Participants:** Service Owner, Service Manager, Key Stakeholders
- **Agenda:** SLA review, incident analysis, improvement suggestions

### 14.2 KPIs and Metrics

| KPI | Target Value | Measurement Frequency |
|-----|--------------|----------------------|
| Service Availability | {{ meta-service.sla.availability_target }} | Monthly |
| MTTR (Mean Time To Repair) | < 2 hours | Monthly |
| MTBF (Mean Time Between Failures) | > 720 hours | Monthly |
| First Call Resolution Rate | > 70% | Monthly |
| Customer Satisfaction | > 4.0/5.0 | Quarterly |

### 14.3 Improvement Measures

<!-- 
INSTRUCTIONS: Improvement Measures
- List identified improvements
- Prioritize by impact and effort
- Track progress
-->

Identified improvement measures are prioritized and included in the service roadmap:

1. [Improvement measure 1]
2. [Improvement measure 2]
3. [Improvement measure 3]

---

## 15. Costs and Chargeback

<!-- 
INSTRUCTIONS: Costs
- Describe the cost structure
- Chargeback: How are costs allocated to users/departments?
- Examples: Flat rate, usage-based, cost center
-->

### 15.1 Cost Structure

- **Fixed Costs:** Infrastructure, licenses, personnel
- **Variable Costs:** Usage-dependent costs
- **One-time Costs:** Projects, migrations

### 15.2 Chargeback

[Description of chargeback model]

---

## 16. Appendices

<!-- 
INSTRUCTIONS: Appendices
- Link to relevant documents
- Runbooks: Step-by-step instructions for common tasks
- Checklists: For maintenance, deployment, troubleshooting
-->

### 16.1 Runbooks

- [Link to runbook 1]: Description
- [Link to runbook 2]: Description

### 16.2 Checklists

- [Link to checklist 1]: Description
- [Link to checklist 2]: Description

### 16.3 Additional Documentation

- Technical documentation: [Link]
- User manual: [Link]
- FAQ: [Link]

---

## 17. Contact Information

### 17.1 Organization

- **Name:** {{ meta-organisation.name }}
- **Address:** {{ meta-organisation.address }}
- **Phone:** {{ meta-organisation.phone }}
- **Web:** {{ meta-organisation.web }}

### 17.2 Service Contacts

- **Service Desk:** {{ escalation.level_1 }} ({{ escalation.level_1_email }})
- **Service Manager:** {{ meta-service.manager }} ({{ meta-service.manager_email }})
- **Service Owner:** {{ meta-service.owner }} ({{ meta-service.owner_email }})

---

## Document History

<!-- 
INSTRUCTIONS: Document History
- Maintain the version history
- Document significant changes
- Add new rows for each version
-->

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 19.02.2026 | Handbook Generator | Initial version |
| [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

---
