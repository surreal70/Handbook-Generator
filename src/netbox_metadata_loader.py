"""
NetBox Metadata Loader for Handbook Generator

Fetches metadata from NetBox and populates metadata-netbox.yaml file.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from typing import Dict, Optional, Any
from pathlib import Path
import yaml
import pynetbox
from src.error_handler import ErrorHandler


class NetBoxMetadataLoader:
    """
    Loads metadata from NetBox and creates metadata-netbox.yaml.
    
    Fetches contacts, devices, and sites from NetBox API and saves them
    to a YAML file for use in template processing.
    
    Example usage:
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "api-token-here",
            {"method": "field", "field": "role"}
        )
        metadata = loader.load_metadata()
        loader.save_to_yaml(metadata, "metadata-netbox.yaml")
    """
    
    def __init__(self, netbox_url: str, api_token: str, role_config: Dict[str, Any]):
        """
        Initialize NetBox metadata loader.
        
        Args:
            netbox_url: URL of NetBox instance
            api_token: API token for authentication
            role_config: Configuration for role distinction
                - method: "field" or "name"
                - field: field name if method is "field" (e.g., "role")
                - mappings: dict of role mappings
        """
        self.netbox_url = netbox_url
        self.api_token = api_token
        self.role_config = role_config
        self.api: Optional[pynetbox.api] = None
    
    def load_metadata(self) -> Dict[str, Any]:
        """
        Load all metadata from NetBox.
        
        Returns:
            Dictionary with contacts, devices, sites
            
        Raises:
            ConnectionError: If connection to NetBox fails
        """
        # Connect to NetBox
        try:
            self.api = pynetbox.api(self.netbox_url, token=self.api_token)
            # Test connection
            self.api.version
        except pynetbox.RequestError as e:
            status_code = getattr(e, 'status_code', None) if hasattr(e, 'status_code') else None
            error_msg = ErrorHandler.api_connection_error(
                "NetBox", self.netbox_url, status_code, str(e)
            )
            raise ConnectionError(error_msg)
        except Exception as e:
            error_msg = ErrorHandler.api_connection_error(
                "NetBox", self.netbox_url, None, str(e)
            )
            raise ConnectionError(error_msg)
        
        # Fetch metadata
        metadata = {
            'contacts': self.fetch_contacts_with_roles(),
            'devices': self.fetch_devices(),
            'sites': self.fetch_sites()
        }
        
        return metadata
    
    def fetch_contacts_with_roles(self) -> Dict[str, Dict[str, str]]:
        """
        Fetch contacts from NetBox and assign roles.
        
        Returns:
            Dictionary mapping roles to contact information
            Example:
                {
                    'ciso': {'name': 'John Doe', 'email': 'john@example.com', 'phone': '+1234567890'},
                    'cio': {'name': 'Jane Smith', 'email': 'jane@example.com', 'phone': '+0987654321'}
                }
        """
        if not self.api:
            return {}
        
        try:
            # Fetch all contacts from NetBox
            # Note: NetBox 3.x uses tenancy.contacts
            contacts_raw = self.api.tenancy.contacts.all()
            
            contacts_by_role = {}
            
            for contact in contacts_raw:
                # Apply role distinction logic
                role = self._determine_role(contact)
                
                if role:
                    # Extract contact information
                    contact_info = {
                        'name': str(contact.name) if hasattr(contact, 'name') and contact.name else '',
                        'email': str(contact.email) if hasattr(contact, 'email') and contact.email else '',
                        'phone': str(contact.phone) if hasattr(contact, 'phone') and contact.phone else ''
                    }
                    
                    contacts_by_role[role] = contact_info
            
            return contacts_by_role
            
        except Exception as e:
            print(f"Warning: Could not fetch contacts from NetBox: {e}")
            return {}
    
    def fetch_devices(self) -> Dict[str, Dict[str, Any]]:
        """
        Fetch device information from NetBox.
        
        Returns:
            Dictionary with device data
            Example:
                {
                    'firewall': {'name': 'fw01', 'ip': '192.168.1.1', 'site': 'HQ'},
                    'switch': {'name': 'sw01', 'ip': '192.168.1.2', 'site': 'HQ'}
                }
        """
        if not self.api:
            return {}
        
        try:
            devices_raw = self.api.dcim.devices.all()
            
            devices = {}
            
            for device in devices_raw:
                device_name = str(device.name) if hasattr(device, 'name') and device.name else ''
                
                if device_name:
                    device_info = {
                        'name': device_name,
                        'ip': str(device.primary_ip) if hasattr(device, 'primary_ip') and device.primary_ip else '',
                        'site': str(device.site.name) if hasattr(device, 'site') and device.site and hasattr(device.site, 'name') else '',
                        'role': str(device.device_role.name) if hasattr(device, 'device_role') and device.device_role and hasattr(device.device_role, 'name') else '',
                        'status': str(device.status) if hasattr(device, 'status') and device.status else ''
                    }
                    
                    # Use device name as key (lowercase, replace spaces with underscores)
                    key = device_name.lower().replace(' ', '_').replace('-', '_')
                    devices[key] = device_info
            
            return devices
            
        except Exception as e:
            print(f"Warning: Could not fetch devices from NetBox: {e}")
            return {}
    
    def fetch_sites(self) -> Dict[str, Dict[str, Any]]:
        """
        Fetch site information from NetBox.
        
        Returns:
            Dictionary with site data
            Example:
                {
                    'hq': {'name': 'Headquarters', 'address': '123 Main St', 'city': 'New York'},
                    'branch': {'name': 'Branch Office', 'address': '456 Oak Ave', 'city': 'Boston'}
                }
        """
        if not self.api:
            return {}
        
        try:
            sites_raw = self.api.dcim.sites.all()
            
            sites = {}
            
            for site in sites_raw:
                site_name = str(site.name) if hasattr(site, 'name') and site.name else ''
                
                if site_name:
                    site_info = {
                        'name': site_name,
                        'address': str(site.physical_address) if hasattr(site, 'physical_address') and site.physical_address else '',
                        'description': str(site.description) if hasattr(site, 'description') and site.description else '',
                        'status': str(site.status) if hasattr(site, 'status') and site.status else ''
                    }
                    
                    # Use site name as key (lowercase, replace spaces with underscores)
                    key = site_name.lower().replace(' ', '_').replace('-', '_')
                    sites[key] = site_info
            
            return sites
            
        except Exception as e:
            print(f"Warning: Could not fetch sites from NetBox: {e}")
            return {}
    
    def _determine_role(self, contact: Any) -> Optional[str]:
        """
        Determine role for a contact based on configured role distinction method.
        
        Args:
            contact: NetBox contact object
            
        Returns:
            Role name (lowercase), or None if role cannot be determined
        """
        method = self.role_config.get('method', 'field')
        mappings = self.role_config.get('mappings', {})
        
        if method == 'field':
            # Field-based role mapping
            field_name = self.role_config.get('field', 'role')
            
            # Get field value from contact
            field_value = None
            if hasattr(contact, field_name):
                field_value = getattr(contact, field_name)
            elif hasattr(contact, 'custom_fields') and isinstance(contact.custom_fields, dict):
                field_value = contact.custom_fields.get(field_name)
            
            if field_value:
                field_value_str = str(field_value)
                
                # Check mappings
                for role_key, role_pattern in mappings.items():
                    if field_value_str.lower() == role_pattern.lower():
                        return role_key.lower()
                
                # If no mapping found, use field value directly (lowercase)
                return field_value_str.lower().replace(' ', '_').replace('-', '_')
        
        elif method == 'name':
            # Name-based role mapping
            contact_name = str(contact.name) if hasattr(contact, 'name') and contact.name else ''
            
            if contact_name:
                # Check mappings
                for role_key, role_pattern in mappings.items():
                    if role_pattern.lower() in contact_name.lower():
                        return role_key.lower()
        
        return None
    
    def save_to_yaml(self, metadata: Dict[str, Any], filepath: str) -> None:
        """
        Save metadata to YAML file.
        
        Args:
            metadata: Metadata dictionary
            filepath: Path to metadata-netbox.yaml
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            filepath_obj = Path(filepath)
            
            # Create parent directory if it doesn't exist
            filepath_obj.parent.mkdir(parents=True, exist_ok=True)
            
            # Write YAML file
            with open(filepath_obj, 'w', encoding='utf-8') as f:
                f.write("# NetBox Metadata - Auto-generated\n")
                f.write("# This file is automatically generated from NetBox data\n")
                f.write("# Do not edit manually - changes will be overwritten\n\n")
                yaml.dump(metadata, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            
            print(f"INFO: NetBox metadata saved to {filepath}")
            
        except Exception as e:
            raise IOError(f"Failed to save metadata to {filepath}: {e}")
