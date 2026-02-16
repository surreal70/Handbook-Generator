# DORA Metrics Handbuch-Templates

## Übersicht

Dieses Verzeichnis enthält Templates für ein DORA (DevOps Research and Assessment) Metrics Handbuch. DORA Metrics sind wissenschaftlich fundierte Leistungsindikatoren für Software-Delivery-Performance.

## Die Vier Kernmetriken

1. **Deployment Frequency** - Wie oft wird Code in Produktion deployed
2. **Lead Time for Changes** - Zeit von Commit bis Production
3. **Mean Time to Restore (MTTR)** - Zeit zur Wiederherstellung nach Incidents
4. **Change Failure Rate** - Prozentsatz fehlgeschlagener Deployments

## Template-Organisation

Die Templates sind nach Themen in Nummernbereichen organisiert:

### 0010-0099: DORA Framework Übersicht
- 0010: DORA Framework Übersicht
- 0020: Software Delivery Performance
- 0030: Organisatorische Performance
- 0040: Performance Benchmarking
- 0050: Reifegrad-Assessment

### 0100-0199: Deployment Frequency
- 0100: Deployment Frequency Übersicht
- 0110: Deployment Frequency Messung
- 0120: Deployment-Automatisierung
- 0130: Deployment-Pipeline
- 0140: Deployment Frequency Verbesserung

### 0200-0299: Lead Time for Changes
- 0200: Lead Time Übersicht
- 0210: Lead Time Messung
- 0220: Value Stream Mapping
- 0230: Bottleneck-Identifikation
- 0240: Lead Time Reduktionsstrategien

### 0300-0399: Mean Time to Restore (MTTR)
- 0300: MTTR Übersicht
- 0310: MTTR Messung
- 0320: Incident-Erkennung
- 0330: Incident-Response-Prozeduren
- 0340: Recovery-Automatisierung
- 0350: MTTR Verbesserung

### 0400-0499: Change Failure Rate und Technical Practices
- 0400: Change Failure Rate Übersicht
- 0410: CFR Messung
- 0420: Quality Assurance Praktiken
- 0430: Testing-Strategien
- 0440: CI/CD Praktiken
- 0450: Monitoring und Observability
- 0460: Technical Debt Management

## Verwendung

### Handbuch generieren

```bash
python handbook-generator --template dora --language de --output test-output/de/dora/
```

### Platzhalter

Die Templates verwenden Platzhalter im Format `{{ source.field }}` für organisationsspezifische Daten:

- `{{ source.organization_name }}` - Name der Organisation
- `{{ source.dora_owner }}` - Verantwortlicher für DORA-Implementierung
- `{{ source.current_deployment_frequency }}` - Aktuelle Deployment Frequency
- `{{ source.current_lead_time }}` - Aktuelle Lead Time
- `{{ source.current_mttr }}` - Aktuelle MTTR
- `{{ source.current_cfr }}` - Aktuelle Change Failure Rate

### Anpassung

1. Kopieren Sie die Templates in Ihr Projekt
2. Passen Sie die Platzhalter an Ihre Organisation an
3. Ergänzen Sie organisationsspezifische Inhalte
4. Generieren Sie das Handbuch

## Performance-Level

DORA definiert vier Performance-Level:

- **Elite**: Top-Performer (z.B. Deployment Frequency: On-demand)
- **High**: Überdurchschnittliche Performance
- **Medium**: Durchschnittliche Performance
- **Low**: Unterdurchschnittliche Performance

## Referenzen

- [DORA State of DevOps Reports](https://dora.dev/)
- [Accelerate: The Science of Lean Software and DevOps](https://itrevolution.com/product/accelerate/)
- [DORA Metrics Guide](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)

## Lizenz

Diese Templates sind Teil des Handbook-Generator-Projekts.

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |
