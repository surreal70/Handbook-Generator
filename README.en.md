# Handbook Generator

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.0.22-green.svg)](about_versioning/VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://img.shields.io/badge/coverage-72%25-yellow.svg)](htmlcov/index.html)
[![Tests](https://img.shields.io/badge/tests-7635%20total-success.svg)](tests/)
[![Documentation](https://img.shields.io/badge/docs-complete-blue.svg)](docs/)

**A professional Python tool for generating standards-compliant handbooks**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Development](#development)

**Languages:** [🇩🇪 Deutsch](README.md) | [🇬🇧 English](README.en.md)

</div>

---

A Python tool for generating professional handbooks from Markdown templates with placeholder replacement from external data sources.

<div align="center">
  <img src="logo/HandBook-Generator.png" alt="Handbook Generator Logo" width="400"/>
</div>

## 🎯 Important Notice

**This is Version 0.0.22 - Limited Production Use**

This version is ready for:
- ✅ Markdown handbook generation (all 44 handbooks)
- ✅ Documentation projects
- ✅ Compliance documentation
- ✅ Development and test environments
- ✅ Inline placeholder support
- ✅ Handbook-specific metadata

Limitations:
- ⚠️ **PDF Generation: HIGHLY EXPERIMENTAL AND PARTIALLY BROKEN**
  - ReportLab Engine: Functional but TOC formatting incomplete
  - WeasyPrint Engine: Requires system libraries (libpango), often non-functional
  - **Recommendation**: Use Markdown output and convert externally
- ⚠️ HTML output not comprehensively tested

See [Release Notes](about_versioning/VERSION_0.0.22_RELEASE_NOTES.md) for details.

## Overview

The Handbook Generator creates professional handbooks in various formats (HTML, PDF, Markdown) from structured Markdown templates. The system replaces placeholders in templates with real data from external systems like NetBox and supports multilingual handbooks.

**Version 0.0.22** - ⚠️ Limited Production Use - Core functionality stable, PDF generation experimental

## Features

- 📝 **Template-based Document Generation** - Structured Markdown templates with intelligent processing
- 📚 **22 Handbook Types** - BCM, ISMS, BSI Grundschutz, IT-Operations, CIS Controls, Common Criteria, COSO, CSA CCM, DORA, GDPR, HIPAA, IDW PS 951, ISO 9001, ISO 31000, ISO 38500, NIST 800-53, NIST CSF, PCI-DSS, SOC 1, TISAX, TOGAF, TSC
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
- 📦 **1,732+ Templates** - Professional, standards-compliant templates (866 DE + 866 EN)
- 🚀 **Batch Generation** - Automatic generation of all handbooks

## Handbook Types

| Type | Standard | Templates (DE/EN) | Description |
|------|----------|-------------------|-------------|
| **BCM** | ISO 22301, BSI BCM | 29/29 | Business Continuity Management |
| **ISMS** | ISO 27001:2022, Annex A | 70/70 | Information Security Management System |
| **BSI Grundschutz** | BSI 200-1/2/3 | 54/54 | IT-Grundschutz according to BSI |
| **IT-Operation** | ITIL v4, ISO 20000-1 | 30/30 | IT Operations Handbook |
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

**Total: 866+ Templates (DE) / 866+ Templates (EN)** across 22 Compliance Frameworks

## What's New?

For detailed information about all releases, see:

📜 **[Version History](about_versioning/VERSION.md)** - Complete overview of all versions with release notes and changes

## Unified Metadata Structure

All template frameworks use a unified metadata structure for consistent documentation information and version tracking.

**Documentation:**
- 📋 **[METADATA_REFERENCE.md](docs/METADATA_REFERENCE.md)** - Complete metadata reference with all fields and descriptions
- 📋 **[PLACEHOLDER_REFERENCE.md](docs/PLACEHOLDER_REFERENCE.md)** - Placeholder syntax and usage
- 📋 **[TEMPLATE_HEADER_SPECIFICATION.md](docs/TEMPLATE_HEADER_SPECIFICATION.md)** - Template header structure and requirements
- ⚙️ **[CONFIGURATION_REFERENCE.md](docs/CONFIGURATION_REFERENCE.md)** - Configuration file reference and settings

**Tools:**
- `helpers/validate_metadata.py` - Metadata validation
- `helpers/generate_placeholder_matrix.py` - Generate placeholder overview

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

## PDF Engine Selection

⚠️ **WARNING: PDF generation is HIGHLY EXPERIMENTAL and PARTIALLY BROKEN**

Direct PDF generation via `--pdf-engine` is experimental in version 0.0.22 and has known issues:

**Known Issues:**
- ❌ ReportLab: TOC formatting incomplete, page breaks partially faulty
- ❌ WeasyPrint: Requires system libraries, often non-functional (libpango issues)
- ❌ Both engines: Not production-ready

**RECOMMENDATION for production environments:**
```bash
# 1. Generate Markdown
./handbook-generator -l en -t bcm -o markdown --test

# 2. Convert to PDF externally (e.g., with Pandoc)
pandoc output/en/bcm/markdown/bcm_handbook.md -o bcm_handbook.pdf --pdf-engine=xelatex --toc
```

### ReportLab (Experimental - Not recommended)

**Status:** ⚠️ Partially functional, but with limitations

**Known Issues:**
- TOC formatting incomplete
- Page breaks not consistent
- Not production-ready

**Installation:**
```bash
pip install reportlab markdown
```

**Usage (at your own risk):**
```bash
# Explicitly use ReportLab
./handbook-generator -l en -t bcm -o pdf --pdf-engine reportlab --test

# Auto-detection (prefers ReportLab)
./handbook-generator -l en -t bcm -o pdf --test
```

### WeasyPrint (Experimental - Often non-functional)

**Status:** ❌ Frequently broken due to system library issues

**Known Issues:**
- libpango libraries often fail to load
- Complex system dependencies
- Often doesn't work despite installed packages

**Installation:**
```bash
# Install Python package
pip install weasyprint

# Install system dependencies (often doesn't work)
# Ubuntu/Debian:
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0

# macOS:
brew install pango

# Windows:
# GTK3 Runtime from https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
```

**Usage (at your own risk):**
```bash
# Explicitly use WeasyPrint
./handbook-generator -l en -t bcm -o pdf --pdf-engine weasyprint --test
```

### Engine Comparison

| Feature | ReportLab | WeasyPrint | Pandoc (Recommended) |
|---------|-----------|------------|-------------------|
| Status | ⚠️ Experimental | ❌ Often broken | ✅ Production-ready |
| Installation | ⭐⭐⭐⭐ Easy | ⭐⭐ Difficult | ⭐⭐⭐⭐ Easy |
| Reliability | ⭐⭐⭐ Medium | ⭐ Poor | ⭐⭐⭐⭐⭐ Excellent |
| PDF Quality | ⭐⭐⭐ Acceptable | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Excellent |
| TOC Support | ⚠️ Partial | ✅ Complete | ✅ Complete |
| Recommendation | ⚠️ Testing only | ❌ Don't use | ✅ Use in production |

### Auto-Detection

If you don't specify `--pdf-engine`, the system automatically detects available engines:

**Preference Order:**
1. ReportLab (preferred, but experimental)
2. WeasyPrint (fallback, often broken)

```bash
# Use auto-detection (not recommended for production)
./handbook-generator -l en -t bcm -o pdf --test

# System automatically selects the best available engine
```

### Troubleshooting

**"No PDF engines available" error:**
```bash
# Install ReportLab (experimental)
pip install reportlab markdown

# Or WeasyPrint (often non-functional)
pip install weasyprint
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0  # Linux
```

**WeasyPrint "OSError" or "cairo" errors:**
```bash
# This is a known issue - WeasyPrint is often non-functional
# RECOMMENDATION: Use Pandoc instead

# 1. Generate Markdown
./handbook-generator -l en -t bcm -o markdown --test

# 2. Convert to PDF with Pandoc
pandoc output/en/bcm/markdown/bcm_handbook.md -o bcm.pdf --pdf-engine=xelatex --toc
```

**Check virtual environment:**
```bash
# Ensure you're in the virtual environment
source venv/bin/activate

# Check installed packages
pip list | grep -E '(reportlab|weasyprint|markdown)'

# Reinstall if needed
pip install --upgrade reportlab markdown
```

## Quick Start

### Generate Single Handbook

```bash
# Generate HTML handbook
./handbook-generator -l en -t bcm -o html --test

# Generate Markdown (RECOMMENDED for PDF conversion)
./handbook-generator -l en -t isms -o markdown --test

# Create PDF with Pandoc (RECOMMENDED)
pandoc output/en/isms/markdown/isms_handbook.md -o isms.pdf --pdf-engine=xelatex --toc

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

# Generate Common Criteria handbook
python -m src.cli --language en --template common-criteria --test

# Generate COSO handbook (Internal Control)
python -m src.cli --language en --template coso --test

# Generate CSA CCM handbook (Cloud Security)
python -m src.cli --language en --template csa-ccm --test

# Generate DORA handbook (Digital Resilience)
python -m src.cli --language en --template dora --test

# Generate GDPR handbook
python -m src.cli --language en --template gdpr --test

# Generate HIPAA handbook
python -m src.cli --language en --template hipaa --test

# Generate IDW PS 951 handbook
python -m src.cli --language en --template idw-ps-951 --test

# Generate ISO 9001 handbook
python -m src.cli --language en --template iso-9001 --test

# Generate ISO 31000 handbook (Risk Management)
python -m src.cli --language en --template iso-31000 --test

# Generate ISO 38500 handbook (IT Governance)
python -m src.cli --language en --template iso-38500 --test

# Generate NIST 800-53 handbook
python -m src.cli --language en --template nist-800-53 --test

# Generate NIST CSF handbook
python -m src.cli --language en --template nist-csf --test

# Generate PCI-DSS handbook
python -m src.cli --language en --template pci-dss --test

# Generate SOC 1 handbook (Service Organization Controls)
python -m src.cli --language en --template soc1 --test

# Generate TISAX handbook (Automotive Security)
python -m src.cli --language en --template tisax --test

# Generate TOGAF handbook
python -m src.cli --language en --template togaf --test

# Generate TSC (SOC 2) handbook
python -m src.cli --language en --template tsc --test

# Generate BCM handbook with verbose logging
python -m src.cli --language en --template bcm --verbose --test

# Use custom configuration file
python -m src.cli --config /path/to/config.yaml --language en --template it-operation --test
```

#### Available Parameters

- `--language, -l`: Select language (`de`, `en`)
- `--template, -t`: Select handbook type (`bcm`, `isms`, `bsi-grundschutz`, `it-operation`, `cis-controls`, `common-criteria`, `coso`, `csa-ccm`, `dora`, `gdpr`, `hipaa`, `idw-ps-951`, `iso-9001`, `iso-31000`, `iso-38500`, `nist-800-53`, `nist-csf`, `pci-dss`, `soc1`, `tisax`, `togaf`, `tsc`)
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
- **[DOCUMENT_HISTORY_GUIDE.md](docs/DOCUMENT_HISTORY_GUIDE.md)** - Guide to standardized document history in templates
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
