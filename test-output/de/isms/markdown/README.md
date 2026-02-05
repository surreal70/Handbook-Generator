# ISMS-Handbuch-Templates (Deutsch)

## Übersicht

Diese Templates bilden die Grundlage für ein vollständiges Information Security Management System (ISMS) Handbuch nach **ISO/IEC 27001:2022** (inkl. **Amendment 1:2024**).

Das ISMS-Handbuch der AdminSend GmbH umfasst ca. 50 strukturierte Dokumente, die alle wesentlichen Aspekte des Informationssicherheitsmanagements abdecken. Die Templates folgen einer **Drei-Ebenen-Architektur**, die strategische, abstrakte und operative Dokumentation klar trennt.

## Drei-Ebenen-Architektur

Das ISMS-Handbuch ist in drei hierarchische Ebenen strukturiert:

### Ebene 1: Basis-ISMS (Foundation)
Strategische Dokumente, die den Rahmen und die Grundlagen des ISMS definieren.

### Ebene 2: Abstract Policies
High-Level-Sicherheitsrichtlinien, die Grundsätze und Anforderungen festlegen.

### Ebene 3: Detailed Guidelines
Detaillierte Implementierungsrichtlinien mit konkreten Verfahren und technischen Kontrollen.

Diese Struktur ermöglicht:
- **Klare Trennung** zwischen strategischer und operativer Dokumentation
- **Flexibilität** bei der Anpassung operativer Details ohne Änderung strategischer Vorgaben
- **Skalierbarkeit** für unterschiedliche Organisationsgrößen
- **Compliance** mit ISO 27001:2022 Anforderungen

## Template-Struktur

### Ebene 1: Basis-ISMS (0010-0160)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| ISMS-0010 | Informationssicherheitsleitlinie | Top-Level ISMS Policy, Management Commitment |
| ISMS-0020 | Geltungsbereich (Scope) | ISMS Scope Definition, Boundaries |
| ISMS-0030 | Kontext und Interessierte Parteien | Context of Organization, Stakeholders |
| ISMS-0040 | Governance, Rollen und Verantwortlichkeiten | ISMS Governance Structure, RACI Matrices |
| ISMS-0050 | Dokumentenlenkung | Document Control, Version Management |
| ISMS-0060 | Risikomanagement-Methodik | Risk Management Methodology |
| ISMS-0070 | Risikoakzeptanzkriterien | Risk Acceptance Criteria |
| ISMS-0080 | Risikoregister (Template) | Risk Register Template |
| ISMS-0090 | Risikobehandlungsplan (RTP) | Risk Treatment Plan Template |
| ISMS-0100 | Statement of Applicability (SoA) | SoA Template mit Annex A Controls |
| ISMS-0110 | Sicherheitsziele und Metriken | Security Objectives, KPIs |
| ISMS-0120 | Schulung, Awareness und Kompetenz | Training and Awareness Program |
| ISMS-0130 | Internes Auditprogramm | Internal Audit Program |
| ISMS-0140 | Management Review (Template) | Management Review Template |
| ISMS-0150 | Nichtkonformitäten und Korrekturmaßnahmen | Non-conformities, Corrective Actions |
| ISMS-0160 | Kontinuierliche Verbesserung | Continuous Improvement Process |

### Ebene 2: Abstract Policies (0200-0680, gerade Nummern)

High-Level-Sicherheitsrichtlinien für 25 Themenbereiche:

| Dokument-ID | Titel | Annex A Mapping |
|-------------|-------|-----------------|
| ISMS-0200 | Policy: Akzeptable Nutzung IT | A.5.10 |
| ISMS-0220 | Policy: Zugriffssteuerung und Identitätsmanagement | A.5.15, A.5.16, A.5.18 |
| ISMS-0240 | Policy: Authentisierung und Passwörter | A.5.17, A.8.5 |
| ISMS-0260 | Policy: Kryptografie und Schlüsselmanagement | A.8.24 |
| ISMS-0280 | Policy: Datenklassifizierung und Informationshandling | A.5.9, A.5.10, A.5.12 |
| ISMS-0300 | Policy: Asset Management | A.5.9, A.5.11 |
| ISMS-0320 | Policy: Logging und Monitoring | A.8.15, A.8.16 |
| ISMS-0340 | Policy: Vulnerability und Patch Management | A.8.8 |
| ISMS-0360 | Policy: Change und Release Management | A.8.32 |
| ISMS-0380 | Policy: Secure Development | A.8.25, A.8.26, A.8.27, A.8.28 |
| ISMS-0400 | Policy: Incident Management | A.5.24, A.5.25, A.5.26, A.6.8 |
| ISMS-0420 | Policy: Backup und Wiederherstellung | A.8.13 |
| ISMS-0440 | Policy: Business Continuity / ICT Readiness | A.5.29, A.5.30 |
| ISMS-0460 | Policy: Lieferanten und Cloud-Sicherheit | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 |
| ISMS-0480 | Policy: Physische Sicherheit | A.7.1, A.7.2, A.7.3, A.7.4 |
| ISMS-0500 | Policy: Mobile Device und Remote Work | A.6.7, A.7.9, A.8.1 |
| ISMS-0520 | Policy: HR Security | A.6.1, A.6.2, A.6.4, A.6.5, A.6.6 |
| ISMS-0540 | Policy: Konfiguration und Hardening | A.8.9, A.8.18, A.8.19 |
| ISMS-0560 | Policy: Datenschutz-Schnittstellen | A.5.34, A.5.36 |
| ISMS-0580 | Policy: Aufbewahrung und Löschung | A.5.10, A.7.14, A.8.10, A.8.11 |
| ISMS-0600 | Policy: Netzwerksicherheit | A.8.20, A.8.21, A.8.22, A.8.23 |
| ISMS-0620 | Policy: Endpoint Security | A.8.1, A.8.7 |
| ISMS-0640 | Policy: Ausnahmen und Risk Waivers | A.5.1 (Ausnahmenprozess) |
| ISMS-0660 | Policy: Informationsübertragung und Kommunikation | A.5.13, A.5.14 |
| ISMS-0680 | Policy: Security in Projects | A.5.8 |

### Ebene 3: Detailed Guidelines (0210-0690, ungerade Nummern)

Detaillierte Implementierungsrichtlinien für jede Policy:

| Dokument-ID | Titel | Zugehörige Policy |
|-------------|-------|-------------------|
| ISMS-0210 | Richtlinie: Akzeptable Nutzung IT | 0200 |
| ISMS-0230 | Richtlinie: IAM, Joiner-Mover-Leaver, Zugriffsanträge | 0220 |
| ISMS-0250 | Richtlinie: MFA, Passwortregeln, Session Management | 0240 |
| ISMS-0270 | Richtlinie: Key Management und Verschlüsselung | 0260 |
| ISMS-0290 | Richtlinie: Datenklassifizierung, Labeling, Handling | 0280 |
| ISMS-0310 | Richtlinie: Asset Inventory, Tagging, Entsorgung | 0300 |
| ISMS-0330 | Richtlinie: Logging, SIEM, Audit Trails | 0320 |
| ISMS-0350 | Richtlinie: Vulnerability Scans, Patching, Exploitation Response | 0340 |
| ISMS-0370 | Richtlinie: Change Management mit Sicherheitsfreigaben | 0360 |
| ISMS-0390 | Richtlinie: Secure SDLC, Coding Review, Secrets | 0380 |
| ISMS-0410 | Richtlinie: Incident Response und Major Incident Prozess | 0400 |
| ISMS-0430 | Richtlinie: Backup, Restore, Regelmäßige Tests | 0420 |
| ISMS-0450 | Richtlinie: ICT DR, Schnittstellen zu BCM | 0440 |
| ISMS-0470 | Richtlinie: Third-Party Risk Assessment, Cloud Controls | 0460 |
| ISMS-0490 | Richtlinie: Zutritt, Besucher, Schutz von Equipment | 0480 |
| ISMS-0510 | Richtlinie: MDM, BringYourOwnDevice, Remote Access | 0500 |
| ISMS-0530 | Richtlinie: HR Onboarding, Rollenwechsel, Offboarding | 0520 |
| ISMS-0550 | Richtlinie: Sicherheitsbaselines, Hardening, Konfig-Änderungen | 0540 |
| ISMS-0570 | Richtlinie: Datenschutz-Anforderungen, Datenverarbeitung | 0560 |
| ISMS-0590 | Richtlinie: Records Retention, Sichere Löschung | 0580 |
| ISMS-0610 | Richtlinie: Segmentierung, Firewalling, Network Access Control | 0600 |
| ISMS-0630 | Richtlinie: EDR, AV, Host Firewall, Device Compliance | 0620 |
| ISMS-0650 | Richtlinie: Ausnahmenprozess | 0640 |
| ISMS-0670 | Richtlinie: E-Mail, Sharing, Zusammenarbeitstools | 0660 |
| ISMS-0690 | Richtlinie: Sicherheitsanforderungen im Projektlebenszyklus | 0680 |

### Anhänge (0710-0740)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| ISMS-0710 | Anhang: Annex A Mapping | Vollständiges Mapping aller 93 Annex A Controls |
| ISMS-0720 | Anhang: Asset- und Systeminventar | Asset Inventory Template |
| ISMS-0730 | Anhang: Datenflüsse und Schnittstellen | Data Flow Diagrams |
| ISMS-0740 | Anhang: Begriffe und Abkürzungen | Glossar |

## Platzhalter-Verwendung

### Meta-Platzhalter (Organisationsdaten)

Die Templates verwenden Platzhalter aus der `metadata.yaml` Datei:

```markdown
**Organisation:** AdminSend GmbH
**CEO:** {{ meta.management.ceo }}
**CIO:** Anna Schmidt (anna.schmidt@adminsend.de)
**CISO:** Thomas Weber (thomas.weber@adminsend.de)
**Dokumentverantwortlicher:** IT Operations Manager
**Datum:** {{ meta.document.date }}
**Nächster Review:** {{ meta.document.next_review }}
```

### NetBox-Platzhalter (Infrastrukturdaten)

Für IT-spezifische Informationen können NetBox-Platzhalter verwendet werden:

```markdown
**Standort:** {{ netbox.site.name }}
**Rechenzentrum:** {{ netbox.site.datacenter.name }}
**Core Switch:** {{ netbox.device.core_switch.name }}
**Management VLAN:** {{ netbox.vlan.management.vid }}
```

### [TODO]-Markierungen

Alle Templates enthalten `[TODO]`-Markierungen für organisationsspezifische Anpassungen:

```markdown
**Kritisches System:** [TODO: Name des Systems]
**RTO:** [TODO: 4 Stunden]
**Sicherheitstool:** {{ meta.security.edr_solution }} [TODO: z.B. CrowdStrike, SentinelOne]
```

## ISO 27001:2022 Compliance-Mapping

### Hauptklauseln

| ISO 27001 Klausel | ISMS-Dokument | Beschreibung |
|-------------------|---------------|--------------|
| 4.1 Understanding the organization | ISMS-0030 | Kontext der Organisation |
| 4.2 Understanding needs of interested parties | ISMS-0030 | Interessierte Parteien |
| 4.3 Determining the scope | ISMS-0020 | ISMS Scope |
| 4.4 Information security management system | ISMS-0010, ISMS-0040 | ISMS Establishment |
| 5.1 Leadership and commitment | ISMS-0010 | Management Commitment |
| 5.2 Policy | ISMS-0010 | Information Security Policy |
| 5.3 Organizational roles | ISMS-0040 | Roles and Responsibilities |
| 6.1.1 General (Risk assessment) | ISMS-0060, ISMS-0080 | Risk Management |
| 6.1.2 Information security risk assessment | ISMS-0060, ISMS-0080 | Risk Assessment |
| 6.1.3 Information security risk treatment | ISMS-0090 | Risk Treatment Plan |
| 6.1.3 d) Statement of Applicability | ISMS-0100 | SoA |
| 6.2 Information security objectives | ISMS-0110 | Security Objectives |
| 7.2 Competence | ISMS-0120 | Training and Awareness |
| 7.5 Documented information | ISMS-0050 | Document Control |
| 8.1 Operational planning and control | ISMS-0090, ISMS-0100 | Operational Controls |
| 9.1 Monitoring, measurement, analysis | ISMS-0110 | Performance Evaluation |
| 9.2 Internal audit | ISMS-0130 | Internal Audit |
| 9.3 Management review | ISMS-0140 | Management Review |
| 10.1 Nonconformity and corrective action | ISMS-0150 | Corrective Actions |
| 10.2 Continual improvement | ISMS-0160 | Continuous Improvement |

### Annex A Controls (93 Controls)

**Vollständiges Mapping:** Siehe `0710_Anhang_AnnexA_Mapping_Template.md`

**Kategorien:**
- **Organisational Controls (5.x):** 37 Controls → Policies 0200-0680
- **People Controls (6.x):** 8 Controls → Policy 0520, Richtlinie 0530
- **Physical Controls (7.x):** 14 Controls → Policy 0480, Richtlinie 0490
- **Technological Controls (8.x):** 34 Controls → Policies 0220-0640

**Amendment 1:2024:**
- Berücksichtigt Änderungen aus Amendment 1:2024
- Aktualisierte Control-Beschreibungen
- Neue Attribute (Control Type, Information Security Properties, Cybersecurity Concepts, Operational Capabilities, Security Domains)

## HTML-Kommentare für Template-Autoren

Die Templates enthalten HTML-Kommentare mit Hinweisen für Template-Autoren:

```markdown

```

Diese Kommentare werden beim Generieren des Handbuchs automatisch entfernt.

## Best Practices für Anpassungen

### 1. Reihenfolge der Bearbeitung

Empfohlene Reihenfolge für die Anpassung der Templates:

**Phase 1: Foundation (Woche 1-2)**
1. **ISMS-0010:** Informationssicherheitsleitlinie anpassen
2. **ISMS-0020:** ISMS Scope definieren
3. **ISMS-0030:** Kontext und Stakeholder identifizieren
4. **ISMS-0040:** Governance-Struktur und Rollen festlegen

**Phase 2: Risk Management (Woche 3-4)**
5. **ISMS-0060:** Risikomanagement-Methodik anpassen
6. **ISMS-0070:** Risikoakzeptanzkriterien definieren
7. **ISMS-0080:** Risikoanalyse durchführen, Risikoregister erstellen
8. **ISMS-0090:** Risikobehandlungsplan erstellen

**Phase 3: Controls Selection (Woche 5-6)**
9. **ISMS-0100:** Statement of Applicability erstellen
10. **Policies (0200-0680):** Relevante Policies auswählen und anpassen
11. **Richtlinien (0210-0690):** Detaillierte Richtlinien ausarbeiten

**Phase 4: Operations (Woche 7-8)**
12. **ISMS-0110:** Sicherheitsziele und KPIs definieren
13. **ISMS-0120:** Schulungsprogramm aufsetzen
14. **ISMS-0130:** Auditprogramm planen
15. **ISMS-0140:** Management Review etablieren

### 2. RACI-Matrizen

Alle RACI-Matrizen sollten vollständig ausgefüllt werden:

- **R** (Responsible): Durchführungsverantwortung
- **A** (Accountable): Gesamtverantwortung, Entscheidungsbefugnis (genau eine Person pro Aktivität)
- **C** (Consulted): Konsultiert, Fachexpertise
- **I** (Informed): Informiert

**Regel:** Jede Aktivität muss genau ein "A" haben.

### 3. Annex A Controls

**Auswahlkriterien:**
- **Risikobasiert:** Controls zur Behandlung identifizierter Risiken
- **Compliance:** Gesetzliche und regulatorische Anforderungen (DSGVO, NIS2, etc.)
- **Best Practices:** Branchenübliche Sicherheitsmaßnahmen
- **Stakeholder-Anforderungen:** Kunden, Partner, Aufsichtsbehörden

**Ausschlüsse dokumentieren:**
- Begründung für nicht anwendbare Controls
- Alternative Maßnahmen (falls vorhanden)
- Genehmigung durch CISO

### 4. Drei-Ebenen-Struktur nutzen

