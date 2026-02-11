---
Document-ID: dora-0310
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# MTTR Measurement

## Purpose

Detailed measurement methodology for Mean Time to Restore.

## Scope

- Measurement procedures
- Data collection
- Calculation

## Measurement Procedures

### Timestamp Capture

- **Incident Start**: {{ source.incident_start_definition }}
- **Incident End**: {{ source.incident_end_definition }}

### Calculation

```
MTTR = Sum of all restoration times / Number of incidents
```

### Aggregation

- Median (preferred)
- 95th Percentile
- Average

## Data Collection

### Incident Tracking

- Automatic incident detection
- Manual incident reporting
- Restoration confirmation

### Data Quality

- **Completeness**: {{ source.mttr_data_completeness }}
- **Accuracy**: {{ source.mttr_data_accuracy }}

<!-- Note: Precise time tracking is critical for MTTR measurement -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
