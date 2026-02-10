# Business Associates und Subunternehmer

**Dokument-ID:** HIPAA-0030  
**Organisation:** AdminSend GmbH  
**Verantwortlich:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Prüfung / Genehmigt  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---



## 1. Zweck

Dieses Dokument identifiziert und verwaltet alle Business Associate-Beziehungen für AdminSend GmbH und stellt die Einhaltung der HIPAA Business Associate-Anforderungen sicher.

### 1.1 Zielsetzungen

- **BA-Identifikation:** Alle Entitäten identifizieren, die die Business Associate-Definition erfüllen
- **BAA-Verwaltung:** Sicherstellen, dass gültige Business Associate Agreements vorhanden sind
- **Compliance-Überwachung:** BA-Compliance mit HIPAA-Anforderungen überwachen
- **Subunternehmer-Aufsicht:** Subunternehmer-Beziehungen verfolgen und verwalten

### 1.2 Referenzen

- **HIPAA Privacy Rule**: 45 CFR §164.502(e), §164.504(e)
- **HIPAA Security Rule**: 45 CFR §164.308(b)
- **HIPAA Breach Notification Rule**: 45 CFR §164.410
- **HITECH Act**: Business Associate-Haftungsbestimmungen

## 2. Business Associate-Definition

### 2.1 Was ist ein Business Associate?

Ein Business Associate ist eine Person oder Entität, die:
1. Funktionen oder Aktivitäten im Namen einer Covered Entity ausführt oder Dienstleistungen für diese erbringt
2. Die Nutzung oder Offenlegung von PHI beinhaltet
3. Nicht Teil der Belegschaft der Covered Entity ist

### 2.2 Häufige Business Associate-Funktionen

**Business Associate-Dienstleistungen umfassen:**
- Anspruchsbearbeitung oder -verwaltung
- Datenanalyse, -verarbeitung oder -verwaltung
- Nutzungsüberprüfung
- Qualitätssicherung
- Abrechnung, Leistungsverwaltung, Praxisverwaltung
- Neubepreisungsdienste oder andere Dienstleistungen
- Rechts-, versicherungsmathematische, buchhalterische, beratende, Datenaggregations-, Verwaltungs-, administrative, Akkreditierungs- oder Finanzdienstleistungen

**Beispiele für Business Associates:**
- Drittverwalter
- Abrechnungsunternehmen
- IT-Dienstleister (mit PHI-Zugriff)
- Cloud-Speicheranbieter
- Aktenvernichtungsunternehmen
- Rechtsanwälte (mit PHI-Zugriff)
- Berater (mit PHI-Zugriff)
- Datenanalysefirmen

### 2.3 Entitäten, die KEINE Business Associates sind

**Conduit-Ausnahme:**
- Telekommunikationsunternehmen
- Internet Service Provider (ISPs)
- Postdienste
- Kurierdienste (wenn nur versiegelte PHI transportiert wird)

**Andere Ausnahmen:**
- Belegschaftsmitglieder
- Gesundheitsdienstleister in Behandlungsbeziehung
- Krankenversicherungsmitglieder
- Gruppenkrankenversicherungs-Sponsoren (mit bestimmten Einschränkungen)

## 3. Business Associate-Inventar

### 3.1 Aktuelle Business Associates

| BA-ID | Business Associate-Name | Bereitgestellte Dienstleistung | PHI-Zugriffstyp | BAA-Status | BAA-Datum | Prüfungsdatum |
|-------|------------------------|-------------------------------|-----------------|------------|-----------|---------------|
| [TODO: BA-001] | [TODO: IT-Support-Anbieter] | IT-Support und -Wartung | ePHI-Zugriff | [TODO: Aktiv] | [TODO: 2024-01-15] | [TODO: 2027-01-15] |
| [TODO: BA-002] | [TODO: Abrechnungsdienst] | Medizinische Abrechnung | PHI-Verarbeitung | [TODO: Aktiv] | [TODO: 2023-06-01] | [TODO: 2026-06-01] |
| [TODO: BA-003] | [TODO: Cloud-Anbieter] | Daten-Hosting | ePHI-Speicherung | [TODO: Aktiv] | [TODO: 2025-03-10] | [TODO: 2028-03-10] |

### 3.2 Business Associate-Details

**BA-001: [TODO: IT-Support-Anbieter]**
- **Kontaktperson:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]
- **Adresse:** [TODO: Adresse]
- **Dienstleistungen:** [TODO: Detaillierte Beschreibung]
- **PHI-Zugriff:** [TODO: Zugriffssysteme, Zugriffstyp]
- **Subunternehmer:** [TODO: Ja/Nein, auflisten falls ja]
- **Versicherung:** [TODO: Cyber-Haftpflichtdeckung Betrag]
- **Compliance-Bestätigung:** [TODO: Datum der letzten Bestätigung]

## 4. Business Associate Agreements (BAAs)

### 4.1 BAA-Anforderungen

**Erforderliche BAA-Bestimmungen (45 CFR §164.504(e)):**

1. **Zulässige Nutzungen und Offenlegungen:**
   - Zulässige Nutzungen und Offenlegungen von PHI spezifizieren
   - Nutzungen/Offenlegungen auf vertraglich oder gesetzlich erforderliche beschränken

2. **Schutzmaßnahmen:**
   - Angemessene Schutzmaßnahmen zur Verhinderung unbefugter Nutzung/Offenlegung implementieren
   - Security Rule für ePHI einhalten

3. **Subunternehmer-Anforderungen:**
   - Sicherstellen, dass Subunternehmer denselben Beschränkungen zustimmen
   - Zufriedenstellende Zusicherungen von Subunternehmern einholen

4. **Berichterstattung:**
   - Unbefugte Nutzungen/Offenlegungen an Covered Entity melden
   - Sicherheitsvorfälle melden
   - Verstöße gegen ungesicherte PHI melden

5. **Individuelle Rechte:**
   - PHI für Zugriffsanfragen verfügbar machen
   - PHI für Änderungsanfragen verfügbar machen
   - Rechenschaft über Offenlegungen ablegen

6. **Compliance:**
   - Interne Praktiken, Bücher und Aufzeichnungen für HHS-Compliance-Prüfung verfügbar machen
   - PHI bei Beendigung zurückgeben oder vernichten (falls machbar)

7. **Beendigung:**
   - Beendigung autorisieren, wenn BA wesentliche Bedingung verletzt
   - PHI-Disposition bei Beendigung spezifizieren

### 4.2 BAA-Vorlage

**Standard-BAA-Vorlagenstandort:** [TODO: Dateipfad oder Dokumentenmanagementsystem-Standort]

**BAA-Vorlagenversion:** [TODO: Versionsnummer und Datum]

**Vorlagengenehmigung:**
- **Genehmigt durch Rechtsabteilung:** [TODO: Ja/Nein, Datum]
- **Genehmigt durch Privacy Officer:** [TODO: Ja/Nein, Datum]
- **Genehmigt durch Compliance:** [TODO: Ja/Nein, Datum]

### 4.3 BAA-Ausführungsprozess

**Prozessschritte:**
1. Bedarf für Business Associate-Beziehung identifizieren
2. BA-Due-Diligence und Risikobewertung durchführen
3. Dienstleistungsvereinbarung aushandeln
4. Business Associate Agreement ausführen
5. BAA im Inventar dokumentieren
6. BA-Compliance überwachen
7. BAA regelmäßig überprüfen (mindestens alle 3 Jahre)

**Genehmigungsbefugnis:**
- **Dienstleistungen < 10.000 $:** [TODO: Abteilungsleiter]
- **Dienstleistungen 10.000-50.000 $:** [TODO: Direktor + Privacy Officer]
- **Dienstleistungen > 50.000 $:** [TODO: Geschäftsführung + Privacy Officer + Rechtsabteilung]

## 5. Subunternehmer-Verwaltung

### 5.1 Subunternehmer-Anforderungen

**HIPAA-Anforderungen für Subunternehmer:**
- Business Associates müssen zufriedenstellende Zusicherungen von Subunternehmern einholen
- Subunternehmer müssen BAA mit Business Associate abschließen
- Subunternehmer haben dieselben HIPAA-Verpflichtungen wie Business Associates
- Covered Entity muss über Subunternehmer-Vereinbarungen benachrichtigt werden

### 5.2 Subunternehmer-Inventar

| Subunternehmer | Primärer BA | Dienstleistung | PHI-Zugriff | BAA mit BA | CE benachrichtigt |
|----------------|-------------|----------------|-------------|------------|-------------------|
| [TODO: Cloud-Backup-Anbieter] | [TODO: IT-Anbieter] | Datensicherung | ePHI | [TODO: Ja] | [TODO: Ja, Datum] |
| [TODO: Offshore-Support] | [TODO: IT-Anbieter] | Help Desk | ePHI | [TODO: Ja] | [TODO: Ja, Datum] |

### 5.3 Subunternehmer-Genehmigungsprozess

**Covered Entity-Genehmigung erforderlich:** [TODO: Ja/Nein]

**Genehmigungsprozess:**
1. Business Associate beantragt Genehmigung zur Nutzung von Subunternehmern
2. BA stellt Subunternehmer-Informationen und vorgeschlagenes BAA bereit
3. Privacy Officer prüft Subunternehmer-Vereinbarung
4. Genehmigung erteilt oder abgelehnt innerhalb [TODO: 10 Werktage]
5. BA führt BAA mit Subunternehmer aus
6. BA stellt Kopie des ausgeführten BAA an Covered Entity bereit

## 6. Business Associate Due Diligence

### 6.1 Bewertung vor Vertragsabschluss

**Due Diligence-Checkliste:**
- [ ] Business Associate-Fragebogen ausgefüllt
- [ ] HIPAA-Compliance-Bestätigung erhalten
- [ ] Sicherheitskontroll-Dokumentation geprüft
- [ ] Incident Response-Plan geprüft
- [ ] Breach Notification-Verfahren geprüft
- [ ] Versicherungsschutz verifiziert (Cyber-Haftpflicht)
- [ ] Referenzen geprüft
- [ ] Finanzielle Stabilität bewertet
- [ ] Subunternehmer-Liste bereitgestellt

**Risikobewertung:**
| Risikofaktor | Bewertung | Minderung |
|-------------|-----------|-----------|
| [TODO: Datenvolumen] | [TODO: Hoch/Mittel/Niedrig] | [TODO: Minderungsmaßnahmen] |
| [TODO: PHI-Sensibilität] | [TODO: Hoch/Mittel/Niedrig] | [TODO: Minderungsmaßnahmen] |
| [TODO: Sicherheitsreife] | [TODO: Hoch/Mittel/Niedrig] | [TODO: Minderungsmaßnahmen] |

### 6.2 Laufende Überwachung

**Überwachungsaktivitäten:**
- Jährliche Compliance-Bestätigung
- Regelmäßige Sicherheitsbewertungen
- Breach Notification-Verfolgung
- Vorfallsprüfung
- Leistungsüberprüfungen
- Vertragskonformitätsprüfungen

**Überwachungsplan:**
| Aktivität | Häufigkeit | Verantwortliche Partei | Zuletzt abgeschlossen |
|----------|-----------|------------------------|----------------------|
| [TODO: Compliance-Bestätigung] | Jährlich | [TODO: Privacy Officer] | [TODO: Datum] |
| [TODO: Sicherheitsbewertung] | Jährlich | [TODO: Security Officer] | [TODO: Datum] |
| [TODO: Leistungsüberprüfung] | Vierteljährlich | [TODO: Vertragsmanager] | [TODO: Datum] |

## 7. Breach Notification von Business Associates

### 7.1 BA Breach Notification-Anforderungen

