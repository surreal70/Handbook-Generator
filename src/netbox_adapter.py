"""
NetBox Data Source Adapter for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

from typing import Optional
import pynetbox
from src.data_source_adapter import DataSourceAdapter
from src.error_handler import ErrorHandler


class NetBoxAdapter(DataSourceAdapter):
    """
    NetBox data source adapter using pynetbox library.
    
    Provides access to NetBox DCIM and IPAM data through the NetBox REST API.
    
    Example usage:
        adapter = NetBoxAdapter("https://netbox.example.com", "api-token-here")
        adapter.connect()
        device_name = adapter.get_field("device_name")
        adapter.disconnect()
        
    Or with context manager:
        with NetBoxAdapter("https://netbox.example.com", "api-token-here") as adapter:
            device_name = adapter.get_field("device_name")
    """
    
    def __init__(self, url: str, api_token: str):
        """
        Initialize NetBox adapter.
        
        Args:
            url: NetBox instance URL (e.g., "https://netbox.example.com")
            api_token: NetBox API authentication token
        """
        self.url = url
        self.api_token = api_token
        self.api: Optional[pynetbox.api] = None
        self._connected = False
    
    def connect(self) -> bool:
        """
        Establish connection to NetBox API.
        
        Returns:
            True if connection successful, False otherwise
            
        Raises:
            ConnectionError: If connection cannot be established
            AuthenticationError: If API token is invalid
        """
        try:
            self.api = pynetbox.api(self.url, token=self.api_token)
            
            # Test connection by making a simple API call
            # This will raise an exception if authentication fails
            self.api.version
            
            self._connected = True
            return True
            
        except pynetbox.RequestError as e:
            self._connected = False
            # Extract status code if available
            status_code = getattr(e, 'status_code', None) if hasattr(e, 'status_code') else None
            error_msg = ErrorHandler.api_connection_error(
                "NetBox", self.url, status_code, str(e)
            )
            raise ConnectionError(error_msg)
        except Exception as e:
            self._connected = False
            error_msg = ErrorHandler.api_connection_error(
                "NetBox", self.url, None, str(e)
            )
            raise ConnectionError(error_msg)
    
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Retrieve field value from NetBox.
        
        Supports simple field names and nested paths:
        - "device_name" -> retrieves device name
        - "site_name" -> retrieves site name
        - "primary_ip" -> retrieves primary IP address
        - "device.name" -> nested field access
        
        Args:
            field_path: Field path to retrieve
            
        Returns:
            Field value as string, or None if not found
            
        Raises:
            ConnectionError: If not connected to NetBox
            ValueError: If field_path is invalid
        """
        if not self._connected or self.api is None:
            raise ConnectionError("Not connected to NetBox. Call connect() first.")
        
        if not field_path:
            raise ValueError("field_path cannot be empty")
        
        try:
            # Parse field path
            parts = field_path.split('.')
            
            # Map common field names to NetBox API endpoints
            # This is a simplified implementation - real implementation would be more comprehensive
            field_mapping = {
                'device_name': self._get_device_name,
                'site_name': self._get_site_name,
                'primary_ip': self._get_primary_ip,
                'device': self._get_device_field,
                'site': self._get_site_field,
            }
            
            # Handle simple field names
            if len(parts) == 1:
                field_name = parts[0]
                if field_name in field_mapping:
                    return field_mapping[field_name]()
                else:
                    # Try to get as generic field
                    return self._get_generic_field(field_path)
            
            # Handle nested paths (e.g., "device.name")
            else:
                base_field = parts[0]
                sub_path = '.'.join(parts[1:])
                
                if base_field in field_mapping:
                    return field_mapping[base_field](sub_path)
                else:
                    return self._get_generic_field(field_path)
                    
        except Exception as e:
            # Log error but return None to allow processing to continue
            print(f"Error retrieving field '{field_path}' from NetBox: {str(e)}")
            return None
    
    def _get_device_name(self, sub_path: Optional[str] = None) -> Optional[str]:
        """Get device name from NetBox."""
        try:
            # This is a simplified implementation
            # Real implementation would need device identifier
            devices = self.api.dcim.devices.all()
            if devices:
                device = devices[0]
                if sub_path:
                    return self._extract_nested_field(device, sub_path)
                return str(device.name) if device.name else None
            return None
        except Exception:
            return None
    
    def _get_site_name(self, sub_path: Optional[str] = None) -> Optional[str]:
        """Get site name from NetBox."""
        try:
            sites = self.api.dcim.sites.all()
            if sites:
                site = sites[0]
                if sub_path:
                    return self._extract_nested_field(site, sub_path)
                return str(site.name) if site.name else None
            return None
        except Exception:
            return None
    
    def _get_primary_ip(self, sub_path: Optional[str] = None) -> Optional[str]:
        """Get primary IP address from NetBox."""
        try:
            devices = self.api.dcim.devices.all()
            if devices:
                device = devices[0]
                if device.primary_ip:
                    if sub_path:
                        return self._extract_nested_field(device.primary_ip, sub_path)
                    return str(device.primary_ip)
            return None
        except Exception:
            return None
    
    def _get_device_field(self, sub_path: str) -> Optional[str]:
        """Get nested device field from NetBox."""
        try:
            devices = self.api.dcim.devices.all()
            if devices:
                device = devices[0]
                return self._extract_nested_field(device, sub_path)
            return None
        except Exception:
            return None
    
    def _get_site_field(self, sub_path: str) -> Optional[str]:
        """Get nested site field from NetBox."""
        try:
            sites = self.api.dcim.sites.all()
            if sites:
                site = sites[0]
                return self._extract_nested_field(site, sub_path)
            return None
        except Exception:
            return None
    
    def _get_generic_field(self, field_path: str) -> Optional[str]:
        """
        Attempt to retrieve a generic field.
        
        This is a fallback for fields not explicitly mapped.
        """
        # Return None for unmapped fields
        return None
    
    def _extract_nested_field(self, obj, field_path: str) -> Optional[str]:
        """
        Extract nested field from NetBox object.
        
        Args:
            obj: NetBox object
            field_path: Dot-separated field path
            
        Returns:
            Field value as string, or None if not found
        """
        try:
            parts = field_path.split('.')
            current = obj
            
            for part in parts:
                if hasattr(current, part):
                    current = getattr(current, part)
                elif isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    return None
            
            return str(current) if current is not None else None
            
        except Exception:
            return None
    
    def disconnect(self) -> None:
        """
        Close connection to NetBox.
        
        Cleans up API connection and resources.
        """
        self.api = None
        self._connected = False
