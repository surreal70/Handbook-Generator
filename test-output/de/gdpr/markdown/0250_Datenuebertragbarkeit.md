# Datenübertragbarkeit

**Dokument-ID:** 0250
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

Dieses Dokument beschreibt die Umsetzung des Rechts auf Datenübertragbarkeit in der AdminSend GmbH. Betroffene Personen haben das Recht, ihre Daten in einem strukturierten, gängigen und maschinenlesbaren Format zu erhalten.

## Recht auf Datenübertragbarkeit (Art. 20)

### Voraussetzungen

**Datenübertragbarkeit gilt nur, wenn:**

| Voraussetzung | Beschreibung |
|---------------|--------------|
| Rechtsgrundlage | Einwilligung (Art. 6 Abs. 1 lit. a) oder Vertrag (Art. 6 Abs. 1 lit. b) |
| Bereitstellung | Daten wurden von betroffener Person bereitgestellt |
| Automatisierte Verarbeitung | Verarbeitung erfolgt automatisiert |

**Nicht anwendbar bei:**
- Verarbeitung aufgrund anderer Rechtsgrundlagen (lit. c, d, e, f)
- Nicht automatisierte Verarbeitung
- Daten, die nicht von betroffener Person bereitgestellt wurden

### Umfang der Datenübertragbarkeit

**Betroffene Daten:**

| Datenart | Übertragbar? | Begründung |
|----------|--------------|------------|
| Von Person bereitgestellt | Ja | Direkt eingegeben oder hochgeladen |
| Durch Beobachtung generiert | Ja | Nutzungsdaten, Standortdaten |
| Abgeleitete/berechnete Daten | Nein | Algorithmen, Analysen, Profile |
| Daten Dritter | Nein | Rechte Dritter betroffen |

### Zwei Varianten

**1. Übertragung an betroffene Person:**
- Bereitstellung in strukturiertem Format
- Gängiges Format (CSV, JSON, XML)
- Maschinenlesbar

**2. Direkte Übertragung an anderen Verantwortlichen:**
- Soweit technisch machbar
- Direkte Übermittlung
- Keine Verpflichtung bei fehlender Schnittstelle

## Technische Umsetzung

### Datenformate

**Unterstützte Formate:**

| Format | Beschreibung | Anwendungsfall |
|--------|--------------|----------------|
| [TODO: JSON] | JavaScript Object Notation | Standard für strukturierte Daten |
| [TODO: CSV] | Comma-Separated Values | Tabellarische Daten |
| [TODO: XML] | Extensible Markup Language | Hierarchische Daten |
| [TODO: PDF] | Portable Document Format | Lesbare Darstellung (zusätzlich) |

### Datenstruktur

**Beispiel JSON-Struktur:**

```json
{
  "export_date": "2024-01-15",
  "data_subject": {
    "id": "12345",
    "name": "Max Mustermann",
    "email": "max@example.com"
  },
  "personal_data": {
    "profile": {
      "created": "2020-01-01",
      "last_updated": "2024-01-10",
      "fields": {
        "name": "Max Mustermann",
        "email": "max@example.com",
        "phone": "+49123456789"
      }
    },
    "orders": [
      {
        "order_id": "ORD-001",
        "date": "2023-12-01",
        "items": [...]
      }
    ],
    "usage_data": {
      "logins": [...],
      "page_views": [...]
    }
  }
}
```

### Schnittstellen

**Technische Übertragungsmöglichkeiten:**

| Methode | Beschreibung | Implementierung |
|---------|--------------|-----------------|
| [TODO: Download-Portal] | Selbstbedienungsportal | Web-Interface |
| [TODO: API] | Programmatische Schnittstelle | REST API |
| [TODO: E-Mail] | Versand als Anhang | Verschlüsselt |
| [TODO: Direkte Übertragung] | An anderen Verantwortlichen | API-to-API |

## Übertragungsprozess

### Prozess für Datenübertragbarkeitsanfragen

**Standardprozess:**

1. **Eingang der Anfrage (Tag 0)**
   - Registrierung
   - Eingangsbestätigung
   - Klärung: An Person oder anderen Verantwortlichen?

2. **Prüfung (Tag 1-10)**
   - Identifikation der betroffenen Person
   - Prüfung der Voraussetzungen
   - Identifikation übertragbarer Daten

3. **Datenexport (Tag 11-20)**
   - Zusammenstellung der Daten
   - Konvertierung in gewünschtes Format
   - Qualitätsprüfung

4. **Übertragung (Tag 21-25)**
   - Bereitstellung zum Download oder
   - Direkte Übertragung an anderen Verantwortlichen
   - Dokumentation

5. **Rückmeldung (Tag 26-30)**
   - Information über Bereitstellung
   - Zugangslink oder Bestätigung der Übertragung

### Direkte Übertragung

**Prozess für direkte Übertragung:**

1. **Identifikation des Empfängers**
   - Name und Kontaktdaten
   - Technische Schnittstelle

2. **Prüfung der technischen Machbarkeit**
   - Verfügbarkeit von Schnittstellen
   - Kompatibilität der Formate

3. **Durchführung der Übertragung**
   - Sichere Übermittlung
   - Bestätigung des Empfangs
   - Dokumentation

**Bei fehlender technischer Machbarkeit:**
- Bereitstellung an betroffene Person
- Information über fehlende Schnittstelle

## Ausnahmen und Einschränkungen

### Rechte und Freiheiten Dritter (Art. 20 Abs. 4)

**Datenübertragbarkeit darf nicht beeinträchtigen:**
- Rechte und Freiheiten anderer Personen
- Geschäftsgeheimnisse
- Geistiges Eigentum

**Maßnahmen:**
- Anonymisierung von Drittdaten
- Ausschluss geschützter Informationen
- Begründung bei Einschränkung

### Keine Löschpflicht

**Datenübertragbarkeit bedeutet nicht:**
- Automatische Löschung beim Verantwortlichen
- Beendigung der Verarbeitung
- Separate Löschanfrage erforderlich

## Dokumentation

### Datenübertragbarkeitsregister

| Datum | Betroffene Person | Format | Empfänger | Umfang | Status | Bearbeiter |
|-------|------------------|--------|-----------|--------|--------|------------|
| [TODO] | [TODO] | JSON | Betroffene Person | Vollständig | Bereitgestellt | [TODO] |
| [TODO] | [TODO] | CSV | Anderer Verantwortlicher | Vollständig | Übertragen | [TODO] |
| [TODO] | [TODO] | JSON | Betroffene Person | Teilweise (Drittrechte) | Bereitgestellt | [TODO] |

### Nachweispflichten

**Dokumentation für Accountability:**
- Alle Datenübertragbarkeitsanfragen
- Bereitgestellte Daten und Formate
- Direkte Übertragungen
- Einschränkungen und deren Begründung
- Technische Machbarkeitsprüfungen

## Fristen

**Bearbeitungsfrist:**
- Unverzüglich, spätestens 1 Monat
- Verlängerung um 2 Monate bei Komplexität möglich
- Begründung der Verlängerung erforderlich

## Verknüpfung zu anderen Dokumenten

- **Transparenz (Art. 12):** Modalitäten der Übertragung
- **Rechtsgrundlagen (Art. 6):** Voraussetzungen für Übertragbarkeit
- **Informationspflichten (Art. 13-14):** Information über Recht
- **Auskunftsrecht (Art. 15):** Ergänzendes Recht

## Häufige Verstöße und deren Vermeidung

| Verstoß | Beispiel | Vermeidung |
|---------|----------|------------|
| Unstrukturiertes Format | PDF-Scan | Maschinenlesbares Format |
| Unvollständige Daten | Nur Stammdaten | Alle übertragbaren Daten |
| Fehlende Schnittstelle | Keine direkte Übertragung | API bereitstellen |
| Verzögerte Bereitstellung | Bereitstellung nach 3 Monaten | Fristenkontrolle |

**Nächste Schritte:**
1. Etablieren Sie Prozess für Datenübertragbarkeitsanfragen
2. Implementieren Sie Export in strukturierten Formaten
3. Entwickeln Sie Schnittstellen für direkte Übertragung
4. Schulen Sie Mitarbeiter zu Datenübertragbarkeit
5. Dokumentieren Sie alle Anfragen im Register

