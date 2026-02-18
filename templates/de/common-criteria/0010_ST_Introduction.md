# ST Introduction

**Dokument-ID:** 0010
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
Dieses Template definiert die Security Target (ST) Einführung gemäß ISO/IEC 15408-1:2022.
Es stellt Identifikation, Überblick und organisatorische Informationen für das ST bereit.

Anpassung erforderlich:
- Vervollständige alle ST- und TOE-Identifikationsfelder
- Liste alle relevanten Protection Profiles auf, falls zutreffend
- Dokumentiere alle TOE-bezogene Dokumentation
- Stelle Konsistenz mit anderen ST-Abschnitten sicher
- Aktualisiere die Revisionshistorie während der ST-Entwicklung

Referenz: ISO/IEC 15408-1:2022, Abschnitt 8.1 (ST Introduction)
-->

## 1. ST Identification

### 1.1 ST Title
**ST Title:** [TODO: Vollständiger Titel des Security Target]  
**ST Version:** {{ meta-handbook.revision }}  
**ST Date:** {{ meta-handbook.modifydate }}  

### 1.2 ST Author
**Author:** {{ meta-handbook.author }}  
**Organization:** {{ meta-organisation.name }}  
**Contact:** [TODO: Kontaktinformationen]  

### 1.3 TOE Identification
**TOE Name:** [TODO: Name des Target of Evaluation]  
**TOE Version:** [TODO: Version des TOE]  
**TOE Developer:** [TODO: Hersteller/Entwickler]  
**TOE Type:** [TODO: Produkttyp, z.B. Firewall, Smartcard, Operating System]  

## 2. ST Overview

### 2.1 Purpose
Dieses Security Target (ST) beschreibt die Sicherheitseigenschaften von [TODO: TOE Name] gemäß ISO/IEC 15408 (Common Criteria for Information Technology Security Evaluation). Das ST dient als Grundlage für die Evaluierung und Zertifizierung des TOE.

### 2.2 Scope
Das ST umfasst:
- Physische und logische Beschreibung des TOE
- Definition der Sicherheitsprobleme (Bedrohungen, OSPs, Annahmen)
- Sicherheitsziele für TOE und Umgebung
- Sicherheitsanforderungen (SFRs und SARs)
- Zusammenfassung der Sicherheitsfunktionen
- Begründungen (Rationales) für alle Beziehungen

### 2.3 Intended Readership
Dieses ST richtet sich an:
- Evaluatoren und Zertifizierungsstellen
- Produktentwickler und Sicherheitsarchitekten
- Kunden und Beschaffer
- Auditoren und Compliance-Verantwortliche

## 3. ST Reference

### 3.1 ST Identification
**ST Reference:** [TODO: Eindeutige Referenz, z.B. ST-PRODUCT-v1.0]  
**ST Registration:** [TODO: Registrierungsnummer bei Zertifizierungsstelle]  

### 3.2 TOE Reference
**TOE Reference:** [TODO: Eindeutige TOE-Referenz]  
**TOE Platform:** [TODO: Hardware/Software-Plattform]  
**TOE Delivery:** [TODO: Lieferform, z.B. Software-Download, Hardware-Gerät]  

## 4. Document Organization

### 4.1 ST Structure
Das ST ist wie folgt strukturiert:

1. **ST Introduction** (dieses Dokument) - Einführung und Identifikation
2. **TOE Description** - Detaillierte Beschreibung des TOE
3. **Security Problem Definition** - Bedrohungen, OSPs, Annahmen
4. **Security Objectives** - Sicherheitsziele
5. **Security Requirements** - SFRs und SARs
6. **TOE Summary Specification** - Sicherheitsfunktionen
7. **Appendices** - PP-Konformität, Rationales, Glossar

### 4.2 Document Conventions
- **SFR**: Security Functional Requirement (Funktionale Sicherheitsanforderung)
- **SAR**: Security Assurance Requirement (Vertrauenswürdigkeitsanforderung)
- **TOE**: Target of Evaluation (Evaluierungsgegenstand)
- **TSF**: TOE Security Functionality (Sicherheitsfunktionalität des TOE)
- **PP**: Protection Profile (Schutzprofil)
- **EAL**: Evaluation Assurance Level (Evaluierungsstufe)

## 5. Related Documentation

### 5.1 Common Criteria Documentation
- ISO/IEC 15408-1:2022 - Introduction and general model
- ISO/IEC 15408-2:2022 - Security functional components
- ISO/IEC 15408-3:2022 - Security assurance components
- Common Methodology for Information Technology Security Evaluation (CEM)

### 5.2 Protection Profiles
[TODO: Liste relevanter Protection Profiles, falls zutreffend]
- PP Name: [TODO]
- PP Version: [TODO]
- PP Registration: [TODO]

### 5.3 TOE Documentation
[TODO: Liste der TOE-Dokumentation]
- User Guide: [TODO]
- Administrator Guide: [TODO]
- Security Guide: [TODO]
- Installation Guide: [TODO]

## 6. Revision History

| Version | Datum | Autor | Änderungen |
|---------|------|--------|---------|
| [Version] | [Date] | [Author] | Initial version |
| [TODO] | [TODO] | [TODO] | [TODO: Beschreibung der Änderungen] |

**Nächste Schritte:**
1. Vervollständigen Sie alle [TODO]-Platzhalter
2. Überprüfen Sie die Konsistenz mit anderen ST-Abschnitten
3. Stellen Sie sicher, dass alle Referenzen korrekt sind
4. Lassen Sie das Dokument von relevanten Stakeholdern reviewen

