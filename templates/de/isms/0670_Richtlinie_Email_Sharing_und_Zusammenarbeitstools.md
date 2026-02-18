# Richtlinie: E-Mail, Sharing und Zusammenarbeitstools

**Dokument-ID:** 0670
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

Diese Richtlinie konkretisiert die `0660_Policy_Informationsuebertragung_und_Kommunikation.md` und definiert:
- E-Mail-Sicherheit und -Nutzung
- File-Sharing und Collaboration-Tools
- Sichere Kommunikationskanäle

**Geltungsbereich:** Alle Kommunikationstools bei **{{ meta-organisation.name }}**

## 2. E-Mail-Sicherheit

### 2.1 E-Mail-System

**Plattform:** {{ meta.email.system }} (z.B. Microsoft 365, Google Workspace)

**Sicherheitsfeatures:**
- SPF, DKIM, DMARC konfiguriert
- TLS für Transport-Verschlüsselung
- Anti-Spam und Anti-Malware
- DLP (Data Loss Prevention)
- E-Mail-Archivierung

### 2.2 E-Mail-Nutzung

**Erlaubte Nutzung:**
- Geschäftliche Kommunikation
- Begrenzte private Nutzung (max. 10 E-Mails/Tag)
- Anmeldung bei geschäftlichen Online-Diensten

**Verbotene Aktivitäten:**
- Versand vertraulicher Daten ohne Verschlüsselung
- Spam, Kettenmails
- Nutzung privater E-Mail für geschäftliche Zwecke
- Automatische Weiterleitung an externe Adressen

**Details:** Siehe `0210_Richtlinie_Akzeptable_Nutzung_IT.md`

### 2.3 E-Mail-Verschlüsselung

**S/MIME:**
- Für vertrauliche E-Mails verpflichtend
- Zertifikate für alle Mitarbeiter
- Automatische Verschlüsselung bei "Vertraulich"-Label

**Opportunistic TLS:**
- Für alle ausgehenden E-Mails
- MTA-STS für bekannte Partner

**Details:** Siehe `0270_Richtlinie_Key_Management_und_Verschluesselung.md`

### 2.4 Phishing-Schutz

**Technische Kontrollen:**
- E-Mail-Gateway mit Anti-Phishing
- Link-Rewriting und Sandbox
- Attachment-Scanning
- DMARC-Enforcement

**Nutzer-Schulung:**
- Phishing-Awareness-Training (jährlich)
- Phishing-Simulationen (quartalsweise)
- Reporting-Button in E-Mail-Client

**Bei Phishing-Verdacht:**
1. E-Mail nicht öffnen/anklicken
2. Melden über Reporting-Button
3. E-Mail löschen
4. IT-Security prüft und reagiert

### 2.5 E-Mail-Archivierung

**Automatische Archivierung:**
- Alle geschäftlichen E-Mails
- Retention: {{ meta.retention.email_years }} Jahre
- Unveränderbarkeit (WORM)

**Zugriff:**
- Nutzer: Eigene E-Mails
- Legal/Compliance: Für eDiscovery
- Vorgesetzte: Mit Genehmigung

**Details:** Siehe `0590_Richtlinie_Records_Retention`

## 3. File-Sharing

### 3.1 Genehmigte Plattformen

**Intern:**
- **File-Server:** {{ netbox.device.fileserver }}
- **SharePoint/OneDrive:** {{ meta.collaboration.sharepoint }}
- **Teams/Slack:** {{ meta.collaboration.teams }}

**Extern (mit Kunden/Partnern):**
- **Secure File Transfer:** {{ meta.filesharing.secure_platform }}
- **Nur mit Verschlüsselung und Passwortschutz**

**Verboten:**
- Private Cloud-Dienste (Dropbox privat, Google Drive privat)
- WeTransfer, Filemail (ohne Genehmigung)
- USB-Sticks für vertrauliche Daten

### 3.2 Berechtigungen

**Least Privilege:**
- Nur erforderliche Berechtigungen
- Read-Only wo möglich
- Zeitlich befristete Freigaben

**Externe Freigaben:**
- Genehmigung durch Daten-Owner
- Passwortschutz verpflichtend
- Ablaufdatum setzen (max. 90 Tage)
- Logging aller Zugriffe

### 3.3 DLP für File-Sharing

**Automatische Kontrollen:**
- Blockierung vertraulicher Daten bei externer Freigabe
- Warnung bei großen Datenmengen
- Alerts bei ungewöhnlichen Sharing-Mustern

## 4. Collaboration-Tools

### 4.1 Microsoft Teams / Slack

**Genehmigte Nutzung:**
- Interne Kommunikation
- Projekt-Collaboration
- Video-Konferenzen

**Sicherheitseinstellungen:**
- Externe Gäste nur mit Genehmigung
- DLP-Policies aktiviert
- Retention-Policies konfiguriert
- Audit-Logging aktiviert

**Verbotene Aktivitäten:**
- Sharing vertraulicher Daten in öffentlichen Channels
- Nutzung privater Accounts für geschäftliche Zwecke
- Installation nicht genehmigter Apps/Bots

### 4.2 Video-Konferenzen

**Genehmigte Plattformen:**
- **Intern:** {{ meta.collaboration.video }} (z.B. Teams, Zoom)
- **Extern:** Nur genehmigte Plattformen

**Sicherheitseinstellungen:**
- Warteraum aktiviert
- Passwortschutz für Meetings
- Keine Aufzeichnung ohne Zustimmung
- Bildschirmfreigabe nur für Moderator

**Best Practices:**
- Hintergrund-Unschärfe nutzen
- Mikrofon stumm schalten wenn nicht sprechend
- Keine vertraulichen Informationen in öffentlichen Meetings

### 4.3 Instant Messaging

**Genehmigte Tools:**
- Microsoft Teams Chat
- Slack (Enterprise)

**Verboten:**
- WhatsApp, Telegram für geschäftliche Kommunikation
- Private Messaging-Apps

**Retention:**
- Chat-Historie: {{ meta.retention.chat_years }} Jahre
- Compliance-Archivierung

## 5. Externe Kommunikation

### 5.1 Kommunikation mit Kunden

**Kanäle:**
- E-Mail (bevorzugt)
- Telefon
- Video-Konferenz
- Kundenportal (falls vorhanden)

**Vertrauliche Informationen:**
- Verschlüsselung verpflichtend
- Secure File Transfer nutzen
- Keine vertraulichen Daten per SMS/WhatsApp

### 5.2 Kommunikation mit Lieferanten

**Anforderungen:**
- NDA vor Austausch vertraulicher Informationen
- Genehmigte Kommunikationskanäle
- Dokumentation wichtiger Kommunikation

### 5.3 Social Media

**Geschäftliche Nutzung:**
- Nur autorisierte Accounts
- Social Media Guidelines befolgen
- Keine vertraulichen Informationen

**Private Nutzung:**
- Keine Vortäuschung offizieller Unternehmensmeinung
- Disclaimer bei Meinungsäußerungen
- Keine negativen Äußerungen über Unternehmen

**Details:** Siehe `0210_Richtlinie_Akzeptable_Nutzung_IT.md`

## 6. Mobile Kommunikation

### 6.1 Geschäfts-Smartphones

**Konfiguration:**
- MDM-Enrollment verpflichtend
- Verschlüsselung aktiviert
- Remote-Wipe-Fähigkeit
- Genehmigte Apps nur

**Nutzung:**
- Geschäftliche E-Mails und Kalender
- Teams/Slack
- Geschäftliche Telefonate

### 6.2 BYOD

**Anforderungen:**
- Containerisierung (Work Profile)
- Separate Apps für geschäftlich/privat
- MDM-Enrollment

**Details:** Siehe `0510_Richtlinie_MDM_BringYourOwnDevice`

## 7. Data Loss Prevention (DLP)

### 7.1 DLP-Policies

**Für E-Mail:**
- Blockierung von Kreditkartennummern
- Warnung bei "Vertraulich"-Label extern
- Blockierung großer Anhänge (> 25 MB)

**Für File-Sharing:**
- Blockierung vertraulicher Daten bei externer Freigabe
- Warnung bei Sharing mit vielen Personen

**Für Collaboration-Tools:**
- Warnung bei Posting vertraulicher Daten in öffentlichen Channels

### 7.2 DLP-Incidents

**Bei DLP-Blockierung:**
1. Nutzer erhält Warnung
2. Incident-Ticket erstellt
3. Security-Team prüft
4. Bei Bedarf: Schulung oder Disziplinarmaßnahmen

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| E-Mail-Verschlüsselung (vertraulich) | 100% |
| Phishing-Klickrate (Simulation) | < 5% |
| DLP-Incidents | < 10 pro Monat |
| Externe Freigaben mit Passwort | 100% |

### 8.2 Audit-Nachweise

- E-Mail-Archiv
- File-Sharing-Logs
- DLP-Incident-Reports
- Phishing-Simulation-Ergebnisse

## 9. Referenzen

### Interne Dokumente
- `0660_Policy_Informationsuebertragung_und_Kommunikation.md`
- `0210_Richtlinie_Akzeptable_Nutzung_IT.md`
- `0270_Richtlinie_Key_Management_und_Verschluesselung.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.14** - Information transfer
- **NIST SP 800-177** - Trustworthy Email

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

