# Guideline: HR Security - Onboarding, Role Change, Offboarding

**Document-ID:** ISMS-0530
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

## 1. Purpose and Scope

This guideline specifies the `0520_Policy_HR_Security.md` and defines:
- Security aspects in the HR lifecycle
- Onboarding, role change, and offboarding processes
- Background checks and confidentiality obligations

**Scope:** All employees, contractors, and third parties at **AdminSend GmbH**

## 2. Pre-Employment

### 2.1 Background Checks

**Standard Employees:**
- Identity verification (ID card)
- Check references (2 references)
- Verify educational qualifications
- Check work authorization

**Privileged Roles:**
- Extended background checks
- Criminal record certificate
- Credit check (for financial access)
- Social media screening (optional)

**External Contractors:**
- Company background check
- NDA before access
- Sponsor responsibility

### 2.2 Employment Contract

**Security Clauses:**
- Confidentiality obligation
- Acceptable Use Policy
- Intellectual property rights
- Post-employment obligations

## 3. Onboarding

### 3.1 First Day of Work

**HR Activities:**
1. Hand over welcome package
2. Sign employment contract
3. Acknowledge security policies
4. Record emergency contacts

**IT Activities:**
1. Account creation (see `0230_Guideline_IAM`)
2. Hardware issuance
3. IT orientation
4. MFA registration

### 3.2 Security Training

**Mandatory Training (First Week):**
- Information Security Awareness (2 hours)
- Data Protection / GDPR (1 hour)
- Acceptable Use Policy (30 minutes)
- Phishing Awareness (30 minutes)

**Confirmation:**
- Quiz (passing threshold: 80%)
- Signature on training certificate

### 3.3 Role-Specific Training

**Developers:**
- Secure Coding Training
- OWASP Top 10

**Administrators:**
- Privileged Access Management
- Incident Response

**HR/Finance:**
- Data Privacy
- Social Engineering Awareness

## 4. Role Change (Mover)

### 4.1 Internal Transfer

**HR Process:**
1. Update new role in HR system
2. Inform old and new supervisor
3. IT ticket for access changes

**IT Process:**
1. Revoke old access
2. Provision new access
3. Adjust hardware (if required)
4. Update documentation

**Details:** See `0230_Guideline_IAM`

### 4.2 Promotions

**Additional Checks:**
- For privileged roles: Extended background check
- Security training for new responsibilities
- Four-eyes principle for critical access

## 5. Offboarding

### 5.1 Planned Departure

**2 Weeks Before Departure:**
- Plan knowledge transfer
- Create handover checklist
- Review access

**Last Day of Work:**
- Hardware return
- Return access card
- Exit interview
- Account deactivation (end of day)

**After Departure:**
- Account deletion (after 30 days)
- Email forwarding (30 days)
- Data archiving

**Details:** See `0230_Guideline_IAM`

### 5.2 Unplanned Departure

**Immediate Actions (within 1 hour):**
1. Deactivate all accounts
2. Block VPN access
3. Deactivate access card
4. Remote wipe mobile devices
5. Inform supervisor and Security

**Reasons:**
- Termination for cause
- Security incidents
- Suspected data misuse

### 5.3 Post-Employment

**Confidentiality Obligation:**
- Remains in effect after departure
- No disclosure of trade secrets
- Return of all documents

**Rehiring:**
- New background check
- New security training
- New accounts (no reactivation of old accounts)

## 6. Confidentiality Obligations

### 6.1 Non-Disclosure Agreement (NDA)

**Signing:**
- At hiring (in employment contract)
- For access to confidential projects
- For data processing (external service providers)

**Contents:**
- Definition of confidential information
- Usage restrictions
- Duration of obligation
- Consequences of violations

### 6.2 Intellectual Property (IP)

**Regulation:**
- All work results belong to the company
- No private use of company code
- Disclosure of inventions

## 7. Disciplinary Measures

### 7.1 Security Violations

**Categories:**
- **Minor:** Unintentional violations (e.g., password sharing)
- **Medium:** Negligent violations (e.g., data loss through carelessness)
- **Severe:** Intentional violations (e.g., data theft)

**Measures:**
- Minor: Warning, retraining
- Medium: Written reprimand
- Severe: Termination, criminal charges

### 7.2 Process

1. Incident report
2. Investigation by HR and Security
3. Hearing of employee
4. Decision on measures
5. Documentation
6. Implementation

## 8. External Contractors

### 8.1 Onboarding

**Prerequisites:**
- Contract with security clauses
- NDA signed
- Background check (by contractor company)
- Internal sponsor

**Access:**
- Time-limited
- Project-based only
- Regular recertification (quarterly)

### 8.2 Monitoring

**Enhanced Monitoring:**
- Access to confidential data
- Privileged activities
- Data exports

### 8.3 Offboarding

**At Project End:**
- Immediate access revocation
- Data return or deletion
- Confirmation of confidentiality obligation

## 9. Compliance and Audit

### 9.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Background check completion | 100% |
| Security training (onboarding) | 100% |
| Offboarding completion (on last day) | 100% |
| NDA signing | 100% |

### 9.2 Audit Evidence

- Background check documentation
- Training certificates
- NDA signatures
- Offboarding checklists

## 10. References

### Internal Documents
- `0520_Policy_HR_Security.md`
- `0230_Guideline_IAM_Joiner_Mover_Leaver_and_Access_Requests.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.6.1** - Screening
- **ISO/IEC 27001:2022 Annex A.6.2** - Terms and conditions of employment
- **ISO/IEC 27001:2022 Annex A.6.3** - Information security awareness, education and training
- **ISO/IEC 27001:2022 Annex A.6.4** - Disciplinary process

**Approved by:** [TODO], CISO  
**Next Review:** [TODO]

