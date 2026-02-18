
Document-ID: nist-csf-0020
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Organizational Context (GV.OC)

**Document-ID:** [FRAMEWORK]-0020
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

## Purpose

This document defines the organizational context for cybersecurity risk management, including mission, stakeholder expectations, and legal/regulatory requirements.

## Scope

{{ meta-handbook.scope }}

## Organizational Mission and Objectives

### Corporate Mission
{{ meta-handbook.organization_mission }}

### Business Objectives
1. {{ meta.business_goal_1 }}
2. {{ meta.business_goal_2 }}
3. {{ meta.business_goal_3 }}

### Cybersecurity Objectives
- Protect critical business processes and data
- Maintain customer trust
- Comply with regulatory requirements
- Minimize cybersecurity risks

## Stakeholder Analysis

### Internal Stakeholders

| Stakeholder | Expectations | Communication Channel |
|-------------|--------------|----------------------|
| Board of Directors | Risk transparency, Compliance | Quarterly reports |
| Executive Management | Business continuity | Monthly reviews |
| IT Department | Clear policies, Resources | Weekly meetings |
| Employees | Secure work environment | Training, Intranet |

### External Stakeholders

| Stakeholder | Expectations | Communication Channel |
|-------------|--------------|----------------------|
| Customers | Data privacy, Availability | Privacy policy |
| Regulators | Compliance evidence | Reports, Audits |
| Partners | Secure collaboration | Contracts, SLAs |
| Suppliers | Security requirements | Supplier contracts |

## Legal and Regulatory Requirements

### Applicable Laws and Regulations

1. **Data Protection**
   - GDPR (General Data Protection Regulation)
   - Local data protection laws
   - {{ meta-handbook.additional_privacy_laws }}

2. **Industry-Specific Regulations**
   - {{ meta.industry_regulation_1 }}
   - {{ meta.industry_regulation_2 }}

3. **Contractual Obligations**
   - Customer contracts with security requirements
   - Supplier agreements
   - Service Level Agreements (SLAs)

## Critical Business Functions

### High-Priority Business Processes

| Process | Criticality | Cybersecurity Requirements |
|---------|-------------|---------------------------|
| {{ meta.critical_process_1 }} | High | Availability, Integrity |
| {{ meta.critical_process_2 }} | High | Confidentiality, Availability |
| {{ meta.critical_process_3 }} | Medium | Integrity, Traceability |

## Risk Tolerance and Appetite

### Risk Appetite Statement
{{ meta-organisation.name }} is willing to accept {{ meta-handbook.risk_appetite_level }} cybersecurity risks to achieve business objectives, provided that:
- Critical systems are adequately protected
- Regulatory requirements are met
- Reputational risks are minimized

### Risk Tolerance Thresholds

| Risk Category | Tolerance Threshold | Escalation |
|---------------|---------------------|------------|
| Data breach | Zero tolerance | Immediate escalation to Board |
| System outage | < 4 hours/year | Escalation to CIO |
| Security incidents | < 10 Minor/year | Monthly review |

## Organizational Structure

### Cybersecurity Governance Structure
```
Board of Directors
    ↓
Executive Management
    ↓
CISO ({{ meta-organisation-roles.role_CISO }})
    ↓
├── Security Operations
├── Risk Management
├── Compliance
└── Security Architecture
```

## Document References

- 0030_risk_management_strategy.md
- 0040_roles_responsibilities.md
- 0050_policy_framework.md

<!-- 
Author Notes:
- Update stakeholder list regularly
- Review legal requirements at least annually
- Adjust risk tolerance to business changes
-->
