# Change und Release Management

## Zweck und Geltungsbereich

Dieses Dokument beschreibt die Change- und Release-Management-Prozesse für AdminSend GmbH gemäß ITIL v4 Best Practices. Es definiert Change-Kategorien, Genehmigungsprozesse, Release-Strategien und Rollback-Prozeduren zur kontrollierten Durchführung von Änderungen an IT-Services und -Systemen.

**Geltungsbereich:** Alle IT-Services, Systeme und Infrastruktur-Komponenten von AdminSend GmbH

**Verantwortlich:** Andreas Huemmer (andreas.huemmer@adminsend.de)

## Change Management

### Change-Definition

Ein **Change** ist das Hinzufügen, Ändern oder Entfernen von etwas, das direkte oder indirekte Auswirkungen auf Services haben könnte. Das Ziel des Change Managements ist die Minimierung von Risiken bei gleichzeitiger Maximierung des Business-Value.

### Change-Prinzipien

**Kernprinzipien:**
- **Kontrolliert:** Alle Changes durchlaufen definierte Prozesse
- **Dokumentiert:** Vollständige Dokumentation aller Changes
- **Genehmigt:** Autorisierung vor Implementierung
- **Getestet:** Validierung vor Produktiv-Deployment
- **Rückgängig machbar:** Rollback-Plan für jeden Change

### Change-Kategorien

#### Standard Change

**Definition:** Vorab genehmigte, risikoarme, häufig durchgeführte Changes mit dokumentierter Prozedur.

**Eigenschaften:**
- Niedriges Risiko
- Bekannte Prozedur
- Vorab-Genehmigung durch CAB
- Keine individuelle Genehmigung erforderlich
- Dokumentierte Runbooks

**Beispiele:**
- Passwort-Reset
- Benutzer-Anlage/Löschung
- Standard-Software-Installation
- Backup-Restore (nicht-kritisch)
- Zertifikats-Erneuerung
- Routine-Patches (getestet)

**Genehmigung:** Automatisch (vorab genehmigt)

**Bearbeitungszeit:** Sofort bis 24 Stunden

#### Normal Change

**Definition:** Changes, die individuelle Bewertung, Genehmigung und Planung erfordern.

**Eigenschaften:**
- Mittleres bis hohes Risiko
- Individuelle Bewertung erforderlich
- CAB-Genehmigung erforderlich
- Detaillierte Planung
- Test-Phase erforderlich

**Beispiele:**
- Neue Software-Deployments
- Infrastruktur-Änderungen
- Netzwerk-Rekonfigurationen
- Datenbank-Schema-Änderungen
- Major-Version-Upgrades
- Neue Service-Einführungen

**Genehmigung:** Change Advisory Board (CAB)

**Bearbeitungszeit:** 1-4 Wochen (abhängig von Komplexität)

#### Emergency Change

**Definition:** Dringende Changes zur Behebung von kritischen Incidents oder Sicherheitsproblemen.

**Eigenschaften:**
- Hohe Dringlichkeit
- Verkürzte Genehmigungsprozesse
- Minimale Dokumentation vor Implementierung
- Nachträgliche vollständige Dokumentation
- Emergency CAB (ECAB) Genehmigung

**Beispiele:**
- Security-Patches (Zero-Day)
- Kritische Bugfixes
- Disaster-Recovery-Maßnahmen
- Service-Wiederherstellung
- Sicherheitsvorfälle

**Genehmigung:** Emergency CAB (ECAB) oder CIO

**Bearbeitungszeit:** Sofort bis 4 Stunden

### Change-Prozess

#### Prozessübersicht

```
┌─────────────────┐
│ Change Request  │
│ Creation        │
└────────┬────────┘
         │
┌────────▼────────┐
│ Change          │
│ Assessment      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Change          │
│ Authorization   │
│ (CAB)           │
└────────┬────────┘
         │
┌────────▼────────┐
│ Change          │
│ Planning        │
└────────┬────────┘
         │
┌────────▼────────┐
│ Change          │
│ Implementation  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Change          │
│ Review          │
└────────┬────────┘
         │
┌────────▼────────┐
│ Change          │
│ Closure         │
└─────────────────┘
```

#### 1. Change Request Creation

**Erforderliche Informationen:**
- **Change-ID:** Automatisch generiert
- **Titel:** Kurzbeschreibung
- **Beschreibung:** Detaillierte Beschreibung der Änderung
- **Begründung:** Business-Reason, Problem-Referenz
- **Kategorie:** Standard / Normal / Emergency
- **Betroffene Services:** Service-Liste
- **Betroffene CIs:** Configuration Items
- **Risiko-Bewertung:** Niedrig / Mittel / Hoch
- **Implementierungs-Plan:** Schritt-für-Schritt-Anleitung
- **Rollback-Plan:** Rückgängig-Machung
- **Test-Plan:** Validierungs-Schritte
- **Zeitfenster:** Geplantes Wartungsfenster
- **Requester:** Antragsteller
- **Implementer:** Durchführender

**Tool:** {{ meta.ticketing_system }}

**Verantwortlich:** Change Requester

#### 2. Change Assessment

**Bewertungs-Kriterien:**
- **Impact:** Auswirkung auf Services und Nutzer
- **Risiko:** Wahrscheinlichkeit und Schwere von Problemen
- **Komplexität:** Technische Komplexität
- **Abhängigkeiten:** Betroffene Systeme und Services
- **Ressourcen:** Erforderliche Skills und Zeit

**Risiko-Matrix:**

|  | **Impact: Niedrig** | **Impact: Mittel** | **Impact: Hoch** |
|---|---|---|---|
| **Wahrscheinlichkeit: Niedrig** | Niedriges Risiko | Mittleres Risiko | Mittleres Risiko |
| **Wahrscheinlichkeit: Mittel** | Mittleres Risiko | Mittleres Risiko | Hohes Risiko |
| **Wahrscheinlichkeit: Hoch** | Mittleres Risiko | Hohes Risiko | Sehr hohes Risiko |

**Verantwortlich:** Change Manager

#### 3. Change Authorization (CAB)

**Change Advisory Board (CAB):**

**Mitglieder:**
- **Chair:** Andreas Huemmer (Change Manager)
- **CIO:** Anna Schmidt
- **CISO:** Thomas Weber
- **Service Owner:** [Service-abhängig]
- **Technical Leads:** [Change-abhängig]
- **Business Representatives:** [Bei Business-Impact]

**CAB-Meeting:**
- **Frequenz:** Wöchentlich (Dienstag 10:00)
- **Dauer:** 60 Minuten
- **Agenda:** Review aller Normal Changes
- **Entscheidung:** Genehmigen / Ablehnen / Zurückstellen

**Emergency CAB (ECAB):**
- **Mitglieder:** CIO, Change Manager, Technical Lead
- **Einberufung:** Ad-hoc bei Emergency Changes
- **Entscheidung:** Innerhalb 1 Stunde

**Genehmigungskriterien:**
- Vollständige Dokumentation
- Akzeptables Risiko
- Ressourcen verfügbar
- Test-Plan vorhanden
- Rollback-Plan vorhanden
- Wartungsfenster verfügbar

#### 4. Change Planning

**Planungs-Aktivitäten:**
- Detaillierte Implementierungs-Schritte
- Ressourcen-Allokation
- Zeitplan erstellen
- Kommunikations-Plan
- Test-Szenarien definieren
- Rollback-Trigger definieren

**Change-Kalender:**
- Alle geplanten Changes visualisieren
- Konflikte identifizieren
- Wartungsfenster koordinieren
- Stakeholder informieren

**Verantwortlich:** Change Implementer, Change Manager

#### 5. Change Implementation

**Pre-Implementation:**
- Backup erstellen
- Rollback-Prozedur bereitstellen
- Team-Briefing durchführen
- Stakeholder informieren

**Implementation:**
- Implementierungs-Plan Schritt-für-Schritt ausführen
- Fortschritt dokumentieren
- Bei Problemen: Rollback-Trigger prüfen

**Post-Implementation:**
- Funktionalität testen
- Monitoring prüfen
- Stakeholder informieren
- Dokumentation aktualisieren

**Verantwortlich:** Change Implementer

#### 6. Change Review

**Review-Aktivitäten:**
- Erfolg der Implementierung bewerten
- Abweichungen vom Plan dokumentieren
- Lessons Learned identifizieren
- Metriken erfassen (Dauer, Downtime, etc.)

**Review-Kriterien:**
- Change erfolgreich implementiert?
- Rollback erforderlich gewesen?
- Unerwartete Probleme aufgetreten?
- Zeitplan eingehalten?
- Dokumentation vollständig?

**Verantwortlich:** Change Manager

#### 7. Change Closure

**Closure-Aktivitäten:**
- Dokumentation finalisieren
- CMDB aktualisieren
- Change-Ticket schließen
- Metriken in Reporting aufnehmen

**Verantwortlich:** Change Manager

### Wartungsfenster

**Standard-Wartungsfenster:**

| Typ | Zeitfenster | Frequenz | Genehmigung |
|---|---|---|---|
| **Routine** | Dienstag 22:00-02:00 | Wöchentlich | Standard Changes |
| **Geplant** | Samstag 20:00-06:00 | Monatlich | Normal Changes |
| **Emergency** | Jederzeit | Ad-hoc | Emergency Changes |

**Wartungsfenster-Regeln:**
- Minimale Service-Unterbrechung
- Nutzer-Benachrichtigung 48h vorher
- Rollback-Zeit einplanen (50% der Implementierungszeit)
- Keine Changes während Business-Critical-Zeiten

### Rollback-Prozeduren

**Rollback-Trigger:**
- Kritische Fehler während Implementation
- Service-Verfügbarkeit < SLA
- Unerwartete Auswirkungen auf andere Services
- Test-Validierung fehlgeschlagen
- Change Manager Entscheidung

**Rollback-Plan-Anforderungen:**
- Schritt-für-Schritt-Anleitung
- Geschätzte Rollback-Dauer
- Erforderliche Ressourcen
- Daten-Wiederherstellung (falls erforderlich)
- Validierungs-Schritte

**Rollback-Prozess:**
1. Rollback-Entscheidung treffen
2. Stakeholder informieren
3. Rollback-Plan ausführen
4. System-Status validieren
5. Incident-Ticket erstellen (falls erforderlich)
6. Post-Rollback-Review durchführen

## Release Management

### Release-Definition

Ein **Release** ist eine Sammlung von Hardware, Software, Dokumentation, Prozessen oder anderen Komponenten, die erforderlich sind, um eine oder mehrere genehmigte Changes zu implementieren.

### Release-Typen

#### Major Release

**Definition:** Signifikante neue Funktionalität oder Architektur-Änderungen

**Eigenschaften:**
- Große Änderungen
- Umfangreiche Tests erforderlich
- Lange Planungsphase
- Hohes Risiko
- Umfangreiche Dokumentation

**Beispiele:**
- Neue Software-Version (z.B. v2.0.0)
- Plattform-Migration
- Architektur-Redesign

**Frequenz:** Quartalsweise oder halbjährlich

**Genehmigung:** CAB + Management

#### Minor Release

**Definition:** Neue Features oder Verbesserungen ohne Architektur-Änderungen

**Eigenschaften:**
- Moderate Änderungen
- Standard-Tests
- Mittleres Risiko
- Abwärtskompatibel

**Beispiele:**
- Feature-Releases (z.B. v1.1.0)
- Performance-Verbesserungen
- Neue Integrationen

**Frequenz:** Monatlich

**Genehmigung:** CAB

#### Patch Release

**Definition:** Bugfixes und Security-Patches

**Eigenschaften:**
- Kleine Änderungen
- Fokus auf Stabilität
- Niedriges Risiko
- Schnelle Implementierung

**Beispiele:**
- Bugfix-Releases (z.B. v1.0.1)
- Security-Patches
- Hotfixes

**Frequenz:** Bei Bedarf (wöchentlich)

**Genehmigung:** Change Manager

### Release-Prozess

#### Prozessübersicht

```
┌─────────────────┐
│ Release         │
│ Planning        │
└────────┬────────┘
         │
┌────────▼────────┐
│ Release         │
│ Build           │
└────────┬────────┘
         │
┌────────▼────────┐
│ Release         │
│ Testing         │
└────────┬────────┘
         │
┌────────▼────────┐
│ Release         │
│ Deployment      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Release         │
│ Review          │
└─────────────────┘
```

#### 1. Release Planning

**Planungs-Aktivitäten:**
- Release-Scope definieren
- Changes für Release auswählen
- Release-Zeitplan erstellen
- Ressourcen planen
- Risiko-Assessment durchführen
- Kommunikations-Plan erstellen

**Release-Scope:**
- Inkludierte Changes
- Neue Features
- Bugfixes
- Abhängigkeiten
- Ausschlüsse

**Verantwortlich:** Release Manager

#### 2. Release Build

**Build-Aktivitäten:**
- Code-Integration
- Automatisierte Builds (CI/CD)
- Artefakt-Erstellung
- Versionierung
- Build-Dokumentation

**Build-Pipeline:**
1. Code-Commit
2. Automatische Tests (Unit, Integration)
3. Code-Quality-Checks (Linting, Security-Scan)
4. Build-Artefakt erstellen
5. Artefakt in Repository speichern

**Verantwortlich:** DevOps-Team

#### 3. Release Testing

**Test-Phasen:**

| Phase | Umgebung | Fokus | Dauer |
|---|---|---|---|
| **Unit Tests** | Dev | Code-Funktionalität | Automatisch |
| **Integration Tests** | Dev | Komponenten-Integration | Automatisch |
| **System Tests** | Test | Gesamtsystem | 1-2 Tage |
| **UAT** | Staging | Business-Anforderungen | 3-5 Tage |
| **Performance Tests** | Staging | Last und Performance | 1-2 Tage |
| **Security Tests** | Staging | Sicherheit | 1-2 Tage |

**Test-Kriterien:**
- Alle Tests bestanden
- Keine kritischen Bugs
- Performance-Ziele erreicht
- Security-Scan ohne High-Findings
- UAT-Abnahme durch Business

**Verantwortlich:** QA-Team, Business-Users

#### 4. Release Deployment

**Deployment-Strategien:**

##### Blue-Green Deployment

**Beschreibung:** Zwei identische Produktions-Umgebungen (Blue und Green). Neue Version wird in inaktiver Umgebung deployed, dann Traffic umgeschaltet.

**Vorteile:**
- Zero-Downtime
- Schneller Rollback
- Vollständige Tests in Prod-Umgebung

**Nachteile:**
- Doppelte Infrastruktur-Kosten
- Datenbank-Migrationen komplex

**Anwendung:** Kritische Services mit hohen Verfügbarkeits-Anforderungen

##### Canary Deployment

**Beschreibung:** Neue Version wird schrittweise für einen kleinen Prozentsatz der Nutzer ausgerollt, dann graduell erhöht.

**Vorteile:**
- Risiko-Minimierung
- Frühe Fehler-Erkennung
- Graduelles Rollout

**Nachteile:**
- Komplexe Traffic-Steuerung
- Längere Deployment-Dauer

**Anwendung:** Services mit großer Nutzerbasis

##### Rolling Deployment

**Beschreibung:** Neue Version wird schrittweise auf Server-Instanzen deployed, während alte Version weiterläuft.

**Vorteile:**
- Keine zusätzliche Infrastruktur
- Graduelles Rollout
- Automatisierbar

**Nachteile:**
- Temporäre Versions-Inkonsistenz
- Komplexe Rollbacks

**Anwendung:** Standard-Deployments mit Load-Balancing

##### Big Bang Deployment

**Beschreibung:** Alle Komponenten werden gleichzeitig aktualisiert.

**Vorteile:**
- Einfach
- Schnell
- Keine Versions-Inkonsistenz

**Nachteile:**
- Downtime erforderlich
- Hohes Risiko
- Komplexe Rollbacks

**Anwendung:** Nur für unkritische Services oder mit Wartungsfenster

**Deployment-Checkliste:**
- [ ] Backup erstellt
- [ ] Rollback-Plan bereit
- [ ] Monitoring aktiviert
- [ ] Stakeholder informiert
- [ ] Team verfügbar
- [ ] Deployment-Runbook geprüft
- [ ] Change-Ticket genehmigt

**Verantwortlich:** DevOps-Team, Release Manager

#### 5. Release Review

**Review-Aktivitäten:**
- Deployment-Erfolg bewerten
- Metriken analysieren
- Lessons Learned dokumentieren
- Verbesserungen identifizieren

**Review-Metriken:**
- Deployment-Dauer
- Downtime (falls vorhanden)
- Anzahl Rollbacks
- Post-Deployment-Incidents
- User-Feedback

**Verantwortlich:** Release Manager

### CI/CD Pipeline

**Continuous Integration (CI):**
- Automatische Builds bei Code-Commit
- Automatische Tests (Unit, Integration)
- Code-Quality-Checks
- Security-Scans
- Artefakt-Erstellung

**Continuous Deployment (CD):**
- Automatisches Deployment in Dev/Test
- Manuelles Deployment in Staging/Prod
- Automatische Rollbacks bei Fehlern
- Deployment-Monitoring

**Pipeline-Tools:**
- **CI/CD-System:** {{ meta.cicd_system }}
- **Version Control:** {{ meta.version_control }}
- **Artefakt-Repository:** {{ meta.artifact_repository }}
- **Container-Registry:** {{ meta.container_registry }}

## Metriken und Reporting

### Change-Management-Metriken

| Metrik | Zielwert | Messung |
|---|---|---|
| **Change Success Rate** | > 95% | Erfolgreiche Changes / Gesamt-Changes |
| **Emergency Change Rate** | < 5% | Emergency Changes / Gesamt-Changes |
| **Change-Related Incidents** | < 10% | Incidents durch Changes / Gesamt-Incidents |
| **CAB Approval Rate** | > 90% | Genehmigte Changes / Eingereichte Changes |
| **Rollback Rate** | < 5% | Rollbacks / Implementierte Changes |

### Release-Management-Metriken

| Metrik | Zielwert | Messung |
|---|---|---|
| **Release Frequency** | Monatlich | Anzahl Releases pro Monat |
| **Lead Time** | < 2 Wochen | Zeit von Commit bis Produktion |
| **Deployment Frequency** | Wöchentlich | Anzahl Deployments pro Woche |
| **Mean Time to Recovery** | < 1 Stunde | Durchschnittliche Wiederherstellungszeit |
| **Change Failure Rate** | < 15% | Fehlgeschlagene Deployments / Gesamt |

### Reporting

**Wöchentliches Change-Report:**
- Anzahl Changes (nach Kategorie)
- Geplante Changes (nächste Woche)
- Change-Kalender
- Offene Change-Requests

**Monatliches Release-Report:**
- Release-Übersicht
- Deployment-Statistiken
- Metriken-Dashboard
- Verbesserungs-Maßnahmen

## Rollen und Verantwortlichkeiten

### Change Manager

**Verantwortlichkeiten:**
- Change-Prozess-Ownership
- CAB-Moderation
- Change-Assessment
- Change-Kalender-Verwaltung
- Reporting

**Person:** Andreas Huemmer

### Release Manager

**Verantwortlichkeiten:**
- Release-Planung
- Release-Koordination
- Deployment-Oversight
- Release-Dokumentation

**Person:** [Name]

### Change Advisory Board (CAB)

**Verantwortlichkeiten:**
- Change-Bewertung
- Change-Genehmigung
- Risiko-Assessment
- Priorisierung

**Mitglieder:** Siehe Abschnitt "Change Authorization"

## Tools und Systeme

### Change-Management-Tool
- **System:** {{ meta.ticketing_system }}
- **URL:** {{ meta.ticketing_system_url }}
- **Zugriff:** Alle IT-Mitarbeiter

### CI/CD-Pipeline
- **System:** {{ meta.cicd_system }}
- **URL:** {{ meta.cicd_url }}
- **Zugriff:** DevOps-Team

### Version Control
- **System:** {{ meta.version_control }}
- **URL:** {{ meta.version_control_url }}
- **Zugriff:** Development-Team

## Referenzen

- ITIL v4 Foundation - Change Enablement
- ITIL v4 Foundation - Release Management
- ISO/IEC 20000-1:2018 - Change Management
- DevOps Handbook - Deployment Strategies
- Site Reliability Engineering (SRE) - Release Engineering

---

**Dokumentverantwortlicher:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.date }}
