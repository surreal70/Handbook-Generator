# Richtlinie: IAM - Joiner, Mover, Leaver und Zugriffsanträge

**Dokument-ID:** 0230
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This guideline provides detailed implementation guidance for Identity and Access Management,
specifically covering the Joiner-Mover-Leaver lifecycle and access request processes.
Customize based on your organization's HR systems, IAM tools, and approval workflows.
-->

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` und definiert detaillierte Prozesse für:
- **Joiner:** Onboarding neuer Mitarbeiter und Zugriffsbereitstellung
- **Mover:** Rollenwechsel und Zugriffsanpassungen
- **Leaver:** Offboarding und Zugriffsentzug
- **Zugriffsanträge:** Prozess für Ad-hoc-Zugriffsanforderungen

**Geltungsbereich:** Alle Mitarbeiter, Auftragnehmer und Dritte bei **{{ meta-organisation.name }}**

## 2. Joiner-Prozess (Onboarding)

### 2.1 Prozessübersicht

**Trigger:** HR erstellt neuen Mitarbeiter in HR-System ({{ meta.hr.system }})

**Zeitrahmen:**
- **Standard-Accounts:** Bereitstellung bis 1 Tag vor Arbeitsbeginn
- **Spezial-Zugriffe:** Bereitstellung bis 3 Tage vor Arbeitsbeginn
- **Externe Auftragnehmer:** Bereitstellung nach Vertragsunterzeichnung

### 2.2 Detaillierter Workflow

**Phase 1: HR-Initiierung (T-5 Tage)**
1. HR erstellt Mitarbeiterdatensatz in {{ meta.hr.system }}
2. HR definiert:
   - Abteilung, Rolle, Standort
   - Vorgesetzter, Kostenstelle
   - Startdatum, Vertragstyp (Festanstellung, Zeitarbeit, Praktikum)
3. Automatische Benachrichtigung an IT-Betrieb

**Phase 2: IT-Provisionierung (T-3 Tage)**
1. **Account-Erstellung:**
   - Active Directory / Azure AD Account
   - E-Mail-Postfach ({{ meta.email.system }})
   - Benutzername nach Schema: `{{ meta.naming.user_format }}` (z.B. vorname.nachname)
   - Initiales Passwort (temporär, muss bei erstem Login geändert werden)

2. **Basis-Zugriffe (automatisch via Rollenmodell):**
   - Zugriff auf Intranet und Collaboration-Tools
   - Standard-Anwendungen für Abteilung
   - Netzlaufwerke gemäß Abteilungszugehörigkeit
   - VPN-Zugang (falls Remote Work)

3. **Hardware-Bereitstellung:**
   - Laptop/Desktop gemäß Rolle (siehe Hardware-Katalog)
   - Mobilgerät (falls erforderlich)
   - Peripherie (Monitor, Tastatur, Maus)
   - Asset-Tagging und Inventarisierung

**Phase 3: Spezial-Zugriffe (T-2 Tage)**
1. Vorgesetzter beantragt spezielle Zugriffe über Self-Service-Portal
2. Genehmigung durch Ressourcen-Owner
3. Provisionierung durch IT-Betrieb oder automatisiert

**Phase 4: Onboarding-Tag (T-0)**
1. **Willkommens-E-Mail:**
   - Zugangsdaten (initiales Passwort)
   - Links zu Schulungen und Policies
   - Kontaktinformationen IT-Support
2. **Erste Anmeldung:**
   - Passwortänderung erzwungen
   - MFA-Registrierung (Authenticator-App, Hardware-Token)
   - Bestätigung der Acceptable Use Policy
3. **IT-Einweisung:**
   - Gerätenutzung, VPN-Zugang
   - Passwort-Manager-Schulung
   - Phishing-Awareness-Grundlagen

### 2.3 Rollenbasierte Zugriffe (RBAC)

**Standard-Rollen:**

| Rolle | Beschreibung | Automatische Zugriffe |
|-------|--------------|----------------------|
| Employee_Standard | Alle Mitarbeiter | Intranet, E-Mail, Office 365, VPN |
| Employee_Developer | Entwickler | + Git, CI/CD, Dev-Umgebungen |
| Employee_Finance | Finanzabteilung | + ERP, Buchhaltungssoftware |
| Employee_HR | Personalabteilung | + HR-System, Bewerbermanagement |
| Employee_Sales | Vertrieb | + CRM, Angebotssystem |
| Contractor_Standard | Externe Auftragnehmer | Basis-Zugriffe, zeitlich befristet |
| Contractor_Developer | Externe Entwickler | + Dev-Zugriffe, zeitlich befristet |

**Privilegierte Rollen:**
- `Admin_System`: Systemadministratoren (Windows, Linux)
- `Admin_Network`: Netzwerkadministratoren
- `Admin_Security`: Security-Team
- `Admin_Database`: Datenbankadministratoren

### 2.4 Externe Auftragnehmer und Dritte

**Besonderheiten:**
- **Vertragsprüfung:** IT-Zugriff nur nach Vertragsunterzeichnung und NDA
- **Zeitliche Befristung:** Accounts automatisch deaktiviert nach Vertragsende
- **Eingeschränkte Zugriffe:** Nur projektbezogene Ressourcen
- **Sponsorship:** Jeder externe Account benötigt internen Sponsor
- **Rezertifizierung:** Quartalsweise Überprüfung durch Sponsor

## 3. Mover-Prozess (Rollenwechsel)

### 3.1 Prozessübersicht

**Trigger:** HR aktualisiert Mitarbeiterdaten (Abteilungswechsel, Beförderung, neue Rolle)

**Zeitrahmen:** Zugriffsanpassung innerhalb 2 Arbeitstagen nach HR-Änderung

### 3.2 Detaillierter Workflow

**Phase 1: HR-Änderung**
1. HR aktualisiert Mitarbeiterdatensatz in {{ meta.hr.system }}
2. Änderungen: Abteilung, Rolle, Vorgesetzter, Standort
3. Automatische Benachrichtigung an IT-Betrieb und bisherigen/neuen Vorgesetzten

**Phase 2: Zugriffs-Review**
1. **Alter Vorgesetzter:** Bestätigt Entzug nicht mehr benötigter Zugriffe
2. **Neuer Vorgesetzter:** Beantragt neue erforderliche Zugriffe
3. **IT-Betrieb:** Prüft aktuelle Zugriffe und plant Änderungen

**Phase 3: Zugriffsanpassung**
1. **Entzug alter Zugriffe:**
   - Entfernung aus alten Abteilungs-Gruppen
   - Entzug abteilungsspezifischer Anwendungszugriffe
   - Archivierung alter E-Mails (falls Postfachwechsel)
2. **Bereitstellung neuer Zugriffe:**
   - Hinzufügen zu neuen Abteilungs-Gruppen
   - Provisionierung neuer Anwendungszugriffe
   - Anpassung Netzlaufwerke und Berechtigungen

**Phase 4: Dokumentation**
1. Aktualisierung CMDB und Asset-Management
2. Dokumentation der Zugriffsänderungen
3. Benachrichtigung an Mitarbeiter über Änderungen

### 3.3 Beförderungen und Privilegien-Erhöhung

**Zusätzliche Prüfungen bei Privilegien-Erhöhung:**
- **Genehmigung:** CISO-Genehmigung für privilegierte Rollen
- **Background Check:** Erweiterte Überprüfung bei Admin-Rechten
- **Schulung:** Zusätzliche Security-Schulungen für privilegierte Nutzer
- **Monitoring:** Erhöhtes Monitoring privilegierter Aktivitäten

## 4. Leaver-Prozess (Offboarding)

### 4.1 Prozessübersicht

**Trigger:** HR markiert Mitarbeiter als ausscheidend in {{ meta.hr.system }}

**Zeitrahmen:**
- **Geplantes Ausscheiden:** Deaktivierung am letzten Arbeitstag
- **Ungeplantes Ausscheiden:** Sofortige Deaktivierung (z.B. Kündigung, Notfall)

### 4.2 Detaillierter Workflow

**Phase 1: Vorbereitung (T-14 Tage)**
1. HR informiert IT-Betrieb über Austrittsdatum
2. **Wissenstransfer:**
   - Vorgesetzter identifiziert kritische Zugriffe und Informationen
   - Übergabe an Nachfolger oder Team
   - Dokumentation von Passwörtern für Shared Accounts (in Password Manager)
3. **Daten-Backup:**
   - Sicherung persönlicher Laufwerke
   - Archivierung E-Mail-Postfach
   - Übergabe projektrelevanter Dateien

**Phase 2: Letzter Arbeitstag (T-0)**
1. **Account-Deaktivierung (End of Business Day):**
   - Active Directory / Azure AD Account deaktiviert
   - E-Mail-Weiterleitung an Vorgesetzten (temporär, 30 Tage)
   - VPN-Zugang gesperrt
   - Alle Anwendungszugriffe entzogen
2. **Hardware-Rückgabe:**
   - Laptop, Mobilgerät, Peripherie
   - Zutrittskarten, Schlüssel
   - Asset-Inventar aktualisiert
3. **Exit-Interview:**
   - Rückgabe aller Unternehmenseigentum
   - Erinnerung an Vertraulichkeitsverpflichtungen
   - Bestätigung der Datenrückgabe

**Phase 3: Post-Offboarding (T+30 Tage)**
1. **Account-Löschung:**
   - Nach 30 Tagen: Endgültige Löschung des Accounts
   - E-Mail-Archivierung gemäß Retention Policy ({{ meta.retention.email_years }} Jahre)
   - Löschung persönlicher Daten (DSGVO-konform)
2. **Lizenz-Freigabe:**
   - Rückgabe von Software-Lizenzen
   - Aktualisierung Lizenz-Management
3. **Dokumentation:**
   - Offboarding-Checkliste abgeschlossen
   - Audit-Trail für Compliance

### 4.3 Notfall-Offboarding

**Sofortige Deaktivierung bei:**
- Kündigung aus wichtigem Grund
- Sicherheitsvorfälle oder Verdacht auf Missbrauch
- Gerichtliche Anordnungen

**Prozess:**
1. **Sofortige Sperrung (innerhalb 1 Stunde):**
   - Alle Accounts deaktiviert
   - VPN und Remote-Zugriffe gesperrt
   - Zutrittskarten deaktiviert
   - Mobilgeräte remote gelöscht (falls MDM)
2. **Forensik:**
   - Sicherung von Logs und Aktivitäten
   - Analyse bei Verdacht auf Datenmissbrauch
   - Einbeziehung Legal und HR
3. **Kommunikation:**
   - Information an Vorgesetzten und Security-Team
   - Dokumentation für rechtliche Zwecke

## 5. Zugriffsanträge (Access Requests)

### 5.1 Self-Service-Portal

**Zugriff:** {{ meta.iam.portal_url }}

**Funktionen:**
- Antrag auf neue Zugriffe (Anwendungen, Netzlaufwerke, Gruppen)
- Übersicht eigener Zugriffe
- Status-Tracking von Anträgen
- Rezertifizierung eigener Zugriffe

### 5.2 Antrags-Workflow

**Schritt 1: Antragstellung**
1. Mitarbeiter stellt Antrag über Self-Service-Portal
2. **Pflichtangaben:**
   - Ressource/Anwendung
   - Begründung (Business Justification)
   - Benötigte Berechtigungsstufe
   - Zeitraum (permanent oder befristet)

**Schritt 2: Genehmigung**
1. **Vorgesetzter:** Prüft geschäftliche Notwendigkeit (1. Genehmigung)
2. **Ressourcen-Owner:** Prüft fachliche Berechtigung (2. Genehmigung)
3. **CISO:** Zusätzliche Genehmigung bei privilegierten Zugriff en
4. **Automatische Genehmigung:** Bei Standard-Zugriff en nach Rollenmodell

**Schritt 3: Provisionierung**
1. **Automatisch:** Bei Standard-Anwendungen (innerhalb 15 Minuten)
2. **Manuell:** Bei Spezial-Zugriff en (innerhalb 1 Arbeitstag)
3. **Benachrichtigung:** E-Mail an Antragsteller bei Abschluss

**Schritt 4: Dokumentation**
1. Audit-Trail im IAM-System
2. Aktualisierung CMDB
3. Compliance-Reporting

### 5.3 Befristete Zugriffe

**Anwendungsfälle:**
- Projektbezogene Zugriffe
- Vertretungen (Urlaub, Krankheit)
- Externe Auftragnehmer
- Test- und Entwicklungszugriffe

**Automatische Deaktivierung:**
- System deaktiviert Zugriff automatisch nach Ablaufdatum
- Benachrichtigung an Nutzer 7 Tage vor Ablauf
- Verlängerung nur über erneuten Antrag

## 6. Rezertifizierung

### 6.1 Regelmäßige Zugriffs-Reviews

**Frequenz:**
- **Standard-Nutzer:** Jährliche Rezertifizierung
- **Privilegierte Nutzer:** Quartalsweise Rezertifizierung
- **Externe Auftragnehmer:** Quartalsweise Rezertifizierung
- **Kritische Systeme:** Monatliche Rezertifizierung

### 6.2 Rezertifizierungs-Prozess

**Schritt 1: Automatische Kampagne**
1. IAM-System startet Rezertifizierungs-Kampagne
2. E-Mail an Vorgesetzte mit Liste der Mitarbeiter-Zugriffe
3. Deadline: 14 Tage für Bestätigung

**Schritt 2: Review durch Vorgesetzte**
1. Vorgesetzter prüft jeden Zugriff:
   - **Bestätigen:** Zugriff weiterhin erforderlich
   - **Entziehen:** Zugriff nicht mehr benötigt
   - **Eskalieren:** Unsicherheit, Rückfrage an Ressourcen-Owner
2. Dokumentation der Entscheidung

**Schritt 3: Automatische Durchsetzung**
1. Bestätigte Zugriffe bleiben aktiv
2. Nicht bestätigte Zugriffe werden nach Deadline automatisch entzogen
3. Eskalierte Fälle werden an CISO weitergeleitet

**Schritt 4: Reporting**
1. Compliance-Report für Audit
2. Identifikation von Zugriffs-Anomalien
3. Optimierung Rollenmodell

### 6.3 Privilegierte Zugriffe

**Zusätzliche Kontrollen:**
- **Vier-Augen-Prinzip:** Zwei Genehmigungen erforderlich
- **Just-in-Time (JIT) Access:** Privilegien nur bei Bedarf, zeitlich befristet
- **Privileged Access Management (PAM):** Verwaltung über PAM-System ({{ meta.security.pam_solution }})
- **Session-Recording:** Aufzeichnung privilegierter Sessions für Audit

## 7. Technische Implementierung

### 7.1 IAM-Technologie-Stack

**Systeme:**
- **Identity Provider:** {{ meta.iam.idp }} (z.B. Azure AD, Okta)
- **HR-System:** {{ meta.hr.system }} (z.B. SAP SuccessFactors, Workday)
- **IAM-Portal:** {{ meta.iam.portal }} (z.B. SailPoint, Saviynt)
- **PAM-System:** {{ meta.security.pam_solution }} (z.B. CyberArk, BeyondTrust)
- **CMDB:** {{ meta.itsm.cmdb }} (z.B. ServiceNow, Jira Service Management)

**Integration:**
- HR-System → IAM-System (automatische Synchronisation)
- IAM-System → Active Directory / Azure AD (Provisionierung)
- IAM-System → Anwendungen (SCIM, SAML, API)

### 7.2 Automatisierung

**Automatisierte Prozesse:**
- Account-Erstellung bei Joiner (innerhalb 1 Stunde nach HR-Eintrag)
- Rollenbasierte Zugriffsvergabe (RBAC)
- Account-Deaktivierung bei Leaver (am letzten Arbeitstag)
- Befristete Zugriffe (automatische Deaktivierung)
- Rezertifizierungs-Kampagnen (automatischer Start)

**Manuelle Prozesse:**
- Spezial-Zugriffe außerhalb Rollenmodell
- Privilegierte Zugriffe (nach Genehmigung)
- Notfall-Offboarding (sofortige Sperrung)

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert | Messung |
|--------|----------|---------|
| Joiner-Provisionierung | < 1 Tag | IAM-System |
| Leaver-Deaktivierung | 100% am letzten Tag | IAM-System |
| Zugriffsanträge (Bearbeitungszeit) | < 1 Arbeitstag | IAM-System |
| Rezertifizierung (Completion Rate) | > 95% | IAM-System |
| Verwaiste Accounts | 0 | Quartalsweise Prüfung |

### 8.2 Audit-Nachweise

**Dokumentation:**
- Joiner/Mover/Leaver-Logs (Audit-Trail)
- Zugriffsanträge und Genehmigungen
- Rezertifizierungs-Berichte
- Privilegierte Zugriffe und Genehmigungen
- Notfall-Offboarding-Dokumentation

**Audit-Frequenz:**
- Interne Audits: Quartalsweise
- Externe Audits: Jährlich (ISO 27001)
- Ad-hoc-Audits: Bei Sicherheitsvorfällen

## 9. Referenzen

### Interne Dokumente
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Übergeordnete Policy
- `0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md` - Authentifizierung
- `0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md` - HR Security
- `0640_Policy_Ausnahmen_und_Risk_Waivers.md` - Exception Process

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.15** - Access control
- **ISO/IEC 27001:2022 Annex A.5.16** - Identity management
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights
- **NIST SP 800-63** - Digital Identity Guidelines

**Genehmigt durch:**  
{{ meta.ciso.name }}, CISO  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }}

