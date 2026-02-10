# Zugriffskontrolle

**Dokument-ID:** PCI-0400  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents access control policies and procedures.
It aligns with PCI-DSS v4.0 Requirement 7 (Restrict Access to System Components and Cardholder Data by Business Need to Know).

Customization required:
- Define access control policies
- Document role-based access control (RBAC)
- List privileged access procedures
- Include access review processes
-->

## 1. Zweck

Dieses Dokument definiert die Zugriffskontrollrichtlinien für {{ meta.organization.name }} gemäß PCI-DSS Requirement 7.

### 1.1 Ziele

- **Need-to-Know-Prinzip:** Zugriff nur für berechtigte Personen
- **Least Privilege:** Minimale erforderliche Zugriffsrechte
- **Rollenbasierte Zugriffskontrolle:** RBAC-Implementierung
- **Compliance:** Erfüllung von PCI-DSS Requirement 7

### 1.2 Geltungsbereich

**Betroffene Systeme:**
- Alle CDE-Systeme
- Systeme mit Karteninhaberdaten
- Administrative Systeme
- Datenbanken mit CHD

## 2. Zugriffskontrollprinzipien

### 2.1 Need-to-Know

**Grundsatz:**
- Zugriff nur für Personen mit geschäftlicher Notwendigkeit
- Dokumentierte Begründung erforderlich
- Regelmäßige Überprüfung der Zugriffsrechte

### 2.2 Least Privilege

**Grundsatz:**
- Minimale erforderliche Berechtigungen
- Keine unnötigen Administratorrechte
- Zeitlich begrenzte privilegierte Zugriffe

### 2.3 Separation of Duties

**Grundsatz:**
- Trennung kritischer Funktionen
- Keine Einzelperson mit vollständiger Kontrolle
- Vier-Augen-Prinzip für kritische Operationen

## 3. Rollenbasierte Zugriffskontrolle (RBAC)

### 3.1 Definierte Rollen

| Rolle | Beschreibung | CDE-Zugriff | CHD-Zugriff |
|-------|--------------|-------------|-------------|
| Payment Administrator | Vollständige Payment-System-Administration | Ja | Ja (vollständig) |
| System Administrator | Server- und Netzwerkadministration | Ja | Nein |
| Database Administrator | Datenbankverwaltung | Ja | Ja (verschlüsselt) |
| Application Administrator | Anwendungsverwaltung | Ja | Nein |
| Security Administrator | Sicherheitssystem-Administration | Ja | Nein |
| Kassierer | POS-Bedienung | Eingeschränkt | Ja (nur Eingabe) |
| Support Mitarbeiter | Kundenservice | Eingeschränkt | Ja (nur Abfrage, maskiert) |
| Entwickler | Softwareentwicklung | Nein | Nein |
| Auditor | Compliance-Prüfung | Lesezugriff | Ja (nur Logs) |

### 3.2 Berechtigungsmatrix

| System/Ressource | Payment Admin | Sys Admin | DB Admin | App Admin | Kassierer | Support |
|------------------|---------------|-----------|----------|-----------|-----------|---------|
| Payment Gateway | RWX | RW | R | RW | - | R |
| CDE-Datenbank | RWX | R | RWX | R | - | R (maskiert) |
| POS-Terminal | RW | RW | - | RW | RW | R |
| Firewall | RW | RWX | - | - | - | - |
| SIEM | RW | RW | - | - | - | R |
| Backup-System | RW | RWX | RW | - | - | - |

**Legende:** R = Read, W = Write, X = Execute, - = Kein Zugriff

## 4. Zugriffsverwaltungsprozess

### 4.1 Zugriffsanforderung

**Prozess:**

1. **Antrag:** Formular mit Begründung
2. **Manager-Genehmigung:** Vorgesetzter genehmigt
3. **Security Review:** IT Security prüft
4. **CISO-Genehmigung:** Bei CDE-Zugriff erforderlich
5. **Provisionierung:** IT implementiert Zugriff
6. **Dokumentation:** Zugriff wird dokumentiert
7. **Benachrichtigung:** Benutzer wird informiert

**Genehmigungsmatrix:**

| Zugriffs-Typ | Genehmiger | Dokumentation |
|--------------|------------|---------------|
| CDE-Zugriff | CISO | Vollständig |
| CHD-Zugriff | CISO + Manager | Vollständig |
| Corporate-Zugriff | Manager | Standard |
| Temporärer Zugriff | IT Security | Mit Ablaufdatum |

### 4.2 Zugriffsänderung

**Prozess bei Rollenänderung:**

1. **Identifikation:** Rollenänderung erkannt
2. **Bewertung:** Neue Zugriffsanforderungen
3. **Genehmigung:** Wie bei Neuantrag
4. **Entzug:** Alte Berechtigungen entfernen
5. **Provisionierung:** Neue Berechtigungen erteilen
6. **Validierung:** Zugriff testen

### 4.3 Zugriffsentzug

**Prozess bei Ausscheiden:**

1. **Benachrichtigung:** HR informiert IT
2. **Sofortiger Entzug:** Alle Zugänge deaktivieren
3. **Rückgabe:** Hardware und Zugangsmittel
4. **Dokumentation:** Entzug dokumentieren
5. **Validierung:** Zugriff testen (sollte blockiert sein)

**Zeitrahmen:**
- Bei Kündigung: Sofort am letzten Arbeitstag
- Bei Versetzung: Innerhalb 24 Stunden
- Bei Verdacht: Sofort

## 5. Privilegierte Zugriffe

### 5.1 Administrative Accounts

**Anforderungen:**
- Separate Admin-Accounts (nicht für tägliche Arbeit)
- Starke Authentifizierung (MFA erforderlich)
- Vollständiges Logging aller Aktionen
- Regelmäßige Überprüfung

**Namenskonvention:**
- Standard-User: `vorname.nachname`
- Admin-User: `vorname.nachname-admin`
- Service-Account: `svc-servicename`

### 5.2 Privileged Access Management (PAM)

**PAM-System:** [TODO: Name des PAM-Systems]

**Funktionen:**
- Just-in-Time (JIT) Zugriff
- Session-Recording
- Passwort-Vaulting
- Automatische Passwortrotation

**Prozess:**
1. Admin beantragt privilegierten Zugriff
2. Genehmigung durch CISO (automatisch oder manuell)
3. Zeitlich begrenzter Zugriff gewährt
4. Session wird aufgezeichnet
5. Automatischer Entzug nach Ablauf

### 5.3 Emergency Access

**Break-Glass-Accounts:**
- Nur für Notfälle
- Passwort in versiegeltem Umschlag
- Verwendung muss dokumentiert werden
- Passwort nach Verwendung ändern

**Prozess:**
1. Notfall identifiziert
2. Umschlag öffnen (mit Zeugen)
3. Zugriff verwenden
4. Incident dokumentieren
5. Passwort sofort ändern
6. CISO informieren

## 6. Zugriffskontrolle für Karteninhaberdaten

### 6.1 CHD-Zugriffsbeschränkungen

**Vollständiger PAN-Zugriff:**
- Nur für autorisierte Rollen
- Dokumentierte Business-Begründung
- CISO-Genehmigung erforderlich
- Vollständiges Logging

**Maskierter PAN-Zugriff:**
- Nur letzte 4 Ziffern sichtbar
- Für Support und Reporting
- Standard-Genehmigung ausreichend

**Kein PAN-Zugriff:**
- Alle anderen Benutzer
- Entwickler (nur Testdaten)
- Externe Dienstleister (ohne Notwendigkeit)

### 6.2 Datenmaskierung

**Maskierungsregeln:**
- PAN: Nur erste 6 und letzte 4 Ziffern (z.B., 123456******1234)
- Ablaufdatum: Vollständig maskiert
- CVV: Niemals anzeigen (darf nicht gespeichert werden)
- Karteninhaber-Name: Teilweise maskiert (z.B., Max M******)

**Ausnahmen:**
- Payment-Administratoren (vollständiger Zugriff)
- Nur mit CISO-Genehmigung
- Vollständiges Logging

## 7. Zugriffskontrolle für Anwendungen

### 7.1 Anwendungsberechtigungen

**Berechtigungsmodell:**
- Rollenbasierte Berechtigungen
- Granulare Funktionsrechte
- Keine Shared Accounts
- Eindeutige Benutzer-IDs

**Beispiel (Payment Application):**

| Funktion | Payment Admin | Kassierer | Support |
|----------|---------------|-----------|---------|
| Transaktion durchführen | Ja | Ja | Nein |
| Transaktion stornieren | Ja | Eingeschränkt | Nein |
| Berichte anzeigen | Ja | Nein | Ja (maskiert) |
| Konfiguration ändern | Ja | Nein | Nein |
| Benutzer verwalten | Ja | Nein | Nein |

### 7.2 API-Zugriffskontrolle

**API-Authentifizierung:**
- API-Keys mit Ablaufdatum
- OAuth 2.0 für externe APIs
- Mutual TLS für kritische APIs
- Rate Limiting

**API-Autorisierung:**
- Scope-basierte Berechtigungen
- Minimale erforderliche Scopes
- Logging aller API-Aufrufe

## 8. Zugriffskontrolle für Datenbanken

### 8.1 Datenbank-Berechtigungen

**Berechtigungsmodell:**
- Separate DB-Accounts pro Anwendung
- Keine Shared Accounts
- Least Privilege für Anwendungen
- DBA-Zugriff nur für Administration

**Beispiel:**

| Account | Typ | Berechtigungen | Zweck |
|---------|-----|----------------|-------|
| app_payment | Application | SELECT, INSERT, UPDATE | Payment-Anwendung |
| app_reporting | Application | SELECT | Reporting |
| dba_admin | DBA | ALL | Administration |
| backup_user | Service | SELECT | Backup |

### 8.2 Verschlüsselte Spalten

**CHD-Spalten:**
- PAN: Verschlüsselt (AES-256)
- Zugriff nur über Entschlüsselungsfunktion
- Logging aller Entschlüsselungen
- Nur autorisierte Accounts

## 9. Zugriffskontrolle für Netzwerk

### 9.1 Netzwerkzugriff

**Zugriffsmethoden:**
- VPN für Remote-Zugriff
- Jump Server für Admin-Zugriff
- Keine direkte Internet-Verbindung zu CDE

**Authentifizierung:**
- Multi-Faktor-Authentifizierung (MFA)
- Zertifikatsbasierte Authentifizierung
- Starke Passwörter

### 9.2 Netzwerksegmentierung

**Zugriffskontrolle zwischen Segmenten:**
- Firewall-Regeln
- ACLs auf Switches
- Micro-Segmentierung

## 10. Zugriffskontrolle für physischen Zugang

### 10.1 Rechenzentrum

**Zugriffskontrolle:**
- Badge-System
- Biometrische Authentifizierung
- Begleitpflicht für Besucher
- Logging aller Zutritte

**Autorisierte Personen:**
- Datacenter-Personal
- Autorisierte Administratoren
- Wartungspersonal (mit Begleitung)

### 10.2 Büroräume mit CDE-Zugriff

**Zugriffskontrolle:**
- Gesperrte Räume
- Badge-Zugang
- Besucherprotokoll

## 11. Zugriffskontrolle für Dienstleister

### 11.1 Dienstleister-Zugriff

**Anforderungen:**
- Separate Accounts für jeden Dienstleister
- Zeitlich begrenzter Zugriff
- Vollständiges Logging
- PCI-DSS AOC erforderlich

**Genehmigungsprozess:**
1. Dienstleister-Vertrag mit PCI-Klauseln
2. AOC-Validierung
3. CISO-Genehmigung
4. Zeitlich begrenzter Zugriff
5. Überwachung während Zugriff

### 11.2 Remote-Support

**Prozess:**
- Nur nach Genehmigung
- Session-Recording
- Begleitung durch internen Admin
- Sofortiger Entzug nach Abschluss

## 12. Zugriffskontrolle-Überwachung

### 12.1 Logging

**Geloggte Ereignisse:**
- Erfolgreiche Anmeldungen
- Fehlgeschlagene Anmeldungen
- Privilegierte Aktionen
- Zugriff auf CHD
- Berechtigungsänderungen

**Log-Retention:** [TODO: 90 Tage online, 1 Jahr Archiv]

### 12.2 Alerting

| Alert | Bedingung | Schweregrad | Benachrichtigung |
|-------|-----------|-------------|------------------|
| Mehrfache fehlgeschlagene Logins | >5 in 15 Min | Mittel | SOC |
| Admin-Login außerhalb Geschäftszeiten | Nach 22:00 Uhr | Mittel | SOC + Manager |
| CHD-Zugriff | Jeder Zugriff | Niedrig | SIEM |
| Berechtigungsänderung | Jede Änderung | Mittel | IT Security |

## 13. Zugriffskontrolle-Reviews

### 13.1 Quartalsweise Überprüfung

**Überprüfungsprozess:**

1. **Benutzer-Review:** Alle Benutzer mit CDE-Zugriff
2. **Berechtigungs-Review:** Alle Berechtigungen validieren
3. **Inaktive Accounts:** Identifizieren und deaktivieren
4. **Dokumentation:** Ergebnisse dokumentieren
5. **Genehmigung:** CISO-Bestätigung

**Letzte Überprüfung:** [TODO: Datum]  
**Nächste Überprüfung:** [TODO: Datum]  
**Verantwortlich:** [TODO: IT Security Team]

### 13.2 Rezertifizierung

**Jährliche Rezertifizierung:**
- Alle Benutzer mit CDE-Zugriff
- Manager bestätigt Business-Notwendigkeit
- IT Security validiert Berechtigungen
- CISO genehmigt

## 14. Compliance-Validierung

### 14.1 Validierungsaktivitäten

**Quartalsweise:**
- Zugriffskontrolle-Review
- Inaktive Account-Cleanup
- Berechtigungsdokumentation

**Jährlich:**
- Vollständige Rezertifizierung
- Penetrationstest
- Compliance-Audit

### 14.2 Validierungsdokumentation

**Erforderliche Nachweise:**
- Zugriffskontrollrichtlinien
- Berechtigungsmatrix
- Genehmigungsnachweise
- Review-Protokolle
- Rezertifizierungsnachweise

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
