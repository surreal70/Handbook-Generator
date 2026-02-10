# Prozessinteraktion und Prozesslandkarte

**Dokument-ID:** 0050  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
Dieses Template visualisiert die Prozesslandkarte des QMS und beschreibt die Wechselwirkungen zwischen Prozessen.
Es dient als Übersicht über das gesamte QMS und zeigt, wie die einzelnen Prozesse zusammenwirken.

Anpassung erforderlich:
- Erstelle visuelle Prozesslandkarte mit allen QMS-Prozessen
- Dokumentiere alle Prozessinteraktionen und Schnittstellen
- Definiere Eingaben und Ausgaben für jeden Prozess
- Identifiziere kritische Schnittstellen und Übergaben
- Lege Prozess-KPIs und Überwachungsmethoden fest
- Verknüpfe mit externen Parteien (Kunden, Lieferanten, Behörden)
- Aktualisiere regelmäßig bei Prozessänderungen

Referenz: ISO 9001:2015, Kapitel 4.4 (Prozessinteraktionen)
-->

## Zweck

Dieses Dokument visualisiert die Prozesslandkarte des Qualitätsmanagementsystems und beschreibt die Wechselwirkungen zwischen den Prozessen. Es dient als Übersicht über das gesamte QMS und zeigt, wie die einzelnen Prozesse zusammenwirken, um die beabsichtigten Ergebnisse zu erreichen.

## Prozesslandkarte

### Übersicht

Die Prozesslandkarte gliedert sich in drei Hauptebenen:

```
┌─────────────────────────────────────────────────────────────┐
│                    MANAGEMENTPROZESSE                        │
│  Strategische Planung | Managementbewertung | Internes Audit│
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      KERNPROZESSE                            │
│  [TODO: Prozess 1] → [TODO: Prozess 2] → [TODO: Prozess 3] │
└─────────────────────────────────────────────────────────────┘
                              ↑
┌─────────────────────────────────────────────────────────────┐
│                  UNTERSTÜTZUNGSPROZESSE                      │
│  Personal | Ressourcen | Dokumentation | IT | Einkauf       │
└─────────────────────────────────────────────────────────────┘
```

### Detaillierte Prozesslandkarte

[TODO: Hier detaillierte Prozesslandkarte als Diagramm einfügen]

**Hinweis:** Die Prozesslandkarte sollte als Diagramm im Ordner `diagrams/` gespeichert und hier referenziert werden.

## Prozessinteraktionen

### Managementprozesse

#### Strategische Planung
**Eingaben von:**
- Kontext der Organisation (4.1)
- Interessierte Parteien (4.2)
- Leistungsdaten aus allen Prozessen

**Ausgaben an:**
- Alle Prozesse: Qualitätspolitik, Qualitätsziele
- Managementbewertung: Strategische Vorgaben
- Ressourcenmanagement: Ressourcenanforderungen

#### Managementbewertung
**Eingaben von:**
- Internes Audit: Audit-Ergebnisse
- Alle Prozesse: Leistungsdaten, KPIs
- Kundenzufriedenheit: Feedback-Daten
- Risikomanagement: Risikobewertungen

**Ausgaben an:**
- Strategische Planung: Verbesserungsbedarf
- Alle Prozesse: Managemententscheidungen
- Ressourcenmanagement: Ressourcenentscheidungen

#### Internes Audit
**Eingaben von:**
- Alle Prozesse: Prozessdokumentation
- Managementbewertung: Auditprogramm
- Risikomanagement: Risikobereiche

**Ausgaben an:**
- Managementbewertung: Audit-Ergebnisse
- Betroffene Prozesse: Nichtkonformitäten
- Verbesserungsprozess: Verbesserungspotenziale

### Kernprozesse

#### [TODO: Kernprozess 1 - z.B. Vertrieb/Kundenmanagement]
**Eingaben von:**
- Kunden: Anfragen, Anforderungen
- Marketing: Marktinformationen
- Produktentwicklung: Produktinformationen

**Ausgaben an:**
- [TODO: Kernprozess 2]: Aufträge, Spezifikationen
- Kunden: Angebote, Auftragsbestätigungen
- Kundenzufriedenheit: Feedback-Anfragen

#### [TODO: Kernprozess 2 - z.B. Produktentwicklung]
**Eingaben von:**
- Vertrieb: Kundenanforderungen
- Marktforschung: Markttrends
- Qualitätsmanagement: Qualitätsanforderungen

**Ausgaben an:**
- [TODO: Kernprozess 3]: Produktspezifikationen
- Einkauf: Materiallisten
- Produktion: Fertigungsunterlagen

#### [TODO: Kernprozess 3 - z.B. Produktion/Dienstleistungserbringung]
**Eingaben von:**
- Produktentwicklung: Spezifikationen
- Einkauf: Materialien, Komponenten
- Qualitätskontrolle: Prüfvorgaben

**Ausgaben an:**
- Qualitätskontrolle: Produkte zur Prüfung
- Versand: Fertige Produkte
- Lager: Lagerbestand

#### [TODO: Kernprozess 4 - z.B. Qualitätskontrolle]
**Eingaben von:**
- Produktion: Produkte zur Prüfung
- Produktentwicklung: Prüfspezifikationen
- Wareneingang: Eingangsmaterialien

**Ausgaben an:**
- Produktion: Prüfergebnisse, Freigaben
- Versand: Freigabe für Auslieferung
- Qualitätsmanagement: Qualitätsdaten

#### [TODO: Kernprozess 5 - z.B. Versand/Auslieferung]
**Eingaben von:**
- Qualitätskontrolle: Freigegebene Produkte
- Vertrieb: Lieferanweisungen
- Lager: Verfügbare Produkte

**Ausgaben an:**
- Kunden: Ausgelieferte Produkte
- Vertrieb: Lieferbestätigungen
- After-Sales: Übergabe für Support

### Unterstützungsprozesse

#### Personalmanagement
**Eingaben von:**
- Alle Prozesse: Personalbedarf, Kompetenzanforderungen
- Strategische Planung: Personalstrategie

**Ausgaben an:**
- Alle Prozesse: Qualifiziertes Personal
- Schulungsmanagement: Schulungsbedarfe

#### Ressourcenmanagement
**Eingaben von:**
- Alle Prozesse: Ressourcenanforderungen
- Strategische Planung: Budgetvorgaben

**Ausgaben an:**
- Alle Prozesse: Infrastruktur, Ausrüstung
- Instandhaltung: Wartungspläne

#### Dokumentenmanagement
**Eingaben von:**
- Alle Prozesse: Dokumente, Änderungsanforderungen
- Qualitätsmanagement: Dokumentationsanforderungen

**Ausgaben an:**
- Alle Prozesse: Gelenkte Dokumente
- Internes Audit: Dokumentationsnachweise

#### IT-Management
**Eingaben von:**
- Alle Prozesse: IT-Anforderungen
- Strategische Planung: IT-Strategie

**Ausgaben an:**
- Alle Prozesse: IT-Systeme, Support
- Datensicherheit: Sicherheitsmaßnahmen

#### Einkauf
**Eingaben von:**
- Produktion: Materialbedarfe
- Produktentwicklung: Spezifikationen
- Qualitätsmanagement: Lieferantenanforderungen

**Ausgaben an:**
- Produktion: Materialien, Komponenten
- Wareneingang: Lieferungen
- Lieferantenmanagement: Lieferantenbewertungen

## Prozessfluss und Wertschöpfungskette

### Hauptwertschöpfungskette

```
Kunde → Vertrieb → [TODO: Entwicklung] → [TODO: Produktion] → 
[TODO: Qualitätskontrolle] → [TODO: Versand] → Kunde
```

### Unterstützende Prozesse

Alle Kernprozesse werden unterstützt durch:
- Personalmanagement (Kompetente Mitarbeiter)
- Ressourcenmanagement (Infrastruktur, Ausrüstung)
- Dokumentenmanagement (Dokumentierte Informationen)
- IT-Management (IT-Systeme)
- Einkauf (Materialien, Dienstleistungen)

### Steuernde Prozesse

