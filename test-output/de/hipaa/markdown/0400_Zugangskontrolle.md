# Zugangskontrolle

**Dokument-ID:** HIPAA-0400
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

Dieses Dokument beschreibt die technischen Schutzmaßnahmen zur Zugangskontrolle für AdminSend GmbH, um technische Richtlinien und Verfahren für elektronische Informationssysteme zu implementieren, die ePHI verwalten, um nur autorisierten Personen oder Softwareprogrammen Zugang zu gewähren.

### 1.1 HIPAA-Anforderung

**Standard:** §164.312(a)(1) - Access Control (Erforderlich)

**Implementierungsspezifikationen:**
- §164.312(a)(2)(i) - Eindeutige Benutzeridentifikation (Erforderlich)
- §164.312(a)(2)(ii) - Notfallzugangsverfahren (Erforderlich)
- §164.312(a)(2)(iii) - Automatische Abmeldung (Adressierbar)
- §164.312(a)(2)(iv) - Verschlüsselung und Entschlüsselung (Adressierbar)

## 2. Eindeutige Benutzeridentifikation

### 2.1 Benutzer-ID-Anforderungen

**Anforderung:** Zuweisung eines eindeutigen Namens und/oder einer Nummer zur Identifizierung und Verfolgung der Benutzeridentität.

**Benutzer-ID-Standards:**
- Eindeutig für jeden einzelnen Benutzer
- Nicht zwischen Benutzern geteilt
- Nach Kündigung nicht wiederverwendet
- Format: [TODO: vorname.nachname, Mitarbeiter-ID usw.]
- Mindestlänge: [TODO: 6 Zeichen]

**Verbotene Praktiken:**
- Gemeinsam genutzte Konten
- Generische Konten (außer für spezifische genehmigte Zwecke)
- Standardkonten (müssen deaktiviert oder umbenannt werden)
- Gastkonten (müssen deaktiviert werden)

### 2.2 Benutzerkontenverwaltung

**Kontoerstellungsprozess:**
1. Manager reicht Zugriffsanfrage ein
2. HR überprüft Beschäftigungsstatus
3. Security Officer genehmigt basierend auf Rolle
4. IT erstellt eindeutiges Benutzerkonto
5. Benutzer über Kontoerstellung benachrichtigt
6. Benutzer schließt erste Anmeldung und Passworteinrichtung ab

**Kontotypen:**
| Kontotyp | Zweck | Erforderliche Genehmigung | Überwachung |
|----------|-------|---------------------------|-------------|
| Standardbenutzer | Reguläres Mitglied | Manager | Standard |
| Privilegierter Benutzer | Systemadministration | IT-Manager + Security Officer | Erweitert |
| Dienstkonto | Automatisierte Prozesse | Security Officer | Erweitert |
| Notfallzugang | Break-Glass-Zugang | Security Officer | Sofortige Überprüfung |

### 2.3 Authentifizierungsmethoden

**Primäre Authentifizierung:**
- Benutzername und Passwort
- Mindestpasswortanforderungen:
  - Länge: [TODO: 12 Zeichen Minimum]
  - Komplexität: Groß-, Kleinbuchstaben, Zahl, Sonderzeichen
  - Historie: [TODO: 12 vorherige Passwörter gespeichert]
  - Alter: Maximum [TODO: 90 Tage], Minimum [TODO: 1 Tag]
  - Sperrung: [TODO: 5 fehlgeschlagene Versuche], Sperrdauer [TODO: 30 Minuten]

**Multi-Faktor-Authentifizierung (MFA):**
- Erforderlich für: Fernzugriff, privilegierte Konten, ePHI-Zugriff aus nicht vertrauenswürdigen Netzwerken
- Methoden: SMS-Code, Authenticator-App, Hardware-Token, biometrisch
- Backup-Codes für MFA-Wiederherstellung bereitgestellt

**Single Sign-On (SSO):**
- Zentralisierte Authentifizierung
- Reduziert Passwortmüdigkeit
- Audit-Trail des Zugriffs
- Integration mit MFA

## 3. Notfallzugangsverfahren

### 3.1 Notfallzugangsdefinition

**Notfallsituationen:**
- Systemausfall, der normale Authentifizierung verhindert
- Naturkatastrophe
- Cyberangriff, der sofortige Reaktion erfordert
- Lebensbedrohliche Patientensituation, die sofortigen ePHI-Zugriff erfordert
- Kritische Systemwartung

### 3.2 Break-Glass-Konten

**Break-Glass-Konto-Eigenschaften:**
- Hochprivilegierter Zugriff
- Nur in Notfällen verwendet
- Anmeldedaten gesichert (versiegelter Umschlag, Passworttresor)
- Sofortige Benachrichtigung bei Verwendung
- Automatische Protokollierung aller Aktivitäten
- Sofortige Überprüfung erforderlich

**Break-Glass-Konto-Inventar:**
| Konto-ID | System | Zugriffsstufe | Anmeldedatenspeicherort | Zuletzt verwendet | Überprüft von |
|----------|--------|---------------|-------------------------|-------------------|---------------|
| [TODO: BG-001] | Active Directory | Domain Admin | [TODO: Sicherer Tresor] | [TODO: Datum] | [TODO: Security Officer] |
| [TODO: BG-002] | EHR-System | System Admin | [TODO: Sicherer Tresor] | [TODO: Datum] | [TODO: Security Officer] |

### 3.3 Notfallzugangsprozess

**Prozessschritte:**
1. **Feststellung:** Notfallsituation festgestellt
2. **Autorisierung:** Security Officer oder Beauftragter autorisiert Notfallzugang
3. **Zugriff:** Break-Glass-Anmeldedaten verwenden
4. **Protokollierung:** Alle Aktivitäten automatisch protokolliert
5. **Benachrichtigung:** Security Officer sofort benachrichtigt
6. **Überwachung:** Echtzeitüberwachung der Notfallzugriffsaktivitäten
7. **Überprüfung:** Sofortige Überprüfung nach Zugriff
8. **Dokumentation:** Notfall, ergriffene Maßnahmen, Begründung dokumentieren
9. **Anmeldedatenrotation:** Break-Glass-Anmeldedaten nach Verwendung ändern

**Notfallzugriffsprotokoll:**
| Datum/Zeit | Benutzer | System | Grund | Autorisiert von | Ergriffene Maßnahmen | Überprüfungsdatum |
|------------|----------|--------|-------|-----------------|----------------------|-------------------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Automatische Abmeldung

### 4.1 Anforderungen an automatische Abmeldung

**Anforderung:** Implementierung elektronischer Verfahren, die eine elektronische Sitzung nach einer vorbestimmten Zeit der Inaktivität beenden.

**Begründung:** Unbefugten Zugriff auf ePHI verhindern, wenn Arbeitsplatz unbeaufsichtigt gelassen wird.

### 4.2 Timeout-Einstellungen

**Inaktivitäts-Timeouts:**
| System/Anwendung | Timeout-Zeitraum | Aktion | Override erlaubt |
|------------------|------------------|--------|------------------|
| Arbeitsplätze | [TODO: 15 Minuten] | Bildschirmsperre | Nein |
| EHR-System | [TODO: 10 Minuten] | Sitzungs-Timeout | Nein |
| Webanwendungen | [TODO: 20 Minuten] | Sitzungs-Timeout | Nein |
| VPN | [TODO: 30 Minuten] | Trennen | Nein |
| Mobile Geräte | [TODO: 5 Minuten] | Bildschirmsperre | Nein |

**Timeout-Aktionen:**
- **Bildschirmsperre:** Passwort zum Entsperren erforderlich, Sitzung bleibt aktiv
- **Sitzungs-Timeout:** Beendet Sitzung, erneute Authentifizierung erforderlich
- **Trennen:** Beendet Netzwerkverbindung

### 4.3 Implementierung

**Technische Implementierung:**
- Gruppenrichtlinie (Windows)
- Konfigurationsprofile (macOS, iOS)
- Anwendungsebenen-Timeouts
- Netzwerkebenen-Timeouts (VPN, Firewall)

**Benutzerbenachrichtigung:**
- Warnung vor Timeout (z.B. 2 Minuten)
- Klare Anzeige des gesperrten Zustands
- Anweisungen zum Entsperren

## 5. Verschlüsselung und Entschlüsselung

### 5.1 Verschlüsselungsanforderungen

**Anforderung:** Implementierung eines Mechanismus zur Verschlüsselung und Entschlüsselung von ePHI.

**Verschlüsselungsanwendungsfälle:**
- ePHI im Ruhezustand (gespeicherte Daten)
- ePHI in Übertragung (übertragene Daten)
- Backup-Medien
- Mobile Geräte
- Wechselmedien
- E-Mail mit ePHI

### 5.2 Verschlüsselungsstandards

**Genehmigte Verschlüsselungsalgorithmen:**
- **Symmetrisch:** AES-256, AES-128
- **Asymmetrisch:** RSA-2048 oder höher, ECC
- **Hashing:** SHA-256, SHA-512
- **TLS:** TLS 1.2 oder höher

**Verbotene Algorithmen:**
- DES, 3DES
- MD5, SHA-1
- SSL, TLS 1.0, TLS 1.1
- RC4

### 5.3 Verschlüsselung im Ruhezustand

**Vollständige Festplattenverschlüsselung:**
- Alle Arbeitsplätze und Laptops: [TODO: BitLocker, FileVault, LUKS]
- Alle Server mit ePHI: [TODO: BitLocker, dm-crypt]
- Alle mobilen Geräte: [TODO: Native Geräteverschlüsselung]

**Datenbankverschlüsselung:**
- Transparent Data Encryption (TDE) für Datenbanken
- Spaltenebenen-Verschlüsselung für sensible Felder
- Verschlüsselungsschlüsselverwaltung

**Datei-/Ordnerverschlüsselung:**
- Verschlüsselte Dateisysteme
- Verschlüsselte Container
- Dokumentenebenen-Verschlüsselung

### 5.4 Verschlüsselung in Übertragung

**Netzwerkverschlüsselung:**
- TLS 1.2+ für allen Webverkehr
- VPN für Fernzugriff (IPsec, SSL VPN)
- Verschlüsselte E-Mail (S/MIME, PGP)
- SFTP/SCP für Dateiübertragungen (kein FTP)
- HTTPS für alle Webanwendungen

**Drahtlosverschlüsselung:**
- WPA3 oder WPA2-Enterprise
- Kein WEP oder offene Netzwerke
- Zertifikatbasierte Authentifizierung

### 5.5 Schlüsselverwaltung

**Schlüsselverwaltungs-Lebenszyklus:**
1. **Generierung:** Kryptografisch sichere Zufallsgenerierung
2. **Verteilung:** Sichere Schlüsselverteilungsmechanismen
3. **Speicherung:** Hardware Security Module (HSM) oder sicherer Schlüsseltresor
4. **Rotation:** Regelmäßiger Schlüsselrotationsplan
5. **Backup:** Sichere Sicherung von Verschlüsselungsschlüsseln
6. **Vernichtung:** Sichere Vernichtung, wenn nicht mehr benötigt

**Schlüsselverwaltungssystem:**
- Zentralisierte Schlüsselverwaltung
- Zugriffskontrollen auf Schlüssel
- Audit-Protokollierung des Schlüsselzugriffs
- Schlüsselhinterlegungs-/Wiederherstellungsverfahren

**Schlüsselrotationsplan:**
| Schlüsseltyp | Rotationshäufigkeit | Verantwortlich |
|--------------|---------------------|----------------|
| Festplattenverschlüsselungsschlüssel | [TODO: Jährlich] | IT Security |
| Datenbankverschlüsselungsschlüssel | [TODO: Jährlich] | Database Admin |
| TLS-Zertifikate | [TODO: Jährlich oder gemäß Anbieter] | IT Security |
| VPN-Schlüssel | [TODO: Vierteljährlich] | Network Admin |

## 6. Zugriffskontrolllisten (ACLs)

### 6.1 ACL-Verwaltung

**ACL-Prinzipien:**
- Geringste Privilegien
- Need-to-know
- Aufgabentrennung
- Defense in Depth

**ACL-Komponenten:**
- Benutzer-/Gruppenidentität
- Ressource (Datei, Ordner, Anwendung, Datenbank)
- Berechtigungen (Lesen, Schreiben, Ausführen, Löschen)
- Bedingungen (Zeit, Standort, Gerät)

