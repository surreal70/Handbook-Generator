# Policy: Business Continuity ICT Readiness

**Dokument-ID:** ISMS-0440
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---



## 1. Zweck

Diese Policy definiert die Grundsätze für ICT Continuity und Disaster Recovery der **AdminSend GmbH**. Sie stellt sicher, dass IT-Systeme und -Services während Störungen weiterbetrieben oder schnell wiederhergestellt werden können, um die Geschäftskontinuität zu gewährleisten.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Systeme:** Alle geschäftskritischen IT-Systeme, Anwendungen, Infrastruktur, Cloud-Services
- **Szenarien:** Naturkatastrophen, Cyberangriffe, Systemausfälle, Pandemien, Lieferantenausfälle
- **Schnittstellen:** Integration mit BCM (Business Continuity Management)
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 ICT Continuity Planning
Für alle geschäftskritischen IT-Services existieren ICT Continuity Pläne, die Wiederherstellungsstrategien, Ressourcen und Verantwortlichkeiten definieren.

### 3.2 Business Impact Analysis (BIA)
Regelmäßige Business Impact Analysen identifizieren kritische IT-Services und deren RPO/RTO-Anforderungen. Die BIA wird mit dem BCM-Team koordiniert.

### 3.3 Redundanz und Hochverfügbarkeit
Kritische IT-Systeme werden mit Redundanz und Hochverfügbarkeit ausgelegt:
- Redundante Komponenten (Server, Storage, Netzwerk)
- Geografisch verteilte Rechenzentren
- Load Balancing und Failover-Mechanismen
- Cloud-basierte Disaster Recovery

### 3.4 Disaster Recovery Pläne (DRP)
Detaillierte Disaster Recovery Pläne beschreiben Schritt-für-Schritt-Prozeduren zur Wiederherstellung von IT-Systemen nach einem Ausfall.

### 3.5 Regelmäßige Tests und Übungen
ICT Continuity und DR-Pläne werden regelmäßig getestet:
- **Kritische Systeme:** Jährliche DR-Tests
- **Wichtige Systeme:** Alle 2 Jahre
- **Tabletop-Übungen:** Quartalsweise

### 3.6 Alternative Arbeitsplätze und Remote Work
Mitarbeiter können bei Standortausfällen von alternativen Standorten oder remote arbeiten. Remote-Access-Infrastruktur ist hochverfügbar ausgelegt.

### 3.7 Lieferanten- und Cloud-Provider-Continuity
Kritische Lieferanten und Cloud-Provider werden auf ihre Business Continuity Fähigkeiten geprüft. SLAs enthalten Continuity-Anforderungen.

### 3.8 Incident-to-Crisis-Eskalation
Klare Eskalationspfade definieren, wann ein IT-Incident zu einer Business Continuity Crisis eskaliert wird und das BCM-Team aktiviert wird.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Business Continuity ICT Readiness

| Aktivität | CISO | BCM Manager | IT-Betrieb | CIO | Crisis Management Team |
|-----------|------|-------------|------------|-----|------------------------|
| Policy-Erstellung | R/A | C | C | C | I |
| BIA-Durchführung | C | R/A | C | C | I |
| DRP-Erstellung | A | C | R | C | I |
| DR-Tests | A | C | R | C | I |
| Crisis Activation | C | R/A | C | C | R |
| Recovery Execution | A | C | R | R | C |
| Post-Incident Review | R/A | R | C | C | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** [TODO] (CISO)
- **BCM Manager:** {{ meta-handbook.bcm_manager }}
- **DR Coordinator:** {{ meta-handbook.it_dr_coordinator }}
- **CIO:** [TODO]
- **Umsetzungsverantwortliche:** IT-Betrieb, System Owner
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0450_Richtlinie_ICT_DR_Schnittstellen_zu_BCM.md** - Detaillierte Implementierungsrichtlinie
- `0420_Policy_Backup_und_Wiederherstellung.md` - Backup Policy
- `0400_Policy_Incident_Management.md` - Incident Management Policy
- BCM-Handbuch (siehe `templates/de/bcm/`)

### Zugehörige Standards/Baselines
- RPO/RTO-Matrix
- DR-Plan-Templates
- Test-Szenarien
- Eskalationspfade

### Zugehörige Prozesse
- Business Impact Analysis Prozess
- Disaster Recovery Prozess
- DR-Test-Prozess
- Crisis Management Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl kritischer Systeme mit DR-Plänen (Ziel: 100%)
- DR-Test-Completion-Rate (Ziel: 100%)
- Durchschnittliche Recovery Time (RTO-Compliance)
- Anzahl erfolgreicher DR-Tests
- BIA-Aktualität (Ziel: jährliche Aktualisierung)
- Verfügbarkeit kritischer Systeme (Ziel: 99.9%)

### Nachweise und Evidence
- Business Impact Analysis Reports
- Disaster Recovery Pläne
- DR-Test-Protokolle
- Verfügbarkeits-Metriken
- Crisis Management Übungsprotokolle
- Audit-Berichte zu BCM/DR

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Fehlende DR-Pläne:** Sofortige Erstellung, Eskalation
- **Nicht getestete DR-Pläne:** Nachholung, Nachschulung
- **RTO/RPO-Verletzungen:** Root Cause Analysis, Remediation
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und BCM Manager genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Continuity-Maßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0450_Richtlinie_ICT_DR_Schnittstellen_zu_BCM.md` - Detailed Guideline
- `0420_Policy_Backup_und_Wiederherstellung.md` - Backup Policy
- BCM-Handbuch (`templates/de/bcm/`)

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.29** - Information security during disruption
- **ISO/IEC 27001:2022 Annex A.5.30** - ICT readiness for business continuity
- **ISO 22301** - Business Continuity Management Systems
- **ISO/IEC 27031** - ICT readiness for business continuity
- **BSI Standard 100-4** - Business Continuity Management

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO] (jährlich oder anlassbezogen)

