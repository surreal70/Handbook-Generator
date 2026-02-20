# Access and Permission Management

**Document-ID:** [FRAMEWORK]-0100
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

## Overview

This document describes access and permission management for the IT service. It defines access control models, permission concepts, and role-based access control (RBAC).

**Service:** {{ meta-handbook.service_name }}  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**Security Officer:** [TODO]  
**Version:** 0

## Access Management Strategy

### Objectives

- **Least Privilege:** Minimum necessary permissions
- **Separation of Duties:** Task separation for risk minimization
- **Need-to-Know:** Access only to required information
- **Accountability:** Traceability of all access
- **Compliance:** Adherence to regulatory requirements

### Core Principles

1. **Default Deny:** No access by default, explicit approval required
2. **Time-Limited Access:** Time-limited permissions where possible
3. **Regular Review:** Regular review of permissions
4. **Audit Trail:** Complete logging of all access
5. **Multi-Factor Authentication:** MFA for privileged access

## Access Control Model

### Authentication

#### Authentication Methods

| Method | Usage | Security Level |
|---|---|---|
| **Username/Password** | Standard access | Basic |
| **Multi-Factor Authentication (MFA)** | Privileged access | High |
| **Certificate-Based** | System-to-system | Very High |
| **SSO (Single Sign-On)** | Enterprise applications | Medium-High |
| **API Keys** | Programmatic access | Medium |
| **Biometric** | High-security areas | Very High |

#### Authentication Infrastructure

**Identity Provider:**
- **System:** [TODO: e.g., Active Directory, Azure AD, Okta]
- **URL:** [TODO: SSO URL]
- **Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

**MFA System:**
- **System:** [TODO: e.g., Duo, Microsoft Authenticator]
- **Required for:** Administrators, privileged accounts
- **Responsible:** [TODO]

### Authorization

#### Authorization Models

**Role-Based Access Control (RBAC):**
- Permissions assigned to roles
- Users receive roles
- Simplifies permission management

**Attribute-Based Access Control (ABAC):**
- Permissions based on attributes
- More flexible than RBAC
- More complex implementation

**Current Model:** [TODO: Select RBAC/ABAC/Hybrid]

## Role-Based Access Control (RBAC)

### Role Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                    Administrator                             │
│  (Full access to all systems and data)                      │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────────────────────────┐
│  Power User     │    │     Operator                         │
│  (Extended      │    │  (Operations access)                 │
│   permissions)  │    └────────┬────────────────────────────┘
└─────────────────┘             │
                                │
                    ┌───────────┴───────────┐
                    │                       │
           ┌────────▼────────┐    ┌────────▼────────┐
           │   Standard User │    │   Read-Only     │
           │  (Basic access) │    │  (Read only)    │
           └─────────────────┘    └─────────────────┘
```

### Role Definitions

#### Administrator
**Description:** Full access to all systems and functions  
**Permissions:**
- Full access to all systems
- User management
- Configuration changes
- System administration
- Backup/restore

**Assigned to:**
- {{ meta-organisation-roles.role_IT_Operations_Manager }}
- [TODO: Additional administrators]

**MFA:** Required

#### Power User
**Description:** Extended permissions for special tasks  
**Permissions:**
- Read and write in assigned areas
- Use advanced functions
- Create reports
- Configuration in own area

**Assigned to:**
- [TODO: List power users]

**MFA:** Recommended

#### Operator
**Description:** Operations access for daily tasks  
**Permissions:**
- Monitoring access
- Incident processing
- Standard operations
- Log access (read-only)

**Assigned to:**
- {{ meta-organisation-roles.role_Service_Desk_Lead }}
- [TODO: Additional operators]

**MFA:** Optional

#### Standard User
**Description:** Basic access for normal users  
**Permissions:**
- Access to own data
- Use standard functions
- Create tickets
- Manage own profile

**Assigned to:**
- All employees

**MFA:** Optional

#### Read-Only
**Description:** Read-only access for reporting and auditing  
**Permissions:**
- Read access to data
- View reports
- View dashboards
- No changes possible

**Assigned to:**
- Auditors
- Management
- [TODO: Additional read-only users]

**MFA:** Optional

## Permission Matrix

### System Permissions

| System/Resource | Administrator | Power User | Operator | Standard User | Read-Only |
|---|---|---|---|---|---|
| **Server Administration** | Full access | - | - | - | Read |
| **Network Configuration** | Full access | - | - | - | Read |
| **Monitoring System** | Full access | Read/Write | Read | - | Read |
| **Ticketing System** | Full access | Read/Write | Read/Write | Create tickets | Read |
| **CMDB** | Full access | Read/Write | Read | - | Read |
| **Backup System** | Full access | - | Read | - | Read |
| **Log Management** | Full access | Read | Read | - | Read |
| **Documentation** | Full access | Read/Write | Read | Read | Read |

### Data Permissions

| Data Classification | Administrator | Power User | Operator | Standard User | Read-Only |
|---|---|---|---|---|---|
| **Public** | Full access | Read/Write | Read | Read | Read |
| **Internal** | Full access | Read/Write | Read | Read | Read |
| **Confidential** | Full access | As needed | - | - | As needed |
| **Restricted** | As needed | - | - | - | - |

## Access Request Process

### Access Request

```
┌─────────────────┐
│ 1. Submit       │
│    Request      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Manager      │
│    Approval     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Security     │
│    Review       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. Provisioning │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. Confirmation │
└─────────────────┘
```

### Request Process

#### 1. Submit Request
**Who:** User or manager  
**How:** Ticket in service desk system  
**Information:**
- Username
- Requested role/permission
- Business justification
- Time period (if temporary)
- Manager approval

#### 2. Manager Approval
**Who:** Direct supervisor  
**Review:**
- Business necessity
- Least privilege principle
- Separation of duties

**Decision:** Approve / Reject / Request clarification

#### 3. Security Review
**Who:** [TODO] or security team  
**Review:**
- Compliance requirements
- Risk assessment
- Conflict check (separation of duties)

**Decision:** Approve / Reject / Modify

#### 4. Provisioning
**Who:** {{ meta-organisation-roles.role_IT_Operations_Manager }} or IT operations  
**Activities:**
- Create/modify account
- Assign permissions
- Set up MFA (if required)
- Documentation in CMDB

**SLA:** Within 1 business day

#### 5. Confirmation
**Who:** IT operations  
**Activities:**
- Inform user
- Provide access credentials
- Complete documentation
- Close ticket

## Privileged Access Management (PAM)

### Privileged Accounts

#### Definition
Privileged accounts have extended permissions and access to critical systems.

**Examples:**
- Root/administrator accounts
- Service accounts
- Database admin accounts
- Network admin accounts
- Backup admin accounts

### PAM Requirements

| Requirement | Description | Implementation |
|---|---|---|
| **Separate Accounts** | Privileged accounts separate from standard accounts | [TODO] |
| **MFA** | Multi-factor authentication required | [TODO] |
| **Session Recording** | Recording of privileged sessions | [TODO] |
| **Just-in-Time Access** | Temporary privilege assignment | [TODO] |
| **Password Vault** | Centralized password management | [TODO] |
| **Regular Rotation** | Regular password rotation | [TODO] |
| **Audit Logging** | Complete logging | [TODO] |

### PAM System

**System:** [TODO: e.g., CyberArk, BeyondTrust, Thycotic]  
**Responsible:** [TODO]  
**Access:** [TODO: PAM system URL]

## Service Accounts

### Service Account Management

**Definition:** Accounts for automated processes and system integrations

**Requirements:**
- Unique naming (e.g., `svc_backup`, `svc_monitoring`)
- Documentation in CMDB
- Minimal permissions
- No interactive logins
- Regular password rotation
- Usage monitoring

### Service Account Inventory

| Service Account | Usage | System | Permissions | Owner |
|---|---|---|---|---|
| `svc_backup` | Backup processes | Backup system | Read, backup | Backup admin |
| `svc_monitoring` | Monitoring | Monitoring system | Read | Monitoring team |
| `svc_integration` | System integration | Integration platform | API access | Integration team |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## Access Review Process

### Regular Reviews

#### Quarterly Reviews
**Frequency:** Every 3 months  
**Scope:** All user permissions  
**Responsible:** Manager + IT operations  
**Process:**
1. Generate review report
2. Managers review their employees' permissions
3. Remove no longer needed permissions
4. Document changes

#### Annual Reviews
**Frequency:** Annually  
**Scope:** Complete access review  
**Responsible:** [TODO]  
**Process:**
1. Comprehensive audit of all accounts
2. Review privileged accounts
3. Validate service accounts
4. Compliance check
5. Create audit report

### Automatic Reviews

**Triggers:**
- Employee change (department/role)
- Project end
- Inactive accounts (> 90 days)
- Expiration of temporary permissions

**Action:**
- Automatic notification to manager
- Deactivation after deadline
- Documentation

## Onboarding and Offboarding

### Onboarding Process

#### New Employee
**Trigger:** HR notification  
**Timeframe:** Before first day of work

**Activities:**
1. [ ] Create account
2. [ ] Assign basic permissions
3. [ ] Set up email account
4. [ ] Provide VPN access
5. [ ] Set up MFA
6. [ ] Provide access credentials
7. [ ] Documentation in CMDB
8. [ ] Send welcome email

**Responsible:** {{ meta-organisation-roles.role_Service_Desk_Lead }}

### Offboarding Process

#### Employee Departure
**Trigger:** HR notification  
**Timeframe:** On last day of work

**Activities:**
1. [ ] Deactivate account
2. [ ] Remove all permissions
3. [ ] Set up email forwarding (if required)
4. [ ] Block VPN access
5. [ ] Return hardware
6. [ ] Archive data
7. [ ] Update documentation
8. [ ] Inform manager

**Responsible:** {{ meta-organisation-roles.role_Service_Desk_Lead }}

#### Role Change
**Trigger:** HR notification or manager request  
**Timeframe:** On change date

**Activities:**
1. [ ] Remove old permissions
2. [ ] Assign new permissions
3. [ ] Conduct access review
4. [ ] Update documentation
5. [ ] Inform user

## Compliance and Auditing

### Compliance Requirements

| Standard | Requirement | Implementation |
|---|---|---|
| **GDPR** | Access control for personal data | RBAC, audit logging |
| **ISO 27001** | Access control policy | This document |
| **SOX** | Separation of duties | Role separation |
| **PCI DSS** | Restricted access to cardholder data | Permission matrix |

### Audit Logging

**Logged Events:**
- Login attempts (successful and failed)
- Permission changes
- Privileged actions
- Access to sensitive data
- Account creation/deletion
- Password changes

**Log Retention:** [TODO: e.g., 1 year]  
**Log System:** [TODO: e.g., Splunk, ELK]  
**Responsible:** [TODO]

### Audit Reports

**Monthly Reports:**
- New accounts
- Deleted accounts
- Permission changes
- Failed login attempts
- Privileged access

**Quarterly Reports:**
- Access review results
- Compliance status
- Risk assessment
- Improvement suggestions

## Emergency Access

### Break-Glass Accounts

**Definition:** Emergency accounts for critical situations

**Usage:**
- Only for critical outages
- When normal access paths unavailable
- After approval by [TODO]

**Requirements:**
- Physically secured passwords
- Complete logging
- Immediate notification to management
- Post-incident review

**Accounts:**
- `emergency_admin` - Full access to all systems
- `emergency_network` - Network emergency access

**Password Management:**
- Sealed envelopes in safe
- Access only by [TODO] or [TODO]

## Contacts

**Access Management Team:**
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} - {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **CISO:** [TODO] - {{ meta-organisation-roles.role_CISO_email }}
- **Service Desk Lead:** {{ meta-organisation-roles.role_Service_Desk_Lead }} - {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **CIO:** [TODO] - {{ meta-organisation-roles.role_CIO_email }}

**Emergency Contacts:**
- **Break-Glass Approval:** [TODO] - {{ meta-organisation-roles.role_CIO_phone }}
- **Security Incident:** [TODO] - {{ meta-organisation-roles.role_CISO_phone }}

**Document Owner:** [TODO]  
**Approved by:** [TODO]  
**Version:** 0  
**Organization:** AdminSend GmbH

