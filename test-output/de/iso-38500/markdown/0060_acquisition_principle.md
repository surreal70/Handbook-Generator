
Document-ID: iso-38500-0060
Owner: [TODO]

Status: Draft
Classification: Internal

# Prinzip 3: Beschaffung (Acquisition)

**Dokument-ID:** [FRAMEWORK]-0060
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

Dieses Dokument beschreibt die Anwendung des Beschaffungs-Prinzips in der IT-Governance der Organisation.

## Geltungsbereich

Dieses Dokument gilt für:
- AdminSend GmbH
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
| Business Case | Erforderlich für Beschaffungen >{{ meta-handbook.business_case_threshold }} EUR |
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
| < {{ meta-handbook.threshold_1 }} EUR | IT-Management |
| {{ meta-handbook.threshold_1 }} - {{ meta-handbook.threshold_2 }} EUR | CIO |
| {{ meta-handbook.threshold_2 }} - {{ meta-handbook.threshold_3 }} EUR | Geschäftsführung |
| > {{ meta-handbook.threshold_3 }} EUR | Vorstand |

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

- Beschaffungen mit Business Case: {{ meta-handbook.acquisitions_with_bc }}%
- Durchschnittliche Beschaffungszeit: {{ meta-handbook.avg_acquisition_time }} Tage
- Nutzenrealisierung: {{ meta-handbook.benefit_realization }}%
- Lieferantenzufriedenheit: {{ meta-handbook.supplier_satisfaction }}/10

## Dokumentenverweise

- 0010_governance_framework.md
- 0020_governance_model.md

