# Anhang: Assetinventar (Template)

**Dokument-ID:** 0710
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template provides an asset inventory structure. In practice, this should be maintained in a CMDB.
Reference: BSI IT-Grundschutz-Kompendium: OPS.1.1.1 Allgemeiner IT-Betrieb
-->

## 1. Zweck und Zielsetzung

Das Assetinventar von **{{ meta-organisation.name }}** dokumentiert alle IT-Assets im Geltungsbereich des ISMS.

**Verantwortlich:** {{ meta-organisation-roles.role_CIO }}

## 2. Hinweis zur Pflege

**Empfehlung:** Dieses Inventar sollte in einer CMDB (Configuration Management Database) oder einem Asset-Management-Tool gepflegt werden. Dieses Dokument dient als Template/Export-Format.

**CMDB-System:** [TODO: z.B. ServiceNow, Device42, NetBox]  
**Ablageort:** [[ netbox.url ]] oder [TODO]

## 3. Asset-Kategorien

### 3.1 Hardware-Assets
- Server (physisch, virtuell)
- Netzwerkgeräte (Router, Switches, Firewalls)
- Storage-Systeme
- Endpoints (Laptops, Desktops, Mobile Devices)
- IoT-Geräte

### 3.2 Software-Assets
- Betriebssysteme
- Anwendungen (kommerziell, Open Source, Eigenentwicklung)
- Datenbanken
- Middleware

### 3.3 Daten-Assets
- Datenbanken
- Fileserver/Shares
- Cloud-Storage
- Backup-Medien

### 3.4 Services
- IT-Services (intern, extern)
- Cloud-Services (SaaS, PaaS, IaaS)

## 4. Asset-Register

| Asset-ID | Name | Typ | Kategorie | Owner | Standort/Region | Schutzbedarf (C/I/A) | Lebenszyklusstatus | Hersteller | Modell | Seriennummer | Anschaffungsdatum | EOL-Datum | Bemerkungen |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [[ netbox.device.id ]] | [[ netbox.device.name ]] | Server | Hardware | {{ meta-organisation-roles.role_CIO }} | [[ netbox.site.name ]] | [TODO] | Produktiv | [[ netbox.device.manufacturer ]] | [[ netbox.device.model ]] | [[ netbox.device.serial ]] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Schutzbedarf-Kategorien:**
- **Normal:** Standard-Schutzbedarf
- **Hoch:** Erhöhter Schutzbedarf
- **Sehr hoch:** Kritischer Schutzbedarf

**Lebenszyklusstatus:**
- **Planung:** In Beschaffung
- **Entwicklung:** In Entwicklung/Konfiguration
- **Produktiv:** Im Produktivbetrieb
- **Wartung:** In Wartung/Support
- **Außerbetrieb:** Stillgelegt
- **Entsorgung:** Zur Entsorgung vorgesehen

## 5. NetBox-Integration

**NetBox-Instanz:** [[ netbox.url ]]

**Verfügbare Daten aus NetBox:**
- Geräte: [[ netbox.device.name ]], [[ netbox.device.type ]], [[ netbox.device.role ]]
- Standorte: [[ netbox.site.name ]], [[ netbox.site.region ]]
- IP-Adressen: [[ netbox.ipaddress.address ]]
- VLANs: [[ netbox.vlan.name ]], [[ netbox.vlan.id ]]
- Racks: [[ netbox.rack.name ]], [[ netbox.rack.location ]]

**Synchronisation:** [TODO: Automatisch/Manuell, Frequenz]

## 6. Asset-Lifecycle-Management

### 6.1 Beschaffung
- Asset wird erfasst (Status: Planung)
- Schutzbedarf wird festgestellt
- Owner wird zugewiesen

### 6.2 Inbetriebnahme
- Asset wird konfiguriert und gehärtet
- Asset wird in Produktion überführt (Status: Produktiv)
- Monitoring wird aktiviert

### 6.3 Betrieb
- Regelmäßige Updates und Patches
- Monitoring und Wartung
- Änderungen werden dokumentiert (Change Management)

### 6.4 Außerbetriebnahme
- Asset wird stillgelegt (Status: Außerbetrieb)
- Daten werden sicher gelöscht
- Asset wird entsorgt (Status: Entsorgung)

**Referenz:** Dokument 0250 (Asset Lifecycle)

## 7. Verantwortlichkeiten (RACI)

| Aktivität | IT-Leitung | Asset-Owner | CMDB-Admin | ISB |
|---|---|---|---|---|
| Asset erfassen | A | R | I | I |
| Schutzbedarf festlegen | A | C | I | R |
| Asset aktualisieren | I | R | A | I |
| Asset-Review (jährlich) | A | R | C | C |
| Asset-Entsorgung | A | R | I | C |

**Legende:**
- **R** = Responsible (Durchführungsverantwortung)
- **A** = Accountable (Gesamtverantwortung)
- **C** = Consulted (Konsultiert)
- **I** = Informed (Informiert)

## 8. Asset-Tagging

**Tagging-Schema:**
- **Environment:** Production, Staging, Development, Test
- **Criticality:** Critical, High, Medium, Low
- **Owner:** Bereichsverantwortlicher
- **Compliance:** ISO27001, BSI, DSGVO, etc.
- **Backup:** Yes/No
- **DR:** Yes/No

**Beispiel (Cloud-Ressourcen):**
```
Environment: Production
Criticality: High
Owner: {{ meta-organisation-roles.role_CIO }}
Compliance: ISO27001, BSI
Backup: Yes
DR: Yes
```

## 9. Reporting

**Regelmäßige Reports:**
- **Monatlich:** Asset-Bestandsübersicht
- **Quartalsweise:** EOL-Report (Assets mit nahendem End-of-Life)
- **Jährlich:** Vollständiger Asset-Review

**Verantwortlich:** {{ meta-organisation-roles.role_CIO }}

## 10. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| IT-Leitung | {{ meta-organisation-roles.role_CIO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| ISB | {{ meta-organisation-roles.role_CISO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**Referenzen:**
- BSI IT-Grundschutz-Kompendium: OPS.1.1.1 Allgemeiner IT-Betrieb
- BSI IT-Grundschutz-Kompendium: OPS.1.2.2 Archivierung
- Dokument 0050: Strukturanalyse
- Dokument 0060: Schutzbedarfsfeststellung
- Dokument 0250: Asset Lifecycle

<!-- End of template -->