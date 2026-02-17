# Risikomanagement – Methodik

**Dokument-ID:** 0060
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

<!-- 
TEMPLATE AUTHOR NOTE:
This document defines the risk management methodology for the ISMS. It establishes
how information security risks are identified, assessed, treated, and monitored.
This is a critical foundation document that drives the entire risk-based approach
of ISO 27001:2022.

ISO 27001:2022 Reference: Clause 6.1.2 - Information security risk assessment
-->

## 1. Ziel und Geltungsbereich

### 1.1 Ziel

Diese Methodik definiert, wie die **{{ meta-organisation.name }}** Informationssicherheitsrisiken systematisch identifiziert, bewertet, behandelt und überwacht. Sie stellt sicher, dass:
- Risiken konsistent und nachvollziehbar bewertet werden
- Risikobehandlungsmaßnahmen priorisiert werden
- Risiken auf ein akzeptables Niveau reduziert werden
- Die Geschäftsführung informierte Entscheidungen treffen kann

### 1.2 Geltungsbereich

Diese Methodik gilt für alle Informationssicherheitsrisiken im ISMS-Scope (siehe `0020_ISMS_Geltungsbereich_Scope.md`):
- IT-Systeme und Infrastruktur
- Geschäftsprozesse
- Informationswerte und Daten
- Lieferanten und Drittparteien
- Physische Sicherheit

## 2. Risikoobjekte

### 2.1 Assets (Informationswerte)

**Kategorien:**
- **Informationen und Daten:** Kundendaten, Geschäftsdaten, technische Daten, Mitarbeiterdaten
- **IT-Systeme:** Server, Netzwerkkomponenten, Endgeräte, Cloud-Infrastruktur
- **Anwendungen:** Geschäftsanwendungen, Entwicklungstools, Kommunikationsplattformen
- **Services:** IT-Services, Geschäftsservices
- **Personen:** Mitarbeiter mit kritischem Wissen
- **Physische Assets:** Rechenzentren, Büros, Hardware

**Asset-Inventar:**
- Siehe `0720_Anhang_Asset_und_Systeminventar_Template.md`
- Asset-Eigentümer (Asset Owner) sind verantwortlich für ihre Assets

### 2.2 Geschäftsprozesse

**Kritische Geschäftsprozesse:**
- [TODO: Liste der kritischen Geschäftsprozesse]
- Siehe Business Impact Analysis (BIA) im BCM-Handbuch

**Prozess-Eigentümer:**
- Verantwortlich für Risiken in ihrem Prozess
- Siehe `0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md`

### 2.3 Lieferanten und Outsourcing

**Kritische Lieferanten:**
- Cloud-Provider (AWS, Azure, GCP)
- Managed Service Provider
- Software-Lieferanten
- Siehe `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md`

**Third-Party Risk Assessment:**
- Separate Risikobewertung für kritische Lieferanten
- Siehe `0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md`

## 3. Risikomanagement-Methodik

### 3.1 Risikomanagement-Prozess

```
┌─────────────────────────────────────────────────────────┐
│              Risikomanagement-Zyklus                     │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────┐
        │  1. Risikoidentifikation        │
        │  (Bedrohungen + Schwachstellen) │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │  2. Risikobewertung             │
        │  (Wahrscheinlichkeit × Impact)  │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │  3. Risikobehandlung            │
        │  (Vermeiden, Reduzieren,        │
        │   Übertragen, Akzeptieren)      │
        └────────────┬────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────┐
        │  4. Risikoüberwachung           │
        │  (Monitoring, Review)           │
        └────────────┬────────────────────┘
                     │
                     └──────────┐
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Kontinuierliche      │
                    │  Verbesserung         │
                    └───────────────────────┘
```

### 3.2 Risikoidentifikation

**Methoden:**
1. **Asset-basiert:** Identifikation von Bedrohungen und Schwachstellen für jedes Asset
2. **Szenario-basiert:** Analyse von Bedrohungsszenarien (z.B. Ransomware, DDoS, Insider-Bedrohung)
3. **Compliance-basiert:** Identifikation von Compliance-Risiken (DSGVO, NIS2, etc.)

**Risikoformel:**
```
Risiko = Bedrohung × Schwachstelle × Asset-Wert
```

**Bedrohungen (Threats):**
- **Cyber-Bedrohungen:** Ransomware, Phishing, DDoS, APT, Malware
- **Menschliche Bedrohungen:** Insider-Bedrohung, Social Engineering, Fehler
- **Umweltbedrohungen:** Feuer, Wasser, Stromausfall, Naturkatastrophen
- **Technische Bedrohungen:** Hardware-Ausfall, Software-Bugs, Konfigurationsfehler

**Schwachstellen (Vulnerabilities):**
- **Technische Schwachstellen:** Ungepatchte Systeme, Fehlkonfigurationen, schwache Verschlüsselung
- **Organisatorische Schwachstellen:** Fehlende Policies, unzureichende Schulung, schwache Prozesse
- **Physische Schwachstellen:** Unzureichender Zutrittsschutz, fehlende Redundanz

**Quellen für Risikoidentifikation:**
- Threat Intelligence (CERT, MITRE ATT&CK, Vendor Advisories)
- Vulnerability Scans (CVE, CVSS)
- Penetration Tests
- Security Incidents und Lessons Learned
- Audit-Findings
- Compliance-Anforderungen

### 3.3 Risikobewertung

**Bewertungsskalen:**

**Wahrscheinlichkeit (Likelihood):**

| Stufe | Beschreibung | Häufigkeit |
|-------|--------------|------------|
| 1 - Sehr unwahrscheinlich | Ereignis ist theoretisch möglich, aber sehr unwahrscheinlich | < 1 in 10 Jahren |
| 2 - Unwahrscheinlich | Ereignis könnte auftreten, ist aber unwahrscheinlich | 1 in 5-10 Jahren |
| 3 - Möglich | Ereignis könnte auftreten | 1 in 1-5 Jahren |
| 4 - Wahrscheinlich | Ereignis wird wahrscheinlich auftreten | 1-5 mal pro Jahr |
| 5 - Sehr wahrscheinlich | Ereignis wird mit hoher Sicherheit auftreten | > 5 mal pro Jahr |

**Auswirkung (Impact):**

| Stufe | Beschreibung | Finanzieller Schaden | Reputationsschaden | Compliance |
|-------|--------------|----------------------|-------------------|------------|
| 1 - Vernachlässigbar | Minimale Auswirkung | < 10.000 € | Keine | Keine |
| 2 - Gering | Geringe Auswirkung | 10.000 - 50.000 € | Lokal | Kleinere Verstöße |
| 3 - Mittel | Moderate Auswirkung | 50.000 - 250.000 € | Regional | Meldepflichtige Vorfälle |
| 4 - Hoch | Erhebliche Auswirkung | 250.000 - 1 Mio. € | National | Bußgelder |
| 5 - Sehr hoch | Katastrophale Auswirkung | > 1 Mio. € | International | Geschäftsverbot |

<!-- 
Customize the impact scales based on your organization's specific risk appetite
and business context. Consider financial, reputational, operational, and 
compliance impacts.
-->

**Risikomatrix:**

```
Impact ↑
  5 │  M   H   H   VH  VH
  4 │  M   M   H   H   VH
  3 │  L   M   M   H   H
  2 │  L   L   M   M   H
  1 │  VL  L   L   M   M
    └─────────────────────→ Likelihood
      1   2   3   4   5

Legende:
VL = Very Low (Sehr niedrig)
L  = Low (Niedrig)
M  = Medium (Mittel)
H  = High (Hoch)
VH = Very High (Sehr hoch)
```

**Risikoscore-Berechnung:**
```
Risikoscore = Wahrscheinlichkeit × Auswirkung

Beispiel:
Wahrscheinlichkeit = 4 (Wahrscheinlich)
Auswirkung = 3 (Mittel)
Risikoscore = 4 × 3 = 12 (Hoch)
```

### 3.4 Risiko-Eigentümer (Risk Owner)

**Verantwortlichkeiten:**
- Jedes identifizierte Risiko hat einen Risiko-Eigentümer
- Risiko-Eigentümer ist verantwortlich für Risikobehandlung
- Typischerweise: Asset Owner, Process Owner, oder CISO

**Eskalation:**
- Hohe und sehr hohe Risiken werden an Geschäftsführung eskaliert
- Siehe `0070_ISMS_Risikoakzeptanzkriterien.md`

## 4. Quellen für Risikoinformationen

### 4.1 Threat Intelligence

**Externe Quellen:**
- **CERT-Bund:** https://www.cert-bund.de/
- **MITRE ATT&CK:** https://attack.mitre.org/
- **NIST NVD:** https://nvd.nist.gov/
- **Vendor Security Advisories:** Microsoft, Cisco, etc.
- **Threat Intelligence Feeds:** [TODO: Kommerzielle Feeds]

**Interne Quellen:**
- Security Incidents und Lessons Learned
- Penetration Test Reports
- Red Team Exercises

### 4.2 Schwachstellen (Vulnerabilities)

**Vulnerability Scanning:**
- **Tools:** [TODO: Nessus, Qualys, OpenVAS]
- **Frequenz:** Wöchentlich (automatisiert)
- **Scope:** Alle Systeme im ISMS-Scope

**CVE und CVSS:**
- Common Vulnerabilities and Exposures (CVE)
- Common Vulnerability Scoring System (CVSS)
- Priorisierung nach CVSS-Score

**Patch Management:**
- Siehe `0340_Policy_Vulnerability_und_Patch_Management.md`

### 4.3 Incidents und Findings

**Security Incidents:**
- Jeder Incident wird auf Risikorelevanz geprüft
- Lessons Learned fließen in Risikoanalyse ein
- Siehe `0400_Policy_Incident_Management.md`

**Audit-Findings:**
- Interne und externe Audit-Findings
- Findings werden als Risiken bewertet
- Siehe `0130_ISMS_Internes_Auditprogramm.md`

## 5. Outputs des Risikomanagements

### 5.1 Risikoregister

**Inhalt:**
- Alle identifizierten Risiken
- Risikobewertung (Wahrscheinlichkeit, Auswirkung, Score)
- Risiko-Eigentümer
- Risikobehandlungsstrategie
- Status und Maßnahmen

**Dokument:** `0080_ISMS_Risikoregister_Template.md`

**Pflege:**
- Quartalsweise Review
- Anlassbezogene Updates (neue Bedrohungen, Incidents)

### 5.2 Risikobehandlungsplan (Risk Treatment Plan)

**Inhalt:**
- Geplante Maßnahmen zur Risikobehandlung
- Verantwortliche und Termine
- Budget und Ressourcen
- Priorisierung

**Dokument:** `0090_ISMS_Risikobehandlungsplan_RTP_Template.md`

**Tracking:**
- Maßnahmen werden im RTP getrackt
- Regelmäßiges Reporting an CISO und Geschäftsführung

### 5.3 Statement of Applicability (SoA)

**Inhalt:**
- Auswahl und Begründung von Annex A Controls
- Basierend auf Risikoanalyse und Compliance-Anforderungen
- Dokumentation von Ausschlüssen

**Dokument:** `0100_ISMS_Statement_of_Applicability_SoA_Template.md`

**Zusammenhang:**
- Risikoanalyse → Identifikation benötigter Controls
- SoA → Dokumentation der Control-Auswahl
- RTP → Implementierung der Controls

## 6. Risikomanagement-Zyklus

### 6.1 Regelmäßiger Review

**Frequenz:**
- **Quartalsweise:** Review des Risikoregisters
- **Jährlich:** Vollständige Risikoanalyse
- **Anlassbezogen:** Bei wesentlichen Änderungen

**Trigger für anlassbezogenen Review:**
- Neue Bedrohungen (z.B. Zero-Day-Exploits)
- Wesentliche organisatorische Änderungen
- Neue Compliance-Anforderungen
- Major Security Incidents
- Audit-Findings

### 6.2 Risikoüberwachung (Risk Monitoring)

**Kontinuierliches Monitoring:**
- Security Monitoring (SIEM, IDS/IPS)
- Vulnerability Scanning
- Threat Intelligence Feeds
- Incident Tracking

**KPIs:**
- Anzahl offener Risiken (nach Risikostufe)
- Durchschnittliche Zeit zur Risikobehebung
- Anzahl akzeptierter Risiken
- Trend der Risikoscores

**Reporting:**
- Quartalsweise an Informationssicherheitsgremium
- Jährlich im Management Review

### 6.3 Kontinuierliche Verbesserung

**Lessons Learned:**
- Aus Security Incidents
- Aus Audit-Findings
- Aus Penetration Tests

**Verbesserungsmaßnahmen:**
- Anpassung der Risikobewertungsskalen
- Verbesserung der Risikoidentifikationsmethoden
- Optimierung des Risikomanagement-Prozesses

## 7. Rollen und Verantwortlichkeiten

### 7.1 RACI-Matrix: Risikomanagement

| Aktivität | CISO | ISMS Manager | Risk Owner | IT-Betrieb | Geschäftsführung |
|-----------|------|--------------|------------|------------|------------------|
| Risikomanagement-Methodik definieren | R/A | C | C | C | I |
| Risikoidentifikation | A | R | C | C | I |
| Risikobewertung | A | R | C | C | I |
| Risikobehandlung planen | A | C | R | C | I |
| Maßnahmen umsetzen | A | C | R | R | I |
| Risikoakzeptanz (niedrig/mittel) | A | I | C | I | I |
| Risikoakzeptanz (hoch/sehr hoch) | C | I | C | I | A |
| Risikoüberwachung | A | R | C | C | I |
| Risiko-Reporting | R | R | C | I | I |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 8. Referenzen

### Interne Dokumente
- `0020_ISMS_Geltungsbereich_Scope.md` - ISMS Scope
- `0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md` - Governance
- `0070_ISMS_Risikoakzeptanzkriterien.md` - Risk Acceptance Criteria
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0090_ISMS_Risikobehandlungsplan_RTP_Template.md` - Risk Treatment Plan
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Vulnerability Management
- `0400_Policy_Incident_Management.md` - Incident Management

### Externe Standards
- **ISO/IEC 27001:2022** - Clause 6.1.2: Information security risk assessment
- **ISO/IEC 27001:2022** - Clause 6.1.3: Information security risk treatment
- **ISO/IEC 27005:2022** - Information security risk management
- **NIST SP 800-30** - Guide for Conducting Risk Assessments

**Genehmigt durch:**  
{{ meta.ciso.name }}, CISO  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }}

