# Policy: Authentication and Passwords

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for authentication and password management.
It ensures that user authentication is strong, secure, and appropriate for the
level of risk. Customize based on your organization's authentication requirements
and security maturity (MFA adoption, passwordless strategies, etc.).

ISO 27001:2022 Annex A Reference: A.5.17, A.5.18
-->

**Document ID:** 0240  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.17, A.5.18 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the principles for authentication and password management at **{{ meta.organization.name }}**. It ensures that user identity is securely verified and authentication information is appropriately protected.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta.organization.name }}
- **Systems:** All IT systems, applications, databases, networks, cloud services
- **Persons:** All employees, contractors, suppliers, and third parties with access to IT resources
- **Authentication Methods:** Passwords, multi-factor authentication (MFA), biometric methods, tokens
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Strong Authentication
All access to IT systems and applications requires secure authentication. The strength of authentication is based on the protection requirements of the resource and the risk.

### 3.2 Multi-Factor Authentication (MFA)
Multi-factor authentication (MFA) is mandatory for access to critical systems, privileged accounts, and remote access. MFA combines at least two independent factors:
- Knowledge (password, PIN)
- Possession (token, smartphone, smartcard)
- Biometrics (fingerprint, facial recognition)

### 3.3 Password Requirements
Passwords must meet the following minimum requirements:
- Sufficient length and complexity (details in guideline)
- No reuse of old passwords
- No sharing or writing down
- Regular change when compromise is suspected

### 3.4 Passwordless Authentication
The organization promotes the use of passwordless authentication methods (e.g., FIDO2, Windows Hello, biometric methods) where technically feasible and secure.

### 3.5 Session Management
Authenticated sessions are protected by appropriate measures:
- Automatic lockout on inactivity
- Secure session tokens
- Logout functionality
- No concurrent sessions for privileged accounts

### 3.6 Protection of Authentication Information
Passwords and other authentication information are stored securely:
- Encrypted or hashed storage (no plaintext passwords)
- Secure transmission (TLS/SSL)
- Protection against brute-force attacks (account lockout, rate limiting)

### 3.7 Privileged Accounts
Privileged accounts (administrators, root, service accounts) are subject to stricter authentication requirements:
- Mandatory MFA
- Separate accounts for privileged activities
- Just-in-Time (JIT) access where possible
- Comprehensive logging

### 3.8 Password Reset and Account Recovery
Password reset and account recovery processes must be securely designed and verify user identity before granting access.

## 4. Roles and Responsibilities

### RACI Matrix: Authentication and Passwords

| Activity | CISO | IT Operations | Employee | IAM Team | Security Operations |
|----------|------|---------------|----------|----------|---------------------|
| Policy Creation | R/A | C | I | C | C |
| MFA Implementation | A | R | I | R | C |
| Password Reset | I | R | R | R | I |
| Session Monitoring | C | C | I | C | R/A |
| Brute-Force Protection | A | R | I | C | R |
| Incident Response | R/A | C | I | C | R |

**Legend:** R = Responsible (Execution), A = Accountable (Accountable), C = Consulted (Consulted), I = Informed (Informed)

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **IAM Manager:** {{ meta.it.iam_manager }}
- **Implementation Responsible:** IT operations, IAM team
- **Control/Audit Function:** ISMS, internal audit, security operations

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md** - Detailed implementation guideline
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access control policy
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Cryptography policy
- `0400_Policy_Incident_Management.md` - Incident management policy

### Related Standards/Baselines
- Password complexity requirements
- MFA implementation standard
- Session timeout configurations
- Privileged Access Management (PAM) standard

### Related Processes
- Password reset process
- Account recovery process
- MFA enrollment process
- Incident response for authentication incidents

## 6. Compliance, Monitoring, and Enforcement

### Metrics and KPIs
- MFA adoption rate (target: 100% for critical systems)
- Number of password reset requests per month
- Number of failed authentication attempts
- Number of account lockouts
- Average password strength (entropy)
- Number of compromised accounts

### Evidence and Proof
- Authentication logs and audit trails
- MFA enrollment status
- Password policy compliance reports
- Brute-force detection logs
- Incident reports for authentication incidents
- Penetration test results

### Consequences for Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Weak passwords:** Forced password change, retraining
- **Password sharing:** Warning up to termination
- **MFA bypass:** Immediate suspension, investigation
- **Repeated violations:** Employment law consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO
- **Documentation:** All exceptions are documented in the risk register
- **Time Limit:** Exceptions are generally time-limited and regularly reviewed
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS policy
- `0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md` - Detailed guideline
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access control policy
- `0080_ISMS_Risikoregister_Template.md` - Risk register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.17** - Authentication information
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights review
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-63B** - Digital Identity Guidelines: Authentication and Lifecycle Management
- **NIST SP 800-63-3** - Digital Identity Guidelines
- **BSI TR-02102** - Cryptographic Procedures: Recommendations and Key Lengths

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
