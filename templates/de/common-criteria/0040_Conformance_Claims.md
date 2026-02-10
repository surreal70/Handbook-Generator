# Conformance Claims

**Dokument-ID:** 0040  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
Dieses Template dokumentiert Konformitätsansprüche für Common Criteria, Protection Profiles
und Assurance Packages gemäß ISO/IEC 15408-1:2022.

Anpassung erforderlich:
- Deklariere CC Part 2 und Part 3 Konformität (conformant oder extended)
- Identifiziere Protection Profile Konformität, falls zutreffend
- Wähle Evaluation Assurance Level (EAL1-EAL7)
- Dokumentiere Augmentierungen des Assurance Package
- Stelle Begründungen für alle Konformitätsansprüche bereit
- Dokumentiere Abweichungen von Protection Profiles

Referenz: ISO/IEC 15408-1:2022, Abschnitt 8.3 (Conformance Claims)
-->

## 1. CC Conformance Claim

### 1.1 CC Version
**Common Criteria Version:** ISO/IEC 15408:2022  
**CC Part 1:** ISO/IEC 15408-1:2022  
**CC Part 2:** ISO/IEC 15408-2:2022  
**CC Part 3:** ISO/IEC 15408-3:2022  

### 1.2 CC Conformance
**Conformance:** [TODO: Wähle eine Option]
- [ ] CC Part 2 conformant
- [ ] CC Part 2 extended
- [ ] CC Part 3 conformant
- [ ] CC Part 3 extended

**Begründung:** [TODO: Begründe die Konformitätsansprüche]

## 2. PP Conformance Claim

### 2.1 PP Identification
[TODO: Falls zutreffend, identifiziere das Protection Profile]

**PP Name:** [TODO: Name des Protection Profile]  
**PP Version:** [TODO: Version]  
**PP Registration:** [TODO: Registrierungsnummer]  
**PP Date:** [TODO: Datum]  

### 2.2 PP Conformance Type
[TODO: Wähle den Konformitätstyp]
- [ ] Strict conformance
- [ ] Demonstrable conformance
- [ ] No PP conformance

**Begründung:** [TODO: Begründe den Konformitätstyp]

### 2.3 PP Deviations
[TODO: Falls zutreffend, dokumentiere Abweichungen vom PP]

| Deviation | Type | Justification |
|-----------|------|---------------|
| [TODO: Abweichung 1] | Addition/Omission/Refinement | [TODO: Begründung] |
| [TODO: Abweichung 2] | Addition/Omission/Refinement | [TODO: Begründung] |

## 3. Package Conformance Claim

### 3.1 Assurance Package
**Package:** [TODO: Wähle das Assurance Package]
- [ ] EAL1 (Functionally tested)
- [ ] EAL2 (Structurally tested)
- [ ] EAL3 (Methodically tested and checked)
- [ ] EAL4 (Methodically designed, tested, and reviewed)
- [ ] EAL5 (Semiformally designed and tested)
- [ ] EAL6 (Semiformally verified design and tested)
- [ ] EAL7 (Formally verified design and tested)

### 3.2 Augmented Package
[TODO: Falls zutreffend, liste zusätzliche SARs auf]

**Augmentation:** [TODO: Ja/Nein]

| SAR Component | Rationale |
|---------------|-----------|
| [TODO: SAR 1] | [TODO: Begründung für Hinzufügung] |
| [TODO: SAR 2] | [TODO: Begründung für Hinzufügung] |

## 4. Conformance Rationale

### 4.1 CC Part 2 Conformance Rationale
[TODO: Begründe die Konformität mit CC Part 2]

**SFR Selection:**
- Alle SFRs stammen aus ISO/IEC 15408-2:2022
- [TODO: Weitere Details]

**SFR Extensions:**
[TODO: Falls zutreffend, begründe SFR-Erweiterungen]
- [TODO: Erweiterung 1]
- [TODO: Erweiterung 2]

### 4.2 CC Part 3 Conformance Rationale
[TODO: Begründe die Konformität mit CC Part 3]

**SAR Selection:**
- Alle SARs stammen aus ISO/IEC 15408-3:2022
- [TODO: Weitere Details]

**SAR Augmentation:**
[TODO: Falls zutreffend, begründe SAR-Augmentierungen]
- [TODO: Augmentierung 1]
- [TODO: Augmentierung 2]

### 4.3 PP Conformance Rationale
[TODO: Falls PP-Konformität beansprucht wird]

**Conformance Demonstration:**
- [TODO: Zeige, wie das ST dem PP entspricht]
- [TODO: Dokumentiere alle Abweichungen]
- [TODO: Begründe alle Ergänzungen]

## 5. Conformance Statement Summary

### 5.1 Summary Table
| Conformance Type | Claim | Details |
|------------------|-------|---------|
| CC Version | ISO/IEC 15408:2022 | [TODO: Details] |
| CC Part 2 | [TODO: conformant/extended] | [TODO: Details] |
| CC Part 3 | [TODO: conformant/extended] | [TODO: Details] |
| PP | [TODO: PP Name oder "None"] | [TODO: Details] |
| Assurance Package | [TODO: EAL Level] | [TODO: Details] |
| Augmentation | [TODO: Yes/No] | [TODO: Details] |

### 5.2 Conformance Verification
[TODO: Beschreibe, wie die Konformität verifiziert werden kann]
- Verification method: [TODO]
- Verification evidence: [TODO]

## 6. Conformance Maintenance

### 6.1 Version Control
**ST Version:** {{ meta.version }}  
**Last Conformance Review:** {{ meta.date }}  
**Next Review:** [TODO: Datum]  

### 6.2 Change Management
[TODO: Beschreibe, wie Änderungen an Konformitätsansprüchen verwaltet werden]
- Change process: [TODO]
- Impact assessment: [TODO]
- Re-evaluation triggers: [TODO]

---

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter
2. Verifiziere Konformität mit gewählten Standards
3. Dokumentiere alle Abweichungen vollständig
4. Stelle Konsistenz mit anderen ST-Abschnitten sicher
