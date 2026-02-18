
Document-ID: nist-csf-0030
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Risikomanagement-Strategie (GV.RM)

**Dokument-ID:** [FRAMEWORK]-0030
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

Dieses Dokument definiert die Cybersecurity-Risikomanagement-Strategie der Organisation, einschließlich Risikoappetit, Risikobewertungsmethodik und Risikobehandlungsansätze.

## Geltungsbereich

{{ meta-handbook.scope }}

## Risikomanagement-Rahmenwerk

### Risikomanagement-Ansatz
{{ meta-organisation.name }} verfolgt einen risikobasierten Ansatz für Cybersecurity, der:
- Geschäftsziele mit Sicherheitsanforderungen in Einklang bringt
- Kontinuierliche Risikobewertung und -überwachung ermöglicht
- Informierte Entscheidungsfindung unterstützt
- Ressourcen auf kritische Risiken fokussiert

### Risikomanagement-Prozess

1. **Risikoidentifikation**: Erkennung potenzieller Cybersecurity-Bedrohungen
2. **Risikobewertung**: Analyse von Wahrscheinlichkeit und Auswirkung
3. **Risikobehandlung**: Auswahl geeigneter Maßnahmen
4. **Risikoüberwachung**: Kontinuierliche Überprüfung und Anpassung

## Risikoappetit und -toleranz

### Risikoappetit-Erklärung
{{ meta-handbook.risk_appetite_statement }}

### Risikotoleranz-Niveaus

| Risikoniveau | Beschreibung | Maßnahmen |
|--------------|--------------|-----------|
| Kritisch | Existenzbedrohend | Sofortige Behandlung erforderlich |
| Hoch | Erhebliche Auswirkung | Behandlung innerhalb 30 Tagen |
| Mittel | Moderate Auswirkung | Behandlung innerhalb 90 Tagen |
| Niedrig | Geringe Auswirkung | Akzeptabel mit Überwachung |

## Risikobewertungsmethodik

### Bewertungskriterien

**Wahrscheinlichkeit:**
- Sehr hoch (5): > 80% Wahrscheinlichkeit
- Hoch (4): 60-80% Wahrscheinlichkeit
- Mittel (3): 40-60% Wahrscheinlichkeit
- Niedrig (2): 20-40% Wahrscheinlichkeit
- Sehr niedrig (1): < 20% Wahrscheinlichkeit

**Auswirkung:**
- Sehr hoch (5): > {{ meta-handbook.impact_threshold_critical }}
- Hoch (4): {{ meta-handbook.impact_threshold_high }}
- Mittel (3): {{ meta-handbook.impact_threshold_medium }}
- Niedrig (2): {{ meta-handbook.impact_threshold_low }}
- Sehr niedrig (1): < {{ meta-handbook.impact_threshold_minimal }}

### Risikomatrix

| Wahrscheinlichkeit | Sehr niedrig | Niedrig | Mittel | Hoch | Sehr hoch |
|-------------------|--------------|---------|--------|------|-----------|
| Sehr hoch (5) | Mittel | Hoch | Hoch | Kritisch | Kritisch |
| Hoch (4) | Niedrig | Mittel | Hoch | Hoch | Kritisch |
| Mittel (3) | Niedrig | Mittel | Mittel | Hoch | Hoch |
| Niedrig (2) | Sehr niedrig | Niedrig | Mittel | Mittel | Hoch |
| Sehr niedrig (1) | Sehr niedrig | Niedrig | Niedrig | Mittel | Mittel |

## Risikobehandlungsoptionen

### Behandlungsstrategien

1. **Vermeiden**: Aktivität einstellen, die das Risiko verursacht
2. **Reduzieren**: Kontrollen implementieren, um Risiko zu mindern
3. **Übertragen**: Risiko auf Dritte übertragen (z.B. Versicherung)
4. **Akzeptieren**: Risiko bewusst akzeptieren mit Begründung

### Entscheidungskriterien

| Risikoniveau | Bevorzugte Strategie | Genehmigung erforderlich |
|--------------|---------------------|-------------------------|
| Kritisch | Vermeiden oder Reduzieren | Vorstand |
| Hoch | Reduzieren | CISO |
| Mittel | Reduzieren oder Übertragen | Risikomanager |
| Niedrig | Akzeptieren mit Überwachung | Abteilungsleiter |

## Risikokommunikation

### Berichterstattung

| Zielgruppe | Häufigkeit | Inhalt |
|------------|-----------|--------|
| Vorstand | Quartalsweise | Risikoprofil, kritische Risiken, Trends |
| Geschäftsführung | Monatlich | Aktuelle Risiken, Behandlungsfortschritt |
| CISO | Wöchentlich | Detaillierte Risikoanalyse, Vorfälle |
| Risikomanager | Täglich | Neue Risiken, Statusänderungen |

## Integration mit Geschäftsrisikomanagement

### Abstimmung mit Enterprise Risk Management (ERM)
- Cybersecurity-Risiken werden in das ERM-Framework integriert
- Konsistente Risikobewertungsmethodik über alle Risikokategorien
- Gemeinsame Berichterstattung an Vorstand und Geschäftsführung

## Kontinuierliche Verbesserung

### Überprüfungszyklen
- Jährliche Überprüfung der Risikomanagement-Strategie
- Quartalsweise Aktualisierung der Risikobewertungen
- Monatliche Überprüfung kritischer Risiken

## Dokumentenverweise

- 0020_organizational_context.md
- 0040_roles_responsibilities.md
- 0100_asset_management.md (Identify)
- 0130_risk_assessment.md (Identify)

