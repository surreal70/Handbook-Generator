"""
Property-Based Tests for CLI Framework Acceptance

Feature: compliance-framework-templates
Task: 10.3

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import sys
import pytest
from unittest.mock import patch
from hypothesis import given, settings, strategies as st

from src.cli import parse_arguments


class TestCLIFrameworkAcceptance:
    """Property-based tests for CLI framework acceptance."""
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from([
            'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
            'common-criteria', 'iso-9001', 'gdpr'
        ]),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_20_cli_framework_acceptance(self, framework, language):
        """
        Feature: compliance-framework-templates
        Property 20: CLI Framework Acceptance
        
        For any new compliance framework (pci-dss, hipaa, nist-800-53, tsc, 
        common-criteria, iso-9001, gdpr), the CLI SHALL accept the framework 
        name as a valid --template option without error.
        
        Validates: Requirements 10.7
        """
        test_args = [
            'cli.py',
            '--language', language,
            '--template', framework
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        # Verify the framework was accepted
        assert args.template == framework, \
            f"New framework '{framework}' should be accepted as valid template"
        assert args.language == language, \
            f"Language '{language}' should be accepted"
    
    @settings(max_examples=50)
    @given(
        framework=st.sampled_from([
            'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
            'common-criteria', 'iso-9001', 'gdpr'
        ])
    )
    def test_property_20_new_frameworks_with_all_languages(self, framework):
        """
        Feature: compliance-framework-templates
        Property 20: CLI Framework Acceptance (Language Independence)
        
        For any new compliance framework, the framework SHALL be accepted
        with both German and English language options.
        
        Validates: Requirements 10.7
        """
        for language in ['de', 'en']:
            test_args = [
                'cli.py',
                '--language', language,
                '--template', framework
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework, \
                f"Framework '{framework}' should work with language '{language}'"
            assert args.language == language
    
    @settings(max_examples=50)
    @given(
        framework=st.sampled_from([
            'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
            'common-criteria', 'iso-9001', 'gdpr'
        ])
    )
    def test_property_20_new_frameworks_with_short_flags(self, framework):
        """
        Feature: compliance-framework-templates
        Property 20: CLI Framework Acceptance (Short Flags)
        
        For any new compliance framework, the framework SHALL be accepted
        with short flag syntax (-l, -t).
        
        Validates: Requirements 10.7
        """
        test_args = [
            'cli.py',
            '-l', 'en',
            '-t', framework
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == framework, \
            f"Framework '{framework}' should work with short flags"
        assert args.language == 'en'
    
    def test_all_new_frameworks_accepted(self):
        """
        Unit test: Verify all new frameworks are accepted.
        
        Feature: compliance-framework-templates
        Validates: Requirements 10.7, 15.1
        """
        new_frameworks = [
            'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
            'common-criteria', 'iso-9001', 'gdpr'
        ]
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', framework
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework, \
                f"New framework '{framework}' should be accepted"
    
    def test_new_frameworks_appear_in_help(self, capsys):
        """
        Unit test: Verify new frameworks appear in help text.
        
        Feature: compliance-framework-templates
        Validates: Requirements 10.7, 15.1
        """
        test_args = ['cli.py', '--help']
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        # Help exits with code 0
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out.lower()
        
        # Verify all new frameworks appear in help text
        new_frameworks = [
            'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
            'common-criteria', 'iso-9001', 'gdpr'
        ]
        
        for framework in new_frameworks:
            assert framework in help_output, \
                f"New framework '{framework}' should appear in help text"
    
    def test_new_frameworks_in_error_message(self, capsys):
        """
        Unit test: Verify new frameworks appear in error messages for invalid input.
        
        Feature: compliance-framework-templates
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'invalid-framework-name'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit):
                parse_arguments()
        
        captured = capsys.readouterr()
        error_output = captured.err
        
        # Verify all new frameworks appear in error message
        new_frameworks = [
            'pci-dss', 'hipaa', 'nist-800-53', 'tsc', 
            'common-criteria', 'iso-9001', 'gdpr'
        ]
        
        for framework in new_frameworks:
            assert framework in error_output, \
                f"New framework '{framework}' should appear in error message"
