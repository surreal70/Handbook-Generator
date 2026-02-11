---
Document-ID: dora-0110
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Deployment Frequency Messung

## Zweck

Dieses Dokument beschreibt die detaillierte Messmethodik für Deployment Frequency.

## Umfang

- Messverfahren
- Datenerfassung
- Berechnung
- Reporting

## Messverfahren

### Automatisierte Erfassung

**CI/CD-Integration**:
- Pipeline-Events tracken
- Deployment-Erfolg/-Fehler erfassen
- Zeitstempel dokumentieren

**Datenquellen**:
- **CI/CD**: {{ source.cicd_system }}
- **Deployment-Log**: {{ source.deployment_log_location }}
- **Monitoring**: {{ source.monitoring_dashboard }}

### Deployment-Definition

**Zählt als Deployment**:
- Erfolgreicher Production-Deploy
- Code-Änderung deployed
- Für End-User verfügbar

**Zählt NICHT als Deployment**:
- Rollbacks
- Hotfixes (separat gezählt)
- Staging/Test-Deployments

## Datenerfassung

### Erfasste Attribute

Für jedes Deployment:
- Timestamp
- Service/Application
- Team
- Commit-ID
- Deployment-Dauer
- Erfolg/Fehler

### Datenqualität

- **Vollständigkeit**: {{ source.data_completeness }}
- **Genauigkeit**: {{ source.data_accuracy }}
- **Aktualität**: {{ source.data_timeliness }}

## Berechnung

### Formel

```
Deployment Frequency = Anzahl erfolgreicher Deployments / Zeitperiode
```

### Aggregation

- **Pro Service**: Individuelle Service-Frequenz
- **Pro Team**: Team-Durchschnitt
- **Organisation**: Gesamtdurchschnitt

### Beispielberechnung

**Service A**:
- Deployments in 30 Tagen: {{ source.service_a_deployments }}
- Deployment Frequency: {{ source.service_a_frequency }}

## Reporting

### Dashboards

- **Real-time Dashboard**: {{ source.realtime_dashboard_url }}
- **Wöchentlicher Report**: {{ source.weekly_report_location }}
- **Monatlicher Report**: {{ source.monthly_report_location }}

### Visualisierungen

- Trend-Charts
- Team-Vergleiche
- Service-Heatmaps

<!-- Hinweis: Automatisierung der Datenerfassung ist kritisch -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
