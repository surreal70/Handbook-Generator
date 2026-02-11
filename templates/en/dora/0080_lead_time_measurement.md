---
Document-ID: dora-0210
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Lead Time Measurement

## Purpose

Detailed measurement methodology for Lead Time for Changes.

## Scope

- Measurement procedures
- Data collection
- Calculation

## Measurement Procedures

### Timestamp Capture

- **Commit Time**: {{ source.commit_timestamp_source }}
- **Deploy Time**: {{ source.deploy_timestamp_source }}

### Calculation

```
Lead Time = Deploy Timestamp - Commit Timestamp
```

### Aggregation

- Median (preferred)
- 95th Percentile
- Average

## Data Collection

### Automation

- Git hooks for commit tracking
- CI/CD integration for deploy tracking
- Automatic correlation

### Data Quality

- **Completeness**: {{ source.lead_time_data_completeness }}
- **Accuracy**: {{ source.lead_time_data_accuracy }}

<!-- Note: Median is more robust against outliers than average -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
