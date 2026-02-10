# Anhang: Datenflüsse und Schnittstellen (Template)

**Dokument-ID:** 0720  
**Dokumenttyp:** Anhang/Template  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents data flows and interfaces for risk analysis and protection needs assessment.
Reference: BSI Standard 200-2 (Structure Analysis), BSI IT-Grundschutz-Kompendium: CON.1 Kryptokonzept
-->

## 1. Zweck und Zielsetzung

Die Dokumentation der Datenflüsse und Schnittstellen von **{{ meta.organization.name }}** unterstützt:
- Schutzbedarfsfeststellung (Dokument 0060)
- Risikoanalyse (Dokument 0090)
- Kryptokonzept (Dokument 0340/0350)
- Datenschutz-Compliance (Dokument 0420/0430)

**Verantwortlich:** {{ meta.ciso.name }} (ISB), {{ meta.cio.name }} (IT-Leitung)

## 2. Datenfluss-Register

| Datenfluss-ID | Quelle | Ziel | Datenarten | Schutzbedarf (C/I/A) | Transportweg | Verschlüsselung | Speicherung | Provider/Drittland | Owner | Rechtsgrundlage | Notiz |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DF-001 | Webserver ({{ netbox.device.name }}) | Datenbank-Server | Kundendaten (personenbezogen) | Sehr hoch/Hoch/Hoch | {{ netbox.vlan.name }} (intern) | TLS 1.3 | Verschlüsselt (AES-256) | Intern | {{ meta.cio.name }} | DSGVO Art. 6(1)(b) | [TODO] |
| DF-002 | Backup-Server | Cloud-Storage (AWS S3) | Backup-Daten | Hoch/Hoch/Hoch | Internet (VPN) | TLS 1.3 + AES-256 | Verschlüsselt (AES-256) | AWS (EU-West-1) | {{ meta.cio.name }} | DSGVO Art. 28 | [TODO] |
| DF-003 | Mitarbeiter (Remote) | VPN-Gateway | Geschäftsdaten | Hoch/Hoch/Normal | Internet | IPsec/IKEv2 | N/A | Intern | {{ meta.cio.name }} | - | [TODO] |
| DF-004 | ERP-System | Payment-Gateway | Zahlungsdaten | Sehr hoch/Sehr hoch/Hoch | Internet (HTTPS) | TLS 1.3 | Nicht gespeichert | Payment Provider (EU) | {{ meta.cio.name }} | PCI-DSS | [TODO] |
| DF-005 | SIEM | Log-Archiv | Log-Daten | Normal/Hoch/Normal | {{ netbox.vlan.name }} (Management) | TLS 1.2 | Verschlüsselt | Intern | {{ meta.ciso.name }} | - | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 3. Schnittstellen-Register

| Schnittstellen-ID | System A | System B | Protokoll | Port | Authentisierung | Verschlüsselung | Datenrichtung | Frequenz | Owner | Notiz |
|---|---|---|---|---|---|---|---|---|---|---|
| IF-001 | Webserver | Datenbank | PostgreSQL | 5432 | Zertifikat | TLS 1.3 | Bidirektional | Permanent | {{ meta.cio.name }} | [TODO] |
| IF-002 | ERP | CRM | REST API | 443 | OAuth 2.0 | TLS 1.3 | Bidirektional | Echtzeit | {{ meta.cio.name }} | [TODO] |
| IF-003 | Monitoring | SIEM | Syslog | 514 | Zertifikat | TLS 1.2 | Unidirektional | Permanent | {{ meta.ciso.name }} | [TODO] |
| IF-004 | AD | LDAP-Clients | LDAPS | 636 | Kerberos | TLS 1.2 | Bidirektional | On-Demand | {{ meta.cio.name }} | [TODO] |
| IF-005 | Backup-Server | Cloud-Storage | S3 API | 443 | API-Key | TLS 1.3 | Unidirektional | Täglich | {{ meta.cio.name }} | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Externe Schnittstellen und Drittanbieter

| Drittanbieter | Service | Datenarten | Schutzbedarf | Standort/Drittland | Vertrag | Datenschutz-Vereinbarung | Owner | Notiz |
|---|---|---|---|---|---|---|---|---|
| AWS | Cloud-Hosting (EC2, S3) | Geschäftsdaten, Backup | Hoch/Hoch/Hoch | EU-West-1 | [TODO: Vertragsnummer] | Ja (Art. 28 DSGVO) | {{ meta.cio.name }} | [TODO] |
| Microsoft | Office 365 | E-Mail, Dokumente | Hoch/Hoch/Normal | EU | [TODO] | Ja | {{ meta.cio.name }} | [TODO] |
| Payment Provider | Zahlungsabwicklung | Zahlungsdaten | Sehr hoch/Sehr hoch/Hoch | EU | [TODO] | Ja | {{ meta.cio.name }} | PCI-DSS zertifiziert |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Referenz:** Dokument 0400/0410 (Lieferanten und Auslagerungsmanagement)

