# Schulung, Awareness und Kompetenz

**Dokument-ID:** 0120
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

<!-- 
TEMPLATE AUTHOR NOTE:
This document defines the security awareness and training program. It ensures
that all personnel are aware of their information security responsibilities
and have the necessary competence to fulfill their roles.

ISO 27001:2022 Reference: Clause 7.2 - Competence, Clause 7.3 - Awareness
-->

## 1. Zweck und Ziele

### 1.1 Zweck

Das Schulungs- und Awareness-Programm der **{{ meta-organisation.name }}** stellt sicher, dass:
- Alle Mitarbeiter ihre Sicherheitsverantwortlichkeiten kennen
- Mitarbeiter die notwendigen Kompetenzen für ihre Rollen haben
- Sicherheitsbewusstsein kontinuierlich gefördert wird
- Compliance mit ISO 27001:2022 und anderen Anforderungen sichergestellt wird

### 1.2 Ziele

- **100% Schulungsteilnahme:** Alle Mitarbeiter absolvieren jährlich Security Awareness Training
- **Phishing-Resilienz:** Klickrate bei Phishing-Simulationen < 5%
- **Incident Reporting:** Erhöhung der gemeldeten Sicherheitsvorfälle durch Mitarbeiter
- **Kompetenzaufbau:** Spezialisierte Schulungen für IT-Security-Rollen

## 2. Zielgruppen

### 2.1 Zielgruppen-Übersicht

| Zielgruppe | Anzahl | Schulungsbedarf | Frequenz | Verantwortlich |
|------------|--------|-----------------|----------|----------------|
| **Alle Mitarbeitenden** | [TODO] | Security Awareness Basics | Jährlich | {{ meta-organisation-roles.role_CISO }} |
| **Admins/Privileged Users** | [TODO] | Advanced Security, Privileged Access | Halbjährlich | {{ meta-organisation-roles.role_CISO }} |
| **Entwickler/DevOps** | [TODO] | Secure Coding, DevSecOps | Halbjährlich | {{ meta-organisation-roles.role_CISO }} |
| **Management** | [TODO] | Security Governance, Risk Management | Jährlich | {{ meta-organisation-roles.role_CISO }} |
| **HR** | [TODO] | HR Security, Onboarding/Offboarding | Jährlich | {{ meta-organisation-roles.role_CISO }} |
| **Dienstleister/Externe** | [TODO] | Security Basics, Compliance | Bei Onboarding | {{ meta-organisation-roles.role_CISO }} |

### 2.2 Rollenspezifische Anforderungen

**IT-Security-Team:**
- ISO 27001 Lead Auditor Training
- Incident Response Training
- Threat Intelligence Training
- Security Tool Training (SIEM, EDR, etc.)

**IT-Betrieb:**
- Secure Configuration Management
- Patch Management
- Backup and Recovery
- Access Management

**Entwickler:**
- OWASP Top 10
- Secure Coding Practices
- Secret Management
- Security Testing (SAST/DAST)

## 3. Schulungsplan

### 3.1 Pflichtschulungen

| Training-ID | Training | Zielgruppe | Frequenz | Dauer | Inhalt | Nachweis | Owner | Status |
|-------------|----------|------------|----------|-------|--------|----------|-------|--------|
| **T-001** | Security Awareness Basics | Alle Mitarbeiter | Jährlich | 60 Min | Phishing, Passwörter, Clean Desk, Incident Reporting | LMS-Zertifikat | {{ meta-organisation-roles.role_CISO }} | Aktiv |
| **T-002** | DSGVO Basics | Alle Mitarbeiter | Jährlich | 30 Min | Datenschutz-Grundlagen, Betroffenenrechte | LMS-Zertifikat | {{ meta-handbook.privacy_dpo }} | Aktiv |
| **T-003** | Phishing Awareness | Alle Mitarbeiter | Quartalsweise | 15 Min | Phishing-Erkennung, Meldung | Simulation-Ergebnis | {{ meta-organisation-roles.role_CISO }} | Aktiv |
| **T-004** | Privileged Access Management | Admins | Halbjährlich | 90 Min | PAM, Least Privilege, Audit Logging | LMS-Zertifikat | {{ meta-organisation-roles.role_CISO }} | Aktiv |
| **T-005** | Secure Coding | Entwickler | Halbjährlich | 120 Min | OWASP Top 10, Input Validation, Secrets | LMS-Zertifikat | {{ meta-organisation-roles.role_CISO }} | Aktiv |
| **T-006** | Incident Response | Security Team | Jährlich | 180 Min | IR-Prozess, Forensik, Communication | Workshop-Teilnahme | {{ meta-organisation-roles.role_CISO }} | Aktiv |

