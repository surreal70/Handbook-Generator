# Log Management und Audit

**Dokument-ID:** [FRAMEWORK]-0190
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---

## Zweck und Geltungsbereich

Dieses Dokument beschreibt die Log-Management- und Audit-Prozesse für AdminSend GmbH. Es definiert Log-Sammlung, -Aggregation, -Retention, Audit-Trail-Anforderungen und SIEM-Integration zur Sicherstellung von Nachvollziehbarkeit, Compliance und Security-Monitoring.

**Geltungsbereich:** Alle IT-Systeme, Netzwerke, Applikationen und Security-Komponenten von AdminSend GmbH

**Verantwortlich:** [TODO] ({{ meta-organisation-roles.role_CISO_email }})

## Log-Management-Grundlagen

### Ziele

**Primäre Ziele:**
- **Security-Monitoring:** Erkennung von Sicherheitsvorfällen
- **Compliance:** Erfüllung regulatorischer Anforderungen
- **Troubleshooting:** Fehleranalyse und Problemlösung
- **Forensik:** Nachvollziehbarkeit von Ereignissen
- **Audit:** Nachweis von Kontrollen und Prozessen
- **Performance-Analyse:** System- und Applikations-Performance

### Log-Typen

#### System-Logs

**Beschreibung:** Betriebssystem-Ereignisse

**Beispiele:**
- Windows Event Logs (Security, System, Application)
- Linux Syslog (/var/log/messages, /var/log/auth.log)
- Boot-Logs, Kernel-Logs

**Wichtige Events:**
- System-Start/-Stop
- Service-Start/-Stop
- Fehler und Warnungen
- Hardware-Events

#### Security-Logs

**Beschreibung:** Sicherheitsrelevante Ereignisse

**Beispiele:**
- Authentifizierungs-Events (Login, Logout, Failed Login)
- Autorisierungs-Events (Zugriffsverweigerung)
- Privilegien-Änderungen
- Security-Policy-Änderungen
- Firewall-Logs
- IDS/IPS-Alerts

**Wichtige Events:**
- Failed Login Attempts
- Privilege Escalation
- Account-Änderungen
- Security-Policy-Änderungen

#### Application-Logs

**Beschreibung:** Applikations-spezifische Ereignisse

**Beispiele:**
- Web-Server-Logs (Apache, Nginx, IIS)
- Datenbank-Logs (MySQL, PostgreSQL, SQL Server)
- Applikations-Logs (Custom-Apps)
- Middleware-Logs (Tomcat, JBoss)

**Wichtige Events:**
- Applikations-Fehler
- Transaktions-Logs
- Performance-Metriken
- User-Aktivitäten

#### Network-Logs

**Beschreibung:** Netzwerk-Ereignisse

**Beispiele:**
- Firewall-Logs
- Router/Switch-Logs
- VPN-Logs
- DNS-Logs
- DHCP-Logs
- Proxy-Logs

**Wichtige Events:**
- Verbindungs-Versuche (erlaubt/blockiert)
- Netzwerk-Änderungen
- Bandwidth-Nutzung
- Anomalien

#### Audit-Logs

**Beschreibung:** Compliance- und Audit-relevante Ereignisse

**Beispiele:**
- Daten-Zugriffe
- Konfigurations-Änderungen
- Administrative Aktivitäten
- Privilegierte Zugriffe

**Wichtige Events:**
- Wer hat was wann gemacht?
- Änderungen an kritischen Systemen
- Zugriff auf sensible Daten

### Log-Levels

| Level | Beschreibung | Verwendung | Beispiel |
|---|---|---|---|
| **EMERGENCY** | System unbrauchbar | Kritische Systemfehler | Kernel Panic |
| **ALERT** | Sofortige Aktion erforderlich | Kritische Fehler | Datenbank nicht erreichbar |
| **CRITICAL** | Kritische Bedingungen | Schwere Fehler | Disk voll |
| **ERROR** | Fehler-Bedingungen | Fehler | Applikations-Fehler |
| **WARNING** | Warnungs-Bedingungen | Warnungen | Disk 80% voll |
| **NOTICE** | Normale aber signifikante Bedingung | Wichtige Events | Service gestartet |
| **INFO** | Informations-Meldungen | Normale Events | User-Login |
| **DEBUG** | Debug-Meldungen | Entwicklung | Funktions-Aufrufe |

## Log-Sammlung und -Aggregation

### Log-Architektur

```
┌─────────────────────────────────────────────────────────┐
│                    Log-Quellen                          │
│  Servers, Network, Applications, Security-Devices       │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ Syslog, Agents, APIs
                     │
┌────────────────────▼────────────────────────────────────┐
│              Log-Collectors/Forwarders                   │
│  Rsyslog, Fluentd, Logstash, Splunk Forwarders         │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ Parsing, Filtering, Enrichment
                     │
┌────────────────────▼────────────────────────────────────┐
│              Log-Aggregation-Platform                    │
│  SIEM, ELK Stack, Splunk, Graylog                       │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────────────────────┐
│ Hot Storage     │    │ Cold Storage / Archive          │
│ (Fast Access)   │    │ (Long-term Retention)           │
└─────────────────┘    └─────────────────────────────────┘
```

### Log-Sammlung-Methoden

#### Syslog

**Protokoll:** RFC 5424 (Syslog Protocol)  
**Transport:** UDP 514 (Standard), TCP 514 (Reliable), TLS 6514 (Secure)

**Vorteile:**
- Standard-Protokoll
- Weit verbreitet
- Einfache Konfiguration

**Nachteile:**
- UDP nicht zuverlässig
- Begrenzte Struktur
- Keine Authentifizierung (ohne TLS)

**Verwendung:** Linux/Unix-Systeme, Netzwerk-Geräte

#### Agent-basiert

**Agents:**
- Splunk Universal Forwarder
- Elastic Beats (Filebeat, Metricbeat)
- Fluentd
- NXLog

**Vorteile:**
- Zuverlässige Übertragung
- Lokale Pufferung
- Parsing und Filtering
- Verschlüsselte Übertragung

**Nachteile:**
- Agent-Installation erforderlich
- Agent-Management
- Ressourcen-Verbrauch

**Verwendung:** Server, Workstations

#### API-basiert

**Methoden:**
- REST APIs
- Cloud-Provider-APIs (AWS CloudWatch, Azure Monitor)
- Webhook-Integration

**Vorteile:**
- Strukturierte Daten
- Echtzeit-Integration
- Keine Agent-Installation

**Nachteile:**
- API-Limits
- Netzwerk-Abhängigkeit
- Komplexere Konfiguration

**Verwendung:** Cloud-Services, SaaS-Applikationen

#### Windows Event Forwarding (WEF)

**Methode:** Windows-native Event-Forwarding

**Vorteile:**
- Keine zusätzlichen Agents
- Zentrale Konfiguration via GPO
- Zuverlässig

**Nachteile:**
- Nur Windows
- Begrenzte Parsing-Optionen

**Verwendung:** Windows-Umgebungen

### Log-Aggregation-Platform

**SIEM-System:** {{ meta-handbook.siem_system }}  
**Version:** [TODO]  
**Management-URL:** {{ meta-handbook.siem_url }}

**Komponenten:**
- **Log-Collectors:** {{ meta-handbook.log_collectors }}
- **Indexer:** {{ meta-handbook.log_indexers }}
- **Search-Heads:** {{ meta-handbook.log_search_heads }}
- **Storage:** {{ meta-handbook.log_storage }}

**Kapazität:**
- **Ingestion-Rate:** {{ meta-handbook.log_ingestion_rate }} GB/Tag
- **Storage-Kapazität:** {{ meta-handbook.log_storage_capacity }} TB
- **Retention (Hot):** {{ meta-handbook.log_retention_hot }} Tage
- **Retention (Cold):** {{ meta-handbook.log_retention_cold }} Tage

### Log-Quellen-Konfiguration

#### Linux-Server

**Rsyslog-Konfiguration:**
```bash
# /etc/rsyslog.d/50-remote.conf

# Alle Logs an zentralen Syslog-Server senden
*.* @@syslog.{{ meta-handbook.domain }}:514

# Nur Security-Logs senden
authpriv.* @@syslog.{{ meta-handbook.domain }}:514

# TLS-verschlüsselt
$DefaultNetstreamDriver gtls
$ActionSendStreamDriverMode 1
$ActionSendStreamDriverAuthMode x509/name
*.* @@syslog.{{ meta-handbook.domain }}:6514
```

#### Windows-Server

**Event-Forwarding-Konfiguration:**
```powershell
# Event-Forwarding aktivieren
wecutil qc

# Subscription erstellen
wecutil cs subscription.xml

# Subscription-XML
<Subscription>
  <SubscriptionId>Security-Events</SubscriptionId>
  <DestinationUrl>http://wec-server.{{ meta-handbook.domain }}:5985/wsman</DestinationUrl>
  <Query>
    <QueryList>
      <Query Id="0">
        <Select Path="Security">*[System[(EventID=4624 or EventID=4625)]]</Select>
      </Query>
    </QueryList>
  </Query>
</Subscription>
```

#### Firewall

**Syslog-Konfiguration:**
- Syslog-Server: [[ netbox.syslog.server ]]
- Facility: Local6
- Severity: Informational und höher
- Format: RFC 5424

**Geloggte Events:**
- Alle erlaubten/blockierten Verbindungen
- Policy-Änderungen
- VPN-Verbindungen
- Admin-Zugriffe

#### Web-Server (Apache)

**Log-Konfiguration:**
```apache
# /etc/apache2/sites-available/default-ssl.conf

# Access-Log
CustomLog /var/log/apache2/access.log combined

# Error-Log
ErrorLog /var/log/apache2/error.log
LogLevel warn

# Forwarding an Syslog
CustomLog "|/usr/bin/logger -t apache -p local6.info" combined
```

#### Datenbank (MySQL)

**Log-Konfiguration:**
```ini
# /etc/mysql/my.cnf

[mysqld]
# General Query Log (nur für Debugging)
general_log = 0
general_log_file = /var/log/mysql/query.log

# Error Log
log_error = /var/log/mysql/error.log

# Slow Query Log
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2

# Audit Plugin (für Compliance)
plugin-load = audit_log.so
audit_log_file = /var/log/mysql/audit.log
audit_log_format = JSON
```

## Log-Retention und -Archivierung

### Retention-Policies

#### Retention nach Log-Typ

| Log-Typ | Hot Storage | Cold Storage | Gesamt | Begründung |
|---|---|---|---|---|
| **Security-Logs** | 90 Tage | 7 Jahre | 7 Jahre | Compliance, Forensik |
| **Audit-Logs** | 90 Tage | 7 Jahre | 7 Jahre | Compliance, Regulierung |
| **System-Logs** | 30 Tage | 1 Jahr | 1 Jahr | Troubleshooting |
| **Application-Logs** | 30 Tage | 1 Jahr | 1 Jahr | Troubleshooting |
| **Network-Logs** | 30 Tage | 1 Jahr | 1 Jahr | Security, Troubleshooting |
| **Web-Access-Logs** | 30 Tage | 6 Monate | 6 Monate | Analytics, Security |
| **Debug-Logs** | 7 Tage | - | 7 Tage | Entwicklung |

#### Retention nach Compliance

**DSGVO:**
- Personenbezogene Daten: Nur so lange wie erforderlich
- Zugriffs-Logs: 6 Monate (empfohlen)
- Security-Logs: 1-2 Jahre

**ISO 27001:**
- Security-Logs: Mindestens 1 Jahr
- Audit-Logs: Mindestens 1 Jahr

**Branchenspezifisch:**
- Finanzsektor: 7-10 Jahre
- Gesundheitswesen: 10 Jahre
- Telekommunikation: 6 Monate (Vorratsdatenspeicherung)

### Storage-Tiers

#### Hot Storage (Schneller Zugriff)

**Technologie:** SSD, NVMe  
**Retention:** 30-90 Tage  
**Zugriff:** Echtzeit-Suche, Dashboards  
**Kosten:** Hoch

**Verwendung:**
- Aktive Monitoring
- Security-Analysen
- Troubleshooting

#### Warm Storage (Mittlerer Zugriff)

**Technologie:** HDD, Object Storage  
**Retention:** 3-12 Monate  
**Zugriff:** Suche (langsamer)  
**Kosten:** Mittel

**Verwendung:**
- Historische Analysen
- Compliance-Audits
- Forensik

