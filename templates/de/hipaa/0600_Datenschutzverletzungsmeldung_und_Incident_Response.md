# Datenschutzverletzungsmeldung und Incident Response

**Dokument-ID:** HIPAA-0600  
**Organisation:** {{ meta.organization.name }}  
**Verantwortlich:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Prüfung / Genehmigt  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Zweck

Dieses Dokument beschreibt die Verfahren zur Datenschutzverletzungsmeldung und Incident Response für {{ meta.organization.name }} gemäß der HIPAA Breach Notification Rule.

### 1.1 HIPAA-Anforderungen

**Breach Notification Rule (45 CFR §§ 164.400-164.414):**
- Definition und Bewertung von Datenschutzverletzungen
- Benachrichtigung von Einzelpersonen
- Benachrichtigung von HHS
- Benachrichtigung der Medien (500+ Einzelpersonen)
- Benachrichtigungspflichten von Business Associates

## 2. Definition von Datenschutzverletzungen

**Datenschutzverletzung:** Erwerb, Zugriff, Nutzung oder Offenlegung von PHI auf eine Weise, die nicht gemäß der Privacy Rule zulässig ist und die Sicherheit oder Privatsphäre der PHI gefährdet.

**Ausnahmen:**
- Unbeabsichtigter Erwerb/Zugriff durch Mitarbeiter in gutem Glauben
- Versehentliche Offenlegung innerhalb der Organisation
- Offenlegung, bei der Empfänger Informationen vernünftigerweise nicht behalten kann

### 2.1 Risikobewertung bei Datenschutzverletzungen

**Risikobewertungsfaktoren:**
1. Art und Umfang der beteiligten PHI
2. Unbefugte Person, die PHI verwendet/erhalten hat
3. Ob PHI tatsächlich erworben oder eingesehen wurde
4. Ausmaß, in dem das Risiko gemindert wurde

**Risikobewertungsprozess:**
1. **Vorfallidentifikation:** Potenziellen Vorfall identifizieren
2. **Vorläufige Bewertung:** Schnelle Bewertung durchführen
3. **Detaillierte Analyse:** Jeden Risikofaktor analysieren
4. **Risikostufe:** Risikostufe bestimmen (niedrig, mittel, hoch)
5. **Datenschutzverletzungsfeststellung:** Feststellen, ob Datenschutzverletzung vorliegt
6. **Dokumentation:** Bewertung dokumentieren
7. **Benachrichtigungsentscheidung:** Benachrichtigungsanforderungen bestimmen

**Risikobewertungsmatrix:**
| Faktor | Niedrig | Mittel | Hoch |
|--------|---------|--------|------|
| Art der PHI | Demografische Daten | Klinische Daten | Sensible Daten (HIV, psychische Gesundheit) |
| Umfang | 1-10 Personen | 11-499 Personen | 500+ Personen |
| Empfänger | Autorisiertes Personal | Nicht autorisiertes Personal intern | Externe unbefugte Partei |
| Erwerb | Nicht eingesehen | Möglicherweise eingesehen | Definitiv eingesehen/kopiert |
| Minderung | Vollständig gemindert | Teilweise gemindert | Nicht gemindert |

### 2.2 Dokumentation der Risikobewertung

**Erforderliche Dokumentation:**
- Datum und Zeit des Vorfalls
- Beschreibung des Vorfalls
- Betroffene PHI
- Anzahl betroffener Personen
- Analyse jedes Risikofaktors
- Datenschutzverletzungsfeststellung
- Begründung für Feststellung
- Benachrichtigungsentscheidung

**Aufbewahrung:**
- Alle Risikobewertungen für [TODO: 6 Jahre] aufbewahren
- Auch wenn keine Datenschutzverletzung festgestellt wurde

## 3. Benachrichtigung von Einzelpersonen

### 3.1 Benachrichtigungsanforderungen

**Wann Benachrichtigung erforderlich:**
- Datenschutzverletzung festgestellt
- Ungesicherte PHI betroffen
- Mehr als niedriges Risiko für Einzelperson

**Zeitrahmen:**
- Ohne unangemessene Verzögerung
- Spätestens [TODO: 60 Tage] nach Entdeckung
- Früher, wenn möglich

**Benachrichtigungsmethode:**
- **Erste Priorität:** Schriftliche Benachrichtigung per Post
- **Alternative:** E-Mail (falls Person zugestimmt hat)
- **Ersatz:** Wenn Kontaktinformationen unzureichend

### 3.2 Inhalt der Benachrichtigung an Einzelpersonen

**Erforderliche Elemente:**
1. **Beschreibung:** Kurze Beschreibung der Datenschutzverletzung
2. **Betroffene PHI:** Arten von PHI betroffen
3. **Schritte der Person:** Schritte, die Person unternehmen sollte
4. **Maßnahmen der Organisation:** Schritte zur Untersuchung und Minderung
5. **Kontaktinformationen:** Kontakt für weitere Informationen
6. **Datum:** Datum der Datenschutzverletzung (falls bekannt)

**Klare Sprache:**
- Einfache, nicht-technische Sprache
- Auf Deutsch (oder bevorzugter Sprache)
- Leicht verständlich
- Keine Rechtfertigungen oder Schuldzuweisungen

**Beispielbenachrichtigung:**
```
Betreff: Wichtige Benachrichtigung über Ihre Gesundheitsinformationen

Sehr geehrte/r [Name],

Wir schreiben Ihnen, um Sie über einen Vorfall zu informieren, der Ihre 
geschützten Gesundheitsinformationen (PHI) betreffen könnte.

Was ist passiert:
[Beschreibung des Vorfalls]

Welche Informationen waren betroffen:
[Arten von PHI]

Was wir tun:
[Maßnahmen der Organisation]

Was Sie tun sollten:
[Empfohlene Schritte]

Für weitere Informationen:
[Kontaktinformationen]

Mit freundlichen Grüßen,
[Organisation]
```

### 3.3 Benachrichtigungsmethoden

**Schriftliche Benachrichtigung (Standard):**
- Per Post an letzte bekannte Adresse
- Erstklassige Post
- Einzeln adressiert

**E-Mail-Benachrichtigung:**
- Nur wenn Person zugestimmt hat
- Sichere E-Mail bevorzugt
- Lesebestätigung anfordern

**Ersatzbenachrichtigung:**
- Wenn Kontaktinformationen unzureichend für < 10 Personen:
  - Alternative schriftliche Benachrichtigung
  - Telefonische Benachrichtigung
  - Andere verfügbare Mittel

- Wenn Kontaktinformationen unzureichend für ≥ 10 Personen:
  - Auffällige Veröffentlichung auf Website für 90 Tage
  - Benachrichtigung in großen Medien (Zeitung, Radio)

**Dringende Benachrichtigung:**
- Telefonische Benachrichtigung zusätzlich zu schriftlicher
- Wenn sofortige Maßnahmen erforderlich
- Dokumentieren Sie Anruf

### 3.4 Dokumentation der Benachrichtigung

**Erforderliche Aufzeichnungen:**
- Liste aller benachrichtigten Personen
- Datum der Benachrichtigung
- Benachrichtigungsmethode
- Kopie der Benachrichtigung
- Rücklaufpost (unzustellbar)
- Ersatzbenachrichtigungsmaßnahmen

## 4. Benachrichtigung von HHS

### 4.1 HHS-Benachrichtigungsanforderungen

**Datenschutzverletzungen mit 500+ Personen:**
- Benachrichtigung an HHS gleichzeitig mit Einzelpersonen
- Spätestens 60 Tage nach Entdeckung
- Über HHS-Website einreichen

**Datenschutzverletzungen mit < 500 Personen:**
- Jährliche Benachrichtigung an HHS
- Innerhalb von 60 Tagen nach Jahresende
- Über HHS-Website einreichen

**HHS-Einreichungsportal:**
- https://ocrportal.hhs.gov/ocr/breach/wizard_breach.jsf
- Elektronische Einreichung erforderlich
- Bestätigung aufbewahren

### 4.2 Inhalt der HHS-Benachrichtigung

**Erforderliche Informationen:**
- Name der Organisation
- Kontaktinformationen
- Datum der Datenschutzverletzung
- Datum der Entdeckung
- Anzahl betroffener Personen
- Beschreibung der Datenschutzverletzung
- Arten betroffener PHI
- Kurze Beschreibung der Untersuchung
- Minderungsmaßnahmen
- Korrekturmaßnahmen

**Zusätzliche Informationen:**
- Business Associate beteiligt (falls zutreffend)
- Strafverfolgung beteiligt (falls zutreffend)
- Medienbenachrichtigung erfolgt (falls zutreffend)

### 4.3 HHS Breach Portal

**Öffentliche Veröffentlichung:**
- HHS veröffentlicht Datenschutzverletzungen mit 500+ Personen
- "Wall of Shame"
- Öffentlich durchsuchbar
- Bleibt für 24 Monate online

**Informationen im Portal:**
- Name der Organisation
- Bundesstaat
- Anzahl betroffener Personen
- Art der Datenschutzverletzung
- Ort der Datenschutzverletzung
- Datum der Datenschutzverletzung

## 5. Medienbenachrichtigung

### 5.1 Medienbenachrichtigungsanforderungen

**Wann erforderlich:**
- Datenschutzverletzung betrifft 500+ Personen in einem Bundesstaat/Gerichtsbarkeit
- Gleichzeitig mit Benachrichtigung von Einzelpersonen
- Spätestens 60 Tage nach Entdeckung

**Medienauswahl:**
- Prominente Medien im betroffenen Bundesstaat/Gebiet
- Zeitungen, Fernsehen, Radio
- Breite Reichweite

### 5.2 Inhalt der Medienbenachrichtigung

**Erforderliche Informationen:**
- Ähnlich wie Benachrichtigung an Einzelpersonen
- Beschreibung der Datenschutzverletzung
- Arten betroffener PHI
- Schritte, die Personen unternehmen sollten
- Kontaktinformationen für weitere Informationen

**Pressemitteilung:**
- Professionell verfasst
- Faktenbasiert
- Keine Spekulationen
- Kontaktinformationen für Medienanfragen

### 5.3 Medienmanagement

**Medienstrategie:**
- Sprecher benennen
- Konsistente Botschaft
- Fakten bereitstellen
- Keine Spekulationen
- Mitgefühl zeigen

**Medienanfragen:**
- An Sprecher weiterleiten
- Konsistente Antworten
- Dokumentieren Sie Anfragen
- Keine unbefugten Aussagen

## 6. Business Associate-Benachrichtigung

### 6.1 Business Associate-Pflichten

**Wenn Business Associate Datenschutzverletzung entdeckt:**
- Covered Entity ohne unangemessene Verzögerung benachrichtigen
- Spätestens 60 Tage nach Entdeckung
- Erforderliche Informationen bereitstellen

**Benachrichtigungsinhalt:**
- Beschreibung der Datenschutzverletzung
- Betroffene PHI
- Anzahl betroffener Personen
- Datum der Datenschutzverletzung
- Datum der Entdeckung
- Untersuchungsergebnisse
- Minderungsmaßnahmen

### 6.2 Covered Entity-Verantwortlichkeiten

**Nach Erhalt der Benachrichtigung von Business Associate:**
1. **Überprüfung:** Benachrichtigung überprüfen
2. **Bewertung:** Eigene Risikobewertung durchführen
3. **Benachrichtigung:** Einzelpersonen, HHS, Medien benachrichtigen (falls erforderlich)
4. **Dokumentation:** Alle Schritte dokumentieren
5. **Überwachung:** Business Associate-Reaktion überwachen

**Business Associate Agreement:**
- Benachrichtigungspflichten spezifizieren
- Zeitrahmen festlegen
- Erforderliche Informationen definieren
- Kooperationspflichten

## 7. Incident Response-Prozess

### 7.1 Incident Response-Team

**Team-Mitglieder:**
- Privacy Officer (Leiter)
- Security Officer
- IT-Manager
- Rechtsberater
- Öffentlichkeitsarbeit/Kommunikation
- Betroffene Abteilungsleiter
- HR (falls Mitarbeiter beteiligt)

**Rollen und Verantwortlichkeiten:**
| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| Privacy Officer | Gesamtleitung, Risikobewertung, Benachrichtigungsentscheidungen |
| Security Officer | Technische Untersuchung, Eindämmung, Behebung |
| IT-Manager | Systemanalyse, Protokollüberprüfung, technische Unterstützung |
| Rechtsberater | Rechtliche Beratung, Compliance-Überprüfung |
| Öffentlichkeitsarbeit | Medienmanagement, externe Kommunikation |
| HR | Mitarbeiteruntersuchungen, Disziplinarmaßnahmen |

### 7.2 Incident Response-Phasen

**Phase 1: Erkennung und Meldung**
- Vorfall erkannt
- An Privacy Officer/Security Officer gemeldet
- Erste Dokumentation

**Phase 2: Eindämmung**
- Sofortige Maßnahmen zur Eindämmung
- Weiteren Zugriff verhindern
- Beweise sichern

**Phase 3: Bewertung**
- Umfang bestimmen
- Betroffene PHI identifizieren
- Betroffene Personen zählen
- Risikobewertung durchführen

**Phase 4: Benachrichtigung**
- Benachrichtigungsentscheidung treffen
- Benachrichtigungen vorbereiten
- Einzelpersonen benachrichtigen
- HHS benachrichtigen (falls erforderlich)
- Medien benachrichtigen (falls erforderlich)

**Phase 5: Behebung**
- Ursache beheben
- Schwachstellen schließen
- Kontrollen verbessern
- Richtlinien aktualisieren

**Phase 6: Nachbereitung**
- Incident Review durchführen
- Lessons Learned dokumentieren
- Verbesserungen umsetzen
- Schulung aktualisieren

### 7.3 Incident Response-Zeitrahmen

**Sofort (0-24 Stunden):**
- Vorfall eindämmen
- Incident Response-Team benachrichtigen
- Vorläufige Bewertung
- Beweise sichern

**Kurzfristig (1-7 Tage):**
- Detaillierte Untersuchung
- Risikobewertung abschließen
- Datenschutzverletzungsfeststellung
- Benachrichtigungsplan entwickeln

**Mittelfristig (7-60 Tage):**
- Benachrichtigungen versenden
- HHS benachrichtigen
- Medien benachrichtigen (falls erforderlich)
- Behebungsmaßnahmen umsetzen

**Langfristig (60+ Tage):**
- Nachbereitung abschließen
- Verbesserungen umsetzen
- Überwachung fortsetzen
- Dokumentation abschließen

## 8. Strafverfolgungsausnahme

### 8.1 Verzögerung der Benachrichtigung

**Wenn Strafverfolgung Verzögerung anfordert:**
- Benachrichtigung kann verzögert werden
- Schriftliche Anfrage von Strafverfolgung erforderlich
- Spezifizierter Zeitraum
- Dokumentieren Sie Anfrage

**Verzögerungszeitraum:**
- Wie von Strafverfolgung angegeben
- Normalerweise 30 Tage
- Verlängerungen möglich
- Benachrichtigung nach Ablauf

### 8.2 Zusammenarbeit mit Strafverfolgung

**Kooperationspflichten:**
- Informationen bereitstellen
- Beweise bewahren
- Untersuchung nicht behindern
- Vertraulichkeit wahren

**Dokumentation:**
- Alle Interaktionen dokumentieren
- Anfragen aufzeichnen
- Bereitgestellte Informationen verfolgen
- Verzögerungen rechtfertigen

## 9. Schulung und Sensibilisierung

### 9.1 Mitarbeiterschulung

**Schulungsthemen:**
- Datenschutzverletzungsdefinition
- Meldepflichten
- Incident Response-Verfahren
- Benachrichtigungsanforderungen
- Dokumentationspflichten

**Häufigkeit:**
- Erstschulung bei Einstellung
- Jährliche Auffrischung
- Nach Vorfällen
- Bei Richtlinienänderungen

### 9.2 Incident Response-Übungen

**Übungstypen:**
- Tischübungen (Tabletop)
- Simulationen
- Vollständige Übungen

**Häufigkeit:**
- Mindestens jährlich
- Nach größeren Änderungen
- Nach tatsächlichen Vorfällen

**Übungsdokumentation:**
- Übungsszenario
- Teilnehmer
- Beobachtungen
- Lessons Learned
- Verbesserungsmaßnahmen

## 10. Dokumentation und Aufzeichnungen

### 10.1 Erforderliche Dokumentation

**Vorfallaufzeichnungen:**
- Vorfallbeschreibung
- Entdeckungsdatum
- Risikobewertung
- Datenschutzverletzungsfeststellung
- Benachrichtigungsentscheidung
- Benachrichtigungsaufzeichnungen
- Untersuchungsergebnisse
- Behebungsmaßnahmen
- Nachbereitungsbericht

**Benachrichtigungsaufzeichnungen:**
- Benachrichtigungen an Einzelpersonen
- HHS-Einreichungen
- Medienbenachrichtigungen
- Business Associate-Benachrichtigungen
- Bestätigungen

### 10.2 Aufbewahrung

**Aufbewahrungsfrist:** [TODO: 6 Jahre ab Datum des Vorfalls]

**Speicherort:** [TODO: Incident Management-System, sicheres Repository]

### 10.3 Berichterstattung

**Interne Berichterstattung:**
- Monatliche Zusammenfassung an Führung
- Vierteljährliche Trendanalyse
- Jährlicher Bericht

**Externe Berichterstattung:**
- HHS-Benachrichtigungen
- Staatliche Meldungen (falls erforderlich)
- Versicherungsmeldungen

## 11. Kontinuierliche Verbesserung

### 11.1 Lessons Learned

**Nach jedem Vorfall:**
- Nachbesprechung durchführen
- Was gut funktioniert hat
- Was verbessert werden kann
- Ursachenanalyse
- Verbesserungsmaßnahmen

**Dokumentation:**
- Lessons Learned-Bericht
- Empfehlungen
- Umsetzungsplan
- Verantwortlichkeiten

### 11.2 Prozessverbesserungen

**Regelmäßige Überprüfung:**
- Incident Response-Verfahren
- Benachrichtigungsvorlagen
- Kontaktlisten
- Schulungsmaterialien

**Aktualisierungen:**
- Basierend auf Lessons Learned
- Regulatorische Änderungen
- Best Practices
- Technologieänderungen

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Ersterstellung |

<!-- Ende des Templates -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
