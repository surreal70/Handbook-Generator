# Audit and Accountability Policy

**Document-ID:** NIST-0220
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

## 1. Control Description

**AU-1 Policy and Procedures**  
**AU-2 Audit Events**  
**AU-3 Content of Audit Records**  

The organization implements audit and accountability controls to track system activity.

## 2. Control Implementation

### 2.1 Auditable Events

**Security-Relevant Events:**
- Successful and failed login attempts
- Account management actions
- Privilege escalation
- System configuration changes
- Data access and modifications
- Security policy changes

### 2.2 Audit Record Content

**Required Information:**
- Event type
- Date and time
- User/process identity
- Source and destination
- Event outcome (success/failure)
- Additional details

### 2.3 Audit Log Management

**Log Retention:** [TODO: 90 days online, 1 year archive]  
**Log Protection:** Encrypted, access-controlled  
**Log Review:** Daily for critical systems  

## 3. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned]  
**SIEM Solution:** [TODO: Tool name]  
**Log Sources:** [TODO: Number of sources]  

<!-- End of template -->
