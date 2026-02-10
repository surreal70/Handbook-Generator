# Requirements Document: Template Metadata Standardization

## Introduction

This document specifies the requirements for standardizing metadata across all compliance framework templates in the handbook generator system. The system currently has 12 compliance frameworks (BCM, ISMS, BSI Grundschutz, IT-Operations, CIS Controls, Common Criteria, GDPR, HIPAA, ISO 9001, NIST 800-53, PCI-DSS, TSC) with varying levels of metadata completeness. This enhancement will ensure unified metadata structure, add version tracking capabilities, and reorganize service-related templates into a dedicated directory.

The standardization will enable better template lifecycle management, compatibility tracking for future migrations, and support for individual customization tracking through revision numbers.

## Glossary

- **Metadata_File**: A special template file (0000_metadata_{lang}_{framework}.md) containing handbook metadata
- **Template_Version**: Version number of the raw template structure (e.g., "1.0"), used for tracking template format changes
- **Revision_Number**: Customization tracking number (e.g., "0"), used for tracking individual handbook modifications
- **Unified_Metadata_Structure**: Standardized set of metadata fields consistent across all frameworks
- **Service_Directory**: Dedicated directory for service-related templates (service-templates and service examples)
- **Framework**: A compliance or operational standard (e.g., GDPR, ISO 9001, PCI-DSS)
- **Bilingual_Support**: Templates available in both German (de) and English (en) languages
- **Placeholder**: Variable in format {{ source.field }} that gets replaced with actual data during generation
- **Missing_Metadata**: Frameworks that lack a complete 0000_metadata file

## Requirements

### Requirement 1: Unified Metadata Structure

**User Story:** Als Compliance-Manager möchte ich eine einheitliche Metadatenstruktur über alle Handbuch-Frameworks hinweg, damit ich konsistente Dokumenteninformationen habe und die Verwaltung vereinfacht wird.

#### Acceptance Criteria

1. WHEN a metadata file is created or updated, THEN it SHALL include all required fields: document_id, owner, version, status, classification, date, organization, author, scope, valid_from, next_review
2. WHEN a metadata file is created, THEN it SHALL follow the structure of GDPR or Common Criteria metadata templates as reference
3. WHEN metadata is displayed, THEN it SHALL use consistent formatting and section organization across all frameworks
4. WHEN a framework has minimal metadata (like CIS Controls), THEN it SHALL be enhanced to include all required fields
5. WHEN metadata fields are defined, THEN they SHALL support placeholder substitution ({{ meta.field }})
6. WHEN metadata is validated, THEN missing required fields SHALL be reported as errors
7. WHEN bilingual frameworks exist, THEN both language variants SHALL have identical metadata structure
8. WHEN a metadata file is created, THEN it SHALL include a "Dokumentenzweck" (Document Purpose) section explaining the handbook's purpose

### Requirement 2: Template Version Tracking

**User Story:** Als System-Administrator möchte ich Template-Versionsnummern verfolgen, damit ich Kompatibilität und Migrationen zwischen Template-Versionen verwalten kann.

#### Acceptance Criteria

1. WHEN a metadata file is created or updated, THEN it SHALL include a "template_version" field
2. WHEN a new template is created, THEN the template_version SHALL be initialized to "1.0"
3. WHEN template structure changes occur, THEN the template_version SHALL be incremented according to semantic versioning
4. WHEN template_version is displayed, THEN it SHALL be clearly labeled as "Template-Version" in German or "Template Version" in English
5. WHEN template_version is stored, THEN it SHALL be in the format "MAJOR.MINOR" (e.g., "1.0", "1.1", "2.0")
6. WHEN validation runs, THEN it SHALL verify that template_version field exists and follows the correct format
7. WHEN comparing templates, THEN template_version SHALL enable compatibility checking for future migrations
8. WHEN template_version is documented, THEN it SHALL explain that this tracks raw template format changes (maintained with -test switch)

### Requirement 3: Revision Number Support

**User Story:** Als Handbuch-Autor möchte ich Revisionsnummern für individuelle Anpassungen verfolgen, damit ich Änderungen an meinen spezifischen Handbüchern nachvollziehen kann.

#### Acceptance Criteria

1. WHEN a metadata file is created or updated, THEN it SHALL include a "revision" field
2. WHEN a new template is created, THEN the revision SHALL be initialized to "0"
3. WHEN revision is displayed, THEN it SHALL be clearly labeled as "Revision" in both German and English
4. WHEN revision is stored, THEN it SHALL be an integer value (e.g., 0, 1, 2, 3)
5. WHEN validation runs, THEN it SHALL verify that revision field exists and is a valid integer
6. WHEN revision is documented, THEN it SHALL explain that this is for individual customization tracking (functionality to be implemented later)
7. WHEN a handbook is customized, THEN the revision number SHALL remain at 0 until customization tracking is implemented
8. WHEN metadata is displayed, THEN revision SHALL be shown separately from template_version

### Requirement 4: Missing Metadata Detection and Creation

**User Story:** Als System-Administrator möchte ich fehlende Metadaten-Dateien automatisch erkennen und erstellen, damit alle Frameworks vollständige Metadaten haben.

#### Acceptance Criteria

1. WHEN the system scans frameworks, THEN it SHALL identify all frameworks missing 0000_metadata files
2. WHEN a missing metadata file is detected, THEN it SHALL be reported with framework name and language
3. WHEN creating missing metadata, THEN it SHALL generate files for both German (de) and English (en) variants
4. WHEN creating missing metadata, THEN it SHALL use the unified metadata structure from Requirement 1
5. WHEN creating missing metadata, THEN it SHALL initialize template_version to "1.0" and revision to "0"
6. WHEN creating missing metadata, THEN it SHALL include framework-specific information (title, purpose, scope)
7. WHEN all 12 frameworks are scanned, THEN the system SHALL report which frameworks have complete metadata
8. WHEN metadata creation completes, THEN it SHALL generate a summary report of created files

### Requirement 5: Service Directory Reorganization

**User Story:** Als Repository-Maintainer möchte ich Service-bezogene Templates in einem dedizierten Verzeichnis organisieren, damit die Struktur klarer und wartbarer ist.

#### Acceptance Criteria

1. WHEN the reorganization is performed, THEN a new directory "service-directory" SHALL be created under templates/de/ and templates/en/
2. WHEN the reorganization is performed, THEN the "email-service" directory SHALL be moved into service-directory/
3. WHEN the reorganization is performed, THEN the "service-templates" directory SHALL be moved into service-directory/
4. WHEN files are moved, THEN all file contents SHALL remain unchanged
5. WHEN files are moved, THEN the directory structure SHALL be: templates/{lang}/service-directory/{email-service,service-templates}/
6. WHEN the reorganization completes, THEN the old directories SHALL be removed
7. WHEN the system references service templates, THEN it SHALL use the new paths
8. WHEN documentation is updated, THEN it SHALL reflect the new service-directory structure

### Requirement 6: Metadata Validation

**User Story:** Als Quality-Assurance-Engineer möchte ich Metadaten validieren, damit ich sicherstelle, dass alle Frameworks den Standards entsprechen.

#### Acceptance Criteria

1. WHEN validation runs, THEN it SHALL check for presence of all required metadata fields
2. WHEN validation runs, THEN it SHALL verify template_version format (MAJOR.MINOR)
3. WHEN validation runs, THEN it SHALL verify revision is a valid integer
4. WHEN validation runs, THEN it SHALL check bilingual consistency (matching fields in de/en)
5. WHEN validation runs, THEN it SHALL verify placeholder syntax is correct
6. WHEN validation detects errors, THEN it SHALL generate a detailed report with framework, file, and error description
7. WHEN validation completes, THEN it SHALL report success rate (X of Y frameworks valid)
8. WHEN validation runs, THEN it SHALL be executable via command line (e.g., validate_metadata.py)

### Requirement 7: Backward Compatibility

**User Story:** Als Existing-User möchte ich, dass bestehende Handbücher weiterhin funktionieren, damit meine Arbeit nicht unterbrochen wird.

#### Acceptance Criteria

1. WHEN metadata is enhanced, THEN existing handbook generation SHALL continue to work
2. WHEN new fields are added, THEN they SHALL have sensible defaults if not provided
3. WHEN old metadata files are encountered, THEN they SHALL be processed without errors
4. WHEN placeholders are missing data, THEN they SHALL be preserved in output (not cause errors)
5. WHEN the system loads templates, THEN it SHALL handle both old and new metadata formats
6. WHEN migration is needed, THEN clear migration instructions SHALL be provided
7. WHEN validation runs on old metadata, THEN it SHALL provide warnings (not errors) for missing new fields
8. WHEN documentation is updated, THEN it SHALL include migration guide for existing users

### Requirement 8: Documentation Updates

**User Story:** Als Handbuch-Autor möchte ich aktualisierte Dokumentation, damit ich die neuen Metadaten-Features verstehe und nutzen kann.

#### Acceptance Criteria

1. WHEN documentation is updated, THEN it SHALL explain the unified metadata structure
2. WHEN documentation is updated, THEN it SHALL explain template_version and its purpose
3. WHEN documentation is updated, THEN it SHALL explain revision numbers and future customization tracking
4. WHEN documentation is updated, THEN it SHALL document the service-directory reorganization
5. WHEN documentation is updated, THEN it SHALL provide examples of complete metadata files
6. WHEN documentation is updated, THEN it SHALL explain how to validate metadata
7. WHEN documentation is updated, THEN it SHALL include migration guide for existing handbooks
8. WHEN documentation is updated, THEN it SHALL be available in both README.md and framework-specific docs

### Requirement 9: Standardized Document History Section

**User Story:** Als Handbuch-Autor möchte ich eine einheitliche Dokumenthistorie in allen Templates, damit Änderungen konsistent nachvollziehbar sind.

#### Acceptance Criteria

1. WHEN a template markdown file is created, THEN it SHALL include a standardized document history section
2. WHEN a document history section is created, THEN it SHALL use the format "Dokumenthistorie" (German) or "Document History" (English)
3. WHEN a document history table is created, THEN it SHALL use the column headers: "Version | Datum | Autor | Änderungen" (German) or "Version | Date | Author | Changes" (English)
4. WHEN a document history table is initialized, THEN it SHALL include one initial row with version "0.1", date "{{ meta.document.last_updated }}", author "{{ meta.defaults.author }}", and changes "Initiale Erstellung" (German) or "Initial Creation" (English)
5. WHEN validating templates, THEN the system SHALL verify that all template files contain a document history section
6. WHEN validating document history, THEN the system SHALL verify the table format matches the standard structure
7. WHEN bilingual templates exist, THEN both language variants SHALL have document history sections with appropriate language-specific labels
8. WHEN a document history section is missing, THEN the validation SHALL report it as a warning (not error) for backward compatibility

### Requirement 10: Metadata Role Cleanup and Reorganization

**User Story:** Als System-Administrator möchte ich duplicate Rollen entfernen und IT-Operations-Rollen korrekt organisieren, damit die Metadatenstruktur klar und wartbar ist.

#### Acceptance Criteria

1. WHEN metadata roles are validated, THEN duplicate role "datenschutzbeauftragter" SHALL be identified as redundant with "data_protection_officer"
2. WHEN metadata cleanup is performed, THEN "datenschutzbeauftragter" SHALL be removed from metadata.example.yaml
3. WHEN metadata cleanup is performed, THEN references to "datenschutzbeauftragter" SHALL be replaced with "data_protection_officer"
4. WHEN IT operations roles are reorganized, THEN "it_manager" and "sysop" SHALL be grouped under the "IT Operations Roles" section
5. WHEN role sections are organized, THEN they SHALL follow the structure: C-Level Executives, IT Operations Roles, BCM and Security Roles
6. WHEN role cleanup is documented, THEN migration notes SHALL explain the removal of "datenschutzbeauftragter"
7. WHEN templates reference removed roles, THEN they SHALL be updated to use the canonical role names
8. WHEN validation runs, THEN it SHALL check for duplicate role definitions and report them as errors

## Framework Coverage

The following 12 frameworks SHALL be standardized:

1. **BCM** (Business Continuity Management)
2. **ISMS** (Information Security Management System)
3. **BSI Grundschutz** (German IT Security Standard)
4. **IT-Operation** (IT Operations Management)
5. **CIS Controls** (Center for Internet Security Controls)
6. **Common Criteria** (ISO/IEC 15408)
7. **GDPR** (General Data Protection Regulation)
8. **HIPAA** (Health Insurance Portability and Accountability Act)
9. **ISO 9001** (Quality Management System)
10. **NIST 800-53** (Security and Privacy Controls)
11. **PCI-DSS** (Payment Card Industry Data Security Standard)
12. **TSC** (Trust Services Criteria / SOC 2)

## Success Criteria

The implementation SHALL be considered successful when:

1. All 12 frameworks have complete metadata files with unified structure
2. All metadata files include template_version (1.0) and revision (0) fields
3. All template markdown files include standardized document history sections
4. Duplicate role "datenschutzbeauftragter" is removed from metadata.example.yaml
5. IT operations roles (it_manager, sysop) are properly organized in the IT Operations Roles section
6. Service-related templates are organized in service-directory/
7. Metadata validation passes for all frameworks
8. Existing handbook generation continues to work without errors
9. Documentation is updated with new metadata features
10. All tests pass (unit tests and property-based tests)
11. Migration guide is available for existing users
