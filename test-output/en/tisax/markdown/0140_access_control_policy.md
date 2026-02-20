
Document-ID: tisax-0140

Status: Draft
Classification: Internal

# Access Control Policy

**Document-ID:** [FRAMEWORK]-0140
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

## Purpose

This document defines the policies and requirements for access control to information systems and resources according to TISAX requirements.

## Scope

This policy applies to all users, systems, and resources of [TODO].

## Fundamental Principles

### Need-to-Know Principle

Access is only granted when:
- Business necessity exists
- Tasks require it
- Approval is present

### Least-Privilege Principle

Users receive:
- Minimum required permissions
- Time-limited access
- Role-based rights

### Segregation of Duties

Critical functions are separated:
- No single person has complete control
- Four-eyes principle for critical actions
- Separation of development and production

## Access Control Process

### 1. User Registration

**New Employees:**
- Request by supervisor
- Approval by IT and information security
- Creation of user accounts
- Assignment of standard permissions
- Training before access grant

**External Users:**
- Contractual agreement required
- Time-limited access
- Sponsorship by internal employee
- Extended monitoring

### 2. Permission Assignment

**Request Process:**
1. User or supervisor submits request
2. Department approves business necessity
3. Information owner approves data access
4. IT implements permissions
5. Documentation in access management system

**Approval Matrix:**

| Access Type | Approver | Documentation |
|-------------|----------|---------------|
| Standard Access | Supervisor | Email |
| Elevated Rights | Supervisor + IT Manager | Ticket System |
| Admin Rights | IT Manager + CISO | Form + Approval |
| Production Access | Department + IT Manager | Change Request |

### 3. Access Management

**Regular Review:**
- Quarterly recertification by supervisors
- Annual full review of all permissions
- Automatic detection of unused accounts
- Removal of no longer needed rights

**Changes:**
- Upon role change: Adjustment of permissions
- Upon departure: Immediate revocation of all access
- Upon security incidents: Temporary suspension possible

### 4. Access Revocation

**Planned Revocation:**
- Upon departure: Deactivation on last working day
- Upon project end: Revocation after project completion
- Upon role change: Adjustment of permissions

**Unplanned Revocation:**
- Upon security incidents: Immediate suspension
- Upon suspected misuse: Temporary suspension
- Upon compliance violations: Immediate suspension

## Authentication

### Password Requirements

**Complexity:**
- Minimum length: [TODO] characters
- Uppercase, lowercase, numbers, special characters
- No dictionary words
- No personal information

**Management:**
- Change every [TODO] days
- No reuse of last [TODO] passwords
- Automatic lockout after [TODO] failed attempts
- Password manager recommended

### Multi-Factor Authentication (MFA)

MFA is required for:
- Administrative access
- Remote access (VPN, Remote Desktop)
- Access to confidential systems
- Privileged accounts

**Supported Factors:**
- Something you know (password)
- Something you have (token, smartphone)
- Something you are (biometrics)

### Single Sign-On (SSO)

[TODO] uses SSO for:
- Central authentication
- Reduction of passwords
- Simplified access management
- Improved security

## Authorization

### Role-Based Access Control (RBAC)

**Standard Roles:**
- User: Basic access to standard systems
- Power User: Extended functions
- Administrator: System administration
- Security Admin: Security management

**Department Roles:**
- Defined by departments
- Based on business processes
- Regularly reviewed and updated

### Attribute-Based Access Control (ABAC)

Access based on:
- User attributes (department, location)
- Resource attributes (classification, type)
- Environmental attributes (time, location, device)
- Action attributes (read, write, delete)

## Privileged Access

### Privileged Access Management (PAM)

**Requirements:**
- Separate privileged accounts
- Just-in-time access
- Session recording
- Automatic password rotation

**Monitoring:**
- Real-time monitoring of privileged sessions
- Alerting on suspicious activities
- Regular auditing
- Compliance reporting

### Administrative Accounts

**Management:**
- Separate from standard accounts
- Elevated authentication requirements
- Time-limited activation
- Comprehensive logging

**Usage:**
- Only for administrative tasks
- No use for email or internet
- No use on standard workstations
- Documentation of all uses

## Remote Access

### VPN Access

**Requirements:**
- MFA mandatory
- Encrypted connection
- Endpoint compliance check
- Logging of all connections

**Permissions:**
- Request and approval required
- Time-limited
- Regular recertification
- Automatic disconnection upon inactivity

### Remote Desktop

**Security Measures:**
- Access only via VPN
- MFA required
- Session timeout
- No local data storage

## Access Control for Systems

### Servers and Infrastructure

- Access only for authorized IT personnel
- Logging of all access
- Regular review of permissions
- Automated compliance checks

### Applications

- Role-based permissions
- Integration with central authentication
- Regular access reviews
- Segregation of duties

### Databases

- Minimum permissions
- Encrypted connections
- Audit logging enabled
- Regular access reviews

### Cloud Services

- Identity federation
- Conditional access policies
- MFA mandatory
- Regular review of permissions

## Monitoring and Logging

### Logging

The following events are logged:
- Successful and failed logins
- Permission changes
- Access to sensitive data
- Administrative actions
- Privileged access

### Monitoring

- Real-time monitoring of critical systems
- Automatic alerting on anomalies
- Regular log analyses
- Security Information and Event Management (SIEM)

### Audit

- Quarterly sampling audits
- Annual full review
- Compliance verification
- Identification of improvement potential

## Exceptions

### Exception Approvals

Exceptions to this policy:
- Must be requested in writing
- Require approval by CISO
- Are time-limited
- Are documented and monitored
- Are regularly reviewed

### Emergency Access

In emergencies:
- Break-glass accounts available
- Usage is immediately escalated
- Comprehensive logging
- Subsequent review mandatory

## TISAX-Specific Requirements

### VDA ISA Controls

This document addresses:
- **3.1**: Access control policy
- **3.2**: User access management
- **3.3**: User responsibilities
- **3.4**: System and application access control

### Assessment Evidence

For TISAX assessments:
- Access control policy
- Process documentation
- Approval evidence
- Audit reports
- Training evidence

## Responsibilities

- **CISO**: Overall responsibility for access control
- **IT Manager**: Implementation and operation
- **Identity & Access Management Team**: Daily management
- **Supervisors**: Approval and recertification
- **Information Owner**: Approval of data access
- **Users**: Compliance with policy

## Training

All users are trained on:
- Access control fundamentals
- Password security
- MFA usage
- Responsibilities
- Reporting security incidents

## Metrics

[TODO] measures:
- Number of active user accounts
- Percentage of MFA-enabled accounts (Target: 100%)
- Average time to grant access
- Number of overdue access reviews
- Number of privileged access
- Number of access violations




