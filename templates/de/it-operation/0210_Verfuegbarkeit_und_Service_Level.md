# Verfügbarkeit und Service Level

**Dokument-ID:** [FRAMEWORK]-0210
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

Dieses Dokument definiert die Verfügbarkeitsanforderungen, Service Level Agreements (SLAs) und Service Level Objectives (SLOs) für den IT-Service. Es beschreibt die Messmethoden, Reporting-Prozesse und Maßnahmen zur kontinuierlichen Verbesserung der Serviceverfügbarkeit.

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

## Verfügbarkeitsanforderungen

### Service-Klassifizierung

| Service-Klasse | Verfügbarkeit | Max. Ausfallzeit/Jahr | Max. Ausfallzeit/Monat | Geschäftskritikalität |
|---|---:|---:|---:|---|
| Kritisch | 99.95% | 4.38 Stunden | 21.6 Minuten | Hoch |
| Wichtig | 99.5% | 43.8 Stunden | 3.6 Stunden | Mittel |
| Standard | 99.0% | 87.6 Stunden | 7.2 Stunden | Niedrig |
| Unkritisch | 95.0% | 438 Stunden | 36 Stunden | Sehr niedrig |

### Service-Zeiten

#### Produktions-Services
- **Verfügbarkeit:** 24/7/365
- **Support-Zeiten:** 24/7 mit On-Call-Bereitschaft
- **Wartungsfenster:** Sonntag 02:00-06:00 Uhr (nach Ankündigung)
- **Notfall-Wartung:** Nach Genehmigung durch {{ meta-organisation-roles.role_cio.name }}

#### Business-Services
- **Verfügbarkeit:** Mo-Fr 06:00-22:00 Uhr
- **Support-Zeiten:** Mo-Fr 08:00-18:00 Uhr
- **Wartungsfenster:** Samstag 20:00-24:00 Uhr
- **Notfall-Wartung:** Nach Genehmigung durch {{ meta-organisation-roles.role_it_operations_manager.name }}

#### Entwicklungs-/Test-Services
- **Verfügbarkeit:** Mo-Fr 08:00-18:00 Uhr
- **Support-Zeiten:** Best Effort
- **Wartungsfenster:** Jederzeit nach Ankündigung
- **Notfall-Wartung:** Nicht erforderlich

### Geplante Wartungsfenster

| Wartungstyp | Frequenz | Dauer | Ankündigungsfrist | Genehmigung |
|---|---|---|---|---|
| Routine-Wartung | Monatlich | 2-4 Stunden | 7 Tage | Ops Manager |
| Patch-Deployment | Monatlich | 1-2 Stunden | 5 Tage | Ops Manager |
| Major-Upgrade | Quartalsweise | 4-8 Stunden | 14 Tage | CIO |
| Notfall-Wartung | Ad-hoc | Variable | 4 Stunden | CIO |

## Service Level Agreements (SLA)

### SLA-Definitionen

#### Verfügbarkeits-SLA

**Service:** [TODO: Service-Name]  
**Gültig ab:** [TODO: Datum]  
**Laufzeit:** 12 Monate mit automatischer Verlängerung

| Metrik | Zielwert | Messmethode | Messintervall |
|---|---:|---|---|
| Verfügbarkeit | 99.5% | Uptime-Monitoring | Monatlich |
| Geplante Ausfallzeit | < 4h/Monat | Change-Kalender | Monatlich |
| Ungeplante Ausfallzeit | < 2h/Monat | Incident-Tracking | Monatlich |
| MTBF (Mean Time Between Failures) | > 720h | Incident-Analyse | Quartalsweise |
| MTTR (Mean Time To Repair) | < 2h | Incident-Tickets | Monatlich |

#### Performance-SLA

| Metrik | Zielwert | Warnschwelle | Messmethode | Messintervall |
|---|---:|---:|---|---|
| Response Time (Avg) | < 200ms | > 300ms | APM-Tool | Kontinuierlich |
| Response Time (95th) | < 500ms | > 750ms | APM-Tool | Kontinuierlich |
| Response Time (99th) | < 1000ms | > 1500ms | APM-Tool | Kontinuierlich |
| Throughput | > 1000 TPS | < 800 TPS | APM-Tool | Kontinuierlich |
| Error Rate | < 0.1% | > 0.5% | APM-Tool | Kontinuierlich |

