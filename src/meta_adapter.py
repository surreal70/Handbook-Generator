"""
Meta Data Source Adapter for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

from typing import Optional
from src.data_source_adapter import DataSourceAdapter
from src.metadata_config_manager import MetadataConfig


class MetaAdapter(DataSourceAdapter):
    """
    Meta data source adapter for organization-wide metadata.
    
    Provides access to metadata from metadata.yaml configuration file.
    
    Example usage:
        adapter = MetaAdapter(metadata_config)
        adapter.connect()
        org_name = adapter.get_field("organization.name")
        ceo_email = adapter.get_field("ceo.email")
        adapter.disconnect()
    """
    
    # German to English role title translation mapping
    ROLE_TITLE_TRANSLATIONS = {
        'Datenschutzbeauftragter': 'Data Protection Officer',
        'Risikomanager': 'Risk Manager',
        'Interner Auditor': 'Internal Auditor',
        'Personalleitung': 'HR Manager',
        'Systemadministrator': 'System Administrator',
        'System Administrator': 'System Administrator',  # Already English
        'IT Manager': 'IT Manager',  # Already English
    }
    
    def __init__(self, metadata_config: MetadataConfig, language: str = 'de'):
        """
        Initialize Meta adapter with metadata configuration.
        
        Args:
            metadata_config: MetadataConfig object with organization metadata
            language: Language for role title translation ('de' or 'en')
        """
        self.metadata = metadata_config
        self.language = language
        self._connected = False
        
        # Service/Process type tracking attributes
        self._current_service_type = None
        self._current_process_type = None
        self._service_config = None
        self._process_config = None
        self._global_service_config = None
        self._global_process_config = None
        self._config_cache = {}  # Cache for loaded YAML files
    
    def connect(self) -> bool:
        """
        Validate metadata configuration (no external connection needed).
        
        Returns:
            True if metadata is valid, False otherwise
        """
        if self.metadata is None:
            return False
        
        # Validate that required fields are present
        if not self.metadata.organization or not self.metadata.organization.name:
            return False
        
        self._connected = True
        return True
    
    def disconnect(self) -> None:
        """
        No-op for meta adapter (no external connection to close).
        """
        self._connected = False
    
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Retrieve field value from metadata configuration.
        
        Supports dot-notation field paths:
        - "organization.name" -> metadata.organization.name
        - "organization.email" -> metadata.organization.email
        - "ceo.name" -> metadata.roles.ceo.name
        - "ceo.email" -> metadata.roles.ceo.email
        - "document.owner" -> metadata.document.owner
        - "handbook.version" -> metadata.handbooks[current_type].version
        - "handbook.owner" -> metadata.handbooks[current_type].owner
        - "handbook.approver" -> metadata.handbooks[current_type].approver
        - "handbook.date" -> metadata.handbooks[current_type].date
        - "author" -> metadata.author
        - "language" -> metadata.language
        
        Note: For handbook placeholders, set_handbook_type() must be called first.
        
        Args:
            field_path: Dot-separated path to the field
            
        Returns:
            Field value as string, or None if field not found
            
        Raises:
            ConnectionError: If not connected (metadata not validated)
            ValueError: If field_path is invalid
        """
        if not self._connected:
            raise ConnectionError("Not connected to metadata. Call connect() first.")
        
        if not field_path:
            raise ValueError("field_path cannot be empty")
        
        return self._resolve_field_path(field_path)
    
    def _resolve_field_path(self, field_path: str) -> Optional[str]:
        """
        Resolve dot-notation field path to metadata value.
        
        Resolution order (hierarchical):
        1. Service/Process-specific metadata (meta-service.yaml / meta-process.yaml)
        2. Global service/process config (meta-global-service.yaml / meta-global-process.yaml)
        3. Role references (meta-organisation-roles.yaml)
        4. Organisation metadata (meta-organisation.yaml)
        5. Global metadata (meta-global.yaml)
        
        Args:
            field_path: Dot-separated field path
            
        Returns:
            Field value as string, or None if not found
        """
        # Level 1: Try service-specific metadata first
        if field_path.startswith('service.'):
            if self._service_config:
                value = self._get_nested_value(self._service_config, field_path)
                if value is not None:
                    return str(value)
            
            # Level 2: Try global service config
            if self._global_service_config:
                value = self._get_nested_value(self._global_service_config, field_path)
                if value is not None:
                    return str(value)
            
            # Not found in service configs
            return None
        
        # Level 1: Try process-specific metadata first
        if field_path.startswith('process.'):
            if self._process_config:
                value = self._get_nested_value(self._process_config, field_path)
                if value is not None:
                    return str(value)
            
            # Level 2: Try global process config
            if self._global_process_config:
                value = self._get_nested_value(self._global_process_config, field_path)
                if value is not None:
                    return str(value)
            
            # Not found in process configs
            return None
        
        # Fall back to existing metadata resolution for non-service/process fields
        parts = field_path.split('.')
        
        # Handle top-level shortcuts
        if len(parts) == 1:
            field_name = parts[0]
            
            # Direct metadata fields
            if field_name == 'author':
                return self.metadata.author
            elif field_name == 'language':
                return self.metadata.language
            else:
                # Try as role name (e.g., "ceo" -> "ceo.name")
                role = self.metadata.get_role(field_name)
                if role:
                    return role.name
                return None
        
        # Handle nested paths
        base_field = parts[0]
        sub_path = '.'.join(parts[1:])
        
        # Organization fields
        if base_field == 'organization':
            return self._get_organization_field(sub_path)
        
        # Document fields
        elif base_field == 'document':
            return self._get_document_field(sub_path)
        
        # Handbook fields (per-handbook versioning)
        elif base_field == 'handbook':
            return self._get_handbook_field(sub_path)
        
        # Role fields (e.g., "ceo.email", "ciso.phone")
        else:
            return self._get_role_field(base_field, sub_path)
    
    def _get_organization_field(self, field_name: str) -> Optional[str]:
        """Get organization field value."""
        if not self.metadata.organization:
            return None
        
        field_mapping = {
            'name': self.metadata.organization.name,
            'address': self.metadata.organization.address,
            'city': self.metadata.organization.city,
            'postal_code': self.metadata.organization.postal_code,
            'country': self.metadata.organization.country,
            'website': self.metadata.organization.website,
            'phone': self.metadata.organization.phone,
            'email': self.metadata.organization.email
        }
        
        return field_mapping.get(field_name)
    
    def _get_document_field(self, field_name: str) -> Optional[str]:
        """Get document field value."""
        if not self.metadata.document:
            return None
        
        field_mapping = {
            'owner': self.metadata.document.owner,
            'approver': self.metadata.document.approver,
            'version': self.metadata.document.version,
            'classification': self.metadata.document.classification
        }
        
        return field_mapping.get(field_name)
    
    def _get_role_field(self, role_name: str, field_name: str) -> Optional[str]:
        """Get role field value."""
        role = self.metadata.get_role(role_name)
        if not role:
            return None
        
        # Get the field value
        field_mapping = {
            'name': role.name,
            'title': role.title,
            'email': role.email,
            'phone': role.phone,
            'department': role.department
        }
        
        value = field_mapping.get(field_name)
        
        # Apply translation for title field in English templates
        if field_name == 'title' and value and self.language == 'en':
            value = self.ROLE_TITLE_TRANSLATIONS.get(value, value)
        
        return value
    
    def _get_handbook_field(self, field_name: str) -> Optional[str]:
        """
        Get handbook field value.
        
        Note: This method requires the handbook type to be set via set_handbook_type()
        before calling get_field() with handbook placeholders.
        
        Args:
            field_name: Field name (version, owner, approver, date)
            
        Returns:
            Field value as string, or None if not found
        """
        # Check if handbook type is set
        if not hasattr(self, '_current_handbook_type') or not self._current_handbook_type:
            return None
        
        # Get handbook metadata for current type
        handbook_info = self.metadata.get_handbook_metadata(self._current_handbook_type)
        if not handbook_info:
            return None
        
        field_mapping = {
            'version': handbook_info.version,
            'owner': handbook_info.owner,
            'approver': handbook_info.approver,
            'date': handbook_info.date
        }
        
        return field_mapping.get(field_name)
    
    def set_handbook_type(self, handbook_type: str) -> None:
        """
        Set the current handbook type for handbook placeholder resolution.
        
        This must be called before processing templates with {{ handbook.* }} placeholders.
        
        Args:
            handbook_type: Type of handbook (bcm, isms, bsi-grundschutz, it-operation)
        """
        self._current_handbook_type = handbook_type

    def set_service_type(self, service_name: str, language: str) -> None:
        """
        Set current service type for service-specific metadata.
        
        This method loads service-specific and global service configurations
        to enable hierarchical placeholder resolution for service templates.
        
        Args:
            service_name: Name of the service (e.g., 'generic-service-template')
            language: Language code ('de' or 'en')
        """
        from pathlib import Path
        import yaml
        
        self._current_service_type = service_name
        
        # Load service-specific metadata
        service_metadata_path = Path(f'services/{language}/{service_name}/meta-service.yaml')
        if service_metadata_path.exists():
            self._service_config = self._load_yaml_cached(service_metadata_path)
        else:
            self._service_config = None
        
        # Load global service config
        global_service_config_path = Path(f'services/{language}/meta-global-service.yaml')
        if global_service_config_path.exists():
            self._global_service_config = self._load_yaml_cached(global_service_config_path)
        else:
            self._global_service_config = None

    def set_process_type(self, process_name: str, language: str) -> None:
        """
        Set current process type for process-specific metadata.
        
        This method loads process-specific and global process configurations
        to enable hierarchical placeholder resolution for process templates.
        
        Args:
            process_name: Name of the process (e.g., 'generic-process-template')
            language: Language code ('de' or 'en')
        """
        from pathlib import Path
        import yaml
        
        self._current_process_type = process_name
        
        # Load process-specific metadata
        process_metadata_path = Path(f'processes/{language}/{process_name}/meta-process.yaml')
        if process_metadata_path.exists():
            self._process_config = self._load_yaml_cached(process_metadata_path)
        else:
            self._process_config = None
        
        # Load global process config
        global_process_config_path = Path(f'processes/{language}/meta-global-process.yaml')
        if global_process_config_path.exists():
            self._global_process_config = self._load_yaml_cached(global_process_config_path)
        else:
            self._global_process_config = None

    def _get_nested_value(self, config: dict, field_path: str) -> Optional[any]:
        """
        Get nested value from config dictionary using dot-notation path.
        
        Args:
            config: Configuration dictionary
            field_path: Dot-separated path to the field (e.g., 'service.sla.availability_target')
            
        Returns:
            Field value, or None if not found
        """
        parts = field_path.split('.')
        current = config
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        
        return current

    def _load_yaml_cached(self, path) -> Optional[dict]:
        """
        Load YAML file with caching for performance.
        
        Args:
            path: Path object to YAML file
            
        Returns:
            Parsed YAML content as dictionary, or None if file doesn't exist or parsing fails
        """
        from pathlib import Path
        import yaml
        
        # Convert to Path if string
        if isinstance(path, str):
            path = Path(path)
        
        cache_key = str(path)
        
        # Return cached value if available
        if cache_key in self._config_cache:
            return self._config_cache[cache_key]
        
        # Check if file exists
        if not path.exists():
            return None
        
        # Load and cache the YAML file
        try:
            with open(path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                self._config_cache[cache_key] = config
                return config
        except yaml.YAMLError as e:
            # Log error but don't crash - return None
            return None
        except Exception as e:
            # Log error but don't crash - return None
            return None
