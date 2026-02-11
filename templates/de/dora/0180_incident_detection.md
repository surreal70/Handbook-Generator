---
Document-ID: dora-0320
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Incident-Erkennung

## Zweck

Beschreibung der Incident-Erkennungsmechanismen.

## Umfang

- Erkennungsmethoden
- Monitoring und Alerting
- Eskalation

## Erkennungsmethoden

### Automatische Erkennung

- **Monitoring-System**: {{ source.monitoring_system }}
- **Alerting-Tool**: {{ source.alerting_tool }}
- **Anomalie-Erkennung**: {{ source.anomaly_detection }}

### Manuelle Erkennung

- User-Reports
- Support-Tickets
- Team-Beobachtungen

## Monitoring und Alerting

### Monitoring-Coverage

- **Application Monitoring**: {{ source.app_monitoring_coverage }}
- **Infrastructure Monitoring**: {{ source.infra_monitoring_coverage }}
- **Business Metrics**: {{ source.business_metrics_monitoring }}

### Alert-Konfiguration

- **Alert-Schwellwerte**: {{ source.alert_thresholds }}
- **Alert-Routing**: {{ source.alert_routing }}
- **On-Call-Rotation**: {{ source.oncall_rotation }}

## Eskalation

### Eskalationspfade

1. **Level 1**: {{ source.escalation_level_1 }}
2. **Level 2**: {{ source.escalation_level_2 }}
3. **Level 3**: {{ source.escalation_level_3 }}

<!-- Hinweis: Schnelle Erkennung ist Voraussetzung für niedrige MTTR -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
