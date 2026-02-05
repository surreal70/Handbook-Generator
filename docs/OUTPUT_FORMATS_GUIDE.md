# Output Formats Guide

This guide explains the different output formats available in the Handbook Generator and provides examples of the generated output structure.

## Table of Contents

- [Overview](#overview)
- [Separate Markdown Files](#separate-markdown-files)
- [PDF with Table of Contents](#pdf-with-table-of-contents)
- [HTML Mini-Website](#html-mini-website)
- [Combined Output](#combined-output)
- [Examples](#examples)

## Overview

The Handbook Generator supports multiple output formats:

1. **Markdown** - Single combined file or separate files per template
2. **PDF** - Single file with optional table of contents and page breaks
3. **HTML** - Mini-website with navigation between pages

All outputs are generated in the `test-output/{language}/{format}/` directory structure.

## Separate Markdown Files

### Usage

```bash
python -m src.cli --language de --template bcm --test --separate-files
```

### Output Structure

```
test-output/de/markdown/
├── TOC.md                                    # Table of contents with links
├── 0010_Zweck_und_Geltungsbereich.md        # Individual template
├── 0020_BCM_Leitlinie_Policy.md             # Individual template
├── 0030_Dokumentenlenkung_und_Versionierung.md
├── 0040_Notfallorganisation_Rollen_und_Gremien.md
└── ... (more templates)
```

### TOC.md Example

```markdown
# Table of Contents

- [0010 - Zweck und Geltungsbereich](0010_Zweck_und_Geltungsbereich.md)
- [0020 - BCM Leitlinie Policy](0020_BCM_Leitlinie_Policy.md)
- [0030 - Dokumentenlenkung und Versionierung](0030_Dokumentenlenkung_und_Versionierung.md)
- [0040 - Notfallorganisation Rollen und Gremien](0040_Notfallorganisation_Rollen_und_Gremien.md)
...
```

### Individual Template Example

**File:** `0010_Zweck_und_Geltungsbereich.md`

```markdown
# Zweck und Geltungsbereich

## 1. Zweck dieses Handbuchs

Dieses Business Continuity Management (BCM) Handbuch beschreibt...

## 2. Geltungsbereich

Das BCM-Handbuch gilt für:
- Organisation: Example Corp
- Standorte: Alle Standorte
...
```

### Benefits

- **Easy Editing**: Individual chapters can be edited separately
- **Version Control**: Git diffs are clearer when changes are made to individual chapters
- **Modular Structure**: Chapters can be shared or reused individually
- **Navigation**: TOC.md provides quick overview and navigation

## PDF with Table of Contents

### Usage

```bash
python -m src.cli --language de --template bcm --output pdf --test --pdf-toc
```

### Output Structure

```
test-output/de/pdf/
└── bcm_handbook.pdf                          # PDF with TOC and page breaks
```

### PDF Structure

The generated PDF contains:

1. **Table of Contents** (First page)
   - Template numbers and titles
   - Clickable links to sections
   - Automatically generated page numbers

2. **Template Sections** (Following pages)
   - Each template starts on a new page
   - Page breaks between templates
   - Anchor IDs for internal linking

### Table of Contents Example

```
Table of Contents

0010 - Zweck und Geltungsbereich ..................... Page 2
0020 - BCM Leitlinie Policy .......................... Page 5
0030 - Dokumentenlenkung und Versionierung ........... Page 8
0040 - Notfallorganisation Rollen und Gremien ........ Page 12
0050 - Kontakte und Eskalation ....................... Page 16
...
```

### Technical Details

- **Page Breaks**: CSS `page-break-after: always` property
- **Anchor IDs**: Format `#section-0010`, `#section-0020`, etc.
- **TOC Links**: HTML anchor links `<a href="#section-0010">...</a>`
- **Rendering**: WeasyPrint converts HTML to PDF with all features

### Benefits

- **Professional Layout**: Clear structure with table of contents
- **Easy Navigation**: Clickable links to all chapters
- **Print-Friendly**: Each chapter starts on a new page
- **Overview**: Quick overview of all contents

## HTML Mini-Website

### Usage

```bash
python -m src.cli --language de --template bcm --output html --test
```

### Output Structure

```
test-output/de/html/
├── index.html                                # Table of contents page
├── 0010_Zweck_und_Geltungsbereich.html      # Individual template page
├── 0020_BCM_Leitlinie_Policy.html           # Individual template page
├── 0030_Dokumentenlenkung_und_Versionierung.html
├── 0040_Notfallorganisation_Rollen_und_Gremien.html
├── ... (more template pages)
└── styles.css                                # Consistent styling
```

### Navigation Features

- **Previous/Next Links**: Navigate between templates
- **Back to TOC**: Link back to table of contents on each page
- **Consistent Styling**: Professional appearance across all pages

### Benefits

- **Web-Based**: View in any browser
- **Easy Navigation**: Click through chapters
- **Responsive**: Works on desktop and mobile
- **Shareable**: Can be hosted on web server

## Combined Output

### Usage

```bash
# Generate all formats with all features
python -m src.cli --language de --template bcm --output all --test --separate-files --pdf-toc
```

### Output Structure

```
test-output/de/
├── markdown/
│   ├── TOC.md
│   ├── 0010_Zweck_und_Geltungsbereich.md
│   ├── 0020_BCM_Leitlinie_Policy.md
│   └── ... (more templates)
├── pdf/
│   └── bcm_handbook.pdf                      # With TOC and page breaks
└── html/
    ├── index.html
    ├── 0010_Zweck_und_Geltungsbereich.html
    ├── 0020_BCM_Leitlinie_Policy.html
    ├── ... (more template pages)
    └── styles.css
```

## Examples

### Example 1: BCM Handbook with Separate Markdown Files

**Command:**
```bash
python -m src.cli --language de --template bcm --test --separate-files
```

**Output:**
- 30 separate markdown files in `test-output/de/markdown/`
- 1 TOC.md file with links to all templates
- Each file named according to pattern: `{number}_{name}.md`

**Use Case:** You want to edit individual chapters separately and track changes in Git.

### Example 2: ISMS Handbook with PDF TOC

**Command:**
```bash
python -m src.cli --language en --template isms --output pdf --test --pdf-toc
```

**Output:**
- 1 PDF file in `test-output/en/pdf/isms_handbook.pdf`
- Table of contents on first page
- ~50 templates with page breaks between each

**Use Case:** You need a professional PDF for printing or distribution.

### Example 3: BSI Grundschutz Handbook - All Formats

**Command:**
```bash
python -m src.cli --language de --template bsi-grundschutz --output all --test --separate-files --pdf-toc
```

**Output:**
- Separate markdown files in `test-output/de/markdown/`
- PDF with TOC in `test-output/de/pdf/`
- HTML mini-website in `test-output/de/html/`

**Use Case:** You want maximum flexibility with all output formats available.

### Example 4: IT-Operation Handbook - Traditional Format

**Command:**
```bash
python -m src.cli --language de --template it-operation --test
```

**Output:**
- 1 combined markdown file in `test-output/de/markdown/it-operation_handbook.md`
- 1 PDF file without TOC in `test-output/de/pdf/it-operation_handbook.pdf`

**Use Case:** You prefer the traditional single-file format.

## Comparison Table

| Feature | Combined Markdown | Separate Markdown | PDF | PDF with TOC | HTML |
|---------|------------------|-------------------|-----|--------------|------|
| Single File | ✅ | ❌ | ✅ | ✅ | ❌ |
| Multiple Files | ❌ | ✅ | ❌ | ❌ | ✅ |
| Table of Contents | ❌ | ✅ (TOC.md) | ❌ | ✅ | ✅ (index.html) |
| Page Breaks | ❌ | ❌ | ❌ | ✅ | N/A |
| Clickable Links | ❌ | ✅ | ❌ | ✅ | ✅ |
| Easy Editing | ✅ | ✅✅ | ❌ | ❌ | ❌ |
| Print-Friendly | ⚠️ | ⚠️ | ✅ | ✅✅ | ⚠️ |
| Web-Friendly | ⚠️ | ✅ | ❌ | ❌ | ✅✅ |
| Git-Friendly | ✅ | ✅✅ | ❌ | ❌ | ✅ |

**Legend:**
- ✅ = Supported
- ✅✅ = Best option for this use case
- ⚠️ = Partially supported
- ❌ = Not supported
- N/A = Not applicable

## Best Practices

### When to Use Separate Markdown Files

- You need to edit individual chapters frequently
- You want clear Git diffs for version control
- You're collaborating with multiple authors on different chapters
- You want to reuse individual chapters in other documents

### When to Use PDF with TOC

- You need a professional document for printing
- You're distributing the handbook to stakeholders
- You want a single file with easy navigation
- You need a formal document for compliance purposes

### When to Use HTML Output

- You want to publish the handbook on an intranet
- You need web-based access for users
- You want responsive design for mobile devices
- You're creating an online knowledge base

### When to Use Combined Output

- You want maximum flexibility
- You're not sure which format you'll need
- You want to provide multiple options to users
- You have sufficient disk space for all formats

## Troubleshooting

### Separate Files Not Generated

**Problem:** Running with `--separate-files` but getting a single file.

**Solution:** Ensure you're using `--output markdown` or `--output both` or `--output all`. The `--separate-files` flag only affects markdown output.

```bash
# Correct
python -m src.cli -l de -t bcm --output markdown --test --separate-files

# Incorrect (will be ignored)
python -m src.cli -l de -t bcm --output pdf --test --separate-files
```

### PDF TOC Not Showing

**Problem:** PDF generated but no table of contents visible.

**Solution:** Ensure you're using the `--pdf-toc` flag:

```bash
# Correct
python -m src.cli -l de -t bcm --output pdf --test --pdf-toc

# Incorrect (no TOC)
python -m src.cli -l de -t bcm --output pdf --test
```

### Test Mode Required Error

**Problem:** `ERROR: Output generation requires --test flag.`

**Solution:** Always include the `--test` flag for safety:

```bash
python -m src.cli -l de -t bcm --test
```

## See Also

- [README.md](../README.md) - Main documentation
- [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Migration from old output structure
- [PDF_GENERATION_GUIDE.md](PDF_GENERATION_GUIDE.md) - Detailed PDF generation guide
