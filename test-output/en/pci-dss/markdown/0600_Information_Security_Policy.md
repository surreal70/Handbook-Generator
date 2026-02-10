# Information Security Policy

**Document ID:** PCI-0600  
**Organization:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Approved by:** CIO  
**Version:** 1.0.0  
**Status:** Draft / In Review / Approved  
**Classification:** internal  
**Last Updated:** {{ meta.document.last_updated }}  

---



## 1. Purpose

This document defines the information security policy for AdminSend GmbH in accordance with PCI-DSS Requirement 12.

### 1.1 Objectives

- **Security Governance:** Establish a security framework
- **Risk Management:** Systematic risk identification and treatment
- **Compliance:** Fulfillment of PCI-DSS Requirement 12
- **Awareness:** Sensitization of all employees

### 1.2 Scope

**Affected Persons:**
- All employees
- All service providers
- All persons with access to CDE or CHD

## 2. Information Security Policy

### 2.1 Security Objectives

**Confidentiality:**
- Protection of cardholder data from unauthorized access
- Access control according to need-to-know principle
- Encryption of sensitive data

**Integrity:**
- Protection against unauthorized modification
- Validation of data changes
- Audit trails for all changes

**Availability:**
- Ensuring system availability
- Business continuity planning
- Disaster recovery

### 2.2 Security Principles

**Defense in Depth:**
- Multi-layered security controls
- No single point of failure
- Redundancy of critical systems

**Least Privilege:**
- Minimum required permissions
- Regular review
- Time-limited privileged access

**Separation of Duties:**
- Separation of critical functions
- Four-eyes principle
- No single person with complete control

**Secure by Default:**
- Secure default configurations
- Deactivation of unnecessary services
- Hardening of all systems

## 3. Roles and Responsibilities

### 3.1 Governance Structure

**Executive Management:**
- Overall responsibility for information security
- Approval of security policies
- Provision of resources

**CISO (Chief Information Security Officer):**
- Responsible for security program
- Compliance monitoring
- Incident response coordination
- Reporting to executive management

**PCI-DSS Program Manager:**
- Responsible for PCI-DSS compliance
- Coordination of assessments
- Documentation and evidence
- Liaison to QSA and acquiring banks

**IT Security Team:**
- Implementation of security controls
- Security monitoring
- Vulnerability management
- Incident response

**IT Operations:**
- System administration
- Patch management
- Backup and recovery
- Change management

**All Employees:**
- Compliance with security policies
- Reporting of security incidents
- Participation in security awareness training

### 3.2 RACI Matrix

| Activity | Executive | CISO | PCI Manager | IT Security | IT Ops | Employees |
|----------|-----------|------|-------------|-------------|--------|-----------|
| Policy approval | A | R | C | C | I | I |
| Security controls | C | A | C | R | R | I |
| Compliance monitoring | I | A | R | C | I | I |
| Incident response | I | A | C | R | C | R |
| Security awareness | C | A | C | R | I | R |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 4. Risk Management

### 4.1 Risk Analysis Process

**Annual Risk Analysis:**
1. Asset identification
2. Threat identification
3. Vulnerability analysis
4. Risk assessment
5. Risk treatment
6. Documentation

**Risk Assessment:**
- Likelihood (1-5)
- Impact (1-5)
- Risk Score = Likelihood × Impact

**Risk Matrix:**

| Risk Score | Category | Treatment |
|------------|----------|-----------|
| 20-25 | Critical | Immediate measures |
| 15-19 | High | Measures within 30 days |
| 10-14 | Medium | Measures within 90 days |
| 5-9 | Low | Monitoring |
| 1-4 | Very low | Accept |

### 4.2 Risk Treatment

**Options:**
- **Avoid:** Discontinue activity
- **Reduce:** Implement controls
- **Transfer:** Insurance, outsourcing
- **Accept:** Consciously accept risk (with approval)

**Risk Acceptance:**
- Only by CISO or executive management
- Documented justification
- Regular review
- Time-limited

## 5. Security Awareness Program

### 5.1 Training Program

**Mandatory Training:**
- Onboarding training (upon hiring)
- Annual refresher training
- Role-specific training
- Ad-hoc training as needed

**Training Content:**
- PCI-DSS basics
- Handling cardholder data
- Password security
- Phishing recognition
- Social engineering
- Incident reporting
- Clean desk policy
- Acceptable use policy

### 5.2 Training Documentation

**Required Evidence:**
- Training attendance lists
- Training materials
- Training certificates
- Knowledge tests
- Refresher training

**Tracking:**
- Training database
- Automatic reminders
- Compliance reporting

### 5.3 Awareness Campaigns

**Regular Campaigns:**
- Monthly security newsletters
- Phishing simulations
- Security posters
- Intranet articles
- Team meetings

## 6. Incident Response

### 6.1 Incident Response Plan

**Phases:**
1. **Preparation:** Preparation and training
2. **Detection:** Detection of incidents
3. **Analysis:** Analysis and assessment
4. **Containment:** Containment
5. **Eradication:** Eradication
6. **Recovery:** Recovery
7. **Post-Incident:** Lessons learned

**Incident Response Team:**
- Incident Response Manager
- IT Security Analysts
- IT Operations
- Legal/Compliance
- PR/Communications
- Executive Management (for major incidents)

### 6.2 Incident Classification

**Severity Levels:**

| Severity | Description | Examples | Response Time |
|----------|-------------|----------|---------------|
| Critical | Massive impact | Data exfiltration, ransomware | Immediate |
| High | Significant impact | Malware infection, unauthorized access | < 1 hour |
| Medium | Moderate impact | Phishing success, policy violation | < 4 hours |
| Low | Minor impact | Suspicious activity | < 24 hours |

### 6.3 Incident Reporting

**Reporting Obligation:**
- All employees must report incidents
- Report to IT Security or Helpdesk
- No fear of consequences for reporting
- Quick reporting is important

**Reporting Channels:**
- Email: [TODO: security@organization.com]
- Phone: [TODO: +1 XXX XXX XXXX]
- Incident portal: [TODO: URL]
- Helpdesk: [TODO: Phone]

### 6.4 Breach Notification

**For Data Breaches:**
- Notification of acquiring banks
- Notification of card brands
- Notification of data protection authority (GDPR)
- Notification of affected cardholders
- Forensic investigation

**Timeframe:**
- Acquiring banks: Immediately
- Card brands: According to requirements
- Data protection authority: 72 hours (GDPR)
- Cardholders: Without undue delay

## 7. Service Provider Management

### 7.1 Service Provider Selection

**Due Diligence:**
- Check PCI-DSS compliance status
- Request AOC (Attestation of Compliance)
- Assess security controls
- Contractual security requirements

**Requirements:**
- PCI-DSS compliant (if CHD access)
- Current AOC
- Incident response process
- Insurance

### 7.2 Service Provider Monitoring

**Annual Review:**
- AOC validation
- Security controls review
- Incident review
- Contract compliance

**Documentation:**
- List of all service providers
- AOCs
- Contracts with PCI clauses
- Review protocols

### 7.3 Service Provider Contracts

**Required Clauses:**
- PCI-DSS compliance obligation
- Incident notification
- Audit rights
- Data protection (GDPR)
- Liability
- Termination for non-compliance

## 8. Document Management

### 8.1 Document Control

**Requirements:**
- Version control
- Approval process
- Regular reviews
- Archiving of old versions

**Document Lifecycle:**
1. Creation
2. Review
3. Approval
4. Publication
5. Annual review
6. Update or archiving

### 8.2 Document Retention

**Retention Periods:**
- Policies: Current + 3 years
- Audit reports: 3 years
- Logs: 1 year
- Incident reports: 3 years
- Training records: 3 years

## 9. Compliance Monitoring

### 9.1 Continuous Monitoring

**Monitoring Activities:**
- Daily security monitoring
- Weekly compliance checks
- Monthly compliance reports
- Quarterly reviews
- Annual assessments

### 9.2 Compliance Reporting

**Reports:**
- Monthly compliance status to CISO
- Quarterly report to executive management
- Annual compliance report
- Ad-hoc reports for incidents

### 9.3 Internal Audits

**Annual Audits:**
- All PCI-DSS requirements
- Sample-based
- Documentation of findings
- Corrective actions
- Follow-up

## 10. Policy Review

### 10.1 Annual Review

**Process:**
1. Review all policies
2. Identify changes
3. Make updates
4. Obtain approval
5. Communicate to employees
6. Update training

**Responsible:** CISO

### 10.2 Ad-hoc Reviews

**Triggers:**
- Significant changes in CDE
- New threats
- Regulatory changes
- After major incidents
- Audit findings

## 11. Compliance Validation

### 11.1 Validation Activities

**Quarterly:**
- Policy compliance checks
- Training status review
- Service provider AOC validation

**Annually:**
- Complete risk analysis
- Internal audits
- QSA assessment
- Policy review

### 11.2 Validation Documentation

**Required Evidence:**
- Information security policy
- Risk analysis reports
- Training records
- Incident response protocols
- Service provider AOCs
- Audit reports

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |


