"""
Tests for Template Manager

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings, strategies as st
import tempfile
import shutil

from src.template_manager import Template, TemplateManager


# Hypothesis strategies for generating test data
@st.composite
def template_structure(draw):
    """
    Generate a valid template directory structure.
    
    Returns a dictionary with:
    - languages: list of language codes
    - categories: list of category names
    - templates: dict mapping (lang, category) to list of template filenames
    """
    languages = draw(st.lists(
        st.sampled_from(['de', 'en', 'fr', 'es']),
        min_size=1,
        max_size=3,
        unique=True
    ))
    
    categories = draw(st.lists(
        st.sampled_from(['backup', 'bcm', 'isms', 'it-operation', 'security']),
        min_size=1,
        max_size=4,
        unique=True
    ))
    
    templates = {}
    for lang in languages:
        for category in categories:
            # Generate template filenames
            num_templates = draw(st.integers(min_value=1, max_value=5))
            template_files = []
            
            # Add metadata template
            template_files.append(f'0000_metadata_{lang}_{category}.md')
            
            # Add content templates
            for i in range(num_templates):
                sort_num = (i + 1) * 100
                name = draw(st.text(
                    alphabet=st.characters(whitelist_categories=('Ll', 'Nd'), whitelist_characters='_-'),
                    min_size=3,
                    max_size=15
                ))
                template_files.append(f'{sort_num:04d}_{name}.md')
            
            templates[(lang, category)] = template_files
    
    return {
        'languages': languages,
        'categories': categories,
        'templates': templates
    }


def create_template_structure(base_dir: Path, structure: dict):
    """
    Create a template directory structure on disk.
    
    Args:
        base_dir: Base directory for templates
        structure: Structure dictionary from template_structure strategy
    """
    for (lang, category), template_files in structure['templates'].items():
        category_dir = base_dir / lang / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        for template_file in template_files:
            template_path = category_dir / template_file
            template_path.write_text(f'# Template: {template_file}\n\nContent here.')


class TestTemplateDataModel:
    """Unit tests for Template data model."""
    
    def test_template_creation(self):
        """Test creating a Template instance."""
        template = Template(
            path=Path('templates/de/backup/0100_intro.md'),
            template_type='content',
            sort_order=100,
            language='de',
            category='backup'
        )
        
        assert template.path == Path('templates/de/backup/0100_intro.md')
        assert template.template_type == 'content'
        assert template.sort_order == 100
        assert template.language == 'de'
        assert template.category == 'backup'
    
    def test_is_metadata(self):
        """Test is_metadata method."""
        metadata_template = Template(
            path=Path('templates/de/backup/0000_metadata_de_backup.md'),
            template_type='metadata',
            sort_order=0,
            language='de',
            category='backup'
        )
        
        content_template = Template(
            path=Path('templates/de/backup/0100_intro.md'),
            template_type='content',
            sort_order=100,
            language='de',
            category='backup'
        )
        
        assert metadata_template.is_metadata() is True
        assert content_template.is_metadata() is False
    
    def test_read_content(self, tmp_path):
        """Test reading template content."""
        template_file = tmp_path / 'test.md'
        template_file.write_text('# Test Content\n\nThis is a test.')
        
        template = Template(
            path=template_file,
            template_type='content',
            sort_order=100,
            language='de',
            category='backup'
        )
        
        content = template.read_content()
        assert content == '# Test Content\n\nThis is a test.'


class TestTemplateDiscovery:
    """Tests for template discovery functionality."""
    
    @settings(max_examples=100)
    @given(structure=template_structure())
    def test_property_1_template_discovery_completeness(self, structure):
        """
        Feature: handbook-generator, Property 1: Template Discovery Completeness
        
        For any valid template directory structure with templates in multiple languages
        and types, the template scanner should discover all templates and correctly
        categorize them by language and type.
        
        Validates: Requirements 1.1, 1.2, 1.3, 1.5
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = Path(tmpdir) / 'templates'
            base_dir.mkdir()
            
            # Create the template structure
            create_template_structure(base_dir, structure)
            
            # Initialize TemplateManager
            manager = TemplateManager(base_dir)
            
            # Discover templates
            discovered = manager.discover_templates()
            
            # Verify all languages are discovered
            for lang in structure['languages']:
                assert lang in discovered, f"Language {lang} not discovered"
            
            # Verify all categories are discovered for each language
            for lang in structure['languages']:
                for category in structure['categories']:
                    if (lang, category) in structure['templates']:
                        assert category in discovered[lang], \
                            f"Category {category} not discovered for language {lang}"
            
            # Verify all template files are discovered
            for (lang, category), template_files in structure['templates'].items():
                discovered_paths = discovered[lang][category]
                discovered_names = {p.name for p in discovered_paths}
                expected_names = set(template_files)
                
                assert discovered_names == expected_names, \
                    f"Template files mismatch for {lang}/{category}: " \
                    f"expected {expected_names}, got {discovered_names}"
            
            # Verify template count matches
            for (lang, category), template_files in structure['templates'].items():
                discovered_count = len(discovered[lang][category])
                expected_count = len(template_files)
                
                assert discovered_count == expected_count, \
                    f"Template count mismatch for {lang}/{category}: " \
                    f"expected {expected_count}, got {discovered_count}"
    
    def test_empty_template_directory(self, tmp_path):
        """Test discovery with empty template directory."""
        manager = TemplateManager(tmp_path)
        discovered = manager.discover_templates()
        
        assert discovered == {}
    
    def test_nonexistent_template_directory(self, tmp_path):
        """Test discovery with non-existent directory."""
        non_existent = tmp_path / 'does_not_exist'
        manager = TemplateManager(non_existent)
        discovered = manager.discover_templates()
        
        assert discovered == {}
    
    def test_examples_directory_excluded(self, tmp_path):
        """Test that examples directory is excluded from discovery."""
        # Create templates directory with examples
        templates_dir = tmp_path / 'templates'
        templates_dir.mkdir()
        
        # Create regular language directory
        (templates_dir / 'de' / 'backup').mkdir(parents=True)
        (templates_dir / 'de' / 'backup' / '0100_test.md').write_text('content')
        
        # Create examples directory
        (templates_dir / 'examples' / 'backup').mkdir(parents=True)
        (templates_dir / 'examples' / 'backup' / '0100_example.md').write_text('example')
        
        manager = TemplateManager(templates_dir)
        discovered = manager.discover_templates()
        
        # Verify examples is not in discovered languages
        assert 'examples' not in discovered
        assert 'de' in discovered


class TestTemplateRetrieval:
    """Tests for template retrieval and sorting."""
    
    def test_get_templates_basic(self, tmp_path):
        """Test basic template retrieval."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'backup').mkdir(parents=True)
        
        # Create templates
        (templates_dir / 'de' / 'backup' / '0000_metadata_de_backup.md').write_text('metadata')
        (templates_dir / 'de' / 'backup' / '0100_intro.md').write_text('intro')
        (templates_dir / 'de' / 'backup' / '0200_strategy.md').write_text('strategy')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'backup')
        
        assert len(templates) == 3
        assert templates[0].is_metadata()
        assert templates[0].sort_order == 0
        assert templates[1].sort_order == 100
        assert templates[2].sort_order == 200
    
    def test_get_templates_nonexistent_language(self, tmp_path):
        """Test retrieval with non-existent language."""
        manager = TemplateManager(tmp_path)
        templates = manager.get_templates('xx', 'backup')
        
        assert templates == []
    
    def test_get_templates_nonexistent_category(self, tmp_path):
        """Test retrieval with non-existent category."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de').mkdir(parents=True)
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'nonexistent')
        
        assert templates == []


class TestTemplateSorting:
    """Tests for template sorting functionality."""
    
    @settings(max_examples=100)
    @given(
        num_content_templates=st.integers(min_value=1, max_value=10),
        has_metadata=st.booleans()
    )
    def test_property_11_template_sorting_and_assembly(self, num_content_templates, has_metadata):
        """
        Feature: handbook-generator, Property 11: Template Sorting and Assembly
        
        For any set of content templates with 4-digit sort numbers and metadata templates,
        the system should process them in the correct order: metadata first (0000),
        then content templates in ascending numerical order.
        
        Validates: Requirements 6.1, 6.2, 6.4, 6.5
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            (templates_dir / 'de' / 'backup').mkdir(parents=True)
            
            # Generate random sort numbers (not necessarily sequential)
            sort_numbers = sorted([100 * (i + 1) for i in range(num_content_templates)])
            
            # Shuffle to create templates in random order on disk
            import random
            shuffled_numbers = sort_numbers.copy()
            random.shuffle(shuffled_numbers)
            
            # Create metadata template if requested
            if has_metadata:
                (templates_dir / 'de' / 'backup' / '0000_metadata_de_backup.md').write_text('metadata')
            
            # Create content templates with shuffled order
            for sort_num in shuffled_numbers:
                filename = f'{sort_num:04d}_content.md'
                (templates_dir / 'de' / 'backup' / filename).write_text(f'content {sort_num}')
            
            # Get templates through TemplateManager
            manager = TemplateManager(templates_dir)
            templates = manager.get_templates('de', 'backup')
            
            # Verify correct number of templates
            expected_count = num_content_templates + (1 if has_metadata else 0)
            assert len(templates) == expected_count
            
            # Verify metadata comes first if present
            if has_metadata:
                assert templates[0].is_metadata()
                assert templates[0].sort_order == 0
                content_start_idx = 1
            else:
                content_start_idx = 0
            
            # Verify content templates are sorted in ascending order
            content_templates = templates[content_start_idx:]
            for i in range(len(content_templates) - 1):
                assert content_templates[i].sort_order < content_templates[i + 1].sort_order, \
                    f"Templates not sorted: {content_templates[i].sort_order} >= {content_templates[i + 1].sort_order}"
            
            # Verify sort orders match expected numbers
            actual_sort_orders = [t.sort_order for t in content_templates]
            assert actual_sort_orders == sort_numbers
    
    @settings(max_examples=100)
    @given(
        num_numbered_templates=st.integers(min_value=0, max_value=5),
        num_unnumbered_templates=st.integers(min_value=1, max_value=3)
    )
    def test_property_12_unnumbered_template_handling(self, num_numbered_templates, num_unnumbered_templates):
        """
        Feature: handbook-generator, Property 12: Unnumbered Template Handling
        
        For any template without a leading 4-digit number, the system should generate
        a warning and place the template at the end of the processing order.
        
        Validates: Requirements 6.3
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            (templates_dir / 'de' / 'backup').mkdir(parents=True)
            
            # Create numbered templates
            numbered_sort_orders = []
            for i in range(num_numbered_templates):
                sort_num = (i + 1) * 100
                numbered_sort_orders.append(sort_num)
                filename = f'{sort_num:04d}_content.md'
                (templates_dir / 'de' / 'backup' / filename).write_text(f'content {sort_num}')
            
            # Create unnumbered templates
            unnumbered_names = []
            for i in range(num_unnumbered_templates):
                filename = f'unnumbered_{i}.md'
                unnumbered_names.append(filename)
                (templates_dir / 'de' / 'backup' / filename).write_text(f'unnumbered content {i}')
            
            # Get templates through TemplateManager
            manager = TemplateManager(templates_dir)
            templates = manager.get_templates('de', 'backup')
            
            # Verify correct total count
            expected_count = num_numbered_templates + num_unnumbered_templates
            assert len(templates) == expected_count
            
            # Verify numbered templates come before unnumbered ones
            if num_numbered_templates > 0:
                # All numbered templates should have sort_order < 9999
                for i in range(num_numbered_templates):
                    assert templates[i].sort_order < 9999, \
                        f"Numbered template has wrong sort order: {templates[i].sort_order}"
            
            # Verify unnumbered templates are at the end with sort_order 9999
            unnumbered_start_idx = num_numbered_templates
            for i in range(unnumbered_start_idx, len(templates)):
                assert templates[i].sort_order == 9999, \
                    f"Unnumbered template should have sort_order 9999, got {templates[i].sort_order}"
            
            # Verify warnings are generated for unnumbered templates
            warnings = manager.validate_template_structure()
            unnumbered_warnings = [w for w in warnings if 'without proper numbering' in w.lower()]
            assert len(unnumbered_warnings) == num_unnumbered_templates, \
                f"Expected {num_unnumbered_templates} warnings, got {len(unnumbered_warnings)}"


class TestMetadataTemplates:
    """Tests for metadata template handling."""
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en', 'fr', 'es', 'it']),
        template_name=st.text(
            alphabet=st.characters(whitelist_categories=('Ll', 'Nd'), whitelist_characters='_-'),
            min_size=3,
            max_size=20
        ),
        is_valid_metadata=st.booleans()
    )
    def test_property_13_metadata_template_format_validation(self, language, template_name, is_valid_metadata):
        """
        Feature: handbook-generator, Property 13: Metadata Template Format Validation
        
        For any filename, if it matches the pattern "0000_metadata_[language]_[templatename].md",
        it should be recognized as a metadata template; otherwise, it should not.
        
        Validates: Requirements 7.1
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            (templates_dir / language / 'backup').mkdir(parents=True)
            
            if is_valid_metadata:
                # Create valid metadata template
                filename = f'0000_metadata_{language}_{template_name}.md'
            else:
                # Create invalid metadata template (missing parts or wrong format)
                import random
                invalid_formats = [
                    f'0001_metadata_{language}_{template_name}.md',  # Wrong number
                    f'metadata_{language}_{template_name}.md',  # Missing number
                    f'0000_{language}_{template_name}.md',  # Missing 'metadata'
                    f'0000_metadata_{template_name}.md',  # Missing language
                    f'{template_name}.md',  # Just name
                ]
                filename = random.choice(invalid_formats)
            
            template_path = templates_dir / language / 'backup' / filename
            template_path.write_text('# Metadata\n\nContent here.')
            
            # Get templates through TemplateManager
            manager = TemplateManager(templates_dir)
            templates = manager.get_templates(language, 'backup')
            
            assert len(templates) == 1
            template = templates[0]
            
            # Verify metadata recognition
            if is_valid_metadata:
                assert template.is_metadata(), \
                    f"Valid metadata template not recognized: {filename}"
                assert template.template_type == 'metadata'
                assert template.sort_order == 0
            else:
                assert not template.is_metadata(), \
                    f"Invalid metadata template incorrectly recognized: {filename}"
                assert template.template_type == 'content'


class TestTemplateValidation:
    """Tests for template validation."""
    
    def test_validate_structure_missing_directory(self, tmp_path):
        """Test validation with missing template directory."""
        non_existent = tmp_path / 'does_not_exist'
        manager = TemplateManager(non_existent)
        warnings = manager.validate_template_structure()
        
        assert len(warnings) > 0
        assert 'not found' in warnings[0].lower()
    
    def test_validate_structure_empty_directory(self, tmp_path):
        """Test validation with empty template directory."""
        manager = TemplateManager(tmp_path)
        warnings = manager.validate_template_structure()
        
        assert len(warnings) > 0
        assert 'no templates found' in warnings[0].lower()
    
    def test_validate_structure_unnumbered_template(self, tmp_path):
        """Test validation with unnumbered template."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'backup').mkdir(parents=True)
        
        # Create template without proper numbering
        (templates_dir / 'de' / 'backup' / 'invalid_name.md').write_text('content')
        
        manager = TemplateManager(templates_dir)
        warnings = manager.validate_template_structure()
        
        assert len(warnings) > 0
        assert 'without proper numbering' in warnings[0].lower()


class TestExampleTemplates:
    """Tests for example template handling."""
    
    @settings(max_examples=100)
    @given(
        num_regular_languages=st.integers(min_value=1, max_value=3),
        num_example_categories=st.integers(min_value=1, max_value=5),
        num_templates_per_category=st.integers(min_value=1, max_value=4)
    )
    def test_property_24_example_template_separation(
        self, 
        num_regular_languages, 
        num_example_categories, 
        num_templates_per_category
    ):
        """
        Feature: handbook-generator, Property 24: Example Template Separation
        
        For any template directory structure containing an "examples" subdirectory,
        templates in the examples directory should be categorized separately from
        regular templates.
        
        Validates: Requirements 13.2
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            templates_dir.mkdir()
            
            # Create regular language directories
            languages = ['de', 'en', 'fr'][:num_regular_languages]
            for lang in languages:
                (templates_dir / lang / 'backup').mkdir(parents=True)
                (templates_dir / lang / 'backup' / '0100_test.md').write_text(f'content {lang}')
            
            # Create examples directory with categories
            example_categories = [
                'backup', 'ISO 27001', 'ISO 9001', 'BSI Grundschutz', 'bcm'
            ][:num_example_categories]
            
            for category in example_categories:
                category_dir = templates_dir / 'examples' / category
                category_dir.mkdir(parents=True)
                
                # Create templates in example category
                for i in range(num_templates_per_category):
                    template_file = category_dir / f'0{(i+1)*100:03d}_example.md'
                    template_file.write_text(f'example content {i}')
            
            # Initialize TemplateManager
            manager = TemplateManager(templates_dir)
            
            # Discover regular templates (should exclude examples)
            regular_templates = manager.discover_templates(include_examples=False)
            
            # Verify examples directory is NOT in regular templates
            assert 'examples' not in regular_templates, \
                "Examples directory should not be in regular template discovery"
            
            # Verify all regular languages are present
            for lang in languages:
                assert lang in regular_templates, \
                    f"Regular language {lang} should be discovered"
            
            # Discover examples separately
            examples = manager.discover_examples()
            
            # Verify all example categories are discovered
            for category in example_categories:
                assert category in examples, \
                    f"Example category {category} should be discovered"
            
            # Verify correct number of templates in each example category
            for category in example_categories:
                assert len(examples[category]) == num_templates_per_category, \
                    f"Expected {num_templates_per_category} templates in {category}, " \
                    f"got {len(examples[category])}"
            
            # Verify examples and regular templates are completely separate
            regular_keys = set(regular_templates.keys())
            example_keys = set(examples.keys())
            
            # No overlap between regular language codes and example categories
            # (though they might share category names like 'backup')
            assert 'examples' not in regular_keys, \
                "Examples should not appear as a language in regular templates"
    
    @settings(max_examples=100)
    @given(
        num_example_templates=st.integers(min_value=1, max_value=5),
        has_metadata=st.booleans()
    )
    def test_property_25_example_template_processing_consistency(
        self, 
        num_example_templates, 
        has_metadata
    ):
        """
        Feature: handbook-generator, Property 25: Example Template Processing Consistency
        
        For any example template, when processed, it should follow the same placeholder
        replacement and validation rules as regular templates.
        
        Validates: Requirements 13.5
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            examples_dir = templates_dir / 'examples' / 'backup'
            examples_dir.mkdir(parents=True)
            
            # Create example templates with same structure as regular templates
            if has_metadata:
                metadata_file = examples_dir / '0000_metadata_en_backup.md'
                metadata_file.write_text('# Metadata\n\nAuthor: Test')
            
            # Create content templates
            for i in range(num_example_templates):
                sort_num = (i + 1) * 100
                template_file = examples_dir / f'{sort_num:04d}_example.md'
                template_file.write_text(f'# Example {i}\n\nContent here.')
            
            # Initialize TemplateManager
            manager = TemplateManager(templates_dir)
            
            # Discover examples
            examples = manager.discover_examples()
            
            # Verify examples are discovered
            assert 'backup' in examples
            
            # Get example template paths
            example_paths = examples['backup']
            
            # Parse each example template using the same parsing logic
            parsed_templates = []
            for path in example_paths:
                # Use the internal parsing method (same as for regular templates)
                template = manager._parse_template(path, 'examples', 'backup')
                parsed_templates.append(template)
            
            # Verify all templates were parsed successfully
            assert len(parsed_templates) == len(example_paths)
            assert all(t is not None for t in parsed_templates)
            
            # Verify metadata template is recognized if present
            if has_metadata:
                metadata_templates = [t for t in parsed_templates if t.is_metadata()]
                assert len(metadata_templates) == 1, \
                    "Metadata template should be recognized in examples"
                assert metadata_templates[0].sort_order == 0
            
            # Verify content templates are properly sorted
            content_templates = [t for t in parsed_templates if not t.is_metadata()]
            assert len(content_templates) == num_example_templates
            
            # Sort templates (same logic as regular templates)
            parsed_templates.sort(key=lambda t: t.sort_order)
            
            # Verify sorting works correctly
            if has_metadata:
                assert parsed_templates[0].is_metadata(), \
                    "Metadata should be first after sorting"
            
            # Verify content templates are in ascending order
            content_start = 1 if has_metadata else 0
            for i in range(content_start, len(parsed_templates) - 1):
                assert parsed_templates[i].sort_order <= parsed_templates[i + 1].sort_order, \
                    "Example templates should be sorted in ascending order"
    
    def test_discover_examples_empty(self, tmp_path):
        """Test discovering examples when examples directory doesn't exist."""
        manager = TemplateManager(tmp_path)
        examples = manager.discover_examples()
        
        assert examples == {}
    
    def test_discover_examples_with_content(self, tmp_path):
        """Test discovering examples with actual content."""
        templates_dir = tmp_path / 'templates'
        examples_dir = templates_dir / 'examples'
        
        # Create example categories
        (examples_dir / 'ISO 27001').mkdir(parents=True)
        (examples_dir / 'ISO 27001' / '0100_intro.md').write_text('ISO intro')
        
        (examples_dir / 'BSI Grundschutz').mkdir(parents=True)
        (examples_dir / 'BSI Grundschutz' / '0100_intro.md').write_text('BSI intro')
        
        manager = TemplateManager(templates_dir)
        examples = manager.discover_examples()
        
        assert 'ISO 27001' in examples
        assert 'BSI Grundschutz' in examples
        assert len(examples['ISO 27001']) == 1
        assert len(examples['BSI Grundschutz']) == 1
