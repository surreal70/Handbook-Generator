---
Document-ID: tisax-0040
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Risikomanagement

## Zweck

Dieses Dokument beschreibt den Risikomanagementprozess für Informationssicherheit bei {{ source.organization_name }}.

## Geltungsbereich

Dieser Prozess gilt für alle Informationssicherheitsrisiken innerhalb von {{ source.organization_name }}.

## Risikomanagementprozess

### Risikoidentifikation

**Methoden**:
- Asset-Inventarisierung
- Bedrohungsanalyse
- Schwachstellenanalyse
- Szenarioanalyse

**Häufigkeit**: {{ source.risk_assessment_frequency }}

### Risikobewertung

**Bewertungskriterien**:

| Wahrscheinlichkeit | Auswirkung | Risikostufe |
|-------------------|------------|-------------|
| Hoch | Hoch | Kritisch |
| Hoch | Mittel | Hoch |
| Mittel | Hoch | Hoch |
| Mittel | Mittel | Mittel |
| Niedrig | Niedrig | Niedrig |

**Risikomatrix**:

```
Auswirkung
    ^
  H | M  H  K
  M | L  M  H
  N | L  L  M
    +----------->
      N  M  H  Wahrscheinlichkeit
```

### Risikobehandlung

**Optionen**:
1. **Vermeiden**: Aktivität einstellen
2. **Reduzieren**: Maßnahmen implementieren
3. **Übertragen**: Versicherung, Outsourcing
4. **Akzeptieren**: Bewusste Risikoübernahme

### Risikoakzeptanz

**Akzeptanzkriterien**:
- Restrisiko unter {{ source.risk_acceptance_threshold }}
- Genehmigung durch {{ source.risk_acceptance_authority }}
- Dokumentation der Begründung

## Risikoregister

{{ source.organization_name }} führt ein Risikoregister mit folgenden Informationen:

- Risiko-ID
- Beschreibung
- Asset
- Bedrohung
- Schwachstelle
- Wahrscheinlichkeit
- Auswirkung
- Risikostufe
- Behandlungsmaßnahmen
- Verantwortlicher
- Status

## Überwachung und Überprüfung

**Aktivitäten**:
- Kontinuierliche Risikoüberwachung
- Regelmäßige Risikoüberprüfung: {{ source.risk_review_frequency }}
- Aktualisierung bei wesentlichen Änderungen
- Berichterstattung an das Management

<!-- Hinweis: Passen Sie die Risikobewertungskriterien an Ihre Organisation an -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
