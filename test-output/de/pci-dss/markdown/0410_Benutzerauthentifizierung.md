# Benutzerauthentifizierung

**Dokument-ID:** PCI-0410
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---



## 1. Zweck

Dieses Dokument definiert die Authentifizierungsrichtlinien für AdminSend GmbH gemäß PCI-DSS Requirement 8.

### 1.1 Ziele

- **Eindeutige Identifikation:** Jeder Benutzer eindeutig identifizierbar
- **Starke Authentifizierung:** Multi-Faktor-Authentifizierung (MFA)
- **Sichere Passwörter:** Passwortrichtlinien durchsetzen
- **Compliance:** Erfüllung von PCI-DSS Requirement 8

### 1.2 Geltungsbereich

**Betroffene Systeme:**
- Alle CDE-Systeme
- Administrative Systeme
- Anwendungen mit CHD-Zugriff
- Remote-Zugriffssysteme

## 2. Benutzeridentifikation

### 2.1 Eindeutige Benutzer-IDs

**Anforderungen:**
- Jeder Benutzer hat eindeutige ID
- Keine Shared Accounts
- Keine Generic Accounts (außer dokumentierte Ausnahmen)
- Benutzer-ID darf nicht wiederverwendet werden

**Namenskonvention:**
- Format: `vorname.nachname`
- Bei Duplikaten: `vorname.nachname2`
- Service-Accounts: `svc-servicename`
- Admin-Accounts: `vorname.nachname-admin`

### 2.2 Verbotene Account-Typen

**Nicht erlaubt:**
- Shared Accounts (mehrere Personen, ein Account)
- Generic Accounts (z.B., "admin", "user", "test")
- Group Accounts
- Vendor Default Accounts (müssen deaktiviert werden)

**Ausnahmen:**
- Notfall-Accounts (Break-Glass) - dokumentiert
- Service-Accounts - dokumentiert und überwacht
- Konsolen-Zugriff (nur mit Logging)

## 3. Authentifizierungsmethoden

### 3.1 Multi-Faktor-Authentifizierung (MFA)

**MFA erforderlich für:**
- Alle CDE-Zugriffe
- Administrative Zugriffe
- Remote-Zugriffe (VPN, Jump Server)
- Privilegierte Accounts
- Zugriff auf CHD

**MFA-Faktoren:**

1. **Etwas, das Sie wissen:**
   - Passwort
   - PIN

2. **Etwas, das Sie haben:**
   - Hardware-Token
   - Software-Token (Authenticator App)
   - Smart Card
   - SMS (nur als Backup)

3. **Etwas, das Sie sind:**
   - Biometrie (Fingerabdruck, Gesichtserkennung)

**MFA-Implementierung:**
- Mindestens 2 verschiedene Faktoren
- Faktoren müssen unabhängig sein
- MFA-System: [TODO: Name des MFA-Systems]

### 3.2 Passwort-Authentifizierung

**Passwortanforderungen:**

- **Mindestlänge:** 12 Zeichen (15 für Admin-Accounts)
- **Komplexität:**
  - Großbuchstaben (A-Z)
  - Kleinbuchstaben (a-z)
  - Ziffern (0-9)
  - Sonderzeichen (!@#$%^&*)
- **Keine Wörterbuch-Wörter**
- **Keine persönlichen Informationen** (Name, Geburtsdatum, etc.)
- **Keine Wiederholung** der letzten 4 Passwörter

**Passwortänderung:**
- Alle 90 Tage für Standard-Benutzer
- Alle 90 Tage für Admin-Accounts
- Sofort bei Verdacht auf Kompromittierung
- Bei Erstanmeldung

**Passwort-Speicherung:**
- Nur als Hash (bcrypt, PBKDF2, Argon2)
- Niemals im Klartext
- Salt für jeden Hash
- Keine reversible Verschlüsselung

### 3.3 Zertifikatsbasierte Authentifizierung

**Verwendung:**
- Server-zu-Server-Kommunikation
- API-Authentifizierung
- VPN-Zugriff (zusätzlich zu MFA)

**Anforderungen:**
- Zertifikate von vertrauenswürdiger CA
- Regelmäßige Erneuerung
- Widerrufsprüfung (CRL/OCSP)
- Sichere Schlüsselspeicherung

## 4. Account-Management

### 4.1 Account-Erstellung

**Prozess:**
1. Genehmigter Zugriffsantrag
2. Eindeutige Benutzer-ID erstellen
3. Temporäres Passwort generieren
4. MFA-Registrierung
5. Benutzer benachrichtigen
6. Passwortänderung bei Erstanmeldung erzwingen

### 4.2 Account-Deaktivierung

**Automatische Deaktivierung:**
- Nach 90 Tagen Inaktivität
- Bei Ausscheiden des Mitarbeiters
- Bei Rollenänderung (alter Account)

**Manuelle Deaktivierung:**
- Bei Sicherheitsvorfällen
- Bei Verdacht auf Kompromittierung
- Auf Anfrage des Managers

**Prozess:**
1. Account deaktivieren (nicht löschen)
2. Alle Sessions beenden
3. Zugriff validieren (sollte blockiert sein)
4. Dokumentieren

### 4.3 Account-Löschung

**Zeitrahmen:**
- 90 Tage nach Deaktivierung
- Nach Abschluss von Audits/Untersuchungen
- Nach Aufbewahrungspflicht

**Prozess:**
1. Bestätigung, dass Account nicht mehr benötigt
2. Backup der Account-Daten (falls erforderlich)
3. Account löschen
4. Dokumentieren

## 5. Passwort-Management

### 5.1 Passwort-Reset

**Self-Service-Reset:**
- Über Identity Management System
- Nach erfolgreicher Identitätsprüfung
- Sicherheitsfragen oder E-Mail-Verifizierung
- MFA-Verifizierung

**Helpdesk-Reset:**
- Identitätsprüfung erforderlich
- Temporäres Passwort
- Passwortänderung bei nächster Anmeldung erzwingen
- Dokumentation des Resets

### 5.2 Passwort-Sperrung

**Account-Sperrung nach:**
- 6 fehlgeschlagenen Anmeldeversuchen
- Sperrung für 30 Minuten
- Oder manuelle Entsperrung durch Admin

**Entsperrung:**
- Automatisch nach 30 Minuten
- Oder durch Helpdesk nach Identitätsprüfung
- Dokumentation der Entsperrung

### 5.3 Passwort-Vault

**Für privilegierte Passwörter:**
- Zentrale Passwort-Vault-Lösung
- Automatische Passwortrotation
- Check-out/Check-in-Prozess
- Session-Recording
- Vollständiges Logging

**Vault-System:** [TODO: Name des Vault-Systems]

## 6. Session-Management

### 6.1 Session-Timeouts

**Inaktivitäts-Timeout:**
- 15 Minuten für CDE-Systeme
- 30 Minuten für Corporate-Systeme
- 5 Minuten für privilegierte Sessions

**Maximale Session-Dauer:**
- 8 Stunden für Standard-Benutzer
- 4 Stunden für Admin-Sessions
- Re-Authentifizierung erforderlich

### 6.2 Session-Sicherheit

**Anforderungen:**
- Eindeutige Session-IDs
- Session-ID-Rotation nach Login
- Sichere Session-Cookies (HttpOnly, Secure, SameSite)
- Session-Invalidierung bei Logout
- Keine Session-IDs in URLs

### 6.3 Concurrent Sessions

**Beschränkungen:**
- Maximal 2 gleichzeitige Sessions pro Benutzer
- Nur 1 privilegierte Session gleichzeitig
- Warnung bei neuer Session
- Option zum Beenden alter Sessions

## 7. Remote-Authentifizierung

### 7.1 VPN-Zugriff

**Authentifizierung:**
- Benutzername + Passwort
- Plus MFA (Hardware-Token oder Authenticator App)
- Zertifikatsbasierte Authentifizierung (optional)

**Autorisierung:**
- Nur autorisierte Benutzer
- Zugriff auf spezifische Netzwerksegmente
- Vollständiges Logging

### 7.2 Jump Server

**Authentifizierung:**
- MFA erforderlich
- Privilegierte Accounts
- Session-Recording
- Zeitlich begrenzter Zugriff

**Zugriffskontrolle:**
- Nur von autorisierten Quell-IPs
- Nur zu autorisierten Ziel-Systemen
- Vollständiges Logging

## 8. Anwendungs-Authentifizierung

### 8.1 Web-Anwendungen

**Authentifizierung:**
- Benutzername + Passwort
- MFA für CDE-Anwendungen
- Session-Management
- HTTPS erforderlich

**Sicherheitsmaßnahmen:**
- Schutz vor Brute-Force (Rate Limiting)
- CAPTCHA nach mehreren Fehlversuchen
- Account-Sperrung
- Sichere Passwort-Speicherung

### 8.2 API-Authentifizierung

**Methoden:**
- API-Keys (mit Ablaufdatum)
- OAuth 2.0
- JWT (JSON Web Tokens)
- Mutual TLS

**Anforderungen:**
- Keine API-Keys in Code
- Rotation von API-Keys
- Scope-basierte Autorisierung
- Rate Limiting

## 9. Service-Account-Management

### 9.1 Service-Accounts

**Anforderungen:**
- Eindeutige Service-Account-IDs
- Dokumentierte Verwendung
- Starke Passwörter (32+ Zeichen)
- Regelmäßige Passwortrotation (90 Tage)
- Keine interaktiven Logins

**Namenskonvention:**
- Format: `svc-servicename`
- Beispiel: `svc-payment-gateway`

### 9.2 Service-Account-Überwachung

**Monitoring:**
- Alle Service-Account-Aktivitäten loggen
- Alerts bei ungewöhnlichen Aktivitäten
- Regelmäßige Überprüfung der Verwendung
- Deaktivierung ungenutzter Accounts

## 10. Authentifizierungs-Logging

### 10.1 Geloggte Ereignisse

**Erfolgreiche Authentifizierung:**
- Benutzer-ID
- Zeitstempel
- Quell-IP-Adresse
- Ziel-System
- Authentifizierungsmethode

**Fehlgeschlagene Authentifizierung:**
- Benutzer-ID (oder Versuch)
- Zeitstempel
- Quell-IP-Adresse
- Ziel-System
- Fehlergrund

**Weitere Ereignisse:**
- Passwortänderungen
- Account-Sperrungen
- Account-Entsperrungen
- MFA-Registrierung
- Privilegierte Aktionen

### 10.2 Log-Retention

**Aufbewahrung:**
- 90 Tage online
- 1 Jahr Archiv
- Unveränderlich (WORM)

**Log-Forwarding:**
- An SIEM-System
- Echtzeitübertragung
- Verschlüsselte Übertragung

## 11. Authentifizierungs-Monitoring

### 11.1 Alerting

| Alert | Bedingung | Schweregrad | Benachrichtigung |
|-------|-----------|-------------|------------------|
| Mehrfache fehlgeschlagene Logins | >5 in 15 Min | Mittel | SOC |
| Admin-Login außerhalb Geschäftszeiten | Nach 22:00 Uhr | Mittel | SOC + Manager |
| MFA-Fehler | >3 Fehler | Niedrig | SOC |
| Account-Sperrung | Jede Sperrung | Niedrig | Helpdesk |
| Privilegierter Zugriff | Jeder Zugriff | Niedrig | SIEM |
| Passwortänderung | Außerhalb Geschäftszeiten | Niedrig | SIEM |

### 11.2 Anomalie-Erkennung

**Überwachung:**
- Ungewöhnliche Login-Zeiten
- Ungewöhnliche Quell-IPs
- Geografische Anomalien
- Mehrfache gleichzeitige Logins
- Privilegierte Zugriffe

## 12. Vendor Default Accounts

### 12.1 Default Account Management

**Anforderungen:**
- Alle Default Accounts identifizieren
- Default Accounts deaktivieren oder löschen
- Falls erforderlich: Passwort ändern
- Dokumentation aller Default Accounts

**Beispiele:**
- admin/admin
- root/root
- Administrator/password
- sa (SQL Server)

### 12.2 Default Account Inventory

| System | Default Account | Status | Aktion |
|--------|-----------------|--------|--------|
| [TODO: System 1] | admin | Deaktiviert | Gelöscht |
| [TODO: System 2] | root | Aktiv | Passwort geändert |
| [TODO: System 3] | Administrator | Deaktiviert | Umbenannt |

## 13. Authentifizierungs-Testing

### 13.1 Penetrationstests

**Jährlich:**
- Authentifizierungsmechanismen testen
- Brute-Force-Angriffe simulieren
- MFA-Bypass-Versuche
- Session-Management-Tests

### 13.2 Vulnerability Scans

**Quartalsweise:**
- Schwache Passwörter identifizieren
- Default Accounts identifizieren
- Authentifizierungs-Schwachstellen

## 14. Compliance-Validierung

### 14.1 Validierungsaktivitäten

**Quartalsweise:**
- Passwortrichtlinien-Compliance
- MFA-Implementierung validieren
- Inaktive Accounts identifizieren
- Default Accounts überprüfen

**Jährlich:**
- Vollständige Authentifizierungs-Audit
- Penetrationstest
- Compliance-Assessment

### 14.2 Validierungsdokumentation

**Erforderliche Nachweise:**
- Authentifizierungsrichtlinien
- MFA-Konfiguration
- Passwortrichtlinien-Konfiguration
- Account-Management-Protokolle
- Penetrationstest-Berichte


