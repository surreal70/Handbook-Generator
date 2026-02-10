# Service-Beschreibung: E-Mail-Service

> **Hinweis:** Dies ist ein individualisiertes Service-Template basierend auf dem generischen Service-Beschreibungs-Template.

## Service-Übersicht

### Basis-Informationen
- **Service-Name:** E-Mail-Service (Microsoft Exchange Online)
- **Service-ID:** SVC-EMAIL-001
- **Service-Owner:** {{ meta.it_operations_manager.name }}
- **Technischer Ansprechpartner:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})
- **Version:** {{ meta.document.version }}
- **Letzte Aktualisierung:** 2026-01-31

### Kurzbeschreibung
Der E-Mail-Service stellt allen Mitarbeitern von {{ meta.organization.name }} eine professionelle E-Mail-Kommunikationsplattform basierend auf Microsoft Exchange Online zur Verfügung. Der Service umfasst E-Mail, Kalender, Kontakte und Aufgabenverwaltung.

### Geschäftszweck
Der E-Mail-Service ermöglicht die interne und externe geschäftliche Kommunikation, unterstützt die Zusammenarbeit zwischen Teams und ist essentiell für die tägliche Geschäftstätigkeit. Der Service gewährleistet sichere, zuverlässige und compliance-konforme E-Mail-Kommunikation.

### Nutzergruppen
- Alle Mitarbeiter (ca. 250 Benutzer)
- Externe Partner mit Gastzugang (ca. 20 Benutzer)
- Service-Accounts für automatisierte Prozesse (ca. 15 Accounts)

## Technische Details

### Systemkomponenten
| Komponente | Typ | Standort | Verantwortlich |
|---|---|---|---|
| Exchange Online | Cloud Service | Microsoft Azure (EU West) | {{ meta.it_operations_manager.name }} |
| Exchange Hybrid Connector | On-Premise Gateway | {{ meta.organization.city }} Datacenter | {{ meta.it_operations_manager.name }} |
| Mail Gateway (Barracuda) | Security Appliance | {{ meta.organization.city }} Datacenter | {{ meta.ciso.name }} |
| Backup Solution (Veeam) | Backup Service | Cloud Storage | {{ meta.it_operations_manager.name }} |

### Abhängigkeiten

#### Upstream-Abhängigkeiten (Services, von denen dieser Service abhängt)
- Active Directory / Azure AD (Authentifizierung)
- Internet-Anbindung (Konnektivität zu Microsoft 365)
- DNS-Service (MX-Records, SPF, DKIM, DMARC)
- Firewall-Service (Port 25, 587, 993, 995, 443)

#### Downstream-Abhängigkeiten (Services, die von diesem Service abhängen)
- Ticketing-System (E-Mail-Benachrichtigungen)
- Monitoring-System (Alert-Versand)
- CRM-System (E-Mail-Integration)
- Workflow-Automation (E-Mail-Trigger)

### Schnittstellen
| Schnittstelle | Typ | Protokoll | Port | Beschreibung |
|---|---|---|---|---|
| SMTP Inbound | Eingehend | SMTP/TLS | 25 | Empfang externer E-Mails |
| SMTP Outbound | Ausgehend | SMTP/TLS | 587 | Versand externer E-Mails |
| IMAP | Client-Zugriff | IMAP/SSL | 993 | E-Mail-Abruf (Legacy) |
| POP3 | Client-Zugriff | POP3/SSL | 995 | E-Mail-Abruf (Legacy) |
| HTTPS/EWS | Client-Zugriff | HTTPS | 443 | Exchange Web Services |
| HTTPS/OWA | Web-Zugriff | HTTPS | 443 | Outlook Web App |
| HTTPS/ActiveSync | Mobile-Zugriff | HTTPS | 443 | Mobile Geräte |

## Betrieb

### Servicezeiten
- **Verfügbarkeit:** 24/7 (Rund um die Uhr)
- **Support-Zeiten:** Mo-Fr 08:00-18:00 Uhr (CET)
- **Wartungsfenster:** Sonntag 02:00-06:00 Uhr (monatlich, nach Ankündigung)

### Service Level Agreements (SLA)

| Kennzahl | Zielwert | Messmethode |
|---|---:|---|
| Verfügbarkeit | 99.9% | Microsoft 365 Service Health Dashboard |
| E-Mail-Zustellung (intern) | < 1 min | Exchange Message Tracking |
| E-Mail-Zustellung (extern) | < 5 min | SMTP Queue Monitoring |
| MTTR (Mean Time To Repair) | < 4 h | Incident Tracking System |
| MTBF (Mean Time Between Failures) | > 720 h | Service Availability Reports |

### Kritikalität

| Dimension | Einstufung | Begründung |
|---|---|---|
| Verfügbarkeit | ☑ hoch | Geschäftskritisch für tägliche Kommunikation |
| Integrität | ☑ hoch | E-Mails müssen vollständig und unverändert zugestellt werden |
| Vertraulichkeit | ☑ hoch | Enthält vertrauliche Geschäftsinformationen |

## Monitoring und Alerting

### Monitoring-Metriken
- **Service Verfügbarkeit:** Microsoft 365 Service Health Status (Ziel: 99.9%)
- **Mail Queue Länge:** SMTP Queue Monitoring (Schwellwert: > 100 Nachrichten)
- **Zustellrate:** Erfolgreiche vs. fehlgeschlagene Zustellungen (Ziel: > 99%)
- **Spam-Erkennungsrate:** Blockierte Spam-Nachrichten (Ziel: > 95%)
- **Mailbox-Auslastung:** Speicherplatznutzung pro Mailbox (Warnung bei > 80%)

### Alerting-Regeln
| Alert | Schwellwert | Priorität | Eskalation |
|---|---|---|---|
| Service Unavailable | Microsoft 365 Status: Down | P1 - Critical | Sofort an {{ meta.it_operations_manager.name }} |
| Mail Queue Stau | > 100 Nachrichten für > 15 min | P2 - High | Nach 15 min an {{ meta.it_operations_manager.name }} |
| Spam-Welle | > 1000 Spam-Mails in 5 min | P2 - High | Nach 5 min an {{ meta.ciso.name }} |
| Mailbox voll | Mailbox > 95% voll | P3 - Medium | Täglicher Report an Service Desk |

### Dashboards
- Microsoft 365 Admin Center: https://admin.microsoft.com
- Exchange Admin Center: https://admin.exchange.microsoft.com
- Barracuda Mail Gateway Dashboard: https://mail-gateway.{{ meta.organization.name }}
- Monitoring Dashboard (Grafana): https://monitoring.{{ meta.organization.name }}/email-service

## Backup und Recovery

### Backup-Strategie
- **Backup-Typ:** Incremental (täglich) + Full (wöchentlich)
- **Backup-Frequenz:** Täglich um 02:00 Uhr
- **Aufbewahrungsdauer:** 30 Tage (täglich), 12 Monate (wöchentlich)
- **Backup-Speicherort:** Veeam Cloud Storage (EU Region)

### Recovery-Ziele
- **RTO (Recovery Time Objective):** 4 Stunden
- **RPO (Recovery Point Objective):** 24 Stunden

### Restore-Prozeduren
1. **Einzelne E-Mail wiederherstellen:** Über Veeam Backup Portal (Self-Service für Benutzer)
2. **Mailbox wiederherstellen:** Ticket an {{ meta.it_operations_manager.email }}, Bearbeitungszeit < 2 Stunden
3. **Kompletter Service-Restore:** Eskalation an Microsoft Support + Veeam Restore, Bearbeitungszeit < 4 Stunden

## Sicherheit

### Zugriffskontrolle
- **Authentifizierung:** Azure AD mit Multi-Factor Authentication (MFA)
- **Autorisierung:** Role-Based Access Control (RBAC)
- **Berechtigte Gruppen:** 
  - Alle Mitarbeiter (Standard-Zugriff)
  - IT-Operations-Team (Admin-Zugriff)
  - Security-Team (Audit-Zugriff)

### Compliance-Anforderungen
- **DSGVO:** Datenschutz-Folgenabschätzung durchgeführt, Datenverarbeitung in EU
- **ISO 27001:** E-Mail-Verschlüsselung (TLS), Zugriffskontrolle, Audit-Logging
- **Archivierung:** Gesetzliche Aufbewahrungspflicht 10 Jahre (GoBD)

### Sicherheitsmaßnahmen
- **Verschlüsselung:** TLS 1.2+ für Transport, BitLocker für Daten at Rest
- **Anti-Spam:** Barracuda Mail Gateway mit Machine Learning
- **Anti-Malware:** Microsoft Defender for Office 365
- **DLP (Data Loss Prevention):** Microsoft 365 DLP Policies
- **E-Mail-Signierung:** S/MIME für vertrauliche Kommunikation

## Kontakte und Eskalation

### Verantwortlichkeiten
- **Service Owner:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})
- **Technical Lead:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.phone }})
- **Security Contact:** {{ meta.ciso.name }} ({{ meta.ciso.email }})
- **On-Call:** {{ meta.service_desk_lead.name }} ({{ meta.service_desk_lead.phone }})

### Eskalationspfad
1. **Level 1:** Service Desk - {{ meta.service_desk_lead.email }} (Mo-Fr 08:00-18:00)
2. **Level 2:** IT Operations - {{ meta.it_operations_manager.email }} (24/7 On-Call)
3. **Level 3:** CIO - {{ meta.cio.email }} (Geschäftskritische Eskalation)
4. **Level 4:** Microsoft Support - Premier Support Contract (24/7)

### Externe Anbieter
- **Microsoft 365:** Premier Support, Ticket-Portal: https://admin.microsoft.com/support
- **Barracuda Networks:** Support-Hotline: +49 89 123456789, E-Mail: support@barracuda.com
- **Veeam Software:** Support-Portal: https://www.veeam.com/support.html

## Bekannte Probleme und Workarounds

### Problem 1: Verzögerte E-Mail-Zustellung bei großen Anhängen
- **Symptom:** E-Mails mit Anhängen > 10 MB werden verzögert zugestellt
- **Ursache:** SMTP Queue Processing Limit
- **Workaround:** Verwendung von OneDrive-Links statt großer Anhänge
- **Permanente Lösung:** In Planung für Q2 2026

### Problem 2: Outlook-Client-Synchronisationsfehler
- **Symptom:** Outlook zeigt "Nicht verbunden" Status
- **Ursache:** Veraltete Outlook-Version oder beschädigtes Profil
- **Workaround:** Outlook-Profil neu erstellen oder auf neueste Version aktualisieren
- **Permanente Lösung:** Automatische Outlook-Updates via WSUS

## Änderungshistorie

| Version | Datum | Autor | Änderungen |
|---|---|---|---|
| 1.0.0 | 2026-01-31 | {{ meta.author }} | Initiale Version - Service-Beschreibung erstellt |
| 1.0.1 | 2026-02-15 | {{ meta.author }} | Backup-Strategie aktualisiert |
| 1.1.0 | 2026-03-01 | {{ meta.author }} | DLP-Policies hinzugefügt |

---

**Dokumentverantwortlicher:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Organisation:** {{ meta.organization.name }}  
**Klassifizierung:** {{ meta.document.classification }}
