# Template Header Specification

## Overview

All template files in the Handbook Generator must include a standardized document header at the beginning of the file. This header provides essential metadata about the document and ensures consistency across all handbooks and languages.

## Purpose

The standardized document header serves multiple purposes:

1. **Identification** - Uniquely identifies each document within a handbook
2. **Ownership** - Clearly defines responsibility and approval chains
3. **Version Control** - Tracks document revisions and update dates
4. **Classification** - Indicates security classification and status
5. **Consistency** - Ensures uniform metadata display across all documents

## Header Format

### Structure

The document header consists of:

1. **Document Title** (H1 heading)
2. **Metadata Fields** (bold key-value pairs)
3. **Horizontal Separator** (three dashes)

### Basic Template

```markdown
# [Document Title]

**[Field Label]:** [Value or Placeholder]
**[Field Label]:** [Value or Placeholder]
...

---
```

## Required Fields

All template headers MUST include these fields in this order:

1. **Document-ID** (or **Dokument-ID** in German)
2. **Organisation**
3. **Owner**
4. **Approved by** (or **Genehmigt durch** in German)
5. **Revision**
6. **Author**
7. **Status**
8. **Classification** (or **Klassifizierung** in German)
9. **Last Update** (or **Letzte Aktualisierung** in German)

## Language-Specific Variations

### German Templates (templates/de/)

German templates use German labels for the header fields:

```markdown
# [Dokumenttitel]

**Dokument-ID:** [ID]
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---
```

### English Templates (templates/en/)

English templates use English labels for the header fields:

```markdown
# [Document Title]

**Document-ID:** [ID]
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---
```

## Field Specifications

### Document-ID / Dokument-ID

- **Type:** Static text or placeholder
- **Format:** Framework-specific or numeric
- **Examples:**
  - `0010` - Simple numeric ID
  - `BCM-0020` - Framework prefix with numeric ID
  - `[FRAMEWORK]-0030` - Placeholder for framework name
- **Purpose:** Uniquely identifies the document within the handbook
- **Notes:** 
  - Use consistent numbering scheme within each handbook
  - Consider using leading zeros for proper sorting (0010, 0020, 0030)
  - Framework prefix helps identify document source

### Organisation

- **Type:** Placeholder
- **Value:** `{{ meta-organisation.name }}`
- **Purpose:** Identifies the organization that owns the handbook
- **Example Output:** "AdminsEnd Ltd.", "Acme Corporation"
- **Notes:** Always uses the same placeholder across all templates

### Owner

- **Type:** Placeholder
- **Value:** `{{ meta-handbook.owner }}`
- **Purpose:** Identifies the person or role with ultimate responsibility
- **Example Output:** "Chief Information Security Officer", "IT Manager"
- **Notes:** Handbook-specific, can vary between handbooks

### Approved by / Genehmigt durch

- **Type:** Placeholder
- **Value:** `{{ meta-handbook.approver }}`
- **Purpose:** Identifies who approved the document
- **Example Output:** "Chief Information Officer", "Management Board"
- **Notes:** Handbook-specific, typically a senior role

### Revision

- **Type:** Placeholder
- **Value:** `{{ meta-handbook.revision }}`
- **Purpose:** Tracks document version number
- **Example Output:** 0, 1, 2, 3
- **Notes:** Manual revision counter, not automatically incremented

### Author

- **Type:** Placeholder
- **Value:** `{{ meta-handbook.author }}`
- **Purpose:** Identifies the primary author of the handbook
- **Example Output:** "Jane Smith", "IT Department"
- **Notes:** Handbook-specific, can be person or team name

### Status

- **Type:** Placeholder
- **Value:** `{{ meta-handbook.status }}`
- **Purpose:** Indicates current lifecycle status
- **Example Output:** "Draft", "In Review", "Approved", "Published"
- **Notes:** Handbook-specific, reflects document maturity

### Classification / Klassifizierung

- **Type:** Placeholder
- **Value:** `{{ meta-handbook.classification }}`
- **Purpose:** Indicates security classification level
- **Example Output:** "Public", "Internal", "Confidential", "Restricted"
- **Notes:** Handbook-specific, determines access control

### Last Update / Letzte Aktualisierung

- **Type:** Placeholder
- **Value:** `{{ meta-handbook.modifydate }}`
- **Purpose:** Shows when the document was last modified
- **Example Output:** "2024-03-20"
- **Notes:** Should be updated whenever document changes

## Complete Examples

### German GDPR Template

```markdown
# Geltungsbereich und Anwendungsbereich

**Dokument-ID:** 0010
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---
```

### English ISMS Template

```markdown
# Information Security Policy

**Document-ID:** ISMS-0010
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---
```

### German BCM Template with Framework Placeholder

```markdown
# Business Impact Analyse

**Dokument-ID:** [FRAMEWORK]-0020
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---
```

### English IT Operations Template

```markdown
# Change Management Process

**Document-ID:** IT-OPS-0050
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---
```

## Label Translation Reference

For consistency, use these exact translations:

| English Label | German Label |
|---------------|--------------|
| Document-ID | Dokument-ID |
| Organisation | Organisation |
| Owner | Owner |
| Approved by | Genehmigt durch |
| Revision | Revision |
| Author | Author |
| Status | Status |
| Classification | Klassifizierung |
| Last Update | Letzte Aktualisierung |

**Note:** Some labels remain in English even in German templates (Organisation, Owner, Revision, Author, Status) as they are commonly understood technical terms.

## Formatting Rules

### Bold Formatting

- All field labels MUST be bold: `**Label:**`
- Values and placeholders are NOT bold
- Maintain consistent spacing: `**Label:** value`

### Spacing

- One blank line after the document title
- No blank lines between metadata fields
- One blank line before the horizontal separator
- One blank line after the horizontal separator

### Horizontal Separator

- Use exactly three dashes: `---`
- Place on its own line
- Separates header from document content

### Example with Spacing

```markdown
# Document Title
[blank line]
**Document-ID:** 0010
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
[blank line]
---
[blank line]
[document content starts here]
```

## Document-ID Conventions

### Numeric IDs

Use for simple sequential numbering:

```
0010, 0020, 0030, 0040, ...
```

**Advantages:**
- Simple and clean
- Easy to maintain
- Good for sorting

**Use When:**
- Single handbook or framework
- No need for framework identification

### Framework-Prefixed IDs

Use when framework identification is needed:

```
BCM-0010, BCM-0020, BCM-0030
ISMS-0010, ISMS-0020, ISMS-0030
GDPR-0010, GDPR-0020, GDPR-0030
```

**Advantages:**
- Clear framework identification
- Useful for cross-references
- Prevents ID conflicts

**Use When:**
- Multiple frameworks in same system
- Cross-framework references needed
- Framework identification important

### Framework Placeholder IDs

Use for generic templates:

```
[FRAMEWORK]-0010
[FRAMEWORK]-0020
[FRAMEWORK]-0030
```

**Advantages:**
- Generic and reusable
- Can be replaced during generation
- Flexible for multiple frameworks

**Use When:**
- Creating generic templates
- Framework name determined at runtime
- Maximum flexibility needed

### Special IDs

Some documents use special IDs:

- `0000` - Metadata document (handbook information)
- `9999` - Framework mapping document
- `XXXX` - Appendix or supplementary documents

## Validation Rules

Templates MUST comply with these validation rules:

### Required Elements

1. ✅ Document title (H1 heading) present
2. ✅ All nine required fields present
3. ✅ Fields in correct order
4. ✅ Horizontal separator present
5. ✅ Correct placeholders used

### Language Consistency

1. ✅ German templates use German labels
2. ✅ English templates use English labels
3. ✅ Placeholders remain in English (language-agnostic)
4. ✅ No mixed language labels

### Formatting Consistency

1. ✅ Bold formatting on labels only
2. ✅ Consistent spacing between elements
3. ✅ Proper placeholder syntax: `{{ meta-source.field }}`
4. ✅ No trailing version information at end of file

## Migration from Old Format

### Old Format (Deprecated)

Old templates may have had:
- Version information at the end of the file
- Different field order
- Missing fields
- Non-standard placeholders

### Migration Steps

1. **Add Missing Fields**
   - Ensure all nine required fields are present
   - Add any missing fields with appropriate placeholders

2. **Update Field Order**
   - Reorder fields to match specification
   - Maintain consistent order across all templates

3. **Update Placeholders**
   - Replace old placeholders with new format
   - Use `meta-handbook.*` for handbook-specific fields
   - Use `meta-organisation.*` for organization fields

4. **Remove Trailing Version Info**
   - Delete version information from end of file
   - Version info now in header only

5. **Standardize Labels**
   - Use exact labels from specification
   - Ensure language consistency (German vs English)

### Example Migration

**Before (Old Format):**
```markdown
# Document Title

**ID:** 0010
**Organization:** {{ organisation.name }}
**Author:** {{ document.author }}

[content]

---
Version: 1.0
Last Updated: 2024-01-15
```

**After (New Format):**
```markdown
# Document Title

**Document-ID:** 0010
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

[content]
```

## Best Practices

### 1. Consistent Document-ID Scheme

Choose one ID scheme and use it consistently within each handbook:
- All numeric: `0010, 0020, 0030`
- All prefixed: `BCM-0010, BCM-0020, BCM-0030`
- Don't mix schemes within a handbook

### 2. Meaningful Document-IDs

Use IDs that reflect document organization:
- `0000` - Metadata/Introduction
- `0010-0090` - Core concepts
- `0100-0900` - Main content
- `9999` - Framework mapping/Appendix

### 3. Update Dates Consistently

- Update `modifydate` whenever document changes
- Use ISO 8601 format (YYYY-MM-DD)
- Keep dates current for compliance

### 4. Appropriate Classification

- Set classification based on content sensitivity
- Review classification regularly
- Ensure classification matches access controls

### 5. Clear Ownership

- Assign specific owners, not generic roles
- Ensure owners are aware of responsibility
- Update ownership when personnel changes

### 6. Meaningful Status Values

Use standard status values:
- "Draft" - Work in progress
- "In Review" - Under review
- "Approved" - Approved but not yet published
- "Published" - Active and in use
- "Archived" - No longer active

### 7. Template Validation

Before committing templates:
- Verify all required fields present
- Check placeholder syntax
- Ensure language consistency
- Validate formatting

## Troubleshooting

### Missing Fields

**Problem:** Template missing required fields

**Solution:**
1. Compare template header with specification
2. Add missing fields in correct order
3. Use appropriate placeholders

### Wrong Language Labels

**Problem:** German template with English labels (or vice versa)

**Solution:**
1. Check template language (de/ or en/ directory)
2. Update labels to match language
3. Keep placeholders in English

### Incorrect Placeholder Syntax

**Problem:** Placeholders not replaced in output

**Solution:**
1. Verify placeholder format: `{{ meta-source.field }}`
2. Check for typos in placeholder names
3. Ensure spaces around placeholder (optional but recommended)

### Formatting Issues

**Problem:** Header doesn't render correctly

**Solution:**
1. Check bold formatting: `**Label:**`
2. Verify spacing between elements
3. Ensure horizontal separator is `---` on its own line

## Validation Checklist

Use this checklist when creating or updating templates:

- [ ] Document title (H1) present
- [ ] All nine required fields present
- [ ] Fields in correct order
- [ ] Correct language labels (German or English)
- [ ] All placeholders use correct syntax
- [ ] Placeholders use English identifiers
- [ ] Bold formatting on labels only
- [ ] Consistent spacing
- [ ] Horizontal separator present
- [ ] No trailing version information
- [ ] Document-ID follows convention
- [ ] Template in correct language directory

## See Also

- [Configuration Reference](CONFIGURATION_REFERENCE.md) - Metadata file documentation
- [Placeholder Reference](PLACEHOLDER_REFERENCE.md) - Complete placeholder list
- [Migration Guide](MIGRATION_GUIDE.md) - Migrating from old format

## Support

For questions about template headers:

1. Review this specification
2. Check example templates in templates/ directory
3. Verify placeholder syntax in Placeholder Reference
4. Use validation checklist above
5. Check for validation errors during generation
