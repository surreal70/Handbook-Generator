# Service: {{ service.name }}

**Dokument-ID:** {{ service.id }}  
**Organisation:** {{ meta-organisation.name }}  
**Service Owner:** {{ service.owner }}  
**Service Manager:** {{ service.manager }}  
**Revision:** {{ service.revision }}  
**Author:** {{ meta-global.source }}  
**Status:** {{ service.status }}  
**Letzte Aktualisierung:** {{ service.modifydate }}  
**Template Version:** {{ meta-global.version }}

---

## 1. Service-Übersicht

### 1.1 Beschreibung

Dieser Service stellt E-Mail-Kommunikation für alle Mitarbeiter der Organisation bereit und unterstützt geschäftskritische Kommunikationsprozesse.

Der Service umfasst:
- E-Mail-Versand und -Empfang (SMTP/IMAP/POP3)
- Webmail-Zugriff (Outlook Web App)
- Mobile E-Mail-Synchronisation (ActiveSync)
- Kalender- und Kontaktverwaltung
- Anti-Spam und Anti-Malware-Schutz
- E-Mail-Archivierung für Compliance

### 1.2 Service-Kategorie

**Kategorie:** {{ service.category }}  
**Kritikalität:** {{ service.criticality }}

### 1.3 Service-Ziele

Die Hauptziele dieses Services sind:

- **Verfügbarkeit:** {{ service.sla.availability_target }} Verfügbarkeit für geschäftskritische E-Mail-Kommunikation
- **Performance:** < 2 Sekunden Antwortzeit für Webmail-Zugriff
- **Sicherheit:** Schutz vor Spam, Malware und Phishing-Angriffen
- **Zuverlässigkeit:** Minimierung von E-Mail-Verlusten durch redundante Systeme

### 1.4 Nutzen für die Organisation

- Unterstützung der Geschäftsprozesse durch zuverlässige E-Mail-Kommunikation
- Verbesserung der Produktivität durch mobile E-Mail-Zugriff
- Reduzierung von Sicherheitsrisiken durch integrierte Anti-Spam/Anti-Malware-Lösung
- Compliance-Konformität durch automatische E-Mail-Archivierung

---

## 2. COBIT-Mapping

**COBIT Version:** {{ compliance.cobit_version }}

### 2.1 Relevante Prozesse

Dieser Service unterstützt folgende COBIT-Prozesse:

- DSS01 - Manage Operations
- DSS02 - Manage Service Requests and Incidents
- DSS05 - Manage Security Services
- DSS06 - Manage Business Process Controls

### 2.2 Controls

Die folgenden Controls werden durch diesen Service adressiert:

- DSS01.01 - Perform operational procedures
- DSS02.01 - Define service requests
- DSS05.01 - Protect against malware
- DSS05.07 - Manage network and connectivity security

### 2.3 Governance-Anforderungen

- **Überwachung:** Tägliche Überprüfung der E-Mail-Zustellung und Anti-Spam-Effektivität
- **Compliance:** Einhaltung von DSGVO-Anforderungen für E-Mail-Archivierung
- **Risikomanagement:** Monatliche Sicherheitsaudits und Phishing-Simulationen

---

## 3. ITIL-Mapping

**ITIL Version:** {{ compliance.itil_version }}

### 3.1 Lifecycle-Phase

**Aktuelle Phase:** {{ service.itil.lifecycle_phase }}

### 3.2 ITIL-Prozesse

Dieser Service ist in folgende ITIL-Prozesse eingebunden:

- Incident Management
- Problem Management
- Access Management
- Service Request Management
- Event Management

### 3.3 Service-Lifecycle-Aktivitäten

#### Service Strategy
- Jährliche Überprüfung der E-Mail-Strategie (Cloud vs. On-Premise)
- Identifikation von Geschäftsanforderungen für E-Mail-Features

#### Service Design
- Architektur-Design für hohe Verfügbarkeit und Skalierbarkeit
- Definition von SLAs für E-Mail-Zustellung und -Verfügbarkeit

#### Service Transition
- Planung und Durchführung von Exchange-Updates
- Migration von Postfächern bei Organisationsänderungen

