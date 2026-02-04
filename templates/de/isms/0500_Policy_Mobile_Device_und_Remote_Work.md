# Policy: Mobile Device und Remote Work

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for mobile device management and remote work security.
It ensures that mobile devices and remote access are secure and compliant with organizational
security requirements. Customize based on your organization's BYOD policy and remote work model.

ISO 27001:2022 Annex A Reference: A.6.7, A.6.8, A.8.9
-->

**Dokument-ID:** 0500  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.6.7, A.6.8, A.8.9 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Grundsätze für Mobile Device Management und Remote Work der **{{ meta.organization.name }}**. Sie stellt sicher, dass mobile Geräte und Remote-Zugriffe sicher verwaltet werden und den Sicherheitsanforderungen der Organisation entsprechen.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta.organization.name }}
- **Geräte:** Laptops, Smartphones, Tablets, Wearables (unternehmenseigen und BYOD)
- **Zugriffsmethoden:** VPN, Remote Desktop, Cloud-Services, Mobile Apps
- **Personen:** Alle Mitarbeiter, Auftragnehmer mit Remote-Zugriff
- **Standorte:** {{ netbox.site.name }}, Home Office, öffentliche Orte, Reisen

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Mobile Device Management (MDM)
Alle mobilen Geräte mit Zugriff auf Unternehmensressourcen werden über ein MDM-System verwaltet. MDM ermöglicht Konfiguration, Monitoring und Remote-Wipe.

### 3.2 BYOD (Bring Your Own Device)
Private Geräte dürfen nur nach Genehmigung und Enrollment im MDM für geschäftliche Zwecke genutzt werden. BYOD-Geräte unterliegen denselben Sicherheitsanforderungen wie Unternehmensgeräte.

### 3.3 Device Encryption
Alle mobilen Geräte müssen vollständig verschlüsselt sein (Full Disk Encryption). Verschlüsselung wird über MDM erzwungen und überwacht.

### 3.4 Secure Remote Access
Remote-Zugriff auf Unternehmensressourcen erfolgt ausschließlich über sichere Kanäle:
- VPN mit Multi-Faktor-Authentisierung
- Zero Trust Network Access (ZTNA)
- Sichere Remote Desktop Lösungen

### 3.5 Device Compliance
Mobile Geräte müssen Compliance-Anforderungen erfüllen:
- Aktuelle Betriebssystem-Version
- Installierte Sicherheits-Updates
- Aktivierte Bildschirmsperre
- Keine Jailbreak/Root
- Installierte Endpoint-Security-Software

### 3.6 Lost/Stolen Device Response
Bei Verlust oder Diebstahl mobiler Geräte wird sofort ein Incident gemeldet. Remote-Wipe wird durchgeführt, um Datenverlust zu verhindern.

### 3.7 Public Wi-Fi und Netzwerksicherheit
Nutzung öffentlicher Wi-Fi-Netzwerke ist nur über VPN gestattet. Unverschlüsselte Verbindungen zu Unternehmensressourcen sind untersagt.

### 3.8 Remote Work Security
Remote-Arbeitsplätze müssen Sicherheitsanforderungen erfüllen:
- Sichere Netzwerkverbindung
- Physische Sicherheit (Bildschirmsperre, Clear Desk)
- Keine Weitergabe von Zugangsdaten
- Compliance mit Acceptable Use Policy

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Mobile Device und Remote Work

| Aktivität | CISO | IT-Betrieb | MDM Administrator | Mitarbeiter | HR |
|-----------|------|------------|-------------------|-------------|-----|
| Policy-Erstellung | R/A | C | C | I | C |
| MDM-Betrieb | A | R | R | I | I |
| Device Enrollment | I | C | R | R/A | I |
| Compliance-Monitoring | A | C | R | I | I |
| Lost Device Response | A | R | R | R | C |
| Remote Access Provisioning | C | R/A | C | I | I |
| Security Training | A | I | I | R | R |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **MDM Administrator:** {{ meta.it.mdm_admin }}
- **Remote Access Manager:** {{ meta.it.remote_access_manager }}
- **Umsetzungsverantwortliche:** IT-Betrieb, Mitarbeiter
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0510_Richtlinie_MDM_BringYourOwnDevice_und_Remote_Access.md** - Detaillierte Implementierungsrichtlinie
- `0200_Policy_Akzeptable_Nutzung_IT.md` - Acceptable Use Policy
- `0240_Policy_Authentisierung_und_Passwoerter.md` - Authentication Policy
- `0620_Policy_Endpoint_Security.md` - Endpoint Security Policy

### Zugehörige Standards/Baselines
- MDM-Konfigurationsstandards
- Device Compliance Requirements
- BYOD-Richtlinie
- Remote Access Standards

### Zugehörige Prozesse
- Device Enrollment Prozess
- Lost/Stolen Device Response Prozess
- Remote Access Provisioning Prozess
- BYOD Approval Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- MDM Enrollment Rate (Ziel: 100% mobiler Geräte)
- Device Compliance Rate (Ziel: 95%)
- Anzahl nicht-compliant Geräte
- Durchschnittliche Zeit zur Remote-Wipe bei Lost Devices
- VPN-Nutzungsrate bei Remote Work
- Anzahl Lost/Stolen Device Incidents

### Nachweise und Evidence
- MDM-Enrollment-Status
- Device Compliance Reports
- Remote Access Logs
- Lost Device Incident Reports
- BYOD Approval Dokumentation
- Security Training Nachweise

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nicht-enrollte Geräte:** Zugriffssperre, Enrollment-Pflicht
- **Non-Compliance:** Zugriffsbeschränkung bis Remediation
- **Nicht gemeldeter Geräteverlust:** Untersuchung, Disziplinarmaßnahmen
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
- `0510_Richtlinie_MDM_BringYourOwnDevice_und_Remote_Access.md` - Detailed Guideline
- `0620_Policy_Endpoint_Security.md` - Endpoint Security Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.6.7** - Remote working
- **ISO/IEC 27001:2022 Annex A.6.8** - Information security event reporting
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **NIST SP 800-46** - Guide to Enterprise Telework, Remote Access, and BYOD Security
- **DSGVO (EU 2016/679)** - Datenschutz bei BYOD und Remote Work

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)
