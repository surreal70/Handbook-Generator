# Betriebskonzept und Betriebsprozesse

**Dokument-ID:** [FRAMEWORK]-0070
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

## Übersicht

Dieses Dokument beschreibt das Betriebskonzept und die Betriebsprozesse für den IT-Service. Es definiert Betriebsmodelle, Prozessabläufe nach ITIL-Standards, Schnittstellen zu anderen Prozessen und Eskalationspfade.

**Service:** {{ meta-handbook.service_name }}  
**Verantwortlich:** {{ meta-organisation-roles.role_it_operations_manager.name }}  
**Stand:** {{ meta-handbook.revision }}

## Betriebsmodell

### Servicezeiten

| Betriebsmodell | Beschreibung | Servicezeiten |
|---|---|---|
| **24/7 Betrieb** | Durchgehender Betrieb ohne Unterbrechung | Mo-So, 00:00-24:00 Uhr |
| **Business Hours** | Betrieb während Geschäftszeiten | Mo-Fr, 08:00-18:00 Uhr |
| **Extended Hours** | Erweiterte Geschäftszeiten | Mo-Fr, 06:00-22:00 Uhr |
| **Follow-the-Sun** | Globaler Betrieb über Zeitzonen | 24/7 mit regionaler Staffelung |

**Aktuelles Betriebsmodell:** [TODO: Betriebsmodell auswählen]

### Wartungsfenster

| Typ | Zeitfenster | Frequenz | Dauer |
|---|---|---|---|
| **Reguläre Wartung** | [TODO: z.B. Sonntag 02:00-06:00] | [TODO: z.B. Monatlich] | [TODO: z.B. 4 Stunden] |
| **Notfallwartung** | Nach Bedarf | Ad-hoc | Variable |
| **Patch-Fenster** | [TODO: z.B. Dienstag 22:00-24:00] | [TODO: z.B. Wöchentlich] | [TODO: z.B. 2 Stunden] |

### Support-Modell

**Support-Stufen:**
- **Level 1 (Service Desk):** {{ meta-organisation-roles.role_service_desk_lead.name }} - {{ meta-organisation-roles.role_service_desk_lead.email }}
- **Level 2 (IT Operations):** {{ meta-organisation-roles.role_it_operations_manager.name }} - {{ meta-organisation-roles.role_it_operations_manager.email }}
- **Level 3 (Specialist/Vendor):** [TODO: Spezialist-Kontakt]

**Rufbereitschaft:**
- **On-Call Rotation:** [TODO: Rotationsplan beschreiben]
- **Erreichbarkeit:** [TODO: Telefon/Pager-Nummer]
- **Reaktionszeit:** [TODO: z.B. 15 Minuten]

## ITIL-Prozesse

### Service Strategy

**Ziel:** Strategische Ausrichtung der IT-Services an Geschäftsanforderungen

**Aktivitäten:**
- Service Portfolio Management
- Financial Management
- Demand Management
- Business Relationship Management

**Verantwortlich:** {{ meta-organisation-roles.role_cio.name }}

### Service Design

**Ziel:** Design neuer oder geänderter Services für den Produktivbetrieb

**Aktivitäten:**
- Service Catalogue Management
- Service Level Management
- Capacity Management
- Availability Management
- IT Service Continuity Management
- Information Security Management
- Supplier Management

**Verantwortlich:** {{ meta-organisation-roles.role_it_operations_manager.name }}

### Service Transition

**Ziel:** Überführung neuer oder geänderter Services in den Produktivbetrieb

**Aktivitäten:**
- Change Management (siehe Kapitel 0140)
- Release and Deployment Management
- Service Validation and Testing
- Knowledge Management
- Configuration Management (siehe Kapitel 0090)

**Verantwortlich:** {{ meta-organisation-roles.role_it_operations_manager.name }}

### Service Operation

**Ziel:** Sicherstellung des effektiven und effizienten Betriebs

**Aktivitäten:**
- Incident Management (siehe Kapitel 0120)
- Problem Management (siehe Kapitel 0130)
- Event Management
- Request Fulfillment
- Access Management (siehe Kapitel 0100)

**Verantwortlich:** {{ meta-organisation-roles.role_service_desk_lead.name }} (Level 1), {{ meta-organisation-roles.role_it_operations_manager.name }} (Level 2)

### Continual Service Improvement (CSI)

**Ziel:** Kontinuierliche Verbesserung der Service-Qualität

**Aktivitäten:**
- Service Measurement and Reporting
- Service Review
- Process Improvement
- Root Cause Analysis

**Verantwortlich:** {{ meta-organisation-roles.role_cio.name }}

## Prozessschnittstellen

### Schnittstellen zu anderen IT-Prozessen

| Prozess | Schnittstelle | Informationsfluss | Verantwortlich |
|---|---|---|---|
| **Incident Management** | Störungsmeldungen → Betrieb | Incidents, Workarounds | Service Desk |
| **Change Management** | Change Requests → Betrieb | Changes, RFCs | CAB |
| **Problem Management** | Known Errors → Betrieb | Problem Records, Solutions | Problem Manager |
| **Configuration Management** | CI-Updates → CMDB | Configuration Items | CMDB Manager |
| **Capacity Management** | Kapazitätsdaten → Planung | Performance Metrics | Capacity Manager |
| **Availability Management** | Verfügbarkeitsdaten → Reporting | Availability Reports | Availability Manager |
| **Security Management** | Security Events → Betrieb | Security Incidents, Patches | {{ meta-organisation-roles.role_ciso.name }} |
| **Backup Management** | Backup-Status → Betrieb | Backup Reports, Restore Requests | Backup Administrator |

### Schnittstellen zu Geschäftsprozessen

| Geschäftsprozess | Schnittstelle | Informationsfluss | Ansprechpartner |
|---|---|---|---|
| **Beschaffung** | Hardware/Software-Anforderungen | Bestellungen, Lieferungen | Procurement |
| **Finanzen** | Budget und Kosten | Kostenberichte, Budgetanfragen | {{ meta-organisation-roles.role_cfo.name }} |
| **Compliance** | Audit-Anforderungen | Audit-Berichte, Nachweise | Compliance Officer |
| **HR** | Mitarbeiter-Onboarding/Offboarding | Zugriffsverwaltung | HR Department |

## Eskalationspfade

### Technische Eskalation

```
┌─────────────────────────────────────────────────────────────┐
│ Level 1: Service Desk                                        │
│ Kontakt: {{ meta-organisation-roles.role_service_desk_lead.name }}                   │
│ E-Mail: {{ meta-organisation-roles.role_service_desk_lead.email }}                   │
│ Telefon: {{ meta-organisation-roles.role_service_desk_lead.phone }}                  │
│ Eskalation nach: 30 Minuten (P1), 2 Stunden (P2)            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Level 2: IT Operations                                       │
│ Kontakt: {{ meta-organisation-roles.role_it_operations_manager.name }}               │
│ E-Mail: {{ meta-organisation-roles.role_it_operations_manager.email }}               │
│ Telefon: {{ meta-organisation-roles.role_it_operations_manager.phone }}              │
│ Eskalation nach: 1 Stunde (P1), 4 Stunden (P2)              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Level 3: Specialist/Vendor                                   │
│ Kontakt: [TODO: Spezialist-Name]                            │
│ E-Mail: [TODO: Spezialist-E-Mail]                           │
│ Telefon: [TODO: Spezialist-Telefon]                         │
│ Eskalation nach: 2 Stunden (P1), 8 Stunden (P2)             │
└─────────────────────────────────────────────────────────────┘
```

### Management-Eskalation

```
┌─────────────────────────────────────────────────────────────┐
│ Stufe 1: IT Operations Manager                               │
│ Kontakt: {{ meta-organisation-roles.role_it_operations_manager.name }}               │
│ E-Mail: {{ meta-organisation-roles.role_it_operations_manager.email }}               │
│ Eskalation bei: Kritische Incidents (P1), SLA-Verletzung    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Stufe 2: Chief Information Officer (CIO)                     │
│ Kontakt: {{ meta-organisation-roles.role_cio.name }}                                 │
│ E-Mail: {{ meta-organisation-roles.role_cio.email }}                                 │
│ Eskalation bei: Major Incidents, Business Impact            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Stufe 3: Chief Executive Officer (CEO)                       │
│ Kontakt: {{ meta-organisation-roles.role_ceo.name }}                                 │
│ E-Mail: {{ meta-organisation-roles.role_ceo.email }}                                 │
│ Eskalation bei: Unternehmenskritische Ausfälle              │
└─────────────────────────────────────────────────────────────┘
```

### Eskalationskriterien

| Priorität | Technische Eskalation | Management-Eskalation | Zeitrahmen |
|---|---|---|---|
| **P1 (Kritisch)** | Nach 30 Min (L1→L2), 1h (L2→L3) | Sofort an IT Ops Manager | Sofort |
| **P2 (Hoch)** | Nach 2h (L1→L2), 4h (L2→L3) | Nach 4 Stunden an IT Ops Manager | 4 Stunden |
| **P3 (Mittel)** | Nach 8h (L1→L2), 1 Tag (L2→L3) | Nach 1 Tag an IT Ops Manager | 1 Tag |
| **P4 (Niedrig)** | Nach 2 Tagen (L1→L2) | Keine automatische Eskalation | 2 Tage |

## Betriebsprozess-Übersicht

### Tägliche Betriebsroutinen

**Morgen-Check (08:00 Uhr):**
- [ ] Monitoring-Dashboards prüfen
- [ ] Backup-Status überprüfen
- [ ] Offene Incidents reviewen
- [ ] System-Health-Check durchführen
- [ ] Log-Dateien auf Anomalien prüfen

**Tages-Betrieb:**
- [ ] Incident-Bearbeitung nach Priorität
- [ ] Change-Implementierungen durchführen
- [ ] Monitoring und Alerting überwachen
- [ ] Dokumentation aktualisieren
- [ ] Kommunikation mit Stakeholdern

**Abend-Check (18:00 Uhr):**
- [ ] Tages-Incidents abschließen oder übergeben
- [ ] Backup-Läufe initiieren
- [ ] Wartungsarbeiten vorbereiten
- [ ] Handover an Nachtschicht (falls 24/7)
- [ ] Tagesbericht erstellen

### Wöchentliche Aktivitäten

- [ ] Service-Review-Meeting (Montag)
- [ ] Patch-Management (Dienstag Abend)
- [ ] Kapazitäts-Review (Mittwoch)
- [ ] Problem-Management-Meeting (Donnerstag)
- [ ] Wochenabschluss und Reporting (Freitag)

### Monatliche Aktivitäten

- [ ] Service-Level-Reporting
- [ ] Kapazitätsplanung
- [ ] Security-Patch-Review
- [ ] Disaster-Recovery-Test
- [ ] Compliance-Check
- [ ] Vendor-Review

## Prozess-Metriken und KPIs

### Betriebsmetriken

| Metrik | Zielwert | Messfrequenz | Verantwortlich |
|---|---:|---|---|
| **Service Availability** | ≥ 99.5% | Täglich | IT Operations |
| **Mean Time To Repair (MTTR)** | ≤ 4 Stunden | Pro Incident | Service Desk |
| **Mean Time Between Failures (MTBF)** | ≥ 720 Stunden | Monatlich | IT Operations |
| **First Call Resolution Rate** | ≥ 70% | Wöchentlich | Service Desk |
| **Change Success Rate** | ≥ 95% | Monatlich | Change Manager |
| **Backup Success Rate** | 100% | Täglich | Backup Admin |

### Prozess-KPIs

| KPI | Zielwert | Messfrequenz | Verantwortlich |
|---|---:|---|---|
| **Incident Resolution Time (P1)** | ≤ 4 Stunden | Pro Incident | Service Desk |
| **Incident Resolution Time (P2)** | ≤ 8 Stunden | Pro Incident | Service Desk |
| **Change Lead Time** | ≤ 5 Tage | Pro Change | Change Manager |
| **Problem Resolution Time** | ≤ 30 Tage | Pro Problem | Problem Manager |
| **SLA Compliance** | ≥ 98% | Monatlich | Service Manager |

## Kontinuierliche Verbesserung

### CSI-Prozess

1. **Identifikation:** Verbesserungspotenziale identifizieren
2. **Analyse:** Root-Cause-Analyse durchführen
3. **Planung:** Verbesserungsmaßnahmen planen
4. **Implementierung:** Maßnahmen umsetzen
5. **Messung:** Erfolg messen und validieren
6. **Review:** Ergebnisse reviewen und dokumentieren

### Verbesserungsquellen

- Incident-Analysen und Trends
- Problem-Management-Erkenntnisse
- Service-Review-Meetings
- Kundenfeedback
- Audit-Ergebnisse
- Benchmark-Vergleiche

### Verbesserungs-Register

| ID | Verbesserung | Priorität | Status | Verantwortlich | Zieldatum |
|---|---|---|---|---|---|
| CSI-001 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| CSI-002 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## Dokumentation und Wissensmanagement

### Dokumentations-Repository

- **Betriebshandbücher:** Zentrale Ablage für alle Betriebsdokumente
- **Runbooks:** Standardisierte Ablaufbeschreibungen
- **Known Error Database:** Bekannte Fehler und Lösungen
- **Configuration Management Database (CMDB):** CI-Dokumentation
- **Change-Historie:** Dokumentation aller Changes

### Wissenstransfer

- **Onboarding:** Einarbeitung neuer Mitarbeiter
- **Training:** Regelmäßige Schulungen
- **Documentation:** Kontinuierliche Dokumentation
- **Knowledge Sharing:** Team-Meetings und Workshops
- **Lessons Learned:** Post-Incident-Reviews

## Compliance und Governance

### Relevante Standards

- **ITIL v4:** IT Service Management Framework
- **ISO 20000:** IT Service Management Standard
- **ISO 27001:** Information Security Management
- **COBIT 2019:** IT Governance Framework

### Audit-Anforderungen

- Dokumentation aller Betriebsprozesse
- Nachweisbare Einhaltung von SLAs
- Change-Management-Protokolle
- Incident-Management-Berichte
- Compliance-Nachweise

## Kontakte

**Betriebsverantwortliche:**
- **IT Operations Manager:** {{ meta-organisation-roles.role_it_operations_manager.name }} - {{ meta-organisation-roles.role_it_operations_manager.email }}
- **Service Desk Lead:** {{ meta-organisation-roles.role_service_desk_lead.name }} - {{ meta-organisation-roles.role_service_desk_lead.email }}
- **CIO:** {{ meta-organisation-roles.role_cio.name }} - {{ meta-organisation-roles.role_cio.email }}

**Weitere Kontakte:** Siehe Kapitel 0270 (Kontakte, Eskalation und Anbieter)

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