## 5. Datenfluss-Diagramme

**Ablageort:** `diagrams/dataflows.png` oder [TODO: Confluence/SharePoint]

**Empfohlene Diagramme:**
1. **High-Level Datenfluss:** Übersicht über alle Hauptdatenflüsse
2. **Detaillierte Datenflüsse:** Pro kritischem System/Service
3. **Externe Datenflüsse:** Alle Datenflüsse zu Drittanbietern
4. **Personenbezogene Daten:** DSGVO-relevante Datenflüsse

**Tools:** [TODO: z.B. Lucidchart, Draw.io, Visio]

## 6. Datenkategorien

### 6.1 Personenbezogene Daten (DSGVO)
- Kundendaten (Name, Adresse, E-Mail, etc.)
- Mitarbeiterdaten (HR-Daten)
- Besondere Kategorien (Art. 9 DSGVO): [TODO: falls zutreffend]

### 6.2 Geschäftsdaten
- Verträge
- Finanzdaten
- Geschäftsgeheimnisse
- Strategische Dokumente

### 6.3 Technische Daten
- Log-Daten
- Monitoring-Daten
- Konfigurationsdaten

### 6.4 Öffentliche Daten
- Marketing-Materialien
- Öffentliche Website-Inhalte

## 7. Verschlüsselungsanforderungen

| Datenart | Schutzbedarf | Transport-Verschlüsselung | Speicher-Verschlüsselung | Schlüsselverwaltung |
|---|---|---|---|---|
| Personenbezogene Daten | Sehr hoch | TLS 1.3 (min. TLS 1.2) | AES-256 | HSM/KMS |
| Geschäftsdaten | Hoch | TLS 1.3 (min. TLS 1.2) | AES-256 | KMS |
| Log-Daten | Normal | TLS 1.2 | Optional | KMS |
| Öffentliche Daten | Normal | TLS 1.2 | Nicht erforderlich | - |

**Referenz:** Dokument 0340/0350 (Kryptografie und Key Management)

## 8. Grenzüberschreitende Datenübermittlung

**Datenübermittlung in Drittländer:**

| Zielland | Datenarten | Rechtsgrundlage | Garantien | Genehmigung | Notiz |
|---|---|---|---|---|---|
| USA | [TODO] | Standardvertragsklauseln (SCC) | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Referenz:** Dokument 0420/0430 (Datenschutz)

## 9. Verantwortlichkeiten (RACI)

| Aktivität | IT-Leitung | ISB | Datenschutzbeauftragter | Fachbereich |
|---|---|---|---|---|
| Datenflüsse dokumentieren | A | C | C | R |
| Schutzbedarf festlegen | A | R | C | C |
| Verschlüsselung implementieren | R | C | I | I |
| Drittanbieter-Verträge prüfen | C | C | R | A |
| Jährlicher Review | A | R | C | C |

**Legende:**
- **R** = Responsible (Durchführungsverantwortung)
- **A** = Accountable (Gesamtverantwortung)
- **C** = Consulted (Konsultiert)
- **I** = Informed (Informiert)

## 10. Änderungsmanagement

**Änderungen an Datenflüssen:**
- Neue Datenflüsse müssen vor Inbetriebnahme dokumentiert werden
- Änderungen an bestehenden Datenflüssen erfordern Change-Ticket
- Sicherheitsrelevante Änderungen erfordern ISB-Freigabe

**Referenz:** Dokument 0380/0390 (Change Management)

## 11. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT-Leitung | {{ meta.cio.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| Datenschutzbeauftragter | [TODO] | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**Referenzen:**
- BSI Standard 200-2: IT-Grundschutz-Methodik (Strukturanalyse)
- BSI IT-Grundschutz-Kompendium: CON.1 Kryptokonzept
- Dokument 0050: Strukturanalyse
- Dokument 0060: Schutzbedarfsfeststellung
- Dokument 0090: Risikoanalyse
- Dokument 0340/0350: Kryptografie und Key Management
- Dokument 0420/0430: Datenschutz

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->