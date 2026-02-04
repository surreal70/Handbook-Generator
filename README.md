# Handbuch-Generator

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
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

Der Handbuch-Generator erstellt aus strukturierten Markdown-Vorlagen professionelle Handbücher in verschiedenen Formaten (Markdown, PDF). Das System ersetzt Platzhalter in den Vorlagen durch echte Daten aus externen Systemen wie NetBox und unterstützt mehrsprachige Handbücher.

## Features

- 📝 **Template-basierte Dokumentengenerierung** - Strukturierte Markdown-Vorlagen mit intelligenter Verarbeitung
- 📚 **Vier Handbuchtypen** - BCM, ISMS, BSI Grundschutz, IT-Operations
- 🔄 **Platzhalter-Ersetzung** - Automatische Datenintegration aus externen Quellen (NetBox, Metadata)
- 🌍 **Mehrsprachige Unterstützung** - Deutsch und Englisch mit identischer Struktur
- 📄 **Multi-Format-Ausgabe** - Markdown und PDF (WeasyPrint)
- 💬 **HTML-Kommentar-Unterstützung** - Nicht-gerenderte Dokumentation für Template-Autoren
- ⚙️ **Konfigurierbare Datenquellen** - Flexible Integration externer Systeme
- 🔍 **Verbose Logging** - Detailliertes Debugging und Fehleranalyse
- ✅ **Umfassend getestet** - 86% Code Coverage, 450+ Tests (Unit & Property-Based)
- 📋 **Framework-Compliance** - ISO 22301, ISO 27001:2022, BSI Standards, ITIL v4
- 📦 **186 Templates** - Professionelle, standardkonforme Vorlagen

## Handbuchtypen

| Typ | Standard | Templates | Beschreibung |
|-----|----------|-----------|--------------|
| **BCM** | ISO 22301, BSI BCM | 30 | Business Continuity Management |
| **ISMS** | ISO 27001:2022, Annex A | 71 | Information Security Management System |
| **BSI Grundschutz** | BSI 200-1/2/3 | 54 | IT-Grundschutz nach BSI |
| **IT-Operation** | ITIL v4, ISO 20000-1 | 31 | IT-Betriebshandbuch |

## Installation

### Voraussetzungen

- Python 3.8 oder höher (empfohlen: Python 3.11+)
- pip (Python Package Manager)

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

## Verwendung

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
python -m src.cli
```

Das System zeigt verfügbare Sprachen und Handbuchtypen an und fragt nach Ihrer Auswahl.

#### Kommandozeilen-Parameter

```bash
# IT-Operations-Handbuch auf Deutsch generieren
python -m src.cli --language de --template it-operation

# BCM-Handbuch auf Deutsch generieren
python -m src.cli --language de --template bcm

# ISMS-Handbuch auf Englisch, nur PDF
python -m src.cli --language en --template isms --output pdf

# BSI Grundschutz-Handbuch auf Deutsch
python -m src.cli --language de --template bsi-grundschutz

# BCM-Handbuch mit ausführlichem Logging
python -m src.cli --language de --template bcm --verbose

# Eigene Konfigurationsdatei verwenden
python -m src.cli --config /path/to/config.yaml --language de --template it-operation
```

#### Verfügbare Parameter

- `--language, -l`: Sprache auswählen (`de`, `en`)
- `--template, -t`: Handbuchtyp auswählen (`bcm`, `isms`, `bsi-grundschutz`, `it-operation`)
- `--output, -o`: Ausgabeformat (`markdown`, `pdf`, `both`) [Standard: `both`]
- `--verbose, -v`: Ausführliches Logging aktivieren
- `--config, -c`: Pfad zur Konfigurationsdatei [Standard: `config.yaml`]

#### Handbuchtypen

- **bcm**: Business Continuity Management (ISO 22301, BSI BCM-Standards)
- **isms**: Information Security Management System (ISO 27001:2022, Annex A)
- **bsi-grundschutz**: BSI IT-Grundschutz (BSI Standards 200-1, 200-2, 200-3)
- **it-operation**: IT-Betriebshandbuch (ITIL v4, ISO 20000-1, COBIT 2019)

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

Das `helpers/` Verzeichnis enthält optionale Utility-Scripts:
- PDF-Generierung mit verschiedenen Backends (WeasyPrint, Pandoc, ReportLab)
- Framework-Section-Insertion
- Siehe [helpers/README.md](helpers/README.md) für Details

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
