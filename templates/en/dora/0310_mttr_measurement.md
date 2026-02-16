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

Practical implementation of MTTR measurement.

## Scope

- Incident tracking
- Time capture
- Calculation logic
- Reporting

## Organization Information

- **Organization**: {{ source.organization_name }}
- **Measurement Owner**: {{ source.mttr_measurement_owner }}
- **Incident Management System**: {{ source.incident_management_system }}

## Incident Tracking

### Incident Lifecycle

1. **Detection**: Incident detected
2. **Acknowledgment**: Incident acknowledged
3. **Diagnosis**: Root cause identified
4. **Recovery**: Service restored
5. **Verification**: Restoration confirmed
6. **Closure**: Incident closed

### Timestamp Capture

```json
{
  "incident_id": "INC-12345",
  "detected_at": "2024-02-13T14:00:00Z",
  "acknowledged_at": "2024-02-13T14:05:00Z",
  "diagnosed_at": "2024-02-13T14:30:00Z",
  "recovered_at": "2024-02-13T15:00:00Z",
  "verified_at": "2024-02-13T15:15:00Z",
  "closed_at": "2024-02-13T15:30:00Z"
}
```

## Calculation Logic

### MTTR Calculation

```
MTTR = (recovered_at - detected_at)
```

### Average MTTR

```
Avg MTTR = Σ(MTTRs) / Number of Incidents
```

### Severity-specific MTTR

```
MTTR_Sev1 = Σ(MTTR Sev1 Incidents) / Number of Sev1 Incidents
```

## Reporting

### Dashboard Metrics

- Current MTTR
- MTTR trend (30/90 days)
- MTTR by severity
- MTTR by team/service

### Visualizations

- Time series charts
- Histograms
- Heatmaps

<!-- Note: Accurate measurement enables improvement -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |
