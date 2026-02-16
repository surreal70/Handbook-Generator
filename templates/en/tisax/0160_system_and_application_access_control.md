---
Document-ID: tisax-0160
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# System and Application Access Control

## Purpose

This document defines requirements for access control to systems and applications according to TISAX requirements.

## Scope

This document applies to all IT systems and applications of {{ source.organization_name }}.

## Access Control Mechanisms

### Authentication
- Unique user identification
- Secure authentication methods
- Multi-factor authentication for critical systems
- Encrypted transmission of credentials

### Authorization
- Least Privilege
- Need-to-Know
- Segregation of Duties
- Role-Based Access Control (RBAC)

## System Access Control

### Operating Systems
**Servers:**
- Access only for authorized personnel
- Privileged accounts separated
- Logging of all access
- Regular patch management

**Workstations:**
- Standard users without admin rights
- Encrypted hard drives
- Endpoint protection
- Automatic updates

### Network Devices
- Separate admin accounts
- Encrypted management connections
- Logging of all configuration changes
- Regular security audits

### Databases
- Minimum permissions
- Encrypted connections
- Audit logging enabled
- Regular access reviews

## Application Access Control

### Business Applications
**Authentication:**
- Integration with central authentication (SSO)
- MFA for remote access
- Session management
- Automatic logout upon inactivity

**Authorization:**
- Role-based permissions
- Function-based access control
- Data-based access control
- Regular recertification

### Web Applications
- HTTPS mandatory
- Secure session management
- Input validation
- Output encoding
- CSRF protection
- XSS prevention

### Cloud Applications
- Identity federation
- Conditional access policies
- MFA mandatory
- Regular review of permissions

## Secure Login Procedures

### Password Management
- See Access Control Policy
- Secure storage (hashing with salt)
- Encrypted transmission
- Password reset process

### Session Management
- Secure session IDs
- Session timeout upon inactivity
- Automatic logout
- No session fixation

## Privileged Access Control

### Administrative Access
- Separate privileged accounts
- Just-in-time access
- Session recording
- Four-eyes principle for critical actions

### Privileged Access Management (PAM)
- Central management of privileged accounts
- Automatic password rotation
- Session monitoring
- Compliance reporting

## Access Control for Development

### Development Environments
- Separated from production environments
- No production data in development
- Access control based on roles
- Version control for code

### Test Environments
- Anonymized test data
- Access control
- Logging
- Regular cleanup

### Production Environments
- Strict access control
- Change management required
- Comprehensive logging
- Segregation of duties

## Remote Access

### VPN
- MFA mandatory
- Encrypted connection
- Endpoint compliance check
- Logging of all connections

### Remote Desktop
- Access only via VPN
- MFA required
- Session timeout
- No local data storage

## Monitoring and Logging

### Logging
- Successful and failed logins
- Permission changes
- Access to sensitive data
- Administrative actions
- Privileged access

### Monitoring
- Real-time monitoring of critical systems
- Automatic alerting on anomalies
- Regular log analyses
- SIEM integration

## TISAX-Specific Requirements

### VDA ISA Controls
- **3.4.1**: Information access restriction
- **3.4.2**: Secure login procedures
- **3.4.3**: Password management system
- **3.4.4**: Use of utility programs

### Assessment Evidence
- Access control configurations
- Audit logs
- Access review reports
- Process documentation

## Metrics

{{ source.organization_name }} measures:
- Number of failed login attempts
- Number of privileged access
- Average session duration
- Number of access violations

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
