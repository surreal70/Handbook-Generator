# Risk Treatment Plan (RTP) – Template

**Document-ID:** [FRAMEWORK]-0090
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
The Risk Treatment Plan (RTP) documents all planned measures to treat identified
risks. It tracks implementation progress, responsibilities, and deadlines. This
is the action plan that translates risk analysis into concrete security improvements.

ISO 27001:2022 Reference: Clause 6.1.3 - Information security risk treatment
-->

**Document ID:** 0090  
**Document Type:** ISMS Plan/Template  
**Standard Reference:** ISO/IEC 27001:2022 Clause 6.1.3  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Confidential  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose and Scope

### 1.1 Purpose

The Risk Treatment Plan (RTP) of **{{ meta-organisation.name }}** documents all planned measures for treating identified information security risks. It serves as:
- Action plan for risk treatment
- Tracking tool for measure implementation
- Evidence for audits and compliance
- Basis for resource planning and budgeting

### 1.2 Scope

This plan encompasses all measures for treating risks within the ISMS scope (see `0020_ISMS_Scope.md`) that are treated with the "Mitigate" or "Transfer" strategy.

**Excluded:**
- Accepted risks (see `0080_ISMS_Risk_Register_Template.md`)
- Avoided risks (activity discontinued)

## 2. Risk Treatment Plan Table

### 2.1 Active Measures

| Measure ID | Risk ID | Measure | Control Reference (Annex A) | Owner | Priority | Effort (PD) | Budget | Target Date | Status | Progress | Remarks |
|------------|---------|---------|----------------------------|-------|----------|-------------|--------|-------------|--------|----------|---------|
| M-001 | R-001 | Procure redundant core switch | A.8.6 (Capacity management) | {{ meta-organisation-roles.role_CIO }} | High | 20 | €50,000 | 2026-06-30 | Planned | 0% | Budget approved, tender in progress |
| M-002 | R-002 | Implement immutable backups | A.8.13 (Information backup) | IT Operations | Very High | 40 | €30,000 | 2026-03-31 | In Progress | 60% | Pilot phase completed |
| M-003 | R-003 | Roll out MFA for all users | A.5.17 (Authentication information) | IAM Team | Very High | 30 | €15,000 | 2026-02-28 | In Progress | 80% | 200 of 250 users migrated |
| M-004 | R-004 | Implement secret scanning tool | A.8.24 (Use of cryptography) | Dev Lead | Medium | 15 | €10,000 | 2026-04-30 | Planned | 10% | Tool evaluation: GitGuardian vs. Gitleaks |
| M-005 | R-005 | Perform VPN hardening | A.5.14 (Information transfer) | IT Operations | Medium | 10 | €5,000 | 2026-05-31 | Planned | 0% | Create hardening guide |

<!-- 
Add your organization's specific risk treatment measures. Each measure should
be linked to a risk in the risk register and an Annex A control where applicable.
-->

[TODO: Add additional measures based on risk register]

### 2.2 Completed Measures (Archive)

| Measure ID | Risk ID | Measure | Owner | Completion Date | Result | Evidence |
|------------|---------|---------|-------|-----------------|--------|----------|
| M-010 | R-020 | Install patch CVE-2025-1234 | IT Operations | 2026-01-10 | Successful | Vulnerability Scan Report |
| M-011 | R-021 | Correct firewall configuration | IT Operations | 2026-01-15 | Successful | Firewall Audit Report |

[TODO: Archive completed measures]

## 3. Measure Prioritization

### 3.1 Prioritization Criteria

**Priority Levels:**

| Priority | Risk Level | Compliance | Effort | Timeframe |
|----------|------------|------------|--------|-----------|
| **Very High** | Very High / High | Critical | Any | Immediate - 3 months |
| **High** | High / Medium | Important | Low-Medium | 3-6 months |
| **Medium** | Medium | Normal | Medium | 6-12 months |
| **Low** | Low | Optional | High | > 12 months |

**Prioritization Formula:**
```
Priority = (Risk Score × 2) + Compliance Factor - Effort Factor

Compliance Factor:
- Critical (GDPR, NIS2): +10
- Important (ISO 27001): +5
- Normal: +0

Effort Factor:
- Low (< 10 PD): -0
- Medium (10-40 PD): -5
- High (> 40 PD): -10
```

### 3.2 Quick Wins

**Quick Wins** are measures with high benefit and low effort:

| Measure ID | Measure | Risk Reduction | Effort | ROI |
|------------|---------|----------------|--------|-----|
| M-003 | MFA rollout | High | Medium | High |
| M-005 | VPN hardening | Medium | Low | Very High |

**Recommendation:** Quick wins should be prioritized to achieve rapid security improvements.

## 4. Measure Details

### 4.1 Measure Description

The following details should be documented for each measure:

**Measure M-002: Implement Immutable Backups**

**Description:**
Implementation of immutable backups to protect against ransomware. Backups are stored in Write-Once-Read-Many (WORM) format and cannot be deleted or modified.

**Objective:**
- Protection against ransomware attacks on backups
- Ensure recoverability in case of data loss
- Compliance with GDPR Art. 32 (Security of processing)

**Scope:**
- All production systems
- Critical databases
- Customer data (GDPR-relevant)

**Implementation Steps:**
1. Evaluate backup solution (Veeam, Commvault, AWS S3 Object Lock)
2. Pilot phase with non-critical systems (✓ Completed)
3. Rollout to production systems (In Progress)
4. Perform restore tests
5. Documentation and training

**Resources:**
- Owner: IT Operations
- Team: 2 Backup Administrators
- Effort: 40 person-days
- Budget: €30,000 (licenses + hardware)

**Dependencies:**
- No critical dependencies

**Implementation Risks:**
- Increased storage requirements (Mitigation: Additional storage procured)
- Longer backup times (Mitigation: Backup window adjusted)

**Success Criteria:**
- All critical systems have immutable backups
- Restore tests successful (RTO/RPO met)
- No ransomware can delete backups

**Evidence:**
- Backup configuration documentation
- Restore test protocols
- Compliance report

<!-- 
Create detailed descriptions for each major risk treatment measure. This helps
with implementation planning and provides evidence for audits.
-->

## 5. Control Mapping (Annex A)

### 5.1 Linkage to Annex A Controls

Each measure should be linked to relevant Annex A controls:

| Measure ID | Annex A Control | Control Name | Implementation Status |
|------------|-----------------|--------------|----------------------|
| M-001 | A.8.6 | Capacity management | Planned |
| M-002 | A.8.13 | Information backup | In Progress |
| M-003 | A.5.17 | Authentication information | In Progress |
| M-004 | A.8.24 | Use of cryptography | Planned |
| M-005 | A.5.14 | Information transfer | Planned |

**Complete Control Mapping:**
- See `0100_ISMS_Statement_of_Applicability_SoA_Template.md`
- See `0710_Appendix_AnnexA_Mapping_Template.md`

### 5.2 Control Implementation Status

**Status Definitions:**

| Status | Description | Criteria |
|--------|-------------|----------|
| **Not Implemented** | Control is not in place | 0% implementation |
| **Planned** | Control is planned but not yet started | Measure in RTP |
| **In Progress** | Control is being implemented | 1-99% implementation |
| **Implemented** | Control is fully implemented | 100% implementation, evidence available |
| **Effective** | Control is implemented and demonstrably effective | Implemented + effectiveness evidence |

## 6. Resource Planning and Budgeting

### 6.1 Resource Overview

**Personnel Resources:**

| Team/Role | Available Capacity (PD/month) | Planned Utilization | Availability |
|-----------|-------------------------------|---------------------|--------------|
| IT Operations | 40 | 30 | 75% |
| Security Team | 20 | 18 | 90% |
| IAM Team | 15 | 12 | 80% |
| Dev Team | 10 | 5 | 50% |

**Financial Resources:**

| Quarter | Budget | Planned Expenses | Available |
|---------|--------|------------------|-----------|
| Q1 2026 | €50,000 | €45,000 | €5,000 |
| Q2 2026 | €50,000 | €55,000 | -€5,000 (Overrun) |
| Q3 2026 | €50,000 | €30,000 | €20,000 |
| Q4 2026 | €50,000 | €20,000 | €30,000 |

