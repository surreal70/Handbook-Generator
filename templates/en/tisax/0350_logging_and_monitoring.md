---
Document-ID: tisax-0350
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Logging and Monitoring

## Purpose

This document describes requirements for logging and monitoring according to TISAX requirements.

## Scope

This document applies to all IT systems of {{ source.organization_name }}.

## Logging

### Logged Events
**Security-relevant:**
- Logins (successful/failed)
- Permission changes
- Access to sensitive data
- Administrative actions
- Security incidents

**System-relevant:**
- System starts/stops
- Errors and warnings
- Configuration changes
- Performance data

### Log Management
- Central log collection
- Secure storage
- Protection against manipulation
- Retention: {{ source.log_retention_days }} days
- SIEM System: {{ source.siem_solution }}

## Monitoring

### Real-time Monitoring
**Monitored Systems:**
- Servers and infrastructure
- Network devices
- Applications
- Security systems

**Metrics:**
- Availability
- Performance
- Security events
- Capacity

### Alerting
**Thresholds:**
- Warning: Potential problems
- Critical: Immediate action required

**Escalation:**
- Automatic notification
- Escalation levels
- 24/7 availability for critical systems

## Log Analysis

### Regular Review
**Daily:**
- Security events
- Critical errors
- Anomalies

**Weekly:**
- Trend analyses
- Compliance checks
- Performance analyses

**Monthly:**
- Comprehensive evaluation
- Management reporting
- Improvement measures

## TISAX-Specific Requirements

### VDA ISA Controls
- **6.5**: Logging and monitoring

### Assessment Evidence
- Logging configuration
- SIEM reports
- Incident documentation

## Metrics

{{ source.organization_name }} measures:
- Number of logged events
- Number of security incidents
- Average response time to alarms

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
