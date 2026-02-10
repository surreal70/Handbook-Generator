# Richtlinie: Ausnahmenprozess

**Dokument-ID:** 0650  
**Dokumenttyp:** Richtlinie (detailliert)  
**Zugehörige Policy:** 0640_Policy_Ausnahmen_und_Risk_Waivers.md  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.5.1  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}

---

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0640_Policy_Ausnahmen_und_Risk_Waivers.md` und definiert:
- Ausnahmenprozess für Security-Policies
- Risk-Waiver-Verfahren
- Kompensationskontrollen

**Geltungsbereich:** Alle Security-Policies bei **{{ meta.organization.name }}**

## 2. Ausnahmen-Kategorien

### 2.1 Temporäre Ausnahmen

**Definition:** Zeitlich befristete Abweichung von Policy

**Beispiele:**
- Verzögertes Patching (wegen Kompatibilitätsproblemen)
- Temporäre Firewall-Regel für Projekt
- Verzögerte Compliance (während Migration)

**Maximale Dauer:** 12 Monate

### 2.2 Permanente Ausnahmen

**Definition:** Dauerhafte Abweichung von Policy

**Beispiele:**
- Legacy-Systeme, die Baseline nicht erfüllen können
- Spezielle Geschäftsanforderungen
- Technische Unmöglichkeit

**Review-Frequenz:** Jährlich

### 2.3 Notfall-Ausnahmen

**Definition:** Sofortige Ausnahme bei Notfällen

**Beispiele:**
- Kritische Business-Anforderung
- Systemausfall-Behebung
- Security-Incident-Response

**Nachträgliche Genehmigung:** Innerhalb 48 Stunden

## 3. Ausnahmenprozess

### 3.1 Antragstellung

**Antrag über:** {{ meta.itsm.portal }} (Ticketsystem)

**Pflichtangaben:**
- Betroffene Policy/Richtlinie
- Beschreibung der Abweichung
- Begründung (Business Justification)
- Betroffene Systeme/Prozesse
- Risikobewertung
- Vorgeschlagene Kompensationskontrollen
- Gewünschte Dauer

**Antragsteller:** System-Owner oder Fachbereichsleiter

### 3.2 Risikobewertung

**Durchführung durch:** IT-Security-Team

**Bewertungskriterien:**
- Wahrscheinlichkeit eines Sicherheitsvorfalls
- Potenzielle Auswirkungen
- Betroffene Assets und Daten
- Bestehende Kontrollen
- Vorgeschlagene Kompensationskontrollen

**Risiko-Matrix:**
| Wahrscheinlichkeit | Auswirkung Niedrig | Auswirkung Mittel | Auswirkung Hoch |
|--------------------|-------------------|-------------------|-----------------|
| Niedrig | Niedrig | Niedrig | Mittel |
| Mittel | Niedrig | Mittel | Hoch |
| Hoch | Mittel | Hoch | Kritisch |

### 3.3 Kompensationskontrollen

**Definition:** Alternative Sicherheitsmaßnahmen zur Risikominimierung

**Beispiele:**
- Netzwerk-Isolation (bei fehlenden Patches)
- Erhöhtes Monitoring (bei schwächerer Authentifizierung)
- Manuelle Prozesse (bei fehlender Automatisierung)
- Zusätzliche Zugriffsbeschränkungen

**Anforderung:**
- Kompensationskontrollen müssen Risiko auf akzeptables Niveau senken
- Dokumentation der Wirksamkeit

### 3.4 Genehmigung

**Genehmigungsstufen:**

| Risiko | Genehmiger | SLA |
|--------|------------|-----|
| Niedrig | IT-Security-Manager | 3 Arbeitstage |
| Mittel | CISO | 5 Arbeitstage |
| Hoch | CISO + CIO | 7 Arbeitstage |
| Kritisch | CISO + CIO + Geschäftsführung | 10 Arbeitstage |

**Genehmigungskriterien:**
- Business Justification nachvollziehbar
- Risiko akzeptabel (mit Kompensationskontrollen)
- Keine Alternative verfügbar
- Zeitlich befristet (bei temporären Ausnahmen)

**Ablehnung:**
- Begründung erforderlich
- Alternative Lösungen vorschlagen

### 3.5 Dokumentation

**Ausnahmen-Register:**
- Alle genehmigten Ausnahmen
- Antragsteller, Genehmiger, Datum
- Risikobewertung
- Kompensationskontrollen
- Ablaufdatum
- Review-Datum

**Speicherort:** {{ meta.compliance.exception_register }}

## 4. Monitoring und Review

### 4.1 Laufende Überwachung

**Verantwortlichkeit:** IT-Security-Team

**Aktivitäten:**
- Wirksamkeit der Kompensationskontrollen prüfen
- Compliance mit Ausnahmen-Bedingungen
- Incidents im Zusammenhang mit Ausnahmen

**Frequenz:** Monatlich (bei kritischen Ausnahmen), quartalsweise (bei anderen)

### 4.2 Regelmäßiger Review

**Temporäre Ausnahmen:**
- Review 30 Tage vor Ablauf
- Entscheidung: Verlängern, Beenden, Permanent machen

**Permanente Ausnahmen:**
- Jährlicher Review
- Prüfung auf Notwendigkeit
- Aktualisierung der Risikobewertung

**Notfall-Ausnahmen:**
- Review innerhalb 7 Tage nach Genehmigung
- Regularisierung oder Beendigung

### 4.3 Eskalation

**Bei Problemen:**
- Kompensationskontrollen unwirksam
- Risiko gestiegen
- Incidents im Zusammenhang mit Ausnahme

**Eskalation an:**
- CISO (sofort)
- Risk Committee (bei kritischen Ausnahmen)

## 5. Beendigung von Ausnahmen

### 5.1 Geplante Beendigung

**Bei Ablauf:**
1. Benachrichtigung an Antragsteller (30 Tage vorher)
2. Remediation-Plan erstellen
3. Umsetzung der Remediation
4. Verifizierung
5. Ausnahme schließen

### 5.2 Vorzeitige Beendigung

**Gründe:**
- Risiko nicht mehr akzeptabel
- Kompensationskontrollen unwirksam
- Alternative Lösung verfügbar
- Geschäftsanforderung entfallen

**Prozess:**
1. Entscheidung durch CISO
2. Benachrichtigung an Antragsteller
3. Sofortige Remediation (oder Systemabschaltung)
4. Dokumentation

## 6. Reporting

### 6.1 Monatlicher Ausnahmen-Report

**Inhalte:**
- Anzahl aktiver Ausnahmen (nach Risiko)
- Neue Ausnahmen im Monat
- Abgelaufene Ausnahmen
- Überfällige Reviews
- Top-Ausnahmen nach Risiko

**Empfänger:** CISO, CIO, Risk Committee

### 6.2 Quartalsweiser Management-Report

**Inhalte:**
- Trend-Analyse
- Ausnahmen nach Kategorie/Abteilung
- Risiko-Posture
- Verbesserungsmaßnahmen

**Empfänger:** Geschäftsführung, Audit Committee

## 7. Compliance und Audit

### 7.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Ausnahmen mit aktuellem Review | 100% |
| Überfällige Ausnahmen | 0 |
| Ausnahmen mit Kompensationskontrollen | 100% |
| Durchschnittliche Ausnahmen-Dauer | < 6 Monate |

### 7.2 Audit-Nachweise

- Ausnahmen-Register
- Anträge und Genehmigungen
- Risikobewertungen
- Review-Protokolle
- Monitoring-Berichte

## 8. Beispiele

### 8.1 Beispiel: Verzögertes Patching

**Szenario:** Kritischer Patch verursacht Kompatibilitätsprobleme mit Business-Anwendung

**Antrag:**
- Policy: Patch Management (Critical Patches innerhalb 7 Tage)
- Abweichung: Verzögerung um 30 Tage
- Begründung: Kompatibilitätsproblem, Vendor arbeitet an Fix
- Risiko: Hoch (bekannter Exploit)

**Kompensationskontrollen:**
- Netzwerk-Isolation des betroffenen Systems
- IPS-Signatur aktiviert
- Erhöhtes Monitoring
- Zugriffsbeschränkungen

**Genehmigung:** CISO + CIO  
**Dauer:** 30 Tage  
**Review:** Wöchentlich

### 8.2 Beispiel: Legacy-System

**Szenario:** Legacy-System kann Security-Baseline nicht erfüllen

**Antrag:**
- Policy: Security-Baseline (CIS Benchmark Level 1)
- Abweichung: Veraltetes OS, keine Patches mehr verfügbar
- Begründung: Kritische Business-Anwendung, keine Migration möglich (kurzfristig)
- Risiko: Hoch

**Kompensationskontrollen:**
- Dediziertes VLAN (isoliert)
- Firewall-Regeln (nur erforderliche Verbindungen)
- Kein Internet-Zugriff
- Read-Only-Zugriff für Standard-Nutzer
- Erhöhtes Monitoring und Logging
- Jährliche Penetration-Tests

**Genehmigung:** CISO + CIO + Geschäftsführung  
**Dauer:** Permanent (bis Migration)  
**Review:** Jährlich

## 9. Referenzen

### Interne Dokumente
- `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- Alle Security-Policies und -Richtlinien

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.5.1** - Policies for information security
- **NIST SP 800-53** - Security and Privacy Controls (Tailoring)

---

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta.document.next_review }}

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
