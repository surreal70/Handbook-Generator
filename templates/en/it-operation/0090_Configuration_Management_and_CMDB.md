# Configuration Management and CMDB

**Document-ID:** [FRAMEWORK]-0090
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

## Overview

This document describes configuration management and the Configuration Management Database (CMDB) for the IT service. It defines CI categories, attributes, relationships, and change processes for Configuration Items.

**Service:** {{ meta-handbook.service_name }}  
**Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}  
**CMDB System:** NetBox  
**Version:** {{ meta-handbook.revision }}

## Configuration Management Process

### Configuration Management Objectives

- **Transparency:** Complete overview of all IT assets and their relationships
- **Control:** Controlled changes to Configuration Items
- **Compliance:** Adherence to license and compliance requirements
- **Planning:** Solid foundation for capacity and change planning
- **Incident Support:** Faster incident resolution through CI information

### ITIL Configuration Management Activities

1. **Management and Planning:** Planning and control of configuration management
2. **Configuration Identification:** Identification and categorization of CIs
3. **Configuration Control:** Control of changes to CIs
4. **Status Accounting:** Recording and reporting of CI status
5. **Verification and Audit:** Verification of CMDB data quality

## Configuration Management Database (CMDB)

### CMDB System: NetBox

**NetBox Instance:**
- **URL:** {{ netbox.url }}
- **Version:** [TODO]
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}

**NetBox Functions:**
- IP Address Management (IPAM)
- Data Center Infrastructure Management (DCIM)
- Device Management
- Circuit Management
- Virtualization Management
- Configuration Context

### CMDB Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    CMDB (NetBox)                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Sites      │  │   Racks      │  │   Devices    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  IP Addresses│  │    VLANs     │  │   Circuits   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Clusters   │  │Virtual Machines│ │  Interfaces  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## CI Categories and Attributes

### Hardware CIs

#### Servers
**Category:** Hardware > Server  
**Attributes:**
- **Name:** {{ netbox.device.name }}
- **Manufacturer:** {{ netbox.device.manufacturer }}
- **Model:** {{ netbox.device.model }}
- **Serial Number:** {{ netbox.device.serial }}
- **Asset Tag:** {{ netbox.device.asset_tag }}
- **Site:** {{ netbox.device.site }}
- **Rack:** {{ netbox.device.rack }}
- **Rack Position:** {{ netbox.device.position }}
- **Status:** Active, Planned, Staged, Failed, Decommissioned
- **Role:** {{ netbox.device.role }}
- **Primary IP:** {{ netbox.device.primary_ip }}

#### Network Devices
**Category:** Hardware > Network  
**Attributes:**
- **Name:** {{ netbox.device.name }}
- **Type:** Switch, Router, Firewall, Load Balancer
- **Manufacturer:** {{ netbox.device.manufacturer }}
- **Model:** {{ netbox.device.model }}
- **Management IP:** {{ netbox.device.primary_ip }}
- **Site:** {{ netbox.device.site }}
- **Interfaces:** {{ netbox.device.interfaces }}
- **VLANs:** {{ netbox.device.vlans }}

#### Storage
**Category:** Hardware > Storage  
**Attributes:**
- **Name:** {{ netbox.device.name }}
- **Type:** SAN, NAS, DAS
- **Capacity:** [TODO] TB
- **Manufacturer:** {{ netbox.device.manufacturer }}
- **Site:** {{ netbox.device.site }}

### Software CIs

#### Operating Systems
**Category:** Software > Operating System  
**Attributes:**
- **Name:** [TODO: e.g., Ubuntu Server 22.04]
- **Version:** [TODO]
- **License:** [TODO]
- **Installed on:** {{ netbox.device.name }}
- **Patch Level:** [TODO]

#### Applications
**Category:** Software > Application  
**Attributes:**
- **Name:** [TODO: Application name]
- **Version:** [TODO]
- **Vendor:** [TODO]
- **License:** [TODO]
- **License Count:** [TODO]
- **Installed on:** {{ netbox.device.name }}
- **Responsible:** [TODO]

### Virtualization CIs

#### Hypervisor Clusters
**Category:** Virtualization > Cluster  
**Attributes:**
- **Name:** {{ netbox.cluster.name }}
- **Type:** {{ netbox.cluster.type }}
- **Site:** {{ netbox.cluster.site }}
- **Host Count:** {{ netbox.cluster.device_count }}

#### Virtual Machines
**Category:** Virtualization > Virtual Machine  
**Attributes:**
- **Name:** {{ netbox.vm.name }}
- **Cluster:** {{ netbox.vm.cluster }}
- **vCPUs:** {{ netbox.vm.vcpus }}
- **Memory:** {{ netbox.vm.memory }} GB
- **Disk:** {{ netbox.vm.disk }} GB
- **Status:** Active, Offline, Staged
- **Primary IP:** {{ netbox.vm.primary_ip }}
- **Operating System:** [TODO]

### Network CIs

#### IP Addresses
**Category:** Network > IP Address  
**Attributes:**
- **IP Address:** {{ netbox.ip.address }}
- **VLAN:** {{ netbox.ip.vlan }}
- **Status:** Active, Reserved, Deprecated
- **DNS Name:** {{ netbox.ip.dns_name }}
- **Assigned to:** {{ netbox.ip.assigned_to }}

#### VLANs
**Category:** Network > VLAN  
**Attributes:**
- **VLAN ID:** {{ netbox.vlan.vid }}
- **Name:** {{ netbox.vlan.name }}
- **Site:** {{ netbox.vlan.site }}
- **Description:** {{ netbox.vlan.description }}

#### Circuits
**Category:** Network > Circuit  
**Attributes:**
- **Circuit ID:** {{ netbox.circuit.cid }}
- **Provider:** {{ netbox.circuit.provider }}
- **Type:** {{ netbox.circuit.type }}
- **Bandwidth:** {{ netbox.circuit.commit_rate }} Mbps
- **Status:** Active, Planned, Decommissioned

### Location CIs

#### Sites
**Category:** Location > Site  
**Attributes:**
- **Name:** {{ netbox.site.name }}
- **Address:** {{ netbox.site.physical_address }}
- **Facility:** {{ netbox.site.facility }}
- **Status:** Active, Planned, Retired
- **Contact:** {{ netbox.site.contact_name }}

## CI Relationships

### Relationship Types

| Relationship | Description | Example |
|---|---|---|
| **Hosted on** | CI runs on another CI | VM hosted on Hypervisor |
| **Connected to** | Physical/logical connection | Server connected to Switch |
| **Depends on** | Functional dependency | Application depends on Database |
| **Part of** | Component of larger CI | Disk part of Server |
| **Uses** | CI uses another CI | Application uses IP Address |
| **Managed by** | Management relationship | Device managed by Management System |

### Relationship Diagram

```
┌─────────────────┐
│   Application   │
└────────┬────────┘
         │ depends on
         ▼
┌─────────────────┐
│   Database      │
└────────┬────────┘
         │ hosted on
         ▼
┌─────────────────┐
│  Virtual Machine│
└────────┬────────┘
         │ hosted on
         ▼
┌─────────────────┐
│   Hypervisor    │
└────────┬────────┘
         │ installed on
         ▼
┌─────────────────┐
│  Physical Server│
└────────┬────────┘
         │ connected to
         ▼
┌─────────────────┐
│     Switch      │
└─────────────────┘
```

### CI Dependencies

**Example: Web Application Stack**

| CI | Depends on | Relationship Type |
|---|---|---|
| Web Application | Application Server | depends on |
| Application Server | Database Server | depends on |
| Application Server | Load Balancer | connected to |
| Database Server | Storage Array | uses |
| Application Server | Virtual Machine | hosted on |
| Virtual Machine | Hypervisor Cluster | hosted on |
| Hypervisor Cluster | Physical Servers | consists of |
| Physical Servers | Network Switch | connected to |

## Change Processes for CIs

### CI Lifecycle

```
┌─────────────┐
│   Planned   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Staged    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Active    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Deprecated  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│Decommissioned│
└─────────────┘
```

### CI Change Process

#### 1. CI Creation
**Trigger:** New hardware/software procured  
**Process:**
1. Create CI in CMDB (Status: Planned)
2. Capture attributes
3. Define relationships
4. Approval by IT Operations Manager
5. Set status to "Staged"

#### 2. CI Activation
**Trigger:** CI put into operation  
**Process:**
1. Create change request (see Chapter 0140)
2. Perform CI configuration
3. Conduct tests
4. Set status to "Active"
5. Activate monitoring

#### 3. CI Modification
**Trigger:** Change to existing CI  
**Process:**
1. Create change request
2. Conduct impact analysis
3. Identify dependent CIs
4. Perform change
5. Update CMDB
6. Conduct validation

#### 4. CI Deactivation
**Trigger:** Take CI out of operation  
**Process:**
1. Create change request
2. Check dependencies
3. Create backup
4. Deactivate CI
5. Set status to "Deprecated"
6. Deactivate monitoring

#### 5. CI Deletion
**Trigger:** Permanently remove CI  
**Process:**
1. Ensure no dependencies exist
2. Archive data
3. Return licenses
4. Set status to "Decommissioned"
5. Delete from CMDB after retention period

### Change Approval for CIs

| CI Category | Approval Required By | Change Type |
|---|---|---|
| **Critical Servers** | IT Operations Manager + CIO | Normal Change |
| **Network Core** | IT Operations Manager + CIO | Normal Change |
| **Standard Servers** | IT Operations Manager | Standard Change |
| **Workstations** | Service Desk Lead | Standard Change |
| **IP Addresses** | Network Administrator | Standard Change |
| **Virtual Machines** | Virtualization Admin | Standard Change |

## CMDB Data Quality

### Data Quality Metrics

| Metric | Target Value | Measurement Frequency | Responsible |
|---|---:|---|---|
| **Completeness** | ≥ 95% | Monthly | CMDB Manager |
| **Accuracy** | ≥ 98% | Monthly | CMDB Manager |
| **Timeliness** | ≤ 7 days | Weekly | CMDB Manager |
| **Consistency** | ≥ 95% | Monthly | CMDB Manager |
| **Uniqueness** | 100% | Continuous | CMDB Manager |

### Data Quality Process

#### Regular Audits
- **Frequency:** Quarterly
- **Scope:** Sample of 10% of all CIs
- **Method:** Compare CMDB data with actual state
- **Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }}

#### Automatic Validation
- **Discovery Tools:** Automatic detection of devices and software
- **Reconciliation:** Comparison between discovery and CMDB
- **Alerts:** Notification of discrepancies
- **Correction:** Automatic or manual correction

#### Manual Verification
- **Trigger:** Before each major change
- **Process:** Manual verification of affected CIs
- **Documentation:** Document changes
- **Approval:** By IT Operations Manager

## CMDB Access and Permissions

### Access Roles

| Role | Permission | Access to |
|---|---|---|
| **CMDB Administrator** | Full access | All CIs |
| **IT Operations Manager** | Read, Write, Delete | All CIs |
| **Network Administrator** | Read, Write | Network CIs |
| **Server Administrator** | Read, Write | Server CIs |
| **Service Desk** | Read | All CIs |
| **Auditor** | Read | All CIs (Read-only) |

### Access Control

**CMDB Administrator:** {{ meta-organisation-roles.role_it_operations_manager.name }}  
**Access via:** {{ netbox.url }}  
**Authentication:** SSO/LDAP  
**Audit Logging:** All changes are logged

## CMDB Integration

### Integrated Systems

