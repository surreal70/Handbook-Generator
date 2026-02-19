# Prozess: {{ process.name }}

**Dokument-ID:** {{ process.id }}  
**Organisation:** {{ meta-organisation.name }}  
**Prozess Owner:** {{ process.owner }}  
**Prozess Manager:** {{ process.manager }}  
**Genehmigt durch:** {{ process.approver }}  
**Revision:** {{ process.revision }}  
**Author:** {{ meta-global.source }}  
**Status:** {{ process.status }}  
**Klassifizierung:** {{ process.classification }}  
**Letzte Aktualisierung:** {{ process.modifydate }}  
**Template Version:** {{ meta-global.version }}

---

## 1. Zweck und Ziel

### 1.1 Zweck

Der Incident Management Prozess stellt sicher, dass IT-Services nach Störungen schnellstmöglich wiederhergestellt werden und die Auswirkungen auf den Geschäftsbetrieb minimiert werden.

### 1.2 Ziele

Die Hauptziele dieses Prozesses sind:

- **Schnelle Wiederherstellung:** Minimierung der Ausfallzeiten durch schnelle Incident-Bearbeitung
- **SLA-Einhaltung:** Einhaltung der definierten Service Level Agreements
- **Transparenz:** Vollständige Dokumentation aller Incidents für Audit und Analyse
- **Kontinuierliche Verbesserung:** Identifikation von Trends und Verbesserungspotentialen

## 2. Geltungsbereich

**Kategorie:** {{ process.category }}  
**Kritikalität:** {{ process.criticality }}

Dieser Prozess gilt für alle IT-Services der Organisation und umfasst:

- Alle ungeplanten Unterbrechungen oder Qualitätsminderungen von IT-Services
- Sicherheitsvorfälle, die die Verfügbarkeit von Services beeinträchtigen
- Hardware- und Software-Ausfälle
- Performance-Probleme, die die Servicequalität beeinträchtigen

**Ausgenommen sind:**
- Geplante Wartungsarbeiten (Change Management)
- Service Requests (Service Request Management)
- Sicherheitsvorfälle ohne Service-Auswirkung (Security Incident Management)

## 3. Trigger und Eingänge

### 3.1 Trigger

Incidents können durch folgende Ereignisse ausgelöst werden:

- **Monitoring-Alerts:** Automatische Erkennung durch Zabbix
- **Benutzer-Meldungen:** Anrufe, E-Mails, Self-Service Portal
- **Service Desk:** Proaktive Erkennung durch Service Desk
- **Andere Prozesse:** Eskalation aus Problem Management oder Change Management

### 3.2 Eingänge

- Incident-Beschreibung und Symptome
- Betroffene Services und Systeme
- Anzahl betroffener Benutzer
- Geschäftsauswirkungen

## 4. Ergebnisse und Outputs

### 4.1 Outputs

- **Wiederhergestellter Service:** Service ist wieder verfügbar
- **Incident-Dokumentation:** Vollständige Dokumentation in ServiceNow
- **Workaround:** Temporäre Lösung (falls vollständige Lösung nicht möglich)
- **Problem-Ticket:** Eskalation zu Problem Management (bei wiederkehrenden Incidents)

### 4.2 Erfolgskriterien

- Service innerhalb SLA wiederhergestellt
- Vollständige Dokumentation des Incidents
- Benutzer informiert über Status und Lösung
- Lessons Learned dokumentiert

## 5. Rollen und Verantwortlichkeiten (RACI)

### 5.1 RACI-Matrix

| Aktivität | System Admin | IT Manager | CISO | Service Desk | CIO |
|-----------|--------------|------------|------|--------------|-----|
| Incident Detection | R | A | C | - | I |
| Incident Logging | - | A | - | R | - |
| Incident Categorization | C | A | - | R | - |
| Incident Investigation | R | A | C | I | - |
| Incident Resolution | R | A | - | I | - |
| Incident Closure | - | A | - | R | - |

**Legende:**
- R = Responsible (Durchführung)
- A = Accountable (Verantwortlich)
- C = Consulted (Konsultiert)
- I = Informed (Informiert)

## 6. Ablaufdiagramm (BPMN)

### 6.1 Prozessschritte