**Business Associates müssen Covered Entity benachrichtigen:**
- **Zeitrahmen:** Ohne unangemessene Verzögerung, spätestens 60 Tage nach Entdeckung
- **Methode:** Schriftliche Benachrichtigung (E-Mail akzeptabel)
- **Inhalt:** 
  - Identifizierung jeder betroffenen Person
  - Beschreibung des Verstoßes
  - Arten der beteiligten PHI
  - Datum des Verstoßes und Entdeckungsdatum
  - Schritte, die Personen unternehmen sollten
  - Untersuchungs- und Minderungsbemühungen des BA

### 7.2 Breach Notification-Protokoll

| Verstoß-ID | BA-Name | Entdeckungsdatum | Benachrichtigungsdatum | Betroffene Personen | Beteiligte PHI | Status |
|-----------|---------|------------------|------------------------|---------------------|----------------|--------|
| [TODO: BR-001] | [TODO: BA-Name] | [TODO: Datum] | [TODO: Datum] | [TODO: Anzahl] | [TODO: Typen] | [TODO: Gelöst] |

### 7.3 Breach Response-Prozess

**Bei Erhalt einer BA Breach Notification:**
1. Empfang der Benachrichtigung bestätigen
2. Bei Bedarf zusätzliche Informationen anfordern
3. Verstoß auf Meldepflichten bewerten
4. Betroffene Personen benachrichtigen (falls erforderlich)
5. HHS benachrichtigen (falls erforderlich)
6. Medien benachrichtigen (falls erforderlich - 500+ Personen)
7. Verstoß und Reaktion dokumentieren
8. BA-Beziehung und Kontrollen überprüfen

## 8. Business Associate-Beendigung

### 8.1 Beendigungsauslöser

**Gründe für Beendigung:**
- Wesentlicher Verstoß gegen BAA
- Versäumnis, Verstoß innerhalb festgelegter Frist zu beheben
- Wiederholte Sicherheitsvorfälle
- Versäumnis, Verstöße zu melden
- Insolvenz oder Konkurs
- Ende der Dienstleistungsbeziehung

### 8.2 Beendigungsprozess

**Beendigungsschritte:**
1. Schriftliche Beendigungsmitteilung bereitstellen
2. Beendigungsdatum angeben
3. Rückgabe oder Vernichtung von PHI anfordern
4. PHI-Rückgabe/-Vernichtung verifizieren
5. Vernichtungszertifikat einholen (falls zutreffend)
6. Business Associate-Inventar aktualisieren
7. Betroffene Systeme/Abteilungen benachrichtigen
8. Nachbeendigungsprüfung durchführen

### 8.3 PHI-Disposition

**Optionen bei Beendigung:**
- **PHI zurückgeben:** BA gibt alle PHI an Covered Entity zurück
- **PHI vernichten:** BA vernichtet PHI und stellt Zertifikat bereit
- **PHI aufbewahren:** Falls Rückgabe/Vernichtung nicht machbar, behält BA PHI mit fortgesetztem Schutz

**Aufbewahrungsbegründung:** [TODO: Gründe dokumentieren, falls PHI-Aufbewahrung erforderlich ist]

## 9. Compliance und Audit

### 9.1 BA-Compliance-Überwachung

**Überwachungsmethoden:**
- Jährliche Compliance-Bestätigungen
- Vor-Ort-Audits (falls vertraglich gestattet)
- Sicherheitsbewertungen
- Penetrationstestergebnisse-Prüfung
- SOC 2-Berichte-Prüfung
- ISO 27001-Zertifizierungen-Prüfung

**Audit-Rechte:**
- Covered Entity behält sich das Recht vor, BA-Compliance zu prüfen
- Audit-Häufigkeit: [TODO: Jährlich oder nach Bedarf]
- Audit-Umfang: HIPAA-Compliance, Sicherheitskontrollen, BAA-Compliance

### 9.2 Dokumentation und Aufzeichnungen

**Erforderliche Dokumentation:**
- Ausgeführte Business Associate Agreements
- Due Diligence-Bewertungen
- Compliance-Bestätigungen
- Breach Notifications
- Audit-Berichte
- Korrespondenz bezüglich PHI

**Aufbewahrungsfrist:** [TODO: 6 Jahre ab Erstellung oder letztem Gültigkeitsdatum]

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Ersterstellung |


