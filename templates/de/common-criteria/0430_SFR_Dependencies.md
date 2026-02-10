# SFR-Abhängigkeiten (SFR Dependencies)

**Dokument-ID:** 0430  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Intern / Vertraulich / Streng vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches Target of Evaluation (TOE) an.

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
This template documents all SFR dependencies and demonstrates their satisfaction.
According to ISO/IEC 15408-2, each SFR may have dependencies on other SFRs that must
be satisfied for the requirement to function correctly.

Key considerations:
- All dependencies must be explicitly identified
- Each dependency must be satisfied by including the required SFR
- If a dependency is not satisfied, a detailed rationale must be provided
- Dependencies are hierarchical - satisfying a higher-level component satisfies lower levels
- Iteration of SFRs must be tracked separately
-->

## 1. Einleitung

Dieses Dokument dokumentiert alle Abhängigkeiten zwischen den Security Functional Requirements (SFRs) des TOE und demonstriert deren Erfüllung. Gemäß ISO/IEC 15408-2 können SFRs Abhängigkeiten zu anderen SFRs haben, die erfüllt sein müssen, damit die Anforderung korrekt funktioniert.

## 2. Übersicht der SFR-Abhängigkeiten

### 2.1 Zusammenfassung

**Statistik:**
- Anzahl der ausgewählten SFRs: [TODO: X]
- Anzahl der SFRs mit Abhängigkeiten: [TODO: X]
- Gesamtzahl der Abhängigkeiten: [TODO: X]
- Anzahl der erfüllten Abhängigkeiten: [TODO: X]
- Anzahl der nicht erfüllten Abhängigkeiten: [TODO: 0]

**Status:** [TODO: ✓ Alle Abhängigkeiten erfüllt / ⚠ Abhängigkeiten nicht erfüllt]

### 2.2 Vollständige Abhängigkeitstabelle

<!-- TODO: Erstelle vollständige Tabelle aller SFRs mit ihren Abhängigkeiten -->

| SFR-ID | SFR-Name | Abhängigkeit | Erfüllt durch | Status | Anmerkungen |
|--------|----------|--------------|---------------|--------|-------------|
| FAU_GEN.1 | Audit data generation | FPT_STM.1 | FPT_STM.1 | ✓ | Zeitstempel für Audit-Einträge |
| FAU_SAR.1 | Audit review | FAU_GEN.1 | FAU_GEN.1 | ✓ | Audit-Daten müssen generiert werden |
| FCS_CKM.1 | Cryptographic key generation | [FCS_CKM.2 oder FCS_COP.1] | FCS_COP.1 | ✓ | Schlüssel für kryptographische Operationen |
| FCS_COP.1 | Cryptographic operation | [FDP_ITC.1 oder FDP_ITC.2 oder FCS_CKM.1] | FCS_CKM.1 | ✓ | Schlüsselgenerierung |
| FDP_ACC.1 | Subset access control | FDP_ACF.1 | FDP_ACF.1 | ✓ | Zugriffskontrollfunktionen |
| FDP_ACF.1 | Security attribute based access control | FDP_ACC.1, FMT_MSA.3 | FDP_ACC.1, FMT_MSA.3 | ✓ | Zugriffskontrollrichtlinie und Attributverwaltung |
| FIA_UAU.1 | Timing of authentication | FIA_UID.1 | FIA_UID.1 | ✓ | Identifikation vor Authentisierung |
| FIA_UID.1 | Timing of identification | Keine | N/A | ✓ | Keine Abhängigkeiten |
| FMT_MSA.1 | Management of security attributes | [FDP_ACC.1 oder FDP_IFC.1], FMT_SMR.1, FMT_SMF.1 | FDP_ACC.1, FMT_SMR.1, FMT_SMF.1 | ✓ | Zugriffskontrolle und Rollenverwaltung |
| FMT_MSA.3 | Static attribute initialisation | FMT_MSA.1, FMT_SMR.1 | FMT_MSA.1, FMT_SMR.1 | ✓ | Attributverwaltung und Rollen |
| FMT_SMF.1 | Specification of Management Functions | Keine | N/A | ✓ | Keine Abhängigkeiten |
| FMT_SMR.1 | Security roles | FIA_UID.1 | FIA_UID.1 | ✓ | Identifikation für Rollenzuweisung |
| FPT_STM.1 | Reliable time stamps | Keine | N/A | ✓ | Keine Abhängigkeiten |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 3. Detaillierte Abhängigkeitsanalyse

### 3.1 Security Audit (FAU)

#### FAU_GEN.1 Audit data generation

**Abhängigkeiten:**
- FPT_STM.1 Reliable time stamps

**Erfüllung:**
FPT_STM.1 ist im Security Target enthalten und stellt zuverlässige Zeitstempel für Audit-Einträge bereit.

**Begründung:**
Audit-Einträge müssen mit präzisen Zeitstempeln versehen werden, um eine chronologische Nachvollziehbarkeit von Sicherheitsereignissen zu gewährleisten.

#### FAU_SAR.1 Audit review

**Abhängigkeiten:**
- FAU_GEN.1 Audit data generation

**Erfüllung:**
FAU_GEN.1 ist im Security Target enthalten und generiert die Audit-Daten, die durch FAU_SAR.1 überprüft werden.

**Begründung:**
Audit-Daten müssen existieren, bevor sie überprüft werden können.

### 3.2 Cryptographic Support (FCS)

#### FCS_CKM.1 Cryptographic key generation

**Abhängigkeiten:**
- [FCS_CKM.2 Cryptographic key distribution] oder [FCS_COP.1 Cryptographic operation]

**Erfüllung:**
FCS_COP.1 ist im Security Target enthalten. Generierte Schlüssel werden für kryptographische Operationen verwendet.

**Begründung:**
Schlüssel müssen für einen Zweck generiert werden. In diesem Fall werden sie für kryptographische Operationen (FCS_COP.1) verwendet.

#### FCS_COP.1 Cryptographic operation

**Abhängigkeiten:**
- [FDP_ITC.1 Import of user data without security attributes] oder [FDP_ITC.2 Import of user data with security attributes] oder [FCS_CKM.1 Cryptographic key generation]

**Erfüllung:**
FCS_CKM.1 ist im Security Target enthalten und generiert die für kryptographische Operationen benötigten Schlüssel.

**Begründung:**
Kryptographische Operationen benötigen Schlüssel, die entweder importiert oder generiert werden müssen.

### 3.3 User Data Protection (FDP)

#### FDP_ACC.1 Subset access control

**Abhängigkeiten:**
- FDP_ACF.1 Security attribute based access control

**Erfüllung:**
FDP_ACF.1 ist im Security Target enthalten und definiert die Zugriffskontrollfunktionen.

**Begründung:**
Eine Zugriffskontrollrichtlinie (FDP_ACC.1) benötigt Zugriffskontrollfunktionen (FDP_ACF.1) für die Durchsetzung.

#### FDP_ACF.1 Security attribute based access control

**Abhängigkeiten:**
- FDP_ACC.1 Subset access control
- FMT_MSA.3 Static attribute initialisation

**Erfüllung:**
Beide Abhängigkeiten sind im Security Target enthalten.

**Begründung:**
- FDP_ACC.1: Zugriffskontrollfunktionen benötigen eine Zugriffskontrollrichtlinie
- FMT_MSA.3: Sicherheitsattribute müssen initialisiert werden, bevor sie für Zugriffsentscheidungen verwendet werden können

### 3.4 Identification and Authentication (FIA)

#### FIA_UID.1 Timing of identification

**Abhängigkeiten:**
Keine

**Erfüllung:**
N/A

#### FIA_UAU.1 Timing of authentication

**Abhängigkeiten:**
- FIA_UID.1 Timing of identification

**Erfüllung:**
FIA_UID.1 ist im Security Target enthalten.

**Begründung:**
Benutzer müssen identifiziert werden, bevor sie authentisiert werden können.

### 3.5 Security Management (FMT)

#### FMT_MSA.1 Management of security attributes

**Abhängigkeiten:**
- [FDP_ACC.1 Subset access control] oder [FDP_IFC.1 Subset information flow control]
- FMT_SMR.1 Security roles
- FMT_SMF.1 Specification of Management Functions

**Erfüllung:**
Alle Abhängigkeiten sind im Security Target enthalten.

**Begründung:**
- FDP_ACC.1: Sicherheitsattribute werden für Zugriffskontrolle verwendet
- FMT_SMR.1: Verwaltung von Attributen erfordert Rollendefinitionen
- FMT_SMF.1: Verwaltungsfunktionen müssen spezifiziert sein

#### FMT_MSA.3 Static attribute initialisation

**Abhängigkeiten:**
- FMT_MSA.1 Management of security attributes
- FMT_SMR.1 Security roles

**Erfüllung:**
Beide Abhängigkeiten sind im Security Target enthalten.

**Begründung:**
Attributinitialisierung benötigt Attributverwaltung und Rollendefinitionen.

#### FMT_SMF.1 Specification of Management Functions

**Abhängigkeiten:**
Keine

**Erfüllung:**
N/A

#### FMT_SMR.1 Security roles

**Abhängigkeiten:**
- FIA_UID.1 Timing of identification

**Erfüllung:**
FIA_UID.1 ist im Security Target enthalten.

**Begründung:**
Rollen können nur identifizierten Benutzern zugewiesen werden.

### 3.6 Protection of the TSF (FPT)

#### FPT_STM.1 Reliable time stamps

**Abhängigkeiten:**
Keine

**Erfüllung:**
N/A

