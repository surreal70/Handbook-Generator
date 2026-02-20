# TOE Logical Scope

**Dokument-ID:** COMMON-CRITERIA-0110
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



## 1. Logical Components Overview

### 1.1 TOE Logical Composition
Der TOE besteht aus folgenden logischen Komponenten:

| Component ID | Component Name | Type | Purpose | Security Relevance |
|--------------|----------------|------|---------|-------------------|
| [TODO: LC-001] | [TODO: Komponentenname] | Module/Service/Function | [TODO: Zweck] | High/Medium/Low |
| [TODO: LC-002] | [TODO: Komponentenname] | Module/Service/Function | [TODO: Zweck] | High/Medium/Low |
| [TODO: LC-003] | [TODO: Komponentenname] | Module/Service/Function | [TODO: Zweck] | High/Medium/Low |

### 1.2 Logical Architecture
[TODO: Beschreibe die logische Architektur des TOE]

```
[TODO: Logisches Architekturdiagramm einfügen]
```

## 2. Security Functions

### 2.1 Security Function Overview
**Der TOE bietet folgende Sicherheitsfunktionen:**

| Function ID | Function Name | Category | Description |
|-------------|---------------|----------|-------------|
| [TODO: SF-001] | [TODO: Funktionsname] | Identification/Authentication/Access Control/Audit/etc. | [TODO: Beschreibung] |
| [TODO: SF-002] | [TODO: Funktionsname] | Identification/Authentication/Access Control/Audit/etc. | [TODO: Beschreibung] |
| [TODO: SF-003] | [TODO: Funktionsname] | Identification/Authentication/Access Control/Audit/etc. | [TODO: Beschreibung] |

### 2.2 Identification and Authentication
**Identifikations- und Authentifizierungsfunktionen:**

**[TODO: Funktion 1]**
- Zweck: [TODO: z.B. Benutzeridentifikation]
- Mechanismus: [TODO: z.B. Username/Password, Biometrie, Token]
- Stärke: [TODO: z.B. Multi-Faktor, Single-Faktor]
- Unterstützte Methoden: [TODO: Liste der Methoden]

**[TODO: Funktion 2]**
- [TODO: Details]

### 2.3 Access Control
**Zugriffskontrollfunktionen:**

**[TODO: Funktion 1]**
- Modell: [TODO: z.B. DAC, MAC, RBAC, ABAC]
- Granularität: [TODO: z.B. Datei, Objekt, Feld]
- Durchsetzung: [TODO: Beschreibung]
- Verwaltung: [TODO: Beschreibung]

**[TODO: Funktion 2]**
- [TODO: Details]

### 2.4 Audit and Logging
**Audit- und Logging-Funktionen:**

**[TODO: Funktion 1]**
- Ereignistypen: [TODO: Liste der auditierten Ereignisse]
- Audit-Daten: [TODO: Gespeicherte Informationen]
- Speicherung: [TODO: Speichermechanismus]
- Schutz: [TODO: Integritätsschutz]
- Überprüfung: [TODO: Überprüfungsmechanismen]

**[TODO: Funktion 2]**
- [TODO: Details]

### 2.5 Cryptographic Functions
**Kryptografische Funktionen:**

**[TODO: Funktion 1]**
- Zweck: [TODO: z.B. Verschlüsselung, Signatur, Hashing]
- Algorithmen: [TODO: z.B. AES-256, RSA-2048, SHA-256]
- Schlüssellängen: [TODO: Schlüssellängen]
- Modi: [TODO: z.B. CBC, GCM, CTR]
- Schlüsselverwaltung: [TODO: Beschreibung]

**[TODO: Funktion 2]**
- [TODO: Details]

### 2.6 Data Protection
**Datenschutzfunktionen:**

**[TODO: Funktion 1]**
- Datentyp: [TODO: z.B. Benutzerdaten, Konfiguration, Credentials]
- Schutzmechanismus: [TODO: z.B. Verschlüsselung, Hashing, Obfuscation]
- Speicherort: [TODO: z.B. Datenbank, Dateisystem, Memory]
- Lebenszyklus: [TODO: Erstellung, Nutzung, Löschung]

**[TODO: Funktion 2]**
- [TODO: Details]

### 2.7 Communication Security
**Kommunikationssicherheitsfunktionen:**

**[TODO: Funktion 1]**
- Protokoll: [TODO: z.B. TLS 1.3, IPsec, SSH]
- Verschlüsselung: [TODO: Algorithmen und Modi]
- Authentifizierung: [TODO: Mechanismus]
- Integritätsschutz: [TODO: Mechanismus]

**[TODO: Funktion 2]**
- [TODO: Details]

### 2.8 Security Management
**Sicherheitsmanagementfunktionen:**