#### Support-SLA

| Priorität | Reaktionszeit | Lösungszeit | Verfügbarkeit | Eskalation |
|---|---|---|---|---|
| P1 - Kritisch | 15 Minuten | 4 Stunden | 24/7 | Sofort an CIO |
| P2 - Hoch | 1 Stunde | 8 Stunden | 24/7 | Nach 4h an Ops Manager |
| P3 - Mittel | 4 Stunden | 24 Stunden | Mo-Fr 08-18 | Nach 24h an Ops Manager |
| P4 - Niedrig | 8 Stunden | 72 Stunden | Mo-Fr 08-18 | Nach 72h an Ops Manager |

### SLA-Vertragspartner

#### Interne SLAs
- **Service Provider:** IT Operations ({{ meta-organisation-roles.role_it_operations_manager.name }})
- **Service Consumer:** Fachabteilungen
- **Verantwortlich:** {{ meta-organisation-roles.role_cio.name }}
- **Review-Zyklus:** Quartalsweise

#### Externe SLAs
- **Service Provider:** {{ meta-organisation.name }}
- **Service Consumer:** [TODO: Kunde/Partner]
- **Vertragslaufzeit:** [TODO: Laufzeit]
- **Vertragsstrafen:** [TODO: Penalties bei SLA-Verletzung]

### SLA-Ausnahmen

#### Ausschlusskriterien (Force Majeure)
- Naturkatastrophen
- Terroranschläge
- Kriege und Unruhen
- Pandemien
- Stromausfälle außerhalb der Kontrolle

#### Geplante Ausnahmen
- Angekündigte Wartungsfenster
- Genehmigte Notfall-Wartungen
- Vom Kunden verursachte Ausfälle
- Drittanbieter-Ausfälle außerhalb der Kontrolle

## Service Level Objectives (SLO)

### Interne SLOs

#### Infrastruktur-SLOs

| Komponente | SLO | Messmethode | Verantwortlich |
|---|---:|---|---|
| Compute-Cluster | 99.9% | Hypervisor-Monitoring | {{ meta-organisation-roles.role_it_operations_manager.name }} |
| Storage-System | 99.95% | Storage-Monitoring | {{ meta-organisation-roles.role_it_operations_manager.name }} |
| Netzwerk-Core | 99.99% | Network-Monitoring | {{ meta-organisation-roles.role_it_operations_manager.name }} |
| Firewall | 99.95% | Security-Monitoring | {{ meta-organisation-roles.role_ciso.name }} |
| Load Balancer | 99.9% | LB-Monitoring | {{ meta-organisation-roles.role_it_operations_manager.name }} |

#### Anwendungs-SLOs

| Anwendung | Verfügbarkeit | Response Time | Error Rate | Verantwortlich |
|---|---:|---:|---:|---|
| [TODO: App 1] | 99.5% | < 200ms | < 0.1% | [TODO] |
| [TODO: App 2] | 99.0% | < 500ms | < 0.5% | [TODO] |
| [TODO: App 3] | 99.9% | < 100ms | < 0.05% | [TODO] |

#### Datenbank-SLOs

| Datenbank | Verfügbarkeit | Query Time | Connection Time | Verantwortlich |
|---|---:|---:|---:|---|
| [TODO: DB 1] | 99.95% | < 50ms | < 10ms | [TODO] |
| [TODO: DB 2] | 99.5% | < 100ms | < 20ms | [TODO] |

### Error Budget

#### Error Budget Konzept
- **Definition:** Tolerierbare Ausfallzeit innerhalb des SLO-Zeitraums
- **Berechnung:** (100% - SLO) × Zeitraum
- **Verwendung:** Balance zwischen Innovation und Stabilität

#### Error Budget Beispiel (99.5% SLO)

| Zeitraum | Verfügbarkeit | Error Budget | Ausfallzeit |
|---|---:|---:|---:|
| Monat | 99.5% | 0.5% | 3.6 Stunden |
| Quartal | 99.5% | 0.5% | 10.8 Stunden |
| Jahr | 99.5% | 0.5% | 43.8 Stunden |

#### Error Budget Policy

**Wenn Error Budget > 50% verbleibend:**
- Normale Entwicklungsgeschwindigkeit
- Neue Features und Experimente erlaubt
- Routine-Wartungen wie geplant

**Wenn Error Budget 25-50% verbleibend:**
- Erhöhte Vorsicht bei Changes
- Fokus auf Stabilität
- Zusätzliche Testing-Anforderungen

**Wenn Error Budget < 25% verbleibend:**
- Feature-Freeze
- Nur kritische Bugfixes
- Fokus auf Reliability-Verbesserungen
- Postmortem für alle Incidents

**Wenn Error Budget aufgebraucht:**
- Vollständiger Change-Freeze
- Nur Notfall-Fixes
- Root-Cause-Analyse aller Ausfälle
- Verbesserungsplan vor Wiederaufnahme

## Verfügbarkeitsmessung

### Messmethoden

#### Synthetische Monitoring
- **Methode:** Automatisierte Tests von definierten Endpunkten
- **Frequenz:** Alle 1-5 Minuten
- **Standorte:** Mehrere geografische Locations
- **Metriken:** Verfügbarkeit, Response Time, Funktionalität

#### Real User Monitoring (RUM)
- **Methode:** Messung echter Benutzer-Interaktionen
- **Erfassung:** Client-seitige Metriken
- **Metriken:** Page Load Time, User Experience, Fehlerrate
- **Datenschutz:** DSGVO-konform, anonymisiert

#### Server-seitiges Monitoring
- **Methode:** Überwachung von Server-Metriken
- **Erfassung:** Logs, Metriken, Traces
- **Metriken:** Uptime, Resource Usage, Error Logs
- **Aggregation:** Zentrales Monitoring-System

### Verfügbarkeitsberechnung

#### Formel
```
Verfügbarkeit (%) = (Gesamtzeit - Ausfallzeit) / Gesamtzeit × 100
```

#### Beispielberechnung (Monat mit 720 Stunden)
```
Gesamtzeit: 720 Stunden
Geplante Wartung: 2 Stunden (ausgeschlossen)
Ungeplante Ausfälle: 1.5 Stunden
Verfügbare Zeit: 720 - 2 = 718 Stunden
Tatsächliche Verfügbarkeit: (718 - 1.5) / 718 × 100 = 99.79%
```

#### Ausschlüsse
- Geplante und angekündigte Wartungsfenster
- Vom Kunden verursachte Ausfälle
- Force Majeure Ereignisse
- Drittanbieter-Ausfälle (nach Vereinbarung)

### Monitoring-Tools

| Tool | Zweck | Messintervall | Zugriff |
|---|---|---|---|
| [TODO: Uptime-Tool] | Verfügbarkeitsmonitoring | 1 Minute | [TODO: URL] |
| [TODO: APM-Tool] | Performance-Monitoring | Kontinuierlich | [TODO: URL] |
| [TODO: RUM-Tool] | Real User Monitoring | Kontinuierlich | [TODO: URL] |
| [TODO: Log-Tool] | Log-Aggregation | Echtzeit | [TODO: URL] |

## Service-Level-Reporting

### Report-Typen

#### Täglicher Verfügbarkeits-Report
- **Empfänger:** IT Operations Team
- **Inhalt:**
  - Verfügbarkeit der letzten 24 Stunden
  - Incidents und Ausfälle
  - Performance-Metriken
  - Aktuelle Alerts
- **Versand:** Automatisch um 08:00 Uhr

#### Wöchentlicher SLA-Report
- **Empfänger:** {{ meta-organisation-roles.role_it_operations_manager.name }}
- **Inhalt:**
  - Wochenverfügbarkeit
  - SLA-Compliance-Status
  - Trend-Analyse
  - Handlungsempfehlungen
- **Versand:** Jeden Montag

#### Monatlicher SLA-Report
- **Empfänger:** {{ meta-organisation-roles.role_cio.name }}, Stakeholder
- **Inhalt:**
  - Monatsverfügbarkeit
  - SLA-Erfüllung vs. Ziele
  - Incident-Zusammenfassung
  - Error Budget Status
  - Verbesserungsmaßnahmen
- **Versand:** Erster Arbeitstag des Folgemonats

