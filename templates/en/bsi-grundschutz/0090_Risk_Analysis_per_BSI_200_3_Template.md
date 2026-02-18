# Risk Analysis (BSI Standard 200-3) – Template

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
This template guides the risk analysis according to BSI Standard 200-3.
Risk analysis is performed for objects with elevated protection requirements or special threat situations.
Reference: BSI Standard 200-3 (Risk Analysis based on IT-Grundschutz)
-->

## 1. Objective and Trigger

The risk analysis according to BSI Standard 200-3 identifies and assesses risks for **{{ meta-organisation.name }}** that are not covered by IT-Grundschutz modules.

**Responsible:** {{ meta.ciso.name }} (ISB)

**Triggers for Risk Analysis:**
- High or very high protection need (see Document 0060)
- Special threat situation (e.g., targeted attacks)
- Deviations from IT-Grundschutz requirements
- New technologies without suitable modules
- External requirements (customers, regulation)

[TODO: Document specific triggers for this risk analysis]

## 2. Risk Objects and Scope

**Affected Objects:**

| Object ID | Object | Type | Protection Need | Justification for Risk Analysis |
|---|---|---|---|---|
| [TODO] | [TODO] | Process/Application/System | Very high | [TODO] |
| [TODO] | [TODO] | Process/Application/System | Very high | [TODO] |

**Interfaces and Providers:**
- [TODO: Document external interfaces and service providers]

## 3. Threats, Vulnerabilities and Scenarios

### 3.1 Threat Catalog

| Threat ID | Threat | Category | Description |
|---|---|---|---|
| T-001 | Targeted Cyber Attacks | External | APT attacks on critical systems |
| T-002 | Ransomware | External | Encryption of critical data |
| T-003 | Insider Threat | Internal | Abuse of privileged access |
| T-004 | DDoS Attacks | External | Availability impairment |
| T-005 | Supply Chain Attacks | External | Compromise via suppliers |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 3.2 Vulnerability Catalog

| Vulnerability ID | Vulnerability | Object | Description |
|---|---|---|---|
| V-001 | Insufficient Segmentation | Network | Missing microsegmentation |
| V-002 | Missing MFA | VPN Access | Password-only authentication |
| V-003 | Outdated Software | [TODO: System] | End-of-life software in use |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 3.3 Risk Scenarios

| Scenario ID | Scenario | Threat | Vulnerability | Affected Object |
|---|---|---|---|---|
| S-001 | Ransomware attack on production systems | T-002 | V-001, V-002 | [TODO: Production system] |
| S-002 | Data theft by insider | T-003 | V-002 | [TODO: Database] |
| S-003 | DDoS on public services | T-004 | [TODO] | [TODO: Web server] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Risk Assessment

### 4.1 Assessment Scale

**Likelihood:**

| Level | Description | Frequency |
|---|---|---|
| 1 - Very Low | Unlikely | < 1x in 10 years |
| 2 - Low | Rare | 1x in 5-10 years |
| 3 - Medium | Occasional | 1x in 1-5 years |
| 4 - High | Probable | 1x per year |
| 5 - Very High | Very probable | Multiple times per year |

**Impact (Damage Level):**

| Level | Description | Financial Impact | Business Impact |
|---|---|---|---|
| 1 - Very Low | Negligible | < 10,000 € | No significant impairment |
| 2 - Low | Limited | 10,000 - 50,000 € | Minor impairment |
| 3 - Medium | Considerable | 50,000 - 250,000 € | Noticeable impairment |
| 4 - High | Severe | 250,000 - 1,000,000 € | Significant impairment |
| 5 - Very High | Catastrophic | > 1,000,000 € | Existential threat |

**Risk Matrix:**

| Likelihood | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---|---|---|---|---|
| 5 - Very High | Medium | High | High | Very High | Very High |
| 4 - High | Medium | Medium | High | High | Very High |
| 3 - Medium | Low | Medium | Medium | High | High |
| 2 - Low | Low | Low | Medium | Medium | High |
| 1 - Very Low | Low | Low | Low | Medium | Medium |

### 4.2 Risk Acceptance Criteria

| Risk Level | Treatment | Approval Required |
|---|---|---|
| **Very High** | Must be treated | Executive Management |
| **High** | Should be treated | ISB |
| **Medium** | Can be treated | ISB |
| **Low** | Can be accepted | Information Domain Responsible |

## 5. Risk Register

| Risk ID | Object | Scenario | Threat | Vulnerability | Existing Measures | Likelihood | Impact | Risk (Before) | Treatment | Additional Measure | Owner | Deadline | Risk (After) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-001 | [TODO] | S-001 | T-002 | V-001, V-002 | Antivirus, Backup | 4 | 5 | Very High | Mitigate | Microsegmentation, MFA | {{ meta.cio.name }} | [TODO] | Medium |
| R-002 | [TODO] | S-002 | T-003 | V-002 | Logging, IAM | 3 | 4 | High | Mitigate | PAM, DLP | {{ meta.cio.name }} | [TODO] | Low |
| R-003 | [TODO] | S-003 | T-004 | [TODO] | Firewall | 3 | 3 | Medium | Mitigate | DDoS Protection | {{ meta.cio.name }} | [TODO] | Low |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Risk Treatment Options:**
- **Mitigate:** Implement additional measures
- **Avoid:** Eliminate risk source
- **Transfer:** Transfer risk to third parties (insurance, outsourcing)
- **Accept:** Consciously accept risk (with approval)

## 6. Risk Assessment: Summary

**Risk Distribution (Before Treatment):**
- Very High: [TODO]
- High: [TODO]
- Medium: [TODO]
- Low: [TODO]

**Risk Distribution (After Treatment):**
- Very High: [TODO]
- High: [TODO]
- Medium: [TODO]
- Low: [TODO]

**Top 5 Risks:**
1. [TODO: Risk 1]
2. [TODO: Risk 2]
3. [TODO: Risk 3]
4. [TODO: Risk 4]
5. [TODO: Risk 5]

## 7. Approval and Risk Acceptance

### 7.1 Risk Owners

| Risk ID | Risk | Risk Owner | Acceptance | Date |
|---|---|---|---|---|
| R-001 | [TODO] | {{ meta.ceo.name }} | Accepted after measure implementation | [TODO] |
| R-002 | [TODO] | {{ meta.ciso.name }} | Accepted after measure implementation | [TODO] |

### 7.2 Management Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| ISB | {{ meta.ciso.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| IT Management | {{ meta.cio.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| Executive Management | {{ meta.ceo.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

## 8. Update and Maintenance

The risk analysis is updated when:
- Significant changes in the threat landscape occur
- New vulnerabilities or security incidents emerge
- Changes to the information domain occur
- At least annually as part of the ISMS review

**Responsible:** {{ meta.ciso.name }} (ISB)  
**Next Review:** {{ meta-handbook.next_review }}

**References:**
- BSI Standard 200-3: Risk Analysis based on IT-Grundschutz
- BSI IT-Grundschutz Compendium

<!-- End of template -->