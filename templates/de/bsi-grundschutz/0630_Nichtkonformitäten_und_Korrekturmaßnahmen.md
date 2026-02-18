# Nichtkonformitäten und Korrekturmaßnahmen

**Dokument-ID:** 0630
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
This template defines the process for handling non-conformities and corrective actions.
Reference: BSI Standard 200-1 (Non-conformities and Corrective Actions)
-->

## 1. Zweck und Zielsetzung

Dieser Prozess stellt sicher, dass Abweichungen von ISMS-Anforderungen systematisch erfasst, behandelt und deren Wirksamkeit geprüft wird.

**Verantwortlich:** {{ meta.ciso.name }} (ISB)

## 2. Quellen für Nichtkonformitäten

**Nichtkonformitäten können identifiziert werden durch:**
- Interne Audits (Dokument 0610)
- Basis-Sicherheitscheck (Dokument 0080)
- Sicherheitsvorfälle (Dokument 0320/0330)
- Penetrationstests und Vulnerability Scans
- Policy-Verstöße
- Management Review (Dokument 0620)
- Externe Audits

## 3. Prozess

### 3.1 Erfassen

**Schritt 1: Identifikation und Dokumentation**
- Nichtkonformität wird identifiziert
- Finding wird im Findings-Register erfasst (siehe Abschnitt 4)
- Kategorisierung: Kritisch/Hoch/Mittel/Niedrig

**Verantwortlich:** Identifizierende Person (Auditor, ISB, etc.)

### 3.2 Ursachenanalyse

**Schritt 2: Root Cause Analysis**
- Warum ist die Nichtkonformität aufgetreten?
- Welche Prozesse/Kontrollen haben versagt?
- Ist dies ein Einzelfall oder systemisches Problem?

**Methoden:**
- 5-Why-Analyse
- Fishbone-Diagramm
- Prozessanalyse

**Verantwortlich:** ISB, betroffener Bereichsverantwortlicher

### 3.3 Maßnahme definieren

**Schritt 3: Korrekturmaßnahme festlegen**
- Sofortmaßnahme (Symptom beheben)
- Korrekturmaßnahme (Ursache beheben)
- Präventivmaßnahme (Wiederholung verhindern)

**Verantwortlich:** ISB, Maßnahmen-Owner

### 3.4 Umsetzung

**Schritt 4: Maßnahme umsetzen**
- Maßnahme wird implementiert
- Fortschritt wird getrackt
- Dokumentation der Umsetzung

**Verantwortlich:** Maßnahmen-Owner

### 3.5 Wirksamkeitsprüfung

**Schritt 5: Effectiveness Check**
- Wurde die Nichtkonformität behoben?
- Ist die Ursache beseitigt?
- Sind keine neuen Probleme entstanden?

**Methoden:**
- Follow-up Audit
- Stichprobenprüfung
- KPI-Monitoring

**Verantwortlich:** ISB, Internal Audit

### 3.6 Abschluss

**Schritt 6: Closure**
- Wirksamkeit bestätigt
- Finding geschlossen
- Lessons Learned dokumentiert

**Verantwortlich:** ISB

## 4. Findings-Register

| Finding-ID | Quelle | Datum | Beschreibung | Kategorie | Root Cause | Maßnahme | Owner | Fällig | Status | Wirksamkeit geprüft am |
|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | Audit Q1 | [TODO] | [TODO] | Hoch | [TODO] | [TODO] | [TODO] | [TODO] | Offen | - |
| F-002 | Basis-Check | [TODO] | [TODO] | Mittel | [TODO] | [TODO] | [TODO] | [TODO] | In Bearbeitung | - |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Status-Werte:**
- **Offen:** Neu identifiziert
- **In Analyse:** Ursachenanalyse läuft
- **In Bearbeitung:** Maßnahme wird umgesetzt
- **Wirksamkeitsprüfung:** Maßnahme umgesetzt, Prüfung ausstehend
- **Geschlossen:** Wirksamkeit bestätigt

## 5. Kategorisierung und Reaktionszeiten

| Kategorie | Beschreibung | Reaktionszeit | Eskalation |
|---|---|---|---|
| **Kritisch** | Schwerwiegende Abweichung, hohes Risiko | Sofort | Geschäftsführung |
| **Hoch** | Wesentliche Abweichung | 7 Tage | ISB |
| **Mittel** | Verbesserungspotenzial | 30 Tage | Bereichsverantwortlicher |
| **Niedrig** | Kleinere Abweichung | 90 Tage | Bereichsverantwortlicher |

## 6. Reporting

**Monatlich:**
- Anzahl offener Findings (nach Kategorie)
- Überfällige Findings
- Abgeschlossene Findings

**Quartalsweise:**
- Trend-Analyse
- Top-Findings-Kategorien
- Wirksamkeit von Korrekturmaßnahmen

**Verantwortlich:** {{ meta.ciso.name }}  
**Empfänger:** Geschäftsführung, ISMS-Team

## 7. Lessons Learned

Nach Abschluss kritischer oder wiederkehrender Findings:
1. **Retrospektive:** Was lief gut? Was nicht?
2. **Prozessverbesserung:** Anpassung von Prozessen/Kontrollen
3. **Dokumentation:** Lessons Learned dokumentieren
4. **Kommunikation:** Erkenntnisse teilen (Awareness)

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | {{ meta.ciso.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| IT-Leitung | {{ meta.cio.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**Referenzen:**
- BSI Standard 200-1: ISMS (Non-conformities and Corrective Actions)
- Dokument 0610: Internes Auditprogramm

<!-- End of template -->