"""
Unit tests for Extended Metadata Roles

Tests the 6 new roles added for BCM, ISMS, and BSI Grundschutz templates:
- sysop (System Administrator)
- datenschutzbeauftragter (Data Protection Officer)
- risikomanager (Risk Manager)
- interner_auditor (Internal Auditor)
- personalleitung (HR Manager)
- it_manager (IT Manager)

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from src.meta_adapter import MetaAdapter
from src.metadata_config_manager import MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo


class TestExtendedRolesInMetadata:
    """Test that all 6 new roles can be defined in metadata."""
    
    @pytest.fixture
    def extended_roles_config(self):
        """Create metadata config with all 6 extended roles."""
        return MetadataConfig(
            organization=OrganizationInfo(
                name="Test Organization",
                address="Test Street 123",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "sysop": PersonRole(
                    name="Michael Schneider",
                    title="System Administrator",
                    email="michael.schneider@test.com",
                    phone="+49 89 12345678-260",
                    department="IT Operations"
                ),
                "datenschutzbeauftragter": PersonRole(
                    name="Dr. Sarah Klein",
                    title="Data Protection Officer",
                    email="sarah.klein@test.com",
                    phone="+49 89 12345678-320",
                    department="Legal & Compliance"
                ),
                "risikomanager": PersonRole(
                    name="Frank Wagner",
                    title="Risk Manager",
                    email="frank.wagner@test.com",
                    phone="+49 89 12345678-350",
                    department="Risk Management"
                ),
                "interner_auditor": PersonRole(
                    name="Dr. Klaus Hoffmann",
                    title="Internal Auditor",
                    email="klaus.hoffmann@test.com",
                    phone="+49 89 12345678-360",
                    department="Internal Audit"
                ),
                "personalleitung": PersonRole(
                    name="Sabine Richter",
                    title="HR Manager",
                    email="sabine.richter@test.com",
                    phone="+49 89 12345678-600",
                    department="Human Resources"
                ),
                "it_manager": PersonRole(
                    name="Martin Bauer",
                    title="IT Manager",
                    email="martin.bauer@test.com",
                    phone="+49 89 12345678-240",
                    department="IT"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
    
    def test_all_extended_roles_defined(self, extended_roles_config):
        """Test that all 6 extended roles are defined in metadata."""
        expected_roles = [
            "sysop",
            "datenschutzbeauftragter",
            "risikomanager",
            "interner_auditor",
            "personalleitung",
            "it_manager"
        ]
        
        for role_key in expected_roles:
            role = extended_roles_config.get_role(role_key)
            assert role is not None, f"Role {role_key} should be defined"
            assert role.name is not None and len(role.name) > 0
            assert role.email is not None and '@' in role.email
            assert role.phone is not None and len(role.phone) > 0
    
    def test_sysop_role_fields(self, extended_roles_config):
        """Test sysop role has all required fields."""
        role = extended_roles_config.get_role("sysop")
        assert role.name == "Michael Schneider"
        assert role.title == "System Administrator"
        assert role.email == "michael.schneider@test.com"
        assert role.phone == "+49 89 12345678-260"
        assert role.department == "IT Operations"
    
    def test_datenschutzbeauftragter_role_fields(self, extended_roles_config):
        """Test datenschutzbeauftragter role has all required fields."""
        role = extended_roles_config.get_role("datenschutzbeauftragter")
        assert role.name == "Dr. Sarah Klein"
        assert role.title == "Data Protection Officer"
        assert role.email == "sarah.klein@test.com"
        assert role.phone == "+49 89 12345678-320"
        assert role.department == "Legal & Compliance"
    
    def test_risikomanager_role_fields(self, extended_roles_config):
        """Test risikomanager role has all required fields."""
        role = extended_roles_config.get_role("risikomanager")
        assert role.name == "Frank Wagner"
        assert role.title == "Risk Manager"
        assert role.email == "frank.wagner@test.com"
        assert role.phone == "+49 89 12345678-350"
        assert role.department == "Risk Management"
    
    def test_interner_auditor_role_fields(self, extended_roles_config):
        """Test interner_auditor role has all required fields."""
        role = extended_roles_config.get_role("interner_auditor")
        assert role.name == "Dr. Klaus Hoffmann"
        assert role.title == "Internal Auditor"
        assert role.email == "klaus.hoffmann@test.com"
        assert role.phone == "+49 89 12345678-360"
        assert role.department == "Internal Audit"
    
    def test_personalleitung_role_fields(self, extended_roles_config):
        """Test personalleitung role has all required fields."""
        role = extended_roles_config.get_role("personalleitung")
        assert role.name == "Sabine Richter"
        assert role.title == "HR Manager"
        assert role.email == "sabine.richter@test.com"
        assert role.phone == "+49 89 12345678-600"
        assert role.department == "Human Resources"
    
    def test_it_manager_role_fields(self, extended_roles_config):
        """Test it_manager role has all required fields."""
        role = extended_roles_config.get_role("it_manager")
        assert role.name == "Martin Bauer"
        assert role.title == "IT Manager"
        assert role.email == "martin.bauer@test.com"
        assert role.phone == "+49 89 12345678-240"
        assert role.department == "IT"


class TestExtendedRolePlaceholders:
    """Test that extended role placeholders work correctly."""
    
    @pytest.fixture
    def extended_roles_config(self):
        """Create metadata config with all 6 extended roles."""
        return MetadataConfig(
            organization=OrganizationInfo(
                name="Test Organization",
                address="Test Street 123",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "sysop": PersonRole(
                    name="Michael Schneider",
                    title="System Administrator",
                    email="michael.schneider@test.com",
                    phone="+49 89 12345678-260"
                ),
                "datenschutzbeauftragter": PersonRole(
                    name="Dr. Sarah Klein",
                    title="Data Protection Officer",
                    email="sarah.klein@test.com",
                    phone="+49 89 12345678-320"
                ),
                "risikomanager": PersonRole(
                    name="Frank Wagner",
                    title="Risk Manager",
                    email="frank.wagner@test.com",
                    phone="+49 89 12345678-350"
                ),
                "interner_auditor": PersonRole(
                    name="Dr. Klaus Hoffmann",
                    title="Internal Auditor",
                    email="klaus.hoffmann@test.com",
                    phone="+49 89 12345678-360"
                ),
                "personalleitung": PersonRole(
                    name="Sabine Richter",
                    title="HR Manager",
                    email="sabine.richter@test.com",
                    phone="+49 89 12345678-600"
                ),
                "it_manager": PersonRole(
                    name="Martin Bauer",
                    title="IT Manager",
                    email="martin.bauer@test.com",
                    phone="+49 89 12345678-240"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
    
    def test_sysop_placeholder_replacement(self, extended_roles_config):
        """Test {{ meta.sysop.* }} placeholder replacement."""
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        assert adapter.get_field("sysop.name") == "Michael Schneider"
        assert adapter.get_field("sysop.title") == "System Administrator"
        assert adapter.get_field("sysop.email") == "michael.schneider@test.com"
        assert adapter.get_field("sysop.phone") == "+49 89 12345678-260"
        
        adapter.disconnect()
    
    def test_datenschutzbeauftragter_placeholder_replacement(self, extended_roles_config):
        """Test {{ meta.datenschutzbeauftragter.* }} placeholder replacement."""
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        assert adapter.get_field("datenschutzbeauftragter.name") == "Dr. Sarah Klein"
        assert adapter.get_field("datenschutzbeauftragter.title") == "Data Protection Officer"
        assert adapter.get_field("datenschutzbeauftragter.email") == "sarah.klein@test.com"
        assert adapter.get_field("datenschutzbeauftragter.phone") == "+49 89 12345678-320"
        
        adapter.disconnect()
    
    def test_risikomanager_placeholder_replacement(self, extended_roles_config):
        """Test {{ meta.risikomanager.* }} placeholder replacement."""
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        assert adapter.get_field("risikomanager.name") == "Frank Wagner"
        assert adapter.get_field("risikomanager.title") == "Risk Manager"
        assert adapter.get_field("risikomanager.email") == "frank.wagner@test.com"
        assert adapter.get_field("risikomanager.phone") == "+49 89 12345678-350"
        
        adapter.disconnect()
    
    def test_interner_auditor_placeholder_replacement(self, extended_roles_config):
        """Test {{ meta.interner_auditor.* }} placeholder replacement."""
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        assert adapter.get_field("interner_auditor.name") == "Dr. Klaus Hoffmann"
        assert adapter.get_field("interner_auditor.title") == "Internal Auditor"
        assert adapter.get_field("interner_auditor.email") == "klaus.hoffmann@test.com"
        assert adapter.get_field("interner_auditor.phone") == "+49 89 12345678-360"
        
        adapter.disconnect()
    
    def test_personalleitung_placeholder_replacement(self, extended_roles_config):
        """Test {{ meta.personalleitung.* }} placeholder replacement."""
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        assert adapter.get_field("personalleitung.name") == "Sabine Richter"
        assert adapter.get_field("personalleitung.title") == "HR Manager"
        assert adapter.get_field("personalleitung.email") == "sabine.richter@test.com"
        assert adapter.get_field("personalleitung.phone") == "+49 89 12345678-600"
        
        adapter.disconnect()
    
    def test_it_manager_placeholder_replacement(self, extended_roles_config):
        """Test {{ meta.it_manager.* }} placeholder replacement."""
        adapter = MetaAdapter(extended_roles_config, language='de')
        adapter.connect()
        
        assert adapter.get_field("it_manager.name") == "Martin Bauer"
        assert adapter.get_field("it_manager.title") == "IT Manager"
        assert adapter.get_field("it_manager.email") == "martin.bauer@test.com"
        assert adapter.get_field("it_manager.phone") == "+49 89 12345678-240"
        
        adapter.disconnect()


class TestGermanToEnglishRoleTranslation:
    """Test German-to-English role title translation."""
    
    @pytest.fixture
    def german_roles_config(self):
        """Create metadata config with German role titles."""
        return MetadataConfig(
            organization=OrganizationInfo(
                name="Test Organization",
                address="Test Street 123",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "sysop": PersonRole(
                    name="Michael Schneider",
                    title="Systemadministrator",  # German
                    email="michael.schneider@test.com",
                    phone="+49 89 12345678-260"
                ),
                "datenschutzbeauftragter": PersonRole(
                    name="Dr. Sarah Klein",
                    title="Datenschutzbeauftragter",  # German
                    email="sarah.klein@test.com",
                    phone="+49 89 12345678-320"
                ),
                "risikomanager": PersonRole(
                    name="Frank Wagner",
                    title="Risikomanager",  # German
                    email="frank.wagner@test.com",
                    phone="+49 89 12345678-350"
                ),
                "interner_auditor": PersonRole(
                    name="Dr. Klaus Hoffmann",
                    title="Interner Auditor",  # German
                    email="klaus.hoffmann@test.com",
                    phone="+49 89 12345678-360"
                ),
                "personalleitung": PersonRole(
                    name="Sabine Richter",
                    title="Personalleitung",  # German
                    email="sabine.richter@test.com",
                    phone="+49 89 12345678-600"
                ),
                "it_manager": PersonRole(
                    name="Martin Bauer",
                    title="IT Manager",  # Already English
                    email="martin.bauer@test.com",
                    phone="+49 89 12345678-240"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
    
    def test_german_titles_in_german_templates(self, german_roles_config):
        """Test that German titles remain unchanged in German templates."""
        adapter = MetaAdapter(german_roles_config, language='de')
        adapter.connect()
        
        # German titles should remain unchanged
        assert adapter.get_field("sysop.title") == "Systemadministrator"
        assert adapter.get_field("datenschutzbeauftragter.title") == "Datenschutzbeauftragter"
        assert adapter.get_field("risikomanager.title") == "Risikomanager"
        assert adapter.get_field("interner_auditor.title") == "Interner Auditor"
        assert adapter.get_field("personalleitung.title") == "Personalleitung"
        assert adapter.get_field("it_manager.title") == "IT Manager"
        
        adapter.disconnect()
    
    def test_german_titles_translated_in_english_templates(self, german_roles_config):
        """Test that German titles are translated to English in English templates."""
        adapter = MetaAdapter(german_roles_config, language='en')
        adapter.connect()
        
        # German titles should be translated to English
        assert adapter.get_field("sysop.title") == "System Administrator"
        assert adapter.get_field("datenschutzbeauftragter.title") == "Data Protection Officer"
        assert adapter.get_field("risikomanager.title") == "Risk Manager"
        assert adapter.get_field("interner_auditor.title") == "Internal Auditor"
        assert adapter.get_field("personalleitung.title") == "HR Manager"
        assert adapter.get_field("it_manager.title") == "IT Manager"  # Already English
        
        adapter.disconnect()
    
    def test_translation_only_affects_title_field(self, german_roles_config):
        """Test that translation only affects title field, not name or other fields."""
        adapter = MetaAdapter(german_roles_config, language='en')
        adapter.connect()
        
        # Name should remain unchanged (German names are fine in English templates)
        assert adapter.get_field("sysop.name") == "Michael Schneider"
        assert adapter.get_field("datenschutzbeauftragter.name") == "Dr. Sarah Klein"
        
        # Email and phone should remain unchanged
        assert adapter.get_field("sysop.email") == "michael.schneider@test.com"
        assert adapter.get_field("sysop.phone") == "+49 89 12345678-260"
        
        adapter.disconnect()
    
    def test_all_translation_mappings(self, german_roles_config):
        """Test all German-to-English translation mappings."""
        adapter = MetaAdapter(german_roles_config, language='en')
        adapter.connect()
        
        expected_translations = {
            "sysop": "System Administrator",
            "datenschutzbeauftragter": "Data Protection Officer",
            "risikomanager": "Risk Manager",
            "interner_auditor": "Internal Auditor",
            "personalleitung": "HR Manager",
            "it_manager": "IT Manager"
        }
        
        for role_key, expected_english_title in expected_translations.items():
            actual_title = adapter.get_field(f"{role_key}.title")
            assert actual_title == expected_english_title, \
                f"Role {role_key}: expected '{expected_english_title}', got '{actual_title}'"
        
        adapter.disconnect()


class TestExtendedRolesIntegration:
    """Integration tests for extended roles with placeholder processor."""
    
    @pytest.fixture
    def extended_roles_config(self):
        """Create metadata config with all 6 extended roles."""
        return MetadataConfig(
            organization=OrganizationInfo(
                name="Test Organization",
                address="Test Street 123",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "sysop": PersonRole(
                    name="Michael Schneider",
                    title="System Administrator",
                    email="michael.schneider@test.com",
                    phone="+49 89 12345678-260"
                ),
                "datenschutzbeauftragter": PersonRole(
                    name="Dr. Sarah Klein",
                    title="Data Protection Officer",
                    email="sarah.klein@test.com",
                    phone="+49 89 12345678-320"
                ),
                "risikomanager": PersonRole(
                    name="Frank Wagner",
                    title="Risk Manager",
                    email="frank.wagner@test.com",
                    phone="+49 89 12345678-350"
                ),
                "interner_auditor": PersonRole(
                    name="Dr. Klaus Hoffmann",
                    title="Internal Auditor",
                    email="klaus.hoffmann@test.com",
                    phone="+49 89 12345678-360"
                ),
                "personalleitung": PersonRole(
                    name="Sabine Richter",
                    title="HR Manager",
                    email="sabine.richter@test.com",
                    phone="+49 89 12345678-600"
                ),
                "it_manager": PersonRole(
                    name="Martin Bauer",
                    title="IT Manager",
                    email="martin.bauer@test.com",
                    phone="+49 89 12345678-240"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
    
    def test_extended_roles_in_template_processing(self, extended_roles_config):
        """Test that extended roles work in template processing."""
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create meta adapter
        meta_adapter = MetaAdapter(extended_roles_config, language='de')
        meta_adapter.connect()
        
        # Create placeholder processor
        processor = PlaceholderProcessor(
            data_sources={'meta': meta_adapter}
        )
        
        # Template with extended role placeholders
        template = """
# IT Security Team

**System Administrator:** {{ meta.sysop.name }} ({{ meta.sysop.email }})
**Data Protection Officer:** {{ meta.datenschutzbeauftragter.name }} ({{ meta.datenschutzbeauftragter.email }})
**Risk Manager:** {{ meta.risikomanager.name }} ({{ meta.risikomanager.email }})
**Internal Auditor:** {{ meta.interner_auditor.name }} ({{ meta.interner_auditor.email }})
**HR Manager:** {{ meta.personalleitung.name }} ({{ meta.personalleitung.email }})
**IT Manager:** {{ meta.it_manager.name }} ({{ meta.it_manager.email }})
"""
        
        # Process template
        result = processor.process_template(template)
        
        # Verify all placeholders were replaced
        assert "Michael Schneider" in result.content
        assert "michael.schneider@test.com" in result.content
        assert "Dr. Sarah Klein" in result.content
        assert "sarah.klein@test.com" in result.content
        assert "Frank Wagner" in result.content
        assert "frank.wagner@test.com" in result.content
        assert "Dr. Klaus Hoffmann" in result.content
        assert "klaus.hoffmann@test.com" in result.content
        assert "Sabine Richter" in result.content
        assert "sabine.richter@test.com" in result.content
        assert "Martin Bauer" in result.content
        assert "martin.bauer@test.com" in result.content
        
        # Verify no placeholders remain
        assert "{{ meta." not in result.content
        assert "}}" not in result.content
        
        # Verify 12 replacements (6 roles × 2 fields each)
        assert len(result.replacements) == 12
        
        meta_adapter.disconnect()
