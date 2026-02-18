# Backup und Restore

**Dokument-ID:** [FRAMEWORK]-0150
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

## Zweck und Geltungsbereich

Dieses Dokument beschreibt die Backup- und Restore-Strategien für {{ meta-organisation.name }}. Es definiert Backup-Methoden, Zeitpläne, Aufbewahrungsfristen, RPO/RTO-Ziele und Restore-Prozeduren zur Sicherstellung der Datenintegrität und -verfügbarkeit.

**Geltungsbereich:** Alle IT-Systeme, Datenbanken, Applikationen und Daten von {{ meta-organisation.name }}

**Verantwortlich:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})

## Backup-Grundlagen

### Backup-Ziele

**Primäre Ziele:**
- **Datenschutz:** Schutz vor Datenverlust
- **Disaster Recovery:** Wiederherstellung nach Katastrophen
- **Compliance:** Erfüllung regulatorischer Anforderungen
- **Business Continuity:** Minimierung von Ausfallzeiten
- **Ransomware-Schutz:** Wiederherstellung nach Cyber-Angriffen

### Recovery-Ziele

#### Recovery Point Objective (RPO)

**Definition:** Maximaler tolerierbarer Datenverlust (Zeitspanne zwischen letztem Backup und Ausfall)

**RPO-Kategorien:**

| Kategorie | RPO | Backup-Frequenz | Anwendung |
|---|---|---|---|
| **Kritisch** | < 1 Stunde | Continuous / Hourly | Transaktionssysteme, Datenbanken |
| **Wichtig** | < 4 Stunden | 4x täglich | Business-Applikationen |
| **Standard** | < 24 Stunden | Täglich | File-Server, E-Mail |
| **Unkritisch** | < 7 Tage | Wöchentlich | Archiv-Daten, Test-Systeme |

#### Recovery Time Objective (RTO)

**Definition:** Maximale tolerierbare Ausfallzeit (Zeit bis zur Wiederherstellung)

**RTO-Kategorien:**

| Kategorie | RTO | Restore-Methode | Anwendung |
|---|---|---|---|
| **Kritisch** | < 1 Stunde | Hot-Standby, Snapshots | Produktions-Datenbanken |
| **Wichtig** | < 4 Stunden | Schnelle Restore-Systeme | Business-Applikationen |
| **Standard** | < 24 Stunden | Standard-Restore | File-Server |
| **Unkritisch** | < 7 Tage | Archiv-Restore | Test-Systeme |

### Backup-Strategien

#### Full Backup

**Beschreibung:** Vollständige Sicherung aller Daten

**Vorteile:**
- Einfache Wiederherstellung
- Nur ein Backup-Set erforderlich
- Schnelle Restore-Zeit

**Nachteile:**
- Lange Backup-Dauer
- Hoher Speicherbedarf
- Hohe Netzwerk-Last

**Anwendung:** Wöchentliche Basis-Backups

#### Incremental Backup

**Beschreibung:** Sicherung nur der seit letztem Backup (Full oder Incremental) geänderten Daten

**Vorteile:**
- Schnelle Backup-Dauer
- Geringer Speicherbedarf
- Geringe Netzwerk-Last

**Nachteile:**
- Komplexe Wiederherstellung
- Alle Incremental-Backups erforderlich
- Längere Restore-Zeit

**Anwendung:** Tägliche Backups zwischen Full-Backups

#### Differential Backup

**Beschreibung:** Sicherung aller seit letztem Full-Backup geänderten Daten

**Vorteile:**
- Schnellere Wiederherstellung als Incremental
- Nur Full + letztes Differential erforderlich
- Moderate Backup-Dauer

**Nachteile:**
- Wachsende Backup-Größe
- Höherer Speicherbedarf als Incremental

**Anwendung:** Alternative zu Incremental bei kritischen Systemen

#### Continuous Data Protection (CDP)

**Beschreibung:** Kontinuierliche Sicherung aller Änderungen in Echtzeit

**Vorteile:**
- Minimaler Datenverlust (RPO < 1 Min)
- Point-in-Time-Recovery
- Keine Backup-Fenster erforderlich

**Nachteile:**
- Hohe Kosten
- Komplexe Infrastruktur
- Hohe Performance-Anforderungen

**Anwendung:** Kritische Datenbanken und Transaktionssysteme

### Backup-Architektur

#### 3-2-1-Backup-Regel

**Regel:** 3 Kopien, 2 verschiedene Medien, 1 Offsite-Kopie

**Umsetzung:**
- **3 Kopien:** Produktiv-Daten + 2 Backups
- **2 Medien:** Disk + Tape oder Cloud
- **1 Offsite:** Geografisch getrennte Kopie

**Beispiel:**
1. Produktiv-Daten auf {{ netbox.storage.primary }}
2. Backup auf {{ netbox.storage.backup_disk }}
3. Offsite-Backup in {{ meta-handbook.backup_cloud_provider }}

#### Backup-Tiers

| Tier | Speicher-Typ | Restore-Zeit | Kosten | Anwendung |
|---|---|---|---|---|
| **Tier 1** | SSD / NVMe | Minuten | Hoch | Snapshots, CDP |
| **Tier 2** | HDD / NAS | Stunden | Mittel | Tägliche Backups |
| **Tier 3** | Tape / Object Storage | Tage | Niedrig | Langzeit-Archivierung |
| **Tier 4** | Cloud Cold Storage | Wochen | Sehr niedrig | Compliance-Archiv |

## Backup-Zeitpläne

### Produktions-Systeme

#### Datenbanken (Kritisch)

**System:** {{ netbox.database.server }}

**Backup-Strategie:**
- **Full Backup:** Sonntag 02:00
- **Differential Backup:** Täglich 02:00 (Mo-Sa)
- **Transaction Log Backup:** Stündlich
- **Snapshots:** Alle 4 Stunden

**RPO:** < 1 Stunde  
**RTO:** < 1 Stunde

**Aufbewahrung:**
- Tägliche Backups: 30 Tage
- Wöchentliche Backups: 12 Wochen
- Monatliche Backups: 12 Monate
- Jährliche Backups: 7 Jahre

#### Applikations-Server (Wichtig)

**System:** {{ netbox.application.server }}

**Backup-Strategie:**
- **Full Backup:** Sonntag 03:00
- **Incremental Backup:** Täglich 03:00 (Mo-Sa)
- **Snapshots:** Täglich vor Deployments

**RPO:** < 24 Stunden  
**RTO:** < 4 Stunden

**Aufbewahrung:**
- Tägliche Backups: 14 Tage
- Wöchentliche Backups: 8 Wochen
- Monatliche Backups: 6 Monate

#### File-Server (Standard)

**System:** {{ netbox.fileserver.server }}

**Backup-Strategie:**
- **Full Backup:** Sonntag 01:00
- **Incremental Backup:** Täglich 01:00 (Mo-Sa)

**RPO:** < 24 Stunden  
**RTO:** < 24 Stunden

**Aufbewahrung:**
- Tägliche Backups: 7 Tage
- Wöchentliche Backups: 4 Wochen
- Monatliche Backups: 3 Monate

### Backup-Kalender

| Tag | 01:00 | 02:00 | 03:00 | Stündlich |
|---|---|---|---|---|
| **Sonntag** | File-Server (Full) | Datenbank (Full) | App-Server (Full) | DB-Logs |
| **Montag** | File-Server (Inc) | Datenbank (Diff) | App-Server (Inc) | DB-Logs |
| **Dienstag** | File-Server (Inc) | Datenbank (Diff) | App-Server (Inc) | DB-Logs |
| **Mittwoch** | File-Server (Inc) | Datenbank (Diff) | App-Server (Inc) | DB-Logs |
| **Donnerstag** | File-Server (Inc) | Datenbank (Diff) | App-Server (Inc) | DB-Logs |
| **Freitag** | File-Server (Inc) | Datenbank (Diff) | App-Server (Inc) | DB-Logs |
| **Samstag** | File-Server (Inc) | Datenbank (Diff) | App-Server (Inc) | DB-Logs |

## Backup-Prozesse

### Backup-Prozess-Übersicht

```
┌─────────────────┐
│ Backup          │
│ Scheduling      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Pre-Backup      │
│ Checks          │
└────────┬────────┘
         │
┌────────▼────────┐
│ Backup          │
│ Execution       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Backup          │
│ Verification    │
└────────┬────────┘
         │
┌────────▼────────┐
│ Backup          │
│ Reporting       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Offsite         │
│ Replication     │
└─────────────────┘
```

### 1. Backup Scheduling

**Automatisierung:**
- Backup-Jobs in {{ meta-handbook.backup_system }} konfiguriert
- Zeitgesteuerte Ausführung
- Abhängigkeiten zwischen Jobs
- Retry-Mechanismen bei Fehlern

**Verantwortlich:** Backup-Administrator

### 2. Pre-Backup Checks

**Prüfungen:**
- Ausreichend Speicherplatz verfügbar
- Backup-Target erreichbar
- Quell-System verfügbar
- Keine laufenden Wartungsarbeiten
- Vorheriges Backup erfolgreich

**Bei Fehlern:** Alert an Operations-Team

### 3. Backup Execution

**Aktivitäten:**
- Applikations-konsistente Snapshots erstellen
- Daten komprimieren
- Daten verschlüsseln (AES-256)
- Daten auf Backup-Target übertragen
- Metadaten speichern

**Monitoring:** Echtzeit-Überwachung in {{ meta-handbook.monitoring_system }}

### 4. Backup Verification

**Verifikations-Methoden:**
- **Checksum-Validierung:** MD5/SHA-256 Prüfsummen
- **Katalog-Prüfung:** Backup-Katalog-Konsistenz
- **Restore-Test:** Stichproben-Restores (monatlich)
- **Integritäts-Scan:** Backup-Daten-Integrität

**Bei Fehlern:** Backup wiederholen, Alert eskalieren

### 5. Backup Reporting

**Reports:**
- Backup-Status (Erfolg/Fehler)
- Backup-Größe und -Dauer
- Speicherplatz-Auslastung
- Fehlgeschlagene Backups
- Trend-Analysen

**Empfänger:** {{ meta-organisation-roles.role_it_operations_manager.email }}

### 6. Offsite Replication

**Replikations-Methoden:**
- **Cloud-Sync:** Automatische Replikation zu {{ meta-handbook.backup_cloud_provider }}
- **Tape-Rotation:** Wöchentliche Tape-Auslagerung
- **Remote-Site:** Replikation zu {{ netbox.site.dr_location }}

**Verschlüsselung:** TLS in Transit, AES-256 at Rest

## Restore-Prozesse

### Restore-Prozess-Übersicht

```
┌─────────────────┐
│ Restore         │
│ Request         │
└────────┬────────┘
         │
┌────────▼────────┐
│ Restore         │
│ Planning        │
└────────┬────────┘
         │
┌────────▼────────┐
│ Restore         │
│ Preparation     │
└────────┬────────┘
         │
┌────────▼────────┐
│ Restore         │
│ Execution       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Restore         │
│ Verification    │
└────────┬────────┘
         │
┌────────▼────────┐
│ Restore         │
│ Documentation   │
└─────────────────┘
```

### 1. Restore Request

**Restore-Gründe:**
- Datenverlust (versehentliches Löschen)
- Daten-Korruption
- Ransomware-Angriff
- Hardware-Ausfall
- Disaster-Recovery
- Test/Entwicklung

**Erforderliche Informationen:**
- Was soll wiederhergestellt werden?
- Welcher Zeitpunkt? (Point-in-Time)
- Wohin soll wiederhergestellt werden?
- Dringlichkeit (RTO)
- Genehmigung

**Tool:** {{ meta-handbook.ticketing_system }}

### 2. Restore Planning

**Planungs-Aktivitäten:**
- Backup-Set identifizieren
- Restore-Methode auswählen
- Restore-Ziel vorbereiten
- Downtime planen (falls erforderlich)
- Stakeholder informieren

**Restore-Methoden:**
- **File-Level-Restore:** Einzelne Dateien/Ordner
- **Volume-Level-Restore:** Komplette Volumes
- **System-Level-Restore:** Bare-Metal-Recovery
- **Database-Restore:** Datenbank-Wiederherstellung
- **VM-Restore:** Virtuelle Maschinen

### 3. Restore Preparation

**Vorbereitungen:**
- Backup-Integrität prüfen
- Restore-Ziel bereitstellen
- Ausreichend Speicherplatz sicherstellen
- Netzwerk-Konnektivität prüfen
- Backup-Medien mounten (falls Tape)

### 4. Restore Execution

**Restore-Schritte:**

#### File-Level-Restore

1. Backup-Katalog durchsuchen
2. Dateien/Ordner auswählen
3. Restore-Ziel angeben
4. Restore starten
5. Fortschritt überwachen

**Geschätzte Dauer:** 10 GB/Stunde (von Disk)

#### Database-Restore

1. Datenbank-Service stoppen
2. Full-Backup wiederherstellen
3. Differential-Backup anwenden (falls vorhanden)
4. Transaction-Logs anwenden (Point-in-Time)
5. Datenbank-Konsistenz prüfen
6. Datenbank-Service starten

