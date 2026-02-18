# BCM-Handbuch-Templates (Deutsch)

## Übersicht

Diese Templates bilden die Grundlage für ein vollständiges Business Continuity Management (BCM) Handbuch nach **ISO 22301:2019** und **BSI-Standard 100-4**.

Das BCM-Handbuch der [TODO] umfasst 30 strukturierte Dokumente, die alle wesentlichen Aspekte des Business Continuity Managements abdecken.

## Template-Struktur

### Foundation (Grundlagen, 0010-0090)

| Dokument-ID | Titel | Beschreibung |
|------|||
| BCM-0010 | Zweck und Geltungsbereich | Definition von Zweck, Scope und Zielen des BCMS |
| BCM-0020 | BCM-Leitlinie / Policy | Management-Commitment und BCM-Policy |
| BCM-0030 | Dokumentenlenkung | Versionierung, Freigabe und Pflege der BCM-Dokumentation |
| BCM-0040 | Notfallorganisation | Rollen, Verantwortlichkeiten und RACI-Matrizen |
| BCM-0050 | Kontakte und Eskalation | Kontaktlisten und Eskalationswege |
| BCM-0060 | Service- und Prozesskatalog | Kritikalitätsbewertung von Services und Prozessen |
| BCM-0070 | BIA-Methodik | Business Impact Analysis Methodik |
| BCM-0080 | BIA-Ergebnisse und RTO/RPO | Ergebnisse der BIA mit RTO/RPO-Werten |
| BCM-0090 | Risikoanalyse und Szenarien | Risikobewertung und Disaster-Szenarien |

### Strategy & Plans (Strategie & Pläne, 0100-0180)

| Dokument-ID | Titel | Beschreibung |
|------|||
| BCM-0100 | Strategie und Kontinuitätsoptionen | BCM-Strategie und Wiederherstellungsoptionen |
| BCM-0110 | Aktivierungskriterien | Kriterien für BCM-Aktivierung |
| BCM-0120 | Krisenmanagementplan | Prozesse für Krisenmanagement |
| BCM-0130 | Kommunikationsplan | Interne und externe Krisenkommunikation |
| BCM-0140 | BCP-Template | Business Continuity Plan Template |
| BCM-0150 | DRP-Template | IT Disaster Recovery Plan Template |
| BCM-0160 | Backup und Restore | Backup-Strategie und Wiederherstellung |
| BCM-0170 | Alternativstandorte | Ausweichstandorte und Notfallarbeitsplätze |
| BCM-0180 | Lieferanten-Kontinuität | BCM für kritische Lieferanten |

### Operations & Compliance (Betrieb & Compliance, 0190-0290)

| Dokument-ID | Titel | Beschreibung |
|------|||
| BCM-0190 | Ressourcenplanung | Mindestbesetzung und Ressourcenbedarf |
| BCM-0200 | Notfallzugang (Break-Glass) | Notfallzugänge und Privileged Access |
| BCM-0210 | Cyber-Incident-Playbook | Ransomware und Cyber-Vorfälle |
| BCM-0220 | Übungs- und Testprogramm | BCM-Übungen und Tests |
| BCM-0230 | Testprotokolle | Dokumentation von Tests und Übungen |
| BCM-0240 | Post-Incident-Review | Nachbereitung und Lessons Learned |
| BCM-0250 | Pflege und KPIs | Wartung und Erfolgsmessung |
| BCM-0260 | Schulungen und Awareness | Training und Sensibilisierung |
| BCM-0270 | Compliance und Audits | Nachweisführung und Audits |
| BCM-0280 | Anhang: Vorlagen | Checklisten und Templates |
| BCM-0290 | Glossar | Begriffe und Abkürzungen |

## Platzhalter-Verwendung

### Meta-Platzhalter (Organisationsdaten)

Die Templates verwenden Platzhalter aus der `metadata.yaml` Datei:

```markdown
**Organisation:** [TODO]
**CEO:** [TODO] ([TODO])
**CIO:** [TODO] ([TODO])
**CISO:** [TODO] ([TODO])
**Dokumentverantwortlicher:** [TODO]
```

### NetBox-Platzhalter (Infrastrukturdaten)

Für IT-spezifische Informationen können NetBox-Platzhalter verwendet werden:

```markdown
**Standort:** {{ netbox.site.name }}
**Rechenzentrum:** {{ netbox.site.datacenter.name }}
**Core Switch:** {{ netbox.device.core_switch.name }}
```

### [TODO]-Markierungen

Alle Templates enthalten `[TODO]`-Markierungen für organisationsspezifische Anpassungen:

```markdown
**Kritischer Lieferant:** [TODO: Name des Lieferanten]
**RTO:** [TODO: 4 Stunden]
**Notfallbudget:** [TODO: 50.000 €]
```

## ISO 22301:2019 Compliance-Mapping

| ISO 22301 Klausel | BCM-Dokument | Beschreibung |
|-----|||
| 4.1 Understanding the organization | BCM-0010 | Kontext der Organisation |
| 4.3 Determining the scope | BCM-0010 | Geltungsbereich |
| 5.2 Policy | BCM-0020 | BCM-Policy |
| 5.3 Organizational roles | BCM-0040 | Rollen und Verantwortlichkeiten |
| 7.5 Documented information | BCM-0030 | Dokumentenlenkung |
| 8.2.2 Business impact analysis | BCM-0070, BCM-0080 | BIA-Methodik und Ergebnisse |
| 8.2.3 Risk assessment | BCM-0090 | Risikoanalyse |
| 8.3 Business continuity strategies | BCM-0100 | BCM-Strategie |
| 8.4 Business continuity procedures | BCM-0140, BCM-0150 | BCP und DRP |
| 8.5 Exercise and testing | BCM-0220, BCM-0230 | Übungen und Tests |
| 9.1 Monitoring and measurement | BCM-0250 | KPIs und Monitoring |
| 9.2 Internal audit | BCM-0270 | Interne Audits |
| 9.3 Management review | BCM-0250 | Management Review |
| 10.1 Nonconformity and corrective action | BCM-0240 | Korrekturmaßnahmen |

## BSI-Standard 100-4 Mapping

| BSI 100-4 Kapitel | BCM-Dokument | Beschreibung |
|-----|||
| 3.1 Initiierung | BCM-0020 | BCM-Policy und Initiierung |
| 3.2 Konzeption | BCM-0070, BCM-0080, BCM-0090 | BIA und Risikoanalyse |
| 3.3 Umsetzung | BCM-0100, BCM-0140, BCM-0150 | Strategie und Pläne |
| 3.4 Tests und Übungen | BCM-0220, BCM-0230 | Übungsprogramm |
| 3.5 Aufrechterhaltung | BCM-0250 | Pflege und Verbesserung |

## HTML-Kommentare für Template-Autoren

Die Templates enthalten HTML-Kommentare mit Hinweisen für Template-Autoren:

```markdown
<!-- 
TEMPLATE AUTHOR NOTE:
This section requires customization based on your organization's specific BCM strategy.
Consider the following:
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)
- Critical business processes
-->
```

Diese Kommentare werden beim Generieren des Handbuchs automatisch entfernt.

## Best Practices für Anpassungen

### 1. Reihenfolge der Bearbeitung

Empfohlene Reihenfolge für die Anpassung der Templates:

1. **Foundation** (0010-0090): Grundlagen festlegen
2. **BIA durchführen** (0070, 0080): Kritikalität ermitteln
3. **Strategie entwickeln** (0100): BCM-Strategie festlegen
4. **Pläne erstellen** (0140, 0150): BCP und DRP ausarbeiten
5. **Übungen planen** (0220): Testprogramm aufsetzen

### 2. RACI-Matrizen

Alle RACI-Matrizen sollten vollständig ausgefüllt werden:

- **R** (Responsible): Durchführungsverantwortung
- **A** (Accountable): Gesamtverantwortung, Entscheidungsbefugnis
- **C** (Consulted): Konsultiert, Fachexpertise
- **I** (Informed): Informiert

**Regel:** Jede Aktivität muss genau ein "A" haben.

### 3. RTO/RPO-Werte

RTO/RPO-Werte sollten realistisch und erreichbar sein:

- **RTO:** Sollte 50-70% des MTPD betragen (Sicherheitspuffer)
- **RPO:** Abhängig von Backup-Frequenz und Datenänderungsrate
- **Validierung:** Durch Tests und Übungen bestätigen

### 4. Kontaktlisten

Kontaktlisten erfordern besondere Aufmerksamkeit:

- **Datenschutz:** DSGVO-konform speichern und verarbeiten
- **Aktualität:** Quartalsweise Überprüfung
- **Offline-Verfügbarkeit:** Verschlüsselte USB-Sticks oder Papierausdrucke

### 5. Dokumentation von Abhängigkeiten

Alle kritischen Abhängigkeiten dokumentieren:

- **People:** Schlüsselpersonen und Mindestbesetzung
- **Facilities:** Standorte und Räumlichkeiten
- **Technology:** IT-Systeme und Infrastruktur
- **Information:** Daten und Wissen
- **Suppliers:** Lieferanten und Dienstleister

## Generierung des Handbuchs

### CLI-Verwendung

```bash
# Deutsches BCM-Handbuch generieren (Test-Modus erforderlich)
python -m src.cli --language de --template bcm --test

# Separate Markdown-Dateien pro Template generieren
python -m src.cli --language de --template bcm --test --separate-files

# PDF mit Inhaltsverzeichnis und Seitenumbrüchen generieren
python -m src.cli --language de --template bcm --output pdf --test --pdf-toc

# Alle Formate mit allen Features generieren
python -m src.cli --language de --template bcm --output all --test --separate-files --pdf-toc

# Englisches BCM-Handbuch generieren
python -m src.cli --language en --template bcm --test
```

### Ausgabeformate

Das System unterstützt mehrere Ausgabeformate:

- **Markdown (kombiniert):** Einzelne .md-Datei mit allen Kapiteln
- **Markdown (separate Dateien):** Separate .md-Dateien für jedes Kapitel mit TOC.md
- **PDF (Standard):** Vollständiges Handbuch als PDF
- **PDF (mit TOC):** PDF mit Inhaltsverzeichnis und Seitenumbrüchen zwischen Kapiteln
- **HTML:** Mini-Website mit Navigation zwischen Seiten

### Ausgabestruktur

Alle Ausgaben werden in der `test-output/` Verzeichnisstruktur gespeichert:

```
test-output/
├── de/
│   ├── markdown/
│   │   ├── TOC.md                                    # Inhaltsverzeichnis (nur mit --separate-files)
│   │   ├── 0010_Zweck_und_Geltungsbereich.md        # Einzelnes Template (nur mit --separate-files)
│   │   ├── 0020_BCM_Leitlinie_Policy.md             # Einzelnes Template (nur mit --separate-files)
│   │   └── bcm_handbook.md                           # Kombinierte Datei (ohne --separate-files)
│   ├── pdf/
│   │   └── bcm_handbook.pdf                          # PDF (mit oder ohne TOC)
│   └── html/
│       ├── index.html                                # Inhaltsverzeichnis
│       ├── 0010_Zweck_und_Geltungsbereich.html
│       └── styles.css
└── en/
    └── ... (gleiche Struktur)
```

### Ausgabeformat-Optionen

**Separate Markdown-Dateien (`--separate-files`):**
- Jedes Template wird als separate .md-Datei gespeichert
- TOC.md Datei mit Links zu allen Templates
- Ideal für Versionskontrolle und individuelle Bearbeitung
- Dateinamen-Muster: `{nummer}_{name}.md`

**PDF mit Inhaltsverzeichnis (`--pdf-toc`):**
- Automatisch generiertes Inhaltsverzeichnis auf erster Seite
- Klickbare Links zu allen Kapiteln
- Seitenumbrüche zwischen Templates
- Professionelles Layout für Druck und Distribution

**HTML Mini-Website (`--output html`):**
- Separate HTML-Seite für jedes Template
- Navigation zwischen Seiten (Vorherige/Nächste)
- Konsistentes Styling über alle Seiten
- Ideal für Intranet oder Online-Zugriff

Weitere Details zu allen Ausgabeformaten finden Sie in der [OUTPUT_FORMATS_GUIDE.md](../../../docs/OUTPUT_FORMATS_GUIDE.md).

## Wartung und Aktualisierung

### Aktualisierungsintervalle

- **Jährlich:** Vollständige Überprüfung aller Dokumente
- **Quartalsweise:** Kontaktlisten und Eskalationswege
- **Ad-hoc:** Bei organisatorischen Änderungen oder nach Vorfällen

### Versionierung

Verwenden Sie semantische Versionierung:

- **MAJOR:** Grundlegende Änderungen der Struktur oder Strategie
- **MINOR:** Ergänzungen und Aktualisierungen
- **PATCH:** Korrekturen und redaktionelle Änderungen

## Support und Feedback

Bei Fragen oder Problemen:

- **Dokumentation:** Siehe Haupt-README.md
- **Issues:** GitHub Issues für Fehlerberichte
- **Contributions:** Pull Requests willkommen

---

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2026-01-31  
**Maintainer:** BCM-Template-Team
