# Zweck und Geltungsbereich

**Dokument-ID:** BCM-0010  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the purpose and scope of the Business Continuity Management System (BCMS).
It aligns with ISO 22301:2019 Clause 4.3 (Determining the scope of the BCMS).

Customization required:
- Define organizational units in scope
- Specify locations covered
- List critical services and processes
- Document any exclusions with justification
-->

## 1. Zweck

Das Business Continuity Management System (BCMS) der {{ meta.organization.name }} dient folgenden Zwecken:

- **Schutz kritischer Geschäftsprozesse:** Sicherstellung der Fortführung geschäftskritischer Aktivitäten auch bei schwerwiegenden Störungen
- **Reduktion von Ausfallzeiten:** Minimierung der Auswirkungen von Unterbrechungen auf Geschäftsbetrieb, Kunden und Stakeholder
- **Erfüllung regulatorischer Anforderungen:** Nachweis der Compliance mit gesetzlichen und vertraglichen Verpflichtungen
- **Krisenreaktionsfähigkeit:** Etablierung strukturierter Prozesse zur Bewältigung von Notfällen und Krisen
- **Kontinuierliche Verbesserung:** Systematische Weiterentwicklung der Business Continuity-Fähigkeiten

### 1.1 Strategische Ziele

Das BCMS verfolgt folgende strategische Ziele:

- Definierte **Recovery Time Objectives (RTO)** und **Recovery Point Objectives (RPO)** für alle kritischen Prozesse
- Aufbau und Aufrechterhaltung der **Krisenreaktionsfähigkeit** auf allen Organisationsebenen
- **Nachweisbarkeit** der Business Continuity-Maßnahmen gegenüber Aufsichtsbehörden, Kunden und Partnern
- **Schutz der Reputation** und des Vertrauens der Stakeholder
- **Minimierung finanzieller Verluste** durch Geschäftsunterbrechungen

### 1.2 Referenzen zu Standards

Dieses BCMS orientiert sich an folgenden Standards und Best Practices:

- **ISO 22301:2019** - Security and resilience — Business continuity management systems — Requirements
- **ISO 22313:2020** - Security and resilience — Business continuity management systems — Guidance on the use of ISO 22301
- **BSI-Standard 100-4** - Notfallmanagement
- **BSI-Standard 200-4** - Business Continuity Management

## 2. Geltungsbereich

### 2.1 Organisationseinheiten

Das BCMS gilt für folgende Organisationseinheiten der {{ meta.organization.name }}:

[TODO: Definieren Sie die eingeschlossenen Organisationseinheiten]

**Beispiel:**
- Geschäftsführung
- IT-Abteilung
- Produktion
- Vertrieb und Marketing
- Finanzen und Controlling
- Personalwesen

### 2.2 Standorte

Das BCMS umfasst folgende Standorte:

[TODO: Listen Sie alle Standorte auf, die im Geltungsbereich liegen]

**Beispiel:**
- Hauptsitz: {{ meta.organization.address }}, {{ meta.organization.postal_code }} {{ meta.organization.city }}
- Produktionsstandort: [Adresse]
- Rechenzentrum: [Adresse]
- Ausweichstandort: [Adresse]

### 2.3 Services und Prozesse

Das BCMS deckt folgende kritischen Services und Geschäftsprozesse ab:

[TODO: Definieren Sie die kritischen Services und Prozesse]

**Beispiel:**
- Kundenservice und Support
- Produktionssteuerung
- Auftragsabwicklung
- Finanzprozesse (Zahlungsverkehr, Buchhaltung)
- IT-Services (E-Mail, ERP-System, Produktionssysteme)

### 2.4 IT- und OT-Systeme

Das BCMS umfasst folgende IT- und OT-Systeme:

[TODO: Listen Sie kritische IT- und OT-Systeme auf]

**Beispiel:**
- ERP-System
- CRM-System
- E-Mail und Collaboration-Plattform
- Produktionssteuerungssysteme (SCADA, MES)
- Netzwerkinfrastruktur
- Backup- und Recovery-Systeme

### 2.5 Ausnahmen und Ausschlüsse

Folgende Bereiche sind explizit vom Geltungsbereich ausgeschlossen:

