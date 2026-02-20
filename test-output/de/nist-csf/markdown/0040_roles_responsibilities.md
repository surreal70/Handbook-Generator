
Document-ID: nist-csf-0040
Owner: [TODO]

Status: Draft
Classification: Internal

# Rollen und Verantwortlichkeiten (GV.RR)

**Dokument-ID:** NIST-CSF-0040
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---

## Zweck

Dieses Dokument definiert die Rollen, Verantwortlichkeiten und Befugnisse für Cybersecurity-Risikomanagement innerhalb der Organisation.

## Geltungsbereich

[TODO]

## Governance-Struktur

### Vorstand
**Verantwortlichkeiten:**
- Strategische Aufsicht über Cybersecurity-Risiken
- Genehmigung der Cybersecurity-Strategie und -Richtlinien
- Überwachung der Cybersecurity-Leistung
- Ressourcenzuweisung für Cybersecurity-Initiativen

### Geschäftsführung
**Verantwortlichkeiten:**
- Umsetzung der Cybersecurity-Strategie
- Bereitstellung von Ressourcen und Unterstützung
- Förderung einer Sicherheitskultur
- Eskalation kritischer Risiken an den Vorstand

## Cybersecurity-Rollen

### Chief Information Security Officer (CISO)
**Name:** [TODO]  
**Verantwortlichkeiten:**
- Gesamtverantwortung für Cybersecurity-Programm
- Entwicklung und Pflege der Cybersecurity-Strategie
- Risikomanagement und Compliance-Überwachung
- Berichterstattung an Geschäftsführung und Vorstand
- Leitung des Cybersecurity-Teams

**Befugnisse:**
- Genehmigung von Sicherheitsrichtlinien
- Budgetverantwortung für Cybersecurity
- Eskalation von Sicherheitsvorfällen
- Durchsetzung von Sicherheitsanforderungen

### Chief Risk Officer (CRO)
**Name:** [TODO]  
**Verantwortlichkeiten:**
- Integration von Cybersecurity-Risiken in ERM
- Risikobewertung und -berichterstattung
- Koordination mit CISO bei Risikobehandlung

### Security Operations Manager
**Name:** {{ meta-handbook.security_ops_manager }}  
**Verantwortlichkeiten:**
- Täglicher Betrieb des Security Operations Center (SOC)
- Incident Response und Management
- Security Monitoring und Threat Detection
- Koordination mit IT-Operations

### Security Architect
**Name:** {{ meta-handbook.security_architect }}  
**Verantwortlichkeiten:**
- Design sicherer Systemarchitekturen
- Sicherheitsanforderungen für neue Projekte
- Technologie-Evaluierung und -Auswahl
- Security-by-Design-Prinzipien

### Compliance Manager
**Name:** [TODO]  
**Verantwortlichkeiten:**
- Überwachung regulatorischer Compliance
- Durchführung von Compliance-Assessments
- Koordination von Audits
- Pflege von Compliance-Dokumentation

## Geschäftsbereichs-Verantwortlichkeiten

### IT-Abteilung
**Leiter:** [TODO]  
**Verantwortlichkeiten:**
- Implementierung von Sicherheitskontrollen
- Patch-Management und Systemhärtung
- Zugriffsverwaltung
- Backup und Recovery

### Human Resources
**Leiter:** [TODO]  
**Verantwortlichkeiten:**
- Sicherheitsschulungen für Mitarbeiter
- Hintergrundüberprüfungen
- Onboarding/Offboarding-Prozesse
- Durchsetzung von Sicherheitsrichtlinien

### Legal/Compliance
**Leiter:** {{ meta-handbook.legal_director }}  
**Verantwortlichkeiten:**
- Rechtliche Beratung zu Cybersecurity
- Vertragsüberprüfung (Sicherheitsklauseln)
- Datenschutz-Compliance
- Incident Response (rechtliche Aspekte)

### Procurement
**Leiter:** {{ meta-handbook.procurement_director }}  
**Verantwortlichkeiten:**
- Lieferanten-Sicherheitsbewertungen
- Sicherheitsanforderungen in Verträgen
- Third-Party Risk Management

## Mitarbeiter-Verantwortlichkeiten

### Alle Mitarbeiter
**Verantwortlichkeiten:**
- Einhaltung von Sicherheitsrichtlinien
- Meldung von Sicherheitsvorfällen
- Teilnahme an Sicherheitsschulungen
- Schutz von Zugangsdaten und Daten

## RACI-Matrix

| Aktivität | CISO | CRO | Sec Ops | IT | HR | Legal |
|-----------|------|-----|---------|----|----|-------|
| Strategie-Entwicklung | A | C | I | I | I | C |
| Risikobewertung | R | A | C | C | I | C |
| Incident Response | A | I | R | C | I | C |
| Policy-Entwicklung | A | C | C | C | C | R |
| Schulungen | C | I | I | I | A | C |
| Compliance-Audits | C | C | I | C | I | A |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Eskalationspfade

### Sicherheitsvorfälle
1. Erkennung → Security Operations
2. Bewertung → CISO
3. Kritische Vorfälle → Geschäftsführung
4. Existenzbedrohende Vorfälle → Vorstand

### Risiken
1. Identifikation → Risikomanager
2. Bewertung → CRO
3. Hohe Risiken → CISO
4. Kritische Risiken → Geschäftsführung/Vorstand

## Dokumentenverweise

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0050_policy_framework.md
- 0060_oversight.md

