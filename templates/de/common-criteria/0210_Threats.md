# Threats (Bedrohungen)

**Dokument-ID:** 0210
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
Dieses Template dokumentiert alle identifizierten Bedrohungen für den TOE gemäß ISO/IEC 15408-1:2022.
Bedrohungen beschreiben potenzielle Angriffe oder Sicherheitsverletzungen, die Assets gefährden können.

Anpassung erforderlich:
- Identifiziere alle relevanten Bedrohungen für den TOE
- Beschreibe jede Bedrohung detailliert mit Angriffsszenario
- Bewerte Wahrscheinlichkeit und Auswirkung jeder Bedrohung
- Ordne Bedrohungen zu Assets und Bedrohungsagenten zu
- Erstelle Bedrohungsmodell und Attack Trees
- Dokumentiere Risikobewertung

Referenz: ISO/IEC 15408-1:2022, Abschnitt 8.3.1 (Threats)
-->

## 1. Threat Overview

### 1.1 Threat Identification Methodology
**Methodik zur Bedrohungsidentifikation:**
[TODO: Beschreibe die verwendete Methodik, z.B. STRIDE, PASTA, Attack Trees]

**Verwendete Frameworks:**
- [TODO: z.B. MITRE ATT&CK]
- [TODO: z.B. OWASP Top 10]
- [TODO: z.B. CWE Top 25]

### 1.2 Threat Categories
**Bedrohungskategorien:**
- **Confidentiality Threats**: Bedrohungen der Vertraulichkeit
- **Integrity Threats**: Bedrohungen der Integrität
- **Availability Threats**: Bedrohungen der Verfügbarkeit
- **Authentication Threats**: Bedrohungen der Authentifizierung
- **Authorization Threats**: Bedrohungen der Autorisierung
- **Non-Repudiation Threats**: Bedrohungen der Nicht-Abstreitbarkeit

### 1.3 Threat Scope
**Im Scope:**
[TODO: Welche Bedrohungen werden betrachtet?]

**Außerhalb des Scope:**
[TODO: Welche Bedrohungen werden nicht betrachtet und warum?]

## 2. Confidentiality Threats

### T.UNAUTHORIZED_ACCESS
**Bedrohungs-ID:** T.UNAUTHORIZED_ACCESS  
**Kategorie:** Confidentiality  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte unbefugten Zugriff auf vertrauliche Daten erlangen]

**Betroffene Assets:**
- [TODO: A.001 - Benutzerdaten]
- [TODO: A.002 - Konfigurationsdaten]

**Bedrohungsagent:**
- [TODO: TA.001 - Externer Angreifer]
- [TODO: TA.002 - Böswilliger Insider]

**Angriffsszenario:**
1. [TODO: Angreifer identifiziert Schwachstelle in Zugriffskontrolle]
2. [TODO: Angreifer umgeht Authentifizierung]
3. [TODO: Angreifer greift auf vertrauliche Daten zu]
4. [TODO: Angreifer exfiltriert Daten]

**Voraussetzungen:**
- [TODO: Netzwerkzugriff auf TOE]
- [TODO: Kenntnis der Systemarchitektur]

**Auswirkungen:**
- **Vertraulichkeit:** High - Vollständiger Verlust der Datenkontrolle
- **Integrität:** None
- **Verfügbarkeit:** None

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]  
**Risikobewertung:** [TODO: High/Medium/Low]

**MITRE ATT&CK Mapping:**
- [TODO: T1078 - Valid Accounts]
- [TODO: T1552 - Unsecured Credentials]

### T.EAVESDROPPING
**Bedrohungs-ID:** T.EAVESDROPPING  
**Kategorie:** Confidentiality  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte Kommunikation abhören und vertrauliche Informationen erlangen]

**Betroffene Assets:**
- [TODO: A.003 - Kommunikationsdaten]

**Bedrohungsagent:**
- [TODO: TA.003 - Network Attacker]

**Angriffsszenario:**
1. [TODO: Angreifer positioniert sich im Netzwerkpfad]
2. [TODO: Angreifer fängt unverschlüsselte Kommunikation ab]
3. [TODO: Angreifer analysiert abgefangene Daten]

**Voraussetzungen:**
- [TODO: Zugriff auf Netzwerkinfrastruktur]
- [TODO: Unverschlüsselte Kommunikation]

**Auswirkungen:**
- **Vertraulichkeit:** High
- **Integrität:** None
- **Verfügbarkeit:** None

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]  
**Risikobewertung:** [TODO: High/Medium/Low]

### T.DATA_LEAKAGE
**Bedrohungs-ID:** T.DATA_LEAKAGE  
**Kategorie:** Confidentiality  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Vertrauliche Daten könnten durch Fehler oder Schwachstellen unbeabsichtigt offengelegt werden]

[TODO: Füge weitere Confidentiality Threats hinzu]

## 3. Integrity Threats

### T.DATA_MANIPULATION
**Bedrohungs-ID:** T.DATA_MANIPULATION  
**Kategorie:** Integrity  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte Daten unbefugt ändern oder manipulieren]

**Betroffene Assets:**
- [TODO: A.004 - Transaktionsdaten]
- [TODO: A.005 - Konfigurationsdaten]

**Bedrohungsagent:**
- [TODO: TA.001 - Externer Angreifer]
- [TODO: TA.002 - Böswilliger Insider]

**Angriffsszenario:**
1. [TODO: Angreifer erlangt Schreibzugriff]
2. [TODO: Angreifer modifiziert kritische Daten]
3. [TODO: Modifikation bleibt unentdeckt]
4. [TODO: System verarbeitet manipulierte Daten]

**Voraussetzungen:**
- [TODO: Schreibzugriff auf Daten]
- [TODO: Fehlende Integritätsprüfungen]

**Auswirkungen:**
- **Vertraulichkeit:** None
- **Integrität:** High - Datenintegrität kompromittiert
- **Verfügbarkeit:** None

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]  
**Risikobewertung:** [TODO: High/Medium/Low]

### T.CODE_INJECTION
**Bedrohungs-ID:** T.CODE_INJECTION  
**Kategorie:** Integrity  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte schädlichen Code in das System einschleusen]

[TODO: Füge weitere Integrity Threats hinzu]

## 4. Availability Threats

### T.DENIAL_OF_SERVICE
**Bedrohungs-ID:** T.DENIAL_OF_SERVICE  
**Kategorie:** Availability  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte die Verfügbarkeit des TOE durch Überlastung beeinträchtigen]

**Betroffene Assets:**
- [TODO: A.006 - Service-Verfügbarkeit]

**Bedrohungsagent:**
- [TODO: TA.003 - Network Attacker]

**Angriffsszenario:**
1. [TODO: Angreifer sendet große Anzahl von Anfragen]
2. [TODO: System-Ressourcen werden erschöpft]
3. [TODO: Legitime Anfragen können nicht mehr verarbeitet werden]

**Voraussetzungen:**
- [TODO: Netzwerkzugriff]
- [TODO: Fehlende Rate-Limiting]

**Auswirkungen:**
- **Vertraulichkeit:** None
- **Integrität:** None
- **Verfügbarkeit:** High - Service nicht verfügbar

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]  
**Risikobewertung:** [TODO: High/Medium/Low]

### T.RESOURCE_EXHAUSTION
**Bedrohungs-ID:** T.RESOURCE_EXHAUSTION  
**Kategorie:** Availability  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte System-Ressourcen erschöpfen]

[TODO: Füge weitere Availability Threats hinzu]

## 5. Authentication Threats

### T.AUTHENTICATION_BYPASS
**Bedrohungs-ID:** T.AUTHENTICATION_BYPASS  
**Kategorie:** Authentication  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte Authentifizierungsmechanismen umgehen]

**Betroffene Assets:**
- [TODO: A.007 - Authentifizierungssystem]

**Bedrohungsagent:**
- [TODO: TA.001 - Externer Angreifer]

**Angriffsszenario:**
1. [TODO: Angreifer identifiziert Schwachstelle in Authentifizierung]
2. [TODO: Angreifer umgeht Authentifizierungsprüfung]
3. [TODO: Angreifer erlangt unbefugten Zugriff]

**Voraussetzungen:**
- [TODO: Zugriff auf Authentifizierungsschnittstelle]
- [TODO: Schwachstelle in Authentifizierungslogik]

**Auswirkungen:**
- **Vertraulichkeit:** High
- **Integrität:** High
- **Verfügbarkeit:** Medium

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]  
**Risikobewertung:** [TODO: High/Medium/Low]

### T.CREDENTIAL_THEFT
**Bedrohungs-ID:** T.CREDENTIAL_THEFT  
**Kategorie:** Authentication  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte Authentifizierungsdaten stehlen]

[TODO: Füge weitere Authentication Threats hinzu]

## 6. Authorization Threats

### T.PRIVILEGE_ESCALATION
**Bedrohungs-ID:** T.PRIVILEGE_ESCALATION  
**Kategorie:** Authorization  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte seine Berechtigungen unbefugt erweitern]

**Betroffene Assets:**
- [TODO: A.008 - Autorisierungssystem]

**Bedrohungsagent:**
- [TODO: TA.002 - Böswilliger Insider]

**Angriffsszenario:**
1. [TODO: Angreifer mit niedrigen Rechten identifiziert Schwachstelle]
2. [TODO: Angreifer nutzt Schwachstelle zur Rechteausweitung]
3. [TODO: Angreifer erlangt administrative Rechte]

**Voraussetzungen:**
- [TODO: Gültiges Benutzerkonto]
- [TODO: Schwachstelle in Autorisierungsprüfung]

**Auswirkungen:**
- **Vertraulichkeit:** High
- **Integrität:** High
- **Verfügbarkeit:** High

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]  
**Risikobewertung:** [TODO: High/Medium/Low]

### T.UNAUTHORIZED_FUNCTION_ACCESS
**Bedrohungs-ID:** T.UNAUTHORIZED_FUNCTION_ACCESS  
**Kategorie:** Authorization  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte auf Funktionen zugreifen, für die er nicht autorisiert ist]

[TODO: Füge weitere Authorization Threats hinzu]

## 7. Non-Repudiation Threats

### T.REPUDIATION
**Bedrohungs-ID:** T.REPUDIATION  
**Kategorie:** Non-Repudiation  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Benutzer könnte durchgeführte Aktionen abstreiten]

**Betroffene Assets:**
- [TODO: A.009 - Audit-Logs]

**Bedrohungsagent:**
- [TODO: TA.002 - Böswilliger Insider]

**Angriffsszenario:**
1. [TODO: Benutzer führt kritische Aktion durch]
2. [TODO: Benutzer manipuliert oder löscht Audit-Logs]
3. [TODO: Benutzer streitet Aktion ab]

**Voraussetzungen:**
- [TODO: Zugriff auf Audit-System]
- [TODO: Fehlende Log-Integrität]

**Auswirkungen:**
- **Vertraulichkeit:** None
- **Integrität:** High
- **Verfügbarkeit:** None

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]  
**Risikobewertung:** [TODO: High/Medium/Low]

### T.LOG_TAMPERING
**Bedrohungs-ID:** T.LOG_TAMPERING  
**Kategorie:** Non-Repudiation  
**Priorität:** [TODO: High/Medium/Low]

**Beschreibung:**
[TODO: Ein Angreifer könnte Audit-Logs manipulieren oder löschen]

[TODO: Füge weitere Non-Repudiation Threats hinzu]

## 8. Threat Summary

### 8.1 Threat Statistics
**Bedrohungsstatistik:**
- Gesamtanzahl Bedrohungen: [TODO: Anzahl]
- Confidentiality Threats: [TODO: Anzahl]
- Integrity Threats: [TODO: Anzahl]
- Availability Threats: [TODO: Anzahl]
- Authentication Threats: [TODO: Anzahl]
- Authorization Threats: [TODO: Anzahl]
- Non-Repudiation Threats: [TODO: Anzahl]

### 8.2 Risk Distribution
**Risikoverteilung:**
- High Risk: [TODO: Anzahl] ([TODO: %])
- Medium Risk: [TODO: Anzahl] ([TODO: %])
- Low Risk: [TODO: Anzahl] ([TODO: %])

### 8.3 Threat Priority Matrix
**Priorisierungsmatrix:**

| Priority | Likelihood High | Likelihood Medium | Likelihood Low |
|----------|----------------|-------------------|----------------|
| **Impact High** | [TODO: Threat IDs] | [TODO: Threat IDs] | [TODO: Threat IDs] |
| **Impact Medium** | [TODO: Threat IDs] | [TODO: Threat IDs] | [TODO: Threat IDs] |
| **Impact Low** | [TODO: Threat IDs] | [TODO: Threat IDs] | [TODO: Threat IDs] |

## 9. Threat Model

### 9.1 Attack Trees
**Attack Tree für kritische Bedrohungen:**

[TODO: Erstelle Attack Trees für die wichtigsten Bedrohungen]

```
[TODO: Attack Tree Diagramm einfügen]
```

### 9.2 Threat Relationships
**Beziehungen zwischen Bedrohungen:**

[TODO: Beschreibe, wie Bedrohungen zusammenhängen oder sich gegenseitig ermöglichen]

```
[TODO: Bedrohungsbeziehungsdiagramm einfügen]
```

### 9.3 Attack Chains
**Angriffsketten:**

**Chain 1: [TODO: Name]**
1. [TODO: T.001] → [TODO: T.003] → [TODO: T.005]
2. [TODO: Beschreibung der Angriffskette]

**Chain 2: [TODO: Name]**
1. [TODO: T.002] → [TODO: T.004]
2. [TODO: Beschreibung der Angriffskette]

## 10. Traceability

### 10.1 Threat-to-Asset Mapping
**Zuordnung Bedrohungen zu Assets:**

| Threat ID | Affected Assets | Impact |
|-----------|----------------|--------|
| [TODO: T.001] | [TODO: A.001, A.002] | [TODO: High] |
| [TODO: T.002] | [TODO: A.003] | [TODO: Medium] |

### 10.2 Threat-to-Agent Mapping
**Zuordnung Bedrohungen zu Agenten:**

| Threat ID | Threat Agents | Capability Required |
|-----------|---------------|---------------------|
| [TODO: T.001] | [TODO: TA.001, TA.002] | [TODO: High] |
| [TODO: T.002] | [TODO: TA.003] | [TODO: Medium] |

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter mit TOE-spezifischen Bedrohungen
2. Führe vollständige Bedrohungsanalyse durch
3. Erstelle Attack Trees für kritische Bedrohungen
4. Bewerte Risiken für alle Bedrohungen
5. Dokumentiere Angriffsketten
6. Überprüfe Konsistenz mit Assets (Template 0200) und Security Objectives (Template 0300)

