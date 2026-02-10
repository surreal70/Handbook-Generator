"""
Tests for Template Manager with new compliance frameworks

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import pytest
from pathlib import Path
import tempfile
from hypothesis import given, settings, strategies as st

from src.template_manager import Template, TemplateManager


class TestNewFrameworkSupport:
    """Tests for new compliance framework support."""
    
    def test_supported_frameworks_list(self):
        """Test that SUPPORTED_FRAMEWORKS includes all new frameworks."""
        expected_frameworks = [
            'pci-dss',
            'hipaa',
            'nist-800-53',
            'tsc',
            'common-criteria',
            'iso-9001',
            'gdpr'
        ]
        
        for framework in expected_frameworks:
            assert framework in TemplateManager.SUPPORTED_FRAMEWORKS, \
                f"Framework {framework} not in SUPPORTED_FRAMEWORKS"
    
    def test_load_pci_dss_templates(self, tmp_path):
        """Test loading PCI-DSS templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'pci-dss').mkdir(parents=True)
        
        # Create PCI-DSS templates
        (templates_dir / 'de' / 'pci-dss' / '0000_metadata_de_pci-dss.md').write_text('# PCI-DSS Metadata')
        (templates_dir / 'de' / 'pci-dss' / '0010_scope.md').write_text('# Scope')
        (templates_dir / 'de' / 'pci-dss' / '0100_firewall.md').write_text('# Firewall')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'pci-dss')
        
        assert len(templates) == 3
        assert templates[0].is_metadata()
        assert templates[0].category == 'pci-dss'
        assert templates[1].sort_order == 10
        assert templates[2].sort_order == 100
    
    def test_load_hipaa_templates(self, tmp_path):
        """Test loading HIPAA templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'en' / 'hipaa').mkdir(parents=True)
        
        # Create HIPAA templates
        (templates_dir / 'en' / 'hipaa' / '0000_metadata_en_hipaa.md').write_text('# HIPAA Metadata')
        (templates_dir / 'en' / 'hipaa' / '0010_scope.md').write_text('# Scope')
        (templates_dir / 'en' / 'hipaa' / '0100_security_management.md').write_text('# Security')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('en', 'hipaa')
        
        assert len(templates) == 3
        assert templates[0].is_metadata()
        assert templates[0].category == 'hipaa'
    
    def test_load_nist_800_53_templates(self, tmp_path):
        """Test loading NIST 800-53 templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'nist-800-53').mkdir(parents=True)
        
        # Create NIST templates
        (templates_dir / 'de' / 'nist-800-53' / '0000_metadata_de_nist-800-53.md').write_text('# NIST Metadata')
        (templates_dir / 'de' / 'nist-800-53' / '0010_categorization.md').write_text('# Categorization')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'nist-800-53')
        
        assert len(templates) == 2
        assert templates[0].is_metadata()
        assert templates[0].category == 'nist-800-53'
    
    def test_load_tsc_templates(self, tmp_path):
        """Test loading TSC templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'en' / 'tsc').mkdir(parents=True)
        
        # Create TSC templates
        (templates_dir / 'en' / 'tsc' / '0000_metadata_en_tsc.md').write_text('# TSC Metadata')
        (templates_dir / 'en' / 'tsc' / '0010_system_description.md').write_text('# System')
        (templates_dir / 'en' / 'tsc' / '0100_cc1.md').write_text('# CC1')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('en', 'tsc')
        
        assert len(templates) == 3
        assert templates[0].is_metadata()
        assert templates[0].category == 'tsc'
    
    def test_load_common_criteria_templates(self, tmp_path):
        """Test loading Common Criteria templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'common-criteria').mkdir(parents=True)
        
        # Create Common Criteria templates
        (templates_dir / 'de' / 'common-criteria' / '0000_metadata_de_common-criteria.md').write_text('# CC Metadata')
        (templates_dir / 'de' / 'common-criteria' / '0010_introduction.md').write_text('# Introduction')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'common-criteria')
        
        assert len(templates) == 2
        assert templates[0].is_metadata()
        assert templates[0].category == 'common-criteria'
    
    def test_load_iso_9001_templates(self, tmp_path):
        """Test loading ISO 9001 templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'en' / 'iso-9001').mkdir(parents=True)
        
        # Create ISO 9001 templates
        (templates_dir / 'en' / 'iso-9001' / '0000_metadata_en_iso-9001.md').write_text('# ISO Metadata')
        (templates_dir / 'en' / 'iso-9001' / '0010_context.md').write_text('# Context')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('en', 'iso-9001')
        
        assert len(templates) == 2
        assert templates[0].is_metadata()
        assert templates[0].category == 'iso-9001'
    
    def test_load_gdpr_templates(self, tmp_path):
        """Test loading GDPR templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'gdpr').mkdir(parents=True)
        
        # Create GDPR templates
        (templates_dir / 'de' / 'gdpr' / '0000_metadata_de_gdpr.md').write_text('# GDPR Metadata')
        (templates_dir / 'de' / 'gdpr' / '0010_scope.md').write_text('# Scope')
        (templates_dir / 'de' / 'gdpr' / '0020_roles.md').write_text('# Roles')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'gdpr')
        
        assert len(templates) == 3
        assert templates[0].is_metadata()
        assert templates[0].category == 'gdpr'


class TestTemplateSortingNewFrameworks:
    """Tests for template sorting with new frameworks."""
    
    def test_sorting_pci_dss_templates(self, tmp_path):
        """Test that PCI-DSS templates are sorted correctly."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'pci-dss').mkdir(parents=True)
        
        # Create templates in random order
        (templates_dir / 'de' / 'pci-dss' / '0500_logging.md').write_text('# Logging')
        (templates_dir / 'de' / 'pci-dss' / '0100_firewall.md').write_text('# Firewall')
        (templates_dir / 'de' / 'pci-dss' / '0000_metadata_de_pci-dss.md').write_text('# Metadata')
        (templates_dir / 'de' / 'pci-dss' / '0400_access.md').write_text('# Access')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'pci-dss')
        
        # Verify sorting: metadata first, then ascending order
        assert len(templates) == 4
        assert templates[0].sort_order == 0  # metadata
        assert templates[1].sort_order == 100
        assert templates[2].sort_order == 400
        assert templates[3].sort_order == 500
    
    def test_sorting_hipaa_templates(self, tmp_path):
        """Test that HIPAA templates are sorted correctly."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'en' / 'hipaa').mkdir(parents=True)
        
        # Create templates in random order
        (templates_dir / 'en' / 'hipaa' / '0400_access_control.md').write_text('# Access')
        (templates_dir / 'en' / 'hipaa' / '0000_metadata_en_hipaa.md').write_text('# Metadata')
        (templates_dir / 'en' / 'hipaa' / '0100_security.md').write_text('# Security')
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('en', 'hipaa')
        
        # Verify sorting
        assert len(templates) == 3
        assert templates[0].sort_order == 0  # metadata
        assert templates[1].sort_order == 100
        assert templates[2].sort_order == 400


class TestMetadataExtractionNewFrameworks:
    """Tests for metadata extraction from new frameworks."""
    
    def test_extract_metadata_pci_dss(self, tmp_path):
        """Test extracting metadata from PCI-DSS templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'de' / 'pci-dss').mkdir(parents=True)
        
        metadata_content = """# PCI-DSS Compliance Handbook
        
Author: Security Team
Version: 1.0
Framework: PCI-DSS v4.0
"""
        (templates_dir / 'de' / 'pci-dss' / '0000_metadata_de_pci-dss.md').write_text(metadata_content)
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('de', 'pci-dss')
        
        assert len(templates) == 1
        assert templates[0].is_metadata()
        
        content = templates[0].read_content()
        assert 'PCI-DSS Compliance Handbook' in content
        assert 'Framework: PCI-DSS v4.0' in content
    
    def test_extract_metadata_gdpr(self, tmp_path):
        """Test extracting metadata from GDPR templates."""
        templates_dir = tmp_path / 'templates'
        (templates_dir / 'en' / 'gdpr').mkdir(parents=True)
        
        metadata_content = """# GDPR Compliance Documentation
        
Author: Privacy Team
Version: 2.0
Framework: GDPR
"""
        (templates_dir / 'en' / 'gdpr' / '0000_metadata_en_gdpr.md').write_text(metadata_content)
        
        manager = TemplateManager(templates_dir)
        templates = manager.get_templates('en', 'gdpr')
        
        assert len(templates) == 1
        assert templates[0].is_metadata()
        
        content = templates[0].read_content()
        assert 'GDPR Compliance Documentation' in content
        assert 'Framework: GDPR' in content


class TestFrameworkDiscovery:
    """Tests for automatic framework discovery."""
    
    def test_discover_all_new_frameworks(self, tmp_path):
        """Test that all new frameworks are discovered automatically."""
        templates_dir = tmp_path / 'templates'
        
        # Create all new frameworks
        new_frameworks = ['pci-dss', 'hipaa', 'nist-800-53', 'tsc', 'common-criteria', 'iso-9001', 'gdpr']
        
        for framework in new_frameworks:
            (templates_dir / 'de' / framework).mkdir(parents=True)
            (templates_dir / 'de' / framework / '0100_test.md').write_text(f'# {framework}')
        
        manager = TemplateManager(templates_dir)
        discovered = manager.discover_templates()
        
        assert 'de' in discovered
        for framework in new_frameworks:
            assert framework in discovered['de'], f"Framework {framework} not discovered"
    
    def test_get_discovered_frameworks(self, tmp_path):
        """Test get_discovered_frameworks method."""
        templates_dir = tmp_path / 'templates'
        
        # Create frameworks in multiple languages
        frameworks = ['pci-dss', 'hipaa', 'gdpr']
        
        for lang in ['de', 'en']:
            for framework in frameworks:
                (templates_dir / lang / framework).mkdir(parents=True)
                (templates_dir / lang / framework / '0100_test.md').write_text(f'# {framework}')
        
        manager = TemplateManager(templates_dir)
        discovered_frameworks = manager.get_discovered_frameworks()
        
        assert len(discovered_frameworks) == 3
        for framework in frameworks:
            assert framework in discovered_frameworks



class TestPropertyBasedTests:
    """Property-based tests for template manager with new frameworks."""
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from([
            'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
            'common-criteria', 'iso-9001', 'gdpr'
        ]),
        language=st.sampled_from(['de', 'en']),
        num_templates=st.integers(min_value=1, max_value=10)
    )
    def test_property_14_template_sorting_by_number(self, framework, language, num_templates):
        """
        Feature: compliance-framework-templates, Property 14: Template Sorting by Number
        
        For any set of templates loaded by Template_Manager, the returned list
        should be sorted in ascending order by the numeric prefix in the filename.
        Metadata templates (0000_metadata_*) should always appear first.
        
        Validates: Requirements 10.3
        """
        from hypothesis import strategies as st
        
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            (templates_dir / language / framework).mkdir(parents=True)
            
            # Generate random sort numbers
            import random
            sort_numbers = sorted([random.randint(1, 99) * 100 for _ in range(num_templates)])
            
            # Create metadata template
            metadata_file = f'0000_metadata_{language}_{framework}.md'
            (templates_dir / language / framework / metadata_file).write_text('# Metadata')
            
            # Create content templates in random order
            shuffled_numbers = sort_numbers.copy()
            random.shuffle(shuffled_numbers)
            
            for sort_num in shuffled_numbers:
                filename = f'{sort_num:04d}_content.md'
                (templates_dir / language / framework / filename).write_text(f'# Content {sort_num}')
            
            # Load templates
            manager = TemplateManager(templates_dir)
            templates = manager.get_templates(language, framework)
            
            # Verify metadata comes first
            assert templates[0].is_metadata(), "Metadata template should be first"
            assert templates[0].sort_order == 0
            
            # Verify content templates are sorted in ascending order
            content_templates = templates[1:]
            for i in range(len(content_templates) - 1):
                assert content_templates[i].sort_order <= content_templates[i + 1].sort_order, \
                    f"Templates not sorted: {content_templates[i].sort_order} > {content_templates[i + 1].sort_order}"
            
            # Verify all expected sort numbers are present
            actual_sort_orders = [t.sort_order for t in content_templates]
            assert actual_sort_orders == sort_numbers, \
                f"Sort orders mismatch: expected {sort_numbers}, got {actual_sort_orders}"

    
    @settings(max_examples=100)
    @given(
        frameworks=st.lists(
            st.sampled_from([
                'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
                'common-criteria', 'iso-9001', 'gdpr',
                'bcm', 'isms', 'it-operation'
            ]),
            min_size=1,
            max_size=7,
            unique=True
        ),
        languages=st.lists(
            st.sampled_from(['de', 'en', 'fr', 'es']),
            min_size=1,
            max_size=3,
            unique=True
        )
    )
    def test_property_13_framework_discovery(self, frameworks, languages):
        """
        Feature: compliance-framework-templates, Property 13: Framework Discovery
        
        For any set of framework directories created in the templates directory,
        the Template_Manager should automatically discover all frameworks without
        requiring updates to a hardcoded list. The discovery should work across
        all language directories.
        
        Validates: Requirements 10.1
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = Path(tmpdir) / 'templates'
            templates_dir.mkdir()
            
            # Create framework directories for each language
            for lang in languages:
                for framework in frameworks:
                    framework_dir = templates_dir / lang / framework
                    framework_dir.mkdir(parents=True)
                    
                    # Create at least one template file
                    template_file = framework_dir / '0100_test.md'
                    template_file.write_text(f'# {framework} template for {lang}')
            
            # Initialize TemplateManager and discover templates
            manager = TemplateManager(templates_dir)
            discovered = manager.discover_templates()
            
            # Verify all languages are discovered
            for lang in languages:
                assert lang in discovered, f"Language {lang} not discovered"
            
            # Verify all frameworks are discovered for each language
            for lang in languages:
                for framework in frameworks:
                    assert framework in discovered[lang], \
                        f"Framework {framework} not discovered for language {lang}"
            
            # Verify get_discovered_frameworks returns all unique frameworks
            discovered_frameworks = manager.get_discovered_frameworks()
            assert len(discovered_frameworks) == len(frameworks), \
                f"Expected {len(frameworks)} frameworks, got {len(discovered_frameworks)}"
            
            for framework in frameworks:
                assert framework in discovered_frameworks, \
                    f"Framework {framework} not in discovered frameworks"
            
            # Verify no extra frameworks are discovered
            assert len(discovered_frameworks) == len(frameworks), \
                "Extra frameworks discovered that were not created"
