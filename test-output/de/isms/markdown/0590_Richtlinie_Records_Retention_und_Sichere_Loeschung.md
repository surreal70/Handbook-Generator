# Richtlinie: Records Retention und Sichere Löschung

**Dokument-ID:** 0590  
**Dokumenttyp:** Richtlinie (detailliert)  
**Zugehörige Policy:** 0580_Policy_Aufbewahrung_und_Loeschung.md  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.33  
**Owner:** {{ meta.compliance.manager }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}

---

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0580_Policy_Aufbewahrung_und_Loeschung.md` und definiert:
- Aufbewahrungsfristen für verschiedene Datentypen
- Sichere Löschverfahren
- Records Management Prozesse

**Geltungsbereich:** Alle Daten und Dokumente bei **AdminSend GmbH**

## 2. Aufbewahrungsfristen

### 2.1 Geschäftsdokumente

| Dokumenttyp | Aufbewahrungsfrist | Rechtsgrundlage |
|-------------|-------------------|-----------------|
| Jahresabschlüsse | 10 Jahre | HGB §257 |
| Buchungsbelege | 10 Jahre | HGB §257 |
| Rechnungen | 10 Jahre | HGB §257, AO §147 |
| Verträge | 10 Jahre nach Ende | HGB §257 |
| Geschäftskorrespondenz | 6 Jahre | HGB §257 |
| Angebote | 6 Jahre | HGB §257 |

### 2.2 Personaldokumente

| Dokumenttyp | Aufbewahrungsfrist | Rechtsgrundlage |
|-------------|-------------------|-----------------|
| Personalakten | 10 Jahre nach Austritt | DSGVO Art. 17 |
| Lohnabrechnungen | 10 Jahre | AO §147 |
| Arbeitszeugnisse | 3 Jahre | BGB §195 |
| Bewerbungsunterlagen (abgelehnt) | 6 Monate | AGG §15 |
| Zeiterfassungsdaten | 2 Jahre | ArbZG §16 |

### 2.3 IT-Daten

| Datentyp | Aufbewahrungsfrist | Begründung |
|----------|-------------------|------------|
| E-Mails (geschäftlich) | {{ meta.retention.email_years }} Jahre | Geschäftskorrespondenz |
| Logs (Security) | {{ meta.retention.log_years }} Jahre | Forensik, Compliance |
| Logs (System) | 1 Jahr | Troubleshooting |
| Backups | Gemäß Backup-Policy | Wiederherstellung |
| Audit-Trails | {{ meta.retention.audit_years }} Jahre | Compliance |

### 2.4 Kundendaten

| Datentyp | Aufbewahrungsfrist | Rechtsgrundlage |
|----------|-------------------|-----------------|
| Kundenstammdaten | Bis Vertragsende + 3 Jahre | Verjährung |
| Bestelldaten | 10 Jahre | HGB §257 |
| Zahlungsdaten | 10 Jahre | AO §147 |
| Kommunikation | 6 Jahre | HGB §257 |

## 3. Retention-Management

### 3.1 Retention-Policies

**Automatisierung:**
- Retention-Labels in Microsoft 365
- Lifecycle-Policies in Cloud-Storage
- Automatische Löschung nach Fristablauf

**Manuelle Prozesse:**
- Für physische Dokumente
- Für Legacy-Systeme

### 3.2 Legal Hold

**Bei rechtlichen Verfahren:**
- Aussetzung der Löschung
- Preservation Order
- Dokumentation des Legal Hold
- Aufhebung nach Verfahrensende

### 3.3 Retention-Register

**Dokumentation:**
- Datentyp, Aufbewahrungsfrist, Rechtsgrundlage
- Speicherort, Verantwortlicher
- Löschdatum
- Regelmäßige Reviews (jährlich)

## 4. Sichere Löschung

### 4.1 Digitale Daten

**Methoden nach DIN 66399:**

| Datenträger | Methode | Standard |
|-------------|---------|----------|
| HDD | Software-Löschung (3-Pass) oder Degaussing | DIN 66399 H-3/H-4 |
| SSD | Secure Erase (ATA) oder Kryptographische Löschung | DIN 66399 H-3 |
| Cloud-Daten | Logische Löschung + Bestätigung | Provider-abhängig |
| Backups | Kryptographische Löschung (Schlüssel vernichten) | DIN 66399 H-4 |

**Tools:**
- DBAN, Blancco (Software-Löschung)
- Degausser (Magnetische Löschung)
- Shredder (Physische Zerstörung)

### 4.2 Physische Dokumente

**Methoden nach DIN 66399:**

| Schutzstufe | Partikelgröße | Anwendung |
|-------------|---------------|-----------|
| P-3 | ≤ 320 mm² | Interne Dokumente |
| P-4 | ≤ 160 mm² | Vertrauliche Dokumente |
| P-5 | ≤ 30 mm² | Streng vertrauliche Dokumente |

**Prozess:**
- Shredder in Büros (P-3)
- Zertifizierte Entsorgungspartner (P-4, P-5)
- Entsorgungsnachweis

### 4.3 Löschprotokoll

**Dokumentation:**
- Datum der Löschung
- Gelöschte Daten/Dokumente
- Löschmethode
- Durchführende Person
- Bestätigung der Löschung

**Retention:** {{ meta.retention.deletion_log_years }} Jahre

## 5. E-Mail-Archivierung

### 5.1 Archivierungspflicht

**Geschäftliche E-Mails:**
- Automatische Archivierung
- Unveränderbarkeit (WORM)
- Aufbewahrung: {{ meta.retention.email_years }} Jahre

**Private E-Mails:**
- Keine Archivierung
- Kennzeichnung durch Nutzer (Betreff: [PRIVAT])

### 5.2 Archivierungssystem

**System:** {{ meta.email.archive_system }}

**Funktionen:**
- Automatische Archivierung
- Volltextsuche
- eDiscovery
- Legal Hold

### 5.3 Zugriff auf Archiv

**Berechtigungen:**
- Nutzer: Eigene E-Mails
- Vorgesetzte: Bei berechtigtem Interesse (mit Genehmigung)
- Legal/Compliance: Für Audits und Ermittlungen
- IT-Admins: Nur für technische Administration

## 6. Datenminimierung

### 6.1 Privacy by Design

**Prinzipien:**
- Nur notwendige Daten erheben
- Kürzeste Aufbewahrungsfrist wählen
- Automatische Löschung implementieren

### 6.2 Regelmäßige Reviews

**Quartalsweise:**
- Ungenutzte Daten identifizieren
- Löschung prüfen
- Retention-Policies anpassen

## 7. Cloud-Daten-Löschung

### 7.1 SaaS-Anwendungen

**Prozess:**
1. Logische Löschung in Anwendung
2. Warten auf Retention-Period (Provider-abhängig)
3. Bestätigung der endgültigen Löschung anfordern
4. Dokumentation

### 7.2 IaaS/PaaS

**Prozess:**
1. Daten löschen
2. Volumes/Disks löschen
3. Snapshots löschen
4. Kryptographische Schlüssel vernichten
5. Bestätigung der Löschung

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Automatische Löschung (nach Frist) | 100% |
| Löschprotokoll-Vollständigkeit | 100% |
| Retention-Policy-Compliance | > 95% |
| Entsorgungsnachweise | 100% |

### 8.2 Audit-Nachweise

- Retention-Register
- Löschprotokolle
- Entsorgungsnachweise
- E-Mail-Archivierungs-Berichte

## 9. Referenzen

### Interne Dokumente
- `0580_Policy_Aufbewahrung_und_Loeschung.md`
- `0570_Richtlinie_Datenschutz_Anforderungen_und_Datenverarbeitung.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.33** - Protection of records
- **DIN 66399** - Vernichtung von Datenträgern
- **HGB §257** - Aufbewahrung von Unterlagen
- **AO §147** - Ordnungsvorschriften für die Aufbewahrung von Unterlagen

---

**Genehmigt durch:** Thomas Weber, CISO  
**Nächster Review:** {{ meta.document.next_review }}
