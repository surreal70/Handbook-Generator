# Konfigurationsmanagement und CMDB

**Dokument-ID:** [FRAMEWORK]-0090
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

## Übersicht

Dieses Dokument beschreibt das Konfigurationsmanagement und die Configuration Management Database (CMDB) für den IT-Service. Es definiert CI-Kategorien, Attribute, Beziehungen und Change-Prozesse für Configuration Items.

**Service:** {{ meta-handbook.service_name }}  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**CMDB-System:** NetBox  
**Stand:** 0

## Konfigurationsmanagement-Prozess

### Ziele des Konfigurationsmanagements

- **Transparenz:** Vollständige Übersicht über alle IT-Assets und deren Beziehungen
- **Kontrolle:** Kontrollierte Änderungen an Configuration Items
- **Compliance:** Einhaltung von Lizenz- und Compliance-Anforderungen
- **Planung:** Fundierte Basis für Kapazitäts- und Change-Planung
- **Incident-Support:** Schnellere Incident-Resolution durch CI-Informationen

### ITIL Configuration Management Aktivitäten

1. **Management and Planning:** Planung und Steuerung des Konfigurationsmanagements
2. **Configuration Identification:** Identifikation und Kategorisierung von CIs
3. **Configuration Control:** Kontrolle von Änderungen an CIs
4. **Status Accounting:** Erfassung und Reporting des CI-Status
5. **Verification and Audit:** Überprüfung der CMDB-Datenqualität

## Configuration Management Database (CMDB)

### CMDB-System: NetBox

**NetBox-Instanz:**
- **URL:** [[ netbox.url ]]
- **Version:** [TODO]
- **Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

**NetBox-Funktionen:**
- IP Address Management (IPAM)
- Data Center Infrastructure Management (DCIM)
- Device Management
- Circuit Management
- Virtualization Management
- Configuration Context

### CMDB-Struktur

```
┌─────────────────────────────────────────────────────────────┐
│                    CMDB (NetBox)                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Sites      │  │   Racks      │  │   Devices    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  IP Addresses│  │    VLANs     │  │   Circuits   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Clusters   │  │Virtual Machines│ │  Interfaces  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## CI-Kategorien und Attribute

### Hardware-CIs

#### Server
**Kategorie:** Hardware > Server  
**Attribute:**
- **Name:** [[ netbox.device.name ]]
- **Hersteller:** [[ netbox.device.manufacturer ]]
- **Modell:** [[ netbox.device.model ]]
- **Seriennummer:** [[ netbox.device.serial ]]
- **Asset-Tag:** [[ netbox.device.asset_tag ]]
- **Standort:** [[ netbox.device.site ]]
- **Rack:** [[ netbox.device.rack ]]
- **Rack-Position:** [[ netbox.device.position ]]
- **Status:** Active, Planned, Staged, Failed, Decommissioned
- **Rolle:** [[ netbox.device.role ]]
- **Primary IP:** [[ netbox.device.primary_ip ]]

#### Netzwerkgeräte
**Kategorie:** Hardware > Network  
**Attribute:**
- **Name:** [[ netbox.device.name ]]
- **Typ:** Switch, Router, Firewall, Load Balancer
- **Hersteller:** [[ netbox.device.manufacturer ]]
- **Modell:** [[ netbox.device.model ]]
- **Management-IP:** [[ netbox.device.primary_ip ]]
- **Standort:** [[ netbox.device.site ]]
- **Interfaces:** [[ netbox.device.interfaces ]]
- **VLANs:** [[ netbox.device.vlans ]]

#### Storage
**Kategorie:** Hardware > Storage  
**Attribute:**
- **Name:** [[ netbox.device.name ]]
- **Typ:** SAN, NAS, DAS
- **Kapazität:** [TODO] TB
- **Hersteller:** [[ netbox.device.manufacturer ]]
- **Standort:** [[ netbox.device.site ]]

### Software-CIs

#### Betriebssysteme
**Kategorie:** Software > Operating System  
**Attribute:**
- **Name:** [TODO: z.B. Ubuntu Server 22.04]
- **Version:** [TODO]
- **Lizenz:** [TODO]
- **Installiert auf:** [[ netbox.device.name ]]
- **Patch-Level:** [TODO]

#### Anwendungen
**Kategorie:** Software > Application  
**Attribute:**
- **Name:** [TODO: Anwendungsname]
- **Version:** [TODO]
- **Hersteller:** [TODO]
- **Lizenz:** [TODO]
- **Lizenzanzahl:** [TODO]
- **Installiert auf:** [[ netbox.device.name ]]
- **Verantwortlich:** [TODO]

### Virtualisierung-CIs

#### Hypervisor-Cluster
**Kategorie:** Virtualization > Cluster  
**Attribute:**
- **Name:** [[ netbox.cluster.name ]]
- **Typ:** [[ netbox.cluster.type ]]
- **Standort:** [[ netbox.cluster.site ]]
- **Anzahl Hosts:** [[ netbox.cluster.device_count ]]

#### Virtuelle Maschinen
**Kategorie:** Virtualization > Virtual Machine  
**Attribute:**
- **Name:** [[ netbox.vm.name ]]
- **Cluster:** [[ netbox.vm.cluster ]]
- **vCPUs:** [[ netbox.vm.vcpus ]]
- **Memory:** [[ netbox.vm.memory ]] GB
- **Disk:** [[ netbox.vm.disk ]] GB
- **Status:** Active, Offline, Staged
- **Primary IP:** [[ netbox.vm.primary_ip ]]
- **Betriebssystem:** [TODO]

### Netzwerk-CIs

#### IP-Adressen
**Kategorie:** Network > IP Address  
**Attribute:**
- **IP-Adresse:** [[ netbox.ip.address ]]
- **VLAN:** [[ netbox.ip.vlan ]]
- **Status:** Active, Reserved, Deprecated
- **DNS-Name:** [[ netbox.ip.dns_name ]]
- **Zugewiesen zu:** [[ netbox.ip.assigned_to ]]

#### VLANs
**Kategorie:** Network > VLAN  
**Attribute:**
- **VLAN-ID:** [[ netbox.vlan.vid ]]
- **Name:** [[ netbox.vlan.name ]]
- **Standort:** [[ netbox.vlan.site ]]
- **Beschreibung:** [[ netbox.vlan.description ]]

#### Circuits
**Kategorie:** Network > Circuit  
**Attribute:**
- **Circuit-ID:** [[ netbox.circuit.cid ]]
- **Provider:** [[ netbox.circuit.provider ]]
- **Typ:** [[ netbox.circuit.type ]]
- **Bandbreite:** [[ netbox.circuit.commit_rate ]] Mbps
- **Status:** Active, Planned, Decommissioned

### Standort-CIs

#### Sites
**Kategorie:** Location > Site  
**Attribute:**
- **Name:** [[ netbox.site.name ]]
- **Adresse:** [[ netbox.site.physical_address ]]
- **Facility:** [[ netbox.site.facility ]]
- **Status:** Active, Planned, Retired
- **Kontakt:** [[ netbox.site.contact_name ]]

## CI-Beziehungen

### Beziehungstypen

| Beziehung | Beschreibung | Beispiel |
|---|---|---|
| **Hosted on** | CI läuft auf anderem CI | VM hosted on Hypervisor |
| **Connected to** | Physische/logische Verbindung | Server connected to Switch |
| **Depends on** | Funktionale Abhängigkeit | Application depends on Database |
| **Part of** | Komponente eines größeren CI | Disk part of Server |
| **Uses** | CI nutzt anderes CI | Application uses IP Address |
| **Managed by** | Verwaltungsbeziehung | Device managed by Management System |

### Beziehungsdiagramm

```
┌─────────────────┐
│   Application   │
└────────┬────────┘
         │ depends on
         ▼
┌─────────────────┐
│   Database      │
└────────┬────────┘
         │ hosted on
         ▼
┌─────────────────┐
│  Virtual Machine│
└────────┬────────┘
         │ hosted on
         ▼
┌─────────────────┐
│   Hypervisor    │
└────────┬────────┘
         │ installed on
         ▼
┌─────────────────┐
│  Physical Server│
└────────┬────────┘
         │ connected to
         ▼
┌─────────────────┐
│     Switch      │
└─────────────────┘
```

### CI-Abhängigkeiten

**Beispiel: Web-Application Stack**

| CI | Abhängig von | Beziehungstyp |
|---|---|---|
| Web Application | Application Server | depends on |
| Application Server | Database Server | depends on |
| Application Server | Load Balancer | connected to |
| Database Server | Storage Array | uses |
| Application Server | Virtual Machine | hosted on |
| Virtual Machine | Hypervisor Cluster | hosted on |
| Hypervisor Cluster | Physical Servers | consists of |
| Physical Servers | Network Switch | connected to |

## Change-Prozesse für CIs

### CI-Lifecycle

```
┌─────────────┐
│   Planned   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Staged    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Active    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Deprecated  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│Decommissioned│
└─────────────┘
```

### CI-Änderungsprozess

#### 1. CI-Erstellung
**Trigger:** Neue Hardware/Software beschafft  
**Prozess:**
1. CI in CMDB anlegen (Status: Planned)
2. Attribute erfassen
3. Beziehungen definieren
4. Genehmigung durch IT Operations Manager
5. Status auf "Staged" setzen

#### 2. CI-Aktivierung
**Trigger:** CI in Betrieb genommen  
**Prozess:**
1. Change Request erstellen (siehe Kapitel 0140)
2. CI-Konfiguration durchführen
3. Tests durchführen
4. Status auf "Active" setzen
5. Monitoring aktivieren

#### 3. CI-Änderung
**Trigger:** Änderung an bestehendem CI  
**Prozess:**
1. Change Request erstellen
2. Impact-Analyse durchführen
3. Abhängige CIs identifizieren
4. Change durchführen
5. CMDB aktualisieren
6. Validierung durchführen

#### 4. CI-Deaktivierung
**Trigger:** CI außer Betrieb nehmen  
**Prozess:**
1. Change Request erstellen
2. Abhängigkeiten prüfen
3. Backup erstellen
4. CI deaktivieren
5. Status auf "Deprecated" setzen
6. Monitoring deaktivieren

#### 5. CI-Löschung
**Trigger:** CI endgültig entfernen  
**Prozess:**
1. Sicherstellen, dass keine Abhängigkeiten bestehen
2. Daten archivieren
3. Lizenzen zurückgeben
4. Status auf "Decommissioned" setzen
5. Nach Aufbewahrungsfrist aus CMDB löschen

### Change-Genehmigung für CIs

| CI-Kategorie | Genehmigung erforderlich durch | Change-Typ |
|---|---|---|
| **Kritische Server** | IT Operations Manager + CIO | Normal Change |
| **Netzwerk-Core** | IT Operations Manager + CIO | Normal Change |
| **Standard-Server** | IT Operations Manager | Standard Change |
| **Workstations** | Service Desk Lead | Standard Change |
| **IP-Adressen** | Network Administrator | Standard Change |
| **Virtuelle Maschinen** | Virtualization Admin | Standard Change |

## CMDB-Datenqualität

### Datenqualitäts-Metriken

| Metrik | Zielwert | Messfrequenz | Verantwortlich |
|---|---:|---|---|
| **Vollständigkeit** | ≥ 95% | Monatlich | CMDB Manager |
| **Genauigkeit** | ≥ 98% | Monatlich | CMDB Manager |
| **Aktualität** | ≤ 7 Tage | Wöchentlich | CMDB Manager |
| **Konsistenz** | ≥ 95% | Monatlich | CMDB Manager |
| **Eindeutigkeit** | 100% | Kontinuierlich | CMDB Manager |

### Datenqualitäts-Prozess

#### Regelmäßige Audits
- **Frequenz:** Quartalsweise
- **Umfang:** Stichprobe von 10% aller CIs
- **Methode:** Vergleich CMDB-Daten mit tatsächlichem Zustand
- **Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Automatische Validierung
- **Discovery-Tools:** Automatische Erkennung von Geräten und Software
- **Reconciliation:** Abgleich zwischen Discovery und CMDB
- **Alerts:** Benachrichtigung bei Abweichungen
- **Korrektur:** Automatische oder manuelle Korrektur

#### Manuelle Überprüfung
- **Trigger:** Vor jedem Major Change
- **Prozess:** Manuelle Überprüfung betroffener CIs
- **Dokumentation:** Änderungen dokumentieren
- **Genehmigung:** Durch IT Operations Manager

## CMDB-Zugriff und Berechtigungen

### Zugriffsrollen

| Rolle | Berechtigung | Zugriff auf |
|---|---|---|
| **CMDB Administrator** | Vollzugriff | Alle CIs |
| **IT Operations Manager** | Lesen, Schreiben, Löschen | Alle CIs |
| **Network Administrator** | Lesen, Schreiben | Netzwerk-CIs |
| **Server Administrator** | Lesen, Schreiben | Server-CIs |
| **Service Desk** | Lesen | Alle CIs |
| **Auditor** | Lesen | Alle CIs (Read-only) |

### Zugriffskontrolle

**CMDB-Administrator:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**Zugriff über:** [[ netbox.url ]]  
**Authentifizierung:** SSO/LDAP  
**Audit-Logging:** Alle Änderungen werden protokolliert

## CMDB-Integration

### Integrierte Systeme

| System | Integration | Datenfluss | Frequenz |
|---|---|---|---|
| **Monitoring** | API | CMDB → Monitoring | Real-time |
| **Ticketing** | API | CMDB ↔ Ticketing | Real-time |
| **Asset Management** | API | Asset Mgmt → CMDB | Täglich |
| **Discovery Tools** | API | Discovery → CMDB | Stündlich |
| **Backup System** | API | CMDB → Backup | Täglich |
| **Change Management** | API | CMDB ↔ Change Mgmt | Real-time |

### API-Zugriff

**NetBox API:**
- **Endpoint:** [[ netbox.url ]]/api/
- **Authentifizierung:** API Token
- **Dokumentation:** [[ netbox.url ]]/api/docs/
- **Rate Limiting:** [TODO: z.B. 1000 Requests/Stunde]

## CMDB-Reporting

### Standard-Reports

#### CI-Inventar-Report
**Frequenz:** Monatlich  
**Inhalt:**
- Anzahl CIs pro Kategorie
- CI-Status-Verteilung
- Neue CIs im letzten Monat
- Deaktivierte CIs im letzten Monat

#### Lizenz-Compliance-Report
**Frequenz:** Quartalsweise  
**Inhalt:**
- Lizenzierte Software
- Installierte Instanzen
- Lizenz-Compliance-Status
- Ablaufende Lizenzen

#### Netzwerk-Inventar-Report
**Frequenz:** Monatlich  
**Inhalt:**
- IP-Adress-Nutzung
- VLAN-Übersicht
- Netzwerkgeräte-Status
- Circuit-Übersicht

#### Change-Impact-Report
**Frequenz:** Pro Change  
**Inhalt:**
- Betroffene CIs
- Abhängige CIs
- Risikobewertung
- Rollback-Plan

## CMDB-Wartung

### Wartungsaktivitäten

#### Tägliche Aktivitäten
- [ ] Discovery-Ergebnisse reviewen
- [ ] Neue CIs validieren
- [ ] Änderungen aus Change-Tickets übernehmen
- [ ] Alerts zu Abweichungen prüfen

#### Wöchentliche Aktivitäten
- [ ] Datenqualitäts-Metriken prüfen
- [ ] Verwaiste CIs identifizieren
- [ ] Beziehungen validieren
- [ ] Backup der CMDB durchführen

#### Monatliche Aktivitäten
- [ ] CMDB-Audit durchführen
- [ ] Reports generieren und verteilen
- [ ] Lizenz-Compliance prüfen
- [ ] Veraltete CIs archivieren

#### Quartalsweise Aktivitäten
- [ ] Umfassendes CMDB-Audit
- [ ] Datenqualitäts-Review
- [ ] Prozess-Review
- [ ] Training für CMDB-Nutzer

## Best Practices

### CMDB-Best-Practices

1. **Eindeutige Identifikation:** Jedes CI muss eindeutig identifizierbar sein
2. **Konsistente Namenskonvention:** Einheitliche Benennung aller CIs
3. **Vollständige Attribute:** Alle relevanten Attribute erfassen
4. **Aktuelle Beziehungen:** Beziehungen zwischen CIs pflegen
5. **Regelmäßige Audits:** Datenqualität kontinuierlich prüfen
6. **Automatisierung:** Discovery und Reconciliation automatisieren
7. **Integration:** CMDB mit anderen Tools integrieren
8. **Dokumentation:** Änderungen dokumentieren
9. **Training:** Nutzer regelmäßig schulen
10. **Governance:** Klare Verantwortlichkeiten definieren

### Namenskonventionen

**Server:**
- Format: `[Standort]-[Typ]-[Umgebung]-[Nummer]`
- Beispiel: `MUC-SRV-PROD-001`

**Virtuelle Maschinen:**
- Format: `[Standort]-[Typ]-[Umgebung]-[Applikation]-[Nummer]`
- Beispiel: `MUC-VM-PROD-WEB-001`

**Netzwerkgeräte:**
- Format: `[Standort]-[Typ]-[Funktion]-[Nummer]`
- Beispiel: `MUC-SW-CORE-001`

## Kontakte

**CMDB-Verantwortliche:**
- **CMDB Administrator:** {{ meta-organisation-roles.role_IT_Operations_Manager }} - {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Network Administrator:** [TODO: Name] - [TODO: E-Mail]
- **Server Administrator:** [TODO: Name] - [TODO: E-Mail]
- **CIO:** [TODO] - {{ meta-organisation-roles.role_CIO_email }}

**NetBox-Support:**
- **URL:** [[ netbox.url ]]
- **Dokumentation:** [[ netbox.url ]]/docs/
- **Support:** [TODO: Support-Kontakt]

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Organisation:** AdminSend GmbH

