# Guideline: Security Requirements in Project Lifecycle

**Document-ID:** [FRAMEWORK]-0690
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## 1. Purpose and Scope

This guideline implements `0680_Policy_Security_in_Projects.md` and defines:
- Security requirements in all project phases
- Security reviews and gateways
- Security-by-design principles

**Scope:** All IT projects at **{{ meta-organisation.name }}**

## 2. Project Classification

### 2.1 Project Categories

**Category A (Critical):**
- New systems with confidential data
- Internet-facing applications
- Critical infrastructure
- **Security Involvement:** Comprehensive

**Category B (High):**
- Internal applications with sensitive data
- Changes to critical systems
- **Security Involvement:** Detailed

**Category C (Standard):**
- Standard IT projects
- Infrastructure upgrades
- **Security Involvement:** Standard

**Category D (Low):**
- Small changes
- Non-critical systems
- **Security Involvement:** Minimal

### 2.2 Classification Criteria

**Assessment:**
- Data classification (Confidential/Highly Confidential = higher category)
- Internet exposure (Yes = higher category)
- Number of users (> 100 = higher category)
- Compliance requirements (GDPR, PCI-DSS = higher category)

## 3. Project Phases and Security Activities

### 3.1 Initiation

**Security Activities:**
- Project classification
- Identify security stakeholders
- Initial security budget

**Deliverables:**
- Project classification
- Security contact person

**Security Gateway:** None (Informational)

### 3.2 Planning

**Security Activities:**
- Define security requirements
- Threat modeling (Category A/B)
- Data Protection Impact Assessment (DPIA) if needed
- Security architecture review
- Security testing plan

**Deliverables:**
- Security Requirements Document
- Threat Model (Category A/B)
- DPIA (if required)
- Security Test Plan

**Security Gateway 1:**
- **Category A/B:** Mandatory
- **Approver:** CISO or Security Architect
- **Criteria:** Security requirements complete, threat model acceptable

### 3.3 Design

**Security Activities:**
- Security architecture review
- Apply secure design patterns
- Authentication/authorization design
- Encryption design
- Logging/monitoring design

**Deliverables:**
- Security Architecture Document
- Data Flow Diagrams
- Authentication/Authorization Design

**Security Gateway 2:**
- **Category A:** Mandatory
- **Approver:** CISO and Security Architect
- **Criteria:** Security architecture acceptable, no critical vulnerabilities in design

### 3.4 Development/Procurement

**Security Activities (Development):**
- Follow secure coding standards
- Code reviews (incl. security review)
- SAST (Static Application Security Testing)
- Dependency scanning
- Secrets management

**Security Activities (Procurement):**
- Vendor security assessment
- Contract review (security clauses)
- Data Processing Agreement (DPA) if needed

**Deliverables:**
- Code review reports
- SAST reports
- Vendor assessment (for procurement)

**Details:** See `0390_Guideline_Secure_SDLC` and `0470_Guideline_Third_Party_Risk_Assessment`

### 3.5 Testing

**Security Testing:**
- DAST (Dynamic Application Security Testing)
- Penetration testing (Category A/B)
- Security test cases
- Vulnerability scanning

**Deliverables:**
- DAST reports
- Penetration test report (Category A/B)
- Security test results

**Security Gateway 3:**
- **Category A/B:** Mandatory
- **Approver:** CISO
- **Criteria:** No critical/high vulnerabilities, all security tests passed

### 3.6 Deployment

**Security Activities:**
- Security configuration review
- Hardening according to baseline
- Configure firewall rules
- Set up monitoring/alerting
- Configure backup

**Deliverables:**
- Security Configuration Checklist
- Firewall Rules Documentation
- Monitoring Setup Documentation

**Security Gateway 4 (Go-Live):**
- **Category A/B:** Mandatory
- **Approver:** CISO
- **Criteria:** Security configuration correct, monitoring active, no open critical findings

### 3.7 Operations and Maintenance

**Security Activities:**
- Regular vulnerability scans
- Patch management
- Security incident monitoring
- Annual security review (Category A)

**Deliverables:**
- Vulnerability scan reports
- Patch compliance reports
- Incident reports

### 3.8 Decommissioning

**Security Activities:**
- Data backup (if required)
- Secure data deletion
- Revoke access
- Remove firewall rules
- Archive documentation

**Deliverables:**
- Deletion log
- Decommissioning checklist

## 4. Security-by-Design Principles

### 4.1 Least Privilege

**Principle:** Minimum required permissions

**Implementation:**
- Role-based access control (RBAC)
- No default admin accounts
- Just-in-Time (JIT) access for privileged operations

### 4.2 Defense in Depth

**Principle:** Multiple security layers

**Implementation:**
- Network segmentation
- Firewall + IDS/IPS
- Endpoint protection + EDR
- Application security + WAF

### 4.3 Fail Secure

**Principle:** Fail to secure state

**Implementation:**
- Default deny (firewall, access control)
- Errors lead to access denial (not access)
- Graceful degradation

### 4.4 Privacy by Design

**Principle:** Data protection from the beginning

**Implementation:**
- Data minimization
- Purpose limitation
- Encryption
- Anonymization/pseudonymization

**Details:** See `0570_Guideline_Data_Protection_Requirements`

## 5. Security Requirements

### 5.1 Functional Security Requirements

**Authentication:**
- Multi-factor authentication (MFA) for external access
- Strong passwords or certificates
- Session management

**Authorization:**
- Role-based access control (RBAC)
- Least privilege
- Segregation of duties

**Encryption:**
- TLS 1.2+ for data transmission
- AES-256 for data at rest
- Secure key management

**Logging:**
- Authentication events
- Access to confidential data
- Administrative actions
- Errors and exceptions

### 5.2 Non-Functional Security Requirements

**Performance:**
- Security controls must not significantly impact performance (< 10%)

**Availability:**
- Security controls highly available
- Failover mechanisms

**Maintainability:**
- Security configuration documented
- Automated security tests

## 6. Threat Modeling

### 6.1 Methodology

**STRIDE:**
- **S**poofing (identity spoofing)
- **T**ampering (manipulation)
- **R**epudiation (deniability)
- **I**nformation Disclosure (information disclosure)
- **D**enial of Service (denial of service)
- **E**levation of Privilege (privilege escalation)

### 6.2 Process

**Steps:**
1. Document system architecture (data flow diagrams)
2. Identify threats (STRIDE)
3. Assess threats (risk)
4. Define mitigation measures
5. Documentation

**Tool:** {{ meta.security.threat_modeling_tool }} (e.g., Microsoft Threat Modeling Tool)

## 7. Security Testing

### 7.1 Test Types

**SAST (Static Application Security Testing):**
- During development
- Automated in CI/CD
- Focus: Code vulnerabilities

**DAST (Dynamic Application Security Testing):**
- During testing phase
- Automated or manual
- Focus: Runtime vulnerabilities

**Penetration Testing:**
- Before go-live (Category A/B)
- Manual by experts
- Focus: Realistic attack scenarios

**Details:** See `0390_Guideline_Secure_SDLC`

### 7.2 Remediation

**Process:**
1. Prioritize findings (by CVSS)
2. Create remediation plan
3. Implement fixes
4. Re-test
5. Documentation

**SLA:**
- Critical: Before go-live
- High: Before go-live or with compensating controls
- Medium: Within 30 days after go-live
- Low: Within 90 days after go-live

## 8. Compliance and Audit

### 8.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Security Gateway Compliance (Category A/B) | 100% |
| Penetration Test Before Go-Live (Category A/B) | 100% |
| Critical Findings Before Go-Live | 0 |
| Security Requirements Completeness | 100% |

### 8.2 Audit Evidence

- Security Requirements Documents
- Threat Models
- Security Test Reports
- Security Gateway Approvals
- DPIA (if required)

## 9. References

### Internal Documents
- `0680_Policy_Security_in_Projects.md`
- `0390_Guideline_Secure_SDLC_Coding_Review_and_Secrets.md`
- `0470_Guideline_Third_Party_Risk_Assessment_and_Cloud_Controls.md`
- `0570_Guideline_Data_Protection_Requirements_and_Data_Processing.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.8** - Information security in project management
- **NIST SP 800-64** - Security Considerations in the System Development Life Cycle
- **OWASP SAMM** - Software Assurance Maturity Model

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

