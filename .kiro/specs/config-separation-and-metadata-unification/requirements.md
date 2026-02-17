# Requirements: Configuration Separation and Metadata Unification

## Feature Name
config-separation-and-metadata-unification

## Overview
This feature separates configuration files into logical components (global, organization, roles, handbook-specific) and unifies metadata placeholders to be language-agnostic and English-only across all templates.

## Glossary

- **Metadata Placeholder**: Template variable in format `{{ identifier.field }}` that gets replaced with actual values during handbook generation
- **Global Config**: System-wide configuration containing Handbook Generator version and source information
- **Organization Config**: Organization-specific information like name, address, contact details
- **Roles Config**: Personnel roles and contact information (CEO, CIO, CISO, etc.)
- **Handbook Config**: Individual handbook metadata (author, classification, status, revision, dates)
- **Template Header**: Standardized document header at the beginning of each template file
- **Language-Agnostic**: Placeholders that work identically in German (de) and English (en) templates

## User Stories

### 1. Configuration File Separation

**Als** Handbook Generator Administrator  
**möchte ich** separate Konfigurationsdateien für verschiedene Aspekte (Global, Organisation, Rollen, Handbuch)  
**damit** ich Konfigurationen logisch organisieren und unabhängig verwalten kann.

#### Acceptance Criteria

**WHEN** the system initializes  
**THEN** it **SHALL** load configuration from four separate YAML files:
- `config.yaml` (global configuration with data source references)
- `meta-global.yaml` (Handbook Generator version and source)
- `meta-organisation.yaml` (organization information)
- `meta-organisation-roles.yaml` (personnel roles)

**WHEN** a handbook is generated  
**THEN** it **SHALL** also load handbook-specific configuration from `meta-handbook.yaml` in the handbook's root directory

**WHEN** any configuration file is missing  
**THEN** the system **SHALL** use default values as specified in the requirements

**WHEN** configuration files are loaded  
**THEN** the system **SHALL** validate required fields and report missing or invalid values

### 2. Global Configuration Structure

**Als** System Administrator  
**möchte ich** eine zentrale config.yaml mit Datenquellen-Referenzen  
**damit** ich externe Datenquellen und globale Metadaten-Dateien konfigurieren kann.

#### Acceptance Criteria

**WHEN** config.yaml is created  
**THEN** it **SHALL** contain the following structure:
```yaml
data_sources:
  meta-global: "meta-global.yaml"
  meta-organisation: "meta-organisation.yaml"
  meta-organisation-roles: "meta-organisation-roles.yaml"
  # Optional external sources
  netbox:
    url: "https://netbox.example.com"
    api_token: "xyz"
  verinice:
    url: "https://verinice.example.com"
    api_token: "xyz"
```

**WHEN** external data sources (netbox, verinice) are configured  
**THEN** they **SHALL** be optional and the system **SHALL** function without them

**WHEN** meta-* file paths are specified  
**THEN** they **SHALL** be relative to the config.yaml location

### 3. Global Metadata (meta-global.yaml)

**Als** System  
**möchte ich** Handbook Generator Versionsinformationen in meta-global.yaml speichern  
**damit** generierte Handbücher die korrekte Generator-Version referenzieren.

#### Acceptance Criteria

**WHEN** meta-global.yaml is created  
**THEN** it **SHALL** contain:
```yaml
source: "HandBook Generator"
version: "[Handbook Generator version number]"
```

**WHEN** meta-global.yaml is missing  
**THEN** the system **SHALL** use default values:
- source: "HandBook Generator"
- version: "1.0.0"

**WHEN** templates reference `{{ meta-global.source }}` or `{{ meta-global.version }}`  
**THEN** they **SHALL** be replaced with values from meta-global.yaml

### 4. Organization Metadata (meta-organisation.yaml)

**Als** Organization Administrator  
**möchte ich** Organisationsinformationen in meta-organisation.yaml pflegen  
**damit** alle Handbücher konsistente Organisationsdaten verwenden.

#### Acceptance Criteria

**WHEN** meta-organisation.yaml is created  
**THEN** it **SHALL** contain:
```yaml
name: "AdminsEnd Ltd."
address: "Endless Lane 42, DE-35813 LandsEnd"
web: "https://www.adminsend.de"
phone: "+49 2323 555 4242"
revision: 0
```

**WHEN** meta-organisation.yaml is missing  
**THEN** the system **SHALL** use default values:
- name: "[TODO]"
- address: "[TODO]"
- web: "[TODO]"
- phone: "[TODO]"
- revision: 0

**WHEN** templates reference `{{ meta-organisation.name }}` or other organization fields  
**THEN** they **SHALL** be replaced with values from meta-organisation.yaml

**WHEN** revision is incremented  
**THEN** it **SHALL** be a manual process (not automated)

### 5. Organization Roles Metadata (meta-organisation-roles.yaml)

**Als** HR Administrator  
**möchte ich** Rolleninformationen in meta-organisation-roles.yaml verwalten  
**damit** Personaländerungen zentral gepflegt werden können.

#### Acceptance Criteria

**WHEN** meta-organisation-roles.yaml is created  
**THEN** it **SHALL** contain all required roles:
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

**WHEN** meta-organisation-roles.yaml is missing  
**THEN** the system **SHALL** use "[TODO]" as default for all roles

**WHEN** templates reference `{{ meta-organisation-roles.role_CEO }}` or other role fields  
**THEN** they **SHALL** be replaced with values from meta-organisation-roles.yaml

**WHEN** role names are defined  
**THEN** they **SHALL** use English identifiers (role_CEO, not rolle_CEO)

