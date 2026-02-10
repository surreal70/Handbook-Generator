# Coverage Matrix

**Dokument-ID:** 0440  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Intern / Vertraulich / Streng vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches Target of Evaluation (TOE) an.

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
This template provides comprehensive coverage matrices that demonstrate traceability
between all elements of the Security Target: Threats, OSPs, Assumptions, Security
Objectives, and Security Requirements.

Key considerations:
- Complete traceability must be demonstrated in both directions
- Every threat must be addressed by at least one security objective
- Every security objective must be addressed by at least one SFR
- Gaps in coverage must be identified and justified
- The matrices support audit and certification processes
-->

## 1. Einleitung

Dieses Dokument stellt umfassende Coverage Matrices bereit, die die Rückverfolgbarkeit zwischen allen Elementen des Security Target demonstrieren:

- Bedrohungen (Threats)
- Organisatorische Sicherheitsrichtlinien (OSPs)
- Annahmen (Assumptions)
- Sicherheitsziele (Security Objectives)
- Sicherheitsanforderungen (Security Requirements)

Die Matrices gewährleisten vollständige Abdeckung und Konsistenz des Security Target.

## 2. Bedrohungen → Sicherheitsziele

### 2.1 Threat Coverage Matrix

Diese Matrix zeigt, wie jede identifizierte Bedrohung durch Sicherheitsziele adressiert wird.

<!-- TODO: Erstelle vollständige Matrix -->

| Bedrohung | Beschreibung | Adressierende Sicherheitsziele | Abdeckung |
|-----------|--------------|-------------------------------|-----------|
| T.UNAUTH_ACCESS | Unautorisierter Zugriff auf TOE-Funktionen | O.ACCESS, O.IDENTIFY, O.AUTHENTICATE | ✓ Vollständig |
| T.DATA_DISCLOSURE | Unbefugte Offenlegung von Daten | O.CRYPTO, O.ACCESS | ✓ Vollständig |
| T.DATA_MANIPULATION | Unbefugte Manipulation von Daten | O.INTEGRITY, O.ACCESS, O.AUDIT | ✓ Vollständig |
| T.MASQUERADE | Identitätsvortäuschung | O.AUTHENTICATE, O.IDENTIFY | ✓ Vollständig |
| T.AUDIT_COMPROMISE | Kompromittierung von Audit-Daten | O.AUDIT, O.PROTECT_TSF | ✓ Vollständig |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 2.2 Vollständigkeitsanalyse

**Statistik:**
- Anzahl identifizierter Bedrohungen: [TODO: X]
- Anzahl vollständig adressierter Bedrohungen: [TODO: X]
- Anzahl teilweise adressierter Bedrohungen: [TODO: 0]
- Anzahl nicht adressierter Bedrohungen: [TODO: 0]

**Status:** [TODO: ✓ Alle Bedrohungen adressiert / ⚠ Lücken vorhanden]

### 2.3 Nicht adressierte Bedrohungen

[TODO: Falls Bedrohungen nicht vollständig adressiert sind, begründe dies]

**Beispiel (falls zutreffend):**
```
Bedrohung: T.PHYSICAL_ATTACK
Status: Nicht durch TOE adressiert
Begründung: Physische Angriffe werden durch Umgebungsannahmen (A.PHYSICAL_PROTECTION) 
und organisatorische Maßnahmen adressiert, nicht durch TOE-Funktionalität.
```

## 3. OSPs → Sicherheitsziele

### 3.1 OSP Coverage Matrix

Diese Matrix zeigt, wie organisatorische Sicherheitsrichtlinien durch Sicherheitsziele umgesetzt werden.

<!-- TODO: Erstelle vollständige Matrix -->

| OSP | Beschreibung | Adressierende Sicherheitsziele | Abdeckung |
|-----|--------------|-------------------------------|-----------|
| P.ACCOUNTABILITY | Benutzeraktionen müssen nachvollziehbar sein | O.AUDIT, O.IDENTIFY | ✓ Vollständig |
| P.AUTHORIZED_USERS | Nur autorisierte Benutzer dürfen auf TOE zugreifen | O.ACCESS, O.AUTHENTICATE | ✓ Vollständig |
| P.CRYPTOGRAPHY | Sensible Daten müssen verschlüsselt werden | O.CRYPTO | ✓ Vollständig |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 3.2 Vollständigkeitsanalyse

**Statistik:**
- Anzahl definierter OSPs: [TODO: X]
- Anzahl vollständig umgesetzter OSPs: [TODO: X]
- Anzahl teilweise umgesetzter OSPs: [TODO: 0]
- Anzahl nicht umgesetzter OSPs: [TODO: 0]

**Status:** [TODO: ✓ Alle OSPs umgesetzt / ⚠ Lücken vorhanden]

## 4. Annahmen → Sicherheitsziele für die Umgebung

### 4.1 Assumption Coverage Matrix

Diese Matrix zeigt, wie Annahmen durch Sicherheitsziele für die Umgebung adressiert werden.

<!-- TODO: Erstelle vollständige Matrix -->

| Annahme | Beschreibung | Adressierende Umgebungsziele | Abdeckung |
|---------|--------------|------------------------------|-----------|
| A.PHYSICAL_PROTECTION | TOE ist physisch geschützt | OE.PHYSICAL | ✓ Vollständig |
| A.TRUSTED_ADMIN | Administratoren sind vertrauenswürdig | OE.ADMIN_TRAINING, OE.ADMIN_VETTING | ✓ Vollständig |
| A.NETWORK_PROTECTION | Netzwerk ist gegen externe Angriffe geschützt | OE.NETWORK_SECURITY | ✓ Vollständig |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 4.2 Vollständigkeitsanalyse

**Statistik:**
- Anzahl definierter Annahmen: [TODO: X]
- Anzahl vollständig adressierter Annahmen: [TODO: X]
- Anzahl teilweise adressierter Annahmen: [TODO: 0]
- Anzahl nicht adressierter Annahmen: [TODO: 0]

**Status:** [TODO: ✓ Alle Annahmen adressiert / ⚠ Lücken vorhanden]

## 5. Sicherheitsziele für TOE → SFRs

### 5.1 Security Objectives to SFRs Matrix

Diese Matrix zeigt, wie Sicherheitsziele für das TOE durch Security Functional Requirements erfüllt werden.

<!-- TODO: Erstelle vollständige Matrix -->

| Sicherheitsziel | Beschreibung | Erfüllende SFRs | Abdeckung |
|-----------------|--------------|-----------------|-----------|
| O.ACCESS | Zugriffskontrolle auf TOE-Ressourcen | FDP_ACC.1, FDP_ACF.1, FMT_MSA.1, FMT_MSA.3 | ✓ Vollständig |
| O.IDENTIFY | Identifikation von Benutzern | FIA_UID.1 | ✓ Vollständig |
| O.AUTHENTICATE | Authentisierung von Benutzern | FIA_UAU.1, FIA_AFL.1 | ✓ Vollständig |
| O.AUDIT | Audit-Aufzeichnung sicherheitsrelevanter Ereignisse | FAU_GEN.1, FAU_SAR.1, FPT_STM.1 | ✓ Vollständig |
| O.CRYPTO | Kryptographischer Schutz sensibler Daten | FCS_CKM.1, FCS_COP.1 | ✓ Vollständig |
| O.INTEGRITY | Schutz der Datenintegrität | FDP_SDI.1, FPT_TST.1 | ✓ Vollständig |
| O.PROTECT_TSF | Schutz der TSF-Funktionalität | FPT_STM.1, FPT_TST.1 | ✓ Vollständig |
| O.MANAGE | Sichere Verwaltung des TOE | FMT_SMF.1, FMT_SMR.1, FMT_MOF.1 | ✓ Vollständig |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 5.2 Vollständigkeitsanalyse

**Statistik:**
- Anzahl Sicherheitsziele für TOE: [TODO: X]
- Anzahl vollständig erfüllter Ziele: [TODO: X]
- Anzahl teilweise erfüllter Ziele: [TODO: 0]
- Anzahl nicht erfüllter Ziele: [TODO: 0]

**Status:** [TODO: ✓ Alle Ziele erfüllt / ⚠ Lücken vorhanden]

### 5.3 Nicht erfüllte Sicherheitsziele

[TODO: Falls Sicherheitsziele nicht vollständig durch SFRs erfüllt sind, begründe dies]

## 6. Umgekehrte Rückverfolgbarkeit: SFRs → Sicherheitsziele

### 6.1 SFRs to Security Objectives Matrix

Diese Matrix zeigt die umgekehrte Rückverfolgbarkeit: Jede SFR muss mindestens ein Sicherheitsziel erfüllen.

<!-- TODO: Erstelle vollständige Matrix -->

| SFR | Erfüllte Sicherheitsziele | Notwendigkeit |
|-----|---------------------------|---------------|
| FAU_GEN.1 | O.AUDIT | ✓ Notwendig |
| FAU_SAR.1 | O.AUDIT | ✓ Notwendig |
| FCS_CKM.1 | O.CRYPTO | ✓ Notwendig |
| FCS_COP.1 | O.CRYPTO | ✓ Notwendig |
| FDP_ACC.1 | O.ACCESS | ✓ Notwendig |
| FDP_ACF.1 | O.ACCESS | ✓ Notwendig |
| FDP_SDI.1 | O.INTEGRITY | ✓ Notwendig |
| FIA_AFL.1 | O.AUTHENTICATE | ✓ Notwendig |
| FIA_UAU.1 | O.AUTHENTICATE | ✓ Notwendig |
| FIA_UID.1 | O.IDENTIFY | ✓ Notwendig |
| FMT_MOF.1 | O.MANAGE | ✓ Notwendig |
| FMT_MSA.1 | O.ACCESS, O.MANAGE | ✓ Notwendig |
| FMT_MSA.3 | O.ACCESS | ✓ Notwendig |
| FMT_SMF.1 | O.MANAGE | ✓ Notwendig |
| FMT_SMR.1 | O.MANAGE | ✓ Notwendig |
| FPT_STM.1 | O.AUDIT, O.PROTECT_TSF | ✓ Notwendig |
| FPT_TST.1 | O.INTEGRITY, O.PROTECT_TSF | ✓ Notwendig |
| [TODO] | [TODO] | [TODO] |

### 6.2 Überflüssige SFRs

[TODO: Identifiziere SFRs, die kein Sicherheitsziel erfüllen (sollte keine geben)]

**Status:** [TODO: ✓ Keine überflüssigen SFRs / ⚠ Überflüssige SFRs identifiziert]

## 7. Vollständige Traceability Matrix

### 7.1 End-to-End Traceability

Diese Matrix zeigt die vollständige Rückverfolgbarkeit von Bedrohungen bis zu SFRs.

<!-- TODO: Erstelle vollständige End-to-End Matrix -->

| Bedrohung/OSP/Annahme | Sicherheitsziel | SFR | Rationale |
|-----------------------|-----------------|-----|-----------|
| T.UNAUTH_ACCESS | O.ACCESS | FDP_ACC.1, FDP_ACF.1 | Zugriffskontrolle verhindert unautorisierten Zugriff |
| T.UNAUTH_ACCESS | O.IDENTIFY | FIA_UID.1 | Identifikation erforderlich vor Zugriff |
| T.UNAUTH_ACCESS | O.AUTHENTICATE | FIA_UAU.1 | Authentisierung verifiziert Identität |
| T.DATA_DISCLOSURE | O.CRYPTO | FCS_COP.1 | Verschlüsselung schützt vor Offenlegung |
| T.DATA_DISCLOSURE | O.ACCESS | FDP_ACC.1 | Zugriffskontrolle begrenzt Datenzugriff |
| T.DATA_MANIPULATION | O.INTEGRITY | FDP_SDI.1 | Integritätsprüfung erkennt Manipulation |
| T.DATA_MANIPULATION | O.ACCESS | FDP_ACC.1 | Zugriffskontrolle verhindert unbefugte Änderungen |
| T.DATA_MANIPULATION | O.AUDIT | FAU_GEN.1 | Audit-Aufzeichnung dokumentiert Änderungen |
| [TODO] | [TODO] | [TODO] | [TODO] |

## 8. Coverage Gaps Analysis

### 8.1 Identifizierte Lücken

[TODO: Identifiziere und dokumentiere Lücken in der Abdeckung]

**Lückentypen:**
- Bedrohungen ohne Sicherheitsziele
- Sicherheitsziele ohne SFRs
- SFRs ohne Sicherheitsziele
- OSPs ohne Umsetzung

**Status:** [TODO: ✓ Keine Lücken / ⚠ X Lücken identifiziert]

### 8.2 Begründung für Lücken

[TODO: Für jede identifizierte Lücke, gebe eine Begründung]

