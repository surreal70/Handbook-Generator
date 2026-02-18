# Roles and Responsibilities

**Document-ID:** [FRAMEWORK]-0040
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

## 1. Purpose

This document defines the roles and responsibilities for TSC compliance and SOC 2 audits.

## 2. Management Roles

### 2.1 Executive Management

**CEO:**
- **Name:** [TODO: Name]
- **Responsibilities:**
  - Overall responsibility for compliance
  - Policy approval
  - Resource allocation

**CTO:**
- **Name:** [TODO: Name]
- **Responsibilities:**
  - Technical strategy
  - System architecture
  - Change approval

**CISO:**
- **Name:** {{ meta-organisation-roles.role_CISO }}
- **Email:** {{ meta-organisation-roles.role_CISO }}
- **Responsibilities:**
  - Security strategy
  - Risk management
  - Incident response

## 3. Operational Roles

### 3.1 System Administration

**System Administrators:**
- **Count:** [TODO: #]
- **Responsibilities:**
  - System maintenance
  - Patch management
  - Backup management

### 3.2 Security Operations

**Security Engineers:**
- **Count:** [TODO: #]
- **Responsibilities:**
  - Security monitoring
  - Incident response
  - Vulnerability management

### 3.3 Development

**Developers:**
- **Count:** [TODO: #]
- **Responsibilities:**
  - Application development
  - Code reviews
  - Security testing

## 4. Compliance Roles

### 4.1 SOC 2 Program Manager

**Name:** [TODO: Name]  
**Email:** [TODO: Email]  
**Responsibilities:**
- SOC 2 program management
- Audit coordination
- Documentation
- Compliance reporting

### 4.2 Service Auditor

**Firm:** [TODO]  
**Contact:** [TODO]  
**Responsibilities:**
- Conduct SOC 2 audit
- Test control effectiveness
- Issue SOC 2 report

## 5. RACI Matrix

### 5.1 Control Environment

| Activity | CEO | CTO | CISO | Ops | Audit |
|----------|-----|-----|------|-----|-------|
| Policy Approval | A | C | R | I | I |
| Risk Assessment | C | C | A/R | C | I |
| Control Design | I | C | A | R | C |
| Control Testing | I | I | C | R | A |

### 5.2 Operations

| Activity | CTO | CISO | Ops | Dev | Audit |
|----------|-----|------|-----|-----|-------|
| Change Management | A | C | R | R | I |
| Incident Response | C | A | R | C | I |
| Monitoring | C | A | R | I | I |
| Backup/Recovery | A | C | R | I | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 6. Training and Qualifications

### 6.1 Mandatory Training

- Security Awareness (annual)
- Role-specific Training
- Compliance Training

### 6.2 Certifications

**Security Team:**
- [TODO: CISSP, CISM, CEH]

**Operations Team:**
- [TODO: AWS Certified, Azure Certified]

