# Risikoanalyse (BSI Standard 200-3) – Template

**Dokument-ID:** 0090  
**Dokumenttyp:** Methodik-Artefakt  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standard 200-3)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template guides the risk analysis according to BSI Standard 200-3.
Risk analysis is performed for objects with elevated protection requirements or special threat situations.
Reference: BSI Standard 200-3 (Risk Analysis based on IT-Grundschutz)
-->

## 1. Ziel und Auslöser

Die Risikoanalyse nach BSI Standard 200-3 identifiziert und bewertet Risiken für **{{ meta.organization.name }}**, die nicht durch IT-Grundschutz-Bausteine abgedeckt sind.

**Verantwortlich:** {{ meta.ciso.name }} (ISB)

**Auslöser für Risikoanalyse:**
- Hoher oder sehr hoher Schutzbedarf (siehe Dokument 0060)
- Besondere Bedrohungslage (z.B. gezielte Angriffe)
- Abweichungen von IT-Grundschutz-Anforderungen
- Neue Technologien ohne passende Bausteine
- Externe Anforderungen (Kunden, Regulierung)

[TODO: Spezifische Auslöser für diese Risikoanalyse dokumentieren]

## 2. Risikoobjekte und Scope

**Betroffene Objekte:**

| Objekt-ID | Objekt | Typ | Schutzbedarf | Begründung für Risikoanalyse |
|---|---|---|---|---|
| [TODO] | [TODO] | Prozess/Anwendung/System | Sehr hoch | [TODO] |
| [TODO] | [TODO] | Prozess/Anwendung/System | Sehr hoch | [TODO] |

**Schnittstellen und Provider:**
- [TODO: Externe Schnittstellen und Dienstleister dokumentieren]

## 3. Bedrohungen, Schwachstellen und Szenarien

### 3.1 Bedrohungskatalog

| Bedrohungs-ID | Bedrohung | Kategorie | Beschreibung |
|---|---|---|---|
| T-001 | Gezielte Cyberangriffe | Extern | APT-Angriffe auf kritische Systeme |
| T-002 | Ransomware | Extern | Verschlüsselung kritischer Daten |
| T-003 | Insider-Bedrohung | Intern | Missbrauch privilegierter Zugriffe |
| T-004 | DDoS-Angriffe | Extern | Verfügbarkeitsbeeinträchtigung |
| T-005 | Supply Chain Attacks | Extern | Kompromittierung über Lieferanten |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 3.2 Schwachstellenkatalog

| Schwachstellen-ID | Schwachstelle | Objekt | Beschreibung |
|---|---|---|---|
| V-001 | Unzureichende Segmentierung | Netzwerk | Fehlende Mikrosegmentierung |
| V-002 | Fehlende MFA | VPN-Zugang | Nur Passwort-Authentifizierung |
| V-003 | Veraltete Software | [TODO: System] | End-of-Life Software im Einsatz |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 3.3 Risikoszenarien

| Szenario-ID | Szenario | Bedrohung | Schwachstelle | Betroffenes Objekt |
|---|---|---|---|---|
| S-001 | Ransomware-Angriff auf Produktionssysteme | T-002 | V-001, V-002 | [TODO: Produktionssystem] |
| S-002 | Datendiebstahl durch Insider | T-003 | V-002 | [TODO: Datenbank] |
| S-003 | DDoS auf öffentliche Services | T-004 | [TODO] | [TODO: Webserver] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Risikobewertung

### 4.1 Bewertungsskala

**Eintrittswahrscheinlichkeit:**

| Stufe | Beschreibung | Häufigkeit |
|---|---|---|
| 1 - Sehr gering | Unwahrscheinlich | < 1x in 10 Jahren |
| 2 - Gering | Selten | 1x in 5-10 Jahren |
| 3 - Mittel | Gelegentlich | 1x in 1-5 Jahren |
| 4 - Hoch | Wahrscheinlich | 1x pro Jahr |
| 5 - Sehr hoch | Sehr wahrscheinlich | Mehrmals pro Jahr |

**Auswirkung (Schadenshöhe):**

| Stufe | Beschreibung | Finanzielle Auswirkung | Geschäftsauswirkung |
|---|---|---|---|
| 1 - Sehr gering | Vernachlässigbar | < 10.000 € | Keine wesentliche Beeinträchtigung |
| 2 - Gering | Begrenzt | 10.000 - 50.000 € | Geringe Beeinträchtigung |
| 3 - Mittel | Beträchtlich | 50.000 - 250.000 € | Merkliche Beeinträchtigung |
| 4 - Hoch | Schwerwiegend | 250.000 - 1.000.000 € | Erhebliche Beeinträchtigung |
| 5 - Sehr hoch | Katastrophal | > 1.000.000 € | Existenzbedrohend |

**Risikomatrix:**

| Eintrittswahrscheinlichkeit | Auswirkung 1 | Auswirkung 2 | Auswirkung 3 | Auswirkung 4 | Auswirkung 5 |
|---|---|---|---|---|---|
| 5 - Sehr hoch | Mittel | Hoch | Hoch | Sehr hoch | Sehr hoch |
| 4 - Hoch | Mittel | Mittel | Hoch | Hoch | Sehr hoch |
| 3 - Mittel | Niedrig | Mittel | Mittel | Hoch | Hoch |
| 2 - Gering | Niedrig | Niedrig | Mittel | Mittel | Hoch |
| 1 - Sehr gering | Niedrig | Niedrig | Niedrig | Mittel | Mittel |

### 4.2 Risikoakzeptanzkriterien

| Risikostufe | Behandlung | Genehmigung erforderlich |
|---|---|---|
| **Sehr hoch** | Muss behandelt werden | Geschäftsführung |
| **Hoch** | Sollte behandelt werden | ISB |
| **Mittel** | Kann behandelt werden | ISB |
| **Niedrig** | Kann akzeptiert werden | Informationsverbund-Verantwortlicher |

## 5. Risikoregister

| Risiko-ID | Objekt | Szenario | Bedrohung | Schwachstelle | Bestehende Maßnahmen | Eintritts­wahrscheinlichkeit | Auswirkung | Risiko (vorher) | Behandlung | Zusätzliche Maßnahme | Owner | Termin | Risiko (nachher) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-001 | [TODO] | S-001 | T-002 | V-001, V-002 | Antivirus, Backup | 4 | 5 | Sehr hoch | Mindern | Mikrosegmentierung, MFA | {{ meta.cio.name }} | [TODO] | Mittel |
| R-002 | [TODO] | S-002 | T-003 | V-002 | Logging, IAM | 3 | 4 | Hoch | Mindern | PAM, DLP | {{ meta.cio.name }} | [TODO] | Niedrig |
| R-003 | [TODO] | S-003 | T-004 | [TODO] | Firewall | 3 | 3 | Mittel | Mindern | DDoS-Protection | {{ meta.cio.name }} | [TODO] | Niedrig |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Risikobehandlungsoptionen:**
- **Mindern:** Zusätzliche Maßnahmen implementieren
- **Vermeiden:** Risikoquelle eliminieren
- **Übertragen:** Risiko auf Dritte übertragen (Versicherung, Outsourcing)
- **Akzeptieren:** Risiko bewusst akzeptieren (mit Genehmigung)

## 6. Risikobewertung: Zusammenfassung

**Risikoverteilung (vor Behandlung):**
- Sehr hoch: [TODO]
- Hoch: [TODO]
- Mittel: [TODO]
- Niedrig: [TODO]

**Risikoverteilung (nach Behandlung):**
- Sehr hoch: [TODO]
- Hoch: [TODO]
- Mittel: [TODO]
- Niedrig: [TODO]

**Top 5 Risiken:**
1. [TODO: Risiko 1]
2. [TODO: Risiko 2]
3. [TODO: Risiko 3]
4. [TODO: Risiko 4]
5. [TODO: Risiko 5]

## 7. Freigabe und Risikoakzeptanz

### 7.1 Risikoeigner

| Risiko-ID | Risiko | Risikoeigner | Akzeptanz | Datum |
|---|---|---|---|---|
| R-001 | [TODO] | {{ meta.ceo.name }} | Akzeptiert nach Maßnahmenumsetzung | [TODO] |
| R-002 | [TODO] | {{ meta.ciso.name }} | Akzeptiert nach Maßnahmenumsetzung | [TODO] |

### 7.2 Management-Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT-Leitung | {{ meta.cio.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| Geschäftsführung | {{ meta.ceo.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

## 8. Aktualisierung und Pflege

Die Risikoanalyse wird aktualisiert bei:
- Wesentlichen Änderungen in der Bedrohungslage
- Neuen Schwachstellen oder Sicherheitsvorfällen
- Änderungen am Informationsverbund
- Mindestens jährlich im Rahmen des ISMS-Reviews

**Verantwortlich:** {{ meta.ciso.name }} (ISB)  
**Nächster Review:** {{ meta.document.next_review }}

---

**Referenzen:**
- BSI Standard 200-3: Risikoanalyse auf der Basis von IT-Grundschutz
- BSI IT-Grundschutz-Kompendium

<!-- End of template -->
