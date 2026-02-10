# Roles and Responsibilities

**Document-ID:** NIST-0030  
**Organization:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Version:** 1.0.0  
**Status:** Draft / In Review / Approved  
**Last Updated:** {{ meta.document.last_updated }}  

---

## 1. Purpose

This document defines roles and responsibilities for the Risk Management Framework (RMF) and security of system {{ meta.nist.system_name }}.

## 2. RMF Roles

### 2.1 Authorizing Official (AO)

**Name:** {{ meta.roles.ao.name }}  
**Email:** {{ meta.roles.ao.email }}  

**Responsibilities:**
- Authorization decision for the system
- Acceptance of security risk
- Approval of System Security Plan (SSP)
- Monitoring of security status

### 2.2 Information System Security Officer (ISSO)

**Name:** {{ meta.roles.isso.name }}  
**Email:** {{ meta.roles.isso.email }}  

**Responsibilities:**
- Daily security operations
- Implementation of security controls
- Incident response
- Security monitoring

### 2.3 Information System Security Manager (ISSM)

**Name:** {{ meta.roles.issm.name }}  
**Email:** {{ meta.roles.issm.email }}  

**Responsibilities:**
- Security program management
- Policy development
- Compliance monitoring
- Risk management

### 2.4 System Owner

**Name:** [TODO: Name]  
**Email:** [TODO: Email]  

**Responsibilities:**
- Overall system responsibility
- Business process responsibility
- Budget and resources
- Approve system changes

### 2.5 Security Control Assessor (SCA)

**Name:** [TODO: Name/Company]  
**Email:** [TODO: Email]  

**Responsibilities:**
- Independent assessment of security controls
- Creation of Security Assessment Report (SAR)
- Identification of weaknesses
- Recommendations for improvements

## 3. RACI Matrix

| Activity | AO | ISSO | ISSM | System Owner | SCA |
|----------|----|----|------|--------------|-----|
| System Categorization | A | C | R | C | I |
| Control Selection | A | R | C | C | I |
| Control Implementation | I | R | C | A | I |
| Control Assessment | I | C | C | I | R |
| Authorization Decision | R | C | C | C | I |
| Continuous Monitoring | A | R | C | C | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |


