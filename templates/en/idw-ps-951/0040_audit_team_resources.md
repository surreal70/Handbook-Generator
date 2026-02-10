# Audit Team and Resources

**Document-ID:** idw-ps-951-0040  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Classification:** {{ meta.classification }}  
**Last Update:** {{ meta.date }}

---

## 1. Purpose

This document describes the composition of the audit team, required qualifications, and resource planning for the IT audit according to IDW PS 951.

## 2. Audit Team

### Team Structure

#### Audit Leadership
- **Name:** {{ source.audit_lead_name }}
- **Role:** Audit Lead
- **Qualification:** {{ source.audit_lead_qualification }}
- **Experience:** {{ source.audit_lead_experience }}
- **Contact:** {{ source.audit_lead_contact }}

#### IT Auditors

| Name | Role | Qualification | Specialization | Availability |
|------|------|---------------|----------------|--------------|
| {{ source.auditor_1_name }} | Senior IT Auditor | {{ source.auditor_1_qual }} | {{ source.auditor_1_spec }} | {{ source.auditor_1_avail }} |
| {{ source.auditor_2_name }} | IT Auditor | {{ source.auditor_2_qual }} | {{ source.auditor_2_spec }} | {{ source.auditor_2_avail }} |
| {{ source.auditor_3_name }} | IT Auditor | {{ source.auditor_3_qual }} | {{ source.auditor_3_spec }} | {{ source.auditor_3_avail }} |

#### Subject Matter Experts
- **Data Protection:** {{ source.privacy_expert }}
- **IT Security:** {{ source.security_expert }}
- **Application Systems:** {{ source.application_expert }}

## 3. Qualification Requirements

### Required Certifications
- CISA (Certified Information Systems Auditor)
- CISM (Certified Information Security Manager)
- CISSP (Certified Information Systems Security Professional)
- ISO 27001 Lead Auditor
- {{ source.additional_certifications }}

### Technical Knowledge
- IT auditing according to IDW PS 951
- IT governance and IT risk management
- IT security and data protection
- Application systems and databases
- IT processes (ITIL, COBIT)

### Industry Knowledge
- {{ source.industry_knowledge }}

## 4. Resource Planning

### Time Budget

| Audit Phase | Audit Lead | Senior Auditor | Auditor | Experts | Total |
|-------------|------------|----------------|---------|---------|-------|
| Planning | {{ source.planning_lead_hours }} | {{ source.planning_senior_hours }} | {{ source.planning_auditor_hours }} | {{ source.planning_expert_hours }} | {{ source.planning_total_hours }} |
| Execution | {{ source.execution_lead_hours }} | {{ source.execution_senior_hours }} | {{ source.execution_auditor_hours }} | {{ source.execution_expert_hours }} | {{ source.execution_total_hours }} |
| Reporting | {{ source.reporting_lead_hours }} | {{ source.reporting_senior_hours }} | {{ source.reporting_auditor_hours }} | {{ source.reporting_expert_hours }} | {{ source.reporting_total_hours }} |
| **Total** | {{ source.total_lead_hours }} | {{ source.total_senior_hours }} | {{ source.total_auditor_hours }} | {{ source.total_expert_hours }} | {{ source.total_hours }} |

### Resource Allocation by Audit Area

| Audit Area | Hours | Auditors | Priority |
|------------|-------|----------|----------|
| IT Strategy and Organization | {{ source.strategy_hours }} | {{ source.strategy_auditors }} | {{ source.strategy_priority }} |
| IT Processes | {{ source.process_hours }} | {{ source.process_auditors }} | {{ source.process_priority }} |
| IT Systems | {{ source.systems_hours }} | {{ source.systems_auditors }} | {{ source.systems_priority }} |
| IT Security | {{ source.security_hours }} | {{ source.security_auditors }} | {{ source.security_priority }} |
| Data Protection | {{ source.privacy_hours }} | {{ source.privacy_auditors }} | {{ source.privacy_priority }} |

## 5. Roles and Responsibilities

### RACI Matrix

| Activity | Audit Lead | Senior Auditor | Auditor | Experts |
|----------|------------|----------------|---------|---------|
| Audit Planning | A/R | C | I | C |
| Risk Analysis | A | R | C | C |
| Control Tests | A | R | R | C |
| Document Review | A | R | R | I |
| Interviews | A | R | R | C |
| Report Creation | A/R | C | C | I |
| Quality Assurance | A/R | C | I | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### Responsibilities

#### Audit Lead
- Overall responsibility for the audit
- Audit planning and control
- Communication with management
- Report approval

#### Senior IT Auditor
- Execution of complex audit procedures
- Supervision of auditors
- Quality assurance
- Technical consulting

#### IT Auditor
- Execution of audit procedures
- Documentation of audit results
- Control tests
- Data analysis

#### Subject Matter Experts
- Specialized consulting
- Assessment of complex issues
- Support with technical questions

## 6. Independence and Objectivity

### Independence Declarations
All team members have submitted independence declarations:
- No financial interests
- No personal relationships
- No conflicts of interest

### Rotation
- {{ source.rotation_policy }}

## 7. Training and Development

### Required Training
- IDW PS 951 updates
- New IT technologies
- Industry-specific topics
- {{ source.required_training }}

### Training Plan
| Team Member | Training | Date | Status |
|-------------|----------|------|--------|
| {{ source.training_1_member }} | {{ source.training_1_topic }} | {{ source.training_1_date }} | {{ source.training_1_status }} |

## 8. External Resources

### External Experts
External experts will be engaged as needed:
- {{ source.external_expert_1 }}
- {{ source.external_expert_2 }}

### Rationale
{{ source.external_expert_rationale }}

## 9. Communication and Coordination

### Team Meetings
- **Frequency:** {{ source.meeting_frequency }}
- **Format:** {{ source.meeting_format }}
- **Participants:** Entire audit team

### Status Reports
- **To:** Audit Lead
- **Frequency:** {{ source.status_report_frequency }}
- **Format:** {{ source.status_report_format }}

## 10. References

- IDW PS 951 - Qualification Requirements
- Audit Engagement Letter
- Resource Plan
- Independence Declarations

---

**Approved by:**  
{{ meta.audit_lead }}, Audit Lead  
Date: {{ meta.approval_date }}

**Next Review:** {{ meta.next_review }}

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initial creation |
