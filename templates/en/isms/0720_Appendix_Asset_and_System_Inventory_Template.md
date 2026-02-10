# Appendix B: Asset and System Inventory

**Document Type:** Appendix  
**Version:** {{ meta.document.version }}  
**Date:** {{ meta.document.date }}  
**Classification:** {{ meta.document.classification }}

---

## Purpose

This document represents the central asset and system inventory of the organization. It fulfills the requirements of ISO/IEC 27001:2022 Annex A 5.9 (Inventory of Information and Other Associated Assets) and serves as the foundation for:

- Asset management and lifecycle management
- Risk assessment and protection needs determination
- Incident response and business continuity planning
- Compliance evidence and audits

The inventory is continuously maintained and reviewed at least quarterly.

## Scope

**Organization:** {{ meta.organization.name }}  
**ISMS Scope:** {{ meta.isms.scope }}  
**Responsible:** Asset Management Team, {{ meta.ciso.name }}

---

## Asset Categories

The inventory includes the following asset categories:

1. **Hardware Assets:** Servers, network devices, endpoints, storage
2. **Software Assets:** Operating systems, applications, licenses
3. **Data Assets:** Databases, file systems, repositories
4. **Network Assets:** VLANs, subnets, connections
5. **Cloud Assets:** Cloud services, SaaS applications
6. **Physical Assets:** Rooms, infrastructure, documentation

---

## Asset Classification

Each asset is classified according to the following criteria:

### Protection Requirements (Confidentiality, Integrity, Availability)

| Level | Description | Example |
|-------|-------------|---------|
| **High** | Critical for business operations, high damage if compromised | Production databases, core banking systems |
| **Medium** | Important for business operations, medium damage if compromised | Internal applications, development systems |
| **Low** | Non-critical, low damage if compromised | Test systems, public information |

### Criticality

| Level | RTO | RPO | Description |
|-------|-----|-----|-------------|
| **Tier 1** | < 4h | < 1h | Business-critical, immediate recovery required |
| **Tier 2** | < 24h | < 4h | Important, recovery within one business day |
| **Tier 3** | < 72h | < 24h | Standard, recovery within 3 days |
| **Tier 4** | > 72h | > 24h | Non-critical, no time-critical recovery |

---

## Hardware Assets

### Servers

| Asset-ID | Hostname | Type | Location | Owner | Protection Req (C/I/A) | Criticality | Status |
|----------|----------|------|----------|-------|------------------------|-------------|--------|
| SRV-001 | {{ netbox.device.primary_server.name }} | Physical Server | {{ netbox.site.name }} | IT Operations | High/High/High | Tier 1 | Production |
| SRV-002 | {{ netbox.device.backup_server.name }} | Physical Server | {{ netbox.site.name }} | IT Operations | High/High/Medium | Tier 2 | Production |
| [TODO] | [TODO: Hostname] | [TODO: Type] | [TODO: Location] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] | [TODO: Status] |

**Note:** Import complete server list from NetBox/CMDB.

---

### Network Devices

| Asset-ID | Hostname | Type | Location | Owner | Protection Req (C/I/A) | Criticality | Status |
|----------|----------|------|----------|-------|------------------------|-------------|--------|
| NET-001 | {{ netbox.device.core_switch.name }} | Core Switch | {{ netbox.site.name }} | Network Team | Medium/High/High | Tier 1 | Production |
| NET-002 | {{ netbox.device.firewall.name }} | Firewall | {{ netbox.site.name }} | Security Team | High/High/High | Tier 1 | Production |
| [TODO] | [TODO: Hostname] | [TODO: Type] | [TODO: Location] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] | [TODO: Status] |

**Note:** Import complete network device list from NetBox.

---

### Endpoints

| Asset-ID | Hostname | Type | User | Owner | Protection Req (C/I/A) | Status |
|----------|----------|------|------|-------|------------------------|--------|
| WS-001 | {{ meta.ciso.workstation }} | Laptop | {{ meta.ciso.name }} | IT Operations | High/Medium/Medium | Production |
| [TODO] | [TODO: Hostname] | [TODO: Type] | [TODO: User] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Status] |

**Note:** Import endpoint inventory from MDM/Endpoint Management System.

---

### Storage Systems

