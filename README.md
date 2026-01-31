# Handbuch-Generator

Ein Python-Tool zur Generierung professioneller Handbücher aus Markdown-Vorlagen mit Platzhalter-Ersetzung aus externen Datenquellen.

## Überblick

Der Handbuch-Generator erstellt aus strukturierten Markdown-Vorlagen professionelle Handbücher in verschiedenen Formaten (Markdown, PDF). Das System ersetzt Platzhalter in den Vorlagen durch echte Daten aus externen Systemen wie NetBox und unterstützt mehrsprachige Handbücher.

## Features

- 📝 Template-basierte Dokumentengenerierung
- 🔄 Platzhalter-Ersetzung aus externen Datenquellen (NetBox)
- 🌍 Mehrsprachige Unterstützung (Deutsch, Englisch)
- 📄 Multi-Format-Ausgabe (Markdown, PDF)
- ⚙️ Konfigurierbare Datenquellen
- 🔍 Verbose Logging für Debugging

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
# Backup-Handbuch auf Deutsch generieren
python -m src.cli --language de --template backup

# ISMS-Handbuch auf Englisch, nur PDF
python -m src.cli --language en --template isms --output pdf

# BCM-Handbuch mit ausführlichem Logging
python -m src.cli --language de --template bcm --verbose

# Eigene Konfigurationsdatei verwenden
python -m src.cli --config /path/to/config.yaml --language de --template it-operation
```

#### Verfügbare Parameter

- `--language, -l`: Sprache auswählen (`de`, `en`)
- `--template, -t`: Handbuchtyp auswählen (`backup`, `bcm`, `isms`, `it-operation`)
- `--output, -o`: Ausgabeformat (`markdown`, `pdf`, `both`) [Standard: `both`]
- `--verbose, -v`: Ausführliches Logging aktivieren
- `--config, -c`: Pfad zur Konfigurationsdatei [Standard: `config.yaml`]

### Vorlagen-Struktur

Vorlagen werden im `templates/` Verzeichnis organisiert:

```
templates/
├── de/                          # Deutsche Vorlagen
│   ├── backup/
│   │   ├── 0000_metadata_de_backup.md
│   │   ├── 0100_einleitung.md
│   │   ├── 0200_backup_strategie.md
│   │   └── 0300_wiederherstellung.md
│   ├── bcm/
│   ├── isms/
│   └── it-operation/
└── en/                          # Englische Vorlagen
    ├── backup/
    ├── bcm/
    ├── isms/
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

### Ausgabe

Generierte Handbücher werden im `Handbook/` Verzeichnis gespeichert:

```
Handbook/
├── de/
│   ├── backup/
│   │   ├── backup_handbook.md
│   │   └── backup_handbook.pdf
│   ├── bcm/
│   ├── isms/
│   └── it-operation/
└── en/
    └── ...
```

## Projektstruktur

```
Handbook-Generator/
├── src/                    # Quellcode
├── tests/                  # Tests (Unit & Property-Based)
├── templates/              # Markdown-Vorlagen
│   ├── de/                # Deutsche Vorlagen
│   └── en/                # Englische Vorlagen
├── docs/                   # Dokumentation
├── Handbook/              # Generierte Handbücher (Output)
├── requirements.txt       # Python-Abhängigkeiten
├── pytest.ini            # Pytest-Konfiguration
└── README.md             # Diese Datei
```

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

Copyright © 2025
