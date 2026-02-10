# Policy: Datenschutz Schnittstellen

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the interface between information security and data protection.
It ensures that ISMS and data protection requirements are aligned and coordinated.
Customize based on your organization's data protection framework and GDPR requirements.

ISO 27001:2022 Annex A Reference: A.5.31, A.5.32, A.5.33, A.5.34
-->

**Dokument-ID:** 0560  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.31-A.5.34 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Schnittstellen zwischen Informationssicherheit und Datenschutz der **{{ meta.organization.name }}**. Sie stellt sicher, dass ISMS und Datenschutzanforderungen aufeinander abgestimmt und koordiniert werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta.organization.name }}
- **Daten:** Alle personenbezogenen Daten gemäß DSGVO
- **Prozesse:** Alle Verarbeitungstätigkeiten personenbezogener Daten
- **Schnittstellen:** ISMS ↔ Datenschutz-Management-System
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Koordination ISMS und Datenschutz
ISMS und Datenschutz-Management werden koordiniert. CISO und DPO arbeiten eng zusammen und stimmen Maßnahmen ab.

### 3.2 Privacy by Design und by Default
Datenschutz wird von Anfang an in Systeme und Prozesse integriert (Privacy by Design). Datenschutzfreundliche Voreinstellungen sind Standard (Privacy by Default).

### 3.3 Datenschutz-Folgenabschätzung (DSFA)
Für risikoreiche Verarbeitungen werden Datenschutz-Folgenabschätzungen durchgeführt. DSFA wird mit ISMS-Risikoanalyse koordiniert.

### 3.4 Betroffenenrechte
Prozesse zur Erfüllung von Betroffenenrechten sind etabliert:
- Auskunftsrecht (Art. 15 DSGVO)
- Recht auf Berichtigung (Art. 16 DSGVO)
- Recht auf Löschung (Art. 17 DSGVO)
- Recht auf Datenübertragbarkeit (Art. 20 DSGVO)
- Widerspruchsrecht (Art. 21 DSGVO)

### 3.5 Verzeichnis von Verarbeitungstätigkeiten
Ein Verzeichnis von Verarbeitungstätigkeiten (VVT) wird geführt und aktuell gehalten. VVT ist mit ISMS-Asset-Inventar abgestimmt.

### 3.6 Auftragsverarbeitung
Auftragsverarbeiter werden nach DSGVO Art. 28 beauftragt. Auftragsverarbeitungsverträge (AVV) enthalten erforderliche Sicherheitsmaßnahmen.

### 3.7 Datenschutzverletzungen
Datenschutzverletzungen werden gemäß DSGVO Art. 33/34 behandelt. Meldepflichten an Aufsichtsbehörden und Betroffene werden eingehalten (72-Stunden-Frist).

### 3.8 Internationale Datentransfers
Internationale Datentransfers erfolgen nur mit angemessenen Garantien (Angemessenheitsbeschluss, Standardvertragsklauseln, BCR).

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Datenschutz Schnittstellen

| Aktivität | CISO | DPO | IT-Betrieb | Business Owner | Legal |
|-----------|------|-----|------------|----------------|-------|
| Policy-Erstellung | R/A | R/A | C | C | C |
| DSFA-Durchführung | C | R/A | C | R | C |
| Betroffenenrechte | I | R/A | C | C | C |
| VVT-Pflege | C | R/A | C | R | I |
| AVV-Verhandlung | C | R/A | I | C | R |
| Data Breach Notification | R/A | R/A | C | C | C |
| Privacy by Design | R | R/A | R | R | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO) und {{ meta.dpo.name }} (DPO)
- **Data Protection Officer:** {{ meta.dpo.name }}
- **Privacy Officer:** {{ meta.privacy.officer }}
- **Umsetzungsverantwortliche:** IT-Betrieb, Business Owner
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, Datenschutzaufsicht

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0570_Richtlinie_Datenschutz_Anforderungen_und_Datenverarbeitung.md** - Detaillierte Implementierungsrichtlinie
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0400_Policy_Incident_Management.md` - Incident Management Policy (Data Breaches)
- `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md` - Supplier Security Policy (AVV)

### Zugehörige Standards/Baselines
- DSFA-Methodik
- Betroffenenrechte-Prozesse
- AVV-Templates
- Data Breach Notification Prozess

### Zugehörige Prozesse
- Datenschutz-Folgenabschätzung (DSFA)
- Betroffenenrechte-Prozess
- Data Breach Notification Prozess
- Privacy by Design Review

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl durchgeführter DSFAs
- Durchschnittliche Bearbeitungszeit Betroffenenrechte (Ziel: < 30 Tage)
- Anzahl Data Breaches und Meldungen
- VVT-Aktualität (Ziel: quartalsweise Aktualisierung)
- Anzahl AVVs mit aktuellen Sicherheitsmaßnahmen (Ziel: 100%)
- Privacy by Design Review Coverage

### Nachweise und Evidence
- DSFA-Dokumentation
- Verzeichnis von Verarbeitungstätigkeiten (VVT)
- Betroffenenrechte-Anfragen und Responses
- Auftragsverarbeitungsverträge (AVV)
- Data Breach Notifications
- Privacy by Design Reviews

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **DSGVO-Verstöße:** Incident Response, Meldung an Aufsichtsbehörde, ggf. Bußgelder
- **Nicht gemeldete Data Breaches:** Compliance-Untersuchung, Disziplinarmaßnahmen
- **Fehlende DSFAs:** Nachholung, Verarbeitungsstopp
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen, Bußgelder

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und DPO genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0570_Richtlinie_Datenschutz_Anforderungen_und_Datenverarbeitung.md` - Detailed Guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.31** - Legal, statutory, regulatory and contractual requirements
- **ISO/IEC 27001:2022 Annex A.5.32** - Intellectual property rights
- **ISO/IEC 27001:2022 Annex A.5.33** - Protection of records
- **ISO/IEC 27001:2022 Annex A.5.34** - Privacy and protection of PII
- **DSGVO (EU 2016/679)** - Datenschutz-Grundverordnung
- **ISO/IEC 27701** - Privacy Information Management System
- **BDSG** - Bundesdatenschutzgesetz

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
