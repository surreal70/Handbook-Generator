
Document-ID: dora-0220

Status: Draft
Classification: Internal

# Value Stream Mapping

**Dokument-ID:** [FRAMEWORK]-0220
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

## Zweck

Dieses Dokument beschreibt die Anwendung von Value Stream Mapping zur Visualisierung und Optimierung des Software-Delivery-Prozesses.

## Umfang

- Value Stream Mapping Grundlagen
- Prozess-Mapping-Methodik
- Identifikation von Verschwendung
- Optimierungsansätze

## Organisationsinformationen

- **Organisation**: [TODO]
- **VSM-Verantwortlicher**: [TODO]
- **Mapping-Frequenz**: [TODO]

## Value Stream Mapping Grundlagen

### Definition

Value Stream Mapping ist eine Lean-Management-Methode zur Visualisierung und Analyse des Material- und Informationsflusses, der erforderlich ist, um ein Produkt oder eine Dienstleistung zum Kunden zu bringen.

### Ziele

- **Transparenz**: Sichtbarmachung des gesamten Prozesses
- **Verschwendung identifizieren**: Nicht-wertschöpfende Aktivitäten erkennen
- **Bottlenecks finden**: Engpässe im Prozess lokalisieren
- **Verbesserungen priorisieren**: Fokus auf größte Hebel

## Prozess-Mapping-Methodik

### Schritt 1: Prozess-Schritte identifizieren

**Typische Schritte im Software-Delivery**:
1. Anforderungsanalyse
2. Design
3. Implementierung
4. Code Review
5. Build
6. Automatisierte Tests
7. Manuelle Tests
8. Security Scan
9. Approval
10. Deployment
11. Verification

### Schritt 2: Zeiten erfassen

**Für jeden Schritt erfassen**:
- **Process Time**: Aktive Bearbeitungszeit
- **Wait Time**: Wartezeit bis zum nächsten Schritt
- **Lead Time**: Gesamtzeit (Process + Wait)

**Beispiel**:
```
Schritt: Code Review
- Process Time: 2 Stunden
- Wait Time: 16 Stunden (Warten auf Reviewer)
- Lead Time: 18 Stunden
```

### Schritt 3: Value Stream Map erstellen

**Visualisierung**:
```
[Commit] → [Build: 10min] → [Wait: 2h] → [Test: 30min] → [Wait: 4h] → 
[Review: 2h] → [Wait: 16h] → [Approval: 1h] → [Wait: 8h] → [Deploy: 15min]

Total Process Time: 3h 55min
Total Wait Time: 30h
Total Lead Time: 33h 55min
```

### Schritt 4: Metriken berechnen

**Process Efficiency**:
```
Efficiency = Process Time / Lead Time × 100%
Efficiency = 3.92h / 33.92h × 100% = 11.6%
```

**Value-Added Ratio**:
```
VA Ratio = Value-Added Time / Total Time × 100%
```

## Verschwendungsarten (Muda)

### 1. Waiting (Warten)

**Beispiele**:
- Warten auf Code Reviews
- Warten auf Approvals
- Warten auf Test-Umgebungen
- Warten auf Deployment-Windows

**Lösungsansätze**:
- Automatisierte Approvals
- Self-Service-Umgebungen
- On-Demand Deployments
- Asynchrone Reviews

### 2. Overprocessing (Überbearbeitung)

**Beispiele**:
- Redundante Approvals
- Doppelte Tests
- Unnötige Dokumentation
- Übermäßige Meetings

**Lösungsansätze**:
- Prozess-Streamlining
- Automatisierung
- Standardisierung
- Lean Documentation

### 3. Defects (Fehler)

**Beispiele**:
- Bugs in Production
- Failed Deployments
- Rollbacks
- Rework

**Lösungsansätze**:
- Test-Automatisierung
- Shift-Left Testing
- Quality Gates
- Continuous Monitoring

### 4. Motion (Bewegung)

**Beispiele**:
- Context-Switching
- Tool-Wechsel
- Informationssuche
- Handoffs zwischen Teams

**Lösungsansätze**:
- Integrierte Toolchains
- Single Source of Truth
- Cross-funktionale Teams
- Automatisierte Workflows

## Bottleneck-Identifikation

### Analyse-Methoden

**Warteschlangen-Analyse**:
- Wo sammeln sich Aufgaben?
- Welche Schritte haben die längsten Wartezeiten?

**Durchsatz-Analyse**:
- Welche Schritte limitieren den Durchsatz?
- Wo ist die Kapazität am geringsten?

**Variabilität-Analyse**:
- Welche Schritte haben hohe Schwankungen?
- Wo ist die Vorhersagbarkeit am niedrigsten?

### Priorisierung

**Impact-Effort-Matrix**:
```
High Impact, Low Effort → Sofort umsetzen
High Impact, High Effort → Planen und umsetzen
Low Impact, Low Effort → Bei Gelegenheit
Low Impact, High Effort → Vermeiden
```

## Optimierungsansätze

### Kurzfristige Maßnahmen

1. **Wartezeiten reduzieren**
   - Automatisierte Notifications
   - SLA für Reviews
   - Parallele Prozesse

2. **Batch-Größen reduzieren**
   - Kleinere Pull Requests
   - Häufigere Deployments
   - Continuous Integration

3. **Automatisierung erhöhen**
   - Automatisierte Tests
   - Automatisierte Deployments
   - Automatisierte Approvals

### Langfristige Maßnahmen

1. **Prozess-Redesign**
   - Elimination unnötiger Schritte
   - Parallelisierung
   - Self-Service-Modelle

2. **Organisationsstruktur**
   - Cross-funktionale Teams
   - Reduzierung von Handoffs
   - Erhöhte Autonomie

3. **Technologie-Modernisierung**
   - Moderne CI/CD-Plattformen
   - Cloud-Infrastruktur
   - Microservices-Architektur

## Continuous Improvement

### Regelmäßige VSM-Sessions

**Frequenz**: [TODO]

**Teilnehmer**:
- Entwickler
- Operations
- Product Owner
- QA

**Agenda**:
1. Aktuellen Value Stream reviewen
2. Metriken analysieren
3. Verbesserungen identifizieren
4. Maßnahmen priorisieren
5. Umsetzung planen

### Erfolgsmessung

**KPIs**:
- Lead Time Reduction
- Process Efficiency Improvement
- Wait Time Reduction
- Throughput Increase

<!-- Hinweis: VSM macht Verschwendung sichtbar und ermöglicht gezielte Optimierung -->

