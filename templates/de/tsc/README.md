# TSC (SOC 2) Compliance Handbuch-Templates (Deutsch)

## Übersicht

Diese Templates bilden die Grundlage für ein vollständiges TSC (Trust Services Criteria) Compliance-Handbuch für **SOC 2-Audits**.

Das TSC-Handbuch der {{ meta.organization.name }} umfasst strukturierte Dokumente, die alle fünf Trust Services-Kategorien abdecken: Security (Common Criteria), Availability, Processing Integrity, Confidentiality und Privacy.

## Template-Struktur

### Foundation (Grundlagen, 0010-0050)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| TSC-0010 | Systembeschreibung | Beschreibung des Service-Systems und seiner Grenzen |
| TSC-0020 | System-Boundaries | Definition der System-Grenzen und Schnittstellen |
| TSC-0030 | System-Komponenten | Infrastruktur, Software, Personen, Prozesse, Daten |
| TSC-0040 | Rollen und Verantwortlichkeiten | TSC-spezifische Rollen und RACI-Matrizen |
| TSC-0050 | Control Environment | Kontrollumgebung und Governance-Struktur |

### Common Criteria - Security (Pflicht für alle SOC 2, 0100-0150)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| TSC-0100 | CC1: Control Environment | Organisationsstruktur, Integrität, Ethik |
| TSC-0110 | CC2: Communication | Kommunikation von Zielen und Verantwortlichkeiten |
| TSC-0120 | CC3: Risk Assessment | Risikobewertungsprozess |
| TSC-0130 | CC4: Monitoring | Überwachung der Kontrollwirksamkeit |
| TSC-0140 | CC5: Control Activities | Logische und physische Zugriffskontrolle |
| TSC-0150 | CC6-CC9: Security Controls | Änderungsmanagement, Operationen, Risikominderung |

### Availability Criteria (Optional, 0200-0230)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| TSC-0200 | A1.1: Availability Commitments | Verfügbarkeitszusagen und SLAs |
| TSC-0210 | A1.2: System Monitoring | Überwachung der Systemverfügbarkeit |
| TSC-0220 | A1.3: Incident Management | Incident-Response für Verfügbarkeitsprobleme |
| TSC-0230 | A1.4: Recovery Procedures | Backup und Disaster Recovery |

### Processing Integrity Criteria (Optional, 0240-0270)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| TSC-0240 | PI1.1: Processing Commitments | Zusagen zur Verarbeitungsintegrität |
| TSC-0250 | PI1.2: Input Validation | Validierung von Eingabedaten |
| TSC-0260 | PI1.3: Processing Controls | Kontrollen während der Verarbeitung |
| TSC-0270 | PI1.4: Output Controls | Kontrollen für Ausgabedaten |

### Confidentiality Criteria (Optional, 0280-0310)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| TSC-0280 | C1.1: Confidentiality Commitments | Vertraulichkeitszusagen |
| TSC-0290 | C1.2: Access Controls | Zugriffskontrolle für vertrauliche Daten |
| TSC-0300 | C1.3: Encryption | Verschlüsselung vertraulicher Daten |
| TSC-0310 | C1.4: Data Disposal | Sichere Löschung vertraulicher Daten |

### Privacy Criteria (Optional, 0320-0350)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| TSC-0320 | P1: Notice and Communication | Datenschutzhinweise |
| TSC-0330 | P2-P3: Choice and Consent | Einwilligung und Wahlmöglichkeiten |
| TSC-0340 | P4-P5: Collection and Use | Datenerhebung und -verwendung |
| TSC-0350 | P6-P8: Access, Disclosure, Quality | Zugang, Offenlegung, Datenqualität |

### Appendices (Anhänge, 0400-0450)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| TSC-0400 | Control Matrix | Vollständige TSC-Kontrollmatrix |
| TSC-0410 | Evidence Documentation | Nachweisdokumentation für Audits |
| TSC-0420 | Test Results | Ergebnisse der Kontrolltests |
| TSC-0430 | Vendor Management | Management von Subservice-Organisationen |
| TSC-0440 | Glossar | TSC-spezifische Begriffe und Abkürzungen |

## Platzhalter-Verwendung

### Meta-Platzhalter (Organisationsdaten)

Die Templates verwenden Platzhalter aus der `metadata.yaml` Datei:

```markdown
**Organisation:** {{ meta.organization.name }}
**Service Auditor:** {{ meta.roles.auditor.name }} ({{ meta.roles.auditor.email }})
**CISO:** {{ meta.roles.ciso.name }} ({{ meta.roles.ciso.email }})
**System Name:** {{ meta.tsc.system_name }}
**Report Period:** {{ meta.tsc.report_period }}
```

### [TODO]-Markierungen

Alle Templates enthalten `[TODO]`-Markierungen für organisationsspezifische Anpassungen:

```markdown
**System Description:** [TODO: Beschreibung des Service-Systems]
**Availability SLA:** [TODO: 99.9% uptime]
**Encryption Standard:** [TODO: AES-256]
```

## TSC Criteria Mapping

### Common Criteria (CC) - Pflicht für alle SOC 2

