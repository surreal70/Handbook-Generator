# Security Objectives Coverage Matrix

**Dokument-ID:** COMMON-CRITERIA-0320
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

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches TOE (Target of Evaluation) an.



## 1. Einleitung

Dieses Dokument präsentiert die Coverage Matrix (Abdeckungsmatrix) für die Sicherheitsziele des TOE **{{ meta-handbook.toe_name }}**. Die Matrix visualisiert die Beziehungen zwischen:

- Sicherheitszielen und Bedrohungen
- Sicherheitszielen und organisatorischen Sicherheitsrichtlinien (OSPs)
- Umgebungszielen und Annahmen

### 1.1 Zweck

Die Coverage Matrix dient als:
- **Vollständigkeitsnachweis**: Alle Elemente der Sicherheitsproblem-Definition sind abgedeckt
- **Rückverfolgbarkeitswerkzeug**: Schnelle Identifikation von Beziehungen
- **Audit-Dokumentation**: Nachweis für Evaluatoren und Auditoren
- **Änderungsmanagement**: Identifikation von Auswirkungen bei Änderungen

### 1.2 Legende

| Symbol | Bedeutung |
|--------|-----------|
| X | Primäre Zuordnung - Das Ziel adressiert direkt die Bedrohung/OSP/Annahme |
| • | Unterstützende Zuordnung - Das Ziel unterstützt indirekt |
| - | Keine Zuordnung |

## 2. Bedrohungen vs. Sicherheitsziele

Die folgende Matrix zeigt, welche Sicherheitsziele welche Bedrohungen adressieren:

| Bedrohung | O.ACCESS_CONTROL | O.IDENTIFICATION_AUTHENTICATION | O.AUDIT_GENERATION | O.AUDIT_PROTECTION | O.DATA_CONFIDENTIALITY | O.CRYPTOGRAPHIC_OPERATIONS | O.DATA_INTEGRITY | O.SECURITY_MANAGEMENT | O.SECURE_STATE | O.TSF_PROTECTION | OE.PHYSICAL_PROTECTION | **[TODO]** |
|-----------|------------------|--------------------------------|-------------------|-------------------|------------------------|---------------------------|------------------|----------------------|---------------|-----------------|----------------------|------------|
| **T.UNAUTHORIZED_ACCESS** | X | • | - | - | - | - | - | - | - | - | - | |
| **T.PRIVILEGE_ESCALATION** | X | • | - | - | - | - | - | - | - | - | - | |
| **T.MASQUERADE** | • | X | - | - | - | - | - | - | - | - | - | |
| **T.AUDIT_COMPROMISE** | - | - | X | X | - | - | - | - | - | - | - | |
| **T.DATA_DISCLOSURE** | • | - | - | - | X | X | - | - | - | - | - | |
| **T.EAVESDROPPING** | - | - | - | - | X | X | - | - | - | - | - | |
| **T.DATA_MODIFICATION** | • | - | - | - | - | X | X | - | - | - | - | |
| **T.DATA_CORRUPTION** | - | - | - | - | - | - | X | - | - | - | - | |
| **T.MALFUNCTION** | - | - | - | - | - | - | - | - | X | - | - | |
| **T.TSF_COMPROMISE** | - | - | - | - | - | - | - | - | - | X | - | |
| **T.TSF_BYPASS** | - | - | - | - | - | - | - | - | - | X | - | |
| **T.PHYSICAL_ATTACK** | - | - | - | - | - | - | - | - | - | - | X | |
| **[TODO: Weitere Bedrohungen]** | | | | | | | | | | | | |

**Analyse:**
- Alle Bedrohungen sind durch mindestens ein Sicherheitsziel abgedeckt ✓
- Mehrfachabdeckung zeigt Defense-in-Depth Ansatz
- **[TODO: Ergänze spezifische Analysen für dein TOE]**

## 3. Organisatorische Sicherheitsrichtlinien vs. Sicherheitsziele

Die folgende Matrix zeigt, welche Sicherheitsziele welche OSPs umsetzen:

| OSP | O.ACCESS_CONTROL | O.IDENTIFICATION_AUTHENTICATION | O.AUDIT_GENERATION | O.AUDIT_PROTECTION | O.DATA_CONFIDENTIALITY | O.CRYPTOGRAPHIC_OPERATIONS | O.DATA_INTEGRITY | O.SECURITY_MANAGEMENT | O.SECURE_STATE | O.TSF_PROTECTION | **[TODO]** |
|-----|------------------|--------------------------------|-------------------|-------------------|------------------------|---------------------------|------------------|----------------------|---------------|-----------------|------------|
| **P.ACCESS_CONTROL** | X | • | - | - | - | - | - | - | - | - | |
| **P.ACCOUNTABILITY** | - | - | X | X | - | - | - | - | - | - | |
| **P.CONFIDENTIALITY** | • | - | - | - | X | • | - | - | - | - | |
| **P.INTEGRITY** | • | - | - | - | - | • | X | - | - | - | |
| **P.MANAGEMENT** | - | - | - | - | - | - | - | X | - | - | |
| **[TODO: Weitere OSPs]** | | | | | | | | | | | |

**Analyse:**
- Alle OSPs sind durch mindestens ein Sicherheitsziel umgesetzt ✓
- Klare Zuordnung zwischen Richtlinien und technischen Zielen
- **[TODO: Ergänze spezifische Analysen für dein TOE]**

## 4. Annahmen vs. Umgebungsziele

Die folgende Matrix zeigt, welche Umgebungsziele welche Annahmen erfüllen:

| Annahme | OE.PHYSICAL_PROTECTION | OE.TRUSTED_ADMIN | OE.USER_TRAINING | OE.NETWORK_PROTECTION | OE.EXTERNAL_SYSTEMS | OE.TIME_STAMPS | **[TODO]** |
|---------|----------------------|------------------|------------------|----------------------|---------------------|---------------|------------|
| **A.PHYSICAL_SECURITY** | X | - | - | - | - | - | |
| **A.TRUSTED_ADMIN** | - | X | - | - | - | - | |
| **A.USER_TRAINING** | - | - | X | - | - | - | |
| **A.NETWORK_SECURITY** | - | - | - | X | - | - | |
| **A.EXTERNAL_SYSTEMS** | - | - | - | - | X | - | |
| **A.TIME_SOURCE** | - | - | - | - | - | X | |
| **[TODO: Weitere Annahmen]** | | | | | | | |

**Analyse:**
- Alle Annahmen sind durch mindestens ein Umgebungsziel erfüllt ✓
- Klare Trennung zwischen TOE- und Umgebungsverantwortlichkeiten
- **[TODO: Ergänze spezifische Analysen für dein TOE]**

## 5. Umgekehrte Rückverfolgbarkeit: Sicherheitsziele zu Sicherheitsproblemen

Die folgende Matrix zeigt die umgekehrte Perspektive - welche Bedrohungen/OSPs/Annahmen jedes Sicherheitsziel rechtfertigen:

### 5.1 TOE-Sicherheitsziele

| Sicherheitsziel | Adressierte Bedrohungen | Umgesetzte OSPs | Begründung |
|-----------------|------------------------|-----------------|------------|
| **O.ACCESS_CONTROL** | T.UNAUTHORIZED_ACCESS, T.PRIVILEGE_ESCALATION | P.ACCESS_CONTROL | Kontrolliert Zugriff auf Ressourcen |
| **O.IDENTIFICATION_AUTHENTICATION** | T.MASQUERADE | - | Verhindert Identitätsvortäuschung |
| **O.AUDIT_GENERATION** | T.AUDIT_COMPROMISE | P.ACCOUNTABILITY | Zeichnet sicherheitsrelevante Ereignisse auf |
| **O.AUDIT_PROTECTION** | T.AUDIT_COMPROMISE | - | Schützt Audit-Daten vor Manipulation |
| **O.DATA_CONFIDENTIALITY** | T.DATA_DISCLOSURE, T.EAVESDROPPING | P.CONFIDENTIALITY | Schützt sensible Daten vor Offenlegung |
| **O.CRYPTOGRAPHIC_OPERATIONS** | T.DATA_DISCLOSURE, T.DATA_MODIFICATION | - | Bietet kryptografische Mechanismen |
| **O.DATA_INTEGRITY** | T.DATA_MODIFICATION, T.DATA_CORRUPTION | P.INTEGRITY | Schützt Datenintegrität |
| **O.SECURITY_MANAGEMENT** | - | P.MANAGEMENT | Ermöglicht Verwaltung von Sicherheitsfunktionen |
| **O.SECURE_STATE** | T.MALFUNCTION | - | Gewährleistet sicheren Zustand bei Fehlern |
| **O.TSF_PROTECTION** | T.TSF_COMPROMISE, T.TSF_BYPASS | - | Schützt Sicherheitsfunktionen selbst |
| **[TODO: Weitere Ziele]** | | | |

