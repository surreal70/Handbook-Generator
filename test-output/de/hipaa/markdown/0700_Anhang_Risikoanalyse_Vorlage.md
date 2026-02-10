# Anhang: Risikoanalyse-Vorlage

**Dokument-ID:** HIPAA-0700  
**Organisation:** AdminSend GmbH  
**Verantwortlich:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Prüfung / Genehmigt  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Zweck

Dieser Anhang bietet eine Vorlage zur Durchführung einer HIPAA Security Rule-Risikoanalyse gemäß §164.308(a)(1)(ii)(A).

## 2. Risikoanalyse-Vorlage

### 2.1 Umfangsdefinition

**ePHI-Inventar:**
| Datenelement | Format | Speicherort | Zugriffskontrollen | Verschlüsselung |
|--------------|--------|-------------|---------------------|-----------------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 2.2 Bedrohungs- und Schwachstellenbewertung

| Bedrohung | Schwachstelle | Wahrscheinlichkeit | Auswirkung | Risikostufe | Minderung |
|-----------|---------------|-------------------|------------|-------------|-----------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 2.3 Risikobehandlungsplan

| Risiko-ID | Behandlung | Kontrollen | Zeitplan | Verantwortlich | Status |
|-----------|------------|------------|----------|----------------|--------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Ersterstellung |


**Beispiel-ePHI-Inventar:**
| Datenelement | Format | Speicherort | Zugriffskontrollen | Verschlüsselung |
|--------------|--------|-------------|---------------------|-----------------|
| Patientendemografie | Elektronisch | EHR-Datenbank | Rollenbasiert, MFA | TDE, AES-256 |
| Klinische Notizen | Elektronisch | EHR-Datenbank | Rollenbasiert, MFA | TDE, AES-256 |
| Laborergebnisse | Elektronisch | Labor-System | Rollenbasiert | TDE, AES-256 |
| Bildgebungsstudien | Elektronisch | PACS | Rollenbasiert | AES-256 |
| Abrechnungsdaten | Elektronisch | Abrechnungssystem | Rollenbasiert | TDE, AES-256 |

**Systeminventar:**
| System | Zweck | ePHI-Typ | Standort | Kritikalität |
|--------|-------|----------|----------|--------------|
| EHR-System | Patientenakten | Alle PHI | Rechenzentrum | Kritisch |
| Labor-System | Laborergebnisse | Laborwerte | Rechenzentrum | Hoch |
| PACS | Medizinische Bildgebung | Bilder, Berichte | Rechenzentrum | Hoch |
| Abrechnungssystem | Abrechnung | Demografische, Abrechnungsdaten | Rechenzentrum | Hoch |

**Bedrohungskategorien:**
1. **Externe Bedrohungen:** Hacker, Malware, Ransomware
2. **Interne Bedrohungen:** Böswillige Insider, fahrlässige Mitarbeiter
3. **Naturkatastrophen:** Feuer, Überschwemmung, Erdbeben
4. **Technische Ausfälle:** Hardware-Ausfall, Software-Fehler
5. **Menschliches Versagen:** Versehentliche Offenlegung, Konfigurationsfehler

**Beispiel-Bedrohungs- und Schwachstellenmatrix:**
| Bedrohung | Schwachstelle | Wahrscheinlichkeit | Auswirkung | Risikostufe | Minderung |
|-----------|---------------|-------------------|------------|-------------|-----------|
| Ransomware-Angriff | Ungepatchte Systeme | Mittel | Hoch | Hoch | Patch-Management, EDR, Backups |
| Unbefugter Zugriff | Schwache Passwörter | Hoch | Mittel | Hoch | MFA, Passwortrichtlinie |
| Datenverlust | Fehlende Backups | Niedrig | Hoch | Mittel | Backup-Strategie, Tests |
| Insider-Bedrohung | Übermäßige Berechtigungen | Mittel | Hoch | Hoch | Least Privilege, Überwachung |
| Phishing | Ungeschulte Mitarbeiter | Hoch | Mittel | Hoch | Schulung, E-Mail-Filterung |

**Wahrscheinlichkeitsskala:**
- **Niedrig:** Unwahrscheinlich innerhalb von 3 Jahren
- **Mittel:** Möglich innerhalb von 3 Jahren
- **Hoch:** Wahrscheinlich innerhalb von 1 Jahr

**Auswirkungsskala:**
- **Niedrig:** Minimale Auswirkung auf Vertraulichkeit, Integrität, Verfügbarkeit
- **Mittel:** Moderate Auswirkung, begrenzte PHI-Offenlegung
- **Hoch:** Schwerwiegende Auswirkung, umfangreiche PHI-Offenlegung

**Risikobehandlungsoptionen:**
1. **Mindern:** Kontrollen implementieren, um Risiko zu reduzieren
2. **Übertragen:** Risiko auf Dritte übertragen (Versicherung)
3. **Vermeiden:** Aktivität einstellen, die Risiko verursacht
4. **Akzeptieren:** Risiko akzeptieren (mit Genehmigung)

