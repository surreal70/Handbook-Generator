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
        
        Args:
            field_path: Dot-separated field path
            
        Returns:
            Field value as string, or None if not found
        """
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
