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
                
                # Collect all .md files in the category directory
                for template_file in category_dir.glob('*.md'):
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
            template_path = self.template_root / language / template_type
            error_msg = ErrorHandler.empty_template_directory_error(template_path)
            raise ValueError(error_msg)
        
        # Sort templates: metadata first (sort_order 0), then by sort_order
        templates.sort(key=lambda t: t.sort_order)
        
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
            expected_path = self.template_root / language / template_type
            return ErrorHandler.template_not_found_error(
                language, template_type, expected_path,
                available_languages, available_types
            )
        
        if template_type not in discovered[language]:
            available_languages, available_types = self.get_available_options()
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
