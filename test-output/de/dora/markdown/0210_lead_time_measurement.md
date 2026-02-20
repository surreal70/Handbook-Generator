
Document-ID: dora-0210

Status: Draft
Classification: Internal

# Lead Time Messung

**Dokument-ID:** [FRAMEWORK]-0210
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---

## Zweck

Dieses Dokument beschreibt die praktische Implementierung der Lead Time Messung, einschließlich Datenerfassung, Berechnung und Reporting.

## Umfang

- Messmethodik und Datenquellen
- Automatisierte Erfassung
- Berechnungslogik
- Reporting und Visualisierung

## Organisationsinformationen

- **Organisation**: [TODO]
- **Messverantwortlicher**: [TODO]
- **Messsystem**: [TODO]

## Datenerfassung

### Start-Zeitpunkt: Code-Commit

**Git-Integration**:
```bash
# Commit-Timestamp erfassen
git log --format="%H|%at|%an|%s" -1
```

**Metadaten**:
- Commit-SHA
- Commit-Timestamp
- Autor
- Branch
- Commit-Message

### End-Zeitpunkt: Production-Deployment

**Deployment-Event**:
```json
{
  "deployment_id": "12345",
  "timestamp": "2024-02-13T14:30:00Z",
  "commit_sha": "abc123",
  "environment": "production",
  "status": "success"
}
```

## Berechnungslogik

### Grundlegende Berechnung

```
Lead Time = Deployment-Timestamp - Commit-Timestamp
```

### Erweiterte Metriken

**Durchschnittliche Lead Time**:
```
Avg Lead Time = Σ(Lead Times) / Anzahl Deployments
```

**Median Lead Time**:
- Sortiere alle Lead Times
- Wähle mittleren Wert

**Perzentile**:
- P50: Median
- P90: 90% der Deployments sind schneller
- P95: 95% der Deployments sind schneller

## Reporting

### Dashboard-Komponenten

- Aktuelle Lead Time
- 30-Tage-Trend
- Performance-Level-Tracking
- Bottleneck-Analyse

### Visualisierungen

- Zeitreihen-Diagramme
- Histogramme
- Heatmaps
- Trend-Linien



