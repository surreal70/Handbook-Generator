# Richtlinie: MDM, Bring Your Own Device und Remote Access

**Dokument-ID:** 0510
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0500_Policy_Mobile_Device_und_Remote_Work.md` und definiert:
- Mobile Device Management (MDM) Anforderungen
- BYOD-Richtlinien und -Prozesse
- Remote-Access-Kontrollen

**Geltungsbereich:** Alle mobilen Geräte und Remote-Zugriffe bei **{{ meta-organisation.name }}**

## 2. Mobile Device Management (MDM)

### 2.1 MDM-System

**Plattform:** {{ meta.mdm.system }} (z.B. Microsoft Intune, Jamf, MobileIron)

**Verwaltete Geräte:**
- Unternehmenseigene Smartphones und Tablets
- BYOD-Geräte mit Unternehmenszugriff
- Laptops (optional, je nach MDM-Fähigkeit)

### 2.2 MDM-Enrollment

**Prozess:**
1. Gerät erhalten oder BYOD-Antrag genehmigt
2. MDM-App installieren
3. Enrollment durchführen
4. Compliance-Checks bestehen
5. Unternehmenszugriff aktiviert

**Pflicht-Enrollment:**
- Alle unternehmenseigenen Geräte
- Alle BYOD-Geräte mit E-Mail-Zugriff oder Unternehmens-Apps

### 2.3 MDM-Policies

**Erzwungene Einstellungen:**
- Geräteverschlüsselung aktiviert
- PIN/Passcode (min. 6 Zeichen) oder Biometrie
- Automatische Bildschirmsperre (5 Minuten)
- OS-Updates innerhalb 30 Tage
- Jailbreak/Root-Detection

**Verbotene Aktivitäten:**
- Jailbreak oder Rooting
- Installation aus unbekannten Quellen
- Deaktivierung von Sicherheitsfeatures

### 2.4 Compliance-Checks

**Automatische Prüfungen:**
- OS-Version aktuell?
- Verschlüsselung aktiv?
- Jailbreak/Root erkannt?
- Malware erkannt?

**Bei Non-Compliance:**
- Warnung an Nutzer (24 Stunden Frist)
- Eingeschränkter Zugriff
- Vollständige Sperrung nach 7 Tagen

## 3. BYOD (Bring Your Own Device)

### 3.1 BYOD-Berechtigung

**Voraussetzungen:**
- Antrag über Self-Service-Portal
- Genehmigung durch Vorgesetzten
- BYOD-Vereinbarung unterschreiben
- MDM-Enrollment

**Berechtigte Geräte:**
- Smartphones (iOS, Android)
- Tablets (iOS, Android)
- Laptops (nach Einzelfallprüfung)

### 3.2 BYOD-Vereinbarung

**Inhalte:**
- Nutzungsbedingungen
- Sicherheitsanforderungen
- MDM-Enrollment-Pflicht
- Remote-Wipe-Zustimmung
- Datenschutz (Trennung privat/geschäftlich)
- Haftung bei Verlust

### 3.3 Containerisierung

**Technologie:**
- Separate Container für geschäftliche Daten
- Verschlüsselte Container
- Keine Vermischung privat/geschäftlich

**Beispiele:**
- iOS: Managed Apps
- Android: Work Profile
- Windows: Windows Information Protection (WIP)

### 3.4 BYOD-Offboarding

**Bei Vertragsende oder BYOD-Beendigung:**
1. Remote Wipe des geschäftlichen Containers
2. Entfernung von Unternehmens-Apps
3. Widerruf von Zertifikaten
4. MDM-Unenrollment
5. Private Daten bleiben erhalten

## 4. Remote Access

### 4.1 VPN-Zugriff

**VPN-System:** {{ meta.network.vpn_solution }}

**Anforderungen:**
- Multi-Faktor-Authentifizierung (MFA)
- Endpoint-Compliance-Check vor Verbindung
- Split-Tunneling verboten (Full-Tunnel)
- Session-Timeout: 8 Stunden

**VPN-Clients:**
- Unternehmens-genehmigte Clients
- Automatische Updates
- Kill-Switch aktiviert

### 4.2 Zero Trust Network Access (ZTNA)

**Prinzipien:**
- Never Trust, Always Verify
- Least Privilege Access
- Micro-Segmentation

**Implementierung:**
- Identity-basierte Zugriffskontrolle
- Device Posture Checks
- Continuous Authentication

### 4.3 Remote Desktop

**Technologien:**
- RDP über VPN (Windows)
- SSH über VPN (Linux)
- Citrix/VMware Horizon (Virtual Desktops)

**Sicherheitskontrollen:**
- MFA für Remote Desktop
- Session-Recording (privilegierte Zugriffe)
- Idle-Timeout: 30 Minuten

## 5. Remote Work Security

### 5.1 Home Office Anforderungen

**Netzwerk:**
- Sicheres WLAN (WPA3 oder WPA2)
- Keine öffentlichen WLANs ohne VPN
- Router-Firmware aktuell

**Arbeitsplatz:**
- Privater Arbeitsbereich (keine Einsicht Dritter)
- Bildschirmsperre bei Abwesenheit
- Keine Nutzung durch Familienmitglieder

### 5.2 Öffentliche Orte

**Erlaubt mit Einschränkungen:**
- Arbeit in Cafés, Flughäfen, Hotels
- VPN verpflichtend
- Privacy-Screen für Laptop
- Keine vertraulichen Gespräche

**Verboten:**
- Öffentliche Computer (Internet-Cafés)
- Ungesicherte WLANs ohne VPN
- Unbeaufsichtigtes Gerät

### 5.3 Reisen

**Internationale Reisen:**
- Meldung an IT-Security (Hochrisiko-Länder)
- Reise-Laptop ohne vertrauliche Daten
- Verschlüsselung verpflichtend
- Keine Nutzung lokaler USB-Sticks

## 6. Mobile Application Management (MAM)

### 6.1 Genehmigte Apps

**Unternehmens-Apps:**
- E-Mail ({{ meta.email.mobile_app }})
- Collaboration ({{ meta.collaboration.mobile_app }})
- VPN-Client
- Authenticator-App

**Genehmigungsprozess:**
- Antrag über IT-Portal
- Security-Review
- Freigabe durch IT-Security

### 6.2 App-Wrapping

**Für unternehmenseigene Apps:**
- MDM-Policies in App integrieren
- Verschlüsselung erzwingen
- Copy/Paste-Kontrolle

## 7. Incident Response

### 7.1 Geräteverlust

**Sofortmaßnahmen:**
1. Meldung an IT-Support ({{ meta.support.phone }})
2. Remote Wipe auslösen (innerhalb 1 Stunde)
3. Passwörter ändern
4. Incident-Ticket erstellen
5. Polizeimeldung (bei Diebstahl)

### 7.2 Kompromittierung

**Bei Verdacht auf Malware:**
1. Gerät vom Netzwerk trennen
2. IT-Security informieren
3. Forensische Analyse (falls erforderlich)
4. Gerät neu aufsetzen
5. Lessons Learned

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| MDM-Enrollment-Rate | 100% |
| Compliance-Rate | > 95% |
| OS-Update-Rate (30 Tage) | > 90% |
| Remote-Wipe-Success-Rate | 100% |

### 8.2 Audit-Nachweise

- MDM-Enrollment-Logs
- Compliance-Reports
- BYOD-Vereinbarungen
- Remote-Access-Logs

## 9. Referenzen

### Interne Dokumente
- `0500_Policy_Mobile_Device_und_Remote_Work.md`
- `0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.6.7** - Remote working
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **NIST SP 800-124** - Guidelines for Managing the Security of Mobile Devices

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

