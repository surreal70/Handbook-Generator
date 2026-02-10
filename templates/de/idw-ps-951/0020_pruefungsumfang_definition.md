# Prüfungsumfang und Scope-Definition

**Dokument-ID:** idw-ps-951-0020  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument definiert den Umfang der IT-Prüfung und legt fest, welche IT-Systeme, Prozesse und Kontrollen im Rahmen der Prüfung nach IDW PS 951 untersucht werden.

## 2. Scope-Definition

### Organisatorischer Scope
- **Geprüfte Organisationseinheiten:** {{ source.audited_units }}
- **Standorte:** {{ source.audited_locations }}
- **Geschäftsbereiche:** {{ source.business_areas }}

### Technischer Scope

#### IT-Systeme im Scope
| System | Beschreibung | Kritikalität | Prüfungstiefe |
|--------|--------------|--------------|---------------|
| {{ source.system_1_name }} | {{ source.system_1_desc }} | {{ source.system_1_criticality }} | {{ source.system_1_depth }} |
| {{ source.system_2_name }} | {{ source.system_2_desc }} | {{ source.system_2_criticality }} | {{ source.system_2_depth }} |
| {{ source.system_3_name }} | {{ source.system_3_desc }} | {{ source.system_3_criticality }} | {{ source.system_3_depth }} |

#### IT-Prozesse im Scope
- Change Management
- Incident Management
- Access Management
- Backup und Recovery
- {{ source.additional_processes }}

## 3. Prüfungsschwerpunkte

### Prüfungsbereiche nach IDW PS 951

#### IT-Strategie und IT-Organisation
- IT-Governance-Struktur
- IT-Organisationsaufbau
- Rollen und Verantwortlichkeiten
- IT-Steuerungsgremien

#### IT-Prozesse
- IT-Service-Management-Prozesse
- Change- und Release-Management
- Problem- und Incident-Management
- Configuration Management

#### IT-Systeme und Anwendungen
- Anwendungslandschaft
- Systemarchitektur
- Anwendungskontrollen
- Schnittstellenmanagement

#### IT-Infrastruktur
- Server- und Storage-Systeme
- Netzwerkinfrastruktur
- Datenbanksysteme
- Backup-Systeme

#### IT-Sicherheit
- Zugriffskontrolle
- Verschlüsselung
- Security Monitoring
- Schwachstellenmanagement

#### Datenschutz
- DSGVO-Compliance
- Datenschutzkontrollen
- Privacy by Design

## 4. Ausschlüsse und Abgrenzungen

### Nicht im Scope
- {{ source.out_of_scope_1 }}
- {{ source.out_of_scope_2 }}
- {{ source.out_of_scope_3 }}

### Begründung für Ausschlüsse
{{ source.exclusion_rationale }}

## 5. Wesentlichkeit und Prüfungstiefe

### Wesentlichkeitskriterien
- **Finanziell:** {{ source.materiality_financial }}
- **Operativ:** {{ source.materiality_operational }}
- **Compliance:** {{ source.materiality_compliance }}

### Prüfungstiefe nach Risiko
- **Hoch:** Detaillierte Prüfung mit umfangreichen Tests
- **Mittel:** Standardprüfung mit Stichproben
- **Niedrig:** Überblicksprüfung

## 6. Schnittstellen zu anderen Prüfungen

### Koordination mit
- Jahresabschlussprüfung
- Interne Revision
- Datenschutzprüfung
- Compliance-Audits

### Abstimmung
{{ source.coordination_approach }}

## 7. Scope-Änderungen

### Änderungsprozess
Änderungen am Prüfungsumfang müssen dokumentiert und genehmigt werden:
- **Antragsteller:** {{ source.change_requestor }}
- **Genehmiger:** {{ source.change_approver }}
- **Dokumentation:** Änderungslog

### Änderungshistorie
| Datum | Änderung | Begründung | Genehmigt durch |
|-------|----------|------------|-----------------|
| {{ source.change_date }} | {{ source.change_description }} | {{ source.change_reason }} | {{ source.change_approver }} |

## 8. Referenzen

- IDW PS 951 - Prüfungsstandard
- Prüfungsauftrag
- IT-Systemdokumentation
- Risikoanalyse

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
