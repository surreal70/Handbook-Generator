# Internal Audit Program (Template)

**Document ID:** 0610  
**Document Type:** Program/Template  
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
This template defines the internal audit program for ISMS.
Reference: BSI Standard 200-1 (Internal Audits), DER.3.1
-->

## 1. Purpose and Objectives

The internal audit program of **{{ meta.organization.name }}** ensures the effectiveness of the ISMS.

**Responsible:** [TODO: Internal Audit]

## 2. Audit Approach

**Principles:**
- **Risk-based:** Focus on critical areas
- **Independent:** Auditors are independent from audited area
- **Scope-related:** Audits cover the entire ISMS scope
- **Systematic:** Structured audit process

## 3. Audit Plan

| Period | Audit Topic | Criteria | Auditor | Auditee | Status | Result | Actions |
|---|---|---|---|---|---|---|---|
| Q1 {{ meta.document.year }} | Basic Security Check Sample | Policies, Guidelines, Evidence | [TODO] | {{ meta.cio.name }} | Planned | - | - |
| Q2 {{ meta.document.year }} | Risk Management Process | Document 0090, Risk Register | [TODO] | {{ meta.ciso.name }} | Planned | - | - |
| Q3 {{ meta.document.year }} | Incident Management | Document 0320/0330, Incident Logs | [TODO] | {{ meta.cio.name }} | Planned | - | - |
| Q4 {{ meta.document.year }} | Document Control | Document 0030, Document Register | [TODO] | {{ meta.ciso.name }} | Planned | - | - |

## 4. Audit Checkpoints

**Standard Checks:**
- Are documents current and approved?
- Is evidence available and traceable?
- Is the action status plausible?
- Are deviations documented and addressed?
- Are processes lived (not just documented)?

## 5. Audit Process

1. **Planning:** Audit scope, criteria, schedule
2. **Preparation:** Document review, checklists
3. **Execution:** Interviews, sampling, inspections
4. **Reporting:** Audit report with findings
5. **Follow-up:** Tracking of corrective actions

## 6. Audit Report Template

**Structure:**
1. Executive Summary
2. Audit Scope and Criteria
3. Audit Methodology
4. Findings (Categorized: Critical/High/Medium/Low)
5. Positive Observations
6. Recommendations
7. Action Plan

## 7. Findings Categorization

| Category | Description | Response Time |
|---|---|---|
| **Critical** | Severe deviation, high risk | Immediately |
| **High** | Significant deviation | 30 days |
| **Medium** | Improvement potential | 90 days |
| **Low** | Minor deviation | 180 days |

## 8. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| Internal Audit | [TODO] | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| CISO | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**References:**
- BSI Standard 200-1: ISMS
- BSI IT-Grundschutz-Kompendium: DER.3.1 Audits and Reviews

<!-- End of template -->
