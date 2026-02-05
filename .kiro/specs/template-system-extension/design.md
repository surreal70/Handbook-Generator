# Design Document: Template System Extension

## Overview

This design extends the existing handbook generator system to support three additional template types (BCM, ISMS, BSI Grundschutz) and adds HTML comment support for non-rendered documentation. The extension maintains full backward compatibility with existing it-operation templates while adding comprehensive, standards-compliant templates for Business Continuity Management (ISO 22301), Information Security Management (ISO 27001:2022), and BSI IT-Grundschutz.

The design follows the existing architecture pattern: templates are organized by language and type, use the same placeholder system (meta and netbox), and generate output through the same CLI interface. The HTML comment feature adds a preprocessing step to strip non-rendered documentation before placeholder processing.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         CLI Interface                        │
│  (Existing: --language, --template, --output)               │
│  (Extended: bcm, isms, bsi-grundschutz template types)      │
│  (Extended: --output html for HTML mini-website)            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 Configuration Manager                        │
│  - Loads config.yaml (manual metadata)                      │
│  - Loads metadata-netbox.yaml (NetBox metadata)             │
│  - Manages per-handbook versioning                          │
│  - Handles role configuration for NetBox                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              NetBox Metadata Loader (NEW)                    │
│  - Fetches contacts with roles from NetBox                  │
│  - Fetches device information from NetBox                   │
│  - Fetches site information from NetBox                     │
│  - Populates metadata-netbox.yaml once per run              │
│  - Applies configured role distinction logic                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    Template Manager                          │
│  - Discovers templates by language/type                     │
│  - Validates template structure                             │
│  - Loads template content                                   │
│  (Extended: Supports bcm, isms, bsi-grundschutz)           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              HTML Comment Processor                          │
│  - Strips <!-- comment --> from templates                   │
│  - Handles single-line and multi-line comments              │
│  - Preserves surrounding markdown                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 Placeholder Processor                        │
│  - Detects {{ source.field }} placeholders                  │
│  - Routes to appropriate data source adapter                │
│  - Replaces placeholders with actual data                   │
│  (Extended: Supports meta-netbox.* placeholders)            │
│  (Extended: Supports handbook.* placeholders)               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   Output Generator                           │
│  - Assembles processed templates                            │
│  (Extended: Generates separate Markdown files with TOC)     │
│  (Extended: Generates PDF with TOC and page breaks)         │
│  (Extended: Generates HTML mini-website with navigation)    │
└─────────────────────────────────────────────────────────────┘
```

### Directory Structure

```
templates/
├── de/
│   ├── it-operation/          # Existing (29 templates, 0010-0290)
│   ├── bcm/                   # NEW (30 templates, 0010-0290)
│   │   ├── README.md
│   │   ├── 0010_Zweck_und_Geltungsbereich.md
│   │   ├── 0020_BCM_Leitlinie_Policy.md
│   │   └── ... (28 more)
│   ├── isms/                  # NEW (~50 templates, 0010-0740)
│   │   ├── README.md
│   │   ├── 0010_ISMS_Informationssicherheitsleitlinie.md
│   │   ├── 0020_ISMS_Geltungsbereich_Scope.md
│   │   └── ... (48 more)
│   └── bsi-grundschutz/       # NEW (~40 templates, 0010-0740)
│       ├── README.md
│       ├── 0010_Informationssicherheitsleitlinie.md
│       ├── 0020_ISMS_Organisation_Rollen_RACI.md
│       └── ... (38 more)
└── en/
    ├── it-operation/          # Existing (29 templates, 0010-0290)
    ├── bcm/                   # NEW (30 templates, 0010-0290)
    ├── isms/                  # NEW (~50 templates, 0010-0740)
    └── bsi-grundschutz/       # NEW (~40 templates, 0010-0740)
```

## Components and Interfaces

### 1. HTML Comment Processor (NEW)

**Purpose**: Strip HTML-style comments from templates before placeholder processing.

**Interface**:
```python
class HTMLCommentProcessor:
    """Processes templates to remove HTML comments."""
    
    def remove_comments(self, content: str) -> str:
        """
        Remove all HTML comments from content.
        
        Args:
            content: Template content with potential HTML comments
            
        Returns:
            Content with all HTML comments removed
        """
        pass
    
    def validate_comments(self, content: str) -> list[str]:
        """
        Validate HTML comments for common issues.
        
        Args:
            content: Template content to validate
            
        Returns:
            List of validation warnings
        """
        pass
```

**Implementation Details**:
- Uses regex pattern: `<!--.*?-->` (non-greedy, DOTALL flag for multiline)
- Handles nested comments by removing outermost comment markers
- Preserves whitespace and markdown formatting
- Integrated into PlaceholderProcessor before placeholder detection

**Edge Cases**:
- Empty comments: `<!-- -->`
- Comments with special characters: `<!-- TODO: Fix {{ meta.org }} -->`
- Multi-line comments spanning multiple paragraphs
- Comments adjacent to markdown syntax: `<!-- comment -->## Header`

### 2. Template Manager (EXTENDED)

**Existing Functionality**: Discovers and loads templates by language/type.

**Extensions**:
- Recognizes new template types: `bcm`, `isms`, `bsi-grundschutz`
- Validates template numbering consistency (0010-0290 for bcm, 0010-0740 for isms/bsi)
- Supports README.md files in each template directory

**No Code Changes Required**: The existing TemplateManager already supports arbitrary template types through directory scanning.

### 3. CLI Interface (EXTENDED)

**Existing Functionality**: Parses command-line arguments for language, template type, output format.

**Extensions**:
```python
parser.add_argument(
    '--template', '-t',
    type=str,
    choices=['backup', 'bcm', 'isms', 'it-operation', 'bsi-grundschutz'],  # Extended
    help='Template type/category for handbook'
)
```

**Backward Compatibility**: Existing `it-operation` and `backup` templates continue to work unchanged.

### 4. Template Validation (NEW)

**Purpose**: Ensure template quality and consistency.

**Interface**:
```python
class TemplateValidator:
    """Validates template content for quality and consistency."""
    
    def validate_raci_matrix(self, content: str) -> list[str]:
        """Validate RACI matrix completeness."""
        pass
    
    def validate_framework_references(self, content: str, template_type: str) -> list[str]:
        """Validate presence of framework references."""
        pass
    
    def validate_placeholder_syntax(self, content: str) -> list[str]:
        """Validate placeholder syntax correctness."""
        pass
    
    def validate_numbering(self, templates: list[Template]) -> list[str]:
        """Validate template numbering sequence."""
        pass
```

**Validation Rules**:
- RACI matrices must have at least one R (Responsible) and one A (Accountable) per row
- Framework references must be present in appropriate templates (ISO 22301 for BCM, ISO 27001 for ISMS, BSI 200-x for Grundschutz)
- Placeholders must follow `{{ source.field }}` syntax
- Template numbering must be sequential with no gaps

### 5. NetBox Metadata Loader (NEW)

**Purpose**: Fetch metadata from NetBox and populate metadata-netbox.yaml file once per run.

**Interface**:
```python
class NetBoxMetadataLoader:
    """Loads metadata from NetBox and creates metadata-netbox.yaml."""
    
    def __init__(self, netbox_url: str, api_token: str, role_config: dict):
        """
        Initialize NetBox loader.
        
        Args:
            netbox_url: URL of NetBox instance
            api_token: API token for authentication
            role_config: Configuration for role distinction
        """
        pass
    
    def load_metadata(self) -> dict:
        """
        Load all metadata from NetBox.
        
        Returns:
            Dictionary with contacts, devices, sites
        """
        pass
    
    def fetch_contacts_with_roles(self) -> dict:
        """
        Fetch contacts from NetBox and assign roles.
        
        Returns:
            Dictionary mapping roles to contact information
        """
        pass
    
    def fetch_devices(self) -> dict:
        """
        Fetch device information from NetBox.
        
        Returns:
            Dictionary with device data
        """
        pass
    
    def fetch_sites(self) -> dict:
        """
        Fetch site information from NetBox.
        
        Returns:
            Dictionary with site data
        """
        pass
    
    def save_to_yaml(self, metadata: dict, filepath: str) -> None:
        """
        Save metadata to YAML file.
        
        Args:
            metadata: Metadata dictionary
            filepath: Path to metadata-netbox.yaml
        """
        pass
```

**Implementation Details**:
- Connects to NetBox API using pynetbox library
- Applies role distinction logic based on configuration
- Supports field-based role assignment (e.g., contact.role, contact.tags)
- Supports name-based role assignment (e.g., "CISO" in name)
- Creates metadata-netbox.yaml in project root
- Runs once at start of handbook generation

**Role Distinction Configuration**:
```yaml
# In config.yaml
netbox:
  url: "https://netbox.example.com"
  api_token: "token_here"
  role_distinction:
    method: "field"  # or "name" or "tags"
    field: "role"    # if method is "field"
    mappings:
      "CISO": "Chief Information Security Officer"
      "CIO": "Chief Information Officer"
      "Sysop": "System Administrator"
      # ... more mappings
```

### 6. Configuration Manager (EXTENDED)

**Purpose**: Manage configuration including per-handbook versioning and metadata.

**Extended Interface**:
```python
class ConfigurationManager:
    """Manages system configuration and metadata."""
    
    def load_config(self, config_path: str) -> dict:
        """Load main configuration file."""
        pass
    
    def load_metadata(self, metadata_path: str) -> dict:
        """Load manual metadata from metadata.yaml."""
        pass
    
    def load_netbox_metadata(self, netbox_metadata_path: str) -> dict:
        """Load NetBox metadata from metadata-netbox.yaml."""
        pass
    
    def get_handbook_metadata(self, handbook_type: str) -> dict:
        """
        Get metadata for specific handbook type.
        
        Args:
            handbook_type: Type of handbook (bcm, isms, etc.)
            
        Returns:
            Dictionary with version, owner, approver, date
        """
        pass
    
    def get_role_metadata(self, role: str, source: str = "meta") -> dict:
        """
        Get metadata for specific role.
        
        Args:
            role: Role name (ciso, cio, sysop, etc.)
            source: Source of metadata ("meta" or "meta-netbox")
            
        Returns:
            Dictionary with name, email, phone
        """
        pass
```

**Per-Handbook Metadata Structure**:
```yaml
# In metadata.yaml
handbooks:
  bcm:
    version: "1.0.0"
    owner: "John Doe"
    approver: "Jane Smith"
    date: "2025-01-15"
  isms:
    version: "2.1.0"
    owner: "Alice Johnson"
    approver: "Bob Williams"
    date: "2025-01-20"
  bsi-grundschutz:
    version: "1.5.0"
    owner: "Charlie Brown"
    approver: "Diana Prince"
    date: "2025-01-10"
  it-operation:
    version: "3.0.0"
    owner: "Eve Adams"
    approver: "Frank Castle"
    date: "2025-01-05"

roles:
  ciso:
    name: "John Security"
    email: "john.security@example.com"
    phone: "+49 123 456789"
  cio:
    name: "Jane Tech"
    email: "jane.tech@example.com"
    phone: "+49 123 456790"
  sysop:
    name: "Bob Admin"
    email: "bob.admin@example.com"
    phone: "+49 123 456791"
  datenschutzbeauftragter:
    name: "Alice Privacy"
    email: "alice.privacy@example.com"
    phone: "+49 123 456792"
  risikomanager:
    name: "Charlie Risk"
    email: "charlie.risk@example.com"
    phone: "+49 123 456793"
  interner_auditor:
    name: "Diana Audit"
    email: "diana.audit@example.com"
    phone: "+49 123 456794"
  personalleitung:
    name: "Eve HR"
    email: "eve.hr@example.com"
    phone: "+49 123 456795"
  it_manager:
    name: "Frank IT"
    email: "frank.it@example.com"
    phone: "+49 123 456796"
```

### 7. Placeholder Processor (EXTENDED)

**Extended Functionality**: Support new placeholder types.

**New Placeholder Types**:

**Handbook-Specific Placeholders**:
```markdown
**Version:** {{ handbook.version }}
**Dokumentverantwortlicher:** {{ handbook.owner }}
**Genehmiger:** {{ handbook.approver }}
**Datum:** {{ handbook.date }}
```

**NetBox Metadata Placeholders**:
```markdown
**CISO (NetBox):** {{ meta-netbox.ciso.name }} ({{ meta-netbox.ciso.email }})
**Standort (NetBox):** {{ meta-netbox.sites.primary.name }}
**Gerät (NetBox):** {{ meta-netbox.devices.firewall.name }}
```

**Extended Role Placeholders**:
```markdown
**Systemadministrator:** {{ meta.sysop.name }}
**Datenschutzbeauftragter:** {{ meta.datenschutzbeauftragter.name }}
**Risikomanager:** {{ meta.risikomanager.name }}
**Interner Auditor:** {{ meta.interner_auditor.name }}
**Personalleitung:** {{ meta.personalleitung.name }}
**IT-Manager:** {{ meta.it_manager.name }}
```

**English Translation** (automatic in English templates):
```markdown
**System Administrator:** {{ meta.sysop.name }}
**Data Protection Officer:** {{ meta.datenschutzbeauftragter.name }}
**Risk Manager:** {{ meta.risikomanager.name }}
**Internal Auditor:** {{ meta.interner_auditor.name }}
**HR Manager:** {{ meta.personalleitung.name }}
**IT Manager:** {{ meta.it_manager.name }}
```

### 8. Output Generator (EXTENDED)

**Extended Functionality**: Support HTML output, separate markdown files, and PDF with TOC.

**New Output Formats**:

**HTML Mini-Website**:
```python
class HTMLOutputGenerator:
    """Generates HTML mini-website from templates."""
    
    def generate_html_site(self, templates: list[Template], output_dir: str) -> None:
        """
        Generate HTML mini-website.
        
        Args:
            templates: List of processed templates
            output_dir: Output directory for HTML files
        """
        pass
    
    def generate_toc_page(self, templates: list[Template]) -> str:
        """
        Generate table of contents HTML page.
        
        Args:
            templates: List of templates
            
        Returns:
            HTML content for TOC page
        """
        pass
    
    def generate_template_page(self, template: Template, prev_link: str, next_link: str) -> str:
        """
        Generate HTML page for single template.
        
        Args:
            template: Template to render
            prev_link: Link to previous page
            next_link: Link to next page
            
        Returns:
            HTML content for template page
        """
        pass
    
    def apply_styling(self, html_content: str) -> str:
        """
        Apply consistent CSS styling.
        
        Args:
            html_content: Raw HTML content
            
        Returns:
            Styled HTML content
        """
        pass
```

**Separate Markdown Files**:
```python
class SeparateMarkdownGenerator:
    """Generates separate markdown files for each template."""
    
    def generate_separate_files(self, templates: list[Template], output_dir: str) -> None:
        """
        Generate separate markdown file for each template.
        
        Args:
            templates: List of processed templates
            output_dir: Output directory for markdown files
        """
        pass
    
    def generate_toc_file(self, templates: list[Template], output_dir: str) -> None:
        """
        Generate table of contents markdown file.
        
        Args:
            templates: List of templates
            output_dir: Output directory
        """
        pass
```

**PDF with Table of Contents**:
```python
class PDFWithTOCGenerator:
    """Generates PDF with table of contents and page breaks."""
    
    def generate_pdf_with_toc(self, templates: list[Template], output_path: str) -> None:
        """
        Generate PDF with TOC and page breaks.
        
        Args:
            templates: List of processed templates
            output_path: Output PDF file path
        """
        pass
    
    def generate_toc_content(self, templates: list[Template]) -> str:
        """
        Generate table of contents content.
        
        Args:
            templates: List of templates
            
        Returns:
            Markdown content for TOC
        """
        pass
    
    def add_page_breaks(self, content: str) -> str:
        """
        Add page breaks between templates.
        
        Args:
            content: Combined markdown content
            
        Returns:
            Content with page break markers
        """
        pass
```

**Output Directory Structure**:
```
Handbook/
├── de/
│   ├── bcm/
│   │   ├── markdown/              # NEW: Separate markdown files
│   │   │   ├── TOC.md
│   │   │   ├── 0010_Zweck_und_Geltungsbereich.md
│   │   │   ├── 0020_BCM_Leitlinie_Policy.md
│   │   │   └── ...
│   │   ├── html/                  # NEW: HTML mini-website
│   │   │   ├── index.html         # TOC page
│   │   │   ├── 0010_Zweck_und_Geltungsbereich.html
│   │   │   ├── 0020_BCM_Leitlinie_Policy.html
│   │   │   ├── styles.css
│   │   │   └── ...
│   │   └── bcm_handbook_de.pdf    # PDF with TOC
│   └── ...
└── en/
    └── ...
```

## Data Models

### Template Structure

**BCM Templates** (30 files, 0010-0290):
```
0010_Zweck_und_Geltungsbereich.md
0020_BCM_Leitlinie_Policy.md
0030_Dokumentenlenkung_und_Versionierung.md
0040_Notfallorganisation_Rollen_und_Gremien.md
0050_Kontakte_und_Eskalation.md
0060_Service_und_Prozesskatalog_Kritikalitaet.md
0070_BIA_Methodik.md
0080_BIA_Ergebnisse_und_RTO_RPO.md
0090_Risikoanalyse_und_Szenarien.md
0100_Strategie_und_Kontinuitaetsoptionen.md
0110_Aktivierungskriterien_und_Entscheidungsbaum.md
0120_Krisenmanagementplan.md
0130_Kommunikationsplan_Intern_Extern.md
0140_BCP_Geschaeftsfortfuehrungsplan_Template.md
0150_DRP_IT_Wiederanlaufplan_Template.md
0160_Backup_und_Restore_Plan.md
0170_Alternativstandort_und_Notfallarbeitsplaetze.md
0180_Lieferanten_und_Drittparteien_Kontinuitaet.md
0190_Ressourcenplanung_und_Mindestbesetzung.md
0200_Notfallzugang_BreakGlass.md
0210_Cyber_Incident_und_Ransomware_Playbook.md
0220_Uebungs_und_Testprogramm.md
0230_Testprotokoll_und_Erfolgskriterien.md
0240_Nachbereitung_Postmortem.md
0250_Pflege_Review_und_KPIs.md
0260_Schulungen_und_Sensibilisierung.md
0270_Compliance_Audit_und_Nachweise.md
0280_Anhang_Vorlagen_und_Checklisten.md
0290_Glossar_und_Abkuerzungen.md
```

**ISMS Templates** (~50 files, 0010-0740):
- **Basis ISMS** (0010-0160): Foundation documents
- **Abstract Policies** (0200-0680, even numbers): High-level policies
- **Detailed Guidelines** (0210-0690, odd numbers): Implementation guidelines
- **Appendices** (0710-0740): Supporting documents

**BSI Grundschutz Templates** (~40 files, 0010-0740):
- **ISMS Foundation** (0010-0100): Policy, Organization, Scope
- **Security Concept** (0100-0110): Gap Analysis, Risk Analysis
- **Policies and Guidelines** (0200-0530): Detailed security policies
- **Management Processes** (0600-0630): Training, Audits, Reviews
- **Appendices** (0700-0740): Evidence, Assets, Data Flows

### Placeholder Usage

All templates use the existing placeholder system:

**Meta Placeholders** (Organization-wide metadata):
```markdown
**Organisation:** {{ meta.organization.name }}
**CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
**CISO:** {{ meta.ciso.name }} ({{ meta.ciso.email }})
**Dokumentverantwortlicher:** {{ meta.document.owner }}
```

**NetBox Placeholders** (Infrastructure data):
```markdown
**Standort:** {{ netbox.site.name }}
**Core Switch:** {{ netbox.device.core_switch.name }}
**Management VLAN:** {{ netbox.vlan.management.vid }}
```

### HTML Comment Usage

Templates can include non-rendered documentation:

```markdown
<!-- 
TEMPLATE AUTHOR NOTE:
This section requires customization based on your organization's 
specific BCM strategy. Consider the following:
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)
- Critical business processes
-->

## Business Impact Analysis

[TODO: Complete BIA based on your organization's requirements]

<!-- End of customization section -->
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: HTML Comment Removal Completeness

*For any* template content containing HTML comments, after processing, the output SHALL NOT contain any HTML comment markers (`<!--` or `-->`).

**Validates: Requirements 16.1, 17.1, 17.2**

### Property 2: HTML Comment Removal Preserves Markdown

*For any* template content with HTML comments, removing comments SHALL preserve all non-comment markdown content exactly, including formatting, headers, lists, and code blocks.

**Validates: Requirements 17.3, 17.4, 17.5**

### Property 3: Template Type Discovery

*For any* valid template directory structure, the system SHALL discover all template types (it-operation, bcm, isms, bsi-grundschutz) and correctly identify available languages for each type.

**Validates: Requirements 21.1, 21.2, 21.3, 21.4**

### Property 4: Bilingual Template Consistency

*For any* template type, the German and English versions SHALL have identical numbering, identical placeholder usage, and identical structural organization.

**Validates: Requirements 3.3, 3.4, 3.5, 8.3, 8.4, 8.5, 13.3, 13.4, 13.5**

### Property 5: Placeholder Processing Independence

*For any* template type (it-operation, bcm, isms, bsi-grundschutz), placeholder processing SHALL work identically, replacing `{{ meta.* }}` and `{{ netbox.* }}` placeholders with the same data sources.

**Validates: Requirements 20.1, 24.1, 24.2**

### Property 6: Template Numbering Sequence

*For any* set of templates in a template type directory, when sorted by filename, the numeric prefixes SHALL form a valid sequence with no duplicates.

**Validates: Requirements 23.2, 23.3, 23.4, 23.5**

### Property 7: RACI Matrix Completeness

*For any* RACI matrix in a template, each activity row SHALL have exactly one 'A' (Accountable) and at least one 'R' (Responsible).

**Validates: Requirements 2.3, 6.4, 11.5**

### Property 8: Framework Reference Presence

*For any* BCM template, at least one reference to ISO 22301 or BSI BCM standards SHALL be present. *For any* ISMS template, at least one reference to ISO 27001:2022 SHALL be present. *For any* BSI Grundschutz template, at least one reference to BSI Standards 200-1, 200-2, or 200-3 SHALL be present.

**Validates: Requirements 2.1, 2.2, 6.1, 6.2, 11.1, 11.2, 11.3**

### Property 9: Output Structure Consistency

*For any* template type and language combination, generated output SHALL be stored in `Handbook/{language}/{template-type}/` with filenames following the pattern `{template-type}_handbook_{language}.{ext}`.

**Validates: Requirements 25.1, 25.2, 25.3**

### Property 10: Backward Compatibility

*For any* existing it-operation template, processing with the extended system SHALL produce identical output to the original system (when HTML comments are not present).

**Validates: Requirements 20.1, 20.2, 20.3, 20.4, 20.5**

### Property 11: HTML Comment Multiline Handling

*For any* HTML comment spanning multiple lines, the entire comment including all intermediate lines SHALL be removed, leaving no comment markers or partial comment content.

**Validates: Requirements 16.3, 17.2**

### Property 12: Placeholder Syntax Validation

*For any* template content, all placeholders SHALL match the pattern `{{ source.field }}` where source is alphanumeric and field can contain dots for nested paths.

**Validates: Requirements 22.1, 24.3**

### Property 13: Template README Presence

*For any* template type directory (bcm, isms, bsi-grundschutz), a README.md file SHALL be present explaining template structure, placeholder usage, and framework compliance.

**Validates: Requirements 4.1, 4.2, 9.1, 9.2, 14.1, 14.2**

### Property 14: CLI Template Type Validation

*For any* CLI invocation with `--template` parameter, if the template type is not in the valid set (backup, bcm, isms, it-operation, bsi-grundschutz), the system SHALL reject the input with an error message listing valid options.

**Validates: Requirements 21.5**

### Property 15: ISMS Three-Tier Structure

*For any* ISMS template set, templates SHALL be organized into three distinct tiers: Basis ISMS (0010-0160), Abstract Policies (0200-0680 even), and Detailed Guidelines (0210-0690 odd).

**Validates: Requirements 7.1, 7.2, 7.3, 7.4, 7.5**

### Property 16: Per-Handbook Metadata Independence

*For any* handbook type (bcm, isms, bsi-grundschutz, it-operation), the system SHALL support independent version numbers, owners, approvers, and dates, such that changing metadata for one handbook does not affect any other handbook.

**Validates: Requirements 26.1, 26.2, 26.3, 26.4**

### Property 17: Handbook Placeholder Support

*For any* handbook type, placeholders in the format `{{ handbook.version }}`, `{{ handbook.owner }}`, `{{ handbook.approver }}`, and `{{ handbook.date }}` SHALL be replaced with the correct handbook-specific metadata.

**Validates: Requirements 26.5**

### Property 18: NetBox Metadata Loading

*For any* valid NetBox configuration, when the system starts, it SHALL fetch contacts, devices, and sites from NetBox exactly once before document processing begins, and populate metadata-netbox.yaml with the fetched data.

**Validates: Requirements 27.2, 27.3, 27.4, 27.5**

### Property 19: Meta-NetBox Placeholder Support

*For any* template containing `{{ meta-netbox.* }}` placeholders, the system SHALL replace them with data from metadata-netbox.yaml, and both `{{ meta.* }}` and `{{ meta-netbox.* }}` placeholders SHALL work independently in the same template.

**Validates: Requirements 28.1, 28.2, 28.3, 28.4, 28.5**

### Property 20: NetBox Role Distinction Application

*For any* configured role distinction method (field-based or name-based), when loading NetBox data, the system SHALL apply the configured logic to map NetBox contacts to roles, and the configuration SHALL be persisted in config.yaml.

**Validates: Requirements 29.4, 29.5**

### Property 21: Extended Role Support

*For any* of the six new roles (sysop, datenschutzbeauftragter, risikomanager, interner_auditor, personalleitung, it_manager), the system SHALL support metadata configuration and placeholder replacement, and SHALL translate German role names to English equivalents in English templates.

**Validates: Requirements 30.1, 30.2, 30.3, 30.4, 30.5, 30.6, 30.7**

### Property 22: HTML Output Structure

*For any* handbook generation with HTML output, the system SHALL create separate HTML files for each template, generate a table of contents index page, provide navigation links between pages, apply consistent styling across all pages, and store output in `Handbook/{language}/{template-type}/html/`.

**Validates: Requirements 31.1, 31.2, 31.3, 31.4, 31.5**

### Property 23: Separate Markdown File Generation

*For any* handbook generation with markdown output, the system SHALL create separate markdown files for each template (no combined file), use filenames matching the pattern `{template-number}_{template-name}.md`, create a TOC file with template numbers, titles, and links, and store output in `Handbook/{language}/{template-type}/markdown/`.

**Validates: Requirements 32.1, 32.2, 32.3, 32.4, 32.5, 32.6**

### Property 24: PDF Table of Contents

*For any* handbook generation with PDF output, the system SHALL insert a table of contents at the beginning of the PDF, start a new page for each template, and include template numbers, titles, and page numbers in the TOC.

**Validates: Requirements 33.1, 33.2, 33.3, 33.4**

## Error Handling

### HTML Comment Processing Errors

**Unclosed Comment**:
```
Error: Unclosed HTML comment detected at line 42
Comment starts with: <!-- TODO: Add BCM strategy
Suggestion: Ensure all comments have closing -->
```

**Nested Comments** (Warning):
```
Warning: Nested HTML comments detected at line 15
HTML comments cannot be nested. Only outermost comment will be removed.
```

### Template Validation Errors

**Missing RACI Matrix Entry**:
```
Warning: RACI matrix incomplete in template 0040_Notfallorganisation_Rollen_und_Gremien.md
Activity "Krisenmanagement" has no Accountable (A) assignment
```

**Missing Framework Reference**:
```
Warning: BCM template 0070_BIA_Methodik.md contains no ISO 22301 references
Consider adding framework references for compliance documentation
```

**Invalid Template Numbering**:
```
Error: Template numbering gap detected in templates/de/bcm/
Expected: 0050_*.md
Found: 0040_*.md, 0060_*.md
```

### Backward Compatibility Errors

**Existing Template Modified**:
```
Error: Existing template structure changed
Template: templates/de/it-operation/0010_Einleitung.md
Expected to remain unchanged for backward compatibility
```

### NetBox Integration Errors

**NetBox Connection Failed**:
```
Error: Failed to connect to NetBox at https://netbox.example.com
Check network connectivity and API token validity
Suggestion: Verify config.yaml contains correct NetBox URL and API token
```

**NetBox Role Mapping Failed**:
```
Warning: Could not map NetBox contact "John Doe" to any configured role
Role distinction method: field-based (field: role)
Contact role value: "Network Engineer"
Suggestion: Add role mapping in config.yaml or adjust role distinction configuration
```

**metadata-netbox.yaml Creation Failed**:
```
Error: Failed to create metadata-netbox.yaml
Permission denied: /path/to/metadata-netbox.yaml
Suggestion: Check file permissions in project directory
```

### Per-Handbook Metadata Errors

**Missing Handbook Metadata**:
```
Warning: No metadata found for handbook type "bcm" in metadata.yaml
Using default values: version="1.0.0", owner="Unknown", approver="Unknown"
Suggestion: Add handbook metadata section to metadata.yaml
```

**Invalid Handbook Placeholder**:
```
Error: Invalid handbook placeholder: {{ handbook.invalid_field }}
Valid fields: version, owner, approver, date
Template: templates/de/bcm/0010_Zweck_und_Geltungsbereich.md, line 15
```

### HTML Output Errors

**HTML Generation Failed**:
```
Error: Failed to generate HTML output
Template: 0050_Kontakte_und_Eskalation.md
Reason: Invalid markdown syntax at line 42
Suggestion: Validate markdown syntax in template
```

**CSS File Missing**:
```
Warning: CSS stylesheet not found
Expected: Handbook/de/bcm/html/styles.css
HTML pages will be generated without styling
```

### Markdown Output Errors

**TOC Generation Failed**:
```
Error: Failed to generate table of contents for markdown output
Reason: No templates found in templates/de/bcm/
Suggestion: Verify template directory exists and contains templates
```

**Filename Pattern Violation**:
```
Warning: Template filename does not match expected pattern
Found: template_without_number.md
Expected: NNNN_template_name.md (e.g., 0010_Einleitung.md)
```

### PDF Output Errors

**PDF TOC Generation Failed**:
```
Error: Failed to generate PDF table of contents
Reason: WeasyPrint encountered invalid HTML
Suggestion: Check template markdown for syntax errors
```

**Page Break Insertion Failed**:
```
Warning: Could not insert page break after template 0050_Kontakte_und_Eskalation.md
PDF may not have proper page separation
```

## Testing Strategy

### Dual Testing Approach

The testing strategy combines unit tests for specific examples and edge cases with property-based tests for universal correctness properties. Both approaches are complementary and necessary for comprehensive coverage.

**Unit Tests**: Focus on specific examples, edge cases, and error conditions. Avoid writing too many unit tests since property-based tests handle comprehensive input coverage.

**Property Tests**: Verify universal properties across all inputs through randomization. Each property test must run a minimum of 100 iterations and reference its design document property.

### Unit Testing Focus Areas

1. **HTML Comment Removal**:
   - Single-line comments
   - Multi-line comments
   - Comments with special characters
   - Empty comments
   - Comments adjacent to markdown syntax

2. **Template Discovery**:
   - Valid template directory structures
   - Missing template directories
   - Mixed language availability

3. **Template Validation**:
   - Complete RACI matrices
   - Incomplete RACI matrices
   - Framework references present/absent
   - Valid/invalid placeholder syntax

4. **CLI Integration**:
   - New template types accepted
   - Invalid template types rejected
   - Backward compatibility with existing types

5. **NetBox Integration**:
   - NetBox connection success/failure
   - Contact fetching with role mapping
   - Device and site information fetching
   - metadata-netbox.yaml creation
   - Role distinction configuration (field-based, name-based)

6. **Per-Handbook Metadata**:
   - Independent version numbers per handbook
   - Independent owners/approvers per handbook
   - Handbook placeholder replacement
   - Missing metadata handling

7. **Extended Roles**:
   - All 6 new roles supported in metadata
   - Role placeholder replacement
   - German to English role name translation

8. **HTML Output**:
   - Separate HTML file per template
   - TOC index page generation
   - Navigation link generation
   - CSS styling application
   - Output directory structure

9. **Separate Markdown Output**:
   - Separate markdown file per template
   - No combined file created
   - Filename pattern compliance
   - TOC file generation
   - Output directory structure

10. **PDF with TOC**:
    - TOC insertion at PDF beginning
    - Page breaks between templates
    - TOC content (numbers, titles, page numbers)
    - Clickable links in TOC

### Property-Based Testing Configuration

**Library**: Use `hypothesis` for Python property-based testing

**Configuration**:
```python
from hypothesis import given, settings, strategies as st

@settings(max_examples=100)  # Minimum 100 iterations
@given(template_content=st.text())
def test_html_comment_removal_completeness(template_content):
    """
    Feature: template-system-extension
    Property 1: HTML Comment Removal Completeness
    
    For any template content containing HTML comments, after processing,
    the output SHALL NOT contain any HTML comment markers.
    """
    # Add HTML comments to content
    content_with_comments = f"<!-- test -->{template_content}<!-- end -->"
    
    # Process content
    processor = HTMLCommentProcessor()
    result = processor.remove_comments(content_with_comments)
    
    # Verify no comment markers remain
    assert "<!--" not in result
    assert "-->" not in result
```

**Test Tags**: Each property test must include a comment tag:
```python
"""
Feature: template-system-extension
Property {number}: {property_title}
"""
```

### Integration Testing

1. **End-to-End Template Processing**:
   - Generate complete BCM handbook (German and English)
   - Generate complete ISMS handbook (German and English)
   - Generate complete BSI Grundschutz handbook (German and English)
   - Verify output structure and content

2. **Backward Compatibility**:
   - Process existing it-operation templates
   - Compare output with baseline
   - Verify no regressions

3. **HTML Comment Integration**:
   - Templates with HTML comments
   - Templates without HTML comments
   - Mixed scenarios

4. **NetBox Integration End-to-End**:
   - Mock NetBox API responses
   - Generate metadata-netbox.yaml
   - Process templates with meta-netbox placeholders
   - Verify correct data replacement
   - Test both field-based and name-based role distinction

5. **Per-Handbook Metadata Integration**:
   - Configure different metadata for each handbook type
   - Generate all handbook types
   - Verify each handbook uses correct metadata
   - Verify handbook placeholders replaced correctly

6. **Multi-Format Output Integration**:
   - Generate HTML output for all handbook types
   - Generate separate markdown files for all handbook types
   - Generate PDF with TOC for all handbook types
   - Verify all output formats coexist correctly
   - Verify output directory structure

7. **Extended Roles Integration**:
   - Configure all 6 new roles in metadata
   - Generate handbooks in German and English
   - Verify role placeholders replaced correctly
   - Verify German-to-English translation in English templates

8. **Complete Workflow Integration**:
   - Start with NetBox data loading
   - Load per-handbook metadata
   - Process templates with all placeholder types
   - Generate all output formats (HTML, markdown, PDF)
   - Verify complete workflow executes without errors

### Test Coverage Goals

- **Unit Test Coverage**: >80% code coverage
- **Property Test Coverage**: All 24 correctness properties implemented (15 existing + 9 new)
- **Integration Test Coverage**: All template types, languages, and output formats
- **Regression Test Coverage**: All existing functionality preserved

