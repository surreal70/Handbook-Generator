# Training, Awareness and Competence

<!-- 
TEMPLATE AUTHOR NOTE:
This document defines the security awareness and training program. It ensures
that all personnel are aware of their information security responsibilities
and have the necessary competence to fulfill their roles.

ISO 27001:2022 Reference: Clause 7.2 - Competence, Clause 7.3 - Awareness
-->

**Document ID:** 0120  
**Document Type:** ISMS Foundation Document  
**Standard Reference:** ISO/IEC 27001:2022 Clauses 7.2, 7.3  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose and Objectives

### 1.1 Purpose

The training and awareness program of **{{ meta.organization.name }}** ensures that:
- All employees know their security responsibilities
- Employees have the necessary competencies for their roles
- Security awareness is continuously promoted
- Compliance with ISO 27001:2022 and other requirements is ensured

### 1.2 Objectives

- **100% Training Participation:** All employees complete annual security awareness training
- **Phishing Resilience:** Click rate in phishing simulations < 5%
- **Incident Reporting:** Increase security incidents reported by employees
- **Competence Building:** Specialized training for IT security roles

## 2. Target Groups

### 2.1 Target Group Overview

| Target Group | Number | Training Need | Frequency | Responsible |
|--------------|--------|---------------|-----------|-------------|
| **All Employees** | {{ meta.organization.employee_count }} | Security Awareness Basics | Annually | {{ meta.ciso.name }} |
| **Admins/Privileged Users** | [TODO] | Advanced Security, Privileged Access | Semi-annually | {{ meta.ciso.name }} |
| **Developers/DevOps** | [TODO] | Secure Coding, DevSecOps | Semi-annually | {{ meta.ciso.name }} |
| **Management** | [TODO] | Security Governance, Risk Management | Annually | {{ meta.ciso.name }} |
| **HR** | [TODO] | HR Security, Onboarding/Offboarding | Annually | {{ meta.ciso.name }} |
| **Contractors/External** | [TODO] | Security Basics, Compliance | At Onboarding | {{ meta.ciso.name }} |

### 2.2 Role-Specific Requirements

**IT Security Team:**
- ISO 27001 Lead Auditor Training
- Incident Response Training
- Threat Intelligence Training
- Security Tool Training (SIEM, EDR, etc.)

**IT Operations:**
- Secure Configuration Management
- Patch Management
- Backup and Recovery
- Access Management

**Developers:**
- OWASP Top 10
- Secure Coding Practices
- Secret Management
- Security Testing (SAST/DAST)

## 3. Training Plan

### 3.1 Mandatory Training

| Training ID | Training | Target Group | Frequency | Duration | Content | Evidence | Owner | Status |
|-------------|----------|--------------|-----------|----------|---------|----------|-------|--------|
| **T-001** | Security Awareness Basics | All Employees | Annually | 60 min | Phishing, passwords, clean desk, incident reporting | LMS certificate | {{ meta.ciso.name }} | Active |
| **T-002** | GDPR Basics | All Employees | Annually | 30 min | Data protection basics, data subject rights | LMS certificate | {{ meta.privacy.dpo }} | Active |
| **T-003** | Phishing Awareness | All Employees | Quarterly | 15 min | Phishing detection, reporting | Simulation result | {{ meta.ciso.name }} | Active |
| **T-004** | Privileged Access Management | Admins | Semi-annually | 90 min | PAM, least privilege, audit logging | LMS certificate | {{ meta.ciso.name }} | Active |
| **T-005** | Secure Coding | Developers | Semi-annually | 120 min | OWASP Top 10, input validation, secrets | LMS certificate | {{ meta.ciso.name }} | Active |
| **T-006** | Incident Response | Security Team | Annually | 180 min | IR process, forensics, communication | Workshop attendance | {{ meta.ciso.name }} | Active |

[TODO: Add additional training]

### 3.2 Optional Training

| Training | Target Group | Frequency | Provider | Cost |
|----------|--------------|-----------|----------|------|
| ISO 27001 Lead Auditor | Security Team | One-time | External | [TODO] |
| CISSP/CISM Certification | Security Team | One-time | External | [TODO] |
| Cloud Security (AWS/Azure) | IT Operations | As needed | External | [TODO] |
| Penetration Testing | Security Team | As needed | External | [TODO] |

### 3.3 Onboarding Training

**New Employees:**
- Day 1: Security Awareness Basics (T-001)
- Day 1: GDPR Basics (T-002)
- Week 1: Role-specific training

**External Contractors:**
- Before access: Security Basics
- NDA signing
- Access policies

## 4. Awareness Campaigns

### 4.1 Regular Campaigns

**Monthly:**
- Security newsletter
- Security tip of the month
- Current threats and warnings

**Quarterly:**
- Phishing simulations
- Security quiz with prizes
- Lunch & learn sessions

**Annually:**
- Security Awareness Month (October)
- Security Champions Program
- Poster campaigns

### 4.2 Topic Focus

