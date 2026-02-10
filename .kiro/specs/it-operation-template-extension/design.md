# Design Document: IT-Operations Template-Erweiterung

## Overview

Die IT-Operations Template-Erweiterung erweitert den bestehenden Handbuch-Generator um umfassende IT-Betriebshandbuch-Templates nach Best Practices aus ITIL, ISO 20000 und COBIT. Das System integriert 29 fachspezifische Templates, führt ein Meta-Platzhalter-System für organisationsweite Metadaten ein und erstellt eine globale Metadaten-Konfiguration für konsistente Organisationsinformationen über alle Handbücher hinweg.

Die Erweiterung baut auf der bestehenden Architektur des Handbuch-Generators auf und erweitert diese um:
- **Meta-Datenquelle**: Neue Datenquelle für organisationsweite Metadaten (analog zu NetBox)
- **Erweiterte Template-Struktur**: 29 fachspezifische Templates für IT-Operations
- **Globale Metadaten-Konfiguration**: Zentrale Verwaltung von Organisationsinformationen
- **Service-Beschreibungs-Template**: Generisches Template für individuelle Services
- **Mehrsprachige Erweiterung**: Alle neuen Templates in Deutsch und Englisch

**Kernfunktionalität:**
- Template-Umbenennung und Restrukturierung
- Integration von 29 ITIL/ISO 20000-konformen Templates
- Meta-Platzhalter-Verarbeitung ({{ meta.feld }})
- Globale Metadaten-Konfiguration (metadata.yaml)
- Generisches Service-Beschreibungs-Template
- Organisationsrollen-Management (CEO, CIO, CISO, CFO, COO)

## Architecture

### Extended High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Interface                            │
│  (Unchanged - existing functionality)                        │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                Template Manager                              │
│  - Extended: IT-Operations templates (29 new templates)     │
│  - Extended: Service description template support           │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Placeholder Processor                           │
│  - Extended: Meta placeholder detection                      │
│  - Extended: Dual-source routing (netbox + meta)            │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────────────────────────┐
│ Data Source     │    │     Output Generator                 │
│ Adapters        │    │  (Unchanged)                         │
│  - NetBox       │    └─────────────────────────────────────┘
│  - Meta (NEW)   │
└─────────────────┘
         │
