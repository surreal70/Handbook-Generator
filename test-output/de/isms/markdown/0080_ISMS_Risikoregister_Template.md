# Risikoregister (Template)

**Dokument-ID:** ISMS-0080
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



## 1. Zweck und Anleitung

### 1.1 Zweck

Das Risikoregister dokumentiert alle identifizierten Informationssicherheitsrisiken im ISMS-Scope der **AdminSend GmbH**. Es dient als:
- Zentrale Übersicht aller Risiken
- Grundlage für Risikobehandlungsentscheidungen
- Nachweis für Audits und Compliance
- Basis für Risiko-Reporting

### 1.2 Anleitung zur Verwendung

**Jede Zeile beschreibt ein Risiko:**
- Eindeutige Risiko-ID (R-001, R-002, etc.)
- Betroffenes Asset oder Prozess
- Bedrohung und Schwachstelle
- Risikobewertung (Wahrscheinlichkeit, Auswirkung, Score)
- Risiko-Eigentümer
- Behandlungsstrategie
- Verknüpfung zu Controls und Maßnahmen

**Pflege:**
- Quartalsweise Review durch ISMS Manager
- Anlassbezogene Updates bei neuen Risiken
- Archivierung behandelter/geschlossener Risiken

**Verknüpfungen:**
- Controls: Siehe `0100_ISMS_Statement_of_Applicability_SoA_Template.md`
- Maßnahmen: Siehe `0090_ISMS_Risikobehandlungsplan_RTP_Template.md`
- Evidence: Siehe `0700_Anhang_Nachweisregister_Evidence.md`

## 2. Risikoregister-Tabelle

### 2.1 Aktive Risiken

| Risiko-ID | Asset/Prozess | Bedrohung | Schwachstelle | Auswirkung (1-5) | Wahrscheinlichkeit (1-5) | Score | Risikostufe | Risiko-Eigentümer | Behandlung | Maßnahme/Control | Status | Zieltermin | Bemerkungen |
|-----------|---------------|-----------|---------------|------------------|--------------------------|-------|-------------|-------------------|------------|------------------|--------|------------|-------------|
| R-001 | [[ netbox.device.core_switch.name ]] | Hardware-Ausfall | Keine Redundanz | 4 | 3 | 12 | Mittel | [TODO] | Mindern | Redundanter Switch beschaffen | Offen | 2026-06-30 | Budget genehmigt |
| R-002 | Kundendaten (DSGVO) | Ransomware | Unzureichende Backups | 5 | 4 | 20 | Hoch | [TODO] | Mindern | Immutable Backups implementieren | In Arbeit | 2026-03-31 | Siehe M-002 |
| R-003 | E-Mail-System | Phishing | Fehlende MFA | 4 | 4 | 16 | Hoch | [TODO] | Mindern | MFA für alle Benutzer | In Arbeit | 2026-02-28 | 80% abgeschlossen |
| R-004 | Entwicklungsumgebung | Secrets in Code | Keine Secret-Scanning | 3 | 3 | 9 | Mittel | Dev-Lead | Mindern | Secret-Scanning Tool | Geplant | 2026-04-30 | Tool-Evaluierung läuft |
| R-005 | Remote-Zugriff | Unbefugter Zugriff | Schwache VPN-Konfiguration | 4 | 2 | 8 | Mittel | IT-Betrieb | Mindern | VPN-Hardening | Offen | 2026-05-31 | - |



[TODO: Weitere Risiken hinzufügen basierend auf Risikoanalyse]

### 2.2 Akzeptierte Risiken

| Risiko-ID | Asset/Prozess | Bedrohung | Schwachstelle | Score | Risikostufe | Risiko-Eigentümer | Akzeptiert durch | Akzeptanzdatum | Gültig bis | Begründung | Review-Status |
|-----------|---------------|-----------|---------------|-------|-------------|-------------------|------------------|----------------|------------|------------|---------------|
| R-010 | Legacy-System XYZ | Ungepatchte Schwachstellen | System im Auslauf | 9 | Mittel | [TODO] | [TODO] | 2026-01-15 | 2026-06-30 | System wird am 30.06.2026 außer Betrieb genommen | Aktiv |
| R-011 | Testumgebung | Fehlende Verschlüsselung | Keine produktiven Daten | 6 | Niedrig | Dev-Lead | [TODO] | 2026-01-20 | 2027-01-20 | Testumgebung enthält nur synthetische Daten | Aktiv |

[TODO: Akzeptierte Risiken dokumentieren]

### 2.3 Geschlossene/Behandelte Risiken (Archiv)

| Risiko-ID | Asset/Prozess | Bedrohung | Score | Behandlung | Abschlussdatum | Bemerkungen |
|-----------|---------------|-----------|-------|------------|----------------|-------------|
| R-020 | Webserver | Ungepatchte Schwachstelle CVE-2025-1234 | 15 | Mindern | 2026-01-10 | Patch installiert, Vulnerability Scan bestätigt |
| R-021 | Firewall | Fehlkonfiguration | 12 | Mindern | 2026-01-15 | Konfiguration korrigiert, Audit durchgeführt |

[TODO: Geschlossene Risiken archivieren]

## 3. Risikokategorien und Klassifizierung

### 3.1 Risikokategorien

**Technische Risiken:**
- Infrastruktur (Hardware, Netzwerk, Cloud)
- Anwendungen (Software, Entwicklung)
- Daten (Datenbanken, Backups, Verschlüsselung)

**Organisatorische Risiken:**
- Prozesse (Fehlende oder unzureichende Prozesse)
- Personal (Fehlende Kompetenzen, Insider-Bedrohung)
- Lieferanten (Third-Party-Risiken)

**Physische Risiken:**
- Standorte (Zutritt, Umweltrisiken)
- Hardware (Diebstahl, Zerstörung)

**Compliance-Risiken:**
- Regulatorische Anforderungen (DSGVO, NIS2, etc.)
- Vertragliche Verpflichtungen

### 3.2 Bedrohungsquellen

**Externe Bedrohungen:**
- Cyberkriminelle (Ransomware, Phishing, DDoS)
- Hacktivisten
- Nationalstaaten (APT)
- Wettbewerber

**Interne Bedrohungen:**
- Insider (böswillig oder fahrlässig)
- Menschliche Fehler
- Prozessfehler

**Umweltbedrohungen:**
- Naturkatastrophen (Feuer, Wasser, Sturm)
- Infrastrukturausfälle (Strom, Kühlung)

## 4. Risikobewertung

### 4.1 Bewertungsskalen

**Wahrscheinlichkeit (Likelihood):**

| Stufe | Beschreibung | Häufigkeit |
|-------|--------------|------------|
| 1 | Sehr unwahrscheinlich | < 1 in 10 Jahren |
| 2 | Unwahrscheinlich | 1 in 5-10 Jahren |
| 3 | Möglich | 1 in 1-5 Jahren |
| 4 | Wahrscheinlich | 1-5 mal pro Jahr |
| 5 | Sehr wahrscheinlich | > 5 mal pro Jahr |

**Auswirkung (Impact):**

| Stufe | Beschreibung | Finanziell | Reputation | Compliance |
|-------|--------------|------------|------------|------------|
| 1 | Vernachlässigbar | < 10k € | Keine | Keine |
| 2 | Gering | 10-50k € | Lokal | Kleinere Verstöße |
| 3 | Mittel | 50-250k € | Regional | Meldepflichtig |
| 4 | Hoch | 250k-1M € | National | Bußgelder |
| 5 | Sehr hoch | > 1M € | International | Geschäftsverbot |

**Risikoscore:** Wahrscheinlichkeit × Auswirkung

**Risikostufen:**

| Score | Risikostufe | Farbe | Behandlung |
|-------|-------------|-------|------------|
| 1-2 | Sehr niedrig | Grün | Monitoring |
| 3-6 | Niedrig | Grün | Monitoring |
| 7-12 | Mittel | Gelb | Behandlung empfohlen |
| 13-20 | Hoch | Orange | Behandlung erforderlich |
| 21-25 | Sehr hoch | Rot | Sofortige Behandlung |

### 4.2 Behandlungsstrategien

**Vermeiden (Avoid):**
- Aktivität einstellen, die das Risiko verursacht
- Beispiel: Verzicht auf risikoreiche Technologie

**Mindern (Mitigate):**
- Maßnahmen zur Reduzierung von Wahrscheinlichkeit oder Auswirkung
- Beispiel: Implementierung von Controls (Firewall, MFA, Verschlüsselung)

**Übertragen (Transfer):**
- Risiko auf Dritte übertragen
- Beispiel: Cyber-Versicherung, Outsourcing mit SLA

**Akzeptieren (Accept):**
- Bewusste Entscheidung, Risiko zu tragen
- Nur für niedrige/mittlere Risiken nach Genehmigung
- Siehe `0070_ISMS_Risikoakzeptanzkriterien.md`

## 5. Risiko-Eigentümer und Verantwortlichkeiten

### 5.1 Risiko-Eigentümer (Risk Owner)

**Verantwortlichkeiten:**
- Verantwortlich für Risikobehandlung
- Entscheidung über Behandlungsstrategie
- Überwachung der Maßnahmenumsetzung
- Regelmäßige Risikobewertung

**Typische Risiko-Eigentümer:**
- **CISO:** Übergreifende Sicherheitsrisiken
- **CIO:** IT-Infrastruktur-Risiken
- **Asset Owner:** Asset-spezifische Risiken
- **Process Owner:** Prozess-spezifische Risiken

### 5.2 RACI-Matrix: Risikomanagement

| Aktivität | CISO | ISMS Manager | Risk Owner | IT-Betrieb |
|-----------|------|--------------|------------|------------|
| Risiko identifizieren | A | R | C | C |
| Risiko bewerten | A | R | C | C |
| Behandlung planen | A | C | R | C |
| Maßnahmen umsetzen | A | C | R | R |
| Risiko überwachen | A | R | C | C |
| Risikoregister pflegen | A | R | C | I |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 6. Risiko-Reporting

### 6.1 Regelmäßiges Reporting

**Quartalsweise:**
- Risiko-Dashboard an Informationssicherheitsgremium
- Anzahl Risiken nach Stufe
- Trend der Risikoscores
- Status der Risikobehandlung

**Jährlich:**
- Vollständiger Risikobericht im Management Review
- Siehe `0140_ISMS_Management_Review_Template.md`

### 6.2 Ad-hoc-Reporting

**Trigger:**
- Neue kritische Risiken (Score ≥ 13)
- Wesentliche Änderung bestehender Risiken
- Security Incidents mit Risikorelevanz

**Eskalation:**
- Hohe Risiken: Sofortige Meldung an CISO und CIO
- Sehr hohe Risiken: Sofortige Meldung an Geschäftsführung

## 7. Risiko-Review und Aktualisierung

### 7.1 Regelmäßiger Review

**Quartalsweise:**
- Review aller aktiven Risiken
- Aktualisierung von Bewertungen
- Status-Update der Maßnahmen
- Review akzeptierter Risiken

**Jährlich:**
- Vollständige Risikoanalyse
- Identifikation neuer Risiken
- Archivierung geschlossener Risiken

### 7.2 Trigger für außerplanmäßigen Review

**Externe Trigger:**
- Neue Bedrohungen (Zero-Day-Exploits, neue Malware)
- Neue Schwachstellen (CVE-Veröffentlichungen)
- Änderung der Bedrohungslage
- Neue Compliance-Anforderungen

**Interne Trigger:**
- Security Incidents
- Audit-Findings
- Wesentliche organisatorische Änderungen
- Neue Assets oder Prozesse

## 8. Verknüpfungen und Referenzen

### 8.1 Verknüpfung zu anderen ISMS-Dokumenten

**Risikobehandlungsplan (RTP):**
- Jedes Risiko mit Behandlung "Mindern" hat Maßnahmen im RTP
- Siehe `0090_ISMS_Risikobehandlungsplan_RTP_Template.md`

**Statement of Applicability (SoA):**
- Controls im SoA sind basierend auf Risikoanalyse ausgewählt
- Siehe `0100_ISMS_Statement_of_Applicability_SoA_Template.md`

**Asset-Inventar:**
- Risiken sind mit Assets verknüpft
- Siehe `0720_Anhang_Asset_und_Systeminventar_Template.md`

**Incident Reports:**
- Incidents können neue Risiken identifizieren
- Siehe `0400_Policy_Incident_Management.md`

### 8.2 Interne Dokumente

- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management Methodology
- `0070_ISMS_Risikoakzeptanzkriterien.md` - Risk Acceptance Criteria
- `0090_ISMS_Risikobehandlungsplan_RTP_Template.md` - Risk Treatment Plan
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA

### 8.3 Externe Standards

- **ISO/IEC 27001:2022** - Clause 6.1.2: Information security risk assessment
- **ISO/IEC 27005:2022** - Information security risk management
- **NIST SP 800-30** - Guide for Conducting Risk Assessments

## Änderungshistorie

| Version | Datum | Autor | Beschreibung | Genehmigt durch |
|---------|-------|-------|--------------|-----------------|
| 1.0 | [TODO] | [TODO] | Initiale Version | {{ meta-handbook.management_ceo }} |

**Genehmigt durch:**  
[TODO], CISO  
Datum: [TODO]

**Nächster Review:** [TODO] (Quartalsweise)

