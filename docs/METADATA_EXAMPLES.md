# Template Metadata Examples

## Overview

This document provides complete examples of metadata files for all compliance frameworks, showing the unified structure with all required fields.

## Table of Contents

- [Metadata Structure](#metadata-structure)
- [Required Fields Reference](#required-fields-reference)
- [Complete Examples](#complete-examples)
  - [GDPR Example](#gdpr-example)
  - [ISO 9001 Example](#iso-9001-example)
  - [NIST 800-53 Example](#nist-800-53-example)
  - [PCI-DSS Example](#pci-dss-example)
- [Before/After Comparison](#beforeafter-comparison)
- [Framework-Specific Examples](#framework-specific-examples)

## Metadata Structure

All metadata files follow this unified structure:

```markdown
# {Framework Name} Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbuch-Informationen

**Handbuch-Titel:** {Framework Full Name}  
**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  

---

## Dokumentenzweck

{Framework-specific purpose description}

## Geltungsbereich

{Framework-specific scope description}

## Normative Verweise

{Framework-specific references}

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initiale Version |

<!-- 
Dieses Dokument ist Teil des {Framework}-Handbuchs und unterliegt der Dokumentenlenkung.
Template-Version: 1.0 - Revision: 0
-->
```

## Required Fields Reference

### Field Descriptions

| Field | Type | Description | Example Value |
|-------|------|-------------|---------------|
| `document_id` | String | Document identifier | "0000" |
| `owner` | Placeholder | Document owner | `{{ meta.owner }}` |
| `version` | Placeholder | Document version | `{{ meta.version }}` |
| `status` | Placeholder | Document status (Draft/Final/Approved) | `{{ meta.status }}` |
| `classification` | Placeholder | Security classification | `{{ meta.classification }}` |
| `date` | Placeholder | Last update date | `{{ meta.date }}` |
| `template_version` | String | Template format version | "1.0" |
| `revision` | Integer | Customization revision number | "0" |
| `organization` | Placeholder | Organization name | `{{ meta.organization }}` |
| `author` | Placeholder | Document author | `{{ meta.author }}` |
| `scope` | Placeholder | Applicability scope | `{{ meta.scope }}` |
| `valid_from` | Placeholder | Validity start date | `{{ meta.valid_from }}` |
| `next_review` | Placeholder | Next review date | `{{ meta.next_review }}` |

### Placeholder Format

All placeholders follow the format: `{{ source.field }}`

**Common sources:**
- `meta` - Metadata from metadata.yaml configuration
- `netbox` - Data from NetBox integration
- `custom` - Custom data sources

## Complete Examples

### GDPR Example

**File:** `templates/de/gdpr/0000_metadata_de_gdpr.md`

```markdown
# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbuch-Informationen

**Handbuch-Titel:** GDPR Compliance Handbuch  
**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  

---

## Dokumentenzweck

Dieses Handbuch dokumentiert die Datenschutzmaßnahmen und -prozesse der Organisation gemäß der Datenschutz-Grundverordnung (DSGVO/GDPR - EU 2016/679). Es dient als zentrale Dokumentation für:

- Verarbeitungstätigkeiten personenbezogener Daten
- Technische und organisatorische Maßnahmen (TOMs)
- Betroffenenrechte und deren Umsetzung
- Datenschutz-Folgenabschätzungen (DSFA)
- Meldepflichten bei Datenschutzverletzungen

## Geltungsbereich

Dieses Handbuch gilt für:
- Alle Verarbeitungstätigkeiten personenbezogener Daten
- Alle Mitarbeiter, Auftragsverarbeiter und Drittanbieter
- Alle Standorte und Systeme der Organisation
- Alle Geschäftsprozesse mit Personenbezug

## Normative Verweise

- Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung - DSGVO)
- Bundesdatenschutzgesetz (BDSG)
- Telekommunikation-Telemedien-Datenschutz-Gesetz (TTDSG)
- Leitlinien der Europäischen Datenschutzkonferenz (EDSA)

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initiale Version |

<!-- 
Dieses Dokument ist Teil des GDPR-Handbuchs und unterliegt der Dokumentenlenkung.
Template-Version: 1.0 - Revision: 0
-->
```

### ISO 9001 Example

**File:** `templates/de/iso-9001/0000_metadata_de_iso-9001.md`

```markdown
# ISO 9001 Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbuch-Informationen

**Handbuch-Titel:** Qualitätsmanagementsystem nach ISO 9001:2015  
**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  

---

## Dokumentenzweck

Dieses Handbuch dokumentiert das Qualitätsmanagementsystem (QMS) der Organisation gemäß ISO 9001:2015. Es beschreibt:

- Kontext der Organisation und interessierte Parteien
- Qualitätspolitik und Qualitätsziele
- Prozesslandschaft und Prozessinteraktionen
- Verantwortlichkeiten und Befugnisse
- Ressourcenmanagement und Kompetenzanforderungen
- Betriebliche Planung und Steuerung
- Leistungsbewertung und Verbesserung

## Geltungsbereich

Das QMS gilt für:
- Alle Geschäftsprozesse der Organisation
- Alle Standorte und Organisationseinheiten
- Alle Produkte und Dienstleistungen
- Alle Mitarbeiter und relevante externe Anbieter

## Normative Verweise

- ISO 9001:2015 (Quality Management Systems - Requirements)
- ISO 9000:2015 (Quality Management - Fundamentals and vocabulary)
- ISO 9004:2018 (Quality Management - Quality of an organization - Guidance)
- ISO 19011:2018 (Guidelines for auditing management systems)

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initiale Version |

<!-- 
Dieses Dokument ist Teil des ISO 9001-Handbuchs und unterliegt der Dokumentenlenkung.
Template-Version: 1.0 - Revision: 0
-->
```

### NIST 800-53 Example

**File:** `templates/en/nist-800-53/0000_metadata_en_nist-800-53.md`

```markdown
# NIST 800-53 Handbook - Metadata

**Document-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Classification:** {{ meta.classification }}  
**Last Updated:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbook Information

**Handbook Title:** NIST SP 800-53 Security and Privacy Controls  
**Organization:** {{ meta.organization }}  
**Author:** {{ meta.author }}  
**Scope:** {{ meta.scope }}  
**Valid From:** {{ meta.valid_from }}  
**Next Review:** {{ meta.next_review }}  

---

## Document Purpose

This handbook documents the implementation of security and privacy controls based on NIST Special Publication 800-53 Revision 5. It provides:

- Control selection and tailoring methodology
- Control implementation statements
- Assessment procedures and evidence
- Continuous monitoring approach
- Control inheritance and shared responsibility
- Privacy controls and privacy impact assessments

## Scope

This handbook applies to:
- All information systems and assets
- All organizational personnel and contractors
- All locations and facilities
- Federal information and information systems
- Privacy programs and personally identifiable information (PII)

## Normative References

- NIST SP 800-53 Rev. 5 (Security and Privacy Controls for Information Systems and Organizations)
- NIST SP 800-53A Rev. 5 (Assessing Security and Privacy Controls)
- NIST SP 800-53B (Control Baselines for Information Systems and Organizations)
- NIST SP 800-37 Rev. 2 (Risk Management Framework)
- FIPS 199 (Standards for Security Categorization)
- FIPS 200 (Minimum Security Requirements)

## Change History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initial Version |

<!-- 
This document is part of the NIST 800-53 handbook and is subject to document control.
Template-Version: 1.0 - Revision: 0
-->
```

### PCI-DSS Example

**File:** `templates/de/pci-dss/0000_metadata_de_pci-dss.md`

```markdown
# PCI-DSS Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbuch-Informationen

**Handbuch-Titel:** PCI-DSS v4.0 Compliance Handbuch  
**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  

---

## Dokumentenzweck

Dieses Handbuch dokumentiert die Umsetzung der Payment Card Industry Data Security Standard (PCI-DSS) Version 4.0 Anforderungen. Es umfasst:

- Karteninhaberdaten-Umgebung (CDE) Definition
- Netzwerksegmentierung und Scoping
- Sicherheitskontrollen für die 12 PCI-DSS Anforderungen
- Kompensationskontrollen und Ausnahmen
- Jährliche Assessments und Reporting
- Incident Response für Kartendaten-Kompromittierungen

## Geltungsbereich

Dieses Handbuch gilt für:
- Alle Systeme, die Karteninhaberdaten speichern, verarbeiten oder übertragen
- Alle Systeme in der Karteninhaberdaten-Umgebung (CDE)
- Alle verbundenen Systeme und Netzwerksegmente
- Alle Mitarbeiter mit Zugriff auf Karteninhaberdaten
- Alle Dienstleister mit Zugriff auf die CDE

## Normative Verweise

- PCI Data Security Standard (PCI-DSS) v4.0
- PCI DSS Requirements and Testing Procedures v4.0
- PA-DSS (Payment Application Data Security Standard)
- PCI Point-to-Point Encryption (P2PE) Standard
- PCI Token Service Provider (TSP) Standard

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initiale Version |

<!-- 
Dieses Dokument ist Teil des PCI-DSS-Handbuchs und unterliegt der Dokumentenlenkung.
Template-Version: 1.0 - Revision: 0
-->
```

## Before/After Comparison

### Before Standardization

**Old CIS Controls metadata** (minimal):

```markdown
# CIS Controls v8 Hardening Templates - Metadata

**Document ID:** 0000  
**Version:** {{ meta.version }}  
**Last Updated:** {{ meta.date }}  

## Handbook Information

**Title:** CIS Controls v8 Hardening Baselines  
**Organization:** {{ meta.organization }}  

## Purpose

This handbook provides hardening baselines based on CIS Controls v8.
```

**Issues:**
- Missing 10 required fields
- No template version tracking
- No revision number
- Incomplete structure
- No normative references
- No change history

### After Standardization

**New CIS Controls metadata** (complete):

```markdown
# CIS Controls Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbuch-Informationen

**Handbuch-Titel:** CIS Controls v8 Hardening Baselines  
**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  

---

## Dokumentenzweck

Dieses Handbuch dokumentiert Hardening-Baselines basierend auf den CIS Controls v8. Es bietet:

- Sicherheitskonfigurationen für Betriebssysteme
- Applikations-Hardening-Richtlinien
- Container- und Cloud-Sicherheitsbaselines
- Compliance-Mapping zu CIS Controls
- Test- und Validierungsverfahren

## Geltungsbereich

Dieses Handbuch gilt für:
- Alle Betriebssysteme (Windows, Linux, macOS)
- Alle Applikationen und Services
- Alle Container und Cloud-Workloads
- Alle Entwicklungs-, Test- und Produktionsumgebungen

## Normative Verweise

- CIS Controls v8 Framework
- CIS Benchmarks für Betriebssysteme
- CIS Benchmarks für Applikationen
- NIST Cybersecurity Framework (CSF)
- ISO/IEC 27001:2022

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initiale Version |

<!-- 
Dieses Dokument ist Teil des CIS Controls-Handbuchs und unterliegt der Dokumentenlenkung.
Template-Version: 1.0 - Revision: 0
-->
```

**Improvements:**
- ✅ All 13 required fields present
- ✅ Template version tracking (1.0)
- ✅ Revision number (0)
- ✅ Complete structure
- ✅ Normative references
- ✅ Change history table
- ✅ Detailed purpose and scope

## Framework-Specific Examples

### BCM (Business Continuity Management)

```markdown
## Dokumentenzweck

Dieses Handbuch dokumentiert das Business Continuity Management (BCM) System der Organisation gemäß ISO 22301 und BSI Standard 100-4. Es umfasst:

- BCM-Strategie und -Politik
- Business Impact Analysen (BIA)
- Risikoanalyse und Notfallszenarien
- Geschäftsfortführungspläne (BCP)
- IT-Wiederanlaufpläne (DRP)
- Krisenmanagement und Kommunikation
- Übungs- und Testprogramm

## Normative Verweise

- ISO 22301:2019 (Business Continuity Management Systems)
- BSI Standard 100-4 (Notfallmanagement)
- ISO 22313:2020 (Guidance on the use of ISO 22301)
```

### ISMS (Information Security Management)

```markdown
## Dokumentenzweck

Dieses Handbuch dokumentiert das Informationssicherheits-Managementsystem (ISMS) der Organisation gemäß ISO/IEC 27001:2022. Es beschreibt:

- ISMS-Kontext und Geltungsbereich
- Informationssicherheitspolitik
- Risikobeurteilung und -behandlung
- Sicherheitskontrollen (Annex A)
- Überwachung und Messung
- Internes Audit und Management Review
- Kontinuierliche Verbesserung

## Normative Verweise

- ISO/IEC 27001:2022 (Information Security Management Systems)
- ISO/IEC 27002:2022 (Information Security Controls)
- ISO/IEC 27005:2022 (Information Security Risk Management)
```

### BSI Grundschutz

```markdown
## Dokumentenzweck

Dieses Handbuch dokumentiert die Umsetzung des BSI IT-Grundschutzes gemäß BSI Standards 200-1, 200-2 und 200-3. Es umfasst:

- Informationsverbund und Strukturanalyse
- Schutzbedarfsfeststellung
- Modellierung und Bausteinzuordnung
- Basis-Sicherheitscheck
- Risikoanalyse nach BSI 200-3
- Sicherheitskonzept und Maßnahmenplan
- Umsetzungssteuerung und Reporting

## Normative Verweise

- BSI Standard 200-1 (Managementsysteme für Informationssicherheit)
- BSI Standard 200-2 (IT-Grundschutz-Methodik)
- BSI Standard 200-3 (Risikoanalyse)
- IT-Grundschutz-Kompendium (aktuelle Edition)
```

### IT-Operation

```markdown
## Dokumentenzweck

Dieses Handbuch dokumentiert den IT-Betrieb der Organisation basierend auf ITIL v4 und ISO/IEC 20000-1. Es beschreibt:

- Service-Katalog und Service Level Agreements
- Incident und Problem Management
- Change und Release Management
- Configuration und Asset Management
- Monitoring und Event Management
- Backup und Recovery Procedures
- Kapazitäts- und Verfügbarkeitsmanagement

## Normative Verweise

- ITIL v4 Framework
- ISO/IEC 20000-1:2018 (Service Management System)
- COBIT 2019 Framework
- ISO/IEC 27001:2022 (für IT-Sicherheit)
```

### Common Criteria

```markdown
## Dokumentenzweck

Dieses Handbuch dokumentiert die Common Criteria Sicherheitsevaluierung gemäß ISO/IEC 15408. Es umfasst:

- Security Target (ST) Struktur
- Protection Profile (PP) Konformität
- Security Functional Requirements (SFR)
- Security Assurance Requirements (SAR)
- TOE Security Functions (TSF)
- Evaluierungsmethodik und Evidence
- Zertifizierungsprozess

## Normative Verweise

- ISO/IEC 15408-1:2009 (Common Criteria Part 1: Introduction)
- ISO/IEC 15408-2:2008 (Common Criteria Part 2: Security Functional Components)
- ISO/IEC 15408-3:2008 (Common Criteria Part 3: Security Assurance Components)
- Common Methodology for IT Security Evaluation (CEM)
```

### HIPAA

```markdown
## Dokumentenzweck

Dieses Handbuch dokumentiert die Umsetzung der HIPAA Security Rule Anforderungen. Es umfasst:

- Administrative Safeguards
- Physical Safeguards
- Technical Safeguards
- Organizational Requirements
- Policies and Procedures
- Documentation Requirements
- Risk Analysis and Risk Management

## Normative Verweise

- Health Insurance Portability and Accountability Act (HIPAA) of 1996
- HIPAA Security Rule (45 CFR Part 164, Subpart C)
- HIPAA Privacy Rule (45 CFR Part 164, Subpart E)
- HITECH Act (Health Information Technology for Economic and Clinical Health)
```

### TSC (Trust Services Criteria)

```markdown
## Dokumentenzweck

Dieses Handbuch dokumentiert die Umsetzung der Trust Services Criteria für SOC 2 Compliance. Es umfasst:

- Security (Common Criteria)
- Availability
- Processing Integrity
- Confidentiality
- Privacy
- Control Environment und Risk Assessment
- Monitoring und Change Management

## Normative Verweise

- AICPA Trust Services Criteria (TSC)
- SOC 2 Reporting Framework
- COSO Internal Control Framework
- ISO/IEC 27001:2022 (für Security Controls)
```

## Using Metadata in Configuration

### metadata.yaml Configuration

```yaml
# Metadata configuration for handbook generation
metadata:
  # Document ownership
  owner: "Chief Information Security Officer"
  
  # Document versioning
  version: "1.0.0"
  status: "Draft"  # Draft, Review, Approved, Final
  
  # Security classification
  classification: "Internal"  # Public, Internal, Confidential, Restricted
  
  # Dates
  date: "2026-02-10"
  valid_from: "2026-03-01"
  next_review: "2027-03-01"
  
  # Organization information
  organization: "Example Corporation"
  author: "Security Team"
  scope: "All organizational information systems and assets"
```

### Generated Output Example

When processed, placeholders are replaced:

```markdown
**Owner:** Chief Information Security Officer  
**Version:** 1.0.0  
**Status:** Draft  
**Klassifizierung:** Internal  
**Letzte Aktualisierung:** 2026-02-10  
**Organisation:** Example Corporation  
**Autor:** Security Team  
**Geltungsbereich:** All organizational information systems and assets  
**Gültig ab:** 2026-03-01  
**Nächste Überprüfung:** 2027-03-01  
```

## Validation

Validate metadata files using the validation script:

```bash
# Validate all frameworks
python helpers/validate_metadata.py --all

# Validate specific framework
python helpers/validate_metadata.py --framework gdpr

# Check bilingual consistency
python helpers/validate_metadata.py --framework iso-9001 --check-bilingual
```

## Best Practices

### 1. Use Consistent Placeholders

Always use the same placeholder names across all frameworks:
- ✅ `{{ meta.owner }}`
- ❌ `{{ metadata.owner }}`
- ❌ `{{ owner }}`

### 2. Maintain Bilingual Consistency

Ensure German and English versions have identical structure:
- Same number of fields
- Same placeholder names
- Same section organization

### 3. Document Framework-Specific Information

Customize the purpose, scope, and references for each framework:
- Be specific about what the handbook covers
- List relevant standards and regulations
- Include framework-specific terminology

### 4. Keep Template Version Consistent

All templates in a framework should have the same template_version:
- Initial release: "1.0"
- Minor updates: "1.1", "1.2", etc.
- Major changes: "2.0", "3.0", etc.

### 5. Initialize Revision to Zero

Always start with revision "0" for new templates:
- Revision tracking is for future functionality
- Will be used for customization tracking
- Keep at "0" until feature is implemented

## Summary

The unified metadata structure provides:
- ✅ Consistency across all 12 frameworks
- ✅ Complete documentation information
- ✅ Version tracking capabilities
- ✅ Bilingual support
- ✅ Placeholder-based customization
- ✅ Comprehensive validation

Use these examples as templates for creating or updating metadata files in your handbook generator.
