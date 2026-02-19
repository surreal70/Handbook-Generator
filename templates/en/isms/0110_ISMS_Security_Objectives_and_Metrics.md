# Information Security Objectives and Metrics

**Document-ID:** [FRAMEWORK]-0110
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
This document defines measurable information security objectives and KPIs.
It ensures that the ISMS performance can be monitored and demonstrates
continuous improvement.

ISO 27001:2022 Reference: Clause 6.2 - Information security objectives
-->

**Document ID:** 0110  
**Document Type:** ISMS Foundation Document  
**Standard Reference:** ISO/IEC 27001:2022 Clause 6.2  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Information Security Objectives

### 1.1 Strategic Objectives

**{{ meta-organisation.name }}** defines the following strategic information security objectives:

| Objective ID | Objective | Description | KPI/Metric | Target Value | Measurement Method | Owner | Frequency | Status |
|--------------|-----------|-------------|------------|--------------|-------------------|-------|-----------|--------|
| **O-001** | Ensure compliance | Compliance with all legal and contractual requirements | Number of compliance violations | 0 | Audit reports, incident reports | {{ meta-organisation-roles.role_CISO }} | Quarterly | Active |
| **O-002** | Minimize risks | Reduction of high and very high risks | Number of risks with score ≥ 13 | < 5 | Risk register | {{ meta-organisation-roles.role_CISO }} | Quarterly | Active |
| **O-003** | Ensure availability | Ensure availability of critical systems | Uptime of critical systems | ≥ 99.5% | Monitoring system | {{ meta-organisation-roles.role_CIO }} | Monthly | Active |
| **O-004** | Reduce incidents | Reduction of number of security incidents | Number of security incidents | < 10 per quarter | Incident management system | {{ meta-organisation-roles.role_CISO }} | Quarterly | Active |
| **O-005** | Increase awareness | Increase security awareness | Training participation rate | 100% | LMS, training records | {{ meta-organisation-roles.role_CISO }} | Annually | Active |
| **O-006** | Patch compliance | Timely installation of critical patches | Average time to install patches (critical) | < 7 days | Vulnerability management system | IT Operations | Monthly | Active |

[TODO: Add additional organization-specific objectives]

### 1.2 Operational Objectives

| Objective ID | Objective | KPI/Metric | Target Value | Owner | Frequency |
|--------------|-----------|------------|--------------|-------|-----------|
| **O-010** | Complete MFA rollout | MFA activation rate | 100% | IT Operations | Monthly |
| **O-011** | Vulnerability management | Average time to remediate high vulnerabilities | < 30 days | IT Operations | Monthly |
| **O-012** | Backup tests | Success rate of restore tests | 100% | IT Operations | Quarterly |
| **O-013** | Phishing resilience | Phishing click rate in simulations | < 5% | {{ meta-organisation-roles.role_CISO }} | Quarterly |

## 2. Key Performance Indicators (KPIs)

### 2.1 Security KPIs

**Risk Management:**
- Number of identified risks (by level)
- Number of treated risks per quarter
- Average risk remediation time
- Number of accepted risks

**Incident Management:**
- Number of security incidents (by severity)
- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- Mean Time to Recover (MTTR)

**Vulnerability Management:**
- Number of open vulnerabilities (by CVSS score)
- Average time to install patches
- Patch compliance rate

**Access Management:**
- Number of privileged accounts
- MFA activation rate
- Recertification rate
- Number of access violations

**Awareness and Training:**
- Training participation rate
- Phishing simulation results
- Number of security incidents reported by employees

### 2.2 Compliance KPIs

- Number of audit findings (by severity)
- Average time to remediate findings
- Compliance rate with policies
- Number of compliance violations

### 2.3 Operational KPIs

- Uptime of critical systems
- Backup success rate
- Restore test success rate
- Number of change requests with security review

## 3. Measurement Methods and Data Sources

### 3.1 Data Sources

| KPI | Data Source | Responsible | Automation |
|-----|-------------|-------------|------------|
| Number of incidents | Incident management system | Security Team | Yes |
| Risk scores | Risk register | ISMS Manager | Partial |
| Vulnerabilities | Vulnerability scanner | IT Operations | Yes |
| Uptime | Monitoring system | IT Operations | Yes |
| Training participation | LMS | HR / CISO | Yes |
| Patch compliance | Patch management system | IT Operations | Yes |

### 3.2 Reporting Dashboards

**Monthly Dashboard:**
- Incident statistics
- Vulnerability status
- Patch compliance
- Uptime statistics

**Quarterly Dashboard:**
- Risk overview
- Audit findings status
- Training statistics
- Trend analyses

**Annual Dashboard:**
- Objective achievement
- Year-over-year comparison
- Strategic recommendations

## 4. Measures for Objective Achievement

### 4.1 Linkage to Risk Treatment Plan

Each objective is linked to measures in the risk treatment plan:
- See `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md`

**Example:**
- **Objective O-002:** Minimize risks
- **Measures:** M-001 (Redundant switch), M-002 (Immutable backups), M-003 (MFA rollout)

### 4.2 Continuous Improvement

**Improvement Cycle:**
1. Define objectives
2. Plan measures
3. Implement measures
4. Measure KPIs
5. Analyze results
6. Identify improvements
7. Adjust objectives

## 5. Review and Adjustment

### 5.1 Regular Review

**Quarterly:**
- Review of KPI values
- Analysis of deviations
- Adjustment of measures

**Annually:**
- Complete review of all objectives
- Adjustment of target values
- Definition of new objectives
- As part of management review

### 5.2 Triggers for Unscheduled Review

- Significant changes to ISMS scope
- New compliance requirements
- Major security incidents
- Audit findings

## 6. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register
- `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md` - Risk Treatment Plan
- `0140_ISMS_Management_Review_Template.md` - Management Review

### External Standards
- **ISO/IEC 27001:2022** - Clause 6.2: Information security objectives
- **ISO/IEC 27001:2022** - Clause 9.1: Monitoring, measurement, analysis and evaluation

**Approved by:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
{{ meta-handbook.management_ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }}

