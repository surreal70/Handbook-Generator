# Service and Process Documentation System - Design Document

## 1. Architektur-Überblick

### 1.1 System-Kontext

Das Service and Process Documentation System erweitert den bestehenden Handbook-Generator um zwei neue Dokumentationstypen:
- IT-Service-Dokumentation (COBIT/ITIL-konform)
- Geschäftsprozess-Dokumentation (BPMN/RACI-basiert)

Die Erweiterung integriert sich nahtlos in die bestehende Architektur und nutzt die vorhandenen Metadata-Konfigurationen.

### 1.2 Komponenten-Diagramm

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLI (cli.py)                             │
│  --template | --service | --process                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   TemplateManager                                │
│  - discover_templates()                                          │
│  - discover_services()      ← NEW                                │
│  - discover_processes()     ← NEW                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              PlaceholderProcessor                                │
│  - process_template()                                            │
│  - resolve_placeholder()                                         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MetaAdapter                                   │
│  - get_field()                                                   │
│  - set_service_type()       ← NEW                                │
│  - set_process_type()       ← NEW                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              Metadata Configuration Files                        │
│  ┌──────────────────┐  ┌──────────────────┐  ┌────────────────┐│
│  │ meta-global.yaml │  │meta-organisation │  │meta-org-roles  ││
│  │                  │  │     .yaml        │  │    .yaml       ││
│  └──────────────────┘  └──────────────────┘  └────────────────┘│
│  ┌──────────────────┐  ┌──────────────────┐                    │
│  │meta-global-      │  │meta-global-      │                    │
│  │  service.yaml    │  │  process.yaml    │                    │
│  └──────────────────┘  └──────────────────┘                    │
│  ┌──────────────────┐  ┌──────────────────┐                    │
│  │meta-service      │  │meta-process      │                    │
│  │    .yaml         │  │    .yaml         │                    │
│  └──────────────────┘  └──────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
```

### 1.3 Datenfluss

1. **CLI-Aufruf**: Benutzer ruft CLI mit `--service` oder `--process` auf
2. **Template-Discovery**: TemplateManager findet Service/Process-Templates
3. **Metadata-Loading**: MetaAdapter lädt alle Konfigurationsebenen
4. **Placeholder-Resolution**: PlaceholderProcessor löst Placeholders hierarchisch auf
5. **Output-Generation**: OutputGenerator erstellt Markdown/PDF/HTML

## 2. Detailliertes Design

### 2.1 Verzeichnisstruktur

```
services/
├── de/
│   ├── meta-global-service.yaml         # Global config
│   ├── generic-service-template/
│   │   ├── meta-service.yaml            # Specific config
│   │   └── service-template.md          # Template
│   └── email-service/                   # Example service
│       ├── meta-service.yaml
│       └── email-service.md
└── en/
    └── [same structure]

processes/
├── de/
│   ├── meta-global-process.yaml         # Global config
│   ├── generic-process-template/
│   │   ├── meta-process.yaml            # Specific config
│   │   ├── diagrams/
│   │   │   └── process-flow.bpmn
│   │   └── process-template.md          # Template
│   └── incident-management/             # Example process
│       ├── meta-process.yaml
│       ├── diagrams/
│       └── incident-management.md
└── en/
    └── [same structure]
```


### 2.2 Konfigurationsdateien

#### 2.2.1 meta-global-service.yaml (Global)

```yaml
# Global Service Configuration
# Applies to all services unless overridden

# Default SLA values
sla:
  availability_target: "99.5%"
  response_time_p1: "15 minutes"
  response_time_p2: "4 hours"
  response_time_p3: "24 hours"
  response_time_p4: "5 business days"
  
# Support hours
support:
  business_hours: "Mo-Fr 08:00-18:00 CET"
  extended_hours: "Mo-Fr 06:00-22:00 CET"
  maintenance_window: "Sa 02:00-06:00 CET"
  
# Escalation paths
escalation:
  level_1: "{{ group_Helpdesk }}"
  level_2: "{{ role_IT_Manager }}"
  level_3: "{{ role_CIO }}"
  level_4: "{{ role_CEO }}"
  
# Compliance frameworks
compliance:
  cobit_version: "COBIT 2019"
  itil_version: "ITIL 4"
  iso_27001: true
  
# Service categories
categories:
  - infrastructure
  - application
  - business
  - security
  - support
```

#### 2.2.2 meta-service.yaml (Specific)

```yaml
# Service-Specific Metadata
# Overrides global configuration

service:
  id: "SVC-001"
  name: "Email Service"
  category: "infrastructure"
  criticality: "High"
  status: "Production"
  classification: "Internal"
  revision: 1
  modifydate: "2025-02-19"
  
  # Role references from meta-organisation-roles.yaml
  owner: "role_IT_Manager"
  manager: "role_IT_Manager"
  approver: "role_CIO"
  
  # Service-specific SLA (overrides global)
  sla:
    availability_target: "99.9%"
    response_time_p1: "10 minutes"
    
  # Technology stack
  technology:
    platform: "Microsoft Exchange Online"
    backup: "Veeam Backup for Office 365"
    monitoring: "Zabbix"
    
  # COBIT mapping
  cobit:
    processes:
      - "DSS01 - Manage Operations"
      - "DSS02 - Manage Service Requests"
      - "DSS05 - Manage Security Services"
      
  # ITIL lifecycle
  itil:
    lifecycle_phase: "Service Operation"
    processes:
      - "Incident Management"
      - "Problem Management"
      - "Access Management"
```


#### 2.2.3 meta-global-process.yaml (Global)

```yaml
# Global Process Configuration
# Applies to all processes unless overridden

# Standard escalation
escalation:
  level_1: "{{ role_IT_Manager }}"
  level_2: "{{ role_Risk_Manager }}"
  level_3: "{{ role_CIO }}"
  level_4: "{{ role_CEO }}"
  
# Compliance frameworks
compliance:
  iso_27001: true
  bsi_grundschutz: true
  gdpr: true
  
# Standard KPIs
kpis:
  process_efficiency: "Cycle time reduction"
  quality: "Error rate"
  compliance: "Audit findings"
  
# Process categories
categories:
  - core
  - support
  - management
  
# Standard control points
controls:
  - "Management approval"
  - "Four-eyes principle"
  - "Audit trail"
```

#### 2.2.4 meta-process.yaml (Specific)

```yaml
# Process-Specific Metadata
# Overrides global configuration

process:
  id: "PROC-001"
  name: "Incident Management"
  category: "core"
  criticality: "Critical"
  status: "Active"
  classification: "Internal"
  revision: 2
  modifydate: "2025-02-19"
  
  # Role references from meta-organisation-roles.yaml
  owner: "role_IT_Manager"
  manager: "role_IT_Manager"
  approver: "role_CIO"
  
  # Process-specific SLA
  sla:
    p1_resolution: "4 hours"
    p2_resolution: "24 hours"
    p3_resolution: "5 business days"
    
  # Systems used
  systems:
    - "ServiceNow"
    - "Zabbix"
    - "Slack"
    
  # RACI roles
  raci:
    incident_detection: 
      responsible: "role_System_Administrator"
      accountable: "role_IT_Manager"
      consulted: "role_CISO"
      informed: "role_CIO"
    incident_analysis:
      responsible: "role_Security_Analyst"
      accountable: "role_CISO"
      consulted: "role_IT_Manager"
      informed: "role_CIO"
      
  # Compliance requirements
  compliance:
    frameworks:
      - "ISO 27001:2022 - Clause 5.24"
      - "BSI IT-Grundschutz - DER.2.1"
    sod_rules:
      - "Incident handler cannot approve own escalations"
      - "Security analyst cannot modify audit logs"
      
  # KPIs
  kpis:
    mttr: "Mean Time To Resolve"
    mtbf: "Mean Time Between Failures"
    first_call_resolution: "Percentage"
```


### 2.3 Template-Struktur

#### 2.3.1 Service-Template (service-template.md)

```markdown
# Service: {{ service.name }}

**Dokument-ID:** {{ service.id }}  
**Organisation:** {{ meta-organisation.name }}  
**Service Owner:** {{ service.owner }}  
**Service Manager:** {{ service.manager }}  
**Genehmigt durch:** {{ service.approver }}  
**Revision:** {{ service.revision }}  
**Author:** {{ meta-global.source }}  
**Status:** {{ service.status }}  
**Klassifizierung:** {{ service.classification }}  
**Letzte Aktualisierung:** {{ service.modifydate }}  
**Template Version:** {{ meta-global.version }}

---

## 1. Service-Übersicht

### 1.1 Beschreibung

[Beschreibung des Services]

### 1.2 Service-Kategorie

**Kategorie:** {{ service.category }}  
**Kritikalität:** {{ service.criticality }}

### 1.3 Service-Ziele

- Ziel 1
- Ziel 2
- Ziel 3

## 2. COBIT-Mapping

**COBIT Version:** {{ compliance.cobit_version }}

### 2.1 Relevante Prozesse

{{ service.cobit.processes }}

### 2.2 Controls

[Liste der relevanten Controls]

## 3. ITIL-Mapping

**ITIL Version:** {{ compliance.itil_version }}

### 3.1 Lifecycle-Phase

{{ service.itil.lifecycle_phase }}

### 3.2 ITIL-Prozesse

{{ service.itil.processes }}

## 4. Service-Komponenten

### 4.1 Technologie-Stack

- **Platform:** {{ service.technology.platform }}
- **Backup:** {{ service.technology.backup }}
- **Monitoring:** {{ service.technology.monitoring }}

### 4.2 Schnittstellen

[Beschreibung der Schnittstellen]

