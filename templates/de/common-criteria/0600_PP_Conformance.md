# Protection Profile Konformität

**Dokument-ID:** 0600
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

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und HTML-Kommentare mit projektspezifischen Informationen.

<!-- 
ANLEITUNG FÜR TEMPLATE-AUTOREN:
Dieses Template dokumentiert die Konformität des Security Target (ST) mit einem oder mehreren Protection Profiles (PP).
Falls keine PP-Konformität beansprucht wird, dokumentieren Sie dies explizit.

Wichtige Aspekte:
- Identifizieren Sie alle relevanten Protection Profiles
- Dokumentieren Sie den Konformitätsanspruch (strict, demonstrable, oder keine Konformität)
- Listen Sie alle Abweichungen vom PP auf
- Begründen Sie jede Abweichung
- Verweisen Sie auf entsprechende ST-Abschnitte
-->

## Übersicht

Dieses Kapitel dokumentiert die Konformität des Security Target (ST) mit relevanten Protection Profiles (PP) gemäß ISO/IEC 15408.

<!-- Beschreiben Sie kurz, ob und mit welchen PPs Konformität beansprucht wird -->

**PP-Konformitätsanspruch:** [TODO: Strict / Demonstrable / Keine Konformität]

## Protection Profile Identifikation

<!-- Listen Sie alle relevanten Protection Profiles auf -->

### PP 1: [TODO: PP-Name]

- **PP-Titel:** [TODO: Vollständiger Titel des Protection Profile]
- **PP-Version:** [TODO: Version]
- **PP-Datum:** [TODO: Veröffentlichungsdatum]
- **PP-Registrierung:** [TODO: Registrierungsnummer falls vorhanden]
- **PP-Herausgeber:** [TODO: Organisation]
- **Konformitätstyp:** [TODO: Strict / Demonstrable]

**Beschreibung:**
<!-- Kurze Beschreibung des PP und seiner Relevanz für das TOE -->
[TODO: Beschreiben Sie das Protection Profile und warum es für dieses TOE relevant ist]

### PP 2: [TODO: PP-Name] (falls zutreffend)

- **PP-Titel:** [TODO: Vollständiger Titel]
- **PP-Version:** [TODO: Version]
- **PP-Datum:** [TODO: Datum]
- **PP-Registrierung:** [TODO: Nummer]
- **PP-Herausgeber:** [TODO: Organisation]
- **Konformitätstyp:** [TODO: Strict / Demonstrable]

**Beschreibung:**
[TODO: Beschreibung]

## Konformitätsanspruch

<!-- Dokumentieren Sie den spezifischen Konformitätsanspruch -->

### Strict Conformance (Strikte Konformität)

<!-- Falls strikte Konformität beansprucht wird -->

[TODO: Dokumentieren Sie, dass das ST alle Anforderungen des PP ohne Änderungen übernimmt]

**Konformitätserklärung:**
- Alle Security Functional Requirements (SFRs) aus dem PP sind im ST enthalten
- Alle Security Assurance Requirements (SARs) aus dem PP sind im ST enthalten
- Alle Sicherheitsziele aus dem PP sind im ST enthalten
- Keine Abweichungen vom PP

### Demonstrable Conformance (Nachweisbare Konformität)

<!-- Falls nachweisbare Konformität beansprucht wird -->

[TODO: Dokumentieren Sie, wie das ST die Anforderungen des PP erfüllt, auch wenn Anpassungen vorgenommen wurden]

**Konformitätserklärung:**
- Das ST erfüllt die Sicherheitsziele des PP
- Das ST kann Zusatzanforderungen enthalten
- Das ST kann PP-Anforderungen verfeinern oder erweitern
- Alle Abweichungen sind dokumentiert und begründet

### Keine PP-Konformität

<!-- Falls keine PP-Konformität beansprucht wird -->

[TODO: Begründen Sie, warum keine PP-Konformität beansprucht wird]

**Begründung:**
[TODO: Erklären Sie die Gründe für die Entscheidung, keine PP-Konformität zu beanspruchen]

## Konformitätsanalyse

<!-- Detaillierte Analyse der Konformität mit jedem PP -->

### Konformität mit [TODO: PP-Name]

#### Security Functional Requirements (SFR)

<!-- Vergleichen Sie die SFRs des PP mit denen des ST -->

| PP SFR | ST SFR | Status | Kommentar |
|--------|--------|--------|-----------|
| [TODO: PP-SFR-ID] | [TODO: ST-SFR-ID] | Identisch / Erweitert / Verfeinert | [TODO: Erläuterung] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Zusammenfassung:**
[TODO: Fassen Sie die SFR-Konformität zusammen]

#### Security Assurance Requirements (SAR)

<!-- Vergleichen Sie die SARs des PP mit denen des ST -->

| PP SAR | ST SAR | Status | Kommentar |
|--------|--------|--------|-----------|
| [TODO: PP-SAR-ID] | [TODO: ST-SAR-ID] | Identisch / Erweitert | [TODO: Erläuterung] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Zusammenfassung:**
[TODO: Fassen Sie die SAR-Konformität zusammen]

#### Sicherheitsziele

<!-- Vergleichen Sie die Sicherheitsziele des PP mit denen des ST -->

| PP-Sicherheitsziel | ST-Sicherheitsziel | Status | Kommentar |
|--------------------|-------------------|--------|-----------|
| [TODO: PP-Ziel-ID] | [TODO: ST-Ziel-ID] | Identisch / Erweitert | [TODO: Erläuterung] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Zusammenfassung:**
[TODO: Fassen Sie die Konformität der Sicherheitsziele zusammen]

## Abweichungen vom Protection Profile

<!-- Dokumentieren Sie alle Abweichungen vom PP -->

### Abweichung 1: [TODO: Titel]

- **Betroffener PP-Abschnitt:** [TODO: Abschnitt/Anforderung]
- **Art der Abweichung:** [TODO: Hinzufügung / Verfeinerung / Auslassung / Änderung]
- **Beschreibung:** [TODO: Beschreiben Sie die Abweichung im Detail]
- **Begründung:** [TODO: Erklären Sie, warum diese Abweichung notwendig ist]
- **Auswirkung auf Sicherheit:** [TODO: Bewerten Sie die Sicherheitsauswirkungen]
- **Verweis auf ST-Abschnitt:** [TODO: Abschnittsnummer im ST]

### Abweichung 2: [TODO: Titel] (falls zutreffend)

- **Betroffener PP-Abschnitt:** [TODO]
- **Art der Abweichung:** [TODO]
- **Beschreibung:** [TODO]
- **Begründung:** [TODO]
- **Auswirkung auf Sicherheit:** [TODO]
- **Verweis auf ST-Abschnitt:** [TODO]

## Zusätzliche Anforderungen

<!-- Dokumentieren Sie alle Anforderungen im ST, die nicht im PP enthalten sind -->

### Zusätzliche SFRs

| ST SFR | Beschreibung | Begründung |
|--------|--------------|------------|
| [TODO: SFR-ID] | [TODO: Kurzbeschreibung] | [TODO: Warum wurde diese SFR hinzugefügt?] |
| [TODO] | [TODO] | [TODO] |

### Zusätzliche SARs

| ST SAR | Beschreibung | Begründung |
|--------|--------------|------------|
| [TODO: SAR-ID] | [TODO: Kurzbeschreibung] | [TODO: Warum wurde diese SAR hinzugefügt?] |
| [TODO] | [TODO] | [TODO] |

### Zusätzliche Sicherheitsziele

| ST-Ziel | Beschreibung | Begründung |
|---------|--------------|------------|
| [TODO: Ziel-ID] | [TODO: Kurzbeschreibung] | [TODO: Warum wurde dieses Ziel hinzugefügt?] |
| [TODO] | [TODO] | [TODO] |

## Konformitätsbewertung

<!-- Zusammenfassende Bewertung der PP-Konformität -->

### Konformitätsstatus

**Gesamtbewertung:** [TODO: Konform / Konform mit Abweichungen / Nicht konform]

**Zusammenfassung:**
[TODO: Fassen Sie den Konformitätsstatus zusammen und bewerten Sie, ob das ST die Anforderungen des PP erfüllt]

### Konformitätsnachweis

<!-- Dokumentieren Sie, wie die Konformität nachgewiesen wird -->

[TODO: Beschreiben Sie die Methodik und Nachweise für die PP-Konformität]

**Nachweisdokumentation:**
- [TODO: Verweis auf relevante ST-Abschnitte]
- [TODO: Verweis auf Mapping-Tabellen]
- [TODO: Verweis auf Rationale-Dokumente]

## Referenzen

<!-- Listen Sie alle referenzierten Protection Profiles und zugehörige Dokumente auf -->

1. [TODO: PP-Referenz 1]
2. [TODO: PP-Referenz 2]
3. [TODO: Weitere relevante Dokumente]

**Nächste Schritte:**
1. Identifizieren Sie alle relevanten Protection Profiles
2. Dokumentieren Sie den Konformitätsanspruch
3. Führen Sie eine detaillierte Konformitätsanalyse durch
4. Dokumentieren Sie alle Abweichungen und Zusatzanforderungen
5. Erstellen Sie Mapping-Tabellen zwischen PP und ST
6. Lassen Sie die PP-Konformität durch Evaluatoren prüfen

