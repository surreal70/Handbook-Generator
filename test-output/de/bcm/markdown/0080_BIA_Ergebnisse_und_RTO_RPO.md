# BIA – Ergebnisse und Zielwerte (RTO/RPO)

**Dokument-ID:** BCM-0080  
**Organisation:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---



## 1. Zusammenfassung

### 1.1 Top-kritische Prozesse und Services

Die folgenden Prozesse wurden als geschäftskritisch identifiziert (RTO < 24 Stunden):

[TODO: Listen Sie die top-kritischen Prozesse auf]

**Beispiele:**
1. **Auftragsabwicklung** - RTO: 4 Stunden, RPO: 15 Minuten
2. **Kundenservice (24/7)** - RTO: 2 Stunden, RPO: 1 Stunde
3. **Produktionssteuerung** - RTO: 8 Stunden, RPO: 30 Minuten
4. **Zahlungsverkehr** - RTO: 4 Stunden, RPO: 15 Minuten
5. **E-Mail und Kommunikation** - RTO: 4 Stunden, RPO: 1 Stunde

### 1.2 Wesentliche Erkenntnisse

[TODO: Dokumentieren Sie die wichtigsten Erkenntnisse aus der BIA]

**Beispiel-Erkenntnisse:**
- **Single Points of Failure:** ERP-System hat keine Redundanz, kritische Abhängigkeit
- **Personalabhängigkeiten:** Schlüsselpersonen in Produktion ohne ausreichende Vertretung
- **Lieferantenrisiken:** Kritischer Lieferant hat kein eigenes BCM
- **IT-Infrastruktur:** Netzwerkinfrastruktur teilweise nicht redundant ausgelegt

## 2. BIA-Ergebnis-Tabelle

### 2.1 Geschäftskritische Prozesse (Kritikalität: HOCH)

| Service/Prozess | MTPD/MAO | RTO | RPO | Manuelle Workarounds möglich? | Bemerkungen |
|-----------------|----------|-----|-----|-------------------------------|-------------|
| [TODO: Prozess 1] | [TODO: 24h] | [TODO: 4h] | [TODO: 15min] | Ja/Nein/Teilweise | [TODO: Bemerkungen] |
| [TODO: Prozess 2] | [TODO] | [TODO] | [TODO] | Ja/Nein/Teilweise | [TODO] |

**Beispiel:**
| Service/Prozess | MTPD/MAO | RTO | RPO | Manuelle Workarounds möglich? | Bemerkungen |
|-----------------|----------|-----|-----|-------------------------------|-------------|
| Auftragsabwicklung | 24h | 4h | 15min | Teilweise (Excel-Listen) | ERP-System kritisch |
| Kundenservice | 8h | 2h | 1h | Ja (Telefon, E-Mail) | CRM-System hilfreich, aber nicht zwingend |
| Produktionssteuerung | 48h | 8h | 30min | Nein | Vollautomatisiert, keine manuelle Alternative |

### 2.2 Wichtige Prozesse (Kritikalität: MITTEL)

| Service/Prozess | MTPD/MAO | RTO | RPO | Manuelle Workarounds möglich? | Bemerkungen |
|-----------------|----------|-----|-----|-------------------------------|-------------|
| [TODO: Prozess 1] | [TODO] | [TODO] | [TODO] | Ja/Nein/Teilweise | [TODO] |

### 2.3 Unterstützende Prozesse (Kritikalität: NIEDRIG)

| Service/Prozess | MTPD/MAO | RTO | RPO | Manuelle Workarounds möglich? | Bemerkungen |
|-----------------|----------|-----|-----|-------------------------------|-------------|
| [TODO: Prozess 1] | [TODO] | [TODO] | [TODO] | Ja/Nein/Teilweise | [TODO] |

## 3. Abhängigkeiten pro kritischem Prozess

### 3.1 Prozess: [TODO: Prozessname]

**People (Personal):**
- [TODO: Mindestbesetzung, Schlüsselpersonen, Spezialwissen]
- Beispiel: Mindestens 3 Auftragsbearbeiter, Vertretungsregelung erforderlich

**Facilities (Standorte und Räumlichkeiten):**
- [TODO: Benötigte Standorte, Räume, Infrastruktur]
- Beispiel: Büroarbeitsplätze, Home-Office als Alternative möglich

**Technology (IT-Systeme):**
- [TODO: Kritische IT-Systeme und Anwendungen]
- Beispiel: ERP-System (SAP), E-Mail, Netzwerkzugang

**Information (Daten):**
- [TODO: Kritische Daten und Informationen]
- Beispiel: Auftragsdatenbank, Kundenstammdaten, Produktkonfigurationen

**Suppliers (Lieferanten und Partner):**
- [TODO: Kritische Lieferanten und Dienstleister]
- Beispiel: Logistikdienstleister, Cloud-Provider, Zahlungsdienstleister

### 3.2 Abhängigkeitsmatrix

[TODO: Erstellen Sie eine Abhängigkeitsmatrix für alle kritischen Prozesse]

| Prozess | People | Facilities | Technology | Information | Suppliers |
|---------|--------|------------|------------|-------------|-----------|
| Auftragsabwicklung | 3 Mitarbeiter | Büro/Home-Office | ERP, E-Mail | Auftragsdaten | Logistik |
| Kundenservice | 5 Mitarbeiter | Call-Center | CRM, Telefon | Kundendaten | Telco |
| Produktion | 10 Mitarbeiter | Produktionshalle | MES, SCADA | Produktionsdaten | Zulieferer |

## 4. Manuelle Workarounds und Notbetrieb

### 4.1 Workaround-Strategien

[TODO: Dokumentieren Sie manuelle Workarounds für kritische Prozesse]

**Beispiel für Prozess "Auftragsabwicklung":**

**Bei Ausfall ERP-System:**
- **Workaround:** Manuelle Auftragserfassung in Excel-Listen
- **Kapazität:** Reduziert auf 30% des Normalbetriebs
- **Dauer:** Maximal 24 Stunden (dann Dateneingabe-Rückstau zu groß)
- **Voraussetzungen:** Excel-Templates vorhanden, Mitarbeiter geschult
- **Einschränkungen:** Keine Echtzeit-Bestandsprüfung, keine automatische Rechnungserstellung

**Bei Ausfall Standort:**
- **Workaround:** Home-Office für Auftragsbearbeitung
- **Kapazität:** 80% des Normalbetriebs
- **Dauer:** Unbegrenzt
- **Voraussetzungen:** VPN-Zugang, Laptops, Telefonie über Softphone
- **Einschränkungen:** Keine physische Dokumentenbearbeitung

### 4.2 Notbetrieb-Kapazitäten

| Prozess | Normalbetrieb | Notbetrieb (manuell) | Notbetrieb (IT-DR) | Bemerkungen |
|---------|---------------|---------------------|-------------------|-------------|
| Auftragsabwicklung | 100% | 30% | 80% | Manuelle Erfassung sehr aufwändig |
| Kundenservice | 100% | 70% | 90% | Telefon als Fallback |
| Produktion | 100% | 0% | 100% | Keine manuelle Alternative |

## 5. Offene Punkte und Maßnahmen

### 5.1 Identifizierte Risiken und Maßnahmen

| Maßnahme | Beschreibung | Owner | Priorität | Fällig | Status | Kosten (geschätzt) |
|----------|--------------|-------|-----------|--------|--------|-------------------|
| [TODO: Maßnahme 1] | [TODO: Beschreibung] | [TODO: Owner] | Hoch/Mittel/Niedrig | [TODO: Datum] | Offen/In Arbeit/Erledigt | [TODO: Betrag] |

**Beispiele:**

| Maßnahme | Beschreibung | Owner | Priorität | Fällig | Status | Kosten (geschätzt) |
|----------|--------------|-------|-----------|--------|--------|-------------------|
| ERP-Redundanz | Implementierung Hochverfügbarkeits-Cluster | {{ meta.roles.cio.name }} | Hoch | Q2 2026 | In Arbeit | 150.000 € |
| Backup-Personal | Schulung von Vertretungen für Schlüsselpersonen | HR | Hoch | Q1 2026 | Offen | 20.000 € |
| Lieferanten-BCM | Anforderung BCM-Nachweise von kritischen Lieferanten | Einkauf | Mittel | Q2 2026 | Offen | 5.000 € |
| Netzwerk-Redundanz | Zweite Internet-Anbindung | {{ meta.roles.it_operations_manager.name }} | Hoch | Q1 2026 | In Arbeit | 30.000 € |

### 5.2 Priorisierung der Maßnahmen

**Priorität HOCH (sofort umsetzen):**
- Maßnahmen zur Beseitigung von Single Points of Failure
- Maßnahmen zur Einhaltung kritischer RTO/RPO-Werte
- Maßnahmen zur Erfüllung regulatorischer Anforderungen

**Priorität MITTEL (innerhalb 6-12 Monate):**
- Maßnahmen zur Verbesserung der Resilienz
- Maßnahmen zur Reduktion von Abhängigkeiten
- Maßnahmen zur Verbesserung von Workarounds

**Priorität NIEDRIG (Nice-to-have):**
- Maßnahmen zur weiteren Optimierung
- Maßnahmen für weniger kritische Prozesse

## 6. Wiederherstellungspriorisierung

### 6.1 Priorisierungsmatrix

Bei einem umfassenden Ausfall erfolgt die Wiederherstellung in folgender Reihenfolge:

**Priorität 1 (0-4 Stunden):**
1. Netzwerkinfrastruktur und Internet-Anbindung
2. E-Mail und Kommunikation
3. Authentifizierung und Zugriffskontrolle

**Priorität 2 (4-8 Stunden):**
4. ERP-System (Auftragsabwicklung, Finanzen)
5. CRM-System (Kundenservice)
6. Produktionssteuerungssysteme

**Priorität 3 (8-24 Stunden):**
7. Weitere Geschäftsanwendungen
8. Entwicklungs- und Testumgebungen
9. Reporting und Analytics

### 6.2 Abhängigkeiten bei Wiederherstellung

```
┌─────────────────────┐
│ Netzwerk/Internet   │
└──────────┬──────────┘
           │
    ┌──────┴──────┬──────────────┐
    │             │              │
┌───▼────┐  ┌────▼─────┐  ┌────▼─────┐
│ E-Mail │  │ Authenti-│  │ Firewall │
│        │  │ fizierung│  │          │
└───┬────┘  └────┬─────┘  └────┬─────┘
    │            │             │
    └────────────┴─────────────┘
                 │
         ┌───────┴───────┐
         │               │
    ┌────▼────┐    ┌────▼────┐
    │ ERP     │    │ CRM     │
    └─────────┘    └─────────┘
```

## 7. Genehmigung und Freigabe

### 7.1 Freigabe durch Fachbereiche

| Fachbereich | Verantwortlicher | Datum | Unterschrift |
|-------------|------------------|-------|--------------|
| [TODO: Bereich 1] | [TODO: Name] | [TODO: Datum] | [TODO] |
| [TODO: Bereich 2] | [TODO: Name] | [TODO: Datum] | [TODO] |

### 7.2 Management-Freigabe

| Rolle | Name | Datum | Unterschrift |
|-------|------|-------|--------------|
| CEO | {{ meta.roles.ceo.name }} | [TODO: Datum] | [TODO] |
| CIO | {{ meta.roles.cio.name }} | [TODO: Datum] | [TODO] |
| BCM-Manager | [TODO: Name] | [TODO: Datum] | [TODO] |

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |


