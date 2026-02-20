# Speicherbegrenzung

**Dokument-ID:** GDPR-0140
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

Dieses Dokument beschreibt die Umsetzung des Grundsatzes der Speicherbegrenzung in der AdminSend GmbH. Personenbezogene Daten dürfen nur so lange gespeichert werden, wie es für den Verarbeitungszweck erforderlich ist.

## Grundsatz gemäß Art. 5 Abs. 1 lit. e DSGVO

**Rechtliche Anforderung:**  
Personenbezogene Daten müssen in einer Form gespeichert werden, die die Identifizierung der betroffenen Personen nur so lange ermöglicht, wie es für die Zwecke, für die sie verarbeitet werden, erforderlich ist.

### Kernprinzip

**Speicherdauer = Zweckerfüllung + gesetzliche Aufbewahrungsfristen**

Nach Ablauf der Speicherdauer müssen Daten:
- Gelöscht werden, oder
- Anonymisiert werden, oder
- Archiviert werden (mit Zugriffsbeschränkungen)

## Löschkonzept

### Festlegung von Löschfristen

**Kriterien für Löschfristen:**
1. Zweck der Verarbeitung
2. Gesetzliche Aufbewahrungsfristen
3. Vertragliche Verpflichtungen
4. Berechtigte Interessen
5. Verjährungsfristen

### Löschfristenmatrix

| Verarbeitungszweck | Datenart | Löschfrist | Rechtsgrundlage | Ausnahmen |
|-------------------|----------|------------|-----------------|-----------|
| [TODO: Kundenbestellung] | Bestelldaten | Nach Vertragserfüllung + 2 Jahre | Gewährleistung | Steuerrecht: 10 Jahre |
| [TODO: Newsletter] | E-Mail, Name | Bis Widerruf | Einwilligung | Keine |
| [TODO: Bewerbung] | Bewerberdaten | 6 Monate nach Absage | Berechtigtes Interesse | Mit Einwilligung länger |
| [TODO: Buchhaltung] | Rechnungsdaten | 10 Jahre | AO, HGB | Keine |
| [TODO: Mitarbeiterdaten] | Personaldaten | 10 Jahre nach Austritt | Sozialversicherung | Keine |

## Gesetzliche Aufbewahrungsfristen

### Steuerrecht (Deutschland)

| Dokumentart | Aufbewahrungsfrist | Rechtsgrundlage |
|-------------|-------------------|-----------------|
| Bücher, Aufzeichnungen, Jahresabschlüsse | 10 Jahre | § 147 AO |
| Handelsbriefe, Buchungsbelege | 10 Jahre | § 147 AO |
| Sonstige Unterlagen | 6 Jahre | § 147 AO |

### Handelsrecht (Deutschland)

| Dokumentart | Aufbewahrungsfrist | Rechtsgrundlage |
|-------------|-------------------|-----------------|
| Handelsbücher, Inventare, Bilanzen | 10 Jahre | § 257 HGB |
| Handelsbriefe | 6 Jahre | § 257 HGB |
| Buchungsbelege | 10 Jahre | § 257 HGB |

### Weitere gesetzliche Fristen

- [TODO: Sozialversicherungsrecht]
- [TODO: Arbeitsrecht]
- [TODO: Produkthaftung]
- [TODO: Branchenspezifische Vorschriften]

## Löschprozesse

### Routinemäßige Löschung

**Automatisierte Löschprozesse:**

| System/Datenbank | Löschrhythmus | Methode | Verantwortlich |
|-----------------|---------------|---------|----------------|
| [TODO: CRM-System] | Monatlich | Automatisiert | IT |
| [TODO: Webserver-Logs] | Täglich | Automatisiert | IT |
| [TODO: Backup-Systeme] | Bei Löschung | Manuell | IT |
| [TODO: Archiv] | Jährlich | Manuell | Fachabteilung |

### Löschverfahren

**Schritte bei Löschung:**

1. **Identifikation löschbarer Daten**
   - Automatische Prüfung der Löschfristen
   - Berücksichtigung von Ausnahmen
   - Erstellung Löschliste

2. **Prüfung vor Löschung**
   - Keine laufenden Verfahren
   - Keine gesetzlichen Aufbewahrungspflichten
   - Keine vertraglichen Verpflichtungen

3. **Durchführung der Löschung**
   - Löschung in allen Systemen
   - Löschung in Backups (oder Markierung)
   - Sichere Löschung (unwiederbringlich)

4. **Dokumentation**
   - Protokollierung der Löschung
   - Nachweis der Löschung
   - Aufbewahrung des Löschprotokolls

### Sichere Löschung

**Technische Löschmethoden:**
- Überschreiben von Datenträgern
- Kryptografische Löschung (Schlüsselvernichtung)
- Physische Vernichtung von Datenträgern
- Sichere Löschung in Cloud-Systemen

## Ausnahmen von der Löschpflicht

### Archivierung im öffentlichen Interesse (Art. 89 DSGVO)

**Zulässige Archivierung für:**
- Archivzwecke im öffentlichen Interesse
- Wissenschaftliche oder historische Forschungszwecke
- Statistische Zwecke

**Voraussetzungen:**
- Geeignete Garantien (Pseudonymisierung, Zugriffsbeschränkungen)
- Datenminimierung
- Technische und organisatorische Maßnahmen

### Aufbewahrung für Rechtsansprüche

**Aufbewahrung zulässig bei:**
- Laufenden Gerichtsverfahren
- Drohenden Rechtsstreitigkeiten
- Verjährungsfristen noch nicht abgelaufen

**Maßnahmen:**
- Einschränkung der Verarbeitung (Art. 18)
- Zugriffsbeschränkungen
- Dokumentation der Aufbewahrungsgründe

## Löschrecht (Art. 17 DSGVO)

### Umsetzung des Löschrechts

**Betroffene Personen haben Recht auf Löschung, wenn:**
- Daten nicht mehr erforderlich
- Einwilligung widerrufen
- Widerspruch eingelegt (Art. 21)
- Daten unrechtmäßig verarbeitet
- Rechtliche Verpflichtung zur Löschung

**Ausnahmen vom Löschrecht:**
- Ausübung des Rechts auf freie Meinungsäußerung
- Erfüllung rechtlicher Verpflichtungen
- Geltendmachung von Rechtsansprüchen
- Archivzwecke im öffentlichen Interesse

### Löschantragsprozess

1. **Eingang des Antrags**
   - Identifikation der betroffenen Person
   - Dokumentation des Antrags
   - Bestätigung des Eingangs

2. **Prüfung der Löschpflicht**
   - Sind Daten noch erforderlich?
   - Bestehen Aufbewahrungspflichten?
   - Greifen Ausnahmen?

3. **Durchführung oder Ablehnung**
   - Bei Löschpflicht: Löschung durchführen
   - Bei Ausnahme: Begründete Ablehnung
   - Benachrichtigung von Empfängern (Art. 19)

4. **Rückmeldung**
   - Information über Löschung oder Ablehnung
   - Frist: Unverzüglich, spätestens 1 Monat

## Kontrollen und Überwachung

### Regelmäßige Überprüfungen

| Kontrolle | Frequenz | Verantwortlich | Dokumentation |
|-----------|----------|----------------|---------------|
| Löschfristenprüfung | Monatlich | IT | Löschprotokoll |
| Löschkonzept-Review | Jährlich | DSB | Review-Bericht |
| Backup-Löschung | Quartalsweise | IT | Backup-Protokoll |
| Löschanträge | Bei Eingang | DSB | Antragsregister |

### Löschprotokollierung

**Dokumentation jeder Löschung:**
- Datum und Uhrzeit
- Gelöschte Datenarten
- Anzahl gelöschter Datensätze
- Löschgrund (Frist, Antrag, etc.)
- Durchführende Person
- Betroffene Systeme

## Dokumentation

### Nachweispflichten

**Für Accountability dokumentieren:**
- Löschkonzept mit Fristen
- Löschprozesse und -verfahren
- Durchgeführte Löschungen (Protokolle)
- Bearbeitete Löschanträge
- Ausnahmen und deren Begründung

### Verzeichnis von Verarbeitungstätigkeiten (Art. 30)

**Dokumentation der Speicherdauer:**
- Löschfristen für jede Verarbeitungstätigkeit
- Begründung der Fristen
- Gesetzliche Aufbewahrungspflichten
- Löschverfahren

## Verknüpfung zu anderen Dokumenten

- **Datenschutzgrundsätze (Art. 5):** Speicherbegrenzung als Grundprinzip
- **Löschrecht (Art. 17):** Umsetzung des Betroffenenrechts
- **Einschränkung (Art. 18):** Alternative zur Löschung
- **Mitteilungspflicht (Art. 19):** Benachrichtigung von Empfängern
- **Verzeichnis (Art. 30):** Dokumentation der Löschfristen

## Häufige Verstöße und deren Vermeidung

| Verstoß | Beispiel | Vermeidung |
|---------|----------|------------|
| Unbegrenzte Speicherung | "Für alle Fälle aufbewahren" | Löschfristen definieren |
| Fehlende Löschprozesse | Keine automatisierte Löschung | Löschroutinen implementieren |
| Ignorieren von Löschanträgen | Verzögerte Bearbeitung | Prozess etablieren |
| Unvollständige Löschung | Nur in einem System gelöscht | Alle Systeme prüfen |

**Nächste Schritte:**
1. Definieren Sie Löschfristen für alle Verarbeitungstätigkeiten
2. Implementieren Sie automatisierte Löschprozesse
3. Etablieren Sie Verfahren für Löschanträge
4. Dokumentieren Sie Löschkonzept und -protokolle
5. Schulen Sie Mitarbeiter zu Löschpflichten

