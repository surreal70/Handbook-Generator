# Betriebsübergabe und Go-Live-Checkliste

**Dokument-ID:** IT-OPERATION-0080
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

## Übersicht

Dieses Dokument beschreibt den Prozess der Betriebsübergabe und enthält eine umfassende Go-Live-Checkliste für die Überführung neuer oder geänderter IT-Services in den Produktivbetrieb.

**Service:** {{ meta-handbook.service_name }}  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**Stand:** 0

## Betriebsübergabe-Prozess

### Phasen der Betriebsübergabe

```
┌─────────────────┐
│ 1. Vorbereitung │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Dokumentation│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Training     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. Testing      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. Go-Live      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 6. Hypercare    │
└─────────────────┘
```

### Rollen und Verantwortlichkeiten

| Rolle | Verantwortung | Ansprechpartner |
|---|---|---|
| **Service Owner** | Gesamtverantwortung für Service | [TODO: Name] |
| **IT Operations Manager** | Betriebsübernahme koordinieren | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **Technical Lead** | Technische Implementierung | [TODO: Name] |
| **Service Desk Lead** | Support-Bereitschaft | {{ meta-organisation-roles.role_Service_Desk_Lead }} |
| **Change Manager** | Change-Genehmigung | [TODO: Name] |
| **CIO** | Finale Freigabe | [TODO] |

## Go-Live-Checkliste

### Phase 1: Vorbereitung (4-6 Wochen vor Go-Live)

#### Projektplanung
- [ ] Go-Live-Datum festgelegt und kommuniziert
- [ ] Projektteam zusammengestellt
- [ ] Rollen und Verantwortlichkeiten definiert
- [ ] Kommunikationsplan erstellt
- [ ] Risikobewertung durchgeführt
- [ ] Rollback-Plan erstellt

#### Infrastruktur
- [ ] Hardware beschafft und installiert
- [ ] Netzwerkanbindung konfiguriert
- [ ] Virtualisierung/Cloud-Ressourcen bereitgestellt
- [ ] Storage-Kapazität allokiert
- [ ] Backup-Infrastruktur eingerichtet
- [ ] Monitoring-Infrastruktur vorbereitet

#### Software und Lizenzen
- [ ] Software-Lizenzen beschafft
- [ ] Software installiert und konfiguriert
- [ ] Patches und Updates eingespielt
- [ ] Lizenz-Compliance geprüft
- [ ] Drittanbieter-Software integriert

### Phase 2: Dokumentation (3-4 Wochen vor Go-Live)

#### Betriebsdokumentation
- [ ] Betriebshandbuch erstellt (dieses Dokument)
- [ ] Systemarchitektur dokumentiert (Kapitel 0040)
- [ ] Infrastruktur dokumentiert (Kapitel 0050)
- [ ] Netzwerkdiagramme erstellt
- [ ] Konfigurationsdokumentation vollständig
- [ ] CMDB-Einträge erstellt (Kapitel 0090)

#### Prozessdokumentation
- [ ] Incident-Management-Prozess definiert (Kapitel 0120)
- [ ] Change-Management-Prozess definiert (Kapitel 0140)
- [ ] Backup-Prozess dokumentiert (Kapitel 0150)
- [ ] Monitoring-Prozess dokumentiert (Kapitel 0110)
- [ ] Eskalationspfade definiert (Kapitel 0070)

#### Runbooks und Anleitungen
- [ ] Standard-Runbooks erstellt (Kapitel 0240)
- [ ] Troubleshooting-Guides erstellt
- [ ] Notfall-Runbooks erstellt
- [ ] Wartungs-Checklisten erstellt
- [ ] FAQ-Dokument erstellt (Kapitel 0260)

### Phase 3: Training (2-3 Wochen vor Go-Live)

#### Service Desk Training
- [ ] Service-Übersicht präsentiert
- [ ] Incident-Handling trainiert
- [ ] Ticketing-System geschult
- [ ] Eskalationsprozesse erklärt
- [ ] FAQ und Known Issues durchgegangen
- [ ] Hands-on-Training durchgeführt

