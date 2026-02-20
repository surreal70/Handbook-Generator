# Internes Auditprogramm (Template)

**Dokument-ID:** ISMS-0130
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



## 1. Zweck und Geltungsbereich

### 1.1 Zweck

Das interne Auditprogramm der **AdminSend GmbH** stellt sicher, dass:
- Das ISMS den Anforderungen von ISO 27001:2022 entspricht
- Das ISMS wirksam implementiert und aufrechterhalten wird
- Verbesserungspotenziale identifiziert werden
- Compliance mit Policies und Richtlinien sichergestellt wird

### 1.2 Geltungsbereich

Das Auditprogramm umfasst:
- Alle Bereiche im ISMS-Scope (siehe `0020_ISMS_Geltungsbereich_Scope.md`)
- Alle Annex A Controls im SoA (siehe `0100_ISMS_Statement_of_Applicability_SoA_Template.md`)
- Alle ISMS-Prozesse und -Dokumente
- Alle Standorte: [[ netbox.site.name ]] und weitere

## 2. Audit-Ansatz

### 2.1 Audit-Prinzipien

**Unabhängigkeit:**
- Auditoren prüfen nicht ihre eigenen Bereiche
- Externe Auditoren für kritische Bereiche (optional)
- Berichtslinie: Audit-Team berichtet an {{ meta-handbook.audit_manager }}

**Risikobasiert:**
- Audit-Frequenz basiert auf Risikobewertung
- Kritische Bereiche werden häufiger geprüft
- Fokus auf hohe Risiken und kritische Controls

**Scope-bezogen:**
- Alle Bereiche im ISMS-Scope werden geprüft
- Vollständige Abdeckung innerhalb des Audit-Zyklus (3 Jahre)

**Objektiv und evidenzbasiert:**
- Audit-Findings basieren auf objektiven Nachweisen
- Stichprobenbasierte Prüfung
- Dokumentation aller Findings

### 2.2 Audit-Typen

**Vollständiges ISMS-Audit:**
- Frequenz: Jährlich
- Scope: Gesamtes ISMS
- Dauer: 5-10 Tage

**Themen-Audits:**
- Frequenz: Quartalsweise
- Scope: Spezifische Themen (z.B. Access Management, Patch Management)
- Dauer: 1-2 Tage

**Follow-up-Audits:**
- Frequenz: Nach Bedarf
- Scope: Überprüfung der Umsetzung von Korrekturmaßnahmen
- Dauer: 0,5-1 Tag

## 3. Jahresplan

### 3.1 Audit-Jahresplan 2026

| Zeitraum | Audit-Thema/Scope | Audit-Typ | Kriterien | Auditor | Auditee | Geplante Dauer | Status |
|----------|-------------------|-----------|-----------|---------|---------|----------------|--------|
| **Q1 2026** | Access Management & IAM | Themen-Audit | A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3 | [TODO] | [TODO] | 2 Tage | Geplant |
| **Q2 2026** | Vulnerability & Patch Management | Themen-Audit | A.8.8, A.5.23 | [TODO] | IT-Betrieb | 1 Tag | Geplant |
| **Q3 2026** | Vollständiges ISMS-Audit | Vollaudit | Alle Clauses, SoA | [TODO] | [TODO] | 10 Tage | Geplant |
| **Q4 2026** | Incident Management & Logging | Themen-Audit | A.5.24, A.5.25, A.5.26, A.5.28, A.8.15, A.8.16 | [TODO] | Security Team | 2 Tage | Geplant |

[TODO: Audit-Plan für 2026 vervollständigen]

### 3.2 Audit-Frequenz nach Risiko

| Bereich | Risikostufe | Audit-Frequenz |
|---------|-------------|----------------|
| Privileged Access Management | Hoch | Halbjährlich |
| Vulnerability Management | Hoch | Halbjährlich |
| Incident Management | Hoch | Halbjährlich |
| Backup & Recovery | Mittel | Jährlich |
| Physical Security | Mittel | Jährlich |
| HR Security | Niedrig | Alle 2 Jahre |

## 4. Audit-Prozess

### 4.1 Audit-Phasen

```
1. Planung
   ├─ Audit-Scope definieren
   ├─ Audit-Team benennen
   ├─ Audit-Plan erstellen
   └─ Auditee informieren
   
2. Vorbereitung
   ├─ Dokumente anfordern
   ├─ Audit-Checkliste erstellen
   ├─ Stichproben definieren
   └─ Interviews planen
   
3. Durchführung
   ├─ Opening Meeting
   ├─ Dokumentenprüfung
   ├─ Interviews
   ├─ Stichproben
   ├─ Beobachtungen
   └─ Closing Meeting
   
4. Berichterstattung
   ├─ Findings dokumentieren
   ├─ Audit-Bericht erstellen
   ├─ Bericht an Auditee
   └─ Bericht an Management
   
5. Follow-up
   ├─ Korrekturmaßnahmen planen
   ├─ Umsetzung überwachen
   ├─ Follow-up-Audit
   └─ Findings schließen
```

### 4.2 Audit-Checkliste (Beispiel)

**Audit-Thema: Access Management**

| Prüfpunkt | Kriterium | Nachweis | Ergebnis | Bemerkungen |
|-----------|-----------|----------|----------|-------------|
| Sind Zugriffsrechte dokumentiert? | Policy 0220 | IAM-Dokumentation | ✓ / ✗ | |
| Werden Zugriffsrechte regelmäßig rezertifiziert? | Richtlinie 0230 | Rezertifizierungsprotokolle | ✓ / ✗ | |
| Ist das Least-Privilege-Prinzip umgesetzt? | A.8.2 | IAM-Konfiguration | ✓ / ✗ | |
| Werden Joiner/Mover/Leaver-Prozesse befolgt? | Richtlinie 0230 | HR-Tickets, IAM-Logs | ✓ / ✗ | |
| Ist MFA für alle Benutzer aktiviert? | A.5.17 | MFA-Konfiguration | ✓ / ✗ | |

[TODO: Vollständige Checklisten für alle Audit-Themen erstellen]

### 4.3 Audit-Kriterien

**Dokumentenprüfung:**
- Sind Dokumente aktuell und freigegeben?
- Sind Dokumente vollständig und konsistent?
- Sind Verantwortlichkeiten definiert?

**Evidence-Prüfung:**
- Ist Evidence vorhanden und aktuell?
- Ist Evidence nachvollziehbar?
- Ist Evidence ausreichend für Nachweis?

**Control-Wirksamkeit:**
- Ist das Control implementiert?
- Ist das Control wirksam (Stichproben)?
- Gibt es Abweichungen oder Schwachstellen?

**Compliance:**
- Werden Policies und Richtlinien befolgt?
- Werden gesetzliche Anforderungen erfüllt?
- Werden vertragliche Verpflichtungen erfüllt?

## 5. Audit-Findings

### 5.1 Finding-Kategorien

**Major Non-Conformity (Schwerwiegend):**
- Wesentlicher Verstoß gegen ISO 27001:2022
- Kritisches Control nicht implementiert
- Systemischer Fehler
- **Beispiel:** Keine Risikoanalyse durchgeführt

**Minor Non-Conformity (Geringfügig):**
- Kleinerer Verstoß gegen ISO 27001:2022
- Control teilweise implementiert
- Isolierter Fehler
- **Beispiel:** Dokumentation unvollständig

**Observation (Beobachtung):**
- Verbesserungspotenzial
- Best Practice nicht umgesetzt
- Kein Verstoß gegen Anforderungen
- **Beispiel:** Prozess könnte effizienter sein

**Opportunity for Improvement (Verbesserungsmöglichkeit):**
- Empfehlung für Verbesserung
- Keine Abweichung
- **Beispiel:** Automatisierung möglich

### 5.2 Finding-Dokumentation

**Für jedes Finding:**
- Finding-ID (z.B. F-2026-Q1-001)
- Kategorie (Major/Minor/Observation)
- Beschreibung
- Betroffener Bereich/Control
- Nachweis/Evidence
- Auswirkung
- Empfohlene Korrekturmaßnahme
- Verantwortlicher
- Frist

### 5.3 Korrekturmaßnahmen

**Prozess:**
1. Auditee plant Korrekturmaßnahme
2. CISO genehmigt Maßnahme und Frist
3. Auditee setzt Maßnahme um
4. Auditor prüft Umsetzung (Follow-up)
5. Finding wird geschlossen

**Fristen:**
- Major Non-Conformity: 30 Tage
- Minor Non-Conformity: 90 Tage
- Observation: 180 Tage

## 6. Audit-Bericht

### 6.1 Berichtsstruktur

**Executive Summary:**
- Audit-Scope und -Ziel
- Audit-Datum und -Team
- Zusammenfassung der Ergebnisse
- Gesamtbewertung

**Audit-Details:**
- Audit-Methodik
- Geprüfte Bereiche und Controls
- Stichproben
- Interviews

**Findings:**
- Liste aller Findings (nach Kategorie)
- Detailbeschreibung jedes Findings
- Empfohlene Korrekturmaßnahmen

**Positive Beobachtungen:**
- Best Practices
- Gut umgesetzte Controls
- Verbesserungen seit letztem Audit

**Schlussfolgerung:**
- Gesamtbewertung des ISMS
- Empfehlungen
- Nächste Schritte

### 6.2 Berichtsverteilung

**Empfänger:**
- Auditee
- CISO
- Geschäftsführung
- Informationssicherheitsgremium

**Vertraulichkeit:**
- Audit-Berichte sind vertraulich
- Zugriff nur für berechtigte Personen

## 7. Auditor-Qualifikation

### 7.1 Anforderungen an Auditoren

**Fachliche Qualifikation:**
- Kenntnisse ISO 27001:2022
- Kenntnisse ISO 27002:2022
- Kenntnisse Audit-Methodik
- Branchenkenntnisse

**Zertifizierungen (empfohlen):**
- ISO 27001 Lead Auditor
- CISA (Certified Information Systems Auditor)
- CISM (Certified Information Security Manager)

**Soft Skills:**
- Kommunikationsfähigkeit
- Objektivität
- Analytisches Denken
- Dokumentationsfähigkeit

### 7.2 Auditor-Training

**Initiales Training:**
- ISO 27001:2022 Schulung
- Audit-Methodik-Schulung
- Shadowing erfahrener Auditoren

**Kontinuierliche Weiterbildung:**
- Jährliche Auffrischung
- Teilnahme an Auditor-Konferenzen
- Austausch mit anderen Auditoren

## 8. Audit-Metriken

### 8.1 KPIs

| Metrik | Zielwert | Aktuell | Status |
|--------|----------|---------|--------|
| Audit-Plan-Erfüllung | 100% | [TODO]% | [TODO] |
| Durchschnittliche Zeit zur Behebung (Major) | < 30 Tage | [TODO] Tage | [TODO] |
| Durchschnittliche Zeit zur Behebung (Minor) | < 90 Tage | [TODO] Tage | [TODO] |
| Anzahl offener Findings | < 5 | [TODO] | [TODO] |
| Wiederkehrende Findings | 0 | [TODO] | [TODO] |

### 8.2 Trend-Analyse

**Jährlicher Review:**
- Anzahl Findings pro Jahr (Trend)
- Häufigste Finding-Kategorien
- Bereiche mit den meisten Findings
- Verbesserungen seit Vorjahr

## 9. Rollen und Verantwortlichkeiten

### 9.1 RACI-Matrix: Audit-Prozess

| Aktivität | Audit Manager | Auditor | Auditee | CISO | Geschäftsführung |
|-----------|---------------|---------|---------|------|------------------|
| Audit-Programm erstellen | R/A | C | C | C | I |
| Audit planen | R | R | C | I | I |
| Audit durchführen | A | R | C | I | I |
| Findings dokumentieren | A | R | C | I | I |
| Audit-Bericht erstellen | R/A | R | C | I | I |
| Korrekturmaßnahmen planen | C | C | R/A | C | I |
| Follow-up durchführen | A | R | C | I | I |
| Audit-Programm reviewen | R/A | C | C | C | C |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 10. Referenzen

### 10.1 Interne Dokumente

- `0020_ISMS_Geltungsbereich_Scope.md` - ISMS Scope
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA
- `0140_ISMS_Management_Review_Template.md` - Management Review
- `0150_ISMS_Nichtkonformitaeten_und_Korrekturmassnahmen.md` - Non-conformities
- Alle Policies (0200-0680) und Richtlinien (0210-0690)

### 10.2 Externe Standards

- **ISO/IEC 27001:2022** - Clause 9.2: Internal audit
- **ISO 19011:2018** - Guidelines for auditing management systems
- **ISO/IEC 27007:2020** - Guidelines for information security management systems auditing

**Genehmigt durch:**  
{{ meta-handbook.audit_manager }}, Audit Manager  
[TODO], CISO  
Datum: [TODO]

**Nächster Review:** [TODO]

