# Policy: Datenklassifizierung und Informationshandling

**Dokument-ID:** 0280
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

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for data classification and information handling.
It ensures that information is classified according to its sensitivity and handled
appropriately throughout its lifecycle. Customize based on your organization's
data classification scheme and regulatory requirements (GDPR, industry-specific).

ISO 27001:2022 Annex A Reference: A.5.12, A.5.13, A.5.14
-->

## 1. Zweck

Diese Policy definiert die Grundsätze für Datenklassifizierung und Informationshandling der **{{ meta-organisation.name }}**. Sie stellt sicher, dass Informationen entsprechend ihrer Sensitivität und ihres Schutzbedarfs klassifiziert, gekennzeichnet und über ihren gesamten Lebenszyklus angemessen geschützt werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Informationen:** Alle Informationen in jeglicher Form (digital, physisch, mündlich)
- **Systeme:** Alle IT-Systeme, Anwendungen, Datenbanken, Speichermedien
- **Personen:** Alle Mitarbeiter, Auftragnehmer, Lieferanten und Dritte mit Zugang zu Informationen
- **Lebenszyklus:** Erstellung, Speicherung, Verarbeitung, Übertragung, Archivierung, Vernichtung
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Verpflichtende Klassifizierung
Alle Informationen der Organisation müssen klassifiziert werden. Die Klassifizierung erfolgt durch den Information Owner basierend auf Vertraulichkeit, Integrität und Verfügbarkeit.

### 3.2 Klassifizierungsstufen
Die Organisation verwendet folgende Klassifizierungsstufen:
- **Öffentlich (Public):** Informationen, die öffentlich zugänglich sind oder sein dürfen
- **Intern (Internal):** Informationen für den internen Gebrauch, nicht für die Öffentlichkeit bestimmt
- **Vertraulich (Confidential):** Sensible Informationen, deren Offenlegung der Organisation schaden könnte
- **Streng Vertraulich (Highly Confidential):** Hochsensible Informationen mit höchstem Schutzbedarf

### 3.3 Kennzeichnung und Labeling
Klassifizierte Informationen werden entsprechend gekennzeichnet:
- Digitale Dokumente: Metadaten, Header/Footer, Wasserzeichen
- Physische Dokumente: Stempel, Aufkleber, Deckblätter
- E-Mails: Subject-Präfix, Banner
- Speichermedien: Etiketten

### 3.4 Handling-Anforderungen
Für jede Klassifizierungsstufe gelten spezifische Handling-Anforderungen:
- Zugriffskontrolle und Berechtigungen
- Verschlüsselung (at rest, in transit)
- Speicherung und Archivierung
- Übertragung und Weitergabe
- Vernichtung und Löschung

### 3.5 Information Owner Verantwortung
Jede Information hat einen definierten Information Owner, der verantwortlich ist für:
- Klassifizierung der Information
- Definition von Zugriffsrechten
- Regelmäßige Überprüfung der Klassifizierung
- Genehmigung von Zugriffs- und Weitergabeanfragen

### 3.6 Weitergabe und Sharing
Die Weitergabe klassifizierter Informationen erfolgt nur nach dem Need-to-Know-Prinzip:
- Interne Weitergabe: Nach Genehmigung durch Information Owner
- Externe Weitergabe: Nach Genehmigung und mit geeigneten Schutzmaßnahmen (NDA, Verschlüsselung)
- Cloud-Speicherung: Nur in genehmigten Cloud-Services mit angemessenen Sicherheitskontrollen

### 3.7 Sichere Vernichtung
Informationen werden am Ende ihres Lebenszyklus sicher vernichtet:
- Digitale Daten: Sichere Löschung (Overwriting, Degaussing)
- Physische Dokumente: Schreddern, Verbrennen
- Speichermedien: Physische Zerstörung bei hochsensiblen Daten

### 3.8 Datenschutz-Compliance
Die Klassifizierung und das Handling personenbezogener Daten erfolgt in Übereinstimmung mit der DSGVO und anderen Datenschutzvorschriften.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Datenklassifizierung und Informationshandling

| Aktivität | CISO | Information Owner | Mitarbeiter | IT-Betrieb | Data Protection Officer |
|-----------|------|-------------------|-------------|------------|-------------------------|
| Policy-Erstellung | R/A | C | I | C | C |
| Klassifizierung | C | R/A | I | I | C |
| Kennzeichnung | I | A | R | C | I |
| Zugriffsgenehmigung | C | R/A | I | I | C |
| Handling-Compliance | A | R | R | C | C |
| Weitergabe-Genehmigung | C | R/A | I | I | C |
| Sichere Vernichtung | C | A | I | R | C |
| Monitoring und Audits | R/A | C | I | C | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Information Owner:** Fachbereichsleiter, Systemverantwortliche
- **Data Protection Officer:** {{ meta.dpo.name }}
- **Umsetzungsverantwortliche:** Alle Mitarbeiter, IT-Betrieb
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, DPO

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md** - Detaillierte Implementierungsrichtlinie
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Cryptography Policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Data Protection Policy
- `0580_Policy_Aufbewahrung_und_Loeschung.md` - Retention and Deletion Policy

### Zugehörige Standards/Baselines
- Klassifizierungsschema und Handling-Matrix
- Labeling-Standards (digital und physisch)
- Verschlüsselungsanforderungen pro Klassifizierungsstufe
- Vernichtungsstandards

### Zugehörige Prozesse
- Klassifizierungsprozess
- Information Owner Assignment
- Weitergabe- und Sharing-Genehmigungsprozess
- Sichere Vernichtungsprozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anteil klassifizierter Informationen (Ziel: 100%)
- Anteil korrekt gekennzeichneter Dokumente
- Anzahl Verstöße gegen Handling-Anforderungen
- Anzahl unbefugter Weitergaben
- Durchschnittliche Zeit zur Klassifizierung neuer Informationen
- Compliance-Rate mit Vernichtungsanforderungen

### Nachweise und Evidence
- Klassifizierungs-Register
- Information Owner Assignments
- Weitergabe-Genehmigungen
- Vernichtungsnachweise
- DLP (Data Loss Prevention) Logs
- Audit-Berichte zu Klassifizierung und Handling

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Fehlende Klassifizierung:** Nachschulung, Korrektur
- **Falsche Kennzeichnung:** Korrektur, Nachschulung
- **Unbefugte Weitergabe:** Verwarnung bis Kündigung, ggf. rechtliche Schritte
- **Unsachgemäße Vernichtung:** Untersuchung, Nachschulung
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Information Owner genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet und werden regelmäßig überprüft
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Sicherheitsmaßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md` - Detailed Guideline
- `0300_Policy_Asset_Management.md` - Asset Management Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.12** - Classification of information
- **ISO/IEC 27001:2022 Annex A.5.13** - Labelling of information
- **ISO/IEC 27001:2022 Annex A.5.14** - Information transfer
- **ISO/IEC 27002:2022** - Information security controls
- **DSGVO (EU 2016/679)** - Datenschutz-Grundverordnung
- **BSI IT-Grundschutz** - Baustein CON.6 Löschen und Vernichten

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