### 6.2 Berechtigungsstufen

**Standard-Berechtigungsstufen:**
| Stufe | Beschreibung | Typische Rollen |
|-------|--------------|-----------------|
| Kein Zugriff | Keine Berechtigungen | Standard für alle Benutzer |
| Lesen | Nur Ansicht | Auditoren, Nur-Lese-Benutzer |
| Lesen/Schreiben | Ansicht und Änderung | Standardbenutzer |
| Vollzugriff | Alle Berechtigungen | Administratoren, Eigentümer |

### 6.3 ACL-Überprüfung

**Überprüfungsprozess:**
- **Häufigkeit:** Vierteljährlich
- **Umfang:** Alle ePHI-Ressourcen
- **Prüfer:** Ressourceneigentümer + Security Officer
- **Maßnahmen:** Unnötige Berechtigungen entfernen, für Rollenänderungen aktualisieren

## 7. Privileged Access Management (PAM)

### 7.1 Definition privilegierter Konten

**Privilegierte Konten:**
- Systemadministratoren
- Datenbankadministratoren
- Netzwerkadministratoren
- Anwendungsadministratoren
- Sicherheitsadministratoren

**Eigenschaften privilegierten Zugriffs:**
- Erhöhte Berechtigungen
- Zugriff auf sensible Systeme
- Fähigkeit zur Änderung von Sicherheitskontrollen
- Zugriff auf alle ePHI

### 7.2 PAM-Kontrollen

**PAM-Anforderungen:**
- Trennung privilegierter Konten von Standardkonten
- Just-in-Time (JIT) Privilegienerweiterung
- Sitzungsaufzeichnung für privilegierten Zugriff
- Erweiterte Überwachung und Alarmierung
- Regelmäßige Zugriffsüberprüfungen
- MFA für privilegierten Zugriff erforderlich

**PAM-Lösung:** [TODO: CyberArk, BeyondTrust, Thycotic usw.]

## 8. Überwachung und Auditing

### 8.1 Zugriffsüberwachung

**Überwachungsaktivitäten:**
- Fehlgeschlagene Anmeldeversuche
- Erfolgreiche Anmeldungen (insbesondere außerhalb der Geschäftszeiten)
- Nutzung privilegierter Konten
- Nutzung von Notfallzugang
- Berechtigungsänderungen
- Kontoerstellung/-löschung
- Passwortzurücksetzungen

**Überwachungstools:**
- SIEM (Security Information and Event Management)
- Log-Aggregation und -Analyse
- User Behavior Analytics (UBA)
- Automatisierte Alarmierung

### 8.2 Zugriffs-Auditing

**Audit-Aktivitäten:**
- Benutzerzugriffsüberprüfungen
- Privilegierte Zugriffsüberprüfungen
- ACL-Überprüfungen
- Inaktive Kontoüberprüfungen
- Verwaiste Kontoüberprüfungen

**Audit-Häufigkeit:**
| Aktivität | Häufigkeit | Verantwortlich |
|-----------|-----------|----------------|
| Benutzerzugriffsüberprüfung | Vierteljährlich | Manager + Security Officer |
| Privilegierte Zugriffsüberprüfung | Monatlich | Security Officer |
| ACL-Überprüfung | Vierteljährlich | Ressourceneigentümer |
| Inaktive Kontoüberprüfung | Monatlich | IT + HR |

## 9. Dokumentation und Aufzeichnungen

### 9.1 Erforderliche Dokumentation

- Benutzerkontoinventar
- Privilegiertes Kontoinventar
- Break-Glass-Kontoverfahren
- Notfallzugriffsprotokolle
- Zugriffsüberprüfungsaufzeichnungen
- ACL-Dokumentation
- Verschlüsselungsschlüsselinventar
- Timeout-Konfigurationsdokumentation

### 9.2 Aufbewahrung

**Aufbewahrungsfrist:** [TODO: 6 Jahre ab Erstellung oder letztem Gültigkeitsdatum]

**Speicherort:** [TODO: Identitätsverwaltungssystem, Dokumenten-Repository]

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [TODO] | Handbook-Generator | Ersterstellung |



