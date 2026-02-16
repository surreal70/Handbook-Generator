---
Document-ID: coso-0520
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Processebenen-Kontrollen

## Purpose

This document describes die Processebenen-Kontrollen (Process-Level Controls) at {{ source.organization_name }}.

## Scope

- Processspezifische Kontrollen
- Transaktionskontrollen
- Operative Kontrollen
- Anwendungskontrollen

## Definition

### Process-Level Controls

{{ source.process_level_controls_definition }}

### Characteristics

**Processspezifisch**: {{ source.process_specific }}
**Direkte Kontrollen**: {{ source.direct_controls }}
**Detektive und präventive Natur**: {{ source.detective_preventive }}
**Messbare Wirksamkeit**: {{ source.measurable_effectiveness }}

## Kategorien von Process-Level Controls

### Transaktionskontrollen

**Eingabekontrollen**: {{ source.input_controls }}
**Verarattungskontrollen**: {{ source.processing_controls }}
**Ausgabekontrollen**: {{ source.output_controls }}

**Beispiele**:
- Datenvalidierung
- Genehmigungsworkflows
- Abstimmungen
- Berichtsvalidierung

### Operative Kontrollen

**Processkontrollen**: {{ source.process_controls }}
**Qualitätskontrollen**: {{ source.quality_controls }}
**Leistungskontrollen**: {{ source.performance_controls }}

**Beispiele**:
- Processchecklisten
- Qualitätsprüfungen
- Leistungsindikatoren
- Processüberwachung

### IT-Anwendungskontrollen

**Automatisierte Kontrollen**: {{ source.automated_controls }}
**Manuelle Kontrollen**: {{ source.manual_controls }}
**IT-abhängige manuelle Kontrollen**: {{ source.it_dependent_manual_controls }}

**Beispiele**:
- Systemvalidierungen
- Zugriffskontrollen
- Berechnungskontrollen
- Schnittstellen-Kontrollen

## Geschäftsprozesse und Kontrollen

### Finanzprozesse

**Order-to-Cash**: {{ source.order_to_cash_controls }}
**Purchase-to-Pay**: {{ source.purchase_to_pay_controls }}
**Record-to-Report**: {{ source.record_to_report_controls }}

### Operative Processe

**Produktion**: {{ source.production_controls }}
**Logistik**: {{ source.logistics_controls }}
**Kundenservice**: {{ source.customer_service_controls }}

### Unterstützungsprozesse

**Personalwesen**: {{ source.hr_controls }}
**IT**: {{ source.it_controls }}
**Beschaffung**: {{ source.procurement_controls }}

## Kontrolltypen

### Präventive Kontrollen

**Definition**: {{ source.preventive_controls_definition }}

**Beispiele**:
- Funktionstrennung
- Genehmigungsverfahren
- Zugriffsrechte
- Systemvalidierungen

### Detektive Kontrollen

**Definition**: {{ source.detective_controls_definition }}

**Beispiele**:
- Abstimmungen
- Analysen
- Überprüfungen
- Ausnahmeberichte

### Korrektive Kontrollen

**Definition**: {{ source.corrective_controls_definition }}

**Beispiele**:
- Fehlerkorrekturverfahren
- Nachbearattungsprozesse
- Anpassungen

## Kontrolldesign

### Kontrollziele

**Vollständigkeit**: {{ source.completeness_objective }}
**Genauigkeit**: {{ source.accuracy_objective }}
**Gültigkeit**: {{ source.validity_objective }}
**Authorisierung**: {{ source.authorization_objective }}
**Zeitnähe**: {{ source.timeliness_objective }}

### Kontrollaktivitäten

**Genehmigungen**: {{ source.approvals }}
**Abstimmungen**: {{ source.reconciliations }}
**Überprüfungen**: {{ source.reviews }}
**Funktionstrennung**: {{ source.segregation_of_duties }}
**Physische Kontrollen**: {{ source.physical_controls }}

### Kontrollfrequenz

**Kontinuierlich**: {{ source.continuous_controls }}
**Täglich**: {{ source.daily_controls }}
**Wöchentlich**: {{ source.weekly_controls }}
**Monatlich**: {{ source.monthly_controls }}
**Quartalsweise**: {{ source.quarterly_controls }}

## Kontrollimplementierung

### Kontrollbeschreibung

