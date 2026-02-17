
Document-ID: dora-0210

Status: Draft
Classification: Internal

# Lead Time Measurement

**Document-ID:** [FRAMEWORK]-0210
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

This document describes the practical implementation of Lead Time measurement, including data collection, calculation, and reporting.

## Scope

- Measurement methodology and data sources
- Automated collection
- Calculation logic
- Reporting and visualization

## Organization Information

- **Organization**: [TODO]
- **Measurement Owner**: [TODO]
- **Measurement System**: [TODO]

## Data Collection

### Start Time: Code Commit

**Git Integration**:
```bash
# Capture commit timestamp
git log --format="%H|%at|%an|%s" -1
```

**Metadata**:
- Commit SHA
- Commit timestamp
- Author
- Branch
- Commit message

### End Time: Production Deployment

**Deployment Event**:
```json
{
  "deployment_id": "12345",
  "timestamp": "2024-02-13T14:30:00Z",
  "commit_sha": "abc123",
  "environment": "production",
  "status": "success"
}
```

## Calculation Logic

### Basic Calculation

```
Lead Time = Deployment Timestamp - Commit Timestamp
```

### Advanced Metrics

**Average Lead Time**:
```
Avg Lead Time = Σ(Lead Times) / Number of Deployments
```

**Median Lead Time**:
- Sort all lead times
- Select middle value

**Percentiles**:
- P50: Median
- P90: 90% of deployments are faster
- P95: 95% of deployments are faster

## Reporting

### Dashboard Components

- Current lead time
- 30-day trend
- Performance level tracking
- Bottleneck analysis

### Visualizations

- Time series charts
- Histograms
- Heatmaps
- Trend lines

<!-- Note: Accurate measurement enables targeted optimization -->

