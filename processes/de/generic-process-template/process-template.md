<!--
=============================================================================
PROZESS-DOKUMENTATIONS-TEMPLATE
=============================================================================

Dieses Template dient zur strukturierten Dokumentation von Geschäftsprozessen
nach BPMN-Standards mit RACI-Matrix und Compliance-Anforderungen.

KONFIGURATIONSDATEIEN:
- meta-process.yaml: Prozess-spezifische Metadaten (in diesem Verzeichnis)
- meta-global-process.yaml: Globale Prozess-Konfiguration (im processes/de/ Verzeichnis)
- meta-organisation.yaml: Organisations-Daten (im Hauptverzeichnis)
- meta-organisation-roles.yaml: Rollen und Kontakte (im Hauptverzeichnis)
- meta-global.yaml: Generator-Informationen (im Hauptverzeichnis)

PLACEHOLDER-SYNTAX:
- {{ meta-process.* }} - Werte aus meta-process.yaml
- {{ meta-global-process.* }} - Werte aus meta-global-process.yaml
- {{ meta-organisation.* }} - Werte aus meta-organisation.yaml
- {{ role_* }} - Rollen aus meta-organisation-roles.yaml
- {{ escalation.* }} - Eskalationswege aus meta-global-process.yaml

VERWENDUNG:
1. Kopieren Sie dieses Template-Verzeichnis
2. Benennen Sie es nach Ihrem Prozess (z.B. "change-management")
3. Passen Sie meta-process.yaml an Ihre Anforderungen an
4. Füllen Sie die Platzhalter-Abschnitte mit Ihren Inhalten
5. Generieren Sie die Dokumentation mit: python -m src.cli --language de --process ihr-prozess-name

=============================================================================
-->

<!-- 
DOKUMENTEN-HEADER
Dieser Abschnitt wird automatisch aus meta-process.yaml befüllt.
Passen Sie die Werte in meta-process.yaml an, nicht hier im Template.
-->
# Prozess: {{ meta-process.name }}

**Dokument-ID:** {{ meta-process.id }}  
**Organisation:** {{ meta-organisation.name }}  
**Prozess Owner:** {{ meta-process.owner }}  
**Prozess Manager:** {{ meta-process.manager }}  
**Genehmigt durch:** {{ meta-process.approver }}  
**Revision:** {{ meta-process.revision }}  
**Author:** {{ meta-process.author }}  
**Status:** {{ meta-process.status }}  
**Klassifizierung:** {{ meta-process.classification }}  
**Letzte Aktualisierung:** {{ meta-process.modifydate }}  
**Template Version:** {{ meta-process.version }}

---

<!--
=============================================================================
ABSCHNITT 1: ZWECK UND ZIEL
=============================================================================
Beschreiben Sie hier den grundlegenden Zweck und die strategischen Ziele
des Prozesses. Dies hilft Stakeholdern zu verstehen, warum der Prozess
existiert und welchen Mehrwert er liefert.
-->

## 1. Zweck und Ziel

### 1.1 Zweck

<!--
Beschreiben Sie den Hauptzweck des Prozesses:
- Welches Problem löst der Prozess?
- Welchen Geschäftswert liefert er?
- Für wen ist der Prozess relevant?
-->
[Beschreibung des Zwecks des Prozesses]

### 1.2 Ziele

<!--
Listen Sie messbare Ziele auf, die der Prozess erreichen soll:
- Verwenden Sie SMART-Kriterien (Spezifisch, Messbar, Erreichbar, Relevant, Terminiert)
- Verknüpfen Sie Ziele mit KPIs (siehe Abschnitt 10)
-->
- Ziel 1: [Beschreibung]
- Ziel 2: [Beschreibung]
- Ziel 3: [Beschreibung]

<!--
=============================================================================
ABSCHNITT 2: GELTUNGSBEREICH
=============================================================================
Definieren Sie klar, was im Prozess enthalten ist und was nicht.
Kategorie und Kritikalität werden aus meta-process.yaml geladen.
-->

## 2. Geltungsbereich

**Kategorie:** {{ meta-process.category }}  
**Kritikalität:** {{ meta-process.criticality }}

<!--
Beschreiben Sie den Geltungsbereich:
- Welche Abteilungen/Teams sind betroffen?
- Welche Systeme/Anwendungen werden verwendet?
- Welche geografischen Standorte sind einbezogen?
- Was ist NICHT im Scope (Abgrenzung)?
-->
[Detaillierte Beschreibung des Geltungsbereichs]

<!--
=============================================================================
ABSCHNITT 3: TRIGGER UND EINGÄNGE
=============================================================================
Definieren Sie, was den Prozess startet und welche Informationen/Ressourcen
benötigt werden.
-->

## 3. Trigger und Eingänge

### 3.1 Trigger

<!--
Listen Sie alle Ereignisse auf, die den Prozess auslösen:
- Zeitbasierte Trigger (z.B. monatlich, quartalsweise)
- Ereignisbasierte Trigger (z.B. Incident gemeldet, Änderungsantrag eingereicht)
- Manuelle Trigger (z.B. auf Anforderung des Managements)
-->
- Trigger 1: [Beschreibung]
- Trigger 2: [Beschreibung]
- Trigger 3: [Beschreibung]

### 3.2 Eingänge

<!--
Listen Sie alle erforderlichen Inputs auf:
- Dokumente (z.B. Formulare, Anträge)
- Daten (z.B. aus anderen Systemen)
- Ressourcen (z.B. Personal, Budget)
- Informationen (z.B. von Stakeholdern)
-->
- Input 1: [Beschreibung]
- Input 2: [Beschreibung]
- Input 3: [Beschreibung]

<!--
=============================================================================
ABSCHNITT 4: ERGEBNISSE UND OUTPUTS
=============================================================================
Definieren Sie, was der Prozess produziert und wie Erfolg gemessen wird.
-->

## 4. Ergebnisse und Outputs

### 4.1 Outputs

<!--
Listen Sie alle Ergebnisse des Prozesses auf:
- Dokumente (z.B. Reports, Genehmigungen)
- Daten (z.B. aktualisierte Datensätze)
- Entscheidungen (z.B. Freigaben, Ablehnungen)
- Aktionen (z.B. implementierte Änderungen)
-->
- Output 1: [Beschreibung]
- Output 2: [Beschreibung]
- Output 3: [Beschreibung]

### 4.2 Erfolgskriterien

<!--
Definieren Sie messbare Erfolgskriterien:
- Qualitätskriterien (z.B. Fehlerrate < 5%)
- Zeitkriterien (z.B. Durchlaufzeit < 24h)
- Zufriedenheitskriterien (z.B. Kundenzufriedenheit > 90%)
-->
[Beschreibung der Erfolgskriterien]

<!--
=============================================================================
ABSCHNITT 5: ROLLEN UND VERANTWORTLICHKEITEN (RACI)
=============================================================================
Die RACI-Matrix wird aus meta-process.yaml geladen und zeigt, wer für welche
Aktivität verantwortlich ist. Passen Sie die RACI-Einträge in meta-process.yaml an.

RACI-REGELN:
- Jede Aktivität muss genau EINE Person/Rolle als "Accountable" haben
- Mehrere Personen können "Responsible" sein
- "Consulted" und "Informed" sind optional
- Vermeiden Sie zu viele "Consulted" (verlangsamt den Prozess)
-->

## 5. Rollen und Verantwortlichkeiten (RACI)

### 5.1 RACI-Matrix

<!--
Diese Tabelle wird automatisch aus meta-process.yaml befüllt.
Fügen Sie weitere Zeilen hinzu für zusätzliche Prozessschritte.
Die Rollen-Referenzen (role_*) werden aus meta-organisation-roles.yaml aufgelöst.
-->
| Aktivität | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Incident Detection | {{ meta-process.raci.incident_detection.responsible }} | {{ meta-process.raci.incident_detection.accountable }} | {{ meta-process.raci.incident_detection.consulted }} | {{ meta-process.raci.incident_detection.informed }} |
| Incident Analysis | {{ meta-process.raci.incident_analysis.responsible }} | {{ meta-process.raci.incident_analysis.accountable }} | {{ meta-process.raci.incident_analysis.consulted }} | {{ meta-process.raci.incident_analysis.informed }} |
| Incident Resolution | {{ meta-process.raci.incident_resolution.responsible }} | {{ meta-process.raci.incident_resolution.accountable }} | {{ meta-process.raci.incident_resolution.consulted }} | {{ meta-process.raci.incident_resolution.informed }} |

**Legende:**
- **R = Responsible (Durchführung):** Führt die Aktivität aus
- **A = Accountable (Verantwortlich):** Trägt die Gesamtverantwortung
- **C = Consulted (Konsultiert):** Wird vor Entscheidungen konsultiert
- **I = Informed (Informiert):** Wird über Ergebnisse informiert

<!--
=============================================================================
ABSCHNITT 6: ABLAUFDIAGRAMM (BPMN)
=============================================================================
Fügen Sie hier Ihr BPMN-Diagramm ein. Speichern Sie die Diagramm-Datei
im Unterverzeichnis "diagrams/".

BPMN-TOOLS:
- Camunda Modeler (kostenlos, empfohlen)
- draw.io / diagrams.net (kostenlos)
- Lucidchart (kommerziell)
- Microsoft Visio (kommerziell)

EXPORT-FORMATE:
- .bpmn (XML-Format, editierbar)
- .png oder .svg (für Anzeige in Dokumentation)
-->

## 6. Ablaufdiagramm (BPMN)

<!--
Ersetzen Sie "process-flow.bpmn" durch den Namen Ihrer Diagramm-Datei.
Wenn Sie ein Bild verwenden, ändern Sie die Dateiendung (z.B. .png, .svg).
-->
![Process Flow](diagrams/process-flow.bpmn)

### 6.1 Prozessschritte

<!--
Beschreiben Sie jeden Schritt im Prozess detailliert:
- Was wird gemacht?
- Wer macht es? (Verweis auf RACI-Matrix)
- Welche Systeme werden verwendet?
- Welche Entscheidungen werden getroffen?
- Was sind die Ausgänge?
-->
1. **Schritt 1:** [Detaillierte Beschreibung des ersten Schritts]
2. **Schritt 2:** [Detaillierte Beschreibung des zweiten Schritts]
3. **Schritt 3:** [Detaillierte Beschreibung des dritten Schritts]
4. **Schritt 4:** [Detaillierte Beschreibung des vierten Schritts]
5. **Schritt 5:** [Detaillierte Beschreibung des fünften Schritts]

<!--
=============================================================================
ABSCHNITT 7: SYSTEME UND TOOLS
=============================================================================
Listen Sie alle IT-Systeme und Tools auf, die im Prozess verwendet werden.
Die System-Liste kann aus meta-process.yaml geladen werden.
-->

## 7. Systeme und Tools

### 7.1 Verwendete Systeme

<!--
Passen Sie diese Liste an Ihre Umgebung an oder verwenden Sie den
Placeholder {{ meta-process.systems }}, um die Liste aus meta-process.yaml
zu laden. Für jedes System sollten Sie angeben:
- Name und Version
- Zweck im Prozess
- Zugriffsberechtigung
- Support-Kontakt
-->
- ServiceNow
- Zabbix
- Slack

[Oder dynamisch aus meta-process.yaml: {{ meta-process.systems }}]

### 7.2 Schnittstellen

<!--
Beschreiben Sie Schnittstellen zu anderen Systemen:
- API-Integrationen
- Datenimporte/-exporte
- Automatisierungen
- Benachrichtigungen
-->
[Beschreibung der Schnittstellen zu anderen Systemen]

