"""
Unit tests for MetadataRoleCleanup.

Tests duplicate role detection, role removal from YAML, role reorganization,
template reference updates, and role structure validation.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import tempfile
import shutil
import yaml
from src.metadata_standardizer import (
    MetadataRoleCleanup,
    DuplicateRole,
    ValidationResult
)


class TestMetadataRoleCleanup:
    """Unit tests for MetadataRoleCleanup class."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def sample_metadata_yaml(self, temp_dir):
        """Create a sample metadata.example.yaml file."""
        metadata_file = temp_dir / "metadata.example.yaml"
        
        content = """# Metadata Configuration
roles:
  # C-Level Executives
  ceo:
    title: "Chief Executive Officer"
    email: "ceo@example.com"
  
  cio:
    title: "Chief Information Officer"
    email: "cio@example.com"
  
  # IT Operations Roles
  it_operations_manager:
    title: "IT Operations Manager"
    email: "it-ops@example.com"
  
  service_desk_lead:
    title: "Service Desk Lead"
    email: "servicedesk@example.com"
  
  # BCM and Security Roles
  bcm_manager:
    title: "BCM Manager"
    email: "bcm@example.com"
  
  data_protection_officer:
    title: "Data Protection Officer"
    email: "dpo@example.com"
  
  datenschutzbeauftragter:
    title: "Datenschutzbeauftragter"
    email: "dsb@example.com"
  
  # Add Custom Roles Here
  it_manager:
    title: "IT Manager"
    email: "it-manager@example.com"
  
  sysop:
    title: "System Operator"
    email: "sysop@example.com"
"""
        metadata_file.write_text(content, encoding='utf-8')
        return metadata_file
    
    @pytest.fixture
    def role_cleanup(self, sample_metadata_yaml):
        """Create a MetadataRoleCleanup instance."""
        return MetadataRoleCleanup(str(sample_metadata_yaml))
    
    def test_init(self, sample_metadata_yaml):
        """Test MetadataRoleCleanup initialization."""
        cleanup = MetadataRoleCleanup(str(sample_metadata_yaml))
        
        assert cleanup.metadata_file == sample_metadata_yaml
        assert cleanup._yaml_content is None
        assert cleanup._roles_data is None
    
    def test_detect_duplicate_roles_with_duplicates(self, role_cleanup):
        """Test duplicate role detection when duplicates exist."""
        duplicates = role_cleanup.detect_duplicate_roles()
        
        assert isinstance(duplicates, list)
        assert len(duplicates) == 1
        assert duplicates[0].role_name == 'datenschutzbeauftragter'
        assert duplicates[0].canonical_role == 'data_protection_officer'
        assert 'Data Protection Officer' in duplicates[0].reason
    
    def test_detect_duplicate_roles_no_duplicates(self, temp_dir):
        """Test duplicate role detection when no duplicates exist."""
        metadata_file = temp_dir / "metadata.example.yaml"
        
        content = """roles:
  ceo:
    title: "CEO"
  
  data_protection_officer:
    title: "Data Protection Officer"
"""
        metadata_file.write_text(content, encoding='utf-8')
        
        cleanup = MetadataRoleCleanup(str(metadata_file))
        duplicates = cleanup.detect_duplicate_roles()
        
        assert isinstance(duplicates, list)
        assert len(duplicates) == 0
    
    def test_detect_duplicate_roles_missing_file(self, temp_dir):
        """Test duplicate role detection with non-existent file."""
        cleanup = MetadataRoleCleanup(str(temp_dir / "nonexistent.yaml"))
        duplicates = cleanup.detect_duplicate_roles()
        
        assert isinstance(duplicates, list)
        assert len(duplicates) == 0
    
    def test_detect_duplicate_roles_no_roles_section(self, temp_dir):
        """Test duplicate role detection when roles section is missing."""
        metadata_file = temp_dir / "metadata.example.yaml"
        metadata_file.write_text("other_section:\n  key: value\n", encoding='utf-8')
        
        cleanup = MetadataRoleCleanup(str(metadata_file))
        duplicates = cleanup.detect_duplicate_roles()
        
        assert isinstance(duplicates, list)
        assert len(duplicates) == 0
    
    def test_remove_duplicate_role_success(self, role_cleanup, sample_metadata_yaml):
        """Test successful removal of duplicate role."""
        result = role_cleanup.remove_duplicate_role('datenschutzbeauftragter')
        
        assert result is True
        
        # Verify role was removed
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        assert 'datenschutzbeauftragter' not in data['roles']
        assert 'data_protection_officer' in data['roles']
    
    def test_remove_duplicate_role_preserves_other_roles(self, role_cleanup, sample_metadata_yaml):
        """Test that removing a role preserves other roles."""
        # Get original roles
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            original_data = yaml.safe_load(f)
        original_roles = set(original_data['roles'].keys())
        
        # Remove duplicate role
        role_cleanup.remove_duplicate_role('datenschutzbeauftragter')
        
        # Verify other roles preserved
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            new_data = yaml.safe_load(f)
        new_roles = set(new_data['roles'].keys())
        
        expected_roles = original_roles - {'datenschutzbeauftragter'}
        assert new_roles == expected_roles
    
    def test_remove_duplicate_role_preserves_formatting(self, role_cleanup, sample_metadata_yaml):
        """Test that removing a role preserves YAML formatting and comments."""
        # Read original content
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Remove role
        role_cleanup.remove_duplicate_role('datenschutzbeauftragter')
        
        # Read new content
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            new_content = f.read()
        
        # Verify comments preserved
        assert '# C-Level Executives' in new_content
        assert '# IT Operations Roles' in new_content
        assert '# BCM and Security Roles' in new_content
        
        # Verify role removed
        assert 'datenschutzbeauftragter:' not in new_content
    
    def test_remove_duplicate_role_nonexistent_role(self, role_cleanup, sample_metadata_yaml):
        """Test removing a role that doesn't exist."""
        result = role_cleanup.remove_duplicate_role('nonexistent_role')
        
        # Should still return True (no error)
        assert result is True
        
        # Verify file unchanged
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        assert 'nonexistent_role' not in data['roles']
    
    def test_remove_duplicate_role_missing_file(self, temp_dir):
        """Test removing a role from non-existent file."""
        cleanup = MetadataRoleCleanup(str(temp_dir / "nonexistent.yaml"))
        result = cleanup.remove_duplicate_role('some_role')
        
        assert result is False
    
    def test_reorganize_it_operations_roles_success(self, role_cleanup, sample_metadata_yaml):
        """Test successful reorganization of IT operations roles."""
        result = role_cleanup.reorganize_it_operations_roles()
        
        assert result is True
        
        # Verify roles moved
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        role_names = list(data['roles'].keys())
        
        # Find indices
        service_desk_idx = role_names.index('service_desk_lead')
        it_manager_idx = role_names.index('it_manager')
        sysop_idx = role_names.index('sysop')
        
        # Verify it_manager and sysop come after service_desk_lead
        assert it_manager_idx > service_desk_idx
        assert sysop_idx > service_desk_idx
        assert sysop_idx > it_manager_idx
    
    def test_reorganize_it_operations_roles_preserves_data(self, role_cleanup, sample_metadata_yaml):
        """Test that reorganization preserves role data."""
        # Get original role data
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            original_data = yaml.safe_load(f)
        original_it_manager = original_data['roles']['it_manager']
        original_sysop = original_data['roles']['sysop']
        
        # Reorganize
        role_cleanup.reorganize_it_operations_roles()
        
        # Verify data preserved
        with open(sample_metadata_yaml, 'r', encoding='utf-8') as f:
            new_data = yaml.safe_load(f)
        
        assert new_data['roles']['it_manager'] == original_it_manager
        assert new_data['roles']['sysop'] == original_sysop
    
    def test_reorganize_it_operations_roles_missing_file(self, temp_dir):
        """Test reorganization with non-existent file."""
        cleanup = MetadataRoleCleanup(str(temp_dir / "nonexistent.yaml"))
        result = cleanup.reorganize_it_operations_roles()
        
        assert result is False
    
    def test_reorganize_it_operations_roles_already_organized(self, temp_dir):
        """Test reorganization when roles are already in correct position."""
        metadata_file = temp_dir / "metadata.example.yaml"
        
        content = """roles:
  service_desk_lead:
    title: "Service Desk Lead"
  
  it_manager:
    title: "IT Manager"
  
  sysop:
    title: "System Operator"
"""
        metadata_file.write_text(content, encoding='utf-8')
        
        cleanup = MetadataRoleCleanup(str(metadata_file))
        result = cleanup.reorganize_it_operations_roles()
        
        # Should return True (no error)
        assert result is True
    
    def test_reorganize_it_operations_roles_missing_roles(self, temp_dir):
        """Test reorganization when target roles don't exist."""
        metadata_file = temp_dir / "metadata.example.yaml"
        
        content = """roles:
  ceo:
    title: "CEO"
  
  service_desk_lead:
    title: "Service Desk Lead"
"""
        metadata_file.write_text(content, encoding='utf-8')
        
        cleanup = MetadataRoleCleanup(str(metadata_file))
        result = cleanup.reorganize_it_operations_roles()
        
        # Should return True (no roles to move)
        assert result is True
    
    def test_validate_role_structure_valid(self, temp_dir):
        """Test role structure validation with valid structure."""
        metadata_file = temp_dir / "metadata.example.yaml"
        
        content = """roles:
  ceo:
    title: "CEO"
  
  service_desk_lead:
    title: "Service Desk Lead"
  
  it_manager:
    title: "IT Manager"
  
  sysop:
    title: "System Operator"
  
  data_protection_officer:
    title: "Data Protection Officer"
"""
        metadata_file.write_text(content, encoding='utf-8')
        
        cleanup = MetadataRoleCleanup(str(metadata_file))
        result = cleanup.validate_role_structure()
        
        assert isinstance(result, ValidationResult)
        assert result.is_valid
        assert len(result.invalid_fields) == 0
    
    def test_validate_role_structure_with_duplicates(self, role_cleanup):
        """Test role structure validation with duplicate roles."""
        result = role_cleanup.validate_role_structure()
        
        assert isinstance(result, ValidationResult)
        assert not result.is_valid
        assert len(result.invalid_fields) == 1
        assert 'datenschutzbeauftragter' in result.invalid_fields[0]
    
    def test_validate_role_structure_wrong_order(self, temp_dir):
        """Test role structure validation with incorrect role order."""
        metadata_file = temp_dir / "metadata.example.yaml"
        
        content = """roles:
  it_manager:
    title: "IT Manager"
  
  service_desk_lead:
    title: "Service Desk Lead"
  
  sysop:
    title: "System Operator"
"""
        metadata_file.write_text(content, encoding='utf-8')
        
        cleanup = MetadataRoleCleanup(str(metadata_file))
        result = cleanup.validate_role_structure()
        
        assert isinstance(result, ValidationResult)
        # Should have warnings about role order
        assert len(result.warnings) > 0
        assert any('it_manager' in w for w in result.warnings)
    
    def test_validate_role_structure_missing_file(self, temp_dir):
        """Test role structure validation with non-existent file."""
        cleanup = MetadataRoleCleanup(str(temp_dir / "nonexistent.yaml"))
        result = cleanup.validate_role_structure()
        
        assert isinstance(result, ValidationResult)
        assert not result.is_valid
        assert len(result.warnings) > 0
    
    def test_validate_role_structure_no_roles_section(self, temp_dir):
        """Test role structure validation when roles section is missing."""
        metadata_file = temp_dir / "metadata.example.yaml"
        metadata_file.write_text("other_section:\n  key: value\n", encoding='utf-8')
        
        cleanup = MetadataRoleCleanup(str(metadata_file))
        result = cleanup.validate_role_structure()
        
        assert isinstance(result, ValidationResult)
        assert not result.is_valid
        assert len(result.warnings) > 0
    
    def test_update_template_references_success(self, role_cleanup, temp_dir):
        """Test successful update of template references."""
        # Create templates directory
        templates_dir = temp_dir / "templates"
        templates_dir.mkdir()
        
        de_dir = templates_dir / "de" / "gdpr"
        de_dir.mkdir(parents=True)
        
        # Create template with old role reference
        template_file = de_dir / "0001_template.md"
        content = """# GDPR Template

Verantwortlicher: {{ meta.datenschutzbeauftragter.name }}
Email: {{ meta.datenschutzbeauftragter.email }}

Some other content.
"""
        template_file.write_text(content, encoding='utf-8')
        
        # Update references
        files_updated = role_cleanup.update_template_references(
            'datenschutzbeauftragter',
            'data_protection_officer',
            str(templates_dir)
        )
        
        assert files_updated == 1
        
        # Verify content updated
        new_content = template_file.read_text(encoding='utf-8')
        assert 'meta.datenschutzbeauftragter' not in new_content
        assert '{{ meta.data_protection_officer.name }}' in new_content
        assert '{{ meta.data_protection_officer.email }}' in new_content
    
    def test_update_template_references_multiple_files(self, role_cleanup, temp_dir):
        """Test updating references across multiple template files."""
        templates_dir = temp_dir / "templates"
        templates_dir.mkdir()
        
        # Create multiple templates with old role reference
        for lang in ['de', 'en']:
            for framework in ['gdpr', 'isms']:
                framework_dir = templates_dir / lang / framework
                framework_dir.mkdir(parents=True)
                
                template_file = framework_dir / "0001_template.md"
                content = f"Contact: {{{{ meta.datenschutzbeauftragter.email }}}}"
                template_file.write_text(content, encoding='utf-8')
        
        # Update references
        files_updated = role_cleanup.update_template_references(
            'datenschutzbeauftragter',
            'data_protection_officer',
            str(templates_dir)
        )
        
        assert files_updated == 4
    
    def test_update_template_references_no_matches(self, role_cleanup, temp_dir):
        """Test updating references when no templates contain the old role."""
        templates_dir = temp_dir / "templates"
        templates_dir.mkdir()
        
        de_dir = templates_dir / "de" / "gdpr"
        de_dir.mkdir(parents=True)
        
        template_file = de_dir / "0001_template.md"
        content = "# Template without old role reference"
        template_file.write_text(content, encoding='utf-8')
        
        files_updated = role_cleanup.update_template_references(
            'datenschutzbeauftragter',
            'data_protection_officer',
            str(templates_dir)
        )
        
        assert files_updated == 0
    
    def test_update_template_references_preserves_other_content(self, role_cleanup, temp_dir):
        """Test that updating references preserves other template content."""
        templates_dir = temp_dir / "templates"
        templates_dir.mkdir()
        
        de_dir = templates_dir / "de" / "gdpr"
        de_dir.mkdir(parents=True)
        
        template_file = de_dir / "0001_template.md"
        content = """# GDPR Template

## Section 1

Contact: {{ meta.datenschutzbeauftragter.email }}

## Section 2

Other role: {{ meta.ceo.name }}

## Section 3

More content here.
"""
        template_file.write_text(content, encoding='utf-8')
        
        # Update references
        role_cleanup.update_template_references(
            'datenschutzbeauftragter',
            'data_protection_officer',
            str(templates_dir)
        )
        
        # Verify other content preserved
        new_content = template_file.read_text(encoding='utf-8')
        assert '# GDPR Template' in new_content
        assert '## Section 1' in new_content
        assert '## Section 2' in new_content
        assert '## Section 3' in new_content
        assert '{{ meta.ceo.name }}' in new_content
        assert 'More content here.' in new_content
    
    def test_update_template_references_missing_templates_dir(self, role_cleanup, temp_dir):
        """Test updating references with non-existent templates directory."""
        files_updated = role_cleanup.update_template_references(
            'datenschutzbeauftragter',
            'data_protection_officer',
            str(temp_dir / "nonexistent")
        )
        
        assert files_updated == 0
    
    def test_update_template_references_multiple_occurrences(self, role_cleanup, temp_dir):
        """Test updating multiple occurrences in same file."""
        templates_dir = temp_dir / "templates"
        templates_dir.mkdir()
        
        de_dir = templates_dir / "de" / "gdpr"
        de_dir.mkdir(parents=True)
        
        template_file = de_dir / "0001_template.md"
        content = """# Template

Name: {{ meta.datenschutzbeauftragter.name }}
Email: {{ meta.datenschutzbeauftragter.email }}
Phone: {{ meta.datenschutzbeauftragter.phone }}
"""
        template_file.write_text(content, encoding='utf-8')
        
        # Update references
        files_updated = role_cleanup.update_template_references(
            'datenschutzbeauftragter',
            'data_protection_officer',
            str(templates_dir)
        )
        
        assert files_updated == 1
        
        # Verify all occurrences updated
        new_content = template_file.read_text(encoding='utf-8')
        assert new_content.count('meta.datenschutzbeauftragter') == 0
        assert new_content.count('meta.data_protection_officer') == 3


class TestDuplicateRole:
    """Unit tests for DuplicateRole dataclass."""
    
    def test_duplicate_role_creation(self):
        """Test DuplicateRole dataclass creation."""
        dup = DuplicateRole(
            role_name='datenschutzbeauftragter',
            canonical_role='data_protection_officer',
            reason='German name for Data Protection Officer'
        )
        
        assert dup.role_name == 'datenschutzbeauftragter'
        assert dup.canonical_role == 'data_protection_officer'
        assert dup.reason == 'German name for Data Protection Officer'
    
    def test_duplicate_role_attributes(self):
        """Test DuplicateRole attributes are accessible."""
        dup = DuplicateRole(
            role_name='test_role',
            canonical_role='canonical_role',
            reason='Test reason'
        )
        
        assert hasattr(dup, 'role_name')
        assert hasattr(dup, 'canonical_role')
        assert hasattr(dup, 'reason')
