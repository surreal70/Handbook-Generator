# Migration Guide: Template System Extension

## Overview

This guide helps existing users migrate to the extended template system that includes three new template types (BCM, ISMS, BSI Grundschutz) and HTML comment support. The extension maintains **full backward compatibility** with existing it-operation templates.

## What's New

### New Template Types

1. **BCM (Business Continuity Management)**
   - 30 templates covering ISO 22301 and BSI BCM standards
   - Available in German and English
   - Includes BIA, RTO/RPO, crisis management, and DR planning

2. **ISMS (Information Security Management System)**
   - ~50 templates covering ISO 27001:2022 (including Amendment 1:2024)
   - Three-tier structure: Basis ISMS, Abstract Policies, Detailed Guidelines
   - Complete Annex A control mapping
   - Available in German and English

3. **BSI Grundschutz**
   - ~40 templates covering BSI Standards 200-1, 200-2, 200-3
   - BSI Baustein references throughout
   - Policy-Guideline pairs for 17 security areas
   - Available in German and English

### HTML Comment Support

Templates can now include HTML comments for non-rendered documentation:

```markdown
<!-- This comment will not appear in the generated handbook -->

# Chapter Title

<!-- 
TEMPLATE AUTHOR NOTE:
Customize this section based on your organization's requirements.
-->

Your content here...
```

**Use cases:**
- Template author notes and hints
- Customization instructions
- Framework compliance references
- TODO markers for incomplete sections

## Backward Compatibility

### Guaranteed Compatibility

✅ **Existing it-operation templates continue to work unchanged**
- No modifications required to existing templates
- Same CLI parameters work as before
- Same output structure and format
- Same placeholder syntax and processing

✅ **Existing configurations remain valid**
- `config.yaml` files work without changes
- `metadata.yaml` files work without changes
- NetBox integration unchanged

✅ **Existing workflows preserved**
- Same command-line interface
- Same output directory structure
- Same file naming conventions

### What Hasn't Changed

- **Placeholder syntax**: `{{ meta.field }}` and `{{ netbox.field }}` work identically
- **Data sources**: NetBox adapter and meta adapter unchanged
- **Output formats**: Markdown and PDF generation unchanged
- **Template discovery**: Automatic language/type detection unchanged
- **Configuration files**: Same structure and fields

## Migration Steps

### For Existing Users (No Action Required)

If you're using it-operation templates, **no migration is needed**. Your existing setup will continue to work exactly as before.

```bash
# This command works exactly as before
python -m src.cli --language de --template it-operation
```

### To Use New Template Types

1. **Update your installation** (if needed):
   ```bash
   git pull origin main
   pip install -r requirements.txt
   ```

2. **Generate new handbook types**:
   ```bash
   # BCM handbook
   python -m src.cli --language de --template bcm
   
   # ISMS handbook
   python -m src.cli --language en --template isms
   
   # BSI Grundschutz handbook
   python -m src.cli --language de --template bsi-grundschutz
   ```

3. **No configuration changes required** - your existing `config.yaml` and `metadata.yaml` work with all template types.

### To Use HTML Comments in Custom Templates

If you maintain custom templates, you can now add HTML comments:

**Before** (workaround with markdown that appeared in output):
```markdown
# Chapter

[//]: # (TODO: Add organization-specific content here)

Content...
```

**After** (clean HTML comments):
```markdown
# Chapter

<!-- TODO: Add organization-specific content here -->

Content...
```

HTML comments are automatically stripped during processing and never appear in generated handbooks.

## New Features Overview

### 1. BCM Templates

**Purpose**: Create comprehensive Business Continuity Management documentation

**Key Features:**
- ISO 22301 compliance mapping
- BSI BCM standards references
- Business Impact Analysis (BIA) templates
- RTO/RPO definitions
- Crisis management plans
- Disaster recovery procedures
- Testing and exercise programs

**Example Usage:**
```bash
python -m src.cli --language de --template bcm --output both
```

**Output:** `Handbook/de/bcm/bcm_handbook_de.md` and `.pdf`

### 2. ISMS Templates

**Purpose**: Create ISO 27001:2022 compliant Information Security Management System documentation

**Key Features:**
- ISO 27001:2022 compliance (including Amendment 1:2024)
- Complete Annex A control mapping
- Three-tier structure:
  - **Basis ISMS** (0010-0160): Foundation documents
  - **Abstract Policies** (0200-0680): High-level security policies
  - **Detailed Guidelines** (0210-0690): Implementation guidance
- Statement of Applicability (SoA) template
- Risk management templates

**Example Usage:**
```bash
python -m src.cli --language en --template isms --output pdf
```

**Output:** `Handbook/en/isms/isms_handbook_en.pdf`

### 3. BSI Grundschutz Templates

**Purpose**: Create BSI IT-Grundschutz compliant security documentation

**Key Features:**
- BSI Standards 200-1, 200-2, 200-3 compliance
- BSI Baustein references throughout
- Structure analysis and protection needs assessment
- Gap analysis (Basis-Sicherheitscheck)
- Risk analysis per BSI Standard 200-3
- Policy-Guideline pairs for 17 security areas
- Evidence register and audit support

**Example Usage:**
```bash
python -m src.cli --language de --template bsi-grundschutz
```

**Output:** `Handbook/de/bsi-grundschutz/bsi-grundschutz_handbook_de.md` and `.pdf`

### 4. HTML Comment Processing

**Purpose**: Add non-rendered documentation to templates

**Features:**
- Single-line comments: `<!-- comment -->`
- Multi-line comments spanning multiple lines
- Automatic removal before placeholder processing
- Preserves all markdown formatting
- No impact on output

**Best Practices:**
```markdown
<!-- 
CUSTOMIZATION REQUIRED:
1. Update organization-specific values
2. Review compliance requirements
3. Adjust RACI matrix for your structure
-->

## Section Title

<!-- This section maps to ISO 27001:2022 Clause 5.2 -->

Content with {{ meta.organization.name }} placeholder...

<!-- End of customization section -->
```

## Template Structure Comparison

### IT-Operation Templates (Existing)

```
templates/de/it-operation/
├── README.md
├── 0010_Einleitung.md
├── 0020_Dokumentenlenkung.md
├── 0030_Service.md
└── ... (26 more templates)
```

**Numbering:** 0010-0290 (29 templates)
**Focus:** IT operations, ITIL v4, ISO 20000-1, COBIT 2019

### BCM Templates (New)

```
templates/de/bcm/
├── README.md
├── 0010_Zweck_und_Geltungsbereich.md
├── 0020_BCM_Leitlinie_Policy.md
├── 0030_Dokumentenlenkung_und_Versionierung.md
└── ... (27 more templates)
```

**Numbering:** 0010-0290 (30 templates)
**Focus:** Business continuity, ISO 22301, BSI BCM standards

### ISMS Templates (New)

```
templates/de/isms/
├── README.md
├── 0010_ISMS_Informationssicherheitsleitlinie.md
├── 0020_ISMS_Geltungsbereich_Scope.md
├── 0030_ISMS_Kontext_und_Interessierte_Parteien.md
├── 0200_Policy_Akzeptable_Nutzung_IT.md
├── 0210_Richtlinie_Akzeptable_Nutzung_IT.md
└── ... (45 more templates)
```

**Numbering:** 0010-0740 (~50 templates)
**Focus:** Information security, ISO 27001:2022, Annex A controls
**Structure:** Three-tier (Basis, Policies, Guidelines)

### BSI Grundschutz Templates (New)

```
templates/de/bsi-grundschutz/
├── README.md
├── 0010_Informationssicherheitsleitlinie.md
├── 0020_ISMS_Organisation_Rollen_RACI.md
├── 0050_Strukturanalyse_Template.md
├── 0200_Policy_Zugriffssteuerung_und_Berechtigungen.md
└── ... (36 more templates)
```

**Numbering:** 0010-0740 (~40 templates)
**Focus:** BSI IT-Grundschutz, BSI Standards 200-1/2/3, BSI Bausteine

## Placeholder Consistency

All template types use the **same placeholder syntax**:

### Meta Placeholders (Organization-wide data)

```markdown
{{ meta.organization.name }}
{{ meta.ceo.name }}
{{ meta.cio.email }}
{{ meta.ciso.name }}
{{ meta.document.owner }}
{{ meta.document.version }}
```

### NetBox Placeholders (Infrastructure data)

```markdown
{{ netbox.site.name }}
{{ netbox.device.core_switch.name }}
{{ netbox.vlan.management.vid }}
{{ netbox.primary_ip }}
```

**No changes required** to your `metadata.yaml` or NetBox configuration.

## CLI Changes

### New Template Type Options

The `--template` parameter now accepts four values:

```bash
--template it-operation      # Existing (unchanged)
--template bcm               # New
--template isms              # New
--template bsi-grundschutz   # New
```

### Interactive Mode

When running without parameters, the system now shows all four template types:

```bash
$ python -m src.cli

Available languages: de, en
Available template types: bcm, bsi-grundschutz, isms, it-operation

Select language (de/en): de
Select template type: bcm
Select output format (markdown/pdf/both): both

Generating BCM handbook in German...
```

### All Other Parameters Unchanged

```bash
--language, -l    # Same as before
--output, -o      # Same as before
--verbose, -v     # Same as before
--config, -c      # Same as before
```

## Output Structure

### Before (Existing)

```
Handbook/
├── de/
│   └── it-operation/
│       ├── it-operation_handbook_de.md
│       └── it-operation_handbook_de.pdf
└── en/
    └── it-operation/
        ├── it-operation_handbook_en.md
        └── it-operation_handbook_en.pdf
```

### After (Extended)

```
Handbook/
├── de/
│   ├── bcm/                    # New
│   ├── isms/                   # New
│   ├── bsi-grundschutz/        # New
│   └── it-operation/           # Unchanged
└── en/
    ├── bcm/                    # New
    ├── isms/                   # New
    ├── bsi-grundschutz/        # New
    └── it-operation/           # Unchanged
```

**File naming pattern:** `{template-type}_handbook_{language}.{ext}`

## Testing Your Migration

### 1. Verify Existing Functionality

```bash
# Test existing it-operation templates
python -m src.cli --language de --template it-operation --output markdown

# Compare output with previous version
diff Handbook/de/it-operation/it-operation_handbook_de.md <previous_version>
```

**Expected result:** Identical output (no changes)

### 2. Test New Template Types

```bash
# Test BCM
python -m src.cli --language de --template bcm --output markdown

# Test ISMS
python -m src.cli --language en --template isms --output markdown

# Test BSI Grundschutz
python -m src.cli --language de --template bsi-grundschutz --output markdown
```

**Expected result:** New handbooks generated successfully

### 3. Test HTML Comments (Optional)

Create a test template with HTML comments:

```markdown
<!-- Test comment -->
# Test Chapter
<!-- Multi-line
comment
test -->
Content
```

Process and verify comments are removed from output.

## Troubleshooting

### Issue: "Template type not found"

**Symptom:** Error message when trying to use new template types

**Solution:** Ensure you've pulled the latest code:
```bash
git pull origin main
```

### Issue: Existing templates not working

**Symptom:** it-operation templates fail to process

**Diagnosis:** This should not happen (backward compatibility guaranteed)

**Solution:** 
1. Check for local modifications to templates
2. Verify `config.yaml` is valid
3. Run with `--verbose` flag for detailed logging
4. Report issue if problem persists

### Issue: HTML comments appearing in output

**Symptom:** Comments like `<!-- ... -->` visible in generated handbooks

**Diagnosis:** HTML comment processor not running

**Solution:**
1. Verify you're using the latest version
2. Check template file encoding (should be UTF-8)
3. Run with `--verbose` to see processing steps

### Issue: Placeholders not replaced in new templates

**Symptom:** `{{ meta.field }}` appears literally in output

**Diagnosis:** Missing metadata or NetBox configuration

**Solution:**
1. Verify `metadata.yaml` exists and is valid
2. Check `config.yaml` for NetBox credentials
3. Ensure placeholder syntax is correct: `{{ source.field }}`
4. Run with `--verbose` to see placeholder processing

## Getting Help

### Documentation

- **Main README:** `README.md` - General usage and setup
- **Framework Mapping:** `docs/FRAMEWORK_MAPPING.md` - Compliance mappings
- **Template READMEs:** Each template directory has a README explaining structure

### Template-Specific Documentation

- **BCM:** `templates/de/bcm/README.md` and `templates/en/bcm/README.md`
- **ISMS:** `templates/de/isms/README.md` and `templates/en/isms/README.md`
- **BSI Grundschutz:** `templates/de/bsi-grundschutz/README.md` and `templates/en/bsi-grundschutz/README.md`

### Support

For questions or issues:
1. Check this migration guide
2. Review template-specific README files
3. Run with `--verbose` flag for detailed logging
4. Check existing GitHub issues
5. Create new issue with detailed description

## Summary

### Key Takeaways

✅ **No action required for existing users** - everything continues to work

✅ **Three new template types available** - BCM, ISMS, BSI Grundschutz

✅ **HTML comments supported** - for template documentation

✅ **Same configuration files** - no changes needed

✅ **Same CLI interface** - just more template type options

✅ **Same placeholder syntax** - works across all template types

### Next Steps

1. **Continue using existing templates** - no changes needed
2. **Explore new template types** - try generating BCM, ISMS, or BSI Grundschutz handbooks
3. **Add HTML comments to custom templates** - improve template documentation
4. **Review framework mappings** - see `docs/FRAMEWORK_MAPPING.md` for compliance details

---

**Document Version:** 1.0.0  
**Last Updated:** 2025-02-03  
**Applies to:** Template System Extension v2.0.0+
