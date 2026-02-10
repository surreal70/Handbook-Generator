# Guideline: IAM - Joiner, Mover, Leaver and Access Requests

<!-- 
TEMPLATE AUTHOR NOTE:
This guideline provides detailed implementation guidance for Identity and Access Management,
specifically covering the Joiner-Mover-Leaver lifecycle and access request processes.
Customize based on your organization's HR systems, IAM tools, and approval workflows.
-->

**Document ID:** 0230  
**Document Type:** Guideline (detailed)  
**Related Policy:** 0220_Policy_Access_Control_and_Identity_Management.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.15, A.5.16, A.5.18  
**Owner:** {{ meta.it_operations.manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose and Scope

This guideline implements the `0220_Policy_Access_Control_and_Identity_Management.md` and defines detailed processes for:
- **Joiner:** Onboarding new employees and access provisioning
- **Mover:** Role changes and access adjustments
- **Leaver:** Offboarding and access revocation
- **Access Requests:** Process for ad-hoc access requests

**Scope:** All employees, contractors, and third parties at **{{ meta.organization.name }}**

## 2. Joiner Process (Onboarding)

### 2.1 Process Overview

**Trigger:** HR creates new employee in HR system ({{ meta.hr.system }})

**Timeline:**
- **Standard Accounts:** Provisioning by 1 day before start date
- **Special Access:** Provisioning by 3 days before start date
- **External Contractors:** Provisioning after contract signing

### 2.2 Detailed Workflow

**Phase 1: HR Initiation (T-5 days)**
1. HR creates employee record in {{ meta.hr.system }}
2. HR defines:
   - Department, role, location
   - Supervisor, cost center
   - Start date, contract type (permanent, temporary, internship)
3. Automatic notification to IT operations

**Phase 2: IT Provisioning (T-3 days)**
1. **Account Creation:**
   - Active Directory / Azure AD account
   - Email mailbox ({{ meta.email.system }})
   - Username per schema: `{{ meta.naming.user_format }}` (e.g., firstname.lastname)
   - Initial password (temporary, must be changed at first login)

2. **Basic Access (automatic via role model):**
   - Access to intranet and collaboration tools
   - Standard applications for department
   - Network drives according to department membership
   - VPN access (if remote work)

3. **Hardware Provisioning:**
   - Laptop/desktop per role (see hardware catalog)
   - Mobile device (if required)
   - Peripherals (monitor, keyboard, mouse)
   - Asset tagging and inventory

**Phase 3: Special Access (T-2 days)**
1. Supervisor requests special access via self-service portal
2. Approval by resource owner
3. Provisioning by IT operations or automated

**Phase 4: Onboarding Day (T-0)**
1. **Welcome Email:**
   - Credentials (initial password)
   - Links to training and policies
   - IT support contact information
2. **First Login:**
   - Password change enforced
   - MFA registration (authenticator app, hardware token)
   - Acceptable Use Policy confirmation
3. **IT Orientation:**
   - Device usage, VPN access
   - Password manager training
   - Phishing awareness basics

### 2.3 Role-Based Access (RBAC)

**Standard Roles:**

| Role | Description | Automatic Access |
|------|-------------|------------------|
| Employee_Standard | All employees | Intranet, email, Office 365, VPN |
| Employee_Developer | Developers | + Git, CI/CD, dev environments |
| Employee_Finance | Finance department | + ERP, accounting software |
| Employee_HR | Human resources | + HR system, applicant management |
| Employee_Sales | Sales | + CRM, quotation system |
| Contractor_Standard | External contractors | Basic access, time-limited |
| Contractor_Developer | External developers | + Dev access, time-limited |

**Privileged Roles:**
- `Admin_System`: System administrators (Windows, Linux)
- `Admin_Network`: Network administrators
- `Admin_Security`: Security team
- `Admin_Database`: Database administrators

### 2.4 External Contractors and Third Parties

**Special Considerations:**
- **Contract Review:** IT access only after contract signing and NDA
- **Time Limitation:** Accounts automatically deactivated after contract end
- **Restricted Access:** Only project-related resources
- **Sponsorship:** Every external account requires internal sponsor
- **Recertification:** Quarterly review by sponsor

## 3. Mover Process (Role Change)

### 3.1 Process Overview

**Trigger:** HR updates employee data (department change, promotion, new role)

**Timeline:** Access adjustment within 2 business days after HR change

### 3.2 Detailed Workflow

**Phase 1: HR Change**
1. HR updates employee record in {{ meta.hr.system }}
2. Changes: Department, role, supervisor, location
3. Automatic notification to IT operations and previous/new supervisors

**Phase 2: Access Review**
1. **Previous Supervisor:** Confirms revocation of no longer needed access
2. **New Supervisor:** Requests new required access
3. **IT Operations:** Reviews current access and plans changes

**Phase 3: Access Adjustment**
1. **Revoke Old Access:**
   - Removal from old department groups
   - Revocation of department-specific application access
   - Archiving old emails (if mailbox change)
2. **Provision New Access:**
   - Addition to new department groups
   - Provisioning new application access
   - Adjustment of network drives and permissions

**Phase 4: Documentation**
1. Update CMDB and asset management
2. Documentation of access changes
3. Notification to employee about changes

### 3.3 Promotions and Privilege Elevation

**Additional Checks for Privilege Elevation:**
- **Approval:** CISO approval for privileged roles
- **Background Check:** Extended verification for admin rights
- **Training:** Additional security training for privileged users
- **Monitoring:** Increased monitoring of privileged activities

## 4. Leaver Process (Offboarding)

### 4.1 Process Overview

**Trigger:** HR marks employee as leaving in {{ meta.hr.system }}

**Timeline:**
- **Planned Departure:** Deactivation on last working day
- **Unplanned Departure:** Immediate deactivation (e.g., termination, emergency)

### 4.2 Detailed Workflow

**Phase 1: Preparation (T-14 days)**
1. HR informs IT operations about departure date
2. **Knowledge Transfer:**
   - Supervisor identifies critical access and information
   - Handover to successor or team
   - Documentation of passwords for shared accounts (in password manager)
3. **Data Backup:**
   - Backup of personal drives
   - Email mailbox archiving
   - Handover of project-relevant files

**Phase 2: Last Working Day (T-0)**
1. **Account Deactivation (End of Business Day):**
   - Active Directory / Azure AD account deactivated
   - Email forwarding to supervisor (temporary, 30 days)
   - VPN access blocked
   - All application access revoked
2. **Hardware Return:**
   - Laptop, mobile device, peripherals
   - Access cards, keys
   - Asset inventory updated
3. **Exit Interview:**
   - Return of all company property
   - Reminder of confidentiality obligations
   - Confirmation of data return

**Phase 3: Post-Offboarding (T+30 days)**
1. **Account Deletion:**
   - After 30 days: Final account deletion
   - Email archiving per retention policy ({{ meta.retention.email_years }} years)
   - Deletion of personal data (GDPR compliant)
2. **License Release:**
   - Return of software licenses
   - Update license management
3. **Documentation:**
   - Offboarding checklist completed
   - Audit trail for compliance

### 4.3 Emergency Offboarding

**Immediate Deactivation for:**
- Termination for cause
- Security incidents or suspected abuse
- Court orders

**Process:**
1. **Immediate Suspension (within 1 hour):**
   - All accounts deactivated
   - VPN and remote access blocked
   - Access cards deactivated
   - Mobile devices remotely wiped (if MDM)
2. **Forensics:**
   - Backup of logs and activities
   - Analysis in case of suspected data abuse
   - Involvement of legal and HR
3. **Communication:**
   - Information to supervisor and security team
   - Documentation for legal purposes

## 5. Access Requests

### 5.1 Self-Service Portal

**Access:** {{ meta.iam.portal_url }}

**Functions:**
- Request new access (applications, network drives, groups)
- Overview of own access
- Status tracking of requests
- Recertification of own access

### 5.2 Request Workflow

**Step 1: Request Submission**
1. Employee submits request via self-service portal
2. **Required Information:**
   - Resource/application
   - Business justification
   - Required permission level
   - Time period (permanent or time-limited)

**Step 2: Approval**
1. **Supervisor:** Reviews business necessity (1st approval)
2. **Resource Owner:** Reviews technical authorization (2nd approval)
3. **CISO:** Additional approval for privileged access
4. **Automatic Approval:** For standard access per role model

**Step 3: Provisioning**
1. **Automatic:** For standard applications (within 15 minutes)
2. **Manual:** For special access (within 1 business day)
3. **Notification:** Email to requester upon completion

**Step 4: Documentation**
1. Audit trail in IAM system
2. CMDB update
3. Compliance reporting

### 5.3 Time-Limited Access

**Use Cases:**
- Project-related access
- Substitutions (vacation, illness)
- External contractors
- Test and development access

**Automatic Deactivation:**
- System automatically deactivates access after expiration date
- Notification to user 7 days before expiration
- Extension only through new request

## 6. Recertification

### 6.1 Regular Access Reviews

**Frequency:**
- **Standard Users:** Annual recertification
- **Privileged Users:** Quarterly recertification
- **External Contractors:** Quarterly recertification
- **Critical Systems:** Monthly recertification

### 6.2 Recertification Process

**Step 1: Automatic Campaign**
1. IAM system starts recertification campaign
2. Email to supervisors with list of employee access
3. Deadline: 14 days for confirmation

**Step 2: Review by Supervisors**
1. Supervisor reviews each access:
   - **Confirm:** Access still required
   - **Revoke:** Access no longer needed
   - **Escalate:** Uncertainty, query to resource owner
2. Documentation of decision

**Step 3: Automatic Enforcement**
1. Confirmed access remains active
2. Unconfirmed access is automatically revoked after deadline
3. Escalated cases are forwarded to CISO

**Step 4: Reporting**
1. Compliance report for audit
2. Identification of access anomalies
3. Optimization of role model

### 6.3 Privileged Access

**Additional Controls:**
- **Four-Eyes Principle:** Two approvals required
- **Just-in-Time (JIT) Access:** Privileges only when needed, time-limited
- **Privileged Access Management (PAM):** Management via PAM system ({{ meta.security.pam_solution }})
- **Session Recording:** Recording of privileged sessions for audit

## 7. Technical Implementation

### 7.1 IAM Technology Stack

**Systems:**
- **Identity Provider:** {{ meta.iam.idp }} (e.g., Azure AD, Okta)
- **HR System:** {{ meta.hr.system }} (e.g., SAP SuccessFactors, Workday)
- **IAM Portal:** {{ meta.iam.portal }} (e.g., SailPoint, Saviynt)
- **PAM System:** {{ meta.security.pam_solution }} (e.g., CyberArk, BeyondTrust)
- **CMDB:** {{ meta.itsm.cmdb }} (e.g., ServiceNow, Jira Service Management)

**Integration:**
- HR system → IAM system (automatic synchronization)
- IAM system → Active Directory / Azure AD (provisioning)
- IAM system → Applications (SCIM, SAML, API)

### 7.2 Automation

**Automated Processes:**
- Account creation for joiner (within 1 hour after HR entry)
- Role-based access provisioning (RBAC)
- Account deactivation for leaver (on last working day)
- Time-limited access (automatic deactivation)
- Recertification campaigns (automatic start)

**Manual Processes:**
- Special access outside role model
- Privileged access (after approval)
- Emergency offboarding (immediate suspension)

## 8. Compliance and Audit

### 8.1 Key Performance Indicators (KPIs)

| Metric | Target Value | Measurement |
|--------|--------------|-------------|
| Joiner Provisioning | < 1 day | IAM system |
| Leaver Deactivation | 100% on last day | IAM system |
| Access Requests (Processing Time) | < 1 business day | IAM system |
| Recertification (Completion Rate) | > 95% | IAM system |
| Orphaned Accounts | 0 | Quarterly review |

### 8.2 Audit Evidence

**Documentation:**
- Joiner/Mover/Leaver logs (audit trail)
- Access requests and approvals
- Recertification reports
- Privileged access and approvals
- Emergency offboarding documentation

**Audit Frequency:**
- Internal audits: Quarterly
- External audits: Annually (ISO 27001)
- Ad-hoc audits: For security incidents

## 9. References

### Internal Documents
- `0220_Policy_Access_Control_and_Identity_Management.md` - Parent policy
- `0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md` - Authentication
- `0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md` - HR security
- `0640_Policy_Ausnahmen_und_Risk_Waivers.md` - Exception process

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.15** - Access control
- **ISO/IEC 27001:2022 Annex A.5.16** - Identity management
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights
- **NIST SP 800-63** - Digital Identity Guidelines

---

**Approved by:**  
{{ meta.ciso.name }}, CISO  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }}

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
