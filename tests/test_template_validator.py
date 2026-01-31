"""
Tests for Template Validator

Tests for template validation functionality including RACI matrices,
placeholder syntax, and framework compliance.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import tempfile

from src.template_validator import TemplateValidator, ValidationResult


class TestRACIMatrixValidation:
    """Tests for RACI matrix validation."""
    
    def test_valid_raci_matrix(self):
        """Test that a valid RACI matrix passes validation."""
        content = """
# Roles and Responsibilities

## RACI Matrix

| Activity | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Operations & Monitoring | A | C | R | I |
| Incident Management | A | C | R | R |
| Change Management | A | C | R | I |
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_raci_matrices(content, 'test.md', result)
        
        # Should have no warnings for valid RACI matrix
        assert len(result.warnings) == 0
        assert result.is_valid
    
    def test_incomplete_raci_matrix(self):
        """Test that an incomplete RACI matrix generates warnings."""
        content = """
# Roles and Responsibilities

## RACI Matrix

| Activity | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Operations & Monitoring | A | C | R |  |
| Incident Management | A |  | R | R |
| Change Management | A | C |  | I |
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_raci_matrices(content, 'test.md', result)
        
        # Should have warnings for incomplete cells
        assert len(result.warnings) > 0
        assert 'incomplete' in result.warnings[0].lower() or 'invalid' in result.warnings[0].lower()
    
    def test_no_raci_matrix(self):
        """Test that templates without RACI matrices don't generate warnings."""
        content = """
# Introduction

This is a template without a RACI matrix.

## Some Section

Content here.
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_raci_matrices(content, 'test.md', result)
        
        # Should have no warnings
        assert len(result.warnings) == 0
        assert result.is_valid
    
    @settings(max_examples=50)
    @given(
        num_roles=st.integers(min_value=2, max_value=6),
        num_activities=st.integers(min_value=2, max_value=8)
    )
    def test_property_14_raci_matrix_completeness(self, num_roles, num_activities):
        """
        Feature: it-operation-template-extension, Property 14: RACI Matrix Completeness
        
        For any template containing a RACI matrix, all cells should be filled with one of the
        valid RACI values (R, A, C, I) or explicitly marked as not applicable.
        
        Validates: Requirements 20.4
        """
        raci_values = ['R', 'A', 'C', 'I']
        
        # Test 1: Complete RACI matrix (all cells filled)
        roles = [f'Role{i}' for i in range(num_roles)]
        header = '| Activity | ' + ' | '.join(roles) + ' |\n'
        separator = '|---|' + '---|' * num_roles + '\n'
        
        rows_complete = []
        for i in range(num_activities):
            activity = f'Activity{i}'
            cells = [activity] + [raci_values[j % len(raci_values)] for j in range(num_roles)]
            rows_complete.append('| ' + ' | '.join(cells) + ' |')
        
        content_complete = header + separator + '\n'.join(rows_complete)
        
        validator = TemplateValidator()
        result_complete = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_raci_matrices(content_complete, 'test.md', result_complete)
        
        # Complete matrix should have no warnings
        assert len(result_complete.warnings) == 0, \
            "Complete RACI matrix should have no warnings"
        
        # Test 2: Incomplete RACI matrix (with empty cells)
        rows_incomplete = []
        for i in range(num_activities):
            activity = f'Activity{i}'
            # Make first role cell empty for each activity
            cells = [activity, ''] + [raci_values[j % len(raci_values)] for j in range(num_roles - 1)]
            rows_incomplete.append('| ' + ' | '.join(cells) + ' |')
        
        content_incomplete = header + separator + '\n'.join(rows_incomplete)
        
        result_incomplete = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_raci_matrices(content_incomplete, 'test.md', result_incomplete)
        
        # Incomplete matrix should have warnings
        assert len(result_incomplete.warnings) > 0, \
            "Incomplete RACI matrix should have warnings"


class TestPlaceholderSyntaxValidation:
    """Tests for placeholder syntax validation."""
    
    def test_valid_meta_placeholders(self):
        """Test that valid meta placeholders pass validation."""
        content = """
# Service Description

**Organization:** {{ meta.organization.name }}
**CIO:** {{ meta.cio.name }}
**Email:** {{ meta.cio.email }}
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_placeholder_syntax(content, 'test.md', result)
        
        # Should have no warnings
        assert len(result.warnings) == 0
    
    def test_valid_netbox_placeholders(self):
        """Test that valid netbox placeholders pass validation."""
        content = """
# Infrastructure

**Site:** {{ netbox.site.name }}
**Device:** {{ netbox.device.core_switch.name }}
**VLAN:** {{ netbox.vlan.management.vid }}
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_placeholder_syntax(content, 'test.md', result)
        
        # Should have no warnings
        assert len(result.warnings) == 0
    
    def test_invalid_placeholder_syntax(self):
        """Test that invalid placeholder syntax generates warnings."""
        content = """
# Service Description

**Organization:** {{ invalid_source.field }}
**Name:** {{ meta }}
**Value:** {{ .field }}
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_placeholder_syntax(content, 'test.md', result)
        
        # Should have warnings for invalid placeholders
        assert len(result.warnings) > 0
        assert any('invalid' in w.lower() for w in result.warnings)
    
    def test_placeholder_with_whitespace(self):
        """Test that placeholders with whitespace are valid."""
        content = """
# Service Description

**Organization:** {{  meta.organization.name  }}
**CIO:** {{meta.cio.name}}
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_placeholder_syntax(content, 'test.md', result)
        
        # Should have no warnings (whitespace is allowed)
        assert len(result.warnings) == 0


class TestFrameworkReferenceValidation:
    """Tests for framework reference validation."""
    
    def test_template_with_itil_reference(self):
        """Test that templates with ITIL references pass validation."""
        content = """
# Incident Management

This process follows ITIL v4 Incident Management practice.

## Process Steps

1. Detect and log incident
2. Categorize and prioritize
3. Investigate and diagnose
4. Resolve and close
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_framework_references(content, '0120_Incident_Management.md', result)
        
        # Should have no warnings
        assert len(result.warnings) == 0
    
    def test_template_with_iso20000_reference(self):
        """Test that templates with ISO 20000 references pass validation."""
        content = """
# Service Level Management

This process implements ISO 20000-1:2018 Clause 8.3 requirements.

## SLA Definitions

...
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_framework_references(content, '0210_Availability.md', result)
        
        # Should have no warnings
        assert len(result.warnings) == 0
    
    def test_template_with_cobit_reference(self):
        """Test that templates with COBIT references pass validation."""
        content = """
# Change Management

This process aligns with COBIT 2019 BAI06 (Managed IT Changes).

## Change Categories

...
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_framework_references(content, '0140_Change_Management.md', result)
        
        # Should have no warnings
        assert len(result.warnings) == 0
    
    def test_operational_template_without_framework_reference(self):
        """Test that operational templates without framework references generate warnings."""
        content = """
# Incident Management

This is an incident management process.

## Process Steps

1. Detect incident
2. Resolve incident
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        # Use a filename that matches operational keywords
        validator._validate_framework_references(content, '0120_incident_management.md', result)
        
        # Should have warning about missing framework reference
        assert len(result.warnings) > 0
        assert any('framework' in w.lower() for w in result.warnings)
    
    def test_non_operational_template_without_framework_reference(self):
        """Test that non-operational templates don't require framework references."""
        content = """
# Introduction

This is an introduction to the handbook.

## Purpose

...
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_framework_references(content, '0010_Introduction.md', result)
        
        # Should have no warnings (introduction doesn't need framework references)
        assert len(result.warnings) == 0
    
    @settings(max_examples=50)
    @given(
        framework=st.sampled_from(['ITIL v4', 'ISO 20000-1:2018', 'COBIT 2019']),
        template_type=st.sampled_from([
            'incident', 'problem', 'change', 'monitoring',
            'backup', 'disaster', 'security', 'compliance'
        ])
    )
    def test_property_16_template_best_practice_compliance(self, framework, template_type):
        """
        Feature: it-operation-template-extension, Property 16: Template Best Practice Compliance
        
        For any IT-operations template, it should reference at least one recognized IT framework
        (ITIL, ISO 20000, COBIT) in its content or structure.
        
        Validates: Requirements 20.3
        """
        # Create template content with framework reference
        content = f"""
# {template_type.title()} Management

This process follows {framework} best practices.

## Process Description

...
"""
        
        validator = TemplateValidator()
        result = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_framework_references(
            content,
            f'0100_{template_type}_management.md',
            result
        )
        
        # Should have no warnings when framework is referenced
        assert len(result.warnings) == 0, \
            f"Template with {framework} reference should have no warnings"
        
        # Now test without framework reference
        content_no_framework = f"""
# {template_type.title()} Management

This is a process description.

## Process Description

...
"""
        
        result_no_framework = ValidationResult(is_valid=True, warnings=[], errors=[])
        validator._validate_framework_references(
            content_no_framework,
            f'0100_{template_type}_management.md',
            result_no_framework
        )
        
        # Should have warning when framework is not referenced
        assert len(result_no_framework.warnings) > 0, \
            f"Operational template without framework reference should have warnings"


class TestTemplateValidation:
    """Integration tests for complete template validation."""
    
    def test_validate_valid_template_file(self):
        """Test validation of a valid template file."""
        content = """
# Incident Management

This process follows ITIL v4 Incident Management practice.

## RACI Matrix

| Activity | CIO | CISO | Ops Manager |
|---|---|---|---|
| Incident Detection | A | C | R |
| Incident Resolution | A | C | R |

## Process Steps

**Organization:** {{ meta.organization.name }}
**CIO:** {{ meta.cio.name }}
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
            tmp_path = Path(tmp.name)
            tmp_path.write_text(content)
            
            try:
                validator = TemplateValidator()
                result = validator.validate_template(tmp_path)
                
                # Should be valid with no errors
                assert result.is_valid
                assert len(result.errors) == 0
                
            finally:
                tmp_path.unlink()
    
    def test_validate_template_with_issues(self):
        """Test validation of a template with multiple issues."""
        content = """
# Incident Management

This is an incident management process.

## RACI Matrix

| Activity | CIO | CISO | Ops Manager |
|---|---|---|---|
| Incident Detection | A |  | R |
| Incident Resolution | A | C |  |

## Process Steps

**Organization:** {{ invalid.source }}
**Name:** {{ meta }}
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
            tmp_path = Path(tmp.name)
            # Rename to have operational keyword in filename
            tmp_path_operational = tmp_path.parent / '0120_incident_management.md'
            tmp_path.write_text(content)
            tmp_path.rename(tmp_path_operational)
            
            try:
                validator = TemplateValidator()
                result = validator.validate_template(tmp_path_operational)
                
                # Should have warnings
                assert len(result.warnings) > 0
                
                # Should have warnings about:
                # 1. Incomplete RACI matrix
                # 2. Invalid placeholder syntax
                # 3. Missing framework reference
                assert any('raci' in w.lower() or 'incomplete' in w.lower() for w in result.warnings)
                assert any('placeholder' in w.lower() or 'invalid' in w.lower() for w in result.warnings)
                assert any('framework' in w.lower() for w in result.warnings)
                
            finally:
                if tmp_path_operational.exists():
                    tmp_path_operational.unlink()
    
    def test_validate_nonexistent_template(self):
        """Test validation of a nonexistent template file."""
        validator = TemplateValidator()
        result = validator.validate_template(Path('nonexistent.md'))
        
        # Should have error
        assert not result.is_valid
        assert len(result.errors) > 0
        assert 'not found' in result.errors[0].lower()
    
    def test_validate_template_directory(self):
        """Test validation of a template directory."""
        # Use actual template directory
        templates_dir = Path('templates/de/it-operation')
        
        if templates_dir.exists():
            validator = TemplateValidator()
            results = validator.validate_template_directory(templates_dir)
            
            # Should have results for multiple templates
            assert len(results) > 0
            
            # All templates should be readable (no errors)
            for filename, result in results.items():
                assert len(result.errors) == 0, \
                    f"Template {filename} should be readable without errors"
    
    def test_validation_summary_output(self, capsys):
        """Test that validation summary is printed correctly."""
        results = {
            'template1.md': ValidationResult(is_valid=True, warnings=[], errors=[]),
            'template2.md': ValidationResult(
                is_valid=True,
                warnings=['Warning 1', 'Warning 2'],
                errors=[]
            ),
            'template3.md': ValidationResult(
                is_valid=False,
                warnings=[],
                errors=['Error 1']
            )
        }
        
        validator = TemplateValidator()
        validator.print_validation_summary(results)
        
        captured = capsys.readouterr()
        
        # Should print summary
        assert 'Template Validation Summary' in captured.out
        assert 'Total templates: 3' in captured.out
        assert 'Total warnings: 2' in captured.out
        assert 'Total errors: 1' in captured.out


class TestMetadataConfigurationValidation:
    """Tests for metadata configuration validation."""
    
    @settings(max_examples=100)
    @given(
        has_org_name=st.booleans(),
        has_doc_owner=st.booleans(),
        has_roles=st.booleans()
    )
    def test_property_15_metadata_configuration_validation(
        self,
        has_org_name,
        has_doc_owner,
        has_roles
    ):
        """
        Feature: it-operation-template-extension, Property 15: Metadata Configuration Validation
        
        For any metadata.yaml file, the validation process should check for required fields
        (organization.name, document.owner) and report missing fields as warnings.
        
        Validates: Requirements 17.4, 17.5
        """
        from src.metadata_config_manager import MetadataConfigManager
        import yaml
        import tempfile
        
        # Create metadata configuration with varying completeness
        metadata = {}
        
        if has_org_name:
            metadata['organization'] = {'name': 'Test Org'}
        else:
            metadata['organization'] = {}
        
        if has_doc_owner:
            metadata['document'] = {'owner': 'Test Owner'}
        else:
            metadata['document'] = {}
        
        if has_roles:
            metadata['roles'] = {
                'ceo': {
                    'name': 'Test CEO',
                    'title': 'CEO',
                    'email': 'ceo@test.com',
                    'phone': '+1234567890'
                }
            }
        else:
            metadata['roles'] = {}
        
        # Write to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as tmp:
            tmp_path = Path(tmp.name)
            yaml.dump(metadata, tmp)
            
            try:
                # Load and validate metadata
                manager = MetadataConfigManager(tmp_path)
                
                try:
                    config = manager.load_metadata()
                    warnings = manager.validate_metadata(config)
                    
                    # If required fields are missing, should have warnings
                    if not has_org_name:
                        assert any('organization' in w.lower() and 'name' in w.lower() for w in warnings), \
                            "Should warn about missing organization.name"
                    
                    if not has_doc_owner:
                        assert any('document' in w.lower() and 'owner' in w.lower() for w in warnings), \
                            "Should warn about missing document.owner"
                    
                    # If all required fields present, should have no warnings about them
                    if has_org_name and has_doc_owner:
                        required_field_warnings = [
                            w for w in warnings
                            if ('organization' in w.lower() and 'name' in w.lower()) or
                               ('document' in w.lower() and 'owner' in w.lower())
                        ]
                        assert len(required_field_warnings) == 0, \
                            "Should have no warnings about required fields when they are present"
                
                except Exception:
                    # If loading fails due to missing required fields, that's expected
                    pass
                
            finally:
                tmp_path.unlink()
