# NIST Cybersecurity Framework 2.0 Handbook

**Document Metadata**

- **Created on:** 2026-02-10
- **Author:** Andreas Huemmer [andreas.huemmer@adminsend.de]
- **Version:** 0.0.8
- **Type:** NIST CSF 2.0 Cybersecurity Handbook

**Document-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Status:** {{ meta.status }}  
**Classification:** {{ meta.classification }}  
**Template-Version:** 1.0  
**Revision:** 0  
---


## Handbook Information

**Organization:** {{ meta.organization }}  
**Scope:** {{ meta.scope }}  
**Valid from:** {{ meta.valid_from }}  
**Next Review:** {{ meta.next_review }}  

---

## Document Purpose

This handbook documents cybersecurity risk management according to the NIST Cybersecurity Framework (CSF) 2.0. It serves as a guide for implementing and managing cybersecurity practices across the six core functions: Govern, Identify, Protect, Detect, Respond, and Recover.

## Scope

{{ meta.scope }}

## Normative References

- NIST Cybersecurity Framework Version 2.0
- NIST Special Publication 800-53 - Security and Privacy Controls
- NIST Special Publication 800-37 - Risk Management Framework
- ISO/IEC 27001:2013 - Information Security Management Systems

## Change History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| {{ meta.version }} | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial Version |



---

**Approved by:**  
Thomas Weber, Chief Information Security Officer  
Date: {{ meta.approval_date }}

**Next Review:** {{ meta.next_review }}

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |


---
Document-ID: nist-csf-0010
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Govern - Overview

## Purpose

This document provides an overview of the Govern function of the NIST Cybersecurity Framework 2.0. The Govern function establishes and monitors the organization's cybersecurity risk management strategy, expectations, and policies.

## Scope

This document applies to:
- {{ meta.organization }}
- All business units and IT systems
- Cybersecurity governance structures

## Govern Function

The Govern function is the first and foundational function in NIST CSF 2.0. It ensures that cybersecurity risk management is integrated into the organization's overall strategy.

### Core Aspects

1. **Organizational Context**: Understanding the mission, stakeholders, and requirements
2. **Risk Management Strategy**: Establishing risk appetite and risk tolerance
3. **Roles and Responsibilities**: Clear assignment of cybersecurity accountability
4. **Policies**: Establishing cybersecurity policies and standards
5. **Oversight**: Monitoring and directing the cybersecurity program

## Govern Categories

### GV.OC - Organizational Context
Understanding the organizational context for cybersecurity risk management

### GV.RM - Risk Management Strategy
Establishing and communicating the risk management strategy

### GV.RR - Roles, Responsibilities, and Authorities
Defining roles and responsibilities for cybersecurity

### GV.PO - Policy
Establishing and maintaining cybersecurity policies

### GV.OV - Oversight
Overseeing the cybersecurity strategy and activities

### GV.SC - Supply Chain Risk Management
Managing cybersecurity risks in the supply chain

## Integration with Other Functions

The Govern function provides the foundation for:
- **Identify**: Informs asset and risk assessments
- **Protect**: Guides protective measures and controls
- **Detect**: Defines detection requirements
- **Respond**: Establishes response expectations
- **Recover**: Sets recovery priorities

## Responsibilities

| Role | Responsibility |
|------|----------------|
| Thomas Weber | Overall responsibility for cybersecurity governance |
| {{ meta.cro }} | Risk management strategy and oversight |
| Board of Directors | Oversight and strategic direction |
| Executive Management | Resource allocation and support |

## Document References

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0040_roles_responsibilities.md
- 0050_policy_framework.md
- 0060_oversight.md
- 0070_supply_chain_risk_management.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0020
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Organizational Context (GV.OC)

## Purpose

This document defines the organizational context for cybersecurity risk management, including mission, stakeholder expectations, and legal/regulatory requirements.

## Scope

{{ meta.scope }}

## Organizational Mission and Objectives

### Corporate Mission
{{ meta.organization_mission }}

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
   - {{ meta.additional_privacy_laws }}

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
{{ meta.organization }} is willing to accept {{ meta.risk_appetite_level }} cybersecurity risks to achieve business objectives, provided that:
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
CISO (Thomas Weber)
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

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0030
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Risk Management Strategy (GV.RM)

## Purpose

This document defines the organization's cybersecurity risk management strategy, including risk appetite, risk assessment methodology, and risk treatment approaches.

## Scope

{{ meta.scope }}

## Risk Management Framework

### Risk Management Approach
{{ meta.organization }} follows a risk-based approach to cybersecurity that:
- Aligns business objectives with security requirements
- Enables continuous risk assessment and monitoring
- Supports informed decision-making
- Focuses resources on critical risks

### Risk Management Process

1. **Risk Identification**: Detecting potential cybersecurity threats
2. **Risk Assessment**: Analyzing likelihood and impact
3. **Risk Treatment**: Selecting appropriate measures
4. **Risk Monitoring**: Continuous review and adjustment

## Risk Appetite and Tolerance

### Risk Appetite Statement
{{ meta.risk_appetite_statement }}

### Risk Tolerance Levels

| Risk Level | Description | Actions |
|------------|-------------|---------|
| Critical | Existential threat | Immediate treatment required |
| High | Significant impact | Treatment within 30 days |
| Medium | Moderate impact | Treatment within 90 days |
| Low | Minor impact | Acceptable with monitoring |

## Risk Assessment Methodology

### Assessment Criteria

**Likelihood:**
- Very high (5): > 80% probability
- High (4): 60-80% probability
- Medium (3): 40-60% probability
- Low (2): 20-40% probability
- Very low (1): < 20% probability

**Impact:**
- Very high (5): > {{ meta.impact_threshold_critical }}
- High (4): {{ meta.impact_threshold_high }}
- Medium (3): {{ meta.impact_threshold_medium }}
- Low (2): {{ meta.impact_threshold_low }}
- Very low (1): < {{ meta.impact_threshold_minimal }}

### Risk Matrix

| Likelihood | Very low | Low | Medium | High | Very high |
|-----------|----------|-----|--------|------|-----------|
| Very high (5) | Medium | High | High | Critical | Critical |
| High (4) | Low | Medium | High | High | Critical |
| Medium (3) | Low | Medium | Medium | High | High |
| Low (2) | Very low | Low | Medium | Medium | High |
| Very low (1) | Very low | Low | Low | Medium | Medium |

## Risk Treatment Options

### Treatment Strategies

1. **Avoid**: Discontinue activity causing the risk
2. **Reduce**: Implement controls to mitigate risk
3. **Transfer**: Transfer risk to third parties (e.g., insurance)
4. **Accept**: Consciously accept risk with justification

### Decision Criteria

| Risk Level | Preferred Strategy | Approval Required |
|------------|-------------------|-------------------|
| Critical | Avoid or Reduce | Board of Directors |
| High | Reduce | CISO |
| Medium | Reduce or Transfer | Risk Manager |
| Low | Accept with monitoring | Department Head |

## Risk Communication

### Reporting

| Audience | Frequency | Content |
|----------|-----------|---------|
| Board of Directors | Quarterly | Risk profile, critical risks, trends |
| Executive Management | Monthly | Current risks, treatment progress |
| CISO | Weekly | Detailed risk analysis, incidents |
| Risk Manager | Daily | New risks, status changes |

## Integration with Business Risk Management

### Alignment with Enterprise Risk Management (ERM)
- Cybersecurity risks are integrated into the ERM framework
- Consistent risk assessment methodology across all risk categories
- Joint reporting to Board and Executive Management

## Continuous Improvement

### Review Cycles
- Annual review of risk management strategy
- Quarterly update of risk assessments
- Monthly review of critical risks

## Document References

- 0020_organizational_context.md
- 0040_roles_responsibilities.md
- 0100_asset_management.md (Identify)
- 0130_risk_assessment.md (Identify)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0040
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Roles and Responsibilities (GV.RR)

## Purpose

This document defines the roles, responsibilities, and authorities for cybersecurity risk management within the organization.

## Scope

{{ meta.scope }}

## Governance Structure

### Board of Directors
**Responsibilities:**
- Strategic oversight of cybersecurity risks
- Approval of cybersecurity strategy and policies
- Monitoring cybersecurity performance
- Resource allocation for cybersecurity initiatives

### Executive Management
**Responsibilities:**
- Implementation of cybersecurity strategy
- Provision of resources and support
- Promotion of security culture
- Escalation of critical risks to the Board

## Cybersecurity Roles

### Chief Information Security Officer (CISO)
**Name:** Thomas Weber  
**Responsibilities:**
- Overall responsibility for cybersecurity program
- Development and maintenance of cybersecurity strategy
- Risk management and compliance oversight
- Reporting to Executive Management and Board
- Leadership of cybersecurity team

**Authorities:**
- Approval of security policies
- Budget responsibility for cybersecurity
- Escalation of security incidents
- Enforcement of security requirements

### Chief Risk Officer (CRO)
**Name:** {{ meta.cro }}  
**Responsibilities:**
- Integration of cybersecurity risks into ERM
- Risk assessment and reporting
- Coordination with CISO on risk treatment

### Security Operations Manager
**Name:** {{ meta.security_ops_manager }}  
**Responsibilities:**
- Daily operation of Security Operations Center (SOC)
- Incident response and management
- Security monitoring and threat detection
- Coordination with IT operations

### Security Architect
**Name:** {{ meta.security_architect }}  
**Responsibilities:**
- Design of secure system architectures
- Security requirements for new projects
- Technology evaluation and selection
- Security-by-design principles

### Compliance Manager
**Name:** {{ meta.compliance_manager }}  
**Responsibilities:**
- Monitoring regulatory compliance
- Conducting compliance assessments
- Coordination of audits
- Maintenance of compliance documentation

## Business Unit Responsibilities

### IT Department
**Head:** {{ meta.it_director }}  
**Responsibilities:**
- Implementation of security controls
- Patch management and system hardening
- Access management
- Backup and recovery

### Human Resources
**Head:** {{ meta.hr_director }}  
**Responsibilities:**
- Security training for employees
- Background checks
- Onboarding/offboarding processes
- Enforcement of security policies

### Legal/Compliance
**Head:** {{ meta.legal_director }}  
**Responsibilities:**
- Legal advice on cybersecurity
- Contract review (security clauses)
- Data protection compliance
- Incident response (legal aspects)

### Procurement
**Head:** {{ meta.procurement_director }}  
**Responsibilities:**
- Supplier security assessments
- Security requirements in contracts
- Third-party risk management

## Employee Responsibilities

### All Employees
**Responsibilities:**
- Compliance with security policies
- Reporting security incidents
- Participation in security training
- Protection of credentials and data

## RACI Matrix

| Activity | CISO | CRO | Sec Ops | IT | HR | Legal |
|----------|------|-----|---------|----|----|-------|
| Strategy Development | A | C | I | I | I | C |
| Risk Assessment | R | A | C | C | I | C |
| Incident Response | A | I | R | C | I | C |
| Policy Development | A | C | C | C | C | R |
| Training | C | I | I | I | A | C |
| Compliance Audits | C | C | I | C | I | A |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Escalation Paths

### Security Incidents
1. Detection → Security Operations
2. Assessment → CISO
3. Critical Incidents → Executive Management
4. Existential Incidents → Board of Directors

### Risks
1. Identification → Risk Manager
2. Assessment → CRO
3. High Risks → CISO
4. Critical Risks → Executive Management/Board

## Document References

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0050_policy_framework.md
- 0060_oversight.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0050
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Policy Framework (GV.PO)

## Purpose

This document describes the organization's cybersecurity policy framework, including policy hierarchy, development process, and enforcement mechanisms.

## Scope

{{ meta.scope }}

## Policy Hierarchy

### Level 1: Cybersecurity Policy (Overarching Policy)
**Purpose:** Defines overarching cybersecurity objectives and principles  
**Approval:** Board of Directors  
**Review:** Annually

### Level 2: Standards
**Purpose:** Specific technical and organizational requirements  
**Approval:** CISO  
**Review:** Annually

### Level 3: Procedures and Guidelines
**Purpose:** Detailed instructions for implementing standards  
**Approval:** Department Head  
**Review:** Semi-annually

### Level 4: Work Instructions
**Purpose:** Step-by-step guidance for specific tasks  
**Approval:** Team Lead  
**Review:** Quarterly

## Core Policies

### 1. Information Security Policy
**Description:** Overarching security policy  
**Scope:** Entire organization  
**Responsible:** Thomas Weber  
**Status:** {{ meta.policy_status }}

**Core Principles:**
- Confidentiality, Integrity, Availability (CIA)
- Defense-in-Depth
- Least Privilege
- Separation of Duties

### 2. Access Control Policy
**Description:** Regulation of access to information and systems  
**Scope:** All users and systems  
**Responsible:** {{ meta.security_architect }}

**Core Elements:**
- User identification and authentication
- Authorization and access rights
- Privileged Access Management
- Access logs and monitoring

### 3. Data Protection Policy
**Description:** Protection of personal and sensitive data  
**Scope:** All data processing activities  
**Responsible:** {{ meta.dpo }}

**Core Elements:**
- Data classification
- Data protection principles (GDPR)
- Data minimization
- Data subject rights

### 4. Incident Response Policy
**Description:** Handling of security incidents  
**Scope:** All employees  
**Responsible:** {{ meta.security_ops_manager }}

**Core Elements:**
- Incident classification
- Reporting obligations
- Response process
- Post-incident review

### 5. Acceptable Use Policy
**Description:** Acceptable use of IT resources  
**Scope:** All users  
**Responsible:** {{ meta.it_director }}

**Core Elements:**
- Permitted and prohibited activities
- Personal use
- Monitoring and surveillance
- Consequences of violations

### 6. Third-Party Risk Management Policy
**Description:** Management of third-party risks  
**Scope:** All suppliers and partners  
**Responsible:** {{ meta.procurement_director }}

**Core Elements:**
- Supplier assessment
- Contractual security requirements
- Ongoing monitoring
- Incident management

## Policy Development Process

### 1. Initiation
- Identification of need
- Stakeholder analysis
- Resource allocation

### 2. Development
- Policy draft
- Stakeholder consultation
- Legal compliance review

### 3. Approval
- Review by CISO
- Approval by responsible authority
- Documentation of approval

### 4. Communication
- Publication on intranet
- Training and awareness
- Employee acknowledgment

### 5. Implementation
- Implementation of requirements
- Provision of resources
- Compliance monitoring

### 6. Review and Update
- Regular reviews
- Adaptation to changes
- Version control

## Policy Enforcement

### Compliance Monitoring
- Regular audits
- Automated compliance checks
- Self-assessments

### Violations and Consequences

| Severity | Examples | Consequences |
|----------|----------|--------------|
| Critical | Intentional data leaks | Termination, legal action |
| High | Repeated violations | Warning, training |
| Medium | Negligence | Caution, training |
| Low | Unintentional errors | Training, awareness |

## Exceptions and Deviations

### Exception Process
1. Request with justification
2. Risk assessment
3. Approval by CISO
4. Time limitation
5. Compensating controls

### Documentation
- Exception register
- Justification and risk assessment
- Approval date and duration
- Compensating controls

## Policy Repository

**Location:** {{ meta.policy_repository }}  
**Access:** All employees (read access)  
**Management:** Compliance team

## Training and Awareness

### Mandatory Training
- New employees: Within 30 days
- All employees: Annually
- Privileged users: Semi-annually

### Awareness Campaigns
- Monthly security tips
- Phishing simulations
- Security newsletter

## Document References

- 0020_organizational_context.md
- 0040_roles_responsibilities.md
- 0060_oversight.md
- 0210_awareness_training.md (Protect)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0060
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Oversight and Monitoring (GV.OV)

## Purpose

This document describes the oversight and monitoring mechanisms for the organization's cybersecurity program.

## Scope

{{ meta.scope }}

## Governance Oversight

### Board of Directors
**Role:** Strategic oversight  
**Frequency:** Quarterly

**Oversight Activities:**
- Review of cybersecurity risk profile
- Approval of strategic initiatives
- Compliance monitoring
- Assessment of cybersecurity investments

**Reporting:**
- Risk dashboard
- Critical incidents
- Compliance status
- Budget and resources

### Executive Management
**Role:** Operational oversight  
**Frequency:** Monthly

**Oversight Activities:**
- Monitoring program implementation
- Resource allocation
- Escalation management
- Performance review

## Cybersecurity Committees

### Cybersecurity Steering Committee
**Chair:** Thomas Weber  
**Members:**
- CIO
- CRO
- CFO
- Business Unit Heads
- Legal Counsel

**Frequency:** Monthly

**Responsibilities:**
- Strategic direction
- Initiative prioritization
- Budget approval
- Risk assessment and treatment

### Security Operations Committee
**Chair:** {{ meta.security_ops_manager }}  
**Members:**
- IT Operations
- Network Team
- Application Security
- Incident Response Team

**Frequency:** Weekly

**Responsibilities:**
- Operational security monitoring
- Incident coordination
- Threat intelligence sharing
- Technical decisions

### Risk Management Committee
**Chair:** {{ meta.cro }}  
**Members:**
- CISO
- Business Unit Heads
- Compliance Manager
- Internal Audit

**Frequency:** Quarterly

**Responsibilities:**
- Risk assessment and prioritization
- Risk treatment strategies
- Risk tolerance review
- Integration with ERM

## Performance Metrics

### Key Performance Indicators (KPIs)

| KPI | Target | Measurement Frequency | Responsible |
|-----|--------|----------------------|-------------|
| Patch Compliance | > 95% | Weekly | IT Operations |
| Incident Response Time | < 4 hours | Daily | SOC |
| Security Training Completion | 100% | Monthly | HR |
| Vulnerability Remediation | < 30 days | Weekly | Security Team |
| Phishing Test Success Rate | < 5% Click Rate | Quarterly | Security Awareness |

### Key Risk Indicators (KRIs)

| KRI | Threshold | Measurement Frequency | Escalation |
|-----|-----------|----------------------|------------|
| Critical Vulnerabilities | > 10 | Daily | CISO |
| Failed Login Attempts | > 1000/day | Daily | SOC |
| Unpatched Systems | > 5% | Weekly | IT Director |
| Data Exfiltration Attempts | > 0 | Real-time | CISO, Executive Management |

## Reporting

### Board Reports
**Frequency:** Quarterly  
**Content:**
- Executive summary
- Risk profile and trends
- Critical incidents
- Compliance status
- Strategic initiatives
- Budget and resources

**Format:** Presentation + written report

### Management Reports
**Frequency:** Monthly  
**Content:**
- Current risks
- Incident statistics
- KPI/KRI dashboard
- Project progress
- Resource utilization

**Format:** Dashboard + summary

### Operational Reports
**Frequency:** Weekly  
**Content:**
- Security incidents
- Threat intelligence
- Vulnerability status
- Patch compliance
- Anomalies and trends

**Format:** Technical report

## Audit and Compliance

### Internal Audits
**Frequency:** Annually  
**Conducted by:** Internal Audit Department  
**Scope:**
- Policy compliance
- Control effectiveness
- Process adherence
- Documentation

### External Audits
**Frequency:** Annually or as needed  
**Conducted by:** External auditors  
**Scope:**
- Regulatory compliance
- Certifications (ISO 27001, etc.)
- Penetration testing
- Security assessments

### Compliance Monitoring
**Frequency:** Continuous  
**Mechanisms:**
- Automated compliance checks
- Policy violation monitoring
- Access reviews
- Configuration audits

## Continuous Improvement

### Lessons Learned
- Post-incident reviews
- Audit findings analysis
- Best practice sharing
- Process optimization

### Program Assessment
**Frequency:** Annually  
**Methodology:**
- Maturity assessment (NIST CSF)
- Gap analysis
- Industry benchmarking
- Stakeholder feedback

### Improvement Actions
- Prioritization based on risk
- Resource allocation
- Implementation planning
- Progress monitoring

## Escalation Processes

### Incident Escalation
1. **Level 1:** SOC Analyst → SOC Manager
2. **Level 2:** SOC Manager → CISO
3. **Level 3:** CISO → Executive Management
4. **Level 4:** Executive Management → Board

### Risk Escalation
1. **Low/Medium:** Risk Manager
2. **High:** CISO + CRO
3. **Critical:** Executive Management
4. **Existential:** Board of Directors

## Document References

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0040_roles_responsibilities.md
- 0050_policy_framework.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0070
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Supply Chain Risk Management (GV.SC)

## Purpose

This document describes the organization's approach to managing cybersecurity risks in the supply chain, including supplier assessment, contract requirements, and ongoing monitoring.

## Scope

{{ meta.scope }}

## Supply Chain Risk Strategy

### Strategic Objectives
- Identification and assessment of supplier risks
- Minimization of cybersecurity risks through third parties
- Ensuring supplier compliance
- Continuous monitoring of supplier performance

### Risk Categories

| Category | Description | Risk Level |
|----------|-------------|------------|
| Critical Suppliers | Access to critical systems/data | High |
| IT Service Providers | Managed services, Cloud providers | High |
| Software Suppliers | Applications, Components | Medium |
| Hardware Suppliers | IT equipment, Network devices | Medium |
| Other Suppliers | No IT involvement | Low |

## Supplier Lifecycle

### 1. Supplier Selection

**Due Diligence:**
- Security assessment
- Financial stability
- Reputation and references
- Compliance evidence

**Assessment Criteria:**
- ISO 27001 certification
- SOC 2 report
- Data protection compliance (GDPR)
- Incident response capabilities
- Business continuity planning

### 2. Contractual Requirements

**Security Clauses:**
- Non-disclosure agreements (NDA)
- Data protection provisions
- Security requirements
- Audit rights
- Incident reporting obligations
- Liability and insurance

**Service Level Agreements (SLAs):**
- Availability: {{ meta.sla_availability }}
- Incident response time: {{ meta.sla_response_time }}
- Patch management: {{ meta.sla_patch_time }}
- Backup and recovery: {{ meta.sla_recovery_time }}

### 3. Onboarding

**Security Requirements:**
- Access control and authentication
- Network segmentation
- Encryption
- Logging and monitoring
- Training of supplier employees

**Documentation:**
- Security policies
- Access documentation
- Contact information
- Escalation processes

### 4. Ongoing Monitoring

**Monitoring Activities:**
- Quarterly security reviews
- Annual audits
- Continuous compliance monitoring
- Incident tracking
- Performance metrics

**Key Performance Indicators:**
| KPI | Target | Measurement Frequency |
|-----|--------|----------------------|
| SLA Compliance | > 99% | Monthly |
| Security Incidents | 0 critical | Monthly |
| Patch Compliance | > 95% | Monthly |
| Audit Findings | < 5 High | Annually |

### 5. Offboarding

**Process:**
- Access revocation
- Data return/deletion
- Archive documentation
- Lessons learned
- Post-termination contractual obligations

## Supplier Categorization

### Tier 1: Critical Suppliers
**Criteria:**
- Access to critical systems or data
- High dependency
- Difficult to replace

