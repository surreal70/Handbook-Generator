# Coverage Matrix (Abdeckungsmatrix)

**Dokument-ID:** 0530
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

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches TOE (Target of Evaluation) an.

<!-- 
ANLEITUNG FÜR TEMPLATE-AUTOREN:
Die Coverage Matrix ist eine zentrale Übersicht, die zeigt, wie alle Sicherheitsanforderungen
durch Sicherheitsfunktionen, Tests und Assurance Measures abgedeckt sind.

WICHTIGE HINWEISE:
- Die Matrix muss vollständig sein - keine Lücken!
- Verwende klare Markierungen (●, ○, ◐) für verschiedene Abdeckungsgrade
- Stelle sicher, dass jede Anforderung mindestens eine Abdeckung hat
- Die Matrix dient als Audit-Trail für die Evaluation
-->

## 1. Einleitung

### 1.1 Zweck

Dieses Dokument enthält die vollständige Coverage Matrix für **[TODO: TOE-Name]**. Die Matrix zeigt die Zuordnung zwischen:

- Security Objectives ↔ Threats, OSPs, Assumptions
- Security Functional Requirements (SFRs) ↔ Security Objectives
- TOE Security Functions (TSFs) ↔ SFRs
- Tests ↔ TSFs und SFRs
- Assurance Measures ↔ Security Assurance Requirements (SARs)

### 1.2 Legende

**Abdeckungsgrade:**
- ● = Vollständige Abdeckung
- ◐ = Teilweise Abdeckung
- ○ = Unterstützende Abdeckung
- (leer) = Keine Abdeckung

## 2. Security Objectives Coverage

### 2.1 Security Objectives for TOE ↔ Threats

Diese Matrix zeigt, wie die Security Objectives for TOE die identifizierten Threats adressieren:

| Threat-ID | Threat-Name | O.TOE-1 | O.TOE-2 | O.TOE-3 | O.TOE-4 | O.TOE-5 |
|-----------|-------------|---------|---------|---------|---------|---------|
| T.[TODO] | [TODO] | ● | | | | |
| T.[TODO] | [TODO] | ● | ● | | | |
| T.[TODO] | [TODO] | | ● | | | |
| T.[TODO] | [TODO] | | | ● | | |
| T.[TODO] | [TODO] | | | ● | ◐ | |

<!-- 
ANLEITUNG:
- Liste alle Threats aus Kapitel 2 (Security Problem Definition) auf
- Liste alle Security Objectives for TOE aus Kapitel 3 auf
- Markiere, welches Objective welche Threat adressiert
- Stelle sicher, dass jede Threat durch mindestens ein Objective abgedeckt ist
-->

**Vollständigkeitsprüfung:**
- Anzahl Threats: [TODO]
- Anzahl abgedeckter Threats: [TODO]
- Nicht abgedeckte Threats: [TODO: Liste oder "Keine"]

### 2.2 Security Objectives for TOE ↔ Organizational Security Policies

Diese Matrix zeigt, wie die Security Objectives for TOE die OSPs erfüllen:

| OSP-ID | OSP-Name | O.TOE-1 | O.TOE-2 | O.TOE-3 | O.TOE-4 | O.TOE-5 |
|--------|----------|---------|---------|---------|---------|---------|
| P.[TODO] | [TODO] | ● | | | | |
| P.[TODO] | [TODO] | | ● | | | |
| P.[TODO] | [TODO] | | | ● | | |

**Vollständigkeitsprüfung:**
- Anzahl OSPs: [TODO]
- Anzahl abgedeckter OSPs: [TODO]
- Nicht abgedeckte OSPs: [TODO: Liste oder "Keine"]

### 2.3 Security Objectives for Environment ↔ Threats

Diese Matrix zeigt, wie die Security Objectives for Environment die Threats adressieren:

| Threat-ID | Threat-Name | O.ENV-1 | O.ENV-2 | O.ENV-3 | O.ENV-4 |
|-----------|-------------|---------|---------|---------|---------|
| T.[TODO] | [TODO] | ● | | | |
| T.[TODO] | [TODO] | | ● | | |
| T.[TODO] | [TODO] | | | ● | |

### 2.4 Security Objectives for Environment ↔ Assumptions

Diese Matrix zeigt, wie die Security Objectives for Environment die Assumptions erfüllen:

| Assumption-ID | Assumption-Name | O.ENV-1 | O.ENV-2 | O.ENV-3 | O.ENV-4 |
|---------------|-----------------|---------|---------|---------|---------|
| A.[TODO] | [TODO] | ● | | | |
| A.[TODO] | [TODO] | | ● | | |
| A.[TODO] | [TODO] | | | ● | |

**Vollständigkeitsprüfung:**
- Anzahl Assumptions: [TODO]
- Anzahl abgedeckter Assumptions: [TODO]
- Nicht abgedeckte Assumptions: [TODO: Liste oder "Keine"]

## 3. Security Functional Requirements Coverage

### 3.1 SFRs ↔ Security Objectives for TOE

Diese Matrix zeigt, wie die SFRs die Security Objectives for TOE erfüllen:

| SFR-ID | SFR-Name | O.TOE-1 | O.TOE-2 | O.TOE-3 | O.TOE-4 | O.TOE-5 |
|--------|----------|---------|---------|---------|---------|---------|
| FAU_GEN.1 | Audit data generation | ● | | | | |
| FAU_SAR.1 | Audit review | ● | | | | |
| FCS_CKM.1 | Cryptographic key generation | | ● | | | |
| FCS_COP.1 | Cryptographic operation | | ● | | | |
| FDP_ACC.1 | Subset access control | | | ● | | |
| FDP_ACF.1 | Security attribute based access control | | | ● | | |
| FIA_UID.1 | Timing of identification | | | | ● | |
| FIA_UAU.1 | Timing of authentication | | | | ● | |
| FIA_AFL.1 | Authentication failure handling | | | | ● | |
| FMT_SMF.1 | Specification of management functions | | | | | ● |
| FMT_SMR.1 | Security roles | | | | | ● |
| FPT_STM.1 | Reliable time stamps | ● | | | | |
| FTA_SSL.1 | TSF-initiated session locking | | | | ● | |
| FTP_TRP.1 | Trusted path | | | | ● | |

<!-- 
ANLEITUNG:
- Liste alle SFRs aus Kapitel 4 (Security Requirements) auf
- Markiere, welche SFR welches Security Objective erfüllt
- Stelle sicher, dass jede SFR mindestens einem Objective zugeordnet ist
- Stelle sicher, dass jedes Objective durch mindestens eine SFR erfüllt wird
-->

**Vollständigkeitsprüfung:**
- Anzahl SFRs: [TODO]
- Anzahl Security Objectives for TOE: [TODO]
- Nicht abgedeckte SFRs: [TODO: Liste oder "Keine"]
- Nicht abgedeckte Objectives: [TODO: Liste oder "Keine"]

## 4. TOE Security Functions Coverage

### 4.1 TSFs ↔ SFRs

Diese Matrix zeigt, wie die TSFs die SFRs implementieren:

| SFR-ID | SFR-Name | TSF-1 | TSF-2 | TSF-3 | TSF-4 | TSF-5 | TSF-6 |
|--------|----------|-------|-------|-------|-------|-------|-------|
| FAU_GEN.1 | Audit data generation | | | ● | | | |
| FAU_SAR.1 | Audit review | | | ● | | | |
| FCS_CKM.1 | Cryptographic key generation | | | | ● | | |
| FCS_COP.1 | Cryptographic operation | | | | ● | | |
| FDP_ACC.1 | Subset access control | | ● | | | | |
| FDP_ACF.1 | Security attribute based access control | | ● | | | | |
| FIA_UID.1 | Timing of identification | ● | | | | | |
| FIA_UAU.1 | Timing of authentication | ● | | | | | |
| FIA_AFL.1 | Authentication failure handling | ● | | | | | |
| FMT_SMF.1 | Specification of management functions | | | | | ● | |
| FMT_SMR.1 | Security roles | | | | | ● | |
| FPT_STM.1 | Reliable time stamps | | | | | | ● |
| FTA_SSL.1 | TSF-initiated session locking | ● | | | | | |
| FTP_TRP.1 | Trusted path | | | | | | ● |

<!-- 
ANLEITUNG:
- Liste alle TSFs aus Kapitel 5 (TOE Summary Specification) auf
- Markiere, welche TSF welche SFR implementiert
- Stelle sicher, dass jede SFR durch mindestens eine TSF abgedeckt ist
- Eine SFR kann durch mehrere TSFs implementiert werden
-->

**TSF-Beschreibungen:**

| TSF-ID | TSF-Name | Beschreibung |
|--------|----------|--------------|
| TSF-1 | [TODO] | [TODO: Kurzbeschreibung] |
| TSF-2 | [TODO] | [TODO: Kurzbeschreibung] |
| TSF-3 | [TODO] | [TODO: Kurzbeschreibung] |
| TSF-4 | [TODO] | [TODO: Kurzbeschreibung] |
| TSF-5 | [TODO] | [TODO: Kurzbeschreibung] |
| TSF-6 | [TODO] | [TODO: Kurzbeschreibung] |

**Vollständigkeitsprüfung:**
- Anzahl SFRs: [TODO]
- Anzahl abgedeckter SFRs: [TODO]
- Nicht abgedeckte SFRs: [TODO: Liste oder "Keine"]

## 5. Test Coverage

### 5.1 Tests ↔ TSFs

Diese Matrix zeigt, wie die Tests die TSFs verifizieren:

| TSF-ID | TSF-Name | Test-1 | Test-2 | Test-3 | Test-4 | Test-5 | Test-6 |
|--------|----------|--------|--------|--------|--------|--------|--------|
| TSF-1 | [TODO] | ● | ● | | | | |
| TSF-2 | [TODO] | | | ● | | | |
| TSF-3 | [TODO] | | | | ● | ● | |
| TSF-4 | [TODO] | | | | | | ● |
| TSF-5 | [TODO] | | ● | | | | |
| TSF-6 | [TODO] | ● | | | | | |

<!-- 
ANLEITUNG:
- Liste alle Tests aus dem Test Plan auf
- Markiere, welcher Test welche TSF verifiziert
- Stelle sicher, dass jede TSF durch mindestens einen Test abgedeckt ist
- Mehrere Tests pro TSF sind empfohlen
-->

**Test-Beschreibungen:**

| Test-ID | Test-Name | Beschreibung | Testtyp |
|---------|-----------|--------------|---------|
| Test-1 | [TODO] | [TODO] | Unit / Integration / System |
| Test-2 | [TODO] | [TODO] | Unit / Integration / System |
| Test-3 | [TODO] | [TODO] | Unit / Integration / System |
| Test-4 | [TODO] | [TODO] | Unit / Integration / System |
| Test-5 | [TODO] | [TODO] | Unit / Integration / System |
| Test-6 | [TODO] | [TODO] | Unit / Integration / System |

**Vollständigkeitsprüfung:**
- Anzahl TSFs: [TODO]
- Anzahl getesteter TSFs: [TODO]
- Nicht getestete TSFs: [TODO: Liste oder "Keine"]

### 5.2 Tests ↔ SFRs (indirekt über TSFs)

Diese Matrix zeigt die indirekte Abdeckung von SFRs durch Tests:

| SFR-ID | SFR-Name | Test-1 | Test-2 | Test-3 | Test-4 | Test-5 | Test-6 |
|--------|----------|--------|--------|--------|--------|--------|--------|
| FAU_GEN.1 | Audit data generation | | | | ● | ● | |
| FAU_SAR.1 | Audit review | | | | ● | ● | |
| FCS_CKM.1 | Cryptographic key generation | | | | | | ● |
| FCS_COP.1 | Cryptographic operation | | | | | | ● |
| FDP_ACC.1 | Subset access control | | | ● | | | |
| FDP_ACF.1 | Security attribute based access control | | | ● | | | |
| FIA_UID.1 | Timing of identification | ● | ● | | | | |
| FIA_UAU.1 | Timing of authentication | ● | ● | | | | |
| FIA_AFL.1 | Authentication failure handling | ● | ● | | | | |
| FMT_SMF.1 | Specification of management functions | | ● | | | | |
| FMT_SMR.1 | Security roles | | ● | | | | |
| FPT_STM.1 | Reliable time stamps | ● | | | | | |
| FTA_SSL.1 | TSF-initiated session locking | ● | ● | | | | |
| FTP_TRP.1 | Trusted path | ● | | | | | |

**Vollständigkeitsprüfung:**
- Anzahl SFRs: [TODO]
- Anzahl getesteter SFRs: [TODO]
- Nicht getestete SFRs: [TODO: Liste oder "Keine"]

## 6. Assurance Measures Coverage

### 6.1 Assurance Measures ↔ SARs

Diese Matrix zeigt, wie die Assurance Measures die SARs erfüllen:

| SAR-ID | SAR-Name | AM-1 | AM-2 | AM-3 | AM-4 | AM-5 | AM-6 |
|--------|----------|------|------|------|------|------|------|
| ACM_CAP.4 | Generation support and acceptance procedures | ● | | | | | |
| ACM_SCP.2 | Problem tracking CM coverage | ● | | | | | |
| ADO_DEL.2 | Detection of modification | | ● | | | | |
| ADO_IGS.1 | Installation, generation, and start-up procedures | | ● | | | | |
| ADV_FSP.2 | Security-enforcing functional specification | | | ● | | | |
| ADV_IMP.1 | Implementation representation of the TSF | | | ● | | | |
| ADV_TDS.2 | Architectural design | | | ● | | | |
| AGD_ADM.1 | Administrator guidance | | | | ● | | |
| AGD_USR.1 | User guidance | | | | ● | | |
| ALC_DVS.1 | Identification of security measures | | | | | ● | |
| ALC_LCD.1 | Developer defined life-cycle model | | | | | ● | |
| ALC_TAT.1 | Well-defined development tools | | | | | ● | |
| ATE_COV.2 | Analysis of coverage | | | | | | ● |
| ATE_DPT.1 | Testing: high-level design | | | | | | ● |
| ATE_FUN.1 | Functional testing | | | | | | ● |
| ATE_IND.2 | Independent testing - sample | | | | | | ● |
| AVA_MSU.2 | Validation of analysis | | | | | | ● |
| AVA_SOF.1 | Strength of TOE security function evaluation | | | | | | ● |
| AVA_VLA.2 | Independent vulnerability analysis | | | | | | ● |

<!-- 
ANLEITUNG:
- Liste alle SARs für das gewählte EAL auf
- Liste alle Assurance Measures aus Kapitel 5 auf
- Markiere, welche Assurance Measure welche SAR erfüllt
- Stelle sicher, dass jede SAR durch mindestens eine Assurance Measure abgedeckt ist
-->

**Assurance Measure Beschreibungen:**

| AM-ID | AM-Name | Beschreibung |
|-------|---------|--------------|
| AM-1 | Configuration Management | [TODO] |
| AM-2 | Delivery and Operation | [TODO] |
| AM-3 | Development Documentation | [TODO] |
| AM-4 | Guidance Documents | [TODO] |
| AM-5 | Life Cycle Support | [TODO] |
| AM-6 | Testing and Vulnerability Assessment | [TODO] |

**Vollständigkeitsprüfung:**
- Anzahl SARs: [TODO]
- Anzahl abgedeckter SARs: [TODO]
- Nicht abgedeckte SARs: [TODO: Liste oder "Keine"]

## 7. Gesamtübersicht

### 7.1 End-to-End Traceability

Diese Übersicht zeigt die vollständige Rückverfolgbarkeit von Threats bis zu Tests:

```
Threats/OSPs/Assumptions
    ↓
Security Objectives (TOE & Environment)
    ↓
Security Functional Requirements (SFRs)
    ↓
TOE Security Functions (TSFs)
    ↓
Tests
```

**Vollständigkeitsprüfung:**
- ✓ Alle Threats sind durch Security Objectives abgedeckt
- ✓ Alle Security Objectives sind durch SFRs erfüllt
- ✓ Alle SFRs sind durch TSFs implementiert
- ✓ Alle TSFs sind durch Tests verifiziert
- ✓ Alle SARs sind durch Assurance Measures erfüllt

### 7.2 Statistik

| Kategorie | Anzahl | Abgedeckt | Abdeckungsgrad |
|-----------|--------|-----------|----------------|
| Threats | [TODO] | [TODO] | [TODO]% |
| OSPs | [TODO] | [TODO] | [TODO]% |
| Assumptions | [TODO] | [TODO] | [TODO]% |
| Security Objectives (TOE) | [TODO] | [TODO] | [TODO]% |
| Security Objectives (ENV) | [TODO] | [TODO] | [TODO]% |
| SFRs | [TODO] | [TODO] | [TODO]% |
| TSFs | [TODO] | [TODO] | [TODO]% |
| Tests | [TODO] | [TODO] | [TODO]% |
| SARs | [TODO] | [TODO] | [TODO]% |
| Assurance Measures | [TODO] | [TODO] | [TODO]% |

### 7.3 Identifizierte Lücken

[TODO: Liste alle identifizierten Lücken in der Abdeckung auf. Wenn keine Lücken existieren, schreibe "Keine Lücken identifiziert".]

| Kategorie | Element | Lücke | Maßnahme |
|-----------|---------|-------|----------|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 8. Zusammenfassung

Die Coverage Matrix demonstriert:

- ✓ Vollständige Rückverfolgbarkeit von Threats bis zu Tests
- ✓ Alle Sicherheitsanforderungen sind abgedeckt
- ✓ Alle Sicherheitsfunktionen sind getestet
- ✓ Alle Assurance Requirements sind erfüllt
- ✓ Keine kritischen Lücken in der Abdeckung

**Status:** [TODO: Vollständig / Mit Lücken / In Bearbeitung]

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [TODO] | [TODO] | Initiale Version |
| 1.0 | [TODO] | [TODO] | [TODO] |

