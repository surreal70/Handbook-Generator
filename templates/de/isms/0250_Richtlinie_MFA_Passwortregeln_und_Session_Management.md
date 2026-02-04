# Richtlinie: MFA, Passwortregeln und Session Management

<!-- 
TEMPLATE AUTHOR NOTE:
This guideline provides detailed implementation guidance for authentication controls,
including Multi-Factor Authentication (MFA), password policies, and session management.
Customize based on your organization's risk tolerance and technical capabilities.
-->

**Dokument-ID:** 0250  
**Dokumenttyp:** Richtlinie (detailliert)  
**Zugehörige Policy:** 0240_Policy_Authentisierung_und_Passwoerter.md  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.17, A.5.18  
**Owner:** {{ meta.it_operations.manager }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0240_Policy_Authentisierung_und_Passwoerter.md` und definiert detaillierte Regeln für:
- Multi-Faktor-Authentifizierung (MFA)
- Passwortrichtlinien und Komplexitätsanforderungen
- Session Management und Timeouts
- Authentifizierungsmethoden und -technologien

**Geltungsbereich:** Alle Systeme, Anwendungen und Nutzer bei **{{ meta.organization.name }}**

## 2. Multi-Faktor-Authentifizierung (MFA)

### 2.1 MFA-Pflicht

**Obligatorisch für:**
- Alle Remote-Zugriffe (VPN, Remote Desktop)
- Alle privilegierten Accounts (Administratoren, Root)
- Zugriff auf kritische Systeme (Produktion, Finanzsysteme)
- Cloud-Services und SaaS-Anwendungen
- E-Mail-Zugriff von externen Geräten
- Zugriff auf vertrauliche Daten

**Optional für:**
- Lokale Anmeldungen im Büro (kann durch Conditional Access erzwungen werden)
- Nicht-kritische interne Anwendungen

### 2.2 MFA-Methoden

**Unterstützte Faktoren:**

| Methode | Typ | Sicherheitsstufe | Anwendungsfall |
|---------|-----|------------------|----------------|
| Authenticator-App (TOTP) | Besitz | Hoch | Standard für alle Nutzer |
| Hardware-Token (FIDO2/U2F) | Besitz | Sehr hoch | Privilegierte Nutzer, Hochsicherheit |
| SMS-Code | Besitz | Mittel | Fallback, nicht empfohlen |
| Push-Benachrichtigung | Besitz | Hoch | Mobile Nutzer |
| Biometrie (Fingerabdruck, Face ID) | Inhärenz | Hoch | Mobile Geräte, Windows Hello |

**Empfohlene Methode:** Authenticator-App (z.B. Microsoft Authenticator, Google Authenticator, Authy)

**Nicht erlaubt:**
- E-Mail-basierte Codes (zu unsicher)
- Sicherheitsfragen (anfällig für Social Engineering)

### 2.3 MFA-Registrierung

**Onboarding:**
1. Neue Mitarbeiter registrieren MFA am ersten Arbeitstag
2. IT-Support unterstützt bei Einrichtung
3. Mindestens 2 MFA-Methoden registrieren (Primary + Backup)
4. Backup-Codes generieren und sicher aufbewahren

**Self-Service:**
- Nutzer können MFA-Methoden über Self-Service-Portal verwalten
- Änderung von MFA-Methoden erfordert Re-Authentifizierung
- Verlust von MFA-Gerät: IT-Support-Prozess für Reset

### 2.4 MFA-Bypass und Notfallzugriff

**Break-Glass-Accounts:**
- Notfall-Accounts ohne MFA für Systemwiederherstellung
- Gesichert in Safe, nur für Notfälle
- Nutzung wird sofort an CISO eskaliert
- Passwort nach jeder Nutzung ändern

**Temporärer MFA-Bypass:**
- Nur in Ausnahmefällen (z.B. Geräteverlust)
- Genehmigung durch IT-Security erforderlich
- Maximal 24 Stunden, dann automatische Sperrung
- Erhöhtes Monitoring während Bypass-Zeitraum

## 3. Passwortrichtlinien

### 3.1 Passwortkomplexität

**Anforderungen für Standard-Nutzer:**
- **Mindestlänge:** 12 Zeichen
- **Komplexität:** Mindestens 3 von 4 Zeichentypen:
  - Großbuchstaben (A-Z)
  - Kleinbuchstaben (a-z)
  - Ziffern (0-9)
  - Sonderzeichen (!@#$%^&*)
- **Keine Wörterbuch-Wörter:** Passwort darf nicht in Common-Password-Liste enthalten sein
- **Keine persönlichen Informationen:** Kein Name, Geburtsdatum, Benutzername

**Anforderungen für privilegierte Nutzer:**
- **Mindestlänge:** 16 Zeichen
- **Komplexität:** Alle 4 Zeichentypen erforderlich
- **Passphrase empfohlen:** Z.B. "Kaffee!Morgen@2024#Sicher"

**Technische Durchsetzung:**
- Active Directory Group Policy Objects (GPOs)
- Azure AD Password Protection
- Passwort-Filter für Common-Password-Prüfung

### 3.2 Passwortänderung

**Regelmäßige Änderung:**
- **Standard-Nutzer:** Alle 90 Tage (optional, wenn MFA aktiv)
- **Privilegierte Nutzer:** Alle 60 Tage (verpflichtend)
- **Service-Accounts:** Alle 180 Tage oder bei Personalwechsel

**Erzwungene Änderung:**
- Bei erstem Login (initiales Passwort)
- Nach Passwort-Reset durch IT-Support
- Bei Verdacht auf Kompromittierung
- Nach Sicherheitsvorfällen

**Passwort-Historie:**
- Letzten 12 Passwörter dürfen nicht wiederverwendet werden
- Verhindert Rotation zwischen wenigen Passwörtern

### 3.3 Passwort-Reset

**Self-Service Password Reset (SSPR):**
- Nutzer können Passwort selbst zurücksetzen über {{ meta.iam.sspr_url }}
- Verifizierung über:
  - MFA-Methode (Authenticator-App, SMS)
  - Alternative E-Mail-Adresse
  - Sicherheitsfragen (nur als Fallback)
- Audit-Log für alle Passwort-Resets

**IT-Support-Reset:**
- Bei Verlust aller SSPR-Methoden
- Identitätsprüfung erforderlich (Personalausweis, Mitarbeiter-ID)
- Temporäres Passwort, muss bei erstem Login geändert werden
- Dokumentation im Ticketsystem

**Notfall-Reset:**
- Bei gesperrten Accounts außerhalb Geschäftszeiten
- On-Call IT-Support verfügbar
- Erhöhte Verifizierung (Vorgesetzten-Bestätigung)

### 3.4 Passwort-Manager

**Empfehlung:**
- Nutzung von Passwort-Manager für alle Nutzer
- Unternehmens-Lösung: {{ meta.security.password_manager }} (z.B. 1Password, Bitwarden)
- Zentrale Verwaltung von Shared Credentials

**Funktionen:**
- Generierung starker, zufälliger Passwörter
- Sichere Speicherung verschlüsselt
- Browser-Integration für Auto-Fill
- Sharing von Credentials im Team (verschlüsselt)
- Audit-Log für Zugriffe

**Schulung:**
- Onboarding-Schulung für neue Mitarbeiter
- Best Practices für Passwort-Manager-Nutzung
- Vermeidung von Passwort-Wiederverwendung

## 4. Session Management

### 4.1 Session-Timeouts

**Inaktivitäts-Timeouts:**

| System-Typ | Timeout | Begründung |
|------------|---------|------------|
| Workstation (lokal) | 15 Minuten | Physischer Zugriff möglich |
| VPN-Verbindung | 8 Stunden | Remote-Zugriff, Re-Auth täglich |
| Web-Anwendungen | 30 Minuten | Balance zwischen Sicherheit und Usability |
| Privilegierte Sessions | 10 Minuten | Erhöhtes Risiko |
| Mobile Apps | 5 Minuten | Geräteverlust-Risiko |

**Absolute Session-Limits:**
- **Standard-Nutzer:** Max. 12 Stunden, dann Re-Authentifizierung
- **Privilegierte Nutzer:** Max. 4 Stunden, dann Re-Authentifizierung
- **Remote-Zugriffe:** Max. 8 Stunden, dann Re-Authentifizierung

### 4.2 Bildschirmsperre

**Automatische Sperre:**
- Nach Inaktivitäts-Timeout (siehe oben)
- Entsperren nur mit Passwort oder Biometrie
- Keine Anzeige sensibler Informationen auf Sperrbildschirm

**Manuelle Sperre:**
- Nutzer müssen Workstation sperren beim Verlassen (Windows+L, Ctrl+Alt+Del)
- Awareness-Kampagnen zu "Clean Desk Policy"
- Stichproben durch Security-Team

### 4.3 Concurrent Sessions

**Limits:**
- **Standard-Nutzer:** Max. 3 gleichzeitige Sessions
- **Privilegierte Nutzer:** Max. 2 gleichzeitige Sessions
- **Service-Accounts:** Max. 1 Session (verhindert Credential-Sharing)

**Monitoring:**
- Alerts bei ungewöhnlichen Session-Mustern
- Automatische Sperrung bei Verdacht auf Account-Sharing
- Geolocation-Checks (unmögliche Reisen)

### 4.4 Session-Sicherheit

**Technische Kontrollen:**
- **Session-Tokens:** Kryptographisch sichere, zufällige Tokens
- **Token-Rotation:** Neue Tokens nach Re-Authentifizierung
- **Secure Cookies:** HttpOnly, Secure, SameSite Flags
- **Session-Fixation-Schutz:** Neue Session-ID nach Login
- **HTTPS-Erzwingung:** Alle Sessions über verschlüsselte Verbindungen

## 5. Authentifizierungsmethoden

### 5.1 Single Sign-On (SSO)

**Implementierung:**
- **Identity Provider:** {{ meta.iam.idp }} (z.B. Azure AD, Okta)
- **Protokolle:** SAML 2.0, OAuth 2.0, OpenID Connect
- **Anwendungen:** Alle Cloud-SaaS-Anwendungen über SSO

**Vorteile:**
- Einmalige Anmeldung für alle Anwendungen
- Zentrale Authentifizierung und MFA
- Reduzierte Passwort-Müdigkeit
- Vereinfachtes Offboarding (zentrale Sperrung)

**Conditional Access:**
- Risikobasierte Authentifizierung
- Geräte-Compliance-Checks
- Geolocation-basierte Policies
- Erzwingung von MFA bei erhöhtem Risiko

### 5.2 Zertifikat-basierte Authentifizierung

**Anwendungsfälle:**
- Maschine-zu-Maschine-Authentifizierung
- VPN-Zugriff (zusätzlich zu MFA)
- Wireless-Netzwerk (802.1X)
- Code-Signing und E-Mail-Verschlüsselung

**PKI-Infrastruktur:**
- Interne Certificate Authority (CA): {{ meta.pki.ca }}
- Zertifikats-Lebenszyklus-Management
- Automatische Erneuerung vor Ablauf
- Revocation-Checks (CRL, OCSP)

### 5.3 Biometrische Authentifizierung

**Unterstützte Methoden:**
- **Windows Hello for Business:** Fingerabdruck, Gesichtserkennung
- **Mobile Geräte:** Touch ID, Face ID
- **Nur als zweiter Faktor:** Biometrie ersetzt nicht Passwort

**Datenschutz:**
- Biometrische Daten werden lokal auf Gerät gespeichert (nicht zentral)
- Keine Übertragung biometrischer Rohdaten
- DSGVO-konforme Verarbeitung

## 6. Service-Accounts und technische Accounts

### 6.1 Service-Account-Richtlinien

**Anforderungen:**
- **Keine interaktiven Logins:** Service-Accounts dürfen nicht für menschliche Anmeldungen genutzt werden
- **Starke Passwörter:** Mindestens 24 Zeichen, zufällig generiert
- **Passwort-Rotation:** Alle 180 Tage oder bei Personalwechsel
- **Dokumentation:** Zweck, Owner, verwendete Systeme

**Verwaltung:**
- Zentrale Verwaltung in Passwort-Manager oder PAM-System
- Genehmigung durch CISO für neue Service-Accounts
- Regelmäßige Reviews (quartalsweise)
- Deaktivierung ungenutzter Accounts

### 6.2 API-Keys und Tokens

**Best Practices:**
- **Rotation:** API-Keys alle 90 Tage rotieren
- **Least Privilege:** Minimale Berechtigungen für API-Keys
- **Secrets Management:** Speicherung in Secrets-Manager (z.B. HashiCorp Vault, Azure Key Vault)
- **Keine Hardcoding:** API-Keys nicht in Code oder Config-Dateien

**Monitoring:**
- Logging aller API-Zugriffe
- Alerts bei ungewöhnlichen API-Nutzungsmustern
- Rate-Limiting für API-Calls

## 7. Monitoring und Alerting

### 7.1 Authentifizierungs-Monitoring

**Überwachte Events:**
- Fehlgeschlagene Login-Versuche (Brute-Force-Detection)
- Erfolgreiche Logins von ungewöhnlichen Standorten
- MFA-Bypass-Versuche
- Passwort-Resets (insbesondere privilegierte Accounts)
- Concurrent Sessions von verschiedenen IPs

**Automatische Alerts:**
- **5 fehlgeschlagene Logins:** Warnung an Nutzer
- **10 fehlgeschlagene Logins:** Account-Sperrung (30 Minuten)
- **Login von neuem Gerät/Standort:** MFA-Challenge
- **Unmögliche Reise:** Alert an Security-Team (z.B. Login in Deutschland, 1 Stunde später in USA)

### 7.2 Account-Sperrung

**Automatische Sperrung:**
- Nach 10 fehlgeschlagenen Login-Versuchen
- Sperrdauer: 30 Minuten (automatische Entsperrung)
- Manuelle Entsperrung durch IT-Support möglich

**Privilegierte Accounts:**
- Bereits nach 5 fehlgeschlagenen Versuchen
- Manuelle Entsperrung nur durch CISO oder IT-Security
- Untersuchung bei Sperrung (möglicher Angriff)

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert | Messung |
|--------|----------|---------|
| MFA-Adoption-Rate | > 99% | IAM-System |
| Passwort-Komplexität-Compliance | 100% | AD-Reports |
| Fehlgeschlagene Logins | < 100 pro Tag | SIEM |
| Passwort-Resets | < 50 pro Monat | IAM-System |
| Session-Timeout-Compliance | > 95% | Endpoint-Monitoring |

### 8.2 Audit-Nachweise

**Dokumentation:**
- Authentifizierungs-Logs (Erfolg und Fehler)
- MFA-Registrierungen und -Nutzung
- Passwort-Änderungen und -Resets
- Account-Sperrungen und Entsperrungen
- Privilegierte Zugriffe

**Retention:**
- Authentifizierungs-Logs: {{ meta.retention.log_years }} Jahre
- Audit-Trails: {{ meta.retention.audit_years }} Jahre

## 9. Referenzen

### Interne Dokumente
- `0240_Policy_Authentisierung_und_Passwoerter.md` - Übergeordnete Policy
- `0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md` - IAM Processes
- `0320_Policy_Logging_und_Monitoring.md` - Logging Policy

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.17** - Authentication information
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights
- **NIST SP 800-63B** - Digital Identity Guidelines (Authentication)
- **OWASP Authentication Cheat Sheet**

---

**Genehmigt durch:**  
{{ meta.ciso.name }}, CISO  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }}
