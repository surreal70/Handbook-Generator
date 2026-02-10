# Policy: Logging und Monitoring

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for logging, monitoring, and security event management.
It ensures that security-relevant events are logged, monitored, and analyzed to detect
and respond to security incidents. Customize based on your organization's SIEM/SOC
capabilities and compliance requirements.

ISO 27001:2022 Annex A Reference: A.8.15, A.8.16
-->

**Dokument-ID:** 0320  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.8.15, A.8.16 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Grundsätze für Logging, Monitoring und Security Event Management der **{{ meta.organization.name }}**. Sie stellt sicher, dass sicherheitsrelevante Ereignisse erfasst, überwacht und analysiert werden, um Sicherheitsvorfälle zu erkennen, zu untersuchen und darauf zu reagieren.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta.organization.name }}
- **Systeme:** Alle IT-Systeme, Anwendungen, Netzwerkkomponenten, Sicherheitssysteme
- **Log-Quellen:** Server, Workstations, Netzwerkgeräte, Firewalls, IDS/IPS, Anwendungen, Datenbanken
- **Monitoring-Bereiche:** Sicherheit, Performance, Verfügbarkeit, Compliance
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Umfassendes Logging
Alle sicherheitsrelevanten Ereignisse werden protokolliert:
- Authentisierungsversuche (erfolgreich und fehlgeschlagen)
- Zugriffe auf sensible Daten und Systeme
- Privilegierte Aktivitäten (Admin-Zugriffe, Konfigurationsänderungen)
- Sicherheitsvorfälle und Anomalien
- System- und Anwendungsfehler

### 3.2 Zentralisiertes Log-Management
Logs werden zentral in einem SIEM (Security Information and Event Management) System gesammelt, gespeichert und analysiert. Dies ermöglicht korrelierte Analysen und effiziente Incident Response.

### 3.3 Log-Integrität und Schutz
Logs werden vor unbefugter Änderung und Löschung geschützt:
- Schreibgeschützte Log-Speicherung
- Integritätsprüfungen (Hashing, digitale Signaturen)
- Zugriffskontrolle auf Log-Systeme
- Verschlüsselte Übertragung

### 3.4 Retention und Aufbewahrung
Logs werden entsprechend gesetzlicher, regulatorischer und geschäftlicher Anforderungen aufbewahrt:
- Sicherheitslogs: Mindestens 12 Monate online, 7 Jahre Archiv
- Audit-Logs: Entsprechend Compliance-Anforderungen
- Performance-Logs: Entsprechend Betriebsanforderungen

### 3.5 Proaktives Monitoring und Alerting
Sicherheitsrelevante Ereignisse werden proaktiv überwacht und bei Anomalien werden Alerts generiert:
- Real-time Monitoring kritischer Systeme
- Automatisierte Alerting-Regeln
- Eskalationsprozesse für kritische Alerts
- 24/7 SOC (Security Operations Center) für kritische Systeme

### 3.6 SIEM Use Cases und Detection Rules
SIEM-Systeme werden mit Use Cases und Detection Rules konfiguriert, um bekannte Angriffsmuster und Anomalien zu erkennen:
- Brute-Force-Angriffe
- Privilege Escalation
- Data Exfiltration
- Malware-Aktivitäten
- Insider-Threats

### 3.7 Log-Analyse und Forensik
Logs werden regelmäßig analysiert und bei Sicherheitsvorfällen für forensische Untersuchungen genutzt:
- Regelmäßige Log-Reviews
- Threat Hunting
- Incident Investigation
- Root Cause Analysis

### 3.8 Datenschutz-Compliance
Logging und Monitoring erfolgen in Übereinstimmung mit Datenschutzvorschriften (DSGVO):
- Minimierung personenbezogener Daten in Logs
- Zweckbindung der Log-Daten
- Zugriffskontrolle auf personenbezogene Log-Daten
- Löschung nach Ablauf der Retention-Periode

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Logging und Monitoring

| Aktivität | CISO | SOC/Security Operations | IT-Betrieb | System Owner | DPO |
|-----------|------|-------------------------|------------|--------------|-----|
| Policy-Erstellung | R/A | C | C | C | C |
| SIEM-Betrieb | A | R | C | I | I |
| Log-Konfiguration | C | C | R | R | I |
| Monitoring und Alerting | A | R | C | I | I |
| Incident Investigation | A | R | C | C | C |
| Log-Retention | C | C | R | I | C |
| Compliance-Prüfung | R/A | C | C | I | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **SOC Manager:** {{ meta.security.soc_manager }}
- **SIEM Administrator:** {{ meta.it.siem_admin }}
- **Umsetzungsverantwortliche:** SOC, IT-Betrieb, System Owner
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, DPO

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0330_Richtlinie_Logging_SIEM_und_Audit_Trails.md** - Detaillierte Implementierungsrichtlinie
- `0400_Policy_Incident_Management.md` - Incident Management Policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Data Protection Policy
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Vulnerability Management Policy

### Zugehörige Standards/Baselines
- Log-Standards und Formate
- SIEM Use Cases und Detection Rules
- Retention-Anforderungen
- Alerting-Schwellwerte

### Zugehörige Prozesse
- Log-Onboarding-Prozess
- Alert-Triage und Eskalation
- Incident Investigation
- Log-Review-Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl Log-Quellen im SIEM (Ziel: 100% kritischer Systeme)
- Log-Vollständigkeit und -Verfügbarkeit (Ziel: 99.9%)
- Durchschnittliche Zeit zur Alert-Triage (MTTD - Mean Time To Detect)
- Anzahl False Positives pro Tag
- SIEM Use Case Coverage
- Compliance-Rate mit Retention-Anforderungen

### Nachweise und Evidence
- SIEM-Konfiguration und Use Cases
- Log-Retention-Nachweise
- Alert-Statistiken und Triage-Reports
- Incident Investigation Reports
- Audit-Berichte zu Logging und Monitoring
- Datenschutz-Impact-Assessments

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Deaktivierung von Logging:** Sofortige Remediation, Untersuchung
- **Unbefugte Log-Manipulation:** Incident Response, arbeitsrechtliche Konsequenzen
- **Nicht-Compliance mit Retention:** Remediation, Nachschulung
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Sicherheitsmaßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0330_Richtlinie_Logging_SIEM_und_Audit_Trails.md` - Detailed Guideline
- `0400_Policy_Incident_Management.md` - Incident Management Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.15** - Logging
- **ISO/IEC 27001:2022 Annex A.8.16** - Monitoring activities
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-92** - Guide to Computer Security Log Management
- **DSGVO (EU 2016/679)** - Datenschutz-Grundverordnung
- **BSI IT-Grundschutz** - Baustein OPS.1.1.5 Protokollierung

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
