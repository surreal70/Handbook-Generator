# SOC 1 / SSAE 18 Framework Mapping

## Überblick

Dieses Dokument ordnet die SOC 1 Handbuch-Vorlagen den COSO Internal Control Framework Komponenten und SOC 1 Berichtsanforderungen zu.

## COSO Framework Komponenten

### 1. Control Environment (Kontrollumgebung)

Die Kontrollumgebung bildet die Grundlage für alle anderen Komponenten der internen Kontrolle.

**COSO Prinzipien**:
1. Integrität und ethische Werte
2. Aufsicht durch den Vorstand
3. Organisationsstruktur und Befugnisse
4. Kompetenz
5. Verantwortlichkeit

**Zugeordnete Vorlagen**:
- 0100_control_environment.md → Alle Prinzipien
- 0110_integrity_and_ethical_values.md → Prinzip 1
- 0120_board_oversight.md → Prinzip 2

### 2. Risk Assessment (Risikobewertung)

Identifikation und Analyse von Risiken, die die Erreichung der Kontrollziele gefährden könnten.

**COSO Prinzipien**:
6. Spezifikation von Zielen
7. Identifikation und Analyse von Risiken
8. Bewertung von Betrugsrisiken
9. Identifikation und Analyse wesentlicher Änderungen

**Zugeordnete Vorlagen**:
- 0200_risk_assessment.md → Prinzipien 6, 7, 9
- 0210_fraud_risk_assessment.md → Prinzip 8

### 3. Control Activities (Kontrollaktivitäten)

Richtlinien und Verfahren, die sicherstellen, dass die Anweisungen des Managements ausgeführt werden.

**COSO Prinzipien**:
10. Auswahl und Entwicklung von Kontrollaktivitäten
11. Auswahl und Entwicklung von allgemeinen Kontrollen über Technologie
12. Einsatz durch Richtlinien und Verfahren

**Zugeordnete Vorlagen**:
- 0300_control_activities.md → Prinzipien 10, 12
- 0310_it_general_controls.md → Prinzip 11

### 4. Information and Communication (Information und Kommunikation)

Erfassung und Kommunikation relevanter Informationen zur Unterstützung der internen Kontrolle.

**COSO Prinzipien**:
13. Verwendung relevanter Informationen
14. Interne Kommunikation
15. Externe Kommunikation

**Zugeordnete Vorlagen**:
- 0400_information_and_communication.md → Prinzipien 13, 14, 15

### 5. Monitoring Activities (Überwachungsaktivitäten)

Laufende und separate Bewertungen zur Feststellung, ob die Komponenten der internen Kontrolle vorhanden und funktionsfähig sind.

**COSO Prinzipien**:
16. Durchführung laufender und/oder separater Bewertungen
17. Bewertung und Kommunikation von Mängeln

**Zugeordnete Vorlagen**:
- 0410_monitoring_activities.md → Prinzipien 16, 17

## SOC 1 Berichtselemente

### Management Assertion

**Beschreibung**: Erklärung des Managements über die Angemessenheit der Systembeschreibung und das Design und die Betriebswirksamkeit der Kontrollen.

**Zugeordnete Vorlagen**:
- 0010_soc1_framework_overview.md
- 0020_service_organization_description.md

### System Description

**Beschreibung**: Beschreibung des Systems der Serviceorganisation, einschließlich Infrastruktur, Software, Personen, Verfahren und Daten.

**Zugeordnete Vorlagen**:
- 0020_service_organization_description.md
- 0030_system_description.md

### Control Objectives

**Beschreibung**: Ziele, die durch die Kontrollen der Serviceorganisation erreicht werden sollen.

**Zugeordnete Vorlagen**:
- 0040_control_objectives.md

### Related Controls

**Beschreibung**: Kontrollen, die entworfen wurden, um die Kontrollziele zu erreichen.

**Zugeordnete Vorlagen**:
- 0100-0199: Control Environment Kontrollen
- 0200-0299: Risk Assessment Kontrollen
- 0300-0399: Control Activities Kontrollen
- 0400-0499: Information and Communication Kontrollen

### Complementary User Entity Controls (CUECs)

**Beschreibung**: Kontrollen, die bei Nutzerorganisationen vorhanden sein müssen, um die Kontrollziele zu erreichen.

**Zugeordnete Vorlagen**:
- 0050_complementary_user_entity_controls.md

### Tests of Controls and Results

