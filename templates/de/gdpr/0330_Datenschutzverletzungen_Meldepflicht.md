# Datenschutzverletzungen und Meldepflicht

**Dokument-ID:** 0330  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
Dieses Template dokumentiert den Umgang mit Datenschutzverletzungen gemäß Art. 33-34 DSGVO.
Es beschreibt Meldepflichten an Aufsichtsbehörde und betroffene Personen.

Anpassung erforderlich:
- Definiere Incident-Response-Prozess
- Erstelle Meldeverfahren für Aufsichtsbehörde (72-Stunden-Frist)
- Definiere Kriterien für Benachrichtigung betroffener Personen
- Implementiere Dokumentationspflicht
- Erstelle Kommunikationspläne

Referenz: DSGVO Art. 33 (Meldung an Aufsichtsbehörde), Art. 34 (Benachrichtigung betroffener Personen)
-->

## Zweck

Dieses Dokument regelt den Umgang mit Datenschutzverletzungen bei {{ meta.organization }} gemäß Art. 33-34 DSGVO. Es definiert Meldepflichten, Fristen und Prozesse zur Bewältigung von Datenschutzvorfällen.

## Definition Datenschutzverletzung (Art. 4 Nr. 12)

Eine Verletzung des Schutzes personenbezogener Daten ist eine Verletzung der Sicherheit, die zur Vernichtung, zum Verlust, zur Veränderung oder zur unbefugten Offenlegung von bzw. zum unbefugten Zugang zu personenbezogenen Daten führt.

### Kategorien von Datenschutzverletzungen

| Kategorie | Beschreibung | Beispiele |
|-----------|--------------|-----------|
| **Vertraulichkeitsverletzung** | Unbefugte Offenlegung oder Zugang | Datenleck, Hacking, versehentliche Weitergabe |
| **Integritätsverletzung** | Unbefugte Veränderung | Manipulation, Korruption von Daten |
| **Verfügbarkeitsverletzung** | Verlust oder Vernichtung | Ransomware, Hardwareausfall, versehentliche Löschung |

## Meldepflicht an Aufsichtsbehörde (Art. 33)

### Grundsatz (Art. 33 Abs. 1)

Der Verantwortliche meldet eine Datenschutzverletzung unverzüglich und möglichst binnen 72 Stunden an die zuständige Aufsichtsbehörde, es sei denn, die Verletzung führt voraussichtlich nicht zu einem Risiko für die Rechte und Freiheiten natürlicher Personen.

### Risikobewertung

**Kriterien zur Bewertung des Risikos:**

| Kriterium | Niedriges Risiko | Hohes Risiko |
|-----------|------------------|--------------|
| Art der Daten | Allgemeine Kontaktdaten | Besondere Kategorien (Art. 9), Finanzdaten |
| Umfang | Wenige Betroffene | Viele Betroffene |
| Schwere | Geringe Auswirkungen | Schwerwiegende Auswirkungen |
| Schutzmaßnahmen | Verschlüsselt, pseudonymisiert | Unverschlüsselt, Klartext |
| Betroffene | Mitarbeiter (intern) | Kunden, Kinder, vulnerable Gruppen |

**Entscheidungsbaum:**
1. Liegt eine Datenschutzverletzung vor? → Ja/Nein
2. Besteht ein Risiko für Rechte und Freiheiten? → Ja/Nein
3. Wenn Ja: Meldung erforderlich
4. Wenn hohes Risiko: Zusätzlich Benachrichtigung betroffener Personen

### Meldepflichtiger Inhalt (Art. 33 Abs. 3)

Die Meldung muss mindestens folgende Informationen enthalten:

#### a) Art der Verletzung

- Beschreibung der Datenschutzverletzung
- Kategorien und ungefähre Anzahl betroffener Personen
- Kategorien und ungefähre Anzahl betroffener Datensätze

#### b) Kontaktstelle

- Name und Kontaktdaten des Datenschutzbeauftragten oder einer sonstigen Anlaufstelle

#### c) Beschreibung der Folgen

- Beschreibung der wahrscheinlichen Folgen der Datenschutzverletzung

#### d) Ergriffene Maßnahmen

- Beschreibung der ergriffenen oder vorgeschlagenen Maßnahmen zur Behebung und Abmilderung

### Meldefrist

**72-Stunden-Frist ab Kenntnisnahme**

| Zeitpunkt | Maßnahme |
|-----------|----------|
| T+0 (Entdeckung) | Incident-Response aktivieren, erste Bewertung |
| T+24h | Risikobewertung abgeschlossen, Meldepflicht geklärt |
| T+48h | Meldung vorbereitet |
| T+72h | Meldung an Aufsichtsbehörde übermittelt |

**Bei Überschreitung der 72-Stunden-Frist:**
- Begründung der Verzögerung erforderlich (Art. 33 Abs. 1)

### Zuständige Aufsichtsbehörde

**Aufsichtsbehörde:** [TODO: Name der zuständigen Behörde]  
**Adresse:** [TODO: Adresse]  
**Melde-Portal:** [TODO: URL zum Online-Meldeformular]  
**Kontakt:** [TODO: E-Mail, Telefon]

## Benachrichtigung betroffener Personen (Art. 34)

### Benachrichtigungspflicht (Art. 34 Abs. 1)

Wenn die Datenschutzverletzung voraussichtlich ein hohes Risiko für die Rechte und Freiheiten natürlicher Personen zur Folge hat, benachrichtigt der Verantwortliche die betroffene Person unverzüglich.

### Kriterien für hohes Risiko

- **Besondere Kategorien personenbezogener Daten (Art. 9)**
- **Finanzdaten, Zugangsdaten**
- **Große Anzahl betroffener Personen**
- **Vulnerable Gruppen (Kinder, Kranke)**
- **Schwerwiegende Folgen (Identitätsdiebstahl, finanzielle Verluste)**

### Inhalt der Benachrichtigung (Art. 34 Abs. 2)

Die Benachrichtigung muss enthalten:

- Art der Datenschutzverletzung
- Name und Kontaktdaten des Datenschutzbeauftragten
- Wahrscheinliche Folgen der Datenschutzverletzung
- Ergriffene oder vorgeschlagene Maßnahmen zur Behebung und Abmilderung
- Empfehlungen für betroffene Personen (z.B. Passwort ändern)

### Ausnahmen von der Benachrichtigungspflicht (Art. 34 Abs. 3)

Keine Benachrichtigung erforderlich, wenn:

**a) Schutzmaßnahmen:** Daten waren verschlüsselt oder anderweitig geschützt  
**b) Nachträgliche Maßnahmen:** Maßnahmen wurden ergriffen, die hohes Risiko beseitigen  
**c) Unverhältnismäßiger Aufwand:** Öffentliche Bekanntmachung stattdessen

## Incident-Response-Prozess

### Phase 1: Erkennung und Bewertung

**Zeitrahmen: 0-4 Stunden**

1. Vorfall erkennen und melden
2. Incident-Response-Team aktivieren
3. Erste Bewertung durchführen
4. Datenschutzverletzung bestätigen

**Verantwortlich:** [TODO: IT-Security, Datenschutzbeauftragter]

### Phase 2: Eindämmung

**Zeitrahmen: 4-12 Stunden**

1. Sofortmaßnahmen zur Schadensbegrenzung
2. Betroffene Systeme isolieren
3. Weitere Datenverluste verhindern
4. Forensische Sicherung

**Verantwortlich:** [TODO: IT-Security]

### Phase 3: Analyse und Risikobewertung

**Zeitrahmen: 12-24 Stunden**

1. Umfang der Verletzung ermitteln
2. Betroffene Daten und Personen identifizieren
3. Risikobewertung durchführen
4. Meldepflicht prüfen

**Verantwortlich:** [TODO: Datenschutzbeauftragter, IT-Security]

### Phase 4: Meldung und Benachrichtigung

**Zeitrahmen: 24-72 Stunden**

1. Meldung an Aufsichtsbehörde (falls erforderlich)
2. Benachrichtigung betroffener Personen (falls erforderlich)
3. Interne Kommunikation
4. Externe Kommunikation (falls erforderlich)

**Verantwortlich:** [TODO: Datenschutzbeauftragter, Geschäftsführung]

### Phase 5: Wiederherstellung

**Zeitrahmen: 72 Stunden - Wochen**

1. Systeme wiederherstellen
2. Sicherheitslücken schließen
3. Maßnahmen zur Verhinderung implementieren
4. Monitoring verstärken

**Verantwortlich:** [TODO: IT-Security]

### Phase 6: Nachbereitung

**Zeitrahmen: Nach Abschluss**

1. Incident dokumentieren
2. Lessons Learned durchführen
3. Prozesse anpassen
4. Schulungen aktualisieren

**Verantwortlich:** [TODO: Datenschutzbeauftragter, IT-Security]

## Dokumentationspflicht (Art. 33 Abs. 5)

Der Verantwortliche dokumentiert alle Datenschutzverletzungen, einschließlich aller Fakten, Auswirkungen und ergriffenen Abhilfemaßnahmen.

### Breach-Register

| Datum | Art der Verletzung | Betroffene Daten | Anzahl Betroffene | Risiko | Gemeldet | Benachrichtigt | Status |
|-------|-------------------|------------------|-------------------|--------|----------|----------------|--------|
| [TODO] | [TODO] | [TODO] | [TODO] | Niedrig/Hoch | Ja/Nein | Ja/Nein | Offen/Geschlossen |

### Aufbewahrungsfrist

**Dokumentation:** Mindestens 3 Jahre nach Abschluss des Vorfalls

## Kommunikationspläne

### Interne Kommunikation

**Eskalationskette:**
1. Entdecker → IT-Security
2. IT-Security → Datenschutzbeauftragter
3. Datenschutzbeauftragter → Geschäftsführung
4. Geschäftsführung → Aufsichtsrat (bei schwerwiegenden Vorfällen)

### Externe Kommunikation

**Stakeholder:**
- Aufsichtsbehörde
- Betroffene Personen
- Medien (bei öffentlichem Interesse)
- Geschäftspartner (bei Betroffenheit)
- Versicherung

**Kommunikationsverantwortlicher:** [TODO: Rolle]

## Verantwortlichkeiten

| Aufgabe | Verantwortlich | Rechenschaftspflichtig | Konsultiert | Informiert |
|---------|----------------|----------------------|-------------|------------|
| Incident Detection | [TODO] | [TODO] | [TODO] | [TODO] |
| Risikobewertung | [TODO] | [TODO] | [TODO] | [TODO] |
| Meldung Aufsichtsbehörde | [TODO] | [TODO] | [TODO] | [TODO] |
| Benachrichtigung Betroffene | [TODO] | [TODO] | [TODO] | [TODO] |
| Dokumentation | [TODO] | [TODO] | [TODO] | [TODO] |

## Verknüpfung zu anderen Dokumenten

- **Sicherheit der Verarbeitung (Art. 32):** Präventive Maßnahmen
- **Auftragsverarbeitung (Art. 28):** Meldepflicht von Auftragsverarbeitern
- **Datenschutz-Folgenabschätzung (Art. 35):** Risikobewertung
- **Incident-Response-Plan:** Detaillierte technische Prozesse

---

**Nächste Schritte:**
1. Implementieren Sie einen Incident-Response-Prozess
2. Definieren Sie Eskalationswege und Verantwortlichkeiten
3. Erstellen Sie Vorlagen für Meldungen und Benachrichtigungen
4. Führen Sie regelmäßige Incident-Response-Übungen durch
5. Etablieren Sie ein Breach-Register
