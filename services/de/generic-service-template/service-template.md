# Service: {{ meta-service.name }}

<!-- 
ANLEITUNG: Dokumenten-Header
- Alle Felder mit {{ }} werden automatisch aus meta-service.yaml befüllt
- Passen Sie die Werte in meta-service.yaml an Ihren konkreten Service an
- Dokument-ID sollte eindeutig sein (z.B. SVC-001, SVC-EMAIL, etc.)
-->

**Dokument-ID:** {{ meta-service.id }}  
**Organisation:** {{ meta-organisation.name }}  
**Service Owner:** {{ meta-service.owner }}  
**Service Manager:** {{ meta-service.manager }}  
**Revision:** {{ meta-service.revision }}  
**Author:** {{ meta-service.source }}  
**Status:** {{ meta-service.status }}  
**Letzte Aktualisierung:** {{ meta-service.modifydate }}  
**Template Version:** {{ meta-service.version }}

---

## 1. Service-Übersicht

<!-- 
ANLEITUNG: Service-Übersicht
- Beschreiben Sie hier die Hauptfunktionalität Ihres Services
- Nennen Sie die Zielgruppe (z.B. "alle Mitarbeiter", "Entwicklungsteam", "Vertrieb")
- Listen Sie die wichtigsten Komponenten auf
- Beispiel: "Dieser Service stellt E-Mail-Kommunikation bereit und unterstützt alle Mitarbeiter"
-->

### 1.1 Beschreibung

Dieser Service stellt [Beschreibung der Hauptfunktionalität] bereit und unterstützt [Zielgruppe/Geschäftsprozesse].

Der Service umfasst:
- [Hauptkomponente 1]
- [Hauptkomponente 2]
- [Hauptkomponente 3]

### 1.2 Service-Kategorie

<!-- 
ANLEITUNG: Service-Kategorie
- Kategorie wird aus meta-service.yaml geladen
- Mögliche Werte: infrastructure, application, business, security, support
- Kritikalität: Critical, High, Medium, Low
-->

**Kategorie:** {{ meta-service.category }}  
**Kritikalität:** {{ meta-service.criticality }}

### 1.3 Service-Ziele

<!-- 
ANLEITUNG: Service-Ziele
- Passen Sie die Ziele an Ihren konkreten Service an
- Fokussieren Sie auf messbare Ziele
- Beispiele: "99.9% Verfügbarkeit", "< 1 Sekunde Antwortzeit"
-->

Die Hauptziele dieses Services sind:

- **Verfügbarkeit:** Sicherstellung einer hohen Verfügbarkeit für geschäftskritische Prozesse
- **Performance:** Gewährleistung optimaler Antwortzeiten und Durchsatz
- **Sicherheit:** Schutz von Daten und Systemen gemäß Compliance-Anforderungen
- **Zuverlässigkeit:** Minimierung von Ausfällen und Störungen

### 1.4 Nutzen für die Organisation

<!-- 
ANLEITUNG: Nutzen
- Beschreiben Sie den konkreten Geschäftsnutzen
- Beispiele: "Ermöglicht mobile Arbeit", "Reduziert manuelle Prozesse um 50%"
-->

- Unterstützung der Geschäftsprozesse durch [spezifischer Nutzen]
- Verbesserung der Produktivität durch [spezifischer Nutzen]
- Reduzierung von Risiken durch [spezifischer Nutzen]

---

## 2. COBIT-Mapping

<!-- 
ANLEITUNG: COBIT-Mapping
- COBIT-Prozesse werden aus meta-service.yaml geladen
- Wählen Sie relevante COBIT 2019 Prozesse aus
- Typische Prozesse: DSS01 (Manage Operations), DSS02 (Manage Service Requests), DSS05 (Manage Security Services)
- Dokumentation: https://www.isaca.org/resources/cobit
-->

**COBIT Version:** {{ meta-global-service.compliance.cobit_version }}

### 2.1 Relevante Prozesse

Dieser Service unterstützt folgende COBIT-Prozesse:

{{ meta-service.cobit.processes }}

### 2.2 Controls

Die folgenden Controls werden durch diesen Service adressiert:

{{ meta-service.cobit.controls }}

### 2.3 Governance-Anforderungen

<!-- 
ANLEITUNG: Governance
- Beschreiben Sie spezifische Governance-Anforderungen für diesen Service
- Beispiele: "Monatliche Berichterstattung an IT-Lenkungsausschuss"
-->