1. **Incident Detection:** Automatische Erkennung durch Monitoring oder manuelle Meldung durch Benutzer
2. **Incident Logging:** Erfassung des Incidents in ServiceNow mit allen relevanten Informationen
3. **Incident Categorization:** Kategorisierung nach Service, Priorität und Impact
4. **Incident Investigation:** Analyse der Ursache und Identifikation der Lösung
5. **Incident Resolution:** Implementierung der Lösung und Wiederherstellung des Services
6. **Incident Closure:** Bestätigung der Lösung durch Benutzer und Abschluss des Tickets

### 6.2 Prozessfluss

```
Start
  ↓
Incident Detection (Monitoring/User)
  ↓
Incident Logging (ServiceNow)
  ↓
Incident Categorization (Priority/Impact)
  ↓
Incident Investigation
  ↓
  ├─→ Lösung gefunden? ─→ Ja ─→ Incident Resolution
  │                              ↓
  └─→ Nein ─→ Eskalation ───────┘
                                 ↓
                          Incident Closure
                                 ↓
                               Ende
```

## 7. Systeme und Tools

### 7.1 Verwendete Systeme

Die folgenden Systeme werden im Incident Management Prozess verwendet:

- **ServiceNow:** Incident-Ticketing und Workflow-Management
- **Zabbix:** Monitoring und automatische Incident-Erkennung
- **Slack:** Kommunikation und Eskalation
- **Microsoft Teams:** Video-Konferenzen für Major Incidents

### 7.2 Schnittstellen

#### Zu anderen Prozessen
- **Problem Management:** Eskalation bei wiederkehrenden Incidents
- **Change Management:** Koordination bei Incidents während Changes
- **Service Request Management:** Abgrenzung zwischen Incidents und Requests

#### Zu anderen Services
- **Monitoring Service:** Automatische Incident-Erkennung
- **E-Mail Service:** Benachrichtigungen an Benutzer
- **Knowledge Management:** Zugriff auf Known Errors und Workarounds

## 8. Artefakte

### 8.1 Tickets

**Incident-Ticket in ServiceNow:**
- Incident-Nummer (automatisch generiert)
- Beschreibung und Symptome
- Betroffener Service
- Priorität (P1-P4)
- Status (New, In Progress, Resolved, Closed)
- Assigned To (verantwortlicher Techniker)
- Resolution Notes

### 8.2 Logs

- **Incident-Log:** Chronologische Dokumentation aller Aktivitäten
- **Communication-Log:** Alle Kommunikationen mit Benutzern
- **Escalation-Log:** Dokumentation aller Eskalationen

### 8.3 Reports

- **Daily Incident Report:** Übersicht aller offenen Incidents
- **SLA Compliance Report:** Einhaltung der SLAs
- **Trend Analysis Report:** Identifikation von Mustern und Trends

## 9. SLAs und OLAs

### 9.1 Service Level Agreements

Die folgenden SLAs gelten für Incident-Bearbeitung:

| Priorität | Beschreibung | Reaktionszeit | Lösungszeit |
|-----------|--------------|---------------|-------------|
| P1 - Kritisch | Kompletter Service-Ausfall | 15 Minuten | {{ process.sla.p1_resolution }} |
| P2 - Hoch | Teilausfall, Workaround verfügbar | 1 Stunde | {{ process.sla.p2_resolution }} |
| P3 - Mittel | Eingeschränkte Funktionalität | 4 Stunden | {{ process.sla.p3_resolution }} |
| P4 - Niedrig | Minimale Auswirkungen | 1 Werktag | {{ process.sla.p4_resolution }} |

### 9.2 Operational Level Agreements

| Support-Team | Verantwortlichkeit | Reaktionszeit |
|--------------|-------------------|---------------|
| Netzwerk-Team | Netzwerk-Incidents | 30 Minuten (P1) |
| Security-Team | Sicherheits-Incidents | 15 Minuten (P1) |
| Application-Team | Applikations-Incidents | 1 Stunde (P2) |

## 10. KPIs und Metriken

### 10.1 Key Performance Indicators

Die folgenden KPIs werden zur Messung der Prozess-Performance verwendet:

| KPI | Zielwert | Messfrequenz |
|-----|----------|--------------|
| MTTR (Mean Time To Resolve) | < 4 Stunden | Monatlich |
| MTBF (Mean Time Between Failures) | > 720 Stunden | Monatlich |
| First Call Resolution Rate | > 70% | Monatlich |
| SLA Compliance Rate | > 95% | Monatlich |
| Incident Volume | Trend-Analyse | Monatlich |

### 10.2 Messung und Reporting

