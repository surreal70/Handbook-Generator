# Tooling and Access Methods

## Overview

This document describes the tools and systems used, access methods and URLs, as well as authentication methods for the IT service. The goal is to provide a central overview of all relevant tools and their access.

**Document Owner:** IT Operations Manager  
**Approved by:** CIO  
**Version:** 1.0.0  
**Organization:** AdminSend GmbH

---

## Tool Categories

### Tool Categories Overview

| Category | Number of Tools | Main Responsible | Criticality |
|---|---:|---|---|
| Monitoring & Observability | [TODO] | Andreas Huemmer | High |
| Infrastructure Management | [TODO] | Andreas Huemmer | High |
| Security & Compliance | [TODO] | Thomas Weber | High |
| Development & Deployment | [TODO] | Andreas Huemmer | Medium |
| Collaboration & Communication | [TODO] | Peter Fischer | Medium |
| Documentation & Knowledge | [TODO] | Andreas Huemmer | Medium |
| Backup & Recovery | [TODO] | Andreas Huemmer | High |

---

## Monitoring and Observability

### System Monitoring

#### [TODO: Monitoring Tool Name]
- **Purpose:** System and infrastructure monitoring
- **URL:** [TODO: https://monitoring.example.com]
- **Access:** VPN + SSO
- **Authentication:** AdminSend GmbH SSO
- **Responsible:** Andreas Huemmer
- **Support:** [TODO: Support Contact]
- **Documentation:** [TODO: Documentation URL]

**Main Functions:**
- Server monitoring (CPU, RAM, Disk, Network)
- Service monitoring (Uptime, Response Time)
- Alerting and notifications
- Dashboards and visualization

---

## Infrastructure Management

### Configuration Management Database (CMDB)

#### NetBox
- **Purpose:** CMDB and IPAM
- **URL:** {{ netbox.url }}
- **Access:** VPN + Username/Password
- **Authentication:** Local accounts or LDAP
- **Responsible:** Andreas Huemmer
- **API:** {{ netbox.api_url }}
- **Documentation:** https://docs.netbox.dev/

**Main Functions:**
- Device inventory
- IP address management (IPAM)
- Rack management
- Cable documentation
- Virtualization tracking

---

## Security and Compliance

### Security Information and Event Management (SIEM)

#### [TODO: SIEM Tool Name]
- **Purpose:** Security event monitoring and analysis
- **URL:** [TODO: https://siem.example.com]
- **Access:** VPN + SSO
- **Authentication:** AdminSend GmbH SSO
- **Responsible:** Thomas Weber
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Security event aggregation
- Threat detection
- Incident response
- Compliance reporting

---

## Access Methods

### VPN Access

#### Corporate VPN
- **Purpose:** Secure remote access
- **URL:** [TODO: https://vpn.example.com]
- **Client:** [TODO: VPN Client Name]
- **Authentication:** AdminSend GmbH AD + MFA
- **Responsible:** Thomas Weber
- **Support:** julia.becker@adminsend.de

**Connection Instructions:**
1. Install VPN client
2. Import/configure profile
3. Connect with AD credentials + MFA
4. Validate connection

---

### SSH Access

#### SSH Bastion Host
- **Purpose:** Secure SSH access to servers
- **Hostname:** [TODO: bastion.example.com]
- **Port:** 22
- **Authentication:** SSH Keys + MFA
- **Responsible:** Andreas Huemmer

**Connection Instructions:**
```bash
# Generate SSH key (if not exists)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add public key to bastion host
# (by admin)

# Connect to bastion host
ssh -i ~/.ssh/id_ed25519 username@bastion.example.com

# From bastion to target server
ssh username@target-server
```

---

## Authentication Methods

### Single Sign-On (SSO)

#### AdminSend GmbH SSO
- **Provider:** [TODO: SSO Provider]
- **Protocol:** SAML 2.0 / OAuth 2.0 / OpenID Connect
- **MFA:** Required for all external access
- **Session Timeout:** 8 hours
- **Responsible:** Thomas Weber

**Supported Applications:**
- [TODO: List of SSO-integrated applications]

---

### API Authentication

#### API Tokens
- **Usage:** Programmatic access to APIs
- **Generation:** Via respective tool interface
- **Rotation:** Every 90 days
- **Storage:** Secrets management system
- **Responsible:** Andreas Huemmer

**Best Practices:**
- Never commit tokens in code
- Minimal permissions (Least Privilege)
- Regular rotation
- Monitor token usage

---

## Emergency Access

### Break-Glass Accounts

#### Emergency Admin Account
- **Purpose:** Emergency access in case of SSO failure
- **Storage:** Sealed envelope in safe
- **Access:** Only by Anna Schmidt or Thomas Weber
- **Logging:** Every use is logged and reviewed
- **Password Rotation:** Quarterly

**Usage Process:**
1. Identify and document emergency
2. Obtain approval from CIO/CISO
3. Open envelope and document
4. Perform access
5. Log all actions
6. Change password and seal new envelope
7. Create incident report

---

## Processes and Responsibilities

### RACI Matrix

| Activity | CIO | CISO | Ops Manager | Ops Team |
|---|---|---|---|---|
| Tool Selection | A | C | R | C |
| Tool Implementation | C | C | A | R |
| Access Management | C | A | R | I |
| Tool Maintenance | I | C | A | R |
| Tool Review | A | C | R | C |
| Emergency Access | A | A | C | I |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

**Last Update:** {{ meta.date }}  
**Next Review:** [TODO: Date]  
**Contact:** andreas.huemmer@adminsend.de
