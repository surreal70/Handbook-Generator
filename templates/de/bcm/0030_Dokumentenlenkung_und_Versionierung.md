# Dokumentenlenkung und Versionierung

**Dokument-ID:** BCM-0030  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines document control procedures for the BCMS.
It aligns with ISO 22301:2019 Clause 7.5 (Documented information).

Customization required:
- Define document repository and access controls
- Establish version control scheme
- Define review and approval workflows
- Ensure offline availability for emergency access
-->

## 1. Dokumentenlandkarte

### 1.1 BCM-Dokumentenstruktur

Die BCM-Dokumentation der {{ meta.organization.name }} umfasst folgende Dokumententypen:

**Strategische Dokumente:**
- BCM-Policy und Leitlinie
- BCM-Strategie und Ziele
- Geltungsbereich und Scope

**Operative Dokumente:**
- Business Impact Analysis (BIA)
- Risikoanalyse und Szenarien
- Business Continuity Pläne (BCP)
- IT Disaster Recovery Pläne (DRP)
- Krisenmanagementpläne

**Unterstützende Dokumente:**
- Kontaktlisten und Eskalationsmatrizen
- Runbooks und Checklisten
- Testprotokolle und Übungsberichte
- Schulungsunterlagen

### 1.2 Dokumentenablage

**Primäre Ablage:**
[TODO: Definieren Sie das primäre Dokumentenmanagementsystem]

**Beispiel:**
- **System:** SharePoint / Confluence / Dokumentenmanagementsystem
- **Pfad:** `BCM/Dokumentation/`
- **Zugriff:** Rollenbasiert (RBAC) gemäß Berechtigungskonzept
- **Backup:** Tägliche Sicherung, 30 Tage Aufbewahrung

**Offline-Verfügbarkeit / Notfallzugriff:**

Kritische BCM-Dokumente müssen auch bei Ausfall der IT-Systeme verfügbar sein:

[TODO: Definieren Sie Offline-Zugriffsmöglichkeiten]

**Beispiel:**
- **Notfall-USB-Sticks:** Verschlüsselte USB-Sticks mit aktuellen BCM-Plänen bei Krisenstabsmitgliedern
- **Papierausdrucke:** Versiegelte Notfallordner an definierten Standorten (Tresor, Ausweichstandort)
- **Cloud-Backup:** Zugriff über mobile Geräte auch bei Ausfall des Hauptstandorts
- **Aktualisierung:** Quartalsweise oder bei wesentlichen Änderungen

### 1.3 Dokumentenregister

| Dokument-ID | Dokumentname | Version | Owner | Klassifizierung | Ablageort |
|-------------|--------------|---------|-------|-----------------|-----------|
| BCM-0010 | Zweck und Geltungsbereich | {{ meta.document.version }} | {{ meta.document.owner }} | {{ meta.document.classification }} | [TODO: Pfad] |
| BCM-0020 | BCM-Leitlinie / Policy | {{ meta.document.version }} | {{ meta.document.owner }} | {{ meta.document.classification }} | [TODO: Pfad] |
| BCM-0030 | Dokumentenlenkung | {{ meta.document.version }} | {{ meta.document.owner }} | {{ meta.document.classification }} | [TODO: Pfad] |
| ... | ... | ... | ... | ... | ... |

[TODO: Vervollständigen Sie das Dokumentenregister]

## 2. Versionierung

### 2.1 Versionierungsschema

Die {{ meta.organization.name }} verwendet folgendes Versionierungsschema für BCM-Dokumente:

**Format:** `MAJOR.MINOR.PATCH`

**Beispiel:** Version 2.3.1

- **MAJOR (2):** Wesentliche inhaltliche Änderungen, neue Struktur, neue Anforderungen
- **MINOR (3):** Ergänzungen, Aktualisierungen ohne grundlegende Änderungen
- **PATCH (1):** Korrekturen, Formatierungen, redaktionelle Änderungen

### 2.2 Versionserhöhung

**MAJOR-Version erhöhen bei:**
- Grundlegender Neustrukturierung des Dokuments
- Wesentlichen Änderungen der BCM-Strategie oder -Prozesse
- Neuen regulatorischen Anforderungen
- Änderungen des Geltungsbereichs

**MINOR-Version erhöhen bei:**
- Ergänzung neuer Abschnitte oder Prozesse
- Aktualisierung von Kontaktdaten oder Rollen
- Anpassung an organisatorische Änderungen
- Ergebnissen aus Übungen oder Tests

**PATCH-Version erhöhen bei:**
- Rechtschreibkorrekturen
- Formatierungsänderungen
- Aktualisierung von Verweisen
- Redaktionellen Anpassungen

### 2.3 Versionsstatus

| Status | Beschreibung | Verwendung |
|--------|--------------|------------|
| **Entwurf** | Dokument in Erstellung | Nur für Autoren sichtbar |
| **In Review** | Dokument in Prüfung | Für Reviewer sichtbar |
| **Freigegeben** | Dokument genehmigt und aktiv | Für alle Berechtigten sichtbar |
| **Archiviert** | Dokument veraltet, historisch | Nur für Archivzwecke |

## 3. Freigabe- und Review-Prozess

### 3.1 Rollen im Dokumentenprozess

**Ersteller (Author):**
- **Verantwortlich:** Fachverantwortlicher oder BCM-Manager
- **Aufgaben:** Erstellung und Pflege des Dokumenteninhalts

**Reviewer (Prüfer):**
- **Verantwortlich:** Fachexperten, betroffene Stakeholder
- **Aufgaben:** Inhaltliche Prüfung, Feedback, Freigabeempfehlung

**Approver (Genehmiger):**
- **Verantwortlich:** {{ meta.document.approver }} oder delegierte Führungskraft
- **Aufgaben:** Formale Freigabe, Verantwortungsübernahme

### 3.2 Freigabeprozess

1. **Erstellung:** Autor erstellt Dokument im Status "Entwurf"
2. **Review:** Dokument wird an Reviewer zur Prüfung übergeben (Status: "In Review")
3. **Überarbeitung:** Autor arbeitet Feedback ein
4. **Genehmigung:** Approver gibt Dokument frei (Status: "Freigegeben")
5. **Veröffentlichung:** Dokument wird für Zielgruppe bereitgestellt
6. **Archivierung:** Alte Version wird archiviert

### 3.3 Review-Intervalle

| Dokumenttyp | Review-Intervall | Verantwortlich |
|-------------|------------------|----------------|
| BCM-Policy | Jährlich | {{ meta.roles.ceo.name }} |
| BIA-Ergebnisse | Jährlich | BCM-Manager |
| BCM-Pläne (BCP/DRP) | Halbjährlich | Fachverantwortliche |
| Kontaktlisten | Quartalsweise | BCM-Manager |
| Runbooks | Nach jeder Übung | IT-Operations |

**Anlassbezogene Reviews:**
- Nach schwerwiegenden Vorfällen
- Bei organisatorischen Änderungen
- Bei Änderungen regulatorischer Anforderungen
- Nach Audits oder Zertifizierungen

## 4. Verteiler und Zugriffsrechte

### 4.1 Zielgruppen

**Krisenstab:**
- Zugriff auf alle BCM-Dokumente
- Offline-Kopien der kritischen Pläne
- Benachrichtigung bei Änderungen

**IT-Operations:**
- Zugriff auf IT-DR-Pläne und Runbooks
- Technische Dokumentation
- Kontaktlisten

**Fachbereiche:**
- Zugriff auf relevante BCP-Pläne
- Prozessspezifische Runbooks
- Schulungsunterlagen

**Externe Dienstleister:**
- Zugriff auf relevante Auszüge (NDA erforderlich)
- Keine Zugriff auf vertrauliche Kontaktdaten
- Nur freigegebene Versionen

### 4.2 Zugriffskontrolle (RBAC)

[TODO: Definieren Sie rollenbasierte Zugriffsrechte]

**Beispiel:**

| Rolle | Lesen | Schreiben | Genehmigen | Löschen |
|-------|-------|-----------|------------|---------|
| BCM-Manager | ✓ | ✓ | ✓ | ✓ |
| Krisenstab | ✓ | - | - | - |
| Fachbereich | ✓ (eigene Pläne) | ✓ (eigene Pläne) | - | - |
| IT-Operations | ✓ (IT-Pläne) | ✓ (IT-Pläne) | - | - |
| Externe | ✓ (freigegebene) | - | - | - |

### 4.3 Schutzbedarf und Klassifizierung

| Klassifizierung | Beschreibung | Beispieldokumente |
|-----------------|--------------|-------------------|
| **Öffentlich** | Keine Schutzbedürftigkeit | BCM-Policy (extern) |
| **Intern** | Nur für Mitarbeiter | BCM-Handbuch, Schulungsunterlagen |
| **Vertraulich** | Eingeschränkter Personenkreis | BIA-Ergebnisse, Kontaktlisten |
| **Streng vertraulich** | Nur für Krisenstab | Notfallzugänge, Passwörter |

## 5. Änderungsprotokoll (Changelog)

### 5.1 Dokumenthistorie

| Version | Datum | Änderung | Autor | Reviewer | Genehmigt durch |
|---------|-------|----------|-------|----------|-----------------|
| 0.1 | {{ meta.document.last_updated }} | Initiale Erstellung | {{ meta.defaults.author }} | [TODO] | [TODO] |

[TODO: Aktualisieren Sie das Änderungsprotokoll bei jeder Dokumentenänderung]

### 5.2 Änderungsanforderungen

Änderungsanforderungen an BCM-Dokumente können eingereicht werden durch:

- **E-Mail an:** [TODO: BCM-Manager E-Mail]
- **Ticketsystem:** [TODO: System und Kategorie]
- **Formular:** [TODO: Link zu Änderungsanforderungsformular]

Jede Änderungsanforderung wird geprüft und priorisiert. Die Bearbeitung erfolgt gemäß definierter SLAs.

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
