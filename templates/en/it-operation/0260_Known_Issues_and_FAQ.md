# Known Issues and FAQ

## Overview

This document contains known issues and workarounds, frequently asked questions (FAQ), and troubleshooting tips for the IT service. The goal is to provide quick solutions for recurring problems and increase support efficiency.

**Document Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Organization:** {{ meta.organization.name }}

---

## Known Issues

### Issue Tracking

All known issues are captured in the ticketing system with the label "Known Issue" and documented here.

**Responsible:** {{ meta.it_operations_manager.name }}  
**Review Cycle:** Monthly

---

### KI-001: [TODO: Issue Title]

**Status:** Open / In Progress / Resolved  
**Priority:** P1 (Critical) / P2 (High) / P3 (Medium) / P4 (Low)  
**Created:** [TODO: Date]  
**Last Update:** [TODO: Date]  
**Ticket ID:** [TODO: Ticket Number]

#### Description
[TODO: Detailed description of the issue]

#### Affected Systems
- [TODO: System 1]
- [TODO: System 2]

#### Symptoms
- [TODO: Symptom 1]
- [TODO: Symptom 2]

#### Root Cause
[TODO: Cause of the issue, if known]

#### Workaround
```
[TODO: Step-by-step workaround]
1. Step 1
2. Step 2
3. Step 3
```

#### Permanent Solution
- **Status:** Planned / In Development / Tested / Deployed
- **ETA:** [TODO: Expected date]
- **Responsible:** [TODO: Name]

---

## Frequently Asked Questions (FAQ)

### General Questions

#### Q: How do I reach IT support?

**A:** IT support can be reached through the following channels:
- **Email:** {{ meta.service_desk_lead.email }}
- **Phone:** {{ meta.service_desk_lead.phone }}
- **Ticketing System:** [TODO: URL]
- **Chat:** [TODO: Chat Channel]

**Support Hours:**
- Mon-Fri: 08:00-18:00
- 24/7 for critical incidents (P1)

---

#### Q: How do I create a support ticket?

**A:** Support tickets can be created through the following methods:

1. **Web Portal:**
   - Go to [TODO: Ticketing URL]
   - Log in with SSO
   - Click "New Ticket"
   - Fill out form and submit

2. **Email:**
   - Email to {{ meta.service_desk_lead.email }}
   - Subject: Brief problem description
   - Content: Detailed description, screenshots

3. **Phone:**
   - Call {{ meta.service_desk_lead.phone }}
   - Describe problem
   - Note ticket number

---

### Access and Authentication

#### Q: I forgot my password. What should I do?

**A:** Password reset via self-service portal:

1. Go to [TODO: Self-Service URL]
2. Click "Forgot Password"
3. Enter username or email
4. Answer security questions or receive code via email/SMS
5. Set new password

**Alternative:** Contact IT support

---

#### Q: How do I set up MFA (Multi-Factor Authentication)?

**A:** MFA setup:

1. Go to [TODO: MFA Portal URL]
2. Log in with current password
3. Choose MFA method:
   - **Authenticator App** (recommended): Scan QR code
   - **SMS:** Verify phone number
   - **Hardware Token:** Register token
4. Generate backup codes and store securely
5. Test MFA

**Important:** Keep backup codes in a safe place!

---

### Applications

#### Q: The application loads very slowly. What can I do?

**A:** Performance troubleshooting:

1. **Clear browser cache:**
   - Chrome: Ctrl+Shift+Del
   - Firefox: Ctrl+Shift+Del
   - Edge: Ctrl+Shift+Del

2. **Disable browser extensions:**
   - Temporarily disable all extensions
   - Test if performance improves

3. **Test another browser:**
   - Try Chrome, Firefox, or Edge

4. **Check network:**
   - Run speed test
   - Check VPN connection

5. **Check system resources:**
   - Open Task Manager
   - Check CPU/RAM usage
   - Close other programs

**If problem persists:** Create ticket with:
- Browser and version
- Affected application
- Time of problem
- Screenshot

---

### Email

#### Q: I cannot send emails. What should I do?

**A:** Email sending troubleshooting:

1. **Check outbox:**
   - Are emails stuck in outbox?
   - Error message present?

2. **Check mailbox size:**
   - Is mailbox full?
   - Archive/delete old emails

3. **Check attachments:**
   - Are attachments too large? (Max: [TODO: Size])
   - Compress attachments or send via file sharing

4. **Check recipient address:**
   - Is email address correct?
   - Typo?

5. **Spam filter:**
   - Was email marked as spam?

**If problem persists:** Contact IT support

---

### Files and Storage

#### Q: I accidentally deleted a file. Can it be recovered?

**A:** File recovery:

1. **Check recycle bin:**
   - Windows: Recycle Bin on desktop
   - macOS: Trash in dock
   - Linux: Trash folder

2. **Network drive:**
   - Check previous versions (Right-click → Properties → Previous Versions)
   - Shadow copies available?

3. **Backup recovery:**
   - Create ticket (P3 - Medium)
   - Provide filename, path, and approximate deletion date
   - IT team restores from backup

**Important:** The sooner reported, the higher the success rate!

**Backup Retention:**
- Daily backups: 30 days
- Weekly backups: 90 days
- Monthly backups: 1 year

---

## Troubleshooting Tips

### General Troubleshooting Steps

1. **Restart:**
   - Often the simplest solution
   - Restart computer, application, or service

2. **Document error:**
   - Create screenshot
   - Note error message
   - Record time

3. **Reproduce:**
   - Trigger problem again
   - Document steps

4. **Isolate:**
   - Different computer?
   - Different browser?
   - Different network?

5. **Research:**
   - Check known issues (this document)
   - Search wiki
   - Ask colleagues

6. **Escalate:**
   - Create ticket
   - Contact IT support

---

## Self-Service Resources

### Documentation
- **Wiki:** [TODO: Wiki URL]
- **Video Tutorials:** [TODO: Video URL]
- **Manuals:** [TODO: Manual URL]

### Tools
- **Self-Service Portal:** [TODO: Portal URL]
- **Password Reset:** [TODO: Reset URL]
- **Software Download:** [TODO: Download URL]

---

## Feedback and Improvements

### Give Feedback

Do you have suggestions for improving this document or IT services?

**Contact:**
- **Email:** {{ meta.it_operations_manager.email }}
- **Feedback Form:** [TODO: Form URL]

### Document Updates

This document is regularly updated based on:
- New known issues
- Frequently asked questions
- User feedback
- Process improvements

**Review Cycle:** Monthly  
**Responsible:** {{ meta.it_operations_manager.name }}

---

**Last Update:** {{ meta.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta.it_operations_manager.email }}
