# Modellierung: Bausteinzuordnung (Template)

**Dokument-ID:** BSI-GRUNDSCHUTZ-0070
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

Die Modellierung ordnet den Objekten des Informationsverbunds von **AdminSend GmbH** geeignete IT-Grundschutz-Bausteine zu. Sie bildet die Grundlage für:
- Basis-Sicherheitscheck (Dokument 0080)
- Identifikation umzusetzender Anforderungen
- Systematische Sicherheitsmaßnahmen-Planung

**Verantwortlich:** [TODO] (ISB)

**Wichtig:** Dieses Dokument referenziert nur Bausteine. Die vollständigen Bausteintexte befinden sich im BSI IT-Grundschutz-Kompendium und werden nicht kopiert.

## 2. IT-Grundschutz-Bausteine: Übersicht

### 2.1 Bausteinstruktur

Das BSI IT-Grundschutz-Kompendium gliedert Bausteine in folgende Schichten:

| Schicht | Kürzel | Beschreibung | Beispiele |
|---|---|---|---|
| **ISMS** | ISMS | Sicherheitsmanagement | ISMS.1 Sicherheitsmanagement |
| **Organisation und Personal** | ORP | Organisatorische Prozesse | ORP.1 Organisation, ORP.3 Sensibilisierung und Schulung |
| **Konzeption und Vorgehensweisen** | CON | Konzepte und Methoden | CON.1 Kryptokonzept, CON.3 Datensicherungskonzept |
| **Betrieb** | OPS | IT-Betriebsprozesse | OPS.1.1.2 Ordnungsgemäße IT-Administration |
| **Detektion und Reaktion** | DER | Incident Management | DER.1 Detektion von sicherheitsrelevanten Ereignissen |
| **Systeme** | SYS | IT-Systeme | SYS.1.1 Allgemeiner Server, SYS.2.1 Allgemeiner Client |
| **Anwendungen** | APP | Anwendungssoftware | APP.1.1 Office-Produkte, APP.3.1 Webanwendungen |
| **IT-Systeme** | NET | Netzwerke und Kommunikation | NET.1.1 Netzarchitektur und -design, NET.3.1 Router und Switches |
| **Industrielle IT** | IND | OT/ICS-Systeme | IND.1 Betriebs- und Steuerungstechnik |

### 2.2 Zuordnungslogik

**Prinzipien:**
1. **Vollständigkeit:** Alle relevanten Objekte erhalten Bausteinzuordnungen
2. **Angemessenheit:** Bausteine passen zum Objekttyp und Schutzbedarf
3. **Keine Redundanz:** Jeder Baustein wird nur einmal pro Objekt zugeordnet
4. **Granularität:** Zuordnung auf sinnvoller Abstraktionsebene

**Vorgehen:**
1. Objekte aus Strukturanalyse (Dokument 0050) übernehmen
2. Passende Bausteine aus IT-Grundschutz-Kompendium identifizieren
3. Zuordnung dokumentieren
4. Validierung durch IT-Leitung und ISB

## 3. Bausteinzuordnung

### 3.1 ISMS und Organisation (ISMS, ORP)



| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| ORG-001 | AdminSend GmbH | Organisation | ISMS.1 Sicherheitsmanagement | Gesamtorganisation | [TODO] |
| ORG-001 | AdminSend GmbH | Organisation | ORP.1 Organisation | Organisationsstruktur | [TODO] |
| ORG-001 | AdminSend GmbH | Organisation | ORP.2 Personal | Personalmanagement | [TODO: HR] |
| ORG-001 | AdminSend GmbH | Organisation | ORP.3 Sensibilisierung und Schulung | Awareness-Programm | [TODO] |
| ORG-001 | AdminSend GmbH | Organisation | ORP.4 Identitäts- und Berechtigungsmanagement | IAM-Prozesse | [TODO] |
| ORG-001 | AdminSend GmbH | Organisation | ORP.5 Compliance Management (Anforderungsmanagement) | Compliance | [TODO] |

### 3.2 Konzeption und Vorgehensweisen (CON)

| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| CON-001 | Kryptokonzept | Konzept | CON.1 Kryptokonzept | Verschlüsselungsstrategie | [TODO] |
| CON-002 | Datensicherungskonzept | Konzept | CON.3 Datensicherungskonzept | Backup-Strategie | [TODO] |
| CON-003 | Löschkonzept | Konzept | CON.6 Löschen und Vernichten | Datenlöschung | [TODO] |
| CON-004 | Patch- und Änderungsmanagement | Konzept | CON.7 Informationssicherheit auf Auslandsreisen | [TODO: falls zutreffend] | [TODO] |
| CON-005 | Softwareentwicklung | Konzept | CON.8 Software-Entwicklung | [TODO: falls zutreffend] | [TODO] |

### 3.3 Betrieb (OPS)

| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| OPS-001 | IT-Betrieb | Betriebsprozess | OPS.1.1.2 Ordnungsgemäße IT-Administration | IT-Administration | [TODO] |
| OPS-002 | Patch Management | Betriebsprozess | OPS.1.1.3 Patch- und Änderungsmanagement | Patch-Prozess | [TODO] |
| OPS-003 | Schutz vor Schadprogrammen | Betriebsprozess | OPS.1.1.4 Schutz vor Schadprogrammen | Malware-Schutz | [TODO] |
| OPS-004 | Datensicherung | Betriebsprozess | OPS.1.1.5 Protokollierung | Logging | [TODO] |
| OPS-005 | Software-Tests | Betriebsprozess | OPS.1.1.6 Software-Tests und -Freigaben | [TODO: falls zutreffend] | [TODO] |
| OPS-006 | Outsourcing | Betriebsprozess | OPS.2.1 Outsourcing für Kunden | [TODO: falls zutreffend] | [TODO] |
| OPS-007 | Cloud-Nutzung | Betriebsprozess | OPS.2.2 Cloud-Nutzung | Cloud-Services | [TODO] |

### 3.4 Detektion und Reaktion (DER)

| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| DER-001 | Detektion | Prozess | DER.1 Detektion von sicherheitsrelevanten Ereignissen | SIEM, Monitoring | [TODO] |
| DER-002 | Incident Management | Prozess | DER.2.1 Behandlung von Sicherheitsvorfällen | Incident Response | [TODO] |
| DER-003 | Forensik | Prozess | DER.2.2 Vorsorge für die IT-Forensik | [TODO: falls zutreffend] | [TODO] |
| DER-004 | Audits | Prozess | DER.3.1 Audits und Revisionen | Internal Audit | [TODO] |

### 3.5 Anwendungen (APP)



| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| A-001 | [TODO: Anwendung 1] | Anwendung | APP.1.1 Office-Produkte | [TODO: falls Office-Anwendung] | [TODO] |
| A-002 | [TODO: Anwendung 2] | Anwendung | APP.3.1 Webanwendungen | [TODO: falls Webanwendung] | [TODO] |
| A-003 | [TODO: Anwendung 3] | Anwendung | APP.3.2 Webserver | [TODO: falls Webserver] | [TODO] |
| A-004 | [TODO: Anwendung 4] | Anwendung | APP.3.3 Fileserver | [TODO: falls Fileserver] | [TODO] |
| A-005 | [TODO: Anwendung 5] | Anwendung | APP.3.6 DNS-Server | [TODO: falls DNS] | [TODO] |
| A-006 | [TODO: Anwendung 6] | Anwendung | APP.4.3 Relationale Datenbanksysteme | [TODO: falls Datenbank] | [TODO] |
| A-007 | [TODO: Anwendung 7] | Anwendung | APP.5.1 Allgemeine Groupware | [TODO: falls Groupware] | [TODO] |
| A-008 | [TODO: Anwendung 8] | Anwendung | APP.5.2 Microsoft Exchange und Outlook | [TODO: falls Exchange] | [TODO] |

### 3.6 IT-Systeme (SYS)



| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| S-001 | [[ netbox.device.server_001 ]] | Server | SYS.1.1 Allgemeiner Server | Allgemeiner Server | [TODO] |
| S-002 | [TODO: Linux-Server] | Server | SYS.1.3 Server unter Linux und Unix | Linux-Server | [TODO] |
| S-003 | [TODO: Windows-Server] | Server | SYS.1.2.3 Windows Server | Windows-Server | [TODO] |
| S-004 | [TODO: Virtualisierung] | Virtualisierung | SYS.1.5 Virtualisierung | VMware/Hyper-V | [TODO] |
| S-005 | [TODO: Container] | Container | SYS.1.6 Containerisierung | Docker/Kubernetes | [TODO] |
| S-006 | [TODO: Storage] | Storage | SYS.1.8 Speicherlösungen | SAN/NAS | [TODO] |
| S-007 | [TODO: Client] | Client | SYS.2.1 Allgemeiner Client | Workstations | [TODO] |
| S-008 | [TODO: Windows-Client] | Client | SYS.2.2.3 Clients unter Windows | Windows-Clients | [TODO] |
| S-009 | [TODO: macOS-Client] | Client | SYS.2.4 Clients unter macOS | macOS-Clients | [TODO] |
| S-010 | [TODO: Mobile Device] | Mobile | SYS.3.2.1 Allgemeine Smartphones und Tablets | Mobile Devices | [TODO] |
| S-011 | [TODO: IoT] | IoT | SYS.4.4 Allgemeines IoT-Gerät | [TODO: falls IoT] | [TODO] |

### 3.7 Netzwerke und Kommunikation (NET)



| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| N-001 | Netzwerkarchitektur | Netzwerk | NET.1.1 Netzarchitektur und -design | Gesamtnetzwerk | [TODO] |
| N-002 | Netzwerkmanagement | Netzwerk | NET.1.2 Netzmanagement | Netzwerk-Monitoring | [TODO] |
| N-003 | [TODO: Router/Switches] | Netzwerkkomponente | NET.3.1 Router und Switches | Netzwerkgeräte | [TODO] |
| N-004 | [TODO: Firewall] | Sicherheitskomponente | NET.3.2 Firewall | Perimeter-Schutz | [TODO] |
| N-005 | [TODO: VPN] | Sicherheitskomponente | NET.3.3 VPN | Remote-Zugriff | [TODO] |
| N-006 | [TODO: WLAN] | Netzwerk | NET.2.1 WLAN-Betrieb | Wireless-Netzwerk | [TODO] |
| N-007 | [TODO: E-Mail] | Kommunikation | NET.4.1 TLS-Verschlüsselung | [TODO: falls zutreffend] | [TODO] |

### 3.8 Industrielle IT (IND) - Optional



| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| IND-001 | [TODO: OT-System] | OT/ICS | IND.1 Betriebs- und Steuerungstechnik | [TODO: falls OT im Scope] | [TODO] |
| IND-002 | [TODO: ICS-Komponente] | OT/ICS | IND.2.1 Allgemeine ICS-Komponente | [TODO: falls ICS im Scope] | [TODO] |

### 3.9 Räume und Infrastruktur (INF)

| Objekt-ID | Objekt | Objektklasse | Zugeordnete Bausteine | Begründung | Owner |
|---|---|---|---|---|---|
| R-001 | Rechenzentrum | Raum | INF.2 Rechenzentrum sowie Serverraum | Kritischer Serverraum | [TODO: Facility] |
| R-002 | [TODO] | Gebäude | INF.1 Allgemeines Gebäude | Hauptstandort | [TODO: Facility] |
| R-003 | [TODO: Büroraum] | Raum | INF.8 Häuslicher Arbeitsplatz | [TODO: falls Home Office] | [TODO] |

## 4. Zusammenfassung und Statistik

### 4.1 Zuordnungsstatistik

| Bausteinschicht | Anzahl zugeordneter Bausteine | Anzahl betroffener Objekte |
|---|---|---|
| ISMS | [TODO] | [TODO] |
| ORP (Organisation und Personal) | [TODO] | [TODO] |
| CON (Konzeption) | [TODO] | [TODO] |
| OPS (Betrieb) | [TODO] | [TODO] |
| DER (Detektion und Reaktion) | [TODO] | [TODO] |
| APP (Anwendungen) | [TODO] | [TODO] |
| SYS (Systeme) | [TODO] | [TODO] |
| NET (Netzwerke) | [TODO] | [TODO] |
| IND (Industrielle IT) | [TODO] | [TODO] |
| INF (Infrastruktur) | [TODO] | [TODO] |
| **Gesamt** | **[TODO]** | **[TODO]** |

### 4.2 Vollständigkeitsprüfung

| Objekttyp | Anzahl Objekte | Anzahl mit Bausteinzuordnung | Vollständigkeit |
|---|---|---|---|
| Prozesse | [TODO] | [TODO] | [TODO: %] |
| Anwendungen | [TODO] | [TODO] | [TODO: %] |
| IT-Systeme | [TODO] | [TODO] | [TODO: %] |
| Netzwerke | [TODO] | [TODO] | [TODO: %] |
| Räume | [TODO] | [TODO] | [TODO: %] |

### 4.3 Offene Punkte

| ID | Objekt | Problem | Verantwortlich | Frist |
|---|---|---|---|---|
| [TODO] | [TODO] | [TODO: Kein passender Baustein gefunden] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO: Unklare Zuordnung] | [TODO] | [TODO] |

## 5. Validierung und Qualitätssicherung

### 5.1 Validierungsprozess

Die Bausteinzuordnung wird validiert durch:
1. **Review durch IT-Leitung:** [TODO] - Technische Korrektheit
2. **Review durch Informationsverbund-Verantwortliche:** Vollständigkeit
3. **Abgleich mit IT-Grundschutz-Kompendium:** Aktualität der Bausteine
4. **Freigabe durch ISB:** [TODO]

### 5.2 Qualitätskriterien

| Kriterium | Status | Bemerkungen |
|---|---|---|
| Alle Objekte haben Bausteinzuordnungen | [TODO: ✓/✗] | [TODO] |
| Bausteine sind aktuell (IT-Grundschutz-Kompendium Edition [TODO]) | [TODO: ✓/✗] | [TODO] |
| Zuordnungen sind nachvollziehbar begründet | [TODO: ✓/✗] | [TODO] |
| Keine Redundanzen | [TODO: ✓/✗] | [TODO] |
| Owner sind benannt | [TODO: ✓/✗] | [TODO] |

## 6. Nächste Schritte

Nach Abschluss der Modellierung folgen:
1. **Basis-Sicherheitscheck (Dokument 0080):** Abgleich Soll-Ist für alle zugeordneten Bausteine
2. **Risikoanalyse (Dokument 0090):** Für Objekte mit erhöhtem Schutzbedarf oder nicht modellierbaren Risiken
3. **Maßnahmenplanung (Dokument 0100):** Umsetzungsplanung identifizierter Anforderungen

## 7. Aktualisierung und Pflege

Die Bausteinzuordnung wird aktualisiert bei:
- Neuen IT-Systemen oder Anwendungen
- Änderungen in der IT-Architektur
- Neuer Edition des IT-Grundschutz-Kompendiums
- Mindestens jährlich im Rahmen des ISMS-Reviews

**Verantwortlich:** [TODO] (ISB)  
**Nächster Review:** [TODO]

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | [TODO] | [TODO] | Draft |
| IT-Leitung | [TODO] | [TODO] | Draft |

**Referenzen:**
- BSI Standard 200-2: IT-Grundschutz-Methodik (Kapitel 7: Modellierung)
- BSI IT-Grundschutz-Kompendium (aktuelle Edition)
- BSI IT-Grundschutz-Kompendium: https://www.bsi.bund.de/grundschutz-kompendium

