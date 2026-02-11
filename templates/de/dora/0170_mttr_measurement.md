---
Document-ID: dora-0310
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# MTTR Messung

## Zweck

Detaillierte Messmethodik für Mean Time to Restore.

## Umfang

- Messverfahren
- Datenerfassung
- Berechnung

## Messverfahren

### Zeitstempel-Erfassung

- **Incident-Start**: {{ source.incident_start_definition }}
- **Incident-Ende**: {{ source.incident_end_definition }}

### Berechnung

```
MTTR = Summe aller Wiederherstellungszeiten / Anzahl Incidents
```

### Aggregation

- Median (bevorzugt)
- 95th Percentile
- Durchschnitt

## Datenerfassung

### Incident-Tracking

- Automatische Incident-Erkennung
- Manuelle Incident-Meldung
- Wiederherstellungs-Bestätigung

### Datenqualität

- **Vollständigkeit**: {{ source.mttr_data_completeness }}
- **Genauigkeit**: {{ source.mttr_data_accuracy }}

<!-- Hinweis: Präzise Zeiterfassung ist kritisch für MTTR-Messung -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
