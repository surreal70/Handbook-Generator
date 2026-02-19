# Placeholder Structure and Hierarchy

## Überblick

Dieses Dokument beschreibt die Placeholder-Struktur und hierarchische Auflösung im Handbook Generator für Handbooks, Services und Prozesse.

## Inhaltsverzeichnis

- [Placeholder-Syntax](#placeholder-syntax)
- [Hierarchische Auflösung](#hierarchische-auflösung)
- [Handbook-Placeholders](#handbook-placeholders)
- [Service-Placeholders](#service-placeholders)
- [Process-Placeholders](#process-placeholders)
- [Rollen-Referenzen](#rollen-referenzen)
- [Fallback-Mechanismus](#fallback-mechanismus)
- [Beispiele](#beispiele)

## Placeholder-Syntax

### Grundlegende Syntax

Placeholders verwenden die Mustache-Syntax mit doppelten geschweiften Klammern:

```markdown
{{ quelle.feld }}
```

**Komponenten:**
- `quelle`: Datenquelle oder Konfigurationsebene (z.B. `service`, `process`, `meta-organisation`)
- `feld`: Feldname oder Pfad mit Punkt-Notation (z.B. `name`, `sla.availability_target`)

### Regeln

1. **Whitespace**: Leerzeichen vor/nach dem Placeholder sind erlaubt
   ```markdown
   {{ service.name }}
   {{service.name}}
   ```

2. **Punkt-Notation**: Verschachtelte Felder mit Punkten trennen
   ```markdown
   {{ service.sla.availability_target }}
   {{ process.raci.incident_detection.responsible }}
   ```

3. **Keine Berechnungen**: Placeholders sind reine Wert-Ersetzungen
   ```markdown
   ✅ {{ service.name }}
   ❌ {{ service.name | uppercase }}
   ```

## Hierarchische Auflösung

### Auflösungs-Priorität

Placeholders werden in hierarchischer Reihenfolge aufgelöst. Die erste gefundene Definition wird verwendet.

#### Für Handbooks

1. `meta-handbook.yaml` (handbook-spezifisch)
2. `meta-organisation-roles.yaml` (Rollen)
3. `meta-organisation.yaml` (Organisation)
4. `meta-global.yaml` (Generator)

#### Für Services

1. `meta-service.yaml` (service-spezifisch)
2. `meta-global-service.yaml` (global für alle Services)
3. `meta-organisation-roles.yaml` (Rollen)
4. `meta-organisation.yaml` (Organisation)
5. `meta-global.yaml` (Generator)

#### Für Prozesse

1. `meta-process.yaml` (prozess-spezifisch)
2. `meta-global-process.yaml` (global für alle Prozesse)
3. `meta-organisation-roles.yaml` (Rollen)
4. `meta-organisation.yaml` (Organisation)
5. `meta-global.yaml` (Generator)

### Auflösungs-Algorithmus

```python
def resolve_placeholder(placeholder: str) -> str:
    """
    Resolve placeholder with hierarchical lookup.
    
    Returns resolved value or "[TODO]" if not found.
    """
    # Level 1: Specific metadata (service/process/handbook)
    value = lookup_specific_metadata(placeholder)
    if value:
        return value
    
    # Level 2: Global metadata (service/process)
    value = lookup_global_metadata(placeholder)
    if value:
        return value
    
    # Level 3: Role references
    value = lookup_roles(placeholder)
    if value:
        return value
    
    # Level 4: Organisation metadata
    value = lookup_organisation(placeholder)
    if value:
        return value
    
    # Level 5: Global generator metadata
    value = lookup_global(placeholder)
    if value:
        return value
    
    # Not found - return TODO marker
    return "[TODO]"
```

## Handbook-Placeholders

### Verfügbare Quellen

#### meta-global.yaml

```yaml
source: "Handbook Generator v0.0.17"
version: "0.0.17"
```

**Placeholders:**
- `{{ meta-global.source }}`
- `{{ meta-global.version }}`

#### meta-organisation.yaml

```yaml
organization:
  name: "Example Corp"
  address: "123 Main Street, 12345 City"
  phone: "+49 123 456789"
  web: "https://example.com"
  revision: 1
```

**Placeholders:**
- `{{ meta-organisation.name }}`
- `{{ meta-organisation.address }}`
- `{{ meta-organisation.phone }}`
- `{{ meta-organisation.web }}`
- `{{ meta-organisation.revision }}`

#### meta-organisation-roles.yaml

```yaml
roles:
  role_CEO: "John Doe"
  role_CEO_email: "john.doe@example.com"
  role_CIO: "Jane Smith"
  role_CIO_email: "jane.smith@example.com"
  role_CISO: "Bob Johnson"
  role_CISO_email: "bob.johnson@example.com"
```

**Placeholders:**
- `{{ role_CEO }}`
- `{{ role_CEO_email }}`
- `{{ role_CIO }}`
- `{{ role_CIO_email }}`
- `{{ role_CISO }}`
- `{{ role_CISO_email }}`

## Service-Placeholders

### Verfügbare Quellen

#### meta-global-service.yaml

```yaml
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
```

**Placeholders:**
- `{{ sla.availability_target }}`
- `{{ sla.response_time_p1 }}`
- `{{ support.business_hours }}`
- `{{ support.maintenance_window }}`
- `{{ escalation.level_1 }}`
- `{{ compliance.cobit_version }}`
- `{{ compliance.itil_version }}`

#### meta-service.yaml

```yaml
service:
  id: "SVC-001"
  name: "Email Service"
  category: "infrastructure"
  criticality: "High"
  status: "Production"
  classification: "Internal"
  revision: 1
  modifydate: "2025-02-19"
  
  owner: "role_IT_Manager"
  manager: "role_IT_Manager"
  approver: "role_CIO"
  
  sla:
    availability_target: "99.9%"
    response_time_p1: "10 minutes"
    
  technology:
    platform: "Microsoft Exchange Online"
    backup: "Veeam Backup for Office 365"
    monitoring: "Zabbix"
    
  cobit:
    processes:
      - "DSS01 - Manage Operations"
      - "DSS02 - Manage Service Requests"
      
  itil:
    lifecycle_phase: "Service Operation"
    processes:
      - "Incident Management"
      - "Problem Management"
```

**Placeholders:**
- `{{ service.id }}`
- `{{ service.name }}`
- `{{ service.category }}`
- `{{ service.criticality }}`
- `{{ service.status }}`
- `{{ service.owner }}`
- `{{ service.sla.availability_target }}`
- `{{ service.technology.platform }}`
- `{{ service.cobit.processes }}`
- `{{ service.itil.lifecycle_phase }}`

## Process-Placeholders

### Verfügbare Quellen

#### meta-global-process.yaml

```yaml
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
  
# Standard control points
controls:
  - "Management approval"
  - "Four-eyes principle"
  - "Audit trail"
```

**Placeholders:**
- `{{ escalation.level_1 }}`
- `{{ compliance.iso_27001 }}`
- `{{ kpis.process_efficiency }}`
- `{{ controls }}`

#### meta-process.yaml

```yaml
process:
  id: "PROC-001"
  name: "Incident Management"
  category: "core"
  criticality: "Critical"
  status: "Active"
  classification: "Internal"
  revision: 2
  modifydate: "2025-02-19"
  
  owner: "role_IT_Manager"
  manager: "role_IT_Manager"
  approver: "role_CIO"
  
  sla:
    p1_resolution: "4 hours"
    p2_resolution: "24 hours"
    p3_resolution: "5 business days"
    
  systems:
    - "ServiceNow"
    - "Zabbix"
    - "Slack"
    
  raci:
    incident_detection:
      responsible: "role_System_Administrator"
      accountable: "role_IT_Manager"
      consulted: "role_CISO"
      informed: "role_CIO"
      
  compliance:
    frameworks:
      - "ISO 27001:2022 - Clause 5.24"
      - "BSI IT-Grundschutz - DER.2.1"
    sod_rules:
      - "Incident handler cannot approve own escalations"
      
  kpis:
    mttr: "Mean Time To Resolve"
    mtbf: "Mean Time Between Failures"
```

**Placeholders:**
- `{{ process.id }}`
- `{{ process.name }}`
- `{{ process.category }}`
- `{{ process.criticality }}`
- `{{ process.status }}`
- `{{ process.owner }}`
- `{{ process.sla.p1_resolution }}`
- `{{ process.systems }}`
- `{{ process.raci.incident_detection.responsible }}`
- `{{ process.compliance.frameworks }}`
- `{{ process.compliance.sod_rules }}`
- `{{ process.kpis.mttr }}`

## Rollen-Referenzen

### Konzept

Rollen-Referenzen ermöglichen die Wiederverwendung von Rollen-Definitionen:

```yaml
# meta-organisation-roles.yaml
roles:
  role_IT_Manager: "Max Mustermann"
  role_IT_Manager_email: "max.mustermann@example.com"
```

```yaml
# meta-service.yaml
service:
  owner: "role_IT_Manager"  # Referenz auf Rolle
```

### Auflösung

Rollen-Referenzen werden in zwei Schritten aufgelöst:

1. **Referenz auflösen**: `service.owner` → `"role_IT_Manager"`
2. **Rolle auflösen**: `role_IT_Manager` → `"Max Mustermann"`

Im Template:

```markdown
**Service Owner:** {{ service.owner }}
<!-- Wird zu: Service Owner: Max Mustermann -->

**Kontakt:** {{ role_IT_Manager_email }}
<!-- Wird zu: Kontakt: max.mustermann@example.com -->
```

### Vorteile

1. **Zentrale Verwaltung**: Rollen an einem Ort definiert
2. **Konsistenz**: Gleiche Rolle in allen Templates
3. **Wartbarkeit**: Änderungen nur an einer Stelle
4. **Wiederverwendung**: Rollen in Services, Prozessen, Handbooks

## Fallback-Mechanismus

### TODO-Marker

Wenn ein Placeholder nicht aufgelöst werden kann, wird `[TODO]` eingefügt:

```markdown
**Service Owner:** {{ service.owner }}
<!-- Wenn nicht definiert: Service Owner: [TODO] -->
```

### Debugging

Bei Verwendung von `--verbose` werden nicht aufgelöste Placeholders geloggt:

```bash
./handbook-generator -l de --service my-service --test --verbose
```

Output:

```
WARNING: Placeholder 'service.owner' not found in any configuration
WARNING: Using fallback value '[TODO]' for 'service.owner'
```

### Best Practices

1. **Vollständige Konfiguration**: Definieren Sie alle benötigten Felder
2. **Validierung**: Prüfen Sie generierte Dokumente auf `[TODO]`
3. **Globale Defaults**: Definieren Sie Defaults in globalen Konfigurationen
4. **Dokumentation**: Dokumentieren Sie erforderliche Felder

## Beispiele

### Beispiel 1: Service mit Hierarchie

**Konfiguration:**

```yaml
# meta-global-service.yaml
sla:
  availability_target: "99.5%"
  response_time_p1: "15 minutes"

# meta-service.yaml
service:
  name: "Email Service"
  sla:
    availability_target: "99.9%"  # Überschreibt global
```

**Template:**

```markdown
# Service: {{ service.name }}

**Verfügbarkeit:** {{ service.sla.availability_target }}
**Response Time P1:** {{ service.sla.response_time_p1 }}
```

**Ergebnis:**

```markdown
# Service: Email Service

**Verfügbarkeit:** 99.9%  <!-- Aus meta-service.yaml -->
**Response Time P1:** 15 minutes  <!-- Aus meta-global-service.yaml -->
```

### Beispiel 2: Prozess mit RACI

**Konfiguration:**

```yaml
# meta-organisation-roles.yaml
roles:
  role_IT_Manager: "Max Mustermann"
  role_CISO: "Dr. Maria Schmidt"

# meta-process.yaml
process:
  name: "Incident Management"
  raci:
    incident_detection:
      responsible: "role_System_Administrator"
      accountable: "role_IT_Manager"
      consulted: "role_CISO"
```

**Template:**

```markdown
# Prozess: {{ process.name }}

## RACI-Matrix

| Aktivität | Responsible | Accountable | Consulted |
|-----------|-------------|-------------|-----------|
| Incident Detection | {{ process.raci.incident_detection.responsible }} | {{ process.raci.incident_detection.accountable }} | {{ process.raci.incident_detection.consulted }} |
```

**Ergebnis:**

```markdown
# Prozess: Incident Management

## RACI-Matrix

| Aktivität | Responsible | Accountable | Consulted |
|-----------|-------------|-------------|-----------|
| Incident Detection | [TODO] | Max Mustermann | Dr. Maria Schmidt |
```

### Beispiel 3: Verschachtelte Referenzen

**Konfiguration:**

```yaml
# meta-organisation-roles.yaml
roles:
  role_IT_Manager: "Max Mustermann"
  role_IT_Manager_email: "max.mustermann@example.com"

# meta-global-service.yaml
escalation:
  level_2: "{{ role_IT_Manager }}"

# meta-service.yaml
service:
  name: "Email Service"
```

**Template:**

```markdown
# Service: {{ service.name }}

## Eskalation

**Level 2:** {{ escalation.level_2 }} ({{ role_IT_Manager_email }})
```

**Ergebnis:**

```markdown
# Service: Email Service

## Eskalation

**Level 2:** Max Mustermann (max.mustermann@example.com)
```

## Weiterführende Dokumentation

- **[SERVICE_DOCUMENTATION_GUIDE.md](SERVICE_DOCUMENTATION_GUIDE.md)** - Service-Dokumentation
- **[PROCESS_DOCUMENTATION_GUIDE.md](PROCESS_DOCUMENTATION_GUIDE.md)** - Prozess-Dokumentation
- **[CONFIGURATION_REFERENCE.md](CONFIGURATION_REFERENCE.md)** - Konfigurationsreferenz
- **[METADATA_REFERENCE.md](METADATA_REFERENCE.md)** - Metadata-Referenz
- **[PLACEHOLDER_REFERENCE.md](PLACEHOLDER_REFERENCE.md)** - Placeholder-Syntax

---

**Version:** 0.0.17  
**Letzte Aktualisierung:** 2025-02-19  
**Autor:** Andreas Huemmer [andreas.huemmer@adminsend.de]