[TODO: Weitere Schulungen hinzufügen]

### 3.2 Optionale Schulungen

| Training | Zielgruppe | Frequenz | Anbieter | Kosten |
|----------|------------|----------|----------|--------|
| ISO 27001 Lead Auditor | Security Team | Einmalig | Extern | [TODO] |
| CISSP/CISM Zertifizierung | Security Team | Einmalig | Extern | [TODO] |
| Cloud Security (AWS/Azure) | IT-Betrieb | Bei Bedarf | Extern | [TODO] |
| Penetration Testing | Security Team | Bei Bedarf | Extern | [TODO] |

### 3.3 Onboarding-Schulungen

**Neue Mitarbeiter:**
- Tag 1: Security Awareness Basics (T-001)
- Tag 1: DSGVO Basics (T-002)
- Woche 1: Rollenspezifische Schulungen

**Externe Dienstleister:**
- Vor Zugriff: Security Basics
- NDA-Unterzeichnung
- Zugriffsrichtlinien

## 4. Awareness-Kampagnen

### 4.1 Regelmäßige Kampagnen

**Monatlich:**
- Security Newsletter
- Security Tip of the Month
- Aktuelle Bedrohungen und Warnungen

**Quartalsweise:**
- Phishing-Simulationen
- Security Quiz mit Preisen
- Lunch & Learn Sessions

**Jährlich:**
- Security Awareness Month (Oktober)
- Security Champions Program
- Poster-Kampagnen

### 4.2 Themen-Schwerpunkte

| Quartal | Thema | Aktivitäten |
|---------|-------|-------------|
| Q1 | Passwort-Sicherheit | MFA-Rollout, Passwort-Manager-Training |
| Q2 | Phishing & Social Engineering | Phishing-Simulation, Awareness-Videos |
| Q3 | Mobile Security | BYOD-Policy, Mobile Device Management |
| Q4 | Incident Response | Incident Reporting, Lessons Learned |

### 4.3 Kommunikationskanäle

- **E-Mail:** Security Newsletter, Warnungen
- **Intranet:** Security-Portal, Policies, FAQs
- **Poster:** Büros, Pausenräume
- **Teams/Slack:** Security-Channel
- **Workshops:** Lunch & Learn, Hands-on-Training

## 5. Phishing-Simulationen

### 5.1 Simulationsprogramm

**Frequenz:** Quartalsweise

**Prozess:**
1. Simulation planen (Thema, Zielgruppe)
2. Phishing-E-Mail versenden
3. Klickrate messen
4. Sofortiges Feedback für Klicker
5. Nachschulung für Risikogruppen
6. Ergebnisse analysieren und berichten

**Zielwerte:**
- Klickrate < 5%
- Melderate > 50%

**Tools:**
- [TODO: KnowBe4, Cofense, etc.]

### 5.2 Eskalation bei hoher Klickrate

**Klickrate > 10%:**
- Zusätzliche Awareness-Kampagne
- Verpflichtende Nachschulung
- Analyse der Ursachen

**Klickrate > 20%:**
- Eskalation an Management
- Intensivierte Schulungsmaßnahmen
- Review des Awareness-Programms

## 6. Wirksamkeitsprüfung

### 6.1 Messmethoden

**Quantitative Metriken:**
- Schulungsteilnahme-Quote
- Phishing-Klickrate
- Quiz-Ergebnisse
- Anzahl gemeldeter Incidents durch Mitarbeiter
- Anzahl Sicherheitsverstöße

**Qualitative Metriken:**
- Feedback-Umfragen
- Interviews mit Stakeholdern
- Beobachtungen (Clean Desk, Screen Lock)

### 6.2 Erfolgskriterien

| Metrik | Zielwert | Aktuell | Status |
|--------|----------|---------|--------|
| Schulungsteilnahme | 100% | [TODO]% | [TODO] |
| Phishing-Klickrate | < 5% | [TODO]% | [TODO] |
| Incident-Meldungen | > 20 pro Quartal | [TODO] | [TODO] |
| Quiz-Erfolgsrate | > 80% | [TODO]% | [TODO] |

### 6.3 Kontinuierliche Verbesserung

**Jährlicher Review:**
- Analyse der Schulungsergebnisse
- Feedback-Auswertung
- Anpassung der Schulungsinhalte
- Identifikation neuer Themen

**Lessons Learned:**
- Aus Security Incidents
- Aus Audit-Findings
- Aus Phishing-Simulationen

## 7. Schulungsnachweise

### 7.1 Dokumentation

**Learning Management System (LMS):**
- Schulungsteilnahme
- Zertifikate
- Quiz-Ergebnisse
- Ablaufdaten

**Manuelle Nachweise:**
- Workshop-Teilnahmelisten
- Externe Zertifikate
- Konferenz-Teilnahmen

### 7.2 Aufbewahrung

**Aufbewahrungsfrist:** 10 Jahre

**Zugriff:**
- HR: Alle Nachweise
- CISO: Alle Nachweise
- Manager: Nachweise ihres Teams
- Mitarbeiter: Eigene Nachweise

### 7.3 Audit-Nachweise

Für Audits werden folgende Nachweise bereitgestellt:
- Schulungsplan
- Teilnahmelisten
- Zertifikate
- Phishing-Simulationsergebnisse
- Awareness-Kampagnen-Dokumentation

## 8. Rollen und Verantwortlichkeiten

### 8.1 RACI-Matrix: Schulung und Awareness

| Aktivität | CISO | HR | Manager | Mitarbeiter | Externe Trainer |
|-----------|------|----|---------| ------------|-----------------|
| Schulungsplan erstellen | R/A | C | C | I | I |
| Schulungen durchführen | R | C | I | I | R |
| Teilnahme sicherstellen | A | C | R | R | I |
| Nachweise dokumentieren | A | R | C | I | I |
| Wirksamkeit prüfen | R/A | C | C | I | I |
| Awareness-Kampagnen | R/A | C | C | I | C |
| Phishing-Simulationen | R/A | I | I | I | C |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### 8.2 Security Champions

**Programm:**
- Freiwillige Mitarbeiter aus allen Abteilungen
- Multiplikatoren für Security Awareness
- Regelmäßige Treffen und Schulungen
- Anerkennung und Incentives

**Aufgaben:**
- Awareness in ihren Teams fördern
- Fragen zu Security beantworten
- Feedback an Security Team
- Teilnahme an Security-Projekten

## 9. Budget und Ressourcen

### 9.1 Budgetplanung

| Kategorie | Jährliches Budget | Bemerkungen |
|-----------|-------------------|-------------|
| LMS-Lizenz | [TODO] € | E-Learning-Plattform |
| Externe Schulungen | [TODO] € | Zertifizierungen, Konferenzen |
| Phishing-Simulation-Tool | [TODO] € | KnowBe4, Cofense, etc. |
| Awareness-Material | [TODO] € | Poster, Flyer, Giveaways |
| Externe Trainer | [TODO] € | Workshops, Spezialschulungen |
| **Gesamt** | **[TODO] €** | |

### 9.2 Zeitressourcen

**CISO/Security Team:**
- Schulungsplanung: 20 PT/Jahr
- Schulungsdurchführung: 40 PT/Jahr
- Awareness-Kampagnen: 30 PT/Jahr
- Phishing-Simulationen: 20 PT/Jahr

**Mitarbeiter:**
- Pflichtschulungen: 2 Stunden/Jahr
- Optionale Schulungen: Nach Bedarf

## 10. Referenzen

### 10.1 Interne Dokumente

- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md` - Governance
- `0110_ISMS_Sicherheitsziele_und_Metriken.md` - Security Objectives
- `0200_Policy_Akzeptable_Nutzung_IT.md` - Acceptable Use Policy
- `0520_Policy_HR_Security.md` - HR Security

### 10.2 Externe Standards

- **ISO/IEC 27001:2022** - Clause 7.2: Competence
- **ISO/IEC 27001:2022** - Clause 7.3: Awareness
- **ISO/IEC 27002:2022** - Control 6.3: Information security awareness, education and training

**Genehmigt durch:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }}

