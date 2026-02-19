# Runbooks und Standardoperationen

**Dokument-ID:** [FRAMEWORK]-0240
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

## Übersicht

Dieses Dokument enthält Standard-Runbooks, Schritt-für-Schritt-Anleitungen und Troubleshooting-Guides für häufige Betriebsaufgaben. Ziel ist es, konsistente und effiziente Durchführung von Standardoperationen zu gewährleisten.

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

## Runbook-Struktur

### Runbook-Template

Jedes Runbook folgt dieser standardisierten Struktur:

```markdown
# [RUNBOOK-TITEL]

**Runbook-ID:** RB-[NUMMER]
**Version:** [VERSION]
**Letzte Aktualisierung:** [DATUM]
**Verantwortlich:** [NAME]

## Zweck
[Beschreibung des Zwecks und Anwendungsfalls]

## Voraussetzungen
- [Erforderliche Berechtigungen]
- [Erforderliche Tools]
- [Erforderliches Wissen]

## Geschätzte Dauer
[ZEIT] Minuten/Stunden

## Risikobewertung
- **Risiko:** Niedrig / Mittel / Hoch
- **Impact:** Niedrig / Mittel / Hoch
- **Rollback möglich:** Ja / Nein

## Schritte
1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]

## Validierung
- [Validierungsschritt 1]
- [Validierungsschritt 2]

## Rollback
[Rollback-Prozedur falls erforderlich]

## Troubleshooting
[Häufige Probleme und Lösungen]

## Referenzen
- [Dokumentation]
- [Tickets]
```

## System-Management Runbooks

### RB-001: Server-Neustart

**Runbook-ID:** RB-001  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Zweck
Kontrollierter Neustart eines Servers zur Behebung von Problemen oder nach Updates.

#### Voraussetzungen
- Root/Administrator-Zugriff auf Server
- Genehmigung für Neustart (bei Produktionssystemen)
- Wartungsfenster (falls erforderlich)

#### Geschätzte Dauer
15-30 Minuten

#### Risikobewertung
- **Risiko:** Mittel
- **Impact:** Hoch (bei Produktionssystemen)
- **Rollback möglich:** Nein

#### Schritte

1. **Vorbereitung**
   ```bash
   # Aktuelle Systemlast prüfen
   uptime
   top
   
   # Laufende Prozesse prüfen
   ps aux | grep [kritische_prozesse]
   
   # Benutzer informieren (falls erforderlich)
   wall "System wird in 5 Minuten neu gestartet"
   ```

2. **Services stoppen**
   ```bash
   # Anwendungs-Services stoppen
   systemctl stop [service_name]
   
   # Status prüfen
   systemctl status [service_name]
   ```

3. **Neustart durchführen**
   ```bash
   # Neustart initiieren
   shutdown -r now
   # oder
   reboot
   ```

4. **Nach Neustart: Validierung**
   ```bash
   # System-Uptime prüfen
   uptime
   
   # Services prüfen
   systemctl status [service_name]
   
   # Logs prüfen
   journalctl -xe
   tail -f /var/log/syslog
   ```

#### Validierung
- [ ] Server ist erreichbar (ping, SSH)
- [ ] Alle kritischen Services laufen
- [ ] Keine Fehler in System-Logs
- [ ] Monitoring zeigt grünen Status
- [ ] Anwendung ist funktionsfähig

#### Troubleshooting
- **Problem:** Server startet nicht
  - **Lösung:** Console-Zugriff nutzen, Boot-Logs prüfen
- **Problem:** Services starten nicht
  - **Lösung:** Manuell starten, Logs prüfen, Dependencies prüfen

### RB-002: Service-Neustart

**Runbook-ID:** RB-002  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Zweck
Neustart eines einzelnen Services ohne System-Neustart.

#### Voraussetzungen
- Sudo/Administrator-Rechte
- Service-Name bekannt

#### Geschätzte Dauer
5-10 Minuten

#### Schritte

1. **Service-Status prüfen**
   ```bash
   # Linux
   systemctl status [service_name]
   
   # Windows
   Get-Service [service_name]
   ```

2. **Service stoppen**
   ```bash
   # Linux
   systemctl stop [service_name]
   
   # Windows
   Stop-Service [service_name]
   ```

3. **Warten und validieren**
   ```bash
   # Prozess-Ende bestätigen
   ps aux | grep [service_name]
   
   # Ports freigegeben prüfen
   netstat -tulpn | grep [port]
   ```

