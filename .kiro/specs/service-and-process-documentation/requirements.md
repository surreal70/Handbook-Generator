# Service and Process Documentation System

## Überblick

Erweiterung des Handbook-Generators um strukturierte Dokumentation von IT-Services und Geschäftsprozessen mit COBIT/ITIL-Konformität und BPMN-Unterstützung.

## Glossar

- **IT-Service**: Eine definierte IT-Dienstleistung mit klaren Schnittstellen, SLAs und Verantwortlichkeiten
- **Geschäftsprozess**: Ein strukturierter Ablauf mit definierten Inputs, Outputs, Rollen und Kontrollpunkten
- **COBIT**: Control Objectives for Information and Related Technologies - Framework für IT-Governance
- **ITIL**: Information Technology Infrastructure Library - Best-Practice-Framework für IT-Service-Management
- **BPMN**: Business Process Model and Notation - Standard für Prozessmodellierung
- **RACI**: Responsibility Assignment Matrix (Responsible, Accountable, Consulted, Informed)
- **SLA**: Service Level Agreement - Vereinbarung über Servicelevel
- **OLA**: Operational Level Agreement - Interne Betriebsvereinbarung
- **KPI**: Key Performance Indicator - Leistungskennzahl
- **SoD**: Segregation of Duties - Funktionstrennung

## User Stories

### US-1: Service-Dokumentation mit COBIT/ITIL-Konformität

**Als** IT-Service-Manager  
**möchte ich** IT-Services strukturiert nach COBIT- und ITIL-Standards dokumentieren  
**damit** alle Services einheitlich beschrieben sind und Compliance-Anforderungen erfüllt werden.

#### Akzeptanzkriterien

**AC-1.1: Service-Template-Struktur (Deutsch)**

WHEN ein generisches Service-Template erstellt wird  
THEN SHALL das Template folgende Abschnitte enthalten:
- Dokumenten-Header (analog zu Handbook-Templates)
- Service-Übersicht (Name, Beschreibung, Kategorie)
- Service-Ziele und Nutzen
- COBIT-Mapping (relevante Prozesse und Controls)
- ITIL-Mapping (Service Lifecycle Phasen)
- Service-Komponenten und Architektur
- Schnittstellen und Abhängigkeiten
- Service Level Agreements (SLAs)
- Operational Level Agreements (OLAs)
- Rollen und Verantwortlichkeiten
- Betriebszeiten und Verfügbarkeit
- Support-Modell und Eskalation
- Monitoring und Reporting
- Kontinuierliche Verbesserung
- Anhänge (Runbooks, Checklisten)

**AC-1.2: Service-Verzeichnisstruktur**

WHEN die Service-Dokumentation implementiert wird  
THEN SHALL folgende Verzeichnisstruktur existieren:
```
services/
├── de/
│   ├── meta-global-service.yaml     # Globale Service-Placeholders
│   └── generic-service-template/
│       ├── meta-service.yaml        # Service-spezifische Placeholders
│       └── service-template.md      # Service-Template
└── en/
    ├── meta-global-service.yaml
    └── generic-service-template/
        ├── meta-service.yaml
        └── service-template.md
```

**AC-1.3: Integration mit bestehenden Metadata-Konfigurationen**

WHEN Service-Templates Placeholders verwenden  
THEN SHALL das System auf folgende bestehende Konfigurationen zugreifen:
- `meta-global.yaml`: Handbook Generator Version und Source-Informationen
- `meta-organisation.yaml`: Organisation (Name, Adresse, Web, Phone, Revision)
- `meta-organisation-roles.yaml`: Rollen (role_CEO, role_CIO, role_CISO, role_IT_Manager, etc.)

**AC-1.4: Globale Service-Placeholders**

WHEN die globale Service-Konfiguration erstellt wird  
THEN SHALL meta-global-service.yaml folgende zusätzliche Placeholders enthalten:
- Standard-SLA-Werte (z.B. availability_target, response_time_p1)
- Standard-Support-Zeiten (z.B. support_hours, maintenance_window)
- Standard-Eskalationswege
- Compliance-Frameworks (z.B. cobit_version, itil_version)
- Service-Kategorien (z.B. infrastructure, application, business)

**AC-1.5: Service-spezifische Placeholders**

