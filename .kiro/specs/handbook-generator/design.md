# Design Document: Handbuch-Generator

## Overview

Der Handbuch-Generator ist eine Python-Konsolenanwendung, die aus strukturierten Markdown-Vorlagen professionelle Handbücher erstellt. Das System ersetzt Platzhalter in den Vorlagen durch echte Daten aus externen Systemen (primär NetBox) und generiert mehrsprachige Handbücher in verschiedenen Ausgabeformaten (Markdown und PDF).

Die Anwendung folgt dem Prinzip der Template-basierten Dokumentengenerierung: Vorlagen definieren die Struktur und den statischen Inhalt, während Platzhalter dynamische Daten aus externen Quellen einbinden. Dies ermöglicht die Erstellung aktueller, datengetriebener Dokumentation ohne manuelle Datenpflege.

**Kernfunktionalität:**
- Template-Discovery und Validierung
- Platzhalter-Parsing mit Jinja2-ähnlicher Syntax
- Integration mit externen Datenquellen (NetBox via pynetbox)
- Multi-Format-Ausgabe (Markdown, PDF)
- Mehrsprachige Unterstützung (Deutsch, Englisch)
- Konfigurierbare Logging-Level

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Interface                            │
│  (Argument Parsing, User Interaction)                       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                Template Manager                              │
│  - Template Discovery                                        │
│  - Template Validation                                       │
│  - Template Sorting & Assembly                               │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Placeholder Processor                           │
│  - Placeholder Detection (Regex)                             │
│  - Placeholder Parsing                                       │
│  - Data Source Routing                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────────────────────────┐
│ Data Source     │    │     Output Generator                 │
│ Adapters        │    │  - Markdown Assembly                 │
│  - NetBox       │    │  - PDF Conversion                    │
│  - (Future)     │    │  - File Writing                      │
└─────────────────┘    └─────────────────────────────────────┘
```

### Component Interaction Flow

1. **CLI Interface** parses command-line arguments and initiates processing
2. **Template Manager** discovers and validates templates based on language/type selection
3. **Placeholder Processor** scans templates for placeholders and routes data requests
4. **Data Source Adapters** fetch data from external systems
5. **Output Generator** assembles processed templates and generates output files

### Design Principles

- **Separation of Concerns**: Klare Trennung zwischen Template-Verwaltung, Datenverarbeitung und Ausgabegenerierung
- **Extensibility**: Plugin-ähnliche Architektur für Data Source Adapters ermöglicht einfache Integration neuer Datenquellen
- **Fail-Safe Processing**: Fehler bei einzelnen Platzhaltern stoppen nicht die gesamte Verarbeitung
- **Configuration over Code**: Externe Konfiguration für Zugangsdaten und Einstellungen

## Components and Interfaces

### 1. CLI Interface (`cli.py`)

**Verantwortlichkeit:** Kommandozeilen-Parsing, Benutzerinteraktion, Programmsteuerung

**Schnittstelle:**
```python
def main() -> int:
    """Entry point for the handbook generator."""
    
def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    
def interactive_selection(template_manager: TemplateManager) -> tuple[str, str]:
    """Interactive language and template type selection."""
```

**Kommandozeilenparameter:**
- `--language, -l`: Sprache auswählen (de, en)
- `--template, -t`: Vorlagentyp auswählen (backup, bcm, isms, it-operation)
- `--output, -o`: Ausgabeformat (markdown, pdf, both) [default: both]
- `--verbose, -v`: Verbose logging aktivieren
- `--config, -c`: Pfad zur Konfigurationsdatei [default: config.yaml]

### 2. Template Manager (`template_manager.py`)

**Verantwortlichkeit:** Template-Discovery, Validierung, Sortierung

**Schnittstelle:**
```python
class TemplateManager:
    def __init__(self, template_root: Path):
        """Initialize with template root directory."""
        
    def discover_templates(self) -> dict[str, dict[str, list[Path]]]:
        """Discover all available templates organized by language and type."""
        
    def get_templates(self, language: str, template_type: str) -> list[Template]:
        """Get sorted templates for specific language and type."""
        
    def validate_template_structure(self) -> list[str]:
        """Validate template directory structure and return warnings."""
```

**Template-Klasse:**
```python
@dataclass
class Template:
    path: Path
    template_type: str  # 'content' or 'metadata'
    sort_order: int  # Extracted from filename (e.g., 0100)
    language: str
    category: str  # backup, bcm, isms, it-operation
    
    def is_metadata(self) -> bool:
        """Check if this is a metadata template."""
        
    def read_content(self) -> str:
        """Read template file content."""
```

**Template-Sortierung:**
- Metadaten-Vorlagen (0000_metadata_*) zuerst
- Content-Vorlagen nach führender 4-stelliger Nummer sortiert
- Vorlagen ohne Nummer am Ende (mit Warnung)

### 3. Placeholder Processor (`placeholder_processor.py`)

**Verantwortlichkeit:** Platzhalter-Erkennung, Parsing, Ersetzung

**Schnittstelle:**
```python
class PlaceholderProcessor:
    def __init__(self, data_sources: dict[str, DataSourceAdapter]):
        """Initialize with available data source adapters."""
        
    def process_template(self, template_content: str) -> ProcessingResult:
        """Process template and replace all placeholders."""
        
    def find_placeholders(self, content: str) -> list[Placeholder]:
        """Find all placeholders in content."""
        
    def replace_placeholder(self, placeholder: Placeholder) -> str:
        """Replace single placeholder with data from source."""
```

**Placeholder-Klasse:**
```python
@dataclass
class Placeholder:
    raw: str  # Original "{{ netbox.device_name }}"
    source: str  # "netbox"
    field: str  # "device_name"
    line_number: int
    
    @classmethod
    def parse(cls, match: re.Match, line_number: int) -> 'Placeholder':
        """Parse placeholder from regex match."""
```

**Platzhalter-Regex:**
```python
PLACEHOLDER_PATTERN = r'^\s*\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}\s*$'
```

**ProcessingResult:**
```python
@dataclass
class ProcessingResult:
    content: str
    replacements: list[Replacement]
    warnings: list[str]
    errors: list[str]
    
@dataclass
class Replacement:
    placeholder: str
    value: str
    source: str
    line_number: int
```

### 4. Data Source Adapters (`data_sources/`)

**Verantwortlichkeit:** Abstraktion für externe Datenquellen

**Base Interface:**
```python
class DataSourceAdapter(ABC):
    @abstractmethod
    def connect(self) -> bool:
        """Establish connection to data source."""
        
    @abstractmethod
    def get_field(self, field_path: str) -> Optional[str]:
        """Retrieve field value from data source."""
        
    @abstractmethod
    def disconnect(self) -> None:
        """Close connection to data source."""
```

**NetBox Adapter (`data_sources/netbox_adapter.py`):**
```python
class NetBoxAdapter(DataSourceAdapter):
    def __init__(self, url: str, api_token: str):
        """Initialize NetBox adapter with connection details."""
        self.api = None
        
    def connect(self) -> bool:
        """Connect to NetBox using pynetbox."""
        # Uses: pynetbox.api(url, token=api_token)
        
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Retrieve field from NetBox.
        
        Examples:
        - "device_name" -> nb.dcim.devices.get(name=...)
        - "site.name" -> nb.dcim.sites.get(...)
        """
```

**Verwendete Bibliothek:** [pynetbox](https://pynetbox.readthedocs.io/)
- Offizielle Python-Client-Bibliothek für NetBox
- Pythonic API für NetBox REST API
- Unterstützt alle NetBox-Apps (dcim, ipam, circuits, etc.)

### 5. Configuration Manager (`config_manager.py`)

**Verantwortlichkeit:** Konfigurationsdatei-Verwaltung

**Schnittstelle:**
```python
class ConfigManager:
    def __init__(self, config_path: Path):
        """Initialize with config file path."""
        
    def load_config(self) -> Config:
        """Load configuration from file."""
        
    def create_default_config(self) -> None:
        """Create default configuration file with examples."""
        
    def ensure_gitignore(self) -> None:
        """Ensure config file is in .gitignore."""
```

**Config-Klasse:**
```python
@dataclass
class Config:
    netbox_url: str
    netbox_api_token: str
    default_language: str = "de"
    default_output_format: str = "both"
    author: str = "Andreas Huemmer [andreas.huemmer@adminsend.de]"
    version: str = "1.0.0"
```

**Konfigurationsdatei-Format (YAML):**
```yaml
# Handbook Generator Configuration
# WARNING: This file contains sensitive credentials - do not commit to git!

data_sources:
  netbox:
    url: "https://netbox.adminsend.local"
    api_token: "c84a2203a437eb034c3ed1b05d18743d0e9e51f6"

defaults:
  language: "de"
  output_format: "both"  # markdown, pdf, both
  
metadata:
  author: "Andreas Huemmer [andreas.huemmer@adminsend.de]"
  version: "1.0.0"
```

### 6. Output Generator (`output_generator.py`)

**Verantwortlichkeit:** Ausgabedatei-Generierung in verschiedenen Formaten

**Schnittstelle:**
```python
class OutputGenerator:
    def __init__(self, output_dir: Path):
        """Initialize with output directory."""
        
    def generate_markdown(
        self, 
        templates: list[ProcessingResult], 
        language: str, 
        template_type: str
    ) -> Path:
        """Generate markdown output file."""
        
    def generate_pdf(
        self, 
        markdown_content: str, 
        language: str, 
        template_type: str
    ) -> Path:
        """Generate PDF from markdown content."""
        
    def ensure_output_structure(self, language: str, template_type: str) -> Path:
        """Ensure output directory structure exists."""
```

**PDF-Generierung:**
- **Bibliothek:** [markdown-pdf](https://pypi.org/project/markdown-pdf/) oder [weasyprint](https://weasyprint.org/)
- **Prozess:** Markdown → HTML → PDF
- **Styling:** CSS für professionelles Layout

**Ausgabestruktur:**
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
    ├── backup/
    ├── bcm/
    ├── isms/
    └── it-operation/
```

### 7. Logger (`logger.py`)

**Verantwortlichkeit:** Strukturiertes Logging mit konfigurierbaren Levels

**Schnittstelle:**
```python
class HandbookLogger:
    def __init__(self, verbose: bool = False):
        """Initialize logger with verbosity level."""
        
    def log_processing(self, template_name: str) -> None:
        """Log template processing (normal level)."""
        
    def log_replacement(self, replacement: Replacement) -> None:
        """Log placeholder replacement (verbose level)."""
        
    def log_statistics(self, stats: Statistics) -> None:
        """Log processing statistics (normal level)."""
        
    def log_warning(self, message: str, verbose_details: str = None) -> None:
        """Log warning with optional verbose details."""
        
    def log_error(self, message: str, verbose_details: str = None) -> None:
        """Log error with optional verbose details."""
```

**Statistics-Klasse:**
```python
@dataclass
class Statistics:
    documents_processed: int
    placeholders_replaced: int
    placeholders_failed: int
    total_words: int
    output_size_bytes: int
    processing_time_seconds: float
```

## Data Models

### Template Directory Structure

```
templates/
├── de/                          # German templates
│   ├── backup/
│   │   ├── 0000_metadata_de_backup.md
│   │   ├── 0100_einleitung.md
│   │   ├── 0200_backup_strategie.md
│   │   └── 0300_wiederherstellung.md
│   ├── bcm/
│   ├── isms/
│   └── it-operation/
├── en/                          # English templates
│   ├── backup/
│   │   ├── 0000_metadata_en_backup.md
│   │   ├── 0100_introduction.md
│   │   ├── 0200_backup_strategy.md
│   │   └── 0300_recovery.md
│   ├── bcm/
│   ├── isms/
│   └── it-operation/
└── examples/                    # Example templates
    ├── backup/
    ├── bcm/
    ├── isms/
    ├── it-operation/
    ├── ISO 27001/
    ├── ISO 9001/
    └── BSI Grundschutz/
```

### Template File Naming Conventions

**Content Templates:**
- Format: `NNNN_name.md` (z.B. `0100_einleitung.md`)
- NNNN: 4-stellige Sortierungsnummer (0100, 0200, 0300, ...)
- Bestimmt die Reihenfolge im generierten Handbuch

**Metadata Templates:**
- Format: `0000_metadata_[language]_[templatename].md`
- Beispiel: `0000_metadata_de_backup.md`
- Wird immer als erste Seite gerendert

### Placeholder Syntax

**Format:** `{{ source.field }}`

**Regeln:**
- Muss die einzige Anweisung in der Zeile sein
- Whitespace vor/nach erlaubt
- Source: Datenquelle (z.B. "netbox")
- Field: Feldpfad mit Punkt-Notation (z.B. "device.name" oder "site.location.name")

**Beispiele:**
```markdown
# Geräteinformationen

Gerätename: {{ netbox.device_name }}
Standort: {{ netbox.site_name }}
IP-Adresse: {{ netbox.primary_ip }}
```

### Configuration File Schema

```yaml
data_sources:
  netbox:
    url: string (required)
    api_token: string (required)
  # Future data sources can be added here
  
defaults:
  language: string (optional, default: "de")
  output_format: string (optional, default: "both")
  
metadata:
  author: string (optional, default: "Andreas Huemmer [andreas.huemmer@adminsend.de]")
  version: string (optional, default: "1.0.0")
```

## Correctness Properties

*Eine Property ist eine Eigenschaft oder ein Verhalten, das über alle gültigen Ausführungen eines Systems hinweg wahr sein sollte - im Wesentlichen eine formale Aussage darüber, was das System tun soll. Properties dienen als Brücke zwischen menschenlesbaren Spezifikationen und maschinenverifizierbaren Korrektheitsgarantien.*


### Property 1: Template Discovery Completeness
*For any* valid template directory structure with templates in multiple languages and types, the template scanner should discover all templates and correctly categorize them by language and type.
**Validates: Requirements 1.1, 1.2, 1.3, 1.5**

### Property 2: CLI Parameter Validation
*For any* combination of language and template type parameters, if the combination exists in the template directory, the system should use it; if it doesn't exist, the system should reject it with an error message listing available options.
**Validates: Requirements 2.1, 2.2, 2.3, 2.5**

### Property 3: Placeholder Detection and Parsing
*For any* template content containing placeholders in the format "{{ source.field }}", the system should correctly identify all placeholders and extract both the source and field components.
**Validates: Requirements 3.1, 3.4**

### Property 4: Placeholder Line Validation
*For any* placeholder in a template, if the placeholder is not the only statement on its line, the system should generate a warning with the filename and line number.
**Validates: Requirements 3.2, 3.3**

### Property 5: Template Pass-Through
*For any* template content without placeholders, the system should output the content unchanged.
**Validates: Requirements 3.5**

### Property 6: Data Extraction from API Responses
*For any* mocked API response and field path, the system should correctly extract the requested field value from the response structure.
**Validates: Requirements 4.3**

### Property 7: Missing Field Handling
*For any* placeholder referencing a non-existent field, the system should generate a warning and leave the placeholder unchanged in the output.
**Validates: Requirements 4.4**

### Property 8: Placeholder Replacement
*For any* placeholder with successfully retrieved data, the system should replace the placeholder with the actual value in the output.
**Validates: Requirements 4.5**

### Property 9: Configuration Parsing
*For any* valid configuration file containing data source credentials, the system should correctly extract all connection parameters (URL, API tokens, etc.).
**Validates: Requirements 5.3**

### Property 10: Invalid Configuration Handling
*For any* configuration file with missing or invalid credentials, the system should generate a descriptive error message indicating which fields are problematic.
**Validates: Requirements 5.5**

### Property 11: Template Sorting and Assembly
*For any* set of content templates with 4-digit sort numbers and metadata templates, the system should process them in the correct order: metadata first (0000), then content templates in ascending numerical order.
**Validates: Requirements 6.1, 6.2, 6.4, 6.5**

### Property 12: Unnumbered Template Handling
*For any* template without a leading 4-digit number, the system should generate a warning and place the template at the end of the processing order.
**Validates: Requirements 6.3**

### Property 13: Metadata Template Format Validation
*For any* filename, if it matches the pattern "0000_metadata_[language]_[templatename].md", it should be recognized as a metadata template; otherwise, it should not.
**Validates: Requirements 7.1**

### Property 14: Version Number Fallback
*For any* metadata template processing, if a version number is specified in the configuration, use it; otherwise, use "1.0.0" as the default.
**Validates: Requirements 7.4**

### Property 15: Markdown Assembly
*For any* set of processed templates, the markdown output should contain all template contents in the correct order as a single concatenated document.
**Validates: Requirements 8.1**

### Property 16: Output Directory Structure Mirroring
*For any* template with language and type (e.g., "de/backup"), the output directory structure should mirror this organization (e.g., "Handbook/de/backup/").
**Validates: Requirements 8.3**

### Property 17: Markdown Validity
*For any* generated markdown output, the content should be parseable as valid markdown syntax.
**Validates: Requirements 8.5**

### Property 18: PDF Generation Error Handling
*For any* PDF generation failure, the system should produce an error message containing details about the failure cause.
**Validates: Requirements 9.5**

### Property 19: Statistics Calculation
*For any* processing run, the system should calculate and report accurate statistics including document count, placeholder replacement count, word count, and output size.
**Validates: Requirements 10.2**

### Property 20: Verbose Logging Detail
*For any* placeholder replacement in verbose mode, the system should log which placeholder was replaced with which value.
**Validates: Requirements 10.4, 10.5**

### Property 21: Data Source Adapter Routing
*For any* placeholder with a specified source (e.g., "netbox"), the system should route the data request to the corresponding adapter; for unknown sources, it should generate a warning listing available sources.
**Validates: Requirements 11.2, 11.3**

### Property 22: Multi-Source Configuration Support
*For any* configuration file containing credentials for multiple data sources, the system should correctly parse and store all data source configurations.
**Validates: Requirements 11.5**

### Property 23: Error Summary Completeness
*For any* processing run with errors and warnings, the final summary should include all errors and warnings that occurred during processing.
**Validates: Requirements 12.5**

### Property 24: Example Template Separation
*For any* template directory structure containing an "examples" subdirectory, templates in the examples directory should be categorized separately from regular templates.
**Validates: Requirements 13.2**

### Property 25: Example Template Processing Consistency
*For any* example template, when processed, it should follow the same placeholder replacement and validation rules as regular templates.
**Validates: Requirements 13.5**

## Error Handling

### Error Categories

**1. Configuration Errors**
- Missing configuration file → Create default config, inform user
- Invalid credentials → Clear error message with field names
- Malformed YAML → Parse error with line number

**2. Template Errors**
- Template directory not found → Error with expected path
- Invalid template filename → Warning, place at end of order
- Malformed placeholder → Warning with file and line number
- Placeholder not on its own line → Warning with location

**3. Data Source Errors**
- Connection failure → Error with URL and status code
- Authentication failure → Error indicating invalid credentials
- Field not found → Warning, leave placeholder unchanged
- Timeout → Error with retry suggestion

**4. Output Errors**
- Output directory creation failure → Error with permissions info
- File write failure → Error with path and reason
- PDF generation failure → Error with detailed cause
- Disk space issues → Error with space requirements

### Error Handling Strategy

**Fail-Safe Processing:**
- Single placeholder failure does not stop entire processing
- Collect all errors and warnings during processing
- Display comprehensive summary at end
- Exit code indicates success (0) or failure (non-zero)

**Logging Levels:**
- **Normal:** Document processing progress, statistics, errors, warnings
- **Verbose:** All normal output + placeholder replacements, API calls, detailed errors

**User-Friendly Messages:**
- Clear description of what went wrong
- Context (file, line number, placeholder)
- Suggestion for resolution where applicable
- No technical stack traces in normal mode (only in verbose)

## Testing Strategy

### Dual Testing Approach

Die Teststrategie kombiniert Unit-Tests für spezifische Beispiele und Edge Cases mit Property-Based Tests für universelle Eigenschaften:

**Unit Tests:**
- Spezifische Beispiele für Template-Parsing
- Edge Cases (leere Dateien, ungültige Formate)
- Fehlerbehandlung für bekannte Szenarien
- Integration zwischen Komponenten
- Mocking von externen APIs (NetBox)

**Property-Based Tests:**
- Universelle Eigenschaften über alle Eingaben
- Minimum 100 Iterationen pro Property-Test
- Randomisierte Template-Strukturen
- Randomisierte Platzhalter-Kombinationen
- Randomisierte Konfigurationen

### Property-Based Testing Configuration

**Bibliothek:** [Hypothesis](https://hypothesis.readthedocs.io/) für Python
- De-facto Standard für Property-Based Testing in Python
- Integriert mit pytest
- Unterstützt komplexe Datenstrukturen und Strategien

**Test-Konfiguration:**
```python
from hypothesis import given, settings
import hypothesis.strategies as st

@settings(max_examples=100)
@given(templates=st.lists(st.text()))
def test_property_X(templates):
    """
    Feature: handbook-generator, Property X: [Property description]
    """
    # Test implementation
```

**Tag-Format für Property-Tests:**
```python
"""
Feature: handbook-generator, Property 1: Template Discovery Completeness
"""
```

### Test Coverage Areas

**1. Template Manager Tests**
- Template discovery with various directory structures
- Template sorting with different numbering schemes
- Metadata template identification
- Language and type categorization

**2. Placeholder Processor Tests**
- Placeholder detection with various formats
- Placeholder parsing and validation
- Line-only validation
- Source and field extraction

**3. Data Source Adapter Tests**
- NetBox adapter with mocked API responses
- Field extraction from nested structures
- Error handling for missing fields
- Connection failure scenarios

**4. Configuration Manager Tests**
- YAML parsing with various structures
- Default config generation
- Gitignore management
- Multi-source configuration

**5. Output Generator Tests**
- Markdown assembly from multiple templates
- Directory structure creation
- PDF generation (with mocked converter)
- File overwrite handling

**6. Integration Tests**
- End-to-end processing with sample templates
- Multi-language handbook generation
- Error propagation through pipeline
- Statistics calculation accuracy

### Test Data

**Sample Templates:**
- Minimal templates (single placeholder)
- Complex templates (multiple placeholders, nested fields)
- Templates without placeholders
- Malformed templates (for error testing)

**Mock Data Sources:**
- NetBox API responses with realistic data structures
- Error responses (404, 401, 500)
- Timeout scenarios
- Partial data (missing fields)

**Configuration Files:**
- Valid configurations with all fields
- Minimal configurations (defaults)
- Invalid configurations (missing fields, wrong types)
- Multi-source configurations

## Dependencies

### Core Dependencies

```
# requirements.txt

# Template Processing
jinja2>=3.1.0              # Template engine (if needed for advanced features)

# Data Source Integration
pynetbox>=7.0.0            # NetBox API client
requests>=2.31.0           # HTTP library (dependency of pynetbox)

# Configuration Management
pyyaml>=6.0                # YAML parsing

# Output Generation
markdown>=3.5.0            # Markdown processing
markdown-pdf>=1.0.0        # Markdown to PDF conversion
# OR
weasyprint>=60.0           # Alternative: HTML/CSS to PDF

# CLI
argparse                   # Built-in, no installation needed
pathlib                    # Built-in, no installation needed

# Testing
pytest>=7.4.0              # Test framework
pytest-cov>=4.1.0          # Coverage reporting
hypothesis>=6.90.0         # Property-based testing
responses>=0.24.0          # HTTP mocking for tests

# Development
flake8>=6.1.0              # Linting
black>=23.0.0              # Code formatting
mypy>=1.7.0                # Type checking
```

### Python Version

- **Minimum:** Python 3.8
- **Recommended:** Python 3.11+
- **Reason:** Modern type hints, performance improvements, better error messages

### External Services

**NetBox:**
- Version: Compatible with NetBox 3.x+
- API: REST API v2.0+
- Authentication: Token-based
- Network: HTTPS required for production

## Implementation Notes

### Phase 1: Core Functionality
1. Template Manager (discovery, sorting)
2. Placeholder Processor (detection, parsing)
3. Configuration Manager
4. Basic CLI interface
5. Markdown output

### Phase 2: Data Integration
1. Data Source Adapter interface
2. NetBox adapter implementation
3. Placeholder replacement with real data
4. Error handling and logging

### Phase 3: Advanced Features
1. PDF generation
2. Verbose logging
3. Statistics calculation
4. Example template support

### Phase 4: Polish
1. Comprehensive error messages
2. Interactive mode
3. Configuration validation
4. Documentation

### Security Considerations

**Credential Management:**
- Configuration file must be in .gitignore
- No credentials in code or logs
- Warn user if config file has wrong permissions (world-readable)

**Input Validation:**
- Validate all user inputs (CLI parameters)
- Sanitize file paths (prevent directory traversal)
- Validate template content (prevent code injection)

**API Security:**
- Use HTTPS for all API connections
- Validate SSL certificates
- Timeout for API requests (prevent hanging)
- Rate limiting awareness

### Performance Considerations

**Template Processing:**
- Stream large templates (don't load entire file into memory)
- Cache compiled regex patterns
- Parallel processing for multiple templates (optional)

**API Calls:**
- Batch requests where possible
- Cache API responses during single run
- Connection pooling for multiple requests

**Output Generation:**
- Stream output to file (don't build entire document in memory)
- Incremental PDF generation if possible
