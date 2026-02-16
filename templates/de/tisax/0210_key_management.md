---
Document-ID: tisax-0210
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Schlüsselverwaltung

## Zweck

Dieses Dokument beschreibt die Prozesse und Verfahren für die Verwaltung kryptographischer Schlüssel gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle kryptographischen Schlüssel in {{ source.organization_name }}.

## Schlüssel-Lebenszyklus

### 1. Schlüsselgenerierung

**Anforderungen:**
- Kryptographisch sichere Zufallszahlengeneratoren (CSRNG)
- Ausreichende Schlüssellänge gemäß Standards
- Sichere Generierungsumgebung
- Dokumentation der Generierung

**Prozess:**
1. Anforderung mit Begründung
2. Genehmigung durch Schlüsselverwalter
3. Generierung in sicherer Umgebung
4. Validierung der Schlüsselqualität
5. Dokumentation und Registrierung

### 2. Schlüsselspeicherung

**Anforderungen:**
- Hardware Security Modules (HSM) für kritische Schlüssel
- Verschlüsselte Speicherung
- Redundante Speicherung
- Zugriffskontrolle
- Physische Sicherheit

**Speicherorte:**
- HSM für Produktionsschlüssel
- Key Management Service (KMS) für Cloud-Schlüssel
- Verschlüsselte Dateien für weniger kritische Schlüssel
- Sichere Tresore für Backup-Schlüssel

### 3. Schlüsselverteilung

**Anforderungen:**
- Sichere Übertragungskanäle
- Authentifizierung der Empfänger
- Verschlüsselte Übertragung
- Protokollierung
- Bestätigung des Empfangs

**Methoden:**
- Automatisierte Verteilung über sichere APIs
- Manuelle Übergabe in versiegelten Umschlägen
- Elektronische Übertragung über verschlüsselte Kanäle
- Persönliche Übergabe bei höchster Sensitivität

### 4. Schlüsselnutzung

**Anforderungen:**
- Verwendung nur für vorgesehenen Zweck
- Protokollierung der Nutzung
- Überwachung auf Missbrauch
- Regelmäßige Überprüfung

**Kontrollen:**
- Zugriffskontrolle
- Audit-Logging
- Anomalie-Erkennung
- Compliance-Monitoring

### 5. Schlüsselrotation

**Anforderungen:**
- Regelmäßige Rotation gemäß Richtlinie
- Automatisierte Prozesse wo möglich
- Keine Unterbrechung des Betriebs
- Dokumentation

**Rotationsintervalle:**
- Kritische Schlüssel: Quartalsweise
- Produktionsschlüssel: Halbjährlich
- Standard-Schlüssel: Jährlich
- Test-Schlüssel: Bei Bedarf

### 6. Schlüsselwiderruf

**Gründe:**
- Kompromittierung vermutet oder bestätigt
- Mitarbeiteraustritt
- Ablauf der Gültigkeit
- Änderung der Anforderungen
- Sicherheitsvorfall

**Prozess:**
1. Identifikation des Widerrufsgrundes
2. Sofortige Sperrung des Schlüssels
3. Benachrichtigung aller Stakeholder
4. Neuausstellung bei Bedarf
5. Dokumentation
6. Post-Incident-Review

### 7. Schlüsselarchivierung

**Anforderungen:**
- Langzeitaufbewahrung für verschlüsselte Daten
- Sichere Speicherung
- Zugriffskontrolle
- Wiederherstellungsprozess
- Regelmäßige Überprüfung der Integrität

**Aufbewahrungsfristen:**
- Gemäß gesetzlichen Anforderungen
- Gemäß Datenaufbewahrungsrichtlinie
- Mindestens solange verschlüsselte Daten existieren

### 8. Schlüsselvernichtung

**Anforderungen:**
- Sichere Löschung
- Mehrfache Überschreibung
- Dokumentation
- Überprüfung der Vollständigkeit
- Keine Wiederherstellbarkeit

**Methoden:**
- Kryptographisches Löschen (Crypto-Shredding)
- Physische Zerstörung von Speichermedien
- Sichere Löschverfahren (z.B. DoD 5220.22-M)
- Zertifizierte Vernichtung

## Schlüsseltypen

### Symmetrische Schlüssel

**Verwendung:**
- Datenverschlüsselung
- Nachrichtenauthentifizierung
- Datenbank-Verschlüsselung

**Verwaltung:**
- Sichere Generierung
- Verschlüsselte Speicherung
- Regelmäßige Rotation
- Sichere Verteilung

### Asymmetrische Schlüsselpaare

**Verwendung:**
- Digitale Signaturen
- Schlüsselaustausch
- Authentifizierung
- Zertifikate

**Verwaltung:**
- Private Schlüssel: Höchste Sicherheitsstufe
- Öffentliche Schlüssel: Verteilung über PKI
- Zertifikatsverwaltung
- Widerrufslisten

### Master-Schlüssel

**Verwendung:**
- Verschlüsselung anderer Schlüssel (Key Encryption Keys)
- Höchste Sicherheitsstufe

**Verwaltung:**
- Speicherung in HSM
- Mehrfache Redundanz
- Strenge Zugriffskontrolle
- Notfall-Wiederherstellungsplan

### Session-Schlüssel

**Verwendung:**
- Temporäre Verschlüsselung
- Kommunikationssitzungen

**Verwaltung:**
- Automatische Generierung
- Kurze Lebensdauer
- Automatische Vernichtung nach Nutzung

## Schlüsselverwaltungssysteme

### Hardware Security Modules (HSM)

**Funktionen:**
- Sichere Schlüsselgenerierung
- Geschützte Schlüsselspeicherung
- Kryptographische Operationen
- Audit-Logging

**Anforderungen:**
- FIPS 140-2 Level 2 oder höher
- Redundante Konfiguration
- Regelmäßige Wartung
- Backup und Recovery

### Key Management Service (KMS)

**Funktionen:**
- Zentrale Schlüsselverwaltung
- API-basierter Zugriff
- Automatisierte Rotation
- Audit-Logging

**Anforderungen:**
- Hochverfügbarkeit
- Verschlüsselte Kommunikation
- Zugriffskontrolle
- Compliance-Monitoring

### Schlüsselverwaltungsdatenbank

**Inhalte:**
- Schlüssel-Metadaten
- Verwendungszweck
- Eigentümer und Verantwortliche
- Gültigkeitsdauer
- Nutzungshistorie

**Sicherheit:**
- Verschlüsselte Speicherung
- Zugriffskontrolle
- Audit-Logging
- Regelmäßige Backups

## Schlüsselwiederherstellung

### Backup und Recovery

**Anforderungen:**
- Regelmäßige Backups kritischer Schlüssel
- Sichere Speicherung der Backups
- Getestete Wiederherstellungsprozesse
- Dokumentation

**Prozess:**
1. Identifikation des Wiederherstellungsbedarfs
2. Genehmigung durch autorisierte Person
3. Wiederherstellung aus Backup
4. Validierung der Wiederherstellung
5. Dokumentation

### Escrow

**Verwendung:**
- Für kritische Geschäftsschlüssel
- Bei Mitarbeiteraustritt
- Für Notfallwiederherstellung

**Anforderungen:**
- Vertrauenswürdige Escrow-Stelle
- Mehrfache Authentifizierung für Zugriff
- Regelmäßige Überprüfung
- Dokumentation

## Zugriffskontrolle

### Berechtigungen

**Rollen:**
- **Schlüsselverwalter**: Vollständige Verwaltung
- **Schlüsselnutzer**: Nutzung zugewiesener Schlüssel
- **Auditor**: Nur Lesezugriff auf Logs
- **Notfallzugriff**: Break-Glass-Zugriff

**Prinzipien:**
- Least Privilege
- Need-to-Know
- Segregation of Duties
- Vier-Augen-Prinzip bei kritischen Operationen

### Authentifizierung

**Anforderungen:**
- Multi-Faktor-Authentifizierung
- Starke Passwörter
- Regelmäßige Rezertifizierung
- Protokollierung aller Zugriffe

## Überwachung und Audit

### Protokollierung

**Ereignisse:**
- Schlüsselgenerierung
- Schlüsselzugriffe
- Schlüsselrotation
- Schlüsselwiderruf
- Schlüsselvernichtung
- Fehlgeschlagene Zugriffsversuche

### Monitoring

**Überwachung:**
- Echtzeit-Monitoring kritischer Operationen
- Automatische Alarmierung bei Anomalien
- Regelmäßige Log-Analysen
- Compliance-Checks

### Audit

**Regelmäßig:**
- Quartalsweise Stichproben
- Jährliche Vollprüfung
- Überprüfung der Compliance
- Identifikation von Verbesserungspotentialen

## Notfallmanagement

### Schlüsselkompromittierung

**Sofortmaßnahmen:**
1. Identifikation des kompromittierten Schlüssels
2. Sofortiger Widerruf
3. Benachrichtigung aller Stakeholder
4. Neuausstellung von Schlüsseln
5. Untersuchung des Vorfalls
6. Dokumentation

### Schlüsselverlust

**Maßnahmen:**
1. Versuch der Wiederherstellung aus Backup
2. Bei Misserfolg: Neuausstellung
3. Überprüfung der Auswirkungen
4. Benachrichtigung der Betroffenen
5. Dokumentation

### Disaster Recovery

**Anforderungen:**
- Dokumentierte Recovery-Prozesse
- Regelmäßige Tests
- Offsite-Backups
- Notfall-Kontakte

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **4.2.1**: Schlüsselverwaltung
- **4.2.2**: Schlüsselgenerierung
- **4.2.3**: Schlüsselspeicherung
- **4.2.4**: Schlüsselverteilung

### Assessment-Nachweise

- Schlüsselverwaltungsprozesse
- Schlüsselverwaltungsdatenbank
- Audit-Logs
- Schulungsnachweise
- Incident-Response-Pläne

## Verantwortlichkeiten

- **Schlüsselverwalter**: Tägliche Verwaltung
- **CISO**: Gesamtverantwortung
- **IT-Sicherheit**: Technische Implementierung
- **Auditor**: Compliance-Überwachung

## Schulung

Schulungsinhalte:
- Schlüsselverwaltungsprozesse
- Sichere Handhabung von Schlüsseln
- Incident Response
- Compliance-Anforderungen

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl aktiver Schlüssel
- Anzahl Schlüsselrotationen (Ziel: 100% fristgerecht)
- Anzahl Schlüsselkompromittierungen (Ziel: 0)
- Durchschnittliche Zeit bis zur Schlüsselbereitstellung
- Compliance-Rate (Ziel: 100%)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
