# Berichtigung und Löschung

**Dokument-ID:** GDPR-0230
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

Dieses Dokument beschreibt die Umsetzung des Rechts auf Berichtigung und Löschung in der AdminSend GmbH. Betroffene Personen haben das Recht auf Berichtigung unrichtiger und Löschung nicht mehr erforderlicher Daten.

## Recht auf Berichtigung (Art. 16)

### Umfang des Berichtigungsrechts

**Betroffene Personen haben Recht auf:**
- Unverzügliche Berichtigung unrichtiger Daten
- Vervollständigung unvollständiger Daten
- Ergänzende Erklärung

### Berichtigungsprozess

**Standardprozess:**

1. **Eingang des Antrags (Tag 0)**
   - Registrierung
   - Eingangsbestätigung
   - Zuweisung

2. **Prüfung (Tag 1-10)**
   - Identifikation der betroffenen Person
   - Prüfung der Unrichtigkeit
   - Abgleich mit Nachweisen

3. **Durchführung (Tag 11-25)**
   - Berichtigung in allen Systemen
   - Benachrichtigung von Empfängern (Art. 19)
   - Dokumentation

4. **Rückmeldung (Tag 26-30)**
   - Information über durchgeführte Berichtigung
   - Liste der benachrichtigten Empfänger

### Berichtigungsmatrix

| System | Verantwortlich | Berichtigungsverfahren | Dokumentation |
|--------|----------------|----------------------|---------------|
| [TODO: CRM] | IT | Manuelle Änderung | Change-Log |
| [TODO: ERP] | IT | Workflow-gesteuert | Audit-Trail |
| [TODO: Datenbank] | IT | SQL-Update | Änderungsprotokoll |
| [TODO: Backup] | IT | Markierung | Backup-Log |

## Recht auf Löschung (Art. 17)

### Löschgründe

**Löschung ist erforderlich, wenn:**

| Grund | Beschreibung | Beispiel |
|-------|--------------|----------|
| Nicht mehr erforderlich | Zweck erfüllt | Bewerberdaten nach Absage |
| Widerruf der Einwilligung | Einwilligung zurückgezogen | Newsletter-Abmeldung |
| Widerspruch | Widerspruch eingelegt (Art. 21) | Werbewiderspruch |
| Unrechtmäßige Verarbeitung | Ohne Rechtsgrundlage | Daten ohne Einwilligung |
| Rechtliche Verpflichtung | Gesetzliche Löschpflicht | Datenschutzverstoß |
| Kinder | Dienste der Informationsgesellschaft | Social Media unter 16 |

### Ausnahmen vom Löschrecht

**Löschung nicht erforderlich bei:**

| Ausnahme | Beschreibung |
|----------|--------------|
| Meinungsfreiheit | Ausübung des Rechts auf freie Meinungsäußerung |
| Rechtliche Verpflichtung | Erfüllung rechtlicher Verpflichtungen |
| Öffentliches Interesse | Aufgaben im öffentlichen Interesse |
| Gesundheitswesen | Gesundheitsvorsorge, Arbeitsmedizin |
| Archivzwecke | Archivierung im öffentlichen Interesse |
| Rechtsansprüche | Geltendmachung, Ausübung oder Verteidigung |

### Löschprozess

**Standardprozess:**

1. **Eingang des Antrags (Tag 0)**
   - Registrierung
   - Eingangsbestätigung
   - Zuweisung

2. **Prüfung (Tag 1-10)**
   - Identifikation der betroffenen Person
   - Prüfung der Löschgründe
   - Prüfung von Ausnahmen
   - Prüfung gesetzlicher Aufbewahrungsfristen

3. **Entscheidung (Tag 11-15)**
   - Löschung oder begründete Ablehnung
   - Bei Ablehnung: Prüfung der Einschränkung (Art. 18)

4. **Durchführung (Tag 16-25)**
   - Löschung in allen Systemen
   - Benachrichtigung von Empfängern (Art. 19)
   - Dokumentation

5. **Rückmeldung (Tag 26-30)**
   - Information über Löschung oder Ablehnung
   - Bei Ablehnung: Begründung und Rechtsbehelfe

