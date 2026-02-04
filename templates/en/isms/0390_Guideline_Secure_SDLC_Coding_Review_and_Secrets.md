# Guideline: Secure SDLC, Code Reviews and Secrets Management

**Document ID:** 0390  
**Document Type:** Guideline (detailed)  
**Related Policy:** 0380_Policy_Secure_Development.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.25, A.8.26  
**Owner:** {{ meta.development.manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}

---

## 1. Purpose and Scope

This guideline implements the `0380_Policy_Secure_Development.md` and defines:
- Secure Software Development Lifecycle (SSDLC)
- Code review processes and security checks
- Secrets management and secure configuration

**Scope:** All software development at **{{ meta.organization.name }}**

## 2. Secure SDLC Phases

### 2.1 Requirements Phase
- Define security requirements
- Conduct threat modeling
- Identify compliance requirements

### 2.2 Design Phase
- Security architecture review
- Data flow diagrams
- Authentication/authorization design

### 2.3 Development Phase
- Follow secure coding standards
- SAST (Static Application Security Testing)
- Dependency scanning

### 2.4 Testing Phase
- DAST (Dynamic Application Security Testing)
- Penetration testing
- Security test cases

### 2.5 Deployment Phase
- Security configuration review
- Secrets management
- Deployment checklist

### 2.6 Maintenance Phase
- Vulnerability management
- Security patches
- Incident response

## 3. Secure Coding Standards

### 3.1 OWASP Top 10

**Mandatory Prevention:**
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging Failures
10. Server-Side Request Forgery (SSRF)

### 3.2 Input Validation
- Validate all inputs (whitelist approach)
- Parameterized queries (SQL injection prevention)
- Output encoding (XSS prevention)

### 3.3 Authentication & Authorization
- Do not implement custom cryptography
- Use established frameworks (OAuth 2.0, OpenID Connect)
- Least privilege principle

### 3.4 Error Handling
- No sensitive information in error messages
- Centralized error logging
- Graceful degradation

## 4. Code Reviews

### 4.1 Peer Code Review

**Process:**
- Every code change requires at least 1 approval
- Review before merge to main branch
- Checklist for security aspects

**Security Review Checklist:**
- [ ] Input validation present?
- [ ] No secrets in code?
- [ ] Secure cryptography used?
- [ ] Error handling correct?
- [ ] Logging implemented?

### 4.2 Security Champion Review

**For Security-Critical Changes:**
- Additional review by Security Champion
- Security Champion: Developer with security training
- At least 1 Security Champion per team

### 4.3 Automated Code Review

**Tools:**
- **SAST:** {{ meta.security.sast_tool }} (e.g., SonarQube, Checkmarx)
- **Dependency Check:** {{ meta.security.dependency_tool }} (e.g., Snyk, Dependabot)
- **Secrets Scanning:** {{ meta.security.secrets_scanner }} (e.g., GitGuardian, TruffleHog)

**Integration:**
- CI/CD pipeline
- Automatic scans on every commit
- Blocking on critical/high findings

## 5. Secrets Management

### 5.1 Prohibited Practices

**Never:**
- Commit secrets to Git
- Secrets in configuration files (plaintext)
- Secrets in environment variables (production)
- Secrets in logs or error messages

### 5.2 Secrets Management System

**System:** {{ meta.security.secrets_manager }} (e.g., HashiCorp Vault, Azure Key Vault, AWS Secrets Manager)

**Features:**
- Central secrets storage (encrypted)
- Dynamic secrets (short-lived)
- Audit logging of all access
- Secrets rotation

### 5.3 Secrets Rotation

**Frequency:**
- API keys: Every 90 days
- Database credentials: Every 180 days
- Service account passwords: Every 180 days

**Automation:**
- Automatic rotation where possible
- Notification before expiry

### 5.4 Development vs. Production

**Separate Secrets:**
- Dev/Test: Separate secrets (lower privileges)
- Production: Production secrets (higher privileges)
- No reuse between environments

## 6. Dependency Management

### 6.1 Third-Party Libraries

**Requirements:**
- Only use approved libraries
- Regular updates
- Vulnerability scanning

**Approval Process:**
- Request via ticketing system
- Security review of library
- License compliance check
- Approval by security team

### 6.2 Software Composition Analysis (SCA)

**Tools:** {{ meta.security.sca_tool }} (e.g., Snyk, WhiteSource)

**Process:**
- Automatic scanning on build
- Identification of known vulnerabilities (CVEs)
- Alerts on critical vulnerabilities
- Remediation recommendations

### 6.3 Dependency Updates

**Strategy:**
- Security updates: Immediately
- Minor updates: Monthly
- Major updates: After testing

## 7. CI/CD Security

### 7.1 Pipeline Security

**Security Gates:**
1. **Commit:** Secrets scanning
2. **Build:** SAST, dependency check
3. **Test:** Unit tests, security tests
4. **Deploy:** DAST, configuration review

**Blocking On:**
- Critical/high SAST findings
- Known exploited vulnerabilities
- Secrets in code

### 7.2 Container Security

**Image Scanning:**
- Scan all container images
- Only deploy signed images
- Regular re-scans

**Best Practices:**
- Minimal base images
- Non-root user
- Read-only filesystem

### 7.3 Infrastructure as Code (IaC)

**Security Scanning:**
- Terraform, CloudFormation, etc.
- Tools: Checkov, Terrascan
- Check for misconfigurations

## 8. Security Testing

### 8.1 SAST (Static Application Security Testing)

**Frequency:** On every commit  
**Tool:** {{ meta.security.sast_tool }}  
**Coverage:** All programming languages

### 8.2 DAST (Dynamic Application Security Testing)

**Frequency:** Weekly (staging), before every release  
**Tool:** {{ meta.security.dast_tool }}  
**Scope:** Web applications, APIs

### 8.3 Penetration Testing

**Frequency:**
- New applications: Before go-live
- Existing applications: Annually
- After critical changes: Ad-hoc

**Execution:**
- Internal or external pentesters
- Scope definition
- Remediation of all findings
- Re-test after fixes

## 9. Compliance and Audit

### 9.1 Key Performance Indicators (KPIs)

| Metric | Target Value |
|--------|--------------|
| Code review coverage | 100% |
| SAST scan coverage | 100% |
| Critical/high findings (open) | 0 |
| Secrets in code | 0 |

### 9.2 Audit Evidence

- Code review logs
- SAST/DAST reports
- Penetration test reports
- Secrets rotation logs

## 10. References

### Internal Documents
- `0380_Policy_Secure_Development.md`
- `0340_Policy_Vulnerability_and_Patch_Management.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.25** - Secure development lifecycle
- **ISO/IEC 27001:2022 Annex A.8.26** - Application security requirements
- **OWASP ASVS** - Application Security Verification Standard
- **NIST SP 800-218** - Secure Software Development Framework

---

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta.document.next_review }}