┌────────▼────────────────────────────────────────────────────┐
│           Configuration Manager                              │
│  - Extended: metadata.yaml support                           │
│  - Extended: Organization roles management                   │
└─────────────────────────────────────────────────────────────┘
```

### Component Changes

**Neue Komponenten:**
1. **Meta Adapter** - Datenquelle für organisationsweite Metadaten
2. **Metadata Configuration Manager** - Verwaltung der metadata.yaml

**Erweiterte Komponenten:**
3. **Template Manager** - Unterstützung für 29 neue IT-Operations-Templates
4. **Placeholder Processor** - Erkennung und Verarbeitung von Meta-Platzhaltern
5. **Configuration Manager** - Laden und Validieren der Metadaten-Konfiguration


## Components and Interfaces

### 1. Meta Adapter (`src/meta_adapter.py`)

**Verantwortlichkeit:** Bereitstellung von organisationsweiten Metadaten aus der metadata.yaml

**Schnittstelle:**
```python
class MetaAdapter(DataSourceAdapter):
    def __init__(self, metadata_config: MetadataConfig):
        """Initialize Meta adapter with metadata configuration."""
        self.metadata = metadata_config
        
    def connect(self) -> bool:
        """Validate metadata configuration (no external connection needed)."""
        return self.metadata is not None
        
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Retrieve field value from metadata configuration.
        
        Examples:
        - "organization_name" -> metadata.organization.name
        - "ceo_name" -> metadata.roles.ceo.name
        - "ciso_email" -> metadata.roles.ciso.email
        - "document_owner" -> metadata.document.owner
        """
        
    def disconnect(self) -> None:
        """No-op for meta adapter (no external connection)."""
        pass
```

**Feldpfad-Auflösung:**
```python
def _resolve_field_path(self, field_path: str) -> Optional[str]:
    """
    Resolve dot-notation field path to metadata value.
    
    Supported paths:
    - organization.name, organization.address, organization.website
    - ceo.name, ceo.title, ceo.email, ceo.phone
    - cio.name, cio.title, cio.email, cio.phone
    - ciso.name, ciso.title, ciso.email, ciso.phone
    - cfo.name, cfo.title, cfo.email, cfo.phone
    - coo.name, coo.title, coo.email, coo.phone
    - document.owner, document.approver, document.version
    - author, version, language (shortcuts)
    """
```

### 2. Metadata Configuration Manager (`src/metadata_config_manager.py`)

**Verantwortlichkeit:** Laden und Validieren der globalen Metadaten-Konfiguration

**Schnittstelle:**
```python
class MetadataConfigManager:
    def __init__(self, config_path: Path = Path("metadata.yaml")):
        """Initialize with metadata config file path."""
        
    def load_metadata(self) -> MetadataConfig:
        """Load metadata configuration from file."""
        
    def create_default_metadata(self) -> None:
        """Create default metadata.yaml with example values."""
        
    def validate_metadata(self, metadata: MetadataConfig) -> list[str]:
        """Validate metadata configuration and return warnings."""
```

**MetadataConfig-Klasse:**
```python
@dataclass
class OrganizationInfo:
    name: str
    address: str
    city: str
    postal_code: str
    country: str
    website: str
    phone: str
    email: str

@dataclass
class PersonRole:
    name: str
    title: str
    email: str
    phone: str
    department: Optional[str] = None

@dataclass
class DocumentInfo:
    owner: str
    approver: str
    version: str
    classification: str  # public, internal, confidential, restricted

@dataclass
class MetadataConfig:
    organization: OrganizationInfo
    roles: dict[str, PersonRole]  # ceo, cio, ciso, cfo, coo, etc.
    document: DocumentInfo
    author: str
    language: str
    
    def get_role(self, role_name: str) -> Optional[PersonRole]:
        """Get role by name (case-insensitive)."""
```


### 3. Extended Placeholder Processor

**Erweiterungen:**
- Erkennung von Meta-Platzhaltern ({{ meta.feld }})
- Routing zu Meta-Adapter für meta-Quelle
- Einheitliche Fehlerbehandlung für beide Quellen

**Erweiterte Schnittstelle:**
```python
class PlaceholderProcessor:
    def __init__(self, data_sources: dict[str, DataSourceAdapter]):
        """
        Initialize with available data source adapters.
        Now supports: 'netbox' and 'meta'
        """
        
    def process_template(self, template_content: str) -> ProcessingResult:
        """Process template and replace all placeholders (netbox + meta)."""
        
    def _route_to_adapter(self, placeholder: Placeholder) -> Optional[str]:
        """Route placeholder to appropriate adapter based on source."""
```

**Unterstützte Platzhalter-Quellen:**
- `{{ netbox.field }}` - NetBox-Datenquelle (bestehend)
- `{{ meta.field }}` - Meta-Datenquelle (neu)

### 4. Extended Configuration Manager

**Erweiterungen:**
- Laden der metadata.yaml zusätzlich zur config.yaml
- Validierung der Metadaten-Struktur
- Integration mit Meta-Adapter

**Erweiterte Config-Klasse:**
```python
@dataclass
class Config:
    # Existing fields
    netbox_url: str
    netbox_api_token: str
    default_language: str = "de"
    default_output_format: str = "both"
    author: str = "Andreas Huemmer [andreas.huemmer@adminsend.de]"
    version: str = "1.0.0"
    
    # New field
    metadata: Optional[MetadataConfig] = None
```

**Erweiterte Methoden:**
```python
def load_config(self) -> Config:
    """
    Load configuration from config.yaml and metadata.yaml.
    Merges both configurations into single Config object.
    """
    
def ensure_metadata_file(self) -> None:
    """Ensure metadata.yaml exists, create default if missing."""
```


## Data Models

### Metadata Configuration File Schema (metadata.yaml)

```yaml
# Global Metadata Configuration
# This file contains organization-wide information used across all handbooks

organization:
  name: "AdminSend GmbH"
  address: "Musterstraße 123"
  city: "München"
  postal_code: "80331"
  country: "Deutschland"
  website: "https://www.adminsend.de"
  phone: "+49 89 12345678"
  email: "info@adminsend.de"

roles:
  ceo:
    name: "Max Mustermann"
    title: "Chief Executive Officer"
    email: "max.mustermann@adminsend.de"
    phone: "+49 89 12345678-100"
    department: "Management"
    
  cio:
    name: "Anna Schmidt"
    title: "Chief Information Officer"
    email: "anna.schmidt@adminsend.de"
    phone: "+49 89 12345678-200"
    department: "IT"
    
  ciso:
    name: "Thomas Weber"
    title: "Chief Information Security Officer"
    email: "thomas.weber@adminsend.de"
    phone: "+49 89 12345678-300"
    department: "IT Security"
    
  cfo:
    name: "Maria Müller"
    title: "Chief Financial Officer"
    email: "maria.mueller@adminsend.de"
    phone: "+49 89 12345678-400"
    department: "Finance"
    
  coo:
    name: "Peter Fischer"
    title: "Chief Operating Officer"
    email: "peter.fischer@adminsend.de"
    phone: "+49 89 12345678-500"
    department: "Operations"
    
  it_operations_manager:
    name: "Andreas Huemmer"
    title: "IT Operations Manager"
    email: "andreas.huemmer@adminsend.de"
    phone: "+49 89 12345678-250"
    department: "IT Operations"
    
  service_desk_lead:
    name: "Julia Becker"
    title: "Service Desk Lead"
    email: "julia.becker@adminsend.de"
    phone: "+49 89 12345678-111"
    department: "Service Desk"

document:
  owner: "IT Operations Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"  # public, internal, confidential, restricted

defaults:
  author: "Andreas Huemmer [andreas.huemmer@adminsend.de]"
  language: "de"
```

### Extended Template Directory Structure

```
templates/
├── de/
│   ├── it-operation/
│   │   ├── 0000_metadata_de_it-operation.md
│   │   ├── 0010_Einleitung.md                          # Renamed from 0100
│   │   ├── 0011_Rahmenbedingungen.md                   # Renamed from 0200
│   │   ├── 0020_Dokumentenlenkung_und_Versionierung.md # NEW
│   │   ├── 0030_Servicebeschreibung_und_Kritikalitaet.md # NEW
│   │   ├── 0040_Systemuebersicht_und_Architektur.md   # NEW
│   │   ├── 0050_Infrastruktur_und_Plattform.md        # NEW
│   │   ├── 0060_Rollen_und_Verantwortlichkeiten.md    # NEW
│   │   ├── 0070_Betriebskonzept_und_Betriebsprozesse.md # NEW
│   │   ├── 0080_Betriebsuebergabe_und_GoLive_Checkliste.md # NEW
│   │   ├── 0090_Konfigurationsmanagement_und_CMDB.md  # NEW
│   │   ├── 0100_Access_und_Berechtigungsmanagement.md # NEW
│   │   ├── 0110_Monitoring_Alerting_und_Observability.md # NEW
│   │   ├── 0120_Incident_Management_Runbook.md        # NEW
│   │   ├── 0130_Problem_Management_und_Postmortems.md # NEW
│   │   ├── 0140_Change_und_Release_Management.md      # NEW
│   │   ├── 0150_Backup_und_Restore.md                 # NEW
│   │   ├── 0160_Disaster_Recovery_und_Business_Continuity.md # NEW
│   │   ├── 0170_Sicherheitsbetrieb_und_Hardening.md   # NEW
│   │   ├── 0180_Patch_und_Update_Management.md        # NEW
│   │   ├── 0190_Log_Management_und_Audit.md           # NEW
│   │   ├── 0200_Kapazitaets_und_Performance_Management.md # NEW
│   │   ├── 0210_Verfuegbarkeit_und_Service_Level.md   # NEW
│   │   ├── 0220_Datenmanagement_und_Datenschutz.md    # NEW
│   │   ├── 0230_Wartung_und_Operations_Routinen.md    # NEW
│   │   ├── 0240_Runbooks_Standardoperationen.md       # NEW
│   │   ├── 0250_Tooling_und_Zugangswege.md            # NEW
│   │   ├── 0260_Bekannte_Probleme_und_FAQ.md          # NEW
│   │   ├── 0270_Kontakte_Eskalation_und_Anbieter.md   # NEW
│   │   ├── 0280_Compliance_und_Audits.md              # NEW
│   │   └── 0290_Anhang_Checklisten_und_Vorlagen.md    # NEW
│   └── service-templates/                              # NEW
│       └── service_description_template.md             # NEW
└── en/
    ├── it-operation/
    │   ├── 0000_metadata_en_it-operation.md
    │   ├── 0010_Introduction.md                        # Renamed
    │   ├── 0011_Framework_Conditions.md                # Renamed
    │   └── [... 29 English templates ...]              # NEW
    └── service-templates/                              # NEW
        └── service_description_template.md             # NEW
```


### Template Content Examples

**Example: 0060_Rollen_und_Verantwortlichkeiten.md (with Meta placeholders)**

```markdown
# Rollen und Verantwortlichkeiten

## Organisationsstruktur

**Organisation:** {{ meta.organization.name }}
**Standort:** {{ meta.organization.city }}, {{ meta.organization.country }}

## Führungsebene

### Chief Information Officer (CIO)
- **Name:** {{ meta.cio.name }}
- **E-Mail:** {{ meta.cio.email }}
- **Telefon:** {{ meta.cio.phone }}
- **Verantwortung:** Gesamtverantwortung für IT-Strategie und -Betrieb

### Chief Information Security Officer (CISO)
- **Name:** {{ meta.ciso.name }}
- **E-Mail:** {{ meta.ciso.email }}
- **Telefon:** {{ meta.ciso.phone }}
- **Verantwortung:** IT-Sicherheit, Compliance, Risikomanagement

## Betriebsebene

### IT Operations Manager
- **Name:** {{ meta.it_operations_manager.name }}
- **E-Mail:** {{ meta.it_operations_manager.email }}
- **Telefon:** {{ meta.it_operations_manager.phone }}
- **Verantwortung:** Täglicher IT-Betrieb, Service Delivery

### Service Desk Lead
- **Name:** {{ meta.service_desk_lead.name }}
- **E-Mail:** {{ meta.service_desk_lead.email }}
- **Telefon:** {{ meta.service_desk_lead.phone }}
- **Verantwortung:** First-Level-Support, Incident Management

## RACI-Matrix

| Aktivität | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Betrieb & Monitoring | A | C | R | I |
| Incident Management | A | C | R | R |
| Change Management | A | C | R | I |
| Security Incidents | A | R | C | I |
| Backup/Restore | A | C | R | I |

> Legende: **R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed
```

**Example: 0050_Infrastruktur_und_Plattform.md (with NetBox placeholders)**

```markdown
# Infrastruktur und Plattform

## Physische Infrastruktur

### Primärer Standort
- **Standort:** {{ netbox.site.name }}
- **Adresse:** {{ netbox.site.physical_address }}
- **Rechenzentrum:** {{ netbox.site.facility }}

### Netzwerkinfrastruktur
- **Core Switch:** {{ netbox.device.core_switch.name }}
- **Management VLAN:** {{ netbox.vlan.management.vid }}
- **Produktions-VLAN:** {{ netbox.vlan.production.vid }}

## Virtualisierung

### Hypervisor-Cluster
- **Cluster-Name:** {{ netbox.cluster.name }}
- **Hypervisor-Typ:** {{ netbox.cluster.type }}
- **Anzahl Hosts:** {{ netbox.cluster.device_count }}

## Cloud-Ressourcen

### Cloud-Provider
- **Provider:** {{ meta.organization.cloud_provider }}
- **Region:** {{ meta.organization.cloud_region }}
- **Account-ID:** {{ meta.organization.cloud_account_id }}
```


### Generic Service Description Template

**File:** `templates/de/service-templates/service_description_template.md`

```markdown
# Service-Beschreibung: [SERVICE_NAME]

> **Hinweis:** Dies ist ein generisches Template. Kopieren Sie diese Datei und passen Sie sie für Ihren spezifischen Service an.

## Service-Übersicht

### Basis-Informationen
- **Service-Name:** [TODO: Service-Name eintragen]
- **Service-ID:** [TODO: Eindeutige Service-ID]
- **Service-Owner:** {{ meta.service_owner.name }}
- **Technischer Ansprechpartner:** [TODO: Name und Kontakt]
- **Version:** {{ meta.document.version }}
- **Letzte Aktualisierung:** {{ meta.date }}

### Kurzbeschreibung
[TODO: 2-3 Sätze zur Beschreibung des Service]

### Geschäftszweck
[TODO: Welchen geschäftlichen Nutzen bietet dieser Service?]

### Nutzergruppen
- [TODO: Nutzergruppe 1]
- [TODO: Nutzergruppe 2]
- [TODO: Nutzergruppe 3]

## Technische Details

### Systemkomponenten
| Komponente | Typ | Standort | Verantwortlich |
|---|---|---|---|
| [TODO] | [TODO] | {{ netbox.site.name }} | [TODO] |

### Abhängigkeiten

#### Upstream-Abhängigkeiten (Services, von denen dieser Service abhängt)
- [TODO: Service 1]
- [TODO: Service 2]

#### Downstream-Abhängigkeiten (Services, die von diesem Service abhängen)
- [TODO: Service 1]
- [TODO: Service 2]

### Schnittstellen
| Schnittstelle | Typ | Protokoll | Port | Beschreibung |
|---|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## Betrieb

### Servicezeiten
- **Verfügbarkeit:** [TODO: z.B. 24/7, Mo-Fr 08:00-18:00]
- **Support-Zeiten:** [TODO: Wann ist Support verfügbar?]
- **Wartungsfenster:** [TODO: Geplante Wartungszeiten]

### Service Level Agreements (SLA)

| Kennzahl | Zielwert | Messmethode |
|---|---:|---|
| Verfügbarkeit | [TODO]% | [TODO] |
| Antwortzeit | [TODO] ms | [TODO] |
| MTTR | [TODO] h | [TODO] |
| MTBF | [TODO] h | [TODO] |

### Kritikalität

| Dimension | Einstufung | Begründung |
|---|---|---|
| Verfügbarkeit | ☐ niedrig ☐ mittel ☐ hoch | [TODO] |
| Integrität | ☐ niedrig ☐ mittel ☐ hoch | [TODO] |
| Vertraulichkeit | ☐ niedrig ☐ mittel ☐ hoch | [TODO] |

## Monitoring und Alerting

### Monitoring-Metriken
- [TODO: Metrik 1 - Beschreibung und Schwellwert]
- [TODO: Metrik 2 - Beschreibung und Schwellwert]
- [TODO: Metrik 3 - Beschreibung und Schwellwert]

### Alerting-Regeln
| Alert | Schwellwert | Priorität | Eskalation |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

### Dashboards
- [TODO: Link zu Monitoring-Dashboard]
- [TODO: Link zu Performance-Dashboard]

## Backup und Recovery

### Backup-Strategie
- **Backup-Typ:** [TODO: Full/Incremental/Differential]
- **Backup-Frequenz:** [TODO: Täglich/Wöchentlich]
- **Aufbewahrungsdauer:** [TODO: Tage/Wochen/Monate]
- **Backup-Speicherort:** {{ netbox.backup_location }}

### Recovery-Ziele
- **RTO (Recovery Time Objective):** [TODO: Stunden]
- **RPO (Recovery Point Objective):** [TODO: Stunden]

## Sicherheit

### Zugriffskontrolle
- **Authentifizierung:** [TODO: Methode]
- **Autorisierung:** [TODO: Rollenmodell]
- **Berechtigte Gruppen:** [TODO: AD-Gruppen/Rollen]

### Compliance-Anforderungen
- [TODO: ISO 27001]
- [TODO: DSGVO]
- [TODO: Weitere Standards]

## Kontakte und Eskalation

### Verantwortlichkeiten
- **Service Owner:** {{ meta.service_owner.name }} ({{ meta.service_owner.email }})
- **Technical Lead:** [TODO: Name und Kontakt]
- **On-Call:** [TODO: Rufbereitschaft-Kontakt]

### Eskalationspfad
1. **Level 1:** Service Desk - {{ meta.service_desk_lead.email }}
2. **Level 2:** IT Operations - {{ meta.it_operations_manager.email }}
3. **Level 3:** CIO - {{ meta.cio.email }}

## Änderungshistorie

| Version | Datum | Autor | Änderungen |
|---|---|---|---|
| 1.0.0 | [TODO] | [TODO] | Initiale Version |

---

**Dokumentverantwortlicher:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Organisation:** {{ meta.organization.name }}
```


## IT Framework Alignment

### ITIL v4 Process Mapping

Die Templates orientieren sich an ITIL v4 Service Management Practices:

| Template | ITIL Practice | Beschreibung |
|---|---|---|
| 0070_Betriebskonzept | Service Design | Betriebsmodelle und Prozessdesign |
| 0110_Monitoring | Monitoring and Event Management | Überwachung und Event-Behandlung |
| 0120_Incident_Management | Incident Management | Störungsbehandlung |
| 0130_Problem_Management | Problem Management | Ursachenanalyse und Prävention |
| 0140_Change_Management | Change Enablement | Änderungssteuerung |
| 0140_Change_Management | Release Management | Release-Planung und Deployment |
| 0150_Backup | Service Continuity Management | Datensicherung |
| 0160_Disaster_Recovery | Service Continuity Management | Notfallwiederherstellung |
| 0090_Konfigurationsmanagement | Service Configuration Management | CMDB und CI-Verwaltung |
| 0100_Access_Management | Service Desk | Zugriffsverwaltung |
| 0210_Verfuegbarkeit | Availability Management | Verfügbarkeitsmanagement |
| 0200_Kapazitaetsmanagement | Capacity and Performance Management | Kapazitätsplanung |

### ISO 20000 Compliance

Templates unterstützen ISO 20000-1:2018 Anforderungen:

| ISO 20000 Clause | Template | Abdeckung |
|---|---|---|
| 6.1 Service Planning | 0070_Betriebskonzept | Service-Planung |
| 8.2 Service Catalogue | 0030_Servicebeschreibung | Service-Katalog |
| 8.3 Service Level Management | 0210_Verfuegbarkeit | SLA-Management |
| 8.4 Service Reporting | 0110_Monitoring | Service-Reporting |
| 8.5 Service Continuity | 0160_Disaster_Recovery | Business Continuity |
| 8.6 Budgeting | 0200_Kapazitaetsmanagement | Budgetplanung |
| 8.7 Capacity Management | 0200_Kapazitaetsmanagement | Kapazitätsmanagement |
| 8.8 Information Security | 0170_Sicherheitsbetrieb | Informationssicherheit |

### COBIT 2019 Alignment

Templates unterstützen COBIT 2019 Governance und Management Objectives:

| COBIT Objective | Template | Fokus |
|---|---|---|
| APO01 Managed IT Management Framework | 0070_Betriebskonzept | IT-Management-Framework |
| APO02 Managed Strategy | 0010_Einleitung | IT-Strategie |
| APO07 Managed Human Resources | 0060_Rollen | Personalmanagement |
| APO09 Managed Service Agreements | 0210_Verfuegbarkeit | Service-Vereinbarungen |
| APO12 Managed Risk | 0160_Disaster_Recovery | Risikomanagement |
| APO13 Managed Security | 0170_Sicherheitsbetrieb | Sicherheitsmanagement |
| BAI03 Managed Solutions Identification | 0040_Systemuebersicht | Lösungsidentifikation |
| BAI06 Managed IT Changes | 0140_Change_Management | Change Management |
| BAI10 Managed Configuration | 0090_Konfigurationsmanagement | Konfigurationsmanagement |
| DSS01 Managed Operations | 0230_Wartung | Betriebsmanagement |
| DSS02 Managed Service Requests | 0120_Incident_Management | Service-Anfragen |
| DSS03 Managed Problems | 0130_Problem_Management | Problem-Management |
| DSS04 Managed Continuity | 0160_Disaster_Recovery | Kontinuitätsmanagement |
| DSS05 Managed Security Services | 0170_Sicherheitsbetrieb | Sicherheitsdienste |
| DSS06 Managed Business Process Controls | 0280_Compliance | Prozesskontrollen |


## Correctness Properties

*Eine Property ist eine Eigenschaft oder ein Verhalten, das über alle gültigen Ausführungen eines Systems hinweg wahr sein sollte - im Wesentlichen eine formale Aussage darüber, was das System tun soll. Properties dienen als Brücke zwischen menschenlesbaren Spezifikationen und maschinenverifizierbaren Korrektheitsgarantien.*

### Property 1: Meta Placeholder Detection
*For any* template content containing meta placeholders in the format "{{ meta.field }}", the system should correctly identify all meta placeholders and distinguish them from netbox placeholders.
**Validates: Requirements 16.1, 16.2**

### Property 2: Meta Field Resolution
*For any* valid meta field path (e.g., "organization.name", "ceo.email"), the system should correctly resolve the field from the metadata configuration and return the corresponding value.
**Validates: Requirements 16.3, 17.2, 17.3**

### Property 3: Meta Field Not Found Handling
*For any* meta placeholder referencing a non-existent field in the metadata configuration, the system should generate a warning and leave the placeholder unchanged.
**Validates: Requirements 16.4**

### Property 4: Dual Source Placeholder Processing
*For any* template containing both netbox and meta placeholders, the system should correctly process both types and route each to the appropriate adapter.
**Validates: Requirements 16.5, 19.2**

### Property 5: Metadata Configuration Loading
*For any* valid metadata.yaml file, the system should correctly parse all sections (organization, roles, document) and create a complete MetadataConfig object.
**Validates: Requirements 17.1, 17.2**

### Property 6: Organization Role Validation
*For any* metadata configuration, if a role (ceo, cio, ciso, cfo, coo) is defined, it should contain at minimum name, title, and email fields.
**Validates: Requirements 18.1, 18.2, 18.5**

### Property 7: Role Field Access
*For any* defined role in the metadata configuration, the system should support accessing role fields via placeholders like "{{ meta.ceo.name }}" and "{{ meta.ciso.email }}".
**Validates: Requirements 18.3**

### Property 8: Missing Role Handling
*For any* placeholder referencing an undefined role, the system should use a default placeholder text or generate a warning.
**Validates: Requirements 18.4**

### Property 9: Template File Renaming
*For any* existing IT-operations template files, when the renaming process is executed, files should be renamed according to the new numbering scheme (0100→0010, 0200→0011).
**Validates: Requirements 1.1, 1.2**

### Property 10: Bilingual Template Consistency
*For any* German IT-operations template, there should exist a corresponding English template with the same numbering and equivalent content structure.
**Validates: Requirements 21.1, 21.2, 21.5**

### Property 11: Template Numbering Sequence
*For any* set of IT-operations templates, the numbering should follow the sequence 0010, 0011, 0020, 0030, ..., 0290 with no gaps in the defined templates.
**Validates: Requirements 2.2**

### Property 12: ITIL Process Coverage
*For any* ITIL v4 core practice (Incident, Problem, Change, Service Continuity), there should exist at least one template that addresses that practice.
**Validates: Requirements 2.5**

### Property 13: Service Template Genericity
*For any* service description template, it should contain placeholder sections that can be customized for any specific IT service without requiring template structure changes.
**Validates: Requirements 15.2, 15.3, 15.5**

### Property 14: RACI Matrix Completeness
*For any* template containing a RACI matrix, all cells should be filled with one of the valid RACI values (R, A, C, I) or explicitly marked as not applicable.
**Validates: Requirements 20.4**

### Property 15: Metadata Configuration Validation
*For any* metadata.yaml file, the validation process should check for required fields (organization.name, document.owner) and report missing fields as warnings.
**Validates: Requirements 17.4, 17.5**

### Property 16: Template Best Practice Compliance
*For any* IT-operations template, it should reference at least one recognized IT framework (ITIL, ISO 20000, COBIT) in its content or structure.
**Validates: Requirements 20.3**

### Property 17: Multi-Language Placeholder Consistency
*For any* placeholder used in a German template, the same placeholder (with same source and field) should be usable in the corresponding English template.
**Validates: Requirements 21.4**

### Property 18: Service Template Individualization
*For any* service description template, when copied and customized for a specific service, all [TODO] markers should be replaceable with service-specific values while maintaining template structure.
**Validates: Requirements 15.4**

### Property 19: Template Documentation Completeness
*For any* template directory containing IT-operations templates, there should exist a README.md file documenting the template structure and usage.
**Validates: Requirements 22.1, 22.2**

### Property 20: Configuration File Separation
*For any* system configuration, metadata configuration (metadata.yaml) should be separate from data source configuration (config.yaml) and both should be loadable independently.
**Validates: Requirements 17.1, 19.1**


## Implementation Strategy

### Phase 1: Meta-Platzhalter-System (Foundation)

**Ziel:** Grundlegende Infrastruktur für Meta-Platzhalter schaffen

**Komponenten:**
1. **MetadataConfig Datenmodell** (`src/metadata_config_manager.py`)
   - OrganizationInfo, PersonRole, DocumentInfo Klassen
   - MetadataConfig Hauptklasse
   - Validierungslogik

2. **MetadataConfigManager** (`src/metadata_config_manager.py`)
   - YAML-Parsing für metadata.yaml
   - Default-Konfiguration erstellen
   - Validierung und Fehlerbehandlung

3. **Meta Adapter** (`src/meta_adapter.py`)
   - DataSourceAdapter Interface implementieren
   - Feldpfad-Auflösung (dot-notation)
   - Rollenfeld-Zugriff

4. **Placeholder Processor Erweiterung** (`src/placeholder_processor.py`)
   - Meta-Platzhalter-Erkennung
   - Routing zu Meta-Adapter
   - Einheitliche Fehlerbehandlung

**Tests:**
- Unit-Tests für MetadataConfig-Parsing
- Unit-Tests für Meta-Adapter Feldauflösung
- Property-Tests für Platzhalter-Erkennung
- Integration-Tests für Dual-Source-Processing

### Phase 2: Template-Struktur-Erweiterung

**Ziel:** IT-Operations-Templates erstellen und integrieren

**Aufgaben:**
1. **Template-Umbenennung**
   - 0100_einleitung.md → 0010_Einleitung.md
   - 0200_betriebsprozesse.md → 0011_Rahmenbedingungen.md
   - Englische Versionen entsprechend

2. **Fachspezifische Templates erstellen** (29 Templates)
   - Deutsche Versionen (templates/de/it-operation/)
   - Englische Versionen (templates/en/it-operation/)
   - Meta- und NetBox-Platzhalter integrieren
   - ITIL/ISO 20000/COBIT Best Practices einarbeiten

3. **Service-Beschreibungs-Template**
   - Generisches Template erstellen
   - Individualisierungshinweise
   - Beispiel-Platzhalter

**Templates-Reihenfolge:**
- 0020: Dokumentenlenkung und Versionierung
- 0030: Servicebeschreibung und Kritikalität
- 0040: Systemübersicht und Architektur
- 0050: Infrastruktur und Plattform
- 0060: Rollen und Verantwortlichkeiten
- 0070: Betriebskonzept und Betriebsprozesse
- 0080: Betriebsübergabe und Go-Live-Checkliste
- 0090: Konfigurationsmanagement und CMDB
- 0100: Access- und Berechtigungsmanagement
- 0110: Monitoring, Alerting und Observability
- 0120: Incident Management – Runbook
- 0130: Problem Management und Postmortems
- 0140: Change- und Release-Management
- 0150: Backup und Restore
- 0160: Disaster Recovery und Business Continuity
- 0170: Sicherheitsbetrieb und Hardening
- 0180: Patch- und Update-Management
- 0190: Log Management und Audit
- 0200: Kapazitäts- und Performance-Management
- 0210: Verfügbarkeit und Service Level
- 0220: Datenmanagement und Datenschutz
- 0230: Wartung und Operations-Routinen
- 0240: Runbooks – Standardoperationen
- 0250: Tooling und Zugangswege
- 0260: Bekannte Probleme und FAQ
- 0270: Kontakte, Eskalation und Anbieter
- 0280: Compliance und Audits
- 0290: Anhang: Checklisten und Vorlagen

### Phase 3: Konfiguration und Integration

**Ziel:** Metadaten-Konfiguration und System-Integration

**Aufgaben:**
1. **metadata.yaml erstellen**
   - Default-Konfiguration mit Beispielwerten
   - Alle Organisationsrollen definieren
   - Dokumentation und Kommentare

2. **ConfigManager erweitern**
   - metadata.yaml laden
   - Mit config.yaml zusammenführen
   - Validierung beider Konfigurationen

3. **CLI-Integration**
   - Keine Änderungen erforderlich (transparent)
   - Metadaten automatisch laden
   - Fehlerbehandlung für fehlende metadata.yaml

**Tests:**
- Unit-Tests für Konfigurationsmanagement
- Integration-Tests für vollständigen Workflow
- Property-Tests für Metadaten-Validierung

### Phase 4: Dokumentation und Validierung

**Ziel:** Dokumentation und Template-Validierung

**Aufgaben:**
1. **Template-Dokumentation**
   - README.md für IT-Operations-Templates
   - Nutzungshinweise
   - Best-Practice-Beispiele
   - Framework-Referenzen (ITIL, ISO 20000, COBIT)

2. **Template-Validierung**
   - RACI-Matrix-Vollständigkeit prüfen
   - Platzhalter-Konsistenz prüfen
   - Framework-Compliance prüfen

3. **Beispiel-Handbuch generieren**
   - Vollständiges IT-Operations-Handbuch
   - Mit Beispiel-Metadaten
   - Deutsch und Englisch

**Tests:**
- Validierungs-Tests für alle Templates
- End-to-End-Tests mit vollständiger Generierung
- Property-Tests für Template-Qualität


## Testing Strategy

### Dual Testing Approach

Die Teststrategie kombiniert Unit-Tests für spezifische Beispiele mit Property-Based Tests für universelle Eigenschaften:

**Unit Tests:**
- Meta-Adapter Feldauflösung mit bekannten Pfaden
- Metadaten-Konfiguration Parsing
- Template-Umbenennung
- RACI-Matrix-Validierung
- Service-Template-Struktur

**Property-Based Tests:**
- Meta-Platzhalter-Erkennung über verschiedene Formate
- Feldpfad-Auflösung mit randomisierten Pfaden
- Dual-Source-Processing mit gemischten Platzhaltern
- Metadaten-Validierung mit verschiedenen Konfigurationen
- Template-Nummerierung und Sortierung

### Property-Based Testing Configuration

**Bibliothek:** [Hypothesis](https://hypothesis.readthedocs.io/) für Python

**Test-Konfiguration:**
```python
from hypothesis import given, settings
import hypothesis.strategies as st

@settings(max_examples=100)
@given(
    field_path=st.text(
        alphabet=st.characters(whitelist_categories=('Ll', 'Lu')),
        min_size=1
    ).map(lambda s: s.replace(' ', '.'))
)
def test_meta_field_resolution(field_path):
    """
    Feature: it-operation-template-extension, Property 2: Meta Field Resolution
    """
    # Test implementation
```

**Strategien für Template-Tests:**
```python
# Strategy for generating valid metadata configurations
@st.composite
def metadata_config_strategy(draw):
    return MetadataConfig(
        organization=OrganizationInfo(
            name=draw(st.text(min_size=1, max_size=100)),
            address=draw(st.text(min_size=1, max_size=200)),
            # ... weitere Felder
        ),
        roles={
            'ceo': PersonRole(
                name=draw(st.text(min_size=1, max_size=100)),
                title=draw(st.text(min_size=1, max_size=100)),
                email=draw(st.emails()),
                phone=draw(st.text(min_size=1, max_size=50))
            ),
            # ... weitere Rollen
        },
        # ... weitere Konfiguration
    )

# Strategy for generating templates with placeholders
@st.composite
def template_with_placeholders_strategy(draw):
    num_meta = draw(st.integers(min_value=0, max_value=10))
    num_netbox = draw(st.integers(min_value=0, max_value=10))
    
    lines = []
    for _ in range(num_meta):
        field = draw(st.sampled_from([
            'organization.name', 'ceo.name', 'cio.email', 'ciso.phone'
        ]))
        lines.append(f"{{{{ meta.{field} }}}}")
    
    for _ in range(num_netbox):
        field = draw(st.sampled_from([
            'device.name', 'site.location', 'vlan.vid'
        ]))
        lines.append(f"{{{{ netbox.{field} }}}}")
    
    return '\n'.join(lines)
```

### Test Coverage Areas

**1. Meta Adapter Tests**
- Feldpfad-Auflösung für alle unterstützten Pfade
- Fehlerbehandlung für ungültige Pfade
- Rollenfeld-Zugriff (ceo.name, ciso.email, etc.)
- Organisationsfeld-Zugriff
- Dokumentfeld-Zugriff

**2. Metadata Configuration Manager Tests**
- YAML-Parsing mit verschiedenen Strukturen
- Validierung von Pflichtfeldern
- Default-Konfiguration erstellen
- Fehlerbehandlung für ungültige YAML
- Rollenvalidierung

**3. Placeholder Processor Extension Tests**
- Meta-Platzhalter-Erkennung
- Dual-Source-Routing (meta + netbox)
- Fehlerbehandlung für unbekannte Quellen
- Platzhalter-Ersetzung mit beiden Quellen
- Statistiken für beide Quellen

**4. Template Structure Tests**
- Template-Umbenennung korrekt
- Alle 29 Templates vorhanden
- Nummerierung konsistent (0010-0290)
- Bilinguale Konsistenz (de/en)
- Service-Template-Struktur

**5. Template Content Tests**
- RACI-Matrix-Vollständigkeit
- Platzhalter-Syntax korrekt
- Framework-Referenzen vorhanden
- Abschnittsstruktur konsistent
- Meta- und NetBox-Platzhalter gemischt

**6. Integration Tests**
- End-to-End mit Meta-Platzhaltern
- End-to-End mit gemischten Platzhaltern
- Vollständiges IT-Operations-Handbuch generieren
- Bilinguale Generierung
- Service-Template-Individualisierung

### Test Data

**Sample Metadata Configurations:**
```yaml
# Minimal configuration
organization:
  name: "Test Org"
roles:
  ceo:
    name: "Test CEO"
    email: "ceo@test.com"
document:
  owner: "Test Owner"

# Complete configuration
organization:
  name: "AdminSend GmbH"
  address: "Musterstraße 123"
  city: "München"
  # ... alle Felder
roles:
  ceo: { name: "...", title: "...", email: "...", phone: "..." }
  cio: { name: "...", title: "...", email: "...", phone: "..." }
  # ... alle Rollen
document:
  owner: "IT Operations Manager"
  approver: "CIO"
  version: "1.0.0"
```

**Sample Templates with Meta Placeholders:**
```markdown
# Test Template 1: Organization Info
Organization: {{ meta.organization.name }}
Location: {{ meta.organization.city }}

# Test Template 2: Roles
CEO: {{ meta.ceo.name }} ({{ meta.ceo.email }})
CIO: {{ meta.cio.name }} ({{ meta.cio.email }})

# Test Template 3: Mixed Placeholders
Organization: {{ meta.organization.name }}
Site: {{ netbox.site.name }}
CEO: {{ meta.ceo.name }}
Device: {{ netbox.device.name }}
```

**Mock Data Sources:**
- Metadata configurations mit allen Rollen
- Metadata configurations mit fehlenden Rollen
- Ungültige YAML-Strukturen
- NetBox-Responses (bestehend)


## Dependencies

### New Dependencies

```
# No new external dependencies required!
# All new functionality uses existing dependencies:
# - pyyaml (already in requirements.txt) for metadata.yaml parsing
# - pathlib (built-in) for file operations
# - dataclasses (built-in) for data models
```

### Existing Dependencies (Unchanged)

```
# requirements.txt (from handbook-generator)

# Template Processing
jinja2>=3.1.0

# Data Source Integration
pynetbox>=7.0.0
requests>=2.31.0

# Configuration Management
pyyaml>=6.0                # Used for both config.yaml and metadata.yaml

# Output Generation
markdown>=3.5.0
markdown-pdf>=1.0.0

# CLI
argparse                   # Built-in
pathlib                    # Built-in

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
hypothesis>=6.90.0
responses>=0.24.0

# Development
flake8>=6.1.0
black>=23.0.0
mypy>=1.7.0
```

## Error Handling

### New Error Categories

**1. Metadata Configuration Errors**
- Missing metadata.yaml → Create default, inform user
- Invalid YAML structure → Parse error with line number
- Missing required fields → Warning with field names
- Invalid role definitions → Error with role name and missing fields

**2. Meta Placeholder Errors**
- Unknown meta field → Warning, leave placeholder unchanged
- Invalid field path → Warning with valid path examples
- Missing role in configuration → Warning, suggest adding role

**3. Template Structure Errors**
- Missing IT-operations templates → Error with expected files
- Inconsistent numbering → Warning with numbering gaps
- Missing bilingual templates → Warning with missing language
- Invalid RACI matrix → Warning with incomplete cells

### Error Handling Strategy

**Graceful Degradation:**
- Missing metadata.yaml → Use defaults, continue processing
- Missing meta fields → Leave placeholders, continue processing
- Invalid templates → Skip template, continue with others
- Collect all errors and warnings, display comprehensive summary

**User-Friendly Messages:**
```python
# Example error messages

# Missing metadata.yaml
"Metadata configuration file 'metadata.yaml' not found. "
"Creating default configuration. Please edit metadata.yaml "
"with your organization's information."

# Missing meta field
"Warning: Meta field 'ceo.name' not found in metadata.yaml. "
"Placeholder '{{ meta.ceo.name }}' left unchanged. "
"Add CEO information to metadata.yaml under 'roles.ceo.name'."

# Invalid RACI matrix
"Warning: RACI matrix in template '0060_Rollen_und_Verantwortlichkeiten.md' "
"has incomplete cells. All cells should contain R, A, C, or I."

# Missing bilingual template
"Warning: English template '0030_Service_Description_and_Criticality.md' "
"not found. German template exists but English version is missing."
```

## Security Considerations

### Metadata Security

**Sensitive Information:**
- Metadata.yaml kann sensible Informationen enthalten (Namen, E-Mails, Telefonnummern)
- Sollte in .gitignore eingetragen werden (optional, da keine Credentials)
- Warnung wenn Datei world-readable ist

**Input Validation:**
- Validierung aller Metadaten-Felder
- Sanitization von E-Mail-Adressen
- Validierung von Telefonnummern (Format)
- Prüfung auf Code-Injection in Feldern

**Access Control:**
- Metadata.yaml sollte nur von autorisierten Personen editierbar sein
- Empfehlung: Dateiberechtigungen 640 (rw-r-----)

## Performance Considerations

### Metadata Loading

**Caching:**
- Metadata.yaml nur einmal pro Programmlauf laden
- MetadataConfig-Objekt im Speicher halten
- Keine wiederholten Dateizugriffe

**Lazy Loading:**
- Metadata nur laden wenn Meta-Platzhalter gefunden werden
- Vermeidung unnötiger Dateizugriffe

### Template Processing

**Parallel Processing:**
- Templates können parallel verarbeitet werden
- Meta-Adapter ist thread-safe (keine externen Verbindungen)
- Shared MetadataConfig-Objekt zwischen Threads

**Memory Efficiency:**
- MetadataConfig ist klein (< 10 KB typisch)
- Keine großen Datenstrukturen im Speicher
- Stream-Processing für große Templates

## Migration Guide

### Für bestehende Handbuch-Generator-Nutzer

**Schritt 1: Metadata.yaml erstellen**
```bash
# System erstellt automatisch default metadata.yaml beim ersten Start
python -m src.cli --language de --template it-operation

# Oder manuell erstellen
cp metadata.example.yaml metadata.yaml
# Bearbeiten mit eigenen Organisationsdaten
```

**Schritt 2: Bestehende Templates aktualisieren**
```bash
# Keine Aktion erforderlich!
# Bestehende Templates funktionieren weiterhin
# Meta-Platzhalter sind optional
```

**Schritt 3: Meta-Platzhalter verwenden (optional)**
```markdown
# In bestehenden Templates Meta-Platzhalter hinzufügen
Organisation: {{ meta.organization.name }}
Verantwortlich: {{ meta.cio.name }}
```

**Schritt 4: IT-Operations-Templates nutzen**
```bash
# Neue IT-Operations-Templates sind automatisch verfügbar
python -m src.cli --language de --template it-operation
```

### Abwärtskompatibilität

**Garantiert:**
- Bestehende Templates funktionieren unverändert
- Bestehende config.yaml bleibt gültig
- Bestehende NetBox-Platzhalter funktionieren
- Keine Breaking Changes in CLI oder API

**Optional:**
- metadata.yaml ist optional
- Meta-Platzhalter sind optional
- Neue IT-Operations-Templates sind zusätzlich

## Implementation Notes

### Code-Organisation

```
src/
├── cli.py                          # Unchanged
├── template_manager.py             # Minor extension for new templates
├── placeholder_processor.py        # Extended for meta placeholders
├── data_source_adapter.py          # Unchanged (base interface)
├── netbox_adapter.py               # Unchanged
├── meta_adapter.py                 # NEW
├── config_manager.py               # Extended for metadata.yaml
├── metadata_config_manager.py      # NEW
├── output_generator.py             # Unchanged
├── logger.py                       # Unchanged
└── error_handler.py                # Unchanged

templates/
├── de/
│   └── it-operation/
│       ├── 0000_metadata_de_it-operation.md
│       ├── 0010_Einleitung.md              # Renamed
│       ├── 0011_Rahmenbedingungen.md       # Renamed
│       ├── 0020_Dokumentenlenkung_und_Versionierung.md  # NEW
│       └── [... 26 weitere neue Templates ...]
└── en/
    └── it-operation/
        └── [... entsprechende englische Templates ...]

tests/
├── test_meta_adapter.py            # NEW
├── test_metadata_config_manager.py # NEW
├── test_placeholder_processor_extended.py  # NEW
├── test_template_structure.py      # NEW
└── test_integration_meta.py        # NEW
```

### Development Workflow

1. **Meta-Adapter entwickeln** → Unit-Tests → Integration-Tests
2. **Metadata-Config-Manager entwickeln** → Unit-Tests → Validierungs-Tests
3. **Placeholder-Processor erweitern** → Unit-Tests → Property-Tests
4. **Templates erstellen** → Struktur-Tests → Content-Tests
5. **Integration testen** → End-to-End-Tests → Beispiel-Handbuch generieren
6. **Dokumentation schreiben** → README → Migration-Guide

### Quality Assurance

**Code Quality:**
- PEP 8 Compliance (flake8)
- Type Hints (mypy)
- Code Formatting (black)
- Test Coverage > 90%

**Template Quality:**
- RACI-Matrix-Vollständigkeit
- Platzhalter-Syntax-Validierung
- Framework-Referenz-Prüfung
- Bilinguale Konsistenz

**Documentation Quality:**
- README mit Beispielen
- Inline-Kommentare in Templates
- Migration-Guide für Nutzer
- API-Dokumentation für Entwickler
