# Non-Conformities and Corrective Actions

**Document-ID:** [FRAMEWORK]-0150
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

<!-- 
TEMPLATE AUTHOR NOTE:
This document defines the process for handling non-conformities and implementing
corrective actions. It ensures systematic treatment of deviations from requirements
and drives continuous improvement.

ISO 27001:2022 Reference: Clause 10.1 - Nonconformity and corrective action
-->

**Document ID:** 0150  
**Document Type:** ISMS Process/Template  
**Standard Reference:** ISO/IEC 27001:2022 Clause 10.1  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose and Objective

### 1.1 Purpose

This document defines the process for systematic treatment of non-conformities in the ISMS of **{{ meta-organisation.name }}**. It ensures that:
- Deviations from requirements are identified and documented
- Root causes are analyzed and addressed
- Corrective actions are effectively implemented
- Recurrence is prevented

### 1.2 Types of Non-Conformities

**Audit Findings:**
- Major non-conformities (severe)
- Minor non-conformities (minor)
- Observations

**Security Incidents:**
- Security incidents with root cause in process/control weaknesses

**Policy Violations:**
- Violations of ISMS policies and guidelines

**Compliance Violations:**
- Violations of legal or contractual requirements

## 2. Process

### 2.1 Process Overview

```
1. Capture
   ├─ Identify non-conformity
   ├─ Create ticket/finding
   └─ Categorize and prioritize
   
2. Root Cause Analysis
   ├─ Perform root cause analysis
   ├─ Identify contributing factors
   └─ Recognize systemic causes
   
3. Define Corrective Action
   ├─ Immediate action (containment)
   ├─ Corrective action
   └─ Preventive action
   
4. Implementation
   ├─ Implement action
   ├─ Track progress
   └─ Document
   
5. Effectiveness Verification
   ├─ Verify effectiveness
   ├─ Conduct follow-up
   └─ Document lessons learned
   
6. Closure
   ├─ Close finding
   ├─ Archive documentation
   └─ Communication
```

### 2.2 Step 1: Capture

**Identification:**
- Through audits (internal/external)
- Through security incidents
- Through monitoring and KPIs
- Through employee reports
- Through management reviews

**Documentation:**
- Assign finding ID (e.g., F-2026-001)
- Description of non-conformity
- Affected area/control
- Evidence
- Categorization (Major/Minor/Observation)
- Priority (High/Medium/Low)

**Responsible:** Auditor, ISMS Manager, or Reporter

### 2.3 Step 2: Root Cause Analysis

**Root Cause Analysis (RCA):**
- **5-Why Method:** Why did this happen? (ask 5 times)
- **Fishbone Diagram:** Cause categories (People, Process, Technology, Environment)
- **Fault Tree Analysis:** Logical analysis of failure causes

**To Identify:**
- Immediate cause
- Root cause
- Contributing factors
- Systemic causes

**Documentation:**
- RCA method
- Identified causes
- Contributing factors

**Responsible:** Finding owner, supported by ISMS Manager

### 2.4 Step 3: Define Corrective Action

**Immediate Action:**
- Containment of problem
- Damage limitation
- Temporary solution

**Corrective Action:**
- Address root cause
- Permanent solution
- Process/control improvement

**Preventive Action:**
- Prevent recurrence
- Prevent similar problems
- Systemic improvements

**Documentation:**
- Description of action
- Responsible person
- Deadline
- Resources/budget
- Success criteria

**Responsible:** Finding owner, approved by CISO

### 2.5 Step 4: Implementation

**Implementation:**
- Implement action according to plan
- Document progress
- Inform stakeholders

**Tracking:**
- Regular status updates
- Escalation for delays
- Adjustment for problems

**Documentation:**
- Implementation steps
- Deviations from plan
- Lessons learned

**Responsible:** Finding owner

### 2.6 Step 5: Effectiveness Verification

**Verification:**
- Is the action implemented?
- Is the non-conformity resolved?
- Is the root cause eliminated?

**Validation:**
- Is the action effective?
- Does the problem still occur?
- Are there unintended side effects?

**Methods:**
- Follow-up audit
- Sampling
- Monitoring
- Interviews

**Documentation:**
- Effectiveness verification performed on
- Method
- Result
- Evidence

**Responsible:** Auditor or ISMS Manager

### 2.7 Step 6: Closure

**Closure Criteria:**
- Action fully implemented
- Effectiveness demonstrated
- Documentation complete
- Lessons learned documented

**Closure Activities:**
- Set finding status to "Closed"
- Archive documentation
- Inform stakeholders
- Communicate lessons learned

**Responsible:** ISMS Manager

## 3. Non-Conformities Register

### 3.1 Active Non-Conformities

| Finding ID | Source | Category | Description | Root Cause | Corrective Action | Owner | Due | Status | Effectiveness Verified |
|------------|--------|----------|-------------|------------|-------------------|-------|-----|--------|----------------------|
| F-2026-001 | Audit | Minor | Documentation incomplete | Process not defined | Document process | [TODO] | 2026-03-31 | In Progress | - |
| F-2026-002 | Incident | Major | Unpatched vulnerability exploited | Patch process insufficient | Improve patch process | IT Operations | 2026-02-28 | In Progress | - |
| F-2026-003 | Monitoring | Observation | MFA activation < 100% | Awareness insufficient | MFA campaign | {{ meta-organisation-roles.role_CISO }} | 2026-04-30 | Planned | - |

[TODO: Add active non-conformities]

### 3.2 Closed Non-Conformities (Archive)

| Finding ID | Source | Category | Description | Corrective Action | Closure Date | Effectiveness Confirmed |
|------------|--------|----------|-------------|-------------------|--------------|------------------------|
| F-2025-050 | Audit | Minor | Backup tests not documented | Establish backup test process | 2026-01-15 | Yes |
| F-2025-051 | Incident | Major | Phishing incident | Security awareness training | 2026-01-20 | Yes |

[TODO: Archive closed non-conformities]

## 4. Prioritization and Deadlines

### 4.1 Prioritization

| Category | Priority | Deadline | Escalation |
|----------|----------|----------|------------|
| Major Non-Conformity | Very High | 30 days | Immediately to CISO and management |
| Minor Non-Conformity | High | 90 days | To CISO if delayed |
| Observation | Medium | 180 days | To ISMS Manager if delayed |
| Opportunity for Improvement | Low | As available | None |

### 4.2 Escalation

**Overdue Actions:**
- > 2 weeks overdue: Reminder to owner
- > 4 weeks overdue: Escalation to CISO
- > 8 weeks overdue: Escalation to management

**Critical Non-Conformities:**
- Major non-conformities: Immediate escalation
- Compliance violations: Immediate escalation
- Recurring non-conformities: Escalation to management

## 5. Root Cause Analysis Methods

### 5.1 5-Why Method

**Example:**
1. **Why** did the non-conformity occur? → Unpatched vulnerability was exploited
2. **Why** was the vulnerability unpatched? → Patch was not installed in time
3. **Why** was the patch not installed in time? → Patch process did not prioritize patch
4. **Why** did the process not prioritize the patch? → CVSS score was not considered
5. **Why** was CVSS score not considered? → Process only considers vendor severity

**Root Cause:** Patch prioritization not based on CVSS score

**Corrective Action:** Extend patch process with CVSS-based prioritization

### 5.2 Fishbone Diagram (Ishikawa)

**Categories:**
- **People:** Lack of training, errors, negligence
- **Process:** Insufficient processes, missing documentation
- **Technology:** Missing tools, misconfiguration, bugs
- **Environment:** Organizational factors, resource shortage

## 6. Effectiveness Verification

### 6.1 Methods

**Audit:**
- Follow-up audit
- Sample testing
- Document review

**Monitoring:**
- KPI tracking
- Incident tracking
- Compliance monitoring

**Testing:**
- Penetration tests
- Vulnerability scans
- Configuration audits

**Interviews:**
- Questioning affected persons
- Feedback collection

### 6.2 Success Criteria

**Action is effective when:**
- Non-conformity no longer occurs
- Root cause is eliminated
- KPIs have improved
- No new problems have emerged
- Stakeholders are satisfied

## 7. Lessons Learned

### 7.1 Documentation

**For each closed non-conformity:**
- What did we learn?
- What worked well?
- What could be improved?
- Which actions are transferable?

### 7.2 Communication

**Target Groups:**
- Affected teams
- ISMS committee
- Management
- All employees (for relevant lessons learned)

**Channels:**
- Lessons learned database
- Security newsletter
- Team meetings
- Awareness campaigns

## 8. Roles and Responsibilities

### 8.1 RACI Matrix: Non-Conformities Process

| Activity | CISO | ISMS Manager | Finding Owner | Auditor | Management |
|----------|------|--------------|---------------|---------|------------|
| Capture non-conformity | A | R | C | R | I |
| Root cause analysis | A | C | R | C | I |
| Define action | A | C | R | C | I |
| Approve action | A | C | I | I | C |
| Implement action | A | C | R | I | I |
| Verify effectiveness | A | R | C | R | I |
| Close finding | A | R | C | C | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 9. Metrics and Reporting

### 9.1 KPIs

| Metric | Target Value | Current | Status |
|--------|--------------|---------|--------|
| Open major findings | 0 | [TODO] | ✓ / ✗ |
| Open minor findings | < 5 | [TODO] | ✓ / ✗ |
| Average remediation time (Major) | < 30 days | [TODO] days | ✓ / ✗ |
| Average remediation time (Minor) | < 90 days | [TODO] days | ✓ / ✗ |
| Overdue findings | 0 | [TODO] | ✓ / ✗ |
| Recurring findings | 0 | [TODO] | ✓ / ✗ |

### 9.2 Reporting

**Monthly:**
- Status of all open findings
- Overdue findings
- Newly added findings

**Quarterly:**
- Trend analysis
- Most common causes
- Effectiveness of actions

**Annually:**
- Complete review in management review
- Lessons learned summary

## 10. References

### 10.1 Internal Documents

- `0130_ISMS_Internal_Audit_Program.md` - Internal Audit Program
- `0140_ISMS_Management_Review_Template.md` - Management Review
- `0160_ISMS_Continuous_Improvement.md` - Continuous Improvement
- `0400_Policy_Incident_Management.md` - Incident Management

### 10.2 External Standards

- **ISO/IEC 27001:2022** - Clause 10.1: Nonconformity and corrective action
- **ISO 9001:2015** - Clause 10.2: Nonconformity and corrective action
- **ISO 19011:2018** - Guidelines for auditing management systems

**Approved by:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }}

