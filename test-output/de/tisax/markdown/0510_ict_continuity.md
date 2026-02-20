
Document-ID: tisax-0510

Status: Draft
Classification: Internal

# IKT-Kontinuität

**Dokument-ID:** [FRAMEWORK]-0510
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

## Zweck

Dieses Dokument beschreibt die Maßnahmen zur Sicherstellung der IKT-Kontinuität gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle IT- und Kommunikationssysteme von [TODO].

## IKT-Kontinuitätsplanung

### Kritische Systeme

**Identifikation:**
- Geschäftskritische Anwendungen
- Infrastruktur-Systeme
- Kommunikationssysteme
- Datenbanken

**Priorisierung:**
- Tier 1: Kritisch (RTO < 4 Stunden)
- Tier 2: Wichtig (RTO < 24 Stunden)
- Tier 3: Standard (RTO < 72 Stunden)

### Redundanz

**Technische Redundanz:**
- Redundante Server
- Redundante Netzwerkverbindungen
- Redundante Stromversorgung
- Redundante Speichersysteme

**Standort-Redundanz:**
- Primäres Rechenzentrum
- Sekundäres Rechenzentrum
- Cloud-Backup

## Disaster Recovery

### DR-Strategien

**Hot Site:**
- Vollständig gespiegelte Umgebung
- Sofortige Umschaltung möglich
- Für kritische Systeme

**Warm Site:**
- Teilweise vorkonfigurierte Umgebung
- Schnelle Aktivierung möglich
- Für wichtige Systeme

**Cold Site:**
- Grundinfrastruktur vorhanden
- Manuelle Konfiguration erforderlich
- Für weniger kritische Systeme

### Failover-Prozesse

**Automatisches Failover:**
- Für kritische Systeme
- Überwachung und Alarmierung
- Automatische Umschaltung

**Manuelles Failover:**
- Für weniger kritische Systeme
- Dokumentierte Verfahren
- Getestete Prozesse

## Backup und Recovery

### Backup-Strategie

**Siehe:** 0340_backup_and_recovery.md

**IKT-spezifisch:**
- System-Images
- Konfigurationsdateien
- Datenbanken
- Anwendungsdaten

### Recovery-Verfahren

**Prozess:**
1. Bewertung des Ausfalls
2. Aktivierung des DR-Plans
3. Wiederherstellung der Systeme
4. Validierung
5. Rückkehr zum Normalbetrieb

## Testing

### Test-Szenarien

**Regelmäßig testen:**
- Kompletter Rechenzentrumsausfall
- Ausfall kritischer Systeme
- Netzwerkausfall
- Datenwiederherstellung

**Testfrequenz:**
- Kritische Systeme: Quartalsweise
- Wichtige Systeme: Halbjährlich
- Standard-Systeme: Jährlich

### Dokumentation

**Nach jedem Test:**
- Test-Bericht
- Identifizierte Probleme
- Verbesserungsmaßnahmen
- Aktualisierung der Pläne

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **10.2**: IKT-Kontinuität

### Assessment-Nachweise

- DR-Pläne
- Redundanz-Dokumentation
- Test-Berichte
- Recovery-Nachweise

## Kennzahlen

[TODO] misst:
- Systemverfügbarkeit
- Erfolgsrate DR-Tests
- Durchschnittliche Recovery-Zeit
- Anzahl ungeplanter Ausfälle

