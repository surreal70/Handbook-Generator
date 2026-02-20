# ISMS-Geltungsbereich (Scope)

**Dokument-ID:** ISMS-0020
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



## 1. Scope-Definition

Der Geltungsbereich des Information Security Management Systems (ISMS) der **AdminSend GmbH** umfasst:

### 1.1 Organisation
- **Organisationsname:** AdminSend GmbH
- **Rechtsform:** [TODO]
- **Hauptsitz:** Musterstraße 123
- **Anzahl Mitarbeiter:** [TODO]
- **Branche:** [TODO]

### 1.2 Standorte
Das ISMS gilt für folgende Standorte:

- **Hauptstandort:** [[ netbox.site.name ]]
  - Adresse: [[ netbox.site.address ]]
  - Funktion: Rechenzentrum, Büros, Entwicklung
  
[TODO: Weitere Standorte hinzufügen]



### 1.3 Prozesse und Services
Das ISMS deckt folgende Geschäftsprozesse und IT-Services ab:

**Kernprozesse:**
- IT-Betrieb und Infrastrukturmanagement
- Softwareentwicklung und DevOps
- Datenverarbeitung und Datenmanagement
- Kundenservice und Support
- [TODO: Weitere Kernprozesse]

**IT-Services:**
- Netzwerkinfrastruktur ([[ netbox.device.core_switch.name ]])
- Server- und Virtualisierungsplattformen
- Cloud-Services und SaaS-Anwendungen
- Datenbanksysteme
- Backup- und Recovery-Systeme
- [TODO: Weitere IT-Services]

### 1.4 Informationswerte und Assets
Das ISMS schützt folgende Kategorien von Informationswerten:

**Daten und Informationen:**
- Kundendaten (personenbezogene Daten gemäß DSGVO)
- Geschäftsdaten (Verträge, Finanzdaten, Strategiedokumente)
- Technische Daten (Quellcode, Systemdokumentation, Konfigurationen)
- Mitarbeiterdaten (HR-Daten, Zugangsdaten)

**IT-Systeme und Infrastruktur:**
- Produktionssysteme und Entwicklungsumgebungen
- Netzwerkkomponenten (Router, Switches, Firewalls)
- Endgeräte (Laptops, Workstations, Mobile Devices)
- Cloud-Infrastruktur und virtuelle Maschinen

**Anwendungen und Software:**
- Geschäftsanwendungen (ERP, CRM, etc.)
- Entwicklungstools und CI/CD-Pipelines
- Kommunikationsplattformen (E-Mail, Collaboration Tools)



### 1.5 Systeme und Plattformen
Das ISMS umfasst folgende technische Plattformen:

**Netzwerkinfrastruktur:**
- Core Switch: [[ netbox.device.core_switch.name ]]
- Management VLAN: [[ netbox.vlan.management.vid ]]
- [TODO: Weitere Netzwerkkomponenten aus NetBox]

**Server und Virtualisierung:**
- [TODO: Serverliste aus Asset-Inventar]

**Cloud-Plattformen:**
- [TODO: AWS/Azure/GCP Accounts und Services]

**Sicherheitssysteme:**
- Firewall, IDS/IPS, SIEM
- Endpoint Protection (EDR/AV)
- Identity and Access Management (IAM)

## 2. Scope-Grenzen und Ausschlüsse

### 2.1 Ausgeschlossene Bereiche
Folgende Bereiche sind explizit vom ISMS-Scope ausgeschlossen:

[TODO: Ausschlüsse definieren, z.B.:]
- Produktionsstätten (falls nicht IT-relevant)
- Externe Lieferanten-Systeme (außerhalb unserer Kontrolle)
- Legacy-Systeme im Auslaufbetrieb (mit Auslaufdatum)

### 2.2 Begründung für Ausschlüsse
Für jeden Ausschluss wird eine Begründung dokumentiert:

[TODO: Begründungen für Ausschlüsse]
- **Beispiel:** Legacy-System XYZ wird am [Datum] außer Betrieb genommen und enthält keine kritischen Daten mehr.

### 2.3 Risiken und Abhängigkeiten durch Ausschlüsse
Ausschlüsse werden im Risikoregister erfasst und bewertet:

[TODO: Risikobewertung für Ausschlüsse]
- Siehe `0080_ISMS_Risikoregister_Template.md` für Details



## 3. Schnittstellen

### 3.1 Externe Organisationen und Provider
Das ISMS hat Schnittstellen zu folgenden externen Parteien:

**Cloud-Provider:**
- [TODO: AWS/Azure/GCP - Services und Verantwortlichkeiten]

**Managed Service Provider:**
- [TODO: MSP-Partner und deren Zugriffe]

**Lieferanten und Dienstleister:**
- [TODO: Kritische Lieferanten mit Zugang zu Informationswerten]



### 3.2 Andere Managementsysteme
Das ISMS ist mit folgenden anderen Managementsystemen integriert:

**Business Continuity Management (BCM):**
- Schnittstelle zu BCM-Handbuch (siehe `0440_Policy_Business_Continuity_ICT_Readiness.md`)
- Gemeinsame Risikoanalyse und BIA

**Datenschutz-Managementsystem (DSMS):**
- Schnittstelle zu DSGVO-Compliance (siehe `0560_Policy_Datenschutz_Schnittstellen.md`)
- Gemeinsame Verarbeitungsverzeichnisse und Datenschutz-Folgenabschätzungen

**Qualitätsmanagement (QMS):**
- [TODO: Schnittstellen zu ISO 9001 oder anderen QMS]

## 4. Scope-Diagramm

Das folgende Diagramm visualisiert den ISMS-Geltungsbereich:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ISMS Scope - AdminSend GmbH     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Standort 1  │  │  Standort 2  │  │ Remote Work  │         │
│  │  (Hauptsitz) │  │   (Zweig)    │  │  (Mitarb.)   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              IT-Infrastruktur                          │    │
│  │  • Netzwerk (Core, Access, DMZ)                       │    │
│  │  • Server (Prod, Dev, Test)                           │    │
│  │  • Cloud (AWS/Azure/GCP)                              │    │
│  │  • Endpoints (Laptops, Workstations, Mobile)          │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              Geschäftsprozesse                         │    │
│  │  • IT-Betrieb & Support                               │    │
│  │  • Softwareentwicklung                                │    │
│  │  • Datenverarbeitung                                  │    │
│  │  • Kundenservice                                      │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              Informationswerte                         │    │
│  │  • Kundendaten (DSGVO-relevant)                       │    │
│  │  • Geschäftsdaten (Verträge, Finanzen)               │    │
│  │  • Technische Daten (Code, Configs)                  │    │
│  │  • Mitarbeiterdaten (HR)                             │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Externe Schnittstellen:
├─ Cloud-Provider (AWS/Azure/GCP)
├─ Managed Service Provider
├─ Lieferanten und Dienstleister
└─ Kunden und Partner

Ausschlüsse:
├─ [TODO: Ausgeschlossene Bereiche]
└─ [TODO: Legacy-Systeme im Auslauf]
```



[TODO: Detailliertes Scope-Diagramm erstellen und verlinken]
- Datei: `diagrams/isms_scope.png`

## 5. Scope-Änderungen und Review

### 5.1 Änderungsmanagement
Änderungen am ISMS-Scope müssen über den Change-Management-Prozess erfolgen:
- Siehe `0360_Policy_Change_und_Release_Management.md`
- Scope-Änderungen erfordern Genehmigung durch CISO und Geschäftsführung
- Auswirkungen auf Risikoanalyse und SoA müssen bewertet werden

### 5.2 Regelmäßiger Review
Der ISMS-Scope wird regelmäßig überprüft:
- **Jährlicher Review:** Im Rahmen des Management Reviews (siehe `0140_ISMS_Management_Review_Template.md`)
- **Anlassbezogener Review:** Bei wesentlichen organisatorischen Änderungen (Merger, Akquisitionen, neue Standorte, neue Services)

## 6. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0030_ISMS_Kontext_und_Interessierte_Parteien.md` - Context of Organization
- `0050_ISMS_Strukturanalyse_Template.md` - Structure Analysis (falls vorhanden)
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA

### Externe Standards
- **ISO/IEC 27001:2022** - Clause 4.3: Determining the scope of the ISMS
- **ISO/IEC 27002:2022** - Information security controls

**Genehmigt durch:**  
[TODO], CISO  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO]