| Asset-ID | Name | Type | Capacity | Location | Owner | Protection Req (C/I/A) | Criticality |
|----------|------|------|----------|----------|-------|------------------------|-------------|
| STO-001 | {{ netbox.device.storage.name }} | SAN | [TODO: Capacity] | {{ netbox.site.name }} | IT Operations | High/High/High | Tier 1 |
| [TODO] | [TODO: Name] | [TODO: Type] | [TODO: Capacity] | [TODO: Location] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] |

---

## Software Assets

### Operating Systems

| Asset-ID | Name | Version | License Type | License Count | Owner | Criticality |
|----------|------|---------|--------------|---------------|-------|-------------|
| OS-001 | Windows Server | 2022 | Volume License | [TODO: Count] | IT Operations | Tier 1 |
| OS-002 | Red Hat Enterprise Linux | 9.x | Subscription | [TODO: Count] | IT Operations | Tier 1 |
| OS-003 | Ubuntu Server | 22.04 LTS | Open Source | Unlimited | IT Operations | Tier 2 |
| [TODO] | [TODO: Name] | [TODO: Version] | [TODO: License Type] | [TODO: Count] | [TODO: Owner] | [TODO: Tier] |

---

### Business Applications

| Asset-ID | Name | Version | Vendor | License Type | Owner | Protection Req (C/I/A) | Criticality |
|----------|------|---------|--------|--------------|-------|------------------------|-------------|
| APP-001 | [TODO: ERP System] | [TODO: Version] | [TODO: Vendor] | [TODO: License Type] | Business Owner | High/High/High | Tier 1 |
| APP-002 | [TODO: CRM System] | [TODO: Version] | [TODO: Vendor] | [TODO: License Type] | Sales | High/Medium/Medium | Tier 2 |
| [TODO] | [TODO: Name] | [TODO: Version] | [TODO: Vendor] | [TODO: License Type] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] |

---

### Security Software

| Asset-ID | Name | Version | Type | Coverage | Owner | Criticality |
|----------|------|---------|------|----------|-------|-------------|
| SEC-001 | [TODO: EDR Solution] | [TODO: Version] | Endpoint Detection & Response | All Endpoints | Security Team | Tier 1 |
| SEC-002 | [TODO: SIEM] | [TODO: Version] | Security Information & Event Management | All Systems | Security Team | Tier 1 |
| SEC-003 | [TODO: Firewall] | [TODO: Version] | Next-Gen Firewall | Perimeter | Security Team | Tier 1 |
| [TODO] | [TODO: Name] | [TODO: Version] | [TODO: Type] | [TODO: Coverage] | [TODO: Owner] | [TODO: Tier] |

---

## Data Assets

### Databases

| Asset-ID | Name | Type | Version | Server | Owner | Protection Req (C/I/A) | Criticality | Backup |
|----------|------|------|---------|--------|-------|------------------------|-------------|--------|
| DB-001 | [TODO: Production DB] | [TODO: PostgreSQL/MySQL/Oracle] | [TODO: Version] | SRV-001 | DBA Team | High/High/High | Tier 1 | Daily |
| DB-002 | [TODO: Test DB] | [TODO: Type] | [TODO: Version] | [TODO: Server] | DBA Team | Low/Medium/Low | Tier 3 | Weekly |
| [TODO] | [TODO: Name] | [TODO: Type] | [TODO: Version] | [TODO: Server] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] | [TODO: Backup] |

---

### File Systems and Shares

| Asset-ID | Name | Type | Path | Server | Owner | Protection Req (C/I/A) | Backup |
|----------|------|------|------|--------|-------|------------------------|--------|
| FS-001 | [TODO: Department Share] | SMB Share | [TODO: Path] | [TODO: Server] | IT Operations | Medium/Medium/Medium | Daily |
| FS-002 | [TODO: Project Share] | SMB Share | [TODO: Path] | [TODO: Server] | Project Management | High/Medium/Medium | Daily |
| [TODO] | [TODO: Name] | [TODO: Type] | [TODO: Path] | [TODO: Server] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Backup] |

---

### Code Repositories

| Asset-ID | Name | Type | URL | Owner | Protection Req (C/I/A) | Backup |
|----------|------|------|-----|-------|------------------------|--------|
| REPO-001 | [TODO: Main Repository] | Git | [TODO: URL] | Development Team | High/High/Medium | Daily |
| [TODO] | [TODO: Name] | [TODO: Type] | [TODO: URL] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Backup] |

---

## Network Assets

### VLANs

| VLAN-ID | Name | Subnet | Purpose | Security Zone | Owner |
|---------|------|--------|---------|---------------|-------|
| {{ netbox.vlan.management.vid }} | {{ netbox.vlan.management.name }} | {{ netbox.vlan.management.subnet }} | Management | Restricted | Network Team |
| {{ netbox.vlan.production.vid }} | {{ netbox.vlan.production.name }} | {{ netbox.vlan.production.subnet }} | Production | Internal | Network Team |
| [TODO] | [TODO: Name] | [TODO: Subnet] | [TODO: Purpose] | [TODO: Zone] | [TODO: Owner] |

**Note:** Import complete VLAN list from NetBox.

---

### External Connections

| Connection-ID | Type | Provider | Bandwidth | Purpose | Owner | Criticality |
|---------------|------|----------|-----------|---------|-------|-------------|
| WAN-001 | Internet | [TODO: Provider] | [TODO: Bandwidth] | Internet Access | Network Team | Tier 1 |
| WAN-002 | MPLS | [TODO: Provider] | [TODO: Bandwidth] | Site-to-Site | Network Team | Tier 1 |
| [TODO] | [TODO: Type] | [TODO: Provider] | [TODO: Bandwidth] | [TODO: Purpose] | [TODO: Owner] | [TODO: Tier] |

---

## Cloud Assets

### Cloud Services (IaaS/PaaS)

| Asset-ID | Service Name | Provider | Type | Region | Owner | Protection Req (C/I/A) | Criticality |
|----------|--------------|----------|------|--------|-------|------------------------|-------------|
| CLOUD-001 | [TODO: VM Instances] | [TODO: AWS/Azure/GCP] | IaaS | [TODO: Region] | Cloud Team | High/High/High | Tier 1 |
| CLOUD-002 | [TODO: Database Service] | [TODO: Provider] | PaaS | [TODO: Region] | DBA Team | High/High/High | Tier 1 |
| [TODO] | [TODO: Service] | [TODO: Provider] | [TODO: Type] | [TODO: Region] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] |

---

### SaaS Applications

| Asset-ID | Service Name | Provider | Purpose | User Count | Owner | Protection Req (C/I/A) |
|----------|--------------|----------|---------|------------|-------|------------------------|
| SAAS-001 | Microsoft 365 | Microsoft | Productivity | [TODO: Count] | IT Operations | High/Medium/High |
| SAAS-002 | [TODO: CRM SaaS] | [TODO: Provider] | Customer Management | [TODO: Count] | Sales | High/Medium/Medium |
| [TODO] | [TODO: Service] | [TODO: Provider] | [TODO: Purpose] | [TODO: Count] | [TODO: Owner] | [TODO: C/I/A] |

---

## Physical Assets

### Sites and Rooms

| Site-ID | Name | Address | Type | Security Level | Owner |
|---------|------|---------|------|----------------|-------|
| SITE-001 | {{ netbox.site.name }} | {{ netbox.site.address }} | Main Site | High | Facility Management |
| SITE-002 | [TODO: Branch Office] | [TODO: Address] | Branch Office | Medium | Facility Management |
| [TODO] | [TODO: Name] | [TODO: Address] | [TODO: Type] | [TODO: Security] | [TODO: Owner] |

---

### Server Rooms and Data Centers

| Room-ID | Name | Site | Type | Size | Air Conditioning | Fire Suppression | Access Control |
|---------|------|------|------|------|------------------|------------------|----------------|
| ROOM-001 | Server Room 1 | SITE-001 | Server Room | [TODO: m²] | Redundant | FM-200 | Biometric |
| [TODO] | [TODO: Name] | [TODO: Site] | [TODO: Type] | [TODO: Size] | [TODO: AC] | [TODO: Fire] | [TODO: Access] |

---

### Critical Infrastructure

| Asset-ID | Name | Type | Site | Capacity | Redundancy | Owner | Criticality |
|----------|------|------|------|----------|------------|-------|-------------|
| INFRA-001 | UPS System 1 | UPS | SITE-001 | [TODO: kVA] | N+1 | Facility Management | Tier 1 |
| INFRA-002 | AC Unit 1 | Air Conditioning | SITE-001 | [TODO: kW] | N+1 | Facility Management | Tier 1 |
| INFRA-003 | Emergency Generator | Generator | SITE-001 | [TODO: kW] | N | Facility Management | Tier 1 |
| [TODO] | [TODO: Name] | [TODO: Type] | [TODO: Site] | [TODO: Capacity] | [TODO: Redundancy] | [TODO: Owner] | [TODO: Tier] |

---

## Asset Lifecycle Management

### Lifecycle Phases

| Phase | Description | Responsible | Process |
|-------|-------------|-------------|---------|
| **Planning** | Requirements determination, budgeting | Business Owner | Requirements Management |
| **Procurement** | Selection, ordering, delivery | Procurement | Procurement Process |
| **Deployment** | Installation, configuration, testing | IT Operations | Change Management |
| **Operation** | Usage, maintenance, monitoring | IT Operations | Operations Processes |
| **Maintenance** | Updates, patches, repairs | IT Operations | Patch Management |
| **Decommissioning** | Decommissioning, data deletion | IT Operations | Decommissioning Process |
| **Disposal** | Secure disposal or reuse | IT Operations | Disposal Process |

---

### Asset Owners and Responsibilities

| Role | Responsibilities | Contact |
|------|------------------|---------|
| **Asset Owner** | Business responsibility, approvals, budget | [TODO: Name/Department] |
| **Technical Owner** | Technical responsibility, operations, maintenance | IT Operations |
| **Security Owner** | Security requirements, risk assessment | {{ meta.ciso.name }} |
| **Data Owner** | Data classification, access control | [TODO: Name/Department] |

---

## Asset Tagging and Labeling

### Tagging Schema

All assets are tagged with the following tags:

| Tag Category | Description | Example |
|--------------|-------------|---------|
| **Environment** | Environment | Production, Development, Test, QA |
| **Criticality** | Criticality | Tier1, Tier2, Tier3, Tier4 |
| **Owner** | Responsible | IT-Ops, Security, Development |
| **CostCenter** | Cost Center | [TODO: Cost Centers] |
| **Project** | Project | [TODO: Project Name] |
| **Compliance** | Compliance Requirements | PCI-DSS, GDPR, ISO27001 |

**Note:** Tagging is maintained in CMDB/Asset Management System.

---

## Inventory Process

### Regular Review

| Activity | Frequency | Responsible | Documentation |
|----------|-----------|-------------|---------------|
| **Complete Inventory** | Annually | Asset Management Team | Inventory Report |
| **Quarterly Review** | Quarterly | Asset Owners | Review Protocol |
| **Automatic Discovery** | Daily | IT Operations | Discovery Logs |
| **Change Tracking** | Continuous | Change Management | Change Records |

---

### Discovery Tools

| Tool | Purpose | Coverage | Owner |
|------|---------|----------|-------|
| NetBox | Network and Infrastructure Inventory | Network Devices, Servers, VLANs | Network Team |
| CMDB | Configuration Management Database | All IT Assets | IT Operations |
| MDM | Mobile Device Management | Endpoints, Mobile Devices | IT Operations |
| Cloud Asset Inventory | Cloud Resources | Cloud Services | Cloud Team |
| [TODO: Tool] | [TODO: Purpose] | [TODO: Coverage] | [TODO: Owner] |

---

## Compliance and Audit

### Audit Requirements

This inventory fulfills the following compliance requirements:

- **ISO/IEC 27001:2022 Annex A 5.9:** Inventory of Information and Other Associated Assets
- **ISO/IEC 27001:2022 Annex A 5.10:** Acceptable Use of Information and Other Associated Assets
- **ISO/IEC 27001:2022 Annex A 8.9:** Configuration Management
- **[TODO: Additional Compliance Requirements]**

---

### Audit Trail

| Date | Change | Performed By | Approved By | Reason |
|------|--------|--------------|-------------|--------|
| {{ meta.document.date }} | Initial Creation | {{ meta.document.author }} | {{ meta.ciso.name }} | ISMS Implementation |
| [TODO: Date] | [TODO: Change] | [TODO: Name] | [TODO: Name] | [TODO: Reason] |

---

## References

- Policy: 0300_Policy_Asset_Management.md
- Guideline: 0310_Guideline_Asset_Inventory_Tagging_and_Disposal.md
- Document: 0100_ISMS_Statement_of_Applicability_SoA_Template.md
- Appendix: 0730_Appendix_Data_Flow_and_Interfaces_Template.md

---

**Document Owner:** Asset Management Team  
**Approved By:** {{ meta.ciso.name }}  
**Next Review:** Quarterly

<!-- 
TEMPLATE AUTHOR NOTE:
This inventory should be generated from automated systems (NetBox, CMDB, MDM).
Manual maintenance is error-prone and should be minimized.
Ensure all assets are tagged with correct protection requirements and criticality.
Integrate this inventory into your risk assessment and BIA processes.
-->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
