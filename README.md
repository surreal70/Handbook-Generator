# Handbuch-Generator

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.0.23-green.svg)](about_versioning/VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://img.shields.io/badge/coverage-72%25-yellow.svg)](htmlcov/index.html)
[![Tests](https://img.shields.io/badge/tests-7635%20total-success.svg)](tests/)
[![Documentation](https://img.shields.io/badge/docs-complete-blue.svg)](docs/)

**Ein professionelles Python-Tool zur Generierung standardkonformer Handbücher**

[Features](#features) • [Installation](#installation) • [Verwendung](#verwendung) • [Dokumentation](#dokumentation) • [Entwicklung](#entwicklung)

**Languages:** [🇩🇪 Deutsch](README.md) | [🇬🇧 English](README.en.md)

</div>

---

Ein Python-Tool zur Generierung professioneller Handbücher aus Markdown-Vorlagen mit Platzhalter-Ersetzung aus externen Datenquellen.

<div align="center">
  <img src="logo/HandBook-Generator.png" alt="Handbook Generator Logo" width="400"/>
</div>

## 🎯 Wichtiger Hinweis

**Dies ist Version 0.0.23 - Begrenzte Produktionsnutzung (Limited Production Use)**

Diese Version ist bereit für:
- ✅ Markdown-Handbuch-Generierung (alle 44 Handbücher)
- ✅ Dokumentationsprojekte
- ✅ Compliance-Dokumentation
- ✅ Entwicklungs- und Testumgebungen
- ✅ Inline-Placeholder-Unterstützung
- ✅ Handbuch-spezifische Metadaten

Einschränkungen:
- ⚠️ **PDF-Generierung: HOCHGRADIG EXPERIMENTELL UND TEILWEISE DEFEKT**
  - ReportLab-Engine: Funktioniert, aber TOC-Formatierung unvollständig
  - WeasyPrint-Engine: Erfordert System-Bibliotheken (libpango), oft nicht funktionsfähig
  - **Empfehlung**: Verwenden Sie Markdown-Ausgabe und konvertieren Sie extern
- ⚠️ HTML-Ausgabe nicht umfassend getestet

Siehe [Release Notes](about_versioning/VERSION_0.0.23_RELEASE_NOTES.md) für Details.

## Überblick

Der Handbuch-Generator erstellt aus strukturierten Markdown-Vorlagen professionelle Handbücher in verschiedenen Formaten (HTML, PDF, Markdown). Das System ersetzt Platzhalter in den Vorlagen durch echte Daten aus externen Systemen wie NetBox und unterstützt mehrsprachige Handbücher.

**Version 0.0.23** - 🎯 Limited Production Use - Core functionality stable, PDF generation experimental

## Features

- 📝 **Template-basierte Dokumentengenerierung** - Strukturierte Markdown-Vorlagen mit intelligenter Verarbeitung
- 📚 **22 Handbuchtypen** - BCM, ISMS, BSI Grundschutz, IT-Operations, CIS Controls, Common Criteria, COSO, CSA CCM, DORA, GDPR, HIPAA, IDW PS 951, ISO 9001, ISO 31000, ISO 38500, NIST 800-53, NIST CSF, PCI-DSS, SOC 1, TISAX, TOGAF, TSC
- 🔄 **Platzhalter-Ersetzung** - Automatische Datenintegration aus externen Quellen (NetBox, Metadata)
- 🌍 **Mehrsprachige Unterstützung** - Deutsch und Englisch mit identischer Struktur
- 📄 **Multi-Format-Ausgabe** - HTML, PDF (Pandoc + XeLaTeX), Markdown
- 🎨 **HTML Mini-Websites** - Professionelle HTML-Ausgabe mit Navigation und Styling
- 📑 **PDF mit Inhaltsverzeichnis** - Professionelle PDFs mit TOC und Seitennummerierung
- 💬 **HTML-Kommentar-Unterstützung** - Nicht-gerenderte Dokumentation für Template-Autoren
- ⚙️ **Konfigurierbare Datenquellen** - Flexible Integration externer Systeme
- 🔍 **Verbose Logging** - Detailliertes Debugging und Fehleranalyse
- ✅ **Umfassend getestet** - 72% Code Coverage, 7,635 Tests (Unit, Integration & Property-Based)
- 📋 **Framework-Compliance** - ISO 22301, ISO 27001:2022, BSI Standards, ITIL v4, CIS Controls v8
- 📦 **1,732+ Templates** - Professionelle, standardkonforme Vorlagen (866 DE + 866 EN)
- 🚀 **Batch-Generierung** - Automatische Generierung aller Handbücher

## Handbuchtypen

| Typ | Standard | Templates (DE/EN) | Beschreibung |
|-----|----------|-------------------|--------------|
| **BCM** | ISO 22301, BSI BCM | 29/29 | Business Continuity Management |
| **ISMS** | ISO 27001:2022, Annex A | 70/70 | Information Security Management System |
| **BSI Grundschutz** | BSI 200-1/2/3 | 54/54 | IT-Grundschutz nach BSI |
| **IT-Operation** | ITIL v4, ISO 20000-1 | 30/30 | IT-Betriebshandbuch |
| **CIS Controls** | CIS Controls v8 | 27/27 | CIS Controls v8 Hardening |
| **Common Criteria** | ISO/IEC 15408 | 35/35 | Common Criteria Security Evaluation |
| **COSO** | COSO Framework | 40/40 | Internal Control Framework |
| **CSA CCM** | CSA CCM v4 | 40/40 | Cloud Controls Matrix |
| **DORA** | EU DORA Regulation | 40/40 | Digital Operational Resilience Act |
| **GDPR** | EU GDPR 2016/679 | 36/36 | General Data Protection Regulation |
| **HIPAA** | HIPAA Security Rule | 13/13 | Health Insurance Portability and Accountability Act |
| **IDW PS 951** | IDW PS 951 | 50/50 | German IT Auditing Standard |
| **ISO 9001** | ISO 9001:2015 | 29/29 | Quality Management System |
| **ISO 31000** | ISO 31000:2018 | 40/40 | Risk Management |
| **ISO 38500** | ISO/IEC 38500:2015 | 40/40 | IT Governance |
| **NIST 800-53** | NIST SP 800-53 Rev. 5 | 52/52 | NIST Security and Privacy Controls |
| **NIST CSF** | NIST CSF 2.0 | 60/60 | NIST Cybersecurity Framework |
| **PCI-DSS** | PCI-DSS v4.0 | 14/14 | Payment Card Industry Data Security Standard |
| **SOC 1** | SSAE 18 / ISAE 3402 | 40/40 | Service Organization Controls Type 1 |
| **TISAX** | TISAX Assessment | 40/40 | Trusted Information Security Assessment Exchange |
| **TOGAF** | TOGAF 9.2 | 70/70 | The Open Group Architecture Framework |
| **TSC** | SOC 2 Trust Services | 17/17 | Trust Services Criteria (SOC 2) |

**Gesamt: 866+ Templates (DE) / 866+ Templates (EN)** über 22 Compliance-Frameworks

## Service und Prozess Dokumentation

**Seit Version 0.0.21** unterstützt der Handbook Generator die strukturierte Dokumentation von IT-Services und Geschäftsprozessen mit COBIT/ITIL-Konformität und BPMN-Unterstützung sowie ein umfassendes Placeholder-Management-System mit Inline-Placeholder-Unterstützung.

### Service-Dokumentation

Dokumentieren Sie IT-Services strukturiert nach COBIT- und ITIL-Standards:

```bash
# Service-Dokumentation generieren (Deutsch)
./handbook-generator --language de --service generic-service-template --test

# Service-Dokumentation generieren (Englisch)
./handbook-generator --language en --service generic-service-template --test

# Service mit allen Formaten
./handbook-generator -l de --service generic-service-template -o all --test --separate-files --pdf-toc
```

**Service-Template-Struktur:**
- Service-Übersicht (Name, Beschreibung, Kategorie)
- COBIT-Mapping (relevante Prozesse und Controls)
- ITIL-Mapping (Service Lifecycle Phasen)
- Service Level Agreements (SLAs)
- Rollen und Verantwortlichkeiten
- Support-Modell und Eskalation
- Monitoring und Reporting

**Verzeichnisstruktur:**
```
services/
├── de/
│   ├── meta-global-service.yaml         # Globale Service-Konfiguration
│   └── generic-service-template/
│       ├── meta-service.yaml            # Service-spezifische Konfiguration
│       └── service-template.md          # Service-Template
└── en/
    └── [identische Struktur]
```

### Prozess-Dokumentation

Dokumentieren Sie Geschäftsprozesse mit BPMN-Diagrammen und Compliance-Anforderungen:

```bash
# Prozess-Dokumentation generieren (Deutsch)
./handbook-generator --language de --process generic-process-template --test

# Prozess-Dokumentation generieren (Englisch)
./handbook-generator --language en --process generic-process-template --test

# Prozess mit allen Formaten
./handbook-generator -l de --process generic-process-template -o all --test --separate-files --pdf-toc
```

**Prozess-Template-Struktur:**
- Zweck und Ziel des Prozesses
- Rollen und Verantwortlichkeiten (RACI-Matrix)
- Ablaufdiagramm (BPMN) mit textueller Beschreibung
- SLAs und OLAs
- KPIs und Metriken
- Kontrollpunkte und Prüfschritte
- Risiken und Compliance-Anforderungen
- Segregation of Duties (SoD)

**Verzeichnisstruktur:**
```
processes/
├── de/
│   ├── meta-global-process.yaml         # Globale Prozess-Konfiguration
│   └── generic-process-template/
│       ├── meta-process.yaml            # Prozess-spezifische Konfiguration
│       ├── diagrams/                    # BPMN-Diagramme
│       └── process-template.md          # Prozess-Template
└── en/
    └── [identische Struktur]
```

### Metadata-Integration

Service- und Prozess-Templates integrieren sich nahtlos mit bestehenden Metadata-Konfigurationen:

**Hierarchische Placeholder-Auflösung:**
1. `meta-service.yaml` / `meta-process.yaml` (spezifisch)
2. `meta-global-service.yaml` / `meta-global-process.yaml` (global)
3. `meta-organisation-roles.yaml` (Rollen und Kontakte)
4. `meta-organisation.yaml` (Organisation)
5. `meta-global.yaml` (Generator-Informationen)

**Beispiel-Placeholders:**
```markdown
# Service: {{ service.name }}

**Service Owner:** {{ service.owner }}  # Referenz: role_IT_Manager
**Organisation:** {{ meta-organisation.name }}
**Verfügbarkeit:** {{ service.sla.availability_target }}
**Support:** {{ support.business_hours }}
```

### Dokumentation

Detaillierte Anleitungen zur Service- und Prozess-Dokumentation:

- **[SERVICE_DOCUMENTATION_GUIDE.md](docs/SERVICE_DOCUMENTATION_GUIDE.md)** - Service-Dokumentation erstellen und anpassen
- **[PROCESS_DOCUMENTATION_GUIDE.md](docs/PROCESS_DOCUMENTATION_GUIDE.md)** - Prozess-Dokumentation mit BPMN und RACI
- **[PLACEHOLDER_STRUCTURE.md](docs/PLACEHOLDER_STRUCTURE.md)** - Placeholder-Hierarchie und Verwendung

## Template Metadata Standardisierung

Alle Template-Frameworks verwenden eine einheitliche Metadatenstruktur für konsistente Dokumenteninformationen und Versionsverwaltung.

### Unified Metadata Structure

Alle Template-Frameworks verwenden eine einheitliche Metadatenstruktur für konsistente Dokumenteninformationen und Versionsverwaltung.

**Dokumentation:**
- 📋 **[METADATA_REFERENCE.md](docs/METADATA_REFERENCE.md)** - Vollständige Metadaten-Referenz mit allen Feldern und Beschreibungen
- 📋 **[PLACEHOLDER_REFERENCE.md](docs/PLACEHOLDER_REFERENCE.md)** - Platzhalter-Syntax und Verwendung
- 📋 **[TEMPLATE_HEADER_SPECIFICATION.md](docs/TEMPLATE_HEADER_SPECIFICATION.md)** - Template-Header-Struktur und Anforderungen
- ⚙️ **[CONFIGURATION_REFERENCE.md](docs/CONFIGURATION_REFERENCE.md)** - Konfigurationsdatei-Referenz und Einstellungen

**Tools:**
- `helpers/validate_metadata.py` - Metadaten-Validierung
- `helpers/generate_placeholder_matrix.py` - Platzhalter-Übersicht generieren

### Metadata Validation

Validieren Sie Metadaten mit dem Validierungsskript:

```bash
# Alle Frameworks validieren
python helpers/validate_metadata.py --all

# Einzelnes Framework validieren
python helpers/validate_metadata.py --framework gdpr

# Nur deutsche Metadaten validieren
python helpers/validate_metadata.py --language de

# JSON-Report generieren
python helpers/validate_metadata.py --all --report metadata_report.json
```

**Validierungsprüfungen:**
- Vollständigkeit aller Pflichtfelder
- Template-Version-Format (MAJOR.MINOR)
- Revisionsnummer-Gültigkeit (nicht-negative Ganzzahl)
- Bilinguale Konsistenz (DE/EN Struktur-Übereinstimmung)
- Platzhalter-Syntax (`{{ source.field }}`)

## Was ist neu?

Für detaillierte Informationen zu allen Releases, siehe:

� **[Versionshistorie](about_versioning/VERSION.md)** - Vollständige Übersicht aller Versionen mit Release Notes und Änderungen

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

## PDF Engine Auswahl

⚠️ **WARNUNG: PDF-Generierung ist HOCHGRADIG EXPERIMENTELL und TEILWEISE DEFEKT**

Die direkte PDF-Generierung über `--pdf-engine` ist in Version 0.0.23 experimentell und weist bekannte Probleme auf:

**Bekannte Probleme:**
- ❌ ReportLab: TOC-Formatierung unvollständig, Seitenumbrüche teilweise fehlerhaft
- ❌ WeasyPrint: Erfordert System-Bibliotheken, oft nicht funktionsfähig (libpango-Probleme)
- ❌ Beide Engines: Nicht produktionsreif

**EMPFEHLUNG für Produktionsumgebungen:**
```bash
# 1. Markdown generieren
./handbook-generator -l de -t bcm -o markdown --test

# 2. Extern zu PDF konvertieren (z.B. mit Pandoc)
pandoc output/de/bcm/markdown/bcm_handbook.md -o bcm_handbook.pdf --pdf-engine=xelatex --toc
```

### ReportLab (Experimentell - Nicht empfohlen)

**Status:** ⚠️ Funktioniert teilweise, aber mit Einschränkungen

**Bekannte Probleme:**
- TOC-Formatierung unvollständig
- Seitenumbrüche nicht konsistent
- Keine Produktionsreife

**Installation:**
```bash
pip install reportlab markdown
```

**Verwendung (auf eigene Gefahr):**
```bash
# Explizit ReportLab verwenden
./handbook-generator -l de -t bcm -o pdf --pdf-engine reportlab --test

# Auto-Erkennung (bevorzugt ReportLab)
./handbook-generator -l de -t bcm -o pdf --test
```

### WeasyPrint (Experimentell - Oft nicht funktionsfähig)

**Status:** ❌ Häufig defekt aufgrund von System-Bibliotheks-Problemen

**Bekannte Probleme:**
- libpango-Bibliotheken oft nicht ladbar
- Komplexe System-Abhängigkeiten
- Funktioniert oft nicht trotz installierter Pakete

**Installation:**
```bash
# Python-Paket installieren
pip install weasyprint

# System-Abhängigkeiten installieren (funktioniert oft nicht)
# Ubuntu/Debian:
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0

# macOS:
brew install pango

# Windows:
# GTK3 Runtime von https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
```

**Verwendung (auf eigene Gefahr):**
```bash
# Explizit WeasyPrint verwenden
./handbook-generator -l de -t bcm -o pdf --pdf-engine weasyprint --test
```

### Engine-Vergleich

| Feature | ReportLab | WeasyPrint | Pandoc (Empfohlen) |
|---------|-----------|------------|-------------------|
| Status | ⚠️ Experimentell | ❌ Oft defekt | ✅ Produktionsreif |
| Installation | ⭐⭐⭐⭐ Einfach | ⭐⭐ Schwierig | ⭐⭐⭐⭐ Einfach |
| Zuverlässigkeit | ⭐⭐⭐ Mittel | ⭐ Schlecht | ⭐⭐⭐⭐⭐ Exzellent |
| PDF-Qualität | ⭐⭐⭐ Akzeptabel | ⭐⭐⭐⭐⭐ Exzellent | ⭐⭐⭐⭐⭐ Exzellent |
| TOC-Support | ⚠️ Teilweise | ✅ Vollständig | ✅ Vollständig |
| Empfehlung | ⚠️ Nur für Tests | ❌ Nicht verwenden | ✅ Produktiv nutzen |

### Auto-Erkennung

Wenn Sie `--pdf-engine` nicht angeben, erkennt das System automatisch verfügbare Engines:

**Präferenz-Reihenfolge:**
1. ReportLab (bevorzugt, aber experimentell)
2. WeasyPrint (Fallback, oft defekt)

```bash
# Auto-Erkennung verwenden (nicht empfohlen für Produktion)
./handbook-generator -l de -t bcm -o pdf --test

# System wählt automatisch die beste verfügbare Engine
```

### Fehlerbehebung

**"No PDF engines available" Fehler:**
```bash
# Installieren Sie ReportLab (experimentell)
pip install reportlab markdown

# Oder WeasyPrint (oft nicht funktionsfähig)
pip install weasyprint
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0  # Linux
```

**WeasyPrint "OSError" oder "cairo" Fehler:**
```bash
# Dies ist ein bekanntes Problem - WeasyPrint ist oft nicht funktionsfähig
# EMPFEHLUNG: Verwenden Sie Pandoc stattdessen

# 1. Markdown generieren
./handbook-generator -l de -t bcm -o markdown --test

# 2. Mit Pandoc zu PDF konvertieren
pandoc output/de/bcm/markdown/bcm_handbook.md -o bcm.pdf --pdf-engine=xelatex --toc
```

**Virtuelle Umgebung prüfen:**
```bash
# Stellen Sie sicher, dass Sie in der virtuellen Umgebung sind
source venv/bin/activate

# Installierte Pakete prüfen
pip list | grep -E '(reportlab|weasyprint|markdown)'

# Neu installieren falls nötig
pip install --upgrade reportlab markdown
```

## Schnellstart

### Einzelnes Handbuch generieren

```bash
# HTML-Handbuch generieren
./handbook-generator -l de -t bcm -o html --test

# Markdown generieren (EMPFOHLEN für PDF-Konvertierung)
./handbook-generator -l de -t isms -o markdown --test

# PDF mit Pandoc erstellen (EMPFOHLEN)
pandoc output/de/isms/markdown/isms_handbook.md -o isms.pdf --pdf-engine=xelatex --toc

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

# ISMS-Handbuch mit ReportLab Engine (empfohlen)
./handbook-generator --language en --template isms --output pdf --pdf-engine reportlab --test

# ISMS-Handbuch mit WeasyPrint Engine (erweiterte Features)
./handbook-generator --language en --template isms --output pdf --pdf-engine weasyprint --test

# BSI Grundschutz-Handbuch auf Deutsch
./handbook-generator --language de --template bsi-grundschutz --test

# CIS Controls-Handbuch auf Deutsch generieren
./handbook-generator --language de --template cis-controls --test

# CIS Controls-Handbuch auf Englisch generieren
./handbook-generator --language en --template cis-controls --test

# CIS Controls-Handbuch mit allen Formaten
./handbook-generator --language de --template cis-controls --output all --test --separate-files --pdf-toc

# Common Criteria-Handbuch generieren
./handbook-generator --language de --template common-criteria --test

# GDPR-Handbuch generieren
./handbook-generator --language de --template gdpr --test

# HIPAA-Handbuch generieren
./handbook-generator --language en --template hipaa --test

# ISO 9001-Handbuch generieren
./handbook-generator --language de --template iso-9001 --test

# NIST 800-53-Handbuch generieren
./handbook-generator --language en --template nist-800-53 --test

# PCI-DSS-Handbuch generieren
./handbook-generator --language de --template pci-dss --test

# TSC (SOC 2)-Handbuch generieren
./handbook-generator --language en --template tsc --test

# ISO 38500-Handbuch generieren (IT Governance)
./handbook-generator --language de --template iso-38500 --test

# ISO 31000-Handbuch generieren (Risk Management)
./handbook-generator --language de --template iso-31000 --test

# CSA CCM-Handbuch generieren (Cloud Security)
./handbook-generator --language en --template csa-ccm --test

# TISAX-Handbuch generieren (Automotive Security)
./handbook-generator --language de --template tisax --test

# SOC 1-Handbuch generieren (Service Organization Controls)
./handbook-generator --language en --template soc1 --test

# COSO-Handbuch generieren (Internal Control)
./handbook-generator --language de --template coso --test

# DORA-Handbuch generieren (Digital Resilience)
./handbook-generator --language en --template dora --test

# BCM-Handbuch mit ausführlichem Logging
./handbook-generator --language de --template bcm --verbose --test

# Eigene Konfigurationsdatei verwenden
./handbook-generator --config /path/to/config.yaml --language de --template it-operation --test
```

#### Verfügbare Parameter

- `--language, -l`: Sprache auswählen (`de`, `en`)
- `--template, -t`: Handbuchtyp auswählen (`bcm`, `isms`, `bsi-grundschutz`, `it-operation`, `cis-controls`, `common-criteria`, `coso`, `csa-ccm`, `dora`, `gdpr`, `hipaa`, `idw-ps-951`, `iso-9001`, `iso-31000`, `iso-38500`, `nist-800-53`, `nist-csf`, `pci-dss`, `soc1`, `tisax`, `togaf`, `tsc`)
- `--service, -s`: Service-Name für Service-Dokumentation (z.B. `generic-service-template`)
- `--process, -p`: Prozess-Name für Prozess-Dokumentation (z.B. `generic-process-template`)
- `--output, -o`: Ausgabeformat (`markdown`, `pdf`, `html`, `both`, `all`) [Standard: `both`]
- `--pdf-engine`: PDF-Engine auswählen (`reportlab`, `weasyprint`, `auto`) [Standard: `auto`]
  - `reportlab`: Pure Python, keine System-Abhängigkeiten (empfohlen)
  - `weasyprint`: Erweiterte Features, benötigt libpango
  - `auto`: Automatische Erkennung (bevorzugt ReportLab)
- `--test`: Test-Modus aktivieren (erforderlich für Ausgabegenerierung)
- `--separate-files`: Separate Markdown-Dateien pro Template generieren (statt kombinierter Datei)
- `--pdf-toc`: PDF mit Inhaltsverzeichnis und Seitenumbrüchen generieren
- `--verbose, -v`: Ausführliches Logging aktivieren
- `--config, -c`: Pfad zur Konfigurationsdatei [Standard: `config.yaml`]

**Hinweis:** Die Optionen `--template`, `--service` und `--process` schließen sich gegenseitig aus. Es kann nur eine Option gleichzeitig verwendet werden.

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
- **cis-controls**: CIS Controls v8 Hardening Templates (CIS Controls v8 Framework)
- **common-criteria**: Common Criteria Security Evaluation (ISO/IEC 15408)
- **coso**: Internal Control Framework (COSO Framework)
- **csa-ccm**: Cloud Controls Matrix (CSA CCM v4)
- **dora**: Digital Operational Resilience Act (EU DORA Regulation)
- **gdpr**: General Data Protection Regulation (EU GDPR 2016/679)
- **hipaa**: Health Insurance Portability and Accountability Act (HIPAA Security Rule)
- **idw-ps-951**: German IT Auditing Standard (IDW PS 951)
- **iso-9001**: Quality Management System (ISO 9001:2015)
- **iso-31000**: Risk Management (ISO 31000:2018)
- **iso-38500**: IT Governance (ISO/IEC 38500:2015)
- **nist-800-53**: NIST Security and Privacy Controls (NIST SP 800-53 Rev. 5)
- **nist-csf**: NIST Cybersecurity Framework (NIST CSF 2.0)
- **pci-dss**: Payment Card Industry Data Security Standard (PCI-DSS v4.0)
- **soc1**: Service Organization Controls Type 1 (SSAE 18 / ISAE 3402)
- **tisax**: Trusted Information Security Assessment Exchange (TISAX Assessment)
- **togaf**: The Open Group Architecture Framework (TOGAF 9.2)
- **tsc**: Trust Services Criteria for SOC 2 (SOC 2 Trust Services)

#### CIS Controls Template-Struktur

Die CIS Controls Templates sind in vier Kategorien organisiert (27 Templates, Nummerierung 0010-0410):

**1. Foundation (0010-0050)** - 5 Templates
- Überblick und Vorgehen
- Geltungsbereich und Asset-Gruppen
- Hardening-Lifecycle
- Ausnahmen und Risikoakzeptanz
- Test und Validierung

**2. Betriebssysteme (0100-0150)** - 6 Templates
- Windows Server Hardening Baseline
- Windows Client Hardening Baseline
- Linux Hardening Baseline
- macOS Hardening Baseline
- Container Base Images Hardening

**3. Applikationen (0200-0330)** - 14 Templates
- Webserver (Nginx, Apache, IIS, Tomcat)
- Datenbanken (PostgreSQL, MySQL, MS SQL Server)
- Container-Plattformen (Kubernetes, Docker)
- Services (SSH, Identity/AD)

**4. Anhänge (0400-0410)** - 2 Templates
- Control Mapping Template
- Checklisten und Evidence

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
│   ├── bcm/                     # Business Continuity Management (29 Templates)
│   │   ├── README.md
│   │   ├── 0010_Zweck_und_Geltungsbereich.md
│   │   ├── 0020_BCM_Leitlinie_Policy.md
│   │   └── ... (27 weitere)
│   ├── isms/                    # Information Security Management (70 Templates)
│   │   ├── README.md
│   │   ├── 0010_ISMS_Informationssicherheitsleitlinie.md
│   │   ├── 0020_ISMS_Geltungsbereich_Scope.md
│   │   └── ... (68 weitere)
│   ├── bsi-grundschutz/         # BSI IT-Grundschutz (54 Templates)
│   │   ├── README.md
│   │   ├── 0010_Informationssicherheitsleitlinie.md
│   │   ├── 0020_ISMS_Organisation_Rollen_RACI.md
│   │   └── ... (52 weitere)
│   ├── it-operation/            # IT-Betriebshandbuch (30 Templates)
│   │   ├── README.md
│   │   ├── 0010_Einleitung.md
│   │   └── ... (28 weitere)
│   ├── cis-controls/            # CIS Controls v8 Hardening (27 Templates)
│   │   ├── 0000_metadata_de_cis-controls.md
│   │   ├── 0010_CIS_Controls_Ueberblick_und_Vorgehen.md
│   │   ├── 0020_Geltungsbereich_Assetgruppen_und_Tiering.md
│   │   └── ... (25 weitere)
│   ├── common-criteria/         # Common Criteria (35 Templates)
│   │   ├── README.md
│   │   └── ... (35 Templates)
│   ├── gdpr/                    # GDPR (36 Templates)
│   │   ├── README.md
│   │   └── ... (36 Templates)
│   ├── hipaa/                   # HIPAA (13 Templates)
│   │   ├── README.md
│   │   └── ... (13 Templates)
│   ├── iso-9001/                # ISO 9001 (29 Templates)
│   │   ├── README.md
│   │   └── ... (29 Templates)
│   ├── nist-800-53/             # NIST 800-53 (52 Templates)
│   │   ├── README.md
│   │   └── ... (52 Templates)
│   ├── pci-dss/                 # PCI-DSS (14 Templates)
│   │   ├── README.md
│   │   └── ... (14 Templates)
│   └── tsc/                     # Trust Services Criteria (17 Templates)
│       ├── README.md
│       └── ... (17 Templates)
└── en/                          # Englische Vorlagen
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    ├── it-operation/
    ├── cis-controls/
    ├── common-criteria/
    ├── gdpr/
    ├── hipaa/
    ├── iso-9001/
    ├── nist-800-53/
    ├── pci-dss/
    └── tsc/            # CIS Controls v8 Hardening (27 Templates)
        ├── 0000_metadata_en_cis-controls.md
        ├── 0010_CIS_Controls_Overview_and_Approach.md
        ├── 0020_Scope_Asset_Groups_and_Tiering.md
        └── ... (25 weitere)
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

## Quality Control System

Das Projekt enthält ein umfassendes Quality Control System zur automatischen Validierung von Framework-Struktur, Template-Metadaten, Test-Ausführung und Code-Qualität. Das System stellt sicher, dass alle 22 Compliance-Frameworks konsistent strukturiert sind und alle 1.732+ Templates den Qualitätsstandards entsprechen.

### Überblick

Das Quality Control System führt vier Hauptprüfungen durch:

1. **Framework Mapping Validation** - Stellt sicher, dass alle Framework-Verzeichnisse korrekt benannte Mapping-Dateien (`9999_Framework_Mapping.md`) enthalten
2. **Version History Validation** - Verifiziert, dass alle Templates standardisierte Version History Sektionen enthalten
3. **Test Suite Execution** - Führt die komplette Test-Suite (765+ Tests) aus und analysiert Fehler systematisch
4. **Coverage Documentation** - Generiert automatisch umfassende Dokumentation aller unterstützten Frameworks mit Template-Zählungen und Bilingual-Konsistenz-Prüfung

### Schnellstart

```bash
# Alle Qualitätsprüfungen ausführen
./quality_control.py

# Spezifische Prüfung ausführen
./quality_control.py --check mapping      # Framework Mapping Validation
./quality_control.py --check version      # Version History Validation
./quality_control.py --check tests        # Test Suite Execution
./quality_control.py --check coverage     # Coverage Documentation

# Test-Kategorien ausführen
./quality_control.py --check tests --test-category unit          # Unit Tests (Standard, ~23s)
./quality_control.py --check tests --test-category integration   # Integration Tests (~3s)
./quality_control.py --check tests --test-category property      # Property-Based Tests (~7s)
./quality_control.py --check tests --test-category all           # Alle Tests (~5+ min)

# Mit ausführlichem Logging
./quality_control.py --verbose

# Bericht in Datei speichern
./quality_control.py --output quality_report.txt
```

**Test-Kategorien:**
- `unit` - Schnelle, isolierte Unit Tests (Standard)
- `integration` - Tests für Komponenten-Interaktion
- `property` - Property-Based Tests mit Hypothesis
- `slow` - Langlaufende Tests
- `all` - Alle Tests (Unit, Integration, Property, Slow)

Siehe [TEST_CATEGORIES.md](TEST_CATEGORIES.md) für Details zu Test-Kategorien.

### Qualitätsmetriken und Trend-Tracking

Das System verfolgt automatisch Qualitätsmetriken über Zeit und identifiziert Verbesserungen oder Regressionen:

```bash
# Qualitätsmetriken über Zeit verfolgen
./quality_control.py --show-trends

# Metriken exportieren (JSON/CSV)
./quality_control.py --export-json metrics.json
./quality_control.py --export-csv metrics.csv
```

**Verfolgte Metriken:**
- **Framework Mapping Compliance Rate** - Prozentsatz der Frameworks mit korrekten Mapping-Dateien
- **Version History Compliance Rate** - Prozentsatz der Templates mit gültiger Version History
- **Test Pass Rate** - Prozentsatz der bestandenen Tests
- **Bilingual Consistency Rate** - Prozentsatz der Frameworks mit identischen DE/EN Template-Zählungen

**Metriken-Speicherung:**
- Metriken werden in `.quality/metrics_history.json` gespeichert
- Jeder Lauf wird mit Timestamp versehen
- Trend-Analyse vergleicht aktuelle mit vorherigen Läufen
- Verbesserungen und Regressionen werden automatisch identifiziert

### Interaktiver Modus

Der interaktive Modus ermöglicht die direkte Behandlung fehlgeschlagener Tests:

```bash
# Interaktive Behandlung fehlgeschlagener Tests
./quality_control.py --interactive

# Tasks für spätere Bearbeitung speichern
./quality_control.py --interactive --save-tasks failed_tests.md
```

**Interaktive Optionen für jeden fehlgeschlagenen Test:**
- **Fix now** - Sofortige Behebung mit Anleitung
- **Create task for later** - Task-Eintrag für spätere Bearbeitung erstellen
- **Skip** - Zum nächsten Test weitergehen
- **View full error** - Vollständigen Error-Traceback anzeigen

### Automatische Remediation-Vorschläge

Das System generiert automatisch Vorschläge zur Behebung identifizierter Probleme:

```bash
# Automatische Vorschläge zur Fehlerbehebung anzeigen
./quality_control.py --show-remediation

# Remediation-Skript generieren
./quality_control.py --generate-remediation-script fix_issues.sh
```

**Remediation-Kategorien:**
- Fehlende Framework Mapping Dateien
- Fehlende Version History Sektionen
- Fehlende Template-Übersetzungen (DE/EN Inkonsistenzen)
- Test-Fehler mit Lösungsvorschlägen

### Detaillierte Dokumentation

Vollständige Dokumentation des Quality Control Systems mit allen Features, Beispielen und Best Practices:

📖 **[QUALITY_CONTROL_GUIDE.md](docs/QUALITY_CONTROL_GUIDE.md)** - Umfassender Leitfaden

**Dokumentations-Inhalte:**
- Detaillierte Beschreibung aller Validatoren
- Verwendungsbeispiele für alle CLI-Optionen
- Metriken-Interpretation und Trend-Analyse
- Interaktiver Modus Workflow
- Remediation-Strategien
- CI/CD Integration-Beispiele
- Troubleshooting und Best Practices

### CI/CD Integration

Das Quality Control System kann einfach in CI/CD-Pipelines integriert werden:

```yaml
# GitHub Actions Beispiel
name: Quality Control
on: [push, pull_request]

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Quality Control
        run: ./quality_control.py --verbose --output quality_report.txt
      - name: Upload Quality Report
        uses: actions/upload-artifact@v2
        with:
          name: quality-report
          path: quality_report.txt
```

**CI/CD Best Practices:**
- Führen Sie Quality Control bei jedem Push/PR aus
- Speichern Sie Qualitätsberichte als Artifacts
- Verwenden Sie `--verbose` für detailliertes Logging
- Tracken Sie Metriken über Zeit mit `--export-json`
- Blockieren Sie Merges bei kritischen Qualitätsproblemen

### Verwendung im Entwicklungs-Workflow

**Vor dem Commit:**
```bash
# Schnelle Validierung
./quality_control.py --check mapping --check version
```

**Vor dem Release:**
```bash
# Vollständige Qualitätsprüfung
./quality_control.py --verbose --output release_quality_report.txt
```

**Nach Template-Änderungen:**
```bash
# Version History und Bilingual Consistency prüfen
./quality_control.py --check version --check coverage
```

**Bei Test-Fehlern:**
```bash
# Interaktive Fehlerbehandlung
./quality_control.py --check tests --interactive
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