**Budget Request:**
- Q2 2026: Additional €5,000 for M-001 (Redundant switch)

### 6.2 Capacity Planning

**Bottlenecks:**
- Security Team: 90% utilized (critical)
- IAM Team: 80% utilized (high)

**Actions:**
- Prioritization of critical measures
- External support for M-004 (Secret scanning)
- Postponement of non-critical measures to Q3/Q4

## 7. Dependencies and Implementation Risks

### 7.1 Dependencies Between Measures

```
M-002 (Immutable Backups)
  ↓ (requires)
M-001 (Redundant Switch)
  ↓ (enables)
M-005 (VPN Hardening)
```

**Critical Path:**
- M-002 must be completed before M-001
- M-001 is prerequisite for M-005

### 7.2 Implementation Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Resource bottlenecks | High | Medium | External support, prioritization |
| Budget overrun | Medium | Medium | Regular budget monitoring, approval process |
| Technical complexity | Medium | High | Pilot phases, external expertise |
| Resistance to change | Low | Medium | Change management, awareness |

### 7.3 Change Management

**Communication:**
- Regular updates to stakeholders
- Awareness campaigns for affected users
- Training for new controls

**Rollback Planning:**
- Create rollback plan for each measure
- Pilot phases before production rollout
- Backup before critical changes

## 8. Tracking and Reporting

### 8.1 Measure Tracking

**Tracking Frequency:**
- Weekly: Status update for critical measures
- Monthly: Complete RTP review
- Quarterly: Reporting to information security committee

**Tracking Metrics:**
- Number of open measures
- Number of overdue measures
- Average implementation duration
- Budget utilization

### 8.2 Reporting

**Monthly Reporting:**
- Status of all active measures
- Progress (% completion)
- Risks and issues
- Budget status

**Quarterly Reporting:**
- Summary for information security committee
- Trend analysis
- Prioritization recommendations

**Escalation:**
- Overdue measures (> 2 weeks): Escalation to CISO
- Critical delays: Escalation to management

## 9. Effectiveness Verification

### 9.1 Evidence of Effectiveness

Effectiveness must be demonstrated for each implemented measure:

**Evidence Methods:**
- **Technical Tests:** Vulnerability scans, penetration tests, configuration audits
- **Process Audits:** Internal audits, compliance checks
- **Monitoring:** SIEM alerts, log analysis, KPI tracking
- **Documentation:** Policies, procedures, training records

**Example M-002 (Immutable Backups):**
- Evidence: Restore test protocol
- Frequency: Quarterly
- Criteria: RTO/RPO met, backups not modifiable

### 9.2 Evidence Register

**Linkage:**
- See `0700_Appendix_Evidence_Register.md`
- Each measure has linked evidence

## 10. Roles and Responsibilities

### 10.1 RACI Matrix: Risk Treatment

| Activity | CISO | ISMS Manager | Measure Owner | IT Operations | Budget Owner |
|----------|------|--------------|---------------|---------------|--------------|
| Create RTP | A | R | C | C | I |
| Prioritize measures | A | R | C | C | C |
| Implement measures | A | C | R | R | I |
| Approve budget | C | I | I | I | A |
| Track progress | A | R | C | I | I |
| Verify effectiveness | A | R | C | R | I |
| RTP review | A | R | C | C | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 11. References

### 11.1 Internal Documents

- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management Methodology
- `0070_ISMS_Risk_Acceptance_Criteria.md` - Risk Acceptance Criteria
- `0080_ISMS_Risk_Register_Template.md` - Risk Register
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA
- `0360_Policy_Change_and_Release_Management.md` - Change Management
- `0700_Appendix_Evidence_Register.md` - Evidence Register

### 11.2 External Standards

- **ISO/IEC 27001:2022** - Clause 6.1.3: Information security risk treatment
- **ISO/IEC 27002:2022** - Information security controls
- **ISO/IEC 27005:2022** - Information security risk management

## Change History

| Version | Date | Author | Description | Approved By |
|---------|------|--------|-------------|-------------|
| 1.0 | {{ meta-handbook.modifydate }} | {{ meta-organisation-roles.role_CISO }} | Initial version | {{ meta-handbook.management_ceo }} |

**Approved by:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (Monthly)

