# Assurance Measures (Sicherungsmaßnahmen)

**Dokument-ID:** 0510  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Intern / Vertraulich / Streng vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches TOE (Target of Evaluation) an.



## 1. Einleitung

### 1.1 Zweck

Dieses Dokument beschreibt die Assurance Measures (Sicherungsmaßnahmen), die implementiert werden, um die Security Assurance Requirements (SARs) für **[TODO: TOE-Name]** zu erfüllen.

Die Assurance Measures demonstrieren, dass:
- Das TOE korrekt entwickelt wurde
- Das TOE angemessen getestet wurde
- Das TOE ordnungsgemäß dokumentiert ist
- Das TOE sicher ausgeliefert und betrieben werden kann

### 1.2 Evaluation Assurance Level

Das TOE wird auf **[TODO: EAL-Level, z.B. EAL4]** evaluiert.



**Begründung für EAL-Wahl:**
[TODO: Erkläre, warum dieses EAL für das TOE angemessen ist. Berücksichtige:
- Die Bedrohungslandschaft
- Die Kritikalität des TOE
- Die Anforderungen der Stakeholder
- Die Kosten-Nutzen-Abwägung]

## 2. Assurance Measures nach SAR-Klassen

### 2.1 Configuration Management (ACM)



#### 2.1.1 ACM_CAP: CM Capabilities

**SAR:** [TODO: z.B. ACM_CAP.4 - Generation support and acceptance procedures]

**Assurance Measure:**

[TODO: Beschreibe die Configuration Management Capabilities. Beispiel:]

Das Projekt verwendet Git als Versionskontrollsystem. Alle TOE-Komponenten (Quellcode, Konfigurationsdateien, Build-Skripte) und Dokumentation sind im Repository versioniert.

**CM-Prozess:**
1. Alle Änderungen werden in Feature-Branches entwickelt
2. Code Reviews sind vor dem Merge erforderlich
3. Automatisierte Tests müssen erfolgreich sein
4. Releases werden mit Git-Tags markiert
5. Jeder Release hat eine eindeutige Versionsnummer

**CM-Tools:**
- Versionskontrolle: Git
- Repository: [TODO: URL]
- Issue Tracking: [TODO: System]
- Build System: [TODO: System]

**Nachweise:**
- CM-Plan: [TODO: Dokumentpfad]
- Repository-Zugriff: [TODO: URL]
- Build-Logs: [TODO: Speicherort]

#### 2.1.2 ACM_SCP: CM Scope

**SAR:** [TODO: z.B. ACM_SCP.2 - Problem tracking CM coverage]

**Assurance Measure:**

[TODO: Beschreibe den Umfang des Configuration Management. Beispiel:]

Das Configuration Management umfasst:
- Alle Quellcode-Dateien des TOE
- Build-Skripte und Konfigurationsdateien
- Security Target und zugehörige Dokumentation
- Test-Suites und Test-Dokumentation
- Evaluations-Artefakte

**CM-Items:**
| Item-ID | Beschreibung | Typ | Repository-Pfad |
|---------|--------------|-----|-----------------|
| [TODO] | [TODO] | Source Code | [TODO] |
| [TODO] | [TODO] | Documentation | [TODO] |
| [TODO] | [TODO] | Test Suite | [TODO] |

**Nachweise:**
- CM-Scope-Dokument: [TODO: Dokumentpfad]
- Configuration Item List: [TODO: Dokumentpfad]

### 2.2 Delivery and Operation (ADO)



#### 2.2.1 ADO_DEL: Delivery

**SAR:** [TODO: z.B. ADO_DEL.2 - Detection of modification]

**Assurance Measure:**

[TODO: Beschreibe die Delivery-Maßnahmen. Beispiel:]

Das TOE wird mit folgenden Sicherheitsmaßnahmen ausgeliefert:

**Integritätsschutz:**
- Alle Releases werden mit SHA-256 gehasht
- Hashes werden auf der offiziellen Website veröffentlicht
- Releases werden digital signiert (GPG/PGP)
- Signaturschlüssel sind über sichere Kanäle verfügbar

**Auslieferungsprozess:**
1. Build des TOE aus versioniertem Quellcode
2. Automatisierte Tests
3. Erstellung von Checksums
4. Digitale Signatur
5. Upload auf sichere Download-Server
6. Veröffentlichung von Checksums und Signaturen

**Nachweise:**
- Delivery Procedures: [TODO: Dokumentpfad]
- Beispiel-Checksums: [TODO: URL]
- Public Key: [TODO: URL]

#### 2.2.2 ADO_IGS: Installation, Generation, and Start-up

**SAR:** [TODO: z.B. ADO_IGS.1 - Installation, generation, and start-up procedures]

**Assurance Measure:**

[TODO: Beschreibe die Installations- und Start-Prozeduren. Beispiel:]

**Installationsanleitung:**
- Detaillierte Schritt-für-Schritt-Anleitung
- Systemvoraussetzungen
- Sicherheitskonfiguration
- Verifikation der Installation

**Nachweise:**
- Installation Guide: [TODO: Dokumentpfad]
- Administrator Guide: [TODO: Dokumentpfad]

### 2.3 Development (ADV)



#### 2.3.1 ADV_FSP: Functional Specification

**SAR:** [TODO: z.B. ADV_FSP.2 - Security-enforcing functional specification]

**Assurance Measure:**

[TODO: Beschreibe die Functional Specification. Beispiel:]

Die Functional Specification beschreibt alle externen Schnittstellen des TOE:

**Dokumentation:**
- TOE Security Functions (TSFs) sind vollständig spezifiziert
- Alle TSF-Schnittstellen sind dokumentiert
- Parameter, Rückgabewerte und Fehlerbehandlung sind beschrieben
- Sicherheitsrelevante Effekte sind dokumentiert

**Nachweise:**
- Functional Specification: [TODO: Dokumentpfad]
- API Documentation: [TODO: Dokumentpfad]

#### 2.3.2 ADV_IMP: Implementation Representation

**SAR:** [TODO: z.B. ADV_IMP.1 - Implementation representation of the TSF]

**Assurance Measure:**

[TODO: Beschreibe die Implementation Representation. Beispiel:]

Der Quellcode des TOE ist verfügbar und dokumentiert:

**Code-Dokumentation:**
- Inline-Kommentare für komplexe Logik
- Funktions- und Klassen-Dokumentation
- Architektur-Dokumentation
- Mapping zwischen Design und Code

**Nachweise:**
- Source Code: [TODO: Repository-URL]
- Code Documentation: [TODO: Dokumentpfad]
- Architecture Document: [TODO: Dokumentpfad]

#### 2.3.3 ADV_TDS: TOE Design

**SAR:** [TODO: z.B. ADV_TDS.2 - Architectural design]

**Assurance Measure:**

[TODO: Beschreibe das TOE Design. Beispiel:]

Das TOE-Design ist auf mehreren Abstraktionsebenen dokumentiert:

**Design-Dokumentation:**
- High-Level Architecture
- Subsystem-Design
- Modul-Design
- Sicherheitsarchitektur

**Nachweise:**
- TOE Design Document: [TODO: Dokumentpfad]
- Architecture Diagrams: [TODO: Dokumentpfad]

### 2.4 Guidance Documents (AGD)



#### 2.4.1 AGD_ADM: Administrator Guidance

**SAR:** [TODO: z.B. AGD_ADM.1 - Administrator guidance]

**Assurance Measure:**

[TODO: Beschreibe die Administrator Guidance. Beispiel:]

**Administrator-Dokumentation umfasst:**
- Sichere Installation und Konfiguration
- Sicherheitsparameter und deren Bedeutung
- Wartung und Updates
- Audit-Log-Verwaltung
- Backup und Recovery
- Incident Response

**Nachweise:**
- Administrator Guide: [TODO: Dokumentpfad]
- Security Configuration Guide: [TODO: Dokumentpfad]

#### 2.4.2 AGD_USR: User Guidance

**SAR:** [TODO: z.B. AGD_USR.1 - User guidance]

**Assurance Measure:**

[TODO: Beschreibe die User Guidance. Beispiel:]

**Benutzer-Dokumentation umfasst:**
- Sichere Nutzung des TOE
- Sicherheitsfunktionen und deren Verwendung
- Sicherheitshinweise und Warnungen
- Verantwortlichkeiten der Benutzer

**Nachweise:**
- User Guide: [TODO: Dokumentpfad]
- Security User Manual: [TODO: Dokumentpfad]

### 2.5 Life Cycle Support (ALC)



#### 2.5.1 ALC_DVS: Development Security

**SAR:** [TODO: z.B. ALC_DVS.1 - Identification of security measures]

**Assurance Measure:**

[TODO: Beschreibe die Development Security Measures. Beispiel:]

**Sicherheitsmaßnahmen in der Entwicklung:**
- Zugriffskontrolle auf Entwicklungssysteme
- Sichere Entwicklungsumgebung
- Code Review-Prozess
- Security Testing während der Entwicklung
- Vertraulichkeitsvereinbarungen für Entwickler

**Nachweise:**
- Development Security Policy: [TODO: Dokumentpfad]
- Access Control Matrix: [TODO: Dokumentpfad]

#### 2.5.2 ALC_LCD: Life Cycle Definition

**SAR:** [TODO: z.B. ALC_LCD.1 - Developer defined life-cycle model]

**Assurance Measure:**

[TODO: Beschreibe das Life Cycle Model. Beispiel:]

**Entwicklungslebenszyklus:**
1. Requirements Analysis
2. Design
3. Implementation
4. Testing
5. Release
6. Maintenance

**Nachweise:**
- Life Cycle Model Document: [TODO: Dokumentpfad]
- Development Process Description: [TODO: Dokumentpfad]

#### 2.5.3 ALC_TAT: Tools and Techniques

**SAR:** [TODO: z.B. ALC_TAT.1 - Well-defined development tools]

**Assurance Measure:**

[TODO: Beschreibe die verwendeten Tools und Techniken. Beispiel:]

**Entwicklungs-Tools:**
| Tool | Version | Zweck | Sicherheitsrelevanz |
|------|---------|-------|---------------------|
| [TODO] | [TODO] | [TODO] | [TODO] |

**Nachweise:**
- Tools and Techniques Document: [TODO: Dokumentpfad]

### 2.6 Tests (ATE)



#### 2.6.1 ATE_COV: Coverage

**SAR:** [TODO: z.B. ATE_COV.2 - Analysis of coverage]

**Assurance Measure:**

[TODO: Beschreibe die Test Coverage. Beispiel:]

**Test-Abdeckung:**
- Alle TSF-Schnittstellen werden getestet
- Alle SFRs werden durch Tests abgedeckt
- Coverage-Analyse wird durchgeführt

**Test-Coverage-Matrix:**
| TSF-ID | Test-ID | SFR-ID | Coverage |
|--------|---------|--------|----------|
| [TODO] | [TODO] | [TODO] | [TODO]% |

**Nachweise:**
- Test Coverage Report: [TODO: Dokumentpfad]
- Coverage Matrix: [TODO: Dokumentpfad]

#### 2.6.2 ATE_DPT: Depth

**SAR:** [TODO: z.B. ATE_DPT.1 - Testing: high-level design]

**Assurance Measure:**

[TODO: Beschreibe die Test Depth. Beispiel:]

**Test-Tiefe:**
- Unit Tests für einzelne Module
- Integration Tests für Subsysteme
- System Tests für das gesamte TOE
- Security Tests für TSFs

**Nachweise:**
- Test Plan: [TODO: Dokumentpfad]
- Test Results: [TODO: Dokumentpfad]

#### 2.6.3 ATE_FUN: Functional Tests

**SAR:** [TODO: z.B. ATE_FUN.1 - Functional testing]

**Assurance Measure:**

[TODO: Beschreibe die Functional Tests. Beispiel:]

**Funktionale Tests:**
- Alle TSFs werden getestet
- Positive und negative Testfälle
- Grenzwert-Tests
- Fehlerbehandlungs-Tests

**Nachweise:**
- Test Specification: [TODO: Dokumentpfad]
- Test Results: [TODO: Dokumentpfad]

#### 2.6.4 ATE_IND: Independent Testing

**SAR:** [TODO: z.B. ATE_IND.2 - Independent testing - sample]

**Assurance Measure:**

