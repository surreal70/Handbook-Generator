# Policy: HR Security

**Dokument-ID:** 0520
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

Diese Policy definiert die Grundsätze für HR Security der **AdminSend GmbH**. Sie stellt sicher, dass Sicherheitsverantwortlichkeiten über den gesamten Beschäftigungslebenszyklus verstanden und erfüllt werden - von der Einstellung bis zur Beendigung des Arbeitsverhältnisses.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Personen:** Alle Mitarbeiter, Auftragnehmer, Zeitarbeiter, Praktikanten
- **Lebenszyklus:** Pre-Employment, Onboarding, Employment, Offboarding
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Pre-Employment Screening
Vor Einstellung werden angemessene Background Checks durchgeführt (Referenzen, Qualifikationen, ggf. Führungszeugnis). Das Screening richtet sich nach Rolle und Schutzbedarf.

### 3.2 Vertragliche Sicherheitsverpflichtungen
Arbeitsverträge enthalten Sicherheitsklauseln:
- Vertraulichkeitsvereinbarungen (NDA)
- Acceptable Use Policy Acknowledgement
- Datenschutzverpflichtungen
- Intellectual Property Rights

### 3.3 Security Awareness und Training
Alle Mitarbeiter durchlaufen Security Awareness Training:
- **Onboarding:** Initiales Security Training
- **Jährlich:** Auffrischungstraining
- **Rollenspezifisch:** Zusätzliches Training für privilegierte Rollen

### 3.4 Joiner-Mover-Leaver-Prozess
Sicherheitsrelevante Aktivitäten werden im Beschäftigungslebenszyklus durchgeführt:
- **Joiner:** Zugriffsvergabe, Training, Equipment-Ausgabe
- **Mover:** Zugriffsanpassung bei Rollenwechsel
- **Leaver:** Zugriffsentzug, Equipment-Rückgabe, Exit-Interview

### 3.5 Disziplinarverfahren
Sicherheitsverstöße werden nach definierten Disziplinarverfahren behandelt. Verstöße werden dokumentiert und können zu arbeitsrechtlichen Konsequenzen führen.

### 3.6 Verantwortlichkeiten und Pflichten
Mitarbeiter sind verpflichtet:
- Sicherheitsrichtlinien einzuhalten
- Sicherheitsvorfälle zu melden
- An Security Training teilzunehmen
- Vertraulichkeit zu wahren

### 3.7 Privilegierte Rollen
Mitarbeiter mit privilegierten Zugriffen unterliegen erweiterten Anforderungen:
- Erweiterte Background Checks
- Zusätzliches Security Training
- Regelmäßige Rezertifizierung
- Strikte Überwachung

### 3.8 Offboarding und Zugriffsentzug
Bei Beendigung des Arbeitsverhältnisses werden alle Zugriffe unverzüglich entzogen:
- IT-Zugriffe deaktiviert (Ziel: < 1 Tag)
- Equipment zurückgegeben
- Vertraulichkeitsverpflichtungen erneuert
- Exit-Interview durchgeführt

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: HR Security

| Aktivität | CISO | HR | Hiring Manager | IT-Betrieb | Legal |
|-----------|------|-----|----------------|------------|-------|
| Policy-Erstellung | R/A | C | C | I | C |
| Background Checks | C | R/A | C | I | C |
| Vertragsklauseln | C | R | I | I | R/A |
| Security Training | R/A | C | I | C | I |
| Joiner Process | C | R | R/A | R | I |
| Mover Process | C | R | R/A | R | I |
| Leaver Process | C | R/A | C | R | I |
| Disziplinarverfahren | C | R/A | C | I | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** [TODO] (CISO)
- **HR Manager:** {{ meta-handbook.hr_manager }}
- **Security Awareness Manager:** {{ meta-handbook.security_awareness_manager }}
- **Umsetzungsverantwortliche:** HR, Hiring Manager, IT-Betrieb
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md** - Detaillierte Implementierungsrichtlinie
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access Control Policy
- `0200_Policy_Akzeptable_Nutzung_IT.md` - Acceptable Use Policy
- `0120_ISMS_Schulung_Awareness_und_Kompetenz.md` - Training and Awareness

### Zugehörige Standards/Baselines
- Background Check Requirements
- Vertragliche Sicherheitsklauseln (Templates)
- Security Training Curriculum
- Joiner-Mover-Leaver Checklists

### Zugehörige Prozesse
- Pre-Employment Screening Prozess
- Joiner-Mover-Leaver Prozess
- Security Training Prozess
- Disziplinarverfahren

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Background Check Completion Rate (Ziel: 100%)
- Security Training Completion Rate (Ziel: 100% jährlich)
- Durchschnittliche Zeit zur Zugriffsvergabe (Joiner)
- Durchschnittliche Zeit zum Zugriffsentzug (Leaver) (Ziel: < 1 Tag)
- Anzahl Sicherheitsverstöße und Disziplinarverfahren
- NDA Signing Rate (Ziel: 100%)

### Nachweise und Evidence
- Background Check Dokumentation
- Verträge mit Sicherheitsklauseln
- Security Training Nachweise
- Joiner-Mover-Leaver Checklists
- Disziplinarverfahren-Dokumentation
- Exit-Interview-Protokolle

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Fehlende Background Checks:** Nachholung vor Zugriffsvergabe
- **Nicht absolviertes Training:** Zugriffsbeschränkung bis Nachholung
- **Sicherheitsverstöße:** Disziplinarverfahren nach HR-Prozess
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen bis Kündigung

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und HR Manager genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md` - Detailed Guideline
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access Control Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.6.1** - Screening
- **ISO/IEC 27001:2022 Annex A.6.2** - Terms and conditions of employment
- **ISO/IEC 27001:2022 Annex A.6.3** - Information security awareness, education and training
- **ISO/IEC 27001:2022 Annex A.6.4** - Disciplinary process
- Arbeitsrechtliche Vorgaben (Deutschland)
- DSGVO (EU 2016/679) - Datenschutz bei Background Checks

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO] (jährlich oder anlassbezogen)

