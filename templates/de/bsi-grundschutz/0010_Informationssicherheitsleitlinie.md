# Informationssicherheitsleitlinie (Top-Management)

**Dokument-ID:** 0010
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
This template provides the top-level information security policy according to BSI IT-Grundschutz.
Customize all [TODO] placeholders based on your organization's specific security strategy.
Reference: BSI Standard 200-1 (ISMS Requirements)
-->

## 1. Zweck und Zielsetzung

Die Informationssicherheitsleitlinie von **{{ meta-organisation.name }}** definiert die strategischen Ziele und Grundsätze für den Schutz von Informationen und IT-Systemen.

### 1.1 Ziel der Informationssicherheit

**{{ meta-organisation.name }}** verpflichtet sich, die Informationssicherheit als integralen Bestandteil der Unternehmensführung zu etablieren. Ziel ist der angemessene Schutz aller Informationswerte vor Bedrohungen und Risiken.

[TODO: Spezifische Sicherheitsziele der Organisation ergänzen]

### 1.2 Schutzwerte

Die Informationssicherheit von **{{ meta-organisation.name }}** basiert auf folgenden Schutzzielen:

- **Vertraulichkeit:** Schutz vor unbefugter Offenlegung von Informationen
- **Integrität:** Schutz vor unbefugter Veränderung von Informationen
- **Verfügbarkeit:** Sicherstellung der Verfügbarkeit von Informationen und Systemen
- **Authentizität:** Sicherstellung der Echtheit und Glaubwürdigkeit von Informationen
- **Nachvollziehbarkeit:** Sicherstellung der Rückverfolgbarkeit von Aktionen

## 2. Geltungsbereich

### 2.1 Organisation und Standorte

Diese Leitlinie gilt für:

- **Organisation:** {{ meta-organisation.name }}
- **Standorte:** [TODO]
- **Geschäftsführung:** {{ meta-organisation-roles.role_CEO }}
- **Informationssicherheitsbeauftragter (ISB):** {{ meta-organisation-roles.role_CISO }}

### 2.2 Informationsverbünde im Scope

[TODO: Definieren Sie die im Scope befindlichen Informationsverbünde]

Beispiele:
- IT-Infrastruktur und Netzwerke
- Geschäftsanwendungen und Datenbanken
- Cloud-Services und externe Dienstleister
- Mobile Endgeräte und Remote-Arbeitsplätze

### 2.3 Ausnahmen

[TODO: Dokumentieren Sie explizite Ausnahmen vom Geltungsbereich]

## 3. Grundsätze

### 3.1 Risikobasierter Ansatz

**{{ meta-organisation.name }}** verfolgt einen risikobasierten Ansatz zur Informationssicherheit gemäß BSI Standard 200-3. Sicherheitsmaßnahmen werden auf Basis einer systematischen Risikoanalyse und -bewertung implementiert.

### 3.2 Verantwortlichkeiten und Ressourcen

Die Geschäftsführung stellt sicher, dass:
- Klare Verantwortlichkeiten für Informationssicherheit definiert sind
- Ausreichende Ressourcen (Personal, Budget, Zeit) bereitgestellt werden
- Informationssicherheit in allen Geschäftsprozessen berücksichtigt wird

### 3.3 Kontinuierliche Verbesserung

Das Informationssicherheits-Managementsystem (ISMS) wird kontinuierlich überwacht, bewertet und verbessert. Regelmäßige Reviews und Audits stellen die Wirksamkeit sicher.

### 3.4 Verpflichtung zur Einhaltung

**{{ meta-organisation.name }}** verpflichtet sich zur Einhaltung:
- Gesetzlicher und regulatorischer Anforderungen (DSGVO, IT-Sicherheitsgesetz, etc.)
- Vertraglicher Verpflichtungen gegenüber Kunden und Partnern
- Interner Richtlinien und Standards
- BSI IT-Grundschutz-Anforderungen

## 4. Verantwortlichkeiten

### 4.1 Top-Management / Geschäftsführung

**Verantwortlich:** {{ meta-organisation-roles.role_CEO }} ([TODO])

Die Geschäftsführung trägt die Gesamtverantwortung für Informationssicherheit und:
- Genehmigt die Informationssicherheitsleitlinie
- Stellt Ressourcen bereit
- Fördert die Sicherheitskultur
- Überwacht die ISMS-Leistung

### 4.2 Informationssicherheitsbeauftragter (ISB)

**Verantwortlich:** {{ meta-organisation-roles.role_CISO }} ([TODO])

Der ISB ist verantwortlich für:
- Koordination des ISMS
- Beratung der Geschäftsführung
- Überwachung der Sicherheitsmaßnahmen
- Durchführung von Risikoanalysen
- Incident Management Koordination

### 4.3 IT-Leitung

**Verantwortlich:** {{ meta-organisation-roles.role_CIO }} ([TODO])

Die IT-Leitung ist verantwortlich für:
- Umsetzung technischer Sicherheitsmaßnahmen
- Betrieb sicherer IT-Systeme
- Patch- und Vulnerability Management
- Technische Incident Response

### 4.4 Informationsverbund-Verantwortliche

[TODO: Definieren Sie Verantwortliche für spezifische Informationsverbünde]

### 4.5 Alle Mitarbeitenden

Alle Mitarbeitenden sind verpflichtet:
- Sicherheitsrichtlinien einzuhalten
- Sicherheitsvorfälle zu melden
- An Schulungen teilzunehmen
- Verantwortungsvoll mit Informationen umzugehen

## 5. Kommunikation und Durchsetzung

### 5.1 Kommunikation der Leitlinie

Diese Leitlinie wird kommuniziert durch:
- Veröffentlichung im Intranet
- Schulungen und Awareness-Programme
- Onboarding neuer Mitarbeitender
- Regelmäßige Erinnerungen und Updates

### 5.2 Konsequenzen bei Verstößen

Verstöße gegen diese Leitlinie können zu folgenden Maßnahmen führen:
- Abmahnung
- Disziplinarische Maßnahmen
- Arbeitsrechtliche Konsequenzen
- Strafrechtliche Verfolgung (bei schwerwiegenden Verstößen)

## 6. Review und Aktualisierung

Diese Leitlinie wird mindestens jährlich oder bei wesentlichen Änderungen überprüft und aktualisiert.

**Nächster Review:** {{ meta-handbook.next_review }}

## 7. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| Geschäftsführung | {{ meta-organisation-roles.role_CEO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| ISB | {{ meta-organisation-roles.role_CISO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**Referenzen:**
- BSI Standard 200-1: Managementsysteme für Informationssicherheit (ISMS)
- BSI Standard 200-2: IT-Grundschutz-Methodik
- BSI Standard 200-3: Risikoanalyse auf der Basis von IT-Grundschutz
- BSI IT-Grundschutz-Kompendium

<!-- End of template -->