[TODO: Beschreibe die Independent Testing Measures. Beispiel:]

**Unabhängige Tests:**
- Evaluator führt eine Auswahl von Tests durch
- Evaluator kann eigene Tests entwickeln
- Testumgebung wird bereitgestellt

**Nachweise:**
- Test Environment Description: [TODO: Dokumentpfad]
- Sample Test Results: [TODO: Dokumentpfad]

### 2.7 Vulnerability Assessment (AVA)



#### 2.7.1 AVA_MSU: Misuse

**SAR:** [TODO: z.B. AVA_MSU.2 - Validation of analysis]

**Assurance Measure:**

[TODO: Beschreibe die Misuse Analysis. Beispiel:]

**Misuse-Analyse:**
- Analyse von Fehlkonfigurationen
- Analyse von unsicherer Nutzung
- Dokumentation von Sicherheitshinweisen

**Nachweise:**
- Misuse Analysis: [TODO: Dokumentpfad]
- Security Warnings: [TODO: Dokumentpfad]

#### 2.7.2 AVA_SOF: Strength of Function

**SAR:** [TODO: z.B. AVA_SOF.1 - Strength of TOE security function evaluation]

**Assurance Measure:**

[TODO: Beschreibe die SOF Evaluation. Beispiel:]

**SOF-Evaluation:**
- Analyse aller probabilistischen Mechanismen
- Berechnung der Angriffsstärke
- Vergleich mit SOF-Claim

**Nachweise:**
- SOF Analysis: [TODO: Dokumentpfad, siehe 0540_Strength_of_Function.md]

#### 2.7.3 AVA_VLA: Vulnerability Analysis

**SAR:** [TODO: z.B. AVA_VLA.2 - Independent vulnerability analysis]

**Assurance Measure:**

[TODO: Beschreibe die Vulnerability Analysis. Beispiel:]

**Vulnerability-Analyse:**
- Analyse bekannter Schwachstellen
- Penetration Testing
- Code-Analyse auf Sicherheitslücken
- Analyse öffentlicher Vulnerability Databases

**Nachweise:**
- Vulnerability Analysis Report: [TODO: Dokumentpfad]
- Penetration Test Results: [TODO: Dokumentpfad]

## 3. Zusammenfassung der Assurance Measures

### 3.1 Vollständigkeitsprüfung

Die folgende Tabelle zeigt die Zuordnung aller SARs zu Assurance Measures:

| SAR-ID | SAR-Name | Assurance Measure | Status |
|--------|----------|-------------------|--------|
| [TODO] | [TODO]   | [TODO]            | ✓      |
| [TODO] | [TODO]   | [TODO]            | ✓      |

**Zusammenfassung:**
- Anzahl der SARs: [TODO]
- Anzahl der abgedeckten SARs: [TODO]
- Abdeckungsgrad: [TODO]%

### 3.2 Nachweise und Artefakte

Die folgenden Dokumente und Artefakte dienen als Nachweise für die Assurance Measures:

| Dokument | Typ | Speicherort | SAR-Zuordnung |
|----------|-----|-------------|---------------|
| [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Evaluator-Aktivitäten

### 4.1 Erforderliche Evaluator-Aktivitäten

Für jede SAR sind spezifische Evaluator-Aktivitäten erforderlich:

[TODO: Liste die Evaluator-Aktivitäten für jede SAR auf. Beispiel:]

**ACM_CAP.4:**
- Prüfung des CM-Systems
- Verifikation der Versionskontrolle
- Prüfung der Acceptance Procedures

**ADV_FSP.2:**
- Review der Functional Specification
- Verifikation der TSF-Beschreibungen
- Prüfung der Vollständigkeit

### 4.2 Bereitstellung von Nachweisen

Alle erforderlichen Nachweise werden dem Evaluator bereitgestellt:

**Bereitstellungsmethode:**
- [TODO: z.B. Secure File Transfer, Evaluator Portal, etc.]

**Zugriff auf Systeme:**
- [TODO: Beschreibe, wie der Evaluator Zugriff auf Entwicklungssysteme, Test-Umgebungen, etc. erhält]

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [TODO] | [TODO] | Initiale Version |
| 1.0 | [TODO] | [TODO] | [TODO] |
