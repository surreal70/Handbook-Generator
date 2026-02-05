# Availability and Service Level

## Overview

This document defines availability requirements, Service Level Agreements (SLAs), and Service Level Objectives (SLOs) for the IT service. It describes measurement methods, reporting processes, and measures for continuous improvement of service availability.

**Document Owner:** IT Operations Manager  
**Approved by:** CIO  
**Version:** 1.0.0  
**Organization:** AdminSend GmbH

---

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
- **Emergency Maintenance:** After approval by Anna Schmidt

#### Business Services
- **Availability:** Mon-Fri 06:00-22:00
- **Support Hours:** Mon-Fri 08:00-18:00
- **Maintenance Window:** Saturday 20:00-24:00
- **Emergency Maintenance:** After approval by Andreas Huemmer

---

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

---

## Service Level Objectives (SLO)

### Internal SLOs

#### Infrastructure SLOs

| Component | SLO | Measurement Method | Responsible |
|---|---:|---|---|
| Compute Cluster | 99.9% | Hypervisor Monitoring | Andreas Huemmer |
| Storage System | 99.95% | Storage Monitoring | Andreas Huemmer |
| Network Core | 99.99% | Network Monitoring | Andreas Huemmer |
| Firewall | 99.95% | Security Monitoring | Thomas Weber |
| Load Balancer | 99.9% | LB Monitoring | Andreas Huemmer |

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

---

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

---

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
- **Recipients:** Andreas Huemmer
- **Content:**
  - Weekly availability
  - SLA compliance status
  - Trend analysis
  - Recommendations
- **Delivery:** Every Monday

#### Monthly SLA Report
- **Recipients:** Anna Schmidt, Stakeholders
- **Content:**
  - Monthly availability
  - SLA fulfillment vs. targets
  - Incident summary
  - Error Budget status
  - Improvement measures
- **Delivery:** First business day of following month

---

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

---

## Compliance and Standards

### Relevant Standards
- **ITIL v4:** Availability Management Practice
- **ISO 20000:** Clause 8.9 - Availability Management
- **COBIT 2019:** DSS01 - Managed Operations

---

**Last Update:** {{ meta.date }}  
**Next Review:** [TODO: Date]  
**Contact:** andreas.huemmer@adminsend.de
