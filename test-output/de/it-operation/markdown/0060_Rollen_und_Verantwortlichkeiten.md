# Rollen und Verantwortlichkeiten

**Dokument-ID:** [FRAMEWORK]-0060
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

## Organisationsstruktur

### Unternehmensinformationen

- **Organisation:** AdminSend GmbH
- **Adresse:** Musterstraße 123, {{ meta-organisation.postal_code }} {{ meta-organisation.city }}
- **Land:** {{ meta-organisation.country }}
- **Website:** {{ meta-organisation.website }}
- **Telefon:** +49 89 12345678
- **E-Mail:** {{ meta-organisation.email }}

### Organisationsübersicht

[TODO: Fügen Sie hier ein Organigramm oder eine Beschreibung der Organisationsstruktur ein]

## Führungsebene

### Chief Executive Officer (CEO)

- **Name:** [TODO]
- **E-Mail:** {{ meta-organisation-roles.role_CEO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CEO_phone }}

**Verantwortlichkeiten:**
- Gesamtverantwortung für das Unternehmen
- Strategische Ausrichtung und Unternehmensziele
- Genehmigung kritischer IT-Investitionen
- Eskalationspunkt für geschäftskritische IT-Vorfälle

### Chief Information Officer (CIO)

- **Name:** [TODO]
- **E-Mail:** {{ meta-organisation-roles.role_CIO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CIO_phone }}

**Verantwortlichkeiten:**
- Gesamtverantwortung für IT-Strategie und -Betrieb
- IT-Budget und Ressourcenplanung
- IT-Governance und Compliance
- Genehmigung von Major Changes
- Verantwortung für IT-Service-Qualität und SLA-Einhaltung

### Chief Information Security Officer (CISO)

- **Name:** [TODO]
- **E-Mail:** {{ meta-organisation-roles.role_CISO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CISO_phone }}

**Verantwortlichkeiten:**
- IT-Sicherheitsstrategie und -Richtlinien
- Informationssicherheits-Management (ISMS)
- Security Incident Response
- Compliance mit Sicherheitsstandards (ISO 27001, BSI Grundschutz)
- Risikomanagement und Vulnerability Management
- Security Awareness und Training

### Chief Financial Officer (CFO)

- **Name:** [TODO]
- **E-Mail:** {{ meta-organisation-roles.role_CFO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CFO_phone }}

**Verantwortlichkeiten:**
- Finanzielle Genehmigung von IT-Projekten
- IT-Budget-Überwachung
- Kosten-Nutzen-Analysen für IT-Investitionen
- Finanzielle Compliance und Audits

### Chief Operating Officer (COO)

- **Name:** {{ meta-organisation-roles.role_COO }}
- **E-Mail:** {{ meta-organisation-roles.role_COO_email }}
- **Telefon:** {{ meta-organisation-roles.role_COO_phone }}

**Verantwortlichkeiten:**
- Operative Geschäftsprozesse
- Business Continuity Management
- Koordination zwischen IT und Geschäftsbereichen
- Service-Level-Anforderungen aus Geschäftssicht

## IT-Betriebsebene

### IT Operations Manager

- **Name:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
- **E-Mail:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Telefon:** {{ meta-organisation-roles.role_IT_Operations_Manager_phone }}

**Verantwortlichkeiten:**
- Täglicher IT-Betrieb und Service Delivery
- Monitoring und Incident Management
- Change Management Koordination
- Kapazitäts- und Performance-Management
- Team-Führung IT Operations
- Eskalationsmanagement für operative Vorfälle
- Sicherstellung der SLA-Einhaltung

**Vertretung:** [TODO: Name und Kontakt der Vertretung]

### Service Desk Lead

