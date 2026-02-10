# Account Management

**Dokument-ID:** NIST-0110  
**Control Family:** Access Control (AC)  
**Control:** AC-2  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Control Description

**AC-2 Account Management**

The organization manages information system accounts including identification, authorization, monitoring, and termination.

## 2. Control Implementation

### 2.1 Account Types

| Account Type | Description | Approval Required |
|--------------|-------------|-------------------|
| Individual | Personal user accounts | Manager |
| Group | Shared group accounts | ISSO |
| System | Service accounts | System Owner |
| Guest | Temporary access | ISSO |
| Privileged | Administrative accounts | ISSM |

### 2.2 Account Management Process

**Account Creation:**
1. Access request submitted
2. Manager approval
3. ISSO review
4. Account provisioning
5. User notification

**Account Modification:**
- Role changes require manager approval
- Privilege escalation requires ISSO approval

**Account Termination:**
- Immediate termination upon separation
- Automated deprovisioning within 24 hours

### 2.3 Account Monitoring

**Monitoring Activities:**
- Inactive accounts reviewed monthly
- Privileged account usage logged
- Failed login attempts monitored
- Account anomalies investigated

## 3. Control Enhancements

**AC-2(1) Automated System Account Management:** [TODO: Implemented / Not Implemented]  
**AC-2(2) Automated Temporary and Emergency Account Management:** [TODO: Implemented / Not Implemented]  
**AC-2(3) Disable Accounts:** [TODO: Implemented / Not Implemented]  
**AC-2(4) Automated Audit Actions:** [TODO: Implemented / Not Implemented]  

## 4. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned]  
**Implementation Date:** [TODO: Datum]  
**Responsible:** {{ meta.roles.isso.name }}  

## 5. Assessment

**Assessment Method:** Examine, Interview, Test  
**Assessment Status:** [TODO: Satisfied / Other than Satisfied]  
**Findings:** [TODO: Beschreibung]  

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
