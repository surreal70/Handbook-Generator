# Incident Management Runbook

## Zweck und Geltungsbereich

Dieses Dokument beschreibt den Incident-Management-Prozess für {{ meta.organization.name }} gemäß ITIL v4 Best Practices. Es definiert Kategorien, Prioritäten, Eskalationsprozesse und Standard-Runbooks für die Behandlung von Service-Störungen.

**Geltungsbereich:** Alle IT-Services und -Systeme von {{ meta.organization.name }}

**Verantwortlich:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})

## Incident-Definition

Ein **Incident** ist eine ungeplante Unterbrechung oder Qualitätsminderung eines IT-Service. Das Ziel des Incident Managements ist die schnellstmögliche Wiederherstellung des normalen Service-Betriebs.

### Abgrenzung zu anderen Prozessen

| Prozess | Fokus | Ziel |
|---|---|---|
| **Incident Management** | Symptombehandlung | Schnelle Wiederherstellung |
| **Problem Management** | Ursachenanalyse | Dauerhafte Lösung |
| **Change Management** | Geplante Änderungen | Kontrollierte Implementierung |
| **Service Request** | Standardanfragen | Erfüllung von Anforderungen |

## Incident-Kategorien

### Kategorisierung nach Bereich

| Kategorie | Beschreibung | Beispiele |
|---|---|---|
| **Hardware** | Physische Geräte und Komponenten | Server-Ausfall, Festplatten-Defekt, Netzwerk-Hardware |
| **Software** | Anwendungen und Betriebssysteme | Applikations-Crash, Lizenz-Probleme, Software-Bugs |
| **Netzwerk** | Netzwerkverbindungen und -dienste | Verbindungsabbrüche, DNS-Probleme, Firewall-Blockaden |
| **Security** | Sicherheitsvorfälle | Malware, Unauthorized Access, Data Breach |
| **Performance** | Leistungsprobleme | Langsame Antwortzeiten, Hohe CPU-Last, Memory Leaks |
| **Daten** | Datenverlust oder -korruption | Datenbank-Korruption, Backup-Fehler, Datenverlust |
| **Benutzer** | Zugriffs- und Berechtigungsprobleme | Login-Probleme, Passwort-Reset, Fehlende Berechtigungen |

### Kategorisierung nach Service

- **E-Mail-Service**
- **File-Server**
- **Datenbank-Service**
- **Web-Applikationen**
- **Netzwerk-Infrastruktur**
- **Backup-Systeme**
- **Monitoring-Systeme**
- **[Weitere Services gemäß Service-Katalog]**

## Incident-Prioritäten

Die Priorität eines Incidents ergibt sich aus **Impact** (Auswirkung) und **Urgency** (Dringlichkeit).

### Impact-Bewertung

| Impact | Beschreibung | Betroffene Nutzer |
|---|---|---|
| **Hoch** | Kritischer Service komplett ausgefallen | > 50% der Nutzer oder geschäftskritischer Service |
| **Mittel** | Service eingeschränkt verfügbar | 10-50% der Nutzer oder wichtiger Service |
| **Niedrig** | Einzelne Nutzer betroffen | < 10% der Nutzer oder unkritischer Service |

### Urgency-Bewertung

| Urgency | Beschreibung | Zeitfenster |
|---|---|---|
| **Hoch** | Sofortige Bearbeitung erforderlich | Geschäftsprozess blockiert |
| **Mittel** | Zeitnahe Bearbeitung erforderlich | Geschäftsprozess beeinträchtigt |
| **Niedrig** | Kann geplant bearbeitet werden | Keine unmittelbare Auswirkung |

### Prioritäts-Matrix

|  | **Urgency: Hoch** | **Urgency: Mittel** | **Urgency: Niedrig** |
|---|---|---|---|
| **Impact: Hoch** | **P1 - Kritisch** | **P2 - Hoch** | **P3 - Mittel** |
| **Impact: Mittel** | **P2 - Hoch** | **P3 - Mittel** | **P4 - Niedrig** |
| **Impact: Niedrig** | **P3 - Mittel** | **P4 - Niedrig** | **P5 - Geplant** |

### Service Level Targets

| Priorität | Reaktionszeit | Lösungszeit | Eskalation nach |
|---|---|---|---|
| **P1 - Kritisch** | 15 Minuten | 4 Stunden | 1 Stunde |
| **P2 - Hoch** | 30 Minuten | 8 Stunden | 2 Stunden |
| **P3 - Mittel** | 2 Stunden | 24 Stunden | 8 Stunden |
| **P4 - Niedrig** | 4 Stunden | 48 Stunden | 24 Stunden |
| **P5 - Geplant** | 1 Arbeitstag | 5 Arbeitstage | - |

## Incident-Management-Prozess

### Prozessübersicht (ITIL v4)

```
┌─────────────────┐
│ Incident        │
│ Detection       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Incident        │
│ Logging         │
└────────┬────────┘
         │
┌────────▼────────┐
│ Categorization  │
│ & Prioritization│
└────────┬────────┘
         │
┌────────▼────────┐
│ Initial         │
│ Diagnosis       │
└────────┬────────┘
         │
    ┌────▼────┐
    │ Known   │ Yes ┌──────────────┐
    │ Error?  ├────►│ Apply        │
    └────┬────┘     │ Workaround   │
         │ No       └──────────────┘
         │
┌────────▼────────┐
│ Investigation   │
│ & Diagnosis     │
└────────┬────────┘
         │
┌────────▼────────┐
│ Resolution      │
│ & Recovery      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Incident        │
│ Closure         │
└─────────────────┘
```

### 1. Incident Detection

**Erkennungsquellen:**
- Monitoring-Alerts ({{ netbox.monitoring_system }})
- Service Desk Tickets
- Benutzer-Meldungen
- Automatische Event-Korrelation

**Verantwortlich:** Monitoring-System, Service Desk

### 2. Incident Logging

**Erforderliche Informationen:**
- Incident-ID (automatisch generiert)
- Zeitstempel der Meldung
- Betroffener Service/System
- Symptombeschreibung
- Betroffene Nutzer/Standorte
- Melder (Name, Kontakt)

**Tool:** {{ meta.ticketing_system }}

**Verantwortlich:** Service Desk

### 3. Categorization & Prioritization

**Aktivitäten:**
- Kategorie zuweisen (Hardware, Software, Netzwerk, etc.)
- Impact bewerten
- Urgency bewerten
- Priorität berechnen (P1-P5)
- Betroffenen Service identifizieren

**Verantwortlich:** Service Desk / Incident Manager

### 4. Initial Diagnosis

**Aktivitäten:**
- Symptome analysieren
- Logs prüfen
- Monitoring-Daten auswerten
- Known Error Database durchsuchen
- Erste Lösungsversuche (Level 1)

**Verantwortlich:** Service Desk (Level 1)

### 5. Investigation & Diagnosis

**Aktivitäten:**
- Detaillierte technische Analyse
- Root-Cause-Identifikation (wenn möglich)
- Workaround-Entwicklung
- Eskalation an Spezialisten (Level 2/3)

**Verantwortlich:** IT Operations Team (Level 2/3)

### 6. Resolution & Recovery

**Aktivitäten:**
- Lösung implementieren
- Service wiederherstellen
- Funktionalität testen
- Nutzer informieren

**Verantwortlich:** IT Operations Team

### 7. Incident Closure

**Aktivitäten:**
- Nutzer-Bestätigung einholen
- Dokumentation vervollständigen
- Incident schließen
- Ggf. Problem-Ticket erstellen

**Verantwortlich:** Service Desk

## Eskalationsprozesse

### Hierarchische Eskalation

| Level | Rolle | Kontakt | Eskalation bei |
|---|---|---|---|
| **Level 1** | Service Desk | {{ meta.service_desk_lead.email }} | Standard-Incidents |
| **Level 2** | IT Operations Team | {{ meta.it_operations_manager.email }} | Komplexe technische Probleme |
| **Level 3** | Spezialisten / Vendor | [Vendor-Kontakte] | Spezialwissen erforderlich |
| **Management** | CIO | {{ meta.cio.email }} | P1-Incidents > 2h |

### Funktionale Eskalation

| Bereich | Ansprechpartner | Kontakt | Zuständigkeit |
|---|---|---|---|
| **Netzwerk** | Network Team | [E-Mail] | Netzwerk-Infrastruktur |
| **Server** | Server Team | [E-Mail] | Server und Virtualisierung |
| **Datenbank** | DBA Team | [E-Mail] | Datenbank-Systeme |
| **Security** | Security Team | {{ meta.ciso.email }} | Sicherheitsvorfälle |
| **Applikationen** | Application Team | [E-Mail] | Business-Applikationen |

### Eskalations-Trigger

**Automatische Eskalation bei:**
- P1-Incident nicht gelöst nach 1 Stunde
- P2-Incident nicht gelöst nach 2 Stunden
- P3-Incident nicht gelöst nach 8 Stunden
- Mehrfache Wiederöffnung desselben Incidents
- Security-Incidents (sofort an CISO)

**Management-Eskalation bei:**
- P1-Incidents (Information an CIO)
- Incidents mit hoher Medienaufmerksamkeit
- Incidents mit rechtlichen Implikationen
- Mehrere gleichzeitige P1/P2-Incidents

## Standard-Runbooks

### Runbook 1: Server nicht erreichbar

**Symptome:** Server antwortet nicht auf Ping, Services nicht verfügbar

**Priorität:** P1 oder P2 (abhängig von Service-Kritikalität)

**Diagnose-Schritte:**
1. Ping-Test durchführen: `ping {{ netbox.server.ip }}`
2. Monitoring-Dashboard prüfen
3. Physischen Zustand prüfen (falls vor Ort)
4. Netzwerk-Konnektivität prüfen
5. Hypervisor-Status prüfen (bei VMs)

**Lösungsschritte:**
1. Netzwerk-Verbindung wiederherstellen (falls Netzwerk-Problem)
2. Server-Neustart durchführen (falls hängend)
3. Hypervisor-Migration durchführen (bei VM-Problem)
4. Hardware-Austausch initiieren (bei Hardware-Defekt)
5. Backup-System aktivieren (falls primäres System defekt)

**Eskalation:** Nach 30 Minuten an Level 2, nach 1 Stunde an Management

### Runbook 2: Applikation langsam / nicht erreichbar

**Symptome:** Lange Antwortzeiten, Timeouts, HTTP 500/503 Fehler

**Priorität:** P2 oder P3

**Diagnose-Schritte:**
1. Applikations-Logs prüfen
2. Performance-Metriken analysieren (CPU, RAM, Disk I/O)
3. Datenbank-Performance prüfen
4. Netzwerk-Latenz messen
5. Load-Balancer-Status prüfen

**Lösungsschritte:**
1. Applikations-Neustart durchführen
2. Cache leeren
3. Datenbank-Queries optimieren
4. Ressourcen skalieren (CPU/RAM erhöhen)
5. Traffic auf andere Instanzen umleiten

**Eskalation:** Nach 2 Stunden an Application Team

### Runbook 3: Datenbank-Verbindungsfehler

**Symptome:** Connection timeout, "Too many connections", Applikation kann nicht auf DB zugreifen

**Priorität:** P1 oder P2

**Diagnose-Schritte:**
1. Datenbank-Status prüfen: `systemctl status postgresql`
2. Connection-Pool prüfen
3. Datenbank-Logs analysieren
4. Disk-Space prüfen
5. Netzwerk-Konnektivität zur DB prüfen

**Lösungsschritte:**
1. Datenbank-Service neu starten
2. Connection-Pool-Limits erhöhen
3. Lange laufende Queries beenden
4. Disk-Space freigeben
5. Failover zu Standby-Datenbank

**Eskalation:** Sofort an DBA Team bei P1

### Runbook 4: Backup fehlgeschlagen

**Symptome:** Backup-Job meldet Fehler, Backup-Monitoring-Alert

**Priorität:** P2 oder P3

**Diagnose-Schritte:**
1. Backup-Logs prüfen
2. Disk-Space auf Backup-Target prüfen
3. Netzwerk-Verbindung zu Backup-Storage prüfen
4. Backup-Software-Status prüfen
5. Quell-System-Status prüfen

**Lösungsschritte:**
1. Backup-Job manuell neu starten
2. Disk-Space auf Backup-Target freigeben
3. Netzwerk-Verbindung wiederherstellen
4. Backup-Software neu starten
5. Alternative Backup-Methode verwenden

**Eskalation:** Nach 4 Stunden an Backup-Team

### Runbook 5: Security-Incident (Malware/Intrusion)

**Symptome:** Malware-Alert, ungewöhnliche Netzwerk-Aktivität, Unauthorized Access

**Priorität:** P1 (immer)

**Diagnose-Schritte:**
1. Alert-Details analysieren
2. Betroffene Systeme identifizieren
3. Ausmaß der Kompromittierung bewerten
4. Logs sichern (Forensik)
5. CISO informieren

**Lösungsschritte:**
1. Betroffene Systeme isolieren (Netzwerk-Trennung)
2. Malware-Scan durchführen
3. Kompromittierte Accounts sperren
4. Passwörter zurücksetzen
5. Forensische Analyse durchführen
6. Systeme neu aufsetzen (falls erforderlich)

**Eskalation:** Sofort an CISO ({{ meta.ciso.email }})

### Runbook 6: Netzwerk-Ausfall

**Symptome:** Keine Netzwerk-Konnektivität, Geräte nicht erreichbar

**Priorität:** P1 oder P2

**Diagnose-Schritte:**
1. Betroffene Netzwerk-Segmente identifizieren
2. Switch/Router-Status prüfen
3. Physische Verkabelung prüfen
4. VLAN-Konfiguration prüfen
5. Routing-Tabellen prüfen

**Lösungsschritte:**
1. Netzwerk-Geräte neu starten
2. Defekte Kabel austauschen
3. VLAN-Konfiguration korrigieren
4. Routing-Probleme beheben
5. Failover zu Backup-Verbindung

**Eskalation:** Nach 30 Minuten an Network Team

## Kommunikationsprozesse

### Interne Kommunikation

**Bei Incident-Eröffnung:**
- Service Desk informiert betroffene Nutzer
- IT Operations Team wird bei P1/P2 sofort informiert
- Management wird bei P1 informiert

**Während der Bearbeitung:**
- Regelmäßige Status-Updates (P1: alle 30 Min, P2: alle 2h)
- Eskalations-Benachrichtigungen
- Team-Kommunikation über {{ meta.collaboration_tool }}

**Bei Incident-Lösung:**
- Nutzer-Benachrichtigung über Lösung
- Management-Information bei P1/P2
- Dokumentation im Ticket-System

### Externe Kommunikation

**Stakeholder-Information:**
- Geschäftsführung bei kritischen Incidents
- Kunden bei Service-Ausfällen
- Externe Partner bei Abhängigkeiten

**Kommunikationskanäle:**
- E-Mail: {{ meta.organization.email }}
- Status-Page: {{ meta.status_page_url }}
- Telefon: {{ meta.organization.phone }}

**Kommunikations-Template:**

```
Betreff: [P1/P2] Service-Störung: [Service-Name]

Sehr geehrte Damen und Herren,

wir informieren Sie über eine aktuelle Service-Störung:

Service: [Service-Name]
Priorität: [P1/P2/P3]
Beginn: [Zeitstempel]
Auswirkung: [Beschreibung]
Status: [In Bearbeitung / Gelöst]

Wir arbeiten mit Hochdruck an der Lösung und halten Sie auf dem Laufenden.

Nächstes Update: [Zeitpunkt]

Mit freundlichen Grüßen
{{ meta.organization.name }}
IT Operations Team
```

## Major Incident Management

### Definition Major Incident

Ein **Major Incident** ist ein Incident mit:
- Priorität P1
- Auswirkung auf kritische Geschäftsprozesse
- Hohe Anzahl betroffener Nutzer (> 50%)
- Potenzielle finanzielle oder rechtliche Konsequenzen

### Major Incident Team

| Rolle | Person | Verantwortung |
|---|---|---|
| **Incident Manager** | {{ meta.it_operations_manager.name }} | Koordination und Kommunikation |
| **Technical Lead** | [Name] | Technische Lösungsfindung |
| **Communication Lead** | [Name] | Stakeholder-Kommunikation |
| **Management Rep** | {{ meta.cio.name }} | Entscheidungen und Eskalation |

### Major Incident Prozess

1. **Incident Declaration:** Incident Manager erklärt Major Incident
2. **Team Assembly:** Major Incident Team wird zusammengerufen
3. **War Room:** Dedizierter Kommunikationskanal (z.B. Conference Call)
4. **Status Updates:** Alle 30 Minuten an Stakeholder
5. **Resolution:** Koordinierte Lösungsumsetzung
6. **Post-Incident Review:** Pflicht-Postmortem innerhalb 48h

## Metriken und Reporting

### Key Performance Indicators (KPIs)

| Metrik | Zielwert | Messung |
|---|---|---|
| **Mean Time to Respond (MTTR)** | < 15 Min (P1) | Durchschnittliche Reaktionszeit |
| **Mean Time to Resolve (MTTR)** | < 4h (P1) | Durchschnittliche Lösungszeit |
| **First Call Resolution Rate** | > 70% | Lösung beim ersten Kontakt |
| **Incident Reopen Rate** | < 5% | Wiederöffnungsrate |
| **SLA Compliance** | > 95% | Einhaltung der SLA-Zeiten |

### Reporting

**Tägliches Reporting:**
- Anzahl offener Incidents (nach Priorität)
- P1/P2 Incidents in Bearbeitung
- SLA-Verstöße

**Wöchentliches Reporting:**
- Incident-Trend-Analyse
- Top-5 Incident-Kategorien
- Eskalations-Statistik

**Monatliches Reporting:**
- KPI-Dashboard
- Service-Verfügbarkeit
- Verbesserungsmaßnahmen

## Tools und Systeme

### Incident-Management-Tool
- **System:** {{ meta.ticketing_system }}
- **URL:** {{ meta.ticketing_system_url }}
- **Zugriff:** Alle IT-Mitarbeiter

### Monitoring-System
- **System:** {{ netbox.monitoring_system }}
- **URL:** {{ meta.monitoring_url }}
- **Zugriff:** IT Operations Team

### Kommunikations-Tools
- **Chat:** {{ meta.collaboration_tool }}
- **Conference:** {{ meta.conference_system }}
- **Status-Page:** {{ meta.status_page_url }}

## Anhang

### Incident-Kategorien (vollständig)

- Hardware > Server
- Hardware > Storage
- Hardware > Network
- Software > Operating System
- Software > Application
- Software > Database
- Network > Connectivity
- Network > Performance
- Security > Malware
- Security > Unauthorized Access
- Security > Data Breach
- Performance > Slow Response
- Performance > High Load
- Data > Corruption
- Data > Loss
- User > Access
- User > Authentication

### Kontakte und Rufbereitschaft

| Team | Primär | Sekundär | Rufbereitschaft |
|---|---|---|---|
| **Service Desk** | {{ meta.service_desk_lead.email }} | [Backup] | 24/7 |
| **IT Operations** | {{ meta.it_operations_manager.email }} | [Backup] | 24/7 |
| **Network Team** | [E-Mail] | [Backup] | On-Call |
| **Security Team** | {{ meta.ciso.email }} | [Backup] | 24/7 |

### Referenzen

- ITIL v4 Foundation
- ISO/IEC 20000-1:2018 - Service Management
- Interne Service-Level-Agreements
- Eskalations-Matrix

---

**Dokumentverantwortlicher:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
