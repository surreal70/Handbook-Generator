"""
Unit tests for Per-Handbook Metadata

Tests for independent metadata per handbook type, handbook placeholder replacement,
and missing metadata handling.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
import yaml
from pathlib import Path
from tempfile import TemporaryDirectory

from src.metadata_config_manager import (
    MetadataConfigManager,
    MetadataConfig,
    OrganizationInfo,
    PersonRole,
    DocumentInfo,
    HandbookInfo
)


class TestHandbookInfo:
    """Test HandbookInfo dataclass."""
    
    def test_valid_handbook_info(self):
        """Test creating valid handbook info."""
        handbook = HandbookInfo(
            version="1.0.0",
            owner="John Doe",
            approver="Jane Smith",
            date="2025-02-05"
        )
        assert handbook.version == "1.0.0"
        assert handbook.owner == "John Doe"
        assert handbook.approver == "Jane Smith"
        assert handbook.date == "2025-02-05"
    
    def test_invalid_date_format(self):
        """Test handbook info with invalid date format."""
        with pytest.raises(ValueError, match="Invalid date format"):
            HandbookInfo(
                version="1.0.0",
                owner="John Doe",
                approver="Jane Smith",
                date="05-02-2025"  # Wrong format
            )
    
    def test_valid_date_formats(self):
        """Test various valid date formats."""
        valid_dates = [
            "2025-02-05",
            "2025-12-31",
            "2024-01-01"
        ]
        
        for date in valid_dates:
            handbook = HandbookInfo(
                version="1.0.0",
                owner="John Doe",
                approver="Jane Smith",
                date=date
            )
            assert handbook.date == date


class TestPerHandbookMetadata:
    """Test per-handbook metadata functionality."""
    
    @pytest.fixture
    def temp_metadata_file(self, tmp_path):
        """Create temporary metadata file."""
        metadata_path = tmp_path / "metadata.yaml"
        return metadata_path
    
    @pytest.fixture
    def metadata_with_handbooks(self):
        """Valid metadata YAML content with per-handbook metadata."""
        return """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"
  
  cio:
    name: "Jane Smith"
    title: "Chief Information Officer"
    email: "jane@test.com"
    phone: "+49 89 12345679"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

handbooks:
  bcm:
    version: "1.0.0"
    owner: "Peter Fischer"
    approver: "Max Mustermann"
    date: "2025-02-05"
  
  isms:
    version: "2.1.0"
    owner: "Thomas Weber"
    approver: "Anna Schmidt"
    date: "2025-02-01"
  
  bsi-grundschutz:
    version: "1.5.0"
    owner: "Thomas Weber"
    approver: "Anna Schmidt"
    date: "2025-01-28"
  
  it-operation:
    version: "3.0.0"
    owner: "Andreas Huemmer"
    approver: "Anna Schmidt"
    date: "2025-01-15"

defaults:
  author: "Test Author"
  language: "de"
"""
    
    def test_load_metadata_with_handbooks(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test loading metadata with per-handbook metadata.
        
        Requirements: 26.1, 26.2, 26.3, 26.4
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify handbooks section is loaded
        assert config.handbooks is not None
        assert len(config.handbooks) == 4
        
        # Verify BCM handbook metadata
        assert "bcm" in config.handbooks
        bcm = config.handbooks["bcm"]
        assert bcm.version == "1.0.0"
        assert bcm.owner == "Peter Fischer"
        assert bcm.approver == "Max Mustermann"
        assert bcm.date == "2025-02-05"
        
        # Verify ISMS handbook metadata
        assert "isms" in config.handbooks
        isms = config.handbooks["isms"]
        assert isms.version == "2.1.0"
        assert isms.owner == "Thomas Weber"
        assert isms.approver == "Anna Schmidt"
        assert isms.date == "2025-02-01"
        
        # Verify BSI Grundschutz handbook metadata
        assert "bsi-grundschutz" in config.handbooks
        bsi = config.handbooks["bsi-grundschutz"]
        assert bsi.version == "1.5.0"
        assert bsi.owner == "Thomas Weber"
        assert bsi.approver == "Anna Schmidt"
        assert bsi.date == "2025-01-28"
        
        # Verify IT Operation handbook metadata
        assert "it-operation" in config.handbooks
        it_op = config.handbooks["it-operation"]
        assert it_op.version == "3.0.0"
        assert it_op.owner == "Andreas Huemmer"
        assert it_op.approver == "Anna Schmidt"
        assert it_op.date == "2025-01-15"
    
    def test_independent_metadata_per_handbook(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test that each handbook has independent metadata.
        
        Requirements: 26.1, 26.2, 26.3, 26.4
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify each handbook has different metadata
        bcm = config.handbooks["bcm"]
        isms = config.handbooks["isms"]
        bsi = config.handbooks["bsi-grundschutz"]
        it_op = config.handbooks["it-operation"]
        
        # Verify versions are independent
        assert bcm.version != isms.version
        assert bcm.version != bsi.version
        assert bcm.version != it_op.version
        assert isms.version != bsi.version
        assert isms.version != it_op.version
        assert bsi.version != it_op.version
        
        # Verify owners are independent
        assert bcm.owner != isms.owner
        assert bcm.owner != it_op.owner
        
        # Verify dates are independent
        assert bcm.date != isms.date
        assert bcm.date != bsi.date
        assert bcm.date != it_op.date
        assert isms.date != bsi.date
        assert isms.date != it_op.date
        assert bsi.date != it_op.date
    
    def test_get_handbook_metadata(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test getting handbook metadata by type.
        
        Requirements: 26.1, 26.2, 26.3, 26.4
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Test getting handbook metadata
        bcm = config.get_handbook_metadata("bcm")
        assert bcm is not None
        assert bcm.version == "1.0.0"
        assert bcm.owner == "Peter Fischer"
        
        isms = config.get_handbook_metadata("isms")
        assert isms is not None
        assert isms.version == "2.1.0"
        assert isms.owner == "Thomas Weber"
        
        bsi = config.get_handbook_metadata("bsi-grundschutz")
        assert bsi is not None
        assert bsi.version == "1.5.0"
        
        it_op = config.get_handbook_metadata("it-operation")
        assert it_op is not None
        assert it_op.version == "3.0.0"
    
    def test_get_handbook_metadata_case_insensitive(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test getting handbook metadata with case-insensitive lookup.
        
        Requirements: 26.1
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Test case-insensitive lookup
        assert config.get_handbook_metadata("bcm") is not None
        assert config.get_handbook_metadata("BCM") is not None
        assert config.get_handbook_metadata("Bcm") is not None
        assert config.get_handbook_metadata("bcm").version == "1.0.0"
        
        assert config.get_handbook_metadata("isms") is not None
        assert config.get_handbook_metadata("ISMS") is not None
        assert config.get_handbook_metadata("Isms") is not None
        
        assert config.get_handbook_metadata("bsi-grundschutz") is not None
        assert config.get_handbook_metadata("BSI-GRUNDSCHUTZ") is not None
        assert config.get_handbook_metadata("Bsi-Grundschutz") is not None
    
    def test_get_handbook_metadata_not_found(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test getting non-existent handbook metadata.
        
        Requirements: 26.1
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Test getting non-existent handbook
        assert config.get_handbook_metadata("nonexistent") is None
        assert config.get_handbook_metadata("cis-controls") is None
    
    def test_load_metadata_without_handbooks(self, temp_metadata_file):
        """
        Test loading metadata without handbooks section.
        
        Requirements: 26.1
        """
        # Write metadata without handbooks section
        metadata_content = """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

defaults:
  author: "Test Author"
  language: "de"
"""
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify handbooks is empty dict (not None)
        assert config.handbooks is not None
        assert isinstance(config.handbooks, dict)
        assert len(config.handbooks) == 0
    
    def test_handbook_metadata_with_missing_fields(self, temp_metadata_file):
        """
        Test loading handbook metadata with missing optional fields.
        
        Requirements: 26.1, 26.2, 26.3, 26.4
        """
        # Write metadata with incomplete handbook info
        metadata_content = """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

handbooks:
  bcm:
    version: "1.0.0"
    # Missing owner, approver, date

defaults:
  author: "Test Author"
  language: "de"
"""
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify handbook is loaded with default values for missing fields
        bcm = config.get_handbook_metadata("bcm")
        assert bcm is not None
        assert bcm.version == "1.0.0"
        assert bcm.owner == ""  # Default empty string
        assert bcm.approver == ""  # Default empty string
        assert bcm.date == ""  # Default empty string
    
    def test_handbook_metadata_invalid_date(self, temp_metadata_file):
        """
        Test loading handbook metadata with invalid date format.
        
        Requirements: 26.4
        """
        # Write metadata with invalid date
        metadata_content = """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

handbooks:
  bcm:
    version: "1.0.0"
    owner: "John Doe"
    approver: "Jane Smith"
    date: "05-02-2025"  # Invalid format

defaults:
  author: "Test Author"
  language: "de"
"""
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata should fail
        manager = MetadataConfigManager(temp_metadata_file)
        
        with pytest.raises(ValueError, match="Invalid date format"):
            manager.load_metadata()
    
    def test_create_default_metadata_includes_handbooks(self, temp_metadata_file):
        """
        Test that default metadata includes handbook metadata.
        
        Requirements: 26.1, 26.2, 26.3, 26.4
        """
        # Create default metadata
        manager = MetadataConfigManager(temp_metadata_file)
        manager.create_default_metadata()
        
        # Verify file was created
        assert temp_metadata_file.exists()
        
        # Load and verify it includes handbooks
        config = manager.load_metadata()
        assert config.handbooks is not None
        assert len(config.handbooks) > 0
        
        # Verify default handbooks are present
        assert "bcm" in config.handbooks
        assert "isms" in config.handbooks
        assert "bsi-grundschutz" in config.handbooks
        assert "it-operation" in config.handbooks
        
        # Verify each has all required fields
        for handbook_type, handbook in config.handbooks.items():
            assert handbook.version is not None
            assert handbook.owner is not None
            assert handbook.approver is not None
            assert handbook.date is not None
    
    def test_handbook_metadata_modification_independence(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test that modifying one handbook's metadata doesn't affect others.
        
        Requirements: 26.1, 26.2, 26.3, 26.4
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Get original values
        bcm_original = config.get_handbook_metadata("bcm")
        isms_original = config.get_handbook_metadata("isms")
        
        # Modify BCM metadata
        config.handbooks["bcm"] = HandbookInfo(
            version="2.0.0",
            owner="New Owner",
            approver="New Approver",
            date="2025-03-01"
        )
        
        # Verify BCM was modified
        bcm_modified = config.get_handbook_metadata("bcm")
        assert bcm_modified.version == "2.0.0"
        assert bcm_modified.owner == "New Owner"
        
        # Verify ISMS was NOT modified
        isms_after = config.get_handbook_metadata("isms")
        assert isms_after.version == isms_original.version
        assert isms_after.owner == isms_original.owner
        assert isms_after.approver == isms_original.approver
        assert isms_after.date == isms_original.date
    
    def test_multiple_handbooks_same_owner(self, temp_metadata_file):
        """
        Test that multiple handbooks can have the same owner.
        
        Requirements: 26.2
        """
        # Write metadata with same owner for multiple handbooks
        metadata_content = """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

handbooks:
  isms:
    version: "2.1.0"
    owner: "Thomas Weber"
    approver: "Anna Schmidt"
    date: "2025-02-01"
  
  bsi-grundschutz:
    version: "1.5.0"
    owner: "Thomas Weber"  # Same owner as ISMS
    approver: "Anna Schmidt"
    date: "2025-01-28"

defaults:
  author: "Test Author"
  language: "de"
"""
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify both handbooks have the same owner
        isms = config.get_handbook_metadata("isms")
        bsi = config.get_handbook_metadata("bsi-grundschutz")
        
        assert isms.owner == "Thomas Weber"
        assert bsi.owner == "Thomas Weber"
        assert isms.owner == bsi.owner
        
        # But they should still be independent objects
        assert isms is not bsi
        assert isms.version != bsi.version
        assert isms.date != bsi.date



class TestHandbookPlaceholderSupport:
    """Test handbook placeholder replacement functionality."""
    
    @pytest.fixture
    def temp_metadata_file(self, tmp_path):
        """Create temporary metadata file."""
        metadata_path = tmp_path / "metadata.yaml"
        return metadata_path
    
    @pytest.fixture
    def metadata_with_handbooks(self):
        """Valid metadata YAML content with per-handbook metadata."""
        return """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

handbooks:
  bcm:
    version: "1.0.0"
    owner: "Peter Fischer"
    approver: "Max Mustermann"
    date: "2025-02-05"
  
  isms:
    version: "2.1.0"
    owner: "Thomas Weber"
    approver: "Anna Schmidt"
    date: "2025-02-01"

defaults:
  author: "Test Author"
  language: "de"
"""
    
    def test_handbook_version_placeholder(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test handbook.version placeholder support.
        
        Requirements: 26.5
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify version can be accessed for placeholder replacement
        bcm = config.get_handbook_metadata("bcm")
        assert bcm.version == "1.0.0"
        
        isms = config.get_handbook_metadata("isms")
        assert isms.version == "2.1.0"
        
        # Simulate placeholder replacement
        template = "Version: {{ handbook.version }}"
        bcm_result = template.replace("{{ handbook.version }}", bcm.version)
        assert bcm_result == "Version: 1.0.0"
        
        isms_result = template.replace("{{ handbook.version }}", isms.version)
        assert isms_result == "Version: 2.1.0"
    
    def test_handbook_owner_placeholder(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test handbook.owner placeholder support.
        
        Requirements: 26.5
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify owner can be accessed for placeholder replacement
        bcm = config.get_handbook_metadata("bcm")
        assert bcm.owner == "Peter Fischer"
        
        isms = config.get_handbook_metadata("isms")
        assert isms.owner == "Thomas Weber"
        
        # Simulate placeholder replacement
        template = "Owner: {{ handbook.owner }}"
        bcm_result = template.replace("{{ handbook.owner }}", bcm.owner)
        assert bcm_result == "Owner: Peter Fischer"
        
        isms_result = template.replace("{{ handbook.owner }}", isms.owner)
        assert isms_result == "Owner: Thomas Weber"
    
    def test_handbook_approver_placeholder(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test handbook.approver placeholder support.
        
        Requirements: 26.5
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify approver can be accessed for placeholder replacement
        bcm = config.get_handbook_metadata("bcm")
        assert bcm.approver == "Max Mustermann"
        
        isms = config.get_handbook_metadata("isms")
        assert isms.approver == "Anna Schmidt"
        
        # Simulate placeholder replacement
        template = "Approver: {{ handbook.approver }}"
        bcm_result = template.replace("{{ handbook.approver }}", bcm.approver)
        assert bcm_result == "Approver: Max Mustermann"
        
        isms_result = template.replace("{{ handbook.approver }}", isms.approver)
        assert isms_result == "Approver: Anna Schmidt"
    
    def test_handbook_date_placeholder(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test handbook.date placeholder support.
        
        Requirements: 26.5
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify date can be accessed for placeholder replacement
        bcm = config.get_handbook_metadata("bcm")
        assert bcm.date == "2025-02-05"
        
        isms = config.get_handbook_metadata("isms")
        assert isms.date == "2025-02-01"
        
        # Simulate placeholder replacement
        template = "Date: {{ handbook.date }}"
        bcm_result = template.replace("{{ handbook.date }}", bcm.date)
        assert bcm_result == "Date: 2025-02-05"
        
        isms_result = template.replace("{{ handbook.date }}", isms.date)
        assert isms_result == "Date: 2025-02-01"
    
    def test_all_handbook_placeholders_together(self, temp_metadata_file, metadata_with_handbooks):
        """
        Test all handbook placeholders in a single template.
        
        Requirements: 26.5
        """
        # Write metadata with handbooks
        temp_metadata_file.write_text(metadata_with_handbooks)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Template with all placeholders
        template = """
