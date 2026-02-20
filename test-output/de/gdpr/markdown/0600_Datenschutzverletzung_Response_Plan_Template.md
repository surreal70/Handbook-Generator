# Datenschutzverletzung Response Plan (Template)

**Dokument-ID:** 0600
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



## Zweck

Dieser Response Plan definiert die Schritte zur Bewältigung von Datenschutzverletzungen bei AdminSend GmbH. Er stellt sicher, dass Datenschutzverletzungen schnell erkannt, bewertet und gemäß DSGVO Art. 33-34 behandelt werden.

## Geltungsbereich

Dieser Plan gilt für alle Datenschutzverletzungen, die personenbezogene Daten betreffen, die von AdminSend GmbH verarbeitet werden.

## Breach Response Team

### Kernteam

| Rolle | Name | Kontakt | Verantwortlichkeiten |
|-------|------|---------|---------------------|
| **Incident Commander** | [TODO] | [TODO: Telefon, E-Mail] | Gesamtverantwortung, Entscheidungen |
| **Datenschutzbeauftragter** | [TODO] | [TODO: Telefon, E-Mail] | Rechtliche Bewertung, Meldepflicht |
| **IT-Security Lead** | [TODO] | [TODO: Telefon, E-Mail] | Technische Analyse, Eindämmung |
| **Legal Counsel** | [TODO] | [TODO: Telefon, E-Mail] | Rechtliche Beratung |
| **Communications Lead** | [TODO] | [TODO: Telefon, E-Mail] | Interne/externe Kommunikation |

### Erweiterte Stakeholder

| Rolle | Name | Kontakt | Wann einbeziehen |
|-------|------|---------|------------------|
| **Geschäftsführung** | [TODO] | [TODO] | Bei hohem Risiko |
| **HR** | [TODO] | [TODO] | Bei Mitarbeiterdaten |
| **Compliance** | [TODO] | [TODO] | Bei regulatorischen Fragen |
| **PR/Marketing** | [TODO] | [TODO] | Bei öffentlicher Kommunikation |

## Breach Response Prozess

### Phase 1: Erkennung und Meldung (0-2 Stunden)

#### 1.1 Breach erkennen

**Erkennungsquellen:**
- Monitoring-Systeme und Alerts
- Mitarbeiter-Meldungen
- Externe Meldungen (Kunden, Partner)
- Audit-Findings
- Medienberichte

#### 1.2 Initiale Meldung

**Wer meldet:**
- Jeder Mitarbeiter, der eine potenzielle Datenschutzverletzung entdeckt

**An wen:**
- IT-Security: [TODO: E-Mail/Telefon]
- Datenschutzbeauftragter: [TODO: E-Mail/Telefon]

**Meldeformular:**
```
INITIALE BREACH-MELDUNG

Melder: [Name, Abteilung, Kontakt]
Datum/Uhrzeit Entdeckung: [YYYY-MM-DD HH:MM]
Entdeckungsart: [Monitoring / Mitarbeiter / Extern / Audit / Sonstiges]

Kurzbeschreibung:
[Was ist passiert?]

Betroffene Systeme:
[Welche Systeme sind betroffen?]

Betroffene Daten (erste Einschätzung):
[Welche Art von Daten?]

Anzahl betroffener Personen (Schätzung):
[Ungefähre Anzahl]

Sofortmaßnahmen ergriffen:
[Was wurde bereits getan?]
```

#### 1.3 Breach Response Team aktivieren

**Incident Commander:**
- Aktiviert Kernteam
- Setzt initiales Meeting an (innerhalb 2 Stunden)
- Erstellt Breach-ID: `BREACH-[YYYY]-[NNN]`

### Phase 2: Bewertung und Eindämmung (2-12 Stunden)

#### 2.1 Initiale Bewertung

**Checkliste:**
- [ ] Liegt tatsächlich eine Datenschutzverletzung vor?
- [ ] Welche Kategorie: Vertraulichkeit / Integrität / Verfügbarkeit?
- [ ] Welche Daten sind betroffen?
- [ ] Wie viele Personen sind betroffen?
- [ ] Sind besondere Kategorien (Art. 9) betroffen?
- [ ] Wie ist die Verletzung entstanden?
- [ ] Ist die Verletzung noch aktiv?

**Dokumentation:**
- Alle Erkenntnisse im Breach-Register dokumentieren
- Screenshots und Logs sichern
- Forensische Sicherung bei Bedarf

#### 2.2 Sofortige Eindämmung

**Technische Maßnahmen:**
- [ ] Betroffene Systeme isolieren
- [ ] Zugriffe sperren
- [ ] Passwörter zurücksetzen
- [ ] Sicherheitslücken schließen
- [ ] Weitere Datenverluste verhindern

**Verantwortlich:** IT-Security Lead

**Zeitrahmen:** Innerhalb 4 Stunden

#### 2.3 Umfangsermittlung

**Zu klären:**
- Genaue Anzahl betroffener Personen
- Genaue Datenkategorien
- Zeitraum der Verletzung
- Ursache der Verletzung
- Potenzielle Auswirkungen

**Methoden:**
- Log-Analyse
- Datenbank-Abfragen
- System-Forensik
- Interviews mit Beteiligten

### Phase 3: Risikobewertung (12-24 Stunden)

#### 3.1 Risiko für Betroffene bewerten

**Bewertungskriterien:**

| Kriterium | Bewertung | Punkte |
|-----------|-----------|--------|
| **Art der Daten** | | |
| - Allgemeine Kontaktdaten | Niedrig | 1 |
| - Finanzdaten, Zugangsdaten | Mittel | 2 |
| - Besondere Kategorien (Art. 9) | Hoch | 3 |
| **Anzahl Betroffene** | | |
| - < 100 Personen | Niedrig | 1 |
| - 100-1.000 Personen | Mittel | 2 |
| - > 1.000 Personen | Hoch | 3 |
| **Schutzmaßnahmen** | | |
| - Verschlüsselt, pseudonymisiert | Niedrig | 1 |
| - Teilweise geschützt | Mittel | 2 |
| - Unverschlüsselt, Klartext | Hoch | 3 |
| **Betroffene Personen** | | |
| - Mitarbeiter (intern) | Niedrig | 1 |
| - Kunden, Partner | Mittel | 2 |
| - Kinder, vulnerable Gruppen | Hoch | 3 |

**Gesamtrisiko:**
- 4-6 Punkte: Niedriges Risiko
- 7-9 Punkte: Mittleres Risiko (Meldepflicht)
- 10-12 Punkte: Hohes Risiko (Meldepflicht + Benachrichtigung)

#### 3.2 Meldepflicht prüfen

**Entscheidungsbaum:**

```
Datenschutzverletzung bestätigt?
├─ Nein → Dokumentieren, kein weiterer Handlungsbedarf
└─ Ja → Risiko für Rechte und Freiheiten?
    ├─ Nein (< 7 Punkte) → Nur dokumentieren
    └─ Ja (≥ 7 Punkte) → Meldung an Aufsichtsbehörde erforderlich
        └─ Hohes Risiko (≥ 10 Punkte)?
            ├─ Nein → Nur Meldung
            └─ Ja → Meldung + Benachrichtigung Betroffener
```

**Verantwortlich:** Datenschutzbeauftragter

### Phase 4: Meldung und Benachrichtigung (24-72 Stunden)

#### 4.1 Meldung an Aufsichtsbehörde (falls erforderlich)

**Frist:** 72 Stunden ab Kenntnisnahme

**Zuständige Behörde:**
- Name: [TODO: z.B. Landesbeauftragte für Datenschutz]
- Melde-Portal: [TODO: URL]
- Kontakt: [TODO: E-Mail, Telefon]

**Meldung vorbereiten:**
- Verwende Template 0610 (Breach Notification Template)
- Stelle alle erforderlichen Informationen zusammen
- Lasse durch Datenschutzbeauftragten prüfen
- Hole Freigabe von Geschäftsführung

**Verantwortlich:** Datenschutzbeauftragter

#### 4.2 Benachrichtigung Betroffener (falls erforderlich)

**Voraussetzung:** Hohes Risiko (≥ 10 Punkte)

**Ausnahmen (keine Benachrichtigung):**
- Daten waren verschlüsselt/pseudonymisiert
- Nachträgliche Maßnahmen beseitigen hohes Risiko
- Unverhältnismäßiger Aufwand (dann öffentliche Bekanntmachung)

**Benachrichtigung vorbereiten:**
- Verwende Template 0620 (Breach Communication Template)
- Klare, verständliche Sprache
- Konkrete Handlungsempfehlungen
- Kontaktmöglichkeiten

**Kommunikationskanäle:**
- E-Mail (bevorzugt)
- Brief (bei fehlender E-Mail)
- Öffentliche Bekanntmachung (bei unverhältnismäßigem Aufwand)

**Verantwortlich:** Communications Lead, Datenschutzbeauftragter

#### 4.3 Interne Kommunikation

**Zu informieren:**
- Geschäftsführung
- Betroffene Abteilungen
- Betriebsrat (bei Mitarbeiterdaten)
- Alle Mitarbeiter (bei Bedarf)

**Kommunikationsplan:**
- Initiale Information: Innerhalb 24 Stunden
- Regelmäßige Updates: Täglich während aktiver Phase
- Abschlussbericht: Nach Incident-Closure

### Phase 5: Wiederherstellung (72 Stunden - Wochen)

#### 5.1 Systeme wiederherstellen

**Checkliste:**
- [ ] Sicherheitslücken geschlossen
- [ ] Systeme gepatcht/aktualisiert
- [ ] Zugriffskontrol len überprüft
- [ ] Monitoring verstärkt
- [ ] Backup-Strategie überprüft

**Verantwortlich:** IT-Security Lead

#### 5.2 Präventive Maßnahmen

**Zu implementieren:**
- Technische Verbesserungen
- Prozessanpassungen
- Schulungen
- Verstärktes Monitoring

### Phase 6: Nachbereitung (Nach Abschluss)

#### 6.1 Post-Breach Review

**Verwende Template 0640 (Post-Breach Review Template)**

**Durchzuführen innerhalb:** 2 Wochen nach Incident-Closure

**Teilnehmer:**
- Breach Response Team
- Betroffene Abteilungen
- Geschäftsführung

**Themen:**
- Was lief gut?
- Was lief schlecht?
- Lessons Learned
- Verbesserungsmaßnahmen

#### 6.2 Dokumentation abschließen

**Checkliste:**
- [ ] Breach-Register aktualisiert
- [ ] Alle Meldungen archiviert
- [ ] Timeline dokumentiert
- [ ] Kosten erfasst
- [ ] Maßnahmen dokumentiert

**Aufbewahrungsfrist:** Mindestens 3 Jahre

## Kommunikationsrichtlinien

### Interne Kommunikation

**Grundsätze:**
- Transparent, aber vertraulich
- Faktenbasiert
- Regelmäßige Updates
- Klare Verantwortlichkeiten

### Externe Kommunikation

**Grundsätze:**
- Nur durch autorisierte Sprecher
- Abgestimmt mit Legal und Datenschutzbeauftragtem
- Keine Spekulationen
- Fokus auf Maßnahmen und Unterstützung

**Medienanfragen:**
- Alle Anfragen an Communications Lead
- Keine spontanen Statements
- Vorbereitung von Q&A

## Eskalation

### Eskalationsstufen

**Stufe 1: Routine**
- Niedriges Risiko
- < 100 Betroffene
- Keine besonderen Kategorien
- Kernteam ausreichend

**Stufe 2: Erhöht**
- Mittleres Risiko
- 100-1.000 Betroffene
- Meldepflicht
- Geschäftsführung informieren

**Stufe 3: Kritisch**
- Hohes Risiko
- > 1.000 Betroffene
- Besondere Kategorien
- Benachrichtigungspflicht
- Geschäftsführung aktiv einbinden
- Externe Berater erwägen

**Stufe 4: Krise**
- Sehr hohes Risiko
- Massive Auswirkungen
- Öffentliches Interesse
- Krisenmanagement aktivieren
- Externe PR-Unterstützung
- Aufsichtsrat informieren

## Kontakte und Ressourcen

### Interne Kontakte

| Rolle | Name | Telefon | E-Mail | Verfügbarkeit |
|-------|------|---------|--------|---------------|
| Incident Commander | [TODO] | [TODO] | [TODO] | 24/7 |
| Datenschutzbeauftragter | [TODO] | [TODO] | [TODO] | 24/7 |
| IT-Security Lead | [TODO] | [TODO] | [TODO] | 24/7 |
| Legal Counsel | [TODO] | [TODO] | [TODO] | Werktags |
| Communications Lead | [TODO] | [TODO] | [TODO] | Werktags |

### Externe Kontakte

| Organisation | Kontakt | Telefon | E-Mail | Zweck |
|--------------|---------|---------|--------|-------|
| Aufsichtsbehörde | [TODO] | [TODO] | [TODO] | Meldung |
| Forensik-Dienstleister | [TODO] | [TODO] | [TODO] | Analyse |
| Rechtsanwalt (extern) | [TODO] | [TODO] | [TODO] | Beratung |
| PR-Agentur | [TODO] | [TODO] | [TODO] | Krisenkommunikation |
| Cyber-Versicherung | [TODO] | [TODO] | [TODO] | Schadensmeldung |

### Tools und Systeme

| Tool | Zweck | Zugriff |
|------|-------|---------|
| [TODO: SIEM] | Monitoring, Log-Analyse | [TODO: URL] |
| [TODO: Ticketsystem] | Incident-Tracking | [TODO: URL] |
| [TODO: Breach-Register] | Dokumentation | [TODO: URL/Datei] |
| [TODO: Kommunikationsplattform] | Team-Koordination | [TODO: URL] |

## Anhänge

- **Template 0610:** Breach Notification Template (Aufsichtsbehörde)
- **Template 0620:** Breach Communication Template (Betroffene)
- **Template 0630:** Breach Register Template
- **Template 0640:** Post-Breach Review Template

**Nächste Schritte:**
1. Passe diesen Plan an deine Organisation an
2. Definiere alle Rollen und Kontakte
3. Führe Breach-Response-Übungen durch (mindestens jährlich)
4. Halte den Plan aktuell
5. Stelle sicher, dass alle Teammitglieder den Plan kennen

