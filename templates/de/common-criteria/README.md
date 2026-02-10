# Common Criteria Security Target Templates (ISO/IEC 15408)

Dieses Verzeichnis enthält Templates für die Erstellung eines Security Target (ST) gemäß ISO/IEC 15408 (Common Criteria for Information Technology Security Evaluation).

## Überblick

Die Common Criteria (CC) sind ein internationaler Standard für die Evaluierung der Sicherheit von IT-Produkten und -Systemen. Ein Security Target dokumentiert die Sicherheitseigenschaften eines Target of Evaluation (TOE) und dient als Grundlage für die Zertifizierung.

## Template-Struktur

Die Templates sind nach der Struktur von ISO/IEC 15408-1:2022 organisiert:

### Foundation (0010-0050)
- **0010**: ST Introduction - Einführung und Identifikation des ST
- **0020**: TOE Overview - Überblick über den Evaluierungsgegenstand
- **0030**: TOE Description Summary - Zusammenfassung der TOE-Beschreibung
- **0040**: Conformance Claims - Konformitätsansprüche (PP, Package, CC Version)
- **0050**: Document Conventions - Dokumentationskonventionen und Terminologie

### TOE Description (0100-0150)
- **0100**: TOE Physical Scope - Physischer Umfang (Hardware, Software, Firmware)
- **0110**: TOE Logical Scope - Logischer Umfang (Sicherheitsfunktionen)
- **0120**: TOE Interfaces - Schnittstellen des TOE
- **0130**: TOE Architecture - Architektur und Komponenten
- **0140**: TOE Lifecycle - Lebenszyklus (Entwicklung, Betrieb, Wartung)

### Security Problem Definition (0200-0250)
- **0200**: Threats - Bedrohungen für den TOE
- **0210**: Organizational Security Policies - Organisatorische Sicherheitspolitiken
- **0220**: Assumptions - Annahmen über die Einsatzumgebung
- **0230**: Threat Agents - Angreifer und deren Fähigkeiten
- **0240**: Assets - Schützenswerte Werte (Assets)

### Security Objectives (0300-0350)
- **0300**: Security Objectives for TOE - Sicherheitsziele für den TOE
- **0310**: Security Objectives for Environment - Sicherheitsziele für die Umgebung
- **0320**: Security Objectives Rationale - Begründung der Sicherheitsziele
- **0330**: Objectives Coverage Matrix - Abdeckungsmatrix Ziele/Bedrohungen

### Security Requirements (0400-0450)
- **0400**: Security Functional Requirements (SFR) - Funktionale Sicherheitsanforderungen
- **0410**: Security Assurance Requirements (SAR) - Vertrauenswürdigkeitsanforderungen
- **0420**: Evaluation Assurance Level (EAL) - Evaluierungsstufe
- **0430**: Security Requirements Rationale - Begründung der Anforderungen
- **0440**: SFR Dependencies - Abhängigkeiten zwischen SFRs
- **0450**: Requirements Coverage Matrix - Abdeckungsmatrix Anforderungen/Ziele

### TOE Summary Specification (0500-0550)
- **0500**: Security Functions - Sicherheitsfunktionen des TOE
- **0510**: Assurance Measures - Vertrauenswürdigkeitsmaßnahmen
- **0520**: Security Functions Rationale - Begründung der Sicherheitsfunktionen
- **0530**: Functions Coverage Matrix - Abdeckungsmatrix Funktionen/SFRs
- **0540**: Strength of Function Claims - Ansprüche zur Funktionsstärke

### Appendices (0600-0650)
- **0600**: Protection Profile Conformance - PP-Konformität
- **0610**: Rationale for Security Objectives - Ausführliche Begründung
- **0620**: Rationale for Security Requirements - Ausführliche Begründung
- **0630**: Glossary and Acronyms - Glossar und Abkürzungen
- **0640**: References - Referenzen und Standards
- **0650**: Evidence and Documentation - Nachweise und Dokumentation

## Nummerierungsschema

- Templates verwenden 4-stellige Nummern mit 10er-Schritten (0010, 0020, 0030, ...)
- Dies ermöglicht spätere Einfügungen zwischen bestehenden Templates
- Nummernbereiche gruppieren zusammengehörige Themen

## Verwendung

1. **Vorbereitung**: Bestimmen Sie das Evaluation Assurance Level (EAL1-EAL7)
2. **TOE-Definition**: Definieren Sie klar den Umfang des TOE
3. **PP-Auswahl**: Wählen Sie ein passendes Protection Profile (optional)
4. **Anpassung**: Passen Sie die Templates an Ihr spezifisches Produkt an
5. **Platzhalter**: Ersetzen Sie alle `[TODO]`-Markierungen
6. **Konsistenz**: Stellen Sie Konsistenz zwischen allen Abschnitten sicher
7. **Rationale**: Dokumentieren Sie alle Begründungen vollständig

## Platzhalter

Templates unterstützen zwei Arten von Platzhaltern:

- **Manuelle Platzhalter**: `[TODO: Beschreibung]` - müssen manuell ersetzt werden
- **Automatische Platzhalter**: `{{ source.field }}` - werden aus Datenquellen befüllt

Beispiele für automatische Platzhalter:
- `{{ meta.organization }}` - Organisationsname
- `{{ meta.author }}` - Autor
- `{{ meta.version }}` - Versionsnummer
- `{{ meta.date }}` - Datum

## Common Criteria Versionen

Diese Templates basieren auf:
- ISO/IEC 15408-1:2022 (Part 1: Introduction and general model)
- ISO/IEC 15408-2:2022 (Part 2: Security functional components)
- ISO/IEC 15408-3:2022 (Part 3: Security assurance components)

## Evaluation Assurance Levels (EAL)

- **EAL1**: Functionally tested
- **EAL2**: Structurally tested
- **EAL3**: Methodically tested and checked
- **EAL4**: Methodically designed, tested, and reviewed
- **EAL5**: Semiformally designed and tested
- **EAL6**: Semiformally verified design and tested
- **EAL7**: Formally verified design and tested

## Wichtige Hinweise

- Das ST muss vollständig und konsistent sein
- Alle SFRs müssen aus ISO/IEC 15408-2 stammen
- Alle SARs müssen aus ISO/IEC 15408-3 stammen
- Die Rationale muss alle Beziehungen nachweisen
- Abhängigkeiten zwischen SFRs müssen erfüllt sein
- Das ST muss von einem akkreditierten Labor evaluiert werden

## Framework Mapping

Siehe `FRAMEWORK_MAPPING.md` für eine detaillierte Zuordnung der Templates zu ISO/IEC 15408 Komponenten.

## Weitere Ressourcen

- Common Criteria Portal: https://www.commoncriteriaportal.org/
- ISO/IEC 15408 Standard
- Protection Profiles Repository
- Certified Products List
- Evaluation Schemes (z.B. BSI, ANSSI, NIAP)

## Support

Bei Fragen zur Verwendung dieser Templates oder zur Common Criteria Evaluierung wenden Sie sich an:
- Ihr internes Sicherheitsteam
- Akkreditierte Evaluierungslabore
- Nationale Zertifizierungsstellen (z.B. BSI in Deutschland)
