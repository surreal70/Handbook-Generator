# Notfallorganisation: Rollen und Gremien

**Dokument-ID:** BCM-0040  
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
This template defines the emergency organization structure, roles, and responsibilities.
It aligns with ISO 22301:2019 Clause 5.3 (Organizational roles, responsibilities and authorities).

Customization required:
- Define crisis management team structure
- Assign specific individuals to roles
- Establish clear RACI matrices
- Define escalation paths and decision authorities
-->

## 1. Organisationsmodell

### 1.1 Notfallorganisationsstruktur

Die Notfallorganisation der {{ meta.organization.name }} besteht aus folgenden Ebenen:

```
┌─────────────────────────────────────┐
│      Krisenstab (Strategic)         │
│   Leitung: {{ meta.roles.ceo.name }}│
└──────────────┬──────────────────────┘
               │
    ┌──────────┴──────────┬────────────────┐
    │                     │                │
┌───▼────────┐  ┌────────▼─────┐  ┌──────▼──────┐
│ BCM-Manager│  │ IT-DR-Team   │  │ Fachbereichs│
│            │  │              │  │ BCP-Teams   │
└────────────┘  └──────────────┘  └─────────────┘
```

**Ebene 1: Krisenstab (Strategic Level)**
- Strategische Entscheidungen und Gesamtkoordination
- Aktivierung bei schwerwiegenden Vorfällen
- Kommunikation mit externen Stakeholdern

**Ebene 2: BCM-Manager / Koordination (Tactical Level)**
- Operative Koordination der BCM-Maßnahmen
- Schnittstelle zwischen Krisenstab und operativen Teams
- Dokumentation und Reporting

**Ebene 3: Operative Teams (Operational Level)**
- IT-DR-Team: Wiederherstellung IT-Systeme
- Fachbereichs-BCP-Teams: Wiederherstellung Geschäftsprozesse
- Support-Teams: Logistik, Kommunikation, HR

### 1.2 Organigramm

[TODO: Fügen Sie ein detailliertes Organigramm ein]

**Verweis:** Siehe `diagrams/bcm_organization.png`

## 2. Rollenbeschreibungen

### 2.1 Krisenstabsleitung

**Rolle:** Krisenstabsleitung / Crisis Management Team Lead

**Verantwortlich:** {{ meta.roles.ceo.name }}  
**Stellvertretung:** {{ meta.roles.coo.name }}  
**Kontakt:** {{ meta.roles.ceo.email }} / {{ meta.roles.ceo.phone }}

**Aufgaben:**
- Gesamtverantwortung für Krisenmanagement und BCM-Aktivierung
- Strategische Entscheidungen über Ressourceneinsatz und Priorisierung
- Freigabe von Kommunikation an externe Stakeholder
- Entscheidung über Aktivierung von Ausweichstandorten
- Genehmigung außerordentlicher Maßnahmen und Budgets

**Entscheidungskompetenzen:**
- Aktivierung und Deaktivierung des Krisenstabs
- Freigabe von Notfallbudgets bis [TODO: Betrag]
- Entscheidung über Geschäftsfortführung oder -einstellung
- Genehmigung von Notfallzugängen (Break-Glass)

**Berichtspflichten:**
- An Aufsichtsrat / Gesellschafter bei schwerwiegenden Krisen
- An Aufsichtsbehörden gemäß regulatorischen Anforderungen

### 2.2 BCM-Manager / BCM-Koordinator

**Rolle:** BCM-Manager / Business Continuity Coordinator

**Verantwortlich:** [TODO: BCM-Manager Name]  
**Stellvertretung:** [TODO: Stellvertreter]  
**Kontakt:** [TODO: E-Mail / Telefon]

**Aufgaben:**
- Operative Leitung des BCMS im Normalbetrieb
- Koordination von BIA, Risikoanalyse und BCM-Planung
- Organisation und Durchführung von BCM-Übungen und Tests
- Pflege der BCM-Dokumentation und Kontaktlisten
- Schulung und Sensibilisierung der Mitarbeiter
- Reporting an Geschäftsführung und Krisenstab

