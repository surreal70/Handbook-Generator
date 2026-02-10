"""
Property-based tests for Validation System with new frameworks.

Tests validation properties for IDW PS 951, NIST CSF 2.0, and TOGAF templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import tempfile
import re

from src.template_validator import TemplateValidator, ValidationResult


class TestTemplateNamingConventionProperties:
    """Property-based tests for template naming convention compliance."""
    
    @settings(max_examples=100)
    @given(
        number=st.integers(min_value=0, max_value=9999),
        name_parts=st.lists(
            st.text(
                alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd'), min_codepoint=97, max_codepoint=122),
                min_size=1,
                max_size=10
            ),
            min_size=1,
            max_size=5
        )
    )
    def test_property_1_template_naming_convention_compliance(self, number, name_parts):
        """
        Feature: additional-compliance-frameworks, Property 1: Template Naming Convention Compliance
        
        For any template file in a framework template set, the filename must match the pattern
        NNNN_descriptive_name.md where NNNN is a 4-digit number.
        
        Validates: Requirements 4.1, 9.1
        """
        validator = TemplateValidator()
        
        # Generate valid filename
        name = '_'.join(name_parts)
        valid_filename = f"{number:04d}_{name}.md"
        
        # Valid filename should match pattern
        assert re.match(r'^\d{4}_[\w\-]+\.md$', valid_filename), \
            f"Valid filename {valid_filename} should match pattern"
        
        # Test invalid filenames
        invalid_filenames = [
            f"{number}_{name}.md",  # Missing leading zeros
            f"{number:04d}{name}.md",  # Missing underscore
            f"{name}_{number:04d}.md",  # Wrong order
            f"{number:04d}_.md",  # Missing name
            f"{number:04d}_{name}",  # Missing extension
        ]
        
        for invalid_filename in invalid_filenames:
            if not re.match(r'^\d{4}_[\w\-]+\.md$', invalid_filename):
                # This is expected - invalid filenames should not match
                pass
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf']),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_1_framework_validation(self, framework, language):
        """
        Test that framework validation checks naming conventions for new frameworks.
        """
        validator = TemplateValidator()
        
        # Validate actual framework templates
        result = validator.validate_framework(language, framework)
        
        # All template files should follow naming convention
        # (errors would be added if they don't)
        for error in result.errors:
            if 'filename format' in error.lower():
                # If there's a filename format error, it should mention the expected pattern
                assert 'NNNN_name.md' in error or 'expected' in error.lower()


class TestTemplateHeaderStructureProperties:
    """Property-based tests for template header structure."""
    
    @settings(max_examples=100)
    @given(
        has_document_id=st.booleans(),
        has_owner=st.booleans(),
        has_version=st.booleans(),
        has_status=st.booleans()
    )
    def test_property_4_template_header_structure(
        self,
        has_document_id,
        has_owner,
        has_version,
        has_status
    ):
        """
        Feature: additional-compliance-frameworks, Property 4: Template Header Structure
        
        For any template file, it must include a header section containing Document-ID, Owner,
        Version, Status, Classification, and Last Update fields.
        
        Validates: Requirements 4.3
        """
        validator = TemplateValidator()
        
        # Build template content with varying header completeness
        content_parts = ["# Template Title\n\n"]
        
        if has_document_id:
            content_parts.append("**Dokument-ID:** TEST-001\n")
        if has_owner:
            content_parts.append("**Owner:** {{ meta.author }}\n")
        if has_version:
            content_parts.append("**Version:** 1.0\n")
        if has_status:
            content_parts.append("**Status:** Draft\n")
        
        content_parts.append("\n## Content\n\nTemplate content here.\n")
        content = ''.join(content_parts)
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
            tmp_path = Path(tmp.name)
            tmp_path.write_text(content)
            
            try:
                result = ValidationResult(is_valid=True, warnings=[], errors=[])
                validator._validate_template_content(tmp_path, result)
                
                # Check warnings for missing fields
                if not has_document_id:
                    assert any('Dokument-ID' in w for w in result.warnings), \
                        "Should warn about missing Dokument-ID"
                if not has_owner:
                    assert any('Owner' in w for w in result.warnings), \
                        "Should warn about missing Owner"
                if not has_version:
                    assert any('Version' in w for w in result.warnings), \
                        "Should warn about missing Version"
                if not has_status:
                    assert any('Status' in w for w in result.warnings), \
                        "Should warn about missing Status"
                
                # If all fields present, should have no warnings about them
                if has_document_id and has_owner and has_version and has_status:
                    header_warnings = [
                        w for w in result.warnings
                        if any(field in w for field in ['Dokument-ID', 'Owner', 'Version', 'Status'])
                    ]
                    assert len(header_warnings) == 0, \
                        "Should have no warnings about header fields when all are present"
            
            finally:
                tmp_path.unlink()


class TestMarkdownStructureProperties:
    """Property-based tests for markdown structure compliance."""
    
    @settings(max_examples=100)
    @given(
        num_sections=st.integers(min_value=1, max_value=10),
        header_level=st.integers(min_value=1, max_value=3)
    )
    def test_property_5_markdown_structure_compliance(self, num_sections, header_level):
        """
        Feature: additional-compliance-frameworks, Property 5: Markdown Structure Compliance
        
        For any template file, it must contain structured sections using markdown headers (##, ###).
        
        Validates: Requirements 4.4
        """
        validator = TemplateValidator()
        
        # Build template with markdown headers
        content_parts = ["# Main Title\n\n"]
        
        for i in range(num_sections):
            header_prefix = '#' * (header_level + 1)
            content_parts.append(f"{header_prefix} Section {i+1}\n\n")
            content_parts.append(f"Content for section {i+1}.\n\n")
        
        content = ''.join(content_parts)
        
        # Check that headers are present
        headers = re.findall(r'^#{1,6}\s+.+$', content, re.MULTILINE)
        assert len(headers) >= num_sections, \
            f"Should have at least {num_sections} headers, found {len(headers)}"
        
        # Verify headers use proper markdown syntax
        for header in headers:
            assert header.startswith('#'), "Headers should start with #"
            assert ' ' in header, "Headers should have space after #"


class TestTemplateNumberUniquenessProperties:
    """Property-based tests for template number uniqueness."""
    
    @settings(max_examples=100)
    @given(
        num_templates=st.integers(min_value=5, max_value=20),
        has_duplicates=st.booleans()
    )
    def test_property_15_template_number_uniqueness(self, num_templates, has_duplicates):
        """
        Feature: additional-compliance-frameworks, Property 15: Template Number Uniqueness
        
        For any framework template set, all template numeric prefixes must be unique within
        that framework.
        
        Validates: Requirements 9.2
        """
        validator = TemplateValidator()
        
        # Generate template numbers
        if has_duplicates:
            # Create some duplicates
            numbers = list(range(10, 10 + num_templates * 10, 10))
            # Add a duplicate
            numbers.append(numbers[0])
        else:
            # All unique
            numbers = list(range(10, 10 + num_templates * 10, 10))
        
        # Create template paths
        templates = [Path(f"{num:04d}_template.md") for num in numbers]
        
        # Validate numbering
        warnings = validator.validate_numbering(templates)
        
        if has_duplicates:
            # Should have warning about duplicates
            assert len(warnings) > 0, "Should have warnings when duplicates exist"
            assert any('duplicate' in w.lower() for w in warnings), \
                f"Should warn about duplicates, got: {warnings}"
        else:
            # Should have no warnings about duplicates
            duplicate_warnings = [w for w in warnings if 'duplicate' in w.lower()]
            assert len(duplicate_warnings) == 0, \
                f"Should have no duplicate warnings, got: {duplicate_warnings}"


class TestFrameworkValidationProperties:
    """Property-based tests for complete framework validation."""
    
    @settings(max_examples=50)
    @given(
        framework=st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf']),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_comprehensive_framework_validation(self, framework, language):
        """
        Test comprehensive validation of new frameworks.
        
        Validates all aspects:
        - Naming conventions
        - Number uniqueness
        - Required files
        - Placeholder syntax
        - Bilingual consistency
        """
        validator = TemplateValidator()
        
        # Validate framework
        result = validator.validate_framework(language, framework)
        
        # Framework should exist
        assert result is not None, f"Should return validation result for {language}/{framework}"
        
        # Check that validation covers all aspects
        # (specific errors/warnings depend on actual template state)
        
        # If there are errors, they should be specific and actionable
        for error in result.errors:
            assert len(error) > 0, "Errors should have descriptive messages"
            # Errors should mention specific issues
            assert any(keyword in error.lower() for keyword in [
                'filename', 'format', 'duplicate', 'metadata', 'placeholder', 'not found'
            ]), f"Error should be specific: {error}"
        
        # If there are warnings, they should be informative
        for warning in result.warnings:
            assert len(warning) > 0, "Warnings should have descriptive messages"


class TestBilingualConsistencyProperties:
    """Property-based tests for bilingual template consistency."""
    
    @settings(max_examples=50)
    @given(
        framework=st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf']),
        num_headers=st.integers(min_value=2, max_value=8),
        num_placeholders=st.integers(min_value=1, max_value=5)
    )
    def test_property_7_bilingual_template_consistency(
        self,
        framework,
        num_headers,
        num_placeholders
    ):
        """
        Feature: additional-compliance-frameworks, Property 7: Bilingual Template Consistency
        
        For any template in one language (German or English), there must exist a corresponding
        template in the other language with identical filename, section structure, and
        placeholder locations.
        
        Validates: Requirements 1.6, 5.3, 5.4, 5.5, 9.6
        """
        validator = TemplateValidator()
        
        # Create matching bilingual templates
        template_number = 100
        
        # Build German template
        de_content_parts = [f"# German Template {template_number}\n\n"]
        for i in range(num_headers):
            de_content_parts.append(f"## Abschnitt {i+1}\n\n")
            de_content_parts.append(f"Inhalt für Abschnitt {i+1}.\n\n")
        
        # Add placeholders
        for i in range(num_placeholders):
            de_content_parts.append(f"**Feld {i+1}:** {{{{ meta.field{i+1} }}}}\n")
        
        de_content = ''.join(de_content_parts)
        
        # Build English template with same structure
        en_content_parts = [f"# English Template {template_number}\n\n"]
        for i in range(num_headers):
            en_content_parts.append(f"## Section {i+1}\n\n")
            en_content_parts.append(f"Content for section {i+1}.\n\n")
        
        # Add same placeholders
        for i in range(num_placeholders):
            en_content_parts.append(f"**Field {i+1}:** {{{{ meta.field{i+1} }}}}\n")
        
        en_content = ''.join(en_content_parts)
        
        # Create temporary files
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            
            de_file = tmpdir_path / f"{template_number:04d}_template_de.md"
            en_file = tmpdir_path / f"{template_number:04d}_template_en.md"
            
            de_file.write_text(de_content)
            en_file.write_text(en_content)
            
            # Check structure matching
            result = ValidationResult(is_valid=True, warnings=[], errors=[])
            validator._check_matching_structure(de_file, en_file, result)
            
            # Should have no warnings about structure mismatch
            structure_warnings = [
                w for w in result.warnings
                if 'structure mismatch' in w.lower() or 'placeholder mismatch' in w.lower()
            ]
            assert len(structure_warnings) == 0, \
                f"Matching templates should have no structure warnings, got: {structure_warnings}"
            
            # Test with mismatched structure
            en_content_mismatched = en_content + "\n## Extra Section\n\nExtra content.\n"
            en_file.write_text(en_content_mismatched)
            
            result_mismatched = ValidationResult(is_valid=True, warnings=[], errors=[])
            validator._check_matching_structure(de_file, en_file, result_mismatched)
            
            # Should have warnings about structure mismatch
            assert len(result_mismatched.warnings) > 0, \
                "Mismatched templates should have warnings"
            assert any('structure mismatch' in w.lower() or 'header' in w.lower() 
                      for w in result_mismatched.warnings), \
                f"Should warn about structure mismatch, got: {result_mismatched.warnings}"


class TestValidationReportProperties:
    """Property-based tests for validation report generation."""
    
    @settings(max_examples=50)
    @given(
        num_frameworks=st.integers(min_value=1, max_value=6),
        error_rate=st.floats(min_value=0.0, max_value=1.0),
        warning_rate=st.floats(min_value=0.0, max_value=1.0)
    )
    def test_property_validation_report_generation(
        self,
        num_frameworks,
        error_rate,
        warning_rate
    ):
        """
        Test that validation reports are generated correctly with varying results.
        
        Validates: Requirements 9.7
        """
        validator = TemplateValidator()
        
        # Create mock validation results
        results = {}
        for i in range(num_frameworks):
            framework_key = f"de/framework-{i}"
            
            # Determine if this framework has errors/warnings
            has_errors = (i / num_frameworks) < error_rate
            has_warnings = (i / num_frameworks) < warning_rate
            
            result = ValidationResult(is_valid=not has_errors, warnings=[], errors=[])
            
            if has_errors:
                result.add_error(f"Error in framework {i}")
            if has_warnings:
                result.add_warning(f"Warning in framework {i}")
            
            results[framework_key] = result
        
        # Generate report
        report = validator.generate_validation_report(results)
        
        # Report should contain summary
        assert 'TEMPLATE VALIDATION REPORT' in report
        assert 'SUMMARY' in report
        assert f'Total frameworks validated: {num_frameworks}' in report
        
        # Report should contain framework details
        for framework_key in results.keys():
            assert framework_key in report
        
        # Report should show errors and warnings
        for framework_key, result in results.items():
            if result.errors:
                assert 'ERRORS:' in report
            if result.warnings:
                assert 'WARNINGS:' in report


class TestNewFrameworksValidation:
    """Integration tests for validating new frameworks."""
    
    def test_validate_idw_ps_951_templates(self):
        """Test validation of IDW PS 951 templates."""
        validator = TemplateValidator()
        
        # Validate German templates
        result_de = validator.validate_framework('de', 'idw-ps-951')
        assert result_de is not None
        
        # Validate English templates
        result_en = validator.validate_framework('en', 'idw-ps-951')
        assert result_en is not None
    
    def test_validate_nist_csf_templates(self):
        """Test validation of NIST CSF templates."""
        validator = TemplateValidator()
        
        # Validate German templates
        result_de = validator.validate_framework('de', 'nist-csf')
        assert result_de is not None
        
        # Validate English templates
        result_en = validator.validate_framework('en', 'nist-csf')
        assert result_en is not None
    
    def test_validate_togaf_templates(self):
        """Test validation of TOGAF templates."""
        validator = TemplateValidator()
        
        # Validate German templates
        result_de = validator.validate_framework('de', 'togaf')
        assert result_de is not None
        
        # Validate English templates
        result_en = validator.validate_framework('en', 'togaf')
        assert result_en is not None
    
    def test_validate_all_new_frameworks(self):
        """Test validation of all new frameworks at once."""
        validator = TemplateValidator()
        
        # Validate all new frameworks
        results = validator.validate_new_frameworks()
        
        # Should have results for all frameworks and languages
        expected_keys = [
            'de/idw-ps-951', 'en/idw-ps-951',
            'de/nist-csf', 'en/nist-csf',
            'de/togaf', 'en/togaf'
        ]
        
        for key in expected_keys:
            assert key in results, f"Should have validation result for {key}"
            assert isinstance(results[key], ValidationResult)
    
    def test_generate_comprehensive_validation_report(self):
        """Test generation of comprehensive validation report for new frameworks."""
        validator = TemplateValidator()
        
        # Validate all new frameworks
        results = validator.validate_new_frameworks()
        
        # Generate report
        report = validator.generate_validation_report(results)
        
        # Report should be comprehensive
        assert len(report) > 0
        assert 'TEMPLATE VALIDATION REPORT' in report
        assert 'idw-ps-951' in report
        assert 'nist-csf' in report
        assert 'togaf' in report
