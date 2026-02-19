# Policy: Incident Management

**Dokument-ID:** 0400
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
This policy establishes the principles for security incident management and response.
It ensures that security incidents are detected, reported, assessed, and responded to
in a timely and effective manner. Customize based on your organization's incident
response capabilities and SOC maturity.

ISO 27001:2022 Annex A Reference: A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
-->

## 1. Zweck

Diese Policy definiert die Grundsätze für Incident Management und Security Incident Response der **{{ meta-organisation.name }}**. Sie stellt sicher, dass Sicherheitsvorfälle zeitnah erkannt, bewertet, behandelt und dokumentiert werden, um Schäden zu minimieren und aus Vorfällen zu lernen.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Incident-Typen:** Security Incidents, Data Breaches, Malware, Phishing, DDoS, Insider Threats
- **Systeme:** Alle IT-Systeme, Anwendungen, Netzwerke, Cloud-Services
- **Personen:** Alle Mitarbeiter, Auftragnehmer, Lieferanten
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Incident Response Capability
Die Organisation unterhält eine Incident Response Capability mit definierten Prozessen, Rollen und Tools zur Behandlung von Sicherheitsvorfällen.

### 3.2 Meldepflicht
Alle Mitarbeiter sind verpflichtet, vermutete oder bestätigte Sicherheitsvorfälle unverzüglich zu melden. Es gibt keine negativen Konsequenzen für gutgläubige Meldungen.

### 3.3 Incident-Kategorisierung und Priorisierung
Incidents werden nach Schweregrad und Auswirkung kategorisiert:
- **Critical:** Schwerwiegende Auswirkungen auf Geschäftsbetrieb oder Datenschutz
- **High:** Erhebliche Auswirkungen, aber Geschäftsbetrieb nicht kritisch gefährdet
- **Medium:** Moderate Auswirkungen, begrenzte Beeinträchtigung
- **Low:** Geringe Auswirkungen, keine unmittelbare Gefahr

### 3.4 Incident Response Lifecycle
Incidents werden nach einem strukturierten Prozess behandelt:
- **Detection & Reporting:** Erkennung und Meldung
- **Triage & Assessment:** Bewertung und Priorisierung
- **Containment:** Eindämmung zur Schadensbegrenzung
- **Eradication:** Beseitigung der Ursache
- **Recovery:** Wiederherstellung des Normalbetriebs
- **Post-Incident Review:** Nachbereitung und Lessons Learned

### 3.5 Eskalation und Kommunikation
Kritische Incidents werden nach definierten Eskalationspfaden an Management, Legal, PR und ggf. Behörden eskaliert. Kommunikation erfolgt nach festgelegten Kommunikationsplänen.

### 3.6 Forensik und Evidence Preservation
Bei schwerwiegenden Incidents wird forensische Analyse durchgeführt. Beweismittel werden sicher gesichert und dokumentiert für mögliche rechtliche Schritte.

### 3.7 Data Breach Notification
Data Breaches werden gemäß DSGVO und anderen regulatorischen Anforderungen innerhalb von 72 Stunden an Aufsichtsbehörden und betroffene Personen gemeldet.

### 3.8 Continuous Improvement
Aus jedem Incident werden Lessons Learned abgeleitet. Erkenntnisse fließen in die Verbesserung von Prozessen, Kontrollen und Awareness ein.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Incident Management

| Aktivität | CISO | Incident Manager | SOC | IT-Betrieb | Legal/DPO | Management |
|-----------|------|------------------|-----|------------|-----------|------------|
| Policy-Erstellung | R/A | C | C | C | C | I |
| Incident Detection | A | C | R | C | I | I |
| Incident Triage | A | R | R | C | I | I |
| Incident Response | A | R | R | R | C | I |
| Eskalation | A | R | C | I | C | I |
| Data Breach Notification | A | C | I | I | R | C |
| Forensik | A | C | R | C | C | I |
| Post-Incident Review | R/A | R | C | C | C | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO)
- **Incident Manager:** {{ meta-handbook.security_incident_manager }}
- **SOC Manager:** {{ meta-handbook.security_soc_manager }}
- **Data Protection Officer:** {{ meta-handbook.dpo_name }}
- **Umsetzungsverantwortliche:** SOC, IT-Betrieb, Incident Response Team
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md** - Detaillierte Implementierungsrichtlinie
- `0320_Policy_Logging_und_Monitoring.md` - Logging and Monitoring Policy
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Data Protection Policy

### Zugehörige Standards/Baselines
- Incident Response Playbooks
- Incident Severity Matrix
- Eskalationspfade
- Data Breach Notification Prozess

### Zugehörige Prozesse
- Incident Response Prozess
- Major Incident Prozess
- Data Breach Notification Prozess
- Post-Incident Review Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl Incidents pro Kategorie und Schweregrad
- MTTD (Mean Time To Detect) - Durchschnittliche Erkennungszeit
- MTTR (Mean Time To Respond) - Durchschnittliche Reaktionszeit
- MTTR (Mean Time To Resolve) - Durchschnittliche Lösungszeit
- Anzahl Data Breaches und Meldungen
- Post-Incident Review Completion Rate (Ziel: 100%)

### Nachweise und Evidence
- Incident-Tickets und Dokumentation
- Incident Response Logs
- Forensik-Reports
- Data Breach Notifications
- Post-Incident Review Reports
- Lessons Learned Dokumentation

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nicht gemeldeter Incident:** Nachschulung, Verwarnung
- **Verzögerte Data Breach Notification:** Compliance-Untersuchung, ggf. Bußgelder
- **Beweismittel-Manipulation:** Schwerwiegende Disziplinarmaßnahmen
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md` - Detailed Guideline
- `0320_Policy_Logging_und_Monitoring.md` - Logging and Monitoring Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.24** - Information security incident management planning and preparation
- **ISO/IEC 27001:2022 Annex A.5.25** - Assessment and decision on information security events
- **ISO/IEC 27001:2022 Annex A.5.26** - Response to information security incidents
- **ISO/IEC 27001:2022 Annex A.5.27** - Learning from information security incidents
- **ISO/IEC 27001:2022 Annex A.5.28** - Collection of evidence
- **NIST SP 800-61** - Computer Security Incident Handling Guide
- **DSGVO (EU 2016/679)** - Art. 33, 34 - Data Breach Notification
- **NIS2-Richtlinie** - Network and Information Security Directive

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