**Beispiel (falls zutreffend):**
```
Lücke: Bedrohung T.PHYSICAL_ATTACK hat kein TOE-Sicherheitsziel
Begründung: Physische Bedrohungen werden durch Umgebungsannahmen und -ziele adressiert,
nicht durch TOE-Funktionalität. Siehe A.PHYSICAL_PROTECTION und OE.PHYSICAL.
```

## 9. Visualisierung

### 9.1 Traceability Diagram

[TODO: Erstelle ein Diagramm, das die Rückverfolgbarkeit visualisiert]

```
Beispiel (als Text):

Bedrohungen          Sicherheitsziele         SFRs
─────────────        ─────────────────        ────────────
T.UNAUTH_ACCESS ───┬─> O.ACCESS ──────────┬─> FDP_ACC.1
                   │                      └─> FDP_ACF.1
                   ├─> O.IDENTIFY ─────────> FIA_UID.1
                   └─> O.AUTHENTICATE ────> FIA_UAU.1

T.DATA_DISCLOSURE ─┬─> O.CRYPTO ──────────┬─> FCS_CKM.1
                   │                      └─> FCS_COP.1
                   └─> O.ACCESS ──────────> FDP_ACC.1

T.DATA_MANIPULATION┬─> O.INTEGRITY ───────> FDP_SDI.1
                   ├─> O.ACCESS ──────────> FDP_ACC.1
                   └─> O.AUDIT ───────────┬─> FAU_GEN.1
                                          └─> FPT_STM.1
```

## 10. Validierung und Wartung

### 10.1 Validierungscheckliste

- [ ] Alle Bedrohungen sind durch Sicherheitsziele adressiert
- [ ] Alle OSPs sind durch Sicherheitsziele umgesetzt
- [ ] Alle Annahmen sind durch Umgebungsziele adressiert
- [ ] Alle Sicherheitsziele für TOE sind durch SFRs erfüllt
- [ ] Alle SFRs erfüllen mindestens ein Sicherheitsziel
- [ ] Keine Lücken in der Abdeckung (oder begründet)
- [ ] Traceability ist bidirektional vollständig

### 10.2 Wartungshinweise

**Bei Änderungen:**
- Neue Bedrohung → Sicherheitsziel hinzufügen → SFR hinzufügen
- Neue SFR → Sicherheitsziel zuordnen → Bedrohung/OSP zuordnen
- Entfernte Bedrohung → Prüfe, ob Sicherheitsziel noch benötigt wird
- Entfernte SFR → Prüfe, ob Sicherheitsziel noch erfüllt ist

**Aktualisierungsfrequenz:**
- Bei jeder Änderung an Bedrohungen, Zielen oder Anforderungen
- Vor jedem Review-Meilenstein
- Vor Einreichung zur Evaluierung

## 11. Zusammenfassung

### 11.1 Coverage Summary

**Vollständigkeit:**
- ✓ Alle Bedrohungen adressiert: [TODO: X/X]
- ✓ Alle OSPs umgesetzt: [TODO: X/X]
- ✓ Alle Annahmen adressiert: [TODO: X/X]
- ✓ Alle Sicherheitsziele erfüllt: [TODO: X/X]
- ✓ Alle SFRs notwendig: [TODO: X/X]

**Gesamtstatus:** [TODO: ✓ Vollständig / ⚠ Lücken vorhanden]

### 11.2 Audit-Bereitschaft

[TODO: Bestätige Bereitschaft für Audit]

Die Coverage Matrices demonstrieren vollständige und konsistente Rückverfolgbarkeit zwischen allen Elementen des Security Target. Das TOE ist bereit für die Evaluierung.

## 12. Referenzen

- Dokument 0200: Security Problem Definition
- Dokument 0300: Security Objectives
- Dokument 0400: Security Requirements
- Dokument 0420: Requirements Rationale
- Dokument 0430: SFR Dependencies
- ISO/IEC 15408-1:2022 - Introduction and general model
- ISO/IEC 15408-2:2022 - Security functional requirements
- ISO/IEC 15408-3:2022 - Security assurance requirements

---

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter
2. Erstelle vollständige Coverage Matrices
3. Identifiziere und begründe Lücken
4. Erstelle Traceability Diagram
5. Führe Peer-Review durch
6. Halte Matrices bei Änderungen aktuell
