# Framework-Specific README Updates

## Overview

This document provides the standardized metadata section that should be added to all framework README.md files. This ensures consistent documentation of the metadata standardization across all 12 compliance frameworks.

## Standard Metadata Section (German)

Add this section to all German framework README.md files (after the template organization section, before "Nutzungshinweise"):

```markdown
## Metadata-Struktur

Dieses Framework verwendet eine standardisierte Metadatenstruktur mit 13 Pflichtfeldern:

### Metadaten-Datei

**Datei:** `0000_metadata_de_{framework}.md`

Die Metadaten-Datei enthält:
- **Dokument-ID:** Eindeutige Identifikation (0000)
- **Owner:** Dokumentenverantwortlicher (`{{ meta.owner }}`)
- **Version:** Dokumentversion (`{{ meta.version }}`)
- **Status:** Dokumentstatus (`{{ meta.status }}`)
- **Klassifizierung:** Sicherheitsklassifizierung (`{{ meta.classification }}`)
- **Letzte Aktualisierung:** Datum (`{{ meta.date }}`)
- **Template-Version:** Template-Format-Version (z.B. "1.0")
- **Revision:** Anpassungs-Revisionsnummer (z.B. "0")
- **Organisation:** Organisationsname (`{{ meta.organization }}`)
- **Autor:** Dokumentautor (`{{ meta.author }}`)
- **Geltungsbereich:** Anwendungsbereich (`{{ meta.scope }}`)
- **Gültig ab:** Gültigkeitsbeginn (`{{ meta.valid_from }}`)
- **Nächste Überprüfung:** Überprüfungsdatum (`{{ meta.next_review }}`)

### Template-Versionierung

**Template-Version** (`template_version`):
- Verfolgt Änderungen am Template-Format
- Format: `MAJOR.MINOR` (z.B. "1.0", "1.1", "2.0")
- Ermöglicht Kompatibilitätsprüfung bei Migrationen
- Wird mit `--test` Flag verwaltet

**Revision** (`revision`):
- Verfolgt individuelle Anpassungen
- Format: Integer (z.B. 0, 1, 2, 3)
- Für zukünftige Customization-Tracking-Funktionalität

### Metadaten validieren

```bash
# {Framework}-Metadaten validieren
python helpers/validate_metadata.py --framework {framework}

# Alle Frameworks validieren
python helpers/validate_metadata.py --all

# Bilinguale Konsistenz prüfen
python helpers/validate_metadata.py --framework {framework} --check-bilingual
```

Siehe [METADATA_VALIDATION_GUIDE.md](../../../docs/METADATA_VALIDATION_GUIDE.md) für Details.
```

## Standard Metadata Section (English)

Add this section to all English framework README.md files (after the template organization section, before "Usage Guidelines"):

```markdown
## Metadata Structure

This framework uses a standardized metadata structure with 13 required fields:

### Metadata File

**File:** `0000_metadata_en_{framework}.md`

The metadata file contains:
- **Document-ID:** Unique identification (0000)
- **Owner:** Document owner (`{{ meta.owner }}`)
- **Version:** Document version (`{{ meta.version }}`)
- **Status:** Document status (`{{ meta.status }}`)
- **Classification:** Security classification (`{{ meta.classification }}`)
- **Last Updated:** Date (`{{ meta.date }}`)
- **Template-Version:** Template format version (e.g., "1.0")
- **Revision:** Customization revision number (e.g., "0")
- **Organization:** Organization name (`{{ meta.organization }}`)
- **Author:** Document author (`{{ meta.author }}`)
- **Scope:** Applicability scope (`{{ meta.scope }}`)
- **Valid From:** Validity start date (`{{ meta.valid_from }}`)
- **Next Review:** Review date (`{{ meta.next_review }}`)

### Template Versioning

**Template Version** (`template_version`):
- Tracks changes to the template format
- Format: `MAJOR.MINOR` (e.g., "1.0", "1.1", "2.0")
- Enables compatibility checking for migrations
- Managed with `--test` flag

**Revision** (`revision`):
- Tracks individual customizations
- Format: Integer (e.g., 0, 1, 2, 3)
- For future customization tracking functionality

### Validate Metadata

```bash
# Validate {Framework} metadata
python helpers/validate_metadata.py --framework {framework}

# Validate all frameworks
python helpers/validate_metadata.py --all

# Check bilingual consistency
python helpers/validate_metadata.py --framework {framework} --check-bilingual
```

See [METADATA_VALIDATION_GUIDE.md](../../../docs/METADATA_VALIDATION_GUIDE.md) for details.
```

## Framework-Specific Replacements

Replace `{framework}` with the appropriate framework identifier:

| Framework | Identifier | German Name | English Name |
|-----------|------------|-------------|--------------|
| BCM | `bcm` | BCM | BCM |
| ISMS | `isms` | ISMS | ISMS |
| BSI Grundschutz | `bsi-grundschutz` | BSI Grundschutz | BSI Grundschutz |
| IT-Operation | `it-operation` | IT-Operation | IT-Operation |
| CIS Controls | `cis-controls` | CIS Controls | CIS Controls |
| Common Criteria | `common-criteria` | Common Criteria | Common Criteria |
| GDPR | `gdpr` | DSGVO | GDPR |
| HIPAA | `hipaa` | HIPAA | HIPAA |
| ISO 9001 | `iso-9001` | ISO 9001 | ISO 9001 |
| NIST 800-53 | `nist-800-53` | NIST 800-53 | NIST 800-53 |
| PCI-DSS | `pci-dss` | PCI-DSS | PCI-DSS |
| TSC | `tsc` | TSC | TSC |

## Implementation Checklist

For each framework:

### German README (templates/de/{framework}/README.md)

- [ ] Add "Metadata-Struktur" section after template organization
- [ ] Replace `{framework}` with framework identifier
- [ ] Verify section placement (before "Nutzungshinweise")
- [ ] Check markdown formatting
- [ ] Validate links to documentation

### English README (templates/en/{framework}/README.md)

- [ ] Add "Metadata Structure" section after template organization
- [ ] Replace `{framework}` with framework identifier
- [ ] Verify section placement (before "Usage Guidelines")
- [ ] Check markdown formatting
- [ ] Validate links to documentation

## Example: GDPR Implementation

### German (templates/de/gdpr/README.md)

```markdown
## Metadata-Struktur

Dieses Framework verwendet eine standardisierte Metadatenstruktur mit 13 Pflichtfeldern:

### Metadaten-Datei

**Datei:** `0000_metadata_de_gdpr.md`

Die Metadaten-Datei enthält:
- **Dokument-ID:** Eindeutige Identifikation (0000)
- **Owner:** Dokumentenverantwortlicher (`{{ meta.owner }}`)
...
```

### English (templates/en/gdpr/README.md)

```markdown
## Metadata Structure

This framework uses a standardized metadata structure with 13 required fields:

### Metadata File

**File:** `0000_metadata_en_gdpr.md`

The metadata file contains:
- **Document-ID:** Unique identification (0000)
- **Owner:** Document owner (`{{ meta.owner }}`)
...
```

## Service Directory Documentation

For frameworks that reference service templates, add this note:

### German

```markdown
### Service-Templates

Service-bezogene Templates befinden sich im dedizierten Verzeichnis:
- `templates/de/service-directory/service-templates/`
- `templates/de/service-directory/email-service/`

Siehe [Service Directory Reorganisation](../../../README.md#service-directory-reorganisation) für Details.
```

### English

```markdown
### Service Templates

Service-related templates are located in the dedicated directory:
- `templates/en/service-directory/service-templates/`

See [Service Directory Reorganization](../../../README.md#service-directory-reorganization) for details.
```

## Validation After Updates

After updating all framework READMEs:

```bash
# Check all README files exist
find templates -name "README.md" | wc -l
# Expected: 24 (12 frameworks × 2 languages)

# Validate markdown syntax
for readme in templates/*/*/README.md; do
    echo "Checking $readme"
    # Use markdown linter if available
    markdownlint "$readme" || echo "No linter available"
done

# Verify metadata sections exist
grep -r "Metadata-Struktur" templates/de/*/README.md | wc -l
# Expected: 12

grep -r "Metadata Structure" templates/en/*/README.md | wc -l
# Expected: 12
```

## Frameworks Updated

Track which frameworks have been updated:

- [x] GDPR (de) - Updated
- [ ] GDPR (en) - Pending
- [ ] BCM (de) - Pending
- [ ] BCM (en) - Pending
- [ ] ISMS (de) - Pending
- [ ] ISMS (en) - Pending
- [ ] BSI Grundschutz (de) - Pending
- [ ] BSI Grundschutz (en) - Pending
- [ ] IT-Operation (de) - Pending
- [ ] IT-Operation (en) - Pending
- [ ] CIS Controls (de) - Pending
- [ ] CIS Controls (en) - Pending
- [ ] Common Criteria (de) - Pending
- [ ] Common Criteria (en) - Pending
- [ ] HIPAA (de) - Pending
- [ ] HIPAA (en) - Pending
- [ ] ISO 9001 (de) - Pending
- [ ] ISO 9001 (en) - Pending
- [ ] NIST 800-53 (de) - Pending
- [ ] NIST 800-53 (en) - Pending
- [ ] PCI-DSS (de) - Pending
- [ ] PCI-DSS (en) - Pending
- [ ] TSC (de) - Pending
- [ ] TSC (en) - Pending

## Summary

This standardized metadata section ensures:
- ✅ Consistent documentation across all frameworks
- ✅ Clear explanation of metadata structure
- ✅ Template versioning documentation
- ✅ Validation instructions
- ✅ Links to detailed guides
- ✅ Bilingual support

All framework README files should include this section to maintain documentation consistency.
