# Appendix: Asset Inventory (Template)

**Document-ID:** [FRAMEWORK]-0710
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template provides an asset inventory structure. In practice, this should be maintained in a CMDB.
Reference: BSI IT-Grundschutz-Kompendium: OPS.1.1.1 General IT Operations
-->

## 1. Purpose and Objectives

The asset inventory of **{{ meta-organisation.name }}** documents all IT assets within the ISMS scope.

**Responsible:** {{ meta-organisation-roles.role_CIO }}

## 2. Maintenance Note

**Recommendation:** This inventory should be maintained in a CMDB (Configuration Management Database) or Asset Management Tool. This document serves as a template/export format.

**CMDB System:** [TODO: e.g., ServiceNow, Device42, NetBox]  
**Storage Location:** [[ netbox.url ]] or [TODO]

## 3. Asset Categories

### 3.1 Hardware Assets
- Servers (physical, virtual)
- Network Devices (routers, switches, firewalls)
- Storage Systems
- Endpoints (laptops, desktops, mobile devices)
- IoT Devices

### 3.2 Software Assets
- Operating Systems
- Applications (commercial, open source, custom development)
- Databases
- Middleware

### 3.3 Data Assets
- Databases
- File Servers/Shares
- Cloud Storage
- Backup Media

### 3.4 Services
- IT Services (internal, external)
- Cloud Services (SaaS, PaaS, IaaS)

## 4. Asset Register

| Asset ID | Name | Type | Category | Owner | Location/Region | Protection Need (C/I/A) | Lifecycle Status | Manufacturer | Model | Serial Number | Acquisition Date | EOL Date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [[ netbox.device.id ]] | [[ netbox.device.name ]] | Server | Hardware | {{ meta-organisation-roles.role_CIO }} | [[ netbox.site.name ]] | [TODO] | Production | [[ netbox.device.manufacturer ]] | [[ netbox.device.model ]] | [[ netbox.device.serial ]] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Protection Need Categories:**
- **Normal:** Standard protection need
- **High:** Elevated protection need
- **Very High:** Critical protection need

**Lifecycle Status:**
- **Planning:** In procurement
- **Development:** In development/configuration
- **Production:** In production operation
- **Maintenance:** In maintenance/support
- **Decommissioned:** Shut down
- **Disposal:** Scheduled for disposal

## 5. NetBox Integration

**NetBox Instance:** [[ netbox.url ]]

**Available Data from NetBox:**
- Devices: [[ netbox.device.name ]], [[ netbox.device.type ]], [[ netbox.device.role ]]
- Sites: [[ netbox.site.name ]], [[ netbox.site.region ]]
- IP Addresses: [[ netbox.ipaddress.address ]]
- VLANs: [[ netbox.vlan.name ]], [[ netbox.vlan.id ]]
- Racks: [[ netbox.rack.name ]], [[ netbox.rack.location ]]

**Synchronization:** [TODO: Automatic/Manual, Frequency]

## 6. Asset Lifecycle Management

### 6.1 Procurement
- Asset is recorded (Status: Planning)
- Protection need is determined
- Owner is assigned

### 6.2 Commissioning
- Asset is configured and hardened
- Asset is transferred to production (Status: Production)
- Monitoring is activated

### 6.3 Operation
- Regular updates and patches
- Monitoring and maintenance
- Changes are documented (Change Management)

### 6.4 Decommissioning
- Asset is shut down (Status: Decommissioned)
- Data is securely deleted
- Asset is disposed of (Status: Disposal)

**Reference:** Document 0250 (Asset Lifecycle)

## 7. Responsibilities (RACI)

| Activity | IT Management | Asset Owner | CMDB Admin | CISO |
|---|---|---|---|---|
| Record Asset | A | R | I | I |
| Determine Protection Need | A | C | I | R |
| Update Asset | I | R | A | I |
| Asset Review (annual) | A | R | C | C |
| Asset Disposal | A | R | I | C |

**Legend:**
- **R** = Responsible (Execution responsibility)
- **A** = Accountable (Overall responsibility)
- **C** = Consulted
- **I** = Informed

## 8. Asset Tagging

**Tagging Schema:**
- **Environment:** Production, Staging, Development, Test
- **Criticality:** Critical, High, Medium, Low
- **Owner:** Area manager
- **Compliance:** ISO27001, BSI, GDPR, etc.
- **Backup:** Yes/No
- **DR:** Yes/No

**Example (Cloud Resources):**
```
Environment: Production
Criticality: High
Owner: {{ meta-organisation-roles.role_CIO }}
Compliance: ISO27001, BSI
Backup: Yes
DR: Yes
```

## 9. Reporting

**Regular Reports:**
- **Monthly:** Asset Inventory Overview
- **Quarterly:** EOL Report (Assets approaching End-of-Life)
- **Annually:** Complete Asset Review

**Responsible:** {{ meta-organisation-roles.role_CIO }}

## 10. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| IT Management | {{ meta-organisation-roles.role_CIO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| CISO | {{ meta-organisation-roles.role_CISO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**References:**
- BSI IT-Grundschutz-Kompendium: OPS.1.1.1 General IT Operations
- BSI IT-Grundschutz-Kompendium: OPS.1.2.2 Archiving
- Document 0050: Structure Analysis
- Document 0060: Protection Needs Assessment
- Document 0250: Asset Lifecycle

<!-- End of template -->