# Richtlinie: Logging, SIEM und Audit Trails

**Dokument-ID:** 0330
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

Diese Richtlinie konkretisiert die `0320_Policy_Logging_und_Monitoring.md` und definiert:
- Logging-Anforderungen pro System-Typ
- SIEM-Integration und Use Cases
- Audit-Trail-Anforderungen und Retention

**Geltungsbereich:** Alle IT-Systeme bei **{{ meta-organisation.name }}**

## 2. Logging-Anforderungen

### 2.1 Zu protokollierende Events

**Authentifizierung:**
- Erfolgreiche und fehlgeschlagene Logins
- Logout-Events
- MFA-Challenges und -Ergebnisse
- Passwort-Änderungen und -Resets
- Account-Sperrungen und -Entsperrungen

**Autorisierung:**
- Zugriffe auf vertrauliche Daten
- Privilegierte Operationen (sudo, Admin-Rechte)
- Zugriffsverweiger ungen (Access Denied)
- Änderungen an Berechtigungen

**System-Events:**
- System-Start und -Shutdown
- Service-Starts und -Stops
- Konfigurationsänderungen
- Software-Installationen und -Updates
- Fehler und Exceptions

**Daten-Events:**
- Datei-Zugriffe (Lesen, Schreiben, Löschen)
- Datenbank-Queries (bei sensiblen Daten)
- Daten-Exporte und -Downloads
- Backup-Operationen

**Netzwerk-Events:**
- Firewall-Blocks und -Allows
- VPN-Verbindungen
- Netzwerk-Scans
- Anomalien im Traffic

### 2.2 Log-Format und Inhalte

**Pflichtfelder:**
- Timestamp (UTC, ISO 8601)
- Event-Typ und Severity
- Quelle (System, Anwendung, IP)
- Nutzer/Account
- Aktion/Operation
- Ergebnis (Erfolg/Fehler)
- Zusätzliche Kontextinformationen

**Beispiel (JSON):**
```json
{
  "timestamp": "2024-02-02T10:15:30Z",
  "event_type": "authentication",
  "severity": "info",
  "source_ip": "192.168.1.100",
  "user": "jdoe",
  "action": "login",
  "result": "success",
  "mfa_method": "authenticator_app"
}
```

### 2.3 Logging-Level

| System-Typ | Logging-Level | Begründung |
|------------|---------------|------------|
| Produktionssysteme | INFO | Balance zwischen Detail und Performance |
| Entwicklungssysteme | DEBUG | Fehlersuche |
| Sicherheitssysteme (Firewall, IDS) | VERBOSE | Maximale Sichtbarkeit |
| Privilegierte Systeme | VERBOSE | Compliance und Forensik |

## 3. SIEM-Integration

### 3.1 SIEM-System

**Plattform:** {{ meta-handbook.security_siem_solution }} (z.B. Splunk, Microsoft Sentinel, Elastic SIEM)

**Architektur:**
- Log-Sammlung über Agents oder Syslog
- Zentrale Log-Aggregation
- Normalisierung und Enrichment
- Korrelation und Alerting
- Langzeit-Archivierung

### 3.2 Log-Quellen

**Priorität 1 (Kritisch):**
- Active Directory / Azure AD
- Firewalls und IDS/IPS
- VPN-Gateways
- Privilegierte Access Management (PAM)
- Datenbanken mit vertraulichen Daten

**Priorität 2 (Hoch):**
- Web-Server und Application-Server
- E-Mail-Gateways
- Cloud-Services (Azure, AWS, Google Cloud)
- Endpoint Detection and Response (EDR)

**Priorität 3 (Mittel):**
- Workstations und Laptops
- Netzwerk-Switches
- Drucker und IoT-Geräte

### 3.3 SIEM Use Cases

**Authentifizierung:**
- Brute-Force-Angriffe (> 10 fehlgeschlagene Logins in 5 Minuten)
- Unmögliche Reisen (Logins von geografisch unmöglichen Standorten)
- Privilegierte Account-Nutzung außerhalb Geschäftszeiten

**Malware und Intrusion:**
- Malware-Detektionen durch EDR
- IDS/IPS-Alerts
- Command & Control (C2) Kommunikation
- Lateral Movement (ungewöhnliche interne Verbindungen)

**Data Exfiltration:**
- Große Datenmengen-Uploads zu externen Zielen
- Zugriff auf viele vertrauliche Dateien in kurzer Zeit
- Ungewöhnliche Datenbank-Queries

**Compliance:**
- Zugriffe auf PII (Personally Identifiable Information)
- Änderungen an Sicherheitskonfigurationen
- Privilegierte Operationen ohne Genehmigung

### 3.4 Alerting und Response

**Severity-Level:**
- **Critical:** Sofortige Eskalation an On-Call Security (24/7)
- **High:** Eskalation innerhalb 1 Stunde
- **Medium:** Bearbeitung innerhalb 4 Stunden
- **Low:** Bearbeitung innerhalb 1 Arbeitstag

**Automatische Response:**
- Account-Sperrung bei Brute-Force
- IP-Blockierung bei Malware-C2
- Quarantäne von Endpoints bei Malware-Detektion

## 4. Audit Trails

### 4.1 Anforderungen

**Unveränderlichkeit:**
- Logs dürfen nicht nachträglich geändert werden
- Kryptographische Signaturen oder Write-Once-Storage
- Zugriff auf Logs nur für autorisierte Personen

**Vollständigkeit:**
- Lückenlose Aufzeichnung aller relevanten Events
- Monitoring der Log-Integrität
- Alerts bei Log-Ausfällen

**Nachvollziehbarkeit:**
- Wer hat was wann gemacht?
- Rekonstruktion von Ereignisketten
- Forensische Analyse möglich

### 4.2 Privilegierte Zugriffe

**Zusätzliche Anforderungen:**
- Session-Recording für privilegierte Zugriffe
- Vier-Augen-Prinzip bei kritischen Operationen
- Genehmigungsworkflow vor Zugriff
- Detaillierte Protokollierung aller Aktionen

**PAM-Integration:**
- Privileged Access Management System: {{ meta-handbook.security_pam_solution }}
- Just-in-Time (JIT) Access
- Automatische Passwort-Rotation
- Session-Monitoring und -Recording

### 4.3 Compliance-Audit-Trails

**Regulatorische Anforderungen:**
- DSGVO: Zugriffe auf personenbezogene Daten
- SOX: Finanzrelevante Transaktionen
- HIPAA: Zugriffe auf Gesundheitsdaten (falls zutreffend)

**Dokumentation:**
- Wer hat auf welche Daten zugegriffen?
- Zweck des Zugriffs
- Genehmigung (falls erforderlich)
- Zeitraum

## 5. Log-Retention

### 5.1 Aufbewahrungsfristen

| Log-Typ | Retention (Online) | Retention (Archiv) | Begründung |
|---------|--------------------|--------------------|------------|
| Security-Logs | 90 Tage | {{ meta-handbook.retention_log_years }} Jahre | Forensik, Compliance |
| Authentifizierungs-Logs | 90 Tage | {{ meta-handbook.retention_log_years }} Jahre | Audit, Compliance |
| System-Logs | 30 Tage | 1 Jahr | Troubleshooting |
| Application-Logs | 30 Tage | 1 Jahr | Debugging |
| Audit-Trails (Compliance) | 180 Tage | {{ meta-handbook.retention_audit_years }} Jahre | Regulatorisch |

### 5.2 Archivierung

**Prozess:**
1. Logs älter als Retention-Period (Online) werden archiviert
2. Komprimierung und Verschlüsselung
3. Übertragung zu Archiv-Storage (z.B. Azure Blob Archive, AWS Glacier)
4. Verifizierung der Archivierung
5. Löschung aus Online-SIEM

**Zugriff auf Archiv:**
- Nur bei begründetem Bedarf (Forensik, Audit)
- Genehmigung durch CISO
- Wiederherstellung in SIEM für Analyse

### 5.3 Sichere Löschung

**Nach Ablauf der Retention:**
- Automatische Löschung aus Archiv
- Kryptographische Löschung (Schlüssel vernichten)
- Dokumentation der Löschung

## 6. Log-Sicherheit

### 6.1 Zugriffskontrolle

**Berechtigungen:**
- **Security-Team:** Vollzugriff auf alle Logs
- **IT-Betrieb:** Zugriff auf System- und Application-Logs
- **Auditoren:** Read-Only-Zugriff auf Audit-Trails
- **Entwickler:** Zugriff nur auf Dev-Logs

**Authentifizierung:**
- MFA für SIEM-Zugriff
- Privilegierte Accounts für Admin-Operationen
- Audit-Logging für SIEM-Zugriffe

### 6.2 Verschlüsselung

**In Transit:**
- TLS 1.2+ für Log-Übertragung
- Mutual TLS für kritische Systeme

**At Rest:**
- Verschlüsselung des SIEM-Storage (AES-256)
- Verschlüsselung von Archiv-Logs

### 6.3 Integritätsschutz

**Methoden:**
- Kryptographische Signaturen (HMAC)
- Write-Once-Read-Many (WORM) Storage
- Blockchain-basierte Log-Integrität (optional)

**Monitoring:**
- Regelmäßige Integritätsprüfungen
- Alerts bei Manipulationsversuchen

## 7. Monitoring und Alerting

### 7.1 Log-Health-Monitoring

**Überwachte Metriken:**
- Log-Ingestion-Rate (Logs pro Sekunde)
- Log-Latenz (Zeit bis Log in SIEM)
- Fehlende Log-Quellen
- SIEM-Storage-Kapazität

**Alerts:**
- Log-Quelle sendet keine Logs (> 15 Minuten)
- Ungewöhnlich hohe Log-Rate (möglicher Angriff oder Fehler)
- SIEM-Storage > 80% voll

### 7.2 Security-Monitoring

**24/7 Security Operations Center (SOC):**
- Monitoring aller SIEM-Alerts
- Triage und Incident Response
- Eskalation bei kritischen Incidents

**Automatisierung:**
- SOAR (Security Orchestration, Automation and Response)
- Automatische Playbooks für häufige Incidents
- Integration mit Ticketsystem

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Log-Quellen-Verfügbarkeit | > 99% |
| SIEM-Alert-Response-Zeit (Critical) | < 15 Minuten |
| False-Positive-Rate | < 10% |
| Log-Retention-Compliance | 100% |

### 8.2 Audit-Nachweise

- SIEM-Konfiguration und Use Cases
- Log-Retention-Berichte
- Incident-Response-Dokumentation
- Zugriffsprotokolle auf SIEM

## 9. Referenzen

### Interne Dokumente
- `0320_Policy_Logging_und_Monitoring.md`
- `0400_Policy_Incident_Management.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.15** - Logging
- **ISO/IEC 27001:2022 Annex A.8.16** - Monitoring activities
- **NIST SP 800-92** - Guide to Computer Security Log Management

**Genehmigt durch:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

