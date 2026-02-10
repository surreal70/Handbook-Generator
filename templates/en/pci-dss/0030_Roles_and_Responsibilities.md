# Roles and Responsibilities

**Document ID:** PCI-0030  
**Organization:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** {{ meta.document.classification }}  
**Last Updated:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines roles and responsibilities for PCI-DSS compliance.
It aligns with PCI-DSS v4.0 Requirement 12.4 (PCI DSS compliance is the responsibility of management).

Customization required:
- Assign specific individuals to roles
- Define RACI matrices for all PCI-DSS activities
- Document escalation paths
- Include contact information
-->

## 1. Purpose

This document defines the roles, responsibilities, and accountabilities for PCI-DSS compliance at {{ meta.organization.name }}.

### 1.1 Objectives

- **Clear Responsibilities:** Unambiguous assignment of PCI-DSS tasks
- **Accountability:** Establishment of decision-making authority
- **Compliance:** Meet PCI-DSS Requirement 12.4
- **Communication:** Transparent communication channels

## 2. Organizational Structure

### 2.1 Executive Management

**Chief Executive Officer (CEO):**
- **Name:** {{ meta.roles.ceo.name }}
- **Email:** {{ meta.roles.ceo.email }}
- **Phone:** {{ meta.roles.ceo.phone }}

**Responsibilities:**
- Overall responsibility for PCI-DSS compliance
- Approval of PCI-DSS budget
- Approval of information security policy
- Escalation point for critical compliance issues

**Chief Information Security Officer (CISO):**
- **Name:** {{ meta.roles.ciso.name }}
- **Email:** {{ meta.roles.ciso.email }}
- **Phone:** {{ meta.roles.ciso.phone }}

**Responsibilities:**
- Leadership of PCI-DSS compliance program
- Approval of security policies and standards
- Oversight of compliance activities
- Reporting to executive management
- Approval of exceptions (risk acceptance)

### 2.2 PCI-DSS Program Management

**PCI-DSS Program Manager:**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Day-to-day management of PCI-DSS program
- Coordination of all compliance activities
- Preparation for audits and assessments
- Maintenance of PCI-DSS documentation
- Training coordination
- Liaison to QSA and acquiring banks

**PCI-DSS Compliance Team:**
- **Members:** [TODO: List of team members]

**Responsibilities:**
- Support of program manager
- Execution of compliance checks
- Documentation of evidence
- Coordination with business units

### 2.3 IT and Operations

**Chief Information Officer (CIO):**
- **Name:** {{ meta.roles.cio.name }}
- **Email:** {{ meta.roles.cio.email }}
- **Phone:** {{ meta.roles.cio.phone }}

**Responsibilities:**
- Responsibility for IT infrastructure and systems
- Approval of IT changes in CDE
- Provision of resources for PCI-DSS compliance
- Escalation point for IT-related compliance issues

**IT Security Manager:**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Implementation of security controls
- Management of firewalls and network segmentation
- Patch management and vulnerability management
- Incident response
- Log monitoring and analysis

**System Administrators:**
- **Count:** [TODO: Count]
- **Contact:** [TODO: Team email]

**Responsibilities:**
- Administration of CDE systems
- Execution of security updates
- Backup and recovery
- Compliance with hardening standards

**Network Administrators:**
- **Count:** [TODO: Count]
- **Contact:** [TODO: Team email]

**Responsibilities:**
- Management of network components
- Firewall configuration and maintenance
- Network segmentation
- VPN management

### 2.4 Application Development

**Development Manager:**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Secure software development (Secure SDLC)
- Code reviews and security testing
- Compliance with secure coding standards
- Vulnerability management in applications

**Developers:**
- **Count:** [TODO: Count]
- **Contact:** [TODO: Team email]

**Responsibilities:**
- Development of secure applications
- Participation in security training
- Remediation of security vulnerabilities
- Documentation of applications

### 2.5 Business Operations

**Operations Manager:**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Business processes involving cardholder data
- Training of employees
- Compliance with operational procedures
- Incident reporting

**Store/Branch Managers:**
- **Count:** [TODO: Count]
- **Contact:** [TODO: Contact list]

**Responsibilities:**
- Physical security at locations
- Training of cashiers/POS operators
- Compliance with PCI-DSS procedures
- Reporting of security incidents

### 2.6 Human Resources

**HR Manager:**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Background checks for employees with CDE access
- Onboarding and offboarding
- Training coordination
- Non-disclosure agreements (NDAs)

### 2.7 Legal and Compliance

**Legal Counsel:**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Legal advice on PCI-DSS
- Contract review (service providers)
- Data protection and compliance
- Breach notification (legal aspects)

**Data Protection Officer (DPO):**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Responsibilities:**
- Data protection compliance (GDPR)
- Interface between PCI-DSS and data protection
- Data protection impact assessments
- Reporting of data breaches

## 3. External Roles

### 3.1 Qualified Security Assessor (QSA)

**Company:** [TODO: QSA Company]  
**Contact:** [TODO: Name]  
**Email:** [TODO: Email]  
**Phone:** [TODO: Phone]  
**QSA ID:** [TODO: QSA ID]  

**Responsibilities:**
- Conduct annual PCI-DSS assessment
- Creation of Report on Compliance (ROC)
- Advice on compliance questions
- Validation of security controls

### 3.2 Approved Scanning Vendor (ASV)

**Company:** [TODO: ASV Company]  
**Contact:** [TODO: Name]  
**Email:** [TODO: Email]  
**Phone:** [TODO: Phone]  
**ASV ID:** [TODO: ASV ID]  

**Responsibilities:**
- Quarterly vulnerability scans
- Creation of scan reports
- Validation of remediation
- Passing scan attestation

### 3.3 Penetration Testing Firm

**Company:** [TODO: Pentest Company]  
**Contact:** [TODO: Name]  
**Email:** [TODO: Email]  
**Phone:** [TODO: Phone]  

**Responsibilities:**
- Annual penetration tests
- Segmentation validation
- Creation of pentest reports
- Retest after remediation

### 3.4 Service Providers

| Service Provider | Contact | Role | PCI-DSS Status |
|------------------|---------|------|----------------|
| [TODO: Payment Processor] | [TODO: Contact] | Payment Processing | AOC available |
| [TODO: Hosting Provider] | [TODO: Contact] | Server Hosting | AOC available |
| [TODO: Managed Security] | [TODO: Contact] | SIEM/SOC | AOC available |

## 4. RACI Matrices

### 4.1 PCI-DSS Requirement 1: Firewall Configuration

| Activity | CISO | PCI Mgr | IT Sec | Network | QSA |
|----------|------|---------|--------|---------|-----|
| Create firewall policy | A | R | C | C | I |
| Configure firewall rules | C | I | A | R | I |
| Quarterly rule review | A | R | C | C | I |
| Approve changes | A | C | R | I | I |

### 4.2 PCI-DSS Requirement 3: Protect Stored Data

| Activity | CISO | PCI Mgr | IT Sec | Dev Mgr | QSA |
|----------|------|---------|--------|---------|-----|
| Encryption policy | A | R | C | C | I |
| Key management | C | I | A | R | I |
| Data deletion | C | R | A | C | I |
| Tokenization | C | R | C | A | I |

### 4.3 PCI-DSS Requirement 6: Secure Development

| Activity | CISO | PCI Mgr | IT Sec | Dev Mgr | Developers |
|----------|------|---------|--------|---------|------------|
| Secure coding standards | A | C | C | R | I |
| Code reviews | C | I | C | A | R |
| Vulnerability scanning | C | R | A | C | I |
| Patch deployment | C | R | A | R | C |

### 4.4 PCI-DSS Requirement 8: Authentication

| Activity | CISO | PCI Mgr | IT Sec | HR | QSA |
|----------|------|---------|--------|-----|-----|
| Authentication policy | A | R | C | C | I |
| User management | C | I | A | R | I |
| MFA implementation | C | R | A | I | I |
| Access removal (offboarding) | C | R | A | R | I |

### 4.5 PCI-DSS Requirement 10: Logging

| Activity | CISO | PCI Mgr | IT Sec | Ops Mgr | QSA |
|----------|------|---------|--------|---------|-----|
| Logging policy | A | R | C | C | I |
| Log configuration | C | I | A | R | I |
| Daily log review | C | R | A | C | I |
| Log retention | A | R | C | I | I |

### 4.6 PCI-DSS Requirement 12: Security Policy

| Activity | CEO | CISO | PCI Mgr | Legal | QSA |
|----------|-----|------|---------|-------|-----|
| Approve security policy | A | R | C | C | I |
| Annual risk assessment | C | A | R | I | I |
| Training program | C | A | R | C | I |
| Incident response plan | C | A | R | C | I |

**Legend:**
- **R** (Responsible): Execution responsibility
- **A** (Accountable): Overall responsibility, decision authority (only one person per activity)
- **C** (Consulted): Consulted, subject matter expertise
- **I** (Informed): Informed

## 5. Escalation Paths

### 5.1 Compliance Escalation

**Level 1:** PCI-DSS Program Manager  
**Level 2:** CISO  
**Level 3:** CEO  

**Escalation Criteria:**
- Critical compliance gaps
- Failed audits
- Data breaches
- Unremediable vulnerabilities

### 5.2 Security Incident Escalation

**Level 1:** IT Security Manager (24/7 on-call)  
**Level 2:** CISO  
**Level 3:** CEO + Legal Counsel  

**Escalation Criteria:**
- Suspected data breach
- Compromise of CDE systems
- Malware infection in CDE
- Unauthorized access to cardholder data

### 5.3 Emergency Contact Information

**24/7 Security Hotline:** [TODO: Phone number]  
**Security Email:** [TODO: security@organization.com]  
**Incident Response Team:** [TODO: Contact list]  

## 6. Training and Awareness

### 6.1 Training Requirements

| Role | Training Topics | Frequency | Responsible |
|------|-----------------|-----------|-------------|
| All Employees | Security Awareness | Annual | HR + PCI Mgr |
| CDE Administrators | PCI-DSS Deep Dive | Annual | PCI Mgr |
| Developers | Secure Coding | Annual | Dev Mgr |
| Cashiers/POS | PCI-DSS Basics | Upon hire + annual | Ops Mgr |

### 6.2 Training Documentation

**Training evidence required:**
- Attendance list
- Training materials
- Participant confirmations
- Test results (if applicable)

**Retention Period:** [TODO: 3 years]

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
