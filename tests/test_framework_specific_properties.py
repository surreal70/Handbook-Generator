"""
Property tests for framework-specific requirements.

Tests Property 2 (Template Numbering Increments) and Property 16 (Framework Requirement Mapping Completeness)
for IDW PS 951, NIST CSF 2.0, and TOGAF templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026

Validates: Requirements 4.2, 10.3
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import re


class TestTemplateNumberingIncrements:
    """
    Property 2: Template Numbering Increments
    
    For any sequence of consecutive templates in a framework, the numeric prefixes
    must increment by 10 (e.g., 0010, 0020, 0030).
    
    Validates: Requirements 4.2
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf']),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_2_template_numbering_increments(self, template_base_path, framework, language):
        """
        Feature: additional-compliance-frameworks, Property 2: Template Numbering Increments
        
        For any sequence of consecutive templates in a framework, the numeric prefixes
        must increment by 10 (e.g., 0010, 0020, 0030).
        
        Validates: Requirements 4.2
        """
        framework_dir = template_base_path / language / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{framework} {language} templates not found")
        
        # Get all content templates (excluding metadata and README)
        templates = sorted([
            f for f in framework_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ])
        
        if len(templates) < 2:
            pytest.skip(f"Not enough templates to test numbering increments")
        
        # Extract template numbers
        template_numbers = []
        for template in templates:
            try:
                number = int(template.name[:4])
                template_numbers.append(number)
            except ValueError:
                # Skip templates without valid numeric prefix
                continue
        
        if len(template_numbers) < 2:
            pytest.skip("Not enough numbered templates")
        
        # Check that consecutive templates increment by 10
        for i in range(len(template_numbers) - 1):
            current = template_numbers[i]
            next_num = template_numbers[i + 1]
            
            # Calculate expected increment
            increment = next_num - current
            
            # Increment should be a multiple of 10
            assert increment % 10 == 0, \
                f"Template numbering should increment by multiples of 10. " \
                f"Found increment of {increment} between {current:04d} and {next_num:04d}"
            
            # Increment should be at least 10 (allowing for gaps)
            assert increment >= 10, \
                f"Template numbering should increment by at least 10. " \
                f"Found increment of {increment} between {current:04d} and {next_num:04d}"
    
    def test_idw_ps_951_numbering_increments(self, template_base_path):
        """Test that IDW PS 951 templates use 10-step increments."""
        for language in ['de', 'en']:
            framework_dir = template_base_path / language / "idw-ps-951"
            
            if not framework_dir.exists():
                continue
            
            templates = sorted([
                f for f in framework_dir.glob("*.md")
                if not f.name.startswith("0000_") and f.name != "README.md"
            ])
            
            template_numbers = []
            for template in templates:
                try:
                    number = int(template.name[:4])
                    template_numbers.append(number)
                except ValueError:
                    continue
            
            # Check increments
            for i in range(len(template_numbers) - 1):
                increment = template_numbers[i + 1] - template_numbers[i]
                assert increment % 10 == 0, \
                    f"IDW PS 951 {language}: Increment should be multiple of 10, got {increment}"
    
    def test_nist_csf_numbering_increments(self, template_base_path):
        """Test that NIST CSF templates use 10-step increments."""
        for language in ['de', 'en']:
            framework_dir = template_base_path / language / "nist-csf"
            
            if not framework_dir.exists():
                continue
            
            templates = sorted([
                f for f in framework_dir.glob("*.md")
                if not f.name.startswith("0000_") and f.name != "README.md"
            ])
            
            template_numbers = []
            for template in templates:
                try:
                    number = int(template.name[:4])
                    template_numbers.append(number)
                except ValueError:
                    continue
            
            # Check increments
            for i in range(len(template_numbers) - 1):
                increment = template_numbers[i + 1] - template_numbers[i]
                assert increment % 10 == 0, \
                    f"NIST CSF {language}: Increment should be multiple of 10, got {increment}"
    
    def test_togaf_numbering_increments(self, template_base_path):
        """Test that TOGAF templates use 10-step increments."""
        for language in ['de', 'en']:
            framework_dir = template_base_path / language / "togaf"
            
            if not framework_dir.exists():
                continue
            
            templates = sorted([
                f for f in framework_dir.glob("*.md")
                if not f.name.startswith("0000_") and f.name != "README.md"
            ])
            
            template_numbers = []
            for template in templates:
                try:
                    number = int(template.name[:4])
                    template_numbers.append(number)
                except ValueError:
                    continue
            
            # Check increments
            for i in range(len(template_numbers) - 1):
                increment = template_numbers[i + 1] - template_numbers[i]
                assert increment % 10 == 0, \
                    f"TOGAF {language}: Increment should be multiple of 10, got {increment}"


class TestFrameworkRequirementMappingCompleteness:
    """
    Property 16: Framework Requirement Mapping Completeness
    
    For any framework requirement or control listed in FRAMEWORK_MAPPING.md,
    it must be mapped to at least one specific template file.
    
    Validates: Requirements 10.3
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def test_idw_ps_951_framework_mapping_exists(self, template_base_path):
        """Test that IDW PS 951 has FRAMEWORK_MAPPING.md files."""
        for language in ['de', 'en']:
            framework_dir = template_base_path / language / "idw-ps-951"
            
            if not framework_dir.exists():
                continue
            
            mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
            assert mapping_file.exists(), \
                f"IDW PS 951 {language} should have FRAMEWORK_MAPPING.md"
            
            # Check that file has content
            content = mapping_file.read_text()
            assert len(content) > 0, \
                f"IDW PS 951 {language} FRAMEWORK_MAPPING.md should have content"
    
    def test_nist_csf_framework_mapping_exists(self, template_base_path):
        """Test that NIST CSF has FRAMEWORK_MAPPING.md files."""
        for language in ['de', 'en']:
            framework_dir = template_base_path / language / "nist-csf"
            
            if not framework_dir.exists():
                continue
            
            mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
            assert mapping_file.exists(), \
                f"NIST CSF {language} should have FRAMEWORK_MAPPING.md"
            
            # Check that file has content
            content = mapping_file.read_text()
            assert len(content) > 0, \
                f"NIST CSF {language} FRAMEWORK_MAPPING.md should have content"
    
    def test_togaf_framework_mapping_exists(self, template_base_path):
        """Test that TOGAF has FRAMEWORK_MAPPING.md files."""
        for language in ['de', 'en']:
            framework_dir = template_base_path / language / "togaf"
            
            if not framework_dir.exists():
                continue
            
            mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
            assert mapping_file.exists(), \
                f"TOGAF {language} should have FRAMEWORK_MAPPING.md"
            
            # Check that file has content
            content = mapping_file.read_text()
            assert len(content) > 0, \
                f"TOGAF {language} FRAMEWORK_MAPPING.md should have content"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf']),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_16_framework_requirement_mapping_completeness(self, template_base_path, framework, language):
        """
        Feature: additional-compliance-frameworks, Property 16: Framework Requirement Mapping Completeness
        
        For any framework requirement or control listed in FRAMEWORK_MAPPING.md,
        it must be mapped to at least one specific template file.
        
        Validates: Requirements 10.3
        """
        framework_dir = template_base_path / language / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{framework} {language} templates not found")
        
        mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
        
        if not mapping_file.exists():
            pytest.skip(f"FRAMEWORK_MAPPING.md not found for {framework} {language}")
        
        # Read mapping file
        content = mapping_file.read_text()
        
        # Extract template references (e.g., 0010_, 0020_)
        template_refs = re.findall(r'(\d{4})_', content)
        
        # Get actual template files
        actual_templates = [
            f.name[:4] for f in framework_dir.glob("*.md")
            if not f.name.startswith("0000_") and f.name != "README.md"
        ]
        
        # Verify that referenced templates exist
        for ref in set(template_refs):
            assert ref in actual_templates, \
                f"FRAMEWORK_MAPPING.md references template {ref}_ which doesn't exist"
        
        # Verify that mapping file has some template references
        assert len(template_refs) > 0, \
            f"FRAMEWORK_MAPPING.md should reference at least one template"
    
    def test_framework_mapping_references_valid_templates(self, template_base_path):
        """Test that FRAMEWORK_MAPPING.md files reference valid templates."""
        frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in frameworks:
            for language in ['de', 'en']:
                framework_dir = template_base_path / language / framework
                
                if not framework_dir.exists():
                    continue
                
                mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
                
                if not mapping_file.exists():
                    continue
                
                content = mapping_file.read_text()
                
                # Extract template references
                template_refs = re.findall(r'(\d{4})_', content)
                
                # Get actual templates
                actual_templates = {
                    f.name[:4] for f in framework_dir.glob("*.md")
                    if not f.name.startswith("0000_") and f.name != "README.md"
                }
                
                # Check that all references are valid
                for ref in set(template_refs):
                    assert ref in actual_templates, \
                        f"{framework} {language}: FRAMEWORK_MAPPING.md references " \
                        f"non-existent template {ref}_"
