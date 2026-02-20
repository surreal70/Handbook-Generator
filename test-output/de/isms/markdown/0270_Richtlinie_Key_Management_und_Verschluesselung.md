# Richtlinie: Key Management und Verschlüsselung

**Dokument-ID:** 0270
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



## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0260_Policy_Kryptografie_und_Schluesselmanagement.md` und definiert detaillierte Verfahren für:
- Kryptographische Algorithmen und Standards
- Schlüsselerzeugung, -speicherung und -rotation
- Zertifikatsmanagement
- Verschlüsselung von Daten in Ruhe und in Bewegung

**Geltungsbereich:** Alle kryptographischen Systeme bei **AdminSend GmbH**

## 2. Kryptographische Standards

### 2.1 Genehmigte Algorithmen

**Symmetrische Verschlüsselung:**
- **AES-256** (Advanced Encryption Standard, 256-bit) - Empfohlen
- **AES-128** - Akzeptabel für nicht-kritische Daten
- **ChaCha20** - Akzeptabel für mobile Geräte

**Asymmetrische Verschlüsselung:**
- **RSA-4096** - Empfohlen für langfristige Sicherheit
- **RSA-2048** - Akzeptabel, Mindestanforderung
- **ECDSA P-384** - Empfohlen für Performance
- **Ed25519** - Akzeptabel für SSH-Keys

**Hash-Funktionen:**
- **SHA-256** - Mindestanforderung
- **SHA-384, SHA-512** - Empfohlen für kritische Anwendungen
- **BLAKE2** - Akzeptabel

**Verbotene Algorithmen:**
- MD5, SHA-1 (kryptographisch gebrochen)
- DES, 3DES (veraltet)
- RSA < 2048 bit (zu schwach)
- RC4 (unsicher)

### 2.2 TLS/SSL-Konfiguration

**TLS-Versionen:**
- **TLS 1.3** - Empfohlen
- **TLS 1.2** - Mindestanforderung
- **TLS 1.1, 1.0, SSL** - Verboten

**Cipher Suites (Empfohlen):**
```
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
```

**Zertifikate:**
- Mindestens RSA-2048 oder ECDSA P-256
- Gültigkeitsdauer: Max. 13 Monate (398 Tage)
- Trusted Certificate Authorities (CAs)

## 3. Schlüsselmanagement

### 3.1 Schlüsselerzeugung

**Anforderungen:**
- Kryptographisch sichere Zufallszahlengeneratoren (CSPRNG)
- Schlüssellängen gemäß Abschnitt 2.1
- Erzeugung in sicherer Umgebung (HSM, Key Vault)

**Prozess:**
1. Schlüsselanforderung über Ticketsystem
2. Genehmigung durch CISO oder IT-Security
3. Erzeugung durch Key Management System
4. Sichere Übergabe an Antragsteller
5. Dokumentation in Key-Register

### 3.2 Schlüsselspeicherung

**Hardware Security Modules (HSM):**
- Kritische Schlüssel (Root-CA, Master-Keys) in HSM: {{ meta-handbook.security_hsm }}
- FIPS 140-2 Level 2 oder höher
- Physische Sicherheit und Zugriffskontrolle

**Key Management Systems:**
- **Cloud:** {{ meta-handbook.cloud_key_vault }} (z.B. Azure Key Vault, AWS KMS)
- **On-Premises:** {{ meta-handbook.security_kms }} (z.B. HashiCorp Vault)
- Verschlüsselte Speicherung
- Audit-Logging aller Zugriffe

**Verboten:**
- Speicherung in Klartext
- Hardcoding in Quellcode
- Speicherung in Konfigurationsdateien
- Übertragung per E-Mail oder Chat

### 3.3 Schlüsselrotation

**Rotations-Intervalle:**

| Schlüsseltyp | Rotation | Begründung |
|--------------|----------|------------|
| Daten-Verschlüsselungsschlüssel (DEK) | Jährlich | Balance zwischen Sicherheit und Aufwand |
| Key-Encryption-Keys (KEK) | Alle 2 Jahre | Selten genutzt, höhere Sicherheit |
| TLS-Zertifikate | Alle 12 Monate | CA-Anforderungen |
| API-Keys | Alle 90 Tage | Häufige Nutzung, höheres Risiko |
| SSH-Keys | Alle 180 Tage | Administrativer Zugriff |

**Automatisierung:**
- Automatische Rotation wo möglich (Cloud-Services)
- Benachrichtigungen 30 Tage vor Ablauf
- Dokumentation aller Rotationen

**Notfall-Rotation:**
- Bei Verdacht auf Kompromittierung: Sofortige Rotation
- Bei Personalwechsel: Rotation aller betroffenen Schlüssel
- Bei Sicherheitsvorfällen: Rotation gemäß Incident Response

### 3.4 Schlüsselvernichtung

**Prozess:**
1. Schlüssel als "deprecated" markieren
2. Grace Period (30 Tage) für Datenentschlüsselung
3. Sichere Löschung aus allen Systemen
4. Dokumentation der Vernichtung

**Methoden:**
- Kryptographisches Überschreiben (mehrfach)
- HSM: Secure Erase-Funktion
- Physische Medien: Zerstörung gemäß DIN 66399

## 4. Zertifikatsmanagement

### 4.1 Public Key Infrastructure (PKI)

**Komponenten:**
- **Root CA:** {{ meta-handbook.pki_root_ca }} (Offline, HSM-geschützt)
- **Issuing CA:** {{ meta-handbook.pki_issuing_ca }} (Online, für Zertifikatsausstellung)
- **Certificate Management System:** {{ meta-handbook.pki_cms }}

**Zertifikatstypen:**
- **Server-Zertifikate:** Web-Server, API-Endpoints
- **Client-Zertifikate:** Benutzer-Authentifizierung, VPN
- **Code-Signing:** Software-Signierung
- **E-Mail-Zertifikate:** S/MIME-Verschlüsselung

### 4.2 Zertifikats-Lebenszyklus

**Ausstellung:**
1. Certificate Signing Request (CSR) erstellen
2. Antrag über PKI-Portal einreichen
3. Validierung durch Certificate Authority
4. Zertifikat ausstellen und bereitstellen
5. Installation und Konfiguration

**Erneuerung:**
- Automatische Benachrichtigung 60 Tage vor Ablauf
- Erneuerung 30 Tage vor Ablauf
- Automatisierung über ACME-Protokoll (Let's Encrypt)

**Widerruf (Revocation):**
- Bei Kompromittierung: Sofortiger Widerruf
- Bei Personalwechsel: Widerruf aller persönlichen Zertifikate
- Veröffentlichung in Certificate Revocation List (CRL)
- OCSP (Online Certificate Status Protocol) für Echtzeit-Checks

### 4.3 Zertifikats-Inventar

**Dokumentation:**
- Alle ausgestellten Zertifikate in CMDB
- Ablaufdaten, Verwendungszweck, Owner
- Automatische Scans für unbekannte Zertifikate

**Monitoring:**
- Tägliche Prüfung auf ablaufende Zertifikate
- Alerts bei Zertifikaten < 30 Tage Gültigkeit
- Automatische Erneuerung wo möglich

## 5. Verschlüsselung von Daten

### 5.1 Data at Rest (Daten in Ruhe)

**Verschlüsselungspflicht:**
- Alle vertraulichen und streng vertraulichen Daten
- Personenbezogene Daten (DSGVO-Anforderung)
- Finanzdaten und Geschäftsgeheimnisse
- Backups und Archivdaten

**Methoden:**

| Speicherort | Methode | Schlüsselverwaltung |
|-------------|---------|---------------------|
| Laptops/Desktops | BitLocker (Windows), FileVault (macOS) | TPM + Recovery Key in Key Vault |
| Server-Festplatten | LUKS (Linux), BitLocker (Windows) | Key Vault |
| Datenbanken | Transparent Data Encryption (TDE) | Database Key Management |
| Cloud-Storage | Server-Side Encryption (SSE) | Cloud Key Management Service |
| Dateiserver | Encrypted File System (EFS) | Active Directory + Key Vault |

**Konfiguration:**
- AES-256 für alle Verschlüsselungen
- Automatische Verschlüsselung bei Speicherung
- Keine Nutzer-Interaktion erforderlich

### 5.2 Data in Transit (Daten in Bewegung)

**Verschlüsselungspflicht:**
- Alle Datenübertragungen über öffentliche Netzwerke
- Interne Übertragungen vertraulicher Daten
- API-Kommunikation
- E-Mail mit vertraulichen Inhalten

**Methoden:**

| Übertragungsart | Protokoll | Konfiguration |
|-----------------|-----------|---------------|
| Web-Traffic | HTTPS (TLS 1.2+) | Siehe Abschnitt 2.2 |
| E-Mail | TLS (SMTP), S/MIME | Opportunistic TLS + Verschlüsselung für vertraulich |
| Dateitransfer | SFTP, FTPS, HTTPS | Keine unverschlüsselten Protokolle |
| VPN | IPsec, WireGuard | AES-256, Perfect Forward Secrecy |
| Database | TLS für Verbindungen | Erzwungene Verschlüsselung |

**Verbotene Protokolle:**
- FTP (unverschlüsselt)
- Telnet (unverschlüsselt)
- HTTP für vertrauliche Daten
- SMTP ohne TLS für vertrauliche E-Mails

### 5.3 Data in Use (Daten in Verarbeitung)

**Technologien:**
- **Confidential Computing:** Verschlüsselung während Verarbeitung (Intel SGX, AMD SEV)
- **Homomorphic Encryption:** Berechnungen auf verschlüsselten Daten (experimentell)
- **Secure Enclaves:** Isolierte Verarbeitungsumgebungen

**Anwendungsfälle:**
- Verarbeitung hochsensibler Daten in Cloud
- Multi-Party-Computation
- Privacy-Preserving Analytics

## 6. E-Mail-Verschlüsselung

### 6.1 S/MIME

**Implementierung:**
- S/MIME-Zertifikate für alle Mitarbeiter
- Automatische Verschlüsselung für E-Mails mit "Vertraulich"-Klassifizierung
- Signierung aller ausgehenden E-Mails

**Konfiguration:**
- Outlook, Thunderbird: S/MIME-Plugin
- Mobile Geräte: Native S/MIME-Unterstützung
- Zertifikatsverteilung über Active Directory

### 6.2 Opportunistic TLS

**SMTP TLS:**
- Alle E-Mail-Server unterstützen STARTTLS
- Erzwungene Verschlüsselung für bekannte Partner
- Fallback auf unverschlüsselt nur für nicht-vertrauliche E-Mails

**MTA-STS (Mail Transfer Agent Strict Transport Security):**
- Policy-Veröffentlichung über DNS
- Erzwingung von TLS für eingehende E-Mails

## 7. Backup-Verschlüsselung

**Anforderungen:**
- Alle Backups verschlüsselt (AES-256)
- Separate Schlüssel für Backups (nicht Produktionsschlüssel)
- Offline-Kopie der Backup-Schlüssel (Safe)

**Prozess:**
1. Backup-Erstellung mit Verschlüsselung
2. Schlüssel in Key Vault speichern
3. Offline-Kopie des Schlüssels in Safe
4. Regelmäßige Restore-Tests (quartalsweise)

**Disaster Recovery:**
- Backup-Schlüssel in Notfall-Dokumentation
- Zugriff nur durch autorisierte Personen
- Vier-Augen-Prinzip für Schlüsselzugriff

## 8. Cloud-Verschlüsselung

### 8.1 Cloud Storage

**Konfiguration:**
- **Azure:** Customer-Managed Keys (CMK) in Azure Key Vault
- **AWS:** Customer Master Keys (CMK) in AWS KMS
- **Google Cloud:** Customer-Managed Encryption Keys (CMEK)

**Vorteile:**
- Kontrolle über Schlüssel
- Möglichkeit zur Schlüsselrotation
- Compliance-Anforderungen erfüllt

### 8.2 Cloud Databases

**Verschlüsselung:**
- Transparent Data Encryption (TDE) aktiviert
- Verschlüsselte Verbindungen (TLS)
- Customer-Managed Keys für kritische Datenbanken

## 9. Compliance und Audit

### 9.1 Messgrößen (KPIs)

| Metrik | Zielwert | Messung |
|--------|----------|---------|
| Verschlüsselte Laptops | 100% | Endpoint-Management |
| TLS 1.2+ Nutzung | 100% | Web-Server-Logs |
| Zertifikats-Ablauf-Incidents | 0 pro Jahr | PKI-Monitoring |
| Schlüsselrotation-Compliance | > 95% | Key Management System |

### 9.2 Audit-Nachweise

**Dokumentation:**
- Kryptographie-Policy und -Richtlinien
- Schlüssel-Register und -Inventar
- Zertifikats-Inventar
- Verschlüsselungs-Konfigurationen
- Audit-Logs für Schlüsselzugriffe

## 10. Referenzen

### Interne Dokumente
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Übergeordnete Policy
- `0420_Policy_Backup_und_Wiederherstellung.md` - Backup Policy

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.24** - Use of cryptography
- **NIST SP 800-57** - Key Management Recommendations
- **NIST SP 800-52** - TLS Guidelines
- **BSI TR-02102** - Kryptographische Verfahren

**Genehmigt durch:**  
[TODO], CISO  
Datum: [TODO]

**Nächster Review:** [TODO]

