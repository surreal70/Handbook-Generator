# Basis-Sicherheitscheck / Gap-Analyse (Template)

**Dokument-ID:** 0080  
**Dokumenttyp:** Methodik-Artefakt  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standard 200-2)  
**Owner:** IT Operations Manager  
**Version:** 1.0.0  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---



## 1. Ziel und Zweck

Der Basis-Sicherheitscheck bewertet systematisch, inwieweit die für den Informationsverbund von **AdminSend GmbH** modellierten IT-Grundschutz-Anforderungen umgesetzt sind. Er bildet die Grundlage für:
- Identifikation von Sicherheitslücken (Gaps)
- Priorisierung von Maßnahmen
- Maßnahmenplanung (Dokument 0100)
- Compliance-Nachweis

**Verantwortlich:** Thomas Weber (ISB)

## 2. Vorgehen und Methodik

### 2.1 Datenquellen

Folgende Quellen werden für den Basis-Sicherheitscheck genutzt:

| Datenquelle | Typ | Verantwortlich | Verwendung |
|---|---|---|---|
| Interviews mit Stakeholdern | Primärquelle | Thomas Weber | Prozess- und Organisationsanforderungen |
| Konfigurationsnachweise | Technisch | Anna Schmidt | Technische Anforderungen |
| Policies und Richtlinien | Dokument | Thomas Weber | Organisatorische Anforderungen |
| Tickets und Change-Records | System | Anna Schmidt | Umsetzungsnachweise |
| Logs und Monitoring-Daten | System | Anna Schmidt | Betriebsanforderungen |
| Audit-Berichte | Dokument | [TODO: Internal Audit] | Externe Validierung |

### 2.2 Bewertungslogik

**Erfüllungsgrade:**

| Status | Kürzel | Beschreibung | Kriterien |
|---|---|---|---|
| **Erfüllt** | E | Anforderung vollständig umgesetzt | Alle Aspekte der Anforderung sind implementiert und nachgewiesen |
| **Teilweise erfüllt** | T | Anforderung teilweise umgesetzt | Wesentliche Aspekte umgesetzt, aber Lücken vorhanden |
| **Nicht erfüllt** | N | Anforderung nicht umgesetzt | Anforderung nicht oder nur minimal umgesetzt |
| **Nicht anwendbar** | N/A | Anforderung nicht relevant | Anforderung trifft auf Organisation nicht zu |
| **Nicht bewertet** | - | Noch nicht geprüft | Bewertung steht noch aus |

### 2.3 Stichprobenumfang

**Prüftiefe:**
- **Kritische Anforderungen (Schutzbedarf "Sehr hoch"):** 100% Prüfung
- **Wichtige Anforderungen (Schutzbedarf "Hoch"):** Stichprobe 50%
- **Standard-Anforderungen (Schutzbedarf "Normal"):** Stichprobe 25%

**Prüfmethoden:**
- Dokumentenprüfung
- Konfigurationsprüfung
- Interviews
- Technische Tests (Stichproben)

### 2.4 Durchführung

**Zeitplan:**
- **Start:** [TODO]
- **Datenerhebung:** [TODO: z.B. 4 Wochen]
- **Bewertung:** [TODO: z.B. 2 Wochen]
- **Validierung:** [TODO: z.B. 1 Woche]
- **Abschluss:** [TODO]

**Beteiligte:**
- ISB: Thomas Weber
- IT-Leitung: Anna Schmidt
- Informationsverbund-Verantwortliche: [TODO]
- Fachabteilungen: [TODO]

## 3. Basis-Sicherheitscheck: Ergebnisse

### 3.1 ISMS und Organisation (ISMS, ORP)



| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| ISMS.1 | Sicherheitsleitlinie erstellt | AdminSend GmbH | E | Dokument 0010 | - | - | Thomas Weber | - |
| ISMS.1 | ISMS-Organisation definiert | AdminSend GmbH | E | Dokument 0020 | - | - | Thomas Weber | - |
| ISMS.1 | Ressourcen bereitgestellt | AdminSend GmbH | T | Budget-Nachweis | Budget unzureichend | Budget erhöhen | Max Mustermann | [TODO] |
| ORP.1 | Rollen und Verantwortlichkeiten definiert | AdminSend GmbH | E | Dokument 0020 | - | - | Thomas Weber | - |
| ORP.2 | Einarbeitung neuer Mitarbeitender | AdminSend GmbH | T | HR-Prozess | Keine Security-Schulung im Onboarding | Security-Schulung integrieren | [TODO: HR] | [TODO] |
| ORP.3 | Awareness-Programm | AdminSend GmbH | N | - | Kein Awareness-Programm vorhanden | Awareness-Programm aufbauen | Thomas Weber | [TODO] |
| ORP.4 | IAM-Prozess | AdminSend GmbH | T | IAM-Richtlinie | Rezertifizierung fehlt | Rezertifizierungsprozess implementieren | Anna Schmidt | [TODO] |

### 3.2 Konzeption und Vorgehensweisen (CON)

| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| CON.1 | Kryptokonzept erstellt | Kryptokonzept | N | - | Kein Kryptokonzept vorhanden | Kryptokonzept erstellen | Thomas Weber | [TODO] |
| CON.3 | Datensicherungskonzept erstellt | Backup-Konzept | E | Backup-Dokumentation | - | - | Anna Schmidt | - |
| CON.3 | Backup-Tests durchgeführt | Backup-Prozess | T | Test-Protokolle | Tests nicht regelmäßig | Quartalsweise Backup-Tests etablieren | Anna Schmidt | [TODO] |
| CON.6 | Löschkonzept erstellt | Löschkonzept | N | - | Kein Löschkonzept vorhanden | Löschkonzept erstellen | Thomas Weber | [TODO] |

### 3.3 Betrieb (OPS)

| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| OPS.1.1.2 | Administrationskonzept | IT-Administration | T | Admin-Richtlinie | Privileged Access Management fehlt | PAM-Lösung implementieren | Anna Schmidt | [TODO] |
| OPS.1.1.3 | Patch-Prozess etabliert | Patch Management | E | Patch-Dokumentation | - | - | Anna Schmidt | - |
| OPS.1.1.3 | Patch-SLAs definiert | Patch Management | T | SLA-Dokument | Kritische Patches > 30 Tage | SLA auf 7 Tage reduzieren | Anna Schmidt | [TODO] |
| OPS.1.1.4 | Malware-Schutz implementiert | Alle Systeme | E | Antivirus-Lösung | - | - | Anna Schmidt | - |
| OPS.1.1.5 | Logging aktiviert | Alle Systeme | T | Log-Konfiguration | Zentrale Log-Sammlung fehlt | SIEM implementieren | Anna Schmidt | [TODO] |
| OPS.2.2 | Cloud-Sicherheitskonzept | Cloud-Services | N | - | Kein Cloud-Sicherheitskonzept | Cloud-Sicherheitskonzept erstellen | Thomas Weber | [TODO] |

### 3.4 Detektion und Reaktion (DER)

| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| DER.1 | Detektion etabliert | Monitoring | T | Monitoring-Tools | SIEM fehlt | SIEM implementieren | Anna Schmidt | [TODO] |
| DER.2.1 | Incident-Response-Prozess | Incident Management | T | IR-Richtlinie | Keine Incident-Response-Übungen | Jährliche IR-Übung etablieren | Thomas Weber | [TODO] |
| DER.2.2 | Forensik-Vorbereitung | Forensik | N | - | Keine Forensik-Vorbereitung | Forensik-Konzept erstellen | Thomas Weber | [TODO] |

### 3.5 Anwendungen (APP)

| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| APP.3.1 | Sichere Webanwendungsentwicklung | [TODO: Webanwendung] | T | SDLC-Prozess | SAST/DAST fehlt | Security-Testing integrieren | [TODO] | [TODO] |
| APP.3.2 | Webserver-Härtung | [TODO: Webserver] | E | Härtungs-Checkliste | - | - | Anna Schmidt | - |
| APP.4.3 | Datenbank-Härtung | [TODO: Datenbank] | T | DB-Konfiguration | Verschlüsselung at rest fehlt | TDE aktivieren | Anna Schmidt | [TODO] |

### 3.6 IT-Systeme (SYS)

| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| SYS.1.1 | Server-Härtung | {{ netbox.device.server_001 }} | E | Härtungs-Baseline | - | - | Anna Schmidt | - |
| SYS.1.3 | Linux-Härtung | [TODO: Linux-Server] | T | CIS Benchmark | Nicht alle CIS-Controls umgesetzt | Vollständige CIS-Umsetzung | Anna Schmidt | [TODO] |
| SYS.1.5 | Virtualisierungs-Sicherheit | [TODO: VMware] | T | VMware-Konfiguration | Netzwerksegmentierung unzureichend | Mikrosegmentierung implementieren | Anna Schmidt | [TODO] |
| SYS.2.1 | Client-Härtung | Workstations | T | GPO-Konfiguration | BitLocker nicht flächendeckend | BitLocker auf allen Clients aktivieren | Anna Schmidt | [TODO] |
| SYS.3.2.1 | Mobile Device Management | Mobile Devices | N | - | Kein MDM vorhanden | MDM-Lösung implementieren | Anna Schmidt | [TODO] |

### 3.7 Netzwerke und Kommunikation (NET)

| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| NET.1.1 | Netzwerksegmentierung | Netzwerkarchitektur | T | Netzwerkdiagramm | Segmentierung unzureichend | Mikrosegmentierung implementieren | Anna Schmidt | [TODO] |
| NET.1.2 | Netzwerk-Monitoring | Netzwerkmanagement | E | Monitoring-Tools | - | - | Anna Schmidt | - |
| NET.3.1 | Router/Switch-Härtung | Netzwerkgeräte | T | Konfigurationsnachweise | SNMP v3 nicht überall | SNMP v3 flächendeckend | Anna Schmidt | [TODO] |
| NET.3.2 | Firewall-Regelwerk | Firewall | E | Firewall-Rules | - | - | Anna Schmidt | - |
| NET.3.3 | VPN-Sicherheit | VPN | T | VPN-Konfiguration | MFA für VPN fehlt | MFA für VPN implementieren | Anna Schmidt | [TODO] |
| NET.2.1 | WLAN-Sicherheit | WLAN | E | WLAN-Konfiguration | - | - | Anna Schmidt | - |

### 3.8 Infrastruktur (INF)

| Baustein | Anforderung (Kurz) | Objekt | Status | Nachweis/Evidence | Finding | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|---|
| INF.1 | Gebäudesicherheit | {{ meta.organization.primary_location }} | T | Sicherheitskonzept | Besuchermanagement unzureichend | Besuchermanagement-System | [TODO: Facility] | [TODO] |
| INF.2 | Rechenzentrum-Sicherheit | Rechenzentrum | E | RZ-Dokumentation | - | - | [TODO: Facility] | - |

## 4. Zusammenfassung und Statistik

### 4.1 Erfüllungsstatistik

| Bausteinschicht | Gesamt | Erfüllt (E) | Teilweise (T) | Nicht erfüllt (N) | N/A | Erfüllungsgrad |
|---|---|---|---|---|---|---|
| ISMS | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| ORP | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| CON | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| OPS | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| DER | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| APP | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| SYS | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| NET | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| INF | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| **Gesamt** | **[TODO]** | **[TODO]** | **[TODO]** | **[TODO]** | **[TODO]** | **[TODO: %]** |

**Gesamterfüllungsgrad:** [TODO: %]

### 4.2 Kritische Lücken (Priorität 1)

| ID | Anforderung | Objekt | Risiko | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|
| GAP-001 | [TODO: Kritische Lücke 1] | [TODO] | Sehr hoch | [TODO] | [TODO] | [TODO] |
| GAP-002 | [TODO: Kritische Lücke 2] | [TODO] | Sehr hoch | [TODO] | [TODO] | [TODO] |

### 4.3 Quick Wins (Priorität 2)

| ID | Anforderung | Objekt | Aufwand | Nutzen | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|---|
| QW-001 | [TODO: Quick Win 1] | [TODO] | Niedrig | Hoch | [TODO] | [TODO] | [TODO] |
| QW-002 | [TODO: Quick Win 2] | [TODO] | Niedrig | Hoch | [TODO] | [TODO] | [TODO] |

### 4.4 Mittelfristige Maßnahmen (Priorität 3)

| ID | Anforderung | Objekt | Aufwand | Maßnahme | Owner | Zieltermin |
|---|---|---|---|---|---|---|
| MF-001 | [TODO: Mittelfristige Maßnahme 1] | [TODO] | Mittel | [TODO] | [TODO] | [TODO] |
| MF-002 | [TODO: Mittelfristige Maßnahme 2] | [TODO] | Mittel | [TODO] | [TODO] | [TODO] |

## 5. Management Summary

### 5.1 Gesamtbewertung

**Erfüllungsgrad:** [TODO: %]

**Bewertung:**
- [TODO: Zusammenfassende Bewertung des Sicherheitsniveaus]
- [TODO: Haupterkenntnisse]
- [TODO: Kritische Handlungsfelder]

### 5.2 Top 5 Findings

1. **[TODO: Finding 1]:** [TODO: Beschreibung und Auswirkung]
2. **[TODO: Finding 2]:** [TODO: Beschreibung und Auswirkung]
3. **[TODO: Finding 3]:** [TODO: Beschreibung und Auswirkung]
4. **[TODO: Finding 4]:** [TODO: Beschreibung und Auswirkung]
5. **[TODO: Finding 5]:** [TODO: Beschreibung und Auswirkung]

### 5.3 Ressourcenbedarf

**Geschätzter Aufwand für Maßnahmenumsetzung:**
- **Personentage:** [TODO]
- **Budget:** [TODO]
- **Externe Unterstützung:** [TODO]
- **Zeitrahmen:** [TODO]

### 5.4 Abhängigkeiten

| Maßnahme | Abhängigkeit | Auswirkung | Mitigation |
|---|---|---|---|
| [TODO: Maßnahme 1] | [TODO: Abhängigkeit] | [TODO] | [TODO] |
| [TODO: Maßnahme 2] | [TODO: Abhängigkeit] | [TODO] | [TODO] |

## 6. Nächste Schritte

1. **Maßnahmenplanung (Dokument 0100):** Detaillierte Planung der identifizierten Maßnahmen
2. **Risikoanalyse (Dokument 0090):** Für Objekte mit erhöhtem Schutzbedarf oder nicht modellierbaren Risiken
3. **Management-Präsentation:** Vorstellung der Ergebnisse an Geschäftsführung
4. **Maßnahmenumsetzung:** Start der Umsetzung priorisierter Maßnahmen

## 7. Aktualisierung und Pflege

Der Basis-Sicherheitscheck wird wiederholt:
- Nach Abschluss wesentlicher Maßnahmen
- Bei wesentlichen Änderungen in der IT-Infrastruktur
- Mindestens jährlich im Rahmen des ISMS-Reviews

**Verantwortlich:** Thomas Weber (ISB)  
**Nächster Check:** {{ meta.document.next_review }}

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | Thomas Weber | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT-Leitung | Anna Schmidt | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| Geschäftsführung | Max Mustermann | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**Referenzen:**
- BSI Standard 200-2: IT-Grundschutz-Methodik (Kapitel 8: Basis-Sicherheitscheck)
- BSI IT-Grundschutz-Kompendium


