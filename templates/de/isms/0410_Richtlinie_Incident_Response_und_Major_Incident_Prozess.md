# Richtlinie: Incident Response und Major Incident Prozess

**Dokument-ID:** 0410
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0400_Policy_Incident_Management.md` und definiert:
- Incident-Response-Prozesse und -Workflows
- Major-Incident-Management
- Security-Incident-Response und Forensik

**Geltungsbereich:** Alle Incidents bei **{{ meta-organisation.name }}**

## 2. Incident-Kategorien

### 2.1 Severity-Level

| Severity | Definition | Beispiele | Response-Zeit |
|----------|------------|-----------|---------------|
| P1 (Critical) | Kritischer Service-Ausfall | Produktionsausfall, Datenverlust, aktiver Cyberangriff | 15 Minuten |
| P2 (High) | Schwere Beeinträchtigung | Performance-Probleme, Teilausfall | 1 Stunde |
| P3 (Medium) | Moderate Beeinträchtigung | Einzelne Nutzer betroffen | 4 Stunden |
| P4 (Low) | Geringe Beeinträchtigung | Kosmetische Fehler | 1 Arbeitstag |

### 2.2 Security Incidents

**Kategorien:**
- Malware-Infektionen
- Phishing-Angriffe
- Unauthorized Access
- Data Breaches
- DDoS-Angriffe
- Insider Threats

**Alle Security Incidents mindestens P2**

## 3. Incident-Response-Prozess

### 3.1 Detection & Reporting

**Meldewege:**
- **IT-Support:** {{ meta.support.phone }}, {{ meta.support.email }}
- **Security-Team:** {{ meta.security.email }}, {{ meta.security.phone }}
- **Self-Service-Portal:** {{ meta.itsm.portal }}

**Pflichtangaben:**
- Beschreibung des Problems
- Betroffene Systeme/Nutzer
- Zeitpunkt des Auftretens
- Auswirkungen

### 3.2 Triage & Classification

**Prozess:**
1. Incident-Ticket erstellen
2. Severity-Level bestimmen
3. Kategorie zuordnen
4. Zuständiges Team zuweisen
5. Erste Response innerhalb SLA

**Eskalation:**
- P1: Sofortige Eskalation an On-Call
- P2: Eskalation nach 1 Stunde ohne Fortschritt
- Security Incidents: Parallel an Security-Team

### 3.3 Investigation & Diagnosis

**Schritte:**
1. Symptome analysieren
2. Logs prüfen
3. Betroffene Systeme identifizieren
4. Root Cause ermitteln
5. Workaround identifizieren (falls möglich)

**Dokumentation:**
- Alle Schritte im Ticket dokumentieren
- Logs und Screenshots anhängen
- Zeitstempel für alle Aktionen

### 3.4 Resolution & Recovery

**Prozess:**
1. Fix implementieren oder Workaround anwenden
2. Funktionstest durchführen
3. Nutzer informieren
4. Monitoring auf Wiederauftreten

**Verifizierung:**
- Nutzer bestätigt Lösung
- Monitoring zeigt normale Werte
- Keine weiteren Meldungen

### 3.5 Closure & Post-Incident Review

**Closure:**
- Ticket schließen nach Nutzer-Bestätigung
- Dokumentation vervollständigen
- Kategorisierung prüfen

**Post-Incident Review (PIR):**
- Bei P1/P2 Incidents verpflichtend
- Innerhalb 7 Tage nach Closure
- Lessons Learned dokumentieren
- Verbesserungsmaßnahmen definieren

## 4. Major Incident Management

### 4.1 Major Incident Kriterien

**Ein Incident ist "Major" wenn:**
- Severity P1
- Mehrere kritische Services betroffen
- Viele Nutzer betroffen (> 100)
- Medienaufmerksamkeit möglich
- Regulatorische Meldepflicht

### 4.2 Major Incident Team

**Rollen:**
- **Incident Manager:** Koordination, Kommunikation
- **Technical Lead:** Technische Lösung
- **Communications Lead:** Stakeholder-Kommunikation
- **Security Lead:** Bei Security Incidents
- **Management Representative:** Entscheidungen

**Verfügbarkeit:** 24/7 On-Call-Rotation

### 4.3 Major Incident Prozess

**Phase 1: Mobilisierung (0-15 Minuten)**
1. Major Incident deklarieren
2. Major Incident Team alarmieren
3. War Room einrichten (physisch oder virtuell)
4. Incident-Bridge aufbauen (Telefonkonferenz)

**Phase 2: Containment (15-60 Minuten)**
1. Auswirkungen begrenzen
2. Workaround implementieren (falls möglich)
3. Stakeholder informieren
4. Monitoring intensivieren

**Phase 3: Resolution (variabel)**
1. Root Cause identifizieren
2. Permanente Lösung implementieren
3. Schrittweise Wiederherstellung
4. Verifizierung

**Phase 4: Recovery (variabel)**
1. Alle Services wiederhergestellt
2. Monitoring auf Normalzustand
3. Nutzer informieren
4. Major Incident beenden

**Phase 5: Post-Incident Review (innerhalb 48 Stunden)**
1. Timeline rekonstruieren
2. Root Cause Analysis
3. Lessons Learned
4. Action Items definieren
5. Management-Bericht

### 4.4 Kommunikation

**Interne Kommunikation:**
- Status-Updates alle 30 Minuten
- Stakeholder-Benachrichtigungen
- Intranet-Status-Page

**Externe Kommunikation:**
- Kunden-Benachrichtigungen (falls zutreffend)
- Medien-Statement (bei Bedarf)
- Regulatorische Meldungen

## 5. Security Incident Response

### 5.1 Security Incident Response Team (SIRT)

**Mitglieder:**
- CISO oder Security Lead
- IT-Security-Analysten
- IT-Forensik-Experte
- Legal/Compliance
- HR (bei Insider Threats)

### 5.2 Security Incident Prozess

**Phase 1: Preparation**
- Incident-Response-Plan aktuell
- Tools und Playbooks bereit
- Team geschult

**Phase 2: Identification**
- Security-Event detektiert (SIEM, EDR, etc.)
- Triage: Ist es ein Incident?
- Severity bestimmen

**Phase 3: Containment**
- **Short-term:** Sofortige Maßnahmen (Account sperren, Netzwerk isolieren)
- **Long-term:** Dauerhafte Isolation

**Phase 4: Eradication**
- Malware entfernen
- Schwachstellen patchen
- Kompromittierte Credentials ändern

**Phase 5: Recovery**
- Systeme wiederherstellen
- Monitoring intensivieren
- Schrittweise Rückkehr zum Normalbetrieb

**Phase 6: Lessons Learned**
- Post-Incident Review
- Playbook-Updates
- Training-Bedarf identifizieren

### 5.3 Forensik

**Wann erforderlich:**
- Data Breaches
- Insider Threats
- Rechtliche Ermittlungen
- Schwere Security Incidents

**Prozess:**
1. **Preservation:** Beweise sichern
2. **Collection:** Daten sammeln (Disk Images, Logs, Memory Dumps)
3. **Analysis:** Forensische Analyse
4. **Reporting:** Forensik-Bericht
5. **Chain of Custody:** Lückenlose Dokumentation

**Tools:** {{ meta.security.forensics_tools }}

### 5.4 Meldepflichten

**Intern:**
- CISO: Sofort
- Management: Innerhalb 4 Stunden
- Datenschutzbeauftragter: Bei Datenschutzverletzung

**Extern:**
- **DSGVO:** Datenschutzbehörde innerhalb 72 Stunden (bei Datenschutzverletzung)
- **Betroffene Personen:** Ohne unangemessene Verzögerung
- **Strafverfolgung:** Bei kriminellen Handlungen

## 6. Incident-Kommunikation

### 6.1 Status-Updates

**Frequenz:**
- P1: Alle 30 Minuten
- P2: Alle 2 Stunden
- P3/P4: Täglich

**Kanäle:**
- E-Mail an Stakeholder
- Status-Page ({{ meta.status.url }})
- Intranet-Benachrichtigungen

### 6.2 Stakeholder-Matrix

| Stakeholder | P1 | P2 | P3 | P4 |
|-------------|----|----|----|----|
| Betroffene Nutzer | Sofort | 1h | 4h | 1d |
| Management | 15min | 2h | - | - |
| CISO (Security) | Sofort | Sofort | 4h | - |
| Kunden (extern) | 1h | 4h | - | - |

## 7. Compliance und Audit

### 7.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| P1 Response-Zeit | < 15 Minuten |
| P1 Resolution-Zeit | < 4 Stunden |
| Major Incident PIR-Completion | 100% |
| Security Incident Detection-Zeit | < 1 Stunde |

### 7.2 Audit-Nachweise

- Incident-Tickets und -Logs
- Post-Incident-Review-Berichte
- Kommunikations-Logs
- Forensik-Berichte (bei Security Incidents)

## 8. Referenzen

### Interne Dokumente
- `0400_Policy_Incident_Management.md`
- `0320_Policy_Logging_und_Monitoring.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.24** - Information security incident management planning
- **ISO/IEC 27001:2022 Annex A.5.25** - Assessment and decision on information security events
- **ISO/IEC 27001:2022 Annex A.5.26** - Response to information security incidents
- **NIST SP 800-61** - Computer Security Incident Handling Guide

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

