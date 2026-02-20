# TOE Summary Specification

**Dokument-ID:** COMMON-CRITERIA-0500
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

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches TOE (Target of Evaluation) an.



## 1. Einleitung

### 1.1 Zweck

Dieses Dokument beschreibt die TOE Summary Specification (TSS) für **[TODO: TOE-Name]**. Die TSS zeigt, wie das TOE die in Kapitel 4 (Security Requirements) definierten Sicherheitsfunktionsanforderungen (SFRs) und Sicherungsanforderungen (SARs) erfüllt.



### 1.2 Struktur der TSS

Die TOE Summary Specification ist wie folgt strukturiert:

- **Kapitel 2**: Übersicht der TOE-Sicherheitsfunktionen (TSFs)
- **Kapitel 3**: Detaillierte Beschreibung der Sicherheitsfunktionen
- **Kapitel 4**: Zuordnung von Sicherheitsfunktionen zu SFRs (Coverage Matrix)
- **Kapitel 5**: Sicherungsmaßnahmen (Assurance Measures)
- **Kapitel 6**: Stärke der Sicherheitsfunktionen (Strength of Function)

## 2. Übersicht der TOE-Sicherheitsfunktionen

### 2.1 Sicherheitsfunktionen - Übersicht

Das TOE implementiert folgende Sicherheitsfunktionen (TSFs):

| TSF-ID | Sicherheitsfunktion | Beschreibung | Zugeordnete SFRs |
|--------|---------------------|--------------|------------------|
| TSF-1 | [TODO: Name] | [TODO: Kurzbeschreibung] | [TODO: SFR-IDs] |
| TSF-2 | [TODO: Name] | [TODO: Kurzbeschreibung] | [TODO: SFR-IDs] |
| TSF-3 | [TODO: Name] | [TODO: Kurzbeschreibung] | [TODO: SFR-IDs] |



### 2.2 Architektur der Sicherheitsfunktionen

```
[TODO: Diagramm einfügen - Architektur der TSFs]

Beispiel:
┌─────────────────────────────────────────────────┐
│           TOE Security Functions                │
├─────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐            │
│  │ TSF-1: I&A   │  │ TSF-2: Access│            │
│  │              │  │ Control      │            │
│  └──────────────┘  └──────────────┘            │
│  ┌──────────────┐  ┌──────────────┐            │
│  │ TSF-3: Audit │  │ TSF-4: Crypto│            │
│  │              │  │              │            │
│  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────┘
```



**Beschreibung:**

[TODO: Beschreibe die Architektur der Sicherheitsfunktionen. Erkläre, wie die verschiedenen TSFs zusammenarbeiten und welche Abhängigkeiten bestehen.]

## 3. Detaillierte Beschreibung der Sicherheitsfunktionen



### 3.1 TSF-1: [TODO: Name der Sicherheitsfunktion]

**TSF-ID:** TSF-1  
**Zugeordnete SFRs:** [TODO: z.B. FIA_UID.1, FIA_UAU.1]

#### 3.1.1 Funktionsbeschreibung

[TODO: Beschreibe die Sicherheitsfunktion im Detail. Erkläre:
- Was die Funktion tut
- Wie sie funktioniert (auf angemessenem Abstraktionsniveau)
- Welche Eingaben sie verarbeitet
- Welche Ausgaben sie erzeugt
- Welche Sicherheitseigenschaften sie gewährleistet]

**Beispiel:**
Die Identifikations- und Authentisierungsfunktion (TSF-1) stellt sicher, dass alle Benutzer vor dem Zugriff auf TOE-Funktionen identifiziert und authentisiert werden. Die Funktion verwendet einen Benutzernamen zur Identifikation und ein Passwort zur Authentisierung. Passwörter werden mit SHA-256 gehasht und gesalzen gespeichert.

#### 3.1.2 Erfüllung der SFRs

[TODO: Erkläre für jede zugeordnete SFR, wie diese Sicherheitsfunktion die Anforderung erfüllt.]

**SFR [TODO: ID]:**
- [TODO: Beschreibung, wie die SFR erfüllt wird]

**SFR [TODO: ID]:**
- [TODO: Beschreibung, wie die SFR erfüllt wird]

#### 3.1.3 Schnittstellen

[TODO: Beschreibe die Schnittstellen dieser TSF zu anderen TSFs oder externen Komponenten.]

- **Schnittstelle zu TSF-X:** [TODO: Beschreibung]
- **Externe Schnittstellen:** [TODO: Beschreibung]

### 3.2 TSF-2: [TODO: Name der Sicherheitsfunktion]

**TSF-ID:** TSF-2  
**Zugeordnete SFRs:** [TODO: SFR-IDs]

#### 3.2.1 Funktionsbeschreibung

[TODO: Beschreibung analog zu 3.1.1]

#### 3.2.2 Erfüllung der SFRs

[TODO: Beschreibung analog zu 3.1.2]

#### 3.2.3 Schnittstellen

[TODO: Beschreibung analog zu 3.1.3]

### 3.3 TSF-3: [TODO: Name der Sicherheitsfunktion]

[TODO: Weitere Sicherheitsfunktionen nach dem gleichen Schema beschreiben]

## 4. Zuordnung von Sicherheitsfunktionen zu SFRs

### 4.1 Coverage Matrix

Die folgende Tabelle zeigt die Zuordnung zwischen Sicherheitsfunktionen (TSFs) und Sicherheitsfunktionsanforderungen (SFRs):

| SFR-ID | SFR-Name | TSF-1 | TSF-2 | TSF-3 | TSF-4 | TSF-5 |
|--------|----------|-------|-------|-------|-------|-------|
| [TODO] | [TODO]   | X     |       |       |       |       |
| [TODO] | [TODO]   | X     | X     |       |       |       |
| [TODO] | [TODO]   |       | X     |       |       |       |
| [TODO] | [TODO]   |       |       | X     |       |       |



### 4.2 Vollständigkeitsprüfung

**Abdeckung der SFRs:**
- Anzahl der SFRs: [TODO: Anzahl]
- Anzahl der abgedeckten SFRs: [TODO: Anzahl]
- Abdeckungsgrad: [TODO: Prozent]

**Nicht abgedeckte SFRs:**
[TODO: Liste alle SFRs auf, die nicht durch TSFs abgedeckt sind. Wenn alle abgedeckt sind, schreibe "Keine".]



## 5. Sicherungsmaßnahmen (Assurance Measures)

### 5.1 Übersicht

Die folgenden Sicherungsmaßnahmen (Assurance Measures) werden implementiert, um die Sicherungsanforderungen (SARs) zu erfüllen:

| SAR-ID | SAR-Name | Assurance Measure | Beschreibung |
|--------|----------|-------------------|--------------|
| [TODO] | [TODO]   | [TODO]            | [TODO]       |
| [TODO] | [TODO]   | [TODO]            | [TODO]       |



### 5.2 Zuordnung zu Evaluation Assurance Level

Das TOE wird auf **[TODO: EAL-Level, z.B. EAL4]** evaluiert. Die folgenden Assurance Measures unterstützen dieses EAL:

[TODO: Liste die Assurance Measures auf, die für das gewählte EAL erforderlich sind.]

**Beispiel für EAL4:**
- Configuration Management (ACM_CAP.4, ACM_SCP.2)
- Delivery and Operation (ADO_DEL.2, ADO_IGS.1)
- Development (ADV_FSP.2, ADV_IMP.1, ADV_TDS.2)
- Guidance Documents (AGD_ADM.1, AGD_USR.1)
- Life Cycle Support (ALC_DVS.1, ALC_LCD.1, ALC_TAT.1)
- Tests (ATE_COV.2, ATE_DPT.1, ATE_FUN.1, ATE_IND.2)
- Vulnerability Assessment (AVA_MSU.2, AVA_SOF.1, AVA_VLA.2)

## 6. Stärke der Sicherheitsfunktionen (Strength of Function)

### 6.1 SOF-Claim

Das TOE beansprucht folgende Stärke der Sicherheitsfunktionen (Strength of Function):

**SOF-Claim:** [TODO: SOF-basic / SOF-medium / SOF-high]



### 6.2 SOF-Analyse

Die folgende Tabelle zeigt die Stärke der einzelnen probabilistischen oder permutationsbasierten Sicherheitsmechanismen:

| TSF-ID | Mechanismus | SOF-Level | Begründung |
|--------|-------------|-----------|------------|
| [TODO] | [TODO]      | [TODO]    | [TODO]     |
| [TODO] | [TODO]      | [TODO]    | [TODO]     |



### 6.3 Erfüllung des SOF-Claims

[TODO: Erkläre, wie die analysierten Mechanismen den SOF-Claim erfüllen. Zeige, dass alle relevanten Mechanismen mindestens das beanspruchte SOF-Level erreichen.]

**Zusammenfassung:**
- Anzahl der analysierten Mechanismen: [TODO]
- Niedrigstes SOF-Level: [TODO]
- Erfüllung des SOF-Claims: [TODO: Ja/Nein]

## 7. Zusammenfassung

### 7.1 Vollständigkeit der TSS

Die TOE Summary Specification ist vollständig und deckt alle Aspekte ab:

- ✓ Alle SFRs sind durch TSFs abgedeckt
- ✓ Alle SARs sind durch Assurance Measures abgedeckt
- ✓ SOF-Claim ist analysiert und begründet
- ✓ Alle Sicherheitsfunktionen sind detailliert beschrieben

### 7.2 Verweis auf weitere Dokumente

Für detaillierte Informationen siehe:

- **0510_Assurance_Measures.md**: Detaillierte Beschreibung der Sicherungsmaßnahmen
- **0520_Functions_Rationale.md**: Begründung der Zuordnung von TSFs zu SFRs
- **0530_Coverage_Matrix.md**: Vollständige Coverage Matrix
- **0540_Strength_of_Function.md**: Detaillierte SOF-Analyse

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [TODO] | [TODO] | Initiale Version |
| 1.0 | [TODO] | [TODO] | [TODO] |

