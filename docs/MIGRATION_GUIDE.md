# Migration Guide: Compliance Framework Templates Extension

## Overview

This guide helps existing users migrate to the extended template system that now includes **twelve compliance framework types** covering major international standards. The extension maintains **full backward compatibility** with all existing templates.

## What's New

### Twelve Compliance Framework Types

The system now supports twelve comprehensive compliance frameworks:

1. **BCM (Business Continuity Management)** - 29 templates
   - ISO 22301 and BSI BCM standards
   - BIA, RTO/RPO, crisis management, DR planning

2. **ISMS (Information Security Management System)** - 70 templates
   - ISO 27001:2022 with complete Annex A control mapping
   - Three-tier structure: Basis ISMS, Abstract Policies, Detailed Guidelines

3. **BSI Grundschutz** - 54 templates
   - BSI Standards 200-1, 200-2, 200-3
   - BSI Baustein references throughout

4. **IT-Operation** - 30 templates
   - ITIL v4, ISO 20000-1, COBIT 2019
   - IT operations and service management

5. **CIS Controls** - 27 templates
   - CIS Controls v8 Framework
   - Hardening baselines for OS and applications

6. **Common Criteria** - 35 templates
   - ISO/IEC 15408 Security Evaluation
   - Security Target (ST) documentation

7. **GDPR** - 36 templates
   - EU GDPR 2016/679
   - Data protection and privacy compliance

8. **HIPAA** - 13 templates
   - HIPAA Security Rule
   - Healthcare data protection

9. **ISO 9001** - 29 templates
   - ISO 9001:2015 Quality Management System
   - Process and quality documentation

10. **NIST 800-53** - 52 templates
    - NIST SP 800-53 Rev. 5
    - Security and privacy controls

11. **PCI-DSS** - 14 templates
    - PCI-DSS v4.0
    - Payment card industry security

12. **TSC (SOC 2)** - 17 templates
    - SOC 2 Trust Services Criteria
    - Service organization controls

**Total: 408 templates in German + 407 templates in English = 815+ templates**

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

2. **Generate handbooks for any framework**:
   ```bash
   # BCM handbook
   ./handbook-generator --language de --template bcm --test
   
   # ISMS handbook
   ./handbook-generator --language en --template isms --test
   
   # BSI Grundschutz handbook
   ./handbook-generator --language de --template bsi-grundschutz --test
   
   # CIS Controls handbook
   ./handbook-generator --language de --template cis-controls --test
   
   # Common Criteria handbook
   ./handbook-generator --language en --template common-criteria --test
   
   # GDPR handbook
   ./handbook-generator --language de --template gdpr --test
   
   # HIPAA handbook
   ./handbook-generator --language en --template hipaa --test
   
   # ISO 9001 handbook
   ./handbook-generator --language de --template iso-9001 --test
   
   # NIST 800-53 handbook
   ./handbook-generator --language en --template nist-800-53 --test
   
   # PCI-DSS handbook
   ./handbook-generator --language de --template pci-dss --test
   
   # TSC (SOC 2) handbook
   ./handbook-generator --language en --template tsc --test
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

The `--template` parameter now accepts twelve values:

```bash
--template bcm                # Business Continuity Management (ISO 22301)
--template isms               # Information Security (ISO 27001:2022)
--template bsi-grundschutz    # BSI IT-Grundschutz
--template it-operation       # IT Operations (ITIL v4, ISO 20000-1)
--template cis-controls       # CIS Controls v8 Hardening
--template common-criteria    # Common Criteria (ISO/IEC 15408)
--template gdpr               # GDPR Compliance (EU 2016/679)
--template hipaa              # HIPAA Security Rule
--template iso-9001           # Quality Management (ISO 9001:2015)
--template nist-800-53        # NIST Security Controls (SP 800-53 Rev. 5)
--template pci-dss            # Payment Card Security (PCI-DSS v4.0)
--template tsc                # SOC 2 Trust Services
```

### Interactive Mode

When running without parameters, the system now shows all twelve template types:

```bash
$ ./handbook-generator

Available languages: de, en
Available template types: bcm, bsi-grundschutz, cis-controls, common-criteria, 
                         gdpr, hipaa, isms, iso-9001, it-operation, 
                         nist-800-53, pci-dss, tsc

Select language (de/en): de
Select template type: gdpr
Select output format (markdown/pdf/html/all): all

Generating GDPR handbook in German...
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
│   ├── bcm/                    # Business Continuity Management
│   ├── isms/                   # Information Security
│   ├── bsi-grundschutz/        # BSI IT-Grundschutz
│   ├── it-operation/           # IT Operations
│   ├── cis-controls/           # CIS Controls v8
│   ├── common-criteria/        # Common Criteria
│   ├── gdpr/                   # GDPR Compliance
│   ├── hipaa/                  # HIPAA Security
│   ├── iso-9001/               # Quality Management
│   ├── nist-800-53/            # NIST Controls
│   ├── pci-dss/                # Payment Card Security
│   └── tsc/                    # SOC 2 Trust Services
└── en/
    ├── bcm/
    ├── isms/
    ├── bsi-grundschutz/
    ├── it-operation/
    ├── cis-controls/
    ├── common-criteria/
    ├── gdpr/
    ├── hipaa/
    ├── iso-9001/
    ├── nist-800-53/
    ├── pci-dss/
    └── tsc/
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
./handbook-generator --language de --template bcm --test

# Test ISMS
./handbook-generator --language en --template isms --test

# Test BSI Grundschutz
./handbook-generator --language de --template bsi-grundschutz --test

# Test CIS Controls
./handbook-generator --language de --template cis-controls --test

# Test Common Criteria
./handbook-generator --language en --template common-criteria --test

# Test GDPR
./handbook-generator --language de --template gdpr --test

# Test HIPAA
./handbook-generator --language en --template hipaa --test

# Test ISO 9001
./handbook-generator --language de --template iso-9001 --test

# Test NIST 800-53
./handbook-generator --language en --template nist-800-53 --test

# Test PCI-DSS
./handbook-generator --language de --template pci-dss --test

# Test TSC
./handbook-generator --language en --template tsc --test
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
- **IT-Operation:** `templates/de/it-operation/README.md` and `templates/en/it-operation/README.md`
- **CIS Controls:** `templates/de/cis-controls/README.md` and `templates/en/cis-controls/README.md`
- **Common Criteria:** `templates/de/common-criteria/README.md` and `templates/en/common-criteria/README.md`
- **GDPR:** `templates/de/gdpr/README.md` and `templates/en/gdpr/README.md`
- **HIPAA:** `templates/de/hipaa/README.md` and `templates/en/hipaa/README.md`
- **ISO 9001:** `templates/de/iso-9001/README.md` and `templates/en/iso-9001/README.md`
- **NIST 800-53:** `templates/de/nist-800-53/README.md` and `templates/en/nist-800-53/README.md`
- **PCI-DSS:** `templates/de/pci-dss/README.md` and `templates/en/pci-dss/README.md`
- **TSC:** `templates/de/tsc/README.md` and `templates/en/tsc/README.md`

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

✅ **Twelve compliance frameworks available** - BCM, ISMS, BSI Grundschutz, IT-Operation, CIS Controls, Common Criteria, GDPR, HIPAA, ISO 9001, NIST 800-53, PCI-DSS, TSC

✅ **815+ templates total** - 408 German + 407 English templates

✅ **HTML comments supported** - for template documentation

✅ **Same configuration files** - no changes needed

✅ **Same CLI interface** - just more template type options

✅ **Same placeholder syntax** - works across all template types

### Next Steps

1. **Continue using existing templates** - no changes needed
2. **Explore new compliance frameworks** - try generating handbooks for your compliance needs
3. **Add HTML comments to custom templates** - improve template documentation
4. **Review framework mappings** - see each framework's `FRAMEWORK_MAPPING.md` for compliance details

---

**Document Version:** 2.0.0  
**Last Updated:** 2026-02-10  
**Applies to:** Compliance Framework Templates Extension v0.0.6+
