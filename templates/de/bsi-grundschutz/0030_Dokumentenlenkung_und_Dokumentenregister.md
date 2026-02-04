# Dokumentenlenkung und Dokumentenregister

**Dokument-ID:** 0030  
**Dokumenttyp:** Prozess/Grundlage  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2/200-3)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines document control procedures for the ISMS according to BSI IT-Grundschutz.
Customize all [TODO] placeholders based on your organization's document management practices.
Reference: BSI Standard 200-1 (Documentation Requirements)
-->

## 1. Zweck und Geltungsbereich

Dieses Dokument beschreibt die Dokumentenlenkung für das Informationssicherheits-Managementsystem (ISMS) von **{{ meta.organization.name }}**. Es definiert Prozesse für Erstellung, Review, Freigabe, Verteilung, Änderung und Archivierung von ISMS-Dokumenten.

### 1.1 Geltungsbereich

Diese Dokumentenlenkung gilt für alle ISMS-relevanten Dokumente:
- Leitlinien und Policies
- Richtlinien und Prozessbeschreibungen
- Sicherheitskonzepte und Risikoanalysen
- Arbeitsanweisungen und Checklisten
- Protokolle und Nachweise

## 2. Ablage und Zugriff

### 2.1 Offizieller Ablageort

**Primärer Ablageort:** [TODO: z.B. SharePoint, Confluence, DMS]

**Verantwortlich:** {{ meta.document.owner }}

Alle ISMS-Dokumente werden zentral abgelegt in:
- **Pfad:** [TODO: z.B. /ISMS/Dokumentation/]
- **Backup:** [TODO: Backup-Strategie]
- **Versionierung:** Automatische Versionierung aktiviert

### 2.2 Zugriffskontrolle (RBAC)

Zugriff auf ISMS-Dokumente erfolgt rollenbasiert:

| Rolle | Lesen | Schreiben | Freigeben | Löschen |
|---|---|---|---|---|
| Geschäftsführung | ✓ | ✗ | ✓ | ✗ |
| ISB | ✓ | ✓ | ✓ | ✓ |
| ISMS-Team | ✓ | ✓ | ✗ | ✗ |
| Informationsverbund-Verantwortliche | ✓ | ✓ (eigene Dokumente) | ✗ | ✗ |
| Alle Mitarbeitenden | ✓ (öffentliche Dokumente) | ✗ | ✗ | ✗ |

### 2.3 Klassifizierung und Schutzbedarf

| Klassifizierung | Beschreibung | Zugriff | Beispiele |
|---|---|---|---|
| **Öffentlich** | Keine Vertraulichkeit | Alle Mitarbeitenden | Awareness-Material |
| **Intern** | Nur für interne Nutzung | Alle Mitarbeitenden | Policies, Richtlinien |
| **Vertraulich** | Eingeschränkter Zugriff | ISMS-Team, Berechtigte | Risikoanalysen, Sicherheitskonzepte |
| **Streng vertraulich** | Höchste Vertraulichkeit | Geschäftsführung, ISB | Incident-Berichte, Audit-Findings |

### 2.4 Notfallzugriff

Im Notfall (z.B. Ausfall des ISB) haben folgende Personen Zugriff auf alle ISMS-Dokumente:
- **Geschäftsführung:** {{ meta.ceo.name }}
- **IT-Leitung:** {{ meta.cio.name }}
- **Stellvertretender ISB:** [TODO]

## 3. Dokumentenlebenszyklus

### 3.1 Erstellung

**Prozess:**
1. **Initiierung:** Bedarf wird identifiziert (ISB, ISMS-Team, Fachabteilung)
2. **Erstellung:** Autor erstellt Dokument basierend auf Template
3. **Qualitätssicherung:** Peer-Review durch ISMS-Team
4. **Freigabe:** Freigabe durch zuständige Rolle (siehe Freigabematrix)

**Verantwortlich:** Dokumentautor, ISB (Koordination)

### 3.2 Review und Freigabe

#### 3.2.1 Freigabematrix

| Dokumenttyp | Ersteller | Reviewer | Genehmiger |
|---|---|---|---|
| Leitlinien/Policies | ISB | ISMS-Team | Geschäftsführung |
| Richtlinien | ISB, Fachabteilung | ISMS-Team | ISB |
| Sicherheitskonzepte | Informationsverbund-Verantwortliche | ISB | ISB |
| Arbeitsanweisungen | Fachabteilung | ISB | IT-Leitung |
| Risikoanalysen | ISB | ISMS-Team | Geschäftsführung |

#### 3.2.2 Review-Intervalle

| Dokumenttyp | Review-Intervall | Verantwortlich |
|---|---|---|
| Leitlinien/Policies | Jährlich | ISB |
| Richtlinien | Jährlich | ISB |
| Sicherheitskonzepte | Jährlich oder bei Änderungen | Informationsverbund-Verantwortliche |
| Arbeitsanweisungen | Jährlich | Fachabteilung |
| Risikoanalysen | Jährlich oder bei wesentlichen Änderungen | ISB |

**Zusätzliche Review-Trigger:**
- Wesentliche Änderungen in der IT-Infrastruktur
- Neue gesetzliche Anforderungen
- Sicherheitsvorfälle
- Audit-Findings
- Organisatorische Änderungen

### 3.3 Versionierung

**Versionierungsschema:**
- **Major Version (X.0):** Wesentliche inhaltliche Änderungen, neue Freigabe erforderlich
- **Minor Version (X.Y):** Kleinere Anpassungen, redaktionelle Änderungen

**Beispiel:**
- Version 1.0: Initiale Freigabe
- Version 1.1: Kleinere Anpassungen
- Version 2.0: Wesentliche Überarbeitung

### 3.4 Verteilung und Kommunikation

**Verteilungsprozess:**
1. Freigabe des Dokuments
2. Veröffentlichung im zentralen Ablageort
3. Benachrichtigung betroffener Stakeholder (E-Mail, Intranet)
4. Schulung/Awareness (falls erforderlich)
5. Bestätigung der Kenntnisnahme (bei kritischen Dokumenten)

**Verantwortlich:** ISB

### 3.5 Änderungsmanagement

**Prozess für Änderungen:**
1. **Änderungsantrag:** Initiator stellt Änderungsantrag an ISB
2. **Bewertung:** ISB bewertet Änderungsbedarf und Auswirkungen
3. **Genehmigung:** Genehmigung durch zuständige Rolle
4. **Umsetzung:** Autor aktualisiert Dokument
5. **Review:** Review durch ISMS-Team
6. **Freigabe:** Freigabe gemäß Freigabematrix
7. **Verteilung:** Kommunikation der Änderungen

### 3.6 Archivierung und Löschung

**Archivierung:**
- Alte Versionen werden für [TODO: z.B. 5 Jahre] archiviert
- Archivierte Dokumente sind schreibgeschützt
- Zugriff nur für ISB und Audit

**Löschung:**
- Dokumente werden nach Ablauf der Aufbewahrungsfrist gelöscht
- Löschung erfolgt gemäß Datenschutz- und Compliance-Anforderungen
- Löschprotokoll wird geführt

**Verantwortlich:** ISB

## 4. Dokumentenregister

<!-- 
TEMPLATE AUTHOR NOTE:
Maintain this register with all ISMS documents. Update regularly.
-->

| Dokument | ID | Owner | Status | Version | Letzte Aktualisierung | Nächster Review |
|---|---|---|---|---|---|---|
| Informationssicherheitsleitlinie | 0010 | {{ meta.ciso.name }} | {{ meta.document.status }} | {{ meta.document.version }} | {{ meta.document.last_updated }} | {{ meta.document.next_review }} |
| ISMS-Organisation, Rollen und RACI | 0020 | {{ meta.ciso.name }} | {{ meta.document.status }} | {{ meta.document.version }} | {{ meta.document.last_updated }} | {{ meta.document.next_review }} |
| Dokumentenlenkung | 0030 | {{ meta.ciso.name }} | {{ meta.document.status }} | {{ meta.document.version }} | {{ meta.document.last_updated }} | {{ meta.document.next_review }} |
| [TODO: Weitere Dokumente ergänzen] | | | | | | |

## 5. Änderungsprotokoll

| Version | Datum | Änderung | Autor | Genehmiger | Status |
|---|---|---|---|---|---|
| 0.1 | {{ meta.document.last_updated }} | Erster Entwurf | {{ meta.document.owner }} | - | Entwurf |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Qualitätssicherung

### 6.1 Dokumentenqualität

Alle ISMS-Dokumente müssen folgende Qualitätskriterien erfüllen:
- **Vollständigkeit:** Alle erforderlichen Inhalte vorhanden
- **Korrektheit:** Inhaltlich korrekt und aktuell
- **Verständlichkeit:** Klar und verständlich formuliert
- **Konsistenz:** Konsistent mit anderen ISMS-Dokumenten
- **Nachvollziehbarkeit:** Änderungen nachvollziehbar dokumentiert

### 6.2 Dokumenten-Templates

Für alle Dokumenttypen existieren Templates mit:
- Standardisiertem Header (Metadaten)
- Strukturvorgaben
- Platzhaltern für variable Inhalte
- Hinweisen für Autoren

**Ablageort Templates:** [TODO: z.B. /ISMS/Templates/]

## 7. Schulung und Awareness

Alle Dokumentautoren und ISMS-Team-Mitglieder werden geschult in:
- Dokumentenlenkungsprozess
- Verwendung von Templates
- Versionierung und Änderungsmanagement
- Klassifizierung und Schutzbedarf

**Verantwortlich:** ISB

## 8. Überwachung und Verbesserung

Der Dokumentenlenkungsprozess wird regelmäßig überwacht:
- **Metriken:** Anzahl Dokumente, Review-Compliance, Änderungsrate
- **Review:** Jährliche Überprüfung des Prozesses
- **Verbesserung:** Kontinuierliche Optimierung basierend auf Feedback

**Nächster Review:** {{ meta.document.next_review }}

---

**Referenzen:**
- BSI Standard 200-1: Managementsysteme für Informationssicherheit (ISMS)
- BSI Standard 200-2: IT-Grundschutz-Methodik

<!-- End of template -->
