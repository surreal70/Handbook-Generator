# Anhang: Nachweisregister (Evidence)

**Dokument-ID:** 0700  
**Dokumenttyp:** Anhang/Template  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2/200-3)  
**Owner:** IT Operations Manager  
**Version:** 1.0.0  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---



## 1. Zweck und Zielsetzung

Das Nachweisregister von **AdminSend GmbH** bietet eine zentrale Übersicht über alle Nachweise (Evidence), die die Umsetzung von Sicherheitsmaßnahmen, Policies und Richtlinien belegen.

**Verantwortlich:** Thomas Weber (ISB)

## 2. Nachweisregister

| Evidence-ID | Thema/Maßnahme | Beschreibung | Dokumenttyp | Ort/Link | Owner | Aufbewahrungsfrist | Letzte Prüfung | Nächste Prüfung | Status |
|---|---|---|---|---|---|---|---|---|---|
| E-001 | Patch-Compliance | Monatlicher Patch-Status-Report | Report | [TODO: SharePoint/CMDB] | Anna Schmidt | 3 Jahre | [TODO] | [TODO] | Aktuell |
| E-002 | Backup-Tests | Quartalsweise Restore-Tests | Testprotokoll | [TODO] | Anna Schmidt | 3 Jahre | [TODO] | [TODO] | Aktuell |
| E-003 | Schulungsnachweise | Teilnehmerlisten Security Awareness | Teilnehmerliste | [TODO: LMS] | Thomas Weber | 5 Jahre | [TODO] | [TODO] | Aktuell |
| E-004 | Audit-Berichte | Interne Audit-Berichte | Audit-Bericht | [TODO] | Internal Audit | 10 Jahre | [TODO] | [TODO] | Aktuell |
| E-005 | Risikoakzeptanzen | Dokumentierte Risikoakzeptanzen | Freigabe-Dokument | [TODO] | Max Mustermann | 5 Jahre | [TODO] | [TODO] | Aktuell |
| E-006 | Vulnerability Scans | Monatliche Vulnerability Scan Reports | Scan-Report | [TODO: Vulnerability Management Tool] | Thomas Weber | 2 Jahre | [TODO] | [TODO] | Aktuell |
| E-007 | Penetrationstests | Jährliche Pentest-Berichte | Pentest-Bericht | [TODO] | Thomas Weber | 5 Jahre | [TODO] | [TODO] | Aktuell |
| E-008 | Incident-Dokumentation | Incident-Reports und Postmortems | Incident-Report | [TODO: ITSM] | Anna Schmidt | 3 Jahre | [TODO] | [TODO] | Aktuell |
| E-009 | Change-Approvals | Change-Freigaben mit Security-Review | Change-Record | [TODO: ITSM] | Anna Schmidt | 2 Jahre | [TODO] | [TODO] | Aktuell |
| E-010 | Zugriffsprotokolle | Privileged Access Logs | Log-Archiv | [TODO: SIEM] | Thomas Weber | 1 Jahr | [TODO] | [TODO] | Aktuell |
| E-011 | Lieferanten-Assessments | Third-Party Risk Assessments | Assessment-Report | [TODO] | Thomas Weber | 3 Jahre | [TODO] | [TODO] | Aktuell |
| E-012 | Managementbewertung | Jährliche Management Review Protokolle | Protokoll | [TODO] | Max Mustermann | 10 Jahre | [TODO] | [TODO] | Aktuell |
| E-013 | Basis-Sicherheitscheck | BSI Basis-Check Ergebnisse | Gap-Analyse | [TODO] | Thomas Weber | 3 Jahre | [TODO] | [TODO] | Aktuell |
| E-014 | Schutzbedarfsfeststellung | Dokumentierte Schutzbedarfe | Bewertung | [TODO] | Thomas Weber | 5 Jahre | [TODO] | [TODO] | Aktuell |
| E-015 | Notfallübungen | BCM/DR Test-Protokolle | Testprotokoll | [TODO] | Thomas Weber | 3 Jahre | [TODO] | [TODO] | Aktuell |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 3. Kategorien von Nachweisen

### 3.1 Technische Nachweise
- Scan-Reports (Vulnerability, Compliance)
- Log-Daten und SIEM-Auswertungen
- Backup-Protokolle
- Patch-Status-Reports
- Konfigurationsdokumentation

### 3.2 Organisatorische Nachweise
- Policies und Richtlinien (freigegeben)
- Schulungsnachweise
- Audit-Berichte
- Management Review Protokolle
- Risikoakzeptanzen

### 3.3 Prozess-Nachweise
- Incident-Reports
- Change-Records
- Problem-Management-Dokumentation
- Testprotokolle (DR, Backup, etc.)

### 3.4 Compliance-Nachweise
- Zertifikate (ISO, BSI, etc.)
- Externe Audit-Berichte
- Penetrationstests
- Datenschutz-Folgenabschätzungen (DPIA)

## 4. Aufbewahrungsfristen

| Dokumenttyp | Aufbewahrungsfrist | Rechtsgrundlage |
|---|---|---|
| Audit-Berichte | 10 Jahre | Handelsrecht |
| Schulungsnachweise | 5 Jahre | Nachweispflicht |
| Incident-Reports | 3 Jahre | Best Practice |
| Log-Daten | 1 Jahr (Standard), 3 Jahre (kritische Systeme) | DSGVO, BSI |
| Risikoakzeptanzen | 5 Jahre | Nachweispflicht |
| Verträge (Lieferanten) | Vertragslaufzeit + 3 Jahre | Handelsrecht |

## 5. Zugriffskontrolle

**Zugriff auf Nachweise:**
- **ISB:** Vollzugriff
- **Internal Audit:** Vollzugriff (Lesezugriff)
- **Geschäftsführung:** Vollzugriff
- **Bereichsverantwortliche:** Zugriff auf eigene Nachweise
- **Externe Auditoren:** Temporärer Lesezugriff (nach Freigabe)

**Ablageorte:**
- Zentrale Dokumentenablage: [TODO: z.B. SharePoint, Confluence]
- ITSM-System: [TODO: z.B. ServiceNow, Jira]
- SIEM/Log-Management: [TODO]
- CMDB: [TODO]

## 6. Prüfung und Aktualisierung

**Regelmäßige Prüfung:**
- **Quartalsweise:** Vollständigkeitsprüfung
- **Jährlich:** Aufbewahrungsfristen-Review
- **Bei Audits:** Verfügbarkeit und Aktualität prüfen

**Verantwortlich:** Thomas Weber

## 7. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | Thomas Weber | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT-Leitung | Anna Schmidt | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**Referenzen:**
- BSI Standard 200-1: ISMS (Dokumentation)
- BSI Standard 200-2: IT-Grundschutz-Methodik (Nachweisführung)
- Alle ISMS-Dokumente (0010-0630)