- **Überwachung:** Regelmäßige Überprüfung der Service-Performance
- **Compliance:** Einhaltung interner und externer Vorgaben
- **Risikomanagement:** Identifikation und Behandlung von Service-Risiken

---

## 3. ITIL-Mapping

<!-- 
ANLEITUNG: ITIL-Mapping
- ITIL-Prozesse werden aus meta-service.yaml geladen
- Wählen Sie relevante ITIL 4 Prozesse aus
- Lifecycle-Phasen: Service Strategy, Service Design, Service Transition, Service Operation, Continual Service Improvement
- Dokumentation: https://www.axelos.com/certifications/itil-service-management
-->

**ITIL Version:** {{ meta-global-service.compliance.itil_version }}

### 3.1 Lifecycle-Phase

**Aktuelle Phase:** {{ meta-service.itil.lifecycle_phase }}

### 3.2 ITIL-Prozesse

Dieser Service ist in folgende ITIL-Prozesse eingebunden:

{{ meta-service.itil.processes }}

### 3.3 Service-Lifecycle-Aktivitäten

<!-- 
ANLEITUNG: Lifecycle-Aktivitäten
- Beschreiben Sie konkrete Aktivitäten in jeder Phase
- Beispiel Service Strategy: "Jährliche Überprüfung der Service-Strategie im Q4"
-->

#### Service Strategy
- Definition der Service-Strategie und Positionierung
- Identifikation von Geschäftsanforderungen

#### Service Design
- Architektur und Design des Services
- Definition von SLAs und OLAs

#### Service Transition
- Planung und Durchführung von Changes
- Wissensmanagement und Dokumentation

#### Service Operation
- Täglicher Betrieb und Support
- Incident und Problem Management

#### Continual Service Improvement
- Regelmäßige Service-Reviews
- Implementierung von Verbesserungsmaßnahmen

---

## 4. Service-Komponenten

<!-- 
ANLEITUNG: Service-Komponenten
- Technologie-Stack wird aus meta-service.yaml geladen
- Beschreiben Sie die technische Architektur
- Fügen Sie Architektur-Diagramme hinzu (z.B. als PNG/SVG)
-->

### 4.1 Technologie-Stack

- **Platform:** {{ meta-service.technology.platform }}
- **Backup:** {{ meta-service.technology.backup }}
- **Monitoring:** {{ meta-service.technology.monitoring }}

### 4.2 Architektur-Übersicht

<!-- 
ANLEITUNG: Architektur
- Fügen Sie hier ein Architektur-Diagramm ein
- Beschreiben Sie die Hauptkomponenten und deren Zusammenspiel
- Beispiel: "Load Balancer -> Web Server -> Application Server -> Database"
-->

[Beschreibung der Service-Architektur]

```
[Architektur-Diagramm oder Beschreibung]
```

### 4.3 Schnittstellen und Abhängigkeiten

<!-- 
ANLEITUNG: Schnittstellen
- Listen Sie alle Schnittstellen zu anderen Services auf
- Interne Schnittstellen: Andere IT-Services in Ihrer Organisation
- Externe Schnittstellen: Cloud-Services, Partner-Systeme
- Abhängigkeiten: Services, von denen dieser Service abhängt
-->

#### Interne Schnittstellen
- [Schnittstelle 1]: Beschreibung
- [Schnittstelle 2]: Beschreibung

#### Externe Schnittstellen
- [Externe Schnittstelle 1]: Beschreibung
- [Externe Schnittstelle 2]: Beschreibung

#### Abhängigkeiten
- [Abhängiger Service 1]: Art der Abhängigkeit
- [Abhängiger Service 2]: Art der Abhängigkeit

---

## 5. Service Level Agreements (SLAs)

<!-- 
ANLEITUNG: SLAs
- SLA-Werte werden aus meta-service.yaml geladen
- Passen Sie die Werte an die Anforderungen Ihres Services an
- Verfügbarkeit: Typisch 99.5% (Standard), 99.9% (Hoch), 99.99% (Kritisch)
- Response Times: P1 (Kritisch), P2 (Hoch), P3 (Mittel), P4 (Niedrig)
-->

### 5.1 Verfügbarkeit

**Verfügbarkeitsziel:** {{ meta-service.sla.availability_target }}

**Messperiode:** Monatlich  
**Ausnahmen:** Geplante Wartungsfenster

### 5.2 Response Times

Die folgenden Reaktionszeiten gelten für Service-Anfragen:

| Priorität | Beschreibung | Reaktionszeit | Lösungszeit |
|-----------|--------------|---------------|-------------|
| P1 - Kritisch | Kompletter Service-Ausfall | {{ meta-service.sla.response_time_p1 }} | 4 Stunden |
| P2 - Hoch | Teilausfall, Workaround verfügbar | {{ meta-service.sla.response_time_p2 }} | 8 Stunden |
| P3 - Mittel | Eingeschränkte Funktionalität | {{ meta-service.sla.response_time_p3 }} | 2 Werktage |
| P4 - Niedrig | Anfragen und Informationen | {{ meta-service.sla.response_time_p4 }} | 5 Werktage |

### 5.3 Performance-Ziele

<!-- 
ANLEITUNG: Performance-Ziele
- Definieren Sie messbare Performance-Ziele
- Beispiele: "< 2 Sekunden Antwortzeit für 95% der Anfragen"
- Passen Sie an Ihren Service an
-->

- **Antwortzeit:** < 2 Sekunden für 95% der Anfragen
- **Durchsatz:** [Spezifische Durchsatzanforderungen]
- **Kapazität:** [Kapazitätsanforderungen]

### 5.4 SLA-Reporting

<!-- 
ANLEITUNG: SLA-Reporting
- Definieren Sie Reporting-Frequenz und -Empfänger
- Beispiel: "Monatlicher SLA-Report an Service Owner und Stakeholder"
-->

- Monatliche SLA-Reports an Service Owner
- Quartalsweise Service-Reviews mit Stakeholdern
- Eskalation bei SLA-Verletzungen

---

## 6. Operational Level Agreements (OLAs)

<!-- 
ANLEITUNG: OLAs
- OLAs sind interne Vereinbarungen zwischen IT-Teams
- Definieren Sie Verantwortlichkeiten und Reaktionszeiten
- Beispiel: "Netzwerk-Team stellt Konnektivität innerhalb 2 Stunden wieder her"
-->

### 6.1 Interne Support-Vereinbarungen

| Support-Team | Verantwortlichkeit | Reaktionszeit |
|--------------|-------------------|---------------|
| [Team 1] | [Verantwortung] | [Zeit] |
| [Team 2] | [Verantwortung] | [Zeit] |

### 6.2 Wartungsfenster

**Standard-Wartungsfenster:** {{ support.maintenance_window }}

Während der Wartungsfenster können folgende Aktivitäten durchgeführt werden:
- System-Updates und Patches
- Konfigurationsänderungen
- Backup-Verifikation

---

## 7. Rollen und Verantwortlichkeiten

<!-- 
ANLEITUNG: Rollen
- Rollen werden aus meta-service.yaml und meta-organisation-roles.yaml geladen
- Service Owner: Strategische Verantwortung, Budget
- Service Manager: Operativer Betrieb, Tagesgeschäft
- Passen Sie die RACI-Matrix an Ihre Organisation an
-->

### 7.1 Service-Organisation

| Rolle | Name | Kontakt | Verantwortlichkeit |
|-------|------|---------|-------------------|
| Service Owner | {{ meta-service.owner }} | {{ meta-service.owner_email }} | Strategische Verantwortung, Budget, Service-Strategie |
| Service Manager | {{ meta-service.manager }} | {{ meta-service.manager_email }} | Operativer Betrieb, SLA-Einhaltung, Team-Führung |

### 7.2 RACI-Matrix

<!-- 
ANLEITUNG: RACI-Matrix
- R = Responsible (Durchführung): Wer führt die Aktivität aus?
- A = Accountable (Verantwortlich): Wer trägt die Gesamtverantwortung?
- C = Consulted (Konsultiert): Wer wird um Rat gefragt?
- I = Informed (Informiert): Wer wird informiert?
- Passen Sie die Aktivitäten und Rollen an Ihren Service an
- Fügen Sie weitere Rollen hinzu (z.B. {{ role_CISO }}, {{ role_System_Administrator }})
- Die Rollennamen werden aus meta-service.yaml und meta-organisation-roles.yaml geladen
-->

| Aktivität | {{ meta-service.owner }} | {{ meta-service.manager }} | {{ role_System_Administrator }} | {{ role_Service_Desk_Lead }} |
|-----------|---------------|-----------------|--------------|----------|
| Service-Strategie | A | C | I | I |
| SLA-Definition | A | R | C | I |
| Täglicher Betrieb | I | A | R | - |
| Incident-Bearbeitung | I | A | R | I |
| Change-Genehmigung | C | C | R | - |

**Legende:**
- R = Responsible (Durchführung)
- A = Accountable (Verantwortlich)
- C = Consulted (Konsultiert)
- I = Informed (Informiert)

---

## 8. Support-Modell

<!-- 
ANLEITUNG: Support-Modell
- Support-Zeiten werden aus service-config.yaml geladen
- Definieren Sie verfügbare Support-Kanäle
- Eskalationspfad wird aus service-config.yaml geladen
-->

### 8.1 Support-Zeiten

- **Business Hours:** {{ support.business_hours }}
- **Extended Hours:** {{ support.extended_hours }}
- **Maintenance Window:** {{ support.maintenance_window }}

### 8.2 Support-Kanäle

<!-- 
ANLEITUNG: Support-Kanäle
- Listen Sie alle verfügbaren Support-Kanäle auf
- Beispiele: Telefon, E-Mail, Ticketsystem, Chat, Self-Service Portal
-->

| Kanal | Verfügbarkeit | Verwendung |
|-------|---------------|------------|
| Telefon | Business Hours | Kritische Incidents (P1, P2) |
| E-Mail | 24/7 | Alle Prioritäten |
| Self-Service Portal | 24/7 | Anfragen, Dokumentation |
| Chat | Business Hours | Schnelle Anfragen |

### 8.3 Eskalationspfad

| Level | Rolle | Kontakt | Eskalationskriterien |
|-------|-------|---------|---------------------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} | Erste Anlaufstelle |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} | Nach 30 Min ohne Lösung (P1) |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} | Nach 1 Std ohne Lösung (P1) |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} | Geschäftskritische Eskalation |

### 8.4 Incident-Klassifizierung

<!-- 
ANLEITUNG: Incident-Klassifizierung
- Passen Sie die Klassifizierung an Ihren Service an
- Definieren Sie klare Kriterien für jede Priorität
- Beispiele für P1: "Kompletter Ausfall", "Datenverlust", "Sicherheitsvorfall"
-->

**P1 - Kritisch:**
- Kompletter Service-Ausfall
- Datenverlust
- Sicherheitsvorfall

**P2 - Hoch:**
- Teilausfall mit Workaround
- Performance-Probleme
- Mehrere Benutzer betroffen

**P3 - Mittel:**
- Einzelne Benutzer betroffen
- Eingeschränkte Funktionalität
- Nicht-kritische Fehler

**P4 - Niedrig:**
- Informationsanfragen
- Feature-Requests
- Dokumentationsfragen

---

## 9. Betriebszeiten und Verfügbarkeit

<!-- 
ANLEITUNG: Betriebszeiten
- Definieren Sie Service-Zeiten und Support-Zeiten
- Geplante Wartung: Frequenz, Fenster, Ankündigungsfrist
-->

### 9.1 Service-Zeiten

**Produktivbetrieb:** 24/7  
**Support:** {{ support.business_hours }}

### 9.2 Geplante Wartung

- **Frequenz:** Monatlich
- **Fenster:** {{ support.maintenance_window }}
- **Ankündigung:** Mindestens 5 Werktage im Voraus
- **Dauer:** Maximal 4 Stunden

### 9.3 Notfall-Wartung

Bei kritischen Sicherheitsupdates oder Notfällen kann außerplanmäßige Wartung mit verkürzter Ankündigungsfrist durchgeführt werden.

---

## 10. Monitoring und Reporting

<!-- 
ANLEITUNG: Monitoring
- Monitoring-Tool wird aus meta-service.yaml geladen
- Definieren Sie überwachte Metriken
- Alerting-Regeln: Wann wird wer wie benachrichtigt?
-->

### 10.1 Monitoring-Strategie

**Monitoring-Tool:** {{ meta-service.technology.monitoring }}

#### Überwachte Metriken
- **Verfügbarkeit:** Uptime-Monitoring aller Komponenten
- **Performance:** Antwortzeiten, Durchsatz, Ressourcennutzung
- **Kapazität:** CPU, RAM, Disk, Netzwerk
- **Fehler:** Error-Rates, Failed Transactions

#### Alerting
- **P1-Alerts:** Sofortige Benachrichtigung via SMS und E-Mail
- **P2-Alerts:** E-Mail-Benachrichtigung innerhalb 15 Minuten
- **P3-Alerts:** E-Mail-Benachrichtigung innerhalb 1 Stunde

### 10.2 Reporting

<!-- 
ANLEITUNG: Reporting
- Definieren Sie Reporting-Frequenz und -Inhalte
- Operative Reports: Für IT-Teams (täglich/wöchentlich)
- Management Reports: Für Führungskräfte (monatlich/quartalsweise)
-->

#### Operative Reports
- **Täglich:** Incident-Übersicht, Performance-Metriken
- **Wöchentlich:** Trend-Analysen, Kapazitätsplanung

#### Management Reports
- **Monatlich:** SLA-Compliance, Service-Performance, Kosten
- **Quartalsweise:** Service-Review, Verbesserungsmaßnahmen

### 10.3 Dashboards

- **Operations Dashboard:** Echtzeit-Übersicht für Support-Teams
- **Management Dashboard:** KPIs und Trends für Service Owner
- **User Dashboard:** Service-Status und Ankündigungen

---

## 11. Backup und Disaster Recovery

<!-- 
ANLEITUNG: Backup und DR
- Backup-Lösung wird aus meta-service.yaml geladen
- RTO (Recovery Time Objective): Wie schnell muss der Service wiederhergestellt sein?
- RPO (Recovery Point Objective): Wie viel Datenverlust ist akzeptabel?
- Typische Werte: RTO 4h, RPO 24h (Standard), RTO 1h, RPO 1h (Kritisch)
-->

### 11.1 Backup-Strategie

**Backup-Lösung:** {{ meta-service.technology.backup }}

- **Frequenz:** Täglich (inkrementell), Wöchentlich (vollständig)
- **Aufbewahrung:** 30 Tage online, 1 Jahr archiviert
- **Speicherort:** Primär: On-Site, Sekundär: Off-Site

### 11.2 Recovery-Ziele

- **RTO (Recovery Time Objective):** {{ meta-service.recovery.rto }}
- **RPO (Recovery Point Objective):** {{ meta-service.recovery.rpo }}

### 11.3 Disaster Recovery Plan

<!-- 
ANLEITUNG: DR-Plan
- Beschreiben Sie die Schritte zur Wiederherstellung
- Definieren Sie Verantwortlichkeiten
- Testen Sie den DR-Plan regelmäßig
-->

1. **Incident-Erkennung:** Monitoring-Alerts, Benutzer-Meldungen
2. **Bewertung:** Schadensumfang und Auswirkungen
3. **Aktivierung:** DR-Plan aktivieren, Teams informieren
4. **Recovery:** Systeme wiederherstellen, Daten zurückspielen
5. **Validierung:** Funktionalität prüfen, Tests durchführen
6. **Kommunikation:** Stakeholder informieren

---

## 12. Sicherheit und Compliance

<!-- 
ANLEITUNG: Sicherheit
- Beschreiben Sie implementierte Sicherheitsmaßnahmen
- Listen Sie relevante Compliance-Standards auf
- Datenschutz: DSGVO-Anforderungen beachten
-->

### 12.1 Sicherheitsmaßnahmen

- **Zugriffskontrolle:** Rollenbasierte Berechtigungen (RBAC)
- **Authentifizierung:** Multi-Faktor-Authentifizierung (MFA)
- **Verschlüsselung:** TLS 1.3 für Datenübertragung, AES-256 für Daten at Rest
- **Logging:** Umfassende Audit-Logs für alle Zugriffe

### 12.2 Compliance-Anforderungen

**Relevante Standards:**
- ISO 27001: Informationssicherheits-Management
- {{ meta-global-service.compliance.cobit_version }}: IT-Governance
- {{ meta-global-service.compliance.itil_version }}: Service-Management

### 12.3 Datenschutz

- **DSGVO-Konformität:** Datenschutz by Design und by Default
- **Datenklassifizierung:** [Klassifizierungsstufe]
- **Aufbewahrungsfristen:** Gemäß gesetzlicher Vorgaben

---

## 13. Change Management

<!-- 
ANLEITUNG: Change Management
- Beschreiben Sie den Change-Prozess für diesen Service
- Change-Kategorien: Standard (genehmigt), Normal (CAB), Emergency (sofort)
-->

### 13.1 Change-Prozess

Alle Änderungen am Service folgen dem etablierten Change-Management-Prozess:

