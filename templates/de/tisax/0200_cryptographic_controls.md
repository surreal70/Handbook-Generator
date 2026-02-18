
Document-ID: tisax-0200

Status: Draft
Classification: Internal

# Kryptographische Kontrollen

**Dokument-ID:** [FRAMEWORK]-0200
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

## Zweck

Dieses Dokument definiert die Anforderungen für den Einsatz kryptographischer Kontrollen gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle kryptographischen Maßnahmen in [TODO].

## Kryptographie-Richtlinie

### Ziele

- Schutz der Vertraulichkeit sensibler Informationen
- Sicherstellung der Datenintegrität
- Authentifizierung von Kommunikationspartnern
- Nicht-Abstreitbarkeit von Transaktionen

### Anwendungsbereiche

**Verschlüsselung erforderlich für:**
- Vertrauliche und streng vertrauliche Daten
- Personenbezogene Daten
- Geschäftsgeheimnisse
- Authentifizierungsinformationen
- Datenübertragung über unsichere Netzwerke

## Verschlüsselungsstandards

### Symmetrische Verschlüsselung

**Zugelassene Algorithmen:**
- AES-256 (bevorzugt)
- AES-128 (akzeptabel)
- ChaCha20 (akzeptabel)

**Nicht zugelassen:**
- DES, 3DES
- RC4
- Blowfish

### Asymmetrische Verschlüsselung

**Zugelassene Algorithmen:**
- RSA (mindestens 2048 Bit, bevorzugt 4096 Bit)
- ECC (mindestens 256 Bit)
- Ed25519

**Nicht zugelassen:**
- RSA < 2048 Bit
- DSA < 2048 Bit

### Hash-Funktionen

**Zugelassene Algorithmen:**
- SHA-256 (bevorzugt)
- SHA-384
- SHA-512
- SHA-3

**Nicht zugelassen:**
- MD5
- SHA-1

## Verschlüsselung ruhender Daten

### Datenspeicherung

**Anforderungen:**
- Verschlüsselung vertraulicher Daten at rest
- Full Disk Encryption für mobile Geräte
- Datenbank-Verschlüsselung für sensible Daten
- Verschlüsselte Backups

**Implementierung:**
- BitLocker (Windows)
- FileVault (macOS)
- LUKS (Linux)
- Transparent Data Encryption (Datenbanken)

### Cloud-Speicher

**Anforderungen:**
- Verschlüsselung vor Upload (Client-seitig)
- Verschlüsselung durch Cloud-Provider
- Schlüsselverwaltung durch Organisation
- Regelmäßige Überprüfung

## Verschlüsselung übertragener Daten

### Netzwerkverschlüsselung

**Anforderungen:**
- TLS 1.2 oder höher für alle Verbindungen
- Starke Cipher Suites
- Zertifikatsvalidierung
- Perfect Forward Secrecy

**Protokolle:**
- HTTPS für Web-Verkehr
- SFTP/SCP für Dateitransfer
- VPN für Remote-Zugriff
- S/MIME oder PGP für E-Mail

### E-Mail-Verschlüsselung

**Anforderungen:**
- Verschlüsselung vertraulicher E-Mails
- S/MIME oder PGP
- Digitale Signaturen
- Sichere Schlüsselverteilung

## Digitale Signaturen

### Anwendung

**Verwendung für:**
- Verträge und Vereinbarungen
- Softwareverteilung
- E-Mail-Kommunikation
- Dokumentenauthentifizierung

**Anforderungen:**
- Qualifizierte elektronische Signaturen wo erforderlich
- Zeitstempel für Langzeitarchivierung
- Sichere Schlüsselaufbewahrung
- Widerrufsmechanismen

## Zertifikatsverwaltung

### Public Key Infrastructure (PKI)

**Komponenten:**
- Certificate Authority (CA)
- Registration Authority (RA)
- Certificate Revocation List (CRL)
- Online Certificate Status Protocol (OCSP)

**Anforderungen:**
- Vertrauenswürdige CAs
- Regelmäßige Zertifikatserneuerung
- Widerrufsprüfung
- Sichere Schlüsselgenerierung

### Zertifikats-Lebenszyklus

**Phasen:**
1. Anforderung und Validierung
2. Ausstellung
3. Verteilung
4. Nutzung
5. Erneuerung
6. Widerruf
7. Archivierung

## Schlüsselverwaltung

### Schlüsselgenerierung

**Anforderungen:**
- Kryptographisch sichere Zufallszahlengeneratoren
- Ausreichende Schlüssellänge
- Sichere Generierungsumgebung
- Dokumentation

### Schlüsselspeicherung

**Anforderungen:**
- Hardware Security Modules (HSM) für kritische Schlüssel
- Verschlüsselte Speicherung
- Zugriffskontrolle
- Physische Sicherheit

**Methoden:**
- HSM
- Key Management Service (KMS)
- Verschlüsselte Dateien
- Sichere Tresore

### Schlüsselverteilung

**Anforderungen:**
- Sichere Übertragungskanäle
- Authentifizierung der Empfänger
- Protokollierung
- Bestätigung des Empfangs

### Schlüsselrotation

**Anforderungen:**
- Regelmäßige Rotation (mindestens jährlich)
- Automatisierte Prozesse wo möglich
- Keine Unterbrechung des Betriebs
- Dokumentation

### Schlüsselwiderruf

**Gründe:**
- Kompromittierung
- Mitarbeiteraustritt
- Ablauf der Gültigkeit
- Änderung der Anforderungen

**Prozess:**
- Sofortige Sperrung
- Benachrichtigung der Stakeholder
- Neuausstellung bei Bedarf
- Dokumentation

### Schlüsselarchivierung

**Anforderungen:**
- Langzeitaufbewahrung für verschlüsselte Daten
- Sichere Speicherung
- Zugriffskontrolle
- Wiederherstellungsprozess

### Schlüsselvernichtung

**Anforderungen:**
- Sichere Löschung
- Dokumentation
- Überprüfung der Vollständigkeit
- Keine Wiederherstellbarkeit

## Kryptographische Geräte

### Hardware Security Modules (HSM)

**Verwendung:**
- Schlüsselgenerierung und -speicherung
- Kryptographische Operationen
- Digitale Signaturen
- Zertifikatsverwaltung

**Anforderungen:**
- FIPS 140-2 Level 2 oder höher
- Physische Sicherheit
- Zugriffskontrolle
- Regelmäßige Wartung

### Trusted Platform Modules (TPM)

**Verwendung:**
- Festplattenverschlüsselung
- Sichere Schlüsselspeicherung
- Plattform-Authentifizierung
- Secure Boot

## Compliance und Standards

### Relevante Standards

- ISO/IEC 27001:2013 (Anhang A.10)
- NIST SP 800-57 (Key Management)
- NIST SP 800-52 (TLS)
- BSI TR-02102 (Kryptographische Verfahren)

### Regulatorische Anforderungen

- DSGVO (Verschlüsselung personenbezogener Daten)
- eIDAS (Elektronische Signaturen)
- TISAX (VDA ISA Katalog)

## Kryptographie-Bewertung

### Regelmäßige Überprüfung

**Jährlich:**
- Überprüfung der verwendeten Algorithmen
- Bewertung der Schlüssellängen
- Überprüfung der Implementierungen
- Aktualisierung der Richtlinien

**Bei Bedarf:**
- Bei neuen Bedrohungen
- Bei neuen Standards
- Bei Sicherheitsvorfällen
- Bei technologischen Änderungen

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **4.1**: Kryptographische Kontrollen
- **4.2**: Schlüsselverwaltung

### Assessment-Nachweise

- Kryptographie-Richtlinie
- Schlüsselverwaltungsprozesse
- Verschlüsselungsnachweise
- Audit-Berichte

## Verantwortlichkeiten

- **CISO**: Gesamtverantwortung
- **Kryptographie-Beauftragter**: Implementierung und Überwachung
- **IT-Sicherheit**: Technische Umsetzung
- **Schlüsselverwalter**: Schlüsselverwaltung

## Schulung

Schulung für:
- Kryptographie-Grundlagen
- Sichere Schlüsselverwaltung
- Verwendung von Verschlüsselungstools
- Incident Response bei Schlüsselkompromittierung

## Kennzahlen

[TODO] misst:
- Anteil verschlüsselter Daten (Ziel: 100% für vertrauliche Daten)
- Anzahl aktiver Schlüssel
- Anzahl Schlüsselrotationen
- Anzahl Sicherheitsvorfälle im Zusammenhang mit Kryptographie

