# Common Criteria Framework-Mapping

**Dokument-ID:** [FRAMEWORK]-9999
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

## Überblick

Dieses Dokument bildet die Common Criteria Security Target Templates auf die ISO/IEC 15408 Standardkomponenten und Evaluation Assurance Levels (EAL) ab. Es bietet Rückverfolgbarkeit zwischen Template-Dateien und spezifischen Common Criteria Anforderungen und stellt eine umfassende Abdeckung der Security Target Struktur sicher.

## ISO/IEC 15408 Standardstruktur

Der Common Criteria Standard besteht aus drei Teilen:

- **ISO/IEC 15408-1**: Einführung und allgemeines Modell
- **ISO/IEC 15408-2**: Funktionale Sicherheitskomponenten (SFRs)
- **ISO/IEC 15408-3**: Vertrauenswürdigkeitskomponenten (SARs)

## Template-Mapping zu ISO/IEC 15408-1 (Security Target Struktur)

### Teil 1: ST-Einführung (ISO/IEC 15408-1, Abschnitt 8.1)

Der ST-Einführungsabschnitt bietet Identifikations- und Übersichtsinformationen über das Security Target und den TOE.

| Template | ISO/IEC 15408-1 Referenz | Beschreibung |
|----------|---------------------------|--------------|
| 0010_ST_Introduction.md | Abschnitt 8.1.1 | ST Introduction: ST-Identifikation, ST-Überblick, ST-Konventionen |
| 0020_TOE_Overview.md | Abschnitt 8.1.2 | TOE Overview: Allgemeine Beschreibung und Überblick über das Evaluierungsobjekt |
| 0030_TOE_Description_Summary.md | Abschnitt 8.1.2 | Zusammenfassung der TOE-Beschreibung |
| 0040_Conformance_Claims.md | Abschnitt 8.1.3 | Conformance Claims: CC-Konformitätsanspruch, PP-Konformitätsanspruch, Paket-Konformitätsanspruch |
| 0050_Document_Conventions.md | Abschnitt 8.1.4 | Document Conventions: Notation, Terminologie und Konventionen |

### Teil 2: TOE-Beschreibung / TOE Description (ISO/IEC 15408-1, Abschnitt 8.2)

Der TOE-Beschreibungsabschnitt bietet detaillierte Informationen über das Evaluierungsobjekt.

| Template | ISO/IEC 15408-1 Referenz | Beschreibung |
|----------|---------------------------|--------------|
| 0100_TOE_Physical_Scope.md | Abschnitt 8.2.1 | Physical Scope: Physischer Umfang des TOE (Hardware, Software, Firmware, Anleitungen) |
| 0110_TOE_Logical_Scope.md | Abschnitt 8.2.2 | Logical Scope: Logischer Umfang des TOE (Sicherheitsfunktionen und -merkmale) |
| 0120_TOE_Interfaces.md | Abschnitt 8.2.3 | Interfaces: TOE-Schnittstellen (Benutzer, Administrator, externe Systeme) |
| 0130_TOE_Architecture.md | Abschnitt 8.2.4 | Architecture: TOE-Architektur und Subsysteme |
| 0140_TOE_Lifecycle.md | Abschnitt 8.2.5 | Lifecycle: TOE-Lebenszyklus (Entwicklung, Bereitstellung, Betrieb, Wartung) |

### Teil 3: Sicherheitsproblem-Definition / Security Problem Definition (ISO/IEC 15408-1, Abschnitt 8.3)

| Template | ISO/IEC 15408-1 Referenz | Beschreibung |
|----------|---------------------------|--------------|
| 0200_Security_Problem_Definition.md | Abschnitt 8.3 | Überblick über die Sicherheitsproblem-Definition |
| 0210_Threats.md | Abschnitt 8.3.1 | Bedrohungen für den TOE und Assets |
| 0220_Organizational_Security_Policies.md | Abschnitt 8.3.2 | Organisatorische Sicherheitsrichtlinien (OSPs) |
| 0230_Assumptions.md | Abschnitt 8.3.3 | Annahmen über die Betriebsumgebung |
| 0240_Threat_Agents_and_Assets.md | Abschnitt 8.3.1 | Bedrohungsakteure (Angreifer) und zu schützende Assets |

### Teil 4: Sicherheitsziele / Security Objectives (ISO/IEC 15408-1, Abschnitt 8.4)

| Template | ISO/IEC 15408-1 Referenz | Beschreibung |
|----------|---------------------------|--------------|
| 0300_Security_Objectives.md | Abschnitt 8.4 | Überblick über Sicherheitsziele |
| 0310_Security_Objectives_Rationale.md | Abschnitt 8.4.1, 8.4.2 | Sicherheitsziele für den TOE und die Betriebsumgebung |
| 0320_Security_Objectives_Coverage_Matrix.md | Abschnitt 8.4.3 | Begründung der Sicherheitsziele und Abdeckungsmatrix |
| 0330_Security_Objectives_Summary.md | Abschnitt 8.4 | Zusammenfassung der Sicherheitsziele |

### Teil 5: Sicherheitsanforderungen / Security Requirements (ISO/IEC 15408-1, Abschnitt 8.5)

| Template | ISO/IEC 15408-1 Referenz | Beschreibung |
|----------|---------------------------|--------------|
| 0400_Security_Requirements.md | Abschnitt 8.5 | Überblick über Sicherheitsanforderungen |
| 0410_Evaluation_Assurance_Level.md | Abschnitt 8.5.2 | Vertrauenswürdigkeitsanforderungen (SARs) und EAL-Auswahl |
| 0420_Requirements_Rationale.md | Abschnitt 8.5.3 | Begründung der Sicherheitsanforderungen |
| 0430_SFR_Dependencies.md | Abschnitt 8.5.3 | SFR-Abhängigkeiten und deren Erfüllung |
| 0440_Coverage_Matrix.md | Abschnitt 8.5.3 | Anforderungs-Abdeckungsmatrix (SFRs/Ziele) |

### Teil 6: TOE-Zusammenfassende Spezifikation / TOE Summary Specification (ISO/IEC 15408-1, Abschnitt 8.6)

Die TOE-Zusammenfassende Spezifikation beschreibt, wie der TOE die Sicherheitsanforderungen erfüllt.

| Template | ISO/IEC 15408-1 Referenz | Beschreibung |
|----------|---------------------------|--------------|
| 0500_TOE_Summary_Specification.md | Abschnitt 8.6 | Überblick über die zusammenfassende TOE-Spezifikation |
| 0510_Assurance_Measures.md | Abschnitt 8.6.2 | Assurance Measures: Vertrauenswürdigkeitsmaßnahmen, die im TOE implementiert sind |
| 0520_Functions_Rationale.md | Abschnitt 8.6.3 | Functions Rationale: Begründung der TOE-Sicherheitsfunktionen |
| 0530_Coverage_Matrix.md | Abschnitt 8.6.3 | Funktions-Abdeckungsmatrix (TSFs/SFRs) |
| 0540_Strength_of_Function.md | Abschnitt 8.6.1 | Strength of Function: Funktionsstärke-Ansprüche |

### Teil 7: Anhänge und unterstützende Dokumentation

| Template | ISO/IEC 15408-1 Referenz | Beschreibung |
|----------|---------------------------|--------------|
| 0600_PP_Conformance.md | Abschnitt 8.1.3 | Nachweis der Protection Profile Konformität |
| 0610_Rationale_for_Objectives.md | Abschnitt 8.4.3 | Detaillierte Begründung für Sicherheitsziele |
| 0620_Rationale_for_Requirements.md | Abschnitt 8.5.3 | Detaillierte Begründung für Sicherheitsanforderungen |
| 0630_Glossary.md | Abschnitt 8.1.4 | Glossar der Begriffe und Akronyme |
| 0640_References.md | N/A | Verweise auf Standards, Spezifikationen und Dokumentation |
| 0650_Evidence_and_Documentation.md | N/A | Unterstützende Nachweise und Evaluierungsdokumentation |

## Funktionale Sicherheitsanforderungen (ISO/IEC 15408-2)

Die funktionalen Sicherheitsanforderungen (SFRs) sind in ISO/IEC 15408-2 definiert und in 11 funktionale Klassen organisiert. Die Templates 0400-0440 sollten auf entsprechende SFRs aus diesen Klassen verweisen:

### SFR-Klassen

| Klasse | Name | Beschreibung | Template-Referenz |
|--------|------|--------------|-------------------|
| FAU | Sicherheitsaudit | Audit-Datengenerierung, Analyse, Überprüfung, Speicherung | 0400, 0430, 0440 |
| FCO | Kommunikation | Nichtabstreitbarkeit von Ursprung und Empfang | 0400, 0430, 0440 |
| FCS | Kryptografische Unterstützung | Kryptografisches Schlüsselmanagement und Operationen | 0400, 0430, 0440 |
| FDP | Benutzerdatenschutz | Zugriffskontrolle, Datenauthentifizierung, Restinformationsschutz | 0400, 0430, 0440 |
| FIA | Identifikation und Authentifizierung | Benutzerauthentifizierung, Authentifizierungsfehler | 0400, 0430, 0440 |
| FMT | Sicherheitsmanagement | Verwaltung von Sicherheitsattributen, Funktionen und Daten | 0400, 0430, 0440 |
| FPR | Datenschutz | Anonymität, Pseudonymität, Unverkettbarkeit, Unbeobachtbarkeit | 0400, 0430, 0440 |
| FPT | Schutz der TSF | Physischer TSF-Schutz, Selbsttest, vertrauenswürdige Wiederherstellung | 0400, 0430, 0440 |
| FRU | Ressourcennutzung | Fehlertoleranz, Dienstpriorität, Ressourcenzuweisung | 0400, 0430, 0440 |
| FTA | TOE-Zugriff | Sitzungssperre, TOE-Zugriffsverlauf, Zugriffsbanner | 0400, 0430, 0440 |
| FTP | Vertrauenswürdiger Pfad/Kanäle | Vertrauenswürdiger Pfad, vertrauenswürdige Kanäle | 0400, 0430, 0440 |

## Vertrauenswürdigkeitsanforderungen (ISO/IEC 15408-3)

Die Vertrauenswürdigkeitsanforderungen (SARs) sind in ISO/IEC 15408-3 definiert und in 10 Vertrauenswürdigkeitsklassen organisiert. Die Templates 0410 und 0510 sollten auf entsprechende SARs basierend auf dem gewählten EAL verweisen:

### SAR-Klassen

| Klasse | Name | Beschreibung | Template-Referenz |
|--------|------|--------------|-------------------|
| ADV | Entwicklung | Sicherheitsarchitektur, funktionale Spezifikation, Implementierungsdarstellung | 0410, 0510 |
| AGD | Anleitungsdokumente | Betriebsbenutzeranleitung, vorbereitende Verfahren | 0410, 0510 |
| ALC | Lebenszyklus-Unterstützung | CM-Fähigkeiten, Auslieferung, Entwicklungssicherheit, Fehlerbehebung | 0410, 0510 |
| ATE | Tests | Abdeckung, Tiefe, funktionale Tests, unabhängige Tests | 0410, 0510 |
| AVA | Schwachstellenbewertung | Schwachstellenanalyse, verdeckte Kanalanalyse, Missbrauchsanalyse | 0410, 0510 |
| ACO | Komposition | Kompositionsbegründung (für zusammengesetzte Evaluierungen) | 0410, 0510 |
| ASE | Security Target Evaluierung | ST-Einführung, Konformitätsansprüche, Sicherheitsproblem-Definition | 0410, 0510 |

## Evaluation Assurance Levels (EAL)

Die Templates unterstützen alle sieben Evaluation Assurance Levels. Template 0410 sollte das gewählte EAL und die entsprechenden SARs spezifizieren:

### EAL1: Funktional getestet

| SAR-Komponente | Beschreibung | Template-Referenz |
|----------------|--------------|-------------------|
| ADV_FSP.1 | Grundlegende funktionale Spezifikation | 0410, 0510 |
| AGD_OPE.1 | Betriebsbenutzeranleitung | 0410, 0510 |
| AGD_PRE.1 | Vorbereitende Verfahren | 0410, 0510 |
| ALC_CMC.1 | Kennzeichnung des TOE | 0410, 0510 |
| ALC_CMS.1 | TOE CM-Abdeckung | 0410, 0510 |
| ATE_IND.1 | Unabhängige Tests - Konformität | 0410, 0510 |
| AVA_VAN.1 | Schwachstellenuntersuchung | 0410, 0510 |

### EAL2: Strukturell getestet

EAL2 umfasst alle EAL1-Komponenten plus:

| SAR-Komponente | Beschreibung | Template-Referenz |
|----------------|--------------|-------------------|
| ADV_ARC.1 | Beschreibung der Sicherheitsarchitektur | 0410, 0510 |
| ADV_FSP.2 | Sicherheitserzwingende funktionale Spezifikation | 0410, 0510 |
| AGD_OPE.1 | Betriebsbenutzeranleitung | 0410, 0510 |
| AGD_PRE.1 | Vorbereitende Verfahren | 0410, 0510 |
| ALC_CMC.2 | Verwendung eines CM-Systems | 0410, 0510 |
| ALC_CMS.2 | Teile der TOE CM-Abdeckung | 0410, 0510 |
| ALC_DEL.1 | Auslieferungsverfahren | 0410, 0510 |
| ATE_COV.1 | Nachweis der Abdeckung | 0410, 0510 |
| ATE_FUN.1 | Funktionale Tests | 0410, 0510 |
| ATE_IND.2 | Unabhängige Tests - Stichprobe | 0410, 0510 |
| AVA_VAN.2 | Schwachstellenanalyse | 0410, 0510 |

### EAL3: Methodisch getestet und geprüft

EAL3 umfasst alle EAL2-Komponenten plus:

| SAR-Komponente | Beschreibung | Template-Referenz |
|----------------|--------------|-------------------|
| ADV_FSP.3 | Funktionale Spezifikation mit vollständiger Zusammenfassung | 0410, 0510 |
| ADV_TDS.1 | Grundlegendes Design | 0410, 0510 |
| ALC_CMC.3 | Autorisierungskontrollen | 0410, 0510 |
| ALC_CMS.3 | Implementierungsdarstellung CM-Abdeckung | 0410, 0510 |
| ALC_DEL.1 | Auslieferungsverfahren | 0410, 0510 |
| ALC_DVS.1 | Identifikation von Sicherheitsmaßnahmen | 0410, 0510 |
| ALC_LCD.1 | Entwicklerdefiniertes Lebenszyklusmodell | 0410, 0510 |
| ATE_DPT.1 | Tests: Grundlegendes Design | 0410, 0510 |
| ATE_FUN.1 | Funktionale Tests | 0410, 0510 |
| ATE_IND.2 | Unabhängige Tests - Stichprobe | 0410, 0510 |
| AVA_VAN.2 | Schwachstellenanalyse | 0410, 0510 |

### EAL4: Methodisch entworfen, getestet und überprüft

EAL4 umfasst alle EAL3-Komponenten plus:

| SAR-Komponente | Beschreibung | Template-Referenz |
|----------------|--------------|-------------------|
| ADV_ARC.1 | Beschreibung der Sicherheitsarchitektur | 0410, 0510 |
| ADV_FSP.4 | Vollständige funktionale Spezifikation | 0410, 0510 |
| ADV_IMP.1 | Implementierungsdarstellung der TSF | 0410, 0510 |
| ADV_TDS.2 | Architektonisches Design | 0410, 0510 |
| ALC_CMC.4 | Produktionsunterstützung, Akzeptanzverfahren und Automatisierung | 0410, 0510 |
| ALC_CMS.4 | Problemverfolgung CM-Abdeckung | 0410, 0510 |
| ALC_TAT.1 | Wohldefinierte Entwicklungswerkzeuge | 0410, 0510 |
| ATE_COV.2 | Analyse der Abdeckung | 0410, 0510 |
| ATE_DPT.1 | Tests: Grundlegendes Design | 0410, 0510 |
| ATE_FUN.1 | Funktionale Tests | 0410, 0510 |
| ATE_IND.2 | Unabhängige Tests - Stichprobe | 0410, 0510 |
| AVA_VAN.3 | Fokussierte Schwachstellenanalyse | 0410, 0510 |

### EAL5: Semiformal entworfen und getestet

EAL5 umfasst alle EAL4-Komponenten plus:

| SAR-Komponente | Beschreibung | Template-Referenz |
|----------------|--------------|-------------------|
| ADV_ARC.1 | Beschreibung der Sicherheitsarchitektur | 0410, 0510 |
| ADV_FSP.5 | Vollständige semiformale funktionale Spezifikation | 0410, 0510 |
| ADV_IMP.1 | Implementierungsdarstellung der TSF | 0410, 0510 |
| ADV_INT.2 | Gut strukturierte Interna | 0410, 0510 |
| ADV_TDS.3 | Grundlegendes modulares Design | 0410, 0510 |
| ALC_DVS.1 | Identifikation von Sicherheitsmaßnahmen | 0410, 0510 |
| ATE_COV.2 | Analyse der Abdeckung | 0410, 0510 |
| ATE_DPT.2 | Tests: Sicherheitserzwingende Module | 0410, 0510 |
| ATE_FUN.1 | Funktionale Tests | 0410, 0510 |
| ATE_IND.2 | Unabhängige Tests - Stichprobe | 0410, 0510 |
| AVA_VAN.4 | Methodische Schwachstellenanalyse | 0410, 0510 |

### EAL6: Semiformal verifiziertes Design und getestet

EAL6 umfasst alle EAL5-Komponenten plus:

| SAR-Komponente | Beschreibung | Template-Referenz |
|----------------|--------------|-------------------|
| ADV_ARC.1 | Beschreibung der Sicherheitsarchitektur | 0410, 0510 |
| ADV_FSP.5 | Vollständige semiformale funktionale Spezifikation | 0410, 0510 |
| ADV_IMP.2 | Vollständige Abbildung der Implementierungsdarstellung der TSF | 0410, 0510 |
| ADV_INT.3 | Minimal komplexe Interna | 0410, 0510 |
| ADV_SPM.1 | Formales TOE-Sicherheitsrichtlinienmodell | 0410, 0510 |
| ADV_TDS.4 | Semiformales modulares Design | 0410, 0510 |
| ALC_DVS.2 | Angemessenheit der Sicherheitsmaßnahmen | 0410, 0510 |
| ATE_COV.3 | Rigorose Analyse der Abdeckung | 0410, 0510 |
| ATE_DPT.3 | Tests: Modulares Design | 0410, 0510 |
| ATE_FUN.2 | Geordnete funktionale Tests | 0410, 0510 |
| ATE_IND.2 | Unabhängige Tests - Stichprobe | 0410, 0510 |
| AVA_VAN.5 | Fortgeschrittene methodische Schwachstellenanalyse | 0410, 0510 |

### EAL7: Formal verifiziertes Design und getestet

EAL7 umfasst alle EAL6-Komponenten plus:

| SAR-Komponente | Beschreibung | Template-Referenz |
|----------------|--------------|-------------------|
| ADV_ARC.1 | Beschreibung der Sicherheitsarchitektur | 0410, 0510 |
| ADV_FSP.6 | Vollständige semiformale funktionale Spezifikation mit zusätzlichen Fehlerinformationen | 0410, 0510 |
| ADV_IMP.2 | Vollständige Abbildung der Implementierungsdarstellung der TSF | 0410, 0510 |
| ADV_INT.3 | Minimal komplexe Interna | 0410, 0510 |
| ADV_SPM.1 | Formales TOE-Sicherheitsrichtlinienmodell | 0410, 0510 |
| ADV_TDS.5 | Vollständiges semiformales modulares Design | 0410, 0510 |
| ALC_DVS.2 | Angemessenheit der Sicherheitsmaßnahmen | 0410, 0510 |
| ATE_COV.3 | Rigorose Analyse der Abdeckung | 0410, 0510 |
| ATE_DPT.4 | Tests: Implementierungsdarstellung | 0410, 0510 |
| ATE_FUN.2 | Geordnete funktionale Tests | 0410, 0510 |
| ATE_IND.3 | Unabhängige Tests - vollständig | 0410, 0510 |
| AVA_VAN.5 | Fortgeschrittene methodische Schwachstellenanalyse | 0410, 0510 |

## Protection Profile Konformität

Bei Anspruch auf Konformität zu einem Protection Profile (PP) sind folgende Templates relevant:

| Template | PP-Konformitätsaspekt | Beschreibung |
|----------|----------------------|--------------|
| 0040_Conformance_Claims.md | PP-Identifikation | Identifikation der PP(s), zu denen das ST Konformität beansprucht |
| 0600_PP_Conformance.md | PP-Konformitätsnachweis | Nachweis, wie das ST die PP-Anforderungen erfüllt |
| 0610_Rationale_for_Objectives.md | Zielkonsistenz | Konsistenz zwischen ST- und PP-Zielen zeigen |
| 0620_Rationale_for_Requirements.md | Anforderungskonsistenz | Konsistenz zwischen ST- und PP-Anforderungen zeigen |

### PP-Konformitätstypen

- **Strikte Konformität**: ST enthält alle PP-Anforderungen ohne Ergänzungen
- **Nachweisbare Konformität**: ST enthält alle PP-Anforderungen plus zusätzliche Anforderungen
- **Paket-Erweiterung**: ST erweitert ein PP mit zusätzlichen Vertrauenswürdigkeitsanforderungen

## Abdeckungsanalyse

### Sicherheitsproblem-Abdeckung

| Sicherheitsproblem-Element | Adressiert durch | Template-Referenz |
|---------------------------|------------------|-------------------|
| Bedrohungen | Sicherheitsziele für TOE | 0210, 0300, 0310, 0320 |
| Organisatorische Sicherheitsrichtlinien | Sicherheitsziele für TOE | 0220, 0300, 0310, 0320 |
| Annahmen | Sicherheitsziele für Umgebung | 0230, 0300, 0310, 0320 |

### Sicherheitsziele-Abdeckung

| Sicherheitsziel-Element | Adressiert durch | Template-Referenz |
|------------------------|------------------|-------------------|
| Sicherheitsziele für TOE | Funktionale Sicherheitsanforderungen (SFRs) | 0300, 0400, 0420, 0440 |
| Sicherheitsziele für Umgebung | Nicht-TOE-Sicherheitsmaßnahmen | 0300, 0310, 0320 |

### Sicherheitsanforderungen-Abdeckung

| Sicherheitsanforderungs-Element | Adressiert durch | Template-Referenz |
|--------------------------------|------------------|-------------------|
| Funktionale Sicherheitsanforderungen (SFRs) | TOE-Sicherheitsfunktionen (TSFs) | 0400, 0500, 0520, 0530 |
| Vertrauenswürdigkeitsanforderungen (SARs) | Vertrauenswürdigkeitsmaßnahmen | 0410, 0510 |

## Begründungsanforderungen

Die Common Criteria erfordern umfassende Begründungsdokumentation, um Folgendes nachzuweisen:

1. **Sicherheitsziele-Begründung** (Template 0310, 0610)
   - Jede Bedrohung wird durch mindestens ein Sicherheitsziel abgewehrt
   - Jede OSP wird durch mindestens ein Sicherheitsziel abgedeckt
   - Jede Annahme wird durch mindestens ein Sicherheitsziel für die Umgebung abgedeckt

2. **Sicherheitsanforderungen-Begründung** (Template 0420, 0620)
   - Jedes Sicherheitsziel für den TOE wird durch mindestens eine SFR adressiert
   - Jede SFR trägt zu mindestens einem Sicherheitsziel bei
   - Alle SFR-Abhängigkeiten sind erfüllt

3. **TOE-Zusammenfassende Spezifikation-Begründung** (Template 0520)
   - Jede SFR wird durch mindestens eine TSF implementiert
   - Jede TSF implementiert mindestens eine SFR

## Abdeckungsmatrizen

Die Templates enthalten mehrere Abdeckungsmatrizen, um Vollständigkeit nachzuweisen:

| Matrix | Template | Zweck |
|--------|----------|-------|
| Bedrohungen/Ziele-Matrix | 0320 | Bildet Bedrohungen auf Sicherheitsziele ab |
| OSPs/Ziele-Matrix | 0320 | Bildet OSPs auf Sicherheitsziele ab |
| Annahmen/Ziele-Matrix | 0320 | Bildet Annahmen auf Sicherheitsziele für Umgebung ab |
| Ziele/SFRs-Matrix | 0440 | Bildet Sicherheitsziele auf SFRs ab |
| SFRs/TSFs-Matrix | 0530 | Bildet SFRs auf TOE-Sicherheitsfunktionen ab |
| SFR-Abhängigkeiten-Matrix | 0430 | Zeigt Erfüllung der SFR-Abhängigkeiten |

## Template-Vollständigkeits-Checkliste

Um eine vollständige Abdeckung der ISO/IEC 15408 Anforderungen sicherzustellen, überprüfen Sie:

- [ ] Alle obligatorischen ST-Abschnitte sind vorhanden (Templates 0010-0650)
- [ ] TOE-Beschreibung ist vollständig und eindeutig (Templates 0100-0140)
- [ ] Alle Bedrohungen, OSPs und Annahmen sind identifiziert (Templates 0210-0240)
- [ ] Sicherheitsziele adressieren alle Sicherheitsproblem-Elemente (Templates 0300-0330)
- [ ] Alle SFRs stammen aus ISO/IEC 15408-2 (Template 0400)
- [ ] Alle SARs entsprechen dem gewählten EAL (Template 0410)
- [ ] Alle SFR-Abhängigkeiten sind erfüllt (Template 0430)
- [ ] Alle Begründungen sind vollständig und nachvollziehbar (Templates 0310, 0420, 0520, 0610, 0620)
- [ ] Alle Abdeckungsmatrizen sind vollständig (Templates 0320, 0440, 0530)
- [ ] PP-Konformität ist nachgewiesen (falls zutreffend) (Templates 0040, 0600)

## Lückenanalyse

### Aktuelle Abdeckung

Das Template-Set bietet umfassende Abdeckung von:
- ✅ Alle obligatorischen ST-Abschnitte gemäß ISO/IEC 15408-1, Abschnitt 8
- ✅ Unterstützung für alle EAL-Stufen (EAL1-EAL7)
- ✅ Alle SFR-Klassen aus ISO/IEC 15408-2
- ✅ Alle SAR-Klassen aus ISO/IEC 15408-3
- ✅ Protection Profile Konformitätsnachweis
- ✅ Vollständige Begründungsdokumentation
- ✅ Abdeckungsmatrizen für Rückverfolgbarkeit

### Optionale Erweiterungen

Die folgenden optionalen Elemente könnten in zukünftigen Versionen hinzugefügt werden:
- Erweiterte Pakete (z.B. CCEVS, ANSSI-spezifische Anforderungen)
- Templates für zusammengesetzte Evaluierungen (ACO-Klasse)
- Formale Methoden-Templates für EAL6/EAL7
- Spezifische PP-Templates für gängige Domänen (z.B. Betriebssysteme, Smartcards, Netzwerkgeräte)

## Referenzen

- ISO/IEC 15408-1:2022 - Informationssicherheit, Cybersicherheit und Datenschutz — Evaluierungskriterien für IT-Sicherheit — Teil 1: Einführung und allgemeines Modell
- ISO/IEC 15408-2:2022 - Teil 2: Funktionale Sicherheitskomponenten
- ISO/IEC 15408-3:2022 - Teil 3: Vertrauenswürdigkeitskomponenten
- Common Criteria Portal: https://www.commoncriteriaportal.org/
- Common Methodology for Information Technology Security Evaluation (CEM)

## Kontakt

Für Fragen zu diesem Framework-Mapping oder Common Criteria Evaluierung:
- Common Criteria Portal: https://www.commoncriteriaportal.org/
- Nationale Zertifizierungsstellen (z.B. BSI, ANSSI, NIAP)
- Akkreditierte Evaluierungslabore