### Löschverfahren

**Technische Löschung:**

| System | Löschmethode | Verantwortlich | Dokumentation |
|--------|--------------|----------------|---------------|
| [TODO: Produktivsysteme] | Sofortige Löschung | IT | Löschprotokoll |
| [TODO: Backups] | Markierung/Überschreiben | IT | Backup-Log |
| [TODO: Archive] | Physische Vernichtung | IT | Vernichtungsprotokoll |
| [TODO: Cloud] | API-gesteuerte Löschung | IT | API-Log |

## Mitteilungspflicht (Art. 19)

### Benachrichtigung von Empfängern

**Bei Berichtigung oder Löschung müssen Empfänger informiert werden:**

**Prozess:**
1. Identifikation aller Empfänger
2. Benachrichtigung über Berichtigung/Löschung
3. Dokumentation der Benachrichtigungen
4. Information der betroffenen Person über Empfänger (auf Verlangen)

**Ausnahmen:**
- Unmöglich
- Unverhältnismäßiger Aufwand

### Empfängermatrix

| Empfängertyp | Benachrichtigungspflicht | Methode | Dokumentation |
|--------------|-------------------------|---------|---------------|
| [TODO: Auftragsverarbeiter] | Ja | E-Mail | Benachrichtigungslog |
| [TODO: Dritte Empfänger] | Ja | E-Mail/Schriftlich | Benachrichtigungslog |
| [TODO: Öffentliche Stellen] | Ja | Schriftlich | Benachrichtigungslog |

## Dokumentation

### Berichtigungs- und Löschregister

| Datum | Betroffene Person | Art | Grund | Durchgeführt | Empfänger benachrichtigt | Bearbeiter |
|-------|------------------|-----|-------|--------------|-------------------------|------------|
| [TODO] | [TODO] | Berichtigung | Unrichtig | Ja | Ja | [TODO] |
| [TODO] | [TODO] | Löschung | Nicht erforderlich | Ja | Ja | [TODO] |
| [TODO] | [TODO] | Löschung | Abgelehnt (Aufbewahrungsfrist) | Nein | N/A | [TODO] |

### Nachweispflichten

**Dokumentation für Accountability:**
- Alle Berichtigungs- und Löschanträge
- Durchgeführte Berichtigungen und Löschungen
- Ablehnungen und deren Begründung
- Benachrichtigungen an Empfänger
- Ausnahmen und deren Begründung

## Fristen

**Bearbeitungsfrist:**
- Unverzüglich, spätestens 1 Monat
- Verlängerung um 2 Monate bei Komplexität möglich
- Begründung der Verlängerung erforderlich

## Verknüpfung zu anderen Dokumenten

- **Transparenz (Art. 12):** Modalitäten der Bearbeitung
- **Richtigkeit (Art. 5 Abs. 1 lit. d):** Grundsatz der Richtigkeit
- **Speicherbegrenzung (Art. 5 Abs. 1 lit. e):** Grundsatz der Löschung
- **Mitteilungspflicht (Art. 19):** Benachrichtigung von Empfängern
- **Einschränkung (Art. 18):** Alternative zur Löschung

## Häufige Verstöße und deren Vermeidung

| Verstoß | Beispiel | Vermeidung |
|---------|----------|------------|
| Unvollständige Berichtigung | Nur in einem System | Alle Systeme prüfen |
| Verzögerte Löschung | Löschung nach 3 Monaten | Fristenkontrolle |
| Fehlende Benachrichtigung | Empfänger nicht informiert | Benachrichtigungsprozess |
| Unbegründete Ablehnung | Ablehnung ohne Prüfung | Sorgfältige Prüfung |

**Nächste Schritte:**
1. Etablieren Sie Prozesse für Berichtigungs- und Löschanträge
2. Implementieren Sie Löschverfahren für alle Systeme
3. Definieren Sie Benachrichtigungsprozess für Empfänger
4. Schulen Sie Mitarbeiter zu Berichtigungs- und Löschrecht
5. Dokumentieren Sie alle Anträge im Register

