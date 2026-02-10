# NIST Cybersecurity Framework 2.0 Handbuch-Vorlagen

## Überblick

Dieses Verzeichnis enthält Vorlagen für die Erstellung eines NIST Cybersecurity Framework (CSF) 2.0 Handbuchs. Die Vorlagen decken alle sechs Kernfunktionen des Frameworks ab: Govern, Identify, Protect, Detect, Respond und Recover.

## NIST CSF 2.0 Struktur

Das NIST Cybersecurity Framework 2.0 ist ein freiwilliges Framework, das aus Standards, Richtlinien und Best Practices besteht, um Cybersecurity-Risiken zu managen. Version 2.0 führt die neue **Govern**-Funktion ein, die die Grundlage für alle anderen Funktionen bildet.

### Die sechs Kernfunktionen

1. **Govern (GV)**: Etabliert und überwacht die Cybersecurity-Risikomanagement-Strategie der Organisation
2. **Identify (ID)**: Entwickelt organisatorisches Verständnis für das Management von Cybersecurity-Risiken
3. **Protect (PR)**: Entwickelt und implementiert Schutzmaßnahmen
4. **Detect (DE)**: Entwickelt und implementiert Aktivitäten zur Erkennung von Cybersecurity-Ereignissen
5. **Respond (RS)**: Entwickelt und implementiert Aktivitäten zur Reaktion auf erkannte Cybersecurity-Vorfälle
6. **Recover (RC)**: Entwickelt und implementiert Aktivitäten zur Wiederherstellung nach Cybersecurity-Vorfällen

## Vorlagen-Organisation

Die Vorlagen sind nach Funktionen organisiert und verwenden ein numerisches Präfix-System:

### Govern-Funktion (0010-0099)
- `0010_govern_overview.md` - Übersicht über die Govern-Funktion
- `0020_organizational_context.md` - Organisatorischer Kontext (GV.OC)
- `0030_risk_management_strategy.md` - Risikomanagement-Strategie (GV.RM)
- `0040_roles_responsibilities.md` - Rollen und Verantwortlichkeiten (GV.RR)
- `0050_policy_framework.md` - Richtlinien-Rahmenwerk (GV.PO)
- `0060_oversight.md` - Aufsicht und Überwachung (GV.OV)
- `0070_supply_chain_risk_management.md` - Lieferketten-Risikomanagement (GV.SC)

### Identify-Funktion (0100-0199)
- `0100_asset_management.md` - Asset Management (ID.AM)
- `0110_business_environment.md` - Geschäftsumfeld (ID.BE)
- `0120_governance.md` - Governance (ID.GV)
- `0130_risk_assessment.md` - Risikobewertung (ID.RA)
- `0140_risk_management_strategy.md` - Risikomanagement-Strategie (ID.RM)
- `0150_supply_chain_risk_management.md` - Lieferketten-Risikomanagement (ID.SC)

### Protect-Funktion (0200-0299)
- `0200_identity_access_control.md` - Identitäts- und Zugriffsmanagement (PR.AA)
- `0210_awareness_training.md` - Awareness und Schulung (PR.AT)
- `0220_data_security.md` - Datensicherheit (PR.DS)
- `0230_information_protection_processes.md` - Informationsschutz-Prozesse (PR.IP)
- `0240_maintenance.md` - Wartung (PR.MA)
- `0250_protective_technology.md` - Schutztechnologie (PR.PT)

### Detect-Funktion (0300-0399)
- `0300_anomalies_events.md` - Anomalien und Ereignisse (DE.AE)
- `0310_security_monitoring.md` - Sicherheitsüberwachung (DE.CM)
- `0320_detection_processes.md` - Erkennungsprozesse (DE.DP)

### Respond-Funktion (0400-0499)
- `0400_response_planning.md` - Response-Planung (RS.RP)
- `0410_communications.md` - Kommunikation (RS.CO)
- `0420_analysis.md` - Analyse (RS.AN)
- `0430_mitigation.md` - Eindämmung (RS.MI)
- `0440_improvements.md` - Verbesserungen (RS.IM)

### Recover-Funktion (0500-0599)
- `0500_recovery_planning.md` - Wiederherstellungsplanung (RC.RP)
- `0510_improvements.md` - Verbesserungen (RC.IM)
- `0520_communications.md` - Kommunikation (RC.CO)

### Implementierung und Bewertung (0600-0699)
- `0600_implementation_tiers.md` - Implementierungsstufen
- `0610_current_profile.md` - Aktuelles Profil
- `0620_target_profile.md` - Zielprofil
- `0630_gap_analysis.md` - Gap-Analyse
- `0640_action_plan.md` - Aktionsplan

## Nummerierungsschema

- Vorlagen verwenden 4-stellige Präfixe (z.B. 0010, 0020, 0030)
- Inkremente von 10 ermöglichen zukünftige Einfügungen
- Funktionen sind in Hunderterbereiche gruppiert (0000-0099, 0100-0199, etc.)

## Platzhalter-System

Die Vorlagen verwenden Platzhalter für organisationsspezifische Daten:

### Metadaten-Platzhalter
- `{{ meta.owner }}` - Dokumentenverantwortlicher
- `{{ meta.version }}` - Versionsnummer
- `{{ meta.date }}` - Datum
- `{{ meta.organization }}` - Organisationsname
- `{{ meta.ciso }}` - Name des CISO
- `{{ meta.cro }}` - Name des CRO

### Datenquellen-Platzhalter
- `{{ source.organization_name }}` - Organisationsname aus Datenquelle
- `{{ source.author }}` - Autor aus Datenquelle
- Weitere organisationsspezifische Felder

## Anpassung der Vorlagen

### 1. Metadaten aktualisieren
Beginnen Sie mit der Datei `0000_metadata_de_nist-csf.md` und füllen Sie die Metadaten aus.

### 2. Platzhalter ersetzen
Ersetzen Sie alle `{{ placeholder }}` mit Ihren organisationsspezifischen Informationen.

### 3. Inhalte anpassen
Passen Sie die Vorlagen an Ihre spezifischen Anforderungen an:
- Fügen Sie organisationsspezifische Prozesse hinzu
- Entfernen Sie nicht zutreffende Abschnitte
- Erweitern Sie Abschnitte nach Bedarf

### 4. Dokumentenverweise aktualisieren
Stellen Sie sicher, dass alle Querverweise zwischen Dokumenten korrekt sind.

## Verwendung mit dem Handbuch-Generator

Diese Vorlagen sind für die Verwendung mit dem Handbuch-Generator-System konzipiert:

```bash
python handbook-generator --template nist-csf --language de --output-format html
```

Unterstützte Ausgabeformate:
- HTML (Mini-Website mit Navigation)
- PDF (mit Inhaltsverzeichnis)
- Markdown (kombiniert oder separate Dateien)

## Framework-Referenz

Weitere Informationen zum NIST Cybersecurity Framework 2.0:
- [NIST CSF 2.0 Website](https://www.nist.gov/cyberframework)
- [NIST CSF 2.0 Framework](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)

## Framework-Mapping

Siehe `FRAMEWORK_MAPPING.md` für eine detaillierte Zuordnung der Vorlagen zu NIST CSF 2.0 Kategorien und Unterkategorien.

## Lizenz

Diese Vorlagen basieren auf dem NIST Cybersecurity Framework 2.0, das gemeinfrei ist.

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2024 | Initiale Version basierend auf NIST CSF 2.0 |
