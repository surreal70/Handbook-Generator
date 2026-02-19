# Kontakte, Eskalation und Anbieter

**Dokument-ID:** [FRAMEWORK]-0270
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

## Übersicht

Dieses Dokument enthält Kontaktlisten, Eskalationspfade, Anbieter und Lieferanten sowie Support-Kontakte für den IT-Service. Ziel ist es, schnellen Zugriff auf relevante Kontaktinformationen in allen Situationen zu gewährleisten.

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

## Interne Kontakte

### Management

#### Chief Executive Officer (CEO)
- **Name:** {{ meta-organisation-roles.role_CEO }}
- **E-Mail:** {{ meta-organisation-roles.role_CEO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CEO_phone }}
- **Verfügbarkeit:** Mo-Fr 09:00-18:00
- **Eskalation:** Nur für kritische Business-Impact-Situationen

#### Chief Information Officer (CIO)
- **Name:** {{ meta-organisation-roles.role_CIO }}
- **E-Mail:** {{ meta-organisation-roles.role_CIO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CIO_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Eskalation:** IT-strategische Entscheidungen, kritische Incidents

#### Chief Information Security Officer (CISO)
- **Name:** {{ meta-organisation-roles.role_CISO }}
- **E-Mail:** {{ meta-organisation-roles.role_CISO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CISO_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00, 24/7 für Security-Incidents
- **Eskalation:** Security-Incidents, Compliance-Fragen

#### Chief Financial Officer (CFO)
- **Name:** {{ meta-organisation-roles.role_CFO }}
- **E-Mail:** {{ meta-organisation-roles.role_CFO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CFO_phone }}
- **Verfügbarkeit:** Mo-Fr 09:00-17:00
- **Eskalation:** Budget-Fragen, finanzielle Genehmigungen

#### Chief Operating Officer (COO)
- **Name:** {{ meta-organisation-roles.role_COO }}
- **E-Mail:** {{ meta-organisation-roles.role_COO_email }}
- **Telefon:** {{ meta-organisation-roles.role_COO_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Eskalation:** Betriebliche Auswirkungen, Prozessfragen

### IT-Operations

#### IT Operations Manager
- **Name:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
- **E-Mail:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Telefon:** {{ meta-organisation-roles.role_IT_Operations_Manager_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00, On-Call für P1-Incidents
- **Verantwortung:** Gesamtverantwortung IT-Betrieb

#### Service Desk Lead
- **Name:** {{ meta-organisation-roles.role_Service_Desk_Lead }}
- **E-Mail:** {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **Telefon:** {{ meta-organisation-roles.role_Service_Desk_Lead_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Verantwortung:** First-Level-Support, Ticket-Management

#### Operations Team
- **E-Mail:** [TODO: ops-team@example.com]
- **Telefon:** [TODO: +49 89 12345678-250]
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Verantwortung:** Täglicher Betrieb, Monitoring, Incident-Response

### Spezialisierte Teams

#### Network Team
- **Team Lead:** [TODO: Name]
- **E-Mail:** [TODO: network-team@example.com]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Verantwortung:** Netzwerk-Infrastruktur, Firewall, VPN

#### Security Team
- **Team Lead:** {{ meta-organisation-roles.role_CISO }}
- **E-Mail:** [TODO: security-team@example.com]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** Mo-Fr 08:00-18:00, 24/7 für Security-Incidents
- **Verantwortung:** IT-Sicherheit, Compliance, Incident-Response

#### Database Team
- **Team Lead:** [TODO: Name]
- **E-Mail:** [TODO: dba-team@example.com]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Verantwortung:** Datenbank-Administration, Performance-Tuning

#### Application Team
- **Team Lead:** [TODO: Name]
- **E-Mail:** [TODO: app-team@example.com]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Verantwortung:** Anwendungs-Support, Deployment

## On-Call und Rufbereitschaft

### On-Call-Rotation

#### Primärer On-Call
- **Aktuell:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Mobilnummer]
- **Verfügbarkeit:** 24/7
- **Rotation:** Wöchentlich (Montag 08:00 Uhr)

#### Sekundärer On-Call (Backup)
- **Aktuell:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Mobilnummer]
- **Verfügbarkeit:** 24/7
- **Rotation:** Wöchentlich (Montag 08:00 Uhr)

### On-Call-Kalender
- **URL:** [TODO: Kalender-URL]
- **Zugriff:** Alle IT-Mitarbeiter
- **Aktualisierung:** Automatisch durch Rotation-Tool

### On-Call-Richtlinien
- **Reaktionszeit P1:** 15 Minuten
- **Reaktionszeit P2:** 1 Stunde
- **Erreichbarkeit:** Telefon und E-Mail
- **Eskalation:** Nach 30 Minuten ohne Antwort

## Eskalationspfade

### Incident-Eskalation

#### Level 1: Service Desk
- **Kontakt:** {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **Telefon:** {{ meta-organisation-roles.role_Service_Desk_Lead_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00
- **Verantwortung:** First-Level-Support, Ticket-Erstellung

**Eskalation zu Level 2:**
- P1: Sofort
- P2: Nach 1 Stunde ohne Lösung
- P3: Nach 4 Stunden ohne Lösung
- P4: Nach 8 Stunden ohne Lösung

#### Level 2: Operations Team
- **Kontakt:** [TODO: ops-team@example.com]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** Mo-Fr 08:00-18:00, On-Call 24/7
- **Verantwortung:** Second-Level-Support, technische Analyse

**Eskalation zu Level 3:**
- P1: Nach 2 Stunden ohne Lösung
- P2: Nach 4 Stunden ohne Lösung
- P3: Nach 8 Stunden ohne Lösung

#### Level 3: IT Operations Manager
- **Kontakt:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Telefon:** {{ meta-organisation-roles.role_IT_Operations_Manager_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00, On-Call für P1
- **Verantwortung:** Koordination, Ressourcen-Allokation

**Eskalation zu Level 4:**
- P1: Nach 4 Stunden ohne Lösung
- P2: Nach 8 Stunden ohne Lösung
- Wenn externe Unterstützung erforderlich

#### Level 4: CIO
- **Kontakt:** {{ meta-organisation-roles.role_CIO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CIO_phone }}
- **Verfügbarkeit:** Mo-Fr 08:00-18:00, erreichbar für kritische Incidents
- **Verantwortung:** Strategische Entscheidungen, Management-Kommunikation

**Eskalation zu Level 5:**
- Kritischer Business-Impact
- Medienrelevanz
- Regulatorische Auswirkungen

#### Level 5: CEO
- **Kontakt:** {{ meta-organisation-roles.role_CEO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CEO_phone }}
- **Verfügbarkeit:** Nach Vereinbarung
- **Verantwortung:** Unternehmensweite Entscheidungen

### Security-Incident-Eskalation

#### Level 1: Security Team
- **Kontakt:** [TODO: security-team@example.com]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** 24/7
- **Verantwortung:** Incident-Response, Forensik

**Eskalation zu Level 2:**
- Kritischer Security-Incident
- Datenverlust oder -diebstahl
- Compliance-Verletzung

#### Level 2: CISO
- **Kontakt:** {{ meta-organisation-roles.role_CISO_email }}
- **Telefon:** {{ meta-organisation-roles.role_CISO_phone }}
- **Verfügbarkeit:** 24/7 für Security-Incidents
- **Verantwortung:** Security-Strategie, Compliance

**Eskalation zu Level 3:**
- Schwerwiegender Datenverlust
- Öffentliche Bekanntmachung erforderlich
- Regulatorische Meldepflicht

#### Level 3: CIO / CEO
- **Kontakt:** {{ meta-organisation-roles.role_CIO_email }} / {{ meta-organisation-roles.role_CEO_email }}
- **Verfügbarkeit:** Nach Vereinbarung
- **Verantwortung:** Unternehmensweite Kommunikation, rechtliche Schritte

## Externe Anbieter und Lieferanten

### Hardware-Anbieter

#### [TODO: Hardware-Vendor Name]
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Support-Hotline:** [TODO: Support-Nummer]
- **Vertragsnummer:** [TODO: Vertragsnummer]
- **Vertragsende:** [TODO: Datum]
- **Support-Level:** [TODO: 24/7, Business Hours]
- **Reaktionszeit:** [TODO: 4h, 8h, Next Business Day]
- **Leistungen:**
  - Hardware-Lieferung
  - Garantie und Reparatur
  - Ersatzteil-Service

### Software-Anbieter

#### [TODO: Software-Vendor Name]
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Support-Portal:** [TODO: URL]
- **Vertragsnummer:** [TODO: Vertragsnummer]
- **Lizenzanzahl:** [TODO: Anzahl]
- **Vertragsende:** [TODO: Datum]
- **Support-Level:** [TODO: Standard, Premium, Enterprise]
- **Leistungen:**
  - Software-Updates
  - Bug-Fixes
  - Technischer Support
  - Schulungen

### Cloud-Provider

#### [TODO: Cloud-Provider Name]
- **Account-Manager:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Support-Hotline:** [TODO: Support-Nummer]
- **Account-ID:** [TODO: Account-ID]
- **Support-Plan:** [TODO: Basic, Business, Enterprise]
- **Leistungen:**
  - Cloud-Infrastruktur
  - 24/7 Support
  - SLA: [TODO: Verfügbarkeit]
  - Technischer Support

**Support-Kanäle:**
- **Telefon:** [TODO: Nummer]
- **Chat:** [TODO: URL]
- **Ticket:** [TODO: Portal-URL]
- **Emergency:** [TODO: Emergency-Nummer]

### Netzwerk-Provider

#### Internet-Provider
- **Anbieter:** [TODO: Provider-Name]
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Störungshotline:** [TODO: Störungs-Nummer]
- **Vertragsnummer:** [TODO: Vertragsnummer]
- **Bandbreite:** [TODO: Bandbreite]
- **SLA:** [TODO: Verfügbarkeit]
- **Leistungen:**
  - Internet-Konnektivität
  - 24/7 Support
  - Störungsbehebung

### Managed-Service-Provider

#### [TODO: MSP Name]
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Support-Hotline:** [TODO: Support-Nummer]
- **Vertragsnummer:** [TODO: Vertragsnummer]
- **Vertragsende:** [TODO: Datum]
- **Support-Level:** [TODO: 24/7, Business Hours]
- **Leistungen:**
  - [TODO: Managed Services]
  - [TODO: Monitoring]
  - [TODO: Support]

### Backup-Service-Provider

#### [TODO: Backup-Provider Name]
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Support-Hotline:** [TODO: Support-Nummer]
- **Vertragsnummer:** [TODO: Vertragsnummer]
- **Storage-Kapazität:** [TODO: Kapazität]
- **Retention:** [TODO: Aufbewahrungsdauer]
- **Leistungen:**
  - Backup-Storage
  - Disaster-Recovery
  - 24/7 Support

### Security-Service-Provider

#### [TODO: Security-Provider Name]
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **SOC-Hotline:** [TODO: SOC-Nummer]
- **Vertragsnummer:** [TODO: Vertragsnummer]
- **Leistungen:**
  - Security-Monitoring
  - Incident-Response
  - Threat-Intelligence
  - Penetration-Testing

## Notfall-Kontakte

### Kritische Situationen

#### Feuer / Medizinischer Notfall
- **Notruf:** 112
- **Gebäudesicherheit:** [TODO: Telefonnummer]
- **Erste-Hilfe:** [TODO: Ersthelfer-Kontakt]

#### Polizei
- **Notruf:** 110
- **Lokale Polizei:** [TODO: Telefonnummer]

#### Gebäudemanagement
- **Facility Management:** [TODO: Telefonnummer]
- **Verfügbarkeit:** 24/7
- **Verantwortung:** Gebäudesicherheit, Zugang

#### Rechtsabteilung
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** Mo-Fr 09:00-17:00, Notfall-Hotline
- **Verantwortung:** Rechtliche Beratung, Verträge

#### PR / Kommunikation
- **Ansprechpartner:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefonnummer]
- **Verfügbarkeit:** Mo-Fr 09:00-18:00, Notfall-Hotline
- **Verantwortung:** Externe Kommunikation, Medien

## Kommunikationskanäle

### Interne Kommunikation

#### E-Mail
- **Primär:** Offizielle Kommunikation
- **Verteiler:**
  - IT-Team: [TODO: it-team@example.com]
  - Management: [TODO: management@example.com]
  - All-Hands: [TODO: all@example.com]

#### Chat / Collaboration
- **Platform:** [TODO: Chat-Platform]
- **Channels:**
  - #it-operations: Täglicher Betrieb
  - #incidents: Incident-Kommunikation
  - #changes: Change-Kommunikation
  - #general: Allgemeine Kommunikation

#### Telefon-Konferenz
- **System:** [TODO: Conferencing-System]
- **Bridge-Nummer:** [TODO: Telefonnummer]
- **PIN:** [TODO: PIN]

#### Video-Konferenz
- **System:** [TODO: Video-System]
- **URL:** [TODO: Meeting-URL]

### Externe Kommunikation

#### Kunden-Kommunikation
- **E-Mail:** [TODO: support@example.com]
- **Telefon:** [TODO: Support-Nummer]
- **Portal:** [TODO: Portal-URL]

#### Status-Page
- **URL:** [TODO: status.example.com]
- **Zweck:** Öffentliche Status-Updates
- **Aktualisierung:** Bei Incidents und Wartungen

#### Social Media
- **Twitter:** [TODO: @company]
- **LinkedIn:** [TODO: Company-Page]
- **Zweck:** Öffentliche Ankündigungen

## Kontakt-Aktualisierung

### Aktualisierungsprozess

1. **Änderungen melden:**
   - E-Mail an {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
   - Neue Kontaktdaten angeben
   - Gültigkeitsdatum angeben

2. **Validierung:**
   - IT Operations Manager prüft Änderung
   - Genehmigung einholen (falls erforderlich)

3. **Aktualisierung:**
   - Dokument aktualisieren
   - CMDB aktualisieren
   - Betroffene Teams informieren

4. **Verifikation:**
   - Neue Kontaktdaten testen
   - Bestätigung einholen

### Review-Zyklus
- **Frequenz:** Quartalsweise
- **Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
- **Prozess:**
  - Alle Kontakte durchgehen
  - Aktualität prüfen
  - Änderungen dokumentieren
  - Teams informieren

## Prozesse und Verantwortlichkeiten

### RACI-Matrix

| Aktivität | CIO | Ops Manager | Ops Team | Service Desk |
|---|---|---|---|---|
| Kontakt-Verwaltung | C | A | R | C |
| Eskalation Level 1-2 | I | C | R | R |
| Eskalation Level 3-4 | A | R | C | I |
| Anbieter-Management | A | R | C | I |
| Notfall-Kommunikation | A | R | C | I |

> **Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance und Standards

### Relevante Standards
- **ITIL v4:** Service Desk Practice, Incident Management
- **ISO 20000:** Clause 8.2 - Service Desk
- **COBIT 2019:** DSS02 - Managed Service Requests and Incidents

### Audit-Anforderungen
- Aktuelle Kontaktlisten
- Eskalationspfad-Dokumentation
- Anbieter-Verträge
- Kommunikations-Protokolle

## Anhang

### Glossar

| Begriff | Definition |
|---|---|
| On-Call | Rufbereitschaft außerhalb regulärer Arbeitszeiten |
| Eskalation | Weiterleitung an höhere Support-Ebene |
| SLA | Service Level Agreement - Vereinbarung über Serviceleistungen |
| MSP | Managed Service Provider - Externer Dienstleister |

### Referenzen
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

## Schnellreferenz

### Wichtigste Kontakte

| Situation | Kontakt | Telefon |
|---|---|---|
| IT-Support | {{ meta-organisation-roles.role_Service_Desk_Lead }} | {{ meta-organisation-roles.role_Service_Desk_Lead_phone }} |
| Kritischer Incident | IT Operations Manager | {{ meta-organisation-roles.role_IT_Operations_Manager_phone }} |
| Security-Incident | {{ meta-organisation-roles.role_CISO }} | {{ meta-organisation-roles.role_CISO_phone }} |
| Management-Eskalation | {{ meta-organisation-roles.role_CIO }} | {{ meta-organisation-roles.role_CIO_phone }} |
| Notfall (Feuer/Medizin) | Notruf | 112 |
| Polizei | Notruf | 110 |

**Letzte Aktualisierung:** {{ meta-handbook.date }}  
**Nächste Review:** [TODO: Datum]  
**Kontakt:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}

