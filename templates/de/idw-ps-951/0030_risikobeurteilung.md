# Risikobeurteilung und Risikoanalyse

**Dokument-ID:** idw-ps-951-0030  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument beschreibt die Risikobeurteilung im Rahmen der IT-Prüfung nach IDW PS 951. Es identifiziert und bewertet IT-Risiken, die die Ordnungsmäßigkeit der Rechnungslegung beeinflussen können.

## 2. Risikoanalysemethodik

### Ansatz
- **Methodik:** {{ source.risk_methodology }}
- **Bewertungsskala:** {{ source.risk_scale }}
- **Risikokategorien:** Inhärentes Risiko, Kontrollrisiko, Entdeckungsrisiko

### Risikobewertungskriterien

#### Eintrittswahrscheinlichkeit
- **Hoch:** Sehr wahrscheinlich (> 50%)
- **Mittel:** Möglich (10-50%)
- **Niedrig:** Unwahrscheinlich (< 10%)

#### Auswirkung
- **Hoch:** Wesentliche Auswirkung auf Rechnungslegung
- **Mittel:** Moderate Auswirkung
- **Niedrig:** Geringe Auswirkung

## 3. Identifizierte IT-Risiken

### Risikoregister

| Risiko-ID | Risikobeschreibung | Kategorie | Wahrscheinlichkeit | Auswirkung | Risikostufe |
|-----------|-------------------|-----------|-------------------|------------|-------------|
| R-001 | {{ source.risk_1_desc }} | {{ source.risk_1_category }} | {{ source.risk_1_likelihood }} | {{ source.risk_1_impact }} | {{ source.risk_1_level }} |
| R-002 | {{ source.risk_2_desc }} | {{ source.risk_2_category }} | {{ source.risk_2_likelihood }} | {{ source.risk_2_impact }} | {{ source.risk_2_level }} |
| R-003 | {{ source.risk_3_desc }} | {{ source.risk_3_category }} | {{ source.risk_3_likelihood }} | {{ source.risk_3_impact }} | {{ source.risk_3_level }} |

### Risikokategorien

#### IT-Governance-Risiken
- Unzureichende IT-Strategie
- Fehlende IT-Governance-Strukturen
- Unklare Verantwortlichkeiten

#### IT-Prozessrisiken
- Unzureichendes Change Management
- Schwaches Incident Management
- Fehlende Prozessdokumentation

#### IT-Systemrisiken
- Systemausfälle
- Datenintegritätsprobleme
- Schnittstellenfehler

#### IT-Sicherheitsrisiken
- Unberechtigte Zugriffe
- Datenverlust
- Cyberangriffe
- Schwachstellen

#### Compliance-Risiken
- Verstöße gegen Datenschutz
- Nichteinhaltung regulatorischer Anforderungen
- Fehlende Nachweise

## 4. Risikobewertung nach Prüfungsbereich

### IT-Strategie und Organisation
- **Inhärentes Risiko:** {{ source.strategy_inherent_risk }}
- **Kontrollrisiko:** {{ source.strategy_control_risk }}
- **Prüfungsrisiko:** {{ source.strategy_audit_risk }}

### IT-Prozesse
- **Inhärentes Risiko:** {{ source.process_inherent_risk }}
- **Kontrollrisiko:** {{ source.process_control_risk }}
- **Prüfungsrisiko:** {{ source.process_audit_risk }}

### IT-Systeme
- **Inhärentes Risiko:** {{ source.systems_inherent_risk }}
- **Kontrollrisiko:** {{ source.systems_control_risk }}
- **Prüfungsrisiko:** {{ source.systems_audit_risk }}

### IT-Sicherheit
- **Inhärentes Risiko:** {{ source.security_inherent_risk }}
- **Kontrollrisiko:** {{ source.security_control_risk }}
- **Prüfungsrisiko:** {{ source.security_audit_risk }}

## 5. Risikobasierte Prüfungsstrategie

### Prüfungsschwerpunkte
Basierend auf der Risikoanalyse werden folgende Bereiche priorisiert:

1. **Hohe Priorität:**
   - {{ source.high_priority_area_1 }}
   - {{ source.high_priority_area_2 }}

2. **Mittlere Priorität:**
   - {{ source.medium_priority_area_1 }}
   - {{ source.medium_priority_area_2 }}

3. **Niedrige Priorität:**
   - {{ source.low_priority_area_1 }}

### Prüfungshandlungen nach Risiko

#### Hochrisikobereiche
- Detaillierte Kontrolltests
- Umfangreiche Stichproben
- Intensive Dokumentenprüfung
- Interviews mit Schlüsselpersonen

#### Mittelrisikobereiche
- Standardkontrolltests
- Repräsentative Stichproben
- Dokumentenprüfung

#### Niedrigrisikobereiche
- Überblicksprüfung
- Analytische Prüfungshandlungen
- Befragungen

## 6. Risikomatrix

### Risikobewertungsmatrix

|                | Niedrige Auswirkung | Mittlere Auswirkung | Hohe Auswirkung |
|----------------|---------------------|---------------------|-----------------|
| **Hoch**       | Mittel              | Hoch                | Kritisch        |
| **Mittel**     | Niedrig             | Mittel              | Hoch            |
| **Niedrig**    | Niedrig             | Niedrig             | Mittel          |

### Risikobehandlung nach Stufe
- **Kritisch:** Sofortige Prüfungshandlungen, detaillierte Tests
- **Hoch:** Prioritäre Prüfung, umfangreiche Tests
- **Mittel:** Standardprüfung
- **Niedrig:** Überblicksprüfung

## 7. Risikokommunikation

### Berichterstattung
- **An Management:** {{ source.management_reporting }}
- **An Prüfungsausschuss:** {{ source.audit_committee_reporting }}
- **Frequenz:** {{ source.reporting_frequency }}

### Eskalation
Kritische Risiken werden sofort eskaliert an:
- {{ source.escalation_contact_1 }}
- {{ source.escalation_contact_2 }}

## 8. Risikoüberwachung

### Monitoring
- Kontinuierliche Überwachung während der Prüfung
- Anpassung der Prüfungsstrategie bei neuen Erkenntnissen
- Dokumentation von Risikoänderungen

### Aktualisierung
Das Risikoregister wird aktualisiert bei:
- Neuen Erkenntnissen
- Änderungen im IT-Umfeld
- Identifikation neuer Risiken

## 9. Referenzen

- IDW PS 951 - Risikobeurteilung
- IDW PS 340 - Risikofrüherkennungssystem
- Organisationsspezifisches Risikoregister
- Vorjahresprüfungsberichte

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
