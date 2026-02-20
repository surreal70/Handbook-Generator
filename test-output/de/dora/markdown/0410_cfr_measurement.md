
Document-ID: dora-0410

Status: Draft
Classification: Internal

# CFR Messung

**Dokument-ID:** DORA-0410
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

Praktische Implementierung der Change Failure Rate Messung.

## Umfang

- Deployment-Tracking
- Failure-Definition
- Berechnungslogik
- Reporting

## Organisationsinformationen

- **Organisation**: [TODO]
- **Messverantwortlicher**: [TODO]

## Deployment-Tracking

### Deployment-Events

```json
{
  "deployment_id": "DEP-12345",
  "timestamp": "2024-02-13T14:00:00Z",
  "commit_sha": "abc123",
  "environment": "production",
  "status": "success",
  "application": "[TODO]"
}
```

### Failure-Events

```json
{
  "incident_id": "INC-67890",
  "timestamp": "2024-02-13T15:00:00Z",
  "related_deployment": "DEP-12345",
  "failure_type": "rollback",
  "severity": "high"
}
```

## Failure-Definition

### Kriterien für Failed Deployment

**Automatische Kriterien**:
- Rollback durchgeführt
- Hotfix deployed
- Error Rate > Threshold
- Performance Degradation

**Manuelle Kriterien**:
- Production Incident
- Customer Impact
- Service Degradation

## Berechnungslogik

### CFR-Berechnung

```
CFR = (Failed Deployments / Total Deployments) × 100%
```

### Zeitfenster

- Tägliche CFR
- Wöchentliche CFR
- Monatliche CFR
- Rollende 30-Tage CFR

### Segmentierung

- CFR nach Team
- CFR nach Service
- CFR nach Environment
- CFR nach Severity

## Reporting

### Dashboard-Metriken

- Aktuelle CFR
- CFR-Trend
- Failed Deployments
- Failure Types

### Visualisierungen

- Zeitreihen-Diagramme
- Pie Charts (Failure Types)
- Heatmaps



