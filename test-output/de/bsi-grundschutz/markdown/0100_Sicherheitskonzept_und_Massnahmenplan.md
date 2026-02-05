# Sicherheitskonzept und Maßnahmenplan

**Dokument-ID:** 0100  
**Dokumenttyp:** Plan/Steuerungsdokument  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2/200-3)  
**Owner:** IT Operations Manager  
**Version:** 1.0.0  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---



## 1. Zielbild und Strategie

### 1.1 Sicherheitsziele

**AdminSend GmbH** verfolgt folgende strategische Sicherheitsziele:

1. **[TODO: Ziel 1]:** [TODO: Beschreibung]
2. **[TODO: Ziel 2]:** [TODO: Beschreibung]
3. **[TODO: Ziel 3]:** [TODO: Beschreibung]

### 1.2 Prioritäten

**Priorisierung nach:**
- Kritikalität (Schutzbedarf)
- Risikohöhe
- Compliance-Anforderungen
- Quick Wins (Aufwand vs. Nutzen)
- Abhängigkeiten

### 1.3 Architekturelle Leitplanken

**Sicherheitsarchitektur-Prinzipien:**
- Defense in Depth (mehrschichtige Sicherheit)
- Zero Trust (Verify explicitly, Least privilege, Assume breach)
- Secure by Design
- Privacy by Design
- [TODO: Weitere Prinzipien]

## 2. Maßnahmenkatalog

### 2.1 Maßnahmen aus Basis-Sicherheitscheck



| Maßnahme-ID | Quelle | Beschreibung | Priorität | Owner | Aufwand (PT) | Budget | Zieltermin | Abhängigkeiten | Status |
|---|---|---|---|---|---|---|---|---|---|
| M-001 | Basis-Check (GAP-001) | [TODO: Kritische Maßnahme 1] | P1 - Kritisch | Thomas Weber | [TODO] | [TODO] | [TODO] | - | Offen |
| M-002 | Basis-Check (QW-001) | [TODO: Quick Win 1] | P2 - Hoch | Anna Schmidt | [TODO] | [TODO] | [TODO] | - | Offen |
| M-003 | Basis-Check | [TODO: Maßnahme 3] | P3 - Mittel | [TODO] | [TODO] | [TODO] | [TODO] | M-001 | Offen |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 2.2 Maßnahmen aus Risikoanalyse



| Maßnahme-ID | Quelle | Beschreibung | Priorität | Owner | Aufwand (PT) | Budget | Zieltermin | Abhängigkeiten | Status |
|---|---|---|---|---|---|---|---|---|---|
| M-101 | Risikoanalyse (R-001) | [TODO: Risikominderung 1] | P1 - Kritisch | Anna Schmidt | [TODO] | [TODO] | [TODO] | - | Offen |
| M-102 | Risikoanalyse (R-002) | [TODO: Risikominderung 2] | P2 - Hoch | Anna Schmidt | [TODO] | [TODO] | [TODO] | - | Offen |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 2.3 Strategische Maßnahmen

| Maßnahme-ID | Beschreibung | Priorität | Owner | Aufwand (PT) | Budget | Zieltermin | Status |
|---|---|---|---|---|---|---|---|
| M-201 | SIEM-Implementierung | P1 - Kritisch | Anna Schmidt | [TODO] | [TODO] | [TODO] | Offen |
| M-202 | Zero Trust Architecture | P2 - Hoch | Anna Schmidt | [TODO] | [TODO] | [TODO] | Offen |
| M-203 | Security Awareness Programm | P2 - Hoch | Thomas Weber | [TODO] | [TODO] | [TODO] | Offen |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 3. Maßnahmen-Priorisierung

### 3.1 Priorität 1 - Kritisch (Sofort)

| Maßnahme-ID | Beschreibung | Owner | Zieltermin | Abhängigkeiten |
|---|---|---|---|---|
| M-001 | [TODO] | [TODO] | [TODO] | - |
| M-101 | [TODO] | [TODO] | [TODO] | - |
| M-201 | [TODO] | [TODO] | [TODO] | - |

**Anzahl:** [TODO]  
**Gesamtaufwand:** [TODO] PT  
**Gesamtbudget:** [TODO] €

### 3.2 Priorität 2 - Hoch (Kurzfristig, 0-6 Monate)

| Maßnahme-ID | Beschreibung | Owner | Zieltermin | Abhängigkeiten |
|---|---|---|---|---|
| M-002 | [TODO] | [TODO] | [TODO] | - |
| M-102 | [TODO] | [TODO] | [TODO] | M-001 |
| M-202 | [TODO] | [TODO] | [TODO] | M-201 |

**Anzahl:** [TODO]  
**Gesamtaufwand:** [TODO] PT  
**Gesamtbudget:** [TODO] €

### 3.3 Priorität 3 - Mittel (Mittelfristig, 6-12 Monate)

| Maßnahme-ID | Beschreibung | Owner | Zieltermin | Abhängigkeiten |
|---|---|---|---|---|
| M-003 | [TODO] | [TODO] | [TODO] | M-001 |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl:** [TODO]  
**Gesamtaufwand:** [TODO] PT  
**Gesamtbudget:** [TODO] €

### 3.4 Priorität 4 - Niedrig (Langfristig, > 12 Monate)

| Maßnahme-ID | Beschreibung | Owner | Zieltermin | Abhängigkeiten |
|---|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl:** [TODO]  
**Gesamtaufwand:** [TODO] PT  
**Gesamtbudget:** [TODO] €

## 4. Roadmap

### 4.1 Quartal 1 (Q1 {{ meta.document.year }})

**Fokus:** Kritische Sicherheitslücken schließen

| Maßnahme-ID | Beschreibung | Owner | Status |
|---|---|---|---|
| M-001 | [TODO] | [TODO] | Geplant |
| M-101 | [TODO] | [TODO] | Geplant |

### 4.2 Quartal 2 (Q2 {{ meta.document.year }})

**Fokus:** Quick Wins und Basis-Sicherheit

| Maßnahme-ID | Beschreibung | Owner | Status |
|---|---|---|---|
| M-002 | [TODO] | [TODO] | Geplant |
| M-201 | [TODO] | [TODO] | Geplant |

### 4.3 Quartal 3 (Q3 {{ meta.document.year }})

**Fokus:** Strategische Maßnahmen

| Maßnahme-ID | Beschreibung | Owner | Status |
|---|---|---|---|
| M-202 | [TODO] | [TODO] | Geplant |
| M-203 | [TODO] | [TODO] | Geplant |

### 4.4 Quartal 4 (Q4 {{ meta.document.year }})

**Fokus:** Konsolidierung und Optimierung

| Maßnahme-ID | Beschreibung | Owner | Status |
|---|---|---|---|
| M-003 | [TODO] | [TODO] | Geplant |
| [TODO] | [TODO] | [TODO] | Geplant |

## 5. Ressourcenplanung

### 5.1 Personalressourcen

| Rolle | Aufwand (PT) | Verfügbarkeit | Lücke |
|---|---|---|---|
| ISB | [TODO] | [TODO] | [TODO] |
| IT-Leitung | [TODO] | [TODO] | [TODO] |
| IT-Administratoren | [TODO] | [TODO] | [TODO] |
| Externe Berater | [TODO] | [TODO] | [TODO] |
| **Gesamt** | **[TODO]** | **[TODO]** | **[TODO]** |

### 5.2 Budget

| Kategorie | Budget | Verwendung |
|---|---|---|
| Software-Lizenzen | [TODO] € | SIEM, PAM, EDR, etc. |
| Hardware | [TODO] € | Firewalls, Server, etc. |
| Externe Dienstleistungen | [TODO] € | Beratung, Implementierung |
| Schulungen | [TODO] € | Awareness, technische Schulungen |
| Sonstiges | [TODO] € | [TODO] |
| **Gesamt** | **[TODO] €** | |

### 5.3 Externe Unterstützung

| Dienstleister | Leistung | Aufwand | Budget | Zeitraum |
|---|---|---|---|---|
| [TODO: Dienstleister 1] | [TODO] | [TODO] PT | [TODO] € | [TODO] |
| [TODO: Dienstleister 2] | [TODO] | [TODO] PT | [TODO] € | [TODO] |

## 6. Abhängigkeiten und Risiken

### 6.1 Kritische Abhängigkeiten

| Maßnahme | Abhängigkeit | Auswirkung | Mitigation |
|---|---|---|---|
| M-202 (Zero Trust) | M-201 (SIEM) | Verzögerung | Parallele Planung |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 6.2 Umsetzungsrisiken

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation | Owner |
|---|---|---|---|---|
| Ressourcenmangel | Hoch | Verzögerung | Externe Unterstützung | Thomas Weber |
| Budget-Kürzung | Mittel | Priorisierung | Fokus auf P1-Maßnahmen | Max Mustermann |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 7. Erfolgsmessung

### 7.1 Erfolgskriterien

| Kriterium | Ziel | Messung |
|---|---|---|
| Maßnahmenumsetzung | 100% P1-Maßnahmen bis [TODO] | Maßnahmenplan-Tracking |
| Erfüllungsgrad IT-Grundschutz | > 80% bis [TODO] | Basis-Sicherheitscheck |
| Risikoreduktion | Keine "Sehr hoch"-Risiken | Risikoregister |
| [TODO] | [TODO] | [TODO] |

### 7.2 Meilensteine

| Meilenstein | Datum | Kriterium | Status |
|---|---|---|---|
| M1: Kritische Lücken geschlossen | [TODO] | Alle P1-Maßnahmen umgesetzt | Geplant |
| M2: Basis-Sicherheit erreicht | [TODO] | 80% Erfüllungsgrad | Geplant |
| M3: Strategische Maßnahmen umgesetzt | [TODO] | SIEM, Zero Trust produktiv | Geplant |
| M4: IT-Grundschutz-Zertifizierung | [TODO] | Zertifizierung erhalten | Geplant |

## 8. Governance und Steuerung

**Steuerungsgremium:** ISMS-Team (siehe Dokument 0020)

**Regeltermine:**
- **Wöchentlich:** Maßnahmen-Status-Update (ISB, IT-Leitung)
- **Monatlich:** ISMS-Team-Meeting (Fortschritt, Eskalationen)
- **Quartalsweise:** Management-Review (Geschäftsführung)

**Reporting:** Siehe Dokument 0110 (Umsetzungssteuerung und KPIs)

## 9. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | Thomas Weber | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT-Leitung | Anna Schmidt | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| Geschäftsführung | Max Mustermann | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**Referenzen:**
- BSI Standard 200-2: IT-Grundschutz-Methodik
- Dokument 0080: Basis-Sicherheitscheck
- Dokument 0090: Risikoanalyse


