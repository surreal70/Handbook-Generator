# Compliance and Audits

**Document-ID:** [FRAMEWORK]-0280
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

## Purpose and Scope

This document describes the compliance and audit processes for {{ meta-organisation.name }}. It defines relevant standards, audit processes, compliance controls, evidence, and non-compliance risks to ensure adherence to regulatory and contractual requirements.

**Scope:** All IT systems, processes, and activities of {{ meta-organisation.name }}

**Responsible:** {{ meta-organisation-roles.role_Compliance_Manager }} ({{ meta-handbook.compliance_officer_email }})

## Compliance Fundamentals

### Compliance Definition

**Compliance:** Adherence to laws, regulations, standards, policies, and contractual obligations

**Objectives:**
- **Legal Certainty:** Avoidance of legal consequences
- **Risk Minimization:** Reduction of compliance risks
- **Reputation:** Protection of company reputation
- **Trust:** Trust of customers and partners
- **Competitive Advantage:** Certifications as differentiator

### Compliance Areas

**Regulatory Compliance:**
- Legal requirements (GDPR, IT Security Act)
- Industry-specific regulations
- Data protection requirements

**Standard Compliance:**
- ISO standards (ISO 27001, ISO 20000)
- Industry standards (PCI-DSS, HIPAA)
- Best practice frameworks (ITIL, COBIT)

**Contractual Compliance:**
- Service Level Agreements (SLAs)
- Customer contracts
- Supplier contracts

**Internal Compliance:**
- Company policies
- IT guidelines
- Security standards

## Relevant Standards and Regulations

### ISO/IEC 27001:2013 - Information Security Management

**Description:** International standard for Information Security Management Systems (ISMS)

**Scope:** All IT systems and information processing

**Status:** {{ meta-handbook.iso27001_status }}  
**Certification:** {{ meta-handbook.iso27001_certification }}  
**Certification Body:** {{ meta-handbook.iso27001_certifier }}  
**Valid Until:** {{ meta-handbook.iso27001_valid_until }}

**Core Requirements:**
- Establish, implement, operate, monitor, review, maintain, and improve ISMS
- Risk assessment and treatment
- 114 controls in 14 categories (Annex A)
- Management review and continuous improvement

**Audit Frequency:**
- **Certification Audit:** Every 3 years
- **Surveillance Audit:** Annually
- **Internal Audit:** Quarterly

**Responsible:** {{ meta-organisation-roles.role_CISO }}

### ISO/IEC 20000-1:2018 - IT Service Management

**Description:** International standard for IT Service Management Systems (SMS)

**Scope:** IT service management processes

**Status:** {{ meta-handbook.iso20000_status }}

**Core Requirements:**
- Service Management System (SMS)
- Service planning and delivery
- Relationship processes
- Resolution processes
- Control processes

**Alignment:** ITIL v4 Framework

**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

### GDPR - General Data Protection Regulation

**Description:** EU regulation for the protection of personal data

**Scope:** All processing of personal data

**Effective:** May 25, 2018

**Core Requirements:**
- Lawfulness of processing (Art. 6)
- Information obligations (Art. 13, 14)
- Data subject rights (Art. 15-22)
- Technical and organizational measures (Art. 32)
- Breach notification obligation (Art. 33, 34)
- Data protection impact assessment (Art. 35)

**Fines:** Up to 20 million EUR or 4% of worldwide annual revenue

**Data Protection Officer:** {{ meta-handbook.data_protection_officer }}

**Record of Processing Activities:** {{ meta-handbook.processing_activities_register }}

### BSI IT-Grundschutz

**Description:** Methodology of the German Federal Office for Information Security

**Scope:** IT security

**Status:** {{ meta-handbook.bsi_grundschutz_status }}

**Protection Levels:**
- **Basic Protection:** Standard security measures
- **Core Protection:** Enhanced security requirements
- **Standard Protection:** Complete implementation

**Building Blocks:** IT-Grundschutz Compendium

**Responsible:** {{ meta-organisation-roles.role_CISO }}

### PCI-DSS (Payment Card Industry Data Security Standard)

**Description:** Security standard for credit card data processing

**Scope:** Systems that process, store, or transmit credit card data

**Status:** {{ meta-handbook.pci_dss_status }}

**12 Requirements:**
1. Firewall configuration
2. No default passwords
3. Protection of stored cardholder data
4. Encryption during transmission
5. Antivirus software
6. Secure systems and applications
7. Access restriction (Need-to-Know)
8. Unique IDs for access
9. Restrict physical access
10. Tracking and monitoring
11. Regular security tests
12. Information security policy

**Compliance Level:** {{ meta-handbook.pci_dss_level }}  
**QSA (Qualified Security Assessor):** {{ meta-handbook.pci_dss_qsa }}

### SOX (Sarbanes-Oxley Act)

**Description:** US law for financial reporting

**Scope:** Finance-relevant IT systems (if publicly traded)

**Status:** {{ meta-handbook.sox_status }}

**IT-relevant Requirements:**
- Section 302: Management responsibility for internal controls
- Section 404: Assessment of internal controls
- Section 409: Timely disclosure
- IT General Controls (ITGC)
- Application Controls

**Responsible:** {{ meta-organisation-roles.role_CFO }}

### COBIT 2019

**Description:** Framework for IT governance and management

**Scope:** IT governance

**Status:** {{ meta-handbook.cobit_status }}

**Governance Objectives:**
- EDM01: Ensured Governance Framework Setting and Maintenance
- EDM02: Ensured Benefits Delivery
- EDM03: Ensured Risk Optimization
- EDM04: Ensured Resource Optimization
- EDM05: Ensured Stakeholder Engagement

**Management Objectives:** 40 objectives in 5 domains (APO, BAI, DSS, MEA, EDM)

### Industry-Specific Regulations

**Telecommunications:**
- Telecommunications Act (TKG)
- Data retention

**Healthcare:**
- HIPAA (Health Insurance Portability and Accountability Act)
- Patient Data Protection Act

**Financial Sector:**
- MaRisk (Minimum Requirements for Risk Management)
- BAIT (Supervisory Requirements for IT)

**Energy:**
- IT Security Catalog according to § 11 Para. 1a EnWG

## Compliance Management Process

### Process Overview

```
┌─────────────────┐
│ Compliance      │
│ Identification  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Gap             │
│ Analysis        │
└────────┬────────┘
         │
┌────────▼────────┐
│ Remediation     │
│ Planning        │
└────────┬────────┘
         │
┌────────▼────────┐
│ Implementation  │
│ & Monitoring    │
└────────┬────────┘
         │
┌────────▼────────┐
│ Audit &         │
│ Assessment      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Continuous      │
│ Improvement     │
└─────────────────┘
```

### 1. Compliance Identification

**Activities:**
- Identify relevant laws and regulations
- Determine applicable standards
- Capture contractual obligations
- Define internal policies

**Sources:**
- Legal department
- Industry associations
- Customer requirements
- Management directives

**Documentation:** Compliance register

**Responsible:** Compliance Officer

### 2. Gap Analysis

**Activities:**
- Capture current state
- Define target state
- Identify gaps
- Assess risks
- Prioritization

**Methods:**
- Self-assessment
- Compliance scans
- Document review
- Interviews

**Output:** Gap analysis report

**Responsible:** Compliance team, departments

### 3. Remediation Planning

**Activities:**
- Define measures
- Assign responsibilities
- Create timelines
- Plan budget
- Manage risks

**Prioritization:**
- **Critical:** Immediate (< 30 days)
- **High:** Short-term (< 90 days)
- **Medium:** Mid-term (< 180 days)
- **Low:** Long-term (< 365 days)

**Output:** Remediation plan

**Responsible:** Compliance Officer, department heads

### 4. Implementation & Monitoring

**Activities:**
- Implement measures
- Monitor progress
- Escalate issues
- Maintain documentation

**Monitoring:**
- Weekly status updates
- Monthly reviews
- Quarterly management reports

**Tools:**
- Compliance management system
- Ticketing system
- Project management tools

**Responsible:** Departments, compliance team

### 5. Audit & Assessment

**Activities:**
- Conduct internal audits
- Coordinate external audits
- Document findings
- Plan corrective actions

**Audit Types:**
- Internal audits
- External audits (certification)
- Customer audits
- Regulatory audits

**Responsible:** Internal audit, external auditors

### 6. Continuous Improvement

**Activities:**
- Document lessons learned
- Optimize processes
- Implement best practices
- Conduct training

**Methods:**
- PDCA cycle (Plan-Do-Check-Act)
- Root cause analysis
- Benchmarking

**Responsible:** Compliance Officer, management

## Audit Processes

