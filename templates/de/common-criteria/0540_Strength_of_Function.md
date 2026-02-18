# Strength of Function (Stärke der Sicherheitsfunktionen)

**Dokument-ID:** 0540
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

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches TOE (Target of Evaluation) an.

<!-- 
ANLEITUNG FÜR TEMPLATE-AUTOREN:
Die Strength of Function (SOF) Analyse bewertet die Stärke probabilistischer oder
permutationsbasierter Sicherheitsmechanismen gegen Angriffe.

WICHTIGE HINWEISE:
- SOF gilt nur für probabilistische/permutationsbasierte Mechanismen (z.B. Passwörter, Schlüssel)
- SOF gilt NICHT für deterministische Mechanismen (z.B. Zugriffskontrolllisten)
- Die Analyse muss mathematisch fundiert sein
- Berücksichtige realistische Angriffsszenarien
- Dokumentiere alle Annahmen
-->

## 1. Einleitung

### 1.1 Zweck

Dieses Dokument analysiert die Strength of Function (SOF) für **[TODO: TOE-Name]**. Die SOF-Analyse bewertet die Stärke probabilistischer oder permutationsbasierter Sicherheitsmechanismen gegen verschiedene Angriffsarten.

### 1.2 SOF-Konzept

**Definition:**
Die Strength of Function ist ein Maß für die Mindeststärke, die ein TOE-Sicherheitsmechanismus gegen direkte Angriffe bietet. Sie wird ausgedrückt als die Wahrscheinlichkeit, dass ein Angreifer den Mechanismus in einer bestimmten Zeit mit bestimmten Ressourcen überwinden kann.

**SOF-Levels:**
- **SOF-basic**: Schutz gegen Angreifer mit begrenzten Ressourcen und Fähigkeiten
- **SOF-medium**: Schutz gegen Angreifer mit moderaten Ressourcen und Fähigkeiten
- **SOF-high**: Schutz gegen Angreifer mit hohen Ressourcen und Fähigkeiten

### 1.3 Anwendbarkeit

SOF gilt für folgende Arten von Mechanismen:
- Passwort-basierte Authentisierung
- Biometrische Authentisierung
- Zufallszahlengeneratoren
- Kryptografische Schlüsselgenerierung (bei probabilistischen Verfahren)
- Challenge-Response-Mechanismen

SOF gilt NICHT für:
- Deterministische Zugriffskontrollmechanismen
- Kryptografische Algorithmen selbst (diese werden separat bewertet)
- Audit-Mechanismen
- Zeitstempel-Mechanismen

## 2. SOF-Claim

### 2.1 Beanspruchtes SOF-Level

Das TOE beansprucht folgendes SOF-Level:

**SOF-Claim:** [TODO: SOF-basic / SOF-medium / SOF-high]

<!-- 
ANLEITUNG:
Wähle das SOF-Level basierend auf:
- Der Bedrohungsanalyse (Kapitel 2 des Security Target)
- Den erwarteten Angreiferfähigkeiten
- Den Sicherheitszielen
- Den Anforderungen der Stakeholder

SOF-basic: Angreifer mit begrenzten Ressourcen (z.B. Einzelperson, einfache Tools)
SOF-medium: Angreifer mit moderaten Ressourcen (z.B. kleine Gruppe, spezialisierte Tools)
SOF-high: Angreifer mit hohen Ressourcen (z.B. organisierte Gruppe, erhebliche Ressourcen)
-->

**Begründung für SOF-Claim:**

[TODO: Begründe die Wahl des SOF-Levels. Beispiel:]

Das TOE wird in einer Umgebung eingesetzt, in der folgende Bedrohungen bestehen:
- [TODO: Beschreibe die relevanten Threats aus Kapitel 2]
- [TODO: Beschreibe die erwarteten Angreiferfähigkeiten]
- [TODO: Beschreibe die Sicherheitsziele]

Basierend auf dieser Analyse ist SOF-[TODO] angemessen, da:
- [TODO: Begründung 1]
- [TODO: Begründung 2]
- [TODO: Begründung 3]

## 3. Identifikation probabilistischer Mechanismen

### 3.1 Übersicht

Die folgenden probabilistischen oder permutationsbasierten Mechanismen wurden im TOE identifiziert:

| Mechanismus-ID | Mechanismus-Name | TSF-ID | Typ | SOF-relevant |
|----------------|------------------|--------|-----|--------------|
| M-1 | [TODO] | TSF-[TODO] | [TODO: Passwort/Biometrie/RNG/etc.] | Ja/Nein |
| M-2 | [TODO] | TSF-[TODO] | [TODO] | Ja/Nein |
| M-3 | [TODO] | TSF-[TODO] | [TODO] | Ja/Nein |

<!-- 
ANLEITUNG:
- Identifiziere alle probabilistischen/permutationsbasierten Mechanismen
- Ordne sie den entsprechenden TSFs zu
- Klassifiziere den Typ des Mechanismus
- Markiere, ob der Mechanismus SOF-relevant ist
-->

### 3.2 Nicht-SOF-relevante Mechanismen

Die folgenden Mechanismen sind NICHT SOF-relevant, da sie deterministisch sind:

| Mechanismus-ID | Mechanismus-Name | TSF-ID | Begründung |
|----------------|------------------|--------|------------|
| [TODO] | [TODO] | TSF-[TODO] | [TODO: Warum nicht SOF-relevant?] |

## 4. SOF-Analyse

<!-- 
ANLEITUNG:
Für jeden SOF-relevanten Mechanismus:
1. Beschreibe den Mechanismus im Detail
2. Identifiziere mögliche Angriffsarten
3. Berechne die Angriffsstärke (Erfolgswahrscheinlichkeit)
4. Bewerte das SOF-Level
5. Vergleiche mit dem SOF-Claim
-->

### 4.1 Mechanismus M-1: [TODO: Name]

**Mechanismus-ID:** M-1  
**TSF-ID:** TSF-[TODO]  
**Typ:** [TODO: z.B. Passwort-Authentisierung]

#### 4.1.1 Mechanismus-Beschreibung

[TODO: Beschreibe den Mechanismus im Detail. Beispiel:]

Der Passwort-Authentisierungsmechanismus verwendet:
- Passwortlänge: Minimum [TODO] Zeichen, Maximum [TODO] Zeichen
- Zeichensatz: [TODO: z.B. Groß-/Kleinbuchstaben, Ziffern, Sonderzeichen]
- Passwort-Komplexitätsregeln: [TODO: Beschreibe die Regeln]
- Speicherung: [TODO: z.B. SHA-256 Hash mit Salt]
- Fehlversuch-Handling: [TODO: z.B. Account-Sperre nach X Versuchen]

#### 4.1.2 Angriffsszenarien

**Mögliche Angriffsarten:**

1. **Brute-Force-Angriff**
   - Beschreibung: Systematisches Ausprobieren aller möglichen Passwörter
   - Ressourcen: [TODO: Beschreibe erforderliche Ressourcen]
   - Zeitaufwand: [TODO: Berechne den Zeitaufwand]

2. **Wörterbuch-Angriff**
   - Beschreibung: Ausprobieren häufig verwendeter Passwörter
   - Ressourcen: [TODO: Beschreibe erforderliche Ressourcen]
   - Zeitaufwand: [TODO: Berechne den Zeitaufwand]

3. **Guessing-Angriff**
   - Beschreibung: Erraten von Passwörtern basierend auf Benutzerinformationen
   - Ressourcen: [TODO: Beschreibe erforderliche Ressourcen]
   - Erfolgswahrscheinlichkeit: [TODO: Schätze die Wahrscheinlichkeit]

#### 4.1.3 SOF-Berechnung

**Annahmen:**
- [TODO: Liste alle Annahmen auf, z.B.:]
- Benutzer wählen Passwörter zufällig aus dem erlaubten Zeichensatz
- Angreifer hat keinen Zugriff auf den Passwort-Hash
- Angreifer kann maximal [TODO] Versuche pro Zeiteinheit durchführen

**Berechnung:**

[TODO: Führe die SOF-Berechnung durch. Beispiel:]

**Zeichensatz-Größe:**
- Kleinbuchstaben: 26
- Großbuchstaben: 26
- Ziffern: 10
- Sonderzeichen: 10
- Gesamt: 72 Zeichen

**Passwort-Raum:**
- Minimale Passwortlänge: 8 Zeichen
- Anzahl möglicher Passwörter: 72^8 = 7,22 × 10^14

**Brute-Force-Angriff:**
- Versuche pro Sekunde: [TODO: z.B. 1000]
- Zeit für vollständige Enumeration: 7,22 × 10^14 / 1000 / 86400 / 365 = ca. 22,9 Millionen Jahre
- Erfolgswahrscheinlichkeit nach 1 Jahr: 1 / 22.900.000 ≈ 4,4 × 10^-8

**Account-Sperre:**
- Maximale Fehlversuche: [TODO: z.B. 5]
- Erfolgswahrscheinlichkeit: 5 / 7,22 × 10^14 ≈ 6,9 × 10^-15

**Wörterbuch-Angriff:**
- Größe des Wörterbuchs: [TODO: z.B. 1 Million häufige Passwörter]
- Erfolgswahrscheinlichkeit (ohne Account-Sperre): 1.000.000 / 7,22 × 10^14 ≈ 1,4 × 10^-9
- Erfolgswahrscheinlichkeit (mit Account-Sperre): 5 / 1.000.000 = 5 × 10^-6

#### 4.1.4 SOF-Bewertung

**Ermitteltes SOF-Level:** [TODO: SOF-basic / SOF-medium / SOF-high]

**Begründung:**

[TODO: Begründe das ermittelte SOF-Level. Beispiel:]

Basierend auf der Analyse:
- Brute-Force-Angriffe sind praktisch unmöglich (Erfolgswahrscheinlichkeit < 10^-10)
- Wörterbuch-Angriffe werden durch Account-Sperre effektiv verhindert (Erfolgswahrscheinlichkeit < 10^-5)
- Der Mechanismus bietet Schutz gegen Angreifer mit [TODO: begrenzten/moderaten/hohen] Ressourcen

Das ermittelte SOF-Level ist **SOF-[TODO]**.

**Vergleich mit SOF-Claim:**
- SOF-Claim: SOF-[TODO]
- Ermitteltes SOF: SOF-[TODO]
- Erfüllung: ✓ Ja / ✗ Nein

### 4.2 Mechanismus M-2: [TODO: Name]

**Mechanismus-ID:** M-2  
**TSF-ID:** TSF-[TODO]  
**Typ:** [TODO]

#### 4.2.1 Mechanismus-Beschreibung

[TODO: Beschreibung analog zu 4.1.1]

#### 4.2.2 Angriffsszenarien

[TODO: Analyse analog zu 4.1.2]

#### 4.2.3 SOF-Berechnung

[TODO: Berechnung analog zu 4.1.3]

#### 4.2.4 SOF-Bewertung

[TODO: Bewertung analog zu 4.1.4]

### 4.3 Mechanismus M-3: [TODO: Name]

[TODO: Weitere Mechanismen nach dem gleichen Schema analysieren]

## 5. Zusammenfassung der SOF-Analyse

### 5.1 Übersicht aller Mechanismen

| Mechanismus-ID | Mechanismus-Name | Ermitteltes SOF | SOF-Claim | Erfüllung |
|----------------|------------------|-----------------|-----------|-----------|
| M-1 | [TODO] | SOF-[TODO] | SOF-[TODO] | ✓/✗ |
| M-2 | [TODO] | SOF-[TODO] | SOF-[TODO] | ✓/✗ |
| M-3 | [TODO] | SOF-[TODO] | SOF-[TODO] | ✓/✗ |

### 5.2 Erfüllung des SOF-Claims

**SOF-Claim:** SOF-[TODO]

**Analyse:**

[TODO: Analysiere, ob alle Mechanismen den SOF-Claim erfüllen. Beispiel:]

- Anzahl analysierter Mechanismen: [TODO]
- Anzahl Mechanismen, die SOF-Claim erfüllen: [TODO]
- Anzahl Mechanismen, die SOF-Claim nicht erfüllen: [TODO]

**Ergebnis:**

[TODO: Wähle eine der folgenden Optionen:]

✓ **Alle Mechanismen erfüllen den SOF-Claim**
- Der SOF-Claim von SOF-[TODO] wird von allen analysierten Mechanismen erreicht oder übertroffen.

✗ **Nicht alle Mechanismen erfüllen den SOF-Claim**
- Die folgenden Mechanismen erfüllen den SOF-Claim nicht: [TODO: Liste]
- Maßnahmen: [TODO: Beschreibe geplante Maßnahmen]

### 5.3 Schwächster Mechanismus

**Schwächster Mechanismus:** [TODO: Mechanismus-ID und Name]  
**SOF-Level:** SOF-[TODO]

**Begründung:**
[TODO: Erkläre, warum dieser Mechanismus der schwächste ist und ob dies akzeptabel ist.]

### 5.4 Annahmen und Einschränkungen

**Annahmen:**
[TODO: Liste alle Annahmen auf, die für die SOF-Analyse getroffen wurden. Beispiel:]
- Benutzer wählen Passwörter zufällig
- Angreifer hat keinen physischen Zugriff auf das System
- Angreifer hat keine Insider-Informationen
- [TODO: Weitere Annahmen]

**Einschränkungen:**
[TODO: Liste alle Einschränkungen der Analyse auf. Beispiel:]
- Die Analyse berücksichtigt keine Side-Channel-Angriffe
- Die Analyse berücksichtigt keine Social-Engineering-Angriffe
- [TODO: Weitere Einschränkungen]

## 6. Empfehlungen

### 6.1 Verbesserungsmöglichkeiten

[TODO: Gib Empfehlungen zur Verbesserung der SOF. Beispiel:]

1. **Passwort-Komplexität erhöhen**
   - Aktuelle Mindestlänge: [TODO]
   - Empfohlene Mindestlänge: [TODO]
   - Erwartete SOF-Verbesserung: [TODO]

2. **Multi-Faktor-Authentisierung**
   - Implementierung eines zweiten Faktors (z.B. OTP, Hardware-Token)
   - Erwartete SOF-Verbesserung: [TODO]

3. **Adaptive Authentisierung**
   - Anpassung der Sicherheitsanforderungen basierend auf Risikobewertung
   - Erwartete SOF-Verbesserung: [TODO]

### 6.2 Wartung und Überwachung

[TODO: Beschreibe Maßnahmen zur Aufrechterhaltung der SOF. Beispiel:]

- Regelmäßige Überprüfung der Passwort-Richtlinien
- Monitoring von Authentisierungsversuchen
- Aktualisierung der SOF-Analyse bei Änderungen am TOE
- Berücksichtigung neuer Angriffstechniken

## 7. Zusammenfassung

### 7.1 Ergebnis der SOF-Analyse

Die SOF-Analyse für **[TODO: TOE-Name]** zeigt:

- ✓ Alle probabilistischen Mechanismen wurden identifiziert
- ✓ Alle Mechanismen wurden analysiert
- ✓ SOF-Berechnungen sind dokumentiert
- ✓ SOF-Claim wird erfüllt / ✗ SOF-Claim wird nicht erfüllt

**Gesamtbewertung:** [TODO: Zusammenfassende Bewertung]

### 7.2 Verweis auf weitere Dokumente

Für weitere Informationen siehe:

- **0500_TOE_Summary_Specification.md**: Detaillierte Beschreibung der TSFs
- **0510_Assurance_Measures.md**: AVA_SOF.1 Assurance Measure
- **Kapitel 4 des Security Target**: Definition der SFRs

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [TODO] | [TODO] | Initiale Version |
| 1.0 | [TODO] | [TODO] | [TODO] |

