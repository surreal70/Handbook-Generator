# Handbook PDFs

This directory contains PDF versions of all generated handbooks from the Handbook Generator system.

## Generated PDFs

### German Handbooks (de/)

1. **BSI IT-Grundschutz Handbook** (284 KB)
   - Path: `de/bsi-grundschutz/bsi-grundschutz_handbook.pdf`
   - Framework: BSI Standards 200-1, 200-2, 200-3
   - Content: 45 templates covering ISMS foundation, policies, guidelines, and appendices

2. **Business Continuity Management (BCM) Handbook** (123 KB)
   - Path: `de/bcm/bcm_handbook.pdf`
   - Framework: ISO 22301
   - Content: 30 templates covering BCM policy, BIA, risk analysis, crisis management, and DR plans

3. **Information Security Management System (ISMS) Handbook** (582 KB)
   - Path: `de/isms/isms_handbook.pdf`
   - Framework: ISO 27001:2022 (including Amendment 1:2024)
   - Content: 54 templates with three-tier structure (Basis, Policies, Guidelines)

4. **IT Operations Handbook** (370 KB)
   - Path: `de/it-operation/it-operation_handbook.pdf`
   - Framework: ITIL/IT Service Management
   - Content: 29 templates covering operations, monitoring, incident management, and compliance

5. **Email Service Handbook** (8.5 KB)
   - Path: `de/email-service/email_service_handbook.pdf`
   - Framework: Service-specific documentation
   - Content: Example service handbook demonstrating template customization

6. **Backup Handbook** (2.3 KB)
   - Path: `de/backup/backup_handbook.pdf`
   - Framework: Backup and recovery procedures
   - Content: Backup strategy and procedures

### English Handbooks (en/)

1. **BSI IT-Grundschutz Handbook** (274 KB)
   - Path: `en/bsi-grundschutz/bsi-grundschutz_handbook.pdf`
   - Framework: BSI Standards 200-1, 200-2, 200-3
   - Content: English version with same structure as German handbook

2. **Business Continuity Management (BCM) Handbook** (117 KB)
   - Path: `en/bcm/bcm_handbook.pdf`
   - Framework: ISO 22301
   - Content: English version with same structure as German handbook

3. **Information Security Management System (ISMS) Handbook** (520 KB)
   - Path: `en/isms/isms_handbook.pdf`
   - Framework: ISO 27001:2022 (including Amendment 1:2024)
   - Content: English version with same structure as German handbook

4. **IT Operations Handbook** (291 KB)
   - Path: `en/it-operation/it-operation_handbook.pdf`
   - Framework: ITIL/IT Service Management
   - Content: English version with same structure as German handbook

## Statistics

- **Total PDFs Generated:** 10
- **Total Size:** ~2.5 MB
- **Languages:** German (de) and English (en)
- **Frameworks Covered:** ISO 27001, ISO 22301, BSI IT-Grundschutz, ITIL
- **Total Templates:** 260+ across all handbooks

## PDF Features

All PDFs include:
- A4 page format with 2cm margins
- Professional styling with color-coded headings
- Table of contents (where applicable)
- Numbered sections
- Syntax-highlighted code blocks
- Formatted tables with alternating row colors
- Page numbering in footer
- UTF-8 encoding for international characters

## Generation Details

- **Generated:** 2026-02-04
- **Generator:** Handbook Generator v2.0.0
- **PDF Engine:** ReportLab (Python)
- **Source Format:** Markdown
- **Metadata Source:** metadata.yaml (AdminSend GmbH)

## Usage

These PDFs are ready for:
- Distribution to stakeholders
- Audit documentation
- Compliance evidence
- Training materials
- Reference documentation
- Certification preparation (ISO 27001, ISO 22301, BSI IT-Grundschutz)

## Regeneration

To regenerate PDFs from updated handbooks:

```bash
# Using Python script (recommended)
python generate_pdfs.py

# Using Pandoc (requires pandoc + LaTeX)
./generate_pdfs_pandoc.sh

# Using wkhtmltopdf (requires wkhtmltopdf)
./generate_pdfs_simple.sh
```

## Notes

- PDFs are generated from the Markdown handbooks in the `Handbook/` directory
- All meta placeholders have been replaced with organization-specific data
- Images referenced in handbooks may show as placeholders if diagram files are missing
- For best results, ensure all referenced diagram files exist before generation

---

**Project:** Handbook Generator - Template System Extension  
**Version:** 2.0.0  
**Organization:** AdminSend GmbH
