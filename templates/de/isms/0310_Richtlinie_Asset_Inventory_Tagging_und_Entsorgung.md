# Richtlinie: Asset Inventory, Tagging und Entsorgung

**Dokument-ID:** 0310
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0300_Policy_Asset_Management.md` und definiert:
- Asset-Inventarisierung und CMDB-Verwaltung
- Asset-Tagging und Kennzeichnung
- Lifecycle-Management und Entsorgung

**Geltungsbereich:** Alle IT-Assets bei **{{ meta-organisation.name }}**

## 2. Asset-Kategorien

### 2.1 Hardware-Assets
- Laptops, Desktops, Server
- Netzwerkgeräte (Switches, Router, Firewalls)
- Mobilgeräte (Smartphones, Tablets)
- Peripherie (Monitore, Drucker, Scanner)
- Speichermedien (USB-Sticks, externe Festplatten)

### 2.2 Software-Assets
- Betriebssysteme und Lizenzen
- Anwendungssoftware
- Cloud-Subscriptions (SaaS)
- Entwicklungstools

### 2.3 Informations-Assets
- Datenbanken
- Dateisysteme und Shares
- Dokumentensammlungen
- Backup-Medien

### 2.4 Services
- Cloud-Services (IaaS, PaaS, SaaS)
- Managed Services
- Support-Verträge

## 3. Asset-Inventarisierung

### 3.1 CMDB (Configuration Management Database)

**System:** {{ meta.itsm.cmdb }} (z.B. ServiceNow, Jira Service Management)

**Pflichtfelder pro Asset:**
- Asset-ID (eindeutig)
- Asset-Typ und Kategorie
- Hersteller, Modell, Seriennummer
- Standort, Raum
- Owner, Nutzer
- Anschaffungsdatum, Kosten
- Wartungsvertrag, Support-Ende
- Status (In Betrieb, Lager, Defekt, Entsorgt)

**Zusatzfelder:**
- IP-Adresse, MAC-Adresse (Netzwerkgeräte)
- Betriebssystem, Patch-Level
- Installierte Software
- Klassifizierung (Kritikalität)
- Abhängigkeiten zu anderen Assets

### 3.2 Automatische Inventarisierung

**Tools:**
- **Endpoint-Management:** {{ meta.endpoint.management }} (z.B. Microsoft Intune, Jamf)
- **Network Discovery:** {{ meta.network.discovery }} (z.B. Nmap, Lansweeper)
- **Cloud Asset Inventory:** Native Cloud-Tools (Azure Resource Graph, AWS Config)

**Prozess:**
- Tägliche automatische Scans
- Abgleich mit CMDB
- Alerts bei unbekannten Assets (Shadow IT)
- Automatische Aktualisierung von Attributen

### 3.3 Manuelle Inventarisierung

**Anlässe:**
- Neue Asset-Beschaffung
- Asset-Übergabe an Mitarbeiter
- Standortwechsel
- Wartung oder Reparatur
- Außerbetriebnahme

**Prozess:**
1. Asset physisch prüfen
2. CMDB-Eintrag erstellen/aktualisieren
3. Asset-Tag anbringen
4. Dokumentation (Fotos bei Bedarf)
5. Übergabeprotokoll (bei Mitarbeiter-Zuweisung)

## 4. Asset-Tagging

### 4.1 Tagging-Schema

**Asset-ID-Format:** `{{ meta.asset.id_format }}`  
Beispiel: `LAP-2024-001234` (Laptop, Jahr, laufende Nummer)

**Präfixe:**
- LAP: Laptop
- DSK: Desktop
- SRV: Server
- NET: Netzwerkgerät
- MOB: Mobilgerät
- PER: Peripherie

### 4.2 Physische Tags

**Barcode/QR-Code-Labels:**
- Selbstklebend, manipulationssicher
- Anbringung an sichtbarer Stelle
- Enthält Asset-ID und QR-Code für CMDB-Link

**RFID-Tags (optional):**
- Für hochwertige Assets
- Automatische Erfassung bei Standortwechsel
- Integration mit Zutrittskontrollsystem

### 4.3 Digitale Tags

**Hostname-Konvention:**
- Format: `{{ meta.naming.hostname_format }}`
- Beispiel: `lap-jdoe-001` (Typ-Nutzer-Nummer)

**Metadaten:**
- Cloud-Resources: Tags für Owner, Kostenstelle, Umgebung
- Virtuelle Maschinen: Tags für Anwendung, Kritikalität

## 5. Asset-Lifecycle-Management

### 5.1 Beschaffung

**Prozess:**
1. Bedarfsanforderung über Ticketsystem
2. Genehmigung durch Vorgesetzten und IT-Leitung
3. Beschaffung über genehmigte Lieferanten
4. Wareneingang und Qualitätsprüfung
5. CMDB-Eintrag erstellen
6. Asset-Tag anbringen
7. Bereitstellung an Nutzer

**Dokumentation:**
- Bestellung, Rechnung
- Garantie- und Wartungsverträge
- Übergabeprotokoll

### 5.2 Betrieb

**Wartung:**
- Regelmäßige Wartung gemäß Herstellervorgaben
- Dokumentation in CMDB
- Firmware- und Software-Updates

**Monitoring:**
- Hardware-Health-Checks
- Kapazitätsplanung
- Lebenszyklusende-Tracking

### 5.3 Außerbetriebnahme

**Trigger:**
- Ende der Nutzungsdauer (typisch 3-5 Jahre)
- Defekt, nicht reparabel
- Technologiewechsel
- Mitarbeiter-Offboarding

**Prozess:**
1. Asset aus Betrieb nehmen
2. Daten sichern (falls erforderlich)
3. Daten sicher löschen (siehe Abschnitt 6)
4. CMDB-Status auf "Außer Betrieb" setzen
5. Entscheidung: Wiederverwendung, Verkauf oder Entsorgung

## 6. Sichere Datenvernichtung

### 6.1 Datenträger-Löschung

**Methoden nach DIN 66399:**

| Datenträger | Klassifizierung | Methode | Standard |
|-------------|-----------------|---------|----------|
| HDD | Intern | Software-Löschung (3-Pass) | DIN 66399 H-3 |
| HDD | Vertraulich | Degaussing + Löschung | DIN 66399 H-4 |
| HDD | Streng Vertraulich | Physische Zerstörung | DIN 66399 H-5 |
| SSD | Intern | Secure Erase (ATA) | DIN 66399 H-3 |
| SSD | Vertraulich/Streng Vertraulich | Kryptographische Löschung + Zerstörung | DIN 66399 H-5 |
| USB/SD | Alle | Physische Zerstörung | DIN 66399 H-4 |

**Tools:**
- **Software:** DBAN, Blancco, Parted Magic
- **Hardware:** Degausser, Shredder

**Dokumentation:**
- Löschprotokoll mit Asset-ID, Datum, Methode, Durchführender
- Zertifikat bei Dienstleister-Entsorgung

### 6.2 Mobile Geräte

**Prozess:**
1. Remote Wipe über MDM ({{ meta.mdm.system }})
2. Factory Reset vor Ort
3. Entfernung von SIM-Karten und SD-Karten
4. Physische Prüfung der Löschung
5. Dokumentation

### 6.3 Cloud-Daten

**Löschung:**
- Logische Löschung in Cloud-Service
- Warten auf Retention-Period-Ablauf
- Bestätigung der endgültigen Löschung durch Provider
- Dokumentation (Löschbestätigung)

## 7. Asset-Entsorgung

### 7.1 Wiederverwendung

**Intern:**
- Aufbereitung und Neuinstallation
- Zuweisung an anderen Mitarbeiter
- Nutzung als Test- oder Entwicklungsgerät

**Spende:**
- Datenvernichtung gemäß Abschnitt 6
- Entfernung aller Asset-Tags und Firmenlogos
- Dokumentation der Spende (Steuer)

### 7.2 Verkauf

**Remarketing:**
- Nur nach vollständiger Datenvernichtung
- Verkauf über zertifizierte Remarketing-Partner
- Erlös-Dokumentation

### 7.3 Entsorgung

**Zertifizierte Entsorgungspartner:**
- WEEE-zertifiziert (Waste Electrical and Electronic Equipment)
- Entsorgungsnachweis erforderlich
- Umweltgerechte Entsorgung

**Prozess:**
1. Datenvernichtung (siehe Abschnitt 6)
2. Übergabe an Entsorgungspartner
3. Entsorgungsnachweis erhalten
4. CMDB-Status auf "Entsorgt" setzen
5. Dokumentation archivieren

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| CMDB-Vollständigkeit | > 95% |
| Asset-Tagging-Rate | 100% |
| Inventur-Abweichungen | < 2% |
| Entsorgungsnachweise | 100% |

### 8.2 Regelmäßige Inventuren

**Frequenz:**
- Vollständige Inventur: Jährlich
- Stichproben: Quartalsweise
- Ad-hoc bei Verdacht auf Verlust

**Prozess:**
1. CMDB-Export
2. Physische Prüfung vor Ort
3. Abgleich CMDB vs. Realität
4. Klärung von Abweichungen
5. CMDB-Korrektur
6. Bericht an Management

### 8.3 Audit-Nachweise

- CMDB-Berichte
- Asset-Übergabeprotokolle
- Löschprotokolle
- Entsorgungsnachweise
- Inventur-Berichte

## 9. Referenzen

### Interne Dokumente
- `0300_Policy_Asset_Management.md`
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.9** - Inventory of information and other associated assets
- **ISO/IEC 27001:2022 Annex A.5.10** - Acceptable use of information
- **DIN 66399** - Vernichtung von Datenträgern
- **WEEE-Richtlinie** - Elektro- und Elektronikgeräte-Entsorgung

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

