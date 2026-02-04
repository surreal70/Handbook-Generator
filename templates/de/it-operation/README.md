# IT-Operations Handbuch Templates

## Übersicht

Diese Template-Sammlung bietet eine umfassende Struktur für IT-Betriebshandbücher nach Best Practices aus ITIL v4, ISO 20000 und COBIT 2019. Die Templates decken alle wesentlichen Aspekte des IT-Betriebs ab und ermöglichen die Erstellung professioneller, standardkonformer Betriebsdokumentation.

## Template-Struktur

Die Templates sind in einer logischen Reihenfolge nummeriert (0010-0290) und decken folgende Themenbereiche ab:

### Grundlagen (0010-0060)

| Template | Beschreibung | Framework-Bezug |
|---|---|---|
| **0010_Einleitung.md** | Zweck, Geltungsbereich und Zielgruppe des Handbuchs | - |
| **0011_Rahmenbedingungen.md** | Organisatorische und technische Rahmenbedingungen | - |
| **0020_Dokumentenlenkung_und_Versionierung.md** | Versionskontrolle, Änderungshistorie, Genehmigungsprozesse | ISO 20000: 6.1 |
| **0030_Servicebeschreibung_und_Kritikalitaet.md** | Service-Definition, Kritikalitätsbewertung, SLA/SLO | ISO 20000: 8.2, 8.3 |
| **0040_Systemuebersicht_und_Architektur.md** | Technische Architektur, Komponenten, Abhängigkeiten | COBIT: BAI03 |
| **0050_Infrastruktur_und_Plattform.md** | Hardware, Virtualisierung, Cloud-Ressourcen, Netzwerk | - |
| **0060_Rollen_und_Verantwortlichkeiten.md** | RACI-Matrix, Kontakte, Eskalationspfade | COBIT: APO07 |

### Betriebsprozesse (0070-0110)

| Template | Beschreibung | Framework-Bezug |
|---|---|---|
| **0070_Betriebskonzept_und_Betriebsprozesse.md** | Betriebsmodelle, ITIL-Prozesse, Schnittstellen | ITIL: Service Design, COBIT: APO01 |
| **0080_Betriebsuebergabe_und_GoLive_Checkliste.md** | Go-Live-Checkliste, Übergabedokumentation | - |
| **0090_Konfigurationsmanagement_und_CMDB.md** | CI-Verwaltung, CMDB-Struktur, Change-Prozesse | ITIL: Service Configuration Management, COBIT: BAI10 |
| **0100_Access_und_Berechtigungsmanagement.md** | Zugriffskontrolle, RBAC, Berechtigungskonzept | ITIL: Service Desk |
| **0110_Monitoring_Alerting_und_Observability.md** | Überwachungskonzepte, Alerting-Regeln, Dashboards | ITIL: Monitoring and Event Management |

### Service Management (0120-0160)

| Template | Beschreibung | Framework-Bezug |
|---|---|---|
| **0120_Incident_Management_Runbook.md** | Störungsbehandlung, Eskalation, Standard-Runbooks | ITIL: Incident Management, COBIT: DSS02 |
| **0130_Problem_Management_und_Postmortems.md** | Root-Cause-Analysis, Known-Error-Database | ITIL: Problem Management, COBIT: DSS03 |
| **0140_Change_und_Release_Management.md** | Change-Kategorien, CAB-Prozesse, Deployment | ITIL: Change Enablement, Release Management, COBIT: BAI06 |
| **0150_Backup_und_Restore.md** | Backup-Strategien, RPO/RTO, Restore-Prozeduren | ITIL: Service Continuity Management |
| **0160_Disaster_Recovery_und_Business_Continuity.md** | DR-Szenarien, Failover/Failback, BC-Pläne | ITIL: Service Continuity Management, ISO 20000: 8.5, COBIT: APO12, DSS04 |

### Security & Compliance (0170-0190, 0280)

| Template | Beschreibung | Framework-Bezug |
|---|---|---|
| **0170_Sicherheitsbetrieb_und_Hardening.md** | Hardening-Richtlinien, Security-Monitoring, Compliance | ISO 20000: 8.8, COBIT: APO13, DSS05 |
| **0180_Patch_und_Update_Management.md** | Patch-Kategorien, Wartungsfenster, Vulnerability-Scanning | - |
| **0190_Log_Management_und_Audit.md** | Log-Sammlung, Retention-Policies, SIEM-Integration | - |
| **0280_Compliance_und_Audits.md** | Standards (ISO 27001, DSGVO, SOX), Audit-Prozesse | COBIT: DSS06 |

### Operations & Support (0200-0270, 0290)

| Template | Beschreibung | Framework-Bezug |
|---|---|---|
| **0200_Kapazitaets_und_Performance_Management.md** | Kapazitätsplanung, Performance-Monitoring, Skalierung | ITIL: Capacity and Performance Management, ISO 20000: 8.7, COBIT: APO09 |
| **0210_Verfuegbarkeit_und_Service_Level.md** | Verfügbarkeitsanforderungen, SLA-Definitionen, Reporting | ITIL: Availability Management, ISO 20000: 8.3, 8.4 |
| **0220_Datenmanagement_und_Datenschutz.md** | Datenklassifizierung, DSGVO-Anforderungen, Data-Governance | - |
| **0230_Wartung_und_Operations_Routinen.md** | Regelmäßige Wartungsaufgaben, Housekeeping-Prozeduren | COBIT: DSS01 |
| **0240_Runbooks_Standardoperationen.md** | Standard-Runbooks, Schritt-für-Schritt-Anleitungen | - |
| **0250_Tooling_und_Zugangswege.md** | Verwendete Tools, Zugriffswege, Authentifizierung | - |
| **0260_Bekannte_Probleme_und_FAQ.md** | Bekannte Probleme, Workarounds, Troubleshooting-Tipps | - |
| **0270_Kontakte_Eskalation_und_Anbieter.md** | Kontaktlisten, Eskalationspfade, Support-Kontakte | - |
| **0290_Anhang_Checklisten_und_Vorlagen.md** | Checklisten-Sammlung, Vorlagen, Formulare | - |

## Platzhalter-Verwendung

Die Templates unterstützen zwei Arten von Platzhaltern für dynamische Inhalte:

### Meta-Platzhalter (Organisationsweite Metadaten)

Meta-Platzhalter werden aus der `metadata.yaml` Konfigurationsdatei befüllt:

```markdown
**Organisation:** {{ meta.organization.name }}
**Standort:** {{ meta.organization.city }}, {{ meta.organization.country }}
**Website:** {{ meta.organization.website }}

**CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
**CISO:** {{ meta.ciso.name }} ({{ meta.ciso.email }})
**IT Operations Manager:** {{ meta.it_operations_manager.name }}
```

**Verfügbare Meta-Felder:**

**Organisation:**
- `{{ meta.organization.name }}` - Organisationsname
- `{{ meta.organization.address }}` - Adresse
- `{{ meta.organization.city }}` - Stadt
- `{{ meta.organization.postal_code }}` - Postleitzahl
- `{{ meta.organization.country }}` - Land
- `{{ meta.organization.website }}` - Website
- `{{ meta.organization.phone }}` - Telefon
- `{{ meta.organization.email }}` - E-Mail

**Rollen (ceo, cio, ciso, cfo, coo, it_operations_manager, service_desk_lead):**
- `{{ meta.ROLLE.name }}` - Name der Person
- `{{ meta.ROLLE.title }}` - Titel/Position
- `{{ meta.ROLLE.email }}` - E-Mail-Adresse
- `{{ meta.ROLLE.phone }}` - Telefonnummer
- `{{ meta.ROLLE.department }}` - Abteilung (optional)

**Dokument:**
- `{{ meta.document.owner }}` - Dokumentverantwortlicher
- `{{ meta.document.approver }}` - Genehmiger
- `{{ meta.document.version }}` - Version
- `{{ meta.document.classification }}` - Klassifizierung

### NetBox-Platzhalter (Infrastruktur-Daten)

NetBox-Platzhalter werden aus der NetBox-CMDB befüllt:

```markdown
**Standort:** {{ netbox.site.name }}
**Adresse:** {{ netbox.site.physical_address }}
**Rechenzentrum:** {{ netbox.site.facility }}

**Core Switch:** {{ netbox.device.core_switch.name }}
**Management VLAN:** {{ netbox.vlan.management.vid }}
**Hypervisor-Cluster:** {{ netbox.cluster.name }}
```

## Best Practices für Template-Anpassungen

### 1. Template-Individualisierung

**Kopieren Sie Templates für spezifische Services:**
```bash
# Beispiel: Individuelles Template für einen spezifischen Service
cp templates/de/service-templates/service_description_template.md \
   my-service/service_description_my_app.md
```

**Ersetzen Sie [TODO] Markierungen:**
- Alle Templates enthalten `[TODO]` Markierungen für individualisierbare Abschnitte
- Ersetzen Sie diese mit servicespezifischen Informationen
- Behalten Sie die Struktur und Überschriften bei

### 2. HTML-Kommentare für Template-Dokumentation

**Verwenden Sie HTML-Kommentare für nicht-gerenderte Hinweise:**

Templates können HTML-Kommentare enthalten, die im generierten Handbuch nicht erscheinen. Diese sind ideal für:

```markdown
<!-- 
TEMPLATE-AUTOR HINWEIS:
Dieser Abschnitt muss für jeden Service individuell angepasst werden.
Berücksichtigen Sie:
- Service-spezifische Architektur
- Abhängigkeiten zu anderen Services
- Kritikalitätseinstufung
-->

## Systemarchitektur

{{ netbox.device.name }}

<!-- TODO: Architekturdiagramm einfügen -->
```

**Anwendungsfälle für HTML-Kommentare:**

**Anpassungshinweise:**
```markdown
<!-- Passen Sie die folgenden Werte an Ihre Organisation an -->
**Wartungsfenster:** Sonntag 02:00-06:00 Uhr
```

**Framework-Referenzen:**
```markdown
<!-- Dieser Abschnitt erfüllt ISO 20000 Anforderung 8.6 -->
## Incident Management
```

**Platzhalter-Dokumentation:**
```markdown
<!-- Der Platzhalter {{ meta.cio.name }} wird durch den CIO-Namen ersetzt -->
**Verantwortlich:** {{ meta.cio.name }}
```

**Best Practices:**
- Kommentare werden vor der Platzhalter-Verarbeitung entfernt
- Platzhalter innerhalb von Kommentaren werden nicht ersetzt
- Verwenden Sie Kommentare für Hinweise, nicht für sensible Daten
- Vermeiden Sie verschachtelte Kommentare

### 3. RACI-Matrizen ausfüllen

**Vollständige RACI-Matrizen sind essentiell:**
```markdown
| Aktivität | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Betrieb & Monitoring | A | C | R | I |
| Incident Management | A | C | R | R |
| Change Management | A | C | R | I |
```

**RACI-Legende:**
- **R** (Responsible) - Führt die Aktivität durch
- **A** (Accountable) - Trägt die Gesamtverantwortung
- **C** (Consulted) - Wird konsultiert
- **I** (Informed) - Wird informiert

**Best Practices:**
- Jede Aktivität muss genau ein "A" haben
- Mindestens ein "R" pro Aktivität
- Vermeiden Sie zu viele "C" (Entscheidungsverzögerung)

### 3. Framework-Referenzen einbinden

**Verweisen Sie auf relevante Standards:**
```markdown
## Compliance-Anforderungen

Dieser Prozess erfüllt folgende Standards:
- **ITIL v4:** Incident Management Practice
- **ISO 20000-1:2018:** Clause 8.6 (Incident Management)
- **COBIT 2019:** DSS02 (Managed Service Requests and Incidents)
```

### 4. Platzhalter konsistent verwenden

**Verwenden Sie Platzhalter für wiederkehrende Informationen:**
```markdown
<!-- Gut: Platzhalter für Organisationsnamen -->
**Organisation:** {{ meta.organization.name }}

<!-- Schlecht: Hardcodierter Wert -->
**Organisation:** AdminSend GmbH
```

**Vorteile:**
- Zentrale Verwaltung in metadata.yaml
- Konsistenz über alle Handbücher
- Einfache Aktualisierung bei Änderungen

### 5. Versionierung und Änderungshistorie

**Pflegen Sie die Änderungshistorie:**
```markdown
## Änderungshistorie

| Version | Datum | Autor | Änderungen | Genehmigt durch |
|---|---|---|---|---|
| 1.0.0 | 2024-01-15 | {{ meta.author }} | Initiale Version | {{ meta.document.approver }} |
| 1.1.0 | 2024-02-20 | {{ meta.author }} | Monitoring-Abschnitt erweitert | {{ meta.document.approver }} |
```

### 6. Service-Level-Definitionen

**Definieren Sie messbare SLAs:**
```markdown
| Kennzahl | Zielwert | Messmethode | Verantwortlich |
|---|---:|---|---|
| Verfügbarkeit | 99.9% | Uptime-Monitoring | {{ meta.it_operations_manager.name }} |
| Antwortzeit | < 200ms | APM-Tool | {{ meta.it_operations_manager.name }} |
| MTTR | < 4h | Incident-Tracking | {{ meta.service_desk_lead.name }} |
```

## Generierung von Handbüchern

### Vollständiges IT-Operations-Handbuch generieren

```bash
# Deutsches Handbuch
python -m src.cli --language de --template it-operation --output-format both

# Englisches Handbuch
python -m src.cli --language en --template it-operation --output-format both
```

### Service-spezifisches Handbuch erstellen

```bash
# 1. Service-Template kopieren und anpassen
cp templates/de/service-templates/service_description_template.md \
   my-service/service_description.md

# 2. [TODO] Markierungen ersetzen
# 3. Handbuch generieren
python -m src.cli --language de --template my-service --output-format both
```

### Ausgabeformate

- `--output-format markdown` - Nur Markdown-Dateien
- `--output-format pdf` - Nur PDF-Dateien
- `--output-format both` - Markdown und PDF

## Konfiguration

### metadata.yaml erstellen

```bash
# Kopieren Sie die Beispiel-Konfiguration
cp metadata.example.yaml metadata.yaml

# Bearbeiten Sie die Datei mit Ihren Organisationsdaten
nano metadata.yaml
```

### Minimale metadata.yaml

```yaml
organization:
  name: "Ihre Organisation"
  address: "Ihre Adresse"
  city: "Ihre Stadt"
  postal_code: "12345"
  country: "Deutschland"
  website: "https://www.ihre-domain.de"
  phone: "+49 123 456789"
  email: "info@ihre-domain.de"

roles:
  cio:
    name: "Name des CIO"
    title: "Chief Information Officer"
    email: "cio@ihre-domain.de"
    phone: "+49 123 456789-100"

document:
  owner: "IT Operations Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"
```

## Framework-Compliance

### ITIL v4 Process Coverage

Die Templates decken folgende ITIL v4 Service Management Practices ab:

- **Service Design** - Betriebskonzept und Prozesse
- **Monitoring and Event Management** - Monitoring und Alerting
- **Incident Management** - Störungsbehandlung
- **Problem Management** - Ursachenanalyse
- **Change Enablement** - Änderungssteuerung
- **Release Management** - Release-Planung
- **Service Configuration Management** - CMDB und CI-Verwaltung
- **Service Continuity Management** - Backup, DR, BC
- **Availability Management** - Verfügbarkeitsmanagement
- **Capacity and Performance Management** - Kapazitätsplanung

### ISO 20000-1:2018 Compliance

Die Templates unterstützen folgende ISO 20000 Anforderungen:

- **6.1** Service Planning - Betriebskonzept
- **8.2** Service Catalogue - Servicebeschreibung
- **8.3** Service Level Management - SLA-Definitionen
- **8.4** Service Reporting - Monitoring und Reporting
- **8.5** Service Continuity - Disaster Recovery
- **8.7** Capacity Management - Kapazitätsmanagement
- **8.8** Information Security - Sicherheitsbetrieb

### COBIT 2019 Alignment

Die Templates unterstützen folgende COBIT Objectives:

- **APO01** Managed IT Management Framework
- **APO07** Managed Human Resources
- **APO09** Managed Service Agreements
- **APO12** Managed Risk
- **APO13** Managed Security
- **BAI03** Managed Solutions Identification
- **BAI06** Managed IT Changes
- **BAI10** Managed Configuration
- **DSS01** Managed Operations
- **DSS02** Managed Service Requests
- **DSS03** Managed Problems
- **DSS04** Managed Continuity
- **DSS05** Managed Security Services
- **DSS06** Managed Business Process Controls

## Häufige Fragen (FAQ)

### Muss ich alle Templates verwenden?

Nein. Wählen Sie die Templates aus, die für Ihren Service relevant sind. Die Nummerierung ermöglicht eine logische Reihenfolge, aber nicht alle Templates sind für jeden Service erforderlich.

### Kann ich eigene Templates hinzufügen?

Ja. Folgen Sie der Nummerierungskonvention (z.B. 0095 für ein Template zwischen 0090 und 0100) und verwenden Sie dieselbe Struktur mit Platzhaltern.

### Wie aktualisiere ich Organisationsinformationen?

Bearbeiten Sie die `metadata.yaml` Datei. Alle Handbücher, die Sie danach generieren, verwenden automatisch die aktualisierten Informationen.

### Funktionieren die Templates ohne NetBox?

Ja. NetBox-Platzhalter sind optional. Wenn NetBox nicht konfiguriert ist, bleiben die Platzhalter unverändert und können manuell ausgefüllt werden.

### Wie erstelle ich mehrsprachige Handbücher?

Generieren Sie Handbücher mit `--language de` für Deutsch und `--language en` für Englisch. Die Templates sind in beiden Sprachen verfügbar.

## Support und Weiterentwicklung

### Feedback und Verbesserungsvorschläge

Wenn Sie Verbesserungsvorschläge für die Templates haben:
1. Dokumentieren Sie den Verbesserungsvorschlag
2. Erstellen Sie ein Beispiel
3. Kontaktieren Sie das Template-Maintainer-Team

### Template-Updates

Die Templates werden regelmäßig aktualisiert, um:
- Neue Framework-Versionen zu berücksichtigen (ITIL, ISO 20000, COBIT)
- Best Practices zu integrieren
- Feedback von Nutzern einzuarbeiten

## Lizenz und Nutzung

Diese Templates sind für den internen Gebrauch in Ihrer Organisation bestimmt. Sie können die Templates frei anpassen und erweitern.

---

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2024-01-31  
**Maintainer:** IT Operations Team
