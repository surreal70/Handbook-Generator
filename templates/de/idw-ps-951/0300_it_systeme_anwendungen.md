# IT-Systeme und Anwendungen

**Dokument-ID:** idw-ps-951-0300  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument beschreibt die Prüfung der IT-Systeme und Anwendungen im Rahmen der IT-Prüfung nach IDW PS 951.

## 2. Prüfungsgegenstand

### Anwendungslandschaft
- **Kernsysteme:** {{ source.core_systems }}
- **Geschäftsanwendungen:** {{ source.business_applications }}
- **Schnittstellen:** {{ source.interfaces }}

### Prüfungsziele
- Bewertung der Anwendungslandschaft
- Prüfung der Systemarchitektur
- Beurteilung der Anwendungskontrollen
- Bewertung des Schnittstellenmanagements

## 3. Prüfungshandlungen

### Dokumentenprüfung
- [ ] Systemdokumentation vorhanden
- [ ] Anwendungskontrollen dokumentiert
- [ ] Schnittstellenverzeichnis aktuell
- [ ] Datenintegritätskontrollen implementiert

### Kontrolltests
- Überprüfung der Anwendungskontrollen
- Prüfung der Schnittstellenfunktionalität
- Test der Datenintegrität

## 4. Prüfungskriterien

| System | Dokumentiert | Kontrolliert | Getestet | Bewertung |
|--------|--------------|--------------|----------|-----------|
| {{ source.system_1 }} | {{ source.system_1_doc }} | {{ source.system_1_ctrl }} | {{ source.system_1_test }} | {{ source.system_1_assess }} |
| {{ source.system_2 }} | {{ source.system_2_doc }} | {{ source.system_2_ctrl }} | {{ source.system_2_test }} | {{ source.system_2_assess }} |

## 5. Feststellungen

### Positive Feststellungen
1. {{ source.positive_finding_1 }}

### Verbesserungspotenziale
1. {{ source.improvement_1 }}

## 6. Empfehlungen

1. {{ source.recommendation_1 }}

## 7. Referenzen

- IDW PS 951 - IT-Systeme
- ISO/IEC 27001

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
