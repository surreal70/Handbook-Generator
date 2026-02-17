# Tooling and Access Methods

**Document-ID:** [FRAMEWORK]-0250
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

## Overview

This document describes the tools and systems used, access methods and URLs, as well as authentication methods for the IT service. The goal is to provide a central overview of all relevant tools and their access.

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organization:** {{ meta-organisation.name }}

## Tool Categories

### Tool Categories Overview

| Category | Number of Tools | Main Responsible | Criticality |
|---|---:|---|---|
| Monitoring & Observability | [TODO] | {{ meta-organisation-roles.role_it_operations_manager.name }} | High |
| Infrastructure Management | [TODO] | {{ meta-organisation-roles.role_it_operations_manager.name }} | High |
| Security & Compliance | [TODO] | {{ meta-organisation-roles.role_ciso.name }} | High |
| Development & Deployment | [TODO] | {{ meta-organisation-roles.role_it_operations_manager.name }} | Medium |
| Collaboration & Communication | [TODO] | {{ meta-organisation-roles.role_coo.name }} | Medium |
| Documentation & Knowledge | [TODO] | {{ meta-organisation-roles.role_it_operations_manager.name }} | Medium |
| Backup & Recovery | [TODO] | {{ meta-organisation-roles.role_it_operations_manager.name }} | High |

## Monitoring and Observability

### System Monitoring

#### [TODO: Monitoring Tool Name]
- **Purpose:** System and infrastructure monitoring
- **URL:** [TODO: https://monitoring.example.com]
- **Access:** VPN + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]
- **Documentation:** [TODO: Documentation URL]

**Main Functions:**
- Server monitoring (CPU, RAM, Disk, Network)
- Service monitoring (Uptime, Response Time)
- Alerting and notifications
- Dashboards and visualization

**Access Permissions:**
- **Admin:** IT Operations Manager, Senior Engineers
- **Read/Write:** Operations Team
- **Read-Only:** Management, Stakeholder

### Application Performance Monitoring (APM)

#### [TODO: APM Tool Name]
- **Purpose:** Application performance monitoring
- **URL:** [TODO: https://apm.example.com]
- **Access:** VPN + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Transaction tracing
- Error tracking
- Performance metrics
- User experience monitoring

### Log Management

#### [TODO: Log Management Tool Name]
- **Purpose:** Central log aggregation and analysis
- **URL:** [TODO: https://logs.example.com]
- **Access:** VPN + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Log aggregation from all systems
- Log search and filtering
- Log analysis and visualization
- Alerting on log patterns

## Infrastructure Management

### Configuration Management Database (CMDB)

#### NetBox
- **Purpose:** CMDB and IPAM
- **URL:** {{ netbox.url }}
- **Access:** VPN + Username/Password
- **Authentication:** Local accounts or LDAP
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **API:** {{ netbox.api_url }}
- **Documentation:** https://docs.netbox.dev/

**Main Functions:**
- Device inventory
- IP address management (IPAM)
- Rack management
- Cable documentation
- Virtualization tracking

**Access Permissions:**
- **Admin:** IT Operations Manager
- **Read/Write:** Operations Team, Network Team
- **Read-Only:** Management, Auditors

### Virtualization

#### [TODO: Hypervisor Management]
- **Purpose:** Virtualization management
- **URL:** [TODO: https://vcenter.example.com]
- **Access:** VPN + Username/Password
- **Authentication:** Local accounts or AD
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- VM management
- Resource allocation
- Snapshot management
- Migration and HA

### Container Orchestration

#### [TODO: Container Platform]
- **Purpose:** Container orchestration
- **URL:** [TODO: https://k8s.example.com]
- **Access:** VPN + kubectl + Token
- **Authentication:** Service accounts, RBAC
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Container deployment
- Service discovery
- Load balancing
- Auto-scaling

### Cloud Management

#### [TODO: Cloud Provider Console]
- **Purpose:** Cloud resource management
- **URL:** [TODO: https://console.cloud-provider.com]
- **Access:** Internet + MFA
- **Authentication:** Cloud provider accounts + MFA
- **Responsible:** {{ meta-organisation-roles.role_cio.name }}
- **Support:** Cloud provider support

**Main Functions:**
- Compute resources
- Storage management
- Networking
- IAM and security

## Security and Compliance

### Security Information and Event Management (SIEM)

#### [TODO: SIEM Tool Name]
- **Purpose:** Security event monitoring and analysis
- **URL:** [TODO: https://siem.example.com]
- **Access:** VPN + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_ciso.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Security event aggregation
- Threat detection
- Incident response
- Compliance reporting

### Vulnerability Management

#### [TODO: Vulnerability Scanner]
- **Purpose:** Vulnerability scanning
- **URL:** [TODO: https://vuln.example.com]
- **Access:** VPN + Username/Password
- **Authentication:** Local accounts
- **Responsible:** {{ meta-organisation-roles.role_ciso.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Vulnerability scanning
- Patch management
- Compliance checks
- Reporting

### Identity and Access Management (IAM)

#### Active Directory / LDAP
- **Purpose:** Central user management
- **URL:** [TODO: ldap://ad.example.com]
- **Access:** Internal + VPN
- **Authentication:** Admin accounts
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- User management
- Group management
- Authentication
- Authorization

### Multi-Factor Authentication (MFA)

#### [TODO: MFA Solution]
- **Purpose:** Two-factor authentication
- **URL:** [TODO: https://mfa.example.com]
- **Access:** Internet
- **Authentication:** Username + MFA token
- **Responsible:** {{ meta-organisation-roles.role_ciso.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- MFA enrollment
- Token management
- Push notifications
- Backup codes

## Development and Deployment

### Version Control

#### [TODO: Git Platform]
- **Purpose:** Source code management
- **URL:** [TODO: https://git.example.com]
- **Access:** VPN + SSO
- **Authentication:** {{ meta-organisation.name }} SSO + SSH keys
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Git repositories
- Code review
- CI/CD integration
- Issue tracking

### CI/CD Pipeline

#### [TODO: CI/CD Tool]
- **Purpose:** Continuous integration/deployment
- **URL:** [TODO: https://ci.example.com]
- **Access:** VPN + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Build automation
- Test automation
- Deployment automation
- Pipeline management

### Artifact Repository

#### [TODO: Artifact Repository]
- **Purpose:** Binary artifact storage
- **URL:** [TODO: https://artifacts.example.com]
- **Access:** VPN + Token
- **Authentication:** API tokens
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Package management
- Container registry
- Dependency management
- Version management

## Collaboration and Communication

### Ticketing System

#### [TODO: Ticketing Tool]
- **Purpose:** Incident and request management
- **URL:** [TODO: https://tickets.example.com]
- **Access:** Internet + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Incident management
- Request management
- Change management
- SLA tracking

### Team Communication

#### [TODO: Chat Platform]
- **Purpose:** Team communication and collaboration
- **URL:** [TODO: https://chat.example.com]
- **Access:** Internet + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_coo.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Team chat
- Channels and direct messages
- File sharing
- Integration with other tools

### Video Conferencing

#### [TODO: Video Tool]
- **Purpose:** Video conferences
- **URL:** [TODO: https://meet.example.com]
- **Access:** Internet
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_coo.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Video calls
- Screen sharing
- Recording
- Chat

## Documentation and Knowledge Management

### Wiki / Knowledge Base

#### [TODO: Wiki Platform]
- **Purpose:** Documentation and knowledge base
- **URL:** [TODO: https://wiki.example.com]
- **Access:** VPN + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Documentation management
- Knowledge articles
- Search and navigation
- Versioning

### Diagram Tool

#### [TODO: Diagramming Tool]
- **Purpose:** Architecture and network diagrams
- **URL:** [TODO: https://diagrams.example.com]
- **Access:** Internet + SSO
- **Authentication:** {{ meta-organisation.name }} SSO
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Diagram creation
- Collaboration
- Export to various formats
- Versioning

## Backup and Recovery

### Backup System

#### [TODO: Backup Solution]
- **Purpose:** Backup and recovery
- **URL:** [TODO: https://backup.example.com]
- **Access:** VPN + Username/Password
- **Authentication:** Local accounts
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Support:** [TODO: Support Contact]

**Main Functions:**
- Backup scheduling
- Backup monitoring
- Restore functions
- Retention management

## Access Methods

### VPN Access

#### Corporate VPN
- **Purpose:** Secure remote access
- **URL:** [TODO: https://vpn.example.com]
- **Client:** [TODO: VPN Client Name]
- **Authentication:** {{ meta-organisation.name }} AD + MFA
- **Responsible:** {{ meta-organisation-roles.role_ciso.name }}
- **Support:** {{ meta-organisation-roles.role_service_desk_lead.email }}

**Connection Instructions:**
1. Install VPN client
2. Import/configure profile
3. Connect with AD credentials + MFA
4. Validate connection

**Troubleshooting:**
- **Problem:** Connection fails
  - **Solution:** Check credentials, check MFA token, check network
- **Problem:** Slow connection
  - **Solution:** Choose different VPN gateway, check split tunneling

### SSH Access

#### SSH Bastion Host
- **Purpose:** Secure SSH access to servers
- **Hostname:** [TODO: bastion.example.com]
- **Port:** 22
- **Authentication:** SSH Keys + MFA
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}

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

### Remote Desktop

#### RDP Gateway
- **Purpose:** Remote desktop access to Windows servers
- **URL:** [TODO: https://rdp.example.com]
- **Authentication:** {{ meta-organisation.name }} AD + MFA
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}

**Connection Instructions:**
1. Open RDP client
2. Enter gateway address
3. Authenticate with AD credentials + MFA
4. Select target server

## Authentication Methods

### Single Sign-On (SSO)

#### {{ meta-organisation.name }} SSO
- **Provider:** [TODO: SSO Provider]
- **Protocol:** SAML 2.0 / OAuth 2.0 / OpenID Connect
- **MFA:** Required for all external access
- **Session Timeout:** 8 hours
- **Responsible:** {{ meta-organisation-roles.role_ciso.name }}

**Supported Applications:**
- [TODO: List of SSO-integrated applications]

### API Authentication

#### API Tokens
- **Usage:** Programmatic access to APIs
- **Generation:** Via respective tool interface
- **Rotation:** Every 90 days
- **Storage:** Secrets management system
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}

**Best Practices:**
- Never commit tokens in code
- Minimal permissions (Least Privilege)
- Regular rotation
- Monitor token usage

### SSH Keys

#### SSH Key Management
- **Key Type:** ED25519 (preferred) or RSA 4096
- **Passphrase:** Required
- **Rotation:** Annually
- **Storage:** Local, encrypted
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}

**Key Generation:**
```bash
# ED25519 (recommended)
ssh-keygen -t ed25519 -C "your_email@example.com"

# RSA 4096 (alternative)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

## Tool Access Matrix

### Access Permissions by Role

| Tool | Ops Manager | Ops Team | Security Team | Management | Auditor |
|---|---|---|---|---|---|
| Monitoring | Admin | Read/Write | Read | Read | Read |
| CMDB (NetBox) | Admin | Read/Write | Read | Read | Read |
| SIEM | Read | Read | Admin | Read | Read |
| Backup System | Admin | Read/Write | Read | - | Read |
| Cloud Console | Admin | Read/Write | Read | Read | - |
| Ticketing | Admin | Read/Write | Read/Write | Read | Read |
| Wiki | Admin | Read/Write | Read/Write | Read | Read |
| VPN | Yes | Yes | Yes | Yes | Yes |
| SSH Bastion | Yes | Yes | Yes | - | - |

## Emergency Access

### Break-Glass Accounts

#### Emergency Admin Account
- **Purpose:** Emergency access in case of SSO failure
- **Storage:** Sealed envelope in safe
- **Access:** Only by {{ meta-organisation-roles.role_cio.name }} or {{ meta-organisation-roles.role_ciso.name }}
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

## Tool Lifecycle Management

### Tool Evaluation

#### Evaluating New Tools
1. **Requirements Analysis:** Identify needs
2. **Market Analysis:** Research available solutions
3. **Proof of Concept:** Test top 3 solutions
4. **Evaluation:** Functionality, costs, integration
5. **Decision:** Select tool
6. **Implementation:** Plan and execute rollout

#### Tool Review
- **Frequency:** Annually
- **Criteria:**
  - Usage and acceptance
  - Cost-benefit ratio
  - Technical currency
  - Support quality
  - Integration with other tools

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

## Compliance and Standards

### Relevant Standards
- **ISO 27001:** A.9 - Access Control
- **ISO 27001:** A.12 - Operations Security
- **COBIT 2019:** DSS05 - Managed Security Services

### Audit Requirements
- Tool inventory
- Access logs
- Authentication logs
- Emergency access documentation

## Appendix

### Glossary

| Term | Definition |
|---|---|
| SSO | Single Sign-On - Single authentication for multiple systems |
| MFA | Multi-Factor Authentication - Multi-factor authentication |
| VPN | Virtual Private Network - Virtual private network |
| API | Application Programming Interface - Programming interface |
| CMDB | Configuration Management Database - Configuration database |
| SIEM | Security Information and Event Management |

### References
- ISO/IEC 27001:2013
- COBIT 2019 Framework
- NIST Cybersecurity Framework

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_it_operations_manager.email }}