**Ergebnis:** Alle TOE-Sicherheitsziele sind durch Bedrohungen oder OSPs gerechtfertigt ✓

### 5.2 Umgebungsziele

| Umgebungsziel | Erfüllte Annahmen | Adressierte Bedrohungen | Begründung |
|---------------|-------------------|------------------------|------------|
| **OE.PHYSICAL_PROTECTION** | A.PHYSICAL_SECURITY | T.PHYSICAL_ATTACK | Schützt TOE vor physischem Zugriff |
| **OE.TRUSTED_ADMIN** | A.TRUSTED_ADMIN | - | Stellt vertrauenswürdige Administratoren sicher |
| **OE.USER_TRAINING** | A.USER_TRAINING | - | Schult Benutzer in sicherer Verwendung |
| **OE.NETWORK_PROTECTION** | A.NETWORK_SECURITY | - | Schützt TOE vor Netzwerkangriffen |
| **OE.EXTERNAL_SYSTEMS** | A.EXTERNAL_SYSTEMS | - | Stellt Sicherheit externer Systeme sicher |
| **OE.TIME_STAMPS** | A.TIME_SOURCE | - | Bietet zuverlässige Zeitstempel |
| **[TODO: Weitere Ziele]** | | | |

**Ergebnis:** Alle Umgebungsziele sind durch Annahmen gerechtfertigt ✓

## 6. Vollständigkeitsanalyse

### 6.1 Bedrohungsabdeckung

**Gesamtzahl der Bedrohungen:** 12 **[TODO: Aktualisiere Anzahl]**  
**Abgedeckte Bedrohungen:** 12 **[TODO: Aktualisiere Anzahl]**  
**Nicht abgedeckte Bedrohungen:** 0 **[TODO: Aktualisiere Anzahl]**

**Status:** ✓ Vollständig abgedeckt

**[TODO: Liste nicht abgedeckte Bedrohungen auf, falls vorhanden]**

### 6.2 OSP-Abdeckung

**Gesamtzahl der OSPs:** 5 **[TODO: Aktualisiere Anzahl]**  
**Umgesetzte OSPs:** 5 **[TODO: Aktualisiere Anzahl]**  
**Nicht umgesetzte OSPs:** 0 **[TODO: Aktualisiere Anzahl]**

**Status:** ✓ Vollständig umgesetzt

**[TODO: Liste nicht umgesetzte OSPs auf, falls vorhanden]**

### 6.3 Annahmenabdeckung

**Gesamtzahl der Annahmen:** 6 **[TODO: Aktualisiere Anzahl]**  
**Erfüllte Annahmen:** 6 **[TODO: Aktualisiere Anzahl]**  
**Nicht erfüllte Annahmen:** 0 **[TODO: Aktualisiere Anzahl]**

**Status:** ✓ Vollständig erfüllt

**[TODO: Liste nicht erfüllte Annahmen auf, falls vorhanden]**

### 6.4 Zielrechtfertigung

**Gesamtzahl der Sicherheitsziele:** 16 **[TODO: Aktualisiere Anzahl]**  
**Gerechtfertigte Ziele:** 16 **[TODO: Aktualisiere Anzahl]**  
**Nicht gerechtfertigte Ziele:** 0 **[TODO: Aktualisiere Anzahl]**

**Status:** ✓ Alle Ziele gerechtfertigt

**[TODO: Liste nicht gerechtfertigte Ziele auf, falls vorhanden]**

## 7. Lückenanalyse

### 7.1 Identifizierte Lücken

**[TODO: Dokumentiere identifizierte Lücken in der Abdeckung]**

Beispiel:
- **Lücke 1:** Bedrohung T.XXX ist nicht durch Sicherheitsziele abgedeckt
  - **Auswirkung:** [Beschreibung]
  - **Empfohlene Maßnahme:** Ergänze Sicherheitsziel O.XXX
  
- **Lücke 2:** Sicherheitsziel O.YYY ist nicht durch Bedrohungen/OSPs gerechtfertigt
  - **Auswirkung:** [Beschreibung]
  - **Empfohlene Maßnahme:** Entferne Ziel oder identifiziere rechtfertigende Bedrohung

**Aktueller Status:** Keine Lücken identifiziert ✓

### 7.2 Redundanzen und Überlappungen

**[TODO: Dokumentiere Redundanzen zwischen Sicherheitszielen]**

Beispiel:
- **Überlappung 1:** O.XXX und O.YYY adressieren beide T.ZZZ
  - **Analyse:** [Ist dies beabsichtigt? Defense-in-Depth?]
  - **Empfehlung:** [Konsolidieren oder beibehalten]

**Aktueller Status:** Überlappungen sind beabsichtigt (Defense-in-Depth) ✓

## 8. Änderungsmanagement

### 8.1 Auswirkungsanalyse bei Änderungen

Wenn Änderungen an der Sicherheitsproblem-Definition oder den Sicherheitszielen vorgenommen werden, muss die Coverage Matrix aktualisiert werden:

**Bei Hinzufügen einer neuen Bedrohung:**
1. Füge Zeile in Matrix 2 hinzu
2. Identifiziere adressierende Sicherheitsziele
3. Falls keine Ziele vorhanden: Erstelle neues Sicherheitsziel
4. Aktualisiere Vollständigkeitsanalyse

**Bei Hinzufügen eines neuen Sicherheitsziels:**
1. Füge Spalte in Matrix 2 und 3 hinzu
2. Identifiziere adressierte Bedrohungen/OSPs
3. Falls keine Bedrohungen/OSPs: Prüfe Notwendigkeit des Ziels
4. Aktualisiere umgekehrte Rückverfolgbarkeit

**Bei Entfernen einer Bedrohung:**
1. Entferne Zeile aus Matrix 2
2. Prüfe, ob zugeordnete Sicherheitsziele noch gerechtfertigt sind
3. Aktualisiere Vollständigkeitsanalyse

**Bei Entfernen eines Sicherheitsziels:**
1. Entferne Spalte aus Matrizen
2. Prüfe, ob alle Bedrohungen/OSPs noch abgedeckt sind
3. Falls nicht: Identifiziere alternatives Ziel oder erstelle neues Ziel

### 8.2 Änderungshistorie

| Datum | Änderung | Auswirkung | Bearbeiter |
|-------|----------|------------|------------|
| [Date] | Initiale Version | - | [TODO] |
| **[TODO]** | | | |

## 9. Zusammenfassung

Die Coverage Matrix demonstriert:

1. **Vollständigkeit:** ✓
   - Alle Bedrohungen sind durch Sicherheitsziele abgedeckt
   - Alle OSPs sind durch Sicherheitsziele umgesetzt
   - Alle Annahmen sind durch Umgebungsziele erfüllt

2. **Rückverfolgbarkeit:** ✓
   - Alle Sicherheitsziele sind durch Bedrohungen/OSPs gerechtfertigt
   - Alle Umgebungsziele sind durch Annahmen gerechtfertigt

3. **Konsistenz:** ✓
   - Keine Lücken in der Abdeckung
   - Keine ungerechtfertigten Ziele

Die Sicherheitsziele bilden eine vollständige und konsistente Grundlage für die Ableitung der Sicherheitsanforderungen (SFRs und SARs).

## 10. Nächste Schritte

Nach der Coverage Matrix:
1. Leite Sicherheitsanforderungen (SFRs) aus den TOE-Sicherheitszielen ab (siehe Template 0400-0450)
2. Definiere Sicherheitsanforderungen für die Umgebung basierend auf Umgebungszielen
3. Erstelle Rationale für Sicherheitsanforderungen

## 11. Referenzen

- ISO/IEC 15408-1: Security Target Evaluation
- ISO/IEC 15408-2: Security Functional Components
- Template 0200-0240: Sicherheitsproblem-Definition
- Template 0300: Sicherheitsziele
- Template 0310: Rationale für Sicherheitsziele
- Template 0400-0450: Sicherheitsanforderungen

