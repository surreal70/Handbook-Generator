# Richtlinie: Sicherheitsanforderungen im Projektlebenszyklus

**Dokument-ID:** 0690
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0680_Policy_Security_in_Projects.md` und definiert:
- Security-Anforderungen in allen Projektphasen
- Security-Reviews und -Gateways
- Security-by-Design-Prinzipien

**Geltungsbereich:** Alle IT-Projekte bei **{{ meta-organisation.name }}**

## 2. Projektklassifizierung

### 2.1 Projekt-Kategorien

**Kategorie A (Kritisch):**
- Neue Systeme mit vertraulichen Daten
- Internet-facing Anwendungen
- Kritische Infrastruktur
- **Security-Involvement:** Umfassend

**Kategorie B (Hoch):**
- Interne Anwendungen mit sensiblen Daten
- Änderungen an kritischen Systemen
- **Security-Involvement:** Detailliert

**Kategorie C (Standard):**
- Standard-IT-Projekte
- Infrastruktur-Upgrades
- **Security-Involvement:** Standard

**Kategorie D (Niedrig):**
- Kleine Änderungen
- Nicht-kritische Systeme
- **Security-Involvement:** Minimal

### 2.2 Klassifizierungskriterien

**Bewertung:**
- Datenklassifizierung (Vertraulich/Streng Vertraulich = höhere Kategorie)
- Internet-Exposition (Ja = höhere Kategorie)
- Anzahl Nutzer (> 100 = höhere Kategorie)
- Compliance-Anforderungen (DSGVO, PCI-DSS = höhere Kategorie)

## 3. Projektphasen und Security-Aktivitäten

### 3.1 Initiierung

**Security-Aktivitäten:**
- Projekt-Klassifizierung
- Security-Stakeholder identifizieren
- Initiales Security-Budget

**Deliverables:**
- Projekt-Klassifizierung
- Security-Kontaktperson

**Security-Gateway:** Keine (Informativ)

### 3.2 Planung

**Security-Aktivitäten:**
- Security-Anforderungen definieren
- Threat Modeling (Kategorie A/B)
- Datenschutz-Folgenabschätzung (DSFA) bei Bedarf
- Security-Architektur-Review
- Security-Testing-Plan

**Deliverables:**
- Security-Requirements-Dokument
- Threat Model (Kategorie A/B)
- DSFA (falls erforderlich)
- Security-Test-Plan

**Security-Gateway 1:**
- **Kategorie A/B:** Verpflichtend
- **Genehmiger:** CISO oder Security-Architekt
- **Kriterien:** Security-Requirements vollständig, Threat Model akzeptabel

### 3.3 Design

**Security-Aktivitäten:**
- Security-Architecture-Review
- Secure-Design-Patterns anwenden
- Authentifizierung/Autorisierung-Design
- Verschlüsselungs-Design
- Logging/Monitoring-Design

**Deliverables:**
- Security-Architecture-Dokument
- Data Flow Diagrams
- Authentication/Authorization-Design

**Security-Gateway 2:**
- **Kategorie A:** Verpflichtend
- **Genehmiger:** CISO und Security-Architekt
- **Kriterien:** Security-Architecture akzeptabel, keine kritischen Schwachstellen im Design

### 3.4 Entwicklung/Beschaffung

**Security-Aktivitäten (Entwicklung):**
- Secure Coding Standards befolgen
- Code-Reviews (inkl. Security-Review)
- SAST (Static Application Security Testing)
- Dependency-Scanning
- Secrets-Management

**Security-Aktivitäten (Beschaffung):**
- Vendor-Security-Assessment
- Vertragsprüfung (Security-Klauseln)
- Auftragsverarbeitungsvertrag (AVV) bei Bedarf

**Deliverables:**
- Code-Review-Berichte
- SAST-Berichte
- Vendor-Assessment (bei Beschaffung)

**Details:** Siehe `0390_Richtlinie_Secure_SDLC` und `0470_Richtlinie_Third_Party_Risk_Assessment`

### 3.5 Testing

**Security-Testing:**
- DAST (Dynamic Application Security Testing)
- Penetration-Testing (Kategorie A/B)
- Security-Test-Cases
- Vulnerability-Scanning

**Deliverables:**
- DAST-Berichte
- Penetration-Test-Bericht (Kategorie A/B)
- Security-Test-Ergebnisse

**Security-Gateway 3:**
- **Kategorie A/B:** Verpflichtend
- **Genehmiger:** CISO
- **Kriterien:** Keine kritischen/hohen Schwachstellen, alle Security-Tests bestanden

### 3.6 Deployment

**Security-Aktivitäten:**
- Security-Configuration-Review
- Hardening gemäß Baseline
- Firewall-Regeln konfigurieren
- Monitoring/Alerting einrichten
- Backup konfigurieren

**Deliverables:**
- Security-Configuration-Checkliste
- Firewall-Regeln-Dokumentation
- Monitoring-Setup-Dokumentation

**Security-Gateway 4 (Go-Live):**
- **Kategorie A/B:** Verpflichtend
- **Genehmiger:** CISO
- **Kriterien:** Security-Configuration korrekt, Monitoring aktiv, keine offenen kritischen Findings

### 3.7 Betrieb und Wartung

**Security-Aktivitäten:**
- Regelmäßige Vulnerability-Scans
- Patch-Management
- Security-Incident-Monitoring
- Jährlicher Security-Review (Kategorie A)

**Deliverables:**
- Vulnerability-Scan-Berichte
- Patch-Compliance-Berichte
- Incident-Reports

### 3.8 Außerbetriebnahme

**Security-Aktivitäten:**
- Daten-Backup (falls erforderlich)
- Sichere Daten-Löschung
- Zugriffe widerrufen
- Firewall-Regeln entfernen
- Dokumentation archivieren

**Deliverables:**
- Löschprotokoll
- Decommissioning-Checkliste

## 4. Security-by-Design-Prinzipien

### 4.1 Least Privilege

**Prinzip:** Minimale erforderliche Berechtigungen

**Umsetzung:**
- Rollenbasierte Zugriffskontrolle (RBAC)
- Keine Default-Admin-Accounts
- Just-in-Time (JIT) Access für privilegierte Operationen

### 4.2 Defense in Depth

**Prinzip:** Mehrere Sicherheitsschichten

**Umsetzung:**
- Netzwerk-Segmentierung
- Firewall + IDS/IPS
- Endpoint-Protection + EDR
- Application-Security + WAF

### 4.3 Fail Secure

**Prinzip:** Bei Fehler in sicheren Zustand

**Umsetzung:**
- Default Deny (Firewall, Zugriffskontrolle)
- Fehler führen zu Zugriffsverweigerung (nicht Zugriff)
- Graceful Degradation

### 4.4 Privacy by Design

**Prinzip:** Datenschutz von Anfang an

**Umsetzung:**
- Datenminimierung
- Zweckbindung
- Verschlüsselung
- Anonymisierung/Pseudonymisierung

**Details:** Siehe `0570_Richtlinie_Datenschutz_Anforderungen`

## 5. Security-Requirements

### 5.1 Funktionale Security-Requirements

**Authentifizierung:**
- Multi-Faktor-Authentifizierung (MFA) für externe Zugriffe
- Starke Passwörter oder Zertifikate
- Session-Management

**Autorisierung:**
- Rollenbasierte Zugriffskontrolle (RBAC)
- Least Privilege
- Segregation of Duties

**Verschlüsselung:**
- TLS 1.2+ für Datenübertragung
- AES-256 für Daten in Ruhe
- Sichere Schlüsselverwaltung

**Logging:**
- Authentifizierungs-Events
- Zugriffe auf vertrauliche Daten
- Administrative Aktionen
- Fehler und Exceptions

### 5.2 Nicht-funktionale Security-Requirements

**Performance:**
- Security-Kontrollen dürfen Performance nicht signifikant beeinträchtigen (< 10%)

**Verfügbarkeit:**
- Security-Kontrollen hochverfügbar
- Failover-Mechanismen

**Wartbarkeit:**
- Security-Konfiguration dokumentiert
- Automatisierte Security-Tests

## 6. Threat Modeling

### 6.1 Methodik

**STRIDE:**
- **S**poofing (Identitätsfälschung)
- **T**ampering (Manipulation)
- **R**epudiation (Abstreitbarkeit)
- **I**nformation Disclosure (Informationspreisgabe)
- **D**enial of Service (Dienstverweigerung)
- **E**levation of Privilege (Rechteausweitung)

### 6.2 Prozess

**Schritte:**
1. System-Architektur dokumentieren (Data Flow Diagrams)
2. Bedrohungen identifizieren (STRIDE)
3. Bedrohungen bewerten (Risiko)
4. Mitigationsmaßnahmen definieren
5. Dokumentation

**Tool:** {{ meta.security.threat_modeling_tool }} (z.B. Microsoft Threat Modeling Tool)

## 7. Security-Testing

### 7.1 Test-Typen

**SAST (Static Application Security Testing):**
- Während Entwicklung
- Automatisiert in CI/CD
- Fokus: Code-Schwachstellen

**DAST (Dynamic Application Security Testing):**
- Während Testing-Phase
- Automatisiert oder manuell
- Fokus: Laufzeit-Schwachstellen

**Penetration-Testing:**
- Vor Go-Live (Kategorie A/B)
- Manuell durch Experten
- Fokus: Realistische Angriffs-Szenarien

**Details:** Siehe `0390_Richtlinie_Secure_SDLC`

### 7.2 Remediation

**Prozess:**
1. Findings priorisieren (nach CVSS)
2. Remediation-Plan erstellen
3. Fixes implementieren
4. Re-Test
5. Dokumentation

**SLA:**
- Critical: Vor Go-Live
- High: Vor Go-Live oder mit Kompensationskontrollen
- Medium: Innerhalb 30 Tage nach Go-Live
- Low: Innerhalb 90 Tage nach Go-Live

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Security-Gateway-Compliance (Kategorie A/B) | 100% |
| Penetration-Test vor Go-Live (Kategorie A/B) | 100% |
| Kritische Findings vor Go-Live | 0 |
| Security-Requirements-Vollständigkeit | 100% |

### 8.2 Audit-Nachweise

- Security-Requirements-Dokumente
- Threat Models
- Security-Test-Berichte
- Security-Gateway-Genehmigungen
- DSFA (falls erforderlich)

## 9. Referenzen

### Interne Dokumente
- `0680_Policy_Security_in_Projects.md`
- `0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md`
- `0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md`
- `0570_Richtlinie_Datenschutz_Anforderungen_und_Datenverarbeitung.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.8** - Information security in project management
- **NIST SP 800-64** - Security Considerations in the System Development Life Cycle
- **OWASP SAMM** - Software Assurance Maturity Model

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

