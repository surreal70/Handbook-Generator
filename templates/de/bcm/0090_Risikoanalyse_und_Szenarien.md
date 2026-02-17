# Risikoanalyse und Szenarien

**Dokument-ID:** BCM-0090
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines risk analysis and disaster scenarios for BCM.
It aligns with ISO 22301:2019 Clause 8.2.3 (Business continuity strategy) and BSI Standard 200-4.

Customization required:
- Identify relevant disaster scenarios for your organization
- Assess probability and impact for each scenario
- Define risk treatment measures
- Establish risk tolerance thresholds
-->

## 1. Ziel

Die Risikoanalyse der {{ meta-organisation.name }} dient der:

- **Identifikation** von Risiken, die die Geschäftskontinuität beeinträchtigen können
- **Bewertung** der Eintrittswahrscheinlichkeit und Auswirkungen
- **Behandlung** durch geeignete Maßnahmen (Vermeidung, Reduktion, Transfer, Akzeptanz)
- **Überwachung** und regelmäßigen Überprüfung der Risiken

Die Risikoanalyse ergänzt die Business Impact Analysis (BIA) und bildet die Grundlage für die BCM-Strategie.

## 2. Szenario-Katalog

### 2.1 IT- und Cyber-Risiken

**2.1.1 Cyberangriff / Ransomware**
- **Beschreibung:** Verschlüsselung von Daten durch Ransomware, Erpressung
- **Betroffene Services:** Alle IT-abhängigen Prozesse
- **Typische Auswirkungen:** Datenverlust, Systemausfall, Erpressungszahlung
- **Referenz:** BSI-Standard 200-4, Abschnitt Cyber-Resilience

**2.1.2 Ausfall Rechenzentrum / Cloud-Region**
- **Beschreibung:** Komplettausfall des primären Rechenzentrums oder Cloud-Region
- **Betroffene Services:** Alle IT-Services
- **Typische Auswirkungen:** Totalausfall IT-Systeme, Datenzugriff nicht möglich

**2.1.3 Netzwerkausfall / Internet-Ausfall**
- **Beschreibung:** Ausfall der Netzwerkinfrastruktur oder Internet-Anbindung
- **Betroffene Services:** Alle netzwerkabhängigen Services
- **Typische Auswirkungen:** Keine Kommunikation, kein Datenzugriff

**2.1.4 Datenverlust / Backup-Ausfall**
- **Beschreibung:** Verlust kritischer Daten, Backup nicht wiederherstellbar
- **Betroffene Services:** Datenabhängige Prozesse
- **Typische Auswirkungen:** Permanenter Datenverlust, RPO-Überschreitung

### 2.2 Infrastruktur-Risiken

**2.2.1 Stromausfall**
- **Beschreibung:** Ausfall der Stromversorgung am Standort
- **Betroffene Services:** Alle stromabhängigen Systeme und Prozesse
- **Typische Auswirkungen:** Produktionsausfall, IT-Ausfall, Gebäudetechnik-Ausfall

**2.2.2 Brand**
- **Beschreibung:** Feuer im Gebäude oder Rechenzentrum
- **Betroffene Services:** Alle Services am betroffenen Standort
- **Typische Auswirkungen:** Standort nicht nutzbar, Sachschäden, Personengefährdung

**2.2.3 Wasserschaden**
- **Beschreibung:** Überschwemmung, Rohrbruch, Löschwasser
- **Betroffene Services:** Services am betroffenen Standort
- **Typische Auswirkungen:** Gebäudeschäden, IT-Hardware-Schäden

**2.2.4 Standort nicht zugänglich**
- **Beschreibung:** Evakuierung, Sperrung, Naturereignis
- **Betroffene Services:** Alle standortabhängigen Prozesse
- **Typische Auswirkungen:** Mitarbeiter können nicht arbeiten, Produktion steht still

### 2.3 Personal-Risiken

**2.3.1 Personalausfall / Pandemie**
- **Beschreibung:** Krankheitswelle, Pandemie, Massenausfall
- **Betroffene Services:** Personalintensive Prozesse
- **Typische Auswirkungen:** Reduzierte Kapazität, Schlüsselpersonen nicht verfügbar

**2.3.2 Ausfall Schlüsselpersonen**
- **Beschreibung:** Langfristiger Ausfall von Personen mit Spezialwissen
- **Betroffene Services:** Prozesse mit Wissensabhängigkeiten
- **Typische Auswirkungen:** Prozesse können nicht durchgeführt werden

### 2.4 Lieferanten-Risiken

**2.4.1 Lieferantenausfall**
- **Beschreibung:** Kritischer Lieferant kann nicht liefern
- **Betroffene Services:** Produktions- und Beschaffungsprozesse
- **Typische Auswirkungen:** Produktionsstopp, Lieferengpässe

**2.4.2 IT-Dienstleister-Ausfall**
- **Beschreibung:** Ausfall eines kritischen IT-Dienstleisters oder Cloud-Providers
- **Betroffene Services:** Ausgelagerte IT-Services
- **Typische Auswirkungen:** Service nicht verfügbar, keine Alternative

### 2.5 Naturereignisse und Umwelt

**2.5.1 Unwetter / Sturm**
- **Beschreibung:** Schwere Unwetter, Sturm, Hagel
- **Betroffene Services:** Standortabhängige Prozesse, Logistik
- **Typische Auswirkungen:** Gebäudeschäden, Verkehrswege blockiert

**2.5.2 Hochwasser**
- **Beschreibung:** Überschwemmung durch Fluss oder Starkregen
- **Betroffene Services:** Standortabhängige Prozesse
- **Typische Auswirkungen:** Standort überflutet, massive Sachschäden

**2.5.3 Erdbeben** (je nach Standort)
- **Beschreibung:** Seismisches Ereignis
- **Betroffene Services:** Alle Services am Standort
- **Typische Auswirkungen:** Gebäudeschäden, Infrastrukturausfall

[TODO: Ergänzen oder streichen Sie Szenarien entsprechend Ihrer Standorte und Risiken]

## 3. Bewertungsmethodik

### 3.1 Bewertungsschema

**Eintrittswahrscheinlichkeit (1-5):**
| Stufe | Bezeichnung | Beschreibung | Häufigkeit |
|-------|-------------|--------------|------------|
| 5 | Sehr hoch | Tritt regelmäßig ein | Mehrmals pro Jahr |
| 4 | Hoch | Tritt gelegentlich ein | Einmal pro Jahr |
| 3 | Mittel | Kann eintreten | Einmal in 1-5 Jahren |
| 2 | Niedrig | Unwahrscheinlich | Einmal in 5-10 Jahren |
| 1 | Sehr niedrig | Sehr unwahrscheinlich | Seltener als alle 10 Jahre |

**Auswirkung (1-5):**
| Stufe | Bezeichnung | Beschreibung | Finanzielle Auswirkung |
|-------|-------------|--------------|----------------------|
| 5 | Katastrophal | Existenzbedrohend | > 1 Mio. € |
| 4 | Sehr hoch | Massive Auswirkungen | 500.000 - 1 Mio. € |
| 3 | Hoch | Erhebliche Auswirkungen | 100.000 - 500.000 € |
| 2 | Mittel | Spürbare Auswirkungen | 10.000 - 100.000 € |
| 1 | Niedrig | Geringe Auswirkungen | < 10.000 € |

**Risiko-Score:**
- Risiko-Score = Eintrittswahrscheinlichkeit × Auswirkung
- Wertebereich: 1-25

### 3.2 Risikotoleranz und Schwellwerte

[TODO: Definieren Sie Ihre Risikotoleranz]

**Beispiel:**

| Risiko-Score | Risikostufe | Behandlung | Eskalation |
|--------------|-------------|------------|------------|
| 15-25 | Kritisch (Rot) | Sofortige Maßnahmen erforderlich | {{ meta-organisation-roles.role_CEO }} |
| 10-14 | Hoch (Orange) | Maßnahmen innerhalb 3 Monate | BCM-Manager |
| 5-9 | Mittel (Gelb) | Maßnahmen innerhalb 12 Monate | Fachbereich |
| 1-4 | Niedrig (Grün) | Überwachung, keine Maßnahmen | Fachbereich |

### 3.3 Risikomatrix

```
Auswirkung
    │
  5 │  10    15    20    25
    │ [Gelb][Orange][Rot][Rot]
  4 │   8    12    16    20
    │ [Gelb][Orange][Orange][Rot]
  3 │   6     9    12    15
    │ [Gelb][Gelb][Orange][Orange]
  2 │   4     6     8    10
    │ [Grün][Gelb][Gelb][Orange]
  1 │   2     3     4     5
    │ [Grün][Grün][Grün][Gelb]
    └─────────────────────────
      1     2     3     4     5
           Wahrscheinlichkeit
```

## 4. Risikoregister

### 4.1 Bewertete Risiken

| Risiko/Szenario | Betroffene Services | Wahrsch. | Auswirkung | Score | Risikostufe | Kontrollen (bestehend) | Maßnahmen (geplant) | Owner |
|-----------------|-------------------|----------|------------|-------|-------------|----------------------|-------------------|-------|
| [TODO: Risiko 1] | [TODO] | 3 | 5 | 15 | Orange | [TODO] | [TODO] | [TODO] |

**Beispiele:**

| Risiko/Szenario | Betroffene Services | Wahrsch. | Auswirkung | Score | Risikostufe | Kontrollen (bestehend) | Maßnahmen (geplant) | Owner |
|-----------------|-------------------|----------|------------|-------|-------------|----------------------|-------------------|-------|
| Ransomware-Angriff | Alle IT-Services | 4 | 5 | 20 | Rot | Firewall, AV, Backup | EDR, Segmentierung, Offline-Backup | {{ meta-organisation-roles.role_CISO }} |
| Stromausfall | Produktion, IT | 3 | 4 | 12 | Orange | USV (15min) | Notstromgenerator | Facility-Manager |
| Personalausfall (Pandemie) | Alle Prozesse | 2 | 4 | 8 | Gelb | Home-Office möglich | Pandemieplan | HR |
| Lieferantenausfall | Produktion | 3 | 3 | 9 | Gelb | Lagerbestand (2 Wochen) | Zweitlieferant | Einkauf |
| Rechenzentrumsausfall | Alle IT-Services | 2 | 5 | 10 | Orange | Backup vorhanden | DR-Standort | {{ meta-organisation-roles.role_CIO }} |

### 4.2 Top-Risiken (Score ≥ 15)

[TODO: Listen Sie die Top-Risiken auf, die sofortige Maßnahmen erfordern]

1. **Ransomware-Angriff** (Score: 20)
   - Maßnahmen: EDR-Implementierung, Netzwerksegmentierung, Offline-Backups
   - Verantwortlich: {{ meta-organisation-roles.role_CISO }}
   - Fällig: Q1 2026

2. [TODO: Weiteres Top-Risiko]

## 5. Risikobehandlung

### 5.1 Behandlungsstrategien

**Risikovermeidung:**
- Aktivität wird nicht durchgeführt oder eingestellt
- Beispiel: Verzicht auf Nutzung unsicherer Cloud-Services

**Risikoreduktion:**
- Maßnahmen zur Reduktion von Wahrscheinlichkeit oder Auswirkung
- Beispiel: Implementierung von Redundanzen, Backup-Strategien

**Risikotransfer:**
- Übertragung des Risikos auf Dritte (Versicherung, Outsourcing)
- Beispiel: Cyber-Versicherung, SLA mit Dienstleistern

**Risikoakzeptanz:**
- Bewusste Akzeptanz des Restrisikos
- Beispiel: Niedrige Risiken ohne Maßnahmen

### 5.2 Maßnahmenplan

| Maßnahme | Risiko | Strategie | Beschreibung | Owner | Priorität | Kosten | Fällig | Status |
|----------|--------|-----------|--------------|-------|-----------|--------|--------|--------|
| [TODO: Maßnahme 1] | [TODO: Risiko] | Reduktion | [TODO: Beschreibung] | [TODO] | Hoch | [TODO] | [TODO] | Offen |

**Beispiele:**

| Maßnahme | Risiko | Strategie | Beschreibung | Owner | Priorität | Kosten | Fällig | Status |
|----------|--------|-----------|--------------|-------|-----------|--------|--------|--------|
| EDR-Implementierung | Ransomware | Reduktion | Endpoint Detection & Response auf allen Clients | {{ meta-organisation-roles.role_CISO }} | Hoch | 50.000 € | Q1 2026 | In Arbeit |
| Notstromgenerator | Stromausfall | Reduktion | Diesel-Generator für 48h Betrieb | Facility | Mittel | 80.000 € | Q2 2026 | Geplant |
| Cyber-Versicherung | Ransomware | Transfer | Versicherung für Cyber-Vorfälle | CFO | Hoch | 20.000 €/Jahr | Q1 2026 | Offen |

## 6. Überwachung und Review

### 6.1 Risiko-Monitoring

**Verantwortlich:** BCM-Manager

**Überwachungsintervall:**
- Quartalsweise Überprüfung des Risikoregisters
- Ad-hoc bei neuen Bedrohungen oder Vorfällen
- Jährliche vollständige Risikoanalyse

**Indikatoren:**
- Neue Bedrohungen (z.B. neue Ransomware-Varianten)
- Vorfälle bei vergleichbaren Organisationen
- Änderungen in der Bedrohungslandschaft
- Technologische Entwicklungen

### 6.2 Eskalation

**Eskalationskriterien:**
- Neues Risiko mit Score ≥ 15
- Bestehend Risiko erhöht sich auf Score ≥ 15
- Risiko tritt ein (Incident)

**Eskalationswege:**
- Score ≥ 15: Sofortige Meldung an {{ meta-organisation-roles.role_CEO }}
- Score 10-14: Meldung an BCM-Manager
- Score < 10: Dokumentation im Risikoregister

<!-- End of template -->
