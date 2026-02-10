# Sicherheitsanforderungen (Security Requirements)

**Dokument-ID:** 0400  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Intern / Vertraulich / Streng vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches Target of Evaluation (TOE) an.



## 1. Einleitung

Dieses Kapitel spezifiziert die Sicherheitsanforderungen für das TOE gemäß ISO/IEC 15408 (Common Criteria). Die Sicherheitsanforderungen gliedern sich in:

- **Security Functional Requirements (SFRs)**: Funktionale Sicherheitsanforderungen, die das TOE erfüllen muss
- **Security Assurance Requirements (SARs)**: Vertrauenswürdigkeitsanforderungen für die Evaluierung des TOE

Alle Sicherheitsanforderungen sind aus den in Kapitel 0300 definierten Sicherheitszielen abgeleitet und adressieren die in Kapitel 0200 identifizierten Bedrohungen, organisatorischen Sicherheitsrichtlinien und Annahmen.

## 2. Security Functional Requirements (SFRs)

### 2.1 Übersicht der SFRs

Die folgenden Security Functional Requirements aus ISO/IEC 15408-2 wurden für das TOE ausgewählt:



| SFR-ID | Klasse | Familie | Komponente | Beschreibung |
|--------|--------|---------|------------|--------------|
| [TODO] | [TODO: z.B. FAU] | [TODO: z.B. FAU_GEN] | [TODO: z.B. FAU_GEN.1] | [TODO: Kurzbeschreibung] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 2.2 Security Audit (FAU)



#### FAU_GEN.1 Audit data generation

**Hierarchical to:** Keine  
**Dependencies:** FPT_STM.1 Reliable time stamps

**FAU_GEN.1.1** Das TSF muss in der Lage sein, einen Audit-Datensatz für die folgenden auditierbaren Ereignisse zu erzeugen:
- [assignment: Liste der auditierbaren Ereignisse]
- [TODO: Spezifiziere konkrete Ereignisse]

**FAU_GEN.1.2** Das TSF muss in jedem Audit-Datensatz mindestens die folgenden Informationen aufzeichnen:
- Datum und Uhrzeit des Ereignisses
- Art des Ereignisses
- Subjekt-Identität
- Ergebnis (Erfolg oder Fehler) des Ereignisses
- [assignment: Weitere Audit-relevante Informationen]

### 2.3 Cryptographic Support (FCS)



#### FCS_COP.1 Cryptographic operation

**Hierarchical to:** Keine  
**Dependencies:** 
- FDP_ITC.1 Import of user data without security attributes oder FDP_ITC.2 Import of user data with security attributes oder FCS_CKM.1 Cryptographic key generation

**FCS_COP.1.1** Das TSF muss [assignment: kryptographische Operation] gemäß einem spezifizierten kryptographischen Algorithmus [assignment: kryptographischer Algorithmus] und kryptographischen Schlüssellängen [assignment: Schlüssellängen] durchführen, die [selection: Standards, Regeln, Richtlinien] entsprechen.

[TODO: Spezifiziere konkrete kryptographische Operationen, Algorithmen und Schlüssellängen]

### 2.4 User Data Protection (FDP)



#### FDP_ACC.1 Subset access control

**Hierarchical to:** Keine  
**Dependencies:** FDP_ACF.1 Security attribute based access control

**FDP_ACC.1.1** Das TSF muss [assignment: Zugriffskontrollrichtlinie] auf [assignment: Subjekte, Objekte und Operationen] durchsetzen.

[TODO: Definiere Zugriffskontrollrichtlinie, Subjekte, Objekte und Operationen]

### 2.5 Identification and Authentication (FIA)



#### FIA_UID.1 Timing of identification

**Hierarchical to:** Keine  
**Dependencies:** Keine

**FIA_UID.1.1** Das TSF muss es jedem Benutzer erlauben, sich zu identifizieren, bevor das TSF dem Benutzer erlaubt, andere TSF-vermittelte Aktionen durchzuführen, die [selection: keine anderen Aktionen, [assignment: Liste der TSF-vermittelten Aktionen]] ausschließen.

[TODO: Spezifiziere Ausnahmen, falls vorhanden]

### 2.6 Security Management (FMT)



#### FMT_SMF.1 Specification of Management Functions

**Hierarchical to:** Keine  
**Dependencies:** Keine

**FMT_SMF.1.1** Das TSF muss in der Lage sein, die folgenden Sicherheitsmanagement-Funktionen durchzuführen:
- [assignment: Liste der Sicherheitsmanagement-Funktionen]

[TODO: Liste alle Sicherheitsmanagement-Funktionen auf]

### 2.7 Protection of the TSF (FPT)



#### FPT_STM.1 Reliable time stamps

**Hierarchical to:** Keine  
**Dependencies:** Keine

**FPT_STM.1.1** Das TSF muss in der Lage sein, zuverlässige Zeitstempel für den eigenen Gebrauch bereitzustellen.

