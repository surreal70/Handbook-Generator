# PCI-DSS Framework Mapping

**Dokument-ID:** [FRAMEWORK]-9999
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

## Übersicht

Dieses Dokument bildet die Zuordnung zwischen den PCI-DSS v4.0 Anforderungen und den entsprechenden Template-Dateien in diesem Template-Set ab. Es dient als Referenz für Compliance-Audits und zur Identifikation von Abdeckungslücken.

**PCI-DSS Version:** 4.0  
**Template-Set Version:** 1.0  
**Letzte Aktualisierung:** 2026-02-06  
**Verantwortlich:** Compliance Team  

## PCI-DSS Anforderungsstruktur

PCI-DSS v4.0 ist in 12 Hauptanforderungen organisiert, die in 6 Zielbereiche gruppiert sind:

### Zielbereich 1: Build and Maintain a Secure Network and Systems
- Requirement 1: Install and Maintain Network Security Controls
- Requirement 2: Apply Secure Configurations to All System Components

### Zielbereich 2: Protect Account Data
- Requirement 3: Protect Stored Account Data
- Requirement 4: Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks

### Zielbereich 3: Maintain a Vulnerability Management Program
- Requirement 5: Protect All Systems and Networks from Malicious Software
- Requirement 6: Develop and Maintain Secure Systems and Software

### Zielbereich 4: Implement Strong Access Control Measures
- Requirement 7: Restrict Access to System Components and Cardholder Data by Business Need to Know
- Requirement 8: Identify Users and Authenticate Access to System Components
- Requirement 9: Restrict Physical Access to Cardholder Data

### Zielbereich 5: Regularly Monitor and Test Networks
- Requirement 10: Log and Monitor All Access to System Components and Cardholder Data
- Requirement 11: Test Security of Systems and Networks Regularly

### Zielbereich 6: Maintain an Information Security Policy
- Requirement 12: Support Information Security with Organizational Policies and Programs

## Template-Mapping nach PCI-DSS Anforderungen

### Foundation Templates (0010-0050)

Diese Templates bilden die Grundlage für das gesamte PCI-DSS Compliance-Programm:

| Template | Dateiname | PCI-DSS Anforderungen |
|----------|-----------|----------------------|
| 0010 | Geltungsbereich_und_CDE_Definition.md | Alle (Scope Definition) |
| 0020 | Netzwerksegmentierung.md | Req 1, Req 2 |
| 0030 | Rollen_und_Verantwortlichkeiten.md | Req 12 |
| 0040 | Datenfluss_Diagramme.md | Req 1, Req 3, Req 4 |
| 0050 | Compliance_Programm.md | Req 12 |

### Requirement 1: Install and Maintain Network Security Controls

**Ziel:** Netzwerksicherheitskontrollen installieren und warten, um Karteninhaberdaten zu schützen.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 1.1 | Prozesse und Mechanismen für Netzwerksicherheitskontrollen | 0100 | Firewall_Konfiguration.md |
| 1.2 | Netzwerksicherheitskontrollen konfigurieren | 0100 | Firewall_Konfiguration.md |
| 1.3 | Netzwerkzugriff zur und von der CDE einschränken | 0100, 0020 | Firewall_Konfiguration.md, Netzwerksegmentierung.md |
| 1.4 | Netzwerkverbindungen zwischen vertrauenswürdigen und nicht vertrauenswürdigen Netzwerken einschränken | 0100, 0020 | Firewall_Konfiguration.md, Netzwerksegmentierung.md |
| 1.5 | Risiken für die CDE durch Nutzung von Diensten, Protokollen und Ports mindern | 0100 | Firewall_Konfiguration.md |

**Abdeckung:** Vollständig  
**Hinweise:** Templates decken Firewall-Konfiguration, Netzwerksegmentierung und Zugriffskontrolle ab.

### Requirement 2: Apply Secure Configurations to All System Components

**Ziel:** Sichere Konfigurationen auf alle Systemkomponenten anwenden.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 2.1 | Prozesse und Mechanismen für sichere Konfigurationen | - | **LÜCKE** |
| 2.2 | Sichere Konfigurationen auf alle Systemkomponenten anwenden | - | **LÜCKE** |
| 2.3 | Drahtlose Umgebungen sichern | - | **LÜCKE** |

**Abdeckung:** Teilweise (über 0100 Firewall-Konfiguration)  
**Hinweise:** **IDENTIFIZIERTE LÜCKE** - Dedizierte Templates für System-Hardening und sichere Konfigurationen fehlen.

### Requirement 3: Protect Stored Account Data

**Ziel:** Gespeicherte Kontodaten schützen.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 3.1 | Prozesse und Mechanismen für Schutz gespeicherter Kontodaten | - | **LÜCKE** |
| 3.2 | Speicherung von Kontodaten nach Autorisierung minimieren | - | **LÜCKE** |
| 3.3 | Sensitive Authentication Data (SAD) nach Autorisierung nicht speichern | - | **LÜCKE** |
| 3.4 | Zugriff auf Displays von vollständigen PAN einschränken | 0400 | Zugriffskontrolle.md |
| 3.5 | PAN unlesbar machen, wo immer gespeichert | - | **LÜCKE** |
| 3.6 | Kryptografische Schlüssel für Schutz gespeicherter Kontodaten sichern | - | **LÜCKE** |
| 3.7 | Kryptografie für Schutz gespeicherter Kontodaten verwalten | - | **LÜCKE** |

**Abdeckung:** Minimal  
**Hinweise:** **IDENTIFIZIERTE LÜCKE** - Templates für Datenverschlüsselung, Schlüsselmanagement und Datenspeicherung fehlen.

### Requirement 4: Protect Cardholder Data with Strong Cryptography During Transmission

**Ziel:** Karteninhaberdaten mit starker Kryptografie während der Übertragung schützen.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 4.1 | Prozesse und Mechanismen für Schutz von CHD bei Übertragung | - | **LÜCKE** |
| 4.2 | PAN mit starker Kryptografie bei Übertragung über offene, öffentliche Netzwerke schützen | - | **LÜCKE** |

**Abdeckung:** Keine  
**Hinweise:** **IDENTIFIZIERTE LÜCKE** - Templates für Verschlüsselung bei Übertragung fehlen.

### Requirement 5: Protect All Systems and Networks from Malicious Software

**Ziel:** Alle Systeme und Netzwerke vor bösartiger Software schützen.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 5.1 | Prozesse und Mechanismen für Schutz vor Malware | - | **LÜCKE** |
| 5.2 | Malware-Schutz auf allen Systemen implementieren | - | **LÜCKE** |
| 5.3 | Anti-Malware-Mechanismen und -Prozesse aktiv halten | - | **LÜCKE** |
| 5.4 | Anti-Phishing-Mechanismen implementieren | - | **LÜCKE** |

**Abdeckung:** Keine  
**Hinweise:** **IDENTIFIZIERTE LÜCKE** - Templates für Malware-Schutz und Anti-Phishing fehlen.

### Requirement 6: Develop and Maintain Secure Systems and Software

**Ziel:** Sichere Systeme und Software entwickeln und warten.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 6.1 | Prozesse und Mechanismen für sichere Systeme und Software | - | **LÜCKE** |
| 6.2 | Bona fide Software und Anwendungen vor Bedrohungen schützen | - | **LÜCKE** |
| 6.3 | Sicherheitslücken identifizieren und beheben | - | **LÜCKE** |
| 6.4 | Öffentlich zugängliche Webanwendungen vor Angriffen schützen | - | **LÜCKE** |
| 6.5 | Änderungen an allen Systemkomponenten sicher verwalten | - | **LÜCKE** |

**Abdeckung:** Keine  
**Hinweise:** **IDENTIFIZIERTE LÜCKE** - Templates für Secure Development, Vulnerability Management und Change Management fehlen.

### Requirement 7: Restrict Access to System Components and Cardholder Data

**Ziel:** Zugriff auf Systemkomponenten und Karteninhaberdaten nach Business Need-to-Know einschränken.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 7.1 | Prozesse und Mechanismen für Zugriffsbeschränkung | 0400 | Zugriffskontrolle.md |
| 7.2 | Zugriff auf Systemkomponenten und Daten nach Need-to-Know einrichten | 0400 | Zugriffskontrolle.md |
| 7.3 | Zugriff auf Systemkomponenten und Daten über Anwendungen und Systeme einrichten | 0400 | Zugriffskontrolle.md |

**Abdeckung:** Vollständig  
**Hinweise:** Template 0400 deckt RBAC, Least Privilege, Need-to-Know und Zugriffsverwaltung ab.

### Requirement 8: Identify Users and Authenticate Access to System Components

