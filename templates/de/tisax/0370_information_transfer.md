
Document-ID: tisax-0370

Status: Draft
Classification: Internal

# Informationsübertragung

**Dokument-ID:** [FRAMEWORK]-0370
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

## Zweck

Dieses Dokument definiert Anforderungen für die sichere Übertragung von Informationen gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Informationsübertragungen von [TODO].

## Übertragungskanäle

### E-Mail

**Anforderungen:**
- Verschlüsselung vertraulicher E-Mails (S/MIME oder PGP)
- SPF, DKIM, DMARC
- Spam- und Malware-Filter
- DLP (Data Loss Prevention)

### Dateitransfer

**Sichere Methoden:**
- SFTP/SCP
- HTTPS
- Verschlüsselte Cloud-Services
- Managed File Transfer (MFT)

**Nicht zugelassen:**
- FTP (unverschlüsselt)
- HTTP (unverschlüsselt)
- Unverschlüsselte E-Mail-Anhänge (vertrauliche Daten)

### Physische Medien

**Anforderungen:**
- Verschlüsselung
- Sichere Verpackung
- Nachverfolgung
- Empfangsbestätigung

## Verschlüsselung

### Übertragungsverschlüsselung

**Anforderungen:**
- TLS 1.2 oder höher
- Starke Cipher Suites
- Zertifikatsvalidierung
- Perfect Forward Secrecy

### End-to-End-Verschlüsselung

**Verwendung für:**
- Streng vertrauliche Informationen
- Personenbezogene Daten
- Geschäftsgeheimnisse

## Datenklassifizierung

### Übertragungsrichtlinien

**Öffentlich:**
- Keine besonderen Anforderungen

**Intern:**
- Verschlüsselte Kanäle bevorzugt

**Vertraulich:**
- Verschlüsselung obligatorisch
- Genehmigung erforderlich

**Streng Vertraulich:**
- End-to-End-Verschlüsselung
- Genehmigungs- und Dokumentationspflicht
- Empfangsbestätigung

## Externe Kommunikation

### Partner und Lieferanten

**Anforderungen:**
- Vertraulichkeitsvereinbarungen
- Sichere Übertragungskanäle
- Dokumentation
- Regelmäßige Überprüfung

### Cloud-Services

**Anforderungen:**
- Verschlüsselte Übertragung
- Verschlüsselte Speicherung
- Zugriffskontrolle
- Compliance-Prüfung

## Überwachung

### Monitoring

**Überwachte Aktivitäten:**
- Übertragung vertraulicher Daten
- Große Datenmengen
- Ungewöhnliche Übertragungsmuster
- Externe Übertragungen

### DLP (Data Loss Prevention)

**Funktionen:**
- Erkennung sensibler Daten
- Blockierung unerlaubter Übertragungen
- Alarmierung
- Reporting

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **7.2**: Informationsübertragung

### Assessment-Nachweise

- Übertragungsrichtlinien
- Verschlüsselungskonfiguration
- DLP-Berichte

## Kennzahlen

[TODO] misst:
- Anzahl verschlüsselter Übertragungen
- Anzahl DLP-Vorfälle
- Compliance-Rate