| Quarter | Topic | Activities |
|---------|-------|------------|
| Q1 | Password Security | MFA rollout, password manager training |
| Q2 | Phishing & Social Engineering | Phishing simulation, awareness videos |
| Q3 | Mobile Security | BYOD policy, mobile device management |
| Q4 | Incident Response | Incident reporting, lessons learned |

### 4.3 Communication Channels

- **Email:** Security newsletter, alerts
- **Intranet:** Security portal, policies, FAQs
- **Posters:** Offices, break rooms
- **Teams/Slack:** Security channel
- **Workshops:** Lunch & learn, hands-on training

## 5. Phishing Simulations

### 5.1 Simulation Program

**Frequency:** Quarterly

**Process:**
1. Plan simulation (topic, target group)
2. Send phishing email
3. Measure click rate
4. Immediate feedback for clickers
5. Follow-up training for risk groups
6. Analyze and report results

**Target Values:**
- Click rate < 5%
- Reporting rate > 50%

**Tools:**
- [TODO: KnowBe4, Cofense, etc.]

### 5.2 Escalation for High Click Rate

**Click rate > 10%:**
- Additional awareness campaign
- Mandatory follow-up training
- Root cause analysis

**Click rate > 20%:**
- Escalation to management
- Intensified training measures
- Review of awareness program

## 6. Effectiveness Verification

### 6.1 Measurement Methods

**Quantitative Metrics:**
- Training participation rate
- Phishing click rate
- Quiz results
- Number of incidents reported by employees
- Number of security violations

**Qualitative Metrics:**
- Feedback surveys
- Stakeholder interviews
- Observations (clean desk, screen lock)

### 6.2 Success Criteria

| Metric | Target Value | Current | Status |
|--------|--------------|---------|--------|
| Training participation | 100% | [TODO]% | [TODO] |
| Phishing click rate | < 5% | [TODO]% | [TODO] |
| Incident reports | > 20 per quarter | [TODO] | [TODO] |
| Quiz success rate | > 80% | [TODO]% | [TODO] |

### 6.3 Continuous Improvement

**Annual Review:**
- Analysis of training results
- Feedback evaluation
- Adjustment of training content
- Identification of new topics

**Lessons Learned:**
- From security incidents
- From audit findings
- From phishing simulations

## 7. Training Records

### 7.1 Documentation

**Learning Management System (LMS):**
- Training participation
- Certificates
- Quiz results
- Expiration dates

**Manual Records:**
- Workshop attendance lists
- External certificates
- Conference attendance

### 7.2 Retention

**Retention Period:** 10 years

**Access:**
- HR: All records
- CISO: All records
- Managers: Records of their team
- Employees: Own records

### 7.3 Audit Evidence

For audits, the following evidence is provided:
- Training plan
- Attendance lists
- Certificates
- Phishing simulation results
- Awareness campaign documentation

## 8. Roles and Responsibilities

### 8.1 RACI Matrix: Training and Awareness

| Activity | CISO | HR | Manager | Employee | External Trainer |
|----------|------|----|---------|----------|------------------|
| Create training plan | R/A | C | C | I | I |
| Conduct training | R | C | I | I | R |
| Ensure participation | A | C | R | R | I |
| Document records | A | R | C | I | I |
| Verify effectiveness | R/A | C | C | I | I |
| Awareness campaigns | R/A | C | C | I | C |
| Phishing simulations | R/A | I | I | I | C |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### 8.2 Security Champions

**Program:**
- Volunteer employees from all departments
- Multipliers for security awareness
- Regular meetings and training
- Recognition and incentives

**Tasks:**
- Promote awareness in their teams
- Answer security questions
- Provide feedback to security team
- Participate in security projects

## 9. Budget and Resources

### 9.1 Budget Planning

| Category | Annual Budget | Remarks |
|----------|---------------|---------|
| LMS license | [TODO] € | E-learning platform |
| External training | [TODO] € | Certifications, conferences |
| Phishing simulation tool | [TODO] € | KnowBe4, Cofense, etc. |
| Awareness materials | [TODO] € | Posters, flyers, giveaways |
| External trainers | [TODO] € | Workshops, specialized training |
| **Total** | **[TODO] €** | |

### 9.2 Time Resources

**CISO/Security Team:**
- Training planning: 20 PD/year
- Training delivery: 40 PD/year
- Awareness campaigns: 30 PD/year
- Phishing simulations: 20 PD/year

**Employees:**
- Mandatory training: 2 hours/year
- Optional training: As needed

## 10. References

### 10.1 Internal Documents

- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0040_ISMS_Governance_Roles_and_Responsibilities.md` - Governance
- `0110_ISMS_Security_Objectives_and_Metrics.md` - Security Objectives
- `0200_Policy_Acceptable_Use_of_IT.md` - Acceptable Use Policy
- `0520_Policy_HR_Security.md` - HR Security

### 10.2 External Standards

- **ISO/IEC 27001:2022** - Clause 7.2: Competence
- **ISO/IEC 27001:2022** - Clause 7.3: Awareness
- **ISO/IEC 27002:2022** - Control 6.3: Information security awareness, education and training

---

**Approved by:**  
{{ meta.ciso.name }}, CISO  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }}
