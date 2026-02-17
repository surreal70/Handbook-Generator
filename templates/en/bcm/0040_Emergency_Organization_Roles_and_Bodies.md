# Emergency Organization: Roles and Bodies

**Document-ID:** [FRAMEWORK]-0040
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the emergency organization structure, roles, and responsibilities.
It aligns with ISO 22301:2019 Clause 5.3 (Organizational roles, responsibilities and authorities).

Customization required:
- Define crisis management team structure
- Assign specific individuals to roles
- Establish clear RACI matrices
- Define escalation paths and decision authorities
-->

## 1. Organizational Model

### 1.1 Emergency Organization Structure

The emergency organization of {{ meta-organisation.name }} consists of the following levels:

```
┌─────────────────────────────────────┐
│      Crisis Team (Strategic)        │
│   Lead: {{ meta-organisation-roles.role_CEO }}   │
└──────────────┬──────────────────────┘
               │
    ┌──────────┴──────────┬────────────────┐
    │                     │                │
┌───▼────────┐  ┌────────▼─────┐  ┌──────▼──────┐
│ BCM Manager│  │ IT-DR Team   │  │ Department  │
│            │  │              │  │ BCP Teams   │
└────────────┘  └──────────────┘  └─────────────┘
```

**Level 1: Crisis Team (Strategic Level)**
- Strategic decisions and overall coordination
- Activation during severe incidents
- Communication with external stakeholders

**Level 2: BCM Manager / Coordination (Tactical Level)**
- Operational coordination of BCM measures
- Interface between crisis team and operational teams
- Documentation and reporting

**Level 3: Operational Teams (Operational Level)**
- IT-DR Team: IT systems recovery
- Department BCP Teams: Business process recovery
- Support Teams: Logistics, communication, HR

### 1.2 Organization Chart

[TODO: Insert detailed organization chart]

**Reference:** See `diagrams/bcm_organization.png`

## 2. Role Descriptions

### 2.1 Crisis Team Lead

**Role:** Crisis Team Lead / Crisis Management Team Lead

**Responsible:** {{ meta-organisation-roles.role_CEO }}  
**Deputy:** [TODO]  
**Contact:** {{ meta-organisation-roles.role_CEO }} / [TODO]

**Tasks:**
- Overall responsibility for crisis management and BCM activation
- Strategic decisions on resource deployment and prioritization
- Approval of communication to external stakeholders
- Decision on activation of alternate sites
- Approval of extraordinary measures and budgets

**Decision Authority:**
- Activation and deactivation of crisis team
- Approval of emergency budgets up to [TODO: Amount]
- Decision on business continuation or cessation
- Approval of emergency access (break-glass)

**Reporting Obligations:**
- To supervisory board / shareholders during severe crises
- To regulatory authorities according to regulatory requirements

### 2.2 BCM Manager / BCM Coordinator

**Role:** BCM Manager / Business Continuity Coordinator

**Responsible:** [TODO: BCM Manager Name]  
**Deputy:** [TODO: Deputy]  
**Contact:** [TODO: Email / Phone]

**Tasks:**
- Operational management of BCMS in normal operations
- Coordination of BIA, risk analysis, and BCM planning
- Organization and execution of BCM exercises and tests
- Maintenance of BCM documentation and contact lists
- Training and awareness of employees
- Reporting to management and crisis team

**Reporting:**
- Quarterly BCM status reports to {{ meta-organisation-roles.role_CEO }}
- Ad-hoc reporting for critical events
- Annual BCM report

**Interfaces:**
- ISMS / CISO: {{ meta-organisation-roles.role_CISO }}
- IT Operations: {{ meta-organisation-roles.role_IT_Manager }}
- Departments: Respective department heads

### 2.3 Incident Commander / Operational Lead

**Role:** Incident Commander / Operational Lead

**Responsible:** [TODO: Incident Commander Name]  
**Deputy:** [TODO: Deputy]  
**Contact:** [TODO: Email / Phone]

**Tasks:**
- Operational management of emergency measures on-site
- Coordination of operational teams (IT-DR, BCP teams)
- Situation assessment and status reporting to crisis team
- Implementation of measures decided by crisis team
- Documentation of all measures and decisions

**Interface to ITSM/Incident:**
- Takeover of major incidents from ITSM process
- Escalation to crisis team when defined thresholds exceeded
- Return to ITSM process after stabilization

**Decision Authority:**
- Operational measures without budget overrun
- Prioritization of recovery measures
- Request for additional resources

### 2.4 Communication / Spokesperson Role

**Role:** Crisis Communication / Spokesperson

**Responsible:** [TODO: Communications Manager]  
**Deputy:** [TODO: Deputy]  
**Contact:** [TODO: Email / Phone]

**Tasks:**
- Internal crisis communication (employees, management)
- External crisis communication (media, customers, partners, authorities)
- Creation and approval of press releases
- Social media monitoring and response
- Stakeholder management

**Approval Processes:**
- Internal communication: Approval by crisis team lead
- External communication: Approval by {{ meta-organisation-roles.role_CEO }}
- Press releases: Approval by management and legal department if applicable

**Communication Channels:**
- Internal: Email, intranet, employee app, phone
- External: Website, social media, press releases, customer hotline

### 2.5 IT-DR Lead

**Role:** IT Disaster Recovery Lead

**Responsible:** {{ meta-organisation-roles.role_IT_Manager }}  
**Deputy:** [TODO: Deputy]  
**Contact:** {{ meta-organisation-roles.role_IT_Manager }} / [TODO]

**Tasks:**
- Leadership of IT-DR team
- Coordination of IT recovery measures
- Implementation of IT disaster recovery plans
- Prioritization of system recovery according to BIA
- Status reporting to incident commander and crisis team

**Runbooks and Recovery Coordination:**
- Management and maintenance of IT-DR runbooks
- Coordination of system recovery in defined sequence
- Execution of restore tests
- Documentation of recovery measures

**Interfaces:**
- IT operations team
- External IT service providers and cloud providers
- Departments (for system approvals)

## 3. RACI Matrix Crisis Management

| Activity | Crisis Team Lead | BCM Manager | Incident Commander | IT-DR Lead | Department | Communication |
|----------|------------------|-------------|-------------------|------------|------------|---------------|
| Activate crisis | **A** | R | C | I | I | I |
| Situation assessment | C | C | **A/R** | C | C | I |
| Strategic decisions | **A** | C | C | I | C | C |
| Operational measures | I | C | **A** | R | R | I |
| IT recovery | I | C | C | **A/R** | C | I |
| BCP implementation | I | C | C | C | **A/R** | I |
| Internal communication | A | C | C | I | I | **R** |
| External communication | **A** | C | I | I | I | **R** |
| Documentation | I | **A** | R | R | R | R |
| End crisis | **A** | R | C | C | C | I |

**Legend:**
- **R** = Responsible (execution responsibility)
- **A** = Accountable (overall responsibility, decision authority)
- **C** = Consulted (consulted, subject matter expertise)
- **I** = Informed (informed)

## 4. Availability and On-Call

### 4.1 On-Call Models

[TODO: Define on-call models for critical roles]

**Example:**

**Crisis Team:**
- **Availability:** 24/7 via mobile phone
- **Response time:** Ready within 2 hours
- **On-call schedule:** Rotating model, quarterly updates

**IT-DR Team:**
- **Availability:** 24/7 on-call
- **Response time:** Ready within 1 hour
- **On-call schedule:** Weekly rotation

**BCM Manager:**
- **Availability:** Business days 08:00-18:00, outside via mobile phone
- **Response time:** Ready within 4 hours

### 4.2 Escalation Times

| Severity | Response Time | Escalate to | Escalation Time |
|----------|---------------|-------------|-----------------|
| **Low** | 4 hours | IT Operations | - |
| **Medium** | 2 hours | Incident Commander | After 4 hours |
| **High** | 1 hour | Crisis Team | After 2 hours |
| **Critical** | Immediate | Crisis Team Lead | Immediate |

### 4.3 Alerting Process

[TODO: Describe the alerting process]

**Example:**
1. **Initial detection:** Incident detected (monitoring, report, etc.)
2. **Initial assessment:** IT operations assesses severity
3. **Alerting:** For major incident → Alert incident commander
4. **Escalation:** For BCM activation → Alert crisis team
5. **Confirmation:** All alerted persons confirm receipt

**Alerting Channels:**
- Primary: Phone (mobile phone)
- Secondary: SMS / Messenger
- Tertiary: Email

## 5. Substitution Rules

### 5.1 Deputy Lists

Deputies are defined for all critical roles:

| Role | Primary | Deputy 1 | Deputy 2 |
|------|---------|----------|----------|
| Crisis Team Lead | {{ meta-organisation-roles.role_CEO }} | [TODO] | [TODO] |
| BCM Manager | [TODO] | [TODO] | [TODO] |
| Incident Commander | [TODO] | [TODO] | [TODO] |
| IT-DR Lead | {{ meta-organisation-roles.role_IT_Manager }} | [TODO] | [TODO] |
| Communication | [TODO] | [TODO] | [TODO] |

### 5.2 Handover Process

During substitution or shift change, a structured handover occurs:

**Handover Contents:**
- Current situation status
- Ongoing measures and their status
- Open decisions and escalations
- Critical information and contacts

**Handover Documentation:**
- Handover protocol (Template: [TODO: Link])
- Logbook entry
- Briefing of successor

<!-- End of template -->
