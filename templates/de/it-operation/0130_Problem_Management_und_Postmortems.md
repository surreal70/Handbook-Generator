# Problem Management und Postmortems

**Dokument-ID:** [FRAMEWORK]-0130
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

## Zweck und Geltungsbereich

Dieses Dokument beschreibt den Problem-Management-Prozess für {{ meta-organisation.name }} gemäß ITIL v4 Best Practices. Es definiert die systematische Analyse wiederkehrender Incidents, Root-Cause-Analysis-Methoden, Postmortem-Prozesse und die Verwaltung der Known Error Database.

**Geltungsbereich:** Alle IT-Services und -Systeme von {{ meta-organisation.name }}

**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_email }})

## Problem-Definition

Ein **Problem** ist die unbekannte Ursache eines oder mehrerer Incidents. Das Ziel des Problem Managements ist die Identifikation und Beseitigung der Grundursache, um zukünftige Incidents zu verhindern.

### Abgrenzung Incident vs. Problem

| Aspekt | Incident | Problem |
|---|---|---|
| **Fokus** | Symptome | Ursachen |
| **Ziel** | Schnelle Wiederherstellung | Dauerhafte Lösung |
| **Zeitrahmen** | Sofort | Geplant |
| **Ansatz** | Workaround | Root-Cause-Elimination |
| **Prozess** | Reaktiv | Proaktiv |

## Problem-Management-Prozess

### Prozessübersicht (ITIL v4)

```
┌─────────────────┐
│ Problem         │
│ Detection       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Logging         │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Categorization  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Prioritization  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Investigation   │
│ & Diagnosis     │
│ (RCA)           │
└────────┬────────┘
         │
┌────────▼────────┐
│ Workaround      │
│ Identification  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Known Error     │
│ Recording       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Resolution      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Closure         │
└─────────────────┘
```

### 1. Problem Detection

**Erkennungsquellen:**
- Wiederkehrende Incidents (> 3x in 30 Tagen)
- Trend-Analyse von Incident-Daten
- Proaktive Monitoring-Analysen
- Major Incident Reviews
- Vendor-Bulletins und Security-Advisories

**Trigger für Problem-Erstellung:**
- Mehrere ähnliche Incidents
- Incidents mit hohem Business-Impact
- Incidents ohne bekannte Lösung
- Strukturelle Schwachstellen

**Verantwortlich:** Problem Manager, IT Operations Team

### 2. Problem Logging

**Erforderliche Informationen:**
- Problem-ID (automatisch generiert)
- Verknüpfte Incident-IDs
- Symptombeschreibung
- Betroffene Services/Systeme
- Betroffene Configuration Items (CIs)
- Erste Hypothesen zur Ursache

**Tool:** {{ meta-handbook.ticketing_system }}

**Verantwortlich:** Problem Manager

### 3. Problem Categorization

**Kategorien:**
- Hardware-Probleme
- Software-Probleme
- Netzwerk-Probleme
- Prozess-Probleme
- Dokumentations-Probleme
- Kapazitäts-Probleme
- Sicherheits-Probleme

**Verantwortlich:** Problem Manager

### 4. Problem Prioritization

**Prioritäts-Faktoren:**
- Anzahl betroffener Incidents
- Business-Impact
- Häufigkeit des Auftretens
- Verfügbarkeit von Workarounds
- Ressourcen-Verfügbarkeit

**Prioritäts-Stufen:**

| Priorität | Beschreibung | Bearbeitungszeit |
|---|---|---|
| **P1 - Kritisch** | Häufige P1-Incidents, kein Workaround | Sofort |
| **P2 - Hoch** | Häufige P2-Incidents, temporärer Workaround | 1 Woche |
| **P3 - Mittel** | Moderate Häufigkeit, Workaround vorhanden | 1 Monat |
| **P4 - Niedrig** | Seltene Incidents, geringer Impact | Geplant |

### 5. Investigation & Diagnosis (Root Cause Analysis)

**RCA-Methoden:**
- 5-Why-Analyse
- Fishbone-Diagramm (Ishikawa)
- Fault Tree Analysis
- Timeline-Analyse
- Log-Korrelation

**Aktivitäten:**
- Daten sammeln (Logs, Monitoring, Konfigurationen)
- Hypothesen entwickeln
- Tests durchführen
- Root-Cause identifizieren
- Dokumentation erstellen

**Verantwortlich:** Problem Manager, Technical Specialists

### 6. Workaround Identification

**Workaround-Kriterien:**
- Reduziert Impact oder Häufigkeit
- Praktikabel für Incident-Teams
- Dokumentiert und getestet
- Temporäre Lösung bis zur permanenten Behebung

**Dokumentation:**
- Workaround-Beschreibung
- Anwendungsschritte
- Einschränkungen
- Gültigkeitsdauer

### 7. Known Error Recording

**Known Error Database (KEDB):**
- Problem-Beschreibung
- Root-Cause
- Workaround
- Permanente Lösung (wenn verfügbar)
- Verknüpfte Incidents
- Verknüpfte CIs

**Zugriff:** Alle IT-Mitarbeiter (Read), Problem Manager (Write)

### 8. Problem Resolution

**Lösungsansätze:**
- Software-Patch oder -Update
- Konfigurationsänderung
- Hardware-Austausch
- Prozess-Verbesserung
- Dokumentations-Update
- Training

**Change-Management:**
- Permanente Lösungen erfordern Change-Request
- Change-Planung und -Genehmigung
- Implementierung über Change-Prozess

### 9. Problem Closure

**Closure-Kriterien:**
- Root-Cause identifiziert und dokumentiert
- Permanente Lösung implementiert
- Keine neuen Incidents aufgetreten (Monitoring-Periode)
- Dokumentation vollständig
- Lessons Learned dokumentiert

**Verantwortlich:** Problem Manager

## Root Cause Analysis (RCA) Methoden

### 5-Why-Analyse

**Methode:** Fünfmal "Warum?" fragen, um zur Grundursache zu gelangen

**Beispiel:**
1. **Warum** ist die Datenbank ausgefallen? → Disk voll
2. **Warum** war die Disk voll? → Log-Dateien nicht rotiert
3. **Warum** wurden Logs nicht rotiert? → Logrotate-Job fehlgeschlagen
4. **Warum** ist der Job fehlgeschlagen? → Falsche Cron-Konfiguration
5. **Warum** war die Konfiguration falsch? → Keine Validierung nach Change

**Root-Cause:** Fehlende Change-Validierung

### Fishbone-Diagramm (Ishikawa)

**Kategorien:**
- **Menschen:** Fehler, Wissen, Training
- **Methoden:** Prozesse, Verfahren, Standards
- **Maschinen:** Hardware, Software, Tools
- **Material:** Daten, Konfigurationen, Dokumentation
- **Umgebung:** Infrastruktur, Netzwerk, Standort
- **Management:** Entscheidungen, Ressourcen, Prioritäten

**Anwendung:**
1. Problem als "Fischkopf" definieren
2. Hauptkategorien als "Gräten" zeichnen
3. Ursachen pro Kategorie identifizieren
4. Tiefere Ursachen als Unter-Gräten hinzufügen
5. Root-Cause identifizieren

### Timeline-Analyse

**Methode:** Chronologische Rekonstruktion der Ereignisse

**Schritte:**
1. Zeitstrahl erstellen
2. Alle relevanten Events eintragen
3. Kausalitäten identifizieren
4. Kritischen Pfad herausarbeiten
5. Root-Cause am Anfang der Kausalkette finden

**Datenquellen:**
- Incident-Tickets
- Change-Records
- Monitoring-Logs
- System-Logs
- Deployment-Historie

## Postmortem-Prozess

### Postmortem-Definition

Ein **Postmortem** ist eine strukturierte Analyse eines Major Incidents oder kritischen Problems mit dem Ziel, Lessons Learned zu identifizieren und Verbesserungen umzusetzen.

### Postmortem-Trigger

**Pflicht-Postmortems bei:**
- Major Incidents (P1)
- Service-Ausfälle > 4 Stunden
- Datenverlust oder Security-Breach
- Incidents mit Medienaufmerksamkeit
- Wiederholte Incidents trotz vorheriger Lösung

**Optional-Postmortems bei:**
- P2-Incidents mit interessanten Lessons Learned
- Erfolgreiche Incident-Bewältigung (Best Practices)
- Near-Miss-Situationen

### Postmortem-Timeline

| Phase | Zeitpunkt | Aktivität |
|---|---|---|
| **Initiierung** | Innerhalb 24h | Postmortem ankündigen, Teilnehmer einladen |
| **Datensammlung** | 24-48h | Logs, Timelines, Fakten sammeln |
| **Meeting** | Innerhalb 1 Woche | Postmortem-Meeting durchführen |
| **Dokumentation** | Innerhalb 2 Wochen | Postmortem-Report finalisieren |
| **Follow-up** | Laufend | Action Items umsetzen und tracken |

### Postmortem-Meeting

**Teilnehmer:**
- Incident Manager
- Betroffene Teams
- Service Owner
- Management (bei Major Incidents)
- Optional: Externe Stakeholder

**Agenda:**
1. **Incident-Übersicht** (5 Min)
   - Was ist passiert?
   - Wann ist es passiert?
   - Wer war betroffen?

2. **Timeline-Review** (15 Min)
   - Chronologische Ereignisse
   - Entscheidungspunkte
   - Kommunikation

3. **Root-Cause-Analysis** (20 Min)
   - 5-Why oder Fishbone
   - Beitragende Faktoren
   - Grundursache

4. **What Went Well** (10 Min)
   - Erfolgreiche Maßnahmen
   - Gute Zusammenarbeit
   - Effektive Tools

5. **What Went Wrong** (10 Min)
   - Probleme und Verzögerungen
   - Kommunikationsprobleme
   - Tool- oder Prozess-Mängel

6. **Action Items** (15 Min)
   - Verbesserungsmaßnahmen
   - Verantwortliche
   - Deadlines

**Dauer:** 60-90 Minuten

**Moderator:** Problem Manager oder neutraler Facilitator

### Postmortem-Prinzipien

**Blameless Culture:**
- Fokus auf Systeme und Prozesse, nicht auf Personen
- Keine Schuldzuweisungen
- Psychologische Sicherheit
- Lernen aus Fehlern

**Faktenbasiert:**
- Objektive Daten (Logs, Metriken)
- Keine Spekulationen
- Verifizierbare Aussagen

**Konstruktiv:**
- Lösungsorientiert
- Konkrete Action Items
- Umsetzbare Verbesserungen

## Postmortem-Template

### 1. Executive Summary

**Incident-Übersicht:**
- **Incident-ID:** [ID]
- **Datum/Zeit:** [Start] - [Ende]
- **Dauer:** [Stunden]
- **Priorität:** P1 / P2
- **Betroffener Service:** [Service-Name]
- **Impact:** [Anzahl Nutzer, Business-Impact]

**Zusammenfassung:**
[2-3 Sätze: Was ist passiert und was war die Ursache?]

### 2. Timeline

| Zeit | Event | Aktion | Verantwortlich |
|---|---|---|---|
| 10:00 | Alert: Database CPU 100% | Monitoring-Alert ausgelöst | Monitoring-System |
| 10:05 | Service Desk erhält Anrufe | Incident-Ticket erstellt | Service Desk |
| 10:15 | Eskalation an DBA-Team | Datenbank-Analyse gestartet | IT Operations |
| 10:30 | Root-Cause identifiziert | Slow Query gefunden | DBA-Team |
| 10:45 | Query optimiert | Deployment durchgeführt | DBA-Team |
| 11:00 | Service wiederhergestellt | Monitoring bestätigt | IT Operations |

### 3. Root Cause Analysis

**5-Why-Analyse:**
1. Warum war die Datenbank überlastet? → Slow Query
2. Warum gab es eine Slow Query? → Fehlender Index
3. Warum fehlte der Index? → Nicht im Deployment enthalten
4. Warum war er nicht im Deployment? → Nicht in Code-Review erkannt
5. Warum wurde es nicht erkannt? → Keine Performance-Tests

**Root-Cause:** Fehlende Performance-Tests im CI/CD-Pipeline

**Beitragende Faktoren:**
- Unzureichende Code-Review-Checkliste
- Keine automatisierten Query-Analysen
- Fehlende Staging-Umgebung mit Produktions-Datenvolumen

### 4. Impact Assessment

**Technischer Impact:**
- Datenbank-CPU: 100% für 60 Minuten
- Antwortzeiten: > 30 Sekunden (normal: < 1s)
- Service-Verfügbarkeit: 0% für 60 Minuten

**Business-Impact:**
- Betroffene Nutzer: 500 (100%)
- Geschäftsprozesse blockiert: Order Processing
- Geschätzter Umsatzverlust: [Betrag]
- Reputationsschaden: Mittel

**SLA-Impact:**
- SLA-Ziel: 99.9% Verfügbarkeit
- Tatsächliche Verfügbarkeit: 99.86%
- SLA-Verstoß: Ja

### 5. What Went Well

- ✅ Schnelle Eskalation an DBA-Team (10 Minuten)
- ✅ Effektive Kommunikation zwischen Teams
- ✅ Root-Cause schnell identifiziert (25 Minuten)
- ✅ Lösung erfolgreich implementiert
- ✅ Keine Datenverluste

