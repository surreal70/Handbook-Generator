---
Document-ID: togaf-0060
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Architecture-Werkzeuge und -Techniken

## Zweck

Dieses Dokument beschreibt die Werkzeuge und Techniken, die im Architecture-Prozess von {{ source.organization_name }} verwendet werden. Es definiert den Werkzeug-Stack, Nutzungsrichtlinien und Best Practices.

## Geltungsbereich

Dieses Dokument umfasst:
- Architecture-Modellierungswerkzeuge
- Dokumentationswerkzeuge
- Kollaborationswerkzeuge
- Analyse- und Bewertungstechniken
- Visualisierungstechniken

## Werkzeug-Stack

### Modellierungswerkzeuge

| Werkzeug | Zweck | Lizenzmodell | Benutzer |
|----------|-------|--------------|----------|
| {{ source.modeling_tool_name }} | Enterprise Architecture-Modellierung | {{ source.modeling_license }} | Architecture Team |
| {{ source.diagram_tool_name }} | Diagrammerstellung | {{ source.diagram_license }} | Alle Projektteams |
| {{ source.data_modeling_tool }} | Datenmodellierung | {{ source.data_modeling_license }} | Data Architects |

**Primäres Modellierungswerkzeug**: {{ source.primary_modeling_tool }}

**Fähigkeiten**:
- Unterstützung für TOGAF Content Framework
- Metamodell-Anpassung
- Beziehungsmanagement
- Impact-Analyse
- Reporting und Dashboards

### Dokumentationswerkzeuge

| Werkzeug | Zweck | Format | Integration |
|----------|-------|--------|-------------|
| {{ source.wiki_tool }} | Kollaborative Dokumentation | Wiki/Markdown | {{ source.wiki_integration }} |
| {{ source.doc_tool }} | Formelle Dokumente | Word/PDF | {{ source.doc_integration }} |
| {{ source.presentation_tool }} | Präsentationen | PowerPoint/PDF | {{ source.presentation_integration }} |

### Repository und Versionskontrolle

**Repository-Werkzeug**: {{ source.repository_tool }}

**Versionskontrolle**: {{ source.version_control_tool }}

**Fähigkeiten**:
- Artefakt-Versionierung
- Workflow-Management
- Zugriffskontrolle
- Audit-Trail
- Suche und Entdeckung

### Kollaborationswerkzeuge

| Werkzeug | Zweck | Nutzung |
|----------|-------|---------|
| {{ source.collaboration_platform }} | Team-Kommunikation | Tägliche Zusammenarbeit |
| {{ source.meeting_tool }} | Virtuelle Meetings | Reviews und Workshops |
| {{ source.whiteboard_tool }} | Visuelles Brainstorming | Design-Sitzungen |

## Modellierungstechniken

### Viewpoint-Ansatz

{{ source.organization_name }} verwendet TOGAF-Viewpoints für:
- **Stakeholder-Viewpoints**: Angepasst an spezifische Stakeholder-Anliegen
- **Architecture-Viewpoints**: Standardisierte Sichten auf Architecture-Domänen
- **Technical-Viewpoints**: Detaillierte technische Perspektiven

### Standardisierte Viewpoints

| Viewpoint | Zweck | Zielgruppe | Artefakte |
|-----------|-------|------------|-----------|
| Business Capability | Geschäftsfähigkeiten-Mapping | Business Leaders | Capability Map, Heat Map |
| Application Portfolio | Anwendungslandschaft | CIO, IT Management | Portfolio Matrix, Roadmap |
| Technology Platform | Technologie-Stack | Technical Architects | Platform Diagram, Standards |
| Information Flow | Datenflüsse | Data Architects | Data Flow Diagrams |

### Modellierungsnotationen

**Primäre Notationen**:
- **ArchiMate**: Für Enterprise Architecture-Modellierung
- **UML**: Für detaillierte Anwendungs- und Datenmodellierung
- **BPMN**: Für Geschäftsprozessmodellierung
- **Custom Notations**: {{ source.custom_notations }}

## Analyse-Techniken

### Gap-Analyse

**Zweck**: Identifikation von Unterschieden zwischen Ist- und Soll-Architecture

**Ansatz**:
1. Dokumentation der Baseline-Architecture
2. Definition der Target-Architecture
3. Identifikation von Gaps
4. Priorisierung von Gaps
5. Entwicklung von Transition-Plänen

### Impact-Analyse

**Zweck**: Bewertung der Auswirkungen von Architecture-Änderungen

**Faktoren**:
- Betroffene Systeme und Komponenten
- Abhängigkeiten und Schnittstellen
- Kosten und Ressourcen
- Risiken und Mitigation
- Zeitrahmen und Meilensteine

### Trade-off-Analyse

**Zweck**: Bewertung von Alternativen und Kompromissen

**Kriterien**:
- Funktionale Anforderungen
- Nicht-funktionale Anforderungen (Performance, Sicherheit, etc.)
- Kosten (Entwicklung, Betrieb, Wartung)
- Risiken
- Strategische Ausrichtung

### Reifegrad-Bewertung

**Framework**: {{ source.maturity_framework }}

**Dimensionen**:
- Architecture-Prozess-Reife
- Governance-Reife
- Werkzeug- und Technologie-Reife
- Fähigkeiten und Kompetenzen
- Stakeholder-Engagement

## Visualisierungstechniken

### Diagrammtypen

| Diagrammtyp | Zweck | Notation | Werkzeug |
|-------------|-------|----------|----------|
| Capability Map | Geschäftsfähigkeiten | Custom | {{ source.capability_tool }} |
| Value Stream | Wertschöpfungsketten | Custom | {{ source.value_stream_tool }} |
| Application Landscape | Anwendungsübersicht | ArchiMate | {{ source.app_landscape_tool }} |
| Data Flow | Datenflüsse | UML/Custom | {{ source.data_flow_tool }} |
| Infrastructure | Infrastruktur | Network Diagram | {{ source.infrastructure_tool }} |
| Roadmap | Zeitliche Planung | Gantt/Timeline | {{ source.roadmap_tool }} |

### Visualisierungs-Best Practices

**Klarheit**:
- Fokus auf eine Botschaft pro Diagramm
- Verwendung konsistenter Notation
- Angemessene Detailtiefe für Zielgruppe
- Klare Beschriftungen und Legenden

**Konsistenz**:
- Standardisierte Farbschemata
- Einheitliche Symbolik
- Konsistente Namenskonventionen
- Wiederverwendbare Templates

**Wartbarkeit**:
- Versionskontrolle für Diagramme
- Quelldateien im Repository
- Dokumentation von Annahmen
- Regelmäßige Aktualisierung

## Bewertungs- und Entscheidungstechniken

### Multi-Criteria Decision Analysis (MCDA)

**Ansatz**:
1. Definition von Bewertungskriterien
2. Gewichtung der Kriterien
3. Bewertung von Alternativen
4. Berechnung von Scores
5. Sensitivitätsanalyse

### Architecture Trade-off Analysis Method (ATAM)

**Phasen**:
1. Präsentation der Architecture
2. Identifikation von Architecture-Ansätzen
3. Generierung von Quality Attribute Utility Tree
4. Analyse von Architecture-Ansätzen
5. Brainstorming und Priorisierung von Szenarien
6. Analyse von Architecture-Ansätzen gegen Szenarien

### Cost-Benefit-Analyse

**Komponenten**:
- **Kosten**: Entwicklung, Implementierung, Betrieb, Wartung
- **Nutzen**: Effizienzgewinne, Risikoreduktion, neue Fähigkeiten
- **ROI-Berechnung**: Payback-Periode, NPV, IRR
- **Sensitivitätsanalyse**: Best/Worst/Most Likely Cases

## Werkzeug-Governance

### Werkzeugauswahl-Kriterien

Bei der Auswahl neuer Werkzeuge werden folgende Kriterien bewertet:
- Funktionale Anforderungen
- Integration mit bestehendem Stack
- Benutzerfreundlichkeit
- Kosten (Lizenz, Schulung, Support)
- Vendor-Stabilität und Roadmap
- Community und Support

### Werkzeug-Lifecycle

| Phase | Aktivitäten | Verantwortlich |
|-------|-------------|----------------|
| Evaluation | Anforderungsanalyse, Proof of Concept | Architecture Team |
| Procurement | Lizenzierung, Vertragsverhandlung | Procurement |
| Onboarding | Installation, Konfiguration, Schulung | IT Operations, Architecture Team |
| Operations | Nutzung, Support, Wartung | IT Operations |
| Retirement | Migration, Datenarchivierung | Architecture Team, IT Operations |

### Schulung und Support

**Schulungsangebote**:
- Einführungsschulungen für neue Werkzeuge
- Fortgeschrittene Techniken und Best Practices
- Regelmäßige Auffrischungskurse
- On-Demand-Support und Dokumentation

**Support-Kanäle**:
- Interne Wissensdatenbank
- Peer-Support über Collaboration-Plattform
- Vendor-Support für lizenzierte Werkzeuge
- Externe Berater für spezialisierte Themen

## Kontinuierliche Verbesserung

Der Werkzeug-Stack und die Techniken werden verbessert durch:
- Regelmäßige Bewertung der Werkzeugeffektivität
- Feedback von Benutzern
- Evaluation neuer Werkzeuge und Technologien
- Benchmarking mit Branchenstandards
- Lessons Learned aus Projekten

<!-- Autorenhinweise: Passen Sie Werkzeuge und Techniken an die Bedürfnisse und das Budget Ihrer Organisation an -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|------|--------|---------|
| 0.1 | {{meta.document.last_updated}} | {{ meta.defaults.author }} | Initiale Erstellung |

<-  ( marked all subtasks complete End of template -->