### Audit Types

#### Internal Audits

**Purpose:** Self-assessment of compliance

**Frequency:**
- **ISO 27001:** Quarterly
- **ISO 20000:** Quarterly
- **GDPR:** Semi-annually
- **Internal Policies:** Annually

**Execution:**
- Internal Audit Team
- Independent from audited area
- Risk-based approach

**Process:**
1. Audit planning
2. Audit preparation
3. Audit execution (Interviews, document review, tests)
4. Document findings
5. Create audit report
6. Plan corrective actions
7. Follow-up

**Responsible:** Internal Audit Team

#### External Audits (Certification)

**Purpose:** Certification according to standards

**Frequency:**
- **Certification Audit:** Every 3 years
- **Surveillance Audit:** Annually
- **Re-certification:** Every 3 years

**Execution:**
- Accredited certification body
- Independent auditors
- Document review and on-site audit

**Audit Phases:**
- **Stage 1:** Document review
- **Stage 2:** On-site audit
- **Surveillance:** Annual monitoring

**Certification Bodies:**
- ISO 27001: {{ meta-handbook.iso27001_certifier }}
- ISO 20000: {{ meta-handbook.iso20000_certifier }}

#### Customer Audits

**Purpose:** Proof of compliance to customers

**Frequency:** As per customer requirements

**Execution:**
- Customer auditors
- On-site or remote
- Focus on contractual requirements

**Preparation:**
- Clarify audit scope
- Provide documentation
- Designate contacts
- Prepare facilities

**Responsible:** Account Manager, Compliance Officer

#### Regulatory Audits

**Purpose:** Review by supervisory authorities

**Frequency:** Ad-hoc or regular (depending on regulation)

**Execution:**
- Supervisory authorities (e.g., data protection authority, BaFin)
- Announced or unannounced
- Comprehensive review

**Examples:**
- Data protection authority (GDPR compliance)
- BaFin (financial sector)
- Federal Network Agency (telecommunications)

**Preparation:**
- Keep documentation current
- Establish processes
- Define contacts

### Audit Preparation

**Checklist:**
- [ ] Audit scope defined
- [ ] Audit plan created
- [ ] Documentation updated
- [ ] Contacts designated
- [ ] Facilities prepared
- [ ] IT systems accessible
- [ ] Stakeholders informed
- [ ] Pre-audit meeting conducted

**Documentation:**
- Policies and procedures
- Risk assessments
- Asset inventory
- Network diagrams
- Access controls
- Incident reports
- Change logs
- Audit logs
- Training records
- Vendor contracts

**Responsible:** Compliance Officer, departments

### Audit Execution

**Audit Methods:**

#### Document Review

**Activities:**
- Review policies and procedures
- Documentation completeness
- Document currency
- Consistency

#### Interviews

**Activities:**
- Employee interviews
- Management interviews
- Check process understanding
- Assess awareness level

**Interview Partners:**
- Management
- IT Operations
- Security team
- Developers
- End users

#### System Tests

**Activities:**
- Configuration reviews
- Test access controls
- Log reviews
- Vulnerability scans
- Penetration tests (if in scope)

#### Observations

**Activities:**
- Process observations
- Workplace inspections
- Check physical security
- Behavioral compliance

### Audit Findings

**Finding Categories:**

| Category | Description | Example |
|---|---|---|
| **Critical** | Severe non-compliance | Missing encryption of sensitive data |
| **Major** | Significant non-compliance | Incomplete documentation |
| **Minor** | Minor deviations | Outdated documents |
| **Observation** | Improvement potential | Process optimization possible |

**Finding Documentation:**
- Finding ID
- Category (Critical/Major/Minor/Observation)
- Description
- Affected systems/processes
- Requirement (standard reference)
- Evidence
- Risk assessment
- Recommended corrective action

**Example Finding:**
```
Finding-ID: AUD-2024-001
Category: Major
Description: Password policy not enforced
Requirement: ISO 27001 A.9.4.3
Evidence: 15 of 50 accounts without password expiration
Risk: High (Unauthorized Access)
Recommendation: Enforce password policy via GPO
Deadline: 30 days
```

### Corrective Actions

**Corrective Action Process:**

1. **Finding Review**
   - Understand finding
   - Identify root cause
   - Assess impact

2. **Action Planning**
   - Define measures
   - Designate responsible parties
   - Create timeline
   - Plan resources

