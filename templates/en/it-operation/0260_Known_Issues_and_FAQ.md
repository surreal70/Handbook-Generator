# Known Issues and FAQ

**Document-ID:** [FRAMEWORK]-0260
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

## Overview

This document contains known issues and workarounds, frequently asked questions (FAQ), and troubleshooting tips for the IT service. The goal is to provide quick solutions for recurring problems and increase support efficiency.

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organization:** {{ meta-organisation.name }}

## Known Issues

### Issue Tracking

All known issues are captured in the ticketing system with the label "Known Issue" and documented here.

**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**Review Cycle:** Monthly

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

#### Affected Users
[TODO: Number or description of affected users]

#### Communication
- [TODO: Date] - Users informed
- [TODO: Date] - Update communicated
- [TODO: Date] - Solution communicated

### KI-002: Intermittent Network Timeouts

**Status:** In Progress  
**Priority:** P2 (High)  
**Created:** 2025-01-15  
**Last Update:** 2025-01-28  
**Ticket ID:** INC-12345

#### Description
Users experience sporadic network timeouts when accessing internal applications. The timeouts occur irregularly and last 30-60 seconds.

#### Affected Systems
- Intranet Portal
- File Server
- Email System

#### Symptoms
- Connection drops without error message
- Slow loading times
- Timeout errors after 30-60 seconds

#### Root Cause
Core switch overload during backup times (22:00-02:00).

#### Workaround
```
1. Perform critical work outside backup times
2. On timeout: Reload page (F5)
3. Use alternative route via VPN (if available)
```

#### Permanent Solution
- **Status:** Planned
- **ETA:** Q2 2026
- **Action:** Upgrade core switch to higher bandwidth
- **Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Affected Users
All internal users during backup times

### KI-003: Slow Database Queries

**Status:** Resolved  
**Priority:** P2 (High)  
**Created:** 2025-01-10  
**Resolved:** 2025-01-25  
**Ticket ID:** INC-12340

#### Description
Certain database queries ran very slowly (> 10 seconds), leading to timeouts in the application.

#### Affected Systems
- Production Database
- Web Application

#### Symptoms
- Slow page load times
- Timeout errors
- High CPU load on DB server

#### Root Cause
Missing indexes on frequently queried tables.

#### Solution
```sql
-- Added missing indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_products_category ON products(category_id);

-- Updated statistics
ANALYZE TABLE users;
ANALYZE TABLE orders;
ANALYZE TABLE products;
```

#### Result
- Query time reduced from 10+ seconds to < 100ms
- CPU load on DB server normalized
- No more timeouts

## Frequently Asked Questions (FAQ)

### General Questions

#### Q: How do I reach IT support?

**A:** IT support can be reached through the following channels:
- **Email:** {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **Phone:** {{ meta-organisation-roles.role_Service_Desk_Lead_phone }}
- **Ticketing System:** [TODO: URL]
- **Chat:** [TODO: Chat Channel]

**Support Hours:**
- Mon-Fri: 08:00-18:00
- 24/7 for critical incidents (P1)

#### Q: How do I create a support ticket?

**A:** Support tickets can be created through the following methods:

1. **Web Portal:**
   - Go to [TODO: Ticketing URL]
   - Log in with SSO
   - Click "New Ticket"
   - Fill out form and submit

2. **Email:**
   - Email to {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
   - Subject: Brief problem description
   - Content: Detailed description, screenshots

3. **Phone:**
   - Call {{ meta-organisation-roles.role_Service_Desk_Lead_phone }}
   - Describe problem
   - Note ticket number

#### Q: How does support prioritize tickets?

**A:** Tickets are processed according to the following priorities:

| Priority | Description | Response Time | Resolution Time |
|---|---|---|---|
| P1 - Critical | Complete system outage | 15 minutes | 4 hours |
| P2 - High | Partial outage, many users affected | 1 hour | 8 hours |
| P3 - Medium | Individual users affected | 4 hours | 24 hours |
| P4 - Low | Questions, feature requests | 8 hours | 72 hours |

### Access and Authentication

#### Q: I forgot my password. What should I do?

**A:** Password reset via self-service portal:

1. Go to [TODO: Self-Service URL]
2. Click "Forgot Password"
3. Enter username or email
4. Answer security questions or receive code via email/SMS
5. Set new password

**Alternative:** Contact IT support

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

#### Q: I cannot connect via VPN. What can I do?

**A:** VPN troubleshooting:

1. **Check credentials:**
   - Username correct?
   - Password correct?
   - MFA token current?

2. **Check VPN client:**
   - Latest version installed?
   - Profile correctly configured?

3. **Check network:**
   - Internet connection working?
   - Firewall not blocking VPN?

4. **Alternatives:**
   - Try different VPN gateway
   - Reinstall VPN client

**If nothing helps:** Contact IT support with:
- VPN client version
- Error message (screenshot)
- Time of problem

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

#### Q: I receive a "500 Internal Server Error". What does that mean?

**A:** A 500 error means a problem occurred on the server.

**Immediate actions:**
1. Reload page (F5)
2. Wait 5 minutes and try again
3. Clear browser cache
4. Try different browser

**If error persists:**
- Create ticket (P2 - High)
- Attach screenshot of error
- Provide exact URL
- Note time

**For IT team:**
- Check server logs
- Check application logs
- Check monitoring alerts

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

#### Q: I receive many spam emails. What can I do?

**A:** Spam reduction:

1. **Train spam filter:**
   - Mark spam emails as "Spam"
   - Mark non-spam emails as "Not Spam"

2. **Block sender:**
   - Add sender to blocklist

3. **Create email rules:**
   - Automatic filtering based on sender/subject

4. **Be careful sharing email:**
   - Don't post email address publicly
   - Use separate email for newsletters

**For suspicious emails:**
- **DO NOT** click on links
- **DO NOT** open attachments
- Forward to {{ meta-organisation-roles.role_CISO_email }}
- Delete email

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

#### Q: My network drive is full. What should I do?

**A:** Storage management:

1. **Analyze storage:**
   - Identify large files
   - Delete old/unnecessary files

2. **Archive files:**
   - Archive old projects
   - Move to archive storage

3. **Remove duplicates:**
   - Identify and delete duplicate files

4. **Compression:**
   - Compress large files (ZIP, 7z)

5. **Request quota increase:**
   - Create ticket with justification
   - Manager approval required

**Quota limits:**
- Standard users: [TODO: Size]
- Power users: [TODO: Size]
- Project shares: [TODO: Size]

### Hardware

#### Q: My computer is very slow. What can I do?

**A:** Performance optimization:

1. **Restart:**
   - Restart computer
   - Often solves the problem

2. **Close programs:**
   - Close unnecessary programs
   - Check Task Manager (Ctrl+Shift+Esc)

3. **Disk cleanup:**
   - Delete temporary files
   - Run Disk Cleanup tool

4. **Check updates:**
   - Install Windows updates
   - Install application updates

5. **Malware scan:**
   - Run antivirus scan

**If problem persists:**
- Create ticket
- Check hardware upgrade
- Consider reinstallation

#### Q: How do I request new hardware?

**A:** Hardware request:

1. **Create ticket:**
   - Category: "Hardware Request"
   - Specify desired hardware
   - Provide justification

2. **Approval:**
   - Manager approval required
   - Budget review by {{ meta-organisation-roles.role_CFO }}

3. **Procurement:**
   - IT team orders hardware
   - Delivery time: [TODO: Timeframe]

4. **Installation:**
   - Schedule appointment with IT team
   - Old hardware will be returned

**Standard hardware:**
- Laptop: [TODO: Model]
- Desktop: [TODO: Model]
- Monitor: [TODO: Model]
- Peripherals: Mouse, keyboard, headset

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

### Browser Issues

**Symptoms:**
- Page doesn't load
- Incorrect display
- Functions don't work

**Solutions:**
1. Clear cache (Ctrl+Shift+Del)
2. Delete cookies
3. Disable browser extensions
4. Test incognito mode
5. Test different browser
6. Reinstall browser

### Network Issues

**Symptoms:**
- No connection
- Slow connection
- Intermittent connection

**Solutions:**
1. Check network cable
2. Check WiFi connection
3. Restart router
4. Renew IP configuration (ipconfig /renew)
5. Flush DNS cache (ipconfig /flushdns)
6. Check VPN connection

### Application Issues

**Symptoms:**
- Application doesn't start
- Application crashes
- Functions missing

**Solutions:**
1. Restart application
2. Restart computer
3. Reinstall application
4. Install updates
5. Test compatibility mode (Windows)
6. Check logs

## Self-Service Resources

### Documentation
- **Wiki:** [TODO: Wiki URL]
- **Video Tutorials:** [TODO: Video URL]
- **Manuals:** [TODO: Manual URL]

### Tools
- **Self-Service Portal:** [TODO: Portal URL]
- **Password Reset:** [TODO: Reset URL]
- **Software Download:** [TODO: Download URL]

### Training
- **Online Courses:** [TODO: Course URL]
- **Webinars:** [TODO: Webinar Calendar]
- **In-Person Training:** Request via IT support

## Feedback and Improvements

### Give Feedback

Do you have suggestions for improving this document or IT services?

**Contact:**
- **Email:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Feedback Form:** [TODO: Form URL]

### Document Updates

This document is regularly updated based on:
- New known issues
- Frequently asked questions
- User feedback
- Process improvements

**Review Cycle:** Monthly  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

## Processes and Responsibilities

### RACI Matrix

| Activity | Ops Manager | Ops Team | Service Desk | Users |
|---|---|---|---|---|
| Document known issues | A | R | C | I |
| Update FAQ | A | R | C | I |
| Develop workarounds | A | R | C | - |
| User support | C | C | R | - |
| Collect feedback | A | C | R | R |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance and Standards

### Relevant Standards
- **ITIL v4:** Service Desk Practice, Knowledge Management
- **ISO 20000:** Clause 8.2 - Service Desk
- **COBIT 2019:** DSS02 - Managed Service Requests and Incidents

## Appendix

### Glossary

| Term | Definition |
|---|---|
| Known Issue | Known problem with documented workaround |
| FAQ | Frequently Asked Questions |
| Workaround | Temporary solution for a problem |
| Root Cause | Underlying cause of a problem |
| Self-Service | User solves problem without support |

### References
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}

