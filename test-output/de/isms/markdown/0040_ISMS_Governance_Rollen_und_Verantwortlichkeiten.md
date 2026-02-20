# ISMS-Governance: Rollen und Verantwortlichkeiten

**Dokument-ID:** 0040
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



## 1. ISMS-Governance-Struktur

### 1.1 Governance-Übersicht

Die ISMS-Governance der **AdminSend GmbH** ist in die Gesamtorganisation integriert und stellt sicher, dass Informationssicherheit auf allen Ebenen verankert ist.

```
┌─────────────────────────────────────────────────────────┐
│              Geschäftsführung / Top Management          │
│                 ({{ meta-handbook.management_ceo }})              │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────┐
│  CIO             │    │  CISO            │
│  [TODO]  │    │  [TODO]  │
└─────────────────┘    └─────────────────┘
         │                       │
         │              ┌────────┴────────┐
         │              │                 │
         │     ┌────────▼────────┐ ┌─────▼──────┐
         │     │ ISMS Manager    │ │ Security   │
         │     │                 │ │ Team       │
         │     └─────────────────┘ └────────────┘
         │
┌────────▼────────────────────────────────────────────────┐
│        Informationssicherheitsgremium                    │
│        (Security Steering Committee)                     │
│  - CISO (Vorsitz)                                       │
│  - CIO                                                  │
│  - Vertreter Fachabteilungen                           │
│  - IT-Betrieb                                          │
│  - Datenschutzbeauftragter                             │
│  - Internal Audit (beratend)                           │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Schlüsselgremien

**Informationssicherheitsgremium (Security Steering Committee):**
- **Vorsitz:** [TODO] (CISO)
- **Mitglieder:** CIO, Vertreter Fachabteilungen, IT-Betrieb, Datenschutzbeauftragter
- **Frequenz:** Quartalsweise oder anlassbezogen
- **Aufgaben:**
  - Strategische Ausrichtung des ISMS
  - Genehmigung von Sicherheitsrichtlinien
  - Überwachung der ISMS-Performance
  - Entscheidung über Risikoakzeptanz
  - Budget-Freigabe für Sicherheitsmaßnahmen

### 1.3 Schnittstellen zu anderen Funktionen

**IT Service Management (ITSM):**
- Integration von Security in ITIL-Prozesse
- Incident Management, Change Management, Problem Management
- Kontakt: {{ meta-handbook.it_service_manager }}

**Datenschutz (DSMS):**
- Schnittstelle zu DSGVO-Compliance
- Gemeinsame Risikoanalyse und Datenschutz-Folgenabschätzung
- Kontakt: {{ meta-handbook.privacy_dpo }}

**Risk Management:**
- Integration in Enterprise Risk Management (ERM)
- Gemeinsames Risikoregister
- Kontakt: {{ meta-handbook.risk_manager }}

**Business Continuity Management (BCM):**
- Schnittstelle zu BCM-Handbuch
- Gemeinsame BIA und Notfallplanung
- Kontakt: {{ meta-handbook.bcm_manager }}

**Internal Audit:**
- Unabhängige Prüfung des ISMS
- Audit-Planung und -Durchführung
- Kontakt: {{ meta-handbook.audit_manager }}



## 2. Rollenbeschreibungen

### 2.1 Geschäftsführung / Top Management

**Rolle:** {{ meta-handbook.management_ceo }}

**Verantwortlichkeiten:**
- Gesamtverantwortung für Informationssicherheit
- Genehmigung der ISMS-Leitlinie
- Bereitstellung von Ressourcen für das ISMS
- Förderung der Sicherheitskultur
- Teilnahme am Management Review

**Befugnisse:**
- Genehmigung von Sicherheitsbudgets
- Entscheidung über strategische Sicherheitsinitiativen
- Genehmigung von Risikoakzeptanzen (bei hohen Risiken)

### 2.2 CISO (Chief Information Security Officer)

**Rolle:** [TODO] ({{ meta-organisation-roles.role_CISO_email }})

**Verantwortlichkeiten:**
- Entwicklung, Implementierung und Überwachung des ISMS
- Leitung des Informationssicherheitsgremiums
- Erstellung und Pflege von Sicherheitsrichtlinien
- Durchführung von Risikoanalysen
- Incident Response Koordination
- Reporting an Geschäftsführung
- Awareness und Schulung

**Befugnisse:**
- Genehmigung von Sicherheitsrichtlinien
- Anordnung von Sicherheitsmaßnahmen
- Eskalation bei kritischen Sicherheitsvorfällen
- Zugriff auf alle sicherheitsrelevanten Informationen

**Berichtslinie:** Berichtet an [TODO] (CIO) und Geschäftsführung

### 2.3 CIO (Chief Information Officer)

**Rolle:** [TODO] ({{ meta-organisation-roles.role_CIO_email }})

**Verantwortlichkeiten:**
- IT-Strategie und IT-Betrieb
- Unterstützung der ISMS-Umsetzung
- Bereitstellung von IT-Ressourcen für Sicherheitsmaßnahmen
- Integration von Security in IT-Prozesse

**Befugnisse:**
- Genehmigung von IT-Projekten mit Sicherheitsrelevanz
- Ressourcenzuteilung für IT-Sicherheit

### 2.4 ISMS Manager

**Rolle:** [TODO: Name und Kontakt]

**Verantwortlichkeiten:**
- Operative Umsetzung des ISMS
- Pflege der ISMS-Dokumentation
- Koordination von Audits und Reviews
- Tracking von Maßnahmen und Findings
- Unterstützung des CISO

**Befugnisse:**
- Koordination von ISMS-Aktivitäten
- Anforderung von Informationen für Audits

### 2.5 Asset Owner / Process Owner

**Rolle:** Fachabteilungsleiter, Prozessverantwortliche

**Verantwortlichkeiten:**
- Verantwortung für Informationswerte in ihrem Bereich
- Klassifizierung von Informationen
- Definition von Zugriffsrechten
- Umsetzung von Sicherheitsmaßnahmen in ihrem Bereich
- Meldung von Sicherheitsvorfällen

**Befugnisse:**
- Genehmigung von Zugriffsrechten für ihre Assets
- Entscheidung über Sicherheitsmaßnahmen in ihrem Bereich

### 2.6 Control Owner

**Rolle:** Verantwortliche für spezifische Sicherheitskontrollen

**Verantwortlichkeiten:**
- Implementierung und Betrieb von Sicherheitskontrollen
- Nachweis der Wirksamkeit (Evidence)
- Reporting über Control-Status
- Behebung von Control-Deficiencies

**Befugnisse:**
- Umsetzung von Sicherheitsmaßnahmen im Rahmen ihrer Kontrolle

**Beispiele:**
- Patch Management Control Owner: IT-Betrieb
- Access Control Owner: IAM-Team
- Backup Control Owner: Backup-Administrator

### 2.7 IT-Betrieb

**Rolle:** IT-Operations-Team

**Verantwortlichkeiten:**
- Umsetzung technischer Sicherheitsmaßnahmen
- Monitoring und Alerting
- Incident Response (technisch)
- Patch Management
- Backup und Recovery

**Befugnisse:**
- Durchführung von Sicherheitsmaßnahmen
- Notfall-Zugriffe bei Incidents

### 2.8 Mitarbeitende (alle)

**Rolle:** Alle Mitarbeiter, Auftragnehmer, Dritte

**Verantwortlichkeiten:**
- Einhaltung von Sicherheitsrichtlinien
- Meldung von Sicherheitsvorfällen
- Teilnahme an Security Awareness Training
- Schutz von Zugangsdaten und Informationen

**Befugnisse:**
- Zugriff auf Informationen nach Need-to-Know-Prinzip

### 2.9 Internal Audit / Compliance

**Rolle:** {{ meta-handbook.audit_manager }}

**Verantwortlichkeiten:**
- Unabhängige Prüfung des ISMS
- Audit-Planung und -Durchführung
- Reporting von Audit-Findings
- Überwachung der Maßnahmenumsetzung

**Befugnisse:**
- Zugriff auf alle ISMS-relevanten Informationen
- Anforderung von Nachweisen und Interviews

## 3. RACI-Matrix: ISMS-Prozesse

### 3.1 ISMS-Kernprozesse

| Aktivität | CISO | CIO | ISMS Manager | Asset Owner | IT-Betrieb | Internal Audit |
|-----------|------|-----|--------------|-------------|------------|----------------|
| **ISMS-Strategie entwickeln** | R/A | C | C | I | I | I |
| **Policies erstellen** | R/A | C | R | C | C | I |
| **Risikoanalyse durchführen** | A | C | R | C | C | I |
| **Risikobehandlung planen** | A | C | R | C | R | I |
| **SoA pflegen** | A | I | R | C | C | I |
| **Controls implementieren** | A | C | C | R | R | I |
| **Monitoring durchführen** | A | I | C | I | R | I |
| **Incidents managen** | A | C | C | I | R | I |
| **Audits durchführen** | C | C | C | C | C | R/A |
| **Management Review** | R | C | R | I | I | C |
| **Awareness Training** | A | C | R | I | I | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### 3.2 Annex A Controls (Beispiele)

| Control | Control Owner | Responsible | Accountable | Consulted | Informed |
|---------|---------------|-------------|-------------|-----------|----------|
| **A.5.1 Policies** | CISO | ISMS Manager | CISO | CIO, Fachabt. | Alle |
| **A.5.7 Threat Intelligence** | Security Team | Security Analyst | CISO | IT-Betrieb | ISMS Manager |
| **A.5.10 Acceptable Use** | CISO | HR | CISO | IT-Betrieb | Alle |
| **A.5.15 Access Control** | IAM Team | IAM Admin | CIO | CISO | IT-Betrieb |
| **A.5.23 Cloud Services** | Cloud Architect | Cloud Admin | CIO | CISO | IT-Betrieb |
| **A.8.8 Backup** | IT-Betrieb | Backup Admin | CIO | CISO | ISMS Manager |
| **A.8.16 Monitoring** | Security Team | SOC Analyst | CISO | IT-Betrieb | ISMS Manager |



## 4. Eskalationspfade

### 4.1 Sicherheitsvorfälle

```
Incident Detection
       │
       ▼
IT-Betrieb / SOC
       │
       ▼
CISO (bei kritischen Incidents)
       │
       ▼
CIO / Geschäftsführung (bei Major Incidents)
       │
       ▼
Externe Meldung (Behörden, Kunden)
```

Siehe `0400_Policy_Incident_Management.md` für Details.

### 4.2 Risikoakzeptanz

```
Risikoidentifikation
       │
       ▼
CISO (Risikobewertung)
       │
       ▼
CISO (Risikoakzeptanz bei niedrigen/mittleren Risiken)
       │
       ▼
Geschäftsführung (Risikoakzeptanz bei hohen Risiken)
```

Siehe `0070_ISMS_Risikoakzeptanzkriterien.md` für Details.

## 5. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0030_ISMS_Kontext_und_Interessierte_Parteien.md` - Context
- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management
- `0130_ISMS_Internes_Auditprogramm.md` - Internal Audit Program

### Externe Standards
- **ISO/IEC 27001:2022** - Clause 5.3: Organizational roles, responsibilities and authorities
- **ISO/IEC 27002:2022** - Control 5.2: Information security roles and responsibilities

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO]

