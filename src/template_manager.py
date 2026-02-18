"""
Template Manager for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import re
from .error_handler import ErrorHandler, ErrorContext


@dataclass
class Template:
    """
    Represents a template file with metadata.
    
    Attributes:
        path: Path to the template file
        template_type: Type of template ('content' or 'metadata')
        sort_order: Numeric sort order extracted from filename (e.g., 100 from '0100_intro.md')
        language: Language code (e.g., 'de', 'en')
        category: Handbook category (e.g., 'backup', 'bcm', 'isms', 'it-operation')
    """
    path: Path
    template_type: str  # 'content' or 'metadata'
    sort_order: int
    language: str
    category: str
    
    def is_metadata(self) -> bool:
        """Check if this is a metadata template."""
        return self.template_type == 'metadata'
    
    def read_content(self) -> str:
        """
        Read template file content.
        
        Returns:
            Template content as string
            
        Raises:
            FileNotFoundError: If template file doesn't exist
            PermissionError: If template file cannot be read
        """
        try:
            return self.path.read_text(encoding='utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Template file not found: {self.path}\n"
                f"The file may have been deleted or moved."
            )
        except PermissionError:
            raise PermissionError(
                f"Permission denied reading template file: {self.path}\n"
                f"Check file permissions and try again."
            )
        except UnicodeDecodeError as e:
            raise ValueError(
                f"Invalid encoding in template file: {self.path}\n"
                f"Template files must be UTF-8 encoded.\n"
                f"Error: {e}"
            )


class TemplateManager:
    """
    Manages template discovery, validation, and sorting.
    """
    
    # Supported compliance and operational frameworks
    SUPPORTED_FRAMEWORKS = [
        'backup',
        'bcm',
        'bsi-grundschutz',
        'cis-controls',
        'common-criteria',
        'coso',
        'csa-ccm',
        'dora',
        'email-service',
        'gdpr',
        'hipaa',
        'idw-ps-951',
        'isms',
        'iso-31000',
        'iso-38500',
        'iso-9001',
        'it-operation',
        'nist-800-53',
        'nist-csf',
        'pci-dss',
        'service-templates',
        'soc1',
        'tisax',
        'togaf',
        'tsc'
    ]
    
    # Framework configuration with display names, language support, and expected template counts
    FRAMEWORK_CONFIG = {
        'idw-ps-951': {
            'display_name': 'IDW PS 951',
            'languages': ['de', 'en'],
            'min_template_count': 50,  # At least 0010-0500
            'has_diagrams': True,
            'description': 'German IT auditing standard'
        },
        'nist-csf': {
            'display_name': 'NIST CSF 2.0',
            'languages': ['de', 'en'],
            'min_template_count': 60,  # At least 0010-0600
            'has_diagrams': True,
            'description': 'NIST Cybersecurity Framework 2.0'
        },
        'togaf': {
            'display_name': 'TOGAF',
            'languages': ['de', 'en'],
            'min_template_count': 70,  # At least 0010-0700
            'has_diagrams': True,
            'description': 'The Open Group Architecture Framework'
        },
        'iso-38500': {
            'display_name': 'ISO/IEC 38500',
            'languages': ['de', 'en'],
            'min_template_count': 40,  # At least 0010-0400
            'has_diagrams': True,
            'description': 'IT Governance standard'
        },
        'iso-31000': {
            'display_name': 'ISO 31000',
            'languages': ['de', 'en'],
            'min_template_count': 50,  # At least 0010-0500
            'has_diagrams': True,
            'description': 'Risk Management standard'
        },
        'csa-ccm': {
            'display_name': 'CSA CCM',
            'languages': ['de', 'en'],
            'min_template_count': 80,  # At least 0010-0800
            'has_diagrams': True,
            'description': 'Cloud Security Alliance Cloud Controls Matrix'
        },
        'tisax': {
            'display_name': 'TISAX',
            'languages': ['de', 'en'],
            'min_template_count': 60,  # At least 0010-0600
            'has_diagrams': True,
            'description': 'Automotive Information Security Assessment'
        },
        'soc1': {
            'display_name': 'SOC 1 / SSAE 18',
            'languages': ['de', 'en'],
            'min_template_count': 50,  # At least 0010-0500
            'has_diagrams': True,
            'description': 'Service Organization Control Type 1'
        },
        'coso': {
            'display_name': 'COSO',
            'languages': ['de', 'en'],
            'min_template_count': 60,  # At least 0010-0600
            'has_diagrams': True,
            'description': 'Committee of Sponsoring Organizations Internal Control Framework'
        },
        'dora': {
            'display_name': 'DORA',
            'languages': ['de', 'en'],
            'min_template_count': 40,  # At least 0010-0400
            'has_diagrams': True,
            'description': 'DevOps Research and Assessment metrics'
        }
    }
    
    # Pattern for metadata templates: 0000_metadata_[language]_[templatename].md
    METADATA_PATTERN = re.compile(r'^0000_metadata_([a-z]{2})_(.+)\.md$')
    
    # Pattern for content templates: NNNN_name.md
    CONTENT_PATTERN = re.compile(r'^(\d{4})_(.+)\.md$')
    
    def __init__(self, template_root: Path):
        """
        Initialize with template root directory.
        
        Args:
            template_root: Path to the templates directory
        """
        self.template_root = Path(template_root)
    
    def discover_templates(self, include_examples: bool = False) -> dict[str, dict[str, list[Path]]]:
        """
        Discover all available templates organized by language and type.
        
        Args:
            include_examples: If True, include templates from examples directory
        
        Returns:
            Dictionary structure: {language: {category: [template_paths]}}
            Example: {'de': {'backup': [Path(...), Path(...)], 'bcm': [...]}, 'en': {...}}
        """
        templates = {}
        
        if not self.template_root.exists():
            return templates
        
        # Scan for language directories (de, en)
        for lang_dir in self.template_root.iterdir():
            if not lang_dir.is_dir():
                continue
            
            # Skip examples directory unless explicitly requested
            if lang_dir.name == 'examples' and not include_examples:
                continue
            
            language = lang_dir.name
            templates[language] = {}
            
            # Scan for category directories (backup, bcm, isms, it-operation)
            for category_dir in lang_dir.iterdir():
                if not category_dir.is_dir():
                    continue
                
                category = category_dir.name
                template_files = []
                
                # Special handling for service-directory: scan subdirectories
                if category == 'service-directory':
                    for service_subdir in category_dir.iterdir():
                        if not service_subdir.is_dir():
                            continue
                        
                        service_category = service_subdir.name
                        service_files = []
                        
                        # Collect all .md files in the service subdirectory
                        for template_file in service_subdir.glob('*.md'):
                            service_files.append(template_file)
                        
                        if service_files:
                            templates[language][service_category] = service_files
                else:
                    # Collect all .md files in the category directory
                    # Skip special documentation files
                    for template_file in category_dir.glob('*.md'):
                        if template_file.name not in ['README.md', '9999_Framework_Mapping.md']:
                            template_files.append(template_file)
                    
                    if template_files:
                        templates[language][category] = template_files
        
        return templates
    
    def discover_examples(self) -> dict[str, list[Path]]:
        """
        Discover example templates in the examples directory.
        
        Returns:
            Dictionary structure: {category: [template_paths]}
            Example: {'backup': [Path(...)], 'ISO 27001': [Path(...)]}
        """
        examples = {}
        examples_dir = self.template_root / 'examples'
        
        if not examples_dir.exists():
            return examples
        
        # Scan for category directories in examples
        for category_dir in examples_dir.iterdir():
            if not category_dir.is_dir():
                continue
            
            category = category_dir.name
            template_files = []
            
            # Collect all .md files in the category directory
            for template_file in category_dir.glob('*.md'):
                template_files.append(template_file)
            
            if template_files:
                examples[category] = template_files
        
        return examples
    
    def get_templates(self, language: str, template_type: str) -> list[Template]:
        """
        Get sorted templates for specific language and type.
        
        Args:
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'backup', 'bcm', 'isms', 'it-operation')
        
        Returns:
            List of Template objects sorted by sort_order
            
        Raises:
            ValueError: If templates don't exist for the given language/type
        """
        # Validate that templates exist
        error_msg = self.validate_template_exists(language, template_type)
        if error_msg:
            raise ValueError(error_msg)
        
        discovered = self.discover_templates()
        template_paths = discovered[language][template_type]
        templates = []
        
        for path in template_paths:
            template = self._parse_template(path, language, template_type)
            if template:
                templates.append(template)
        
        # Edge case: No valid templates after parsing
        if not templates:
            # Construct path (handle service templates)
            if template_type in ['email-service', 'service-templates']:
                template_path = self.template_root / language / 'service-directory' / template_type
            else:
                template_path = self.template_root / language / template_type
            error_msg = ErrorHandler.empty_template_directory_error(template_path)
            raise ValueError(error_msg)
        
        # Sort templates: metadata first (sort_order 0), then by sort_order
        # Handle edge cases: missing numbers, duplicates
        templates.sort(key=lambda t: (t.sort_order, t.path.name))
        
        # Check for duplicate sort orders (excluding metadata and unnumbered templates)
        seen_orders = {}
        for template in templates:
            if template.sort_order not in [0, 9999]:  # Skip metadata and unnumbered
                if template.sort_order in seen_orders:
                    # Log warning about duplicate but continue processing
                    pass  # Handled by secondary sort on filename
                seen_orders[template.sort_order] = template
        
        return templates
    
    def _parse_template(self, path: Path, language: str, category: str) -> Optional[Template]:
        """
        Parse a template file and extract metadata.
        
        Args:
            path: Path to template file
            language: Language code
            category: Template category
        
        Returns:
            Template object or None if parsing fails
        """
        filename = path.name
        
        # Check if it's a metadata template
        metadata_match = self.METADATA_PATTERN.match(filename)
        if metadata_match:
            return Template(
                path=path,
                template_type='metadata',
                sort_order=0,  # Metadata templates always come first
                language=language,
                category=category
            )
        
        # Check if it's a content template
        content_match = self.CONTENT_PATTERN.match(filename)
        if content_match:
            sort_number = int(content_match.group(1))
            return Template(
                path=path,
                template_type='content',
                sort_order=sort_number,
                language=language,
                category=category
            )
        
        # Template without proper numbering - assign high sort order
        return Template(
            path=path,
            template_type='content',
            sort_order=9999,  # Place at end
            language=language,
            category=category
        )
    
    def validate_template_structure(self) -> list[str]:
        """
        Validate template directory structure and return warnings.
        
        Returns:
            List of warning messages
        """
        warnings = []
        
        if not self.template_root.exists():
            warnings.append(
                f"Template directory not found: {self.template_root}\n"
                f"Expected structure: templates/{{language}}/{{category}}/"
            )
            return warnings
        
        discovered = self.discover_templates()
        
        if not discovered:
            warnings.append(
                f"No templates found in {self.template_root}\n"
                f"Expected structure: templates/{{language}}/{{category}}/"
            )
        
        # Check for templates without proper numbering
        for language, categories in discovered.items():
            for category, template_paths in categories.items():
                for path in template_paths:
                    filename = path.name
                    if not self.METADATA_PATTERN.match(filename) and not self.CONTENT_PATTERN.match(filename):
                        reason = "Missing 4-digit prefix (e.g., 0100_) or invalid metadata format"
                        warning = ErrorHandler.invalid_filename_warning(path, reason)
                        warnings.append(warning)
        
        return warnings
    
    def get_available_options(self) -> tuple[list[str], dict[str, list[str]]]:
        """
        Get available languages and template types.
        
        Returns:
            Tuple of (available_languages, available_types_per_language)
        """
        discovered = self.discover_templates()
        available_languages = list(discovered.keys())
        available_types = {lang: list(categories.keys()) for lang, categories in discovered.items()}
        return available_languages, available_types
    
    def get_discovered_frameworks(self) -> set[str]:
        """
        Get all discovered framework directories across all languages.
        Automatically detects new framework directories without requiring
        updates to SUPPORTED_FRAMEWORKS list.
        
        Returns:
            Set of framework names discovered in template directories
        """
        discovered = self.discover_templates()
        frameworks = set()
        
        for lang_templates in discovered.values():
            frameworks.update(lang_templates.keys())
        
        return frameworks
    
    def get_framework_config(self, framework: str) -> Optional[dict]:
        """
        Get configuration for a specific framework.
        
        Args:
            framework: Framework identifier (e.g., 'idw-ps-951', 'nist-csf', 'togaf')
            
        Returns:
            Framework configuration dictionary or None if not configured
        """
        return self.FRAMEWORK_CONFIG.get(framework)
    
    def validate_framework_structure(self, framework: str, language: str) -> list[str]:
        """
        Validate framework directory structure and return warnings/errors.
        
        Args:
            framework: Framework identifier
            language: Language code
            
        Returns:
            List of validation messages (warnings and errors)
        """
        messages = []
        
        # Check if framework directory exists
        framework_dir = self.template_root / language / framework
        if not framework_dir.exists():
            messages.append(
                f"Framework directory not found: {framework_dir}\n"
                f"Expected structure: templates/{language}/{framework}/"
            )
            return messages
        
        # Check for required files
        required_files = ['README.md', '9999_Framework_Mapping.md']
        for required_file in required_files:
            file_path = framework_dir / required_file
            if not file_path.exists():
                messages.append(
                    f"Required file missing: {file_path}\n"
                    f"Framework {framework} should include {required_file}"
                )
        
        # Check for metadata template
        metadata_pattern = f'0000_metadata_{language}_{framework}.md'
        metadata_path = framework_dir / metadata_pattern
        if not metadata_path.exists():
            messages.append(
                f"Metadata template missing: {metadata_path}\n"
                f"Framework {framework} should include metadata template"
            )
        
        # Check for diagrams directory
        diagrams_dir = framework_dir / 'diagrams'
        if not diagrams_dir.exists():
            messages.append(
                f"Diagrams directory missing: {diagrams_dir}\n"
                f"Framework {framework} should include diagrams/ subdirectory"
            )
        
        # Check template count if framework is configured
        config = self.get_framework_config(framework)
        if config:
            discovered = self.discover_templates()
            if language in discovered and framework in discovered[language]:
                template_count = len(discovered[language][framework])
                min_count = config.get('min_template_count', 0)
                
                if template_count < min_count:
                    messages.append(
                        f"Insufficient templates for {framework}: "
                        f"found {template_count}, expected at least {min_count}"
                    )
        
        return messages
    
    def extract_metadata(self, language: str, framework: str) -> dict[str, str]:
        """
        Extract metadata from framework metadata template.
        
        Args:
            language: Language code
            framework: Framework identifier
            
        Returns:
            Dictionary with metadata fields (title, author, version, date, organization, classification)
            
        Raises:
            ValueError: If metadata template not found or cannot be parsed
        """
        # Find metadata template
        metadata_pattern = f'0000_metadata_{language}_{framework}.md'
        framework_dir = self.template_root / language / framework
        metadata_path = framework_dir / metadata_pattern
        
        if not metadata_path.exists():
            raise ValueError(
                f"Metadata template not found: {metadata_path}\n"
                f"Framework {framework} requires a metadata template"
            )
        
        # Read metadata content
        try:
            content = metadata_path.read_text(encoding='utf-8')
        except Exception as e:
            raise ValueError(
                f"Failed to read metadata template: {metadata_path}\n"
                f"Error: {e}"
            )
        
        # Extract metadata fields from YAML frontmatter or content
        metadata = {
            'title': '',
            'author': '',
            'version': '',
            'date': '',
            'organization': '',
            'classification': ''
        }
        
        # Parse YAML frontmatter if present
        if content.startswith('---'):
            try:
                # Extract frontmatter between --- markers
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1].strip()
                    
                    # Parse simple YAML key-value pairs
                    for line in frontmatter.split('\n'):
                        line = line.strip()
                        if ':' in line:
                            key, value = line.split(':', 1)
                            key = key.strip().lower()
                            value = value.strip().strip('"').strip("'")
                            
                            if key in metadata:
                                metadata[key] = value
            except Exception:
                # If frontmatter parsing fails, continue with empty metadata
                pass
        
        return metadata
    
    def validate_template_exists(self, language: str, template_type: str) -> Optional[str]:
        """
        Validate that a template exists for the given language and type.
        
        Args:
            language: Language code
            template_type: Template category
            
        Returns:
            Error message if template doesn't exist, None otherwise
        """
        discovered = self.discover_templates()
        
        if language not in discovered:
            available_languages, available_types = self.get_available_options()
            # Construct expected path (handle service templates)
            if template_type in ['email-service', 'service-templates']:
                expected_path = self.template_root / language / 'service-directory' / template_type
            else:
                expected_path = self.template_root / language / template_type
            return ErrorHandler.template_not_found_error(
                language, template_type, expected_path,
                available_languages, available_types
            )
        
        if template_type not in discovered[language]:
            available_languages, available_types = self.get_available_options()
            # Construct expected path (handle service templates)
            if template_type in ['email-service', 'service-templates']:
                expected_path = self.template_root / language / 'service-directory' / template_type
            else:
                expected_path = self.template_root / language / template_type
            return ErrorHandler.template_not_found_error(
                language, template_type, expected_path,
                available_languages, available_types
            )
        
        # Check if directory is empty
        template_paths = discovered[language][template_type]
        if not template_paths:
            template_path = self.template_root / language / template_type
            return ErrorHandler.empty_template_directory_error(template_path)
        
        return None
    
    def detect_handbook_directory(self, language: str, template_type: str) -> Optional[Path]:
        """
        Detect handbook directory from template path.
        
        The handbook directory is where meta-handbook.yaml should be located.
        For standard templates: templates/{language}/{template_type}/
        For service templates: templates/{language}/service-directory/{template_type}/
        
        Args:
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'bcm', 'isms', 'email-service')
            
        Returns:
            Path to handbook directory, or None if not found
        """
        # Handle service templates (in service-directory subdirectory)
        if template_type in ['email-service', 'service-templates']:
            handbook_dir = self.template_root / language / 'service-directory' / template_type
        else:
            handbook_dir = self.template_root / language / template_type
        
        # Return path if directory exists
        if handbook_dir.exists() and handbook_dir.is_dir():
            return handbook_dir
        
        return None
    
    def load_handbook_metadata(self, language: str, template_type: str):
        """
        Load handbook-specific metadata for a given language and template type.
        
        This method detects the handbook directory and loads meta-handbook.yaml
        from that directory using MetadataLoader.
        
        Args:
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'bcm', 'isms')
            
        Returns:
            HandbookMetadata object with loaded or default values
            
        Raises:
            ValueError: If handbook directory cannot be detected
        """
        from src.metadata_loader import MetadataLoader
        
        # Detect handbook directory
        handbook_dir = self.detect_handbook_directory(language, template_type)
        
        if handbook_dir is None:
            raise ValueError(
                f"Cannot detect handbook directory for language '{language}' "
                f"and template type '{template_type}'"
            )
        
        # Load handbook metadata using MetadataLoader
        metadata_loader = MetadataLoader()
        handbook_metadata = metadata_loader.load_handbook_metadata(handbook_dir)
        
        return handbook_metadata
    
    def process_handbook(self, language: str, template_type: str, unified_metadata):
        """
        Process a handbook by loading handbook-specific metadata and merging it
        into the unified metadata context.
        
        This method:
        1. Detects the handbook directory from language and template type
        2. Loads handbook-specific metadata using MetadataLoader
        3. Merges handbook metadata into the UnifiedMetadata context
        
        Args:
            language: Language code (e.g., 'de', 'en')
            template_type: Template category (e.g., 'bcm', 'isms')
            unified_metadata: UnifiedMetadata object to update with handbook metadata
            
        Returns:
            Updated UnifiedMetadata object with handbook metadata merged
            
        Raises:
            ValueError: If handbook directory cannot be detected
        """
        # Load handbook-specific metadata
        handbook_metadata = self.load_handbook_metadata(language, template_type)
        
        # Merge handbook metadata into unified context
        unified_metadata.handbook = handbook_metadata
        
        return unified_metadata
