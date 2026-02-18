
Document-ID: tisax-0110

Status: Draft
Classification: Internal

# Asset-Inventar

**Dokument-ID:** [FRAMEWORK]-0110
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Zweck

Dieses Dokument beschreibt die Anforderungen und Prozesse für die Führung eines vollständigen Asset-Inventars gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Assets von [TODO], die im Rahmen von TISAX-relevanten Prozessen erfasst werden müssen.

## Inventar-Anforderungen

### Vollständigkeit

Das Asset-Inventar muss alle relevanten Assets erfassen:

- Hardware (Server, Workstations, Netzwerkgeräte, mobile Geräte)
- Software (Betriebssysteme, Anwendungen, Datenbanken)
- Daten und Informationen
- Services (Cloud-Services, externe Dienstleistungen)
- Dokumentation
- Physische Infrastruktur

### Aktualität

Das Inventar muss aktuell gehalten werden:

- Neue Assets werden innerhalb von [TODO] erfasst
- Änderungen werden zeitnah dokumentiert
- Außerbetriebnahmen werden umgehend vermerkt
- Regelmäßige Validierung der Inventardaten

## Inventar-Struktur

### Pflichtfelder

Für jedes Asset werden folgende Informationen erfasst:

| Feld | Beschreibung | Beispiel |
|------|--------------|----------|
| Asset-ID | Eindeutige Kennung | AST-2024-001 |
| Asset-Name | Bezeichnung | Produktionsserver 01 |
| Asset-Typ | Kategorie | Server |
| Beschreibung | Detaillierte Beschreibung | Hauptproduktionsserver für ERP-System |
| Asset Owner | Verantwortlicher | [TODO] |
| Standort | Physischer/logischer Ort | Rechenzentrum A, Rack 12 |
| Status | Betriebsstatus | In Betrieb |
| Klassifizierung | Schutzbedarf | Vertraulich |

### Optionale Felder

Zusätzliche Informationen je nach Asset-Typ:

- Hersteller und Modell
- Seriennummer
- Anschaffungsdatum und -kosten
- Wartungsvertrag
- Lizenzinformationen
- IP-Adresse/Hostname
- Betriebssystem und Version
- Abhängigkeiten zu anderen Assets
- Backup-Status

## Inventarisierungsprozess

### 1. Asset-Erfassung

#### Automatisierte Erfassung

[TODO] nutzt folgende Tools:

- **Network Discovery**: [TODO]
- **Endpoint Management**: [TODO]
- **Cloud Asset Management**: [TODO]
- **CMDB Integration**: [TODO]

#### Manuelle Erfassung

Für Assets, die nicht automatisch erfasst werden können:

1. Asset-Erfassungsformular ausfüllen
2. Klassifizierung durch Asset Owner
3. Eintrag in Asset-Inventar-System
4. Validierung durch Asset Management Team

### 2. Asset-Registrierung

Neue Assets werden registriert durch:

1. **Beschaffungsprozess**: Automatische Erfassung bei Bestellung
2. **Onboarding**: Erfassung bei Inbetriebnahme
3. **Discovery**: Identifikation durch Scanning
4. **Meldung**: Manuelle Meldung durch Mitarbeiter

### 3. Asset-Aktualisierung

Änderungen werden erfasst bei:

- Hardware-Upgrades
- Software-Updates
- Standortwechsel
- Eigentümerwechsel
- Klassifizierungsänderungen
- Statusänderungen

### 4. Asset-Außerbetriebnahme

Bei Außerbetriebnahme:

1. Asset-Status auf "Außer Betrieb" setzen
2. Sichere Datenlöschung dokumentieren
3. Physische Entsorgung oder Archivierung
4. Lizenzen freigeben
5. Abhängigkeiten auflösen

## Inventar-Kategorien

### Hardware-Assets

**Server und Infrastruktur:**
- Physische Server
- Virtuelle Maschinen
- Storage-Systeme
- Netzwerkgeräte (Router, Switches, Firewalls)

**Endgeräte:**
- Workstations und Laptops
- Mobile Geräte (Smartphones, Tablets)
- Drucker und Multifunktionsgeräte
- IoT-Geräte

### Software-Assets

**Systemsoftware:**
- Betriebssysteme
- Virtualisierungsplattformen
- Datenbankmanagementsysteme
- Middleware

**Anwendungssoftware:**
- Geschäftsanwendungen
- Entwicklungstools
- Office-Software
- Sicherheitssoftware

### Informations-Assets

**Daten:**
- Kundendaten
- Produktdaten
- Finanzdaten
- Personaldaten
- Prototypen und Entwicklungsdaten

**Dokumentation:**
- Technische Dokumentation
- Prozessdokumentation
- Verträge und Vereinbarungen
- Richtlinien und Verfahren

### Service-Assets

- Cloud-Services (IaaS, PaaS, SaaS)
- Managed Services
- Externe Dienstleistungen
- Support-Verträge

## Inventar-Verwaltung

### Verantwortlichkeiten

**Asset Management Team:**
- Pflege des Inventar-Systems
- Koordination der Inventarisierung
- Qualitätssicherung der Daten
- Berichterstattung

**Asset Owner:**
- Klassifizierung ihrer Assets
- Validierung der Asset-Informationen
- Meldung von Änderungen
- Genehmigung von Zugriffen

**IT-Abteilung:**
- Technische Erfassung von IT-Assets
- Automatisierte Discovery
- Integration mit CMDB
- Bereitstellung von Asset-Daten

### Inventar-System

[TODO] nutzt folgendes System für das Asset-Inventar:

- **System**: [TODO]
- **Zugriff**: [TODO]
- **Backup**: [TODO]
- **Integration**: [TODO]

## Inventar-Validierung

### Regelmäßige Überprüfung

**Jährliche Vollprüfung:**
- Vollständige Inventur aller Assets
- Abgleich mit physischen Beständen
- Validierung aller Asset-Informationen
- Bereinigung veralteter Einträge

**Quartalsweise Stichproben:**
- Prüfung kritischer Assets
- Validierung von Hochrisiko-Assets
- Überprüfung der Klassifizierung
- Kontrolle der Asset Owner Zuordnung

**Kontinuierliche Überwachung:**
- Automatische Konsistenzprüfungen
- Erkennung nicht erfasster Assets
- Identifikation von Abweichungen
- Alarmierung bei kritischen Änderungen

### Qualitätssicherung

Qualitätskriterien für das Inventar:

- **Vollständigkeit**: >95% aller Assets erfasst
- **Aktualität**: <5% veraltete Einträge
- **Genauigkeit**: <2% fehlerhafte Informationen
- **Konsistenz**: 100% Pflichtfelder ausgefüllt

## Integration und Schnittstellen

### CMDB-Integration

Integration mit Configuration Management Database:

- Bidirektionaler Datenaustausch
- Synchronisation von CI-Informationen
- Konsistenzprüfung
- Automatische Updates

### Change Management

Integration mit Change Management:

- Automatische Aktualisierung bei Changes
- Validierung von Asset-Änderungen
- Nachverfolgung von Konfigurationsänderungen
- Impact-Analyse

### Procurement

Integration mit Beschaffung:

- Automatische Erfassung neuer Assets
- Lizenzmanagement
- Kostenverfolgung
- Vertragsmanagement

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:

- **2.2.1**: Inventarisierung von Assets
- **2.2.2**: Eigentümerschaft von Assets
- **2.2.3**: Akzeptable Nutzung von Assets

### Assessment-Nachweise

Für TISAX-Assessments:

- Vollständiges Asset-Inventar
- Inventarisierungsprozess-Dokumentation
- Nachweise über regelmäßige Validierung
- Beispiele für Asset-Datensätze
- Berichte über Inventar-Qualität

## Berichterstattung

### Regelmäßige Berichte

**Monatlich:**
- Anzahl neu erfasster Assets
- Anzahl außer Betrieb genommener Assets
- Inventar-Qualitätskennzahlen
- Nicht zugeordnete Assets

**Quartalsweise:**
- Vollständigkeitsanalyse
- Klassifizierungsübersicht
- Asset Owner Verteilung
- Trend-Analysen

**Jährlich:**
- Gesamtinventar-Bericht
- Asset-Wert-Analyse
- Compliance-Status
- Verbesserungsempfehlungen

## Kennzahlen

[TODO] misst:

- Anzahl erfasster Assets nach Kategorie
- Inventar-Vollständigkeit (Ziel: >95%)
- Aktualität der Daten (Ziel: <30 Tage seit letzter Prüfung)
- Anteil klassifizierter Assets (Ziel: 100%)
- Anzahl nicht zugeordneter Assets (Ziel: 0)
- Zeit bis zur Erfassung neuer Assets (Ziel: <5 Tage)

<!-- Hinweis: Passen Sie die Tools und Kennzahlen an Ihre Organisation an -->

