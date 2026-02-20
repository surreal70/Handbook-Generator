
Document-ID: tisax-0140

Status: Draft
Classification: Internal

# Zugriffskontroll-Richtlinie

**Dokument-ID:** [FRAMEWORK]-0140
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

## Zweck

Dieses Dokument definiert die Richtlinien und Anforderungen für die Zugriffskontrolle auf Informationssysteme und -ressourcen gemäß TISAX-Anforderungen.

## Geltungsbereich

Diese Richtlinie gilt für alle Benutzer, Systeme und Ressourcen von [TODO].

## Grundprinzipien

### Need-to-Know-Prinzip

Zugriff wird nur gewährt, wenn:
- Geschäftliche Notwendigkeit besteht
- Aufgaben dies erfordern
- Genehmigung vorliegt

### Least-Privilege-Prinzip

Benutzer erhalten:
- Minimale erforderliche Berechtigungen
- Zeitlich begrenzte Zugriffe
- Rollenbasierte Rechte

### Segregation of Duties

Kritische Funktionen werden getrennt:
- Keine Einzelperson hat vollständige Kontrolle
- Vier-Augen-Prinzip bei kritischen Aktionen
- Trennung von Entwicklung und Produktion

## Zugriffskontroll-Prozess

### 1. Benutzer-Registrierung

**Neue Mitarbeiter:**
- Antrag durch Vorgesetzten
- Genehmigung durch IT und Informationssicherheit
- Erstellung von Benutzerkonten
- Zuweisung von Standardberechtigungen

**Externe Benutzer:**
- Vertragliche Vereinbarung erforderlich
- Zeitlich begrenzte Zugriffe
- Sponsorship durch internen Mitarbeiter
- Erweiterte Überwachung

### 2. Berechtigungsvergabe

**Antragsprozess:**
1. Benutzer oder Vorgesetzter stellt Antrag
2. Fachbereich genehmigt geschäftliche Notwendigkeit
3. Information Owner genehmigt Datenzugriff
4. IT implementiert Berechtigungen
5. Dokumentation im Access Management System

**Genehmigungsmatrix:**

| Zugriffstyp | Genehmiger | Dokumentation |
|-------------|-----------|---------------|
| Standard-Zugriff | Vorgesetzter | E-Mail |
| Erhöhte Rechte | Vorgesetzter + IT-Manager | Ticket-System |
| Admin-Rechte | IT-Manager + CISO | Formular + Genehmigung |
| Produktionszugriff | Fachbereich + IT-Manager | Change Request |

### 3. Zugriffsverwaltung

**Regelmäßige Überprüfung:**
- Quartalsweise Rezertifizierung durch Vorgesetzte
- Jährliche Vollprüfung aller Berechtigungen
- Automatische Erkennung ungenutzter Konten
- Entfernung nicht mehr benötigter Rechte

**Änderungen:**
- Bei Rollenwechsel: Anpassung der Berechtigungen
- Bei Austritt: Sofortige Sperrung aller Zugriffe
- Bei Sicherheitsvorfällen: Temporäre Sperrung möglich

### 4. Zugriffsentzug

**Geplanter Entzug:**
- Bei Austritt: Deaktivierung am letzten Arbeitstag
- Bei Projektende: Entzug nach Projektabschluss
- Bei Rollenwechsel: Anpassung der Berechtigungen

**Ungeplanter Entzug:**
- Bei Sicherheitsvorfällen: Sofortige Sperrung
- Bei Verdacht auf Missbrauch: Temporäre Sperrung
- Bei Compliance-Verstößen: Sofortige Sperrung

## Authentifizierung

### Passwort-Anforderungen

**Komplexität:**
- Mindestlänge: [TODO] Zeichen
- Großbuchstaben, Kleinbuchstaben, Zahlen, Sonderzeichen
- Keine Wörterbuchwörter
- Keine persönlichen Informationen

**Verwaltung:**
- Änderung alle [TODO] Tage
- Keine Wiederverwendung der letzten [TODO] Passwörter
- Automatische Sperrung nach [TODO] Fehlversuchen
- Passwort-Manager empfohlen

### Multi-Faktor-Authentifizierung (MFA)

MFA ist erforderlich für:
- Administrative Zugriffe
- Remote-Zugriffe (VPN, Remote Desktop)
- Zugriff auf vertrauliche Systeme
- Privilegierte Konten

**Unterstützte Faktoren:**
- Etwas, das man weiß (Passwort)
- Etwas, das man hat (Token, Smartphone)
- Etwas, das man ist (Biometrie)

### Single Sign-On (SSO)

[TODO] nutzt SSO für:
- Zentrale Authentifizierung
- Reduzierung von Passwörtern
- Vereinfachte Zugriffsverwaltung
- Verbesserte Sicherheit

## Autorisierung

### Rollenbasierte Zugriffskontrolle (RBAC)

**Standard-Rollen:**
- Benutzer: Basis-Zugriff auf Standardsysteme
- Power User: Erweiterte Funktionen
- Administrator: System-Administration
- Security Admin: Sicherheitsverwaltung

**Fachbereichs-Rollen:**
- Definiert durch Fachbereiche
- Basierend auf Geschäftsprozessen
- Regelmäßig überprüft und aktualisiert

