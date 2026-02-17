
Document-ID: nist-csf-0020
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Organisatorischer Kontext (GV.OC)

**Dokument-ID:** [FRAMEWORK]-0020
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

## Zweck

Dieses Dokument definiert den organisatorischen Kontext für das Cybersecurity-Risikomanagement, einschließlich Mission, Stakeholder-Erwartungen und rechtlicher/regulatorischer Anforderungen.

## Geltungsbereich

{{ meta-handbook.scope }}

## Organisationsmission und -ziele

### Unternehmensmission
{{ meta-handbook.organization_mission }}

### Geschäftsziele
1. {{ meta.business_goal_1 }}
2. {{ meta.business_goal_2 }}
3. {{ meta.business_goal_3 }}

### Cybersecurity-Ziele
- Schutz kritischer Geschäftsprozesse und -daten
- Aufrechterhaltung des Kundenvertrauens
- Einhaltung regulatorischer Anforderungen
- Minimierung von Cybersecurity-Risiken

## Stakeholder-Analyse

### Interne Stakeholder

| Stakeholder | Erwartungen | Kommunikationskanal |
|-------------|-------------|---------------------|
| Vorstand | Risikotransparenz, Compliance | Quartalsberichte |
| Geschäftsführung | Geschäftskontinuität | Monatliche Reviews |
| IT-Abteilung | Klare Richtlinien, Ressourcen | Wöchentliche Meetings |
| Mitarbeiter | Sichere Arbeitsumgebung | Schulungen, Intranet |

### Externe Stakeholder

| Stakeholder | Erwartungen | Kommunikationskanal |
|-------------|-------------|---------------------|
| Kunden | Datenschutz, Verfügbarkeit | Datenschutzerklärung |
| Regulierungsbehörden | Compliance-Nachweise | Berichte, Audits |
| Partner | Sichere Zusammenarbeit | Verträge, SLAs |
| Lieferanten | Sicherheitsanforderungen | Lieferantenverträge |

## Rechtliche und regulatorische Anforderungen

### Anwendbare Gesetze und Vorschriften

1. **Datenschutz**
   - DSGVO (EU-Datenschutz-Grundverordnung)
   - BDSG (Bundesdatenschutzgesetz)
   - {{ meta-handbook.additional_privacy_laws }}

2. **Branchenspezifische Vorschriften**
   - {{ meta.industry_regulation_1 }}
   - {{ meta.industry_regulation_2 }}

3. **Vertragliche Verpflichtungen**
   - Kundenverträge mit Sicherheitsanforderungen
   - Lieferantenvereinbarungen
   - Service Level Agreements (SLAs)

## Kritische Geschäftsfunktionen

### Geschäftsprozesse mit hoher Priorität

| Prozess | Kritikalität | Cybersecurity-Anforderungen |
|---------|--------------|----------------------------|
| {{ meta.critical_process_1 }} | Hoch | Verfügbarkeit, Integrität |
| {{ meta.critical_process_2 }} | Hoch | Vertraulichkeit, Verfügbarkeit |
| {{ meta.critical_process_3 }} | Mittel | Integrität, Nachvollziehbarkeit |

## Risikotoleranz und -appetit

### Risikoappetit-Erklärung
{{ meta-organisation.name }} ist bereit, {{ meta-handbook.risk_appetite_level }} Cybersecurity-Risiken einzugehen, um Geschäftsziele zu erreichen, unter der Bedingung, dass:
- Kritische Systeme angemessen geschützt sind
- Regulatorische Anforderungen erfüllt werden
- Reputationsrisiken minimiert werden

### Risikotoleranz-Schwellenwerte

| Risikokategorie | Toleranzschwelle | Eskalation |
|-----------------|------------------|------------|
| Datenschutzverletzung | Null-Toleranz | Sofortige Eskalation an Vorstand |
| Systemausfall | < 4 Stunden/Jahr | Eskalation an CIO |
| Sicherheitsvorfälle | < 10 Minor/Jahr | Monatliches Review |

## Organisationsstruktur

### Cybersecurity-Governance-Struktur
```
Vorstand
    ↓
Geschäftsführung
    ↓
CISO ({{ meta-organisation-roles.role_CISO }})
    ↓
├── Security Operations
├── Risk Management
├── Compliance
└── Security Architecture
```

## Dokumentenverweise

- 0030_risk_management_strategy.md
- 0040_roles_responsibilities.md
- 0050_policy_framework.md

