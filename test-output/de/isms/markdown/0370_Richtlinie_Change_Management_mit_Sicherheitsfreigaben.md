# Richtlinie: Change Management mit Sicherheitsfreigaben

**Dokument-ID:** ISMS-0370
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0360_Policy_Change_und_Release_Management.md` und definiert:
- Change-Management-Prozesse mit Sicherheitsprüfungen
- Change-Kategorien und Genehmigungsworkflows
- Rollback-Verfahren und Post-Implementation-Reviews

**Geltungsbereich:** Alle IT-Änderungen bei **AdminSend GmbH**

## 2. Change-Kategorien

### 2.1 Standard Changes
**Definition:** Vorab genehmigte, risikoarme, häufige Änderungen

**Beispiele:**
- Passwort-Resets
- Software-Updates (getestet)
- Hinzufügen von Nutzern zu Standardgruppen

**Genehmigung:** Keine individuelle Genehmigung erforderlich  
**Sicherheitsprüfung:** Nicht erforderlich

### 2.2 Normal Changes
**Definition:** Geplante Änderungen mit mittlerem Risiko

**Beispiele:**
- Konfigurationsänderungen
- Software-Installationen
- Netzwerk-Änderungen

**Genehmigung:** Change Advisory Board (CAB)  
**Sicherheitsprüfung:** Bei sicherheitsrelevanten Änderungen

### 2.3 Emergency Changes
**Definition:** Ungeplante, dringende Änderungen

**Beispiele:**
- Kritische Security-Patches
- Systemausfälle
- Aktive Sicherheitsvorfälle

**Genehmigung:** Emergency CAB (ECAB)  
**Sicherheitsprüfung:** Nachträglich

## 3. Change-Management-Prozess

### 3.1 Change Request (RFC)

**Pflichtfelder:**
- Change-Titel und Beschreibung
- Begründung (Business Justification)
- Betroffene Systeme und Services
- Risikobewertung
- Rollback-Plan
- Test-Ergebnisse
- Geplantes Zeitfenster

**Sicherheitsrelevante Zusatzfelder:**
- Auswirkungen auf Sicherheitskontrollen
- Änderungen an Firewall-Regeln
- Neue externe Verbindungen
- Privilegierte Zugriffe erforderlich

### 3.2 Risikobewertung

**Risiko-Matrix:**
| Wahrscheinlichkeit | Auswirkung Niedrig | Auswirkung Mittel | Auswirkung Hoch |
|--------------------|-------------------|-------------------|-----------------|
| Niedrig | Niedrig | Niedrig | Mittel |
| Mittel | Niedrig | Mittel | Hoch |
| Hoch | Mittel | Hoch | Kritisch |

**Auswirkungen:**
- **Niedrig:** Einzelner Nutzer betroffen
- **Mittel:** Abteilung betroffen
- **Hoch:** Gesamte Organisation betroffen

### 3.3 Sicherheitsprüfung

**Trigger:**
- Änderungen an Sicherheitssystemen (Firewall, IDS, etc.)
- Neue externe Verbindungen
- Privilegierte Zugriffe
- Änderungen an Authentifizierung/Autorisierung
- Risiko "Hoch" oder "Kritisch"

**Prüfung durch IT-Security:**
- Review des Change Requests
- Sicherheitsauswirkungen bewerten
- Zusätzliche Kontrollen empfehlen
- Genehmigung oder Ablehnung

**SLA:** Sicherheitsprüfung innerhalb 2 Arbeitstagen

### 3.4 Change Advisory Board (CAB)

**Mitglieder:**
- Change Manager (Vorsitz)
- IT-Betrieb
- IT-Security (bei sicherheitsrelevanten Changes)
- Application Owner (bei Anwendungsänderungen)
- Business Representative

**Frequenz:** Wöchentlich (Dienstag 10:00 Uhr)

**Aufgaben:**
- Review und Genehmigung von Normal Changes
- Priorisierung bei Konflikten
- Risikobewertung
- Terminplanung

### 3.5 Implementation

**Pre-Implementation:**
- Backup erstellen
- Rollback-Plan bereitstellen
- Kommunikation an betroffene Nutzer
- Monitoring vorbereiten

**Implementation:**
- Änderung gemäß Plan durchführen
- Dokumentation aller Schritte
- Abweichungen dokumentieren

**Post-Implementation:**
- Funktionstest
- Monitoring auf Fehler (24 Stunden)
- Change-Status aktualisieren
- Dokumentation vervollständigen

### 3.6 Rollback

**Trigger:**
- Funktionstest fehlgeschlagen
- Kritische Fehler in Produktion
- Sicherheitsprobleme erkannt

**Prozess:**
1. Rollback-Entscheidung durch Change Manager
2. Rollback gemäß Rollback-Plan
3. Verifizierung der Wiederherstellung
4. Root-Cause-Analyse
5. Neuer Change Request für erneuten Versuch

## 4. Emergency Changes

### 4.1 Emergency CAB (ECAB)

**Mitglieder:**
- Change Manager oder Stellvertreter
- IT-Betrieb (On-Call)
- CISO oder IT-Security (On-Call)

**Verfügbarkeit:** 24/7

**Genehmigungsprozess:**
- Telefonische oder E-Mail-Genehmigung
- Dokumentation im Nachhinein
- Review im nächsten regulären CAB

### 4.2 Emergency Change-Prozess

**Beschleunigter Workflow:**
1. **Initiierung:** Incident-Manager erstellt Emergency RFC
2. **Bewertung:** ECAB bewertet Dringlichkeit und Risiko
3. **Genehmigung:** ECAB genehmigt (oder lehnt ab)
4. **Implementation:** Sofortige Durchführung
5. **Dokumentation:** Nachträgliche Vervollständigung
6. **Review:** Im nächsten CAB

**Sicherheitsprüfung:**
- Bei kritischen Security-Patches: Nachträglich
- Bei anderen Emergency Changes: Vor Implementation (wenn möglich)

## 5. Sicherheitskontrollen

### 5.1 Segregation of Duties

**Prinzip:** Keine Person darf Change anfordern, genehmigen und implementieren

**Rollen:**
- **Requester:** Beantragt Change
- **Approver:** Genehmigt Change (CAB)
- **Implementer:** Führt Change durch
- **Reviewer:** Prüft Post-Implementation

### 5.2 Privilegierte Changes

**Zusätzliche Anforderungen:**
- Vier-Augen-Prinzip bei Implementation
- Session-Recording
- Detaillierte Dokumentation
- Post-Implementation-Security-Review

### 5.3 Firewall-Changes

**Spezielle Anforderungen:**
- Begründung für jede neue Regel
- Quell- und Ziel-IP/Port dokumentieren
- Zeitliche Befristung (wo möglich)
- Regelmäßiger Review (quartalsweise)

**Genehmigung:**
- IT-Security: Verpflichtend
- Network-Team: Technische Umsetzbarkeit
- Application Owner: Business Justification

## 6. Testing und Validation

### 6.1 Test-Umgebungen

**Anforderungen:**
- Dev/Test-Umgebung für alle kritischen Systeme
- Möglichst identisch zu Produktion
- Isoliert von Produktion

**Test-Prozess:**
1. Change in Dev/Test implementieren
2. Funktionstest durchführen
3. Performance-Test (bei Bedarf)
4. Security-Test (bei sicherheitsrelevanten Changes)
5. Dokumentation der Test-Ergebnisse

### 6.2 Security Testing

**Bei sicherheitsrelevanten Changes:**
- Vulnerability-Scan nach Change
- Penetration-Test (bei kritischen Änderungen)
- Code-Review (bei Software-Changes)
- Configuration-Review

## 7. Dokumentation und Audit

### 7.1 Change-Dokumentation

**Pflicht-Dokumentation:**
- Change Request (RFC)
- Genehmigungen
- Implementation-Log
- Test-Ergebnisse
- Post-Implementation-Review

**Aufbewahrung:** {{ meta-handbook.retention_change_years }} Jahre

### 7.2 Post-Implementation Review (PIR)

**Durchführung:**
- Innerhalb 7 Tage nach Implementation
- Bei allen Normal und Emergency Changes

**Inhalte:**
- Erfolg der Implementation
- Aufgetretene Probleme
- Lessons Learned
- Verbesserungsvorschläge

### 7.3 Compliance und Audit

**Messgrößen (KPIs):**
| Metrik | Zielwert |
|--------|----------|
| Erfolgreiche Changes | > 95% |
| Emergency Changes | < 10% aller Changes |
| Unauthorized Changes | 0 |
| PIR-Completion-Rate | 100% |

**Audit-Nachweise:**
- Change-Logs
- Genehmigungen
- Sicherheitsprüfungen
- PIR-Berichte

## 8. Referenzen

### Interne Dokumente
- `0360_Policy_Change_und_Release_Management.md`
- `0400_Policy_Incident_Management.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.32** - Change management
- **ITIL 4** - Change Enablement Practice

**Genehmigt durch:** [TODO], CISO  
**Nächster Review:** [TODO]