**[TODO: Funktion 1]**
- Verwaltungsbereich: [TODO: z.B. Benutzer, Richtlinien, Konfiguration]
- Verwaltungsschnittstelle: [TODO: GUI/CLI/API]
- Berechtigungen: [TODO: Erforderliche Rechte]
- Audit: [TODO: Auditierung von Verwaltungsaktionen]

**[TODO: Funktion 2]**
- [TODO: Details]

## 3. Functional Modules

### 3.1 Core Modules
**Kernmodule des TOE:**

**[TODO: Modul 1]**
- Zweck: [TODO: Beschreibung]
- Funktionen: [TODO: Bereitgestellte Funktionen]
- Schnittstellen: [TODO: Interne und externe Schnittstellen]
- Abhängigkeiten: [TODO: Abhängigkeiten zu anderen Modulen]
- Sicherheitsrelevanz: [TODO: Sicherheitsfunktionen]

**[TODO: Modul 2]**
- [TODO: Details]

### 3.2 Security Modules
**Sicherheitsmodule:**

**[TODO: Sicherheitsmodul 1]**
- Zweck: [TODO: Beschreibung]
- Sicherheitsfunktionen: [TODO: Implementierte Sicherheitsfunktionen]
- Kryptografie: [TODO: Verwendete kryptografische Mechanismen]
- Schnittstellen: [TODO: Schnittstellen]

**[TODO: Sicherheitsmodul 2]**
- [TODO: Details]

### 3.3 Support Modules
**Unterstützungsmodule:**

**[TODO: Modul 1]**
- Zweck: [TODO: Beschreibung]
- Funktionen: [TODO: Bereitgestellte Funktionen]
- Sicherheitsrelevanz: [TODO: Indirekte Sicherheitsrelevanz]

**[TODO: Modul 2]**
- [TODO: Details]

## 4. Functional Capabilities

### 4.1 User Functions
**Benutzerfunktionen:**

| Function | Description | Security Impact |
|----------|-------------|-----------------|
| [TODO: Funktion 1] | [TODO: Beschreibung] | [TODO: Sicherheitsauswirkung] |
| [TODO: Funktion 2] | [TODO: Beschreibung] | [TODO: Sicherheitsauswirkung] |
| [TODO: Funktion 3] | [TODO: Beschreibung] | [TODO: Sicherheitsauswirkung] |

### 4.2 Administrative Functions
**Administratorfunktionen:**

| Function | Description | Required Privilege |
|----------|-------------|-------------------|
| [TODO: Funktion 1] | [TODO: Beschreibung] | [TODO: Erforderliche Berechtigung] |
| [TODO: Funktion 2] | [TODO: Beschreibung] | [TODO: Erforderliche Berechtigung] |
| [TODO: Funktion 3] | [TODO: Beschreibung] | [TODO: Erforderliche Berechtigung] |

### 4.3 System Functions
**Systemfunktionen:**

| Function | Description | Trigger |
|----------|-------------|---------|
| [TODO: Funktion 1] | [TODO: Beschreibung] | [TODO: Auslöser] |
| [TODO: Funktion 2] | [TODO: Beschreibung] | [TODO: Auslöser] |
| [TODO: Funktion 3] | [TODO: Beschreibung] | [TODO: Auslöser] |

## 5. Logical Boundaries

### 5.1 Included Functions
**Folgende Funktionen sind im TOE enthalten:**

**Sicherheitsfunktionen:**
- [TODO: Funktion 1]: [TODO: Begründung für Einschluss]
- [TODO: Funktion 2]: [TODO: Begründung für Einschluss]

**Nicht-Sicherheitsfunktionen:**
- [TODO: Funktion 1]: [TODO: Begründung für Einschluss]
- [TODO: Funktion 2]: [TODO: Begründung für Einschluss]

### 5.2 Excluded Functions
**Folgende Funktionen sind NICHT im TOE enthalten:**
- [TODO: Funktion 1]: [TODO: Begründung für Ausschluss]
- [TODO: Funktion 2]: [TODO: Begründung für Ausschluss]
- [TODO: Funktion 3]: [TODO: Begründung für Ausschluss]

### 5.3 Boundary Rationale
[TODO: Erkläre die Begründung für die logischen Grenzen des TOE]

Die logischen Grenzen wurden wie folgt definiert:
- [TODO: Begründung 1]
- [TODO: Begründung 2]
- [TODO: Begründung 3]

## 6. Security Mechanisms

### 6.1 Authentication Mechanisms
**Authentifizierungsmechanismen:**

| Mechanism | Type | Strength | Use Case |
|-----------|------|----------|----------|
| [TODO: Mechanismus 1] | Password/Biometric/Token/Certificate | [TODO: Stärke] | [TODO: Anwendungsfall] |
| [TODO: Mechanismus 2] | Password/Biometric/Token/Certificate | [TODO: Stärke] | [TODO: Anwendungsfall] |

### 6.2 Authorization Mechanisms
**Autorisierungsmechanismen:**

| Mechanism | Model | Enforcement Point | Policy |
|-----------|-------|-------------------|--------|
| [TODO: Mechanismus 1] | DAC/MAC/RBAC/ABAC | [TODO: Durchsetzungspunkt] | [TODO: Richtlinie] |
| [TODO: Mechanismus 2] | DAC/MAC/RBAC/ABAC | [TODO: Durchsetzungspunkt] | [TODO: Richtlinie] |

### 6.3 Cryptographic Mechanisms
**Kryptografische Mechanismen:**

| Mechanism | Algorithm | Key Length | Purpose |
|-----------|-----------|------------|---------|
| [TODO: Mechanismus 1] | [TODO: Algorithmus] | [TODO: Schlüssellänge] | [TODO: Zweck] |
| [TODO: Mechanismus 2] | [TODO: Algorithmus] | [TODO: Schlüssellänge] | [TODO: Zweck] |

### 6.4 Integrity Mechanisms
**Integritätsmechanismen:**

| Mechanism | Type | Protected Asset | Verification |
|-----------|------|-----------------|--------------|
| [TODO: Mechanismus 1] | Hash/MAC/Signature | [TODO: Geschütztes Asset] | [TODO: Verifikation] |
| [TODO: Mechanismus 2] | Hash/MAC/Signature | [TODO: Geschütztes Asset] | [TODO: Verifikation] |

## 7. Data Flow

### 7.1 Internal Data Flow
[TODO: Beschreibe den internen Datenfluss zwischen logischen Komponenten]

```
[TODO: Internes Datenflussdiagramm einfügen]
```

### 7.2 Security-Critical Data Flow
[TODO: Beschreibe sicherheitskritische Datenflüsse]

**[TODO: Datenfluss 1]**
- Quelle: [TODO: Quellkomponente]
- Ziel: [TODO: Zielkomponente]
- Datentyp: [TODO: z.B. Credentials, Keys, Audit Data]
- Schutz: [TODO: Schutzmechanismen]

**[TODO: Datenfluss 2]**
- [TODO: Details]

### 7.3 Trust Boundaries
[TODO: Definiere Vertrauensgrenzen innerhalb des TOE]

```
[TODO: Vertrauensgrenzendiagramm einfügen]
```

## 8. Functional Architecture

### 8.1 Layered Architecture
[TODO: Beschreibe die geschichtete Architektur des TOE]

**Schicht 1: [TODO: Schichtname]**
- Zweck: [TODO: Beschreibung]
- Komponenten: [TODO: Komponenten in dieser Schicht]
- Schnittstellen: [TODO: Schnittstellen]

**Schicht 2: [TODO: Schichtname]**
- [TODO: Details]

### 8.2 Component Interactions
[TODO: Beschreibe Interaktionen zwischen Komponenten]

```
[TODO: Komponenteninteraktionsdiagramm einfügen]
```

### 8.3 Security Enforcement Points
**Sicherheitsdurchsetzungspunkte:**

| Enforcement Point | Location | Enforced Policy | Mechanism |
|-------------------|----------|-----------------|-----------|
| [TODO: Punkt 1] | [TODO: Ort] | [TODO: Richtlinie] | [TODO: Mechanismus] |
| [TODO: Punkt 2] | [TODO: Ort] | [TODO: Richtlinie] | [TODO: Mechanismus] |

## 9. Operational Modes

### 9.1 Normal Operation Mode
**Normalbetriebsmodus:**
- Beschreibung: [TODO: Beschreibung]
- Verfügbare Funktionen: [TODO: Funktionen]
- Sicherheitsverhalten: [TODO: Sicherheitsverhalten]

### 9.2 Maintenance Mode
**Wartungsmodus:**
- Beschreibung: [TODO: Beschreibung]
- Verfügbare Funktionen: [TODO: Funktionen]
- Sicherheitsverhalten: [TODO: Sicherheitsverhalten]
- Zugriffskontrolle: [TODO: Zugriffskontrolle]

### 9.3 Secure State
**Sicherer Zustand:**
- Definition: [TODO: Definition des sicheren Zustands]
- Aufrechterhaltung: [TODO: Wie wird der sichere Zustand aufrechterhalten]
- Wiederherstellung: [TODO: Wiederherstellung nach Fehler]

**Nächste Schritte:**
1. Vervollständige alle [TODO]-Platzhalter mit TOE-spezifischen Informationen
2. Erstelle detaillierte funktionale Architekturdiagramme
3. Dokumentiere alle Sicherheitsmechanismen vollständig
4. Überprüfe die Konsistenz mit dem physischen Umfang (Template 0100)
5. Stelle sicher, dass alle Sicherheitsfunktionen dokumentiert sind

