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


@dataclass
class DataSourceConfig:
    """Configuration for a single data source."""
    url: str
    api_token: str


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
        metadata: Optional metadata configuration for organization-wide information
    """
    data_sources: Dict[str, DataSourceConfig] = field(default_factory=dict)
    default_language: str = "de"
    default_output_format: str = "both"
    author: str = "Andreas Huemmer [andreas.huemmer@adminsend.de]"
    version: str = "0.0.1"
    metadata: Optional[MetadataConfig] = None
    
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
    
    def load_config(self) -> Config:
        """
        Load configuration from file.
        
        Also attempts to load metadata.yaml from the same directory.
        If metadata.yaml doesn't exist, creates a default one.
        
        Returns:
            Config object with loaded configuration
            
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
        
        # Load metadata.yaml from the same directory
        metadata_path = self.config_path.parent / "metadata.yaml"
        metadata_manager = MetadataConfigManager(metadata_path)
        
        try:
            config.metadata = metadata_manager.load_metadata()
        except FileNotFoundError:
            # metadata.yaml doesn't exist - create default
            print(f"INFO: metadata.yaml not found at {metadata_path}")
            print(f"INFO: Creating default metadata.yaml...")
            try:
                metadata_manager.create_default_metadata()
                print(f"INFO: Default metadata.yaml created at {metadata_path}")
                print(f"INFO: Please review and update with your organization's information.")
                # Load the newly created default metadata
                config.metadata = metadata_manager.load_metadata()
            except Exception as e:
                print(f"WARNING: Could not create default metadata.yaml: {e}")
                print(f"WARNING: Continuing without metadata configuration.")
                config.metadata = None
        except (ValueError, yaml.YAMLError) as e:
            print(f"WARNING: Error loading metadata.yaml: {e}")
            print(f"WARNING: Continuing without metadata configuration.")
            config.metadata = None
        
        return config
    
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
        # Parse data sources
        data_sources = {}
        data_sources_raw = config_data.get('data_sources', {})
        
        for source_name, source_config in data_sources_raw.items():
            if not isinstance(source_config, dict):
                raise ValueError(
                    f"Invalid configuration for data source '{source_name}': "
                    f"expected dictionary, got {type(source_config).__name__}"
                )
            
            url = source_config.get('url')
            api_token = source_config.get('api_token')
            
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
                api_token=api_token
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
