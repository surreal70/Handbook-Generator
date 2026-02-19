# Schulung und Awareness – Programm

**Dokument-ID:** 0600
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
This template defines the security awareness and training program.
Reference: BSI Standard 200-1 (Awareness and Training), ORP.3
-->

## 1. Zweck und Zielsetzung

Das Schulungs- und Awareness-Programm von **{{ meta-organisation.name }}** stellt sicher, dass alle Mitarbeitenden über erforderliche Sicherheitskenntnisse verfügen.

**Verantwortlich:** {{ meta-organisation-roles.role_CISO }} (ISB)

## 2. Zielgruppen

| Zielgruppe | Anzahl | Spezifische Anforderungen |
|---|---|---|
| Alle Mitarbeitenden | [TODO] | Basis-Awareness |
| IT-Administratoren | [TODO] | Technische Sicherheit, Privileged Access |
| Entwickler | [TODO] | Secure Coding, SDLC |
| Führungskräfte | [TODO] | Sicherheitsstrategie, Risikomanagement |
| Externe Dienstleister | [TODO] | Relevante Sicherheitsanforderungen |

## 3. Schulungskatalog

| Training | Zielgruppe | Frequenz | Dauer | Inhalte | Nachweis | Owner |
|---|---|---|---|---|---|---|
| Grundlagentraining Informationssicherheit | Alle | Jährlich | 1h | Policies, Phishing, Passwörter, Incident-Meldung | LMS-Zertifikat | {{ meta-organisation-roles.role_CISO }} |
| Onboarding Security | Neue Mitarbeitende | Bei Eintritt | 30min | Grundlagen, Policies | Teilnahmeliste | HR |
| Phishing-Simulation | Alle | Quartalsweise | 10min | Phishing-Erkennung | Klickrate | {{ meta-organisation-roles.role_CISO }} |
| Admin-Schulung | IT-Admins | Jährlich | 4h | Privileged Access, Härtung, Logging | Teilnahmeliste | {{ meta-organisation-roles.role_CIO }} |
| Secure Coding | Entwickler | Jährlich | 8h | OWASP Top 10, SAST/DAST | Teilnahmeliste | {{ meta-organisation-roles.role_CIO }} |
| [TODO: Weitere Schulungen] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Wirksamkeitsmessung

### 4.1 Metriken (KPIs)

| KPI | Ziel | Messung | Frequenz |
|---|---|---|---|
| Schulungsquote | 100% | % Mitarbeitende mit aktuellem Training | Quartalsweise |
| Phishing-Test-Erfolgsrate | > 90% | % Mitarbeitende, die Phishing erkennen | Quartalsweise |
| Quiz-Erfolgsrate | > 80% | % bestandene Abschlusstests | Nach Schulung |

### 4.2 Feedback und Verbesserung

- **Feedback-Umfragen:** Nach jeder Schulung
- **Lessons Learned:** Aus Sicherheitsvorfällen
- **Kontinuierliche Verbesserung:** Jährliche Programm-Review

## 5. Schulungsmaterialien

**Verfügbare Materialien:**
- E-Learning-Module (LMS)
- Präsentationen
- Checklisten und Quick Reference Guides
- Poster und Infografiken
- Newsletter und Intranet-Artikel

**Ablageort:** [TODO: z.B. Intranet/Schulungsportal]

## 6. Kommunikation und Awareness-Kampagnen

**Regelmäßige Aktivitäten:**
- Monatlicher Security-Newsletter
- Quartalsweise Awareness-Kampagnen (Themen: Phishing, Passwörter, etc.)
- Security Champions Programm
- Jährlicher Security Awareness Month

## 7. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | {{ meta-organisation-roles.role_CISO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| HR | [TODO] | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**Referenzen:**
- BSI Standard 200-1: ISMS
- BSI IT-Grundschutz-Kompendium: ORP.3 Sensibilisierung und Schulung

<!-- End of template -->