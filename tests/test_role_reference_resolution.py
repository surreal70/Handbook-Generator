"""
Tests for role reference resolution in service and process documentation.

Tests the resolution of role references from meta-organisation-roles.yaml
in service and process templates, including role names and email addresses.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import tempfile
import yaml

from src.meta_adapter import MetaAdapter
from src.metadata_config_manager import MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo


def create_test_metadata_config():
    """Helper function to create test metadata configuration."""
    org_info = OrganizationInfo(
        name="Test Organization",
        address="Test Address",
        city="Test City",
        postal_code="12345",
        country="Germany",
        website="https://example.com",
        phone="+49 123 456789",
        email="test@example.com"
    )
    doc_info = DocumentInfo(
        owner="Test Owner",
        approver="Test Approver",
        version="1.0.0",
        classification="internal"
    )
    return MetadataConfig(
        organization=org_info,
        roles={},
        document=doc_info,
        author="Test Author",
        language="de"
    )


class TestRoleReferenceResolution:
    """Tests for role reference resolution."""
    
    def test_role_reference_in_service_owner(self):
        """Test resolving role reference in service owner field."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create service config with role reference
            service_config = {
                'service': {
                    'id': 'SVC-001',
                    'owner': 'role_IT_Manager'  # Role reference
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Create metadata config with roles
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            
            it_manager_role = PersonRole(
                name="John Doe",
                title="IT Manager",
                email="john.doe@example.com",
                phone="+49 123 456789"
            )
            
            metadata_config = MetadataConfig(
                organization=org_config,
                roles={'role_IT_Manager': it_manager_role}
            )
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should resolve role reference
            owner = adapter.get_field('service.owner')
            assert owner == 'role_IT_Manager'
            
            # Should also be able to resolve the actual role
            role_name = adapter.get_field('role_IT_Manager')
            assert role_name == 'John Doe'
    
    def test_role_reference_in_process_owner(self):
        """Test resolving role reference in process owner field."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory structure
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create process config with role reference
            process_config = {
                'process': {
                    'id': 'PROC-001',
                    'owner': 'role_Risk_Manager'  # Role reference
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create metadata config with roles
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            
            risk_manager_role = PersonRole(
                name="Jane Smith",
                title="Risk Manager",
                email="jane.smith@example.com",
                phone="+49 123 456790"
            )
            
            metadata_config = MetadataConfig(
                organization=org_config,
                roles={'role_Risk_Manager': risk_manager_role}
            )
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # Should resolve role reference
            owner = adapter.get_field('process.owner')
            assert owner == 'role_Risk_Manager'
            
            # Should also be able to resolve the actual role
            role_name = adapter.get_field('role_Risk_Manager')
            assert role_name == 'Jane Smith'
    
    def test_role_email_resolution(self):
        """Test resolving role email addresses."""
        # Create metadata config with roles
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        
        cio_role = PersonRole(
            name="Alice Johnson",
            title="CIO",
            email="alice.johnson@example.com",
            phone="+49 123 456791"
        )
        
        metadata_config = MetadataConfig(
            organization=org_config,
            roles={'role_CIO': cio_role}
        )
        
        # Test resolution
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Should resolve role name
        role_name = adapter.get_field('role_CIO')
        assert role_name == 'Alice Johnson'
        
        # Should resolve role email
        role_email = adapter.get_field('role_CIO_email')
        assert role_email == 'alice.johnson@example.com'
    
    def test_multiple_role_references(self):
        """Test resolving multiple role references."""
        # Create metadata config with multiple roles
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        
        roles = {
            'role_CEO': PersonRole(
                name="Bob Williams",
                title="CEO",
                email="bob.williams@example.com",
                phone="+49 123 456792"
            ),
            'role_CIO': PersonRole(
                name="Alice Johnson",
                title="CIO",
                email="alice.johnson@example.com",
                phone="+49 123 456791"
            ),
            'role_CISO': PersonRole(
                name="Charlie Brown",
                title="CISO",
                email="charlie.brown@example.com",
                phone="+49 123 456793"
            )
        }
        
        metadata_config = MetadataConfig(
            organization=org_config,
            roles=roles
        )
        
        # Test resolution
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Should resolve all roles
        assert adapter.get_field('role_CEO') == 'Bob Williams'
        assert adapter.get_field('role_CIO') == 'Alice Johnson'
        assert adapter.get_field('role_CISO') == 'Charlie Brown'
        
        # Should resolve all emails
        assert adapter.get_field('role_CEO_email') == 'bob.williams@example.com'
        assert adapter.get_field('role_CIO_email') == 'alice.johnson@example.com'
        assert adapter.get_field('role_CISO_email') == 'charlie.brown@example.com'


class TestRoleReferenceInRACI:
    """Tests for role references in RACI matrices."""
    
    def test_raci_role_references(self):
        """Test resolving role references in RACI matrix."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory structure
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create process config with RACI matrix
            process_config = {
                'process': {
                    'id': 'PROC-001',
                    'raci': {
                        'incident_detection': {
                            'responsible': 'role_System_Administrator',
                            'accountable': 'role_IT_Manager',
                            'consulted': 'role_CISO',
                            'informed': 'role_CIO'
                        }
                    }
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create metadata config with roles
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            
            roles = {
                'role_System_Administrator': PersonRole(
                    name="Dave Davis",
                    title="System Administrator",
                    email="dave.davis@example.com",
                    phone="+49 123 456794"
                ),
                'role_IT_Manager': PersonRole(
                    name="John Doe",
                    title="IT Manager",
                    email="john.doe@example.com",
                    phone="+49 123 456789"
                ),
                'role_CISO': PersonRole(
                    name="Charlie Brown",
                    title="CISO",
                    email="charlie.brown@example.com",
                    phone="+49 123 456793"
                ),
                'role_CIO': PersonRole(
                    name="Alice Johnson",
                    title="CIO",
                    email="alice.johnson@example.com",
                    phone="+49 123 456791"
                )
            }
            
            metadata_config = MetadataConfig(
                organization=org_config,
                roles=roles
            )
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # Should resolve RACI role references
            responsible = adapter.get_field('process.raci.incident_detection.responsible')
            assert responsible == 'role_System_Administrator'
            
            # Should be able to resolve the actual role names
            assert adapter.get_field('role_System_Administrator') == 'Dave Davis'
            assert adapter.get_field('role_IT_Manager') == 'John Doe'
            assert adapter.get_field('role_CISO') == 'Charlie Brown'
            assert adapter.get_field('role_CIO') == 'Alice Johnson'


class TestRoleReferenceInEscalation:
    """Tests for role references in escalation paths."""
    
    def test_escalation_role_references(self):
        """Test resolving role references in escalation paths."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create global service config with escalation
            global_config = {
                'escalation': {
                    'level_1': 'role_Helpdesk',
                    'level_2': 'role_IT_Manager',
                    'level_3': 'role_CIO',
                    'level_4': 'role_CEO'
                }
            }
            global_config_path = Path(tmpdir) / 'services' / 'de' / 'meta-global-service.yaml'
            with open(global_config_path, 'w') as f:
                yaml.dump(global_config, f)
            
            # Create minimal service config
            service_config = {
                'service': {
                    'id': 'SVC-001'
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Create metadata config with roles
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            
            roles = {
                'role_Helpdesk': PersonRole(
                    name="Helpdesk Team",
                    title="Helpdesk",
                    email="helpdesk@example.com",
                    phone="+49 123 456795"
                ),
                'role_IT_Manager': PersonRole(
                    name="John Doe",
                    title="IT Manager",
                    email="john.doe@example.com",
                    phone="+49 123 456789"
                ),
                'role_CIO': PersonRole(
                    name="Alice Johnson",
                    title="CIO",
                    email="alice.johnson@example.com",
                    phone="+49 123 456791"
                ),
                'role_CEO': PersonRole(
                    name="Bob Williams",
                    title="CEO",
                    email="bob.williams@example.com",
                    phone="+49 123 456792"
                )
            }
            
            metadata_config = MetadataConfig(
                organization=org_config,
                roles=roles
            )
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should resolve escalation role references
            level_1 = adapter.get_field('escalation.level_1')
            assert level_1 == 'role_Helpdesk'
            
            # Should be able to resolve the actual role names
            assert adapter.get_field('role_Helpdesk') == 'Helpdesk Team'
            assert adapter.get_field('role_IT_Manager') == 'John Doe'
            assert adapter.get_field('role_CIO') == 'Alice Johnson'
            assert adapter.get_field('role_CEO') == 'Bob Williams'


class TestMissingRoleReferences:
    """Tests for handling missing role references."""
    
    def test_missing_role_returns_none(self):
        """Test that missing role reference returns None."""
        # Create metadata config without roles
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = MetadataConfig(organization=org_config)
        
        # Test resolution
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Should return None for missing role
        value = adapter.get_field('role_Nonexistent')
        assert value is None
    
    def test_missing_role_email_returns_none(self):
        """Test that missing role email returns None."""
        # Create metadata config with role but no email
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        
        role_without_email = PersonRole(
            name="John Doe",
            title="IT Manager",
            email=None,  # No email
            phone="+49 123 456789"
        )
        
        metadata_config = MetadataConfig(
            organization=org_config,
            roles={'role_IT_Manager': role_without_email}
        )
        
        # Test resolution
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Should resolve role name
        role_name = adapter.get_field('role_IT_Manager')
        assert role_name == 'John Doe'
        
        # Should return None for missing email
        role_email = adapter.get_field('role_IT_Manager_email')
        assert role_email is None


class TestRoleReferenceValidation:
    """Tests for role reference validation."""
    
    def test_valid_role_reference_format(self):
        """Test that role references follow correct format."""
        # Create metadata config with roles
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        
        # Valid role reference format: role_<Name>
        valid_roles = {
            'role_IT_Manager': PersonRole(
                name="John Doe",
                title="IT Manager",
                email="john.doe@example.com",
                phone="+49 123 456789"
            ),
            'role_CISO': PersonRole(
                name="Charlie Brown",
                title="CISO",
                email="charlie.brown@example.com",
                phone="+49 123 456793"
            )
        }
        
        metadata_config = MetadataConfig(
            organization=org_config,
            roles=valid_roles
        )
        
        # Test resolution
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Should resolve valid role references
        assert adapter.get_field('role_IT_Manager') is not None
        assert adapter.get_field('role_CISO') is not None
    
    def test_role_reference_case_sensitivity(self):
        """Test that role references are case-sensitive."""
        # Create metadata config with roles
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        
        role = PersonRole(
            name="John Doe",
            title="IT Manager",
            email="john.doe@example.com",
            phone="+49 123 456789"
        )
        
        metadata_config = MetadataConfig(
            organization=org_config,
            roles={'role_IT_Manager': role}
        )
        
        # Test resolution
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Should resolve exact case
        assert adapter.get_field('role_IT_Manager') == 'John Doe'
        
        # Should not resolve different case
        assert adapter.get_field('role_it_manager') is None
        assert adapter.get_field('ROLE_IT_MANAGER') is None