**Requirements:**
- Comprehensive due diligence
- ISO 27001 certification required
- Quarterly reviews
- Annual audits
- Incident response plan required

**Examples:**
- {{ meta.critical_supplier_1 }}
- {{ meta.critical_supplier_2 }}

### Tier 2: Important Suppliers
**Criteria:**
- Access to non-critical systems
- Moderate dependency
- Replaceable with effort

**Requirements:**
- Standard due diligence
- SOC 2 or equivalent
- Semi-annual reviews
- Audits every 2 years

**Examples:**
- {{ meta.important_supplier_1 }}
- {{ meta.important_supplier_2 }}

### Tier 3: Standard Suppliers
**Criteria:**
- No direct system access
- Low dependency
- Easily replaceable

**Requirements:**
- Basic security assessment
- Annual reviews
- Self-assessment

## Risk Assessment

### Assessment Matrix

| Factor | Weight | Rating |
|--------|--------|--------|
| Data Access | 30% | 1-5 |
| System Access | 25% | 1-5 |
| Business Criticality | 20% | 1-5 |
| Compliance Status | 15% | 1-5 |
| Security Maturity | 10% | 1-5 |

**Total Risk = Σ (Factor × Weight)**

### Risk Treatment

| Risk Score | Category | Actions |
|------------|----------|---------|
| 4.0 - 5.0 | Critical | Immediate action, possible contract termination |
| 3.0 - 3.9 | High | Improvement plan required |
| 2.0 - 2.9 | Medium | Monitoring and regular reviews |
| 1.0 - 1.9 | Low | Standard monitoring |

## Incident Management

### Supplier Incidents

**Reporting Requirements:**
- Critical incidents: Immediate (< 1 hour)
- High incidents: < 4 hours
- Medium incidents: < 24 hours
- Low incidents: < 72 hours

**Response Process:**
1. Incident report by supplier
2. Assessment by SOC
3. Response coordination
4. Stakeholder communication
5. Post-incident review
6. Lessons learned

### Escalation
- Critical incidents → CISO + Executive Management
- Data breaches → DPO + Legal
- Contract violations → Procurement + Legal

## Compliance and Audits

### Audit Requirements

**Internal Audits:**
- Tier 1: Annually
- Tier 2: Every 2 years
- Tier 3: Risk-based

**External Audits:**
- ISO 27001 certification (Tier 1)
- SOC 2 reports (Tier 1-2)
- Penetration testing (as needed)

### Compliance Monitoring
- Continuous monitoring of certifications
- Tracking of audit findings
- Review of improvement actions

## Software Supply Chain

### Software Components
- Software Bill of Materials (SBOM)
- Vulnerability scanning
- License compliance
- Update management

### Open Source Software
- Approval process
- Vulnerability monitoring
- License review
- Community support assessment

## Document References

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0050_policy_framework.md
- 0150_supply_chain_risk_management.md (Identify)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0100
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Asset Management (ID.AM)

## Purpose

This document describes the asset management program for identifying and managing data, personnel, devices, systems, and facilities that enable the organization to achieve business objectives.

## Scope

{{ meta.scope }}

## Asset Categories

### 1. Hardware Assets
- Servers and workstations
- Network devices
- Mobile devices
- IoT devices
- Storage systems

### 2. Software Assets
- Operating systems
- Applications
- Databases
- Middleware
- Development tools

### 3. Data Assets
- Customer data
- Financial data
- Intellectual property
- Personnel data
- Trade secrets

### 4. Services and Systems
- Cloud services
- SaaS applications
- Managed services
- Critical business processes

### 5. Personnel
- IT personnel
- Privileged users
- External service providers
- Administrators

## Asset Inventory

### Inventory Process
1. Asset discovery (automated and manual)
2. Asset classification
3. Asset valuation
4. Documentation in CMDB
5. Regular updates

### Asset Attributes
| Attribute | Description | Required |
|-----------|-------------|----------|
| Asset-ID | Unique identifier | Yes |
| Asset-Name | Descriptive name | Yes |
| Asset-Type | Category | Yes |
| Owner | Responsible party | Yes |
| Location | Physical/logical location | Yes |
| Criticality | Business importance | Yes |
| Value | Business value | Yes |
| Status | Active/Inactive/Decommissioned | Yes |

## Asset Classification

### Criticality Levels
| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Business essential | Production systems, Customer databases |
| High | Important for operations | ERP systems, Email servers |
| Medium | Supporting systems | Intranet, Collaboration tools |
| Low | Non-critical systems | Test environments |

### Data Classification
| Classification | Description | Protection Requirements |
|----------------|-------------|------------------------|
| Highly Confidential | Highest sensitivity | Encryption, MFA, Audit logging |
| Confidential | Business sensitive | Access control, Encryption |
| Internal | Employees only | Access control |
| Public | No restrictions | Basic protection |

## Asset Lifecycle

### 1. Acquisition
- Approval process
- Security requirements
- Supplier assessment
- Contract management

### 2. Deployment
- Configuration per standards
- Security hardening
- Inventory registration
- Documentation

### 3. Operation
- Patch management
- Monitoring
- Maintenance
- Change management

### 4. Decommissioning
- Data deletion
- Asset return
- Documentation
- Disposal

## Asset Ownership

### Responsibilities

**Asset Owner:**
- Business responsibility
- Classification
- Access approval
- Compliance

**Asset Custodian (IT):**
- Technical management
- Security controls
- Backup and recovery
- Patch management

**Asset User:**
- Proper use
- Problem reporting
- Policy compliance

## Document References

- 0110_business_environment.md
- 0130_risk_assessment.md
- 0220_data_security.md (Protect)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0110
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Business Environment (ID.BE)

## Purpose

This document describes the organization's business environment, including mission, objectives, stakeholders, and activities to inform cybersecurity decisions.

## Scope

{{ meta.scope }}

## Business Mission and Objectives

### Mission
{{ meta.organization_mission }}

### Strategic Objectives
1. {{ meta.strategic_goal_1 }}
2. {{ meta.strategic_goal_2 }}
3. {{ meta.strategic_goal_3 }}

## Critical Business Processes

| Process | Description | Criticality | Dependencies |
|---------|-------------|-------------|--------------|
| {{ meta.process_1 }} | {{ meta.process_1_desc }} | High | {{ meta.process_1_deps }} |
| {{ meta.process_2 }} | {{ meta.process_2_desc }} | High | {{ meta.process_2_deps }} |
| {{ meta.process_3 }} | {{ meta.process_3_desc }} | Medium | {{ meta.process_3_deps }} |

## Stakeholders

### Internal Stakeholders
- Board and Executive Management
- Employees
- IT Department
- Compliance and Legal

### External Stakeholders
- Customers
- Partners
- Suppliers
- Regulators

## Business Dependencies

### IT Systems
- ERP System: {{ meta.erp_system }}
- CRM System: {{ meta.crm_system }}
- Production Systems: {{ meta.production_systems }}

### External Services
- Cloud Provider: {{ meta.cloud_provider }}
- Managed Services: {{ meta.managed_services }}
- Payment Provider: {{ meta.payment_provider }}

## Document References

- 0020_organizational_context.md (Govern)
- 0100_asset_management.md
- 0130_risk_assessment.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0120
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Governance (ID.GV)

## Purpose

Documentation of cybersecurity governance requirements and their integration into business risk management.

## Scope

{{ meta.scope }}

## Governance Requirements

### Legal and Regulatory Requirements
- GDPR
- {{ meta.regulation_1 }}
- {{ meta.regulation_2 }}

### Cybersecurity Roles
- CISO: Thomas Weber
- CRO: {{ meta.cro }}
- Compliance Manager: {{ meta.compliance_manager }}

## Integration with Risk Management

Cybersecurity governance is integrated into Enterprise Risk Management (ERM).

## Document References