**Ziel:** Benutzer identifizieren und Zugriff auf Systemkomponenten authentifizieren.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 8.1 | Prozesse und Mechanismen für Benutzeridentifikation und Authentifizierung | 0410 | Benutzerauthentifizierung.md |
| 8.2 | Benutzer vor Zugriff auf Systemkomponenten identifizieren | 0410 | Benutzerauthentifizierung.md |
| 8.3 | Starke Authentifizierung für Benutzer einrichten | 0410 | Benutzerauthentifizierung.md |
| 8.4 | Multi-Faktor-Authentifizierung (MFA) implementieren | 0410 | Benutzerauthentifizierung.md |
| 8.5 | MFA-Systeme vor Missbrauch schützen | 0410 | Benutzerauthentifizierung.md |
| 8.6 | Verwendung von Anwendungs- und System-Accounts verwalten | 0410 | Benutzerauthentifizierung.md |

**Abdeckung:** Vollständig  
**Hinweise:** Template 0410 deckt Authentifizierung, MFA, Passwortrichtlinien und Account-Management ab.

### Requirement 9: Restrict Physical Access to Cardholder Data

**Ziel:** Physischen Zugriff auf Karteninhaberdaten einschränken.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 9.1 | Prozesse und Mechanismen für physische Zugriffsbeschränkung | 0420 | Physische_Sicherheit.md |
| 9.2 | Physischen Zugriff auf CDE einschränken | 0420 | Physische_Sicherheit.md |
| 9.3 | Physischen Zugriff für Personal und Besucher kontrollieren | 0420 | Physische_Sicherheit.md |
| 9.4 | Medien mit Karteninhaberdaten sichern | 0420 | Physische_Sicherheit.md |
| 9.5 | Point-of-Interaction (POI)-Geräte vor Manipulation schützen | 0420 | Physische_Sicherheit.md |

**Abdeckung:** Vollständig  
**Hinweise:** Template 0420 deckt physische Zugangskontrollen, Besuchermanagement und Mediensicherheit ab.

### Requirement 10: Log and Monitor All Access to System Components and Cardholder Data

**Ziel:** Alle Zugriffe auf Systemkomponenten und Karteninhaberdaten loggen und überwachen.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 10.1 | Prozesse und Mechanismen für Logging und Monitoring | 0500 | Logging_und_Monitoring.md |
| 10.2 | Audit Logs implementieren, um Benutzeraktivitäten zu rekonstruieren | 0500 | Logging_und_Monitoring.md |
| 10.3 | Audit Logs vor Zerstörung und unbefugten Änderungen schützen | 0500 | Logging_und_Monitoring.md |
| 10.4 | Audit Logs überprüfen, um Anomalien oder verdächtige Aktivitäten zu identifizieren | 0500 | Logging_und_Monitoring.md |
| 10.5 | Audit Log-Historie aufbewahren | 0500 | Logging_und_Monitoring.md |
| 10.6 | Sicherheitslücken und Anomalien durch Sicherheitsüberwachung erkennen und darauf reagieren | 0500 | Logging_und_Monitoring.md |
| 10.7 | Fehler in Sicherheitssystemen rechtzeitig erkennen, melden und darauf reagieren | 0500 | Logging_und_Monitoring.md |

**Abdeckung:** Vollständig  
**Hinweise:** Template 0500 deckt Logging-Anforderungen, SIEM, Log-Retention, Monitoring und Alerting ab.

### Requirement 11: Test Security of Systems and Networks Regularly

**Ziel:** Sicherheit von Systemen und Netzwerken regelmäßig testen.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 11.1 | Prozesse und Mechanismen für regelmäßige Sicherheitstests | 0510 | Netzwerksicherheitstests.md |
| 11.2 | Drahtlose Zugriffspunkte identifizieren und überwachen | 0510 | Netzwerksicherheitstests.md |
| 11.3 | Externe und interne Schwachstellen identifizieren und beheben | 0510 | Netzwerksicherheitstests.md |
| 11.4 | Externe und interne Penetrationstests durchführen | 0510 | Netzwerksicherheitstests.md |
| 11.5 | Netzwerk-Intrusions und -Manipulationen erkennen und darauf reagieren | 0510 | Netzwerksicherheitstests.md |
| 11.6 | Unbefugte Änderungen an Zahlungsseiten erkennen und darauf reagieren | 0510 | Netzwerksicherheitstests.md |

