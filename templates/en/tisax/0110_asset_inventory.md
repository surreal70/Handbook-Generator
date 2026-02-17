
Document-ID: tisax-0110

Status: Draft
Classification: Internal

# Asset Inventory

**Document-ID:** [FRAMEWORK]-0110
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

## Purpose

This document describes the requirements and processes for maintaining a complete asset inventory according to TISAX requirements.

## Scope

This document applies to all assets of [TODO] that must be captured within TISAX-relevant processes.

## Inventory Requirements

### Completeness

The asset inventory must capture all relevant assets:

- Hardware (servers, workstations, network devices, mobile devices)
- Software (operating systems, applications, databases)
- Data and information
- Services (cloud services, external services)
- Documentation
- Physical infrastructure

### Currency

The inventory must be kept current:

- New assets are captured within [TODO]
- Changes are documented promptly
- Decommissioning is noted immediately
- Regular validation of inventory data

## Inventory Structure

### Mandatory Fields

The following information is captured for each asset:

| Field | Description | Example |
|-------|-------------|---------|
| Asset ID | Unique identifier | AST-2024-001 |
| Asset Name | Designation | Production Server 01 |
| Asset Type | Category | Server |
| Description | Detailed description | Main production server for ERP system |
| Asset Owner | Responsible person | [TODO] |
| Location | Physical/logical location | Data Center A, Rack 12 |
| Status | Operational status | In Operation |
| Classification | Protection level | Confidential |

### Optional Fields

Additional information depending on asset type:

- Manufacturer and model
- Serial number
- Acquisition date and cost
- Maintenance contract
- License information
- IP address/hostname
- Operating system and version
- Dependencies on other assets
- Backup status

## Inventorization Process

### 1. Asset Capture

#### Automated Capture

[TODO] uses the following tools:

- **Network Discovery**: [TODO]
- **Endpoint Management**: [TODO]
- **Cloud Asset Management**: [TODO]
- **CMDB Integration**: [TODO]

#### Manual Capture

For assets that cannot be captured automatically:

1. Complete asset capture form
2. Classification by asset owner
3. Entry in asset inventory system
4. Validation by asset management team

### 2. Asset Registration

New assets are registered through:

1. **Procurement Process**: Automatic capture upon ordering
2. **Onboarding**: Capture during commissioning
3. **Discovery**: Identification through scanning
4. **Reporting**: Manual reporting by employees

### 3. Asset Updates

Changes are captured for:

- Hardware upgrades
- Software updates
- Location changes
- Owner changes
- Classification changes
- Status changes

### 4. Asset Decommissioning

Upon decommissioning:

1. Set asset status to "Decommissioned"
2. Document secure data deletion
3. Physical disposal or archiving
4. Release licenses
5. Resolve dependencies

## Inventory Categories

### Hardware Assets

**Servers and Infrastructure:**
- Physical servers
- Virtual machines
- Storage systems
- Network devices (routers, switches, firewalls)

**Endpoints:**
- Workstations and laptops
- Mobile devices (smartphones, tablets)
- Printers and multifunction devices
- IoT devices

### Software Assets

**System Software:**
- Operating systems
- Virtualization platforms
- Database management systems
- Middleware

**Application Software:**
- Business applications
- Development tools
- Office software
- Security software

### Information Assets

**Data:**
- Customer data
- Product data
- Financial data
- Personnel data
- Prototypes and development data

**Documentation:**
- Technical documentation
- Process documentation
- Contracts and agreements
- Policies and procedures

### Service Assets

- Cloud services (IaaS, PaaS, SaaS)
- Managed services
- External services
- Support contracts

## Inventory Management

### Responsibilities

**Asset Management Team:**
- Maintenance of inventory system
- Coordination of inventorization
- Quality assurance of data
- Reporting

**Asset Owner:**
- Classification of their assets
- Validation of asset information
- Reporting of changes
- Approval of access

**IT Department:**
- Technical capture of IT assets
- Automated discovery
- Integration with CMDB
- Provision of asset data

### Inventory System

[TODO] uses the following system for asset inventory:

- **System**: [TODO]
- **Access**: [TODO]
- **Backup**: [TODO]
- **Integration**: [TODO]

## Inventory Validation

### Regular Review

**Annual Full Review:**
- Complete inventory of all assets
- Comparison with physical inventory
- Validation of all asset information
- Cleanup of outdated entries

**Quarterly Sampling:**
- Review of critical assets
- Validation of high-risk assets
- Review of classification
- Check of asset owner assignment

**Continuous Monitoring:**
- Automatic consistency checks
- Detection of uncaptured assets
- Identification of deviations
- Alerting for critical changes

### Quality Assurance

Quality criteria for the inventory:

- **Completeness**: >95% of all assets captured
- **Currency**: <5% outdated entries
- **Accuracy**: <2% incorrect information
- **Consistency**: 100% mandatory fields completed

## Integration and Interfaces

### CMDB Integration

Integration with Configuration Management Database:

- Bidirectional data exchange
- Synchronization of CI information
- Consistency checking
- Automatic updates

### Change Management

Integration with change management:

- Automatic update upon changes
- Validation of asset changes
- Tracking of configuration changes
- Impact analysis

### Procurement

Integration with procurement:

- Automatic capture of new assets
- License management
- Cost tracking
- Contract management

## TISAX-Specific Requirements

### VDA ISA Controls

This document addresses:

- **2.2.1**: Inventory of assets
- **2.2.2**: Ownership of assets
- **2.2.3**: Acceptable use of assets

### Assessment Evidence

For TISAX assessments:

- Complete asset inventory
- Inventorization process documentation
- Evidence of regular validation
- Examples of asset records
- Reports on inventory quality

## Reporting

### Regular Reports

**Monthly:**
- Number of newly captured assets
- Number of decommissioned assets
- Inventory quality metrics
- Unassigned assets

**Quarterly:**
- Completeness analysis
- Classification overview
- Asset owner distribution
- Trend analyses

**Annually:**
- Total inventory report
- Asset value analysis
- Compliance status
- Improvement recommendations

## Metrics

[TODO] measures:

- Number of captured assets by category
- Inventory completeness (Target: >95%)
- Currency of data (Target: <30 days since last review)
- Percentage of classified assets (Target: 100%)
- Number of unassigned assets (Target: 0)
- Time to capture new assets (Target: <5 days)

<!-- Note: Adapt tools and metrics to your organization -->

<!-- End of template -->