1. **Request for Change (RFC):** Einreichung über Service Portal
2. **Bewertung:** Impact- und Risiko-Analyse
3. **Genehmigung:** Change Advisory Board (CAB)
4. **Planung:** Detaillierte Implementierungsplanung
5. **Implementierung:** Durchführung während Wartungsfenster
6. **Review:** Post-Implementation Review

### 13.2 Change-Kategorien

| Kategorie | Genehmigung | Vorlaufzeit |
|-----------|-------------|-------------|
| Standard | Service Manager | 2 Werktage |
| Normal | CAB | 5 Werktage |
| Emergency | Emergency CAB | Sofort |

---

## 14. Kontinuierliche Verbesserung

<!-- 
ANLEITUNG: Kontinuierliche Verbesserung
- Definieren Sie Service-Review-Prozess
- KPIs werden teilweise aus meta-service.yaml geladen
- Verbesserungsmaßnahmen: Priorisieren und tracken
-->

### 14.1 Service-Review-Prozess

- **Frequenz:** Quartalsweise
- **Teilnehmer:** Service Owner, Service Manager, Key Stakeholders
- **Agenda:** SLA-Review, Incident-Analyse, Verbesserungsvorschläge

### 14.2 KPIs und Metriken

| KPI | Zielwert | Messfrequenz |
|-----|----------|--------------|
| Service-Verfügbarkeit | {{ meta-service.sla.availability_target }} | Monatlich |
| MTTR (Mean Time To Repair) | < 2 Stunden | Monatlich |
| MTBF (Mean Time Between Failures) | > 720 Stunden | Monatlich |
| First Call Resolution Rate | > 70% | Monatlich |
| Customer Satisfaction | > 4.0/5.0 | Quartalsweise |

### 14.3 Verbesserungsmaßnahmen

<!-- 
ANLEITUNG: Verbesserungsmaßnahmen
- Listen Sie identifizierte Verbesserungen auf
- Priorisieren Sie nach Impact und Aufwand
- Tracken Sie den Fortschritt
-->

Identifizierte Verbesserungsmaßnahmen werden priorisiert und in den Service-Roadmap aufgenommen:

1. [Verbesserungsmaßnahme 1]
2. [Verbesserungsmaßnahme 2]
3. [Verbesserungsmaßnahme 3]

---

## 15. Kosten und Verrechnung

<!-- 
ANLEITUNG: Kosten
- Beschreiben Sie die Kostenstruktur
- Verrechnung: Wie werden Kosten auf Nutzer/Abteilungen umgelegt?
- Beispiele: Pauschale, nutzungsbasiert, Kostenstelle
-->

### 15.1 Kostenstruktur

- **Fixkosten:** Infrastruktur, Lizenzen, Personal
- **Variable Kosten:** Nutzungsabhängige Kosten
- **Einmalige Kosten:** Projekte, Migrationen

### 15.2 Verrechnung

[Beschreibung des Verrechnungsmodells]

---

## 16. Anhänge

<!-- 
ANLEITUNG: Anhänge
- Verlinken Sie relevante Dokumente
- Runbooks: Schritt-für-Schritt-Anleitungen für häufige Aufgaben
- Checklisten: Für Wartung, Deployment, Troubleshooting
-->

### 16.1 Runbooks

- [Link zu Runbook 1]: Beschreibung
- [Link zu Runbook 2]: Beschreibung

### 16.2 Checklisten

- [Link zu Checklist 1]: Beschreibung
- [Link zu Checklist 2]: Beschreibung

### 16.3 Weitere Dokumentation

- Technische Dokumentation: [Link]
- Benutzerhandbuch: [Link]
- FAQ: [Link]

---

## 17. Kontaktinformationen

### 17.1 Organisation

- **Name:** {{ meta-organisation.name }}
- **Adresse:** {{ meta-organisation.address }}
- **Telefon:** {{ meta-organisation.phone }}
- **Web:** {{ meta-organisation.web }}

### 17.2 Service-Kontakte

- **Service Desk:** {{ escalation.level_1 }} ({{ escalation.level_1_email }})
- **Service Manager:** {{ meta-service.manager }} ({{ meta-service.manager_email }})
- **Service Owner:** {{ meta-service.owner }} ({{ meta-service.owner_email }})

---

## Dokumentenhistorie

<!-- 
ANLEITUNG: Dokumentenhistorie
- Pflegen Sie die Versionshistorie
- Dokumentieren Sie wesentliche Änderungen
- Fügen Sie neue Zeilen für jede Version hinzu
-->

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 19.02.2026 | Handbook Generator | Initiale Version |
| [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

---
