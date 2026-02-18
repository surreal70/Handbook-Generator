# TSC Framework Mapping

**Dokument-ID:** [FRAMEWORK]-9999
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

## Übersicht

Dieses Dokument mappt die TSC-Templates zu den Trust Services Criteria (TSC) für SOC 2-Audits.

## Trust Services Categories

### Common Criteria (CC) - Security (Pflicht für alle SOC 2)

| TSC Criterion | Template | Beschreibung |
|---------------|----------|--------------|
| **CC1: Control Environment** | TSC-0100 | Organisationsstruktur, Integrität, ethische Werte |
| CC1.1 | TSC-0100 | Integrity and ethical values |
| CC1.2 | TSC-0100 | Board independence |
| CC1.3 | TSC-0100 | Management oversight |
| CC1.4 | TSC-0100 | Commitment to competence |
| CC1.5 | TSC-0100 | Accountability |
| **CC2: Communication and Information** | TSC-0110 | Kommunikation von Zielen und Verantwortlichkeiten |
| CC2.1 | TSC-0110 | Internal communication |
| CC2.2 | TSC-0110 | External communication |
| CC2.3 | TSC-0110 | Information quality |
| **CC3: Risk Assessment** | TSC-0120 | Risikobewertungsprozess |
| CC3.1 | TSC-0120 | Risk identification |
| CC3.2 | TSC-0120 | Risk analysis |
| CC3.3 | TSC-0120 | Risk response |
| **CC4: Monitoring Activities** | TSC-0130 | Überwachung der Kontrollwirksamkeit |
| CC4.1 | TSC-0130 | Ongoing monitoring |
| CC4.2 | TSC-0130 | Separate evaluations |
| CC4.3 | TSC-0130 | Evaluation and communication |
| **CC5: Control Activities** | TSC-0140 | Logische und physische Zugriffskontrolle |
| CC5.1 | TSC-0140 | Selection and development of control activities |
| CC5.2 | TSC-0140 | Technology controls |
| CC5.3 | TSC-0140 | Policies and procedures |
| **CC6: Logical and Physical Access Controls** | TSC-0150 | Zugriffskontrolle |
| CC6.1 | TSC-0150 | Logical access |
| CC6.2 | TSC-0150 | Physical access |
| CC6.3 | TSC-0150 | Access removal |
| CC6.6 | TSC-0150 | Logical access - Identification and authentication |
| CC6.7 | TSC-0150 | Logical access - Privileged access |
| CC6.8 | TSC-0150 | Physical access - Data centers |
| **CC7: System Operations** | TSC-0150 | Systemoperationen |
| CC7.1 | TSC-0150 | Detection and monitoring |
| CC7.2 | TSC-0150 | System capacity |
| CC7.3 | TSC-0150 | System monitoring tools |
| CC7.4 | TSC-0150 | Incident response |
| CC7.5 | TSC-0150 | Incident mitigation |
| **CC8: Change Management** | TSC-0150 | Änderungsmanagement |
| CC8.1 | TSC-0150 | Change authorization |
| CC8.2 | TSC-0150 | Change testing |
| CC8.3 | TSC-0150 | Change deployment |
| **CC9: Risk Mitigation** | TSC-0150 | Risikominderung |
| CC9.1 | TSC-0150 | Risk assessment |
| CC9.2 | TSC-0150 | Vendor management |

### Availability (A) - Optional

| TSC Criterion | Template | Beschreibung |
|---------------|----------|--------------|
| **A1: Availability** | TSC-0200 | Systemverfügbarkeit |
| A1.1 | TSC-0200 | Availability commitments and SLAs |
| A1.2 | TSC-0200 | System monitoring and alerting |
| A1.3 | TSC-0200 | Incident management for availability |
| A1.4 | TSC-0200 | Recovery procedures and disaster recovery |

### Processing Integrity (PI) - Optional

| TSC Criterion | Template | Beschreibung |
|---------------|----------|--------------|
| **PI1: Processing Integrity** | TSC-0240 | Verarbeitungsintegrität |
| PI1.1 | TSC-0240 | Processing commitments |
| PI1.2 | TSC-0240 | Input validation |
| PI1.3 | TSC-0240 | Processing controls |
| PI1.4 | TSC-0240 | Output controls |
| PI1.5 | TSC-0240 | Error handling and correction |

### Confidentiality (C) - Optional

| TSC Criterion | Template | Beschreibung |
|---------------|----------|--------------|
| **C1: Confidentiality** | TSC-0280 | Vertraulichkeit |
| C1.1 | TSC-0280 | Confidentiality commitments |
| C1.2 | TSC-0280 | Access controls for confidential data |
| C1.3 | TSC-0280 | Encryption of confidential data |
| C1.4 | TSC-0280 | Secure disposal of confidential data |

### Privacy (P) - Optional

| TSC Criterion | Template | Beschreibung |
|---------------|----------|--------------|
| **P1: Notice and Communication** | TSC-0320 | Datenschutzhinweise |
| P1.1 | TSC-0320 | Privacy notice |
| P1.2 | TSC-0320 | Privacy policy communication |
| **P2: Choice and Consent** | TSC-0320 | Einwilligung |
| P2.1 | TSC-0320 | Consent for collection |
| **P3: Collection** | TSC-0320 | Datenerhebung |
| P3.1 | TSC-0320 | Collection limitation |
| P3.2 | TSC-0320 | Data minimization |
| **P4: Use, Retention, and Disposal** | TSC-0320 | Verwendung und Aufbewahrung |
| P4.1 | TSC-0320 | Purpose limitation |
| P4.2 | TSC-0320 | Data retention |
| P4.3 | TSC-0320 | Secure disposal |
| **P5: Access** | TSC-0320 | Zugang |
| P5.1 | TSC-0320 | Data subject access requests |
| P5.2 | TSC-0320 | Data correction |
| **P6: Disclosure to Third Parties** | TSC-0320 | Offenlegung |
| P6.1 | TSC-0320 | Third-party disclosures |
| P6.2 | TSC-0320 | Data processing agreements |
| **P7: Quality** | TSC-0320 | Datenqualität |
| P7.1 | TSC-0320 | Data accuracy |
| **P8: Monitoring and Enforcement** | TSC-0320 | Überwachung |
| P8.1 | TSC-0320 | Privacy compliance monitoring |

## Foundation Templates

| Template | Beschreibung | TSC Relevanz |
|----------|--------------|--------------|
| TSC-0010 | Systembeschreibung | System Description (Required for all SOC 2) |
| TSC-0020 | System-Grenzen | System Boundaries (Required for all SOC 2) |
| TSC-0030 | System-Komponenten | Infrastructure, Software, People, Processes, Data |
| TSC-0040 | Rollen und Verantwortlichkeiten | Organizational Structure (CC1) |
| TSC-0050 | Control Environment | Control Environment (CC1) |

## Appendices

| Template | Beschreibung | TSC Relevanz |
|----------|--------------|--------------|
| TSC-0400 | Control Matrix | Complete mapping of all controls |
| TSC-0410 | Evidence Documentation | Audit evidence repository |
| TSC-0420 | Test Results | Control testing results |
| TSC-0430 | Vendor Management | Subservice organization management |
| TSC-0440 | Glossar | TSC terminology |

## Coverage Analysis

### Common Criteria (CC) - 100% Coverage

Alle 9 Common Criteria (CC1-CC9) sind vollständig abgedeckt:
- ✅ CC1: Control Environment (TSC-0100)
- ✅ CC2: Communication (TSC-0110)
- ✅ CC3: Risk Assessment (TSC-0120)
- ✅ CC4: Monitoring (TSC-0130)
- ✅ CC5: Control Activities (TSC-0140)
- ✅ CC6: Logical and Physical Access (TSC-0150)
- ✅ CC7: System Operations (TSC-0150)
- ✅ CC8: Change Management (TSC-0150)
- ✅ CC9: Risk Mitigation (TSC-0150)

### Optional Categories - 100% Coverage

Alle optionalen Kategorien sind vollständig abgedeckt:
- ✅ Availability (A1) - TSC-0200
- ✅ Processing Integrity (PI1) - TSC-0240
- ✅ Confidentiality (C1) - TSC-0280
- ✅ Privacy (P1-P8) - TSC-0320

## Gaps and Recommendations

### Keine Gaps identifiziert

Alle TSC-Kriterien sind durch Templates abgedeckt.

### Empfehlungen

1. **Customization:** Passen Sie die Templates an Ihre spezifische Systemumgebung an
2. **Evidence Collection:** Sammeln Sie Nachweise für jede Kontrolle
3. **Control Testing:** Führen Sie regelmäßige Kontrolltests durch
4. **Documentation:** Halten Sie die Dokumentation aktuell
5. **Audit Preparation:** Bereiten Sie sich frühzeitig auf das SOC 2-Audit vor

## SOC 2 Report Types

### Type I Report

- **Scope:** Design der Kontrollen
- **Zeitpunkt:** Stichtagsbezogen
- **Templates:** Alle Templates relevant

### Type II Report

- **Scope:** Design und Wirksamkeit der Kontrollen
- **Zeitraum:** Zeitraumbezogen (6-12 Monate)
- **Templates:** Alle Templates relevant + Nachweis der Kontrollwirksamkeit

## Verwendung

1. **Scope Definition:** Definieren Sie, welche TSC-Kategorien für Ihr SOC 2-Audit relevant sind
2. **Template Selection:** Wählen Sie die entsprechenden Templates aus
3. **Customization:** Passen Sie die Templates an Ihre Organisation an
4. **Evidence Collection:** Sammeln Sie Nachweise für jede Kontrolle
5. **Audit Preparation:** Bereiten Sie die Dokumentation für das Audit vor

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2026-02-07  
**Maintainer:** TSC-Template-Team

