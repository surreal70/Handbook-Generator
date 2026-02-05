# Richtlinie: ICT Disaster Recovery - Schnittstellen zu BCM

**Dokument-ID:** 0450  
**Dokumenttyp:** Richtlinie (detailliert)  
**Zugehörige Policy:** 0440_Policy_Business_Continuity_ICT_Readiness.md  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.29, A.5.30  
**Owner:** {{ meta.it_operations.manager }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.document.date }}

---

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0440_Policy_Business_Continuity_ICT_Readiness.md` und definiert:
- ICT Disaster Recovery Pläne und Prozesse
- Schnittstellen zum Business Continuity Management (BCM)
- ICT-Readiness für Notfallsituationen

**Geltungsbereich:** Alle IT-Systeme und -Services bei **AdminSend GmbH**

## 2. ICT Disaster Recovery Strategie

### 2.1 Recovery-Ziele

**RTO (Recovery Time Objective):**
| System-Tier | RTO | Begründung |
|-------------|-----|------------|
| Tier 1 (Kritisch) | 4 Stunden | Geschäftskritische Systeme |
| Tier 2 (Wichtig) | 24 Stunden | Wichtige Business-Funktionen |
| Tier 3 (Standard) | 72 Stunden | Standard-IT-Services |

**RPO (Recovery Point Objective):**
| System-Tier | RPO | Backup-Frequenz |
|-------------|-----|-----------------|
| Tier 1 | 1 Stunde | Stündlich |
| Tier 2 | 24 Stunden | Täglich |
| Tier 3 | 7 Tage | Wöchentlich |

### 2.2 DR-Strategien

**Hot Site:**
- Vollständig redundante Infrastruktur
- Echtzeit-Replikation
- Sofortige Failover-Fähigkeit
- Für Tier 1 Systeme

**Warm Site:**
- Teilweise vorkonfigurierte Infrastruktur
- Regelmäßige Backups
- Aktivierung innerhalb Stunden
- Für Tier 2 Systeme

**Cold Site:**
- Grundinfrastruktur vorhanden
- Wiederherstellung aus Backups
- Aktivierung innerhalb Tagen
- Für Tier 3 Systeme

## 3. DR-Infrastruktur

### 3.1 Primäres Rechenzentrum

**Standort:** {{ netbox.site.primary }}  
**Systeme:** Alle Produktionssysteme  
**Redundanz:** N+1 für kritische Komponenten

### 3.2 DR-Standort

**Standort:** {{ netbox.site.dr }}  
**Entfernung:** > 50 km vom Primärstandort  
**Systeme:** Replizierte Tier 1 Systeme, Backup-Infrastruktur

### 3.3 Cloud-DR

**Cloud-Provider:** {{ meta.cloud.dr_provider }}  
**Regionen:** {{ meta.cloud.primary_region }}, {{ meta.cloud.dr_region }}  
**Services:** IaaS für DR-Workloads

## 4. Schnittstellen zu BCM

### 4.1 Business Impact Analysis (BIA)

**ICT-Input für BIA:**
- System-Abhängigkeiten
- RTO/RPO-Fähigkeiten
- Single Points of Failure
- Wiederherstellungskosten

**BIA-Output für ICT:**
- Kritikalität der Business-Prozesse
- Maximale Ausfalltoleranz (MTD)
- Priorisierung der Wiederherstellung

### 4.2 BCM-Pläne

**ICT-Beiträge:**
- IT Disaster Recovery Plan (DRP)
- Technische Wiederherstellungsprozeduren
- Kontaktlisten IT-Personal
- Eskalationspfade

**BCM-Koordination:**
- Abstimmung mit Business Continuity Plans (BCP)
- Gemeinsame Übungen und Tests
- Konsistente Kommunikation

### 4.3 Krisenmanagement

**ICT-Rolle im Krisenstab:**
- IT-Vertreter im Krisenstab
- Status-Updates zu IT-Systemen
- Technische Entscheidungsunterstützung
- Koordination der IT-Wiederherstellung

## 5. DR-Aktivierung

### 5.1 Aktivierungskriterien

**Automatische Aktivierung:**
- Kompletter Ausfall Primärstandort
- Kritische Infrastrukturkomponenten ausgefallen
- Naturkatastrophen

**Manuelle Aktivierung:**
- Entscheidung durch Krisenstab
- Geplante Failover-Tests
- Wartungsarbeiten

### 5.2 Aktivierungsprozess

**Phase 1: Assessment (0-30 Minuten)**
1. Schadensumfang bewerten
2. DR-Aktivierung entscheiden
3. Krisenstab informieren
4. DR-Team mobilisieren

**Phase 2: Activation (30 Minuten - 4 Stunden)**
1. DR-Infrastruktur aktivieren
2. Systeme wiederherstellen (nach Priorität)
3. Netzwerk-Routing umstellen
4. Funktionstest

**Phase 3: Operation (variabel)**
1. Betrieb im DR-Modus
2. Monitoring intensivieren
3. Regelmäßige Status-Updates
4. Vorbereitung Rückkehr

**Phase 4: Failback (geplant)**
1. Primärstandort wiederherstellen
2. Daten synchronisieren
3. Geplanter Failback
4. Verifizierung

## 6. DR-Tests

### 6.1 Test-Typen

**Tabletop-Exercise:**
- Frequenz: Quartalsweise
- Durchsprache des DR-Plans
- Keine technische Aktivierung

**Partial Failover:**
- Frequenz: Halbjährlich
- Einzelne Systeme failover
- Minimale Business-Auswirkung

**Full DR-Drill:**
- Frequenz: Jährlich
- Kompletter Failover aller Tier 1 Systeme
- Geplante Downtime erforderlich

### 6.2 Test-Dokumentation

**Test-Protokoll:**
- Datum, Teilnehmer, Scope
- Durchgeführte Schritte
- Gemessene RTO/RPO
- Probleme und Lessons Learned
- Verbesserungsmaßnahmen

## 7. Compliance und Audit

### 7.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| DR-Test-Success-Rate | 100% |
| RTO-Einhaltung (Test) | 100% |
| RPO-Einhaltung (Test) | 100% |
| DR-Plan-Aktualität | < 6 Monate |

### 7.2 Audit-Nachweise

- DR-Pläne und -Prozeduren
- Test-Protokolle
- BIA-Dokumentation
- Failover-Logs

## 8. Referenzen

### Interne Dokumente
- `0440_Policy_Business_Continuity_ICT_Readiness.md`
- `0430_Richtlinie_Backup_Restore_und_Regelmaessige_Tests.md`
- BCM-Handbuch (falls vorhanden)

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.29** - Information security during disruption
- **ISO/IEC 27001:2022 Annex A.5.30** - ICT readiness for business continuity
- **ISO 22301** - Business Continuity Management

---

**Genehmigt durch:** Thomas Weber, CISO  
**Nächster Review:** {{ meta.document.next_review }}
