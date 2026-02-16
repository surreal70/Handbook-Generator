---
Document-ID: dora-0230
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Bottleneck-Identifikation

## Zweck

Dieses Dokument beschreibt Methoden zur Identifikation und Analyse von Bottlenecks im Software-Delivery-Prozess.

## Umfang

- Bottleneck-Analyse-Methoden
- Datenerfassung und -analyse
- Priorisierung von Engpässen
- Lösungsansätze

## Organisationsinformationen

- **Organisation**: {{ source.organization_name }}
- **Analyse-Verantwortlicher**: {{ source.bottleneck_analysis_owner }}

## Bottleneck-Analyse-Methoden

### Theory of Constraints

**Grundprinzip**: Der Durchsatz eines Systems wird durch seinen schwächsten Punkt (Bottleneck) bestimmt.

**5-Schritte-Prozess**:
1. Identifiziere den Bottleneck
2. Nutze den Bottleneck optimal aus
3. Ordne alles dem Bottleneck unter
4. Erweitere den Bottleneck
5. Wiederhole den Prozess

### Warteschlangen-Theorie

**Little's Law**:
```
Lead Time = Work in Progress / Throughput
```

**Analyse**:
- Wo sammeln sich Aufgaben?
- Welche Schritte haben die längsten Queues?
- Wo ist die Variabilität am höchsten?

### Durchsatz-Analyse

**Metriken**:
- Deployments pro Zeiteinheit
- Durchschnittliche Bearbeitungszeit pro Schritt
- Kapazität pro Schritt
- Auslastung pro Schritt

## Datenerfassung

### Prozess-Metriken

**Für jeden Prozess-Schritt erfassen**:
- Anzahl der Aufgaben in Queue
- Durchschnittliche Wartezeit
- Durchschnittliche Bearbeitungszeit
- Anzahl der Bearbeiter/Ressourcen
- Auslastung

### Analyse-Tools

- **CI/CD-Analytics**: Pipeline-Metriken
- **Issue-Tracking**: Ticket-Flow-Metriken
- **Version Control**: Commit-to-Deploy-Zeiten
- **Monitoring**: System-Performance-Metriken

## Häufige Bottlenecks

### 1. Code Review

**Symptome**:
- Lange Wartezeiten auf Reviews
- Große Queue von offenen Pull Requests
- Wenige Reviewer für viele Entwickler

**Lösungsansätze**:
- Mehr Reviewer trainieren
- Kleinere Pull Requests
- Automatisierte Code-Analyse
- Asynchrone Reviews

### 2. Test-Ausführung

**Symptome**:
- Lange Test-Laufzeiten
- Flaky Tests
- Begrenzte Test-Infrastruktur
- Sequentielle Test-Ausführung

**Lösungsansätze**:
- Test-Parallelisierung
- Test-Optimierung
- Cloud-Test-Infrastruktur
- Selektive Test-Ausführung

### 3. Approval-Prozesse

**Symptome**:
- Lange Wartezeiten auf Genehmigungen
- Viele Approval-Stufen
- Begrenzte Verfügbarkeit von Approvers
- Manuelle Approval-Prozesse

**Lösungsansätze**:
- Automatisierte Approvals
- Risk-basierte Approvals
- Delegierte Approvals
- Self-Service-Deployments

### 4. Deployment-Kapazität

**Symptome**:
- Deployment-Windows
- Begrenzte Deployment-Slots
- Manuelle Deployment-Schritte
- Shared Deployment-Ressourcen

**Lösungsansätze**:
- Deployment-Automatisierung
- On-Demand Deployments
- Parallele Deployments
- Self-Service-Deployments

## Priorisierung

### Impact-Assessment

**Kriterien**:
- Häufigkeit des Bottlenecks
- Durchschnittliche Verzögerung
- Anzahl betroffener Teams
- Business-Impact

**Berechnung**:
```
Impact Score = Frequency × Delay × Teams × Business Value
```

### Lösungs-Aufwand

**Kategorien**:
- Quick Wins (< 1 Woche)
- Mittelfristig (1-4 Wochen)
- Langfristig (> 1 Monat)

### Priorisierungs-Matrix

```
High Impact, Low Effort → P1 (Sofort)
High Impact, High Effort → P2 (Planen)
Low Impact, Low Effort → P3 (Bei Gelegenheit)
Low Impact, High Effort → P4 (Vermeiden)
```

## Lösungsansätze

### Kapazität erhöhen

- Mehr Ressourcen
- Bessere Tools
- Automatisierung
- Parallelisierung

### Nachfrage reduzieren

- Batch-Größen reduzieren
- Priorisierung
- Elimination unnötiger Schritte
- Self-Service

### Prozess optimieren

- Streamlining
- Standardisierung
- Automatisierung
- Continuous Improvement

## Monitoring und Tracking

### KPIs

- Bottleneck-Dauer
- Queue-Länge
- Durchsatz
- Lead Time

### Dashboards

- Echtzeit-Monitoring
- Trend-Analysen
- Alerts bei Verschlechterung

<!-- Hinweis: Bottleneck-Elimination ist kontinuierlicher Prozess -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |
