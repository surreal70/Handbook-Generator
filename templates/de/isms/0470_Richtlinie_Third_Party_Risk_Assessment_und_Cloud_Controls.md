# Richtlinie: Third-Party Risk Assessment und Cloud Controls

**Dokument-ID:** 0470
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md` und definiert:
- Third-Party Risk Assessment Prozesse
- Cloud Security Controls und Compliance
- Lieferantenmanagement und -überwachung

**Geltungsbereich:** Alle Lieferanten und Cloud-Services bei **{{ meta-organisation.name }}**

## 2. Third-Party Risk Assessment

### 2.1 Lieferanten-Kategorisierung

**Kritikalität:**
| Kategorie | Definition | Beispiele | Assessment-Tiefe |
|-----------|------------|-----------|------------------|
| Kritisch | Zugriff auf vertrauliche Daten oder kritische Systeme | Cloud-Provider, Managed Security Services | Umfassend |
| Hoch | Wichtige Business-Services | ERP-Anbieter, Payment-Provider | Detailliert |
| Mittel | Standard-Services | Office-Software, Marketing-Tools | Standard |
| Niedrig | Minimale Auswirkung | Büromaterial, Catering | Minimal |

### 2.2 Pre-Contract Assessment

**Phase 1: Initial Screening**
- Fragebogen zu Sicherheitskontrollen
- Zertifizierungen (ISO 27001, SOC 2)
- Datenschutz-Compliance (DSGVO)
- Finanzielle Stabilität

**Phase 2: Detailed Assessment (Kritisch/Hoch)**
- Security-Audit oder On-Site-Visit
- Penetration-Test-Berichte
- Incident-Response-Fähigkeiten
- Business Continuity Plans

**Phase 3: Contract Negotiation**
- Security-Klauseln im Vertrag
- SLAs für Sicherheit und Verfügbarkeit
- Audit-Rechte
- Incident-Notification-Pflichten

### 2.3 Ongoing Monitoring

**Frequenz:**
- Kritisch: Quartalsweise Review
- Hoch: Halbjährlich
- Mittel: Jährlich
- Niedrig: Bei Vertragsverlängerung

**Monitoring-Aktivitäten:**
- Zertifizierungs-Status prüfen
- Security-Incidents beim Lieferanten
- Compliance-Berichte anfordern
- Performance gegen SLAs

### 2.4 Offboarding

**Prozess:**
1. Datenrückgabe oder -löschung
2. Zugriffe widerrufen
3. Vertraulichkeitsverpflichtungen bestätigen
4. Abschlussdokumentation

## 3. Cloud Security Controls

### 3.1 Cloud Service Models

**IaaS (Infrastructure as a Service):**
- Shared Responsibility Model
- Kunde verantwortlich für OS, Anwendungen, Daten
- Provider verantwortlich für Infrastruktur

**PaaS (Platform as a Service):**
- Provider verantwortlich für Plattform
- Kunde verantwortlich für Anwendungen, Daten

**SaaS (Software as a Service):**
- Provider verantwortlich für alles außer Daten
- Kunde verantwortlich für Daten und Zugriffskontrolle

### 3.2 Cloud Security Assessment

**Vor Cloud-Adoption:**
- Cloud Security Posture Assessment
- Data Residency und Compliance prüfen
- Verschlüsselungsoptionen evaluieren
- Backup und DR-Fähigkeiten

**Cloud Security Controls:**
- Identity and Access Management (IAM)
- Netzwerk-Segmentierung
- Verschlüsselung (at rest, in transit)
- Logging und Monitoring
- Compliance-Zertifizierungen

### 3.3 Cloud Access Security Broker (CASB)

**Funktionen:**
- Visibility in Cloud-Nutzung
- Data Loss Prevention (DLP)
- Threat Protection
- Compliance-Monitoring

**CASB-System:** {{ meta.security.casb_solution }}

### 3.4 Multi-Cloud und Hybrid-Cloud

**Governance:**
- Einheitliche Security-Policies über alle Clouds
- Zentrale Identity-Provider (SSO)
- Konsistentes Monitoring

**Cloud-Provider:**
- Primary: {{ meta.cloud.primary_provider }}
- Secondary: {{ meta.cloud.secondary_provider }}

## 4. Vertragsmanagement

### 4.1 Security-Klauseln

**Pflicht-Klauseln:**
- Datenschutz und DSGVO-Compliance
- Sicherheitskontrollen und -standards
- Incident-Notification (innerhalb 24 Stunden)
- Audit-Rechte
- Datenrückgabe bei Vertragsende
- Haftung bei Datenverletzungen

### 4.2 Service Level Agreements (SLAs)

**Security-SLAs:**
- Verfügbarkeit (z.B. 99.9%)
- Incident-Response-Zeit
- Patch-Management-Zeitrahmen
- Backup-Frequenz und -Retention

### 4.3 Data Processing Agreements (DPA)

**DSGVO-Anforderungen:**
- Auftragsverarbeitungsvertrag (AVV)
- Technische und organisatorische Maßnahmen (TOMs)
- Sub-Processor-Liste
- Datenübermittlung in Drittländer

## 5. Lieferanten-Risikomanagement

### 5.1 Risiko-Register

**Dokumentation:**
- Lieferant, Service, Kritikalität
- Identifizierte Risiken
- Mitigationsmaßnahmen
- Residual Risk
- Review-Datum

### 5.2 Incident Management

**Bei Lieferanten-Incidents:**
1. Benachrichtigung durch Lieferanten (SLA: 24h)
2. Impact-Assessment
3. Mitigationsmaßnahmen koordinieren
4. Eigene Kunden informieren (falls erforderlich)
5. Post-Incident-Review

### 5.3 Business Continuity

**Lieferanten-Ausfall-Szenarien:**
- Alternative Lieferanten identifizieren
- Exit-Strategie definieren
- Daten-Portabilität sicherstellen

## 6. Compliance und Audit

### 6.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Lieferanten mit aktuellem Assessment | 100% |
| Kritische Lieferanten mit ISO 27001 | > 90% |
| SLA-Einhaltung | > 95% |
| Incident-Notification-Compliance | 100% |

### 6.2 Audit-Nachweise

- Lieferanten-Assessments
- Verträge mit Security-Klauseln
- SLA-Reports
- Incident-Dokumentation

## 7. Referenzen

### Interne Dokumente
- `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md`
- `0400_Policy_Incident_Management.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.19** - Information security in supplier relationships
- **ISO/IEC 27001:2022 Annex A.5.20** - Addressing information security within supplier agreements
- **ISO/IEC 27001:2022 Annex A.5.21** - Managing information security in the ICT supply chain
- **ISO/IEC 27001:2022 Annex A.5.22** - Monitoring, review and change management of supplier services
- **ISO/IEC 27001:2022 Annex A.5.23** - Information security for use of cloud services

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

