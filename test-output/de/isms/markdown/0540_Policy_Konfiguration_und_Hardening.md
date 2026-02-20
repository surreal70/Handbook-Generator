# Policy: Konfiguration und Hardening

**Dokument-ID:** 0540
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

Diese Policy definiert die Grundsätze für sichere Konfiguration und System-Hardening der **AdminSend GmbH**. Sie stellt sicher, dass IT-Systeme sicher konfiguriert und gegen Angriffe gehärtet werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Systeme:** Alle Server, Workstations, Netzwerkgeräte, Anwendungen, Cloud-Ressourcen
- **Umgebungen:** Produktion, Test, Entwicklung
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Security Baselines
Für alle Systemtypen existieren Security Baselines, die Mindestanforderungen an sichere Konfiguration definieren. Baselines basieren auf anerkannten Standards (CIS Benchmarks, BSI, Vendor Best Practices).

### 3.2 Secure by Default
Systeme werden mit sicheren Standardkonfigurationen deployed. Unsichere Default-Einstellungen werden geändert, unnötige Features deaktiviert.

### 3.3 Hardening-Maßnahmen
Systeme werden gehärtet:
- Entfernung unnötiger Software und Services
- Deaktivierung nicht benötigter Ports und Protokolle
- Änderung von Default-Credentials
- Minimierung der Angriffsfläche

### 3.4 Configuration Management
Konfigurationen werden zentral verwaltet und versioniert (Infrastructure as Code, Configuration Management Tools). Änderungen erfolgen kontrolliert über Change Management.

### 3.5 Configuration Drift Detection
Abweichungen von Security Baselines (Configuration Drift) werden automatisch erkannt und gemeldet. Nicht genehmigte Änderungen werden zurückgesetzt.

### 3.6 Least Functionality
Systeme werden nach dem Prinzip der geringsten Funktionalität konfiguriert. Nur erforderliche Funktionen und Services sind aktiviert.

### 3.7 Secure Configuration Reviews
Konfigurationen werden regelmäßig überprüft:
- **Kritische Systeme:** Quartalsweise
- **Wichtige Systeme:** Halbjährlich
- **Standard-Systeme:** Jährlich

### 3.8 Dokumentation
Alle Konfigurationsabweichungen von Baselines werden dokumentiert und begründet. Dokumentation ist aktuell und nachvollziehbar.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Konfiguration und Hardening

| Aktivität | CISO | IT-Betrieb | System Owner | Security Team | Change Management |
|-----------|------|------------|--------------|---------------|-------------------|
| Policy-Erstellung | R/A | C | C | C | I |
| Baseline-Erstellung | A | C | C | R | I |
| System-Hardening | C | R/A | C | C | I |
| Configuration Management | C | R/A | C | I | C |
| Drift Detection | A | C | I | R | I |
| Configuration Reviews | A | C | R | R | I |
| Compliance-Prüfung | R/A | C | C | C | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** [TODO] (CISO)
- **Configuration Manager:** {{ meta-handbook.it_config_manager }}
- **Security Architect:** {{ meta-handbook.security_architect }}
- **Umsetzungsverantwortliche:** IT-Betrieb, System Owner
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0550_Richtlinie_Sicherheitsbaselines_Hardening_und_Konfig_Aenderungen.md** - Detaillierte Implementierungsrichtlinie
- `0360_Policy_Change_und_Release_Management.md` - Change Management Policy
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Vulnerability Management Policy

### Zugehörige Standards/Baselines
- Security Baselines (Windows, Linux, Network Devices, Cloud)
- Hardening Guides
- Configuration Management Standards
- Drift Detection Rules

### Zugehörige Prozesse
- Configuration Management Prozess
- Hardening Prozess
- Configuration Review Prozess
- Drift Remediation Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Baseline Compliance Rate (Ziel: 95%)
- Anzahl Configuration Drift Findings
- Durchschnittliche Zeit zur Drift-Remediation
- Configuration Review Completion Rate (Ziel: 100%)
- Anzahl Systeme mit Default-Credentials (Ziel: 0)
- Hardening Coverage (Ziel: 100% kritischer Systeme)

### Nachweise und Evidence
- Security Baselines Dokumentation
- Configuration Management Logs
- Drift Detection Reports
- Configuration Review Reports
- Hardening Checklists
- Audit-Berichte zu Configuration Compliance

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nicht gehärtete Systeme:** Sofortige Remediation, Produktionssperre
- **Configuration Drift:** Remediation nach Priorität
- **Default-Credentials:** Sofortige Änderung, Incident Response
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und System Owner genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Sicherheitsmaßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0550_Richtlinie_Sicherheitsbaselines_Hardening_und_Konfig_Aenderungen.md` - Detailed Guideline
- `0360_Policy_Change_und_Release_Management.md` - Change Management Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **ISO/IEC 27001:2022 Annex A.8.10** - Information deletion
- **CIS Benchmarks** - Center for Internet Security Configuration Benchmarks
- **NIST SP 800-123** - Guide to General Server Security
- **BSI IT-Grundschutz** - Sicherheitsanforderungen

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO] (jährlich oder anlassbezogen)

