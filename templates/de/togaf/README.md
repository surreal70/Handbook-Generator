# TOGAF Enterprise Architecture Handbuch-Vorlagen

## Übersicht

Dieses Verzeichnis enthält Vorlagen zur Erstellung von TOGAF (The Open Group Architecture Framework) Enterprise Architecture-Dokumentation. Die Vorlagen folgen der TOGAF Architecture Development Method (ADM) und bieten umfassende Abdeckung aller ADM-Phasen.

## Framework-Informationen

- **Framework**: The Open Group Architecture Framework (TOGAF)
- **Version**: TOGAF 9.2
- **Sprache**: Deutsch
- **Vorlagenanzahl**: 14+ Vorlagen für alle ADM-Phasen

## Vorlagenorganisation

Vorlagen sind nach TOGAF ADM-Phasen mit einem numerischen Präfix-System organisiert:

### Preliminary Phase und Foundation (0010-0099)
- **0010**: Einrichtung des Architecture Frameworks
- **0020**: Architecture-Prinzipien
- **0030**: Governance Framework
- **0040**: Repository-Struktur
- **0050**: Stakeholder-Management
- **0060**: Werkzeuge und Techniken

### Phase A - Architecture Vision (0100-0199)
- **0100**: Architecture Vision
- **0110**: Geschäftsziele und Treiber

### Phase B - Business Architecture (0200-0299)
- **0200**: Business Architecture Übersicht
- **0210**: Business Capability Model

### Phase C - Information Systems Architecture (0300-0399)
- **0300**: Daten-Architecture
- **0330**: Anwendungs-Architecture

### Phase D - Technology Architecture (0400-0499)
- **0400**: Technologie-Architecture Übersicht

### Phase E - Opportunities and Solutions (0500-0599)
- **0500**: Implementierungsansatz

### Phase F-H - Migration and Governance (0600-0699)
- **0600**: Migrationsplanung

### Requirements Management (0700-0799)
- **0700**: Requirements Management

## Vorlagenstruktur

Jede Vorlage folgt einer konsistenten Struktur:

```markdown
---
Document-ID: togaf-NNNN
Owner: {{ meta-handbook.author }}
Version: {{ meta-handbook.revision }}
Status: Draft
Classification: Internal
Last Update: {{ meta-handbook.modifydate }}
---

# Vorlagentitel

## Zweck
[Beschreibung des Vorlagenzwecks]

## Geltungsbereich
[Was in dieser Vorlage abgedeckt wird]

## Inhaltssektionen
[Hauptinhalt mit Platzhaltern]

<!-- Autorenhinweise: Anleitung für Vorlagenbenutzer -->
```

## Platzhalter-System

Vorlagen verwenden Platzhalter für organisationsspezifische Daten:

- `{{ meta-handbook.author }}` - Dokumentautor
- `{{ meta-handbook.revision }}` - Dokumentversion
- `{{ meta-handbook.modifydate }}` - Dokumentdatum
- `[TODO]` - Organisationsname
- `[TODO]` - Andere organisationsspezifische Felder

## Anpassungsleitfaden

### Schritt 1: Metadaten konfigurieren
Bearbeiten Sie die Metadaten-Vorlage (0000_metadata_de_togaf.md) mit den Informationen Ihrer Organisation.

### Schritt 2: Vorlagen anpassen
Überprüfen Sie jede Vorlage und:
- Füllen Sie Platzhalterwerte aus
- Fügen Sie organisationsspezifische Inhalte hinzu
- Entfernen Sie nicht zutreffende Abschnitte
- Fügen Sie bei Bedarf zusätzliche Abschnitte hinzu

### Schritt 3: An Ihren Kontext anpassen
- Passen Sie Governance-Strukturen an Ihre Organisation an
- Modifizieren Sie Capability Models für Ihr Geschäft
- Passen Sie Technologie-Standards an Ihre Umgebung an
- Richten Sie sich an bestehenden Prozessen und Methoden aus

### Schritt 4: Pflegen und Aktualisieren
- Überprüfen Sie Vorlagen regelmäßig
- Aktualisieren Sie basierend auf Architecture-Änderungen
- Integrieren Sie Lessons Learned
- Halten Sie die Ausrichtung an TOGAF-Updates

## Nutzungsrichtlinien

### Für Enterprise Architects
- Verwenden Sie Vorlagen als Ausgangspunkte für Architecture-Dokumentation
- Passen Sie basierend auf Stakeholder-Bedürfnissen an
- Wahren Sie Konsistenz über Architecture-Artefakte hinweg
- Verknüpfen Sie verwandte Dokumente und Artefakte

### Für Architecture-Teams
- Folgen Sie dem ADM-Zyklus systematisch
- Dokumentieren Sie Entscheidungen mit Architecture Decision Records (ADRs)
- Wahren Sie Traceability zwischen Requirements und Architecture
- Binden Sie Stakeholder während des gesamten Prozesses ein

### Für Projektteams
- Referenzieren Sie Architecture-Vorlagen für Projektplanung
- Stellen Sie sicher, dass Projekt-Architectures mit Enterprise Architecture übereinstimmen
- Reichen Sie Architecture zur Compliance-Prüfung ein
- Dokumentieren Sie Abweichungen und Ausnahmen

## Integration mit TOGAF ADM

Diese Vorlagen unterstützen den vollständigen TOGAF ADM-Zyklus:

1. **Preliminary Phase**: Etablierung der Architecture Capability
2. **Phase A**: Definition der Architecture Vision
3. **Phase B**: Entwicklung der Business Architecture
4. **Phase C**: Entwicklung der Information Systems Architecture
5. **Phase D**: Entwicklung der Technology Architecture
6. **Phase E**: Identifikation von Opportunities and Solutions
7. **Phase F**: Planung der Migration
8. **Phase G**: Implementierung der Governance
9. **Phase H**: Management von Architecture-Änderungen
10. **Requirements Management**: Kontinuierlich während des gesamten Prozesses

## Zusätzliche Ressourcen

- **FRAMEWORK_MAPPING.md**: Mapping von Vorlagen zu TOGAF ADM-Phasen und Ergebnissen
- **diagrams/**: Verzeichnis für Architecture-Diagramme und Visualisierungen
- **TOGAF-Dokumentation**: https://www.opengroup.org/togaf

## Support und Feedback

Für Fragen oder Vorschläge zu diesen Vorlagen:
- Kontaktieren Sie das Enterprise Architecture-Team
- Reichen Sie Feedback über das Architecture Repository ein
- Nehmen Sie an Architecture Governance-Meetings teil

---

*Diese Vorlagen basieren auf TOGAF 9.2 und sollten an die spezifischen Bedürfnisse und den Kontext Ihrer Organisation angepasst werden.*
