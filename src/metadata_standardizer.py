"""
Metadata Standardizer for Handbook Generator

Manages metadata standardization across all compliance framework templates.
Provides functionality to scan, validate, create, and enhance metadata files.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set
import re


@dataclass
class FrameworkStatus:
    """
    Status information for a framework's metadata.
    
    Attributes:
        name: Framework name (e.g., 'gdpr', 'iso-9001')
        has_de_metadata: Whether German metadata file exists
        has_en_metadata: Whether English metadata file exists
        de_metadata_complete: Whether German metadata has all required fields
        en_metadata_complete: Whether English metadata has all required fields
        missing_fields: List of missing required fields
    """
    name: str
    has_de_metadata: bool
    has_en_metadata: bool
    de_metadata_complete: bool
    en_metadata_complete: bool
    missing_fields: List[str] = field(default_factory=list)


@dataclass
class MissingMetadata:
    """
    Information about missing metadata file.
    
    Attributes:
        framework: Framework name
        language: Language code ('de' or 'en')
        expected_path: Expected file path for the metadata file
    """
    framework: str
    language: str
    expected_path: str


@dataclass
class ValidationResult:
    """
    Result of metadata validation.
    
    Attributes:
        is_valid: Whether metadata passes all validation checks
        missing_fields: List of missing required fields
        invalid_fields: List of fields with invalid format/values
        warnings: List of warning messages
    """
    is_valid: bool
    missing_fields: List[str] = field(default_factory=list)
    invalid_fields: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


@dataclass
class StandardizationReport:
    """
    Summary report of standardization process.
    
    Attributes:
        total_frameworks: Total number of frameworks scanned
        frameworks_processed: Number of frameworks processed
        files_created: Number of metadata files created
        files_enhanced: Number of metadata files enhanced
        validation_errors: Number of validation errors found
        summary: Human-readable summary text
    """
    total_frameworks: int
    frameworks_processed: int
    files_created: int
    files_enhanced: int
    validation_errors: int
    summary: str


class MetadataStandardizer:
    """
    Manages metadata standardization across all compliance framework templates.
    
    Provides functionality to:
    - Scan frameworks and detect missing metadata
    - Create new metadata files with unified structure
    - Enhance existing metadata files with missing fields
    - Validate metadata structure and content
    - Generate standardization reports
    """
    
    # Required metadata fields for unified structure
    REQUIRED_FIELDS = [
        'document_id',
        'owner',
        'version',
        'status',
        'classification',
        'date',
        'template_version',
        'revision',
        'organization',
        'author',
        'scope',
        'valid_from',
        'next_review'
    ]
    
    # Pattern for metadata files: 0000_metadata_{language}_{framework}.md
    METADATA_PATTERN = re.compile(r'^0000_metadata_([a-z]{2})_(.+)\.md$')
    
    # Pattern for template_version: MAJOR.MINOR (e.g., "1.0", "2.1")
    VERSION_PATTERN = re.compile(r'^\d+\.\d+$')
    
    # Supported languages
    SUPPORTED_LANGUAGES = ['de', 'en']
    
    def __init__(self, templates_dir: str):
        """
        Initialize MetadataStandardizer with templates directory.
        
        Args:
            templates_dir: Path to the templates directory
        """
        self.templates_dir = Path(templates_dir)
        self._frameworks_cache: Optional[Set[str]] = None
    
    def scan_frameworks(self) -> Dict[str, FrameworkStatus]:
        """
        Scan all frameworks and return status report.
        
        Discovers all framework directories and checks metadata completeness
        for each language variant.
        
        Returns:
            Dictionary mapping framework name to FrameworkStatus
            Example: {'gdpr': FrameworkStatus(...), 'iso-9001': FrameworkStatus(...)}
        """
        frameworks_status = {}
        
        # Discover all frameworks
        frameworks = self._discover_frameworks()
        
        for framework in frameworks:
            # Check for metadata files in both languages
            de_path = self._get_metadata_path(framework, 'de')
            en_path = self._get_metadata_path(framework, 'en')
            
            has_de = de_path.exists()
            has_en = en_path.exists()
            
            # Check completeness
            de_complete = False
            en_complete = False
            missing_fields = []
            
            if has_de:
                de_validation = self.validate_metadata_structure(str(de_path))
                de_complete = de_validation.is_valid
                if not de_complete:
                    missing_fields.extend(de_validation.missing_fields)
            
            if has_en:
                en_validation = self.validate_metadata_structure(str(en_path))
                en_complete = en_validation.is_valid
                if not en_complete:
                    # Only add missing fields not already in list
                    for field in en_validation.missing_fields:
                        if field not in missing_fields:
                            missing_fields.append(field)
            
            frameworks_status[framework] = FrameworkStatus(
                name=framework,
                has_de_metadata=has_de,
                has_en_metadata=has_en,
                de_metadata_complete=de_complete,
                en_metadata_complete=en_complete,
                missing_fields=missing_fields
            )
        
        return frameworks_status
    
    def detect_missing_metadata(self) -> List[MissingMetadata]:
        """
        Identify frameworks missing metadata files.
        
        Returns:
            List of MissingMetadata objects for each missing file
        """
        missing = []
        frameworks = self._discover_frameworks()
        
        for framework in frameworks:
            for language in self.SUPPORTED_LANGUAGES:
                metadata_path = self._get_metadata_path(framework, language)
                
                if not metadata_path.exists():
                    missing.append(MissingMetadata(
                        framework=framework,
                        language=language,
                        expected_path=str(metadata_path)
                    ))
        
        return missing
    
    def _discover_frameworks(self) -> Set[str]:
        """
        Discover all framework directories in templates directory.
        
        Returns:
            Set of framework names
        """
        if self._frameworks_cache is not None:
            return self._frameworks_cache
        
        frameworks = set()
        
        if not self.templates_dir.exists():
            return frameworks
        
        # Scan both language directories
        for language in self.SUPPORTED_LANGUAGES:
            lang_dir = self.templates_dir / language
            
            if not lang_dir.exists():
                continue
            
            # Each subdirectory is a framework
            for item in lang_dir.iterdir():
                if item.is_dir():
                    # Skip service-directory and examples
                    if item.name not in ['service-directory', 'examples']:
                        frameworks.add(item.name)
        
        self._frameworks_cache = frameworks
        return frameworks
    
    def _get_metadata_path(self, framework: str, language: str) -> Path:
        """
        Get expected metadata file path for framework and language.
        
        Args:
            framework: Framework name
            language: Language code ('de' or 'en')
        
        Returns:
            Path to metadata file
        """
        filename = f"0000_metadata_{language}_{framework}.md"
        return self.templates_dir / language / framework / filename
    
    def validate_metadata_structure(self, filepath: str) -> ValidationResult:
        """
        Validate metadata file against unified structure.
        
        Checks for:
        - All 13 required fields present
        - template_version format (MAJOR.MINOR)
        - revision is non-negative integer
        
        Args:
            filepath: Path to metadata file
        
        Returns:
            ValidationResult with validation status and details
        """
        path = Path(filepath)
        
        if not path.exists():
            return ValidationResult(
                is_valid=False,
                missing_fields=self.REQUIRED_FIELDS.copy(),
                warnings=[f"File does not exist: {filepath}"]
            )
        
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                warnings=[f"Could not read file: {e}"]
            )
        
        missing_fields = []
        invalid_fields = []
        warnings = []
        
        # Check for required fields
        for field in self.REQUIRED_FIELDS:
            if field == 'template_version':
                # Check for Template-Version or Template Version
                if not self._field_exists(content, 'template_version', ['Template-Version', 'Template Version']):
                    missing_fields.append('template_version')
                else:
                    # Validate format or accept placeholder
                    version_value = self._extract_field_value(content, ['Template-Version', 'Template Version'])
                    if version_value:
                        # Accept placeholders as valid
                        if not (version_value.startswith('{{') and version_value.endswith('}}')):
                            if not self.VERSION_PATTERN.match(version_value):
                                invalid_fields.append(f'template_version (invalid format: {version_value})')
            
            elif field == 'revision':
                # Check for Revision
                if not self._field_exists(content, 'revision', ['Revision']):
                    missing_fields.append('revision')
                else:
                    # Validate it's an integer or placeholder
                    revision_value = self._extract_field_value(content, ['Revision'])
                    if revision_value:
                        # Accept placeholders as valid
                        if not (revision_value.startswith('{{') and revision_value.endswith('}}')):
                            try:
                                rev_int = int(revision_value)
                                if rev_int < 0:
                                    invalid_fields.append(f'revision (must be non-negative: {revision_value})')
                            except ValueError:
                                invalid_fields.append(f'revision (not an integer or placeholder: {revision_value})')
            
            else:
                # Check for other required fields
                field_labels = self._get_field_labels(field)
                if not self._field_exists(content, field, field_labels):
                    missing_fields.append(field)
        
        is_valid = len(missing_fields) == 0 and len(invalid_fields) == 0
        
        return ValidationResult(
            is_valid=is_valid,
            missing_fields=missing_fields,
            invalid_fields=invalid_fields,
            warnings=warnings
        )
    
    def _field_exists(self, content: str, field_name: str, labels: List[str]) -> bool:
        """
        Check if a field exists in metadata content.
        
        Args:
            content: Metadata file content
            field_name: Internal field name
            labels: List of possible label variations
        
        Returns:
            True if field exists, False otherwise
        """
        for label in labels:
            # Check for markdown bold format: **Label:**
            if f"**{label}:**" in content:
                return True
            # Check for plain format: Label:
            if f"{label}:" in content:
                return True
        return False
    
    def _extract_field_value(self, content: str, labels: List[str]) -> Optional[str]:
        """
        Extract field value from metadata content.
        Handles both literal values and placeholder syntax ({{ meta-handbook.field }}).
        
        Args:
            content: Metadata file content
            labels: List of possible label variations
        
        Returns:
            Field value or None if not found
        """
        for label in labels:
            # Try markdown bold format: **Label:** value
            pattern = rf'\*\*{re.escape(label)}:\*\*\s*(.+?)(?:\n|$)'
            match = re.search(pattern, content)
            if match:
                value = match.group(1).strip()
                # Check if it's a placeholder
                if value.startswith('{{') and value.endswith('}}'):
                    # Return the placeholder as-is for validation
                    return value
                return value
            
            # Try plain format: Label: value
            pattern = rf'{re.escape(label)}:\s*(.+?)(?:\n|$)'
            match = re.search(pattern, content)
            if match:
                value = match.group(1).strip()
                # Check if it's a placeholder
                if value.startswith('{{') and value.endswith('}}'):
                    # Return the placeholder as-is for validation
                    return value
                return value
        
        return None
    
    def _get_field_labels(self, field_name: str) -> List[str]:
        """
        Get possible label variations for a field.
        
        Args:
            field_name: Internal field name
        
        Returns:
            List of label variations (German and English)
        """
        label_map = {
            'document_id': ['Dokument-ID', 'Document-ID', 'Document ID'],
            'owner': ['Owner'],
            'version': ['Version'],
            'status': ['Status'],
            'classification': ['Klassifizierung', 'Classification'],
            'date': ['Letzte Aktualisierung', 'Last Updated', 'Erstellt am', 'Created'],
            'organization': ['Organisation', 'Organization'],
            'author': ['Autor', 'Author'],
            'scope': ['Geltungsbereich', 'Scope'],
            'valid_from': ['Gültig ab', 'Valid From', 'Valid from', 'Erstellungsdatum'],
            'next_review': ['Nächste Überprüfung', 'Next Review', 'Next review']
        }
        
        return label_map.get(field_name, [field_name])

    
    def generate_report(self) -> StandardizationReport:
        """
        Generate summary report of standardization process.
        
        Scans all frameworks and generates statistics about:
        - Total frameworks found
        - Frameworks with complete metadata
        - Missing metadata files
        - Validation errors
        
        Returns:
            StandardizationReport with summary statistics
        """
        frameworks_status = self.scan_frameworks()
        missing_metadata = self.detect_missing_metadata()
        
        total_frameworks = len(frameworks_status)
        frameworks_processed = 0
        files_created = 0
        files_enhanced = 0
        validation_errors = 0
        
        # Count frameworks with complete metadata
        for status in frameworks_status.values():
            if status.de_metadata_complete and status.en_metadata_complete:
                frameworks_processed += 1
            
            # Count validation errors (missing fields)
            if status.missing_fields:
                validation_errors += len(status.missing_fields)
        
        # Count missing files
        files_created = len(missing_metadata)
        
        # Count files that need enhancement (exist but incomplete)
        for status in frameworks_status.values():
            if status.has_de_metadata and not status.de_metadata_complete:
                files_enhanced += 1
            if status.has_en_metadata and not status.en_metadata_complete:
                files_enhanced += 1
        
        # Generate summary text
        summary_lines = [
            f"Metadata Standardization Report",
            f"=" * 50,
            f"Total frameworks scanned: {total_frameworks}",
            f"Frameworks with complete metadata: {frameworks_processed}",
            f"Missing metadata files: {files_created}",
            f"Files needing enhancement: {files_enhanced}",
            f"Validation errors found: {validation_errors}",
            f"",
            f"Framework Status:"
        ]
        
        for framework, status in sorted(frameworks_status.items()):
            de_status = "✓" if status.de_metadata_complete else ("✗" if status.has_de_metadata else "missing")
            en_status = "✓" if status.en_metadata_complete else ("✗" if status.has_en_metadata else "missing")
            summary_lines.append(f"  {framework:25} DE: {de_status:8} EN: {en_status:8}")
            
            if status.missing_fields:
                summary_lines.append(f"    Missing fields: {', '.join(status.missing_fields)}")
        
        summary = "\n".join(summary_lines)
        
        return StandardizationReport(
            total_frameworks=total_frameworks,
            frameworks_processed=frameworks_processed,
            files_created=files_created,
            files_enhanced=files_enhanced,
            validation_errors=validation_errors,
            summary=summary
        )

    
    # Framework-specific metadata templates
    FRAMEWORK_INFO = {
        'bcm': {
            'de': {
                'title': 'BCM Handbuch',
                'full_name': 'Business Continuity Management Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert das Business Continuity Management (BCM) System der Organisation gemäß ISO 22301 und BSI Standard 100-4. Es beschreibt die Struktur, Prozesse, Verantwortlichkeiten und Verfahren zur Sicherstellung der Geschäftskontinuität.',
                'scope': '{{ meta.bcm_scope }}',
                'references': [
                    'ISO 22301:2019 (Business Continuity Management)',
                    'BSI Standard 100-4 (Notfallmanagement)'
                ]
            },
            'en': {
                'title': 'BCM Handbook',
                'full_name': 'Business Continuity Management Handbook',
                'purpose': 'This handbook documents the organization\'s Business Continuity Management (BCM) system according to ISO 22301 and BSI Standard 100-4. It describes the structure, processes, responsibilities, and procedures for ensuring business continuity.',
                'scope': '{{ meta.bcm_scope }}',
                'references': [
                    'ISO 22301:2019 (Business Continuity Management)',
                    'BSI Standard 100-4 (Emergency Management)'
                ]
            }
        },
        'isms': {
            'de': {
                'title': 'ISMS Handbuch',
                'full_name': 'Informationssicherheits-Managementsystem Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert das Informationssicherheits-Managementsystem (ISMS) der Organisation gemäß ISO/IEC 27001. Es beschreibt die Struktur, Prozesse, Verantwortlichkeiten und Verfahren zur Sicherstellung der Informationssicherheit.',
                'scope': '{{ meta.isms_scope }}',
                'references': [
                    'ISO/IEC 27001:2022 (Information Security Management)',
                    'ISO/IEC 27002:2022 (Information Security Controls)'
                ]
            },
            'en': {
                'title': 'ISMS Handbook',
                'full_name': 'Information Security Management System Handbook',
                'purpose': 'This handbook documents the organization\'s Information Security Management System (ISMS) according to ISO/IEC 27001. It describes the structure, processes, responsibilities, and procedures for ensuring information security.',
                'scope': '{{ meta.isms_scope }}',
                'references': [
                    'ISO/IEC 27001:2022 (Information Security Management)',
                    'ISO/IEC 27002:2022 (Information Security Controls)'
                ]
            }
        },
        'bsi-grundschutz': {
            'de': {
                'title': 'BSI Grundschutz Handbuch',
                'full_name': 'BSI IT-Grundschutz Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert die Umsetzung des BSI IT-Grundschutzes in der Organisation. Es beschreibt die Struktur, Prozesse, Verantwortlichkeiten und Maßnahmen zur Erreichung eines angemessenen IT-Sicherheitsniveaus.',
                'scope': '{{ meta.grundschutz_scope }}',
                'references': [
                    'BSI IT-Grundschutz-Kompendium',
                    'BSI Standard 200-1 (Managementsysteme für Informationssicherheit)',
                    'BSI Standard 200-2 (IT-Grundschutz-Methodik)',
                    'BSI Standard 200-3 (Risikoanalyse)'
                ]
            },
            'en': {
                'title': 'BSI IT-Grundschutz Handbook',
                'full_name': 'BSI IT-Grundschutz Handbook',
                'purpose': 'This handbook documents the implementation of BSI IT-Grundschutz in the organization. It describes the structure, processes, responsibilities, and measures to achieve an appropriate IT security level.',
                'scope': '{{ meta.grundschutz_scope }}',
                'references': [
                    'BSI IT-Grundschutz Compendium',
                    'BSI Standard 200-1 (Management Systems for Information Security)',
                    'BSI Standard 200-2 (IT-Grundschutz Methodology)',
                    'BSI Standard 200-3 (Risk Analysis)'
                ]
            }
        },
        'it-operation': {
            'de': {
                'title': 'IT-Betriebshandbuch',
                'full_name': 'IT-Betriebshandbuch',
                'purpose': 'Dieses Handbuch dokumentiert die IT-Betriebsprozesse und -verfahren der Organisation. Es beschreibt die Struktur, Verantwortlichkeiten und Prozesse für den sicheren und effizienten IT-Betrieb.',
                'scope': '{{ meta.it_operation_scope }}',
                'references': [
                    'ITIL v4 (IT Service Management)',
                    'ISO/IEC 20000 (IT Service Management)'
                ]
            },
            'en': {
                'title': 'IT Operations Handbook',
                'full_name': 'IT Operations Handbook',
                'purpose': 'This handbook documents the organization\'s IT operations processes and procedures. It describes the structure, responsibilities, and processes for secure and efficient IT operations.',
                'scope': '{{ meta.it_operation_scope }}',
                'references': [
                    'ITIL v4 (IT Service Management)',
                    'ISO/IEC 20000 (IT Service Management)'
                ]
            }
        },
        'cis-controls': {
            'de': {
                'title': 'CIS Controls Handbuch',
                'full_name': 'CIS Controls v8 Hardening Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert die Umsetzung der CIS Controls v8 in der Organisation. Es beschreibt Hardening-Standards, Sicherheitsbaselines und Konfigurationsrichtlinien für IT-Systeme.',
                'scope': '{{ meta.cis_scope }}',
                'references': [
                    'CIS Controls v8',
                    'CIS Benchmarks'
                ]
            },
            'en': {
                'title': 'CIS Controls Handbook',
                'full_name': 'CIS Controls v8 Hardening Handbook',
                'purpose': 'This handbook documents the implementation of CIS Controls v8 in the organization. It describes hardening standards, security baselines, and configuration guidelines for IT systems.',
                'scope': '{{ meta.cis_scope }}',
                'references': [
                    'CIS Controls v8',
                    'CIS Benchmarks'
                ]
            }
        },
        'common-criteria': {
            'de': {
                'title': 'Common Criteria Security Target',
                'full_name': 'Common Criteria Security Target (ISO/IEC 15408)',
                'purpose': 'Dieses Security Target (ST) dokumentiert die Sicherheitseigenschaften des Target of Evaluation (TOE) gemäß ISO/IEC 15408 (Common Criteria for Information Technology Security Evaluation).',
                'scope': '{{ meta.cc_scope }}',
                'references': [
                    'ISO/IEC 15408-1:2022 (Common Criteria Part 1)',
                    'ISO/IEC 15408-2:2022 (Common Criteria Part 2)',
                    'ISO/IEC 15408-3:2022 (Common Criteria Part 3)'
                ]
            },
            'en': {
                'title': 'Common Criteria Security Target',
                'full_name': 'Common Criteria Security Target (ISO/IEC 15408)',
                'purpose': 'This Security Target (ST) documents the security properties of the Target of Evaluation (TOE) according to ISO/IEC 15408 (Common Criteria for Information Technology Security Evaluation).',
                'scope': '{{ meta.cc_scope }}',
                'references': [
                    'ISO/IEC 15408-1:2022 (Common Criteria Part 1)',
                    'ISO/IEC 15408-2:2022 (Common Criteria Part 2)',
                    'ISO/IEC 15408-3:2022 (Common Criteria Part 3)'
                ]
            }
        },
        'gdpr': {
            'de': {
                'title': 'DSGVO Datenschutz-Handbuch',
                'full_name': 'DSGVO Datenschutz-Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert die Datenschutzmaßnahmen und -prozesse der Organisation gemäß der Datenschutz-Grundverordnung (DSGVO/GDPR - EU 2016/679).',
                'scope': '{{ meta.gdpr_scope }}',
                'references': [
                    'Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung - DSGVO)',
                    'Bundesdatenschutzgesetz (BDSG)'
                ]
            },
            'en': {
                'title': 'GDPR Data Protection Handbook',
                'full_name': 'GDPR Data Protection Handbook',
                'purpose': 'This handbook documents the organization\'s data protection measures and processes according to the General Data Protection Regulation (GDPR - EU 2016/679).',
                'scope': '{{ meta.gdpr_scope }}',
                'references': [
                    'Regulation (EU) 2016/679 (General Data Protection Regulation - GDPR)',
                    'National data protection laws'
                ]
            }
        },
        'hipaa': {
            'de': {
                'title': 'HIPAA Compliance Handbuch',
                'full_name': 'HIPAA Compliance Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert die Umsetzung der HIPAA-Anforderungen (Health Insurance Portability and Accountability Act) in der Organisation.',
                'scope': '{{ meta.hipaa_scope }}',
                'references': [
                    'HIPAA Privacy Rule (45 CFR Part 160 and Part 164, Subparts A and E)',
                    'HIPAA Security Rule (45 CFR Part 164, Subpart C)',
                    'HIPAA Breach Notification Rule (45 CFR Part 164, Subpart D)'
                ]
            },
            'en': {
                'title': 'HIPAA Compliance Handbook',
                'full_name': 'HIPAA Compliance Handbook',
                'purpose': 'This handbook documents the implementation of HIPAA (Health Insurance Portability and Accountability Act) requirements in the organization.',
                'scope': '{{ meta.hipaa_scope }}',
                'references': [
                    'HIPAA Privacy Rule (45 CFR Part 160 and Part 164, Subparts A and E)',
                    'HIPAA Security Rule (45 CFR Part 164, Subpart C)',
                    'HIPAA Breach Notification Rule (45 CFR Part 164, Subpart D)'
                ]
            }
        },
        'iso-9001': {
            'de': {
                'title': 'QMS Handbuch',
                'full_name': 'Qualitätsmanagementsystem Handbuch (ISO 9001)',
                'purpose': 'Dieses Handbuch dokumentiert das Qualitätsmanagementsystem (QMS) der Organisation gemäß ISO 9001:2015.',
                'scope': '{{ meta.qms_scope }}',
                'references': [
                    'ISO 9001:2015 (Quality Management Systems)',
                    'ISO 9000:2015 (Quality Management - Fundamentals and vocabulary)'
                ]
            },
            'en': {
                'title': 'QMS Handbook',
                'full_name': 'Quality Management System Handbook (ISO 9001)',
                'purpose': 'This handbook documents the organization\'s Quality Management System (QMS) according to ISO 9001:2015.',
                'scope': '{{ meta.qms_scope }}',
                'references': [
                    'ISO 9001:2015 (Quality Management Systems)',
                    'ISO 9000:2015 (Quality Management - Fundamentals and vocabulary)'
                ]
            }
        },
        'nist-800-53': {
            'de': {
                'title': 'NIST 800-53 Handbuch',
                'full_name': 'NIST 800-53 Security Controls Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert die Umsetzung der NIST 800-53 Security and Privacy Controls in der Organisation.',
                'scope': '{{ meta.nist_scope }}',
                'references': [
                    'NIST SP 800-53 Rev. 5 (Security and Privacy Controls)',
                    'NIST SP 800-53B (Control Baselines)'
                ]
            },
            'en': {
                'title': 'NIST 800-53 Handbook',
                'full_name': 'NIST 800-53 Security Controls Handbook',
                'purpose': 'This handbook documents the implementation of NIST 800-53 Security and Privacy Controls in the organization.',
                'scope': '{{ meta.nist_scope }}',
                'references': [
                    'NIST SP 800-53 Rev. 5 (Security and Privacy Controls)',
                    'NIST SP 800-53B (Control Baselines)'
                ]
            }
        },
        'pci-dss': {
            'de': {
                'title': 'PCI-DSS Handbuch',
                'full_name': 'PCI-DSS Compliance Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert die Umsetzung der Payment Card Industry Data Security Standard (PCI-DSS) Anforderungen in der Organisation.',
                'scope': '{{ meta.pci_scope }}',
                'references': [
                    'PCI DSS v4.0 (Payment Card Industry Data Security Standard)',
                    'PCI DSS Requirements and Testing Procedures'
                ]
            },
            'en': {
                'title': 'PCI-DSS Handbook',
                'full_name': 'PCI-DSS Compliance Handbook',
                'purpose': 'This handbook documents the implementation of Payment Card Industry Data Security Standard (PCI-DSS) requirements in the organization.',
                'scope': '{{ meta.pci_scope }}',
                'references': [
                    'PCI DSS v4.0 (Payment Card Industry Data Security Standard)',
                    'PCI DSS Requirements and Testing Procedures'
                ]
            }
        },
        'tsc': {
            'de': {
                'title': 'TSC Handbuch',
                'full_name': 'Trust Services Criteria (SOC 2) Handbuch',
                'purpose': 'Dieses Handbuch dokumentiert die Umsetzung der Trust Services Criteria (TSC) für SOC 2 Compliance in der Organisation.',
                'scope': '{{ meta.tsc_scope }}',
                'references': [
                    'AICPA Trust Services Criteria',
                    'SOC 2 Reporting Framework'
                ]
            },
            'en': {
                'title': 'TSC Handbook',
                'full_name': 'Trust Services Criteria (SOC 2) Handbook',
                'purpose': 'This handbook documents the implementation of Trust Services Criteria (TSC) for SOC 2 compliance in the organization.',
                'scope': '{{ meta.tsc_scope }}',
                'references': [
                    'AICPA Trust Services Criteria',
                    'SOC 2 Reporting Framework'
                ]
            }
        }
    }
    
    def create_metadata_file(self, framework: str, language: str) -> bool:
        """
        Create standardized metadata file for framework.
        
        Uses unified metadata template structure with framework-specific
        content (title, purpose, references). Initializes template_version
        to "1.0" and revision to "0".
        
        Args:
            framework: Framework name (e.g., 'gdpr', 'iso-9001')
            language: Language code ('de' or 'en')
        
        Returns:
            True if file created successfully, False otherwise
        
        Raises:
            ValueError: If framework or language is invalid
            FileExistsError: If metadata file already exists
        """
        if language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {language}. Must be one of: {self.SUPPORTED_LANGUAGES}")
        
        # Get metadata path
        metadata_path = self._get_metadata_path(framework, language)
        
        if metadata_path.exists():
            raise FileExistsError(f"Metadata file already exists: {metadata_path}")
        
        # Get framework-specific information
        framework_info = self.FRAMEWORK_INFO.get(framework)
        if not framework_info:
            # Use generic template for unknown frameworks
            framework_info = {
                language: {
                    'title': f'{framework.upper()} Handbook',
                    'full_name': f'{framework.upper()} Handbook',
                    'purpose': f'This handbook documents the {framework} framework implementation.',
                    'scope': '{{ meta.scope }}',
                    'references': [f'{framework.upper()} Standard']
                }
            }
        
        lang_info = framework_info.get(language, framework_info.get('de', framework_info.get('en')))
        
        # Generate metadata content
        content = self._generate_metadata_content(
            framework=framework,
            language=language,
            title=lang_info['title'],
            full_name=lang_info['full_name'],
            purpose=lang_info['purpose'],
            scope=lang_info['scope'],
            references=lang_info['references']
        )
        
        # Create parent directory if needed
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write metadata file
        try:
            metadata_path.write_text(content, encoding='utf-8')
            return True
        except Exception as e:
            print(f"Error creating metadata file: {e}")
            return False
    
    def _generate_metadata_content(
        self,
        framework: str,
        language: str,
        title: str,
        full_name: str,
        purpose: str,
        scope: str,
        references: List[str]
    ) -> str:
        """
        Generate metadata file content using unified template.
        
        Args:
            framework: Framework name
            language: Language code
            title: Short title
            full_name: Full handbook name
            purpose: Document purpose description
            scope: Scope description
            references: List of normative references
        
        Returns:
            Complete metadata file content
        """
        # Format references as bullet list
        references_text = "\n".join(f"- {ref}" for ref in references)
        
        # Language-specific labels
        if language == 'de':
            labels = {
                'metadata_title': f'{title} - Metadaten',
                'document_id': 'Dokument-ID',
                'owner': 'Owner',
                'version': 'Version',
                'status': 'Status',
                'classification': 'Klassifizierung',
                'last_updated': 'Letzte Aktualisierung',
                'template_version': 'Template-Version',
                'revision': 'Revision',
                'handbook_info': 'Handbuch-Informationen',
                'handbook_title': 'Handbuch-Titel',
                'organization': 'Organisation',
                'author': 'Autor',
                'scope_label': 'Geltungsbereich',
                'valid_from': 'Gültig ab',
                'next_review': 'Nächste Überprüfung',
                'purpose_title': 'Dokumentenzweck',
                'scope_title': 'Geltungsbereich',
                'references_title': 'Normative Verweise',
                'history_title': 'Änderungshistorie',
                'history_version': 'Version',
                'history_date': 'Datum',
                'history_author': 'Autor',
                'history_change': 'Änderung',
                'history_initial': 'Initiale Version',
                'footer_comment': f'Dieses Dokument ist Teil des {title}s und unterliegt der Dokumentenlenkung.'
            }
        else:  # English
            labels = {
                'metadata_title': f'{title} - Metadata',
                'document_id': 'Document-ID',
                'owner': 'Owner',
                'version': 'Version',
                'status': 'Status',
                'classification': 'Classification',
                'last_updated': 'Last Updated',
                'template_version': 'Template Version',
                'revision': 'Revision',
                'handbook_info': 'Handbook Information',
                'handbook_title': 'Handbook Title',
                'organization': 'Organization',
                'author': 'Author',
                'scope_label': 'Scope',
                'valid_from': 'Valid from',
                'next_review': 'Next Review',
                'purpose_title': 'Document Purpose',
                'scope_title': 'Scope',
                'references_title': 'Normative References',
                'history_title': 'Change History',
                'history_version': 'Version',
                'history_date': 'Date',
                'history_author': 'Author',
                'history_change': 'Change',
                'history_initial': 'Initial Version',
                'footer_comment': f'This document is part of the {title} and is subject to document control.'
            }
        
        # Generate content
        content = f"""# {labels['metadata_title']}

**{labels['document_id']}:** 0000  
**{labels['owner']}:** {{{{ meta.owner }}}}  
**{labels['version']}:** {{{{ meta.version }}}}  
**{labels['status']}:** {{{{ meta.status }}}}  
**{labels['classification']}:** {{{{ meta.classification }}}}  
**{labels['last_updated']}:** {{{{ meta.date }}}}  
**{labels['template_version']}:** 1.0  
**{labels['revision']}:** 0  

---

## {labels['handbook_info']}

**{labels['handbook_title']}:** {full_name}  
**{labels['organization']}:** {{{{ meta.organization }}}}  
**{labels['author']}:** {{{{ meta.author }}}}  
**{labels['scope_label']}:** {scope}  
**{labels['valid_from']}:** {{{{ meta.valid_from }}}}  
**{labels['next_review']}:** {{{{ meta.next_review }}}}  

---

## {labels['purpose_title']}

{purpose}

## {labels['scope_title']}

{scope}

## {labels['references_title']}

{references_text}

## {labels['history_title']}

| {labels['history_version']} | {labels['history_date']} | {labels['history_author']} | {labels['history_change']} |
|---------|-------|-------|----------|
| {{{{ meta.version }}}} | {{{{ meta.date }}}} | {{{{ meta.author }}}} | {labels['history_initial']} |

<!-- 
{labels['footer_comment']}
Template-Version: 1.0
Revision: 0
-->
"""
        
        return content

    
    def enhance_existing_metadata(self, filepath: str) -> bool:
        """
        Add missing required fields to existing metadata file.
        
        Preserves existing content and structure while adding:
        - Missing required fields
        - template_version field (set to "1.0")
        - revision field (set to "0")
        
        Args:
            filepath: Path to existing metadata file
        
        Returns:
            True if file enhanced successfully, False otherwise
        
        Raises:
            FileNotFoundError: If metadata file doesn't exist
        """
        path = Path(filepath)
        
        if not path.exists():
            raise FileNotFoundError(f"Metadata file not found: {filepath}")
        
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading metadata file: {e}")
            return False
        
        # Validate current structure
        validation = self.validate_metadata_structure(filepath)
        
        if validation.is_valid:
            # Already complete, no enhancement needed
            return True
        
        # Determine language from filename
        match = self.METADATA_PATTERN.match(path.name)
        if match:
            language = match.group(1)
        else:
            # Try to detect from content
            language = 'de' if 'Dokument-ID' in content or 'Geltungsbereich' in content else 'en'
        
        # Enhance content with missing fields
        enhanced_content = self._enhance_content(
            content=content,
            missing_fields=validation.missing_fields,
            invalid_fields=validation.invalid_fields,
            language=language
        )
        
        # Write enhanced content
        try:
            path.write_text(enhanced_content, encoding='utf-8')
            return True
        except Exception as e:
            print(f"Error writing enhanced metadata file: {e}")
            return False
    
    def _enhance_content(
        self,
        content: str,
        missing_fields: List[str],
        invalid_fields: List[str],
        language: str
    ) -> str:
        """
        Enhance metadata content by adding missing fields.
        
        Args:
            content: Original metadata content
            missing_fields: List of missing field names
            invalid_fields: List of invalid field descriptions
            language: Language code ('de' or 'en')
        
        Returns:
            Enhanced metadata content
        """
        lines = content.split('\n')
        enhanced_lines = []
        
        # Track which sections we've found
        found_header = False
        in_header = True
        found_handbook_info = False
        found_purpose = False
        found_scope = False
        found_references = False
        found_history = False
        
        # Categorize missing fields
        header_fields_to_add = []
        info_fields_to_add = []
        
        for field in missing_fields:
            if field in ['document_id', 'owner', 'version', 'status', 'classification', 'date', 'template_version', 'revision']:
                header_fields_to_add.append(field)
            elif field in ['organization', 'author', 'scope', 'valid_from', 'next_review']:
                info_fields_to_add.append(field)
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if we're leaving the header section (first ---)
            if line.strip() == '---' and in_header and not found_header:
                found_header = True
                in_header = False
                # Add missing header fields before the separator
                if header_fields_to_add:
                    for field in header_fields_to_add:
                        label = self._get_field_label(field, language)
                        placeholder = self._get_field_placeholder(field)
                        enhanced_lines.append(f"**{label}:** {placeholder}  ")
                enhanced_lines.append(line)
                i += 1
                continue
            
            # Check for Handbook Information section
            if '## ' in line and ('Handbuch-Informationen' in line or 'Handbook Information' in line):
                found_handbook_info = True
                enhanced_lines.append(line)
                i += 1
                continue
            
            # Check if we're at the end of Handbook Information section
            if found_handbook_info and not found_purpose and line.strip() == '---':
                # Add missing info fields before the separator
                if info_fields_to_add:
                    for field in info_fields_to_add:
                        label = self._get_field_label(field, language)
                        placeholder = self._get_field_placeholder(field)
                        enhanced_lines.append(f"**{label}:** {placeholder}  ")
                enhanced_lines.append(line)
                i += 1
                continue
            
            # Check for other sections
            if '## ' in line:
                if 'Dokumentenzweck' in line or 'Document Purpose' in line:
                    found_purpose = True
                elif 'Geltungsbereich' in line or 'Scope' in line:
                    found_scope = True
                elif 'Normative Verweise' in line or 'Normative References' in line:
                    found_references = True
                elif 'Änderungshistorie' in line or 'Change History' in line:
                    found_history = True
            
            enhanced_lines.append(line)
            i += 1
        
        # Add missing Handbook Information section if needed
        if not found_handbook_info and info_fields_to_add:
            enhanced_lines.append('')
            enhanced_lines.append('## ' + ('Handbuch-Informationen' if language == 'de' else 'Handbook Information'))
            enhanced_lines.append('')
            for field in info_fields_to_add:
                label = self._get_field_label(field, language)
                placeholder = self._get_field_placeholder(field)
                enhanced_lines.append(f"**{label}:** {placeholder}  ")
            enhanced_lines.append('')
            enhanced_lines.append('---')
        
        # Add missing sections at the end if needed
        if not found_purpose:
            enhanced_lines.append('')
            enhanced_lines.append('## ' + ('Dokumentenzweck' if language == 'de' else 'Document Purpose'))
            enhanced_lines.append('')
            enhanced_lines.append('[TODO: Add document purpose description]')
        
        if not found_scope:
            enhanced_lines.append('')
            enhanced_lines.append('## ' + ('Geltungsbereich' if language == 'de' else 'Scope'))
            enhanced_lines.append('')
            enhanced_lines.append('{{ meta.scope }}')
        
        if not found_references:
            enhanced_lines.append('')
            enhanced_lines.append('## ' + ('Normative Verweise' if language == 'de' else 'Normative References'))
            enhanced_lines.append('')
            enhanced_lines.append('[TODO: Add normative references]')
        
        if not found_history:
            enhanced_lines.append('')
            enhanced_lines.append('## ' + ('Änderungshistorie' if language == 'de' else 'Change History'))
            enhanced_lines.append('')
            if language == 'de':
                enhanced_lines.append('| Version | Datum | Autor | Änderung |')
                enhanced_lines.append('|---------|-------|-------|----------|')
                enhanced_lines.append('| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initiale Version |')
            else:
                enhanced_lines.append('| Version | Date | Author | Change |')
                enhanced_lines.append('|---------|------|--------|--------|')
                enhanced_lines.append('| {{ meta.version }} | {{ meta.date }} | {{ meta.author }} | Initial Version |')
        
        # Handle footer comment - remove old one if exists and add new one
        # Find and remove existing footer comment (everything from <!-- to -->)
        footer_start = -1
        for i in range(len(enhanced_lines) - 1, -1, -1):
            if '-->' in enhanced_lines[i]:
                # Found end of comment, keep looking for start
                continue
            elif '<!--' in enhanced_lines[i]:
                # Found start of comment
                footer_start = i
                break
        
        # Remove footer if found
        if footer_start >= 0:
            # Remove from footer_start to end
            enhanced_lines = enhanced_lines[:footer_start]
            # Remove trailing empty lines
            while enhanced_lines and enhanced_lines[-1].strip() == '':
                enhanced_lines.pop()
        
        # Add new footer comment
        enhanced_lines.append('')
        enhanced_lines.append('<!-- ')
        if language == 'de':
            enhanced_lines.append('Dieses Dokument unterliegt der Dokumentenlenkung.')
        else:
            enhanced_lines.append('This document is subject to document control.')
        enhanced_lines.append('Template-Version: 1.0')
        enhanced_lines.append('Revision: 0')
        enhanced_lines.append('-->')
        
        return '\n'.join(enhanced_lines)
    
    def _get_field_label(self, field_name: str, language: str) -> str:
        """
        Get display label for a field.
        
        Args:
            field_name: Internal field name
            language: Language code
        
        Returns:
            Display label
        """
        if language == 'de':
            labels = {
                'document_id': 'Dokument-ID',
                'owner': 'Owner',
                'version': 'Version',
                'status': 'Status',
                'classification': 'Klassifizierung',
                'date': 'Letzte Aktualisierung',
                'template_version': 'Template-Version',
                'revision': 'Revision',
                'organization': 'Organisation',
                'author': 'Autor',
                'scope': 'Geltungsbereich',
                'valid_from': 'Gültig ab',
                'next_review': 'Nächste Überprüfung'
            }
        else:
            labels = {
                'document_id': 'Document-ID',
                'owner': 'Owner',
                'version': 'Version',
                'status': 'Status',
                'classification': 'Classification',
                'date': 'Last Updated',
                'template_version': 'Template Version',
                'revision': 'Revision',
                'organization': 'Organization',
                'author': 'Author',
                'scope': 'Scope',
                'valid_from': 'Valid from',
                'next_review': 'Next Review'
            }
        
        return labels.get(field_name, field_name)
    
    def _get_field_placeholder(self, field_name: str) -> str:
        """
        Get placeholder value for a field.
        
        Args:
            field_name: Internal field name
        
        Returns:
            Placeholder value
        """
        placeholders = {
            'document_id': '0000',
            'owner': '{{ meta.owner }}',
            'version': '{{ meta.version }}',
            'status': '{{ meta.status }}',
            'classification': '{{ meta.classification }}',
            'date': '{{ meta.date }}',
            'template_version': '1.0',
            'revision': '0',
            'organization': '{{ meta.organization }}',
            'author': '{{ meta.author }}',
            'scope': '{{ meta.scope }}',
            'valid_from': '{{ meta.valid_from }}',
            'next_review': '{{ meta.next_review }}'
        }
        
        return placeholders.get(field_name, f'{{{{ meta.{field_name} }}}}')



class DocumentHistoryStandardizer:
    """
    Manages document history standardization across all template files.
    
    Provides functionality to:
    - Scan template markdown files (excluding metadata files)
    - Detect existing document history sections
    - Add standardized document history sections
    - Validate document history format
    """
    
    # Pattern for metadata files to skip
    METADATA_PATTERN = re.compile(r'^0000_metadata_[a-z]{2}_.*\.md$')
    
    # Supported languages
    SUPPORTED_LANGUAGES = ['de', 'en']
    
    def __init__(self, templates_dir: str):
        """
        Initialize DocumentHistoryStandardizer with templates directory.
        
        Args:
            templates_dir: Path to the templates directory
        """
        self.templates_dir = Path(templates_dir)
    
    def scan_template_files(self) -> List[str]:
        """
        Scan all template markdown files (excluding metadata files).
        
        Returns:
            List of template file paths
        """
        template_files = []
        
        if not self.templates_dir.exists():
            return template_files
        
        # Scan both language directories
        for language in self.SUPPORTED_LANGUAGES:
            lang_dir = self.templates_dir / language
            
            if not lang_dir.exists():
                continue
            
            # Recursively find all .md files
            for md_file in lang_dir.rglob('*.md'):
                # Skip metadata files
                if not self.METADATA_PATTERN.match(md_file.name):
                    template_files.append(str(md_file))
        
        return template_files
    
    def has_document_history(self, filepath: str) -> bool:
        """
        Check if file contains document history section.
        
        Args:
            filepath: Path to template file
        
        Returns:
            True if document history section exists, False otherwise
        """
        path = Path(filepath)
        
        if not path.exists():
            return False
        
        try:
            content = path.read_text(encoding='utf-8')
        except Exception:
            return False
        
        # Check for German or English document history headers (both old and new format)
        # Also check for "Änderungshistorie" (Change History) which is used in metadata files
        return ('**Dokumenthistorie:**' in content or 
                '**Document History:**' in content or
                '## Dokumenthistorie' in content or 
                '## Document History' in content or
                '## Änderungshistorie' in content or
                '## Change History' in content)
    
    def generate_history_section(self, language: str) -> str:
        """
        Generate standardized document history section for DE/EN templates.
        
        Args:
            language: Language code ('de' or 'en')
        
        Returns:
            Formatted document history section
        """
        if language == 'de':
            return """**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
"""
        else:  # English
            return """**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
"""
    
    def add_document_history(self, filepath: str, language: str) -> bool:
        """
        Add standardized document history section to template file.
        
        Inserts section before <!-- End of template --> marker if present,
        otherwise at end of file.
        Skips metadata files (0000_metadata_*.md).
        Preserves existing file content.
        Removes duplicate document history sections.
        
        Args:
            filepath: Path to template file
            language: Language code ('de' or 'en')
        
        Returns:
            True if history added successfully, False otherwise
        """
        path = Path(filepath)
        
        # Skip metadata files
        if self.METADATA_PATTERN.match(path.name):
            return False
        
        if not path.exists():
            return False
        
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return False
        
        # Check if already has the correct format
        if self.has_document_history(filepath):
            # Check if it's in the correct position (before <!-- End of template -->)
            end_marker = '<!-- End of template -->'
            if end_marker in content:
                # Check if history is before the marker
                parts = content.split(end_marker)
                if '**Dokumenthistorie:**' in parts[0] or '**Document History:**' in parts[0]:
                    # Already in correct position
                    return True
                # History is after marker, need to move it
            else:
                # No marker, history is at end - this is correct
                return True
        
        # Remove any existing document history sections
        # Pattern 1: ## Dokumenthistorie / ## Document History
        content = re.sub(
            r'\n+## (Dokumenthistorie|Document History)\n+\| Version.*?\n\|.*?\n\| 0\.1.*?\n*',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Pattern 2: **Dokumenthistorie:** / **Document History:**
        content = re.sub(
            r'\n+\*\*(Dokumenthistorie|Document History):\*\*\n+\| Version.*?\n\|.*?\n\| 0\.1.*?\n*',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Pattern 3: With separator before
        content = re.sub(
            r'\n+---\n+\*\*(Dokumenthistorie|Document History):\*\*\n+\| Version.*?\n\|.*?\n\| 0\.1.*?\n*',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Clean up trailing whitespace and separators
        content = content.rstrip()
        while content.endswith('\n---'):
            content = content[:-4].rstrip()
        
        # Generate history section
        history_section = self.generate_history_section(language)
        
        # Find the <!-- End of template --> marker
        end_marker = '<!-- End of template -->'
        
        if end_marker in content:
            # Insert before the end marker
            parts = content.split(end_marker, 1)
            enhanced_content = parts[0].rstrip() + '\n\n---\n\n' + history_section.rstrip() + '\n\n' + end_marker
            if len(parts) > 1:
                enhanced_content += parts[1]
        else:
            # No end marker, add at the end
            enhanced_content = content + '\n\n---\n\n' + history_section
        
        # Write enhanced content
        try:
            path.write_text(enhanced_content, encoding='utf-8')
            return True
        except Exception as e:
            print(f"Error writing file {filepath}: {e}")
            return False
    
    def validate_document_history_format(self, filepath: str) -> ValidationResult:
        """
        Validate document history section format.
        
        Checks for:
        - Presence of "**Dokumenthistorie:**" or "**Document History:**"
        - Table format with correct column headers
        - Initial row with version 0.1
        
        Returns validation warnings (not errors) for backward compatibility.
        
        Args:
            filepath: Path to template file
        
        Returns:
            ValidationResult with validation status and warnings
        """
        path = Path(filepath)
        
        # Skip metadata files
        if self.METADATA_PATTERN.match(path.name):
            return ValidationResult(
                is_valid=True,
                warnings=["Skipped metadata file"]
            )
        
        if not path.exists():
            return ValidationResult(
                is_valid=False,
                warnings=[f"File does not exist: {filepath}"]
            )
        
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                warnings=[f"Could not read file: {e}"]
            )
        
        warnings = []
        
        # Check for document history header (old format with bold)
        has_de_header = '**Dokumenthistorie:**' in content
        has_en_header = '**Document History:**' in content
        
        # Also check for new format (## header)
        has_de_header_new = '## Dokumenthistorie' in content
        has_en_header_new = '## Document History' in content
        
        if not (has_de_header or has_en_header or has_de_header_new or has_en_header_new):
            warnings.append("Missing document history section")
            return ValidationResult(
                is_valid=True,  # Warning, not error for backward compatibility
                warnings=warnings
            )
        
        # Determine language
        if has_de_header or has_de_header_new:
            language = 'de'
        else:
            language = 'en'
        
        # Check for table headers
        if language == 'de':
            expected_headers = ['Version', 'Datum', 'Autor', 'Änderungen']
            header_pattern = r'\|\s*Version\s*\|\s*Datum\s*\|\s*Autor\s*\|\s*Änderungen\s*\|'
        else:
            expected_headers = ['Version', 'Date', 'Author', 'Changes']
            header_pattern = r'\|\s*Version\s*\|\s*Date\s*\|\s*Author\s*\|\s*Changes\s*\|'
        
        if not re.search(header_pattern, content):
            warnings.append(f"Document history table headers do not match expected format: {', '.join(expected_headers)}")
        
        # Check for initial version 0.1
        version_pattern = r'\|\s*0\.1\s*\|'
        if not re.search(version_pattern, content):
            warnings.append("Document history missing initial version 0.1")
        
        return ValidationResult(
            is_valid=True,  # Always return True for backward compatibility
            warnings=warnings
        )



@dataclass
class DuplicateRole:
    """
    Information about a duplicate role definition.
    
    Attributes:
        role_name: Name of the duplicate role
        canonical_role: Name of the canonical role it duplicates
        reason: Explanation of why it's considered a duplicate
    """
    role_name: str
    canonical_role: str
    reason: str


class MetadataRoleCleanup:
    """
    Manages role cleanup and reorganization in metadata.example.yaml.
    
    Provides functionality to:
    - Detect duplicate role definitions
    - Remove duplicate roles from YAML
    - Reorganize IT operations roles into proper sections
    - Validate role structure and organization
    - Update template references to removed roles
    """
    
    def __init__(self, metadata_file: str = "metadata.example.yaml"):
        """
        Initialize MetadataRoleCleanup with metadata file path.
        
        Args:
            metadata_file: Path to metadata.example.yaml file
        """
        self.metadata_file = Path(metadata_file)
        self._yaml_content: Optional[str] = None
        self._roles_data: Optional[Dict] = None
    
    def detect_duplicate_roles(self) -> List[DuplicateRole]:
        """
        Detect duplicate role definitions based on semantic analysis.
        
        Identifies roles that serve the same purpose but have different names.
        Currently detects:
        - datenschutzbeauftragter (duplicate of data_protection_officer)
        
        Returns:
            List of DuplicateRole objects
        """
        duplicates = []
        
        if not self.metadata_file.exists():
            return duplicates
        
        try:
            import yaml
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading YAML file: {e}")
            return duplicates
        
        if 'roles' not in data:
            return duplicates
        
        roles = data['roles']
        
        # Check for datenschutzbeauftragter (German) vs data_protection_officer (English)
        if 'datenschutzbeauftragter' in roles and 'data_protection_officer' in roles:
            duplicates.append(DuplicateRole(
                role_name='datenschutzbeauftragter',
                canonical_role='data_protection_officer',
                reason='German name for Data Protection Officer - duplicate of data_protection_officer'
            ))
        
        # Could add more semantic duplicate detection here in the future
        # For example, checking role titles or responsibilities
        
        return duplicates
    
    def remove_duplicate_role(self, role_name: str) -> bool:
        """
        Remove duplicate role from metadata YAML file.
        
        Preserves formatting, comments, and structure of the YAML file.
        Uses line-by-line processing to maintain exact formatting.
        
        Args:
            role_name: Name of the role to remove
        
        Returns:
            True if role removed successfully, False otherwise
        """
        if not self.metadata_file.exists():
            print(f"Metadata file not found: {self.metadata_file}")
            return False
        
        try:
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading metadata file: {e}")
            return False
        
        # Find the role definition and remove it
        new_lines = []
        in_role_block = False
        role_indent = 0
        skip_until_next_role = False
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if this is the start of the role we want to remove
            if line.strip().startswith(f'{role_name}:'):
                # Found the role to remove
                in_role_block = True
                skip_until_next_role = True
                # Determine indentation level
                role_indent = len(line) - len(line.lstrip())
                i += 1
                continue
            
            # If we're skipping a role block
            if skip_until_next_role:
                # Check if we've reached the next role or end of roles section
                stripped = line.strip()
                
                # Empty lines or comments within the role block
                if not stripped or stripped.startswith('#'):
                    i += 1
                    continue
                
                # Check indentation to see if we're still in the role block
                current_indent = len(line) - len(line.lstrip())
                
                # If indentation is same or less than role indent, we've left the role block
                if current_indent <= role_indent and stripped:
                    skip_until_next_role = False
                    in_role_block = False
                    # Don't skip this line, process it normally
                else:
                    # Still in the role block, skip this line
                    i += 1
                    continue
            
            # Keep this line
            new_lines.append(line)
            i += 1
        
        # Write the modified content back
        try:
            with open(self.metadata_file, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            return True
        except Exception as e:
            print(f"Error writing metadata file: {e}")
            return False
    
    def reorganize_it_operations_roles(self) -> bool:
        """
        Reorganize IT operations roles into proper sections.
        
        Moves it_manager and sysop from "Add Custom Roles Here" section
        to "IT Operations Roles" section.
        
        Ensures proper section ordering:
        - C-Level Executives
        - IT Operations Roles
        - BCM and Security Roles
        - Add Custom Roles Here
        
        Returns:
            True if reorganization successful, False otherwise
        """
        if not self.metadata_file.exists():
            print(f"Metadata file not found: {self.metadata_file}")
            return False
        
        try:
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading metadata file: {e}")
            return False
        
        # Find the roles to move and their definitions
        roles_to_move = ['it_manager', 'sysop']
        role_definitions = {}  # role_name -> list of lines
        
        # First pass: extract role definitions and mark for removal
        i = 0
        while i < len(lines):
            line = lines[i]
            
            for role_name in roles_to_move:
                if line.strip().startswith(f'{role_name}:'):
                    # Found a role to move, extract its full definition
                    role_lines = [line]
                    role_indent = len(line) - len(line.lstrip())
                    i += 1
                    
                    # Collect all lines that belong to this role
                    while i < len(lines):
                        next_line = lines[i]
                        next_stripped = next_line.strip()
                        
                        # Empty lines or comments
                        if not next_stripped or next_stripped.startswith('#'):
                            role_lines.append(next_line)
                            i += 1
                            continue
                        
                        # Check indentation
                        next_indent = len(next_line) - len(next_line.lstrip())
                        
                        # If same or less indentation and not empty, we've left the role
                        if next_indent <= role_indent:
                            break
                        
                        role_lines.append(next_line)
                        i += 1
                    
                    role_definitions[role_name] = role_lines
                    break
            else:
                i += 1
        
        if not role_definitions:
            # Roles not found or already in correct position
            return True
        
        # Second pass: build new file with roles moved
        new_lines = []
        skip_role = None
        role_indent = 0
        inserted_roles = False
        
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            # Check if we should skip this role (it's being moved)
            if not skip_role:
                for role_name in roles_to_move:
                    if stripped.startswith(f'{role_name}:'):
                        skip_role = role_name
                        role_indent = len(line) - len(line.lstrip())
                        i += 1
                        break
                
                if skip_role:
                    continue
            
            # If we're currently skipping a role
            if skip_role:
                # Check if we've left the role block
                if not stripped or stripped.startswith('#'):
                    # Empty line or comment within role block
                    i += 1
                    continue
                
                current_indent = len(line) - len(line.lstrip())
                
                if current_indent <= role_indent and stripped:
                    # We've left the role block
                    skip_role = None
                    # Don't skip this line, process it normally
                else:
                    # Still in the role block, skip this line
                    i += 1
                    continue
            
            # Check if this is service_desk_lead (insert point for moved roles)
            if not inserted_roles and stripped.startswith('service_desk_lead:'):
                # Add service_desk_lead
                new_lines.append(line)
                role_indent = len(line) - len(line.lstrip())
                i += 1
                
                # Collect all lines of service_desk_lead
                while i < len(lines):
                    next_line = lines[i]
                    next_stripped = next_line.strip()
                    
                    if not next_stripped or next_stripped.startswith('#'):
                        new_lines.append(next_line)
                        i += 1
                        continue
                    
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent <= role_indent:
                        break
                    
                    new_lines.append(next_line)
                    i += 1
                
                # Insert the moved roles here
                for role_name in ['it_manager', 'sysop']:
                    if role_name in role_definitions:
                        new_lines.append('\n')
                        new_lines.extend(role_definitions[role_name])
                
                inserted_roles = True
                continue
            
            # Keep this line
            new_lines.append(line)
            i += 1
        
        # Write the modified content back
        try:
            with open(self.metadata_file, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            return True
        except Exception as e:
            print(f"Error writing metadata file: {e}")
            return False
    
    def validate_role_structure(self) -> ValidationResult:
        """
        Validate role organization and detect duplicates.
        
        Checks for:
        - Duplicate role definitions
        - Proper section organization
        - IT operations roles in correct section
        
        Returns:
            ValidationResult with validation status and details
        """
        if not self.metadata_file.exists():
            return ValidationResult(
                is_valid=False,
                warnings=[f"Metadata file not found: {self.metadata_file}"]
            )
        
        try:
            import yaml
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                warnings=[f"Error loading YAML file: {e}"]
            )
        
        if 'roles' not in data:
            return ValidationResult(
                is_valid=False,
                warnings=["No roles section found in metadata file"]
            )
        
        roles = data['roles']
        invalid_fields = []
        warnings = []
        
        # Check for duplicate roles
        duplicates = self.detect_duplicate_roles()
        if duplicates:
            for dup in duplicates:
                invalid_fields.append(
                    f"Duplicate role '{dup.role_name}' (duplicate of '{dup.canonical_role}'): {dup.reason}"
                )
        
        # Check role ordering (this is a simplified check)
        role_names = list(roles.keys())
        
        # Check if it_manager and sysop are after service_desk_lead
        if 'service_desk_lead' in role_names:
            service_desk_idx = role_names.index('service_desk_lead')
            
            if 'it_manager' in role_names:
                it_manager_idx = role_names.index('it_manager')
                if it_manager_idx < service_desk_idx:
                    warnings.append("it_manager should be in IT Operations Roles section (after service_desk_lead)")
            
            if 'sysop' in role_names:
                sysop_idx = role_names.index('sysop')
                if sysop_idx < service_desk_idx:
                    warnings.append("sysop should be in IT Operations Roles section (after service_desk_lead)")
        
        is_valid = len(invalid_fields) == 0
        
        return ValidationResult(
            is_valid=is_valid,
            invalid_fields=invalid_fields,
            warnings=warnings
        )
    
    def update_template_references(self, old_role: str, new_role: str, templates_dir: str = "templates") -> int:
        """
        Update template files that reference removed roles.
        
        Scans all template markdown files and replaces references to old_role
        with new_role in placeholder format.
        
        Args:
            old_role: Old role name to replace (e.g., 'datenschutzbeauftragter')
            new_role: New role name to use (e.g., 'data_protection_officer')
            templates_dir: Path to templates directory
        
        Returns:
            Number of files updated
        """
        templates_path = Path(templates_dir)
        
        if not templates_path.exists():
            print(f"Templates directory not found: {templates_dir}")
            return 0
        
        files_updated = 0
        
        # Pattern to match {{ meta.old_role.* }}
        old_pattern = re.compile(
            r'\{\{\s*meta\.' + re.escape(old_role) + r'\.([a-zA-Z_]+)\s*\}\}'
        )
        
        # Scan all markdown files
        for md_file in templates_path.rglob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
            except Exception as e:
                print(f"Error reading {md_file}: {e}")
                continue
            
            # Check if file contains references to old role
            if f'meta.{old_role}.' not in content:
                continue
            
            # Replace all occurrences
            new_content = old_pattern.sub(
                r'{{ meta.' + new_role + r'.\1 }}',
                content
            )
            
            if new_content != content:
                try:
                    md_file.write_text(new_content, encoding='utf-8')
                    files_updated += 1
                    print(f"Updated: {md_file}")
                except Exception as e:
                    print(f"Error writing {md_file}: {e}")
        
        return files_updated
