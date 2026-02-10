# User Authentication

**Document ID:** PCI-0410  
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
This template documents user authentication policies and procedures.
It aligns with PCI-DSS v4.0 Requirement 8 (Identify Users and Authenticate Access to System Components).

Customization required:
- Define authentication policies
- Document MFA requirements
- Include password policies
- Define session management
-->

## 1. Purpose

This document defines the authentication policies for {{ meta.organization.name }} in accordance with PCI-DSS Requirement 8.

### 1.1 Objectives

- **Unique Identification:** Each user uniquely identifiable
- **Strong Authentication:** Multi-Factor Authentication (MFA)
- **Secure Passwords:** Enforce password policies
- **Compliance:** Fulfillment of PCI-DSS Requirement 8

### 1.2 Scope

**Affected Systems:**
- All CDE systems
- Administrative systems
- Applications with CHD access
- Remote access systems

## 2. User Identification

### 2.1 Unique User IDs

**Requirements:**
- Each user has unique ID
- No shared accounts
- No generic accounts (except documented exceptions)
- User ID must not be reused

**Naming Convention:**
- Format: `firstname.lastname`
- For duplicates: `firstname.lastname2`
- Service accounts: `svc-servicename`
- Admin accounts: `firstname.lastname-admin`

### 2.2 Prohibited Account Types

**Not Allowed:**
- Shared accounts (multiple people, one account)
- Generic accounts (e.g., "admin", "user", "test")
- Group accounts
- Vendor default accounts (must be disabled)

**Exceptions:**
- Emergency accounts (Break-Glass) - documented
- Service accounts - documented and monitored
- Console access (only with logging)

## 3. Authentication Methods

### 3.1 Multi-Factor Authentication (MFA)

**MFA Required for:**
- All CDE access
- Administrative access
- Remote access (VPN, Jump Server)
- Privileged accounts
- Access to CHD

**MFA Factors:**

1. **Something You Know:**
   - Password
   - PIN

2. **Something You Have:**
   - Hardware token
   - Software token (Authenticator App)
   - Smart card
   - SMS (backup only)

3. **Something You Are:**
   - Biometrics (fingerprint, facial recognition)

**MFA Implementation:**
- At least 2 different factors
- Factors must be independent
- MFA System: [TODO: Name of MFA system]

### 3.2 Password Authentication

**Password Requirements:**

