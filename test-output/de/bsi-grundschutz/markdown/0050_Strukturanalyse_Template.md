# Strukturanalyse (Template)

**Dokument-ID:** 0050
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



## 1. Ziel und Zweck

Die Strukturanalyse erfasst systematisch die Struktur des Informationsverbunds von **AdminSend GmbH**. Sie bildet die Grundlage für:
- Schutzbedarfsfeststellung (Dokument 0060)
- Modellierung und Bausteinzuordnung (Dokument 0070)
- Basis-Sicherheitscheck (Dokument 0080)
- Risikoanalyse (Dokument 0090)

**Verantwortlich:** [TODO] (ISB)

## 2. Vorgehen und Methodik

### 2.1 Datenquellen

Folgende Datenquellen werden für die Strukturanalyse genutzt:

| Datenquelle | Typ | Verantwortlich | Aktualität |
|---|---|---|---|
| CMDB/Asset-Inventar | System | [TODO] | [TODO] |
| Netzwerkdokumentation | Dokument | [TODO] | [TODO] |
| Architekturdiagramme | Dokument | [TODO] | [TODO] |
| Verträge mit Dienstleistern | Dokument | [TODO] | [TODO] |
| Interviews mit Stakeholdern | Primärquelle | [TODO] | [TODO] |

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
- ISB: [TODO]
- IT-Leitung: [TODO]
- Informationsverbund-Verantwortliche: [TODO]
- Fachabteilungen: [TODO]

## 3. Struktur-Register

### 3.1 Geschäftsprozesse und Services



| ID | Prozess/Service | Owner | Beschreibung | Kritikalität | Abhängigkeiten | Anwendungen |
|---|---|---|---|---|---|---|
| P-001 | [TODO: Prozess 1] | [TODO] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | [TODO: A-001, A-002] |
| P-002 | [TODO: Prozess 2] | [TODO] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | [TODO] |
| P-003 | [TODO: Prozess 3] | [TODO] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | [TODO] |

**Anzahl Prozesse gesamt:** [TODO]

### 3.2 Anwendungen



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



| ID | System/Komponente | Typ | Owner | Standort/Region | Betrieb | IP-Adresse | Bemerkungen |
|---|---|---|---|---|---|---|---|
| S-001 | [[ netbox.device.server_001 ]] | Server | [TODO] | [TODO] | Intern | [[ netbox.ip.server_001 ]] | [TODO] |
| S-002 | [TODO: System 2] | Datenbank | [TODO] | [TODO] | Intern/Extern | [TODO] | [TODO] |
| S-003 | [TODO: System 3] | Storage | [TODO] | [TODO] | Intern/Extern | [TODO] | [TODO] |
| S-004 | [TODO: System 4] | Firewall | [TODO] | [TODO] | Intern | [TODO] | [TODO] |

**Anzahl IT-Systeme gesamt:** [TODO]

**Systemtypen:**
- Server: [TODO]
- Datenbanken: [TODO]
- Storage: [TODO]
- Netzwerkkomponenten: [TODO]
- Sicherheitskomponenten: [TODO]
- Clients: [TODO]

### 3.4 Netzwerke und Kommunikation



| ID | Netz/Zone | Zweck | Segmentierung | Internetzugang | VLAN-ID | Betreiber | Sicherheitszone |
|---|---|---|---|---|---|---|---|
| N-001 | Management-Netz | Administration | Ja | Nein | [[ netbox.vlan.management ]] | [TODO] | Hochsicher |
| N-002 | Produktiv-Netz | Geschäftsanwendungen | Ja | Ja (gefiltert) | [TODO] | [TODO] | Sicher |
| N-003 | DMZ | Externe Services | Ja | Ja | [TODO] | [TODO] | Mittel |
| N-004 | Gast-WLAN | Gäste | Ja | Ja (isoliert) | [TODO] | [TODO] | Niedrig |

**Anzahl Netzwerksegmente gesamt:** [TODO]

**Sicherheitszonen:**
- Hochsicher (Management, kritische Systeme): [TODO]
- Sicher (Produktivsysteme): [TODO]
- Mittel (DMZ, externe Schnittstellen): [TODO]
- Niedrig (Gast-Netz): [TODO]

### 3.5 Räume und Standorte



| ID | Standort/Raum | Typ | Schutzmaßnahmen | Zutritt | Betreiber | Kritikalität |
|---|---|---|---|---|---|---|
| R-001 | [TODO] | Hauptstandort | [TODO] | Zugangskontrolle | AdminSend GmbH | Hoch |
| R-002 | Rechenzentrum | Serverraum | Klimatisierung, Brandschutz, Zutrittskontrolle | Autorisiert | AdminSend GmbH | Hoch |
| R-003 | [TODO: Raum 3] | [TODO] | [TODO] | [TODO] | [TODO] | Mittel/Niedrig |

**Anzahl Standorte gesamt:** [TODO]  
**Anzahl kritische Räume gesamt:** [TODO]

### 3.6 Externe Dienstleister und Cloud-Provider



| ID | Dienstleister | Service | Kritikalität | Vertrag | Zertifizierungen | Standort | Bemerkungen |
|---|---|---|---|---|---|---|---|
| D-001 | [TODO: Provider 1] | [TODO: Service] | Hoch/Mittel/Niedrig | [TODO: Vertragsnr.] | [TODO: ISO 27001, etc.] | [TODO] | [TODO] |
| D-002 | [TODO: Provider 2] | [TODO: Service] | Hoch/Mittel/Niedrig | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl Dienstleister gesamt:** [TODO]

### 3.7 Personen und Rollen



| Rolle | Name | Verantwortungsbereich | Kontakt | Stellvertreter |
|---|---|---|---|---|
| Geschäftsführung | [TODO] | Gesamtverantwortung | {{ meta-organisation-roles.role_CEO_email }} | [TODO] |
| ISB | [TODO] | ISMS-Koordination | {{ meta-organisation-roles.role_CISO_email }} | [TODO] |
| IT-Leitung | [TODO] | IT-Betrieb | {{ meta-organisation-roles.role_CIO_email }} | [TODO] |
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
1. **Review durch IT-Leitung:** [TODO]
2. **Review durch Informationsverbund-Verantwortliche:** [TODO]
3. **Abgleich mit CMDB/Inventar:** [TODO: Datum]
4. **Freigabe durch ISB:** [TODO]

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

**Verantwortlich:** [TODO] (ISB)  
**Nächster Review:** [TODO]

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | [TODO] | [TODO] | Draft |
| IT-Leitung | [TODO] | [TODO] | Draft |

**Referenzen:**
- BSI Standard 200-2: IT-Grundschutz-Methodik (Kapitel 5: Strukturanalyse)
- BSI IT-Grundschutz-Kompendium

