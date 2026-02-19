# Policy: Zugriffssteuerung und Identitätsmanagement

**Dokument-ID:** 0220
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
This policy establishes the principles for access control and identity management.
It ensures that access to information and systems is granted based on business need
and the principle of least privilege. Customize based on your organization's
access control requirements and IAM maturity.

ISO 27001:2022 Annex A Reference: A.5.15, A.5.16, A.5.17, A.5.18
-->

## 1. Zweck

Diese Policy definiert die Grundsätze für Zugriffssteuerung und Identitätsmanagement (IAM) der **{{ meta-organisation.name }}**. Sie stellt sicher, dass der Zugriff auf Informationen und IT-Systeme ausschließlich autorisierten Personen gewährt wird und auf Basis des Need-to-Know-Prinzips und der geringsten Privilegien (Least Privilege) erfolgt.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Systeme:** Alle IT-Systeme, Anwendungen, Datenbanken, Netzwerke, Cloud-Services
- **Personen:** Alle Mitarbeiter, Auftragnehmer, Lieferanten und Dritte mit Zugang zu IT-Ressourcen
- **Zugriffsmethoden:** Lokaler Zugriff, Remote-Zugriff, privilegierter Zugriff, API-Zugriff
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Least Privilege (Geringste Privilegien)
Nutzer erhalten nur die minimalen Zugriffsrechte, die zur Erfüllung ihrer Aufgaben erforderlich sind. Privilegierte Zugriffe werden restriktiv vergeben und regelmäßig überprüft.

### 3.2 Need-to-Know-Prinzip
Der Zugriff auf Informationen wird nur gewährt, wenn eine geschäftliche Notwendigkeit besteht. Zugriffe werden auf Basis von Rollen und Verantwortlichkeiten vergeben.

### 3.3 Identitätslebenszyklus (Joiner-Mover-Leaver)
Identitäten werden über den gesamten Lebenszyklus verwaltet:
- **Joiner:** Zugriffsrechte werden bei Eintritt basierend auf Rolle und Funktion vergeben
- **Mover:** Zugriffsrechte werden bei Rollenwechsel angepasst (alte Rechte entziehen, neue gewähren)
- **Leaver:** Alle Zugriffsrechte werden bei Austritt unverzüglich entzogen

### 3.4 Rollenbasierte Zugriffskontrolle (RBAC)
Zugriffsrechte werden primär über Rollen und Gruppen vergeben, nicht über individuelle Berechtigungen. Rollenmodelle werden regelmäßig überprüft und aktualisiert.

### 3.5 Segregation of Duties (Funktionstrennung)
Kritische Funktionen werden so aufgeteilt, dass keine einzelne Person alle Schritte eines sensiblen Prozesses durchführen kann. Dies verhindert Betrug und Fehler.

### 3.6 Regelmäßige Rezertifizierung
Zugriffsrechte werden regelmäßig (mindestens jährlich) überprüft und rezertifiziert. Nicht mehr benötigte Rechte werden entzogen.

### 3.7 Privileged Access Management (PAM)
Privilegierte Accounts (Administratoren, Root, Service-Accounts) unterliegen besonderen Kontrollen:
- Separate Accounts für privilegierte Tätigkeiten
- Just-in-Time (JIT) Access wo möglich
- Umfassende Protokollierung und Überwachung

### 3.8 Zugriffsgenehmigung und Dokumentation
Alle Zugriffsvergaben müssen durch den Ressourcen-Owner genehmigt und dokumentiert werden. Zugriffsentscheidungen sind nachvollziehbar und auditierbar.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Zugriffssteuerung und IAM

| Aktivität | CISO | IT-Betrieb | Ressourcen-Owner | HR | Mitarbeiter |
|-----------|------|------------|------------------|-----|-------------|
| Policy-Erstellung | R/A | C | C | C | I |
| IAM-System-Betrieb | C | R/A | I | I | I |
| Zugriff beantragen | I | I | C | I | R |
| Zugriff genehmigen | C | I | R/A | C | I |
| Zugriff provisionieren | I | R | I | I | I |
| Rezertifizierung | C | C | R/A | C | I |
| Zugriff entziehen (Leaver) | C | R | I | R/A | I |
| Monitoring und Audits | R/A | C | C | I | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO)
- **IAM-Verantwortlicher:** {{ meta-handbook.it_iam_manager }}
- **Ressourcen-Owner:** Fachbereichsleiter, Systemverantwortliche
- **Umsetzungsverantwortliche:** IT-Betrieb, HR
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md** - Detaillierte IAM-Richtlinie
- `0240_Policy_Authentisierung_und_Passwoerter.md` - Authentication Policy
- `0520_Policy_HR_Security.md` - HR Security Policy
- `0640_Policy_Ausnahmen_und_Risk_Waivers.md` - Exception Policy

### Zugehörige Standards/Baselines
- Rollenmodell und RBAC-Matrix
- Privileged Access Management (PAM) Standard
- Rezertifizierungsprozess
- Service-Account-Management

### Zugehörige Prozesse
- Joiner-Mover-Leaver-Prozess
- Zugriffsgenehmigungsprozess
- Rezertifizierungsprozess
- Incident Response bei unbefugtem Zugriff

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl offener Zugriffsanträge und durchschnittliche Bearbeitungszeit
- Rezertifizierungsrate (Ziel: 100% jährlich)
- Anzahl nicht rezertifizierter Accounts
- Anzahl privilegierter Accounts und deren Nutzungshäufigkeit
- Anzahl Verstöße gegen Least Privilege
- Durchschnittliche Zeit zur Deaktivierung von Leaver-Accounts (Ziel: < 1 Tag)

### Nachweise und Evidence
- IAM-System-Logs und Audit-Trails
- Zugriffsgenehmigungen und Anträge
- Rezertifizierungsnachweise
- Joiner-Mover-Leaver-Dokumentation
- Privileged Access Logs
- Audit-Berichte zu Zugriffsrechten

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Unbefugte Zugriffsvergabe:** Sofortige Sperrung, Untersuchung, ggf. Disziplinarmaßnahmen
- **Nicht rezertifizierte Accounts:** Automatische Deaktivierung nach Frist
- **Missbrauch privilegierter Zugriffe:** Sofortige Sperrung, arbeitsrechtliche Konsequenzen
- **Weitergabe von Zugangsdaten:** Verwarnung bis Kündigung

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Ressourcen-Owner genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet und werden regelmäßig überprüft

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md` - Detailed IAM Guideline
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md` - HR Security Guideline

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.15** - Identity management
- **ISO/IEC 27001:2022 Annex A.5.16** - Access rights
- **ISO/IEC 27001:2022 Annex A.5.17** - Authentication information
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights review
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-63** - Digital Identity Guidelines

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

