# Policy: Physische Sicherheit

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for physical security of facilities,
equipment, and information. It ensures that physical access to sensitive areas
and assets is controlled and monitored. Customize based on your organization's
facility types and security requirements.

ISO 27001:2022 Annex A Reference: A.7.1, A.7.2, A.7.3, A.7.4
-->

**Dokument-ID:** 0480  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.7.1-A.7.4 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Grundsätze für physische Sicherheit der **{{ meta.organization.name }}**. Sie stellt sicher, dass physischer Zugang zu Einrichtungen, Geräten und Informationen kontrolliert und überwacht wird, um unbefugten Zugriff, Diebstahl und Beschädigung zu verhindern.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta.organization.name }}
- **Einrichtungen:** Büros, Rechenzentren, Serverräume, Lager, Produktionsstätten
- **Assets:** IT-Equipment, Server, Netzwerkkomponenten, mobile Geräte, Dokumente
- **Personen:** Mitarbeiter, Besucher, Auftragnehmer, Lieferanten
- **Standorte:** {{ netbox.site.name }} und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Perimeter-Sicherheit
Physische Sicherheitsbereiche werden durch Perimeter-Sicherheit geschützt (Zäune, Mauern, Sicherheitstüren). Zutrittspunkte werden kontrolliert und überwacht.

### 3.2 Zutrittskontrolle
Der Zutritt zu sensiblen Bereichen wird kontrolliert:
- Elektronische Zutrittskontrollsysteme (Badge, Biometrie)
- Besuchermanagement und Begleitpflicht
- Protokollierung aller Zutritte
- Regelmäßige Überprüfung von Zutrittsrechten

### 3.3 Sicherheitszonen
Einrichtungen werden in Sicherheitszonen eingeteilt:
- **Öffentlich:** Empfang, Besprechungsräume
- **Intern:** Büros, Arbeitsplätze
- **Eingeschränkt:** Serverräume, Rechenzentren
- **Hochsicher:** Kritische Infrastruktur, Tresorräume

### 3.4 Videoüberwachung
Kritische Bereiche werden videoüberwacht. Aufzeichnungen werden gemäß Datenschutzanforderungen gespeichert und geschützt.

### 3.5 Schutz vor Umweltgefahren
IT-Equipment wird vor Umweltgefahren geschützt:
- Brandschutz (Rauchmelder, Löschanlagen)
- Klimatisierung und Temperaturüberwachung
- Wasserschutz (Leckageerkennung)
- Stromversorgung (USV, Notstromgeneratoren)

### 3.6 Sichere Entsorgung
Physische Medien und Dokumente werden sicher entsorgt (Schreddern, Verbrennen, zertifizierte Entsorgung).

### 3.7 Clear Desk und Clear Screen
Arbeitsplätze werden bei Abwesenheit aufgeräumt (Clear Desk). Bildschirme werden gesperrt (Clear Screen).

### 3.8 Equipment Security
IT-Equipment wird vor Diebstahl geschützt (Kensington-Locks, Alarmanlagen, Inventarisierung).

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Physische Sicherheit

| Aktivität | CISO | Facility Management | Security | IT-Betrieb | HR |
|-----------|------|---------------------|----------|------------|-----|
| Policy-Erstellung | R/A | C | C | C | I |
| Zutrittskontrolle | C | R/A | R | I | C |
| Besuchermanagement | I | R/A | R | I | C |
| Videoüberwachung | C | R/A | R | I | C |
| Umweltschutz | C | R/A | I | C | I |
| Equipment Security | C | C | I | R/A | I |
| Compliance-Prüfung | R/A | C | C | I | I |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Facility Manager:** {{ meta.facility.manager }}
- **Security Manager:** {{ meta.security.physical_security_manager }}
- **Umsetzungsverantwortliche:** Facility Management, Security, IT-Betrieb
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md** - Detaillierte Implementierungsrichtlinie
- `0300_Policy_Asset_Management.md` - Asset Management Policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Data Protection Policy (Videoüberwachung)

### Zugehörige Standards/Baselines
- Sicherheitszonen-Konzept
- Zutrittskontroll-Matrix
- Besuchermanagement-Prozess
- Videoüberwachungs-Richtlinie

### Zugehörige Prozesse
- Zutrittskontroll-Prozess
- Besuchermanagement-Prozess
- Incident Response bei physischen Sicherheitsvorfällen
- Equipment-Entsorgungsprozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl unbefugter Zutrittsversuche
- Besucheranzahl und Compliance mit Begleitpflicht
- Anzahl physischer Sicherheitsvorfälle (Diebstahl, Einbruch)
- Zutrittskontroll-System-Verfügbarkeit (Ziel: 99.9%)
- Clear Desk/Clear Screen Compliance-Rate
- Anzahl verlorener oder gestohlener Assets

### Nachweise und Evidence
- Zutrittskontroll-Logs
- Besucherprotokolle
- Videoüberwachungs-Aufzeichnungen
- Sicherheitsvorfalls-Reports
- Facility-Audit-Berichte
- Equipment-Inventar

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Unbefugter Zutritt:** Sofortige Eskalation, Untersuchung
- **Tailgating (Mitschleusen):** Verwarnung, Nachschulung
- **Clear Desk/Screen-Verstöße:** Verwarnung, Nachschulung
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Facility Manager genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md` - Detailed Guideline
- `0300_Policy_Asset_Management.md` - Asset Management Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.7.1** - Physical security perimeters
- **ISO/IEC 27001:2022 Annex A.7.2** - Physical entry
- **ISO/IEC 27001:2022 Annex A.7.3** - Securing offices, rooms and facilities
- **ISO/IEC 27001:2022 Annex A.7.4** - Physical security monitoring
- **DSGVO (EU 2016/679)** - Datenschutz bei Videoüberwachung
- **BSI IT-Grundschutz** - Baustein INF.1 Allgemeines Gebäude

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)