**Beispiel-Risikobehandlungsplan:**
| Risiko-ID | Risiko | Behandlung | Kontrollen | Zeitplan | Verantwortlich | Status | Kosten |
|-----------|--------|------------|------------|----------|----------------|--------|--------|
| R-001 | Ransomware | Mindern | EDR, Backups, Patch-Management | Q1 2024 | IT Security | In Arbeit | €50.000 |
| R-002 | Schwache Passwörter | Mindern | MFA, Passwortrichtlinie | Q1 2024 | IT | Abgeschlossen | €10.000 |
| R-003 | Datenverlust | Mindern | Backup-Strategie, Offsite-Backups | Q2 2024 | IT | Geplant | €30.000 |
| R-004 | Insider-Bedrohung | Mindern | Least Privilege, SIEM, UBA | Q2 2024 | IT Security | Geplant | €40.000 |

### 2.4 Kontrollbewertung

**Bestehende Kontrollen:**
| Kontroll-ID | Kontrollname | Typ | Implementiert | Effektiv | Lücken |
|-------------|--------------|-----|---------------|----------|--------|
| AC-001 | Eindeutige Benutzer-IDs | Technisch | Ja | Ja | Keine |
| AC-002 | Multi-Faktor-Authentifizierung | Technisch | Teilweise | Teilweise | Nicht für alle Systeme |
| AC-003 | Automatische Abmeldung | Technisch | Ja | Ja | Keine |
| PE-001 | Physische Zugangskontrollen | Physisch | Ja | Teilweise | Einige Bereiche ungesichert |
| AD-001 | Zugriffsautorisierung | Administrativ | Ja | Teilweise | Inkonsistente Durchsetzung |

### 2.5 Gap-Analyse

**Identifizierte Lücken:**
| Lücken-ID | Beschreibung | Betroffene Systeme | Risikostufe | Empfohlene Maßnahme | Priorität |
|-----------|--------------|-------------------|-------------|---------------------|-----------|
| G-001 | MFA nicht für alle Systeme | Labor-System, PACS | Hoch | MFA implementieren | Hoch |
| G-002 | Ungesicherte physische Bereiche | Lagerräume | Mittel | Zugangskontrollen hinzufügen | Mittel |
| G-003 | Inkonsistente Zugriffsautorisierung | Alle Systeme | Hoch | Prozess standardisieren | Hoch |
| G-004 | Niedrige Schulungsabschlussrate | Organisation | Mittel | Schulungsprogramm verbessern | Mittel |

## 3. Risikoanalyse-Methodik

### 3.1 Risikoanalyse-Ansatz

**Methodik:**
- **Qualitativ:** Beschreibende Bewertung (Niedrig, Mittel, Hoch)
- **Quantitativ:** Numerische Bewertung (z.B. ALE - Annual Loss Expectancy)
- **Hybrid:** Kombination aus qualitativ und quantitativ

### 3.2 Risikoanalyse-Prozess

**10-Schritte-Prozess:**
1. **Vorbereitung:** Umfang definieren, Team zusammenstellen
2. **Informationssammlung:** ePHI-Inventar, Systeminventar erstellen
3. **Bedrohungsidentifikation:** Externe und interne Bedrohungen identifizieren
4. **Schwachstellenidentifikation:** Technische, physische, administrative Schwachstellen
5. **Kontrollanalyse:** Bestehende Kontrollen bewerten
6. **Wahrscheinlichkeitsbestimmung:** Wahrscheinlichkeit für jede Bedrohung
7. **Auswirkungsanalyse:** Auswirkung auf Vertraulichkeit, Integrität, Verfügbarkeit
8. **Risikobestimmung:** Risikostufe berechnen
9. **Kontrollempfehlungen:** Kontrollen zur Risikominderung empfehlen
10. **Dokumentation:** Risikoanalysebericht erstellen

### 3.3 Risikoanalyse-Häufigkeit

**Regelmäßige Überprüfungen:**
- Jährlich (Minimum)
- Bei wesentlichen Änderungen
- Nach Sicherheitsvorfällen
- Bei neuen Bedrohungen

## 4. Anhänge

### 4.1 Anhang A: Risikoanalyse-Checkliste

**Vorbereitungsphase:**
- [ ] Umfang definiert
- [ ] Team zusammengestellt
- [ ] Ressourcen zugewiesen
- [ ] Zeitplan erstellt

**Informationssammlungsphase:**
- [ ] ePHI-Inventar erstellt
- [ ] Systeminventar erstellt
- [ ] Netzwerkdiagramme überprüft
- [ ] Richtlinien überprüft
- [ ] Interviews durchgeführt

**Bewertungsphase:**
- [ ] Bedrohungen identifiziert
- [ ] Schwachstellen identifiziert
- [ ] Kontrollen bewertet
- [ ] Wahrscheinlichkeit bestimmt
- [ ] Auswirkung analysiert
- [ ] Risiken berechnet

**Berichtsphase:**
- [ ] Bericht erstellt
- [ ] Überprüft
- [ ] Genehmigt
- [ ] Verteilt

### 4.2 Anhang B: Glossar

**Begriffe:**
- **ePHI:** Elektronisch geschützte Gesundheitsinformationen
- **Bedrohung:** Potenzielle Ursache eines unerwünschten Vorfalls
- **Schwachstelle:** Schwäche, die von Bedrohung ausgenutzt werden kann
- **Risiko:** Wahrscheinlichkeit, dass Bedrohung Schwachstelle ausnutzt
- **Kontrolle:** Schutzmaßnahme zur Risikominderung
- **Wahrscheinlichkeit:** Chance, dass Ereignis eintritt
- **Auswirkung:** Schaden, wenn Ereignis eintritt
- **Risikostufe:** Kombination aus Wahrscheinlichkeit und Auswirkung

