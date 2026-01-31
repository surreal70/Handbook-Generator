"""
Meta Data Source Adapter for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
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
    
    def __init__(self, metadata_config: MetadataConfig):
        """
        Initialize Meta adapter with metadata configuration.
        
        Args:
            metadata_config: MetadataConfig object with organization metadata
        """
        self.metadata = metadata_config
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
        - "author" -> metadata.author
        - "language" -> metadata.language
        
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
        
        field_mapping = {
            'name': role.name,
            'title': role.title,
            'email': role.email,
            'phone': role.phone,
            'department': role.department
        }
        
        return field_mapping.get(field_name)