**Geschätzte Dauer:** 100 GB/Stunde

#### VM-Restore

1. VM ausschalten (falls läuft)
2. VM-Backup auswählen
3. Restore-Ziel (Datastore) auswählen
4. VM wiederherstellen
5. VM-Konfiguration prüfen
6. VM starten

**Geschätzte Dauer:** 50 GB/Stunde

#### Bare-Metal-Restore

1. Boot-Medium erstellen
2. System von Boot-Medium starten
3. Backup-Quelle verbinden
4. System-Backup auswählen
5. Restore auf Hardware durchführen
6. System neu starten

**Geschätzte Dauer:** 20 GB/Stunde

### 5. Restore Verification

**Verifikations-Schritte:**
- Daten-Vollständigkeit prüfen
- Daten-Integrität validieren
- Applikations-Funktionalität testen
- Performance-Check durchführen
- Nutzer-Akzeptanz einholen

**Verifikations-Checkliste:**
- [ ] Alle angeforderten Daten wiederhergestellt
- [ ] Daten-Integrität bestätigt
- [ ] Applikation funktionsfähig
- [ ] Performance akzeptabel
- [ ] Nutzer informiert

### 6. Restore Documentation

**Dokumentation:**
- Restore-Ticket aktualisieren
- Restore-Dauer dokumentieren
- Probleme und Lösungen festhalten
- Lessons Learned identifizieren
- Metriken erfassen

## Backup-Technologien

### Backup-Software

**Primäres Backup-System:**
- **System:** {{ meta-handbook.backup_system }}
- **Version:** [TODO]
- **Lizenz:** {{ meta-handbook.backup_system_license }}

**Funktionen:**
- Applikations-konsistente Backups
- Deduplizierung
- Kompression
- Verschlüsselung
- Cloud-Integration
- Automatische Verifikation

### Snapshot-Technologie

**Storage-Snapshots:**
- **System:** {{ netbox.storage.system }}
- **Snapshot-Frequenz:** Alle 4 Stunden
- **Aufbewahrung:** 48 Stunden
- **Verwendung:** Schnelle Rollbacks, Pre-Change-Snapshots

**VM-Snapshots:**
- **System:** {{ netbox.hypervisor.system }}
- **Snapshot-Typ:** Crash-consistent
- **Verwendung:** Pre-Deployment-Snapshots
- **Warnung:** Keine Langzeit-Backup-Lösung

### Cloud-Backup

**Cloud-Provider:**
- **Provider:** {{ meta-handbook.backup_cloud_provider }}
- **Region:** {{ meta-handbook.backup_cloud_region }}
- **Storage-Tier:** Standard / Glacier

**Vorteile:**
- Offsite-Backup automatisch
- Skalierbar
- Geo-Redundanz
- Pay-per-Use

**Nachteile:**
- Abhängigkeit von Internet-Verbindung
- Restore-Dauer bei großen Datenmengen
- Laufende Kosten

## Backup-Sicherheit

### Verschlüsselung

**In Transit:**
- TLS 1.3 für Netzwerk-Übertragung
- VPN für Remote-Backups

**At Rest:**
- AES-256 Verschlüsselung
- Separate Schlüssel-Verwaltung
- Key-Rotation alle 90 Tage

**Key-Management:**
- Schlüssel in {{ meta-handbook.key_management_system }}
- Zugriff nur für autorisierte Administratoren
- Backup der Schlüssel (Escrow)

### Immutable Backups

**Konzept:** Backups können nicht geändert oder gelöscht werden (Schutz vor Ransomware)

**Implementierung:**
- Object-Lock in Cloud-Storage
- WORM-Tapes (Write Once Read Many)
- Air-Gapped-Backups

**Aufbewahrung:** Mindestens 30 Tage immutable

### Zugriffskontrolle

**Berechtigungen:**
- Backup-Administratoren: Vollzugriff
- System-Administratoren: Restore-Berechtigung
- Service Desk: Keine Backup-Berechtigung

**Audit-Logging:**
- Alle Backup/Restore-Aktivitäten geloggt
- Logs in SIEM-System {{ meta-handbook.siem_system }}
- Monatliche Audit-Reviews

## Backup-Testing

### Test-Strategie

**Test-Typen:**
- **Verifikations-Tests:** Automatisch nach jedem Backup
- **Restore-Tests:** Monatliche Stichproben
- **DR-Tests:** Quartalsweise Full-Restore-Tests
- **Compliance-Tests:** Jährliche Audits

### Restore-Test-Prozess

**Monatlicher Restore-Test:**
1. Zufälliges System auswählen
2. Restore in isolierte Test-Umgebung
3. Funktionalität validieren
4. Restore-Dauer messen
5. Ergebnisse dokumentieren

**Test-Kriterien:**
- Restore erfolgreich
- RTO eingehalten
- Daten vollständig
- Applikation funktionsfähig

**Bei Fehlern:**
- Incident-Ticket erstellen
- Backup-Strategie überprüfen
- Korrekturmaßnahmen umsetzen
- Re-Test durchführen

### DR-Test

**Quartalsweiser DR-Test:**
1. Disaster-Szenario simulieren
2. Komplettes System in DR-Site wiederherstellen
3. Failover durchführen
4. Business-Prozesse testen
5. Failback durchführen

**Dokumentation:**
- Test-Plan
- Test-Ergebnisse
- Identifizierte Probleme
- Verbesserungs-Maßnahmen

## Metriken und Reporting

### Backup-Metriken

| Metrik | Zielwert | Messung |
|---|---|---|
| **Backup Success Rate** | > 98% | Erfolgreiche Backups / Gesamt-Backups |
| **Backup Window Compliance** | > 95% | Backups in Zeitfenster / Gesamt-Backups |
| **Restore Success Rate** | > 99% | Erfolgreiche Restores / Gesamt-Restores |
| **RTO Compliance** | > 95% | Restores innerhalb RTO / Gesamt-Restores |
| **RPO Compliance** | > 99% | Datenverlust < RPO / Gesamt-Incidents |

### Reporting

**Tägliches Backup-Report:**
- Backup-Status (Erfolg/Fehler)
- Fehlgeschlagene Backups
- Speicherplatz-Auslastung
- Alerts und Warnungen

**Monatliches Backup-Report:**
- Backup-Statistiken
- Restore-Aktivitäten
- Metriken-Dashboard
- Trend-Analysen
- Kapazitäts-Planung

**Quartalsweises Management-Report:**
- Backup-Strategie-Review
- DR-Test-Ergebnisse
- Compliance-Status
- Verbesserungs-Maßnahmen
- Budget-Planung

## Rollen und Verantwortlichkeiten

### Backup-Administrator

**Verantwortlichkeiten:**
- Backup-System-Verwaltung
- Backup-Job-Konfiguration
- Monitoring und Alerting
- Restore-Durchführung
- Reporting

**Person:** [Name]

### Storage-Administrator

**Verantwortlichkeiten:**
- Backup-Storage-Verwaltung
- Kapazitäts-Planung
- Performance-Optimierung
- Snapshot-Management

**Person:** [Name]

### IT Operations Manager

**Verantwortlichkeiten:**
- Backup-Strategie-Ownership
- Budget-Verantwortung
- Compliance-Sicherstellung
- Eskalations-Management

**Person:** {{ meta-organisation-roles.role_it_operations_manager.name }}

## Compliance und Regulierung

### Regulatorische Anforderungen

**DSGVO:**
- Daten-Verschlüsselung
- Zugriffskontrolle
- Audit-Logging
- Daten-Löschung nach Aufbewahrungsfrist

**ISO 27001:**
- Backup-Policy dokumentiert
- Regelmäßige Backup-Tests
- Incident-Response-Plan
- Kontinuierliche Verbesserung

**Branchenspezifisch:**
- [Weitere regulatorische Anforderungen]

### Aufbewahrungsfristen

| Daten-Typ | Aufbewahrungsfrist | Begründung |
|---|---|---|
| **Finanzdaten** | 10 Jahre | Steuerrecht |
| **Personaldaten** | 7 Jahre | Arbeitsrecht |
| **Vertragsdaten** | 6 Jahre | Vertragsrecht |
| **E-Mails** | 6 Jahre | Compliance |
| **System-Logs** | 1 Jahr | Security |
| **Backup-Logs** | 3 Jahre | Audit |

## Referenzen

- ITIL v4 - Service Continuity Management
- ISO/IEC 27001:2013 - Backup Controls
- DSGVO - Artikel 32 (Datensicherheit)
- 3-2-1-Backup-Regel
- Backup-System-Dokumentation: {{ meta-handbook.backup_system_docs }}

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Klassifizierung:** {{ meta-handbook.classification }}  
**Letzte Aktualisierung:** {{ meta-handbook.date }}

