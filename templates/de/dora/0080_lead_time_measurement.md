---
Document-ID: dora-0210
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Lead Time Messung

## Zweck

Detaillierte Messmethodik für Lead Time for Changes.

## Umfang

- Messverfahren
- Datenerfassung
- Berechnung

## Messverfahren

### Zeitstempel-Erfassung

- **Commit-Zeit**: {{ source.commit_timestamp_source }}
- **Deploy-Zeit**: {{ source.deploy_timestamp_source }}

### Berechnung

```
Lead Time = Deploy-Timestamp - Commit-Timestamp
```

### Aggregation

- Median (bevorzugt)
- 95th Percentile
- Durchschnitt

## Datenerfassung

### Automatisierung

- Git-Hooks für Commit-Tracking
- CI/CD-Integration für Deploy-Tracking
- Automatische Korrelation

### Datenqualität

- **Vollständigkeit**: {{ source.lead_time_data_completeness }}
- **Genauigkeit**: {{ source.lead_time_data_accuracy }}

<!-- Hinweis: Median ist robuster gegen Ausreißer als Durchschnitt -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