#### Quartalsweiser Management-Report
- **Empfänger:** {{ meta-organisation-roles.role_ceo.name }}, {{ meta-organisation-roles.role_cio.name }}, {{ meta-organisation-roles.role_cfo.name }}
- **Inhalt:**
  - Quartalsverfügbarkeit
  - SLA-Trends
  - Kosten-Nutzen-Analyse
  - Strategische Empfehlungen
- **Versand:** Quartalsende + 5 Arbeitstage

### Report-Metriken

#### Verfügbarkeits-Dashboard

| Metrik | Ziel | Aktuell (Monat) | Trend | Status |
|---|---:|---:|---|---|
| Gesamtverfügbarkeit | 99.5% | [TODO]% | [TODO] | ✓ / ⚠ / ✗ |
| Ungeplante Ausfälle | < 2h | [TODO]h | [TODO] | ✓ / ⚠ / ✗ |
| MTBF | > 720h | [TODO]h | [TODO] | ✓ / ⚠ / ✗ |
| MTTR | < 2h | [TODO]h | [TODO] | ✓ / ⚠ / ✗ |
| Error Budget verbleibend | > 0% | [TODO]% | [TODO] | ✓ / ⚠ / ✗ |

#### Incident-Statistiken

| Priorität | Anzahl | Avg. MTTR | SLA-Erfüllung | Trend |
|---|---:|---:|---:|---|
| P1 - Kritisch | [TODO] | [TODO]h | [TODO]% | [TODO] |
| P2 - Hoch | [TODO] | [TODO]h | [TODO]% | [TODO] |
| P3 - Mittel | [TODO] | [TODO]h | [TODO]% | [TODO] |
| P4 - Niedrig | [TODO] | [TODO]h | [TODO]% | [TODO] |

## Verfügbarkeitsverbesserungen

### Verbesserungsmaßnahmen

#### Redundanz und Hochverfügbarkeit
- **Aktiv-Aktiv-Cluster:** Lastverteilung über mehrere Knoten
- **Aktiv-Passiv-Cluster:** Failover-Konfiguration
- **Geografische Redundanz:** Multi-Region-Deployment
- **Datenbank-Replikation:** Synchrone/Asynchrone Replikation
- **Load Balancing:** Verteilung der Last auf mehrere Instanzen

#### Automatisierung
- **Auto-Healing:** Automatische Wiederherstellung bei Fehlern
- **Auto-Scaling:** Automatische Kapazitätsanpassung
- **Automated Failover:** Automatischer Failover bei Ausfall
- **Health Checks:** Kontinuierliche Gesundheitsprüfungen
- **Self-Service:** Automatisierte Bereitstellung

#### Monitoring und Alerting
- **Proaktives Monitoring:** Früherkennung von Problemen
- **Predictive Analytics:** Vorhersage von Ausfällen
- **Intelligent Alerting:** Reduzierung von False Positives
- **Anomalie-Erkennung:** ML-basierte Anomalie-Erkennung
- **Distributed Tracing:** End-to-End-Nachverfolgung

#### Prozessverbesserungen
- **Incident Management:** Optimierung der Incident-Prozesse
- **Change Management:** Reduzierung von Change-bedingten Ausfällen
- **Capacity Management:** Proaktive Kapazitätsplanung
- **Disaster Recovery:** Verbesserung der DR-Prozesse
- **Continuous Improvement:** Regelmäßige Retrospektiven

### Verbesserungs-Roadmap

| Quartal | Maßnahme | Erwarteter Impact | Verantwortlich | Status |
|---|---|---|---|---|
| Q1 2026 | [TODO] | +0.1% Verfügbarkeit | [TODO] | Geplant |
| Q2 2026 | [TODO] | -30min MTTR | [TODO] | Geplant |
| Q3 2026 | [TODO] | +0.2% Verfügbarkeit | [TODO] | Geplant |
| Q4 2026 | [TODO] | -50% Incidents | [TODO] | Geplant |

### Lessons Learned

#### Postmortem-Prozess
1. **Incident-Dokumentation:** Detaillierte Beschreibung des Vorfalls
2. **Timeline-Erstellung:** Chronologischer Ablauf
3. **Root-Cause-Analysis:** 5-Why-Methode
4. **Impact-Assessment:** Betroffene Systeme und Benutzer
5. **Corrective Actions:** Sofortmaßnahmen und langfristige Verbesserungen
6. **Follow-Up:** Überprüfung der Umsetzung

#### Postmortem-Template
- **Incident-ID:** [TODO]
- **Datum/Zeit:** [TODO]
- **Dauer:** [TODO]
- **Betroffene Services:** [TODO]
- **Root Cause:** [TODO]
- **Maßnahmen:** [TODO]
- **Verantwortlich:** [TODO]
- **Status:** [TODO]

## SLA-Review und Anpassung

### Review-Prozess

#### Quartalsweiser SLA-Review
- **Teilnehmer:** {{ meta-organisation-roles.role_cio.name }}, {{ meta-organisation-roles.role_it_operations_manager.name }}, Stakeholder
- **Agenda:**
  - SLA-Erfüllung der letzten 3 Monate
  - Trend-Analyse
  - Verbesserungspotenziale
  - Anpassungsbedarf
- **Output:** Review-Protokoll mit Handlungsempfehlungen

#### Jährlicher SLA-Review
- **Teilnehmer:** {{ meta-organisation-roles.role_ceo.name }}, {{ meta-organisation-roles.role_cio.name }}, {{ meta-organisation-roles.role_cfo.name }}, Stakeholder
- **Agenda:**
  - Jahresverfügbarkeit
  - SLA-Angemessenheit
  - Kosten-Nutzen-Analyse
  - Strategische Ausrichtung
- **Output:** SLA-Anpassungen für das Folgejahr

### Anpassungskriterien

#### SLA-Verschärfung (höhere Anforderungen)
- Geschäftskritikalität gestiegen
- Wettbewerbsdruck
- Regulatorische Anforderungen
- Kundenfeedback

#### SLA-Lockerung (niedrigere Anforderungen)
- Kosten-Nutzen-Verhältnis
- Technische Machbarkeit
- Geschäftspriorität gesunken
- Realistische Zielsetzung

## Prozesse und Verantwortlichkeiten

### RACI-Matrix

| Aktivität | CIO | Ops Manager | Ops Team | Stakeholder |
|---|---|---|---|---|
| SLA-Definition | A | R | C | C |
| Verfügbarkeitsmessung | I | A | R | - |
| SLA-Reporting | C | A | R | I |
| SLA-Review | A | R | C | C |
| Verbesserungsmaßnahmen | A | R | C | I |
| Incident-Response | I | A | R | I |
| Postmortems | C | A | R | I |

> **Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### Eskalationspfad

1. **Level 1:** Operations Team - Incident-Response und Monitoring
2. **Level 2:** {{ meta-organisation-roles.role_it_operations_manager.name }} - SLA-Verletzungen
3. **Level 3:** {{ meta-organisation-roles.role_cio.name }} - Kritische SLA-Verletzungen
4. **Level 4:** {{ meta-organisation-roles.role_ceo.name }} - Vertragliche Konsequenzen

## Compliance und Standards

### Relevante Standards
- **ITIL v4:** Availability Management Practice
- **ISO 20000:** Clause 8.9 - Availability Management
- **COBIT 2019:** DSS01 - Managed Operations

### Audit-Anforderungen
- SLA-Dokumentation und Verträge
- Verfügbarkeits-Reports und Metriken
- Incident-Dokumentation
- Verbesserungsmaßnahmen-Nachweise

## Anhang

### Glossar

| Begriff | Definition |
|---|---|
| SLA | Service Level Agreement - Vereinbarung über Serviceleistungen |
| SLO | Service Level Objective - Internes Serviceziel |
| SLI | Service Level Indicator - Messbare Metrik |
| MTBF | Mean Time Between Failures - Durchschnittliche Zeit zwischen Ausfällen |
| MTTR | Mean Time To Repair - Durchschnittliche Reparaturzeit |
| Error Budget | Tolerierbare Ausfallzeit innerhalb des SLO-Zeitraums |
| Uptime | Verfügbare Zeit eines Systems |
| Downtime | Ausfallzeit eines Systems |

### Referenzen
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework
- Site Reliability Engineering (Google)

**Letzte Aktualisierung:** {{ meta-handbook.date }}  
**Nächste Review:** [TODO: Datum]  
**Kontakt:** {{ meta-organisation-roles.role_it_operations_manager.email }}

