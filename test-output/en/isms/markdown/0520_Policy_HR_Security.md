# Policy: HR Security

**Document-ID:** [FRAMEWORK]-0520
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



**Document ID:** 0520  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.6.1-A.6.4 (incl. Amendment 1:2024)  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose

This policy defines the principles for HR Security at **AdminSend GmbH**. It ensures that security responsibilities are understood and fulfilled throughout the employment lifecycle - from hiring through termination.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Persons:** All employees, contractors, temporary workers, interns
- **Lifecycle:** Pre-employment, onboarding, employment, offboarding
- **Locations:** [[ netbox.site.name ]] and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Pre-Employment Screening
Appropriate background checks are conducted before hiring (references, qualifications, criminal record if applicable). Screening is based on role and protection requirements.

### 3.2 Contractual Security Obligations
Employment contracts contain security clauses:
- Confidentiality agreements (NDA)
- Acceptable Use Policy acknowledgement
- Data protection obligations
- Intellectual property rights

### 3.3 Security Awareness and Training
All employees undergo security awareness training:
- **Onboarding:** Initial security training
- **Annually:** Refresher training
- **Role-specific:** Additional training for privileged roles

### 3.4 Joiner-Mover-Leaver Process
Security-relevant activities are performed throughout the employment lifecycle:
- **Joiner:** Access provisioning, training, equipment issuance
- **Mover:** Access adjustment for role changes
- **Leaver:** Access revocation, equipment return, exit interview

### 3.5 Disciplinary Process
Security violations are handled according to defined disciplinary procedures. Violations are documented and may lead to employment consequences.

### 3.6 Responsibilities and Duties
Employees are obligated to:
- Comply with security policies
- Report security incidents
- Participate in security training
- Maintain confidentiality

### 3.7 Privileged Roles
Employees with privileged access are subject to enhanced requirements:
- Extended background checks
- Additional security training
- Regular recertification
- Strict monitoring

### 3.8 Offboarding and Access Revocation
Upon termination of employment, all access is immediately revoked:
- IT access deactivated (Target: < 1 day)
- Equipment returned
- Confidentiality obligations renewed
- Exit interview conducted

## 4. Roles and Responsibilities

### RACI Matrix: HR Security

| Activity | CISO | HR | Hiring Manager | IT Operations | Legal |
|----------|------|-----|----------------|---------------|-------|
| Policy Creation | R/A | C | C | I | C |
| Background Checks | C | R/A | C | I | C |
| Contract Clauses | C | R | I | I | R/A |
| Security Training | R/A | C | I | C | I |
| Joiner Process | C | R | R/A | R | I |
| Mover Process | C | R | R/A | R | I |
| Leaver Process | C | R/A | C | R | I |
| Disciplinary Process | C | R/A | C | I | C |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** [TODO] (CISO)
- **HR Manager:** {{ meta-handbook.hr_manager }}
- **Security Awareness Manager:** {{ meta-handbook.security_awareness_manager }}
- **Implementation Responsible:** HR, Hiring Manager, IT Operations
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Associated Guidelines
- **0530_Guideline_HR_Onboarding_Role_Change_Offboarding.md** - Detailed implementation guideline
- `0220_Policy_Access_Control_and_Identity_Management.md` - Access Control Policy
- `0200_Policy_Acceptable_Use_of_IT.md` - Acceptable Use Policy
- `0120_ISMS_Training_Awareness_and_Competence.md` - Training and Awareness

### Associated Standards/Baselines
- Background check requirements
- Contractual security clauses (templates)
- Security training curriculum
- Joiner-Mover-Leaver checklists

### Associated Processes
- Pre-employment screening process
- Joiner-Mover-Leaver process
- Security training process
- Disciplinary process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Background check completion rate (Target: 100%)
- Security training completion rate (Target: 100% annually)
- Average time to access provisioning (Joiner)
- Average time to access revocation (Leaver) (Target: < 1 day)
- Number of security violations and disciplinary procedures
- NDA signing rate (Target: 100%)

### Evidence and Proof
- Background check documentation
- Contracts with security clauses
- Security training evidence
- Joiner-Mover-Leaver checklists
- Disciplinary procedure documentation
- Exit interview protocols

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Missing Background Checks:** Completion before access provisioning
- **Incomplete Training:** Access restriction until completion
- **Security Violations:** Disciplinary procedure per HR process
- **Repeated Violations:** Employment consequences up to termination

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and HR Manager
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0530_Guideline_HR_Onboarding_Role_Change_Offboarding.md` - Detailed Guideline
- `0220_Policy_Access_Control_and_Identity_Management.md` - Access Control Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.6.1** - Screening
- **ISO/IEC 27001:2022 Annex A.6.2** - Terms and conditions of employment
- **ISO/IEC 27001:2022 Annex A.6.3** - Information security awareness, education and training
- **ISO/IEC 27001:2022 Annex A.6.4** - Disciplinary process
- Employment law requirements (Germany)
- **GDPR (EU 2016/679)** - Data protection for background checks

**Approved by:**  
{{ meta-handbook.management_ceo }}, Management  
Date: [TODO]

**Next Review:** [TODO] (annually or as needed)

