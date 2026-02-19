
Document-ID: iso-38500-0080
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Prinzip 5: Konformität (Conformance)

**Dokument-ID:** [FRAMEWORK]-0080
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Zweck

Dieses Dokument beschreibt die Anwendung des Konformitäts-Prinzips in der IT-Governance der Organisation.

## Geltungsbereich

Dieses Dokument gilt für:
- {{ meta-organisation.name }}
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
| Datenschutz | DSGVO, BDSG | {{ meta-handbook.data_protection_status }} |
| IT-Sicherheit | ISO 27001, BSI | {{ meta-handbook.security_status }} |
| Finanzberichterstattung | SOX, HGB | {{ meta-handbook.financial_status }} |
| Branchenspezifisch | {{ meta-handbook.industry_regulations }} | {{ meta-handbook.industry_status }} |

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
| {{ meta-organisation-roles.role_CISO }} | IT-Sicherheits-Compliance |
| {{ meta-organisation-roles.role_GDPR_Manager }} | Datenschutz-Compliance |
| {{ meta-organisation-roles.role_CIO }} | Gesamte IT-Compliance |
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

- Compliance-Rate: {{ meta-handbook.compliance_rate }}%
- Anzahl Compliance-Verstöße: {{ meta-handbook.compliance_violations }}
- Durchschnittliche Behebungszeit: {{ meta-handbook.remediation_time }} Tage
- Audit-Findings: {{ meta-handbook.audit_findings }}
- Richtlinien-Aktualität: {{ meta-handbook.policy_currency }}%

### Compliance-Dashboard

| Anforderung | Status | Letzte Prüfung | Nächste Prüfung |
|-------------|--------|----------------|-----------------|
| DSGVO | {{ meta-handbook.gdpr_status }} | {{ meta-handbook.gdpr_last_audit }} | {{ meta-handbook.gdpr_next_audit }} |
| ISO 27001 | {{ meta-handbook.iso27001_status }} | {{ meta-handbook.iso27001_last_audit }} | {{ meta-handbook.iso27001_next_audit }} |
| BSI Grundschutz | {{ meta-handbook.bsi_status }} | {{ meta-handbook.bsi_last_audit }} | {{ meta-handbook.bsi_next_audit }} |

## Dokumentenverweise

- 0010_governance_framework.md
- 0020_governance_model.md

