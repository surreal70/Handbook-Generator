# Risk Management – Methodology

**Document-ID:** [FRAMEWORK]-0060
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
This document defines the risk management methodology for the ISMS. It establishes
how information security risks are identified, assessed, treated, and monitored.
This is a critical foundation document that drives the entire risk-based approach
of ISO 27001:2022.

ISO 27001:2022 Reference: Clause 6.1.2 - Information security risk assessment
-->

**Document ID:** 0060  
**Document Type:** ISMS Foundation Document  
**Standard Reference:** ISO/IEC 27001:2022 Clause 6.1.2  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Objective and Scope

### 1.1 Objective

This methodology defines how **{{ meta-organisation.name }}** systematically identifies, assesses, treats, and monitors information security risks. It ensures that:
- Risks are assessed consistently and transparently
- Risk treatment measures are prioritized
- Risks are reduced to an acceptable level
- Management can make informed decisions

### 1.2 Scope

This methodology applies to all information security risks within the ISMS scope (see `0020_ISMS_Scope.md`):
- IT systems and infrastructure
- Business processes
- Information assets and data
- Suppliers and third parties
- Physical security

## 2. Risk Objects

### 2.1 Assets (Information Assets)

**Categories:**
- **Information and Data:** Customer data, business data, technical data, employee data
- **IT Systems:** Servers, network components, endpoints, cloud infrastructure
- **Applications:** Business applications, development tools, communication platforms
- **Services:** IT services, business services
- **People:** Employees with critical knowledge
- **Physical Assets:** Data centers, offices, hardware

**Asset Inventory:**
- See `0720_Appendix_Asset_and_System_Inventory_Template.md`
- Asset owners are responsible for their assets

### 2.2 Business Processes

**Critical Business Processes:**
- [TODO: List of critical business processes]
- See Business Impact Analysis (BIA) in BCM handbook

**Process Owners:**
- Responsible for risks in their process
- See `0040_ISMS_Governance_Roles_and_Responsibilities.md`

### 2.3 Suppliers and Outsourcing

**Critical Suppliers:**
- Cloud providers (AWS, Azure, GCP)
- Managed service providers
- Software suppliers
- See `0460_Policy_Suppliers_and_Cloud_Security.md`

**Third-Party Risk Assessment:**
- Separate risk assessment for critical suppliers
- See `0470_Guideline_Third_Party_Risk_Assessment_and_Cloud_Controls.md`

## 3. Risk Management Methodology

### 3.1 Risk Management Process

```
┌─────────────────────────────────────────────────────────┐
│              Risk Management Cycle                       │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────┐
        │  1. Risk Identification         │
        │  (Threats + Vulnerabilities)    │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │  2. Risk Assessment             │
        │  (Likelihood × Impact)          │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │  3. Risk Treatment              │
        │  (Avoid, Mitigate,              │
        │   Transfer, Accept)             │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │  4. Risk Monitoring             │
        │  (Monitoring, Review)           │
        └────────────┬────────────────────┘
                     │
                     └──────────┐
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Continuous           │
                    │  Improvement          │
                    └───────────────────────┘
```

### 3.2 Risk Identification

**Methods:**
1. **Asset-based:** Identification of threats and vulnerabilities for each asset
2. **Scenario-based:** Analysis of threat scenarios (e.g., ransomware, DDoS, insider threat)
3. **Compliance-based:** Identification of compliance risks (GDPR, NIS2, etc.)

**Risk Formula:**
```
Risk = Threat × Vulnerability × Asset Value
```

**Threats:**
- **Cyber Threats:** Ransomware, phishing, DDoS, APT, malware
- **Human Threats:** Insider threat, social engineering, errors
- **Environmental Threats:** Fire, water, power outage, natural disasters
- **Technical Threats:** Hardware failure, software bugs, configuration errors

