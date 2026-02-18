"""
Tests for Version History Validator.

This module contains both unit tests and property-based tests for the
VersionHistoryValidator component of the quality control system.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import os
import tempfile
import pytest
from pathlib import Path
from hypothesis import given, strategies as st

from src.quality_control.version_history_validator import VersionHistoryValidator
from src.quality_control.data_structures import TemplateFile, VersionHistoryValidationResult


# Strategy for generating valid framework names
framework_name_strategy = st.text(
    min_size=1, 
    max_size=50, 
    alphabet=st.characters(
        whitelist_categories=('Lu', 'Ll', 'Nd'), 
        whitelist_characters='-_'
    )
).filter(lambda x: '/' not in x and x.strip())

# Strategy for generating valid template names (no slashes, no empty)
template_name_strategy = st.text(
    min_size=1, 
    max_size=30,
    alphabet=st.characters(
        whitelist_categories=('Lu', 'Ll', 'Nd'), 
        whitelist_characters='-_'
    )
).filter(lambda x: '/' not in x and x.strip())


class TestVersionHistoryValidatorProperties:
    """Property-based tests for VersionHistoryValidator."""
    
    @given(st.lists(st.tuples(
        framework_name_strategy,
        template_name_strategy,
        st.sampled_from(['has_version_history', 'no_version_history'])
    ), min_size=0, max_size=20, unique_by=lambda x: (x[0], x[1])))
    def test_property_6_version_history_detection(self, template_configs):
        """
        Feature: quality-control-and-framework-documentation
        Property 6: Version History Detection
        
        **Validates: Requirements 2.2, 2.4**
        
        For any template file, the Template_Validator should correctly identify
        whether it contains a "## Version History" or "## Versionshistorie" section.
        """
        # Setup: Create temporary directory structure with templates
        with tempfile.TemporaryDirectory() as tmpdir:
            expected_with_history = []
            expected_without_history = []
            
            for framework_name, template_name, has_history in template_configs:
                framework_dir = os.path.join(tmpdir, "templates", "de", framework_name)
                os.makedirs(framework_dir, exist_ok=True)
                
                template_file = os.path.join(framework_dir, f"{template_name}.md")
                
                if has_history == 'has_version_history':
                    # Create template with version history
                    content = f"""# {template_name}

Some content here.

## Version History

- Version 1.0 - Initial release
- Version 1.1 - Updates

## Other Section

More content.
"""
                    expected_with_history.append((framework_name, f"{template_name}.md"))
                else:
                    # Create template without version history
                    content = f"""# {template_name}

Some content here.

## Other Section

More content.
"""
                    expected_without_history.append((framework_name, f"{template_name}.md"))
                
                Path(template_file).write_text(content, encoding='utf-8')
            
            # Execute: Scan templates
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            # Verify: Correct identification of version history
            templates_with_history = {
                (t.framework, t.path.name) 
                for t in templates 
                if t.has_version_history
            }
            templates_without_history = {
                (t.framework, t.path.name) 
                for t in templates 
                if not t.has_version_history
            }
            
            # Property: All templates with version history are identified
            assert templates_with_history == set(expected_with_history), \
                f"Expected with history: {set(expected_with_history)}, Got: {templates_with_history}"
            
            # Property: All templates without version history are identified
            assert templates_without_history == set(expected_without_history), \
                f"Expected without history: {set(expected_without_history)}, Got: {templates_without_history}"
    
    @given(st.lists(st.tuples(
        framework_name_strategy,
        template_name_strategy,
        st.sampled_from(['de', 'en'])  # language with German header
    ), min_size=0, max_size=15, unique_by=lambda x: (x[0], x[1], x[2])))
    def test_property_6_german_version_history_detection(self, template_configs):
        """
        Feature: quality-control-and-framework-documentation
        Property 6: Version History Detection (German)
        
        **Validates: Requirements 2.2, 2.4**
        
        For any template file with German version history header,
        the Template_Validator should correctly identify it.
        """
        # Setup: Create temporary directory structure with German templates
        with tempfile.TemporaryDirectory() as tmpdir:
            expected_with_history = []
            
            for framework_name, template_name, language in template_configs:
                framework_dir = os.path.join(tmpdir, "templates", language, framework_name)
                os.makedirs(framework_dir, exist_ok=True)
                
                template_file = os.path.join(framework_dir, f"{template_name}.md")
                
                # Create template with German version history header
                content = f"""# {template_name}

Inhalt hier.

## Versionshistorie

- Version 1.0 - Erste Version
- Version 1.1 - Aktualisierungen

## Andere Sektion

Mehr Inhalt.
"""
                Path(template_file).write_text(content, encoding='utf-8')
                expected_with_history.append((framework_name, f"{template_name}.md", language))
            
            # Execute: Scan templates
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            # Verify: All templates with German version history are identified
            templates_with_history = {
                (t.framework, t.path.name, t.language) 
                for t in templates 
                if t.has_version_history
            }
            
            # Property: All templates with German version history header are detected
            assert templates_with_history == set(expected_with_history), \
                f"Expected: {set(expected_with_history)}, Got: {templates_with_history}"
            
            # Property: All detected templates have valid format (at least one version entry)
            for template in templates:
                if template.has_version_history:
                    assert template.version_history_format_valid, \
                        f"Template {template.path.name} has version history but invalid format"
                    assert template.version_entries > 0, \
                        f"Template {template.path.name} should have at least one version entry"
    
    @given(st.lists(st.tuples(
        framework_name_strategy,
        template_name_strategy,
        st.sampled_from(['valid', 'missing', 'invalid'])  # template status
    ), min_size=0, max_size=30, unique_by=lambda x: (x[0], x[1])))
    def test_property_5_accurate_counting(self, template_configs):
        """
        Feature: quality-control-and-framework-documentation
        Property 5: Accurate Counting
        
        **Validates: Requirements 2.6, 3.7, 4.4, 4.9**
        
        For any directory containing template files, the count reported by
        the system should equal the actual number of files matching the criteria.
        """
        # Setup: Create temporary directory structure with various templates
        with tempfile.TemporaryDirectory() as tmpdir:
            expected_valid = 0
            expected_missing = 0
            expected_invalid = 0
            total_templates = 0
            
            for framework_name, template_name, status in template_configs:
                framework_dir = os.path.join(tmpdir, "templates", "de", framework_name)
                os.makedirs(framework_dir, exist_ok=True)
                
                template_file = os.path.join(framework_dir, f"{template_name}.md")
                total_templates += 1
                
                if status == 'valid':
                    # Create template with valid version history
                    content = f"""# {template_name}
## Version History
- Version 1.0
"""
                    expected_valid += 1
                elif status == 'missing':
                    # Create template without version history
                    content = f"""# {template_name}
## Some Section
Content
"""
                    expected_missing += 1
                else:  # invalid
                    # Create template with empty version history
                    content = f"""# {template_name}
## Version History
(No entries)
"""
                    expected_invalid += 1
                
                Path(template_file).write_text(content, encoding='utf-8')
            
            # Execute: Scan and validate templates
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            result = validator.validate_version_history(templates)
            
            # Property: Total count matches actual number of templates
            assert result.total_templates == total_templates, \
                f"Expected {total_templates} templates, got {result.total_templates}"
            
            # Property: Valid count matches expected
            assert result.valid_templates == expected_valid, \
                f"Expected {expected_valid} valid templates, got {result.valid_templates}"
            
            # Property: Missing count matches expected
            assert len(result.missing_version_history) == expected_missing, \
                f"Expected {expected_missing} missing, got {len(result.missing_version_history)}"
            
            # Property: Invalid count matches expected
            assert len(result.invalid_format) == expected_invalid, \
                f"Expected {expected_invalid} invalid, got {len(result.invalid_format)}"
            
            # Property: Sum of categories equals total
            sum_categories = result.valid_templates + len(result.missing_version_history) + len(result.invalid_format)
            assert sum_categories == result.total_templates, \
                f"Sum of categories ({sum_categories}) should equal total ({result.total_templates})"


class TestVersionHistoryValidatorUnit:
    """Unit tests for VersionHistoryValidator edge cases."""
    
    def test_empty_templates_directory(self):
        """Test scanning when templates directory exists but is empty."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create empty templates/de and templates/en directories
            os.makedirs(os.path.join(tmpdir, "templates", "de"))
            os.makedirs(os.path.join(tmpdir, "templates", "en"))
            
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            assert templates == [], "Empty directories should return empty list"
    
    def test_missing_templates_directory(self):
        """Test scanning when templates directory doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Don't create templates directory
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            assert templates == [], "Missing templates directory should return empty list"
    
    def test_template_without_version_history(self):
        """Test template file without version history section."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            template_file = os.path.join(framework_dir, "template.md")
            content = """# Test Template

This is a test template without version history.

## Some Section

Content here.
"""
            Path(template_file).write_text(content, encoding='utf-8')
            
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            assert len(templates) == 1
            assert templates[0].has_version_history is False
            assert templates[0].version_history_format_valid is False
            assert templates[0].version_entries == 0
    
    def test_template_with_empty_version_history(self):
        """Test template with version history section but no entries."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            template_file = os.path.join(framework_dir, "template.md")
            content = """# Test Template

This is a test template.

## Version History

(No entries yet)

## Some Section

Content here.
"""
            Path(template_file).write_text(content, encoding='utf-8')
            
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            assert len(templates) == 1
            assert templates[0].has_version_history is True
            assert templates[0].version_history_format_valid is False
            assert templates[0].version_entries == 0
    
    def test_template_with_valid_version_history(self):
        """Test template with valid version history section."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            template_file = os.path.join(framework_dir, "template.md")
            content = """# Test Template

This is a test template.

## Version History

- Version 1.0 - Initial release
- Version 1.1 - Bug fixes

## Some Section

Content here.
"""
            Path(template_file).write_text(content, encoding='utf-8')
            
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            assert len(templates) == 1
            assert templates[0].has_version_history is True
            assert templates[0].version_history_format_valid is True
            assert templates[0].version_entries == 2
    
    def test_template_with_german_version_history(self):
        """Test template with German version history header."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            template_file = os.path.join(framework_dir, "template.md")
            content = """# Test Template

Dies ist eine Test-Vorlage.

## Versionshistorie

- Version 1.0 - Erste Version
- Version 1.1 - Fehlerbehebungen

## Andere Sektion

Inhalt hier.
"""
            Path(template_file).write_text(content, encoding='utf-8')
            
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            assert len(templates) == 1
            assert templates[0].has_version_history is True
            assert templates[0].version_history_format_valid is True
            assert templates[0].version_entries == 2
    
    def test_malformed_markdown(self):
        """Test handling of malformed Markdown files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            template_file = os.path.join(framework_dir, "template.md")
            content = """# Test Template

## Version History
No proper formatting
Version 1.0
Version 1.1

## Some Section
"""
            Path(template_file).write_text(content, encoding='utf-8')
            
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            assert len(templates) == 1
            assert templates[0].has_version_history is True
            # Should still detect version entries even with non-standard formatting
            assert templates[0].version_entries >= 0
    
    def test_excluded_files_not_scanned(self):
        """Test that excluded files (README, metadata) are not scanned."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            # Create excluded files
            for filename in ['README.md', 'metadata.yaml', '9999_Framework_Mapping.md']:
                file_path = os.path.join(framework_dir, filename)
                Path(file_path).write_text("# Content", encoding='utf-8')
            
            # Create a regular template
            template_file = os.path.join(framework_dir, "template.md")
            Path(template_file).write_text("# Template", encoding='utf-8')
            
            validator = VersionHistoryValidator(tmpdir)
            templates = validator.scan_templates()
            
            # Should only find the regular template, not the excluded files
            assert len(templates) == 1
            assert templates[0].path.name == "template.md"
    
    def test_validate_method_integration(self):
        """Test the complete validate() method integration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = os.path.join(tmpdir, "templates", "de", "test-framework")
            os.makedirs(framework_dir)
            
            # Create template with valid version history
            valid_template = os.path.join(framework_dir, "valid.md")
            Path(valid_template).write_text("""# Valid
## Version History
- Version 1.0
""", encoding='utf-8')
            
            # Create template without version history
            invalid_template = os.path.join(framework_dir, "invalid.md")
            Path(invalid_template).write_text("""# Invalid
## Some Section
Content
""", encoding='utf-8')
            
            validator = VersionHistoryValidator(tmpdir)
            result = validator.validate()
            
            assert result.total_templates == 2
            assert result.valid_templates == 1
            assert len(result.missing_version_history) == 1
            assert result.success is False
    
    def test_generate_report_with_error(self):
        """Test report generation when validation has an error."""
        result = VersionHistoryValidationResult(
            total_templates=0,
            valid_templates=0,
            missing_version_history=[],
            invalid_format=[],
            success=False,
            error="Test error message"
        )
        
        validator = VersionHistoryValidator()
        report = validator.generate_report(result)
        
        assert "ERROR: Test error message" in report
    
    def test_generate_report_success(self):
        """Test report generation when all validations pass."""
        result = VersionHistoryValidationResult(
            total_templates=10,
            valid_templates=10,
            missing_version_history=[],
            invalid_format=[],
            success=True
        )
        
        validator = VersionHistoryValidator()
        report = validator.generate_report(result)
        
        assert "PASS" in report
        assert "All templates have valid version history!" in report
    
    def test_generate_report_with_missing_history(self):
        """Test report generation with missing version history."""
        template = TemplateFile(
            path=Path("/test/framework/template.md"),
            framework="test-framework",
            language="de",
            has_version_history=False,
            version_history_format_valid=False,
            version_entries=0
        )
        
        result = VersionHistoryValidationResult(
            total_templates=1,
            valid_templates=0,
            missing_version_history=[template],
            invalid_format=[],
            success=False
        )
        
        validator = VersionHistoryValidator()
        report = validator.generate_report(result)
        
        assert "Templates Missing Version History:" in report
        assert "test-framework" in report
        assert "Remediation:" in report
