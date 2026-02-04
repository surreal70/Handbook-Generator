# ISMS-Organisation, Rollen und Verantwortlichkeiten

**Dokument-ID:** 0020  
**Dokumenttyp:** Grundlagendokument  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2/200-3)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the ISMS organization structure, roles, and responsibilities according to BSI IT-Grundschutz.
Customize all [TODO] placeholders based on your organization's specific structure.
Reference: BSI Standard 200-1 (ISMS Organization Requirements)
-->

## 1. ISMS-Organisation

### 1.1 ISMS-Owner/Sponsor

**Verantwortlich:** {{ meta.ceo.name }} ({{ meta.ceo.email }})

Der ISMS-Owner trägt die Gesamtverantwortung für das Informationssicherheits-Managementsystem und stellt sicher, dass:
- Ausreichende Ressourcen bereitgestellt werden
- Die Informationssicherheitsleitlinie genehmigt wird
- Strategische Entscheidungen zur Informationssicherheit getroffen werden
- Das ISMS in die Geschäftsprozesse integriert wird

### 1.2 Informationssicherheitsbeauftragter (ISB)

**Verantwortlich:** {{ meta.ciso.name }} ({{ meta.ciso.email }})

Der ISB ist die zentrale Koordinationsstelle für alle Informationssicherheitsaktivitäten:
- Koordination und Steuerung des ISMS
- Beratung der Geschäftsführung und Fachabteilungen
- Durchführung von Risikoanalysen und Sicherheitsbewertungen
- Überwachung der Umsetzung von Sicherheitsmaßnahmen
- Berichterstattung an die Geschäftsführung
- Koordination von Sicherheitsvorfällen
- Durchführung von Awareness-Maßnahmen

### 1.3 ISMS-Team / Informationssicherheitsgremium

Das ISMS-Team unterstützt den ISB bei der Umsetzung des ISMS:

| Rolle | Name | Verantwortungsbereich |
|---|---|---|
| ISB (Leitung) | {{ meta.ciso.name }} | Gesamtkoordination ISMS |
| IT-Leitung | {{ meta.cio.name }} | Technische Sicherheitsmaßnahmen |
| Datenschutzbeauftragter | [TODO] | Datenschutz-Schnittstelle |
| BCM-Verantwortlicher | [TODO] | Business Continuity |
| Risk Manager | [TODO] | Risikomanagement |
| HR-Vertreter | [TODO] | Personal- und Awareness-Themen |
| Legal/Compliance | [TODO] | Rechtliche Anforderungen |

**Sitzungsrhythmus:** [TODO: z.B. monatlich, quartalsweise]

### 1.4 Schnittstellen zu anderen Bereichen

#### 1.4.1 IT Service Management (ITSM)

**Ansprechpartner:** {{ meta.cio.name }}

Schnittstellen:
- Change Management: Sicherheitsbewertung von Changes
- Incident Management: Sicherheitsvorfälle
- Problem Management: Sicherheitsschwachstellen
- Configuration Management: Asset-Inventar

#### 1.4.2 Datenschutz

**Ansprechpartner:** [TODO: Datenschutzbeauftragter]

Schnittstellen:
- Verzeichnis von Verarbeitungstätigkeiten (VVT)
- Datenschutz-Folgenabschätzung (DSFA)
- Technische und organisatorische Maßnahmen (TOM)
- Meldung von Datenschutzverletzungen

#### 1.4.3 Business Continuity Management (BCM)

**Ansprechpartner:** [TODO: BCM-Verantwortlicher]

Schnittstellen:
- Business Impact Analysis (BIA)
- IT-Disaster Recovery Pläne
- Notfallübungen und Tests
- Krisenmanagement

#### 1.4.4 Risikomanagement

**Ansprechpartner:** [TODO: Risk Manager]

Schnittstellen:
- Unternehmensweites Risikomanagement
- Risikoregister und -bewertung
- Risikoreporting
- Risikoakzeptanz-Entscheidungen

#### 1.4.5 Internal Audit

**Ansprechpartner:** [TODO: Internal Audit]

Schnittstellen:
- ISMS-Audits
- Compliance-Prüfungen
- Nachverfolgung von Audit-Findings
- Berichterstattung an Management

## 2. Rollen und Verantwortlichkeiten

### 2.1 Informationsverbund-Verantwortliche/r

**Rolle:** Verantwortlich für einen spezifischen Informationsverbund (z.B. Geschäftsanwendung, IT-System)

**Aufgaben:**
- Definition des Geltungsbereichs des Informationsverbunds
- Durchführung der Strukturanalyse
- Schutzbedarfsfeststellung
- Modellierung und Bausteinzuordnung
- Koordination der Maßnahmenumsetzung
- Überwachung der Sicherheit des Informationsverbunds

[TODO: Benennen Sie spezifische Informationsverbund-Verantwortliche]

### 2.2 Asset Owner / System Owner

**Rolle:** Verantwortlich für spezifische Assets oder IT-Systeme

**Aufgaben:**
- Klassifizierung und Bewertung von Assets
- Definition von Sicherheitsanforderungen
- Genehmigung von Zugriffsrechten
- Überwachung der Asset-Nutzung
- Entscheidung über Außerbetriebnahme

[TODO: Definieren Sie Asset Owner für kritische Systeme]

### 2.3 Maßnahme-/Control-Owner

**Rolle:** Verantwortlich für die Umsetzung spezifischer Sicherheitsmaßnahmen

**Aufgaben:**
- Implementierung zugewiesener Sicherheitsmaßnahmen
- Dokumentation der Umsetzung
- Nachweis der Wirksamkeit
- Kontinuierliche Überwachung und Verbesserung

[TODO: Zuordnung von Maßnahmen-Verantwortlichen]

### 2.4 Administratoren / Betreiber

**Rolle:** Technische Umsetzung und Betrieb von IT-Systemen

**Aufgaben:**
- Konfiguration und Härtung von Systemen
- Patch- und Update-Management
- Monitoring und Logging
- Backup und Recovery
- Incident Response (technisch)

**Verantwortlich:** {{ meta.cio.name }} (IT-Leitung)

### 2.5 Alle Mitarbeitenden

**Rolle:** Nutzer von IT-Systemen und Informationen

**Aufgaben:**
- Einhaltung von Sicherheitsrichtlinien
- Meldung von Sicherheitsvorfällen
- Teilnahme an Schulungen
- Verantwortungsvoller Umgang mit Informationen
- Schutz von Zugangsdaten

## 3. RACI-Matrix für BSI IT-Grundschutz-Prozesse

<!-- 
RACI-Legende:
R = Responsible (Durchführungsverantwortung)
A = Accountable (Gesamtverantwortung, Entscheidungsbefugnis)
C = Consulted (Konsultiert, Fachexpertise)
I = Informed (Informiert)
-->

| Aktivität | Geschäfts­führung | ISB | IT-Leitung | Informations­verbund-Verantwortliche | Fach­abteilungen | Internal Audit |
|---|---|---|---|---|---|---|
| **Strukturanalyse** | I | A | C | R | C | I |
| **Schutzbedarfsfeststellung** | A | C | C | R | C | I |
| **Modellierung (Bausteinzuordnung)** | I | A | C | R | C | I |
| **Basis-Sicherheitscheck** | I | A | C | R | C | I |
| **Risikoanalyse (BSI 200-3)** | A | R | C | C | C | I |
| **Maßnahmenplanung** | A | R | C | C | C | I |
| **Maßnahmenumsetzung** | I | C | R | R | R | I |
| **Wirksamkeitsprüfung** | I | A | C | R | C | I |
| **ISMS-Audit** | I | C | C | C | C | R/A |
| **Management Review** | A | R | C | I | I | C |
| **Incident Management** | I | A | R | C | C | I |
| **Awareness-Schulungen** | I | A | C | C | R | I |
| **Dokumentation** | I | A | R | R | C | I |

## 4. Eskalationswege

### 4.1 Operative Eskalation

1. **Level 1:** Informationsverbund-Verantwortliche / System Owner
2. **Level 2:** ISB / IT-Leitung
3. **Level 3:** Geschäftsführung

### 4.2 Sicherheitsvorfälle

1. **Meldung:** Alle Mitarbeitenden → ISB / IT-Leitung
2. **Bewertung:** ISB / IT-Leitung
3. **Eskalation (bei Major Incidents):** Geschäftsführung
4. **Externe Meldung (falls erforderlich):** BSI, Datenschutzbehörde, Strafverfolgung

## 5. Kommunikation und Berichtswesen

### 5.1 Regelmäßige Berichte

| Bericht | Frequenz | Ersteller | Empfänger |
|---|---|---|---|
| ISMS-Status-Report | Monatlich | ISB | Geschäftsführung, ISMS-Team |
| Sicherheitsvorfälle | Monatlich | ISB | Geschäftsführung |
| Risiko-Dashboard | Quartalsweise | ISB | Geschäftsführung |
| Management Review | Jährlich | ISB | Geschäftsführung |
| Audit-Ergebnisse | Nach Audit | Internal Audit | Geschäftsführung, ISB |

### 5.2 Ad-hoc Kommunikation

- **Sicherheitsvorfälle:** Sofortige Meldung an ISB
- **Kritische Schwachstellen:** Sofortige Meldung an ISB und IT-Leitung
- **Compliance-Verstöße:** Meldung an ISB und Legal/Compliance

## 6. Ressourcen und Budget

[TODO: Definieren Sie Budget und Ressourcen für ISMS-Aktivitäten]

- **ISMS-Budget:** [TODO]
- **Personalressourcen:** [TODO]
- **Externe Unterstützung:** [TODO]
- **Tools und Systeme:** [TODO]

## 7. Review und Aktualisierung

Diese Organisationsstruktur wird mindestens jährlich oder bei wesentlichen Änderungen überprüft und aktualisiert.

**Nächster Review:** {{ meta.document.next_review }}

---

**Referenzen:**
- BSI Standard 200-1: Managementsysteme für Informationssicherheit (ISMS)
- BSI Standard 200-2: IT-Grundschutz-Methodik
- BSI IT-Grundschutz-Kompendium

<!-- End of template -->
