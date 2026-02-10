# Schutzbedarfsfeststellung (Template)

**Dokument-ID:** 0060  
**Dokumenttyp:** Methodik-Artefakt  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standard 200-2)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template guides the protection requirements determination according to BSI IT-Grundschutz Standard 200-2.
Protection requirements are determined for confidentiality, integrity, and availability.
Reference: BSI Standard 200-2 (Chapter 6: Protection Requirements Determination)
-->

## 1. Ziel und Zweck

Die Schutzbedarfsfeststellung bestimmt systematisch den Schutzbedarf für Geschäftsprozesse, Informationen, Anwendungen und IT-Systeme von **{{ meta.organization.name }}**. Sie bildet die Grundlage für:
- Auswahl angemessener Sicherheitsmaßnahmen
- Priorisierung von Sicherheitsinvestitionen
- Risikoanalyse (Dokument 0090)
- Compliance-Nachweis

**Verantwortlich:** {{ meta.ciso.name }} (ISB)

## 2. Schutzbedarfskategorien und Kriterien

### 2.1 Schutzziele

Die Schutzbedarfsfeststellung erfolgt für folgende Schutzziele:

#### 2.1.1 Vertraulichkeit (Confidentiality)

Schutz vor unbefugter Offenlegung von Informationen.

| Kategorie | Beschreibung | Schadensbeispiele |
|---|---|---|
| **Normal** | Begrenzte negative Auswirkungen | Geringfügige Beeinträchtigung, interne Peinlichkeit |
| **Hoch** | Beträchtliche negative Auswirkungen | Verstoß gegen Gesetze, erheblicher finanzieller Schaden, Reputationsschaden |
| **Sehr hoch** | Existenzbedrohende Auswirkungen | Existenzgefährdung, katastrophaler Reputationsschaden, strafrechtliche Konsequenzen |

#### 2.1.2 Integrität (Integrity)

Schutz vor unbefugter Veränderung von Informationen.

| Kategorie | Beschreibung | Schadensbeispiele |
|---|---|---|
| **Normal** | Begrenzte negative Auswirkungen | Korrigierbare Fehler, geringe Auswirkungen auf Geschäftsprozesse |
| **Hoch** | Beträchtliche negative Auswirkungen | Erhebliche Geschäftsprozess-Störungen, finanzielle Verluste, Compliance-Verstöße |
| **Sehr hoch** | Existenzbedrohende Auswirkungen | Kritische Geschäftsprozess-Ausfälle, existenzbedrohende finanzielle Schäden |

#### 2.1.3 Verfügbarkeit (Availability)

Sicherstellung der Verfügbarkeit von Informationen und Systemen.

| Kategorie | Beschreibung | Tolerierbare Ausfallzeit | Schadensbeispiele |
|---|---|---|---|
| **Normal** | Begrenzte negative Auswirkungen | > 24 Stunden | Geringe Produktivitätsverluste, Unannehmlichkeiten |
| **Hoch** | Beträchtliche negative Auswirkungen | 4-24 Stunden | Erhebliche Produktivitätsverluste, Kundenbeschwerden, finanzielle Verluste |
| **Sehr hoch** | Existenzbedrohende Auswirkungen | < 4 Stunden | Kritische Geschäftsprozess-Ausfälle, massive finanzielle Verluste, Existenzgefährdung |

#### 2.1.4 Authentizität (Optional)

Sicherstellung der Echtheit und Glaubwürdigkeit von Informationen.

| Kategorie | Beschreibung | Schadensbeispiele |
|---|---|---|
| **Normal** | Begrenzte negative Auswirkungen | Geringe Zweifel an Echtheit, korrigierbar |
| **Hoch** | Beträchtliche negative Auswirkungen | Erhebliche rechtliche oder finanzielle Konsequenzen |
| **Sehr hoch** | Existenzbedrohende Auswirkungen | Existenzbedrohende rechtliche oder finanzielle Konsequenzen |

#### 2.1.5 Nachvollziehbarkeit (Optional)

Sicherstellung der Rückverfolgbarkeit von Aktionen.

| Kategorie | Beschreibung | Schadensbeispiele |
|---|---|---|
| **Normal** | Begrenzte negative Auswirkungen | Erschwerte Fehlersuche, geringe Compliance-Risiken |
| **Hoch** | Beträchtliche negative Auswirkungen | Compliance-Verstöße, erschwerte Incident-Aufklärung |
| **Sehr hoch** | Existenzbedrohende Auswirkungen | Schwerwiegende Compliance-Verstöße, unmögliche Incident-Aufklärung |

### 2.2 Bewertungsmaßstab

**Bewertungskriterien:**
- Gesetzliche und regulatorische Anforderungen (DSGVO, IT-Sicherheitsgesetz, etc.)
- Vertragliche Verpflichtungen
- Geschäftskritikalität
- Finanzielle Auswirkungen
- Reputationsrisiken
- Personenbezogene Daten
- Geschäftsgeheimnisse

## 3. Schutzbedarfsfeststellung

### 3.1 Geschäftsprozesse

<!-- 
TEMPLATE AUTHOR NOTE:
Determine protection requirements for all business processes in scope.
Start with business processes, then derive requirements for applications and systems.
-->

| Prozess-ID | Prozess | Owner | C | I | A | Begründung | Schutzbedarf gesamt |
|---|---|---|---|---|---|---|---|
| P-001 | [TODO: Prozess 1] | [TODO] | Normal/Hoch/Sehr hoch | Normal/Hoch/Sehr hoch | Normal/Hoch/Sehr hoch | [TODO: Begründung] | [TODO: Maximum-Prinzip] |
| P-002 | [TODO: Prozess 2] | [TODO] | Normal/Hoch/Sehr hoch | Normal/Hoch/Sehr hoch | Normal/Hoch/Sehr hoch | [TODO] | [TODO] |
| P-003 | [TODO: Prozess 3] | [TODO] | Normal/Hoch/Sehr hoch | Normal/Hoch/Sehr hoch | Normal/Hoch/Sehr hoch | [TODO] | [TODO] |

**Anzahl Prozesse gesamt:** [TODO]  
**Verteilung:**
- Normal: [TODO]
- Hoch: [TODO]
- Sehr hoch: [TODO]

### 3.2 Informationen und Daten

| Info-ID | Information/Datenart | Prozess | C | I | A | Begründung | Schutzbedarf gesamt |
|---|---|---|---|---|---|---|---|
| I-001 | Personenbezogene Daten (DSGVO) | [TODO] | Hoch | Hoch | Normal | DSGVO-Anforderungen | Hoch |
| I-002 | Geschäftsgeheimnisse | [TODO] | Sehr hoch | Hoch | Normal | Wettbewerbsvorteil | Sehr hoch |
| I-003 | Finanzdaten | [TODO] | Hoch | Sehr hoch | Hoch | Gesetzliche Anforderungen | Sehr hoch |
| I-004 | [TODO: Weitere Daten] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl Informationsarten gesamt:** [TODO]

### 3.3 Anwendungen

| Anwendungs-ID | Anwendung | Prozess | C | I | A | Begründung | Schutzbedarf gesamt |
|---|---|---|---|---|---|---|---|
| A-001 | [TODO: Anwendung 1] | P-001 | [TODO] | [TODO] | [TODO] | Vererbung von Prozess P-001 | [TODO] |
| A-002 | [TODO: Anwendung 2] | P-002 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| A-003 | [TODO: Anwendung 3] | P-003 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl Anwendungen gesamt:** [TODO]

### 3.4 IT-Systeme und Komponenten

| System-ID | System/Komponente | Anwendung | C | I | A | Begründung | Schutzbedarf gesamt |
|---|---|---|---|---|---|---|---|
| S-001 | {{ netbox.device.server_001 }} | A-001 | [TODO] | [TODO] | [TODO] | Vererbung von Anwendung A-001 | [TODO] |
| S-002 | [TODO: System 2] | A-002 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| S-003 | [TODO: System 3] | A-003 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl IT-Systeme gesamt:** [TODO]

### 3.5 Netzwerke

| Netz-ID | Netzwerk/Zone | Systeme | C | I | A | Begründung | Schutzbedarf gesamt |
|---|---|---|---|---|---|---|---|
| N-001 | Management-Netz | S-001, S-002 | Sehr hoch | Sehr hoch | Hoch | Kritische Administrationszugriffe | Sehr hoch |
| N-002 | Produktiv-Netz | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| N-003 | DMZ | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl Netzwerke gesamt:** [TODO]

### 3.6 Räume und Standorte

| Raum-ID | Raum/Standort | Systeme | C | I | A | Begründung | Schutzbedarf gesamt |
|---|---|---|---|---|---|---|---|
| R-001 | Rechenzentrum | Alle kritischen Server | Sehr hoch | Sehr hoch | Sehr hoch | Hosting kritischer Systeme | Sehr hoch |
| R-002 | {{ meta.organization.primary_location }} | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Anzahl Räume gesamt:** [TODO]

## 4. Schutzbedarfsvererbung und Abhängigkeiten

### 4.1 Vererbungsprinzip

Der Schutzbedarf wird nach dem **Maximum-Prinzip** vererbt:

```
Geschäftsprozess
    ↓ (vererbt Schutzbedarf)
Informationen
    ↓ (vererbt Schutzbedarf)
Anwendungen
    ↓ (vererbt Schutzbedarf)
IT-Systeme
    ↓ (vererbt Schutzbedarf)
Netzwerke, Räume
```

**Beispiel:**
- Prozess P-001 hat Schutzbedarf "Sehr hoch" für Vertraulichkeit
- Anwendung A-001 unterstützt Prozess P-001
- → Anwendung A-001 erbt Schutzbedarf "Sehr hoch" für Vertraulichkeit
- Server S-001 hostet Anwendung A-001
- → Server S-001 erbt Schutzbedarf "Sehr hoch" für Vertraulichkeit

