# Post-Breach Review Template

**Dokument-ID:** 0640  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Template  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
Dieses Template dient der strukturierten Nachbereitung einer Datenschutzverletzung.
Es hilft, Lessons Learned zu identifizieren und Verbesserungsmaßnahmen abzuleiten.

Anpassung erforderlich:
- Führe das Review innerhalb 2 Wochen nach Incident-Closure durch
- Beziehe alle relevanten Stakeholder ein
- Dokumentiere ehrlich und konstruktiv
- Leite konkrete Maßnahmen ab
- Verfolge Umsetzung der Maßnahmen

Referenz: Best Practice für Incident Management
-->

## Post-Breach Review

**Breach-ID:** [TODO: BREACH-YYYY-NNN]  
**Review-Datum:** [TODO: YYYY-MM-DD]  
**Moderator:** [TODO: Name]  

### Teilnehmer

| Name | Rolle | Abteilung |
|------|-------|-----------|
| [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] |

---

## 1. Incident-Zusammenfassung

**Kurzbeschreibung:**  
[TODO: 2-3 Sätze zur Beschreibung des Vorfalls]

**Zeitraum:**  
- Beginn: [TODO: YYYY-MM-DD HH:MM]
- Entdeckung: [TODO: YYYY-MM-DD HH:MM]
- Abschluss: [TODO: YYYY-MM-DD HH:MM]
- Gesamtdauer: [TODO: X Stunden/Tage]

**Betroffene:**  
- Anzahl Personen: [TODO]
- Datenkategorien: [TODO]
- Risikostufe: [TODO: Niedrig/Mittel/Hoch]

---

## 2. Timeline-Analyse

| Zeitpunkt | Ereignis | Verantwortlich | Dauer bis nächstem Schritt |
|-----------|----------|----------------|----------------------------|
| [TODO: HH:MM] | Vorfall tritt ein | - | - |
| [TODO: HH:MM] | Entdeckung | [TODO] | [TODO: X Min/Std] |
| [TODO: HH:MM] | Erste Meldung | [TODO] | [TODO: X Min/Std] |
| [TODO: HH:MM] | Team aktiviert | [TODO] | [TODO: X Min/Std] |
| [TODO: HH:MM] | Eindämmung | [TODO] | [TODO: X Min/Std] |
| [TODO: HH:MM] | Meldung Behörde | [TODO] | [TODO: X Std] |
| [TODO: HH:MM] | Benachrichtigung Betroffene | [TODO] | [TODO: X Std] |
| [TODO: HH:MM] | Incident geschlossen | [TODO] | - |

**Analyse:**  
[TODO: Waren die Reaktionszeiten angemessen? Wo gab es Verzögerungen?]

---

## 3. Was lief gut? (Positives)

### 3.1 Erkennung und Meldung

**Positive Aspekte:**
- [TODO: z.B. Schnelle Erkennung durch Monitoring]
- [TODO: z.B. Klare Meldewege funktionierten]

### 3.2 Response und Eindämmung

**Positive Aspekte:**
- [TODO: z.B. Team war gut vorbereitet]
- [TODO: z.B. Technische Maßnahmen griffen schnell]

### 3.3 Kommunikation

**Positive Aspekte:**
- [TODO: z.B. Klare interne Kommunikation]
- [TODO: z.B. Professionelle externe Kommunikation]

### 3.4 Dokumentation

**Positive Aspekte:**
- [TODO: z.B. Vollständige Dokumentation]
- [TODO: z.B. Breach-Register aktuell]

---

## 4. Was lief schlecht? (Verbesserungsbedarf)

### 4.1 Erkennung und Meldung

**Probleme:**
- [TODO: z.B. Verzögerte Erkennung]
- [TODO: z.B. Unklare Meldewege]

**Ursachen:**
- [TODO: Warum traten diese Probleme auf?]

### 4.2 Response und Eindämmung

**Probleme:**
- [TODO: z.B. Verzögerte Reaktion]
- [TODO: z.B. Fehlende Tools]

**Ursachen:**
- [TODO: Warum traten diese Probleme auf?]

### 4.3 Kommunikation

**Probleme:**
- [TODO: z.B. Verzögerte Benachrichtigung]
- [TODO: z.B. Unklare Botschaften]

**Ursachen:**
- [TODO: Warum traten diese Probleme auf?]

### 4.4 Dokumentation

**Probleme:**
- [TODO: z.B. Lückenhafte Dokumentation]
- [TODO: z.B. Fehlende Templates]

**Ursachen:**
- [TODO: Warum traten diese Probleme auf?]

---

## 5. Root Cause Analysis

**Primäre Ursache:**  
[TODO: Was war die Hauptursache des Vorfalls?]

**Beitragende Faktoren:**
- [TODO: Faktor 1]
- [TODO: Faktor 2]
- [TODO: Faktor 3]

**5-Why-Analyse:**

1. Warum trat der Vorfall auf?  
   [TODO: Antwort]

2. Warum [Antwort aus 1]?  
   [TODO: Antwort]

3. Warum [Antwort aus 2]?  
   [TODO: Antwort]

4. Warum [Antwort aus 3]?  
   [TODO: Antwort]

5. Warum [Antwort aus 4]?  
   [TODO: Root Cause]

---

## 6. Lessons Learned

### 6.1 Technische Erkenntnisse

- [TODO: z.B. Monitoring-Lücken identifiziert]
- [TODO: z.B. Sicherheitskonfiguration unzureichend]

### 6.2 Prozessuale Erkenntnisse

- [TODO: z.B. Response-Plan muss aktualisiert werden]
- [TODO: z.B. Eskalationswege unklar]

### 6.3 Organisatorische Erkenntnisse

- [TODO: z.B. Schulungsbedarf identifiziert]
- [TODO: z.B. Rollen müssen klarer definiert werden]

### 6.4 Kommunikative Erkenntnisse

- [TODO: z.B. Templates müssen verbessert werden]
- [TODO: z.B. Kommunikationswege optimieren]

---

## 7. Verbesserungsmaßnahmen

### 7.1 Sofortmaßnahmen (innerhalb 1 Monat)

| Maßnahme | Verantwortlich | Frist | Priorität | Status |
|----------|----------------|-------|-----------|--------|
| [TODO: z.B. Monitoring erweitern] | [TODO] | [TODO: YYYY-MM-DD] | Hoch | [ ] Offen |
| [TODO: z.B. Response-Plan aktualisieren] | [TODO] | [TODO: YYYY-MM-DD] | Hoch | [ ] Offen |

### 7.2 Mittelfristige Maßnahmen (1-3 Monate)

| Maßnahme | Verantwortlich | Frist | Priorität | Status |
|----------|----------------|-------|-----------|--------|
| [TODO: z.B. Schulungen durchführen] | [TODO] | [TODO: YYYY-MM-DD] | Mittel | [ ] Offen |
| [TODO: z.B. Prozesse dokumentieren] | [TODO] | [TODO: YYYY-MM-DD] | Mittel | [ ] Offen |

### 7.3 Langfristige Maßnahmen (3-12 Monate)

| Maßnahme | Verantwortlich | Frist | Priorität | Status |
|----------|----------------|-------|-----------|--------|
| [TODO: z.B. Neue Tools implementieren] | [TODO] | [TODO: YYYY-MM-DD] | Niedrig | [ ] Offen |
| [TODO: z.B. Organisationsstruktur anpassen] | [TODO] | [TODO: YYYY-MM-DD] | Niedrig | [ ] Offen |

---

## 8. Kosten-Nutzen-Analyse

### 8.1 Kosten des Vorfalls

| Kostenart | Betrag (EUR) |
|-----------|--------------|
| Direkte Kosten (Forensik, externe Berater) | [TODO] |
| Personalkosten (Arbeitszeit) | [TODO] |
| Meldungen und Benachrichtigungen | [TODO] |
| Reputationsschaden (geschätzt) | [TODO] |
| **Gesamt** | **[TODO]** |

### 8.2 Kosten der Verbesserungsmaßnahmen

| Maßnahme | Geschätzte Kosten (EUR) |
|----------|-------------------------|
| [TODO: Maßnahme 1] | [TODO] |
| [TODO: Maßnahme 2] | [TODO] |
| **Gesamt** | **[TODO]** |

### 8.3 Erwarteter Nutzen

[TODO: Beschreibe den erwarteten Nutzen der Maßnahmen, z.B. Risikoreduktion, schnellere Response-Zeiten]

---

## 9. Response-Plan-Anpassungen

**Erforderliche Änderungen am Response-Plan:**

| Abschnitt | Änderung | Begründung |
|-----------|----------|------------|
| [TODO: z.B. Kontakte] | [TODO: z.B. Neue Kontakte ergänzen] | [TODO] |
| [TODO: z.B. Eskalation] | [TODO: z.B. Schwellenwerte anpassen] | [TODO] |

---

## 10. Schulungs- und Awareness-Bedarf

**Identifizierter Schulungsbedarf:**

| Zielgruppe | Thema | Format | Zeitrahmen |
|------------|-------|--------|------------|
| [TODO: z.B. IT-Team] | [TODO: z.B. Incident Response] | [TODO: Workshop] | [TODO: Q2 2024] |
| [TODO: z.B. Alle MA] | [TODO: z.B. Data Breach Awareness] | [TODO: E-Learning] | [TODO: Q2 2024] |

---

## 11. Follow-up und Monitoring

**Nächste Schritte:**

| Aktion | Verantwortlich | Frist |
|--------|----------------|-------|
| Maßnahmenplan erstellen | [TODO] | [TODO: YYYY-MM-DD] |
| Monatliches Review-Meeting | [TODO] | [TODO: Jeden 1. Montag] |
| Fortschrittsbericht an Geschäftsführung | [TODO] | [TODO: YYYY-MM-DD] |
| Follow-up Review (3 Monate) | [TODO] | [TODO: YYYY-MM-DD] |

---

## 12. Abschluss und Freigabe

**Zusammenfassung:**  
[TODO: 2-3 Sätze Zusammenfassung der wichtigsten Erkenntnisse und Maßnahmen]

**Freigabe:**

| Rolle | Name | Datum | Unterschrift |
|-------|------|-------|--------------|
| Moderator | [TODO] | [TODO] | _____________ |
| Datenschutzbeauftragter | [TODO] | [TODO] | _____________ |
| Geschäftsführung | [TODO] | [TODO] | _____________ |

---

**Anhänge:**
- [ ] Detaillierte Timeline
- [ ] Technischer Bericht
- [ ] Kommunikationsmaterialien
- [ ] Maßnahmenplan (detailliert)
