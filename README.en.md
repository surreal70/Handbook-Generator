# Handbook Generator

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.0.5-blue.svg)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://img.shields.io/badge/coverage-84%25-brightgreen.svg)](htmlcov/index.html)
[![Tests](https://img.shields.io/badge/tests-765%20passed-success.svg)](tests/)
[![Documentation](https://img.shields.io/badge/docs-complete-blue.svg)](docs/)

**A professional Python tool for generating standards-compliant handbooks**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Development](#development)

**Languages:** [🇩🇪 Deutsch](README.md) | [🇬🇧 English](README.en.md)

</div>

---

A Python tool for generating professional handbooks from Markdown templates with placeholder replacement from external data sources.

## Overview

The Handbook Generator creates professional handbooks in various formats (HTML, PDF, Markdown) from structured Markdown templates. The system replaces placeholders in templates with real data from external systems like NetBox and supports multilingual handbooks.

**Version 0.0.5** - Placeholder System Validation & Testing

## Features

- 📝 **Template-based Document Generation** - Structured Markdown templates with intelligent processing
- 📚 **Five Handbook Types** - BCM, ISMS, BSI Grundschutz, IT-Operations, CIS Controls
- 🔄 **Placeholder Replacement** - Automatic data integration from external sources (NetBox, Metadata)
- 🌍 **Multilingual Support** - German and English with identical structure
- 📄 **Multi-Format Output** - HTML, PDF (Pandoc + XeLaTeX), Markdown
- 🎨 **HTML Mini-Websites** - Professional HTML output with navigation and styling
- 📑 **PDF with Table of Contents** - Professional PDFs with TOC and page numbering
- 💬 **HTML Comment Support** - Non-rendered documentation for template authors
- ⚙️ **Configurable Data Sources** - Flexible integration of external systems
- 🔍 **Verbose Logging** - Detailed debugging and error analysis
- ✅ **Comprehensively Tested** - 86% Code Coverage, 450+ Tests (Unit & Property-Based)
- 📋 **Framework Compliance** - ISO 22301, ISO 27001:2022, BSI Standards, ITIL v4, CIS Controls v8
- 📦 **240 Templates** - Professional, standards-compliant templates
- 🚀 **Batch Generation** - Automatic generation of all handbooks

## Handbook Types

| Type | Standard | Templates | Description |
|------|----------|-----------|-------------|
| **BCM** | ISO 22301, BSI BCM | 30 | Business Continuity Management |
| **ISMS** | ISO 27001:2022, Annex A | 71 | Information Security Management System |
| **BSI Grundschutz** | BSI 200-1/2/3 | 54 | IT-Grundschutz according to BSI |
| **IT-Operation** | ITIL v4, ISO 20000-1 | 31 | IT Operations Handbook |
| **CIS Controls** | CIS Controls v8 | 27 | CIS Controls v8 Hardening |

## New in Version 0.0.5 🎉

- ✅ **Placeholder System Validation** - Comprehensive testing and validation
- ✅ **Metadata Configuration Validation** - Automated validation of metadata.yaml
- ✅ **Placeholder Consistency Reports** - Cross-handbook placeholder analysis
- ✅ **Test Suite Enhancement** - 93% pass rate with 144 placeholder tests
- ✅ **Documentation Updates** - Complete validation and test reports
- ✅ **27 New Templates** - Hardening baselines for OS and applications (54 with DE/EN)
- ✅ **Foundation Templates** - Overview, scope, lifecycle, exceptions, testing
- ✅ **OS Hardening** - Windows Server/Client, Linux, macOS, Containers
- ✅ **App Hardening** - Web servers, databases, Kubernetes, Docker, SSH, Identity
- ✅ **Fully Bilingual** - German and English with identical structure
- ✅ **90+ New Tests** - Property-based and integration tests
- ✅ **Backward Compatible** - All existing handbook types work unchanged
- ✅ **240 Templates Total** - Across 5 handbook types

## New in Version 0.0.3

- ✅ **Complete PDF Generation** - All 8 handbooks available as PDF (3.4 MB)
- ✅ **Pandoc + XeLaTeX Integration** - Professional PDF generation with TOC
- ✅ **Batch Generation** - Automatic generation of all handbooks
- ✅ **784 Files Generated** - 388 HTML + 8 PDF + 388 Markdown
- ✅ **Helper Scripts** - Automated generation scripts in `helpers/`
- ✅ **Separate Directories** - Each handbook in its own directory
- ✅ **Production Ready** - All formats ready for use

**Generated Handbooks:**
- 🇩🇪 German: BCM, ISMS, BSI Grundschutz, IT-Operation (HTML + PDF)
- 🇬🇧 English: BCM, ISMS, BSI Grundschutz, IT-Operation (HTML + PDF)

## Installation

### Prerequisites

- Python 3.8 or higher (recommended: Python 3.11+)
- pip (Python Package Manager)
- Pandoc + XeLaTeX (for PDF generation)

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

4. Enable PDF generation (recommended):
```bash
# For PDF generation with Pandoc + XeLaTeX (recommended)
sudo apt-get install pandoc texlive-xetex

# Or for WeasyPrint (experimental, not recommended)
sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0
```

## Quick Start

### Generate Single Handbook

```bash
# Generate HTML handbook
./handbook-generator -l en -t bcm -o html --test

# Generate PDF handbook (requires Pandoc + XeLaTeX)
./handbook-generator -l en -t isms -o pdf --test --pdf-toc

# Generate all formats
./handbook-generator -l en -t bcm -o all --test --separate-files --pdf-toc
```

### Generate All Handbooks (Batch)

```bash
# Generate all HTML handbooks (8 handbooks)
bash helpers/generate_all_handbooks.sh

# Generate all PDF handbooks (8 PDFs)
bash helpers/generate_pdfs_pandoc.sh
```

**Result:**
- 8 handbooks (4 types × 2 languages)
- 388 HTML files
- 8 PDF files (3.4 MB)
- 388 Markdown files
- Total: 784 files

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

**Important:** Since version 2.0, the `--test` flag is required to generate outputs. This prevents accidental file overwrites.

```bash
# Generate IT-Operations handbook in English (test mode required)
python -m src.cli --language en --template it-operation --test

# Generate BCM handbook in German
python -m src.cli --language de --template bcm --test

# Generate ISMS handbook in English, PDF only
python -m src.cli --language en --template isms --output pdf --test

# Generate BSI Grundschutz handbook in German
python -m src.cli --language de --template bsi-grundschutz --test

# Generate CIS Controls handbook in German
python -m src.cli --language de --template cis-controls --test

# Generate CIS Controls handbook in English
python -m src.cli --language en --template cis-controls --test

# Generate CIS Controls handbook with all formats
python -m src.cli --language en --template cis-controls --output all --test --separate-files --pdf-toc

# Generate BCM handbook with verbose logging
python -m src.cli --language en --template bcm --verbose --test

# Use custom configuration file
python -m src.cli --config /path/to/config.yaml --language en --template it-operation --test
```

#### Available Parameters

- `--language, -l`: Select language (`de`, `en`)
- `--template, -t`: Select handbook type (`bcm`, `isms`, `bsi-grundschutz`, `it-operation`, `cis-controls`)
- `--output, -o`: Output format (`markdown`, `pdf`, `both`) [Default: `both`]
- `--test`: Enable test mode (required for output generation)
- `--verbose, -v`: Enable verbose logging
- `--config, -c`: Path to configuration file [Default: `config.yaml`]

#### Test Mode and Output Structure

**Since version 2.0**, the generator uses a consolidated output structure and requires the `--test` flag for safety.

**Since version 2.1**, each handbook is stored in a separate directory:

**New Output Structure (Version 2.1+):**
```
test-output/
├── de/                          # German outputs
│   ├── bcm/                     # BCM handbook
│   │   ├── markdown/            # Separate markdown files
│   │   │   ├── TOC.md          # Table of contents with links
│   │   │   ├── 0010_Zweck_und_Geltungsbereich.md
│   │   │   ├── 0020_BCM_Leitlinie_Policy.md
│   │   │   └── ...
│   │   ├── pdf/                 # PDF outputs
│   │   │   └── bcm_handbook.pdf
│   │   └── html/                # HTML mini-website
│   │       ├── index.html
│   │       └── ...
│   ├── isms/                    # ISMS handbook
│   │   ├── markdown/
│   │   ├── pdf/
│   │   └── html/
│   ├── bsi-grundschutz/         # BSI Grundschutz handbook
│   │   ├── markdown/
│   │   ├── pdf/
│   │   └── html/
│   └── it-operation/            # IT-Operations handbook
│       ├── markdown/
│       ├── pdf/
│       └── html/
└── en/                          # English outputs
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    └── it-operation/
```

**Advantages of new structure:**
- ✅ Each handbook has its own directory
- ✅ No file conflicts between different handbook types
- ✅ Easier navigation and organization
- ✅ Parallel generation of multiple handbooks possible
- ✅ Each handbook is self-contained and complete

**Why Test Mode?**
- **Safety**: Prevents accidental overwriting of production files
- **Consolidation**: All outputs in one place instead of scattered across `Handbook/` and `PDF_Output/`
- **Clarity**: Explicit activation makes output generation intentional

**Migration from Old Structure:**
- Old structure: `Handbook/{language}/{type}/` and `PDF_Output/{language}/{type}/`
- New structure: `test-output/{language}/{type}/{format}/`
- Files are named by template type (e.g., `bcm_handbook.pdf`)

**Without --test Flag:**
```bash
$ python -m src.cli --language en --template bcm
ERROR: Output generation requires --test flag. Use --test to enable test mode output.
```

#### Handbook Types

- **bcm**: Business Continuity Management (ISO 22301, BSI BCM Standards)
- **isms**: Information Security Management System (ISO 27001:2022, Annex A)
- **bsi-grundschutz**: BSI IT-Grundschutz (BSI Standards 200-1, 200-2, 200-3)
- **it-operation**: IT Operations Handbook (ITIL v4, ISO 20000-1, COBIT 2019)
- **cis-controls**: CIS Controls v8 Hardening Templates (CIS Controls v8 Framework)

#### CIS Controls Template Structure

The CIS Controls templates are organized into four categories (27 templates, numbering 0010-0410):

**1. Foundation (0010-0050)** - 5 Templates
- Overview and approach
- Scope and asset groups
- Hardening lifecycle
- Exceptions and risk acceptance
- Testing and validation

**2. Operating Systems (0100-0150)** - 6 Templates
- Windows Server Hardening Baseline
- Windows Client Hardening Baseline
- Linux Hardening Baseline
- macOS Hardening Baseline
- Container Base Images Hardening

**3. Applications (0200-0330)** - 14 Templates
- Web servers (Nginx, Apache, IIS, Tomcat)
- Databases (PostgreSQL, MySQL, MS SQL Server)
- Container platforms (Kubernetes, Docker)
- Services (SSH, Identity/AD)

**4. Appendices (0400-0410)** - 2 Templates
- Control Mapping Template
- Checklists and Evidence

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
│   ├── it-operation/            # IT Operations Handbook (31 Templates)
│   │   ├── README.md
│   │   ├── 0010_Einleitung.md
│   │   └── ... (29 more)
│   └── cis-controls/            # CIS Controls v8 Hardening (27 Templates)
│       ├── 0000_metadata_de_cis-controls.md
│       ├── 0010_CIS_Controls_Ueberblick_und_Vorgehen.md
│       ├── 0020_Geltungsbereich_Assetgruppen_und_Tiering.md
│       └── ... (25 more)
└── en/                          # English templates
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    ├── it-operation/
    └── cis-controls/            # CIS Controls v8 Hardening (27 Templates)
        ├── 0000_metadata_en_cis-controls.md
        ├── 0010_CIS_Controls_Overview_and_Approach.md
        ├── 0020_Scope_Asset_Groups_and_Tiering.md
        └── ... (25 more)
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

Generated handbooks are saved in the `test-output/` directory:

```
test-output/
├── de/
│   ├── bcm/
│   │   ├── markdown/
│   │   ├── pdf/
│   │   │   └── bcm_handbook_de.pdf
│   │   └── html/
│   ├── isms/
│   │   ├── markdown/
│   │   ├── pdf/
│   │   │   └── isms_handbook_de.pdf
│   │   └── html/
│   ├── bsi-grundschutz/
│   │   ├── markdown/
│   │   ├── pdf/
│   │   │   └── bsi-grundschutz_handbook_de.pdf
│   │   └── html/
│   └── it-operation/
│       ├── markdown/
│       ├── pdf/
│       │   └── it-operation_handbook_de.pdf
│       └── html/
└── en/
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    └── it-operation/
```

### Viewing Generated Handbooks

After generation, you can view the handbooks as follows:

**HTML Handbooks:**
```bash
# Open in browser
firefox test-output/en/bcm/html/index.html

# Or start local web server
cd test-output
python3 -m http.server 8000
# Then open: http://localhost:8000/
```

**PDF Handbooks:**
```bash
# Open PDF
evince test-output/en/isms/pdf/isms_handbook_en.pdf

# List all PDFs
ls test-output/*/*/pdf/*.pdf
```

**Markdown Files:**
```bash
# View individual markdown files
cat test-output/en/bcm/markdown/0010_Purpose_and_Scope.md

# View table of contents
cat test-output/en/bcm/markdown/TOC.md
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

- **[OUTPUT_FORMATS_GUIDE.md](docs/OUTPUT_FORMATS_GUIDE.md)** - Detailed guide to all output formats (Separate Markdown, PDF with TOC, HTML)
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

The `helpers/` directory contains batch generation scripts:

**generate_all_handbooks.sh** - Generates all HTML handbooks automatically
```bash
bash helpers/generate_all_handbooks.sh
```
- Generates 8 handbooks (4 types × 2 languages)
- 388 HTML files
- Automatic progress tracking

**generate_pdfs_pandoc.sh** - Generates all PDF handbooks automatically
```bash
bash helpers/generate_pdfs_pandoc.sh
```
- Generates 8 PDFs (4 types × 2 languages)
- 3.4 MB total size
- Professional formatting with TOC

More details: [helpers/README.md](helpers/README.md)

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
