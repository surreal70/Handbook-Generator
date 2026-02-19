# Service Documentation Guide

## Überblick

Dieser Leitfaden beschreibt, wie Sie IT-Services mit dem Handbook Generator strukturiert nach COBIT- und ITIL-Standards dokumentieren können.

## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Schnellstart](#schnellstart)
- [Service-Template-Struktur](#service-template-struktur)
- [Metadata-Konfiguration](#metadata-konfiguration)
- [Placeholder-Verwendung](#placeholder-verwendung)
- [COBIT-Integration](#cobit-integration)
- [ITIL-Integration](#itil-integration)
- [Eigene Services erstellen](#eigene-services-erstellen)
- [Best Practices](#best-practices)
- [Beispiele](#beispiele)

## Einführung

Die Service-Dokumentation ermöglicht die strukturierte Beschreibung von IT-Services mit:

- **COBIT-Konformität**: Mapping zu COBIT-Prozessen und Controls
- **ITIL-Konformität**: Zuordnung zu ITIL Service Lifecycle Phasen
- **SLA-Management**: Strukturierte Definition von Service Level Agreements
- **Rollen und Verantwortlichkeiten**: Integration mit Organisationsrollen
- **Support-Modell**: Eskalationswege und Support-Zeiten
- **Monitoring**: KPIs und Reporting-Anforderungen

## Schnellstart

### Service-Dokumentation generieren

```bash
# Generisches Service-Template (Deutsch)
./handbook-generator --language de --service generic-service-template --test

# Generisches Service-Template (Englisch)
./handbook-generator --language en --service generic-service-template --test

# Mit allen Ausgabeformaten
./handbook-generator -l de --service generic-service-template -o all --test --separate-files --pdf-toc
```

### Ausgabe

Die generierten Service-Dokumente werden in folgendem Verzeichnis gespeichert:

```
test-output/
├── de/
│   └── generic-service-template/
│       ├── markdown/
│       │   └── service-template.md
│       ├── pdf/
│       │   └── service_documentation.pdf
│       └── html/
│           └── index.html
└── en/
    └── [identische Struktur]
```

## Service-Template-Struktur

### Verzeichnisstruktur

```
services/
├── de/
│   ├── meta-global-service.yaml         # Globale Service-Konfiguration
│   └── generic-service-template/
│       ├── meta-service.yaml            # Service-spezifische Konfiguration
│       └── service-template.md          # Service-Template
└── en/
    ├── meta-global-service.yaml
    └── generic-service-template/
        ├── meta-service.yaml
        └── service-template.md
```

### Template-Abschnitte

Ein Service-Template enthält folgende Hauptabschnitte:

1. **Dokumenten-Header**: Metadaten (ID, Owner, Status, Revision)
2. **Service-Übersicht**: Name, Beschreibung, Kategorie, Kritikalität
3. **Service-Ziele**: Geschäftsziele und Nutzen
4. **COBIT-Mapping**: Relevante COBIT-Prozesse und Controls
5. **ITIL-Mapping**: Service Lifecycle Phasen und Prozesse
6. **Service-Komponenten**: Technologie-Stack und Architektur
7. **Schnittstellen**: Abhängigkeiten zu anderen Services
8. **SLAs**: Service Level Agreements (Verfügbarkeit, Response Times)
9. **OLAs**: Operational Level Agreements
10. **Rollen und Verantwortlichkeiten**: Service Owner, Manager, Team
11. **Betriebszeiten**: Support-Zeiten und Wartungsfenster
12. **Support-Modell**: Eskalationswege und Kontakte
13. **Monitoring**: KPIs, Metriken, Reporting
14. **Kontinuierliche Verbesserung**: Verbesserungsprozesse
15. **Anhänge**: Runbooks, Checklisten, Dokumentation

## Metadata-Konfiguration

### Globale Service-Konfiguration (meta-global-service.yaml)

Die globale Konfiguration definiert Standard-Werte für alle Services:

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

### Service-spezifische Konfiguration (meta-service.yaml)

Die service-spezifische Konfiguration überschreibt globale Werte:

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

## Placeholder-Verwendung

### Hierarchische Auflösung

Placeholders werden in folgender Priorität aufgelöst (höchste zuerst):

1. `meta-service.yaml` (service-spezifisch)
2. `meta-global-service.yaml` (global für alle Services)
3. `meta-organisation-roles.yaml` (Rollen und Kontakte)
4. `meta-organisation.yaml` (Organisation)
5. `meta-global.yaml` (Generator-Informationen)

### Beispiel-Placeholders

```markdown
# Service: {{ service.name }}

**Dokument-ID:** {{ service.id }}
**Organisation:** {{ meta-organisation.name }}
**Service Owner:** {{ service.owner }}
**Service Manager:** {{ role_IT_Manager }}
**Genehmigt durch:** {{ role_CIO }}
**Status:** {{ service.status }}
**Letzte Aktualisierung:** {{ service.modifydate }}
**Template Version:** {{ meta-global.version }}

## Service Level Agreements

**Verfügbarkeit:** {{ service.sla.availability_target }}
**Response Time P1:** {{ service.sla.response_time_p1 }}
**Response Time P2:** {{ service.sla.response_time_p2 }}

## Support-Zeiten

**Business Hours:** {{ support.business_hours }}
**Extended Hours:** {{ support.extended_hours }}
**Maintenance Window:** {{ support.maintenance_window }}

## Eskalation

| Level | Rolle | Kontakt |
|-------|-------|---------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} |
```

### Rollen-Referenzen

Rollen werden aus `meta-organisation-roles.yaml` aufgelöst:

```yaml
# meta-organisation-roles.yaml
roles:
  role_IT_Manager: "Max Mustermann"
  role_IT_Manager_email: "max.mustermann@example.com"
  role_CIO: "Dr. Maria Schmidt"
  role_CIO_email: "maria.schmidt@example.com"
```

Im Template:

```markdown
**Service Manager:** {{ role_IT_Manager }} ({{ role_IT_Manager_email }})
**Genehmigt durch:** {{ role_CIO }} ({{ role_CIO_email }})
```

## COBIT-Integration

### COBIT-Prozess-Mapping

Services können zu COBIT-Prozessen gemappt werden:

```yaml
# meta-service.yaml
service:
  cobit:
    processes:
      - "DSS01 - Manage Operations"
      - "DSS02 - Manage Service Requests"
      - "DSS03 - Manage Problems"
      - "DSS05 - Manage Security Services"
    controls:
      - "DSS01.01 - Perform operational procedures"
      - "DSS02.01 - Define service requests"
      - "DSS05.01 - Protect against malware"
```

Im Template:

```markdown
## COBIT-Mapping

**COBIT Version:** {{ compliance.cobit_version }}

### Relevante Prozesse

{{ service.cobit.processes }}

### Controls

{{ service.cobit.controls }}
```

### COBIT 2019 Prozesse

Häufig verwendete COBIT-Prozesse für Services:

- **DSS01**: Manage Operations
- **DSS02**: Manage Service Requests and Incidents
- **DSS03**: Manage Problems
- **DSS04**: Manage Continuity
- **DSS05**: Manage Security Services
- **DSS06**: Manage Business Process Controls

## ITIL-Integration

### ITIL Service Lifecycle

Services werden ITIL Lifecycle-Phasen zugeordnet:

```yaml
# meta-service.yaml
service:
  itil:
    lifecycle_phase: "Service Operation"
    processes:
      - "Incident Management"
      - "Problem Management"
      - "Change Management"
      - "Access Management"
      - "Service Request Management"
```

Im Template:

```markdown
## ITIL-Mapping

**ITIL Version:** {{ compliance.itil_version }}

### Lifecycle-Phase

{{ service.itil.lifecycle_phase }}

### ITIL-Prozesse

{{ service.itil.processes }}
```

### ITIL 4 Lifecycle-Phasen

- **Service Strategy**: Strategische Planung
- **Service Design**: Service-Design und Architektur
- **Service Transition**: Überführung in den Betrieb
- **Service Operation**: Laufender Betrieb
- **Continual Service Improvement**: Kontinuierliche Verbesserung

## Eigene Services erstellen

### Schritt 1: Service-Verzeichnis erstellen

```bash
# Für deutschen Service
mkdir -p services/de/email-service

# Für englischen Service
mkdir -p services/en/email-service
```

### Schritt 2: Service-Konfiguration erstellen

Erstellen Sie `services/de/email-service/meta-service.yaml`:

```yaml
service:
  id: "SVC-EMAIL-001"
  name: "E-Mail Service"
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
    response_time_p2: "2 hours"
    
  technology:
    platform: "Microsoft Exchange Online"
    backup: "Veeam Backup for Office 365"
    monitoring: "Zabbix"
    antispam: "Mimecast"
    
  cobit:
    processes:
      - "DSS01 - Manage Operations"
      - "DSS02 - Manage Service Requests"
      - "DSS05 - Manage Security Services"
      
  itil:
    lifecycle_phase: "Service Operation"
    processes:
      - "Incident Management"
      - "Problem Management"
      - "Access Management"
```

### Schritt 3: Service-Template erstellen

Kopieren Sie das generische Template und passen Sie es an:

```bash
cp services/de/generic-service-template/service-template.md \
   services/de/email-service/email-service.md
```

Passen Sie das Template an Ihre Bedürfnisse an.

### Schritt 4: Service generieren

```bash
./handbook-generator --language de --service email-service --test
```

## Best Practices

### 1. Konsistente Namensgebung

- Service-IDs: `SVC-<KATEGORIE>-<NUMMER>` (z.B. `SVC-INFRA-001`)
- Verzeichnisnamen: Kleinbuchstaben mit Bindestrichen (z.B. `email-service`)
- Template-Dateien: `<service-name>.md` (z.B. `email-service.md`)

### 2. Vollständige Metadata

Füllen Sie alle relevanten Felder in `meta-service.yaml` aus:

- ✅ Service-ID, Name, Kategorie
- ✅ Owner, Manager, Approver (mit Rollen-Referenzen)
- ✅ SLA-Werte (Verfügbarkeit, Response Times)
- ✅ Technologie-Stack
- ✅ COBIT- und ITIL-Mappings

### 3. Rollen-Referenzen verwenden

Verwenden Sie immer Rollen-Referenzen statt direkter Namen:

```yaml
# ✅ Gut: Rollen-Referenz
owner: "role_IT_Manager"

# ❌ Schlecht: Direkter Name
owner: "Max Mustermann"
```

### 4. SLA-Hierarchie nutzen

Definieren Sie Standard-SLAs in `meta-global-service.yaml` und überschreiben Sie nur bei Bedarf:

```yaml
# meta-global-service.yaml (Standard)
sla:
  availability_target: "99.5%"
  response_time_p1: "15 minutes"

# meta-service.yaml (Überschreibung für kritischen Service)
service:
  sla:
    availability_target: "99.9%"
    response_time_p1: "10 minutes"
```

### 5. Dokumentation aktuell halten

- Aktualisieren Sie `modifydate` bei Änderungen
- Erhöhen Sie `revision` bei größeren Änderungen
- Dokumentieren Sie Änderungen in einer Version History

### 6. Bilinguale Konsistenz

Halten Sie deutsche und englische Versionen synchron:

- Identische Struktur in DE und EN
- Gleiche Service-IDs
- Konsistente Metadata-Felder

## Beispiele

### Beispiel 1: Infrastructure Service (E-Mail)

```yaml
# services/de/email-service/meta-service.yaml
service:
  id: "SVC-INFRA-001"
  name: "E-Mail Service"
  category: "infrastructure"
  criticality: "High"
  
  sla:
    availability_target: "99.9%"
    response_time_p1: "10 minutes"
    
  technology:
    platform: "Microsoft Exchange Online"
    backup: "Veeam Backup for Office 365"
    
  cobit:
    processes:
      - "DSS01 - Manage Operations"
      - "DSS05 - Manage Security Services"
      
  itil:
    lifecycle_phase: "Service Operation"
```

### Beispiel 2: Application Service (ERP)

```yaml
# services/de/erp-service/meta-service.yaml
service:
  id: "SVC-APP-001"
  name: "ERP System"
  category: "application"
  criticality: "Critical"
  
  sla:
    availability_target: "99.95%"
    response_time_p1: "5 minutes"
    
  technology:
    platform: "SAP S/4HANA"
    database: "SAP HANA"
    backup: "SAP HANA Backup"
    
  cobit:
    processes:
      - "DSS01 - Manage Operations"
      - "DSS02 - Manage Service Requests"
      - "DSS04 - Manage Continuity"
      
  itil:
    lifecycle_phase: "Service Operation"
```

### Beispiel 3: Security Service (Firewall)

```yaml
# services/de/firewall-service/meta-service.yaml
service:
  id: "SVC-SEC-001"
  name: "Firewall Service"
  category: "security"
  criticality: "Critical"
  
  sla:
    availability_target: "99.99%"
    response_time_p1: "5 minutes"
    
  technology:
    platform: "Palo Alto Networks"
    management: "Panorama"
    monitoring: "Splunk"
    
  cobit:
    processes:
      - "DSS05 - Manage Security Services"
      - "DSS01 - Manage Operations"
      
  itil:
    lifecycle_phase: "Service Operation"
```

## Weiterführende Dokumentation

- **[PROCESS_DOCUMENTATION_GUIDE.md](PROCESS_DOCUMENTATION_GUIDE.md)** - Prozess-Dokumentation
- **[PLACEHOLDER_STRUCTURE.md](PLACEHOLDER_STRUCTURE.md)** - Placeholder-Hierarchie
- **[CONFIGURATION_REFERENCE.md](CONFIGURATION_REFERENCE.md)** - Konfigurationsreferenz
- **[METADATA_REFERENCE.md](METADATA_REFERENCE.md)** - Metadata-Referenz

## Support

Bei Fragen oder Problemen:

1. Prüfen Sie die Dokumentation
2. Überprüfen Sie die Beispiel-Services
3. Kontaktieren Sie den Support

---

**Version:** 0.0.17  
**Letzte Aktualisierung:** 2025-02-19  
**Autor:** Andreas Huemmer [andreas.huemmer@adminsend.de]
