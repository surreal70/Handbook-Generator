---
Document-ID: nist-csf-0060
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Aufsicht und Überwachung (GV.OV)

## Zweck

Dieses Dokument beschreibt die Aufsichts- und Überwachungsmechanismen für das Cybersecurity-Programm der Organisation.

## Geltungsbereich

{{ meta.scope }}

## Governance-Aufsicht

### Vorstand
**Rolle:** Strategische Aufsicht  
**Häufigkeit:** Quartalsweise

**Aufsichtsaktivitäten:**
- Review des Cybersecurity-Risikoprofils
- Genehmigung strategischer Initiativen
- Überwachung der Compliance
- Bewertung der Cybersecurity-Investitionen

**Berichterstattung:**
- Risiko-Dashboard
- Kritische Vorfälle
- Compliance-Status
- Budget und Ressourcen

### Geschäftsführung
**Rolle:** Operative Aufsicht  
**Häufigkeit:** Monatlich

**Aufsichtsaktivitäten:**
- Überwachung der Programmumsetzung
- Ressourcenzuweisung
- Eskalationsmanagement
- Performance-Review

## Cybersecurity-Komitees

### Cybersecurity Steering Committee
**Vorsitz:** {{ meta.ciso }}  
**Mitglieder:**
- CIO
- CRO
- CFO
- Geschäftsbereichsleiter
- Legal Counsel

**Häufigkeit:** Monatlich

**Aufgaben:**
- Strategische Ausrichtung
- Priorisierung von Initiativen
- Budgetgenehmigung
- Risikobewertung und -behandlung

### Security Operations Committee
**Vorsitz:** {{ meta.security_ops_manager }}  
**Mitglieder:**
- IT Operations
- Network Team
- Application Security
- Incident Response Team

**Häufigkeit:** Wöchentlich

**Aufgaben:**
- Operative Sicherheitsüberwachung
- Incident-Koordination
- Threat Intelligence Sharing
- Technische Entscheidungen

### Risk Management Committee
**Vorsitz:** {{ meta.cro }}  
**Mitglieder:**
- CISO
- Business Unit Heads
- Compliance Manager
- Internal Audit

**Häufigkeit:** Quartalsweise

**Aufgaben:**
- Risikobewertung und -priorisierung
- Risikobehandlungsstrategien
- Risikotoleranz-Review
- Integration mit ERM

## Performance-Metriken

### Key Performance Indicators (KPIs)

| KPI | Zielwert | Messhäufigkeit | Verantwortlich |
|-----|----------|----------------|----------------|
| Patch-Compliance | > 95% | Wöchentlich | IT Operations |
| Incident Response Time | < 4 Stunden | Täglich | SOC |
| Security Training Completion | 100% | Monatlich | HR |
| Vulnerability Remediation | < 30 Tage | Wöchentlich | Security Team |
| Phishing Test Success Rate | < 5% Click Rate | Quartalsweise | Security Awareness |

### Key Risk Indicators (KRIs)

| KRI | Schwellenwert | Messhäufigkeit | Eskalation |
|-----|---------------|----------------|------------|
| Kritische Schwachstellen | > 10 | Täglich | CISO |
| Failed Login Attempts | > 1000/Tag | Täglich | SOC |
| Unpatched Systems | > 5% | Wöchentlich | IT Director |
| Data Exfiltration Attempts | > 0 | Echtzeit | CISO, Geschäftsführung |

## Berichtswesen

### Vorstandsberichte
**Häufigkeit:** Quartalsweise  
**Inhalt:**
- Executive Summary
- Risikoprofil und Trends
- Kritische Vorfälle
- Compliance-Status
- Strategische Initiativen
- Budget und Ressourcen

**Format:** Präsentation + schriftlicher Bericht

### Management-Berichte
**Häufigkeit:** Monatlich  
**Inhalt:**
- Aktuelle Risiken
- Vorfallsstatistiken
- KPI/KRI-Dashboard
- Projektfortschritt
- Ressourcenauslastung

**Format:** Dashboard + Zusammenfassung

### Operative Berichte
**Häufigkeit:** Wöchentlich  
**Inhalt:**
- Sicherheitsvorfälle
- Threat Intelligence
- Schwachstellen-Status
- Patch-Compliance
- Anomalien und Trends

**Format:** Technischer Bericht

## Audit und Compliance

### Interne Audits
**Häufigkeit:** Jährlich  
**Durchführung:** Internal Audit Department  
**Umfang:**
- Richtlinien-Compliance
- Kontrollen-Wirksamkeit
- Prozess-Adherence
- Dokumentation

### Externe Audits
**Häufigkeit:** Jährlich oder nach Bedarf  
**Durchführung:** Externe Prüfer  
**Umfang:**
- Regulatorische Compliance
- Zertifizierungen (ISO 27001, etc.)
- Penetrationstests
- Security Assessments

### Compliance-Überwachung
**Häufigkeit:** Kontinuierlich  
**Mechanismen:**
- Automatisierte Compliance-Checks
- Policy Violation Monitoring
- Access Reviews
- Configuration Audits

## Kontinuierliche Verbesserung

### Lessons Learned
- Post-Incident Reviews
- Audit-Findings-Analyse
- Best Practice Sharing
- Prozessoptimierung

### Programm-Bewertung
**Häufigkeit:** Jährlich  
**Methodik:**
- Maturity Assessment (NIST CSF)
- Gap-Analyse
- Benchmark mit Industrie
- Stakeholder-Feedback

### Verbesserungsmaßnahmen
- Priorisierung basierend auf Risiko
- Ressourcenzuweisung
- Implementierungsplanung
- Fortschrittsüberwachung

## Eskalationsprozesse

### Incident Escalation
1. **Level 1:** SOC Analyst → SOC Manager
2. **Level 2:** SOC Manager → CISO
3. **Level 3:** CISO → Geschäftsführung
4. **Level 4:** Geschäftsführung → Vorstand

### Risk Escalation
1. **Niedrig/Mittel:** Risk Manager
2. **Hoch:** CISO + CRO
3. **Kritisch:** Geschäftsführung
4. **Existenzbedrohend:** Vorstand

## Dokumentenverweise

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0040_roles_responsibilities.md
- 0050_policy_framework.md

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |

<!-- 
Autor-Hinweise:
- Passen Sie Berichtsformate an Zielgruppen an
- Stellen Sie sicher, dass Metriken aussagekräftig sind
- Überprüfen Sie Eskalationsprozesse regelmäßig
-->
