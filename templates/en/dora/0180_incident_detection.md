---
Document-ID: dora-0320
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Incident Detection

## Purpose

Description of incident detection mechanisms.

## Scope

- Detection methods
- Monitoring and alerting
- Escalation

## Detection Methods

### Automatic Detection

- **Monitoring System**: {{ source.monitoring_system }}
- **Alerting Tool**: {{ source.alerting_tool }}
- **Anomaly Detection**: {{ source.anomaly_detection }}

### Manual Detection

- User reports
- Support tickets
- Team observations

## Monitoring and Alerting

### Monitoring Coverage

- **Application Monitoring**: {{ source.app_monitoring_coverage }}
- **Infrastructure Monitoring**: {{ source.infra_monitoring_coverage }}
- **Business Metrics**: {{ source.business_metrics_monitoring }}

### Alert Configuration

- **Alert Thresholds**: {{ source.alert_thresholds }}
- **Alert Routing**: {{ source.alert_routing }}
- **On-Call Rotation**: {{ source.oncall_rotation }}

## Escalation

### Escalation Paths

1. **Level 1**: {{ source.escalation_level_1 }}
2. **Level 2**: {{ source.escalation_level_2 }}
3. **Level 3**: {{ source.escalation_level_3 }}

<!-- Note: Fast detection is prerequisite for low MTTR -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