- 0020_organizational_context.md (Govern)
- 0040_roles_responsibilities.md (Govern)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0130
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Risk Assessment (ID.RA)

## Purpose

This document describes the risk assessment process for identifying and evaluating cybersecurity risks.

## Scope

{{ meta.scope }}

## Risk Assessment Process

1. Asset identification
2. Threat identification
3. Vulnerability assessment
4. Impact analysis
5. Risk calculation
6. Risk prioritization

## Document References

- 0030_risk_management_strategy.md (Govern)
- 0100_asset_management.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0140
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Risk Management Strategy (ID.RM)

## Purpose

This document describes the risk management strategy implementation.

## Scope

{{ meta.scope }}

## Risk Management Approach

The organization follows a risk-based approach aligned with the Govern function.

## Document References

- 0030_risk_management_strategy.md (Govern)
- 0130_risk_assessment.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0150
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Supply Chain Risk Management (ID.SC)

## Purpose

This document describes supply chain risk management implementation.

## Scope

{{ meta.scope }}

## Supply Chain Risk Management

Supplier assessment and monitoring processes.

## Document References

- 0070_supply_chain_risk_management.md (Govern)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0200
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Identity Management and Access Control (PR.AA)

## Purpose

This document describes identity management and access control processes.

## Scope

{{ meta.scope }}

## Access Control Principles

- Least Privilege
- Separation of Duties
- Need-to-Know
- Multi-Factor Authentication

## Identity Management

### User Lifecycle
1. Provisioning
2. Access Reviews
3. Deprovisioning

## Document References

- 0050_policy_framework.md (Govern)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0210
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Awareness and Training (PR.AT)

## Purpose

This document describes security awareness and training programs.

## Scope

{{ meta.scope }}

## Training Programs

### Mandatory Training
- New employee orientation
- Annual security awareness
- Role-based training

## Awareness Campaigns

- Monthly security tips
- Phishing simulations
- Security newsletters

## Document References

- 0050_policy_framework.md (Govern)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0220
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Data Security (PR.DS)

## Purpose

This document describes data security controls and processes.

## Scope

{{ meta.scope }}

## Data Protection

### Data Classification
- Highly Confidential
- Confidential
- Internal
- Public

### Protection Measures
- Encryption at rest
- Encryption in transit
- Access controls
- Data loss prevention

## Document References

- 0100_asset_management.md (Identify)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0230
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Information Protection Processes (PR.IP)

## Purpose

This document describes information protection processes and procedures.

## Scope

{{ meta.scope }}

## Protection Processes

- Configuration management
- Change control
- Backup and recovery
- Secure disposal

## Document References

- 0050_policy_framework.md (Govern)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0240
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Maintenance (PR.MA)

## Purpose

This document describes maintenance processes for systems and assets.

## Scope

{{ meta.scope }}

## Maintenance Activities

- Patch management
- System updates
- Hardware maintenance
- Software maintenance

## Document References

- 0100_asset_management.md (Identify)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0250
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Protective Technology (PR.PT)

## Purpose

This document describes protective technology solutions.

## Scope

{{ meta.scope }}

## Protective Technologies

- Firewalls
- Intrusion Prevention Systems
- Antivirus/Antimalware
- Encryption solutions
- DLP solutions

## Document References

- 0220_data_security.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0300
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Anomalies and Events (DE.AE)

## Purpose

This document describes processes for detecting anomalies and security events.

## Scope

{{ meta.scope }}

## Anomaly Detection

### Detection Methods
- Baseline analysis
- Behavioral analytics
- Signature-based detection
- Anomaly-based detection

### Event Categories
- Security events
- System events
- Application events
- Network events

## Document References

- 0310_security_monitoring.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0310
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Security Continuous Monitoring (DE.CM)

## Purpose

This document describes continuous security monitoring processes.

## Scope

{{ meta.scope }}

## Monitoring Activities

### Continuous Monitoring
- Network monitoring
- System monitoring
- Application monitoring
- User activity monitoring

### Monitoring Tools
- SIEM: {{ meta.siem_tool }}
- IDS/IPS: {{ meta.ids_tool }}
- Log management: {{ meta.log_tool }}

## Document References

- 0300_anomalies_events.md
- 0400_response_planning.md (Respond)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0320
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Detection Processes (DE.DP)

## Purpose

This document describes detection processes and procedures.

## Scope

{{ meta.scope }}

## Detection Processes

### Process Components
- Event collection
- Event correlation
- Alert generation
- Alert triage
- Incident escalation

### Detection Effectiveness
- Regular testing
- False positive reduction
- Coverage assessment

## Document References

- 0300_anomalies_events.md
- 0310_security_monitoring.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0400
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Response Planning (RS.RP)

## Purpose

This document describes incident response planning processes.

## Scope

{{ meta.scope }}

## Response Planning

### Incident Response Team
- Incident Response Manager: {{ meta.ir_manager }}
- Security Analysts
- IT Operations
- Legal/Compliance
- Communications

### Response Procedures
- Incident classification
- Escalation procedures
- Communication protocols
- Documentation requirements

## Document References

- 0050_policy_framework.md (Govern)
- 0310_security_monitoring.md (Detect)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0410
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Communications (RS.CO)

## Purpose

This document describes incident response communication processes.

## Scope

{{ meta.scope }}

## Communication Protocols

### Internal Communication
- Incident Response Team
- Executive Management
- Affected Business Units
- IT Operations

### External Communication
- Customers
- Regulators
- Law Enforcement
- Media

## Document References

- 0400_response_planning.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0420
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Analysis (RS.AN)

## Purpose

This document describes incident analysis processes.

## Scope

{{ meta.scope }}

## Analysis Activities

### Incident Analysis
- Root cause analysis
- Impact assessment
- Scope determination
- Evidence collection

### Forensic Analysis
- Digital forensics
- Log analysis
- Malware analysis

## Document References

- 0400_response_planning.md
- 0310_security_monitoring.md (Detect)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0430
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Mitigation (RS.MI)

## Purpose

This document describes incident mitigation and containment processes.

## Scope

{{ meta.scope }}

## Mitigation Activities

### Containment
- Isolation of affected systems
- Network segmentation
- Access restriction

### Eradication
- Malware removal
- Vulnerability patching
- Configuration changes

### Recovery
- System restoration
- Service resumption
- Validation

## Document References

- 0400_response_planning.md
- 0500_recovery_planning.md (Recover)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0440
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Improvements (RS.IM)

## Purpose

This document describes post-incident improvement processes.

## Scope

{{ meta.scope }}

## Improvement Activities

### Post-Incident Review
- Lessons learned
- Process improvements
- Control enhancements
- Training updates

### Metrics and Reporting
- Incident trends
- Response effectiveness
- Time to detect/respond
- Cost of incidents

## Document References

- 0400_response_planning.md
- 0060_oversight.md (Govern)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0500
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Recovery Planning (RC.RP)

## Purpose

This document describes recovery planning processes for restoring systems and services after incidents.

## Scope

{{ meta.scope }}

## Recovery Planning

### Recovery Objectives
- Recovery Time Objective (RTO): {{ meta.rto }}
- Recovery Point Objective (RPO): {{ meta.rpo }}

### Recovery Procedures
- System restoration
- Data recovery
- Service resumption
- Validation and testing

### Business Continuity
- Critical business functions
- Alternative processing sites
- Backup systems
- Communication plans

## Document References

- 0430_mitigation.md (Respond)
- 0110_business_environment.md (Identify)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0510
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Improvements (RC.IM)

## Purpose

This document describes recovery improvement processes.

## Scope

{{ meta.scope }}

## Improvement Activities

### Recovery Process Improvements
- Lessons learned from recovery activities
- Process optimization
- Technology improvements
- Training enhancements

### Recovery Metrics
- Recovery time actual vs. RTO
- Data loss actual vs. RPO
- Recovery success rate
- Cost of recovery