- **Minimum Length:** 12 characters (15 for admin accounts)
- **Complexity:**
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (!@#$%^&*)
- **No Dictionary Words**
- **No Personal Information** (name, birthdate, etc.)
- **No Reuse** of last 4 passwords

**Password Change:**
- Every 90 days for standard users
- Every 90 days for admin accounts
- Immediately upon suspicion of compromise
- Upon first login

**Password Storage:**
- Only as hash (bcrypt, PBKDF2, Argon2)
- Never in cleartext
- Salt for each hash
- No reversible encryption

### 3.3 Certificate-Based Authentication

**Usage:**
- Server-to-server communication
- API authentication
- VPN access (in addition to MFA)

**Requirements:**
- Certificates from trusted CA
- Regular renewal
- Revocation checking (CRL/OCSP)
- Secure key storage

## 4. Account Management

### 4.1 Account Creation

**Process:**
1. Approved access request
2. Create unique user ID
3. Generate temporary password
4. MFA registration
5. Notify user
6. Force password change on first login

### 4.2 Account Deactivation

**Automatic Deactivation:**
- After 90 days of inactivity
- Upon employee termination
- Upon role change (old account)

**Manual Deactivation:**
- During security incidents
- Upon suspicion of compromise
- At manager's request

**Process:**
1. Deactivate account (do not delete)
2. Terminate all sessions
3. Validate access (should be blocked)
4. Document

### 4.3 Account Deletion

**Timeframe:**
- 90 days after deactivation
- After completion of audits/investigations
- After retention requirements

**Process:**
1. Confirm account no longer needed
2. Backup account data (if required)
3. Delete account
4. Document

## 5. Password Management

### 5.1 Password Reset

**Self-Service Reset:**
- Via Identity Management System
- After successful identity verification
- Security questions or email verification
- MFA verification

**Helpdesk Reset:**
- Identity verification required
- Temporary password
- Force password change on next login
- Document reset

### 5.2 Password Lockout

**Account Lockout After:**
- 6 failed login attempts
- Lockout for 30 minutes
- Or manual unlock by admin

**Unlock:**
- Automatically after 30 minutes
- Or by helpdesk after identity verification
- Document unlock

### 5.3 Password Vault

**For Privileged Passwords:**
- Central password vault solution
- Automatic password rotation
- Check-out/check-in process
- Session recording
- Complete logging

**Vault System:** [TODO: Name of vault system]

## 6. Session Management

### 6.1 Session Timeouts

**Inactivity Timeout:**
- 15 minutes for CDE systems
- 30 minutes for corporate systems
- 5 minutes for privileged sessions

**Maximum Session Duration:**
- 8 hours for standard users
- 4 hours for admin sessions
- Re-authentication required

### 6.2 Session Security

**Requirements:**
- Unique session IDs
- Session ID rotation after login
- Secure session cookies (HttpOnly, Secure, SameSite)
- Session invalidation on logout
- No session IDs in URLs

### 6.3 Concurrent Sessions

**Restrictions:**
- Maximum 2 concurrent sessions per user
- Only 1 privileged session at a time
- Warning on new session
- Option to terminate old sessions

## 7. Remote Authentication

### 7.1 VPN Access

**Authentication:**
- Username + Password
- Plus MFA (Hardware token or Authenticator App)
- Certificate-based authentication (optional)

**Authorization:**
- Only authorized users
- Access to specific network segments
- Complete logging

### 7.2 Jump Server

**Authentication:**
- MFA required
- Privileged accounts
- Session recording
- Time-limited access

**Access Control:**
- Only from authorized source IPs
- Only to authorized target systems
- Complete logging

## 8. Application Authentication

### 8.1 Web Applications

**Authentication:**
- Username + Password
- MFA for CDE applications
- Session management
- HTTPS required

**Security Measures:**
- Brute-force protection (Rate Limiting)
- CAPTCHA after multiple failures
- Account lockout
- Secure password storage

### 8.2 API Authentication

**Methods:**
- API Keys (with expiration)
- OAuth 2.0
- JWT (JSON Web Tokens)
- Mutual TLS

**Requirements:**
- No API keys in code
- API key rotation
- Scope-based authorization
- Rate limiting

## 9. Service Account Management

### 9.1 Service Accounts

**Requirements:**
- Unique service account IDs
- Documented usage
- Strong passwords (32+ characters)
- Regular password rotation (90 days)
- No interactive logins

**Naming Convention:**
- Format: `svc-servicename`
- Example: `svc-payment-gateway`

### 9.2 Service Account Monitoring

**Monitoring:**
- Log all service account activities
- Alerts on unusual activities
- Regular review of usage
- Deactivation of unused accounts

## 10. Authentication Logging

### 10.1 Logged Events

**Successful Authentication:**
- User ID
- Timestamp
- Source IP address
- Target system
- Authentication method

**Failed Authentication:**
- User ID (or attempt)
- Timestamp
- Source IP address
- Target system
- Failure reason

**Other Events:**
- Password changes
- Account lockouts
- Account unlocks
- MFA registration
- Privileged actions

### 10.2 Log Retention

**Retention:**
- 90 days online
- 1 year archive
- Immutable (WORM)

**Log Forwarding:**
- To SIEM system
- Real-time transmission
- Encrypted transmission

## 11. Authentication Monitoring

### 11.1 Alerting

| Alert | Condition | Severity | Notification |
|-------|-----------|----------|--------------|
| Multiple failed logins | >5 in 15 min | Medium | SOC |
| Admin login outside business hours | After 10 PM | Medium | SOC + Manager |
| MFA failure | >3 failures | Low | SOC |
| Account lockout | Any lockout | Low | Helpdesk |
| Privileged access | Any access | Low | SIEM |
| Password change | Outside business hours | Low | SIEM |

### 11.2 Anomaly Detection

**Monitoring:**
- Unusual login times
- Unusual source IPs
- Geographic anomalies
- Multiple concurrent logins
- Privileged access

## 12. Vendor Default Accounts

### 12.1 Default Account Management

**Requirements:**
- Identify all default accounts
- Disable or delete default accounts
- If required: Change password
- Document all default accounts

**Examples:**
- admin/admin
- root/root
- Administrator/password
- sa (SQL Server)

### 12.2 Default Account Inventory

| System | Default Account | Status | Action |
|--------|-----------------|--------|--------|
| [TODO: System 1] | admin | Disabled | Deleted |
| [TODO: System 2] | root | Active | Password changed |
| [TODO: System 3] | Administrator | Disabled | Renamed |

## 13. Authentication Testing

### 13.1 Penetration Tests

**Annually:**
- Test authentication mechanisms
- Simulate brute-force attacks
- MFA bypass attempts
- Session management tests

### 13.2 Vulnerability Scans

**Quarterly:**
- Identify weak passwords
- Identify default accounts
- Authentication vulnerabilities

## 14. Compliance Validation

### 14.1 Validation Activities

**Quarterly:**
- Password policy compliance
- Validate MFA implementation
- Identify inactive accounts
- Review default accounts

**Annually:**
- Complete authentication audit
- Penetration testing
- Compliance assessment

### 14.2 Validation Documentation

**Required Evidence:**
- Authentication policies
- MFA configuration
- Password policy configuration
- Account management protocols
- Penetration test reports

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
