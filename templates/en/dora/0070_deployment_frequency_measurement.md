---
Document-ID: dora-0110
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Deployment Frequency Measurement

## Purpose

This document describes the detailed measurement methodology for Deployment Frequency.

## Scope

- Measurement procedures
- Data collection
- Calculation
- Reporting

## Measurement Procedures

### Automated Collection

**CI/CD Integration**:
- Track pipeline events
- Capture deployment success/failure
- Document timestamps

**Data Sources**:
- **CI/CD**: {{ source.cicd_system }}
- **Deployment Log**: {{ source.deployment_log_location }}
- **Monitoring**: {{ source.monitoring_dashboard }}

### Deployment Definition

**Counts as Deployment**:
- Successful production deploy
- Code change deployed
- Available to end users

**Does NOT count as Deployment**:
- Rollbacks
- Hotfixes (counted separately)
- Staging/Test deployments

## Data Collection

### Captured Attributes

For each deployment:
- Timestamp
- Service/Application
- Team
- Commit ID
- Deployment duration
- Success/Failure

### Data Quality

- **Completeness**: {{ source.data_completeness }}
- **Accuracy**: {{ source.data_accuracy }}
- **Timeliness**: {{ source.data_timeliness }}

## Calculation

### Formula

```
Deployment Frequency = Number of successful deployments / Time period
```

### Aggregation

- **Per Service**: Individual service frequency
- **Per Team**: Team average
- **Organization**: Overall average

### Example Calculation

**Service A**:
- Deployments in 30 days: {{ source.service_a_deployments }}
- Deployment Frequency: {{ source.service_a_frequency }}

## Reporting

### Dashboards

- **Real-time Dashboard**: {{ source.realtime_dashboard_url }}
- **Weekly Report**: {{ source.weekly_report_location }}
- **Monthly Report**: {{ source.monthly_report_location }}

### Visualizations

- Trend charts
- Team comparisons
- Service heatmaps

<!-- Note: Automation of data collection is critical -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
