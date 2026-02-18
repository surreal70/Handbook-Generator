
Document-ID: dora-0410

Status: Draft
Classification: Internal

# CFR Measurement

**Document-ID:** [FRAMEWORK]-0410
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

Practical implementation of Change Failure Rate measurement.

## Scope

- Deployment tracking
- Failure definition
- Calculation logic
- Reporting

## Organization Information

- **Organization**: [TODO]
- **Measurement Owner**: [TODO]

## Deployment Tracking

### Deployment Events

```json
{
  "deployment_id": "DEP-12345",
  "timestamp": "2024-02-13T14:00:00Z",
  "commit_sha": "abc123",
  "environment": "production",
  "status": "success",
  "application": "[TODO]"
}
```

### Failure Events

```json
{
  "incident_id": "INC-67890",
  "timestamp": "2024-02-13T15:00:00Z",
  "related_deployment": "DEP-12345",
  "failure_type": "rollback",
  "severity": "high"
}
```

## Failure Definition

### Criteria for Failed Deployment

**Automatic Criteria**:
- Rollback performed
- Hotfix deployed
- Error rate > threshold
- Performance degradation

**Manual Criteria**:
- Production incident
- Customer impact
- Service degradation

## Calculation Logic

### CFR Calculation

```
CFR = (Failed Deployments / Total Deployments) × 100%
```

### Time Windows

- Daily CFR
- Weekly CFR
- Monthly CFR
- Rolling 30-day CFR

### Segmentation

- CFR by team
- CFR by service
- CFR by environment
- CFR by severity

## Reporting

### Dashboard Metrics

- Current CFR
- CFR trend
- Failed deployments
- Failure types

### Visualizations

- Time series charts
- Pie charts (failure types)
- Heatmaps

<!-- Note: Accurate measurement enables quality improvement -->

