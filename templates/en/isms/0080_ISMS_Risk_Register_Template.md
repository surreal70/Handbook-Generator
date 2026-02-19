# Risk Register (Template)

**Document-ID:** [FRAMEWORK]-0080
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
The risk register is the central repository for all identified information security
risks. It documents risk assessments, treatment decisions, and tracks risk status.
This is a living document that should be reviewed and updated regularly.

ISO 27001:2022 Reference: Clause 6.1.2 - Information security risk assessment
-->

**Document ID:** 0080  
**Document Type:** ISMS Register/Template  
**Standard Reference:** ISO/IEC 27001:2022 Clause 6.1.2  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Confidential  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose and Instructions

### 1.1 Purpose

The risk register documents all identified information security risks within the ISMS scope of **{{ meta-organisation.name }}**. It serves as:
- Central overview of all risks
- Basis for risk treatment decisions
- Evidence for audits and compliance
- Basis for risk reporting

### 1.2 Usage Instructions

**Each row describes a risk:**
- Unique risk ID (R-001, R-002, etc.)
- Affected asset or process
- Threat and vulnerability
- Risk assessment (likelihood, impact, score)
- Risk owner
- Treatment strategy
- Link to controls and measures

**Maintenance:**
- Quarterly review by ISMS Manager
- Event-driven updates for new risks
- Archiving of treated/closed risks

**Links:**
- Controls: See `0100_ISMS_Statement_of_Applicability_SoA_Template.md`
- Measures: See `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md`
- Evidence: See `0700_Appendix_Evidence_Register.md`

## 2. Risk Register Table

### 2.1 Active Risks

| Risk ID | Asset/Process | Threat | Vulnerability | Impact (1-5) | Likelihood (1-5) | Score | Risk Level | Risk Owner | Treatment | Measure/Control | Status | Target Date | Remarks |
|---------|---------------|--------|---------------|--------------|------------------|-------|------------|------------|------------|-----------------|--------|-------------|---------|
| R-001 | [[ netbox.device.core_switch.name ]] | Hardware failure | No redundancy | 4 | 3 | 12 | Medium | {{ meta-organisation-roles.role_CIO }} | Mitigate | Procure redundant switch | Open | 2026-06-30 | Budget approved |
| R-002 | Customer data (GDPR) | Ransomware | Insufficient backups | 5 | 4 | 20 | High | {{ meta-organisation-roles.role_CISO }} | Mitigate | Implement immutable backups | In Progress | 2026-03-31 | See M-002 |
| R-003 | Email system | Phishing | Missing MFA | 4 | 4 | 16 | High | {{ meta-organisation-roles.role_CIO }} | Mitigate | MFA for all users | In Progress | 2026-02-28 | 80% complete |
| R-004 | Development environment | Secrets in code | No secret scanning | 3 | 3 | 9 | Medium | Dev Lead | Mitigate | Secret scanning tool | Planned | 2026-04-30 | Tool evaluation ongoing |
| R-005 | Remote access | Unauthorized access | Weak VPN configuration | 4 | 2 | 8 | Medium | IT Operations | Mitigate | VPN hardening | Open | 2026-05-31 | - |

<!-- 
Add your organization's specific risks to this table. Each risk should be
uniquely identified and linked to treatment measures.
-->

[TODO: Add additional risks based on risk analysis]

### 2.2 Accepted Risks

| Risk ID | Asset/Process | Threat | Vulnerability | Score | Risk Level | Risk Owner | Accepted By | Acceptance Date | Valid Until | Justification | Review Status |
|---------|---------------|--------|---------------|-------|-------------|---------------|--------------|----------------|-------------|---------------|---------------|
| R-010 | Legacy system XYZ | Unpatched vulnerabilities | System being phased out | 9 | Medium | {{ meta-organisation-roles.role_CIO }} | {{ meta-organisation-roles.role_CISO }} | 2026-01-15 | 2026-06-30 | System will be decommissioned on 30.06.2026 | Active |
| R-011 | Test environment | Missing encryption | No production data | 6 | Low | Dev Lead | {{ meta-organisation-roles.role_CISO }} | 2026-01-20 | 2027-01-20 | Test environment contains only synthetic data | Active |

[TODO: Document accepted risks]

### 2.3 Closed/Treated Risks (Archive)

| Risk ID | Asset/Process | Threat | Score | Treatment | Closure Date | Remarks |
|---------|---------------|--------|-------|------------|--------------|---------|
| R-020 | Web server | Unpatched vulnerability CVE-2025-1234 | 15 | Mitigate | 2026-01-10 | Patch installed, vulnerability scan confirmed |
| R-021 | Firewall | Misconfiguration | 12 | Mitigate | 2026-01-15 | Configuration corrected, audit performed |

[TODO: Archive closed risks]

## 3. Risk Categories and Classification

### 3.1 Risk Categories

**Technical Risks:**
- Infrastructure (hardware, network, cloud)
- Applications (software, development)
- Data (databases, backups, encryption)

**Organizational Risks:**
- Processes (missing or insufficient processes)
- Personnel (lack of competence, insider threat)
- Suppliers (third-party risks)

**Physical Risks:**
- Locations (access, environmental risks)
- Hardware (theft, destruction)

**Compliance Risks:**
- Regulatory requirements (GDPR, NIS2, etc.)
- Contractual obligations

### 3.2 Threat Sources

**External Threats:**
- Cybercriminals (ransomware, phishing, DDoS)
- Hacktivists
- Nation-states (APT)
- Competitors

**Internal Threats:**
- Insiders (malicious or negligent)
- Human errors
- Process failures

**Environmental Threats:**
- Natural disasters (fire, water, storm)
- Infrastructure failures (power, cooling)

## 4. Risk Assessment

### 4.1 Assessment Scales

**Likelihood:**

| Level | Description | Frequency |
|-------|-------------|-----------|
| 1 | Very unlikely | < 1 in 10 years |
| 2 | Unlikely | 1 in 5-10 years |
| 3 | Possible | 1 in 1-5 years |
| 4 | Likely | 1-5 times per year |
| 5 | Very likely | > 5 times per year |

**Impact:**

| Level | Description | Financial | Reputation | Compliance |
|-------|-------------|-----------|------------|------------|
| 1 | Negligible | < €10k | None | None |
| 2 | Low | €10-50k | Local | Minor violations |
| 3 | Medium | €50-250k | Regional | Reportable |
| 4 | High | €250k-1M | National | Fines |
| 5 | Very high | > €1M | International | Business prohibition |

**Risk Score:** Likelihood × Impact

**Risk Levels:**

| Score | Risk Level | Color | Treatment |
|-------|------------|-------|-----------|
| 1-2 | Very low | Green | Monitoring |
| 3-6 | Low | Green | Monitoring |
| 7-12 | Medium | Yellow | Treatment recommended |
| 13-20 | High | Orange | Treatment required |
| 21-25 | Very high | Red | Immediate treatment |

### 4.2 Treatment Strategies

**Avoid:**
- Discontinue activity causing the risk
- Example: Avoid risky technology

**Mitigate:**
- Measures to reduce likelihood or impact
- Example: Implement controls (firewall, MFA, encryption)

**Transfer:**
- Transfer risk to third parties
- Example: Cyber insurance, outsourcing with SLA

**Accept:**
- Conscious decision to bear the risk
- Only for low/medium risks after approval
- See `0070_ISMS_Risk_Acceptance_Criteria.md`

## 5. Risk Owners and Responsibilities

### 5.1 Risk Owner

**Responsibilities:**
- Responsible for risk treatment
- Decision on treatment strategy
- Monitoring of measure implementation
- Regular risk assessment

**Typical Risk Owners:**
- **CISO:** Cross-cutting security risks
- **CIO:** IT infrastructure risks
- **Asset Owner:** Asset-specific risks
- **Process Owner:** Process-specific risks

### 5.2 RACI Matrix: Risk Management

| Activity | CISO | ISMS Manager | Risk Owner | IT Operations |
|----------|------|--------------|------------|---------------|
| Identify risk | A | R | C | C |
| Assess risk | A | R | C | C |
| Plan treatment | A | C | R | C |
| Implement measures | A | C | R | R |
| Monitor risk | A | R | C | C |
| Maintain risk register | A | R | C | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 6. Risk Reporting

### 6.1 Regular Reporting

**Quarterly:**
- Risk dashboard to information security committee
- Number of risks by level
- Trend of risk scores
- Status of risk treatment

**Annually:**
- Complete risk report in management review
- See `0140_ISMS_Management_Review_Template.md`

### 6.2 Ad-hoc Reporting

**Triggers:**
- New critical risks (score ≥ 13)
- Significant change in existing risks
- Security incidents with risk relevance

**Escalation:**
- High risks: Immediate notification to CISO and CIO
- Very high risks: Immediate notification to management

## 7. Risk Review and Update

### 7.1 Regular Review

**Quarterly:**
- Review of all active risks
- Update of assessments
- Status update of measures
- Review of accepted risks

**Annually:**
- Complete risk analysis
- Identification of new risks
- Archiving of closed risks

### 7.2 Triggers for Unscheduled Review

**External Triggers:**
- New threats (zero-day exploits, new malware)
- New vulnerabilities (CVE publications)
- Change in threat landscape
- New compliance requirements

**Internal Triggers:**
- Security incidents
- Audit findings
- Significant organizational changes
- New assets or processes

## 8. Links and References

### 8.1 Links to Other ISMS Documents

**Risk Treatment Plan (RTP):**
- Each risk with treatment "Mitigate" has measures in RTP
- See `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md`

**Statement of Applicability (SoA):**
- Controls in SoA are selected based on risk analysis
- See `0100_ISMS_Statement_of_Applicability_SoA_Template.md`

**Asset Inventory:**
- Risks are linked to assets
- See `0720_Appendix_Asset_and_System_Inventory_Template.md`

**Incident Reports:**
- Incidents can identify new risks
- See `0400_Policy_Incident_Management.md`

### 8.2 Internal Documents

- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management Methodology
- `0070_ISMS_Risk_Acceptance_Criteria.md` - Risk Acceptance Criteria
- `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md` - Risk Treatment Plan
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA

### 8.3 External Standards

- **ISO/IEC 27001:2022** - Clause 6.1.2: Information security risk assessment
- **ISO/IEC 27005:2022** - Information security risk management
- **NIST SP 800-30** - Guide for Conducting Risk Assessments

## Change History

| Version | Date | Author | Description | Approved By |
|---------|------|--------|-------------|-------------|
| 1.0 | {{ meta-handbook.modifydate }} | {{ meta-organisation-roles.role_CISO }} | Initial version | {{ meta-handbook.management_ceo }} |

**Approved by:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (Quarterly)

