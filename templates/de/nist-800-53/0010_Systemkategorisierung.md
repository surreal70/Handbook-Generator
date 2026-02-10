# Systemkategorisierung

**Dokument-ID:** NIST-0010  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents the FIPS 199 system categorization process.
It aligns with NIST SP 800-60 (Guide for Mapping Types of Information and Information Systems to Security Categories).

Customization required:
- Determine security impact levels for confidentiality, integrity, and availability
- Identify information types processed by the system
- Document categorization rationale
- Obtain Authorizing Official approval
-->

## 1. Zweck

Dieses Dokument beschreibt die Kategorisierung des Informationssystems {{ meta.nist.system_name }} gemäß FIPS 199 und NIST SP 800-60.

### 1.1 Ziele

- **FIPS 199-Konformität:** Kategorisierung nach Sicherheitszielen (Vertraulichkeit, Integrität, Verfügbarkeit)
- **Risikobewertung:** Bestimmung der potenziellen Auswirkungen bei Sicherheitsverletzungen
- **Baseline-Auswahl:** Grundlage für die Auswahl der Sicherheitskontrollen
- **Compliance:** Erfüllung bundesweiter Anforderungen

### 1.2 Referenzen

- **FIPS 199:** Standards for Security Categorization of Federal Information and Information Systems
- **NIST SP 800-60 Vol. 1 Rev. 1:** Guide for Mapping Types of Information and Information Systems to Security Categories
- **NIST SP 800-60 Vol. 2 Rev. 1:** Appendices to Guide for Mapping Types of Information and Information Systems to Security Categories
- **NIST SP 800-53 Rev. 5:** Security and Privacy Controls for Information Systems and Organizations

## 2. Systeminformationen

### 2.1 Systemidentifikation

**Systemname:** {{ meta.nist.system_name }}  
**System-ID:** {{ meta.nist.system_id }}  
**System Owner:** [TODO: Name] ([TODO: E-Mail])  
**Authorizing Official (AO):** {{ meta.roles.ao.name }} ({{ meta.roles.ao.email }})  
**Information System Security Officer (ISSO):** {{ meta.roles.isso.name }} ({{ meta.roles.isso.email }})  

### 2.2 Systembeschreibung

**Zweck:** [TODO: Beschreibung des Systemzwecks]

**Funktionen:**
- [TODO: Hauptfunktion 1]
- [TODO: Hauptfunktion 2]
- [TODO: Hauptfunktion 3]

**Benutzer:**
- **Interne Benutzer:** [TODO: Anzahl und Rollen]
- **Externe Benutzer:** [TODO: Anzahl und Rollen]
- **Privilegierte Benutzer:** [TODO: Anzahl und Rollen]

### 2.3 Informationstypen

| Informationstyp | Beschreibung | Quelle (NIST 800-60) |
|-----------------|--------------|----------------------|
| [TODO: Typ 1] | [TODO: Beschreibung] | [TODO: C.2.x.x] |
| [TODO: Typ 2] | [TODO: Beschreibung] | [TODO: C.3.x.x] |
| [TODO: Typ 3] | [TODO: Beschreibung] | [TODO: C.4.x.x] |

## 3. FIPS 199 Kategorisierung

### 3.1 Sicherheitsziele und Impact Levels

Die Kategorisierung erfolgt nach den drei Sicherheitszielen:

#### 3.1.1 Vertraulichkeit (Confidentiality)

**Definition:** Schutz vor unbefugter Offenlegung von Informationen.

**Impact Level:** [TODO: Low / Moderate / High]

**Begründung:**
[TODO: Beschreiben Sie die potenziellen Auswirkungen einer unbefugten Offenlegung]

**Beispiele für Auswirkungen:**
- **Low:** Begrenzte negative Auswirkungen auf Organisationsoperationen, -vermögen oder -personen
- **Moderate:** Ernsthafte negative Auswirkungen
- **High:** Schwerwiegende oder katastrophale negative Auswirkungen

**Spezifische Auswirkungen für dieses System:**
- [TODO: Auswirkung 1]
- [TODO: Auswirkung 2]
- [TODO: Auswirkung 3]

#### 3.1.2 Integrität (Integrity)

**Definition:** Schutz vor unbefugter Änderung oder Zerstörung von Informationen.

**Impact Level:** [TODO: Low / Moderate / High]

**Begründung:**
[TODO: Beschreiben Sie die potenziellen Auswirkungen einer unbefugten Änderung]

**Spezifische Auswirkungen für dieses System:**
- [TODO: Auswirkung 1]
- [TODO: Auswirkung 2]
- [TODO: Auswirkung 3]

#### 3.1.3 Verfügbarkeit (Availability)

**Definition:** Sicherstellung des rechtzeitigen und zuverlässigen Zugriffs auf Informationen.

**Impact Level:** [TODO: Low / Moderate / High]

**Begründung:**
[TODO: Beschreiben Sie die potenziellen Auswirkungen eines Verfügbarkeitsverlusts]

**Spezifische Auswirkungen für dieses System:**
- [TODO: Auswirkung 1]
- [TODO: Auswirkung 2]
- [TODO: Auswirkung 3]

### 3.2 Gesamtkategorisierung

**FIPS 199 Security Category:**

```
SC {{ meta.nist.system_name }} = {(confidentiality, [TODO: impact]), (integrity, [TODO: impact]), (availability, [TODO: impact])}
```

**Beispiel:**
```
SC Information System = {(confidentiality, MODERATE), (integrity, MODERATE), (availability, LOW)}
```

**Overall System Categorization:** [TODO: Low / Moderate / High]

> **Hinweis:** Die Gesamtkategorisierung entspricht dem höchsten Impact Level der drei Sicherheitsziele (High-Water Mark).

## 4. Kategorisierung nach Informationstypen

### 4.1 Informationstyp-Analyse

Für jeden Informationstyp wird die Kategorisierung gemäß NIST SP 800-60 durchgeführt:

#### Informationstyp 1: [TODO: Name]

**Beschreibung:** [TODO: Beschreibung des Informationstyps]

**NIST 800-60 Referenz:** [TODO: C.x.x.x]

| Sicherheitsziel | Provisional Impact | Angepasster Impact | Begründung |
|-----------------|-------------------|-------------------|------------|
| Vertraulichkeit | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Begründung] |
| Integrität | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Begründung] |
| Verfügbarkeit | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Begründung] |

#### Informationstyp 2: [TODO: Name]

**Beschreibung:** [TODO: Beschreibung des Informationstyps]

**NIST 800-60 Referenz:** [TODO: C.x.x.x]

| Sicherheitsziel | Provisional Impact | Angepasster Impact | Begründung |
|-----------------|-------------------|-------------------|------------|
| Vertraulichkeit | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Begründung] |
| Integrität | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Begründung] |
| Verfügbarkeit | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Begründung] |

### 4.2 Aggregierte Kategorisierung

**Methode:** High-Water Mark (höchster Impact Level über alle Informationstypen)

| Sicherheitsziel | Aggregierter Impact |
|-----------------|---------------------|
| Vertraulichkeit | [TODO: Low / Moderate / High] |
| Integrität | [TODO: Low / Moderate / High] |
| Verfügbarkeit | [TODO: Low / Moderate / High] |

## 5. Baseline-Auswahl

### 5.1 NIST 800-53 Baseline

Basierend auf der Gesamtkategorisierung wird folgende Baseline ausgewählt:

**Ausgewählte Baseline:** [TODO: Low / Moderate / High Baseline]

**Baseline-Kontrollen:**
- **Low Baseline:** NIST SP 800-53B, Appendix A
- **Moderate Baseline:** NIST SP 800-53B, Appendix B
- **High Baseline:** NIST SP 800-53B, Appendix C

### 5.2 Tailoring

**Tailoring-Aktivitäten:**
- **Hinzugefügte Kontrollen:** [TODO: Liste zusätzlicher Kontrollen]
- **Entfernte Kontrollen:** [TODO: Liste entfernter Kontrollen mit Begründung]
- **Angepasste Kontrollen:** [TODO: Liste angepasster Kontrollen]

## 6. Kategorisierungsprozess

### 6.1 Prozessschritte

1. **Systemidentifikation:** Identifikation des zu kategorisierenden Systems
2. **Informationstyp-Identifikation:** Identifikation aller verarbeiteten Informationstypen
3. **Provisional Impact:** Bestimmung der provisorischen Impact Levels gemäß NIST 800-60
4. **Impact-Anpassung:** Anpassung basierend auf organisationsspezifischen Faktoren
5. **Aggregation:** Aggregation zu Gesamtkategorisierung
6. **Dokumentation:** Dokumentation der Kategorisierung
7. **Genehmigung:** Genehmigung durch Authorizing Official

### 6.2 Beteiligte Rollen

| Rolle | Name | Verantwortlichkeit |
|-------|------|-------------------|
| System Owner | [TODO: Name] | Systemverantwortung |
| Information Owner | [TODO: Name] | Informationsverantwortung |
| ISSO | {{ meta.roles.isso.name }} | Sicherheitsbewertung |
| ISSM | {{ meta.roles.issm.name }} | Sicherheitsmanagement |
| Authorizing Official (AO) | {{ meta.roles.ao.name }} | Genehmigung |

### 6.3 Kategorisierungsdatum

**Initiale Kategorisierung:** [TODO: Datum]  
**Letzte Überprüfung:** [TODO: Datum]  
**Nächste Überprüfung:** [TODO: Datum]  

## 7. Auswirkungsanalyse

### 7.1 Vertraulichkeitsverlust

**Potenzielle Auswirkungen bei unbefugter Offenlegung:**

| Bereich | Auswirkung | Schweregrad |
|---------|------------|-------------|
| Organisationsoperationen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Organisationsvermögen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Personen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Nationale Sicherheit | [TODO: Beschreibung] | [TODO: L/M/H] |

### 7.2 Integritätsverlust

**Potenzielle Auswirkungen bei unbefugter Änderung:**

| Bereich | Auswirkung | Schweregrad |
|---------|------------|-------------|
| Organisationsoperationen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Organisationsvermögen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Personen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Nationale Sicherheit | [TODO: Beschreibung] | [TODO: L/M/H] |

### 7.3 Verfügbarkeitsverlust

**Potenzielle Auswirkungen bei Systemausfall:**

| Bereich | Auswirkung | Schweregrad |
|---------|------------|-------------|
| Organisationsoperationen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Organisationsvermögen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Personen | [TODO: Beschreibung] | [TODO: L/M/H] |
| Nationale Sicherheit | [TODO: Beschreibung] | [TODO: L/M/H] |

## 8. Genehmigung

### 8.1 Kategorisierungsgenehmigung

**Kategorisierung genehmigt durch:**

**Name:** {{ meta.roles.ao.name }}  
**Titel:** Authorizing Official (AO)  
**Datum:** [TODO: Datum]  
**Unterschrift:** [TODO: Unterschrift oder elektronische Genehmigung]  

### 8.2 Überprüfungsintervall

**Überprüfungsfrequenz:** [TODO: Jährlich / Bei signifikanten Änderungen]

**Auslöser für Neukategorisierung:**
- Signifikante Änderungen am System
- Neue Informationstypen
- Änderungen in der Bedrohungslandschaft
- Organisatorische Änderungen
- Gesetzliche oder regulatorische Änderungen

## 9. Anhang

### 9.1 FIPS 199 Impact Level Definitionen

**Low Impact:**
> The potential impact is LOW if the loss of confidentiality, integrity, or availability could be expected to have a limited adverse effect on organizational operations, organizational assets, or individuals.

**Moderate Impact:**
> The potential impact is MODERATE if the loss of confidentiality, integrity, or availability could be expected to have a serious adverse effect on organizational operations, organizational assets, or individuals.

**High Impact:**
> The potential impact is HIGH if the loss of confidentiality, integrity, or availability could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, or individuals.

### 9.2 Kategorisierungsmatrix

| Informationstyp | Vertraulichkeit | Integrität | Verfügbarkeit | Gesamt |
|-----------------|-----------------|------------|---------------|--------|
| [TODO: Typ 1] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] |
| [TODO: Typ 2] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] |
| [TODO: Typ 3] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] |
| **System Gesamt** | **[TODO: L/M/H]** | **[TODO: L/M/H]** | **[TODO: L/M/H]** | **[TODO: L/M/H]** |

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
