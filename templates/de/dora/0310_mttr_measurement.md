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

Praktische Implementierung der MTTR-Messung.

## Umfang

- Incident-Tracking
- Zeiterfassung
- Berechnungslogik
- Reporting

## Organisationsinformationen

- **Organisation**: {{ source.organization_name }}
- **Messverantwortlicher**: {{ source.mttr_measurement_owner }}
- **Incident-Management-System**: {{ source.incident_management_system }}

## Incident-Tracking

### Incident-Lifecycle

1. **Detection**: Incident erkannt
2. **Acknowledgment**: Incident bestätigt
3. **Diagnosis**: Root Cause identifiziert
4. **Recovery**: Service wiederhergestellt
5. **Verification**: Wiederherstellung bestätigt
6. **Closure**: Incident geschlossen

### Zeitstempel-Erfassung

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

## Berechnungslogik

### MTTR-Berechnung

```
MTTR = (recovered_at - detected_at)
```

### Durchschnittliche MTTR

```
Avg MTTR = Σ(MTTRs) / Anzahl Incidents
```

### Severity-spezifische MTTR

```
MTTR_Sev1 = Σ(MTTR Sev1 Incidents) / Anzahl Sev1 Incidents
```

## Reporting

### Dashboard-Metriken

- Aktuelle MTTR
- MTTR-Trend (30/90 Tage)
- MTTR nach Severity
- MTTR nach Team/Service

### Visualisierungen

- Zeitreihen-Diagramme
- Histogramme
- Heatmaps

<!-- Hinweis: Genaue Messung ermöglicht Verbesserung -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |
