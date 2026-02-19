# Richtlinie: Sicherheitsbaselines, Hardening und Konfigurationsänderungen

**Dokument-ID:** 0550
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

Diese Richtlinie konkretisiert die `0540_Policy_Konfiguration_und_Hardening.md` und definiert:
- Sicherheitsbaselines für verschiedene Systemtypen
- Hardening-Prozesse und -Standards
- Configuration Management und Change Control

**Geltungsbereich:** Alle IT-Systeme bei **{{ meta-organisation.name }}**

## 2. Sicherheitsbaselines

### 2.1 Windows Server

**Baseline-Standard:** CIS Benchmark Level 1

**Kern-Anforderungen:**
- Lokale Administrator-Accounts deaktivieren (außer Break-Glass)
- Windows Firewall aktiviert
- Windows Defender aktiviert
- Automatische Updates aktiviert
- SMBv1 deaktiviert
- PowerShell Logging aktiviert
- Audit-Policies konfiguriert

**Tools:**
- Group Policy Objects (GPOs)
- Microsoft Security Compliance Toolkit
- CIS-CAT Pro

### 2.2 Linux Server

**Baseline-Standard:** CIS Benchmark Level 1

**Kern-Anforderungen:**
- Root-Login über SSH deaktiviert
- SSH Key-based Authentication
- Firewall (iptables/firewalld) aktiviert
- SELinux/AppArmor aktiviert
- Automatische Security-Updates
- Unnötige Services deaktiviert
- Audit-Daemon (auditd) aktiviert

**Tools:**
- Ansible/Puppet für Konfigurationsmanagement
- Lynis für Security-Audits

### 2.3 Netzwerkgeräte

**Baseline-Standard:** Vendor Best Practices + CIS Benchmarks

**Kern-Anforderungen:**
- Default-Passwörter geändert
- SNMP v3 (oder deaktiviert)
- Unused Ports deaktiviert
- Management-Zugriff nur über dediziertes VLAN
- Logging zu SIEM
- NTP konfiguriert

### 2.4 Cloud-Workloads

**Baseline-Standard:** Cloud Security Posture Management (CSPM)

**Azure:**
- Azure Security Benchmark
- Microsoft Defender for Cloud Empfehlungen

**AWS:**
- AWS Foundational Security Best Practices
- CIS AWS Foundations Benchmark

**GCP:**
- CIS Google Cloud Platform Foundation Benchmark

## 3. Hardening-Prozess

### 3.1 Build-Phase

**Golden Images:**
- Vorkonfigurierte, gehärtete Images
- Regelmäßige Updates (monatlich)
- Automatisierte Builds (CI/CD)

**Prozess:**
1. Base-Image (Vendor)
2. Hardening-Scripts anwenden
3. Security-Scan
4. Approval
5. Image-Repository

### 3.2 Deployment-Phase

**Automatisierung:**
- Infrastructure as Code (Terraform, ARM Templates)
- Configuration Management (Ansible, Puppet, Chef)
- Compliance-Checks vor Deployment

**Manuelle Schritte:**
- Nur bei Ausnahmen
- Dokumentation erforderlich
- Post-Deployment-Verification

### 3.3 Maintenance-Phase

**Regelmäßige Reviews:**
- Quartalsweise Configuration-Audits
- Drift-Detection (Abweichungen von Baseline)
- Remediation von Non-Compliance

## 4. Configuration Management

### 4.1 Configuration Management Database (CMDB)

**System:** {{ meta-handbook.itsm_cmdb }}

**Dokumentierte Konfigurationen:**
- System-Typ und -Version
- Installierte Software
- Netzwerk-Konfiguration
- Security-Konfiguration
- Baseline-Version

### 4.2 Configuration Baselines

**Baseline-Versionen:**
- Major-Version: Bei signifikanten Änderungen
- Minor-Version: Bei kleineren Updates
- Patch-Version: Bei Security-Fixes

**Beispiel:** Windows-Server-Baseline v2.1.3

### 4.3 Drift Detection

**Monitoring:**
- Automatische Scans (täglich)
- Vergleich mit Baseline
- Alerts bei Abweichungen

**Tools:**
- Microsoft Defender for Cloud (Azure)
- AWS Config (AWS)
- Chef InSpec, Ansible Tower

**Remediation:**
- Automatische Korrektur (wo möglich)
- Manuelle Korrektur mit Ticket
- Ausnahmen-Prozess (siehe Abschnitt 6)

## 5. Konfigurationsänderungen

### 5.1 Change-Prozess

**Alle Konfigurationsänderungen über Change Management:**
- Change Request (RFC) erstellen
- Security-Impact-Assessment
- Testing in Dev/Test
- CAB-Genehmigung
- Implementation
- Verification

**Details:** Siehe `0370_Richtlinie_Change_Management`

### 5.2 Emergency Changes

**Bei kritischen Security-Fixes:**
- Beschleunigter Prozess
- ECAB-Genehmigung
- Nachträgliche Dokumentation

### 5.3 Configuration Backup

**Vor jeder Änderung:**
- Backup der aktuellen Konfiguration
- Versionierung
- Rollback-Fähigkeit

**Retention:** {{ meta-handbook.retention_config_years }} Jahre

## 6. Ausnahmen und Abweichungen

### 6.1 Ausnahmenprozess

**Antrag:**
- Begründung (Business Justification)
- Risikobewertung
- Kompensationskontrollen
- Zeitliche Befristung

**Genehmigung:**
- CISO-Genehmigung erforderlich
- Dokumentation im Ausnahmen-Register
- Regelmäßiger Review (quartalsweise)

**Details:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`

### 6.2 Legacy-Systeme

**Für Systeme, die Baseline nicht erfüllen können:**
- Kompensationskontrollen implementieren
- Netzwerk-Isolation
- Erhöhtes Monitoring
- Migration-Plan erstellen

## 7. Compliance-Monitoring

### 7.1 Automated Compliance Scanning

**Tools:**
- **Windows:** Microsoft Security Compliance Toolkit, CIS-CAT
- **Linux:** Lynis, OpenSCAP
- **Cloud:** Cloud Security Posture Management (CSPM)
- **Network:** Nessus, Qualys

**Frequenz:**
- Kritische Systeme: Wöchentlich
- Standard-Systeme: Monatlich

### 7.2 Compliance-Reporting

**Monatlicher Compliance-Report:**
- Compliance-Rate pro Baseline
- Top Non-Compliance-Items
- Trend-Analyse
- Remediation-Status

**Ziel:** > 95% Compliance

### 7.3 Audit-Nachweise

- Baseline-Dokumente
- Compliance-Scan-Berichte
- Ausnahmen-Register
- Remediation-Tickets

## 8. Hardening-Standards

### 8.1 Referenz-Standards

**Primär:**
- CIS Benchmarks (Center for Internet Security)
- DISA STIGs (Defense Information Systems Agency Security Technical Implementation Guides)
- Vendor Best Practices

**Sekundär:**
- NIST Cybersecurity Framework
- BSI IT-Grundschutz

### 8.2 Baseline-Dokumentation

**Für jede Baseline:**
- Scope und Anwendungsbereich
- Konfigurationseinstellungen (detailliert)
- Begründung für jede Einstellung
- Test-Prozeduren
- Rollback-Prozeduren

**Speicherort:** {{ meta-handbook.documentation_baseline_repo }}

## 9. Compliance und Audit

### 9.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Baseline-Compliance-Rate | > 95% |
| Drift-Remediation-Zeit | < 7 Tage |
| Golden-Image-Aktualität | < 30 Tage |
| Ausnahmen mit aktuellem Review | 100% |

### 9.2 Audit-Nachweise

- Baseline-Dokumente
- Compliance-Scan-Berichte
- Configuration-Backups
- Change-Records

## 10. Referenzen

### Interne Dokumente
- `0540_Policy_Konfiguration_und_Hardening.md`
- `0370_Richtlinie_Change_Management_mit_Sicherheitsfreigaben.md`
- `0640_Policy_Ausnahmen_und_Risk_Waivers.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **CIS Benchmarks** - https://www.cisecurity.org/cis-benchmarks/
- **NIST SP 800-70** - Security Configuration Checklists

**Genehmigt durch:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

