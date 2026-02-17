# ISO/IEC 38500 IT-Governance Handbuch-Vorlagen

## Überblick

Dieses Verzeichnis enthält Vorlagen für die Erstellung eines ISO/IEC 38500 IT-Governance Handbuchs. Die Vorlagen decken alle Aspekte der IT-Governance ab: die sechs Prinzipien, das EDM-Modell, Rollen und Verantwortlichkeiten sowie Implementierung und kontinuierliche Verbesserung.

## ISO/IEC 38500 Struktur

ISO/IEC 38500 ist der internationale Standard für Corporate Governance of IT. Er definiert ein Framework für effektive, effiziente und akzeptable Nutzung von IT in Organisationen.

### Die sechs Governance-Prinzipien

1. **Verantwortung (Responsibility)**: Klare Verantwortlichkeiten für IT-Entscheidungen
2. **Strategie (Strategy)**: IT-Strategie unterstützt Unternehmensstrategie
3. **Beschaffung (Acquisition)**: IT-Beschaffungen sind angemessen begründet
4. **Leistung (Performance)**: IT liefert erforderliche Leistung
5. **Konformität (Conformance)**: IT erfüllt alle Verpflichtungen
6. **Menschliches Verhalten (Human Behavior)**: IT respektiert menschliche Bedürfnisse

### Das EDM-Modell

- **Evaluate (Bewerten)**: Bewertung der aktuellen und zukünftigen IT-Nutzung
- **Direct (Steuern)**: Vorbereitung und Kommunikation von Plänen und Richtlinien
- **Monitor (Überwachen)**: Überwachung der Konformität und Leistung

## Vorlagen-Organisation

Die Vorlagen sind thematisch organisiert und verwenden ein numerisches Präfix-System:

### Governance Framework und Prinzipien (0010-0099)
- `0010_governance_framework.md` - IT-Governance Framework Übersicht
- `0020_governance_model.md` - IT-Governance Modell
- `0030_principles_overview.md` - Übersicht der sechs Prinzipien
- `0040_responsibility_principle.md` - Prinzip 1: Verantwortung
- `0050_strategy_principle.md` - Prinzip 2: Strategie
- `0060_acquisition_principle.md` - Prinzip 3: Beschaffung
- `0070_performance_principle.md` - Prinzip 4: Leistung
- `0080_conformance_principle.md` - Prinzip 5: Konformität
- `0090_human_behavior_principle.md` - Prinzip 6: Menschliches Verhalten

### Evaluate-Direct-Monitor Modell (0100-0199)
- `0100_edm_model.md` - EDM-Modell Übersicht
- `0110_evaluation_processes.md` - Bewertungsprozesse
- `0120_direction_processes.md` - Steuerungsprozesse
- `0130_monitoring_processes.md` - Überwachungsprozesse
- `0140_performance_measurement.md` - Leistungsmessung

### Rollen und Verantwortlichkeiten (0200-0299)
- `0200_governance_roles.md` - IT-Governance Rollen
- `0210_board_responsibilities.md` - Vorstandsverantwortlichkeiten
- `0220_executive_responsibilities.md` - Geschäftsführungsverantwortlichkeiten
- `0230_it_management_responsibilities.md` - IT-Management-Verantwortlichkeiten
- `0240_stakeholder_engagement.md` - Stakeholder-Einbindung

### Implementierung und Verbesserung (0300-0399)
- `0300_governance_implementation.md` - IT-Governance Implementierung
- `0310_policy_framework.md` - Richtlinien-Framework
- `0320_decision_making.md` - Entscheidungsprozesse
- `0330_communication.md` - Kommunikation
- `0340_continuous_improvement.md` - Kontinuierliche Verbesserung

## Nummerierungsschema

- Vorlagen verwenden 4-stellige Präfixe (z.B. 0010, 0020, 0030)
- Inkremente von 10 ermöglichen zukünftige Einfügungen
- Themen sind in Hunderterbereiche gruppiert (0000-0099, 0100-0199, etc.)

## Platzhalter-System

Die Vorlagen verwenden Platzhalter für organisationsspezifische Daten:

### Metadaten-Platzhalter
- `{{ meta-handbook.owner }}` - Dokumentenverantwortlicher
- `{{ meta-handbook.revision }}` - Versionsnummer
- `{{ meta-handbook.modifydate }}` - Datum
- `{{ meta-organisation.name }}` - Organisationsname
- `{{ meta-organisation-roles.role_CIO }}` - Name des CIO
- `{{ meta-organisation-roles.role_CISO }}` - Name des CISO

### Datenquellen-Platzhalter
- `[TODO]` - Organisationsname aus Datenquelle
- `[TODO]` - Autor aus Datenquelle
- Weitere organisationsspezifische Felder

## Anpassung der Vorlagen

### 1. Metadaten aktualisieren
Beginnen Sie mit der Datei `0000_metadata_de_iso-38500.md` und füllen Sie die Metadaten aus.

### 2. Platzhalter ersetzen
Ersetzen Sie alle `{{ placeholder }}` mit Ihren organisationsspezifischen Informationen.

### 3. Inhalte anpassen
Passen Sie die Vorlagen an Ihre spezifischen Anforderungen an:
- Fügen Sie organisationsspezifische Governance-Strukturen hinzu
- Entfernen Sie nicht zutreffende Abschnitte
- Erweitern Sie Abschnitte nach Bedarf

### 4. Dokumentenverweise aktualisieren
Stellen Sie sicher, dass alle Querverweise zwischen Dokumenten korrekt sind.

## Verwendung mit dem Handbuch-Generator

Diese Vorlagen sind für die Verwendung mit dem Handbuch-Generator-System konzipiert:

```bash
python handbook-generator --template iso-38500 --language de --output-format html
```

Unterstützte Ausgabeformate:
- HTML (Mini-Website mit Navigation)
- PDF (mit Inhaltsverzeichnis)
- Markdown (kombiniert oder separate Dateien)

## Framework-Referenz

Weitere Informationen zu ISO/IEC 38500:
- [ISO/IEC 38500:2015](https://www.iso.org/standard/62816.html)
- ISO/IEC 38500:2015 - Information technology — Governance of IT for the organization

## Framework-Mapping

Siehe `FRAMEWORK_MAPPING.md` für eine detaillierte Zuordnung der Vorlagen zu ISO/IEC 38500 Prinzipien und Praktiken.

## Lizenz

Diese Vorlagen basieren auf ISO/IEC 38500:2015. Der Standard selbst ist urheberrechtlich geschützt.

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2024 | Initiale Version basierend auf ISO/IEC 38500:2015 |

