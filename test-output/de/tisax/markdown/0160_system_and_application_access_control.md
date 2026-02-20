
Document-ID: tisax-0160

Status: Draft
Classification: Internal

# System- und Anwendungszugriffskontrolle

**Dokument-ID:** TISAX-0160
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

## Zweck

Dieses Dokument definiert die Anforderungen für die Zugriffskontrolle auf Systeme und Anwendungen gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle IT-Systeme und Anwendungen von [TODO].

## Zugriffskontroll-Mechanismen

### Authentifizierung

**Anforderungen:**
- Eindeutige Benutzeridentifikation
- Sichere Authentifizierungsmethoden
- Multi-Faktor-Authentifizierung für kritische Systeme
- Verschlüsselte Übertragung von Credentials

**Methoden:**
- Passwort-basiert
- Token-basiert
- Zertifikat-basiert
- Biometrisch

### Autorisierung

**Prinzipien:**
- Least Privilege
- Need-to-Know
- Segregation of Duties
- Role-Based Access Control (RBAC)

**Implementierung:**
- Zentrale Autorisierungssysteme
- Konsistente Rechtevergabe
- Regelmäßige Überprüfung
- Audit-Logging

## System-Zugriffskontrolle

### Betriebssysteme

**Server:**
- Zugriff nur für autorisiertes Personal
- Privilegierte Konten getrennt
- Protokollierung aller Zugriffe
- Regelmäßige Patch-Management

**Workstations:**
- Standard-Benutzer ohne Admin-Rechte
- Verschlüsselte Festplatten
- Endpoint Protection
- Automatische Updates

### Netzwerkgeräte

**Anforderungen:**
- Separate Admin-Konten
- Verschlüsselte Management-Verbindungen
- Protokollierung aller Konfigurationsänderungen
- Regelmäßige Sicherheitsaudits

### Datenbanken

**Zugriffskontrolle:**
- Minimale Berechtigungen
- Verschlüsselte Verbindungen
- Audit-Logging aktiviert
- Regelmäßige Access Reviews

## Anwendungszugriffskontrolle

### Geschäftsanwendungen

**Authentifizierung:**
- Integration mit zentraler Authentifizierung (SSO)
- MFA für Remote-Zugriffe
- Session-Management
- Automatische Abmeldung bei Inaktivität

**Autorisierung:**
- Rollenbasierte Berechtigungen
- Funktionsbasierte Zugriffskontrolle
- Datenbasierte Zugriffskontrolle
- Regelmäßige Rezertifizierung

### Web-Anwendungen

**Sicherheitsmaßnahmen:**
- HTTPS obligatorisch
- Sichere Session-Verwaltung
- Input-Validierung
- Output-Encoding
- CSRF-Protection
- XSS-Prevention

### Cloud-Anwendungen

**Anforderungen:**
- Identity Federation
- Conditional Access Policies
- MFA obligatorisch
- Regelmäßige Überprüfung der Berechtigungen

## Sichere Anmeldeverfahren

### Passwort-Management

**Anforderungen:**
- Siehe Zugriffskontroll-Richtlinie
- Sichere Speicherung (Hashing mit Salt)
- Verschlüsselte Übertragung
- Passwort-Reset-Prozess

### Session-Management

**Anforderungen:**
- Sichere Session-IDs
- Session-Timeout bei Inaktivität
- Automatische Abmeldung
- Keine Session-Fixation

### Fehlerbehandlung

**Anforderungen:**
- Keine detaillierten Fehlermeldungen an Benutzer
- Protokollierung von Fehlern
- Generische Fehlermeldungen
- Schutz vor Brute-Force-Angriffen

## Privilegierte Zugriffskontrolle

### Administrative Zugriffe

**Anforderungen:**
- Separate privilegierte Konten
- Just-in-Time Access
- Session-Aufzeichnung
- Vier-Augen-Prinzip bei kritischen Aktionen

### Privileged Access Management (PAM)

**Funktionen:**
- Zentrale Verwaltung privilegierter Konten
- Automatische Passwortrotation
- Session-Monitoring
- Compliance-Reporting

## Zugriffskontrolle für Entwicklung

### Entwicklungsumgebungen

**Anforderungen:**
- Getrennt von Produktionsumgebungen
- Keine Produktionsdaten in Entwicklung
- Zugriffskontrolle basierend auf Rollen
- Versionskontrolle für Code

### Test-Umgebungen

**Anforderungen:**
- Anonymisierte Testdaten
- Zugriffskontrolle
- Protokollierung
- Regelmäßige Bereinigung

### Produktionsumgebungen

**Anforderungen:**
- Strenge Zugriffskontrolle
- Change Management erforderlich
- Umfassende Protokollierung
- Segregation of Duties

## Remote-Zugriff

### VPN

**Anforderungen:**
- MFA obligatorisch
- Verschlüsselte Verbindung
- Endpoint-Compliance-Check
- Protokollierung aller Verbindungen

### Remote Desktop

**Anforderungen:**
- Zugriff nur über VPN
- MFA erforderlich
- Session-Timeout
- Keine lokale Datenspeicherung

## Überwachung und Protokollierung

### Protokollierung

**Ereignisse:**
- Erfolgreiche und fehlgeschlagene Anmeldungen
- Berechtigungsänderungen
- Zugriffe auf sensible Daten
- Administrative Aktionen
- Privilegierte Zugriffe

### Monitoring

**Überwachung:**
- Echtzeit-Überwachung kritischer Systeme
- Automatische Alarmierung bei Anomalien
- Regelmäßige Log-Analysen
- SIEM-Integration

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **3.4.1**: Informationszugriffsbeschränkung
- **3.4.2**: Sichere Anmeldeverfahren
- **3.4.3**: Passwortverwaltungssystem
- **3.4.4**: Verwendung von Dienstprogrammen

### Assessment-Nachweise

- Zugriffskontroll-Konfigurationen
- Audit-Logs
- Access Review Berichte
- Prozessdokumentation

## Kennzahlen

[TODO] misst:
- Anzahl fehlgeschlagener Anmeldeversuche
- Anzahl privilegierter Zugriffe
- Durchschnittliche Session-Dauer
- Anzahl Zugriffsverletzungen

