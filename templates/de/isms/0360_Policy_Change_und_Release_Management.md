# Policy: Change und Release Management

**Dokument-ID:** 0360
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for change and release management.
It ensures that changes to IT systems are controlled, tested, and documented
to minimize disruption and security risks. Customize based on your organization's
ITIL/DevOps maturity and change management processes.

ISO 27001:2022 Annex A Reference: A.8.32
-->

## 1. Zweck

Diese Policy definiert die Grundsätze für Change und Release Management der **{{ meta-organisation.name }}**. Sie stellt sicher, dass Änderungen an IT-Systemen kontrolliert, getestet und dokumentiert werden, um Betriebsunterbrechungen und Sicherheitsrisiken zu minimieren.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Systeme:** Alle IT-Systeme, Anwendungen, Infrastruktur, Netzwerke, Cloud-Services
- **Change-Typen:** Standard Changes, Normal Changes, Emergency Changes
- **Umgebungen:** Produktion, Test, Entwicklung
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Kontrollierte Änderungen
Alle Änderungen an produktiven IT-Systemen müssen über den Change Management Prozess genehmigt, dokumentiert und nachverfolgt werden.

### 3.2 Change-Kategorisierung
Changes werden nach Risiko und Auswirkung kategorisiert:
- **Standard Changes:** Vorab genehmigte, risikoarme, wiederkehrende Changes
- **Normal Changes:** Reguläre Changes mit CAB-Genehmigung
- **Emergency Changes:** Dringende Changes zur Behebung kritischer Probleme

### 3.3 Change Advisory Board (CAB)
Ein Change Advisory Board bewertet und genehmigt Normal und Emergency Changes. Das CAB besteht aus Vertretern von IT, Security, Business und Change Management.

### 3.4 Risiko- und Impact-Analyse
Vor jeder Änderung wird eine Risiko- und Impact-Analyse durchgeführt. Sicherheitsrisiken werden bewertet und Mitigationsmaßnahmen definiert.

### 3.5 Test und Validierung
Changes werden in Test-Umgebungen validiert, bevor sie in Produktion ausgerollt werden. Kritische Changes erfordern umfassende Tests.

### 3.6 Rollback-Planung
Für jeden Change existiert ein Rollback-Plan, um bei Problemen schnell zum vorherigen Zustand zurückkehren zu können.

### 3.7 Dokumentation und Nachvollziehbarkeit
Alle Changes werden dokumentiert (Beschreibung, Begründung, Genehmigung, Durchführung, Ergebnis). Changes sind nachvollziehbar und auditierbar.

### 3.8 Security Review
Changes mit Sicherheitsrelevanz erfordern ein Security Review durch das Security Team vor der Genehmigung.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Change und Release Management

| Aktivität | Change Manager | CAB | CISO | Change Requester | IT-Betrieb |
|-----------|----------------|-----|------|------------------|------------|
| Policy-Erstellung | C | C | R/A | I | C |
| Change-Antrag | I | I | I | R | I |
| Risiko-Analyse | R | C | C | C | C |
| CAB-Genehmigung | R | A | C | I | I |
| Security Review | C | C | R/A | I | I |
| Change-Durchführung | C | I | I | I | R/A |
| Rollback | R | I | C | I | R/A |
| Post-Implementation Review | R/A | C | C | C | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Change Manager:** {{ meta.it.change_manager }}
- **CAB Chair:** {{ meta.it.cab_chair }}
- **Umsetzungsverantwortliche:** IT-Betrieb, Entwicklung
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0370_Richtlinie_Change_Management_mit_Sicherheitsfreigaben.md** - Detaillierte Implementierungsrichtlinie
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Patch Management Policy
- `0380_Policy_Secure_Development.md` - Secure Development Policy
- `0400_Policy_Incident_Management.md` - Incident Management Policy

### Zugehörige Standards/Baselines
- Change-Kategorisierung und Genehmigungsprozesse
- CAB-Zusammensetzung und Entscheidungskriterien
- Test- und Validierungsanforderungen
- Rollback-Prozeduren

### Zugehörige Prozesse
- Change Management Prozess
- Emergency Change Prozess
- Release Management Prozess
- Post-Implementation Review

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl Changes pro Kategorie (Standard, Normal, Emergency)
- Change Success Rate (Ziel: >95%)
- Anzahl Failed Changes und Rollbacks
- Durchschnittliche Change-Durchlaufzeit
- Anzahl ungenehmigter Changes (Ziel: 0)
- Security Review Coverage für sicherheitsrelevante Changes (Ziel: 100%)

### Nachweise und Evidence
- Change-Tickets und Genehmigungen
- CAB-Meeting-Protokolle
- Security Review Dokumentation
- Test-Ergebnisse
- Rollback-Dokumentation
- Post-Implementation Review Reports

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Ungenehmigter Change:** Rollback, Untersuchung, Nachschulung
- **Fehlende Dokumentation:** Nachholung, Verwarnung
- **Übersprungener Security Review:** Untersuchung, Disziplinarmaßnahmen
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom Change Manager und CISO genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden dokumentiert und im Post-Implementation Review besprochen
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0370_Richtlinie_Change_Management_mit_Sicherheitsfreigaben.md` - Detailed Guideline
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Patch Management Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.32** - Change management
- **ISO/IEC 27002:2022** - Information security controls
- **ITIL 4** - Change Enablement
- **ISO/IEC 20000** - IT Service Management

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

