# Access Control

**Document-ID:** [FRAMEWORK]-0400
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



## 1. Purpose

This document describes the Access Control technical safeguards for AdminSend GmbH to implement technical policies and procedures for electronic information systems that maintain ePHI to allow access only to authorized persons or software programs.

### 1.1 HIPAA Requirement

**Standard:** §164.312(a)(1) - Access Control (Required)

**Implementation Specifications:**
- §164.312(a)(2)(i) - Unique User Identification (Required)
- §164.312(a)(2)(ii) - Emergency Access Procedure (Required)
- §164.312(a)(2)(iii) - Automatic Logoff (Addressable)
- §164.312(a)(2)(iv) - Encryption and Decryption (Addressable)

## 2. Unique User Identification

### 2.1 User ID Requirements

**Requirement:** Assign a unique name and/or number for identifying and tracking user identity.

**User ID Standards:**
- Unique to each individual user
- Not shared between users
- Not reused after termination
- Format: [TODO: firstname.lastname, employee ID, etc.]
- Minimum length: [TODO: 6 characters]

**Prohibited Practices:**
- Shared accounts
- Generic accounts (except for specific approved purposes)
- Default accounts (must be disabled or renamed)
- Guest accounts (must be disabled)

### 2.2 User Account Management

**Account Creation Process:**
1. Manager submits access request
2. HR verifies employment status
3. Security Officer approves based on role
4. IT creates unique user account
5. User notified of account creation
6. User completes initial login and password setup

**Account Types:**
| Account Type | Purpose | Approval Required | Monitoring |
|--------------|---------|-------------------|------------|
| Standard User | Regular workforce member | Manager | Standard |
| Privileged User | System administration | IT Manager + Security Officer | Enhanced |
| Service Account | Automated processes | Security Officer | Enhanced |
| Emergency Access | Break-glass access | Security Officer | Immediate review |

### 2.3 Authentication Methods

**Primary Authentication:**
- Username and password
- Minimum password requirements:
  - Length: [TODO: 12 characters minimum]
  - Complexity: Upper, lower, number, special character
  - History: [TODO: 12 previous passwords remembered]
  - Age: Maximum [TODO: 90 days], minimum [TODO: 1 day]
  - Lockout: [TODO: 5 failed attempts], lockout duration [TODO: 30 minutes]

**Multi-Factor Authentication (MFA):**
- Required for: Remote access, privileged accounts, ePHI access from untrusted networks
- Methods: SMS code, authenticator app, hardware token, biometric
- Backup codes provided for MFA recovery

**Single Sign-On (SSO):**
- Centralized authentication
- Reduces password fatigue
- Audit trail of access
- Integration with MFA

## 3. Emergency Access Procedure

### 3.1 Emergency Access Definition

**Emergency Situations:**
- System failure preventing normal authentication
- Natural disaster
- Cyberattack requiring immediate response
- Life-threatening patient situation requiring immediate ePHI access
- Critical system maintenance

### 3.2 Break-Glass Accounts

**Break-Glass Account Characteristics:**
- Highly privileged access
- Used only in emergencies
- Credentials secured (sealed envelope, password vault)
- Immediate notification upon use
- Automatic logging of all activities
- Immediate review required

**Break-Glass Account Inventory:**
| Account ID | System | Access Level | Credential Location | Last Used | Reviewed By |
|------------|--------|--------------|---------------------|-----------|-------------|
| [TODO: BG-001] | Active Directory | Domain Admin | [TODO: Secure vault] | [TODO: Date] | [TODO: Security Officer] |
| [TODO: BG-002] | EHR System | System Admin | [TODO: Secure vault] | [TODO: Date] | [TODO: Security Officer] |

### 3.3 Emergency Access Process

**Process Steps:**
1. **Determination:** Determine emergency situation exists
2. **Authorization:** Security Officer or designee authorizes emergency access
3. **Access:** Use break-glass credentials
4. **Logging:** All activities automatically logged
5. **Notification:** Security Officer immediately notified
6. **Monitoring:** Real-time monitoring of emergency access activities
7. **Review:** Immediate post-access review
8. **Documentation:** Document emergency, actions taken, justification
9. **Credential Rotation:** Change break-glass credentials after use

**Emergency Access Log:**
| Date/Time | User | System | Reason | Authorized By | Actions Taken | Review Date |
|-----------|------|--------|--------|---------------|---------------|-------------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Automatic Logoff

### 4.1 Automatic Logoff Requirements

**Requirement:** Implement electronic procedures that terminate an electronic session after a predetermined time of inactivity.

**Rationale:** Prevent unauthorized access to ePHI when workstation left unattended.

### 4.2 Timeout Settings

**Inactivity Timeouts:**
| System/Application | Timeout Period | Action | Override Allowed |
|--------------------|----------------|--------|------------------|
| Workstations | [TODO: 15 minutes] | Screen lock | No |
| EHR System | [TODO: 10 minutes] | Session timeout | No |
| Web Applications | [TODO: 20 minutes] | Session timeout | No |
| VPN | [TODO: 30 minutes] | Disconnect | No |
| Mobile Devices | [TODO: 5 minutes] | Screen lock | No |

**Timeout Actions:**
- **Screen Lock:** Requires password to unlock, session remains active
- **Session Timeout:** Terminates session, requires re-authentication
- **Disconnect:** Terminates network connection

### 4.3 Implementation

**Technical Implementation:**
- Group Policy (Windows)
- Configuration profiles (macOS, iOS)
- Application-level timeouts
- Network-level timeouts (VPN, firewall)

**User Notification:**
- Warning before timeout (e.g., 2 minutes)
- Clear indication of locked state
- Instructions for unlocking

## 5. Encryption and Decryption

### 5.1 Encryption Requirements

**Requirement:** Implement a mechanism to encrypt and decrypt ePHI.

**Encryption Use Cases:**
- ePHI at rest (stored data)
- ePHI in transit (transmitted data)
- Backup media
- Mobile devices
- Removable media
- Email containing ePHI

### 5.2 Encryption Standards

**Approved Encryption Algorithms:**
- **Symmetric:** AES-256, AES-128
- **Asymmetric:** RSA-2048 or higher, ECC
- **Hashing:** SHA-256, SHA-512
- **TLS:** TLS 1.2 or higher

**Prohibited Algorithms:**
- DES, 3DES
- MD5, SHA-1
- SSL, TLS 1.0, TLS 1.1
- RC4

### 5.3 Encryption at Rest

**Full Disk Encryption:**
- All workstations and laptops: [TODO: BitLocker, FileVault, LUKS]
- All servers with ePHI: [TODO: BitLocker, dm-crypt]
- All mobile devices: [TODO: Native device encryption]

**Database Encryption:**
- Transparent Data Encryption (TDE) for databases
- Column-level encryption for sensitive fields
- Encryption key management

**File/Folder Encryption:**
- Encrypted file systems
- Encrypted containers
- Document-level encryption

### 5.4 Encryption in Transit

**Network Encryption:**
- TLS 1.2+ for all web traffic
- VPN for remote access (IPsec, SSL VPN)
- Encrypted email (S/MIME, PGP)
- SFTP/SCP for file transfers (no FTP)
- HTTPS for all web applications

**Wireless Encryption:**
- WPA3 or WPA2-Enterprise
- No WEP or open networks
- Certificate-based authentication

### 5.5 Key Management

**Key Management Lifecycle:**
1. **Generation:** Cryptographically secure random generation
2. **Distribution:** Secure key distribution mechanisms
3. **Storage:** Hardware Security Module (HSM) or secure key vault
4. **Rotation:** Regular key rotation schedule
5. **Backup:** Secure backup of encryption keys
6. **Destruction:** Secure destruction when no longer needed

**Key Management System:**
- Centralized key management
- Access controls on keys
- Audit logging of key access
- Key escrow/recovery procedures

**Key Rotation Schedule:**
| Key Type | Rotation Frequency | Responsible |
|----------|-------------------|-------------|
| Disk encryption keys | [TODO: Annually] | IT Security |
| Database encryption keys | [TODO: Annually] | Database Admin |
| TLS certificates | [TODO: Annually or per vendor] | IT Security |
| VPN keys | [TODO: Quarterly] | Network Admin |

## 6. Access Control Lists (ACLs)

### 6.1 ACL Management

**ACL Principles:**
- Least privilege
- Need-to-know
- Separation of duties
- Defense in depth

**ACL Components:**
- User/group identity
- Resource (file, folder, application, database)
- Permissions (read, write, execute, delete)
- Conditions (time, location, device)

### 6.2 Permission Levels

**Standard Permission Levels:**
| Level | Description | Typical Roles |
|-------|-------------|---------------|
| No Access | No permissions | Default for all users |
| Read | View only | Auditors, read-only users |
| Read/Write | View and modify | Standard users |
| Full Control | All permissions | Administrators, owners |

### 6.3 ACL Review

**Review Process:**
- **Frequency:** Quarterly
- **Scope:** All ePHI resources
- **Reviewers:** Resource owners + Security Officer
- **Actions:** Remove unnecessary permissions, update for role changes

## 7. Privileged Access Management (PAM)

### 7.1 Privileged Account Definition

**Privileged Accounts:**
- System administrators
- Database administrators
- Network administrators
- Application administrators
- Security administrators

**Privileged Access Characteristics:**
- Elevated permissions
- Access to sensitive systems
- Ability to modify security controls
- Access to all ePHI

### 7.2 PAM Controls

**PAM Requirements:**
- Separate privileged accounts from standard accounts
- Just-in-time (JIT) privilege elevation
- Session recording for privileged access
- Enhanced monitoring and alerting
- Regular access reviews
- MFA required for privileged access

**PAM Solution:** [TODO: CyberArk, BeyondTrust, Thycotic, etc.]

## 8. Monitoring and Auditing

### 8.1 Access Monitoring

**Monitoring Activities:**
- Failed login attempts
- Successful logins (especially after hours)
- Privileged account usage
- Emergency access usage
- Permission changes
- Account creation/deletion
- Password resets

**Monitoring Tools:**
- SIEM (Security Information and Event Management)
- Log aggregation and analysis
- User behavior analytics (UBA)
- Automated alerting

### 8.2 Access Auditing

**Audit Activities:**
- User access reviews
- Privileged access reviews
- ACL reviews
- Inactive account reviews
- Orphaned account reviews

**Audit Frequency:**
| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| User access review | Quarterly | Managers + Security Officer |
| Privileged access review | Monthly | Security Officer |
| ACL review | Quarterly | Resource owners |
| Inactive account review | Monthly | IT + HR |

## 9. Documentation and Records

### 9.1 Required Documentation

- User account inventory
- Privileged account inventory
- Break-glass account procedures
- Emergency access logs
- Access review records
- ACL documentation
- Encryption key inventory
- Timeout configuration documentation

### 9.2 Retention

**Retention Period:** [TODO: 6 years from creation or last effective date]

**Storage Location:** [TODO: Identity management system, document repository]


