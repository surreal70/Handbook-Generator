# Risikobehandlungsplan (RTP) – Template

**Dokument-ID:** ISMS-0090
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



## 1. Ziel und Geltungsbereich

### 1.1 Ziel

Der Risikobehandlungsplan (Risk Treatment Plan, RTP) der **AdminSend GmbH** dokumentiert alle geplanten Maßnahmen zur Behandlung identifizierter Informationssicherheitsrisiken. Er dient als:
- Aktionsplan für Risikobehandlung
- Tracking-Tool für Maßnahmenumsetzung
- Nachweis für Audits und Compliance
- Basis für Ressourcenplanung und Budgetierung

### 1.2 Geltungsbereich

Dieser Plan umfasst alle Maßnahmen zur Behandlung von Risiken im ISMS-Scope (siehe `0020_ISMS_Geltungsbereich_Scope.md`), die mit der Strategie "Mindern" oder "Übertragen" behandelt werden.

**Ausgeschlossen:**
- Akzeptierte Risiken (siehe `0080_ISMS_Risikoregister_Template.md`)
- Vermiedene Risiken (Aktivität eingestellt)

## 2. Risikobehandlungsplan-Tabelle

### 2.1 Aktive Maßnahmen

| Maßnahme-ID | Risiko-ID | Maßnahme | Control-Referenz (Annex A) | Owner | Priorität | Aufwand (PT) | Budget | Zieltermin | Status | Fortschritt | Bemerkungen |
|-------------|-----------|----------|----------------------------|-------|-----------|--------------|--------|------------|--------|-------------|-------------|
| M-001 | R-001 | Redundanter Core Switch beschaffen | A.8.6 (Capacity management) | [TODO] | Hoch | 20 | 50.000 € | 2026-06-30 | Geplant | 0% | Budget genehmigt, Ausschreibung läuft |
| M-002 | R-002 | Immutable Backups implementieren | A.8.13 (Information backup) | IT-Betrieb | Sehr hoch | 40 | 30.000 € | 2026-03-31 | In Arbeit | 60% | Pilotphase abgeschlossen |
| M-003 | R-003 | MFA für alle Benutzer ausrollen | A.5.17 (Authentication information) | IAM-Team | Sehr hoch | 30 | 15.000 € | 2026-02-28 | In Arbeit | 80% | 200 von 250 Benutzern migriert |
| M-004 | R-004 | Secret-Scanning Tool implementieren | A.8.24 (Use of cryptography) | Dev-Lead | Mittel | 15 | 10.000 € | 2026-04-30 | Geplant | 10% | Tool-Evaluierung: GitGuardian vs. Gitleaks |
| M-005 | R-005 | VPN-Hardening durchführen | A.5.14 (Information transfer) | IT-Betrieb | Mittel | 10 | 5.000 € | 2026-05-31 | Geplant | 0% | Hardening-Guide erstellen |



[TODO: Weitere Maßnahmen hinzufügen basierend auf Risikoregister]

### 2.2 Abgeschlossene Maßnahmen (Archiv)

| Maßnahme-ID | Risiko-ID | Maßnahme | Owner | Abschlussdatum | Ergebnis | Nachweis/Evidence |
|-------------|-----------|----------|-------|----------------|----------|-------------------|
| M-010 | R-020 | Patch CVE-2025-1234 installieren | IT-Betrieb | 2026-01-10 | Erfolgreich | Vulnerability Scan Report |
| M-011 | R-021 | Firewall-Konfiguration korrigieren | IT-Betrieb | 2026-01-15 | Erfolgreich | Firewall Audit Report |

[TODO: Abgeschlossene Maßnahmen archivieren]

## 3. Maßnahmenpriorisierung

### 3.1 Priorisierungskriterien

**Prioritätsstufen:**

| Priorität | Risikostufe | Compliance | Aufwand | Zeitrahmen |
|-----------|-------------|------------|---------|------------|
| **Sehr hoch** | Sehr hoch / Hoch | Kritisch | Egal | Sofort - 3 Monate |
| **Hoch** | Hoch / Mittel | Wichtig | Niedrig-Mittel | 3-6 Monate |
| **Mittel** | Mittel | Normal | Mittel | 6-12 Monate |
| **Niedrig** | Niedrig | Optional | Hoch | > 12 Monate |

**Priorisierungsformel:**
```
Priorität = (Risikoscore × 2) + Compliance-Faktor - Aufwand-Faktor

Compliance-Faktor:
- Kritisch (DSGVO, NIS2): +10
- Wichtig (ISO 27001): +5
- Normal: +0

Aufwand-Faktor:
- Niedrig (< 10 PT): -0
- Mittel (10-40 PT): -5
- Hoch (> 40 PT): -10
```

### 3.2 Quick Wins

**Quick Wins** sind Maßnahmen mit hohem Nutzen und niedrigem Aufwand:

| Maßnahme-ID | Maßnahme | Risikoreduktion | Aufwand | ROI |
|-------------|----------|-----------------|---------|-----|
| M-003 | MFA-Rollout | Hoch | Mittel | Hoch |
| M-005 | VPN-Hardening | Mittel | Niedrig | Sehr hoch |

**Empfehlung:** Quick Wins sollten priorisiert werden, um schnelle Sicherheitsverbesserungen zu erzielen.

## 4. Maßnahmendetails

### 4.1 Maßnahmenbeschreibung

Für jede Maßnahme sollten folgende Details dokumentiert werden:

**Maßnahme M-002: Immutable Backups implementieren**

**Beschreibung:**
Implementierung von unveränderlichen (immutable) Backups zum Schutz vor Ransomware. Backups werden in einem Write-Once-Read-Many (WORM) Format gespeichert und können nicht gelöscht oder modifiziert werden.

**Ziel:**
- Schutz vor Ransomware-Angriffen auf Backups
- Sicherstellung der Wiederherstellbarkeit bei Datenverlust
- Compliance mit DSGVO Art. 32 (Sicherheit der Verarbeitung)

**Scope:**
- Alle produktiven Systeme
- Kritische Datenbanken
- Kundendaten (DSGVO-relevant)

**Implementierungsschritte:**
1. Backup-Lösung evaluieren (Veeam, Commvault, AWS S3 Object Lock)
2. Pilotphase mit nicht-kritischen Systemen (✓ Abgeschlossen)
3. Rollout auf produktive Systeme (In Arbeit)
4. Restore-Tests durchführen
5. Dokumentation und Schulung

**Ressourcen:**
- Owner: IT-Betrieb
- Team: 2 Backup-Administratoren
- Aufwand: 40 Personentage
- Budget: 30.000 € (Lizenzen + Hardware)

**Abhängigkeiten:**
- Keine kritischen Abhängigkeiten

**Risiken der Umsetzung:**
- Erhöhter Speicherbedarf (Mitigation: Zusätzlicher Storage beschafft)
- Längere Backup-Zeiten (Mitigation: Backup-Fenster angepasst)

**Erfolgskriterien:**
- Alle kritischen Systeme haben immutable Backups
- Restore-Tests erfolgreich (RTO/RPO eingehalten)
- Keine Ransomware kann Backups löschen

**Nachweis/Evidence:**
- Backup-Konfigurationsdokumentation
- Restore-Test-Protokolle
- Compliance-Bericht



## 5. Control-Mapping (Annex A)

### 5.1 Verknüpfung zu Annex A Controls

Jede Maßnahme sollte mit relevanten Annex A Controls verknüpft werden:

| Maßnahme-ID | Annex A Control | Control-Name | Implementierungsstatus |
|-------------|-----------------|--------------|------------------------|
| M-001 | A.8.6 | Capacity management | Geplant |
| M-002 | A.8.13 | Information backup | In Arbeit |
| M-003 | A.5.17 | Authentication information | In Arbeit |
| M-004 | A.8.24 | Use of cryptography | Geplant |
| M-005 | A.5.14 | Information transfer | Geplant |

**Vollständiges Control-Mapping:**
- Siehe `0100_ISMS_Statement_of_Applicability_SoA_Template.md`
- Siehe `0710_Anhang_AnnexA_Mapping_Template.md`

### 5.2 Control-Implementierungsstatus

**Status-Definitionen:**

| Status | Beschreibung | Kriterien |
|--------|--------------|-----------|
| **Nicht implementiert** | Control ist nicht vorhanden | 0% Umsetzung |
| **Geplant** | Control ist geplant, aber noch nicht begonnen | Maßnahme im RTP |
| **In Arbeit** | Control wird gerade implementiert | 1-99% Umsetzung |
| **Implementiert** | Control ist vollständig implementiert | 100% Umsetzung, Evidence vorhanden |
| **Wirksam** | Control ist implementiert und nachweislich wirksam | Implementiert + Wirksamkeitsnachweis |

## 6. Ressourcenplanung und Budgetierung

### 6.1 Ressourcenübersicht

**Personelle Ressourcen:**

| Team/Rolle | Verfügbare Kapazität (PT/Monat) | Geplante Auslastung | Verfügbarkeit |
|------------|----------------------------------|---------------------|---------------|
| IT-Betrieb | 40 | 30 | 75% |
| Security Team | 20 | 18 | 90% |
| IAM-Team | 15 | 12 | 80% |
| Dev-Team | 10 | 5 | 50% |

**Finanzielle Ressourcen:**

| Quartal | Budget | Geplante Ausgaben | Verfügbar |
|---------|--------|-------------------|-----------|
| Q1 2026 | 50.000 € | 45.000 € | 5.000 € |
| Q2 2026 | 50.000 € | 55.000 € | -5.000 € (Überziehung) |
| Q3 2026 | 50.000 € | 30.000 € | 20.000 € |
| Q4 2026 | 50.000 € | 20.000 € | 30.000 € |

**Budgetanforderung:**
- Q2 2026: Zusätzliche 5.000 € für M-001 (Redundanter Switch)

### 6.2 Kapazitätsplanung

**Engpässe:**
- Security Team: 90% ausgelastet (kritisch)
- IAM-Team: 80% ausgelastet (hoch)

**Maßnahmen:**
- Priorisierung kritischer Maßnahmen
- Externe Unterstützung für M-004 (Secret-Scanning)
- Verschiebung nicht-kritischer Maßnahmen auf Q3/Q4

## 7. Abhängigkeiten und Risiken der Umsetzung

### 7.1 Abhängigkeiten zwischen Maßnahmen

```
M-002 (Immutable Backups)
  ↓ (benötigt)
M-001 (Redundanter Switch)
  ↓ (ermöglicht)
M-005 (VPN-Hardening)
```

**Kritischer Pfad:**
- M-002 muss vor M-001 abgeschlossen sein
- M-001 ist Voraussetzung für M-005

### 7.2 Risiken der Umsetzung

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|--------|-------------------|------------|------------|
| Ressourcenengpässe | Hoch | Mittel | Externe Unterstützung, Priorisierung |
| Budgetüberschreitung | Mittel | Mittel | Regelmäßiges Budget-Monitoring, Genehmigungsprozess |
| Technische Komplexität | Mittel | Hoch | Pilotphasen, externe Expertise |
| Widerstand gegen Änderungen | Niedrig | Mittel | Change Management, Awareness |

### 7.3 Change Management

**Kommunikation:**
- Regelmäßige Updates an Stakeholder
- Awareness-Kampagnen für betroffene Benutzer
- Schulungen für neue Controls

**Rollback-Planung:**
- Für jede Maßnahme Rollback-Plan erstellen
- Pilotphasen vor Produktiv-Rollout
- Backup vor kritischen Änderungen

## 8. Tracking und Reporting

### 8.1 Maßnahmen-Tracking

**Tracking-Frequenz:**
- Wöchentlich: Status-Update für kritische Maßnahmen
- Monatlich: Vollständiges RTP-Review
- Quartalsweise: Reporting an Informationssicherheitsgremium

**Tracking-Metriken:**
- Anzahl offener Maßnahmen
- Anzahl überfälliger Maßnahmen
- Durchschnittliche Umsetzungsdauer
- Budget-Auslastung

### 8.2 Reporting

**Monatliches Reporting:**
- Status aller aktiven Maßnahmen
- Fortschritt (% Completion)
- Risiken und Probleme
- Budget-Status

**Quartalsweises Reporting:**
- Zusammenfassung für Informationssicherheitsgremium
- Trend-Analyse
- Priorisierungsempfehlungen

**Eskalation:**
- Überfällige Maßnahmen (> 2 Wochen): Eskalation an CISO
- Kritische Verzögerungen: Eskalation an Geschäftsführung

## 9. Wirksamkeitsprüfung

### 9.1 Nachweis der Wirksamkeit

Für jede implementierte Maßnahme muss die Wirksamkeit nachgewiesen werden:

**Nachweismethoden:**
- **Technische Tests:** Vulnerability Scans, Penetration Tests, Configuration Audits
- **Prozess-Audits:** Internal Audits, Compliance Checks
- **Monitoring:** SIEM-Alerts, Log-Analyse, KPI-Tracking
- **Dokumentation:** Policies, Procedures, Training Records

**Beispiel M-002 (Immutable Backups):**
- Nachweis: Restore-Test-Protokoll
- Frequenz: Quartalsweise
- Kriterien: RTO/RPO eingehalten, Backups nicht modifizierbar

### 9.2 Evidence-Register

**Verknüpfung:**
- Siehe `0700_Anhang_Nachweisregister_Evidence.md`
- Jede Maßnahme hat verknüpfte Evidence

## 10. Rollen und Verantwortlichkeiten

### 10.1 RACI-Matrix: Risikobehandlung

| Aktivität | CISO | ISMS Manager | Maßnahmen-Owner | IT-Betrieb | Budget-Owner |
|-----------|------|--------------|-----------------|------------|--------------|
| RTP erstellen | A | R | C | C | I |
| Maßnahmen priorisieren | A | R | C | C | C |
| Maßnahmen umsetzen | A | C | R | R | I |
| Budget freigeben | C | I | I | I | A |
| Fortschritt tracken | A | R | C | I | I |
| Wirksamkeit prüfen | A | R | C | R | I |
| RTP-Review | A | R | C | C | I |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 11. Referenzen

### 11.1 Interne Dokumente

- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management Methodology
- `0070_ISMS_Risikoakzeptanzkriterien.md` - Risk Acceptance Criteria
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA
- `0360_Policy_Change_und_Release_Management.md` - Change Management
- `0700_Anhang_Nachweisregister_Evidence.md` - Evidence Register

### 11.2 Externe Standards

- **ISO/IEC 27001:2022** - Clause 6.1.3: Information security risk treatment
- **ISO/IEC 27002:2022** - Information security controls
- **ISO/IEC 27005:2022** - Information security risk management

## Änderungshistorie

| Version | Datum | Autor | Beschreibung | Genehmigt durch |
|---------|-------|-------|--------------|-----------------|
| 1.0 | [TODO] | [TODO] | Initiale Version | {{ meta-handbook.management_ceo }} |

**Genehmigt durch:**  
[TODO], CISO  
Datum: [TODO]

**Nächster Review:** [TODO] (Monatlich)

