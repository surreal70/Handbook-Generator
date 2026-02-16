# TISAX Handbuch-Vorlagen

## Überblick

Dieses Verzeichnis enthält Vorlagen für ein TISAX (Trusted Information Security Assessment Exchange) Handbuch. TISAX ist ein Informationssicherheits-Assessment-Standard für die Automobilindustrie, der auf dem VDA ISA-Katalog basiert.

## Vorlagenorganisation

Die Vorlagen sind nach TISAX-Kontrollbereichen organisiert und verwenden ein numerisches Präfix-System:

### 0010-0099: Informationssicherheitsmanagement
- 0010: TISAX Framework Übersicht
- 0020: Informationssicherheitsrichtlinie
- 0030: Organisation der Informationssicherheit
- 0040: Risikomanagement
- 0050: Sicherheitsziele und Planung

### 0100-0199: Asset Management und Zugriffskontrolle
- 0100: Asset Management Übersicht
- 0110: Asset-Inventar
- 0120: Informationsklassifizierung
- 0130: Medienhandhabung
- 0140: Zugriffskontrollrichtlinie
- 0150: Benutzerzugriffsverwaltung
- 0160: System- und Anwendungszugriffskontrolle

### 0200-0299: Kryptographie und physische Sicherheit
- 0200: Kryptographische Kontrollen
- 0210: Schlüsselverwaltung
- 0220: Physischer Sicherheitsperimeter
- 0230: Physische Zutrittskontrolle
- 0240: Sicherung von Büros und Einrichtungen
- 0250: Gerätesicherheit

### 0300-0399: Betriebs- und Kommunikationssicherheit
- 0300: Betriebssicherheit Übersicht
- 0310: Change Management
- 0320: Kapazitätsmanagement
- 0330: Malware-Schutz
- 0340: Backup und Recovery
- 0350: Logging und Monitoring
- 0360: Netzwerksicherheitsmanagement
- 0370: Informationsübertragung

### 0400-0499: Lieferantenbeziehungen und Incident Management
- 0400: Lieferantensicherheit
- 0410: Lieferantenvereinbarungen
- 0420: Lieferantenüberwachung
- 0430: Incident-Management-Verfahren
- 0440: Incident Response
- 0450: Beweissicherung

### 0500-0599: Business Continuity und Compliance
- 0500: Business Continuity Planning
- 0510: IKT-Kontinuität
- 0520: Einhaltung gesetzlicher Anforderungen
- 0530: Schutz geistigen Eigentums
- 0540: Schutz von Aufzeichnungen
- 0550: Datenschutz und Schutz personenbezogener Daten

## Verwendung der Vorlagen

### Platzhalter

Die Vorlagen verwenden Platzhalter im Format `{{ source.field }}` für organisationsspezifische Daten:

- `{{ source.organization_name }}` - Name Ihrer Organisation
- `{{ source.author }}` - Autor des Dokuments
- `{{ meta.version }}` - Versionsnummer
- `{{ meta.date }}` - Datum

### Anpassung

1. Kopieren Sie die Vorlagen in Ihr Projektverzeichnis
2. Ersetzen Sie die Platzhalter durch Ihre organisationsspezifischen Informationen
3. Passen Sie den Inhalt an Ihre spezifischen Anforderungen an
4. Entfernen Sie nicht zutreffende Abschnitte
5. Fügen Sie zusätzliche organisationsspezifische Abschnitte hinzu

### TISAX Assessment Levels

TISAX definiert drei Assessment Levels:

- **AL1**: Grundlegendes Assessment (Selbstauskunft)
- **AL2**: Detailliertes Assessment mit Vor-Ort-Prüfung
- **AL3**: Sehr detailliertes Assessment mit umfassender Vor-Ort-Prüfung

Passen Sie die Detailtiefe Ihrer Dokumentation an das angestrebte Assessment Level an.

## TISAX-Anforderungen

Die Vorlagen decken die folgenden TISAX-Bereiche ab:

1. **Informationssicherheit**: Schutz von Informationen und IT-Systemen
2. **Prototypenschutz**: Schutz von Prototypen und Entwicklungsinformationen
3. **Datenschutz**: Schutz personenbezogener Daten gemäß DSGVO

## Framework-Mapping

Siehe FRAMEWORK_MAPPING.md für eine detaillierte Zuordnung der Vorlagen zu spezifischen TISAX-Assessment-Zielen und VDA ISA-Kontrollen.

## Weitere Ressourcen

- VDA ISA Katalog
- TISAX Teilnehmerhandbuch
- ENX Association (TISAX-Betreiber)
- DSGVO und BDSG für Datenschutzanforderungen

## Hinweise

- Diese Vorlagen dienen als Ausgangspunkt und müssen an Ihre spezifischen Anforderungen angepasst werden
- Konsultieren Sie bei Bedarf Experten für Informationssicherheit und Datenschutz
- Halten Sie die Dokumentation aktuell und überprüfen Sie sie regelmäßig
- Bereiten Sie sich gründlich auf TISAX-Assessments vor

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |
