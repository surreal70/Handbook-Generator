# Prüfungsteam und Ressourcen

**Dokument-ID:** idw-ps-951-0040  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument beschreibt die Zusammensetzung des Prüfungsteams, die erforderlichen Qualifikationen und die Ressourcenplanung für die IT-Prüfung nach IDW PS 951.

## 2. Prüfungsteam

### Teamstruktur

#### Prüfungsleitung
- **Name:** {{ source.audit_lead_name }}
- **Rolle:** Prüfungsleiter
- **Qualifikation:** {{ source.audit_lead_qualification }}
- **Erfahrung:** {{ source.audit_lead_experience }}
- **Kontakt:** {{ source.audit_lead_contact }}

#### IT-Prüfer

| Name | Rolle | Qualifikation | Spezialisierung | Verfügbarkeit |
|------|-------|---------------|-----------------|---------------|
| {{ source.auditor_1_name }} | Senior IT-Prüfer | {{ source.auditor_1_qual }} | {{ source.auditor_1_spec }} | {{ source.auditor_1_avail }} |
| {{ source.auditor_2_name }} | IT-Prüfer | {{ source.auditor_2_qual }} | {{ source.auditor_2_spec }} | {{ source.auditor_2_avail }} |
| {{ source.auditor_3_name }} | IT-Prüfer | {{ source.auditor_3_qual }} | {{ source.auditor_3_spec }} | {{ source.auditor_3_avail }} |

#### Fachexperten
- **Datenschutz:** {{ source.privacy_expert }}
- **IT-Sicherheit:** {{ source.security_expert }}
- **Anwendungssysteme:** {{ source.application_expert }}

## 3. Qualifikationsanforderungen

### Erforderliche Zertifizierungen
- CISA (Certified Information Systems Auditor)
- CISM (Certified Information Security Manager)
- CISSP (Certified Information Systems Security Professional)
- ISO 27001 Lead Auditor
- {{ source.additional_certifications }}

### Fachkenntnisse
- IT-Prüfung nach IDW PS 951
- IT-Governance und IT-Risikomanagement
- IT-Sicherheit und Datenschutz
- Anwendungssysteme und Datenbanken
- IT-Prozesse (ITIL, COBIT)

### Branchenkenntnisse
- {{ source.industry_knowledge }}

## 4. Ressourcenplanung

### Zeitbudget

| Prüfungsphase | Prüfungsleiter | Senior Prüfer | Prüfer | Experten | Gesamt |
|---------------|----------------|---------------|--------|----------|--------|
| Planung | {{ source.planning_lead_hours }} | {{ source.planning_senior_hours }} | {{ source.planning_auditor_hours }} | {{ source.planning_expert_hours }} | {{ source.planning_total_hours }} |
| Durchführung | {{ source.execution_lead_hours }} | {{ source.execution_senior_hours }} | {{ source.execution_auditor_hours }} | {{ source.execution_expert_hours }} | {{ source.execution_total_hours }} |
| Berichterstattung | {{ source.reporting_lead_hours }} | {{ source.reporting_senior_hours }} | {{ source.reporting_auditor_hours }} | {{ source.reporting_expert_hours }} | {{ source.reporting_total_hours }} |
| **Gesamt** | {{ source.total_lead_hours }} | {{ source.total_senior_hours }} | {{ source.total_auditor_hours }} | {{ source.total_expert_hours }} | {{ source.total_hours }} |

### Ressourcenallokation nach Prüfungsbereich

| Prüfungsbereich | Stunden | Prüfer | Priorität |
|-----------------|---------|--------|-----------|
| IT-Strategie und Organisation | {{ source.strategy_hours }} | {{ source.strategy_auditors }} | {{ source.strategy_priority }} |
| IT-Prozesse | {{ source.process_hours }} | {{ source.process_auditors }} | {{ source.process_priority }} |
| IT-Systeme | {{ source.systems_hours }} | {{ source.systems_auditors }} | {{ source.systems_priority }} |
| IT-Sicherheit | {{ source.security_hours }} | {{ source.security_auditors }} | {{ source.security_priority }} |
| Datenschutz | {{ source.privacy_hours }} | {{ source.privacy_auditors }} | {{ source.privacy_priority }} |

## 5. Rollen und Verantwortlichkeiten

### RACI-Matrix

| Aktivität | Prüfungsleiter | Senior Prüfer | Prüfer | Experten |
|-----------|----------------|---------------|--------|----------|
| Prüfungsplanung | A/R | C | I | C |
| Risikoanalyse | A | R | C | C |
| Kontrolltests | A | R | R | C |
| Dokumentenprüfung | A | R | R | I |
| Interviews | A | R | R | C |
| Berichtserstellung | A/R | C | C | I |
| Qualitätssicherung | A/R | C | I | I |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### Verantwortlichkeiten

#### Prüfungsleiter
- Gesamtverantwortung für die Prüfung
- Prüfungsplanung und -steuerung
- Kommunikation mit Management
- Berichtsgenehmigung

#### Senior IT-Prüfer
- Durchführung komplexer Prüfungshandlungen
- Supervision der Prüfer
- Qualitätssicherung
- Fachliche Beratung

#### IT-Prüfer
- Durchführung von Prüfungshandlungen
- Dokumentation der Prüfungsergebnisse
- Kontrolltests
- Datenanalyse

#### Fachexperten
- Spezialisierte Beratung
- Beurteilung komplexer Sachverhalte
- Unterstützung bei technischen Fragen

## 6. Unabhängigkeit und Objektivität

### Unabhängigkeitserklärungen
Alle Teammitglieder haben Unabhängigkeitserklärungen abgegeben:
- Keine finanziellen Interessen
- Keine persönlichen Beziehungen
- Keine Interessenkonflikte

### Rotation
- {{ source.rotation_policy }}

## 7. Schulung und Weiterbildung

### Erforderliche Schulungen
- IDW PS 951 Aktualisierungen
- Neue IT-Technologien
- Branchenspezifische Themen
- {{ source.required_training }}

### Weiterbildungsplan
| Teammitglied | Schulung | Termin | Status |
|--------------|----------|--------|--------|
| {{ source.training_1_member }} | {{ source.training_1_topic }} | {{ source.training_1_date }} | {{ source.training_1_status }} |

## 8. Externe Ressourcen

### Externe Experten
Bei Bedarf werden externe Experten hinzugezogen:
- {{ source.external_expert_1 }}
- {{ source.external_expert_2 }}

### Begründung
{{ source.external_expert_rationale }}

## 9. Kommunikation und Koordination

### Team-Meetings
- **Frequenz:** {{ source.meeting_frequency }}
- **Format:** {{ source.meeting_format }}
- **Teilnehmer:** Gesamtes Prüfungsteam

### Statusberichte
- **An:** Prüfungsleiter
- **Frequenz:** {{ source.status_report_frequency }}
- **Format:** {{ source.status_report_format }}

## 10. Referenzen

- IDW PS 951 - Qualifikationsanforderungen
- Prüfungsauftrag
- Ressourcenplan
- Unabhängigkeitserklärungen

---

**Genehmigt durch:**  
{{ meta.audit_lead }}, Prüfungsleiter  
Datum: {{ meta.approval_date }}

**Nächster Review:** {{ meta.next_review }}

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |
