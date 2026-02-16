"""
Property-based tests for Template Manager integration with new frameworks.

Tests for IDW PS 951, NIST CSF 2.0, and TOGAF framework support.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import tempfile

from src.template_manager import TemplateManager


# Hypothesis strategies for new frameworks
@st.composite
def new_framework_structure(draw):
    """
    Generate a valid template directory structure for new frameworks.
    
    Returns a dictionary with:
    - framework: framework identifier (Phase 1 + Phase 2)
    - languages: list of language codes
    - templates: dict mapping language to list of template filenames
    """
    # Include both Phase 1 and Phase 2 frameworks
    framework = draw(st.sampled_from([
        'idw-ps-951', 'nist-csf', 'togaf',  # Phase 1
        'iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora'  # Phase 2
    ]))
    
    languages = draw(st.lists(
        st.sampled_from(['de', 'en']),
        min_size=1,
        max_size=2,
        unique=True
    ))
    
    # Determine minimum template count based on framework
    min_counts = {
        'idw-ps-951': 50,  # 0010-0500
        'nist-csf': 60,    # 0010-0600
        'togaf': 70,       # 0010-0700
        'iso-38500': 40,   # 0010-0400
        'iso-31000': 50,   # 0010-0500
        'csa-ccm': 80,     # 0010-0800
        'tisax': 60,       # 0010-0600
        'soc1': 50,        # 0010-0500
        'coso': 60,        # 0010-0600
        'dora': 40         # 0010-0400
    }
    min_count = min_counts[framework]
    
    templates = {}
    for lang in languages:
        template_files = []
        
        # Add metadata template
        template_files.append(f'0000_metadata_{lang}_{framework}.md')
        
        # Add content templates (at least minimum required)
        num_templates = draw(st.integers(min_value=min_count // 10, max_value=min_count // 10 + 5))
        for i in range(num_templates):
            sort_num = (i + 1) * 10
            name = draw(st.text(
                alphabet=st.characters(whitelist_categories=('Ll', 'Nd'), whitelist_characters='_-'),
                min_size=3,
                max_size=15
            ))
            template_files.append(f'{sort_num:04d}_{name}.md')
        
        templates[lang] = template_files
    
    return {
        'framework': framework,
        'languages': languages,
        'templates': templates
    }


def create_framework_structure(base_dir: Path, structure: dict):
    """
    Create a framework directory structure on disk.
    
    Args:
        base_dir: Base directory for templates
        structure: Structure dictionary from new_framework_structure strategy
    """
    framework = structure['framework']
    
    for lang, template_files in structure['templates'].items():
        framework_dir = base_dir / lang / framework
        framework_dir.mkdir(parents=True, exist_ok=True)
        
        # Create diagrams directory
        (framework_dir / 'diagrams').mkdir(exist_ok=True)
        
        # Create required documentation files (but not as .md to avoid discovery)
        (framework_dir / 'README.md').write_text(f'# {framework} Templates\n\nDocumentation here.')
        (framework_dir / '9999_Framework_Mapping.md').write_text(f'# Framework Mapping\n\nMapping here.')
        
        # Create template files
        for template_file in template_files:
            template_path = framework_dir / template_file
            
            # Add metadata frontmatter for metadata templates
            if template_file.startswith('0000_metadata'):
                content = f'''---
title: "{framework} Handbook"
author: "Test Author"
version: "1.0"
date: "2026-01-01"
organization: "Test Organization"
classification: "Internal"
---

# Metadata

This file contains metadata for the {framework} handbook.
'''
            else:
                content = f'# Template: {template_file}\n\nContent here.'
            
            template_path.write_text(content)


class TestProperty8TemplateDiscovery:
    """
    Property 8: Template Discovery
    
    For any new framework directory added to templates/de/ or templates/en/,
    the Template_Manager must automatically discover and load it.
    
    Validates: Requirements 6.1
    """
    
    @settings(max_examples=100)
    @given(structure=new_framework_structure())
    def test_property_8_template_discovery(self, structure):
        """
        Feature: additional-compliance-frameworks, Property 8: Template Discovery
        
        For any new framework directory (idw-ps-951, nist-csf, togaf) added to
        templates/de/ or templates/en/, the Template_Manager must automatically
        discover and load it without requiring updates to configuration.
        
        Validates: Requirements 6.1
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir) / 'templates'
            base_dir.mkdir()
            
            # Create the framework structure
            create_framework_structure(base_dir, structure)
            
            # Initialize TemplateManager
            manager = TemplateManager(base_dir)
            
            # Discover frameworks
            discovered_frameworks = manager.get_discovered_frameworks()
            
            # Verify framework is discovered
            framework = structure['framework']
            assert framework in discovered_frameworks, \
                f"Framework {framework} not discovered"
            
            # Discover all templates
            discovered = manager.discover_templates()
            
            # Verify all languages are discovered
            for lang in structure['languages']:
                assert lang in discovered, \
                    f"Language {lang} not discovered for framework {framework}"
                
                # Verify framework is in language templates
                assert framework in discovered[lang], \
                    f"Framework {framework} not discovered in language {lang}"
                
                # Verify all template files are discovered
                discovered_paths = discovered[lang][framework]
                discovered_names = {p.name for p in discovered_paths}
                expected_names = set(structure['templates'][lang])
                
                # Verify all expected templates are present (may have additional files like README.md)
                assert expected_names.issubset(discovered_names), \
                    f"Template files missing for {lang}/{framework}: " \
                    f"expected {expected_names}, got {discovered_names}"


class TestProperty9TemplateSortingByNumericPrefix:
    """
    Property 9: Template Sorting by Numeric Prefix
    
    For any set of loaded templates from a framework, the Template_Manager
    must sort them in ascending order by their numeric prefix.
    
    Validates: Requirements 6.3
    """
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from([
            'idw-ps-951', 'nist-csf', 'togaf',  # Phase 1
            'iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora'  # Phase 2
        ]),
        language=st.sampled_from(['de', 'en']),
        num_templates=st.integers(min_value=3, max_value=15)
    )
    def test_property_9_template_sorting_by_numeric_prefix(self, framework, language, num_templates):
        """
        Feature: additional-compliance-frameworks, Property 9: Template Sorting by Numeric Prefix
        
        For any set of templates from a new framework, the Template_Manager must
        sort them in ascending order by their numeric prefix, with metadata (0000)
        first, followed by content templates in numerical order.
        
        Validates: Requirements 6.3
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir) / 'templates'
            framework_dir = base_dir / language / framework
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create metadata template
            metadata_file = framework_dir / f'0000_metadata_{language}_{framework}.md'
            metadata_file.write_text(f'# Metadata for {framework}')
            
            # Generate random sort numbers (not necessarily sequential)
            import random
            sort_numbers = sorted([random.randint(1, 99) * 10 for _ in range(num_templates)])
            
            # Shuffle to create templates in random order on disk
            shuffled_numbers = sort_numbers.copy()
            random.shuffle(shuffled_numbers)
            
            # Create content templates with shuffled order
            for sort_num in shuffled_numbers:
                filename = f'{sort_num:04d}_content.md'
                (framework_dir / filename).write_text(f'# Content {sort_num}')
            
            # Get templates through TemplateManager
            manager = TemplateManager(base_dir)
            templates = manager.get_templates(language, framework)
            
            # Verify correct number of templates (metadata + content)
            assert len(templates) == num_templates + 1
            
            # Verify metadata comes first
            assert templates[0].is_metadata()
            assert templates[0].sort_order == 0
            
            # Verify content templates are sorted in ascending order
            content_templates = templates[1:]
            for i in range(len(content_templates) - 1):
                assert content_templates[i].sort_order <= content_templates[i + 1].sort_order, \
                    f"Templates not sorted: {content_templates[i].sort_order} > {content_templates[i + 1].sort_order}"
            
            # Verify sort orders match expected numbers
            actual_sort_orders = [t.sort_order for t in content_templates]
            assert actual_sort_orders == sort_numbers
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from([
            'idw-ps-951', 'nist-csf', 'togaf',  # Phase 1
            'iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora'  # Phase 2
        ]),
        language=st.sampled_from(['de', 'en']),
        num_duplicates=st.integers(min_value=1, max_value=3)
    )
    def test_property_9_duplicate_sort_numbers_handling(self, framework, language, num_duplicates):
        """
        Feature: additional-compliance-frameworks, Property 9: Template Sorting by Numeric Prefix
        
        For any templates with duplicate sort numbers, the Template_Manager must
        handle them gracefully by using filename as secondary sort key.
        
        Validates: Requirements 6.3
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir) / 'templates'
            framework_dir = base_dir / language / framework
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create templates with duplicate sort numbers
            sort_num = 100
            filenames = []
            for i in range(num_duplicates):
                filename = f'{sort_num:04d}_content_{chr(97 + i)}.md'  # a, b, c, etc.
                filenames.append(filename)
                (framework_dir / filename).write_text(f'# Content {i}')
            
            # Get templates through TemplateManager
            manager = TemplateManager(base_dir)
            templates = manager.get_templates(language, framework)
            
            # Verify all templates are loaded
            assert len(templates) == num_duplicates
            
            # Verify all have same sort order
            for template in templates:
                assert template.sort_order == sort_num
            
            # Verify secondary sort by filename works
            template_names = [t.path.name for t in templates]
            assert template_names == sorted(filenames)


class TestProperty10MetadataExtraction:
    """
    Property 10: Metadata Extraction
    
    For any metadata template file (0000_metadata_*.md), the Template_Manager
    must successfully extract all metadata fields.
    
    Validates: Requirements 6.4
    """
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from([
            'idw-ps-951', 'nist-csf', 'togaf',  # Phase 1
            'iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora'  # Phase 2
        ]),
        language=st.sampled_from(['de', 'en']),
        title=st.text(
            alphabet=st.characters(blacklist_characters='\r\n"\'\\'),
            min_size=5,
            max_size=50
        ),
        author=st.text(
            alphabet=st.characters(blacklist_characters='\r\n"\'\\'),
            min_size=3,
            max_size=30
        ),
        version=st.text(
            alphabet=st.characters(blacklist_characters='\r\n"\'\\'),
            min_size=3,
            max_size=10
        ),
        organization=st.text(
            alphabet=st.characters(blacklist_characters='\r\n"\'\\'),
            min_size=3,
            max_size=40
        )
    )
    def test_property_10_metadata_extraction(self, framework, language, title, author, version, organization):
        """
        Feature: additional-compliance-frameworks, Property 10: Metadata Extraction
        
        For any metadata template file (0000_metadata_*.md) for new frameworks,
        the Template_Manager must successfully extract all required metadata fields:
        title, author, version, date, organization, classification.
        
        Validates: Requirements 6.4
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir) / 'templates'
            framework_dir = base_dir / language / framework
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create metadata template with frontmatter
            metadata_file = framework_dir / f'0000_metadata_{language}_{framework}.md'
            metadata_content = f'''---
title: "{title}"
author: "{author}"
version: "{version}"
date: "2026-01-15"
organization: "{organization}"
classification: "Internal"
---

# Metadata

This file contains metadata for the {framework} handbook.
'''
            metadata_file.write_text(metadata_content)
            
            # Initialize TemplateManager
            manager = TemplateManager(base_dir)
            
            # Extract metadata
            metadata = manager.extract_metadata(language, framework)
            
            # Verify all required fields are present
            required_fields = ['title', 'author', 'version', 'date', 'organization', 'classification']
            for field in required_fields:
                assert field in metadata, f"Required field '{field}' not in metadata"
            
            # Verify extracted values match input
            assert metadata['title'] == title
            assert metadata['author'] == author
            assert metadata['version'] == version
            assert metadata['date'] == '2026-01-15'
            assert metadata['organization'] == organization
            assert metadata['classification'] == 'Internal'
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from([
            'idw-ps-951', 'nist-csf', 'togaf',  # Phase 1
            'iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora'  # Phase 2
        ]),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_10_metadata_extraction_missing_template(self, framework, language):
        """
        Feature: additional-compliance-frameworks, Property 10: Metadata Extraction
        
        For any framework without a metadata template, the Template_Manager must
        raise a clear error indicating the missing metadata template.
        
        Validates: Requirements 6.4
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir) / 'templates'
            framework_dir = base_dir / language / framework
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Do NOT create metadata template
            
            # Initialize TemplateManager
            manager = TemplateManager(base_dir)
            
            # Attempt to extract metadata should raise error
            with pytest.raises(ValueError, match="Metadata template not found"):
                manager.extract_metadata(language, framework)
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from([
            'idw-ps-951', 'nist-csf', 'togaf',  # Phase 1
            'iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora'  # Phase 2
        ]),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_10_metadata_extraction_empty_frontmatter(self, framework, language):
        """
        Feature: additional-compliance-frameworks, Property 10: Metadata Extraction
        
        For any metadata template with empty or missing frontmatter, the Template_Manager
        must return empty strings for metadata fields rather than failing.
        
        Validates: Requirements 6.4
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir) / 'templates'
            framework_dir = base_dir / language / framework
            framework_dir.mkdir(parents=True, exist_ok=True)
            
            # Create metadata template without frontmatter
            metadata_file = framework_dir / f'0000_metadata_{language}_{framework}.md'
            metadata_content = f'# Metadata\n\nNo frontmatter here.'
            metadata_file.write_text(metadata_content)
            
            # Initialize TemplateManager
            manager = TemplateManager(base_dir)
            
            # Extract metadata
            metadata = manager.extract_metadata(language, framework)
            
            # Verify all required fields are present but empty
            required_fields = ['title', 'author', 'version', 'date', 'organization', 'classification']
            for field in required_fields:
                assert field in metadata, f"Required field '{field}' not in metadata"
                assert metadata[field] == '', f"Field '{field}' should be empty string"


class TestFrameworkConfiguration:
    """Tests for framework configuration functionality."""
    
    def test_get_framework_config_idw_ps_951(self):
        """Test getting configuration for IDW PS 951 framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('idw-ps-951')
        
        assert config is not None
        assert config['display_name'] == 'IDW PS 951'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 50
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_nist_csf(self):
        """Test getting configuration for NIST CSF 2.0 framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('nist-csf')
        
        assert config is not None
        assert config['display_name'] == 'NIST CSF 2.0'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 60
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_togaf(self):
        """Test getting configuration for TOGAF framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('togaf')
        
        assert config is not None
        assert config['display_name'] == 'TOGAF'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 70
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_iso_38500(self):
        """Test getting configuration for ISO/IEC 38500 framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('iso-38500')
        
        assert config is not None
        assert config['display_name'] == 'ISO/IEC 38500'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 40
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_iso_31000(self):
        """Test getting configuration for ISO 31000 framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('iso-31000')
        
        assert config is not None
        assert config['display_name'] == 'ISO 31000'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 50
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_csa_ccm(self):
        """Test getting configuration for CSA CCM framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('csa-ccm')
        
        assert config is not None
        assert config['display_name'] == 'CSA CCM'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 80
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_tisax(self):
        """Test getting configuration for TISAX framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('tisax')
        
        assert config is not None
        assert config['display_name'] == 'TISAX'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 60
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_soc1(self):
        """Test getting configuration for SOC 1 framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('soc1')
        
        assert config is not None
        assert config['display_name'] == 'SOC 1 / SSAE 18'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 50
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_coso(self):
        """Test getting configuration for COSO framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('coso')
        
        assert config is not None
        assert config['display_name'] == 'COSO'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 60
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_dora(self):
        """Test getting configuration for DORA framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('dora')
        
        assert config is not None
        assert config['display_name'] == 'DORA'
        assert 'de' in config['languages']
        assert 'en' in config['languages']
        assert config['min_template_count'] == 40
        assert config['has_diagrams'] is True
    
    def test_get_framework_config_unknown(self):
        """Test getting configuration for unknown framework."""
        manager = TemplateManager(Path('templates'))
        config = manager.get_framework_config('unknown-framework')
        
        assert config is None


class TestFrameworkValidation:
    """Tests for framework structure validation."""
    
    def test_validate_framework_structure_complete(self, tmp_path):
        """Test validation with complete framework structure."""
        templates_dir = tmp_path / 'templates'
        framework_dir = templates_dir / 'de' / 'idw-ps-951'
        framework_dir.mkdir(parents=True)
        
        # Create all required files
        (framework_dir / 'README.md').write_text('# README')
        (framework_dir / '9999_Framework_Mapping.md').write_text('# Mapping')
        (framework_dir / '0000_metadata_de_idw-ps-951.md').write_text('# Metadata')
        (framework_dir / 'diagrams').mkdir()
        
        # Create sufficient templates
        for i in range(50):
            (framework_dir / f'{(i+1)*10:04d}_template.md').write_text('content')
        
        manager = TemplateManager(templates_dir)
        messages = manager.validate_framework_structure('idw-ps-951', 'de')
        
        # Should have no validation errors
        assert len(messages) == 0
    
    def test_validate_framework_structure_missing_files(self, tmp_path):
        """Test validation with missing required files."""
        templates_dir = tmp_path / 'templates'
        framework_dir = templates_dir / 'de' / 'nist-csf'
        framework_dir.mkdir(parents=True)
        
        # Create only metadata template
        (framework_dir / '0000_metadata_de_nist-csf.md').write_text('# Metadata')
        
        manager = TemplateManager(templates_dir)
        messages = manager.validate_framework_structure('nist-csf', 'de')
        
        # Should have validation errors for missing files
        assert len(messages) > 0
        assert any('README.md' in msg for msg in messages)
        assert any('9999_Framework_Mapping.md' in msg for msg in messages)
        assert any('diagrams' in msg for msg in messages)
    
    def test_validate_framework_structure_insufficient_templates(self, tmp_path):
        """Test validation with insufficient template count."""
        templates_dir = tmp_path / 'templates'
        framework_dir = templates_dir / 'de' / 'togaf'
        framework_dir.mkdir(parents=True)
        
        # Create required files
        (framework_dir / 'README.md').write_text('# README')
        (framework_dir / '9999_Framework_Mapping.md').write_text('# Mapping')
        (framework_dir / '0000_metadata_de_togaf.md').write_text('# Metadata')
        (framework_dir / 'diagrams').mkdir()
        
        # Create only 10 templates (less than required 70)
        for i in range(10):
            (framework_dir / f'{(i+1)*10:04d}_template.md').write_text('content')
        
        manager = TemplateManager(templates_dir)
        messages = manager.validate_framework_structure('togaf', 'de')
        
        # Should have validation error for insufficient templates
        assert len(messages) > 0
        assert any('Insufficient templates' in msg for msg in messages)
