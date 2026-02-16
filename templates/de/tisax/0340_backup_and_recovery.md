---
Document-ID: tisax-0340
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Backup und Recovery

## Zweck

Dieses Dokument beschreibt die Backup- und Recovery-Prozesse gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle geschäftskritischen Daten von {{ source.organization_name }}.

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
- Retention: {{ source.backup_retention_days }} Tage

**Standard-Systeme:**
- Wöchentlich vollständig
- Retention: {{ source.backup_retention_days }} Tage

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
- RTO: {{ source.critical_rto }} Stunden
- Priorisierte Wiederherstellung

**Standard-Systeme:**
- RTO: {{ source.standard_rto }} Stunden

### Recovery Point Objective (RPO)

**Kritische Daten:**
- RPO: {{ source.critical_rpo }} Stunden
- Minimaler Datenverlust

**Standard-Daten:**
- RPO: {{ source.standard_rpo }} Stunden

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

{{ source.organization_name }} misst:
- Erfolgsrate Backups
- Durchschnittliche Recovery-Zeit
- Anzahl erfolgreicher Recovery-Tests

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
