"""
Test automatic framework discovery for Phase 2 frameworks.

Verifies that Template_Manager discovers all seven new Phase 2 frameworks:
- ISO/IEC 38500
- ISO 31000
- CSA CCM
- TISAX
- SOC 1
- COSO
- DORA

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2025, 2026
"""

import pytest
from pathlib import Path
from src.template_manager import TemplateManager


class TestPhase2FrameworkDiscovery:
    """Test automatic discovery of Phase 2 frameworks."""
    
    def test_discover_all_phase2_frameworks(self):
        """
        Test that Template_Manager discovers all seven Phase 2 frameworks
        without requiring configuration updates.
        
        Validates: Requirements 6.1, 6.2
        """
        # Initialize TemplateManager with actual templates directory
        manager = TemplateManager(Path('templates'))
        
        # Discover all frameworks
        discovered_frameworks = manager.get_discovered_frameworks()
        
        # Phase 2 frameworks that should be discovered
        phase2_frameworks = [
            'iso-38500',
            'iso-31000',
            'csa-ccm',
            'tisax',
            'soc1',
            'coso',
            'dora'
        ]
        
        # Verify each Phase 2 framework is discovered
        for framework in phase2_frameworks:
            assert framework in discovered_frameworks, \
                f"Phase 2 framework '{framework}' not discovered automatically"
    
    def test_phase2_frameworks_in_both_languages(self):
        """
        Test that all Phase 2 frameworks are available in both German and English.
        
        Validates: Requirements 6.1, 6.2
        """
        manager = TemplateManager(Path('templates'))
        discovered = manager.discover_templates()
        
        phase2_frameworks = [
            'iso-38500',
            'iso-31000',
            'csa-ccm',
            'tisax',
            'soc1',
            'coso',
            'dora'
        ]
        
        # Verify each framework exists in both languages
        for framework in phase2_frameworks:
            assert 'de' in discovered, "German language directory not found"
            assert 'en' in discovered, "English language directory not found"
            
            assert framework in discovered['de'], \
                f"Framework '{framework}' not found in German templates"
            assert framework in discovered['en'], \
                f"Framework '{framework}' not found in English templates"
    
    def test_phase2_framework_directory_structure(self):
        """
        Test that Phase 2 frameworks have proper directory structure.
        
        Validates: Requirements 6.2
        """
        manager = TemplateManager(Path('templates'))
        
        phase2_frameworks = [
            'iso-38500',
            'iso-31000',
            'csa-ccm',
            'tisax',
            'soc1',
            'coso',
            'dora'
        ]
        
        for framework in phase2_frameworks:
            for language in ['de', 'en']:
                # Validate framework structure
                messages = manager.validate_framework_structure(framework, language)
                
                # Should have no critical errors (missing directory)
                critical_errors = [msg for msg in messages if 'not found' in msg.lower()]
                assert len(critical_errors) == 0, \
                    f"Framework '{framework}' has critical structure errors in {language}: {critical_errors}"
    
    def test_phase2_framework_configurations(self):
        """
        Test that all Phase 2 frameworks have proper configuration.
        
        Validates: Requirements 6.1, 6.7
        """
        manager = TemplateManager(Path('templates'))
        
        phase2_frameworks = {
            'iso-38500': {
                'display_name': 'ISO/IEC 38500',
                'min_template_count': 40
            },
            'iso-31000': {
                'display_name': 'ISO 31000',
                'min_template_count': 50
            },
            'csa-ccm': {
                'display_name': 'CSA CCM',
                'min_template_count': 80
            },
            'tisax': {
                'display_name': 'TISAX',
                'min_template_count': 60
            },
            'soc1': {
                'display_name': 'SOC 1 / SSAE 18',
                'min_template_count': 50
            },
            'coso': {
                'display_name': 'COSO',
                'min_template_count': 60
            },
            'dora': {
                'display_name': 'DORA',
                'min_template_count': 40
            }
        }
        
        for framework, expected_config in phase2_frameworks.items():
            config = manager.get_framework_config(framework)
            
            assert config is not None, \
                f"Framework '{framework}' has no configuration"
            
            assert config['display_name'] == expected_config['display_name'], \
                f"Framework '{framework}' has incorrect display name"
            
            assert config['min_template_count'] == expected_config['min_template_count'], \
                f"Framework '{framework}' has incorrect minimum template count"
            
            assert 'de' in config['languages'], \
                f"Framework '{framework}' missing German language support"
            
            assert 'en' in config['languages'], \
                f"Framework '{framework}' missing English language support"
            
            assert config['has_diagrams'] is True, \
                f"Framework '{framework}' should have diagrams support"
    
    def test_phase2_frameworks_in_supported_list(self):
        """
        Test that all Phase 2 frameworks are in SUPPORTED_FRAMEWORKS list.
        
        Validates: Requirements 6.1
        """
        manager = TemplateManager(Path('templates'))
        
        phase2_frameworks = [
            'iso-38500',
            'iso-31000',
            'csa-ccm',
            'tisax',
            'soc1',
            'coso',
            'dora'
        ]
        
        for framework in phase2_frameworks:
            assert framework in manager.SUPPORTED_FRAMEWORKS, \
                f"Framework '{framework}' not in SUPPORTED_FRAMEWORKS list"
