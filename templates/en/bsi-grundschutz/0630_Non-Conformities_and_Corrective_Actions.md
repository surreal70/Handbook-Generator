# Non-Conformities and Corrective Actions

**Document ID:** 0630  
**Document Type:** Process/Template  
**Reference Framework:** BSI IT-Grundschutz (BSI Standards 200-1/200-2)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Classification:** {{ meta.document.classification }}  
**Last Updated:** {{ meta.document.last_updated }}  
**Next Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the process for handling non-conformities and corrective actions.
Reference: BSI Standard 200-1 (Non-conformities and Corrective Actions)
-->

## 1. Purpose and Objectives

This process ensures that deviations from ISMS requirements are systematically captured, addressed, and their effectiveness verified.

**Responsible:** {{ meta.ciso.name }} (CISO)

## 2. Sources for Non-Conformities

**Non-conformities can be identified through:**
- Internal Audits (Document 0610)
- Basic Security Check (Document 0080)
- Security Incidents (Document 0320/0330)
- Penetration Tests and Vulnerability Scans
- Policy Violations
- Management Review (Document 0620)
- External Audits

## 3. Process

### 3.1 Capture

**Step 1: Identification and Documentation**
- Non-conformity is identified
- Finding is recorded in the Findings Register (see Section 4)
- Categorization: Critical/High/Medium/Low

**Responsible:** Identifying person (Auditor, CISO, etc.)

### 3.2 Root Cause Analysis

**Step 2: Root Cause Analysis**
- Why did the non-conformity occur?
- Which processes/controls failed?
- Is this an isolated case or systemic problem?

**Methods:**
- 5-Why Analysis
- Fishbone Diagram
- Process Analysis

**Responsible:** CISO, affected area manager

### 3.3 Define Action

**Step 3: Define Corrective Action**
- Immediate action (fix symptom)
- Corrective action (fix cause)
- Preventive action (prevent recurrence)

**Responsible:** CISO, Action Owner

### 3.4 Implementation

**Step 4: Implement Action**
- Action is implemented
- Progress is tracked
- Implementation documentation

**Responsible:** Action Owner

### 3.5 Effectiveness Check

**Step 5: Effectiveness Check**
- Was the non-conformity resolved?
- Is the cause eliminated?
- Have no new problems emerged?

**Methods:**
- Follow-up Audit
- Sampling
- KPI Monitoring

**Responsible:** CISO, Internal Audit

### 3.6 Closure

**Step 6: Closure**
- Effectiveness confirmed
- Finding closed
- Lessons Learned documented

**Responsible:** CISO

## 4. Findings Register

| Finding ID | Source | Date | Description | Category | Root Cause | Action | Owner | Due | Status | Effectiveness Verified On |
|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | Audit Q1 | [TODO] | [TODO] | High | [TODO] | [TODO] | [TODO] | [TODO] | Open | - |
| F-002 | Basic Check | [TODO] | [TODO] | Medium | [TODO] | [TODO] | [TODO] | [TODO] | In Progress | - |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Status Values:**
- **Open:** Newly identified
- **In Analysis:** Root cause analysis ongoing
- **In Progress:** Action being implemented
- **Effectiveness Check:** Action implemented, verification pending
- **Closed:** Effectiveness confirmed

## 5. Categorization and Response Times

| Category | Description | Response Time | Escalation |
|---|---|---|---|
| **Critical** | Severe deviation, high risk | Immediately | Executive Management |
| **High** | Significant deviation | 7 days | CISO |
| **Medium** | Improvement potential | 30 days | Area Manager |
| **Low** | Minor deviation | 90 days | Area Manager |

## 6. Reporting

**Monthly:**
- Number of open findings (by category)
- Overdue findings
- Closed findings

**Quarterly:**
- Trend analysis
- Top finding categories
- Effectiveness of corrective actions

**Responsible:** {{ meta.ciso.name }}  
**Recipients:** Executive Management, ISMS Team

## 7. Lessons Learned

After closing critical or recurring findings:
1. **Retrospective:** What went well? What didn't?
2. **Process Improvement:** Adjustment of processes/controls
3. **Documentation:** Document lessons learned
4. **Communication:** Share insights (Awareness)

## 8. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| CISO | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT Management | {{ meta.cio.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**References:**
- BSI Standard 200-1: ISMS (Non-conformities and Corrective Actions)
- Document 0610: Internal Audit Program

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |

<!-- End of template -->