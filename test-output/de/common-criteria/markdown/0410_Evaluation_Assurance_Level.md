# Evaluation Assurance Level (EAL)

**Dokument-ID:** 0410
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

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches Target of Evaluation (TOE) an.



## 1. Einleitung

Dieses Dokument beschreibt die Auswahl und Begründung des Evaluation Assurance Level (EAL) für das TOE. Das EAL definiert die Tiefe und Strenge der Sicherheitsevaluierung gemäß ISO/IEC 15408-3.

## 2. EAL-Übersicht

Common Criteria definiert sieben vordefinierte Evaluation Assurance Levels:

| EAL | Bezeichnung | Beschreibung | Typische Anwendung |
|-----|-------------|--------------|-------------------|
| EAL1 | Functionally tested | Grundlegende Funktionsprüfung | Kommerzielle Standardprodukte |
| EAL2 | Structurally tested | Strukturelle Prüfung mit Entwicklerdokumentation | Kommerzielle Produkte mit Sicherheitsfunktionen |
| EAL3 | Methodically tested and checked | Methodische Prüfung und Überprüfung | Sicherheitsprodukte mit moderaten Anforderungen |
| EAL4 | Methodically designed, tested, and reviewed | Methodisches Design, Test und Review | Sicherheitsprodukte für kommerzielle Umgebungen |
| EAL5 | Semiformally designed and tested | Semiformales Design und Test | Hochsicherheitsprodukte |
| EAL6 | Semiformally verified design and tested | Semiformale Verifikation und Test | Hochsicherheitsumgebungen mit hohem Risiko |
| EAL7 | Formally verified design and tested | Formale Verifikation und Test | Extrem hohe Sicherheitsanforderungen |

## 3. Gewähltes EAL

**Gewähltes Evaluation Assurance Level:** [TODO: z.B. EAL4]

### 3.1 Begründung der EAL-Auswahl

[TODO: Begründe die Auswahl des EAL basierend auf:]
- Bedrohungslandschaft und Risikobewertung
- Schutzbedarf der zu schützenden Assets
- Einsatzumgebung des TOE
- Kosten-Nutzen-Verhältnis
- Marktanforderungen und regulatorische Vorgaben
- Entwicklungsressourcen und -zeitplan

**Beispiel:**
```
EAL4 wurde gewählt, da es ein ausgewogenes Verhältnis zwischen Sicherheitsvertrauen und 
Entwicklungsaufwand bietet. Das TOE wird in kommerziellen Umgebungen mit moderaten bis 
hohen Sicherheitsanforderungen eingesetzt. EAL4 erfordert methodisches Design, Test und 
Review, was den Sicherheitsanforderungen der Zielumgebung entspricht, ohne die formalen 
Verifikationsanforderungen höherer EALs zu benötigen.
```

### 3.2 Alternativen und Abwägungen

[TODO: Diskutiere alternative EALs und warum sie nicht gewählt wurden]

**Niedrigere EALs (z.B. EAL3):**
- [TODO: Warum nicht ausreichend?]

**Höhere EALs (z.B. EAL5+):**
- [TODO: Warum nicht erforderlich oder nicht praktikabel?]

## 4. Security Assurance Requirements (SARs) für gewähltes EAL

### 4.1 Mandatory SARs für EAL [TODO: X]

Die folgenden Security Assurance Requirements sind für EAL [TODO: X] verpflichtend:

#### 4.1.1 Security Target Evaluation (ASE)

- **ASE_CCL.1** Conformance claims
- **ASE_ECD.1** Extended components definition
- **ASE_INT.1** ST introduction
- **ASE_OBJ.2** Security objectives
- **ASE_REQ.2** Derived security requirements
- **ASE_SPD.1** Security problem definition
- **ASE_TSS.1** TOE summary specification

#### 4.1.2 Development (ADV)

[TODO: Füge ADV-Komponenten für gewähltes EAL hinzu]

**Für EAL4:**
- **ADV_ARC.1** Security architecture description
- **ADV_FSP.4** Complete functional specification
- **ADV_IMP.1** Implementation representation of the TSF
- **ADV_TDS.3** Basic modular design

#### 4.1.3 Guidance Documents (AGD)

- **AGD_OPE.1** Operational user guidance
- **AGD_PRE.1** Preparative procedures

#### 4.1.4 Life-cycle Support (ALC)

[TODO: Füge ALC-Komponenten für gewähltes EAL hinzu]

**Für EAL4:**
- **ALC_CMC.4** Production support, acceptance procedures and automation
- **ALC_CMS.4** Problem tracking CM coverage
- **ALC_DEL.1** Delivery procedures
- **ALC_DVS.1** Identification of security measures
- **ALC_LCD.1** Developer defined life-cycle model
- **ALC_TAT.1** Well-defined development tools

#### 4.1.5 Tests (ATE)

[TODO: Füge ATE-Komponenten für gewähltes EAL hinzu]

**Für EAL4:**
- **ATE_COV.2** Analysis of coverage
- **ATE_DPT.1** Testing: high-level design
- **ATE_FUN.1** Functional testing
- **ATE_IND.2** Independent testing - sample

#### 4.1.6 Vulnerability Assessment (AVA)

[TODO: Füge AVA-Komponenten für gewähltes EAL hinzu]

**Für EAL4:**
- **AVA_VAN.3** Focused vulnerability analysis

### 4.2 Augmentation (Zusätzliche SARs)

[TODO: Falls zusätzliche SARs über das gewählte EAL hinaus verwendet werden, liste und begründe sie hier]

**Beispiel:**
```
Zusätzlich zu den EAL4-Anforderungen werden folgende SARs hinzugefügt:
- ALC_FLR.2 Flaw reporting procedures (aus EAL5)
  Begründung: Verbesserte Schwachstellenverwaltung für produktive Umgebungen
```

## 5. Entwicklungs- und Evaluierungsaufwand

### 5.1 Entwicklungsaufwand

[TODO: Schätze den zusätzlichen Entwicklungsaufwand für das gewählte EAL]

**Dokumentationsaufwand:**
- [TODO: Erforderliche Dokumente und geschätzter Aufwand]

**Prozessanforderungen:**
- [TODO: Erforderliche Entwicklungsprozesse und -werkzeuge]

**Testaufwand:**
- [TODO: Erforderliche Tests und Testabdeckung]

### 5.2 Evaluierungsaufwand

[TODO: Schätze Dauer und Kosten der Evaluierung]

**Geschätzte Evaluierungsdauer:** [TODO: z.B. 6-12 Monate]  
**Geschätzte Evaluierungskosten:** [TODO: Kostenrahmen]  
**Evaluierungslabor:** [TODO: Geplantes oder ausgewähltes Labor]

## 6. Compliance und Zertifizierung

### 6.1 Zertifizierungsschema

[TODO: Spezifiziere das Zertifizierungsschema]

**Beispiele:**
- Common Criteria Recognition Arrangement (CCRA)
- Nationales Schema (z.B. BSI Deutschland, ANSSI Frankreich)
- [TODO: Spezifisches Schema]

### 6.2 Mutual Recognition

[TODO: Beschreibe Mutual Recognition Agreements, falls relevant]

Das gewählte EAL und Zertifizierungsschema ermöglicht die Anerkennung in folgenden Ländern:
- [TODO: Liste der Länder mit Mutual Recognition]

## 7. Zeitplan und Meilensteine

[TODO: Erstelle einen groben Zeitplan für die Evaluierung]

| Meilenstein | Geplantes Datum | Status |
|-------------|-----------------|--------|
| ST-Fertigstellung | [TODO] | [TODO] |
| Evaluierungsbeginn | [TODO] | [TODO] |
| ADV-Phase abgeschlossen | [TODO] | [TODO] |
| ATE-Phase abgeschlossen | [TODO] | [TODO] |
| AVA-Phase abgeschlossen | [TODO] | [TODO] |
| Zertifizierung | [TODO] | [TODO] |

## 8. Risiken und Mitigation

[TODO: Identifiziere Risiken für die Evaluierung]

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|--------|-------------------|------------|------------|
| [TODO: z.B. Verzögerungen in der Dokumentation] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

## 9. Referenzen

- ISO/IEC 15408-3:2022 - Security assurance requirements
- Common Criteria for Information Technology Security Evaluation - Evaluation Assurance Levels
- [TODO: Nationale Zertifizierungsrichtlinien]
- [TODO: Weitere relevante Dokumente]

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter
2. Validiere die EAL-Auswahl mit Stakeholdern
3. Bestätige die Verfügbarkeit von Ressourcen für die Evaluierung
4. Kontaktiere potenzielle Evaluierungslabore
5. Erstelle detaillierten Projektplan für die Evaluierung