### 4.2 Vererbungstabelle

| Von (Quelle) | Nach (Ziel) | Vererbter Schutzbedarf | Begründung |
|---|---|---|---|
| P-001 | A-001 | C: Sehr hoch, I: Hoch, A: Hoch | Anwendung unterstützt kritischen Prozess |
| A-001 | S-001 | C: Sehr hoch, I: Hoch, A: Hoch | Server hostet kritische Anwendung |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 4.3 Ausnahmen und Begründungen

**Ausnahmen vom Maximum-Prinzip:**

| Objekt | Erwarteter Schutzbedarf | Tatsächlicher Schutzbedarf | Begründung | Genehmigt von |
|---|---|---|---|---|
| [TODO: Objekt] | [TODO] | [TODO] | [TODO: Begründung für Abweichung] | {{ meta.ciso.name }} |

**Wichtig:** Ausnahmen müssen dokumentiert und genehmigt werden.

### 4.4 Kumulative Effekte

Wenn ein System mehrere Anwendungen mit unterschiedlichem Schutzbedarf hostet, gilt das **Maximum-Prinzip**:

| System | Anwendung 1 | Anwendung 2 | Anwendung 3 | Resultierender Schutzbedarf |
|---|---|---|---|---|
| S-001 | C: Hoch | C: Sehr hoch | C: Normal | C: Sehr hoch (Maximum) |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Validierung und Qualitätssicherung

### 5.1 Validierungsprozess

Die Schutzbedarfsfeststellung wird validiert durch:

1. **Review durch Prozess-Owner:** Bestätigung der Geschäftskritikalität
2. **Review durch IT-Leitung:** {{ meta.cio.name }} - Technische Machbarkeit
3. **Review durch Legal/Compliance:** Gesetzliche Anforderungen
4. **Review durch Datenschutz:** DSGVO-Konformität
5. **Freigabe durch ISB:** {{ meta.ciso.name }}

### 5.2 Konsistenzprüfung

| Prüfkriterium | Status | Bemerkungen |
|---|---|---|
| Alle Prozesse bewertet | [TODO: ✓/✗] | [TODO] |
| Alle Anwendungen bewertet | [TODO: ✓/✗] | [TODO] |
| Alle IT-Systeme bewertet | [TODO: ✓/✗] | [TODO] |
| Vererbung konsistent | [TODO: ✓/✗] | [TODO] |
| Ausnahmen dokumentiert | [TODO: ✓/✗] | [TODO] |
| Begründungen vollständig | [TODO: ✓/✗] | [TODO] |

## 6. Auswirkungen auf Sicherheitsmaßnahmen

### 6.1 Maßnahmen nach Schutzbedarf

| Schutzbedarf | Beispielhafte Maßnahmen |
|---|---|
| **Normal** | Standard-Sicherheitsmaßnahmen, Basis-Härtung, Standard-Backup |
| **Hoch** | Erweiterte Sicherheitsmaßnahmen, Verschlüsselung, MFA, erweiterte Überwachung, redundante Systeme |
| **Sehr hoch** | Maximale Sicherheitsmaßnahmen, Ende-zu-Ende-Verschlüsselung, Hardware-Token, 24/7-Überwachung, Hochverfügbarkeit, Disaster Recovery |

### 6.2 Priorisierung von Maßnahmen

Sicherheitsmaßnahmen werden priorisiert nach:
1. **Sehr hoher Schutzbedarf:** Höchste Priorität
2. **Hoher Schutzbedarf:** Hohe Priorität
3. **Normaler Schutzbedarf:** Normale Priorität

## 7. Dokumentation und Nachweise

Folgende Dokumente und Nachweise werden geführt:
- Dieses Schutzbedarfsfeststellungs-Dokument
- Bewertungsworkshop-Protokolle
- Freigaben der Prozess-Owner
- Ausnahme-Genehmigungen
- Änderungsprotokolle

## 8. Aktualisierung und Pflege

Die Schutzbedarfsfeststellung wird aktualisiert bei:
- Neuen Geschäftsprozessen oder Anwendungen
- Wesentlichen Änderungen an bestehenden Prozessen
- Neuen gesetzlichen Anforderungen
- Sicherheitsvorfällen
- Mindestens jährlich im Rahmen des ISMS-Reviews

**Verantwortlich:** {{ meta.ciso.name }} (ISB)  
**Nächster Review:** {{ meta.document.next_review }}

## 9. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT-Leitung | {{ meta.cio.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| Geschäftsführung | {{ meta.ceo.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**Referenzen:**
- BSI Standard 200-2: IT-Grundschutz-Methodik (Kapitel 6: Schutzbedarfsfeststellung)
- BSI IT-Grundschutz-Kompendium

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->