# Anhang C: Datenfluss und Schnittstellen

**Dokument-ID:** [FRAMEWORK]-0730
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

## Zweck

Dieses Dokument dokumentiert alle Datenflüsse und Schnittstellen innerhalb der Organisation sowie zu externen Partnern und Dienstleistern. Es erfüllt die Anforderungen von:

- ISO/IEC 27001:2022 Annex A 5.14 (Information Transfer)
- ISO/IEC 27001:2022 Annex A 5.19-5.23 (Supplier Relationships)
- ISO/IEC 27001:2022 Annex A 8.20-8.22 (Network Security)

Die Dokumentation dient als Grundlage für:

- Risikobewertung von Datenübertragungen
- Sicherheitsanforderungen für Schnittstellen
- Datenschutz-Folgenabschätzungen (DPIA)
- Incident Response und Forensik

## Geltungsbereich

**Organisation:** AdminSend GmbH  
**ISMS Scope:** {{ meta-handbook.isms_scope }}  
**Verantwortlich:** [TODO], Data Protection Officer

## Datenfluss-Kategorien

### Interne Datenflüsse

Datenübertragungen innerhalb der Organisation zwischen verschiedenen Systemen und Standorten.

### Externe Datenflüsse

Datenübertragungen zwischen der Organisation und externen Partnern, Kunden, Lieferanten oder Cloud-Diensten.

### Grenzüberschreitende Datenflüsse

Datenübertragungen über Ländergrenzen hinweg, die besondere Datenschutzanforderungen (DSGVO Art. 44-50) erfüllen müssen.

## Datenklassifizierung

Alle Datenflüsse werden nach folgenden Klassifizierungen bewertet:

| Klassifizierung | Beschreibung | Beispiele | Schutzmaßnahmen |
|-----------------|--------------|-----------|-----------------|
| **Öffentlich** | Für die Öffentlichkeit bestimmt | Marketing-Materialien, öffentliche Website | Keine besonderen Maßnahmen |
| **Intern** | Nur für interne Nutzung | Interne Dokumente, Betriebshandbücher | Zugriffskontrolle |
| **Vertraulich** | Sensible Geschäftsinformationen | Verträge, Finanzberichte | Verschlüsselung, strenge Zugriffskontrolle |
| **Streng Vertraulich** | Höchst sensible Daten | Personenbezogene Daten, Geschäftsgeheimnisse | Ende-zu-Ende-Verschlüsselung, MFA, Audit Logging |

## Interne Datenflüsse

### Anwendungs-zu-Anwendungs Kommunikation

| Datenfluss-ID | Quelle | Ziel | Protokoll | Port | Datentyp | Klassifizierung | Verschlüsselung | Frequenz |
|---------------|--------|------|-----------|------|----------|-----------------|-----------------|----------|
| DF-INT-001 | [TODO: ERP System] | [TODO: CRM System] | HTTPS | 443 | Kundendaten | Vertraulich | TLS 1.3 | Echtzeit |
| DF-INT-002 | [TODO: App Server] | [TODO: Database] | PostgreSQL | 5432 | Transaktionsdaten | Streng Vertraulich | TLS 1.2+ | Kontinuierlich |
| DF-INT-003 | [TODO: Backup System] | [TODO: Storage] | iSCSI | 3260 | Backup-Daten | Vertraulich | IPSec | Täglich |
| [TODO] | [TODO: Quelle] | [TODO: Ziel] | [TODO: Protokoll] | [TODO: Port] | [TODO: Datentyp] | [TODO: Klassifizierung] | [TODO: Verschlüsselung] | [TODO: Frequenz] |

**Sicherheitsmaßnahmen:**
- Netzwerksegmentierung zwischen Anwendungs- und Datenbankschicht
- Firewall-Regeln mit Least-Privilege-Prinzip
- Verschlüsselte Verbindungen (TLS 1.2+)
- Authentifizierung über Zertifikate oder Service Accounts

### Site-to-Site Verbindungen

| Datenfluss-ID | Quelle-Standort | Ziel-Standort | Verbindungstyp | Bandbreite | Datentyp | Verschlüsselung | Redundanz |
|---------------|-----------------|---------------|----------------|------------|----------|-----------------|-----------|
| DF-S2S-001 | [[ netbox.site.name ]] | [TODO: Zweigstelle] | MPLS | [TODO: Mbps] | Alle Geschäftsdaten | IPSec | Ja |
| DF-S2S-002 | [[ netbox.site.name ]] | [TODO: DR-Standort] | Dedicated Line | [TODO: Mbps] | Replikationsdaten | AES-256 | Ja |
| [TODO] | [TODO: Quelle] | [TODO: Ziel] | [TODO: Typ] | [TODO: Bandbreite] | [TODO: Datentyp] | [TODO: Verschlüsselung] | [TODO: Redundanz] |

**Sicherheitsmaßnahmen:**
- VPN-Tunnel mit IPSec oder WireGuard
- Redundante Verbindungen für kritische Standorte
- Monitoring und Alerting bei Verbindungsausfällen
- Regelmäßige Sicherheitsaudits

### Datenbank-Replikation

| Datenfluss-ID | Primäre DB | Sekundäre DB | Replikationstyp | Datentyp | Klassifizierung | Verschlüsselung | RPO |
|---------------|------------|--------------|-----------------|----------|-----------------|-----------------|-----|
| DF-REP-001 | [TODO: Prod DB] | [TODO: DR DB] | Asynchron | Alle Produktionsdaten | Streng Vertraulich | TLS 1.3 | < 1h |
| DF-REP-002 | [TODO: Prod DB] | [TODO: Reporting DB] | Synchron | Reporting-Daten | Vertraulich | TLS 1.2 | < 5min |
| [TODO] | [TODO: Primär] | [TODO: Sekundär] | [TODO: Typ] | [TODO: Datentyp] | [TODO: Klassifizierung] | [TODO: Verschlüsselung] | [TODO: RPO] |

## Externe Datenflüsse

### Cloud Services

| Datenfluss-ID | Internes System | Cloud Service | Provider | Datentyp | Klassifizierung | Verschlüsselung | Datenstandort |
|---------------|-----------------|---------------|----------|----------|-----------------|-----------------|---------------|
| DF-EXT-001 | [TODO: File Server] | Microsoft 365 | Microsoft | Dokumente, E-Mails | Vertraulich | TLS 1.3, At-Rest AES-256 | EU |
| DF-EXT-002 | [TODO: App Server] | AWS S3 | Amazon | Backup-Daten | Vertraulich | TLS 1.3, SSE-S3 | EU (Frankfurt) |
| DF-EXT-003 | [TODO: Monitoring] | Azure Monitor | Microsoft | Logs, Metriken | Intern | TLS 1.3 | EU |
| [TODO] | [TODO: System] | [TODO: Service] | [TODO: Provider] | [TODO: Datentyp] | [TODO: Klassifizierung] | [TODO: Verschlüsselung] | [TODO: Standort] |

**Sicherheitsmaßnahmen:**
- Cloud Security Posture Management (CSPM)
- Identity and Access Management (IAM) mit Least Privilege
- Verschlüsselung in Transit und At-Rest
- Regelmäßige Security Assessments der Cloud Provider
- Data Residency Compliance (DSGVO)

### Partner-Schnittstellen

| Datenfluss-ID | Internes System | Partner | Schnittstellentyp | Datentyp | Klassifizierung | Verschlüsselung | Vertrag |
|---------------|-----------------|---------|-------------------|----------|-----------------|-----------------|---------|
| DF-PART-001 | [TODO: ERP] | [TODO: Lieferant A] | REST API | Bestelldaten | Vertraulich | TLS 1.3, API Key | [TODO: Vertragsnr.] |
| DF-PART-002 | [TODO: CRM] | [TODO: Partner B] | SFTP | Kundendaten | Streng Vertraulich | SSH, PGP | [TODO: Vertragsnr.] |
| [TODO] | [TODO: System] | [TODO: Partner] | [TODO: Typ] | [TODO: Datentyp] | [TODO: Klassifizierung] | [TODO: Verschlüsselung] | [TODO: Vertrag] |

**Sicherheitsmaßnahmen:**
- Supplier Security Assessments vor Vertragsabschluss
- Data Processing Agreements (DPA) gemäß DSGVO Art. 28
- Mutual TLS (mTLS) für API-Kommunikation
- API Rate Limiting und Monitoring
- Regelmäßige Sicherheitsaudits

### Kunden-Schnittstellen

| Datenfluss-ID | Internes System | Schnittstelle | Protokoll | Datentyp | Klassifizierung | Verschlüsselung | Authentifizierung |
|---------------|-----------------|---------------|-----------|----------|-----------------|-----------------|-------------------|
| DF-CUST-001 | [TODO: Web App] | Kundenportal | HTTPS | Kundendaten | Streng Vertraulich | TLS 1.3 | OAuth 2.0 + MFA |
| DF-CUST-002 | [TODO: API Gateway] | Mobile App | HTTPS | Transaktionsdaten | Vertraulich | TLS 1.3 | JWT + Biometrie |
| [TODO] | [TODO: System] | [TODO: Schnittstelle] | [TODO: Protokoll] | [TODO: Datentyp] | [TODO: Klassifizierung] | [TODO: Verschlüsselung] | [TODO: Auth] |

**Sicherheitsmaßnahmen:**
- Web Application Firewall (WAF)
- DDoS Protection
- Rate Limiting und Throttling
- Input Validation und Output Encoding
- Security Headers (HSTS, CSP, etc.)

## Grenzüberschreitende Datenflüsse

### EU-Drittland-Transfers

| Datenfluss-ID | Quelle (EU) | Ziel (Drittland) | Land | Datentyp | Rechtsgrundlage | Schutzmaßnahmen |
|---------------|-------------|------------------|------|----------|-----------------|-----------------|
| DF-CROSS-001 | [[ netbox.site.name ]] | [TODO: US-Rechenzentrum] | USA | Cloud-Daten | Standard Contractual Clauses (SCC) | Verschlüsselung, Access Controls |
| [TODO] | [TODO: Quelle] | [TODO: Ziel] | [TODO: Land] | [TODO: Datentyp] | [TODO: Rechtsgrundlage] | [TODO: Maßnahmen] |

**DSGVO-Compliance:**
- Art. 44-50 DSGVO: Datenübermittlung in Drittländer
- Standard Contractual Clauses (SCC) gemäß Art. 46 Abs. 2 lit. c DSGVO
- Transfer Impact Assessment (TIA) durchgeführt
- Zusätzliche Schutzmaßnahmen implementiert

## Schnittstellen-Dokumentation

### API-Schnittstellen

| API-ID | Name | Typ | Version | Authentifizierung | Autorisierung | Rate Limit | Dokumentation |
|--------|------|-----|---------|-------------------|---------------|------------|---------------|
| API-001 | [TODO: Customer API] | REST | v2.0 | OAuth 2.0 | RBAC | 1000 req/min | [TODO: URL] |
| API-002 | [TODO: Partner API] | REST | v1.5 | API Key + mTLS | API Key Scopes | 500 req/min | [TODO: URL] |
| API-003 | [TODO: Internal API] | GraphQL | v1.0 | JWT | ABAC | Unbegrenzt | [TODO: URL] |
| [TODO] | [TODO: Name] | [TODO: Typ] | [TODO: Version] | [TODO: Auth] | [TODO: Authz] | [TODO: Limit] | [TODO: Docs] |

**Sicherheitsanforderungen:**
- API Gateway mit Authentifizierung und Autorisierung
- Input Validation und Schema Validation
- Output Filtering (keine sensiblen Daten in Fehlermeldungen)
- Logging und Monitoring aller API-Zugriffe
- Versionierung und Deprecation Policy

### Datei-Transfer-Schnittstellen

| Schnittstellen-ID | Typ | Protokoll | Quelle | Ziel | Datentyp | Verschlüsselung | Authentifizierung |
|-------------------|-----|-----------|--------|------|----------|-----------------|-------------------|
| FT-001 | SFTP | SSH | [TODO: System] | [TODO: Partner] | Dateien | SSH, PGP | SSH Key |
| FT-002 | FTPS | FTP over TLS | [TODO: System] | [TODO: System] | Backup-Dateien | TLS 1.3 | Zertifikat |
| FT-003 | MFT | Managed File Transfer | [TODO: System] | [TODO: Partner] | Geschäftsdaten | AES-256 | OAuth 2.0 |
| [TODO] | [TODO: Typ] | [TODO: Protokoll] | [TODO: Quelle] | [TODO: Ziel] | [TODO: Datentyp] | [TODO: Verschlüsselung] | [TODO: Auth] |

### Messaging-Schnittstellen

| Schnittstellen-ID | Typ | Protokoll | Quelle | Ziel | Nachrichtentyp | Verschlüsselung | Persistenz |
|-------------------|-----|-----------|--------|------|----------------|-----------------|------------|
| MSG-001 | Message Queue | AMQP | [TODO: Producer] | [TODO: Consumer] | Events | TLS 1.3 | 7 Tage |
| MSG-002 | Event Stream | Kafka | [TODO: Producer] | [TODO: Consumer] | Logs | TLS 1.3 | 30 Tage |
| [TODO] | [TODO: Typ] | [TODO: Protokoll] | [TODO: Quelle] | [TODO: Ziel] | [TODO: Nachrichtentyp] | [TODO: Verschlüsselung] | [TODO: Persistenz] |

### E-Mail-Kommunikation

| Kommunikationstyp | Absender | Empfänger | Datentyp | Klassifizierung | Verschlüsselung | Archivierung |
|-------------------|----------|-----------|----------|-----------------|-----------------|--------------|
| Geschäfts-E-Mail | [TODO] | Extern | Geschäftskorrespondenz | Vertraulich | TLS (Opportunistic) | 7 Jahre |
| Vertrauliche E-Mail | [TODO] | Extern | Vertragsdokumente | Streng Vertraulich | S/MIME oder PGP | 10 Jahre |
| Interne E-Mail | [TODO] | [TODO] | Interne Kommunikation | Intern | TLS (Enforced) | 3 Jahre |

**Sicherheitsmaßnahmen:**
- SPF, DKIM, DMARC für E-Mail-Authentifizierung
- E-Mail Gateway mit Anti-Spam und Anti-Malware
- Data Loss Prevention (DLP) für ausgehende E-Mails
- E-Mail-Verschlüsselung für vertrauliche Inhalte
- E-Mail-Archivierung gemäß gesetzlichen Anforderungen

## Netzwerk-Architektur

### Netzwerk-Zonen

| Zone | Beschreibung | Sicherheitsstufe | Zugriffskontrolle | Systeme |
|------|--------------|------------------|-------------------|---------|
| **DMZ** | Demilitarisierte Zone für öffentlich zugängliche Dienste | Hoch | Firewall, IDS/IPS | Web Server, Mail Gateway |
| **Internal** | Internes Netzwerk für Geschäftsanwendungen | Mittel | Firewall, NAC | App Server, File Server |
| **Management** | Management-Netzwerk für Administration | Sehr Hoch | Firewall, MFA, Jump Host | Management Interfaces |
| **Production** | Produktionsnetzwerk für kritische Systeme | Sehr Hoch | Firewall, Segmentierung | Database Server, Core Systems |
| **Development** | Entwicklungs- und Testnetzwerk | Niedrig | Firewall | Dev/Test Systems |

### Firewall-Regeln (Beispiel)

| Regel-ID | Quelle-Zone | Ziel-Zone | Protokoll | Port | Aktion | Logging | Beschreibung |
|----------|-------------|-----------|-----------|------|--------|---------|--------------|
| FW-001 | Internet | DMZ | HTTPS | 443 | Allow | Ja | Web-Traffic zu Web Servern |
| FW-002 | DMZ | Internal | HTTPS | 443 | Allow | Ja | Web Server zu App Server |
| FW-003 | Internal | Production | PostgreSQL | 5432 | Allow | Ja | App Server zu Database |
| FW-004 | Management | All | SSH | 22 | Allow | Ja | Admin-Zugriff |
| FW-999 | Any | Any | Any | Any | Deny | Ja | Default Deny |

**Hinweis:** Vollständige Firewall-Regeln in separater Dokumentation.

## Datenfluss-Diagramme

### High-Level Architektur

```
[Internet]
    |
    | HTTPS (443)
    v
[Firewall/WAF]
    |
    | HTTPS (443)
    v
[DMZ - Web Server]
    |
    | HTTPS (443)
    v
[Internal - App Server]
    |
    | PostgreSQL (5432)
    v
[Production - Database]
```

**Hinweis:** Detaillierte Netzwerkdiagramme in separaten Dateien (z.B. Visio, Draw.io).

### Datenfluss für kritische Geschäftsprozesse

#### Beispiel: Kundenbestellung

```
[Kunde] 
  -> HTTPS -> [Web Portal (DMZ)]
  -> HTTPS -> [Order Service (Internal)]
  -> PostgreSQL -> [Order DB (Production)]
  -> HTTPS -> [Payment Gateway (External)]
  -> HTTPS -> [ERP System (Internal)]
  -> HTTPS -> [Warehouse System (Internal)]
```

**Sicherheitsmaßnahmen:**
- Ende-zu-Ende-Verschlüsselung
- Authentifizierung auf jeder Ebene
- Input Validation
- Audit Logging aller Transaktionen

## Risikobewertung Datenflüsse

### Risikomatrix

| Datenfluss-ID | Bedrohung | Wahrscheinlichkeit | Auswirkung | Risiko | Maßnahmen | Restrisiko |
|---------------|-----------|-------------------|------------|--------|-----------|------------|
| DF-EXT-001 | Datenverlust bei Cloud-Transfer | Niedrig | Hoch | Mittel | Verschlüsselung, DLP | Niedrig |
| DF-PART-001 | Unbefugter Zugriff durch Partner | Mittel | Hoch | Hoch | mTLS, API Gateway, Monitoring | Mittel |
| DF-CROSS-001 | Drittland-Zugriff auf EU-Daten | Mittel | Sehr Hoch | Hoch | SCC, Verschlüsselung, Access Controls | Mittel |
| [TODO] | [TODO: Bedrohung] | [TODO: W'keit] | [TODO: Auswirkung] | [TODO: Risiko] | [TODO: Maßnahmen] | [TODO: Restrisiko] |

## Monitoring und Logging

### Datenfluss-Monitoring

| Monitoring-Typ | Tool | Metriken | Alerting | Retention |
|----------------|------|----------|----------|-----------|
| Network Traffic | [TODO: NetFlow/sFlow] | Bandbreite, Verbindungen, Anomalien | Ja | 90 Tage |
| API Traffic | [TODO: API Gateway] | Request Rate, Latency, Errors | Ja | 90 Tage |
| Firewall Logs | [TODO: SIEM] | Blocked Connections, Rule Hits | Ja | 1 Jahr |
| Application Logs | [TODO: Log Management] | Transactions, Errors, Security Events | Ja | 1 Jahr |

### Security Events

Folgende Security Events werden für Datenflüsse überwacht:

- Ungewöhnliche Datenübertragungsvolumen
- Verbindungen zu unbekannten Zielen
- Fehlgeschlagene Authentifizierungsversuche
- Protokollverletzungen
- Verschlüsselungsfehler
- DLP-Verstöße

## Compliance und Datenschutz

### DSGVO-Anforderungen

| Anforderung | Artikel | Umsetzung | Nachweis |
|-------------|---------|-----------|----------|
| Rechtmäßigkeit der Verarbeitung | Art. 6 | Rechtsgrundlage dokumentiert | Verarbeitungsverzeichnis |
| Datenminimierung | Art. 5 Abs. 1 lit. c | Nur notwendige Daten übertragen | Datenfluss-Dokumentation |
| Integrität und Vertraulichkeit | Art. 5 Abs. 1 lit. f | Verschlüsselung, Zugriffskontrolle | Sicherheitsmaßnahmen |
| Drittland-Transfer | Art. 44-50 | SCC, TIA | Transfer-Dokumentation |

### Verarbeitungsverzeichnis-Referenz

Alle Datenflüsse sind im Verarbeitungsverzeichnis gemäß Art. 30 DSGVO dokumentiert.

**Referenz:** [TODO: Link zum Verarbeitungsverzeichnis]

## Änderungsmanagement

### Change Control

Alle Änderungen an Datenflüssen und Schnittstellen unterliegen dem Change Management Prozess:

1. **Change Request:** Antrag mit Begründung und Risikobewertung
2. **Security Review:** Bewertung durch Security Team
3. **Approval:** Genehmigung durch Change Advisory Board
4. **Implementation:** Umsetzung mit Dokumentation
5. **Verification:** Test und Validierung
6. **Documentation Update:** Aktualisierung dieses Dokuments

**Referenz:** 0360_Policy_Change_und_Release_Management.md

## Referenzen

- Policy: 0660_Policy_Informationsuebertragung_und_Kommunikation.md
- Richtlinie: 0670_Richtlinie_Email_Sharing_und_Zusammenarbeitstools.md
- Policy: 0460_Policy_Lieferanten_und_Cloud_Sicherheit.md
- Richtlinie: 0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md
- Policy: 0600_Policy_Netzwerksicherheit.md
- Richtlinie: 0610_Richtlinie_Segmentierung_Firewalling_und_Network_Access_Control.md
- Anhang: 0720_Anhang_Asset_und_Systeminventar_Template.md

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** {{ meta-handbook.management_name }}  
**Nächste Überprüfung:** Halbjährlich