WHEN ein Service-Template erstellt wird  
THEN SHALL meta-service.yaml folgende Placeholders enthalten:
- Service-Name und ID
- Service-Owner (Referenz auf role_* aus meta-organisation-roles.yaml)
- Service-Manager (Referenz auf role_* aus meta-organisation-roles.yaml)
- Service-Kategorie
- Kritikalität (Critical, High, Medium, Low)
- Spezifische SLA-Werte (überschreiben globale Defaults)
- Service-spezifische Kontakte
- Technologie-Stack
- COBIT-Prozess-Mapping
- ITIL-Lifecycle-Phase

**AC-1.6: Dokumenten-Header-Konsistenz**

WHEN ein Service-Template erstellt wird  
THEN SHALL der Dokumenten-Header folgende Felder enthalten (analog zu Handbook-Templates):
- Dokument-ID: {{ service.id }}
- Organisation: {{ meta-organisation.name }}
- Owner: {{ service.owner }} (aus meta-organisation-roles)
- Genehmigt durch: {{ service.approver }} (aus meta-organisation-roles)
- Revision: {{ service.revision }}
- Author: {{ meta-global.source }}
- Status: {{ service.status }}
- Klassifizierung: {{ service.classification }}
- Letzte Aktualisierung: {{ service.modifydate }}
- Template Version: {{ meta-global.version }}

**AC-1.7: Placeholder-Hierarchie**

WHEN Placeholders in Service-Templates verarbeitet werden  
THEN SHALL folgende Priorität gelten (höchste zuerst):
1. meta-service.yaml (service-spezifisch)
2. meta-global-service.yaml (global für alle Services)
3. meta-organisation-roles.yaml (Rollen und Kontakte)
4. meta-organisation.yaml (Organisation)
5. meta-global.yaml (Generator-Informationen)

**AC-1.8: COBIT-Integration**

WHEN ein Service dokumentiert wird  
THEN SHALL das Template Abschnitte für COBIT-Mapping enthalten:
- Relevante COBIT-Prozesse (z.B. DSS01, DSS02)
- Zugeordnete Controls
- Governance-Anforderungen

**AC-1.9: ITIL-Integration**

WHEN ein Service dokumentiert wird  
THEN SHALL das Template Abschnitte für ITIL-Mapping enthalten:
- Service Strategy
- Service Design
- Service Transition
- Service Operation
- Continual Service Improvement

### US-2: Prozess-Dokumentation mit BPMN und Compliance

**Als** Prozess-Manager  
**möchte ich** Geschäftsprozesse strukturiert mit BPMN-Diagrammen und Compliance-Anforderungen dokumentieren  
**damit** alle Prozesse nachvollziehbar, prüfbar und optimierbar sind.

#### Akzeptanzkriterien

**AC-2.1: Prozess-Template-Struktur (Deutsch)**

WHEN ein generisches Prozess-Template erstellt wird  
THEN SHALL das Template folgende Abschnitte enthalten:
- Dokumenten-Header (analog zu Handbook-Templates)
- Zweck und Ziel des Prozesses
- Geltungsbereich
- Trigger und Eingänge
- Ergebnisse und Outputs
- Rollen und Verantwortlichkeiten (RACI-Matrix)
- Ablaufdiagramm (BPMN) mit textueller Beschreibung
- Systeme und Tools
- Schnittstellen zu anderen Prozessen
- Artefakte (Tickets, Logs, Reports)
- SLAs und OLAs
- KPIs und Metriken
- Kontrollpunkte und Prüfschritte
- Risiken und Compliance-Anforderungen
- Segregation of Duties (SoD)
- Eskalationen und Ausnahmen
- Anhänge (Checklisten, Runbooks, Formulare)

**AC-2.2: Prozess-Verzeichnisstruktur**

WHEN die Prozess-Dokumentation implementiert wird  
THEN SHALL folgende Verzeichnisstruktur existieren:
```
processes/
├── de/
│   ├── meta-global-process.yaml      # Globale Prozess-Placeholders
│   └── generic-process-template/
│       ├── meta-process.yaml         # Prozess-spezifische Placeholders
│       ├── diagrams/                 # BPMN-Diagramme
│       └── process-template.md       # Prozess-Template
└── en/
    ├── meta-global-process.yaml
    └── generic-process-template/
        ├── meta-process.yaml
        ├── diagrams/
        └── process-template.md
```

**AC-2.3: Integration mit bestehenden Metadata-Konfigurationen**

WHEN Prozess-Templates Placeholders verwenden  
THEN SHALL das System auf folgende bestehende Konfigurationen zugreifen:
- `meta-global.yaml`: Handbook Generator Version und Source-Informationen
- `meta-organisation.yaml`: Organisation (Name, Adresse, Web, Phone, Revision)
- `meta-organisation-roles.yaml`: Rollen (role_CEO, role_CIO, role_CISO, role_IT_Manager, role_Risk_Manager, etc.)

**AC-2.4: Globale Prozess-Placeholders**

WHEN die globale Prozess-Konfiguration erstellt wird  
THEN SHALL meta-global-process.yaml folgende zusätzliche Placeholders enthalten:
- Standard-Eskalationswege
- Compliance-Frameworks (z.B. iso_27001, bsi_grundschutz)
- Standard-KPIs (z.B. process_efficiency, cycle_time)
- Audit-Anforderungen
- Standard-Kontrollpunkte
- Prozess-Kategorien (z.B. core, support, management)

**AC-2.5: Prozess-spezifische Placeholders**

WHEN ein Prozess-Template erstellt wird  
THEN SHALL meta-process.yaml folgende Placeholders enthalten:
- Prozess-Name und ID
- Prozess-Owner (Referenz auf role_* aus meta-organisation-roles.yaml)
- Prozess-Manager (Referenz auf role_* aus meta-organisation-roles.yaml)
- Prozess-Kategorie
- Kritikalität (Critical, High, Medium, Low)
- Spezifische SLAs/OLAs
- Prozess-spezifische Rollen (RACI-Matrix)
- Verwendete Systeme
- Compliance-Anforderungen
- SoD-Regeln

**AC-2.6: Dokumenten-Header-Konsistenz**

WHEN ein Prozess-Template erstellt wird  
THEN SHALL der Dokumenten-Header folgende Felder enthalten (analog zu Handbook-Templates):
- Dokument-ID: {{ process.id }}
- Organisation: {{ meta-organisation.name }}
- Owner: {{ process.owner }} (aus meta-organisation-roles)
- Genehmigt durch: {{ process.approver }} (aus meta-organisation-roles)
- Revision: {{ process.revision }}
- Author: {{ meta-global.source }}
- Status: {{ process.status }}
- Klassifizierung: {{ process.classification }}
- Letzte Aktualisierung: {{ process.modifydate }}
- Template Version: {{ meta-global.version }}

**AC-2.7: Placeholder-Hierarchie**

WHEN Placeholders in Prozess-Templates verarbeitet werden  
THEN SHALL folgende Priorität gelten (höchste zuerst):
1. meta-process.yaml (prozess-spezifisch)
2. meta-global-process.yaml (global für alle Prozesse)
3. meta-organisation-roles.yaml (Rollen und Kontakte)
4. meta-organisation.yaml (Organisation)
5. meta-global.yaml (Generator-Informationen)

**AC-2.8: RACI-Matrix-Integration**

WHEN ein Prozess dokumentiert wird  
THEN SHALL das Template eine RACI-Matrix enthalten mit:
- Prozessschritten
- Beteiligten Rollen
- Verantwortlichkeiten (R, A, C, I)

**AC-2.9: BPMN-Diagramm-Unterstützung**

WHEN ein Prozess dokumentiert wird  
THEN SHALL das Template Platzhalter für BPMN-Diagramme enthalten:
- Referenz auf Diagramm-Datei
- Textuelle Kurzbeschreibung des Ablaufs
- Hinweise zur Diagramm-Erstellung

**AC-2.10: Compliance und SoD**

WHEN ein Prozess dokumentiert wird  
THEN SHALL das Template Abschnitte für Compliance enthalten:
- Relevante Compliance-Frameworks
- Segregation of Duties (SoD) Anforderungen
- Kontrollpunkte und Prüfschritte
- Risiken und Mitigationen

### US-3: CLI-Integration für Service- und Prozess-Generierung

**Als** Benutzer des Handbook-Generators  
**möchte ich** Services und Prozesse über die CLI generieren können  
**damit** ich alle Dokumentationstypen einheitlich erstellen kann.

#### Akzeptanzkriterien

**AC-3.1: CLI-Option für Services**

WHEN der Handbook-Generator aufgerufen wird  
THEN SHALL eine neue Option `--service` verfügbar sein:
```bash
python -m src.cli --language de --service generic-service-template --test
```

**AC-3.2: CLI-Option für Prozesse**

WHEN der Handbook-Generator aufgerufen wird  
THEN SHALL eine neue Option `--process` verfügbar sein:
```bash
python -m src.cli --language de --process generic-process-template --test
```

**AC-3.3: Mutual Exclusivity**

WHEN CLI-Optionen verwendet werden  
THEN SHALL `--template`, `--service` und `--process` sich gegenseitig ausschließen  
AND nur eine Option gleichzeitig verwendet werden können.

**AC-3.4: Output-Format-Unterstützung**

WHEN Services oder Prozesse generiert werden  
THEN SHALL alle bestehenden Output-Formate unterstützt werden:
- Markdown (Standard)
- PDF
- HTML
- Separate Files

**AC-3.5: Placeholder-Verarbeitung**

WHEN Services oder Prozesse generiert werden  
THEN SHALL der PlaceholderProcessor alle Konfigurationsebenen verarbeiten:
- Globale Konfiguration (meta-global-service.yaml / meta-global-process.yaml)
- Spezifische Konfiguration (meta-service.yaml / meta-process.yaml)
- Bestehende Metadata-Konfigurationen (meta-global.yaml, meta-organisation.yaml, meta-organisation-roles.yaml)

**AC-3.6: Metadata-Adapter-Integration**

WHEN Services oder Prozesse generiert werden  
THEN SHALL der MetaAdapter erweitert werden um:
- Unterstützung für service.* Placeholders
- Unterstützung für process.* Placeholders
- Hierarchische Auflösung über alle Konfigurationsebenen
- Fallback auf [TODO] bei fehlenden Werten

**AC-3.7: Hilfe-Text-Erweiterung**

WHEN `--help` aufgerufen wird  
THEN SHALL die Hilfe Beispiele für Service- und Prozess-Generierung enthalten:
```
Examples:
  # Generate German service documentation
  python -m src.cli --language de --service generic-service-template --test
  
  # Generate English process documentation
  python -m src.cli --language en --process generic-process-template --test
  
  # Generate service documentation in PDF format
  python -m src.cli -l de --service my-service -o pdf --test
```

### US-4: Englische Übersetzung

**Als** internationaler Benutzer  
**möchte ich** Service- und Prozess-Templates auch auf Englisch verfügbar haben  
**damit** ich in meiner bevorzugten Sprache arbeiten kann.

#### Akzeptanzkriterien

**AC-4.1: Englische Service-Templates**

WHEN die deutsche Service-Dokumentation abgeschlossen ist  
THEN SHALL eine englische Version erstellt werden mit:
- Übersetzten Abschnittsüberschriften
- Übersetzten Placeholder-Beschreibungen
- Angepassten Beispielen
- Konsistenter Struktur zur deutschen Version

**AC-4.2: Englische Prozess-Templates**

WHEN die deutsche Prozess-Dokumentation abgeschlossen ist  
THEN SHALL eine englische Version erstellt werden mit:
- Übersetzten Abschnittsüberschriften
- Übersetzten RACI-Beschreibungen
- Übersetzten Compliance-Hinweisen
- Konsistenter Struktur zur deutschen Version

**AC-4.3: Sprachkonsistenz**

WHEN englische Templates erstellt werden  
THEN SHALL die Terminologie konsistent sein mit:
- Bestehenden englischen Handbook-Templates
- COBIT/ITIL-Standardterminologie
- BPMN-Standardterminologie

## Technische Anforderungen

### TR-1: Verzeichnisstruktur

- Services und Prozesse in separaten Verzeichnissen
- Sprachspezifische Unterverzeichnisse (de/en)
- Konsistente Namenskonventionen

### TR-2: YAML-Konfiguration

- Zweistufige Konfiguration (global + spezifisch)
- Integration mit bestehenden Metadata-Konfigurationen:
  - meta-global.yaml (Generator-Informationen)
  - meta-organisation.yaml (Organisations-Daten)
  - meta-organisation-roles.yaml (Rollen und Kontakte)
- Kompatibilität mit bestehendem PlaceholderProcessor
- Validierung der Placeholder-Syntax
- Hierarchische Auflösung mit definierter Priorität

### TR-3: CLI-Erweiterung

- Erweiterung von src/cli.py
- Neue Argument-Parser-Optionen
- Mutual Exclusivity zwischen Template-Typen
- Backward Compatibility mit bestehenden Optionen

### TR-4: Template-Manager-Integration

- Erweiterung von TemplateManager für Services/Prozesse
- Unterstützung für mehrere Konfigurationsebenen
- Integration mit MetaAdapter für hierarchische Placeholder-Auflösung
- Konsistente Fehlerbehandlung
- Unterstützung für role_* Referenzen aus meta-organisation-roles.yaml

### TR-5: Dokumentation

- README-Updates für neue Features
- Beispiele für Service- und Prozess-Generierung
- Dokumentation der Placeholder-Struktur

## Abhängigkeiten

- Bestehender Handbook-Generator
- PlaceholderProcessor
- TemplateManager
- ConfigManager
- OutputGenerator
- MetaAdapter (erweitert für service/process Placeholders)
- Bestehende Metadata-Konfigurationen (meta-global.yaml, meta-organisation.yaml, meta-organisation-roles.yaml)

## Placeholder-Beispiele

### Service-Template Placeholders

```markdown
# Service: {{ service.name }}

**Dokument-ID:** {{ service.id }}
**Organisation:** {{ meta-organisation.name }}
**Service Owner:** {{ service.owner }}  # Referenz: role_IT_Manager
**Service Manager:** {{ role_IT_Manager }}  # Direkt aus meta-organisation-roles.yaml
**Genehmigt durch:** {{ role_CIO }}
**Status:** {{ service.status }}
**Letzte Aktualisierung:** {{ service.modifydate }}
**Template Version:** {{ meta-global.version }}

## Kontaktinformationen

- **Organisation:** {{ meta-organisation.name }}
- **Adresse:** {{ meta-organisation.address }}
- **Telefon:** {{ meta-organisation.phone }}
- **Web:** {{ meta-organisation.web }}

## Eskalation

- **Level 1:** {{ group_Helpdesk }} ({{ group_Helpdesk_email }})
- **Level 2:** {{ role_IT_Manager }} ({{ role_IT_Manager_email }})
- **Level 3:** {{ role_CIO }} ({{ role_CIO_email }})
```

### Process-Template Placeholders

```markdown
# Prozess: {{ process.name }}

**Dokument-ID:** {{ process.id }}
**Organisation:** {{ meta-organisation.name }}
**Prozess Owner:** {{ process.owner }}  # Referenz: role_Risk_Manager
**Prozess Manager:** {{ role_Risk_Manager }}  # Direkt aus meta-organisation-roles.yaml
**Genehmigt durch:** {{ role_CEO }}
**Status:** {{ process.status }}

## RACI-Matrix

| Aktivität | {{ role_IT_Manager }} | {{ role_CISO }} | {{ role_Risk_Manager }} |
|-----------|----------------------|-----------------|-------------------------|
| Risikoidentifikation | R | C | A |
| Risikobewertung | C | R | A |
| Risikobehandlung | R | C | A |
```

## Nicht-Funktionale Anforderungen

### NFR-1: Konsistenz

Alle Templates (Handbooks, Services, Prozesse) sollen eine konsistente Struktur und Formatierung aufweisen.

### NFR-2: Erweiterbarkeit

Die Lösung soll einfach um weitere Service- und Prozess-Templates erweiterbar sein.

### NFR-3: Wartbarkeit

Code-Änderungen sollen minimal invasiv sein und bestehende Funktionalität nicht beeinträchtigen.

### NFR-4: Dokumentation

Alle neuen Features sollen vollständig dokumentiert sein mit Beispielen und Best Practices.

## Ausschlüsse

- Automatische BPMN-Diagramm-Generierung (nur Platzhalter)
- Automatische COBIT/ITIL-Mapping-Validierung
- Integration mit externen Service-Management-Tools
- Automatische KPI-Berechnung
