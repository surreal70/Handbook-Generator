# TOE Physical Scope

**Dokument-ID:** 0100  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
Dieses Template dokumentiert den physischen Umfang des Target of Evaluation (TOE) gemäß ISO/IEC 15408-1:2022.
Es definiert alle physischen Komponenten, Hardware, Software, Firmware und Dokumentation, die Teil des TOE sind.

Anpassung erforderlich:
- Liste alle physischen Komponenten des TOE auf
- Dokumentiere Hardware-Komponenten mit Spezifikationen
- Dokumentiere Software-Komponenten mit Versionen
- Dokumentiere Firmware-Komponenten
- Definiere physische Grenzen und Ausschlüsse
- Erstelle Komponentendiagramme
- Dokumentiere Lieferumfang und Verpackung

Referenz: ISO/IEC 15408-1:2022, Abschnitt 8.2.1 (TOE Physical Scope)
-->

## 1. Physical Components Overview

### 1.1 TOE Physical Composition
Der TOE besteht aus folgenden physischen Komponenten:

| Component ID | Component Name | Type | Version | Description |
|--------------|----------------|------|---------|-------------|
| [TODO: PC-001] | [TODO: Komponentenname] | Hardware/Software/Firmware | [TODO: Version] | [TODO: Beschreibung] |
| [TODO: PC-002] | [TODO: Komponentenname] | Hardware/Software/Firmware | [TODO: Version] | [TODO: Beschreibung] |
| [TODO: PC-003] | [TODO: Komponentenname] | Hardware/Software/Firmware | [TODO: Version] | [TODO: Beschreibung] |

### 1.2 Component Dependencies
[TODO: Beschreibe Abhängigkeiten zwischen physischen Komponenten]

```
[TODO: Komponentenabhängigkeitsdiagramm einfügen]
```

## 2. Hardware Components

### 2.1 Hardware Inventory
**Hardware-Komponenten im TOE:**

| Hardware ID | Name | Manufacturer | Model | Specifications |
|-------------|------|--------------|-------|----------------|
| [TODO: HW-001] | [TODO: Name] | [TODO: Hersteller] | [TODO: Modell] | [TODO: Spezifikationen] |
| [TODO: HW-002] | [TODO: Name] | [TODO: Hersteller] | [TODO: Modell] | [TODO: Spezifikationen] |

### 2.2 Hardware Specifications
**[TODO: Hardware-Komponente 1]**
- Prozessor: [TODO: CPU-Spezifikationen]
- Speicher: [TODO: RAM-Spezifikationen]
- Speichermedien: [TODO: Storage-Spezifikationen]
- Netzwerk: [TODO: Netzwerkschnittstellen]
- Sicherheitsmodule: [TODO: z.B. TPM, HSM, Secure Element]

**[TODO: Hardware-Komponente 2]**
- [TODO: Spezifikationen]

### 2.3 Hardware Security Features
[TODO: Beschreibe hardwarebasierte Sicherheitsfunktionen]
- Secure Boot: [TODO: Beschreibung]
- Hardware-Verschlüsselung: [TODO: Beschreibung]
- Tamper-Schutz: [TODO: Beschreibung]
- Physische Sicherheitsmerkmale: [TODO: Beschreibung]

## 3. Software Components

### 3.1 Software Inventory
**Software-Komponenten im TOE:**

| Software ID | Name | Type | Version | Build | License |
|-------------|------|------|---------|-------|---------|
| [TODO: SW-001] | [TODO: Name] | Application/Service/Library | [TODO: Version] | [TODO: Build] | [TODO: Lizenz] |
| [TODO: SW-002] | [TODO: Name] | Application/Service/Library | [TODO: Version] | [TODO: Build] | [TODO: Lizenz] |

### 3.2 Software Modules
**[TODO: Software-Modul 1]**
- Zweck: [TODO: Beschreibung]
- Programmiersprache: [TODO: z.B. C, C++, Java, Python]
- Größe: [TODO: LOC oder Dateigröße]
- Abhängigkeiten: [TODO: Externe Bibliotheken]

**[TODO: Software-Modul 2]**
- [TODO: Details]

### 3.3 Software Configuration
**Konfigurationsdateien:**
- [TODO: Konfigurationsdatei 1]: [TODO: Zweck]
- [TODO: Konfigurationsdatei 2]: [TODO: Zweck]

**Datenbanken:**
- [TODO: Datenbank 1]: [TODO: Zweck und Schema]

## 4. Firmware Components

### 4.1 Firmware Inventory
**Firmware-Komponenten im TOE:**

| Firmware ID | Name | Target Hardware | Version | Purpose |
|-------------|------|-----------------|---------|---------|
| [TODO: FW-001] | [TODO: Name] | [TODO: Hardware] | [TODO: Version] | [TODO: Zweck] |
| [TODO: FW-002] | [TODO: Name] | [TODO: Hardware] | [TODO: Version] | [TODO: Zweck] |

### 4.2 Firmware Details
**[TODO: Firmware-Komponente 1]**
- Typ: [TODO: z.B. BIOS, UEFI, Embedded Controller]
- Größe: [TODO: Größe in KB/MB]
- Update-Mechanismus: [TODO: Beschreibung]
- Signatur: [TODO: Signiermethode]

### 4.3 Firmware Security
[TODO: Beschreibe Firmware-Sicherheitsmaßnahmen]
- Secure Firmware Update: [TODO]
- Firmware-Integritätsprüfung: [TODO]
- Rollback-Schutz: [TODO]

## 5. Documentation Components

### 5.1 User Documentation
**Im TOE enthaltene Benutzerdokumentation:**
- [TODO: Benutzerhandbuch]: [TODO: Format, Version]
- [TODO: Schnellstartanleitung]: [TODO: Format, Version]
- [TODO: Online-Hilfe]: [TODO: Format, Version]

### 5.2 Administrator Documentation
**Im TOE enthaltene Administratordokumentation:**
- [TODO: Administratorhandbuch]: [TODO: Format, Version]
- [TODO: Installationsanleitung]: [TODO: Format, Version]
- [TODO: Konfigurationshandbuch]: [TODO: Format, Version]
- [TODO: Sicherheitshandbuch]: [TODO: Format, Version]

### 5.3 Security Documentation
**Sicherheitsrelevante Dokumentation:**
- Security Target (ST): [TODO: Version]
- [TODO: Weitere Sicherheitsdokumentation]

## 6. Physical Boundaries

### 6.1 Included Components
**Folgende Komponenten sind im TOE enthalten:**
- [TODO: Komponente 1]: [TODO: Begründung für Einschluss]
- [TODO: Komponente 2]: [TODO: Begründung für Einschluss]
- [TODO: Komponente 3]: [TODO: Begründung für Einschluss]

### 6.2 Excluded Components
**Folgende Komponenten sind NICHT im TOE enthalten:**
- [TODO: Komponente 1]: [TODO: Begründung für Ausschluss]
- [TODO: Komponente 2]: [TODO: Begründung für Ausschluss]
- [TODO: Komponente 3]: [TODO: Begründung für Ausschluss]

### 6.3 Boundary Rationale
[TODO: Erkläre die Begründung für die physischen Grenzen des TOE]

Die physischen Grenzen wurden wie folgt definiert:
- [TODO: Begründung 1]
- [TODO: Begründung 2]
- [TODO: Begründung 3]

## 7. Delivery and Packaging

### 7.1 Delivery Format
**Der TOE wird geliefert als:**
- [TODO: z.B. Physisches Gerät, Software-Download, Container-Image, etc.]

**Liefermedien:**
- [TODO: z.B. USB-Stick, DVD, Download-Link, etc.]

### 7.2 Package Contents
**Das TOE-Paket enthält:**
1. [TODO: Komponente 1]
2. [TODO: Komponente 2]
3. [TODO: Komponente 3]
4. [TODO: Dokumentation]
5. [TODO: Lizenzinformationen]

### 7.3 Integrity Protection
**Integritätsschutz für Lieferung:**
- Digitale Signatur: [TODO: Signaturalgorithmus und Schlüssel]
- Prüfsummen: [TODO: Hash-Algorithmus]
- Versiegelung: [TODO: Physische Versiegelung falls zutreffend]

## 8. Version Control

### 8.1 Component Versions
**Versionskontrolle für TOE-Komponenten:**

| Component | Version | Release Date | Changes |
|-----------|---------|--------------|---------|
| [TODO: Komponente 1] | [TODO: Version] | [TODO: Datum] | [TODO: Änderungen] |
| [TODO: Komponente 2] | [TODO: Version] | [TODO: Datum] | [TODO: Änderungen] |

### 8.2 Version Identification
**Versionserkennung:**
- Methode: [TODO: z.B. About-Dialog, Versionsdatei, CLI-Befehl]
- Befehl: [TODO: z.B. `--version`, `/version`, etc.]
- Ausgabeformat: [TODO: Beispielausgabe]

### 8.3 Configuration Management
**Konfigurationsmanagement:**
- CM-System: [TODO: z.B. Git, SVN, etc.]
- Repository: [TODO: Repository-Informationen]
- Build-System: [TODO: Build-System-Informationen]

## 9. Physical Scope Diagram

### 9.1 Component Diagram
[TODO: Erstelle ein Diagramm, das alle physischen Komponenten und ihre Beziehungen zeigt]

```
[TODO: Komponentendiagramm einfügen]
```

### 9.2 Deployment Diagram
[TODO: Erstelle ein Deployment-Diagramm, das zeigt, wie Komponenten bereitgestellt werden]

```
[TODO: Deployment-Diagramm einfügen]
```

---

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter mit TOE-spezifischen Informationen
2. Erstelle detaillierte Komponentendiagramme
3. Dokumentiere alle Versionen und Build-Informationen
4. Überprüfe die Konsistenz mit dem logischen Umfang (Template 0110)
5. Stelle sicher, dass alle Lieferkomponenten dokumentiert sind

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
