
Document-ID: dora-0310

Status: Draft
Classification: Internal

# MTTR Messung

**Dokument-ID:** [FRAMEWORK]-0170
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

Detaillierte Messmethodik für Mean Time to Restore.

## Umfang

- Messverfahren
- Datenerfassung
- Berechnung

## Messverfahren

### Zeitstempel-Erfassung

- **Incident-Start**: [TODO]
- **Incident-Ende**: [TODO]

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

- **Vollständigkeit**: [TODO]
- **Genauigkeit**: [TODO]

<!-- Hinweis: Präzise Zeiterfassung ist kritisch für MTTR-Messung -->

