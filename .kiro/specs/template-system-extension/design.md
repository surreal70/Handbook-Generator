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
│              HTML Comment Processor (NEW)                    │
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
│  (Unchanged: Works with all template types)                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   Output Generator                           │
│  - Assembles processed templates                            │
│  - Generates Markdown output                                │
│  - Generates PDF output                                     │
│  (Unchanged: Works with all template types)                 │
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

### Test Coverage Goals

- **Unit Test Coverage**: >80% code coverage
- **Property Test Coverage**: All 15 correctness properties implemented
- **Integration Test Coverage**: All template types and languages
- **Regression Test Coverage**: All existing functionality preserved

