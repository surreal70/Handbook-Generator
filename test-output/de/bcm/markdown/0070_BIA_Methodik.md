# Business Impact Analysis (BIA) – Methodik

**Dokument-ID:** BCM-0070
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



## 1. Zweck und Output

### 1.1 Ziele der BIA

Die Business Impact Analysis (BIA) der AdminSend GmbH verfolgt folgende Ziele:

- **Identifikation kritischer Geschäftsprozesse:** Ermittlung der geschäftskritischen Prozesse und Services
- **Quantifizierung von Auswirkungen:** Bewertung der finanziellen, operativen und reputationsbezogenen Auswirkungen von Ausfällen
- **Festlegung von Zielwerten:** Definition von RTO (Recovery Time Objective) und RPO (Recovery Point Objective)
- **Priorisierung:** Festlegung der Wiederherstellungspriorisierung
- **Ressourcenplanung:** Ermittlung des Ressourcenbedarfs für Business Continuity

### 1.2 Erwartete Ergebnisse

Die BIA liefert folgende Ergebnisse:

**RTO (Recovery Time Objective):**
- Maximale tolerierbare Ausfallzeit für jeden kritischen Prozess
- Zeitpunkt, bis zu dem ein Prozess wiederhergestellt sein muss

**RPO (Recovery Point Objective):**
- Maximaler tolerierbarer Datenverlust
- Zeitpunkt, bis zu dem Daten wiederhergestellt werden müssen

**MTPD (Maximum Tolerable Period of Disruption):**
- Maximale Zeitspanne, die ein Prozess ausfallen kann, bevor irreparable Schäden entstehen
- Auch: MAO (Maximum Acceptable Outage)

**Priorisierung:**
- Reihenfolge der Wiederherstellung von Prozessen und Systemen
- Abhängigkeiten zwischen Prozessen

**Ressourcenbedarf:**
- Personal, Räumlichkeiten, IT-Systeme, Daten, Lieferanten
- Mindestressourcen für Notbetrieb

## 2. Vorgehen und Methodik

### 2.1 BIA-Prozess

```
┌─────────────────┐
│ 1. Vorbereitung │
│ - Scope          │
│ - Stakeholder    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Datenerhebung│
│ - Workshops      │
│ - Interviews     │
│ - Fragebögen     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Analyse      │
│ - Bewertung      │
│ - Abhängigkeiten │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. RTO/RPO      │
│ - Festlegung     │
│ - Validierung    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. Dokumentation│
│ - Bericht        │
│ - Präsentation   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 6. Freigabe     │
│ - Review         │
│ - Genehmigung    │
└─────────────────┘
```

### 2.2 Workshops und Interviews

**Zielgruppe:**
- Fachbereichsleiter und Prozessverantwortliche
- IT-Verantwortliche
- Schlüsselpersonen mit Spezialwissen

**Format:**
- **Workshops:** Gruppenformat für übergreifende Themen (2-4 Stunden)
- **Interviews:** Einzelgespräche für detaillierte Prozessanalyse (1-2 Stunden)
- **Fragebögen:** Standardisierte Erhebung für weniger kritische Prozesse

**Durchführung:**
[TODO: Definieren Sie Workshop-/Interview-Plan]

**Beispiel-Zeitplan:**
| Woche | Aktivität | Teilnehmer | Verantwortlich |
|-------|-----------|------------|----------------|
| 1 | Kick-off Workshop | Alle Bereichsleiter | BCM-Manager |
| 2-3 | Einzelinterviews Fachbereiche | Prozessverantwortliche | BCM-Manager |
| 4 | IT-Workshop | IT-Team | BCM-Manager + [TODO] |
| 5 | Konsolidierung und Analyse | BCM-Team | BCM-Manager |
| 6 | Ergebnispräsentation | Management | BCM-Manager |

### 2.3 Datenquellen

**Primäre Datenquellen:**
- Workshops und Interviews mit Fachbereichen
- Bestehende Prozessdokumentation
- IT-Service-Katalog und CMDB
- Finanzberichte und Umsatzdaten

**Sekundäre Datenquellen:**
- Vertragsdokumente und SLAs
- Compliance-Anforderungen
- Historische Vorfallsdaten
- Benchmarks und Best Practices

### 2.4 Review- und Validierungsschritte

**Validierung durch Fachbereiche:**
1. Entwurf der BIA-Ergebnisse wird an Prozessverantwortliche gesendet
2. Fachbereiche prüfen und kommentieren innerhalb von [TODO: X] Tagen
3. Feedback wird eingearbeitet

**Management-Review:**
1. Konsolidierte BIA-Ergebnisse werden dem Management präsentiert
2. RTO/RPO-Werte werden diskutiert und validiert
3. Priorisierung wird festgelegt

**Formale Freigabe:**
- Genehmigung durch [TODO] (CEO)
- Bestätigung durch Fachbereichsleiter
- Dokumentation der Freigabe

## 3. Bewertungsdimensionen

### 3.1 Finanzielle Auswirkungen

**Direkte finanzielle Verluste:**
- Umsatzverlust pro Stunde/Tag
- Vertragsstrafen und Schadensersatzforderungen
- Zusätzliche Kosten für Notfallmaßnahmen

**Bewertungsskala:**
[TODO: Definieren Sie Ihre Bewertungsskala]

**Beispiel:**
| Stufe | Beschreibung | Umsatzverlust pro Tag |
|-------|--------------|----------------------|
| 5 - Kritisch | Existenzbedrohend | > 500.000 € |
| 4 - Sehr hoch | Massive Auswirkungen | 100.000 - 500.000 € |
| 3 - Hoch | Erhebliche Auswirkungen | 50.000 - 100.000 € |
| 2 - Mittel | Spürbare Auswirkungen | 10.000 - 50.000 € |
| 1 - Niedrig | Geringe Auswirkungen | < 10.000 € |

### 3.2 Operative Auswirkungen

**Beeinträchtigung des Geschäftsbetriebs:**
- Durchsatz und Produktionskapazität
- Rückstau und Nacharbeitsaufwand
- Qualitätsprobleme
- Beeinträchtigung anderer Prozesse

**Bewertungsskala:**
| Stufe | Beschreibung | Operative Auswirkung |
|-------|--------------|---------------------|
| 5 - Kritisch | Kompletter Stillstand | Alle Prozesse betroffen |
| 4 - Sehr hoch | Massive Beeinträchtigung | Mehrere kritische Prozesse betroffen |
| 3 - Hoch | Erhebliche Beeinträchtigung | Ein kritischer Prozess betroffen |
| 2 - Mittel | Spürbare Beeinträchtigung | Verzögerungen, aber Betrieb möglich |
| 1 - Niedrig | Geringe Beeinträchtigung | Keine wesentliche Auswirkung |

### 3.3 Rechtliche und regulatorische Auswirkungen

**Compliance-Risiken:**
- Gesetzliche Verpflichtungen (z.B. DSGVO, Arbeitsschutz)
- Vertragliche Verpflichtungen (SLAs, Lieferverträge)
- Meldepflichten gegenüber Behörden
- Haftungsrisiken

**Bewertungsskala:**
| Stufe | Beschreibung | Rechtliche Auswirkung |
|-------|--------------|----------------------|
| 5 - Kritisch | Schwerer Gesetzesverstoß | Strafverfahren, Lizenzverlust |
| 4 - Sehr hoch | Erheblicher Verstoß | Bußgelder > 100.000 € |
| 3 - Hoch | Verstoß | Bußgelder 10.000 - 100.000 € |
| 2 - Mittel | Vertragsverletzung | Vertragsstrafen |
| 1 - Niedrig | Keine Verpflichtung | Keine rechtlichen Folgen |

### 3.4 Sicherheitsauswirkungen

**Gefährdung von Personen und Anlagen:**
- Personensicherheit (Mitarbeiter, Kunden, Besucher)
- Umweltgefährdung
- Anlagensicherheit
- Datensicherheit

**Bewertungsskala:**
| Stufe | Beschreibung | Sicherheitsauswirkung |
|-------|--------------|----------------------|
| 5 - Kritisch | Lebensgefahr | Todesfälle oder schwere Verletzungen |
| 4 - Sehr hoch | Erhebliche Gefährdung | Verletzungen, Umweltschäden |
| 3 - Hoch | Gefährdung | Gesundheitsrisiken |
| 2 - Mittel | Geringe Gefährdung | Sachschäden |
| 1 - Niedrig | Keine Gefährdung | Keine Sicherheitsrisiken |

### 3.5 Reputationsauswirkungen

**Image und Vertrauen:**
- Kundenvertrauen und Kundenzufriedenheit
- Markenimage und öffentliche Wahrnehmung
- Vertrauen von Partnern und Investoren
- Medienberichterstattung

**Bewertungsskala:**
| Stufe | Beschreibung | Reputationsauswirkung |
|-------|--------------|----------------------|
| 5 - Kritisch | Irreparabler Schaden | Massive negative Medienberichterstattung, Kundenabwanderung |
| 4 - Sehr hoch | Schwerer Schaden | Nationale Medienberichterstattung, erheblicher Vertrauensverlust |
| 3 - Hoch | Erheblicher Schaden | Regionale Medienberichterstattung, Kundenbeschwerden |
| 2 - Mittel | Spürbarer Schaden | Social Media Kritik, einzelne Beschwerden |
| 1 - Niedrig | Geringer Schaden | Keine öffentliche Wahrnehmung |

## 4. Zeitabhängigkeit der Auswirkungen

### 4.1 Zeitfenster-Analyse

Die Auswirkungen von Prozessausfällen werden für verschiedene Zeitfenster bewertet:

**Zeitfenster:**
- **0-4 Stunden:** Sofortige Auswirkungen
- **4-24 Stunden:** Kurzfristige Auswirkungen
- **1-3 Tage:** Mittelfristige Auswirkungen
- **> 3 Tage:** Langfristige Auswirkungen

### 4.2 Impact-Progression

[TODO: Dokumentieren Sie die zeitabhängige Entwicklung der Auswirkungen]

**Beispiel für Prozess "Auftragsabwicklung":**

| Zeitfenster | Finanzielle Auswirkung | Operative Auswirkung | Reputationsauswirkung |
|-------------|----------------------|---------------------|----------------------|
| 0-4h | Gering (Stufe 1) | Mittel (Stufe 2) | Niedrig (Stufe 1) |
| 4-24h | Mittel (Stufe 2) | Hoch (Stufe 3) | Mittel (Stufe 2) |
| 1-3d | Hoch (Stufe 3) | Sehr hoch (Stufe 4) | Hoch (Stufe 3) |
| > 3d | Kritisch (Stufe 5) | Kritisch (Stufe 5) | Sehr hoch (Stufe 4) |

### 4.3 MTPD-Bestimmung

**Maximum Tolerable Period of Disruption (MTPD):**

Der MTPD ist der Zeitpunkt, ab dem die Auswirkungen eines Ausfalls inakzeptabel werden.

**Bestimmung:**
- MTPD = Zeitpunkt, ab dem Auswirkungen Stufe 4 oder 5 erreichen
- Oder: Zeitpunkt, ab dem mehrere Dimensionen Stufe 3 erreichen

**Beispiel:**
- Prozess "Auftragsabwicklung": MTPD = 24 Stunden (ab dann Stufe 4/5)
- Prozess "E-Mail": MTPD = 4 Stunden (ab dann Stufe 3 in mehreren Dimensionen)

## 5. RTO/RPO-Festlegung

### 5.1 RTO-Bestimmung

**Recovery Time Objective (RTO):**
- RTO muss deutlich unter MTPD liegen (Sicherheitspuffer)
- Empfehlung: RTO = 50-70% des MTPD

**Beispiel:**
- MTPD = 24 Stunden → RTO = 12-16 Stunden
- MTPD = 4 Stunden → RTO = 2-3 Stunden

### 5.2 RPO-Bestimmung

**Recovery Point Objective (RPO):**
- Maximaler tolerierbarer Datenverlust
- Abhängig von Datenänderungsrate und Geschäftskritikalität

**Beispiel:**
- Transaktionsdaten: RPO = 15 Minuten (kontinuierliche Replikation)
- Konfigurationsdaten: RPO = 24 Stunden (tägliches Backup)
- Archivdaten: RPO = 7 Tage (wöchentliches Backup)

## 6. Ergebnisfreigabe

### 6.1 Verantwortliche für Abnahme

**Fachbereichsebene:**
- Prozessverantwortliche bestätigen BIA-Ergebnisse für ihre Prozesse
- Validierung der RTO/RPO-Werte

**Management-Ebene:**
- [TODO] (CEO) genehmigt Gesamt-BIA
- [TODO] (CIO) genehmigt IT-bezogene RTO/RPO
- Fachbereichsleiter genehmigen ihre Bereiche

### 6.2 Freigabeprozess

1. **Entwurf:** BCM-Manager erstellt BIA-Bericht
2. **Fachbereichs-Review:** Prozessverantwortliche prüfen (2 Wochen)
3. **Überarbeitung:** Feedback wird eingearbeitet
4. **Management-Präsentation:** Vorstellung der Ergebnisse
5. **Formale Freigabe:** Unterschriften der Verantwortlichen
6. **Veröffentlichung:** BIA-Ergebnisse werden kommuniziert


