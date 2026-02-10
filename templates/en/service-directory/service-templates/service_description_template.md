# Service Description: [SERVICE_NAME]

> **Note:** This is a generic template. Copy this file and customize it for your specific service. Replace all [TODO] markers with service-specific information.

## Service Overview

### Basic Information
- **Service Name:** [TODO: Enter service name]
- **Service ID:** [TODO: Unique service ID]
- **Service Owner:** {{ meta.it_operations_manager.name }}
- **Technical Contact:** [TODO: Name and contact]
- **Version:** {{ meta.document.version }}
- **Last Updated:** [TODO: Date]

### Brief Description
[TODO: 2-3 sentences describing the service]

### Business Purpose
[TODO: What business value does this service provide?]

### User Groups
- [TODO: User group 1]
- [TODO: User group 2]
- [TODO: User group 3]

## Technical Details

### System Components
| Component | Type | Location | Responsible |
|---|---|---|---|
| [TODO] | [TODO] | {{ netbox.site.name }} | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

### Dependencies

#### Upstream Dependencies (Services this service depends on)
- [TODO: Service 1]
- [TODO: Service 2]
- [TODO: Service 3]

#### Downstream Dependencies (Services that depend on this service)
- [TODO: Service 1]
- [TODO: Service 2]
- [TODO: Service 3]

### Interfaces
| Interface | Type | Protocol | Port | Description |
|---|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## Operations

### Service Hours
- **Availability:** [TODO: e.g., 24/7, Mon-Fri 08:00-18:00]
- **Support Hours:** [TODO: When is support available?]
- **Maintenance Windows:** [TODO: Scheduled maintenance times]

### Service Level Agreements (SLA)

| Metric | Target Value | Measurement Method |
|---|---:|---|
| Availability | [TODO]% | [TODO] |
| Response Time | [TODO] ms | [TODO] |
| MTTR | [TODO] h | [TODO] |
| MTBF | [TODO] h | [TODO] |

### Criticality

| Dimension | Classification | Justification |
|---|---|---|
| Availability | ☐ low ☐ medium ☐ high | [TODO] |
| Integrity | ☐ low ☐ medium ☐ high | [TODO] |
| Confidentiality | ☐ low ☐ medium ☐ high | [TODO] |
| Traceability | ☐ low ☐ medium ☐ high | [TODO] |

## Monitoring and Alerting

### Monitoring Metrics
- [TODO: Metric 1 - Description and threshold]
- [TODO: Metric 2 - Description and threshold]
- [TODO: Metric 3 - Description and threshold]

### Alerting Rules
| Alert | Threshold | Priority | Escalation |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

### Dashboards
- [TODO: Link to monitoring dashboard]
- [TODO: Link to performance dashboard]

## Backup and Recovery

### Backup Strategy
- **Backup Type:** [TODO: Full/Incremental/Differential]
- **Backup Frequency:** [TODO: Daily/Weekly]
- **Retention Period:** [TODO: Days/Weeks/Months]
- **Backup Location:** [TODO: Storage location]

### Recovery Objectives
- **RTO (Recovery Time Objective):** [TODO: Hours]
- **RPO (Recovery Point Objective):** [TODO: Hours]

### Restore Procedure
1. [TODO: Step 1]
2. [TODO: Step 2]
3. [TODO: Step 3]

## Security

### Access Control
- **Authentication:** [TODO: Method]
- **Authorization:** [TODO: Role model]
- **Authorized Groups:** [TODO: AD groups/roles]

### Compliance Requirements
- [TODO: ISO 27001]
- [TODO: GDPR]
- [TODO: Other standards]

### Security Measures
- [TODO: Encryption]
- [TODO: Network segmentation]
- [TODO: Logging and monitoring]

## Contacts and Escalation

### Responsibilities
- **Service Owner:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})
- **Technical Lead:** [TODO: Name and contact]
- **On-Call:** [TODO: On-call contact]

### Escalation Path
1. **Level 1:** Service Desk - {{ meta.service_desk_lead.name }} ({{ meta.service_desk_lead.email }})
2. **Level 2:** IT Operations - {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})
3. **Level 3:** CIO - {{ meta.cio.name }} ({{ meta.cio.email }})

## Operational Processes

### Incident Management
- **Incident Categories:** [TODO: List categories]
- **Priorities:** [TODO: P1, P2, P3, P4]
- **Escalation Times:** [TODO: Time windows]

### Change Management
- **Change Categories:** [TODO: Standard, Normal, Emergency]
- **Approval Process:** [TODO: Describe process]
- **Maintenance Windows:** [TODO: Time windows]

### Problem Management
- **Known Errors:** [TODO: Document known errors]
- **Workarounds:** [TODO: Describe workarounds]

## Capacity and Performance

### Capacity Planning
- **Current Utilization:** [TODO: Percentage]
- **Growth Forecast:** [TODO: Forecast]
- **Scaling Strategy:** [TODO: Strategy]

### Performance Metrics
| Metric | Current | Target | Threshold |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

## Documentation and Knowledge Management

### Technical Documentation
- [TODO: Link to architecture diagrams]
- [TODO: Link to configuration documentation]
- [TODO: Link to operations manual]

### Runbooks
- [TODO: Link to standard runbooks]
- [TODO: Link to troubleshooting guides]

### Training Materials
- [TODO: Link to training materials]
- [TODO: Link to video tutorials]

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0.0 | [TODO] | [TODO] | Initial version |
| [TODO] | [TODO] | [TODO] | [TODO] |

---

**Document Owner:** {{ meta.document.owner }}  
**Approved By:** {{ meta.document.approver }}  
**Organization:** {{ meta.organization.name }}  
**Classification:** {{ meta.document.classification }}
