# Richtlinie: Datenklassifizierung, Labeling und Handling

**Dokument-ID:** 0290
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0280_Policy_Datenklassifizierung_und_Informationshandling.md` und definiert:
- Klassifizierungsstufen und Kriterien
- Labeling-Verfahren für Dokumente und E-Mails
- Handling-Anforderungen pro Klassifizierungsstufe

**Geltungsbereich:** Alle Informationen bei **AdminSend GmbH**

## 2. Klassifizierungsstufen

### 2.1 Öffentlich (Public)

**Definition:** Informationen für öffentliche Verbreitung bestimmt

**Beispiele:**
- Marketing-Materialien, Pressemitteilungen
- Öffentliche Website-Inhalte
- Produktdokumentationen

**Handling:**
- Keine Zugriffsbeschränkungen
- Keine Verschlüsselung erforderlich
- Freie Weitergabe erlaubt

### 2.2 Intern (Internal)

**Definition:** Informationen für interne Nutzung, nicht für Öffentlichkeit

**Beispiele:**
- Interne Prozessdokumentationen
- Organisationsstrukturen
- Allgemeine Geschäftskommunikation

**Handling:**
- Zugriff nur für Mitarbeiter und autorisierte Dritte
- Keine Verschlüsselung erforderlich (außer bei externer Übertragung)
- Weitergabe an Dritte nur mit NDA

### 2.3 Vertraulich (Confidential)

**Definition:** Sensible Geschäftsinformationen, Schaden bei Offenlegung

**Beispiele:**
- Verträge, Angebote
- Personaldaten
- Finanzberichte (intern)
- Kundendaten

**Handling:**
- Zugriff nur nach Need-to-Know-Prinzip
- Verschlüsselung bei Übertragung und Speicherung
- Weitergabe nur mit Genehmigung
- Sichere Vernichtung erforderlich

### 2.4 Streng Vertraulich (Highly Confidential)

**Definition:** Höchst sensible Informationen, erheblicher Schaden bei Offenlegung

**Beispiele:**
- Geschäftsgeheimnisse, M&A-Pläne
- Strategische Pläne
- Sicherheitskonzepte
- Kritische Infrastrukturdaten

**Handling:**
- Zugriff nur für autorisierte Personen (explizite Genehmigung)
- Verschlüsselung verpflichtend (at rest und in transit)
- Keine E-Mail-Versand ohne Verschlüsselung
- Physische Dokumente in Safe
- Sichere Vernichtung nach DIN 66399 P-5

## 3. Klassifizierungsprozess

### 3.1 Verantwortlichkeiten

**Daten-Owner:**
- Klassifizierung neuer Informationen
- Review und Anpassung bei Änderungen
- Genehmigung von Zugriff en

**Ersteller:**
- Anwendung der Klassifizierung bei Dokumenterstellung
- Labeling gemäß Vorgaben
- Einhaltung Handling-Anforderungen

**IT-Betrieb:**
- Technische Umsetzung (DLP, Verschlüsselung)
- Monitoring und Compliance-Checks

### 3.2 Klassifizierungskriterien

**Fragen zur Bestimmung:**
1. Welcher Schaden entsteht bei Offenlegung?
2. Gibt es gesetzliche/regulatorische Anforderungen?
3. Wer benötigt Zugriff (Öffentlichkeit, Mitarbeiter, spezifische Personen)?
4. Wie lange müssen Daten aufbewahrt werden?

**Entscheidungsbaum:**
- Öffentlich bestimmt? → Öffentlich
- Nur intern relevant? → Intern
- Geschäftsschaden bei Offenlegung? → Vertraulich
- Erheblicher Schaden oder gesetzliche Pflicht? → Streng Vertraulich

## 4. Labeling-Verfahren

### 4.1 Dokumente

**Microsoft Office:**
- Sensitivity Labels in Office 365
- Automatische Anwendung über DLP-Regeln
- Header/Footer mit Klassifizierung

**PDF:**
- Wasserzeichen mit Klassifizierung
- Metadaten-Tags

**Physische Dokumente:**
- Stempel oder Aufdruck auf jeder Seite
- Farbcodierung (z.B. Rot für Streng Vertraulich)

### 4.2 E-Mails

**Betreffzeile:**
- Präfix: [VERTRAULICH], [STRENG VERTRAULICH]
- Automatisch durch E-Mail-Client

**E-Mail-Body:**
- Disclaimer im Footer
- Verschlüsselung bei Vertraulich/Streng Vertraulich

**Outlook-Integration:**
- Sensitivity Labels
- Automatische Verschlüsselung bei Klassifizierung

### 4.3 Digitale Assets

**Dateisysteme:**
- Metadaten-Tags
- Separate Ordnerstrukturen pro Klassifizierung
- Zugriffskontrolle über ACLs

**Datenbanken:**
- Spalten-Level-Klassifizierung
- Row-Level-Security
- Audit-Logging für Zugriffe

## 5. Handling-Anforderungen

### 5.1 Speicherung

| Klassifizierung | Speicherort | Verschlüsselung | Zugriffskontrolle |
|-----------------|-------------|-----------------|-------------------|
| Öffentlich | Beliebig | Optional | Keine |
| Intern | Genehmigte Systeme | Bei externer Speicherung | Mitarbeiter |
| Vertraulich | Genehmigte Systeme | Verpflichtend | Need-to-Know |
| Streng Vertraulich | Dedizierte Systeme | Verpflichtend (AES-256) | Explizite Genehmigung |

### 5.2 Übertragung

| Klassifizierung | E-Mail | Dateitransfer | Physisch |
|-----------------|--------|---------------|----------|
| Öffentlich | Unverschlüsselt OK | Beliebig | Keine Anforderungen |
| Intern | TLS empfohlen | SFTP/HTTPS | Versiegelte Umschläge |
| Vertraulich | S/MIME verpflichtend | SFTP/HTTPS verschlüsselt | Einschreiben, versiegelt |
| Streng Vertraulich | S/MIME + Genehmigung | Dedizierte Kanäle | Kurier, persönliche Übergabe |

### 5.3 Vernichtung

| Klassifizierung | Digital | Papier | Datenträger |
|-----------------|---------|--------|-------------|
| Öffentlich | Normale Löschung | Papierkorb | Normale Löschung |
| Intern | Sichere Löschung | Shredder P-3 | Sichere Löschung |
| Vertraulich | Kryptographische Löschung | Shredder P-4 | Degaussing + Zerstörung |
| Streng Vertraulich | Kryptographische Löschung | Shredder P-5 | Physische Zerstörung |

## 6. Data Loss Prevention (DLP)

### 6.1 DLP-Regeln

**Automatische Erkennung:**
- Kreditkartennummern, Sozialversicherungsnummern
- Dokumente mit "Vertraulich"-Label
- Personenbezogene Daten (DSGVO)

**Aktionen:**
- **Warnung:** Bei Versand Intern-klassifizierter Daten extern
- **Blockierung:** Bei Versand Vertraulich/Streng Vertraulich ohne Verschlüsselung
- **Quarantäne:** Bei Verdacht auf Datenleck

### 6.2 Monitoring

**Überwachte Kanäle:**
- E-Mail (ausgehend)
- Cloud-Uploads (OneDrive, SharePoint)
- USB-Geräte
- Drucker

**Alerts:**
- Automatische Benachrichtigung an Security-Team
- Incident-Erstellung bei kritischen Verstößen

## 7. Schulung und Awareness

**Pflichtschulungen:**
- Onboarding: Datenklassifizierung-Grundlagen
- Jährlich: Refresher und Updates

**Awareness-Materialien:**
- Poster mit Klassifizierungsstufen
- Quick-Reference-Karten
- Intranet-Artikel

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Klassifizierte Dokumente | > 80% |
| DLP-Incidents | < 10 pro Monat |
| Schulungsteilnahme | 100% |

### 8.2 Audit-Nachweise

- Klassifizierungs-Register
- DLP-Logs und Incidents
- Schulungsnachweise
- Zugriffsprotokolle

## 9. Referenzen

### Interne Dokumente
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md`
- `0320_Policy_Logging_und_Monitoring.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.12** - Classification of information
- **ISO/IEC 27001:2022 Annex A.5.13** - Labelling of information
- **DIN 66399** - Vernichtung von Datenträgern

**Genehmigt durch:** [TODO], CISO  
**Nächster Review:** [TODO]