**Vulnerabilities:**
- **Technical Vulnerabilities:** Unpatched systems, misconfigurations, weak encryption
- **Organizational Vulnerabilities:** Missing policies, insufficient training, weak processes
- **Physical Vulnerabilities:** Insufficient access control, missing redundancy

**Sources for Risk Identification:**
- Threat Intelligence (CERT, MITRE ATT&CK, vendor advisories)
- Vulnerability Scans (CVE, CVSS)
- Penetration Tests
- Security Incidents and Lessons Learned
- Audit Findings
- Compliance Requirements

### 3.3 Risk Assessment

**Assessment Scales:**

**Likelihood:**

| Level | Description | Frequency |
|-------|-------------|-----------|
| 1 - Very Unlikely | Event is theoretically possible but very unlikely | < 1 in 10 years |
| 2 - Unlikely | Event could occur but is unlikely | 1 in 5-10 years |
| 3 - Possible | Event could occur | 1 in 1-5 years |
| 4 - Likely | Event will probably occur | 1-5 times per year |
| 5 - Very Likely | Event will almost certainly occur | > 5 times per year |

**Impact:**

| Level | Description | Financial Damage | Reputational Damage | Compliance |
|-------|-------------|------------------|---------------------|------------|
| 1 - Negligible | Minimal impact | < €10,000 | None | None |
| 2 - Low | Minor impact | €10,000 - €50,000 | Local | Minor violations |
| 3 - Medium | Moderate impact | €50,000 - €250,000 | Regional | Reportable incidents |
| 4 - High | Significant impact | €250,000 - €1M | National | Fines |
| 5 - Very High | Catastrophic impact | > €1M | International | Business prohibition |

<!-- 
Customize the impact scales based on your organization's specific risk appetite
and business context. Consider financial, reputational, operational, and 
compliance impacts.
-->

**Risk Matrix:**

```
Impact ↑
  5 │  M   H   H   VH  VH
  4 │  M   M   H   H   VH
  3 │  L   M   M   H   H
  2 │  L   L   M   M   H
  1 │  VL  L   L   M   M
    └─────────────────────→ Likelihood
      1   2   3   4   5

Legend:
VL = Very Low
L  = Low
M  = Medium
H  = High
VH = Very High
```

**Risk Score Calculation:**
```
Risk Score = Likelihood × Impact

Example:
Likelihood = 4 (Likely)
Impact = 3 (Medium)
Risk Score = 4 × 3 = 12 (High)
```

### 3.4 Risk Owner

**Responsibilities:**
- Each identified risk has a risk owner
- Risk owner is responsible for risk treatment
- Typically: Asset owner, process owner, or CISO

**Escalation:**
- High and very high risks are escalated to management
- See `0070_ISMS_Risk_Acceptance_Criteria.md`

## 4. Sources for Risk Information

### 4.1 Threat Intelligence

**External Sources:**
- **CERT-Bund:** https://www.cert-bund.de/
- **MITRE ATT&CK:** https://attack.mitre.org/
- **NIST NVD:** https://nvd.nist.gov/
- **Vendor Security Advisories:** Microsoft, Cisco, etc.
- **Threat Intelligence Feeds:** [TODO: Commercial feeds]

**Internal Sources:**
- Security incidents and lessons learned
- Penetration test reports
- Red team exercises

### 4.2 Vulnerabilities

**Vulnerability Scanning:**
- **Tools:** [TODO: Nessus, Qualys, OpenVAS]
- **Frequency:** Weekly (automated)
- **Scope:** All systems in ISMS scope

**CVE and CVSS:**
- Common Vulnerabilities and Exposures (CVE)
- Common Vulnerability Scoring System (CVSS)
- Prioritization by CVSS score

**Patch Management:**
- See `0340_Policy_Vulnerability_and_Patch_Management.md`

### 4.3 Incidents and Findings

**Security Incidents:**
- Each incident is reviewed for risk relevance
- Lessons learned flow into risk analysis
- See `0400_Policy_Incident_Management.md`

