# Design Document: Configuration Separation and Metadata Unification

## Overview

This design implements a comprehensive restructuring of the Handbook Generator's configuration and metadata system. The current monolithic `metadata.yaml` file will be separated into four logical configuration files, and all template placeholders will be unified to use English identifiers. Additionally, handbook-specific metadata will be moved to individual `meta-handbook.yaml` files within each handbook directory.

The design focuses on:
1. **Logical separation** of configuration concerns (global, organization, roles, handbook-specific)
2. **Language-agnostic placeholders** using English identifiers across all templates
3. **Standardized document headers** with consistent metadata display
4. **Backward incompatibility** - no migration support, clean break from old format

## Architecture

### Configuration File Structure

The new configuration architecture consists of five distinct files:

```
project-root/
├── config.yaml                    # Data source references
├── meta-global.yaml               # Handbook Generator version info
├── meta-organisation.yaml         # Organization information
├── meta-organisation-roles.yaml   # Personnel roles
└── handbooks/
    ├── bcm/
    │   ├── meta-handbook.yaml     # BCM handbook metadata
    │   └── templates/
    ├── isms/
    │   ├── meta-handbook.yaml     # ISMS handbook metadata
    │   └── templates/
    └── ...
```

### Configuration Loading Strategy

The system will use a **cascading configuration loader** that:

1. Loads `config.yaml` first to determine data source locations
2. Loads global metadata files in order:
   - `meta-global.yaml`
   - `meta-organisation.yaml`
   - `meta-organisation-roles.yaml`
3. When processing a specific handbook, loads `meta-handbook.yaml` from that handbook's directory
4. Merges all configurations into a unified metadata context
5. Provides default values for missing fields

### Data Flow

```
config.yaml
    ↓
ConfigManager
    ↓
MetadataConfigManager
    ├→ meta-global.yaml
    ├→ meta-organisation.yaml
    ├→ meta-organisation-roles.yaml
    └→ meta-handbook.yaml (per handbook)
    ↓
Unified Metadata Context
    ↓
PlaceholderProcessor
    ↓
Template with Resolved Placeholders
```

## Components and Interfaces

### 1. ConfigManager (Modified)

**Responsibilities:**
- Load `config.yaml` and parse data source references
- Coordinate loading of all metadata files
- Provide unified configuration object to the system

**Key Changes:**
```python
class ConfigManager:
    def load_config(self) -> Config:
        """Load config.yaml and all metadata files."""
        # Load config.yaml
        config_data = self._load_yaml(self.config_path)
        
        # Load metadata files based on config.yaml references
        metadata_loader = MetadataLoader(config_data['data_sources'])
        metadata = metadata_loader.load_all_metadata()
        
        return Config(
            data_sources=config_data['data_sources'],
            metadata=metadata
        )
```

**Interface:**
```python
@dataclass
class Config:
    data_sources: Dict[str, DataSourceConfig]
    metadata: UnifiedMetadata
    default_language: str = "de"
    default_output_format: str = "both"
```

### 2. MetadataLoader (New Component)

**Responsibilities:**
- Load and parse all metadata YAML files
- Validate metadata structure and required fields
- Provide default values for missing fields
- Merge metadata into unified context

**Interface:**
```python
class MetadataLoader:
    def __init__(self, data_source_config: Dict):
        """Initialize with data source configuration from config.yaml."""
        self.meta_global_path = Path(data_source_config.get('meta-global', 'meta-global.yaml'))
        self.meta_org_path = Path(data_source_config.get('meta-organisation', 'meta-organisation.yaml'))
        self.meta_roles_path = Path(data_source_config.get('meta-organisation-roles', 'meta-organisation-roles.yaml'))
    
    def load_all_metadata(self) -> UnifiedMetadata:
        """Load all global metadata files."""
        global_meta = self._load_global_metadata()
        org_meta = self._load_organisation_metadata()
        roles_meta = self._load_roles_metadata()
        
        return UnifiedMetadata(
            global_info=global_meta,
            organisation=org_meta,
            roles=roles_meta
        )
    
    def load_handbook_metadata(self, handbook_path: Path) -> HandbookMetadata:
        """Load handbook-specific metadata from handbook directory."""
        meta_handbook_path = handbook_path / "meta-handbook.yaml"
        return self._load_handbook_metadata(meta_handbook_path)
    
    def _load_global_metadata(self) -> GlobalMetadata:
        """Load meta-global.yaml with defaults."""
        # Implementation with default fallbacks
    
    def _load_organisation_metadata(self) -> OrganisationMetadata:
        """Load meta-organisation.yaml with defaults."""
        # Implementation with default fallbacks
    
    def _load_roles_metadata(self) -> RolesMetadata:
        """Load meta-organisation-roles.yaml with defaults."""
        # Implementation with default fallbacks
    
    def _load_handbook_metadata(self, path: Path) -> HandbookMetadata:
        """Load meta-handbook.yaml with defaults."""
        # Implementation with default fallbacks
```

### 3. UnifiedMetadata (New Data Model)

**Responsibilities:**
- Provide unified access to all metadata
- Support nested field access (e.g., `meta-organisation.name`)
- Handle default values transparently

**Interface:**
```python
@dataclass
class GlobalMetadata:
    source: str = "HandBook Generator"
    version: str = "1.0.0"

@dataclass
class OrganisationMetadata:
    name: str = "[TODO]"
    address: str = "[TODO]"
    web: str = "[TODO]"
    phone: str = "[TODO]"
    revision: int = 0

@dataclass
class RolesMetadata:
    role_CEO: str = "[TODO]"
    role_CFO: str = "[TODO]"
    role_CTO: str = "[TODO]"
    role_CIO: str = "[TODO]"
    role_CISO: str = "[TODO]"
    role_HR_Manager: str = "[TODO]"
    role_Risk_Manager: str = "[TODO]"
    role_GDPR_Manager: str = "[TODO]"
    role_IT_Manager: str = "[TODO]"
    role_Compliance_Manager: str = "[TODO]"
    role_Internal_Auditor: str = "[TODO]"
    group_IT_Services: str = "[TODO]"
    group_DEVOPS: str = "[TODO]"
    group_Helpdesk: str = "[TODO]"

@dataclass
class HandbookMetadata:
    author: str = "[TODO]"
    classification: str = "[TODO]"
    status: str = "[TODO]"
    type: str = "[TODO]"
    templateset_version: str = "0.1"
    revision: int = 0
    shortname: str = "[TODO]"
    longname: str = "[TODO]"
    maintainer: str = None  # Defaults to author
    owner: str = "[TODO]"
    approver: str = "[TODO]"
    creationdate: str = "[TODO]"
    modifydate: str = "[TODO]"
    valid_from: str = "[TODO]"
    next_review: str = "[TODO]"
    scope: str = "[TODO]"
    
    def __post_init__(self):
        """Set maintainer to author if not specified."""
        if self.maintainer is None:
            self.maintainer = self.author

@dataclass
class UnifiedMetadata:
    global_info: GlobalMetadata
    organisation: OrganisationMetadata
    roles: RolesMetadata
    handbook: Optional[HandbookMetadata] = None
    
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Get field value by path (e.g., 'meta-organisation.name').
        
        Supports paths like:
        - meta-global.version
        - meta-organisation.name
        - meta-organisation-roles.role_CEO
        - meta-handbook.author
        """
        parts = field_path.split('.')
        if len(parts) < 2:
            return None
        
        source = parts[0]
        field = '.'.join(parts[1:])
        
        if source == 'meta-global':
            return self._get_nested_field(self.global_info, field)
        elif source == 'meta-organisation':
            return self._get_nested_field(self.organisation, field)
        elif source == 'meta-organisation-roles':
            return self._get_nested_field(self.roles, field)
        elif source == 'meta-handbook':
            if self.handbook is None:
                return None
            return self._get_nested_field(self.handbook, field)
        
        return None
    
    def _get_nested_field(self, obj, field_path: str):
        """Get nested field from object using dot notation."""
        current = obj
        for part in field_path.split('.'):
            if hasattr(current, part):
                current = getattr(current, part)
            else:
                return None
        return current
```

