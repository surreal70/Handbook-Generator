"""
Unit tests for Service Directory Reorganization.

Tests directory creation, file moving, rollback on errors, and cleanup of old directories.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from pathlib import Path
import tempfile
import shutil
import sys

# Add helpers directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'helpers'))

from reorganize_service_directory import ServiceDirectoryReorganizer


class TestServiceDirectoryReorganizer:
    """Unit tests for ServiceDirectoryReorganizer class."""
    
    @pytest.fixture
    def temp_templates_dir(self):
        """Create a temporary templates directory for testing."""
        temp_dir = tempfile.mkdtemp()
        templates_dir = Path(temp_dir) / "templates"
        templates_dir.mkdir()
        
        # Create language directories
        (templates_dir / "de").mkdir()
        (templates_dir / "en").mkdir()
        
        # Create old structure directories with some files
        de_email_service = templates_dir / "de" / "email-service"
        de_email_service.mkdir()
        (de_email_service / "test_file.md").write_text("Test content", encoding='utf-8')
        
        de_service_templates = templates_dir / "de" / "service-templates"
        de_service_templates.mkdir()
        (de_service_templates / "template1.md").write_text("Template 1", encoding='utf-8')
        
        en_service_templates = templates_dir / "en" / "service-templates"
        en_service_templates.mkdir()
        (en_service_templates / "template2.md").write_text("Template 2", encoding='utf-8')
        
        yield templates_dir
        
        # Cleanup
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def reorganizer(self, temp_templates_dir):
        """Create a ServiceDirectoryReorganizer instance with temp directory."""
        return ServiceDirectoryReorganizer(str(temp_templates_dir))
    
    def test_init(self, temp_templates_dir):
        """Test ServiceDirectoryReorganizer initialization."""
        reorganizer = ServiceDirectoryReorganizer(str(temp_templates_dir))
        
        assert reorganizer.templates_dir == temp_templates_dir
        assert reorganizer.backup_dir is None
        assert len(reorganizer.moves_performed) == 0
    
    def test_validate_environment_success(self, reorganizer):
        """Test environment validation with valid structure."""
        result = reorganizer.validate_environment()
        
        assert result is True
    
    def test_validate_environment_missing_templates_dir(self):
        """Test environment validation with missing templates directory."""
        reorganizer = ServiceDirectoryReorganizer("/nonexistent/templates")
        
        result = reorganizer.validate_environment()
        
        assert result is False
    
    def test_validate_environment_partial_structure(self, temp_templates_dir):
        """Test environment validation with partial structure."""
        # Remove one of the source directories
        shutil.rmtree(temp_templates_dir / "de" / "email-service")
        
        reorganizer = ServiceDirectoryReorganizer(str(temp_templates_dir))
        result = reorganizer.validate_environment()
        
        # Should still return True but with warnings
        assert result is True
    
    def test_create_backup_success(self, reorganizer, temp_templates_dir):
        """Test successful backup creation."""
        result = reorganizer.create_backup()
        
        assert result is True
        assert reorganizer.backup_dir is not None
        assert reorganizer.backup_dir.exists()
        
        # Verify backup contains the same structure
        assert (reorganizer.backup_dir / "de" / "email-service").exists()
        assert (reorganizer.backup_dir / "de" / "service-templates").exists()
        assert (reorganizer.backup_dir / "en" / "service-templates").exists()
    
    def test_create_backup_removes_existing(self, reorganizer, temp_templates_dir):
        """Test that existing backup is removed before creating new one."""
        # Create first backup
        reorganizer.create_backup()
        first_backup = reorganizer.backup_dir
        
        # Create second backup
        reorganizer.create_backup()
        second_backup = reorganizer.backup_dir
        
        assert first_backup == second_backup
        assert second_backup.exists()
    
    def test_create_service_directories_success(self, reorganizer, temp_templates_dir):
        """Test successful service directory creation."""
        result = reorganizer.create_service_directories()
        
        assert result is True
        assert (temp_templates_dir / "de" / "service-directory").exists()
        assert (temp_templates_dir / "en" / "service-directory").exists()
    
    def test_create_service_directories_already_exist(self, reorganizer, temp_templates_dir):
        """Test service directory creation when directories already exist."""
        # Create directories first
        (temp_templates_dir / "de" / "service-directory").mkdir()
        (temp_templates_dir / "en" / "service-directory").mkdir()
        
        result = reorganizer.create_service_directories()
        
        # Should still succeed (exist_ok=True)
        assert result is True
    
    def test_move_directory_success(self, reorganizer, temp_templates_dir):
        """Test successful directory move."""
        source = temp_templates_dir / "de" / "email-service"
        destination = temp_templates_dir / "de" / "service-directory" / "email-service"
        
        # Create destination parent
        (temp_templates_dir / "de" / "service-directory").mkdir()
        
        result = reorganizer.move_directory(source, destination)
        
        assert result is True
        assert not source.exists()
        assert destination.exists()
        assert (destination / "test_file.md").exists()
        assert len(reorganizer.moves_performed) == 1
    
    def test_move_directory_source_not_exists(self, reorganizer, temp_templates_dir):
        """Test move when source directory doesn't exist."""
        source = temp_templates_dir / "de" / "nonexistent"
        destination = temp_templates_dir / "de" / "service-directory" / "nonexistent"
        
        result = reorganizer.move_directory(source, destination)
        
        # Should return True (not an error if already moved)
        assert result is True
    
    def test_move_directory_destination_exists(self, reorganizer, temp_templates_dir):
        """Test move when destination already exists."""
        source = temp_templates_dir / "de" / "email-service"
        destination = temp_templates_dir / "de" / "service-directory" / "email-service"
        
        # Create destination parent and destination
        (temp_templates_dir / "de" / "service-directory").mkdir()
        destination.mkdir()
        (destination / "old_file.md").write_text("Old content", encoding='utf-8')
        
        result = reorganizer.move_directory(source, destination)
        
        assert result is True
        assert destination.exists()
        # Should have new content, not old
        assert (destination / "test_file.md").exists()
        assert not (destination / "old_file.md").exists()
    
    def test_perform_reorganization_success(self, reorganizer, temp_templates_dir):
        """Test complete reorganization process."""
        # Create service directories first
        reorganizer.create_service_directories()
        
        result = reorganizer.perform_reorganization()
        
        assert result is True
        
        # Verify new structure
        assert (temp_templates_dir / "de" / "service-directory" / "email-service").exists()
        assert (temp_templates_dir / "de" / "service-directory" / "service-templates").exists()
        assert (temp_templates_dir / "en" / "service-directory" / "service-templates").exists()
        
        # Verify old structure is gone
        assert not (temp_templates_dir / "de" / "email-service").exists()
        assert not (temp_templates_dir / "de" / "service-templates").exists()
        assert not (temp_templates_dir / "en" / "service-templates").exists()
        
        # Verify files were moved
        assert (temp_templates_dir / "de" / "service-directory" / "email-service" / "test_file.md").exists()
        assert (temp_templates_dir / "de" / "service-directory" / "service-templates" / "template1.md").exists()
        assert (temp_templates_dir / "en" / "service-directory" / "service-templates" / "template2.md").exists()
    
    def test_verify_reorganization_success(self, reorganizer, temp_templates_dir):
        """Test verification of successful reorganization."""
        # Perform reorganization
        reorganizer.create_service_directories()
        reorganizer.perform_reorganization()
        
        result = reorganizer.verify_reorganization()
        
        assert result is True
    
    def test_verify_reorganization_missing_directory(self, reorganizer, temp_templates_dir):
        """Test verification fails when required directory is missing."""
        # Create service directories but don't move files
        reorganizer.create_service_directories()
        
        result = reorganizer.verify_reorganization()
        
        # Should fail because directories are empty or files not moved
        assert result is False
    
    def test_verify_reorganization_old_directory_exists(self, reorganizer, temp_templates_dir):
        """Test verification fails when old directory still exists."""
        # Create new structure
        reorganizer.create_service_directories()
        reorganizer.perform_reorganization()
        
        # Recreate an old directory
        (temp_templates_dir / "de" / "email-service").mkdir()
        
        result = reorganizer.verify_reorganization()
        
        assert result is False
    
    def test_rollback_success(self, reorganizer, temp_templates_dir):
        """Test successful rollback."""
        # Create backup
        reorganizer.create_backup()
        
        # Make some changes
        reorganizer.create_service_directories()
        shutil.rmtree(temp_templates_dir / "de" / "email-service")
        
        # Rollback
        result = reorganizer.rollback()
        
        assert result is True
        assert (temp_templates_dir / "de" / "email-service").exists()
    
    def test_rollback_no_backup(self, reorganizer):
        """Test rollback fails when no backup exists."""
        result = reorganizer.rollback()
        
        assert result is False
    
    def test_cleanup_backup(self, reorganizer):
        """Test backup cleanup."""
        # Create backup
        reorganizer.create_backup()
        backup_dir = reorganizer.backup_dir
        
        assert backup_dir.exists()
        
        # Cleanup
        reorganizer.cleanup_backup()
        
        assert not backup_dir.exists()
    
    def test_cleanup_backup_no_backup(self, reorganizer):
        """Test cleanup when no backup exists."""
        # Should not raise an error
        reorganizer.cleanup_backup()
    
    def test_generate_report(self, reorganizer, temp_templates_dir):
        """Test report generation."""
        # Perform some moves
        reorganizer.create_service_directories()
        reorganizer.perform_reorganization()
        
        report = reorganizer.generate_report()
        
        assert isinstance(report, dict)
        assert "directories_moved" in report
        assert "moves" in report
        assert report["directories_moved"] == 3  # Three directories moved
        assert len(report["moves"]) == 3
    
    def test_run_complete_success(self, reorganizer, temp_templates_dir):
        """Test complete run with all steps."""
        result = reorganizer.run(create_backup=True, keep_backup=False)
        
        assert result is True
        
        # Verify reorganization
        assert (temp_templates_dir / "de" / "service-directory" / "email-service").exists()
        assert (temp_templates_dir / "de" / "service-directory" / "service-templates").exists()
        assert (temp_templates_dir / "en" / "service-directory" / "service-templates").exists()
        
        # Verify old structure is gone
        assert not (temp_templates_dir / "de" / "email-service").exists()
        assert not (temp_templates_dir / "de" / "service-templates").exists()
        assert not (temp_templates_dir / "en" / "service-templates").exists()
        
        # Verify backup was cleaned up
        assert reorganizer.backup_dir is None or not reorganizer.backup_dir.exists()
    
    def test_run_with_keep_backup(self, reorganizer, temp_templates_dir):
        """Test complete run keeping backup."""
        result = reorganizer.run(create_backup=True, keep_backup=True)
        
        assert result is True
        
        # Verify backup still exists
        assert reorganizer.backup_dir is not None
        assert reorganizer.backup_dir.exists()
    
    def test_run_without_backup(self, reorganizer, temp_templates_dir):
        """Test complete run without creating backup."""
        result = reorganizer.run(create_backup=False, keep_backup=False)
        
        assert result is True
        assert reorganizer.backup_dir is None
    
    def test_run_rollback_on_failure(self, reorganizer, temp_templates_dir):
        """Test rollback occurs on failure."""
        # Create backup
        reorganizer.create_backup()
        
        # Make one of the source directories read-only to cause failure
        # Remove a directory to simulate missing source
        shutil.rmtree(temp_templates_dir / "de" / "email-service")
        
        # Run should fail because verification will fail (missing directory)
        result = reorganizer.run(create_backup=False, keep_backup=False)
        
        # Should fail because email-service directory is missing
        assert result is False
    
    def test_moves_performed_tracking(self, reorganizer, temp_templates_dir):
        """Test that moves are tracked correctly."""
        reorganizer.create_service_directories()
        reorganizer.perform_reorganization()
        
        assert len(reorganizer.moves_performed) == 3
        
        # Verify each move is recorded
        move_sources = [str(source) for source, _ in reorganizer.moves_performed]
        assert any("email-service" in source for source in move_sources)
        assert any("service-templates" in source for source in move_sources)
    
    def test_file_content_preservation(self, reorganizer, temp_templates_dir):
        """Test that file contents are preserved during move."""
        # Get original content
        original_content = (temp_templates_dir / "de" / "email-service" / "test_file.md").read_text(encoding='utf-8')
        
        # Perform reorganization
        reorganizer.run(create_backup=False)
        
        # Verify content is preserved
        new_path = temp_templates_dir / "de" / "service-directory" / "email-service" / "test_file.md"
        new_content = new_path.read_text(encoding='utf-8')
        
        assert new_content == original_content
    
    def test_directory_structure_preservation(self, reorganizer, temp_templates_dir):
        """Test that directory structure is preserved during move."""
        # Create subdirectory in source
        subdir = temp_templates_dir / "de" / "email-service" / "subdir"
        subdir.mkdir()
        (subdir / "nested_file.md").write_text("Nested content", encoding='utf-8')
        
        # Perform reorganization
        reorganizer.run(create_backup=False)
        
        # Verify subdirectory structure is preserved
        new_subdir = temp_templates_dir / "de" / "service-directory" / "email-service" / "subdir"
        assert new_subdir.exists()
        assert (new_subdir / "nested_file.md").exists()
        assert (new_subdir / "nested_file.md").read_text(encoding='utf-8') == "Nested content"