### Attributbasierte Zugriffskontrolle (ABAC)

Zugriff basierend auf:
- Benutzerattributen (Abteilung, Standort)
- Ressourcenattributen (Klassifizierung, Typ)
- Umgebungsattributen (Zeit, Ort, Gerät)
- Aktionsattributen (Lesen, Schreiben, Löschen)

## Privilegierte Zugriffe

### Privileged Access Management (PAM)

**Anforderungen:**
- Separate privilegierte Konten
- Just-in-Time-Zugriff
- Session-Aufzeichnung
- Automatische Passwortrotation

**Überwachung:**
- Echtzeit-Monitoring privilegierter Sitzungen
- Alarmierung bei verdächtigen Aktivitäten
- Regelmäßige Auditierung
- Compliance-Reporting

### Administrative Konten

**Verwaltung:**
- Getrennt von Standard-Konten
- Erhöhte Authentifizierungsanforderungen
- Zeitlich begrenzte Aktivierung
- Umfassende Protokollierung

**Nutzung:**
- Nur für administrative Tätigkeiten
- Keine Nutzung für E-Mail oder Internet
- Keine Nutzung auf Standard-Workstations
- Dokumentation aller Nutzungen

## Remote-Zugriff

### VPN-Zugriff

**Anforderungen:**
- MFA obligatorisch
- Verschlüsselte Verbindung
- Endpoint-Compliance-Check
- Protokollierung aller Verbindungen

**Berechtigungen:**
- Antrag und Genehmigung erforderlich
- Zeitlich begrenzt
- Regelmäßige Rezertifizierung
- Automatische Trennung bei Inaktivität

### Remote Desktop

**Sicherheitsmaßnahmen:**
- Zugriff nur über VPN
- MFA erforderlich
- Session-Timeout
- Keine lokale Datenspeicherung

## Zugriffskontrolle für Systeme

### Server und Infrastruktur

- Zugriff nur für autorisiertes IT-Personal
- Protokollierung aller Zugriffe
- Regelmäßige Überprüfung der Berechtigungen
- Automatisierte Compliance-Checks

### Anwendungen

- Rollenbasierte Berechtigungen
- Integration mit zentraler Authentifizierung
- Regelmäßige Access Reviews
- Segregation of Duties

### Datenbanken

- Minimale Berechtigungen
- Verschlüsselte Verbindungen
- Audit-Logging aktiviert
- Regelmäßige Zugriffsprüfungen

### Cloud-Services

- Identity Federation
- Conditional Access Policies
- MFA obligatorisch
- Regelmäßige Überprüfung der Berechtigungen

## Überwachung und Protokollierung

### Protokollierung

Folgende Ereignisse werden protokolliert:
- Erfolgreiche und fehlgeschlagene Anmeldungen
- Berechtigungsänderungen
- Zugriffe auf sensible Daten
- Administrative Aktionen
- Privilegierte Zugriffe

### Monitoring

- Echtzeit-Überwachung kritischer Systeme
- Automatische Alarmierung bei Anomalien
- Regelmäßige Log-Analysen
- Security Information and Event Management (SIEM)

### Audit

- Quartalsweise Stichproben-Audits
- Jährliche Vollprüfung
- Überprüfung der Compliance
- Identifikation von Verbesserungspotentialen

## Ausnahmen

### Ausnahmegenehmigungen

Ausnahmen von dieser Richtlinie:
- Müssen schriftlich beantragt werden
- Erfordern Genehmigung durch CISO
- Sind zeitlich begrenzt
- Werden dokumentiert und überwacht
- Werden regelmäßig überprüft

### Notfallzugriffe

Bei Notfällen:
- Break-Glass-Konten verfügbar
- Nutzung wird sofort eskaliert
- Umfassende Protokollierung
- Nachträgliche Überprüfung obligatorisch

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **3.1**: Zugriffskontroll-Richtlinie
- **3.2**: Benutzerzugriffsverwaltung
- **3.3**: Benutzerverantwortlichkeiten
- **3.4**: System- und Anwendungszugriffskontrolle

### Assessment-Nachweise

Für TISAX-Assessments:
- Zugriffskontroll-Richtlinie
- Prozessdokumentation
- Genehmigungsnachweise
- Audit-Berichte
- Schulungsnachweise

## Verantwortlichkeiten

- **CISO**: Gesamtverantwortung für Zugriffskontrolle
- **IT-Manager**: Implementierung und Betrieb
- **Identity & Access Management Team**: Tägliche Verwaltung
- **Vorgesetzte**: Genehmigung und Rezertifizierung
- **Information Owner**: Genehmigung von Datenzugriffen
- **Benutzer**: Einhaltung der Richtlinie

## Schulung

Alle Benutzer werden geschult zu:
- Zugriffskontroll-Grundlagen
- Passwort-Sicherheit
- MFA-Nutzung
- Verantwortlichkeiten
- Meldung von Sicherheitsvorfällen

## Kennzahlen

[TODO] misst:
- Anzahl aktiver Benutzerkonten
- Anteil MFA-aktivierter Konten (Ziel: 100%)
- Durchschnittliche Zeit bis zur Berechtigungsvergabe
- Anzahl überfälliger Access Reviews
- Anzahl privilegierter Zugriffe
- Anzahl Zugriffsverletzungen



