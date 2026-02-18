# Nichtkonformitäten und Korrekturmaßnahmen

**Dokument-ID:** 0150
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
This document defines the process for handling non-conformities and implementing
corrective actions. It ensures systematic treatment of deviations from requirements
and drives continuous improvement.

ISO 27001:2022 Reference: Clause 10.1 - Nonconformity and corrective action
-->

## 1. Zweck und Ziel

### 1.1 Zweck

Dieses Dokument definiert den Prozess zur systematischen Behandlung von Nichtkonformitäten (Non-Conformities) im ISMS der **{{ meta-organisation.name }}**. Es stellt sicher, dass:
- Abweichungen von Anforderungen erkannt und dokumentiert werden
- Ursachen analysiert und behoben werden
- Korrekturmaßnahmen wirksam umgesetzt werden
- Wiederholungen verhindert werden

### 1.2 Arten von Nichtkonformitäten

**Audit-Findings:**
- Major Non-Conformities (schwerwiegend)
- Minor Non-Conformities (geringfügig)
- Observations (Beobachtungen)

**Security Incidents:**
- Sicherheitsvorfälle mit Ursache in Prozess-/Control-Schwächen

**Policy-Verstöße:**
- Verstöße gegen ISMS-Policies und -Richtlinien

**Compliance-Verstöße:**
- Verstöße gegen gesetzliche oder vertragliche Anforderungen

## 2. Prozess

### 2.1 Prozessübersicht

```
1. Erfassen
   ├─ Nichtkonformität identifizieren
   ├─ Ticket/Finding erstellen
   └─ Kategorisieren und priorisieren
   
2. Ursachenanalyse
   ├─ Root Cause Analysis durchführen
   ├─ Beitragende Faktoren identifizieren
   └─ Systemische Ursachen erkennen
   
3. Korrekturmaßnahme definieren
   ├─ Sofortmaßnahme (Containment)
   ├─ Korrekturmaßnahme (Corrective Action)
   └─ Präventivmaßnahme (Preventive Action)
   
4. Umsetzung
   ├─ Maßnahme implementieren
   ├─ Fortschritt tracken
   └─ Dokumentieren
   
5. Wirksamkeitsprüfung
   ├─ Wirksamkeit verifizieren
   ├─ Follow-up durchführen
   └─ Lessons Learned dokumentieren
   
6. Abschluss
   ├─ Finding schließen
   ├─ Dokumentation archivieren
   └─ Kommunikation
```

### 2.2 Schritt 1: Erfassen

**Identifikation:**
- Durch Audits (intern/extern)
- Durch Security Incidents
- Durch Monitoring und KPIs
- Durch Mitarbeiter-Meldungen
- Durch Management Reviews

**Dokumentation:**
- Finding-ID vergeben (z.B. F-2026-001)
- Beschreibung der Nichtkonformität
- Betroffener Bereich/Control
- Nachweis/Evidence
- Kategorisierung (Major/Minor/Observation)
- Priorität (Hoch/Mittel/Niedrig)

**Verantwortlich:** Auditor, ISMS Manager, oder Melder

### 2.3 Schritt 2: Ursachenanalyse

**Root Cause Analysis (RCA):**
- **5-Why-Methode:** Warum ist das passiert? (5x fragen)
- **Fishbone-Diagramm:** Ursachen-Kategorien (Mensch, Prozess, Technologie, Umgebung)
- **Fault Tree Analysis:** Logische Analyse von Fehlerursachen

**Zu identifizieren:**
- Direkte Ursache (Immediate Cause)
- Grundursache (Root Cause)
- Beitragende Faktoren (Contributing Factors)
- Systemische Ursachen (Systemic Causes)

**Dokumentation:**
- RCA-Methode
- Identifizierte Ursachen
- Beitragende Faktoren

**Verantwortlich:** Finding-Owner, unterstützt durch ISMS Manager

### 2.4 Schritt 3: Korrekturmaßnahme definieren

**Sofortmaßnahme (Immediate Action):**
- Eindämmung des Problems
- Schadensbegrenzung
- Temporäre Lösung

**Korrekturmaßnahme (Corrective Action):**
- Behebung der Grundursache
- Dauerhafte Lösung
- Prozess-/Control-Verbesserung

**Präventivmaßnahme (Preventive Action):**
- Verhinderung von Wiederholungen
- Verhinderung ähnlicher Probleme
- Systemische Verbesserungen

**Dokumentation:**
- Beschreibung der Maßnahme
- Verantwortlicher
- Frist
- Ressourcen/Budget
- Erfolgskriterien

**Verantwortlich:** Finding-Owner, genehmigt durch CISO

### 2.5 Schritt 4: Umsetzung

**Implementierung:**
- Maßnahme gemäß Plan umsetzen
- Fortschritt dokumentieren
- Stakeholder informieren

**Tracking:**
- Regelmäßige Status-Updates
- Eskalation bei Verzögerungen
- Anpassung bei Problemen

**Dokumentation:**
- Umsetzungsschritte
- Abweichungen vom Plan
- Lessons Learned

**Verantwortlich:** Finding-Owner

### 2.6 Schritt 5: Wirksamkeitsprüfung

**Verifikation:**
- Ist die Maßnahme umgesetzt?
- Ist die Nichtkonformität behoben?
- Ist die Grundursache beseitigt?

**Validierung:**
- Ist die Maßnahme wirksam?
- Tritt das Problem noch auf?
- Gibt es unbeabsichtigte Nebenwirkungen?

**Methoden:**
- Follow-up-Audit
- Stichproben
- Monitoring
- Interviews

**Dokumentation:**
- Wirksamkeitsprüfung durchgeführt am
- Methode
- Ergebnis
- Nachweis/Evidence

**Verantwortlich:** Auditor oder ISMS Manager

### 2.7 Schritt 6: Abschluss

**Kriterien für Abschluss:**
- Maßnahme vollständig umgesetzt
- Wirksamkeit nachgewiesen
- Dokumentation vollständig
- Lessons Learned dokumentiert

**Abschluss-Aktivitäten:**
- Finding-Status auf "Geschlossen" setzen
- Dokumentation archivieren
- Stakeholder informieren
- Lessons Learned kommunizieren

**Verantwortlich:** ISMS Manager

## 3. Nichtkonformitäten-Register

### 3.1 Aktive Nichtkonformitäten

| Finding-ID | Quelle | Kategorie | Beschreibung | Root Cause | Korrekturmaßnahme | Owner | Fällig | Status | Wirksamkeit geprüft |
|------------|--------|-----------|--------------|------------|-------------------|-------|--------|--------|---------------------|
| F-2026-001 | Audit | Minor | Dokumentation unvollständig | Prozess nicht definiert | Prozess dokumentieren | [TODO] | 2026-03-31 | In Arbeit | - |
| F-2026-002 | Incident | Major | Ungepatchte Schwachstelle ausgenutzt | Patch-Prozess unzureichend | Patch-Prozess verbessern | IT-Betrieb | 2026-02-28 | In Arbeit | - |
| F-2026-003 | Monitoring | Observation | MFA-Aktivierung < 100% | Awareness unzureichend | MFA-Kampagne | {{ meta.ciso.name }} | 2026-04-30 | Geplant | - |

[TODO: Aktive Nichtkonformitäten hinzufügen]

### 3.2 Geschlossene Nichtkonformitäten (Archiv)

| Finding-ID | Quelle | Kategorie | Beschreibung | Korrekturmaßnahme | Abschlussdatum | Wirksamkeit bestätigt |
|------------|--------|-----------|--------------|-------------------|----------------|----------------------|
| F-2025-050 | Audit | Minor | Backup-Tests nicht dokumentiert | Backup-Test-Prozess etabliert | 2026-01-15 | Ja |
| F-2025-051 | Incident | Major | Phishing-Incident | Security Awareness Training | 2026-01-20 | Ja |

[TODO: Geschlossene Nichtkonformitäten archivieren]

## 4. Priorisierung und Fristen

### 4.1 Priorisierung

| Kategorie | Priorität | Frist | Eskalation |
|-----------|-----------|-------|------------|
| Major Non-Conformity | Sehr hoch | 30 Tage | Sofort an CISO und Geschäftsführung |
| Minor Non-Conformity | Hoch | 90 Tage | Bei Verzögerung an CISO |
| Observation | Mittel | 180 Tage | Bei Verzögerung an ISMS Manager |
| Opportunity for Improvement | Niedrig | Nach Verfügbarkeit | Keine |

### 4.2 Eskalation

**Überfällige Maßnahmen:**
- > 2 Wochen überfällig: Erinnerung an Owner
- > 4 Wochen überfällig: Eskalation an CISO
- > 8 Wochen überfällig: Eskalation an Geschäftsführung

**Kritische Nichtkonformitäten:**
- Major Non-Conformities: Sofortige Eskalation
- Compliance-Verstöße: Sofortige Eskalation
- Wiederholte Nichtkonformitäten: Eskalation an Management

## 5. Ursachenanalyse-Methoden

### 5.1 5-Why-Methode

**Beispiel:**
1. **Warum** trat die Nichtkonformität auf? → Ungepatchte Schwachstelle wurde ausgenutzt
2. **Warum** war die Schwachstelle ungepatcht? → Patch wurde nicht rechtzeitig installiert
3. **Warum** wurde der Patch nicht rechtzeitig installiert? → Patch-Prozess hat Patch nicht priorisiert
4. **Warum** hat der Prozess den Patch nicht priorisiert? → CVSS-Score wurde nicht berücksichtigt
5. **Warum** wurde CVSS-Score nicht berücksichtigt? → Prozess berücksichtigt nur Vendor-Severity

**Root Cause:** Patch-Priorisierung basiert nicht auf CVSS-Score

**Korrekturmaßnahme:** Patch-Prozess um CVSS-basierte Priorisierung erweitern

### 5.2 Fishbone-Diagramm (Ishikawa)

**Kategorien:**
- **Mensch:** Fehlende Schulung, Fehler, Fahrlässigkeit
- **Prozess:** Unzureichende Prozesse, fehlende Dokumentation
- **Technologie:** Fehlende Tools, Fehlkonfiguration, Bugs
- **Umgebung:** Organisatorische Faktoren, Ressourcenmangel

## 6. Wirksamkeitsprüfung

### 6.1 Methoden

**Audit:**
- Follow-up-Audit
- Stichprobenprüfung
- Dokumentenprüfung

**Monitoring:**
- KPI-Tracking
- Incident-Tracking
- Compliance-Monitoring

**Testing:**
- Penetration Tests
- Vulnerability Scans
- Configuration Audits

**Interviews:**
- Befragung betroffener Personen
- Feedback-Sammlung

### 6.2 Erfolgskriterien

**Maßnahme ist wirksam, wenn:**
- Nichtkonformität tritt nicht mehr auf
- Root Cause ist beseitigt
- KPIs haben sich verbessert
- Keine neuen Probleme entstanden sind
- Stakeholder sind zufrieden

## 7. Lessons Learned

### 7.1 Dokumentation

**Für jede geschlossene Nichtkonformität:**
- Was haben wir gelernt?
- Was hat gut funktioniert?
- Was könnte verbessert werden?
- Welche Maßnahmen sind übertragbar?

### 7.2 Kommunikation

**Zielgruppen:**
- Betroffene Teams
- ISMS-Gremium
- Management
- Alle Mitarbeiter (bei relevanten Lessons Learned)

**Kanäle:**
- Lessons-Learned-Datenbank
- Security Newsletter
- Team-Meetings
- Awareness-Kampagnen

## 8. Rollen und Verantwortlichkeiten

### 8.1 RACI-Matrix: Nichtkonformitäten-Prozess

| Aktivität | CISO | ISMS Manager | Finding-Owner | Auditor | Geschäftsführung |
|-----------|------|--------------|---------------|---------|------------------|
| Nichtkonformität erfassen | A | R | C | R | I |
| Ursachenanalyse | A | C | R | C | I |
| Maßnahme definieren | A | C | R | C | I |
| Maßnahme genehmigen | A | C | I | I | C |
| Maßnahme umsetzen | A | C | R | I | I |
| Wirksamkeit prüfen | A | R | C | R | I |
| Finding schließen | A | R | C | C | I |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 9. Metriken und Reporting

### 9.1 KPIs

| Metrik | Zielwert | Aktuell | Status |
|--------|----------|---------|--------|
| Offene Major Findings | 0 | [TODO] | ✓ / ✗ |
| Offene Minor Findings | < 5 | [TODO] | ✓ / ✗ |
| Durchschnittliche Behebungszeit (Major) | < 30 Tage | [TODO] Tage | ✓ / ✗ |
| Durchschnittliche Behebungszeit (Minor) | < 90 Tage | [TODO] Tage | ✓ / ✗ |
| Überfällige Findings | 0 | [TODO] | ✓ / ✗ |
| Wiederkehrende Findings | 0 | [TODO] | ✓ / ✗ |

### 9.2 Reporting

**Monatlich:**
- Status aller offenen Findings
- Überfällige Findings
- Neu hinzugekommene Findings

**Quartalsweise:**
- Trend-Analyse
- Häufigste Ursachen
- Wirksamkeit von Maßnahmen

**Jährlich:**
- Vollständiger Review im Management Review
- Lessons Learned Zusammenfassung

## 10. Referenzen

### 10.1 Interne Dokumente

- `0130_ISMS_Internes_Auditprogramm.md` - Internal Audit Program
- `0140_ISMS_Management_Review_Template.md` - Management Review
- `0160_ISMS_Kontinuierliche_Verbesserung.md` - Continuous Improvement
- `0400_Policy_Incident_Management.md` - Incident Management

### 10.2 Externe Standards

- **ISO/IEC 27001:2022** - Clause 10.1: Nonconformity and corrective action
- **ISO 9001:2015** - Clause 10.2: Nonconformity and corrective action
- **ISO 19011:2018** - Guidelines for auditing management systems

**Genehmigt durch:**  
{{ meta.ciso.name }}, CISO  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }}