#### Cold Storage (Archiv)

**Technologie:** Tape, Cloud Glacier, Object Storage  
**Retention:** 1-7 Jahre  
**Zugriff:** Restore erforderlich (Stunden bis Tage)  
**Kosten:** Niedrig

**Verwendung:**
- Langzeit-Archivierung
- Compliance-Anforderungen
- Rechtliche Aufbewahrung

### Archivierungs-Prozess

**Automatische Archivierung:**
1. Logs älter als Hot-Retention werden komprimiert
2. Komprimierte Logs werden zu Warm/Cold Storage verschoben
3. Metadaten bleiben für Suche verfügbar
4. Originale werden aus Hot Storage gelöscht

**Archiv-Format:**
- Kompression: gzip, bzip2
- Verschlüsselung: AES-256
- Integrität: SHA-256 Checksums
- Metadaten: JSON-Index

**Archiv-Speicherort:** {{ meta-handbook.log_archive_location }}

### Log-Löschung

**Automatische Löschung:**
- Logs älter als Retention-Policy werden automatisch gelöscht
- Löschung wird geloggt (Audit-Trail)
- Checksums vor Löschung verifizieren

**Manuelle Löschung:**
- Nur mit Management-Genehmigung
- Begründung dokumentieren
- Löschungs-Protokoll erstellen

**DSGVO-Löschung:**
- Recht auf Vergessenwerden
- Personenbezogene Daten löschen
- Dokumentation der Löschung

## Log-Analyse und -Monitoring

### SIEM-Integration

**SIEM-System:** {{ meta-handbook.siem_system }}

**Funktionen:**
- **Real-time Monitoring:** Echtzeit-Überwachung
- **Correlation:** Event-Korrelation
- **Alerting:** Automatische Alerts
- **Dashboards:** Visualisierung
- **Reporting:** Compliance-Reports
- **Threat Intelligence:** Integration von Threat-Feeds

### Use-Cases und Correlation-Rules

#### Failed Login Attempts

**Use-Case:** Erkennung von Brute-Force-Angriffen

**Regel:**
```
IF failed_login_count > 5 
   AND time_window = 5 minutes
   AND same_source_ip
THEN alert "Possible Brute-Force Attack"
```

**Severity:** High  
**Response:** Account temporär sperren, IP blockieren

#### Privilege Escalation

**Use-Case:** Erkennung von unautorisierten Privilegien-Änderungen

**Regel:**
```
IF event_type = "privilege_change"
   AND new_privilege = "admin"
   AND user NOT IN admin_group
THEN alert "Unauthorized Privilege Escalation"
```

**Severity:** Critical  
**Response:** Sofortige Untersuchung, Account deaktivieren

#### Data Exfiltration

**Use-Case:** Erkennung von ungewöhnlichen Daten-Transfers

**Regel:**
```
IF data_transfer_size > 1GB
   AND destination = external
   AND time = outside_business_hours
THEN alert "Possible Data Exfiltration"
```

**Severity:** Critical  
**Response:** Verbindung blockieren, Forensik starten

#### Malware Detection

**Use-Case:** Erkennung von Malware-Aktivitäten

**Regel:**
```
IF antivirus_alert = "malware_detected"
   OR process_name IN malware_indicators
   OR network_connection TO known_c2_server
THEN alert "Malware Detected"
```

**Severity:** Critical  
**Response:** Host isolieren, Incident-Response

#### Configuration Changes

**Use-Case:** Überwachung von kritischen Konfigurations-Änderungen

**Regel:**
```
IF event_type = "config_change"
   AND system IN critical_systems
   AND user NOT IN authorized_admins
THEN alert "Unauthorized Configuration Change"
```

**Severity:** High  
**Response:** Change verifizieren, ggf. rollback

### Dashboards

#### Security-Dashboard

**Metriken:**
- Failed Login Attempts (letzte 24h)
- Security-Alerts (nach Severity)
- Top-10-Angreifer-IPs
- Malware-Detections
- Firewall-Blocks

**Zielgruppe:** Security-Operations-Team

#### Operations-Dashboard

**Metriken:**
- System-Errors (nach System)
- Application-Errors (nach App)
- Performance-Metriken
- Disk-Space-Warnungen
- Service-Verfügbarkeit

**Zielgruppe:** IT-Operations-Team

#### Compliance-Dashboard

**Metriken:**
- Audit-Log-Coverage
- Retention-Compliance
- Access-Reviews
- Policy-Violations
- Privileged-Access-Monitoring

**Zielgruppe:** Compliance-Officer, Auditoren

### Alerting

**Alert-Kanäle:**
- **E-Mail:** {{ meta-handbook.alert_email }}
- **SMS:** Für kritische Alerts
- **Ticketing:** {{ meta-handbook.ticketing_system }}
- **SIEM-Console:** Real-time Alerts
- **Slack/Teams:** Team-Benachrichtigungen

**Alert-Priorisierung:**

| Severity | Response-Zeit | Eskalation | Beispiel |
|---|---|---|---|
| **Critical** | Sofort | Sofort an On-Call | Malware, Data Breach |
| **High** | < 1 Stunde | Nach 1h | Failed Logins, Privilege Escalation |
| **Medium** | < 4 Stunden | Nach 4h | Config Changes, Policy Violations |
| **Low** | < 24 Stunden | Nach 24h | Informational Events |

**Alert-Tuning:**
- False-Positive-Reduktion
- Threshold-Anpassung
- Whitelist für legitime Aktivitäten
- Regelmäßige Review (monatlich)

## Audit-Trail-Anforderungen

### Audit-Logging-Prinzipien

**Was wird geloggt:**
- **Wer:** User-ID, IP-Adresse, Session-ID
- **Was:** Aktion, Ressource, Änderungen
- **Wann:** Timestamp (UTC)
- **Wo:** System, Applikation, Komponente
- **Ergebnis:** Erfolg/Fehler, Fehlercode

**Audit-Log-Format:**
```json
{
  "timestamp": "2024-01-31T10:30:45Z",
  "user": "jdoe",
  "source_ip": "192.168.1.100",
  "action": "file_access",
  "resource": "/data/sensitive/customer_data.csv",
  "result": "success",
  "system": "fileserver01",
  "session_id": "abc123xyz"
}
```

### Kritische Audit-Events

#### Authentifizierung und Autorisierung

**Events:**
- Login (erfolgreich/fehlgeschlagen)
- Logout
- Passwort-Änderung
- Account-Erstellung/-Löschung
- Privilegien-Änderung
- Rollen-Zuweisung

#### Daten-Zugriff

**Events:**
- Zugriff auf sensible Daten
- Daten-Export
- Daten-Änderung
- Daten-Löschung
- Datenbank-Queries (bei sensiblen Daten)

#### System-Änderungen

**Events:**
- Konfigurations-Änderungen
- Software-Installation/-Deinstallation
- Service-Start/-Stop
- Firewall-Regel-Änderungen
- Netzwerk-Änderungen

#### Administrative Aktivitäten

**Events:**
- Privilegierte Zugriffe
- Backup/Restore-Operationen
- Security-Policy-Änderungen
- Audit-Log-Zugriffe
- System-Wartung

### Audit-Log-Integrität

**Schutzmaßnahmen:**
- **Write-Once:** Logs können nicht geändert werden
- **Digitale Signaturen:** Logs werden signiert
- **Checksums:** Integritäts-Prüfung
- **Separate Storage:** Logs auf separatem System
- **Access-Control:** Nur autorisierte Zugriffe

**Verifikation:**
- Regelmäßige Integritäts-Checks
- Checksum-Validierung
- Signatur-Verifikation
- Anomalie-Erkennung (fehlende Logs)

## Compliance und Regulierung

### DSGVO (GDPR)

**Anforderungen:**
- Logging von Zugriff auf personenbezogene Daten
- Recht auf Auskunft (welche Daten wurden verarbeitet)
- Recht auf Löschung (Logs mit personenbezogenen Daten)
- Meldepflicht bei Data Breach (72h)

**Umsetzung:**
- Zugriffs-Logs für alle personenbezogenen Daten
- Pseudonymisierung wo möglich
- Retention-Policies beachten
- Lösch-Prozesse implementiert

### ISO 27001

