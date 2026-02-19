
Document-ID: nist-csf-0070
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Lieferketten-Risikomanagement (GV.SC)

**Dokument-ID:** [FRAMEWORK]-0070
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

Dieses Dokument beschreibt den Ansatz der Organisation zum Management von Cybersecurity-Risiken in der Lieferkette, einschließlich Lieferantenbewertung, Vertragsanforderungen und laufender Überwachung.

## Geltungsbereich

{{ meta-handbook.scope }}

## Lieferketten-Risikostrategie

### Strategische Ziele
- Identifikation und Bewertung von Lieferantenrisiken
- Minimierung von Cybersecurity-Risiken durch Dritte
- Sicherstellung der Compliance bei Lieferanten
- Kontinuierliche Überwachung der Lieferantenleistung

### Risikokategorien

| Kategorie | Beschreibung | Risikostufe |
|-----------|--------------|-------------|
| Kritische Lieferanten | Zugriff auf kritische Systeme/Daten | Hoch |
| IT-Dienstleister | Managed Services, Cloud Provider | Hoch |
| Software-Lieferanten | Anwendungen, Komponenten | Mittel |
| Hardware-Lieferanten | IT-Equipment, Netzwerkgeräte | Mittel |
| Sonstige Lieferanten | Keine IT-Berührung | Niedrig |

## Lieferanten-Lebenszyklus

### 1. Lieferantenauswahl

**Due Diligence:**
- Sicherheitsbewertung
- Finanzielle Stabilität
- Reputation und Referenzen
- Compliance-Nachweise

**Bewertungskriterien:**
- ISO 27001 Zertifizierung
- SOC 2 Bericht
- Datenschutz-Compliance (DSGVO)
- Incident Response Capabilities
- Business Continuity Planning

### 2. Vertragliche Anforderungen

**Sicherheitsklauseln:**
- Vertraulichkeitsvereinbarungen (NDA)
- Datenschutzbestimmungen
- Sicherheitsanforderungen
- Audit-Rechte
- Incident-Meldepflichten
- Haftung und Versicherung

**Service Level Agreements (SLAs):**
- Verfügbarkeit: {{ meta-handbook.sla_availability }}
- Incident Response Zeit: {{ meta-handbook.sla_response_time }}
- Patch-Management: {{ meta-handbook.sla_patch_time }}
- Backup und Recovery: {{ meta-handbook.sla_recovery_time }}

### 3. Onboarding

**Sicherheitsanforderungen:**
- Zugriffskontrolle und Authentifizierung
- Netzwerksegmentierung
- Verschlüsselung
- Logging und Monitoring
- Schulung der Lieferantenmitarbeiter

**Dokumentation:**
- Sicherheitsrichtlinien
- Zugriffsdokumentation
- Kontaktinformationen
- Eskalationsprozesse

### 4. Laufende Überwachung

**Monitoring-Aktivitäten:**
- Quartalsweise Sicherheitsreviews
- Jährliche Audits
- Kontinuierliche Compliance-Überwachung
- Incident-Tracking
- Performance-Metriken

**Key Performance Indicators:**
| KPI | Zielwert | Messhäufigkeit |
|-----|----------|----------------|
| SLA-Einhaltung | > 99% | Monatlich |
| Sicherheitsvorfälle | 0 kritische | Monatlich |
| Patch-Compliance | > 95% | Monatlich |
| Audit-Findings | < 5 High | Jährlich |

### 5. Offboarding

**Prozess:**
- Zugriffswiderruf
- Datenrückgabe/-löschung
- Dokumentation archivieren
- Lessons Learned
- Vertragliche Verpflichtungen nach Beendigung

## Lieferantenkategorisierung

### Tier 1: Kritische Lieferanten
**Kriterien:**
- Zugriff auf kritische Systeme oder Daten
- Hohe Abhängigkeit
- Schwer ersetzbar

**Anforderungen:**
- Umfassende Due Diligence
- ISO 27001 Zertifizierung erforderlich
- Quartalsweise Reviews
- Jährliche Audits
- Incident Response Plan erforderlich

**Beispiele:**
- {{ meta-handbook.critical_supplier_1 }}
- {{ meta-handbook.critical_supplier_2 }}

### Tier 2: Wichtige Lieferanten
**Kriterien:**
- Zugriff auf nicht-kritische Systeme
- Moderate Abhängigkeit
- Ersetzbar mit Aufwand

**Anforderungen:**
- Standard Due Diligence
- SOC 2 oder gleichwertig
- Halbjährliche Reviews
- Alle 2 Jahre Audits

**Beispiele:**
- {{ meta-handbook.important_supplier_1 }}
- {{ meta-handbook.important_supplier_2 }}

### Tier 3: Standard-Lieferanten
**Kriterien:**
- Kein direkter Systemzugriff
- Geringe Abhängigkeit
- Leicht ersetzbar

**Anforderungen:**
- Basis-Sicherheitsbewertung
- Jährliche Reviews
- Self-Assessment

## Risikobewertung

### Bewertungsmatrix

| Faktor | Gewichtung | Bewertung |
|--------|------------|-----------|
| Datenzugriff | 30% | 1-5 |
| Systemzugriff | 25% | 1-5 |
| Geschäftskritikalität | 20% | 1-5 |
| Compliance-Status | 15% | 1-5 |
| Sicherheitsreife | 10% | 1-5 |

**Gesamtrisiko = Σ (Faktor × Gewichtung)**

### Risikobehandlung

| Risikoscore | Kategorie | Maßnahmen |
|-------------|-----------|-----------|
| 4.0 - 5.0 | Kritisch | Sofortige Maßnahmen, möglicher Vertragsausstieg |
| 3.0 - 3.9 | Hoch | Verbesserungsplan erforderlich |
| 2.0 - 2.9 | Mittel | Überwachung und regelmäßige Reviews |
| 1.0 - 1.9 | Niedrig | Standard-Monitoring |

## Incident Management

### Lieferanten-Incidents

**Meldepflichten:**
- Kritische Incidents: Sofort (< 1 Stunde)
- Hohe Incidents: < 4 Stunden
- Mittlere Incidents: < 24 Stunden
- Niedrige Incidents: < 72 Stunden

**Response-Prozess:**
1. Incident-Meldung durch Lieferanten
2. Bewertung durch SOC
3. Koordination der Response
4. Kommunikation mit Stakeholdern
5. Post-Incident Review
6. Lessons Learned

### Eskalation
- Kritische Incidents → CISO + Geschäftsführung
- Datenschutzverletzungen → DPO + Legal
- Vertragsverletzungen → Procurement + Legal

## Compliance und Audits

### Audit-Anforderungen

**Interne Audits:**
- Tier 1: Jährlich
- Tier 2: Alle 2 Jahre
- Tier 3: Risikobasiert

**Externe Audits:**
- ISO 27001 Zertifizierung (Tier 1)
- SOC 2 Berichte (Tier 1-2)
- Penetrationstests (nach Bedarf)

### Compliance-Überwachung
- Kontinuierliche Überwachung der Zertifizierungen
- Tracking von Audit-Findings
- Überprüfung von Verbesserungsmaßnahmen

## Software Supply Chain

### Software-Komponenten
- Software Bill of Materials (SBOM)
- Vulnerability Scanning
- License Compliance
- Update-Management

### Open Source Software
- Genehmigungsprozess
- Vulnerability Monitoring
- License-Überprüfung
- Community-Support-Bewertung

## Dokumentenverweise

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0050_policy_framework.md
- 0150_supply_chain_risk_management.md (Identify)