## Document References

- 0500_recovery_planning.md
- 0440_improvements.md (Respond)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0520
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Communications (RC.CO)

## Purpose

This document describes recovery communication processes.

## Scope

{{ meta.scope }}

## Communication During Recovery

### Internal Communication
- Status updates to management
- Communication with affected users
- Coordination with IT teams

### External Communication
- Customer notifications
- Regulatory reporting
- Public relations

### Communication Channels
- Email
- Intranet
- Emergency notification system
- Social media

## Document References

- 0500_recovery_planning.md
- 0410_communications.md (Respond)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0600
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Implementation Tiers

## Purpose

This document describes the NIST CSF implementation tiers and the organization's current tier assessment.

## Scope

{{ meta.scope }}

## Implementation Tiers

### Tier 1: Partial
- Risk management process not formalized
- Limited awareness of cybersecurity risk
- Reactive approach

### Tier 2: Risk Informed
- Risk management practices approved but not organization-wide
- Awareness of cybersecurity risk exists
- Some risk-informed decisions

### Tier 3: Repeatable
- Formal risk management practices
- Organization-wide approach
- Consistent risk-informed decisions

### Tier 4: Adaptive
- Adaptive risk management
- Continuous improvement
- Advanced cybersecurity practices

## Current Tier Assessment

**Current Tier:** {{ meta.current_tier }}

**Target Tier:** {{ meta.target_tier }}

## Document References

- 0030_risk_management_strategy.md (Govern)
- 0630_gap_analysis.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0610
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Current Profile

## Purpose

This document describes the organization's current cybersecurity profile based on NIST CSF 2.0.

## Scope

{{ meta.scope }}

## Current Profile Assessment

### Govern Function
- Current maturity: {{ meta.govern_maturity }}
- Key strengths: {{ meta.govern_strengths }}
- Key gaps: {{ meta.govern_gaps }}

### Identify Function
- Current maturity: {{ meta.identify_maturity }}
- Key strengths: {{ meta.identify_strengths }}
- Key gaps: {{ meta.identify_gaps }}

### Protect Function
- Current maturity: {{ meta.protect_maturity }}
- Key strengths: {{ meta.protect_strengths }}
- Key gaps: {{ meta.protect_gaps }}

### Detect Function
- Current maturity: {{ meta.detect_maturity }}
- Key strengths: {{ meta.detect_strengths }}
- Key gaps: {{ meta.detect_gaps }}

### Respond Function
- Current maturity: {{ meta.respond_maturity }}
- Key strengths: {{ meta.respond_strengths }}
- Key gaps: {{ meta.respond_gaps }}

### Recover Function
- Current maturity: {{ meta.recover_maturity }}
- Key strengths: {{ meta.recover_strengths }}
- Key gaps: {{ meta.recover_gaps }}

## Document References

- 0620_target_profile.md
- 0630_gap_analysis.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0620
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Target Profile

## Purpose

This document describes the organization's target cybersecurity profile based on NIST CSF 2.0.

## Scope

{{ meta.scope }}

## Target Profile

### Govern Function
- Target maturity: {{ meta.govern_target }}
- Priority improvements: {{ meta.govern_priorities }}

### Identify Function
- Target maturity: {{ meta.identify_target }}
- Priority improvements: {{ meta.identify_priorities }}

### Protect Function
- Target maturity: {{ meta.protect_target }}
- Priority improvements: {{ meta.protect_priorities }}

### Detect Function
- Target maturity: {{ meta.detect_target }}
- Priority improvements: {{ meta.detect_priorities }}

### Respond Function
- Target maturity: {{ meta.respond_target }}
- Priority improvements: {{ meta.respond_priorities }}

### Recover Function
- Target maturity: {{ meta.recover_target }}
- Priority improvements: {{ meta.recover_priorities }}

## Document References

- 0610_current_profile.md
- 0630_gap_analysis.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0630
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Gap Analysis

## Purpose

This document describes the gap analysis between current and target cybersecurity profiles.

## Scope

{{ meta.scope }}

## Gap Analysis

### Methodology
1. Compare current vs. target profiles
2. Identify gaps by function and category
3. Prioritize gaps based on risk
4. Estimate resources required

### Identified Gaps

| Function | Category | Current | Target | Priority | Effort |
|----------|----------|---------|--------|----------|--------|
| Govern | GV.OC | 2 | 4 | High | Medium |
| Identify | ID.AM | 3 | 4 | Medium | Low |
| Protect | PR.AA | 2 | 4 | High | High |
| Detect | DE.CM | 3 | 4 | Medium | Medium |
| Respond | RS.RP | 2 | 3 | High | Medium |
| Recover | RC.RP | 2 | 4 | Medium | High |

## Document References

- 0610_current_profile.md
- 0620_target_profile.md
- 0640_action_plan.md

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




---
Document-ID: nist-csf-0640
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Action Plan

## Purpose

This document describes the action plan for closing identified gaps and achieving the target profile.

## Scope

{{ meta.scope }}

## Action Plan

### Prioritized Actions

| Priority | Action | Function | Timeline | Owner | Budget |
|----------|--------|----------|----------|-------|--------|
| 1 | Implement MFA | Protect | Q1 2024 | Thomas Weber | {{ meta.budget_1 }} |
| 2 | Deploy SIEM | Detect | Q2 2024 | {{ meta.security_ops_manager }} | {{ meta.budget_2 }} |
| 3 | Enhance IR plan | Respond | Q1 2024 | {{ meta.ir_manager }} | {{ meta.budget_3 }} |
| 4 | Improve asset inventory | Identify | Q2 2024 | {{ meta.it_director }} | {{ meta.budget_4 }} |

### Implementation Roadmap

**Year 1:**
- High priority gaps
- Quick wins
- Foundation building

**Year 2:**
- Medium priority gaps
- Process maturity
- Technology enhancements

**Year 3:**
- Low priority gaps
- Optimization
- Continuous improvement

## Document References

- 0630_gap_analysis.md
- 0060_oversight.md (Govern)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial creation |




# NIST CSF 2.0 Framework Mapping

## Overview

This document maps the handbook templates to NIST Cybersecurity Framework 2.0 categories and subcategories.

## 1. Govern (GV)

### GV.OC: Organizational Context
**Templates:**
- 0020_organizational_context.md

**Subcategories:**
- GV.OC-01: Organizational context is understood
- GV.OC-02: Legal, regulatory, and contractual requirements are understood
- GV.OC-03: Critical objectives, stakeholders, and activities are understood
- GV.OC-04: Dependencies and critical functions are understood
- GV.OC-05: Organizational resilience objectives are established

### GV.RM: Risk Management Strategy
**Templates:**
- 0030_risk_management_strategy.md

**Subcategories:**
- GV.RM-01: Risk management objectives are established
- GV.RM-02: Risk appetite and risk tolerance are established
- GV.RM-03: Risk management roles and responsibilities are established
- GV.RM-04: Strategic direction informs risk management
- GV.RM-05: Cybersecurity risks are integrated into business decisions
- GV.RM-06: Risk management strategy is communicated
- GV.RM-07: Risk management strategy is regularly reviewed

### GV.RR: Roles, Responsibilities, and Authorities
**Templates:**
- 0040_roles_responsibilities.md

**Subcategories:**
- GV.RR-01: Cybersecurity roles and responsibilities are established
- GV.RR-02: Cybersecurity responsibilities are assigned
- GV.RR-03: Adequate resources are allocated
- GV.RR-04: Cybersecurity responsibilities are integrated into job descriptions

### GV.PO: Policy
**Templates:**
- 0050_policy_framework.md

**Subcategories:**
- GV.PO-01: Cybersecurity policies are established
- GV.PO-02: Policies are communicated
- GV.PO-03: Policies are enforced
- GV.PO-04: Policies are regularly reviewed and updated

### GV.OV: Oversight
**Templates:**
- 0060_oversight.md

**Subcategories:**
- GV.OV-01: Cybersecurity oversight is established
- GV.OV-02: Cybersecurity strategy is monitored
- GV.OV-03: Cybersecurity performance is measured
- GV.OV-04: Cybersecurity risks are reported to leadership

### GV.SC: Supply Chain Risk Management
**Templates:**
- 0070_supply_chain_risk_management.md

**Subcategories:**
- GV.SC-01: Supply chain cybersecurity risks are identified
- GV.SC-02: Suppliers are assessed
- GV.SC-03: Contracts include cybersecurity requirements
- GV.SC-04: Suppliers are monitored
- GV.SC-05: Supplier incidents are managed

## 2. Identify (ID)

### ID.AM: Asset Management
**Templates:**
- 0100_asset_management.md

**Subcategories:**
- ID.AM-01: Physical devices and systems are inventoried
- ID.AM-02: Software platforms and applications are inventoried
- ID.AM-03: Organizational communication and data flows are mapped
- ID.AM-04: External information systems are catalogued
- ID.AM-05: Resources are prioritized based on criticality
- ID.AM-07: Roles and responsibilities for assets are assigned
- ID.AM-08: Systems, hardware, and software are managed by lifecycle

### ID.BE: Business Environment
**Templates:**
- 0110_business_environment.md

**Subcategories:**
- ID.BE-01: Organization's role in the supply chain is identified
- ID.BE-02: Organization's place in critical infrastructure sector is identified
- ID.BE-03: Priorities for organizational mission are established
- ID.BE-04: Dependencies and critical functions are established
- ID.BE-05: Resilience requirements are established

### ID.GV: Governance
**Templates:**
- 0120_governance.md

**Subcategories:**
- ID.GV-01: Cybersecurity policies are established
- ID.GV-02: Cybersecurity roles are assigned
- ID.GV-03: Legal and regulatory requirements are understood
- ID.GV-04: Governance and risk management are integrated

### ID.RA: Risk Assessment
**Templates:**
- 0130_risk_assessment.md

**Subcategories:**
- ID.RA-01: Asset vulnerabilities are identified
- ID.RA-02: Cyber threat intelligence is received
- ID.RA-03: Threats are identified
- ID.RA-04: Potential business impacts are identified
- ID.RA-05: Threats, vulnerabilities, and impacts are used to determine risk
- ID.RA-06: Risk responses are identified and prioritized
- ID.RA-07: Risk assessments are performed
- ID.RA-08: Risk assessments are updated
- ID.RA-09: Risk assessments are communicated
- ID.RA-10: Critical cybersecurity risks are escalated

### ID.RM: Risk Management Strategy
**Templates:**
- 0140_risk_management_strategy.md

**Subcategories:**
- ID.RM-01: Risk management processes are established
- ID.RM-02: Risk tolerance is determined
- ID.RM-03: Risk tolerance is communicated

### ID.SC: Supply Chain Risk Management
**Templates:**
- 0150_supply_chain_risk_management.md

**Subcategories:**
- ID.SC-01: Supply chain partners are identified
- ID.SC-02: Supply chain contracts are established
- ID.SC-03: Suppliers are assessed
- ID.SC-04: Suppliers are monitored
- ID.SC-05: Supplier response plans are established

## 3. Protect (PR)

### PR.AA: Identity Management and Access Control
**Templates:**
- 0200_identity_access_control.md

**Subcategories:**
- PR.AA-01: Identities and credentials are managed for authorized devices
- PR.AA-02: Identities and credentials are managed for authorized users
- PR.AA-03: Identities are verified
- PR.AA-04: Identity and access management is enforced
- PR.AA-05: Physical access is managed
- PR.AA-06: Identities are correlated with credentials

### PR.AT: Awareness and Training
**Templates:**
- 0210_awareness_training.md

**Subcategories:**
- PR.AT-01: All users are trained in cybersecurity awareness
- PR.AT-02: Privileged users understand their roles
- PR.AT-03: Third-party stakeholders understand their roles
- PR.AT-04: Senior executives understand their roles
- PR.AT-05: Physical and cybersecurity personnel understand their roles

### PR.DS: Data Security
**Templates:**
- 0220_data_security.md

**Subcategories:**
- PR.DS-01: Data at rest is protected
- PR.DS-02: Data in transit is protected
- PR.DS-03: Assets are formally managed
- PR.DS-04: Adequate capacity is maintained
- PR.DS-05: Protection against data leaks is implemented
- PR.DS-06: Integrity checking mechanisms are used
- PR.DS-07: Development and testing environments are separated
- PR.DS-08: Integrity checks are performed
- PR.DS-10: Confidentiality, integrity, and availability are enforced
- PR.DS-11: Data is managed according to retention requirements

### PR.IP: Information Protection Processes
**Templates:**
- 0230_information_protection_processes.md

**Subcategories:**
- PR.IP-01: Baseline configurations are created
- PR.IP-02: System development lifecycle is managed
- PR.IP-03: Configuration change control is implemented
- PR.IP-04: Backups are performed
- PR.IP-05: Policies for physical operating environment are met
- PR.IP-06: Data is securely disposed
- PR.IP-07: Protection processes are continuously improved
- PR.IP-08: Effectiveness of protection technologies is shared
- PR.IP-09: Response plans are managed
- PR.IP-10: Response plans are tested
- PR.IP-11: Cybersecurity is integrated into HR practices
- PR.IP-12: Vulnerability management plan is developed

### PR.MA: Maintenance
**Templates:**
- 0240_maintenance.md

**Subcategories:**
- PR.MA-01: Maintenance is performed
- PR.MA-02: Remote maintenance is approved and logged

### PR.PT: Protective Technology
**Templates:**
- 0250_protective_technology.md

**Subcategories:**
- PR.PT-01: Audit/log records are determined
- PR.PT-02: Removable media is protected
- PR.PT-03: Least functionality is configured
- PR.PT-04: Communications and control networks are protected
- PR.PT-05: Mechanisms are implemented to achieve resilience

## 4. Detect (DE)

### DE.AE: Anomalies and Events
**Templates:**
- 0300_anomalies_events.md

**Subcategories:**
- DE.AE-01: Network baseline is established
- DE.AE-02: Detected events are analyzed
- DE.AE-03: Event data is aggregated
- DE.AE-04: Impact of events is determined
- DE.AE-06: Information about threats is received
- DE.AE-07: Threat data is used
- DE.AE-08: Incident thresholds are established

### DE.CM: Security Continuous Monitoring
**Templates:**
- 0310_security_monitoring.md

**Subcategories:**
- DE.CM-01: Network is monitored
- DE.CM-02: Physical environment is monitored
- DE.CM-03: Personnel activity is monitored
- DE.CM-04: Malicious code is detected
- DE.CM-06: External service provider activity is monitored
- DE.CM-07: Unauthorized activity is monitored
- DE.CM-09: Vulnerabilities are identified

### DE.DP: Detection Processes
**Templates:**
- 0320_detection_processes.md

**Subcategories:**
- DE.DP-01: Roles and responsibilities for detection are defined
- DE.DP-02: Detection activities comply with requirements
- DE.DP-03: Detection processes are tested
- DE.DP-04: Event detection information is communicated
- DE.DP-05: Detection processes are continuously improved

## 5. Respond (RS)

### RS.RP: Response Planning
**Templates:**
- 0400_response_planning.md

**Subcategories:**
- RS.RP-01: Response plan is executed

### RS.CO: Communications
**Templates:**
- 0410_communications.md

**Subcategories:**
- RS.CO-01: Personnel know their roles
- RS.CO-02: Incidents are reported
- RS.CO-03: Information is shared
- RS.CO-04: Coordination with stakeholders occurs
- RS.CO-05: Voluntary information sharing occurs

### RS.AN: Analysis
**Templates:**
- 0420_analysis.md

**Subcategories:**
- RS.AN-01: Notifications are investigated
- RS.AN-02: Impact of incidents is understood
- RS.AN-03: Forensics are performed
- RS.AN-04: Incidents are categorized
- RS.AN-05: Processes are established

### RS.MI: Mitigation
**Templates:**
- 0430_mitigation.md

**Subcategories:**
- RS.MI-01: Incidents are contained
- RS.MI-02: Incidents are eradicated
- RS.MI-03: Newly identified vulnerabilities are mitigated

### RS.IM: Improvements
**Templates:**
- 0440_improvements.md

**Subcategories:**
- RS.IM-01: Response plans incorporate lessons learned
- RS.IM-02: Response strategies are updated

## 6. Recover (RC)

### RC.RP: Recovery Planning
**Templates:**
- 0500_recovery_planning.md

**Subcategories:**
- RC.RP-01: Recovery plan is executed

### RC.IM: Improvements
**Templates:**
- 0510_improvements.md

**Subcategories:**
- RC.IM-01: Recovery plans incorporate lessons learned
- RC.IM-02: Recovery strategies are updated

### RC.CO: Communications
**Templates:**
- 0520_communications.md

**Subcategories:**
- RC.CO-01: Public relations are managed
- RC.CO-02: Reputation is repaired
- RC.CO-03: Recovery activities are communicated

## 7. Implementation and Assessment

### Implementation Tiers
**Templates:**
- 0600_implementation_tiers.md

**Description:**
Assessment of organizational cybersecurity maturity across four tiers (Partial, Risk Informed, Repeatable, Adaptive).

### Profiles
**Templates:**
- 0610_current_profile.md - Current state
- 0620_target_profile.md - Target state
- 0630_gap_analysis.md - Gap analysis
- 0640_action_plan.md - Action plan

**Description:**
Profiles enable assessment of current cybersecurity posture and planning for improvements.

## Coverage

These templates cover all core functions and categories of NIST CSF 2.0. Organizations should adapt the templates to their specific requirements and risk profiles.


# NIST Cybersecurity Framework 2.0 Handbook Templates

## Overview

This directory contains templates for creating a NIST Cybersecurity Framework (CSF) 2.0 handbook. The templates cover all six core functions of the framework: Govern, Identify, Protect, Detect, Respond, and Recover.

## NIST CSF 2.0 Structure

The NIST Cybersecurity Framework 2.0 is a voluntary framework consisting of standards, guidelines, and best practices to manage cybersecurity risks. Version 2.0 introduces the new **Govern** function, which provides the foundation for all other functions.

### The Six Core Functions

1. **Govern (GV)**: Establishes and monitors the organization's cybersecurity risk management strategy
2. **Identify (ID)**: Develops organizational understanding to manage cybersecurity risks
3. **Protect (PR)**: Develops and implements protective measures
4. **Detect (DE)**: Develops and implements activities to detect cybersecurity events
5. **Respond (RS)**: Develops and implements activities to respond to detected cybersecurity incidents
6. **Recover (RC)**: Develops and implements activities to restore capabilities after cybersecurity incidents

## Template Organization

Templates are organized by function and use a numeric prefix system:

### Govern Function (0010-0099)
- `0010_govern_overview.md` - Overview of the Govern function
- `0020_organizational_context.md` - Organizational Context (GV.OC)
- `0030_risk_management_strategy.md` - Risk Management Strategy (GV.RM)
- `0040_roles_responsibilities.md` - Roles and Responsibilities (GV.RR)
- `0050_policy_framework.md` - Policy Framework (GV.PO)
- `0060_oversight.md` - Oversight and Monitoring (GV.OV)
- `0070_supply_chain_risk_management.md` - Supply Chain Risk Management (GV.SC)

### Identify Function (0100-0199)
- `0100_asset_management.md` - Asset Management (ID.AM)
- `0110_business_environment.md` - Business Environment (ID.BE)
- `0120_governance.md` - Governance (ID.GV)
- `0130_risk_assessment.md` - Risk Assessment (ID.RA)
- `0140_risk_management_strategy.md` - Risk Management Strategy (ID.RM)
- `0150_supply_chain_risk_management.md` - Supply Chain Risk Management (ID.SC)

### Protect Function (0200-0299)
- `0200_identity_access_control.md` - Identity Management and Access Control (PR.AA)
- `0210_awareness_training.md` - Awareness and Training (PR.AT)
- `0220_data_security.md` - Data Security (PR.DS)
- `0230_information_protection_processes.md` - Information Protection Processes (PR.IP)
- `0240_maintenance.md` - Maintenance (PR.MA)
- `0250_protective_technology.md` - Protective Technology (PR.PT)

### Detect Function (0300-0399)
- `0300_anomalies_events.md` - Anomalies and Events (DE.AE)
- `0310_security_monitoring.md` - Security Continuous Monitoring (DE.CM)
- `0320_detection_processes.md` - Detection Processes (DE.DP)

### Respond Function (0400-0499)
- `0400_response_planning.md` - Response Planning (RS.RP)
- `0410_communications.md` - Communications (RS.CO)
- `0420_analysis.md` - Analysis (RS.AN)
- `0430_mitigation.md` - Mitigation (RS.MI)
- `0440_improvements.md` - Improvements (RS.IM)

### Recover Function (0500-0599)
- `0500_recovery_planning.md` - Recovery Planning (RC.RP)
- `0510_improvements.md` - Improvements (RC.IM)
- `0520_communications.md` - Communications (RC.CO)

### Implementation and Assessment (0600-0699)
- `0600_implementation_tiers.md` - Implementation Tiers
- `0610_current_profile.md` - Current Profile
- `0620_target_profile.md` - Target Profile
- `0630_gap_analysis.md` - Gap Analysis
- `0640_action_plan.md` - Action Plan

## Numbering Scheme

- Templates use 4-digit prefixes (e.g., 0010, 0020, 0030)
- Increments of 10 allow for future insertions
- Functions are grouped in hundred ranges (0000-0099, 0100-0199, etc.)

## Placeholder System

Templates use placeholders for organization-specific data:

### Metadata Placeholders
- `{{ meta.owner }}` - Document owner
- `{{ meta.version }}` - Version number
- `{{ meta.date }}` - Date
- `{{ meta.organization }}` - Organization name
- `Thomas Weber` - CISO name
- `{{ meta.cro }}` - CRO name

### Data Source Placeholders
- `{{ source.organization_name }}` - Organization name from data source
- `{{ source.author }}` - Author from data source
- Additional organization-specific fields

## Customizing Templates

### 1. Update Metadata
Start with the `0000_metadata_en_nist-csf.md` file and fill in the metadata.

### 2. Replace Placeholders
Replace all `{{ placeholder }}` with your organization-specific information.

### 3. Adapt Content
Customize templates to your specific requirements:
- Add organization-specific processes
- Remove non-applicable sections
- Expand sections as needed

### 4. Update Document References
Ensure all cross-references between documents are correct.

## Using with Handbook Generator

These templates are designed for use with the handbook generator system:

```bash
python handbook-generator --template nist-csf --language en --output-format html
```

Supported output formats:
- HTML (mini-website with navigation)
- PDF (with table of contents)
- Markdown (combined or separate files)

## Framework Reference

For more information about NIST Cybersecurity Framework 2.0:
- [NIST CSF 2.0 Website](https://www.nist.gov/cyberframework)
- [NIST CSF 2.0 Framework](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)

## Framework Mapping

See `FRAMEWORK_MAPPING.md` for detailed mapping of templates to NIST CSF 2.0 categories and subcategories.

## License

These templates are based on the NIST Cybersecurity Framework 2.0, which is in the public domain.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024 | Initial version based on NIST CSF 2.0 |
