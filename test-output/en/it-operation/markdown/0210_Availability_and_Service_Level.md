# Availability and Service Level

**Document-ID:** [FRAMEWORK]-0210
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

This document defines availability requirements, Service Level Agreements (SLAs), and Service Level Objectives (SLOs) for the IT service. It describes measurement methods, reporting processes, and measures for continuous improvement of service availability.

**Document Owner:** [TODO]  
**Approved by:** [TODO]  
**Version:** 0  
**Organization:** AdminSend GmbH

## Availability Requirements

### Service Classification

| Service Class | Availability | Max Downtime/Year | Max Downtime/Month | Business Criticality |
|---|---:|---:|---:|---|
| Critical | 99.95% | 4.38 hours | 21.6 minutes | High |
| Important | 99.5% | 43.8 hours | 3.6 hours | Medium |
| Standard | 99.0% | 87.6 hours | 7.2 hours | Low |
| Non-critical | 95.0% | 438 hours | 36 hours | Very low |

### Service Times

#### Production Services
- **Availability:** 24/7/365
- **Support Hours:** 24/7 with on-call availability
- **Maintenance Window:** Sunday 02:00-06:00 (after announcement)
- **Emergency Maintenance:** After approval by [TODO]

#### Business Services
- **Availability:** Mon-Fri 06:00-22:00
- **Support Hours:** Mon-Fri 08:00-18:00
- **Maintenance Window:** Saturday 20:00-24:00
- **Emergency Maintenance:** After approval by {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Development/Test Services
- **Availability:** Mon-Fri 08:00-18:00
- **Support Hours:** Best Effort
- **Maintenance Window:** Anytime after announcement
- **Emergency Maintenance:** Not required

### Planned Maintenance Windows

| Maintenance Type | Frequency | Duration | Announcement Period | Approval |
|---|---|---|---|---|
| Routine Maintenance | Monthly | 2-4 hours | 7 days | Ops Manager |
| Patch Deployment | Monthly | 1-2 hours | 5 days | Ops Manager |
| Major Upgrade | Quarterly | 4-8 hours | 14 days | CIO |
| Emergency Maintenance | Ad-hoc | Variable | 4 hours | CIO |

## Service Level Agreements (SLA)

### SLA Definitions

#### Availability SLA

**Service:** [TODO: Service Name]  
**Valid from:** [TODO: Date]  
**Duration:** 12 months with automatic renewal

| Metric | Target | Measurement Method | Measurement Interval |
|---|---:|---|---|
| Availability | 99.5% | Uptime Monitoring | Monthly |
| Planned Downtime | < 4h/month | Change Calendar | Monthly |
| Unplanned Downtime | < 2h/month | Incident Tracking | Monthly |
| MTBF (Mean Time Between Failures) | > 720h | Incident Analysis | Quarterly |
| MTTR (Mean Time To Repair) | < 2h | Incident Tickets | Monthly |

#### Performance SLA

| Metric | Target | Warning Threshold | Measurement Method | Measurement Interval |
|---|---:|---:|---|---|
| Response Time (Avg) | < 200ms | > 300ms | APM Tool | Continuous |
| Response Time (95th) | < 500ms | > 750ms | APM Tool | Continuous |
| Response Time (99th) | < 1000ms | > 1500ms | APM Tool | Continuous |
| Throughput | > 1000 TPS | < 800 TPS | APM Tool | Continuous |
| Error Rate | < 0.1% | > 0.5% | APM Tool | Continuous |

#### Support SLA

| Priority | Response Time | Resolution Time | Availability | Escalation |
|---|---|---|---|---|
| P1 - Critical | 15 minutes | 4 hours | 24/7 | Immediately to CIO |
| P2 - High | 1 hour | 8 hours | 24/7 | After 4h to Ops Manager |
| P3 - Medium | 4 hours | 24 hours | Mon-Fri 08-18 | After 24h to Ops Manager |
| P4 - Low | 8 hours | 72 hours | Mon-Fri 08-18 | After 72h to Ops Manager |

### SLA Contract Partners

#### Internal SLAs
- **Service Provider:** IT Operations ({{ meta-organisation-roles.role_IT_Operations_Manager }})
- **Service Consumer:** Business Departments
- **Responsible:** [TODO]
- **Review Cycle:** Quarterly

#### External SLAs
- **Service Provider:** AdminSend GmbH
- **Service Consumer:** [TODO: Customer/Partner]
- **Contract Duration:** [TODO: Duration]
- **Penalties:** [TODO: Penalties for SLA violations]

### SLA Exceptions

#### Exclusion Criteria (Force Majeure)
- Natural disasters
- Terrorist attacks
- Wars and civil unrest
- Pandemics
- Power outages beyond control

#### Planned Exceptions
- Announced maintenance windows
- Approved emergency maintenance
- Customer-caused outages
- Third-party outages beyond control

## Service Level Objectives (SLO)

### Internal SLOs

#### Infrastructure SLOs

| Component | SLO | Measurement Method | Responsible |
|---|---:|---|---|
| Compute Cluster | 99.9% | Hypervisor Monitoring | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Storage System | 99.95% | Storage Monitoring | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Network Core | 99.99% | Network Monitoring | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Firewall | 99.95% | Security Monitoring | [TODO] |
| Load Balancer | 99.9% | LB Monitoring | {{ meta-organisation-roles.role_IT_Operations_Manager }} |

#### Application SLOs

| Application | Availability | Response Time | Error Rate | Responsible |
|---|---:|---:|---:|---|
| [TODO: App 1] | 99.5% | < 200ms | < 0.1% | [TODO] |
| [TODO: App 2] | 99.0% | < 500ms | < 0.5% | [TODO] |
| [TODO: App 3] | 99.9% | < 100ms | < 0.05% | [TODO] |

#### Database SLOs

| Database | Availability | Query Time | Connection Time | Responsible |
|---|---:|---:|---:|---|
| [TODO: DB 1] | 99.95% | < 50ms | < 10ms | [TODO] |
| [TODO: DB 2] | 99.5% | < 100ms | < 20ms | [TODO] |

### Error Budget

#### Error Budget Concept
- **Definition:** Tolerable downtime within the SLO period
- **Calculation:** (100% - SLO) × Period
- **Usage:** Balance between innovation and stability

#### Error Budget Example (99.5% SLO)

| Period | Availability | Error Budget | Downtime |
|---|---:|---:|---:|
| Month | 99.5% | 0.5% | 3.6 hours |
| Quarter | 99.5% | 0.5% | 10.8 hours |
| Year | 99.5% | 0.5% | 43.8 hours |

#### Error Budget Policy

**When Error Budget > 50% remaining:**
- Normal development velocity
- New features and experiments allowed
- Routine maintenance as planned

**When Error Budget 25-50% remaining:**
- Increased caution with changes
- Focus on stability
- Additional testing requirements

**When Error Budget < 25% remaining:**
- Feature freeze
- Only critical bugfixes
- Focus on reliability improvements
- Postmortem for all incidents

**When Error Budget exhausted:**
- Complete change freeze
- Only emergency fixes
- Root cause analysis of all outages
- Improvement plan before resumption

## Availability Measurement

### Measurement Methods

#### Synthetic Monitoring
- **Method:** Automated tests of defined endpoints
- **Frequency:** Every 1-5 minutes
- **Locations:** Multiple geographic locations
- **Metrics:** Availability, Response Time, Functionality

#### Real User Monitoring (RUM)
- **Method:** Measurement of actual user interactions
- **Collection:** Client-side metrics
- **Metrics:** Page Load Time, User Experience, Error Rate
- **Privacy:** GDPR compliant, anonymized

#### Server-Side Monitoring
- **Method:** Monitoring of server metrics
- **Collection:** Logs, Metrics, Traces
- **Metrics:** Uptime, Resource Usage, Error Logs
- **Aggregation:** Central monitoring system

### Availability Calculation

#### Formula
```
Availability (%) = (Total Time - Downtime) / Total Time × 100
```

#### Example Calculation (Month with 720 hours)
```
Total Time: 720 hours
Planned Maintenance: 2 hours (excluded)
Unplanned Outages: 1.5 hours
Available Time: 720 - 2 = 718 hours
Actual Availability: (718 - 1.5) / 718 × 100 = 99.79%
```

#### Exclusions
- Planned and announced maintenance windows
- Customer-caused outages
- Force Majeure events
- Third-party outages (as agreed)

### Monitoring Tools

| Tool | Purpose | Measurement Interval | Access |
|---|---|---|---|
| [TODO: Uptime Tool] | Availability Monitoring | 1 minute | [TODO: URL] |
| [TODO: APM Tool] | Performance Monitoring | Continuous | [TODO: URL] |
| [TODO: RUM Tool] | Real User Monitoring | Continuous | [TODO: URL] |
| [TODO: Log Tool] | Log Aggregation | Real-time | [TODO: URL] |

## Service Level Reporting

### Report Types

#### Daily Availability Report
- **Recipients:** IT Operations Team
- **Content:**
  - Availability of last 24 hours
  - Incidents and outages
  - Performance metrics
  - Current alerts
- **Delivery:** Automatically at 08:00

#### Weekly SLA Report
- **Recipients:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
- **Content:**
  - Weekly availability
  - SLA compliance status
  - Trend analysis
  - Recommendations
- **Delivery:** Every Monday

#### Monthly SLA Report
- **Recipients:** [TODO], Stakeholders
- **Content:**
  - Monthly availability
  - SLA fulfillment vs. targets
  - Incident summary
  - Error Budget status
  - Improvement measures
- **Delivery:** First business day of following month

#### Quarterly Management Report
- **Recipients:** [TODO], [TODO], [TODO]
- **Content:**
  - Quarterly availability
  - SLA trends
  - Cost-benefit analysis
  - Strategic recommendations
- **Delivery:** Quarter end + 5 business days

### Report Metrics

#### Availability Dashboard

| Metric | Target | Current (Month) | Trend | Status |
|---|---:|---:|---|---|
| Overall Availability | 99.5% | [TODO]% | [TODO] | ✓ / ⚠ / ✗ |
| Unplanned Outages | < 2h | [TODO]h | [TODO] | ✓ / ⚠ / ✗ |
| MTBF | > 720h | [TODO]h | [TODO] | ✓ / ⚠ / ✗ |
| MTTR | < 2h | [TODO]h | [TODO] | ✓ / ⚠ / ✗ |
| Error Budget Remaining | > 0% | [TODO]% | [TODO] | ✓ / ⚠ / ✗ |

#### Incident Statistics

| Priority | Count | Avg. MTTR | SLA Fulfillment | Trend |
|---|---:|---:|---:|---|
| P1 - Critical | [TODO] | [TODO]h | [TODO]% | [TODO] |
| P2 - High | [TODO] | [TODO]h | [TODO]% | [TODO] |
| P3 - Medium | [TODO] | [TODO]h | [TODO]% | [TODO] |
| P4 - Low | [TODO] | [TODO]h | [TODO]% | [TODO] |

## Availability Improvements

### Improvement Measures

#### Redundancy and High Availability
- **Active-Active Cluster:** Load distribution across multiple nodes
- **Active-Passive Cluster:** Failover configuration
- **Geographic Redundancy:** Multi-region deployment
- **Database Replication:** Synchronous/Asynchronous replication
- **Load Balancing:** Distribution of load across multiple instances

#### Automation
- **Auto-Healing:** Automatic recovery from failures
- **Auto-Scaling:** Automatic capacity adjustment
- **Automated Failover:** Automatic failover on failure
- **Health Checks:** Continuous health monitoring
- **Self-Service:** Automated provisioning

#### Monitoring and Alerting
- **Proactive Monitoring:** Early detection of problems
- **Predictive Analytics:** Prediction of failures
- **Intelligent Alerting:** Reduction of false positives
- **Anomaly Detection:** ML-based anomaly detection
- **Distributed Tracing:** End-to-end tracing

#### Process Improvements
- **Incident Management:** Optimization of incident processes
- **Change Management:** Reduction of change-related outages
- **Capacity Management:** Proactive capacity planning
- **Disaster Recovery:** Improvement of DR processes
- **Continuous Improvement:** Regular retrospectives

### Improvement Roadmap

| Quarter | Measure | Expected Impact | Responsible | Status |
|---|---|---|---|---|
| Q1 2026 | [TODO] | +0.1% Availability | [TODO] | Planned |
| Q2 2026 | [TODO] | -30min MTTR | [TODO] | Planned |
| Q3 2026 | [TODO] | +0.2% Availability | [TODO] | Planned |
| Q4 2026 | [TODO] | -50% Incidents | [TODO] | Planned |

### Lessons Learned

#### Postmortem Process
1. **Incident Documentation:** Detailed description of the incident
2. **Timeline Creation:** Chronological sequence
3. **Root Cause Analysis:** 5-Why method
4. **Impact Assessment:** Affected systems and users
5. **Corrective Actions:** Immediate measures and long-term improvements
6. **Follow-Up:** Review of implementation

#### Postmortem Template
- **Incident ID:** [TODO]
- **Date/Time:** [TODO]
- **Duration:** [TODO]
- **Affected Services:** [TODO]
- **Root Cause:** [TODO]
- **Actions:** [TODO]
- **Responsible:** [TODO]
- **Status:** [TODO]

## SLA Review and Adjustment

### Review Process

#### Quarterly SLA Review
- **Participants:** [TODO], {{ meta-organisation-roles.role_IT_Operations_Manager }}, Stakeholders
- **Agenda:**
  - SLA fulfillment of last 3 months
  - Trend analysis
  - Improvement potential
  - Adjustment needs
- **Output:** Review protocol with recommendations

#### Annual SLA Review
- **Participants:** [TODO], [TODO], [TODO], Stakeholders
- **Agenda:**
  - Annual availability
  - SLA appropriateness
  - Cost-benefit analysis
  - Strategic alignment
- **Output:** SLA adjustments for following year

### Adjustment Criteria

#### SLA Tightening (higher requirements)
- Business criticality increased
- Competitive pressure
- Regulatory requirements
- Customer feedback

#### SLA Relaxation (lower requirements)
- Cost-benefit ratio
- Technical feasibility
- Business priority decreased
- Realistic goal setting

## Processes and Responsibilities

### RACI Matrix

| Activity | CIO | Ops Manager | Ops Team | Stakeholder |
|---|---|---|---|---|
| SLA Definition | A | R | C | C |
| Availability Measurement | I | A | R | - |
| SLA Reporting | C | A | R | I |
| SLA Review | A | R | C | C |
| Improvement Measures | A | R | C | I |
| Incident Response | I | A | R | I |
| Postmortems | C | A | R | I |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### Escalation Path

1. **Level 1:** Operations Team - Incident response and monitoring
2. **Level 2:** {{ meta-organisation-roles.role_IT_Operations_Manager }} - SLA violations
3. **Level 3:** [TODO] - Critical SLA violations
4. **Level 4:** [TODO] - Contractual consequences

## Compliance and Standards

### Relevant Standards
- **ITIL v4:** Availability Management Practice
- **ISO 20000:** Clause 8.9 - Availability Management
- **COBIT 2019:** DSS01 - Managed Operations

### Audit Requirements
- SLA documentation and contracts
- Availability reports and metrics
- Incident documentation
- Evidence of improvement measures

## Appendix

### Glossary

| Term | Definition |
|---|---|
| SLA | Service Level Agreement - Agreement on service levels |
| SLO | Service Level Objective - Internal service target |
| SLI | Service Level Indicator - Measurable metric |
| MTBF | Mean Time Between Failures - Average time between failures |
| MTTR | Mean Time To Repair - Average repair time |
| Error Budget | Tolerable downtime within the SLO period |
| Uptime | Available time of a system |
| Downtime | Outage time of a system |

### References
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework
- Site Reliability Engineering (Google)

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}

