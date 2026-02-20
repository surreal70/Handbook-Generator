# ISMS Governance: Roles and Responsibilities

**Document-ID:** ISMS-0040
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



**Document ID:** 0040  
**Document Type:** ISMS Foundation Document  
**Standard Reference:** ISO/IEC 27001:2022 Clause 5.3  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. ISMS Governance Structure

### 1.1 Governance Overview

The ISMS governance of **AdminSend GmbH** is integrated into the overall organization and ensures that information security is anchored at all levels.

```
┌─────────────────────────────────────────────────────────┐
│              Management / Top Management                 │
│                 ({{ meta-handbook.management_ceo }})              │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────┐
│  CIO             │    │  CISO            │
│  [TODO]  │    │  [TODO]  │
└─────────────────┘    └─────────────────┘
         │                       │
         │              ┌────────┴────────┐
         │              │                 │
         │     ┌────────▼────────┐ ┌─────▼──────┐
         │     │ ISMS Manager    │ │ Security   │
         │     │                 │ │ Team       │
         │     └─────────────────┘ └────────────┘
         │
┌────────▼────────────────────────────────────────────────┐
│        Information Security Committee                    │
│        (Security Steering Committee)                     │
│  - CISO (Chair)                                         │
│  - CIO                                                  │
│  - Business Unit Representatives                        │
│  - IT Operations                                        │
│  - Data Protection Officer                              │
│  - Internal Audit (advisory)                            │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Key Committees

**Information Security Committee (Security Steering Committee):**
- **Chair:** [TODO] (CISO)
- **Members:** CIO, business unit representatives, IT operations, data protection officer
- **Frequency:** Quarterly or as needed
- **Responsibilities:**
  - Strategic direction of the ISMS
  - Approval of security policies
  - Monitoring ISMS performance
  - Risk acceptance decisions
  - Budget approval for security measures

### 1.3 Interfaces to Other Functions

**IT Service Management (ITSM):**
- Integration of security into ITIL processes
- Incident management, change management, problem management
- Contact: {{ meta-handbook.it_service_manager }}

**Data Protection (DPMS):**
- Interface to GDPR compliance
- Joint risk analysis and data protection impact assessment
- Contact: {{ meta-handbook.privacy_dpo }}

**Risk Management:**
- Integration into Enterprise Risk Management (ERM)
- Shared risk register
- Contact: {{ meta-handbook.risk_manager }}

**Business Continuity Management (BCM):**
- Interface to BCM handbook
- Joint BIA and emergency planning
- Contact: {{ meta-handbook.bcm_manager }}

**Internal Audit:**
- Independent review of the ISMS
- Audit planning and execution
- Contact: {{ meta-handbook.audit_manager }}



## 2. Role Descriptions

### 2.1 Management / Top Management

**Role:** {{ meta-handbook.management_ceo }}

**Responsibilities:**
- Overall responsibility for information security
- Approval of ISMS policy
- Provision of resources for the ISMS
- Promotion of security culture
- Participation in management review

**Authorities:**
- Approval of security budgets
- Decision on strategic security initiatives
- Approval of risk acceptances (for high risks)

### 2.2 CISO (Chief Information Security Officer)

**Role:** [TODO] ({{ meta-organisation-roles.role_CISO_email }})

**Responsibilities:**
- Development, implementation, and monitoring of the ISMS
- Leadership of the information security committee
- Creation and maintenance of security policies
- Conducting risk analyses
- Incident response coordination
- Reporting to management
- Awareness and training

**Authorities:**
- Approval of security policies
- Ordering security measures
- Escalation for critical security incidents
- Access to all security-relevant information

**Reporting Line:** Reports to [TODO] (CIO) and management

### 2.3 CIO (Chief Information Officer)

**Role:** [TODO] ({{ meta-organisation-roles.role_CIO_email }})

**Responsibilities:**
- IT strategy and IT operations
- Support of ISMS implementation
- Provision of IT resources for security measures
- Integration of security into IT processes

**Authorities:**
- Approval of IT projects with security relevance
- Resource allocation for IT security

### 2.4 ISMS Manager

**Role:** [TODO: Name and contact]

**Responsibilities:**
- Operational implementation of the ISMS
- Maintenance of ISMS documentation
- Coordination of audits and reviews
- Tracking of measures and findings
- Support of the CISO

**Authorities:**
- Coordination of ISMS activities
- Request for information for audits

### 2.5 Asset Owner / Process Owner

**Role:** Business unit managers, process owners

**Responsibilities:**
- Responsibility for information assets in their area
- Classification of information
- Definition of access rights
- Implementation of security measures in their area
- Reporting of security incidents

**Authorities:**
- Approval of access rights for their assets
- Decision on security measures in their area

### 2.6 Control Owner

**Role:** Responsible for specific security controls

**Responsibilities:**
- Implementation and operation of security controls
- Evidence of effectiveness
- Reporting on control status
- Remediation of control deficiencies

**Authorities:**
- Implementation of security measures within their control

**Examples:**
- Patch Management Control Owner: IT Operations
- Access Control Owner: IAM Team
- Backup Control Owner: Backup Administrator

### 2.7 IT Operations

**Role:** IT Operations Team

**Responsibilities:**
- Implementation of technical security measures
- Monitoring and alerting
- Incident response (technical)
- Patch management
- Backup and recovery

**Authorities:**
- Execution of security measures
- Emergency access during incidents

### 2.8 Employees (all)

**Role:** All employees, contractors, third parties

**Responsibilities:**
- Compliance with security policies
- Reporting of security incidents
- Participation in security awareness training
- Protection of credentials and information

**Authorities:**
- Access to information according to need-to-know principle

### 2.9 Internal Audit / Compliance

**Role:** {{ meta-handbook.audit_manager }}

**Responsibilities:**
- Independent review of the ISMS
- Audit planning and execution
- Reporting of audit findings
- Monitoring of measure implementation

**Authorities:**
- Access to all ISMS-relevant information
- Request for evidence and interviews

## 3. RACI Matrix: ISMS Processes

### 3.1 ISMS Core Processes

| Activity | CISO | CIO | ISMS Manager | Asset Owner | IT Operations | Internal Audit |
|----------|------|-----|--------------|-------------|---------------|----------------|
| **Develop ISMS strategy** | R/A | C | C | I | I | I |
| **Create policies** | R/A | C | R | C | C | I |
| **Conduct risk analysis** | A | C | R | C | C | I |
| **Plan risk treatment** | A | C | R | C | R | I |
| **Maintain SoA** | A | I | R | C | C | I |
| **Implement controls** | A | C | C | R | R | I |
| **Perform monitoring** | A | I | C | I | R | I |
| **Manage incidents** | A | C | C | I | R | I |
| **Conduct audits** | C | C | C | C | C | R/A |
| **Management review** | R | C | R | I | I | C |
| **Awareness training** | A | C | R | I | I | I |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### 3.2 Annex A Controls (Examples)

| Control | Control Owner | Responsible | Accountable | Consulted | Informed |
|---------|---------------|-------------|-------------|-----------|----------|
| **A.5.1 Policies** | CISO | ISMS Manager | CISO | CIO, Business Units | All |
| **A.5.7 Threat Intelligence** | Security Team | Security Analyst | CISO | IT Operations | ISMS Manager |
| **A.5.10 Acceptable Use** | CISO | HR | CISO | IT Operations | All |
| **A.5.15 Access Control** | IAM Team | IAM Admin | CIO | CISO | IT Operations |
| **A.5.23 Cloud Services** | Cloud Architect | Cloud Admin | CIO | CISO | IT Operations |
| **A.8.8 Backup** | IT Operations | Backup Admin | CIO | CISO | ISMS Manager |
| **A.8.16 Monitoring** | Security Team | SOC Analyst | CISO | IT Operations | ISMS Manager |



## 4. Escalation Paths

### 4.1 Security Incidents

```
Incident Detection
       │
       ▼
IT Operations / SOC
       │
       ▼
CISO (for critical incidents)
       │
       ▼
CIO / Management (for major incidents)
       │
       ▼
External Reporting (authorities, customers)
```

See `0400_Policy_Incident_Management.md` for details.

### 4.2 Risk Acceptance

```
Risk Identification
       │
       ▼
CISO (risk assessment)
       │
       ▼
CISO (risk acceptance for low/medium risks)
       │
       ▼
Management (risk acceptance for high risks)
```

See `0070_ISMS_Risk_Acceptance_Criteria.md` for details.

## 5. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0030_ISMS_Context_and_Interested_Parties.md` - Context
- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management
- `0130_ISMS_Internal_Audit_Program.md` - Internal Audit Program

### External Standards
- **ISO/IEC 27001:2022** - Clause 5.3: Organizational roles, responsibilities and authorities
- **ISO/IEC 27002:2022** - Control 5.2: Information security roles and responsibilities

**Approved by:**  
{{ meta-handbook.management_ceo }}, Management  
Date: [TODO]

**Next Review:** [TODO]

