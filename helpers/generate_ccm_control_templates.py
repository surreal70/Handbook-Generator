#!/usr/bin/env python3
"""
CSA CCM Control Template Generator

This script generates individual template files for each CSA CCM v4.0 control.
It creates both German and English versions with consistent structure.

Usage:
    python helpers/generate_ccm_control_templates.py

Author: Andreas Huemmer
Copyright (c) 2025, 2026
"""

import os
from pathlib import Path

# CCM v4.0 Control Definitions
CCM_CONTROLS = {
    "AIS": {
        "name_de": "Application & Interface Security",
        "name_en": "Application & Interface Security",
        "controls": [
            ("AIS-01", "Application Security", "Anwendungssicherheit"),
            ("AIS-02", "Secure Design & Development", "Sichere Entwicklung"),
            ("AIS-03", "Application Security Testing", "Anwendungssicherheitstests"),
            ("AIS-04", "Application Security Monitoring", "Anwendungssicherheitsüberwachung"),
        ]
    },
    "AAC": {
        "name_de": "Audit Assurance & Compliance",
        "name_en": "Audit Assurance & Compliance",
        "controls": [
            ("AAC-01", "Audit Assurance & Compliance", "Audit-Sicherheit und Compliance"),
            ("AAC-02", "Audit Planning", "Audit-Planung"),
            ("AAC-03", "Independent Audits", "Unabhängige Audits"),
            ("AAC-04", "Audit Logging / Intrusion Detection", "Audit-Protokollierung"),
            ("AAC-05", "Audit Tools Access", "Zugriff auf Audit-Tools"),
        ]
    },
    "BCR": {
        "name_de": "Business Continuity Management & Operational Resilience",
        "name_en": "Business Continuity Management & Operational Resilience",
        "controls": [
            ("BCR-01", "Business Continuity Management", "Geschäftskontinuitätsmanagement"),
            ("BCR-02", "Business Continuity Planning", "Geschäftskontinuitätsplanung"),
            ("BCR-03", "Business Continuity Testing", "Geschäftskontinuitätstests"),
            ("BCR-04", "Environmental Risks", "Umweltrisiken"),
            ("BCR-05", "Equipment Location", "Gerätestandort"),
            ("BCR-06", "Equipment Maintenance", "Gerätewartung"),
            ("BCR-07", "Equipment Power Failures", "Stromausfälle"),
            ("BCR-08", "Impact Analysis", "Auswirkungsanalyse"),
            ("BCR-09", "Policy", "Richtlinie"),
            ("BCR-10", "Retention Policy", "Aufbewahrungsrichtlinie"),
        ]
    },
    "CCC": {
        "name_de": "Change Control & Configuration Management",
        "name_en": "Change Control & Configuration Management",
        "controls": [
            ("CCC-01", "Change Control & Configuration Management", "Änderungssteuerung"),
            ("CCC-02", "Change Detection", "Änderungserkennung"),
            ("CCC-03", "Change Management", "Änderungsmanagement"),
            ("CCC-04", "Configuration Management", "Konfigurationsmanagement"),
            ("CCC-05", "New Development / Acquisition", "Neue Entwicklung"),
            ("CCC-06", "Outsourced Development", "Ausgelagerte Entwicklung"),
            ("CCC-07", "Production Changes", "Produktionsänderungen"),
            ("CCC-08", "Quality Testing", "Qualitätstests"),
            ("CCC-09", "Unauthorized Software Installations", "Unerlaubte Software"),
        ]
    },
    "DSP": {
        "name_de": "Data Security & Privacy",
        "name_en": "Data Security & Privacy",
        "controls": [
            ("DSP-01", "Data Inventory / Flows", "Dateninventar"),
            ("DSP-02", "Data Security / Integrity", "Datensicherheit"),
            ("DSP-03", "Data Classification", "Datenklassifizierung"),
            ("DSP-04", "Data Retention / Deletion", "Datenaufbewahrung"),
            ("DSP-05", "Data Encryption at Rest", "Verschlüsselung im Ruhezustand"),
            ("DSP-06", "Data Encryption in Transit", "Verschlüsselung bei Übertragung"),
            ("DSP-07", "Data Loss Prevention", "Datenverlustprävention"),
            ("DSP-08", "Privacy", "Datenschutz"),
        ]
    },
    "DCS": {
        "name_de": "Datacenter Security",
        "name_en": "Datacenter Security",
        "controls": [
            ("DCS-01", "Datacenter Security", "Rechenzentrumssicherheit"),
            ("DCS-02", "Controlled Access Points", "Kontrollierte Zugangspunkte"),
            ("DCS-03", "Equipment Identification", "Geräteidentifikation"),
            ("DCS-04", "Off-Site Authorization", "Externe Autorisierung"),
            ("DCS-05", "Off-Site Equipment", "Externe Geräte"),
            ("DCS-06", "Physical Security - Perimeter", "Physische Sicherheit"),
            ("DCS-07", "Secure Area Authorization", "Sichere Bereichsautorisierung"),
            ("DCS-08", "Unauthorized Persons Entry", "Unbefugter Zutritt"),
        ]
    },
    "EKM": {
        "name_de": "Encryption & Key Management",
        "name_en": "Encryption & Key Management",
        "controls": [
            ("EKM-01", "Encryption & Key Management", "Verschlüsselung und Schlüsselverwaltung"),
            ("EKM-02", "Entitlement", "Berechtigung"),
            ("EKM-03", "Key Generation", "Schlüsselerzeugung"),
            ("EKM-04", "Sensitive Data Protection", "Schutz sensibler Daten"),
        ]
    },
    "GRC": {
        "name_de": "Governance, Risk & Compliance",
        "name_en": "Governance, Risk & Compliance",
        "controls": [
            ("GRC-01", "Baseline Requirements", "Baseline-Anforderungen"),
            ("GRC-02", "Governance Oversight", "Governance-Aufsicht"),
            ("GRC-03", "Risk Management Program", "Risikomanagement-Programm"),
            ("GRC-04", "Policy", "Richtlinie"),
            ("GRC-05", "Policy Enforcement", "Richtliniendurchsetzung"),
            ("GRC-06", "Policy Impact on Risk Assessments", "Richtlinienauswirkungen"),
            ("GRC-07", "Policy Reviews", "Richtlinienüberprüfungen"),
        ]
    },
    "HRS": {
        "name_de": "Human Resources",
        "name_en": "Human Resources",
        "controls": [
            ("HRS-01", "Human Resources Security", "Personalwesen-Sicherheit"),
            ("HRS-02", "Asset Returns", "Rückgabe von Vermögenswerten"),
            ("HRS-03", "Background Screening", "Hintergrundüberprüfungen"),
            ("HRS-04", "Employment Agreements", "Arbeitsverträge"),
            ("HRS-05", "Employment Termination", "Beendigung des Arbeitsverhältnisses"),
            ("HRS-06", "Mobile Device Management", "Mobile Geräteverwaltung"),
            ("HRS-07", "Non-Disclosure Agreements", "Vertraulichkeitsvereinbarungen"),
            ("HRS-08", "Roles / Responsibilities", "Rollen und Verantwortlichkeiten"),
            ("HRS-09", "Training / Awareness", "Schulung und Bewusstsein"),
            ("HRS-10", "User Responsibility", "Benutzerverantwortung"),
            ("HRS-11", "Workspace", "Arbeitsplatz"),
        ]
    },
    "IAM": {
        "name_de": "Identity & Access Management",
        "name_en": "Identity & Access Management",
        "controls": [
            ("IAM-01", "Identity & Access Management", "Identitäts- und Zugriffsmanagement"),
            ("IAM-02", "Credential Lifecycle / Provision Management", "Credential-Lebenszyklus"),
            ("IAM-03", "Authentication & Authorization", "Authentifizierung und Autorisierung"),
            ("IAM-04", "Privileged User & Access Management", "Privilegiertes Zugriffsmanagement"),
            ("IAM-05", "User Access Reviews", "Benutzerzugriffsprüfungen"),
            ("IAM-06", "User Access Revocation", "Benutzerzugriffswiderruf"),
            ("IAM-07", "User Access Policy", "Benutzerzugriffsrichtlinie"),
            ("IAM-08", "User ID Credentials", "Benutzer-ID-Anmeldeinformationen"),
        ]
    },
    "IVS": {
        "name_de": "Infrastructure & Virtualization Security",
        "name_en": "Infrastructure & Virtualization Security",
        "controls": [
            ("IVS-01", "Infrastructure & Virtualization Security", "Infrastruktur- und Virtualisierungssicherheit"),
            ("IVS-02", "Network Security", "Netzwerksicherheit"),
            ("IVS-03", "Network Security Management", "Netzwerksicherheitsmanagement"),
            ("IVS-04", "Perimeter Security", "Perimetersicherheit"),
            ("IVS-05", "Wireless Security", "Drahtlose Sicherheit"),
            ("IVS-06", "OS Hardening and Base Controls", "OS-Härtung"),
            ("IVS-07", "Production / Non-Production Environments", "Produktions-/Nicht-Produktionsumgebungen"),
            ("IVS-08", "Segmentation", "Segmentierung"),
            ("IVS-09", "Virtualization Security", "Virtualisierungssicherheit"),
        ]
    },
    "IPY": {
        "name_de": "Interoperability & Portability",
        "name_en": "Interoperability & Portability",
        "controls": [
            ("IPY-01", "Interoperability & Portability", "Interoperabilität und Portabilität"),
            ("IPY-02", "APIs", "APIs"),
            ("IPY-03", "Data Request", "Datenanforderung"),
            ("IPY-04", "Policy & Legal", "Richtlinien und Recht"),
            ("IPY-05", "Standardized Network Protocols", "Standardisierte Netzwerkprotokolle"),
        ]
    },
    "MOS": {
        "name_de": "Mobile Security",
        "name_en": "Mobile Security",
        "controls": [
            ("MOS-01", "Mobile Security", "Mobile Sicherheit"),
            ("MOS-02", "Anti-Malware", "Anti-Malware"),
            ("MOS-03", "Application Stores", "Anwendungsstores"),
            ("MOS-04", "Approved Applications", "Genehmigte Anwendungen"),
            ("MOS-05", "Approved Software", "Genehmigte Software"),
            ("MOS-06", "Device Eligibility", "Geräteberechtigung"),
            ("MOS-07", "Device Inventory", "Geräteinventar"),
            ("MOS-08", "Device Management", "Geräteverwaltung"),
            ("MOS-09", "Jailbreaking and Rooting", "Jailbreaking und Rooting"),
            ("MOS-10", "OS Versions", "OS-Versionen"),
            ("MOS-11", "Remote Wipe", "Fernlöschung"),
            ("MOS-12", "Security Patches", "Sicherheitspatches"),
            ("MOS-13", "User Awareness", "Benutzerbewusstsein"),
        ]
    },
    "SEF": {
        "name_de": "Security Incident Management",
        "name_en": "Security Incident Management",
        "controls": [
            ("SEF-01", "Security Incident Management", "Sicherheitsvorfallmanagement"),
            ("SEF-02", "Incident Response Plan", "Incident-Response-Plan"),
            ("SEF-03", "Incident Response Metrics", "Incident-Response-Metriken"),
            ("SEF-04", "Incident Response Testing", "Incident-Response-Tests"),
        ]
    },
    "SCM": {
        "name_de": "Supply Chain Management",
        "name_en": "Supply Chain Management",
        "controls": [
            ("SCM-01", "Supply Chain Management", "Lieferkettenmanagement"),
            ("SCM-02", "Supply Chain Agreements", "Lieferkettenvereinbarungen"),
            ("SCM-03", "Supply Chain Metrics", "Lieferketten-Metriken"),
            ("SCM-04", "Third Party Assessment", "Drittanbieterbewertung"),
        ]
    },
    "TVM": {
        "name_de": "Threat & Vulnerability Management",
        "name_en": "Threat & Vulnerability Management",
        "controls": [
            ("TVM-01", "Threat & Vulnerability Management", "Bedrohungs- und Schwachstellenmanagement"),
            ("TVM-02", "Vulnerability / Patch Management", "Schwachstellen-/Patch-Management"),
            ("TVM-03", "Mobile Code", "Mobiler Code"),
        ]
    },
}


def generate_control_template(domain, control_id, control_name_en, control_name_de, language, base_number):
    """Generate a control template file."""
    
    if language == "de":
        control_name = control_name_de
        template = f"""---
Document-ID: csa-ccm-{base_number:04d}
Owner: {{{{ meta.author }}}}
Version: {{{{ meta.version }}}}
Status: Draft
Classification: Internal
Last Update: {{{{ meta.date }}}}
---

# {control_id}: {control_name}

## CCM-Kontrolle

**Kontrolldomäne**: {CCM_CONTROLS[domain]['name_de']}  
**Kontroll-ID**: {control_id}  
**Kontrollname**: {control_name}

## Kontrollziel

[Beschreiben Sie das Ziel dieser Kontrolle]

## Kontrollbeschreibung

Die Organisation muss:
- [Anforderung 1]
- [Anforderung 2]
- [Anforderung 3]

## Implementierung in {{{{ source.organization_name }}}}

### Aktuelle Implementierung

[Beschreiben Sie, wie diese Kontrolle in Ihrer Organisation implementiert ist]

### Verantwortlichkeiten

| Rolle | Verantwortlichkeit |
|-------|-------------------|
| [Rolle 1] | [Verantwortlichkeit] |
| [Rolle 2] | [Verantwortlichkeit] |

## Kontrollaktivitäten

### 1. [Aktivität 1]

**Prozess**:
- [Schritt 1]
- [Schritt 2]

**Frequenz**: [Frequenz]

### 2. [Aktivität 2]

**Prozess**:
- [Schritt 1]
- [Schritt 2]

**Frequenz**: [Frequenz]

## Nachweise und Evidenzen

### Erforderliche Nachweise

1. **[Nachweis-Kategorie 1]**:
   - [Dokument 1]
   - [Dokument 2]

2. **[Nachweis-Kategorie 2]**:
   - [Dokument 1]
   - [Dokument 2]

## Metriken und KPIs

| Metrik | Zielwert | Messfrequenz |
|--------|----------|--------------|
| [Metrik 1] | [Wert] | [Frequenz] |
| [Metrik 2] | [Wert] | [Frequenz] |

## Risiken und Kontrolllücken

### Identifizierte Risiken

| Risiko | Wahrscheinlichkeit | Auswirkung | Risikoscore | Maßnahme |
|--------|-------------------|------------|-------------|----------|
| [Risiko 1] | [W] | [A] | [Score] | [Maßnahme] |

## Audit-Hinweise

### Audit-Fragen

1. [Frage 1]
2. [Frage 2]
3. [Frage 3]

### Audit-Evidenzen

- [Evidenz 1]
- [Evidenz 2]

## Referenzen

### Interne Dokumente

- [Dokument 1]
- [Dokument 2]

### Externe Standards

- CSA CCM v4.0 - {control_id}
- [Weitere Standards]

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| 1.0 | {{{{ meta.date }}}} | {{{{ meta.author }}}} | Initiale Version |

<!-- Hinweis: Passen Sie diese Kontrolle an Ihre Organisation an -->
"""
    else:  # English
        control_name = control_name_en
        template = f"""---
Document-ID: csa-ccm-{base_number:04d}
Owner: {{{{ meta.author }}}}
Version: {{{{ meta.version }}}}
Status: Draft
Classification: Internal
Last Update: {{{{ meta.date }}}}
---

# {control_id}: {control_name}

## CCM Control

**Control Domain**: {CCM_CONTROLS[domain]['name_en']}  
**Control ID**: {control_id}  
**Control Name**: {control_name}

## Control Objective

[Describe the objective of this control]

## Control Description

The organization must:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

## Implementation in {{{{ source.organization_name }}}}

### Current Implementation

[Describe how this control is implemented in your organization]

### Responsibilities

| Role | Responsibility |
|------|----------------|
| [Role 1] | [Responsibility] |
| [Role 2] | [Responsibility] |

## Control Activities

### 1. [Activity 1]

**Process**:
- [Step 1]
- [Step 2]

**Frequency**: [Frequency]

### 2. [Activity 2]

**Process**:
- [Step 1]
- [Step 2]

**Frequency**: [Frequency]

## Evidence and Artifacts

### Required Evidence

1. **[Evidence Category 1]**:
   - [Document 1]
   - [Document 2]

2. **[Evidence Category 2]**:
   - [Document 1]
   - [Document 2]

## Metrics and KPIs

| Metric | Target Value | Measurement Frequency |
|--------|--------------|----------------------|
| [Metric 1] | [Value] | [Frequency] |
| [Metric 2] | [Value] | [Frequency] |

## Risks and Control Gaps

### Identified Risks

| Risk | Likelihood | Impact | Risk Score | Mitigation |
|------|-----------|--------|------------|------------|
| [Risk 1] | [L] | [I] | [Score] | [Mitigation] |

## Audit Notes

### Audit Questions

1. [Question 1]
2. [Question 2]
3. [Question 3]

### Audit Evidence

- [Evidence 1]
- [Evidence 2]

## References

### Internal Documents

- [Document 1]
- [Document 2]

### External Standards

- CSA CCM v4.0 - {control_id}
- [Additional standards]

## Change History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | {{{{ meta.date }}}} | {{{{ meta.author }}}} | Initial version |

<!-- Note: Customize this control for your organization -->
"""
    
    return template


def main():
    """Generate all CCM control templates."""
    
    base_dir = Path("templates")
    
    # Starting numbers for each domain
    domain_base_numbers = {
        "GRC": 40,   # 0040-0069
        "AIS": 110,  # 0110-0139
        "DSP": 210,  # 0210-0279
        "EKM": 280,  # 0280-0299
        "IAM": 310,  # 0310-0379
        "IVS": 410,  # 0410-0489
        "DCS": 490,  # 0490-0519
        "SEF": 510,  # 0510-0539
        "TVM": 540,  # 0540-0559
        "BCR": 560,  # 0560-0619
        "AAC": 620,  # 0620-0649
        "SCM": 650,  # 0650-0669
        "HRS": 710,  # 0710-0779
        "CCC": 780,  # 0780-0819
        "MOS": 820,  # 0820-0869
        "IPY": 870,  # 0870-0899
    }
    
    total_generated = 0
    
    for domain, domain_data in CCM_CONTROLS.items():
        base_number = domain_base_numbers.get(domain, 900)
        
        for idx, (control_id, control_name_en, control_name_de) in enumerate(domain_data["controls"]):
            current_number = base_number + (idx * 10)
            
            for language in ["de", "en"]:
                # Create directory if it doesn't exist
                lang_dir = base_dir / language / "csa-ccm"
                lang_dir.mkdir(parents=True, exist_ok=True)
                
                # Generate filename
                control_id_clean = control_id.replace("-", "").lower()
                filename = f"{current_number:04d}_{control_id_clean}_{control_name_en.lower().replace(' ', '_').replace('/', '_')}.md"
                filepath = lang_dir / filename
                
                # Generate template content
                content = generate_control_template(
                    domain, control_id, control_name_en, control_name_de, 
                    language, current_number
                )
                
                # Write file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Generated: {filepath}")
                total_generated += 1
    
    print(f"\nTotal templates generated: {total_generated}")
    print(f"Templates per language: {total_generated // 2}")


if __name__ == "__main__":
    main()
