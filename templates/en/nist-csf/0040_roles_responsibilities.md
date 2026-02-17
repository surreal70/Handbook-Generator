
Document-ID: nist-csf-0040
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Roles and Responsibilities (GV.RR)

**Document-ID:** [FRAMEWORK]-0040
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

## Purpose

This document defines the roles, responsibilities, and authorities for cybersecurity risk management within the organization.

## Scope

{{ meta-handbook.scope }}

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
**Name:** {{ meta-organisation-roles.role_CISO }}  
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
**Name:** {{ meta-organisation-roles.role_Risk_Manager }}  
**Responsibilities:**
- Integration of cybersecurity risks into ERM
- Risk assessment and reporting
- Coordination with CISO on risk treatment

### Security Operations Manager
**Name:** {{ meta-handbook.security_ops_manager }}  
**Responsibilities:**
- Daily operation of Security Operations Center (SOC)
- Incident response and management
- Security monitoring and threat detection
- Coordination with IT operations

### Security Architect
**Name:** {{ meta-handbook.security_architect }}  
**Responsibilities:**
- Design of secure system architectures
- Security requirements for new projects
- Technology evaluation and selection
- Security-by-design principles

### Compliance Manager
**Name:** {{ meta-organisation-roles.role_Compliance_Manager }}  
**Responsibilities:**
- Monitoring regulatory compliance
- Conducting compliance assessments
- Coordination of audits
- Maintenance of compliance documentation

## Business Unit Responsibilities

### IT Department
**Head:** {{ meta-organisation-roles.role_IT_Manager }}  
**Responsibilities:**
- Implementation of security controls
- Patch management and system hardening
- Access management
- Backup and recovery

### Human Resources
**Head:** {{ meta-organisation-roles.role_HR_Manager }}  
**Responsibilities:**
- Security training for employees
- Background checks
- Onboarding/offboarding processes
- Enforcement of security policies

### Legal/Compliance
**Head:** {{ meta-handbook.legal_director }}  
**Responsibilities:**
- Legal advice on cybersecurity
- Contract review (security clauses)
- Data protection compliance
- Incident response (legal aspects)

### Procurement
**Head:** {{ meta-handbook.procurement_director }}  
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

<!-- 
Author Notes:
- Update role assignments when personnel changes occur
- Review RACI matrix regularly for accuracy
- Ensure all roles are clearly defined
-->
