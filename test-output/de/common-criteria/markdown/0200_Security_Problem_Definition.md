# Security Problem Definition

**Dokument-ID:** 0200
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---



## 1. Security Problem Overview

### 1.1 Purpose
Dieses Dokument definiert das Sicherheitsproblem, das der TOE lösen soll. Es beschreibt:
- **Threats (Bedrohungen)**: Potenzielle Angriffe und Sicherheitsverletzungen
- **Organizational Security Policies (OSPs)**: Sicherheitsrichtlinien, die eingehalten werden müssen
- **Assumptions (Annahmen)**: Erwartungen an die Betriebsumgebung

### 1.2 Security Problem Context
**Anwendungskontext:**
[TODO: Beschreibe den Kontext, in dem der TOE eingesetzt wird]

**Sicherheitsrelevante Faktoren:**
- [TODO: Faktor 1]
- [TODO: Faktor 2]
- [TODO: Faktor 3]

### 1.3 Security Problem Scope
**Im Scope:**
- [TODO: Was wird durch die Sicherheitsproblem-Definition abgedeckt]

**Außerhalb des Scope:**
- [TODO: Was wird nicht abgedeckt]

## 2. Assets

### 2.1 Asset Identification
**Schützenswerte Assets:**

| Asset ID | Asset Name | Type | Value | Description |
|----------|------------|------|-------|-------------|
| [TODO: A.001] | [TODO: Asset-Name] | Data/Service/Function | High/Medium/Low | [TODO: Beschreibung] |
| [TODO: A.002] | [TODO: Asset-Name] | Data/Service/Function | High/Medium/Low | [TODO: Beschreibung] |
| [TODO: A.003] | [TODO: Asset-Name] | Data/Service/Function | High/Medium/Low | [TODO: Beschreibung] |

### 2.2 Asset Classification
**Daten-Assets:**
- [TODO: Daten-Asset 1]: [TODO: Klassifizierung und Schutzbedarf]
- [TODO: Daten-Asset 2]: [TODO: Klassifizierung und Schutzbedarf]

**Service-Assets:**
- [TODO: Service-Asset 1]: [TODO: Verfügbarkeitsanforderungen]
- [TODO: Service-Asset 2]: [TODO: Verfügbarkeitsanforderungen]

**Funktions-Assets:**
- [TODO: Funktions-Asset 1]: [TODO: Integritätsanforderungen]
- [TODO: Funktions-Asset 2]: [TODO: Integritätsanforderungen]

### 2.3 Asset Dependencies
[TODO: Beschreibe Abhängigkeiten zwischen Assets]

```
[TODO: Asset-Abhängigkeitsdiagramm einfügen]
```

## 3. Threat Agents

### 3.1 Threat Agent Profiles
**Identifizierte Bedrohungsagenten:**

| Agent ID | Agent Type | Motivation | Capability | Resources | Description |
|----------|------------|------------|------------|-----------|-------------|
| [TODO: TA.001] | [TODO: z.B. Insider, External Attacker] | [TODO: Motivation] | High/Medium/Low | High/Medium/Low | [TODO: Beschreibung] |
| [TODO: TA.002] | [TODO: Typ] | [TODO: Motivation] | High/Medium/Low | High/Medium/Low | [TODO: Beschreibung] |

### 3.2 Threat Agent Capabilities
**[TODO: Bedrohungsagent 1]**
- **Fähigkeiten**: [TODO: z.B. Netzwerkzugriff, physischer Zugriff, Insider-Wissen]
- **Ressourcen**: [TODO: z.B. Zeit, Budget, Werkzeuge]
- **Motivation**: [TODO: z.B. finanzieller Gewinn, Sabotage, Spionage]
- **Angriffsvektoren**: [TODO: Mögliche Angriffswege]

**[TODO: Bedrohungsagent 2]**
- [TODO: Details]

### 3.3 Attack Potential
**Bewertung des Angriffspotenzials:**

| Agent | Elapsed Time | Expertise | Knowledge | Window of Opportunity | Equipment | Attack Potential |
|-------|--------------|-----------|-----------|----------------------|-----------|------------------|
| [TODO: TA.001] | [TODO: < 1 day / < 1 month / > 1 month] | [TODO: Layman / Proficient / Expert] | [TODO: Public / Restricted / Sensitive] | [TODO: Unnecessary / Easy / Moderate / Difficult] | [TODO: Standard / Specialized / Bespoke] | [TODO: Basic / Enhanced-Basic / Moderate / High] |

## 4. Threats

### 4.1 Threat Catalog
**Identifizierte Bedrohungen:**

| Threat ID | Threat Name | Asset | Agent | Likelihood | Impact | Risk | Description |
|-----------|-------------|-------|-------|------------|--------|------|-------------|
| [TODO: T.001] | [TODO: Bedrohungsname] | [TODO: A.001] | [TODO: TA.001] | High/Medium/Low | High/Medium/Low | High/Medium/Low | [TODO: Beschreibung] |
| [TODO: T.002] | [TODO: Bedrohungsname] | [TODO: A.002] | [TODO: TA.002] | High/Medium/Low | High/Medium/Low | High/Medium/Low | [TODO: Beschreibung] |

### 4.2 Threat Details

#### T.001: [TODO: Bedrohungsname]
**Beschreibung:**
[TODO: Detaillierte Beschreibung der Bedrohung]

**Betroffene Assets:**
- [TODO: Asset 1]
- [TODO: Asset 2]

**Bedrohungsagent:**
- [TODO: TA.001]

**Angriffsszenario:**
1. [TODO: Schritt 1]
2. [TODO: Schritt 2]
3. [TODO: Schritt 3]

**Auswirkungen:**
- Vertraulichkeit: [TODO: High/Medium/Low/None]
- Integrität: [TODO: High/Medium/Low/None]
- Verfügbarkeit: [TODO: High/Medium/Low/None]

**Wahrscheinlichkeit:** [TODO: High/Medium/Low]

**Risikobewertung:** [TODO: High/Medium/Low]

#### T.002: [TODO: Bedrohungsname]
[TODO: Wiederhole die Struktur für jede Bedrohung]

### 4.3 Threat Scenarios
**Angriffsszenario 1: [TODO: Szenarioname]**
[TODO: Beschreibe ein vollständiges Angriffsszenario]

**Angriffsszenario 2: [TODO: Szenarioname]**
[TODO: Beschreibe ein weiteres Angriffsszenario]

## 5. Organizational Security Policies

### 5.1 OSP Catalog
**Organisatorische Sicherheitsrichtlinien:**

| OSP ID | OSP Name | Category | Mandatory | Description |
|--------|----------|----------|-----------|-------------|
| [TODO: P.001] | [TODO: Richtlinienname] | [TODO: z.B. Access Control, Audit, Crypto] | Yes/No | [TODO: Beschreibung] |
| [TODO: P.002] | [TODO: Richtlinienname] | [TODO: Kategorie] | Yes/No | [TODO: Beschreibung] |

### 5.2 OSP Details

#### P.001: [TODO: Richtlinienname]
**Beschreibung:**
[TODO: Detaillierte Beschreibung der Richtlinie]

**Zweck:**
[TODO: Warum ist diese Richtlinie erforderlich?]

**Anforderungen:**
- [TODO: Anforderung 1]
- [TODO: Anforderung 2]
- [TODO: Anforderung 3]

**Anwendungsbereich:**
[TODO: Wo gilt diese Richtlinie?]

**Compliance-Anforderungen:**
[TODO: Externe Standards oder Vorschriften, die diese Richtlinie erfüllt]

#### P.002: [TODO: Richtlinienname]
[TODO: Wiederhole die Struktur für jede OSP]

### 5.3 Policy Compliance Matrix
**Zuordnung von Richtlinien zu externen Standards:**

| OSP ID | ISO 27001 | NIST 800-53 | PCI-DSS | GDPR | Other |
|--------|-----------|-------------|---------|------|-------|
| [TODO: P.001] | [TODO: Control] | [TODO: Control] | [TODO: Req] | [TODO: Article] | [TODO: Standard] |
| [TODO: P.002] | [TODO: Control] | [TODO: Control] | [TODO: Req] | [TODO: Article] | [TODO: Standard] |

## 6. Assumptions

### 6.1 Assumption Catalog
**Annahmen über die Betriebsumgebung:**

| Assumption ID | Assumption Name | Category | Criticality | Description |
|---------------|-----------------|----------|-------------|-------------|
| [TODO: A.001] | [TODO: Annahmename] | [TODO: z.B. Physical, Personnel, Connectivity] | High/Medium/Low | [TODO: Beschreibung] |
| [TODO: A.002] | [TODO: Annahmename] | [TODO: Kategorie] | High/Medium/Low | [TODO: Beschreibung] |

### 6.2 Assumption Details

#### A.001: [TODO: Annahmename]
**Beschreibung:**
[TODO: Detaillierte Beschreibung der Annahme]

**Begründung:**
[TODO: Warum ist diese Annahme gerechtfertigt?]

**Auswirkungen:**
[TODO: Was passiert, wenn diese Annahme nicht erfüllt ist?]

**Verantwortlichkeit:**
[TODO: Wer ist für die Erfüllung dieser Annahme verantwortlich?]

**Verifikation:**
[TODO: Wie kann überprüft werden, dass diese Annahme erfüllt ist?]

#### A.002: [TODO: Annahmename]
[TODO: Wiederhole die Struktur für jede Annahme]

### 6.3 Environmental Assumptions
**Physische Umgebung:**
- [TODO: Annahme über physische Sicherheit]
- [TODO: Annahme über Umgebungsbedingungen]

**Personal:**
- [TODO: Annahme über Benutzerverhalten]
- [TODO: Annahme über Administratorkompetenzen]

**Konnektivität:**
- [TODO: Annahme über Netzwerksicherheit]
- [TODO: Annahme über Kommunikationskanäle]

## 7. Security Problem Summary

### 7.1 Threat Summary
**Zusammenfassung der Bedrohungen:**
- Anzahl identifizierter Bedrohungen: [TODO: Anzahl]
- Bedrohungen mit hohem Risiko: [TODO: Anzahl]
- Bedrohungen mit mittlerem Risiko: [TODO: Anzahl]
- Bedrohungen mit niedrigem Risiko: [TODO: Anzahl]

### 7.2 OSP Summary
**Zusammenfassung der Richtlinien:**
- Anzahl organisatorischer Sicherheitsrichtlinien: [TODO: Anzahl]
- Verpflichtende Richtlinien: [TODO: Anzahl]
- Optionale Richtlinien: [TODO: Anzahl]

### 7.3 Assumption Summary
**Zusammenfassung der Annahmen:**
- Anzahl der Annahmen: [TODO: Anzahl]
- Kritische Annahmen: [TODO: Anzahl]
- Annahmen mit mittlerer Kritikalität: [TODO: Anzahl]
- Annahmen mit niedriger Kritikalität: [TODO: Anzahl]

### 7.4 Coverage Analysis
**Abdeckungsanalyse:**
[TODO: Analysiere, ob alle Assets durch Bedrohungen, OSPs oder Annahmen abgedeckt sind]

## 8. Traceability

### 8.1 Asset-to-Threat Mapping
**Zuordnung von Assets zu Bedrohungen:**

| Asset ID | Threats |
|----------|---------|
| [TODO: A.001] | [TODO: T.001, T.003, T.005] |
| [TODO: A.002] | [TODO: T.002, T.004] |

### 8.2 Threat-to-Agent Mapping
**Zuordnung von Bedrohungen zu Agenten:**

| Threat ID | Threat Agents |
|-----------|---------------|
| [TODO: T.001] | [TODO: TA.001, TA.002] |
| [TODO: T.002] | [TODO: TA.003] |

### 8.3 Security Problem Traceability Matrix
**Vollständige Rückverfolgbarkeit:**

| Asset | Threat | OSP | Assumption | Agent |
|-------|--------|-----|------------|-------|
| [TODO: A.001] | [TODO: T.001] | [TODO: P.001] | [TODO: A.001] | [TODO: TA.001] |
| [TODO: A.002] | [TODO: T.002] | [TODO: P.002] | [TODO: A.002] | [TODO: TA.002] |

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter mit TOE-spezifischen Informationen
2. Führe eine vollständige Bedrohungsanalyse durch
3. Dokumentiere alle relevanten OSPs
4. Identifiziere und validiere alle Annahmen
5. Erstelle Bedrohungsmodell und Angriffsszenarien
6. Überprüfe die Konsistenz mit Security Objectives (Template 0300)