### 2.8 TOE Access (FTA)



### 2.9 Trusted Path/Channels (FTP)



### 2.10 Weitere SFR-Klassen



## 3. Security Assurance Requirements (SARs)

### 3.1 Übersicht der SARs

Die Security Assurance Requirements definieren die Vertrauenswürdigkeitsanforderungen für die Evaluierung des TOE. Die SARs sind durch die Auswahl des Evaluation Assurance Level (EAL) bestimmt.

**Gewähltes EAL:** [TODO: z.B. EAL4]

### 3.2 Assurance Class: Security Target Evaluation (ASE)

Die folgenden ASE-Komponenten sind für alle EALs erforderlich:

- **ASE_CCL.1** Conformance claims
- **ASE_ECD.1** Extended components definition
- **ASE_INT.1** ST introduction
- **ASE_OBJ.2** Security objectives
- **ASE_REQ.2** Derived security requirements
- **ASE_SPD.1** Security problem definition
- **ASE_TSS.1** TOE summary specification

[TODO: Passe an gewähltes EAL an]

### 3.3 Assurance Class: Development (ADV)



Für EAL [TODO: X] sind folgende ADV-Komponenten erforderlich:

- **ADV_ARC.1** Security architecture description
- **ADV_FSP.4** Complete functional specification
- **ADV_IMP.1** Implementation representation of the TSF
- **ADV_TDS.3** Basic modular design

[TODO: Passe an gewähltes EAL an]

### 3.4 Assurance Class: Guidance Documents (AGD)



- **AGD_OPE.1** Operational user guidance
- **AGD_PRE.1** Preparative procedures

### 3.5 Assurance Class: Life-cycle Support (ALC)



Für EAL [TODO: X] sind folgende ALC-Komponenten erforderlich:

- **ALC_CMC.4** Production support, acceptance procedures and automation
- **ALC_CMS.4** Problem tracking CM coverage
- **ALC_DEL.1** Delivery procedures
- **ALC_DVS.1** Identification of security measures
- **ALC_LCD.1** Developer defined life-cycle model
- **ALC_TAT.1** Well-defined development tools

[TODO: Passe an gewähltes EAL an]

### 3.6 Assurance Class: Tests (ATE)



- **ATE_COV.2** Analysis of coverage
- **ATE_DPT.1** Testing: high-level design
- **ATE_FUN.1** Functional testing
- **ATE_IND.2** Independent testing - sample

[TODO: Passe an gewähltes EAL an]

### 3.7 Assurance Class: Vulnerability Assessment (AVA)



- **AVA_VAN.3** Focused vulnerability analysis

[TODO: Passe an gewähltes EAL an]

## 4. Security Requirements Rationale

Die Begründung für die Auswahl der Sicherheitsanforderungen wird in Dokument 0420 detailliert dargestellt.

Zusammenfassung:
- Alle SFRs sind aus den Sicherheitszielen für das TOE abgeleitet
- Alle SFR-Abhängigkeiten sind erfüllt (siehe Dokument 0430)
- Die gewählten SARs entsprechen dem Evaluation Assurance Level [TODO: X]
- Die Sicherheitsanforderungen sind vollständig, konsistent und intern widerspruchsfrei

## 5. Operationen auf SFRs

Gemäß ISO/IEC 15408-2 können folgende Operationen auf SFRs durchgeführt werden:

- **Assignment**: Spezifizierung von Parametern (markiert mit [assignment: ...])
- **Selection**: Auswahl aus vorgegebenen Optionen (markiert mit [selection: ...])
- **Refinement**: Verfeinerung der Anforderung (kursiv dargestellt)
- **Iteration**: Mehrfache Verwendung einer Komponente (durch Suffix gekennzeichnet, z.B. FDP_ACC.1/1, FDP_ACC.1/2)

Alle durchgeführten Operationen sind in den SFR-Spezifikationen oben dokumentiert.

## 6. Referenzen

- ISO/IEC 15408-2:2022 - Security functional requirements
- ISO/IEC 15408-3:2022 - Security assurance requirements
- [TODO: Weitere relevante Standards und Spezifikationen]

## 7. Anhänge

### 7.1 SFR-Übersichtstabelle

Eine vollständige Übersicht aller SFRs mit Abhängigkeiten findet sich in Dokument 0430.

### 7.2 SAR-Übersichtstabelle

Eine vollständige Übersicht aller SARs entsprechend dem gewählten EAL findet sich in Dokument 0410.

---

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter
2. Spezifiziere alle Assignments und Selections in den SFRs
3. Verifiziere die Vollständigkeit der SFR-Abhängigkeiten (siehe Dokument 0430)
4. Stelle sicher, dass alle SFRs aus den Sicherheitszielen abgeleitet sind
5. Dokumentiere die Rationale in Dokument 0420
