# Conformance Claims

**Document-ID:** 0040
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents conformance claims for Common Criteria, Protection Profiles,
and assurance packages according to ISO/IEC 15408-1:2022.

Customization required:
- Declare CC Part 2 and Part 3 conformance (conformant or extended)
- Identify Protection Profile conformance if applicable
- Select Evaluation Assurance Level (EAL1-EAL7)
- Document any augmentations to the assurance package
- Provide rationale for all conformance claims
- Document any deviations from Protection Profiles

Reference: ISO/IEC 15408-1:2022, Section 8.3 (Conformance Claims)
-->

## 1. CC Conformance Claim

### 1.1 CC Version
**Common Criteria Version:** ISO/IEC 15408:2022  
**CC Part 1:** ISO/IEC 15408-1:2022  
**CC Part 2:** ISO/IEC 15408-2:2022  
**CC Part 3:** ISO/IEC 15408-3:2022  

### 1.2 CC Conformance
**Conformance:** [TODO: Select one option]
- [ ] CC Part 2 conformant
- [ ] CC Part 2 extended
- [ ] CC Part 3 conformant
- [ ] CC Part 3 extended

**Rationale:** [TODO: Justify the conformance claims]

## 2. PP Conformance Claim

### 2.1 PP Identification
[TODO: If applicable, identify the Protection Profile]

**PP Name:** [TODO: Protection Profile name]  
**PP Version:** [TODO: Version]  
**PP Registration:** [TODO: Registration number]  
**PP Date:** [TODO: Date]  

### 2.2 PP Conformance Type
[TODO: Select conformance type]
- [ ] Strict conformance
- [ ] Demonstrable conformance
- [ ] No PP conformance

**Rationale:** [TODO: Justify the conformance type]

### 2.3 PP Deviations
[TODO: If applicable, document deviations from PP]

| Deviation | Type | Justification |
|-----------|------|---------------|
| [TODO: Deviation 1] | Addition/Omission/Refinement | [TODO: Justification] |
| [TODO: Deviation 2] | Addition/Omission/Refinement | [TODO: Justification] |

## 3. Package Conformance Claim

### 3.1 Assurance Package
**Package:** [TODO: Select the assurance package]
- [ ] EAL1 (Functionally tested)
- [ ] EAL2 (Structurally tested)
- [ ] EAL3 (Methodically tested and checked)
- [ ] EAL4 (Methodically designed, tested, and reviewed)
- [ ] EAL5 (Semiformally designed and tested)
- [ ] EAL6 (Semiformally verified design and tested)
- [ ] EAL7 (Formally verified design and tested)

### 3.2 Augmented Package
[TODO: If applicable, list additional SARs]

**Augmentation:** [TODO: Yes/No]

| SAR Component | Rationale |
|---------------|-----------|
| [TODO: SAR 1] | [TODO: Rationale for addition] |
| [TODO: SAR 2] | [TODO: Rationale for addition] |

## 4. Conformance Rationale

### 4.1 CC Part 2 Conformance Rationale
[TODO: Justify conformance with CC Part 2]

**SFR Selection:**
- All SFRs are derived from ISO/IEC 15408-2:2022
- [TODO: Additional details]

**SFR Extensions:**
[TODO: If applicable, justify SFR extensions]
- [TODO: Extension 1]
- [TODO: Extension 2]

### 4.2 CC Part 3 Conformance Rationale
[TODO: Justify conformance with CC Part 3]

**SAR Selection:**
- All SARs are derived from ISO/IEC 15408-3:2022
- [TODO: Additional details]

**SAR Augmentation:**
[TODO: If applicable, justify SAR augmentations]
- [TODO: Augmentation 1]
- [TODO: Augmentation 2]

### 4.3 PP Conformance Rationale
[TODO: If PP conformance is claimed]

**Conformance Demonstration:**
- [TODO: Show how the ST conforms to the PP]
- [TODO: Document all deviations]
- [TODO: Justify all additions]

## 5. Conformance Statement Summary

### 5.1 Summary Table
| Conformance Type | Claim | Details |
|------------------|-------|---------|
| CC Version | ISO/IEC 15408:2022 | [TODO: Details] |
| CC Part 2 | [TODO: conformant/extended] | [TODO: Details] |
| CC Part 3 | [TODO: conformant/extended] | [TODO: Details] |
| PP | [TODO: PP Name or "None"] | [TODO: Details] |
| Assurance Package | [TODO: EAL Level] | [TODO: Details] |
| Augmentation | [TODO: Yes/No] | [TODO: Details] |

### 5.2 Conformance Verification
[TODO: Describe how conformance can be verified]
- Verification method: [TODO]
- Verification evidence: [TODO]

## 6. Conformance Maintenance

### 6.1 Version Control
**ST Version:** {{ meta-handbook.revision }}  
**Last Conformance Review:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  

### 6.2 Change Management
[TODO: Describe how changes to conformance claims are managed]
- Change process: [TODO]
- Impact assessment: [TODO]
- Re-evaluation triggers: [TODO]

**Next Steps:**
1. Complete all [TODO] placeholders
2. Verify conformance with selected standards
3. Document all deviations completely
4. Ensure consistency with other ST sections