- **Automatische Messung:** KPIs werden automatisch aus ServiceNow extrahiert
- **Monatliche Reports:** An IT-Management und Service Owner
- **Quartalsweise Reviews:** Detaillierte Analyse und Verbesserungsmaßnahmen

## 11. Kontrollpunkte

### 11.1 Prüfschritte

Die folgenden Kontrollpunkte sind im Prozess implementiert:

- **Incident Logging:** Vollständigkeit der Incident-Informationen prüfen
- **Categorization:** Korrekte Priorität und Impact-Bewertung
- **Resolution:** Bestätigung der Lösung durch Benutzer
- **Closure:** Four-Eyes-Principle für P1-Incidents

### 11.2 Audit-Anforderungen

- Vollständige Dokumentation aller Incidents in ServiceNow
- Nachvollziehbare Eskalationswege und Genehmigungen
- Zeitstempel für alle Prozessschritte
- Regelmäßige Reviews und Lessons Learned

## 12. Risiken und Compliance

### 12.1 Compliance-Frameworks

Dieser Prozess erfüllt Anforderungen folgender Frameworks:

- ISO 27001:2022 - Clause 5.24 (Information security incident management)
- ISO 27001:2022 - Clause 5.25 (Assessment and decision on information security events)
- BSI IT-Grundschutz - DER.2.1 (Incident Management)
- ITIL 4 - Incident Management Practice

### 12.2 Segregation of Duties (SoD)

Die folgenden SoD-Regeln sind implementiert:

- Incident handler cannot approve own escalations
- Security analyst cannot modify audit logs
- Service desk agent cannot close P1 incidents without approval

### 12.3 Risiken

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|--------|-------------------|------------|------------|
| SLA-Verletzung | Mittel | Hoch | Automatische Eskalation, 24/7 Support |
| Unvollständige Dokumentation | Niedrig | Mittel | Pflichtfelder in ServiceNow, Audits |
| Fehlende Eskalation | Niedrig | Hoch | Automatische Eskalations-Regeln |
| Kommunikationsfehler | Mittel | Mittel | Standardisierte Templates, Status-Updates |

## 13. Eskalationen und Ausnahmen

### 13.1 Eskalationspfad

| Level | Rolle | Kontakt | Eskalationskriterien |
|-------|-------|---------|---------------------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} | Erste Anlaufstelle |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} | Nach 30 Min ohne Lösung (P1) |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} | Nach 1 Std ohne Lösung (P1) |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} | Geschäftskritische Eskalation |

### 13.2 Ausnahmen

Ausnahmen vom Standard-Prozess sind nur in folgenden Fällen erlaubt:

- **Major Incidents:** Aktivierung des Major Incident Prozesses
- **Sicherheitsvorfälle:** Aktivierung des Security Incident Response Prozesses
- **Notfälle:** Mit Genehmigung des IT-Managers

## 14. Anhänge

### 14.1 Checklisten

- **P1 Incident Checklist:** Schritt-für-Schritt-Anleitung für kritische Incidents
- **Major Incident Checklist:** Aktivierung und Koordination von Major Incidents
- **Post-Incident Review Checklist:** Lessons Learned nach Major Incidents

### 14.2 Runbooks

- **Common Incidents Runbook:** Lösungen für häufige Incidents
- **Escalation Runbook:** Eskalationsprozeduren und Kontakte
- **Communication Runbook:** Templates für Benutzer-Kommunikation

### 14.3 Formulare

- **Incident Report Form:** Standardisiertes Formular für Incident-Meldungen
- **Post-Incident Review Form:** Template für Lessons Learned
- **Major Incident Declaration Form:** Aktivierung des Major Incident Prozesses

---

## 15. Kontaktinformationen

### 15.1 Organisation

- **Name:** {{ meta-organisation.name }}
- **Adresse:** {{ meta-organisation.address }}
- **Telefon:** {{ meta-organisation.phone }}
- **Web:** {{ meta-organisation.web }}

### 15.2 Prozess-Kontakte

- **Prozess Owner:** {{ role_IT_Manager }} ({{ role_IT_Manager_email }})
- **Prozess Manager:** {{ role_IT_Manager }} ({{ role_IT_Manager_email }})
- **Service Desk:** {{ escalation.level_1 }} ({{ escalation.level_1_email }})

---

## Dokumentenhistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | 15.01.2026 | Handbook Generator | Initiale Version |
| 2.0 | 19.02.2026 | Handbook Generator | Aktualisierung: RACI-Matrix erweitert, SoD-Regeln hinzugefügt |

---
