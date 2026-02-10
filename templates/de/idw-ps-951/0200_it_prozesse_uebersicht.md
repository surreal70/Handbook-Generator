# IT-Prozesse Übersicht

**Dokument-ID:** idw-ps-951-0200  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument beschreibt die Prüfung der IT-Prozesse im Rahmen der IT-Prüfung nach IDW PS 951.

## 2. Prüfungsgegenstand

### IT-Prozesslandschaft
- **Prozessrahmenwerk:** {{ source.process_framework }}
- **Prozessdokumentation:** {{ source.process_documentation }}
- **Prozessverantwortliche:** {{ source.process_owners }}

### Prüfungsziele
- Bewertung der IT-Prozesslandschaft
- Prüfung der Prozessdokumentation
- Beurteilung der Prozesskontrollen
- Bewertung der Prozessreife

## 3. Prüfungshandlungen

### Dokumentenprüfung
- [ ] Prozessdokumentation vorhanden
- [ ] Prozessverantwortlichkeiten definiert
- [ ] Prozesskontrollen implementiert
- [ ] Prozess-KPIs definiert

### Kontrolltests
- Überprüfung der Prozessausführung
- Prüfung der Kontrollwirksamkeit
- Bewertung der Prozessreife

## 4. Prüfungskriterien

| Prozess | Dokumentiert | Kontrolliert | Gemessen | Bewertung |
|---------|--------------|--------------|----------|-----------|
| Change Management | {{ source.change_documented }} | {{ source.change_controlled }} | {{ source.change_measured }} | {{ source.change_assessment }} |
| Incident Management | {{ source.incident_documented }} | {{ source.incident_controlled }} | {{ source.incident_measured }} | {{ source.incident_assessment }} |
| Problem Management | {{ source.problem_documented }} | {{ source.problem_controlled }} | {{ source.problem_measured }} | {{ source.problem_assessment }} |

## 5. Feststellungen

### Positive Feststellungen
1. {{ source.positive_finding_1 }}

### Verbesserungspotenziale
1. {{ source.improvement_1 }}

## 6. Empfehlungen

1. {{ source.recommendation_1 }}

## 7. Referenzen

- IDW PS 951 - IT-Prozesse
- ITIL 4
- COBIT 2019

---

**Genehmigt durch:**  
{{ meta.audit_lead }}, Prüfungsleiter  
Datum: {{ meta.approval_date }}

**Nächster Review:** {{ meta.next_review }}

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |
