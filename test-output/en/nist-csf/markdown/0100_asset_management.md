
Document-ID: nist-csf-0100
Owner: [TODO]

Status: Draft
Classification: Internal

# Asset Management (ID.AM)

**Document-ID:** NIST-CSF-0100
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

This document describes the asset management program for identifying and managing data, personnel, devices, systems, and facilities that enable the organization to achieve business objectives.

## Scope

[TODO]

## Asset Categories

### 1. Hardware Assets
- Servers and workstations
- Network devices
- Mobile devices
- IoT devices
- Storage systems

### 2. Software Assets
- Operating systems
- Applications
- Databases
- Middleware
- Development tools

### 3. Data Assets
- Customer data
- Financial data
- Intellectual property
- Personnel data
- Trade secrets

### 4. Services and Systems
- Cloud services
- SaaS applications
- Managed services
- Critical business processes

### 5. Personnel
- IT personnel
- Privileged users
- External service providers
- Administrators

## Asset Inventory

### Inventory Process
1. Asset discovery (automated and manual)
2. Asset classification
3. Asset valuation
4. Documentation in CMDB
5. Regular updates

### Asset Attributes
| Attribute | Description | Required |
|-----------|-------------|----------|
| Asset-ID | Unique identifier | Yes |
| Asset-Name | Descriptive name | Yes |
| Asset-Type | Category | Yes |
| Owner | Responsible party | Yes |
| Location | Physical/logical location | Yes |
| Criticality | Business importance | Yes |
| Value | Business value | Yes |
| Status | Active/Inactive/Decommissioned | Yes |

## Asset Classification

### Criticality Levels
| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Business essential | Production systems, Customer databases |
| High | Important for operations | ERP systems, Email servers |
| Medium | Supporting systems | Intranet, Collaboration tools |
| Low | Non-critical systems | Test environments |

### Data Classification
| Classification | Description | Protection Requirements |
|----------------|-------------|------------------------|
| Highly Confidential | Highest sensitivity | Encryption, MFA, Audit logging |
| Confidential | Business sensitive | Access control, Encryption |
| Internal | Employees only | Access control |
| Public | No restrictions | Basic protection |

## Asset Lifecycle

### 1. Acquisition
- Approval process
- Security requirements
- Supplier assessment
- Contract management

### 2. Deployment
- Configuration per standards
- Security hardening
- Inventory registration
- Documentation

### 3. Operation
- Patch management
- Monitoring
- Maintenance
- Change management

### 4. Decommissioning
- Data deletion
- Asset return
- Documentation
- Disposal

## Asset Ownership

### Responsibilities

**Asset Owner:**
- Business responsibility
- Classification
- Access approval
- Compliance

**Asset Custodian (IT):**
- Technical management
- Security controls
- Backup and recovery
- Patch management

**Asset User:**
- Proper use
- Problem reporting
- Policy compliance

## Document References

- 0110_business_environment.md
- 0130_risk_assessment.md
- 0220_data_security.md (Protect)

