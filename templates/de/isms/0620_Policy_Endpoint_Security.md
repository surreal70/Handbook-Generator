# Policy: Endpoint Security

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes requirements for endpoint security and device protection.
It ensures that all endpoints (workstations, laptops, mobile devices) are properly secured.
Customize based on your organization's endpoint landscape and security requirements.

ISO 27001:2022 Annex A Reference: A.8.1, A.8.2, A.8.3, A.6.7
-->

**Dokument-ID:** 0620  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.8.1-A.8.3, A.6.7 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Anforderungen an die Endpoint Security der **{{ meta.organization.name }}**. Sie stellt sicher, dass alle Endgeräte (Workstations, Laptops, mobile Geräte) angemessen gesichert sind und vor Bedrohungen geschützt werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta.organization.name }}
- **Geräte:** Alle Endgeräte (Workstations, Laptops, Tablets, Smartphones)
- **Betriebssysteme:** Windows, macOS, Linux, iOS, Android
- **Eigentum:** Unternehmenseigene und BYOD-Geräte (mit Unternehmenszugriff)
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte, Remote Work

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Endpoint Protection Platform (EPP)
Alle Endgeräte sind mit Endpoint Protection ausgestattet. EPP umfasst Antivirus, Anti-Malware, Host-Firewall und Application Control.

### 3.2 Endpoint Detection and Response (EDR)
Kritische Endgeräte sind mit EDR-Lösung ausgestattet. EDR ermöglicht erweiterte Bedrohungserkennung, Incident Response und Forensik.

### 3.3 Device Compliance
Endgeräte müssen Compliance-Anforderungen erfüllen:
- Aktuelle Betriebssystem-Version
- Aktuelle Security-Patches
- EPP/EDR installiert und aktiv
- Disk Encryption aktiviert
- Screen Lock konfiguriert

### 3.4 Disk Encryption
Alle Endgeräte mit Unternehmensdaten sind verschlüsselt (Full Disk Encryption). Verschlüsselung schützt vor Datenverlust bei Diebstahl oder Verlust.

### 3.5 Host-based Firewall
Alle Endgeräte haben eine aktivierte Host-Firewall. Firewall-Regeln folgen dem Least-Privilege-Prinzip.

### 3.6 Application Control
Nicht autorisierte Anwendungen werden blockiert (Application Whitelisting oder Blacklisting). Application Control reduziert Malware-Risiko.

### 3.7 Patch Management
Endgeräte werden regelmäßig gepatcht. Security-Patches werden zeitnah installiert (siehe `0340_Policy_Vulnerability_und_Patch_Management.md`).

### 3.8 Remote Wipe
Verlorene oder gestohlene Geräte können remote gelöscht werden. Remote Wipe schützt vor Datenverlust.

### 3.9 BYOD (Bring Your Own Device)
BYOD-Geräte mit Unternehmenszugriff müssen Mindest-Sicherheitsanforderungen erfüllen. BYOD wird über MDM/MAM verwaltet (siehe `0500_Policy_Mobile_Device_und_Remote_Work.md`).

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Endpoint Security

| Aktivität | CISO | Endpoint Security | IT-Betrieb | SOC | End User |
|-----------|------|-------------------|------------|-----|----------|
| Policy-Erstellung | R/A | R | C | C | I |
| EPP/EDR-Deployment | C | R/A | R | C | I |
| Device Compliance | C | R/A | R | C | R |
| Disk Encryption | C | R/A | R | I | C |
| Patch Management | C | R | R/A | I | C |
| Remote Wipe | C | R/A | C | C | I |
| BYOD-Management | C | R/A | R | I | R |
| Incident Response | C | R | C | R/A | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Endpoint Security Manager:** {{ meta.endpoint.security_manager }}
- **IT Operations Manager:** {{ meta.it.operations_manager }}
- **SOC Manager:** {{ meta.soc.manager }}
- **Umsetzungsverantwortliche:** IT-Betrieb, End Users
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, SOC

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0630_Richtlinie_EDR_AV_Host_Firewall_und_Device_Compliance.md** - Detaillierte Implementierungsrichtlinie
- `0500_Policy_Mobile_Device_und_Remote_Work.md` - Mobile Device Policy
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Patch Management Policy
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Encryption Policy

### Zugehörige Standards/Baselines
- Endpoint Security Baseline (Windows, macOS, Linux)
- EPP/EDR-Konfiguration
- Device Compliance Requirements
- Disk Encryption Standards
- Application Whitelist/Blacklist

### Zugehörige Prozesse
- Endpoint Onboarding/Offboarding
- Device Compliance Monitoring
- EPP/EDR Alert Response
- Remote Wipe Prozess
- BYOD Enrollment

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- EPP/EDR Coverage (Ziel: 100% aller Endgeräte)
- Device Compliance Rate (Ziel: >95%)
- Disk Encryption Coverage (Ziel: 100%)
- Patch Compliance (Ziel: >95% innerhalb SLA)
- EPP/EDR Detection Rate
- Durchschnittliche Incident Response Time (Ziel: < 30 Minuten)
- Anzahl Remote Wipes

### Nachweise und Evidence
- Endpoint Inventory
- EPP/EDR-Deployment-Status
- Device Compliance Reports
- Disk Encryption Status
- Patch Compliance Reports
- EPP/EDR-Logs und Alerts
- Remote Wipe Logs

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Non-compliant Devices:** Netzwerkzugriff blockiert bis Compliance hergestellt
- **Deaktivierte EPP/EDR:** Sofortige Reaktivierung, Incident Response
- **Fehlende Disk Encryption:** Nachholung, Zugriffsbeschränkung
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen, Gerätenutzung untersagt

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Endpoint Security Manager genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0630_Richtlinie_EDR_AV_Host_Firewall_und_Device_Compliance.md` - Detailed Guideline
- `0500_Policy_Mobile_Device_und_Remote_Work.md` - Mobile Device Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.1** - User endpoint devices
- **ISO/IEC 27001:2022 Annex A.8.2** - Privileged access rights
- **ISO/IEC 27001:2022 Annex A.8.3** - Information access restriction
- **ISO/IEC 27001:2022 Annex A.6.7** - Remote working
- **NIST SP 800-124** - Guidelines for Managing the Security of Mobile Devices
- **NIST SP 800-171** - Protecting Controlled Unclassified Information
- **CIS Controls v8** - Control 4 (Secure Configuration of Enterprise Assets)

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