Alle Prozesse werden gesteuert durch:
- Strategische Planung (Vorgaben, Ziele)
- Managementbewertung (Entscheidungen, Ressourcen)
- Internes Audit (Überwachung, Verbesserung)

## Schnittstellen zu externen Parteien

### Kunden
**Schnittstellen:**
- Anfragen und Anforderungen → Vertrieb
- Feedback und Beschwerden → Kundenzufriedenheit
- Ausgelieferte Produkte ← Versand
- After-Sales-Support ← Service

### Lieferanten
**Schnittstellen:**
- Bestellungen → Einkauf
- Lieferungen → Wareneingang
- Qualitätsdaten ← Qualitätskontrolle
- Lieferantenbewertungen ← Lieferantenmanagement

### Regulierungsbehörden
**Schnittstellen:**
- Compliance-Anforderungen → Qualitätsmanagement
- Nachweise und Berichte ← Qualitätsmanagement
- Audits und Inspektionen ↔ Qualitätsmanagement

### Zertifizierungsstellen
**Schnittstellen:**
- Zertifizierungsaudits ↔ Qualitätsmanagement
- Zertifikate ← Zertifizierungsstelle
- Überwachungsaudits ↔ Qualitätsmanagement

## Prozessleistung und -überwachung

### Prozess-KPI-Übersicht

| Prozess | Haupt-KPI | Zielwert | Messfrequenz |
|---------|-----------|----------|--------------|
| [TODO: Prozess 1] | [TODO: KPI] | [TODO] | [TODO] |
| [TODO: Prozess 2] | [TODO: KPI] | [TODO] | [TODO] |
| [TODO: Prozess 3] | [TODO: KPI] | [TODO] | [TODO] |

### Gesamtsystem-KPIs

**Qualitätsziele auf Systemebene:**
1. [TODO: z.B. Kundenzufriedenheit > 90%]
2. [TODO: z.B. Ausschussrate < 2%]
3. [TODO: z.B. Liefertreue > 95%]
4. [TODO: z.B. Reklamationsquote < 1%]

## Risiken und Chancen in Prozessinteraktionen

### Identifizierte Schnittstellenrisiken

| Schnittstelle | Risiko | Auswirkung | Maßnahme |
|---------------|--------|------------|----------|
| [TODO: Prozess A → B] | [TODO: Risiko] | [TODO] | [TODO] |
| [TODO: Prozess C → D] | [TODO: Risiko] | [TODO] | [TODO] |

### Chancen in Prozessinteraktionen

| Schnittstelle | Chance | Potenzial | Maßnahme |
|---------------|--------|-----------|----------|
| [TODO: Prozess A → B] | [TODO: Chance] | [TODO] | [TODO] |
| [TODO: Prozess C → D] | [TODO: Chance] | [TODO] | [TODO] |

## Pflege und Aktualisierung

### Verantwortlichkeiten

- **Pflege der Prozesslandkarte:** [TODO: Qualitätsmanagementbeauftragter]
- **Aktualisierung bei Prozessänderungen:** [TODO: Prozesseigner]
- **Genehmigung:** [TODO: Geschäftsführung]

### Aktualisierungsanlässe

Die Prozesslandkarte wird aktualisiert bei:
- Neuen oder geänderten Prozessen
- Änderungen in Prozessinteraktionen
- Organisatorischen Änderungen
- Ergebnissen der Managementbewertung
- Audit-Feststellungen

## Anhänge

- **Anhang A:** Detaillierte Prozesslandkarte (Diagramm)
- **Anhang B:** Prozessinteraktionsmatrix
- **Anhang C:** SIPOC-Diagramme (Supplier-Input-Process-Output-Customer)
- **Anhang D:** Prozessflussdiagramme

---

**Nächste Schritte:**
1. Erstellen Sie eine visuelle Prozesslandkarte
2. Dokumentieren Sie alle Prozessinteraktionen
3. Identifizieren Sie kritische Schnittstellen
4. Definieren Sie Schnittstellenverantwortlichkeiten
5. Überwachen Sie die Wirksamkeit der Prozessinteraktionen
6. Aktualisieren Sie die Prozesslandkarte regelmäßig

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
