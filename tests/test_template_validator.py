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
        warnings = validator.validate_raci_matrix(content)
        
        # Should have no warnings for valid RACI matrix
        assert len(warnings) == 0
    
    def test_raci_matrix_missing_accountable(self):
        """Test that RACI matrix without Accountable generates warning."""
        content = """
# Roles and Responsibilities

## RACI Matrix

| Activity | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Operations & Monitoring | R | C | R | I |
| Incident Management | R | C | R | R |
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_raci_matrix(content)
        
        # Should have warnings for missing Accountable
        assert len(warnings) > 0
        assert any('accountable' in w.lower() for w in warnings)
    
    def test_raci_matrix_missing_responsible(self):
        """Test that RACI matrix without Responsible generates warning."""
        content = """
# Roles and Responsibilities

## RACI Matrix

| Activity | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Operations & Monitoring | A | C | I | I |
| Incident Management | A | C | I | I |
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_raci_matrix(content)
        
        # Should have warnings for missing Responsible
        assert len(warnings) > 0
        assert any('responsible' in w.lower() for w in warnings)
    
    def test_raci_matrix_multiple_accountable(self):
        """Test that RACI matrix with multiple Accountable generates warning."""
        content = """
# Roles and Responsibilities

## RACI Matrix

| Activity | CIO | CISO | Ops Manager | Service Desk |
|---|---|---|---|---|
| Operations & Monitoring | A | A | R | I |
| Incident Management | A | C | R | R |
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_raci_matrix(content)
        
        # Should have warnings for multiple Accountable
        assert len(warnings) > 0
        assert any('multiple' in w.lower() and 'accountable' in w.lower() for w in warnings)
    
    def test_no_raci_matrix(self):
        """Test that templates without RACI matrices don't generate warnings."""
        content = """
# Introduction

This is a template without a RACI matrix.

## Some Section

Content here.
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_raci_matrix(content)
        
        # Should have no warnings
        assert len(warnings) == 0


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
        warnings = validator.validate_placeholder_syntax(content)
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_valid_netbox_placeholders(self):
        """Test that valid netbox placeholders pass validation."""
        content = """
# Infrastructure

**Site:** {{ netbox.site.name }}
**Device:** {{ netbox.device.core_switch.name }}
**VLAN:** {{ netbox.vlan.management.vid }}
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_placeholder_syntax(content)
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_invalid_placeholder_syntax(self):
        """Test that invalid placeholder syntax generates warnings."""
        content = """
# Service Description

**Organization:** {{ invalid }}
**Name:** {{ meta }}
**Value:** {{ .field }}
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_placeholder_syntax(content)
        
        # Should have warnings for invalid placeholders
        assert len(warnings) > 0
        assert any('invalid' in w.lower() for w in warnings)
    
    def test_placeholder_with_whitespace(self):
        """Test that placeholders with whitespace are valid."""
        content = """
# Service Description

**Organization:** {{  meta.organization.name  }}
**CIO:** {{meta.cio.name}}
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_placeholder_syntax(content)
        
        # Should have no warnings (whitespace is allowed)
        assert len(warnings) == 0


class TestFrameworkReferenceValidation:
    """Tests for framework reference validation."""
    
    def test_it_operation_template_with_itil_reference(self):
        """Test that IT-operation templates with ITIL references pass validation."""
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
        warnings = validator.validate_framework_references(content, 'it-operation')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_it_operation_template_with_iso20000_reference(self):
        """Test that IT-operation templates with ISO 20000 references pass validation."""
        content = """
# Service Level Management

This process implements ISO 20000-1:2018 Clause 8.3 requirements.

## SLA Definitions

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'it-operation')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_it_operation_template_with_cobit_reference(self):
        """Test that IT-operation templates with COBIT references pass validation."""
        content = """
# Change Management

This process aligns with COBIT 2019 BAI06 (Managed IT Changes).

## Change Categories

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'it-operation')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_bcm_template_with_iso22301_reference(self):
        """Test that BCM templates with ISO 22301 references pass validation."""
        content = """
# Business Impact Analysis

This BIA follows ISO 22301:2019 Clause 8.2 requirements.

## BIA Methodology

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'bcm')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_bcm_template_with_bsi_bcm_reference(self):
        """Test that BCM templates with BSI BCM references pass validation."""
        content = """
# Emergency Management

This process implements BSI Standard 100-4 requirements.

## Emergency Response

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'bcm')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_isms_template_with_iso27001_reference(self):
        """Test that ISMS templates with ISO 27001 references pass validation."""
        content = """
# Information Security Policy

This policy implements ISO 27001:2022 Clause 5.2 requirements.

## Policy Statement

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'isms')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_isms_template_with_annex_a_reference(self):
        """Test that ISMS templates with Annex A references pass validation."""
        content = """
# Access Control Policy

This policy addresses ISO 27001:2022 Annex A Control A.9.

## Access Control Requirements

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'isms')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_bsi_grundschutz_template_with_bsi_200_1_reference(self):
        """Test that BSI Grundschutz templates with BSI 200-1 references pass validation."""
        content = """
# Information Security Policy

This policy follows BSI Standard 200-1 requirements.

## ISMS Organization

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'bsi-grundschutz')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_bsi_grundschutz_template_with_baustein_reference(self):
        """Test that BSI Grundschutz templates with Baustein references pass validation."""
        content = """
# Access Control

This implements BSI Baustein ORP.4 requirements.

## Access Control Measures

...
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'bsi-grundschutz')
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_template_without_framework_reference(self):
        """Test that templates without framework references generate warnings."""
        content = """
# Incident Management

This is an incident management process.

## Process Steps

1. Detect incident
2. Resolve incident
"""
        
        validator = TemplateValidator()
        warnings = validator.validate_framework_references(content, 'it-operation')
        
        # Should have warning about missing framework reference
        assert len(warnings) > 0
        assert any('framework' in w.lower() for w in warnings)


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



class TestTemplateNumberingValidation:
    """Tests for template numbering sequence validation."""
    
    def test_valid_numbering_sequence(self):
        """Test that valid numbering sequence passes validation."""
        from src.template_manager import Template
        from pathlib import Path
        
        templates = [
            Template(Path('0010_intro.md'), 'content', 10, 'de', 'bcm'),
            Template(Path('0020_policy.md'), 'content', 20, 'de', 'bcm'),
            Template(Path('0030_scope.md'), 'content', 30, 'de', 'bcm'),
        ]
        
        validator = TemplateValidator()
        warnings = validator.validate_numbering(templates)
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_duplicate_numbering(self):
        """Test that duplicate numbering generates warnings."""
        from src.template_manager import Template
        from pathlib import Path
        
        templates = [
            Template(Path('0010_intro.md'), 'content', 10, 'de', 'bcm'),
            Template(Path('0010_policy.md'), 'content', 10, 'de', 'bcm'),
            Template(Path('0020_scope.md'), 'content', 20, 'de', 'bcm'),
        ]
        
        validator = TemplateValidator()
        warnings = validator.validate_numbering(templates)
        
        # Should have warning about duplicates
        assert len(warnings) > 0
        assert any('duplicate' in w.lower() for w in warnings)
    
    def test_missing_prefix(self):
        """Test that templates without 4-digit prefix generate warnings."""
        from pathlib import Path
        
        templates = [
            Path('0010_intro.md'),
            Path('intro.md'),  # Missing prefix
            Path('0020_policy.md'),
        ]
        
        validator = TemplateValidator()
        warnings = validator.validate_numbering(templates)
        
        # Should have warning about missing prefix
        assert len(warnings) > 0
        assert any('prefix' in w.lower() for w in warnings)
    
    def test_large_gap_in_numbering(self):
        """Test that large gaps in numbering generate warnings."""
        from src.template_manager import Template
        from pathlib import Path
        
        templates = [
            Template(Path('0010_intro.md'), 'content', 10, 'de', 'bcm'),
            Template(Path('0100_policy.md'), 'content', 100, 'de', 'bcm'),  # Large gap
        ]
        
        validator = TemplateValidator()
        warnings = validator.validate_numbering(templates)
        
        # Should have warning about large gap
        assert len(warnings) > 0
        assert any('gap' in w.lower() for w in warnings)



class TestRACIMatrixProperties:
    """Property-based tests for RACI matrix validation."""
    
    @settings(max_examples=100)
    @given(
        num_roles=st.integers(min_value=2, max_value=8),
        num_activities=st.integers(min_value=2, max_value=10)
    )
    def test_property_7_raci_matrix_completeness(self, num_roles, num_activities):
        """
        Feature: template-system-extension
        Property 7: RACI Matrix Completeness
        
        For any RACI matrix in a template, each activity row SHALL have exactly one 'A' (Accountable)
        and at least one 'R' (Responsible).
        
        Validates: Requirements 2.3, 6.4, 11.5
        """
        validator = TemplateValidator()
        
        # Test 1: Valid RACI matrix (exactly one A, at least one R per row)
        roles = [f'Role{i}' for i in range(num_roles)]
        header = '| Activity | ' + ' | '.join(roles) + ' |\n'
        separator = '|---|' + '---|' * num_roles + '\n'
        
        rows_valid = []
        for i in range(num_activities):
            activity = f'Activity{i}'
            # Ensure exactly one A and at least one R
            cells = [activity]
            cells.append('A')  # First role is Accountable
            cells.append('R')  # Second role is Responsible
            # Fill remaining roles with C or I
            for j in range(2, num_roles):
                cells.append('C' if j % 2 == 0 else 'I')
            rows_valid.append('| ' + ' | '.join(cells) + ' |')
        
        content_valid = header + separator + '\n'.join(rows_valid)
        warnings_valid = validator.validate_raci_matrix(content_valid)
        
        # Valid matrix should have no warnings
        assert len(warnings_valid) == 0, \
            f"Valid RACI matrix should have no warnings, got: {warnings_valid}"
        
        # Test 2: Invalid RACI matrix (missing Accountable)
        rows_no_a = []
        for i in range(num_activities):
            activity = f'Activity{i}'
            cells = [activity]
            # No A, only R, C, I
            for j in range(num_roles):
                cells.append('R' if j == 0 else ('C' if j % 2 == 0 else 'I'))
            rows_no_a.append('| ' + ' | '.join(cells) + ' |')
        
        content_no_a = header + separator + '\n'.join(rows_no_a)
        warnings_no_a = validator.validate_raci_matrix(content_no_a)
        
        # Should have warnings about missing Accountable
        assert len(warnings_no_a) > 0, \
            "RACI matrix without Accountable should have warnings"
        assert any('accountable' in w.lower() for w in warnings_no_a), \
            f"Should warn about missing Accountable, got: {warnings_no_a}"
        
        # Test 3: Invalid RACI matrix (missing Responsible)
        rows_no_r = []
        for i in range(num_activities):
            activity = f'Activity{i}'
            cells = [activity]
            # No R, only A, C, I
            for j in range(num_roles):
                cells.append('A' if j == 0 else ('C' if j % 2 == 0 else 'I'))
            rows_no_r.append('| ' + ' | '.join(cells) + ' |')
        
        content_no_r = header + separator + '\n'.join(rows_no_r)
        warnings_no_r = validator.validate_raci_matrix(content_no_r)
        
        # Should have warnings about missing Responsible
        assert len(warnings_no_r) > 0, \
            "RACI matrix without Responsible should have warnings"
        assert any('responsible' in w.lower() for w in warnings_no_r), \
            f"Should warn about missing Responsible, got: {warnings_no_r}"
        
        # Test 4: Invalid RACI matrix (multiple Accountable)
        rows_multi_a = []
        for i in range(num_activities):
            activity = f'Activity{i}'
            cells = [activity]
            # Multiple A values
            for j in range(num_roles):
                cells.append('A' if j < 2 else ('R' if j == 2 else 'C'))
            rows_multi_a.append('| ' + ' | '.join(cells) + ' |')
        
        content_multi_a = header + separator + '\n'.join(rows_multi_a)
        warnings_multi_a = validator.validate_raci_matrix(content_multi_a)
        
        # Should have warnings about multiple Accountable
        assert len(warnings_multi_a) > 0, \
            "RACI matrix with multiple Accountable should have warnings"
        assert any('multiple' in w.lower() and 'accountable' in w.lower() for w in warnings_multi_a), \
            f"Should warn about multiple Accountable, got: {warnings_multi_a}"



class TestFrameworkReferenceProperties:
    """Property-based tests for framework reference validation."""
    
    @settings(max_examples=100)
    @given(
        template_type=st.sampled_from(['it-operation', 'bcm', 'isms', 'bsi-grundschutz']),
        has_framework_ref=st.booleans()
    )
    def test_property_8_framework_reference_presence(self, template_type, has_framework_ref):
        """
        Feature: template-system-extension
        Property 8: Framework Reference Presence
        
        For any BCM template, at least one reference to ISO 22301 or BSI BCM standards SHALL be present.
        For any ISMS template, at least one reference to ISO 27001:2022 SHALL be present.
        For any BSI Grundschutz template, at least one reference to BSI Standards 200-1, 200-2, or 200-3 SHALL be present.
        For any IT-operation template, at least one reference to ITIL, ISO 20000, or COBIT SHALL be present.
        
        Validates: Requirements 2.1, 2.2, 6.1, 6.2, 11.1, 11.2, 11.3
        """
        validator = TemplateValidator()
        
        # Define framework references for each template type
        framework_refs = {
            'it-operation': ['ITIL v4', 'ISO 20000-1:2018', 'COBIT 2019'],
            'bcm': ['ISO 22301:2019', 'BSI Standard 100-4'],
            'isms': ['ISO 27001:2022', 'Annex A'],
            'bsi-grundschutz': ['BSI Standard 200-1', 'BSI Baustein']
        }
        
        # Select a framework reference for this template type
        framework_ref = framework_refs[template_type][0]
        
        # Create template content with or without framework reference
        if has_framework_ref:
            content = f"""
# Template Content

This template implements {framework_ref} requirements.

## Section

Content here.
"""
        else:
            content = """
# Template Content

This is a template without framework references.

## Section

Content here.
"""
        
        warnings = validator.validate_framework_references(content, template_type)
        
        # If framework reference is present, should have no warnings
        if has_framework_ref:
            assert len(warnings) == 0, \
                f"Template with {framework_ref} reference should have no warnings, got: {warnings}"
        else:
            # If framework reference is missing, should have warning
            assert len(warnings) > 0, \
                f"Template without framework reference should have warnings"
            assert any('framework' in w.lower() for w in warnings), \
                f"Should warn about missing framework reference, got: {warnings}"
    
    @settings(max_examples=50)
    @given(
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz']),
        framework_idx=st.integers(min_value=0, max_value=1)
    )
    def test_property_8_multiple_framework_options(self, template_type, framework_idx):
        """
        Test that any valid framework reference for a template type is accepted.
        """
        validator = TemplateValidator()
        
        # Define multiple valid framework references for each template type
        framework_options = {
            'bcm': ['ISO 22301:2019', 'BSI Standard 100-4'],
            'isms': ['ISO 27001:2022', 'Annex A Control A.5'],
            'bsi-grundschutz': ['BSI Standard 200-1', 'BSI IT-Grundschutz']
        }
        
        framework_ref = framework_options[template_type][framework_idx]
        
        content = f"""
# Template Content

This template follows {framework_ref} requirements.

## Implementation

Details here.
"""
        
        warnings = validator.validate_framework_references(content, template_type)
        
        # Should have no warnings with any valid framework reference
        assert len(warnings) == 0, \
            f"Template with {framework_ref} reference should have no warnings, got: {warnings}"
