# Richtlinie: HR Security - Onboarding, Rollenwechsel, Offboarding

**Dokument-ID:** 0530
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0520_Policy_HR_Security.md` und definiert:
- Security-Aspekte im HR-Lifecycle
- Onboarding, Rollenwechsel und Offboarding-Prozesse
- Background-Checks und Vertraulichkeitsverpflichtungen

**Geltungsbereich:** Alle Mitarbeiter, Auftragnehmer und Dritte bei **{{ meta-organisation.name }}**

## 2. Pre-Employment

### 2.1 Background Checks

**Standard-Mitarbeiter:**
- Identitätsprüfung (Personalausweis)
- Referenzen prüfen (2 Referenzen)
- Bildungsabschlüsse verifizieren
- Arbeitserlaubnis prüfen

**Privilegierte Rollen:**
- Erweiterte Background-Checks
- Führungszeugnis
- Kreditwürdigkeit (bei Finanzzugriff)
- Social Media Screening (optional)

**Externe Auftragnehmer:**
- Firmen-Background-Check
- NDA vor Zugriff
- Sponsor-Verantwortung

### 2.2 Arbeitsvertrag

**Security-Klauseln:**
- Vertraulichkeitsverpflichtung
- Acceptable Use Policy
- Intellectual Property Rights
- Post-Employment-Verpflichtungen

## 3. Onboarding

### 3.1 Erster Arbeitstag

**HR-Aktivitäten:**
1. Willkommens-Paket übergeben
2. Arbeitsvertrag unterschreiben
3. Security-Policies bestätigen
4. Notfallkontakte erfassen

**IT-Aktivitäten:**
1. Account-Erstellung (siehe `0230_Richtlinie_IAM`)
2. Hardware-Ausgabe
3. IT-Einweisung
4. MFA-Registrierung

### 3.2 Security-Schulungen

**Pflicht-Schulungen (Erste Woche):**
- Information Security Awareness (2 Stunden)
- Data Protection / DSGVO (1 Stunde)
- Acceptable Use Policy (30 Minuten)
- Phishing-Awareness (30 Minuten)

**Bestätigung:**
- Quiz (Bestehensgrenze: 80%)
- Unterschrift auf Schulungsnachweis

### 3.3 Rollenspezifische Schulungen

**Entwickler:**
- Secure Coding Training
- OWASP Top 10

**Administratoren:**
- Privileged Access Management
- Incident Response

**HR/Finance:**
- Data Privacy
- Social Engineering Awareness

## 4. Rollenwechsel (Mover)

### 4.1 Interner Wechsel

**HR-Prozess:**
1. Neue Rolle in HR-System aktualisieren
2. Alter und neuer Vorgesetzter informieren
3. IT-Ticket für Zugriffsänderungen

**IT-Prozess:**
1. Alte Zugriffe entziehen
2. Neue Zugriffe bereitstellen
3. Hardware anpassen (falls erforderlich)
4. Dokumentation aktualisieren

**Details:** Siehe `0230_Richtlinie_IAM`

### 4.2 Beförderungen

**Zusätzliche Prüfungen:**
- Bei privilegierten Rollen: Erweiterter Background-Check
- Security-Schulungen für neue Verantwortung
- Vier-Augen-Prinzip bei kritischen Zugriff en

## 5. Offboarding

### 5.1 Geplantes Ausscheiden

**2 Wochen vor Austritt:**
- Wissenstransfer planen
- Übergabe-Checkliste erstellen
- Zugriffe reviewen

**Letzter Arbeitstag:**
- Hardware-Rückgabe
- Zutrittskarte abgeben
- Exit-Interview
- Account-Deaktivierung (End of Day)

**Nach Austritt:**
- Account-Löschung (nach 30 Tagen)
- E-Mail-Weiterleitung (30 Tage)
- Daten-Archivierung

**Details:** Siehe `0230_Richtlinie_IAM`

### 5.2 Ungeplantes Ausscheiden

**Sofortmaßnahmen (innerhalb 1 Stunde):**
1. Alle Accounts deaktivieren
2. VPN-Zugriff sperren
3. Zutrittskarte deaktivieren
4. Mobile Geräte remote löschen
5. Vorgesetzten und Security informieren

**Gründe:**
- Kündigung aus wichtigem Grund
- Sicherheitsvorfälle
- Verdacht auf Datenmissbrauch

### 5.3 Post-Employment

**Vertraulichkeitsverpflichtung:**
- Bleibt nach Austritt bestehen
- Keine Weitergabe von Geschäftsgeheimnissen
- Rückgabe aller Unterlagen

**Wiedereinstellung:**
- Neuer Background-Check
- Neue Security-Schulungen
- Neue Accounts (keine Reaktivierung alter Accounts)

## 6. Vertraulichkeitsverpflichtungen

### 6.1 Non-Disclosure Agreement (NDA)

**Unterzeichnung:**
- Bei Einstellung (im Arbeitsvertrag)
- Bei Zugriff auf vertrauliche Projekte
- Bei Auftragsverarbeitung (externe Dienstleister)

**Inhalte:**
- Definition vertraulicher Informationen
- Nutzungsbeschränkungen
- Dauer der Verpflichtung
- Konsequenzen bei Verstößen

### 6.2 Intellectual Property (IP)

**Regelung:**
- Alle Arbeitsergebnisse gehören dem Unternehmen
- Keine private Nutzung von Unternehmens-Code
- Offenlegung von Erfindungen

## 7. Disziplinarmaßnahmen

### 7.1 Security-Verstöße

**Kategorien:**
- **Leicht:** Unbeabsichtigte Verstöße (z.B. Passwort-Sharing)
- **Mittel:** Fahrlässige Verstöße (z.B. Datenverlust durch Unachtsamkeit)
- **Schwer:** Vorsätzliche Verstöße (z.B. Datendiebstahl)

**Maßnahmen:**
- Leicht: Verwarnung, Nachschulung
- Mittel: Schriftliche Abmahnung
- Schwer: Kündigung, Strafanzeige

### 7.2 Prozess

1. Incident-Meldung
2. Untersuchung durch HR und Security
3. Anhörung des Mitarbeiters
4. Entscheidung über Maßnahmen
5. Dokumentation
6. Umsetzung

## 8. Externe Auftragnehmer

### 8.1 Onboarding

**Voraussetzungen:**
- Vertrag mit Security-Klauseln
- NDA unterschrieben
- Background-Check (durch Auftragnehmer-Firma)
- Interner Sponsor

**Zugriffe:**
- Zeitlich befristet
- Nur projektbezogen
- Regelmäßige Rezertifizierung (quartalsweise)

### 8.2 Monitoring

**Erhöhte Überwachung:**
- Zugriffe auf vertrauliche Daten
- Privilegierte Aktivitäten
- Datenexporte

### 8.3 Offboarding

**Bei Projektende:**
- Sofortige Zugriffsentziehung
- Datenrückgabe oder -löschung
- Bestätigung der Vertraulichkeitsverpflichtung

## 9. Compliance und Audit

### 9.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Background-Check-Completion | 100% |
| Security-Schulung (Onboarding) | 100% |
| Offboarding-Completion (am letzten Tag) | 100% |
| NDA-Unterzeichnung | 100% |

### 9.2 Audit-Nachweise

- Background-Check-Dokumentation
- Schulungsnachweise
- NDA-Unterschriften
- Offboarding-Checklisten

## 10. Referenzen

### Interne Dokumente
- `0520_Policy_HR_Security.md`
- `0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.6.1** - Screening
- **ISO/IEC 27001:2022 Annex A.6.2** - Terms and conditions of employment
- **ISO/IEC 27001:2022 Annex A.6.3** - Information security awareness, education and training
- **ISO/IEC 27001:2022 Annex A.6.4** - Disciplinary process

**Genehmigt durch:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