**Audit Findings:**
- Internal and external audit findings
- Findings are assessed as risks
- See `0130_ISMS_Internal_Audit_Program.md`

## 5. Outputs of Risk Management

### 5.1 Risk Register

**Content:**
- All identified risks
- Risk assessment (likelihood, impact, score)
- Risk owner
- Risk treatment strategy
- Status and measures

**Document:** `0080_ISMS_Risk_Register_Template.md`

**Maintenance:**
- Quarterly review
- Event-driven updates (new threats, incidents)

### 5.2 Risk Treatment Plan (RTP)

**Content:**
- Planned measures for risk treatment
- Responsible parties and deadlines
- Budget and resources
- Prioritization

**Document:** `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md`

**Tracking:**
- Measures are tracked in RTP
- Regular reporting to CISO and management

### 5.3 Statement of Applicability (SoA)

**Content:**
- Selection and justification of Annex A controls
- Based on risk analysis and compliance requirements
- Documentation of exclusions

**Document:** `0100_ISMS_Statement_of_Applicability_SoA_Template.md`

**Relationship:**
- Risk analysis → Identification of required controls
- SoA → Documentation of control selection
- RTP → Implementation of controls

## 6. Risk Management Cycle

### 6.1 Regular Review

**Frequency:**
- **Quarterly:** Review of risk register
- **Annually:** Complete risk analysis
- **Event-driven:** For significant changes

**Triggers for Event-Driven Review:**
- New threats (e.g., zero-day exploits)
- Significant organizational changes
- New compliance requirements
- Major security incidents
- Audit findings

### 6.2 Risk Monitoring

**Continuous Monitoring:**
- Security monitoring (SIEM, IDS/IPS)
- Vulnerability scanning
- Threat intelligence feeds
- Incident tracking

**KPIs:**
- Number of open risks (by risk level)
- Average time to risk remediation
- Number of accepted risks
- Trend of risk scores

**Reporting:**
- Quarterly to information security committee
- Annually in management review

### 6.3 Continuous Improvement

**Lessons Learned:**
- From security incidents
- From audit findings
- From penetration tests

**Improvement Measures:**
- Adjustment of risk assessment scales
- Improvement of risk identification methods
- Optimization of risk management process

## 7. Roles and Responsibilities

### 7.1 RACI Matrix: Risk Management

| Activity | CISO | ISMS Manager | Risk Owner | IT Operations | Management |
|----------|------|--------------|------------|---------------|------------|
| Define risk management methodology | R/A | C | C | C | I |
| Risk identification | A | R | C | C | I |
| Risk assessment | A | R | C | C | I |
| Plan risk treatment | A | C | R | C | I |
| Implement measures | A | C | R | R | I |
| Risk acceptance (low/medium) | A | I | C | I | I |
| Risk acceptance (high/very high) | C | I | C | I | A |
| Risk monitoring | A | R | C | C | I |
| Risk reporting | R | R | C | I | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 8. References

### Internal Documents
- `0020_ISMS_Scope.md` - ISMS Scope
- `0040_ISMS_Governance_Roles_and_Responsibilities.md` - Governance
- `0070_ISMS_Risk_Acceptance_Criteria.md` - Risk Acceptance Criteria
- `0080_ISMS_Risk_Register_Template.md` - Risk Register
- `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md` - Risk Treatment Plan
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA
- `0340_Policy_Vulnerability_and_Patch_Management.md` - Vulnerability Management
- `0400_Policy_Incident_Management.md` - Incident Management

### External Standards
- **ISO/IEC 27001:2022** - Clause 6.1.2: Information security risk assessment
- **ISO/IEC 27001:2022** - Clause 6.1.3: Information security risk treatment
- **ISO/IEC 27005:2022** - Information security risk management
- **NIST SP 800-30** - Guide for Conducting Risk Assessments

**Approved by:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
{{ meta-handbook.management_ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }}

