# Internal Audit Program (Template)

**Document-ID:** [FRAMEWORK]-0130
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



**Document ID:** 0130  
**Document Type:** ISMS Program/Template  
**Standard Reference:** ISO/IEC 27001:2022 Clause 9.2  
**Owner:** {{ meta-handbook.audit_manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Confidential  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose and Scope

### 1.1 Purpose

The internal audit program of **AdminSend GmbH** ensures that:
- The ISMS complies with ISO 27001:2022 requirements
- The ISMS is effectively implemented and maintained
- Improvement opportunities are identified
- Compliance with policies and guidelines is ensured

### 1.2 Scope

The audit program encompasses:
- All areas within the ISMS scope (see `0020_ISMS_Scope.md`)
- All Annex A controls in the SoA (see `0100_ISMS_Statement_of_Applicability_SoA_Template.md`)
- All ISMS processes and documents
- All locations: [[ netbox.site.name ]] and others

## 2. Audit Approach

### 2.1 Audit Principles

**Independence:**
- Auditors do not audit their own areas
- External auditors for critical areas (optional)
- Reporting line: Audit team reports to {{ meta-handbook.audit_manager }}

**Risk-Based:**
- Audit frequency based on risk assessment
- Critical areas audited more frequently
- Focus on high risks and critical controls

**Scope-Based:**
- All areas within ISMS scope are audited
- Complete coverage within audit cycle (3 years)

**Objective and Evidence-Based:**
- Audit findings based on objective evidence
- Sample-based testing
- Documentation of all findings

### 2.2 Audit Types

**Complete ISMS Audit:**
- Frequency: Annually
- Scope: Entire ISMS
- Duration: 5-10 days

**Topic Audits:**
- Frequency: Quarterly
- Scope: Specific topics (e.g., access management, patch management)
- Duration: 1-2 days

**Follow-up Audits:**
- Frequency: As needed
- Scope: Verification of corrective action implementation
- Duration: 0.5-1 day

## 3. Annual Plan

### 3.1 Audit Annual Plan 2026

| Period | Audit Topic/Scope | Audit Type | Criteria | Auditor | Auditee | Planned Duration | Status |
|--------|-------------------|------------|----------|---------|---------|------------------|--------|
| **Q1 2026** | Access Management & IAM | Topic Audit | A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3 | [TODO] | [TODO] | 2 days | Planned |
| **Q2 2026** | Vulnerability & Patch Management | Topic Audit | A.8.8, A.5.23 | [TODO] | IT Operations | 1 day | Planned |
| **Q3 2026** | Complete ISMS Audit | Full Audit | All Clauses, SoA | [TODO] | [TODO] | 10 days | Planned |
| **Q4 2026** | Incident Management & Logging | Topic Audit | A.5.24, A.5.25, A.5.26, A.5.28, A.8.15, A.8.16 | [TODO] | Security Team | 2 days | Planned |

[TODO: Complete audit plan for 2026]

### 3.2 Audit Frequency by Risk

| Area | Risk Level | Audit Frequency |
|------|------------|-----------------|
| Privileged Access Management | High | Semi-annually |
| Vulnerability Management | High | Semi-annually |
| Incident Management | High | Semi-annually |
| Backup & Recovery | Medium | Annually |
| Physical Security | Medium | Annually |
| HR Security | Low | Every 2 years |

## 4. Audit Process

### 4.1 Audit Phases

```
1. Planning
   ├─ Define audit scope
   ├─ Appoint audit team
   ├─ Create audit plan
   └─ Inform auditee
   
2. Preparation
   ├─ Request documents
   ├─ Create audit checklist
   ├─ Define samples
   └─ Plan interviews
   
3. Execution
   ├─ Opening meeting
   ├─ Document review
   ├─ Interviews
   ├─ Sampling
   ├─ Observations
   └─ Closing meeting
   
4. Reporting
   ├─ Document findings
   ├─ Create audit report
   ├─ Report to auditee
   └─ Report to management
   
5. Follow-up
   ├─ Plan corrective actions
   ├─ Monitor implementation
   ├─ Follow-up audit
   └─ Close findings
```

### 4.2 Audit Checklist (Example)

**Audit Topic: Access Management**

| Check Point | Criterion | Evidence | Result | Remarks |
|-------------|-----------|----------|--------|---------|
| Are access rights documented? | Policy 0220 | IAM documentation | ✓ / ✗ | |
| Are access rights regularly recertified? | Guideline 0230 | Recertification protocols | ✓ / ✗ | |
| Is least privilege principle implemented? | A.8.2 | IAM configuration | ✓ / ✗ | |
| Are joiner/mover/leaver processes followed? | Guideline 0230 | HR tickets, IAM logs | ✓ / ✗ | |
| Is MFA enabled for all users? | A.5.17 | MFA configuration | ✓ / ✗ | |

[TODO: Create complete checklists for all audit topics]

### 4.3 Audit Criteria

**Document Review:**
- Are documents current and approved?
- Are documents complete and consistent?
- Are responsibilities defined?

**Evidence Review:**
- Is evidence available and current?
- Is evidence traceable?
- Is evidence sufficient for proof?

**Control Effectiveness:**
- Is the control implemented?
- Is the control effective (sampling)?
- Are there deviations or weaknesses?

**Compliance:**
- Are policies and guidelines followed?
- Are legal requirements met?
- Are contractual obligations met?

## 5. Audit Findings

### 5.1 Finding Categories

**Major Non-Conformity (Severe):**
- Significant violation of ISO 27001:2022
- Critical control not implemented
- Systemic failure
- **Example:** No risk analysis performed

**Minor Non-Conformity (Minor):**
- Minor violation of ISO 27001:2022
- Control partially implemented
- Isolated error
- **Example:** Documentation incomplete

**Observation:**
- Improvement potential
- Best practice not implemented
- No violation of requirements
- **Example:** Process could be more efficient

**Opportunity for Improvement:**
- Recommendation for improvement
- No deviation
- **Example:** Automation possible

### 5.2 Finding Documentation

**For each finding:**
- Finding ID (e.g., F-2026-Q1-001)
- Category (Major/Minor/Observation)
- Description
- Affected area/control
- Evidence
- Impact
- Recommended corrective action
- Responsible person
- Deadline

### 5.3 Corrective Actions

**Process:**
1. Auditee plans corrective action
2. CISO approves action and deadline
3. Auditee implements action
4. Auditor verifies implementation (follow-up)
5. Finding is closed

**Deadlines:**
- Major Non-Conformity: 30 days
- Minor Non-Conformity: 90 days
- Observation: 180 days

## 6. Audit Report

### 6.1 Report Structure

**Executive Summary:**
- Audit scope and objective
- Audit date and team
- Summary of results
- Overall assessment

**Audit Details:**
- Audit methodology
- Audited areas and controls
- Samples
- Interviews

**Findings:**
- List of all findings (by category)
- Detailed description of each finding
- Recommended corrective actions

**Positive Observations:**
- Best practices
- Well-implemented controls
- Improvements since last audit

**Conclusion:**
- Overall assessment of ISMS
- Recommendations
- Next steps

### 6.2 Report Distribution

**Recipients:**
- Auditee
- CISO
- Management
- Information security committee

**Confidentiality:**
- Audit reports are confidential
- Access only for authorized persons

## 7. Auditor Qualification

### 7.1 Auditor Requirements

**Technical Qualification:**
- Knowledge of ISO 27001:2022
- Knowledge of ISO 27002:2022
- Knowledge of audit methodology
- Industry knowledge

**Certifications (recommended):**
- ISO 27001 Lead Auditor
- CISA (Certified Information Systems Auditor)
- CISM (Certified Information Security Manager)

**Soft Skills:**
- Communication skills
- Objectivity
- Analytical thinking
- Documentation skills

### 7.2 Auditor Training

**Initial Training:**
- ISO 27001:2022 training
- Audit methodology training
- Shadowing experienced auditors

**Continuous Education:**
- Annual refresher
- Participation in auditor conferences
- Exchange with other auditors

## 8. Audit Metrics

### 8.1 KPIs

| Metric | Target Value | Current | Status |
|--------|--------------|---------|--------|
| Audit plan fulfillment | 100% | [TODO]% | [TODO] |
| Average time to remediate (Major) | < 30 days | [TODO] days | [TODO] |
| Average time to remediate (Minor) | < 90 days | [TODO] days | [TODO] |
| Number of open findings | < 5 | [TODO] | [TODO] |
| Recurring findings | 0 | [TODO] | [TODO] |

### 8.2 Trend Analysis

**Annual Review:**
- Number of findings per year (trend)
- Most common finding categories
- Areas with most findings
- Improvements since previous year

## 9. Roles and Responsibilities

### 9.1 RACI Matrix: Audit Process

| Activity | Audit Manager | Auditor | Auditee | CISO | Management |
|----------|---------------|---------|---------|------|------------|
| Create audit program | R/A | C | C | C | I |
| Plan audit | R | R | C | I | I |
| Conduct audit | A | R | C | I | I |
| Document findings | A | R | C | I | I |
| Create audit report | R/A | R | C | I | I |
| Plan corrective actions | C | C | R/A | C | I |
| Conduct follow-up | A | R | C | I | I |
| Review audit program | R/A | C | C | C | C |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 10. References

### 10.1 Internal Documents

- `0020_ISMS_Scope.md` - ISMS Scope
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA
- `0140_ISMS_Management_Review_Template.md` - Management Review
- `0150_ISMS_Non_Conformities_and_Corrective_Actions.md` - Non-conformities
- All Policies (0200-0680) and Guidelines (0210-0690)

### 10.2 External Standards

- **ISO/IEC 27001:2022** - Clause 9.2: Internal audit
- **ISO 19011:2018** - Guidelines for auditing management systems
- **ISO/IEC 27007:2020** - Guidelines for information security management systems auditing

**Approved by:**  
{{ meta-handbook.audit_manager }}, Audit Manager  
[TODO], CISO  
Date: [TODO]

**Next Review:** [TODO]

