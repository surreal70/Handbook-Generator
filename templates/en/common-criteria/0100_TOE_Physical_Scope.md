# TOE Physical Scope

**Document-ID:** 0100
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
This template documents the physical scope of the Target of Evaluation (TOE) according to ISO/IEC 15408-1:2022.
It defines all physical components, hardware, software, firmware, and documentation that are part of the TOE.

Customization required:
- List all physical components of the TOE
- Document hardware components with specifications
- Document software components with versions
- Document firmware components
- Define physical boundaries and exclusions
- Create component diagrams
- Document delivery scope and packaging

Reference: ISO/IEC 15408-1:2022, Section 8.2.1 (TOE Physical Scope)
-->

## 1. Physical Components Overview

### 1.1 TOE Physical Composition
The TOE consists of the following physical components:

| Component ID | Component Name | Type | Version | Description |
|--------------|----------------|------|---------|-------------|
| [TODO: PC-001] | [TODO: Component name] | Hardware/Software/Firmware | [TODO: Version] | [TODO: Description] |
| [TODO: PC-002] | [TODO: Component name] | Hardware/Software/Firmware | [TODO: Version] | [TODO: Description] |
| [TODO: PC-003] | [TODO: Component name] | Hardware/Software/Firmware | [TODO: Version] | [TODO: Description] |

### 1.2 Component Dependencies
[TODO: Describe dependencies between physical components]

```
[TODO: Insert component dependency diagram]
```

## 2. Hardware Components

### 2.1 Hardware Inventory
**Hardware components in the TOE:**

| Hardware ID | Name | Manufacturer | Model | Specifications |
|-------------|------|--------------|-------|----------------|
| [TODO: HW-001] | [TODO: Name] | [TODO: Manufacturer] | [TODO: Model] | [TODO: Specifications] |
| [TODO: HW-002] | [TODO: Name] | [TODO: Manufacturer] | [TODO: Model] | [TODO: Specifications] |

### 2.2 Hardware Specifications
**[TODO: Hardware Component 1]**
- Processor: [TODO: CPU specifications]
- Memory: [TODO: RAM specifications]
- Storage: [TODO: Storage specifications]
- Network: [TODO: Network interfaces]
- Security modules: [TODO: e.g., TPM, HSM, Secure Element]

**[TODO: Hardware Component 2]**
- [TODO: Specifications]

### 2.3 Hardware Security Features
[TODO: Describe hardware-based security features]
- Secure Boot: [TODO: Description]
- Hardware encryption: [TODO: Description]
- Tamper protection: [TODO: Description]
- Physical security features: [TODO: Description]

## 3. Software Components

### 3.1 Software Inventory
**Software components in the TOE:**

| Software ID | Name | Type | Version | Build | License |
|-------------|------|------|---------|-------|---------|
| [TODO: SW-001] | [TODO: Name] | Application/Service/Library | [TODO: Version] | [TODO: Build] | [TODO: License] |
| [TODO: SW-002] | [TODO: Name] | Application/Service/Library | [TODO: Version] | [TODO: Build] | [TODO: License] |

### 3.2 Software Modules
**[TODO: Software Module 1]**
- Purpose: [TODO: Description]
- Programming language: [TODO: e.g., C, C++, Java, Python]
- Size: [TODO: LOC or file size]
- Dependencies: [TODO: External libraries]

**[TODO: Software Module 2]**
- [TODO: Details]

### 3.3 Software Configuration
**Configuration files:**
- [TODO: Configuration file 1]: [TODO: Purpose]
- [TODO: Configuration file 2]: [TODO: Purpose]

**Databases:**
- [TODO: Database 1]: [TODO: Purpose and schema]

## 4. Firmware Components

### 4.1 Firmware Inventory
**Firmware components in the TOE:**

| Firmware ID | Name | Target Hardware | Version | Purpose |
|-------------|------|-----------------|---------|---------|
| [TODO: FW-001] | [TODO: Name] | [TODO: Hardware] | [TODO: Version] | [TODO: Purpose] |
| [TODO: FW-002] | [TODO: Name] | [TODO: Hardware] | [TODO: Version] | [TODO: Purpose] |

### 4.2 Firmware Details
**[TODO: Firmware Component 1]**
- Type: [TODO: e.g., BIOS, UEFI, Embedded Controller]
- Size: [TODO: Size in KB/MB]
- Update mechanism: [TODO: Description]
- Signature: [TODO: Signing method]

### 4.3 Firmware Security
[TODO: Describe firmware security measures]
- Secure firmware update: [TODO]
- Firmware integrity verification: [TODO]
- Rollback protection: [TODO]

## 5. Documentation Components

### 5.1 User Documentation
**User documentation included in the TOE:**
- [TODO: User Guide]: [TODO: Format, version]
- [TODO: Quick Start Guide]: [TODO: Format, version]
- [TODO: Online Help]: [TODO: Format, version]

### 5.2 Administrator Documentation
**Administrator documentation included in the TOE:**
- [TODO: Administrator Guide]: [TODO: Format, version]
- [TODO: Installation Guide]: [TODO: Format, version]
- [TODO: Configuration Guide]: [TODO: Format, version]
- [TODO: Security Guide]: [TODO: Format, version]

### 5.3 Security Documentation
**Security-related documentation:**
- Security Target (ST): [TODO: Version]
- [TODO: Additional security documentation]

## 6. Physical Boundaries

### 6.1 Included Components
**The following components are included in the TOE:**
- [TODO: Component 1]: [TODO: Rationale for inclusion]
- [TODO: Component 2]: [TODO: Rationale for inclusion]
- [TODO: Component 3]: [TODO: Rationale for inclusion]

### 6.2 Excluded Components
**The following components are NOT included in the TOE:**
- [TODO: Component 1]: [TODO: Rationale for exclusion]
- [TODO: Component 2]: [TODO: Rationale for exclusion]
- [TODO: Component 3]: [TODO: Rationale for exclusion]

### 6.3 Boundary Rationale
[TODO: Explain the rationale for the physical boundaries of the TOE]

The physical boundaries were defined as follows:
- [TODO: Rationale 1]
- [TODO: Rationale 2]
- [TODO: Rationale 3]

## 7. Delivery and Packaging

### 7.1 Delivery Format
**The TOE is delivered as:**
- [TODO: e.g., Physical device, Software download, Container image, etc.]

**Delivery media:**
- [TODO: e.g., USB drive, DVD, Download link, etc.]

### 7.2 Package Contents
**The TOE package contains:**
1. [TODO: Component 1]
2. [TODO: Component 2]
3. [TODO: Component 3]
4. [TODO: Documentation]
5. [TODO: License information]

### 7.3 Integrity Protection
**Integrity protection for delivery:**
- Digital signature: [TODO: Signature algorithm and key]
- Checksums: [TODO: Hash algorithm]
- Sealing: [TODO: Physical sealing if applicable]

## 8. Version Control

### 8.1 Component Versions
**Version control for TOE components:**

| Component | Version | Release Date | Changes |
|-----------|---------|--------------|---------|
| [TODO: Component 1] | [TODO: Version] | [TODO: Date] | [TODO: Changes] |
| [TODO: Component 2] | [TODO: Version] | [TODO: Date] | [TODO: Changes] |

### 8.2 Version Identification
**Version identification:**
- Method: [TODO: e.g., About dialog, Version file, CLI command]
- Command: [TODO: e.g., `--version`, `/version`, etc.]
- Output format: [TODO: Example output]

### 8.3 Configuration Management
**Configuration management:**
- CM system: [TODO: e.g., Git, SVN, etc.]
- Repository: [TODO: Repository information]
- Build system: [TODO: Build system information]

## 9. Physical Scope Diagram

### 9.1 Component Diagram
[TODO: Create a diagram showing all physical components and their relationships]

```
[TODO: Insert component diagram]
```

### 9.2 Deployment Diagram
[TODO: Create a deployment diagram showing how components are deployed]

```
[TODO: Insert deployment diagram]
```

**Next Steps:**
1. Complete all [TODO] placeholders with TOE-specific information
2. Create detailed component diagrams
3. Document all versions and build information
4. Verify consistency with logical scope (Template 0110)
5. Ensure all delivery components are documented

