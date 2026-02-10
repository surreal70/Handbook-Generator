# Datenminimierung

**Dokument-ID:** 0120  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
Dieses Template dokumentiert den Grundsatz der Datenminimierung gemäß Art. 5 Abs. 1 lit. c DSGVO.

Anpassung erforderlich:
- Definiere Erforderlichkeitskriterien für Datenerhebung
- Dokumentiere Prozesse zur Prüfung der Datenminimierung
- Beschreibe Maßnahmen zur Reduzierung von Datenerhebung
- Implementiere Privacy by Design Prinzipien

Referenz: DSGVO Art. 5 Abs. 1 lit. c (Datenminimierung)
-->

## Zweck

Dieses Dokument beschreibt die Umsetzung des Grundsatzes der Datenminimierung in der {{ meta.organization }}. Es dürfen nur die personenbezogenen Daten erhoben werden, die für den jeweiligen Zweck tatsächlich erforderlich sind.

## Grundsatz gemäß Art. 5 Abs. 1 lit. c DSGVO

**Rechtliche Anforderung:**  
Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für die Zwecke der Verarbeitung notwendige Maß beschränkt sein.

### Drei Kriterien

1. **Angemessen:** Daten müssen in einem vernünftigen Verhältnis zum Zweck stehen
2. **Erheblich:** Daten müssen für den Zweck relevant sein
3. **Auf das Notwendige beschränkt:** Nur die minimal erforderlichen Daten erheben

## Erforderlichkeitsprüfung

### Prüfprozess für Datenerhebung

**Vor jeder Datenerhebung prüfen:**

1. **Ist die Datenerhebung für den Zweck erforderlich?**
   - Kann der Zweck ohne diese Daten erreicht werden?
   - Gibt es mildere Mittel?
   - Ist die Datenerhebung verhältnismäßig?

2. **Welche Daten sind minimal erforderlich?**
   - Welche Daten sind zwingend notwendig?
   - Welche Daten sind "nice-to-have" (zu vermeiden)?
   - Können Daten anonymisiert oder pseudonymisiert werden?

3. **Dokumentation der Erforderlichkeit**
   - Begründung im Verzeichnis von Verarbeitungstätigkeiten
   - Nachweis der Erforderlichkeitsprüfung
   - Regelmäßige Überprüfung

### Erforderlichkeitsmatrix

| Datenart | Zweck | Erforderlich? | Begründung | Alternative |
|----------|-------|---------------|------------|-------------|
| [TODO: Name] | [TODO: Vertragserfüllung] | Ja | [TODO: Identifikation] | Keine |
| [TODO: Geburtsdatum] | [TODO: Newsletter] | Nein | [TODO: Nicht erforderlich] | Weglassen |
| [TODO: Adresse] | [TODO: Lieferung] | Ja | [TODO: Zustellung] | Packstation |
| [TODO: Telefon] | [TODO: Kontakt] | Teilweise | [TODO: Alternative E-Mail] | E-Mail |

## Umsetzung in unserer Organisation

### Datenerhebung nach Kategorien

**Pflichtangaben vs. freiwillige Angaben:**

| Verarbeitungszweck | Pflichtangaben | Freiwillige Angaben | Nicht erforderlich |
|-------------------|----------------|---------------------|-------------------|
| [TODO: Bestellung] | [TODO: Name, Adresse, Zahlung] | [TODO: Telefon] | [TODO: Geburtsdatum] |
| [TODO: Newsletter] | [TODO: E-Mail] | [TODO: Name] | [TODO: Adresse] |
| [TODO: Kundenkonto] | [TODO: E-Mail, Passwort] | [TODO: Profilbild] | [TODO: Soziale Medien] |

**Kennzeichnung in Formularen:**
- Pflichtfelder mit * markieren
- Freiwillige Felder klar kennzeichnen
- Erklärung, warum Daten benötigt werden

### Maßnahmen zur Datenminimierung

| Maßnahme | Beschreibung | Verantwortlich | Status |
|----------|--------------|----------------|--------|
| [TODO: Erforderlichkeitsprüfung] | Prüfung vor neuen Verarbeitungen | DSB | [TODO] |
| [TODO: Formularoptimierung] | Reduzierung von Eingabefeldern | IT | [TODO] |
| [TODO: Anonymisierung] | Wo möglich anonyme Daten nutzen | IT | [TODO] |
| [TODO: Pseudonymisierung] | Pseudonyme statt Klardaten | IT | [TODO] |

## Technische Umsetzung

### Privacy by Design (Art. 25)

**Datenminimierung durch Technikgestaltung:**

- [TODO: Formulare nur mit erforderlichen Feldern]
- [TODO: Optionale Felder klar gekennzeichnet]
- [TODO: Automatische Anonymisierung nach Zweckerfüllung]
- [TODO: Pseudonymisierung sensibler Daten]
- [TODO: Aggregation statt Einzeldaten für Statistiken]

### Anonymisierung und Pseudonymisierung

**Anonymisierung:**
- Vollständige Entfernung des Personenbezugs
- Keine Rückführbarkeit auf Personen
- Keine DSGVO-Anwendung mehr

**Pseudonymisierung:**
- Trennung von Identifikationsdaten und Inhaltsdaten
- Rückführbarkeit nur mit Zusatzinformation
- Weiterhin DSGVO-Anwendung, aber geringeres Risiko

**Anwendungsfälle:**

| Zweck | Methode | Beispiel |
|-------|---------|----------|
| [TODO: Statistik] | Anonymisierung | Aggregierte Nutzungsdaten |
| [TODO: Analyse] | Pseudonymisierung | Nutzer-ID statt Name |
| [TODO: Forschung] | Anonymisierung | Entfernung aller Identifikatoren |
| [TODO: Backup] | Pseudonymisierung | Verschlüsselte Personendaten |

## Vermeidung übermäßiger Datenerhebung

### Häufige Fehler

| Fehler | Beispiel | Korrektur |
|--------|----------|-----------|
| "Nice-to-have" Daten | Geburtsdatum für Newsletter | Nur E-Mail erheben |
| Übermäßige Profilbildung | Tracking aller Aktivitäten | Nur notwendiges Tracking |
| Vorratsdatenspeicherung | "Könnte mal nützlich sein" | Nur bei konkretem Zweck |
| Fehlende Differenzierung | Alle Daten als Pflicht | Pflicht vs. freiwillig trennen |

### Checkliste gegen übermäßige Datenerhebung

- [ ] Jedes Datenfeld hat einen dokumentierten Zweck
- [ ] Keine "nice-to-have" Datenfelder
- [ ] Pflicht- und freiwillige Felder getrennt
- [ ] Anonymisierung/Pseudonymisierung geprüft
- [ ] Keine Vorratsdatenspeicherung
- [ ] Regelmäßige Überprüfung der Erforderlichkeit
- [ ] Mitarbeiter geschult zu Datenminimierung

## Regelmäßige Überprüfung

### Datenbestandsprüfung

**Quartalsweise prüfen:**

1. **Welche Daten werden erhoben?**
   - Inventarisierung aller Datenfelder
   - Zuordnung zu Verarbeitungszwecken

2. **Sind alle Daten noch erforderlich?**
   - Erforderlichkeitsprüfung für bestehende Daten
   - Identifikation überflüssiger Daten

3. **Können Daten reduziert werden?**
   - Möglichkeiten zur Anonymisierung
   - Möglichkeiten zur Pseudonymisierung
   - Löschung nicht mehr erforderlicher Daten

### Kontrollen

| Kontrolle | Frequenz | Verantwortlich | Dokumentation |
|-----------|----------|----------------|---------------|
| Erforderlichkeitsprüfung | Bei neuen Verarbeitungen | DSB | Prüfprotokoll |
| Datenbestandsprüfung | Quartalsweise | DSB | Inventarliste |
| Formularprüfung | Jährlich | IT/DSB | Prüfbericht |
| Anonymisierungspotenzial | Jährlich | IT | Analysebericht |

## Dokumentation

### Nachweispflichten

**Für jede Verarbeitung dokumentieren:**
- Welche Daten werden erhoben?
- Warum ist jede Datenart erforderlich?
- Wurden Alternativen geprüft (Anonymisierung, Pseudonymisierung)?
- Wie wird die Erforderlichkeit regelmäßig überprüft?

### Verzeichnis von Verarbeitungstätigkeiten (Art. 30)

**Dokumentation der Datenminimierung:**
- Kategorien personenbezogener Daten
- Begründung der Erforderlichkeit
- Maßnahmen zur Minimierung
- Anonymisierung/Pseudonymisierung

## Verknüpfung zu anderen Dokumenten

- **Datenschutzgrundsätze (Art. 5):** Datenminimierung als Grundprinzip
- **Zweckbindung (Art. 5 Abs. 1 lit. b):** Zweckbezogene Erforderlichkeit
- **Privacy by Design (Art. 25):** Technische Umsetzung
- **Verzeichnis (Art. 30):** Dokumentation der Datenarten
- **Informationspflichten (Art. 13-14):** Information über erhobene Daten

## Häufige Verstöße und deren Vermeidung

| Verstoß | Beispiel | Vermeidung |
|---------|----------|------------|
| Übermäßige Datenerhebung | Alle Daten "für alle Fälle" | Erforderlichkeitsprüfung |
| Fehlende Differenzierung | Alle Felder als Pflicht | Pflicht vs. freiwillig |
| Vorratsdatenspeicherung | Daten ohne konkreten Zweck | Zweckbindung beachten |
| Keine Anonymisierung | Klardaten wo nicht nötig | Anonymisierung prüfen |

---

**Nächste Schritte:**
1. Führen Sie Erforderlichkeitsprüfung für alle Datenerhebungen durch
2. Optimieren Sie Formulare und reduzieren Sie Datenfelder
3. Implementieren Sie Anonymisierung und Pseudonymisierung
4. Schulen Sie Mitarbeiter zu Datenminimierung
5. Etablieren Sie regelmäßige Datenbestandsprüfungen

