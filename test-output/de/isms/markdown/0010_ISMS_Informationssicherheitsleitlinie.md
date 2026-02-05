# ISMS-Leitlinie / Informationssicherheits-Policy



**Dokument-ID:** 0010  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Clause 5.2 (inkl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Informationssicherheitsleitlinie definiert die strategischen Grundsätze und Verpflichtungen der **AdminSend GmbH** zum Schutz von Informationswerten. Sie bildet die Grundlage für das Information Security Management System (ISMS) nach ISO/IEC 27001:2022 und stellt sicher, dass Informationssicherheit als integraler Bestandteil aller Geschäftsprozesse verstanden und umgesetzt wird.



## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Systeme und Informationen:** Alle IT-Systeme, Anwendungen, Daten und Informationsverarbeitungsprozesse
- **Personen:** Alle Mitarbeiter, Auftragnehmer, Lieferanten und Dritte mit Zugang zu Informationswerten
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen von dieser Policy sind nur über den definierten Ausnahmenprozess (siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.



## 3. Grundsätze (Policy Statements)

Die AdminSend GmbH verpflichtet sich zu folgenden Grundsätzen der Informationssicherheit:

### 3.1 Vertraulichkeit (Confidentiality)
Informationen werden nur autorisierten Personen, Systemen und Prozessen zugänglich gemacht. Der Zugriff erfolgt nach dem Need-to-Know-Prinzip und wird durch geeignete Zugangskontrollen geschützt.

### 3.2 Integrität (Integrity)
Die Richtigkeit, Vollständigkeit und Aktualität von Informationen wird durch geeignete Kontrollen sichergestellt. Unbefugte oder unbeabsichtigte Änderungen werden verhindert und erkannt.

### 3.3 Verfügbarkeit (Availability)
Informationen und IT-Systeme stehen autorisierten Nutzern bei Bedarf zur Verfügung. Geschäftskritische Systeme werden durch angemessene Redundanz- und Wiederherstellungsmaßnahmen geschützt.

### 3.4 Compliance und rechtliche Anforderungen
Die Organisation erfüllt alle anwendbaren gesetzlichen, regulatorischen und vertraglichen Anforderungen an die Informationssicherheit, einschließlich Datenschutz (DSGVO), Branchenstandards und Kundenanforderungen.

### 3.5 Risikoorientierter Ansatz
Informationssicherheitsmaßnahmen werden auf Basis einer systematischen Risikoanalyse priorisiert und umgesetzt. Risiken werden identifiziert, bewertet und nach definierten Kriterien behandelt.

### 3.6 Kontinuierliche Verbesserung
Das ISMS wird kontinuierlich überwacht, gemessen und verbessert. Sicherheitsvorfälle, Audits und Reviews dienen als Grundlage für Verbesserungsmaßnahmen.

### 3.7 Awareness und Schulung
Alle Mitarbeiter werden regelmäßig über Informationssicherheitsrisiken und ihre Verantwortlichkeiten geschult. Sicherheitsbewusstsein ist Teil der Unternehmenskultur.

### 3.8 Lieferanten- und Drittparteien-Management
Lieferanten und Dritte, die Zugang zu Informationswerten haben, werden nach Sicherheitskriterien bewertet und vertraglich zur Einhaltung von Sicherheitsanforderungen verpflichtet.



## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: ISMS-Leitlinie

| Aktivität | CISO | CIO | Geschäftsführung | IT-Betrieb | Fachabteilungen |
|-----------|------|-----|------------------|------------|-----------------|
| Policy-Erstellung | R/A | C | I | C | C |
| Policy-Genehmigung | C | C | A | I | I |
| Policy-Kommunikation | R | C | I | I | I |
| Policy-Umsetzung | A | R | I | R | R |
| Policy-Überwachung | R/A | C | I | C | C |
| Policy-Review | R/A | C | C | I | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **CISO (Chief Information Security Officer):** Thomas Weber (thomas.weber@adminsend.de)
  - Verantwortlich für die Entwicklung, Umsetzung und Überwachung des ISMS
  - Berichtet an: Anna Schmidt

- **CIO (Chief Information Officer):** Anna Schmidt (anna.schmidt@adminsend.de)
  - Verantwortlich für IT-Strategie und IT-Betrieb
  - Unterstützt ISMS-Umsetzung

- **Geschäftsführung:** {{ meta.management.ceo }}
  - Genehmigt ISMS-Leitlinie und stellt Ressourcen bereit
  - Trägt Gesamtverantwortung für Informationssicherheit



## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Diese abstrakte Policy wird durch folgende detaillierte Dokumente konkretisiert:

### Basis-ISMS-Dokumente
- `0020_ISMS_Geltungsbereich_Scope.md` - ISMS Scope Definition
- `0030_ISMS_Kontext_und_Interessierte_Parteien.md` - Context of Organization
- `0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md` - ISMS Governance
- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management Methodology

### Themenspezifische Policies (Abstract)
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md`
- `0240_Policy_Authentisierung_und_Passwoerter.md`
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md`
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md`
- [Weitere Policies siehe ISMS-Dokumentenstruktur]

### Detaillierte Richtlinien (Detailed Guidelines)
- Siehe entsprechende Richtlinien-Dokumente (0210-0690, ungerade Nummern)



## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl Sicherheitsvorfälle pro Quartal
- Durchschnittliche Zeit zur Behebung kritischer Schwachstellen
- Schulungsteilnahme-Quote (Ziel: 100% jährlich)
- Audit-Findings und deren Behebungsrate
- Compliance-Rate mit Sicherheitsrichtlinien

### Nachweise und Evidence
- ISMS-Dokumentation und Aufzeichnungen
- Audit-Berichte (intern und extern)
- Risikoregister und Risikobehandlungspläne
- Schulungsnachweise und Awareness-Kampagnen
- Incident-Reports und Lessons Learned

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt und können zu disziplinarischen Maßnahmen führen, einschließlich:
- Verwarnung und Nachschulung
- Entzug von Zugriffsrechten
- Arbeitsrechtliche Konsequenzen
- Rechtliche Schritte bei vorsätzlichen oder grob fahrlässigen Verstößen



## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig und müssen über den definierten Ausnahmenprozess beantragt werden:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und ggf. der Geschäftsführung genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert und regelmäßig überprüft
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet und müssen regelmäßig erneuert werden

## 8. Referenzen

### Interne Dokumente
- ISMS-Dokumentenstruktur (siehe README.md)
- Risikoregister (`0080_ISMS_Risikoregister_Template.md`)
- Statement of Applicability (`0100_ISMS_Statement_of_Applicability_SoA_Template.md`)
- Internes Auditprogramm (`0130_ISMS_Internes_Auditprogramm.md`)

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022** - Information security management systems - Requirements
- **ISO/IEC 27001:2022/Amd 1:2024** - Amendment 1 (Annex A updates)
- **ISO/IEC 27002:2022** - Information security controls
- **DSGVO (EU 2016/679)** - Datenschutz-Grundverordnung
- **BSI IT-Grundschutz** - Bundesamt für Sicherheit in der Informationstechnik

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)