**Beschreibung**: Beschreibung der vom Service Auditor durchgeführten Tests und deren Ergebnisse (Type II).

**Hinweis**: Diese werden vom Service Auditor erstellt, nicht von der Serviceorganisation.

## Kontrollziele zu Vorlagen Mapping

### Kontrollziel: Zugriffskontrolle

**COSO-Komponente**: Control Activities

**Relevante Vorlagen**:
- 0300_control_activities.md (IT General Controls Abschnitt)
- 0310_it_general_controls.md (Access Controls Abschnitt)

**Kontrollaktivitäten**:
- Benutzerauthentifizierung
- Benutzerautorisierung
- Privileged Access Management
- Zugriffsprüfungen

### Kontrollziel: Änderungsmanagement

**COSO-Komponente**: Control Activities

**Relevante Vorlagen**:
- 0310_it_general_controls.md (Change Management Abschnitt)

**Kontrollaktivitäten**:
- Change Request Process
- Impact Assessment
- Testing
- Approval
- Implementation

### Kontrollziel: Backup und Recovery

**COSO-Komponente**: Control Activities

**Relevante Vorlagen**:
- 0310_it_general_controls.md (Backup and Recovery Abschnitt)

**Kontrollaktivitäten**:
- Backup-Verfahren
- Recovery-Tests
- Retention

### Kontrollziel: Transaktionsverarbeitung

**COSO-Komponente**: Control Activities

**Relevante Vorlagen**:
- 0300_control_activities.md (Transaction Processing Controls Abschnitt)

**Kontrollaktivitäten**:
- Eingabekontrollen (Vollständigkeit, Genauigkeit, Gültigkeit)
- Verarbeitungskontrollen (Berechnungen, Logik, Fehlerbehandlung)
- Ausgabekontrollen (Vollständigkeit, Genauigkeit, Verteilung)

### Kontrollziel: Funktionstrennung

**COSO-Komponente**: Control Activities

**Relevante Vorlagen**:
- 0300_control_activities.md (Segregation of Duties Abschnitt)

**Kontrollaktivitäten**:
- Kritische Trennungen
- Kompensatorische Kontrollen
- Überwachung von Konflikten

### Kontrollziel: Überwachung der Kontrollwirksamkeit

**COSO-Komponente**: Monitoring Activities

**Relevante Vorlagen**:
- 0410_monitoring_activities.md

**Kontrollaktivitäten**:
- Laufende Überwachung
- Interne Audits
- Mängelbehebung

## Compliance-Mapping

### SSAE 18 Anforderungen

| SSAE 18 Anforderung | Zugeordnete Vorlagen |
|---------------------|----------------------|
| AT-C 320.09 - System Description | 0020, 0030 |
| AT-C 320.10 - Control Objectives | 0040 |
| AT-C 320.11 - Related Controls | 0100-0499 |
| AT-C 320.12 - Complementary User Entity Controls | 0050 |
| AT-C 320.13 - Management Assertion | 0010 |

### COSO 2013 Framework

| COSO Komponente | COSO Prinzipien | Zugeordnete Vorlagen |
|-----------------|-----------------|----------------------|
| Control Environment | 1-5 | 0100-0199 |
| Risk Assessment | 6-9 | 0200-0299 |
| Control Activities | 10-12 | 0300-0399 |
| Information and Communication | 13-15 | 0400 |
| Monitoring Activities | 16-17 | 0410 |

## Lückenanalyse

### Vollständige Abdeckung

Die Vorlagen decken alle fünf COSO-Komponenten und alle 17 COSO-Prinzipien ab.

### Anpassungsbedarf

Organisationen müssen die Vorlagen anpassen für:
- Spezifische Kontrollziele basierend auf ihren Services
- Organisationsspezifische Kontrollen
- Branchenspezifische Anforderungen
- Subservice-Organisationen

### Zusätzliche Dokumentation

Zusätzlich zu diesen Vorlagen benötigen Sie:
- Kontrollnachweise (Evidence)
- Testdokumentation (für Type II)
- Incident-Berichte
- Change-Logs
- Audit-Berichte

## Referenzen

- SSAE 18 (AT-C Section 320)
- COSO Internal Control - Integrated Framework (2013)
- SOC 1 Reporting Guide (AICPA)
- Service Organization Control Reports (AICPA)

---

**Hinweis**: Dieses Mapping dient als Leitfaden. Arbeiten Sie mit Ihrem Service Auditor zusammen, um sicherzustellen, dass alle Anforderungen erfüllt sind.
