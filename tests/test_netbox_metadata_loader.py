"""
Unit tests for NetBox Metadata Loader

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from unittest.mock import Mock, MagicMock, patch
from pathlib import Path
import yaml
import tempfile
import os

from src.netbox_metadata_loader import NetBoxMetadataLoader


class TestNetBoxMetadataLoader:
    """Test suite for NetBoxMetadataLoader class."""
    
    @pytest.fixture
    def role_config_field_based(self):
        """Fixture for field-based role configuration."""
        return {
            'method': 'field',
            'field': 'role',
            'mappings': {
                'ciso': 'Chief Information Security Officer',
                'cio': 'Chief Information Officer',
                'sysop': 'System Administrator'
            }
        }
    
    @pytest.fixture
    def role_config_name_based(self):
        """Fixture for name-based role configuration."""
        return {
            'method': 'name',
            'mappings': {
                'ciso': 'CISO',
                'cio': 'CIO',
                'sysop': 'Admin'
            }
        }
    
    @pytest.fixture
    def mock_netbox_api(self):
        """Fixture for mocked NetBox API."""
        api = MagicMock()
        api.version = "3.5.0"
        return api
    
    @pytest.fixture
    def mock_contact(self):
        """Fixture for mocked NetBox contact."""
        contact = MagicMock()
        contact.name = "John Doe"
        contact.email = "john.doe@example.com"
        contact.phone = "+1234567890"
        contact.role = "Chief Information Security Officer"
        return contact
    
    @pytest.fixture
    def mock_device(self):
        """Fixture for mocked NetBox device."""
        device = MagicMock()
        device.name = "firewall-01"
        device.primary_ip = "192.168.1.1"
        
        site = MagicMock()
        site.name = "Headquarters"
        device.site = site
        
        device_role = MagicMock()
        device_role.name = "Firewall"
        device.device_role = device_role
        
        device.status = "active"
        return device
    
    @pytest.fixture
    def mock_site(self):
        """Fixture for mocked NetBox site."""
        site = MagicMock()
        site.name = "Headquarters"
        site.physical_address = "123 Main St, New York, NY 10001"
        site.description = "Main office location"
        site.status = "active"
        return site
    
    def test_init(self, role_config_field_based):
        """Test NetBoxMetadataLoader initialization."""
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        
        assert loader.netbox_url == "https://netbox.example.com"
        assert loader.api_token == "test-token"
        assert loader.role_config == role_config_field_based
        assert loader.api is None
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_load_metadata_success(self, mock_pynetbox_api, role_config_field_based,
                                   mock_netbox_api, mock_contact, mock_device, mock_site):
        """Test successful metadata loading from NetBox."""
        # Setup mock API
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.tenancy.contacts.all.return_value = [mock_contact]
        mock_netbox_api.dcim.devices.all.return_value = [mock_device]
        mock_netbox_api.dcim.sites.all.return_value = [mock_site]
        
        # Create loader and load metadata
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        
        metadata = loader.load_metadata()
        
        # Verify metadata structure
        assert 'contacts' in metadata
        assert 'devices' in metadata
        assert 'sites' in metadata
        
        # Verify contacts
        assert 'ciso' in metadata['contacts']
        assert metadata['contacts']['ciso']['name'] == "John Doe"
        assert metadata['contacts']['ciso']['email'] == "john.doe@example.com"
        assert metadata['contacts']['ciso']['phone'] == "+1234567890"
        
        # Verify devices
        assert 'firewall_01' in metadata['devices']
        assert metadata['devices']['firewall_01']['name'] == "firewall-01"
        assert metadata['devices']['firewall_01']['ip'] == "192.168.1.1"
        assert metadata['devices']['firewall_01']['site'] == "Headquarters"
        
        # Verify sites
        assert 'headquarters' in metadata['sites']
        assert metadata['sites']['headquarters']['name'] == "Headquarters"
        assert metadata['sites']['headquarters']['address'] == "123 Main St, New York, NY 10001"
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_load_metadata_connection_error(self, mock_pynetbox_api, role_config_field_based):
        """Test metadata loading with connection error."""
        # Setup mock to raise exception
        mock_pynetbox_api.side_effect = Exception("Connection refused")
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        
        # Should raise ConnectionError
        with pytest.raises(ConnectionError):
            loader.load_metadata()
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_fetch_contacts_field_based_role_mapping(self, mock_pynetbox_api,
                                                     role_config_field_based,
                                                     mock_netbox_api):
        """Test contact fetching with field-based role mapping."""
        # Setup mock contacts with different roles
        contact1 = MagicMock()
        contact1.name = "John Doe"
        contact1.email = "john@example.com"
        contact1.phone = "+1111111111"
        contact1.role = "Chief Information Security Officer"
        
        contact2 = MagicMock()
        contact2.name = "Jane Smith"
        contact2.email = "jane@example.com"
        contact2.phone = "+2222222222"
        contact2.role = "Chief Information Officer"
        
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.tenancy.contacts.all.return_value = [contact1, contact2]
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        loader.api = mock_netbox_api
        
        contacts = loader.fetch_contacts_with_roles()
        
        # Verify both contacts mapped correctly
        assert 'ciso' in contacts
        assert contacts['ciso']['name'] == "John Doe"
        
        assert 'cio' in contacts
        assert contacts['cio']['name'] == "Jane Smith"
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_fetch_contacts_name_based_role_mapping(self, mock_pynetbox_api,
                                                    role_config_name_based,
                                                    mock_netbox_api):
        """Test contact fetching with name-based role mapping."""
        # Setup mock contacts with role indicators in names
        contact1 = MagicMock()
        contact1.name = "John Doe (CISO)"
        contact1.email = "john@example.com"
        contact1.phone = "+1111111111"
        contact1.role = None
        
        contact2 = MagicMock()
        contact2.name = "Jane Smith - CIO"
        contact2.email = "jane@example.com"
        contact2.phone = "+2222222222"
        contact2.role = None
        
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.tenancy.contacts.all.return_value = [contact1, contact2]
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_name_based
        )
        loader.api = mock_netbox_api
        
        contacts = loader.fetch_contacts_with_roles()
        
        # Verify both contacts mapped correctly by name
        assert 'ciso' in contacts
        assert contacts['ciso']['name'] == "John Doe (CISO)"
        
        assert 'cio' in contacts
        assert contacts['cio']['name'] == "Jane Smith - CIO"
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_fetch_devices(self, mock_pynetbox_api, role_config_field_based,
                          mock_netbox_api, mock_device):
        """Test device fetching from NetBox."""
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.dcim.devices.all.return_value = [mock_device]
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        loader.api = mock_netbox_api
        
        devices = loader.fetch_devices()
        
        # Verify device data
        assert 'firewall_01' in devices
        assert devices['firewall_01']['name'] == "firewall-01"
        assert devices['firewall_01']['ip'] == "192.168.1.1"
        assert devices['firewall_01']['site'] == "Headquarters"
        assert devices['firewall_01']['role'] == "Firewall"
        assert devices['firewall_01']['status'] == "active"
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_fetch_sites(self, mock_pynetbox_api, role_config_field_based,
                        mock_netbox_api, mock_site):
        """Test site fetching from NetBox."""
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.dcim.sites.all.return_value = [mock_site]
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        loader.api = mock_netbox_api
        
        sites = loader.fetch_sites()
        
        # Verify site data
        assert 'headquarters' in sites
        assert sites['headquarters']['name'] == "Headquarters"
        assert sites['headquarters']['address'] == "123 Main St, New York, NY 10001"
        assert sites['headquarters']['description'] == "Main office location"
        assert sites['headquarters']['status'] == "active"
    
    def test_save_to_yaml(self, role_config_field_based):
        """Test saving metadata to YAML file."""
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        
        metadata = {
            'contacts': {
                'ciso': {'name': 'John Doe', 'email': 'john@example.com', 'phone': '+1234567890'}
            },
            'devices': {
                'firewall_01': {'name': 'firewall-01', 'ip': '192.168.1.1'}
            },
            'sites': {
                'hq': {'name': 'Headquarters', 'address': '123 Main St'}
            }
        }
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            temp_path = f.name
        
        try:
            # Save metadata
            loader.save_to_yaml(metadata, temp_path)
            
            # Verify file exists
            assert Path(temp_path).exists()
            
            # Load and verify content
            with open(temp_path, 'r', encoding='utf-8') as f:
                loaded_data = yaml.safe_load(f)
            
            assert loaded_data == metadata
            
        finally:
            # Cleanup
            if Path(temp_path).exists():
                os.unlink(temp_path)
    
    def test_save_to_yaml_io_error(self, role_config_field_based):
        """Test saving metadata with IO error."""
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        
        metadata = {'contacts': {}}
        
        # Try to save to invalid path
        with pytest.raises(IOError):
            loader.save_to_yaml(metadata, "/invalid/path/metadata.yaml")
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_determine_role_field_based(self, mock_pynetbox_api, role_config_field_based):
        """Test role determination with field-based method."""
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        
        # Test with matching role
        contact = MagicMock()
        contact.name = "John Doe"
        contact.role = "Chief Information Security Officer"
        
        role = loader._determine_role(contact)
        assert role == "ciso"
        
        # Test with non-matching role
        contact2 = MagicMock()
        contact2.name = "Jane Smith"
        contact2.role = "Network Engineer"
        
        role2 = loader._determine_role(contact2)
        assert role2 == "network_engineer"  # Normalized
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_determine_role_name_based(self, mock_pynetbox_api, role_config_name_based):
        """Test role determination with name-based method."""
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_name_based
        )
        
        # Test with matching name pattern
        contact = MagicMock()
        contact.name = "John Doe (CISO)"
        
        role = loader._determine_role(contact)
        assert role == "ciso"
        
        # Test with non-matching name
        contact2 = MagicMock()
        contact2.name = "Jane Smith"
        
        role2 = loader._determine_role(contact2)
        assert role2 is None
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_fetch_contacts_empty_result(self, mock_pynetbox_api, role_config_field_based,
                                        mock_netbox_api):
        """Test contact fetching with empty result."""
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.tenancy.contacts.all.return_value = []
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        loader.api = mock_netbox_api
        
        contacts = loader.fetch_contacts_with_roles()
        
        assert contacts == {}
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_fetch_devices_empty_result(self, mock_pynetbox_api, role_config_field_based,
                                       mock_netbox_api):
        """Test device fetching with empty result."""
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.dcim.devices.all.return_value = []
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        loader.api = mock_netbox_api
        
        devices = loader.fetch_devices()
        
        assert devices == {}
    
    @patch('src.netbox_metadata_loader.pynetbox.api')
    def test_fetch_sites_empty_result(self, mock_pynetbox_api, role_config_field_based,
                                     mock_netbox_api):
        """Test site fetching with empty result."""
        mock_pynetbox_api.return_value = mock_netbox_api
        mock_netbox_api.dcim.sites.all.return_value = []
        
        loader = NetBoxMetadataLoader(
            "https://netbox.example.com",
            "test-token",
            role_config_field_based
        )
        loader.api = mock_netbox_api
        
        sites = loader.fetch_sites()
        
        assert sites == {}
