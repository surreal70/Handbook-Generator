"""
Tests for Framework Mapping Validator.

This module contains both unit tests and property-based tests for the
FrameworkMappingValidator component of the quality control system.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import os
import tempfile
import pytest
from pathlib import Path
from hypothesis import given, strategies as st

from src.quality_control.framework_mapping_validator import FrameworkMappingValidator
from src.quality_control.data_structures import FrameworkInfo, ValidationResult


class TestFrameworkMappingValidatorProperties:
    """Property-based tests for FrameworkMappingValidator."""
    
    @given(st.lists(st.text(min_size=1, max_size=50, alphabet=st.characters(
        whitelist_categories=('Lu', 'Ll', 'Nd'), 
        whitelist_characters='-_'
    )), min_size=0, max_size=20, unique=True))
    def test_property_1_complete_framework_discovery(self, framework_names):
        """
        Feature: quality-control-and-framework-documentation
        Property 1: Complete Framework Discovery
        
        **Validates: Requirements 1.1, 2.1, 4.1**
        
        For any directory structure containing framework directories,
        the system should discover all frameworks without omission.
        """
        # Setup: Create temporary directory structure
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create framework directories for both languages
            for name in framework_names:
                os.makedirs(os.path.join(tmpdir, "templates", "de", name), exist_ok=True)
                os.makedirs(os.path.join(tmpdir, "templates", "en", name), exist_ok=True)
            
            # Execute: Scan frameworks
            validator = FrameworkMappingValidator(tmpdir)
            discovered = validator.scan_frameworks()
            
            # Verify: All frameworks discovered (each framework appears twice: de and en)
            discovered_names = {f.name for f in discovered}
            expected_names = set(framework_names)
            
            # Property: All expected frameworks are discovered
            assert discovered_names == expected_names, \
                f"Missing frameworks: {expected_names - discovered_names}, " \
                f"Extra frameworks: {discovered_names - expected_names}"
            
            # Property: Each framework appears exactly twice (de and en)
            if framework_names:  # Only check if we have frameworks
                for name in framework_names:
                    frameworks_with_name = [f for f in discovered if f.name == name]
                    assert len(frameworks_with_name) == 2, \
                        f"Framework {name} should appear twice (de and en), found {len(frameworks_with_name)}"
                    
                    languages = {f.language for f in frameworks_with_name}
                    assert languages == {'de', 'en'}, \
                        f"Framework {name} should have both de and en, found {languages}"
    
    @given(st.lists(st.tuples(
        st.text(min_size=1, max_size=50, alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'), 
            whitelist_characters='-_'
        )),
        st.booleans()  # has_correct_mapping_file
    ), min_size=0, max_size=20, unique_by=lambda x: x[0]))
    def test_property_2_universal_file_validation(self, framework_configs):
        """
        Feature: quality-control-and-framework-documentation
        Property 2: Universal File Validation
        
        **Validates: Requirements 1.2, 1.4**
        
        For any framework directory, the system should correctly identify
        whether the 9999_Framework_Mapping.md file exists and is correctly named.
        """
        # Setup: Create temporary directory structure
        with tempfile.TemporaryDirectory() as tmpdir:
            expected_correct = []
            expected_missing = []
            
            for framework_name, has_correct_file in framework_configs:
                framework_dir = os.path.join(tmpdir, "templates", "de", framework_name)
                os.makedirs(framework_dir, exist_ok=True)
                
                if has_correct_file:
                    # Create correctly named mapping file
                    mapping_file = os.path.join(framework_dir, "9999_Framework_Mapping.md")
                    Path(mapping_file).touch()
                    expected_correct.append(framework_name)
                else:
                    expected_missing.append(framework_name)
            
            # Execute: Scan and validate frameworks
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            result = validator.validate_mapping_files(frameworks)
            
            # Verify: Correct identification of mapping files
            valid_names = {f.name for f in frameworks if f.has_mapping_file}
            invalid_names = {f.name for f in frameworks if not f.has_mapping_file}
            
            # Property: All frameworks with correct files are identified as valid
            assert valid_names == set(expected_correct), \
                f"Expected valid: {set(expected_correct)}, Got: {valid_names}"
            
            # Property: All frameworks without correct files are identified as invalid
            assert invalid_names == set(expected_missing), \
                f"Expected invalid: {set(expected_missing)}, Got: {invalid_names}"
            
            # Property: Validation result counts match
            assert result.valid_frameworks == len(expected_correct)
            assert len(result.missing_files) == len(expected_missing)
            assert result.total_frameworks == len(framework_configs)
    
    @given(st.lists(st.tuples(
        st.text(min_size=1, max_size=50, alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd'), 
            whitelist_characters='-_'
        )),
        st.sampled_from(['correct', 'incorrect', 'missing'])  # file status
    ), min_size=0, max_size=20, unique_by=lambda x: x[0]))
    def test_property_3_complete_error_reporting(self, framework_configs):
        """
        Feature: quality-control-and-framework-documentation
        Property 3: Complete Error Reporting
        
        **Validates: Requirements 1.3, 1.4, 2.3, 2.5, 4.6**
        
        For any set of validation errors (missing files, incorrect names),
        the system should report all errors without omission.
        """
        # Setup: Create temporary directory structure with various error conditions
        with tempfile.TemporaryDirectory() as tmpdir:
            expected_valid = []
            expected_invalid = []
            expected_missing = []
            
            for framework_name, file_status in framework_configs:
                framework_dir = os.path.join(tmpdir, "templates", "de", framework_name)
                os.makedirs(framework_dir, exist_ok=True)
                
                if file_status == 'correct':
                    # Create correctly named mapping file
                    mapping_file = os.path.join(framework_dir, "9999_Framework_Mapping.md")
                    Path(mapping_file).touch()
                    expected_valid.append(framework_name)
                elif file_status == 'incorrect':
                    # Create incorrectly named mapping file
                    mapping_file = os.path.join(framework_dir, "9999_Framework_Mapping.md")
                    Path(mapping_file).touch()
                    expected_invalid.append(framework_name)
                else:  # missing
                    expected_missing.append(framework_name)
            
            # Execute: Scan, validate, and generate report
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            result = validator.validate_mapping_files(frameworks)
            report = validator.generate_report(result)
            
            # Verify: All errors are reported
            # Property: All invalid frameworks are in the result
            invalid_names = {f.name for f in result.invalid_frameworks}
            assert invalid_names == set(expected_invalid), \
                f"Expected invalid: {set(expected_invalid)}, Got: {invalid_names}"
            
            # Property: All missing files are in the result
            missing_names = {f.name for f in result.missing_files}
            assert missing_names == set(expected_missing), \
                f"Expected missing: {set(expected_missing)}, Got: {missing_names}"
            
            # Property: Report contains all framework names with errors
            for framework_name in expected_invalid:
                assert framework_name in report, \
                    f"Framework {framework_name} with incorrect file not in report"
            
            for framework_name in expected_missing:
                assert framework_name in report, \
                    f"Framework {framework_name} with missing file not in report"
            
            # Property: Success status is correct
            has_errors = len(expected_invalid) > 0 or len(expected_missing) > 0
            assert result.success == (not has_errors), \
                f"Success status should be {not has_errors}, got {result.success}"


class TestFrameworkMappingValidatorUnit:
    """Unit tests for FrameworkMappingValidator edge cases."""
    
    def test_empty_templates_directory(self):
        """Test scanning when templates directory exists but is empty."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create empty templates/de and templates/en directories
            os.makedirs(os.path.join(tmpdir, "templates", "de"))
            os.makedirs(os.path.join(tmpdir, "templates", "en"))
            
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            
            assert frameworks == [], "Empty directories should return empty list"
    
    def test_missing_templates_directory(self):
        """Test scanning when templates directory doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Don't create templates directory
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            
            assert frameworks == [], "Missing templates directory should return empty list"
    
    def test_single_framework(self):
        """Test scanning with a single framework."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create single framework
            os.makedirs(os.path.join(tmpdir, "templates", "de", "test-framework"))
            os.makedirs(os.path.join(tmpdir, "templates", "en", "test-framework"))
            
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            
            assert len(frameworks) == 2, "Should find framework in both languages"
            assert all(f.name == "test-framework" for f in frameworks)
            assert {f.language for f in frameworks} == {'de', 'en'}
    
    def test_framework_with_correct_mapping_file(self):
        """Test framework with correctly named mapping file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            # Create correctly named mapping file
            mapping_file = os.path.join(framework_dir, "9999_Framework_Mapping.md")
            Path(mapping_file).touch()
            
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            
            assert len(frameworks) == 1
            assert frameworks[0].has_mapping_file is True
            assert frameworks[0].mapping_file_name == "9999_Framework_Mapping.md"
    
    def test_framework_with_incorrect_mapping_file(self):
        """Test framework with incorrectly named mapping file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            # Create incorrectly named mapping file
            mapping_file = os.path.join(framework_dir, "9999_Framework_Mapping.md")
            Path(mapping_file).touch()
            
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            
            assert len(frameworks) == 1
            assert frameworks[0].has_mapping_file is False
            assert frameworks[0].mapping_file_name == "9999_Framework_Mapping.md"
    
    def test_framework_without_mapping_file(self):
        """Test framework without any mapping file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            validator = FrameworkMappingValidator(tmpdir)
            frameworks = validator.scan_frameworks()
            
            assert len(frameworks) == 1
            assert frameworks[0].has_mapping_file is False
            assert frameworks[0].mapping_file_name is None
    
    def test_permission_error_handling(self):
        """Test handling of permission errors when scanning directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            # Create a file to make the directory non-empty
            test_file = os.path.join(framework_dir, "test.md")
            Path(test_file).touch()
            
            # Remove read permissions from the framework directory
            os.chmod(framework_dir, 0o000)
            
            try:
                validator = FrameworkMappingValidator(tmpdir)
                frameworks = validator.scan_frameworks()
                
                # Should handle permission error gracefully
                # The framework directory itself is discovered, but we can't read its contents
                assert isinstance(frameworks, list)
            finally:
                # Restore permissions for cleanup
                os.chmod(framework_dir, 0o755)
    
    def test_validate_method_integration(self):
        """Test the complete validate() method integration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create mix of valid and invalid frameworks
            valid_dir = os.path.join(tmpdir, "templates", "de", "valid-framework")
            os.makedirs(valid_dir)
            Path(os.path.join(valid_dir, "9999_Framework_Mapping.md")).touch()
            
            invalid_dir = os.path.join(tmpdir, "templates", "de", "invalid-framework")
            os.makedirs(invalid_dir)
            
            validator = FrameworkMappingValidator(tmpdir)
            result = validator.validate()
            
            assert result.total_frameworks == 2
            assert result.valid_frameworks == 1
            assert len(result.missing_files) == 1
            assert result.success is False
    
    def test_generate_report_with_error(self):
        """Test report generation when validation has an error."""
        result = ValidationResult(
            total_frameworks=0,
            valid_frameworks=0,
            invalid_frameworks=[],
            missing_files=[],
            success=False,
            error="Test error message"
        )
        
        validator = FrameworkMappingValidator()
        report = validator.generate_report(result)
        
        assert "ERROR: Test error message" in report
    
    def test_generate_report_success(self):
        """Test report generation when all validations pass."""
        result = ValidationResult(
            total_frameworks=2,
            valid_frameworks=2,
            invalid_frameworks=[],
            missing_files=[],
            success=True
        )
        
        validator = FrameworkMappingValidator()
        report = validator.generate_report(result)
        
        assert "PASS" in report
        assert "All frameworks have correctly named mapping files!" in report
