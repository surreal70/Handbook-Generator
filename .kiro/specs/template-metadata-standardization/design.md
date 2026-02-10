# Design Document: Template Metadata Standardization

## Overview

This design document specifies the technical approach for standardizing metadata across all compliance framework templates, adding version tracking, and reorganizing service-related templates. The implementation will enhance 12 existing frameworks with unified metadata structure, enable future compatibility management through version tracking, and improve repository organization.

## Architecture

### System Components

```
handbook-generator/
├── templates/
│   ├── de/
│   │   ├── service-directory/          # NEW: Reorganized service templates
│   │   │   ├── email-service/          # MOVED from templates/de/
│   │   │   └── service-templates/      # MOVED from templates/de/
│   │   ├── bcm/
│   │   │   └── 0000_metadata_de_bcm.md # ENHANCED with new fields
│   │   ├── isms/
│   │   ├── ... (10 more frameworks)
│   └── en/
│       └── (same structure as de/)
├── src/
│   └── metadata_standardizer.py       # NEW: Metadata management tool
├── helpers/
│   └── validate_metadata.py           # NEW: Metadata validation script
└── tests/
    └── test_metadata_standardization.py # NEW: Test suite
```

### Metadata Structure

#### Unified Metadata Template

All metadata files will follow this structure:

```markdown
# {Framework Name} Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbuch-Informationen

**Handbuch-Titel:** {Framework Full Name}  
**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  

---

## Dokumentenzweck

{Framework-specific purpose description}

## Geltungsbereich

{Framework-specific scope description}

## Normative Verweise

{Framework-specific references}

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initiale Version |

<!-- 
Dieses Dokument ist Teil des {Framework}-Handbuchs und unterliegt der Dokumentenlenkung.
Template-Version: 1.0 - Revision: 0
-->
```

### Required Metadata Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| document_id | String | Document identifier | "0000" |
| owner | Placeholder | Document owner | "{{ meta.owner }}" |
| version | Placeholder | Document version | "{{ meta.version }}" |
| status | Placeholder | Document status | "{{ meta.status }}" |
| classification | Placeholder | Security classification | "{{ meta.classification }}" |
| date | Placeholder | Last update date | "{{ meta.date }}" |
| template_version | String | Template format version | "1.0" |
| revision | Integer | Customization revision | "0" |
| organization | Placeholder | Organization name | "{{ meta.organization }}" |
| author | Placeholder | Document author | "{{ meta.author }}" |
| scope | Placeholder | Applicability scope | "{{ meta.scope }}" |
| valid_from | Placeholder | Validity start date | "{{ meta.valid_from }}" |
| next_review | Placeholder | Next review date | "{{ meta.next_review }}" |

## Implementation Components

### 1. Metadata Standardizer Tool

**File:** `src/metadata_standardizer.py`

**Purpose:** Scan, analyze, and standardize metadata files across all frameworks.

**Key Functions:**

```python
class MetadataStandardizer:
    def __init__(self, templates_dir: str):
        """Initialize with templates directory path"""
        
    def scan_frameworks(self) -> Dict[str, FrameworkStatus]:
        """Scan all frameworks and return status report"""
        
    def detect_missing_metadata(self) -> List[MissingMetadata]:
        """Identify frameworks missing metadata files"""
        
    def create_metadata_file(self, framework: str, language: str) -> bool:
        """Create standardized metadata file for framework"""
        
    def enhance_existing_metadata(self, filepath: str) -> bool:
        """Add missing fields to existing metadata file"""
        
    def validate_metadata_structure(self, filepath: str) -> ValidationResult:
        """Validate metadata file against unified structure"""
        
    def generate_report(self) -> StandardizationReport:
        """Generate summary report of standardization process"""
```

**Data Structures:**

```python
@dataclass
class FrameworkStatus:
    name: str
    has_de_metadata: bool
    has_en_metadata: bool
    de_metadata_complete: bool
    en_metadata_complete: bool
    missing_fields: List[str]
    
@dataclass
class MissingMetadata:
    framework: str
    language: str
    expected_path: str
    
@dataclass
class ValidationResult:
    is_valid: bool
    missing_fields: List[str]
    invalid_fields: List[str]
    warnings: List[str]
    
@dataclass
class StandardizationReport:
    total_frameworks: int
    frameworks_processed: int
    files_created: int
    files_enhanced: int
    validation_errors: int
    summary: str
```

### 2. Metadata Validation Script

**File:** `helpers/validate_metadata.py`

**Purpose:** Command-line tool for validating metadata across all frameworks.

**Usage:**
```bash
python helpers/validate_metadata.py --all
python helpers/validate_metadata.py --framework gdpr
python helpers/validate_metadata.py --language de
python helpers/validate_metadata.py --report output.json
```

