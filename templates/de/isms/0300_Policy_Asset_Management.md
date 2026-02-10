# Policy: Asset Management

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for asset management and inventory control.
It ensures that all organizational assets are identified, documented, and appropriately
protected throughout their lifecycle. Customize based on your organization's asset
types and management maturity.

ISO 27001:2022 Annex A Reference: A.5.9, A.5.10, A.5.11
-->

**Dokument-ID:** 0300  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.9-A.5.11 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Grundsätze für Asset Management und Inventarverwaltung der **{{ meta.organization.name }}**. Sie stellt sicher, dass alle Informationswerte (Assets) identifiziert, dokumentiert, klassifiziert und über ihren gesamten Lebenszyklus angemessen geschützt werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta.organization.name }}
- **Asset-Typen:** Hardware, Software, Daten, Informationen, Dienste, Personen, immaterielle Werte
- **Systeme:** Alle IT-Systeme, Netzwerkkomponenten, Endgeräte, Server, Cloud-Ressourcen
- **Lebenszyklus:** Beschaffung, Inbetriebnahme, Betrieb, Wartung, Außerbetriebnahme, Entsorgung
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Vollständiges Asset-Inventar
Alle Assets der Organisation werden in einem zentralen Asset-Inventar erfasst und dokumentiert. Das Inventar wird regelmäßig aktualisiert und auf Vollständigkeit überprüft.

### 3.2 Asset Owner Assignment
Jedes Asset hat einen definierten Asset Owner, der verantwortlich ist für:
- Klassifizierung des Assets
- Definition von Schutzanforderungen
- Genehmigung von Zugriffs- und Nutzungsrechten
- Lifecycle-Management

### 3.3 Asset-Klassifizierung und Tagging
Assets werden klassifiziert und mit Metadaten versehen (Tagging):
- Klassifizierung nach Schutzbedarf (Vertraulichkeit, Integrität, Verfügbarkeit)
- Technische Tags (Umgebung, Applikation, Kostenstelle)
- Compliance-Tags (DSGVO, PCI-DSS, etc.)

### 3.4 Lifecycle-Management
Assets werden über ihren gesamten Lebenszyklus verwaltet:
- **Beschaffung:** Sicherheitsanforderungen, Genehmigungsprozess
- **Inbetriebnahme:** Konfiguration, Härtung, Dokumentation
- **Betrieb:** Wartung, Patching, Monitoring
- **Außerbetriebnahme:** Datenlöschung, Dekommissionierung
- **Entsorgung:** Sichere Vernichtung, Recycling

### 3.5 Akzeptable Nutzung
Assets dürfen nur für genehmigte geschäftliche Zwecke genutzt werden. Private Nutzung ist nur im Rahmen der Acceptable Use Policy (`0200_Policy_Akzeptable_Nutzung_IT.md`) gestattet.

### 3.6 Rückgabe von Assets
Bei Rollenwechsel oder Austritt müssen alle Assets zurückgegeben werden. Der Rückgabeprozess ist Teil des Leaver-Prozesses.

### 3.7 Schutz vor Verlust und Diebstahl
Assets werden durch geeignete Maßnahmen vor Verlust, Diebstahl und unbefugtem Zugriff geschützt:
- Physische Sicherheit (Zutrittskontrolle, Alarmanlagen)
- Verschlüsselung mobiler Geräte
- Remote-Wipe-Funktionalität
- Versicherung kritischer Assets

### 3.8 Sichere Entsorgung
Assets werden am Ende ihres Lebenszyklus sicher entsorgt:
- Datenlöschung nach anerkannten Standards
- Physische Zerstörung bei hochsensiblen Daten
- Umweltgerechtes Recycling
- Dokumentation der Entsorgung

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Asset Management

| Aktivität | CISO | Asset Owner | IT-Betrieb | Procurement | Facility Management |
|-----------|------|-------------|------------|-------------|---------------------|
| Policy-Erstellung | R/A | C | C | C | I |
| Asset-Inventarisierung | A | R | R | C | C |
| Asset Owner Assignment | C | R/A | I | I | I |
| Klassifizierung | C | R/A | I | I | I |
| Lifecycle-Management | A | R | R | C | C |
| Sichere Entsorgung | C | A | R | I | R |
| Monitoring und Audits | R/A | C | C | I | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Asset Owner:** Fachbereichsleiter, Systemverantwortliche
- **Asset Manager:** {{ meta.it.asset_manager }}
- **Umsetzungsverantwortliche:** IT-Betrieb, Procurement, Facility Management
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md** - Detaillierte Implementierungsrichtlinie
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0200_Policy_Akzeptable_Nutzung_IT.md` - Acceptable Use Policy
- `0480_Policy_Physische_Sicherheit.md` - Physical Security Policy

### Zugehörige Standards/Baselines
- Asset-Inventar-Schema (CMDB)
- Tagging-Standards
- Entsorgungsstandards
- Lifecycle-Management-Prozesse

### Zugehörige Prozesse
- Asset-Beschaffungsprozess
- Asset-Onboarding und Konfiguration
- Asset-Rückgabeprozess (Leaver)
- Sichere Entsorgungsprozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Inventarisierungsrate (Ziel: 100% aller Assets erfasst)
- Anzahl Assets ohne Asset Owner
- Anzahl nicht klassifizierter Assets
- Durchschnittliche Zeit zur Asset-Registrierung
- Anzahl verlorener oder gestohlener Assets
- Compliance-Rate mit Entsorgungsstandards

### Nachweise und Evidence
- Asset-Inventar (CMDB)
- Asset Owner Assignments
- Klassifizierungs-Register
- Entsorgungsnachweise
- Audit-Berichte zu Asset Management
- Versicherungsnachweise

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nicht registrierte Assets:** Nachregistrierung, Nachschulung
- **Verlust von Assets:** Untersuchung, ggf. Kostenerstattung
- **Unsachgemäße Entsorgung:** Nachschulung, Disziplinarmaßnahmen
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Asset Owner genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md` - Detailed Guideline
- `0720_Anhang_Asset_und_Systeminventar_Template.md` - Asset Inventory Template
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.9** - Inventory of information and other associated assets
- **ISO/IEC 27001:2022 Annex A.5.10** - Acceptable use of information and other associated assets
- **ISO/IEC 27001:2022 Annex A.5.11** - Return of assets
- **ISO/IEC 27002:2022** - Information security controls
- **ITIL 4** - IT Asset Management
- **ISO/IEC 19770** - IT Asset Management

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