- **Name:** {{ meta-organisation-roles.role_Service_Desk_Lead }}
- **E-Mail:** {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **Telefon:** {{ meta-organisation-roles.role_Service_Desk_Lead_phone }}

**Verantwortlichkeiten:**
- First-Level-Support und Incident Management
- Ticket-Management und Priorisierung
- Nutzer-Kommunikation
- Service-Katalog-Pflege
- Team-Führung Service Desk
- Service-Desk-Metriken und Reporting

**Vertretung:** [TODO: Name und Kontakt der Vertretung]

## Weitere IT-Rollen

### System Administrator

- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Server- und Systemadministration
- Patch- und Update-Management
- Backup und Restore
- System-Monitoring
- Dokumentation der Systemkonfigurationen

### Network Administrator

- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Netzwerkinfrastruktur-Management
- Firewall- und Security-Konfiguration
- Netzwerk-Monitoring
- VPN- und Remote-Access-Management
- Netzwerk-Dokumentation

### Database Administrator (DBA)

- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Datenbank-Administration und -Optimierung
- Datenbank-Backup und Recovery
- Performance-Tuning
- Datenbank-Security
- Datenbank-Monitoring

### Application Manager

- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Applikations-Support und -Wartung
- Release-Management für Applikationen
- Applikations-Monitoring
- Koordination mit Entwicklungsteams
- Applikations-Dokumentation

### Security Administrator

- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Security-Monitoring und Incident Response
- Vulnerability-Scanning und -Management
- Security-Patch-Management
- Access-Management und Berechtigungen
- Security-Audits und Compliance-Checks

## RACI-Matrix für IT-Betriebsaktivitäten

Die RACI-Matrix definiert Verantwortlichkeiten für IT-Betriebsaktivitäten:
- **R** = Responsible (Durchführungsverantwortung)
- **A** = Accountable (Gesamtverantwortung, Entscheidungsbefugnis)
- **C** = Consulted (Konsultiert, muss befragt werden)
- **I** = Informed (Informiert, muss informiert werden)

### Service Management

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Service-Strategie** | A | R | C | C | C | C | I | I | I | I | I | I |
| **Service-Design** | I | A | C | I | C | R | C | C | C | C | C | C |
| **Service-Transition** | I | A | C | I | C | R | C | R | R | R | R | C |
| **Service-Operation** | I | A | C | I | I | R | R | R | R | R | R | R |
| **Continual Improvement** | I | A | C | I | C | R | C | C | C | C | C | C |

### Incident Management

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Incident-Erfassung** | I | I | I | I | I | C | R | C | C | C | C | C |
| **Incident-Klassifizierung** | I | I | C | I | I | C | R | C | C | C | C | C |
| **Incident-Diagnose** | I | I | C | I | I | C | R | R | R | R | R | R |
| **Incident-Lösung** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Incident-Abschluss** | I | I | I | I | I | A | R | C | C | C | C | C |
| **Major Incident** | I | A | C | I | C | R | R | R | R | R | R | R |

### Problem Management

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Problem-Identifikation** | I | I | C | I | I | A | R | R | R | R | R | R |
| **Problem-Analyse** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Root-Cause-Analysis** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Workaround-Entwicklung** | I | I | C | I | I | A | C | R | R | R | R | R |
| **Known-Error-Dokumentation** | I | I | I | I | I | A | R | C | C | C | C | C |
| **Problem-Lösung** | I | A | C | I | I | R | C | R | R | R | R | R |

### Change Management

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Change-Request** | I | I | C | I | I | C | C | R | R | R | R | R |
| **Change-Bewertung** | I | C | C | I | C | A | I | R | R | R | R | R |
| **Change-Genehmigung (Standard)** | I | I | I | I | I | A | I | I | I | I | I | I |
| **Change-Genehmigung (Normal)** | I | A | C | I | C | R | I | I | I | I | I | I |
| **Change-Genehmigung (Emergency)** | I | A | C | I | C | R | I | I | I | I | I | I |
| **Change-Implementierung** | I | I | C | I | I | A | I | R | R | R | R | R |
| **Change-Review** | I | A | C | I | I | R | C | C | C | C | C | C |

### Security Management

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Security-Strategie** | A | C | R | C | C | C | I | I | I | I | I | I |
| **Security-Richtlinien** | A | C | R | I | C | C | I | C | C | C | C | C |
| **Security-Monitoring** | I | I | A | I | I | C | I | C | C | C | C | R |
| **Security-Incident** | I | A | R | I | C | C | C | C | C | C | C | R |
| **Vulnerability-Management** | I | I | A | I | I | C | I | C | C | C | C | R |
| **Access-Management** | I | I | A | I | I | C | C | R | R | R | R | R |
| **Security-Audits** | I | A | R | C | C | C | I | C | C | C | C | R |

### Backup und Recovery

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Backup-Strategie** | I | A | C | I | C | R | I | C | C | C | C | C |
| **Backup-Durchführung** | I | I | I | I | I | A | I | R | C | R | C | I |
| **Backup-Monitoring** | I | I | I | I | I | A | I | R | C | R | C | I |
| **Backup-Tests** | I | I | C | I | I | A | I | R | C | R | C | C |
| **Restore-Durchführung** | I | I | C | I | I | A | C | R | C | R | C | C |
| **Disaster-Recovery** | I | A | C | I | C | R | C | R | R | R | R | C |

### Monitoring und Performance

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Monitoring-Strategie** | I | A | C | I | C | R | I | C | C | C | C | C |
| **Monitoring-Konfiguration** | I | I | C | I | I | A | I | R | R | R | R | R |
| **24/7-Monitoring** | I | I | C | I | I | A | R | R | R | R | R | R |
| **Alert-Management** | I | I | C | I | I | A | R | R | R | R | R | R |
| **Performance-Tuning** | I | I | I | I | I | A | I | R | R | R | R | I |
| **Kapazitätsplanung** | I | A | I | C | C | R | I | C | C | C | C | I |

### Compliance und Audits

| Aktivität | CEO | CIO | CISO | CFO | COO | Ops Manager | Service Desk | Sys Admin | Net Admin | DBA | App Manager | Sec Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Compliance-Strategie** | A | R | C | C | C | C | I | I | I | I | I | I |
| **Compliance-Kontrollen** | I | A | R | C | C | C | I | C | C | C | C | C |
| **Audit-Vorbereitung** | I | A | R | C | C | R | C | C | C | C | C | C |
| **Audit-Durchführung** | C | A | R | C | C | R | C | C | C | C | C | C |
| **Audit-Nachbereitung** | I | A | R | I | C | R | I | C | C | C | C | C |

## Kontaktlisten und Erreichbarkeiten

### Führungsebene - Kontakte

| Rolle | Name | E-Mail | Telefon | Mobil | Verfügbarkeit |
|---|---|---|---|---|---|
| **CEO** | [TODO] | {{ meta-organisation-roles.role_CEO_email }} | {{ meta-organisation-roles.role_CEO_phone }} | [TODO] | Mo-Fr 09:00-17:00 |
| **CIO** | [TODO] | {{ meta-organisation-roles.role_CIO_email }} | {{ meta-organisation-roles.role_CIO_phone }} | [TODO] | Mo-Fr 08:00-18:00 |
| **CISO** | [TODO] | {{ meta-organisation-roles.role_CISO_email }} | {{ meta-organisation-roles.role_CISO_phone }} | [TODO] | Mo-Fr 08:00-18:00 |
| **CFO** | [TODO] | {{ meta-organisation-roles.role_CFO_email }} | {{ meta-organisation-roles.role_CFO_phone }} | [TODO] | Mo-Fr 09:00-17:00 |
| **COO** | {{ meta-organisation-roles.role_COO }} | {{ meta-organisation-roles.role_COO_email }} | {{ meta-organisation-roles.role_COO_phone }} | [TODO] | Mo-Fr 08:00-18:00 |

### IT-Operations - Kontakte

| Rolle | Name | E-Mail | Telefon | Mobil | Verfügbarkeit |
|---|---|---|---|---|---|
| **IT Ops Manager** | {{ meta-organisation-roles.role_IT_Operations_Manager }} | {{ meta-organisation-roles.role_IT_Operations_Manager_email }} | {{ meta-organisation-roles.role_IT_Operations_Manager_phone }} | [TODO] | Mo-Fr 07:00-19:00 |
| **Service Desk Lead** | {{ meta-organisation-roles.role_Service_Desk_Lead }} | {{ meta-organisation-roles.role_Service_Desk_Lead_email }} | {{ meta-organisation-roles.role_Service_Desk_Lead_phone }} | [TODO] | Mo-Fr 08:00-17:00 |
| **System Admin** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Network Admin** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **DBA** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **App Manager** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Security Admin** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### Service Desk - Kontakte

**Zentrale Service-Desk-Nummer:** [TODO: Telefonnummer]  
**Service-Desk-E-Mail:** [TODO: E-Mail-Adresse]  
**Service-Portal:** [TODO: URL]

**Servicezeiten:**
- **Regulär:** Mo-Fr 08:00-17:00 Uhr
- **Erweitert:** [TODO: Falls zutreffend]
- **24/7:** [TODO: Falls zutreffend]

## On-Call und Rufbereitschaft

### Rufbereitschafts-Modell

**Betriebsmodell:** [TODO: 24/7, Business Hours, Follow-the-Sun]

**Rufbereitschaftszeiten:**
- **Werktags:** [TODO: z.B. 17:00-08:00 Uhr]
- **Wochenende:** [TODO: z.B. Fr 17:00 - Mo 08:00 Uhr]
- **Feiertage:** [TODO: 24 Stunden]

### Rufbereitschafts-Rotation

| Woche | Primär | Sekundär | Eskalation |
|---|---|---|---|
| **KW [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **KW [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **KW [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **KW [TODO]** | [TODO: Name] | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |

**Rotationsplan:** [TODO: Link zum aktuellen Rufbereitschaftsplan]

### On-Call-Kontakte

**Primäre Rufbereitschaft:**
- **Telefon:** [TODO: On-Call-Nummer]
- **E-Mail:** [TODO: On-Call-E-Mail]
- **Erreichbarkeit:** [TODO: Reaktionszeit]

**Sekundäre Rufbereitschaft:**
- **Telefon:** [TODO: Backup-Nummer]
- **E-Mail:** [TODO: Backup-E-Mail]
- **Erreichbarkeit:** [TODO: Reaktionszeit]

**Eskalation:**
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_phone }})
- **CIO:** [TODO] ({{ meta-organisation-roles.role_CIO_phone }})

### Rufbereitschafts-Prozess

**1. Alarmierung:**
- Monitoring-System sendet Alert
- Automatische Benachrichtigung an On-Call-Person
- Kanäle: SMS, Telefon, E-Mail, Push-Notification

**2. Reaktion:**
- **Reaktionszeit:** [TODO: z.B. 15 Minuten]
- **Bestätigung:** On-Call-Person bestätigt Empfang
- **Erste Analyse:** Innerhalb [TODO: z.B. 30 Minuten]

**3. Eskalation:**
- **Level 1:** Primäre Rufbereitschaft (0-15 Min)
- **Level 2:** Sekundäre Rufbereitschaft (15-30 Min)
- **Level 3:** IT Operations Manager (30-60 Min)
- **Level 4:** CIO (> 60 Min oder kritischer Vorfall)

**4. Dokumentation:**
- Alle Aktivitäten im Ticket-System dokumentieren
- Zeitstempel für alle Aktionen
- Post-Incident-Review bei Major Incidents

### Rufbereitschafts-Richtlinien

**Verfügbarkeit:**
- On-Call-Person muss erreichbar sein
- Reaktionszeit: [TODO: z.B. 15 Minuten]
- Zugriff auf Laptop und VPN erforderlich
- Nüchternheit während Rufbereitschaft

**Kompensation:**
- Rufbereitschaftspauschale: [TODO: Betrag]
- Einsatzvergütung: [TODO: Stundensatz]
- Freizeitausgleich: [TODO: Regelung]

**Übergabe:**
- Übergabe-Call am Ende der Rufbereitschaft
- Dokumentation offener Vorfälle
- Briefing der nächsten On-Call-Person

## Eskalationspfade

### Standard-Eskalation

```
Level 1: Service Desk
    ↓ (15 Min)
Level 2: Fachspezialist (Sys/Net/DB/App Admin)
    ↓ (30 Min)
Level 3: IT Operations Manager
    ↓ (60 Min)
Level 4: CIO
    ↓ (kritisch)
Level 5: CEO
```

### Security-Incident-Eskalation

```
Security Alert
    ↓ (sofort)
Security Administrator
    ↓ (15 Min)
CISO
    ↓ (30 Min bei Major Incident)
CIO + CEO
    ↓ (bei Datenschutzvorfall)
Datenschutzbeauftragter + Behörden
```

### Business-Critical-Incident-Eskalation

```
Major Incident
    ↓ (sofort)
IT Operations Manager + On-Call
    ↓ (15 Min)
CIO + CISO
    ↓ (30 Min)
COO + CEO
    ↓ (bei Bedarf)
Externe Dienstleister + Hersteller
```

### Eskalationskriterien

**Automatische Eskalation bei:**
- Keine Reaktion innerhalb der definierten Zeit
- Incident kann nicht gelöst werden
- Mehrere kritische Systeme betroffen
- Datenschutz- oder Security-Vorfall
- Geschäftskritische Services ausgefallen

**Eskalationszeiten:**
- **P1 (Kritisch):** 15 Min → 30 Min → 60 Min
- **P2 (Hoch):** 30 Min → 60 Min → 2 Std
- **P3 (Mittel):** 2 Std → 4 Std → 8 Std
- **P4 (Niedrig):** 8 Std → 1 Tag → 2 Tage

## Vertretungsregelungen

### Führungsebene - Vertretungen

| Rolle | Primär | Vertretung 1 | Vertretung 2 |
|---|---|---|---|
| **CEO** | [TODO] | [TODO: Name] | [TODO: Name] |
| **CIO** | [TODO] | {{ meta-organisation-roles.role_IT_Operations_Manager }} | [TODO: Name] |
| **CISO** | [TODO] | [TODO: Name] | [TODO] |
| **CFO** | [TODO] | [TODO: Name] | [TODO: Name] |
| **COO** | {{ meta-organisation-roles.role_COO }} | [TODO: Name] | [TODO: Name] |

### IT-Operations - Vertretungen

| Rolle | Primär | Vertretung 1 | Vertretung 2 |
|---|---|---|---|
| **IT Ops Manager** | {{ meta-organisation-roles.role_IT_Operations_Manager }} | [TODO: Name] | [TODO] |
| **Service Desk Lead** | {{ meta-organisation-roles.role_Service_Desk_Lead }} | [TODO: Name] | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| **System Admin** | [TODO: Name] | [TODO: Name] | [TODO: Name] |
| **Network Admin** | [TODO: Name] | [TODO: Name] | [TODO: Name] |
| **DBA** | [TODO: Name] | [TODO: Name] | [TODO: Name] |

### Vertretungsprozess

**Bei geplanter Abwesenheit:**
1. Vertretung mindestens [TODO: z.B. 1 Woche] im Voraus informieren
2. Übergabe-Dokumentation erstellen
3. Offene Themen und Vorfälle übergeben
4. Kontaktinformationen aktualisieren
5. Out-of-Office-Nachricht mit Vertretungskontakt

**Bei ungeplanter Abwesenheit:**
1. Vorgesetzten informieren
2. Automatische Vertretungsregelung greift
3. Vertretung übernimmt alle laufenden Aufgaben
4. Nachträgliche Übergabe bei Rückkehr

## Schulung und Qualifikation

### Erforderliche Qualifikationen

| Rolle | Erforderliche Zertifizierungen | Empfohlene Schulungen |
|---|---|---|
| **IT Ops Manager** | ITIL Foundation, ITIL Managing Professional | COBIT, ISO 20000 |
| **Service Desk Lead** | ITIL Foundation | ITIL Specialist, HDI Support Center Manager |
| **System Admin** | [TODO: z.B. MCSA, RHCSA] | [TODO: Hersteller-Zertifizierungen] |
| **Network Admin** | [TODO: z.B. CCNA, CCNP] | [TODO: Netzwerk-Sicherheit] |
| **DBA** | [TODO: z.B. Oracle DBA, MCDBA] | [TODO: Performance-Tuning] |
| **Security Admin** | [TODO: z.B. CISSP, CEH] | [TODO: Security-Frameworks] |

### Schulungsplan

**Jährliche Pflichtschulungen:**
- IT-Sicherheit und Datenschutz (alle Mitarbeiter)
- ITIL-Refresher (IT Operations Team)
- Incident-Management-Prozesse (Service Desk)
- Change-Management-Prozesse (alle IT-Mitarbeiter)

**Individuelle Weiterbildung:**
- Budget: [TODO: Betrag pro Mitarbeiter/Jahr]
- Genehmigung: IT Operations Manager / CIO
- Dokumentation: Schulungsnachweise im Personalordner

## Änderungshistorie

| Version | Datum | Autor | Änderungen | Genehmigt durch |
|---|---|---|---|---|
| 1.0.0 | [TODO] | [TODO] | Initiale Version | [TODO] |

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Klassifizierung:** Internal  
**Organisation:** AdminSend GmbH

