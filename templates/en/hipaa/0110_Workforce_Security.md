# Workforce Security

**Document ID:** HIPAA-0110  
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
This template documents Workforce Security (Administrative Safeguard).
It aligns with HIPAA Security Rule §164.308(a)(3) - Workforce Security.

Required (R) Standard with Addressable (A) Implementation Specifications:
- Authorization and/or Supervision (A)
- Workforce Clearance Procedure (A)
- Termination Procedures (A)
-->

## 1. Purpose

This document describes the Workforce Security procedures for {{ meta.organization.name }} to ensure that all workforce members have appropriate access to ePHI and to prevent unauthorized access.

### 1.1 HIPAA Requirement

**Standard:** §164.308(a)(3) - Workforce Security (Required)

**Implementation Specifications:**
- §164.308(a)(3)(ii)(A) - Authorization and/or Supervision (Addressable)
- §164.308(a)(3)(ii)(B) - Workforce Clearance Procedure (Addressable)
- §164.308(a)(3)(ii)(C) - Termination Procedures (Addressable)

## 2. Authorization and Supervision

### 2.1 Access Authorization

**Principle:** Access to ePHI is granted based on role, job function, and minimum necessary standard.

**Authorization Process:**
1. **Job Analysis:** Determine ePHI access requirements for role
2. **Access Request:** Manager submits access request
3. **Justification:** Document business need
4. **Approval:** Privacy Officer and/or Security Officer approve
5. **Provisioning:** IT provisions access
6. **Documentation:** Access logged
7. **Acknowledgment:** Employee acknowledges responsibilities

**Authorization Criteria:**
- Job role requires ePHI access
- Minimum necessary access only
- Appropriate training completed
- Background check completed (if required)
- Confidentiality agreement signed

### 2.2 Supervision Requirements

**Supervised Access:**
Workforce members with limited training or temporary status may require supervision when accessing ePHI.

**Supervision Levels:**
| Workforce Type | Supervision Required | Supervisor | Duration |
|----------------|---------------------|------------|----------|
| New employees (< 90 days) | Yes | Direct manager | Until training complete |
| Temporary staff | Yes | Assigned supervisor | Duration of assignment |
| Interns/students | Yes | Preceptor/instructor | Duration of program |
| Contractors (short-term) | Yes | Project manager | Duration of contract |

**Supervisor Responsibilities:**
- Monitor workforce member's ePHI access
- Ensure compliance with policies
- Provide guidance and training
- Report violations
- Document supervision activities

## 3. Workforce Clearance Procedure

### 3.1 Pre-Employment Screening

**Background Check Requirements:**

**All Workforce with ePHI Access:**
- Identity verification
- Employment history verification (7 years)
- Education verification
- Professional license verification (if applicable)

**Workforce with Elevated Access:**
- Criminal background check
- Credit check (for financial roles)
- Reference checks (minimum 3)

**Background Check Process:**
1. **Conditional Offer:** Offer contingent on background check
2. **Authorization:** Candidate authorizes background check
3. **Screening:** Third-party vendor conducts check
4. **Review:** HR reviews results
5. **Decision:** Hire/no-hire decision
6. **Documentation:** Results documented and secured
7. **Adverse Action:** Follow FCRA requirements if adverse action taken

**Background Check Vendor:** [TODO: Vendor name]

### 3.2 Clearance Levels

| Clearance Level | Requirements | Roles | ePHI Access |
|-----------------|--------------|-------|-------------|
| Level 1 - Basic | Identity verification, employment history | Administrative staff | Limited ePHI |
| Level 2 - Standard | Level 1 + education verification | Clinical staff | Full ePHI for patient care |
| Level 3 - Elevated | Level 2 + criminal background check | IT staff, billing | System-level ePHI access |
| Level 4 - Executive | Level 3 + credit check, references | Executives, compliance | All ePHI |

### 3.3 Ongoing Clearance

**Periodic Re-screening:**
- **Frequency:** [TODO: Every 3-5 years or as required by role]
- **Scope:** Criminal background check, license verification
- **Trigger Events:** Promotion, role change, security incident

**Continuous Monitoring:**
- Professional license status
- Sanctions or disciplinary actions
- Criminal convictions (if permitted by law)

## 4. Termination Procedures

### 4.1 Termination Process

**Termination Types:**
- Voluntary resignation
- Involuntary termination
- Retirement
- End of contract/temporary assignment
- Death

**Termination Checklist:**

**Immediate Actions (Day of Termination):**
- [ ] Disable all system access (within 1 hour of notification)
- [ ] Disable email account
- [ ] Disable VPN access
- [ ] Disable physical access (badge, keys)
- [ ] Collect company devices (laptop, phone, tablet)
- [ ] Collect access badges and keys
- [ ] Change shared passwords/codes known to employee
- [ ] Notify IT, Security, and Facilities

**Within 24 Hours:**
- [ ] Review and archive employee's files
- [ ] Forward email to manager (if appropriate)
- [ ] Remove from distribution lists
- [ ] Update organizational charts
- [ ] Notify relevant departments
- [ ] Document termination in HR system

**Within 1 Week:**
- [ ] Conduct exit interview
- [ ] Remind of confidentiality obligations
- [ ] Collect signed acknowledgment of obligations
- [ ] Final paycheck processing
- [ ] COBRA notification (if applicable)
- [ ] Return of property verification

### 4.2 Access Termination

**System Access Termination:**
| System | Termination Method | Responsible | Verification |
|--------|-------------------|-------------|--------------|
| Active Directory | Account disabled | IT | Automated report |
| EHR System | User deactivated | IT | Manual verification |
| Email | Mailbox disabled | IT | Automated report |
| VPN | Certificate revoked | IT | Manual verification |
| Physical Access | Badge deactivated | Facilities | Access log review |

**Termination Verification:**
- IT generates termination report
- Security Officer reviews report
- Exceptions investigated and resolved
- Documentation retained

### 4.3 Knowledge Transfer

**Knowledge Transfer Process:**
1. **Identification:** Identify critical knowledge and responsibilities
2. **Documentation:** Document processes and procedures
3. **Training:** Train replacement or team members
4. **Transition:** Gradual transition of responsibilities (if possible)
5. **Verification:** Verify knowledge transfer complete

**Critical Knowledge Areas:**
- System access and passwords
- Ongoing projects
- Key contacts
- Pending issues
- Documentation locations

### 4.4 Post-Termination Monitoring

**Monitoring Activities:**
- Review audit logs for terminated employee accounts
- Monitor for unauthorized access attempts
- Review for data exfiltration
- Monitor for policy violations prior to termination

**Monitoring Period:** [TODO: 90 days post-termination]

## 5. Role-Based Access Control (RBAC)

### 5.1 Role Definitions

| Role ID | Role Name | Department | ePHI Access Level | Systems | Approval Required |
|---------|-----------|------------|-------------------|---------|-------------------|
| [TODO: ROLE-001] | Physician | Clinical | Full patient care | EHR, Lab, Imaging | Medical Director |
| [TODO: ROLE-002] | Nurse | Clinical | Full patient care | EHR, Medication | Nurse Manager |
| [TODO: ROLE-003] | Medical Assistant | Clinical | Limited | EHR (vitals, scheduling) | Clinical Manager |
| [TODO: ROLE-004] | Billing Specialist | Billing | Billing data only | Billing system | Billing Manager |
| [TODO: ROLE-005] | IT Administrator | IT | System admin | All systems | IT Manager + Security Officer |
| [TODO: ROLE-006] | Receptionist | Front Desk | Demographics only | EHR (scheduling) | Office Manager |

### 5.2 Access Matrix

| Role | Patient Demographics | Clinical Notes | Lab Results | Medications | Billing | System Admin |
|------|---------------------|----------------|-------------|-------------|---------|--------------|
| Physician | Read/Write | Read/Write | Read/Write | Read/Write | Read | No |
| Nurse | Read/Write | Read/Write | Read | Read/Write | No | No |
| Medical Assistant | Read/Write | Read | Read | No | No | No |
| Billing Specialist | Read | No | No | No | Read/Write | No |
| IT Administrator | No* | No* | No* | No* | No* | Yes |
| Receptionist | Read/Write | No | No | No | No | No |

*IT Administrators have technical access but should not access ePHI unless required for troubleshooting

## 6. Training Requirements

### 6.1 Workforce Security Training

**Initial Training (Within 30 days of hire):**
- HIPAA overview
- Workforce security policies
- Access control procedures
- Password requirements
- Confidentiality obligations
- Sanctions for violations

**Annual Training:**
- Workforce security refresher
- Policy updates
- Case studies
- Emerging threats

**Role-Specific Training:**
- Supervisors: Supervision responsibilities
- IT Staff: Technical safeguards
- Managers: Access authorization procedures

### 6.2 Training Documentation

**Required Documentation:**
- Training attendance records
- Training materials
- Test scores (if applicable)
- Acknowledgment of understanding
- Training certificates

**Retention:** [TODO: 6 years]

## 7. Confidentiality Agreements

### 7.1 Confidentiality Agreement Requirements

**All Workforce Members Must Sign:**
- Confidentiality agreement
- Acceptable use policy
- HIPAA acknowledgment
- Security policy acknowledgment

**Timing:**
- Before access to ePHI granted
- Upon policy changes (re-acknowledgment)
- Annually (re-acknowledgment)

### 7.2 Agreement Content

**Confidentiality Agreement Must Include:**
- Obligation to protect PHI/ePHI
- Prohibition on unauthorized access
- Prohibition on unauthorized disclosure
- Reporting requirements for incidents
- Sanctions for violations
- Obligations continue after termination
- Acknowledgment of understanding

**Agreement Storage:** [TODO: HR personnel files, electronic repository]

## 8. Monitoring and Compliance

### 8.1 Workforce Security Monitoring

**Monitoring Activities:**
- Access log reviews
- Inappropriate access investigations
- Policy compliance audits
- Training completion tracking
- Background check compliance
- Termination procedure compliance

**Monitoring Frequency:**
| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| Access log review | Monthly | Security Officer |
| Training compliance | Quarterly | HR + Privacy Officer |
| Background check compliance | Annual | HR |
| Termination procedure audit | Quarterly | Security Officer |

### 8.2 Compliance Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Training completion rate | 100% | [TODO: %] | [TODO: Green/Yellow/Red] |
| Background checks completed | 100% | [TODO: %] | [TODO: Green/Yellow/Red] |
| Termination procedures followed | 100% | [TODO: %] | [TODO: Green/Yellow/Red] |
| Access reviews completed | 100% | [TODO: %] | [TODO: Green/Yellow/Red] |

## 9. Documentation and Records

### 9.1 Required Documentation

- Access authorization forms
- Background check results
- Confidentiality agreements
- Training records
- Termination checklists
- Access termination verification
- Supervision logs
- Incident reports

### 9.2 Retention

**Retention Period:** [TODO: 6 years from termination of employment or last effective date]

**Storage Location:** [TODO: HR system, document management system]

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
