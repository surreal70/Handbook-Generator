# Dokumentenlenkung / Dokumentierte Information

**Dokument-ID:** 0050
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

<!-- 
TEMPLATE AUTHOR NOTE:
This document defines how ISMS documentation is controlled, including creation,
review, approval, distribution, storage, and archival. Proper document control
ensures that the right people have access to the right information at the right time.

ISO 27001:2022 Reference: Clause 7.5 - Documented information
-->

## 1. Zweck und Geltungsbereich

Dieses Dokument definiert die Anforderungen an die Lenkung dokumentierter Informationen im Rahmen des ISMS der **{{ meta-organisation.name }}**. Es stellt sicher, dass:
- Dokumente verfügbar und geeignet für die Verwendung sind
- Dokumente angemessen geschützt werden
- Dokumente kontrolliert erstellt, geprüft, genehmigt und aktualisiert werden

## 2. Ablage und Zugriff

### 2.1 Offizieller Ablageort

**Primärer Ablageort:**
- **System:** [TODO: SharePoint, Confluence, DMS]
- **Pfad:** [TODO: /ISMS/Dokumentation/]
- **URL:** [TODO: https://docs.organization.com/isms/]

**Backup und Archivierung:**
- **Backup-System:** [[ netbox.backup.system ]]
- **Backup-Frequenz:** Täglich
- **Archivierungsdauer:** 10 Jahre nach Außerbetriebnahme

### 2.2 Zugriffskontrolle

**Zugriffsberechtigungen:**

| Dokumenttyp | CISO | ISMS Manager | IT-Betrieb | Fachabteilungen | Alle Mitarbeiter |
|-------------|------|--------------|------------|-----------------|------------------|
| ISMS-Leitlinie | R/W | R/W | R | R | R |
| Policies (Abstract) | R/W | R/W | R | R | R |
| Richtlinien (Detailed) | R/W | R/W | R/W | R | R |
| Risikoregister | R/W | R/W | R | - | - |
| Audit-Berichte | R/W | R/W | - | - | - |
| Incident Reports | R/W | R/W | R/W | - | - |

**Legende:** R = Read (Lesen), W = Write (Schreiben), - = Kein Zugriff

**Zugriffsverwaltung:**
- Zugriffsrechte werden über IAM-System verwaltet
- Siehe `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md`
- Rezertifizierung: Quartalsweise

### 2.3 Offline-/Notfallzugriff

**Notfallzugriff:**
- Kritische Dokumente (Notfallpläne, Kontaktlisten) werden zusätzlich offline gespeichert
- Ablageort: [TODO: Physischer Safe, verschlüsselter USB-Stick]
- Verantwortlich: {{ meta-organisation-roles.role_CISO }}

**Break-Glass-Zugriff:**
- Siehe `0200_Notfallzugang_BreakGlass.md` (BCM-Handbuch)
- Notfallzugriff auf ISMS-Dokumentation bei Ausfall des primären Systems

<!-- 
Define offline access procedures for critical documents that may be needed
during a disaster or system outage.
-->

## 3. Dokumentenlebenszyklus

### 3.1 Erstellung

**Prozess:**
1. **Initiierung:** Bedarf wird identifiziert (z.B. neue Policy, neue Anforderung)
2. **Autor benennen:** CISO oder ISMS Manager benennt Autor
3. **Template verwenden:** Autor verwendet entsprechendes Template
4. **Entwurf erstellen:** Autor erstellt Entwurf mit Status "Entwurf"
5. **Metadaten erfassen:** Dokument-ID, Owner, Version, Klassifizierung

**Verantwortlich:** Dokumentautor (benannt durch CISO)

### 3.2 Review

**Review-Prozess:**
1. **Peer Review:** Fachliche Prüfung durch Kollegen
2. **Stakeholder Review:** Konsultation betroffener Stakeholder
3. **CISO Review:** Finale Prüfung durch CISO
4. **Status ändern:** Von "Entwurf" zu "In Review"

**Review-Kriterien:**
- Fachliche Korrektheit
- Vollständigkeit
- Konsistenz mit anderen ISMS-Dokumenten
- Compliance mit ISO 27001:2022
- Verständlichkeit und Umsetzbarkeit

**Verantwortlich:** CISO oder ISMS Manager

### 3.3 Freigabe

**Freigabe-Prozess:**
1. **Freigabe-Antrag:** Nach erfolgreichem Review
2. **Genehmigung:** Durch CISO (Policies) oder Geschäftsführung (ISMS-Leitlinie)
3. **Status ändern:** Von "In Review" zu "Freigegeben"
4. **Versionsnummer:** Finale Versionsnummer vergeben (z.B. 1.0)

**Freigabe-Befugnisse:**

| Dokumenttyp | Freigabe durch |
|-------------|----------------|
| ISMS-Leitlinie | Geschäftsführung |
| Policies (Abstract) | CISO |
| Richtlinien (Detailed) | CISO oder ISMS Manager |
| Prozessdokumente | CISO oder ISMS Manager |
| Templates | ISMS Manager |

**Verantwortlich:** Siehe Tabelle oben

### 3.4 Veröffentlichung und Kommunikation

**Veröffentlichung:**
1. **Upload:** Dokument wird im offiziellen Ablageort veröffentlicht
2. **Dokumentenregister aktualisieren:** Eintrag im Dokumentenregister
3. **Alte Version archivieren:** Vorherige Version wird archiviert

**Kommunikation:**
- **Neue Dokumente:** E-Mail-Benachrichtigung an alle betroffenen Stakeholder
- **Wesentliche Änderungen:** E-Mail-Benachrichtigung + Awareness-Kampagne
- **Kleinere Änderungen:** Eintrag im Change-Log, keine separate Benachrichtigung

**Kommunikationskanäle:**
- E-Mail an alle Mitarbeiter
- Intranet-News
- Security Awareness Training
- Team-Meetings

**Verantwortlich:** ISMS Manager

### 3.5 Änderungsmanagement

**Änderungsprozess:**
1. **Änderungsantrag:** Bedarf für Änderung wird identifiziert
2. **Impact Assessment:** Auswirkungen der Änderung bewerten
3. **Änderung durchführen:** Dokument wird aktualisiert
4. **Review und Freigabe:** Wie bei Neuerstellung
5. **Versionsnummer erhöhen:** Major (1.0 → 2.0) oder Minor (1.0 → 1.1)

**Versionierungsschema:**
- **Major Version (X.0):** Wesentliche Änderungen, neue Anforderungen
- **Minor Version (X.Y):** Kleinere Änderungen, Korrekturen, Klarstellungen

**Change-Log:**
Jedes Dokument enthält einen Change-Log mit:
- Versionsnummer
- Datum
- Autor
- Beschreibung der Änderung
- Genehmiger

**Verantwortlich:** Dokumentautor, CISO

### 3.6 Regelmäßiger Review

**Review-Intervalle:**

| Dokumenttyp | Review-Intervall |
|-------------|------------------|
| ISMS-Leitlinie | Jährlich |
| Policies (Abstract) | Jährlich |
| Richtlinien (Detailed) | Jährlich oder bei Bedarf |
| Risikoregister | Quartalsweise |
| SoA | Jährlich oder bei Scope-Änderung |
| Prozessdokumente | Alle 2 Jahre |

**Review-Trigger (anlassbezogen):**
- Neue gesetzliche Anforderungen
- Wesentliche organisatorische Änderungen
- Sicherheitsvorfälle mit Lessons Learned
- Audit-Findings
- Technologieänderungen

**Review-Prozess:**
1. **Review-Erinnerung:** ISMS Manager erinnert Owner
2. **Review durchführen:** Owner prüft Aktualität und Relevanz
3. **Entscheidung:** Keine Änderung / Änderung erforderlich
4. **Dokumentation:** Review-Datum im Dokument aktualisieren

**Verantwortlich:** Dokumentowner (siehe Dokumentenregister)

### 3.7 Archivierung und Löschung

**Archivierung:**
- **Alte Versionen:** Werden archiviert, sobald neue Version freigegeben wird
- **Archivierungsdauer:** 10 Jahre
- **Archivierungsort:** [TODO: Archiv-System]

**Löschung:**
- **Außerbetriebnahme:** Dokumente werden nach Ablauf der Archivierungsdauer gelöscht
- **Löschprozess:** Sichere Löschung gemäß `0580_Policy_Aufbewahrung_und_Loeschung.md`
- **Genehmigung:** Löschung muss durch CISO genehmigt werden

**Verantwortlich:** ISMS Manager

## 4. Versionierung

### 4.1 Versionierungsschema

**Format:** X.Y

- **X (Major Version):** Wesentliche Änderungen
  - Neue Anforderungen
  - Strukturelle Änderungen
  - Änderung des Geltungsbereichs

- **Y (Minor Version):** Kleinere Änderungen
  - Korrekturen
  - Klarstellungen
  - Aktualisierung von Kontaktdaten

**Beispiele:**
- 0.1 → Entwurf
- 1.0 → Erste freigegebene Version
- 1.1 → Kleinere Korrektur
- 2.0 → Wesentliche Überarbeitung

### 4.2 Change-Log

Jedes Dokument enthält einen Change-Log am Ende:

```markdown
## Änderungshistorie

| Version | Datum | Autor | Beschreibung | Genehmigt durch |
|---------|-------|-------|--------------|-----------------|
| 1.0 | 2026-01-15 | {{ meta-organisation-roles.role_CISO }} | Initiale Version | Geschäftsführung |
| 1.1 | 2026-03-20 | ISMS Manager | Kontaktdaten aktualisiert | CISO |
| 2.0 | 2026-12-01 | {{ meta-organisation-roles.role_CISO }} | Neue Anforderungen aus NIS2 | Geschäftsführung |
```

## 5. Dokumentenregister

Das Dokumentenregister ist die zentrale Übersicht aller ISMS-Dokumente.

### 5.1 Dokumentenregister-Struktur

| Dokument-ID | Dokumenttitel | Owner | Status | Version | Letzte Änderung | Nächster Review |
|-------------|---------------|-------|--------|---------|-----------------|-----------------|
| 0010 | ISMS-Leitlinie | {{ meta-organisation-roles.role_CISO }} | Freigegeben | 1.0 | {{ meta-handbook.modifydate }} | {{ meta-handbook.next_review }} |
| 0020 | ISMS-Geltungsbereich | {{ meta-organisation-roles.role_CISO }} | Freigegeben | 1.0 | {{ meta-handbook.modifydate }} | {{ meta-handbook.next_review }} |
| 0030 | Kontext und Stakeholder | {{ meta-organisation-roles.role_CISO }} | Freigegeben | 1.0 | {{ meta-handbook.modifydate }} | {{ meta-handbook.next_review }} |
| 0040 | ISMS-Governance | {{ meta-organisation-roles.role_CISO }} | Freigegeben | 1.0 | {{ meta-handbook.modifydate }} | {{ meta-handbook.next_review }} |
| 0050 | Dokumentenlenkung | {{ meta-organisation-roles.role_CISO }} | Freigegeben | 1.0 | {{ meta-handbook.modifydate }} | {{ meta-handbook.next_review }} |
| ... | ... | ... | ... | ... | ... | ... |

[TODO: Vollständiges Dokumentenregister erstellen und pflegen]

### 5.2 Pflege des Dokumentenregisters

**Verantwortlich:** ISMS Manager

**Aktualisierung:**
- Bei jeder Dokumentänderung
- Bei Statusänderungen
- Bei Owner-Wechsel

**Zugriff:**
- Dokumentenregister ist für alle Mitarbeiter lesbar
- Ablageort: [TODO: Link zum Dokumentenregister]

## 6. Dokumentklassifizierung

Alle ISMS-Dokumente werden klassifiziert gemäß `0280_Policy_Datenklassifizierung_und_Informationshandling.md`:

| Klassifizierung | Beschreibung | Beispiele |
|-----------------|--------------|-----------|
| **Öffentlich** | Keine Vertraulichkeit | Öffentliche Policies |
| **Intern** | Nur für Mitarbeiter | Die meisten ISMS-Dokumente |
| **Vertraulich** | Eingeschränkter Zugriff | Risikoregister, Audit-Berichte |
| **Streng vertraulich** | Sehr eingeschränkter Zugriff | Incident Reports mit sensiblen Daten |

**Kennzeichnung:**
- Klassifizierung wird im Dokument-Header angegeben
- Klassifizierung bestimmt Zugriffsrechte und Handhabung

## 7. Externe Dokumente

**Externe Dokumente** (z.B. Lieferanten-Policies, Zertifikate) werden ebenfalls kontrolliert:

**Prozess:**
1. **Identifikation:** Relevante externe Dokumente identifizieren
2. **Bewertung:** Relevanz und Vertrauenswürdigkeit prüfen
3. **Ablage:** In separatem Bereich ablegen
4. **Kennzeichnung:** Als "Externes Dokument" kennzeichnen
5. **Review:** Regelmäßig auf Aktualität prüfen

**Verantwortlich:** ISMS Manager

## 8. Aufbewahrungsfristen

| Dokumenttyp | Aufbewahrungsfrist | Rechtsgrundlage |
|-------------|-------------------|-----------------|
| ISMS-Leitlinie | 10 Jahre nach Außerbetriebnahme | ISO 27001 |
| Policies und Richtlinien | 10 Jahre nach Außerbetriebnahme | ISO 27001 |
| Risikoregister | 10 Jahre | ISO 27001 |
| Audit-Berichte | 10 Jahre | ISO 27001, Handelsrecht |
| Incident Reports | 10 Jahre | DSGVO, NIS2 |
| Schulungsnachweise | 10 Jahre | Nachweispflicht |
| Verträge | Gemäß Vertragsrecht | Handelsrecht |

Siehe `0580_Policy_Aufbewahrung_und_Loeschung.md` für Details.

## 9. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md` - Governance
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification
- `0360_Policy_Change_und_Release_Management.md` - Change Management
- `0580_Policy_Aufbewahrung_und_Loeschung.md` - Retention and Deletion

### Externe Standards
- **ISO/IEC 27001:2022** - Clause 7.5: Documented information
- **ISO/IEC 27002:2022** - Control 5.1: Policies for information security

**Genehmigt durch:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }}

