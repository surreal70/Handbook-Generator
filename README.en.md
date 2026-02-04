# Handbook Generator

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://img.shields.io/badge/coverage-86%25-brightgreen.svg)](htmlcov/index.html)
[![Tests](https://img.shields.io/badge/tests-450%20passed-success.svg)](tests/)
[![Documentation](https://img.shields.io/badge/docs-complete-blue.svg)](docs/)

**A professional Python tool for generating standards-compliant handbooks**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Development](#development)

**Languages:** [🇩🇪 Deutsch](README.md) | [🇬🇧 English](README.en.md)

</div>

---

A Python tool for generating professional handbooks from Markdown templates with placeholder replacement from external data sources.

## Overview

The Handbook Generator creates professional handbooks in various formats (Markdown, PDF) from structured Markdown templates. The system replaces placeholders in templates with real data from external systems like NetBox and supports multilingual handbooks.

## Features

- 📝 **Template-based Document Generation** - Structured Markdown templates with intelligent processing
- 📚 **Four Handbook Types** - BCM, ISMS, BSI Grundschutz, IT-Operations
- 🔄 **Placeholder Replacement** - Automatic data integration from external sources (NetBox, Metadata)
- 🌍 **Multilingual Support** - German and English with identical structure
- 📄 **Multi-Format Output** - Markdown and PDF (WeasyPrint)
- 💬 **HTML Comment Support** - Non-rendered documentation for template authors
- ⚙️ **Configurable Data Sources** - Flexible integration of external systems
- 🔍 **Verbose Logging** - Detailed debugging and error analysis
- ✅ **Comprehensively Tested** - 86% Code Coverage, 450+ Tests (Unit & Property-Based)
- 📋 **Framework Compliance** - ISO 22301, ISO 27001:2022, BSI Standards, ITIL v4
- 📦 **186 Templates** - Professional, standards-compliant templates

## Handbook Types

| Type | Standard | Templates | Description |
|------|----------|-----------|-------------|
| **BCM** | ISO 22301, BSI BCM | 30 | Business Continuity Management |
| **ISMS** | ISO 27001:2022, Annex A | 71 | Information Security Management System |
| **BSI Grundschutz** | BSI 200-1/2/3 | 54 | IT-Grundschutz according to BSI |
| **IT-Operation** | ITIL v4, ISO 20000-1 | 31 | IT Operations Handbook |

## Installation

### Prerequisites

- Python 3.8 or higher (recommended: Python 3.11+)
- pip (Python Package Manager)

### Setup

1. Clone repository:
```bash
git clone <repository-url>
cd Handbook-Generator
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Configuration

Create a `config.yaml` file in the project directory. An example configuration is automatically created if no file exists.

#### Example Configuration

```yaml
# Handbook Generator Configuration
# WARNING: This file contains sensitive credentials - do not commit to git!

data_sources:
  netbox:
    url: "https://netbox.example.com"
    api_token: "your_api_token_here"
  # Additional data sources can be added here

defaults:
  language: "en"
  output_format: "both"  # markdown, pdf, both

metadata:
  author: "Andreas Huemmer [andreas.huemmer@adminsend.de]"
  version: "1.0.0"
```

#### Configuration Options

**data_sources:**
- `netbox.url`: URL of your NetBox instance (required)
- `netbox.api_token`: API token for NetBox authentication (required)

**defaults:**
- `language`: Default language (`de` or `en`)
- `output_format`: Default output format (`markdown`, `pdf`, or `both`)

**metadata:**
- `author`: Author information for metadata page
- `version`: Version number for generated handbooks

**Important:** 
- The `config.yaml` contains sensitive credentials and should not be committed to Git!
- The system automatically adds the file to `.gitignore`
- Use `config.example.yaml` as a template for new installations

### Generate Handbook

#### Interactive Mode

Start the generator without parameters for interactive selection:

```bash
python -m src.cli
```

The system displays available languages and handbook types and asks for your selection.

#### Command Line Parameters

```bash
# Generate IT-Operations handbook in English
python -m src.cli --language en --template it-operation

# Generate BCM handbook in German
python -m src.cli --language de --template bcm

# Generate ISMS handbook in English, PDF only
python -m src.cli --language en --template isms --output pdf

# Generate BSI Grundschutz handbook in German
python -m src.cli --language de --template bsi-grundschutz

# Generate BCM handbook with verbose logging
python -m src.cli --language en --template bcm --verbose

# Use custom configuration file
python -m src.cli --config /path/to/config.yaml --language en --template it-operation
```

#### Available Parameters

- `--language, -l`: Select language (`de`, `en`)
- `--template, -t`: Select handbook type (`bcm`, `isms`, `bsi-grundschutz`, `it-operation`)
- `--output, -o`: Output format (`markdown`, `pdf`, `both`) [Default: `both`]
- `--verbose, -v`: Enable verbose logging
- `--config, -c`: Path to configuration file [Default: `config.yaml`]

#### Handbook Types

- **bcm**: Business Continuity Management (ISO 22301, BSI BCM Standards)
- **isms**: Information Security Management System (ISO 27001:2022, Annex A)
- **bsi-grundschutz**: BSI IT-Grundschutz (BSI Standards 200-1, 200-2, 200-3)
- **it-operation**: IT Operations Handbook (ITIL v4, ISO 20000-1, COBIT 2019)

### Template Structure

Templates are organized in the `templates/` directory:

```
templates/
├── de/                          # German templates
│   ├── bcm/                     # Business Continuity Management (30 Templates)
│   │   ├── README.md
│   │   ├── 0010_Zweck_und_Geltungsbereich.md
│   │   ├── 0020_BCM_Leitlinie_Policy.md
│   │   └── ... (28 more)
│   ├── isms/                    # Information Security Management (71 Templates)
│   │   ├── README.md
│   │   ├── 0010_ISMS_Informationssicherheitsleitlinie.md
│   │   ├── 0020_ISMS_Geltungsbereich_Scope.md
│   │   └── ... (69 more)
│   ├── bsi-grundschutz/         # BSI IT-Grundschutz (54 Templates)
│   │   ├── README.md
│   │   ├── 0010_Informationssicherheitsleitlinie.md
│   │   ├── 0020_ISMS_Organisation_Rollen_RACI.md
│   │   └── ... (52 more)
│   └── it-operation/            # IT Operations Handbook (31 Templates)
│       ├── README.md
│       ├── 0010_Einleitung.md
│       └── ... (29 more)
└── en/                          # English templates
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    └── it-operation/
```

#### File Naming Conventions

- **Content Templates**: `NNNN_name.md` (e.g. `0100_introduction.md`)
  - NNNN: 4-digit sorting number (0100, 0200, 0300, ...)
  - Determines order in generated handbook

- **Metadata Templates**: `0000_metadata_[language]_[type].md`
  - Always rendered as first page
  - Contains creation date, authors, version number

### Placeholder Syntax

Placeholders in the format `{{ source.field }}` are replaced with real data:

```markdown
# Device Information

Device Name: {{ netbox.device_name }}
Location: {{ netbox.site_name }}
IP Address: {{ netbox.primary_ip }}
```

**Rules:**
- Placeholder must be the only instruction on the line
- Whitespace before/after is allowed
- Source: Data source (e.g. "netbox")
- Field: Field path with dot notation (e.g. "device.name")

### HTML Comments in Templates

Templates can contain HTML comments that do not appear in the generated handbook. These are useful for:
- Notes for template authors
- Customization hints
- Template structure documentation
- TODO markers

#### Syntax

```markdown
<!-- This is a comment and will not appear in the output -->

# Chapter

<!-- 
NOTE FOR TEMPLATE AUTHORS:
This section must be customized for each organization.
Consider:
- Specific security policies
- Compliance requirements
- Organizational structure
-->

Your content here...
```

#### Best Practices

**Use comments for:**
- Customization hints: `<!-- TODO: Insert organization-specific values -->`
- Explanations: `<!-- This section fulfills ISO 27001 requirement 5.2 -->`
- Template documentation: `<!-- Placeholder {{ meta.org }} will be replaced with organization name -->`

**Avoid:**
- Sensitive information in comments (will be removed, but visible in templates)
- Nested comments: `<!-- Outer <!-- Inner --> -->` (not supported)

#### Comment Processing

- Comments are removed **before** placeholder replacement
- Single-line and multi-line comments are supported
- Surrounding Markdown content remains unchanged
- Placeholders within comments are **not** processed

### Output

Generated handbooks are saved in the `Handbook/` directory:

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

## Project Structure

```
Handbook-Generator/
├── src/                    # Source code
│   ├── cli.py             # Command-Line Interface
│   ├── template_manager.py
│   ├── placeholder_processor.py
│   ├── html_comment_processor.py
│   ├── output_generator.py
│   └── ...
├── tests/                  # Tests (Unit & Property-Based)
│   ├── test_*.py          # Unit Tests
│   └── conftest.py        # Test Configuration
├── templates/              # Markdown templates
│   ├── de/                # German templates
│   │   ├── bcm/          # 30 BCM Templates
│   │   ├── isms/         # 71 ISMS Templates
│   │   ├── bsi-grundschutz/  # 54 BSI Templates
│   │   └── it-operation/ # 31 IT-Ops Templates
│   └── en/                # English templates (identical structure)
├── docs/                   # Documentation
│   ├── FRAMEWORK_MAPPING.md
│   ├── MIGRATION_GUIDE.md
│   ├── PDF_GENERATION_GUIDE.md
│   └── cis-controls-structure.md
├── helpers/                # Utility Scripts
│   ├── generate_handbook_pdfs.py
│   ├── generate_pdfs.py
│   └── README.md
├── Handbook/              # Generated handbooks (Output)
│   ├── de/
│   └── en/
├── requirements.txt       # Python dependencies
├── pytest.ini            # Pytest configuration
├── setup.py              # Package setup
└── README.md             # This file
```

## Documentation

Comprehensive documentation can be found in the `docs/` directory:

- **[FRAMEWORK_MAPPING.md](docs/FRAMEWORK_MAPPING.md)** - Framework compliance mappings (ISO 22301, ISO 27001, BSI, ITIL)
- **[MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md)** - Migration guide for existing users
- **[PDF_GENERATION_GUIDE.md](docs/PDF_GENERATION_GUIDE.md)** - Detailed guide for PDF generation
- **[PDF_GENERATION_SUMMARY.md](docs/PDF_GENERATION_SUMMARY.md)** - PDF generation summary
- **[QUICK_START_PDF.md](docs/QUICK_START_PDF.md)** - Quick start for PDF generation
- **[cis-controls-structure.md](docs/cis-controls-structure.md)** - CIS Controls v8 structure design

### Template Documentation

Each template directory contains a `README.md` with:
- Template structure and numbering
- Placeholder usage and examples
- Framework compliance mapping
- Best practices for customization

### Helper Scripts

The `helpers/` directory contains optional utility scripts:
- PDF generation with various backends (WeasyPrint, Pandoc, ReportLab)
- Framework section insertion
- See [helpers/README.md](helpers/README.md) for details

## Development

### Run Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Unit tests only
pytest -m unit

# Property-based tests only
pytest -m property
```

### Code Quality

```bash
# Linting
flake8 src/

# Code formatting
black src/ tests/

# Type checking
mypy src/
```

## License

See LICENSE file.

## Author

Andreas Huemmer [andreas.huemmer@adminsend.de]

Copyright © 2025, 2026