4. **Service starten**
   ```bash
   # Linux
   systemctl start [service_name]
   
   # Windows
   Start-Service [service_name]
   ```

5. **Validierung**
   ```bash
   # Status prüfen
   systemctl status [service_name]
   
   # Logs prüfen
   journalctl -u [service_name] -f
   ```

#### Validierung
- [ ] Service läuft (Status: active/running)
- [ ] Keine Fehler in Logs
- [ ] Port ist gebunden
- [ ] Anwendung antwortet

### RB-003: Disk-Space-Cleanup

**Runbook-ID:** RB-003  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Zweck
Freigabe von Speicherplatz bei kritischer Disk-Auslastung.

#### Voraussetzungen
- Root/Administrator-Zugriff
- Backup vor größeren Löschungen

#### Geschätzte Dauer
30-60 Minuten

#### Schritte

1. **Disk-Auslastung analysieren**
   ```bash
   # Gesamtübersicht
   df -h
   
   # Größte Verzeichnisse finden
   du -h / | sort -rh | head -20
   
   # Größte Dateien finden
   find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
   ```

2. **Log-Dateien bereinigen**
   ```bash
   # Alte Logs löschen
   find /var/log -type f -name "*.log" -mtime +30 -delete
   
   # Komprimierte Logs löschen
   find /var/log -type f -name "*.gz" -mtime +90 -delete
   
   # Journal-Logs bereinigen
   journalctl --vacuum-time=30d
   ```

3. **Temporäre Dateien löschen**
   ```bash
   # /tmp bereinigen
   find /tmp -type f -atime +7 -delete
   
   # /var/tmp bereinigen
   find /var/tmp -type f -atime +30 -delete
   ```

4. **Package-Cache bereinigen**
   ```bash
   # Debian/Ubuntu
   apt-get clean
   apt-get autoclean
   apt-get autoremove
   
   # RedHat/CentOS
   yum clean all
   
   # Docker
   docker system prune -a
   ```

5. **Alte Backups archivieren/löschen**
   ```bash
   # Alte Backups identifizieren
   find /backup -type f -mtime +90
   
   # Nach Genehmigung löschen
   find /backup -type f -mtime +90 -delete
   ```

#### Validierung
- [ ] Disk-Auslastung unter 80%
- [ ] Kritische Services laufen weiter
- [ ] Keine wichtigen Daten gelöscht
- [ ] Monitoring-Alerts gelöst

## Datenbank-Management Runbooks

### RB-010: Datenbank-Backup

**Runbook-ID:** RB-010  
**Version:** 1.0  
**Verantwortlich:** Database Administrator

#### Zweck
Manuelles Datenbank-Backup vor kritischen Änderungen.

#### Voraussetzungen
- Datenbank-Admin-Rechte
- Ausreichend Speicherplatz
- Backup-Verzeichnis vorhanden

#### Geschätzte Dauer
15-60 Minuten (abhängig von DB-Größe)

#### Schritte

**PostgreSQL:**
```bash
# Full Backup
pg_dump -U postgres -F c -b -v -f /backup/db_$(date +%Y%m%d_%H%M%S).backup [database_name]

# Schema-only Backup
pg_dump -U postgres -s -f /backup/schema_$(date +%Y%m%d_%H%M%S).sql [database_name]
```

**MySQL/MariaDB:**
```bash
# Full Backup
mysqldump -u root -p --single-transaction --routines --triggers [database_name] > /backup/db_$(date +%Y%m%d_%H%M%S).sql

# All Databases
mysqldump -u root -p --all-databases > /backup/all_dbs_$(date +%Y%m%d_%H%M%S).sql
```

**MongoDB:**
```bash
# Full Backup
mongodump --out /backup/mongodb_$(date +%Y%m%d_%H%M%S)

# Specific Database
mongodump --db [database_name] --out /backup/mongodb_$(date +%Y%m%d_%H%M%S)
```

#### Validierung
- [ ] Backup-Datei erstellt
- [ ] Backup-Größe plausibel
- [ ] Backup-Integrität geprüft
- [ ] Backup-Speicherort dokumentiert

### RB-011: Datenbank-Restore

**Runbook-ID:** RB-011  
**Version:** 1.0  
**Verantwortlich:** Database Administrator

#### Zweck
Wiederherstellung einer Datenbank aus Backup.

#### Voraussetzungen
- Datenbank-Admin-Rechte
- Gültiges Backup vorhanden
- Wartungsfenster (für Produktionssysteme)

#### Geschätzte Dauer
30-120 Minuten (abhängig von DB-Größe)

#### Risikobewertung
- **Risiko:** Hoch
- **Impact:** Hoch
- **Rollback möglich:** Ja (mit aktuellem Backup)

#### Schritte

1. **Vorbereitung**
   ```bash
   # Aktuelles Backup erstellen (Sicherheit!)
   [siehe RB-010]
   
   # Benutzer informieren
   # Services stoppen
   ```

2. **Restore durchführen**

   **PostgreSQL:**
   ```bash
   # Datenbank löschen und neu erstellen
   dropdb [database_name]
   createdb [database_name]
   
   # Restore
   pg_restore -U postgres -d [database_name] -v /backup/db_backup.backup
   ```

   **MySQL/MariaDB:**
   ```bash
   # Restore
   mysql -u root -p [database_name] < /backup/db_backup.sql
   ```

   **MongoDB:**
   ```bash
   # Restore
   mongorestore --db [database_name] /backup/mongodb_backup/[database_name]
   ```

3. **Validierung**
   ```bash
   # Tabellen/Collections prüfen
   # Datensätze zählen
   # Integrität prüfen
   ```

#### Validierung
- [ ] Datenbank ist erreichbar
- [ ] Alle Tabellen/Collections vorhanden
- [ ] Datensatz-Anzahl plausibel
- [ ] Anwendung funktioniert
- [ ] Keine Fehler in Logs

## Netzwerk-Management Runbooks

### RB-020: Firewall-Regel hinzufügen

**Runbook-ID:** RB-020  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_CISO }}

#### Zweck
Hinzufügen einer neuen Firewall-Regel.

#### Voraussetzungen
- Firewall-Admin-Rechte
- Change-Ticket genehmigt
- Regel-Details dokumentiert

#### Geschätzte Dauer
15-30 Minuten

#### Schritte

1. **Regel-Details dokumentieren**
   - Quell-IP/Netzwerk
   - Ziel-IP/Netzwerk
   - Port/Protokoll
   - Aktion (Allow/Deny)
   - Begründung

2. **Regel hinzufügen**

   **iptables (Linux):**
   ```bash
   # Regel hinzufügen
   iptables -A INPUT -s [source_ip] -p tcp --dport [port] -j ACCEPT
   
   # Regel speichern
   iptables-save > /etc/iptables/rules.v4
   ```

   **firewalld (Linux):**
   ```bash
   # Port öffnen
   firewall-cmd --permanent --add-port=[port]/tcp
   
   # Reload
   firewall-cmd --reload
   ```

   **Windows Firewall:**
   ```powershell
   # Regel hinzufügen
   New-NetFirewallRule -DisplayName "[Rule Name]" -Direction Inbound -Protocol TCP -LocalPort [port] -Action Allow
   ```

3. **Validierung**
   ```bash
   # Regel prüfen
   iptables -L -n -v
   
   # Konnektivität testen
   telnet [target_ip] [port]
   nc -zv [target_ip] [port]
   ```

#### Validierung
- [ ] Regel ist aktiv
- [ ] Konnektivität funktioniert
- [ ] Keine unerwünschten Nebeneffekte
- [ ] Regel dokumentiert

## Benutzer-Management Runbooks

### RB-030: Benutzer-Account erstellen

**Runbook-ID:** RB-030  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Zweck
Erstellung eines neuen Benutzer-Accounts.

#### Voraussetzungen
- Admin-Rechte
- Genehmigtes Ticket
- Benutzer-Details vorhanden

#### Geschätzte Dauer
10-15 Minuten

#### Schritte

1. **Benutzer-Details sammeln**
   - Vollständiger Name
   - E-Mail-Adresse
   - Abteilung
   - Erforderliche Gruppen/Rollen
   - Manager/Genehmiger

2. **Account erstellen**

   **Linux:**
   ```bash
   # Benutzer erstellen
   useradd -m -s /bin/bash -c "[Full Name]" [username]
   
   # Passwort setzen
   passwd [username]
   
   # Zu Gruppen hinzufügen
   usermod -aG [group1],[group2] [username]
   ```

   **Active Directory:**
   ```powershell
   # Benutzer erstellen
   New-ADUser -Name "[Full Name]" -GivenName "[First]" -Surname "[Last]" `
     -SamAccountName [username] -UserPrincipalName [username]@domain.com `
     -Path "OU=Users,DC=domain,DC=com" -AccountPassword (ConvertTo-SecureString "[password]" -AsPlainText -Force) `
     -Enabled $true
   
   # Zu Gruppen hinzufügen
   Add-ADGroupMember -Identity "[Group Name]" -Members [username]
   ```

3. **Berechtigungen zuweisen**
   - Dateisystem-Berechtigungen
   - Anwendungs-Zugriffe
   - E-Mail-Account
   - VPN-Zugang

4. **Benutzer informieren**
   - Willkommens-E-Mail senden
   - Zugangsdaten übermitteln (sicher!)
   - Dokumentation bereitstellen

#### Validierung
- [ ] Account ist aktiv
- [ ] Login funktioniert
- [ ] Berechtigungen korrekt
- [ ] Benutzer informiert
- [ ] Dokumentiert in CMDB

### RB-031: Benutzer-Account deaktivieren

**Runbook-ID:** RB-031  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Zweck
Deaktivierung eines Benutzer-Accounts (z.B. bei Austritt).

#### Voraussetzungen
- Admin-Rechte
- Genehmigtes Ticket
- Offboarding-Checkliste

#### Geschätzte Dauer
20-30 Minuten

#### Schritte

1. **Account deaktivieren**

   **Linux:**
   ```bash
   # Account sperren
   usermod -L [username]
   passwd -l [username]
   
   # Shell deaktivieren
   usermod -s /sbin/nologin [username]
   ```

   **Active Directory:**
   ```powershell
   # Account deaktivieren
   Disable-ADAccount -Identity [username]
   
   # Beschreibung aktualisieren
   Set-ADUser -Identity [username] -Description "Deactivated on $(Get-Date -Format 'yyyy-MM-dd')"
   ```

2. **Zugriffe entfernen**
   - VPN-Zugang deaktivieren
   - E-Mail-Weiterleitung einrichten
   - Gruppen-Mitgliedschaften entfernen
   - Anwendungs-Zugriffe widerrufen
   - Hardware zurückfordern

3. **Daten sichern**
   - Home-Verzeichnis archivieren
   - E-Mails archivieren
   - Wichtige Dateien sichern

4. **Dokumentation**
   - Offboarding-Checkliste abarbeiten
   - CMDB aktualisieren
   - Manager informieren

#### Validierung
- [ ] Account ist deaktiviert
- [ ] Login nicht mehr möglich
- [ ] Alle Zugriffe entfernt
- [ ] Daten gesichert
- [ ] Dokumentiert

## Monitoring und Alerting Runbooks

### RB-040: Alert-Untersuchung

**Runbook-ID:** RB-040  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Zweck
Systematische Untersuchung eines Monitoring-Alerts.

#### Voraussetzungen
- Zugriff auf Monitoring-System
- Zugriff auf betroffene Systeme

#### Geschätzte Dauer
15-60 Minuten

#### Schritte

1. **Alert-Details erfassen**
   - Alert-Name und Severity
   - Betroffenes System/Service
   - Zeitpunkt des Auftretens
   - Alert-Beschreibung

2. **Erste Analyse**
   ```bash
   # System-Status prüfen
   uptime
   top
   df -h
   free -m
   
   # Service-Status prüfen
   systemctl status [service]
   
   # Logs prüfen
   journalctl -xe
   tail -f /var/log/[relevant_log]
   ```

3. **Ursache identifizieren**
   - Korrelation mit anderen Events
   - Änderungen in letzter Zeit
   - Bekannte Probleme prüfen
   - Metriken analysieren

4. **Maßnahmen ergreifen**
   - Sofortmaßnahmen (falls erforderlich)
   - Incident-Ticket erstellen
   - Eskalation (falls erforderlich)
   - Dokumentation

5. **Validierung**
   - Alert ist gelöst
   - System funktioniert normal
   - Keine weiteren Alerts

#### Troubleshooting-Matrix

| Alert-Typ | Erste Prüfung | Häufige Ursachen | Sofortmaßnahme |
|---|---|---|---|
| High CPU | top, ps aux | Runaway-Prozess | Prozess beenden |
| High Memory | free -m, ps aux | Memory-Leak | Service-Neustart |
| Disk Full | df -h, du -h | Log-Dateien, Backups | Cleanup durchführen |
| Service Down | systemctl status | Crash, Config-Fehler | Service-Neustart |
| High Latency | ping, traceroute | Netzwerk, Last | Load-Balancing prüfen |

## Backup und Recovery Runbooks

### RB-050: Backup-Verifikation

**Runbook-ID:** RB-050  
**Version:** 1.0  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Zweck
Regelmäßige Überprüfung der Backup-Integrität.

#### Voraussetzungen
- Zugriff auf Backup-System
- Test-Umgebung verfügbar

#### Geschätzte Dauer
30-60 Minuten

#### Schritte

1. **Backup-Status prüfen**
   ```bash
   # Letzte Backups anzeigen
   [backup_tool] list --last 7
   
   # Backup-Logs prüfen
   tail -100 /var/log/backup.log
   ```

2. **Backup-Integrität prüfen**
   ```bash
   # Checksummen validieren
   [backup_tool] verify [backup_id]
   
   # Backup-Größe prüfen
   ls -lh /backup/
   ```

3. **Restore-Test durchführen**
   - Zufälliges Backup auswählen
   - In Test-Umgebung wiederherstellen
   - Funktionalität validieren
   - Ergebnis dokumentieren

4. **Dokumentation**
   - Test-Ergebnis festhalten
   - Probleme dokumentieren
   - Verbesserungen identifizieren

#### Validierung
- [ ] Alle Backups erfolgreich
- [ ] Integrität bestätigt
- [ ] Restore-Test erfolgreich
- [ ] Dokumentiert

## Troubleshooting-Guides

### Allgemeine Troubleshooting-Methodik

1. **Problem identifizieren**
   - Symptome sammeln
   - Fehlermeldungen notieren
   - Zeitpunkt des Auftretens

2. **Informationen sammeln**
   - Logs analysieren
   - Monitoring-Daten prüfen
   - Änderungen identifizieren

3. **Hypothese bilden**
   - Mögliche Ursachen auflisten
   - Wahrscheinlichkeit bewerten
   - Priorisieren

4. **Testen**
   - Hypothese testen
   - Ergebnisse dokumentieren
   - Nächste Hypothese

5. **Lösung implementieren**
   - Korrekturmaßnahme durchführen
   - Validieren
   - Dokumentieren

6. **Prävention**
   - Root-Cause-Analysis
   - Verbesserungen identifizieren
   - Implementieren

### Häufige Probleme und Lösungen

#### Problem: Service startet nicht

**Symptome:**
- Service-Status: failed
- Fehlermeldung in Logs

**Diagnose:**
```bash
# Status prüfen
systemctl status [service]

# Logs prüfen
journalctl -u [service] -n 50

# Config-Test
[service] -t  # (z.B. nginx -t, apache2ctl configtest)
```

**Lösungen:**
1. Config-Fehler korrigieren
2. Dependencies prüfen
3. Berechtigungen prüfen
4. Ports prüfen (bereits belegt?)

#### Problem: Hohe CPU-Last

**Symptome:**
- CPU-Auslastung > 80%
- System langsam

**Diagnose:**
```bash
# Top-Prozesse identifizieren
top
htop

# Prozess-Details
ps aux | sort -nrk 3,3 | head -n 5
```

**Lösungen:**
1. Runaway-Prozess beenden
2. Ressourcen-Limits setzen
3. Skalierung prüfen
4. Code-Optimierung

#### Problem: Disk voll

**Symptome:**
- Disk-Auslastung > 90%
- "No space left on device" Fehler

**Diagnose:**
```bash
# Auslastung prüfen
df -h

# Große Dateien finden
du -h / | sort -rh | head -20
find / -type f -size +100M
```

**Lösungen:**
1. Logs bereinigen
2. Temporäre Dateien löschen
3. Alte Backups archivieren
4. Storage erweitern

## Prozesse und Verantwortlichkeiten

### RACI-Matrix

| Aktivität | CIO | Ops Manager | Ops Team | On-Call |
|---|---|---|---|---|
| Runbook-Erstellung | C | A | R | C |
| Runbook-Ausführung | I | C | R | R |
| Runbook-Aktualisierung | I | A | R | C |
| Troubleshooting | I | C | R | R |

> **Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance und Standards

### Relevante Standards
- **ITIL v4:** Service Operation Practice
- **ISO 20000:** Clause 8.1 - Operational Planning and Control
- **COBIT 2019:** DSS01 - Managed Operations

## Anhang

### Glossar

| Begriff | Definition |
|---|---|
| Runbook | Dokumentierte Schritt-für-Schritt-Anleitung für Standardoperationen |
| Troubleshooting | Systematische Fehlersuche und -behebung |
| Standard Operating Procedure (SOP) | Standardisierte Betriebsanweisung |

### Referenzen
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

**Letzte Aktualisierung:** {{ meta-handbook.date }}  
**Nächste Review:** [TODO: Datum]  
**Kontakt:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}

