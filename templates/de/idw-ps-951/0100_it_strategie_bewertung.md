# IT-Strategie Bewertung

**Dokument-ID:** idw-ps-951-0100  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument beschreibt die Prüfung der IT-Strategie im Rahmen der IT-Prüfung nach IDW PS 951. Es bewertet die Ausrichtung der IT-Strategie an den Unternehmenszielen und die strategische IT-Planung.

## 2. Prüfungsgegenstand

### IT-Strategie
- **Strategiedokument:** {{ source.strategy_document }}
- **Gültigkeitszeitraum:** {{ source.strategy_period }}
- **Verantwortlich:** {{ source.strategy_owner }}
- **Letzte Aktualisierung:** {{ source.strategy_last_update }}

### Prüfungsziele
- Bewertung der Ausrichtung der IT-Strategie an Unternehmenszielen
- Prüfung der strategischen IT-Planung
- Beurteilung der IT-Governance-Struktur
- Bewertung der IT-Investitionsplanung

## 3. Prüfungshandlungen

### Dokumentenprüfung
- [ ] IT-Strategiedokument vorhanden und aktuell
- [ ] Abstimmung mit Unternehmensstrategie dokumentiert
- [ ] IT-Ziele definiert und messbar
- [ ] Strategische Initiativen priorisiert
- [ ] Ressourcenplanung vorhanden

### Interviews
- **CIO/IT-Leitung:** {{ source.cio_interview }}
- **Geschäftsführung:** {{ source.management_interview }}
- **IT-Strategie-Verantwortliche:** {{ source.strategy_responsible_interview }}

### Analytische Prüfungshandlungen
- Vergleich IT-Strategie mit Branchenstandards
- Bewertung der strategischen Ausrichtung
- Analyse der IT-Investitionen

## 4. Prüfungskriterien

### Strategische Ausrichtung
| Kriterium | Anforderung | Ist-Zustand | Bewertung |
|-----------|-------------|-------------|-----------|
| Abstimmung mit Unternehmensstrategie | Dokumentiert | {{ source.alignment_status }} | {{ source.alignment_assessment }} |
| IT-Ziele definiert | Messbar und terminiert | {{ source.objectives_status }} | {{ source.objectives_assessment }} |
| Stakeholder-Einbindung | Regelmäßig | {{ source.stakeholder_status }} | {{ source.stakeholder_assessment }} |
| Strategieüberprüfung | Jährlich | {{ source.review_status }} | {{ source.review_assessment }} |

### IT-Governance
- **Governance-Struktur:** {{ source.governance_structure }}
- **Entscheidungsgremien:** {{ source.decision_bodies }}
- **Eskalationsprozesse:** {{ source.escalation_processes }}

## 5. Feststellungen

### Positive Feststellungen
1. {{ source.positive_finding_1 }}
2. {{ source.positive_finding_2 }}

### Verbesserungspotenziale
1. {{ source.improvement_1 }}
2. {{ source.improvement_2 }}

### Kritische Feststellungen
1. {{ source.critical_finding_1 }}
2. {{ source.critical_finding_2 }}

## 6. Risikobewertung

### Identifizierte Risiken
| Risiko | Beschreibung | Auswirkung | Wahrscheinlichkeit | Risikostufe |
|--------|--------------|------------|-------------------|-------------|
| {{ source.risk_1_id }} | {{ source.risk_1_desc }} | {{ source.risk_1_impact }} | {{ source.risk_1_likelihood }} | {{ source.risk_1_level }} |

### Kontrollbewertung
- **Kontrolldesign:** {{ source.control_design }}
- **Kontrollwirksamkeit:** {{ source.control_effectiveness }}

## 7. Empfehlungen

### Kurzfristige Maßnahmen (0-3 Monate)
1. {{ source.short_term_recommendation_1 }}
2. {{ source.short_term_recommendation_2 }}

### Mittelfristige Maßnahmen (3-12 Monate)
1. {{ source.medium_term_recommendation_1 }}
2. {{ source.medium_term_recommendation_2 }}

### Langfristige Maßnahmen (> 12 Monate)
1. {{ source.long_term_recommendation_1 }}

## 8. Nachweise

### Geprüfte Dokumente
- IT-Strategiedokument
- Unternehmensstrategie
- IT-Governance-Richtlinien
- Sitzungsprotokolle IT-Steuerungsgremium
- IT-Investitionsplanung

### Interviews
- {{ source.interview_list }}

## 9. Referenzen

- IDW PS 951 - IT-Strategie und IT-Organisation
- COBIT 2019 - Governance Framework
- ISO/IEC 38500 - IT Governance

---

**Genehmigt durch:**  
{{ meta.audit_lead }}, Prüfungsleiter  
Datum: {{ meta.approval_date }}

**Nächster Review:** {{ meta.next_review }}

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |
