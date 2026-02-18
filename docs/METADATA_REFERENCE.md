# Metadata Reference Guide

## Overview

This guide provides a comprehensive reference for the unified metadata structure used across all handbook frameworks in the Handbook Generator. Every framework includes standardized metadata files that ensure consistent documentation information and enable proper version tracking.

## Table of Contents

- [Metadata File Structure](#metadata-file-structure)
- [Required Fields](#required-fields)
- [Field Descriptions](#field-descriptions)
- [Placeholder Syntax](#placeholder-syntax)
- [Version Tracking](#version-tracking)
- [Bilingual Consistency](#bilingual-consistency)
- [Examples](#examples)
- [Related Documentation](#related-documentation)

## Metadata File Structure

Each framework contains a metadata file following this naming convention:

```
0000_metadata_{language}_{framework}.md
```

**Examples:**
- `0000_metadata_de_bcm.md` - German BCM metadata
- `0000_metadata_en_isms.md` - English ISMS metadata
- `0000_metadata_de_gdpr.md` - German GDPR metadata

## Required Fields

All metadata files must contain standardized fields using placeholder syntax. The fields are populated from the `meta-handbook.yaml` configuration file.

| Field | Placeholder | Description |
|-------|-------------|-------------|
| Document ID | Static "0000" | Unique document identifier for metadata |
| Date | `{{ meta-handbook.creationdate }}` | Document creation date |
| Owner | `{{ meta-handbook.owner }}` | Document owner/responsible person |
| Revision | `{{ meta-handbook.revision }}` | Document revision number |
| Status | `{{ meta-handbook.status }}` | Document status (Draft, Active, etc.) |
| Classification | `{{ meta-handbook.classification }}` | Security classification level |
| Last Update | `{{ meta-handbook.modifydate }}` | Last modification date |
| Template Version | `{{ meta-handbook.templateset_version }}` | Template format version |
| Handbook Title | `{{ meta-handbook.longname }}` | Full handbook title |
| Handbook Short | `{{ meta-handbook.shortname }}` | Short handbook identifier |
| Organization | `{{ meta-organisation.name }}` | Organization name |
| Author | `{{ meta-handbook.author }}` | Document author |
| Scope | `{{ meta-handbook.scope }}` | Document scope/applicability |
| Valid From | `{{ meta-handbook.valid_from }}` | Effective date |
| Next Review | `{{ meta-handbook.next_review }}` | Scheduled review date |
| Approver | `{{ meta-handbook.approver }}` | Approval authority |

## Field Descriptions

### Document Identification

**document_id**
- Static identifier for the metadata document
- Always "0000" for metadata files
- Used for document ordering and reference

**templateset_version**
- Tracks the template format version
- Placeholder: `{{ meta-handbook.templateset_version }}`
- Incremented when template structure changes
- Enables compatibility tracking for migrations

**revision**
- Tracks document revision changes
- Placeholder: `{{ meta-handbook.revision }}`
- Incremented when document is updated
- Enables tracking of document modifications

### Dynamic Fields (Placeholders)

The following fields use placeholder syntax and are populated from `meta-handbook.yaml`:

**creationdate**
- Document creation date
- Placeholder: `{{ meta-handbook.creationdate }}`
- Format: ISO 8601 (YYYY-MM-DD) recommended

**modifydate**
- Last modification date
- Placeholder: `{{ meta-handbook.modifydate }}`
- Format: ISO 8601 (YYYY-MM-DD) recommended
- Updated when document changes

**owner**
- Document owner or responsible person
- Placeholder: `{{ meta-handbook.owner }}`
- Source: `meta-handbook.yaml`

**status**
- Document lifecycle status
- Placeholder: `{{ meta-handbook.status }}`
- Common values: "Draft", "In Review", "Approved", "Active"

**classification**
- Security classification level
- Placeholder: `{{ meta-handbook.classification }}`
- Common values: "Public", "Internal", "Confidential", "Restricted"

**longname**
- Full handbook title
- Placeholder: `{{ meta-handbook.longname }}`
- Complete descriptive name of the handbook

**shortname**
- Short handbook identifier
- Placeholder: `{{ meta-handbook.shortname }}`
- Abbreviated name or acronym

**author**
- Document author or creator
- Placeholder: `{{ meta-handbook.author }}`
- Can be individual or team name

**scope**
- Document scope or applicability
- Placeholder: `{{ meta-handbook.scope }}`
- Defines where the document applies

**valid_from**
- Date when document becomes effective
- Placeholder: `{{ meta-handbook.valid_from }}`
- Format: ISO 8601 (YYYY-MM-DD) recommended

**next_review**
- Scheduled next review date
- Placeholder: `{{ meta-handbook.next_review }}`
- Ensures regular document updates

**approver**
- Approval authority
- Placeholder: `{{ meta-handbook.approver }}`
- Person or role who approved the document

### Organization Fields

**organization name**
- Organization or company name
- Placeholder: `{{ meta-organisation.name }}`
- Source: `meta-organisation.yaml`
- Used in headers, footers, and document identification

## Placeholder Syntax

All dynamic fields use the standardized placeholder syntax:

```
{{ source.field }}
```

**Components:**
- `{{` - Opening delimiter
- `source` - Data source identifier (e.g., `meta`, `netbox`, `organisation`)
- `.` - Separator
- `field` - Field name within the source
- `}}` - Closing delimiter

**Examples:**
```markdown
{{ meta-handbook.owner }}
{{ meta-handbook.status }}
{{ meta-handbook.longname }}
{{ meta-organisation.name }}
{{ netbox.site.name }}
```

For complete placeholder documentation, see [PLACEHOLDER_REFERENCE.md](PLACEHOLDER_REFERENCE.md).

## Version Tracking

### Template Version

The `templateset_version` field tracks the template format version:

**Format:** Version string (e.g., "1.0", "2.1")
- Incremented when template structure changes
- Enables compatibility checking during migrations
- Identifies which templates need updates
- Supports automated migration tools

**Purpose:**
- Enables compatibility checking during migrations
- Identifies which templates need updates
- Supports automated migration tools

### Revision Number

The `revision` field tracks document changes:

**Purpose:**
- Tracks document modifications
- Distinguishes original from modified documents
- Helps identify which documents need review during updates

**Workflow:**
1. Initial document: First revision
2. First update: Increment revision
3. Subsequent updates: Continue incrementing

## Bilingual Consistency

All frameworks must maintain bilingual consistency between German (de) and English (en) versions:

**Requirements:**
- Same field structure in both languages
- Same placeholder usage
- Same template_version and revision values
- Translated content but identical structure

**Validation:**
The metadata validation system checks for:
- Matching field presence in both languages
- Consistent placeholder locations
- Identical version numbers

## Examples

### Complete Metadata File Example (German)

```markdown
# BCM Handbuch - Metadaten

**Dokument-ID:** 0000  
**Datum:** {{ meta-handbook.creationdate }}  
**Owner:** {{ meta-handbook.owner }}  
**Revision:** {{ meta-handbook.revision }}  
**Status:** {{ meta-handbook.status }}  
**Klassifizierung:** {{ meta-handbook.classification }}  
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}  
**Template-Version:** {{ meta-handbook.templateset_version }}  

---

## Handbuch-Informationen

**Handbuch-Titel:** {{ meta-handbook.longname }}
**Handbuch-Short:** {{ meta-handbook.shortname }}
**Organisation:** {{ meta-organisation.name }}  
**Autor:** {{ meta-handbook.author }}  
**Geltungsbereich:** {{ meta-handbook.scope }}  
**Gültig ab:** {{ meta-handbook.valid_from }}  
**Nächste Überprüfung:** {{ meta-handbook.next_review }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  

---

## Dokumentenzweck

Dieses Dokument enthält die Metadaten für das BCM Handbuch.

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| 0.1 | {{ meta-handbook.creationdate }} | Handbook-Generator | Initiale Version |
```

### Complete Metadata File Example (English)

```markdown
# BCM Handbook - Metadata

**Document ID:** 0000  
**Date:** {{ meta-handbook.creationdate }}  
**Owner:** {{ meta-handbook.owner }}  
**Revision:** {{ meta-handbook.revision }}  
**Status:** {{ meta-handbook.status }}  
**Classification:** {{ meta-handbook.classification }}  
**Last Update:** {{ meta-handbook.modifydate }}  
**Template Version:** {{ meta-handbook.templateset_version }}  

---

## Handbook Information

**Handbook Title:** {{ meta-handbook.longname }}
**Handbook Short:** {{ meta-handbook.shortname }}
**Organization:** {{ meta-organisation.name }}  
**Author:** {{ meta-handbook.author }}  
**Scope:** {{ meta-handbook.scope }}  
**Valid From:** {{ meta-handbook.valid_from }}  
**Next Review:** {{ meta-handbook.next_review }}  
**Approved By:** {{ meta-handbook.approver }}  

---

## Document Purpose

This document contains the metadata for the BCM Handbook.

## Change History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | {{ meta-handbook.creationdate }} | Handbook-Generator | Initial version |
```

## Related Documentation

- **[PLACEHOLDER_REFERENCE.md](PLACEHOLDER_REFERENCE.md)** - Complete placeholder syntax and usage guide
- **[TEMPLATE_HEADER_SPECIFICATION.md](TEMPLATE_HEADER_SPECIFICATION.md)** - Template header structure and requirements
- **[METADATA_VALIDATION_GUIDE.md](METADATA_VALIDATION_GUIDE.md)** - Validation procedures and tools
- **[METADATA_EXAMPLES.md](METADATA_EXAMPLES.md)** - Additional metadata examples for all frameworks

## Tools and Helpers

### Metadata Validation

Validate metadata files using the validation script:

```bash
# Validate all frameworks
python helpers/validate_metadata.py --all

# Validate specific framework
python helpers/validate_metadata.py --framework gdpr

# Validate specific language
python helpers/validate_metadata.py --language de

# Generate JSON report
python helpers/validate_metadata.py --all --report metadata_report.json
```

### Placeholder Matrix Generator

Generate a comprehensive overview of all placeholders used across templates:

```bash
# Generate placeholder matrix
python helpers/generate_placeholder_matrix.py

# Output: placeholder_matrix.html
```

The placeholder matrix provides:
- Complete list of all placeholders used
- Which templates use which placeholders
- Placeholder frequency and distribution
- Visual overview for documentation and validation

## Best Practices

1. **Always maintain bilingual consistency** - Changes to German metadata must be reflected in English metadata
2. **Use semantic versioning** - Follow MAJOR.MINOR format for template_version
3. **Track customizations** - Increment revision number when modifying templates
4. **Validate regularly** - Run validation after any metadata changes
5. **Document changes** - Update change history when incrementing revision
6. **Use placeholders** - Never hardcode values that should be dynamic
7. **Follow naming conventions** - Use standard field names across all frameworks

## Troubleshooting

### Common Issues

**Missing Required Fields**
- Error: "Missing required field: {field_name}"
- Solution: Add the missing field to the metadata file

**Invalid Template Version Format**
- Error: "Invalid template_version format"
- Solution: Use MAJOR.MINOR format (e.g., "1.0", "2.1")

**Bilingual Inconsistency**
- Error: "Field structure mismatch between de and en"
- Solution: Ensure both language versions have identical field structure

**Invalid Placeholder Syntax**
- Error: "Invalid placeholder syntax"
- Solution: Use correct format: `{{ source.field }}`

### Getting Help

For additional support:
1. Check the validation output for specific error messages
2. Review the METADATA_EXAMPLES.md for correct formatting
3. Run the validation script with verbose output
4. Consult the METADATA_VALIDATION_GUIDE.md for detailed validation procedures

---

**Author**: Andreas Huemmer [andreas.huemmer@adminsend.de]  
**Copyright**: © 2025, 2026
