# Metadaten: Common Criteria Security Target

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

## Handbuch-Informationen

**Handbuch-Titel:** Common Criteria Security Target (ISO/IEC 15408)  
**Organisation:** {{ meta.organization }}  
**Autor:** Andreas Huemmer [andreas.huemmer@adminsend.de]  
**Erstellungsdatum:** {{ meta.date }}  
**Version:** {{ meta.version }}  
**Geltungsbereich:** {{ meta.scope }}  

---

## Zweck

Dieses Security Target (ST) dokumentiert die Sicherheitseigenschaften des Target of Evaluation (TOE) gemäß ISO/IEC 15408 (Common Criteria for Information Technology Security Evaluation). Es beschreibt die Sicherheitsfunktionen, Sicherheitsziele und Sicherheitsanforderungen des TOE sowie die Evaluierungsstufe (Evaluation Assurance Level, EAL).

## Zielgruppe

- Evaluatoren und Zertifizierungsstellen
- Produktentwickler und Sicherheitsarchitekten
- Kunden und Beschaffer sicherheitskritischer IT-Produkte
- Auditoren und Compliance-Verantwortliche

## Dokumentenstruktur

Das Security Target folgt der Struktur von ISO/IEC 15408-1:2022 und umfasst:

1. **ST Introduction** - Einführung, TOE-Übersicht, Konformitätsansprüche
2. **TOE Description** - Detaillierte Beschreibung des Evaluierungsgegenstands
3. **Security Problem Definition** - Bedrohungen, organisatorische Sicherheitspolitiken, Annahmen
4. **Security Objectives** - Sicherheitsziele für TOE und Umgebung
5. **Security Requirements** - Funktionale und Vertrauenswürdigkeitsanforderungen (SFR, SAR)
6. **TOE Summary Specification** - Zusammenfassung der Sicherheitsfunktionen
7. **Appendices** - PP-Konformität, Rationale, Glossar

## Hinweise zur Verwendung

- Alle `[TODO]`-Platzhalter müssen durch spezifische Informationen ersetzt werden
- Platzhalter im Format `{{ source.field }}` werden automatisch aus Datenquellen befüllt
- Diagramme können im Unterordner `diagrams/` abgelegt werden
- Das ST muss konsistent mit dem gewählten Protection Profile (PP) sein
- Alle Sicherheitsanforderungen müssen aus ISO/IEC 15408-2 und 15408-3 stammen

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| {{ meta.version }} | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initiale Version |