3. **Implementation**
   - Implement measures
   - Monitor progress
   - Maintain documentation

4. **Verification**
   - Check effectiveness
   - Collect evidence
   - Inform auditor

5. **Closure**
   - Close finding
   - Lessons learned
   - Process improvement

**Corrective Action Plan:**

| Finding-ID | Measure | Responsible | Deadline | Status |
|---|---|---|---|---|
| AUD-2024-001 | GPO for password policy | IT Admin | 30 days | In Progress |
| AUD-2024-002 | Update documentation | Compliance | 14 days | Completed |

**Tracking:** Compliance management system

### Audit Reporting

**Audit Report Contents:**
- Executive summary
- Audit scope and methodology
- Findings (by category)
- Positive observations
- Corrective action plan
- Recommendations
- Conclusion

**Report Recipients:**
- Management
- Audit committee
- Affected departments
- External auditors (for follow-up)

**Confidentiality:** Confidential

## Compliance Controls and Evidence

### Technical Controls

#### Access Control

**Controls:**
- Multi-Factor Authentication (MFA)
- Role-Based Access Control (RBAC)
- Least Privilege Principle
- Privileged Access Management (PAM)
- Access Reviews (quarterly)

**Evidence:**
- Access Control Matrix
- User Access Reports
- Access Review Protocols
- MFA Activation Rate

#### Encryption

**Controls:**
- Encryption at Rest (AES-256)
- Encryption in Transit (TLS 1.3)
- Key Management
- Certificate Management

**Evidence:**
- Encryption Inventory
- Key Management Procedures
- Certificate Inventory
- Encryption Scan Reports

#### Logging and Monitoring

**Controls:**
- Central log collection
- SIEM monitoring
- Audit trails
- Log retention (per policy)

**Evidence:**
- Log collection status
- SIEM use cases
- Audit log samples
- Retention compliance reports

#### Vulnerability Management

**Controls:**
- Regular vulnerability scans
- Patch management
- Penetration tests
- Security assessments

**Evidence:**
- Scan reports
- Patch compliance reports
- Pentest reports
- Remediation tracking

### Organizational Controls

#### Policies and Procedures

**Controls:**
- Documented policies
- Regular reviews
- Management approval
- Communication to employees

**Evidence:**
- Policy documents
- Review protocols
- Approval signatures
- Communication evidence

#### Training and Awareness

**Controls:**
- Security awareness training
- Role-specific training
- Phishing simulations
- Training tracking

**Evidence:**
- Training records
- Attendance lists
- Phishing simulation results
- Awareness campaign documentation

#### Incident Management

**Controls:**
- Incident response plan
- Incident tracking
- Post-incident reviews
- Lessons learned process

**Evidence:**
- Incident reports
- Response timelines
- Post-incident review protocols
- Improvement actions

#### Change Management

**Controls:**
- Change approval process
- Change Advisory Board (CAB)
- Change documentation
- Rollback procedures

**Evidence:**
- Change tickets
- CAB meeting protocols
- Change success rate
- Rollback documentation

### Physical Controls

#### Access Control

**Controls:**
- Badge system
- Visitor management
- Video surveillance
- Alarm systems

**Evidence:**
- Access logs
- Visitor logs
- Video recordings (if permitted)
- Alarm protocols

#### Environmental Controls

**Controls:**
- Air conditioning
- UPS (Uninterruptible Power Supply)
- Fire protection
- Water protection

**Evidence:**
- Maintenance protocols
- UPS test protocols
- Fire protection drills
- Environmental monitoring logs

## Non-Compliance Risks and Measures

### Risk Categories

#### Legal Risks

**Risks:**
- Fines and penalties
- Legal proceedings
- Liability claims
- Executive liability

**Examples:**
- GDPR violation: Up to 20 million EUR or 4% annual revenue
- PCI-DSS violation: Up to $500,000 per month
- SOX violation: Criminal consequences

**Mitigations:**
- Establish compliance program
- Regular audits
- Involve legal counsel
- Insurance (Cyber insurance)

#### Financial Risks

**Risks:**
- Fines
- Contractual penalties
- Revenue losses
- Increased insurance premiums

**Examples:**
- SLA violations: Contractual penalties
- Certification loss: Customer loss
- Data breach: Damages

**Mitigations:**
- Risk assessment
- Financial reserves
- Insurance
- Contract management

#### Reputation Risks

**Risks:**
- Loss of trust
- Negative press
- Customer churn
- Difficulties in acquiring new customers

**Examples:**
- Data breach publicly known
- Compliance violations in media
- Certification withdrawal

**Mitigations:**
- Proactive communication
- Crisis management plan
- PR strategy
- Transparency

#### Operational Risks

**Risks:**
- Service interruptions
- Inefficient processes
- Employee frustration
- Vendor issues

**Examples:**
- Audit findings lead to service changes
- Compliance requirements delay projects
- Additional documentation effort

**Mitigations:**
- Compliance by design
- Process automation
- Training and awareness
- Vendor management

### Risk Management

**Risk Assessment:**

| Likelihood | Impact | Risk Level | Measures |
|---|---|---|---|
| **High** | **High** | Critical | Immediate measures |
| **High** | **Medium** | High | Short-term measures |
| **Medium** | **High** | High | Short-term measures |
| **Medium** | **Medium** | Medium | Mid-term measures |
| **Low** | **High** | Medium | Monitoring |
| **Low** | **Medium** | Low | Accept or monitor |
| **Low** | **Low** | Very low | Accept |

**Risk Treatment Options:**
- **Avoid:** Avoid risk (discontinue activity)
- **Mitigate:** Reduce risk (implement controls)
- **Transfer:** Transfer risk (insurance, outsourcing)
- **Accept:** Accept risk (with management approval)

**Risk Register:** {{ meta-handbook.risk_register }}

### Incident Response for Non-Compliance

**Process:**

1. **Detection**
   - Non-compliance identified
   - Assess severity
   - Inform stakeholders

2. **Assessment**
   - Determine scope
   - Analyze impact
   - Check reporting obligations

3. **Containment**
   - Immediate measures
   - Prevent further violations
   - Start documentation

4. **Remediation**
   - Corrective actions
   - Root cause analysis
   - Preventive actions

5. **Reporting**
   - Internal reporting
   - External reporting (if required)
   - Management briefing

6. **Lessons Learned**
   - Post-incident review
   - Process improvements
   - Training updates

## Compliance Metrics and Reporting

### Key Performance Indicators (KPIs)

| KPI | Target | Measurement | Frequency |
|---|---|---|---|
| **Audit Findings Rate** | < 5 Major Findings | Findings per audit | After audit |
| **Corrective Action Closure Rate** | > 95% on time | Closed CAs / Total CAs | Monthly |
| **Training Completion Rate** | 100% | Completed trainings / Required trainings | Quarterly |
| **Policy Review Compliance** | 100% | Reviewed policies / Total policies | Annually |
| **Incident Reporting Time** | < 24h | Time from incident to report | Per incident |
| **Vulnerability Remediation SLA** | > 95% | Remediated in SLA / Total | Monthly |

### Compliance Dashboard

**Metrics:**
- Compliance status by standard
- Open audit findings
- Corrective actions status
- Training completion rate
- Policy review status
- Incident trends

**Tool:** {{ meta-handbook.compliance_dashboard }}

**Access:** Management, compliance team, auditors

### Reporting

#### Monthly Compliance Status Report

**Contents:**
- Compliance status overview
- New findings
- Corrective actions progress
- Upcoming audits
- Risks and issues

**Recipients:** Compliance Officer, management

#### Quarterly Compliance Management Report

**Contents:**
- Compliance KPIs
- Audit summary
- Risk assessment
- Training status
- Budget and resources
- Strategic recommendations

**Recipients:** Management, audit committee, board

#### Annual Compliance Review

**Contents:**
- Year in review
- Certification status
- Compliance program effectiveness
- Lessons learned
- Strategic planning for next year
- Budget planning

**Recipients:** Management, board, stakeholders

## Compliance Tools and Systems

### Governance, Risk, and Compliance (GRC) Platform

**System:** {{ meta-handbook.grc_system }}  
**Version:** [TODO]  
**Management URL:** {{ meta-handbook.grc_url }}

**Functions:**
- Compliance management
- Risk management
- Audit management
- Policy management
- Incident management
- Reporting and dashboards

### Document Management

**System:** {{ meta-handbook.document_management_system }}

**Functions:**
- Central document repository
- Version control
- Approval workflows
- Access control
- Audit trail

**Document Types:**
- Policies and procedures
- Audit reports
- Compliance evidence
- Training materials
- Contracts

### Compliance Scanning Tools

**Vulnerability Scanner:** {{ meta-handbook.vulnerability_scanner }}  
**Configuration Scanner:** {{ meta-handbook.config_scanner }}  
**Compliance Scanner:** {{ meta-handbook.compliance_scanner }}

**Functions:**
- Automatic compliance checks
- Configuration audits
- Benchmark comparisons (CIS, STIG)
- Continuous compliance monitoring

### Training Management

**System:** {{ meta-handbook.training_system }}

**Functions:**
- Training catalog
- Enrollment and tracking
- Certificates
- Reporting
- Phishing simulations

## Roles and Responsibilities

### Compliance Officer

**Responsibilities:**
- Compliance program ownership
- Compliance strategy
- Audit coordination
- Risk management
- Reporting to management

**Person:** {{ meta-organisation-roles.role_Compliance_Manager }}

### Data Protection Officer (DPO)

**Responsibilities:**
- GDPR compliance
- Data protection consulting
- Monitoring data processing
- Cooperation with supervisory authorities
- Training

**Person:** {{ meta-handbook.data_protection_officer }}

### Internal Audit Team

**Responsibilities:**
- Conduct internal audits
- Audit planning
- Document findings
- Follow-up on corrective actions

**Team Lead:** {{ meta-handbook.internal_audit_lead }}

### CISO (Chief Information Security Officer)

**Responsibilities:**
- Security compliance
- ISO 27001 ownership
- Security audits
- Risk management

**Person:** {{ meta-organisation-roles.role_CISO }}

### IT Operations Manager

**Responsibilities:**
- Operational compliance implementation
- ISO 20000 ownership
- Process compliance
- Tool implementation

**Person:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

### Department Heads

**Responsibilities:**
- Compliance in their area
- Employee training
- Corrective actions implementation
- Documentation

## Best Practices

### Compliance Best Practices

1. **Compliance by Design**
   - Consider compliance from the start
   - Don't add it retrospectively
   - Integrate into development processes

2. **Automation**
   - Automate compliance checks
   - Continuous compliance monitoring
   - Automatic reporting

3. **Documentation**
   - Document everything
   - Keep documentation current
   - Central repository

4. **Training and Awareness**
   - Regular training
   - Role-specific training
   - Awareness campaigns

5. **Proactive Management**
   - Don't wait for audits
   - Regular self-assessments
   - Continuous improvement

6. **Stakeholder Engagement**
   - Secure management support
   - Involve departments
   - Foster communication

7. **Risk-Based Approach**
   - Focus on critical areas
   - Use resources efficiently
   - Prioritization

8. **Vendor Management**
   - Check vendor compliance
   - Contracts with compliance clauses
   - Regular vendor audits

## Audit Calendar

### Annual Audit Calendar

| Month | Audit Type | Standard | Execution |
|---|---|---|---|
| **January** | Internal Audit | ISO 27001 | Internal Audit Team |
| **February** | Compliance Review | GDPR | DPO |
| **March** | Internal Audit | ISO 20000 | Internal Audit Team |
| **April** | External Audit | ISO 27001 | Certification Body |
| **May** | Vulnerability Assessment | PCI-DSS | QSA |
| **June** | Internal Audit | ISO 27001 | Internal Audit Team |
| **July** | Compliance Review | Internal Policies | Compliance Officer |
| **August** | Internal Audit | ISO 20000 | Internal Audit Team |
| **September** | External Audit | ISO 20000 | Certification Body |
| **October** | Internal Audit | ISO 27001 | Internal Audit Team |
| **November** | Penetration Test | Security | External Pentesters |
| **December** | Annual Review | All Standards | Compliance Officer |

**Note:** Customer audits and regulatory audits are scheduled ad-hoc

## References

- ISO/IEC 27001:2013 - Information Security Management
- ISO/IEC 20000-1:2018 - IT Service Management
- GDPR (EU 2016/679) - General Data Protection Regulation
- BSI IT-Grundschutz Compendium
- PCI-DSS v4.0 - Payment Card Industry Data Security Standard
- SOX (Sarbanes-Oxley Act)
- COBIT 2019 - Control Objectives for Information and Related Technologies
- NIST SP 800-53 - Security and Privacy Controls
- CIS Controls v8 - Center for Internet Security Controls

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Classification:** {{ meta-handbook.classification }}  
**Last Update:** {{ meta-handbook.date }}

