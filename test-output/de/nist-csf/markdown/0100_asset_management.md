
Document-ID: nist-csf-0100
Owner: [TODO]

Status: Draft
Classification: Internal

# Asset Management (ID.AM)

**Dokument-ID:** NIST-CSF-0100
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

Dieses Dokument beschreibt das Asset-Management-Programm zur Identifikation und Verwaltung von Daten, Personal, Geräten, Systemen und Einrichtungen, die es der Organisation ermöglichen, Geschäftsziele zu erreichen.

## Geltungsbereich

[TODO]

## Asset-Kategorien

### 1. Hardware-Assets
- Server und Workstations
- Netzwerkgeräte
- Mobile Geräte
- IoT-Geräte
- Speichersysteme

### 2. Software-Assets
- Betriebssysteme
- Anwendungen
- Datenbanken
- Middleware
- Entwicklungstools

### 3. Daten-Assets
- Kundendaten
- Finanzdaten
- Geistiges Eigentum
- Personaldaten
- Geschäftsgeheimnisse

### 4. Dienste und Systeme
- Cloud-Services
- SaaS-Anwendungen
- Managed Services
- Kritische Geschäftsprozesse

### 5. Personal
- IT-Personal
- Privilegierte Benutzer
- Externe Dienstleister
- Administratoren

## Asset-Inventar

### Inventarisierungsprozess
1. Asset-Erkennung (automatisiert und manuell)
2. Asset-Klassifizierung
3. Asset-Bewertung
4. Dokumentation im CMDB
5. Regelmäßige Aktualisierung

### Asset-Attribute
| Attribut | Beschreibung | Pflichtfeld |
|----------|--------------|-------------|
| Asset-ID | Eindeutige Kennung | Ja |
| Asset-Name | Beschreibender Name | Ja |
| Asset-Typ | Kategorie | Ja |
| Owner | Verantwortlicher | Ja |
| Standort | Physischer/logischer Ort | Ja |
| Kritikalität | Geschäftswichtigkeit | Ja |
| Wert | Geschäftswert | Ja |
| Status | Aktiv/Inaktiv/Außer Betrieb | Ja |

## Asset-Klassifizierung

### Kritikalitätsstufen
| Stufe | Beschreibung | Beispiele |
|-------|--------------|-----------|
| Kritisch | Geschäftsessentiell | Produktionssysteme, Kundendatenbanken |
| Hoch | Wichtig für Geschäftsbetrieb | ERP-Systeme, E-Mail-Server |
| Mittel | Unterstützende Systeme | Intranet, Collaboration-Tools |
| Niedrig | Nicht-kritische Systeme | Test-Umgebungen |

### Datenklassifizierung
| Klassifizierung | Beschreibung | Schutzanforderungen |
|-----------------|--------------|---------------------|
| Streng vertraulich | Höchste Sensitivität | Verschlüsselung, MFA, Audit-Logging |
| Vertraulich | Geschäftssensitiv | Zugriffskontrolle, Verschlüsselung |
| Intern | Nur für Mitarbeiter | Zugriffskontrolle |
| Öffentlich | Keine Einschränkungen | Basis-Schutz |

## Asset-Lifecycle

### 1. Beschaffung
- Genehmigungsprozess
- Sicherheitsanforderungen
- Lieferantenbewertung
- Vertragsmanagement

### 2. Bereitstellung
- Konfiguration nach Standards
- Sicherheitshärtung
- Inventarisierung
- Dokumentation

### 3. Betrieb
- Patch-Management
- Monitoring
- Wartung
- Änderungsmanagement

### 4. Außerbetriebnahme
- Datenlöschung
- Asset-Rückgabe
- Dokumentation
- Entsorgung

## Asset-Ownership

### Verantwortlichkeiten

**Asset Owner:**
- Geschäftliche Verantwortung
- Klassifizierung
- Zugriffsgenehmigung
- Compliance

**Asset Custodian (IT):**
- Technische Verwaltung
- Sicherheitskontrollen
- Backup und Recovery
- Patch-Management

**Asset User:**
- Ordnungsgemäße Nutzung
- Meldung von Problemen
- Einhaltung von Richtlinien

## Dokumentenverweise

- 0110_business_environment.md
- 0130_risk_assessment.md
- 0220_data_security.md (Protect)