## 5. Service Level Agreements (SLAs)

### 5.1 Verfügbarkeit

**Ziel:** {{ service.sla.availability_target }}

### 5.2 Response Times

- **Priority 1:** {{ service.sla.response_time_p1 }}
- **Priority 2:** {{ service.sla.response_time_p2 }}
- **Priority 3:** {{ service.sla.response_time_p3 }}
- **Priority 4:** {{ service.sla.response_time_p4 }}

## 6. Rollen und Verantwortlichkeiten

| Rolle | Name | Kontakt |
|-------|------|---------|
| Service Owner | {{ service.owner }} | {{ service.owner_email }} |
| Service Manager | {{ service.manager }} | {{ service.manager_email }} |
| Approver | {{ service.approver }} | {{ service.approver_email }} |

## 7. Support-Modell

### 7.1 Support-Zeiten

- **Business Hours:** {{ support.business_hours }}
- **Extended Hours:** {{ support.extended_hours }}
- **Maintenance Window:** {{ support.maintenance_window }}

### 7.2 Eskalation

| Level | Rolle | Kontakt |
|-------|-------|---------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} |

## 8. Monitoring und Reporting

[Monitoring-Strategie]

## 9. Kontinuierliche Verbesserung

[Verbesserungsprozess]

## 10. Anhänge

### 10.1 Runbooks

[Links zu Runbooks]

### 10.2 Checklisten

[Links zu Checklisten]
```


#### 2.3.2 Process-Template (process-template.md)

```markdown
# Prozess: {{ process.name }}

**Dokument-ID:** {{ process.id }}  
**Organisation:** {{ meta-organisation.name }}  
**Prozess Owner:** {{ process.owner }}  
**Prozess Manager:** {{ process.manager }}  
**Genehmigt durch:** {{ process.approver }}  
**Revision:** {{ process.revision }}  
**Author:** {{ meta-global.source }}  
**Status:** {{ process.status }}  
**Klassifizierung:** {{ process.classification }}  
**Letzte Aktualisierung:** {{ process.modifydate }}  
**Template Version:** {{ meta-global.version }}

---

## 1. Zweck und Ziel

### 1.1 Zweck

[Zweck des Prozesses]

### 1.2 Ziele

- Ziel 1
- Ziel 2
- Ziel 3

## 2. Geltungsbereich

**Kategorie:** {{ process.category }}  
**Kritikalität:** {{ process.criticality }}

[Beschreibung des Geltungsbereichs]

## 3. Trigger und Eingänge

### 3.1 Trigger

- Trigger 1
- Trigger 2

### 3.2 Eingänge

- Input 1
- Input 2

## 4. Ergebnisse und Outputs

### 4.1 Outputs

- Output 1
- Output 2

### 4.2 Erfolgskriterien

[Erfolgskriterien]

## 5. Rollen und Verantwortlichkeiten (RACI)

### 5.1 RACI-Matrix

| Aktivität | {{ process.raci.incident_detection.responsible }} | {{ process.raci.incident_detection.accountable }} | {{ process.raci.incident_detection.consulted }} | {{ process.raci.incident_detection.informed }} |
|-----------|---------------------------------------------------|---------------------------------------------------|------------------------------------------------|-----------------------------------------------|
| Incident Detection | R | A | C | I |
| Incident Analysis | C | R | A | I |
| Incident Resolution | R | A | C | I |

**Legende:**
- R = Responsible (Durchführung)
- A = Accountable (Verantwortlich)
- C = Consulted (Konsultiert)
- I = Informed (Informiert)

## 6. Ablaufdiagramm (BPMN)

![Process Flow](diagrams/process-flow.bpmn)

### 6.1 Prozessschritte

1. **Schritt 1:** [Beschreibung]
2. **Schritt 2:** [Beschreibung]
3. **Schritt 3:** [Beschreibung]

## 7. Systeme und Tools

### 7.1 Verwendete Systeme

{{ process.systems }}

### 7.2 Schnittstellen

[Beschreibung der Schnittstellen]

## 8. Artefakte

### 8.1 Tickets

[Ticket-Typen und -Workflows]

### 8.2 Logs

[Logging-Anforderungen]

### 8.3 Reports

[Report-Typen]

## 9. SLAs und OLAs

### 9.1 Service Level Agreements

- **P1 Resolution:** {{ process.sla.p1_resolution }}
- **P2 Resolution:** {{ process.sla.p2_resolution }}
- **P3 Resolution:** {{ process.sla.p3_resolution }}

### 9.2 Operational Level Agreements

[OLA-Details]

## 10. KPIs und Metriken

### 10.1 Key Performance Indicators

{{ process.kpis }}

### 10.2 Messung und Reporting

[Messverfahren]

## 11. Kontrollpunkte

### 11.1 Prüfschritte

{{ controls }}

### 11.2 Audit-Anforderungen

[Audit-Details]

## 12. Risiken und Compliance

### 12.1 Compliance-Frameworks

{{ process.compliance.frameworks }}

### 12.2 Segregation of Duties (SoD)

{{ process.compliance.sod_rules }}

### 12.3 Risiken

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|--------|-------------------|------------|------------|
| [Risiko 1] | [Hoch/Mittel/Niedrig] | [Hoch/Mittel/Niedrig] | [Maßnahme] |

## 13. Eskalationen und Ausnahmen

### 13.1 Eskalationspfad

| Level | Rolle | Kontakt |
|-------|-------|---------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} |

### 13.2 Ausnahmen

[Ausnahmenprozess]

## 14. Anhänge

### 14.1 Checklisten

[Links zu Checklisten]

### 14.2 Runbooks

[Links zu Runbooks]

### 14.3 Formulare

[Links zu Formularen]
```


## 3. Komponenten-Design

### 3.1 CLI-Erweiterung (src/cli.py)

#### 3.1.1 Neue Argumente

```python
parser.add_argument(
    '--service', '-s',
    type=str,
    help='Service name for service documentation generation'
)

parser.add_argument(
    '--process', '-p',
    type=str,
    help='Process name for process documentation generation'
)
```

#### 3.1.2 Mutual Exclusivity

```python
# Create mutually exclusive group
doc_type_group = parser.add_mutually_exclusive_group()
doc_type_group.add_argument('--template', '-t', ...)
doc_type_group.add_argument('--service', '-s', ...)
doc_type_group.add_argument('--process', '-p', ...)
```

#### 3.1.3 Validation Logic

```python
def validate_arguments(args: argparse.Namespace) -> Optional[str]:
    """Validate parsed arguments for consistency."""
    
    # Count how many doc types are specified
    doc_types = sum([
        args.template is not None,
        args.service is not None,
        args.process is not None
    ])
    
    if doc_types > 1:
        return "Error: Only one of --template, --service, or --process can be specified"
    
    # Language must be provided with any doc type
    if doc_types > 0 and args.language is None:
        return "Error: --language must be specified"
    
    return None
```

### 3.2 TemplateManager-Erweiterung (src/template_manager.py)

#### 3.2.1 Neue Methoden

```python
def discover_services(self) -> Dict[str, Dict[str, List[Template]]]:
    """
    Discover available service templates.
    
    Returns:
        Dictionary mapping language -> service_name -> templates
    """
    services = {}
    services_root = Path('services')
    
    if not services_root.exists():
        return services
    
    for lang_dir in services_root.iterdir():
        if not lang_dir.is_dir():
            continue
            
        language = lang_dir.name
        services[language] = {}
        
        for service_dir in lang_dir.iterdir():
            if not service_dir.is_dir():
                continue
            if service_dir.name == 'diagrams':
                continue
                
            service_name = service_dir.name
            templates = self._load_templates_from_directory(service_dir)
            
            if templates:
                services[language][service_name] = templates
    
    return services

def discover_processes(self) -> Dict[str, Dict[str, List[Template]]]:
    """
    Discover available process templates.
    
    Returns:
        Dictionary mapping language -> process_name -> templates
    """
    processes = {}
    processes_root = Path('processes')
    
    if not processes_root.exists():
        return processes
    
    for lang_dir in processes_root.iterdir():
        if not lang_dir.is_dir():
            continue
            
        language = lang_dir.name
        processes[language] = {}
        
        for process_dir in lang_dir.iterdir():
            if not process_dir.is_dir():
                continue
            if process_dir.name == 'diagrams':
                continue
                
            process_name = process_dir.name
            templates = self._load_templates_from_directory(process_dir)
            
            if templates:
                processes[language][process_name] = templates
    
    return processes

def get_services(self, language: str, service_name: str) -> List[Template]:
    """Get service templates for specific language and service."""
    services = self.discover_services()
    
    if language not in services:
        raise ValueError(f"No services found for language '{language}'")
    
    if service_name not in services[language]:
        raise ValueError(
            f"Service '{service_name}' not found for language '{language}'"
        )
    
    return services[language][service_name]

def get_processes(self, language: str, process_name: str) -> List[Template]:
    """Get process templates for specific language and process."""
    processes = self.discover_processes()
    
    if language not in processes:
        raise ValueError(f"No processes found for language '{language}'")
    
    if process_name not in processes[language]:
        raise ValueError(
            f"Process '{process_name}' not found for language '{language}'"
        )
    
    return processes[language][process_name]
