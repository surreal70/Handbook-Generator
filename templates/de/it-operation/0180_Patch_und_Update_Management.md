# Patch und Update Management

**Dokument-ID:** [FRAMEWORK]-0180
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

## Zweck und Geltungsbereich

Dieses Dokument beschreibt die Patch- und Update-Management-Prozesse für {{ meta-organisation.name }}. Es definiert Patch-Kategorien, Zeitpläne, Test- und Rollout-Prozesse sowie Vulnerability-Scanning und Priorisierung zur Sicherstellung der System-Sicherheit und -Stabilität.

**Geltungsbereich:** Alle IT-Systeme, Betriebssysteme, Applikationen und Firmware von {{ meta-organisation.name }}

**Verantwortlich:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})

## Patch-Management-Grundlagen

### Ziele

**Primäre Ziele:**
- **Sicherheit:** Schließen von Sicherheitslücken
- **Stabilität:** Behebung von Bugs und Fehlern
- **Compliance:** Erfüllung regulatorischer Anforderungen
- **Performance:** Optimierung und neue Features
- **Kompatibilität:** Unterstützung neuer Technologien

### Patch-Kategorien

#### Security Patches (Sicherheits-Updates)

**Beschreibung:** Patches, die Sicherheitslücken schließen

**Priorität:** Kritisch bis Hoch

**Beispiele:**
- CVE-behaftete Vulnerabilities
- Zero-Day-Exploits
- Kritische Sicherheitslücken

**SLA:**
- **Critical (CVSS 9.0-10.0):** 7 Tage
- **High (CVSS 7.0-8.9):** 30 Tage
- **Medium (CVSS 4.0-6.9):** 90 Tage
- **Low (CVSS 0.1-3.9):** 180 Tage

#### Feature Updates (Funktions-Updates)

**Beschreibung:** Updates mit neuen Funktionen und Verbesserungen

**Priorität:** Mittel

**Beispiele:**
- Neue Features
- Performance-Verbesserungen
- UI/UX-Verbesserungen

**SLA:** Nach Bedarf, geplant in Wartungsfenstern

#### Bugfix Patches (Fehlerbehebungen)

**Beschreibung:** Patches zur Behebung von Bugs ohne Sicherheitsrelevanz

**Priorität:** Niedrig bis Mittel

**Beispiele:**
- Funktionale Fehler
- Performance-Probleme
- Kompatibilitäts-Probleme

**SLA:** 90 Tage oder nach Bedarf

#### Firmware Updates

**Beschreibung:** Updates für Hardware-Firmware

**Priorität:** Mittel bis Hoch

**Beispiele:**
- BIOS/UEFI-Updates
- Storage-Controller-Firmware
- Netzwerk-Equipment-Firmware

**SLA:** Nach Herstellerempfehlung, geplant

### Patch-Quellen

| System-Typ | Patch-Quelle | Update-Mechanismus |
|---|---|---|
| **Windows** | Windows Update, WSUS | Automatisch/Manuell |
| **Linux (RHEL/CentOS)** | Red Hat Network, YUM | yum update |
| **Linux (Ubuntu/Debian)** | Ubuntu Repositories, APT | apt update && apt upgrade |
| **VMware** | VMware Update Manager | VUM |
| **Applikationen** | Vendor-Websites, Package-Manager | Manuell/Automatisch |
| **Firmware** | Vendor-Support-Sites | Manuell |
| **Cloud-Services** | Provider-Managed | Automatisch |

## Patch-Management-Prozess

### Prozess-Übersicht

```
┌─────────────────┐
│ Vulnerability   │
│ Identification  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Assessment      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Acquisition     │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Testing         │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Deployment      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Verification    │
│ & Reporting     │
└─────────────────┘
```

### 1. Vulnerability Identification

**Identifikations-Quellen:**
- **Vulnerability-Scanner:** {{ meta-handbook.vulnerability_scanner }}
- **Vendor-Advisories:** Microsoft, Red Hat, VMware, etc.
- **Security-Mailinglists:** CERT, US-CERT, vendor-specific
- **Threat-Intelligence:** {{ meta-handbook.threat_intelligence_source }}
- **SIEM-Alerts:** {{ meta-handbook.siem_system }}

