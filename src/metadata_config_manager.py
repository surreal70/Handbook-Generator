"""
Metadata Configuration Manager for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional, Dict
import re
import yaml


class Classification(Enum):
    """Document classification levels."""
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"


@dataclass
class OrganizationInfo:
    """
    Organization information for metadata.
    
    Attributes:
        name: Organization name
        address: Street address
        city: City name
        postal_code: Postal/ZIP code
        country: Country name
        website: Organization website URL
        phone: Contact phone number
        email: Contact email address
    """
    name: str
    address: str
    city: str
    postal_code: str
    country: str
    website: str
    phone: str
    email: str
    
    def __post_init__(self):
        """Validate organization info after initialization."""
        # Validate email format
        if not self._is_valid_email(self.email):
            raise ValueError(f"Invalid email format: {self.email}")
        
        # Validate phone format (basic check)
        if not self._is_valid_phone(self.phone):
            raise ValueError(f"Invalid phone format: {self.phone}")
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Validate email address format."""
        if not email:
            return False
        # Basic email validation regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def _is_valid_phone(phone: str) -> bool:
        """Validate phone number format (basic check)."""
        if not phone:
            return False
        # Allow digits, spaces, hyphens, parentheses, and plus sign
        pattern = r'^[\d\s\-\(\)\+]+$'
        return bool(re.match(pattern, phone)) and len(phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')) >= 7


@dataclass
class PersonRole:
    """
    Person role information for metadata.
    
    Attributes:
        name: Person's full name
        title: Job title
        email: Email address
        phone: Phone number
        department: Department name (optional)
    """
    name: str
    title: str
    email: str
    phone: str
    department: Optional[str] = None
    
    def __post_init__(self):
        """Validate person role after initialization."""
        # Validate email format
        if not self._is_valid_email(self.email):
            raise ValueError(f"Invalid email format for {self.name}: {self.email}")
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Validate email address format."""
        if not email:
            return False
        # Basic email validation regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))


@dataclass
class DocumentInfo:
    """
    Document information for metadata.
    
    Attributes:
        owner: Document owner name
        approver: Document approver name
        version: Document version (e.g., "1.0.0")
        classification: Document classification level
    """
    owner: str
    approver: str
    version: str
    classification: str
    
    def __post_init__(self):
        """Validate document info after initialization."""
        # Validate classification
        valid_classifications = [c.value for c in Classification]
        if self.classification not in valid_classifications:
            raise ValueError(
                f"Invalid classification: {self.classification}. "
                f"Must be one of: {', '.join(valid_classifications)}"
            )


@dataclass
class MetadataConfig:
    """
    Main metadata configuration class.
    
    Attributes:
        organization: Organization information
        roles: Dictionary of person roles (role_name -> PersonRole)
        document: Document information
        author: Default author name
        language: Default language code
    """
    organization: OrganizationInfo
    roles: Dict[str, PersonRole]
    document: DocumentInfo
    author: str
    language: str
    
    def get_role(self, role_name: str) -> Optional[PersonRole]:
        """
        Get role by name (case-insensitive).
        
        Args:
            role_name: Name of the role (e.g., "ceo", "CIO", "CISO")
            
        Returns:
            PersonRole object if found, None otherwise
        """
        # Convert to lowercase for case-insensitive lookup
        role_name_lower = role_name.lower()
        
        # Try direct lookup
        if role_name_lower in self.roles:
            return self.roles[role_name_lower]
        
        # Try case-insensitive search
        for key, value in self.roles.items():
            if key.lower() == role_name_lower:
                return value
        
        return None


class MetadataConfigManager:
    """
    Manages metadata configuration file loading, creation, and validation.
    
    Handles YAML parsing for metadata.yaml, default configuration generation,
    and validation of metadata structure.
    """
    
    def __init__(self, metadata_path: Path = Path("metadata.yaml")):
        """
        Initialize MetadataConfigManager with metadata file path.
        
        Args:
            metadata_path: Path to the metadata configuration file
        """
        self.metadata_path = Path(metadata_path)
    
    def load_metadata(self) -> MetadataConfig:
        """
        Load metadata configuration from file.
        
        Returns:
            MetadataConfig object with loaded configuration
            
        Raises:
            FileNotFoundError: If metadata file doesn't exist
            ValueError: If metadata is invalid or missing required fields
            yaml.YAMLError: If YAML syntax is invalid
        """
        if not self.metadata_path.exists():
            raise FileNotFoundError(
                f"Metadata configuration file not found: {self.metadata_path}\n"
                f"Run create_default_metadata() to generate a default configuration file."
            )
        
        try:
            with open(self.metadata_path, 'r', encoding='utf-8') as f:
                metadata_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(
                f"Invalid YAML syntax in metadata file: {self.metadata_path}\n"
                f"Error: {e}"
            )
        
        if not metadata_data:
            raise ValueError(
                f"Metadata file is empty: {self.metadata_path}"
            )
        
        return self._parse_metadata(metadata_data)
    
    def _parse_metadata(self, metadata_data: dict) -> MetadataConfig:
        """
        Parse metadata dictionary into MetadataConfig object.
        
        Args:
            metadata_data: Dictionary loaded from YAML file
            
        Returns:
            MetadataConfig object
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        # Parse organization
        org_data = metadata_data.get('organization', {})
        if not org_data:
            raise ValueError("Missing required section 'organization' in metadata.yaml")
        
        try:
            organization = OrganizationInfo(
                name=org_data.get('name', ''),
                address=org_data.get('address', ''),
                city=org_data.get('city', ''),
                postal_code=org_data.get('postal_code', ''),
                country=org_data.get('country', ''),
                website=org_data.get('website', ''),
                phone=org_data.get('phone', ''),
                email=org_data.get('email', '')
            )
        except ValueError as e:
            raise ValueError(f"Invalid organization data: {e}")
        
        # Parse roles
        roles_data = metadata_data.get('roles', {})
        roles = {}
        
        for role_name, role_data in roles_data.items():
            if not isinstance(role_data, dict):
                raise ValueError(
                    f"Invalid configuration for role '{role_name}': "
                    f"expected dictionary, got {type(role_data).__name__}"
                )
            
            try:
                roles[role_name.lower()] = PersonRole(
                    name=role_data.get('name', ''),
                    title=role_data.get('title', ''),
                    email=role_data.get('email', ''),
                    phone=role_data.get('phone', ''),
                    department=role_data.get('department')
                )
            except ValueError as e:
                raise ValueError(f"Invalid data for role '{role_name}': {e}")
        
        # Parse document
        doc_data = metadata_data.get('document', {})
        if not doc_data:
            raise ValueError("Missing required section 'document' in metadata.yaml")
        
        try:
            document = DocumentInfo(
                owner=doc_data.get('owner', ''),
                approver=doc_data.get('approver', ''),
                version=doc_data.get('version', '0.0.1'),
                classification=doc_data.get('classification', 'internal')
            )
        except ValueError as e:
            raise ValueError(f"Invalid document data: {e}")
        
        # Parse defaults
        defaults = metadata_data.get('defaults', {})
        author = defaults.get('author', 'Andreas Huemmer [andreas.huemmer@adminsend.de]')
        language = defaults.get('language', 'de')
        
        return MetadataConfig(
            organization=organization,
            roles=roles,
            document=document,
            author=author,
            language=language
        )


    DEFAULT_METADATA_CONTENT = """# Global Metadata Configuration
# This file contains organization-wide information used across all handbooks

organization:
  name: "AdminSend GmbH"
  address: "Musterstraße 123"
  city: "München"
  postal_code: "80331"
  country: "Deutschland"
  website: "https://www.adminsend.de"
  phone: "+49 89 12345678"
  email: "info@adminsend.de"

roles:
  ceo:
    name: "Max Mustermann"
    title: "Chief Executive Officer"
    email: "max.mustermann@adminsend.de"
    phone: "+49 89 12345678-100"
    department: "Management"
    
  cio:
    name: "Anna Schmidt"
    title: "Chief Information Officer"
    email: "anna.schmidt@adminsend.de"
    phone: "+49 89 12345678-200"
    department: "IT"
    
  ciso:
    name: "Thomas Weber"
    title: "Chief Information Security Officer"
    email: "thomas.weber@adminsend.de"
    phone: "+49 89 12345678-300"
    department: "IT Security"
    
  cfo:
    name: "Maria Müller"
    title: "Chief Financial Officer"
    email: "maria.mueller@adminsend.de"
    phone: "+49 89 12345678-400"
    department: "Finance"
    
  coo:
    name: "Peter Fischer"
    title: "Chief Operating Officer"
    email: "peter.fischer@adminsend.de"
    phone: "+49 89 12345678-500"
    department: "Operations"
    
  it_operations_manager:
    name: "Andreas Huemmer"
    title: "IT Operations Manager"
    email: "andreas.huemmer@adminsend.de"
    phone: "+49 89 12345678-250"
    department: "IT Operations"
    
  service_desk_lead:
    name: "Julia Becker"
    title: "Service Desk Lead"
    email: "julia.becker@adminsend.de"
    phone: "+49 89 12345678-111"
    department: "Service Desk"

document:
  owner: "IT Operations Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"  # public, internal, confidential, restricted

defaults:
  author: "Andreas Huemmer [andreas.huemmer@adminsend.de]"
  language: "de"
"""
    
    def create_default_metadata(self) -> None:
        """
        Create default metadata.yaml file with example values.
        
        Raises:
            FileExistsError: If metadata file already exists
        """
        if self.metadata_path.exists():
            raise FileExistsError(
                f"Metadata file already exists: {self.metadata_path}\n"
                f"Delete it first if you want to create a new default configuration."
            )
        
        # Create parent directory if it doesn't exist
        self.metadata_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write default metadata
        with open(self.metadata_path, 'w', encoding='utf-8') as f:
            f.write(self.DEFAULT_METADATA_CONTENT)


    def validate_metadata(self, metadata: MetadataConfig) -> list[str]:
        """
        Validate metadata configuration and return warnings.
        
        Args:
            metadata: MetadataConfig object to validate
            
        Returns:
            List of warning messages (empty if no issues)
        """
        warnings = []
        
        # Check required fields
        if not metadata.organization.name:
            warnings.append("Missing required field: organization.name")
        
        if not metadata.document.owner:
            warnings.append("Missing required field: document.owner")
        
        # Validate email addresses
        if metadata.organization.email:
            if not OrganizationInfo._is_valid_email(metadata.organization.email):
                warnings.append(f"Invalid organization email: {metadata.organization.email}")
        
        # Check for standard roles
        standard_roles = ['ceo', 'cio', 'ciso', 'cfo', 'coo']
        for role in standard_roles:
            if role not in metadata.roles:
                warnings.append(f"Missing standard role: {role}")
        
        # Validate role emails
        for role_name, role in metadata.roles.items():
            if not role.email:
                warnings.append(f"Missing email for role: {role_name}")
            elif not PersonRole._is_valid_email(role.email):
                warnings.append(f"Invalid email for role {role_name}: {role.email}")
            
            if not role.name:
                warnings.append(f"Missing name for role: {role_name}")
        
        return warnings