**Version:** {{ handbook.version }}
**Owner:** {{ handbook.owner }}
**Approver:** {{ handbook.approver }}
**Date:** {{ handbook.date }}
"""
        
        # Test BCM handbook
        bcm = config.get_handbook_metadata("bcm")
        bcm_result = template
        bcm_result = bcm_result.replace("{{ handbook.version }}", bcm.version)
        bcm_result = bcm_result.replace("{{ handbook.owner }}", bcm.owner)
        bcm_result = bcm_result.replace("{{ handbook.approver }}", bcm.approver)
        bcm_result = bcm_result.replace("{{ handbook.date }}", bcm.date)
        
        assert "Version:** 1.0.0" in bcm_result
        assert "Owner:** Peter Fischer" in bcm_result
        assert "Approver:** Max Mustermann" in bcm_result
        assert "Date:** 2025-02-05" in bcm_result
        
        # Test ISMS handbook
        isms = config.get_handbook_metadata("isms")
        isms_result = template
        isms_result = isms_result.replace("{{ handbook.version }}", isms.version)
        isms_result = isms_result.replace("{{ handbook.owner }}", isms.owner)
        isms_result = isms_result.replace("{{ handbook.approver }}", isms.approver)
        isms_result = isms_result.replace("{{ handbook.date }}", isms.date)
        
        assert "Version:** 2.1.0" in isms_result
        assert "Owner:** Thomas Weber" in isms_result
        assert "Approver:** Anna Schmidt" in isms_result
        assert "Date:** 2025-02-01" in isms_result
    
    def test_missing_handbook_metadata_handling(self, temp_metadata_file):
        """
        Test handling of missing handbook metadata.
        
        Requirements: 26.5
        """
        # Write metadata without handbooks section
        metadata_content = """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

defaults:
  author: "Test Author"
  language: "de"
"""
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Try to get non-existent handbook metadata
        bcm = config.get_handbook_metadata("bcm")
        assert bcm is None
        
        # Simulate placeholder replacement with missing metadata
        # Should use default values or leave placeholder unchanged
        template = "Version: {{ handbook.version }}"
        
        # When handbook metadata is missing, placeholder processor should handle it
        # For now, we just verify that get_handbook_metadata returns None
        assert config.get_handbook_metadata("bcm") is None
        assert config.get_handbook_metadata("isms") is None
        assert config.get_handbook_metadata("bsi-grundschutz") is None
        assert config.get_handbook_metadata("it-operation") is None
    
    def test_handbook_placeholder_with_empty_values(self, temp_metadata_file):
        """
        Test handbook placeholders with empty values.
        
        Requirements: 26.5
        """
        # Write metadata with empty handbook values
        metadata_content = """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

handbooks:
  bcm:
    version: "1.0.0"
    owner: ""
    approver: ""
    date: ""

defaults:
  author: "Test Author"
  language: "de"
"""
        temp_metadata_file.write_text(metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Get handbook with empty values
        bcm = config.get_handbook_metadata("bcm")
        assert bcm is not None
        assert bcm.version == "1.0.0"
        assert bcm.owner == ""
        assert bcm.approver == ""
        assert bcm.date == ""
        
        # Simulate placeholder replacement with empty values
        template = "Owner: {{ handbook.owner }}"
        result = template.replace("{{ handbook.owner }}", bcm.owner)
        assert result == "Owner: "  # Empty value
