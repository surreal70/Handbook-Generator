# Richtlinie: Backup, Restore und Regelmäßige Tests

**Dokument-ID:** 0430  
**Dokumenttyp:** Richtlinie (detailliert)  
**Zugehörige Policy:** 0420_Policy_Backup_und_Wiederherstellung.md  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.8.13  
**Owner:** {{ meta.it_operations.manager }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.document.date }}

---

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0420_Policy_Backup_und_Wiederherstellung.md` und definiert:
- Backup-Strategien und -Frequenzen
- Restore-Prozesse und -Tests
- Backup-Monitoring und -Verifizierung

**Geltungsbereich:** Alle Daten und Systeme bei **{{ meta.organization.name }}**

## 2. Backup-Strategie

### 2.1 3-2-1-Regel

**Prinzip:**
- **3** Kopien der Daten (1 Produktion + 2 Backups)
- **2** verschiedene Medientypen (z.B. Disk + Tape/Cloud)
- **1** Kopie Off-Site (geografisch getrennt)

### 2.2 Backup-Typen

**Full Backup:**
- Vollständige Sicherung aller Daten
- Frequenz: Wöchentlich (Sonntag)
- Längste Restore-Zeit, aber einfachste Wiederherstellung

**Incremental Backup:**
- Nur Änderungen seit letztem Backup
- Frequenz: Täglich
- Schnellstes Backup, längere Restore-Zeit

**Differential Backup:**
- Änderungen seit letztem Full Backup
- Frequenz: Optional, bei Bedarf
- Balance zwischen Full und Incremental

### 2.3 Backup-Frequenzen

| System-Typ | Full | Incremental | RPO | RTO |
|------------|------|-------------|-----|-----|
| Kritische Datenbanken | Täglich | Stündlich | 1h | 4h |
| Produktionsserver | Wöchentlich | Täglich | 24h | 8h |
| Fileserver | Wöchentlich | Täglich | 24h | 8h |
| Workstations | Monatlich | Wöchentlich | 7d | 24h |
| E-Mail | Täglich | Stündlich | 1h | 4h |

**RPO (Recovery Point Objective):** Maximaler Datenverlust  
**RTO (Recovery Time Objective):** Maximale Wiederherstellungszeit

## 3. Backup-Implementierung

### 3.1 Backup-Systeme

**On-Premises:**
- **Backup-Server:** {{ meta.backup.server }}
- **Backup-Software:** {{ meta.backup.software }} (z.B. Veeam, Commvault)
- **Storage:** {{ meta.backup.storage }} (Disk, Tape)

**Cloud-Backup:**
- **Cloud-Provider:** {{ meta.cloud.backup_provider }} (z.B. Azure Backup, AWS Backup)
- **Verschlüsselung:** AES-256
- **Geo-Redundanz:** Aktiviert

### 3.2 Backup-Zeitfenster

**Produktionssysteme:**
- Backup-Window: 22:00 - 06:00 Uhr
- Minimale Performance-Beeinträchtigung
- Monitoring während Backup

**Entwicklungssysteme:**
- Backup-Window: Jederzeit
- Keine Performance-Anforderungen

### 3.3 Verschlüsselung

**In Transit:**
- TLS 1.2+ für Backup-Übertragung
- VPN für Off-Site-Backups

**At Rest:**
- AES-256 Verschlüsselung aller Backups
- Schlüsselverwaltung über Key Vault
- Separate Schlüssel für Backups

### 3.4 Retention

**Retention-Schema (GFS - Grandfather-Father-Son):**
- **Daily:** 7 Tage
- **Weekly:** 4 Wochen
- **Monthly:** 12 Monate
- **Yearly:** {{ meta.retention.backup_years }} Jahre

**Compliance-Backups:**
- Finanzd aten: 10 Jahre
- Personaldaten: Gemäß DSGVO
- E-Mails: {{ meta.retention.email_years }} Jahre

## 4. Restore-Prozesse

### 4.1 Restore-Typen

**File-Level Restore:**
- Einzelne Dateien oder Ordner
- Self-Service für Nutzer (begrenzt)
- IT-Support für umfangreichere Restores

**System-Level Restore:**
- Vollständige Server-Wiederherstellung
- Bare-Metal-Recovery
- Nur durch IT-Betrieb

**Database Restore:**
- Point-in-Time-Recovery
- Transaktions-Logs
- Nur durch Database-Admins

### 4.2 Restore-Prozess

**Schritt 1: Anforderung**
- Ticket erstellen mit Details (Was, Wann, Warum)
- Genehmigung durch Vorgesetzten (bei umfangreichen Restores)

**Schritt 2: Vorbereitung**
- Backup-Katalog prüfen
- Restore-Ziel vorbereiten
- Downtime planen (falls erforderlich)

**Schritt 3: Restore**
- Restore durchführen
- Fortschritt überwachen
- Fehlerbehandlung

**Schritt 4: Verifizierung**
- Datenintegrität prüfen
- Funktionstest
- Nutzer-Bestätigung

**Schritt 5: Dokumentation**
- Restore-Log
- Lessons Learned
- Ticket schließen

### 4.3 Disaster Recovery

**Bei Totalausfall:**
1. Disaster Recovery Plan aktivieren
2. Alternative Infrastruktur bereitstellen
3. Kritische Systeme zuerst wiederherstellen
4. Schrittweise Wiederherstellung weiterer Systeme
5. Verifizierung und Rückkehr zum Normalbetrieb

**Details:** Siehe `0160_Disaster_Recovery_und_Business_Continuity.md` (IT-Operation Templates)

## 5. Backup-Monitoring

### 5.1 Überwachte Metriken

**Backup-Jobs:**
- Erfolgreiche/Fehlgeschlagene Backups
- Backup-Dauer
- Backup-Größe
- Änderungsrate

**Storage:**
- Verfügbarer Speicherplatz
- Wachstumsrate
- Deduplizierungsrate

**Performance:**
- Backup-Geschwindigkeit
- Netzwerk-Auslastung
- Storage-Performance

### 5.2 Alerting

**Kritische Alerts:**
- Backup fehlgeschlagen (2x hintereinander)
- Storage > 90% voll
- Backup-Window überschritten
- Verschlüsselung fehlgeschlagen

**Eskalation:**
- Erste Benachrichtigung: Backup-Admin
- Nach 2 Stunden: IT-Operations-Manager
- Nach 4 Stunden: CISO (bei kritischen Systemen)

### 5.3 Reporting

**Täglicher Backup-Report:**
- Status aller Backup-Jobs
- Fehlgeschlagene Backups
- Storage-Auslastung

**Monatlicher Management-Report:**
- Backup-Success-Rate
- Restore-Statistiken
- Kapazitätsplanung
- Compliance-Status

## 6. Backup-Tests

### 6.1 Test-Frequenzen

| Test-Typ | Frequenz | Durchführung |
|----------|----------|--------------|
| File-Level Restore | Monatlich | Stichprobe |
| System-Level Restore | Quartalsweise | Kritische Systeme |
| Database Restore | Monatlich | Point-in-Time-Recovery |
| Disaster Recovery | Jährlich | Vollständiger DR-Test |

### 6.2 Test-Prozess

**Planung:**
1. Test-Scope definieren
2. Test-Zeitfenster festlegen
3. Stakeholder informieren
4. Test-Umgebung vorbereiten

**Durchführung:**
1. Restore in Test-Umgebung
2. Datenintegrität prüfen
3. Funktionstest
4. Performance-Test
5. Zeitnahme (RTO-Verifizierung)

**Dokumentation:**
1. Test-Protokoll erstellen
2. Erfolg/Misserfolg dokumentieren
3. Probleme und Lessons Learned
4. Verbesserungsmaßnahmen definieren

**Nachbereitung:**
1. Test-Umgebung bereinigen
2. Backup-Prozesse anpassen (falls erforderlich)
3. Management-Bericht

### 6.3 Disaster Recovery Drill

**Jährlicher DR-Test:**
- Simulation eines Totalausfalls
- Aktivierung des DR-Plans
- Wiederherstellung kritischer Systeme
- Zeitnahme und Dokumentation
- Management-Präsentation

**Teilnehmer:**
- IT-Betrieb
- Application-Owner
- Management
- Business-Vertreter

## 7. Backup-Sicherheit

### 7.1 Zugriffskontrolle

**Berechtigungen:**
- **Backup-Admins:** Vollzugriff auf Backup-System
- **System-Admins:** Restore-Berechtigung für eigene Systeme
- **Nutzer:** Self-Service-Restore (begrenzt)

**Authentifizierung:**
- MFA für Backup-System-Zugriff
- Privilegierte Accounts für Backup-Admins

### 7.2 Immutable Backups

**Schutz vor Ransomware:**
- Immutable Backups (Write-Once-Read-Many)
- Air-Gapped Backups (offline)
- Separate Credentials für Backup-Storage

**Retention Lock:**
- Backups können nicht vorzeitig gelöscht werden
- Schutz vor versehentlicher oder böswilliger Löschung

### 7.3 Audit-Logging

**Protokollierte Events:**
- Backup-Job-Starts und -Ends
- Restore-Anforderungen und -Durchführungen
- Konfigurationsänderungen
- Zugriffe auf Backup-System

**Retention:** {{ meta.retention.log_years }} Jahre

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Backup-Success-Rate | > 99% |
| Restore-Success-Rate | 100% |
| RTO-Einhaltung | 100% |
| RPO-Einhaltung | 100% |
| Test-Completion-Rate | 100% |

### 8.2 Audit-Nachweise

- Backup-Logs und -Reports
- Restore-Test-Protokolle
- DR-Drill-Dokumentation
- Compliance-Berichte

## 9. Referenzen

### Interne Dokumente
- `0420_Policy_Backup_und_Wiederherstellung.md`
- `0160_Disaster_Recovery_und_Business_Continuity.md` (IT-Operation)

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.13** - Information backup
- **NIST SP 800-34** - Contingency Planning Guide

---

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta.document.next_review }}