### 4. PlaceholderProcessor (Modified)

**Responsibilities:**
- Detect placeholders in templates
- Resolve placeholders using UnifiedMetadata
- Support new English placeholder format

**Key Changes:**
```python
class PlaceholderProcessor:
    # Updated pattern to support new placeholder format
    # Matches: {{ meta-global.version }}, {{ meta-organisation.name }}, etc.
    PLACEHOLDER_PATTERN = re.compile(r'\{\{\s*(meta-[\w-]+)\.(\w+(?:\.\w+)*)\s*\}\}')
    
    def __init__(self, unified_metadata: UnifiedMetadata):
        """Initialize with unified metadata context."""
        self.metadata = unified_metadata
    
    def replace_placeholder(self, placeholder: Placeholder) -> tuple[Optional[str], Optional[str]]:
        """
        Replace placeholder using unified metadata.
        
        Supports:
        - {{ meta-global.version }}
        - {{ meta-organisation.name }}
        - {{ meta-organisation-roles.role_CEO }}
        - {{ meta-handbook.author }}
        """
        # Build full field path
        full_path = f"{placeholder.source}.{placeholder.field}"
        
        # Get value from unified metadata
        value = self.metadata.get_field(full_path)
        
        if value is None:
            warning = f"Field not found: {full_path}"
            return None, warning
        
        return str(value), None
```

### 5. TemplateManager (Modified)

**Responsibilities:**
- Load templates from handbook directories
- Load handbook-specific metadata
- Process templates with unified metadata context

**Key Changes:**
```python
class TemplateManager:
    def process_handbook(self, handbook_path: Path, unified_metadata: UnifiedMetadata):
        """Process all templates in a handbook directory."""
        # Load handbook-specific metadata
        metadata_loader = MetadataLoader({})
        handbook_meta = metadata_loader.load_handbook_metadata(handbook_path)
        
        # Add handbook metadata to unified context
        unified_metadata.handbook = handbook_meta
        
        # Process templates
        for template_file in self._find_templates(handbook_path):
            processor = PlaceholderProcessor(unified_metadata)
            result = processor.process_template(template_file.read_text())
            # ... handle result
```

## Data Models

### Configuration File Schemas

#### config.yaml
```yaml
data_sources:
  meta-global: "meta-global.yaml"
  meta-organisation: "meta-organisation.yaml"
  meta-organisation-roles: "meta-organisation-roles.yaml"
  # Optional external sources
  netbox:
    url: "https://netbox.example.com"
    api_token: "xyz"
```

#### meta-global.yaml
```yaml
source: "HandBook Generator"
version: "1.0.0"
```

#### meta-organisation.yaml
```yaml
name: "AdminsEnd Ltd."
address: "Endless Lane 42, DE-35813 LandsEnd"
web: "https://www.adminsend.de"
phone: "+49 2323 555 4242"
revision: 0
```

#### meta-organisation-roles.yaml
```yaml
role_CEO: "[TODO]"
role_CFO: "[TODO]"
role_CTO: "[TODO]"
role_CIO: "[TODO]"
role_CISO: "[TODO]"
role_HR_Manager: "[TODO]"
role_Risk_Manager: "[TODO]"
role_GDPR_Manager: "[TODO]"
role_IT_Manager: "[TODO]"
role_Compliance_Manager: "[TODO]"
role_Internal_Auditor: "[TODO]"
group_IT_Services: "[TODO]"
group_DEVOPS: "[TODO]"
group_Helpdesk: "[TODO]"
```

#### meta-handbook.yaml (in each handbook directory)
```yaml
author: "[TODO]"
classification: "[TODO]"
status: "[TODO]"
type: "[TODO]"
templateset_version: "0.1"
revision: 0
shortname: "[TODO]"
longname: "[TODO]"
maintainer: "[author value]"  # defaults to author
owner: "[TODO]"
approver: "[TODO]"
creationdate: "[TODO]"
modifydate: "[TODO]"
valid_from: "[TODO]"
next_review: "[TODO]"
scope: "[TODO]"
```

### Placeholder Mapping

Old format → New format:

| Old Placeholder | New Placeholder |
|----------------|-----------------|
| `{{ meta.organisation.name }}` | `{{ meta-organisation.name }}` |
| `{{ meta.document.owner }}` | `{{ meta-handbook.owner }}` |
| `{{ meta.document.version }}` | `{{ meta-handbook.revision }}` |
| `{{ meta.ceo.name }}` | `{{ meta-organisation-roles.role_CEO }}` |
| `{{ metadata.version }}` | `{{ meta-global.version }}` |
| `{{ metadata.author }}` | `{{ meta-handbook.author }}` |

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*


### Property Reflection

After analyzing all acceptance criteria, I've identified several areas where properties can be consolidated:

**Redundancy Analysis:**

1. **Default value properties (1.3, 3.2, 4.2, 5.2, 8.5)**: These all test the same behavior - when configuration files are missing, defaults are used. Can be consolidated into a single comprehensive property.

2. **Placeholder replacement properties (3.3, 4.3, 5.3, 6.4)**: These all test placeholder replacement for different metadata sources. Can be consolidated into a single property that tests all placeholder types.

3. **File structure examples (2.1, 3.1, 4.1, 5.1, 6.1, 10.1)**: These are all example tests checking specific file structures. Keep as examples but don't create separate properties.

4. **Validation properties (1.4, 9.1)**: These test the same validation behavior. Consolidate into one property.

**Consolidated Properties:**
- Configuration loading and defaults (combines 1.1, 1.2, 1.3, 3.2, 4.2, 5.2)
- Placeholder replacement (combines 3.3, 4.3, 5.3, 6.4)
- Validation and error reporting (combines 1.4, 9.1, 9.2)
- Template structure validation (combines 7.1, 7.2, 8.1)

### Property 1: Configuration File Loading
*For any* valid set of configuration files (config.yaml, meta-global.yaml, meta-organisation.yaml, meta-organisation-roles.yaml), when the system initializes, all four files should be loaded and their contents should be accessible through the unified metadata context.

**Validates: Requirements 1.1**

### Property 2: Handbook Metadata Loading
*For any* handbook directory containing a meta-handbook.yaml file, when that handbook is processed, the handbook-specific metadata should be loaded and merged into the unified metadata context.

**Validates: Requirements 1.2**

### Property 3: Default Values for Missing Configuration
*For any* missing configuration file (meta-global.yaml, meta-organisation.yaml, meta-organisation-roles.yaml, or meta-handbook.yaml), the system should use predefined default values and continue operation without errors.

**Validates: Requirements 1.3, 3.2, 4.2, 5.2, 6.5**

### Property 4: Configuration Validation
*For any* configuration file with invalid YAML syntax, missing required fields, or incorrect field types, the system should report specific validation errors including file name, field name, and corrective action.

**Validates: Requirements 1.4, 9.1, 9.2**

### Property 5: Optional External Data Sources
*For any* configuration with or without external data sources (netbox, verinice), the system should function correctly, treating external sources as optional.

**Validates: Requirements 2.2**

### Property 6: Relative Path Resolution
*For any* config.yaml file location, when meta-* file paths are specified, they should be resolved relative to the config.yaml location.

**Validates: Requirements 2.3**

### Property 7: Unified Placeholder Replacement
*For any* template containing placeholders in the format {{ meta-source.field }}, all placeholders should be replaced with corresponding values from the unified metadata context (meta-global, meta-organisation, meta-organisation-roles, meta-handbook).

**Validates: Requirements 3.3, 4.3, 5.3, 6.4, 7.2**

### Property 8: Maintainer Default Value
*For any* meta-handbook.yaml file where maintainer is not specified, the maintainer field should default to the author field value.

**Validates: Requirements 6.2**

### Property 9: English Placeholder Format
*For any* template file, all placeholders should use English identifiers following the pattern {{ meta-source.field }} where source is one of: meta-global, meta-organisation, meta-organisation-roles, meta-handbook.

**Validates: Requirements 7.1, 7.2**

### Property 10: Bilingual Placeholder Consistency
*For any* handbook that has both German (de) and English (en) template versions, the placeholders used in both language versions should be identical (same English identifiers).

**Validates: Requirements 7.3**

### Property 11: Standardized Document Headers
*For any* template file, it should contain a document header section with the required metadata fields (Document-ID, Organisation, Owner, Approved by, Revision, Author, Status, Classification, Last Update).

**Validates: Requirements 8.1**

### Property 12: Localized Header Labels
*For any* template file, the document header labels should match the template language (German labels for de/ templates, English labels for en/ templates).

**Validates: Requirements 8.2**

### Property 13: No Trailing Version Information
*For any* template file, there should be no version information section at the end of the file (version info is now in the header).

**Validates: Requirements 8.3**

### Property 14: English Role Identifiers
*For any* meta-organisation-roles.yaml file, all role field names should use English identifiers (role_CEO, role_CIO, etc., not rolle_CEO, rolle_CIO).

**Validates: Requirements 5.4**

### Property 15: Circular Reference Detection
*For any* configuration with circular file references, the system should detect the circular reference, report an error, and halt processing.

**Validates: Requirements 9.3**

### Property 16: TODO Value Warnings
*For any* configuration containing [TODO] placeholder values, when templates are generated, the system should emit warnings but continue generation.

**Validates: Requirements 9.4**

### Property 17: Example File Completeness
*For any* example configuration file (config.example.yaml, meta-global.example.yaml, etc.), it should contain complete structure, inline comments, realistic example values, and documentation references.

**Validates: Requirements 10.2**

### Property 18: Documentation Completeness
*For any* documentation file, it should include all required sections: migration guide, placeholder reference, configuration file reference, template header specification, and troubleshooting guide.

**Validates: Requirements 10.3**

## Error Handling

### Error Categories

1. **Configuration Loading Errors**
   - Missing required configuration files (use defaults)
   - Invalid YAML syntax (report error with line number)
   - Missing required fields (report field name and provide default)
   - Invalid field types (report expected vs actual type)

2. **Placeholder Resolution Errors**
   - Unknown metadata source (report available sources)
   - Field not found in metadata (report field path)
   - Circular references (detect and halt)

3. **Validation Errors**
   - Invalid placeholder format (report line number and correct format)
   - Missing document headers (report template name)
   - German placeholders in templates (report placeholder and suggest English equivalent)

### Error Reporting Strategy

All errors should follow this format:
```
[ERROR|WARNING] [Component] [File:Line]: Message
  Context: Additional context information
  Suggestion: Corrective action
```

Example:
```
ERROR ConfigLoader meta-organisation.yaml:5: Missing required field 'name'
  Context: Field 'name' is required for organization metadata
  Suggestion: Add 'name: "Your Organization Name"' to meta-organisation.yaml
```

### Default Value Strategy

When configuration is missing or invalid, use these defaults:

| Field | Default Value | Rationale |
|-------|--------------|-----------|
| meta-global.source | "HandBook Generator" | Standard product name |
| meta-global.version | "1.0.0" | Semantic versioning start |
| meta-organisation.* | "[TODO]" | Explicit placeholder for user to fill |
| meta-organisation-roles.* | "[TODO]" | Explicit placeholder for user to fill |
| meta-handbook.* | "[TODO]" | Explicit placeholder for user to fill |
| meta-handbook.revision | 0 | Start at zero |
| meta-handbook.maintainer | author value | Sensible default |

## Testing Strategy

### Unit Testing Approach

Unit tests will focus on:

1. **Configuration Loading**
   - Test loading each configuration file individually
   - Test loading with missing files (verify defaults)
   - Test loading with invalid YAML (verify error reporting)
   - Test loading with missing required fields (verify defaults and warnings)

2. **Metadata Merging**
   - Test merging global metadata
   - Test merging handbook-specific metadata
   - Test field access through unified metadata context

3. **Placeholder Processing**
   - Test placeholder detection with new format
   - Test placeholder replacement with each metadata source
   - Test error handling for unknown sources/fields

4. **Validation**
   - Test YAML syntax validation
   - Test required field validation
   - Test field type validation
   - Test circular reference detection

5. **Template Processing**
   - Test document header detection
   - Test placeholder format validation
   - Test bilingual consistency checking

### Property-Based Testing Approach

Property tests will verify universal behaviors across all inputs:

1. **Configuration Round-Trip Property**
   - For any valid configuration, loading and then accessing all fields should return the original values
   - Minimum 100 iterations with randomly generated valid configurations

2. **Placeholder Replacement Idempotence**
   - For any template with placeholders, processing it twice should produce the same result as processing it once
   - Validates that placeholder replacement doesn't introduce new placeholders

3. **Default Value Consistency**
   - For any missing configuration file, the defaults used should be consistent across multiple loads
   - Validates that default generation is deterministic

4. **Path Resolution Consistency**
   - For any config.yaml location, relative paths should resolve consistently regardless of current working directory
   - Validates path resolution is based on config.yaml location, not CWD

5. **Validation Completeness**
   - For any invalid configuration, at least one validation error should be reported
   - Validates that validation catches all invalid states

6. **Bilingual Placeholder Invariant**
   - For any handbook with both de/ and en/ templates, the set of placeholders should be identical
   - Validates language-agnostic placeholder design

### Test Configuration

All property-based tests will:
- Run minimum 100 iterations per test
- Use hypothesis library for Python
- Tag tests with: **Feature: config-separation-and-metadata-unification, Property N: [property text]**
- Generate random but valid test data
- Include edge cases (empty strings, special characters, boundary values)

### Integration Testing

Integration tests will verify:

1. **End-to-End Handbook Generation**
   - Create complete configuration set
   - Process a handbook with templates
   - Verify all placeholders are replaced
   - Verify output contains correct metadata

2. **Multi-Handbook Processing**
   - Process multiple handbooks with different meta-handbook.yaml files
   - Verify each handbook gets correct metadata
   - Verify no cross-contamination between handbooks

3. **Backward Incompatibility**
   - Verify old placeholder format is not supported
   - Verify old metadata.yaml structure is not loaded
   - Verify clear error messages for old format

## Migration Strategy

**Important: NO automatic migration is provided.**

Users must manually create the new configuration structure. The system will:

1. **Detect old format** and provide clear error message:
   ```
   ERROR: Old configuration format detected (metadata.yaml)
   
   The configuration format has changed. Please create new configuration files:
   - config.yaml
   - meta-global.yaml
   - meta-organisation.yaml
   - meta-organisation-roles.yaml
   - meta-handbook.yaml (in each handbook directory)
   
   See documentation: docs/MIGRATION_GUIDE.md
   Example files: *.example.yaml
   ```

2. **Provide example files** for all new configuration formats

3. **Provide documentation** with:
   - Step-by-step migration instructions
   - Mapping from old to new structure
   - Placeholder conversion table
   - Common pitfalls and solutions

### Manual Migration Steps

Users will need to:

1. **Create config.yaml**
   - Copy data source configuration from old config.yaml
   - Add references to new metadata files

2. **Create meta-global.yaml**
   - Extract version information
   - Set source to "HandBook Generator"

3. **Create meta-organisation.yaml**
   - Extract organization section from old metadata.yaml
   - Flatten structure (remove nested fields if any)

4. **Create meta-organisation-roles.yaml**
   - Extract roles section from old metadata.yaml
   - Rename role keys to English (ceo → role_CEO)

5. **Create meta-handbook.yaml in each handbook directory**
   - Extract handbook-specific metadata from old metadata.yaml handbooks section
   - Add new required fields (shortname, longname, scope, etc.)

6. **Update all templates**
   - Replace old placeholders with new format
   - Add standardized document headers
   - Remove trailing version information

## Implementation Notes

### File Organization

```
project-root/
├── config.yaml
├── config.example.yaml
├── meta-global.yaml
├── meta-global.example.yaml
├── meta-organisation.yaml
├── meta-organisation.example.yaml
├── meta-organisation-roles.yaml
├── meta-organisation-roles.example.yaml
├── src/
│   ├── config_manager.py (modified)
│   ├── metadata_loader.py (new)
│   ├── unified_metadata.py (new)
│   ├── placeholder_processor.py (modified)
│   └── template_manager.py (modified)
├── templates/
│   ├── de/
│   │   ├── bcm/
│   │   │   ├── meta-handbook.yaml
│   │   │   ├── meta-handbook.example.yaml
│   │   │   └── *.md (updated templates)
│   │   └── isms/
│   │       ├── meta-handbook.yaml
│   │       ├── meta-handbook.example.yaml
│   │       └── *.md (updated templates)
│   └── en/
│       └── (similar structure)
├── tests/
│   ├── test_config_separation.py (new)
│   ├── test_metadata_loader.py (new)
│   ├── test_unified_metadata.py (new)
│   ├── test_placeholder_processor.py (updated)
│   └── test_template_manager.py (updated)
└── docs/
    ├── MIGRATION_GUIDE.md (new)
    ├── CONFIGURATION_REFERENCE.md (new)
    └── PLACEHOLDER_REFERENCE.md (new)
```

### Backward Compatibility

**None.** This is a breaking change. The system will:
- Not load old metadata.yaml format
- Not support old placeholder format
- Provide clear error messages directing users to migration guide
- Fail fast with actionable error messages

### Performance Considerations

1. **Configuration Caching**
   - Load configuration files once at startup
   - Cache unified metadata context
   - Reload only when files change (optional watch mode)

2. **Lazy Loading**
   - Load handbook-specific metadata only when processing that handbook
   - Don't load all handbook metadata at startup

3. **Validation Optimization**
   - Validate configuration once at load time
   - Cache validation results
   - Skip re-validation during template processing

### Security Considerations

1. **File Path Validation**
   - Validate all file paths to prevent directory traversal
   - Ensure paths are relative to config.yaml location
   - Reject absolute paths in configuration

2. **YAML Safety**
   - Use yaml.safe_load() to prevent code execution
   - Validate YAML structure before processing
   - Limit file size to prevent DoS

3. **Sensitive Data**
   - Keep config.yaml in .gitignore (contains API tokens)
   - Metadata files can be committed (no sensitive data)
   - Document which files should/shouldn't be committed

## Documentation Requirements

### User Documentation

1. **MIGRATION_GUIDE.md**
   - Overview of changes
   - Step-by-step migration instructions
   - Placeholder conversion table
   - Common issues and solutions
   - FAQ

2. **CONFIGURATION_REFERENCE.md**
   - Complete reference for all configuration files
   - Field descriptions and valid values
   - Default values
   - Examples for each file

3. **PLACEHOLDER_REFERENCE.md**
   - Complete list of all placeholders
   - Organized by metadata source
   - Examples of usage
   - Mapping from old to new format

4. **TEMPLATE_HEADER_SPECIFICATION.md**
   - Document header format
   - Required fields
   - Language-specific variations
   - Examples

### Developer Documentation

1. **Architecture documentation** in code comments
2. **API documentation** for new components
3. **Test documentation** explaining property-based tests
4. **Contributing guide** for adding new metadata fields

## Success Criteria

1. ✅ All configuration files successfully separated into logical components
2. ✅ All templates updated with standardized headers and English placeholders
3. ✅ All existing tests pass with new configuration structure
4. ✅ New tests added for configuration loading, validation, and placeholder processing
5. ✅ Property-based tests implemented for all correctness properties
6. ✅ Documentation complete and accurate
7. ✅ Example configuration files provided for all new formats
8. ✅ Migration guide complete with step-by-step instructions
9. ✅ No backward compatibility with old format (clean break)
10. ✅ Clear error messages for old format detection