[TODO: Dokumentieren Sie Ausnahmen mit Begründung und genehmigender Instanz]

**Beispiel:**
- **Tochtergesellschaft XY:** Betreibt eigenes BCMS (Genehmigt durch: {{ meta.roles.ceo.name }})
- **Entwicklungsumgebungen:** Nicht geschäftskritisch (Genehmigt durch: {{ meta.roles.cio.name }})

## 3. Annahmen und Einschränkungen

### 3.1 Grundannahmen

Das BCMS basiert auf folgenden Annahmen:

[TODO: Definieren Sie die Grundannahmen für Ihr BCMS]

**Beispiel:**
- Maximaler Personalausfall: Bis zu 30% der Belegschaft gleichzeitig nicht verfügbar
- Wiederherstellung kritischer IT-Systeme: Innerhalb von 24 Stunden möglich
- Verfügbarkeit von Ausweichstandorten: Innerhalb von 4 Stunden erreichbar
- Lieferketten: Kritische Lieferanten haben eigene BCM-Maßnahmen implementiert
- Externe Unterstützung: Notfalldienste (Feuerwehr, Polizei) sind verfügbar

### 3.2 Abhängigkeiten außerhalb der Kontrolle

Folgende Abhängigkeiten liegen außerhalb der direkten Kontrolle der Organisation:

[TODO: Identifizieren Sie externe Abhängigkeiten]

**Beispiel:**
- Verfügbarkeit öffentlicher Infrastruktur (Strom, Wasser, Telekommunikation)
- Verfügbarkeit von Cloud-Service-Providern
- Lieferfähigkeit kritischer Zulieferer
- Verfügbarkeit von Notfalldiensten
- Politische und regulatorische Rahmenbedingungen

## 4. Schnittstellen zu anderen Managementsystemen

### 4.1 Informationssicherheits-Managementsystem (ISMS)

**Verantwortlich:** {{ meta.roles.ciso.name }} ({{ meta.roles.ciso.email }})

Schnittstellen:
- Incident Management und Security Incident Response
- IT-Notfallpläne und Disaster Recovery
- Risikomanagement und Risikoanalyse
- Zugriffskontrolle und Notfallzugänge (Break-Glass)

[TODO: Beschreiben Sie die konkreten Schnittstellen zu Ihrem ISMS]

### 4.2 IT-Service-Management (ITSM)

**Verantwortlich:** {{ meta.roles.it_operations_manager.name }} ({{ meta.roles.it_operations_manager.email }})

Schnittstellen:
- Incident Management (Major Incidents → BCM-Aktivierung)
- Change Management (Emergency Changes)
- Problem Management (Post-Incident-Reviews)
- Service Level Management (SLA-Definitionen)

[TODO: Beschreiben Sie die konkreten Schnittstellen zu Ihrem ITSM]

### 4.3 Datenschutz und Compliance

**Verantwortlich:** [TODO: Datenschutzbeauftragter]

Schnittstellen:
- Datenschutz-Folgenabschätzungen (DPIA) für BCM-Maßnahmen
- Meldepflichten bei Datenschutzvorfällen
- Aufbewahrungsfristen für BCM-Dokumentation
- Compliance-Nachweise für Aufsichtsbehörden

[TODO: Beschreiben Sie die konkreten Schnittstellen zum Datenschutz]

### 4.4 Risikomanagement

**Verantwortlich:** [TODO: Risikomanager]

Schnittstellen:
- Unternehmensweites Risikomanagement
- Business Impact Analysis (BIA)
- Risikoanalyse und Risikobewertung
- Risikominderungsmaßnahmen

[TODO: Beschreiben Sie die konkreten Schnittstellen zum Risikomanagement]

### 4.5 Krisenkommunikation und Public Relations

**Verantwortlich:** [TODO: Kommunikationsverantwortlicher]

Schnittstellen:
- Interne Krisenkommunikation
- Externe Krisenkommunikation (Medien, Kunden, Partner)
- Stakeholder-Management
- Reputationsschutz

[TODO: Beschreiben Sie die konkreten Schnittstellen zur Krisenkommunikation]

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