**Ebene 1 (Basis-ISMS):**
- Strategische Dokumente, selten geändert
- Management-Genehmigung erforderlich
- Jährlicher Review

**Ebene 2 (Abstract Policies):**
- High-Level-Grundsätze, stabil
- CISO-Genehmigung erforderlich
- Jährlicher Review

**Ebene 3 (Detailed Guidelines):**
- Operative Details, häufiger geändert
- IT-Betrieb/Fachbereich-Genehmigung
- Quartalsweiser Review oder bei Bedarf

**Vorteil:** Operative Änderungen erfordern keine Anpassung strategischer Dokumente.

### 5. Dokumentation von Nachweisen (Evidence)

Für jedes implementierte Control sollten Nachweise dokumentiert werden:

- **Policies und Richtlinien:** Genehmigte Dokumente
- **Technische Kontrollen:** Konfigurationsnachweise, Screenshots
- **Prozesse:** Prozessbeschreibungen, Workflows
- **Schulungen:** Teilnahmenachweise, Zertifikate
- **Audits:** Audit-Berichte, Findings, Corrective Actions
- **Monitoring:** Logs, Reports, Dashboards

**Nachweisregister:** Siehe `0700_Anhang_Nachweisregister_Evidence.md` (BSI Grundschutz)

### 6. Integration mit anderen Management-Systemen

**BCM (Business Continuity Management):**
- Policy 0440: Business Continuity / ICT Readiness
- Richtlinie 0450: ICT DR, Schnittstellen zu BCM
- Verknüpfung zu BCM-Handbuch (siehe BCM-Templates)

**Datenschutz (DSGVO):**
- Policy 0560: Datenschutz-Schnittstellen
- Richtlinie 0570: Datenschutz-Anforderungen, Datenverarbeitung
- Verknüpfung zu Datenschutz-Management-System

**IT Service Management (ITIL):**
- Policy 0360: Change und Release Management
- Policy 0400: Incident Management
- Integration mit ITSM-Tools (ServiceNow, Jira Service Management)

## Generierung des Handbuchs

### CLI-Verwendung

```bash
# Deutsches ISMS-Handbuch generieren (Test-Modus erforderlich)
python -m src.cli --language de --template isms --test

# Separate Markdown-Dateien pro Template generieren
python -m src.cli --language de --template isms --test --separate-files

# PDF mit Inhaltsverzeichnis und Seitenumbrüchen generieren
python -m src.cli --language de --template isms --output pdf --test --pdf-toc

# Alle Formate mit allen Features generieren
python -m src.cli --language de --template isms --output all --test --separate-files --pdf-toc

# Englisches ISMS-Handbuch generieren
python -m src.cli --language en --template isms --test
```

### Ausgabeformate

Das System unterstützt mehrere Ausgabeformate:

- **Markdown (kombiniert):** Einzelne .md-Datei mit allen Kapiteln
- **Markdown (separate Dateien):** Separate .md-Dateien für jedes Kapitel mit TOC.md
- **PDF (Standard):** Vollständiges Handbuch als PDF
- **PDF (mit TOC):** PDF mit Inhaltsverzeichnis und Seitenumbrüchen zwischen Kapiteln
- **HTML:** Mini-Website mit Navigation zwischen Seiten

Weitere Details zu allen Ausgabeformaten finden Sie in der [OUTPUT_FORMATS_GUIDE.md](../../../docs/OUTPUT_FORMATS_GUIDE.md).

### Konfiguration

**metadata.yaml:**
```yaml
organization:
  name: "Muster GmbH"
  
management:
  ceo: "Max Mustermann"
  
cio:
  name: "Dr. Anna Schmidt"
  email: "anna.schmidt@example.com"
  
ciso:
  name: "Thomas Müller"
  email: "thomas.mueller@example.com"
  
document:
  owner: "ISMS-Team"
  date: "2026-02-01"
  next_review: "2027-02-01"
  approval_date: "2026-02-01"
  
security:
  edr_solution: "CrowdStrike Falcon"
  siem_solution: "Microsoft Sentinel"
  web_filter: "Cisco Umbrella"
  # ... weitere Sicherheitstools
```

## Wartung und Aktualisierung

### Aktualisierungsintervalle

**Jährlich:**
- Vollständige Überprüfung aller Basis-ISMS-Dokumente (0010-0160)
- Review aller Abstract Policies (0200-0680)
- Aktualisierung des Statement of Applicability (0100)
- Management Review (0140)

**Quartalsweise:**
- Review der Detailed Guidelines (0210-0690) bei Bedarf
- Aktualisierung des Risikoregisters (0080)
- Tracking des Risikobehandlungsplans (0090)
- KPI-Review (0110)

**Ad-hoc:**
- Bei organisatorischen Änderungen (Scope, Struktur)
- Bei neuen Risiken oder Bedrohungen
- Bei Audit-Findings oder Incidents
- Bei Änderungen von Compliance-Anforderungen

### Versionierung

Verwenden Sie semantische Versionierung:

- **MAJOR:** Grundlegende Änderungen der ISMS-Struktur oder -Strategie
- **MINOR:** Ergänzungen und Aktualisierungen von Policies/Richtlinien
- **PATCH:** Korrekturen und redaktionelle Änderungen

### Change Management

Änderungen an ISMS-Dokumenten sollten über den Change-Prozess gesteuert werden:
- **Change Request:** Antrag mit Begründung
- **Impact Assessment:** Auswirkungen auf ISMS und Compliance
- **Approval:** Genehmigung durch CISO (Policies) oder Fachbereich (Richtlinien)
- **Communication:** Information an betroffene Stakeholder
- **Training:** Schulung bei wesentlichen Änderungen

## Zertifizierung und Audits

### ISO 27001:2022 Zertifizierung

**Vorbereitung:**
1. **Gap Analysis:** Vergleich IST-Zustand mit ISO 27001 Anforderungen
2. **Dokumentation:** Vollständige ISMS-Dokumentation erstellen
3. **Implementierung:** Controls gemäß SoA implementieren
4. **Internal Audit:** Internes Audit durchführen (ISMS-0130)
5. **Management Review:** Management Review durchführen (ISMS-0140)

**Zertifizierungsaudit:**
- **Stage 1:** Dokumentenprüfung, Readiness Assessment
- **Stage 2:** Vor-Ort-Audit, Interviews, Evidence-Prüfung
- **Zertifikat:** Gültig für 3 Jahre
- **Surveillance Audits:** Jährliche Überwachungsaudits

**Rezertifizierung:**
- Nach 3 Jahren vollständiges Rezertifizierungsaudit

### Interne Audits

**Auditprogramm:** Siehe ISMS-0130

**Audit-Frequenz:**
- Alle ISMS-Bereiche mindestens jährlich
- Kritische Bereiche halbjährlich
- Ad-hoc-Audits bei Bedarf

**Audit-Nachweise:**
- Audit-Pläne und -Berichte
- Findings und Corrective Actions
- Follow-up-Audits

## Support und Feedback

Bei Fragen oder Problemen:

- **Dokumentation:** Siehe Haupt-README.md
- **Issues:** GitHub Issues für Fehlerberichte
- **Contributions:** Pull Requests willkommen

## Referenzen

### Externe Standards

- **ISO/IEC 27001:2022** - Information security management systems - Requirements
- **ISO/IEC 27001:2022/Amd 1:2024** - Amendment 1 (Annex A updates)
- **ISO/IEC 27002:2022** - Information security controls (detailed guidance)
- **ISO/IEC 27005:2022** - Information security risk management
- **DSGVO (EU 2016/679)** - Datenschutz-Grundverordnung
- **NIS2-Richtlinie (EU 2022/2555)** - Network and Information Security Directive
- **BSI IT-Grundschutz** - Bundesamt für Sicherheit in der Informationstechnik

### Verwandte Template-Sets

- **BCM-Templates:** Business Continuity Management (ISO 22301)
- **BSI Grundschutz-Templates:** BSI IT-Grundschutz Standards 200-1, 200-2, 200-3
- **IT-Operation-Templates:** IT-Betriebshandbuch

---

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2026-02-02  
**Maintainer:** ISMS-Template-Team
