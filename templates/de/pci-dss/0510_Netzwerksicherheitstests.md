# Netzwerksicherheitstests

**Dokument-ID:** PCI-0510
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents network security testing requirements.
It aligns with PCI-DSS v4.0 Requirement 11 (Test Security of Systems and Networks Regularly).

Customization required:
- Define vulnerability scanning procedures
- Document penetration testing requirements
- Include IDS/IPS configuration
- Define file integrity monitoring
-->

## 1. Zweck

Dieses Dokument definiert die Netzwerksicherheitstests für {{ meta-organisation.name }} gemäß PCI-DSS Requirement 11.

### 1.1 Ziele

- **Schwachstellen-Identifikation:** Regelmäßige Vulnerability Scans
- **Penetrationstests:** Jährliche Sicherheitstests
- **Intrusion Detection:** IDS/IPS-Implementierung
- **Compliance:** Erfüllung von PCI-DSS Requirement 11

### 1.2 Geltungsbereich

**Betroffene Systeme:**
- Alle CDE-Systeme
- Perimeter-Systeme
- Interne Netzwerke
- Webanwendungen

## 2. Vulnerability Scanning

### 2.1 Quartalsweise Scans

**Anforderungen:**
- Quartalsweise externe Scans durch ASV
- Quartalsweise interne Scans
- Nach signifikanten Änderungen
- Alle Systeme im CDE

**ASV (Approved Scanning Vendor):**
- Name: [TODO: ASV-Name]
- Kontakt: [TODO: Kontakt]
- Letzte Scan: [TODO: Datum]
- Nächste Scan: [TODO: Datum]

### 2.2 Externe Vulnerability Scans

**Prozess:**
1. ASV-Scan beauftragen
2. Scan durchführen lassen
3. Ergebnisse analysieren
4. Schwachstellen beheben
5. Re-Scan durchführen
6. Passing Scan erreichen
7. ASV-Bericht archivieren

**Passing Scan-Kriterien:**
- Keine Schwachstellen mit CVSS ≥ 4.0
- Alle kritischen Schwachstellen behoben
- ASV-Bestätigung

### 2.3 Interne Vulnerability Scans

**Prozess:**
- Quartalsweise Scans aller internen Systeme
- Authentifizierte Scans (mit Credentials)
- Vollständige Netzwerk-Scans
- Schwachstellen-Priorisierung
- Remediation-Plan

**Scan-Tool:** [TODO: Name des Scan-Tools]

**Scan-Umfang:**
- Alle CDE-Systeme
- Alle Systeme mit CHD-Zugriff
- Netzwerkkomponenten
- Datenbanken
- Webanwendungen

### 2.4 Schwachstellen-Management

**Priorisierung:**

| CVSS-Score | Schweregrad | Remediation-Frist |
|------------|-------------|-------------------|
| 9.0 - 10.0 | Kritisch | 7 Tage |
| 7.0 - 8.9 | Hoch | 30 Tage |
| 4.0 - 6.9 | Mittel | 90 Tage |
| 0.1 - 3.9 | Niedrig | 180 Tage |

**Remediation-Prozess:**
1. Schwachstelle identifiziert
2. Risikobewertung
3. Remediation-Plan erstellen
4. Patch/Fix implementieren
5. Validierung
6. Dokumentation

## 3. Penetrationstests

### 3.1 Jährliche Penetrationstests

**Anforderungen:**
- Jährlich durch qualifizierte Tester
- Nach signifikanten Änderungen
- Externe und interne Tests
- Netzwerk- und Anwendungs-Tests

**Penetrationstest-Firma:**
- Name: [TODO: Firma]
- Kontakt: [TODO: Kontakt]
- Letzter Test: [TODO: Datum]
- Nächster Test: [TODO: Datum]

### 3.2 Externe Penetrationstests

**Umfang:**
- Perimeter-Systeme
- Öffentlich zugängliche Webanwendungen
- VPN-Zugänge
- E-Mail-Systeme

**Methodik:**
- Black-Box-Testing
- Exploitation von Schwachstellen
- Social Engineering (optional)
- Dokumentation aller Findings

### 3.3 Interne Penetrationstests

**Umfang:**
- CDE-Netzwerk
- Interne Anwendungen
- Lateral Movement-Tests
- Privilegien-Eskalation

**Methodik:**
- Gray-Box-Testing
- Authentifizierte Tests
- Exploitation
- Post-Exploitation

### 3.4 Segmentierungstests

**Anforderungen:**
- Validierung der Netzwerksegmentierung
- Versuche, CDE-Grenzen zu überschreiten
- Firewall-Regel-Validierung
- Dokumentation der Ergebnisse

**Prozess:**
1. Segmentierung dokumentieren
2. Test-Szenarien definieren
3. Penetrationstest durchführen
4. Ergebnisse analysieren
5. Schwachstellen beheben
6. Re-Test
7. Dokumentation

## 4. Intrusion Detection/Prevention

### 4.1 IDS/IPS-Implementierung

**Anforderungen:**
- IDS/IPS an allen CDE-Grenzen
- Echtzeitüberwachung
- Automatische Alerts
- Regelmäßige Signatur-Updates

**IDS/IPS-Systeme:**

| System | Typ | Standort | Funktion |
|--------|-----|----------|----------|
| [TODO: IDS-01] | Network IDS | Perimeter | Erkennung |
| [TODO: IPS-01] | Network IPS | CDE-Grenze | Prävention |
| [TODO: HIDS-01] | Host IDS | CDE-Server | Erkennung |

### 4.2 IDS/IPS-Signaturen

**Anforderungen:**
- Aktuelle Signaturen
- Tägliche Updates
- Custom Signaturen für bekannte Bedrohungen
- Regelmäßige Überprüfung

**Update-Prozess:**
1. Signatur-Updates herunterladen
2. In Testumgebung testen
3. In Produktion deployen
4. Validierung
5. Dokumentation

### 4.3 IDS/IPS-Alerting

**Alert-Kategorien:**
- Kritisch: Sofortige Aktion erforderlich
- Hoch: Untersuchung innerhalb 1 Stunde
- Mittel: Untersuchung innerhalb 4 Stunden
- Niedrig: Review innerhalb 24 Stunden

**Alert-Response:**
- Automatische Benachrichtigung an SOC
- Initiale Untersuchung
- Eskalation bei Bedarf
- Incident Response
- Dokumentation

## 5. File Integrity Monitoring (FIM)

### 5.1 FIM-Implementierung

**Anforderungen:**
- FIM auf allen CDE-Systemen
- Überwachung kritischer Dateien
- Echtzeitüberwachung
- Automatische Alerts

**FIM-Tool:** [TODO: Name des FIM-Tools]

### 5.2 Überwachte Dateien

**Kritische Dateien:**
- Systemdateien
- Konfigurationsdateien
- Anwendungsdateien
- Logdateien
- Datenbank-Dateien

**Beispiele:**
- `/etc/passwd`, `/etc/shadow` (Linux)
- `C:\Windows\System32\config\SAM` (Windows)
- Firewall-Konfigurationen
- Webserver-Konfigurationen
- Datenbank-Konfigurationen

### 5.3 FIM-Alerting

**Alerts bei:**
- Dateiänderungen
- Dateilöschungen
- Neue Dateien
- Berechtigungsänderungen
- Eigentümeränderungen

**Alert-Response:**
1. Alert empfangen
2. Änderung validieren
3. Autorisierte Änderung? (Change Request)
4. Falls nicht autorisiert: Incident Response
5. Dokumentation

## 6. Change Detection

### 6.1 Change Detection-Mechanismen

**Anforderungen:**
- Automatische Erkennung von Änderungen
- Vergleich mit Baseline
- Alerting bei unautorisierten Änderungen
- Dokumentation aller Änderungen

**Überwachte Änderungen:**
- Konfigurationsänderungen
- Software-Installationen
- Patch-Installationen
- Benutzer-Änderungen
- Berechtigungsänderungen

### 6.2 Baseline-Management

**Prozess:**
1. Initiale Baseline erstellen
2. Baseline dokumentieren
3. Regelmäßige Validierung
4. Aktualisierung nach genehmigten Änderungen
5. Dokumentation

**Baseline-Komponenten:**
- Systemkonfiguration
- Installierte Software
- Netzwerkkonfiguration
- Benutzer und Berechtigungen
- Dienste und Prozesse

## 7. Wireless Security Testing

### 7.1 Wireless Access Point Detection

**Anforderungen:**
- Quartalsweise Scans nach Wireless APs
- Erkennung von Rogue APs
- Validierung autorisierter APs
- Dokumentation

**Scan-Methoden:**
- Wireless Scanner
- Physische Inspektionen
- Netzwerk-Scans

### 7.2 Wireless Security Standards

**Anforderungen für autorisierte WLANs:**
- WPA3 oder WPA2 mit AES
- Starke Authentifizierung (802.1X)
- Separate VLAN für WLAN
- Keine Verbindung zu CDE ohne zusätzliche Kontrollen

## 8. Web Application Security Testing

### 8.1 Anwendungssicherheitstests

**Anforderungen:**
- Jährliche Sicherheitstests
- Nach signifikanten Änderungen
- OWASP Top 10-Abdeckung
- Authentifizierte und unauthentifizierte Tests

**Test-Methoden:**
- Automatisierte Scans (DAST)
- Manuelle Penetrationstests
- Code-Reviews (SAST)
- Fuzzing

### 8.2 OWASP Top 10

**Zu testende Schwachstellen:**
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

## 9. Social Engineering Testing

### 9.1 Phishing-Simulationen

**Anforderungen:**
- Regelmäßige Phishing-Tests
- Verschiedene Szenarien
- Mitarbeiter-Sensibilisierung
- Dokumentation der Ergebnisse

**Prozess:**
1. Phishing-Kampagne planen
2. E-Mails versenden
3. Klickraten messen
4. Mitarbeiter schulen
5. Dokumentation

### 9.2 Physical Social Engineering

**Tests:**
- Tailgating-Versuche
- Badge-Cloning
- Dumpster Diving
- Pretexting

**Dokumentation:**
- Erfolgreiche Angriffe
- Schwachstellen identifizieren
- Verbesserungsmaßnahmen
- Mitarbeiter-Sensibilisierung

## 10. Compliance-Validierung

### 10.1 Validierungsaktivitäten

**Quartalsweise:**
- Vulnerability Scans (extern und intern)
- Wireless AP-Scans
- FIM-Validierung

**Jährlich:**
- Penetrationstests (extern und intern)
- Segmentierungstests
- Web Application Security Tests
- Social Engineering Tests

### 10.2 Validierungsdokumentation

**Erforderliche Nachweise:**
- ASV-Scan-Berichte (4 pro Jahr)
- Interne Scan-Berichte (4 pro Jahr)
- Penetrationstest-Berichte (1 pro Jahr)
- Segmentierungstest-Berichte
- FIM-Konfiguration und Logs
- IDS/IPS-Konfiguration und Logs

<!-- End of template -->