**Anforderungen:**
- A.12.4.1: Event-Logging
- A.12.4.2: Schutz von Log-Informationen
- A.12.4.3: Administrator- und Operator-Logs
- A.12.4.4: Zeitsynchronisation

**Umsetzung:**
- Umfassendes Event-Logging
- Log-Integrität sichergestellt
- Privilegierte Zugriffe geloggt
- NTP-Synchronisation

### PCI-DSS (falls zutreffend)

**Anforderungen:**
- Requirement 10: Track and monitor all access to network resources and cardholder data
- Audit-Trails für alle Zugriffe
- Tägliche Log-Reviews
- Retention: Mindestens 1 Jahr (3 Monate online)

### SOX (falls zutreffend)

**Anforderungen:**
- Audit-Trails für finanzrelevante Systeme
- Änderungs-Nachvollziehbarkeit
- Access-Controls geloggt
- Retention: 7 Jahre

## Log-Management-Tools

### SIEM-Platform

**System:** {{ meta-handbook.siem_system }}  
**Komponenten:**
- Indexer
- Search-Heads
- Forwarders
- Deployment-Server

### Log-Collectors

**Rsyslog:**
- Zentrale Syslog-Server
- Filtering und Parsing
- Forwarding an SIEM

**Fluentd/Fluent Bit:**
- Lightweight Log-Collector
- Plugin-basiert
- Kubernetes-Integration

**Elastic Beats:**
- Filebeat: Log-Files
- Metricbeat: System-Metriken
- Packetbeat: Network-Traffic
- Auditbeat: Audit-Daten

### Log-Analysis-Tools

**Kibana:**
- Visualisierung
- Dashboards
- Ad-hoc-Queries

**Grafana:**
- Metriken-Visualisierung
- Alerting
- Multi-Source-Integration

## Rollen und Verantwortlichkeiten

### Log-Management-Team

**Verantwortlichkeiten:**
- Log-Infrastruktur-Verwaltung
- Log-Sammlung-Konfiguration
- Retention-Policy-Umsetzung
- Tool-Administration

**Team-Lead:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

### Security-Operations-Team

**Verantwortlichkeiten:**
- SIEM-Monitoring
- Alert-Response
- Use-Case-Entwicklung
- Threat-Hunting

**Team-Lead:** [TODO]

### Compliance-Officer

**Verantwortlichkeiten:**
- Compliance-Anforderungen definieren
- Audit-Unterstützung
- Retention-Policy-Review
- Regulierungs-Überwachung

**Person:** [TODO]

## Metriken und Reporting

### Log-Management-Metriken

| Metrik | Zielwert | Messung |
|---|---|---|
| **Log-Collection-Rate** | > 99% | Gesammelte Logs / Erwartete Logs |
| **Log-Ingestion-Latency** | < 5 Min | Zeit von Event bis SIEM |
| **Storage-Utilization** | < 80% | Verwendeter Storage / Gesamt-Storage |
| **Alert-Response-Time** | < 15 Min | Zeit von Alert bis Response |
| **False-Positive-Rate** | < 10% | False Positives / Gesamt-Alerts |

### Reporting

**Tägliches Log-Status-Report:**
- Log-Collection-Status
- Fehlende Log-Quellen
- Storage-Auslastung
- Kritische Alerts

**Wöchentliches Security-Report:**
- Security-Events-Zusammenfassung
- Top-Alerts
- Trend-Analysen
- Anomalien

**Monatliches Compliance-Report:**
- Audit-Log-Coverage
- Retention-Compliance
- Access-Reviews
- Policy-Violations

**Quartalsweises Management-Report:**
- Log-Management-Strategie-Review
- Kapazitäts-Planung
- Compliance-Status
- Verbesserungs-Maßnahmen

## Referenzen

- ISO/IEC 27001:2013 - A.12.4 (Logging and Monitoring)
- NIST SP 800-92 - Guide to Computer Security Log Management
- PCI-DSS v4.0 - Requirement 10
- DSGVO - Artikel 30 (Verzeichnis von Verarbeitungstätigkeiten)
- CIS Controls v8 - Control 8 (Audit Log Management)
- ITIL v4 - Monitoring and Event Management

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Klassifizierung:** Internal  
**Letzte Aktualisierung:** {{ meta-handbook.date }}

