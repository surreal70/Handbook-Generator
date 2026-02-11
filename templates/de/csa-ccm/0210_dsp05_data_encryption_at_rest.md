---
Document-ID: csa-ccm-0210
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# DSP-05: Data Encryption at Rest

## CCM-Kontrolle

**Kontrolldomäne**: Data Security & Privacy (DSP)  
**Kontroll-ID**: DSP-05  
**Kontrollname**: Data Encryption at Rest

## Kontrollziel

Schutz sensibler Daten im Ruhezustand durch Verschlüsselung, um unbefugten Zugriff zu verhindern und Vertraulichkeit zu gewährleisten.

## Kontrollbeschreibung

Die Organisation muss:
- Alle sensiblen Daten im Ruhezustand verschlüsseln
- Starke Verschlüsselungsalgorithmen verwenden (mindestens AES-256)
- Verschlüsselungsschlüssel sicher verwalten
- Verschlüsselung für alle Speicherorte implementieren (Datenbanken, File Storage, Backups)
- Regelmäßige Überprüfung der Verschlüsselungsimplementierung

## Implementierung in {{ source.organization_name }}

### Verschlüsselungsstandards

**Algorithmen**:
- **Symmetrisch**: AES-256-GCM
- **Asymmetrisch**: RSA-4096, ECC P-384
- **Hashing**: SHA-256, SHA-384

**Protokolle**:
- TLS 1.3 (für Daten in Übertragung)
- IPSec (für VPN-Verbindungen)

### Verschlüsselungsimplementierung

**Datenbanken**:

| Datenbank | Typ | Verschlüsselungsmethode | Status |
|-----------|-----|------------------------|--------|
| [DB 1] | PostgreSQL | Transparent Data Encryption (TDE) | Aktiv |
| [DB 2] | MySQL | InnoDB Encryption | Aktiv |
| [DB 3] | MongoDB | Encryption at Rest | Aktiv |

**File Storage**:

| Storage | Typ | Verschlüsselungsmethode | Status |
|---------|-----|------------------------|--------|
| [Storage 1] | Object Storage | Server-Side Encryption (SSE) | Aktiv |
| [Storage 2] | Block Storage | LUKS Full Disk Encryption | Aktiv |
| [Storage 3] | NAS | AES-256 Encryption | Aktiv |

**Backups**:

| Backup-System | Verschlüsselungsmethode | Schlüsselverwaltung | Status |
|---------------|------------------------|---------------------|--------|
| [Backup 1] | AES-256 | KMS | Aktiv |
| [Backup 2] | AES-256 | HSM | Aktiv |

### Schlüsselverwaltung

**Key Management System (KMS)**:
- **Anbieter**: [KMS-Anbieter]
- **Typ**: Cloud-basiert / On-Premises / Hybrid
- **FIPS 140-2 Level**: Level 2/3

**Schlüsselhierarchie**:
```
Master Key (Root Key)
    ├── Key Encryption Keys (KEK)
    │   ├── Data Encryption Key 1 (DEK)
    │   ├── Data Encryption Key 2 (DEK)
    │   └── Data Encryption Key 3 (DEK)
    └── Backup Encryption Keys
```

**Schlüsselrotation**:
- **Master Keys**: Jährlich
- **Data Encryption Keys**: Quartalsweise
- **Backup Keys**: Halbjährlich

### Zugriffskontrolle für Verschlüsselungsschlüssel

**Berechtigungsmodell**:

| Rolle | Berechtigung | Genehmigung erforderlich |
|-------|--------------|-------------------------|
| Security Admin | Vollzugriff auf KMS | CISO |
| Database Admin | Zugriff auf DB-Schlüssel | Security Admin |
| Backup Admin | Zugriff auf Backup-Schlüssel | Security Admin |
| Developer | Kein direkter Zugriff | N/A |

**Multi-Person Control**:
- Schlüsselerzeugung: 2 Personen erforderlich
- Schlüssellöschung: 3 Personen erforderlich
- Master Key Rotation: CISO + 2 Security Admins

## Kontrollaktivitäten

### 1. Verschlüsselungsimplementierung

**Prozess**:
1. Datenklassifizierung durchführen
2. Verschlüsselungsanforderungen definieren
3. Verschlüsselungslösung auswählen
4. Implementierung und Konfiguration
5. Testing und Validierung
6. Dokumentation

**Verantwortlich**: Security Team, Infrastructure Team

### 2. Schlüsselmanagement

**Prozess**:
1. Schlüsselerzeugung
2. Schlüsselspeicherung im KMS/HSM
3. Schlüsselverteilung (automatisiert)
4. Schlüsselrotation (geplant)
5. Schlüsselarchivierung
6. Schlüsselvernichtung

**Automatisierung**: 95% der Schlüsseloperationen automatisiert

### 3. Verschlüsselungsüberwachung

**Monitoring**:
- Verschlüsselungsstatus aller Systeme
- Schlüsselzugriffe und -verwendung
- Fehlgeschlagene Verschlüsselungsoperationen
- Compliance-Abweichungen

**Tools**:
- SIEM Integration
- KMS Audit Logs
- Cloud Security Posture Management (CSPM)

**Alerting**:
- Unverschlüsselte sensible Daten erkannt
- Unberechtigter Schlüsselzugriff
- Verschlüsselungsfehler
- Schlüsselrotation überfällig

### 4. Compliance-Validierung

**Validierungsmethoden**:
- Automatisierte Compliance-Scans
- Manuelle Stichproben
- Penetration Tests
- Externe Audits

**Frequenz**:
- Automatisiert: Täglich
- Manuell: Monatlich
- Penetration Test: Jährlich
- Audit: Jährlich

## Nachweise und Evidenzen

### Erforderliche Nachweise

1. **Verschlüsselungskonfiguration**:
   - Verschlüsselungsrichtlinien
   - Konfigurationsdokumentation
   - Verschlüsselungsinventar

2. **Schlüsselverwaltung**:
   - KMS-Konfiguration
   - Schlüsselrotationsprotokolle
   - Zugriffsprotokolle

3. **Monitoring und Alerting**:
   - SIEM-Logs
   - Compliance-Scan-Berichte
   - Alert-Historie

4. **Testing und Validierung**:
   - Verschlüsselungstests
   - Penetration Test Reports
   - Audit-Berichte

## Metriken und KPIs

| Metrik | Zielwert | Messfrequenz |
|--------|----------|--------------|
| Verschlüsselungsrate (sensible Daten) | 100% | Täglich |
| Unverschlüsselte sensible Daten | 0 | Täglich |
| Schlüsselrotation pünktlich | 100% | Monatlich |
| Verschlüsselungsfehler | < 0.1% | Wöchentlich |
| KMS-Verfügbarkeit | ≥ 99.9% | Monatlich |
| Zeit bis zur Verschlüsselung neuer Daten | ≤ 24 Stunden | Pro System |

## Risiken und Kontrolllücken

### Identifizierte Risiken

| Risiko | Wahrscheinlichkeit | Auswirkung | Risikoscore | Maßnahme |
|--------|-------------------|------------|-------------|----------|
| Schlüsselverlust | Niedrig | Kritisch | 15 | Backup, Escrow |
| Unberechtigter Schlüsselzugriff | Niedrig | Hoch | 10 | MFA, Monitoring |
| Schwache Verschlüsselung | Sehr niedrig | Hoch | 5 | Standards, Reviews |
| Performance-Probleme | Mittel | Mittel | 9 | Hardware-Beschleunigung |

### Kontrolllücken

**Legacy-Systeme**:
- **Beschreibung**: Einige Legacy-Systeme unterstützen keine moderne Verschlüsselung
- **Risiko**: Mittel
- **Remediation**: Migration zu neuen Systemen geplant
- **Fälligkeitsdatum**: [Datum]

## Audit-Hinweise

### Audit-Fragen

1. Sind alle sensiblen Daten im Ruhezustand verschlüsselt?
2. Werden starke Verschlüsselungsalgorithmen verwendet (AES-256)?
3. Ist ein Key Management System implementiert?
4. Werden Verschlüsselungsschlüssel regelmäßig rotiert?
5. Wird der Verschlüsselungsstatus überwacht?
6. Sind Backups verschlüsselt?

### Audit-Evidenzen

- Verschlüsselungsrichtlinien
- Verschlüsselungsinventar
- KMS-Konfiguration
- Schlüsselrotationsprotokolle
- Compliance-Scan-Berichte
- Audit-Logs
- Penetration Test Reports

## Referenzen

### Interne Dokumente

- Data Encryption Policy
- Key Management Procedures
- Data Classification Policy

### Externe Standards

- CSA CCM v4.0 - DSP-05
- NIST SP 800-57 (Key Management)
- NIST SP 800-111 (Storage Encryption)
- ISO/IEC 27018:2019 (Cloud Privacy)
- FIPS 140-2 (Cryptographic Module Validation)
- GDPR Article 32 (Security of Processing)

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Version |

<!-- Hinweis: Passen Sie Verschlüsselungsimplementierung an Ihre Infrastruktur an -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
