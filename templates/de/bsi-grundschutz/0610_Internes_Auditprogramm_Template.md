# Internes Auditprogramm (Template)

**Dokument-ID:** 0610  
**Dokumenttyp:** Programm/Template  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the internal audit program for ISMS.
Reference: BSI Standard 200-1 (Internal Audits), DER.3.1
-->

## 1. Zweck und Zielsetzung

Das interne Auditprogramm von **{{ meta.organization.name }}** stellt die Wirksamkeit des ISMS sicher.

**Verantwortlich:** [TODO: Internal Audit]

## 2. Audit-Ansatz

**Prinzipien:**
- **Risikobasiert:** Fokus auf kritische Bereiche
- **Unabhängig:** Auditoren sind unabhängig vom auditierten Bereich
- **Scope-bezogen:** Audits decken den gesamten ISMS-Scope ab
- **Systematisch:** Strukturierter Audit-Prozess

## 3. Audit-Plan

| Zeitraum | Audit-Thema | Kriterien | Auditor | Auditee | Status | Ergebnis | Maßnahmen |
|---|---|---|---|---|---|---|---|
| Q1 {{ meta.document.year }} | Basis-Sicherheitscheck Stichprobe | Policies, Richtlinien, Evidence | [TODO] | {{ meta.cio.name }} | Geplant | - | - |
| Q2 {{ meta.document.year }} | Risikomanagement-Prozess | Dokument 0090, Risikoregister | [TODO] | {{ meta.ciso.name }} | Geplant | - | - |
| Q3 {{ meta.document.year }} | Incident Management | Dokument 0320/0330, Incident-Logs | [TODO] | {{ meta.cio.name }} | Geplant | - | - |
| Q4 {{ meta.document.year }} | Dokumentenlenkung | Dokument 0030, Dokumentenregister | [TODO] | {{ meta.ciso.name }} | Geplant | - | - |

## 4. Audit-Checkpunkte

**Standardprüfungen:**
- Sind Dokumente aktuell und freigegeben?
- Ist Evidence vorhanden und nachvollziehbar?
- Ist der Maßnahmenstatus plausibel?
- Sind Abweichungen dokumentiert und behandelt?
- Werden Prozesse gelebt (nicht nur dokumentiert)?

## 5. Audit-Prozess

1. **Planung:** Audit-Scope, Kriterien, Zeitplan
2. **Vorbereitung:** Dokumentenreview, Checklisten
3. **Durchführung:** Interviews, Stichproben, Begehungen
4. **Berichterstattung:** Audit-Bericht mit Findings
5. **Follow-up:** Nachverfolgung von Korrekturmaßnahmen

## 6. Audit-Bericht Template

**Struktur:**
1. Executive Summary
2. Audit-Scope und Kriterien
3. Audit-Methodik
4. Findings (Kategorisiert: Kritisch/Hoch/Mittel/Niedrig)
5. Positive Beobachtungen
6. Empfehlungen
7. Maßnahmenplan

## 7. Findings-Kategorisierung

| Kategorie | Beschreibung | Reaktionszeit |
|---|---|---|
| **Kritisch** | Schwerwiegende Abweichung, hohes Risiko | Sofort |
| **Hoch** | Wesentliche Abweichung | 30 Tage |
| **Mittel** | Verbesserungspotenzial | 90 Tage |
| **Niedrig** | Kleinere Abweichung | 180 Tage |

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| Internal Audit | [TODO] | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| ISB | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**Referenzen:**
- BSI Standard 200-1: ISMS
- BSI IT-Grundschutz-Kompendium: DER.3.1 Audits und Revisionen

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->