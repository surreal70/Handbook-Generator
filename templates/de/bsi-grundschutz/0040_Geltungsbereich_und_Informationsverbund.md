# Geltungsbereich und Informationsverbund (Abgrenzung)

**Dokument-ID:** 0040
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the scope and information domain boundaries according to BSI IT-Grundschutz.
Customize all [TODO] placeholders based on your organization's specific scope.
Reference: BSI Standard 200-2 (Scope Definition and Information Domain)
-->

## 1. Zweck und Zielsetzung

Dieses Dokument definiert den Geltungsbereich des Informationssicherheits-Managementsystems (ISMS) von **{{ meta-organisation.name }}** und grenzt den Informationsverbund ab. Die klare Definition des Scopes ist Grundlage für alle weiteren IT-Grundschutz-Aktivitäten (Strukturanalyse, Schutzbedarfsfeststellung, Modellierung).

## 2. Scope-Definition

### 2.1 Organisationseinheiten und Standorte

**Organisation:** {{ meta-organisation.name }}

**Standorte im Scope:**

| Standort | Adresse | Typ | Mitarbeitende | Im Scope |
|---|---|---|---|---|
| [TODO] | [TODO] | Hauptstandort | [TODO] | ✓ |
| [TODO: Weitere Standorte] | [TODO] | [TODO] | [TODO] | ✓/✗ |

**Organisationseinheiten im Scope:**
- Geschäftsführung
- IT-Abteilung
- [TODO: Weitere Abteilungen]

### 2.2 Geschäftsprozesse und Services

**Kritische Geschäftsprozesse im Scope:**

| Prozess | Beschreibung | Kritikalität | Owner | Im Scope |
|---|---|---|---|---|
| [TODO: Prozess 1] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | ✓ |
| [TODO: Prozess 2] | [TODO] | Hoch/Mittel/Niedrig | [TODO] | ✓ |

**IT-Services im Scope:**

| Service | Beschreibung | Nutzer | Service Owner | Im Scope |
|---|---|---|---|---|
| [TODO: Service 1] | [TODO] | [TODO] | {{ meta.cio.name }} | ✓ |
| [TODO: Service 2] | [TODO] | [TODO] | {{ meta.cio.name }} | ✓ |

### 2.3 IT-Infrastruktur

**IT-Systeme im Scope:**

#### 2.3.1 On-Premise IT

| Kategorie | Systeme | Anzahl | Im Scope |
|---|---|---|---|
| Server | {{ netbox.device.servers }} | [TODO] | ✓ |
| Netzwerk | {{ netbox.device.network }} | [TODO] | ✓ |
| Storage | {{ netbox.device.storage }} | [TODO] | ✓ |
| Clients | Workstations, Laptops | [TODO] | ✓ |
| Mobile Devices | Smartphones, Tablets | [TODO] | ✓ |

#### 2.3.2 Cloud-Services

| Cloud-Service | Provider | Typ (IaaS/PaaS/SaaS) | Im Scope |
|---|---|---|---|
| [TODO: Cloud Service 1] | [TODO] | [TODO] | ✓ |
| [TODO: Cloud Service 2] | [TODO] | [TODO] | ✓ |

#### 2.3.3 OT/IoT (falls zutreffend)

| OT/IoT-System | Beschreibung | Standort | Im Scope |
|---|---|---|---|
| [TODO: OT System 1] | [TODO] | [TODO] | ✓/✗ |

### 2.4 Anwendungen und Daten

**Geschäftsanwendungen im Scope:**

| Anwendung | Typ | Kritikalität | Datenklassifizierung | Im Scope |
|---|---|---|---|---|
| [TODO: Anwendung 1] | [TODO] | Hoch/Mittel/Niedrig | Vertraulich/Intern | ✓ |
| [TODO: Anwendung 2] | [TODO] | Hoch/Mittel/Niedrig | Vertraulich/Intern | ✓ |

**Datenarten im Scope:**
- Personenbezogene Daten (DSGVO-relevant)
- Geschäftsgeheimnisse
- Kundendaten
- Finanzdaten
- [TODO: Weitere Datenarten]

## 3. Abgrenzung des Informationsverbunds

### 3.1 In Scope

**Folgende Elemente sind im Scope des ISMS:**

1. **Infrastruktur:**
   - Alle Server und Netzwerkkomponenten an Standort [TODO]
   - [TODO: Weitere Infrastruktur]

2. **Anwendungen:**
   - Alle geschäftskritischen Anwendungen
   - [TODO: Spezifische Anwendungen]

3. **Daten:**
   - Alle personenbezogenen Daten
   - Alle Geschäftsdaten mit Klassifizierung "Vertraulich" oder höher
   - [TODO: Weitere Daten]

4. **Personen:**
   - Alle Mitarbeitenden von {{ meta-organisation.name }}
   - Externe Dienstleister mit Zugriff auf Scope-Systeme
   - [TODO: Weitere Personengruppen]

5. **Prozesse:**
   - Alle IT-Betriebsprozesse
   - Alle geschäftskritischen Prozesse
   - [TODO: Weitere Prozesse]

### 3.2 Out of Scope

**Folgende Elemente sind NICHT im Scope des ISMS:**

| Element | Begründung | Risikobewertung | Schnittstellen zum Scope |
|---|---|---|---|
| [TODO: Out-of-Scope Element 1] | [TODO: Begründung] | [TODO: Risiko] | [TODO: Schnittstellen] |
| [TODO: Out-of-Scope Element 2] | [TODO: Begründung] | [TODO: Risiko] | [TODO: Schnittstellen] |

**Wichtig:** Auch Out-of-Scope-Elemente müssen hinsichtlich ihrer Risiken für den Scope bewertet werden, insbesondere wenn Schnittstellen bestehen.

### 3.3 Begründung der Abgrenzung

[TODO: Erläutern Sie die Gründe für die gewählte Scope-Abgrenzung]

Beispiele für Begründungen:
- Fokus auf kritische Geschäftsprozesse
- Ressourcenbeschränkungen (schrittweise Erweiterung geplant)
- Externe Verantwortung (z.B. ausgelagerte Prozesse)
- Geringe Kritikalität

## 4. Schnittstellen und Abhängigkeiten

### 4.1 Externe Dienstleister und Provider

| Dienstleister | Service | Kritikalität | Vertragliche Regelungen | Sicherheitsanforderungen |
|---|---|---|---|---|
| [TODO: Provider 1] | [TODO] | Hoch/Mittel/Niedrig | [TODO: Vertrag vorhanden] | [TODO: SLA, Zertifizierungen] |
| [TODO: Provider 2] | [TODO] | Hoch/Mittel/Niedrig | [TODO: Vertrag vorhanden] | [TODO: SLA, Zertifizierungen] |

### 4.2 Kritische Schnittstellen

**Schnittstellen zwischen Scope und Out-of-Scope:**

| Schnittstelle | Von (Scope) | Nach (Out-of-Scope) | Datenfluss | Sicherheitsmaßnahmen |
|---|---|---|---|---|
| [TODO: Schnittstelle 1] | [TODO] | [TODO] | [TODO] | [TODO: Verschlüsselung, Firewall, etc.] |
| [TODO: Schnittstelle 2] | [TODO] | [TODO] | [TODO] | [TODO] |

**Schnittstellen zu externen Partnern:**

| Partner | Zweck | Datenarten | Sicherheitsmaßnahmen |
|---|---|---|---|
| [TODO: Partner 1] | [TODO] | [TODO] | [TODO] |
| [TODO: Partner 2] | [TODO] | [TODO] | [TODO] |

### 4.3 Abhängigkeiten

**Kritische Abhängigkeiten des Scopes:**

| Abhängigkeit | Typ | Auswirkung bei Ausfall | Mitigationsmaßnahmen |
|---|---|---|---|
| Internetanbindung | Externe Infrastruktur | [TODO] | [TODO: Redundanz, Backup-Leitung] |
| Stromversorgung | Externe Infrastruktur | [TODO] | [TODO: USV, Notstrom] |
| [TODO: Weitere Abhängigkeiten] | [TODO] | [TODO] | [TODO] |

## 5. Informationsverbund-Diagramm

<!-- 
TEMPLATE AUTHOR NOTE:
Create a diagram showing the information domain boundaries, main components, and interfaces.
Save as: diagrams/informationsverbund.png
-->

![Informationsverbund-Diagramm](diagrams/informationsverbund.png)

**Diagramm-Legende:**
- **Grüne Linie:** Scope-Grenze (im ISMS)
- **Rote Linie:** Out-of-Scope-Grenze
- **Blaue Pfeile:** Datenflüsse
- **Gelbe Symbole:** Kritische Schnittstellen

[TODO: Erstellen Sie ein Diagramm des Informationsverbunds]

## 6. Scope-Änderungen

### 6.1 Änderungsprozess

Änderungen am Scope erfordern:
1. **Antrag:** Formaler Änderungsantrag an ISB
2. **Bewertung:** Bewertung der Auswirkungen (Risiken, Ressourcen, Compliance)
3. **Genehmigung:** Genehmigung durch Geschäftsführung
4. **Umsetzung:** Aktualisierung aller betroffenen Dokumente
5. **Kommunikation:** Information aller Stakeholder

**Verantwortlich:** {{ meta.ciso.name }} (ISB)

### 6.2 Scope-Review

Der Scope wird regelmäßig überprüft:
- **Frequenz:** Jährlich oder bei wesentlichen Änderungen
- **Trigger:** Neue Geschäftsprozesse, IT-Systeme, Standorte, regulatorische Anforderungen
- **Verantwortlich:** ISB

**Nächster Review:** {{ meta-handbook.next_review }}

## 7. Dokumentation und Nachweise

Folgende Dokumente und Nachweise werden für den Scope geführt:
- Dieses Scope-Dokument
- Informationsverbund-Diagramm
- Asset-Inventar (siehe Anhang 0710)
- Datenfluss-Diagramme (siehe Anhang 0720)
- Verträge mit externen Dienstleistern
- Scope-Änderungsprotokolle

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| Geschäftsführung | {{ meta.ceo.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| ISB | {{ meta.ciso.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**Referenzen:**
- BSI Standard 200-1: Managementsysteme für Informationssicherheit (ISMS)
- BSI Standard 200-2: IT-Grundschutz-Methodik (Kapitel 4: Festlegung des Geltungsbereichs)
- BSI IT-Grundschutz-Kompendium

<!-- End of template -->