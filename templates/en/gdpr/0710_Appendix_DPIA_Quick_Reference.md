# Appendix: DPIA Quick Reference

**Document-ID:** 0710  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Reference  
**Classification:** Internal  
**Last Update:** {{ meta.date }}  

---

<!-- 
This document is a quick reference for Data Protection Impact Assessments (DPIA).
It helps decide when a DPIA is required and how to conduct it.

Reference: GDPR Art. 35 (Data protection impact assessment)
-->

## When is a DPIA Required?

### Mandatory Cases (Art. 35(3))

A DPIA is **always** required for:

1. **Systematic and extensive evaluation of personal aspects**
   - Automated processing including profiling
   - Basis for decisions with legal effect or significant impact

2. **Large-scale processing of special categories (Art. 9)**
   - Health data, genetic data, biometric data
   - Data concerning criminal convictions and offences

3. **Systematic large-scale monitoring of publicly accessible areas**
   - Video surveillance
   - Tracking and monitoring

### Supervisory Authority Blacklist

Additionally required for (examples):
- Scoring and rating
- Automated decisions with legal effect
- Systematic monitoring
- Processing sensitive data at large scale
- Data matching or combination
- Data of vulnerable persons (children, patients, employees)
- Innovative technologies (AI, biometrics)
- Third country transfer without adequacy decision

### Threshold Criteria

**Number of Data Subjects:**
- < 5,000: Usually no DPIA required
- 5,000 - 20,000: DPIA recommended
- > 20,000: DPIA usually required

**Risk Factors (more applicable, more likely DPIA):**
- [ ] Evaluation or scoring
- [ ] Automated decisions
- [ ] Systematic monitoring
- [ ] Special categories (Art. 9)
- [ ] Vulnerable groups
- [ ] Large-scale processing
- [ ] Data matching
- [ ] Innovative technology
- [ ] Third country transfer
- [ ] Prevention of rights exercise

**Rule of thumb:** With 2 or more risk factors → Conduct DPIA

---

## DPIA Process (Quick Overview)

### Phase 1: Preparation

1. **Check:** Is DPIA required?
2. **Form team:** Controller, DPO, IT, Business unit
3. **Gather information:** Processing description, data flows, systems

### Phase 2: Execution

4. **Description:** Describe processing in detail
5. **Necessity:** Check necessity and proportionality
6. **Identify risks:** Systematic risk analysis
7. **Define measures:** Technical and organizational measures
8. **Assess residual risk:** Is residual risk acceptable?

### Phase 3: Consultation

9. **Data Protection Officer:** Obtain opinion
10. **Data subjects (optional):** Seek views
11. **Supervisory authority (if required):** Consult if high residual risk

### Phase 4: Documentation

12. **Document DPIA:** Use Template 0410
13. **Approval:** Controller approves
14. **Archiving:** Retain DPIA

---

## Risk Assessment Matrix

### Likelihood

| Level | Description | Example |
|-------|-------------|---------|
| **Low** | Unlikely | Encrypted data, strong security measures |
| **Medium** | Possible | Standard security, known vulnerabilities |
| **High** | Likely | Weak security, publicly accessible |

### Severity of Impact

| Level | Description | Example |
|-------|-------------|---------|
| **Low** | Minor impact | General contact data, no sensitive data |
| **Medium** | Significant impact | Financial data, contract data |
| **High** | Severe impact | Health data, identity theft possible |

### Risk Matrix

|  | **Low Severity** | **Medium Severity** | **High Severity** |
|---|---|---|---|
| **Low Likelihood** | Low Risk | Medium Risk | Medium Risk |
| **Medium Likelihood** | Medium Risk | Medium Risk | High Risk |
| **High Likelihood** | Medium Risk | High Risk | Very High Risk |

**Action Recommendation:**
- **Low Risk:** Standard measures sufficient
- **Medium Risk:** Additional measures required
- **High Risk:** Comprehensive measures, possibly consult authority
- **Very High Risk:** Consultation with authority required

---

## Typical Measures

### Technical Measures

- **Encryption:** End-to-end, transport, storage
- **Pseudonymization:** Separation of identification data
- **Anonymization:** Irreversible removal of personal data
- **Access control:** Role-based, Least Privilege
- **Logging:** Traceability, Audit trails
- **Backup:** Regular, tested
- **Monitoring:** Anomaly detection, Intrusion Detection

### Organizational Measures

- **Policies:** Data protection policy, Security policy
- **Training:** Regular, target group-specific
- **Contracts:** Processor agreements, NDAs
- **Processes:** Incident response, Erasure concept
- **Documentation:** Processing records, TOMs
- **Audits:** Regular reviews

### Privacy by Design/Default

- **Data minimization:** Collect only necessary data
- **Purpose limitation:** Clear purpose definition
- **Storage limitation:** Automatic deletion
- **Transparency:** Clear information for data subjects
- **User-friendliness:** Easy exercise of rights

---

## Checklist: DPIA Required?

- [ ] Systematic and extensive evaluation of personal aspects?
- [ ] Automated decisions with legal effect?
- [ ] Large-scale processing of special categories (Art. 9)?
- [ ] Systematic monitoring of publicly accessible areas?
- [ ] Scoring or rating?
- [ ] Processing sensitive data at large scale?
- [ ] Data matching or combination?
- [ ] Data of vulnerable persons (children, patients)?
- [ ] Innovative technologies (AI, biometrics)?
- [ ] Third country transfer without adequacy decision?
- [ ] More than 20,000 data subjects?
- [ ] 2 or more risk factors apply?

**If 1 or more questions answered Yes:** Conduct DPIA!

---

## Prior Consultation with Supervisory Authority

**Required when:**
- Residual risk remains high despite measures
- No adequate measures possible
- Uncertainty about adequacy of measures

**Process:**
1. Complete DPIA fully
2. Document all possible measures
3. Request to supervisory authority with DPIA documentation
4. Authority has 8 weeks (extendable to 14 weeks)
5. Implement authority's opinion

---

## Avoid Common Mistakes

❌ **Conduct DPIA too late** → Before processing starts!  
❌ **Superficial risk analysis** → Systematic and detailed!  
❌ **Not involving DPO** → Always consult!  
❌ **No concrete measures** → Specific and implementable!  
❌ **Not updating DPIA** → Review upon changes!  
❌ **No documentation** → Document completely!

---

## Useful Resources

**Templates:**
- Template 0410: DPIA Template
- Template 0400: DPIA Fundamentals

**External Resources:**
- WP29 Guidelines on DPIA (wp248rev.01)
- Supervisory authority blacklists
- DPIA tools from supervisory authorities

**Contact:**
- Data Protection Officer: [TODO: Contact]
- Supervisory Authority: [TODO: Contact]

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
