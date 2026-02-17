# Service- und Prozesskatalog mit Kritikalität

**Dokument-ID:** BCM-0060
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents the service and process catalog with criticality assessment.
It serves as the foundation for BIA, strategies, and BCM plans.

Customization required:
- List all business-critical services and processes
- Assign owners and criticality levels
- Document dependencies
- Identify stakeholders
-->

## 1. Ziel

Dieses Dokument dokumentiert alle im BCM betrachteten Services und Geschäftsprozesse der {{ meta-organisation.name }} inklusive:

- **Kritikalitätsbewertung:** Einstufung nach Geschäftskritikalität (Hoch/Mittel/Niedrig)
- **Ownership:** Klare Zuordnung von Verantwortlichkeiten
- **Abhängigkeiten:** Identifikation kritischer Abhängigkeiten
- **Stakeholder:** Betroffene Kunden und interne/externe Stakeholder

Der Service- und Prozesskatalog bildet die Grundlage für:
- Business Impact Analysis (BIA)
- BCM-Strategien und Kontinuitätsoptionen
- Business Continuity Pläne (BCP)
- IT Disaster Recovery Pläne (DRP)

## 2. Service- und Prozesskatalog

### 2.1 Geschäftskritische Services (Kritikalität: HOCH)

| Service/Prozess | Owner | Beschreibung | Top 5 Abhängigkeiten | Kunden/Stakeholder |
|-----------------|-------|--------------|----------------------|-------------------|
| [TODO: Service 1] | [TODO: Owner] | [TODO: Beschreibung] | [TODO: 1. IT-System, 2. Lieferant, 3. Personal, 4. Standort, 5. Daten] | [TODO: Externe Kunden, Partner] |
| [TODO: Service 2] | [TODO: Owner] | [TODO: Beschreibung] | [TODO: Abhängigkeiten] | [TODO: Stakeholder] |

**Beispiele für geschäftskritische Services:**
- Kundenservice und Support (24/7)
- Produktionssteuerung und -durchführung
- Auftragsabwicklung und Logistik
- Zahlungsverkehr und Finanzprozesse
- E-Commerce-Plattform

### 2.2 Wichtige Services (Kritikalität: MITTEL)

| Service/Prozess | Owner | Beschreibung | Top 5 Abhängigkeiten | Kunden/Stakeholder |
|-----------------|-------|--------------|----------------------|-------------------|
| [TODO: Service 1] | [TODO: Owner] | [TODO: Beschreibung] | [TODO: Abhängigkeiten] | [TODO: Stakeholder] |

**Beispiele für wichtige Services:**
- Personalverwaltung und HR-Prozesse
- Einkauf und Beschaffung
- Marketing und Vertrieb (nicht zeitkritisch)
- Controlling und Reporting
- Qualitätsmanagement

### 2.3 Unterstützende Services (Kritikalität: NIEDRIG)

| Service/Prozess | Owner | Beschreibung | Top 5 Abhängigkeiten | Kunden/Stakeholder |
|-----------------|-------|--------------|----------------------|-------------------|
| [TODO: Service 1] | [TODO: Owner] | [TODO: Beschreibung] | [TODO: Abhängigkeiten] | [TODO: Stakeholder] |

**Beispiele für unterstützende Services:**
- Entwicklungsumgebungen
- Schulungs- und Trainingsplattformen
- Archivierung und Dokumentenmanagement
- Interne Kommunikationstools (nicht zeitkritisch)

## 3. Kriterien zur Kritikalitätsbewertung

### 3.1 Bewertungsdimensionen

Die Kritikalität wird anhand folgender Dimensionen bewertet:

**1. Finanzieller Impact**
- Direkter Umsatzverlust pro Stunde/Tag
- Vertragsstrafen und Schadensersatzforderungen
- Zusätzliche Kosten für Notfallmaßnahmen

**2. Operativer Impact**
- Beeinträchtigung anderer Geschäftsprozesse
- Produktionsausfall oder Qualitätsprobleme
- Rückstau und Nacharbeitsaufwand

**3. Rechtliche und regulatorische Anforderungen**
- Gesetzliche Verpflichtungen und Compliance
- Vertragliche Verpflichtungen (SLAs)
- Meldepflichten gegenüber Behörden

**4. Sicherheit**
- Gefährdung von Menschenleben
- Umweltgefährdung
- Anlagensicherheit

**5. Reputation und Vertrauen**
- Kundenvertrauen und Kundenzufriedenheit
- Markenimage und öffentliche Wahrnehmung
- Vertrauen von Partnern und Investoren

### 3.2 Bewertungslogik und Scoring

[TODO: Definieren Sie Ihre Bewertungslogik]

**Beispiel-Scoring:**

| Kritikalität | Finanzieller Impact | Operativer Impact | Rechtlicher Impact | Sicherheits-Impact | Reputations-Impact |
|--------------|---------------------|-------------------|-------------------|-------------------|-------------------|
| **HOCH** | > 50.000 €/Tag | Mehrere Prozesse betroffen | Gesetzesverstoß | Personengefährdung | Massive Medienberichterstattung |
| **MITTEL** | 10.000-50.000 €/Tag | Ein Prozess betroffen | Vertragsverletzung | Sachschaden | Kundenbeschwerden |
| **NIEDRIG** | < 10.000 €/Tag | Keine Auswirkung | Keine Verpflichtung | Kein Schaden | Keine Auswirkung |

**Gesamtbewertung:**
- Wenn mindestens eine Dimension "HOCH" → Gesamtkritikalität: **HOCH**
- Wenn mindestens zwei Dimensionen "MITTEL" → Gesamtkritikalität: **MITTEL**
- Sonst → Gesamtkritikalität: **NIEDRIG**

### 3.3 Kritikalitätsmatrix

```
Impact
  │
H │  [Service A]  [Service B]
  │  [Service C]
  │
M │              [Service D]
  │  [Service E]
  │
L │              [Service F]  [Service G]
  │
  └─────────────────────────────────────
    L           M           H
              Wahrscheinlichkeit
```

[TODO: Ordnen Sie Ihre Services in die Matrix ein]

## 4. IT-Services und Systeme

### 4.1 Kritische IT-Services

| IT-Service | Unterstützte Geschäftsprozesse | Kritikalität | IT-Owner | Technologie |
|------------|-------------------------------|--------------|----------|-------------|
| [TODO: ERP-System] | Auftragsabwicklung, Finanzen, Produktion | HOCH | {{ meta-organisation-roles.role_IT_Manager }} | [TODO: SAP/Oracle/etc.] |
| [TODO: E-Mail] | Alle Geschäftsprozesse | HOCH | {{ meta-organisation-roles.role_IT_Manager }} | [TODO: Exchange/M365/etc.] |
| [TODO: CRM] | Vertrieb, Kundenservice | MITTEL | [TODO] | [TODO: Salesforce/etc.] |

### 4.2 IT-Infrastruktur

| Infrastruktur-Komponente | Abhängige Services | Kritikalität | Standort | Redundanz |
|--------------------------|-------------------|--------------|----------|-----------|
| [TODO: Core Switch] | Alle IT-Services | HOCH | [TODO] | Ja/Nein |
| [TODO: Firewall] | Internet-Zugang | HOCH | [TODO] | Ja/Nein |
| [TODO: Storage] | Alle Daten | HOCH | [TODO] | Ja/Nein |

## 5. Abhängigkeitsanalyse

### 5.1 Abhängigkeitstypen

**People (Personal):**
- Schlüsselpersonen und Spezialwissen
- Mindestbesetzung für Betrieb
- Externe Dienstleister

**Facilities (Standorte und Räumlichkeiten):**
- Bürogebäude und Produktionsstätten
- Rechenzentren
- Lager und Logistikzentren

**Technology (IT-Systeme und Technologie):**
- Geschäftsanwendungen (ERP, CRM, etc.)
- IT-Infrastruktur (Netzwerk, Server, Storage)
- Cloud-Services

**Information (Daten und Informationen):**
- Geschäftsdaten und Kundendaten
- Konfigurationsdaten
- Dokumentation und Wissen

**Suppliers (Lieferanten und Partner):**
- Kritische Zulieferer
- IT-Dienstleister und Cloud-Provider
- Logistikpartner

### 5.2 Abhängigkeitsmatrix (Beispiel)

[TODO: Erstellen Sie eine Abhängigkeitsmatrix für Ihre kritischen Services]

**Beispiel für Service "Auftragsabwicklung":**

| Abhängigkeitstyp | Konkrete Abhängigkeit | Kritikalität | Ausweichmöglichkeit |
|------------------|----------------------|--------------|---------------------|
| People | Auftragsbearbeiter (mind. 3) | HOCH | Schulung von Backup-Personal |
| Facilities | Bürostandort Hauptsitz | MITTEL | Home-Office möglich |
| Technology | ERP-System | HOCH | Keine (Single Point of Failure) |
| Information | Auftragsdatenbank | HOCH | Backup vorhanden |
| Suppliers | Logistikdienstleister | HOCH | Alternativdienstleister verfügbar |

## 6. Stakeholder-Übersicht

### 6.1 Interne Stakeholder

| Stakeholder-Gruppe | Betroffene Services | Kommunikationsbedarf | Ansprechpartner |
|-------------------|-------------------|---------------------|-----------------|
| Geschäftsführung | Alle kritischen Services | Strategische Entscheidungen | {{ meta-organisation-roles.role_CEO }} |
| IT-Abteilung | Alle IT-abhängigen Services | Technische Koordination | {{ meta-organisation-roles.role_CIO }} |
| Fachbereiche | Jeweilige Services | Operative Umsetzung | [TODO: Bereichsleiter] |
| Mitarbeiter | Alle Services | Information und Anweisungen | [TODO: HR/Kommunikation] |

### 6.2 Externe Stakeholder

| Stakeholder-Gruppe | Betroffene Services | Kommunikationsbedarf | Ansprechpartner |
|-------------------|-------------------|---------------------|-----------------|
| Kunden | Kundenservice, Produktion, Lieferung | Statusupdates, Alternativlösungen | [TODO: Kundenservice] |
| Lieferanten | Beschaffung, Produktion | Koordination, Anpassungen | [TODO: Einkauf] |
| Partner | Gemeinsame Services | Abstimmung, Koordination | [TODO: Partnerverantwortlicher] |
| Behörden | Regulierte Services | Meldungen, Nachweise | [TODO: Compliance] |
| Medien | Alle Services (bei Krise) | Pressemitteilungen | [TODO: PR/Kommunikation] |

## 7. Pflege und Aktualisierung

**Verantwortlich:** BCM-Manager

**Aktualisierungsintervall:**
- Jährliche Überprüfung aller Services und Kritikalitätsbewertungen
- Ad-hoc bei organisatorischen Änderungen (neue Services, Prozessänderungen)
- Nach BIA-Durchführung

**Review-Prozess:**
1. BCM-Manager initiiert Review
2. Service-Owner prüfen und aktualisieren ihre Services
3. Kritikalitätsbewertung wird validiert
4. Änderungen werden dokumentiert und kommuniziert

<!-- End of template -->
