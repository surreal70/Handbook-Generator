# PCI-DSS Compliance Handbuch-Templates (Deutsch)

## Übersicht

Diese Templates bilden die Grundlage für ein vollständiges PCI-DSS (Payment Card Industry Data Security Standard) Compliance-Handbuch nach **PCI-DSS v4.0**.

Das PCI-DSS Handbuch der {{ meta.organization.name }} umfasst strukturierte Dokumente, die alle 12 PCI-DSS-Anforderungen abdecken und die Sicherheit von Karteninhaberdaten gewährleisten.

## Template-Struktur

### Foundation (Grundlagen, 0010-0050)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0010 | Geltungsbereich und CDE-Definition | Definition des Cardholder Data Environment (CDE) und Scope |
| PCI-0020 | Netzwerksegmentierung | Dokumentation der Netzwerksegmentierung und Isolation des CDE |
| PCI-0030 | Rollen und Verantwortlichkeiten | PCI-DSS-spezifische Rollen und RACI-Matrizen |
| PCI-0040 | Datenfluss-Diagramme | Visualisierung der Karteninhaberdaten-Flüsse |
| PCI-0050 | Compliance-Programm | PCI-DSS Compliance-Management und Governance |

### Build and Maintain Secure Network (Anforderungen 1-2, 0100-0150)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0100 | Firewall-Konfiguration | Firewall- und Router-Konfigurationsstandards (Req 1) |
| PCI-0110 | Netzwerk-Zugriffskontrolle | Zugriffskontrolle auf Netzwerkebene |
| PCI-0120 | Systemhärtung | Sichere Konfiguration von Systemen (Req 2) |
| PCI-0130 | Vendor Defaults | Änderung von Herstellerstandards |
| PCI-0140 | Wireless Security | Sicherheit drahtloser Netzwerke |

### Protect Cardholder Data (Anforderungen 3-4, 0200-0250)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0200 | Datenspeicherung | Schutz gespeicherter Karteninhaberdaten (Req 3) |
| PCI-0210 | Verschlüsselung | Verschlüsselungsstandards und Key Management |
| PCI-0220 | Datenübertragung | Schutz bei Übertragung über öffentliche Netzwerke (Req 4) |
| PCI-0230 | Datenaufbewahrung | Aufbewahrungsfristen und sichere Löschung |
| PCI-0240 | Maskierung und Tokenisierung | PAN-Maskierung und Tokenisierungsverfahren |

### Maintain Vulnerability Management (Anforderungen 5-6, 0300-0350)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0300 | Malware-Schutz | Anti-Malware-Programme und -Prozesse (Req 5) |
| PCI-0310 | Patch Management | Sicherheitspatches und Updates (Req 6) |
| PCI-0320 | Secure Development | Sichere Softwareentwicklung |
| PCI-0330 | Vulnerability Scanning | Quartalsweise Schwachstellenscans |
| PCI-0340 | Penetration Testing | Jährliche Penetrationstests |

### Implement Strong Access Control (Anforderungen 7-9, 0400-0450)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0400 | Zugriffskontrolle | Need-to-know-Prinzip (Req 7) |
| PCI-0410 | Authentifizierung | Benutzeridentifikation und Authentifizierung (Req 8) |
| PCI-0420 | Multi-Faktor-Authentifizierung | MFA für CDE-Zugriff |
| PCI-0430 | Physische Sicherheit | Physischer Zugang zum CDE (Req 9) |
| PCI-0440 | Medienhandhabung | Sichere Handhabung physischer Medien |

### Monitor and Test Networks (Anforderungen 10-11, 0500-0550)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0500 | Logging und Monitoring | Protokollierung aller Zugriffe (Req 10) |
| PCI-0510 | Log-Überprüfung | Tägliche Log-Überprüfung |
| PCI-0520 | Sicherheitstests | Regelmäßige Sicherheitstests (Req 11) |
| PCI-0530 | Intrusion Detection | IDS/IPS-Systeme |
| PCI-0540 | File Integrity Monitoring | Überwachung kritischer Dateien |

### Maintain Information Security Policy (Anforderung 12, 0600-0650)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0600 | Sicherheitsrichtlinie | Informationssicherheitsrichtlinie (Req 12) |
| PCI-0610 | Risikobewertung | Jährliche Risikobewertung |
| PCI-0620 | Schulungsprogramm | Security Awareness Training |
| PCI-0630 | Incident Response | Incident-Response-Plan |
| PCI-0640 | Dienstleister-Management | Management von Dienstleistern |

### Appendices (Anhänge, 0700-0750)

| Dokument-ID | Titel | Beschreibung |
|-------------|-------|--------------|
| PCI-0700 | Compliance-Nachweise | Dokumentation für Audits |
| PCI-0710 | Scan-Berichte | Quartalsweise Vulnerability-Scan-Berichte |
| PCI-0720 | Penetrationstest-Berichte | Jährliche Penetrationstest-Dokumentation |
| PCI-0730 | Checklisten | PCI-DSS Self-Assessment Questionnaire (SAQ) |
| PCI-0740 | Glossar | PCI-DSS-spezifische Begriffe und Abkürzungen |

## Platzhalter-Verwendung

### Meta-Platzhalter (Organisationsdaten)

Die Templates verwenden Platzhalter aus der `metadata.yaml` Datei:

```markdown
**Organisation:** {{ meta.organization.name }}
**QSA:** {{ meta.roles.qsa.name }} ({{ meta.roles.qsa.email }})
**CISO:** {{ meta.roles.ciso.name }} ({{ meta.roles.ciso.email }})
**Merchant ID:** {{ meta.pci.merchant_id }}
**Service Provider ID:** {{ meta.pci.service_provider_id }}
```

### [TODO]-Markierungen

Alle Templates enthalten `[TODO]`-Markierungen für organisationsspezifische Anpassungen:

```markdown
**CDE-Systeme:** [TODO: Liste der Systeme im CDE]
**Verschlüsselungsalgorithmus:** [TODO: AES-256]
**Scan-Vendor:** [TODO: Approved Scanning Vendor Name]
```

## PCI-DSS v4.0 Compliance-Mapping

| PCI-DSS Anforderung | PCI-Dokument | Beschreibung |
|---------------------|--------------|--------------|
| Req 1: Firewall Configuration | PCI-0100, PCI-0110 | Firewall- und Netzwerksicherheit |
| Req 2: Secure Configuration | PCI-0120, PCI-0130, PCI-0140 | Systemhärtung |
| Req 3: Protect Stored Data | PCI-0200, PCI-0210, PCI-0230 | Datenspeicherung |
| Req 4: Encrypt Transmission | PCI-0220 | Datenübertragung |
| Req 5: Protect Against Malware | PCI-0300 | Malware-Schutz |
| Req 6: Secure Systems | PCI-0310, PCI-0320 | Patch Management |
| Req 7: Restrict Access | PCI-0400 | Zugriffskontrolle |
| Req 8: Identify Users | PCI-0410, PCI-0420 | Authentifizierung |
| Req 9: Physical Access | PCI-0430, PCI-0440 | Physische Sicherheit |
| Req 10: Log and Monitor | PCI-0500, PCI-0510 | Logging |
| Req 11: Test Security | PCI-0520, PCI-0530, PCI-0540 | Sicherheitstests |
| Req 12: Security Policy | PCI-0600-PCI-0640 | Richtlinien |

## Wichtige PCI-DSS-Konzepte

### Cardholder Data Environment (CDE)

Das CDE umfasst:
- **Systeme:** Alle Systeme, die Karteninhaberdaten speichern, verarbeiten oder übertragen
- **Netzwerke:** Netzwerksegmente, die mit CDE-Systemen verbunden sind
- **Personen:** Mitarbeiter mit Zugriff auf Karteninhaberdaten

### Karteninhaberdaten (CHD)

- **Primary Account Number (PAN):** 13-19-stellige Kartennummer
- **Cardholder Name:** Name des Karteninhabers
- **Service Code:** 3-stelliger Code
- **Expiration Date:** Ablaufdatum

### Sensitive Authentication Data (SAD)

**Darf NICHT nach Autorisierung gespeichert werden:**
- **Full Track Data:** Magnetstreifendaten
- **CAV2/CVC2/CVV2/CID:** Kartenprüfnummer
- **PIN/PIN Block:** PIN-Daten

### Merchant Levels

- **Level 1:** > 6 Millionen Transaktionen/Jahr
- **Level 2:** 1-6 Millionen Transaktionen/Jahr
- **Level 3:** 20.000-1 Million E-Commerce-Transaktionen/Jahr
- **Level 4:** < 20.000 E-Commerce-Transaktionen/Jahr oder < 1 Million Transaktionen/Jahr

## Best Practices für PCI-DSS-Compliance

### 1. Scope Reduction

- **Netzwerksegmentierung:** CDE vom restlichen Netzwerk isolieren
- **Tokenisierung:** PAN durch Token ersetzen
- **Point-to-Point-Verschlüsselung (P2PE):** Verschlüsselung am Point of Sale
- **Outsourcing:** Nutzung PCI-DSS-zertifizierter Service Provider

### 2. Quartalsweise Aktivitäten

- **Vulnerability Scans:** Durch Approved Scanning Vendor (ASV)
- **Log-Überprüfung:** Tägliche Überprüfung kritischer Logs
- **Firewall-Regelüberprüfung:** Quartalsweise Review

### 3. Jährliche Aktivitäten

- **Penetrationstests:** Durch qualifizierte Tester
- **Risikobewertung:** Formale Risikobewertung
- **Security Awareness Training:** Für alle Mitarbeiter
- **Richtlinienüberprüfung:** Review aller Sicherheitsrichtlinien

### 4. Dokumentation

- **Netzwerkdiagramme:** Aktuell halten
- **Datenflussdiagramme:** Alle CHD-Flüsse dokumentieren
- **System-Inventar:** Alle CDE-Systeme erfassen
- **Änderungsprotokolle:** Alle Änderungen dokumentieren

## Generierung des Handbuchs

### CLI-Verwendung

```bash
# Deutsches PCI-DSS-Handbuch generieren
python -m src.cli --language de --template pci-dss --test

# Englisches PCI-DSS-Handbuch generieren
python -m src.cli --language en --template pci-dss --test

# PDF mit Inhaltsverzeichnis generieren
python -m src.cli --language de --template pci-dss --output pdf --test --pdf-toc

# Alle Formate generieren
python -m src.cli --language de --template pci-dss --output all --test --separate-files --pdf-toc
```

## Wartung und Aktualisierung

### Aktualisierungsintervalle

- **Jährlich:** Vollständige Überprüfung vor Re-Assessment
- **Quartalsweise:** Scan-Berichte und Log-Reviews
- **Ad-hoc:** Bei Änderungen am CDE oder nach Incidents

### Versionierung

- **MAJOR:** Neue PCI-DSS-Version (z.B. v4.0 → v5.0)
- **MINOR:** Ergänzungen und Aktualisierungen
- **PATCH:** Korrekturen und redaktionelle Änderungen

## Support und Feedback

Bei Fragen oder Problemen:

- **Dokumentation:** Siehe Haupt-README.md
- **PCI SSC:** https://www.pcisecuritystandards.org/
- **Issues:** GitHub Issues für Fehlerberichte

---

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2026-02-06  
**Maintainer:** PCI-DSS-Template-Team
