# Policy: Aufbewahrung und Löschung

**Dokument-ID:** 0580
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes requirements for records retention and secure deletion.
It ensures compliance with legal retention requirements and data minimization principles.
Customize based on your organization's legal requirements and industry-specific regulations.

ISO 27001:2022 Annex A Reference: A.5.33, A.5.34, A.8.10
-->

## 1. Zweck

Diese Policy definiert die Anforderungen an Aufbewahrung und Löschung von Informationen und Daten der **{{ meta-organisation.name }}**. Sie stellt sicher, dass gesetzliche Aufbewahrungspflichten erfüllt und Datenschutzgrundsätze (Datensparsamkeit, Speicherbegrenzung) eingehalten werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Daten:** Alle Informationen und Daten (strukturiert und unstrukturiert)
- **Systeme:** Alle IT-Systeme, Datenbanken, Backup-Systeme, Archive
- **Medien:** Digitale und physische Datenträger
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Aufbewahrungsfristen
Für alle Informationen werden Aufbewahrungsfristen definiert. Aufbewahrungsfristen basieren auf gesetzlichen, regulatorischen und geschäftlichen Anforderungen.

### 3.2 Retention Schedule
Ein Retention Schedule (Aufbewahrungsplan) wird erstellt und gepflegt. Der Retention Schedule definiert für jede Informationskategorie:
- Aufbewahrungsfrist
- Rechtsgrundlage
- Löschverfahren
- Verantwortliche Rolle

### 3.3 Datensparsamkeit und Speicherbegrenzung
Daten werden nur so lange aufbewahrt, wie erforderlich (DSGVO Art. 5 Abs. 1 lit. e). Nach Ablauf der Aufbewahrungsfrist werden Daten gelöscht oder anonymisiert.

### 3.4 Sichere Löschung
Daten werden sicher und unwiederbringlich gelöscht. Löschverfahren stellen sicher, dass Daten nicht wiederhergestellt werden können.

### 3.5 Löschkonzept
Ein Löschkonzept definiert:
- Löschverfahren für verschiedene Datenträger
- Löschfristen und Trigger
- Verantwortlichkeiten
- Nachweisführung

### 3.6 Backup-Aufbewahrung
Backups unterliegen denselben Aufbewahrungsfristen wie Produktivdaten. Backups werden nach Ablauf der Aufbewahrungsfrist gelöscht.

### 3.7 Legal Hold
Bei rechtlichen Verfahren oder Untersuchungen können Daten von der Löschung ausgenommen werden (Legal Hold). Legal Hold wird dokumentiert und überwacht.

### 3.8 Physische Datenträger
Physische Datenträger (Festplatten, USB-Sticks, Papier) werden sicher entsorgt:
- Digitale Datenträger: Sichere Löschung oder physische Zerstörung
- Papier: Schreddern oder zertifizierte Entsorgung

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Aufbewahrung und Löschung

| Aktivität | CISO | DPO | IT-Betrieb | Business Owner | Records Manager |
|-----------|------|-----|------------|----------------|-----------------|
| Policy-Erstellung | R/A | C | C | C | C |
| Retention Schedule | C | C | C | R | R/A |
| Löschkonzept | R/A | C | R | C | C |
| Löschung Durchführung | I | I | R/A | C | C |
| Legal Hold | C | C | I | C | R/A |
| Backup-Löschung | C | I | R/A | I | C |
| Physische Entsorgung | C | I | R/A | I | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO)
- **Records Manager:** {{ meta-handbook.records_manager }}
- **Data Protection Officer:** {{ meta-handbook.dpo_name }}
- **Umsetzungsverantwortliche:** IT-Betrieb, Business Owner
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, Legal

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0590_Richtlinie_Records_Retention_und_Sichere_Loeschung.md** - Detaillierte Implementierungsrichtlinie
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Privacy Policy
- `0420_Policy_Backup_und_Wiederherstellung.md` - Backup Policy

### Zugehörige Standards/Baselines
- Retention Schedule (Aufbewahrungsplan)
- Löschkonzept
- Sichere Löschverfahren (NIST SP 800-88, BSI TL-03423)
- Legal Hold Prozess

### Zugehörige Prozesse
- Retention Management Prozess
- Löschprozess (automatisiert und manuell)
- Legal Hold Prozess
- Physische Entsorgung Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Retention Schedule Coverage (Ziel: 100% aller Informationskategorien)
- Anzahl durchgeführter Löschungen (geplant vs. durchgeführt)
- Durchschnittliche Zeit bis zur Löschung nach Fristablauf (Ziel: < 30 Tage)
- Anzahl Legal Holds und Dauer
- Backup-Löschung Compliance (Ziel: 100%)
- Anzahl sicher entsorgter physischer Datenträger

### Nachweise und Evidence
- Retention Schedule
- Löschprotokolle und Nachweise
- Legal Hold Dokumentation
- Backup-Löschprotokolle
- Entsorgungsnachweise (Zertifikate)
- Audit Logs für Löschungen

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nicht gelöschte Daten:** Nachholung, Compliance-Untersuchung
- **Fehlende Retention Schedule:** Erstellung, Risikobewertung
- **Unsichere Löschung:** Incident Response, Risikobewertung
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen, Bußgelder

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und DPO genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0590_Richtlinie_Records_Retention_und_Sichere_Loeschung.md` - Detailed Guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.33** - Protection of records
- **ISO/IEC 27001:2022 Annex A.5.34** - Privacy and protection of PII
- **ISO/IEC 27001:2022 Annex A.8.10** - Information deletion
- **DSGVO Art. 5 Abs. 1 lit. e** - Speicherbegrenzung
- **DSGVO Art. 17** - Recht auf Löschung
- **NIST SP 800-88** - Guidelines for Media Sanitization
- **BSI TL-03423** - Leitfaden zur Löschung und Vernichtung

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