**Validation Checks:**

1. **Required Fields Check**
   - Verify all 13 required fields are present
   - Check field format and syntax

2. **Template Version Check**
   - Verify template_version exists
   - Validate format: MAJOR.MINOR (e.g., "1.0")
   - Check semantic versioning compliance

3. **Revision Number Check**
   - Verify revision field exists
   - Validate it's a valid integer
   - Check it's >= 0

4. **Bilingual Consistency Check**
   - Compare DE and EN metadata files
   - Verify matching structure
   - Check placeholder consistency

5. **Placeholder Syntax Check**
   - Validate {{ source.field }} format
   - Check for malformed placeholders
   - Verify placeholder names are valid

### 3. Service Directory Reorganization

**Migration Script:** `helpers/reorganize_service_directory.py`

**Steps:**

1. Create new directories:
   - `templates/de/service-directory/`
   - `templates/en/service-directory/`

2. Move existing directories:
   - `templates/de/email-service/` → `templates/de/service-directory/email-service/`
   - `templates/de/service-templates/` → `templates/de/service-directory/service-templates/`
   - `templates/en/service-templates/` → `templates/en/service-directory/service-templates/`

3. Update references:
   - Search for hardcoded paths in Python code
   - Update documentation references
   - Update README.md examples

4. Verify migration:
   - Check all files moved successfully
   - Verify no broken links
   - Test handbook generation with new paths

## Framework-Specific Metadata

### Framework Metadata Templates

Each framework will have customized metadata with framework-specific information:

#### 1. BCM (Business Continuity Management)
```markdown
## Dokumentenzweck
Dieses Handbuch dokumentiert das Business Continuity Management (BCM) System der Organisation...

## Normative Verweise
- ISO 22301:2019 (Business Continuity Management)
- BSI Standard 100-4 (Notfallmanagement)
```

#### 2. GDPR (Data Protection)
```markdown
## Dokumentenzweck
Dieses Handbuch dokumentiert die Datenschutzmaßnahmen und -prozesse der Organisation gemäß der Datenschutz-Grundverordnung (DSGVO/GDPR - EU 2016/679)...

## Normative Verweise
- Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung - DSGVO)
- Bundesdatenschutzgesetz (BDSG)
```

#### 3. ISO 9001 (Quality Management)
```markdown
## Dokumentenzweck
Dieses Handbuch dokumentiert das Qualitätsmanagementsystem (QMS) der Organisation gemäß ISO 9001:2015...

## Normative Verweise
- ISO 9001:2015 (Quality Management Systems)
- ISO 9000:2015 (Quality Management - Fundamentals and vocabulary)
```

(Similar customizations for all 12 frameworks)

## Correctness Properties

### Property 1: Metadata Field Completeness
**Statement:** All metadata files SHALL contain all 13 required fields.

**Validation:**
```python
def test_metadata_completeness(metadata_file):
    required_fields = [
        'document_id', 'owner', 'version', 'status', 'classification',
        'date', 'template_version', 'revision', 'organization', 'author',
        'scope', 'valid_from', 'next_review'
    ]
    for field in required_fields:
        assert field_exists_in(metadata_file, field)
```

**Property-Based Test:**
```python
@given(framework=st.sampled_from(ALL_FRAMEWORKS),
       language=st.sampled_from(['de', 'en']))
def test_all_metadata_files_complete(framework, language):
    metadata_file = load_metadata(framework, language)
    assert has_all_required_fields(metadata_file)
```

### Property 2: Template Version Format
**Statement:** All template_version fields SHALL follow semantic versioning format "MAJOR.MINOR".

**Validation:**
```python
def test_template_version_format(metadata_file):
    version = extract_template_version(metadata_file)
    assert re.match(r'^\d+\.\d+$', version)
```

**Property-Based Test:**
```python
@given(framework=st.sampled_from(ALL_FRAMEWORKS),
       language=st.sampled_from(['de', 'en']))
def test_template_version_format_valid(framework, language):
    metadata_file = load_metadata(framework, language)
    version = extract_template_version(metadata_file)
    assert is_valid_semantic_version(version)
```

### Property 3: Revision Number Validity
**Statement:** All revision fields SHALL be non-negative integers.

**Validation:**
```python
def test_revision_number_valid(metadata_file):
    revision = extract_revision(metadata_file)
    assert isinstance(revision, int)
    assert revision >= 0
```

**Property-Based Test:**
```python
@given(framework=st.sampled_from(ALL_FRAMEWORKS),
       language=st.sampled_from(['de', 'en']))
def test_revision_is_valid_integer(framework, language):
    metadata_file = load_metadata(framework, language)
    revision = extract_revision(metadata_file)
    assert isinstance(revision, int) and revision >= 0
```

### Property 4: Bilingual Consistency
**Statement:** German and English metadata files for the same framework SHALL have identical structure.

**Validation:**
```python
def test_bilingual_consistency(framework):
    de_metadata = load_metadata(framework, 'de')
    en_metadata = load_metadata(framework, 'en')
    assert same_structure(de_metadata, en_metadata)
    assert same_placeholders(de_metadata, en_metadata)
```

**Property-Based Test:**
```python
@given(framework=st.sampled_from(ALL_FRAMEWORKS))
def test_de_en_metadata_structure_matches(framework):
    de_fields = extract_fields(load_metadata(framework, 'de'))
    en_fields = extract_fields(load_metadata(framework, 'en'))
    assert de_fields == en_fields
```

### Property 5: Placeholder Syntax Validity
**Statement:** All placeholders SHALL follow the format {{ source.field }}.

**Validation:**
```python
def test_placeholder_syntax(metadata_file):
    placeholders = extract_placeholders(metadata_file)
    for placeholder in placeholders:
        assert re.match(r'\{\{\s*\w+\.\w+\s*\}\}', placeholder)
```

**Property-Based Test:**
```python
@given(framework=st.sampled_from(ALL_FRAMEWORKS),
       language=st.sampled_from(['de', 'en']))
def test_all_placeholders_valid_syntax(framework, language):
    metadata_file = load_metadata(framework, language)
    placeholders = extract_placeholders(metadata_file)
    assert all(is_valid_placeholder(p) for p in placeholders)
```

### Property 6: Service Directory Structure
**Statement:** After reorganization, service templates SHALL be located in service-directory/.

**Validation:**
```python
def test_service_directory_structure():
    assert os.path.exists('templates/de/service-directory/email-service')
    assert os.path.exists('templates/de/service-directory/service-templates')
    assert os.path.exists('templates/en/service-directory/service-templates')
    assert not os.path.exists('templates/de/email-service')
    assert not os.path.exists('templates/de/service-templates')
```

**Property-Based Test:**
```python
@given(language=st.sampled_from(['de', 'en']))
def test_service_directory_exists_and_old_removed(language):
    service_dir = f'templates/{language}/service-directory'
    assert os.path.exists(service_dir)
    assert os.path.exists(f'{service_dir}/service-templates')
    if language == 'de':
        assert os.path.exists(f'{service_dir}/email-service')
```

## Error Handling

### Error Categories

1. **Missing Metadata File**
   - Error: Framework missing metadata file
   - Action: Create new metadata file with unified structure
   - Log: Framework name, language, created file path

2. **Incomplete Metadata**
   - Error: Metadata file missing required fields
   - Action: Add missing fields with placeholder values
   - Log: Framework name, missing fields list

3. **Invalid Template Version**
   - Error: template_version format invalid
   - Action: Set to "1.0" and log warning
   - Log: Framework name, invalid value, corrected value

4. **Invalid Revision Number**
   - Error: revision not a valid integer
   - Action: Set to 0 and log warning
   - Log: Framework name, invalid value

5. **Bilingual Inconsistency**
   - Error: DE and EN metadata structures don't match
   - Action: Report error, require manual review
   - Log: Framework name, specific inconsistencies

6. **File System Errors**
   - Error: Cannot read/write metadata file
   - Action: Report error, skip framework
   - Log: Framework name, error details, file path

### Error Recovery Strategy

```python
class MetadataError(Exception):
    """Base exception for metadata operations"""
    pass

class MissingMetadataError(MetadataError):
    """Raised when metadata file is missing"""
    def __init__(self, framework, language):
        self.framework = framework
        self.language = language
        super().__init__(f"Missing metadata for {framework} ({language})")

class InvalidMetadataError(MetadataError):
    """Raised when metadata structure is invalid"""
    def __init__(self, filepath, errors):
        self.filepath = filepath
        self.errors = errors
        super().__init__(f"Invalid metadata in {filepath}: {errors}")

def safe_metadata_operation(operation):
    """Decorator for safe metadata operations with error handling"""
    def wrapper(*args, **kwargs):
        try:
            return operation(*args, **kwargs)
        except MissingMetadataError as e:
            logger.warning(f"Missing metadata: {e}")
            return create_default_metadata(e.framework, e.language)
        except InvalidMetadataError as e:
            logger.error(f"Invalid metadata: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
    return wrapper
```

## Testing Strategy

### Unit Tests

1. **Metadata Field Extraction**
   - Test extracting each required field
   - Test handling missing fields
   - Test placeholder preservation

2. **Template Version Parsing**
   - Test valid version formats
   - Test invalid version formats
   - Test version comparison

3. **Revision Number Handling**
   - Test integer parsing
   - Test invalid values
   - Test increment operations

4. **File Operations**
   - Test reading metadata files
   - Test writing metadata files
   - Test file path handling

### Integration Tests

1. **End-to-End Standardization**
   - Run standardizer on all frameworks
   - Verify all metadata files created/enhanced
   - Validate all files pass validation

2. **Service Directory Migration**
   - Run reorganization script
   - Verify all files moved correctly
   - Test handbook generation with new paths

3. **Backward Compatibility**
   - Test with existing metadata files
   - Verify handbook generation still works
   - Test with missing optional fields

### Property-Based Tests

All 6 correctness properties will be tested using Hypothesis with:
- Minimum 100 test cases per property
- All 12 frameworks tested
- Both languages (de/en) tested
- Edge cases: empty files, malformed syntax, missing sections

## Migration Path

### Phase 1: Preparation
1. Backup existing metadata files
2. Create metadata standardizer tool
3. Create validation script
4. Run initial scan and generate report

### Phase 2: Metadata Enhancement
1. Identify frameworks with missing/incomplete metadata
2. Create missing metadata files
3. Enhance existing metadata files
4. Add template_version and revision fields

### Phase 3: Service Directory Reorganization
1. Create service-directory structure
2. Move email-service and service-templates
3. Update code references
4. Update documentation

### Phase 4: Validation
1. Run validation on all frameworks
2. Fix any validation errors
3. Verify bilingual consistency
4. Test handbook generation

### Phase 5: Documentation
1. Update README.md
2. Create migration guide
3. Document new metadata fields
4. Update framework-specific docs

## Backward Compatibility

### Compatibility Guarantees

1. **Existing Handbooks**
   - All existing handbook generation will continue to work
   - New fields are optional for existing handbooks
   - Placeholders without data are preserved

2. **Old Metadata Format**
   - System will handle metadata files without template_version/revision
   - Validation will warn (not error) on missing new fields
   - Automatic migration available via standardizer tool

3. **Service Templates**
   - Old paths will be deprecated but documented
   - Migration script provided for updating references
   - Handbook generator will support both old and new paths temporarily

### Migration Guide

```markdown
# Migration Guide: Template Metadata Standardization

## For Existing Users

If you have existing handbooks, follow these steps:

1. **Backup your metadata files**
   ```bash
   cp -r templates/ templates.backup/
   ```

2. **Run the standardizer**
   ```bash
   python src/metadata_standardizer.py --enhance-all
   ```

3. **Validate the results**
   ```bash
   python helpers/validate_metadata.py --all
   ```

4. **Update service template references (if applicable)**
   ```bash
   python helpers/reorganize_service_directory.py
   ```

5. **Test handbook generation**
   ```bash
   ./handbook-generator --template gdpr --language de --output test-output/
   ```

## New Fields

- **template_version**: Set to "1.0" for all existing templates
- **revision**: Set to "0" for all existing templates

These fields enable future compatibility tracking and customization management.
```

## Performance Considerations

### Optimization Strategies

1. **Parallel Processing**
   - Process multiple frameworks concurrently
   - Use multiprocessing for independent operations
   - Target: < 5 seconds for all 12 frameworks

2. **Caching**
   - Cache parsed metadata files
   - Cache validation results
   - Invalidate cache on file changes

3. **Incremental Updates**
   - Only process changed files
   - Track modification timestamps
   - Skip unchanged frameworks

4. **Memory Management**
   - Stream large files instead of loading entirely
   - Release resources after processing each framework
   - Limit concurrent file operations

## Security Considerations

1. **File Path Validation**
   - Validate all file paths to prevent directory traversal
   - Restrict operations to templates/ directory
   - Sanitize user input in file names

2. **Content Validation**
   - Validate metadata content before writing
   - Prevent injection of malicious placeholders
   - Sanitize markdown content

3. **Backup Strategy**
   - Create backups before modifications
   - Enable rollback on errors
   - Log all file operations

## Success Metrics

The implementation will be considered successful when:

1. **Coverage**: All 12 frameworks have complete metadata (100%)
2. **Validation**: All metadata files pass validation (0 errors)
3. **Consistency**: All bilingual pairs are consistent (100%)
4. **Performance**: Standardization completes in < 5 seconds
5. **Compatibility**: All existing handbooks generate successfully
6. **Documentation**: Migration guide and examples available
7. **Tests**: All unit and property-based tests pass
8. **Organization**: Service templates reorganized successfully
