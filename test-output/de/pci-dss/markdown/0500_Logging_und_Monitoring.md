# Logging und Monitoring

**Dokument-ID:** PCI-0500  
**Organisation:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---



## 1. Zweck

Dieses Dokument definiert die Logging- und Monitoring-Anforderungen für AdminSend GmbH gemäß PCI-DSS Requirement 10.

### 1.1 Ziele

- **Nachvollziehbarkeit:** Alle Zugriffe auf CDE und CHD loggen
- **Anomalie-Erkennung:** Verdächtige Aktivitäten identifizieren
- **Incident Response:** Forensische Untersuchungen ermöglichen
- **Compliance:** Erfüllung von PCI-DSS Requirement 10

### 1.2 Geltungsbereich

**Betroffene Systeme:**
- Alle CDE-Systeme
- Systeme mit CHD-Zugriff
- Netzwerkkomponenten
- Sicherheitssysteme

## 2. Logging-Anforderungen

### 2.1 Zu loggende Ereignisse

**Benutzer-Zugriffe:**
- Alle Anmeldungen (erfolgreich und fehlgeschlagen)
- Alle Abmeldungen
- Privilegierte Aktionen
- Zugriff auf CHD
- Berechtigungsänderungen

**System-Ereignisse:**
- System-Starts und -Stops
- Konfigurationsänderungen
- Software-Installationen
- Patch-Installationen
- Dienst-Starts und -Stops

**Netzwerk-Ereignisse:**
- Firewall-Regel-Änderungen
- Blockierte Verbindungen
- VPN-Verbindungen
- IDS/IPS-Alerts

**Sicherheits-Ereignisse:**
- Antivirus-Detektionen
- Sicherheitsrichtlinien-Verletzungen
- Account-Sperrungen
- Passwortänderungen

**Datenbank-Ereignisse:**
- Alle Zugriffe auf CHD-Tabellen
- Schema-Änderungen
- Privilegierte Datenbankoperationen
- Fehlgeschlagene Zugriffe

### 2.2 Log-Einträge-Format

**Erforderliche Felder:**
- **Benutzer-ID:** Wer hat die Aktion durchgeführt?
- **Ereignistyp:** Was ist passiert?
- **Zeitstempel:** Wann ist es passiert? (synchronisierte Zeit)
- **Erfolg/Fehler:** War die Aktion erfolgreich?
- **Quelle:** Von wo kam die Aktion? (IP-Adresse, Hostname)
- **Ziel:** Welches System/Ressource war betroffen?
- **Zusätzliche Details:** Relevante Kontextinformationen

**Beispiel:**
```
2026-02-06 14:32:15 UTC | USER=john.doe | EVENT=LOGIN_SUCCESS | SOURCE=10.1.100.50 | TARGET=payment-gateway-01 | DETAILS=MFA_VERIFIED
```

## 3. SIEM-System

### 3.1 SIEM-Implementierung

**SIEM-System:** [TODO: Name des SIEM-Systems]

**Funktionen:**
- Zentrale Log-Sammlung
- Echtzeitanalyse
- Korrelation von Ereignissen
- Alerting
- Reporting
- Forensische Suche

**Architektur:**
- Log-Quellen → Log-Forwarder → SIEM
- Verschlüsselte Übertragung (TLS 1.2+)
- Redundante SIEM-Server
- Sichere Log-Speicherung

### 3.2 Log-Forwarding

**Konfiguration:**
- Alle CDE-Systeme senden Logs an SIEM
- Echtzeitübertragung (< 5 Minuten Verzögerung)
- Verschlüsselte Übertragung
- Authentifizierung der Log-Quellen

**Log-Forwarder:**
- Syslog (RFC 5424)
- Windows Event Forwarding
- Agent-basiert (z.B., Splunk Forwarder, Elastic Beats)

### 3.3 Log-Parsing und -Normalisierung

**Anforderungen:**
- Einheitliches Log-Format
- Parsing aller relevanten Felder
- Normalisierung von Zeitstempeln
- Anreicherung mit Kontext (z.B., Geo-IP)

## 4. Log-Retention

### 4.1 Aufbewahrungsfristen

**Online-Speicherung:**
- 90 Tage in SIEM (schneller Zugriff)
- Volltext-Suche möglich
- Echtzeitanalyse

**Archiv-Speicherung:**
- 1 Jahr in Archiv
- Komprimiert
- Verschlüsselt
- WORM-Speicher (Write Once Read Many)

**Langzeit-Archivierung:**
- Nach gesetzlichen Anforderungen
- Sichere Lagerung
- Dokumentation

### 4.2 Log-Backup

**Anforderungen:**
- Tägliche Backups der Logs
- Offsite-Lagerung
- Verschlüsselte Backups
- Regelmäßige Restore-Tests

## 5. Log-Integrität

### 5.1 Schutz vor Manipulation

**Maßnahmen:**
- WORM-Speicher für Logs
- Digitale Signaturen
- Hash-Werte für Log-Dateien
- Zugriffskontrolle auf Logs
- Logging von Log-Zugriffen

**Validierung:**
- Regelmäßige Integritätsprüfung
- Automatische Alerts bei Manipulation
- Forensische Untersuchung bei Verdacht

### 5.2 Log-Zugriffskontrolle

**Berechtigungen:**
- Nur autorisiertes Personal
- Read-Only-Zugriff für die meisten Benutzer
- Vollzugriff nur für Log-Administratoren
- Logging aller Log-Zugriffe

**Rollen:**
- Log-Administrator: Vollzugriff
- Security-Analyst: Lesezugriff, Suche, Alerting
- Auditor: Lesezugriff
- Standard-Benutzer: Kein Zugriff

## 6. Zeitsynchronisation

### 6.1 NTP-Konfiguration

**Anforderungen:**
- Alle Systeme synchronisiert mit NTP
- Interne NTP-Server
- Externe NTP-Quellen (Stratum 1 oder 2)
- Redundante NTP-Server

**NTP-Server:**
- Primär: [TODO: IP-Adresse]
- Sekundär: [TODO: IP-Adresse]
- Externe Quelle: [TODO: z.B., ptbtime1.ptb.de]

**Zeitzone:**
- UTC für alle Logs
- Lokale Zeitzone für Anzeige (mit UTC-Offset)

### 6.2 Zeitabweichungs-Monitoring

**Überwachung:**
- Maximale Abweichung: 1 Sekunde
- Alerts bei Abweichung > 1 Sekunde
- Automatische Korrektur
- Logging von Zeitänderungen

## 7. Monitoring und Alerting

### 7.1 Security Monitoring

**24/7 Monitoring:**
- Security Operations Center (SOC)
- Echtzeitüberwachung aller Alerts
- Incident Response bei kritischen Alerts
- Eskalation nach Schweregrad

**SOC-Team:**
- SOC-Analyst (Tier 1)
- Senior SOC-Analyst (Tier 2)
- Security Engineer (Tier 3)
- CISO (Eskalation)

### 7.2 Alerting-Regeln

**Kritische Alerts:**

| Alert | Bedingung | Aktion | Eskalation |
|-------|-----------|--------|------------|
| Mehrfache fehlgeschlagene Logins | >10 in 5 Min | Sofortige Untersuchung | SOC → CISO |
| Unbefugter CDE-Zugriff | Blockierte Verbindung zu CDE | Sofortige Untersuchung | SOC → IT Security |
| Malware-Detektion | Antivirus-Alert | Isolation des Systems | SOC → IT Security |
| Datenexfiltration | Große Datenübertragung | Verbindung blockieren | SOC → CISO |
| Privilegierte Aktion | Root/Admin-Aktion | Logging, Review | SOC |
| Firewall-Regel-Änderung | Konfigurationsänderung | Validierung | SOC → Network Team |

**Hohe Alerts:**
- Admin-Login außerhalb Geschäftszeiten
- Zugriff auf CHD
- Konfigurationsänderungen
- Neue Software-Installation

**Mittlere Alerts:**
- Fehlgeschlagene Authentifizierung
- Passwortänderung
- Account-Sperrung

**Niedrige Alerts:**
- Informative Ereignisse
- Routine-Aktivitäten

### 7.3 Alert-Response

**Prozess:**
1. Alert empfangen
2. Schweregrad bewerten
3. Initiale Untersuchung
4. Eskalation (falls erforderlich)
5. Incident Response (falls erforderlich)
6. Dokumentation
7. Follow-up

**Response-Zeiten:**
- Kritisch: Sofort (< 15 Minuten)
- Hoch: < 1 Stunde
- Mittel: < 4 Stunden
- Niedrig: < 24 Stunden

## 8. Log-Review

### 8.1 Tägliche Log-Review

**Prozess:**
- Automatisierte Analyse durch SIEM
- Review kritischer Alerts
- Identifikation von Anomalien
- Dokumentation von Findings

**Verantwortlich:** SOC-Team

### 8.2 Wöchentliche Log-Review

**Prozess:**
- Review aller Alerts der Woche
- Trend-Analyse
- Identifikation von Mustern
- Optimierung von Alerting-Regeln

**Verantwortlich:** Senior SOC-Analyst

### 8.3 Monatliche Log-Review

**Prozess:**
- Umfassende Analyse aller Logs
- Compliance-Validierung
- Reporting an Management
- Identifikation von Verbesserungen

**Verantwortlich:** IT Security Manager

## 9. Use Cases und Korrelationsregeln

### 9.1 Definierte Use Cases

**Authentifizierung:**
- Brute-Force-Angriffe
- Credential Stuffing
- Ungewöhnliche Login-Zeiten
- Geografische Anomalien

**Zugriffskontrolle:**
- Unbefugte Zugriffe
- Privilegien-Eskalation
- Lateral Movement

**Datenexfiltration:**
- Große Datenübertragungen
- Ungewöhnliche Datenzugriffe
- Zugriff auf viele Datensätze

**Malware:**
- Antivirus-Detektionen
- Verdächtige Prozesse
- Command & Control-Kommunikation

**Insider-Bedrohungen:**
- Ungewöhnliche Benutzeraktivitäten
- Zugriff außerhalb Arbeitszeiten
- Massendownloads

### 9.2 Korrelationsregeln

**Beispiel-Regel: Brute-Force-Angriff**
```
IF (fehlgeschlagene_logins > 10 IN 5 Minuten)
AND (gleiche_quell_ip)
THEN
  ALERT "Brute-Force-Angriff erkannt"
  SEVERITY = CRITICAL
  ACTION = Block_IP
```

**Beispiel-Regel: Privilegien-Eskalation**
```
IF (benutzer_erhält_admin_rechte)
AND (benutzer_führt_privilegierte_aktion_aus IN 10 Minuten)
THEN
  ALERT "Mögliche Privilegien-Eskalation"
  SEVERITY = HIGH
  ACTION = Investigate
```

## 10. Audit Trails

### 10.1 Audit Trail-Anforderungen

**Für alle CHD-Zugriffe:**
- Vollständige Audit Trails
- Unveränderlich
- Nachvollziehbar
- Zeitlich geordnet

**Informationen:**
- Wer hat zugegriffen?
- Wann wurde zugegriffen?
- Welche Daten wurden zugegriffen?
- Welche Aktion wurde durchgeführt?
- War die Aktion erfolgreich?

### 10.2 Audit Trail-Review

**Prozess:**
- Regelmäßige Review (täglich für kritische Systeme)
- Identifikation von Anomalien
- Dokumentation von Findings
- Follow-up bei Auffälligkeiten

## 11. Forensische Untersuchungen

### 11.1 Log-Analyse für Forensik

**Prozess:**
1. Incident identifiziert
2. Relevante Logs sammeln
3. Timeline erstellen
4. Ursachenanalyse
5. Dokumentation
6. Lessons Learned

**Tools:**
- SIEM-Forensik-Funktionen
- Log-Analyse-Tools
- Timeline-Analyse-Tools

### 11.2 Chain of Custody

**Anforderungen:**
- Dokumentation aller Log-Zugriffe
- Unveränderlichkeit der Logs
- Nachvollziehbare Beweiskette
- Rechtssichere Dokumentation

## 12. Compliance-Validierung

### 12.1 Validierungsaktivitäten

**Täglich:**
- Log-Review
- Alert-Response
- Anomalie-Erkennung

**Wöchentlich:**
- Trend-Analyse
- Use Case-Validierung

**Monatlich:**
- Umfassende Log-Review
- Compliance-Reporting

**Quartalsweise:**
- Log-Retention-Validierung
- SIEM-Konfiguration-Review

**Jährlich:**
- Vollständige Logging-Audit
- Penetrationstest
- Compliance-Assessment

### 12.2 Validierungsdokumentation

**Erforderliche Nachweise:**
- Logging-Konfiguration
- SIEM-Konfiguration
- Log-Review-Protokolle
- Alert-Response-Protokolle
- Forensische Untersuchungsberichte

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |


