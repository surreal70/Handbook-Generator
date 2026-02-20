# Guideline: MFA, Password Rules and Session Management

**Document-ID:** [FRAMEWORK]-0250
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



**Document ID:** 0250  
**Document Type:** Guideline (detailed)  
**Related Policy:** 0240_Policy_Authentication_and_Passwords.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.17, A.5.18  
**Owner:** {{ meta-handbook.it_operations_manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose and Scope

This guideline implements the `0240_Policy_Authentication_and_Passwords.md` and defines detailed rules for:
- Multi-factor authentication (MFA)
- Password policies and complexity requirements
- Session management and timeouts
- Authentication methods and technologies

**Scope:** All systems, applications, and users at **AdminSend GmbH**

## 2. Multi-Factor Authentication (MFA)

### 2.1 MFA Requirements

**Mandatory for:**
- All remote access (VPN, remote desktop)
- All privileged accounts (administrators, root)
- Access to critical systems (production, financial systems)
- Cloud services and SaaS applications
- Email access from external devices
- Access to confidential data

**Optional for:**
- Local logins in the office (can be enforced via conditional access)
- Non-critical internal applications

### 2.2 MFA Methods

**Supported Factors:**

| Method | Type | Security Level | Use Case |
|--------|------|----------------|----------|
| Authenticator App (TOTP) | Possession | High | Standard for all users |
| Hardware Token (FIDO2/U2F) | Possession | Very High | Privileged users, high security |
| SMS Code | Possession | Medium | Fallback, not recommended |
| Push Notification | Possession | High | Mobile users |
| Biometrics (Fingerprint, Face ID) | Inherence | High | Mobile devices, Windows Hello |

**Recommended Method:** Authenticator app (e.g., Microsoft Authenticator, Google Authenticator, Authy)

**Not Permitted:**
- Email-based codes (too insecure)
- Security questions (vulnerable to social engineering)

### 2.3 MFA Registration

**Onboarding:**
1. New employees register MFA on first working day
2. IT support assists with setup
3. Register at least 2 MFA methods (primary + backup)
4. Generate backup codes and store securely

**Self-Service:**
- Users can manage MFA methods via self-service portal
- Changing MFA methods requires re-authentication
- Loss of MFA device: IT support process for reset

### 2.4 MFA Bypass and Emergency Access

**Break-Glass Accounts:**
- Emergency accounts without MFA for system recovery
- Secured in safe, only for emergencies
- Usage is immediately escalated to CISO
- Change password after each use

**Temporary MFA Bypass:**
- Only in exceptional cases (e.g., device loss)
- Approval by IT security required
- Maximum 24 hours, then automatic suspension
- Increased monitoring during bypass period

## 3. Password Policies

### 3.1 Password Complexity

**Requirements for Standard Users:**
- **Minimum Length:** 12 characters
- **Complexity:** At least 3 of 4 character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (!@#$%^&*)
- **No Dictionary Words:** Password must not be in common password list
- **No Personal Information:** No name, date of birth, username

**Requirements for Privileged Users:**
- **Minimum Length:** 16 characters
- **Complexity:** All 4 character types required
- **Passphrase Recommended:** E.g., "Coffee!Morning@2024#Secure"

**Technical Enforcement:**
- Active Directory Group Policy Objects (GPOs)
- Azure AD Password Protection
- Password filter for common password checking

### 3.2 Password Change

**Regular Change:**
- **Standard Users:** Every 90 days (optional if MFA active)
- **Privileged Users:** Every 60 days (mandatory)
- **Service Accounts:** Every 180 days or upon personnel change

**Forced Change:**
- At first login (initial password)
- After password reset by IT support
- When compromise is suspected
- After security incidents

**Password History:**
- Last 12 passwords cannot be reused
- Prevents rotation between few passwords

### 3.3 Password Reset

**Self-Service Password Reset (SSPR):**
- Users can reset password themselves via {{ meta-handbook.iam_sspr_url }}
- Verification via:
  - MFA method (authenticator app, SMS)
  - Alternative email address
  - Security questions (only as fallback)
- Audit log for all password resets

**IT Support Reset:**
- When all SSPR methods are lost
- Identity verification required (ID card, employee ID)
- Temporary password, must be changed at first login
- Documentation in ticket system

**Emergency Reset:**
- For locked accounts outside business hours
- On-call IT support available
- Enhanced verification (supervisor confirmation)

### 3.4 Password Manager

**Recommendation:**
- Use of password manager for all users
- Enterprise solution: {{ meta-handbook.security_password_manager }} (e.g., 1Password, Bitwarden)
- Central management of shared credentials

**Features:**
- Generation of strong, random passwords
- Secure encrypted storage
- Browser integration for auto-fill
- Sharing of credentials within team (encrypted)
- Audit log for access

**Training:**
- Onboarding training for new employees
- Best practices for password manager usage
- Avoiding password reuse

## 4. Session Management

### 4.1 Session Timeouts

**Inactivity Timeouts:**

| System Type | Timeout | Justification |
|-------------|---------|---------------|
| Workstation (local) | 15 minutes | Physical access possible |
| VPN Connection | 8 hours | Remote access, re-auth daily |
| Web Applications | 30 minutes | Balance between security and usability |
| Privileged Sessions | 10 minutes | Elevated risk |
| Mobile Apps | 5 minutes | Device loss risk |

**Absolute Session Limits:**
- **Standard Users:** Max. 12 hours, then re-authentication
- **Privileged Users:** Max. 4 hours, then re-authentication
- **Remote Access:** Max. 8 hours, then re-authentication

### 4.2 Screen Lock

**Automatic Lock:**
- After inactivity timeout (see above)
- Unlock only with password or biometrics
- No display of sensitive information on lock screen

**Manual Lock:**
- Users must lock workstation when leaving (Windows+L, Ctrl+Alt+Del)
- Awareness campaigns on "Clean Desk Policy"
- Spot checks by security team

### 4.3 Concurrent Sessions

**Limits:**
- **Standard Users:** Max. 3 concurrent sessions
- **Privileged Users:** Max. 2 concurrent sessions
- **Service Accounts:** Max. 1 session (prevents credential sharing)

**Monitoring:**
- Alerts for unusual session patterns
- Automatic suspension on suspected account sharing
- Geolocation checks (impossible travel)

### 4.4 Session Security

**Technical Controls:**
- **Session Tokens:** Cryptographically secure, random tokens
- **Token Rotation:** New tokens after re-authentication
- **Secure Cookies:** HttpOnly, Secure, SameSite flags
- **Session Fixation Protection:** New session ID after login
- **HTTPS Enforcement:** All sessions over encrypted connections

## 5. Authentication Methods

### 5.1 Single Sign-On (SSO)

**Implementation:**
- **Identity Provider:** {{ meta-handbook.iam_idp }} (e.g., Azure AD, Okta)
- **Protocols:** SAML 2.0, OAuth 2.0, OpenID Connect
- **Applications:** All cloud SaaS applications via SSO

**Benefits:**
- Single login for all applications
- Central authentication and MFA
- Reduced password fatigue
- Simplified offboarding (central suspension)

**Conditional Access:**
- Risk-based authentication
- Device compliance checks
- Geolocation-based policies
- MFA enforcement at elevated risk

### 5.2 Certificate-Based Authentication

**Use Cases:**
- Machine-to-machine authentication
- VPN access (in addition to MFA)
- Wireless network (802.1X)
- Code signing and email encryption

**PKI Infrastructure:**
- Internal Certificate Authority (CA): {{ meta-handbook.pki_ca }}
- Certificate lifecycle management
- Automatic renewal before expiration
- Revocation checks (CRL, OCSP)

### 5.3 Biometric Authentication

**Supported Methods:**
- **Windows Hello for Business:** Fingerprint, facial recognition
- **Mobile Devices:** Touch ID, Face ID
- **Only as Second Factor:** Biometrics do not replace password

**Data Protection:**
- Biometric data stored locally on device (not centrally)
- No transmission of raw biometric data
- GDPR-compliant processing

## 6. Service Accounts and Technical Accounts

### 6.1 Service Account Policies

**Requirements:**
- **No Interactive Logins:** Service accounts must not be used for human logins
- **Strong Passwords:** At least 24 characters, randomly generated
- **Password Rotation:** Every 180 days or upon personnel change
- **Documentation:** Purpose, owner, systems used

**Management:**
- Central management in password manager or PAM system
- CISO approval for new service accounts
- Regular reviews (quarterly)
- Deactivation of unused accounts

### 6.2 API Keys and Tokens

**Best Practices:**
- **Rotation:** Rotate API keys every 90 days
- **Least Privilege:** Minimal permissions for API keys
- **Secrets Management:** Storage in secrets manager (e.g., HashiCorp Vault, Azure Key Vault)
- **No Hardcoding:** API keys not in code or config files

**Monitoring:**
- Logging of all API access
- Alerts for unusual API usage patterns
- Rate limiting for API calls

## 7. Monitoring and Alerting

### 7.1 Authentication Monitoring

**Monitored Events:**
- Failed login attempts (brute-force detection)
- Successful logins from unusual locations
- MFA bypass attempts
- Password resets (especially privileged accounts)
- Concurrent sessions from different IPs

**Automatic Alerts:**
- **5 failed logins:** Warning to user
- **10 failed logins:** Account lockout (30 minutes)
- **Login from new device/location:** MFA challenge
- **Impossible travel:** Alert to security team (e.g., login in Germany, 1 hour later in USA)

### 7.2 Account Lockout

**Automatic Lockout:**
- After 10 failed login attempts
- Lockout duration: 30 minutes (automatic unlock)
- Manual unlock by IT support possible

**Privileged Accounts:**
- Already after 5 failed attempts
- Manual unlock only by CISO or IT security
- Investigation upon lockout (possible attack)

## 8. Compliance and Audit

### 8.1 Key Performance Indicators (KPIs)

| Metric | Target Value | Measurement |
|--------|--------------|-------------|
| MFA Adoption Rate | > 99% | IAM system |
| Password Complexity Compliance | 100% | AD reports |
| Failed Logins | < 100 per day | SIEM |
| Password Resets | < 50 per month | IAM system |
| Session Timeout Compliance | > 95% | Endpoint monitoring |

### 8.2 Audit Evidence

**Documentation:**
- Authentication logs (success and failure)
- MFA registrations and usage
- Password changes and resets
- Account lockouts and unlocks
- Privileged access

**Retention:**
- Authentication logs: {{ meta-handbook.retention_log_years }} years
- Audit trails: {{ meta-handbook.retention_audit_years }} years

## 9. References

### Internal Documents
- `0240_Policy_Authentication_and_Passwords.md` - Parent policy
- `0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md` - IAM processes
- `0320_Policy_Logging_und_Monitoring.md` - Logging policy

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.17** - Authentication information
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights
- **NIST SP 800-63B** - Digital Identity Guidelines (Authentication)
- **OWASP Authentication Cheat Sheet**

**Approved by:**  
[TODO], CISO  
Date: [TODO]

**Next Review:** [TODO]

