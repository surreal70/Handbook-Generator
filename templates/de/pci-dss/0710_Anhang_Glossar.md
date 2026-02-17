# Anhang: Glossar und Abkürzungen

**Dokument-ID:** PCI-0710
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template provides a glossary of PCI-DSS terms and abbreviations.
It helps ensure consistent understanding of terminology.

Customization required:
- Add organization-specific terms
- Include local terminology
- Update as needed
-->

## 1. Zweck

Dieses Dokument definiert alle Begriffe und Abkürzungen, die in der PCI-DSS-Dokumentation von {{ meta-organisation.name }} verwendet werden.

## 2. PCI-DSS-Begriffe

### A

**Acquiring Bank (Acquirer)**
- Bank, die Zahlungskarten-Transaktionen für Händler verarbeitet
- Verantwortlich für PCI-DSS-Compliance des Händlers

**AOC (Attestation of Compliance)**
- Bestätigung der PCI-DSS-Compliance
- Ausgestellt von QSA oder durch Self-Assessment

**ASV (Approved Scanning Vendor)**
- Von PCI SSC zugelassener Anbieter für Vulnerability Scans
- Führt quartalsweise externe Scans durch

**Authentication**
- Prozess der Identitätsverifizierung
- Typischerweise durch Passwort, Token oder Biometrie

**Authorization**
- Prozess der Berechtigungsprüfung
- Bestimmt, welche Aktionen ein Benutzer durchführen darf

### C

**Cardholder Data (CHD)**
- Karteninhaberdaten
- Umfasst PAN, Karteninhabername, Ablaufdatum, Service Code

**Cardholder Data Environment (CDE)**
- Umgebung, die Karteninhaberdaten speichert, verarbeitet oder überträgt
- Umfasst Systeme, Netzwerke, Personen und Prozesse

**CDE Segmentation**
- Netzwerksegmentierung zur Isolation des CDE
- Reduziert Compliance-Scope

**CVV/CVC/CVV2/CVC2**
- Card Verification Value/Code
- 3-4-stelliger Sicherheitscode
- Darf NICHT nach Autorisierung gespeichert werden

### D

**Data Retention**
- Datenspeicherungsrichtlinie
- Definiert, wie lange Daten gespeichert werden dürfen

**Default Account**
- Herstellerseitig vorkonfigurierter Account
- Muss deaktiviert oder Passwort geändert werden

**DMZ (Demilitarized Zone)**
- Netzwerksegment zwischen Internet und internem Netzwerk
- Für öffentlich zugängliche Dienste

### E

**Encryption**
- Verschlüsselung von Daten
- Erforderlich für gespeicherte und übertragene CHD

**Encryption Key**
- Schlüssel zur Ver- und Entschlüsselung
- Muss sicher gespeichert und verwaltet werden

### F

**FIM (File Integrity Monitoring)**
- Dateiintegritätsüberwachung
- Erkennt unbefugte Änderungen an kritischen Dateien

**Firewall**
- Netzwerksicherheitsgerät
- Kontrolliert Datenverkehr zwischen Netzwerksegmenten

### H

**Hashing**
- Einweg-Verschlüsselung
- Für Passwort-Speicherung

**Hardening**
- Härtung von Systemen
- Entfernung unnötiger Dienste und Funktionen

### I

**IDS/IPS (Intrusion Detection/Prevention System)**
- System zur Erkennung und Verhinderung von Angriffen
- Erforderlich an allen CDE-Grenzen

**Incident Response**
- Reaktion auf Sicherheitsvorfälle
- Strukturierter Prozess zur Behandlung von Incidents

### K

**Key Management**
- Verwaltung kryptografischer Schlüssel
- Umfasst Generierung, Speicherung, Rotation, Vernichtung

### L

**Least Privilege**
- Prinzip der minimalen Berechtigungen
- Benutzer erhalten nur erforderliche Zugriffsrechte

**Logging**
- Protokollierung von Ereignissen
- Erforderlich für alle Zugriffe auf CDE und CHD

### M

**Malware**
- Schadsoftware
- Viren, Trojaner, Ransomware, etc.

**Merchant**
- Händler, der Zahlungskarten akzeptiert
- Unterliegt PCI-DSS-Compliance

**MFA (Multi-Factor Authentication)**
- Mehr-Faktor-Authentifizierung
- Erforderlich für CDE-Zugriffe

### N

**Need-to-Know**
- Prinzip des berechtigten Wissens
- Zugriff nur bei geschäftlicher Notwendigkeit

**Network Segmentation**
- Netzwerksegmentierung
- Trennung von CDE und Corporate-Netzwerk

**NTP (Network Time Protocol)**
- Protokoll zur Zeitsynchronisation
- Erforderlich für korrekte Zeitstempel in Logs

### P

**PA-DSS (Payment Application Data Security Standard)**
- Sicherheitsstandard für Zahlungsanwendungen
- Ergänzt PCI-DSS

**PAN (Primary Account Number)**
- Primäre Kontonummer
- 13-19-stellige Kartennummer
- Kernstück der Karteninhaberdaten

**Penetration Test**
- Sicherheitstest durch simulierte Angriffe
- Jährlich erforderlich

**PCI DSS (Payment Card Industry Data Security Standard)**
- Sicherheitsstandard für Zahlungskartenindustrie
- Definiert Anforderungen zum Schutz von Karteninhaberdaten

**PCI SSC (Payment Card Industry Security Standards Council)**
- Organisation, die PCI-DSS entwickelt und verwaltet

**POS (Point of Sale)**
- Verkaufsstelle
- Terminal zur Karteneingabe

### Q

**QSA (Qualified Security Assessor)**
- Qualifizierter Sicherheitsprüfer
- Führt PCI-DSS-Assessments durch

### R

**RBAC (Role-Based Access Control)**
- Rollenbasierte Zugriffskontrolle
- Berechtigungen basierend auf Rollen

**Risk Assessment**
- Risikoanalyse
- Jährlich erforderlich

**ROC (Report on Compliance)**
- Compliance-Bericht
- Erstellt von QSA nach Assessment

### S

**SAD (Sensitive Authentication Data)**
- Sensitive Authentifizierungsdaten
- Full Track Data, CVV, PIN
- Darf NICHT nach Autorisierung gespeichert werden

**SAQ (Self-Assessment Questionnaire)**
- Selbstbewertungsfragebogen
- Für kleinere Händler ohne QSA-Assessment

**Scope**
- Geltungsbereich der PCI-DSS-Compliance
- Alle Systeme, die CHD speichern, verarbeiten oder übertragen

**Segmentation**
- Siehe Network Segmentation

**Service Provider**
- Dienstleister, der CHD im Auftrag verarbeitet
- Unterliegt PCI-DSS-Compliance

**SIEM (Security Information and Event Management)**
- System zur zentralen Log-Verwaltung und -Analyse

**Strong Cryptography**
- Starke Verschlüsselung
- Mindestens AES-128, RSA-2048

### T

**Tokenization**
- Ersetzung von PAN durch Token
- Reduziert Compliance-Scope

**TLS (Transport Layer Security)**
- Verschlüsselungsprotokoll für Datenübertragung
- Mindestens TLS 1.2 erforderlich

**Track Data**
- Magnetstreifendaten
- Track 1 und Track 2
- Darf NICHT nach Autorisierung gespeichert werden

### V

**Vulnerability**
- Schwachstelle in System oder Anwendung
- Muss identifiziert und behoben werden

**Vulnerability Scan**
- Schwachstellen-Scan
- Quartalsweise erforderlich (extern und intern)

### W

**WAF (Web Application Firewall)**
- Firewall für Webanwendungen
- Schutz vor OWASP Top 10

**WORM (Write Once Read Many)**
- Speicher, der nur einmal beschrieben werden kann
- Für Log-Speicherung zur Integritätssicherung

## 3. Abkürzungen

| Abkürzung | Bedeutung |
|-----------|-----------|
| ACL | Access Control List |
| AES | Advanced Encryption Standard |
| AOC | Attestation of Compliance |
| API | Application Programming Interface |
| ASV | Approved Scanning Vendor |
| AV | Antivirus |
| BAA | Business Associate Agreement |
| CA | Certificate Authority |
| CDE | Cardholder Data Environment |
| CHD | Cardholder Data |
| CISO | Chief Information Security Officer |
| CRL | Certificate Revocation List |
| CVV | Card Verification Value |
| CVSS | Common Vulnerability Scoring System |
| DAST | Dynamic Application Security Testing |
| DBA | Database Administrator |
| DMZ | Demilitarized Zone |
| DPA | Data Processing Agreement |
| DSGVO | Datenschutz-Grundverordnung (GDPR) |
| EAL | Evaluation Assurance Level |
| EDR | Endpoint Detection and Response |
| FIM | File Integrity Monitoring |
| GDPR | General Data Protection Regulation |
| HIDS | Host-based Intrusion Detection System |
| HTTPS | Hypertext Transfer Protocol Secure |
| IAM | Identity and Access Management |
| IDS | Intrusion Detection System |
| IPS | Intrusion Prevention System |
| ISO | International Organization for Standardization |
| JIT | Just-in-Time |
| KPI | Key Performance Indicator |
| LDAP | Lightweight Directory Access Protocol |
| MAC | Media Access Control |
| MDM | Mobile Device Management |
| MFA | Multi-Factor Authentication |
| NIDS | Network-based Intrusion Detection System |
| NIST | National Institute of Standards and Technology |
| NTP | Network Time Protocol |
| OCSP | Online Certificate Status Protocol |
| OS | Operating System |
| OWASP | Open Web Application Security Project |
| PA-DSS | Payment Application Data Security Standard |
| PAM | Privileged Access Management |
| PAN | Primary Account Number |
| PCI DSS | Payment Card Industry Data Security Standard |
| PCI SSC | Payment Card Industry Security Standards Council |
| PIN | Personal Identification Number |
| PKI | Public Key Infrastructure |
| POA&M | Plan of Action and Milestones |
| POS | Point of Sale |
| QSA | Qualified Security Assessor |
| RACI | Responsible, Accountable, Consulted, Informed |
| RBAC | Role-Based Access Control |
| RFC | Request for Comments |
| ROC | Report on Compliance |
| RPO | Recovery Point Objective |
| RSA | Rivest-Shamir-Adleman (Verschlüsselungsalgorithmus) |
| RTO | Recovery Time Objective |
| SAD | Sensitive Authentication Data |
| SAQ | Self-Assessment Questionnaire |
| SAST | Static Application Security Testing |
| SDLC | Software Development Lifecycle |
| SIEM | Security Information and Event Management |
| SOC | Security Operations Center |
| SQL | Structured Query Language |
| SSH | Secure Shell |
| SSL | Secure Sockets Layer (veraltet, durch TLS ersetzt) |
| SSO | Single Sign-On |
| TLS | Transport Layer Security |
| TOE | Target of Evaluation |
| UTC | Coordinated Universal Time |
| VLAN | Virtual Local Area Network |
| VPN | Virtual Private Network |
| WAF | Web Application Firewall |
| WORM | Write Once Read Many |

## 4. Organisationsspezifische Begriffe

[TODO: Fügen Sie hier organisationsspezifische Begriffe und Abkürzungen hinzu]

| Begriff/Abkürzung | Bedeutung |
|-------------------|-----------|
| [TODO] | [TODO] |

<!-- End of template -->
