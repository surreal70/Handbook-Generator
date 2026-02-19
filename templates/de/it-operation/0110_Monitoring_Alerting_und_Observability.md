# Monitoring, Alerting und Observability

**Dokument-ID:** [FRAMEWORK]-0110
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Übersicht

Dieses Dokument beschreibt die Monitoring-, Alerting- und Observability-Strategie für den IT-Service. Es definiert Monitoring-Tools, Alerting-Regeln, Schwellwerte und Observability-Konzepte.

**Service:** {{ meta-handbook.service_name }}  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**Stand:** {{ meta-handbook.revision }}

## Monitoring-Strategie

### Monitoring-Ziele

- **Proaktive Erkennung:** Probleme erkennen bevor sie Auswirkungen haben
- **Performance-Optimierung:** Engpässe identifizieren und beheben
- **Verfügbarkeit:** Service-Verfügbarkeit sicherstellen
- **Kapazitätsplanung:** Trends erkennen für Kapazitätsplanung
- **Compliance:** Nachweis der Service-Level-Einhaltung

### Monitoring-Ebenen

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 7: Business Metrics                                    │
│ (Transaktionen, User Experience, Business KPIs)             │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│ Layer 6: Application Monitoring                              │
│ (Application Performance, Errors, Response Times)            │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│ Layer 5: Service Monitoring                                  │
│ (Service Health, API Endpoints, Dependencies)                │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│ Layer 4: Infrastructure Monitoring                           │
│ (Servers, Network, Storage, Virtualization)                  │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│ Layer 3: System Monitoring                                   │
│ (CPU, Memory, Disk, Network Interfaces)                      │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│ Layer 2: Network Monitoring                                  │
│ (Connectivity, Bandwidth, Latency, Packet Loss)              │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│ Layer 1: Physical Monitoring                                 │
│ (Power, Cooling, Environmental)                              │
└─────────────────────────────────────────────────────────────┘
```

## Monitoring-Tools

### Tool-Stack

| Tool | Verwendung | Verantwortlich | URL |
|---|---|---|---|
| **[TODO: z.B. Prometheus]** | Metriken-Sammlung | Monitoring Team | [TODO] |
| **[TODO: z.B. Grafana]** | Visualisierung | Monitoring Team | [TODO] |
| **[TODO: z.B. Nagios/Zabbix]** | Infrastructure Monitoring | IT Operations | [TODO] |
| **[TODO: z.B. ELK Stack]** | Log-Aggregation | IT Operations | [TODO] |
| **[TODO: z.B. Jaeger]** | Distributed Tracing | Development Team | [TODO] |
| **[TODO: z.B. Pingdom]** | Synthetic Monitoring | IT Operations | [TODO] |
| **[TODO: z.B. New Relic/Datadog]** | APM | Development Team | [TODO] |

### Tool-Integration

**Datenfluss:**
```
┌─────────────┐
│   Agents    │
│  (Exporters)│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Collectors │
│ (Prometheus)│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Storage   │
│  (TSDB)     │
└──────┬──────┘
       │
       ├──────────────┐
       │              │
       ▼              ▼
┌─────────────┐  ┌─────────────┐
│Visualization│  │  Alerting   │
│  (Grafana)  │  │(Alertmanager)│
└─────────────┘  └─────────────┘
```

## Infrastructure Monitoring

### Server-Monitoring

#### Metriken

| Metrik | Beschreibung | Schwellwert Warning | Schwellwert Critical | Frequenz |
|---|---|---:|---:|---|
| **CPU Usage** | CPU-Auslastung | > 80% | > 95% | 1 Min |
| **Memory Usage** | RAM-Auslastung | > 85% | > 95% | 1 Min |
| **Disk Usage** | Festplatten-Auslastung | > 80% | > 90% | 5 Min |
| **Disk I/O** | Disk-Operationen | > 80% | > 95% | 1 Min |
| **Network Traffic** | Netzwerk-Durchsatz | > 80% | > 95% | 1 Min |
| **Load Average** | System-Last | > 4.0 | > 8.0 | 1 Min |
| **Swap Usage** | Swap-Nutzung | > 50% | > 80% | 5 Min |

#### Überwachte Server

| Server | Standort | Rolle | Monitoring-Agent | Status |
|---|---|---|---|---|
| [[ netbox.device.name ]] | [[ netbox.device.site ]] | [[ netbox.device.role ]] | [TODO: Agent] | ☐ Aktiv |
| [TODO] | [TODO] | [TODO] | [TODO] | ☐ Aktiv |

### Netzwerk-Monitoring

#### Metriken

| Metrik | Beschreibung | Schwellwert Warning | Schwellwert Critical | Frequenz |
|---|---|---:|---:|---|
| **Interface Status** | Port Up/Down | Down | Down > 5 Min | 30 Sek |
| **Bandwidth Usage** | Bandbreiten-Auslastung | > 80% | > 95% | 1 Min |
| **Packet Loss** | Paketverlust | > 1% | > 5% | 1 Min |
| **Latency** | Netzwerk-Latenz | > 50ms | > 100ms | 1 Min |
| **Error Rate** | Fehlerrate | > 0.1% | > 1% | 1 Min |
| **CRC Errors** | CRC-Fehler | > 0 | > 100 | 5 Min |

#### Überwachte Netzwerkgeräte

| Gerät | Typ | Standort | Management-IP | Status |
|---|---|---|---|---|
| [[ netbox.device.name ]] | [[ netbox.device.device_type ]] | [[ netbox.device.site ]] | [[ netbox.device.primary_ip ]] | ☐ Aktiv |
| [TODO] | [TODO] | [TODO] | [TODO] | ☐ Aktiv |

### Storage-Monitoring

#### Metriken

| Metrik | Beschreibung | Schwellwert Warning | Schwellwert Critical | Frequenz |
|---|---|---:|---:|---|
| **Capacity** | Speicherkapazität | > 80% | > 90% | 5 Min |
| **IOPS** | I/O-Operationen | > 80% Max | > 95% Max | 1 Min |
| **Throughput** | Durchsatz | > 80% Max | > 95% Max | 1 Min |
| **Latency** | Zugriffszeit | > 20ms | > 50ms | 1 Min |
| **Disk Health** | Festplatten-Gesundheit | SMART Warning | SMART Error | 1 Stunde |

### Virtualisierung-Monitoring

#### Hypervisor-Metriken

| Metrik | Beschreibung | Schwellwert Warning | Schwellwert Critical | Frequenz |
|---|---|---:|---:|---|
| **Host CPU** | CPU-Auslastung Host | > 80% | > 95% | 1 Min |
| **Host Memory** | RAM-Auslastung Host | > 85% | > 95% | 1 Min |
| **VM Count** | Anzahl VMs | > 80% Max | > 95% Max | 5 Min |
| **Datastore Usage** | Datastore-Auslastung | > 80% | > 90% | 5 Min |
| **VM Performance** | VM-Performance | Degraded | Critical | 1 Min |

## Application Monitoring

### Application Performance Monitoring (APM)

#### Metriken

| Metrik | Beschreibung | Schwellwert Warning | Schwellwert Critical | Frequenz |
|---|---|---:|---:|---|
| **Response Time** | Antwortzeit | > 500ms | > 2000ms | Real-time |
| **Error Rate** | Fehlerrate | > 1% | > 5% | Real-time |
| **Throughput** | Requests/Sekunde | < 80% Normal | < 50% Normal | Real-time |
| **Apdex Score** | User Satisfaction | < 0.85 | < 0.70 | Real-time |
| **Database Query Time** | DB-Abfragezeit | > 100ms | > 500ms | Real-time |
| **External API Latency** | API-Latenz | > 200ms | > 1000ms | Real-time |

### Synthetic Monitoring

**Überwachte Endpunkte:**

| Endpunkt | Typ | Frequenz | Erwartete Response | Timeout |
|---|---|---|---|---|
| [TODO: URL] | HTTP/HTTPS | 1 Min | 200 OK | 5 Sek |
| [TODO: URL] | API | 1 Min | 200 OK | 3 Sek |
| [TODO: URL] | Health Check | 30 Sek | 200 OK | 2 Sek |

**Prüfungen:**
- HTTP-Status-Code
- Response-Zeit
- Content-Validierung
- SSL-Zertifikat-Gültigkeit
- DNS-Auflösung

## Observability

### Die drei Säulen der Observability

#### 1. Metrics (Metriken)
**Definition:** Numerische Werte über Zeit  
**Verwendung:** Trends, Alerts, Dashboards  
**Tools:** Prometheus, Grafana  
**Beispiele:**
- CPU-Auslastung
- Request-Rate
- Error-Rate
- Response-Time

#### 2. Logs (Protokolle)
**Definition:** Ereignis-basierte Aufzeichnungen  
**Verwendung:** Debugging, Audit, Troubleshooting  
**Tools:** ELK Stack, Splunk  
**Beispiele:**
- Application-Logs
- System-Logs
- Access-Logs
- Error-Logs

#### 3. Traces (Ablaufverfolgung)
**Definition:** Request-Flow durch verteilte Systeme  
**Verwendung:** Performance-Analyse, Bottleneck-Identifikation  
**Tools:** Jaeger, Zipkin  
**Beispiele:**
- Distributed Tracing
- Service-Dependencies
- Latency-Breakdown
- Error-Propagation

### Observability-Strategie

```
┌─────────────────────────────────────────────────────────────┐
│                    User Request                              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   Metrics Collection  │ ──→ Prometheus
         └───────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │    Log Aggregation    │ ──→ ELK Stack
         └───────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │  Distributed Tracing  │ ──→ Jaeger
         └───────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   Correlation &       │
         │   Visualization       │ ──→ Grafana
         └───────────────────────┘
```

## Alerting

### Alerting-Strategie

**Prinzipien:**
- **Actionable:** Jeder Alert erfordert eine Aktion
- **Relevant:** Nur kritische Ereignisse alarmieren
- **Timely:** Alerts in Echtzeit
- **Clear:** Eindeutige Alert-Beschreibungen
- **Escalation:** Definierte Eskalationspfade

### Alert-Severity-Levels

| Level | Beschreibung | Reaktionszeit | Eskalation | Beispiel |
|---|---|---|---|---|
| **Critical** | Service-Ausfall | Sofort | Sofort | Service Down |
| **High** | Schwerwiegendes Problem | 15 Min | Nach 30 Min | CPU > 95% |
| **Medium** | Problem erfordert Aufmerksamkeit | 1 Stunde | Nach 4 Stunden | Disk > 85% |
| **Low** | Informativ, keine sofortige Aktion | 1 Tag | Keine | Backup Warning |
| **Info** | Informativ | Keine | Keine | Backup Success |

### Alerting-Regeln

#### Infrastructure Alerts

| Alert | Bedingung | Severity | Aktion | Verantwortlich |
|---|---|---|---|---|
| **Server Down** | Ping failed > 5 Min | Critical | Sofort prüfen | {{ meta-organisation-roles.role_Service_Desk_Lead }} |
| **High CPU** | CPU > 95% für 5 Min | High | Performance prüfen | IT Operations |
| **High Memory** | Memory > 95% für 5 Min | High | Memory-Leak prüfen | IT Operations |
| **Disk Full** | Disk > 90% | High | Speicher freigeben | IT Operations |
| **Disk Warning** | Disk > 80% | Medium | Kapazität planen | IT Operations |

#### Application Alerts

| Alert | Bedingung | Severity | Aktion | Verantwortlich |
|---|---|---|---|---|
| **Service Down** | Health Check failed | Critical | Service restart | {{ meta-organisation-roles.role_Service_Desk_Lead }} |
| **High Error Rate** | Errors > 5% für 5 Min | High | Logs prüfen | Development Team |
| **Slow Response** | Response Time > 2s | High | Performance prüfen | Development Team |
| **API Failure** | External API down | High | Vendor kontaktieren | IT Operations |

#### Network Alerts

| Alert | Bedingung | Severity | Aktion | Verantwortlich |
|---|---|---|---|---|
| **Link Down** | Interface down > 5 Min | Critical | Verbindung prüfen | Network Team |
| **High Bandwidth** | Bandwidth > 95% | High | Traffic analysieren | Network Team |
| **High Latency** | Latency > 100ms | Medium | Routing prüfen | Network Team |
| **Packet Loss** | Loss > 5% | High | Verbindung prüfen | Network Team |

### Alert-Routing

```
┌─────────────────┐
│  Alert Trigger  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Alert Manager   │
└────────┬────────┘
         │
         ├──────────────┬──────────────┬──────────────┐
         │              │              │              │
         ▼              ▼              ▼              ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   E-Mail    │  │    Slack    │  │     SMS     │  │  PagerDuty  │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

### Alert-Empfänger

| Severity | Primär | Sekundär | Eskalation |
|---|---|---|---|
| **Critical** | On-Call Engineer | IT Ops Manager | CIO |
| **High** | IT Operations Team | IT Ops Manager | - |
| **Medium** | IT Operations Team | - | - |
| **Low** | E-Mail an Team | - | - |

**On-Call-Rotation:**
- **Woche 1:** [TODO: Name]
- **Woche 2:** [TODO: Name]
- **Woche 3:** [TODO: Name]
- **Woche 4:** [TODO: Name]

## Dashboards

### Dashboard-Übersicht

#### Executive Dashboard
**Zielgruppe:** Management  
**Inhalt:**
- Service-Verfügbarkeit (aktuell und historisch)
- SLA-Compliance
- Incident-Übersicht
- Performance-Trends
- Kosten-Übersicht

**URL:** [TODO: Dashboard-URL]

#### Operations Dashboard
**Zielgruppe:** IT Operations  
**Inhalt:**
- Aktuelle Alerts
- System-Health-Status
- Performance-Metriken
- Capacity-Trends
- Incident-Status

**URL:** [TODO: Dashboard-URL]

#### Application Dashboard
**Zielgruppe:** Development Team  
**Inhalt:**
- Application-Performance
- Error-Rates
- Response-Times
- Database-Performance
- API-Latencies

**URL:** [TODO: Dashboard-URL]

#### Infrastructure Dashboard
**Zielgruppe:** Infrastructure Team  
**Inhalt:**
- Server-Status
- Network-Status
- Storage-Status
- Virtualization-Status
- Environmental-Status

**URL:** [TODO: Dashboard-URL]

### Dashboard-Best-Practices

1. **Single Pane of Glass:** Alle wichtigen Informationen auf einen Blick
2. **Color Coding:** Rot (Critical), Orange (Warning), Grün (OK)
3. **Drill-Down:** Von Übersicht zu Details navigieren
4. **Real-Time:** Aktuelle Daten anzeigen
5. **Historical:** Trends über Zeit zeigen
6. **Annotations:** Wichtige Events markieren

## Monitoring-Prozesse

### Tägliche Monitoring-Routinen

**Morgen-Check (08:00 Uhr):**
- [ ] Dashboards prüfen
- [ ] Offene Alerts reviewen
- [ ] Overnight-Incidents prüfen
- [ ] Backup-Status validieren
- [ ] Performance-Trends analysieren

**Tages-Monitoring:**
- [ ] Kontinuierliche Alert-Überwachung
- [ ] Incident-Response bei Alerts
- [ ] Performance-Optimierung
- [ ] Kapazitäts-Monitoring

**Abend-Check (18:00 Uhr):**
- [ ] Tages-Alerts reviewen
- [ ] Offene Issues dokumentieren
- [ ] Handover an Nachtschicht (falls 24/7)
- [ ] Wartungsarbeiten planen

### Wöchentliche Aktivitäten

- [ ] Monitoring-Daten analysieren
- [ ] Alert-Tuning durchführen
- [ ] False-Positives reduzieren
- [ ] Dashboard-Updates
- [ ] Kapazitäts-Trends reviewen

### Monatliche Aktivitäten

- [ ] Monitoring-Coverage prüfen
- [ ] SLA-Reports erstellen
- [ ] Performance-Trends analysieren
- [ ] Monitoring-Tools aktualisieren
- [ ] Alert-Regeln optimieren

## Service Level Indicators (SLIs)

### Definierte SLIs

| SLI | Beschreibung | Messung | Zielwert |
|---|---|---|---|
| **Availability** | Service-Verfügbarkeit | Uptime / Total Time | ≥ 99.5% |
| **Latency** | Response-Zeit | P95 Response Time | ≤ 500ms |
| **Error Rate** | Fehlerrate | Errors / Total Requests | ≤ 0.1% |
| **Throughput** | Durchsatz | Requests / Second | ≥ [TODO] |
| **Saturation** | Ressourcen-Auslastung | CPU/Memory/Disk Usage | ≤ 80% |

### SLI-Monitoring

**Datenquellen:**
- Synthetic Monitoring
- Real User Monitoring (RUM)
- Application Logs
- Infrastructure Metrics

**Reporting:**
- Echtzeit-Dashboards
- Tägliche Reports
- Monatliche SLA-Reports

## Incident Response

### Monitoring-basierte Incident Response

```
┌─────────────────┐
│  Alert Trigger  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Alert Received  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Initial Triage  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Incident Created│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Investigation   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Resolution    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Post-Mortem     │
└─────────────────┘
```

**Details:** Siehe Kapitel 0120 (Incident Management)

## Monitoring-Dokumentation

### Runbooks

Für jeden kritischen Alert existiert ein Runbook:
- Alert-Beschreibung
- Mögliche Ursachen
- Diagnose-Schritte
- Lösungsschritte
- Eskalationspfad

**Runbook-Verzeichnis:** Siehe Kapitel 0240 (Runbooks)

### Known Issues

Bekannte Monitoring-Probleme und Workarounds:
- False-Positive-Alerts
- Monitoring-Gaps
- Tool-Limitierungen

**Known Issues:** Siehe Kapitel 0260 (Bekannte Probleme und FAQ)

## Monitoring-Tools-Zugriff

### Tool-Zugänge

| Tool | URL | Authentifizierung | Zugriff |
|---|---|---|---|
| [TODO: Monitoring-Tool] | [TODO: URL] | SSO | IT Operations |
| [TODO: Dashboard-Tool] | [TODO: URL] | SSO | Alle |
| [TODO: Log-Tool] | [TODO: URL] | SSO | IT Operations |
| [TODO: APM-Tool] | [TODO: URL] | SSO | Development |

### Berechtigungen

- **Administrator:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
- **Operator:** IT Operations Team
- **Read-Only:** Management, Auditors

## Kontakte

**Monitoring-Team:**
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} - {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Service Desk Lead:** {{ meta-organisation-roles.role_Service_Desk_Lead }} - {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **On-Call Engineer:** [TODO: Rotation] - [TODO: On-Call-Nummer]

**Eskalation:**
- **Level 2:** {{ meta-organisation-roles.role_IT_Operations_Manager }} - {{ meta-organisation-roles.role_IT_Operations_Manager_phone }}
- **Level 3:** {{ meta-organisation-roles.role_CIO }} - {{ meta-organisation-roles.role_CIO_phone }}

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