**Abdeckung:** Vollständig  
**Hinweise:** Template 0510 deckt Vulnerability Scanning, Penetrationstests, IDS/IPS und Change Detection ab.

### Requirement 12: Support Information Security with Organizational Policies and Programs

**Ziel:** Informationssicherheit mit organisatorischen Richtlinien und Programmen unterstützen.

| Sub-Requirement | Beschreibung | Template | Dateiname |
|-----------------|--------------|----------|-----------|
| 12.1 | Prozesse und Mechanismen für Informationssicherheitsrichtlinien | 0600 | Informationssicherheitsrichtlinie.md |
| 12.2 | Akzeptable Nutzungsrichtlinien implementieren | 0600 | Informationssicherheitsrichtlinie.md |
| 12.3 | Risiken für Informationsressourcen bewerten und verwalten | 0600 | Informationssicherheitsrichtlinie.md |
| 12.4 | PCI-DSS-Compliance durch Risikobewertung von Dienstleistern sicherstellen | 0600 | Informationssicherheitsrichtlinie.md |
| 12.5 | PCI-DSS-Anforderungen in Geschäftsprozessen (BAU) verwalten | 0050, 0600 | Compliance_Programm.md, Informationssicherheitsrichtlinie.md |
| 12.6 | Sicherheitsbewusstsein aufrechterhalten | 0600 | Informationssicherheitsrichtlinie.md |
| 12.7 | Personal vor der Einstellung und regelmäßig überprüfen | 0600 | Informationssicherheitsrichtlinie.md |
| 12.8 | Risiko von Dienstleistern und anderen Dritten verwalten | 0600 | Informationssicherheitsrichtlinie.md |
| 12.9 | Dienstleister bestätigen PCI-DSS-Anforderungen mindestens jährlich | 0600 | Informationssicherheitsrichtlinie.md |
| 12.10 | Verdächtige und bestätigte Sicherheitsvorfälle dokumentieren und kommunizieren | 0600 | Informationssicherheitsrichtlinie.md |

**Abdeckung:** Vollständig  
**Hinweise:** Templates 0050 und 0600 decken Richtlinien, Risikomanagement, Awareness und Incident Response ab.

## Zusammenfassung der Abdeckung

### Vollständig abgedeckte Anforderungen

| Requirement | Titel | Haupttemplate(s) |
|-------------|-------|------------------|
| 1 | Network Security Controls | 0100, 0020 |
| 7 | Access Control | 0400 |
| 8 | User Authentication | 0410 |
| 9 | Physical Security | 0420 |
| 10 | Logging and Monitoring | 0500 |
| 11 | Security Testing | 0510 |
| 12 | Information Security Policy | 0600, 0050 |

**Abdeckungsrate:** 7 von 12 Anforderungen (58%)

### Identifizierte Abdeckungslücken

Die folgenden PCI-DSS Anforderungen sind **nicht vollständig** durch Templates abgedeckt:

| Requirement | Titel | Fehlende Templates | Priorität |
|-------------|-------|-------------------|-----------|
| 2 | Secure Configurations | System-Hardening, Sichere Konfigurationen, Wireless Security | **HOCH** |
| 3 | Protect Stored Account Data | Datenverschlüsselung, Schlüsselmanagement, Datenspeicherung, Data Retention | **KRITISCH** |
| 4 | Protect Data in Transit | Verschlüsselung bei Übertragung, TLS-Konfiguration | **KRITISCH** |
| 5 | Malware Protection | Anti-Malware, Anti-Phishing | **HOCH** |
| 6 | Secure Development | Secure SDLC, Vulnerability Management, Change Management, Patch Management | **HOCH** |

### Empfohlene zusätzliche Templates

Um vollständige PCI-DSS-Compliance zu erreichen, sollten folgende Templates erstellt werden:

#### Requirement 2: Secure Configurations
- **0110_System_Hardening.md** - Sichere Systemkonfigurationen und Hardening-Standards
- **0120_Wireless_Security.md** - Wireless-Netzwerksicherheit
- **0130_Default_Accounts_and_Passwords.md** - Management von Standard-Accounts und Passwörtern

#### Requirement 3: Protect Stored Account Data
- **0200_Data_Storage_and_Retention.md** - Datenspeicherung und Aufbewahrungsfristen
- **0210_Data_Encryption.md** - Verschlüsselung gespeicherter Daten
- **0220_Key_Management.md** - Kryptografisches Schlüsselmanagement
- **0230_PAN_Masking.md** - PAN-Maskierung und Anzeige-Kontrollen

#### Requirement 4: Protect Data in Transit
- **0240_Encryption_in_Transit.md** - Verschlüsselung bei Datenübertragung
- **0250_TLS_Configuration.md** - TLS/SSL-Konfiguration und -Management

#### Requirement 5: Malware Protection
- **0300_Anti_Malware.md** - Anti-Malware-Schutz und -Management
- **0310_Anti_Phishing.md** - Anti-Phishing-Maßnahmen

#### Requirement 6: Secure Development
- **0320_Secure_SDLC.md** - Secure Software Development Lifecycle
- **0330_Vulnerability_Management.md** - Schwachstellenmanagement
- **0340_Patch_Management.md** - Patch-Management-Prozess
- **0350_Change_Management.md** - Änderungsmanagement
- **0360_Web_Application_Security.md** - Webanwendungssicherheit (WAF, Code Reviews)

### Appendix Templates (0700-0750)

Die folgenden Appendix-Templates sind vorhanden:

| Template | Dateiname | Zweck |
|----------|-----------|-------|
| 0700 | Anhang_Nachweisregister.md | Dokumentation von Compliance-Nachweisen |
| 0710 | Anhang_Glossar.md | Begriffe und Definitionen |

**Empfohlene zusätzliche Appendix-Templates:**
- **0720_Anhang_Checklisten.md** - Compliance-Checklisten für alle 12 Requirements
- **0730_Anhang_Audit_Logs.md** - Beispiele für Audit-Log-Formate
- **0740_Anhang_Formulare.md** - Standardformulare (Zugriffsanträge, Change Requests, etc.)
- **0750_Anhang_Kontakte.md** - Notfallkontakte und Eskalationswege

## Nutzungshinweise

### Für Compliance-Audits

1. **Anforderungs-Mapping:** Verwenden Sie dieses Dokument, um zu identifizieren, welche Templates für jede PCI-DSS-Anforderung relevant sind.

2. **Lückenanalyse:** Überprüfen Sie die identifizierten Lücken und priorisieren Sie die Erstellung fehlender Templates.

3. **Nachweisführung:** Nutzen Sie Template 0700 (Nachweisregister), um alle Compliance-Nachweise zu dokumentieren.

4. **Audit-Vorbereitung:** Stellen Sie sicher, dass alle relevanten Templates ausgefüllt und aktuell sind.

### Für Template-Anpassung

1. **Organisationsspezifische Anpassung:** Ersetzen Sie alle `[TODO]`-Platzhalter mit organisationsspezifischen Informationen.

2. **Placeholder-Substitution:** Nutzen Sie das Placeholder-System (`{{ meta.* }}`) für automatische Dateneinfügung.

3. **Zusätzliche Abschnitte:** Fügen Sie bei Bedarf zusätzliche Abschnitte hinzu, die für Ihre Organisation relevant sind.

4. **Versionskontrolle:** Dokumentieren Sie alle Änderungen in der Dokumenthistorie am Ende jedes Templates.

### Für kontinuierliche Compliance

1. **Regelmäßige Reviews:** Überprüfen Sie Templates quartalsweise auf Aktualität.

2. **Änderungsmanagement:** Aktualisieren Sie Templates bei Änderungen in Prozessen oder Technologien.

3. **PCI-DSS-Updates:** Passen Sie Templates an, wenn neue PCI-DSS-Versionen veröffentlicht werden.

4. **Lessons Learned:** Integrieren Sie Erkenntnisse aus Audits und Incidents in die Templates.

## Referenzen

- **PCI-DSS v4.0:** [PCI Security Standards Council](https://www.pcisecuritystandards.org/)
- **PCI-DSS v4.0 Summary of Changes:** Dokumentiert Änderungen von v3.2.1 zu v4.0
- **PCI-DSS v4.0 ROC Template:** Report on Compliance Template
- **PCI-DSS v4.0 SAQ:** Self-Assessment Questionnaires

## Änderungshistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | 2026-02-06 | Compliance Team | Initiale Erstellung des Framework-Mappings |

**Hinweis:** Dieses Mapping-Dokument sollte bei jeder Änderung der Templates oder bei Veröffentlichung neuer PCI-DSS-Versionen aktualisiert werden.