### 3.7 [TODO: Weitere SFR-Klassen]

[TODO: Füge Abhängigkeitsanalysen für alle weiteren verwendeten SFRs hinzu]

## 4. Abhängigkeitsgraph

### 4.1 Visualisierung

[TODO: Erstelle einen Abhängigkeitsgraphen, der die Beziehungen zwischen SFRs visualisiert]

```
Beispiel-Graph (als Text):

FIA_UID.1 ──┬──> FIA_UAU.1
            └──> FMT_SMR.1 ──┬──> FMT_MSA.1 ──> FDP_ACF.1 ──┐
                             └──> FMT_MSA.3 ──────────────┘
                                                           │
FPT_STM.1 ──> FAU_GEN.1 ──> FAU_SAR.1                     │
                                                           ▼
FCS_CKM.1 ◄──> FCS_COP.1                          FDP_ACC.1 ◄──┘
```

### 4.2 Kritische Pfade

[TODO: Identifiziere kritische Abhängigkeitspfade]

**Kritischer Pfad 1: Zugriffskontrolle**
```
FIA_UID.1 → FMT_SMR.1 → FMT_MSA.1 → FDP_ACF.1 ↔ FDP_ACC.1
```

**Kritischer Pfad 2: Audit**
```
FPT_STM.1 → FAU_GEN.1 → FAU_SAR.1
```

## 5. Nicht erfüllte Abhängigkeiten

### 5.1 Übersicht

[TODO: Falls Abhängigkeiten nicht erfüllt sind, dokumentiere sie hier]

**Status:** [TODO: Keine nicht erfüllten Abhängigkeiten / X nicht erfüllte Abhängigkeiten]

### 5.2 Begründung für nicht erfüllte Abhängigkeiten

[TODO: Für jede nicht erfüllte Abhängigkeit, gebe eine detaillierte Begründung]

**Beispiel (falls zutreffend):**
```
SFR: FCS_CKM.1
Abhängigkeit: FCS_CKM.2 oder FCS_COP.1
Status: Teilweise erfüllt (nur FCS_COP.1)

Begründung: FCS_CKM.2 (Key distribution) ist nicht erforderlich, da das TOE keine 
Schlüsselverteilung an externe Entitäten durchführt. Alle Schlüssel werden intern 
generiert und verwendet (FCS_COP.1).
```

## 6. Hierarchische Beziehungen

### 6.1 Verwendung hierarchischer Komponenten

[TODO: Dokumentiere, falls hierarchisch höhere SFR-Komponenten verwendet werden]

Gemäß ISO/IEC 15408-2 erfüllt eine hierarchisch höhere Komponente automatisch die Abhängigkeiten niedrigerer Komponenten.

**Beispiel:**
```
Falls FDP_ACC.2 (Complete access control) verwendet wird, erfüllt dies automatisch 
die Abhängigkeit zu FDP_ACC.1 (Subset access control).
```

## 7. Iterationen

### 7.1 Iterierte SFRs

[TODO: Falls SFRs mehrfach verwendet werden (Iteration), dokumentiere die Abhängigkeiten für jede Iteration]

| Iterierte SFR | Iteration | Abhängigkeiten | Erfüllung |
|---------------|-----------|----------------|-----------|
| [TODO: z.B. FDP_ACC.1/1] | 1 | FDP_ACF.1/1 | ✓ |
| [TODO: z.B. FDP_ACC.1/2] | 2 | FDP_ACF.1/2 | ✓ |

## 8. Validierung

### 8.1 Validierungscheckliste

- [ ] Alle SFRs sind in der Abhängigkeitstabelle aufgeführt
- [ ] Alle Abhängigkeiten sind gemäß ISO/IEC 15408-2 korrekt identifiziert
- [ ] Alle Abhängigkeiten sind erfüllt oder begründet
- [ ] Hierarchische Beziehungen sind korrekt berücksichtigt
- [ ] Iterationen sind vollständig dokumentiert
- [ ] Abhängigkeitsgraph ist konsistent mit der Tabelle

### 8.2 Peer-Review

**Reviewer:** [TODO: Name]  
**Datum:** [TODO: Datum]  
**Status:** [TODO: Approved / Changes requested]  
**Kommentare:** [TODO: Kommentare]

## 9. Referenzen

- Dokument 0400: Security Requirements
- Dokument 0420: Requirements Rationale
- ISO/IEC 15408-2:2022 - Security functional requirements (Anhang B: Dependencies)
- [TODO: Weitere relevante Dokumente]

---

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter
2. Erstelle vollständige Abhängigkeitstabelle
3. Verifiziere alle Abhängigkeiten gegen ISO/IEC 15408-2
4. Erstelle Abhängigkeitsgraph
5. Führe Peer-Review durch
6. Aktualisiere bei Änderungen an SFRs

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
