# Rollen und Verantwortlichkeiten

**Dokument-ID:** TSC-0040  
**Organisation:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Zweck

Dieses Dokument definiert die Rollen und Verantwortlichkeiten für TSC-Compliance und SOC 2-Audits.

## 2. Management-Rollen

### 2.1 Executive Management

**CEO:**
- **Name:** [TODO: Name]
- **Verantwortlichkeiten:**
  - Gesamtverantwortung für Compliance
  - Genehmigung von Richtlinien
  - Ressourcenzuweisung

**CTO:**
- **Name:** [TODO: Name]
- **Verantwortlichkeiten:**
  - Technische Strategie
  - System-Architektur
  - Change Approval

**CISO:**
- **Name:** {{ meta.roles.ciso.name }}
- **Email:** {{ meta.roles.ciso.email }}
- **Verantwortlichkeiten:**
  - Sicherheitsstrategie
  - Risikomanagement
  - Incident Response

## 3. Operational Rollen

### 3.1 System Administration

**System Administrators:**
- **Anzahl:** [TODO: #]
- **Verantwortlichkeiten:**
  - System-Wartung
  - Patch-Management
  - Backup-Verwaltung

### 3.2 Security Operations

**Security Engineers:**
- **Anzahl:** [TODO: #]
- **Verantwortlichkeiten:**
  - Security Monitoring
  - Incident Response
  - Vulnerability Management

### 3.3 Development

**Developers:**
- **Anzahl:** [TODO: #]
- **Verantwortlichkeiten:**
  - Application Development
  - Code Reviews
  - Security Testing

## 4. Compliance-Rollen

### 4.1 SOC 2 Program Manager

**Name:** [TODO: Name]  
**Email:** [TODO: Email]  
**Verantwortlichkeiten:**
- SOC 2-Programm-Management
- Audit-Koordination
- Dokumentation
- Compliance-Reporting

### 4.2 Service Auditor

**Firma:** {{ meta.roles.auditor.name }}  
**Kontakt:** {{ meta.roles.auditor.email }}  
**Verantwortlichkeiten:**
- SOC 2-Audit durchführen
- Kontrollwirksamkeit prüfen
- SOC 2-Bericht erstellen

## 5. RACI-Matrix

### 5.1 Control Environment

| Aktivität | CEO | CTO | CISO | Ops | Audit |
|-----------|-----|-----|------|-----|-------|
| Policy Approval | A | C | R | I | I |
| Risk Assessment | C | C | A/R | C | I |
| Control Design | I | C | A | R | C |
| Control Testing | I | I | C | R | A |

### 5.2 Operations

| Aktivität | CTO | CISO | Ops | Dev | Audit |
|-----------|-----|------|-----|-----|-------|
| Change Management | A | C | R | R | I |
| Incident Response | C | A | R | C | I |
| Monitoring | C | A | R | I | I |
| Backup/Recovery | A | C | R | I | I |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## 6. Training und Qualifikationen

### 6.1 Mandatory Training

- Security Awareness (jährlich)
- Role-specific Training
- Compliance Training

### 6.2 Certifications

**Security Team:**
- [TODO: CISSP, CISM, CEH]

**Operations Team:**
- [TODO: AWS Certified, Azure Certified]

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