**Kontrollziel**: {{ source.control_objective }}
**Kontrollaktivität**: {{ source.control_activity }}
**Kontrolleigentümer**: {{ source.control_owner }}
**Kontrollfrequenz**: {{ source.control_frequency }}
**Kontrollevidence**: {{ source.control_evidence }}

### Kontrollmatrix

{{ source.control_matrix }}

### Kontrollnachweis

**Dokumentation**: {{ source.control_documentation }}
**Evidence**: {{ source.control_evidence_types }}
**Aufbewahrung**: {{ source.evidence_retention }}

## Funktionstrennung

### Prinzip

{{ source.segregation_principle }}

### Kritische Trennungen

**Authorisierung und Ausführung**: {{ source.authorization_execution_separation }}
**Ausführung und Aufzeichnung**: {{ source.execution_recording_separation }}
**Verwahrung und Aufzeichnung**: {{ source.custody_recording_separation }}

### Kompensationskontrollen

{{ source.compensating_controls }}

## Automatisierung von Kontrollen

### Automatisierungsvorteile

**Konsistenz**: {{ source.automation_consistency }}
**Effizienz**: {{ source.automation_efficiency }}
**Vollständigkeit**: {{ source.automation_completeness }}
**Zeitnähe**: {{ source.automation_timeliness }}

### Automatisierungsmöglichkeiten

**Robotic Process Automation (RPA)**: {{ source.rpa_controls }}
**Workflow-Automatisierung**: {{ source.workflow_automation }}
**Datenvalidierung**: {{ source.automated_validation }}

### IT-Abhängigkeiten

{{ source.it_dependencies }}

## Kontrolltests

### Testarten

**Design-Tests**: {{ source.design_testing }}
**Wirksamkeitstests**: {{ source.effectiveness_testing }}

### Testmethoden

**Inquiry**: {{ source.inquiry }}
**Observation**: {{ source.observation }}
**Inspection**: {{ source.inspection }}
**Re-performance**: {{ source.reperformance }}

### Teststichproben

**Stichprobenauswahl**: {{ source.sample_selection }}
**Stichprobengröße**: {{ source.sample_size }}
**Stichprobenbewertung**: {{ source.sample_evaluation }}

## Kontrollmängel

### Mängelarten

**Design-Mängel**: {{ source.design_deficiencies }}
**Operative Mängel**: {{ source.operating_deficiencies }}

### Mängelbewertung

**Schweregrad**: {{ source.deficiency_severity }}
**Auswirkung**: {{ source.deficiency_impact }}
**Wahrscheinlichkeit**: {{ source.deficiency_likelihood }}

### Mängelbehebung

**Abhilfemaßnahmen**: {{ source.remediation_actions }}
**Zeitplan**: {{ source.remediation_timeline }}
**Verantwortlichkeiten**: {{ source.remediation_responsibilities }}

## Überwachung von Process-Level Controls

### Laufende Überwachung

**Kontrollselbstbewertungen**: {{ source.control_self_assessments }}
**Key Control Indicators**: {{ source.key_control_indicators }}
**Automatisierte Überwachung**: {{ source.automated_monitoring }}

### Periodische Bewertungen

**Interne Revision**: {{ source.internal_audit_testing }}
**Management-Reviews**: {{ source.management_reviews }}

## Beziehung zu Entity-Level Controls

### Hierarchie

{{ source.control_hierarchy }}

### Abhängigkeiten

{{ source.control_dependencies }}

### Integration

{{ source.elc_plc_integration }}

## Dokumentation

### Processdokumentation

**Processflussdiagramme**: {{ source.process_flow_diagrams }}
**Processbeschreibungen**: {{ source.process_descriptions }}
**RACI-Matrizen**: {{ source.raci_matrices }}

### Kontrolldokumentation

**Kontrollbeschreibungen**: {{ source.control_descriptions }}
**Kontrollmatrizen**: {{ source.control_matrices }}
**Testdokumentation**: {{ source.test_documentation }}

## Roles and Responsibilities

**Processeigentümer**: {{ source.process_owner_responsibilities }}
**Kontrolleigentümer**: {{ source.control_owner_responsibilities }}
**Kontrollausführende**: {{ source.control_performer_responsibilities }}
**Kontrollprüfer**: {{ source.control_reviewer_responsibilities }}

## References

- Kontrollrahmen
- Processhandbücher
- Kontrollmatrizen
- Funktionstrennung-Matrix
- COSO Internal Control Framework

---

**Document History:**

| Version | Date | Author | Changes |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
