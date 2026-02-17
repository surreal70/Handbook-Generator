# Breach Notification Template (Supervisory Authority)

**Document-ID:** 0610
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
This template is a template for notifying a data breach to the supervisory authority according to Art. 33 GDPR.

Customization required:
- Complete all [TODO] fields
- Ensure all required information is included
- Have Data Protection Officer review
- Obtain management approval
- Submit within 72 hours of awareness

Reference: GDPR Art. 33 (Notification to supervisory authority)
-->

## Notification of a Data Breach pursuant to Art. 33 GDPR

**To:** [TODO: Name of competent supervisory authority]  
**Date:** [TODO: YYYY-MM-DD]  
**Breach-ID:** [TODO: BREACH-YYYY-NNN]  

### 1. Controller

**Organization:** {{ meta-organisation.name }}  
**Address:** [TODO: Full address]  
**Contact Person:** [TODO: Name, Function]  
**Phone:** [TODO: Phone number]  
**Email:** [TODO: Email address]  

### 2. Data Protection Officer

**Name:** [TODO: Name of Data Protection Officer]  
**Phone:** [TODO: Phone number]  
**Email:** [TODO: Email address]  

## A. Nature of the Breach (Art. 33(3)(a))

### Description of the Data Breach

**Date and Time of Breach:**  
[TODO: YYYY-MM-DD HH:MM - YYYY-MM-DD HH:MM]

**Date and Time of Awareness:**  
[TODO: YYYY-MM-DD HH:MM]

**Type of Breach:**  
[ ] Confidentiality breach (unauthorized disclosure or access)  
[ ] Integrity breach (unauthorized alteration)  
[ ] Availability breach (loss or destruction)  

**Detailed Description:**  
[TODO: Describe in detail what happened, how the breach occurred, which systems are affected]

**Example:**
```
On [Date] at [Time], it was discovered that due to a misconfiguration of the 
web server, personal data of customers was publicly accessible for a period 
of [Period]. The data was accessible via an unprotected API interface.
```

### Categories of Personal Data Affected

| Data Category | Description | Special Category (Art. 9) |
|---------------|-------------|---------------------------|
| [TODO: e.g., Master Data] | [TODO: Name, Address, Date of birth] | [ ] Yes [X] No |
| [TODO: e.g., Contact Data] | [TODO: Email, Phone] | [ ] Yes [X] No |
| [TODO: e.g., Financial Data] | [TODO: Account number, Credit card] | [ ] Yes [X] No |

**Special categories of personal data affected (Art. 9):**  
[ ] Yes [ ] No

If Yes, which:  
[ ] Health data  
[ ] Genetic data  
[ ] Biometric data  
[ ] Data revealing racial/ethnic origin  
[ ] Political opinions  
[ ] Religious/philosophical beliefs  
[ ] Trade union membership  
[ ] Sex life/sexual orientation  

### Categories of Data Subjects

**Number of data subjects affected (approximate):** [TODO: e.g., 1,234 persons]

**Categories:**  
[ ] Customers  
[ ] Employees  
[ ] Suppliers/Partners  
[ ] Patients  
[ ] Children  
[ ] Other: [TODO]

**Vulnerable groups affected:**  
[ ] Yes [ ] No

If Yes, which: [TODO: e.g., Children, Patients, Disabled persons]

### Number of Data Records Affected

**Approximate number:** [TODO: e.g., 5,000 records]

## B. Contact Point (Art. 33(3)(b))

**Name and contact details of the Data Protection Officer:**

Name: [TODO: Name]  
Phone: [TODO: Phone number]  
Email: [TODO: Email address]  
Availability: [TODO: e.g., Mon-Fri 9am-5pm, Emergency 24/7]

**Alternative Contact Point:**

Name: [TODO: Name, Function]  
Phone: [TODO: Phone number]  
Email: [TODO: Email address]  

## C. Likely Consequences (Art. 33(3)(c))

### Description of Likely Consequences

**For data subjects:**

[TODO: Describe the possible impacts on the rights and freedoms of data subjects]

**Examples:**
- Identity theft
- Financial loss
- Reputational damage
- Discrimination
- Loss of confidentiality
- Psychological distress

**Risk Assessment:**  
[ ] Low risk  
[ ] Medium risk  
[ ] High risk  
[ ] Very high risk  

**Justification of Risk Assessment:**  
[TODO: Explain why the risk was assessed this way, considering type of data, number of data subjects, protective measures, etc.]

## D. Measures Taken (Art. 33(3)(d))

### Measures to Address the Data Breach

**Immediate Measures (already taken):**

1. [TODO: e.g., Isolated affected systems]
   - Time: [TODO: YYYY-MM-DD HH:MM]
   - Responsible: [TODO: Name/Role]

2. [TODO: e.g., Closed security gap]
   - Time: [TODO: YYYY-MM-DD HH:MM]
   - Responsible: [TODO: Name/Role]

3. [TODO: e.g., Reset passwords]
   - Time: [TODO: YYYY-MM-DD HH:MM]
   - Responsible: [TODO: Name/Role]

### Measures to Mitigate Adverse Effects

**Already implemented:**

1. [TODO: e.g., Notified data subjects]
   - Time: [TODO: YYYY-MM-DD]
   - Method: [TODO: Email/Letter/Phone]

2. [TODO: e.g., Enhanced monitoring]
   - Time: [TODO: YYYY-MM-DD]
   - Description: [TODO]

**Planned Measures:**

1. [TODO: e.g., Implementation of additional security measures]
   - Planned time: [TODO: YYYY-MM-DD]
   - Responsible: [TODO: Name/Role]

2. [TODO: e.g., Employee training]
   - Planned time: [TODO: YYYY-MM-DD]
   - Responsible: [TODO: Name/Role]

## E. Communication to Data Subjects (Art. 34)

**Were data subjects notified?**  
[ ] Yes [ ] No [ ] Planned

**If Yes:**
- Time: [TODO: YYYY-MM-DD]
- Method: [TODO: Email/Letter/Public announcement]
- Number of notified persons: [TODO]

**If No, justification:**  
[ ] No high risk to rights and freedoms  
[ ] Data was encrypted/pseudonymized  
[ ] Subsequent measures eliminate high risk  
[ ] Disproportionate effort (public announcement planned)  

**Explanation:**  
[TODO: Justify why no communication occurred or why the chosen method is appropriate]

## F. Cross-Border Processing

**Is there cross-border processing?**  
[ ] Yes [ ] No

**If Yes:**
- Main establishment: [TODO: Country]
- Other affected Member States: [TODO: Countries]
- Lead supervisory authority: [TODO: Name]

## G. Processor Involved

**Is a processor involved?**  
[ ] Yes [ ] No

**If Yes:**

| Processor | Role | Notified | Time |
|-----------|------|----------|------|
| [TODO: Name] | [TODO: e.g., Cloud provider] | [ ] Yes [ ] No | [TODO: YYYY-MM-DD] |

## H. Additional Information

**Previous data breaches:**  
[ ] Yes [ ] No

If Yes, number in last 12 months: [TODO]

**Insurance:**  
[ ] Cyber insurance available  
[ ] Insurance notified on: [TODO: YYYY-MM-DD]

**External Support:**  
[ ] Forensics provider involved  
[ ] Lawyer consulted  
[ ] Other: [TODO]

**Media Coverage:**  
[ ] Yes [ ] No [ ] Expected

**Criminal Complaint Filed:**  
[ ] Yes [ ] No [ ] Planned

If Yes:
- Authority: [TODO: e.g., Police, Prosecutor]
- Case number: [TODO]
- Date: [TODO: YYYY-MM-DD]

## I. Attachments

[ ] Timeline of events  
[ ] Technical report  
[ ] Forensic analysis  
[ ] Communication to data subjects (sample)  
[ ] Other: [TODO]

## J. Declaration

I hereby confirm that the above information is complete and truthful to the best of my knowledge and belief.

**Place, Date:** [TODO: Place, YYYY-MM-DD]

**Name:** [TODO: Name of Controller/Data Protection Officer]

**Function:** [TODO: Function]

**Signature:** _______________________

## K. Submission Notes

**Submit to:**  
[TODO: Name of supervisory authority]  
[TODO: Address]  
[TODO: Email]  
[TODO: Online portal URL]

**Deadline:** 72 hours from awareness (Art. 33(1))

**If deadline exceeded:**  
Include justification for delay (Art. 33(1))

**Subsequent submission of information:**  
If not all information is immediately available, it can be submitted in phases (Art. 33(4))

**Internal Notes:**

Created by: [TODO: Name]  
Reviewed by: [TODO: Data Protection Officer]  
Approved by: [TODO: Management]  
Submitted on: [TODO: YYYY-MM-DD HH:MM]  
Authority case number: [TODO: Enter after receipt]

