# Document History Standardization Guide

## Overview

This guide explains the standardized document history section that has been added to all template files in the handbook generator system. The document history section provides a consistent way to track changes to template files across all compliance frameworks and languages.

## Purpose

The document history section serves several important purposes:

1. **Change Tracking**: Provides a clear audit trail of all modifications made to template files
2. **Version Management**: Links template changes to version numbers for easy reference
3. **Accountability**: Records who made changes and when they were made
4. **Compliance**: Supports regulatory requirements for document control and traceability
5. **Collaboration**: Helps teams understand the evolution of templates over time

## Standard Format

### German Templates (Dokumenthistorie)

All German-language template files include a document history section with the following format:

```markdown
## Dokumenthistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
```

**Column Headers:**
- **Version**: Version number of the template (e.g., 0.1, 1.0, 1.1)
- **Datum**: Date of the change (German for "Date")
- **Autor**: Person who made the change (German for "Author")
- **Änderungen**: Description of changes made (German for "Changes")

### English Templates (Document History)

All English-language template files include a document history section with the following format:

```markdown
## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
```

**Column Headers:**
- **Version**: Version number of the template (e.g., 0.1, 1.0, 1.1)
- **Date**: Date of the change
- **Author**: Person who made the change
- **Changes**: Description of changes made

## Initial Version

All templates are initialized with version **0.1** to indicate the initial template creation. This follows a semantic versioning approach where:

- **0.x**: Initial template development and refinement
- **1.x**: First stable release and minor updates
- **2.x**: Major structural changes or rewrites

## Placeholder Usage

The document history section uses placeholders that are automatically replaced during handbook generation:

- `{{ meta.document.last_updated }}`: Replaced with the document's last update date from metadata
- `{{ meta.defaults.author }}`: Replaced with the default author name from metadata configuration

These placeholders ensure that the document history reflects the actual metadata values configured for each handbook instance.

## Location in Templates

The document history section is placed at the **end of each template file**, after all content sections. This ensures:

1. Content remains the primary focus when viewing templates
2. History information is easily accessible for reference
3. Consistent placement across all templates

A blank line is added before the section for improved readability.

## Examples

### Example 1: GDPR Policy Template (German)

```markdown
# Datenschutzrichtlinie

## 1. Zweck

Diese Richtlinie definiert die Datenschutzanforderungen...

## 2. Geltungsbereich

Diese Richtlinie gilt für...

## 3. Verantwortlichkeiten

Der Datenschutzbeauftragte ist verantwortlich für...

## Dokumenthistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
```

### Example 2: ISO 9001 Procedure Template (English)

```markdown
# Quality Management Procedure

## 1. Purpose

This procedure defines the quality management requirements...

## 2. Scope

This procedure applies to...

## 3. Responsibilities

The Quality Manager is responsible for...

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
```

### Example 3: Updated Template with Multiple Versions (German)

```markdown
# Incident Response Plan

## 1. Zweck

Dieser Plan definiert die Vorgehensweise bei Sicherheitsvorfällen...

## Dokumenthistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.1 | 2026-02-01 | Max Mustermann | Eskalationsprozess aktualisiert |
| 1.0 | 2025-12-15 | Max Mustermann | Erste stabile Version |
| 0.2 | 2025-11-20 | Max Mustermann | Rollen und Verantwortlichkeiten hinzugefügt |
| 0.1 | 2025-11-01 | Max Mustermann | Initiale Erstellung |
```

## Adding Document History to Custom Templates

If you create custom templates or modify existing ones, follow these steps to add a standardized document history section:

### Step 1: Determine the Language

Identify whether your template is in German (de) or English (en) based on:
- The template directory structure (templates/de/ or templates/en/)
- The content language of the template

### Step 2: Add the Section Header

Add the appropriate section header at the end of your template file:

**For German templates:**
```markdown
## Dokumenthistorie
```

**For English templates:**
```markdown
## Document History
```

### Step 3: Add the Table

Add the table with appropriate column headers and initial row:

**For German templates:**
```markdown
| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
```

**For English templates:**
```markdown
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
```

### Step 4: Ensure Proper Spacing

Add a blank line before the document history section to separate it from the preceding content:

```markdown
... (previous content)

## Dokumenthistorie

| Version | Datum | Autor | Änderungen |
...
```

### Step 5: Update Version Numbers

When making changes to your template, add new rows to the table:

1. Insert new rows at the **top** of the table (after the header row)
2. Increment the version number appropriately
3. Use actual dates instead of placeholders for updates
4. Provide clear, concise descriptions of changes

**Example:**
```markdown
| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.1 | 2026-02-10 | Jane Doe | Added new compliance requirements |
| 1.0 | 2026-01-15 | Jane Doe | First stable release |
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
```

## Validation

The handbook generator system includes validation to ensure document history sections are properly formatted:

### Validation Checks

1. **Presence Check**: Verifies that all template files contain a document history section
2. **Format Check**: Validates the table structure and column headers
3. **Language Check**: Ensures German templates use German headers and English templates use English headers
4. **Initial Version Check**: Confirms the presence of version 0.1 with initial creation entry

### Running Validation

To validate document history sections across all templates:

```bash
python helpers/validate_metadata.py --all
```

To validate a specific framework:

```bash
python helpers/validate_metadata.py --framework gdpr
```

### Validation Output

The validation tool will report:
- Templates missing document history sections
- Templates with incorrect table format
- Templates with mismatched language headers
- Overall compliance statistics

## Best Practices

### Version Numbering

1. **Start with 0.1**: All new templates begin with version 0.1
2. **Increment Minor Versions**: Use 0.2, 0.3, etc. for development changes
3. **First Stable Release**: Use 1.0 for the first production-ready version
4. **Minor Updates**: Use 1.1, 1.2, etc. for small changes and additions
5. **Major Changes**: Use 2.0, 3.0, etc. for significant restructuring

### Change Descriptions

1. **Be Specific**: Clearly describe what changed (e.g., "Added section 4.2 on data retention")
2. **Be Concise**: Keep descriptions brief but informative
3. **Use Action Verbs**: Start with verbs like "Added", "Updated", "Removed", "Corrected"
4. **Reference Sections**: Mention specific sections or requirements when relevant

### Date Format

1. **Use ISO Format**: YYYY-MM-DD (e.g., 2026-02-10)
2. **Be Consistent**: Use the same date format throughout the table
3. **Use Placeholders Initially**: Keep `{{ meta.document.last_updated }}` for version 0.1
4. **Use Actual Dates for Updates**: Replace placeholders with real dates when making changes

### Author Information

1. **Use Full Names**: Provide complete names for accountability
2. **Be Consistent**: Use the same name format throughout
3. **Use Placeholders Initially**: Keep `{{ meta.defaults.author }}` for version 0.1
4. **Use Actual Names for Updates**: Replace placeholders with real names when making changes

## Integration with Metadata

The document history section complements the metadata system:

### Metadata Fields

- **template_version**: Tracks the raw template structure version (e.g., "1.0")
- **revision**: Tracks individual handbook customization (e.g., "0")
- **Document History**: Tracks content changes within the template

### Relationship

```
Template Version (metadata) → Overall template structure changes
    ↓
Document History (in template) → Specific content changes
    ↓
Revision (metadata) → Individual handbook customizations
```

### Example Workflow

1. **Initial Template Creation**
   - template_version: "1.0"
   - revision: "0"
   - Document History: Version 0.1 - Initial Creation

2. **Content Update**
   - template_version: "1.0" (unchanged)
   - revision: "0" (unchanged)
   - Document History: Version 1.0 - First stable release

3. **Template Structure Change**
   - template_version: "1.1" (incremented)
   - revision: "0" (unchanged)
   - Document History: Version 1.1 - Updated section structure

4. **Individual Handbook Customization**
   - template_version: "1.1" (unchanged)
   - revision: "1" (incremented)
   - Document History: Version 1.1 - Customized for specific department

## Automated Tools

### Adding Document History

Use the metadata standardizer tool to automatically add document history sections:

```python
from src.metadata_standardizer import MetadataStandardizer

standardizer = MetadataStandardizer('templates/')
standardizer.add_document_history_to_all_templates()
```

### Validation

Use the validation script to check document history compliance:

```bash
# Validate all frameworks
python helpers/validate_metadata.py --all

# Validate specific framework
python helpers/validate_metadata.py --framework iso-9001

# Generate detailed report
python helpers/validate_metadata.py --all --report validation_report.json
```

## Troubleshooting

### Common Issues

#### Issue 1: Missing Document History Section

**Symptom**: Validation reports missing document history

**Solution**: Add the section manually following the steps in "Adding Document History to Custom Templates"

#### Issue 2: Incorrect Table Format

**Symptom**: Validation reports incorrect table structure

**Solution**: Ensure the table has exactly 4 columns with proper markdown formatting:
```markdown
| Column1 | Column2 | Column3 | Column4 |
|---------|---------|---------|---------|
| Value1  | Value2  | Value3  | Value4  |
```

#### Issue 3: Language Mismatch

**Symptom**: German template has English headers or vice versa

**Solution**: Update the headers to match the template language:
- German: `| Version | Datum | Autor | Änderungen |`
- English: `| Version | Date | Author | Changes |`

#### Issue 4: Placeholders Not Replaced

**Symptom**: Generated handbook shows `{{ meta.document.last_updated }}` instead of actual date

**Solution**: Ensure your metadata configuration includes:
```yaml
document:
  last_updated: "2026-02-10"
defaults:
  author: "Your Name"
```

## Framework Coverage

Document history sections have been added to all templates across these frameworks:

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

Both German (de) and English (en) variants are supported for all frameworks.

## Related Documentation

- **Metadata Standardization Guide**: See `docs/METADATA_EXAMPLES.md` for metadata structure
- **Migration Guide**: See `docs/MIGRATION_GUIDE.md` for upgrading existing handbooks
- **Validation Guide**: See `docs/METADATA_VALIDATION_GUIDE.md` for validation details
- **Template Version Tracking**: See README.md for template_version and revision fields

## Support

For questions or issues related to document history standardization:

1. Review this guide and related documentation
2. Run validation to identify specific issues
3. Check the examples provided in this guide
4. Refer to the requirements document: `.kiro/specs/template-metadata-standardization/requirements.md`

## Summary

The document history standardization provides:

- ✅ Consistent change tracking across all templates
- ✅ Bilingual support (German and English)
- ✅ Automated validation and compliance checking
- ✅ Clear guidelines for manual additions
- ✅ Integration with metadata version tracking
- ✅ Support for all 12 compliance frameworks

By following this guide, you can ensure that all templates maintain proper document history sections that support compliance, collaboration, and change management requirements.
