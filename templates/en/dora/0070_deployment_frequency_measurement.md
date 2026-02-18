
Document-ID: dora-0110

Status: Draft
Classification: Internal

# Deployment Frequency Measurement

**Document-ID:** [FRAMEWORK]-0070
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
- **CI/CD**: [TODO]
- **Deployment Log**: [TODO]
- **Monitoring**: [TODO]

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

- **Completeness**: [TODO]
- **Accuracy**: [TODO]
- **Timeliness**: [TODO]

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
- Deployments in 30 days: [TODO]
- Deployment Frequency: [TODO]

## Reporting

### Dashboards

- **Real-time Dashboard**: [TODO]
- **Weekly Report**: [TODO]
- **Monthly Report**: [TODO]

### Visualizations

- Trend charts
- Team comparisons
- Service heatmaps

<!-- Note: Automation of data collection is critical -->

<!-- End of template -->
