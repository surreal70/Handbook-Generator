# Anhang B: Asset- und Systeminventar

**Dokumenttyp:** Anhang  
**Version:** {{ meta.document.version }}  
**Datum:** {{ meta.document.date }}  
**Klassifizierung:** {{ meta.document.classification }}

---

## Zweck

Dieses Dokument stellt das zentrale Asset- und Systeminventar der Organisation dar. Es erfüllt die Anforderungen von ISO/IEC 27001:2022 Annex A 5.9 (Inventory of Information and Other Associated Assets) und dient als Grundlage für:

- Asset Management und Lifecycle-Verwaltung
- Risikobewertung und Schutzbedarfsfeststellung
- Incident Response und Business Continuity Planning
- Compliance-Nachweisführung und Audits

Das Inventar wird kontinuierlich gepflegt und mindestens quartalsweise überprüft.

## Geltungsbereich

**Organisation:** {{ meta.organization.name }}  
**ISMS Scope:** {{ meta.isms.scope }}  
**Verantwortlich:** Asset Management Team, {{ meta.ciso.name }}

---

## Asset-Kategorien

Das Inventar umfasst folgende Asset-Kategorien:

1. **Hardware Assets:** Server, Netzwerkgeräte, Endpoints, Storage
2. **Software Assets:** Betriebssysteme, Anwendungen, Lizenzen
3. **Daten Assets:** Datenbanken, Dateisysteme, Repositories
4. **Netzwerk Assets:** VLANs, Subnetze, Verbindungen
5. **Cloud Assets:** Cloud Services, SaaS-Anwendungen
6. **Physische Assets:** Räume, Infrastruktur, Dokumentation

---

## Asset-Klassifizierung

Jedes Asset wird nach folgenden Kriterien klassifiziert:

### Schutzbedarf (Confidentiality, Integrity, Availability)

| Stufe | Beschreibung | Beispiel |
|-------|--------------|----------|
| **Hoch** | Kritisch für Geschäftsbetrieb, hoher Schaden bei Kompromittierung | Produktionsdatenbanken, Core Banking Systems |
| **Mittel** | Wichtig für Geschäftsbetrieb, mittlerer Schaden bei Kompromittierung | Interne Anwendungen, Entwicklungssysteme |
| **Niedrig** | Unkritisch, geringer Schaden bei Kompromittierung | Test-Systeme, öffentliche Informationen |

### Kritikalität

| Stufe | RTO | RPO | Beschreibung |
|-------|-----|-----|--------------|
| **Tier 1** | < 4h | < 1h | Geschäftskritisch, sofortige Wiederherstellung erforderlich |
| **Tier 2** | < 24h | < 4h | Wichtig, Wiederherstellung innerhalb eines Arbeitstages |
| **Tier 3** | < 72h | < 24h | Standard, Wiederherstellung innerhalb von 3 Tagen |
| **Tier 4** | > 72h | > 24h | Unkritisch, keine zeitkritische Wiederherstellung |

---

## Hardware Assets

### Server

| Asset-ID | Hostname | Typ | Standort | Owner | Schutzbedarf (C/I/A) | Kritikalität | Status |
|----------|----------|-----|----------|-------|----------------------|--------------|--------|
| SRV-001 | {{ netbox.device.primary_server.name }} | Physical Server | {{ netbox.site.name }} | IT Operations | Hoch/Hoch/Hoch | Tier 1 | Produktiv |
| SRV-002 | {{ netbox.device.backup_server.name }} | Physical Server | {{ netbox.site.name }} | IT Operations | Hoch/Hoch/Mittel | Tier 2 | Produktiv |
| [TODO] | [TODO: Hostname] | [TODO: Typ] | [TODO: Standort] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] | [TODO: Status] |

**Hinweis:** Vollständige Server-Liste aus NetBox/CMDB importieren.

---

### Netzwerkgeräte

| Asset-ID | Hostname | Typ | Standort | Owner | Schutzbedarf (C/I/A) | Kritikalität | Status |
|----------|----------|-----|----------|-------|----------------------|--------------|--------|
| NET-001 | {{ netbox.device.core_switch.name }} | Core Switch | {{ netbox.site.name }} | Network Team | Mittel/Hoch/Hoch | Tier 1 | Produktiv |
| NET-002 | {{ netbox.device.firewall.name }} | Firewall | {{ netbox.site.name }} | Security Team | Hoch/Hoch/Hoch | Tier 1 | Produktiv |
| [TODO] | [TODO: Hostname] | [TODO: Typ] | [TODO: Standort] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] | [TODO: Status] |

**Hinweis:** Vollständige Netzwerkgeräte-Liste aus NetBox importieren.

---

### Endpoints

| Asset-ID | Hostname | Typ | Benutzer | Owner | Schutzbedarf (C/I/A) | Status |
|----------|----------|-----|----------|-------|----------------------|--------|
| WS-001 | {{ meta.ciso.workstation }} | Laptop | {{ meta.ciso.name }} | IT Operations | Hoch/Mittel/Mittel | Produktiv |
| [TODO] | [TODO: Hostname] | [TODO: Typ] | [TODO: Benutzer] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Status] |

**Hinweis:** Endpoint-Inventar aus MDM/Endpoint Management System importieren.

---

### Storage-Systeme

| Asset-ID | Name | Typ | Kapazität | Standort | Owner | Schutzbedarf (C/I/A) | Kritikalität |
|----------|------|-----|-----------|----------|-------|----------------------|--------------|
| STO-001 | {{ netbox.device.storage.name }} | SAN | [TODO: Kapazität] | {{ netbox.site.name }} | IT Operations | Hoch/Hoch/Hoch | Tier 1 |
| [TODO] | [TODO: Name] | [TODO: Typ] | [TODO: Kapazität] | [TODO: Standort] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] |

---

## Software Assets

### Betriebssysteme

| Asset-ID | Name | Version | Lizenztyp | Anzahl Lizenzen | Owner | Kritikalität |
|----------|------|---------|-----------|-----------------|-------|--------------|
| OS-001 | Windows Server | 2022 | Volume License | [TODO: Anzahl] | IT Operations | Tier 1 |
| OS-002 | Red Hat Enterprise Linux | 9.x | Subscription | [TODO: Anzahl] | IT Operations | Tier 1 |
| OS-003 | Ubuntu Server | 22.04 LTS | Open Source | Unbegrenzt | IT Operations | Tier 2 |
| [TODO] | [TODO: Name] | [TODO: Version] | [TODO: Lizenztyp] | [TODO: Anzahl] | [TODO: Owner] | [TODO: Tier] |

---

### Geschäftsanwendungen

| Asset-ID | Name | Version | Vendor | Lizenztyp | Owner | Schutzbedarf (C/I/A) | Kritikalität |
|----------|------|---------|--------|-----------|-------|----------------------|--------------|
| APP-001 | [TODO: ERP System] | [TODO: Version] | [TODO: Vendor] | [TODO: Lizenztyp] | Business Owner | Hoch/Hoch/Hoch | Tier 1 |
| APP-002 | [TODO: CRM System] | [TODO: Version] | [TODO: Vendor] | [TODO: Lizenztyp] | Sales | Hoch/Mittel/Mittel | Tier 2 |
| [TODO] | [TODO: Name] | [TODO: Version] | [TODO: Vendor] | [TODO: Lizenztyp] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] |

---

### Sicherheitssoftware

| Asset-ID | Name | Version | Typ | Abdeckung | Owner | Kritikalität |
|----------|------|---------|-----|-----------|-------|--------------|
| SEC-001 | [TODO: EDR Solution] | [TODO: Version] | Endpoint Detection & Response | Alle Endpoints | Security Team | Tier 1 |
| SEC-002 | [TODO: SIEM] | [TODO: Version] | Security Information & Event Management | Alle Systeme | Security Team | Tier 1 |
| SEC-003 | [TODO: Firewall] | [TODO: Version] | Next-Gen Firewall | Perimeter | Security Team | Tier 1 |
| [TODO] | [TODO: Name] | [TODO: Version] | [TODO: Typ] | [TODO: Abdeckung] | [TODO: Owner] | [TODO: Tier] |

---

## Daten Assets

### Datenbanken

| Asset-ID | Name | Typ | Version | Server | Owner | Schutzbedarf (C/I/A) | Kritikalität | Backup |
|----------|------|-----|---------|--------|-------|----------------------|--------------|--------|
| DB-001 | [TODO: Produktions-DB] | [TODO: PostgreSQL/MySQL/Oracle] | [TODO: Version] | SRV-001 | DBA Team | Hoch/Hoch/Hoch | Tier 1 | Täglich |
| DB-002 | [TODO: Test-DB] | [TODO: Typ] | [TODO: Version] | [TODO: Server] | DBA Team | Niedrig/Mittel/Niedrig | Tier 3 | Wöchentlich |
| [TODO] | [TODO: Name] | [TODO: Typ] | [TODO: Version] | [TODO: Server] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] | [TODO: Backup] |

---

### Dateisysteme und Shares

| Asset-ID | Name | Typ | Pfad | Server | Owner | Schutzbedarf (C/I/A) | Backup |
|----------|------|-----|------|--------|-------|----------------------|--------|
| FS-001 | [TODO: Abteilungs-Share] | SMB Share | [TODO: Pfad] | [TODO: Server] | IT Operations | Mittel/Mittel/Mittel | Täglich |
| FS-002 | [TODO: Projekt-Share] | SMB Share | [TODO: Pfad] | [TODO: Server] | Project Management | Hoch/Mittel/Mittel | Täglich |
| [TODO] | [TODO: Name] | [TODO: Typ] | [TODO: Pfad] | [TODO: Server] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Backup] |

---

### Code Repositories

| Asset-ID | Name | Typ | URL | Owner | Schutzbedarf (C/I/A) | Backup |
|----------|------|-----|-----|-------|----------------------|--------|
| REPO-001 | [TODO: Main Repository] | Git | [TODO: URL] | Development Team | Hoch/Hoch/Mittel | Täglich |
| [TODO] | [TODO: Name] | [TODO: Typ] | [TODO: URL] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Backup] |

---

## Netzwerk Assets

### VLANs

| VLAN-ID | Name | Subnet | Zweck | Sicherheitszone | Owner |
|---------|------|--------|-------|-----------------|-------|
| {{ netbox.vlan.management.vid }} | {{ netbox.vlan.management.name }} | {{ netbox.vlan.management.subnet }} | Management | Restricted | Network Team |
| {{ netbox.vlan.production.vid }} | {{ netbox.vlan.production.name }} | {{ netbox.vlan.production.subnet }} | Production | Internal | Network Team |
| [TODO] | [TODO: Name] | [TODO: Subnet] | [TODO: Zweck] | [TODO: Zone] | [TODO: Owner] |

**Hinweis:** Vollständige VLAN-Liste aus NetBox importieren.

---

### Externe Verbindungen

| Verbindungs-ID | Typ | Provider | Bandbreite | Zweck | Owner | Kritikalität |
|----------------|-----|----------|------------|-------|-------|--------------|
| WAN-001 | Internet | [TODO: Provider] | [TODO: Bandbreite] | Internet Access | Network Team | Tier 1 |
| WAN-002 | MPLS | [TODO: Provider] | [TODO: Bandbreite] | Site-to-Site | Network Team | Tier 1 |
| [TODO] | [TODO: Typ] | [TODO: Provider] | [TODO: Bandbreite] | [TODO: Zweck] | [TODO: Owner] | [TODO: Tier] |

---

## Cloud Assets

### Cloud Services (IaaS/PaaS)

| Asset-ID | Service Name | Provider | Typ | Region | Owner | Schutzbedarf (C/I/A) | Kritikalität |
|----------|--------------|----------|-----|--------|-------|----------------------|--------------|
| CLOUD-001 | [TODO: VM Instances] | [TODO: AWS/Azure/GCP] | IaaS | [TODO: Region] | Cloud Team | Hoch/Hoch/Hoch | Tier 1 |
| CLOUD-002 | [TODO: Database Service] | [TODO: Provider] | PaaS | [TODO: Region] | DBA Team | Hoch/Hoch/Hoch | Tier 1 |
| [TODO] | [TODO: Service] | [TODO: Provider] | [TODO: Typ] | [TODO: Region] | [TODO: Owner] | [TODO: C/I/A] | [TODO: Tier] |

---

### SaaS-Anwendungen

| Asset-ID | Service Name | Provider | Zweck | Benutzeranzahl | Owner | Schutzbedarf (C/I/A) |
|----------|--------------|----------|-------|----------------|-------|----------------------|
| SAAS-001 | Microsoft 365 | Microsoft | Productivity | [TODO: Anzahl] | IT Operations | Hoch/Mittel/Hoch |
| SAAS-002 | [TODO: CRM SaaS] | [TODO: Provider] | Customer Management | [TODO: Anzahl] | Sales | Hoch/Mittel/Mittel |
| [TODO] | [TODO: Service] | [TODO: Provider] | [TODO: Zweck] | [TODO: Anzahl] | [TODO: Owner] | [TODO: C/I/A] |

---

## Physische Assets

### Standorte und Räume

| Standort-ID | Name | Adresse | Typ | Sicherheitsstufe | Owner |
|-------------|------|---------|-----|------------------|-------|
| SITE-001 | {{ netbox.site.name }} | {{ netbox.site.address }} | Hauptstandort | Hoch | Facility Management |
| SITE-002 | [TODO: Zweigstelle] | [TODO: Adresse] | Zweigstelle | Mittel | Facility Management |
| [TODO] | [TODO: Name] | [TODO: Adresse] | [TODO: Typ] | [TODO: Sicherheit] | [TODO: Owner] |

---

### Serverräume und Rechenzentren

| Raum-ID | Name | Standort | Typ | Größe | Klimatisierung | Brandschutz | Zutrittskontrolle |
|---------|------|----------|-----|-------|----------------|-------------|-------------------|
| ROOM-001 | Serverraum 1 | SITE-001 | Serverraum | [TODO: m²] | Redundant | FM-200 | Biometrisch |
| [TODO] | [TODO: Name] | [TODO: Standort] | [TODO: Typ] | [TODO: Größe] | [TODO: Klima] | [TODO: Brand] | [TODO: Zutritt] |

---

### Kritische Infrastruktur

| Asset-ID | Name | Typ | Standort | Kapazität | Redundanz | Owner | Kritikalität |
|----------|------|-----|----------|-----------|-----------|-------|--------------|
| INFRA-001 | USV Anlage 1 | USV | SITE-001 | [TODO: kVA] | N+1 | Facility Management | Tier 1 |
| INFRA-002 | Klimaanlage 1 | Klimatisierung | SITE-001 | [TODO: kW] | N+1 | Facility Management | Tier 1 |
| INFRA-003 | Notstromgenerator | Generator | SITE-001 | [TODO: kW] | N | Facility Management | Tier 1 |
| [TODO] | [TODO: Name] | [TODO: Typ] | [TODO: Standort] | [TODO: Kapazität] | [TODO: Redundanz] | [TODO: Owner] | [TODO: Tier] |

---

## Asset Lifecycle Management

### Lifecycle-Phasen

| Phase | Beschreibung | Verantwortlich | Prozess |
|-------|--------------|----------------|---------|
| **Planung** | Bedarfsermittlung, Budgetierung | Business Owner | Anforderungsmanagement |
| **Beschaffung** | Auswahl, Bestellung, Lieferung | Procurement | Beschaffungsprozess |
| **Inbetriebnahme** | Installation, Konfiguration, Tests | IT Operations | Change Management |
| **Betrieb** | Nutzung, Wartung, Monitoring | IT Operations | Betriebsprozesse |
| **Wartung** | Updates, Patches, Reparaturen | IT Operations | Patch Management |
| **Außerbetriebnahme** | Dekommissionierung, Datenlöschung | IT Operations | Decommissioning Process |
| **Entsorgung** | Sichere Entsorgung oder Wiederverwendung | IT Operations | Disposal Process |

---

### Asset Owner und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten | Kontakt |
|-------|----------------------|---------|
| **Asset Owner** | Geschäftliche Verantwortung, Genehmigungen, Budget | [TODO: Name/Abteilung] |
| **Technical Owner** | Technische Verantwortung, Betrieb, Wartung | IT Operations |
| **Security Owner** | Sicherheitsanforderungen, Risikobewertung | {{ meta.ciso.name }} |
| **Data Owner** | Datenklassifizierung, Zugriffskontrolle | [TODO: Name/Abteilung] |

---

## Asset-Tagging und Kennzeichnung

### Tagging-Schema

Alle Assets werden mit folgenden Tags versehen:

| Tag-Kategorie | Beschreibung | Beispiel |
|---------------|--------------|----------|
| **Environment** | Umgebung | Production, Development, Test, QA |
| **Criticality** | Kritikalität | Tier1, Tier2, Tier3, Tier4 |
| **Owner** | Verantwortlicher | IT-Ops, Security, Development |
| **CostCenter** | Kostenstelle | [TODO: Kostenstellen] |
| **Project** | Projekt | [TODO: Projektname] |
| **Compliance** | Compliance-Anforderungen | PCI-DSS, GDPR, ISO27001 |

**Hinweis:** Tagging wird in CMDB/Asset Management System gepflegt.

---

## Inventarisierungsprozess

### Regelmäßige Überprüfung

| Aktivität | Frequenz | Verantwortlich | Dokumentation |
|-----------|----------|----------------|---------------|
| **Vollständige Inventur** | Jährlich | Asset Management Team | Inventurbericht |
| **Quartalsweise Überprüfung** | Quartalsweise | Asset Owners | Review-Protokoll |
| **Automatische Discovery** | Täglich | IT Operations | Discovery Logs |
| **Änderungsverfolgung** | Kontinuierlich | Change Management | Change Records |

---

### Discovery-Tools

| Tool | Zweck | Abdeckung | Owner |
|------|-------|-----------|-------|
| NetBox | Netzwerk- und Infrastruktur-Inventar | Netzwerkgeräte, Server, VLANs | Network Team |
| CMDB | Configuration Management Database | Alle IT-Assets | IT Operations |
| MDM | Mobile Device Management | Endpoints, Mobile Devices | IT Operations |
| Cloud Asset Inventory | Cloud Resources | Cloud Services | Cloud Team |
| [TODO: Tool] | [TODO: Zweck] | [TODO: Abdeckung] | [TODO: Owner] |

---

## Compliance und Audit

### Audit-Anforderungen

Dieses Inventar erfüllt folgende Compliance-Anforderungen:

- **ISO/IEC 27001:2022 Annex A 5.9:** Inventory of Information and Other Associated Assets
- **ISO/IEC 27001:2022 Annex A 5.10:** Acceptable Use of Information and Other Associated Assets
- **ISO/IEC 27001:2022 Annex A 8.9:** Configuration Management
- **[TODO: Weitere Compliance-Anforderungen]**

---

### Audit Trail

| Datum | Änderung | Durchgeführt von | Genehmigt von | Grund |
|-------|----------|------------------|---------------|-------|
| {{ meta.document.date }} | Initiale Erstellung | {{ meta.document.author }} | {{ meta.ciso.name }} | ISMS-Implementierung |
| [TODO: Datum] | [TODO: Änderung] | [TODO: Name] | [TODO: Name] | [TODO: Grund] |

---

## Referenzen

- Policy: 0300_Policy_Asset_Management.md
- Richtlinie: 0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md
- Dokument: 0100_ISMS_Statement_of_Applicability_SoA_Template.md
- Anhang: 0730_Anhang_Datenfluss_und_Schnittstellen_Template.md

---

**Dokumentverantwortlicher:** Asset Management Team  
**Genehmigt durch:** {{ meta.ciso.name }}  
**Nächste Überprüfung:** Quartalsweise

<!-- 
TEMPLATE AUTHOR NOTE:
Dieses Inventar sollte aus automatisierten Systemen (NetBox, CMDB, MDM) generiert werden.
Manuelle Pflege ist fehleranfällig und sollte minimiert werden.
Stellen Sie sicher, dass alle Assets mit korrekten Schutzbedarfen und Kritikalitäten versehen sind.
Integrieren Sie dieses Inventar in Ihre Risikobewertungs- und BIA-Prozesse.
-->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
