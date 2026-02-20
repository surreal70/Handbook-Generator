# Policy: Authentisierung und Passwörter

**Dokument-ID:** 0240
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



## 1. Zweck

Diese Policy definiert die Grundsätze für Authentisierung und Passwortmanagement der **AdminSend GmbH**. Sie stellt sicher, dass die Identität von Nutzern sicher verifiziert wird und Authentisierungsinformationen angemessen geschützt werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Systeme:** Alle IT-Systeme, Anwendungen, Datenbanken, Netzwerke, Cloud-Services
- **Personen:** Alle Mitarbeiter, Auftragnehmer, Lieferanten und Dritte mit Zugang zu IT-Ressourcen
- **Authentisierungsmethoden:** Passwörter, Multi-Faktor-Authentisierung (MFA), biometrische Verfahren, Token
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Starke Authentisierung
Alle Zugriffe auf IT-Systeme und Anwendungen erfordern eine sichere Authentisierung. Die Stärke der Authentisierung richtet sich nach dem Schutzbedarf der Ressource und dem Risiko.

### 3.2 Multi-Faktor-Authentisierung (MFA)
Für den Zugriff auf kritische Systeme, privilegierte Accounts und Remote-Zugriffe ist Multi-Faktor-Authentisierung (MFA) verpflichtend. MFA kombiniert mindestens zwei unabhängige Faktoren:
- Wissen (Passwort, PIN)
- Besitz (Token, Smartphone, Smartcard)
- Biometrie (Fingerabdruck, Gesichtserkennung)

### 3.3 Passwortanforderungen
Passwörter müssen folgenden Mindestanforderungen entsprechen:
- Ausreichende Länge und Komplexität (Details in Richtlinie)
- Keine Wiederverwendung alter Passwörter
- Keine Weitergabe oder Aufschreibung
- Regelmäßige Änderung bei Verdacht auf Kompromittierung

### 3.4 Passwortlose Authentisierung
Die Organisation fördert den Einsatz passwortloser Authentisierungsmethoden (z.B. FIDO2, Windows Hello, biometrische Verfahren) wo technisch möglich und sicher.

### 3.5 Session Management
Authentisierte Sitzungen (Sessions) werden durch geeignete Maßnahmen geschützt:
- Automatische Sperrung bei Inaktivität
- Sichere Session-Token
- Logout-Funktionalität
- Keine parallelen Sessions für privilegierte Accounts

### 3.6 Schutz von Authentisierungsinformationen
Passwörter und andere Authentisierungsinformationen werden sicher gespeichert:
- Verschlüsselte oder gehashte Speicherung (keine Klartext-Passwörter)
- Sichere Übertragung (TLS/SSL)
- Schutz vor Brute-Force-Angriffen (Account-Lockout, Rate-Limiting)

### 3.7 Privilegierte Accounts
Privilegierte Accounts (Administratoren, Root, Service-Accounts) unterliegen strengeren Authentisierungsanforderungen:
- Verpflichtende MFA
- Separate Accounts für privilegierte Tätigkeiten
- Just-in-Time (JIT) Access wo möglich
- Umfassende Protokollierung

### 3.8 Passwort-Reset und Account-Recovery
Passwort-Reset- und Account-Recovery-Prozesse müssen sicher gestaltet sein und die Identität des Nutzers verifizieren, bevor Zugriff gewährt wird.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Authentisierung und Passwörter

| Aktivität | CISO | IT-Betrieb | Mitarbeiter | IAM-Team | Security Operations |
|-----------|------|------------|-------------|----------|---------------------|
| Policy-Erstellung | R/A | C | I | C | C |
| MFA-Implementierung | A | R | I | R | C |
| Passwort-Reset | I | R | R | R | I |
| Session-Monitoring | C | C | I | C | R/A |
| Brute-Force-Schutz | A | R | I | C | R |
| Incident Response | R/A | C | I | C | R |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** [TODO] (CISO)
- **IAM-Verantwortlicher:** {{ meta-handbook.it_iam_manager }}
- **Umsetzungsverantwortliche:** IT-Betrieb, IAM-Team
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, Security Operations

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md** - Detaillierte Implementierungsrichtlinie
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access Control Policy
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Cryptography Policy
- `0400_Policy_Incident_Management.md` - Incident Management Policy

### Zugehörige Standards/Baselines
- Passwort-Komplexitätsanforderungen
- MFA-Implementierungsstandard
- Session-Timeout-Konfigurationen
- Privileged Access Management (PAM) Standard

### Zugehörige Prozesse
- Passwort-Reset-Prozess
- Account-Recovery-Prozess
- MFA-Enrollment-Prozess
- Incident Response bei Authentisierungsvorfällen

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- MFA-Adoption-Rate (Ziel: 100% für kritische Systeme)
- Anzahl Passwort-Reset-Anfragen pro Monat
- Anzahl fehlgeschlagener Authentisierungsversuche
- Anzahl Account-Lockouts
- Durchschnittliche Passwort-Stärke (Entropy)
- Anzahl kompromittierter Accounts

### Nachweise und Evidence
- Authentisierungs-Logs und Audit-Trails
- MFA-Enrollment-Status
- Passwort-Policy-Compliance-Reports
- Brute-Force-Detection-Logs
- Incident-Reports bei Authentisierungsvorfällen
- Penetration-Test-Ergebnisse

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Schwache Passwörter:** Erzwungene Passwortänderung, Nachschulung
- **Passwort-Weitergabe:** Verwarnung bis Kündigung
- **MFA-Umgehung:** Sofortige Sperrung, Untersuchung
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet und werden regelmäßig überprüft
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Sicherheitsmaßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md` - Detailed Guideline
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access Control Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.17** - Authentication information
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights review
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-63B** - Digital Identity Guidelines: Authentication and Lifecycle Management
- **NIST SP 800-63-3** - Digital Identity Guidelines
- **BSI TR-02102** - Kryptographische Verfahren: Empfehlungen und Schlüssellängen

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO] (jährlich oder anlassbezogen)

