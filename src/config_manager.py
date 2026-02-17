"""
Configuration Manager for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Dict
import yaml
from src.error_handler import ErrorHandler
from src.metadata_config_manager import MetadataConfig, MetadataConfigManager
from src.metadata_loader import MetadataLoader
from src.unified_metadata import UnifiedMetadata


@dataclass
class DataSourceConfig:
    """Configuration for a single data source."""
    url: str
    api_token: str
    role_distinction: Optional[Dict] = None


@dataclass
class Config:
    """
    Configuration data model for the Handbook Generator.
    
    Attributes:
        data_sources: Dictionary of data source configurations (e.g., 'netbox')
        default_language: Default language for handbook generation (default: 'de')
        default_output_format: Default output format (default: 'both')
        author: Author information for metadata
        version: Version number for generated handbooks
        unified_metadata: Unified metadata from all configuration sources
    """
    data_sources: Dict[str, DataSourceConfig] = field(default_factory=dict)
    default_language: str = "de"
    default_output_format: str = "both"
    author: str = "Andreas Huemmer [andreas.huemmer@adminsend.de]"
    version: str = "0.0.1"
    unified_metadata: Optional[UnifiedMetadata] = None
    
    @property
    def netbox_url(self) -> Optional[str]:
        """Get NetBox URL if configured."""
        netbox = self.data_sources.get('netbox')
        return netbox.url if netbox else None
    
    @property
    def netbox_api_token(self) -> Optional[str]:
        """Get NetBox API token if configured."""
        netbox = self.data_sources.get('netbox')
        return netbox.api_token if netbox else None
    
    @property
    def netbox_role_distinction(self) -> Optional[Dict]:
        """Get NetBox role distinction configuration if configured."""
        netbox = self.data_sources.get('netbox')
        return netbox.role_distinction if netbox else None


class ConfigManager:
    """
    Manages configuration file loading, creation, and validation.
    
    Handles YAML parsing, default configuration generation, and ensures
    configuration files are properly excluded from version control.
    """
    
    DEFAULT_CONFIG_CONTENT = """# Handbook Generator Configuration
# WARNING: This file contains sensitive credentials - do not commit to git!

data_sources:
  netbox:
    url: "https://netbox.example.com"
    api_token: "your-api-token-here"
    
    # NetBox role distinction configuration
    role_distinction:
      method: "field"  # "field" or "name"
      field: "role"    # Field name if method is "field"
      mappings:
        ciso: "Chief Information Security Officer"
        cio: "Chief Information Officer"
        sysop: "System Administrator"

defaults:
  language: "de"
  output_format: "both"  # markdown, pdf, both
  
metadata:
  author: "Andreas Huemmer [andreas.huemmer@adminsend.de]"
  version: "1.0.0"
"""
    
    def __init__(self, config_path: Path):
        """
        Initialize ConfigManager with configuration file path.
        
        Args:
            config_path: Path to the configuration file
        """
        self.config_path = Path(config_path)
        self.project_root = self._find_project_root()
    
    def _find_project_root(self) -> Path:
        """Find project root by looking for .git directory or using config path parent."""
        current = self.config_path.parent.absolute()
        
        # Look for .git directory
        while current != current.parent:
            if (current / '.git').exists():
                return current
            current = current.parent
        
        # Fallback to config file's parent directory
        return self.config_path.parent.absolute()
    
    def _resolve_metadata_paths(self, data_source_config: Dict) -> Dict:
        """
        Resolve meta-* file paths relative to config.yaml location.
        
        Validates paths to prevent directory traversal attacks.
        
        Args:
            data_source_config: Data source configuration from config.yaml
            
        Returns:
            Dictionary with resolved absolute paths for meta-* files
            
        Raises:
            ValueError: If path validation fails (directory traversal attempt)
        """
        config_dir = self.config_path.parent.absolute()
        resolved = {}
        
        # Meta file keys that should be resolved
        meta_keys = ['meta-global', 'meta-organisation', 'meta-organisation-roles']
        
        for key in meta_keys:
            if key in data_source_config:
                relative_path = data_source_config[key]
                
                # Resolve path relative to config.yaml location
                resolved_path = (config_dir / relative_path).resolve()
                
                # Validate: ensure resolved path is within or at config directory
                # This prevents directory traversal attacks
                try:
                    resolved_path.relative_to(config_dir)
                except ValueError:
                    # Path is outside config directory - potential directory traversal
                    raise ValueError(
                        f"ERROR ConfigManager: Invalid path for '{key}': {relative_path}\n"
                        f"  Context: Path resolves outside configuration directory\n"
                        f"  Resolved to: {resolved_path}\n"
                        f"  Config directory: {config_dir}\n"
                        f"  Suggestion: Use relative paths within the configuration directory. "
                        f"Absolute paths and paths with '..' that escape the config directory are not allowed."
                    )
                
                # Store as string for MetadataLoader
                resolved[key] = str(resolved_path)
        
        # Copy other data sources (like netbox) without modification
        for key, value in data_source_config.items():
            if key not in meta_keys:
                resolved[key] = value
        
        return resolved
    
    def _detect_old_format(self) -> Optional[str]:
        """
        Detect if old configuration format is being used.
        
        Checks for:
        1. Old metadata.yaml file in project root
        2. Old placeholder format in templates ({{ meta.organisation.name }})
        
        Returns:
            Error message if old format detected, None otherwise
        """
        errors = []
        
        # Check for old metadata.yaml file
        old_metadata_path = self.project_root / "metadata.yaml"
        if old_metadata_path.exists():
            errors.append(
                f"  - Old metadata.yaml file found at: {old_metadata_path}"
            )
        
        # Check for old placeholder format in templates
        templates_dir = self.project_root / "templates"
        if templates_dir.exists():
            old_placeholders_found = self._scan_for_old_placeholders(templates_dir)
            if old_placeholders_found:
                errors.append(
                    f"  - Old placeholder format detected in templates:"
                )
                for template_path, placeholders in old_placeholders_found[:5]:  # Show first 5
                    relative_path = template_path.relative_to(self.project_root)
                    errors.append(f"    * {relative_path}: {', '.join(placeholders[:3])}")
                
                if len(old_placeholders_found) > 5:
                    errors.append(f"    * ... and {len(old_placeholders_found) - 5} more files")
        
        if errors:
            return "\n".join(errors)
        
        return None
    
    def _scan_for_old_placeholders(self, templates_dir: Path) -> list[tuple[Path, list[str]]]:
        """
        Scan templates directory for old placeholder format.
        
        Old formats include:
        - {{ meta.organisation.name }}
        - {{ meta.document.owner }}
        - {{ meta.ceo.name }}
        
        Args:
            templates_dir: Path to templates directory
            
        Returns:
            List of tuples (template_path, list_of_old_placeholders)
        """
        import re
        
        # Pattern to match old placeholder formats
        # Matches: {{ meta.* }} or {{ metadata.* }} (but not meta-global, meta-organisation, etc.)
        old_placeholder_pattern = re.compile(r'\{\{\s*meta\.[\w.]+\s*\}\}')
        
        files_with_old_placeholders = []
        
        # Scan all .md files in templates directory
        for template_file in templates_dir.rglob("*.md"):
            try:
                content = template_file.read_text(encoding='utf-8')
                matches = old_placeholder_pattern.findall(content)
                
                if matches:
                    # Remove duplicates and keep unique placeholders
                    unique_placeholders = list(set(matches))
                    files_with_old_placeholders.append((template_file, unique_placeholders))
            except Exception:
                # Skip files that can't be read
                continue
        
        return files_with_old_placeholders
    
    def load_config(self) -> Config:
        """
        Load configuration from file.
        
        Loads config.yaml and all metadata files using the new metadata structure:
        - meta-global.yaml: Handbook Generator version and source
        - meta-organisation.yaml: Organization information
        - meta-organisation-roles.yaml: Personnel roles
        
        All meta-* file paths are resolved relative to config.yaml location.
        
        Returns:
            Config object with loaded configuration and unified metadata
            
        Raises:
            FileNotFoundError: If configuration file doesn't exist
            ValueError: If configuration is invalid or missing required fields
            yaml.YAMLError: If YAML syntax is invalid
        """
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Run with --create-config to generate a default configuration file."
            )
        
        # Detect old configuration format
        old_format_error = self._detect_old_format()
        if old_format_error:
            raise ValueError(
                f"\n{'='*80}\n"
                f"ERROR: Old configuration format detected\n"
                f"{'='*80}\n\n"
                f"The configuration format has changed. The following issues were found:\n\n"
                f"{old_format_error}\n\n"
                f"{'='*80}\n"
                f"REQUIRED ACTIONS:\n"
                f"{'='*80}\n\n"
                f"1. Create new configuration files:\n"
                f"   - config.yaml (with data_sources section)\n"
                f"   - meta-global.yaml (Handbook Generator version and source)\n"
                f"   - meta-organisation.yaml (organization information)\n"
                f"   - meta-organisation-roles.yaml (personnel roles)\n"
                f"   - meta-handbook.yaml (in each handbook directory)\n\n"
                f"2. Update all template placeholders to new format:\n"
                f"   Old: {{{{ meta.organisation.name }}}}\n"
                f"   New: {{{{ meta-organisation.name }}}}\n\n"
                f"3. Remove old metadata.yaml file after migration\n\n"
                f"{'='*80}\n"
                f"DOCUMENTATION:\n"
                f"{'='*80}\n\n"
                f"  Migration Guide:     docs/MIGRATION_GUIDE.md (if available)\n"
                f"  Configuration Ref:   docs/CONFIGURATION_REFERENCE.md\n"
                f"  Placeholder Ref:     docs/PLACEHOLDER_REFERENCE.md\n"
                f"  Example Files:       *.example.yaml\n\n"
                f"{'='*80}\n"
            )
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(
                f"Invalid YAML syntax in configuration file: {self.config_path}\n"
                f"Error: {e}"
            )
        
        if not config_data:
            raise ValueError(
                f"Configuration file is empty: {self.config_path}"
            )
        
        config = self._parse_config(config_data)
        
        # Load unified metadata using MetadataLoader
        # Extract data source configuration and resolve paths relative to config.yaml
        data_source_config = config_data.get('data_sources', {})
        resolved_data_sources = self._resolve_metadata_paths(data_source_config)
        
        # Create MetadataLoader with resolved paths
        metadata_loader = MetadataLoader(resolved_data_sources)
        
        try:
            # Load all global metadata
            config.unified_metadata = metadata_loader.load_all_metadata()
        except (ValueError, yaml.YAMLError) as e:
            print(f"WARNING: Error loading metadata: {e}")
            print(f"WARNING: Continuing with default metadata values.")
            # Create default unified metadata
            config.unified_metadata = UnifiedMetadata()
        
        return config
    
    def load_netbox_metadata(self, netbox_metadata_path: Optional[Path] = None) -> Optional[dict]:
        """
        Load NetBox metadata from metadata-netbox.yaml file.
        
        This file is generated by NetBoxMetadataLoader and contains
        contacts, devices, and sites fetched from NetBox.
        
        Args:
            netbox_metadata_path: Path to metadata-netbox.yaml file.
                                 If None, uses default path in project root.
        
        Returns:
            Dictionary with NetBox metadata, or None if file doesn't exist
            
        Raises:
            yaml.YAMLError: If YAML syntax is invalid
            ValueError: If metadata structure is invalid
        """
        if netbox_metadata_path is None:
            netbox_metadata_path = self.project_root / "metadata-netbox.yaml"
        else:
            netbox_metadata_path = Path(netbox_metadata_path)
        
        if not netbox_metadata_path.exists():
            print(f"INFO: metadata-netbox.yaml not found at {netbox_metadata_path}")
            print(f"INFO: NetBox metadata will not be available for placeholders.")
            return None
        
        try:
            with open(netbox_metadata_path, 'r', encoding='utf-8') as f:
                netbox_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(
                f"Invalid YAML syntax in NetBox metadata file: {netbox_metadata_path}\n"
                f"Error: {e}"
            )
        
        if not netbox_data:
            print(f"WARNING: NetBox metadata file is empty: {netbox_metadata_path}")
            return None
        
        # Validate basic structure
        if not isinstance(netbox_data, dict):
            raise ValueError(
                f"Invalid NetBox metadata structure: expected dictionary, "
                f"got {type(netbox_data).__name__}"
            )
        
        return netbox_data
    
    def _parse_config(self, config_data: dict) -> Config:
        """
        Parse configuration dictionary into Config object.
        
        Args:
            config_data: Dictionary loaded from YAML file
            
        Returns:
            Config object
            
        Raises:
            ValueError: If required fields are missing
        """
        # Parse data sources (skip meta-* entries as they're handled separately)
        data_sources = {}
        data_sources_raw = config_data.get('data_sources', {})
        
        # Meta file keys that should be skipped (not actual data sources)
        meta_keys = {'meta-global', 'meta-organisation', 'meta-organisation-roles'}
        
        for source_name, source_config in data_sources_raw.items():
            # Skip meta-* entries - they're metadata file paths, not data sources
            if source_name in meta_keys:
                continue
            
            if not isinstance(source_config, dict):
                raise ValueError(
                    f"Invalid configuration for data source '{source_name}': "
                    f"expected dictionary, got {type(source_config).__name__}"
                )
            
            url = source_config.get('url')
            api_token = source_config.get('api_token')
            role_distinction = source_config.get('role_distinction')
            
            if not url:
                raise ValueError(
                    f"Missing required field 'url' for data source '{source_name}'"
                )
            if not api_token:
                raise ValueError(
                    f"Missing required field 'api_token' for data source '{source_name}'"
                )
            
            data_sources[source_name] = DataSourceConfig(
                url=url,
                api_token=api_token,
                role_distinction=role_distinction
            )
        
        # Parse defaults
        defaults = config_data.get('defaults', {})
        default_language = defaults.get('language', 'de')
        default_output_format = defaults.get('output_format', 'both')
        
        # Parse metadata
        metadata = config_data.get('metadata', {})
        author = metadata.get('author', 'Andreas Huemmer [andreas.huemmer@adminsend.de]')
        # Import version from package
        from . import __version__
        version = metadata.get('version', __version__)
        
        return Config(
            data_sources=data_sources,
            default_language=default_language,
            default_output_format=default_output_format,
            author=author,
            version=version
        )
    
    def create_default_config(self) -> None:
        """
        Create default configuration file with example values.
        
        Raises:
            FileExistsError: If configuration file already exists
        """
        if self.config_path.exists():
            raise FileExistsError(
                f"Configuration file already exists: {self.config_path}\n"
                f"Delete it first if you want to create a new default configuration."
            )
        
        # Create parent directory if it doesn't exist
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write default configuration
        with open(self.config_path, 'w', encoding='utf-8') as f:
            f.write(self.DEFAULT_CONFIG_CONTENT)
        
        # Ensure it's in .gitignore
        self.ensure_gitignore()
    
    def ensure_gitignore(self) -> None:
        """
        Ensure configuration file is listed in .gitignore.
        
        Creates or updates .gitignore to include the configuration file.
        """
        gitignore_path = self.project_root / '.gitignore'
        config_relative = self.config_path.relative_to(self.project_root)
        gitignore_entry = str(config_relative)
        
        # Read existing .gitignore if it exists
        existing_entries = []
        if gitignore_path.exists():
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                existing_entries = [line.strip() for line in f.readlines()]
        
        # Check if config file is already in .gitignore
        if gitignore_entry in existing_entries:
            return
        
        # Add config file to .gitignore
        with open(gitignore_path, 'a', encoding='utf-8') as f:
            if existing_entries and not existing_entries[-1] == '':
                f.write('\n')
            f.write(f'# Handbook Generator configuration (contains sensitive credentials)\n')
            f.write(f'{gitignore_entry}\n')
    
    def ensure_metadata_file(self) -> None:
        """
        Ensure metadata.yaml exists in the same directory as config.yaml.
        
        Creates default metadata.yaml if it doesn't exist and informs the user.
        """
        metadata_path = self.config_path.parent / "metadata.yaml"
        
        if metadata_path.exists():
            print(f"INFO: metadata.yaml found at {metadata_path}")
            return
        
        print(f"INFO: metadata.yaml not found at {metadata_path}")
        print(f"INFO: Creating default metadata.yaml...")
        
        metadata_manager = MetadataConfigManager(metadata_path)
        
        try:
            metadata_manager.create_default_metadata()
            print(f"SUCCESS: Default metadata.yaml created at {metadata_path}")
            print(f"INFO: Please review and update with your organization's information.")
        except Exception as e:
            print(f"ERROR: Could not create default metadata.yaml: {e}")
            raise
    
    def validate_config(self, config: Config) -> Optional[str]:
        """
        Validate configuration and return error message if invalid.
        
        Args:
            config: Config object to validate
            
        Returns:
            Error message if validation fails, None otherwise
        """
        missing_fields = []
        invalid_fields = {}
        
        # Check if at least one data source is configured
        if not config.data_sources:
            missing_fields.append("data_sources (at least one data source required)")
        
        # Validate each data source
        for source_name, source_config in config.data_sources.items():
            if not source_config.url:
                missing_fields.append(f"data_sources.{source_name}.url")
            elif not source_config.url.startswith(('http://', 'https://')):
                invalid_fields[f"data_sources.{source_name}.url"] = "Must start with http:// or https://"
            
            if not source_config.api_token:
                missing_fields.append(f"data_sources.{source_name}.api_token")
            elif source_config.api_token == "your-api-token-here":
                invalid_fields[f"data_sources.{source_name}.api_token"] = "Replace with actual API token"
        
        # Validate output format
        valid_formats = ['markdown', 'pdf', 'both']
        if config.default_output_format not in valid_formats:
            invalid_fields["defaults.output_format"] = f"Must be one of: {', '.join(valid_formats)}"
        
        # Generate error message if there are issues
        if missing_fields or invalid_fields:
            return ErrorHandler.configuration_error(
                self.config_path,
                missing_fields,
                invalid_fields
            )
        
        return None