**Reporting:**
- Quartalsweise BCM-Status-Reports an {{ meta.roles.ceo.name }}
- Ad-hoc-Reporting bei kritischen Ereignissen
- Jährlicher BCM-Jahresbericht

**Schnittstellen:**
- ISMS / CISO: {{ meta.roles.ciso.name }}
- IT-Operations: {{ meta.roles.it_operations_manager.name }}
- Fachbereiche: Jeweilige Bereichsleiter

### 2.3 Incident Commander / Einsatzleitung (operativ)

**Rolle:** Incident Commander / Operational Lead

**Verantwortlich:** [TODO: Incident Commander Name]  
**Stellvertretung:** [TODO: Stellvertreter]  
**Kontakt:** [TODO: E-Mail / Telefon]

**Aufgaben:**
- Operative Leitung der Notfallmaßnahmen vor Ort
- Koordination der operativen Teams (IT-DR, BCP-Teams)
- Lagebeurteilung und Statusreporting an Krisenstab
- Umsetzung der vom Krisenstab beschlossenen Maßnahmen
- Dokumentation aller Maßnahmen und Entscheidungen

**Schnittstelle zu ITSM/Incident:**
- Übernahme von Major Incidents aus ITSM-Prozess
- Eskalation an Krisenstab bei Überschreitung definierter Schwellwerte
- Rückführung in ITSM-Prozess nach Stabilisierung

**Entscheidungskompetenzen:**
- Operative Maßnahmen ohne Budgetüberschreitung
- Priorisierung von Wiederherstellungsmaßnahmen
- Anforderung zusätzlicher Ressourcen

### 2.4 Kommunikation / Sprecherrolle

**Rolle:** Krisenkommunikation / Spokesperson

**Verantwortlich:** [TODO: Kommunikationsverantwortlicher]  
**Stellvertretung:** [TODO: Stellvertreter]  
**Kontakt:** [TODO: E-Mail / Telefon]

**Aufgaben:**
- Interne Krisenkommunikation (Mitarbeiter, Management)
- Externe Krisenkommunikation (Medien, Kunden, Partner, Behörden)
- Erstellung und Freigabe von Pressemitteilungen
- Social Media Monitoring und Response
- Stakeholder-Management

**Freigabeprozesse:**
- Interne Kommunikation: Freigabe durch Krisenstabsleitung
- Externe Kommunikation: Freigabe durch {{ meta.roles.ceo.name }}
- Pressemitteilungen: Freigabe durch Geschäftsführung und ggf. Rechtsabteilung

**Kommunikationskanäle:**
- Intern: E-Mail, Intranet, Mitarbeiter-App, Telefon
- Extern: Website, Social Media, Pressemitteilungen, Kundenhotline

### 2.5 IT-DR-Lead

**Rolle:** IT Disaster Recovery Lead

**Verantwortlich:** {{ meta.roles.it_operations_manager.name }}  
**Stellvertretung:** [TODO: Stellvertreter]  
**Kontakt:** {{ meta.roles.it_operations_manager.email }} / {{ meta.roles.it_operations_manager.phone }}

**Aufgaben:**
- Leitung des IT-DR-Teams
- Koordination der IT-Wiederherstellungsmaßnahmen
- Umsetzung der IT-Disaster-Recovery-Pläne
- Priorisierung der Systemwiederherstellung gemäß BIA
- Statusreporting an Incident Commander und Krisenstab

**Runbooks und Wiederanlaufkoordination:**
- Verwaltung und Pflege der IT-DR-Runbooks
- Koordination der Systemwiederherstellung in definierter Reihenfolge
- Durchführung von Restore-Tests
- Dokumentation der Wiederherstellungsmaßnahmen

**Schnittstellen:**
- IT-Operations-Team
- Externe IT-Dienstleister und Cloud-Provider
- Fachbereiche (für Systemfreigaben)

## 3. RACI-Matrix Krisenmanagement

| Aktivität | Krisenstabs-leitung | BCM-Manager | Incident Commander | IT-DR-Lead | Fachbereich | Kommunikation |
|-----------|---------------------|-------------|-------------------|------------|-------------|---------------|
| Krise aktivieren | **A** | R | C | I | I | I |
| Lagebeurteilung | C | C | **A/R** | C | C | I |
| Strategische Entscheidungen | **A** | C | C | I | C | C |
| Operative Maßnahmen | I | C | **A** | R | R | I |
| IT-Wiederherstellung | I | C | C | **A/R** | C | I |
| BCP-Umsetzung | I | C | C | C | **A/R** | I |
| Interne Kommunikation | A | C | C | I | I | **R** |
| Externe Kommunikation | **A** | C | I | I | I | **R** |
| Dokumentation | I | **A** | R | R | R | R |
| Krise beenden | **A** | R | C | C | C | I |

**Legende:**
- **R** = Responsible (Durchführungsverantwortung)
- **A** = Accountable (Gesamtverantwortung, Entscheidungsbefugnis)
- **C** = Consulted (Konsultiert, Fachexpertise)
- **I** = Informed (Informiert)

## 4. Erreichbarkeit und Rufbereitschaft

### 4.1 Bereitschaftsmodelle

[TODO: Definieren Sie Bereitschaftsmodelle für kritische Rollen]

**Beispiel:**

**Krisenstab:**
- **Erreichbarkeit:** 24/7 über Mobiltelefon
- **Reaktionszeit:** Innerhalb von 2 Stunden einsatzbereit
- **Bereitschaftsplan:** Rotierendes Modell, quartalsweise Aktualisierung

**IT-DR-Team:**
- **Erreichbarkeit:** 24/7 Rufbereitschaft
- **Reaktionszeit:** Innerhalb von 1 Stunde einsatzbereit
- **Bereitschaftsplan:** Wöchentliche Rotation

**BCM-Manager:**
- **Erreichbarkeit:** Werktags 08:00-18:00 Uhr, außerhalb über Mobiltelefon
- **Reaktionszeit:** Innerhalb von 4 Stunden einsatzbereit

### 4.2 Eskalationszeiten

| Schweregrad | Reaktionszeit | Eskalation an | Eskalationszeit |
|-------------|---------------|---------------|-----------------|
| **Niedrig** | 4 Stunden | IT-Operations | - |
| **Mittel** | 2 Stunden | Incident Commander | Nach 4 Stunden |
| **Hoch** | 1 Stunde | Krisenstab | Nach 2 Stunden |
| **Kritisch** | Sofort | Krisenstabsleitung | Sofort |

### 4.3 Alarmierungsprozess

[TODO: Beschreiben Sie den Alarmierungsprozess]

**Beispiel:**
1. **Ersterkennung:** Incident wird erkannt (Monitoring, Meldung, etc.)
2. **Erstbewertung:** IT-Operations bewertet Schweregrad
3. **Alarmierung:** Bei Major Incident → Alarmierung Incident Commander
4. **Eskalation:** Bei BCM-Aktivierung → Alarmierung Krisenstab
5. **Bestätigung:** Alle alarmierten Personen bestätigen Empfang

**Alarmierungskanäle:**
- Primär: Telefon (Mobiltelefon)
- Sekundär: SMS / Messenger
- Tertiär: E-Mail

## 5. Vertretungsregelungen

### 5.1 Stellvertreterlisten

Für alle kritischen Rollen sind Stellvertreter definiert:

| Rolle | Primär | Stellvertreter 1 | Stellvertreter 2 |
|-------|--------|------------------|------------------|
| Krisenstabsleitung | {{ meta.roles.ceo.name }} | {{ meta.roles.coo.name }} | [TODO] |
| BCM-Manager | [TODO] | [TODO] | [TODO] |
| Incident Commander | [TODO] | [TODO] | [TODO] |
| IT-DR-Lead | {{ meta.roles.it_operations_manager.name }} | [TODO] | [TODO] |
| Kommunikation | [TODO] | [TODO] | [TODO] |

### 5.2 Übergabeprozess

Bei Vertretung oder Schichtwechsel erfolgt eine strukturierte Übergabe:

**Übergabeinhalte:**
- Aktueller Lagestatus
- Laufende Maßnahmen und deren Status
- Offene Entscheidungen und Eskalationen
- Kritische Informationen und Kontakte

**Übergabedokumentation:**
- Übergabeprotokoll (Template: [TODO: Link])
- Logbuch-Eintrag
- Briefing des Nachfolgers

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
