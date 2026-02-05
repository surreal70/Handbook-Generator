# Design Document: CIS Controls v8 Hardening Templates Integration

## Overview

This design document specifies the technical approach for integrating CIS Controls v8 Hardening Templates as a fifth handbook type in the existing handbook generator system. The integration leverages the existing template discovery, processing, and output generation infrastructure while adding CIS Controls-specific templates and bilingual support.

The handbook generator currently supports four handbook types (BCM, ISMS, BSI Grundschutz, IT-Operation) with 186 templates across German and English. The CIS Controls integration adds 27 templates covering system hardening baselines, operating system configurations, application security standards, and compliance documentation.

### Key Design Principles

1. **Zero Code Changes**: The existing TemplateManager automatically discovers templates based on directory structure, requiring no code modifications
2. **Backward Compatibility**: All existing handbook types continue to function identically
3. **Bilingual Parity**: German and English templates maintain identical structure and numbering
4. **Consistent Integration**: CIS Controls follows the same patterns as existing handbook types
5. **Comprehensive Testing**: Property-based and unit tests ensure correctness and prevent regressions

## Architecture

### System Components

The handbook generator consists of these key components:

```
┌─────────────────────────────────────────────────────────────┐
│                         CLI Layer                            │
│  (Argument parsing, user interaction, workflow control)      │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Template Manager                           │
│  (Discovery, validation, sorting, metadata extraction)       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│               Placeholder Processor                          │
│  (Data source integration, placeholder replacement)          │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                Output Generator                              │
│  (Markdown assembly, PDF generation, HTML site creation)     │
└─────────────────────────────────────────────────────────────┘
```

### Integration Points

The CIS Controls integration touches these components:

1. **Template Manager**: Discovers CIS Controls templates in `templates/{lang}/cis-controls/`
2. **CLI**: Accepts `cis-controls` as a valid `--template` argument
3. **Output Generator**: Generates CIS Controls handbooks in all supported formats
4. **Documentation**: Updates README.md with CIS Controls information


## Components and Interfaces

### Template Directory Structure

The CIS Controls templates follow the established directory structure pattern:

```
templates/
├── de/
│   └── cis-controls/
│       ├── 0000_metadata_de_cis-controls.md
│       ├── 0010_CIS_Controls_Ueberblick_und_Vorgehen.md
│       ├── 0020_Geltungsbereich_Assetgruppen_und_Tiering.md
│       ├── ... (25 more templates)
│       └── 0410_Anhang_Checklisten_und_Evidence.md
└── en/
    └── cis-controls/
        ├── 0000_metadata_en_cis-controls.md
        ├── 0010_CIS_Controls_Overview_and_Approach.md
        ├── 0020_Scope_Asset_Groups_and_Tiering.md
        ├── ... (25 more templates)
        └── 0410_Appendix_Checklists_and_Evidence.md
```

### Template Manager Interface

The TemplateManager class provides these methods (no changes required):

```python
class TemplateManager:
    def discover_templates(self, include_examples: bool = False) -> dict[str, dict[str, list[Path]]]:
        """
        Discover all available templates organized by language and type.
        Returns: {language: {category: [template_paths]}}
        """
    
    def get_templates(self, language: str, template_type: str) -> list[Template]:
        """
        Get sorted templates for specific language and type.
        Returns: List of Template objects sorted by sort_order
        """
    
    def get_available_options(self) -> tuple[list[str], dict[str, list[str]]]:
        """
        Get available languages and template types.
        Returns: (available_languages, available_types_per_language)
        """
    
    def validate_template_exists(self, language: str, template_type: str) -> Optional[str]:
        """
        Validate that a template exists for the given language and type.
        Returns: Error message if template doesn't exist, None otherwise
        """
```

### CLI Interface

The CLI accepts `cis-controls` as a valid template type (requires one-line change):

```python
parser.add_argument(
    '--template', '-t',
    type=str,
    choices=['backup', 'bcm', 'bsi-grundschutz', 'isms', 'it-operation', 'cis-controls'],
    help='Template type/category for handbook'
)
```

### Output Generator Interface

The OutputGenerator class generates output in all formats (no changes required):

```python
class OutputGenerator:
    def generate_markdown(self, processed_contents: list[str], language: str, 
                         template_type: str, filename: Optional[str] = None) -> OutputResult:
        """Generate markdown output file from processed templates."""
    
    def generate_separate_markdown_files(self, templates_data: list[tuple[str, str]], 
                                        language: str, template_type: str) -> OutputResult:
        """Generate separate markdown files for each template."""
    
    def generate_pdf(self, markdown_content: str, language: str, 
                    template_type: str, filename: Optional[str] = None) -> OutputResult:
        """Generate PDF output file from markdown content."""
    
    def generate_pdf_with_toc(self, templates_data: list[tuple[str, str, str]], 
                             language: str, template_type: str, 
                             filename: Optional[str] = None) -> OutputResult:
        """Generate PDF with table of contents from template data."""
```


## Data Models

### Template Data Model

The existing Template dataclass represents individual template files:

```python
@dataclass
class Template:
    path: Path                  # Path to template file
    template_type: str          # 'content' or 'metadata'
    sort_order: int            # Numeric sort order (0 for metadata, 10-9999 for content)
    language: str              # Language code ('de', 'en')
    category: str              # Handbook category ('cis-controls', 'bcm', etc.)
    
    def is_metadata(self) -> bool:
        """Check if this is a metadata template."""
    
    def read_content(self) -> str:
        """Read template file content."""
```

### CIS Controls Template Categories

The 27 CIS Controls templates are organized into four categories:

1. **Foundation (0010-0050)**: 5 templates
   - Overview and approach
   - Scope and asset groups
   - Hardening lifecycle
   - Exceptions and risk acceptance
   - Testing and validation

2. **Operating Systems (0100-0150)**: 6 templates
   - OS README
   - Windows Server baseline
   - Windows Client baseline
   - Linux baseline
   - macOS baseline
   - Container base images

3. **Applications (0200-0330)**: 14 templates
   - Applications README
   - Web servers (Nginx, Apache, IIS, Tomcat)
   - Databases (PostgreSQL, MySQL, MS SQL Server)
   - Container platforms (Kubernetes, Docker)
   - Services (SSH, Identity/AD)

4. **Appendices (0400-0410)**: 2 templates
   - Control mapping template
   - Checklists and evidence

### Metadata Template Structure

The metadata templates follow the established pattern:

```markdown
# CIS Controls v8 Hardening Templates

**Handbook Type:** CIS Controls v8 Hardening
**Language:** {{ meta.language }}
**Organization:** {{ meta.organization }}
**Version:** {{ meta.version }}
**Author:** {{ meta.author }}
**Date:** {{ meta.date }}

## Purpose

This handbook documents system hardening baselines and standards based on 
CIS Controls v8 framework...
```

### Output Structure

Generated CIS Controls handbooks follow the consolidated output structure:

```
test-output/
├── de/
│   └── cis-controls/
│       ├── markdown/
│       │   ├── TOC.md
│       │   ├── 0010_CIS_Controls_Ueberblick_und_Vorgehen.md
│       │   └── ... (26 more files)
│       ├── pdf/
│       │   └── cis-controls_handbook.pdf
│       └── html/
│           ├── index.html
│           ├── 0010_CIS_Controls_Ueberblick_und_Vorgehen.html
│           └── ... (26 more files + styles.css)
└── en/
    └── cis-controls/
        ├── markdown/
        ├── pdf/
        └── html/
```


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Template Discovery Completeness

*For any* language directory containing a template type subdirectory with .md files, the Template_Manager SHALL discover and return all templates in that subdirectory when discover_templates() is called.

**Validates: Requirements 1.1, 1.2, 4.1**

### Property 2: Template Sorting Consistency

*For any* language and template type combination, when get_templates() is called, the returned templates SHALL be sorted by sort_order with metadata templates (sort_order=0) appearing first, followed by content templates in ascending numeric order.

**Validates: Requirements 4.2, 4.3**

### Property 3: Filename Convention Validation

*For any* template file in a template directory, if the filename does not match the pattern `NNNN_name.md` (where NNNN is 4 digits) or `0000_metadata_[lang]_[type].md`, the validate_template_structure() method SHALL generate a warning message containing the filename and the reason for invalidity.

**Validates: Requirements 1.3, 11.1, 11.2, 11.3, 11.4, 11.5**

### Property 4: Content Preservation During Migration

*For any* template file migrated from source to destination directory, the file content SHALL be byte-for-byte identical after migration, preserving all text, formatting, and placeholders.

**Validates: Requirements 1.4**

### Property 5: Directory Structure Preservation

*For any* set of template files with a hierarchical directory structure, when migrated to a new location, the relative directory structure and file organization SHALL be preserved identically.

**Validates: Requirements 1.5**

### Property 6: Metadata Template First Position

*For any* handbook generation request, when templates are retrieved and sorted, the metadata template (if present) SHALL always appear at index 0 in the sorted template list, before all content templates.

**Validates: Requirements 2.3**

### Property 7: Metadata Required Fields Presence

*For any* generated handbook with a metadata template, the rendered output SHALL contain all required metadata fields: handbook title, version, author, and creation date.

**Validates: Requirements 2.4**

### Property 8: Placeholder Processing in Metadata

*For any* metadata template containing placeholders in the format `{{ source.field }}`, the Placeholder_Processor SHALL replace all valid placeholders with their corresponding values from configured data sources.

**Validates: Requirements 2.5**

### Property 9: Available Options Completeness

*For any* template type discovered by discover_templates(), that template type SHALL appear in the list returned by get_available_options() for all languages where it exists.

**Validates: Requirements 3.3, 4.4**

### Property 10: CLI Flag Compatibility

*For any* handbook type, all CLI flags (--language, --output, --test, --separate-files, --pdf-toc, --verbose) SHALL function identically regardless of which handbook type is selected.

**Validates: Requirements 3.4**

### Property 11: Error Message Informativeness

*For any* invalid template type provided to the CLI, the error message SHALL include a list of all available template types discovered in the template directory.

**Validates: Requirements 3.5**

### Property 12: Template Existence Validation

*For any* valid combination of language and template type where templates exist in the filesystem, validate_template_exists() SHALL return None (indicating no error).

**Validates: Requirements 4.5**

### Property 13: Multi-Format Output Generation

*For any* handbook type, the system SHALL successfully generate output in all requested formats (HTML, PDF, Markdown, separate files, PDF with TOC) without errors when valid templates and test mode are provided.

**Validates: Requirements 5.1, 5.2, 5.3, 5.4, 5.5**

### Property 14: Placeholder Replacement Correctness

*For any* template containing valid placeholders `{{ source.field }}`, the Placeholder_Processor SHALL replace each placeholder with the corresponding value from the data source, and the placeholder syntax SHALL not appear in the final output.

**Validates: Requirements 6.1, 6.4**

### Property 15: Placeholder Error Handling

*For any* template containing invalid placeholders (non-existent source or field), the system SHALL generate an error message containing the template name, placeholder text, and specific reason for failure, without crashing.

**Validates: Requirements 6.2, 6.3, 6.5**

### Property 16: Bilingual Structure Consistency

*For any* template type available in multiple languages, the template count, numbering sequence, and directory structure SHALL be identical across all languages.

**Validates: Requirements 7.3**

### Property 17: Placeholder Preservation Across Languages

*For any* template available in multiple languages, all placeholder references `{{ source.field }}` SHALL be identical across language versions, ensuring consistent data integration.

**Validates: Requirements 7.4**

### Property 18: Language Selection Functionality

*For any* template type available in multiple languages, the --language flag SHALL control which language's templates are used, and the generated output SHALL contain content exclusively from the selected language.

**Validates: Requirements 7.5**

### Property 19: Backward Compatibility Preservation

*For any* existing handbook type (BCM, ISMS, BSI Grundschutz, IT-Operation), the generated output SHALL be identical before and after adding new template types to the system.

**Validates: Requirements 10.1, 10.2, 10.3, 10.4**

### Property 20: Output Structure Consistency

*For any* handbook type, the generated output directory structure SHALL follow the pattern `test-output/{language}/{handbook-type}/{output-type}/` with consistent organization across all handbook types.

**Validates: Requirements 12.4**

### Property 21: Batch Generation Error Resilience

*For any* batch generation process, if generation fails for one handbook type, the system SHALL log the error and continue processing remaining handbook types without terminating the entire batch.

**Validates: Requirements 12.5**


## Error Handling

### Template Discovery Errors

**Error Condition**: CIS Controls template directory does not exist
- **Detection**: TemplateManager.discover_templates() finds no `cis-controls` subdirectory
- **Handling**: Return empty dictionary for that template type; CLI shows available options
- **User Message**: "Template type 'cis-controls' not found. Available types: [list]"

**Error Condition**: CIS Controls templates have invalid filenames
- **Detection**: Filename doesn't match `NNNN_name.md` or metadata pattern
- **Handling**: Generate warning via validate_template_structure(); assign sort_order=9999
- **User Message**: "Warning: Invalid filename format: {filename}. Expected NNNN_name.md"

**Error Condition**: Metadata template missing
- **Detection**: No `0000_metadata_[lang]_cis-controls.md` file found
- **Handling**: Continue without metadata; log warning
- **User Message**: "Warning: No metadata template found for cis-controls"

### Template Processing Errors

**Error Condition**: Template file cannot be read
- **Detection**: FileNotFoundError or PermissionError during read_content()
- **Handling**: Log error with filename; skip template; continue with others
- **User Message**: "Error: Cannot read template {filename}: {reason}"

**Error Condition**: Template contains invalid UTF-8
- **Detection**: UnicodeDecodeError during read_content()
- **Handling**: Log error; skip template
- **User Message**: "Error: Invalid encoding in {filename}. Templates must be UTF-8."

**Error Condition**: Placeholder references non-existent data source
- **Detection**: PlaceholderProcessor cannot find data source adapter
- **Handling**: Log error with placeholder details; leave placeholder unreplaced
- **User Message**: "Error in {template}: Unknown data source '{source}' in placeholder {{{{ source.field }}}}"

**Error Condition**: Placeholder references non-existent field
- **Detection**: Data source adapter returns None for field
- **Handling**: Log error; leave placeholder unreplaced
- **User Message**: "Error in {template}: Field '{field}' not found in source '{source}'"

### Output Generation Errors

**Error Condition**: Test mode not enabled
- **Detection**: OutputGenerator.ensure_output_structure() called with test_mode=False
- **Handling**: Raise RuntimeError; prevent file creation
- **User Message**: "Output generation requires --test flag. Use --test to enable test mode output."

**Error Condition**: Output directory cannot be created
- **Detection**: PermissionError during mkdir()
- **Handling**: Log error; return OutputResult with error
- **User Message**: "Error: Cannot create output directory {path}: Permission denied"

**Error Condition**: PDF generation dependencies missing
- **Detection**: ImportError when importing markdown or weasyprint
- **Handling**: Log error; return OutputResult with error; skip PDF generation
- **User Message**: "PDF generation dependencies not available. Install with: pip install markdown weasyprint"

**Error Condition**: Markdown to PDF conversion fails
- **Detection**: Exception during HTML.write_pdf()
- **Handling**: Log error with details; return OutputResult with error
- **User Message**: "Failed to generate PDF: {error}. Ensure weasyprint dependencies are installed correctly."

### CLI Errors

**Error Condition**: Invalid template type specified
- **Detection**: argparse validation or TemplateManager.validate_template_exists()
- **Handling**: Display error with available options; exit with code 1
- **User Message**: "Error: Template type 'invalid' not found. Available types: [list]"

**Error Condition**: Language and template mismatch
- **Detection**: TemplateManager.get_templates() raises ValueError
- **Handling**: Display error with available combinations; exit with code 1
- **User Message**: "Error: No templates found for language 'en' and type 'cis-controls'"

**Error Condition**: Configuration file missing
- **Detection**: ConfigManager.load_config() raises FileNotFoundError
- **Handling**: Display error with instructions; exit with code 1
- **User Message**: "Configuration file not found: config.yaml. Run with --create-config to create default configuration."


## Testing Strategy

### Dual Testing Approach

The CIS Controls integration requires both unit tests and property-based tests to ensure comprehensive coverage:

- **Unit Tests**: Verify specific examples, edge cases, and integration points
- **Property Tests**: Verify universal properties across all inputs using randomization
- **Minimum 100 iterations per property test** (due to randomization)
- **Target: Maintain 86% code coverage** across the entire codebase

### Property-Based Testing

Property-based tests use the Hypothesis library to generate random test data and verify that properties hold across all inputs. Each property test must:

1. Run minimum 100 iterations with random inputs
2. Reference its design document property in a comment
3. Use the tag format: `Feature: cis-controls-integration, Property {number}: {property_text}`

**Example Property Test**:

```python
from hypothesis import given, settings
import hypothesis.strategies as st

@settings(max_examples=100)
@given(
    language=st.sampled_from(['de', 'en']),
    template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation', 'cis-controls'])
)
def test_property_1_template_discovery_completeness(language, template_type, tmp_path):
    """
    Feature: cis-controls-integration, Property 1: Template Discovery Completeness
    
    For any language directory containing a template type subdirectory with .md files,
    the Template_Manager SHALL discover and return all templates in that subdirectory.
    
    Validates: Requirements 1.1, 1.2, 4.1
    """
    # Create template structure
    template_dir = tmp_path / "templates" / language / template_type
    template_dir.mkdir(parents=True)
    
    # Create test templates
    expected_templates = []
    for i in range(3):
        template_file = template_dir / f"{(i+1)*10:04d}_test_template_{i}.md"
        template_file.write_text(f"# Template {i}")
        expected_templates.append(template_file)
    
    # Test discovery
    manager = TemplateManager(tmp_path / "templates")
    discovered = manager.discover_templates()
    
    # Verify all templates discovered
    assert language in discovered
    assert template_type in discovered[language]
    assert len(discovered[language][template_type]) == len(expected_templates)
```

### Unit Testing

Unit tests verify specific scenarios and edge cases:

**Template Discovery Tests**:
- Test discovery of CIS Controls templates in German directory
- Test discovery of CIS Controls templates in English directory
- Test discovery when CIS Controls directory is empty
- Test discovery when CIS Controls directory doesn't exist

**Template Parsing Tests**:
- Test parsing of CIS Controls metadata template
- Test parsing of CIS Controls content templates with valid numbering
- Test parsing of templates with invalid numbering
- Test extraction of sort order from filenames

**CLI Integration Tests**:
- Test `--template cis-controls` flag acceptance
- Test `-t cis-controls` short flag acceptance
- Test error message when invalid template type provided
- Test that cis-controls appears in available options

**Output Generation Tests**:
- Test Markdown generation for CIS Controls handbook
- Test PDF generation for CIS Controls handbook
- Test HTML generation for CIS Controls handbook
- Test separate files generation for CIS Controls
- Test PDF with TOC generation for CIS Controls

**Placeholder Processing Tests**:
- Test placeholder replacement in CIS Controls templates
- Test error handling for invalid placeholders
- Test metadata placeholder replacement

**Backward Compatibility Tests**:
- Test that BCM handbook generation produces identical output
- Test that ISMS handbook generation produces identical output
- Test that BSI Grundschutz handbook generation produces identical output
- Test that IT-Operation handbook generation produces identical output

### Integration Testing

Integration tests verify end-to-end workflows:

**Full Generation Workflow**:
```python
def test_cis_controls_full_generation_workflow():
    """Test complete workflow from CLI to output files."""
    # Run CLI command
    result = subprocess.run([
        './handbook-generator',
        '--language', 'de',
        '--template', 'cis-controls',
        '--output', 'all',
        '--test'
    ], capture_output=True)
    
    # Verify success
    assert result.returncode == 0
    
    # Verify output files exist
    assert Path('test-output/de/cis-controls/markdown/cis-controls_handbook.md').exists()
    assert Path('test-output/de/cis-controls/pdf/cis-controls_handbook.pdf').exists()
    assert Path('test-output/de/cis-controls/html/index.html').exists()
```

**Batch Generation Test**:
```python
def test_batch_generation_includes_cis_controls():
    """Test that batch generation script includes CIS Controls."""
    result = subprocess.run(['bash', 'helpers/generate_all_handbooks.sh'], capture_output=True)
    
    # Verify CIS Controls handbooks generated
    assert Path('test-output/de/cis-controls/html/index.html').exists()
    assert Path('test-output/en/cis-controls/html/index.html').exists()
```

### Test Organization

Tests are organized by component:

```
tests/
├── test_template_manager.py          # Template discovery and parsing
├── test_cli.py                        # CLI argument handling
├── test_output_generator.py           # Output generation
├── test_placeholder_processor.py      # Placeholder replacement
├── test_cis_controls_integration.py   # CIS Controls-specific tests
└── conftest.py                        # Shared fixtures
```

### Coverage Requirements

- **Minimum 86% overall code coverage** (maintain existing level)
- **100% coverage for new CIS Controls-specific code**
- **Property tests must run 100+ iterations each**
- **All existing tests must continue to pass**

