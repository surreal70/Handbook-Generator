# Access Control

**Document-ID:** PCI-DSS-0400
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

This document defines the access control policies for AdminSend GmbH in accordance with PCI-DSS Requirement 7.

### 1.1 Objectives

- **Need-to-Know Principle:** Access only for authorized personnel
- **Least Privilege:** Minimum required access rights
- **Role-Based Access Control:** RBAC implementation
- **Compliance:** Fulfillment of PCI-DSS Requirement 7

### 1.2 Scope

**Affected Systems:**
- All CDE systems
- Systems with cardholder data
- Administrative systems
- Databases with CHD

## 2. Access Control Principles

### 2.1 Need-to-Know

**Principle:**
- Access only for persons with business necessity
- Documented justification required
- Regular review of access rights

### 2.2 Least Privilege

**Principle:**
- Minimum required permissions
- No unnecessary administrator rights
- Time-limited privileged access

### 2.3 Separation of Duties

**Principle:**
- Separation of critical functions
- No single person with complete control
- Four-eyes principle for critical operations

## 3. Role-Based Access Control (RBAC)

### 3.1 Defined Roles

| Role | Description | CDE Access | CHD Access |
|------|-------------|------------|------------|
| Payment Administrator | Full payment system administration | Yes | Yes (full) |
| System Administrator | Server and network administration | Yes | No |
| Database Administrator | Database management | Yes | Yes (encrypted) |
| Application Administrator | Application management | Yes | No |
| Security Administrator | Security system administration | Yes | No |
| Cashier | POS operation | Limited | Yes (input only) |
| Support Staff | Customer service | Limited | Yes (query only, masked) |
| Developer | Software development | No | No |
| Auditor | Compliance review | Read-only | Yes (logs only) |

### 3.2 Permission Matrix

| System/Resource | Payment Admin | Sys Admin | DB Admin | App Admin | Cashier | Support |
|-----------------|---------------|-----------|----------|-----------|---------|---------|
| Payment Gateway | RWX | RW | R | RW | - | R |
| CDE Database | RWX | R | RWX | R | - | R (masked) |
| POS Terminal | RW | RW | - | RW | RW | R |
| Firewall | RW | RWX | - | - | - | - |
| SIEM | RW | RW | - | - | - | R |
| Backup System | RW | RWX | RW | - | - | - |

**Legend:** R = Read, W = Write, X = Execute, - = No Access

## 4. Access Management Process

### 4.1 Access Request

**Process:**

1. **Request:** Form with justification
2. **Manager Approval:** Supervisor approves
3. **Security Review:** IT Security reviews
4. **CISO Approval:** Required for CDE access
5. **Provisioning:** IT implements access
6. **Documentation:** Access is documented
7. **Notification:** User is informed

**Approval Matrix:**

| Access Type | Approver | Documentation |
|-------------|----------|---------------|
| CDE Access | CISO | Complete |
| CHD Access | CISO + Manager | Complete |
| Corporate Access | Manager | Standard |
| Temporary Access | IT Security | With expiration date |

### 4.2 Access Modification

**Process for Role Change:**

1. **Identification:** Role change detected
2. **Assessment:** New access requirements
3. **Approval:** Same as new request
4. **Revocation:** Remove old permissions
5. **Provisioning:** Grant new permissions
6. **Validation:** Test access

### 4.3 Access Revocation

**Process for Termination:**

1. **Notification:** HR informs IT
2. **Immediate Revocation:** Deactivate all access
3. **Return:** Hardware and access credentials
4. **Documentation:** Document revocation
5. **Validation:** Test access (should be blocked)

**Timeframe:**
- Upon termination: Immediately on last working day
- Upon transfer: Within 24 hours
- Upon suspicion: Immediately

## 5. Privileged Access

### 5.1 Administrative Accounts

**Requirements:**
- Separate admin accounts (not for daily work)
- Strong authentication (MFA required)
- Complete logging of all actions
- Regular review

**Naming Convention:**
- Standard user: `firstname.lastname`
- Admin user: `firstname.lastname-admin`
- Service account: `svc-servicename`

### 5.2 Privileged Access Management (PAM)

**PAM System:** [TODO: Name of PAM system]

**Functions:**
- Just-in-Time (JIT) access
- Session recording
- Password vaulting
- Automatic password rotation

**Process:**
1. Admin requests privileged access
2. Approval by CISO (automatic or manual)
3. Time-limited access granted
4. Session is recorded
5. Automatic revocation after expiration

### 5.3 Emergency Access

**Break-Glass Accounts:**
- Only for emergencies
- Password in sealed envelope
- Usage must be documented
- Change password after use

**Process:**
1. Emergency identified
2. Open envelope (with witness)
3. Use access
4. Document incident
5. Change password immediately
6. Inform CISO

## 6. Access Control for Cardholder Data

### 6.1 CHD Access Restrictions

**Full PAN Access:**
- Only for authorized roles
- Documented business justification
- CISO approval required
- Complete logging

**Masked PAN Access:**
- Only last 4 digits visible
- For support and reporting
- Standard approval sufficient

**No PAN Access:**
- All other users
- Developers (test data only)
- External service providers (without necessity)

### 6.2 Data Masking

**Masking Rules:**
- PAN: Only first 6 and last 4 digits (e.g., 123456******1234)
- Expiration date: Fully masked
- CVV: Never display (must not be stored)
- Cardholder name: Partially masked (e.g., John D******)

**Exceptions:**
- Payment administrators (full access)
- Only with CISO approval
- Complete logging

## 7. Application Access Control

### 7.1 Application Permissions

**Permission Model:**
- Role-based permissions
- Granular function rights
- No shared accounts
- Unique user IDs

**Example (Payment Application):**

| Function | Payment Admin | Cashier | Support |
|----------|---------------|---------|---------|
| Perform transaction | Yes | Yes | No |
| Cancel transaction | Yes | Limited | No |
| View reports | Yes | No | Yes (masked) |
| Change configuration | Yes | No | No |
| Manage users | Yes | No | No |

### 7.2 API Access Control

**API Authentication:**
- API keys with expiration
- OAuth 2.0 for external APIs
- Mutual TLS for critical APIs
- Rate limiting

**API Authorization:**
- Scope-based permissions
- Minimum required scopes
- Logging of all API calls

## 8. Database Access Control

### 8.1 Database Permissions

**Permission Model:**
- Separate DB accounts per application
- No shared accounts
- Least privilege for applications
- DBA access only for administration

**Example:**

| Account | Type | Permissions | Purpose |
|---------|------|-------------|---------|
| app_payment | Application | SELECT, INSERT, UPDATE | Payment application |
| app_reporting | Application | SELECT | Reporting |
| dba_admin | DBA | ALL | Administration |
| backup_user | Service | SELECT | Backup |

### 8.2 Encrypted Columns

**CHD Columns:**
- PAN: Encrypted (AES-256)
- Access only via decryption function
- Logging of all decryptions
- Only authorized accounts

## 9. Network Access Control

### 9.1 Network Access

**Access Methods:**
- VPN for remote access
- Jump server for admin access
- No direct internet connection to CDE

**Authentication:**
- Multi-Factor Authentication (MFA)
- Certificate-based authentication
- Strong passwords

### 9.2 Network Segmentation

**Access Control Between Segments:**
- Firewall rules
- ACLs on switches
- Micro-segmentation

## 10. Physical Access Control

### 10.1 Data Center

**Access Control:**
- Badge system
- Biometric authentication
- Escort requirement for visitors
- Logging of all access

**Authorized Persons:**
- Data center personnel
- Authorized administrators
- Maintenance personnel (with escort)

### 10.2 Offices with CDE Access

**Access Control:**
- Locked rooms
- Badge access
- Visitor log

## 11. Service Provider Access Control

### 11.1 Service Provider Access

**Requirements:**
- Separate accounts for each service provider
- Time-limited access
- Complete logging
- PCI-DSS AOC required

**Approval Process:**
1. Service provider contract with PCI clauses
2. AOC validation
3. CISO approval
4. Time-limited access
5. Monitoring during access

### 11.2 Remote Support

**Process:**
- Only after approval
- Session recording
- Accompanied by internal admin
- Immediate revocation after completion

## 12. Access Control Monitoring

### 12.1 Logging

**Logged Events:**
- Successful logins
- Failed logins
- Privileged actions
- Access to CHD
- Permission changes

**Log Retention:** [TODO: 90 days online, 1 year archive]

### 12.2 Alerting

| Alert | Condition | Severity | Notification |
|-------|-----------|----------|--------------|
| Multiple failed logins | >5 in 15 min | Medium | SOC |
| Admin login outside business hours | After 10 PM | Medium | SOC + Manager |
| CHD access | Any access | Low | SIEM |
| Permission change | Any change | Medium | IT Security |

## 13. Access Control Reviews

### 13.1 Quarterly Review

**Review Process:**

1. **User Review:** All users with CDE access
2. **Permission Review:** Validate all permissions
3. **Inactive Accounts:** Identify and deactivate
4. **Documentation:** Document results
5. **Approval:** CISO confirmation

**Last Review:** [TODO: Date]  
**Next Review:** [TODO: Date]  
**Responsible:** [TODO: IT Security Team]

### 13.2 Recertification

**Annual Recertification:**
- All users with CDE access
- Manager confirms business necessity
- IT Security validates permissions
- CISO approves

## 14. Compliance Validation

### 14.1 Validation Activities

**Quarterly:**
- Access control review
- Inactive account cleanup
- Permission documentation

**Annually:**
- Complete recertification
- Penetration testing
- Compliance audit

### 14.2 Validation Documentation

**Required Evidence:**
- Access control policies
- Permission matrix
- Approval evidence
- Review protocols
- Recertification evidence


