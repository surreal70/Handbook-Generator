"""
Unified metadata data models for configuration separation.

This module provides data classes for different metadata sources:
- GlobalMetadata: Handbook Generator version and source information
- OrganisationMetadata: Organization-specific information
- RolesMetadata: Personnel roles and contact information
- HandbookMetadata: Individual handbook metadata
- UnifiedMetadata: Unified access to all metadata sources
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GlobalMetadata:
    """Global metadata for Handbook Generator."""
    source: str = "HandBook Generator"
    version: str = "1.0.0"


@dataclass
class OrganisationMetadata:
    """Organization-specific metadata."""
    name: str = "[TODO]"
    address: str = "[TODO]"
    web: str = "[TODO]"
    phone: str = "[TODO]"
    revision: int = 0


@dataclass
class RolesMetadata:
    """Personnel roles and contact information."""
    role_CEO: str = "[TODO]"
    role_CFO: str = "[TODO]"
    role_CTO: str = "[TODO]"
    role_CIO: str = "[TODO]"
    role_CISO: str = "[TODO]"
    role_HR_Manager: str = "[TODO]"
    role_Risk_Manager: str = "[TODO]"
    role_GDPR_Manager: str = "[TODO]"
    role_IT_Manager: str = "[TODO]"
    role_Compliance_Manager: str = "[TODO]"
    role_Internal_Auditor: str = "[TODO]"
    group_IT_Services: str = "[TODO]"
    group_DEVOPS: str = "[TODO]"
    group_Helpdesk: str = "[TODO]"


@dataclass
class HandbookMetadata:
    """Individual handbook metadata."""
    author: str = "[TODO]"
    classification: str = "[TODO]"
    status: str = "[TODO]"
    type: str = "[TODO]"
    templateset_version: str = "0.1"
    revision: int = 0
    shortname: str = "[TODO]"
    longname: str = "[TODO]"
    maintainer: Optional[str] = None
    owner: str = "[TODO]"
    approver: str = "[TODO]"
    creationdate: str = "[TODO]"
    modifydate: str = "[TODO]"
    valid_from: str = "[TODO]"
    next_review: str = "[TODO]"
    scope: str = "[TODO]"
    
    def __post_init__(self):
        """Set maintainer to author if not specified."""
        if self.maintainer is None:
            self.maintainer = self.author


@dataclass
class UnifiedMetadata:
    """Unified access to all metadata sources."""
    global_info: GlobalMetadata = field(default_factory=GlobalMetadata)
    organisation: OrganisationMetadata = field(default_factory=OrganisationMetadata)
    roles: RolesMetadata = field(default_factory=RolesMetadata)
    handbook: Optional[HandbookMetadata] = None
    
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Get field value by path (e.g., 'meta-organisation.name').
        
        Supports paths like:
        - meta-global.version
        - meta-organisation.name
        - meta-organisation-roles.role_CEO
        - meta-handbook.author
        
        Args:
            field_path: Dot-separated path to field (e.g., 'meta-organisation.name')
            
        Returns:
            Field value as string, or None if not found
        """
        parts = field_path.split('.')
        if len(parts) < 2:
            return None
        
        source = parts[0]
        field = '.'.join(parts[1:])
        
        if source == 'meta-global':
            return self._get_nested_field(self.global_info, field)
        elif source == 'meta-organisation':
            return self._get_nested_field(self.organisation, field)
        elif source == 'meta-organisation-roles':
            return self._get_nested_field(self.roles, field)
        elif source == 'meta-handbook':
            if self.handbook is None:
                return None
            return self._get_nested_field(self.handbook, field)
        
        return None
    
    def _get_nested_field(self, obj, field_path: str):
        """
        Get nested field from object using dot notation.
        
        Args:
            obj: Object to get field from
            field_path: Dot-separated field path
            
        Returns:
            Field value, or None if not found
        """
        current = obj
        for part in field_path.split('.'):
            if hasattr(current, part):
                current = getattr(current, part)
            else:
                return None
        return current
