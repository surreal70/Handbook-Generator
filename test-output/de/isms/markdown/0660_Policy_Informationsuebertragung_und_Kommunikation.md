# Policy: Informationsübertragung und Kommunikation



**Dokument-ID:** 0660  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.14, A.8.24, A.8.26 (inkl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Anforderungen an die sichere Informationsübertragung und Kommunikation der **AdminSend GmbH**. Sie stellt sicher, dass Informationen während der Übertragung angemessen geschützt werden und Kommunikationskanäle sicher sind.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Kommunikationskanäle:** E-Mail, Messaging, File Sharing, Collaboration Tools
- **Daten:** Alle Informationen (insbesondere vertrauliche und personenbezogene Daten)
- **Übertragungswege:** Intern, extern, Cloud, Partner
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Verschlüsselte Übertragung
Vertrauliche Informationen werden verschlüsselt übertragen. Verschlüsselung erfolgt in Transit (TLS/SSL) und at Rest.

### 3.2 E-Mail-Sicherheit
E-Mail-Kommunikation ist gesichert:
- **Inbound:** SPF, DKIM, DMARC, Anti-Spam, Anti-Malware
- **Outbound:** TLS-Verschlüsselung, S/MIME oder PGP für vertrauliche Inhalte
- **Phishing-Schutz:** User Awareness, technische Schutzmaßnahmen

### 3.3 Sichere File Sharing
File Sharing erfolgt über genehmigte Plattformen. Vertrauliche Dateien werden verschlüsselt geteilt. Public File Sharing (z.B. WeTransfer) ist für vertrauliche Daten untersagt.

### 3.4 Collaboration Tools
Collaboration Tools (Teams, Slack, etc.) müssen Sicherheitsanforderungen erfüllen:
- Verschlüsselte Kommunikation
- Zugriffskontrolle
- Data Loss Prevention (DLP)
- Audit Logging

### 3.5 Messaging und Chat
Instant Messaging für geschäftliche Kommunikation erfolgt über genehmigte Tools. Private Messaging-Apps sind für vertrauliche Geschäftsinformationen untersagt.

### 3.6 Data Loss Prevention (DLP)
DLP-Systeme verhindern unbeabsichtigte oder böswillige Datenexfiltration. DLP überwacht E-Mail, File Sharing und Collaboration Tools.

### 3.7 Externe Kommunikation
Kommunikation mit externen Parteien (Kunden, Partner, Lieferanten) erfolgt über sichere Kanäle. Vertraulichkeitsvereinbarungen (NDAs) werden bei Bedarf abgeschlossen.

### 3.8 Mobile Kommunikation
Mobile Kommunikation (Smartphones, Tablets) erfolgt über sichere Kanäle. Mobile Geräte sind mit MDM/MAM verwaltet (siehe `0500_Policy_Mobile_Device_und_Remote_Work.md`).

### 3.9 Social Media
Geschäftliche Social-Media-Nutzung folgt Social-Media-Richtlinien. Vertrauliche Informationen werden nicht über Social Media geteilt.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Informationsübertragung und Kommunikation

| Aktivität | CISO | IT-Betrieb | Communication Security | End User | DPO |
|-----------|------|------------|------------------------|----------|-----|
| Policy-Erstellung | R/A | C | R | I | C |
| E-Mail-Security | C | R/A | R | I | C |
| File Sharing | C | R/A | R | R | C |
| Collaboration Tools | C | R/A | R | R | C |
| DLP-Implementierung | R/A | R | R | I | C |
| Externe Kommunikation | C | C | C | R | C |
| Mobile Kommunikation | C | R/A | C | R | I |
| Social Media | C | I | R/A | R | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** Thomas Weber (CISO)
- **Communication Security Manager:** {{ meta.communication.security_manager }}
- **IT Operations Manager:** {{ meta.it.operations_manager }}
- **Data Protection Officer:** {{ meta.dpo.name }}
- **Umsetzungsverantwortliche:** IT-Betrieb, End Users
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, DPO

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0670_Richtlinie_Email_Sharing_und_Zusammenarbeitstools.md** - Detaillierte Implementierungsrichtlinie
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Encryption Policy
- `0500_Policy_Mobile_Device_und_Remote_Work.md` - Mobile Device Policy

### Zugehörige Standards/Baselines
- E-Mail-Security-Konfiguration (SPF, DKIM, DMARC)
- Genehmigte File-Sharing-Plattformen
- Genehmigte Collaboration Tools
- DLP-Regeln und -Policies
- Social-Media-Richtlinien

### Zugehörige Prozesse
- E-Mail-Verschlüsselungsprozess (S/MIME, PGP)
- File-Sharing-Genehmigungsprozess
- DLP-Incident-Response
- Externe Kommunikation (NDA-Prozess)

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- E-Mail-Verschlüsselungsrate (Ziel: 100% für vertrauliche E-Mails)
- SPF/DKIM/DMARC-Compliance (Ziel: 100%)
- DLP-Incident-Rate
- Anzahl blockierter Phishing-E-Mails
- File-Sharing-Compliance (Ziel: 100% genehmigte Plattformen)
- Collaboration-Tool-Compliance
- Anzahl Social-Media-Verstöße

### Nachweise und Evidence
- E-Mail-Security-Konfiguration (SPF, DKIM, DMARC)
- E-Mail-Verschlüsselungsprotokolle
- DLP-Logs und Incident-Reports
- File-Sharing-Logs
- Collaboration-Tool-Konfiguration
- Phishing-Simulation-Ergebnisse
- Social-Media-Monitoring

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Unverschlüsselte vertrauliche E-Mails:** Incident Response, User Awareness Training
- **Nicht genehmigte File-Sharing-Tools:** Zugriff blockiert, Disziplinarmaßnahmen
- **DLP-Verstöße:** Incident Response, Untersuchung, ggf. Disziplinarmaßnahmen
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen, Zugriffsentzug

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Communication Security Manager genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0670_Richtlinie_Email_Sharing_und_Zusammenarbeitstools.md` - Detailed Guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.14** - Information transfer
- **ISO/IEC 27001:2022 Annex A.8.24** - Use of cryptography
- **ISO/IEC 27001:2022 Annex A.8.26** - Application security requirements
- **NIST SP 800-177** - Trustworthy Email
- **RFC 7208** - Sender Policy Framework (SPF)
- **RFC 6376** - DomainKeys Identified Mail (DKIM)
- **RFC 7489** - Domain-based Message Authentication, Reporting, and Conformance (DMARC)

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)