#### Service Operation
- 24/7 Monitoring der E-Mail-Infrastruktur
- Incident Management für E-Mail-Ausfälle und -Probleme

#### Continual Service Improvement
- Quartalsweise Service-Reviews mit Stakeholdern
- Implementierung von Verbesserungen basierend auf User-Feedback

---

## 4. Service-Komponenten

### 4.1 Technologie-Stack

- **Platform:** {{ service.technology.platform }}
- **Backup:** {{ service.technology.backup }}
- **Monitoring:** {{ service.technology.monitoring }}
- **Anti-Spam:** {{ service.technology.antispam }}
- **Archivierung:** {{ service.technology.archiving }}

### 4.2 Architektur-Übersicht

Der E-Mail-Service basiert auf Microsoft Exchange Online mit folgenden Komponenten:

```
Internet
    ↓
Mimecast (Anti-Spam/Anti-Malware)
    ↓
Microsoft Exchange Online
    ↓
    ├─→ Outlook Desktop Clients
    ├─→ Outlook Web App (OWA)
    ├─→ Mobile Devices (ActiveSync)
    └─→ Barracuda Message Archiver
```

### 4.3 Schnittstellen und Abhängigkeiten

#### Interne Schnittstellen
- **Active Directory**: Benutzer-Authentifizierung und Synchronisation
- **VPN-Service**: Sicherer Zugriff für externe Mitarbeiter
- **Monitoring-Service**: Zabbix für Verfügbarkeits-Monitoring

#### Externe Schnittstellen
- **Microsoft 365**: Cloud-basierte E-Mail-Plattform
- **Mimecast**: Cloud-basierte Anti-Spam/Anti-Malware-Lösung
- **Barracuda**: Cloud-basierte E-Mail-Archivierung

#### Abhängigkeiten
- **Internet-Konnektivität**: Kritisch für Cloud-basierten Service
- **DNS-Service**: Erforderlich für E-Mail-Routing (MX-Records)
- **Active Directory**: Erforderlich für Benutzer-Authentifizierung

---

## 5. Service Level Agreements (SLAs)

### 5.1 Verfügbarkeit

**Verfügbarkeitsziel:** {{ service.sla.availability_target }}

**Messperiode:** Monatlich  
**Ausnahmen:** Geplante Wartungsfenster ({{ support.maintenance_window }})

### 5.2 Response Times

Die folgenden Reaktionszeiten gelten für E-Mail-Service-Anfragen:

| Priorität | Beschreibung | Reaktionszeit | Lösungszeit |
|-----------|--------------|---------------|-------------|
| P1 - Kritisch | Kompletter E-Mail-Ausfall | {{ service.sla.response_time_p1 }} | 4 Stunden |
| P2 - Hoch | Teilausfall, Workaround verfügbar | {{ service.sla.response_time_p2 }} | 8 Stunden |
| P3 - Mittel | Einzelne Postfächer betroffen | {{ service.sla.response_time_p3 }} | 1 Werktag |
| P4 - Niedrig | Anfragen und Informationen | {{ service.sla.response_time_p4 }} | 2 Werktage |

### 5.3 Performance-Ziele

- **Antwortzeit Webmail:** < 2 Sekunden für 95% der Anfragen
- **E-Mail-Zustellung (intern):** < 30 Sekunden
- **E-Mail-Zustellung (extern):** < 5 Minuten
- **Postfach-Kapazität:** 50 GB pro Benutzer

### 5.4 SLA-Reporting

- Monatliche SLA-Reports an Service Owner und IT-Management
- Quartalsweise Service-Reviews mit Business-Stakeholdern
- Sofortige Eskalation bei SLA-Verletzungen

---

## 6. Operational Level Agreements (OLAs)

### 6.1 Interne Support-Vereinbarungen

| Support-Team | Verantwortlichkeit | Reaktionszeit |
|--------------|-------------------|---------------|
| Netzwerk-Team | Internet-Konnektivität | 30 Minuten (P1) |
| Security-Team | Anti-Spam/Anti-Malware-Konfiguration | 2 Stunden (P2) |
| Identity-Team | Active Directory Synchronisation | 1 Stunde (P2) |

### 6.2 Wartungsfenster

**Standard-Wartungsfenster:** {{ support.maintenance_window }}

Während der Wartungsfenster können folgende Aktivitäten durchgeführt werden:
- Exchange Online Updates (automatisch durch Microsoft)
- Mimecast-Konfigurationsänderungen
- Barracuda-Archivierungs-Wartung

---

## 7. Rollen und Verantwortlichkeiten

### 7.1 Service-Organisation

| Rolle | Name | Kontakt | Verantwortlichkeit |
|-------|------|---------|-------------------|
| Service Owner | {{ role_IT_Manager }} | {{ role_IT_Manager_email }} | Strategische Verantwortung, Budget, Service-Strategie |
| Service Manager | {{ role_IT_Manager }} | {{ role_IT_Manager_email }} | Operativer Betrieb, SLA-Einhaltung, Team-Führung |

### 7.2 RACI-Matrix

| Aktivität | Service Owner | Service Manager | System Admin | Service Desk |
|-----------|---------------|-----------------|--------------|--------------|
| Service-Strategie | A | C | I | I |
| SLA-Definition | A | R | C | I |
| Täglicher Betrieb | I | A | R | - |
| Incident-Bearbeitung | I | A | R | R |
| Change-Genehmigung | A | C | R | - |
| Postfach-Erstellung | I | A | R | R |

**Legende:**
- R = Responsible (Durchführung)
- A = Accountable (Verantwortlich)
- C = Consulted (Konsultiert)
- I = Informed (Informiert)

---

## 8. Support-Modell

### 8.1 Support-Zeiten

- **Business Hours:** {{ support.business_hours }}
- **Extended Hours:** {{ support.extended_hours }}
- **Maintenance Window:** {{ support.maintenance_window }}

### 8.2 Support-Kanäle

| Kanal | Verfügbarkeit | Verwendung |
|-------|---------------|------------|
| Telefon | Business Hours | Kritische E-Mail-Ausfälle (P1, P2) |
| E-Mail | 24/7 | Alle Prioritäten (außer P1) |
| Self-Service Portal | 24/7 | Postfach-Anfragen, Dokumentation |
| Chat | Business Hours | Schnelle E-Mail-Fragen |

### 8.3 Eskalationspfad

| Level | Rolle | Kontakt | Eskalationskriterien |
|-------|-------|---------|---------------------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} | Erste Anlaufstelle für E-Mail-Probleme |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} | Nach 30 Min ohne Lösung (P1) |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} | Nach 1 Std ohne Lösung (P1) |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} | Geschäftskritische Eskalation |

### 8.4 Incident-Klassifizierung

**P1 - Kritisch:**
- Kompletter E-Mail-Ausfall (kein Senden/Empfangen)
- Datenverlust in Postfächern
- Sicherheitsvorfall (Kompromittierung)

**P2 - Hoch:**
- Teilausfall (z.B. nur Webmail betroffen)
- Performance-Probleme (langsame E-Mail-Zustellung)
- Mehrere Benutzer können nicht auf Postfächer zugreifen

**P3 - Mittel:**
- Einzelne Benutzer betroffen
- Eingeschränkte Funktionalität (z.B. Kalender-Sync)
- Nicht-kritische Fehler

**P4 - Niedrig:**
- Informationsanfragen zu E-Mail-Features
- Postfach-Erweiterungsanfragen
- Dokumentationsfragen

---

## 9. Betriebszeiten und Verfügbarkeit

### 9.1 Service-Zeiten

**Produktivbetrieb:** 24/7  
**Support:** {{ support.business_hours }}

### 9.2 Geplante Wartung

- **Frequenz:** Monatlich (Microsoft Exchange Online Updates)
- **Fenster:** {{ support.maintenance_window }}
- **Ankündigung:** Mindestens 5 Werktage im Voraus
- **Dauer:** Maximal 2 Stunden

### 9.3 Notfall-Wartung

Bei kritischen Sicherheitsupdates oder Notfällen kann außerplanmäßige Wartung mit verkürzter Ankündigungsfrist (24 Stunden) durchgeführt werden.

---

## 10. Monitoring und Reporting

### 10.1 Monitoring-Strategie

**Monitoring-Tool:** {{ service.technology.monitoring }}

#### Überwachte Metriken
- **Verfügbarkeit:** Uptime-Monitoring von Exchange Online, Mimecast, Barracuda
- **Performance:** E-Mail-Zustellungszeiten, Webmail-Antwortzeiten
- **Kapazität:** Postfach-Auslastung, Archivierungs-Speicher
- **Sicherheit:** Spam-Rate, Malware-Erkennungen, Phishing-Versuche

#### Alerting
- **P1-Alerts:** Sofortige Benachrichtigung via SMS und E-Mail bei komplettem Ausfall
- **P2-Alerts:** E-Mail-Benachrichtigung innerhalb 15 Minuten bei Teilausfällen
- **P3-Alerts:** E-Mail-Benachrichtigung innerhalb 1 Stunde bei Performance-Problemen

### 10.2 Reporting

#### Operative Reports
- **Täglich:** E-Mail-Zustellungs-Statistiken, Spam-/Malware-Erkennungen
- **Wöchentlich:** Postfach-Auslastung, Performance-Trends

#### Management Reports
- **Monatlich:** SLA-Compliance, Service-Performance, Sicherheits-Incidents
- **Quartalsweise:** Service-Review, Verbesserungsmaßnahmen, Kosten

### 10.3 Dashboards

- **Operations Dashboard:** Echtzeit-Übersicht für Support-Teams (Zabbix)
- **Management Dashboard:** KPIs und Trends für Service Owner
- **User Dashboard:** Service-Status und Ankündigungen (Self-Service Portal)

---

## 11. Backup und Disaster Recovery

### 11.1 Backup-Strategie

**Backup-Lösung:** {{ service.technology.backup }}

- **Frequenz:** Täglich (inkrementell), Wöchentlich (vollständig)
- **Aufbewahrung:** 30 Tage online, 7 Jahre archiviert (Compliance)
- **Speicherort:** Primär: Veeam Cloud, Sekundär: On-Premise

### 11.2 Recovery-Ziele

- **RTO (Recovery Time Objective):** 4 Stunden
- **RPO (Recovery Point Objective):** 24 Stunden

### 11.3 Disaster Recovery Plan

1. **Incident-Erkennung:** Zabbix-Alerts, Benutzer-Meldungen
2. **Bewertung:** Schadensumfang (einzelne Postfächer vs. kompletter Ausfall)
3. **Aktivierung:** DR-Plan aktivieren, Teams informieren
4. **Recovery:** Postfächer aus Veeam Backup wiederherstellen
5. **Validierung:** E-Mail-Zustellung testen, Postfach-Zugriff prüfen
6. **Kommunikation:** Benutzer und Stakeholder informieren

---

## 12. Sicherheit und Compliance

### 12.1 Sicherheitsmaßnahmen

- **Zugriffskontrolle:** Rollenbasierte Berechtigungen (RBAC) in Exchange Online
- **Authentifizierung:** Multi-Faktor-Authentifizierung (MFA) für alle Benutzer
- **Verschlüsselung:** TLS 1.3 für E-Mail-Transport, AES-256 für Daten at Rest
- **Anti-Spam/Anti-Malware:** Mimecast mit 99.9% Spam-Erkennungsrate
- **Logging:** Umfassende Audit-Logs für alle E-Mail-Zugriffe

### 12.2 Compliance-Anforderungen

**Relevante Standards:**
- ISO 27001: Informationssicherheits-Management
- COBIT 2019: IT-Governance
- ITIL 4: Service-Management
- DSGVO: Datenschutz-Grundverordnung

### 12.3 Datenschutz

- **DSGVO-Konformität:** E-Mail-Archivierung mit Aufbewahrungsfristen
- **Datenklassifizierung:** Vertraulich (E-Mail-Inhalte)
- **Aufbewahrungsfristen:** 7 Jahre für geschäftliche E-Mails (gesetzlich)

---

## 13. Change Management

### 13.1 Change-Prozess

Alle Änderungen am E-Mail-Service folgen dem etablierten Change-Management-Prozess:

1. **Request for Change (RFC):** Einreichung über Service Portal
2. **Bewertung:** Impact-Analyse (Anzahl betroffener Benutzer)
3. **Genehmigung:** Change Advisory Board (CAB)
4. **Planung:** Detaillierte Implementierungsplanung
5. **Implementierung:** Durchführung während Wartungsfenster
6. **Review:** Post-Implementation Review

### 13.2 Change-Kategorien

| Kategorie | Genehmigung | Vorlaufzeit | Beispiele |
|-----------|-------------|-------------|-----------|
| Standard | Service Manager | 2 Werktage | Postfach-Erstellung, Verteilerlisten |
| Normal | CAB | 5 Werktage | Mimecast-Konfiguration, Exchange-Policies |
| Emergency | Emergency CAB | Sofort | Sicherheits-Patches, kritische Bugfixes |

---

## 14. Kontinuierliche Verbesserung

### 14.1 Service-Review-Prozess

- **Frequenz:** Quartalsweise
- **Teilnehmer:** Service Owner, Service Manager, Key Stakeholders
- **Agenda:** SLA-Review, Incident-Analyse, User-Feedback, Verbesserungsvorschläge

### 14.2 KPIs und Metriken

| KPI | Zielwert | Messfrequenz |
|-----|----------|--------------|
| Service-Verfügbarkeit | {{ service.sla.availability_target }} | Monatlich |
| MTTR (Mean Time To Repair) | < 2 Stunden | Monatlich |
| MTBF (Mean Time Between Failures) | > 720 Stunden | Monatlich |
| Spam-Erkennungsrate | > 99.9% | Monatlich |
| Customer Satisfaction | > 4.0/5.0 | Quartalsweise |

### 14.3 Verbesserungsmaßnahmen

Identifizierte Verbesserungsmaßnahmen für Q1 2026:

1. **Phishing-Simulationen:** Monatliche Phishing-Tests für alle Mitarbeiter
2. **Self-Service-Erweiterung:** Automatische Postfach-Erstellung über Portal
3. **Mobile-App-Optimierung:** Verbesserung der Outlook Mobile App Performance

---

## 15. Kosten und Verrechnung

### 15.1 Kostenstruktur

- **Fixkosten:** Microsoft 365 E3 Lizenzen (€20/Benutzer/Monat)
- **Variable Kosten:** Mimecast (€5/Benutzer/Monat), Barracuda (€3/Benutzer/Monat)
- **Einmalige Kosten:** Migrationen, Schulungen

### 15.2 Verrechnung

Kosten werden monatlich pro Benutzer verrechnet:
- **Standard-Postfach:** €28/Monat (inkl. alle Services)
- **Shared-Postfach:** €10/Monat (ohne Lizenz)

---

## 16. Anhänge

### 16.1 Runbooks

- **Postfach-Erstellung:** Schritt-für-Schritt-Anleitung für neue Postfächer
- **E-Mail-Wiederherstellung:** Anleitung zur Wiederherstellung gelöschter E-Mails
- **Mimecast-Konfiguration:** Anleitung für Anti-Spam-Regeln

### 16.2 Checklisten

- **Onboarding-Checklist:** Für neue Mitarbeiter (Postfach, Mobile, Outlook)
- **Offboarding-Checklist:** Für ausscheidende Mitarbeiter
- **Wartungs-Checklist:** Monatliche Wartungsaufgaben

### 16.3 Weitere Dokumentation

- Technische Dokumentation: [Link zu Confluence]
- Benutzerhandbuch: [Link zu SharePoint]
- FAQ: [Link zu Self-Service Portal]

---

## 17. Kontaktinformationen

### 17.1 Organisation

- **Name:** {{ meta-organisation.name }}
- **Adresse:** {{ meta-organisation.address }}
- **Telefon:** {{ meta-organisation.phone }}
- **Web:** {{ meta-organisation.web }}

### 17.2 Service-Kontakte

- **Service Desk:** {{ escalation.level_1 }} ({{ escalation.level_1_email }})
- **Service Manager:** {{ role_IT_Manager }} ({{ role_IT_Manager_email }})
- **Service Owner:** {{ role_IT_Manager }} ({{ role_IT_Manager_email }})

---

## Dokumentenhistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | 19.02.2026 | Handbook Generator | Initiale Version - E-Mail Service Dokumentation |

---
