# Anhang: DSFA Quick Reference

**Dokument-ID:** GDPR-0710
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



## Wann ist eine DSFA erforderlich?

### Pflichtfälle (Art. 35 Abs. 3)

Eine DSFA ist **immer** erforderlich bei:

1. **Systematische und umfassende Bewertung persönlicher Aspekte**
   - Automatisierte Verarbeitung einschließlich Profiling
   - Grundlage für Entscheidungen mit Rechtswirkung oder erheblicher Beeinträchtigung

2. **Umfangreiche Verarbeitung besonderer Kategorien (Art. 9)**
   - Gesundheitsdaten, genetische Daten, biometrische Daten
   - Daten über strafrechtliche Verurteilungen und Straftaten

3. **Systematische umfangreiche Überwachung öffentlich zugänglicher Bereiche**
   - Videoüberwachung
   - Tracking und Monitoring

### Blacklist der Aufsichtsbehörden

Zusätzlich erforderlich bei (Beispiele):
- Scoring und Rating
- Automatisierte Entscheidungen mit Rechtswirkung
- Systematisches Monitoring
- Verarbeitung sensibler Daten in großem Umfang
- Datenabgleich oder Datenzusammenführung
- Daten vulnerabler Personen (Kinder, Patienten, Mitarbeiter)
- Innovative Technologien (KI, Biometrie)
- Drittlandübermittlung ohne Angemessenheitsbeschluss

### Schwellenwertkriterien

**Anzahl betroffener Personen:**
- < 5.000: Meist keine DSFA erforderlich
- 5.000 - 20.000: DSFA empfohlen
- > 20.000: DSFA meist erforderlich

**Risikofaktoren (je mehr zutreffen, desto eher DSFA):**
- [ ] Bewertung oder Scoring
- [ ] Automatisierte Entscheidungen
- [ ] Systematisches Monitoring
- [ ] Besondere Kategorien (Art. 9)
- [ ] Vulnerable Gruppen
- [ ] Umfangreiche Verarbeitung
- [ ] Datenabgleich
- [ ] Innovative Technologie
- [ ] Drittlandübermittlung
- [ ] Verhinderung von Rechtsausübung

**Faustregel:** Bei 2 oder mehr Risikofaktoren → DSFA durchführen

## DSFA-Prozess (Kurzübersicht)

### Phase 1: Vorbereitung

1. **Prüfen:** Ist DSFA erforderlich?
2. **Team bilden:** Verantwortlicher, Datenschutzbeauftragter, IT, Fachbereich
3. **Informationen sammeln:** Verarbeitungsbeschreibung, Datenflüsse, Systeme

### Phase 2: Durchführung

4. **Beschreibung:** Verarbeitung detailliert beschreiben
5. **Notwendigkeit:** Notwendigkeit und Verhältnismäßigkeit prüfen
6. **Risiken identifizieren:** Systematische Risikoanalyse
7. **Maßnahmen definieren:** Technische und organisatorische Maßnahmen
8. **Restrisiko bewerten:** Ist Restrisiko akzeptabel?

### Phase 3: Konsultation

9. **Datenschutzbeauftragter:** Stellungnahme einholen
10. **Betroffene (optional):** Ansichten einholen
11. **Aufsichtsbehörde (falls erforderlich):** Bei hohem Restrisiko konsultieren

### Phase 4: Dokumentation

12. **DSFA dokumentieren:** Template 0410 verwenden
13. **Genehmigung:** Verantwortlicher genehmigt
14. **Archivierung:** DSFA aufbewahren

## Risikobewertungsmatrix

### Eintrittswahrscheinlichkeit

| Stufe | Beschreibung | Beispiel |
|-------|--------------|----------|
| **Niedrig** | Unwahrscheinlich | Verschlüsselte Daten, starke Sicherheitsmaßnahmen |
| **Mittel** | Möglich | Standardsicherheit, bekannte Schwachstellen |
| **Hoch** | Wahrscheinlich | Schwache Sicherheit, öffentlich zugänglich |

### Schwere der Auswirkungen

| Stufe | Beschreibung | Beispiel |
|-------|--------------|----------|
| **Niedrig** | Geringe Beeinträchtigung | Allgemeine Kontaktdaten, keine sensiblen Daten |
| **Mittel** | Erhebliche Beeinträchtigung | Finanzdaten, Vertragsdaten |
| **Hoch** | Schwerwiegende Beeinträchtigung | Gesundheitsdaten, Identitätsdiebstahl möglich |

### Risikomatrix

|  | **Niedrige Schwere** | **Mittlere Schwere** | **Hohe Schwere** |
|---|---|---|---|
| **Niedrige Wahrscheinlichkeit** | Niedriges Risiko | Mittleres Risiko | Mittleres Risiko |
| **Mittlere Wahrscheinlichkeit** | Mittleres Risiko | Mittleres Risiko | Hohes Risiko |
| **Hohe Wahrscheinlichkeit** | Mittleres Risiko | Hohes Risiko | Sehr hohes Risiko |

**Handlungsempfehlung:**
- **Niedriges Risiko:** Standardmaßnahmen ausreichend
- **Mittleres Risiko:** Zusätzliche Maßnahmen erforderlich
- **Hohes Risiko:** Umfassende Maßnahmen, ggf. Konsultation Aufsichtsbehörde
- **Sehr hohes Risiko:** Konsultation Aufsichtsbehörde erforderlich

## Typische Maßnahmen

### Technische Maßnahmen

- **Verschlüsselung:** Ende-zu-Ende, Transport, Speicherung
- **Pseudonymisierung:** Trennung von Identifikationsdaten
- **Anonymisierung:** Irreversible Entfernung personenbezogener Daten
- **Zugriffskontrolle:** Rollenbasiert, Least Privilege
- **Logging:** Nachvollziehbarkeit, Audit-Trails
- **Backup:** Regelmäßig, getestet
- **Monitoring:** Anomalieerkennung, Intrusion Detection

### Organisatorische Maßnahmen

- **Richtlinien:** Datenschutzrichtlinie, Sicherheitsrichtlinie
- **Schulungen:** Regelmäßig, zielgruppenspezifisch
- **Verträge:** Auftragsverarbeiter-Verträge, NDAs
- **Prozesse:** Incident Response, Löschkonzept
- **Dokumentation:** Verarbeitungsverzeichnis, TOMs
- **Audits:** Regelmäßige Überprüfungen

### Privacy by Design/Default

- **Datenminimierung:** Nur notwendige Daten erheben
- **Zweckbindung:** Klare Zweckdefinition
- **Speicherbegrenzung:** Automatische Löschung
- **Transparenz:** Klare Informationen für Betroffene
- **Benutzerfreundlichkeit:** Einfache Ausübung von Rechten

## Checkliste: DSFA erforderlich?

- [ ] Systematische und umfassende Bewertung persönlicher Aspekte?
- [ ] Automatisierte Entscheidungen mit Rechtswirkung?
- [ ] Umfangreiche Verarbeitung besonderer Kategorien (Art. 9)?
- [ ] Systematische Überwachung öffentlich zugänglicher Bereiche?
- [ ] Scoring oder Rating?
- [ ] Verarbeitung sensibler Daten in großem Umfang?
- [ ] Datenabgleich oder Datenzusammenführung?
- [ ] Daten vulnerabler Personen (Kinder, Patienten)?
- [ ] Innovative Technologien (KI, Biometrie)?
- [ ] Drittlandübermittlung ohne Angemessenheitsbeschluss?
- [ ] Mehr als 20.000 betroffene Personen?
- [ ] 2 oder mehr Risikofaktoren treffen zu?

**Wenn 1 oder mehr Fragen mit Ja beantwortet:** DSFA durchführen!

## Vorherige Konsultation der Aufsichtsbehörde

**Erforderlich wenn:**
- Restrisiko trotz Maßnahmen hoch bleibt
- Keine angemessenen Maßnahmen möglich
- Unsicherheit über Angemessenheit der Maßnahmen

**Prozess:**
1. DSFA vollständig durchführen
2. Alle möglichen Maßnahmen dokumentieren
3. Anfrage an Aufsichtsbehörde mit DSFA-Dokumentation
4. Aufsichtsbehörde hat 8 Wochen Zeit (verlängerbar auf 14 Wochen)
5. Stellungnahme der Behörde umsetzen

## Häufige Fehler vermeiden

❌ **DSFA zu spät durchführen** → Vor Beginn der Verarbeitung!  
❌ **Oberflächliche Risikoanalyse** → Systematisch und detailliert!  
❌ **Datenschutzbeauftragten nicht einbeziehen** → Immer konsultieren!  
❌ **Keine konkreten Maßnahmen** → Spezifisch und umsetzbar!  
❌ **DSFA nicht aktualisieren** → Bei Änderungen überprüfen!  
❌ **Keine Dokumentation** → Vollständig dokumentieren!

## Nützliche Ressourcen

**Templates:**
- Template 0410: DSFA Template (Vorlage)
- Template 0400: DSFA Grundlagen

**Externe Ressourcen:**
- WP29 Guidelines on DPIA (wp248rev.01)
- Blacklist der Aufsichtsbehörden
- DSFA-Tools der Aufsichtsbehörden

**Kontakt:**
- Datenschutzbeauftragter: [TODO: Kontakt]
- Aufsichtsbehörde: [TODO: Kontakt]

