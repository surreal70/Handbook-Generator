# Threat Agents and Assets

**Dokument-ID:** 0240  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
Dieses Template dokumentiert Bedrohungsagenten und schützenswerte Assets gemäß ISO/IEC 15408-1:2022.
Es beschreibt detailliert, wer potenzielle Angreifer sind und welche Assets geschützt werden müssen.

Anpassung erforderlich:
- Identifiziere alle relevanten Bedrohungsagenten
- Beschreibe Fähigkeiten, Motivation und Ressourcen jedes Agenten
- Identifiziere alle schützenswerten Assets
- Klassifiziere Assets nach Wert und Schutzbedarf
- Dokumentiere Asset-Abhängigkeiten
- Bewerte Angriffspotenzial

Referenz: ISO/IEC 15408-1:2022, Abschnitt 8.3 (Security Problem Definition)
-->

## 1. Overview

### 1.1 Purpose
Dieses Dokument definiert:
- **Threat Agents**: Potenzielle Angreifer mit ihren Fähigkeiten und Motivationen
- **Assets**: Schützenswerte Ressourcen, Daten und Funktionen

### 1.2 Scope
**Im Scope:**
[TODO: Was wird in diesem Dokument abgedeckt?]

**Außerhalb des Scope:**
[TODO: Was wird nicht abgedeckt?]

## 2. Assets

### 2.1 Asset Identification

#### 2.1.1 Asset Categories
**Asset-Kategorien:**
- **Data Assets**: Daten und Informationen
- **Service Assets**: Dienste und Funktionen
- **System Assets**: Systemkomponenten und Infrastruktur
- **Credential Assets**: Authentifizierungs- und Autorisierungsdaten
- **Configuration Assets**: Konfigurationsdaten und -einstellungen

#### 2.1.2 Asset Inventory
**Asset-Inventar:**

| Asset ID | Asset Name | Category | Owner | Location | Description |
|----------|------------|----------|-------|----------|-------------|
| [TODO: A.001] | [TODO: Name] | [TODO: Data/Service/System] | [TODO: Owner] | [TODO: Location] | [TODO: Beschreibung] |
| [TODO: A.002] | [TODO: Name] | [TODO: Kategorie] | [TODO: Owner] | [TODO: Location] | [TODO: Beschreibung] |
| [TODO: A.003] | [TODO: Name] | [TODO: Kategorie] | [TODO: Owner] | [TODO: Location] | [TODO: Beschreibung] |

### 2.2 Data Assets

#### A.USER_DATA
**Asset-ID:** A.USER_DATA  
**Kategorie:** Data  
**Typ:** [TODO: Personal Data / Business Data / Technical Data]

**Beschreibung:**
[TODO: Benutzerdaten einschließlich persönlicher Informationen, Präferenzen und Profildaten]

**Eigenschaften:**
- **Vertraulichkeit:** [TODO: High/Medium/Low]
- **Integrität:** [TODO: High/Medium/Low]
- **Verfügbarkeit:** [TODO: High/Medium/Low]
- **Datenvolumen:** [TODO: z.B. 1 TB]
- **Datenformat:** [TODO: z.B. JSON, XML, Database]

**Schutzbedarf:**
- **Vertraulichkeit:** [TODO: Begründung für Schutzbedarf]
- **Integrität:** [TODO: Begründung für Schutzbedarf]
- **Verfügbarkeit:** [TODO: Begründung für Schutzbedarf]

**Regulatorische Anforderungen:**
- [TODO: GDPR Article 32 - Security of processing]
- [TODO: HIPAA §164.312 - Technical safeguards]
- [TODO: Weitere Anforderungen]

**Wert:**
- **Geschäftswert:** [TODO: High/Medium/Low]
- **Monetärer Wert:** [TODO: Schätzung]
- **Reputationswert:** [TODO: High/Medium/Low]

**Lebenszyklus:**
- **Erstellung:** [TODO: Wie werden Daten erstellt?]
- **Speicherung:** [TODO: Wo werden Daten gespeichert?]
- **Verarbeitung:** [TODO: Wie werden Daten verarbeitet?]
- **Übertragung:** [TODO: Wie werden Daten übertragen?]
- **Archivierung:** [TODO: Wie werden Daten archiviert?]
- **Löschung:** [TODO: Wie werden Daten gelöscht?]

---

#### A.AUTHENTICATION_DATA
**Asset-ID:** A.AUTHENTICATION_DATA  
**Kategorie:** Credential  
**Typ:** [TODO: Passwords / Tokens / Certificates]

**Beschreibung:**
[TODO: Authentifizierungsdaten wie Passwörter, Tokens, Zertifikate]

[TODO: Füge weitere Data Assets hinzu]

### 2.3 Service Assets

#### A.AUTHENTICATION_SERVICE
**Asset-ID:** A.AUTHENTICATION_SERVICE  
**Kategorie:** Service  
**Typ:** [TODO: Authentication / Authorization / Identity Management]

**Beschreibung:**
[TODO: Authentifizierungsdienst, der Benutzeridentitäten verifiziert]

**Eigenschaften:**
- **Verfügbarkeit:** [TODO: 99.9% SLA]
- **Performance:** [TODO: < 100ms Response Time]
- **Kapazität:** [TODO: 1000 req/sec]

**Schutzbedarf:**
- **Verfügbarkeit:** [TODO: High - Kritisch für Systemzugang]
- **Integrität:** [TODO: High - Falsche Authentifizierung gefährdet Sicherheit]
- **Vertraulichkeit:** [TODO: Medium - Metadaten können sensibel sein]

**Abhängigkeiten:**
- [TODO: A.AUTHENTICATION_DATA]
- [TODO: A.USER_DATABASE]
- [TODO: A.NETWORK_CONNECTIVITY]

**Wert:**
- **Geschäftswert:** [TODO: High - Grundlegende Sicherheitsfunktion]
- **Kritikalität:** [TODO: High - System nicht nutzbar ohne Authentifizierung]

---

#### A.DATA_PROCESSING_SERVICE
**Asset-ID:** A.DATA_PROCESSING_SERVICE  
**Kategorie:** Service  
**Typ:** [TODO: Processing / Computation / Transformation]

**Beschreibung:**
[TODO: Dienst zur Verarbeitung von Geschäftsdaten]

[TODO: Füge weitere Service Assets hinzu]

### 2.4 System Assets

#### A.TOE_PLATFORM
**Asset-ID:** A.TOE_PLATFORM  
**Kategorie:** System  
**Typ:** [TODO: Hardware / Software / Firmware]

**Beschreibung:**
[TODO: Die Plattform, auf der der TOE läuft]

**Komponenten:**
- [TODO: Betriebssystem]
- [TODO: Hardware-Plattform]
- [TODO: Virtualisierungsschicht]
- [TODO: Container-Runtime]

**Schutzbedarf:**
- **Verfügbarkeit:** [TODO: High]
- **Integrität:** [TODO: High]
- **Vertraulichkeit:** [TODO: Medium]

**Kritikalität:**
[TODO: High - Kompromittierung der Plattform gefährdet alle Assets]

---

#### A.CRYPTOGRAPHIC_KEYS
**Asset-ID:** A.CRYPTOGRAPHIC_KEYS  
**Kategorie:** System  
**Typ:** [TODO: Encryption Keys / Signing Keys / Certificates]

**Beschreibung:**
[TODO: Kryptografische Schlüssel für Verschlüsselung und Signatur]

[TODO: Füge weitere System Assets hinzu]

### 2.5 Asset Classification

#### 2.5.1 Classification Scheme
**Klassifizierungsschema:**

| Classification | Confidentiality | Integrity | Availability | Examples |
|----------------|----------------|-----------|--------------|----------|
| **Critical** | High | High | High | [TODO: A.001, A.003] |
| **High** | High | High | Medium | [TODO: A.002, A.005] |
| **Medium** | Medium | Medium | Medium | [TODO: A.004, A.006] |
| **Low** | Low | Low | Low | [TODO: A.007] |

#### 2.5.2 Asset Value Matrix
**Asset-Wert-Matrix:**

| Asset ID | Business Value | Regulatory Value | Reputation Value | Total Value |
|----------|---------------|------------------|------------------|-------------|
| [TODO: A.001] | [TODO: High] | [TODO: High] | [TODO: High] | [TODO: Critical] |
| [TODO: A.002] | [TODO: Medium] | [TODO: High] | [TODO: Medium] | [TODO: High] |

### 2.6 Asset Dependencies

#### 2.6.1 Dependency Graph
**Asset-Abhängigkeiten:**

[TODO: Erstelle ein Diagramm, das Asset-Abhängigkeiten zeigt]

```
[TODO: Asset-Abhängigkeitsdiagramm einfügen]
```

#### 2.6.2 Dependency Matrix
**Abhängigkeitsmatrix:**

| Asset | Depends On | Impact if Unavailable |
|-------|------------|----------------------|
| [TODO: A.001] | [TODO: A.003, A.005] | [TODO: Service nicht verfügbar] |
| [TODO: A.002] | [TODO: A.004] | [TODO: Datenverarbeitung nicht möglich] |

## 3. Threat Agents

### 3.1 Threat Agent Identification

#### 3.1.1 Agent Categories
**Agenten-Kategorien:**
- **External Attackers**: Externe Angreifer ohne legitimen Zugang
- **Insiders**: Mitarbeiter mit legitimem Zugang
- **Privileged Insiders**: Administratoren mit privilegiertem Zugang
- **Nation-State Actors**: Staatlich unterstützte Angreifer
- **Organized Crime**: Organisierte Kriminalität
- **Hacktivists**: Ideologisch motivierte Angreifer
- **Script Kiddies**: Unerfahrene Angreifer mit vorgefertigten Tools

#### 3.1.2 Agent Inventory
**Agenten-Inventar:**

| Agent ID | Agent Type | Motivation | Capability | Resources | Description |
|----------|------------|------------|------------|-----------|-------------|
| [TODO: TA.001] | [TODO: External Attacker] | [TODO: Financial] | [TODO: High] | [TODO: High] | [TODO: Beschreibung] |
| [TODO: TA.002] | [TODO: Insider] | [TODO: Revenge] | [TODO: Medium] | [TODO: Medium] | [TODO: Beschreibung] |
| [TODO: TA.003] | [TODO: Nation-State] | [TODO: Espionage] | [TODO: Very High] | [TODO: Very High] | [TODO: Beschreibung] |

### 3.2 Threat Agent Profiles

#### TA.EXTERNAL_ATTACKER
**Agenten-ID:** TA.EXTERNAL_ATTACKER  
**Typ:** External Attacker  
**Skill Level:** [TODO: Expert / Proficient / Layman]

**Beschreibung:**
[TODO: Externer Angreifer ohne legitimen Zugang zum System, der versucht, über Netzwerk oder andere externe Schnittstellen einzudringen]

**Motivation:**
- **Primär:** [TODO: z.B. Finanzieller Gewinn, Datendiebstahl]
- **Sekundär:** [TODO: z.B. Reputation, Herausforderung]

**Fähigkeiten:**
- **Technische Expertise:** [TODO: High - Kenntnisse in Netzwerksicherheit, Exploitation]
- **Werkzeuge:** [TODO: Metasploit, Burp Suite, Custom Scripts]
- **Kenntnisse:** [TODO: Öffentlich verfügbare Informationen, OSINT]
- **Zugang:** [TODO: Netzwerkzugang, keine physischen Zugang]

**Ressourcen:**
- **Zeit:** [TODO: Wochen bis Monate]
- **Budget:** [TODO: $10,000 - $100,000]
- **Team:** [TODO: 1-5 Personen]
- **Infrastruktur:** [TODO: Cloud-Ressourcen, Botnets]

**Angriffsvektoren:**
- [TODO: Netzwerkangriffe (SQL Injection, XSS, etc.)]
- [TODO: Social Engineering (Phishing)]
- [TODO: Exploitation bekannter Schwachstellen]
- [TODO: Brute-Force-Angriffe]
- [TODO: DDoS-Angriffe]

**Angriffspotenzial:**
[TODO: High - Basierend auf CCRA Attack Potential Methodology]

**Beispielszenarien:**
1. [TODO: Szenario 1]
2. [TODO: Szenario 2]

---

#### TA.MALICIOUS_INSIDER
**Agenten-ID:** TA.MALICIOUS_INSIDER  
**Typ:** Insider  
**Skill Level:** [TODO: Expert / Proficient / Layman]

**Beschreibung:**
[TODO: Böswilliger Mitarbeiter mit legitimem Zugang zum System]

**Motivation:**
- **Primär:** [TODO: z.B. Rache, finanzieller Gewinn]
- **Sekundär:** [TODO: z.B. Ideologie, Erpressung]

**Fähigkeiten:**
- **Technische Expertise:** [TODO: Medium - Grundlegende IT-Kenntnisse]
- **Werkzeuge:** [TODO: Standard-Benutzertools, USB-Sticks]
- **Kenntnisse:** [TODO: Insider-Wissen über Systeme und Prozesse]
- **Zugang:** [TODO: Legitimer Benutzerzugang, physischer Zugang]

**Ressourcen:**
- **Zeit:** [TODO: Tage bis Wochen]
- **Budget:** [TODO: Minimal]
- **Team:** [TODO: Einzelperson]
- **Infrastruktur:** [TODO: Unternehmensressourcen]

**Angriffsvektoren:**
- [TODO: Datenexfiltration über USB oder E-Mail]
- [TODO: Sabotage von Systemen oder Daten]
- [TODO: Missbrauch von Zugriffsrechten]
- [TODO: Weitergabe von Credentials an Externe]

**Angriffspotenzial:**
[TODO: Medium-High - Insider-Zugang kompensiert niedrigere technische Fähigkeiten]

---

#### TA.PRIVILEGED_ADMIN
**Agenten-ID:** TA.PRIVILEGED_ADMIN  
**Typ:** Privileged Insider  
**Skill Level:** [TODO: Expert]

**Beschreibung:**
[TODO: Böswilliger Administrator mit privilegiertem Zugang]

**Motivation:**
- **Primär:** [TODO: z.B. Finanzieller Gewinn, Erpressung]
- **Sekundär:** [TODO: z.B. Rache, Ideologie]

**Fähigkeiten:**
- **Technische Expertise:** [TODO: High - Tiefes Systemverständnis]
- **Werkzeuge:** [TODO: Administrative Tools, Root-Zugang]
- **Kenntnisse:** [TODO: Vollständiges Insider-Wissen, Zugang zu Dokumentation]
- **Zugang:** [TODO: Privilegierter Zugang, physischer Zugang]

**Ressourcen:**
- **Zeit:** [TODO: Stunden bis Tage]
- **Budget:** [TODO: Minimal]
- **Team:** [TODO: Einzelperson]
- **Infrastruktur:** [TODO: Vollständiger Zugang zu Unternehmensressourcen]

**Angriffsvektoren:**
- [TODO: Direkte Datenmanipulation]
- [TODO: Deaktivierung von Sicherheitsmechanismen]
- [TODO: Erstellung von Backdoors]
- [TODO: Manipulation von Audit-Logs]
- [TODO: Privilege Escalation für andere Accounts]

**Angriffspotenzial:**
[TODO: Very High - Privilegierter Zugang ermöglicht nahezu alle Angriffe]

---

#### TA.NATION_STATE
**Agenten-ID:** TA.NATION_STATE  
**Typ:** Nation-State Actor  
**Skill Level:** [TODO: Expert]

**Beschreibung:**
[TODO: Staatlich unterstützter Angreifer mit umfangreichen Ressourcen]

[TODO: Füge weitere Threat Agents hinzu]

### 3.3 Attack Potential Assessment

#### 3.3.1 CCRA Methodology
**Common Criteria Recognition Arrangement (CCRA) Attack Potential:**

| Factor | Level | Points | Description |
|--------|-------|--------|-------------|
| **Elapsed Time** | < 1 day | 0 | [TODO] |
| | < 1 week | 1 | [TODO] |
| | < 1 month | 4 | [TODO] |
| | < 6 months | 10 | [TODO] |
| | > 6 months | 17 | [TODO] |
| **Expertise** | Layman | 0 | [TODO] |
| | Proficient | 3 | [TODO] |
| | Expert | 6 | [TODO] |
| **Knowledge** | Public | 0 | [TODO] |
| | Restricted | 3 | [TODO] |
| | Sensitive | 7 | [TODO] |
| **Window of Opportunity** | Unnecessary | 0 | [TODO] |
| | Easy | 1 | [TODO] |
| | Moderate | 4 | [TODO] |
| | Difficult | 10 | [TODO] |
| **Equipment** | Standard | 0 | [TODO] |
| | Specialized | 4 | [TODO] |
| | Bespoke | 7 | [TODO] |

#### 3.3.2 Attack Potential Ratings
**Angriffspotenzial-Bewertungen:**

| Agent ID | Elapsed Time | Expertise | Knowledge | Window | Equipment | Total | Rating |
|----------|--------------|-----------|-----------|--------|-----------|-------|--------|
| [TODO: TA.001] | [TODO: 4] | [TODO: 6] | [TODO: 3] | [TODO: 1] | [TODO: 4] | [TODO: 18] | [TODO: Moderate] |
| [TODO: TA.002] | [TODO: 1] | [TODO: 3] | [TODO: 7] | [TODO: 0] | [TODO: 0] | [TODO: 11] | [TODO: Enhanced-Basic] |

**Rating Scale:**
- **0-9 points:** Basic
- **10-13 points:** Enhanced-Basic
- **14-19 points:** Moderate
- **20-24 points:** High
- **≥25 points:** Beyond High

### 3.4 Threat Agent Capabilities Matrix

**Fähigkeiten-Matrix:**

| Agent | Network Access | Physical Access | Insider Knowledge | Technical Skills | Resources | Persistence |
|-------|---------------|-----------------|-------------------|------------------|-----------|-------------|
| [TODO: TA.001] | [TODO: Yes] | [TODO: No] | [TODO: No] | [TODO: High] | [TODO: High] | [TODO: High] |
| [TODO: TA.002] | [TODO: Yes] | [TODO: Yes] | [TODO: Yes] | [TODO: Medium] | [TODO: Low] | [TODO: Medium] |
| [TODO: TA.003] | [TODO: Yes] | [TODO: No] | [TODO: No] | [TODO: Expert] | [TODO: Very High] | [TODO: Very High] |

## 4. Asset-Agent Relationships

### 4.1 Asset-Agent Threat Matrix
**Welche Agenten bedrohen welche Assets:**

| Asset | TA.001 | TA.002 | TA.003 | TA.004 | TA.005 |
|-------|--------|--------|--------|--------|--------|
| [TODO: A.001] | [TODO: High] | [TODO: Medium] | [TODO: High] | [TODO: Low] | [TODO: Medium] |
| [TODO: A.002] | [TODO: Medium] | [TODO: High] | [TODO: Medium] | [TODO: Low] | [TODO: Low] |

### 4.2 High-Risk Combinations
**Hochrisiko-Kombinationen:**

| Asset | Agent | Risk Level | Rationale |
|-------|-------|------------|-----------|
| [TODO: A.001] | [TODO: TA.003] | [TODO: Critical] | [TODO: Hochwertige Daten + Hochqualifizierter Angreifer] |
| [TODO: A.002] | [TODO: TA.002] | [TODO: High] | [TODO: Kritischer Service + Insider-Zugang] |

## 5. Summary

### 5.1 Asset Summary
**Asset-Zusammenfassung:**
- Gesamtanzahl Assets: [TODO: Anzahl]
- Critical Assets: [TODO: Anzahl]
- High-Value Assets: [TODO: Anzahl]
- Medium-Value Assets: [TODO: Anzahl]
- Low-Value Assets: [TODO: Anzahl]

### 5.2 Threat Agent Summary
**Agenten-Zusammenfassung:**
- Gesamtanzahl Agenten: [TODO: Anzahl]
- External Attackers: [TODO: Anzahl]
- Insiders: [TODO: Anzahl]
- Privileged Insiders: [TODO: Anzahl]
- Nation-State Actors: [TODO: Anzahl]
- Other: [TODO: Anzahl]

### 5.3 Risk Overview
**Risikoübersicht:**
- Critical Risk Combinations: [TODO: Anzahl]
- High Risk Combinations: [TODO: Anzahl]
- Medium Risk Combinations: [TODO: Anzahl]
- Low Risk Combinations: [TODO: Anzahl]

---

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter mit TOE-spezifischen Assets und Agenten
2. Führe vollständige Asset-Identifikation durch
3. Dokumentiere alle relevanten Bedrohungsagenten
4. Bewerte Angriffspotenzial für alle Agenten
5. Erstelle Asset-Abhängigkeitsdiagramme
6. Überprüfe Konsistenz mit Threats (Template 0210) und Security Objectives (Template 0300)

