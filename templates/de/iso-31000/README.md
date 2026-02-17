# ISO 31000 Risikomanagement Handbuch-Vorlagen

## Überblick

Dieses Verzeichnis enthält Vorlagen für die Erstellung eines ISO 31000 Risikomanagement Handbuchs. Die Vorlagen decken alle Aspekte des Risikomanagements ab: die acht Prinzipien, das Framework, den Risikomanagement-Prozess sowie Überwachung und kontinuierliche Verbesserung.

## ISO 31000 Struktur

ISO 31000 ist der internationale Standard für Risikomanagement. Er bietet Prinzipien, ein Framework und einen Prozess für das Management von Risiken in jeder Organisation.

### Die acht Risikomanagement-Prinzipien

1. **Integriert**: Risikomanagement ist Teil aller Organisationsaktivitäten
2. **Strukturiert und umfassend**: Systematischer Ansatz für konsistente Ergebnisse
3. **Angepasst**: Risikomanagement ist auf Kontext und Ziele abgestimmt
4. **Inklusiv**: Einbeziehung von Stakeholdern für relevante Erkenntnisse
5. **Dynamisch**: Risikomanagement reagiert auf Veränderungen
6. **Beste verfügbare Informationen**: Entscheidungen basieren auf aktuellen Daten
7. **Menschliche und kulturelle Faktoren**: Berücksichtigung menschlichen Verhaltens
8. **Kontinuierliche Verbesserung**: Ständige Weiterentwicklung des Risikomanagements

### Risikomanagement-Framework

- **Führung und Verpflichtung**: Top-Management-Unterstützung
- **Integration**: Einbettung in Organisationsprozesse
- **Design**: Anpassung an Organisationskontext
- **Implementierung**: Umsetzung des Frameworks
- **Bewertung**: Überprüfung der Wirksamkeit
- **Verbesserung**: Kontinuierliche Anpassung

### Risikomanagement-Prozess

- **Kommunikation und Konsultation**: Stakeholder-Einbindung
- **Festlegung des Kontexts**: Rahmenbedingungen definieren
- **Risikobeurteilung**: Identifikation, Analyse, Bewertung
- **Risikobehandlung**: Maßnahmen zur Risikominderung
- **Überwachung und Überprüfung**: Kontinuierliche Kontrolle
- **Aufzeichnung und Berichterstattung**: Dokumentation und Kommunikation

## Vorlagen-Organisation

Die Vorlagen sind thematisch organisiert und verwenden ein numerisches Präfix-System:

### Risikomanagement-Prinzipien (0010-0099)
- `0010_risk_management_overview.md` - Risikomanagement Übersicht
- `0020_integrated_principle.md` - Prinzip 1: Integriert
- `0030_structured_comprehensive_principle.md` - Prinzip 2: Strukturiert und umfassend
- `0040_customized_principle.md` - Prinzip 3: Angepasst
- `0050_inclusive_dynamic_principle.md` - Prinzip 4 & 5: Inklusiv und Dynamisch
- `0060_best_information_principle.md` - Prinzip 6: Beste verfügbare Informationen
- `0070_human_cultural_factors_principle.md` - Prinzip 7: Menschliche und kulturelle Faktoren
- `0080_continual_improvement_principle.md` - Prinzip 8: Kontinuierliche Verbesserung

### Risikomanagement-Framework (0100-0199)
- `0100_framework_overview.md` - Framework Übersicht
- `0110_leadership_commitment.md` - Führung und Verpflichtung
- `0120_integration.md` - Integration
- `0130_framework_design.md` - Framework-Design
- `0140_framework_implementation.md` - Framework-Implementierung
- `0150_framework_evaluation.md` - Framework-Bewertung
- `0160_framework_improvement.md` - Framework-Verbesserung

### Risikobeurteilungsprozess (0200-0299)
- `0200_risk_assessment_overview.md` - Risikobeurteilung Übersicht
- `0210_scope_context.md` - Festlegung des Kontexts
- `0220_risk_identification.md` - Risikoidentifikation
- `0230_risk_analysis.md` - Risikoanalyse
- `0240_risk_evaluation.md` - Risikobewertung

### Risikobehandlung und Kommunikation (0300-0399)
- `0300_risk_treatment_overview.md` - Risikobehandlung Übersicht
- `0310_treatment_options.md` - Behandlungsoptionen
- `0320_treatment_plans.md` - Behandlungspläne
- `0330_treatment_implementation.md` - Umsetzung der Behandlung
- `0340_communication_consultation.md` - Kommunikation und Konsultation
- `0350_recording_reporting.md` - Aufzeichnung und Berichterstattung

### Überwachung und Überprüfung (0400-0499)
- `0400_monitoring_review_overview.md` - Überwachung und Überprüfung Übersicht
- `0410_performance_monitoring.md` - Leistungsüberwachung
- `0420_risk_register_maintenance.md` - Risikoregister-Pflege
- `0430_review_processes.md` - Überprüfungsprozesse
- `0440_lessons_learned.md` - Lessons Learned

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
- `{{ meta-organisation-roles.role_CEO }}` - Name des CEO
- `{{ meta-organisation-roles.role_Risk_Manager }}` - Name des Chief Risk Officer

### Datenquellen-Platzhalter
- `[TODO]` - Organisationsname aus Datenquelle
- `[TODO]` - Autor aus Datenquelle
- Weitere organisationsspezifische Felder

## Anpassung der Vorlagen

### 1. Metadaten aktualisieren
Beginnen Sie mit der Datei `0000_metadata_de_iso-31000.md` und füllen Sie die Metadaten aus.

### 2. Platzhalter ersetzen
Ersetzen Sie alle `{{ placeholder }}` mit Ihren organisationsspezifischen Informationen.

### 3. Inhalte anpassen
Passen Sie die Vorlagen an Ihre spezifischen Anforderungen an:
- Fügen Sie organisationsspezifische Risikokategorien hinzu
- Definieren Sie Ihren Risikoappetit und Risikotoleranz
- Passen Sie Bewertungskriterien an
- Erweitern Sie Abschnitte nach Bedarf

### 4. Dokumentenverweise aktualisieren
Stellen Sie sicher, dass alle Querverweise zwischen Dokumenten korrekt sind.

## Verwendung mit dem Handbuch-Generator

Diese Vorlagen sind für die Verwendung mit dem Handbuch-Generator-System konzipiert:

```bash
python handbook-generator --template iso-31000 --language de --output-format html
```

Unterstützte Ausgabeformate:
- HTML (Mini-Website mit Navigation)
- PDF (mit Inhaltsverzeichnis)
- Markdown (kombiniert oder separate Dateien)

## Framework-Referenz

Weitere Informationen zu ISO 31000:
- [ISO 31000:2018](https://www.iso.org/standard/65694.html)
- ISO 31000:2018 - Risk management — Guidelines

## Framework-Mapping

Siehe `FRAMEWORK_MAPPING.md` für eine detaillierte Zuordnung der Vorlagen zu ISO 31000 Komponenten und Klauseln.

## Lizenz

Diese Vorlagen basieren auf ISO 31000:2018. Der Standard selbst ist urheberrechtlich geschützt.

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2024 | Initiale Version basierend auf ISO 31000:2018 |