**Aktivitäten:**
- Vulnerability-Scans durchführen (wöchentlich)
- Vendor-Advisories überwachen (täglich)
- CVE-Datenbank prüfen
- Betroffene Systeme identifizieren
- Patch-Verfügbarkeit prüfen

**Verantwortlich:** Security-Operations-Team

### 2. Patch Assessment

**Bewertungs-Kriterien:**

| Kriterium | Bewertung |
|---|---|
| **CVSS-Score** | 0.0 - 10.0 |
| **Exploit-Verfügbarkeit** | Ja/Nein |
| **Asset-Kritikalität** | Kritisch/Wichtig/Standard |
| **Exposure** | Internet-facing/Internal |
| **Vendor-Empfehlung** | Sofort/Geplant/Optional |

**Risiko-Matrix:**

|  | **Internet-facing** | **Internal** |
|---|---|---|
| **Critical (CVSS 9-10)** | Sofort (7 Tage) | Hoch (14 Tage) |
| **High (CVSS 7-8.9)** | Hoch (14 Tage) | Mittel (30 Tage) |
| **Medium (CVSS 4-6.9)** | Mittel (30 Tage) | Niedrig (90 Tage) |
| **Low (CVSS 0-3.9)** | Niedrig (90 Tage) | Sehr niedrig (180 Tage) |

**Impact-Assessment:**
- Welche Systeme sind betroffen?
- Welche Business-Prozesse sind abhängig?
- Ist ein Reboot erforderlich?
- Gibt es bekannte Kompatibilitäts-Probleme?
- Welches Wartungsfenster ist verfügbar?

**Entscheidung:**
- **Patch:** Patch installieren
- **Defer:** Patch verschieben (mit Begründung)
- **Reject:** Patch nicht installieren (mit Begründung)
- **Workaround:** Alternative Mitigation

**Verantwortlich:** Patch-Management-Team

### 3. Patch Acquisition

**Beschaffungs-Aktivitäten:**
- Patch von Vendor-Quelle herunterladen
- Patch-Integrität verifizieren (Checksums, Signaturen)
- Patch in Patch-Repository speichern
- Patch-Metadaten dokumentieren

**Patch-Repository:** {{ meta-handbook.patch_repository }}

**Dokumentation:**
- Patch-ID
- Vendor
- Release-Date
- CVE-IDs
- Betroffene Systeme
- Installations-Anweisungen

**Verantwortlich:** Patch-Management-Team

### 4. Patch Testing

**Test-Umgebungen:**

| Umgebung | Zweck | Systeme |
|---|---|---|
| **Dev** | Entwickler-Tests | {{ netbox.environment.dev }} |
| **Test** | Funktionale Tests | {{ netbox.environment.test }} |
| **Staging** | Pre-Production-Tests | {{ netbox.environment.staging }} |
| **Production** | Produktiv-Systeme | {{ netbox.environment.production }} |

**Test-Prozess:**

#### Phase 1: Dev-Testing (Optional)

**Dauer:** 1-2 Tage

**Aktivitäten:**
- Patch in Dev-Umgebung installieren
- Basis-Funktionalität testen
- Offensichtliche Probleme identifizieren

#### Phase 2: Test-Testing

**Dauer:** 3-5 Tage

**Aktivitäten:**
- Patch in Test-Umgebung installieren
- Funktionale Tests durchführen
- Performance-Tests durchführen
- Kompatibilitäts-Tests durchführen
- Rollback-Prozedur testen

**Test-Checkliste:**
- [ ] Patch erfolgreich installiert
- [ ] System startet nach Reboot
- [ ] Applikationen starten
- [ ] Basis-Funktionalität funktioniert
- [ ] Performance akzeptabel
- [ ] Keine Error-Logs
- [ ] Rollback erfolgreich getestet

#### Phase 3: Staging-Testing

**Dauer:** 2-3 Tage

**Aktivitäten:**
- Patch in Staging-Umgebung installieren
- Business-Prozess-Tests durchführen
- User-Acceptance-Tests (UAT)
- Last-Tests (falls kritisch)

**Go/No-Go-Entscheidung:**
- Alle Tests bestanden → Go
- Kritische Probleme → No-Go, Patch zurückstellen
- Nicht-kritische Probleme → Go mit Workaround

**Verantwortlich:** QA-Team, Applikations-Owner

**Ausnahmen (Emergency-Patches):**
- Kritische Security-Patches können Test-Phase verkürzen
- Mindestens Basis-Tests in Test-Umgebung
- Erhöhtes Risiko akzeptiert und dokumentiert

### 5. Patch Deployment

**Deployment-Strategien:**

#### Phased Rollout (Standard)

**Beschreibung:** Schrittweise Ausrollung in Phasen

**Phasen:**
1. **Pilot-Gruppe:** 5-10% der Systeme (1-2 Tage)
2. **Phase 1:** 25% der Systeme (2-3 Tage)
3. **Phase 2:** 50% der Systeme (2-3 Tage)
4. **Phase 3:** Alle verbleibenden Systeme

**Vorteile:**
- Risiko-Minimierung
- Frühe Problem-Erkennung
- Kontrollierte Ausrollung

**Anwendung:** Standard-Patches, Feature-Updates

#### Big Bang (Alle auf einmal)

**Beschreibung:** Alle Systeme gleichzeitig patchen

**Vorteile:**
- Schnelle Ausrollung
- Einfache Koordination

**Nachteile:**
- Hohes Risiko
- Große Impact bei Problemen

**Anwendung:** Nur für unkritische Systeme oder in Notfällen

#### Rolling Update

**Beschreibung:** Systeme nacheinander patchen (z.B. in Clustern)

**Vorteile:**
- Keine Downtime
- Kontinuierliche Verfügbarkeit

**Anwendung:** Hochverfügbare Systeme, Load-Balanced-Cluster

**Deployment-Methoden:**

| Methode | Tool | Anwendung |
|---|---|---|
| **Automatisch** | WSUS, SCCM, Ansible | Standard-Patches |
| **Semi-Automatisch** | Patch-Management-Tool | Geplante Patches |
| **Manuell** | Remote-Session | Kritische Systeme, Firmware |

**Deployment-Zeitfenster:**

| System-Tier | Wartungsfenster | Frequenz |
|---|---|---|
| **Tier 0 (Kritisch)** | Sonntag 02:00-06:00 | Monatlich |
| **Tier 1 (Wichtig)** | Samstag 22:00-02:00 | Monatlich |
| **Tier 2 (Standard)** | Mittwoch 20:00-22:00 | Monatlich |
| **Tier 3 (Unkritisch)** | Jederzeit | Nach Bedarf |

**Deployment-Checkliste:**
- [ ] Change-Ticket erstellt und genehmigt
- [ ] Stakeholder informiert
- [ ] Backup erstellt
- [ ] Rollback-Plan bereit
- [ ] Monitoring aktiviert
- [ ] On-Call-Team verfügbar

**Verantwortlich:** IT-Operations-Team

### 6. Verification & Reporting

**Verifikations-Aktivitäten:**
- Patch-Installation bestätigen
- System-Funktionalität prüfen
- Performance-Metriken überwachen
- Error-Logs prüfen
- Vulnerability-Scan wiederholen

**Verifikations-Checkliste:**
- [ ] Patch auf allen Ziel-Systemen installiert
- [ ] Systeme laufen stabil
- [ ] Keine kritischen Errors
- [ ] Performance normal
- [ ] Vulnerability geschlossen (Scan)

**Reporting:**
- Patch-Status-Report
- Erfolgs-/Fehler-Rate
- Offene Patches
- Compliance-Status

**Verantwortlich:** Patch-Management-Team

## Patch-Zeitpläne

### Monatlicher Patch-Zyklus

**Microsoft Patch Tuesday:**
- **Patch-Release:** 2. Dienstag im Monat
- **Assessment:** Dienstag-Mittwoch
- **Testing:** Mittwoch-Freitag (Woche 1)
- **Staging:** Montag-Mittwoch (Woche 2)
- **Production-Deployment:** Samstag/Sonntag (Woche 2-3)

**Linux-Patches:**
- **Assessment:** Wöchentlich (Montag)
- **Testing:** Dienstag-Donnerstag
- **Deployment:** Samstag (monatlich)

**Applikations-Patches:**
- **Assessment:** Bei Vendor-Release
- **Testing:** 1 Woche
- **Deployment:** Nächstes Wartungsfenster

### Emergency-Patches

**Trigger:**
- Critical-Vulnerability (CVSS > 9.0)
- Aktive Exploits in the Wild
- Zero-Day-Vulnerabilities
- Vendor-Empfehlung "Sofort"

**Prozess:**
- **Assessment:** Sofort (< 4 Stunden)
- **Testing:** Minimal (< 8 Stunden)
- **Deployment:** Sofort (< 24 Stunden)

**Genehmigung:** CIO oder CISO

**Kommunikation:** Alle Stakeholder sofort informieren

### Patch-Kalender

| Woche | Montag | Dienstag | Mittwoch | Donnerstag | Freitag | Samstag | Sonntag |
|---|---|---|---|---|---|---|---|
| **Woche 1** | Assessment | Testing | Testing | Testing | Testing | - | - |
| **Woche 2** | Staging | Staging | Staging | Go/No-Go | - | Tier 1 Deploy | Tier 0 Deploy |
| **Woche 3** | Verification | Reporting | Tier 2 Deploy | - | - | - | - |
| **Woche 4** | - | - | - | - | - | - | - |

## Patch-Management-Tools

### Windows-Patch-Management

**Tool:** Windows Server Update Services (WSUS)  
**Server:** {{ netbox.wsus.server }}  
**Management:** {{ netbox.wsus.management_url }}

**Konfiguration:**
- Automatische Synchronisation mit Microsoft Update
- Patch-Approval-Workflow
- Computer-Gruppen nach Tier
- Reporting und Compliance-Dashboard

**Patch-Gruppen:**
- **Pilot:** Test-Systeme
- **Tier-0:** Kritische Produktions-Systeme
- **Tier-1:** Wichtige Produktions-Systeme
- **Tier-2:** Standard-Systeme
- **Tier-3:** Unkritische Systeme

### Linux-Patch-Management

**Tool:** Ansible / Satellite  
**Server:** {{ netbox.ansible.server }}

**Playbooks:**
- `patch-assessment.yml` - Verfügbare Updates prüfen
- `patch-security.yml` - Nur Security-Updates
- `patch-all.yml` - Alle Updates
- `patch-rollback.yml` - Rollback

**Beispiel-Playbook:**
```yaml

- name: Patch Linux Servers
  hosts: linux_servers
  become: yes
  tasks:
    - name: Update package cache
      apt:
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Install security updates
      apt:
        upgrade: safe
        autoremove: yes
      when: ansible_os_family == "Debian"
    
    - name: Check if reboot required
      stat:
        path: /var/run/reboot-required
      register: reboot_required
    
    - name: Reboot if required
      reboot:
        msg: "Reboot for security updates"
      when: reboot_required.stat.exists
```

### VMware-Patch-Management

**Tool:** VMware Update Manager (VUM)  
**Integration:** vCenter {{ netbox.vcenter.server }}

**Baseline-Gruppen:**
- **Critical-Patches:** Kritische Security-Patches
- **Non-Critical-Patches:** Alle anderen Patches
- **Upgrades:** ESXi-Upgrades

**Remediation-Prozess:**
- Baseline-Compliance prüfen
- Hosts in Maintenance-Mode
- Patches installieren
- Hosts rebooten
- Compliance verifizieren

### Vulnerability-Scanner

**Tool:** {{ meta-handbook.vulnerability_scanner }}  
**Scan-Frequenz:** Wöchentlich

**Scan-Profile:**
- **Full-Scan:** Alle Vulnerabilities
- **Patch-Scan:** Nur fehlende Patches
- **Compliance-Scan:** Compliance-Checks

**Integration:** SIEM, Ticketing-System

## Rollback-Prozeduren

### Rollback-Trigger

**Rollback erforderlich bei:**
- Kritische Funktionalität nicht verfügbar
- Performance-Degradation > 20%
- Daten-Korruption
- Sicherheits-Probleme durch Patch
- Business-Prozess-Ausfall

**Rollback-Entscheidung:** IT Operations Manager oder höher

### Rollback-Methoden

#### Windows-Rollback

**Methode 1: Windows-Uninstall**
```powershell
# Patch-Liste anzeigen
Get-HotFix

# Patch deinstallieren
wusa /uninstall /kb:KBXXXXXX /quiet /norestart
```

**Methode 2: System-Restore**
- Restore-Point vor Patch-Installation
- System-Wiederherstellung durchführen

**Methode 3: Backup-Restore**
- VM-Snapshot wiederherstellen
- Bare-Metal-Restore

#### Linux-Rollback

**Methode 1: Package-Downgrade**
```bash
# Ubuntu/Debian
apt-cache policy <package>
apt-get install <package>=<old-version>

# RHEL/CentOS
yum downgrade <package>
```

**Methode 2: Snapshot-Rollback**
- LVM-Snapshot wiederherstellen
- VM-Snapshot wiederherstellen

#### VMware-Rollback

**Methode:** VUM-Rollback
- Baseline-Remediation rückgängig machen
- Vorherige Patch-Version installieren

### Rollback-Prozess

1. **Rollback-Entscheidung treffen**
   - Impact bewerten
   - Stakeholder informieren

2. **Rollback durchführen**
   - Rollback-Methode auswählen
   - Rollback ausführen
   - System neu starten (falls erforderlich)

3. **Verifikation**
   - Funktionalität prüfen
   - Performance prüfen
   - Logs prüfen

4. **Dokumentation**
   - Rollback-Grund dokumentieren
   - Lessons Learned
   - Alternative Lösungen evaluieren

## Compliance und Reporting

### Patch-Compliance-Metriken

| Metrik | Zielwert | Messung |
|---|---|---|
| **Patch Compliance Rate** | > 95% | Gepatchte Systeme / Gesamt-Systeme |
| **Critical Patch SLA** | > 95% | Patches in SLA / Gesamt-Patches |
| **Mean Time to Patch (MTTP)** | < 30 Tage | Durchschnittliche Patch-Dauer |
| **Patch Success Rate** | > 98% | Erfolgreiche Patches / Gesamt-Patches |
| **Rollback Rate** | < 2% | Rollbacks / Gesamt-Patches |

### Patch-Compliance-Dashboard

**Metriken:**
- Patch-Status nach System-Tier
- Offene Critical-Patches
- SLA-Compliance
- Patch-Trends (monatlich)
- Top-10-Vulnerabilities

**Tool:** {{ meta-handbook.patch_dashboard }}

**Zugriff:** IT-Management, Security-Team

### Reporting

**Wöchentliches Patch-Status-Report:**
- Neue Patches verfügbar
- Patches in Testing
- Geplante Deployments
- Offene Critical-Patches

**Monatliches Patch-Compliance-Report:**
- Patch-Compliance-Rate
- SLA-Compliance
- Patch-Statistiken
- Trend-Analysen
- Verbesserungs-Maßnahmen

**Quartalsweises Management-Report:**
- Patch-Management-Strategie-Review
- Risiko-Assessment
- Compliance-Status
- Budget und Ressourcen

**Empfänger:**
- Wöchentlich: IT-Operations-Team
- Monatlich: IT-Management, Security-Team
- Quartalsweise: CIO, CISO, Management

## Ausnahmen und Sonderfälle

### Patch-Ausnahmen

**Gründe für Ausnahmen:**
- Vendor-Support endet (End-of-Life)
- Applikations-Inkompatibilität
- Business-kritische Systeme (Change-Freeze)
- Spezielle Vendor-Anforderungen

**Ausnahme-Prozess:**
1. Ausnahme-Antrag stellen
2. Risiko-Assessment durchführen
3. Kompensations-Maßnahmen definieren
4. Management-Genehmigung einholen
5. Ausnahme dokumentieren
6. Regelmäßig reviewen (quartalsweise)

**Ausnahme-Register:** {{ meta-handbook.exception_register }}

### End-of-Life-Systeme

**Strategie:**
- Migration planen
- Netzwerk-Segmentierung
- Zusätzliche Monitoring
- Kompensations-Kontrollen
- Risiko-Akzeptanz dokumentieren

**EOL-Register:** {{ meta-handbook.eol_register }}

### Legacy-Applikationen

**Herausforderungen:**
- Keine Patches verfügbar
- Inkompatibilität mit neuen OS-Versionen
- Vendor-Support eingestellt

**Mitigations:**
- Virtualisierung/Containerisierung
- Netzwerk-Isolation
- WAF/IPS vor Applikation
- Regelmäßige Vulnerability-Scans
- Migrations-Roadmap

## Rollen und Verantwortlichkeiten

### Patch-Management-Team

**Verantwortlichkeiten:**
- Patch-Prozess-Ownership
- Vulnerability-Assessment
- Patch-Testing-Koordination
- Deployment-Planung
- Reporting

**Team-Lead:** {{ meta-organisation-roles.role_it_operations_manager.name }}

### System-Administratoren

**Verantwortlichkeiten:**
- Patch-Deployment durchführen
- System-Monitoring
- Rollback-Durchführung
- Dokumentation

### Security-Team

**Verantwortlichkeiten:**
- Vulnerability-Scanning
- Risiko-Assessment
- Security-Patch-Priorisierung
- Compliance-Überwachung

**Lead:** {{ meta-organisation-roles.role_ciso.name }}

### Applikations-Owner

**Verantwortlichkeiten:**
- Applikations-Kompatibilität prüfen
- User-Acceptance-Tests
- Go/No-Go-Entscheidung
- Business-Impact-Assessment

### Change-Manager

**Verantwortlichkeiten:**
- Change-Tickets genehmigen
- Change-Kalender verwalten
- Stakeholder-Kommunikation
- Post-Implementation-Review

## Best Practices

### Patch-Management-Best-Practices

1. **Regelmäßige Vulnerability-Scans**
   - Wöchentliche Scans
   - Automatisierte Scans
   - Priorisierung nach Risiko

2. **Test vor Deployment**
   - Immer in Test-Umgebung testen
   - Rollback-Plan bereit haben
   - Dokumentation aktuell halten

3. **Phased Rollout**
   - Pilot-Gruppe zuerst
   - Schrittweise Ausrollung
   - Monitoring während Rollout

4. **Backup vor Patching**
   - Immer Backup erstellen
   - Backup-Integrität prüfen
   - Restore-Prozedur testen

5. **Kommunikation**
   - Stakeholder frühzeitig informieren
   - Status-Updates während Deployment
   - Post-Deployment-Kommunikation

6. **Dokumentation**
   - Patch-Prozess dokumentieren
   - Lessons Learned festhalten
   - Knowledge-Base pflegen

7. **Automatisierung**
   - Patch-Deployment automatisieren
   - Reporting automatisieren
   - Compliance-Checks automatisieren

8. **Kontinuierliche Verbesserung**
   - Prozess regelmäßig reviewen
   - Metriken analysieren
   - Optimierungen umsetzen

## Referenzen

- NIST SP 800-40 Rev. 4 - Guide to Enterprise Patch Management Planning
- ISO/IEC 27002:2013 - Control 12.6.1 (Management of Technical Vulnerabilities)
- CIS Controls v8 - Control 7 (Continuous Vulnerability Management)
- ITIL v4 - Change Enablement Practice
- Vendor-Patch-Dokumentation (Microsoft, Red Hat, VMware)
- CVE Database: https://cve.mitre.org
- NVD Database: https://nvd.nist.gov

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Klassifizierung:** {{ meta-handbook.classification }}  
**Letzte Aktualisierung:** {{ meta-handbook.date }}

