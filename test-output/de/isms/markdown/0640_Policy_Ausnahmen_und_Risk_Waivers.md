# Policy: Ausnahmen und Risk Waivers

**Dokument-ID:** 0640
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



## 1. Zweck

Diese Policy definiert den Prozess für Ausnahmen (Exceptions) und Risk Waivers von Sicherheitsrichtlinien der **AdminSend GmbH**. Sie stellt sicher, dass Ausnahmen angemessen begründet, genehmigt, dokumentiert und überwacht werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Policies:** Alle Sicherheitsrichtlinien und -standards
- **Systeme:** Alle IT-Systeme und Anwendungen
- **Prozesse:** Alle sicherheitsrelevanten Prozesse
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Diese Policy selbst unterliegt keinem Ausnahmenprozess.

## 3. Grundsätze (Policy Statements)

### 3.1 Ausnahmen als Ausnahme
Ausnahmen von Sicherheitsrichtlinien sind die Ausnahme, nicht die Regel. Richtlinien sind grundsätzlich einzuhalten.

### 3.2 Formaler Ausnahmenprozess
Ausnahmen müssen über einen formalen Prozess beantragt werden. Informelle oder mündliche Ausnahmen sind nicht zulässig.

### 3.3 Begründungspflicht
Jede Ausnahme muss begründet werden:
- Geschäftliche Notwendigkeit
- Technische Unmöglichkeit
- Unverhältnismäßiger Aufwand
- Zeitliche Befristung

### 3.4 Risikobewertung
Für jede Ausnahme wird eine Risikobewertung durchgeführt. Risiken werden identifiziert, bewertet und dokumentiert.

### 3.5 Kompensationsmaßnahmen
Ausnahmen erfordern Kompensationsmaßnahmen. Kompensationsmaßnahmen reduzieren das Restrisiko auf ein akzeptables Niveau.

### 3.6 Genehmigungspflicht
Ausnahmen müssen von autorisierten Personen genehmigt werden:
- **Low Risk:** CISO oder Stellvertreter
- **Medium Risk:** CISO + Business Owner
- **High Risk:** CISO + CIO + Management

### 3.7 Zeitliche Befristung
Ausnahmen sind grundsätzlich zeitlich befristet. Maximale Laufzeit: 12 Monate. Verlängerungen erfordern erneute Genehmigung.

### 3.8 Dokumentation
Alle Ausnahmen werden zentral dokumentiert (Ausnahmenregister). Dokumentation umfasst:
- Antragsteller und Datum
- Betroffene Policy/Standard
- Begründung
- Risikobewertung
- Kompensationsmaßnahmen
- Genehmiger und Datum
- Laufzeit und Review-Datum

### 3.9 Monitoring und Review
Ausnahmen werden regelmäßig überprüft (mindestens quartalsweise). Nicht mehr benötigte Ausnahmen werden zurückgezogen.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Ausnahmen und Risk Waivers

| Aktivität | CISO | CIO | Business Owner | Risk Manager | ISMS Team |
|-----------|------|-----|----------------|--------------|-----------|
| Policy-Erstellung | R/A | C | C | C | C |
| Ausnahmenantrag | I | I | R | I | C |
| Risikobewertung | R/A | C | C | R | C |
| Kompensationsmaßnahmen | R/A | C | R | C | C |
| Genehmigung (Low) | R/A | I | I | I | I |
| Genehmigung (Medium) | R/A | I | R/A | C | I |
| Genehmigung (High) | R/A | R/A | R/A | C | I |
| Ausnahmenregister | C | I | I | C | R/A |
| Monitoring & Review | R/A | C | C | C | R |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** [TODO] (CISO)
- **CIO:** [TODO]
- **Risk Manager:** {{ meta-handbook.risk_manager }}
- **ISMS Team:** {{ meta-handbook.isms_team }}
- **Antragsteller:** Business Owner, IT-Betrieb
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0650_Richtlinie_Ausnahmenprozess.md** - Detaillierte Implementierungsrichtlinie
- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management Methodology
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Zugehörige Standards/Baselines
- Ausnahmenantrag-Template
- Risikobewertungs-Template
- Kompensationsmaßnahmen-Katalog
- Ausnahmenregister

### Zugehörige Prozesse
- Ausnahmenantragsprozess
- Risikobewertungsprozess
- Genehmigungsprozess
- Monitoring und Review Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl aktiver Ausnahmen
- Durchschnittliche Laufzeit von Ausnahmen
- Anzahl abgelaufener Ausnahmen (Ziel: 0)
- Anzahl verlängerter Ausnahmen
- Ausnahmen nach Risikokategorie (Low/Medium/High)
- Review-Compliance (Ziel: 100% quartalsweise)
- Anzahl zurückgezogener Ausnahmen

### Nachweise und Evidence
- Ausnahmenregister
- Ausnahmenanträge und Genehmigungen
- Risikobewertungen
- Kompensationsmaßnahmen-Dokumentation
- Review-Protokolle
- Audit Logs für Ausnahmen

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nicht genehmigte Ausnahmen:** Sofortige Compliance-Herstellung oder Systemabschaltung
- **Fehlende Dokumentation:** Nachholung, Compliance-Untersuchung
- **Abgelaufene Ausnahmen:** Sofortige Compliance-Herstellung oder Verlängerungsantrag
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen, Eskalation an Management

## 7. Ausnahmen

Diese Policy selbst unterliegt keinem Ausnahmenprozess. Änderungen an dieser Policy erfordern Management-Genehmigung.

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0650_Richtlinie_Ausnahmenprozess.md` - Detailed Guideline
- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management Methodology
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.1** - Policies for information security
- **ISO/IEC 27001:2022 Annex A.6.1.2** - Segregation of duties
- **ISO/IEC 27005** - Information security risk management
- **NIST SP 800-37** - Risk Management Framework
- **COBIT 2019** - APO12 (Managed Risk)

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO] (jährlich oder anlassbezogen)

