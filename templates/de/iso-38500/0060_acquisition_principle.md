---
Document-ID: iso-38500-0060
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Prinzip 3: Beschaffung (Acquisition)

## Zweck

Dieses Dokument beschreibt die Anwendung des Beschaffungs-Prinzips in der IT-Governance der Organisation.

## Geltungsbereich

Dieses Dokument gilt für:
- {{ meta.organization }}
- Alle IT-Beschaffungen (Hardware, Software, Services)
- Beschaffungsprozesse und -entscheidungen

## Prinzip-Definition

IT-Beschaffungen werden aus gültigen Gründen getätigt, auf der Grundlage angemessener Analysen, mit klaren und transparenten Entscheidungen.

## Evaluate (Bewerten)

### Beschaffungsbedarf bewerten

- Ist die Beschaffung geschäftlich gerechtfertigt?
- Wurden Alternativen analysiert?
- Sind Kosten und Nutzen angemessen?
- Wurden Risiken bewertet?

### Bewertungskriterien

| Kriterium | Anforderung |
|-----------|-------------|
| Business Case | Erforderlich für Beschaffungen >{{ meta.business_case_threshold }} EUR |
| Kosten-Nutzen-Analyse | Erforderlich |
| Risikoanalyse | Erforderlich |
| Alternativenprüfung | Mindestens 3 Optionen |

## Direct (Steuern)

### Beschaffungsprozess

1. **Bedarfsermittlung**: Geschäftsbedarf identifizieren
2. **Business Case**: Rechtfertigung erstellen
3. **Marktanalyse**: Optionen evaluieren
4. **Bewertung**: Kosten, Nutzen, Risiken analysieren
5. **Genehmigung**: Entscheidung durch Governance-Gremium
6. **Beschaffung**: Durchführung
7. **Implementierung**: Umsetzung
8. **Review**: Nachbewertung

### Genehmigungsschwellen

| Beschaffungswert | Genehmigung durch |
|------------------|-------------------|
| < {{ meta.threshold_1 }} EUR | IT-Management |
| {{ meta.threshold_1 }} - {{ meta.threshold_2 }} EUR | CIO |
| {{ meta.threshold_2 }} - {{ meta.threshold_3 }} EUR | Geschäftsführung |
| > {{ meta.threshold_3 }} EUR | Vorstand |

### Beschaffungskriterien

- **Funktionalität**: Erfüllt Anforderungen
- **Kosten**: Total Cost of Ownership
- **Qualität**: Zuverlässigkeit und Leistung
- **Risiko**: Technische und geschäftliche Risiken
- **Compliance**: Regulatorische Anforderungen
- **Nachhaltigkeit**: Langfristige Tragfähigkeit

## Monitor (Überwachen)

### Überwachungsmaßnahmen

1. **Beschaffungs-Reviews**: Quartalsweise
2. **Nutzenrealisierung**: Nach Implementierung
3. **Lieferanten-Performance**: Kontinuierlich
4. **Lessons Learned**: Nach Projektabschluss

### KPIs

- Beschaffungen mit Business Case: {{ meta.acquisitions_with_bc }}%
- Durchschnittliche Beschaffungszeit: {{ meta.avg_acquisition_time }} Tage
- Nutzenrealisierung: {{ meta.benefit_realization }}%
- Lieferantenzufriedenheit: {{ meta.supplier_satisfaction }}/10

## Dokumentenverweise

- 0010_governance_framework.md
- 0020_governance_model.md

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |

