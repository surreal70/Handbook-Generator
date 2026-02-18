"""
Unit tests for framework validation system.

Tests validation of new compliance framework templates including:
- Template structure validation
- Required files validation
- Placeholder syntax validation
- Bilingual consistency validation

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2025, 2026
"""

import re
import pytest
from pathlib import Path
from src.template_validator import TemplateValidator, ValidationResult


class TestTemplateStructureValidation:
    """Test validation of template structure (Requirement 13.1, 13.2, 8.3, 8.4)."""
    
    def test_valid_filename_format(self, tmp_path):
        """Test that valid filename format passes validation."""
        # Create test framework directory
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create valid template files
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        (framework_dir / "0010_valid_template.md").write_text(
            "**Dokument-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        (framework_dir / "0020_another_template.md").write_text(
            "**Dokument-ID:** TEST-002\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert result.is_valid
        assert len(result.errors) == 0
    
    def test_invalid_filename_format(self, tmp_path):
        """Test that invalid filename format is detected."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        
        # Create invalid template files
        (framework_dir / "invalid_name.md").write_text("Content")
        (framework_dir / "10_short_number.md").write_text("Content")
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert not result.is_valid
        assert any("Invalid filename format" in error for error in result.errors)
    
    def test_unique_template_numbers(self, tmp_path):
        """Test that duplicate template numbers are detected."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        
        # Create templates with duplicate numbers
        (framework_dir / "0010_first_template.md").write_text(
            "**Dokument-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        (framework_dir / "0010_duplicate_template.md").write_text(
            "**Dokument-ID:** TEST-002\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert not result.is_valid
        assert any("Duplicate template number: 0010" in error for error in result.errors)
    
    def test_required_header_fields(self, tmp_path):
        """Test that missing header fields generate warnings."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        
        # Create template missing header fields
        (framework_dir / "0010_incomplete_template.md").write_text("# Template without headers")
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert len(result.warnings) > 0
        assert any("Missing header field" in warning for warning in result.warnings)


class TestRequiredFilesValidation:
    """Test validation of required files (Requirement 13.3, 13.4)."""
    
    def test_metadata_template_exists(self, tmp_path):
        """Test that metadata template existence is validated."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create template without metadata
        (framework_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert not result.is_valid
        assert any("Metadata template not found" in error for error in result.errors)
    
    def test_readme_exists(self, tmp_path):
        """Test that README.md existence is validated."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata but no README
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        (framework_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert any("README.md not found" in warning for warning in result.warnings)
    
    def test_framework_directory_not_found(self, tmp_path):
        """Test that missing framework directory is detected."""
        validator = TemplateValidator()
        result = validator.validate_framework("de", "nonexistent-framework", tmp_path / "templates")
        
        assert not result.is_valid
        assert any("Template directory not found" in error for error in result.errors)


class TestPlaceholderSyntaxValidation:
    """Test validation of placeholder syntax (Requirement 13.5, 11.5)."""
    
    def test_valid_placeholder_syntax(self, tmp_path):
        """Test that valid placeholder syntax passes validation."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        
        # Create template with valid placeholders
        (framework_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n"
            "**Owner:** {{ meta.owner }}\n"
            "**Version:** {{ meta.version }}\n"
            "**Status:** Draft\n"
            "Organization: {{ netbox.organization }}\n"
            "Nested: {{ source.nested.field }}"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert result.is_valid
        assert not any("Invalid placeholder syntax" in error for error in result.errors)
    
    def test_invalid_placeholder_syntax(self, tmp_path):
        """Test that invalid placeholder syntax is detected."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        
        # Create template with invalid placeholders
        (framework_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n"
            "**Owner:** Test\n"
            "**Version:** 1.0\n"
            "**Status:** Draft\n"
            "Invalid: {{ invalid }}\n"
            "Missing dot: {{nodot}}\n"
            "Special chars: {{ source.field! }}"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert not result.is_valid
        assert any("Invalid placeholder syntax" in error for error in result.errors)


class TestBilingualConsistencyValidation:
    """Test validation of bilingual consistency (Requirement 13.6, 9.3, 9.4, 9.5)."""
    
    def test_matching_filenames_across_languages(self, tmp_path):
        """Test that matching filenames are validated across languages."""
        # Create German templates
        de_dir = tmp_path / "templates" / "de" / "test-framework"
        de_dir.mkdir(parents=True)
        (de_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        (de_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        (de_dir / "0020_template.md").write_text(
            "**Dokument-ID:** TEST-002\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        
        # Create English templates with matching numbers
        en_dir = tmp_path / "templates" / "en" / "test-framework"
        en_dir.mkdir(parents=True)
        (en_dir / "0000_metadata_en_test-framework.md").write_text("# Metadata")
        (en_dir / "0010_template.md").write_text(
            "**Document-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        (en_dir / "0020_template.md").write_text(
            "**Document-ID:** TEST-002\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert result.is_valid
        assert not any("Missing" in warning and "translation" in warning for warning in result.warnings)
    
    def test_missing_translations_detected(self, tmp_path):
        """Test that missing translations are detected."""
        # Create German templates
        de_dir = tmp_path / "templates" / "de" / "test-framework"
        de_dir.mkdir(parents=True)
        (de_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        (de_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        (de_dir / "0020_template.md").write_text(
            "**Dokument-ID:** TEST-002\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        
        # Create English templates with missing translation
        en_dir = tmp_path / "templates" / "en" / "test-framework"
        en_dir.mkdir(parents=True)
        (en_dir / "0000_metadata_en_test-framework.md").write_text("# Metadata")
        (en_dir / "0010_template.md").write_text(
            "**Document-ID:** TEST-001\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
        )
        # Missing 0020 in English
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert any("Missing English translations" in warning for warning in result.warnings)
    
    def test_matching_markdown_structure(self, tmp_path):
        """Test that markdown structure is validated across languages."""
        # Create German template with specific structure
        de_dir = tmp_path / "templates" / "de" / "test-framework"
        de_dir.mkdir(parents=True)
        (de_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        (de_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n"
            "**Owner:** {{ meta.owner }}\n"
            "**Version:** 1.0\n"
            "**Status:** Draft\n"
            "# Abschnitt 1\n"
            "## Unterabschnitt 1.1\n"
            "# Abschnitt 2"
        )
        
        # Create English template with different structure
        en_dir = tmp_path / "templates" / "en" / "test-framework"
        en_dir.mkdir(parents=True)
        (en_dir / "0000_metadata_en_test-framework.md").write_text("# Metadata")
        (en_dir / "0010_template.md").write_text(
            "**Document-ID:** TEST-001\n"
            "**Owner:** {{ meta.owner }}\n"
            "**Version:** 1.0\n"
            "**Status:** Draft\n"
            "# Section 1\n"
            "# Section 2"
            # Missing subsection
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert any("Structure mismatch" in warning for warning in result.warnings)
    
    def test_matching_placeholder_positions(self, tmp_path):
        """Test that placeholder positions are validated across languages."""
        # Create German template
        de_dir = tmp_path / "templates" / "de" / "test-framework"
        de_dir.mkdir(parents=True)
        (de_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        (de_dir / "0010_template.md").write_text(
            "**Dokument-ID:** TEST-001\n"
            "**Owner:** {{ meta.owner }}\n"
            "**Version:** {{ meta.version }}\n"
            "**Status:** Draft"
        )
        
        # Create English template with different placeholders
        en_dir = tmp_path / "templates" / "en" / "test-framework"
        en_dir.mkdir(parents=True)
        (en_dir / "0000_metadata_en_test-framework.md").write_text("# Metadata")
        (en_dir / "0010_template.md").write_text(
            "**Document-ID:** TEST-001\n"
            "**Owner:** {{ meta.owner }}\n"
            "**Version:** 1.0\n"  # Hardcoded instead of placeholder
            "**Status:** Draft"
        )
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert any("Placeholder mismatch" in warning for warning in result.warnings)


class TestValidationReportGeneration:
    """Test validation report generation (Requirement 13.7)."""
    
    def test_validation_report_structure(self, tmp_path):
        """Test that validation report contains expected information."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        
        # Create template with issues
        (framework_dir / "0010_template.md").write_text("Content without headers")
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        # Check report structure
        assert isinstance(result, ValidationResult)
        assert hasattr(result, 'is_valid')
        assert hasattr(result, 'warnings')
        assert hasattr(result, 'errors')
        assert isinstance(result.warnings, list)
        assert isinstance(result.errors, list)
    
    def test_validation_report_with_errors_and_warnings(self, tmp_path):
        """Test that validation report captures both errors and warnings."""
        framework_dir = tmp_path / "templates" / "de" / "test-framework"
        framework_dir.mkdir(parents=True)
        
        # Create metadata
        (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
        
        # Create template with both errors and warnings
        (framework_dir / "invalid_name.md").write_text("Content")  # Error: invalid filename
        (framework_dir / "0010_template.md").write_text("Content")  # Warning: missing headers
        
        validator = TemplateValidator()
        result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
        
        assert not result.is_valid
        assert len(result.errors) > 0
        assert len(result.warnings) > 0



class TestFrameworkValidationProperties:
    """Property-based tests for framework validation system."""
    
    def test_property_1_template_naming_convention_compliance(self, tmp_path):
        """
        Property 1: Template Naming Convention Compliance
        
        For all templates in a framework:
        - Filename MUST match pattern NNNN_name.md where NNNN is 4 digits
        - Name part can contain alphanumeric, hyphens, underscores, and German umlauts
        
        **Validates: Requirements 8.1**
        """
        from hypothesis import given, strategies as st
        
        @given(
            template_number=st.integers(min_value=0, max_value=9999),
            template_name=st.text(
                alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd'), whitelist_characters='-_äöüÄÖÜß'),
                min_size=1,
                max_size=50
            ).filter(lambda x: x and not x.startswith('-') and not x.startswith('_'))
        )
        def property_test(template_number, template_name):
            framework_dir = tmp_path / "templates" / "de" / "test-framework"
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create metadata
            (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
            
            # Create template with generated name
            filename = f"{template_number:04d}_{template_name}.md"
            (framework_dir / filename).write_text(
                "**Dokument-ID:** TEST\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
            )
            
            validator = TemplateValidator()
            result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
            
            # Valid names should pass, invalid should fail
            if re.match(r'^\d{4}_[\w\-äöüÄÖÜß]+\.md$', filename):
                assert not any(f"Invalid filename format: {filename}" in error for error in result.errors)
            
            # Cleanup
            (framework_dir / filename).unlink(missing_ok=True)
        
        property_test()
    
    def test_property_2_template_number_uniqueness(self, tmp_path):
        """
        Property 2: Template Number Uniqueness
        
        For all templates in a framework:
        - Template numbers MUST be unique within the framework
        - Duplicate numbers MUST be reported as errors
        
        **Validates: Requirements 13.2**
        """
        from hypothesis import given, strategies as st
        
        @given(
            numbers=st.lists(st.integers(min_value=10, max_value=9999), min_size=2, max_size=10)
        )
        def property_test(numbers):
            framework_dir = tmp_path / "templates" / "de" / "test-framework"
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create metadata
            (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
            
            # Create templates with given numbers
            for i, number in enumerate(numbers):
                filename = f"{number:04d}_template_{i}.md"
                (framework_dir / filename).write_text(
                    "**Dokument-ID:** TEST\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
                )
            
            validator = TemplateValidator()
            result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
            
            # Check if duplicates are detected
            unique_numbers = len(set(numbers))
            total_numbers = len(numbers)
            has_duplicates = unique_numbers < total_numbers
            
            if has_duplicates:
                assert not result.is_valid
                assert any("Duplicate template number" in error for error in result.errors)
            else:
                # No duplicate errors should be present
                assert not any("Duplicate template number" in error for error in result.errors)
            
            # Cleanup
            for i, number in enumerate(numbers):
                filename = f"{number:04d}_template_{i}.md"
                (framework_dir / filename).unlink(missing_ok=True)
        
        property_test()
    
    def test_property_8_placeholder_syntax_validity(self, tmp_path):
        """
        Property 8: Placeholder Syntax Validity
        
        For all placeholders in templates:
        - MUST follow format {{ source.field }}
        - Source and field MUST be alphanumeric with underscores
        - Field can contain dots for nested paths
        
        **Validates: Requirements 8.5**
        """
        from hypothesis import given, strategies as st
        
        # Build better strategies
        source_strategy = st.text(
            alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_',
            min_size=1,
            max_size=20
        )
        
        field_part_strategy = st.text(
            alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_',
            min_size=1,
            max_size=15
        )
        
        # Generate field with at least one dot
        field_strategy = st.builds(
            lambda parts: '.'.join(parts),
            st.lists(field_part_strategy, min_size=2, max_size=3)
        )
        
        @given(
            source=source_strategy,
            field=field_strategy
        )
        def property_test(source, field):
            framework_dir = tmp_path / "templates" / "de" / "test-framework"
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create metadata
            (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
            
            # Create template with placeholder
            placeholder = f"{{{{ {source}.{field} }}}}"
            (framework_dir / "0010_template.md").write_text(
                f"**Dokument-ID:** TEST\n**Owner:** {placeholder}\n**Version:** 1.0\n**Status:** Draft"
            )
            
            validator = TemplateValidator()
            result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
            
            # Check if placeholder is valid
            is_valid_placeholder = re.match(r'^\{\{\s*[a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+\s*\}\}$', placeholder)
            
            if is_valid_placeholder:
                assert not any("Invalid placeholder syntax" in error for error in result.errors)
            
            # Cleanup
            (framework_dir / "0010_template.md").unlink(missing_ok=True)
        
        property_test()
    
    def test_property_10_bilingual_filename_consistency(self, tmp_path):
        """
        Property 10: Bilingual Filename Consistency
        
        For all bilingual frameworks:
        - Template numbers MUST match across German and English versions
        - Missing translations MUST be reported as warnings
        
        **Validates: Requirements 9.3**
        """
        from hypothesis import given, strategies as st
        
        @given(
            de_numbers=st.lists(st.integers(min_value=10, max_value=100), min_size=1, max_size=5, unique=True),
            en_numbers=st.lists(st.integers(min_value=10, max_value=100), min_size=1, max_size=5, unique=True)
        )
        def property_test(de_numbers, en_numbers):
            # Create German templates
            de_dir = tmp_path / "templates" / "de" / "test-framework"
            de_dir.mkdir(parents=True, exist_ok=True)
            (de_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
            
            for number in de_numbers:
                (de_dir / f"{number:04d}_template.md").write_text(
                    "**Dokument-ID:** TEST\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
                )
            
            # Create English templates
            en_dir = tmp_path / "templates" / "en" / "test-framework"
            en_dir.mkdir(parents=True, exist_ok=True)
            (en_dir / "0000_metadata_en_test-framework.md").write_text("# Metadata")
            
            for number in en_numbers:
                (en_dir / f"{number:04d}_template.md").write_text(
                    "**Document-ID:** TEST\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
                )
            
            validator = TemplateValidator()
            result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
            
            # Check for missing translations
            de_set = set(de_numbers)
            en_set = set(en_numbers)
            missing_en = de_set - en_set
            missing_de = en_set - de_set
            
            if missing_en:
                assert any("Missing English translations" in warning for warning in result.warnings)
            if missing_de:
                assert any("Missing German translations" in warning for warning in result.warnings)
            
            # Cleanup
            for number in de_numbers:
                (de_dir / f"{number:04d}_template.md").unlink(missing_ok=True)
            for number in en_numbers:
                (en_dir / f"{number:04d}_template.md").unlink(missing_ok=True)
        
        property_test()
    
    def test_property_29_validation_idempotence(self, tmp_path):
        """
        Property 29: Validation Idempotence
        
        For any framework:
        - Running validation multiple times MUST produce identical results
        - Validation MUST NOT modify the templates
        - Validation MUST be deterministic
        
        **Validates: Requirements 13.1-13.7**
        """
        from hypothesis import given, strategies as st
        
        @given(
            num_templates=st.integers(min_value=1, max_value=5),
            num_runs=st.integers(min_value=2, max_value=5)
        )
        def property_test(num_templates, num_runs):
            framework_dir = tmp_path / "templates" / "de" / "test-framework"
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create metadata
            (framework_dir / "0000_metadata_de_test-framework.md").write_text("# Metadata")
            
            # Create templates
            for i in range(num_templates):
                number = (i + 1) * 10
                (framework_dir / f"{number:04d}_template.md").write_text(
                    f"**Dokument-ID:** TEST-{i}\n**Owner:** Test\n**Version:** 1.0\n**Status:** Draft"
                )
            
            validator = TemplateValidator()
            
            # Run validation multiple times
            results = []
            for _ in range(num_runs):
                result = validator.validate_framework("de", "test-framework", tmp_path / "templates")
                results.append({
                    'is_valid': result.is_valid,
                    'num_errors': len(result.errors),
                    'num_warnings': len(result.warnings),
                    'errors': sorted(result.errors),
                    'warnings': sorted(result.warnings)
                })
            
            # All results should be identical
            first_result = results[0]
            for result in results[1:]:
                assert result['is_valid'] == first_result['is_valid']
                assert result['num_errors'] == first_result['num_errors']
                assert result['num_warnings'] == first_result['num_warnings']
                assert result['errors'] == first_result['errors']
                assert result['warnings'] == first_result['warnings']
            
            # Cleanup
            for i in range(num_templates):
                number = (i + 1) * 10
                (framework_dir / f"{number:04d}_template.md").unlink(missing_ok=True)
        
        property_test()
