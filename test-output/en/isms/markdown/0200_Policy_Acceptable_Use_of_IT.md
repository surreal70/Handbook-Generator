# Policy: Acceptable Use of IT



**Document ID:** 0200  
**Document Type:** Policy (Abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.10 (incl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the principles for acceptable use of IT resources at **AdminSend GmbH**. It ensures that IT systems, applications, and information are used exclusively for business purposes and in compliance with legal and regulatory requirements.



## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Systems:** All IT systems, networks, applications, email, internet, cloud services
- **Persons:** All employees, contractors, temporary workers, interns, and third parties with access to IT resources
- **Devices:** Company-owned and private devices (BYOD) accessing company resources
- **Locations:** {{ netbox.site.name }} and all operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Business Use
IT resources of the organization are provided primarily for business purposes. Personal use is permitted only to the extent that it does not interfere with business use and complies with security policies.

### 3.2 Responsible Use
Users are required to use IT resources responsibly, efficiently, and in accordance with all applicable policies. Misuse, waste, or damage to IT resources is prohibited.

### 3.3 Prohibited Activities
The following activities are expressly prohibited:
- Accessing, storing, or distributing illegal, offensive, or inappropriate content
- Circumventing security controls or unauthorized access to systems
- Installing unauthorized software or modifying system configurations
- Using IT resources for commercial purposes outside business activities
- Sending spam, phishing, or other malicious communications

### 3.4 Privacy and Confidentiality
Users must maintain the confidentiality of company information and must not share or publish confidential information without authorization.

### 3.5 Monitoring and Surveillance
The organization reserves the right to monitor the use of IT resources to ensure security, compliance, and proper use. Users have no expectation of privacy when using company resources.

### 3.6 Personal Responsibility
Users are personally responsible for all activities performed under their credentials. Credentials must not be shared.



## 4. Roles and Responsibilities

### RACI Matrix: Acceptable Use of IT

| Activity | CISO | IT Operations | HR | Employee | Legal/Compliance |
|----------|------|---------------|-----|----------|------------------|
| Policy creation | R/A | C | C | I | C |
| Policy communication | R | C | R | I | I |
| Training and awareness | C | C | R | R | I |
| Monitoring and surveillance | A | R | I | I | C |
| Investigate violations | R | C | R | I | C |
| Enforce sanctions | C | I | R/A | I | C |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** Thomas Weber (CISO)
- **Implementation Responsible:** IT Operations, HR
- **Control/Audit Authority:** ISMS, Internal Audit, Legal/Compliance

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0210_Guideline_Acceptable_Use_of_IT.md** - Detailed implementation guideline
- `0220_Policy_Access_Control_and_Identity_Management.md` - Access Control Policy
- `0500_Policy_Mobile_Device_and_Remote_Work.md` - Mobile Device Policy
- `0660_Policy_Information_Transfer_and_Communication.md` - Communication Policy

### Related Standards/Baselines
- Email usage guidelines
- Internet usage guidelines
- BYOD guidelines (Bring Your Own Device)
- Social media guidelines

### Related Processes
- User onboarding/offboarding
- Incident response for policy violations
- HR disciplinary procedures



## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of policy violations per quarter
- Training participation rate (Target: 100% annually)
- Number of blocked inappropriate accesses
- Average time to investigate violations
- Repeat offender rate

### Evidence
- Training records and confirmations
- Monitoring logs and audit trails
- Incident reports for violations
- Disciplinary action documentation
- Awareness campaign metrics

### Consequences for Violations
Violations of this policy will be handled according to applicable HR and compliance processes:
- **Minor Violations:** Warning, retraining, monitoring
- **Medium Violations:** Written warning, temporary access restrictions
- **Severe Violations:** Employment consequences up to termination, legal action
- **Intentional Violations:** Immediate suspension, termination, criminal prosecution

## 7. Exceptions

Exceptions to this policy are only permitted in justified cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and, if applicable, HR
- **Documentation:** All exceptions are documented and regularly reviewed
- **Time Limit:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0210_Guideline_Acceptable_Use_of_IT.md` - Detailed Guideline
- `0400_Policy_Incident_Management.md` - Incident Management Policy
- `0530_Guideline_HR_Onboarding_Role_Change_Offboarding.md` - HR Security Guideline

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.10** - Acceptable use of information and other associated assets
- **ISO/IEC 27002:2022** - Information security controls
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- Employment law requirements for IT use

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
