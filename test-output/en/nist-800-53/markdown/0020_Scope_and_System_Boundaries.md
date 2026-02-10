# Scope and System Boundaries

**Document-ID:** NIST-0020  
**Organization:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Version:** 1.0.0  
**Status:** Draft / In Review / Approved  
**Last Updated:** {{ meta.document.last_updated }}  

---

## 1. Purpose

This document defines the scope and authorization boundaries of the information system {{ meta.nist.system_name }}.

## 2. System Identification

**System Name:** {{ meta.nist.system_name }}  
**System ID:** {{ meta.nist.system_id }}  
**FIPS 199 Categorization:** [TODO: Low / Moderate / High]  
**System Owner:** [TODO: Name]  
**Authorizing Official (AO):** {{ meta.roles.ao.name }}  

## 3. Authorization Boundary

### 3.1 Boundary Definition

The authorization boundary includes all components under a single authorization decision.

**Authorization Boundary:** [TODO: Description of boundary]

**Included Components:**
- [TODO: Component 1]
- [TODO: Component 2]

**Excluded Components:**
- [TODO: Component 1 - Rationale]

### 3.2 Network Diagram

[TODO: Insert network diagram showing authorization boundary]

## 4. System Components

### 4.1 Hardware Components

| Component | Type | Location | Function | Criticality |
|-----------|------|----------|----------|-------------|
| [TODO: Server 1] | Server | [TODO: DC1] | [TODO: Function] | [TODO: H/M/L] |

### 4.2 Software Components

| Component | Version | Vendor | Function | License |
|-----------|---------|--------|----------|---------|
| [TODO: OS] | [TODO: Version] | [TODO: Vendor] | Operating System | [TODO: License] |

### 4.3 Data Components

| Data Type | Classification | Storage Location | Retention | Backup |
|-----------|----------------|------------------|-----------|--------|
| [TODO: Data 1] | [TODO: Classification] | [TODO: Location] | [TODO: Time] | [TODO: Yes/No] |

## 5. External Interfaces

### 5.1 System Connections

| Connected System | Connection Type | Protocol | Purpose | Authorization |
|------------------|-----------------|----------|---------|---------------|
| [TODO: System 1] | [TODO: Type] | [TODO: Protocol] | [TODO: Purpose] | [TODO: ATO Number] |

## 6. Locations

### 6.1 Physical Locations

| Location-ID | Location Name | Address | Components | Security Level |
|-------------|---------------|---------|------------|----------------|
| [TODO: LOC-01] | [TODO: Name] | [TODO: Address] | [TODO: List] | [TODO: Level] |

## 7. Personnel

### 7.1 User Roles

| Role | Count | Access Level | Rationale |
|------|-------|--------------|-----------|
| [TODO: Admin] | [TODO: Count] | Privileged | Administration |

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |


