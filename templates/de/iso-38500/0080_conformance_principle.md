---
Document-ID: iso-38500-0080
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Prinzip 5: Konformität (Conformance)

## Zweck

Dieses Dokument beschreibt die Anwendung des Konformitäts-Prinzips in der IT-Governance der Organisation.

## Geltungsbereich

Dieses Dokument gilt für:
- {{ meta.organization }}
- Alle IT-Compliance-Anforderungen
- Gesetzliche, regulatorische und interne Verpflichtungen

## Prinzip-Definition

IT erfüllt alle obligatorischen Gesetze und Vorschriften. Richtlinien und Praktiken sind klar definiert, implementiert und durchgesetzt.

## Evaluate (Bewerten)

### Compliance-Anforderungen bewerten

- Welche gesetzlichen Anforderungen gelten?
- Welche regulatorischen Standards sind relevant?
- Sind interne Richtlinien aktuell?
- Gibt es Compliance-Lücken?

### Compliance-Bereiche

| Bereich | Anforderungen | Status |
|---------|---------------|--------|
| Datenschutz | DSGVO, BDSG | {{ meta.data_protection_status }} |
| IT-Sicherheit | ISO 27001, BSI | {{ meta.security_status }} |
| Finanzberichterstattung | SOX, HGB | {{ meta.financial_status }} |
| Branchenspezifisch | {{ meta.industry_regulations }} | {{ meta.industry_status }} |

## Direct (Steuern)

### Compliance-Framework

**Gesetzliche Anforderungen:**
- Datenschutz (DSGVO)
- IT-Sicherheit (BSI IT-Grundschutz)
- Archivierung (GoBD)
- Arbeitsrecht

**Regulatorische Standards:**
- ISO/IEC 27001
- ISO/IEC 20000
- ITIL
- COBIT

**Interne Richtlinien:**
- IT-Sicherheitsrichtlinie
- Datenschutzrichtlinie
- Nutzungsrichtlinien
- Compliance-Richtlinie

### Compliance-Prozesse

1. **Anforderungsmanagement**: Identifikation und Dokumentation
2. **Gap-Analyse**: Soll-Ist-Vergleich
3. **Maßnahmenplanung**: Compliance-Maßnahmen definieren
4. **Implementierung**: Umsetzung der Maßnahmen
5. **Überwachung**: Kontinuierliche Kontrolle
6. **Audit**: Regelmäßige Überprüfung
7. **Verbesserung**: Kontinuierliche Optimierung

### Verantwortlichkeiten

| Rolle | Verantwortung |
|-------|---------------|
| {{ meta.ciso }} | IT-Sicherheits-Compliance |
| {{ meta.dpo }} | Datenschutz-Compliance |
| {{ meta.cio }} | Gesamte IT-Compliance |
| Compliance Officer | Compliance-Überwachung |
| Interne Revision | Compliance-Audits |

## Monitor (Überwachen)

### Überwachungsmaßnahmen

1. **Compliance-Monitoring**: Kontinuierliche Überwachung
2. **Interne Audits**: Quartalsweise
3. **Externe Audits**: Jährlich
4. **Compliance-Reports**: Monatlich an Geschäftsführung
5. **Incident-Tracking**: Compliance-Verstöße dokumentieren

### KPIs

- Compliance-Rate: {{ meta.compliance_rate }}%
- Anzahl Compliance-Verstöße: {{ meta.compliance_violations }}
- Durchschnittliche Behebungszeit: {{ meta.remediation_time }} Tage
- Audit-Findings: {{ meta.audit_findings }}
- Richtlinien-Aktualität: {{ meta.policy_currency }}%

### Compliance-Dashboard

| Anforderung | Status | Letzte Prüfung | Nächste Prüfung |
|-------------|--------|----------------|-----------------|
| DSGVO | {{ meta.gdpr_status }} | {{ meta.gdpr_last_audit }} | {{ meta.gdpr_next_audit }} |
| ISO 27001 | {{ meta.iso27001_status }} | {{ meta.iso27001_last_audit }} | {{ meta.iso27001_next_audit }} |
| BSI Grundschutz | {{ meta.bsi_status }} | {{ meta.bsi_last_audit }} | {{ meta.bsi_next_audit }} |

## Dokumentenverweise

- 0010_governance_framework.md
- 0020_governance_model.md

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |

