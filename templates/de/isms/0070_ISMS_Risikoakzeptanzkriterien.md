# Risikokriterien und Risikoakzeptanz

**Dokument-ID:** 0070
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
This document defines risk acceptance criteria and the process for accepting risks.
It establishes thresholds for acceptable risk levels and defines who can accept
risks at different levels.
-->

## 1. Risikoappetit und Toleranz

### 1.1 Risikoappetit

Die **{{ meta-organisation.name }}** definiert ihren Risikoappetit wie folgt:

**Allgemeiner Risikoappetit:** [TODO: Konservativ / Moderat / Progressiv]

**Toleranzschwellen nach Risikostufe:**

| Risikostufe | Risikoscore | Akzeptabel | Behandlung erforderlich |
|-------------|-------------|------------|-------------------------|
| Sehr niedrig | 1-2 | Ja | Monitoring |
| Niedrig | 3-6 | Ja | Monitoring |
| Mittel | 7-12 | Bedingt | Risikobehandlung empfohlen |
| Hoch | 13-20 | Nein | Risikobehandlung erforderlich |
| Sehr hoch | 21-25 | Nein | Sofortige Risikobehandlung |

### 1.2 Akzeptanzkriterien

**Automatisch akzeptabel:**
- Risikoscore ≤ 6 (Niedrig)
- Keine Compliance-Verstöße
- Keine kritischen Assets betroffen

**Bedingt akzeptabel:**
- Risikoscore 7-12 (Mittel)
- Mit Kompensationsmaßnahmen
- Zeitlich befristet (max. 12 Monate)

**Nicht akzeptabel:**
- Risikoscore ≥ 13 (Hoch/Sehr hoch)
- Compliance-Verstöße
- Kritische Assets ohne Schutzmaßnahmen

## 2. Bewertungsdimensionen

### 2.1 CIA-Triade

**Vertraulichkeit (Confidentiality):**
- Schutz vor unbefugter Offenlegung
- Klassifizierung: Öffentlich, Intern, Vertraulich, Streng vertraulich

**Integrität (Integrity):**
- Schutz vor unbefugter Änderung
- Korrektheit und Vollständigkeit von Informationen

**Verfügbarkeit (Availability):**
- Sicherstellung des Zugriffs bei Bedarf
- RTO/RPO-Anforderungen

### 2.2 Weitere Dimensionen

**Recht und Regulatorik:**
- DSGVO-Compliance
- Branchenspezifische Regulierung
- Vertragliche Verpflichtungen

**Reputation:**
- Auswirkungen auf Unternehmensimage
- Kundenvertrauen
- Medienberichterstattung

## 3. Akzeptanzprozess

### 3.1 Akzeptanzbefugnisse

| Risikostufe | Akzeptanz durch | Dokumentation | Genehmigung |
|-------------|-----------------|---------------|-------------|
| Sehr niedrig / Niedrig | CISO | Risikoregister | CISO |
| Mittel | CISO | Risikoregister + Begründung | CISO + CIO |
| Hoch | Geschäftsführung | Risikoregister + Formale Risikoakzeptanz | Geschäftsführung |
| Sehr hoch | Geschäftsführung | Risikoregister + Formale Risikoakzeptanz + Maßnahmenplan | Geschäftsführung |

### 3.2 Dokumentationspflicht

**Mindestangaben:**
- Risiko-ID und Beschreibung
- Risikobewertung (Wahrscheinlichkeit, Auswirkung, Score)
- Begründung für Akzeptanz
- Kompensationsmaßnahmen (falls vorhanden)
- Akzeptanzdatum und Gültigkeitsdauer
- Akzeptierende Person

**Dokument:** Siehe `0080_ISMS_Risikoregister_Template.md`

### 3.3 Laufzeit von Akzeptanzen

**Befristung:**
- Niedrige Risiken: Unbefristet (mit jährlichem Review)
- Mittlere Risiken: Max. 12 Monate
- Hohe Risiken: Max. 6 Monate
- Sehr hohe Risiken: Max. 3 Monate (Ausnahme)

**Verlängerung:**
- Erfordert erneute Bewertung und Genehmigung
- Begründung für Verlängerung erforderlich

### 3.4 Review von akzeptierten Risiken

**Regelmäßiger Review:**
- Quartalsweise: Alle akzeptierten Risiken
- Jährlich: Vollständige Neubewertung

**Trigger für außerplanmäßigen Review:**
- Neue Bedrohungen oder Schwachstellen
- Änderung der Geschäftsumgebung
- Security Incidents
- Audit-Findings

## 4. Referenzen

### Interne Dokumente
- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management Methodology
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0090_ISMS_Risikobehandlungsplan_RTP_Template.md` - Risk Treatment Plan

### Externe Standards
- **ISO/IEC 27001:2022** - Clause 6.1.2: Information security risk assessment
- **ISO/IEC 27005:2022** - Information security risk management

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }}

