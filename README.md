# Handbuch-Generator

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.0.3-blue.svg)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://img.shields.io/badge/coverage-86%25-brightgreen.svg)](htmlcov/index.html)
[![Tests](https://img.shields.io/badge/tests-450%20passed-success.svg)](tests/)
[![Documentation](https://img.shields.io/badge/docs-complete-blue.svg)](docs/)

**Ein professionelles Python-Tool zur Generierung standardkonformer Handbücher**

[Features](#features) • [Installation](#installation) • [Verwendung](#verwendung) • [Dokumentation](#dokumentation) • [Entwicklung](#entwicklung)

**Languages:** [🇩🇪 Deutsch](README.md) | [🇬🇧 English](README.en.md)

</div>

---

Ein Python-Tool zur Generierung professioneller Handbücher aus Markdown-Vorlagen mit Platzhalter-Ersetzung aus externen Datenquellen.

## Überblick

Der Handbuch-Generator erstellt aus strukturierten Markdown-Vorlagen professionelle Handbücher in verschiedenen Formaten (HTML, PDF, Markdown). Das System ersetzt Platzhalter in den Vorlagen durch echte Daten aus externen Systemen wie NetBox und unterstützt mehrsprachige Handbücher.

**Version 0.0.3** - Vollständige Handbuch-Generierung mit PDF-Unterstützung

## Features

- 📝 **Template-basierte Dokumentengenerierung** - Strukturierte Markdown-Vorlagen mit intelligenter Verarbeitung
- 📚 **Vier Handbuchtypen** - BCM, ISMS, BSI Grundschutz, IT-Operations
- 🔄 **Platzhalter-Ersetzung** - Automatische Datenintegration aus externen Quellen (NetBox, Metadata)
- 🌍 **Mehrsprachige Unterstützung** - Deutsch und Englisch mit identischer Struktur
- 📄 **Multi-Format-Ausgabe** - HTML, PDF (Pandoc + XeLaTeX), Markdown
- 🎨 **HTML Mini-Websites** - Professionelle HTML-Ausgabe mit Navigation und Styling
- 📑 **PDF mit Inhaltsverzeichnis** - Professionelle PDFs mit TOC und Seitennummerierung
- 💬 **HTML-Kommentar-Unterstützung** - Nicht-gerenderte Dokumentation für Template-Autoren
- ⚙️ **Konfigurierbare Datenquellen** - Flexible Integration externer Systeme
- 🔍 **Verbose Logging** - Detailliertes Debugging und Fehleranalyse
- ✅ **Umfassend getestet** - 86% Code Coverage, 450+ Tests (Unit & Property-Based)
- 📋 **Framework-Compliance** - ISO 22301, ISO 27001:2022, BSI Standards, ITIL v4
- 📦 **186 Templates** - Professionelle, standardkonforme Vorlagen
- 🚀 **Batch-Generierung** - Automatische Generierung aller Handbücher

## Handbuchtypen

| Typ | Standard | Templates | Beschreibung |
|-----|----------|-----------|--------------|
| **BCM** | ISO 22301, BSI BCM | 30 | Business Continuity Management |
| **ISMS** | ISO 27001:2022, Annex A | 71 | Information Security Management System |
| **BSI Grundschutz** | BSI 200-1/2/3 | 54 | IT-Grundschutz nach BSI |
| **IT-Operation** | ITIL v4, ISO 20000-1 | 31 | IT-Betriebshandbuch |

## Neu in Version 0.0.3 🎉

- ✅ **Vollständige PDF-Generierung** - Alle 8 Handbücher als PDF verfügbar (3.4 MB)
- ✅ **Pandoc + XeLaTeX Integration** - Professionelle PDF-Generierung mit TOC
- ✅ **Batch-Generierung** - Automatische Generierung aller Handbücher
- ✅ **784 Dateien generiert** - 388 HTML + 8 PDF + 388 Markdown
- ✅ **Helper Scripts** - Automatisierte Generierungsskripte in `helpers/`
- ✅ **Separate Verzeichnisse** - Jedes Handbuch in eigenem Verzeichnis
- ✅ **Produktionsreif** - Alle Formate einsatzbereit

**Generierte Handbücher:**
- 🇩🇪 Deutsch: BCM, ISMS, BSI Grundschutz, IT-Operation (HTML + PDF)
- 🇬🇧 English: BCM, ISMS, BSI Grundschutz, IT-Operation (HTML + PDF)

## Installation

### Voraussetzungen

- Python 3.8 oder höher (empfohlen: Python 3.11+)
- pip (Python Package Manager)
- Pandoc + XeLaTeX (für PDF-Generierung)

### Setup

1. Repository klonen:
```bash
git clone <repository-url>
cd Handbook-Generator
```

2. Virtual Environment erstellen und aktivieren:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# oder
venv\Scripts\activate  # Windows
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. PDF-Generierung aktivieren (empfohlen):
```bash
# Für PDF-Generierung mit Pandoc + XeLaTeX (empfohlen)
sudo apt-get install pandoc texlive-xetex

# Oder für WeasyPrint (experimentell, nicht empfohlen)
sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0
```

## Schnellstart

### Einzelnes Handbuch generieren

```bash
# HTML-Handbuch generieren
./handbook-generator -l de -t bcm -o html --test

# PDF-Handbuch generieren (erfordert Pandoc + XeLaTeX)
./handbook-generator -l de -t isms -o pdf --test --pdf-toc

# Alle Formate generieren
./handbook-generator -l de -t bcm -o all --test --separate-files --pdf-toc
```

### Alle Handbücher generieren (Batch)

```bash
# Alle HTML-Handbücher generieren (8 Handbücher)
bash helpers/generate_all_handbooks.sh

# Alle PDF-Handbücher generieren (8 PDFs)
bash helpers/generate_pdfs_pandoc.sh
```

**Ergebnis:**
- 8 Handbücher (4 Typen × 2 Sprachen)
- 388 HTML-Dateien
- 8 PDF-Dateien (3.4 MB)
- 388 Markdown-Dateien
- Gesamt: 784 Dateien

## Verwendung

### Direkter Befehl (Empfohlen)

**Seit Version 2.1** kann der Handbook Generator direkt als Befehl ausgeführt werden:

```bash
# Direkter Befehl (einfacher und schneller)
./handbook-generator --language de --template bcm --test --separate-files

# Oder mit Kurzformen
./handbook-generator -l de -t bcm --test --separate-files
```

**Vorteile:**
- ✅ Kürzer und einfacher zu tippen
- ✅ Professionelleres CLI-Tool-Verhalten
- ✅ Einfacher in Shell-Skripten zu verwenden
- ✅ Kann zu PATH hinzugefügt werden für systemweiten Zugriff

**Alternative (funktioniert weiterhin):**
```bash
# Klassischer Python-Modul-Aufruf
python -m src.cli --language de --template bcm --test --separate-files
```

### Konfiguration

Erstellen Sie eine `config.yaml` Datei im Projektverzeichnis. Eine Beispiel-Konfiguration wird automatisch erstellt, wenn keine Datei vorhanden ist.

#### Beispiel-Konfiguration

```yaml
# Handbook Generator Configuration
# WARNING: This file contains sensitive credentials - do not commit to git!

data_sources:
  netbox:
    url: "https://netbox.example.com"
    api_token: "your_api_token_here"
  # Weitere Datenquellen können hier hinzugefügt werden

defaults:
  language: "de"
  output_format: "both"  # markdown, pdf, both

metadata:
  author: "Andreas Huemmer [andreas.huemmer@adminsend.de]"
  version: "1.0.0"
```

#### Konfigurationsoptionen

**data_sources:**
- `netbox.url`: URL Ihrer NetBox-Instanz (erforderlich)
- `netbox.api_token`: API-Token für NetBox-Authentifizierung (erforderlich)

**defaults:**
- `language`: Standard-Sprache (`de` oder `en`)
- `output_format`: Standard-Ausgabeformat (`markdown`, `pdf`, oder `both`)

**metadata:**
- `author`: Autor-Information für Metadaten-Seite
- `version`: Versionsnummer für generierte Handbücher

**Wichtig:** 
- Die `config.yaml` enthält sensible Zugangsdaten und sollte nicht in Git committed werden!
- Das System fügt die Datei automatisch zu `.gitignore` hinzu
- Verwenden Sie `config.example.yaml` als Vorlage für neue Installationen

### Handbuch generieren

#### Interaktiver Modus

Starten Sie den Generator ohne Parameter für eine interaktive Auswahl:

```bash
./handbook-generator
```

Das System zeigt verfügbare Sprachen und Handbuchtypen an und fragt nach Ihrer Auswahl.

#### Kommandozeilen-Parameter

**Wichtig:** Seit Version 2.0 ist der `--test` Flag erforderlich, um Ausgaben zu generieren. Dies verhindert versehentliches Überschreiben von Dateien.

```bash
# IT-Operations-Handbuch auf Deutsch generieren (Test-Modus erforderlich)
./handbook-generator --language de --template it-operation --test

# BCM-Handbuch auf Deutsch generieren
./handbook-generator --language de --template bcm --test

# ISMS-Handbuch auf Englisch, nur PDF
./handbook-generator --language en --template isms --output pdf --test

# BSI Grundschutz-Handbuch auf Deutsch
./handbook-generator --language de --template bsi-grundschutz --test

# BCM-Handbuch mit ausführlichem Logging
./handbook-generator --language de --template bcm --verbose --test

# Eigene Konfigurationsdatei verwenden
./handbook-generator --config /path/to/config.yaml --language de --template it-operation --test
```

#### Verfügbare Parameter

- `--language, -l`: Sprache auswählen (`de`, `en`)
- `--template, -t`: Handbuchtyp auswählen (`bcm`, `isms`, `bsi-grundschutz`, `it-operation`)
- `--output, -o`: Ausgabeformat (`markdown`, `pdf`, `html`, `both`, `all`) [Standard: `both`]
- `--test`: Test-Modus aktivieren (erforderlich für Ausgabegenerierung)
- `--separate-files`: Separate Markdown-Dateien pro Template generieren (statt kombinierter Datei)
- `--pdf-toc`: PDF mit Inhaltsverzeichnis und Seitenumbrüchen generieren
- `--verbose, -v`: Ausführliches Logging aktivieren
- `--config, -c`: Pfad zur Konfigurationsdatei [Standard: `config.yaml`]

#### Test-Modus und Ausgabestruktur

**Seit Version 2.0** verwendet der Generator eine konsolidierte Ausgabestruktur und erfordert den `--test` Flag für Sicherheit.

**Seit Version 2.1** wird jedes Handbuch in einem separaten Verzeichnis gespeichert:

**Neue Ausgabestruktur (Version 2.1+):**
```
test-output/
├── de/                          # Deutsche Ausgaben
│   ├── bcm/                     # BCM-Handbuch
│   │   ├── markdown/            # Separate Markdown-Dateien
│   │   │   ├── TOC.md          # Inhaltsverzeichnis mit Links
│   │   │   ├── 0010_Zweck_und_Geltungsbereich.md
│   │   │   ├── 0020_BCM_Leitlinie_Policy.md
│   │   │   └── ...
│   │   ├── pdf/                 # PDF-Ausgaben
│   │   │   └── bcm_handbook.pdf
│   │   └── html/                # HTML Mini-Website
│   │       ├── index.html
│   │       └── ...
│   ├── isms/                    # ISMS-Handbuch
│   │   ├── markdown/
│   │   ├── pdf/
│   │   └── html/
│   ├── bsi-grundschutz/         # BSI Grundschutz-Handbuch
│   │   ├── markdown/
│   │   ├── pdf/
│   │   └── html/
│   └── it-operation/            # IT-Operations-Handbuch
│       ├── markdown/
│       ├── pdf/
│       └── html/
└── en/                          # Englische Ausgaben
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    └── it-operation/
```

**Vorteile der neuen Struktur:**
- ✅ Jedes Handbuch hat sein eigenes Verzeichnis
- ✅ Keine Datei-Konflikte zwischen verschiedenen Handbuchtypen
- ✅ Einfachere Navigation und Organisation
- ✅ Parallele Generierung mehrerer Handbücher möglich
- ✅ Jedes Handbuch ist eigenständig und vollständig
│       ├── index.html
│       ├── 0010_Template_Name.html
│       └── styles.css
└── en/                          # Englische Ausgaben
    ├── markdown/
    ├── pdf/
    └── html/
```

**Warum Test-Modus?**
- **Sicherheit**: Verhindert versehentliches Überschreiben von Produktionsdateien
- **Konsolidierung**: Alle Ausgaben an einem Ort statt verstreut in `Handbook/` und `PDF_Output/`
- **Klarheit**: Explizite Aktivierung macht Ausgabegenerierung bewusst

**Migration von alter Struktur:**
- Alte Struktur: `Handbook/{sprache}/{typ}/` und `PDF_Output/{sprache}/{typ}/`
- Neue Struktur: `test-output/{sprache}/{ausgabetyp}/`
- Dateien werden nach Template-Typ benannt (z.B. `bcm_handbook.pdf`)

**Ohne --test Flag:**
```bash
$ python -m src.cli --language de --template bcm
ERROR: Output generation requires --test flag. Use --test to enable test mode output.
```

#### Separate Markdown-Dateien

**Seit Version 2.1** können Sie separate Markdown-Dateien für jedes Template generieren, anstatt einer kombinierten Datei:

**Verwendung:**
```bash
# Separate Markdown-Dateien für BCM-Handbuch generieren
python -m src.cli --language de --template bcm --test --separate-files

# Nur separate Markdown-Dateien (kein PDF)
python -m src.cli --language de --template bcm --output markdown --test --separate-files
```

**Ausgabestruktur:**
```
test-output/de/markdown/
├── TOC.md                                    # Inhaltsverzeichnis mit Links
├── 0010_Zweck_und_Geltungsbereich.md        # Einzelnes Template
├── 0020_BCM_Leitlinie_Policy.md             # Einzelnes Template
├── 0030_Dokumentenlenkung_und_Versionierung.md
└── ... (weitere Templates)
```

**TOC.md Datei:**
Die `TOC.md` Datei enthält ein Inhaltsverzeichnis mit Links zu allen Template-Dateien:
```markdown
# Table of Contents

- [0010 - Zweck und Geltungsbereich](0010_Zweck_und_Geltungsbereich.md)
- [0020 - BCM Leitlinie Policy](0020_BCM_Leitlinie_Policy.md)
- [0030 - Dokumentenlenkung und Versionierung](0030_Dokumentenlenkung_und_Versionierung.md)
...
```

**Dateinamen-Muster:**
- Format: `{template-nummer}_{template-name}.md`
- Beispiel: `0010_Zweck_und_Geltungsbereich.md`
- Template-Nummer: 4-stellige Nummer aus Dateinamen
- Template-Name: Aus Dateinamen extrahiert, Unterstriche durch Leerzeichen ersetzt

**Vorteile:**
- **Einfache Bearbeitung**: Einzelne Kapitel können separat bearbeitet werden
- **Versionskontrolle**: Git-Diffs sind übersichtlicher bei Änderungen an einzelnen Kapiteln
- **Modulare Struktur**: Kapitel können einzeln weitergegeben oder wiederverwendet werden
- **Navigation**: TOC.md bietet schnellen Überblick und Navigation

#### PDF mit Inhaltsverzeichnis

**Seit Version 2.1** können Sie PDFs mit einem automatisch generierten Inhaltsverzeichnis und Seitenumbrüchen zwischen Templates erstellen:

**Verwendung:**
```bash
# PDF mit Inhaltsverzeichnis für BCM-Handbuch generieren
python -m src.cli --language de --template bcm --output pdf --test --pdf-toc

# PDF mit TOC und separate Markdown-Dateien
python -m src.cli --language de --template bcm --test --separate-files --pdf-toc
```

**Inhaltsverzeichnis-Struktur:**
Das Inhaltsverzeichnis wird automatisch am Anfang des PDFs eingefügt und enthält:
- **Template-Nummern**: 4-stellige Nummerierung (z.B. 0010, 0020)
- **Template-Titel**: Aus Dateinamen extrahiert
- **Klickbare Links**: Direkte Navigation zu Abschnitten im PDF
- **Seitenzahlen**: Automatisch generiert durch PDF-Renderer

**Beispiel-Inhaltsverzeichnis:**
```
Table of Contents

0010 - Zweck und Geltungsbereich ..................... Seite 2
0020 - BCM Leitlinie Policy .......................... Seite 5
0030 - Dokumentenlenkung und Versionierung ........... Seite 8
0040 - Notfallorganisation Rollen und Gremien ........ Seite 12
...
```

**Seitenumbrüche:**
- Jedes Template beginnt auf einer neuen Seite
- Seitenumbrüche werden automatisch zwischen Templates eingefügt
- Verhindert, dass Kapitel mitten auf einer Seite beginnen
- Verbessert Lesbarkeit und professionelles Erscheinungsbild

**Technische Details:**
- Verwendet HTML/CSS `page-break-after` Property
- Anchor-IDs für interne Verlinkung: `#section-0010`, `#section-0020`, etc.
- TOC wird als HTML-Struktur generiert und in PDF konvertiert
- WeasyPrint rendert das finale PDF mit allen Features

**Vorteile:**
- **Professionelles Layout**: Klare Struktur mit Inhaltsverzeichnis
- **Einfache Navigation**: Klickbare Links zu allen Kapiteln
- **Druckfreundlich**: Jedes Kapitel beginnt auf neuer Seite
- **Übersichtlichkeit**: Schneller Überblick über alle Inhalte

#### Handbuchtypen

- **bcm**: Business Continuity Management (ISO 22301, BSI BCM-Standards)
- **isms**: Information Security Management System (ISO 27001:2022, Annex A)
- **bsi-grundschutz**: BSI IT-Grundschutz (BSI Standards 200-1, 200-2, 200-3)
- **it-operation**: IT-Betriebshandbuch (ITIL v4, ISO 20000-1, COBIT 2019)

### Generierte Handbücher ansehen

Nach der Generierung können Sie die Handbücher wie folgt ansehen:

**HTML-Handbücher:**
```bash
# Im Browser öffnen
firefox test-output/de/bcm/html/index.html

# Oder lokalen Webserver starten
cd test-output
python3 -m http.server 8000
# Dann öffnen: http://localhost:8000/
```

**PDF-Handbücher:**
```bash
# PDF öffnen
evince test-output/de/isms/pdf/isms_handbook_de.pdf

# Alle PDFs auflisten
ls test-output/*/*/pdf/*.pdf
```

**Markdown-Dateien:**
```bash
# Einzelne Markdown-Dateien ansehen
cat test-output/de/bcm/markdown/0010_Zweck_und_Geltungsbereich.md

# Inhaltsverzeichnis ansehen
cat test-output/de/bcm/markdown/TOC.md
```

### Vorlagen-Struktur

Vorlagen werden im `templates/` Verzeichnis organisiert:

```
templates/
├── de/                          # Deutsche Vorlagen
│   ├── bcm/                     # Business Continuity Management (30 Templates)
│   │   ├── README.md
│   │   ├── 0010_Zweck_und_Geltungsbereich.md
│   │   ├── 0020_BCM_Leitlinie_Policy.md
│   │   └── ... (28 weitere)
│   ├── isms/                    # Information Security Management (71 Templates)
│   │   ├── README.md
│   │   ├── 0010_ISMS_Informationssicherheitsleitlinie.md
│   │   ├── 0020_ISMS_Geltungsbereich_Scope.md
│   │   └── ... (69 weitere)
│   ├── bsi-grundschutz/         # BSI IT-Grundschutz (54 Templates)
│   │   ├── README.md
│   │   ├── 0010_Informationssicherheitsleitlinie.md
│   │   ├── 0020_ISMS_Organisation_Rollen_RACI.md
│   │   └── ... (52 weitere)
│   └── it-operation/            # IT-Betriebshandbuch (31 Templates)
│       ├── README.md
│       ├── 0010_Einleitung.md
│       └── ... (29 weitere)
└── en/                          # Englische Vorlagen
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    └── it-operation/
```

#### Dateinamen-Konventionen

- **Content-Vorlagen**: `NNNN_name.md` (z.B. `0100_einleitung.md`)
  - NNNN: 4-stellige Sortierungsnummer (0100, 0200, 0300, ...)
  - Bestimmt die Reihenfolge im generierten Handbuch

- **Metadaten-Vorlagen**: `0000_metadata_[sprache]_[typ].md`
  - Wird immer als erste Seite gerendert
  - Enthält Erstellungsdatum, Autoren, Versionsnummer

### Platzhalter-Syntax

Platzhalter im Format `{{ quelle.feld }}` werden durch echte Daten ersetzt:

```markdown
# Geräteinformationen

Gerätename: {{ netbox.device_name }}
Standort: {{ netbox.site_name }}
IP-Adresse: {{ netbox.primary_ip }}
```

**Regeln:**
- Platzhalter muss die einzige Anweisung in der Zeile sein
- Whitespace vor/nach ist erlaubt
- Quelle: Datenquelle (z.B. "netbox")
- Feld: Feldpfad mit Punkt-Notation (z.B. "device.name")

### HTML-Kommentare in Vorlagen

Vorlagen können HTML-Kommentare enthalten, die nicht im generierten Handbuch erscheinen. Diese sind nützlich für:
- Hinweise für Template-Autoren
- Anpassungshinweise
- Dokumentation der Template-Struktur
- TODO-Markierungen

#### Syntax

```markdown
<!-- Dies ist ein Kommentar und wird nicht im Output erscheinen -->

# Kapitel

<!-- 
HINWEIS FÜR TEMPLATE-AUTOREN:
Dieser Abschnitt muss für jede Organisation angepasst werden.
Berücksichtigen Sie:
- Spezifische Sicherheitsrichtlinien
- Compliance-Anforderungen
- Organisationsstruktur
-->

Ihr Inhalt hier...
```

#### Best Practices

**Verwenden Sie Kommentare für:**
- Anpassungshinweise: `<!-- TODO: Organisationsspezifische Werte einfügen -->`
- Erklärungen: `<!-- Dieser Abschnitt erfüllt ISO 27001 Anforderung 5.2 -->`
- Template-Dokumentation: `<!-- Platzhalter {{ meta.org }} wird durch Organisationsnamen ersetzt -->`

**Vermeiden Sie:**
- Sensible Informationen in Kommentaren (werden zwar entfernt, aber in Vorlagen sichtbar)
- Verschachtelte Kommentare: `<!-- Outer <!-- Inner --> -->` (nicht unterstützt)

#### Kommentar-Verarbeitung

- Kommentare werden **vor** der Platzhalter-Ersetzung entfernt
- Einzeilige und mehrzeilige Kommentare werden unterstützt
- Umgebender Markdown-Inhalt bleibt unverändert
- Platzhalter innerhalb von Kommentaren werden **nicht** verarbeitet

### Ausgabe

Generierte Handbücher werden im `Handbook/` Verzeichnis gespeichert:

```
Handbook/
├── de/
│   ├── bcm/
│   │   ├── bcm_handbook_de.md
│   │   └── bcm_handbook_de.pdf
│   ├── isms/
│   │   ├── isms_handbook_de.md
│   │   └── isms_handbook_de.pdf
│   ├── bsi-grundschutz/
│   │   ├── bsi-grundschutz_handbook_de.md
│   │   └── bsi-grundschutz_handbook_de.pdf
│   └── it-operation/
│       ├── it-operation_handbook_de.md
│       └── it-operation_handbook_de.pdf
└── en/
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    └── it-operation/
```

## Projektstruktur

```
Handbook-Generator/
├── src/                    # Quellcode
│   ├── cli.py             # Command-Line Interface
│   ├── template_manager.py
│   ├── placeholder_processor.py
│   ├── html_comment_processor.py
│   ├── output_generator.py
│   └── ...
├── tests/                  # Tests (Unit & Property-Based)
│   ├── test_*.py          # Unit Tests
│   └── conftest.py        # Test Configuration
├── templates/              # Markdown-Vorlagen
│   ├── de/                # Deutsche Vorlagen
│   │   ├── bcm/          # 30 BCM Templates
│   │   ├── isms/         # ~50 ISMS Templates
│   │   ├── bsi-grundschutz/  # ~40 BSI Templates
│   │   └── it-operation/ # 30 IT-Ops Templates
│   └── en/                # Englische Vorlagen (identische Struktur)
├── docs/                   # Dokumentation
│   ├── FRAMEWORK_MAPPING.md
│   ├── MIGRATION_GUIDE.md
│   ├── PDF_GENERATION_GUIDE.md
│   └── cis-controls-structure.md
├── helpers/                # Utility Scripts
│   ├── generate_handbook_pdfs.py
│   ├── generate_pdfs.py
│   └── README.md
├── Handbook/              # Generierte Handbücher (Output)
│   ├── de/
│   └── en/
├── requirements.txt       # Python-Abhängigkeiten
├── pytest.ini            # Pytest-Konfiguration
├── setup.py              # Package Setup
└── README.md             # Diese Datei
```

## Dokumentation

Umfassende Dokumentation finden Sie im `docs/` Verzeichnis:

- **[OUTPUT_FORMATS_GUIDE.md](docs/OUTPUT_FORMATS_GUIDE.md)** - Detaillierte Anleitung zu allen Ausgabeformaten (Separate Markdown, PDF mit TOC, HTML)
- **[FRAMEWORK_MAPPING.md](docs/FRAMEWORK_MAPPING.md)** - Framework-Compliance-Mappings (ISO 22301, ISO 27001, BSI, ITIL)
- **[MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md)** - Migrationsleitfaden für bestehende Nutzer
- **[PDF_GENERATION_GUIDE.md](docs/PDF_GENERATION_GUIDE.md)** - Detaillierte Anleitung zur PDF-Generierung
- **[PDF_GENERATION_SUMMARY.md](docs/PDF_GENERATION_SUMMARY.md)** - Zusammenfassung der PDF-Generierung
- **[QUICK_START_PDF.md](docs/QUICK_START_PDF.md)** - Schnellstart für PDF-Generierung
- **[cis-controls-structure.md](docs/cis-controls-structure.md)** - CIS Controls v8 Struktur-Design

### Template-Dokumentation

Jedes Template-Verzeichnis enthält eine `README.md` mit:
- Template-Struktur und Nummerierung
- Platzhalter-Verwendung und Beispiele
- Framework-Compliance-Mapping
- Best Practices für Anpassungen

### Helper Scripts

Das `helpers/` Verzeichnis enthält Batch-Generierungsskripte:

**generate_all_handbooks.sh** - Generiert alle HTML-Handbücher automatisch
```bash
bash helpers/generate_all_handbooks.sh
```
- Generiert 8 Handbücher (4 Typen × 2 Sprachen)
- 388 HTML-Dateien
- Automatische Fortschrittsanzeige

**generate_pdfs_pandoc.sh** - Generiert alle PDF-Handbücher automatisch
```bash
bash helpers/generate_pdfs_pandoc.sh
```
- Generiert 8 PDFs (4 Typen × 2 Sprachen)
- 3.4 MB Gesamtgröße
- Professionelle Formatierung mit TOC

Weitere Details: [helpers/README.md](helpers/README.md)

## Entwicklung

### Tests ausführen

```bash
# Alle Tests
pytest

# Mit Coverage
pytest --cov=src --cov-report=html

# Nur Unit-Tests
pytest -m unit

# Nur Property-Based Tests
pytest -m property
```

### Code-Qualität

```bash
# Linting
flake8 src/

# Code-Formatierung
black src/ tests/

# Type-Checking
mypy src/
```

## Lizenz

Siehe LICENSE Datei.

## Autor

Andreas Huemmer [andreas.huemmer@adminsend.de]

Copyright © 2025, 2026

"Ich scheiss dich zu mit meiner Dokumentation
Ich kleb dich zu von oben bis unten.
Ich schieb se dir hinten und vorne rein"

Zitat, frei nach Maria Adorf in Kir Royal als Generaldirektor Heinrich.

https://www.youtube.com/watch?v=CwE4mk2fbow