| TSC Criterion | TSC-Dokument | Beschreibung |
|---------------|--------------|--------------|
| CC1: Control Environment | TSC-0100 | Organisationsstruktur und Integrität |
| CC2: Communication | TSC-0110 | Kommunikation von Zielen |
| CC3: Risk Assessment | TSC-0120 | Risikobewertung |
| CC4: Monitoring | TSC-0130 | Überwachung der Kontrollen |
| CC5: Control Activities | TSC-0140 | Zugriffskontrolle |
| CC6: Logical Access | TSC-0150 | Logische Zugriffskontrolle |
| CC7: System Operations | TSC-0150 | Systemoperationen |
| CC8: Change Management | TSC-0150 | Änderungsmanagement |
| CC9: Risk Mitigation | TSC-0150 | Risikominderung |

### Optional Categories

| Category | TSC-Dokumente | Beschreibung |
|----------|---------------|--------------|
| Availability (A) | TSC-0200 - TSC-0230 | Systemverfügbarkeit |
| Processing Integrity (PI) | TSC-0240 - TSC-0270 | Verarbeitungsintegrität |
| Confidentiality (C) | TSC-0280 - TSC-0310 | Vertraulichkeit |
| Privacy (P) | TSC-0320 - TSC-0350 | Datenschutz |

## SOC 2 Report Types

### Type I Report

- **Zeitpunkt:** Stichtagsbezogen (zu einem bestimmten Datum)
- **Prüfungsumfang:** Design der Kontrollen
- **Aussage:** Kontrollen sind angemessen gestaltet

### Type II Report

- **Zeitraum:** Zeitraumbezogen (z.B. 6-12 Monate)
- **Prüfungsumfang:** Design und Wirksamkeit der Kontrollen
- **Aussage:** Kontrollen sind angemessen gestaltet UND wirksam

## Trust Services Categories

### Security (Common Criteria) - PFLICHT

Schutz des Systems vor unbefugtem Zugriff (logisch und physisch):
- Zugriffskontrolle
- Authentifizierung
- Netzwerksicherheit
- Physische Sicherheit
- Änderungsmanagement

### Availability - OPTIONAL

System ist verfügbar für Betrieb und Nutzung wie vereinbart:
- Systemverfügbarkeit
- Incident Management
- Backup und Recovery
- Kapazitätsplanung

### Processing Integrity - OPTIONAL

Systemverarbeitung ist vollständig, gültig, genau, zeitgerecht und autorisiert:
- Eingabevalidierung
- Verarbeitungskontrollen
- Ausgabekontrollen
- Fehlerbehandlung

### Confidentiality - OPTIONAL

Vertrauliche Informationen sind geschützt wie vereinbart:
- Datenverschlüsselung
- Zugriffsbeschränkungen
- Sichere Übertragung
- Sichere Löschung

### Privacy - OPTIONAL

Personenbezogene Daten werden gemäß Datenschutzhinweisen erhoben, verwendet, aufbewahrt, offengelegt und gelöscht:
- Datenschutzhinweise
- Einwilligung
- Datenminimierung
- Betroffenenrechte

## Best Practices für SOC 2-Compliance

### 1. Scope-Definition

- **System Boundaries:** Klare Definition der Systemgrenzen
- **Service Commitments:** Dokumentierte Zusagen an Kunden
- **Subservice Organizations:** Identifikation aller Subdienstleister
- **Complementary User Entity Controls (CUEC):** Kontrollen beim Kunden

### 2. Control Design

- **Risk-Based Approach:** Kontrollen basierend auf Risikobewertung
- **Control Objectives:** Klare Kontrollziele definieren
- **Control Activities:** Spezifische Kontrollaktivitäten dokumentieren
- **Evidence Collection:** Nachweise für jede Kontrolle sammeln

### 3. Control Testing

- **Test Procedures:** Dokumentierte Testverfahren
- **Sample Selection:** Angemessene Stichprobenauswahl
- **Test Frequency:** Regelmäßige Tests während des Berichtszeitraums
- **Exception Handling:** Umgang mit Kontrollabweichungen

### 4. Documentation

- **System Description:** Detaillierte Systembeschreibung
- **Control Matrix:** Vollständige Kontrollmatrix
- **Policies and Procedures:** Alle relevanten Richtlinien
- **Evidence Repository:** Zentrale Nachweisablage

## Generierung des Handbuchs

### CLI-Verwendung

```bash
# Deutsches TSC-Handbuch generieren
python -m src.cli --language de --template tsc --test

# Englisches TSC-Handbuch generieren
python -m src.cli --language en --template tsc --test

# PDF mit Inhaltsverzeichnis generieren
python -m src.cli --language de --template tsc --output pdf --test --pdf-toc

# Alle Formate generieren
python -m src.cli --language de --template tsc --output all --test --separate-files --pdf-toc
```

## Wartung und Aktualisierung

### Aktualisierungsintervalle

- **Jährlich:** Vollständige Überprüfung vor SOC 2-Audit
- **Quartalsweise:** Review der Kontrollwirksamkeit
- **Ad-hoc:** Bei Systemänderungen oder neuen Risiken

### Versionierung

- **MAJOR:** Neue TSC-Version oder wesentliche Systemänderungen
- **MINOR:** Ergänzungen und Aktualisierungen
- **PATCH:** Korrekturen und redaktionelle Änderungen

## Support und Feedback

Bei Fragen oder Problemen:

- **Dokumentation:** Siehe Haupt-README.md
- **AICPA:** https://www.aicpa.org/soc4so
- **Issues:** GitHub Issues für Fehlerberichte

---

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2026-02-07  
**Maintainer:** TSC-Template-Team

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