```


### 3.3 MetaAdapter-Erweiterung (src/meta_adapter.py)

#### 3.3.1 Neue Attribute und Methoden

```python
class MetaAdapter(DataSourceAdapter):
    """Meta data source adapter with service/process support."""
    
    def __init__(self, metadata_config: MetadataConfig, language: str = 'de'):
        """Initialize with metadata configuration."""
        self.metadata = metadata_config
        self.language = language
        self._connected = False
        self._current_service_type = None  # NEW
        self._current_process_type = None  # NEW
        self._service_config = None        # NEW
        self._process_config = None        # NEW
    
    def set_service_type(self, service_name: str, language: str) -> None:
        """
        Set current service type for service-specific metadata.
        
        Args:
            service_name: Name of the service
            language: Language code (de/en)
        """
        self._current_service_type = service_name
        
        # Load service-specific metadata
        service_metadata_path = Path(f'services/{language}/{service_name}/meta-service.yaml')
        if service_metadata_path.exists():
            with open(service_metadata_path, 'r', encoding='utf-8') as f:
                self._service_config = yaml.safe_load(f)
        
        # Load global service config
        global_service_config_path = Path(f'services/{language}/meta-global-service.yaml')
        if global_service_config_path.exists():
            with open(global_service_config_path, 'r', encoding='utf-8') as f:
                self._global_service_config = yaml.safe_load(f)
    
    def set_process_type(self, process_name: str, language: str) -> None:
        """
        Set current process type for process-specific metadata.
        
        Args:
            process_name: Name of the process
            language: Language code (de/en)
        """
        self._current_process_type = process_name
        
        # Load process-specific metadata
        process_metadata_path = Path(f'processes/{language}/{process_name}/meta-process.yaml')
        if process_metadata_path.exists():
            with open(process_metadata_path, 'r', encoding='utf-8') as f:
                self._process_config = yaml.safe_load(f)
        
        # Load global process config
        global_process_config_path = Path(f'processes/{language}/meta-global-process.yaml')
        if global_process_config_path.exists():
            with open(global_process_config_path, 'r', encoding='utf-8') as f:
                self._global_process_config = yaml.safe_load(f)
    
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Retrieve field value with hierarchical resolution.
        
        Resolution order:
        1. Service/Process-specific metadata
        2. Global service/process config
        3. meta-organisation-roles.yaml
        4. meta-organisation.yaml
        5. meta-global.yaml
        
        Args:
            field_path: Dot-separated path to the field
            
        Returns:
            Field value as string, or None if not found
        """
        # Try service-specific metadata first
        if self._service_config and field_path.startswith('service.'):
            value = self._get_nested_value(self._service_config, field_path)
            if value is not None:
                return str(value)
        
        # Try global service config
        if self._global_service_config and field_path.startswith('service.'):
            value = self._get_nested_value(self._global_service_config, field_path)
            if value is not None:
                return str(value)
        
        # Try process-specific metadata
        if self._process_config and field_path.startswith('process.'):
            value = self._get_nested_value(self._process_config, field_path)
            if value is not None:
                return str(value)
        
        # Try global process config
        if self._global_process_config and field_path.startswith('process.'):
            value = self._get_nested_value(self._global_process_config, field_path)
            if value is not None:
                return str(value)
        
        # Fall back to existing metadata resolution
        # (meta-organisation-roles, meta-organisation, meta-global)
        return self._get_existing_metadata_field(field_path)
    
    def _get_nested_value(self, config: dict, field_path: str) -> Optional[Any]:
        """Get nested value from config dictionary."""
        parts = field_path.split('.')
        current = config
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        
        return current
```


### 3.4 ConfigManager-Erweiterung (src/config_manager.py)

#### 3.4.1 Neue Konfigurationsfelder

```python
@dataclass
class Config:
    """Configuration for handbook generator."""
    
    # Existing fields
    netbox_url: Optional[str] = None
    netbox_api_token: Optional[str] = None
    metadata: Optional[MetadataConfig] = None
    
    # NEW: Service and process configuration paths
    service_config_path: str = "services"
    process_config_path: str = "processes"
    
    # NEW: Enable/disable service and process features
    enable_services: bool = True
    enable_processes: bool = True
```

### 3.5 Main Function Integration (src/cli.py)

#### 3.5.1 Service Generation Flow

```python
def main() -> int:
    """Entry point for the handbook generator."""
    
    # ... existing argument parsing ...
    
    # Determine documentation type
    if args.service:
        doc_type = 'service'
        doc_name = args.service
    elif args.process:
        doc_type = 'process'
        doc_name = args.process
    else:
        doc_type = 'template'
        doc_name = args.template
    
    # Get templates based on doc type
    if doc_type == 'service':
        try:
            templates = template_manager.get_services(language, doc_name)
        except ValueError as e:
            logger.log_error(str(e))
            return 1
    elif doc_type == 'process':
        try:
            templates = template_manager.get_processes(language, doc_name)
        except ValueError as e:
            logger.log_error(str(e))
            return 1
    else:
        try:
            templates = template_manager.get_templates(language, doc_name)
        except ValueError as e:
            logger.log_error(str(e))
            return 1
    
    # Set service/process type in meta adapter
    if doc_type == 'service' and 'meta' in data_sources:
        data_sources['meta'].set_service_type(doc_name, language)
    elif doc_type == 'process' and 'meta' in data_sources:
        data_sources['meta'].set_process_type(doc_name, language)
    
    # ... continue with existing processing logic ...
```

## 4. Placeholder-Resolution-Algorithmus

### 4.1 Hierarchische Auflösung

```python
def resolve_placeholder(placeholder: str) -> str:
    """
    Resolve placeholder with hierarchical lookup.
    
    Priority (highest to lowest):
    1. meta-service.yaml / meta-process.yaml
    2. meta-global-service.yaml / meta-global-process.yaml
    3. meta-organisation-roles.yaml
    4. meta-organisation.yaml
    5. meta-global.yaml
    
    Args:
        placeholder: Placeholder string (e.g., "service.owner")
        
    Returns:
        Resolved value or "[TODO]" if not found
    """
    # Level 1: Service/Process-specific metadata
    if placeholder.startswith('service.'):
        value = meta_adapter.get_field(placeholder)
        if value:
            return value
    
    if placeholder.startswith('process.'):
        value = meta_adapter.get_field(placeholder)
        if value:
            return value
    
    # Level 2: Global service/process config
    # (handled internally by meta_adapter.get_field)
    
    # Level 3: Role references
    if placeholder.startswith('role_'):
        value = meta_adapter.get_field(f"roles.{placeholder}")
        if value:
            return value
    
    # Level 4: Organisation metadata
    if placeholder.startswith('meta-organisation.'):
        value = meta_adapter.get_field(placeholder.replace('meta-organisation.', 'organization.'))
        if value:
            return value
    
    # Level 5: Global metadata
    if placeholder.startswith('meta-global.'):
        value = meta_adapter.get_field(placeholder.replace('meta-global.', ''))
        if value:
            return value
    
    # Not found - return TODO marker
    return "[TODO]"
```


### 4.2 Role Reference Resolution

```python
def resolve_role_reference(role_ref: str) -> Tuple[str, str]:
    """
    Resolve role reference to name and email.
    
    Args:
        role_ref: Role reference (e.g., "role_IT_Manager")
        
    Returns:
        Tuple of (name, email)
    """
    # Get role name
    name = meta_adapter.get_field(role_ref)
    if not name:
        name = "[TODO]"
    
    # Get role email
    email_field = f"{role_ref}_email"
    email = meta_adapter.get_field(email_field)
    if not email:
        email = "[TODO]"
    
    return (name, email)
```

## 5. Datenmodell

### 5.1 Service-Datenmodell

```python
@dataclass
class ServiceMetadata:
    """Service metadata structure."""
    
    # Identification
    id: str
    name: str
    category: str
    criticality: str
    
    # Status
    status: str
    classification: str
    revision: int
    modifydate: str
    
    # Ownership
    owner: str          # Role reference
    manager: str        # Role reference
    approver: str       # Role reference
    
    # SLA
    sla: Dict[str, str]
    
    # Technology
    technology: Dict[str, str]
    
    # Framework mapping
    cobit: Dict[str, List[str]]
    itil: Dict[str, Any]
```

### 5.2 Process-Datenmodell

```python
@dataclass
class ProcessMetadata:
    """Process metadata structure."""
    
    # Identification
    id: str
    name: str
    category: str
    criticality: str
    
    # Status
    status: str
    classification: str
    revision: int
    modifydate: str
    
    # Ownership
    owner: str          # Role reference
    manager: str        # Role reference
    approver: str       # Role reference
    
    # SLA/OLA
    sla: Dict[str, str]
    
    # Systems
    systems: List[str]
    
    # RACI
    raci: Dict[str, Dict[str, str]]
    
    # Compliance
    compliance: Dict[str, Any]
    
    # KPIs
    kpis: Dict[str, str]
```

## 6. Fehlerbehandlung

### 6.1 Fehlende Konfigurationsdateien

```python
def load_service_config(service_name: str, language: str) -> Optional[dict]:
    """Load service configuration with error handling."""
    
    config_path = Path(f'services/{language}/{service_name}/meta-service.yaml')
    
    if not config_path.exists():
        logger.log_warning(
            f"Service metadata not found: {config_path}. "
            f"Using global defaults."
        )
        return None
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        logger.log_error(
            f"Failed to parse service metadata: {config_path}. "
            f"Error: {str(e)}"
        )
        return None
    except Exception as e:
        logger.log_error(
            f"Failed to load service metadata: {config_path}. "
            f"Error: {str(e)}"
        )
        return None
```

### 6.2 Fehlende Placeholders

```python
def handle_missing_placeholder(placeholder: str, context: str) -> str:
    """Handle missing placeholder with appropriate fallback."""
    
    logger.log_warning(
        f"Placeholder '{placeholder}' not found in {context}. "
        f"Using [TODO] marker."
    )
    
    return "[TODO]"
```

### 6.3 Ungültige Role-Referenzen

```python
def validate_role_reference(role_ref: str) -> bool:
    """Validate that role reference exists in meta-organisation-roles.yaml."""
    
    value = meta_adapter.get_field(role_ref)
    
    if value is None or value == "[TODO]":
        logger.log_warning(
            f"Role reference '{role_ref}' not found in meta-organisation-roles.yaml. "
            f"Please add this role to the configuration."
        )
        return False
    
    return True
```


## 7. Testing-Strategie

### 7.1 Unit Tests

#### 7.1.1 TemplateManager Tests

```python
def test_discover_services():
    """Test service discovery."""
    manager = TemplateManager(Path('services'))
    services = manager.discover_services()
    
    assert 'de' in services
    assert 'generic-service-template' in services['de']

def test_get_services():
    """Test getting specific service templates."""
    manager = TemplateManager(Path('services'))
    templates = manager.get_services('de', 'generic-service-template')
    
    assert len(templates) > 0
    assert templates[0].path.name == 'service-template.md'

def test_discover_processes():
    """Test process discovery."""
    manager = TemplateManager(Path('processes'))
    processes = manager.discover_processes()
    
    assert 'de' in processes
    assert 'generic-process-template' in processes['de']
```

#### 7.1.2 MetaAdapter Tests

```python
def test_set_service_type():
    """Test setting service type."""
    adapter = MetaAdapter(metadata_config)
    adapter.set_service_type('generic-service-template', 'de')
    
    assert adapter._current_service_type == 'generic-service-template'
    assert adapter._service_config is not None

def test_service_placeholder_resolution():
    """Test service placeholder resolution."""
    adapter = MetaAdapter(metadata_config)
    adapter.set_service_type('generic-service-template', 'de')
    
    value = adapter.get_field('service.name')
    assert value is not None
    assert value != "[TODO]"

def test_hierarchical_resolution():
    """Test hierarchical placeholder resolution."""
    adapter = MetaAdapter(metadata_config)
    adapter.set_service_type('generic-service-template', 'de')
    
    # Should resolve from meta-service.yaml
    service_value = adapter.get_field('service.id')
    assert service_value == 'SVC-001'
    
    # Should resolve from meta-organisation.yaml
    org_value = adapter.get_field('organization.name')
    assert org_value == 'AdminsEnd Ltd.'
    
    # Should resolve from meta-organisation-roles.yaml
    role_value = adapter.get_field('role_IT_Manager')
    assert role_value is not None
```

### 7.2 Integration Tests

```python
def test_service_generation_end_to_end():
    """Test complete service generation workflow."""
    # Setup
    config = load_config('config.yaml')
    template_manager = TemplateManager(Path('services'))
    meta_adapter = MetaAdapter(config.metadata)
    
    # Get service templates
    templates = template_manager.get_services('de', 'generic-service-template')
    assert len(templates) > 0
    
    # Set service type
    meta_adapter.set_service_type('generic-service-template', 'de')
    
    # Process template
    processor = PlaceholderProcessor({'meta': meta_adapter})
    result = processor.process_template(templates[0].read_content(), templates[0].path.name)
    
    # Verify placeholders resolved
    assert '[TODO]' not in result.content or result.warnings
    assert '{{ service.name }}' not in result.content
    assert '{{ meta-organisation.name }}' not in result.content

def test_process_generation_end_to_end():
    """Test complete process generation workflow."""
    # Similar to service test but for processes
    pass
```

### 7.3 CLI Tests

```python
def test_cli_service_option():
    """Test CLI with --service option."""
    result = subprocess.run(
        ['python', '-m', 'src.cli', '--language', 'de', '--service', 'generic-service-template', '--test'],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert 'Service' in result.stdout

def test_cli_mutual_exclusivity():
    """Test that --template, --service, --process are mutually exclusive."""
    result = subprocess.run(
        ['python', '-m', 'src.cli', '--template', 'isms', '--service', 'email-service', '--test'],
        capture_output=True,
        text=True
    )
    
    assert result.returncode != 0
    assert 'mutually exclusive' in result.stderr.lower()
```


## 8. Migration und Backward Compatibility

### 8.1 Bestehende Funktionalität

- Alle bestehenden `--template` Optionen bleiben unverändert
- Bestehende Metadata-Konfigurationen werden nicht modifiziert
- Bestehende Templates funktionieren weiterhin ohne Änderungen

### 8.2 Neue Verzeichnisse

- `services/` und `processes/` Verzeichnisse sind optional
- System funktioniert auch ohne diese Verzeichnisse
- Warnung wird ausgegeben, wenn Verzeichnisse fehlen aber `--service` oder `--process` verwendet wird

### 8.3 Konfigurationsdateien

- Neue YAML-Konfigurationen sind optional
- System verwendet Fallback-Werte wenn Konfigurationen fehlen
- Bestehende `meta-*.yaml` Dateien werden erweitert, nicht ersetzt

## 9. Deployment und Rollout

### 9.1 Phase 1: Deutsche Templates

1. Erstelle Verzeichnisstruktur für Services und Prozesse
2. Implementiere `meta-global-service.yaml` und `meta-global-process.yaml`
3. Erstelle generische Templates (Deutsch)
4. Teste mit Beispiel-Service und -Prozess

### 9.2 Phase 2: CLI-Integration

1. Erweitere CLI um `--service` und `--process` Optionen
2. Implementiere Mutual Exclusivity
3. Erweitere TemplateManager
4. Teste CLI-Integration

### 9.3 Phase 3: MetaAdapter-Erweiterung

1. Implementiere `set_service_type()` und `set_process_type()`
2. Erweitere `get_field()` für hierarchische Auflösung
3. Teste Placeholder-Resolution
4. Validiere Role-Referenzen

### 9.4 Phase 4: Englische Templates

1. Übersetze deutsche Templates ins Englische
2. Erstelle englische Konfigurationsdateien
3. Teste bilinguale Konsistenz
4. Validiere Terminologie

### 9.5 Phase 5: Dokumentation und Beispiele

1. Aktualisiere README mit neuen Features
2. Erstelle Beispiel-Services und -Prozesse
3. Dokumentiere Placeholder-Struktur
4. Erstelle Best-Practice-Guide

## 10. Performance-Überlegungen

### 10.1 Konfigurationsdatei-Caching

```python
class MetaAdapter:
    """Meta adapter with configuration caching."""
    
    def __init__(self, metadata_config: MetadataConfig, language: str = 'de'):
        self._config_cache = {}  # Cache for loaded YAML files
    
    def _load_yaml_cached(self, path: Path) -> Optional[dict]:
        """Load YAML file with caching."""
        cache_key = str(path)
        
        if cache_key in self._config_cache:
            return self._config_cache[cache_key]
        
        if not path.exists():
            return None
        
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            self._config_cache[cache_key] = config
            return config
```

### 10.2 Template Discovery Optimization

- Discovery-Ergebnisse werden gecacht
- Nur bei Bedarf neu geladen
- Vermeidung redundanter Dateisystem-Zugriffe

## 11. Sicherheitsüberlegungen

### 11.1 YAML-Injection-Schutz

```python
def load_yaml_safe(path: Path) -> dict:
    """Load YAML file with security checks."""
    
    # Use safe_load to prevent code execution
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
```

### 11.2 Path Traversal Protection

```python
def validate_path(base_path: Path, requested_path: str) -> bool:
    """Validate that requested path is within base path."""
    
    full_path = (base_path / requested_path).resolve()
    return full_path.is_relative_to(base_path.resolve())
```

### 11.3 Sensitive Data Handling

- Keine Passwörter oder Secrets in YAML-Dateien
- Kontaktdaten können optional sein
- Warnung bei fehlenden Daten statt Fehler

## 12. Monitoring und Logging

### 12.1 Logging-Erweiterungen

```python
# Service generation logging
logger.log_info(f"Generating service documentation: {service_name}")
logger.log_verbose(f"Loaded service metadata from: {metadata_path}")
logger.log_warning(f"Missing service configuration: {config_path}")

# Process generation logging
logger.log_info(f"Generating process documentation: {process_name}")
logger.log_verbose(f"Loaded process metadata from: {metadata_path}")
logger.log_warning(f"Missing BPMN diagram: {diagram_path}")

# Placeholder resolution logging
logger.log_replacement(f"Resolved {placeholder} -> {value}")
logger.log_warning(f"Placeholder not found: {placeholder}")
```

### 12.2 Metriken

- Anzahl generierter Services
- Anzahl generierter Prozesse
- Anzahl aufgelöster Placeholders
- Anzahl fehlender Placeholders
- Verarbeitungszeit pro Dokumenttyp

## 13. Wartung und Support

### 13.1 Versionierung

- Template-Version in jedem Dokument
- Konfigurationsdatei-Versionierung
- Changelog für Template-Änderungen

### 13.2 Dokumentation

- Inline-Kommentare in Templates
- Beispiel-Konfigurationen
- Troubleshooting-Guide
- FAQ-Sektion

### 13.3 Support-Prozess

- Issue-Templates für Service/Process-Probleme
- Validierungs-Tools für Konfigurationsdateien
- Automatische Konsistenz-Checks

## 14. Zukünftige Erweiterungen

### 14.1 Mögliche Features

- Automatische BPMN-Diagramm-Generierung
- Service-Katalog-Export
- Prozess-Metriken-Dashboard
- Integration mit CMDB-Systemen
- Automatische Compliance-Validierung
- Service-Dependency-Mapping

### 14.2 Nicht im Scope

- Automatische COBIT/ITIL-Mapping-Validierung
- Integration mit externen Service-Management-Tools
- Automatische KPI-Berechnung
- Workflow-Automation
- Approval-Workflows
