# Document Conventions

**Dokument-ID:** 0050  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---



## 1. Terminology and Notation

### 1.1 Common Criteria Terminology
Dieses Security Target verwendet Terminologie aus ISO/IEC 15408:2022:

| Term | Definition |
|------|------------|
| **TOE** | Target of Evaluation - das IT-Produkt oder -System, das evaluiert wird |
| **TSF** | TOE Security Functionality - kombinierte Funktionalität aller Hardware, Software und Firmware des TOE, die für die korrekte Durchsetzung der SFRs erforderlich ist |
| **TSP** | TOE Security Policy - Regelwerk, das regelt, wie Assets innerhalb des TOE verwaltet, geschützt und verteilt werden |
| **SFR** | Security Functional Requirement - Anforderung an die Sicherheitsdurchsetzung durch den TOE |
| **SAR** | Security Assurance Requirement - Anforderung zur Sicherstellung der Sicherheit des TOE |
| **PP** | Protection Profile - implementierungsunabhängige Aussage über Sicherheitsbedürfnisse für einen TOE-Typ |
| **ST** | Security Target - implementierungsabhängige Aussage über Sicherheitsbedürfnisse für einen spezifischen TOE |
| **EAL** | Evaluation Assurance Level - Paket von Vertrauenswürdigkeitsanforderungen |

### 1.2 TOE-Specific Terminology
[TODO: Definiere TOE-spezifische Begriffe]

| Term | Definition |
|------|------------|
| [TODO: Begriff 1] | [TODO: Definition] |
| [TODO: Begriff 2] | [TODO: Definition] |
| [TODO: Begriff 3] | [TODO: Definition] |

## 2. Notation Conventions

### 2.1 SFR Notation
Security Functional Requirements werden mit der Notation aus ISO/IEC 15408-2:2022 identifiziert:

**Format:** `CLASS.FAMILY.COMPONENT.ELEMENT`

**Beispiel:** `FIA_UAU.1.1`
- **FIA** = Class (Identification and Authentication)
- **UAU** = Family (User Authentication)
- **1** = Component number
- **1** = Element number

### 2.2 SAR Notation
Security Assurance Requirements werden mit der Notation aus ISO/IEC 15408-3:2022 identifiziert:

**Format:** `CLASS.FAMILY.COMPONENT`

**Beispiel:** `ADV_FSP.1`
- **ADV** = Class (Development)
- **FSP** = Family (Functional Specification)
- **1** = Component number

### 2.3 Operations on Requirements
Folgende Operationen können auf SFRs und SARs angewendet werden:

| Operation | Symbol | Description |
|-----------|--------|-------------|
| **Assignment** | [assignment:] | Parameter spezifizieren |
| **Selection** | [selection:] | Aus einer Liste von Optionen wählen |
| **Refinement** | **fett** | Details hinzufügen oder einschränken |
| **Iteration** | /iteration | Anforderung mehrfach anwenden |

**Beispiel:**
- Original: "The TSF shall authenticate [assignment: list of users]"
- Vervollständigt: "The TSF shall authenticate [assignment: administrators, operators]"

## 3. Document Structure

### 3.1 Section Organization
Dieses ST ist gemäß ISO/IEC 15408-1:2022 organisiert:

1. **ST Introduction** - Identifikation und Überblick
2. **TOE Description** - Physische und logische Beschreibung
3. **Security Problem Definition** - Bedrohungen, OSPs, Annahmen
4. **Security Objectives** - Ziele für TOE und Umgebung
5. **Security Requirements** - SFRs und SARs
6. **TOE Summary Specification** - Sicherheitsfunktionen
7. **Appendices** - Unterstützende Informationen

### 3.2 Cross-References
Querverweise innerhalb dieses ST verwenden folgendes Format:
- Abschnittsverweise: "Siehe Abschnitt X.Y"
- Tabellenverweise: "Siehe Tabelle X"
- Abbildungsverweise: "Siehe Abbildung X"

## 4. Formatting Conventions

### 4.1 Text Formatting
| Format | Usage |
|--------|-------|
| **Fett** | Betonung, Verfeinerungen |
| *Kursiv* | Definitionen, erste Verwendung von Begriffen |
| `Monospace` | Code, Befehle, Identifikatoren |
| [TODO] | Platzhalter, der vervollständigt werden muss |

### 4.2 Lists and Tables
- **Aufzählungslisten**: Verwendet für ungeordnete Elemente
- **Nummerierte Listen**: Verwendet für sequenzielle Schritte oder geordnete Elemente
- **Tabellen**: Verwendet für strukturierte Daten und Zuordnungen

### 4.3 Diagrams
[TODO: Beschreibe Diagrammkonventionen, falls zutreffend]
- Architekturdiagramme: [TODO]
- Datenflussdiagramme: [TODO]
- Sequenzdiagramme: [TODO]

## 5. Abbreviations and Acronyms

### 5.1 Common Criteria Abbreviations
| Abbreviation | Full Term |
|--------------|-----------|
| CC | Common Criteria |
| CEM | Common Evaluation Methodology |
| EAL | Evaluation Assurance Level |
| IT | Information Technology |
| OSP | Organizational Security Policy |
| PP | Protection Profile |
| SAR | Security Assurance Requirement |
| SFR | Security Functional Requirement |
| ST | Security Target |
| TOE | Target of Evaluation |
| TSF | TOE Security Functionality |
| TSP | TOE Security Policy |

### 5.2 TOE-Specific Abbreviations
[TODO: Liste TOE-spezifische Abkürzungen auf]

| Abbreviation | Full Term |
|--------------|-----------|
| [TODO: Abk. 1] | [TODO: Vollständiger Begriff] |
| [TODO: Abk. 2] | [TODO: Vollständiger Begriff] |
| [TODO: Abk. 3] | [TODO: Vollständiger Begriff] |

## 6. References

### 6.1 Normative References
Folgende Dokumente werden normativ in diesem ST referenziert:

1. ISO/IEC 15408-1:2022, Information technology — Security techniques — Evaluation criteria for IT security — Part 1: Introduction and general model
2. ISO/IEC 15408-2:2022, Information technology — Security techniques — Evaluation criteria for IT security — Part 2: Security functional components
3. ISO/IEC 15408-3:2022, Information technology — Security techniques — Evaluation criteria for IT security — Part 3: Security assurance components
4. Common Methodology for Information Technology Security Evaluation (CEM)

### 6.2 Informative References
[TODO: Liste informative Referenzen auf]

1. [TODO: Referenz 1]
2. [TODO: Referenz 2]
3. [TODO: Referenz 3]

## 7. Document Conventions Summary

### 7.1 Key Conventions
- Alle SFRs stammen aus ISO/IEC 15408-2:2022, sofern nicht als erweitert markiert
- Alle SARs stammen aus ISO/IEC 15408-3:2022, sofern nicht als augmentiert markiert
- Operationen auf Anforderungen sind klar markiert
- Alle [TODO]-Platzhalter müssen vor Finalisierung vervollständigt werden

### 7.2 Consistency Rules
- Terminologie muss im gesamten ST konsistent sein
- Alle Querverweise müssen gültig sein
- Alle Tabellen und Abbildungen müssen sequenziell nummeriert sein
- Alle Anforderungen müssen eindeutig identifiziert sein

---

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter
2. Verifiziere Konsistenz der Terminologieverwendung
3. Stelle sicher, dass alle Abkürzungen definiert sind
4. Prüfe, dass alle Referenzen vollständig sind
