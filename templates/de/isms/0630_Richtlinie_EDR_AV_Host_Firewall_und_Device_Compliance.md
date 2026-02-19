# Richtlinie: EDR, Antivirus, Host-Firewall und Device Compliance

**Dokument-ID:** 0630
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0620_Policy_Endpoint_Security.md` und definiert:
- Endpoint Detection and Response (EDR) Anforderungen
- Antivirus-Konfiguration und -Management
- Host-Firewall-Policies
- Device-Compliance-Anforderungen

**Geltungsbereich:** Alle Endpoints bei **{{ meta-organisation.name }}**

## 2. Endpoint Detection and Response (EDR)

### 2.1 EDR-System

**Plattform:** {{ meta-handbook.security_edr_solution }} (z.B. CrowdStrike, SentinelOne, Microsoft Defender for Endpoint)

**Funktionen:**
- Real-time Threat Detection
- Behavioral Analysis
- Automated Response
- Forensic Capabilities
- Threat Hunting

### 2.2 EDR-Deployment

**Pflicht-Installation:**
- Alle Workstations (Windows, macOS, Linux)
- Alle Server
- Keine Ausnahmen (außer über Ausnahmenprozess)

**Deployment-Methoden:**
- Group Policy (Windows)
- MDM (macOS, Mobile)
- Configuration Management (Linux)

### 2.3 EDR-Policies

**Detection-Modi:**
- **Prevent:** Automatische Blockierung (Standard)
- **Detect:** Nur Alerting (für Legacy-Systeme)

**Behavioral Policies:**
- Ransomware-Protection
- Credential-Theft-Protection
- Exploit-Protection
- Script-Control (PowerShell, CMD)

### 2.4 EDR-Response

**Automatische Aktionen:**
- Malware-Quarantäne
- Prozess-Terminierung
- Netzwerk-Isolation (bei kritischen Threats)

**Manuelle Aktionen:**
- Remote Shell für Forensik
- File Retrieval
- Memory Dump

### 2.5 Tamper Protection

**Schutz vor Deaktivierung:**
- EDR-Agent kann nicht deaktiviert werden (ohne Admin-Passwort)
- Uninstall-Passwort erforderlich
- Alerts bei Tamper-Versuchen

## 3. Antivirus (AV)

### 3.1 AV-System

**Plattform:** {{ meta-handbook.security_av_solution }} (oft integriert in EDR)

**Scan-Typen:**
- Real-time Scanning (On-Access)
- Scheduled Full Scans (wöchentlich)
- Quick Scans (täglich)

### 3.2 AV-Konfiguration

**Scan-Einstellungen:**
- Alle Dateitypen scannen
- Archive scannen
- E-Mail-Anhänge scannen
- Removable Media scannen

**Exclusions:**
- Nur nach Genehmigung durch IT-Security
- Dokumentation erforderlich
- Regelmäßiger Review (quartalsweise)

### 3.3 Signature-Updates

**Automatische Updates:**
- Mehrmals täglich
- Über interne Update-Server (WSUS, etc.)
- Fallback auf Cloud-Updates

**Monitoring:**
- Alerts bei veralteten Signaturen (> 7 Tage)

### 3.4 Malware-Handling

**Bei Malware-Detektion:**
1. Automatische Quarantäne
2. Alert an Security-Team
3. Incident-Ticket erstellen
4. Forensische Analyse (bei Bedarf)
5. Remediation
6. Lessons Learned

## 4. Host-Firewall

### 4.1 Windows Firewall

**Konfiguration via GPO:**
- Firewall aktiviert (alle Profile: Domain, Private, Public)
- Inbound: Default Deny
- Outbound: Default Allow (mit Ausnahmen)

**Erlaubte Inbound-Verbindungen:**
- Remote Desktop (nur von Management-VLAN)
- File Sharing (nur im Corporate Network)
- Monitoring-Agents

### 4.2 macOS Firewall

**Konfiguration via MDM:**
- Application Firewall aktiviert
- Stealth Mode aktiviert
- Nur signierte Apps erlaubt

### 4.3 Linux Firewall

**iptables/firewalld:**
- Default Deny für Inbound
- Nur erforderliche Services erlaubt
- Logging aktiviert

## 5. Device Compliance

### 5.1 Compliance-Anforderungen

**Pflicht-Anforderungen:**
- EDR/AV installiert und aktiv
- OS-Patches aktuell (< 30 Tage alt)
- Disk-Verschlüsselung aktiviert
- Host-Firewall aktiviert
- Screen-Lock konfiguriert (max. 15 Minuten)
- Kein Jailbreak/Root (Mobile)

### 5.2 Compliance-Checks

**Automatische Prüfung:**
- Bei jedem Netzwerk-Zugriff (NAC)
- Bei VPN-Verbindung
- Täglich (Endpoint-Management)

**Bei Non-Compliance:**
- Warnung an Nutzer (24 Stunden Frist)
- Eingeschränkter Netzwerk-Zugriff
- Vollständige Sperrung nach 7 Tagen

### 5.3 Compliance-Reporting

**Wöchentlicher Report:**
- Compliance-Rate pro Abteilung
- Top Non-Compliance-Items
- Trend-Analyse

**Ziel:** > 95% Compliance

## 6. Patch Management

### 6.1 OS-Patches

**Windows:**
- WSUS für Patch-Verteilung
- Automatische Installation (außerhalb Geschäftszeiten)
- Reboot-Fenster: Wochenende

**macOS:**
- Automatische Updates über MDM
- Deferred Updates (7 Tage Test-Period)

**Linux:**
- Automatische Security-Updates (unattended-upgrades)
- Manuelle Updates für Kernel

### 6.2 Application-Patches

**Third-Party-Applications:**
- Ninite, Chocolatey für automatische Updates
- Manuelle Updates für kritische Apps

**Patch-SLA:**
- Critical: 7 Tage
- High: 30 Tage
- Medium: 90 Tage

**Details:** Siehe `0350_Richtlinie_Vulnerability_Scans_Patching`

## 7. Application Control

### 7.1 Application Whitelisting

**Für kritische Systeme:**
- Nur signierte, genehmigte Anwendungen
- Blockierung nicht genehmigter Software
- Ausnahmen über Ticketsystem

**Tools:**
- Windows Defender Application Control (WDAC)
- AppLocker

### 7.2 Script Control

**PowerShell:**
- Constrained Language Mode
- Script-Signing erforderlich
- Logging aktiviert

**CMD/Batch:**
- Blockiert für Standard-Nutzer
- Nur für Admins

## 8. USB und Removable Media

### 8.1 USB-Control

**Policies:**
- USB-Storage blockiert (Standard-Nutzer)
- Nur genehmigte USB-Geräte (Whitelist)
- Automatisches Scannen bei Anschluss

**Ausnahmen:**
- Antrag über Ticketsystem
- Zeitlich befristet
- Verschlüsselte USB-Sticks

### 8.2 DLP für Removable Media

**Data Loss Prevention:**
- Blockierung vertraulicher Daten auf USB
- Alerts bei Kopierversuchen
- Logging aller USB-Aktivitäten

## 9. Monitoring und Alerting

### 9.1 Endpoint-Monitoring

**Überwachte Metriken:**
- EDR/AV-Status
- Patch-Level
- Compliance-Status
- Malware-Detektionen
- Anomalien (CPU, Netzwerk)

### 9.2 SIEM-Integration

**Events zu SIEM:**
- Malware-Detektionen
- EDR-Alerts
- Compliance-Violations
- Tamper-Attempts

### 9.3 Automated Response

**SOAR-Integration:**
- Automatische Isolation bei Malware
- Automatische Ticket-Erstellung
- Automatische Benachrichtigungen

## 10. Compliance und Audit

### 10.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| EDR-Deployment-Rate | 100% |
| AV-Signature-Aktualität | 100% |
| Device-Compliance-Rate | > 95% |
| Malware-Detection-Rate | Baseline |
| Patch-Compliance (30 Tage) | > 90% |

### 10.2 Audit-Nachweise

- EDR-Deployment-Status
- Compliance-Reports
- Malware-Incident-Reports
- Patch-Compliance-Reports

## 11. Referenzen

### Interne Dokumente
- `0620_Policy_Endpoint_Security.md`
- `0350_Richtlinie_Vulnerability_Scans_Patching_und_Exploitation_Response.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.7** - Protection against malware
- **NIST SP 800-83** - Guide to Malware Incident Prevention and Handling
- **CIS Controls** - Malware Defenses

**Genehmigt durch:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

