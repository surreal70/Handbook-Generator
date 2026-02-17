# Strukturanalyse (Template)

**Dokument-ID:** 0050
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template guides the structure analysis according to BSI IT-Grundschutz Standard 200-2.
The structure analysis captures all relevant elements of the information domain.
Reference: BSI Standard 200-2 (Chapter 5: Structure Analysis)
-->

## 1. Ziel und Zweck

Die Strukturanalyse erfasst systematisch die Struktur des Informationsverbunds von **{{ meta-organisation.name }}**. Sie bildet die Grundlage für:
- Schutzbedarfsfeststellung (Dokument 0060)
- Modellierung und Bausteinzuordnung (Dokument 0070)
- Basis-Sicherheitscheck (Dokument 0080)
- Risikoanalyse (Dokument 0090)

**Verantwortlich:** {{ meta.ciso.name }} (ISB)

## 2. Vorgehen und Methodik

### 2.1 Datenquellen

Folgende Datenquellen werden für die Strukturanalyse genutzt:

| Datenquelle | Typ | Verantwortlich | Aktualität |
|---|---|---|---|
| CMDB/Asset-Inventar | System | {{ meta.cio.name }} | [TODO] |
| Netzwerkdokumentation | Dokument | {{ meta.cio.name }} | [TODO] |
| Architekturdiagramme | Dokument | {{ meta.cio.name }} | [TODO] |
| Verträge mit Dienstleistern | Dokument | [TODO] | [TODO] |
| Interviews mit Stakeholdern | Primärquelle | {{ meta.ciso.name }} | [TODO] |

### 2.2 Granularität

Die Strukturanalyse erfolgt auf folgenden Granularitätsebenen:

- **Geschäftsprozesse:** Prozessebene (nicht Aktivitätsebene)
- **Anwendungen:** Anwendungssystemebene (nicht Modulebene)
- **IT-Systeme:** Logische Systeme (Server, Datenbanken, Storage)
- **Netzwerke:** Netzwerksegmente und Zonen
- **Räume:** Standorte und kritische Räume (Rechenzentrum, Serverraum)

### 2.3 Durchführung

**Zeitplan:**
- **Start:** [TODO]
- **Datenerhebung:** [TODO: z.B. 2 Wochen]
- **Validierung:** [TODO: z.B. 1 Woche]
- **Abschluss:** [TODO]

**Beteiligte:**
- ISB: {{ meta.ciso.name }}
- IT-Leitung: {{ meta.cio.name }}
- Informationsverbund-Verantwortliche: [TODO]
- Fachabteilungen: [TODO]

## 3. Struktur-Register

### 3.1 Geschäftsprozesse und Services

<!-- 
TEMPLATE AUTHOR NOTE:
Document all business processes and IT services in scope.
Link to process documentation where available.
-->

| ID | Prozess/Service | Owner | Beschreibung | Kritikalität | Abhängigkeiten | Anwendungen |
|---|---|---|---|---|---|---|
| P-001 | [TODO: Prozess 1] | [TODO] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | [TODO: A-001, A-002] |
| P-002 | [TODO: Prozess 2] | [TODO] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | [TODO] |
| P-003 | [TODO: Prozess 3] | [TODO] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | [TODO] |

**Anzahl Prozesse gesamt:** [TODO]

### 3.2 Anwendungen

<!-- 
TEMPLATE AUTHOR NOTE:
Document all applications in scope, including SaaS and cloud applications.
-->

| ID | Anwendung | Owner | Zweck | Nutzergruppe | Schnittstellen | Hosting | Kritikalität |
|---|---|---|---|---|---|---|---|
| A-001 | [TODO: App 1] | [TODO] | [TODO] | [TODO] | [TODO] | On-Prem/Cloud/SaaS | Hoch/Mittel/Niedrig |
| A-002 | [TODO: App 2] | [TODO] | [TODO] | [TODO] | [TODO] | On-Prem/Cloud/SaaS | Hoch/Mittel/Niedrig |
| A-003 | [TODO: App 3] | [TODO] | [TODO] | [TODO] | [TODO] | On-Prem/Cloud/SaaS | Hoch/Mittel/Niedrig |

**Anzahl Anwendungen gesamt:** [TODO]

**Hosting-Verteilung:**
- On-Premise: [TODO]
- Cloud (IaaS/PaaS): [TODO]
- SaaS: [TODO]

### 3.3 IT-Systeme und Komponenten

<!-- 
TEMPLATE AUTHOR NOTE:
Document all IT systems and components. Use NetBox data where available.
-->

| ID | System/Komponente | Typ | Owner | Standort/Region | Betrieb | IP-Adresse | Bemerkungen |
|---|---|---|---|---|---|---|---|
| S-001 | {{ netbox.device.server_001 }} | Server | {{ meta.cio.name }} | [TODO] | Intern | {{ netbox.ip.server_001 }} | [TODO] |
| S-002 | [TODO: System 2] | Datenbank | {{ meta.cio.name }} | [TODO] | Intern/Extern | [TODO] | [TODO] |
| S-003 | [TODO: System 3] | Storage | {{ meta.cio.name }} | [TODO] | Intern/Extern | [TODO] | [TODO] |
| S-004 | [TODO: System 4] | Firewall | {{ meta.cio.name }} | [TODO] | Intern | [TODO] | [TODO] |

**Anzahl IT-Systeme gesamt:** [TODO]

**Systemtypen:**
- Server: [TODO]
- Datenbanken: [TODO]
- Storage: [TODO]
- Netzwerkkomponenten: [TODO]
- Sicherheitskomponenten: [TODO]
- Clients: [TODO]

### 3.4 Netzwerke und Kommunikation

<!-- 
TEMPLATE AUTHOR NOTE:
Document network segments, VLANs, and zones. Use NetBox data where available.
-->

| ID | Netz/Zone | Zweck | Segmentierung | Internetzugang | VLAN-ID | Betreiber | Sicherheitszone |
|---|---|---|---|---|---|---|---|
| N-001 | Management-Netz | Administration | Ja | Nein | {{ netbox.vlan.management }} | {{ meta.cio.name }} | Hochsicher |
| N-002 | Produktiv-Netz | Geschäftsanwendungen | Ja | Ja (gefiltert) | [TODO] | {{ meta.cio.name }} | Sicher |
| N-003 | DMZ | Externe Services | Ja | Ja | [TODO] | {{ meta.cio.name }} | Mittel |
| N-004 | Gast-WLAN | Gäste | Ja | Ja (isoliert) | [TODO] | {{ meta.cio.name }} | Niedrig |

**Anzahl Netzwerksegmente gesamt:** [TODO]

**Sicherheitszonen:**
- Hochsicher (Management, kritische Systeme): [TODO]
- Sicher (Produktivsysteme): [TODO]
- Mittel (DMZ, externe Schnittstellen): [TODO]
- Niedrig (Gast-Netz): [TODO]

### 3.5 Räume und Standorte

<!-- 
TEMPLATE AUTHOR NOTE:
Document physical locations and critical rooms.
-->

| ID | Standort/Raum | Typ | Schutzmaßnahmen | Zutritt | Betreiber | Kritikalität |
|---|---|---|---|---|---|---|
| R-001 | [TODO] | Hauptstandort | [TODO] | Zugangskontrolle | {{ meta-organisation.name }} | Hoch |
| R-002 | Rechenzentrum | Serverraum | Klimatisierung, Brandschutz, Zutrittskontrolle | Autorisiert | {{ meta-organisation.name }} | Hoch |
| R-003 | [TODO: Raum 3] | [TODO] | [TODO] | [TODO] | [TODO] | Mittel/Niedrig |

**Anzahl Standorte gesamt:** [TODO]  
**Anzahl kritische Räume gesamt:** [TODO]

### 3.6 Externe Dienstleister und Cloud-Provider

<!-- 
TEMPLATE AUTHOR NOTE:
Document all external service providers and cloud providers.
-->

| ID | Dienstleister | Service | Kritikalität | Vertrag | Zertifizierungen | Standort | Bemerkungen |
|---|---|---|---|---|---|---|---|
| D-001 | [TODO: Provider 1] | [TODO: Service] | Hoch/Mittel/Niedrig | [TODO: Vertragsnr.] | [TODO: ISO 27001, etc.] | [TODO] | [TODO] |
| D-002 | [TODO: Provider 2] | [TODO: Service] | Hoch/Mittel/Niedrig | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl Dienstleister gesamt:** [TODO]

### 3.7 Personen und Rollen

<!-- 
TEMPLATE AUTHOR NOTE:
Document key personnel and roles relevant for information security.
-->

| Rolle | Name | Verantwortungsbereich | Kontakt | Stellvertreter |
|---|---|---|---|---|
| Geschäftsführung | {{ meta.ceo.name }} | Gesamtverantwortung | {{ meta.ceo.email }} | [TODO] |
| ISB | {{ meta.ciso.name }} | ISMS-Koordination | {{ meta.ciso.email }} | [TODO] |
| IT-Leitung | {{ meta.cio.name }} | IT-Betrieb | {{ meta.cio.email }} | [TODO] |
| [TODO: Weitere Rollen] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Abhängigkeiten und Schnittstellen

### 4.1 Interne Abhängigkeiten

| Von (Quelle) | Nach (Ziel) | Typ | Kritikalität | Bemerkungen |
|---|---|---|---|---|
| [TODO: System A] | [TODO: System B] | Datenfluss | Hoch/Mittel/Niedrig | [TODO] |
| [TODO: Anwendung X] | [TODO: Datenbank Y] | Datenzugriff | Hoch/Mittel/Niedrig | [TODO] |

### 4.2 Externe Schnittstellen

| Schnittstelle | Partner/Provider | Richtung | Datenarten | Protokoll | Sicherheitsmaßnahmen |
|---|---|---|---|---|---|
| [TODO: Schnittstelle 1] | [TODO] | Eingehend/Ausgehend/Bidirektional | [TODO] | [TODO] | [TODO: VPN, TLS, etc.] |
| [TODO: Schnittstelle 2] | [TODO] | Eingehend/Ausgehend/Bidirektional | [TODO] | [TODO] | [TODO] |

## 5. Diagramme und Visualisierungen

<!-- 
TEMPLATE AUTHOR NOTE:
Create diagrams to visualize the structure:
- Network diagram
- Application architecture
- Data flow diagram
Save in: diagrams/
-->

### 5.1 Netzwerkdiagramm

![Netzwerkdiagramm](diagrams/netzwerk.png)

[TODO: Erstellen Sie ein Netzwerkdiagramm mit allen Segmenten und Zonen]

### 5.2 Anwendungsarchitektur

![Anwendungsarchitektur](diagrams/anwendungsarchitektur.png)

[TODO: Erstellen Sie ein Diagramm der Anwendungslandschaft]

### 5.3 Datenflussdiagramm

![Datenflussdiagramm](diagrams/datenfluss.png)

[TODO: Erstellen Sie ein Datenflussdiagramm für kritische Prozesse]

## 6. Validierung und Qualitätssicherung

### 6.1 Validierungsprozess

Die Strukturanalyse wird validiert durch:
1. **Review durch IT-Leitung:** {{ meta.cio.name }}
2. **Review durch Informationsverbund-Verantwortliche:** [TODO]
3. **Abgleich mit CMDB/Inventar:** [TODO: Datum]
4. **Freigabe durch ISB:** {{ meta.ciso.name }}

### 6.2 Vollständigkeitsprüfung

| Kategorie | Anzahl erfasst | Vollständigkeit | Bemerkungen |
|---|---|---|---|
| Geschäftsprozesse | [TODO] | [TODO: %] | [TODO] |
| Anwendungen | [TODO] | [TODO: %] | [TODO] |
| IT-Systeme | [TODO] | [TODO: %] | [TODO] |
| Netzwerke | [TODO] | [TODO: %] | [TODO] |
| Räume | [TODO] | [TODO: %] | [TODO] |
| Dienstleister | [TODO] | [TODO: %] | [TODO] |

## 7. Aktualisierung und Pflege

Die Strukturanalyse wird aktualisiert bei:
- Neuen IT-Systemen oder Anwendungen
- Änderungen in der Netzwerkarchitektur
- Neuen Dienstleistern oder Cloud-Services
- Organisatorischen Änderungen
- Mindestens jährlich im Rahmen des ISMS-Reviews

**Verantwortlich:** {{ meta.ciso.name }} (ISB)  
**Nächster Review:** {{ meta-handbook.next_review }}

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | {{ meta.ciso.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| IT-Leitung | {{ meta.cio.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**Referenzen:**
- BSI Standard 200-2: IT-Grundschutz-Methodik (Kapitel 5: Strukturanalyse)
- BSI IT-Grundschutz-Kompendium

<!-- End of template -->