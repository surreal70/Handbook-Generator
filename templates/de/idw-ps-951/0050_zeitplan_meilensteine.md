# Zeitplan und Meilensteine

**Dokument-ID:** idw-ps-951-0050  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument definiert den Zeitplan, die Meilensteine und die kritischen Termine für die IT-Prüfung nach IDW PS 951.

## 2. Gesamtzeitplan

### Prüfungszeitraum
- **Prüfungsbeginn:** {{ source.audit_start_date }}
- **Prüfungsende:** {{ source.audit_end_date }}
- **Gesamtdauer:** {{ source.audit_duration }}

### Phasenübersicht

| Phase | Start | Ende | Dauer | Status |
|-------|-------|------|-------|--------|
| Vorbereitung | {{ source.prep_start }} | {{ source.prep_end }} | {{ source.prep_duration }} | {{ source.prep_status }} |
| Planung | {{ source.planning_start }} | {{ source.planning_end }} | {{ source.planning_duration }} | {{ source.planning_status }} |
| Durchführung | {{ source.execution_start }} | {{ source.execution_end }} | {{ source.execution_duration }} | {{ source.execution_status }} |
| Berichterstattung | {{ source.reporting_start }} | {{ source.reporting_end }} | {{ source.reporting_duration }} | {{ source.reporting_status }} |
| Follow-up | {{ source.followup_start }} | {{ source.followup_end }} | {{ source.followup_duration }} | {{ source.followup_status }} |

## 3. Detaillierter Zeitplan

### Phase 1: Vorbereitung

| Aktivität | Verantwortlich | Start | Ende | Dauer |
|-----------|----------------|-------|------|-------|
| Prüfungsauftrag klären | {{ source.prep_1_owner }} | {{ source.prep_1_start }} | {{ source.prep_1_end }} | {{ source.prep_1_duration }} |
| Dokumentenanforderung | {{ source.prep_2_owner }} | {{ source.prep_2_start }} | {{ source.prep_2_end }} | {{ source.prep_2_duration }} |
| Vorjahresberichte prüfen | {{ source.prep_3_owner }} | {{ source.prep_3_start }} | {{ source.prep_3_end }} | {{ source.prep_3_duration }} |
| Team zusammenstellen | {{ source.prep_4_owner }} | {{ source.prep_4_start }} | {{ source.prep_4_end }} | {{ source.prep_4_duration }} |

### Phase 2: Planung

| Aktivität | Verantwortlich | Start | Ende | Dauer |
|-----------|----------------|-------|------|-------|
| Risikoanalyse | {{ source.plan_1_owner }} | {{ source.plan_1_start }} | {{ source.plan_1_end }} | {{ source.plan_1_duration }} |
| Scope-Definition | {{ source.plan_2_owner }} | {{ source.plan_2_start }} | {{ source.plan_2_end }} | {{ source.plan_2_duration }} |
| Prüfungsprogramm erstellen | {{ source.plan_3_owner }} | {{ source.plan_3_start }} | {{ source.plan_3_end }} | {{ source.plan_3_duration }} |
| Auftaktgespräch | {{ source.plan_4_owner }} | {{ source.plan_4_start }} | {{ source.plan_4_end }} | {{ source.plan_4_duration }} |

### Phase 3: Durchführung

| Aktivität | Verantwortlich | Start | Ende | Dauer |
|-----------|----------------|-------|------|-------|
| IT-Strategie prüfen | {{ source.exec_1_owner }} | {{ source.exec_1_start }} | {{ source.exec_1_end }} | {{ source.exec_1_duration }} |
| IT-Prozesse prüfen | {{ source.exec_2_owner }} | {{ source.exec_2_start }} | {{ source.exec_2_end }} | {{ source.exec_2_duration }} |
| IT-Systeme prüfen | {{ source.exec_3_owner }} | {{ source.exec_3_start }} | {{ source.exec_3_end }} | {{ source.exec_3_duration }} |
| IT-Sicherheit prüfen | {{ source.exec_4_owner }} | {{ source.exec_4_start }} | {{ source.exec_4_end }} | {{ source.exec_4_duration }} |
| Kontrolltests durchführen | {{ source.exec_5_owner }} | {{ source.exec_5_start }} | {{ source.exec_5_end }} | {{ source.exec_5_duration }} |
| Interviews führen | {{ source.exec_6_owner }} | {{ source.exec_6_start }} | {{ source.exec_6_end }} | {{ source.exec_6_duration }} |

### Phase 4: Berichterstattung

| Aktivität | Verantwortlich | Start | Ende | Dauer |
|-----------|----------------|-------|------|-------|
| Prüfungsergebnisse konsolidieren | {{ source.report_1_owner }} | {{ source.report_1_start }} | {{ source.report_1_end }} | {{ source.report_1_duration }} |
| Berichtsentwurf erstellen | {{ source.report_2_owner }} | {{ source.report_2_start }} | {{ source.report_2_end }} | {{ source.report_2_duration }} |
| Qualitätssicherung | {{ source.report_3_owner }} | {{ source.report_3_start }} | {{ source.report_3_end }} | {{ source.report_3_duration }} |
| Abschlussgespräch | {{ source.report_4_owner }} | {{ source.report_4_start }} | {{ source.report_4_end }} | {{ source.report_4_duration }} |
| Finaler Bericht | {{ source.report_5_owner }} | {{ source.report_5_start }} | {{ source.report_5_end }} | {{ source.report_5_duration }} |

## 4. Meilensteine

### Kritische Meilensteine

| Meilenstein | Datum | Verantwortlich | Status | Abhängigkeiten |
|-------------|-------|----------------|--------|----------------|
| M1: Prüfungsauftrag erteilt | {{ source.milestone_1_date }} | {{ source.milestone_1_owner }} | {{ source.milestone_1_status }} | - |
| M2: Prüfungsplanung abgeschlossen | {{ source.milestone_2_date }} | {{ source.milestone_2_owner }} | {{ source.milestone_2_status }} | M1 |
| M3: Auftaktgespräch durchgeführt | {{ source.milestone_3_date }} | {{ source.milestone_3_owner }} | {{ source.milestone_3_status }} | M2 |
| M4: Prüfungshandlungen abgeschlossen | {{ source.milestone_4_date }} | {{ source.milestone_4_owner }} | {{ source.milestone_4_status }} | M3 |
| M5: Berichtsentwurf erstellt | {{ source.milestone_5_date }} | {{ source.milestone_5_owner }} | {{ source.milestone_5_status }} | M4 |
| M6: Abschlussgespräch durchgeführt | {{ source.milestone_6_date }} | {{ source.milestone_6_owner }} | {{ source.milestone_6_status }} | M5 |
| M7: Finaler Bericht übergeben | {{ source.milestone_7_date }} | {{ source.milestone_7_owner }} | {{ source.milestone_7_status }} | M6 |

## 5. Kritischer Pfad

### Kritische Aktivitäten
Die folgenden Aktivitäten liegen auf dem kritischen Pfad und dürfen nicht verzögert werden:
1. {{ source.critical_activity_1 }}
2. {{ source.critical_activity_2 }}
3. {{ source.critical_activity_3 }}

### Pufferzeiten
- Planungspuffer: {{ source.planning_buffer }}
- Durchführungspuffer: {{ source.execution_buffer }}
- Berichtspuffer: {{ source.reporting_buffer }}

## 6. Ressourcenauslastung

### Auslastungsplan

| Kalenderwoche | Prüfungsleiter | Senior Prüfer | Prüfer | Experten |
|---------------|----------------|---------------|--------|----------|
| KW {{ source.week_1 }} | {{ source.week_1_lead }} | {{ source.week_1_senior }} | {{ source.week_1_auditor }} | {{ source.week_1_expert }} |
| KW {{ source.week_2 }} | {{ source.week_2_lead }} | {{ source.week_2_senior }} | {{ source.week_2_auditor }} | {{ source.week_2_expert }} |
| KW {{ source.week_3 }} | {{ source.week_3_lead }} | {{ source.week_3_senior }} | {{ source.week_3_auditor }} | {{ source.week_3_expert }} |

## 7. Meetings und Termine

### Regelmäßige Meetings

| Meeting | Frequenz | Teilnehmer | Dauer |
|---------|----------|------------|-------|
| Team-Meeting | {{ source.team_meeting_freq }} | Prüfungsteam | {{ source.team_meeting_duration }} |
| Status-Update | {{ source.status_meeting_freq }} | Prüfungsleiter, Management | {{ source.status_meeting_duration }} |
| Koordination | {{ source.coord_meeting_freq }} | Prüfungsleiter, IT-Leitung | {{ source.coord_meeting_duration }} |

### Wichtige Termine

| Termin | Datum | Teilnehmer | Zweck |
|--------|-------|------------|-------|
| Auftaktgespräch | {{ source.kickoff_date }} | {{ source.kickoff_participants }} | Prüfungsstart |
| Zwischenbesprechung | {{ source.interim_date }} | {{ source.interim_participants }} | Statusupdate |
| Abschlussgespräch | {{ source.closing_date }} | {{ source.closing_participants }} | Ergebnispräsentation |

## 8. Risiken und Verzögerungen

### Zeitplanrisiken
| Risiko | Wahrscheinlichkeit | Auswirkung | Maßnahme |
|--------|-------------------|------------|----------|
| {{ source.schedule_risk_1 }} | {{ source.risk_1_likelihood }} | {{ source.risk_1_impact }} | {{ source.risk_1_mitigation }} |
| {{ source.schedule_risk_2 }} | {{ source.risk_2_likelihood }} | {{ source.risk_2_impact }} | {{ source.risk_2_mitigation }} |

### Eskalationsprozess
Bei Verzögerungen:
1. Meldung an Prüfungsleiter
2. Bewertung der Auswirkungen
3. Anpassung des Zeitplans
4. Information der Stakeholder

## 9. Änderungsmanagement

### Zeitplanänderungen
Änderungen am Zeitplan müssen dokumentiert werden:
- **Änderungsantrag:** {{ source.change_request_process }}
- **Genehmigung:** {{ source.change_approval_authority }}
- **Kommunikation:** {{ source.change_communication }}

### Änderungshistorie
| Datum | Änderung | Begründung | Genehmigt durch |
|-------|----------|------------|-----------------|
| {{ source.change_1_date }} | {{ source.change_1_desc }} | {{ source.change_1_reason }} | {{ source.change_1_approver }} |

## 10. Referenzen

- Prüfungsauftrag
- Ressourcenplan
- Risikoanalyse
- Projektmanagement-Richtlinien

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
