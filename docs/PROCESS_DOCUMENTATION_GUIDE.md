# Process Documentation Guide

## Überblick

Dieser Leitfaden beschreibt, wie Sie Geschäftsprozesse mit dem Handbook Generator strukturiert mit BPMN-Diagrammen, RACI-Matrizen und Compliance-Anforderungen dokumentieren können.

## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Schnellstart](#schnellstart)
- [Prozess-Template-Struktur](#prozess-template-struktur)
- [Metadata-Konfiguration](#metadata-konfiguration)
- [Placeholder-Verwendung](#placeholder-verwendung)
- [RACI-Matrix](#raci-matrix)
- [BPMN-Diagramme](#bpmn-diagramme)
- [Compliance und SoD](#compliance-und-sod)
- [Eigene Prozesse erstellen](#eigene-prozesse-erstellen)
- [Best Practices](#best-practices)
- [Beispiele](#beispiele)

## Einführung

Die Prozess-Dokumentation ermöglicht die strukturierte Beschreibung von Geschäftsprozessen mit:

- **RACI-Matrizen**: Klare Verantwortlichkeiten (Responsible, Accountable, Consulted, Informed)
- **BPMN-Diagramme**: Visuelle Prozessdarstellung mit Business Process Model and Notation
- **SLA/OLA-Management**: Service Level und Operational Level Agreements
- **KPIs und Metriken**: Messbare Leistungsindikatoren
- **Compliance-Integration**: Mapping zu Compliance-Frameworks (ISO 27001, BSI, GDPR)
- **Segregation of Duties**: Funktionstrennung und Kontrollpunkte
- **Risikomanagement**: Risikoidentifikation und Mitigationsmaßnahmen

## Schnellstart

### Prozess-Dokumentation generieren

```bash
# Generisches Prozess-Template (Deutsch)
./handbook-generator --language de --process generic-process-template --test

# Generisches Prozess-Template (Englisch)
./handbook-generator --language en --process generic-process-template --test

# Mit allen Ausgabeformaten
./handbook-generator -l de --process generic-process-template -o all --test --separate-files --pdf-toc
```

### Ausgabe

Die generierten Prozess-Dokumente werden in folgendem Verzeichnis gespeichert:

```
test-output/
├── de/
│   └── generic-process-template/
│       ├── markdown/
│       │   └── process-template.md
│       ├── pdf/
│       │   └── process_documentation.pdf
│       └── html/
│           └── index.html
└── en/
    └── [identische Struktur]
```

## Prozess-Template-Struktur

### Verzeichnisstruktur

```
processes/
├── de/
│   ├── meta-global-process.yaml         # Globale Prozess-Konfiguration
│   └── generic-process-template/
│       ├── meta-process.yaml            # Prozess-spezifische Konfiguration
│       ├── diagrams/                    # BPMN-Diagramme
│       │   └── process-flow.bpmn
│       └── process-template.md          # Prozess-Template
└── en/
    ├── meta-global-process.yaml
    └── generic-process-template/
        ├── meta-process.yaml
        ├── diagrams/
        └── process-template.md
```

### Template-Abschnitte

Ein Prozess-Template enthält folgende Hauptabschnitte:

1. **Dokumenten-Header**: Metadaten (ID, Owner, Status, Revision)
2. **Zweck und Ziel**: Prozesszweck und Geschäftsziele
3. **Geltungsbereich**: Anwendungsbereich und Grenzen
4. **Trigger und Eingänge**: Auslöser und Inputs
5. **Ergebnisse und Outputs**: Erwartete Outputs und Erfolgskriterien
6. **Rollen und Verantwortlichkeiten**: RACI-Matrix
7. **Ablaufdiagramm**: BPMN-Diagramm mit textueller Beschreibung
8. **Systeme und Tools**: Verwendete IT-Systeme
9. **Schnittstellen**: Abhängigkeiten zu anderen Prozessen
10. **Artefakte**: Tickets, Logs, Reports
11. **SLAs und OLAs**: Service Level Agreements
12. **KPIs und Metriken**: Leistungsindikatoren
13. **Kontrollpunkte**: Prüfschritte und Audit-Anforderungen
14. **Risiken und Compliance**: Compliance-Frameworks und SoD-Regeln
15. **Eskalationen**: Eskalationswege und Ausnahmen
16. **Anhänge**: Checklisten, Runbooks, Formulare

## Metadata-Konfiguration

### Globale Prozess-Konfiguration (meta-global-process.yaml)

Die globale Konfiguration definiert Standard-Werte für alle Prozesse:

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

### Prozess-spezifische Konfiguration (meta-process.yaml)

Die prozess-spezifische Konfiguration überschreibt globale Werte:

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

## Placeholder-Verwendung

### Hierarchische Auflösung

Placeholders werden in folgender Priorität aufgelöst (höchste zuerst):

1. `meta-process.yaml` (prozess-spezifisch)
2. `meta-global-process.yaml` (global für alle Prozesse)
3. `meta-organisation-roles.yaml` (Rollen und Kontakte)
4. `meta-organisation.yaml` (Organisation)
5. `meta-global.yaml` (Generator-Informationen)

### Beispiel-Placeholders

```markdown
# Prozess: {{ process.name }}

**Dokument-ID:** {{ process.id }}
**Organisation:** {{ meta-organisation.name }}
**Prozess Owner:** {{ process.owner }}
**Prozess Manager:** {{ role_IT_Manager }}
**Genehmigt durch:** {{ role_CIO }}
**Status:** {{ process.status }}
**Letzte Aktualisierung:** {{ process.modifydate }}

## SLAs

**P1 Resolution:** {{ process.sla.p1_resolution }}
**P2 Resolution:** {{ process.sla.p2_resolution }}
**P3 Resolution:** {{ process.sla.p3_resolution }}

## Verwendete Systeme

{{ process.systems }}

## Eskalation

| Level | Rolle | Kontakt |
|-------|-------|---------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} |
```

## RACI-Matrix

### RACI-Konzept

RACI definiert Verantwortlichkeiten für Prozessschritte:

- **R (Responsible)**: Durchführung - Wer führt die Aktivität aus?
- **A (Accountable)**: Verantwortlich - Wer ist letztverantwortlich?
- **C (Consulted)**: Konsultiert - Wer wird um Rat gefragt?
- **I (Informed)**: Informiert - Wer wird über Ergebnisse informiert?

### RACI in Metadata definieren

```yaml
# meta-process.yaml
process:
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
    incident_resolution:
      responsible: "role_System_Administrator"
      accountable: "role_IT_Manager"
      consulted: "role_CISO"
      informed: "role_CIO"
```

### RACI-Matrix im Template

```markdown
## Rollen und Verantwortlichkeiten (RACI)

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
```

### RACI Best Practices

1. **Genau ein A pro Aktivität**: Jede Aktivität hat genau einen Accountable
2. **Mindestens ein R**: Jede Aktivität braucht mindestens einen Responsible
3. **C und I optional**: Nicht jede Aktivität braucht Consulted oder Informed
4. **Keine Überlappung R/A**: Idealerweise sind R und A verschiedene Personen (Four-Eyes-Principle)

## BPMN-Diagramme

### BPMN-Diagramm-Integration

BPMN-Diagramme werden im `diagrams/` Unterverzeichnis gespeichert:

```
processes/de/incident-management/
├── meta-process.yaml
├── diagrams/
│   ├── incident-flow.bpmn
│   ├── escalation-flow.bpmn
│   └── resolution-flow.bpmn
└── incident-management.md
```

### BPMN im Template referenzieren

```markdown
## Ablaufdiagramm (BPMN)

![Incident Management Flow](diagrams/incident-flow.bpmn)

### Prozessschritte

1. **Incident Detection**: Automatische Erkennung oder manuelle Meldung
2. **Incident Logging**: Erfassung in ServiceNow
3. **Incident Categorization**: Kategorisierung und Priorisierung
4. **Incident Investigation**: Analyse und Diagnose
5. **Incident Resolution**: Behebung und Wiederherstellung
6. **Incident Closure**: Dokumentation und Abschluss
```

### BPMN-Tools

Empfohlene Tools für BPMN-Diagramme:

- **Camunda Modeler**: Open-Source BPMN-Editor
- **bpmn.io**: Web-basierter BPMN-Editor
- **Lucidchart**: Kommerzielles Diagramm-Tool
- **draw.io**: Kostenloses Diagramm-Tool

## Compliance und SoD

### Compliance-Framework-Mapping

Prozesse können zu Compliance-Frameworks gemappt werden:

```yaml
# meta-process.yaml
process:
  compliance:
    frameworks:
      - "ISO 27001:2022 - Clause 5.24 (Information security incident management)"
      - "ISO 27001:2022 - Clause 5.25 (Assessment and decision on information security events)"
      - "BSI IT-Grundschutz - DER.2.1 (Incident Management)"
      - "GDPR Article 33 (Notification of a personal data breach)"
```

Im Template:

```markdown
## Compliance-Anforderungen

### Relevante Frameworks

{{ process.compliance.frameworks }}

### Audit-Anforderungen

- Vollständige Dokumentation aller Incidents
- Nachvollziehbare Eskalationswege
- Zeitstempel für alle Prozessschritte
- Regelmäßige Reviews und Lessons Learned
```

### Segregation of Duties (SoD)

SoD-Regeln verhindern Interessenkonflikte:

```yaml
# meta-process.yaml
process:
  compliance:
    sod_rules:
      - "Incident handler cannot approve own escalations"
      - "Security analyst cannot modify audit logs"
      - "Change implementer cannot approve own changes"
      - "Backup operator cannot restore own backups without approval"
```

Im Template:

```markdown
## Segregation of Duties (SoD)

### SoD-Regeln

{{ process.compliance.sod_rules }}

### Kontrollmechanismen

- Four-Eyes-Principle für kritische Aktivitäten
- Automatische SoD-Prüfung in ServiceNow
- Regelmäßige SoD-Audits
- Ausnahmen nur mit Management-Genehmigung
```

## Eigene Prozesse erstellen

### Schritt 1: Prozess-Verzeichnis erstellen

```bash
# Für deutschen Prozess
mkdir -p processes/de/incident-management/diagrams

# Für englischen Prozess
mkdir -p processes/en/incident-management/diagrams
```

### Schritt 2: Prozess-Konfiguration erstellen

Erstellen Sie `processes/de/incident-management/meta-process.yaml`:

```yaml
process:
  id: "PROC-INC-001"
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

### Schritt 3: BPMN-Diagramm erstellen

Erstellen Sie ein BPMN-Diagramm mit einem BPMN-Editor und speichern Sie es in:

```
processes/de/incident-management/diagrams/incident-flow.bpmn
```

### Schritt 4: Prozess-Template erstellen

Kopieren Sie das generische Template und passen Sie es an:

```bash
cp processes/de/generic-process-template/process-template.md \
   processes/de/incident-management/incident-management.md
```

### Schritt 5: Prozess generieren

```bash
./handbook-generator --language de --process incident-management --test
```

## Best Practices

### 1. Konsistente Namensgebung

- Prozess-IDs: `PROC-<KATEGORIE>-<NUMMER>` (z.B. `PROC-INC-001`)
- Verzeichnisnamen: Kleinbuchstaben mit Bindestrichen (z.B. `incident-management`)
- Template-Dateien: `<process-name>.md` (z.B. `incident-management.md`)

### 2. Vollständige RACI-Matrix

Definieren Sie RACI für alle kritischen Prozessschritte:

- ✅ Genau ein Accountable (A) pro Schritt
- ✅ Mindestens ein Responsible (R) pro Schritt
- ✅ Consulted (C) und Informed (I) wo sinnvoll
- ✅ Keine Überlappung R/A für kritische Schritte

### 3. Messbare KPIs

Definieren Sie messbare KPIs:

```yaml
kpis:
  mttr: "Mean Time To Resolve"
  mtbf: "Mean Time Between Failures"
  first_call_resolution: "Percentage of incidents resolved on first contact"
  sla_compliance: "Percentage of incidents resolved within SLA"
```

### 4. Compliance-Mapping

Mappen Sie Prozesse zu relevanten Compliance-Frameworks:

```yaml
compliance:
  frameworks:
    - "ISO 27001:2022 - Clause 5.24"
    - "BSI IT-Grundschutz - DER.2.1"
    - "GDPR Article 33"
```

### 5. SoD-Regeln dokumentieren

Dokumentieren Sie alle SoD-Regeln explizit:

```yaml
sod_rules:
  - "Incident handler cannot approve own escalations"
  - "Security analyst cannot modify audit logs"
  - "Change implementer cannot approve own changes"
```

### 6. BPMN-Diagramme aktuell halten

- Aktualisieren Sie BPMN-Diagramme bei Prozessänderungen
- Versionieren Sie BPMN-Dateien
- Dokumentieren Sie Änderungen

### 7. Bilinguale Konsistenz

Halten Sie deutsche und englische Versionen synchron:

- Identische Struktur in DE und EN
- Gleiche Prozess-IDs
- Konsistente RACI-Definitionen

## Beispiele

### Beispiel 1: Incident Management

```yaml
# processes/de/incident-management/meta-process.yaml
process:
  id: "PROC-INC-001"
  name: "Incident Management"
  category: "core"
  criticality: "Critical"
  
  sla:
    p1_resolution: "4 hours"
    p2_resolution: "24 hours"
    
  systems:
    - "ServiceNow"
    - "Zabbix"
    
  raci:
    incident_detection:
      responsible: "role_System_Administrator"
      accountable: "role_IT_Manager"
      
  compliance:
    frameworks:
      - "ISO 27001:2022 - Clause 5.24"
    sod_rules:
      - "Incident handler cannot approve own escalations"
```

### Beispiel 2: Change Management

```yaml
# processes/de/change-management/meta-process.yaml
process:
  id: "PROC-CHG-001"
  name: "Change Management"
  category: "core"
  criticality: "High"
  
  sla:
    standard_change: "5 business days"
    emergency_change: "4 hours"
    
  systems:
    - "ServiceNow"
    - "Git"
    - "Jenkins"
    
  raci:
    change_request:
      responsible: "role_Change_Requester"
      accountable: "role_Change_Manager"
      consulted: "role_IT_Manager"
      informed: "role_CIO"
    change_approval:
      responsible: "role_Change_Manager"
      accountable: "role_Change_Advisory_Board"
      
  compliance:
    frameworks:
      - "ISO 27001:2022 - Clause 5.37"
      - "ITIL 4 - Change Enablement"
    sod_rules:
      - "Change implementer cannot approve own changes"
      - "Change requester cannot be change approver"
```

### Beispiel 3: Backup and Recovery

```yaml
# processes/de/backup-recovery/meta-process.yaml
process:
  id: "PROC-BCK-001"
  name: "Backup and Recovery"
  category: "support"
  criticality: "Critical"
  
  sla:
    backup_frequency: "Daily"
    rto: "4 hours"
    rpo: "24 hours"
    
  systems:
    - "Veeam Backup"
    - "NetBackup"
    
  raci:
    backup_execution:
      responsible: "role_Backup_Administrator"
      accountable: "role_IT_Manager"
    restore_request:
      responsible: "role_Backup_Administrator"
      accountable: "role_IT_Manager"
      consulted: "role_Data_Owner"
      
  compliance:
    frameworks:
      - "ISO 27001:2022 - Clause 5.29"
      - "BSI IT-Grundschutz - CON.3"
    sod_rules:
      - "Backup operator cannot restore own backups without approval"
```

## Weiterführende Dokumentation

- **[SERVICE_DOCUMENTATION_GUIDE.md](SERVICE_DOCUMENTATION_GUIDE.md)** - Service-Dokumentation
- **[PLACEHOLDER_STRUCTURE.md](PLACEHOLDER_STRUCTURE.md)** - Placeholder-Hierarchie
- **[CONFIGURATION_REFERENCE.md](CONFIGURATION_REFERENCE.md)** - Konfigurationsreferenz
- **[METADATA_REFERENCE.md](METADATA_REFERENCE.md)** - Metadata-Referenz

## Support

Bei Fragen oder Problemen:

1. Prüfen Sie die Dokumentation
2. Überprüfen Sie die Beispiel-Prozesse
3. Kontaktieren Sie den Support

---

**Version:** 0.0.17  
**Letzte Aktualisierung:** 2025-02-19  
**Autor:** Andreas Huemmer [andreas.huemmer@adminsend.de]