#### Operations Team Training
- [ ] Technische Architektur erklärt
- [ ] Monitoring-Tools geschult
- [ ] Backup/Restore-Prozeduren trainiert
- [ ] Change-Prozess durchgegangen
- [ ] Notfall-Prozeduren geübt
- [ ] Runbooks durchgearbeitet

#### Management Briefing
- [ ] Service-Übersicht präsentiert
- [ ] SLAs und KPIs erklärt
- [ ] Risiken und Mitigationen besprochen
- [ ] Eskalationsprozesse kommuniziert
- [ ] Reporting-Mechanismen erklärt

### Phase 4: Testing (1-2 Wochen vor Go-Live)

#### Funktionale Tests
- [ ] Unit-Tests durchgeführt
- [ ] Integrationstests durchgeführt
- [ ] End-to-End-Tests durchgeführt
- [ ] User Acceptance Tests (UAT) durchgeführt
- [ ] Performance-Tests durchgeführt
- [ ] Security-Tests durchgeführt

#### Betriebstests
- [ ] Backup-Test durchgeführt
- [ ] Restore-Test durchgeführt
- [ ] Failover-Test durchgeführt
- [ ] Monitoring-Alerts getestet
- [ ] Incident-Prozess getestet
- [ ] Eskalationsprozess getestet

#### Disaster Recovery Test
- [ ] DR-Plan getestet
- [ ] Failover zu DR-Site getestet
- [ ] Failback zu Primary Site getestet
- [ ] RTO/RPO validiert
- [ ] DR-Dokumentation aktualisiert

### Phase 5: Go-Live (Go-Live-Tag)

#### Pre-Go-Live (24 Stunden vorher)
- [ ] Go/No-Go-Meeting durchgeführt
- [ ] Alle Stakeholder informiert
- [ ] Wartungsfenster kommuniziert
- [ ] Rollback-Plan final geprüft
- [ ] Backup vor Go-Live erstellt
- [ ] Change-Ticket genehmigt

#### Go-Live-Aktivitäten
- [ ] Wartungsfenster gestartet
- [ ] Service-Migration durchgeführt
- [ ] Konfigurationsänderungen angewendet
- [ ] Smoke-Tests durchgeführt
- [ ] Monitoring aktiviert
- [ ] Service-Status kommuniziert

#### Post-Go-Live (unmittelbar nach Go-Live)
- [ ] Service-Verfügbarkeit bestätigt
- [ ] Monitoring-Dashboards geprüft
- [ ] Erste Transaktionen validiert
- [ ] Performance-Metriken geprüft
- [ ] Stakeholder informiert
- [ ] Go-Live-Protokoll erstellt

### Phase 6: Hypercare (1-4 Wochen nach Go-Live)

#### Hypercare-Support
- [ ] Erweiterte Support-Zeiten aktiviert
- [ ] Zusätzliche Ressourcen bereitgestellt
- [ ] Tägliche Status-Meetings durchgeführt
- [ ] Incident-Tracking intensiviert
- [ ] Performance-Monitoring verstärkt
- [ ] User-Feedback gesammelt

#### Stabilisierung
- [ ] Kritische Issues behoben
- [ ] Performance optimiert
- [ ] Dokumentation aktualisiert
- [ ] Known Issues dokumentiert
- [ ] Lessons Learned dokumentiert
- [ ] Post-Implementation-Review durchgeführt

## Übergabedokumentation

### Übergabe-Paket

Das Übergabe-Paket muss folgende Dokumente enthalten:

#### Technische Dokumentation
1. **Systemarchitektur** (Kapitel 0040)
   - Architekturdiagramme
   - Komponentenbeschreibungen
   - Datenflüsse
   - Abhängigkeiten

2. **Infrastruktur** (Kapitel 0050)
   - Hardware-Inventar
   - Netzwerkkonfiguration
   - IP-Adressierung
   - Virtualisierung/Cloud-Ressourcen

3. **Konfiguration** (Kapitel 0090)
   - Konfigurationsdateien
   - CMDB-Einträge
   - Netzwerk-Konfiguration
   - Security-Konfiguration

#### Betriebsdokumentation
4. **Betriebsprozesse** (Kapitel 0070)
   - Betriebsmodell
   - ITIL-Prozesse
   - Eskalationspfade
   - KPIs und Metriken

5. **Monitoring** (Kapitel 0110)
   - Monitoring-Strategie
   - Alert-Konfiguration
   - Dashboard-Übersichten
   - Schwellwerte

6. **Backup und Recovery** (Kapitel 0150)
   - Backup-Strategie
   - Backup-Zeitpläne
   - Restore-Prozeduren
   - RTO/RPO-Werte

#### Support-Dokumentation
7. **Runbooks** (Kapitel 0240)
   - Standard-Operationen
   - Troubleshooting-Guides
   - Notfall-Prozeduren
   - Wartungs-Checklisten

8. **Known Issues und FAQ** (Kapitel 0260)
   - Bekannte Probleme
   - Workarounds
   - Häufige Fragen
   - Lösungen

9. **Kontakte** (Kapitel 0270)
   - Ansprechpartner
   - Eskalationskontakte
   - Vendor-Kontakte
   - On-Call-Informationen

### Übergabe-Meeting

**Agenda:**
1. Service-Übersicht und Geschäftszweck
2. Technische Architektur und Infrastruktur
3. Betriebsprozesse und Verantwortlichkeiten
4. Monitoring und Alerting
5. Incident- und Problem-Management
6. Backup und Disaster Recovery
7. Known Issues und Risiken
8. Fragen und Antworten

**Teilnehmer:**
- Service Owner
- IT Operations Manager: {{ meta-organisation-roles.role_IT_Operations_Manager }}
- Technical Lead
- Service Desk Lead: {{ meta-organisation-roles.role_Service_Desk_Lead }}
- CIO: [TODO]

## Acceptance-Kriterien

### Technische Acceptance-Kriterien

| Kriterium | Anforderung | Status | Verifiziert durch |
|---|---|---|---|
| **Funktionalität** | Alle Features funktionieren gemäß Spezifikation | ☐ | [TODO] |
| **Performance** | Response-Zeiten < [TODO] ms | ☐ | [TODO] |
| **Verfügbarkeit** | Service erreichbar 24/7 | ☐ | [TODO] |
| **Skalierbarkeit** | Unterstützt [TODO] gleichzeitige Benutzer | ☐ | [TODO] |
| **Security** | Security-Tests bestanden | ☐ | [TODO] |
| **Backup** | Backup-Tests erfolgreich | ☐ | [TODO] |
| **Monitoring** | Alle Metriken werden erfasst | ☐ | [TODO] |
| **Integration** | Alle Schnittstellen funktionieren | ☐ | [TODO] |

### Betriebliche Acceptance-Kriterien

| Kriterium | Anforderung | Status | Verifiziert durch |
|---|---|---|---|
| **Dokumentation** | Vollständige Betriebsdokumentation | ☐ | IT Ops Manager |
| **Training** | Team geschult und einsatzbereit | ☐ | Service Desk Lead |
| **Runbooks** | Alle Runbooks erstellt und getestet | ☐ | IT Ops Manager |
| **CMDB** | Alle CIs dokumentiert | ☐ | CMDB Manager |
| **SLA** | SLAs definiert und vereinbart | ☐ | Service Manager |
| **Support** | Support-Prozesse etabliert | ☐ | Service Desk Lead |
| **Monitoring** | Monitoring aktiv und funktional | ☐ | Monitoring Team |
| **Backup** | Backup-Prozess etabliert | ☐ | Backup Admin |

### Geschäftliche Acceptance-Kriterien

| Kriterium | Anforderung | Status | Verifiziert durch |
|---|---|---|---|
| **Business Requirements** | Alle Geschäftsanforderungen erfüllt | ☐ | Service Owner |
| **User Acceptance** | UAT erfolgreich abgeschlossen | ☐ | Business Users |
| **Compliance** | Compliance-Anforderungen erfüllt | ☐ | Compliance Officer |
| **Budget** | Innerhalb des Budgets | ☐ | [TODO] |
| **Timeline** | Zeitplan eingehalten | ☐ | Project Manager |

## Go/No-Go-Entscheidung

### Go/No-Go-Meeting

**Zeitpunkt:** 24 Stunden vor geplantem Go-Live  
**Teilnehmer:**
- Service Owner
- IT Operations Manager: {{ meta-organisation-roles.role_IT_Operations_Manager }}
- Technical Lead
- Change Manager
- CIO: [TODO]

### Entscheidungskriterien

| Kriterium | Go | No-Go | Status |
|---|---|---|---|
| **Alle Tests bestanden** | ✓ | ✗ | ☐ |
| **Dokumentation vollständig** | ✓ | ✗ | ☐ |
| **Team trainiert** | ✓ | ✗ | ☐ |
| **Keine kritischen Issues** | ✓ | ✗ | ☐ |
| **Rollback-Plan vorhanden** | ✓ | ✗ | ☐ |
| **Stakeholder informiert** | ✓ | ✗ | ☐ |
| **Change genehmigt** | ✓ | ✗ | ☐ |
| **Backup erstellt** | ✓ | ✗ | ☐ |

**Entscheidung:** ☐ GO ☐ NO-GO

**Begründung:** [TODO]

**Unterschriften:**
- Service Owner: _________________ Datum: _______
- IT Operations Manager: _________________ Datum: _______
- CIO: _________________ Datum: _______

## Rollback-Plan

### Rollback-Trigger

Rollback wird ausgelöst bei:
- Kritischen Funktionsausfällen
- Schwerwiegenden Performance-Problemen
- Datenverlust oder Datenkorruption
- Security-Incidents
- Nicht erfüllten Acceptance-Kriterien

### Rollback-Prozedur

1. **Entscheidung:** IT Operations Manager entscheidet über Rollback
2. **Kommunikation:** Stakeholder informieren
3. **Wartungsfenster:** Falls erforderlich, Wartungsfenster aktivieren
4. **Backup-Restore:** Letztes funktionierendes Backup wiederherstellen
5. **Konfiguration:** Alte Konfiguration wiederherstellen
6. **Validierung:** Funktionalität prüfen
7. **Kommunikation:** Rollback-Abschluss kommunizieren
8. **Post-Mortem:** Ursachenanalyse durchführen

### Rollback-Zeitfenster

- **Innerhalb 4 Stunden nach Go-Live:** Schneller Rollback möglich
- **4-24 Stunden nach Go-Live:** Rollback mit erhöhtem Aufwand
- **Nach 24 Stunden:** Rollback nur nach sorgfältiger Analyse

## Post-Implementation-Review

### Review-Meeting

**Zeitpunkt:** 2-4 Wochen nach Go-Live  
**Teilnehmer:** Alle Projektbeteiligten

**Agenda:**
1. Go-Live-Verlauf Review
2. Lessons Learned
3. Issues und Resolutionen
4. Performance-Analyse
5. User-Feedback
6. Verbesserungsvorschläge
7. Nächste Schritte

### Lessons Learned

| Kategorie | Was lief gut? | Was lief schlecht? | Verbesserungen |
|---|---|---|---|
| **Planung** | [TODO] | [TODO] | [TODO] |
| **Kommunikation** | [TODO] | [TODO] | [TODO] |
| **Testing** | [TODO] | [TODO] | [TODO] |
| **Training** | [TODO] | [TODO] | [TODO] |
| **Go-Live** | [TODO] | [TODO] | [TODO] |
| **Support** | [TODO] | [TODO] | [TODO] |

### Metriken nach Go-Live

| Metrik | Zielwert | Ist-Wert | Status |
|---|---:|---:|---|
| **Verfügbarkeit (erste Woche)** | ≥ 99% | [TODO]% | ☐ |
| **Incidents (erste Woche)** | ≤ 10 | [TODO] | ☐ |
| **MTTR (erste Woche)** | ≤ 4h | [TODO]h | ☐ |
| **User Satisfaction** | ≥ 80% | [TODO]% | ☐ |
| **Performance** | < [TODO] ms | [TODO] ms | ☐ |

## Kontakte

**Go-Live-Team:**
- **Service Owner:** [TODO: Name] - [TODO: E-Mail]
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} - {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Technical Lead:** [TODO: Name] - [TODO: E-Mail]
- **Service Desk Lead:** {{ meta-organisation-roles.role_Service_Desk_Lead }} - {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **Change Manager:** [TODO: Name] - [TODO: E-Mail]
- **CIO:** [TODO] - {{ meta-organisation-roles.role_CIO_email }}

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Organisation:** AdminSend GmbH

