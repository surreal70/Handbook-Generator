
Document-ID: dora-0210

Status: Draft
Classification: Internal

# Lead Time Messung

**Dokument-ID:** [FRAMEWORK]-0080
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Zweck

Detaillierte Messmethodik für Lead Time for Changes.

## Umfang

- Messverfahren
- Datenerfassung
- Berechnung

## Messverfahren

### Zeitstempel-Erfassung

- **Commit-Zeit**: [TODO]
- **Deploy-Zeit**: [TODO]

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

- **Vollständigkeit**: [TODO]
- **Genauigkeit**: [TODO]

<!-- Hinweis: Median ist robuster gegen Ausreißer als Durchschnitt -->

