# Policy: Backup und Wiederherstellung

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for backup and recovery operations.
It ensures that critical data and systems can be restored in case of data loss,
corruption, or disaster. Customize based on your organization's RPO/RTO
requirements and backup infrastructure.

ISO 27001:2022 Annex A Reference: A.8.13
-->

**Dokument-ID:** 0420  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.8.13 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Grundsätze für Backup und Wiederherstellung der **{{ meta.organization.name }}**. Sie stellt sicher, dass kritische Daten und Systeme im Falle von Datenverlust, Korruption oder Katastrophen wiederhergestellt werden können.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta.organization.name }}
- **Systeme:** Alle IT-Systeme, Datenbanken, Anwendungen, Dateisysteme, VMs, Cloud-Ressourcen
- **Daten:** Alle geschäftskritischen und personenbezogenen Daten
- **Backup-Typen:** Full, Incremental, Differential, Snapshot, Cloud Backup
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Backup-Strategie basierend auf RPO/RTO
Backup-Strategien werden basierend auf Recovery Point Objective (RPO) und Recovery Time Objective (RTO) definiert:
- **Kritische Systeme:** RPO < 1 Stunde, RTO < 4 Stunden
- **Wichtige Systeme:** RPO < 24 Stunden, RTO < 24 Stunden
- **Standard-Systeme:** RPO < 7 Tage, RTO < 72 Stunden

### 3.2 3-2-1 Backup-Regel
Backups folgen der 3-2-1-Regel:
- **3** Kopien der Daten (Original + 2 Backups)
- **2** verschiedene Speichermedien/Technologien
- **1** Kopie offsite/offline (Air-Gapped oder geografisch getrennt)

### 3.3 Verschlüsselte Backups
Alle Backups werden verschlüsselt gespeichert (at rest) und übertragen (in transit). Verschlüsselungsschlüssel werden sicher verwaltet und getrennt von Backups gespeichert.

### 3.4 Regelmäßige Backup-Tests
Backups werden regelmäßig getestet, um die Wiederherstellbarkeit sicherzustellen:
- **Kritische Systeme:** Monatliche Restore-Tests
- **Wichtige Systeme:** Quartalsweise Restore-Tests
- **Standard-Systeme:** Jährliche Restore-Tests

### 3.5 Immutable Backups
Kritische Backups werden als immutable (unveränderlich) gespeichert, um Schutz vor Ransomware und versehentlicher Löschung zu bieten.

### 3.6 Backup-Monitoring und Alerting
Backup-Jobs werden kontinuierlich überwacht. Fehlgeschlagene Backups lösen sofortige Alerts aus und werden priorisiert behoben.

### 3.7 Retention und Aufbewahrung
Backups werden entsprechend gesetzlicher, regulatorischer und geschäftlicher Anforderungen aufbewahrt:
- **Tägliche Backups:** 30 Tage
- **Wöchentliche Backups:** 12 Wochen
- **Monatliche Backups:** 12 Monate
- **Jährliche Backups:** 7 Jahre (oder nach Compliance-Anforderungen)

### 3.8 Disaster Recovery Integration
Backup-Strategien sind in die Disaster Recovery und Business Continuity Pläne integriert.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Backup und Wiederherstellung

| Aktivität | CISO | Backup Administrator | IT-Betrieb | System Owner | BCM Manager |
|-----------|------|----------------------|------------|--------------|-------------|
| Policy-Erstellung | R/A | C | C | C | C |
| Backup-Konfiguration | C | R/A | C | C | I |
| Backup-Durchführung | I | R/A | C | I | I |
| Backup-Monitoring | C | R/A | C | I | I |
| Restore-Tests | C | R | R | R/A | C |
| Disaster Recovery | A | C | R | C | R |
| Compliance-Prüfung | R/A | C | I | I | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Backup Administrator:** {{ meta.it.backup_admin }}
- **BCM Manager:** {{ meta.bcm.manager }}
- **Umsetzungsverantwortliche:** IT-Betrieb, System Owner
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0430_Richtlinie_Backup_Restore_und_Regelmaessige_Tests.md** - Detaillierte Implementierungsrichtlinie
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Cryptography Policy
- `0580_Policy_Aufbewahrung_und_Loeschung.md` - Retention Policy

### Zugehörige Standards/Baselines
- RPO/RTO-Matrix
- Backup-Schedule
- Retention-Anforderungen
- Restore-Test-Prozeduren

### Zugehörige Prozesse
- Backup-Prozess
- Restore-Prozess
- Backup-Test-Prozess
- Disaster Recovery Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Backup Success Rate (Ziel: 99.9%)
- Anzahl fehlgeschlagener Backups
- Durchschnittliche Backup-Dauer
- Restore Success Rate (Ziel: 100%)
- Durchschnittliche Restore-Dauer (RTO-Compliance)
- Backup-Test-Completion-Rate (Ziel: 100%)

### Nachweise und Evidence
- Backup-Logs und Job-Status
- Restore-Test-Protokolle
- Backup-Monitoring-Reports
- Disaster Recovery Test Reports
- Compliance-Nachweise (Retention)
- Audit-Berichte zu Backup-Compliance

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Fehlende Backups:** Sofortige Remediation, Untersuchung
- **Nicht getestete Backups:** Nachholung, Nachschulung
- **Unverschlüsselte Backups:** Sofortige Verschlüsselung, Untersuchung
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
- `0430_Richtlinie_Backup_Restore_und_Regelmaessige_Tests.md` - Detailed Guideline
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.13** - Information backup
- **ISO/IEC 27002:2022** - Information security controls
- **ISO 22301** - Business Continuity Management
- **DSGVO (EU 2016/679)** - Datenschutz-Grundverordnung (Backup von personenbezogenen Daten)

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)
