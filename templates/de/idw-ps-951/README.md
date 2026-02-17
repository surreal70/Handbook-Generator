# IDW PS 951 IT-Prüfungshandbuch Templates

## Überblick

Dieses Verzeichnis enthält Templates für die IT-Prüfung gemäß IDW Prüfungsstandard 951 "Grundsätze ordnungsmäßiger Prüfung von Compliance Management Systemen". Die Templates unterstützen die systematische Prüfung von IT-Systemen, IT-Prozessen und IT-Kontrollen im Rahmen der Jahresabschlussprüfung und sonstiger betriebswirtschaftlicher Prüfungen.

## IDW PS 951 Referenz

Der IDW Prüfungsstandard 951 wurde vom Institut der Wirtschaftsprüfer in Deutschland e.V. (IDW) herausgegeben und definiert die Grundsätze für die Prüfung von IT-Systemen im Rahmen der Abschlussprüfung. Der Standard adressiert:

- IT-Strategie und IT-Organisation
- IT-Prozesse und IT-Service-Management
- IT-Systeme und Anwendungen
- IT-Infrastruktur und IT-Betrieb
- IT-Sicherheit und Datenschutz
- IT-Governance und IT-Risikomanagement

## Template-Organisation

### Nummerierungsschema

Die Templates folgen einem strukturierten Nummerierungsschema mit 4-stelligen Präfixen:

- **0000**: Metadaten
- **0010-0099**: Prüfungsplanung und Vorbereitung
- **0100-0199**: IT-Strategie und IT-Organisation
- **0200-0299**: IT-Prozesse
- **0300-0399**: IT-Systeme und Anwendungen
- **0400-0499**: IT-Infrastruktur und IT-Betrieb
- **0500-0599**: IT-Sicherheit und Datenschutz

### Template-Struktur

Jedes Template folgt einer standardisierten Struktur:

```markdown
# Template-Titel

**Dokument-ID:** idw-ps-951-NNNN
**Owner:** {{ meta-organisation-roles.role_Internal_Auditor }}
**Version:** {{ meta-handbook.revision }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

## 1. Zweck
## 2. Prüfungsgegenstand
## 3. Prüfungshandlungen
## 4. Prüfungskriterien
## 5. Feststellungen
## 6. Empfehlungen
## 7. Referenzen
```

## Prüfungsbereiche

### 1. Prüfungsplanung (0010-0099)

- **0010**: Prüfungsplanung Übersicht
- **0020**: Prüfungsumfang und Scope-Definition
- **0030**: Risikobeurteilung und Risikoanalyse
- **0040**: Prüfungsteam und Ressourcen
- **0050**: Zeitplan und Meilensteine

### 2. IT-Strategie und Organisation (0100-0199)

- **0100**: IT-Strategie Bewertung
- **0110**: IT-Governance-Struktur
- **0120**: IT-Organisation und Rollen
- **0130**: IT-Steuerungsgremien
- **0140**: IT-Service-Management

### 3. IT-Prozesse (0200-0299)

- **0200**: IT-Prozesse Übersicht
- **0210**: Change Management
- **0220**: Incident Management
- **0230**: Problem Management
- **0240**: Release Management
- **0250**: Configuration Management

### 4. IT-Systeme und Anwendungen (0300-0399)

- **0300**: IT-Systeme und Anwendungen Übersicht
- **0310**: Systemarchitektur
- **0320**: Anwendungskontrollen
- **0330**: Schnittstellenmanagement
- **0340**: Datenintegritätskontrollen

### 5. IT-Infrastruktur und Betrieb (0400-0499)

- **0400**: IT-Infrastruktur und Betrieb Übersicht
- **0410**: Server und Storage
- **0420**: Netzwerkinfrastruktur
- **0430**: Datenbanksysteme
- **0440**: Backup und Recovery
- **0450**: Betriebsprozeduren

### 6. IT-Sicherheit und Datenschutz (0500-0599)

- **0500**: IT-Sicherheit und Datenschutz Übersicht
- **0510**: Zugriffskontrolle
- **0520**: Verschlüsselung und Schlüsselmanagement
- **0530**: Security Monitoring
- **0540**: Datenschutz-Compliance
- **0550**: Privacy Controls

## Placeholder-System

Die Templates verwenden ein Placeholder-System für organisationsspezifische Daten:

### Metadata-Placeholders
- `{{ meta-organisation-roles.role_Internal_Auditor }}` - Prüfungsleiter
- `{{ meta-handbook.revision }}` - Dokumentversion
- `{{ meta-handbook.status }}` - Dokumentstatus
- `{{ meta-handbook.modifydate }}` - Datum

### Source-Placeholders
- `[TODO]` - Organisationsname
- `[TODO]` - Prüfungszeitraum
- `[TODO]` - Systeme im Scope
- Weitere kontextspezifische Placeholders

## Anpassung der Templates

### 1. Metadaten anpassen

Passen Sie die Metadaten-Template-Datei an:
- `0000_metadata_de_idw-ps-951.md`

### 2. Organisationsspezifische Daten

Ersetzen Sie die Placeholders mit Ihren Daten:
- Manuell in den Templates
- Über das Placeholder-System des Handbook-Generators
- Über Datenquellen (z.B. NetBox)

### 3. Prüfungsumfang anpassen

Passen Sie die Templates an Ihren spezifischen Prüfungsumfang an:
- Entfernen Sie nicht relevante Abschnitte
- Fügen Sie zusätzliche Prüfungsbereiche hinzu
- Passen Sie Prüfungskriterien an

### 4. Prüfungstiefe anpassen

Passen Sie die Detailtiefe an Ihre Anforderungen an:
- Detaillierte Prüfung: Alle Abschnitte vollständig ausfüllen
- Standardprüfung: Fokus auf Kernbereiche
- Überblicksprüfung: Zusammenfassende Bewertungen

## Verwendung

### 1. Handbook generieren

```bash
python handbook-generator --template idw-ps-951 --language de --output-format html
```

### 2. Ausgabeformate

- **HTML**: Interaktive Website mit Navigation
- **PDF**: Druckbares Dokument mit Inhaltsverzeichnis
- **Markdown**: Editierbare Einzeldateien

### 3. Prüfungsdokumentation

Die generierten Handbücher dienen als:
- Prüfungsleitfaden
- Dokumentationsvorlage
- Berichtsgrundlage
- Nachweisdokumentation

## Best Practices

### Prüfungsplanung
1. Beginnen Sie mit der Risikoanalyse (0030)
2. Definieren Sie den Scope klar (0020)
3. Planen Sie ausreichend Ressourcen (0040)
4. Erstellen Sie einen realistischen Zeitplan (0050)

### Prüfungsdurchführung
1. Dokumentieren Sie alle Prüfungshandlungen
2. Sammeln Sie ausreichend Nachweise
3. Führen Sie strukturierte Interviews
4. Testen Sie Kontrollen systematisch

### Berichterstattung
1. Strukturieren Sie Feststellungen nach Schweregrad
2. Formulieren Sie konkrete Empfehlungen
3. Priorisieren Sie Maßnahmen
4. Definieren Sie Umsetzungsfristen

## Compliance und Standards

Die Templates berücksichtigen:
- **IDW PS 951**: Prüfungsstandard für IT-Systeme
- **IDW PS 340**: Risikofrüherkennungssystem
- **ISO/IEC 27001**: Informationssicherheit
- **DSGVO**: Datenschutz-Grundverordnung
- **BSI IT-Grundschutz**: IT-Sicherheitsstandards
- **COBIT 2019**: IT-Governance-Framework
- **ITIL 4**: IT-Service-Management

## Support und Dokumentation

Weitere Informationen:
- **FRAMEWORK_MAPPING.md**: Mapping zu IDW PS 951 Anforderungen
- **Handbook-Generator Dokumentation**: Allgemeine Nutzungshinweise
- **IDW Website**: https://www.idw.de

## Lizenz und Haftungsausschluss

Diese Templates dienen als Orientierungshilfe und müssen an die spezifischen Anforderungen Ihrer Organisation angepasst werden. Sie ersetzen nicht die fachliche Beurteilung durch qualifizierte Prüfer.

---

**Template-Version:** 1.0  
**Letzte Aktualisierung:** 2026-02-10  
**Sprache:** Deutsch

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |
