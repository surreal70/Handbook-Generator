# IT-Infrastruktur und Betrieb

**Dokument-ID:** idw-ps-951-0400  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}

---

## 1. Zweck

Dieses Dokument beschreibt die Prüfung der IT-Infrastruktur und des IT-Betriebs im Rahmen der IT-Prüfung nach IDW PS 951.

## 2. Prüfungsgegenstand

### IT-Infrastruktur
- **Server und Storage:** {{ source.server_storage }}
- **Netzwerkinfrastruktur:** {{ source.network_infrastructure }}
- **Datenbanksysteme:** {{ source.database_systems }}
- **Backup-Systeme:** {{ source.backup_systems }}

### Prüfungsziele
- Bewertung der IT-Infrastruktur
- Prüfung der Betriebsprozesse
- Beurteilung der Verfügbarkeit
- Bewertung der Backup- und Recovery-Prozesse

## 3. Prüfungshandlungen

### Dokumentenprüfung
- [ ] Infrastrukturdokumentation vorhanden
- [ ] Betriebshandbücher aktuell
- [ ] Backup-Konzept dokumentiert
- [ ] Disaster-Recovery-Plan vorhanden

### Kontrolltests
- Überprüfung der Backup-Prozesse
- Prüfung der Monitoring-Systeme
- Test der Recovery-Verfahren

## 4. Prüfungskriterien

| Komponente | Dokumentiert | Überwacht | Getestet | Bewertung |
|------------|--------------|-----------|----------|-----------|
| Server | {{ source.server_doc }} | {{ source.server_mon }} | {{ source.server_test }} | {{ source.server_assess }} |
| Netzwerk | {{ source.network_doc }} | {{ source.network_mon }} | {{ source.network_test }} | {{ source.network_assess }} |
| Backup | {{ source.backup_doc }} | {{ source.backup_mon }} | {{ source.backup_test }} | {{ source.backup_assess }} |

## 5. Feststellungen

### Positive Feststellungen
1. {{ source.positive_finding_1 }}

### Verbesserungspotenziale
1. {{ source.improvement_1 }}

## 6. Empfehlungen

1. {{ source.recommendation_1 }}

## 7. Referenzen

- IDW PS 951 - IT-Infrastruktur
- ITIL 4
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
