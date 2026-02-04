"""
Tests for NetBox Adapter

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from hypothesis import given, settings, strategies as st
from unittest.mock import Mock, MagicMock, patch
from src.netbox_adapter import NetBoxAdapter
from src.data_source_adapter import DataSourceAdapter


# ============================================================================
# Property-Based Tests
# ============================================================================

@settings(max_examples=100)
@given(
    field_name=st.sampled_from(['name', 'id', 'status', 'description', 'slug']),
    field_value=st.text(min_size=1, max_size=50)
)
def test_property_6_data_extraction_from_api_responses(field_name, field_value):
    """
    Feature: handbook-generator, Property 6: Data Extraction from API Responses
    
    For any mocked API response and field path, the system should correctly
    extract the requested field value from the response structure.
    
    Validates: Requirements 4.3
    """
    # Create a mock NetBox object with the field
    mock_object = Mock()
    setattr(mock_object, field_name, field_value)
    
    # Create adapter
    adapter = NetBoxAdapter("https://netbox.test", "test-token")
    
    # Test nested field extraction
    result = adapter._extract_nested_field(mock_object, field_name)
    
    # Verify extraction
    assert result == str(field_value), \
        f"Failed to extract field '{field_name}' with value '{field_value}'"


@settings(max_examples=100)
@given(
    nested_path=st.lists(
        st.sampled_from(['device', 'site', 'name', 'location', 'status']),
        min_size=2,
        max_size=4
    ),
    final_value=st.text(min_size=1, max_size=30)
)
def test_property_6_nested_field_extraction(nested_path, final_value):
    """
    Feature: handbook-generator, Property 6: Data Extraction from API Responses
    
    For any nested field path, the system should correctly traverse the object
    hierarchy and extract the final value.
    
    Validates: Requirements 4.3
    """
    # Build nested mock object structure
    mock_root = Mock()
    current = mock_root
    
    for i, part in enumerate(nested_path[:-1]):
        next_obj = Mock()
        setattr(current, part, next_obj)
        current = next_obj
    
    # Set final value
    setattr(current, nested_path[-1], final_value)
    
    # Create adapter
    adapter = NetBoxAdapter("https://netbox.test", "test-token")
    
    # Test extraction
    field_path = '.'.join(nested_path)
    result = adapter._extract_nested_field(mock_root, field_path)
    
    # Verify extraction
    assert result == str(final_value), \
        f"Failed to extract nested field '{field_path}' with value '{final_value}'"


@settings(max_examples=100)
@given(
    field_path=st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'))),
)
def test_property_6_missing_field_returns_none(field_path):
    """
    Feature: handbook-generator, Property 6: Data Extraction from API Responses
    
    For any field path that doesn't exist in the API response, the system
    should return None rather than raising an exception.
    
    Validates: Requirements 4.3
    """
    # Create mock object without the requested field
    mock_object = Mock(spec=[])  # Empty spec means no attributes
    
    # Create adapter
    adapter = NetBoxAdapter("https://netbox.test", "test-token")
    
    # Test extraction of non-existent field
    result = adapter._extract_nested_field(mock_object, field_path)
    
    # Verify None is returned
    assert result is None, \
        f"Expected None for missing field '{field_path}', got '{result}'"


# ============================================================================
# Unit Tests
# ============================================================================

def test_netbox_adapter_initialization():
    """Test NetBox adapter initialization."""
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token-123")
    
    assert adapter.url == "https://netbox.example.com"
    assert adapter.api_token == "test-token-123"
    assert adapter.api is None
    assert adapter._connected is False


def test_netbox_adapter_is_data_source_adapter():
    """Test that NetBoxAdapter implements DataSourceAdapter interface."""
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    
    assert isinstance(adapter, DataSourceAdapter)
    assert hasattr(adapter, 'connect')
    assert hasattr(adapter, 'get_field')
    assert hasattr(adapter, 'disconnect')


@patch('src.netbox_adapter.pynetbox.api')
def test_netbox_adapter_connect_success(mock_pynetbox_api):
    """Test successful connection to NetBox."""
    # Setup mock
    mock_api_instance = Mock()
    mock_api_instance.version = "3.5.0"
    mock_pynetbox_api.return_value = mock_api_instance
    
    # Test connection
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    result = adapter.connect()
    
    assert result is True
    assert adapter._connected is True
    assert adapter.api is not None
    mock_pynetbox_api.assert_called_once_with(
        "https://netbox.example.com",
        token="test-token"
    )


@patch('src.netbox_adapter.pynetbox.api')
def test_netbox_adapter_connect_failure(mock_pynetbox_api):
    """Test connection failure to NetBox."""
    # Setup mock to raise exception
    mock_pynetbox_api.side_effect = Exception("Connection refused")
    
    # Test connection
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    
    with pytest.raises(ConnectionError) as exc_info:
        adapter.connect()
    
    # Check that error message contains relevant information
    error_msg = str(exc_info.value)
    assert "Failed to connect to NetBox" in error_msg or "Unexpected error connecting to NetBox" in error_msg
    assert adapter._connected is False


def test_netbox_adapter_get_field_not_connected():
    """Test get_field raises error when not connected."""
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    
    with pytest.raises(ConnectionError) as exc_info:
        adapter.get_field("device_name")
    
    assert "Not connected to NetBox" in str(exc_info.value)


def test_netbox_adapter_get_field_empty_path():
    """Test get_field raises error for empty field path."""
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    adapter._connected = True
    adapter.api = Mock()
    
    with pytest.raises(ValueError) as exc_info:
        adapter.get_field("")
    
    assert "field_path cannot be empty" in str(exc_info.value)


@patch('src.netbox_adapter.pynetbox.api')
def test_netbox_adapter_get_device_name(mock_pynetbox_api):
    """Test retrieving device name from NetBox."""
    # Setup mock
    mock_device = Mock()
    mock_device.name = "server-01"
    
    mock_api_instance = Mock()
    mock_api_instance.version = "3.5.0"
    mock_api_instance.dcim.devices.all.return_value = [mock_device]
    mock_pynetbox_api.return_value = mock_api_instance
    
    # Test
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    adapter.connect()
    result = adapter.get_field("device_name")
    
    assert result == "server-01"


@patch('src.netbox_adapter.pynetbox.api')
def test_netbox_adapter_get_site_name(mock_pynetbox_api):
    """Test retrieving site name from NetBox."""
    # Setup mock
    mock_site = Mock()
    mock_site.name = "datacenter-01"
    
    mock_api_instance = Mock()
    mock_api_instance.version = "3.5.0"
    mock_api_instance.dcim.sites.all.return_value = [mock_site]
    mock_pynetbox_api.return_value = mock_api_instance
    
    # Test
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    adapter.connect()
    result = adapter.get_field("site_name")
    
    assert result == "datacenter-01"


@patch('src.netbox_adapter.pynetbox.api')
def test_netbox_adapter_get_field_not_found(mock_pynetbox_api):
    """Test get_field returns None for non-existent field."""
    # Setup mock with empty results
    mock_api_instance = Mock()
    mock_api_instance.version = "3.5.0"
    mock_api_instance.dcim.devices.all.return_value = []
    mock_pynetbox_api.return_value = mock_api_instance
    
    # Test
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    adapter.connect()
    result = adapter.get_field("device_name")
    
    assert result is None


@patch('src.netbox_adapter.pynetbox.api')
def test_netbox_adapter_disconnect(mock_pynetbox_api):
    """Test disconnecting from NetBox."""
    # Setup mock
    mock_api_instance = Mock()
    mock_api_instance.version = "3.5.0"
    mock_pynetbox_api.return_value = mock_api_instance
    
    # Connect and disconnect
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    adapter.connect()
    assert adapter._connected is True
    
    adapter.disconnect()
    assert adapter._connected is False
    assert adapter.api is None


@patch('src.netbox_adapter.pynetbox.api')
def test_netbox_adapter_context_manager(mock_pynetbox_api):
    """Test NetBox adapter as context manager."""
    # Setup mock
    mock_api_instance = Mock()
    mock_api_instance.version = "3.5.0"
    mock_pynetbox_api.return_value = mock_api_instance
    
    # Test context manager
    adapter = NetBoxAdapter("https://netbox.example.com", "test-token")
    
    with adapter as a:
        assert a._connected is True
        assert a.api is not None
    
    # After context, should be disconnected
    assert adapter._connected is False
    assert adapter.api is None


def test_extract_nested_field_with_dict():
    """Test extracting nested field from dictionary-like object."""
    # Create mock object with dict attribute
    mock_object = Mock()
    mock_object.data = {'nested': {'value': 'test-value'}}
    
    adapter = NetBoxAdapter("https://netbox.test", "test-token")
    
    # Test extraction from dict
    result = adapter._extract_nested_field(mock_object.data, 'nested.value')
    
    assert result == 'test-value'


def test_extract_nested_field_none_value():
    """Test extracting nested field that has None value."""
    mock_object = Mock()
    mock_object.field = None
    
    adapter = NetBoxAdapter("https://netbox.test", "test-token")
    result = adapter._extract_nested_field(mock_object, 'field')
    
    assert result is None