<!--
=============================================================================
ABSCHNITT 8: ARTEFAKTE
=============================================================================
Dokumentieren Sie alle Artefakte, die während des Prozesses erstellt oder
verwendet werden.
-->

## 8. Artefakte

### 8.1 Tickets

<!--
Beschreiben Sie Ticket-Typen und deren Workflows:
- Welche Ticket-Typen werden verwendet?
- Welche Felder sind Pflicht/Optional?
- Welche Status-Übergänge gibt es?
- Wer kann Tickets erstellen/bearbeiten?
-->
[Beschreibung der Ticket-Typen und -Workflows]

### 8.2 Logs

<!--
Definieren Sie Logging-Anforderungen:
- Was muss geloggt werden?
- Wo werden Logs gespeichert?
- Wie lange werden Logs aufbewahrt?
- Wer hat Zugriff auf Logs?
- Compliance-Anforderungen (z.B. GDPR, Audit-Trail)
-->
[Beschreibung der Logging-Anforderungen]

### 8.3 Reports

<!--
Listen Sie alle Reports auf:
- Report-Name und Zweck
- Häufigkeit (täglich, wöchentlich, monatlich)
- Empfänger
- Datenquellen
-->
[Beschreibung der Report-Typen]

<!--
=============================================================================
ABSCHNITT 9: SLAs UND OLAs
=============================================================================
SLA-Werte werden aus meta-process.yaml geladen.
Passen Sie die Werte dort an Ihre Anforderungen an.

SLA vs. OLA:
- SLA (Service Level Agreement): Vereinbarung mit Kunden/Endbenutzern
- OLA (Operational Level Agreement): Interne Vereinbarung zwischen Teams
-->

## 9. SLAs und OLAs

### 9.1 Service Level Agreements

<!--
Diese Werte werden aus meta-process.yaml geladen.
Definieren Sie SLAs für verschiedene Prioritätsstufen:
- P1: Kritisch (Geschäftsbetrieb beeinträchtigt)
- P2: Hoch (Wichtige Funktionen beeinträchtigt)
- P3: Mittel (Eingeschränkte Funktionalität)
- P4: Niedrig (Kosmetische Probleme)
-->
- **P1 Resolution:** {{ meta-process.sla.p1_resolution }}
- **P2 Resolution:** {{ meta-process.sla.p2_resolution }}
- **P3 Resolution:** {{ meta-process.sla.p3_resolution }}

### 9.2 Operational Level Agreements

<!--
Beschreiben Sie interne OLAs:
- Zwischen welchen Teams?
- Welche Leistungen werden zugesagt?
- Welche Reaktionszeiten gelten?
- Wie wird die Einhaltung gemessen?
-->
[Beschreibung der OLA-Details]

<!--
=============================================================================
ABSCHNITT 10: KPIs UND METRIKEN
=============================================================================
KPI-Definitionen werden aus meta-process.yaml geladen.
Definieren Sie messbare Kennzahlen zur Prozessüberwachung.
-->

## 10. KPIs und Metriken

### 10.1 Key Performance Indicators

<!--
Diese KPIs werden aus meta-process.yaml geladen.
Passen Sie die KPIs an Ihre Prozessziele an (siehe Abschnitt 1.2).

BEISPIEL-KPIs:
- Effizienz: Durchlaufzeit, Bearbeitungszeit, Automatisierungsgrad
- Qualität: Fehlerrate, Nacharbeitsquote, Kundenzufriedenheit
- Compliance: Audit-Findings, SLA-Einhaltung, Dokumentationsvollständigkeit
-->
- **MTTR:** {{ meta-process.kpis.mttr }}
- **MTBF:** {{ meta-process.kpis.mtbf }}
- **First Call Resolution:** {{ meta-process.kpis.first_call_resolution }}

### 10.2 Messung und Reporting

<!--
Beschreiben Sie, wie KPIs gemessen und berichtet werden:
- Datenquellen (aus welchen Systemen?)
- Messfrequenz (täglich, wöchentlich, monatlich?)
- Reporting-Format (Dashboard, Report, Meeting?)
- Verantwortlichkeiten (wer sammelt/analysiert/berichtet?)
- Zielwerte und Schwellenwerte
-->
[Beschreibung der Messverfahren und Reporting-Mechanismen]

<!--
=============================================================================
ABSCHNITT 11: KONTROLLPUNKTE
=============================================================================
Definieren Sie Kontrollmechanismen zur Qualitätssicherung und Compliance.
Standard-Kontrollpunkte werden aus meta-global-process.yaml geladen.
-->

## 11. Kontrollpunkte

### 11.1 Prüfschritte

<!--
Diese Standard-Kontrollpunkte werden aus meta-global-process.yaml geladen.
Ergänzen Sie prozess-spezifische Kontrollpunkte:
- An welchen Stellen im Prozess?
- Wer führt die Kontrolle durch?
- Was wird geprüft?
- Wie wird das Ergebnis dokumentiert?
-->
- Management-Genehmigung
- Vier-Augen-Prinzip
- Audit-Trail

[Aus meta-global-process.yaml]

### 11.2 Audit-Anforderungen

<!--
Beschreiben Sie Audit-Anforderungen:
- Welche Compliance-Frameworks gelten? (siehe Abschnitt 12.1)
- Welche Nachweise müssen vorliegen?
- Wie oft finden Audits statt?
- Wer führt Audits durch (intern/extern)?
- Wie werden Audit-Findings behandelt?
-->
[Beschreibung der Audit-Details]

<!--
=============================================================================
ABSCHNITT 12: RISIKEN UND COMPLIANCE
=============================================================================
Compliance-Frameworks und SoD-Regeln werden aus meta-process.yaml geladen.
Dokumentieren Sie Risiken und deren Behandlung.
-->

## 12. Risiken und Compliance

### 12.1 Compliance-Frameworks

<!--
Diese Liste wird aus meta-process.yaml geladen.
Fügen Sie alle relevanten Compliance-Frameworks hinzu:
- ISO 27001 (Informationssicherheit)
- BSI IT-Grundschutz (IT-Sicherheit)
- GDPR/DSGVO (Datenschutz)
- SOX (Finanzberichterstattung)
- HIPAA (Gesundheitsdaten)
- PCI DSS (Zahlungskartendaten)

Geben Sie für jedes Framework die relevanten Klauseln/Controls an.
-->
- ISO 27001:2022 - Clause 5.24
- BSI IT-Grundschutz - DER.2.1

[Aus meta-process.yaml: {{ meta-process.compliance.frameworks }}]

### 12.2 Segregation of Duties (SoD)

<!--
SoD-Regeln werden aus meta-process.yaml geladen.
Segregation of Duties verhindert Interessenkonflikte und Betrug.

BEISPIELE FÜR SOD-REGELN:
- Wer Änderungen beantragt, darf sie nicht genehmigen
- Wer Code entwickelt, darf ihn nicht in Produktion deployen
- Wer Zahlungen auslöst, darf sie nicht genehmigen
- Wer Logs erstellt, darf sie nicht löschen/ändern
-->
- Incident-Handler kann eigene Eskalationen nicht genehmigen
- Security-Analyst kann Audit-Logs nicht ändern

[Aus meta-process.yaml: {{ meta-process.compliance.sod_rules }}]

### 12.3 Risiken

<!--
Führen Sie eine Risikoanalyse durch und dokumentieren Sie:
- Risikobeschreibung (was kann schiefgehen?)
- Wahrscheinlichkeit (Hoch/Mittel/Niedrig oder 1-5)
- Auswirkung (Hoch/Mittel/Niedrig oder 1-5)
- Risikoscore (Wahrscheinlichkeit × Auswirkung)
- Mitigation (wie wird das Risiko reduziert?)
- Verantwortlicher (wer überwacht das Risiko?)
-->
| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|--------|-------------------|------------|------------|
| [Risiko 1] | [Hoch/Mittel/Niedrig] | [Hoch/Mittel/Niedrig] | [Maßnahme] |
| [Risiko 2] | [Hoch/Mittel/Niedrig] | [Hoch/Mittel/Niedrig] | [Maßnahme] |
| [Risiko 3] | [Hoch/Mittel/Niedrig] | [Hoch/Mittel/Niedrig] | [Maßnahme] |

<!--
=============================================================================
ABSCHNITT 13: ESKALATIONEN UND AUSNAHMEN
=============================================================================
Eskalationswege werden aus meta-global-process.yaml geladen.
Die Rollen-Referenzen werden aus meta-organisation-roles.yaml aufgelöst.
-->

## 13. Eskalationen und Ausnahmen

### 13.1 Eskalationspfad

<!--
Diese Tabelle wird automatisch aus meta-global-process.yaml befüllt.
Die Eskalationswege sind global für alle Prozesse definiert.
Passen Sie bei Bedarf die Werte in meta-global-process.yaml an.

ESKALATIONSKRITERIEN:
- Level 1: Erste Anlaufstelle, normale Bearbeitung
- Level 2: Bei Verzögerungen oder komplexen Problemen
- Level 3: Bei kritischen Problemen oder Management-Entscheidungen
- Level 4: Bei geschäftskritischen Eskalationen oder Krisen
-->
| Level | Rolle | Kontakt |
|-------|-------|---------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} |

### 13.2 Ausnahmen

<!--
Beschreiben Sie den Prozess für Ausnahmen:
- Wann ist eine Ausnahme gerechtfertigt?
- Wer kann Ausnahmen genehmigen?
- Wie werden Ausnahmen dokumentiert?
- Wie lange sind Ausnahmen gültig?
- Wie werden Ausnahmen überwacht?

BEISPIELE FÜR AUSNAHMEN:
- Notfall-Änderungen ohne Change-Ticket
- Abweichung von Standard-Prozeduren
- Temporäre Umgehung von Kontrollen
-->
[Beschreibung des Ausnahmenprozesses]

<!--
=============================================================================
ABSCHNITT 14: ANHÄNGE
=============================================================================
Verlinken Sie hier auf zusätzliche Dokumente und Ressourcen.
-->

## 14. Anhänge

### 14.1 Checklisten

<!--
Verlinken Sie auf Checklisten für wiederkehrende Aufgaben:
- Pre-Flight-Checklisten
- Qualitätssicherungs-Checklisten
- Abnahme-Checklisten
- Audit-Checklisten

Speichern Sie Checklisten im gleichen Verzeichnis oder in einem
Unterverzeichnis "checklists/".
-->
[Links zu relevanten Checklisten]

### 14.2 Runbooks

<!--
Verlinken Sie auf detaillierte Runbooks/Playbooks:
- Schritt-für-Schritt-Anleitungen
- Troubleshooting-Guides
- Notfall-Prozeduren
- Wiederherstellungs-Prozeduren

Speichern Sie Runbooks im gleichen Verzeichnis oder in einem
Unterverzeichnis "runbooks/".
-->
[Links zu relevanten Runbooks]

### 14.3 Formulare

<!--
Verlinken Sie auf Formulare und Templates:
- Antragsformulare
- Genehmigungsformulare
- Dokumentations-Templates
- Report-Templates

Speichern Sie Formulare im gleichen Verzeichnis oder in einem
Unterverzeichnis "forms/".
-->
[Links zu relevanten Formularen]

---

<!--
=============================================================================
DOKUMENTENHISTORIE
=============================================================================
Pflegen Sie die Versionshistorie des Prozesses.
Fügen Sie für jede Änderung eine neue Zeile hinzu.
-->

## Dokumentenhistorie

<!-- 
ANLEITUNG: Dokumentenhistorie
- Pflegen Sie die Versionshistorie
- Dokumentieren Sie wesentliche Änderungen
- Fügen Sie neue Zeilen für jede Version hinzu
-->

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 19.02.2026 | Handbook Generator | Initiale Version |
| [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

---
