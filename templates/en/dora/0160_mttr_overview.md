---
Document-ID: dora-0300
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Mean Time to Restore (MTTR) Overview

## Purpose

Description of the MTTR metric and its significance for service stability.

## Scope

- MTTR definition
- Measurement methodology
- Current performance
- Improvement approaches

## Definition

MTTR measures the average time to restore service after an incident or outage.

### Organization Context

- **Organization**: {{ source.organization_name }}
- **Current MTTR**: {{ source.current_mttr }}
- **Performance Level**: {{ source.mttr_level }}

## Measurement Methodology

### Incident Definition

An incident is:
- Service degradation
- Service outage
- Critical error in production

### Time Tracking

- **Start**: Incident detection
- **End**: Service fully restored

### Data Sources

- **Incident Management**: {{ source.incident_management_system }}
- **Monitoring**: {{ source.monitoring_system }}
- **Alerting**: {{ source.alerting_system }}

## Current Performance

### Overall Organization

- **Median MTTR**: {{ source.median_mttr }}
- **95th Percentile**: {{ source.p95_mttr }}
- **Performance Level**: {{ source.mttr_performance_level }}

### By Service

| Service | Median MTTR | Performance Level |
|---------|-------------|-------------------|
| {{ source.service_1_name }} | {{ source.service_1_mttr }} | {{ source.service_1_mttr_level }} |
| {{ source.service_2_name }} | {{ source.service_2_mttr }} | {{ source.service_2_mttr_level }} |
| {{ source.service_3_name }} | {{ source.service_3_mttr }} | {{ source.service_3_mttr_level }} |

## Improvement Approaches

### Short-term

1. {{ source.mttr_short_term_1 }}
2. {{ source.mttr_short_term_2 }}

### Long-term

1. {{ source.mttr_long_term_1 }}
2. {{ source.mttr_long_term_2 }}

<!-- Note: MTTR is indicator of resilience and recovery capability -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
