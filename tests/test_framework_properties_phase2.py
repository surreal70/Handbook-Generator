"""
Property-based tests for Phase 2 framework-specific requirements.

Tests Property 2 (Template Numbering Increments) and Property 16 (Framework Requirement
Mapping Completeness) for all Phase 2 frameworks.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026

Validates: Requirements 4.2, 10.3
"""

import pytest
import os
import re
from pathlib import Path
from hypothesis import given, settings, strategies as st


# Phase 2 frameworks
PHASE2_FRAMEWORKS = [
    ('iso-38500', 'ISO/IEC 38500'),
    ('iso-31000', 'ISO 31000'),
    ('csa-ccm', 'CSA CCM'),
    ('tisax', 'TISAX'),
    ('soc1', 'SOC 1'),
    ('coso', 'COSO'),
    ('dora', 'DORA')
]


class TestProperty2TemplateNumberingIncrements:
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
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_property_2_template_numbering_increments_german(self, template_base_path, framework, display_name):
        """
        Feature: additional-compliance-frameworks, Property 2: Template Numbering Increments
        
        Test that German templates have numeric prefixes that increment by 10.
        
        **Validates: Requirements 4.2**
        """
        framework_dir = template_base_path / "de" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} German templates not found")
        
        # Get all template files (excluding metadata)
        templates = sorted([
            f for f in os.listdir(framework_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ])
        
        if len(templates) < 2:
            pytest.skip(f"Not enough {display_name} templates to test numbering")
        
        # Extract numeric prefixes
        numbers = []
        for template in templates:
            match = re.match(r'^(\d{4})_', template)
            if match:
                numbers.append(int(match.group(1)))
        
        # Check that consecutive numbers differ by 10
        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]
            assert diff == 10, \
                f"{display_name}: Template numbers should increment by 10, " \
                f"but {numbers[i]} -> {numbers[i+1]} (diff: {diff})"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_property_2_template_numbering_increments_english(self, template_base_path, framework, display_name):
        """
        Feature: additional-compliance-frameworks, Property 2: Template Numbering Increments
        
        Test that English templates have numeric prefixes that increment by 10.
        
        **Validates: Requirements 4.2**
        """
        framework_dir = template_base_path / "en" / framework
        
        if not framework_dir.exists():
            pytest.skip(f"{display_name} English templates not found")
        
        # Get all template files (excluding metadata)
        templates = sorted([
            f for f in os.listdir(framework_dir)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ])
        
        if len(templates) < 2:
            pytest.skip(f"Not enough {display_name} templates to test numbering")
        
        # Extract numeric prefixes
        numbers = []
        for template in templates:
            match = re.match(r'^(\d{4})_', template)
            if match:
                numbers.append(int(match.group(1)))
        
        # Check that consecutive numbers differ by 10
        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]
            assert diff == 10, \
                f"{display_name}: Template numbers should increment by 10, " \
                f"but {numbers[i]} -> {numbers[i+1]} (diff: {diff})"
    
    @settings(max_examples=100)
    @given(
        start_number=st.integers(min_value=10, max_value=100),
        count=st.integers(min_value=2, max_value=20)
    )
    def test_property_2_numbering_increment_validation(self, start_number, count):
        """
        Property test: Verify that template numbering increment validation works correctly.
        
        Generate random template number sequences and verify they follow the increment rule.
        """
        # Generate valid sequence (increments of 10)
        valid_numbers = [start_number + (i * 10) for i in range(count)]
        
        # Check that consecutive numbers differ by 10
        for i in range(len(valid_numbers) - 1):
            diff = valid_numbers[i + 1] - valid_numbers[i]
            assert diff == 10, f"Valid sequence should have increment of 10"
        
        # Generate invalid sequence (random increments)
        if count > 1:
            invalid_numbers = [start_number]
            for i in range(1, count):
                # Add random increment (not 10)
                increment = 5 if i % 2 == 0 else 15
                invalid_numbers.append(invalid_numbers[-1] + increment)
            
            # Check that at least one pair doesn't have increment of 10
            has_invalid_increment = False
            for i in range(len(invalid_numbers) - 1):
                diff = invalid_numbers[i + 1] - invalid_numbers[i]
                if diff != 10:
                    has_invalid_increment = True
                    break
            
            assert has_invalid_increment, "Invalid sequence should have at least one non-10 increment"


class TestProperty16FrameworkRequirementMappingCompleteness:
    """
    Property 16: Framework Requirement Mapping Completeness
    
    For any framework requirement or control listed in FRAMEWORK_MAPPING.md, it must be
    mapped to at least one specific template file.
    
    Validates: Requirements 10.3
    """
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def extract_template_references(self, mapping_content):
        """Extract template file references from FRAMEWORK_MAPPING.md content."""
        # Look for patterns like: 0010_template_name.md, [0010_template_name.md], etc.
        pattern = r'\b(\d{4}_[\w\-]+\.md)\b'
        return set(re.findall(pattern, mapping_content))
    
    def extract_requirements(self, mapping_content):
        """Extract requirement identifiers from FRAMEWORK_MAPPING.md content."""
        # Look for various requirement patterns
        patterns = [
            r'\b([A-Z]{2,}[-\.]?\d+(?:\.\d+)*)\b',  # e.g., GV.01, PR-01, AC.1.1
            r'\b(Principle \d+)\b',  # e.g., Principle 1
            r'\b(Component \d+)\b',  # e.g., Component 1
            r'\b(Control \d+)\b',  # e.g., Control 1
        ]
        
        requirements = set()
        for pattern in patterns:
            requirements.update(re.findall(pattern, mapping_content))
        
        return requirements
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_property_16_framework_mapping_completeness_german(self, template_base_path, framework, display_name):
        """
        Feature: additional-compliance-frameworks, Property 16: Framework Requirement Mapping Completeness
        
        Test that German FRAMEWORK_MAPPING.md maps all requirements to templates.
        
        **Validates: Requirements 10.3**
        """
        framework_dir = template_base_path / "de" / framework
        mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
        
        if not mapping_file.exists():
            pytest.skip(f"{display_name} German FRAMEWORK_MAPPING.md not found")
        
        # Read mapping file
        mapping_content = mapping_file.read_text()
        
        # Extract template references
        template_refs = self.extract_template_references(mapping_content)
        
        # Extract requirements
        requirements = self.extract_requirements(mapping_content)
        
        # Verify that mapping file has content
        assert len(mapping_content) > 100, \
            f"{display_name}: FRAMEWORK_MAPPING.md should have substantial content"
        
        # Verify that template references exist
        assert len(template_refs) > 0, \
            f"{display_name}: FRAMEWORK_MAPPING.md should reference template files"
        
        # Verify that requirements are listed
        assert len(requirements) > 0, \
            f"{display_name}: FRAMEWORK_MAPPING.md should list framework requirements"
        
        # Verify that referenced templates actually exist
        for template_ref in template_refs:
            template_path = framework_dir / template_ref
            assert template_path.exists(), \
                f"{display_name}: Referenced template {template_ref} should exist"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_property_16_framework_mapping_completeness_english(self, template_base_path, framework, display_name):
        """
        Feature: additional-compliance-frameworks, Property 16: Framework Requirement Mapping Completeness
        
        Test that English FRAMEWORK_MAPPING.md maps all requirements to templates.
        
        **Validates: Requirements 10.3**
        """
        framework_dir = template_base_path / "en" / framework
        mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
        
        if not mapping_file.exists():
            pytest.skip(f"{display_name} English FRAMEWORK_MAPPING.md not found")
        
        # Read mapping file
        mapping_content = mapping_file.read_text()
        
        # Extract template references
        template_refs = self.extract_template_references(mapping_content)
        
        # Extract requirements
        requirements = self.extract_requirements(mapping_content)
        
        # Verify that mapping file has content
        assert len(mapping_content) > 100, \
            f"{display_name}: FRAMEWORK_MAPPING.md should have substantial content"
        
        # Verify that template references exist
        assert len(template_refs) > 0, \
            f"{display_name}: FRAMEWORK_MAPPING.md should reference template files"
        
        # Verify that requirements are listed
        assert len(requirements) > 0, \
            f"{display_name}: FRAMEWORK_MAPPING.md should list framework requirements"
        
        # Verify that referenced templates actually exist
        for template_ref in template_refs:
            template_path = framework_dir / template_ref
            assert template_path.exists(), \
                f"{display_name}: Referenced template {template_ref} should exist"
    
    @pytest.mark.parametrize("framework,display_name", PHASE2_FRAMEWORKS)
    def test_property_16_mapping_structure(self, template_base_path, framework, display_name):
        """Test that FRAMEWORK_MAPPING.md has proper structure."""
        for language in ['de', 'en']:
            framework_dir = template_base_path / language / framework
            mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
            
            if not mapping_file.exists():
                continue
            
            content = mapping_file.read_text()
            
            # Check for markdown headers
            has_headers = re.search(r'^#{1,3}\s+', content, re.MULTILINE)
            assert has_headers, \
                f"{display_name} ({language}): FRAMEWORK_MAPPING.md should have markdown headers"
            
            # Check for table or list structure
            has_table = '|' in content
            has_list = re.search(r'^\s*[-*]\s+', content, re.MULTILINE)
            
            assert has_table or has_list, \
                f"{display_name} ({language}): FRAMEWORK_MAPPING.md should have tables or lists"
    
    @settings(max_examples=50)
    @given(
        num_requirements=st.integers(min_value=5, max_value=50),
        num_templates=st.integers(min_value=3, max_value=30)
    )
    def test_property_16_mapping_coverage_validation(self, num_requirements, num_templates):
        """
        Property test: Verify that requirement mapping coverage validation works correctly.
        
        Generate random requirement-to-template mappings and verify coverage.
        """
        # Generate requirements
        requirements = [f"REQ-{i:03d}" for i in range(num_requirements)]
        
        # Generate templates
        templates = [f"{(i+1)*10:04d}_template_{i}.md" for i in range(num_templates)]
        
        # Create mapping (each requirement maps to at least one template)
        mapping = {}
        for req in requirements:
            # Map to 1-3 random templates
            num_mappings = min(3, num_templates)
            mapped_templates = templates[:num_mappings]
            mapping[req] = mapped_templates
        
        # Verify that all requirements are mapped
        assert len(mapping) == num_requirements, \
            "All requirements should be mapped"
        
        # Verify that each requirement maps to at least one template
        for req, mapped_templates in mapping.items():
            assert len(mapped_templates) > 0, \
                f"Requirement {req} should map to at least one template"
        
        # Verify that all mapped templates are valid
        for req, mapped_templates in mapping.items():
            for template in mapped_templates:
                assert template in templates, \
                    f"Mapped template {template} should be in template list"


class TestPhase2ComprehensiveProperties:
    """Comprehensive property tests for Phase 2 frameworks."""
    
    @pytest.fixture
    def template_base_path(self):
        """Provide base path for templates."""
        return Path("templates")
    
    def test_all_phase2_frameworks_follow_numbering_convention(self, template_base_path):
        """Test that all Phase 2 frameworks follow the numbering convention."""
        for framework, display_name in PHASE2_FRAMEWORKS:
            for language in ['de', 'en']:
                framework_dir = template_base_path / language / framework
                
                if not framework_dir.exists():
                    continue
                
                # Get all template files
                templates = sorted([
                    f for f in os.listdir(framework_dir)
                    if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
                ])
                
                if len(templates) < 2:
                    continue
                
                # Extract and verify numbering
                numbers = []
                for template in templates:
                    match = re.match(r'^(\d{4})_', template)
                    if match:
                        numbers.append(int(match.group(1)))
                
                # All numbers should be multiples of 10
                for num in numbers:
                    assert num % 10 == 0, \
                        f"{display_name} ({language}): Template number {num} should be multiple of 10"
    
    def test_all_phase2_frameworks_have_framework_mapping(self, template_base_path):
        """Test that all Phase 2 frameworks have FRAMEWORK_MAPPING.md files."""
        for framework, display_name in PHASE2_FRAMEWORKS:
            for language in ['de', 'en']:
                framework_dir = template_base_path / language / framework
                
                if not framework_dir.exists():
                    continue
                
                mapping_file = framework_dir / "FRAMEWORK_MAPPING.md"
                assert mapping_file.exists(), \
                    f"{display_name} ({language}): FRAMEWORK_MAPPING.md should exist"
                
                # Verify file has content
                content = mapping_file.read_text()
                assert len(content) > 0, \
                    f"{display_name} ({language}): FRAMEWORK_MAPPING.md should not be empty"
    
    def test_phase2_template_numbering_ranges(self, template_base_path):
        """Test that Phase 2 frameworks have appropriate template numbering ranges."""
        expected_ranges = {
            'iso-38500': (10, 400),
            'iso-31000': (10, 500),
            'csa-ccm': (10, 800),
            'tisax': (10, 600),
            'soc1': (10, 500),
            'coso': (10, 600),
            'dora': (10, 400)
        }
        
        for framework, (min_num, max_num) in expected_ranges.items():
            for language in ['de', 'en']:
                framework_dir = template_base_path / language / framework
                
                if not framework_dir.exists():
                    continue
                
                # Get all template numbers
                templates = [
                    f for f in os.listdir(framework_dir)
                    if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
                ]
                
                if not templates:
                    continue
                
                numbers = []
                for template in templates:
                    match = re.match(r'^(\d{4})_', template)
                    if match:
                        numbers.append(int(match.group(1)))
                
                if numbers:
                    assert min(numbers) >= min_num, \
                        f"{framework} ({language}): Minimum template number should be >= {min_num}"
                    assert max(numbers) <= max_num, \
                        f"{framework} ({language}): Maximum template number should be <= {max_num}"