| System | Integration | Data Flow | Frequency |
|---|---|---|---|
| **Monitoring** | API | CMDB → Monitoring | Real-time |
| **Ticketing** | API | CMDB ↔ Ticketing | Real-time |
| **Asset Management** | API | Asset Mgmt → CMDB | Daily |
| **Discovery Tools** | API | Discovery → CMDB | Hourly |
| **Backup System** | API | CMDB → Backup | Daily |
| **Change Management** | API | CMDB ↔ Change Mgmt | Real-time |

### API Access

**NetBox API:**
- **Endpoint:** {{ netbox.url }}/api/
- **Authentication:** API Token
- **Documentation:** {{ netbox.url }}/api/docs/
- **Rate Limiting:** [TODO: e.g., 1000 requests/hour]

## CMDB Reporting

### Standard Reports

#### CI Inventory Report
**Frequency:** Monthly  
**Content:**
- Number of CIs per category
- CI status distribution
- New CIs in last month
- Deactivated CIs in last month

#### License Compliance Report
**Frequency:** Quarterly  
**Content:**
- Licensed software
- Installed instances
- License compliance status
- Expiring licenses

#### Network Inventory Report
**Frequency:** Monthly  
**Content:**
- IP address usage
- VLAN overview
- Network device status
- Circuit overview

#### Change Impact Report
**Frequency:** Per change  
**Content:**
- Affected CIs
- Dependent CIs
- Risk assessment
- Rollback plan

## CMDB Maintenance

### Maintenance Activities

#### Daily Activities
- [ ] Review discovery results
- [ ] Validate new CIs
- [ ] Adopt changes from change tickets
- [ ] Check alerts for discrepancies

#### Weekly Activities
- [ ] Check data quality metrics
- [ ] Identify orphaned CIs
- [ ] Validate relationships
- [ ] Perform CMDB backup

#### Monthly Activities
- [ ] Conduct CMDB audit
- [ ] Generate and distribute reports
- [ ] Check license compliance
- [ ] Archive obsolete CIs

#### Quarterly Activities
- [ ] Comprehensive CMDB audit
- [ ] Data quality review
- [ ] Process review
- [ ] Training for CMDB users

## Best Practices

### CMDB Best Practices

1. **Unique Identification:** Each CI must be uniquely identifiable
2. **Consistent Naming Convention:** Uniform naming of all CIs
3. **Complete Attributes:** Capture all relevant attributes
4. **Current Relationships:** Maintain relationships between CIs
5. **Regular Audits:** Continuously check data quality
6. **Automation:** Automate discovery and reconciliation
7. **Integration:** Integrate CMDB with other tools
8. **Documentation:** Document changes
9. **Training:** Train users regularly
10. **Governance:** Define clear responsibilities

### Naming Conventions

**Servers:**
- Format: `[Site]-[Type]-[Environment]-[Number]`
- Example: `MUC-SRV-PROD-001`

**Virtual Machines:**
- Format: `[Site]-[Type]-[Environment]-[Application]-[Number]`
- Example: `MUC-VM-PROD-WEB-001`

**Network Devices:**
- Format: `[Site]-[Type]-[Function]-[Number]`
- Example: `MUC-SW-CORE-001`

## Contacts

**CMDB Responsible:**
- **CMDB Administrator:** {{ meta-organisation-roles.role_it_operations_manager.name }} - {{ meta-organisation-roles.role_it_operations_manager.email }}
- **Network Administrator:** [TODO: Name] - [TODO: Email]
- **Server Administrator:** [TODO: Name] - [TODO: Email]
- **CIO:** {{ meta-organisation-roles.role_cio.name }} - {{ meta-organisation-roles.role_cio.email }}

**NetBox Support:**
- **URL:** {{ netbox.url }}
- **Documentation:** {{ netbox.url }}/docs/
- **Support:** [TODO: Support contact]

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organization:** {{ meta-organisation.name }}

