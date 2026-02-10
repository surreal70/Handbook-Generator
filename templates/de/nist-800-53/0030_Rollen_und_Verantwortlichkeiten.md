# Rollen und Verantwortlichkeiten

**Dokument-ID:** NIST-0030  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Zweck

Dieses Dokument definiert die Rollen und Verantwortlichkeiten für das Risk Management Framework (RMF) und die Sicherheit des Systems {{ meta.nist.system_name }}.

## 2. RMF-Rollen

### 2.1 Authorizing Official (AO)

**Name:** {{ meta.roles.ao.name }}  
**E-Mail:** {{ meta.roles.ao.email }}  

**Verantwortlichkeiten:**
- Autorisierungsentscheidung für das System
- Akzeptanz des Sicherheitsrisikos
- Genehmigung des System Security Plan (SSP)
- Überwachung des Sicherheitsstatus

### 2.2 Information System Security Officer (ISSO)

**Name:** {{ meta.roles.isso.name }}  
**E-Mail:** {{ meta.roles.isso.email }}  

**Verantwortlichkeiten:**
- Tägliche Sicherheitsoperationen
- Implementierung von Sicherheitskontrollen
- Incident Response
- Sicherheitsüberwachung

### 2.3 Information System Security Manager (ISSM)

**Name:** {{ meta.roles.issm.name }}  
**E-Mail:** {{ meta.roles.issm.email }}  

**Verantwortlichkeiten:**
- Sicherheitsprogramm-Management
- Richtlinienentwicklung
- Compliance-Überwachung
- Risikomanagement

### 2.4 System Owner

**Name:** [TODO: Name]  
**E-Mail:** [TODO: E-Mail]  

**Verantwortlichkeiten:**
- Gesamtverantwortung für das System
- Geschäftsprozess-Verantwortung
- Budget und Ressourcen
- Systemänderungen genehmigen

### 2.5 Security Control Assessor (SCA)

**Name:** [TODO: Name/Firma]  
**E-Mail:** [TODO: E-Mail]  

**Verantwortlichkeiten:**
- Unabhängige Bewertung der Sicherheitskontrollen
- Erstellung des Security Assessment Report (SAR)
- Identifikation von Schwachstellen
- Empfehlungen für Verbesserungen

## 3. RACI-Matrix

| Aktivität | AO | ISSO | ISSM | System Owner | SCA |
|-----------|----|----|------|--------------|-----|
| System Categorization | A | C | R | C | I |
| Control Selection | A | R | C | C | I |
| Control Implementation | I | R | C | A | I |
| Control Assessment | I | C | C | I | R |
| Authorization Decision | R | C | C | C | I |
| Continuous Monitoring | A | R | C | C | I |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
