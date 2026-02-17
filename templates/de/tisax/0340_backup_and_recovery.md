
Document-ID: tisax-0340

Status: Draft
Classification: Internal

# Backup und Recovery

**Dokument-ID:** [FRAMEWORK]-0340
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

## Zweck

Dieses Dokument beschreibt die Backup- und Recovery-Prozesse gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle geschäftskritischen Daten von [TODO].

## Backup-Strategie

### Backup-Typen

**Vollbackup:**
- Wöchentlich
- Alle Daten
- Längere Durchführungszeit

**Inkrementelles Backup:**
- Täglich
- Nur Änderungen seit letztem Backup
- Schnelle Durchführung

**Differentielles Backup:**
- Bei Bedarf
- Änderungen seit letztem Vollbackup

### Backup-Zeitplan

**Kritische Systeme:**
- Täglich inkrementell
- Wöchentlich vollständig
- Retention: [TODO] Tage

**Standard-Systeme:**
- Wöchentlich vollständig
- Retention: [TODO] Tage

### Backup-Speicherorte

**Primär:**
- Lokales Backup-System
- Schneller Zugriff

**Sekundär:**
- Offsite-Backup
- Schutz vor Standortausfall
- Verschlüsselte Übertragung

## Recovery-Prozess

### Recovery Time Objective (RTO)

**Kritische Systeme:**
- RTO: [TODO] Stunden
- Priorisierte Wiederherstellung

**Standard-Systeme:**
- RTO: [TODO] Stunden

### Recovery Point Objective (RPO)

**Kritische Daten:**
- RPO: [TODO] Stunden
- Minimaler Datenverlust

**Standard-Daten:**
- RPO: [TODO] Stunden

### Recovery-Verfahren

**Prozess:**
1. Identifikation des Wiederherstellungsbedarfs
2. Auswahl des geeigneten Backups
3. Wiederherstellung
4. Validierung
5. Dokumentation

## Testing

### Backup-Tests

**Regelmäßig:**
- Monatliche Stichproben
- Quartalsweise Volltest
- Dokumentation der Ergebnisse

### Recovery-Tests

**Jährlich:**
- Disaster Recovery Test
- Vollständige Systemwiederherstellung
- Dokumentation und Lessons Learned

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **6.4**: Backup

### Assessment-Nachweise

- Backup-Konzept
- Backup-Protokolle
- Test-Berichte

## Kennzahlen

[TODO] misst:
- Erfolgsrate Backups
- Durchschnittliche Recovery-Zeit
- Anzahl erfolgreicher Recovery-Tests

