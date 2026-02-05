# Richtlinie: Datenschutz-Anforderungen und Datenverarbeitung

**Dokument-ID:** 0570  
**Dokumenttyp:** Richtlinie (detailliert)  
**Zugehörige Policy:** 0560_Policy_Datenschutz_Schnittstellen.md  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.34  
**Owner:** {{ meta.dpo.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}

---

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0560_Policy_Datenschutz_Schnittstellen.md` und definiert:
- DSGVO-Compliance-Anforderungen
- Datenverarbeitungsprozesse
- Betroffenenrechte und deren Umsetzung

**Geltungsbereich:** Alle personenbezogenen Daten bei **AdminSend GmbH**

## 2. DSGVO-Grundprinzipien

### 2.1 Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz

**Rechtsgrundlagen (Art. 6 DSGVO):**
- Einwilligung (Art. 6 Abs. 1 lit. a)
- Vertragserfüllung (Art. 6 Abs. 1 lit. b)
- Rechtliche Verpflichtung (Art. 6 Abs. 1 lit. c)
- Berechtigtes Interesse (Art. 6 Abs. 1 lit. f)

**Dokumentation:**
- Rechtsgrundlage für jede Verarbeitung dokumentieren
- Verzeichnis von Verarbeitungstätigkeiten (VVT)

### 2.2 Zweckbindung

**Prinzip:**
- Daten nur für festgelegte, eindeutige Zwecke erheben
- Keine Weiterverarbeitung für andere Zwecke (ohne neue Rechtsgrundlage)

### 2.3 Datenminimierung

**Prinzip:**
- Nur notwendige Daten erheben
- Regelmäßige Prüfung auf Erforderlichkeit

### 2.4 Richtigkeit

**Maßnahmen:**
- Daten aktuell halten
- Fehlerhafte Daten korrigieren
- Prozesse für Datenaktualisierung

### 2.5 Speicherbegrenzung

**Löschkonzept:**
- Aufbewahrungsfristen definieren
- Automatische Löschung nach Fristablauf
- Dokumentation der Löschung

**Details:** Siehe `0590_Richtlinie_Records_Retention_und_Sichere_Loeschung.md`

### 2.6 Integrität und Vertraulichkeit

**Technische Maßnahmen:**
- Verschlüsselung
- Zugriffskontrolle
- Logging und Monitoring

### 2.7 Rechenschaftspflicht

**Nachweispflicht:**
- Dokumentation aller Maßnahmen
- Datenschutz-Folgenabschätzung (DSFA)
- Verzeichnis von Verarbeitungstätigkeiten (VVT)

## 3. Verzeichnis von Verarbeitungstätigkeiten (VVT)

### 3.1 Pflichtangaben (Art. 30 DSGVO)

**Für jede Verarbeitung:**
- Name und Kontaktdaten des Verantwortlichen
- Zwecke der Verarbeitung
- Kategorien betroffener Personen
- Kategorien personenbezogener Daten
- Kategorien von Empfängern
- Drittlandübermittlungen
- Löschfristen
- Technische und organisatorische Maßnahmen (TOMs)

### 3.2 VVT-Pflege

**Verantwortlichkeit:**
- Datenschutzbeauftragter koordiniert
- Fachbereiche liefern Informationen
- Jährliche Aktualisierung (mindestens)

**Tool:** {{ meta.dpo.vvt_tool }}

## 4. Datenschutz-Folgenabschätzung (DSFA)

### 4.1 Wann erforderlich?

**Pflicht bei (Art. 35 DSGVO):**
- Systematische umfangreiche Bewertung persönlicher Aspekte (Profiling)
- Umfangreiche Verarbeitung besonderer Kategorien (Art. 9)
- Systematische umfangreiche Überwachung öffentlicher Bereiche

**Beispiele:**
- Neue CRM-Systeme mit Profiling
- Videoüberwachung
- Biometrische Authentifizierung

### 4.2 DSFA-Prozess

**Schritte:**
1. Beschreibung der Verarbeitung
2. Bewertung der Notwendigkeit und Verhältnismäßigkeit
3. Risikobewertung für Betroffene
4. Abhilfemaßnahmen
5. Konsultation des Datenschutzbeauftragten
6. Dokumentation

**Bei hohem Risiko:**
- Konsultation der Aufsichtsbehörde vor Verarbeitung

## 5. Betroffenenrechte

### 5.1 Auskunftsrecht (Art. 15 DSGVO)

**Prozess:**
1. Antrag per E-Mail an {{ meta.dpo.email }}
2. Identitätsprüfung
3. Zusammenstellung der Informationen
4. Antwort innerhalb 1 Monat

**Auszukunftende Informationen:**
- Verarbeitungszwecke
- Kategorien personenbezogener Daten
- Empfänger
- Speicherdauer
- Betroffenenrechte
- Kopie der Daten

### 5.2 Recht auf Berichtigung (Art. 16 DSGVO)

**Prozess:**
1. Antrag auf Berichtigung
2. Prüfung der Richtigkeit
3. Korrektur innerhalb 1 Monat
4. Benachrichtigung an Empfänger (falls erforderlich)

### 5.3 Recht auf Löschung (Art. 17 DSGVO)

**Löschgründe:**
- Zweck erfüllt
- Einwilligung widerrufen
- Widerspruch gegen Verarbeitung
- Unrechtmäßige Verarbeitung

**Ausnahmen:**
- Rechtliche Aufbewahrungspflichten
- Geltendmachung von Rechtsansprüchen

### 5.4 Recht auf Einschränkung (Art. 18 DSGVO)

**Einschränkung statt Löschung:**
- Bei Bestreitung der Richtigkeit
- Bei unrechtmäßiger Verarbeitung (Betroffener will keine Löschung)
- Bei Widerspruch (während Prüfung)

### 5.5 Recht auf Datenübertragbarkeit (Art. 20 DSGVO)

**Voraussetzungen:**
- Verarbeitung auf Einwilligung oder Vertrag
- Automatisierte Verarbeitung

**Format:**
- Strukturiert, gängig, maschinenlesbar (z.B. CSV, JSON)

### 5.6 Widerspruchsrecht (Art. 21 DSGVO)

**Bei berechtigtem Interesse:**
- Betroffener kann widersprechen
- Abwägung erforderlich
- Verarbeitung einstellen (außer zwingende Gründe)

**Bei Direktwerbung:**
- Widerspruch jederzeit möglich
- Verarbeitung sofort einstellen

## 6. Auftragsverarbeitung

### 6.1 Auftragsverarbeitungsvertrag (AVV)

**Pflicht bei:**
- Dienstleister verarbeitet personenbezogene Daten im Auftrag
- Cloud-Provider, IT-Dienstleister, etc.

**Pflichtinhalte (Art. 28 DSGVO):**
- Gegenstand und Dauer
- Art und Zweck der Verarbeitung
- Kategorien personenbezogener Daten
- Pflichten und Rechte des Verantwortlichen
- Technische und organisatorische Maßnahmen (TOMs)
- Sub-Auftragsverarbeiter
- Unterstützungspflichten

### 6.2 Technische und Organisatorische Maßnahmen (TOMs)

**Kategorien:**
- Zutrittskontrolle
- Zugangskontrolle
- Zugriffskontrolle
- Weitergabekontrolle
- Eingabekontrolle
- Auftragskontrolle
- Verfügbarkeitskontrolle
- Trennungskontrolle

**Dokumentation:**
- TOMs für jede Verarbeitung
- Regelmäßige Überprüfung und Anpassung

## 7. Datenschutzverletzungen (Data Breaches)

### 7.1 Meldepflicht (Art. 33 DSGVO)

**An Aufsichtsbehörde:**
- Innerhalb 72 Stunden nach Bekanntwerden
- Wenn Risiko für Betroffene

**Ausnahmen:**
- Kein Risiko für Betroffene (z.B. verschlüsselte Daten)

### 7.2 Benachrichtigung Betroffener (Art. 34 DSGVO)

**Pflicht bei:**
- Hohes Risiko für Betroffene
- Ohne unangemessene Verzögerung

**Inhalt:**
- Art der Verletzung
- Kontaktstelle (Datenschutzbeauftragter)
- Wahrscheinliche Folgen
- Ergriffene Maßnahmen

### 7.3 Dokumentation

**Verzeichnis von Datenschutzverletzungen:**
- Alle Verletzungen dokumentieren (auch nicht meldepflichtige)
- Sachverhalt, Auswirkungen, Abhilfemaßnahmen
- Nachweis für Aufsichtsbehörde

## 8. Internationale Datentransfers

### 8.1 Drittlandübermittlung

**Erlaubt bei:**
- Angemessenheitsbeschluss der EU-Kommission
- Standardvertragsklauseln (SCCs)
- Binding Corporate Rules (BCRs)
- Einwilligung

### 8.2 Schrems II Compliance

**Transfer Impact Assessment (TIA):**
- Rechtslage im Drittland prüfen
- Zusätzliche Maßnahmen implementieren (z.B. Verschlüsselung)
- Dokumentation

## 9. Compliance und Audit

### 9.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Betroffenenanfragen (Antwortzeit) | < 1 Monat |
| VVT-Aktualität | < 12 Monate |
| DSFA-Completion (neue Systeme) | 100% |
| Datenschutzverletzungen (Meldung) | < 72 Stunden |

### 9.2 Audit-Nachweise

- Verzeichnis von Verarbeitungstätigkeiten (VVT)
- Datenschutz-Folgenabschätzungen (DSFA)
- Auftragsverarbeitungsverträge (AVV)
- Betroffenenanfragen und -antworten
- Verzeichnis von Datenschutzverletzungen

## 10. Referenzen

### Interne Dokumente
- `0560_Policy_Datenschutz_Schnittstellen.md`
- `0590_Richtlinie_Records_Retention_und_Sichere_Loeschung.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.34** - Privacy and protection of PII
- **DSGVO (EU 2016/679)** - Datenschutz-Grundverordnung
- **BDSG** - Bundesdatenschutzgesetz

---

**Genehmigt durch:** {{ meta.dpo.name }}, Datenschutzbeauftragter  
**Nächster Review:** {{ meta.document.next_review }}
