# BSI IT-Grundschutz-Handbuch-Templates (Deutsch)

## Übersicht

Diese Templates bilden die Grundlage für ein vollständiges IT-Sicherheitshandbuch nach **BSI IT-Grundschutz** (BSI Standards 200-1, 200-2, 200-3) und dem **BSI IT-Grundschutz-Kompendium**.

Das IT-Sicherheitshandbuch der [TODO] umfasst ca. 40 strukturierte Dokumente, die alle wesentlichen Aspekte eines Informationssicherheits-Managementsystems (ISMS) nach BSI IT-Grundschutz abdecken.

## Template-Struktur

### ISMS Foundation (Grundlagen, 0010-0110)

| Dokument-ID | Titel | Beschreibung | BSI Standard |
|------||||
| BSI-0010 | Informationssicherheitsleitlinie | Top-Management-Policy für Informationssicherheit | BSI 200-1 |
| BSI-0020 | ISMS-Organisation, Rollen, RACI | Organisationsstruktur und Verantwortlichkeiten | BSI 200-1 |
| BSI-0030 | Dokumentenlenkung und Dokumentenregister | Versionierung, Freigabe und Pflege der ISMS-Dokumentation | BSI 200-1 |
| BSI-0040 | Geltungsbereich und Informationsverbund | Definition des ISMS-Scope | BSI 200-2 |
| BSI-0050 | Strukturanalyse | Erfassung aller relevanten Objekte | BSI 200-2 |
| BSI-0060 | Schutzbedarfsfeststellung | Bewertung von Vertraulichkeit, Integrität, Verfügbarkeit | BSI 200-2 |
| BSI-0070 | Modellierung und Bausteinzuordnung | Zuordnung von BSI-Bausteinen | BSI 200-2 |
| BSI-0080 | Basis-Sicherheitscheck (Gap-Analyse) | Soll-Ist-Vergleich der Maßnahmen | BSI 200-2 |
| BSI-0090 | Risikoanalyse nach BSI 200-3 | Risikoanalyse für zusätzlichen Schutzbedarf | BSI 200-3 |
| BSI-0100 | Sicherheitskonzept und Maßnahmenplan | Konsolidiertes Sicherheitskonzept | BSI 200-2 |
| BSI-0110 | Umsetzungssteuerung, Reporting, KPIs | Steuerung und Überwachung der Umsetzung | BSI 200-1 |

### Security Policies and Guidelines (Richtlinien, 0200-0530)

Die Sicherheitsrichtlinien sind in Policy-Richtlinien-Paare organisiert:
- **Policies (gerade Nummern, 0200-0520):** Abstrakte, strategische Grundsätze
- **Richtlinien (ungerade Nummern, 0210-0530):** Konkrete Implementierungsanweisungen

| Policy-ID | Policy-Titel | Richtlinien-ID | Richtlinien-Titel | BSI Bausteine |
|----||--|-----|-|
| BSI-0200 | Policy: Zugriffssteuerung und Berechtigungen | BSI-0210 | Richtlinie: IAM Joiner Mover Leaver und Rezertifizierung | ORP.4, OPS.1.1.2 |
| BSI-0220 | Policy: Authentisierung und MFA | BSI-0230 | Richtlinie: Passwort, MFA und Sitzungsregeln | ORP.4, OPS.1.1.5 |
| BSI-0240 | Policy: Asset und Inventarmanagement | BSI-0250 | Richtlinie: Asset Lifecycle, Tagging und Entsorgung | OPS.1.1.1, OPS.1.2.7 |
| BSI-0260 | Policy: Konfiguration und Hardening | BSI-0270 | Richtlinie: Sicherheitsbaselines und Abweichungsmanagement | SYS.1.1, SYS.2.1 |
| BSI-0280 | Policy: Patch und Vulnerability Management | BSI-0290 | Richtlinie: Scans, Patching und Exploitation Response | OPS.1.1.3 |
| BSI-0300 | Policy: Logging, Monitoring und Detektion | BSI-0310 | Richtlinie: Log Standards, SIEM, Use Cases und Retention | OPS.1.1.5, DER.1 |
| BSI-0320 | Policy: Incident Management | BSI-0330 | Richtlinie: Incident Response, Eskalation und Forensik | DER.2.1 |
| BSI-0340 | Policy: Kryptografie und Key Management | BSI-0350 | Richtlinie: Verschlüsselung, Key Rotation und Zertifikate | CON.1 |
| BSI-0360 | Policy: Sichere Softwareentwicklung | BSI-0370 | Richtlinie: Secure SDLC, Code Reviews, SAST, DAST, Secrets | CON.8 |
| BSI-0380 | Policy: Change und Release Management | BSI-0390 | Richtlinie: Change, Freigaben und Sicherheitschecks | OPS.1.1.3 |
| BSI-0400 | Policy: Lieferanten und Auslagerungsmanagement | BSI-0410 | Richtlinie: Third-Party Risk Assessment und Vertragsklauseln | OPS.2.1, OPS.2.2 |
| BSI-0420 | Policy: Datenschutz und Datenhandling | BSI-0430 | Richtlinie: Datenklassifizierung, Labeling und Weitergabe | CON.2, CON.3 |
| BSI-0440 | Policy: Backup und Wiederherstellung | BSI-0450 | Richtlinie: Backup, Restore und regelmäßige Tests | CON.3 |
| BSI-0460 | Policy: Netzwerk und Kommunikationssicherheit | BSI-0470 | Richtlinie: Segmentierung, Firewalling, VPN und Admin-Zugänge | NET.1.1, NET.1.2 |
| BSI-0480 | Policy: Endpoint und Mobile Security | BSI-0490 | Richtlinie: MDM, EDR, Device Compliance und Remote Work | SYS.2.1, SYS.3.2.2 |
| BSI-0500 | Policy: Physische Sicherheit | BSI-0510 | Richtlinie: Zutritt, Besucher und Schutz von Equipment | INF.1, INF.2 |
| BSI-0520 | Policy: Ausnahmenprozess und Risikoakzeptanz | BSI-0530 | Richtlinie: Ausnahmen, Risk Waiver und Review | - |

### Management Processes (Management-Prozesse, 0600-0630)

| Dokument-ID | Titel | Beschreibung | BSI Standard |
|------||||
| BSI-0600 | Schulung und Awareness-Programm | Sensibilisierung und Schulung | BSI 200-1, ORP.3 |
| BSI-0610 | Internes Auditprogramm | ISMS-Audits und Kontrollen | BSI 200-1 |
| BSI-0620 | Managementbewertung (Management Review) | Bewertung durch Top-Management | BSI 200-1 |
| BSI-0630 | Nichtkonformitäten und Korrekturmaßnahmen | Behandlung von Abweichungen | BSI 200-1 |

### Appendices (Anhänge, 0700-0740)

| Dokument-ID | Titel | Beschreibung |
|------|||
| BSI-0700 | Anhang: Nachweisregister (Evidence) | Register aller Nachweise und Evidenzen |
| BSI-0710 | Anhang: Assetinventar | Vollständiges Asset-Inventar |
| BSI-0720 | Anhang: Datenflüsse und Schnittstellen | Dokumentation aller Datenflüsse |
| BSI-0730 | Anhang: Diagramme, Netzplan und Zonen | Netzwerkdiagramme und Zonierung |
| BSI-0740 | Anhang: Begriffe und Abkürzungen | Glossar |

## Platzhalter-Verwendung

### Meta-Platzhalter (Organisationsdaten)

Die Templates verwenden Platzhalter aus der `metadata.yaml` Datei:

```markdown
**Organisation:** [TODO]
**CEO:** {{ meta.ceo.name }} ({{ meta.ceo.email }})
**CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
**CISO/ISB:** {{ meta.ciso.name }} ({{ meta.ciso.email }})
**Dokumentverantwortlicher:** [TODO]
**Standorte:** [TODO]
```

### NetBox-Platzhalter (Infrastrukturdaten)

Für IT-spezifische Informationen können NetBox-Platzhalter verwendet werden:

```markdown
**Standort:** {{ netbox.site.name }}
**Rechenzentrum:** {{ netbox.site.datacenter.name }}
**Core Switch:** {{ netbox.device.core_switch.name }}
**Management VLAN:** {{ netbox.vlan.management }}
**Server:** {{ netbox.device.server_001 }}
**IP-Adresse:** {{ netbox.ip.server_001 }}
```

### [TODO]-Markierungen

Alle Templates enthalten `[TODO]`-Markierungen für organisationsspezifische Anpassungen:

```markdown
**Kritisches System:** [TODO: Name des Systems]
**Schutzbedarf:** [TODO: Hoch/Mittel/Niedrig]
**Verantwortlicher:** [TODO: Name]
**BSI Baustein:** [TODO: z.B. SYS.1.1]
```

## BSI Standards Compliance-Mapping

### BSI Standard 200-1: ISMS-Anforderungen

| BSI 200-1 Kapitel | BSI-Dokument | Beschreibung |
|-----|||
| 4 Aufbau eines ISMS | BSI-0010, BSI-0020 | Leitlinie und Organisation |
| 5 ISMS-Prozess | BSI-0040 bis BSI-0110 | Strukturanalyse bis Umsetzungssteuerung |
| 6 Dokumentation | BSI-0030 | Dokumentenlenkung |
| 7 Rollen im ISMS | BSI-0020 | RACI-Matrizen |
| 8 Ressourcen | BSI-0020 | Ressourcenplanung |
| 9 Schulung und Sensibilisierung | BSI-0600 | Awareness-Programm |
| 10 Aufrechterhaltung und Verbesserung | BSI-0610, BSI-0620, BSI-0630 | Audits, Reviews, Korrekturmaßnahmen |

### BSI Standard 200-2: IT-Grundschutz-Methodik

| BSI 200-2 Kapitel | BSI-Dokument | Beschreibung |
|-----|||
| 4 Festlegung des Geltungsbereichs | BSI-0040 | Informationsverbund |
| 5 Strukturanalyse | BSI-0050 | Erfassung aller Objekte |
| 6 Schutzbedarfsfeststellung | BSI-0060 | Bewertung CIA |
| 7 Modellierung | BSI-0070 | Bausteinzuordnung |
| 8 IT-Grundschutz-Check | BSI-0080 | Gap-Analyse |
| 9 Risikoanalyse | BSI-0090 | Zusätzlicher Schutzbedarf |
| 10 Konsolidierung | BSI-0100 | Sicherheitskonzept |
| 11 Umsetzung | BSI-0110 | Maßnahmenumsetzung |

### BSI Standard 200-3: Risikoanalyse

| BSI 200-3 Kapitel | BSI-Dokument | Beschreibung |
|-----|||
| 4 Vorbereitung | BSI-0090 | Risikoanalyse-Vorbereitung |
| 5 Gefährdungsanalyse | BSI-0090 | Identifikation von Gefährdungen |
| 6 Risikoeinschätzung | BSI-0090 | Bewertung von Risiken |
| 7 Risikobehandlung | BSI-0100 | Maßnahmenplanung |

## BSI IT-Grundschutz-Kompendium Baustein-Mapping

### Prozess-Bausteine (ORP, OPS, DER)

| Baustein | Titel | BSI-Dokumente |
|---||-|
| ORP.1 | Organisation | BSI-0020 |
| ORP.2 | Personal | BSI-0600 |
| ORP.3 | Sensibilisierung und Schulung | BSI-0600 |
| ORP.4 | Identitäts- und Berechtigungsmanagement | BSI-0200, BSI-0210, BSI-0220, BSI-0230 |
| ORP.5 | Compliance Management | BSI-0630 |
| OPS.1.1.1 | Ordnungsgemäße IT-Administration | BSI-0240, BSI-0250 |
| OPS.1.1.2 | Ordnungsgemäße IT-Administration | BSI-0200, BSI-0210 |
| OPS.1.1.3 | Patch- und Änderungsmanagement | BSI-0280, BSI-0290, BSI-0380, BSI-0390 |
| OPS.1.1.5 | Protokollierung | BSI-0300, BSI-0310 |
| OPS.1.2.7 | Verkauf/Aussonderung von IT | BSI-0240, BSI-0250 |
| OPS.2.1 | Outsourcing für Kunden | BSI-0400, BSI-0410 |
| OPS.2.2 | Cloud-Nutzung | BSI-0400, BSI-0410 |
| DER.1 | Detektion von sicherheitsrelevanten Ereignissen | BSI-0300, BSI-0310 |
| DER.2.1 | Behandlung von Sicherheitsvorfällen | BSI-0320, BSI-0330 |

### System-Bausteine (SYS, NET, INF)

| Baustein | Titel | BSI-Dokumente |
|---||-|
| SYS.1.1 | Allgemeiner Server | BSI-0260, BSI-0270 |
| SYS.2.1 | Allgemeiner Client | BSI-0260, BSI-0270, BSI-0480, BSI-0490 |
| SYS.3.2.2 | Mobile Device Management | BSI-0480, BSI-0490 |
| NET.1.1 | Netzarchitektur und -design | BSI-0460, BSI-0470 |
| NET.1.2 | Netzmanagement | BSI-0460, BSI-0470 |
| INF.1 | Allgemeines Gebäude | BSI-0500, BSI-0510 |
| INF.2 | Rechenzentrum sowie Serverraum | BSI-0500, BSI-0510 |

### Konzept-Bausteine (CON)

| Baustein | Titel | BSI-Dokumente |
|---||-|
| CON.1 | Kryptokonzept | BSI-0340, BSI-0350 |
| CON.2 | Datenschutz | BSI-0420, BSI-0430 |
| CON.3 | Datensicherungskonzept | BSI-0440, BSI-0450 |
| CON.8 | Software-Entwicklung | BSI-0360, BSI-0370 |

## HTML-Kommentare für Template-Autoren

Die Templates enthalten HTML-Kommentare mit Hinweisen für Template-Autoren:

```markdown
<!-- 
TEMPLATE AUTHOR NOTE:
This template guides the structure analysis according to BSI IT-Grundschutz Standard 200-2.
The structure analysis captures all relevant elements of the information domain.
Reference: BSI Standard 200-2 (Chapter 5: Structure Analysis)
-->
```

Diese Kommentare werden beim Generieren des Handbuchs automatisch entfernt.

## Best Practices für Anpassungen

### 1. Reihenfolge der Bearbeitung

Empfohlene Reihenfolge für die Anpassung der Templates nach BSI IT-Grundschutz-Methodik:

1. **ISMS Foundation** (0010-0040): Leitlinie, Organisation, Scope festlegen
2. **Strukturanalyse** (0050): Alle Objekte erfassen
3. **Schutzbedarfsfeststellung** (0060): CIA-Bewertung durchführen
4. **Modellierung** (0070): BSI-Bausteine zuordnen
5. **Basis-Sicherheitscheck** (0080): Gap-Analyse durchführen
6. **Risikoanalyse** (0090): Zusätzlichen Schutzbedarf ermitteln
7. **Sicherheitskonzept** (0100): Maßnahmen konsolidieren
8. **Policies und Richtlinien** (0200-0530): Detaillierte Richtlinien ausarbeiten
9. **Management-Prozesse** (0600-0630): Audits, Reviews, Schulungen planen

### 2. RACI-Matrizen

Alle RACI-Matrizen sollten vollständig ausgefüllt werden:

- **R** (Responsible): Durchführungsverantwortung
- **A** (Accountable): Gesamtverantwortung, Entscheidungsbefugnis
- **C** (Consulted): Konsultiert, Fachexpertise
- **I** (Informed): Informiert

**Regel:** Jede Aktivität muss genau ein "A" haben.

### 3. Schutzbedarfsfeststellung

Die Schutzbedarfsfeststellung erfolgt für die Grundwerte:

- **Vertraulichkeit:** Schutz vor unbefugter Offenlegung
- **Integrität:** Schutz vor unbefugter Veränderung
- **Verfügbarkeit:** Sicherstellung der Verfügbarkeit

**Kategorien:**
- **Normal:** Schadensauswirkungen sind begrenzt und überschaubar
- **Hoch:** Schadensauswirkungen können beträchtlich sein
- **Sehr hoch:** Schadensauswirkungen können ein existenziell bedrohliches, katastrophales Ausmaß erreichen

### 4. BSI-Baustein-Zuordnung

Bei der Modellierung (Dokument 0070) werden BSI-Bausteine zugeordnet:

- **Prozess-Bausteine:** ORP, OPS, DER
- **System-Bausteine:** SYS, NET, INF, IND
- **Anwendungs-Bausteine:** APP
- **Konzept-Bausteine:** CON

**Tipp:** Verwenden Sie das aktuelle BSI IT-Grundschutz-Kompendium als Referenz.

### 5. Gap-Analyse (Basis-Sicherheitscheck)

Der Basis-Sicherheitscheck (Dokument 0080) vergleicht Soll und Ist:

- **Entbehrlich:** Anforderung nicht anwendbar
- **Ja:** Anforderung vollständig umgesetzt
- **Teilweise:** Anforderung teilweise umgesetzt
- **Nein:** Anforderung nicht umgesetzt

**Ziel:** Identifikation von Umsetzungslücken für den Maßnahmenplan.

### 6. Risikoanalyse nach BSI 200-3

Die Risikoanalyse (Dokument 0090) wird durchgeführt für:

- Objekte mit zusätzlichem Schutzbedarf (sehr hoch)
- Objekte, die nicht durch IT-Grundschutz abgedeckt sind
- Objekte mit spezifischen Gefährdungen

**Methodik:** BSI Standard 200-3 (Gefährdungsanalyse, Risikoeinschätzung, Risikobehandlung)

### 7. Dokumentation von Nachweisen

Alle Nachweise (Evidence) sollten im Nachweisregister (Dokument 0700) dokumentiert werden:

- **Typ:** Dokument, Screenshot, Log, Konfiguration, Zertifikat
- **Speicherort:** Pfad oder URL
- **Verantwortlicher:** Owner des Nachweises
- **Aktualität:** Datum der letzten Aktualisierung

## Generierung des Handbuchs

### CLI-Verwendung

```bash
# Deutsches BSI Grundschutz-Handbuch generieren (Test-Modus erforderlich)
python -m src.cli --language de --template bsi-grundschutz --test

# Separate Markdown-Dateien pro Template generieren
python -m src.cli --language de --template bsi-grundschutz --test --separate-files

# PDF mit Inhaltsverzeichnis und Seitenumbrüchen generieren
python -m src.cli --language de --template bsi-grundschutz --output pdf --test --pdf-toc

# Alle Formate mit allen Features generieren
python -m src.cli --language de --template bsi-grundschutz --output all --test --separate-files --pdf-toc

# Englisches BSI Grundschutz-Handbuch generieren
python -m src.cli --language en --template bsi-grundschutz --test
```

### Ausgabeformate

Das System unterstützt mehrere Ausgabeformate:

- **Markdown (kombiniert):** Einzelne .md-Datei mit allen Kapiteln
- **Markdown (separate Dateien):** Separate .md-Dateien für jedes Kapitel mit TOC.md
- **PDF (Standard):** Vollständiges Handbuch als PDF
- **PDF (mit TOC):** PDF mit Inhaltsverzeichnis und Seitenumbrüchen zwischen Kapiteln
- **HTML:** Mini-Website mit Navigation zwischen Seiten

Weitere Details zu allen Ausgabeformaten finden Sie in der [OUTPUT_FORMATS_GUIDE.md](../../../docs/OUTPUT_FORMATS_GUIDE.md).

## Wartung und Aktualisierung

### Aktualisierungsintervalle

- **Jährlich:** Vollständige Überprüfung aller Dokumente (Management Review)
- **Quartalsweise:** Strukturanalyse, Asset-Inventar, Kontaktlisten
- **Ad-hoc:** Bei organisatorischen Änderungen, neuen Systemen, Sicherheitsvorfällen

### Versionierung

Verwenden Sie semantische Versionierung:

- **MAJOR:** Grundlegende Änderungen der ISMS-Struktur oder Scope
- **MINOR:** Ergänzungen und Aktualisierungen (neue Bausteine, Richtlinien)
- **PATCH:** Korrekturen und redaktionelle Änderungen

### BSI IT-Grundschutz-Kompendium Updates

Das BSI IT-Grundschutz-Kompendium wird regelmäßig aktualisiert:

- **Jährlich:** Neue Edition des Kompendiums
- **Laufend:** Aktualisierung einzelner Bausteine

**Empfehlung:** Überprüfen Sie jährlich, ob neue oder aktualisierte Bausteine relevant sind.

## Zertifizierung nach ISO 27001 auf Basis von IT-Grundschutz

Die BSI IT-Grundschutz-Templates unterstützen die Zertifizierung nach ISO 27001 auf Basis von IT-Grundschutz:

- **ISO 27001-Zertifizierung:** Internationale Anerkennung
- **IT-Grundschutz-Zertifizierung:** BSI-Zertifizierung (nur für deutsche Organisationen)

**Mapping:** Die Templates enthalten Referenzen zu ISO 27001:2022 Klauseln, wo relevant.

## Support und Feedback

Bei Fragen oder Problemen:

- **Dokumentation:** Siehe Haupt-README.md
- **BSI-Ressourcen:** https://www.bsi.bund.de/grundschutz
- **Issues:** GitHub Issues für Fehlerberichte
- **Contributions:** Pull Requests willkommen

## Weiterführende Ressourcen

- **BSI IT-Grundschutz-Kompendium:** https://www.bsi.bund.de/kompendium
- **BSI Standards 200-1, 200-2, 200-3:** https://www.bsi.bund.de/standards
- **BSI Grundschutz-Tools:** GSTOOL, verinice
- **ISO 27001:2022:** Internationale Norm für ISMS

---

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2026-02-03  
**Maintainer:** BSI-Grundschutz-Template-Team