### 6. What Went Wrong

- ❌ Slow Query nicht vor Deployment erkannt
- ❌ Keine automatischen Performance-Tests
- ❌ Staging-Umgebung nicht repräsentativ
- ❌ Monitoring-Alert zu spät (CPU-Threshold zu hoch)
- ❌ Rollback-Prozedur nicht dokumentiert

### 7. Action Items

| ID | Maßnahme | Verantwortlich | Deadline | Status |
|---|---|---|---|---|
| AI-001 | Performance-Tests in CI/CD integrieren | DevOps-Team | 2 Wochen | Open |
| AI-002 | Code-Review-Checkliste erweitern | Dev-Team | 1 Woche | Open |
| AI-003 | Staging-Datenbank mit Prod-Volumen | DBA-Team | 1 Monat | Open |
| AI-004 | Monitoring-Thresholds anpassen | Ops-Team | 1 Woche | Open |
| AI-005 | Rollback-Runbook erstellen | DBA-Team | 2 Wochen | Open |

### 8. Lessons Learned

**Technisch:**
- Performance-Tests sind essentiell vor Deployments
- Staging-Umgebung muss Produktions-Datenvolumen simulieren
- Automatisierte Query-Analyse kann Probleme früh erkennen

**Prozess:**
- Code-Review-Checklisten müssen Performance-Aspekte abdecken
- Rollback-Prozeduren müssen dokumentiert und getestet sein
- Monitoring-Thresholds müssen regelmäßig überprüft werden

**Organisatorisch:**
- Team-Kommunikation funktionierte gut
- Eskalationsprozesse waren effektiv
- Dokumentation muss verbessert werden

### 9. Follow-up

**Review-Termin:** [Datum, 4 Wochen nach Incident]

**Review-Agenda:**
- Status aller Action Items
- Wirksamkeit der Maßnahmen
- Weitere Verbesserungen

**Verantwortlich:** Problem Manager

## Known Error Database (KEDB)

### KEDB-Struktur

**Erforderliche Felder:**
- **Known-Error-ID:** Eindeutige Kennung
- **Titel:** Kurzbeschreibung
- **Symptome:** Wie äußert sich das Problem?
- **Root-Cause:** Identifizierte Grundursache
- **Workaround:** Temporäre Lösung
- **Permanente Lösung:** Dauerhafte Behebung (wenn verfügbar)
- **Betroffene CIs:** Configuration Items
- **Verknüpfte Incidents:** Incident-IDs
- **Verknüpfte Problems:** Problem-IDs
- **Status:** Open, Workaround Available, Resolved, Closed
- **Priorität:** P1-P4
- **Erstellt:** Datum, Autor
- **Aktualisiert:** Datum, Autor

### KEDB-Beispiel

**Known-Error-ID:** KE-2024-001

**Titel:** PostgreSQL Connection Pool Exhaustion

**Symptome:**
- Applikation meldet "Connection timeout"
- Datenbank-Logs zeigen "too many connections"
- Monitoring zeigt 100% Connection-Pool-Auslastung

**Root-Cause:**
- Connection-Pool-Limit zu niedrig konfiguriert (max_connections=100)
- Applikation gibt Connections nicht korrekt frei (Connection Leak)
- Fehlende Connection-Timeout-Konfiguration

**Workaround:**
1. PostgreSQL-Service neu starten: `systemctl restart postgresql`
2. Applikation neu starten: `systemctl restart app-service`
3. Monitoring: Connection-Pool-Auslastung beobachten

**Permanente Lösung:**
1. max_connections in postgresql.conf erhöhen: `max_connections = 200`
2. Connection-Leak in Applikation beheben (Code-Fix)
3. Connection-Timeout konfigurieren: `idle_in_transaction_session_timeout = 60000`
4. Connection-Pool-Monitoring verbessern

**Betroffene CIs:**
- [[ netbox.database.server ]]
- [[ netbox.application.server ]]

**Verknüpfte Incidents:** INC-2024-123, INC-2024-145, INC-2024-167

**Status:** Resolved

**Priorität:** P2

### KEDB-Nutzung

**Incident-Bearbeitung:**
1. Incident-Symptome mit KEDB abgleichen
2. Bei Treffer: Workaround anwenden
3. Incident mit Known-Error verknüpfen
4. Problem-Ticket referenzieren

**Problem-Analyse:**
1. Neue Known Errors in KEDB eintragen
2. Workarounds dokumentieren
3. Permanente Lösungen tracken
4. Status aktualisieren

**Wissensmanagement:**
- KEDB als Wissensdatenbank nutzen
- Regelmäßige Reviews (monatlich)
- Veraltete Einträge archivieren
- Best Practices dokumentieren

## Proaktives Problem Management

### Trend-Analyse

**Datenquellen:**
- Incident-Statistiken
- Monitoring-Metriken
- Performance-Daten
- Kapazitäts-Auslastung

**Analyse-Methoden:**
- Zeitreihen-Analyse
- Korrelations-Analyse
- Anomalie-Erkennung
- Predictive Analytics

**Ziel:** Probleme identifizieren, bevor sie zu Incidents werden

### Proaktive Maßnahmen

**Regelmäßige Reviews:**
- Wöchentliche Incident-Trend-Reviews
- Monatliche Problem-Reviews
- Quartalsweise Service-Reviews

**Präventive Maßnahmen:**
- Kapazitäts-Upgrades
- Software-Updates und Patches
- Konfigurationsoptimierungen
- Prozess-Verbesserungen
- Training und Dokumentation

### Continuous Improvement

**Verbesserungs-Zyklus:**
1. **Measure:** Metriken erfassen
2. **Analyze:** Trends identifizieren
3. **Improve:** Maßnahmen umsetzen
4. **Control:** Wirksamkeit prüfen

**Verbesserungs-Bereiche:**
- Prozesse
- Tools
- Dokumentation
- Skills und Training
- Infrastruktur

## Metriken und Reporting

### Key Performance Indicators (KPIs)

| Metrik | Zielwert | Messung |
|---|---|---|
| **Problem Resolution Rate** | > 80% | Gelöste Problems / Gesamt-Problems |
| **Mean Time to Resolve Problem** | < 30 Tage | Durchschnittliche Lösungszeit |
| **Known Error Utilization** | > 60% | Incidents mit KEDB-Workaround |
| **Recurring Incident Rate** | < 10% | Incidents mit bekannter Ursache |
| **Postmortem Completion Rate** | 100% | Postmortems für Major Incidents |

### Reporting

**Monatliches Problem-Report:**
- Anzahl offener Problems (nach Priorität)
- Neu erstellte Problems
- Gelöste Problems
- Top-5 Problem-Kategorien
- KEDB-Statistiken
- Action Items Status

**Quartalsweise Trend-Analyse:**
- Problem-Trends über Zeit
- Wiederkehrende Problem-Muster
- Verbesserungs-Maßnahmen-Wirksamkeit
- ROI von Problem-Management

## Rollen und Verantwortlichkeiten

### Problem Manager

**Verantwortlichkeiten:**
- Problem-Prozess-Ownership
- Problem-Priorisierung
- RCA-Koordination
- KEDB-Verwaltung
- Postmortem-Moderation
- Reporting

**Person:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

### Technical Specialists

**Verantwortlichkeiten:**
- Technische Analyse
- RCA-Durchführung
- Lösungsentwicklung
- Workaround-Identifikation

**Teams:** Server-Team, Network-Team, DBA-Team, Application-Team

### Service Owner

**Verantwortlichkeiten:**
- Business-Impact-Bewertung
- Priorisierungs-Entscheidungen
- Ressourcen-Bereitstellung
- Stakeholder-Kommunikation

## Tools und Systeme

### Problem-Management-Tool
- **System:** {{ meta-handbook.ticketing_system }}
- **URL:** {{ meta-handbook.ticketing_system_url }}
- **Zugriff:** IT Operations Team

### Known Error Database
- **System:** {{ meta-handbook.ticketing_system }} (KEDB-Modul)
- **URL:** {{ meta-handbook.kedb_url }}
- **Zugriff:** Alle IT-Mitarbeiter (Read)

### RCA-Tools
- **Collaboration:** {{ meta-handbook.collaboration_tool }}
- **Diagramming:** {{ meta-handbook.diagramming_tool }}
- **Log-Analysis:** {{ meta-handbook.log_analysis_tool }}

## Referenzen

- ITIL v4 Foundation - Problem Management
- ISO/IEC 20000-1:2018 - Problem Management
- Site Reliability Engineering (SRE) - Postmortem Culture
- Interne Incident-Management-Prozesse
- Change-Management-Prozesse

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Klassifizierung:** {{ meta-handbook.classification }}  
**Letzte Aktualisierung:** {{ meta-handbook.date }}