### 6. Handbook-Specific Metadata (meta-handbook.yaml)

**Als** Handbook Author  
**möchte ich** handbuchspezifische Metadaten in meta-handbook.yaml im Handbuch-Verzeichnis pflegen  
**damit** jedes Handbuch eigene Versionierung und Verantwortlichkeiten hat.

#### Acceptance Criteria

**WHEN** meta-handbook.yaml is created in a handbook directory  
**THEN** it **SHALL** contain:
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

**WHEN** maintainer is not specified  
**THEN** it **SHALL** default to the author value

**WHEN** revision is changed  
**THEN** it **SHALL** be a manual process

**WHEN** templates reference `{{ meta-handbook.author }}` or other handbook fields  
**THEN** they **SHALL** be replaced with values from the handbook's meta-handbook.yaml

**WHEN** meta-handbook.yaml is missing for a handbook  
**THEN** the system **SHALL** use default "[TODO]" values and warn the user

### 7. Unified English Placeholders

**Als** Template Developer  
**möchte ich** einheitliche englische Platzhalter in allen Templates  
**damit** Templates sprachunabhängig sind und einfacher zu warten sind.

#### Acceptance Criteria

**WHEN** templates are created or updated  
**THEN** all placeholders **SHALL** use English identifiers

**WHEN** placeholders reference metadata  
**THEN** they **SHALL** follow the pattern: `{{ source.field }}`  
where source is one of: meta-global, meta-organisation, meta-organisation-roles, meta-handbook

**WHEN** German templates use placeholders  
**THEN** they **SHALL** use the same English placeholders as English templates

**WHEN** placeholders are replaced  
**THEN** the replacement values **SHALL** be in the appropriate language for the template

**WHEN** existing German placeholders are found (e.g., `{{ meta.organisation.name }}`)  
**THEN** they **SHALL** be migrated to new format (e.g., `{{ meta-organisation.name }}`)

### 8. Standardized Template Document Header

**Als** Template User  
**möchte ich** einen standardisierten Dokumenten-Header in jedem Template  
**damit** alle Dokumente konsistente Metadaten anzeigen.

#### Acceptance Criteria

**WHEN** a template file is created or updated  
**THEN** it **SHALL** include a document header with the following structure:
```markdown
**Dokument-ID:** [context-specific ID, e.g., BCM-0020]
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
```

**WHEN** the template is in English  
**THEN** the header labels **SHALL** be in English:
```markdown
**Document-ID:** [context-specific ID]
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
```

**WHEN** existing templates have version information at the end  
**THEN** it **SHALL** be removed (version info is now in the header)

**WHEN** Document-ID is specified  
**THEN** it **SHALL** be context-specific (e.g., BCM-0020 for BCM handbook template 20)

**WHEN** Revision is displayed  
**THEN** it **SHALL** default to 0 and be manually incremented

### 9. Validation and Error Handling

**Als** System  
**möchte ich** Konfigurationsdateien validieren  
**damit** Fehler frühzeitig erkannt werden.

#### Acceptance Criteria

**WHEN** configuration files are loaded  
**THEN** the system **SHALL** validate:
- YAML syntax is correct
- Required fields are present
- Field values match expected types
- File references are valid

**WHEN** validation fails  
**THEN** the system **SHALL**:
- Report specific error with file name and line number
- Indicate which field is missing or invalid
- Suggest corrective action
- Use default values where possible

**WHEN** circular references are detected  
**THEN** the system **SHALL** report an error and halt

**WHEN** [TODO] values are found during generation  
**THEN** the system **SHALL** warn but continue generation

### 10. Documentation and Examples

**Als** New User  
**möchte ich** Beispielkonfigurationen und Dokumentation  
**damit** ich das System schnell einrichten kann.

#### Acceptance Criteria

**WHEN** the system is installed  
**THEN** it **SHALL** provide example files:
- config.example.yaml
- meta-global.example.yaml
- meta-organisation.example.yaml
- meta-organisation-roles.example.yaml
- meta-handbook.example.yaml

**WHEN** example files are provided  
**THEN** they **SHALL** include:
- Complete structure with all fields
- Inline comments explaining each field
- Realistic example values
- References to documentation

**WHEN** documentation is created  
**THEN** it **SHALL** include:
- Migration guide from old to new format
- Placeholder reference guide
- Configuration file reference
- Template header specification
- Troubleshooting guide

## Non-Functional Requirements

### Performance
- Configuration loading **SHALL** complete within 1 second for typical setups
- Template processing **SHALL NOT** be significantly slower than current implementation

### Maintainability
- Configuration structure **SHALL** be extensible for future metadata fields
- Placeholder format **SHALL** support nested structures (e.g., `{{ meta-organisation.address.street }}`)

### Usability
- Error messages **SHALL** be clear and actionable
- Default values **SHALL** allow system to function without full configuration
- Migration process **SHALL** be automated where possible

### Compatibility
- All existing templates **SHALL** be updated to new format
- Test suite **SHALL** be updated to validate new structure

## Out of Scope

- Migration from old configuration format (users must manually create new structure)
- Backward compatibility with old placeholder format
- Automatic translation of placeholder values between languages
- GUI for configuration management
- Real-time synchronization with external data sources
- Automatic revision incrementing
- Version control integration for configuration files

## Dependencies

- YAML parsing library (PyYAML)
- Existing template processing system
- Existing metadata loading infrastructure

## Success Criteria

1. All configuration files successfully separated into logical components
2. All templates updated with standardized headers and English placeholders
3. All existing tests pass with new configuration structure
4. Documentation complete and accurate
5. Example configuration files provided for all new formats
